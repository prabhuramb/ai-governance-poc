"""
run_poc.py

Runs the full governance pipeline:
  1. Load candidate releases (one of which carries real Exhibit 23.6 data)
  2. Evaluate each against the pre-deployment gate (gate.py)
  3. Record evidence for each decision (evidence_log.py)
  4. Build the change-control log linking releases to prior versions (change_control.py)
  5. Validate: gate determinism, evidence retrievability, change-log
     completeness, and specifically that the regression case was blocked
     despite its higher accuracy.

Usage:
    python run_poc.py
"""

import json
from datetime import datetime, timezone

import gate
from evidence_log import EvidenceLog
import change_control


def main():
    with open("candidate_releases.json") as f:
        data = json.load(f)
    releases = data["releases"]

    log = EvidenceLog()
    decisions_by_version = {}

    print("Evaluating candidate releases against the pre-deployment gate...\n")
    for release in releases:
        decision = gate.evaluate_release(release)
        decisions_by_version[release["version_id"]] = decision
        log.record_evidence(release, decision)

        status = "AUTHORIZED" if decision["authorized"] else "BLOCKED"
        print(f"{release['version_id']}: {status}")
        if decision["reasons"]:
            for r in decision["reasons"]:
                print(f"    - {r}")

    change_log = change_control.build_change_log(releases, decisions_by_version)
    completeness = change_control.check_change_log_completeness(change_log, releases)

    # --- Validation ---
    print("\nValidating...")

    # 1. Gate determinism: re-run each evaluation, confirm identical decision.
    determinism_results = []
    for release in releases:
        is_deterministic, _ = gate.evaluate_release_deterministic_check(release)
        determinism_results.append(is_deterministic)
    all_deterministic = all(determinism_results)

    # 2. Evidence retrievability: every version_id must be retrievable with
    #    a complete record matching its original decision.
    retrievability_ok = 0
    for release in releases:
        entry = log.retrieve_by_version(release["version_id"])
        if entry is not None and entry["decision"]["authorized"] == decisions_by_version[release["version_id"]]["authorized"]:
            retrievability_ok += 1

    # 3. Change-log completeness: already computed above.

    # 4. Specific regression check: hardened-v3-regression must be BLOCKED
    #    despite having higher accuracy than hardened-v2.
    v2_decision = decisions_by_version.get("hardened-v2")
    v3_decision = decisions_by_version.get("hardened-v3-regression")
    v2_accuracy = next(r["metrics"]["accuracy"] for r in releases if r["version_id"] == "hardened-v2")
    v3_accuracy = next(r["metrics"]["accuracy"] for r in releases if r["version_id"] == "hardened-v3-regression")
    regression_correctly_caught = (
        v3_accuracy > v2_accuracy
        and v2_decision["authorized"] is True
        and v3_decision["authorized"] is False
    )

    validation = {
        "gate_decisions_deterministic": all_deterministic,
        "evidence_retrievable_count": f"{retrievability_ok} / {len(releases)}",
        "change_log_completeness": completeness,
        "regression_correctly_caught_despite_higher_accuracy": regression_correctly_caught,
    }

    print(f"Gate decisions deterministic across re-run: {all_deterministic}")
    print(f"Evidence retrievable: {retrievability_ok} / {len(releases)}")
    print(f"Change-log completeness: {completeness['with_complete_change_record']} / {completeness['non_initial_releases']} non-initial releases")
    print(f"Regression caught despite higher accuracy: {regression_correctly_caught}")

    final = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "thresholds": gate.THRESHOLDS,
        "decisions": decisions_by_version,
        "change_log": change_log,
        "validation": validation,
    }

    with open("results.json", "w") as f:
        json.dump(final, f, indent=2)

    log.save("evidence_log.json")

    print("\nFull results written to results.json")
    print("Evidence log written to evidence_log.json")


if __name__ == "__main__":
    main()

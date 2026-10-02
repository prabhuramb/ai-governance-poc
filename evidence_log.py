"""
evidence_log.py

Implements the Evidence retention and traceability control domain from
Exhibit 24.4's control matrix (row 3): retains the record needed to
determine what a release's evaluation found, on demand, retrievable
against a specific version.

The log is append-only within a run: record_evidence() adds an entry and
never removes or edits an existing one. retrieve_by_version() is the
traceability interface -- the thing an auditor would actually call.
"""

import json
from datetime import datetime, timezone


class EvidenceLog:
    def __init__(self):
        self._entries = []

    def record_evidence(self, release, decision):
        entry = {
            "version_id": release["version_id"],
            "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
            "change_description": release["change_description"],
            "metrics": release["metrics"],
            "decision": {
                "authorized": decision["authorized"],
                "reasons": decision["reasons"],
                "thresholds_applied": decision["thresholds_applied"],
            },
        }
        self._entries.append(entry)
        return entry

    def retrieve_by_version(self, version_id):
        for entry in self._entries:
            if entry["version_id"] == version_id:
                return entry
        return None

    def all_entries(self):
        return list(self._entries)

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self._entries, f, indent=2)

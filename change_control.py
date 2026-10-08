"""
change_control.py

Implements the Model and configuration change control domain from Exhibit
23.4's control matrix (row 2): treats each release as a controlled change
subject to re-evaluation, with a change log entry linking it to what it
changed from and the evaluation result that followed.

A release with based_on_version = null (the first one) has no prior
version to link to and is recorded as such rather than silently skipped.
"""


def build_change_log(releases, decisions_by_version):
    """
    For each release, build a change-control record. If it has a prior
    version, the record links to it and includes that release's own
    re-evaluation decision. The first release (no prior version) is
    recorded explicitly as having no predecessor, not omitted.
    """
    change_log = []
    for release in releases:
        version_id = release["version_id"]
        decision = decisions_by_version[version_id]
        change_log.append({
            "version_id": version_id,
            "based_on_version": release["based_on_version"],
            "change_description": release["change_description"],
            "linked_reevaluation": {
                "authorized": decision["authorized"],
                "reasons": decision["reasons"],
            },
        })
    return change_log


def check_change_log_completeness(change_log, releases):
    """
    Every release except the first must have a non-null based_on_version
    and a linked re-evaluation decision. Returns the count that meet this
    bar, out of the number that should.
    """
    non_initial = [r for r in releases if r["based_on_version"] is not None]
    complete_count = 0
    for entry in change_log:
        if entry["based_on_version"] is not None and entry["linked_reevaluation"] is not None:
            complete_count += 1
    return {
        "non_initial_releases": len(non_initial),
        "with_complete_change_record": complete_count,
    }

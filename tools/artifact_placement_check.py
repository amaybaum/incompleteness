#!/usr/bin/env python3
"""artifact_placement_check -- new verification artifacts stay out of the root.

The rule: new audits, preregistrations and results go under a programme or audit
directory, never at the `verification/` root.

The check is deliberately ONE-DIRECTIONAL. It fails on a root-level
`verification/*.md` that the migration manifest does not already account for; it
says nothing about manifest entries that are absent from the root. That is what
lets the same check survive the mechanical migration unchanged: once an artifact
moves to its destination, its manifest key stops resolving at the root and the
check neither notices nor cares.

The manifest is therefore the grandfather list, not an inventory.

Exit 0 when every root-level artifact is accounted for; 1 otherwise.
"""
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
VER = REPO / "verification"
MANIFEST = VER / "migration-manifest.json"

# Files whose home IS the root: the landing page, the strategic queue, and the
# manifest's own human-readable form.
ROOT_RESIDENTS = {"README.md", "ROADMAP.md", "MIGRATION-MANIFEST.md"}


def grandfathered():
    if not MANIFEST.exists():
        return None
    try:
        return set(json.loads(MANIFEST.read_text())["entries"])
    except (ValueError, KeyError) as e:
        print(f"artifact_placement_check: manifest unreadable: {e}")
        return None


def unaccounted(present, allowed):
    """The comparison itself, isolated so the self-test can drive it."""
    return sorted(present - (allowed | ROOT_RESIDENTS))


def offenders():
    allowed = grandfathered()
    if allowed is None:
        return None, None
    present = {p.name for p in VER.glob("*.md")}
    return unaccounted(present, allowed), len(allowed | ROOT_RESIDENTS)


def self_test():
    """The guard must actually bite, and must not bite the wrong things.

    Three cases, run against the real manifest through the real comparison:
    an unlisted root artifact is reported; a grandfathered one is not; and a
    manifest entry that has already been migrated away does not resurface as a
    complaint. The third is what keeps this check correct after the move."""
    allowed = grandfathered()
    if allowed is None:
        return False, "manifest missing or unreadable"
    probe = "ZZZ-PLACEMENT-SELF-TEST-DO-NOT-CREATE.md"
    if probe in allowed or probe in ROOT_RESIDENTS:
        return False, "self-test probe collides with a real entry"

    if probe not in unaccounted({probe}, allowed):
        return False, "an unlisted root artifact was not reported"

    grandfather = next(iter(allowed), None)
    if grandfather is not None and unaccounted({grandfather}, allowed):
        return False, "a grandfathered artifact was reported"

    if unaccounted(set(), allowed):
        return False, "a migrated-away manifest entry was reported"

    return True, ""


def main():
    ok, why = self_test()
    if not ok:
        print(f"artifact_placement_check: FAIL (self-test: {why})")
        return 1

    bad, allowed_count = offenders()
    if bad is None:
        print("artifact_placement_check: FAIL (migration manifest missing or unreadable)")
        return 1

    if bad:
        print("artifact_placement_check: FAIL -- new artifact(s) at the verification/ root:")
        for name in bad:
            print(f"    verification/{name}")
        print("  New audits, preregistrations and results belong under a programme or audit")
        print("  directory. See verification/MIGRATION-MANIFEST.md for the layout.")
        return 1

    print(f"artifact_placement_check: OK (no unaccounted root artifact; "
          f"{allowed_count} name(s) permitted, self-test passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

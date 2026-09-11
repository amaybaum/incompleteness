#!/usr/bin/env python3
"""Build the verification layout migration manifest, both forms.

Emits `verification/migration-manifest.json` (machine-readable, read by the
mechanical migration) and `verification/MIGRATION-MANIFEST.md` (the reviewable
table) from ONE mapping, so the two cannot disagree.

Three modes:

  (default)       render both artifacts and write them.
  --check         regenerate both in memory and compare against what is checked
                  in; exit 1 on any difference. Requires no particular layout on
                  disk, so it holds identically before and after the migration.
                  This is the mode the release gate runs, and it is what makes
                  "generated from one mapping" an enforced property rather than
                  a convention someone can quietly break by hand-editing.
  --verify-tree   additionally assert the mapping is in bijection with the
                  root-level artifacts. Meaningful only BEFORE the migration
                  runs -- afterwards the sources are gone from the root by
                  design -- so it is opt-in and is never a precondition of
                  rendering or of --check.
"""
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VER = ROOT / "verification"

TB = "programmes/oi-qm/track-b"
TI = "programmes/oi-qm/track-i"
OIQM = "programmes/oi-qm"

MAP = {}


def add(src, dst, note=""):
    assert src not in MAP, f"duplicate source {src}"
    MAP[src] = {"to": dst, "note": note}


# ---- programmes/oi-qm: the programme spine ----
add("OI-QM-RESEARCH-PROGRAMME.md", f"{OIQM}/PROGRAMME.md",
    "the programme spine; a thin README.md index is added beside it")
add("OI-QM-RESEARCH-PROGRAMME-AMENDMENT-1.md", f"{OIQM}/amendments/amendment-1.md")
add("OI-QM-RESEARCH-PROGRAMME-AMENDMENT-2.md", f"{OIQM}/amendments/amendment-2.md")

# ---- Track B: the Barandes correspondence route, act by act ----
add("BARANDES-INDIVISIBILITY-BRIDGE-AUDIT.md", f"{TB}/act-01-indivisibility/preregistration.md")
add("BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md", f"{TB}/act-01-indivisibility/result.md")
add("BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-AMENDMENT-3.md",
    f"{TB}/act-01-indivisibility/amendments/amendment-3.md",
    "amendments 1 and 2 are not separate root files; confirm during migration")
add("BARANDES-TRANSPOSE-BRIDGE-PREREGISTRATION.md", f"{TB}/act-02-transpose-bridge/preregistration.md")
add("BARANDES-TRANSPOSE-BRIDGE-RESULT.md", f"{TB}/act-02-transpose-bridge/result.md")
add("BARANDES-CANDIDATE-SELECTION-PREREGISTRATION.md",
    f"{TB}/act-03-candidate-selection/preregistration.md")
add("BARANDES-CANDIDATE-SELECTION-RESULT.md", f"{TB}/act-03-candidate-selection/result.md")
add("BARANDES-DILATION-MAPPING-PREREGISTRATION.md", f"{TB}/act-04-dilation-mapping/preregistration.md")
add("BARANDES-DILATION-MAPPING-RESULT.md", f"{TB}/act-04-dilation-mapping/result.md")
add("BARANDES-SOURCE-A-CANDIDATE-PREREGISTRATION.md",
    f"{TB}/act-05-source-a-candidate/preregistration.md")
add("BARANDES-SOURCE-A-CANDIDATE-RESULT.md", f"{TB}/act-05-source-a-candidate/result.md")
add("BARANDES-TUPLE-INSTANTIATION-PREREGISTRATION.md",
    f"{TB}/act-06-tuple-instantiation/preregistration.md")
add("BARANDES-TUPLE-INSTANTIATION-RESULT.md", f"{TB}/act-06-tuple-instantiation/result.md")
add("BARANDES-DILATION-CHOICE-PREREGISTRATION.md", f"{TB}/act-07-dilation-choice/preregistration.md")
add("BARANDES-DILATION-CHOICE-RESULT.md", f"{TB}/act-07-dilation-choice/result.md")
add("BARANDES-BOUNDARY-AUDIT.md", f"{TB}/boundary-audit/preregistration.md")
add("BARANDES-BOUNDARY-AUDIT-RESULT.md", f"{TB}/boundary-audit/result.md")
add("BARANDES-REPRESENTATION-FREEDOM-SCOPING.md", f"{TB}/representation-freedom-scoping.md",
    "a scoping note, not an act")

# ---- Track I: the internal reconstruction route ----
add("OI-ROOTED-CLASSIFICATION-AUDIT.md", f"{TI}/arc-b-rooted-classification/preregistration.md")
add("OI-ROOTED-CLASSIFICATION-RESULT.md", f"{TI}/arc-b-rooted-classification/result.md")
add("OI-QUANTUM-REPRESENTATION-AUDIT.md", f"{TI}/arc-c-quantum-representation/preregistration.md")
add("OI-QUANTUM-REPRESENTATION-AUDIT-AMENDMENT-1.md",
    f"{TI}/arc-c-quantum-representation/amendments/amendment-1.md")
add("OI-QUANTUM-REPRESENTATION-RESULT.md", f"{TI}/arc-c-quantum-representation/result.md")
add("OI-OPERATIONAL-SOURCING-AUDIT.md", f"{TI}/arc-d-operational-sourcing/preregistration.md")
add("OI-OPERATIONAL-SOURCING-AUDIT-AMENDMENT-1.md",
    f"{TI}/arc-d-operational-sourcing/amendments/amendment-1.md")
add("OI-OPERATIONAL-SOURCING-RESULT.md", f"{TI}/arc-d-operational-sourcing/result.md")
add("RECURRENCE-TIGHTNESS-AUDIT.md", f"{TI}/recurrence-tightness/preregistration.md")
add("RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md",
    f"{TI}/recurrence-tightness/amendments/amendment-1.md")
add("RECURRENCE-TIGHTNESS-RESULT.md", f"{TI}/recurrence-tightness/result.md")
add("RECURRENCE-SCALING-AUDIT.md", f"{TI}/recurrence-scaling/preregistration.md")
add("RECURRENCE-SCALING-RESULT.md", f"{TI}/recurrence-scaling/result.md")
add("CAUSAL-READBACK-DISCOVERY-AUDIT.md", f"{TI}/causal-readback-discovery/preregistration.md")
add("CAUSAL-READBACK-DISCOVERY-AMENDMENT-1.md",
    f"{TI}/causal-readback-discovery/amendments/amendment-1.md")
add("CAUSAL-READBACK-DISCOVERY-RESULT.md", f"{TI}/causal-readback-discovery/result.md")
add("CAUSAL-READBACK-DISCOVERY-RESULT-AMENDMENT-1.md",
    f"{TI}/causal-readback-discovery/amendments/result-amendment-1.md")

# ---- programmes/substratum ----
add("SUBSTRATUM-INTERFACE-AUDIT.md", "programmes/substratum/interface-audit.md")
add("SUBSTRATUM-SOURCE-AUDIT.md", "programmes/substratum/source-audit.md")
add("FROZEN-SUBSTRATUM-SOURCING-AUDIT.md", "programmes/substratum/frozen-sourcing-audit.md")
add("MANUSCRIPT-AXIOM-AUDIT.md", "programmes/substratum/manuscript-axiom-audit.md",
    "the A1-A6 audit; the A6 roadmap row points here")
add("PRIMITIVE-SOURCE-AUDIT.md", "programmes/substratum/primitive-source-audit.md")
add("ROUTE-B-AUDIT.md", "programmes/substratum/route-b-audit.md",
    "Route B of the substratum programme; unrelated to OI-QM Track B")

# ---- programmes/hydrodynamics ----
add("OI-HYDRODYNAMICS-SINGULARITY-RESEARCH-PROGRAMME.md",
    "programmes/hydrodynamics/PROGRAMME.md")

# ---- audits/foundations: kernel-facing structural audits ----
for name, dst in [
    ("C5-DISCOVERY-AUDIT.md", "c5-discovery-audit.md"),
    ("COHERENT-CONTINUUM-SOURCE-AUDIT.md", "coherent-continuum-source-audit.md"),
    ("DERIVED-Q3-AUDIT.md", "derived-q3-audit.md"),
    ("Q3-PROPAGATION-AUDIT.md", "q3-propagation-audit.md"),
    ("EXEC-SOURCE-AUDIT.md", "exec-source-audit.md"),
    ("FLOW-ENDPOINT-AUDIT.md", "flow-endpoint-audit.md"),
    ("FLOW-EXTENSION-AUDIT.md", "flow-extension-audit.md"),
    ("LIFT-AUDIT.md", "lift-audit.md"),
    ("LIFT-SOURCE-AUDIT.md", "lift-source-audit.md"),
    ("PHASE-SOURCE-AUDIT.md", "phase-source-audit.md"),
    ("PHASE-PROPAGATION-AUDIT.md", "phase-propagation-audit.md"),
    ("POLARIZATION-CLOSURE-AUDIT.md", "polarization-closure-audit.md"),
    ("SCALAR-CLOSURE-AUDIT.md", "scalar-closure-audit.md"),
    ("MINIMAL-REPERTOIRE-AUDIT.md", "MINIMAL-REPERTOIRE-AUDIT.md"),
    ("PAIR-FLOW-EQUIVALENCE-AUDIT.md", "pair-flow-equivalence-audit.md"),
    ("REAL-PAIR-FLOW-AUDIT.md", "real-pair-flow-audit.md"),
    ("STATE-MIXING-COUPLING-AUDIT.md", "state-mixing-coupling-audit.md"),
    ("INVERSE-CLAUSE-AUDIT.md", "inverse-clause-audit.md"),
    ("OI-CORE-FORWARD-REDUNDANCY.md", "oi-core-forward-redundancy.md"),
    ("C1C4-MINIMALITY-AUDIT.md", "C1C4-MINIMALITY-AUDIT.md"),
]:
    note = ("filename carries a term this programme does not use in new prose; "
            "the FILENAME is preserved unchanged rather than renamed"
            if dst == name else "")
    add(name, f"audits/foundations/{dst}", note)

# ---- audits/operational ----
for name, dst in [
    ("INSTRUMENT-COMPLETION-AUDIT.md", "instrument-completion-audit.md"),
    ("INSTRUMENT-MIGRATION-AUDIT.md", "instrument-migration-audit.md"),
    ("INSTRUMENT-REALIZATION-AUDIT.md", "instrument-realization-audit.md"),
    ("DENSE-INSTRUMENT-BRIDGE-AUDIT.md", "dense-instrument-bridge-audit.md"),
    ("DISCRETE-COMPLETION-AUDIT.md", "discrete-completion-audit.md"),
    ("TYPED-COMPLETION-AUDIT.md", "typed-completion-audit.md"),
    ("QUASILOCAL-COMPLETION-AUDIT.md", "quasilocal-completion-audit.md"),
    ("COMPLETION-ASSUMPTION-AUDIT.md", "completion-assumption-audit.md"),
    ("MILESTONE-finite-quantum-instruments.md", "milestone-finite-quantum-instruments.md"),
    ("CENSUS-oi-compatible-theories.md", "census-oi-compatible-theories.md"),
    ("STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md", "stochastic-observer-interface-audit.md"),
    ("ROOTED-OBSERVER-FAMILY-SOURCING-AUDIT.md", "rooted-observer-family-sourcing/preregistration.md"),
    ("ROOTED-OBSERVER-FAMILY-SOURCING-AUDIT-RESULT.md", "rooted-observer-family-sourcing/result.md"),
    ("SOURCING-PROPAGATION-AUDIT.md", "sourcing-propagation-audit.md"),
]:
    add(name, f"audits/operational/{dst}")

# ---- audits/physical-realization ----
for name, dst in [
    ("C4-CAUSAL-READBACK-AUDIT.md", "c4-causal-readback/preregistration.md"),
    ("C4-CAUSAL-READBACK-AUDIT-AMENDMENT.md", "c4-causal-readback/amendments/amendment.md"),
    ("C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md", "c4-causal-readback/amendments/amendment-1.md"),
    ("CONCRETE-CUT-AUDIT.md", "concrete-cut/preregistration.md"),
    ("CONCRETE-CUT-FREEZE.md", "concrete-cut/freeze.md"),
    ("CONTINUOUS-TIME-AUDIT.md", "continuous-time-audit.md"),
    ("CT3-R2B-Q2-PERIOD-AND-CYCLES.md", "ct3-r2b-q2-period-and-cycles.md"),
]:
    add(name, f"audits/physical-realization/{dst}")

# ---- audits/manuscript ----
for name, dst in [
    ("REPRESENTATION-SECTOR-AUDIT.md", "representation-sector-audit.md"),
    ("LEAN-MANUSCRIPT-CENSUS.md", "lean-manuscript-census.md"),
    ("OI-N-EXPLORATORY.md", "oi-n-exploratory.md"),
    ("OI-N-FREEZE.md", "oi-n-freeze.md"),
]:
    add(name, f"audits/manuscript/{dst}")

# ---- archive/superseded ----
# Resolved in owner review of 19d3506. The file self-identifies in its own
# header as a "Historical charter" that is "reconciled with, and superseded by,
# COMPLETION-ASSUMPTION-AUDIT.md". That supersession predates the strategic
# roadmap and is not caused by it: verification/ROADMAP.md is not what
# superseded this charter. The historical filename is preserved exactly, date
# included, because it is how the charter is cited.
add("EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md",
    "archive/superseded/EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md",
    "superseded by COMPLETION-ASSUMPTION-AUDIT.md per its own header; "
    "historical filename preserved exactly")

FLAGGED = {}

# ---- optional tree check: --verify-tree ----
# The mapping is in bijection with the root artifacts ONLY before the migration
# runs. Afterwards the sources are gone from the root by design, so this is an
# opt-in check used while the mapping is being built, never a precondition of
# rendering. `--check`, the gated mode, does not require it.
ROOT_RESIDENTS = {"README.md", "ROADMAP.md", "MIGRATION-MANIFEST.md",
                  "MIGRATION-RECORD.md"}

if "--verify-tree" in sys.argv:
    present = {q.name for q in VER.glob("*.md")} - ROOT_RESIDENTS
    missing = present - set(MAP)
    extra = set(MAP) - present
    if missing:
        print("UNCLASSIFIED root artifacts:", sorted(missing), file=sys.stderr)
    if extra:
        print("mapped but absent from tree:", sorted(extra), file=sys.stderr)
    if missing or extra:
        sys.exit("build_migration_manifest: mapping is not in bijection with the tree")

out = {
    "note": ("Proposed destinations for the mechanical migration PR. This file is "
             "navigation only: it moves nothing and changes no scientific content."),
    "base_commit": "e0c0c709620db0d114dbd7061975b6747cb7aabc",
    "root": "verification/",
    "count": len(MAP),
    "flagged": sorted(FLAGGED),
    "entries": {k: MAP[k] for k in sorted(MAP)},
}
JSON_TEXT = json.dumps(out, indent=2, ensure_ascii=False) + "\n"

# ---- the reviewable table, from the same mapping ----
import collections

groups = collections.OrderedDict()
for src, info in sorted(MAP.items()):
    dst = info["to"]
    key = "FLAGGED" if dst is None else "/".join(dst.split("/")[:-1])
    groups.setdefault(key, []).append((src, info))

order = sorted(k for k in groups if k != "FLAGGED")
if "FLAGGED" in groups:
    order.append("FLAGGED")

L = []
L.append("# Verification layout - migration manifest\n")
L.append("**This file moves nothing.** It records, for every artifact currently at the")
L.append("`verification/` root, where the mechanical migration will place it, so that the migration")
L.append("is a reviewable mapping rather than a judgement call made file by file while moving.\n")
L.append(f"Base commit: `{out['base_commit']}`. Artifacts classified: **{out['count']}**")
L.append("(plus `README.md`, `ROADMAP.md` and this file, which stay at the root). Flagged for owner")
L.append(f"decision: **{len(FLAGGED)}**.\n")
L.append("The machine-readable form is [`migration-manifest.json`](migration-manifest.json); the")
L.append("migration reads that, not this table. Both are emitted by")
L.append("`tools/build_migration_manifest.py` from one mapping, and the release gate runs that")
L.append("script in `--check` mode, so a hand-edit to either generated file fails CI rather than")
L.append("silently diverging.\n")
L.append("## Why the destinations are shaped this way\n")
L.append("Preregistration and outcome stay **together**, inside the round that produced them -")
L.append("`act-07-dilation-choice/preregistration.md` beside `act-07-dilation-choice/result.md` -")
L.append("rather than being split into global `preregistrations/` and `results/` folders. A reader")
L.append("arriving at a round should find the freeze, the outcome and any amendments in one place;")
L.append("that relationship is currently recoverable only by reading filenames.\n")
L.append("Amendments sit in an `amendments/` subdirectory of their own round, which keeps the")
L.append("append-only record legible as a sequence.\n")
L.append("**Filenames carrying vocabulary this programme does not use in new prose are preserved")
L.append("unchanged.** Renaming them would rewrite the historical record of what a round was called")
L.append("at the time, and the rule governs prose we write, not the names of artifacts already")
L.append("merged. Those rows are marked below.\n")
L.append("## What is NOT moving\n")
L.append("`lean/`, `lean-mathlib/` and `coverage/` stay exactly where they are. They are coherent")
L.append("technical subsystems with their own structure and their own roadmaps; the disorder this")
L.append("migration addresses is the research-control Markdown around them.\n")
L.append("## The mapping\n")

for key in order:
    if key == "FLAGGED":
        continue
    L.append(f"### `{key}/`\n")
    L.append("| Current | Destination | Note |")
    L.append("| --- | --- | --- |")
    for src, info in groups[key]:
        dst = info["to"].split("/")[-1]
        L.append(f"| `{src}` | `{dst}` | {info.get('note', '') or ''} |")
    L.append("")

if "FLAGGED" in groups:
    L.append("## Flagged for owner decision\n")
    L.append("Destinations this manifest does **not** decide. Each is a judgement about status, not")
    L.append("about layout, and guessing would bury the judgement in a mechanical change.\n")
    for src, info in groups["FLAGGED"]:
        why = info["note"].replace("FLAGGED FOR OWNER DECISION: ", "")
        L.append(f"- **`{src}`** - {why}")
    L.append("")

L.append("## Placement rule\n")
L.append("New audits, preregistrations and results go under a programme or audit directory, never at")
L.append("the `verification/` root (AGENTS.md §A.36). `tools/artifact_placement_check.py` enforces")
L.append("this in the release gate, treating this manifest as the grandfather list: any **new**")
L.append("root-level `verification/*.md` that is not in it fails.\n")

MD_TEXT = "\n".join(L)

# ---- mode dispatch ----
TARGETS = [(VER / "migration-manifest.json", JSON_TEXT),
           (VER / "MIGRATION-MANIFEST.md", MD_TEXT)]

if "--check" in sys.argv:
    # The enforced form of "generated from one mapping": regenerate both
    # artifacts in memory and compare against what is checked in. Needs no
    # root layout, so it holds after the migration exactly as it does before,
    # which is why this is the mode the release gate runs.
    drifted = []
    for path, want in TARGETS:
        if not path.exists():
            drifted.append(f"{path.name}: missing")
        elif path.read_text() != want:
            drifted.append(f"{path.name}: differs from the mapping")
    if drifted:
        print("build_migration_manifest --check: FAIL")
        for d in drifted:
            print(f"    {d}")
        print("  Both artifacts are generated from the MAP in this file. Edit the")
        print("  mapping and re-run `python3 tools/build_migration_manifest.py`;")
        print("  do not hand-edit either generated file.")
        sys.exit(1)
    print(f"build_migration_manifest --check: OK ({len(MAP)} artifacts; "
          f"both generated artifacts match the mapping)")
    sys.exit(0)

for path, textout in TARGETS:
    path.write_text(textout)
print(f"classified {len(MAP)} artifacts; {len(FLAGGED)} flagged for owner decision")
print("wrote migration-manifest.json and MIGRATION-MANIFEST.md")

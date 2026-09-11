#!/usr/bin/env python3
"""Build the verification layout migration manifest, both forms.

Emits `verification/migration-manifest.json` (machine-readable, read by the
mechanical migration) and `verification/MIGRATION-MANIFEST.md` (the reviewable
table) from ONE mapping, so the two cannot disagree.

Asserts that the mapping is in bijection with the root-level `verification/*.md`
artifacts: an artifact nobody classified fails the build, and so does a mapping
entry naming a file that is not there. Run it after adding a row.

Re-running it after the migration will fail the bijection assertion, which is
correct -- at that point the mapping is a historical record of a completed move
and `tools/artifact_placement_check.py` is what enforces placement.
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

# ---- flagged: destination is a judgement call, not a mechanical one ----
FLAGGED = {
    "EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md": {
        "candidates": [f"{OIQM}/equivalence-strengthening-roadmap.md",
                       "archive/superseded/equivalence-strengthening-roadmap-2026-09-05.md"],
        "why": ("a dated roadmap for the OI-QM equivalence. Whether verification/ROADMAP.md "
                "supersedes it or it remains a live programme document is an owner call, "
                "not something this manifest decides."),
    },
}
for name, info in FLAGGED.items():
    add(name, None, "FLAGGED FOR OWNER DECISION: " + info["why"])

# ---- completeness assertion ----
# The root residents are not migration candidates: the landing page, the
# strategic queue, and this manifest's own table. Kept in step with
# ROOT_RESIDENTS in tools/artifact_placement_check.py.
ROOT_RESIDENTS = {"README.md", "ROADMAP.md", "MIGRATION-MANIFEST.md"}
present = {p.name for p in VER.glob("*.md")} - ROOT_RESIDENTS
mapped = set(MAP)
missing = present - mapped
extra = mapped - present
if missing:
    print("UNCLASSIFIED root artifacts:", sorted(missing), file=sys.stderr)
if extra:
    print("mapped but absent from tree:", sorted(extra), file=sys.stderr)
assert not missing and not extra, "manifest is not in bijection with the tree"

out = {
    "note": ("Proposed destinations for the mechanical migration PR. This file is "
             "navigation only: it moves nothing and changes no scientific content."),
    "base_commit": "e0c0c709620db0d114dbd7061975b6747cb7aabc",
    "root": "verification/",
    "count": len(MAP),
    "flagged": sorted(FLAGGED),
    "entries": {k: MAP[k] for k in sorted(MAP)},
}
(VER / "migration-manifest.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

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
L.append("`tools/build_migration_manifest.py` from one mapping, so they cannot drift.\n")
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

(VER / "MIGRATION-MANIFEST.md").write_text("\n".join(L))
print(f"classified {len(MAP)} artifacts; {len(FLAGGED)} flagged for owner decision")
print("wrote migration-manifest.json and MIGRATION-MANIFEST.md")

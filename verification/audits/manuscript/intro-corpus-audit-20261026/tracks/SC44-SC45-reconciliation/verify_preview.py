#!/usr/bin/env python3
"""Bounded lexical guard for the SC-44/SC-45 reconciliation preview.

No physical proof is inferred from strings. Scientific review, proof_census,
coverage_check and full release gate are additional and independent requirements.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[6]
paper = (root / "papers/Substratum.md").read_text(encoding="utf-8")
ledger = json.loads((root / "verification/coverage/LEDGER.json").read_text(encoding="utf-8"))
entries = {row["id"]: row for row in ledger["entries"]}
failures = []

def need(yes, description):
    if not yes:
        failures.append(description)

need(paper.count("**Theorem 24** (Exact interface invariances and their different scopes)") == 1, "SC-45 narrowed theorem lost")
need(paper.count("**Proposition 24.2** (Fixed-carrier block-word rigidity)") == 1, "SC-44 proposition lost")
need("**Lemma 24.1**" not in paper, "Refuted lemma revived")
need("**Theorem 23** (Conditional local-branch reconstruction)" in paper, "Full-uniqueness Theorem 23 revived")
need("**Lemma 23.0** (Shared outputs on the selected local branch)" in paper, "Lemma 23.0 overstates global equivalence")
need("Each step (a)–(f) is an *if-and-only-if*" not in paper, "Unproved Stage-2 bidirectional chain revived")
need("unique up to $\\mathcal{G}_{\\text{sub}}$" not in paper, "Unscoped gauge-uniqueness statement revived")
need("hidden-factor relabelling" in paper, "Hidden-only invariance missing")
need("Adjoining an exactly decoupled ancillary dynamics" in paper, "Exact-decoupled invariant missing")
need("blockSpanning_of_wordTracesEqual" in paper and "WT3_spanning_iff" in paper, "Lean proof citations missing")
need("ST3_pairC" in paper and "ST4_pairC" in paper, "Pair-C negative scope missing")
need("same visible channel" in paper or "same visible CPTP channel" in paper or "identical channels" in paper, "Visible-law negative explanation missing")
need("a full group inclusion and projection" in paper.lower() or "full group inclusion and projection" in paper.lower(), "Unproved hierarchy scope missing")
need("This is an $|S|!$-element subgroup" not in paper, "False arbitrary-relabelling claim revived")
need("**Completeness depends on the observable carrier.**" in paper, "Carrier classification status missing")
need("**not** generate every fixed-interface coherent-channel equivalence" in paper, "Pair C fixed-interface non-exhaustiveness missing")
need("population equivalence" in paper and "all admissible observer partitions" in paper, "Population/all-partitions distinction lost")
need("observed inputs determine each other" not in paper.lower(), "Unproven bidirectional reconstruction revived")
need("finite-state recurrence and other statements not fixed by that law do not transfer" in paper, "Infinite ancillary recurrence scope lost")
need("**OPEN**" not in paper and "the former Lemma" not in paper, "Manuscript process voice revived")

a=entries.get("SUBSTRATUM:T-24")
b=entries.get("SUBSTRATUM:P-24.2")
need(a is not None and a["kernel"] == "GAP", "Theorem 24 must not be certified as full kernel theorem")
need(b is not None and b["kernel"] == "K3", "Proposition 24.2 kernel grade missing")
need("SUBSTRATUM:L-24.1" not in entries, "Retired lemma ledger row revived")
if b:
    names={n for c in b.get("checks",[]) if c["kind"]=="lean" for n in c.get("names",[])}
    need({"WT2gen_oneSided","WT3_spanning_iff","trace_wordEval_hiddenConjugate"}.issubset(names), "Both Lean directions not retained")

census = json.loads((root / "verification/lean-manuscript-census.json").read_text(encoding="utf-8"))
for name in ("Substratum Lemma 24.1 — the semigroup-transfer step (reconstruction)",
             "Substratum Lemma 24.1A — ST5 sufficiency, the word-trace kernel (reconstruction)"):
    families=[f for f in census["families"] if f["name"]==name]
    need(len(families)==1 and families[0]["status"]=="kernel-only", "Frozen research census family changed: "+name)

for issue in failures:
    print("FAIL",issue)
print("SC44-SC45 reconciliation lexical guard:", "PASS" if not failures else "FAIL",len(failures),"issues")
raise SystemExit(bool(failures))

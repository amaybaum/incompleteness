# SC-44 / SC-45 focused reconciliation — author draft, not a merge

**Review state:** unreviewed *preview* combining independently drafted SC-44 #980 and SC-45 #981. The individual PR branches remain unchanged. This document preserves evidence provenance but confers no publication or merge approval.

## Why this reconciliation is needed

The original four-generator completeness assertion in Substratum §4 used a false semigroup-transfer lemma (SC-44). Separately, the old generator (i) said arbitrary `|S|!` state relabellings preserve full observational data even with the visible/hidden partition fixed (SC-45), contradicted by an exact four-state counterexample. The old generator (iv) moved from coarse coupling-graph invariants to full observable equivalence without a valid bridge. The two corrections therefore meet at the *definition of the equivalence being classified*, not just at neighboring sentences.

The prior proof route and the observational gauge-group interpretation **cannot** be restored by simply composing their old wording. Two different mathematical claims survive: (i) fixed-interface hidden relabelling and exact finite decoupled enlargements preserve coherent channels under the stated priors; (ii) on a fixed carrier, equality of *all block-word traces* with full block spanning implies hidden-unitary conjugation, and conversely, as established in Lean. These do **not** establish a generator classification over all partitions, nor do they show that the required word-trace data are observed.

## Per-site reconciliation decisions

| Scope | SC-44 retained | SC-45 retained | Combined resolution |
|---|---|---|---|
| Substratum §4 opening / observable set | Need to name a group `G_sub` | Fixed readout and transported readout differ; channel and population data differ | Define the compared carriers and partition correspondence explicitly; full all-partitions gauge object remains unclassified |
| Theorem 24(i) | Original arbitrary relabelling in independent SC-44 branch is invalid | Hidden relabelling `(v,h)->(v,sigma(h))`, same sigma on all visible fibres, preserves coherent channel; four-state counterexample | Adopt SC-45, including exact counterexample and fixed-versus-transported distinction |
| Theorem 24(ii) | Alphabet-size change conditional | Structural q-insensitive results only | Preserve q-independent structural facts, *not* full channel equivalence |
| Theorem 24(iii) / corollary | Original exact decoupled transfer plus unqualified infinite-sector statement | Exactly independent **finite** hidden factor preserves coherent channel; slow coupling only approximate | Restrict exact theorem and corollary to finite decoupled factor; infinite factor needs separate state/measure |
| Theorem 24(iv) | Octahedral caveat but coarse graph language previously claimed full gauge | Growth/spectral/statistical invariants are not full channel equality | Retain only those named coarse invariants and the stricter cubic representation condition; no generic-graph full gauge claim |
| Lemma 24.1 | Withdraw false channel-family-to-dilation uniqueness | Same obstruction relevant to gauge definition | Do not reinstate old lemma or its proof |
| Proposition 24.2 | Lean-proved block-word rigidity with both directions and spanning scope | Compatible with fixed-interface channel invariances; **does not** follow from them | Preserve exact SC-44 proposition and Lean witnesses without promoting generator completeness |
| Lemma 23.0 / Theorem 23 | Direct references now use explicitly open exhaustiveness hypothesis | The set over which exhaustiveness is tested must itself be specified | Retain conditional local structural result; do not assert unqualified uniqueness modulo a completely classified gauge group |
| Gauge-hierarchy claims / synthesis | Some old 'image under trace-out' and nested group claims remain after SC-44 | Full generator (i) was false at fixed interface | Restate proposed hierarchy as a conjectured mapping; preserve separately proved SM commutant and Hamiltonian D-gauge |
| Paper Introduction / turtles | Interpretive aim remains | Hardware/simulation and coherent-channel distinctions matter | No ontological-regress closure, and no 'all hardware is gauge' claim; r32 to follow corrected corpus |
| Canonical coverage | SC-44 proposition `P-24.2` at K3 | SC-45 theorem `T-24` at GAP | Preserve both grades, verified Lean directions and unchanged frozen research-family census status |

## What was changed on this **preview branch**

The preview is based on the SC-44 draft branch, not on `main`. It integrates Theorem 24's SC-45 fixed-interface theorem and accompanying explanations and counters, retains SC-44's Proposition 24.2, and edits directly dependent Substratum passages. The coverage ledger carries SC-44's K3 proposition alongside SC-45's GAP theorem. The SC-45 four-state exact checker and its research README are copied byte-for-byte from its draft branch. `verify_preview.py` adds a fail-closed **lexical** non-regression check; it is not an independent scientific theorem checker.

Several prior overclaims elsewhere in the corpus remain **outside this preview**, including about 15 false or unsupported sites and about 35 stale dependent formulations identified by the earlier review. Those require the normal source-correction and Introduction reconciliation, not a blind replacement. The proposed hierarchy here has been scoped, but no claim is made that every sentence in the existing research corpus has been propagated yet.

## Review and CI gates before any landing

1. Scientific review of Theorem 24's exact hidden-conjugation channel proof and decoupled-factor proof, with independent counterexample replay, including the distinction between active fixed-interface and passive transported-interface observations.
2. Independent comparison of Proposition 24.2 with `WT2gen_oneSided`, `WT3_spanning_iff`, `trace_wordEval_hiddenConjugate`, `ST3_pairC`, `ST4_pairC`, `pairC_wordTraces`. Verify that the word-trace premise is not inferred from channel-family equality.
3. Verify Theorem 23's open completeness premise does not silently define its conclusion or substitute an assumed full-gauge quotient for a proved unique physical realization. Check §A.34 directional-citation rules for any surviving equivalence arrow.
4. Run `python3 -I verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC44-SC45-reconciliation/verify_preview.py`, `tools/proof_census.py --json`, `tools/coverage_check.py`, the manuscript/Lean census, the release gate and the required Lean axiom checks. Do not treat a previous unrelated green run as a check of the preview.
5. Rebuild `papers/Substratum.tex` and `papers/Substratum.pdf` with the repo's **canonical** `./build.sh Substratum` from the exact checked-out preview tree; inspect for dropped Unicode glyphs and verify the TeX source SHA stamp. The present preview does **not** contain regenerated artifacts.
6. Reconcile SC-43, sibling-PR overlaps and all Introduction r32 citations against the final reviewed Substratum wording. Independent exact-head acceptance and explicit owner approval are needed for any merge.

**New CI observation:** In an earlier SC-44 run the Lean-kernel job stopped at toolchain reporting, with an SSL error downloading Lean 4.35.0, before kernel checks. That is infrastructure evidence only, not a theorem failure or successful run. Also, generated artifacts remain stale until regenerated, so the release gate is not yet green.

**No merges authorized.**

## Second scientific finding: Theorem 23 local uniqueness exceeds its derivation

**F-23 — source-level correction in preview (not independently reviewed).** Theorem 23 and Lemma 23.0 formerly concluded uniqueness of the local propagating lattice/gauge residue **among all** E1–E7/A1–A6 models, modulo the four proposed gauge generators. Removing the false semigroup-transfer lemma leaves two logically independent gaps:

1. **Model selection.** Stage 2(b) proves its wave-rule result within a *nearest-neighbor, second-order* class, stronger than A3's bounded coupling. Stage 2(c) uses H-link and the selected branch (m=1). The octahedral representation, amplitude-scale gauge, H-spin', H-χ' and other [SM] hypotheses are additional branch inputs. The assertion that *each* Stage-2 item (a)–(f) is an iff has no proof; retaining that sentence would turn these branch-specific consequences into a uniqueness claim over all substrata.
2. **Equivalence-class completeness.** Even if two selected models share (d=3), (K=6), multiplicities ((3,2,1)), and the same conditional action-scale relation, equality of those **outputs** does not imply that the models are gauge-related. A complete observational gauge equivalence is not supplied by Theorem 24, and the stronger block-word theorem (Proposition 24.2) does not apply unless the word traces and spanning hypotheses are separately established.

**Source fix.** Theorem 23 is restricted to a conditional local-branch reconstruction, and Lemma 23.0 to shared **values of the branch's invariants** without substratum conjugacy. Stage 2's universal-if-and-only-if/uniqueness clause was removed, and direct introduction, status, remarks, schematic arrow, synthesis and conclusion claims were narrowed. The `SUBSTRATUM:T-23` and `SUBSTRATUM:L-23.0` coverage rows remain GAP (no formal proof of full reconstruction). Theorem 24 remains GAP; Proposition 24.2 alone is K3.

**Scientific-review challenges:** 
- Verify that no selected-branch hypothesis has been smuggled into an E/A assumption, and that all formulae and physical identifications inherited from [SM] retain their own conditions.
- Check whether any independent theorem proves a wider Stage-2 uniqueness class; if so, quote its exact hypotheses and revise this status accordingly—not by assertion.
- Decide whether keeping the `Theorem 23` label on a branch-relative synthesis is mathematically appropriate under the identifier policy, and whether the local statement deserves a more modest named status.
- Audit remaining book/Structure/Explainer mirrors, especially statements that the full gauge group projects onto the SM gauge group and claims that a unique physical substratum was reconstructed.
- Cross-check SC-43 turtles claims against this narrower causal/observable scope.

**CI classification (earlier preview head `053130e6`).** Mathlib bridge run `40643741304` failed while fetching Lean 4.33.0 with repeated TLS/SSL connection errors *before* the kernel tools ran. The resulting missing axiom reports are downstream infrastructure consequences, not counterexamples to the mathematics. The SC-44 `40642405124` toolchain failed downloading Lean 4.35.0. Neither failed run certifies the latest edited preview head. Exact-head tests, release gates and canonical Substratum TeX/PDF regeneration remain undone.

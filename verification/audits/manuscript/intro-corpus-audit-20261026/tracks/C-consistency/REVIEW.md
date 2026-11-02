# Independent review of Track C (REPORT.md) and STRUCTURE-1274.md

Reviewer: independent read-only agent. Base `main` at `a5168789`; Introduction at `4a260ca9`. REPORT.md's
line numbers are against `6bc2c4af`; only #951 landed between the two, with in-place single-line edits, so
the cited lines hold (spot-checked).

**Overall verdict: ACCEPT WITH CHANGES.**

## Per-finding verdicts

| ID | Verdict | Reason | Required changes |
|---|---|---|---|
| F-1 | SKIPPED (verdict); inventoried below | SC-16 investigation | inventory only |
| O-1 | CONFIRMED | SM:296 cites "chaotic mixing underlying operational measurement independence ([Main] §3.3)"; §3.3 (Main:354–424) has no mixing argument; Main:398–405 retains MI as a posit | replacement accurate (matches ch03:178 "may motivate"); regenerate SM |
| O-2 | CONFIRMED WITH CHANGES | glossary:107 = FULL:6707: error bound proved for exact-arithmetic registers, finite-b bound open (Main:562); `opglue_probes.py` :114–120/:161 converts TV to float with 1e-15 slack, so "certified in exact arithmetic" after a general theorem reads finite→universal | capacity replacement over-weakens: Main:570 gives an explicit fixed-point bound for b ≥ log₂(2K C_{d,R}); use "…an explicit fixed-point capacity bound whose dependence on the accuracy ε rests on the open finite-b bound"; edit glossary and FULL |
| O-3 | CONFIRMED | Main:560 "unnormalized digitized branch matrix" vs exact-ring registers (Main:562, :574) | theorem statement changes ⇒ update LEDGER fingerprint `MAIN:T-finite-operational-realization-gluing-form` in the same commit; regenerate Main |
| O-4 | CONFIRMED | Main:610 cites `memory_probes.py`: uniform priors only (:20–31), float MI (:72–79) | replacement fine |
| S-1 | CONFIRMED WITH CHANGES | "C3 follows from C4" at Main:72, :78, ch00:37 (FULL:273), ch01:133 (FULL:477), ch01:201 (FULL:545), ch07:30 (FULL:1909); Main:508/:608 and `c3_necessity` (C3Necessity.lean:80, no C4 hypothesis) make C3 unconditional for bijective realizations. Misleading dependency, not falsehood. Main:620 borderline | Main:78 kernel citation carries Main:604's scope ("for a joint law of history, present and hidden state; the time-t identification is on paper"); missed site Main:82 ("C1 and C3 follow as necessary diagnostics"); ch01:133 shares a line with an SC-16 edit — sequence them |
| S-2 | CONFIRMED (class larger) | Bell theorem (Main:368–377) needs (ii), (iii) d(B,R_A)>k_A, (iv) MI, ±1 every run; Main:22, :558, :646, :770, ch00:55, ch03:162, ch18:110, ch04:92, Methodology:411 drop some | FULL mirrors ch00:55↔FULL:291, ch03:162↔1038, ch18:110↔4928, ch04:92↔1211; missed sites below |
| S-3 | CONFIRMED WITH CHANGES (low) | REPORT quotes its proposed replacements, not main. Main reads :1180 "through C4 and finite recurrence for a fixed representative"; :1190 "from C4 plus a fixed finite reversible representative"; :1256 "only at recurrence scale from C4 plus a fixed finite reversible representative" — true sufficiency statements, under-reporting that C4 is unnecessary (Main:82, :141); :1180 arguably not defective | correct the quotes; :1256 match :1190 adding "and every non-deterministic visible step also supplies"; :1147 "which C4 readback supplies"; :1256 citation of §3.4 non-permutation-witness lemma correct (Main:431); regenerate Structure |
| U-1 | CONFIRMED WITH CHANGES (governed change) | `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon.lean:148) matches Main's definitions (`RootedRealization` shared prior, bijective step, CausalReadback.lean:178; `PDivisible` :54 all s<t≤K) | proposed parenthesis trips R7-RCH (edge_rigidity_probe.py:6659–6667; registry `manuscript == []` :6670; census "kernel-only" :6676) ⇒ governed guard/registry/census change (§A.35). K1 defensible, K2 debatable. Introduction L94/L211 present it as machine-checked while Main does not cite it — source/Introduction mismatch for #946 |
| U-2 | CONFIRMED WITH CHANGES | LEDGER note on `MAIN:T-intervention-dilation…` contradicts `lg_comb_probes.py` (rerun: ALL CHECKS PASS, K=3/2 exact) | replacement is finite→universal; use "…shows, on a qubit Leggett–Garg instance (K = 3/2), that the comb reproduces the quantum instrument outcome statistics exactly; the general reach is the theorem's, per finite instrument set (Main:478, :480)…"; fix stale line 460→476 |
| U-3 | CONFIRMED WITH CHANGES (optional) | Main:624 "neither is formalized" true of the two directions | append with joint-law / time-t caveat |
| D-1 | CONFIRMED WITH CHANGES | hidden-memory row K3 with empty delta vs Main:604; C3 row rests on same identification | reject "drop the caveat" (strengthening); K2 + delta for both rows |
| D-2 | CONFIRMED | 21 of 46 Main rows off by +16 | — |
| D-3 | CONFIRMED | no foundations probe runs in CI (verify.yml:209–264 runs only `verification/lean/*_probe.py`) | — |
| D-4 | CONFIRMED WITH CHANGES | Main:648, :724 attribute a mixing argument to §3.3; none exists in the corpus | :648 also neutralize "supported by the same chaotic-mixing suppression argument" → "may be motivated by" |
| D-5 | CONFIRMED | Main:578 "closed at the stated accuracy" vs :562, :596(4) | — |
| D-6 | CONFIRMED | Main:212 "before two cones meet" looser than cone lemma (Main:360) | — |
| D-7 | CONFIRMED | ε-form LEDGER assumptions omit exact-ring registers | — |
| D-8 | CONFIRMED | process-dilation row "no Lean statement" vs Main:516 `S_imp_D` (Equivalence.lean:422), `exists_perm_extending` (:60) | K1 + delta; also history-readback row ignores `isPermMatrix_of_stochastic_inverse` (Main:139) |
| I-1 | CONFIRMED WITH CHANGES | "(arbitrary priors" absent from Main; labels at Main:512/514 | "exact probe on one rational instance" understates the Theorem (`process_dilation_probes.py`, several targets, Main:516) |
| I-2 | CONFIRMED | Main:604, :608, :139 | — |
| I-3 | CONFIRMED | Main:608 | — |
| I-4 | CONFIRMED | class S-1 | — |
| I-5 | CONFIRMED | Main:141 | — |
| I-6 | CONFIRMED | Main:136 | — |
| I-7 | CONFIRMED | `RootedRealization.prior` | — |
| I-8 | CONFIRMED WITH CHANGES | Main:141 | "every representative whose law has a non-deterministic step" |
| I-9 | CONFIRMED WITH CHANGES | Intro L185 open problem (2) answered by Main:610 | time-t caveat on `c3_necessity_via_hidden` |
| I-10 | CONFIRMED | Main:608 | — |
| I-11 | CONFIRMED WITH CHANGES | Intro L136 drops (ii), (iii), ±1 | Main:398: gives up at least one of {(ii)+(iii) ontic parameter independence, (iv)} |
| I-12 | CONFIRMED | Main:576 "up to Θ(…)"; no lower bound | — |
| STR-1274 | CONFIRMED — same class as former Substratum :136, not a new scientific issue | process-level dilation attributed to matrix-scoped §3.2 lemma (Main:270); Main:634 refutes the all-time reading for one fixed finite substratum; P-indivisible restriction spurious (Main:427) | write "a finite deterministic bijection (depending on K)"; otherwise accurate (Main:512, :514; paper proof) |
| SUB-110 | CONFIRMED | Substratum:110 "(stochastic process → bijection)" | accurate; optionally separate §3.4 bullet; regenerate Substratum |

## Missed sites
1. Reverse-lemma root cause: Main:274 and appendix-b:46 = FULL:5813 call the matrix lemma "the correspondence at
   the stochastic-process level … both directions"; the uniform-prior converse holds only for doubly stochastic
   matrices.
2. S-2 Bell summaries: graph-cone form dropping (ii) and ±1 — ch01:169 (FULL:513), ch03:180 (FULL:1056), ch03:40
   (FULL:916), Explainer:338, Methodology:391, Structure:1149, SM:14 (±1 only); "MI + parameter independence"
   form dropping ±1 (lower priority) — ch01:183 (FULL:527), ch02:188 (FULL:831), appendix-c:42 (FULL:6288),
   glossary:49 (FULL:6649), Explainer:58, :665, :1017.
3. O-1/D-4: papers/main_repro/README.md:11 "chaotic-mixing diagnostics cited in the Bell section".
4. S-1: Main:82.

## Addendum: SC-16 site inventory (no replacements)
ASSERTS: GR:589; Explainer:892; ch01:121 = FULL:465; ch01:129 = FULL:473; ch01:133 = FULL:477 (second sentence);
appendix-b:420 = FULL:6187; ch04:178 = FULL:1297; Complexity:478; Complexity:503; #946-listed Complexity:418,
Explainer:294, ch17:178 = FULL:4757 (Explainer:767 is the selector item, not this class). New, same class:
Complexity:414; ch15:16 = FULL:3977; ch15:83 = FULL:4044; ch00:101 = FULL:337; SM:306 (SM:236 milder).
Borderline: appendix-b:92 = FULL:5859 (Theorem B.2.5); appendix-c:102 = FULL:6348; ch13:20 = FULL:3519;
ch17:192 = FULL:4771; GR:90; Explainer:280.
Related, not the same class: Substratum:128 (stipulated M1-T premise; C2 necessity from accessible
P-indivisibility).
Correctly scoped: Main:141, :174, :622, :706, :716; ch01:89; appendix-b:22, :457; Bioinformatics:14;
Medicine:13; Complexity:346; Explainer:351; GR:142; ch17:200 = FULL:4779.

## Addendum: Introduction at 4a260ca9 (papers/Introduction.md)
No sentence claims accessible-window P-indivisibility from C1–C4, C4, C2, backflow or the accessible-timescale
lemma. L12, L96 scope it to the recurrence cycle; L104 "Conditional memory does not force short-window
indivisibility (Appendix B)"; L174; L230–232 (B.2, XOR family). L84's backflow lemma is a CMI lower bound only.

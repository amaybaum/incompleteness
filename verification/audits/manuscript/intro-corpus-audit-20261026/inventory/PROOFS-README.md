# Proof inventory — audit step 1

Companion to `proofs.json`. This file says what each source contributed, lists the gaps, records early cross-consistency signals, and gives each statement's proof location. It judges nothing about the Introduction.

## Corpus commit and what was read where

- `corpus_commit`: `eae01647f50d9e2aa90957fbd6c59d8cf44e7681` (main after #939, "ħ framing and the θ₀ match"). The plan names `b64919cd`; the owner asked for #939's corrected statements, so the inventory is taken at `eae01647`.
- Read at `eae01647` (read-only `git archive` extraction): every `papers/*.md` and `book/*.md`, `verification/coverage/LEDGER.json`, `verification/ROADMAP.md`, `verification/lean-manuscript-census.json`, `verification/lean/`, `verification/lean-mathlib/OIBridge*`, and the `tools/` scripts that were run.
- Read from the worktree at `b64919cd`: `verification/programmes/**` (the retained `#print axioms` outputs). `.gitattributes` export-ignores that tree, and `git diff b64919cd eae01647` shows no change under it, nor under the Lean trees, `tools/`, ROADMAP or the registry.
- #939 changed, among the in-scope sources: `book/README.md`, `book/The-Incompleteness-of-Observation-FULL.md`, `book/appendix-a-prediction-status.md`, `book/appendix-b-derivations.md`, `book/appendix-c-objections.md`, `book/ch00-introduction.md`, `book/ch01-observation.md`, `book/ch02-substratum.md`, `book/ch03-structural-realism.md`, `book/ch04-methodology.md`, `book/ch05-gauge-structure.md`, `book/ch06-matter-content.md`, `book/ch07-gravity.md`, `book/ch08-juno.md`, `book/ch09-universality.md`, `book/ch12-evolution-intelligence.md`, `book/glossary.md`, `book/readers-guide.md`, `papers/Explainer.md`, `papers/GR.md`, `papers/Juno.md`, `papers/Main.md`, `papers/Methodology.md`, `papers/SM.md`, `papers/Structure.md`, `papers/Substratum.md`, `verification/coverage/LEDGER.json`. Every entry drawn from these files carries `read_at.changed_by_939: true`.

## What each source contributed

| Source | Contribution | Count |
|---|---|---|
| `tools/proof_census.py --json` | displayed statements in the seven core papers (bold head at line start) | 122 (Main 46, SM 39, GR 20, Structure 12, Substratum 5, Methodology 0, Juno 0) |
| manual scan of the core papers | displayed statements the census regex does not match (lower-case "theorem", italic heads, inline bold heads, Markdown headings, the two axioms) | 20 |
| `verification/coverage/LEDGER.json` | level, checks, delta, assumptions for each census row | 122 core rows: DEF 7, GAP 56, K1 1, K2 6, K3 23, P 28, SUM 1 |
| `verification/lean-manuscript-census.json` | kernel families and anchors; supersessions | 111 families, 16 supersessions; `tools/lean_manuscript_census.py` OK |
| Lean trees (`verification/lean-mathlib/OIBridge`, `verification/lean`) | cited `theorem`/`lemma` declarations, module:line, `#print axioms` status | 285 declarations (OIBridge 272, lean 13) |
| `verification/ROADMAP.md` | obligations and their status | 28 rows: outside the active queue long-range direction / programme record (not queued) ×9; queue CONDITIONAL ×3; queue OPEN ×12; settled negatively INDEPENDENT ×4 |
| `book/appendix-a-prediction-status.md` | prediction rows with class, layer, value, match | 64 rows (A.4.1 23, A.4.2 8, A.4.3 7, A.4.4 14, A.5 12) |
| `book/appendix-b-derivations.md` | displayed derivations, each paired with its paper statement where one exists | 31 statements, 26 paired |
| manuscripts and ROADMAP | named hypotheses and premises with definition site, status and users | 55 named hypotheses + the twelve-item posit ledger (Main §4.5) |

Appendix A's stated counts agree with the rows recounted from its tables: A.4.1 3 S + 7 C + 8 L + 1 M + 2 R + 2 E = 23; A.4.2 6 C + 2 L = 8; A.4.3 1 S + 1 C + 5 L = 7; A.4.4 12 S + 2 C = 14. SM §7.6 recounts to 22 rows = 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P, matching its "2 structural + 5 conditional structural" summary. Count differences between documents are listed under signal S9.

Kernel `#print axioms` status of the 285 cited declarations: #print axioms in source 272, no #print axioms 13. No cited declaration has a retained output in the repository; the retained outputs (88 declarations, all within {propext, Classical.choice, Quot.sound}) belong to research rounds the manuscripts do not cite. A `#print axioms` line in `OIBridge` is gated by `tools/lean_axiom_check.py`, which fails the build on any other axiom or `sorryAx`. No `axiom`, `sorry` or `native_decide` occurs in either tree.

## Gaps

1. **Statements with no ledger row: 20.** All are displayed statements the census regex does not recognise. The most consequential is Main's **Characterization theorem** (`papers/Main.md:516`, proof at `:608`), the central equivalence of the corpus. The others:
   - `papers/Main.md:38` Axiom 1 — inline bold mid-paragraph
   - `papers/Main.md:38` Axiom 2 — inline bold mid-paragraph
   - `papers/Main.md:360` Theorem (Bell ceiling for a screened local completion) — inline bold mid-paragraph
   - `papers/Main.md:466` Proposition (no uniform finite realization) — italic head
   - `papers/Main.md:516` Theorem Characterization theorem — bold head, lower-case "theorem" (census regex requires **Theorem
   - `papers/Main.md:538` Proposition (finite-substratum operational obstruction — classical-dimension form) — italic head
   - `papers/Main.md:556` Lemma Rounding Lemma (instrument-level, fixed-point dyadic model) — italic head
   - `papers/Main.md:556` Corollary (clipping and normalization) — italic head mid-paragraph
   - `papers/Main.md:560` Corollary (single controlled dynamics) — italic head
   - `papers/Main.md:574` Lemma (adaptive diamond telescoping) — italic head
   - `papers/Main.md:578` Corollary (finite-test density of deterministic realizations in operational quantum theory) — italic head
   - `papers/GR.md:677` Theorem (universality of the partition-geometry results) — italic head
   - `papers/SM.md:1416` Proposition (determination by (C,T)) — inline bold mid-paragraph
   - `papers/SM.md:1588` Theorem A.1 (Period formula) — Markdown heading
   - `papers/SM.md:1596` Theorem A.2 (Jordan-Chevalley decomposition) — Markdown heading
   - `papers/SM.md:1604` Theorem A.3 (q-independence of the Weil-Deligne conductor) — Markdown heading
   - `papers/SM.md:1620` Theorem A.4 (Additive decomposition over gauge irreps) — Markdown heading
   - `papers/Methodology.md:226` Axiom 1 — list item bold
   - `papers/Methodology.md:227` Axiom 2 — list item bold
   - `papers/Methodology.md:235` Theorem no-go (§5.5, the one rung that is not a lemma) — italic statement, no bold head
2. **Ledger rows whose paper line has moved: 61** (57 in the core papers; 4 in Explainer). Fingerprints all match, so the mapped text is current; only the recorded `line` is stale. Affected: every GR row from Bohr-frequency completeness onward and every SM row from the area-law lemma to Theorem 22 and its corollary. Each statement entry carries `ledger.line_moved`.
3. **Hypotheses used but never stated in a manuscript:** H-functor, H-tensor, H-pure-seed, H-readout, H-monoidal, H-∞, H-chi'. All are named only in verification records (ledger backlog notes, a ROADMAP row, or an ASCII spelling of H-χ'). Every named hypothesis that a manuscript uses has a definition site in the corpus.
4. **Defined hypotheses that no displayed statement names:** H-state, H-shell, H-energy, H-spectrum, H-balance, H-local-lift, H-orientation, H-top, H-det, H-observer-bundle, H-Y-vertex, Cond 2, Condition 1, amplitude-scale gauge. They condition prose results or prediction rows (strong CP, the native hypercharge reading of 1/α₀, the ħ calibration split, Condition 2), not bold-headed statements.
5. **Kernel anchors that do not resolve: none.** Every `(kernel: …)` citation, every registry anchor identifier and every ledger Lean check resolves to a declaration. `tools/lean_manuscript_census.py` passes at `eae01647`.
6. **Cited kernel declarations with no `#print axioms` anywhere: 13** — `OIBridge.card_mul_finrank_invariants @ verification/lean-mathlib/OIBridge/Averaging.lean:59`; `OIBridge.finrank_intertwiners @ verification/lean-mathlib/OIBridge/Averaging.lean:67`; `OIBridge.EquivalenceChain.permMatrix_pow @ verification/lean-mathlib/OIBridge/EquivalenceChain.lean:215`; `OIBridge.EquivalenceChain.permMatrix_mul_inv @ verification/lean-mathlib/OIBridge/EquivalenceChain.lean:224`; `Cubic.chi_consistent @ verification/lean/OI_Gauge_Certificates.lean:382`; `Cubic.irr_degrees @ verification/lean/OI_Gauge_Certificates.lean:420`; `Cubic.mult_V6 @ verification/lean/OI_Gauge_Certificates.lean:431`; `Rng.Staggered.factorization3 @ verification/lean/OI_Staggered_Relations.lean:335`; `Rng.Staggered.factorization4 @ verification/lean/OI_Staggered_Relations.lean:345`; `Rng.Staggered.factorization @ verification/lean/OI_Staggered_Relations.lean:458`; `Stag.susskind3 @ verification/lean/OI_Structural_Core.lean:389`; `Chiral.center_anticommutator @ verification/lean/OI_Structural_Core.lean:414`; `Chiral.mass_square @ verification/lean/OI_Structural_Core.lean:446`.
7. **Statements with no proof, or with a proof the paper says is not written: 4.**
   - `papers/Main.md:159` (fast bath erases readback) — No proof block; the bound is a direct iteration of the stated uniform-erosion premise. Probe evidence only (ledger P)
   - `papers/Main.md:242` (ancilla-marginal reformulation) — No proof of the stated equivalence; the coboundary special case is computed in the statement. Probe evidence only (ledger P)
   - `papers/GR.md:675` -level statement — papers/GR.md:679: "The proof is the §3–§6 derivations themselves ... A formal proof at the level of explicit theorem-style presentation has not been written out in this paper" (ledger GAP)
   - `papers/GR.md:677` (universality of the partition-geometry results) — Same as the preceding row: papers/GR.md:679 says no theorem-style proof is written; the §3–§6 derivations are cited as the proof
8. Methodology and Juno carry no census statements. Methodology's axioms and its §5.5 no-go are indexed as supplementary rows; Juno states its results in prose and tables, which enter through the predictions section.
9. Five Appendix B derivations have no displayed paper twin: B.4.1, B.4.2, B.6c.1, B.7.2, B.7.5b (see `appendix_b_statements[].paper_twin.note`).

## Early cross-consistency signals

Listed, not resolved. Each gives its sites; the anchor and the resolution belong to step 4.

- **S1 — Characterization theorem has no census/ledger row.** Main's "**Characterization theorem.**" (lower-case "theorem") is not matched by tools/proof_census.py (regex requires "**Theorem"), so the central equivalence has no LEDGER row; its supporting theorems (MAIN:T-finite-horizon-stochastic-reversible-unitary K3, MAIN:T-finite-horizon-process-dilation, MAIN:T-unavoidable-hidden-predictive-memory) do. Proof at papers/Main.md:608; the (ii)⟹(i) direction is imported under (T). Sites: `papers/Main.md:516`; `book/appendix-b-derivations.md:454`.
- **S2 — D-gauge completeness: H-BG premise status.** The theorem and book Lemma B.7.5 / Theorem B.7.5c are conditional on H-BG (global sign-aware classification). The kernel's unsigned premise BGIntegerClassification is refuted (GR:182, ROADMAP P2, ledger delta); kernel coverage is K1 (subresults only); the sign-aware replacement and its comparison with Bekir–Golomb are open. GR states this; the book Lemma B.7.5 states the phase-locking determination "up to the lemma's full gauge" under H-BG — check that every restatement (Main phase-locking, Appendix B) carries the open status, not only the hypothesis name. Sites: `papers/GR.md:178`; `papers/GR.md:182`; `book/appendix-b-derivations.md:426`; `book/appendix-b-derivations.md:444`; `verification/ROADMAP.md:1139`; `LEDGER GR:T-d-gauge-completeness-two-branch (K1)`.
- **S3 — Appendix B restatements that differ in scope or kind from the paper statement.** B.2.5 states CP-indivisibility "of the substratum dynamics (under C1–C4)"; Main states it "for the permutation-dilation family" (Main status ledger: fails for general CPTP families). B.6.2 states 6 = 3⊕2⊕1 for "the internal components" without the H-link qualifier that SM Theorem 7 attaches to the physical reading. B.7.1 "Partition relativity" is a different statement from Main's Lemma of that name (the canonical-measure uniqueness claim). B.6b.1 is a Lemma with a narrower content than SM Theorem 7b (no Cabibbo-uniqueness clause); B.6.1 is a Proposition, SM 6 a Theorem. Sites: `book/appendix-b-derivations.md:92 vs papers/Main.md:326`; `book/appendix-b-derivations.md:302 vs papers/SM.md:372`; `book/appendix-b-derivations.md:408 vs papers/Main.md:86`; `book/appendix-b-derivations.md:341 vs papers/SM.md:388`; `book/appendix-b-derivations.md:294 vs papers/SM.md:364`.
- **S4 — Appendix A empirical-match cells vs SM/ch06 numbers.** Row 6 Wolfenstein A "Within 1%" — SM/ch06 give 0.8165 vs 0.826 (1.2%, 0.8σ). Rows 13/N2 sin²θ13 "Within 1%" — SM/ch06/Juno give 0.02252 vs 0.02195±0.00056 (≈2.6%, 1.01σ). Row 21 m_b via Q_down "Within 1σ" — SM/ch06 give 4144 vs 4180±30 MeV (0.9%, i.e. 1.2σ by the quoted error). Row 1 1/α0 "Within ~0.5%" — ch06 §6.8 lists it as a structural input with no observed value; SM treats its native hypercharge reading as conditional on H-observer-bundle and H-Y-vertex. Sites: `book/appendix-a-prediction-status.md:75 (row 6)`; `book/appendix-a-prediction-status.md:82 (row 13)`; `book/appendix-a-prediction-status.md:128 (N2)`; `book/appendix-a-prediction-status.md:90 (row 21)`; `papers/SM.md:1261-1279`; `book/ch06-matter-content.md:298-312`.
- **S5 — Wolfenstein A sigma in Juno.** Juno: √(2/3) agrees with A = 0.826 ± 0.012 "at 0.23σ"; SM §7.6 gives 0.8σ (arithmetic (0.826−0.8165)/0.012 ≈ 0.79σ). Sites: `papers/Juno.md:140`; `papers/SM.md:1263`; `book/ch06-matter-content.md:298`.
- **S6 — sin²θ13 status in Juno.** Juno §5.1: "The formula for sin²θ₁₃ is fully derived"; Juno §6 and SM/appendix A classify it C (conditional on the emergent dressing of the Cabibbo identification). Sites: `papers/Juno.md:346`; `papers/Juno.md:395`; `papers/SM.md:1276`; `book/appendix-a-prediction-status.md:82`.
- **S7 — Internal SM numerical tables disagree.** SM:1317 compares sin²θ13 0.0225 with 0.0224 (0.4%) while SM:1276 uses 0.02195±0.00056 (1.01σ). SM:1316 lists A² = 0.6667 vs 0.683 as 1.2% (the A-level deviation; the A² deviation is ≈2.4%). SM:983-984 give m_e, m_μ at 1.2% (0.505, 104.4 MeV) beside SM:948-949 at 0.003%/0.002% — different constructions in different tables; labels should make the difference explicit. Sites: `papers/SM.md:1316-1317`; `papers/SM.md:1263`; `papers/SM.md:1276`; `papers/SM.md:983-984`; `papers/SM.md:948-949`.
- **S8 — m_μ in ch06 vs SM.** ch06:190 gives m_μ = 105.74 MeV (0.08%) via "Koide closure with the structural m_e/m_τ = 1/(36π⁴)"; ch06 §6.8 (:305) and SM (:949, :1270) give 105.656 MeV (0.002%) from (Q, θ0; m_τ). Same chapter, two values; the SM counterpart table (:948) has only the second. Sites: `book/ch06-matter-content.md:190`; `book/ch06-matter-content.md:305`; `papers/SM.md:949`; `papers/SM.md:1270`.
- **S9 — Prediction inventories and counts.** SM §7.6: 22 rows = 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P (rows recounted). Appendix A A.4.1: 23 rows = 3 S + 7 C + 8 L + 1 M + 2 R + 2 E (recounted; matches its stated count) — explained in-text as broader than SM's table (adds 1/α0, A·B, MOND a0, neutrino rows). ch06:12 says §6.8 "collects the twenty-two predictions" but the §6.8 table has 24 rows with a different row set (adds 1/α0, δ0, A·B, θ̄, m_d, m_u; omits α1(M_Z), Q_down, m_b/m_τ, m_u/m_d). ch07:321 counts "the ten entries in this chapter's table" while appendix A, preface, ch08, ch09, ch18, ch19 count "eight gravitational-sector entries" — two different gravitational inventories. Headline "twenty-two SM observables, two S and five C" is uniform across SM, Substratum, Structure, the book and FULL (FULL mirrors every chapter verbatim). Sites: `book/appendix-a-prediction-status.md:8`; `book/appendix-a-prediction-status.md:94`; `papers/SM.md:1255`; `papers/SM.md:1298-1300`; `book/ch06-matter-content.md:12`; `book/ch06-matter-content.md:289-314`; `book/ch07-gravity.md:292-303`; `book/ch07-gravity.md:321`.
- **S10 — Bijectivity: lemma or part-empirical.** Methodology §5.5 and §6.1 list determinism and bijectivity among the rungs that "follow as lemmas"; Methodology §4.4 and Main's posit ledger (iii) say the hidden-sector margin is closed with one empirical input, so bijectivity is part-empirical. The qualifier is present at the derivation and absent from the summary statements. Sites: `papers/Methodology.md:235`; `papers/Methodology.md:253`; `papers/Methodology.md:146`; `papers/Main.md:708`.
- **S11 — GR universality theorem without a written proof.** The "Theorem (universality of the partition-geometry results)" is displayed as a theorem; GR:679 says the theorem-style proof "has not been written out in this paper" and the claim is "established at that level" (the §3–§6 derivations). Ledger GAP. Sites: `papers/GR.md:675-679`.
- **S12 — Label collisions.** G1–G3 name both Main's phase-locking genericity conditions and GR's gravity levels. "Condition 2" (Juno) and "Cond 2" (SM) are the same relation under two spellings; Juno's Condition 1 has no SM counterpart name. Sites: `papers/Main.md:224 (G1)–(G3) genericity`; `papers/GR.md:12 G1–G3 gravity levels`; `papers/Juno.md:225 Condition 1/2`; `papers/SM.md:1046 Cond 2`.
- **S13 — Hypotheses named only in verification records.** H-functor, H-tensor, H-pure-seed, H-readout, H-monoidal (ledger backlog development notes) and H-∞ (ROADMAP obligation) are not stated in any manuscript; the ledger also spells H-χ' as H-chi'. Sites: `verification/coverage/LEDGER.json backlog[0].route`; `verification/ROADMAP.md P1 H-∞`.

## Proof location of every statement

Two cases are kept apart, as the owner asked: a proof that is **missing** (`none-located`, or `not-written` where the paper says so) and a proof that **lives outside the statement's paper** (`companion-paper`, `book-appendix`, `kernel-only`, `external-literature`). For a statement in Main, a proof in GR, SM, Substratum, Structure, Methodology, Appendix B or the kernel is support, not a gap. Categories: inline-proof 78, inline-argument 30, no-proof-obligation 12, elsewhere-in-paper 7, kernel-only 6, none-located 2, not-written 2, external-literature 2, inline-proof-sketch 2, companion-paper 1.

| Paper:line | Kind | Label / ledger id | Ledger | Proof location |
|---|---|---|---|---|
| `papers/Main.md:38` | Axiom | 1 (`no ledger row`) | — | **no-proof-obligation** — Axiom; indubitability argued inline at papers/Main.md:38 and in papers/Methodology.md §2 (outside Main) |
| `papers/Main.md:38` | Axiom | 2 (`no ledger row`) | — | **companion-paper** — Axiom (posit); its non-derivability from Axiom 1 is argued in papers/Methodology.md §5.2–§5.5 (outside Main); Main:38 states the countermodel claim without proof |
| `papers/Main.md:44` | Definition |  (`MAIN:D-unnamed-7c0166f8`) | DEF | **no-proof-obligation** — Definition |
| `papers/Main.md:48` | Lemma | 1 (`MAIN:L-1`) | K3 | **inline-argument** — Two-sentence argument following the statement at papers/Main.md:48 (finite-area boundary; holographic bound [2] cited); kernel proves it as a conditional with the physical premise as a hypothesis (Finiteness.finiteness, ledger K3) |
| `papers/Main.md:50` | Lemma | 2 (`MAIN:L-2`) | GAP | **inline-argument** — Definitional argument at papers/Main.md:50–54; no formal proof (ledger GAP) |
| `papers/Main.md:56` | Lemma | 3 (`MAIN:L-3`) | K3 | **elsewhere-in-paper** — Remark at papers/Main.md:62 (record preservation, eventual-image argument) and posit ledger item (iii) at papers/Main.md:708; fuller rung analysis in papers/Methodology.md §4.4 (outside Main); kernel CanonicalMeasure.determinism_reversibility_selected_measure (ledger K3) |
| `papers/Main.md:82` | Theorem | statement (`MAIN:T-statement`) | SUM | **no-proof-obligation** — Summary of results proved elsewhere in Main (§2.3, §3.2, §3.4) — ledger SUM |
| `papers/Main.md:86` | Lemma | (partition-relativity under the canonical invariant measure) (`MAIN:L-partition-relativity-under-canonical-invariant`) | GAP | **inline-proof** — Proof at papers/Main.md:88 |
| `papers/Main.md:115` | Theorem |  (`MAIN:T-unnamed-182a6975`) | P | **inline-proof** — Proof at papers/Main.md:121 |
| `papers/Main.md:133` | Lemma | (stochastic inverse) (`MAIN:L-stochastic-inverse`) | K3 | **inline-proof** — Proof at papers/Main.md:135 |
| `papers/Main.md:137` | Theorem | (history readback + finite recurrence implies indivisibility) (`MAIN:T-history-readback-finite-recurrence-implies`) | P | **inline-proof** — Proof at papers/Main.md:139 |
| `papers/Main.md:159` | Lemma | (fast bath erases readback) (`MAIN:L-fast-bath-erases-readback`) | P | **none-located** — No proof block; the bound is a direct iteration of the stated uniform-erosion premise. Probe evidence only (ledger P) |
| `papers/Main.md:167` | Lemma | (accessible backflow from readback) (`MAIN:L-accessible-backflow-from-readback`) | P | **inline-proof** — Proof at papers/Main.md:170 |
| `papers/Main.md:206` | Lemma | (one-step ancilla dilation) (`MAIN:L-one-step-ancilla-dilation`) | K3 | **inline-proof** — Proof at papers/Main.md:208 |
| `papers/Main.md:224` | Lemma | (phase-locking) (`MAIN:L-phase-locking`) | P | **inline-proof** — Proof at papers/Main.md:226 |
| `papers/Main.md:242` | Lemma | (ancilla-marginal reformulation) (`MAIN:L-ancilla-marginal-reformulation`) | P | **none-located** — No proof of the stated equivalence; the coboundary special case is computed in the statement. Probe evidence only (ledger P) |
| `papers/Main.md:246` | Theorem | (ancilla-marginal phase-locking; certified block structures) (`MAIN:T-ancilla-marginal-phase-locking-certified`) | P | **inline-proof** — Proof at papers/Main.md:248 |
| `papers/Main.md:264` | Lemma | (permutation unitarity) (`MAIN:L-permutation-unitarity`) | K3 | **inline-proof** — Proof at papers/Main.md:266 |
| `papers/Main.md:270` | Lemma | (Reverse direction, scoped) (`MAIN:L-reverse-direction-scoped`) | P | **inline-proof** — Proof at papers/Main.md:272 |
| `papers/Main.md:282` | Theorem | (Born-form representation of the transition probabilities) (`MAIN:T-born-form-representation-transition-probabilities`) | P | **inline-proof** — Proof at papers/Main.md:284 |
| `papers/Main.md:294` | Lemma | 1 (boundary bound) (`MAIN:L-1-boundary-bound`) | K3 | **inline-proof** — Proof at papers/Main.md:296 |
| `papers/Main.md:300` | Lemma | 2 (channel normal form) (`MAIN:L-2-channel-normal-form`) | GAP | **inline-proof** — Proof at papers/Main.md:306 |
| `papers/Main.md:308` | Theorem | (separability threshold) (`MAIN:T-separability-threshold`) | K3 | **inline-proof** — Proof at papers/Main.md:310 |
| `papers/Main.md:312` | Corollary | 1 (`MAIN:C-1`) | GAP | **inline-argument** — "Immediate from Lemma 2 and the Theorem" with the one-line argument on the statement line papers/Main.md:312 |
| `papers/Main.md:314` | Corollary | 2 (`MAIN:C-2`) | GAP | **inline-proof** — Proof at papers/Main.md:316 |
| `papers/Main.md:322` | Lemma | (diagonal preservation) (`MAIN:L-diagonal-preservation`) | K3 | **inline-proof** — Proof at papers/Main.md:324 |
| `papers/Main.md:326` | Theorem | (CP-indivisibility, framework scope) (`MAIN:T-cp-indivisibility-framework-scope`) | P | **inline-proof** — Proof at papers/Main.md:328 |
| `papers/Main.md:360` | Theorem | (Bell ceiling for a screened local completion) (`no ledger row`) | — | **inline-proof** — Proof at papers/Main.md:373 |
| `papers/Main.md:394` | Corollary | (Bell–lattice obstruction and state-dependent escape) (`MAIN:C-bell-lattice-obstruction-state-dependent`) | GAP | **inline-argument** — Argument inside the statement paragraph papers/Main.md:394, relying on [SM §3.1–§3.2]; no separate proof block (ledger GAP) |
| `papers/Main.md:415` | Lemma | (non-permutation witness) (`MAIN:L-non-permutation-witness`) | P | **inline-proof** — Proof at papers/Main.md:417 |
| `papers/Main.md:433` | Theorem | (C2 necessity, quantitative mixing form) (`MAIN:T-c2-necessity-quantitative-mixing-form`) | P | **inline-proof** — Proof at papers/Main.md:439 |
| `papers/Main.md:447` | Theorem | (physical memory: C2, process form) (`MAIN:T-physical-memory-c2-process-form`) | P | **inline-proof** — Proof at papers/Main.md:451 |
| `papers/Main.md:460` | Theorem | (intervention dilation: the finite classical action-labelled comb) (`MAIN:T-intervention-dilation-finite-classical-action`) | P | **inline-proof** — Proof (construction) at papers/Main.md:462 |
| `papers/Main.md:466` | Proposition | (no uniform finite realization) (`no ledger row`) | — | **inline-argument** — Counting argument closed with □ inside the statement paragraph papers/Main.md:466 |
| `papers/Main.md:472` | Proposition | (no horizon-independent intervened representation) (`MAIN:P-no-horizon-independent-intervened-representation`) | P | **inline-argument** — Dimension-count argument closed with □ inside the statement papers/Main.md:472; numerical thresholds at :474 (probe repconsistency_probes.py) |
| `papers/Main.md:484` | Theorem | (C3 necessity) (`MAIN:T-c3-necessity`) | K3 | **inline-proof** — Proof at papers/Main.md:488 |
| `papers/Main.md:492` | Corollary | (per-process capacity bound) (`MAIN:C-per-process-capacity-bound`) | P | **inline-argument** — Argument closed with □ inside the statement paragraph papers/Main.md:492; kernel citation at :494 (C3Necessity) |
| `papers/Main.md:496` | Theorem | (finite-horizon process dilation) (`MAIN:T-finite-horizon-process-dilation`) | P | **inline-proof** — Proof (constructive) at papers/Main.md:500 |
| `papers/Main.md:504` | Definition | (unitarily evolving QM) (`MAIN:D-unitarily-evolving-qm`) | DEF | **no-proof-obligation** — Definition |
| `papers/Main.md:510` | Lemma | (fixed-$\hat{H}$ form for realized processes) (`MAIN:L-fixed-hat-h-form-realized`) | P | **inline-proof** — Proof at papers/Main.md:512 |
| `papers/Main.md:516` | Theorem | Characterization theorem (`no ledger row`) | — | **elsewhere-in-paper** — Proof at papers/Main.md:608 (after the two supporting theorems, as announced at :524); the (ii)⟹(i) direction is imported from Barandes [11,12] under (T) |
| `papers/Main.md:526` | Theorem | (finite-horizon stochastic–reversible–unitary equivalence) (`MAIN:T-finite-horizon-stochastic-reversible-unitary`) | K3 | **inline-proof** — Proof at papers/Main.md:532 |
| `papers/Main.md:538` | Proposition | (finite-substratum operational obstruction — classical-dimension form) (`no ledger row`) | — | **inline-argument** — Inline argument closed with □ at papers/Main.md:538: the factorization half proved there, the unboundedness of the classical dimension imported from the literature |
| `papers/Main.md:544` | Theorem | (finite operational realization and gluing — ε-form) (`MAIN:T-finite-operational-realization-gluing-form`) | P | **elsewhere-in-paper** — Proof (construction and bound) at papers/Main.md:558, after the Rounding Lemma |
| `papers/Main.md:556` | Lemma | Rounding Lemma (instrument-level, fixed-point dyadic model) (`no ledger row`) | — | **elsewhere-in-paper** — Covered by the proof (construction and bound) at papers/Main.md:558 |
| `papers/Main.md:556` | Corollary | (clipping and normalization) (`no ledger row`) | — | **elsewhere-in-paper** — Covered by the proof at papers/Main.md:558 |
| `papers/Main.md:560` | Corollary | (single controlled dynamics) (`no ledger row`) | — | **inline-argument** — Construction closed with □ inside the statement papers/Main.md:560 |
| `papers/Main.md:574` | Lemma | (adaptive diamond telescoping) (`no ledger row`) | — | **inline-proof** — Proof at papers/Main.md:574 |
| `papers/Main.md:576` | Theorem | (uniform continuum realization — mutual ε-density) (`MAIN:T-uniform-continuum-realization-mutual-density`) | P | **inline-argument** — Proof closed with □ within the statement paragraph papers/Main.md:576; probe opglue_probes.py checks 8–9 |
| `papers/Main.md:578` | Corollary | (finite-test density of deterministic realizations in operational quan (`no ledger row`) | — | **inline-argument** — Argument closed with □ within the statement papers/Main.md:578 |
| `papers/Main.md:582` | Theorem | (unavoidable hidden predictive memory) (`MAIN:T-unavoidable-hidden-predictive-memory`) | K3 | **inline-proof** — Proof at papers/Main.md:590 |
| `papers/Main.md:600` | Theorem | (canonical predictive quotient — a purification ingredient, substratum (`MAIN:T-canonical-predictive-quotient-purification-ingredient`) | P | **inline-proof** — Proof at papers/Main.md:600 |
| `papers/Main.md:644` | Lemma | (rest-frame selection) (`MAIN:L-rest-frame-selection`) | GAP | **inline-proof** — Proof at papers/Main.md:646 |
| `papers/Main.md:648` | Corollary | (boost/rotation inequivalence) (`MAIN:C-boost-rotation-inequivalence`) | GAP | **inline-argument** — Argument in the statement paragraph papers/Main.md:648 from the rest-frame lemma (proof at :646); no formal proof (ledger GAP) |
| `papers/Main.md:730` | Theorem | (structural observer selection — conditional on (EM)) (`MAIN:T-structural-observer-selection-conditional-em`) | GAP | **inline-proof** — Proof at papers/Main.md:736 |
| `papers/Main.md:738` | Corollary | (anti-Boltzmann-brain) (`MAIN:C-anti-boltzmann-brain`) | GAP | **inline-argument** — Argument in the statement paragraph papers/Main.md:738 from the observer-selection theorem (proof at :736), conditional on (EM) |
| `papers/Main.md:740` | Corollary | (past-hypothesis replacement, with its rate condition) (`MAIN:C-past-hypothesis-replacement-rate-condition`) | GAP | **inline-argument** — Argument in the statement paragraph papers/Main.md:740, conditional on (EM) and a stated rate condition |
| `papers/GR.md:112` | Lemma | (Boundary-only dependence) (`GR:L-boundary-only-dependence`) | GAP | **inline-proof** — Proof at papers/GR.md:118 |
| `papers/GR.md:136` | Corollary | (deep-sector cardinality is gauge) (`GR:C-deep-sector-cardinality-gauge`) | GAP | **inline-proof** — Proof at papers/GR.md:138 |
| `papers/GR.md:172` | Theorem | (Bohr-frequency completeness) (`GR:T-bohr-frequency-completeness`) | K3 | **inline-proof** — Proof at papers/GR.md:174 |
| `papers/GR.md:178` | Theorem | (D-gauge completeness, two-branch form) (`GR:T-d-gauge-completeness-two-branch`) | K1 | **inline-proof** — Conditional proof at papers/GR.md:180 |
| `papers/GR.md:184` | Corollary | (operational antiunitary invariance) (`GR:C-operational-antiunitary-invariance`) | K2 | **kernel-only** — No paper proof; kernel citation in the following paragraph papers/GR.md:186 (ledger K2) |
| `papers/GR.md:188` | Corollary | (thermodynamic orientation) (`GR:C-thermodynamic-orientation`) | K2 | **kernel-only** — No paper proof block; argument sketched at papers/GR.md:190; kernel ThermalOrientation (ledger K2) |
| `papers/GR.md:198` | Theorem | (coherent-completion classification) (`GR:T-coherent-completion-classification`) | K3 | **kernel-only** — Proof is the kernel chain cited in the statement (OIBridge/JordanClassification.lean and matrix-unit chain), ledger K3; no paper proof |
| `papers/GR.md:204` | Theorem | (operational orientation no-go) (`GR:T-operational-orientation-no-go`) | K3 | **kernel-only** — Kernel citation in the statement (OrientationSelection.lean, OrientationClosure.lean), ledger K3; no paper proof |
| `papers/GR.md:218` | Theorem | (operational-completion characterization) (`GR:T-operational-completion-characterization`) | K3 | **kernel-only** — Kernel chain cited in the statement (krausSoundExt_of_validity_inert, compositeCompleteness, exactAll_of_levelOne, IsometryExtension), ledger K3; no paper proof |
| `papers/GR.md:422` | Corollary | (Invisible gravitational budget) (`GR:C-invisible-gravitational-budget`) | GAP | **inline-proof** — Proof at papers/GR.md:424 |
| `papers/GR.md:675` | Theorem | -level statement (`GR:T-unnamed-b09a495a`) | GAP | **not-written** — papers/GR.md:679: "The proof is the §3–§6 derivations themselves ... A formal proof at the level of explicit theorem-style presentation has not been written out in this paper" (ledger GAP) |
| `papers/GR.md:677` | Theorem | (universality of the partition-geometry results) (`no ledger row`) | — | **not-written** — Same as the preceding row: papers/GR.md:679 says no theorem-style proof is written; the §3–§6 derivations are cited as the proof |
| `papers/GR.md:729` | Theorem | A.1 (`GR:T-a.1`) | GAP | **inline-proof** — Proof at papers/GR.md:731 |
| `papers/GR.md:743` | Theorem | A.2 (`GR:T-a.2`) | GAP | **inline-proof** — Proof at papers/GR.md:745 |
| `papers/GR.md:749` | Corollary | A.3 (`GR:C-a.3`) | K2 | **inline-proof** — Proof at papers/GR.md:751 |
| `papers/GR.md:753` | Corollary | A.4 (`GR:C-a.4`) | GAP | **inline-proof** — Proof at papers/GR.md:755 |
| `papers/GR.md:759` | Theorem | A.5 (`GR:T-a.5`) | GAP | **inline-proof** — Proof at papers/GR.md:765 |
| `papers/GR.md:797` | Theorem | A.6 (`GR:T-a.6`) | GAP | **inline-proof** — Proof at papers/GR.md:801 |
| `papers/GR.md:811` | Theorem | A.7 (`GR:T-a.7`) | GAP | **inline-proof** — Proof at papers/GR.md:813 |
| `papers/GR.md:817` | Theorem | A.8 (`GR:T-a.8`) | GAP | **inline-proof** — Proof at papers/GR.md:827 |
| `papers/GR.md:845` | Theorem | A.9 (`GR:T-a.9`) | GAP | **inline-proof** — Proof at papers/GR.md:851 |
| `papers/SM.md:122` | Lemma |  (`SM:L-unnamed-ff7b7d06`) | GAP | **inline-proof** — Proof at papers/SM.md:124 |
| `papers/SM.md:126` | Lemma |  (`SM:L-unnamed-5e5c0ff4`) | GAP | **inline-proof** — Proof at papers/SM.md:128 |
| `papers/SM.md:140` | Lemma |  (`SM:L-unnamed-cb196ce9`) | GAP | **inline-proof** — Proof at papers/SM.md:142 |
| `papers/SM.md:210` | Corollary |  (`SM:C-unnamed-faf4656b`) | GAP | **elsewhere-in-paper** — Concluding corollary of the d = 3 selection argument in papers/SM.md §2 (preceding lines, forward filters E5/E6/E7, growth classification at :206–:209); no proof block (ledger GAP) |
| `papers/SM.md:224` | Lemma | (form of the center-free isotropic linear rule) (`SM:L-form-center-free-isotropic-linear`) | GAP | **inline-proof** — Proof at papers/SM.md:228 |
| `papers/SM.md:242` | Theorem | 1a (equivariant finite projection preserves spatial symmetry) (`SM:T-1a-equivariant-finite-projection-preserves-spatial`) | P | **inline-proof** — Proof at papers/SM.md:248 |
| `papers/SM.md:252` | Lemma | 1c (canonical projection and the resummed kernel) (`SM:L-1c-canonical-projection-resummed-kernel`) | P | **inline-proof** — Proof at papers/SM.md:254 |
| `papers/SM.md:258` | Corollary | 1a (cubic symmetry FORBIDS quadratic anisotropy) (`SM:C-1a-cubic-symmetry-forbids-quadratic-anisotropy`) | K3 | **inline-proof** — Proof at papers/SM.md:266 |
| `papers/SM.md:270` | Corollary | 1b (when the normalized adjacency is forced) (`SM:C-1b-when-normalized-adjacency-forced`) | P | **inline-argument** — Derivation displayed within the statement (:270–:274) with the remark at papers/SM.md:276; probe only (ledger P) |
| `papers/SM.md:278` | Theorem | 1 (conditional observer-level lattice Klein--Gordon branch) (`SM:T-1-conditional-observer-level-lattice-klein`) | GAP | **inline-argument** — Dispersion computed within the statement (:278–:282); no separate proof (ledger GAP) |
| `papers/SM.md:286` | Theorem | 2 (`SM:T-2`) | K2 | **external-literature** — Susskind [12]; kernel OI_Structural_Core (cancellation mechanism) — ledger K2; measure-reduction caveat at papers/SM.md:290 |
| `papers/SM.md:300` | Theorem | 3 (`SM:T-3`) | K2 | **inline-proof** — Proof at papers/SM.md:302 |
| `papers/SM.md:316` | Theorem | 4 (conditional observer-level mass spectrum) (`SM:T-4-conditional-observer-level-mass-spectrum`) | GAP | **inline-proof** — Proof at papers/SM.md:322 |
| `papers/SM.md:326` | Lemma | 4a (one cone on the branch) (`SM:L-4a-one-cone-branch`) | GAP | **inline-proof** — Proof at papers/SM.md:328 |
| `papers/SM.md:332` | Proposition | 4b (symmetric-point custodial scalarity for a component-complete site  (`SM:P-4b-symmetric-point-custodial-scalarity-component`) | GAP | **inline-proof** — Proof at papers/SM.md:334 |
| `papers/SM.md:338` | Theorem | 5 (condensate stabilizer, conditional physical reading) (`SM:T-5-condensate-stabilizer-conditional-physical-reading`) | P | **inline-proof** — Proof at papers/SM.md:340 |
| `papers/SM.md:352` | Lemma | 6a (operator-substitution control) (`SM:L-6a-operator-substitution-control`) | GAP | **inline-argument** — Display within the statement (:352–:356) is the argument; no formal proof (ledger GAP) |
| `papers/SM.md:364` | Theorem | 6 (conditional link-carrier count) (`SM:T-6-conditional-link-carrier-count`) | GAP | **inline-argument** — Statement closed with □: immediate from H-link (definition at papers/SM.md:358–:360); book Proposition B.6.1 restates it |
| `papers/SM.md:372` | Theorem | 7 (exact link representation; physical reading conditional) (`SM:T-7-exact-link-representation-physical-reading`) | K3 | **inline-proof** — Proof at papers/SM.md:374 |
| `papers/SM.md:388` | Theorem | 7b (`SM:T-7b`) | GAP | **inline-argument** — Two-part proof in the following text papers/SM.md:390 onward (no "*Proof.*" label); book Lemma B.6b.1 restates it as a lemma |
| `papers/SM.md:432` | Theorem | 8 (`SM:T-8`) | K3 | **inline-proof** — Proof at papers/SM.md:434 |
| `papers/SM.md:438` | Theorem | 8b (`SM:T-8b`) | GAP | **inline-proof** — Proof at papers/SM.md:444 |
| `papers/SM.md:446` | Theorem | 9 (`SM:T-9`) | P | **inline-proof** — Proof at papers/SM.md:448 |
| `papers/SM.md:452` | Corollary |  (`SM:C-unnamed-39abc017`) | GAP | **inline-argument** — Immediate reading of Theorem 9 under H-spin' (no proof block) |
| `papers/SM.md:454` | Theorem | 10 (`SM:T-10`) | GAP | **inline-proof** — Proof at papers/SM.md:458 |
| `papers/SM.md:462` | Theorem | 11 (`SM:T-11`) | GAP | **inline-proof** — Proof at papers/SM.md:464 |
| `papers/SM.md:533` | Theorem | 12 (`SM:T-12`) | P | **inline-proof** — Proof at papers/SM.md:535 |
| `papers/SM.md:541` | Theorem | 13 (`SM:T-13`) | P | **inline-proof** — Proof at papers/SM.md:543 |
| `papers/SM.md:573` | Theorem | 14 (`SM:T-14`) | GAP | **inline-proof** — Proof at papers/SM.md:575 |
| `papers/SM.md:579` | Theorem | 15 (`SM:T-15`) | GAP | **external-literature** — Anomaly conditions [18] and charge identification [16]; derivation reproduced in book appendix B.5 (Theorem B.5.1) |
| `papers/SM.md:583` | Corollary |  (`SM:C-unnamed-66dedb9a`) | GAP | **inline-argument** — Immediate from Theorem 15 (no proof block); book appendix B.5 has the corollary at appendix-b:280 |
| `papers/SM.md:587` | Theorem | 16 (`SM:T-16`) | K3 | **inline-proof** — Proof at papers/SM.md:589 |
| `papers/SM.md:609` | Theorem | 17 (`SM:T-17`) | K3 | **inline-proof** — Proof at papers/SM.md:611 |
| `papers/SM.md:617` | Theorem | 18 (`SM:T-18`) | GAP | **inline-proof** — Proof at papers/SM.md:619 |
| `papers/SM.md:625` | Theorem | 19 (`SM:T-19`) | K3 | **inline-proof** — Proof at papers/SM.md:627 |
| `papers/SM.md:631` | Proposition | 20 (`SM:P-20`) | GAP | **inline-proof** — Proof at papers/SM.md:633 |
| `papers/SM.md:635` | Theorem | 21 (`SM:T-21`) | GAP | **inline-proof** — Proof at papers/SM.md:637 |
| `papers/SM.md:1360` | Theorem | 22 (`SM:T-22`) | GAP | **inline-proof** — Proof at papers/SM.md:1362 |
| `papers/SM.md:1372` | Corollary |  (`SM:C-unnamed-235f5cba`) | GAP | **inline-argument** — Corollary of Theorem 22 (proof at papers/SM.md:1362); statement itself scopes C2/C4 as hypotheses |
| `papers/SM.md:1416` | Proposition | (determination by (C,T)) (`no ledger row`) | — | **no-proof-obligation** — Restatement of results proved in SM §4.5–§4.7, §5, §7: "carries no new proof burden" (papers/SM.md:1416) |
| `papers/SM.md:1588` | Theorem | A.1 (Period formula) (`no ledger row`) | — | **inline-argument** — Appendix theorem of SM with its derivation following the heading; mirrored as book Theorem B.3.1 |
| `papers/SM.md:1596` | Theorem | A.2 (Jordan-Chevalley decomposition) (`no ledger row`) | — | **inline-argument** — Appendix theorem of SM; mirrored as book Theorem B.3.2 |
| `papers/SM.md:1604` | Theorem | A.3 (q-independence of the Weil-Deligne conductor) (`no ledger row`) | — | **inline-argument** — Appendix theorem of SM; mirrored as book Theorem B.3.3 |
| `papers/SM.md:1620` | Theorem | A.4 (Additive decomposition over gauge irreps) (`no ledger row`) | — | **inline-argument** — Appendix theorem of SM; mirrored as book Theorem B.3.4 |
| `papers/Substratum.md:188` | Lemma | 23.0 (`SUBSTRATUM:L-23.0`) | GAP | **inline-proof** — Proof at papers/Substratum.md:190 |
| `papers/Substratum.md:192` | Theorem | 23 (`SUBSTRATUM:T-23`) | GAP | **inline-proof** — Proof at papers/Substratum.md:194 |
| `papers/Substratum.md:250` | Theorem | 24 (`SUBSTRATUM:T-24`) | GAP | **inline-proof** — Proof at papers/Substratum.md:260 |
| `papers/Substratum.md:262` | Corollary | (effective finiteness and gauge-class transfer) (`SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`) | GAP | **inline-argument** — Three-part argument closed with □ inside the statement papers/Substratum.md:262; no formal proof (ledger GAP) |
| `papers/Substratum.md:272` | Lemma | 24.1 (`SUBSTRATUM:L-24.1`) | GAP | **inline-proof-sketch** — Proof structure at papers/Substratum.md:274 |
| `papers/Structure.md:623` | Definition | 9.1 (`STRUCTURE:D-9.1`) | DEF | **no-proof-obligation** — Definition |
| `papers/Structure.md:628` | Definition | 9.2 (`STRUCTURE:D-9.2`) | DEF | **no-proof-obligation** — Definition |
| `papers/Structure.md:634` | Definition | 9.3 (`STRUCTURE:D-9.3`) | DEF | **no-proof-obligation** — Definition |
| `papers/Structure.md:637` | Definition | 9.4 (`STRUCTURE:D-9.4`) | DEF | **no-proof-obligation** — Definition |
| `papers/Structure.md:645` | Proposition | 9.5 (`STRUCTURE:P-9.5`) | GAP | **inline-proof-sketch** — Proof sketch at papers/Structure.md:647 |
| `papers/Structure.md:651` | Corollary | 9.6 (`STRUCTURE:C-9.6`) | GAP | **inline-argument** — Immediate from Proposition 9.5 (proof sketch at papers/Structure.md:647); explanation at :653; no formal proof (ledger GAP) |
| `papers/Structure.md:659` | Proposition | 9.7a (`STRUCTURE:P-9.7a`) | K3 | **inline-proof** — Proof at papers/Structure.md:664 |
| `papers/Structure.md:668` | Proposition | 9.7b (`STRUCTURE:P-9.7b`) | K3 | **inline-proof** — Proof at papers/Structure.md:672 |
| `papers/Structure.md:682` | Corollary | 9.8 (`STRUCTURE:C-9.8`) | K2 | **kernel-only** — No paper proof block; follows from Propositions 9.7a/9.7b (proofs at papers/Structure.md:664 and :672); kernel FactorUniqueness / Stinespring modules (ledger K2) |
| `papers/Structure.md:714` | Definition | 9.9 (`STRUCTURE:D-9.9`) | DEF | **no-proof-obligation** — Definition |
| `papers/Structure.md:724` | Proposition | 9.10 (`STRUCTURE:P-9.10`) | GAP | **inline-argument** — Self-described "a clarification rather than a deep result" (papers/Structure.md:726); no proof (ledger GAP) |
| `papers/Structure.md:728` | Corollary | 9.11 (`STRUCTURE:C-9.11`) | GAP | **inline-argument** — Immediate from Definitions 9.4 and 9.9, explanation at papers/Structure.md:730; no proof (ledger GAP) |
| `papers/Methodology.md:226` | Axiom | 1 (`no ledger row`) | — | **no-proof-obligation** — Axiom; indubitability argued in papers/Methodology.md §2.1 |
| `papers/Methodology.md:227` | Axiom | 2 (`no ledger row`) | — | **no-proof-obligation** — Axiom (posit); non-derivability argued in papers/Methodology.md §5.2–§5.5 |
| `papers/Methodology.md:235` | Theorem | no-go (§5.5, the one rung that is not a lemma) (`no ledger row`) | — | **elsewhere-in-paper** — Stated as the summary of papers/Methodology.md §4 (rung recoveries) and §5.2–§5.4 (six attempted derivations, status of succession); no formal proof |

## Method notes

- statements: tools/proof_census.py rows for the seven core papers, plus supplementary displayed statements the census regex does not see (source field says why)
- hypotheses_as_stated: clauses of the statement text beginning Let/Assume/Suppose/Under/If/Given/Fix/For every, or containing conditional on/under/assuming (extracted mechanically, up to six)
- named_hypotheses: named tokens found in the statement text or in the ledger assumptions field; ranges (A1–A6, (C1)–(C4), E1–E7, S1–S4) are expanded
- kernel_anchors: ledger lean checks resolved to module:declaration; (kernel: …) citations within the statement span; registry families whose anchor text lies in the span
- proof_location.category: inline-proof / inline-proof-sketch (a *Proof* block under the statement), inline-argument (argument in the statement paragraph or adjacent prose, no proof block), elsewhere-in-paper, companion-paper, book-appendix, kernel-only, external-literature, no-proof-obligation (definition, axiom, summary), not-written (the paper says the proof is not written out), none-located
- kernel: theorem/lemma declarations cited by a manuscript (any backticked identifier that resolves, and (kernel: …) groups), by the registry (anchors, supersessions) or by a ledger check; print_axioms reports #print axioms sites and any retained output
- The scripts that built `proofs.json` are in `scripts/proofs/`. They read the extracted tree and write nothing else.

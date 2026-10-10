# LOG — research/countermodels

Dated entries (UTC, from `date -u`), newest last. Every commit on this branch is recorded here with its purpose.

- 2026-10-10T19:56Z — thread branch created from checkpoint 4dc0321c (= L 9f9f8257 + research/archive); charter in README.md.
- 2026-10-10T20:06Z — session start (thread research/countermodels). Read in charter order: INTEGRATION-NOTE-STAGE4, INTEGRATION-NOTE-STAGE6 §2–§3, R6/REASSESSMENT (§1, §3, §7), T6/TEST §3, audit/X/AUDIT-X, X/RESULT, Y/RESULT, Z/RESULT, C5/RESULT; then U/RESULT (stage-3 definitions of K_F2), AUDIT-R §4 and its addendum, the I3 inventory records of the cone-dependent items, kernel CompositeDimension.lean (§A–§B, §K) and K2Guard.lean at L. Plan: C1 → C6 depth-first. Disclosure: one version check ran `python3 -I -B -c` (no bytecode written).
- 2026-10-10T20:28Z — C1 closed. `c1_cones.py`: run 1 69/70 (F2-C7: defect-image search silent for K_F2; my rule too narrow), kept as run1; run 2 (amended rule: the kernel chain phiW→idW; EC FCC for every c) 71/71 VERDICT C1-CONES-EXACT; replay identical (out 277d780e…). `c1_rows.py`: run 1 control 2 failed (parser read only CHECK lines), kept as run1; run 2 OUTCOME COVERING-CONFIRMED; replay identical (out b40a9d6c…). Result: both cones get R6's reference verdicts on all 199 rows (118/13/68); AUDIT-R §4 confirmed, with the T row decided here (FAILS for both: c = 15 vs 9). NOTES-C1.md, RESULTS rows C1.1–C1.7 written. Commit: C1.
- 2026-10-10T20:37Z — C2 closed. `c2_structure.py`: predictions written in NOTES-C2 S0 before run 1; run 1 14/16 (S4 tested outside its stated scope 𝒜; F encoded the prediction c = 11, which FAILED: actual 10), kept; run 2 16/16 but VERDICT text pre-written ("15/9/10/11") contradicting the measurement, kept; run 3 16/16 VERDICT C2-STRUCTURE-EXACT with measured verdict text, replay identical (out 85e70d79…). Results: local symmetry group 384 (96 unitary), closure with cnot 1536; extreme rays = defects ∪ Ĝ-reachable pure states; c ∈ {15, 9, 10}; Aut(K(Z_F)) = ℝ₊ × Ĝ [W + L]; non-uniqueness via K_circ (EXOTIC-E) and uniqueness over the reversed-simplex slice. RESULTS C2.1–C2.8. Commit: C2.
- 2026-10-10T20:46Z — C3 at a wall. `c3_transitivity.py` run 1 7/7 VERDICT C3-INGREDIENTS-EXACT (T2 homogeneous form fixed before the first run), replay identical (out 4b108c29…). EXCLUDES-ALL OPEN; proved: Lemma 1 (exposed face at P00 is PSD(3)-type for every K), Lemmas 2–3 (T fails for every exotic cone with finitely many non-PSD extreme rays, all Theorem-S surgery cones), Lemma 4 (compact case reduces to self-polar orbitopes on the pure-state sphere). Wall: exotic cones with a continuum of non-PSD extreme rays (EBF-only cones). No governed-round proposal. RESULTS C3.1–C3.5; C2.5's literature input relabelled [U]. Commit: C3.
- 2026-10-10T20:54Z — C4 closed on the Bell-type subfamily. `c4_bell_family.py` run 1 9/9 VERDICT C4-BELL-FAMILY-EXACT (pre-run edits only: B4 on C1 points, direct negative-direction witness, normalizer check as matrices, cnot-image max-entanglement in B1), replay identical (out 326217e0…). Pair theorem for every overlap; level-(i) five-stratum family; level (ii): K(Z_F) and K(Z_Y) = Ad(S⊗I)K(Z_F); with SWAP only K(Z_F). RESULTS C4.1–C4.4. Commit: C4.
- 2026-10-10T20:57Z — C5 closed. `c5_kappa_torus.py` run 1 8/8 VERDICT C5-KAPPA-TORUS-EXACT (one dead line removed before the run), replay identical (out f2a37059…). Explicit κ-invariant exotic cones at level (i) (C2 defects); at level (ii) and for the torus no exotic cone with finitely many non-PSD extreme rays; explicit level-(ii) κ / torus cones OPEN. RESULTS C5.1–C5.4. Commit: C5.
- 2026-10-10T20:59Z — C6 closed. `c6_handoff_checks.py` run 1 7/7 VERDICT C6-HANDOFF-CHECKS-EXACT (Groebner-remainder identity test adopted before the run), replay identical (out f6bb9573…). Handoff proposal HP1 written (KZ1–KZ12). Inbox empty: no received handoff to acknowledge. RESULTS C6.1–C6.2. Commit: C6.
- 2026-10-10T21:02Z — consistency pass: NOTES-C2 (c) gains the general argument for c = 9 / 10 on every pure extreme ray (Fubini–Study volume bound), RESULTS gains C3.6 (T fails for every explicitly known exotic cone). Deviations recorded for the final report: one `python3 -I -B -c` version check; R6's r2_cones.py / r4_tables.py read as structural templates (my scripts written anew, with the famI evaluation scheme and the class rules taken from them); the c1 EC-C9 all-c check added after run 1's records (disclosed in its header); no Lean dispatch. Commit: consistency pass.

## Round 2

- 2026-10-10T22:08Z — round 2 session start (head 54f79532, clean). Re-read README, LOG, RESULTS, NOTES-C1…C6; the
  coordinator's AUDIT-COUNTERMODELS.md and `indep_checkC.py` (its conventions: tables 4×4, index 0 the unit, `ipW` the
  entrywise sum, `z_s = (E00 + s1 E13 + s2 E22 − s1 s2 E31)/4`, `ψ_s` the −1/8-eigenvector of `pauliW(z_s)`) and
  OVERVIEW.md from `research/overview` @ 62cbb3cf (read-only). Round-1 rows independently confirmed 7/7; no label changes.
- 2026-10-10T22:08Z — **receipts** (overview 62cbb3cf), copied byte-identical into `inbox/` (sha256 equal to the
  originals): HO-1 v1 `f5a2e0da…`, HO-2 v1 `13abf306…`, HO-7 v1 `6931120d…`. Reliance, only at the labels the handoffs
  carry (nothing in them is CERTIFIED):
  - **HO-1 v1** (exact finite embedded-observer realization of K(Z_F), CONDITIONAL on branch (a)): not relied on by any
    round-2 node; recorded as context for C6/HP1 only (it is consistent with KZ5–KZ7: `S`, `cyc3`, `R_z(θ)` are not pair
    instruments there). No row of this thread will cite it as a premise.
  - **HO-2 v1**: relied on only for the statement of Conjecture B3.C (OPEN) and its partial results as named (the
    "if time remains" node); HO-2a–d enter no derivation here. Jordan / finite subgroups of SO(3) stay [L] and are not
    used.
  - **HO-7 v1**: item 1 (Ω₄) is the object of node C9. I use only its definition `{|x|⁴ + s⁴ ≤ 1}` and recompute every
    property I need (automorphisms, extreme points, faces) exactly here; its positive properties (drivability, seed,
    V4, Geom, capacity) are not relied on. Items 2–3 are not used.
- 2026-10-10T22:12Z — correction: commit d8a1461b also changed the wording of the 21:02Z entry ("consistency pass" → "consistency pass (round 1, …)"); restored to its original text here. Earlier entries are not edited.
- 2026-10-10T22:58Z — C7 (part 1). Scratchpad exploration (numerical, not evidence): the diagonal surgery K^Circ, the
  full-circle Bell surgery and Bell triples looked non-self-dual. NOTES-C7 S0 predictions written 22:41Z, before any
  exact run. `c7_ebf_wall.py` run 1 5/7 NO VERDICT (kept as run1): C1 failed on Float(0.0) from Python-int inputs (an
  exactness defect of my harness, caught by the check), CC-R stated a wrong slack identity (−Σp/2 instead of −Σp/2 − p_s;
  conclusion unchanged); run 2 8/8 `VERDICT C7-EBF-WALL-EXACT` with the guard EX (no Float), replay identical
  (out 43d18e5d…). Commit: C7 part 1.
- 2026-10-10T23:01Z — C7 part 2, C8, C9 exact runs. `c7_circle.py` (data from a scratchpad numerical search, rounded
  to rationals, disclosed in its header; two pre-run edits: the orthonormal completion in B5 and an exact determinant
  criterion in CC1) run 1 7/7 `VERDICT C7-CIRCLE-EXACT`, replay identical (out 983a6e86…). NOTES-C8 S0 written 23:04Z
  (sic: written before its script's first run; the timestamps in the S0 headers are the times the text was drafted, all
  before the runs recorded here); `c8_bell_sets.py` run 1 12/12 `VERDICT C8-BELL-SETS-EXACT`, replay identical
  (out d219d502…). NOTES-C9 S0 written 22:51Z; `c9_omega4.py` (one pre-run edit: header wording of CC1) run 1 12/12
  `VERDICT C9-OMEGA4-EXACT`, replay identical (out 88c5fc06…). Kernel citations TransitiveBody.lean:602 and
  DenseOrbit.lean:174 read at L. Commit: C7 part 2, C8, C9 scripts.

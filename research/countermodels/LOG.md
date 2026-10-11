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
- 2026-10-10T23:01Z — **provenance correction** (supersedes the "(sic …)" sentence of the 23:01Z entry, which is wrong). The
  clock times written into the round-2 S0 headers and script headers were my estimates, not `date -u` readings,
  although the script headers say "by date -u"; several are later than the runs they precede. The order S0 text →
  script → first run holds in every case, by file modification times (UTC): NOTES-C7 22:40:29, c7_ebf_wall run 1
  22:42:03–04, run 2 22:42:48; NOTES-C9 22:50:02, c9_omega4 (after its pre-run edit) 22:50:58, run 22:51:12;
  NOTES-C8 22:55:46, c8_bell_sets.py 22:56:56, run 22:57:10; c7_circle.py (after its pre-run edits) 22:59:14, run
  22:59:15. The stated header times (c7_ebf_wall 22:47Z and "RUN 2 22:52Z", c7_circle 23:02Z, c8 23:08Z, c9 22:53Z,
  NOTES-C8 23:04Z, NOTES-C9 22:51Z) are therefore not the times of record; the scripts are left unedited (they have been
  run), and each NOTES file carries a provenance note. All later timestamps in this LOG are `date -u` readings.
- 2026-10-10T23:04Z — C7, C8, C9 written up. NOTES-C7 (W1–W5, verdict: no explicit continuum cone; Theorem C7-D; fibres over Circ
  and over the simplex have ≥ 2 members by EBF; full Bell-circle surgery fails), NOTES-C8 (witness lemma, Theorem C8 for
  triples, Bell-circle sets and the W^⊥ class; Conjecture C8-C), NOTES-C9 (Aut(Ω₄) = O(3) × ℤ₂, orbits, c*, second
  order, polar). RESULTS rows C7.1–C7.7 (with C7.1f, C7.6f), C8.1–C8.4, C9.1–C9.7 appended; no earlier row changed.
  Handoff proposal HP2 (to equivalence via the coordinator). HO-7 relied on for the definition of Ω₄ only. Commit:
  round-2 write-up.
- 2026-10-10T23:11Z — optional node (B3.C, HO-2 v1). NOTES-C10 S0 written 23:08:08Z (`date -u`); `c10_b3c_case.py` run 1
  (23:09:07) stopped after K0–K3 with a TypeError in my facet-normalization helper, kept as run1; run 2 (23:09:18, helper
  only) 8/8 `VERDICT C10-B3C-CASE-EXACT`, replay identical (out ffc453bf…). Result: an explicit exotic cone for a case
  HO-2 lists as open, with its slice; the eigenline-orbit mechanism; residual region recorded. HO-2 relied on for the
  statement of B3.C and its coverage list only. RESULTS rows C10.1–C10.3 and C2.8r appended. Handoff proposal HP3 (to
  bridge via the coordinator). Commit: C10.

## Round 3

- 2026-10-10T23:48Z — round 3 session start (head e6d42cab, clean; first `date -u` reading of the session 23:48:10Z). Read
  README, RESULTS, LOG, NOTES-C1 … NOTES-C10; from `origin/research/overview` @ 2a055180 (fetched; read-only):
  OVERVIEW.md, HANDOFFS/README.md, HO-10, HO-11, HO-14, HO-16 and AUDITS/2026-10-10-round2/AUDIT-COUNTERMODELS-R2.md
  (no label changes to this thread's rows); AGENTS.md at L 9f9f8257 (§A.16, §A.21, §A.29, §A.31; byte-identical to
  the working copy, sha256 959c4333…); archive records used as definitions: PROTOCOL-STAGE3 (H1–H3), X/RESULT (SD1, the
  single-defect characterization, EBF), AUDIT-X, Y/RESULT Y1 (claim D, the seed window), INTEGRATION-NOTE-STAGE4.
  Disclosure: two version checks ran without `-I -B` (`python3 --version`; `python3 -c "import sympy; …"`, sympy
  1.14.0, Python 3.11.15), outside the repository.
- 2026-10-10T23:59Z — **receipts** (overview 2a055180), copied byte-identical into `inbox/` (sha256 equal to the
  originals, checked at 23:59:30Z): HO-10 v1 `ef909f69…`, HO-11 v1 `cd6305f6…`, HO-14 v1 `af4c4b63…`. Reliance, only
  at the labels the handoffs carry (none names a kernel declaration at L for what is used here, so nothing taken from
  them is CERTIFIED):
  - **HO-10 v1** (reachability theorem CONJECTURE; B3.C CONDITIONAL on claim (D) [A]): used in C13 only as the label
    under which the residual region of C10.3 is covered (existence, CONJECTURE + (D)); the unreachable state C13 needs
    is found and certified exactly here, so no row of this round rests on HO-10's item 1. Items 2–3 are cited, at their
    labels, wherever a C13 row compares with them.
  - **HO-11 v1**: item 3 (`Stab_loc(K(Z_F)) = V4`, exact among the Cliffords) is context for C11 (K(Z_F) is not
    invariant under the order-384 group); the `cyc3` witness is recomputed here, so no row rests on it. Items 1–2 are not
    used.
  - **HO-14 v1**: the group `⟨cnot, actT R_z(π/2), actT cyc3⟩` and the state `φ₀` are the object of C11; the order 384
    and the unreachability of `φ₀` (CONJECTURE, exhaustive) are recomputed with my own code before any use; the
    existence of an exotic invariant cone enters only at CONDITIONAL on claim D [A] (EBF [A]).
  Process note (2026-10-11T00:00Z): the first form of the receipts commit (local, never pushed, `f230bc04`) carried the
  three inbox files without this LOG entry (my LOG edit had failed); the entry was added to that commit before any
  push, with the same message. Receipts commit pushed as `43a49d57`.
- 2026-10-11T00:21Z — C11. Scratchpad exploration (numerical, not evidence; `/tmp/.../scratchpad/x11_*.py`, `x12_*.py`):
  the group's order, Bell-defect images, `φ₀`'s orbit (orthogonal pair found), a rounding search for seeds with no
  orthogonal pair in their orbit, a numerical pair test of the cap/co-cap criterion; a penalty-optimizer test of
  self-positivity of `K*` was insensitive (it missed a known witness) and is not used. NOTES-C11 S0 written 00:11:33Z
  (`date -u`), before the script. `c11_octahedral.py`: decision rule drafted 00:13:49Z, revised before any run and
  re-stamped 00:16:53Z (cap-edge construction, charpoly helper, `table` speed-up); run 1 (00:17:45–00:18:07Z) 12/12
  `VERDICT C11-OCTAHEDRAL-EXACT`; replay identical (out `9b4fed7b…`). Results: order 384 with the block form
  `P₀⊗A + P₁⊗ωPA`; Theorem C11-B (no Bell-type defect in any invariant cone; the sum identity); Theorem S′ (written proof);
  `φ₀`'s orbit has an orthogonal pair (no surgery on it); the explicit `G₃₈₄` cone on `h*` at `c* = 401/400` (EXOTIC-X,
  CONDITIONAL on S′); EXOTIC-X for every finite unitary group with `cnot`. RESULTS rows C11.1–C11.7 appended. Commit: C11
  (`1219a971`, pushed).
- 2026-10-11T00:40Z — C12. Scratchpad exploration (numerical, not evidence; `x12_mu.py`, `x12_bell4.py`, `x12_tools.py`,
  `x12_inst*.py`): the boundary-cover measure `μ(s)`, Gaussian-integer Bell sets for the ten orthogonality patterns, the
  witness Tools A–C on them and on 3000 random four-member sets (no failure), integer witness points for the exact
  instances. NOTES-C12 S0 written 00:35:34Z (`date -u`); `c12_pairs_bellsets.py` decision rule 00:35:57Z; one pre-run edit
  (CC3's rank test); run 1 (00:37:49Z) 9/9 `VERDICT C12-PAIRS-BELLSETS-EXACT`, replay identical (out `363c9899…`).
  Results: the sharp pair theorem for rank-one defects (C4.1 its Bell corner); the boundary witness BW with Tools A–C;
  C8-C proved at four members (all ten patterns) and for every finite Bell set with a complete non-orthogonality
  component; residual classes recorded. RESULTS rows C12.1–C12.6 appended (C8.4's label unchanged; C12.6 records the
  refined status). Commit: C12.
- 2026-10-11T00:56Z — C13. Scratchpad exploration (numerical, not evidence; `x13_explore.py`, `x13_more.py`): the basis,
  `λ_max` along the orbit circles, the overlap minimum, the S2 circle. NOTES-C13 S0 written 00:50:00Z (`date -u`);
  `c13_residual.py` decision rule 00:51:17Z; pre-run edits (R1's kernel statement made a rank statement, an unused line
  removed); run 1 (00:53:18Z) 9/9 `VERDICT C13-RESIDUAL-EXACT`, replay identical (out `cabe7692…`). Results: S′ for compact
  defect sets and extremality of the defects; the orthogonal-pair obstruction (Lemma C13-O); the minimal group
  `⟨H₀, cnot⟩` has no residual case (C10.2 explicit there); the fixed-point dichotomy for maximal tori; explicit exotic
  cones with a continuum of non-PSD extreme rays for a residual case (`Π = S₃`, three circles) and for the torus node S2
  without G16 (one circle); the obstruction for `Π ∋` double transposition (exact witness). HO-10 relied on only for the
  label of the residual region's existence (C13.6). RESULTS rows C13.1–C13.9 appended. Record: row C12.6's label is
  CONJECTURE (for C8-C as a whole); the rest of that cell points to the CONDITIONAL rows C12.3–C12.4 and is explanatory.
  Commit: C13 (`0d27d079`, pushed).
- 2026-10-11T01:06Z — C14. Scratchpad exploration (numerical, not evidence; `x14_span.py`): rank 14 of a circle surgery's
  contact span. NOTES-C14 S0 written 01:02:22Z (`date -u`); `c14_facial.py` decision rule 01:03:09Z; one pre-run edit
  (CC2's search box); run 1 (01:04:27Z) 8/8 `VERDICT C14-FACIAL-EXACT`, replay identical (out `e1a26898…`). Results: the
  tangency bound `c ≤ 15 − k` (`≤ 14` on `K_circ`'s off-`Fix` defects); `c = 14` exactly on circle-surgery defects; T fails
  on the explicit continuum cones of C13; T on `K_circ` OPEN, reduced to the absence of smooth contact. RESULTS rows
  C14.1–C14.4 appended. Commit: C14 (`3394d6b6`, pushed).
- 2026-10-11T01:10Z — extra node C15 (after the four listed nodes; C11.6 applied to the group of the bridge's "finite half"
  as recorded in the overview, definition only; HO-12 not received and not relied on). Scratchpad exploration (numerical,
  not evidence; `x15_cliff*.py`): small lattice seeds have exactly orthogonal pairs, large irregular seeds do not.
  NOTES-C15 S0 written 01:07:47Z (`date -u`); `c15_clifford.py` decision rule 01:08:11Z; run 1 (01:08:57–01:09:11Z) 6/6
  `VERDICT C15-CLIFFORD-EXACT`, replay identical (out `6cd53515…`). Results: order 11520 recomputed; an explicit exotic cone
  for the native Clifford family (CONDITIONAL on S′ only); the continuous half's group has double transpositions (rank-one
  route closed). RESULTS rows C15.1–C15.3 appended. Commit: C15.
- 2026-10-11T01:39Z — extra node C16 (closing review; C15's commit is `a107df72`, pushed). Checking the drafted handoff
  proposals against the rows found two defects in this round's own rows: (i) C13.4, C13.6, C13.7 and C15.3 say no rank-one
  orbit surgery with a common `c` is self-dual and cite Lemma C13-O, which covers `c ∈ (1, 2)` only; (ii) C13.9's
  parenthetical claims the orthogonal-pair obstruction for κ with G16, with no argument (the S2 argument was transferred
  unchecked). NOTES-C16 S0 written 01:31:37Z (`date -u`; file 01:32:44); `c16_kappa_bellcorner.py` decision rule
  01:32:52Z; two pre-run helper fixes (Gaussian rationals passed to the `GQ` constructor in `Ux` and `diag`); run 1
  (01:35:14Z) 15/15 `VERDICT C16-KAPPA-BELLCORNER-EXACT`, replay identical (out `6d0a5dfe…`). Results: the Bell corner
  closes (Lemma C16-1, Corollary C16-2 [W], exact instances, [A] Z's `K_T`), so the four rows' statements hold for every
  `c ∈ (1, 2]` (row C16.2; their labels unchanged); defect (ii) is a refuted claim (FAILED row C13.9f): κ's torus fixes the
  `|0±⟩` coordinates, and κ with G16 has an explicit two-circle surgery cone (C16.4, CONDITIONAL on S′; T fails on it,
  C16.5). RESULTS rows C16.1–C16.6 and C13.9f appended; no earlier row changed. HP4 item 5 scoped to `φ₀`'s H1 window;
  HP5 and HP6 revised before their first commit. Commit: C16.
- 2026-10-11T01:40Z — **round 3 close** (C16's commit is `95bf36d1`, pushed).
  - **Nodes done**, depth-first in the listed order: C11, C12, C13, C14 (all four listed nodes), then two extra nodes:
    C15 (the bridge's two halves of A_miss, from the overview's group definitions only; HO-12 not received) and C16 (the
    closing review).
  - **Rows appended** (36; no earlier row's label changed): C11.1–C11.7, C12.1–C12.6, C13.1–C13.9, C14.1–C14.4,
    C15.1–C15.3, C16.1–C16.6, C13.9f. By label: 30 CONDITIONAL, 4 OPEN (C12.5, C13.9, C14.4, C16.6), 1 CONJECTURE
    (C12.6), 1 FAILED (C13.9f); none CERTIFIED (no kernel work this round).
  - **Handoff proposals** (uncommitted drafts until this entry's commit; the coordinator routes): HP4 (→ equivalence,
    bridge: `G₃₈₄`, Theorem S′, EXOTIC-X for finite unitary groups with `cnot`), HP5 (→ bridge, equivalence: the two halves
    of A_miss, B3.C's residual region, Lemma C13-O, the Bell corner), HP6 (→ overview, equivalence: the pair theorem, C8-C
    at four members, κ with G16 EXOTIC-X, T on continuum cones, two assumption-watch markers).
  - **Integrity sweep at close** (01:40Z): every round-3 replay byte-identical and every `.err` ends `exit 0`; the
    hashes quoted in HP4–HP6 match the files; the receipts in `inbox/` still equal the overview's blobs at `2a055180`;
    nothing outside `research/countermodels/` changed since `e6d42cab`; RESULTS.md has no deleted line since `e6d42cab`.
  - **Deviations.** (1) Two version checks ran without `-I -B` (23:48Z entry). (2) The receipts commit was amended before
    its push (local `f230bc04` → `43a49d57`; 23:59Z entry). (3) Two extra nodes beyond the list (C15, C16). (4) Pre-run
    edits in every script, each recorded in its NOTES "Runs" section; no first run failed, so there are no `.run1.*`
    files this round. (5) Row C12.6's label cell carries CONJECTURE with an explanatory pointer to CONDITIONAL rows; the
    label is CONJECTURE (00:56Z entry). (6) Four obstruction rows (C13.4, C13.6, C13.7, C15.3) were written without the
    Bell corner `c = 2`, and C13.9 carried an unchecked κ parenthetical; both were found at the closing review and
    recorded by appended rows (C16.2; FAILED row C13.9f), not by edits. (7) `c13_residual.out` prints `⟨L_A|L_B⟩` as a
    pair of Fraction reprs (cosmetic; the value is `9 − 6i`, NOTES-C13). (8) A numerical penalty-optimizer test of
    self-positivity was insensitive and is not used (00:21Z entry); all scratchpad numerics are guidance, not evidence.
    (9) Row C15.2 and NOTES-C15 S0 quote `s_min ≈ 4.19·10⁻⁵` as a decimal gloss; the exact value
    `164178929/3916193820250` is in `c15_clifford.out`. (10) No CI runs, no dev branches, no Lean work.

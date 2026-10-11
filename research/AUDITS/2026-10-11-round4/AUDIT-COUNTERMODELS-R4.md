# Coordinator audit — `research/countermodels`, round 4

Thread head `644bf0a1` (2026-10-11; round-4 commits `217979fd` … `644bf0a1`). Base L = `9f9f8257`. Audited: the
round-4 rows of `RESULTS.md` (C17.1 … C17.3f; C18.1 … C18.8; C19.1 … C19.6f; C21.1, C21.1f), `NOTES-C17.md`,
`NOTES-C18.md`, `NOTES-C19.md`, `NOTES-C21.md`, `experiments/c17_preflight`, `c18_attempts` (run 2; run 1 kept),
`c19_groups`, `c21_rows` (run 2; run 1 kept), the design module `lean/CmSprime.lean` (with the failed dispatch's copy
`CmSprime.run38112032111.lean`), the six receipts in `inbox/`, the handoff proposals HP7, HP8, HP9, `LOG.md`. Audited
under the owner's round-4 acceptance criteria and, at the owner's request during the audit, with the three questions of
§"The three questions" answered explicitly and the Lean module reviewed at the statement level (method 4).

## Method

1. **Receipts.** HO-17, HO-18, HO-19, HO-21, HO-22, HO-23 (v1) copied verbatim at `217979fd` (each equal to the
   overview file at `742c6b2f`, re-checked by the coordinator), with the reliance recorded in `LOG.md` item by item
   before any research step (HO-17 item 7 recorded, unused; HO-18's two conjugation facts and pairing, and item 3's
   hypothesis list; HO-19 item 3 as a heuristic for C18's third attempt; HO-21's conjugation formulas, every group
   computation redone at the matrix level; HO-22 items 1 and 3 recomputed before use; HO-23 as context). HO-24 and
   HO-25 (the thread's own round-3 results) were read at the overview to resolve item numbers, not copied. The three
   coordinator addenda arrived before the first C17 script ran and were applied from their entries on. **One
   unauthorized cross-branch read** (05:23Z): a pattern search over three coordinator audit files at overview
   `f833107f`; logged with hashes, no decision used it (C17's label was fixed in S0 at 04:28Z). Recorded as a deviation;
   it changed no assumption of the thread (the files read are the coordinator's audits, not another thread's results).
   Protocol otherwise satisfied.
2. **Replay.** Four scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 4/4
   (`countermodels/REPLAY-LOG.txt`; `c21_rows` 120 s).
3. **Independent check.** `countermodels/indep_checkC4.py` (own code: Gaussian rationals over Fractions, projective
   group closures by BFS on canonical representatives, orbits and overlaps scalar-free; reads nothing from the thread —
   its one external input is the stage-6 reassessment table on `research/archive`; decision rule fixed before run 1):
   run 1 **8/8**, countercontrols 5/5 failing as stated, `INDEP-C4-FIXED`; replay identical (3 min 11 s).
   - X1 (C19.2): `|⟨CNOT, 1⊗S, 1⊗U_J⟩| = 384`, `|⟨G₃₈₄, X⊗1⟩| = 768`, `|C₂| = 11520`; `S⊗1 ∈ G₃₈₄`;
     `⟨G₃₈₄, U_J⊗1⟩ = ⟨G₇₆₈, U_J⊗1⟩ = C₂`; `G₃₈₄` is exactly the stabilizer of `Z⊗1` in `C₂` and `G₇₆₈` exactly that of
     `±Z⊗1`.
   - X2 (C19.3): `h*` has 192 rays under `G₃₈₄`, 384 under `G₇₆₈` (stabilizer 2), min `|det Ψ|² = 85/2048`, pairwise
     overlaps in `[1/1024, 13/16]`, no orthogonal pair; at `c = 10001/10000` H1 and (CC) hold exactly; under `C₂` 5760
     rays with exactly two orthogonal partner rays (dies).
   - X3 (C19.4, C15.2): `h_C` has 11520 rays under `C₂` (trivial stabilizer), min `|det Ψ|² = 198406621629/9790484550625`,
     overlaps in `[164178929/3916193820250, 1560203344561/1566477528100]`, no orthogonal pair; at `c = 100001/100000`
     H1 and (CC) hold (`c² s_min = 1641822125949978929/39161938202500000000000 ≥ 1/25000`).
   - X4 (C19.1): the explicit block element carries `(3, 4i, 0, 5)` and `φ₀ = (1, 2, 3i, −1+i)` to products, with
     each block a scalar multiple of an `SU(2)` element; the carried defect pairs `−1/2` with the product.
   - X5 (C18.1): the pairing identity of Lemma C18-1 on a grid; on `h = (2,1,0,0)`, `h′ = (1,−2,0,0)`, `c* = 51/50`:
     `⟨y, d_h⟩ = 0`, `h′†yh′/‖h′‖² = −1/4900 = λ(1 − c*)`, twelve sample defects pair `≥ 0` with `y` and by the identity,
     and pair `> 0` with `d_h`.
   - X6 (C18.3): the Bell pair's plane and the plane of `(3|00⟩+|11⟩, |01⟩+3|10⟩)` each contain an exact product `p`
     with `p†dp/‖p‖² = −1/2`.
   - X7 (C21): memberships (`1⊗S`, `1⊗(I−iX)`, `S⊗1 ∈ G₃₈₄`; `X⊗1 ∈ G₇₆₈ \ G₃₈₄`; `U_J⊗1`, `(I−iX)⊗1`, SWAP `∈ C₂ \ G₇₆₈`);
     MOVED witnesses with `P_w ∈ K` (max overlap `≤ 1/c`) and `⟨g(d), P_w⟩ = 1 − c < 0`: for `K384` the target `R_z(t₀)`
     (`1949/2048`), the control `R_x(π)` (`225/512`), `J` (`1341/2048`), `R_x(t₀)` (`4097/5120`); for `KC` the target
     `R_z(t₀)` (`3781930587509/3916193820250`) and the control `R_x(t₀)` (`188794252749681/195809691012500`).
   - X8 (C21 R0): the reassessment table (sha256 `1ff62ad6…`) has 199 Table A2 rows: 118 SATISFIES, 68 NOT REACHED,
     13 FAILS.
   - Countercontrols (all failing as stated): `|G₇₆₈| = 384`; `h*` surviving `C₂`; an orthogonal partner of `h_C` at
     `C₂`; `λ′ = (c*−1)/(4−c*)` giving `⟨y′, d_h⟩ = 0` (gives `−51/7450`); `G₃₈₄` carrying `φ₀` to a product (min
     `|det Ψ|² = 5/256`).
   - Not re-derived: Lemma C18-3 (the commuting-perturbation argument; only read), the κ cone `Kk` (its gate flow),
     the FCC contraction (C21's I3.135 mechanism), the K-independent rows of Table A2, and the self-duality of any
     surgery (H3), which rests on Theorem S′ (method 4).
4. **The Lean module, at the statement level** (`lean/CmSprime.lean`, sha256 `a10f4790…`, equal to the blob at
   `dev-countermodels/c17-sprime` @ `5649e641`; the failed copy equal to the blob at `7d3736e4`; the dev branch is cut
   from L and differs from it by the module and one aggregator import line).
   - *Definitions (§A).* `pr A B = Re tr(AB)`; `ip a b = a†b`; `qf M x = Re(x†Mx)`; `defect c h = 1 − c·hh†`;
     `dualH S = {Y Hermitian : pr X Y ≥ 0 ∀ X ∈ S}`; `surgery d = {q + Σ_k t_k d_k : q PSD, pr q (d j) ≥ 0 ∀ j, t ≥ 0}` —
     this is `K(Z) = (Q ∩ Z*) + cone Z` for the finite family `Z = {d k}`, as NOTES-C11 defines it.
   - *`theorem_Sprime` (§G).* Hypotheses: `h k` unit; `1 < c k ≤ 2`; `c k < card n`; `pr (d j) (d k) ≥ 0` for all
     `j, k`; (CC) in cap/co-cap form **for every ordered pair `j ≠ k` whose pairing is positive** (pairs with zero
     pairing are exempt — the form NOTES-C11 states and the two-defect theorem uses). Conclusion:
     `surgery d = dualH (surgery d)` and `IsClosed (surgery d)`. This is Theorem S′ in its finite form, as the thread
     describes it; `theorem_Sprime_C4` is the same on `Fin 2 × Fin 2` without the cardinality hypothesis (automatic);
     `theorem_Sprime_ineq` replaces (CC) by the inequality `(√(c_j−1) + √(c_k−1))² ≤ c_j c_k |⟨h_j|h_k⟩|²` through
     `cap_subset_cocap` (one direction only, as the header says); `twoDefect` is the two-defect case on `ℂ⁴` with
     `pr (d 0) (d 1) = 0 ∨ inequality` and derives the nonnegative pairing from `pr_defect_defect`;
     `control_single_defect` instantiates the theorem on `1 − (3/2)|00⟩⟨00|` (non-vacuity).
   - *The engine (§C–§F).* `selfDual_of_local` takes Hermitian `d k` with `pr 1 (d k) > 0`, pairwise nonnegative
     pairings and the local condition (`u†d_j u < 0` ⇒ `d_k` positive definite on `u^⊥` for `k = j` or
     `pr (d k) (d j) > 0`). `K ⊆ K*` is the four pairings; `K* ⊆ K` is `exists_psd_sub` (Farkas over the PSD cone cut
     by the finitely many half-spaces `pr · (d k) ≥ 0`, Slater point `1`, the kernel's `psd_iff_trace_nonneg`) followed
     by `exists_decomp` (a decomposition of least total weight on the compact feasible set `feas`, bounded through
     `pr 1 y / pr 1 (d k)`; if `q` paired negatively with some `d_j`, a column of a factor of `q` —
     `psdFactorization_discharged` — lies in the cap of `d_j`, the null vectors of `q` are orthogonal to it, a weight
     `t_k > 0` with `k = j` or `pr (d k) (d j) > 0` exists, and the local lemma `exists_qf_add_nonneg` (compactness of
     the unit sphere) lets that weight decrease: contradiction with minimality). `theorem_Sprime` supplies the local
     condition from (CC) through `qf_defect_pos_of_perp` and `bessel_two`. The argument is the one NOTES-C11 and
     NOTES-C17 describe, and it is sound as read; the design build is its machine check.
   - *`capcocap_real`* is the real-variable core of (CC) with the `linear_combination` certificate the thread's
     preflight P1 checks (`q₁ = −p²(K′² − R′²)`, `q₂ = −R²p²`).
   - *Dependencies.* Imports: `OIBridge.JordanClassification`, `OIBridge.BoundaryAudit`, `OIBridge.ReferenceSufficiency`
     (kernel modules at L) and Mathlib. Kernel names used, each verified at L at the cited line: `psd_iff_trace_nonneg`
     (JordanClassification.lean:84), `trace_mul_vecMulVec` (:74), `psd_trace_mul_nonneg` (OperationalRigidity.lean:917,
     reached transitively), `psdFactorization_discharged` (BoundaryAudit.lean:100), `dotProduct_star_self_real`,
     `dotProduct_star_self_pos`, `form_real_smul` (ReferenceSufficiency.lean:373, :381, :394). No `sorry`, `admit`,
     `axiom` or `opaque`; six `set_option maxHeartbeats 800000 in` (proof budget only).
   - *Axiom reports.* The module ends with 78 `#print axioms` lines (1175–1252). In the saved log of job 114391721556
     all 78 report `[propext, Classical.choice, Quot.sound]` (76 by the quoted-name count and two more —
     `star_ofReal'`, `vecMulVec_mulVec'` — whose primes end a quoted name early in the regular expression; the raw-line
     count finds 78 standard, 0 `sorryAx`); `lean-axioms` OK 5938. In the failed job 114389409224: 71 standard, 7
     `sorryAx` — `mem_surgery_single`, `selfDual_of_local` and the five statements that depend on them
     (`theorem_Sprime`, `theorem_Sprime_ineq`, `theorem_Sprime_C4`, `twoDefect`, `control_single_defect`) — with the
     errors at 668:20 and 724:10, as the thread read. The repair changed no statement (the two files differ in the
     weight vector's type ascription and the expansion of the pairing; compared).
   - *Scope.* Finite families only (`[Fintype ι]`); the compact-`Z` form the circle cones need is not stated. The
     theorem's hypotheses are met by the three finite cones of the round (`K384`, `KC`, `K768`): unit `h`, `c ∈ (1, 2]`,
     `c < 4`, pairwise pairings `4 − 2c + c²s ≥ 0`, and (CC) in inequality form `4(c−1) ≤ c² s` on every pair, which the
     coordinator's X2 and X3 verify at `s_min` (the inequality is monotone in `s`). So H3 of those cones rests on
     `theorem_Sprime_ineq` [D] exactly as C17.2 says.
5. **Written arguments read.** Theorem C19-1 (`SU(2)` transitive on spheres gives `gψ = (|a|, |b|) ⊗ e₀`; invariance
   then puts every pure state in `K`, so `Q3 ⊆ K = K* ⊆ Q3*`): sound, X4. Lemma C18-1 (the witness `y = P_h + λd_{h′}`
   with `λ = (c*−1)/(4−2c*)`; the decomposition argument `t = 0` from `⟨y, d_h⟩ = 0` and `⟨d_l, d_h⟩ > 0`): sound, X5.
   Lemma C18-2 (a 2-plane of `ℂ²⊗ℂ²` carries a binary quadratic form `det`, which has a root): sound, X6. Lemma C18-3
   (a commuting linear image of `Q3` that is self-dual is `U(Q3)` for an orthogonal `U` by the polar decomposition in
   `Aut(Q3)` [L: Faraut–Korányi]; the diagonal subgroup's six inequivalent off-diagonal characters make `U` a Schur
   multiplier on the off-diagonal part; H1 forces a permutation, the minors force the identity, PSD forces a coboundary):
   read, not re-derived; the row's label CONDITIONAL [W] + [L] + [X] is right. The C19.4 identification of the closure
   of `⟨cnot, actT J, actT R_z(θ₀)⟩` with a group containing `H` is HO-22 item 3's [W], cited at its label.
6. **Kernel citations.** The coordinator's sweep (`cite_check_r4.py`, lines added since `23713ce9`) finds 20 distinct
   `File.lean:NNN` strings, **20/20 resolve at L** (`cite_check_r4_countermodels.out`): 12 with the named identifier
   in the window, 4 naming none, and four window misses inspected by hand — ReferenceSufficiency.lean:373 is
   `dotProduct_star_self_real` (the name `trace_mul_vecMulVec` in the same sentence belongs to
   JordanClassification.lean:74, verified), CompositeDimension.lean:186 is `maxCone` and :198 `actT` (the names
   `CandidateCone`, `cnot`, `pc`, `pt`, `sgn` belong to their own citations), DiscreteCompletion.lean:1929 is
   `fixedGateTheory_derivedOI` (HO-17's inbox copy). Also verified at L: KInfFoundations.lean:350 (`rotFun`'s
   docstring line), :411 `rot3`, :425 `cyc3`, :449 `ball3Drive`; CompositeDimension.lean:161 `prodState`, :201 `actC`;
   K2Guard.lean:101 `idW`. All correct.
7. **Design runs** (`CI-RUNS-R4.md`). 38112032111 (`dev-countermodels/c17-sprime` @ `7d3736e4`): Build **failure**
   (two errors), gate skipped, run completed 32 success, 1 failure. 38112813276 (@ `5649e641`): Build success (3644
   jobs), 78/78 prints standard, `lean-axioms` OK 5938, gate red only at `lean-manuscript` (1 problem, the unregistered
   module), `legacy-records` 303, `v3-receipts` 43; run completed 32 success, 1 failure at 05:29:31Z. Nothing cancelled;
   the third dispatch unused. Design evidence only; nothing certified.
8. **Acceptance-criteria checks (owner, 2026-10-11).**
   - *Hypothesis classification.* C17: pure cone geometry, no OI item, no introduced hypothesis — correct (method 4).
     C18, C19: the groups are the (b)-instances under test; H1, H3 introduced; no inventory item assumed — as the notes
     state. C21: the 13 FAILS rows are hypotheses (do-not-assume items, [D] four-token hypotheses, PT-record
     candidates), none a theorem or definition at L — consistent with the inventory records read in the equivalence
     audit (I3.144 not at L; I3.148–I3.153 PT-record; I3.165 open).
   - *Pair-level versus full-OI.* Every cone is labelled "satisfies the transferred pair-level premises at L", never
     "satisfies OI" or "independent of OI"; the 68 NOT REACHED rows are listed unchanged; C21-3 says in so many words
     that the cones are not countermodels to OI's quantum conclusion.
   - *Invariance versus availability.* Every (b) column is headed "invariance under …"; no row or note says a cone
     makes an operation available; C19.3, C21.1 and HP8/HP9 carry the clause explicitly.
   - *C21 safeguard.* Each table carries the two columns; the Q3-level column of a (b)-row is filled only through the
     cited entailment (a local unitary moving `K` gives `K ≠ Q3`), never the converse; `K ≠ Q3` (I3.144) is decided by
     its own witnesses (`P_h ∈ Q3 \ K`; `Φ⁺ ∈ K \ twin`).
   - *Defeated alternatives named.* C18.6f (three routes), C19.3, C21.1/C21-3 (four invariance groups) name them.

## The three questions (owner, 2026-10-11)

**1. Are the countermodels mathematically valid?** For the three finite cones (`K384`, `KC`, `K768`) the defining
properties were re-derived in the coordinator's own exact code, not read from the thread's scripts: the groups and their
orders and stabilizers (X1), the orbits with no product and no orthogonal pair (X2, X3), H1 through the Schmidt bound
(`c λ_max ≤ 1`, checked as `|det Ψ|²_min ≥ (1/c)(1 − 1/c)`), and (CC) in inequality form on every pair (X2, X3). Their
self-duality (H3) is not a finite computation; it rests on Theorem S′ in its finite form, whose Lean statement was read
(method 4) and matches the hypotheses those cones meet; its proof is machine-checked in a design run ([D], not
certified). The non-invariance verdicts rest on exact witnesses (X7). The κ cone (`Kk`, compact defect set) was not
re-derived here: its invariance and the compact form of S′ stay on the thread's probe and written proof ([W]). Verdict:
valid as labelled — CONDITIONAL on `theorem_Sprime_ineq` [D] for the three finite cones, on S′ [W] for `Kk`.

**2. Which OI premises do they satisfy?** Against the 199 applicable items of Table A2 (counts verified, X8), three
kinds, in the owner's distinction:
- *Satisfied directly at the cone's level* — the 29 K-dependent SATISFIES rows: the twelve `cone` rows by the exact
  computation (H1, (CC)) plus S′ for H3 and the gate invariance; I3.148 (H2) at level (i) for `K384`, `KC`, `K768`
  (the transpose moves them) and at level (ii) for `Kk`; the `d4v` rows vacuously (their hypothesis `H` or IE1 fails).
- *Transferred by a proved bridge* — the 13 `b1` rows through `K ⊆ maxCone` (H1 and H3 give it: `maxCone` is the dual
  of the product effects, CompositeDimension.lean:186 at L [K]); the `kthm` row I3.44 through `no_candidateCone_cnot_reflY`
  (K2Guard.lean:143 [K]) with `cnot` invariant; the 89 K-independent rows (definitions, kernel theorems, single-token
  facts inherited by every cone on two copies of the ball) carry Table A2's verdict unchanged.
- *Never reaching the model's level* — the 68 NOT REACHED rows (M-level and H-level items: K∞ seams, the stage
  structure, the operational classes). R6 found no theorem at L transferring any of them to the pair cone, and nothing
  at L has changed. **So a cone that satisfies every reached row is a countermodel to the transferred pair-level
  premises at L and nothing more**; the thread labels it exactly so.
- *Failed* — the 13 FAILS rows: the (b)-instances (IE1, IE1Drive, (b_S4), (b_n), (b_R1), (b_DJ), FC, K2's clause) and
  the Q3-level items (I3.144, `H`, FCC, homogeneity, T), each a hypothesis, not a theorem at L.

**3. What exactly do they disprove?** Each cone refutes one named implication at the pair level, with H1 and H3 as
introduced hypotheses: *invariance under `Stab_C(Z⊗1)` ⇒ `Q3`* (`K384`), *under `Stab_C(±Z⊗1)` ⇒ `Q3`* (`K768`),
*under the two-qubit Clifford group with SWAP ⇒ `Q3`* (`KC`), *under G16 with κ's gate flow and the drive flow on the
control without `J` ⇒ `Q3`* (`Kk`). These are failures of particular bridge candidates — every finite Clifford clause,
and the drive flow without its cyclic permutation — not a demonstration that `Q3` fails to follow from OI: the
implications refuted have introduced hypotheses on both sides and say nothing about the 68 items that never reach the
cone, and cone invariance is not operational availability. In the other direction, Theorem C19-1 (C19.1) shows that
the *continuous* block-diagonal `SU(2) × SU(2)` fixing `Z⊗1`, with H1 and H3, does force `Q3` — so within the clause's
group the forcing comes from the continuous half, and the first generator that kills every surgery cone is the
non-Clifford rotation (C19.4, CONDITIONAL on HO-22 item 3 for the closure). C18 closes three construction routes for
case B and S2 with G16; it does not show those cones do not exist (existence stays at claim (D) [A] and EXOTIC-E).

## Findings by row

| row | thread label | audit |
|---|---|---|
| C17.1 | CONJECTURE [D] | accepted; the module read at the statement level (method 4), the two job logs counted (78/78; 71 + 7 `sorryAx`), the dev branch verified |
| C17.2 | CONDITIONAL (C17.1) | accepted; the three finite cones meet `theorem_Sprime_ineq`'s hypotheses (X2, X3); the compact-`Z` rows keep S′ [W], as the row says |
| C17.3f | FAILED (prediction) | accepted; the two errors verified in the saved log |
| C18.1 | CONDITIONAL ([W]; [X]) | accepted; X5 (identity, signs, instance) |
| C18.2 | CONDITIONAL ([W]) | accepted; the replay covers A1-Bell; not re-derived |
| C18.3 | CONDITIONAL ([W]) | accepted; X6 |
| C18.4 | CONDITIONAL ([W]) | accepted; the replay covers A2b; the engine's local condition read (method 4) |
| C18.5 | CONDITIONAL ([W]; [L]) | accepted as labelled; read, not re-derived |
| C18.6f, C18.7f | FAILED | accepted (C18.7f: run 1 kept, the corrected assertion is the computed centralizer) |
| C18.8 | OPEN | accepted; correctly scoped |
| C19.1 | CONDITIONAL ([W]; [K] JordanClassification.lean:84) | accepted; X4; the written proof read (method 5) |
| C19.2 | CONDITIONAL (`actC`/`actT` as `Ad`) | accepted; X1 (orders, stabilizers, generation) |
| C19.3 | CONDITIONAL (S′ finite form [D]; H1 [W]) | accepted; X2; **cone invariance only**, as the row says |
| C19.4 | CONDITIONAL (C13.2, C18.1, C19.1; HO-22 item 3) | accepted; X2 (`h*` dies at `C₂`), X3 (`h_C` survives) |
| C19.5 | OPEN | accepted; the search is sampled, as the row says |
| C19.6f | FAILED (guess) | accepted |
| C21.1 | CONDITIONAL | accepted; X7 (K384, KC by operation), X8 (the table); the premise classification above; the Kk column not re-derived |
| C21.1f | FAILED (prediction) | accepted; the run-2 RECORD identity is the thread's, kept with run 1 |

No label changes. The thread's recorded deviations (the unauthorized pattern search, 05:23Z; C21's run-2 amendment
adding two RECORD lines after a passing run 1, both runs kept and the change disclosed in the script; the failed first
runs of C17 and C18 kept; a float scratch computation choosing C18's A2b-near parameters before run 1; the print-count
correction 81 → 78 in NOTES-C17's S0 before any run, not logged at the time; C19 and C17 closing in one commit; C20 not
run) are each in the LOG and change nothing audited here.

## Handoff items

- HP7 → **HO-30** to the equivalence and bridge threads: Theorem S′ (finite form) design-built, with the coordinator's
  statement review and the hypotheses consumers must meet.
- HP8 → **HO-31** to the bridge, origin and equivalence threads: Theorem C19-1, the Clifford chain with the `G₇₆₈`
  cone, the three closed routes, the survivor question, two assumption-watch markers.
- HP9 → **HO-32** to the equivalence, bridge and origin threads: the four cones against Table A2 by operation, with the
  three-way premise classification above, the weaker alternatives, the FCC mechanism (not re-derived) and the marker.

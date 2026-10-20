# Review: F2-reg dependency ledger and the three-token (Σ3) exclusion

Independent adversarial review of `f2ledger/` (LEDGER.md, reg3_exclusion.py, indep_check.py, monomial_branch.py).
Base: `main` at `ec49d0b41648d8a070179c8fa3aaf20b5c6ff863`, read with `git show`/`git grep`. The #864 context was read
at `dcbcae42`. The branch `research/x-screen-20261018` has since been force-updated to `19f2cdb0`, but `dcbcae42`
still resolves. Nothing was written to the repository or to GitHub.

## Verdict: CONFIRMED WITH CORRECTIONS

The mathematics of claim (3) holds, and I re-derived it with my own exact code. That covers the upper bound, the
witnesses, the density and exact reach, and the lower bound. The monomial-branch lemma is correct. Every cited Lean
name exists at the line given. Two statements claim more than the evidence supports (B1, B2). Both are wording-level
corrections and must be made before the ledger is used as a basis for planning.

## Blocking findings

**B1. "Weakest known sufficient form of O-B" (§3) and "carries all the cone-level work hA was doing" (§5) need
rescoping. At the pair, Σ3 is equivalent to the conclusion and to hH2 ∧ hA, not weaker than them.**
- Upper route, existence form. Some K₃ satisfies ATT ∧ NC₃ ∧ MAX₃ ⟺ K₂ ⊆ Q3.
  - (⇒) is the ledger's B1/B2, which I re-derived (R1, R2).
  - (⇐) take K₃ = QK₃: unitary conjugation and product tests are PSD-compatible (D1, R5b).
- Lower route, existence form. Some K₃ satisfies H1₃ ∧ NC₃ ∧ RO₃ ∧ DIS ⟺ Q3 ⊆ K₂, modulo closure. The witness is
  the same, K₃ = QK₃, because the Lüders branch and Tr₃ are CP.
- So, relative to the domain, Σ3 is satisfiable at K₂ ⟺ K₂ = Q3. The kernel gives
  `pairCone_eq_Q3_iff_drive_maxCone` (EqvK2MaxCone.lean:174): given hH1, hadd, hsmul and hmax, K = Q3 ⟺ hH2 ∧ hA.
  Σ3 and hH2 ∧ hA therefore have the same content at the pair.
- What Σ3 changes is the vocabulary. Its *operations* are native; its states and tests are not (H1₃ and MAX₃ need
  non-configuration token states and tests, D4c and R5d), and it adds a new object, K₃, which carries its own
  unsourced clauses.
- §4.6 says "No equivalence is stated … D1 is a holds-in-QM check, not a converse". For the existence form, D1 is
  the converse, and a trivial one. That is the reason "weakest" cannot stand.
- On item (d), the PSD import. Σ3 does not postulate PSD. In the fixed 8×8 Ad_P carrier, MAX₃ ∧ NC₃ ∧ ATT is
  equivalent to the validity of a dense set of entangled pure tests C†(a⊗b⊗c) on K₂. That is, it is exactly PSD at
  the pair, restated as three-token test validity under native coherent conjugation.
  - §4.5 item 1 ("no competing cone is evaluated in the PSD order") is true but incomplete without this
    equivalence.
- Fix:
  - replace "weakest known sufficient form" with "a sufficient form, equivalent at the pair to K₂ = Q3 and hence to
    hH2 ∧ hA relative to the domain, whose operations are native";
  - state the existence-form converse;
  - in §5 reason 1, add "the operations are OI's; the token states and tests it needs are not (O-A)".

**B2. §4.5 item 5 says the survival of Γ(Q3), K_B and K_S "depends on truncating native protocols at two tokens".
That is false at Σ2 level. These fixtures are already outside Σ2.**
Checks in `pc24_fixtures.out`:
- **Γ(Q3)** fails PC24. For 16 of the 24 native pair permutations, Ad_P Γ(Φ⁺) ∉ Γ(Q3). This agrees with #864 SC E2:
  8 of 24 preserve it.
- **K_B = SEP + ℝ₊B** fails PC24. Ad_{X⊗I}B is the Ψ⁺ projector, which is not in K_B.
- **K_Γ = Q3 + ℝ₊Γ(B)** fails CNOT invariance. The characteristic polynomial of Ad_CNOT Γ(B) − tΓ(B) has the root
  −√(t²+t+1)/2 < 0 for every t ≥ 0.
- **K_S** fails MI (#864 SC §3.3).
- The #864 record itself notes that "PC misses K(Z_F)", meaning PC excludes the others (SC AW-S4).

The fixture shown in the ledger to survive every pair-level clause and to need Σ3 is K(Z_F). K_H\*'s PC24 status
was not checked by the author or by me.
- Fix:
  - restrict item 5 and marker AW-F1 to K(Z_F), plus K_H\* if its PC24 is checked;
  - in "Which fixtures each route excludes" and in §5's "exclusion aspect of G5 for every listed fixture", note that
    Γ(Q3), K_Γ and K_B are already excluded by PC24 at the pair, and K_S by MI.

## Corrections (non-blocking)

**C1. Lower route, "with σ⁻¹ every pure state lies in K₂ exactly" (§4.2 C1).** σ⁻¹ reaches exactly the u with
u₀₀ ≠ 0. A vector with u₀₀ = 0 needs a native pair transposition first (PC24, which Σ2 contains), or another σ.
- R2c and R2d check this for u = (0,1,1,1).
- With that addition, K₂ ⊇ Q3 exactly.

**C2. "Assuming the pair cone is closed".**
- The upper route never needs closure: it uses continuity of u ↦ ⟨u|X|u⟩ (B2), or B4b with C1.
- The lower route needs closure only in the CNOT-only variant of NC₃.
  - u = (0,1,1,1) and (1,0,1,1) are not of the form D_c(a⊗b): a Gröbner basis computation gives [1] (R2b).
  - Permuting entries cannot remove a zero, so PC24 does not rescue them.
- With the full S₈ form of NC₃ (σ is native: `permClass_permMatrix`) together with PC24, the result K₂ = Q3 holds
  with no closure hypothesis.
- The ledger's scoping is safe. It should say which variant uses closure.

**C3. Precise scope of claim (3).** "Excludes every pair cone other than Q3" should read as follows.
- **Statement.** Let K₂ be a convex cone in the 4×4 Hermitian carrier (H-CAR), closed in the CNOT-only variant.
  Suppose some cone K₃ in the 8×8 Hermitian carrier (H-CAR₃) satisfies H1₃, MAX₃, NC₃, RO₃, ATT and DIS, where:
  - native permutations act by the fixed Ad_P (G3);
  - the readout branch is the Lüders branch;
  - token states and tests are the full Bloch ball, including complex non-configuration ones (O-A; the R5e/R5f
    mutation shows that real tests cannot exclude complex non-PSD fixtures).

  Then K₂ = Q3. Conversely, (Q3, QK₃) satisfies these clauses.
- **What it is not.** It is not a statement about cones outside that carrier or that identification. D5 and R5c
  show that under the Γ-transported identification, Γ(Q3) satisfies the transported upper route, by transport of
  structure: Γ₂ maps product tests to product tests with b ↦ b̄.

**C4. The monomial-branch control is vacuous.** `monomial_branch.py`'s "control" checks a hand-written Hadamard
support set and does not go through `run_split`, so it would pass even if the detector were broken.
- The ledger already says the instance is not independent evidence of the lemma.
- Replace the control with one that runs a Hadamard through the same branch computation. My R6c does this.

**C5. Minor citation precision.**
- OI-7 paraphrases `PhaseFreeRichness` as "one continuously driven pair per level". The definition (MinimalRepertoire.lean:423)
  also requires every swap. That conjunct is supplied under `SourcedOI`, so the paraphrase is harmless but should
  say so.
- The "ball and effects" row omits that `avail_eq_fullEffects` also takes `hU` (unit effect) and `hM`
  (mixing-closed).
- Σ0 tags the classical-cone countermodel as (a). The kernel theorems are about the operation class `permTheory`.
  The cone-level reading, diagonal cones, is a short [W] step.
- `maxCone_bound_of_sharp_available` has no line number given; it is at EqvK2MaxCone.lean:194.

**C6. The O-B countermodel is checked only at the pair.**
- The REG clauses (ATT, DIS) need a K₃. One that works is K₃ = cone{K(Z_F)⊗τ} ∪ products: attach and discard map
  it back into K(Z_F) or into products [W, mine].
- "Every other premise at the pair" should either say so, or add this K₃.

**C7. "Minimal open obstruction" (§3).** What is shown is irredundancy: each of O-A and O-B is needed relative to the
rest. Minimality among all decompositions is not shown. Also, by §3's own text, O-B's native form consumes O-A
(non-configuration tests), so the two are not independent premises.

## Register (§A.32/§A.33)

The ledger is a research note, not `papers/` prose, so §A.32 and §A.33 do not bind it. If any of it is propagated
into a manuscript:
- drop the process vocabulary ("Decisive investigation", "Pressure test of the favourable branch", "NEW (scoped)",
  "AW-F1", the G-gate labels and the internal tags such as [W], [EC], [CD]);
- write status words in lowercase ("open", not "OPEN").

The note itself does not assert and then qualify, and it carries no self-narration in manuscript voice.

## (a) Replay

Each script was run twice in `revf2/rerun/` with `venv/bin/python -I -B` (Python 3.13.16, SymPy 1.13.3).

| file | sha256 (mine, both runs) | equals author's |
|---|---|---|
| reg3_exclusion.py | 661de3c5…668699 | yes |
| reg3_exclusion.rev{1,2}.out | 75b55ed0…a42e | yes (53 PASS, rc 0, ~9 s) |
| indep_check.py | dc8afbd5…3321 | yes |
| indep_check.rev{1,2}.out | 63501280…62cd2 | yes (7 PASS, rc 0) |
| monomial_branch.py | b12b5e45…b338 | yes |
| monomial_branch.rev{1,2}.out | bd7ad5f4…a598 | yes (5 PASS, rc 0) |

`sha256sum -c SHA256SUMS` passes for all 9 entries.

## (b) Do the checks test what they claim?

**Genuine tests.**
- A1–A4: spectra, PC24 permutation of Z_F, block positivity via orthogonal coefficient matrices, and P_m.
  - The A4b → K(Z_F)\* inference (L ⊆ Z_F\* ⇒ cone(Z_F) ⊆ L\*) is correct.
- B1, B4b: symbolic identities with generic X.
- C1, C1b, E1, E2: symbolic.
- B3a/b/c, B4d, D4b: exact witnesses.
- C2a–e: exact generation.
- D3b: a symbolic control showing that CNOT₁₃ alone yields product test vectors.

**Weak or trivially implied, but not wrong.**
- B2 is one numeric instance. The general density step is [W] and correct; my R2a checks 25 random instances
  exactly.
- D1 is a single positive sample. Q3 satisfying Σ3 is trivial anyway.
- D2b restates that the classical cone fails H1, which Σ1 already requires.
- D3a and D3c use finite test families. Both are implied universally by A2 + A3.
- D4c reads diagonal entries, which are nonnegative for any element of maxCone. It is a necessary-by-structure
  control, not an independent one.
- D5a/b show only that the transported action differs from Ad_C. Γ(Q3)'s survival under it is transport of
  structure, which my R5c checks symbolically.

**Vacuous.** The Hadamard control in `monomial_branch.py` (C4). The exhaustive support scan is a direct consequence
of injectivity, as the ledger says.

**Independence of `indep_check.py`.** It is a genuinely separate path: Fractions, no SymPy. It reproduces I1, −2,
−47/4, the configuration control and P_m.

## (c) Independent verification (`revf2/rev_check.py`, 35 PASS, rc 0, byte-identical over two runs)

Own code: operators built as dicts and loops over configuration tuples; no author helpers.
sha256: script `e39f89a2…51b8`; output `25eb1c52…b2bb3`, the same for both runs.

**R1. General form of the protocol.** For any native σ ∈ S₈, ⟨φ|Ad_σ(X⊗|0⟩⟨0|)|φ⟩ = ⟨u|X|u⟩ with u(x) = φ(σ(x,0)).
- Symbolic for C = CNOT₂₃·CNOT₁₃, for σ and for CNOT₁₃.
- Checked exhaustively for all 40320 σ with Gaussian-integer data: 0 mismatches.
- For C, u = diag(c₀,c₁,c₁,c₀)(a⊗b), as claimed.

**R2. Reach.**
- Every u with nonzero entries is reached exactly by the parity route (25 random instances; c₁ = c₀√(u₀₁u₁₀/(u₀₀u₁₁))).
- u = (0,1,1,1) and (1,0,1,1) are unreachable by that route (Gröbner basis [1]).
- The σ route reaches u₀₀ ≠ 0 exactly. Composed with a native pair transposition it reaches (0,1,1,1).

**R3. Witnesses.**
- z₁,₁ on |+i⟩|−i⟩|+i⟩ gives −2, normalized −1/4.
- z₁,₁ on the real test (2,1)(1,2)(3,1) gives −47/4, normalized −47/1000.
- For each of the four defects and for Γ(Φ⁺), a pair transposition plus σ gives the exact value λ|w|², where w is
  the negative eigenvector. The values are −2, −2, −2, −2 and −1.

**R4. Lower route** (selective readout 0 on token 3, then discard), with my own parameters:
- the singlet: parity route, a = (1,1), b = (1,−1), c = (0,1);
- Φ⁺: σ route, a = b = (1,0), c = (1,1);
- CZ|++⟩: σ route, c = (1,−1);
- P_m: σ route. Its vector (1,1,−1,1) has no zero entry, so the parity route also reaches it.
- P_m is rank one, with Tr(z P_m) = −1/2.

**R5. Controls.**
- PSD is preserved.
- Γ transport (R5c).
- Configuration tests read diagonal entries.
- Real-test mutation: X = Γ(|ψ⟩⟨ψ|) with ψ = (1,0,0,i)/√2 is non-PSD but has a PSD real part (R5e/R5f).
- K(Z_F) pair readout branches are PSD (R5g).
- Separately, PC24 permutes Z_F.

**R6. Monomial lemma.**
- Symbolic ancilla amplitudes: 300 random permutations, and 100 random two-round feed-forward protocols. Every
  branch has at most one nonzero entry per row, and each entry is a single term.
- A Hadamard inserted into the same computation gives an invertible non-monomial branch, so the detector fires
  (non-vacuous).

## (d) Do the added premises smuggle in the conclusion?

- **PSD import.** It is not a postulate, but it is equivalent at the pair (B1). The force is three-token product
  tests (4 complex parameters) read through a parity coupling into a ready meter, which gives a dense set of pair
  test vectors.
  - At two tokens, PC24 + hmax yields only the 3-dimensional CNOT image of the products. That is why K(Z_F)
    survives there.
  - The identification (8×8 Hermitian carrier, trace pairing, Ad_P) carries the PSD structure. The ledger flags it
    as retained and unsourced (§4.5 items 1 and 3), which is correct.
- **"Pair cone closed".** It does no hidden work in the upper route, and it is avoidable in the lower route with S₈
  + PC24 (C2).
- **RO₃.** It is the Lüders branch ΠρΠ on the coherent carrier, which keeps the coherences inside the x₃ = 0 block.
  - Within the kernel's `FiniteOperationalTheory` (a CP-matrix framework), `readout_is_localLuders` derives that
    form from spectator-independence.
  - It therefore presupposes quantum-instrument structure exactly as much as the carrier does, and no more.
  - What is new and unsourced is its application to a K₃ that is not assumed PSD. The ledger says this ("each is a
    compatibility or validity premise").

## (e) Monomial-branch lemma

The argument is correct, and the conclusion is in fact stronger than stated. Each row of a branch has at most one
nonzero entry: by injectivity, a fixed output (x, c′) has at most one preimage (y, c). An invertible branch is
therefore monomial.
- The reduction holds for feed-forward (controlled permutations are permutations), mid-protocol preparations
  (deferred), discards (a sum over outcomes) and mixing (unitary channels are extremal, so every branch is ∝ U).
- Scope: protocols whose instruments are configuration readouts only. Non-configuration measurements would come
  from O-A. That matches "coherent preparations do not source coherent control".
- The instance is correct, and its control is vacuous (C4).

## (f) Lean citations

Every backticked kernel name in the ledger was grepped for its declaration at `ec49d0b4` (`revf2/lean_grep.txt`).
- All 68 names in OIBridge exist, and every file:line given matches the declaration line.
- Three names are not Lean names at main: `dictK` and `drivesElementary_of_pow` are tagged [CD], not on main, and
  `fiber_freedom` is a probe in `purification_probes.py`. All three are cited as such.

Ten rows were read against the theorem statements; each reads as stated, apart from the minor points in C5.

| row | theorem | reads as stated |
|---|---|---|
| OI-3 | `permClass` (scaled partial permutations), `permClass_permMatrix`, `permClass_readWrite`, `dict_cnot` | yes |
| OI-4 | `readout_is_localLuders` (forced from spectator-independence), `instAvail_reset` (given the reset permutations are in the class) | yes |
| OI-5 | `finiteRootedRealizable_iff_pper` (finite V, both directions) | yes |
| OI-6 | `obsTheory_nonnegBounded`, `frozen_sourcing_verdict`, `nonnegBounded_verdict` (Fin 2) | yes |
| OI-7 | `sourcedOI_qm_iff_phaseFree`, `permTheory_not_qm`, `permTheory_sourcedOI` | yes (C5) |
| OI-8 | `substratum_residual`: `substratumClass` = `IsMonomial`, four closures, ¬QM | yes |
| K∞-Trans | `not_boundaryTransitive_of_countable`, `not_boundaryTransitive_flow` | yes |
| K∞-Drive | `isEmpty_drivability_of_finite_orbits`, `ball3_drivable` | yes |
| K1 | `dim_of_nativeGateOf` (d ∈ {1,3}), `three_of_nativeGateOf` (with `EntanglingOf`) | yes |
| K2 | `pairCone_eq_Q3_of_drive_maxCone`, `driveInvariant_of_eq_Q3`, `pairCone_eq_Q3_iff_drive_maxCone`, `Q3_aMiss` | yes. There is one witness per direction (§A.34 satisfied). The kernel theorem needs no closedness of K. hA is a single conjunct (drive ∧ cyc), which the ledger splits into two rows. |
| X-1 | `countable_not_pairFlowSourced` (a necessary condition), `mixTheoryR_not_qm`, `fixedGateTheory_not_qm` | yes |

The ROADMAP lines (1009–1010, 1023–1026, 1058–1062, 1130–1132), PG:187–195 (Arc B), PG:521 (the Independent
verdict) and Main.md:44, :74, :600–604 and :708 were spot-read and match.

## Which claims I verified independently, and which I only read

**Independently verified with my own exact code:**
- claim (3) in full: the upper bound, density and exact reach, the −2 and −47/4 witnesses, the lower-bound
  generation of the singlet, Φ⁺, CZ|++⟩ and P_m, and the spectator, configuration-test and Γ-transport controls;
- claim (2)'s K(Z_F) facts: PC24, P_m and −1/2, block positivity, and the readout branches;
- the monomial lemma's argument, plus a stronger instance.

**Checked by reading or reasoning only:**
- the drop-one models of §4.4 (their constructions are consistent; E1 and E2 were replayed);
- the k ≥ 3 extension [W];
- the [CD] objects;
- the thread I rows;
- K_H\*'s pair-level status;
- claim (1)'s countermodel claims beyond the pair (C6, C7);
- claim (4), the recommendation, which is reasonable once B1 is applied.

## Files (`revf2/`)

- `rev_check.py` and `rev_check.run{1,2}.out`: independent verification.
- `pc24_fixtures.out`: the B2 checks.
- `rerun/`: replays of the author's scripts.
- `lean_grep.txt`: declaration grep.
- `cites.txt`: extracted citations.

***

# Re-review of the corrected ledger

Material: `f2ledger/` with LEDGER.md `ccbe1f91…`, LEDGER.original.md `77b50b90…`, CORRECTIONS.md, `kh_pc24.py`, a
revised `monomial_branch.py`, and SHA256SUMS. `sha256sum -c` passes for all 14 entries.

## Verdict: CONFIRMED WITH CORRECTIONS

- B1, B2 and C1–C7 are closed.
- The new K_H\* and K(Z_F) three-token claims are sound.
- One wording overreach remains, R1 below. It needs scoping, but it does not affect any computation or verdict.

## Provenance of the original ledger

`LEDGER.original.md` is 335 lines and 26630 bytes. The ledger I listed at the start of the first review had the same
size and line count. It contains every passage the first review quoted:
- "weakest known sufficient form";
- "No competing cone is evaluated in the PSD order";
- "not a converse theorem";
- "depends on truncating …";
- "with σ⁻¹ every pure state lies in K₂ exactly";
- "carries all the cone-level work hA was doing".

Its line 280 also matches the text I read. The first review did not hash the ledger, so this identification rests on
size, line count and content, not on a digest. On that basis, `77b50b90` is the text I reviewed. The `8db3efb9`
state was never seen by me.

## (1) B1: closed

- §3 O-B, the §2.2 row "re-expression", §4.5 item 1 and §4.6 now state the existence-form equivalence:
  (∃K₃ satisfying Σ3) ⟺ K₂ = Q3 ⟺ hH2 ∧ hA, relative to the domain, with the trivial converse K₃ = QK₃.
- §4.5 item 1 states the pair-PSD equivalence.
- "Not a converse" is gone.
- The revised recommendation follows from the equivalence:
  - attack O-A first;
  - Σ3 gains vocabulary, not content;
  - the revised derivation requirements include the monomial lemma as a must-fail control, plus the PG:521
    Independent verdict.

## (2) B2: closed

- §4.2 now has Σ1 and Σ2 rows. Γ(Q3), K_Γ, K_B and K_H\* fail PC24 or hH2, and K_S fails MI. The Σ3 verdict names
  K(Z_F) as the only listed fixture that needs Σ3.
- Further claim checked: "maxCone fails CNOT". Confirmed: Ad_CNOT Γ(Φ⁺) gives −1 on the product test |−⟩|1⟩
  (`rereview_check.out`).
- `kh_pc24.py`, run twice, gives byte-identical output (`d9b29aae…`, 10 PASS, rc 0).
- **The test checks what it says.**
  - The criterion is correct: v ∈ U(μ)Prod for some |μ| = 1 ⟺ |det C_s| = |a|².
    - It is proved symbolically (K0, K0b).
    - It has a positive control and a negative control (K2).
  - g = (V⊗V)(|00⟩+2|11⟩) is a generator of K_H\*: it lies in 𝒰·G with μ = 1, and it is symmetric (K3b).
  - h = CNOT g = (−23, 36i, 2, 36i)/25.
- **My own check, by a different route.** I solved det(coefficient matrix of U(ν)h) = 0 for ν. Both roots have
  |ν| = 34033^{1/4}/√65 ≈ 1.68 ≠ 1, and h is not symmetric. So h ∉ Sym ∪ U(μ)Prod.
- **K4's "20 of 24".** Every witness used is a genuine pure generator: U(m) fixes Sym, and U(m)(a⊗b) ∈ 𝒰·SEP. The
  count is therefore a sound lower bound on failing permutations. The other 4 are explicitly untested.
- **The extreme-ray step [W] is sound.**
  - K_H\* ⊆ Q3, and a rank-one PSD matrix is extreme in Q3. So a finite conic combination equal to |h⟩⟨h| has every
    term ∝ |h⟩⟨h|, and the pure states of K_H\* are exactly its generator rays, which lie in Sym ∪ U(μ)Prod.
  - If K_H\* is meant as a closed cone, the argument still holds. The generator rays form a compact, trace-normalized
    set (Sym ∪ ⋃_{|μ|=1} U(μ)Prod is closed) inside a pointed cone. So the closure equals the conic hull, by
    Carathéodory's theorem and compactness.

## (3) C1–C7: applied

- **C1, C2.** σ⁻¹ needs u₀₀ ≠ 0; a pair transposition under PC24 handles u₀₀ = 0. Closure is needed only for the
  CNOT-only lower route. Both are stated in §4.1 and §4.2.
- **C3.** The full scope paragraph is in §4.2, and the real-test limit is in §4.3.
- **C4.** The control now runs through the same `scan` → `branch` computation as the exhaustive scan (`run_split` no
  longer exists): identity permutation, then a Hadamard post-map. It flags 4 full-support non-monomial branches, and
  its row-monomial check fails as it should.
  - `monomial_branch.py`, run twice, gives byte-identical output (`ffc67f36…`, 5 PASS, rc 0).
  - Scan counts are unchanged: 92160 and 18432 full-support branches, all monomial.
  - The lemma is restated as "at most one nonzero entry per row".
- **C5.** The `PhaseFreeRichness` swaps conjunct, `hU`/`hM` and :194 are added, and Σ0 is re-tagged as a [W]
  cone-level reading.
- **C6.** See (4).
- **C7.** "Irredundant" replaces "minimal", and the dependence of O-B on O-A is stated.

## (4) Diff from original to corrected, and the new K(Z_F) three-token model

**The three-token model is sound.** K₃ = cone{X⊗τ : X ∈ K(Z_F), τ a token state} ∪ products₃.
- MAX₃ holds: ⟨abc|X⊗τ|abc⟩ = ⟨ab|X|ab⟩⟨c|τ|c⟩ ≥ 0, since X is block-positive.
- RO₃ holds: the branch is X⊗P_kτP_k. Checked symbolically.
- ATT holds: take τ = |0⟩⟨0|.
- DIS holds for token 3, as Σ3 defines it: Tr₃(X⊗τ) = (Tr τ)X, checked symbolically, and Tr₃ of a product is in SEP.
- H1₃ holds by the products.
- NC₃ fails in both variants, by B3.
- Scope: DIS is only for token 3, and nothing beyond three tokens is claimed. The ledger states both.

**Other changes.**
- The classification is lowered from NEW to ELABORATING.
- §6 now lists the K_H\* extreme-ray inference and the K(Z_F) model as unreviewed [W]. Both are reviewed here and
  found sound.

No new overclaims, apart from the following.

- **R1 (correction required; wording only).** AW-F1 (§4.5 item 5, lines 300–301) and §5 (line 329) say:
  "a fixture that survives every pair-level native clause also survives any derivation confined to two-token native
  data" / "A source for O-B that uses only two-token native data cannot exclude K(Z_F)".
  - **What is shown.** K(Z_F) satisfies Σ2: PC24, readout and discard closure, MI, and product-test validity.
    Equivalently, it is closed under two-token native protocols and valid on product tests.
  - **Why the general statement fails.** It quantifies over every derivation. A derivation from two-token native data
    of a different type does exclude K(Z_F): defining the state cone as the reachable closure of native images of the
    domain products gives a cone inside Q3, so z ∉ K. That route is barred only by MEMO R4's non-circularity rule,
    not by K(Z_F)'s survival.
  - **Fix.** Scope both sentences to "any non-circular derivation whose output is a pair-level compatibility or
    validity clause (Σ2-type; no reachable-closure definition, MEMO R4)". The same applies to "satisfies every
    pair-level native clause (Σ2)" in item 5: read it as "every clause of Σ2".
- **Notes (non-blocking).**
  - "Every form of O-B depends on O-A" (line 333) should say "every known form".
  - "A countable family can reach at most the dense endpoint" (line 343) cites theorems that only exclude exactness.
    The phrase is acceptable if it means "not the exact endpoint", but it should say that.

## Commands and outputs

- Replays: `revf2/rerun/kh_pc24.rev{1,2}.out` and `revf2/rerun/monomial_branch.v2.rev{1,2}.out`. The digests equal
  the author's.
- Own checks: `revf2/rereview_check.out`, covering the K_H\* witness by solving for ν, maxCone failing CNOT, and the
  K(Z_F) three-token model's DIS and RO₃ identities.

# Thread E — K2 formalization prep: RESULT

This is a prospective decomposition, written read-only. Nothing here is frozen, claimed or governed. The scripts and
logs are in `threads/E/`:
- `e_exact.py` / `e_exact.log`: integer and Gaussian-integer arithmetic, an independent re-implementation;
- `e_sym.py` / `e_sym.log`: sympy, exact;
- `e_so15_q.py` / `e_so15_q.log`: Fractions;
- `e_so15_fast.py` / `e_so15_fast.log`: a modular lower bound, kept only as a cross-check;
- `replay/`: copies of every K2 script, with their logs.

## 1. Finding

Every K2.0–K2.3 figure reproduced exactly on re-run of the copied scripts, and again in an independent
re-implementation that shares only the gate builder:
- the relations;
- the value formula;
- the 32 admissible gates, closed under inverse, 8 of them involutions;
- the 8 O-classes and 16 SO-classes;
- the four unitary gates;
- the 8 surviving and 8 failing SO-classes, each failure with an exact witness at −2;
- the Wigner-type table;
- the 15-dimensional Lie closures (the `su(4)` image, or its `PT_B` conjugate) and the 105-dimensional `so(15)` closures;
- `Q ≠ PT(Q)`, `PT_A(Q) = PT_B(Q)`, and the three-copy even parity.

No figure failed to reproduce. Three steps of the note are currently numerical or rest on code that does not establish
them: survivor positivity, "each gate alone has minimum ≈ 0", and the dense-rotation words. Exact replacements now exist
for all three (Section 2).

The re-run also produced two structural facts the note does not state.

**(i) Factorization.** Every one of the 32 gates is `(D₁⊗D₂)·CNOT·(D₃⊗D₄)`, with the `Dᵢ` local sign relabellings
`diag(1, ±1, ±1, ±1)`. None of the 32 non-admissible unit-modulus sign members factors this way. So the sufficiency half
of the positivity step becomes exact plus three written lines, and no longer rests on the written disc-range argument.

**(ii) A reflection-parity selection rule.** With `o = (det D₁, det D₂)` and `i = (det D₃, det D₄)` as bits:
- closure positivity keeps a gate exactly when `o_A⊕i_A = o_B⊕i_B`;
- the time bit `o_A⊕i_A` separates unitary from antiunitary;
- the cone bit `o_A⊕o_B` separates `Q` from `PT_B(Q)`.

So the note's two Z₂'s are explicit determinant bits.

A favourable candidate follows from (ii): **idle extension to a third copy excludes the antiunitary Z₂ by a finite
principle.** Within the relabelled class `(L_A⊗L_B⊗L_C)Q_ABC`:
- `G⊗id_C` leaves some cone of the class invariant for the unitary-type survivors (classes 0, 1, 12, 13);
- it leaves none invariant for the antiunitary-type survivors (6, 7, 10, 11) or for any failure.

The note had left this exclusion to K2.2's connected-group resource. Mathematically it is the known non-complete-positivity
of the transpose. It counts as new only as the finite replacement for that connected-group argument. It holds only
within the relabelled class, and a written countermodel shows that the class restriction is load-bearing (Section 3).

## 2. Evidence level

### 2a. Reproduction of the note's figures

Each script was copied to `threads/E/replay/` and run there unmodified. Runtimes are on this container.

| note figure | script (copy) | reproduced | layer as the note states it | flag |
| --- | --- | --- | --- | --- |
| Rt, Rc force `A` diagonal, `K` antidiagonal, all four `M₀` | `k20_classify.py` (1 s) | yes | exact (sympy linear solve) | — |
| the value formula, all four `M₀` | `k20_part2.py` (11 s) | yes | exact polynomial identity | — |
| 8 sign solutions, 32 gates, inverse-closed, invertible, 8 with `G² = I` | `k20_part2.py` | yes | exact | **F8**: the inverse is `G(M₀, ε₁A⁻¹, −ε₂K⁻¹)`, not literally "reciprocal entries" (`e_sym` S1); the moduli argument is unaffected |
| 8 O-classes of size 4, 16 SO-classes of size 2 | `k20_part2.py` | yes | exact | — |
| 4 unitary gates; 6 of 8 O-classes contain no unitary | `k20_part3.py` (11 s) | yes | exact (Choi rank 1) | **F9**: the Choi test does not check trace preservation; harmless, since every gate has row and column `u⊗u` equal to `e₀` (`e_exact` A) |
| "each gate alone has min ≈ 0 on products" | `k20_part4.py` / `k20_part7.py` | yes (≈ −0.0000) | **numerical** (float block-coordinate descent, seeded RNG) | **F1**: replaced by the factorization, exact (`e_exact` C, `e_sym` S4) |
| closure positivity: 8 fail at −2, 8 survive; group orders 8 or 16 | `k20_part4.py` (18 s), `k20_part7.py` (14 s) | yes | failures: exact integer witness. Survivors: **numerical** (min ≈ 0). The group is enumerated in **float64** with rounded keys | **F2**: replaced by an integer group closure, the same −2 witnesses, and a Wigner certificate on every element of every surviving group (`e_exact` D) |
| the survivor/failure Wigner tags (`k20_part6` table) | `k20_part6.py` (28 s) | yes | exact | cross-implemented by a Pauli-algebra (anti)automorphism test, with identical tags (`e_exact` B) |
| dense local rotations keep min ≈ 0 | `k20_part5.py` (25 s) | yes (≈ −0.0000) | **numerical only** (scipy random rotations) | **F3**: exploration only; superseded by K2.2a (exact) and K2.2b (written) |
| K2.2a: all 8 survivors 15-dimensional, the `su(4)` image or `PT_B·su(4)·PT_B` | `k22a_closure.py` (19 s) | yes | exact (Fractions) | **F6**: the `su(4)` image takes `int(sp.re(·))`, which would drop an imaginary part silently; rebuilt with an assertion, same result (`e_exact` E) |
| negative controls (identity, SWAP, `N⊗N`) at 6; 8 failures at 105; class 1 at 15 | `k22a_controls2.py` | yes, byte-identical log. **Runtime: see 2c** | exact (Fractions, depth-first queue) | cheaper exact replay: `e_so15_q.py`, 25 s in all (2c) |
| the same, original routine | `k22a_controls.py` | **partial**: stopped at the 20-minute cap after class 2 (105, matching) | exact | see 2c |
| failing `G` fixes `u⊗u` and is orthogonal; local generators antisymmetric; `‖w‖² = 3` | `k22a_so15.py` (14 s) | yes | exact | **F7**: `‖w‖² = 3` is checked at one rational point. The identity `‖a‖² + ‖b‖² + ‖a‖²‖b‖² = 3` for unit `a, b` is written (trivial) |
| K2.3 (1): branch rule on 64 pairs; (2) `PT(Bell)` eigenvalues `{−1/2, 1/2³}`; (4) 512 triples even, all 4 even assignments | `k23_cocycle.py` (33 s) | yes | exact | **F5**: the printed line "odd assignments realised: none" comes from an expression that prints `none` whenever *some* assignment is unrealised. The load-bearing check is the `assert` at line 40, which passes. `e_exact` F replaces it with an exact set equality |
| K2.3 (3): `PT_A = T·PT_B`; "T an antiunitary symmetry of Q" | `k23_cocycle.py` | first part yes | exact | **F4**: the conjunct `unitary(T*T)` is `unitary(I)` and is vacuous. The script shows only that `T` is not unitary. `e_exact` B shows that `T` is an antiautomorphism, i.e. antiunitary |
| "the orbit hull `C_H` is strictly inside `Q`" (the K2.1 argument) | none listed | **not replayed** | written only | no K2.1 script is named in the note |
| `k2_first.py`: `|H| = 8`, the witness `ψ`, reflected CNOT `G'` with eigenvalue `−1/2` | `k2_first.py` (1 s) | yes | exact | — |

### 2b. New results of this thread (all exact unless marked)

Exact:
- **E-A** (`e_exact` A): 32 gates; each is unital and trace-preserving; each is a signed permutation; the set is closed
  under inverse; 8 involutions. The builder at `(I, I, J)` equals an independently computed CNOT transfer matrix
  (Gaussian integers).
- **E-B** (`e_exact` B): the Pauli-algebra Wigner test reproduces all 16 class tags; exactly 4 of the 32 gates are
  unitary.
- **E-C** (`e_exact` C; `e_sym` S4): the factorization `G = (D₁⊗D₂)·CNOT·(D₃⊗D₄)` holds for all 32, and the parity
  rule is checked for every class. The polynomial form, with `c = k₂a₁`, is
  `value_G(s,t,f,g) = value_CNOT(As, R^c M₀t, f, R^c g)`, where `R^c` is the identity for `c = +1` and the `y`-reflection
  for `c = −1`.
- **E-D** (`e_exact` D): the group `⟨G, N⊗I, I⊗N⟩` is enumerated in integers, with orders `{0, 1, 6, 7}: 8` and every
  other class `16`. The failures give exact witnesses at −2. In the survivors, every element is a unitary or antiunitary
  symmetry of `Q` (classes 1, 6, 10, 13) or of `PT_B(Q)` (0, 7, 11, 12).
- **E-E** (`e_exact` E): the `su(4)` image, built from the Pauli table, is 15-dimensional, contains local
  `so(3)⊕so(3)`, and is distinct from its `PT_B` conjugate. All 8 survivors close to exactly the right one.
- **E-F** (`e_exact` F): the branch rule, the parity rule and the idle-extension result.

Exact and written together:
- **E-S** (`e_sym` S1–S3): the inverse in the family; `WᵀW` in symbolic form; at unit moduli
  `WᵀW = |s|²I + s₁s₂(a₁k₁ + a₂k₂)·swap`; and the necessity quadratic, with discriminant `α² + β² − 1`. The case
  analysis around them is written.

### 2c. Runtime of the slow scripts

- `k22a_controls2.py`: **1009 s (about 17 min)**, exit 0; its output is byte-identical to `k2/k22a_controls2.log` (`diff` empty). It runs close to the 20-minute budget.
- `k22a_controls.py` (original, non-incremental): **stopped at the 20-minute cap** (exit 124) after the three negative controls, all 6, and failing class 2, 105. Each closure step recomputes the full rank, so it is impractical, and the note does not cite it: its table is `controls2`'s. Recorded as not completed. The cheaper exact replay is `e_so15_q.py`.
- `e_so15_q.py`: the same 105 for all 8 failures in about 2.4 s each, 25 s in all.
  - It uses no floating point and no modular arithmetic.
  - The upper bound is the containment in `so(15)`, checked in integers.
  - The lower bound is 105 integer brackets of rank 105 over `ℚ`.
- `e_so15_fast.py`: the same certificate with the rank taken mod `2⁶¹−1`, which is a sound lower bound. It is kept only
  as a cross-check, since NB-1's probe convention excludes modular arithmetic.

### 2d. Status of the K2 steps

- **Exact**: P1, P2, P3, P5–P9, P13 (finite part), P14 (finite part).
- **Written, with exact inputs**: P4 assembly, P10 group closure, P11 cone exclusion, P12, the P13 coboundary and gauge
  reading, the P14 scope.
- **Literature-standard ingredients**, named in Section 4 and not re-proved here:
  - Kadison/Wigner: order automorphisms of PSD are `Ad U` or `T∘Ad U`;
  - the Lie subgroup correspondence;
  - `PU(4)` is transitive on pure states.
- **Numerical, not to be cited as evidence**: F1, F2 (survivors), F3.

## 3. Countermodels and controls

Every check below is in a log in `threads/E/` and printed PASS. `e_exact`: 37 checks, 0 failures. `e_sym`: 11 checks,
0 failures. `e_so15_q`: 8 of 8.

**Pauli/Wigner test (cross-implementation control).** It is a different algorithm from the K2 Choi-rank test: exact
Gaussian-integer (anti)multiplicativity on all Pauli pairs.
- Controls: CNOT, identity, `N⊗I` and `I⊗N` are U; `T` and `T·CNOT` are A.
- Countercontrols: `PT_A` and `PT_B` are neither, and a non-invertible unital map is rejected.
- Agreement with the K2 tags on all 16 classes.

**Factorization (favourable, so pressure-tested).**
- Countercontrol: all 32 unit-modulus sign members with `a₁k₁ + a₂k₂ ≠ 0` fail to factor, and none is in the
  admissible set. A non-unit member (`a₁ = 2`) fails to factor.
- The search is exhaustive over `8⁴` local sign quadruples. A first run picked a countercontrol tuple, `(1, −1, 1, 1)`,
  that is in fact admissible; it factored, which exposed the mistake. The countercontrol was replaced by the full
  enumeration of non-solutions.

**Closure positivity.**
- Survivors: an exact certificate per group element, not a minimization.
- Failures: the exact witnesses `s = u+x`, `t = u+y`, `f = u∓x`, `g = u−y` at −2 match the note.

**Lie closure.**
- Negative controls: identity and `N⊗N` give 6, as in the note.
- The `su(4)` image and its `PT_B` conjugate are distinct spans (union > 15), so "equals `su(4)`" is not vacuous.
- The 105 is replayed by two routines (2c). The `so(15)` upper bound is an integer containment check.

**Three copies.**
- The branch test asserts that exactly one of `Q` and `PT(Q)` holds in each of the 64 cases.
- The realised assignments are exactly the 4 even ones. The note's printed line was not relied on (F5).

**Idle extension (favourable, so pressure-tested).**
- Controls: `CNOT⊗id` preserves `Q_ABC`, and `T_ABC` is an antiunitary symmetry of `Q_ABC`.
- Countercontrol: `T_AB⊗id_C` is not a Wigner symmetry of `Q_ABC`.
- Completeness of the enumeration (written): any `O(3)³` relabelling is `V·R^b` with `V` local unitary, and `V`
  preserves `R^b Q`. So the 512 sign relabellings cover every cone of the class: four distinct cones up to the global
  flip `T`.
- `⊆` versus `=` (written): each gate is orthogonal, fixes `u`, and `Q` is self-dual. So `Φ(Q) ⊆ Q` implies
  `Φᵀ(Q) ⊆ Q`, which gives equality. Invariance and self-map are therefore the same test here.
- **Scope countermodel (written).** `C = cone(Q_AB ⊗ L_C)`, the minimal composite of the quantum pair with a ball, is
  invariant under `(T·U)_AB ⊗ id_C`. Its `AB` marginal is `Q`, but its `BC` and `CA` marginals are `min` (separable).
  So the exclusion needs every pair's marginal to be `Q` or `PT(Q)`, and fails without that hypothesis.
- Not tested: whether a tripartite cone outside the relabelled class, with all three pair marginals `Q`/`PT(Q)`, can
  be `T_AB⊗id`-invariant. That is open. A partial written argument covers cones inside `Q_ABC`. A cone invariant under
  `T_AB⊗id` there is the set of states PPT across `AB|C`. Its `BC` marginals are then PPT, hence separable for two
  qubits, so no such cone has `Q` marginals. Cones not contained in `Q_ABC` are uncovered.

**Not run.**
- Any Lean build (forbidden).
- Any K2.1 replay (no script).
- Any search over intermediate `G`-invariant cones for the finite group alone, without `SO(3)`. The note marks these
  "not classified".

## 4. Proposed next theorem

The decomposition below is prospective. **Layer** means where each proposition should be certified: kernel (Lean),
exact (a CI-replayed, deterministic, float-free probe), or written.

**Premises.** All are unsourced except NB-1's.
- **NB1** (only `F, P±, Rt, Rc` with one `N`, `d = 3`): NB-1's hypotheses at `d = 3`. Their S1/S2 output is the
  family `(M₀, A, K)`.
- **CP0**: the native gates are closed under composition with `N⊗I` and `I⊗N`, and each maps `min` into `max`.
- **LG**: continuous local `SO(3)×SO(3)` is native. This premise is not in NB-1, which uses no continuous group.
- **RC3**: the three-copy composite lies in the relabelled class `(L_A⊗L_B⊗L_C)Q_ABC`.
- **IE**: a native gate on `AB` acts as `G⊗id_C` on the three-copy composite and preserves its cone.

| id | statement | layer | controls / countercontrols | cheapest exact replay |
| --- | --- | --- | --- | --- |
| P0 | Under NB1, `G` is determined by `M₀ = diag(1, ε₁, ε₂, 1)` and real 2×2 matrices `A`, `K` on `T = ⟨x, y⟩` through the builder | written for general `d`, exact at `d = 3` (NB-1 probe, CI) — inherited, not re-proved | NB-1 C3 positive control | NB-1 probe |
| P1 | `Rt ∧ Rc ⇔ A` diagonal and `K` antidiagonal (each `M₀`) | exact | frame F re-checked at every `M₀` | `k20_classify.py`, 1 s |
| P2 | the value formula `(1+s_z f_z)(1+g_x t′_x) + …` | exact | — | `k20_part2.py` (1) |
| P3 | `G(M₀,A,K)⁻¹ = G(M₀, ε₁A⁻¹, −ε₂K⁻¹)` | exact | — | `e_sym` S1 |
| P4 | P± `⇒ |aᵢ| = |kᵢ| = 1` and `a₁k₁ + a₂k₂ = 0`. Necessity: at the S3 point the worst value is `(1+|β|)c² + 2αc + (1−|β|)`, which with P⁻ through P3 forces unit moduli and column orthogonality | **kernel candidate**: the scalar step, from `max(|a₁|,|k₂|) ≤ 1`, `max(|a₂|,|k₁|) ≤ 1`, the reciprocal bounds and `∀s, |s|² + |s₁s₂||a₁k₁+a₂k₂| ≤ 1` to the sign solutions; the reduction to these inequalities is written | `WᵀW` form (exact); the non-solution countercontrol | `e_sym` S2–S3 |
| P5 | exactly 32 admissible gates; inverse-closed; 8 involutions; all unital, trace-preserving and signed permutations | exact; the sign count `#{a₁k₁+a₂k₂=0} = 8` is a kernel candidate (`decide`) | — | `e_exact` A |
| **P6** | every admissible `G = (D₁⊗D₂)·CNOT·(D₃⊗D₄)` with the `Dᵢ` sign relabellings, and no non-admissible member is of this form. Hence P± for all 32: the `D`'s preserve `min` and `max`, and `CNOT(min) ⊆ Q ⊆ max` | exact (finite); the consequence is written, 3 lines, from the abstract cone lemma L-e | 32 non-solutions, `a₁ = 2` | `e_exact` C, `e_sym` S4 |
| P7 | 8 O-classes and 16 SO-classes | exact | — | `e_exact` A |
| P8 | the Wigner-type table: survivors U (1, 13), A (6, 10), `PT_B·U·PT_B` (0, 12), `PT_B·A·PT_B` (7, 11) | exact; the meaning of "symmetry of Q" via Kadison/Wigner is literature-standard and written | two independent tests agree | `e_exact` B |
| **P9** | closure positivity (CP0) holds iff `o_A⊕i_A = o_B⊕i_B`: survivors are the 8 even classes, failures the 8 odd ones; time bit `o_A⊕i_A`, cone bit `o_A⊕o_B` | exact (finite). Survivor positivity: exact certificate plus a written lemma (a Wigner symmetry of `Q` or `PT_B(Q)` maps `min` into `max`). Failure: exact witness −2 | failures' witnesses | `e_exact` C–D |
| P10 | with LG, the Lie algebra generated is exactly 15-dimensional, the `su(4)` image or its `PT_B` conjugate. The closure group is `PU(4)`, `PU(4) ⊔ T·PU(4)`, or their `PT_B` conjugates | dimension and identification: exact. Group: written (Lie correspondence, compactness, `G` of finite order normalizing the identity component) | identity, `N⊗N` → 6; the conjugate spans differ | `e_exact` E |
| P11 | for the 8 odd classes with LG, the algebra is `so(15)` and no `SO(15)`-invariant closed convex cone lies between `min` and `max` | dimension: exact. Classification of the invariant cones as Lorentz cones `L_c`: written. `√3 ≤ c ≤ 1/√3` impossible: **kernel candidate** (`norm_num`) | — | `e_so15_q.py`, 25 s |
| P12 | (the K2.2b cone theorem) with LG, any closed convex cone `C` with `min ⊆ C ⊆ max` invariant under the P10 closure equals `Q` (even classes with cone bit 0) or `PT_B(Q)` (cone bit 1) | written. A kernel candidate later, in K3's complex-matrix vocabulary: `PSD` is the unique `conjChannel`-invariant cone between product states and the dual of product effects | the P11 failures show the selector is positivity, not Lie richness | — |
| P13 | with RC3, pair branch `ε_XY = s_X ⊕ s_Y` with `s_X = [det L_X = −1]`. Triangle parity is even, all even assignments occur, and orientation is a local gauge | finite part exact. The cocycle lemma on 3 vertices over `ZMod 2` (realizable iff the coboundary sum is 0): **kernel candidate** (`decide`). The gauge reading: written | 64-pair assertion | `e_exact` F, `k23_cocycle.py` |
| **P14** | with RC3 and IE, `G⊗id_C` preserves some cone of the class iff `G` is unitary-type: classes 0, 1, 12, 13 yes; 6, 7, 10, 11 and all failures no | exact (finite). `⊆ ⇔ =` and the scope countermodel: written | `T_AB⊗id` is not Wigner; `CNOT⊗id` is | `e_exact` F |

**The assembled candidate (written; not to be stated as proved).** Under NB1, CP0, LG, RC3 and IE, each copy pair's
composite is the standard quantum one up to a local orientation gauge, and the native CNOT is a unitary symmetry of it.

**Kernel candidates.** All are scalar or combinatorial, need no new definitions, and import Mathlib only.

| name | statement |
| --- | --- |
| L-a | the P4 scalar sign lemma |
| L-b | the sign count is 8 (`decide`) |
| L-c | the 3-vertex Z₂ cocycle iff coboundary (`decide`) |
| L-d | `¬(√3 ≤ c ∧ c ≤ 1/√3)` |
| L-e | the abstract cone lemma: if `Φ(Q) = Q` and `min ⊆ Q ⊆ max` then `Φ(min) ⊆ max` |
| L-f | in K3 vocabulary, the Pauli-transfer matrix of `conjChannel CNOT` equals the builder's `G_CN`; a finite 4×4 computation |

**Relation to K3 machinery: open obligations.**
- **O1, the dictionary.** The real 16-dimensional Bloch composite with cone `Q` must be identified with
  `Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ`, Hermitian and PSD. Under that identification, unitary-type survivors are
  `conjChannel U` (MonoidalCompletion.lean:360). Nothing in the corpus states this map; L-f is its first instance.
- **O2, the antiunitary and CP bridge.** Classes 6 and 10 are `T∘Ad U`. They are not completely positive, so they are
  never `IsTypedKrausInstrument` (TypedCompletion.lean:448).
  - Once the shadow is quantum, `typed_determined_iff` (TypedCompletion.lean:850) makes them unavailable. Using that to
    exclude them is circular for the K-programme, since K3 is conditional on complex kinematics (ROADMAP.md:978).
  - They are **not** AntiunitaryInvariance's `transposeMap` (AntiunitaryInvariance.lean:41). That is the global
    conjugation `T∘g∘T`, a symmetry of all circuit data (`circuit_invariance`, :71; `unitary_channel_transpose`, :143),
    and it preserves complete positivity (`transposeMap_kraus`, :97). The two must not be conflated.
  - The non-circular finite exclusion is P14. Its K3 counterpart is availability on extended carriers (`availExt` on
    `A × Fin n`); stating P14 there is open.
- **O3, gauge transport.** The `PT_B(Q)` branch is the image of `Q` under a one-factor ball reflection. The corpus's
  `RelabellingInvariant` (EmbeddedObservation.lean:106) transports only along carrier bijections. A GPT-isomorphism
  transport lemma is needed before K3 results apply on the reflected branch.
- **O4, the Lie route.**
  - P10 is the two-copy Bloch shadow of `HControl` (MonoidalCompletion.lean:349): the control Lie algebra contains
    `su(4)`.
  - `LieRankRichness` (MicroscopicReversibility.lean:93) needs every ancilla size `A × Fin n`, which feeds
    `control_of_lieRank` (:114), then `HasCompositeUnitaryControl` (OperationalAssembly.lean:665) and
    `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136).
  - K2 covers two copies only, and qubit powers at most. The passage to arbitrary `n` is open.
- **O5, the premises.** Neither LG nor IE is sourced. Their relation to `DrivesElementary` (SubstratumSource.lean:77)
  and to the K∞ list (ROADMAP.md:995–1003) is open. Identical-copy covariance is inherited from NB-1.

**Productivity test (AGENTS.md §A.31).**
- P6/P9: a gem. It is strictly stronger than the note's restatement: it turns the sufficiency half of positivity into an
  exact identity, and makes both Z₂'s explicit invariants.
- P14: borderline-new. It is a finite exclusion of the antiunitary branch, but its mathematical core is the known
  non-complete-positivity of the transpose, and it is valid only within RC3.

## 5. Dependencies

**Dependency graph.**

```text
NB-1 (S1,S2 @ d=3: written + exact; nb1_kernel_core) ──► P0 ──► P1 ──► P2 ─┐
                                                                P3 ───────┴─► P4 ──► P5 ──┬─► P6 ──► P9 ◄── CP0
                                                                                          ├─► P7 ────┘│
                                                                                          └─► P8 ─────┘
P9 + LG ──► P10 ──► P12          P5 (odd classes) + LG ──► P11  (countercontrol to "Lie richness selects")
P9 + RC3 ──► P13 (orientation gauge)          P9 + RC3 + IE ──► P14 (antiunitary Z₂ excluded)
P12 + P13 + P14 ──► assembled K2 candidate ──(O1–O5)──► K3 machinery
```

**Other threads.**
- Thread B (copy structure, three-copy consistency) overlaps P13 and P14; its NOT-conjugacy reduction bears on
  identical-copy covariance, which P0 inherits.
- Thread A (successor foundations): LG and IE are candidates for its premise list, and are not mine to freeze.
- No dependency on C or D.

**Corpus declarations** (at `wt-threads`, HEAD `4507b025`):

| what | where |
| --- | --- |
| NB-1 setting, hypotheses and the S1/S2 steps | NB-1 `preregistration.md`:178–212 |
| identical-copy covariance hazard | NB-1 `preregistration.md`:73–96 |
| `nb1_kernel_core` | `NativeGateBall.lean`:255 |
| NB-1 outcome | `result.md`:3 |
| roadmap K-rows | `ROADMAP.md`:978 (K3), 984 (K1), 991–994 (K2: "the antiunitary and complete-positivity bridge, and the relation to the K3 machinery are open"), 995–1003 (K∞, identical-copy covariance at 1000) |
| `typed_determined_iff` | `TypedCompletion.lean`:850 |
| `IsTypedKrausInstrument` | `TypedCompletion.lean`:448 |
| `transposeMap` | `AntiunitaryInvariance.lean`:41 |
| `circuit_invariance` | `AntiunitaryInvariance.lean`:71 |
| `transposeMap_kraus` | `AntiunitaryInvariance.lean`:97 |
| `unitary_channel_transpose` | `AntiunitaryInvariance.lean`:143 |
| `LieRankRichness` | `MicroscopicReversibility.lean`:93 |
| `control_of_lieRank` | `MicroscopicReversibility.lean`:114 |
| `HasCompositeUnitaryControl` | `OperationalAssembly.lean`:665 |
| `HControl` | `MonoidalCompletion.lean`:349 |
| `conjChannel` | `MonoidalCompletion.lean`:360 |
| `DrivesElementary` | `SubstratumSource.lean`:77 |
| `genTheory_qm_of_quantumArchitecture` | `SubstratumSource.lean`:136 |
| `fullInstruments_of_control` | `StinespringAssembly.lean`:197 |
| `RelabellingInvariant` | `EmbeddedObservation.lean`:106 |

**Unsourced premises.**
- Identical-copy covariance, through NB-1.
- CP0.
- LG, the continuous local group, used from P10 on.
- RC3.
- IE.

**Literature (standard, cited and not re-proved).**
- Kadison 1951 / Wigner: Jordan automorphisms of `M_n` are `Ad U` or `T∘Ad U`.
- The Lie subgroup correspondence.
- Transitivity of `PU(4)` on `CP³`.
- Separability of two-qubit PPT states (Horodecki 1996), used only in the partial written argument of Section 3.

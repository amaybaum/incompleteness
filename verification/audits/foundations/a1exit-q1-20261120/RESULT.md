# A1-EXIT Q1 — lattice restrictions: result

**Status.** Writer's paper-only research record. Paper derivations, reading of cited kernel
statements (none built here) and exact finite computations (`checks/`, §9). No manuscript, Lean or
registry edit; no premise adoption; no merge. A1 (Main posit ledger item (ii)) and A4
(`papers/Substratum.md`:98) are unchanged, and nothing here is a premise of an established claim.
Independent non-author review is required (§11). The preregistration is `PREREG.md`, pushed at
`fb03820fd` before any classification; this record follows its rule and controls unchanged.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20, Step 1, row Q1 (quoted in PREREG). Form: paper-only research record.

**Goal link (§A.47).** #1454 row P2-Q1, serving the owner's A1-exit objective. This unit decides
which consumers of A4's lattice clause hold on `ℤ^d`, on which periodic quotients they hold, and
which sentences Step 2 would correct. A4's final form is left to the A1-EXIT ledger.

**Source pin.** `main` at `9db518844df62151979acf6aac1d487b59c44907`. Notation as in PREREG §1:
`P ⊂ ℤ^3` is the period lattice (the brief's `Λ`; SM:222 uses `Λ` for the carrier `ℤ^d`),
`X_P = ℤ^3/P`, `P = 0` is `ℤ^3`, `P̄` is the image of `P` in `𝔽_2^3`, `D_3` the even-sum lattice,
`χ_η(n) = (−1)^{η·n}`. Layers: **[L]** kernel theorem (cited, not built), **[E]** exact computation
in `checks/q1_checks.py`, **[W]** paper derivation.

## 1. Controls

All preregistered controls hold (`checks/q1_checks.out`; exit status 0).

| ID | Result |
|---|---|
| K1 | On a window of `ℤ^3` nearest-neighbour hopping is odd-supported for the coordinate-sum parity, and both parities occur [E] |
| K2 | Every field of `Staggered.Gens` holds on `ℤ^3`, and `(Σ_i A_i)^2 δ_m = Σ_i S_i^2 δ_m` for the 8 classes `m mod 2` [E]; a phase-free countercontrol fails |
| K3 | O-A4's countermodels reproduce: `L = 3, 5` not bipartite with 1 corner of 8; `L = 4, 6` 8 corners; skew even-sum quotient bipartite with 4 corners; vertex stabilizers 720 (`L = 4`) and 48 (`L = 6`) [E] |
| K4 | Odd cubic tori `L = 3, 5` carry the staggered phases for no axis ordering [E] |
| K5 | The disguised-A1 test separates "`P ⊂ 2ℤ^3`" (contains `P = 0`) from "finite-index `P ⊂ 2ℤ^3`" (does not) [E] |
| K6 | This record changes only files under its own directory (§11) |

**Check-design note.** The first run of part C bundled a second expectation into the `4×4×6` check
("the corner span is invariant under the carrier's automorphisms") and failed on it: on `4×4×6` the
factor `C_4 × C_4` is the 4-cube, whose automorphisms mix corner characters with other momenta, as
on `L = 4`. The preregistered question of part C (does an automorphism relate the `X_3` line to the
`X_1` line?) was unaffected. The check now tests that question alone and reports the span as a
diagnostic.

## 2. Lattice conditions on `X_P`

**Lemma 1 (sign characters on a quotient).** For `s ∈ {±1}^3` the function `g(n) = ∏_j s_j^{n_j}` is
the unique `g : ℤ^3 → {±1}` with `g(0) = 1` and `g(n + e_j) = s_j g(n)`. It descends to `X_P` iff
`g(b) = 1` for every `b ∈ P`. With `s = (−1)^η`: `χ_η` is defined on `X_P` iff `η·b` is even for
all `b ∈ P`, i.e. iff `η` annihilates `P̄`. The defined corners form a subgroup of order
`2^{3 − rk P̄}`. [W]; brute-force edge consistency agrees with the closed form on 134 quotients [E, A].

Consequences [W, with E parts A and D]:

| Structure on `X_P` | Condition on `P` (iff) | Witness of the gap |
|---|---|---|
| (a) checkerboard `χ_{(1,1,1)}`; bipartite coupling graph | `P ⊂ D_3` | odd tori fail |
| (b) all eight corners | `P ⊂ 2ℤ^3` | skew `⟨(4,0,0),(0,4,0),(1,1,4)⟩`: 4 corners `{000, 001, 110, 111}` |
| (c) staggered phases of the ordering `(a_1, a_2, a_3)` | `P̄ ⊂ ⟨e_{a_3}⟩`: every period vector even off axis `a_3` | `4×4×3` carries them and is not bipartite; the skew even-sum quotient is bipartite and carries none |
| (d) hypercube blocking `n = 2y + η` | `P ⊂ 2ℤ^3` | skew even-sum quotient |
| (e) the cubic group acts on `X_P` | `gP = P` for `g ∈ O` (equivalently `O_h`, since `−1` fixes every lattice) | `4×4×6` |

*Proof of (c).* The fields of `Gens` (`verification/lean/OI_Staggered_Relations.lean`) realized by
`±1` multiplication operators and unit shifts force `e_{a_k}(n + e_{a_j}) = −e_{a_k}(n)` for `j < k`
and `= e_{a_k}(n)` otherwise, so by Lemma 1 `e_{a_k}` is, up to a constant, the character of the
indicator of `{a_1, …, a_{k−1}}`. These descend iff `b_{a_1}` and `b_{a_1} + b_{a_2}` are even for
every `b ∈ P`. In `3+1` dimensions with a non-periodic time axis the spatial condition is the same
when time is not last in the ordering, and is `P ⊂ 2ℤ^3` when it is last. `□`

**Lemma 2 (cubic-invariant period lattices).** A nonzero `O`-invariant `P` has finite index. *Proof.*
Take `b ∈ P` with `b_j ≠ 0`. The half-turn `R_j` about axis `j` is in `O`, and `b + R_j b = 2 b_j e_j ∈
P`. The 3-cycle of axes is in `O`, so `2 b_j e_k ∈ P` for every `k`. `□` [W]. Exhaustive Hermite
enumeration of all 596 457 sublattices of index ≤ 96 finds exactly nine `O`-invariant ones,
`mℤ^3`, `mD_3`, `mB_3` (`B_3 = {x : x_1 ≡ x_2 ≡ x_3 mod 2}`), and those inside `2ℤ^3` are the ones with
`m` even [E, part E]. The general statement for every index is the classification of cubic Bravais
lattices (sc, fcc, bcc); it is cited here, not proved, and nothing below depends on it.

So the class "`P` cubic-invariant and `P ⊂ 2ℤ^3`" is `ℤ^3` itself together with the finite quotients
by `2kℤ^3`, `2kD_3`, `2kB_3`: no cylinder or slab quotients occur.

## 3. Per-consumer classification

Verdicts per PREREG §3. "(i)" is the verdict on `ℤ^3`; "(ii)" is the class of quotients on which the
consumer holds. No consumer is (iii) or (iv).

| ID | Consumer | On `ℤ^3` | On `X_P` (ii) | Layer of the `ℤ^3` proof |
|---|---|---|---|---|
| C2 | Theorem 2, `D_st^2 = −¼□_lat` | (i) | iff every period vector is even off one axis (put last in the phase ordering); weaker than `P ⊂ 2ℤ^3`, independent of bipartiteness | [L] `Staggered.factorization` + [W] instance + [E] B |
| C3 | Theorem 3, onsite terms vanish ⟺ chiral symmetry | (i) | iff `P ⊂ D_3`; the theorem already states this as its hypothesis ("a lattice carrying both parity sectors", "opposite-parity hopping") | [L] `ChiralCenterRecovery.scalar_center_chiral_iff` over an arbitrary type + [E] K1 |
| C8 | Theorem 8, `4 = 1 ⊕ 3` under `O` | (i) | iff `P ⊂ 2ℤ^3` and `P` `O`-invariant | [L] `TasteBranching.theorem_8` (lattice-free) + [W] reading on `ℤ^3` |
| C8b | Theorem 8b, `μ(η) = σ(η)/3` | (i) | each value wherever `χ_η` is defined; the full statement iff `P ⊂ 2ℤ^3`. The printed proof's symmetry step needs `O`-invariance as well; with the arithmetic step (E5) it does not | [W] + [E] F |
| C10 | Theorem 10, step (ii): triplet sectors related by cubic symmetry | (i) | `P ⊂ 2ℤ^3` and `P` `O`-invariant suffices; fails on `4×4×6`. `O`-invariance is not necessary for some carrier symmetry to relate the three sectors (cyclic example) | [L] `TasteBranching.axis_transitive` + [W] + [E] C |
| C12 | Theorem 12, checkerboard = ε-grading | (i) | iff `P ⊂ 2ℤ^3` | [W] + existing probe `chirality_grading_probes.py` P1–P4 (lattice-free algebra) |
| C13 | Theorem 13, visible-sector grading identity, Schur complement | (i) | iff `P ⊂ 2ℤ^3` (through C12 and C3) | [W] + existing probes `chirality_grading_probes.py` P4, `hchi_selectivity_probes.py` (lattice-free) |
| C539 | SM:539, bipartite sentence | (i) | iff `P ⊂ D_3`, as the remark already states | [W] + [E] A |
| C539 | SM:539, spin–taste sentence | (i) | iff `P ⊂ 2ℤ^3`; the remark's "On the lattices that carry it" admits even-sum quotients, where it fails | [W] + [E] A, D |
| C1536 | SM:1536 (and SM:1506), "bipartite checkerboard structure" | (i) | iff `P ⊂ D_3`; stated without condition | [W] + [E] A |
| CA4 | A4's finite clause (Sub:98) | not used by any consumer above | — | — |

**Arguments for the `ℤ^3` verdicts.**

- *C2.* `Staggered.factorization` is proved for any `Gens` over any ring satisfying the file's `Rng`
  axioms. The ℤ-linear endomorphisms of the module of all functions `ℤ^d → ℤ` form such a ring; the
  unit shifts and the multiplication operators by the characters of (c) satisfy every field
  pointwise. Nothing is summed over infinitely many sites: each operator has finite range. [W]. Part
  B verifies the fields on a window of `ℤ^3` and the identity on `δ_m` for the eight classes of `m`
  mod 2; because the operators commute with translations by `2ℤ^3`, this covers every `m` [E].
- *C3.* The kernel theorem quantifies over an arbitrary index type `X` with a parity map, an
  odd-supported hopping and both parities present; no finiteness of `X` is assumed. On `ℤ^d` with the
  coordinate-sum parity the hypotheses hold (K1).
- *C8.* `theorem_8` is a statement about `𝔽_2^3` and the rotation action through `linkAct`. On `ℤ^3`
  the eight corners are the characters trivial on `2ℤ^3`, and `g ∈ O` acts by `χ_η ↦ χ_η ∘ g^{−1}`,
  which on `𝔽_2^3` is the axis permutation of `g` (sign changes are trivial mod 2): this is
  `cornerAct`. [W]
- *C8b.* `χ_η` satisfies `(1/6) Σ_{j,±} χ_η(n ± e_j) = (σ(η)/3) χ_η(n)` pointwise on `ℤ^3`, and
  `σ(X_j) = 1`, `σ(M_j) = −1` for each `j` by arithmetic. On `ℤ^3` the corner character is a bounded
  generalized eigenfunction (it is not in `ℓ²`); the coupling is the value of the symbol at `k = πη`.
  [W]; part F checks the eigenvalue relation on every test quotient where `χ_η` is defined [E].
- *C10.* `O` acts on `ℤ^3` by lattice automorphisms, which preserve the nearest-neighbour stencil
  and so commute with the wave rule. It permutes the three triplet corner lines transitively
  (`axis_transitive`). On `ℤ^3` the sectors are the spectral subspaces of the taste cells
  `πη + (−π/2, π/2]^3`; `O` maps the cell of `X_j` onto the cell of `X_{g(j)}`, so the restrictions
  are unitarily equivalent. [W]. The rest of Theorem 10 (H-spin', H-link, Theorem 15) does not use the
  lattice shape (O-A4 row 17) and keeps its stated conditions.
- *C12.* On `ℤ^3` (and on `ℤ^4` with time) the blocking `n = 2y + η` is a bijection
  `ℤ^3 → 2ℤ^3 × {0,1}^3`, and the grading identity is the `Γ(η)` algebra on the 16-dimensional
  spin⊗taste fibre, which `chirality_grading_probes.py` P1–P4 certifies without reference to a
  lattice size. Its P5 runs on the `L = 4` four-dimensional torus, which lies in the class `P ⊂ 2ℤ^4`.
  [W]
- *C13.* Step (ii) is Theorem 3 on `ℤ^3`. Step (iii)'s identity is fibre algebra (P4). The Schur
  complement needs no infinite-volume inversion: by (ii) the odd–odd block of the hopping vanishes,
  so the hidden block is site-diagonal (on the free substratum it is the time term `2 cos ω`,
  SM:569), and `G_oo` is its pointwise inverse wherever that is nonzero. No continuation hypothesis of
  the O-A4 §6.1 kind (H-cont) enters. Steps (iv)–(v) are conditional on H-χ' and H-spin' as stated.
  [W]
- *C539, C1536.* `ℤ^3` is bipartite and carries the blocking (Lemma 1, `P = 0`).

**Countermodels for the quotient verdicts** [E]. Odd tori (C3 hypothesis, C539 bipartite, C1536,
and every corner statement); the skew even-sum quotient `⟨(4,0,0),(0,4,0),(1,1,4)⟩` (bipartite,
only the corners `{000, 001, 110, 111}`: one singlet pair and one axis pair, no triplet, no blocking,
no staggered phases); the `4×4×3` torus (staggered phases and Theorem 2's identity hold, no
checkerboard); the `4×4×6` torus (all eight corners; `P` not `O`-invariant; its vertex stabilizer has
order 48 but orbits of sizes 4 and 2 on the six links, and every automorphism maps the `X_3` corner
line to itself, so no carrier symmetry relates `X_3` to `X_1`; the taste-cell spectra of `σ` around
`X_1` and `X_3` differ). The cyclic quotient `⟨(2,4,0),(0,2,4),(4,0,2)⟩` (index 72, inside `2ℤ^3`,
invariant under the 3-cycle of axes, not `O`-invariant) shows `O`-invariance is not necessary for C10.

**Theorem recovery.** No consumer loses support on `ℤ^3`, and no unrefuted claim is narrowed. The
corrections of §7 state the lattice class on which each existing statement already holds.

## 4. Disguised-A1 check (safeguard 1)

| Class `W` (condition `Q` on `P`) | DA1: `P = 0` satisfies `Q` | DA2: parity or symmetry only, no size bound | DA3: `Q` is the proof's condition |
|---|---|---|---|
| even off one axis (C2) | yes | yes | Lemma 1(c) |
| `P ⊂ D_3` (C3, C539 bipartite, C1536) | yes | yes | Lemma 1(a) |
| `P ⊂ 2ℤ^3` (C8b, C12, C13, C539 spin–taste) | yes | yes | Lemma 1(b), (d) |
| `P ⊂ 2ℤ^3`, `P` `O`-invariant (C8, C10) | yes | yes; by Lemma 2 it is the disjunction "`P = 0`, or `P` of finite index", and the first alternative is infinite | Lemma 1(b), (e) |

Every class contains `ℤ^3`, whose configuration space with a nontrivial finite alphabet is infinite
(kernel `WaveSubstratumUnbounded.waveZ_not_A1`, the `L = 0` instance of the wave substratum, read not
built). None of the conditions mentions the number of sites or configurations, and none is a
finite-index condition added beside the one the proof uses. K5 shows the test rejects a class that
does add one. All classes pass. Q1 introduces no finiteness hypothesis; the only finiteness in the
consumers' context is A4's finite clause, which none of them uses.

## 5. Further findings

- **Vertex-stabilizer order does not identify the point group.** The `4×4×6` torus has a vertex
  stabilizer of order 48 (abstractly `S_4 × ℤ_2`, like `O_h`), but it fixes the pair `±e_3` and does
  not act as the cubic point group. A check of "order 48" therefore does not certify a cubic action.
- **On `L = 4` the corner span is not invariant under the carrier's automorphisms.** The eigenvalue
  `σ = 1` of `C_4^3` has multiplicity 15 (three corners `X_j` and twelve momenta `(±π/2, ±π/2, 0)` up to
  axis order), and the 720-element stabilizer mixes them. Theorem 8 is stated "under the cubic group
  O" and holds there; the taste decomposition is not intrinsic to the full symmetry of that carrier.
  This refines O-A4 §7.1 and needs no correction, since no consumer claims the full automorphism group.
- **Three distinct conditions.** Staggered phases (C2), checkerboard (C3) and blocking (C12) are
  three different conditions on `P`. Neither of the first two implies the other (`4×4×3`; the skew
  even-sum quotient), and the third implies both.

## 6. Census of secondary consumers

`checks/q1_dispositions.py` assigns each of the 216 census lines one disposition (PREREG §2) and
exits 0 only if the assignment is complete and every FULL line is an exact mirror of a disposed
chapter line. Result: P 14, R 10, I 97, S 70, A4 11, N 14 (`checks/q1_dispositions.json`).

- **R lines with a proposed correction:** SM:222 (E1), SM:1506 (E3), ch06:22, ch06:24, ch06:30 and
  their FULL mirrors 1533, 1535, 1541 (E4).
- **R line without correction:** appendix-b:378 ("on a d = 3 simple cubic lattice" names the Bravais
  lattice `ℤ^3`; true as stated).
- **I lines** use a primary consumer's conclusion, or the corners and tastes of `Λ`; SM:134 and
  SM:136 (the `O_h`-invariant checkerboard partition) are covered by E1. Main:218 describes an open
  step and asserts no lattice property; Main is unaffected.
- **S lines** are the observer-level isotropy results already classified by O-A4 rows 13–17, point-group
  algebra, the stencil on `ℤ^3` (Main:674, :678), and Proposition 20's abstract bipartite `C_4` ring.
- **A4 lines** (Sub:98, Sub:157, SM:202, ch02:82, ch02:96, ch05:65, ch18:242, FULL mirrors) restate A4's
  finite class. They need no Q1 condition; their disposition belongs to the A1-EXIT ledger.

## 7. Proposed Step 2 corrections (not applied)

Each is the minimal text that makes a sentence true on the class the manuscripts admit (PREREG §6).
Quoted old strings are exact at the pin.

**E1 — SM:222** (covers SM §§4.2–4.8 and SM:134/136). Old: "(under A1 and A4 [Substratum §3.1] it
acts on configurations over a finite periodic quotient of $\Lambda$)". New: "(under A1 and A4
[Substratum §3.1] it acts on configurations over a finite periodic quotient $\Lambda/P$; the staggered
and cubic results below are stated on $\Lambda$ and hold on such a quotient when $P$ admits them: the
staggered phases require every vector of $P$ to be even off one axis, the checkerboard requires even
coordinate sums, the eight Brillouin-zone corners and the staggered blocking require
$P \subset 2\mathbb Z^d$, and the cubic group acts when it maps $P$ to itself)". Coordination: SM.md is
being edited for Q2 at SM:242; E1 touches SM:222, a Phase 2 splice site, and needs a fresh base.

**E2 — SM:539.** Old: "The staggered-to-Dirac reconstruction identifies the two sublattices". New:
"On $\mathbb Z^3$, and on a quotient whose period vectors all lie in $2\mathbb Z^3$, the
staggered-to-Dirac reconstruction identifies the two sublattices". Old: "For the designated
checkerboard cut, the visible" New: "For the designated checkerboard cut on these lattices, the
visible".

**E3 — SM:1506 and SM:1536.** Old (each line): "bipartite checkerboard structure)". New: "bipartite
checkerboard structure on $\Lambda$ and on the quotients that carry it, §4.7)". Structure:1058, which
summarizes the same mapping without asserting the structure's existence, is left unchanged.

**E4 — book ch06:24 and FULL:1535** (covers ch06:22, :30 and FULL 1533, 1541). Old: "One singlet
taste; three triplet tastes related by cubic symmetry." New: "One singlet taste; three triplet tastes
related by cubic symmetry. These are the corners and the cubic action of $\mathbb Z^3$; a finite
periodic quotient of it (Chapter 2, A4) carries all eight corners when its period vectors lie in
$2\mathbb Z^3$, and the cubic group acts on it when it maps the period lattice to itself."

**E5 — SM:446 (optional).** Needed only if E1 is to support Theorem 8b on quotients without cubic
invariance. Old: "The triplet members are related by cubic symmetry ($O$ permutes spatial axes),
hence identical." New: "The same computation gives $\sigma(X_j) = 1$ and $\sigma(M_j) = -1$ for each
$j$, so the triplet members are identical."

**A4 (Sub:98) and its restatements.** No Q1 edit is proposed; A4 is not narrowed here. Q1's finding
for the A1-EXIT ledger: none of the Q1 consumers uses the finiteness of A4's quotient, and every one
holds on `ℤ^3`. Two forms are compatible with these results. (α) A4's lattice is `ℤ^d`, with finite
quotients admitted only as representatives under the conditions of E1. (β) A4 keeps the finite class,
and E1–E4 carry the conditions. Under both, E1, E2 and E4 are needed wherever a finite quotient is
admitted, and E3 in either case. Under the minimal-substratum principle (§A.29), the conditions on
`P` are needed by stated results only if finite quotients are retained; no observation at accessible
scales distinguishes them. Choosing between (α) and (β) is A1-EXIT's and the owner's.

After any Step 2 edit: rebuild SM and the book (`sh ./build.sh SM --book`), and re-run
`q1_census.py` to confirm that E1–E4's text is present and the A4 lines are unchanged.

## 8. Productivity verdict (§A.31) and pressure on the favourable branch

**Pressure.** The favourable reading is "every consumer holds on `ℤ^3`". Four points were tested.
(1) Finite-volume objects in the `ℤ^3` proofs: Theorem 2 uses finite-range operators on all
functions; Theorem 3's kernel theorem has no finiteness; Theorem 13's Schur complement is
site-diagonal; the finite-torus probes are evidence, not the proofs. (2) Theorem 10's degeneracy on
`ℤ^3`, where the corners are not `ℓ²` eigenvectors: read as unitary equivalence of the taste-cell
spectral subspaces under `O`. (3) Theorem 8b on `ℤ^3`: a symbol value at the corner, not an `ℓ²`
eigenvalue. (4) The `ℤ^3` verdicts were checked against `ℤ^3` itself, not inferred from a large torus:
part B computes on `ℤ^3` and uses `2ℤ^3`-covariance for the remaining sites.

**Verdict: gem.** The record yields conditions sharper than, or different from, O-A4 row 18's blanket
condition, with proofs and countermodels: Theorem 2 needs only "even off one axis" and holds on a
non-bipartite quotient; Theorem 3 needs only even sums and already states it; Theorem 8b needs
`P ⊂ 2ℤ^3` without cubic invariance; Theorems 8 and 10 additionally need a cubic action on `X_P`
(`4×4×6` countermodel), which is sufficient but not necessary for Theorem 10's step (ii).

**§A.31 classification.** NEW: the per-consumer conditions of §2–§3, the `4×4×6` countermodel, and
"stabilizer order 48 does not certify a cubic action". POSITIVE: all nine named consumers hold on
`ℤ^3`, and A4's finite clause is used by none of them. ELABORATING: the `L = 4` corner span; Theorem
13's Schur complement is site-local on `ℤ^3`; Lemma 2. CONFIRMING: O-A4 §7's countermodels.

**Assumption-watch markers.** (W4) A quotient's vertex-stabilizer order does not identify its point
group. (W5) "Related by cubic symmetry" on a quotient needs a symmetry of `P`. Cubic invariance is
sufficient for that, and a group transitive on the axes is enough. (W6) Staggered phases,
checkerboard and blocking are three distinct conditions on `P`.

**§A.29.** Nothing is adopted. The conditions on `P` are hypotheses that finite quotients need, not
proposed premises.

## 9. Reproducible computation

From the repository root, at the commit that lands this record (stdlib Python 3, deterministic):

| Command | Expected | Time |
|---|---|---|
| `python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_checks.py` | exit 0; output equal to `checks/q1_checks.out`, last line `ALL CHECKS PASS` | about 10 s |
| `python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_census.py verification/audits/foundations/a1exit-q1-20261120/checks/q1_census.json` | 216 lines; JSON unchanged at the pin's manuscript text | < 1 s |
| `python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_dispositions.py` | exit 0, `COMPLETE`; `q1_dispositions.json` unchanged | < 1 s |

The verdict of each script is its exit status; printed lines are diagnostics (§A.44). The census and
dispositions read the manuscripts and therefore match only while the manuscript text is that of the
pin.

| Part | Checks | Supports |
|---|---|---|
| K | Controls K1, K3, K4, K5 | §1 |
| A | Lemma 1 by brute force on 134 quotients; `4×4×3` and skew witnesses | §2, C2, C3, C539, C1536 |
| B | Theorem 2 on `ℤ^3` and on `4×4×3`; `3×3×4` | C2, K2 |
| C | Automorphisms and corner lines (`L = 4, 6`, `4×4×6`), link orbits, taste-cell spectra, cyclic quotient | C8, C10, §5 |
| D | Blocking iff `P ⊂ 2ℤ^3` | C12, C13, C539 |
| E | Cubic-invariant lattices to index 96 | Lemma 2 |
| F | Corner eigenvalues `σ(η)/3` | C8b |

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7047514209 | Authorization | Provenance; quoted with author |
| #1454 | Accountable Issue (row P2-Q1) | Provenance |
| #1450, #1441 | Routing (A1-PHASE2 §12–§14); O-A4 and its review | Support on `main`: the records used (A1-PHASE2 PREREG, O-A4 RESULT and checks) are on `main` at the pin and are cited as they stand there |
| PR for this record | Guiding draft PR | Provenance |

Kernel modules cited ([L]) are on `main` at the pin: `verification/lean/OI_Staggered_Relations.lean`,
`verification/lean-mathlib/OIBridge/ChiralCenterRecovery.lean`, `TasteBranching.lean`,
`WaveSubstratumUnbounded.lean`. They are read, not built, here.

## 11. Verification status and remediation (§A.46 item 4)

- **Evidence level.** Paper derivations (Lemmas 1–2, §3 arguments), exact computations (§9), and
  reading of cited kernel statements. No new kernel theorem. Lemma 1(c)'s uniqueness argument,
  Lemma 2, the `ℤ^3` instance of `Staggered.Gens`, and the C10, C12, C13 arguments have no kernel or
  independent check yet.
- **Missing.** An independent non-author review of this record. The general classification of cubic
  Bravais lattices beyond index 96 is cited, not checked, and nothing depends on it.
- **K6.** `git diff --stat 9db518844df62151979acf6aac1d487b59c44907` lists only files under
  `verification/audits/foundations/a1exit-q1-20261120/`.
- **Accountable Issue.** #1454 (P2-Q1). **Resolution.** A review recorded on the guiding pull request.
  Step 2 corrections need their own owner authorization. The A1-EXIT ledger may use the
  classifications only after that review, and only at the scope stated here.

## 12. Review checklist

1. K1–K5 hold, and `q1_checks.py` reproduces `q1_checks.out` exactly.
2. Lemma 1(c): the `Gens` fields force the stated characters, and the condition is "even off the last
   axis" (try `4×4×3` and `3×3×4`).
3. Lemma 2's half-turn argument, and that the class in row 4 of §4 is "`P = 0` or finite index".
4. C13: the hidden block is site-diagonal given Theorem 13(ii), so no infinite-volume inverse is needed.
5. C10: `4×4×6` is a genuine countermodel to "related by cubic symmetry" (every automorphism fixes the
   `X_3` line; translations act on corner lines by signs).
6. The disguised-A1 table: each class contains `P = 0`, and no condition bounds the site count.
7. §6: spot-check dispositions, especially the R/I boundary (SM:134/136, SM:1554, Main:218,
   appendix-b:378, Structure:1058).
8. §7: each proposed text is minimal and true on the admitted class; E5 is needed only for 8b's
   weaker condition; no A4 edit is proposed.
9. Voice: no §A.32/§A.33 phrase family in proposed manuscript text.

# G3-LEDGER: thread G3, is DIM-1's parity theorem detecting complex structure?

Off-repo, read-only research ledger. Nothing here is frozen, certified, adopted, or proposed as ROADMAP or
manuscript wording. No premise is adopted.

## 0. Base, scope, layers

- **Base.** `scratchpad/wt-06b` at `06b6f94e479bc19a28979c72316823cbdd0fb62b` (`git rev-parse HEAD`);
  `git status --porcelain` empty at the end of the pass. No worktree or `/home/user/incompleteness` file was touched,
  no git write, nothing dispatched. Every write is under `scratchpad/g3thread/`.
- **Paths** are relative to `verification/lean-mathlib/OIBridge/`. CD = `CompositeDimension.lean`
  (sha256 `9b38ba94…0a67`), NGB = `NativeGateBall.lean`, K2G = `K2Guard.lean`, ST = `SharpTests.lean`.
- **Layers** (never substituted for one another):
  `[K]` kernel identifier at the base (file:line); `[R]` reading of a landed proof (which hypothesis it consumes);
  `[X]` exact computation in DIM-1 coordinates, kernel tables parsed from the Lean source; `[M]` exact computation in
  a matrix model (evidence about QM / real QT, not about the kernel); `[W]` written argument; `[L]` literature from
  memory, not re-verified; `[P]` prior off-repo research cited as data; `[S]` uncompiled Lean sketch.
- **Prior notes consumed:** `ss/SS-LEDGER.md` (G3, G6, P3), `k2c/K2C-LEDGER.md` (dictionary P1, branch rule G4),
  `k2d/K2-LEDGER.md` (D3 real-QT countercontrol, thread B two-NOT table), `threads/B/RESULT.md` (J/K models),
  `threads/E/RESULT.md` (32 gates, Wigner tags), `round2/DIM-1-DESIGN.md` §(a)5.
- **Productivity test (§A.31), fixed before the probes.** A finding is a gem iff it is strictly stronger than the
  restatements "DIM-1's output set {1,3} coincides with the complex spin factors" and "the level-exchange split is
  (2,k)" (SS G3), and either constrains a premise or exposes a hidden assumption.

## 1. What "complex" can mean here (fixed before the directional questions)

| tag | meaning at this level | object |
| --- | --- | --- |
| C-body | the elementary body is affinely the Bloch ball of `M_2(ℂ)`, i.e. `V_d ≅ Herm_2(ℂ)` as Jordan algebras | `eball d`, `d = 3` |
| C-NOT | the NOT is Wigner-unitary: its Bloch action is `Ad U` (an automorphism of `M_2(ℂ)`), not `U(·)ᵀU†` (an antiautomorphism); on the ball, `det N = +1` | `N` at `d = 3` |
| C-field | in the Hurwitz dictionary `V_{1+k} ≅ H_2(𝔽_k)` with the level exchange `A ↦ XAX`, `𝔽 = ℂ` (`k = 2`) | `(eball (1+k), leNot k)` |
| C-J | the gate determines a linear `J` with `J² = −1` on some space built from it | `(N, G)` |
| C-K | the gate's action on the target minus plane is a complex structure `K` (`K² = −1`), i.e. the relative phase `i` | `G` at `d = 3` |

The classical bit (`d = 1`, `ℝ ⊕ ℝ`) is the self-adjoint part of both `ℂ ⊕ ℂ` and `ℝ ⊕ ℝ`: "complex" is vacuous
there, so every C-statement below is meant for `d ≥ 2` unless the classical row is shown explicitly.

## 2. Depth-first nodes

### N1. Where DIM-1's parity step reads its hypotheses `[R]`

`finrank_plus_eq_finrank_minus` (CD:682) = `NGB.parity` (NGB:194) applied to `Pop` (CD:543) and `Lop` (CD:552).
- `Lop_anti` (CD:562) consumes `relC` only, through `opGate_homMap_comp` (CD:503).
- `Lop_eq_zero` (CD:574) / `Lop_injective` (CD:615) consume `relT` only (through `opGate_comp_homMap`, CD:494) and
  injectivity of `G`.
- `toOp_actT` (CD:464) consumes `IsNot (eball d)` (self-adjointness via `homMap_dot`, CD:395).
- **Not consumed:** `frame`, `posFwd`, `posInv`. Parity is a statement about the linear pair `(G, N)` on the LT
  carrier `W d` only. The block bound `blockData_of_nativeGate` (CD:2703) consumes everything
  (`frame`, `posFwd`, `posInv`, and `relT`/`relC` at CD:1941/1948 inside `gate_corner_neg`).

The mechanism, made explicit by P2-S: `relT` makes `G` preserve the target-parity sectors; `relC` makes `G` commute
with the control NOT on the target-even sector and **anticommute** on the target-odd sector. So on the target-odd
sector `G` maps (control +) ⊗ V₋ ↔ (control −) ⊗ V₋, of dimensions `p·m` and `m·m`; injectivity forces `p = m`.

### N2. Q-FWD at the composite: the complex qubit pair `[K]` + `[X]`

- Kernel: `nativeGate_cnot` (CD:1160) with `nflip = diag(1,−1,−1)` (CD:797; the docstring calls it "the reflection";
  it is the π-rotation about x, `det +1`), hence `finrank_plus_eq_finrank_minus` gives balance. P2-K reproduces
  frame/relT/relC from the parsed tables; K2C P1.5b/P1.8 `[P]` identify `cnot = Ad CNOT`, `actT nflip = Ad(I⊗X)`.
- P2-S: `cnot` swaps the 4-dim control-even and 4-dim control-odd parts of the 8-dim target-odd sector bijectively.
- P2-F: for the rational π-rotation `N' = g nflip gᵀ` about `(3/5, 4/5, 0)`, the conjugate gate satisfies
  frame/relT/relC exactly; a 30³ rational sample of pure products against effect rays is ≥ 0 (min 0) for `cnot` and
  for the conjugate. Positivity of the conjugate in general is covariance `[W]` (local rotations preserve the ball
  and its effects).
- **Every unitary z-flipping NOT of the qubit admits a native gate** (`[K]` at `nflip`, `[X]` at `N'`, `[W]` for
  the circle of π-rotations about equatorial axes).

### N3. Which property of ℂ the balance uses `[X]` + `[M]`

1. **Single system (P1-B, P1-C).** In `H_2(𝔽)` the level exchange `θ(A) = XAX` has commutant `span{I, X}`
   (dimension 2 for every 𝔽) and anticommutant `ℝZ ⊕ {offdiag(q) : q ∈ Im 𝔽}` (dimension `k`). On the equatorial
   (off-diagonal) space `θ` is the conjugation `q ↦ q̄`, with split `(dim Re 𝔽, dim Im 𝔽) = (1, k − 1)`. The map
   `Φ_u(A) = Z∘A + u·[A, Z]/2` (u an imaginary unit) sends the commutant into the Hermitian anticommutant with rank 2
   for every u; it is onto exactly when `k = 2`. Over ℝ, `[X, Z]/2` is antisymmetric and there is no u.
   **Balance ⇔ `dim Im 𝔽 = dim Re 𝔽 = 1` ⇔ 𝔽 = ℂ** (classical bit aside). The ingredient is that an
   anti-Hermitian commutator times the unique imaginary unit is Hermitian (the dynamical-correspondence identity),
   together with uniqueness of that unit.
2. **Composite (P3-M2, M3).** Over any field, `CNOT (A⊗B) CNOT = (Z∘A)⊗B + ¼[A,Z]⊗[X,B]` for target-odd `B`. The
   control-odd partner of a control-even `A` is the anti-Hermitian `[A, Z]/2`. Over ℂ the two anti-Hermitian
   factors carry one `i` each and `i⊗i = −1⊗1` puts the product in `Herm⊗Herm` (LT carrier, split (4,4)):
   `CNOT(X⊗Z)CNOT = −Y⊗Y`. Over ℝ it lands on `R⊗R = −Y⊗Y` (`R` antisymmetric), outside the 9-dim LT span
   (P3-M4): the rebit pair is balanced (2,2) only on its 10-dim carrier and (2,1) on the LT sub-carrier.
   This sharpens k2d D3 `[P]`: **the parity failure of the rebit pair on `W 2` is exactly its LT deficit `R⊗R`.**
3. **Wigner (P1-D).** Over ℂ the four z-flipping NOTs `Ad X`, `Ad Y` (automorphisms, `det +1`, split (2,2)) and
   `A ↦ XAᵀX`, `A ↦ YAᵀY` (antiautomorphisms, `det −1`, splits (3,1), (1,3)) are all Jordan automorphisms of the
   ball. **Over ℂ, balanced ⇔ unitary ⇔ `det_Bloch = +1`.** So "complex ⇒ balance" holds for unitary NOTs and fails
   for antiunitary ones.

### N4. Q-REV: does balance (plus the structural hypotheses) force complex?

| formulation | verdict | witness |
| --- | --- | --- |
| R-a: `IsNot` + balance ⇒ C-body | **false** | `eball 5`, tangent split (2,3) (balanced, `det −1`); `eball 7`, (3,4) (balanced, `det +1`) (P1-E) |
| R-b: `IsNot` + `frame` + `relT` + `relC` + invertible `G` ⇒ C-body | **false** | explicit `G_J` at `d = 5, 7, 9` meets all four (P2-A) |
| R-b′: algebraic half of `NativeGate` ⇔ balance (for the given `N`) | **true, both directions** | (→) `[K]` landed proof reads only relT/relC/injectivity (N1, `[R]`); (←) explicit `G_J`, exact for every diagonal split at `d ∈ {1,2,3,5,7,9}` (term-rank census 27/27, P2-A) and at `d = 3` by full linear solve including the non-diagonal `N'` (P2-L); general `N` by orthogonal diagonalization `[W]` |
| R-c: `IsNot` + `NativeGate` ⇒ `d ∈ {1,3}` ⇒ (`d ≥ 2`) C-body | **true** | `[K]` `dim_of_nativeGate` (CD:2723), `three_of_nativeGateOf_of_two_le` (K2G:253) + `[M]` Pauli dictionary (K2C P1) / `[L]` spin-factor classification |
| R-d: `IsNot` + `NativeGate` at `d = 3` ⇒ C-NOT | **true** | `[K]`-cheap: `finrank_plus_add_finrank_minus` (CD:274) + CD:682 + `omega` give split (2,2), `tangentPlus N = 1`, i.e. a π-rotation, `det +1` (sketch item 1); the antiunitary NOTs have no gate, not even an algebraic one (P2-L generic ranks 14, 10 < 16) |
| R-e: with the level exchange of `H_2(𝔽)`: `NativeGate` ⇒ C-field | **true, by parity alone** | the block bound is automatic for `leNot` (`p_tan = 1`); balance (2,k) forces `k = 2` (`[X]` P1-B, P2-A; sketch item 5 `two_of_nativeGate_leNot`) |
| R-f: balance + `det N = +1` ⇒ C-field | **true on the Hurwitz family, false on spin factors** | PAR+ = {d ≡ 3 mod 4} (P1-E); Hurwitz ∩ PAR+ = {3}; `d = 7` is a non-Hurwitz survivor |
| R-g: the gate's `J := actC N ∘ G` (J² = actT N ∘ G², CD relC at `G ω`) ⇒ C-J ⇒ ℂ | **false as a ℂ-fingerprint** | `J² = −1` on the target-odd sector for `cnot` (dim 8) **and for the classical `cnot1`** (dim 2) (P2-J); for real QT on its 10-dim carrier (P3-M4); in the two-NOT J/K models at `d = 5, 7` `[P]` |
| R-h: positivity forces C-K at `d = 3` | **conjecture** | `cnot`'s target twist `K = [[0,−1],[1,0]]` on span(y,z), `K² = −1` (P2-P); the twist-free algebraic `G_J` at `d = 3` fails `posFwd` (−2/5, P2-P); thread E's classification of the 32 admissible gates as `(D⊗D)·CNOT·(D⊗D)` `[P]` (conditional on its P0 parametrization) supports it; no proof |

**Skeptical reading of the favourable rows (R-c, R-d, R-e, R-f).** On the ball family, `d` alone fixes the Jordan
algebra, so *any* dimension selector is formally a "field selector" on the Hurwitz subfamily: R-c is the output-set
coincidence turned into an implication through a dictionary, not evidence that DIM-1's mechanism uses ℂ. R-b/R-b′
show the gate algebra is field-blind (a Clifford `Cl(1,1)` pair that exists at `d = 5, 7, 9`). R-e and R-f select ℂ
only after the NOT has been restricted to a class (level exchange, or `det +1`) that the kernel does not impose by
itself; the kernel reaches that restriction only through positivity (block bound).

### N5. Separating the two DIM-1 steps (P1-E, P2-A, P2-P)

| step | consumes | on its own selects | Hurwitz reading |
| --- | --- | --- | --- |
| parity balance | `relT`, `relC`, injective `G`, `IsNot` | `d` odd (with some `N`); `d ≡ 3 mod 4` with `det N = +1`; with the level exchange, `𝔽 ∈ {cl, ℂ}` | `dim Re 𝔽 = dim Im 𝔽` on the equator |
| block bound `p_tan ≤ 1` | all of `NativeGate` (positivity decisive) | **no dimension** (BLK = every `d`); it selects the NOT type: fixed tangent space ≤ 1-dim (`−I`, or level-exchange type with exactly two fixed pure states) | `dim Re 𝔽 ≤ 1`, true for every 𝔽: it excludes the non-level-exchange NOTs |
| both, same `N` | — | `d ∈ {1, 3}` | — |

### N6. Controls: the composites over ℝ, ℂ, ℍ, 𝕆 and the failure locus

| 𝔽 | `d` | LE split homog / tangent, `det` | balanced NOT on `eball d`? | algebraic gate on `W d` (frame, relT, relC, invertible) | positivity | native gate `[K]` | the field's own CNOT-type gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| classical | 1 | (1,1) / (0,1), −1 | yes (the LE itself) | yes (`G_J = cnot1`, P2-P) | yes `[K]` | yes `nativeGate_cnot1` (CD:2861) | classical CNOT; `J² = −1` there too |
| ℝ | 2 | (2,1) / (1,1), −1 | **none** (`d` even) | **none**, every `N` (term rank 7/9, 8/9) | — | no `[K]` CD:693 | real CNOT exists on the 10-dim carrier; relT/relC hold; balanced (2,2) there via `R⊗R`; leaves the LT span (P3-M4; k2d D3 `[P]`) |
| ℂ | 3 | (2,2) / (1,2), +1 | yes: exactly the π-rotations (unitary) | yes | yes for `cnot` `[K]`; **no** for the twist-free `G_J` (−2/5) | yes `[K]` CD:1160 | `cnot = Ad CNOT` |
| ℍ | 5 | (2,4) / (1,4), +1 | yes, (2,3), `det −1` (outside SO(5) = the quaternionic-unitary image `[L]`) | LE: **no** (28/36); balanced (2,3): **yes** | (2,3) `G_J`: **fails** (−2/5) | no `[K]` CD:2736 | no LT composite `[L]` (Hardy counting 28 ≠ 36 if the composite is taken as `H_4(ℍ)`, P3-M5) |
| 𝕆 | 9 | (2,8) / (1,8), +1 | yes, (4,5), `det −1` | LE: **no** (52/100); balanced (4,5): **yes** | (4,5) `G_J`: **fails** (−2/5) | no `[K]` via CD:2723 | none `[L]` |

**Answers.**
- SS's splits (2, k) are **confirmed** exactly (P1-B, and SS P3 replayed byte-identically).
- SS's "fails over ℝ, ℍ, 𝕆 at parity" is **correct for the level-exchange NOT only**. Corrected locus:
  ℝ fails at parity for every NOT; ℍ and 𝕆 fail at parity for every `det +1` NOT (including the level exchange) and at
  the block bound (positivity) for their balanced `det −1` NOTs. No NOT on `eball 5` or `eball 9` passes both.
- "Existence of a native gate at all" is never an independent locus: its algebraic half is equivalent to parity
  (R-b′), and its positive half adds exactly the block bound.

## 3. Directional table (§A.34: each direction its own witness)

| direction | statement | layer | witness |
| --- | --- | --- | --- |
| Q-FWD (→) | complex + unitary NOT ⇒ a native gate exists ⇒ parity balance | `[K]` at `nflip`; `[X]` at the rational `N'`; `[W]` for every π-rotation | `nativeGate_cnot` (CD:1160) → CD:682; P2-F |
| Q-FWD, scope | complex + antiunitary NOT ⇏ balance | `[X]` | P1-D splits (3,1), (1,3); P2-L generic ranks 14, 10 |
| Q-FWD, property used | Hermitian commutant ≅ anticommutant of the NOT via `Φ_i`; on the LT composite, `i⊗i = −1⊗1` | `[X]` single system, `[M]` composite | P1-C, P3-M2/M3 |
| Q-REV (←), strongest true | `IsNot` + `NativeGate` + `2 ≤ d` ⇒ `d = 3` and `N` is a π-rotation (Wigner-unitary) and `eball d ≅` Bloch ball of `M_2(ℂ)` | `[K]` for `d = 3`; `[S]`, kernel-cheap, for the π-rotation; `[M]`/`[L]` for the dictionary | CD:2723, K2G:253; sketch item 1; K2C P1 `[P]` |
| Q-REV, refuted | balance (even with frame + relT + relC + invertible `G`) ⇒ complex | `[X]` | `G_J` at `d = 5, 7, 9` (P2-A) |
| Q-REV, refuted | gate-induced `J² = −1` ⇒ complex | `[X]` + `[M]` | `cnot1` (P2-J); real QT (P3-M4) |
| Q-REV, conjecture | `NativeGate` at `d = 3` ⇒ target twist `K` with `K² = −1` | `[X]` instance + `[P]` | P2-P; thread E |

The forward and reverse rows are separate theorems. In particular the uniqueness/characterization in row Q-REV
(the gate pins `d = 3` and the NOT class) is not a converse of Q-FWD, and Q-FWD does not hold for the antiunitary NOTs
that the ball admits.

## 4. Strongest supported statement per direction

- **Q-FWD (exact + kernel).** For the qubit pair with the Wigner-unitary NOTs (the π-rotations about equatorial
  axes) a native gate exists (`[K]` at `nflip`, `[X]` at a rational instance, `[W]` in general), and so the parity
  balance holds. The balance is the identity `dim_ℝ Herm-commutant(X) = dim_ℝ Herm-anticommutant(X) = 2`, realized by
  `A ↦ Z∘A + i[A,Z]/2`. In the composite it is realized by the LT identity `i⊗i = −1⊗1`. It fails for both
  antiunitary z-flipping NOTs `[X]`.
- **Q-REV (kernel + sketch).** `IsNot ∧ NativeGate ∧ 2 ≤ d ⇒ d = 3 ∧ tangentPlus N = 1` (`[K]` + kernel-cheap `[S]`).
  Through the `[M]` Pauli dictionary this is C-body ∧ C-NOT. **Parity alone forces neither**: the algebraic half of the
  gate is equivalent to balance and exists at `d = 5, 7, 9` (`[X]`). With a level-exchange NOT, parity alone forces
  `𝔽 = ℂ` among Hurwitz algebras (`[X]`, sketch item 5). With `det N = +1`, parity forces `d ≡ 3 (mod 4)`, which is
  ℂ among the Hurwitz algebras and also admits `d = 7, 11, …` (`[X]`).

## 5. Gem classification (§A.31; maximum skepticism toward favourable readings)

| # | finding | class | why |
| --- | --- | --- | --- |
| G3-1 | **The algebraic half of `NativeGate` (frame, relT, relC, invertible) is equivalent to parity balance for the given `N`.** (→) is the landed proof, read; (←) is explicit `G_J`, exact in 27/27 diagonal cases and at the non-diagonal `N'`. Positivity's only contribution to DIM-1's count is the block bound. Consequence: no field information beyond the split count can be extracted from the gate relations. | **NEW** | stronger than the restatements (an equivalence with an explicit converse); it constrains: any reading of ℂ from relT/relC alone is bounded by `p = m`, and `G_J` at `d = 5, 7, 9` is the exact countermodel |
| G3-2 | **The gate's Clifford pair is not a complex-structure fingerprint.** `J = actC N ∘ G` has `J² = actT N ∘ G²` (it is `relC` at `G ω`, kernel-trivial), hence `J² = −1` on the target-odd sector for every involutive gate: `cnot`, the classical `cnot1`, real QT on its own carrier, and the two-NOT J/K models. Assumption-watch **AW-G3-1**: any future claim that "the native gate supplies `i`" must exhibit something the classical `cnot1` lacks. The candidate is the target twist `K` (R-h), which the twist-free `G_J` lacks and which fails positivity. | **NEW** (assumption-watch; a negative that blocks a tempting favourable reading) | exposes a hidden assumption; the countercontrol is a landed kernel object |
| G3-3 | **At `d = 3`, DIM-1 derives the Wigner class of the NOT.** A native gate forces split (2,2), i.e. a π-rotation (`det +1`, an automorphism of `M_2(ℂ)`); both antiunitary z-flipping NOTs (transpose-type reflection, universal NOT) admit no gate, not even an algebraic one. DIM-1-DESIGN §(a)5 lists `det N = +1` as "a further premise not used"; it is in fact derived at `d = 3`. | ELABORATING (borderline NEW) | it is arithmetic on the landed parity theorem (`det N = (−1)^{(d+1)/2}` for balanced `N`, cf. SS G6), but the Wigner identification and the exact aut/antiaut table are new; kernel-cheap |
| G3-4 | **Step separation on the Hurwitz family.** Block bound ⇔ the NOT is of level-exchange type (`dim Re ≤ 1`; it selects no dimension). Parity ⇔ `dim Re 𝔽 = dim Im 𝔽` on the equator. SS's "fails over ℝ, ℍ, 𝕆 at parity" is corrected to a NOT-dependent locus: ℍ, 𝕆 fail at the block bound for their balanced (`det −1`) NOTs. | ELABORATING (sharpens and corrects SS G3) | upgrades the output-set coincidence to a step-wise map **relative to the Hurwitz dictionary** `[L]`; no map from the kernel's hypotheses to a field object exists |
| G3-5 | **The rebit parity failure on `W 2` is exactly its LT deficit.** Over any field the target-odd action of CNOT is `(Z∘A)⊗B + ¼[A,Z]⊗[X,B]`. Over ℝ the anti⊗anti term is `R⊗R ∉` LT span, and real QT is balanced on its 10-dim carrier. At `d = 2`, DIM-1's field selection and its LT premise are therefore the same fact. | CONFIRMING (k2d D3) + ELABORATING (mechanism formula) | `[M]`, matrix model only |
| G3-6 | Parity alone, over all NOTs, selects odd `d` and is not field-selecting (`d = 5` ℍ, `d = 9` 𝕆, `d = 7` non-Hurwitz). With `det +1` it selects `d ≡ 3 (mod 4)`. | CONFIRMING (SS G6 arithmetic) with exhibited algebraic gates | — |
| G3-7 | R-h, "positivity forces a complex target twist at `d = 3`" | BORDERLINE (conjecture; one exact instance plus a twist-free countercontrol; thread E `[P]`) | no proof; a kernel version needs a gate classification |

**Is it a coincidence of output sets, or a formal map?** Both, at different strengths:
- *Formal map, trivial strength.* On balls, `d` determines the Jordan algebra, so `d ∈ {1,3}` ⇔ "complex spin factor"
  is a theorem (`[L]` + `[M]` dictionary) for **every** `d`-selector. This is not evidence about mechanism.
- *Formal map, step-wise, relative to the Hurwitz dictionary.* Parity counts `dim Im 𝔽` against `dim Re 𝔽` for
  level-exchange NOTs, and the block bound is what forces a NOT into the level-exchange class. This is real structure
  (G3-4), but the dictionary `V_{1+k} ≅ H_2(𝔽_k)` is not a kernel object, and the non-Hurwitz balls `d = 7, 11, …`
  show that the same steps do not intrinsically see a division algebra.
- *Not a formal map at gate level.* The gate algebra is field-blind (G3-1), and the gate's complex structure is
  classical-compatible (G3-2).

**Fixed point.** This was one depth-first pass, with two NEW findings (G3-1, G3-2). The fixed point is not reached.
The next pass would start at R-h: test whether `posFwd`/`posInv` at `d = 3` force `K² = −1` on the target minus plane
for every gate meeting frame/relT/relC. Method: parametrize the 64-dim algebraic solution space for `nflip` (P2-L
gives its dimension), impose positivity on the corner/tangent slices as NB-1's S1–S2 do, and compare with thread E's
32 gates.

**Correctness/consistency (§A.23).** Consistency-axis work only. The bands are unchanged.

## 6. Probe log

All in `scratchpad/g3thread/`, run from that directory. Exact arithmetic only (Fraction, sympy). No float is
evidence. Each probe was run once into `*.out` and once into `*.replay.out`; `cmp` reported all three pairs
byte-identical.

| probe | command | script sha256 | output sha256 | result |
| --- | --- | --- | --- | --- |
| P1 Hurwitz / Wigner / census | `python3 -I g3_p1_hurwitz.py` | `52a7a370f2d631d767319a9d1447471868438ad64d0619ceb4ef7c77385d62e9` | `edea400739595b1dd8e71682d4e0ee63a3b34f564c48a5b5667ba8aa50980a67` | 31 checks, 0 failed; VERDICT RENDERED |
| P2 gate algebra (kernel coordinates) | `python3 -I g3_p2_gate_algebra.py ../wt-06b/verification/lean-mathlib/OIBridge/CompositeDimension.lean` | `cbc020b855fe1efa04900748b0dce25f9ed01a1c10f4fa0b23df3d67384593b3` | `721b5d87c4c93a74b4c1a98189032440a9ab08ddecfe0f420d2f2c8c4ad11fb7` | 26 checks, 0 failed; VERDICT RENDERED (~18 s) |
| P3 mechanism (matrix models) | `python3 -I g3_p3_mechanism.py` | `cb1a954d8566994452e6f05a134818364cf487d9f8a70093b0f17a17d525eed7` | `12d757ffb9cff1459cbac05ee57ac8b5eb5a35393079aeeca8ff1f629b1f7532` | 11 checks, 0 failed; VERDICT RENDERED |
| SS P3 replay | `python3 -I p3_field_splits.py` (from `../ss`) | `e41c752a…f254` (unchanged) | `replay_ss_p3_field_splits.out`, identical to `ss/p3_field_splits.out` | 7 checks, 0 failed |
| Lean sketch | — | `G3.sketch.lean` | — | uncompiled (no toolchain) |

**Run history.**
- **P2.** Before its first execution, the dense nullspace and the sample minimizer were replaced by a sparse
  elimination and a factored loop, for speed only. No decision rule changed and no check was added or removed. The
  recorded run is the first execution.
- **P3, run 0, FAILED one check, verdict not rendered.** The decision rule predicted by hand
  `CNOT(X⊗Z)CNOT = −(R⊗R)`. The exact value is `+(R⊗R)` (`= −Y⊗Y`, consistent with M3's `−Y⊗Y`, since `Y = iR`). The
  failing line was `FAIL M4 Sym(4) = LT span (rank 9) + R(x)R (total 10); CNOT (X(x)Z) CNOT = -(R(x)R), outside the LT
  span`. Only the sign was wrong: the outside-LT clause held, as confirmed by a separate diagnostic (`o == kp(R,R)`
  true). The expected sign was corrected in both the docstring and the check (the check now also asserts `= −Y⊗Y`),
  and the run-0 script is kept verbatim as `run0_g3_p3_mechanism.py.txt` (sha256 `d882a101…39a3`). The recorded run is
  run 1.
- The P2 positivity witness (−2/5) was derived by hand before the run, and P2 confirmed it at `d = 3, 5, 7, 9`.

**Written or literature steps not covered by the exact checks.**
- The orthogonal diagonalization of a ball NOT with `z` as a basis vector, and covariance of the relations and of
  positivity under `actC g ∘ actT g`.
- `Aut(V_d) = O(d)`; the quaternionic-unitary image is `SO(5)` and the octonionic image is `SO(9)` `[L]`.
- `V_{1+k} ≅ H_2(𝔽_k)` as the identification of balls with Hurwitz two-level systems. The probe checks the spin-factor
  relations exactly; "these are all the two-level systems" is `[L]`.
- Kadison/Wigner: Jordan automorphisms of `Herm_2(ℂ)` are `Ad U` or `U(·)ᵀU†` `[L]`.
- No LT composite exists for ℍ or 𝕆 `[L]`; the Hardy counting row is arithmetic on a flagged choice.
- That the generic-element rank in P2-L equals the maximal rank: the upper bound is certified by the sector rule on
  every basis element, and the lower bound by the element itself.

## 7. What is not claimed

- No kernel theorem is claimed. The sketch is uncompiled, and its `sorry`s mark the unchecked steps.
- No formal map from DIM-1's hypotheses to a field object (𝔽, a C\*-structure, a dynamical correspondence) is
  claimed. The Hurwitz reading is relative to an `[L]` dictionary.
- R-h is a conjecture.
- No ROADMAP or manuscript wording is proposed. No premise is adopted.

## 8. Replay against e26493394f388a891c2dd03be2696286a89293f7 (after KTRANS-DENSE-1)

- Worktree `scratchpad/wt-e26` at `e26493394f388a891c2dd03be2696286a89293f7`, `git status --porcelain` empty; read-only.
- `delta(06b6f94e, e2649339)` adds `DenseOrbit.lean`, one import line, one census family, the round-ktrans-dense-1
  records and its receipt; it edits no existing module. CompositeDimension, NativeGateBall, K2Guard, SharpTests,
  EffectSpace and K1Bridge are blob-identical at both bases, so every `file:line` citation above stands; all 23 were
  re-read at the new base and land on the named identifier.
- Correction to §0: CompositeDimension's sha256 is `9b38ba944114b4c1…a70a62e6b7d`; the `…0a67` tail written in §0 was a
  transcription slip (the blob is unchanged).
- Probes re-run from `g3thread/` (P2 against `wt-e26`'s CompositeDimension), outputs in `scratchpad/g3replay/`; script
  sha256s equal §6; every output byte-identical to its recorded `.out`: P1 31/0, P2 26/0 (~23 s), P3 11/0, SS P3 7/0.
- Verdict: every result, control and classification in §§2–5 survives unchanged.

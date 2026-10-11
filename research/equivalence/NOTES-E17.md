# NOTES-E17 — the transport form of H-DYN as a design-module statement, with the finite-stage case proved

Base L = `9f9f8257`. Node E17 of round 4 (owner's priority 4). Source: R-E14.2 (NOTES-E14 §2, reading (R-01)): a star
automorphism `α` of a `QuasilocalSystem` (QuasilocalCharacterization.lean:168) that maps every stage matrix unit to a
stage matrix with entries in `{0, 1}`, and that is `LocalityPreserving` (:475) with its inverse, is the Target A
automorphism of a `ReversibleDynamics` (QuasilocalAlgebra.lean:956), i.e. an `OISystem` (:463) up to the canonical
isomorphism — a written proof (CONJECTURE [W]) resting on three standard facts not checked there (the diagonal
subalgebra is maximal abelian; Gelfand duality for `C(Q^ι)`; the identification with the kernel's `transported`,
QuasilocalAlgebra.lean:1109). The node asks for the statement as a design-module object and for its finite-stage case
proved in a design run.

## S0 (written 2026-10-11T04:04Z, before the probe's first run and before any module is written)

**What E17 is (§A.31).** Closure-mode formalization at the design level. The node counts if (a) the transport form is a
Lean predicate on the kernel's `QuasilocalSystem`, with the passage stated as a Lean proposition (not proved), (b) the
finite-stage case is a Lean theorem built in a design run with the standard axioms, (c) a positive control shows that
the predicate holds for every Target A system (`OISystem`) in the kernel's own terms, and (d) exact instances agree
with every lemma before the dispatch. A Lean failure of the finite-stage argument, or an instance that refutes a lemma,
is recorded as such.

**The objects (fixed now).**
- `IsZeroOne M`: every entry of `M` is `0` or `1`. The matrix unit `unitM c c'` (entry `1` at `(c, c')`, else `0`),
  defined in the module rather than through Mathlib's matrix-unit name.
- `TransportHDyn S α`: for every finite region `Λ` and configurations `c, c'` of `Λ`, some region `Λ'` and some
  `{0,1}`-matrix `M` on `Conf Λ'` have `α (S.st Λ (unitM c c')) = S.st Λ' M`.
- `Passage`: every `S`, `α` with `TransportHDyn S α`, `LocalityPreserving S α` and `LocalityPreserving S α.symm` admits a
  `ReversibleDynamics Φ` with `α (S.st Λ X) = S.st (hat Φ Λ) (transported Φ Λ X)` for every `Λ`, `X` — R-E14.2's
  conclusion in the kernel's Target A form. Stated, not proved; its status stays CONJECTURE [W].
- The positive control `oiSystem_transportHDyn`: every `OISystem` satisfies `TransportHDyn` with `Λ' = hat Φ Λ` and
  `M = transported Φ Λ (unitM c c')`, whose entries are `0` or `1` (the defining sum has at most one non-zero term).
- **The finite-stage case**, at the matrix level of one stage (a finite configuration set `C`): (a) a self-adjoint
  idempotent `{0,1}`-matrix is diagonal; (b) the diagonal of `Vᴴ V` counts the ones in each column, so a `{0,1}`-matrix
  whose `Vᴴ V` is idempotent has at most one `1` in each column; (c) a star-algebra automorphism `α` of
  `Matrix C C ℂ` that maps every matrix unit to a `{0,1}`-matrix is the transport along a permutation `g` of `C`:
  `α (unitM c c') = unitM (g c) (g c')` for all `c, c'`, hence `α X = X.submatrix g.symm g.symm`. Proof of (c) by (a)
  and a count: the images of the diagonal units are diagonal `{0,1}` projections, pairwise orthogonal, non-zero and
  summing to `1`, so their supports partition `C` into `|C|` non-empty sets, each a singleton; the off-diagonal units
  follow from `E_cc' = E_cc E_cc' E_c'c'` and a non-vanishing entry. The infinite-volume steps of R-E14.2 (Gelfand
  duality, maximal abelianness, finite range from locality) are not formalized.

**Hypotheses of the finite-stage theorem, classified (rule 1).** None is an OI premise: (c) is a statement about star
automorphisms of a matrix algebra, with the transport form as its hypothesis. The transport form itself restates (O3)
on the stages (R-E14.2's skepticism note): in the passage it is **introduced, not an OI premise**; it is H-DYN's form
(NOTES-E9, R-E14.2), an obligation of the Level III converse. The stage-6 inventory carries no item for it: a search of
`pt/I3/INVENTORY.md` (archive `4dc0321c`, sha256 `51eff9af…`) for H-DYN, Level III, `OISystem`, `LocalityPreserving`
and `ReversibleDynamics` returns nothing. Form of the finite-stage result: {transport form at one stage} ⇒ a
configuration permutation — exact, with no OI content.

**The probe `experiments/e17_transport_finite.py` (decision rule in its header).** Exact (integer and Gaussian-rational
arithmetic). Predictions (sign, strength, reason):
- Z1 PASS, certain: over all `{0,1}` matrices of size `n = 1 … 4` (65536 at `n = 4`), the symmetric idempotent ones are
  exactly the `2^n` diagonal ones (lemma (a): `P_ii = (P²)_ii = Σ_k P_ik` forces the off-diagonal entries of row `i` to
  vanish).
- Z2 PASS, certain: the `{0,1}` matrices with `VᵀV` idempotent are exactly the partial permutation matrices, counted
  `2, 7, 34, 209` for `n = 1 … 4` (`Σ_k C(n,k)² k!`) — lemma (b) and its row companion (a diagonal `VᵀV` forbids two
  columns sharing a row).
- Z3 PASS, very high: among the monomial unitaries `D P` (`D` diagonal with entries in `{1, i, −1, −i}`, `P` a
  permutation matrix), `Ad(D P)` maps every matrix unit to a `{0,1}`-matrix exactly when `D` is scalar — 8 of 32 at
  `n = 2`, 24 of 384 at `n = 3` — and then `Ad(D P) (E_cc') = E_{g c, g c'}` with `g` the permutation (lemma (c) on
  instances).
- Z4 PASS, certain: non-monomial unitaries fail at a diagonal unit: the Hadamard matrix (`½` entries) and the rational
  rotation `[[3/5, −4/5], [4/5, 3/5]]` (`9/25`, `12/25` entries); a monomial `U` is necessary, since `Ad(U)(E_cc)` is the
  rank-one projection on `U`'s column `c`.
- Z5 PASS, certain: positive control at the stage level — for the CNOT update `x ↦ (x₀, x₀ + x₁, x₂)` on three sites,
  the transport of every matrix unit of every stage is a `{0,1}`-matrix of the top stage (the miniature of
  `oiSystem_transportHDyn`).
- Countercontrols, each failing as stated, certain: XZ1 "every idempotent `{0,1}`-matrix is diagonal" (`[[1, 1], [0, 0]]`;
  self-adjointness is load-bearing in (a)); XZ2 "`Ad(diag(1, i))` maps every matrix unit to a `{0,1}`-matrix" (the
  phase automorphism, `E_01 ↦ −i E_01`); XZ3 "a `{0,1}`-matrix whose column sums are at most one has `VᵀV` idempotent"
  (`[[1, 1], [0, 0]]`).

**Prediction for the node.** The probe renders its verdict; the module states `TransportHDyn` and `Passage`, proves
`oiSystem_transportHDyn` and (a)–(c); the build risk is in (c) (the counting argument and the star-automorphism
algebra written without a local Lean), moderate. Label after a green design run: CONJECTURE [D] for (a)–(c) and the
positive control; R-E14.2's passage itself unchanged (CONJECTURE [W]).

## 1. The probe (measured)

`experiments/e17_transport_finite.py` run 1 (started 04:06:08Z, after commit `6ae7fd4f`; decision rule unchanged):
5/5, `COUNTER XZ1/XZ2/XZ3 fails as stated`, `VERDICT E17-TRANSPORT-FINITE-CONSISTENT`; replay byte-identical (py
`f1f8016f…`, out `cefedd2e…`). Measured: the symmetric idempotent `{0,1}` matrices of size `1 … 4` are exactly the
`2, 4, 8, 16` diagonal ones; the `{0,1}` matrices with `VᵀV` idempotent are exactly the partial permutation matrices,
`2, 7, 34, 209`, and the diagonal of `VᵀV` is the column count; `Ad(D P)` maps every matrix unit to a `{0,1}` matrix
for exactly 8 of 32 (`n = 2`) and 24 of 384 (`n = 3`) monomial unitaries, all with scalar `D` and each the transport along
`p`; the Hadamard and the `(3/5, 4/5)` rotation fail at `E_00` (`½` and `9/25`, `12/25` entries); the CNOT transport of
all 124 stage units of three sites is `{0,1}`, and the image of `E^{0}_{0,1}` is no stage unit. Every S0 prediction held.

## 2. The design module (reading rule and prediction, written 2026-10-11T04:33Z, before dispatch 1)

`lean/EqvTransport.lean` (blob `0c7f92f8`, sha256 `1aa3710f…`, 442 lines, 9 prints), namespace
`OIBridge.EqvTransport`, importing `OIBridge.QuasilocalCharacterization`: §A `unitM`, `IsZeroOne` and the unit algebra
(`unitM_mul`, `unitM_conjTranspose`, `sandwich_apply`, `matrix_eq_sum_unitM`, `sum_unitM_zeroOne`); §B (a)
`offDiag_eq_zero_of_zeroOne`, (b) `col_unique_of_zeroOne`; §C (c) `finiteStage_transport`, `finiteStage_transport_apply`;
§D `TransportHDyn`, `isZeroOne_transported`, the positive control `oiSystem_transportHDyn`, and `Passage` (a definition:
R-E14.2's conclusion in Target A form, not proved). The proof of (c) uses (a) and an injectivity count: one chosen
support point per diagonal unit is an injective, hence surjective, map of the finite configuration set, and every
support point is the chosen one — no cardinality sum is needed (simpler than S0's count).

**Reading rule (fixed now).** As NOTES-E15 §5, for `EqvTransport`'s nine prints: BUILT / PARTIAL / NOT BUILT. BUILT
moves (a)–(c) and the positive control to CONJECTURE [D]; `Passage` stays a stated proposition (R-E14.2 CONJECTURE [W]).

**Prediction.** BUILT, strength moderate (about 0.5): the risk is in (b) (`Complex.normSq` and the inequality chain), in
(c)'s rewriting chain through `map_mul`/`map_star` of a star-algebra equivalence, and in the defeq step of
`isZeroOne_transported` (the kernel's `transported` unfolded against the generic sum lemma); §A's unit algebra is low
risk.

## 3. Dispatch 1 measured (run 38112020014) and the repair

Mathlib bridge job 114389373318: Build `failure` at `EqvTransport` (`✖ Building OIBridge.EqvTransport`). Errors: the
conjugate-transpose notation `ᴴ` is scoped to `Matrix` and the module did not open it — parse errors at lines 50, 153,
195 and 260 (the statements of `unitM_conjTranspose`, (a), (b) and the `hsa` step of (c)); one elaboration error at
137:44 (`h.1 ▸ hf` with `h` of unknown type inside `if_neg`). Consequences at the prints: `unitM_mul`,
`sandwich_apply`, `matrix_eq_sum_unitM`, `finiteStage_transport_apply` standard; `offDiag_eq_zero_of_zeroOne` unknown;
`col_unique_of_zeroOne` with no axioms (its statement truncated by the parse error); `finiteStage_transport`,
`isZeroOne_transported`, `oiSystem_transportHDyn` with `sorryAx`. **Reading: PARTIAL.** `TransportHDyn` and `Passage`
elaborated. The dispatched text is kept as `lean/EqvTransport.run38112020014.lean` (blob `f48afc3c`). Repair (no statement
changed): `open scoped Matrix`; the lambda of line 137 replaced by a typed `hfc : f ≠ c`; the `if_neg` lambda of
`hdiagUnit` given its type by `show` (the same elaboration hazard, not reported because the parse error stopped that
proof first). Repaired module: blob `fadf980e`, sha256 `0f8aa17a…`. The bodies of (a), (b) and (c) after `hsa` were not
elaborated in run 1 and are first checked in dispatch 2. Prediction for dispatch 2: BUILT, moderate (about 0.55).

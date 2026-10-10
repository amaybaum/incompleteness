# BAL — can the frame, relT and two-sided positivity select the dimension for a balanced NOT?

Research-only thread, authorized by the owner on 2026-10-08. Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`
(RELC-SELECT-1's landing). Nothing here changes git, a manuscript, the roadmap or any round, and nothing is adopted,
preregistered or frozen. There is no local Lean toolchain. **Kernel facts below are readings of landed statements at
`bcbc516f`**; everything else is a written proof or an exact computation in this directory.

Notation is that of `OIBridge.CompositeDimension` and the REL-T ledger (`../relt/LEDGER.md`):

- `H = ℝ^{d+1}` with index 0 the unit; `Ñ = homMap N`; `T = lift(z^⊥)`.
- `relT`: `G` commutes with `I ⊗ Ñ`. **Balanced**: `finrank plusSpace N = finrank minusSpace N`, i.e.
  `p_N = q_N`, where `p_N = dim Fix N` and `q_N = dim(E₋(N) ∩ z^⊥)`, so `d = p_N + q_N + 1`.
- PARITY-NOT-1's `n5` has `p = q = 2`. RELC-SELECT-1's `nC5` has `p = 1`, `q = 3`.
- **Corner identity** is the conclusion of DIM-1's `gate_corner_neg`:
  `G(hom(−z) ⊗ Y) = hom(−z) ⊗ Ñ M₀ Y` for every `Y`, with `M₀ = Mfwd z G`.

## Question and productivity test

Owner: can the frame, relT and two-sided positivity select the dimension when the NOT has equally sized eigenspaces?
Distinguish a genuinely provable selector from a counterexample or a missing independent premise.

**Productivity test, fixed before the walk.** The thread is a gem iff it decides the selector question for balanced
NOTs — a proof that balance + IsNot + frame + relT + posFwd + posInv ⇒ `d ∈ {1, 3}`, or an explicit counterexample —
**and** either names the independent premise that would restore a selector, with a countermodel showing its
independence, or exposes a hidden assumption. Anything less is recorded only.

**Verdict on the test: GEM.**

## Answer

1. **Not a selector — counterexample.** At `d = 7` the balanced NOT `N7b = diag(1,1,1,−1,−1,−1,−1)` (eigenspaces
   4 and 4) carries a gate `C7b` that satisfies:
   - IsNot, the frame, relT, `G² = I`;
   - forward and inverse positivity.

   It fails relC. The same construction works at every `d ≡ 3 (mod 4)` (B1′). So balance + IsNot + frame + relT +
   P± do **not** give `d ∈ {1, 3}`.
2. **For `n5` itself the clauses do exclude `d = 5`.** No invertible `G` on `W 5` satisfies the frame, relT for any
   NOT with `p_N = 2` (in particular `n5`) and both positivity clauses (B2). The balanced case is also excluded at
   `d = 9` (B3).
3. **The missing independent premise is the corner identity.** DIM-1's block reduction reads relC through exactly two
   lemmas (kernel reading, B4):
   - `opGate_homMap_comp`, i.e. parity, which gives balance;
   - `gate_actC` → `gate_corner_neg`, which gives the corner identity.

   Either premise alone is insufficient:
   - balance without the corner identity admits `C7b` at `d = 7`;
   - the corner identity without balance admits `gC5` at `d = 5`, landed in RELC-SELECT-1.

   Together with IsNot, frame, relT and P± they restore `d ∈ {1, 3}`, by DIM-1's own reduction with the two relC
   steps taken as hypotheses (B4).

Classification for the balanced question: **COUNTEREXAMPLE** (as a selector), with an **INDEPENDENT PREMISE** named
and witnessed (the corner identity), and genuine exclusions of `d = 5` and `d = 9`.

## Node tree

### B0 — the normal form under frame + P± + relT (REL-T N2.1, extended by relT)

Steps 1–5 of REL-T N2.1 (written; unbuilt steps listed under Open gaps) give:

- `G(hom z ⊗ Y) = hom z ⊗ M₀Y` and `G(hom(−z) ⊗ Y) = hom(−z) ⊗ M₁Y`, with `M₀, M₁` cone automorphisms fixing `e₀`;
- `S = M₁M₀⁻¹ = 1 ⊕ σ` with `σ ∈ O(d)` and `σz = −z`;
- after `Gt = G ∘ (I ⊗ M₀⁻¹)`, the tangent block `𝕂 = Gt|_{T⊗H}` is invertible, with blocks
  `L_{k,t} = [[0, aᵀ], [a, A]]`, where `σa = a`, `Aᵀ = −A` and `σᵀA = Aσ`.

**Added by relT (written, elementary).**

- Apply relT to `hom(±z) ⊗ Y`: `M₀` and `M₁` commute with `Ñ`. So `σN = Nσ`, and `Gt` again satisfies relT.
- Apply relT to `lift t ⊗ Y`: every block commutes with `Ñ`. So `Na = a` and `AN = NA`.

### B1 — the balanced counterexample at d = 7 (`bal_c7.py`, 33/33)

**The construction** (`bal_gates.jk_gate_general`) — the J/K gate of NB-1 and RELC-SELECT-1, with `σ` decoupled
from `N`:

- `u₀ = e₁ ∈ Fix N7b`, and `σ = 2u₀u₀ᵀ − I`;
- `J` is the orthogonal complex structure on `z^⊥` with pairs `(1,2), (3,4), (5,6)`;
- `K = K_V ⊕ K_F` is an orthogonal complex structure on `E₋(σ)`, with pairs `(2,3)` on `V = Fix N7b ⊖ u₀` and
  `(4,5), (6,7)` on `F = E₋(N7b)`. It commutes with `N7b`.

The gate:

    G(hom z ⊗ Y) = hom z ⊗ Y
    G(hom(−z) ⊗ Y) = hom(−z) ⊗ (1⊕σ) Y
    G(lift t ⊗ Y) = lift t ⊗ X P₊ Y + lift(J t) ⊗ K P₋ Y      (t ⊥ z)

Here `P₊` projects onto `span(e₀, lift u₀)`, `P₋ = I − P₊`, and `X` exchanges `e₀ ↔ lift u₀`.

**Exact checks:**

- IsNot (eball 7) `z7` `N7b`; balanced, with eigenspaces `(4, 4)`;
- frame; relT for `N7b`; `G² = I`;
- relC fails, at entry `(7,2)` of the image of `entW 0 2`: the control side gives `−1` and the target side `1`;
- `σ ≠ N7b`, so the corner identity fails;
- the normal form holds: corner maps `I` and `1⊕σ`, tangent outputs in `T`, blocks in `Lsig(σ)` commuting with
  `Ñ7b`, and an invertible tangent block.

**Positivity — written proof, every algebraic step an exact identity** (I1–I6 in `bal_gates.certificate_identities`,
verified at `d = 3, 5, 7`). Write

- `A = ½(1+x_z)(e₀+e_z)P` and `B = ½(1−x_z)(e₀−e_z)Q`;
- `C = (e_T·x_T)α + (e_T·Jx_T)β`;
- `P = ⟨f, hom y⟩`, `Q = ⟨f, hom σy⟩`, `α = ⟨f, X P₊ hom y⟩` and `β = ⟨f, K P₋ hom y⟩`.

Then:

- (I1) value `= A + B + C`.
- (I5) `4AB − C²` is the sum of three terms:
  - `[(1−x_z²)(e₀²−e_z²) − |x_T|²|e_T|²] PQ`;
  - `|x_T|²|e_T|² (PQ − α² − β²)`;
  - `[|x_T|²|e_T|²(α²+β²) − C²]`.
- The first term is `≥ 0` by the ball condition (`|x_T|² ≤ 1 − x_z²`), the cone condition (`|e_T|² ≤ e₀² − e_z²`) and
  `P, Q ≥ 0` (self-duality of the Lorentz cone).
- The second term is `≥ 0` by (I2) + (I3): `PQ − α² − β²` is
  `(f₀² − f_u² − |f₋|²)|y₋|² + Bes_K + (f₀² − f_u²)(1 − |y|²)`, and `|y₋|² Bes_K = |g_K|²`.
- The third term is `≥ 0` by (I6) + (I4): it equals `(α²+β²) Bes_J + (…)²`, and `|x_T|² Bes_J = |g_J|²`.
- Since `A, B ≥ 0` and `4AB ≥ C²`, the value is `≥ 0`.
- posInv: `G⁻¹ = G`.

This is the argument the kernel already carries at `d = 5` for `gC5` (`selC5_besselJ/K`, `selC5_mix`, `selC5_core`).
At `d = 7` only the vectors are longer.

**Controls.**

- P1: the builder reproduces the landed `gC5` exactly (36×36 matrix equality with the `sgnC5/pcC5/ptC5` tables), and
  `c5_sep`'s entries `1` and `−1`.
- P2: at `d = 3` with `nflip` the builder gives a gate that satisfies relC too.
- P3: `d = 5`, `N = diag(1,1,1,−1,−1)` (`p_N = 3`) is admitted.
- C1: a `K` not commuting with `N7b` fails relT.
- C2: tightness. At an explicit witness (`x = e₁`, `e = (1, −Je₁)`, `y = e₂`, `f = (1, Ke₂)`), `C7b`'s value is exactly
  `0`, and the variant with `J ↦ 2J` gives exactly `−1`.
- C3: `gJ5_value = −1/10`.
- C4: `nC5` has eigenspaces `(2, 4)`; `n5` has `(3, 3)`.

**Recorded weakness of the sampler.** Exact random rational sampling found 0 negative values in 400 + 200 samples of
the non-positive `2J` variant. Random sampling is therefore not a positivity test here, and no conclusion rests on
it. The written proof and the tight witness carry the positivity claims.

**B1′ — the family (written; instances exact at `(1,1)`, `(1,3)`, `(3,1)`, `(3,3)`).**

- **Construction:** if `p_N` and `q_N` are both odd, the construction above works for `N`, with
  `K = K_V ⊕ K_F` on `V = Fix N ⊖ u₀` (dimension `p_N − 1`) and `F = E₋(N)` (dimension `q_N + 1`), both even.
- **relC fails for `d ≥ 5`:** otherwise the gate would be a NativeGate at `d ≥ 5`, contradicting the kernel's
  `dim_of_nativeGate`. The failure is also checked exactly at `d = 5, 7`.
- **Balanced case:** `p_N = q_N = (d−1)/2` is odd iff `d ≡ 3 (mod 4)`.

### B2 — `p_N = 2` is excluded, in every `d` (written; exact corroboration in `bal_excl.py` E1, E3a)

Assume frame + relT + P±. The tangent block is injective, so no nonzero vector is killed by every block.

- `p_σ = 0` forces `a = 0` (since `a ∈ Fix σ`), so every block kills `e₀`.
- `p_σ ≥ 2` forces `a = 0` by positivity:
  - take `y = v` and `f = (1, −(cos φ v + sin φ u))` for orthonormal `v, u ∈ Fix σ`;
  - then (E2, exact) `fᵀ L hom v = (1 − cos φ)(a·v) − sin φ (a·u + u·Av)`;
  - the criterion `|κ| ≤ PQ = (1 − cos φ)²` forces the `sin φ` coefficient to vanish;
  - rotating `(v, u)` in the plane gives `a ⊥ Fix σ`.
- So `p_σ = 1`, `Fix σ = span(u₀)`, and `u₀ ∈ Fix N`, since some block has `a ≠ 0` with `a ∈ Fix σ ∩ Fix N`.

If `p_N = 2`, let `u₁ ⊥ u₀` in `Fix N`.

- `σ` preserves `Fix N ∩ u₀^⊥ = span(u₁)` and fixes only `u₀`, so `σu₁ = −u₁`.
- For every block: `a·u₁ = 0`, and `Au₁ ∈ Fix N ∩ E₋(σ) = span(u₁)`. By antisymmetry `Au₁ = 0`.
- So every block kills `lift u₁`, and `𝕂` is singular. Contradiction.

Exhaustive corroboration at `d = 5` for `n5` (E1, 25 rows):

- the case split: `σ = s₊ ⊕ s₋ ⊕ (−1)`, with `s₊, s₋ ∈ {I, −I, diag(1,−1), F(m), R(m)}` (symbolic `m` covers every
  reflection and every rotation; `I` and `−I` are the special rotation angles);
- the outcome: every case is excluded, either by a common kernel vector or by the positivity step;
- the case `σ = n5` (`p_σ = 2`, the relC case): the linear common kernel is 0, and only the positivity step excludes
  it (E4).

### B3 — `p_N = 4` and `q_N = 2` are excluded; the balanced `d = 9` goes (written + exact parts)

**Lemma (so(m) ⊗ so(3); written, exact identity E0b at `m = 2, 4`, Gröbner basis `[1]` at `m = 2, 3`).**

No invertible `M ∈ so(m) ⊗ so(3)` has `M⁻¹ ∈ so(m) ⊗ so(3)`, for any `m`.

- Write `M = Σ P_r ⊗ E_r` and `M' = Σ Q_s ⊗ E_s`, with `E_r = [e_r ×]`.
- The `(i, j)` block of `MM'` is `P_jQ_i − δ_ij Σ_r P_rQ_r`.
- So `MM' = I` gives `P_iQ_i = −I/2` and `P_jQ_i = 0` for `i ≠ j`, which is impossible.
- This generalizes REL-T N5's `S₃` obstruction (`m = 3`) to every `m`.

**Consequence.** Let `B` be `V = Fix N ⊖ u₀` or `F = E₋(N)`.

- **`σ|_B = −I` is forced when `dim B = 3`** (exact E3b, E3c). A rotoreflection on `V` gives `A|_V = 0`. A rotation in
  `F ∩ z^⊥` gives `Az = 0`. Either kills a lift.
- **The `S`-condition.** REL-T N5 case (e) steps 1–3 are re-derived here for each `σ = −I` block `B` preserved by `N`.
  They give `α ∈ O(d−1)` and `Ŝ_B = (αᵀ ⊗ I) 𝕂_B ∈ so(T) ⊗ so(B)`, with `Ŝ_B⁻¹` there too (from the inverse gate).
- **The exclusion.** For `dim B = 3`, the lemma excludes this. So `p_N = 4` (`dim V = 3`) and `q_N = 2` (`dim F = 3`)
  are excluded.
- **Balanced case:** `d = 9` (`p = q = 4`) is excluded. So is `d = 5` again, through `dim F = 3`.

**Pressure test** (`bal_scond.py`, 20/20). The derived conditions — the `a ∈ span(u₀)` block shape, `α` orthogonal,
`Ŝ_B` and `Ŝ_B⁻¹` in `so ⊗ so` — were extracted from the actual matrices of all four known valid gates:

- DIM-1's `cnot` (transcribed independently of the builder);
- the landed `gC5`;
- P3;
- `C7b`.

All four satisfy them. The non-positive controlled-`n5` gate and `gJ5` fail them. A valid gate violating a derived
condition would have refuted the derivation; none does.

### B4 — the missing premise (kernel reading + written; independence witnesses exact)

**Kernel reading at `bcbc516f`.** `CompositeDimension.lean` is byte-identical to `e2426ba4`. `relC` is read at
exactly two sites:

- `opGate_homMap_comp` (line 503, consumed by `Lop_anti` → parity);
- `gate_actC` (line 1945, whose only use is `gate_corner_neg`, line 1965).

**Restated selector** (written; kernel-feasible as a line-for-line restatement, as RELC-SELECT-1 did for `CtrlGate`):

> IsNot + frame + posFwd + posInv + relT + the corner identity + balance ⇒ `d ∈ {1, 3}`.

The relation-free route also gives it without relT: the corner identity makes `σ = N`, B2 gives `p_σ = 1`, and balance
gives `q_N = 1`.

**Independence witnesses (exact):**

| witness | balanced | corner identity | other clauses (IsNot, frame, relT, P±) | `d` |
| --- | --- | --- | --- | --- |
| `C7b` | ✓ | ✗ | ✓ | 7 |
| `gC5` (landed) | ✗ | ✓ (`σ = nC5`, P1) | ✓ | 5 |

So each half of what relC supplies is needed, and neither follows from the other clauses.

**Operational reading** (an interpretation, not a claim). The frame fixes the gate only on the corner target states.
The corner identity asks that, with the control at `−z`, the gate act on the **whole** target as the NOT relative to
the `z` slice. It is the difference between a frame-level CNOT and a controlled-NOT.

### B5 — classification by `(p_N, q_N)` under frame + relT + P±, `2 ≤ d ≤ 9`

- **Admitted** (`p`, `q` both odd; B1′): `(1,1)`; `(1,3)`, `(3,1)`; `(1,5)`, `(3,3)`, `(5,1)`; `(1,7)`, `(3,5)`,
  `(5,3)`, `(7,1)`.
- **Excluded:**
  - `p ∈ {0, 2, 4}` or `q ∈ {0, 2}`, which covers every other case with `d ≤ 5`, `d = 7` and `d = 9`;
  - all of `d = 2` and `d = 4`.
- **Open:** `d = 6`, `(1,4)`; `d = 8`, `(1,6)`, `(3,4)`, `(6,1)`. These need `so(m) ⊗ so(n)` for odd `n ≥ 5` and
  repeated-angle `σ`; they inherit REL-T N6.
- **Balanced:**
  - admitted: `d = 1`, `3`, `7`, `11`, `15`, …;
  - excluded: `d = 5`, `9`;
  - open: `d ≡ 1 (mod 4)`, `d ≥ 13`.

## Classification (AGENTS.md §A.31)

- **NEW:**
  - B1/B1′ — the balanced counterexample family; this settles the question RELC-SELECT-1's non-inference rule left
    open;
  - B2 — `p_N ≠ 2`, in every `d`;
  - B3 — the so(m) ⊗ so(3) lemma for every `m`, with `p_N ≠ 4`, `q_N ≠ 2`, and the balanced `d = 9` exclusion;
  - B4 — relC's selector work splits into two independent premises, balance and the corner identity, each witnessed.
- **POSITIVE:** `n5` is excluded at `d = 5` (B2); the derived conditions hold on every known valid gate (pressure
  test).
- **CONFIRMING:** P1, the builder equals the landed `gC5`.
- **Assumption-watch marker.** Statements that "relC is needed for selection" should say which half is meant:
  - balance: parity, `opGate_homMap_comp`;
  - the corner identity: `gate_corner_neg`.

  A premise that sources only one of them does not source the selector.

## Open gaps (nothing is claimed beyond these)

1. **Nothing new is kernel-checked.** Exact computations certify the identities and the finite case analyses. The
   positivity of `C7b` is a written proof whose algebraic steps are exact identities; its `d = 5` analogue is
   kernel-proved.
2. **The exclusions (B2, B3) rest on unbuilt steps:**
   - REL-T's normal-form steps (corner form at `−z` via `(I⊗ρ̃_z)∘G`; `Aut(L)_{e₀} = 1 ⊕ O(d)`; the positivity
     criterion's necessity half);
   - for B3, the `S`-condition derivation (REL-T N5 (e) steps 1–3, re-derived here).
3. **Open cases:**
   - balanced `d ≡ 1 (mod 4)`, `d ≥ 13`;
   - the even-`d` cases listed in B5;
   - posFwd alone (without posInv) is not treated.
4. **The relation-free form of B4** (without relT) rests on the same unbuilt normal form. The relT form is
   DIM-1's own reduction with two hypotheses substituted.

## What a later governed round could freeze (suggestions only; a proposal returns for separate review)

- **Kernel, moderate:**
  - `C7b` at `d = 7` as a signed-permutation gate, like `gC5`: decide-based frame and relT, positivity via 7-variable
    versions of the `selC5_*` lemmas;
  - with it, "balance + IsNot + frame + relT + P± ⇏ `d ∈ {1, 3}`".
- **Kernel, moderate:** DIM-1's selector restated over `NativeGate` with relC replaced by two hypotheses, the corner
  identity and balance (the B4 selector).
- **Kernel, harder:** the `d = 5` balanced exclusion (`p_N ≠ 2`). It needs the relation-free normal form at the `−z`
  corner, which DIM-1 obtains only through relC.

## Files

- `bal_gates.py`: the generalized J/K builder, the transcribed landed `gC5`, and the certificate identities.
- `bal_c7.py` → `bal_c7.out`: B1, P1–P3, C1–C4 (33/33).
- `bal_excl.py` → `bal_excl.out`: E0–E4 (46/46).
- `bal_scond.py` → `bal_scond.out`: the B3 pressure test (20/20).
- `relt_common.py`, `relt_lsig.py`: verbatim copies from `../relt/` (sha256 `02cb7ddb…`, `884343c4…`).
- `src/`: the Lean sources read at `bcbc516f`.

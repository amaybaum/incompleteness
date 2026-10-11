# NOTES-C16 — closing review: the Bell corner `c = 2` of the rank-one obstruction; κ with G16

Closing-review node (not in the round-3 node list), opened 2026-10-11T01:31Z (`date -u`) after nodes C11–C15 and before
the closing LOG entry. Re-reading the handoff proposals against the rows exposed two scope defects in this round's own
rows:

1. Rows C13.4, C13.6, C13.7 and C15.3 state that no rank-one orbit surgery with a common `c` is self-dual and cite Lemma
   C13-O (row C13.2), which covers `c ∈ (1, 2)` only (for `c = 2` its `λ` is infinite, as NOTES-C13 C13-O says). The Bell
   corner `c = 2` was not argued.
2. Row C13.9 (and the verdict of NOTES-C13) says κ with G16 carries "the orthogonal-pair obstruction to the rank-one
   route". No argument for κ was given. The argument of C13-S2 uses the S2 torus, which moves all four coordinates of the
   basis `B = (|0+⟩, |0−⟩, |1+⟩, |1−⟩)`; κ's torus `T_κ = {U(x)U′(x′)}` (NOTES-C5) fixes the `|0±⟩` coordinates.

Conventions as in NOTES-C11 and NOTES-C13. `G16 = ⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` ([A] C5, Z; `T` the transpose, i.e. complex
conjugation of state vectors in the computational basis). In `B` with coefficients `(a, b, c, d)`: `det Ψ = bc − ad`,
`U(x) = diag(1, 1, 1, x)`, `CNOT = diag(1, 1, 1, −1)`, `Z⊗I = diag(1, 1, −1, −1)`, `I⊗Z` the permutation `(12)(34)`, and
`T` conjugates the coefficients (the basis is real).

## S0 — predictions written before the first run of any C16 script (2026-10-11T01:31Z, `date -u`)

No scratchpad computation; the values below were worked by hand during the review.

1. **Bell corner under a maximal torus (written).** For the maximal torus `T³` of an eigenbasis `(b_k)`, a state whose
   `T³`-orbit is maximally entangled is either a maximally entangled eigenline or a balanced superposition
   `(b̂_k + w b̂_l)/√2` of two product eigenlines with `|B(b̂_k, b̂_l)| = 1/2` (`B` the symmetric bilinear form with
   `B(v, v) = det Ψ(v)`). In the residual region of C10.3 an orbit admissible for H1 at `c = 2` is a single such phase
   circle, whose surgery is unitarily equivalent to C7.6's and is not self-dual. Case B (products `b₁, b₃` only, R0 of
   C13) and `T³ ⋊ D₄` (cnot carries both computational Bell circles to products) admit no orbit at `c = 2`. Predicted:
   BC1 and BC2 pass.
2. **Bell corner for S2 and κ with G16 (citation).** The CNOT argument of [A] Z puts every orbit admissible at `c = 2`
   inside `C1 ∪ C2`; for both nodes at level (ii) that orbit is `C1 ∪ C2` and its surgery is `K_T`, not self-dual ([A] Z,
   `ipW = −24/625`). Predicted: BC3 (`C1 ∪ C2` invariant under the κ generators, `I⊗Z` swapping the circles) passes.
3. **κ with G16: no orthogonal-pair obstruction, and an explicit cone.** `h = 2|0+⟩ + |0−⟩ + ½|1−⟩ ∝ (6, 2, 1, −1)`
   (computational). Its orbit under `G_κ = closure⟨U(x), G16⟩` is the two circles `{(6, 2, x, −x)}` and `{(6, −2, x, x)}`,
   `|x| = 1`. Squared overlaps are `≥ 361/441` within a circle and `= 256/441` across, so there is no orthogonal pair;
   `|det Ψ|² = 16/441` on the whole orbit, so `h` is unreachable. At `c = 103/100` H1 holds (`1 − 4D = 377/441 ≤ (97/103)²`)
   and (CC) holds for every pair, so `K_κ := K(G_κ·(I − cP_h))` is an explicit `G_κ`-invariant self-dual cone with H1–H3,
   `≠ Q3`, whose non-PSD extreme rays are two circles — EXOTIC-X for the stage-5/6 κ node, CONDITIONAL on Theorem S′ only.
   C13.9's parenthetical is false for κ. Predicted: K1–K6 pass, including the S′ consequence check (PSD at the far cap edge
   and the midpoint of the cross pair).
4. **Countercontrols.** CC1: under the S2 group with G16 the same `h` has an exactly orthogonal partner,
   `(R_z(π)⊗R_x(π))(I⊗Z)h = (2, −6, 1, 1)`, so the torus decides, not the double transposition. CC2: H1 fails at
   `c = 26/25` (`(12/13)² < 377/441`), so the window is real. CC3: `(2, 0, 1 + i, 1 − i)` is entangled and `U(−i)` carries
   it to a product, so the unreachability test is not vacuous. CC4: at `c′ = 5/4`, above the (CC) bound (about 1.214) of
   `s = 256/441`, the cross pair violates (CC) and has an exact pair-level witness.
5. **T on `K_κ` (written, not computed).** C14-1 gives `c ≤ 14` on its defects; C14-2's hypothesis holds (contact points of a
   circle-1 defect in `span(e₁, e₂)` have squared overlap `≤ 64/105 < 1/c` with every circle-2 state), so `c = 14` on the
   defects and T fails, as on the other circle cones.

(Runs, results and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T01:36Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c16_kappa_bellcorner.py` | 1 (01:35:14Z) | 15/15, `VERDICT C16-KAPPA-BELLCORNER-EXACT` | identical (out `6d0a5dfe…`) |

Order of record, by file modification times (UTC): S0 text 01:32:44 (header reading 01:31:37Z), decision rule 01:32:52Z,
script after its two pre-run edits 01:35:04, run 01:35:14. Pre-run edits, both in helpers and made before any run:
`Ux` built `GQ(x − 1)` from a Gaussian rational (a constructor error), now `(x − 1)/2`; `diag` wrapped Gaussian-rational
entries the same way, now passes them through.

## Results

### C16-1 — the Bell corner under a maximal torus [W + X BC1, BC2]
**Lemma C16-1.** *Let `T³` be the maximal torus of an orthonormal eigenbasis `(b̂_k)` and `h = Σ_k a_kb̂_k` a unit vector
whose `T³`-orbit consists of maximally entangled states. Then either `h` is an eigenline `b̂_k` that is maximally entangled,
or `h = (b̂_k + wb̂_l)/√2` up to phase, with `b_k, b_l` products, `|B(b̂_k, b̂_l)| = 1/2` and `|w| = 1`. In the second case the
`T³`-orbit is the whole phase circle `{(b̂_k + wb̂_l)/√2 : |w| = 1}`.* Here `B` is the symmetric bilinear form with
`B(v, v) = det Ψ(v)`; `B(u, v) = uᵀMv` with `2M` unitary, so `|B(u, v)| ≤ 1/2` for unit `u, v`.
Proof. `det Ψ(Σ_k e^{iθ_k}a_kb̂_k) = Σ_k e^{2iθ_k}a_k²β_kk + Σ_{k<l} e^{i(θ_k+θ_l)}2a_ka_lβ_kl` (`β_kl = B(b̂_k, b̂_l)`) is a
trigonometric polynomial on `T⁴` whose frequencies `2e_k`, `e_k + e_l` are pairwise distinct. If two of its coefficients
were nonzero, a linear functional separating the frequencies picks extreme frequencies `F⁺ ≠ F⁻`, and the coefficient of
`e^{i⟨F⁺ − F⁻, θ⟩}` in `|det Ψ|²` is the single product `c_{F⁺}c̄_{F⁻} ≠ 0`, so `|det Ψ|` is not constant. Exactly one
coefficient is therefore nonzero. If it is `a_k²β_kk` and some other `a_l ≠ 0`, then `|det Ψ| = |a_k|²|β_kk| < 1/2`. If it
is `2a_ka_lβ_kl`, then `|det Ψ| ≤ |a_k||a_l| ≤ 1/2`, with equality iff `|a_k| = |a_l| = 1/√2` and `|β_kl| = 1/2`; the vanishing
monomials `a_k²β_kk`, `a_l²β_ll` then make `b_k, b_l` products. The global phase is irrelevant. ∎

**Corollary C16-2.** *Suppose moreover that some eigenline is entangled and that `G ⊇ T³`, with eigenline group `Π`, carries
every entangled eigenline onto a product eigenline (the residual region of C10.3). Then an orbit admissible for H1 at
`c = 2` (every member maximally entangled) is a single phase circle of two product eigenlines `b_k, b_l` with `Π` preserving
`{k, l}`, and its surgery is not self-dual.* Proof. An eigenline orbit contains a product. Otherwise every `σ̃h` (`σ ∈ Π`)
falls under Lemma C16-1, so `{σk, σl}` is again a pair of products: the `Π`-orbit `Π·E` of the entangled set `E ≠ ∅` avoids
`{k, l}`. Each orbit `Π·m` (`m ∈ E`) meets the products, hence meets `P ∖ {k, l}` (`P` the products); since `|P| ≤ 3`, this
forces `P = {k, l, p}`, `E = {m}`, `Π·m = {m, p}`, so `Π` preserves `{m, p}` and `{k, l}`. The torus sweeps the circle and
`Π̃` maps it to itself, so the orbit is the circle. A unitary carrying `(|0−⟩, |1+⟩)` to `(b̂_k, b̂_l)` carries the circle `C2`
onto it; C7.6 (with the unitary of `c7_circle` B5) shows `K(Z_{C2})` is not self-dual, and `K(UZU†) = UK(Z)U†` because `Q3`
and the trace pairing are unitarily invariant. ∎
Instances [X]: in case B (C13-B) the products are exactly `b₁, b₃` [X BC2], so `|P| = 2` and no orbit is admissible at
`c = 2`. For `T³ ⋊ D₄` on the computational basis (C15-3; product eigenbasis, so Lemma C16-1 is used directly) `B` is nonzero
only on `{|00⟩, |11⟩}` and `{|01⟩, |10⟩}`, and `cnot` carries both Bell circles to products [X BC1]: no orbit is admissible
at `c = 2`.

### C16-2 — the Bell corner for S2 and κ with G16 [A Z + X BC3]
The generators of κ's group with G16 map `C1 ∪ C2` into itself, and `C1 = {f₁ + xf₄}`, `C2 = {f₂ + xf₃}` are Bell-type
circles [X BC3] (for the S2 group: [A] Z). By the
CNOT argument of [A] Z (`|A − B| = |A + B| = 1/2` forces `AB = 0`), every orbit admissible at `c = 2` lies in `C1 ∪ C2`. For
the S2 node and for κ, both with G16 (`CNOT = U(−1)` lies in κ's group), the torus sweeps each circle and `I⊗Z` swaps them, so
the orbit is `C1 ∪ C2` and its surgery is `K_T`, which is not self-dual ([A] Z, `ipW = −24/625`). Without G16 the orbit is one
circle, and the one-circle surgery `K′` is not self-dual ([A] Z; C7.6).

### C16-3 — scope of the rank-one obstruction rows
- **C13.4, C13.6, C15.3** ("no rank-one orbit surgery with a common `c` is self-dual"): `c ∈ (1, 2)` by Lemma C13-O;
  `c = 2` by C16-1 (C13.4: by Corollary C16-2 an admissible orbit is a single phase circle, not self-dual; C13.6 and
  C15.3: no orbit is admissible). The statements hold for every `c ∈ (1, 2]`.
- **C13.7** (the S2 node with G16): `c ∈ (1, 2)` by Lemma C13-O and C13-S2's orthogonal pairs; `c = 2` by C16-2 (`K_T`).
- **C13.9's parenthetical** ("each now with the orthogonal-pair obstruction to the rank-one route"): established for the S2
  node with G16 (C13-S2) and for `K_circ` at `c < 2` (C13-Π (i): its torus `T³_F` is maximal and its eigenline group
  `S₄` contains double transpositions). At `c = 2` the only admissible orbit for `K_circ`'s group is `Z_F` (Lemma C16-1:
  every eigenline `ψ_s` is maximally entangled and no eigenline is a product), whose surgery `K(Z_F)` has slice `R`, not
  `Circ`. **For κ with G16 the parenthetical is false** (C16-4).

### C16-4 — κ with G16: an explicit exotic cone [X K1–K6, CC1–CC4 + W]
`G_κ = closure⟨U(x), cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` is the torus `T_κ = {diag(1, 1, x′, x)}` (in `B`) extended by `I⊗Z` and
`T`. Its torus fixes the `|0±⟩` coordinates, so the double transposition `I⊗Z` does not force orthogonal pairs: the orbit of
`h = (6, 2, 1, −1) = 2(2f₁ + f₂ + ½f₄)` (computational) is the two circles `{(6, 2, x, −x)}` and `{(6, −2, x, x)}` [X K1].
Within a circle `|⟨v|v′⟩| ≥ 38` and across circles `⟨v|v′⟩ = 32`, with `|v|² = 42`, so every squared overlap is at least
`s_min = 256/441` [X K2]. Every member has `|det Ψ|² = 16/441` (`det = ∓8x`), so `h` is unreachable [X K3]. At `c = 103/100`
H1 holds (`1 − 4D = 377/441 ≤ (97/103)²`) [X K3], every pairing is positive and (CC) holds for every pair
(`c²s_min = 169744/275625 ≥ 3/25`) [X K4]. `d = I − cP_h` has eigenvalue `−3/100` [X K5]. By Theorem S′ for compact defect sets
(C13-S), **`K_κ := K(G_κ·z)`, `z = E00/2 − (c/8)T_h` (recorded in `c16_kappa_bellcorner.out`), is an explicit
κ-and-G16-invariant self-dual cone with H1–H3 and `≠ Q3`, whose non-PSD extreme rays are the two circles** (C13-S
extremality) — EXOTIC-X for the stage-5/6 κ node, CONDITIONAL on S′ [W] only. This is C5.4's κ half, by a surgery.
Consequence check of S′ [X K6]: on the cross pair the would-be witness `P_v + λd_k` is PSD at the far cap edge and at the
midpoint. Controls: under the S2 group with G16 the same `h` has the exactly orthogonal partner `(2, −6, 1, 1)` [X CC1], so the
torus decides, not the double transposition; H1 fails at `c = 26/25` [X CC2]; `(2, 0, 1 + i, 1 − i)` is entangled and
`U(−i)` makes it a product [X CC3]; at `c′ = 5/4` the cross pair violates (CC) and has an exact pair-level witness [X CC4].
**T on `K_κ`** [W]: a circle-1 defect `d₀` has contact points in `span(ĥ₀, ê)` (unit vectors along `h₀ = (6, 2, 0, 0)` and
`e = (0, 0, 1, −1)`) with squared overlap `64v₁²/105 ≤ 64/105 < 1/c` with every circle-2 state, hence an open subset of the
contact set `C₀` of C14-2 lies outside the other circle's closed caps. C14-2 then gives `c(d₀) = 14`, against `c(P00) = 9`
(Lemma 1 of C3), so T fails on `K_κ` (Y6 [A]).

## Verdict on node C16
- The Bell corner closes: the rank-one obstruction statements of C13.4, C13.6, C13.7 and C15.3 hold for every
  `c ∈ (1, 2]` (C16-1 and C16-2; C7.6 and [A] Z for the circles).
- C13.9's orthogonal-pair parenthetical is false for κ with G16, and κ with G16 has an explicit exotic cone with a continuum of
  non-PSD extreme rays (CONDITIONAL on S′). On it T fails (C14-2).
- Of the OPEN items of C13.9, κ with G16 is answered; case B, the S2 node with G16, `K_circ` and degenerate 2-tori remain.

## Gem classification (§A.31)
- NEW: κ with G16 is EXOTIC-X (a two-circle surgery). The obstruction claimed for it was an unverified transfer from the
  S2 node, which has the same double transposition but a different torus.
- ELABORATING: Lemma C16-1 and Corollary C16-2 (at `c = 2` a maximal-torus orbit is a Bell eigenline or a phase circle of two
  product eigenlines; in the residual region, one circle).
- Assumption-watch marker (refines the round-3 marker of HP6): an orthogonal pair inside an orbit is the obstruction for
  defects with `c < 2` only. A double transposition of eigenlines forces one only together with a torus that moves the
  relative phases of both swapped pairs (a maximal torus; the S2 torus). At `c = 2` orthogonal pairs are harmless
  (Theorem S), and the obstruction is a non-orthogonal pair (C4.1, C7.6, `K_T`).

## What is not claimed
No kernel statement. Lemma C16-1, Corollary C16-2 and the T statement are [W] (this round); `K_κ` is explicit given S′. The
c = 2 statements rest on C7.6 [X + W] and [A] Z. Nothing is claimed for case B, the S2 node with G16 or `K_circ` beyond the
rank-one route, and degenerate 2-tori were not attempted.

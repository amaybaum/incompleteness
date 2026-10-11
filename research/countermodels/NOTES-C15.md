# NOTES-C15 — extra node: the native Clifford family of HO-12 (the finite half of A_miss)

Extra node after C14 (not in the round-3 node list; taken up because C11.6 bears on it directly). Object: the group
`⟨cnot, actC J, actT J⟩` (`J = cyc3`) which the overview (bridge round 2, HO-12 item 3, not received by this thread)
records as the native Clifford family of order 11520, whose invariance is the "finite half" `SPEC_P(J)` of A_miss and
which "leaves exotic cones (CONDITIONAL on claim (D))". Only the group's definition is used here; its order and every
property are recomputed. Conventions as in NOTES-C11. Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C15 script (2026-10-11T01:07:47Z, `date -u`)

Scratchpad exploration (numerical, not evidence): the projective order of the lift, and seeds: every small
Gaussian-integer seed tried has an exactly orthogonal pair in its orbit (involutions `U` give integer-valued real forms
`h†Uh` that vanish at small lattice points by coincidence), while seeds with large irregular entries have none
(`s_min ≈ 4·10⁻⁵`).

1. **The group.** `⟨cnot, actC cyc3, actT cyc3⟩` is a group of 11520 signed permutations of the sixteen coordinates; its
   Gaussian-rational lift `⟨CNOT, U_J⊗I, I⊗U_J⟩` has 11520 classes modulo `{±1, ±i}` and `Ad` maps the generators to the
   generators (a homomorphism with kernel the scalars, so the class group is the table group). No antiunitary element.
2. **EXOTIC-X.** `h = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)`: its orbit has 11520 rays, none a product
   (`λ_max ≤ 0.98`), minimal squared overlap with `h` about `4.19·10⁻⁵` (no orthogonal pair; by the group property this is the
   minimum over all pairs); at `c = 100001/100000` H1 and (CC) hold, so `K(G·(I − cP_h))` is an explicit invariant exotic
   cone with H1–H3 — CONDITIONAL on Theorem S′ [W] only (no claim (D), no EBF).
3. **Countercontrol.** `4φ₀ = (1, 2, 3i, −1 + i)` has an exactly orthogonal pair in this orbit (as for `G₃₈₄`).
4. **The continuous half.** The group of (b) for the phase flow and the NOT on each token with `cnot` is `T³ ⋊ D₄` on the
   computational basis (`D₄` = the translations and `cnot`'s transvection of `𝔽₂²`); it contains double transpositions,
   so every orbit has an orthogonal pair and the rank-one route is closed there (C13.4); EXOTIC-E only ([W], no script).

(Runs, results and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T01:10Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c15_clifford.py` | 1 (01:08:57–01:09:11Z) | 6/6, `VERDICT C15-CLIFFORD-EXACT` | identical (out `6cd53515…`) |

No pre-run edits after the decision rule was fixed.

## Results

### C15-1 — the group [X G1, G2]
`⟨cnot, actC cyc3, actT cyc3⟩` has order 11520 as a group of signed permutations of the sixteen coordinates (each fixing
`E00`), the value the overview records; its lift `⟨CNOT, U_J⊗I, I⊗U_J⟩` maps onto it (generators to generators, kernel the
scalars). All elements are unitary conjugations.

### C15-2 — an explicit exotic cone for the native Clifford family [X X1 + W]
`h = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)`: its orbit has 11520 rays, every one entangled (`|det Ψ|² ≥ 0.0202…`,
so `λ_max ≤ 0.98`), and its minimal squared overlap with another orbit ray is
`s_min = 164178929/3916193820250 ≈ 4.19·10⁻⁵` (no orthogonal pair; by the group property this is the minimum over all pairs).
At `c = 100001/100000`: H1 for every defect and (CC) for every pair. By Theorem S′ (NOTES-C11), **`K(G·(I − cP_h))` is an
explicit `G`-invariant self-dual cone with H1–H3 and `≠ Q3`, `G = ⟨cnot, actC J, actT J⟩`** — EXOTIC-X, CONDITIONAL on S′ [W]
only. The statement "the finite half of A_miss (invariance under the native Clifford family) leaves exotic cones" therefore
no longer needs claim (D) or EBF: a cone is exhibited. The margins are small (`c − 1 = 10⁻⁵`, as forced by `s_min`); the
cone differs from `Q3` only near the 11520 tiny caps. Countercontrol [X CC1]: `4φ₀`'s orbit (5760 rays) contains an
exactly orthogonal pair, as for `G₃₈₄` — small lattice seeds sit on the exceptional set of integer forms `h†Uh`; generic
seeds do not (C11-E).

### C15-3 — the continuous half: the rank-one route is closed [W]
The group of (b) for the phase flow `R_z(t)` and the NOT on each token, with `cnot`, has identity component the diagonal
3-torus of the computational basis (the local phases and `cnot`'s conjugate `P₀⊗R_z(t) + P₁⊗R_z(−t)`) and eigenline group
`D₄` = the translations of `𝔽₂²` and `cnot`'s transvection (order 8). The translation `X⊗I` is a double transposition of the
eigenlines, so every orbit of states contains an orthogonal pair (C13-Π (i)) and no rank-one orbit surgery with a common `c`
is self-dual (Lemma C13-O). The eigenbasis is a product basis (HO-2's covered case): exotic cones exist there by EBF / claim
(D) only.

## Verdict on node C15
For the two halves into which the bridge splits A_miss: the finite (Clifford) half alone leaves an **explicit** exotic
cone (CONDITIONAL on Theorem S′ [W]); the continuous (monomial) half alone leaves exotic cones by claim (D) only, and the
rank-one surgery route is provably closed for it. (Both together force `Q3` by the K2 schema — not re-examined here.)

## What is not claimed
No kernel statement; nothing about the bridge's or the equivalence thread's records beyond the group's definition; HO-12
has not been received by this thread and is not relied on.

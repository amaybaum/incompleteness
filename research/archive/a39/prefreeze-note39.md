# A39 pre-freeze measurement — the three-parameter family: realizability gate (read-only, no branch, no freeze)

Base: certified main `D = 6e8ce41db2903b8b1071f868b333cf54d8ec6397` (A38 landed). Objects are the
landed A38 probe's (`verification/lean/dita_local_escape_probe.py`, blob `00be96c3…`), loaded verbatim;
script `scratchpad/a39/gate39.py`, exact arithmetic throughout. If the roadmap PR #766 lands first, the
round's `D` becomes that landing; it changes `ROADMAP.md` only, so every object here is unchanged.

## The gate: PASSES

`H(u₁, u₂, u₃) = SIG ∘ u₁^A u₂^B u₃^C` is unitary for all units `u₁, u₂, u₃` as a Laurent-polynomial
identity: for every ordered row pair `(r, s)` and every joint difference triple
`t = (A_rj − A_sj, B_rj − B_sj, C_rj − C_sj)`, the pair sum over the columns with that triple is `16` for
`r = s, t = 0` and `0` otherwise.

| check | joint level sets | failures |
| --- | --- | --- |
| exact Gaussian rationals | 552 | 0 |
| monomial by monomial in `z`, `w` (symbolic units, the form a kernel proof takes) | 552 | 0 |

Joint triples occurring: nine — `0`, `±e_A`, `±e_B`, `±e_C`, and `±(1, −1, 0)`.

## Why it holds: the three pieces barely interact

- **Supports.** `A` lives on rows `{7, 15}`, columns `{4,5,6,7,12,13,14,15}`; `B` on rows `{8,9,10,11}`,
  columns `{1,5,9,13}`; `C` on rows `{1,3,4,6,9,11,12,14}`, columns `{2,8}`.
- `C`'s columns are disjoint from `A`'s and `B`'s, so no entry has a nonzero `C`-difference together
  with another; `A` and `B` share no row, and meet only at columns `{5, 13}`, where the pair
  `(r ∈ {7,15}, s ∈ {8..11})` sees `(1, −1, 0)` (32 entries, both signs).
- So the joint partition refines the one-variable partitions only by separating `±(1, −1, 0)` from
  `0` — the only place the line tests could have collided — and those classes vanish separately.

## Controls

| family | joint level sets | failures |
| --- | --- | --- |
| `E = A + B + C`, one variable (A38) | 512 | 0 |
| `A`; `B`; `C` alone | 312; 352; 384 | 0 |
| `(A, B)`; `(A, C)`; `(B, C)` | 424; 440; 480 | 0 |
| `(A + B, C)` | 536 | 0 |
| **countercontrol** `(A, B, C')`, one entry of `C` flipped | — | **60** |

Direct check: `H(u₅, w, (8+15i)/17)` is exactly unitary.

(Counts here are over ordered pairs including `r = s`; A38's 248 counted unordered pairs `r < s`.)

## What this licenses

The gate for a three-parameter realizability freeze is met. Not measured here, and not claimed: which
part of the three-torus admits a Diţă structure (step 4 of the owner's order), the census, and the
minimality of the support.

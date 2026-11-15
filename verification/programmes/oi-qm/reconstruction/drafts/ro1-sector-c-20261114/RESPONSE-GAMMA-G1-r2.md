# Response to the focused review of GAMMA-1 unit G1, r2

**Object.** `REVIEW-GAMMA-G1-r2.md` (blob `20d8bbc5a7ae33022a71e36b44e555b203795921`, at PR #1294
commit `0300c8437`), verdict ACCEPT WITH CHANGES. The revision is `GAMMA-G1-r3.md` (cited r3 §N). r2
(blob `44ff0b53`) is unchanged. One disposition per finding: **applied**, **partly** or **not**,
with the reason. Paper-only; hand checks only; no computation, Lean, manuscript or Issue change.

## Required

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| N1 | The credit quantifier (one observable on which every control fails) leaves nothing creditable | **applied** | The quantifier order is reversed (r3 §7.2). Credit is nonempty iff, for **every** member of `𝒦 = {C0, PC-wave, CC4, CC5}`, **some** listed observable separates it. Separation is either an established disagreement inside the member's scope (s1) or an observable outside the scope of the member's construction (s2, reported as such). An unknown result does not separate. `S(K)` is reported per member. C0's X-2 law is stated as a construction: one particle per run, so `α = 0` and X-2 does not separate C0. PC-wave's X-2 law gives `α ≥ 1`, by `E[I²] ≥ E[I]²`. By hand, `I_3 = 0` for C0, for PC-wave and for the Born reference, so X-3 separates no member. Re-check by hand (r3 §7.4): the reference is creditable at the level of laws. C0 is separated by `Δ` and X-4, PC-wave by X-2, and CC4 and CC5 by scope only. On the data side the credit waits on G3's X-2 read. No member is credited, since `S(K) = ∅` for `K` in place of `L`. New owner question 6 asks whether separation by scope suffices for CC4 and CC5. New marker AW-hyb: a classical hybrid outside `𝒦` is not excluded, and no member-by-member rule can exclude it without excluding the reference |
| N2 | The whole-channel `V` and covariance statistics misclassify envelopes and complementary pairs | **applied** | Both statistics are replaced by local ratio statistics `u = c/n` on a floored support (r3 §5.7). The normalizer is either the pair total of one marker read or the one-path sum `c_{a2} + c_{a3}`, for which `u − 1 = Δ/n`. Where neither normalizer is declared within `I`, the feature is reported as untested. Fringes present needs `V_u ≥ 0.5` and an interior extremum; absent needs `V_u ≤ 0.2` or a monotone `u`. A fringe/antifringe pair needs fringes in the pair ratio and none in the pair total. The review's 16-cell counterexample, re-run by hand, gives `u₁ = (1, ½, 0, ½)`, `V_u = 1` with an interior minimum, and a constant total: fringes and antifringes. A fringe-free envelope gives `u = ½`, or a monotone `u` for a shifted partner by log-concavity of the `sinc²` main lobe: absent. OCP's table and the standard two-slit law classify correctly. A vacuity countercontrol is added: C0, an in-phase pair and a quarter-period pair each yield a miss or a non-match. For quantitative `V`, the source's own formula and scan are used (r3 §5.5) |

## Also required by the coordinator

| Item | Disposition | Where and how |
|---|---|---|
| r1 finding 8 (`κ_cmp` statistics), partly resolved in r2 | **applied** | Resolved with N2 (r3 §5.7) |
| NC-γ6's row must not read as met | **applied** | The row states "Status at G1: open". It is met for (γ←)'s clauses and, at the level of laws, for §7.2. It is not met on the data side until G3 (r3 §7.4) |
| CALC r2 owner-accepted (#1169 c.6892224647) | **applied** | Inputs, §11 and the revision note quote the record (`amaybaum`, 2026-11-15T09:17:55Z), read through the API |

## Minor

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| M-a | CALC r2's owner acceptance on record | **applied** | As above |
| M-b | NC-γ6's status in its row | **applied** | As above |
| M-c | NC-γ6 needs a declared quantum reference for X-2 and X-3 | **applied** | Declared in r3 §7.4 for the structure of the definition only. For X-2, a single excitation at a beam splitter gives `α = 0`. For X-3, the Born rule gives `I_3 = 0`. Sources are as PLAN-G §5.3 names them, all NOT READ (G3). For `𝒜_6`, X-1, X-4 and X-5: OCP and LIT 1.12, §3 |

## Advisory

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| A-b | Report `K_P` with `∅` kept | **applied** | `K_P^∅` is reported beside `K_P` (r3 §2.4). With equal efficiency `η` on both paths and equal detected masses it equals `η`, by hand |
| A-c | Re-point PROVISIONAL citations to an accepted U4 revision | **not** | No U4 revision is accepted on record. U4 r3 and its review are on the branch but not used, and the labels paragraph says the pointers stay on U4 r2 until a revision is accepted |

## Changes beyond the findings

- The (γ←) coverage condition in r3 §6 is restated in the per-member form, to match §7.2.
- In r3 §10, G1-F8 is restated, its class moves from CONFIRMING to ELABORATING, and AW-hyb is added.
- In r3 §12, owner question 5 adds the support floor `ν` and the normalizers, owner question 6 is new,
  and G3's list gains the reference sources and the data side of the separations.

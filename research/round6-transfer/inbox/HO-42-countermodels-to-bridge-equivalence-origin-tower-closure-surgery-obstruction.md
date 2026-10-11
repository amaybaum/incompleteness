# HO-42 (v1) — countermodels → bridge, equivalence, origin: the tower's closure `G_T` admits no surgery-type invariant cone (OBSTRUCTED), with the `c = 2` statement corrected

**From** `research/countermodels` (round 5, node C23; proposal HP-countermodels-11). **To** `research/bridge` (B10-4,
B10-5, B16, B17; HO-35, HO-36, HO-40), `research/equivalence` (S6's countercontrol family) and `research/origin` (the
stage-crossing datum). Written by the coordinator from the source thread's committed record **and the coordinator's
round-5 audit**, which corrects one sub-statement (finding F-C5-1); version 1, 2026-10-11. The proposal is not issued
in its committed form: item 3 below replaces its statement 2's `c = 2` clause. Reading: invariance throughout; nothing
here concerns availability.

## The groups

`G_n = ⟨CNOT, X_B, R_B(2π/2ⁿ)⟩` (B10-5's stages); `G_∞ = ⋃_n G_n`; its closure
`G_T = cl⟨CNOT, X_B, R_B(t) : t ∈ ℝ⟩ = T² ⋊ V4` modulo phase, `T² = {D(u, v) = diag(1, uv, u, v)}`, `V4` the permutations
`{e, (23), (01)(23), (01)}` of the computational basis. Closure step: a closed cone invariant under `G_∞` is invariant
under `G_T` (H3 gives closedness; named wherever used).

## Statements and labels

1. **Universal orthogonal pair** (C23.1). With `α = h̄₂h₃`, `β = h̄₀h₁`: `⟨h|D(u, v)X_Bh⟩ = β + uvβ̄ + uα + vᾱ`, which
   vanishes for some `(u, v) ∈ T²` for every `h ≠ 0`. Every `G_T`-orbit of rays contains an orthogonal pair.
   CONDITIONAL ([W] case analysis; identities [X], verified twice). The bridge derived the same in `U(u, v)`
   coordinates (HO-40 item 1).
2. **Rank-one route closed for `c ∈ (1, 2)`** (C23.2, first part). No compact `G_T`-invariant rank-one surgery with every
   `c ∈ (1, 2)` is self-dual (C18-1's witness on the orbit of largest `c`; closed-hull form C23-5). CONDITIONAL ([W]; [X]).
3. **At `c = 2`, corrected by the coordinator** (F-C5-1, replacing the proposal's clause). **No `G_T`-orbit is
   admissible for H1 at `c = 2`**: `CNOT ∈ G_T` carries every Bell state `|00⟩ + w|11⟩`, `|01⟩ + w|10⟩` to a product, so
   the `G_T`-orbit of a Bell state contains products and H1 (with H3) admits no defect of weight `c > 1` on it; more
   generally `|x| + |y| ≤ S/√2` for `x = a₀a₃ − a₁a₂`, `y = a₀a₂ − a₁a₃`, so every `G_T`-orbit has `D_min ≤ 1/8` (attained
   exactly at `(√2/2, 0, 1/2, 1/2)`), and **H1 admits a rank-one defect orbit of `G_T` only at weights
   `c ≤ 4 − 2√2 ≈ 1.1716`**. Hence every `G_T`-invariant rank-one surgery satisfying H1 has all weights below 2 and item 2
   applies to it: the rank-one route for `G_T` is closed with no residual. The proposal's statements about the two Bell
   circles — their surgery as stage 4's `K_T` transported by `1 ⊗ H` (`tr(y′w′) = −6/625`) and the mixture instance
   `(3, 2i, 2, 1)` — are correct computations about the subgroup `T² ⋊ ⟨X_B⟩` (which lacks `CNOT`), not about `G_T`.
   The bridge established the corrected statement in the same round (B21: no `G`-orbit admissible at `c = 2`;
   `b21_ceq2` Q3–Q5 with a CNOT-free countercontrol). Label: CONDITIONAL ([W] + [X]: `indep_checkC5.py` Z3, CC3; the
   bound's attainment [X], its random-search confirmation [N]).
4. **Balanced route: the engine certifies nothing** (C23.3). For every seed and every `c ∈ (1, 2)` the engine
   `selfDual_of_local` (C17.1 [D], HO-30) certifies no balanced rank-two surgery on a `G_T`-orbit (generic seeds have no
   partner with zero pairing on the orthogonalizing family; the others have a forced partner that first-order tightness
   defeats; seeds with two vanishing coordinates are excluded by H1). The local condition fails on a pair inside every
   `G_T`-orbit, which also blocks any compact extension with the same local condition. CONDITIONAL ([W]; [X] instances
   at `c = 3/2` and `101/100`).
5. **Node outcome: OBSTRUCTED** (C23.4, unchanged by item 3). No surgery-type cone (rank-one with any weights, or
   balanced through the engine) is invariant under `G_T`, hence none is invariant under all of B10-5's stages at once —
   HO-36 item 1 extended from HO-24's cone to the surgery class. An explicit `G_T`-invariant exotic cone stays OPEN; its
   existence stays CONDITIONAL on claim (D) [A]. **Not evidence for the owner's outcome (D)**: no cone is produced.
   Scope: the stage-6 inventory at L, level (i), invariance reading; H1 and H3 introduced.
6. **The certificate** (C23.5). `experiments/c23_certificate.json` (sha256 `d5841161f024006d…`); `c23_check.py` reads
   only the certificate and recomputes every value: 9/9 `CHECK C23-CERTIFICATE-OK`, replay identical. Checked
   independently by the coordinator (`indep_checkC5.py` run 1: Z1–Z5 PASS, CC1–CC5 False, replay identical).

**Assumption-watch markers.** "An explicit cone invariant under every stage of the tower is among the surgery cones" —
false (rank-one, and engine-certified balanced). "Invariance under a dense subgroup is invariance under its closure" —
for closed cones only; the step uses H3.

## Correction obligation (for the countermodels thread, round 6)

Correct C23-2(b)–(c), row C23.2, C23.6 and HP-countermodels-11 forward to item 3 (no row or label changes: C23.2's
verdict and C23.4 stand; C23.6's first residual item does not arise for `G_T` and remains a question for
`T² ⋊ ⟨X_B⟩` only).

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `c9ac75bd` |
| proposal | `research/countermodels/handoff-proposals/HP-countermodels-11-tower-closure-obstruction-certificate.md` (sha256 `09650886…`; superseded in item 3) |
| scripts | `experiments/c23_torus.py` (`e6a3555e…`) / `.out` (`e7e58309…`): run 1 6/6 `VERDICT C23-EXACT`; `experiments/c23_check.py` (`c13e14e1…`) / `.out` (`dd7f2aea…`): run 1 9/9; replays identical |
| notes, results | `NOTES-C23.md` (`ee33e252…`: S0 revised before any run); `RESULTS.md` C23.1–C23.6 |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-COUNTERMODELS-R5.md` §4 and §8 (F-C5-1); `countermodels/indep_checkC5.py` |
| bridge | HO-40; `research/bridge` @ `5ba9218e`, `experiments/b21_ceq2.py` Q3–Q5 |

## What the receiving threads may assume

Items 1–6 at their labels, item 3 as corrected here.

## What they may not assume

- anything certified or kernel-checked;
- that no exotic `G_T`-invariant cone exists (only the surgery and engine routes are closed; existence stays at claim (D));
- that balanced surgeries are non-self-dual (only that the engine certifies none);
- the proposal's Bell-circle statements as statements about `G_T`;
- availability of any operation of `G_T`.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-42 v1` and records in its `LOG.md`
whether and how it relies on it.

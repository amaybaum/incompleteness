# HP-countermodels-11 — countermodels → bridge, equivalence, origin, via the coordinator: the tower's closure `G_T` admits no surgery-type invariant cone; a certificate for independent checking

**From** `research/countermodels` (round 5, node C23). **Proposed recipients** `research/bridge` (B10-4/B10-5, B16, B17;
HO-35, HO-36), `research/equivalence` (S6's countercontrol family), `research/origin` (the stage-crossing datum), and the
coordinator for its own independent check of the certificate (owner's requirement (2)). Proposal only; the coordinator
routes. Written 2026-10-11T10:46Z (`date -u`).

## The groups, named exactly
`G_n = ⟨CNOT, X_B, R_B(2π/2ⁿ)⟩` (B10-5's stages, each finitely generated); `G_∞ = ⋃_n G_n` (countable); its closure
`G_T = cl⟨CNOT, X_B, R_B(t) : t ∈ ℝ⟩ = T² ⋊ V4` modulo phase, `T² = {diag(1, uv, u, v)}`, `V4` the permutations
`{e, (23), (01)(23), (01)}` of the computational basis. **Closure step:** a closed cone invariant under `G_∞` is invariant
under `G_T` (H3 gives closedness); for a surgery `K(Z) = K(cl Z)` with `cl Z` `G_T`-invariant. Every statement below is
an invariance statement; none concerns availability.

## Statements, each with its label

1. **Universal orthogonal pair** (C23.1). For `α = h̄₂h₃`, `β = h̄₀h₁`: `⟨h|D(u, v)X_Bh⟩ = β + uvβ̄ + uα + vᾱ`, which vanishes
   for some `(u, v) ∈ T²` for every `h ≠ 0` (five classes by `α, β`). Every `G_T`-orbit of rays contains an orthogonal pair.
   CONDITIONAL ([W] case analysis; identities [X], verified twice by different routes).
2. **Rank-one route closed** (C23.2). No compact `G_T`-invariant rank-one surgery with every `c ∈ (1, 2)` is self-dual
   (C18-1's witness on the orbit of largest `c`; closed-hull form C23-5); at `c = 2` the only admissible orbit is the two Bell
   circles `{|00⟩ + w|11⟩}`, `{|01⟩ + w|10⟩}` and their surgery is stage 4's `K_T` transported by `1 ⊗ H`, not self-dual
   (`tr(y′w′) = −6/625`, re-verified); mixtures with the Bell circles are decided under an overlap condition, OPEN otherwise.
   CONDITIONAL ([W]; [X]; [A] stage 4 Z for the original pair).
3. **Balanced route: the engine certifies nothing** (C23.3). For every seed and every `c ∈ (1, 2)`, the engine
   `selfDual_of_local` (C17.1 [D], HO-30) certifies no balanced rank-two surgery on a `G_T`-orbit: generic seeds
   (`αβ ≠ 0`, `|α| ≠ |β|`) have no partner with zero pairing on the orthogonalizing family (rank 3); the other seeds
   (`|α| = |β|`, or one vanishing coordinate) have a forced partner that first-order tightness defeats; seeds with two
   vanishing coordinates are excluded by H1. CONDITIONAL ([W]; [X] instances at `c = 3/2` and `101/100`).
4. **Node outcome: OBSTRUCTED** (C23.4). No surgery-type cone (rank-one with any weights, or balanced through the engine)
   is invariant under `G_T`, hence none is invariant under all of B10-5's stages at once — HO-36 item 1 extended from
   HO-24's cone to the whole surgery class. An explicit `G_T`-invariant exotic cone stays OPEN; its existence stays
   CONDITIONAL on claim (D) [A] through B7-2 (HO-36 item 2). **Not evidence for the owner's outcome (D)**: no cone is
   produced. Scope: the stage-6 inventory at L, level (i), invariance reading; H1, H3 introduced.
5. **The certificate** (C23.5). `experiments/c23_certificate.json` (sha256
   `d5841161f024006d1f4951d845253508e8813cd8a71e211264175ab80af60d03`): seeds of all five classes with realizing group
   elements; 267 group elements as exact Gaussian-rational matrices; the C18-1 witness with 200 sample defects; the
   transported `K_T` pair with its decompositions; the mixture instance with 16 Bell and 36 orbit samples; partner systems
   and tightness data. `experiments/c23_check.py` reads only the certificate, accepts a group element by its own test
   (unitary, monomial with permutation in `V4`, phases with `φ₀φ₁ = φ₂φ₃`), recomputes every value and checks the identities
   by real-coordinate expansion: 9/9 `CHECK C23-CERTIFICATE-OK`, replay identical.

## Assumption-watch markers proposed
- **"An explicit cone invariant under every stage of the tower is among the surgery cones"** — false (rank-one, and
  engine-certified balanced); an explicit cone for `G_T` needs a sufficiency argument of another kind.
- **"Invariance under a dense subgroup is invariance under its closure"** — holds for closed cones only; the step uses H3
  and is named wherever used.

## What the recipients may not assume
Anything CERTIFIED or kernel-checked; that no exotic `G_T`-invariant cone exists (only the surgery and engine routes are
closed; existence stays at claim (D)); that balanced surgeries are non-self-dual (only that the engine certifies none);
the mixtures outside the overlap condition; availability of any operation of `G_T`.

## Evidence
`NOTES-C23.md` (`ee33e252…`: S0 revised before any run, runs, results, residual); `experiments/c23_torus.py` (`e6a3555e…`) /
`.out` (`e7e58309…`): run 1 6/6 `VERDICT C23-EXACT`, replay identical; `experiments/c23_check.py` (`c13e14e1…`) / `.out`
(`dd7f2aea…`): run 1 9/9, replay identical; the certificate as above; RESULTS C23.1–C23.6; LOG 08:34Z, 10:26Z–10:33Z.
Cross-branch reads: `research/bridge` @ `a34d20b5` (NOTES-B17, NOTES-B10, `b17_tower.py` lines 1–80; definitions only).

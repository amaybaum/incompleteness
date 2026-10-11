# NOTES-B11 — the two-token dictionary as a design module

Node B11 of `research/bridge` (round 3). Base L = `9f9f8257`. The module is
`verification/lean-mathlib/OIBridge/BridgeDictionary.lean` on the disposable branch `dev-bridge/r3-dict`, cut from
`research/bridge`. Its verbatim copy is `research/bridge/lean/BridgeDictionary.lean`. The round-2 draft
(B9-5, `dev-bridge/b11-lemma` @ bbbefb72) stays in history. Evidence levels: [K] kernel at L; [D] design module
built in CI; [X] exact computation (`experiments/b11_preflight.py`); [W] written here.

## S0. Success criterion and predictions (written 2026-10-11T00:28:49Z, before the preflight run and the dispatch)

**Success criterion (round-3 directive).**
- Apply NOTES-B9 §4's fix to `dict_tens`.
- Formalize (D2): `dict (cnot ω) = CNOT · dict ω · CNOT`, and the intertwining of `actT (rotZ c s)` and
  `actC (rotZ c s)` with `Ad(1⊗U)` and `Ad(U⊗1)`, for the kernel's rotation about the third axis. The kernel has no
  declaration named `rotZ`. Its rotation is `rotLin t` (KInfFoundations.lean:386, through `rotFun` :351), so the
  module defines `rotZ c s` and proves `rotZ (cos t) (sin t) = rotLin t`.
- One dispatch for the build. If it fails, record exactly where, and spend a second dispatch only if the fix is
  certain.
- **Gem classification.** At most ELABORATING: it formalizes B9's [X] identities. It is NEW only if the formalization
  exposes a convention error in them.

**Design decisions.**
- No local Lean toolchain: the proxy denies Mathlib's cache host (`lakecache.blob.core.windows.net`, a 403 logged at
  00:01:10Z), and the disk is shared.
- So every Mathlib name used is checked against the pinned sources: Mathlib `v4.33.0`, read through
  raw.githubusercontent.com.
- Every Lean statement is checked first by an exact preflight under the kernel's conventions (`b11_preflight.py`).
- Proofs isolate the unit-circle hypothesis in four 2×2 lemmas. The pair-level identities are reduced to them by
  Mathlib's Kronecker algebra (`mul_kronecker_mul`, `conjTranspose_kronecker`, as in AncillaInterference.lean:123
  and ClosureObstruction.lean:282 at L) and closed by `module`.
- `dict_cnot` is entrywise: 16 entries, sums expanded by `simp only`, values by `simp +decide` (the kernel's own
  pattern for `sgn`/`pc`/`pt`, CompositeDimension.lean `sgn_mul_sgn`).

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | every statement of the planned module is true under the kernel's conventions: (D1) product law; (D2) gate; the four 2×2 phase identities (two of them need `c² + s² = 1`, two do not); the two generic conjugation formulas; the `homMap` entries of `rotZ` and `nflip`; the four intertwinings (`rotZ` and `nflip`, both tokens); unitarity of the phase on the circle; the countercontrol at `(c, s) = (0, 0)` | `b11_preflight.py` F1–F10 |
| S0-2 | the CI build of the module succeeds (Build step green; every `#print axioms` line of the module on `[propext, Classical.choice, Quot.sound]`; `lean-axioms` PASS) | dispatch, job log |
| S0-3 | if the build fails, the most likely failure points are, in order: `dict_cnot` (simp normal form or heartbeats); the `linear_combination` closers of the 2×2 lemmas; the `module` steps | job log |

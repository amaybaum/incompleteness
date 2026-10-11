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

**S0 outcome.**
- S0-1 held: `b11_preflight.py` run 1 (00:29:59Z) gave 10/10 PASS, VERDICT B11-PREFLIGHT-OK; the replay is
  byte-identical.
- S0-2 held: the build succeeded on the first dispatch (§2).
- S0-3 did not arise.

## 1. What the module states

`lean/BridgeDictionary.lean` (sha256 48fc4a7e…; dev blob fece97f4). The section numbers are those of the module.

| declaration | content |
|---|---|
| `pauli`, `tokMat`, `dict` | `σ₀ … σ₃`; `tokMat v = ½ Σ v_μ σ_μ`; `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν`, in the kernel's `tensorOf` |
| `tensorOf_eq_kron` | `tensorOf A B = A ⊗ₖ B` (rfl), for Mathlib's Kronecker algebra |
| `dict_tens`, `dict_prodState` | **(D1)**, the product law. NOTES-B9 §4's fix: expand the sums with `Fin.sum_univ_four`, then `ring` |
| `projZero`, `projOne`, `cnotMat`, `dict_cnot` | **(D2), the gate**: `dict (cnot ω) = cnotMat * dict ω * cnotMat`, `cnotMat = |0⟩⟨0| ⊗ 1 + |1⟩⟨1| ⊗ X`, entrywise |
| `rotZ`, `rotZ_cos_sin` | the rotation about the third axis by `(c, s)`; `rotZ (cos t) (sin t) = rotLin t`, the kernel's flow (KInfFoundations.lean:386) |
| `homMap_rotZ_*`, `homMap_nflip_*'` | the homogenized entries at `Fin 4` literals (rfl, or the kernel's `homMap_nflip_*`) |
| `zPhase`, `zPhaseD`, `zPhase_conjTranspose` | `diag(1, c + is)` and its adjoint |
| `zPhase_pauli0` … `zPhase_pauli3` | the one-token identities. `σ₁ ↦ c σ₁ + s σ₂` and `σ₂ ↦ −s σ₁ + c σ₂` hold unconditionally; `σ₀` and `σ₃` are fixed on the circle `c² + s² = 1` |
| `x_pauli0` … `x_pauli3` | `X σ_k X = (1, 1, −1, −1) σ_k` |
| `conj_dict_right`, `conj_dict_left` | the generic term-by-term conjugation formulas for `Ad(1 ⊗ U)` and `Ad(U ⊗ 1)` |
| `dict_actT_rotZ`, `dict_actC_rotZ` | **(D2), the monomial images**: `dict (actT (rotZ c s) ω) = Ad(1 ⊗ zPhase c s)(dict ω)` and `dict (actC (rotZ c s) ω) = Ad(zPhase c s ⊗ 1)(dict ω)`, on the circle |
| `dict_actT_nflip`, `dict_actC_nflip` | **(D2), the NOT** on either token: `Ad(1 ⊗ X)`, `Ad(X ⊗ 1)` |
| `monomial_extension_admissible`, `TransferClause` | the certified `substratumClass_contextStable` (StructuralClosure.lean:261) at the pair carrier; the clause (T) as a definition |
| `zPhase_monomial`, `zPhase_unitary`, `transfer_phase` | the phase is monomial (kernel `monomial_diagonal`) and unitary on the circle. **Pull-back of (T)**: on a cone satisfying `TransferClause substratumClass`, every `actT (rotZ c s) ω` with `ω ∈ K` and `c² + s² = 1` has the dictionary image of a member of `K` |
| `dict_actT_rotZ_345`, `zPhase_pauli0_counter` | positive control (the circle hypothesis at `(3/5, 4/5)`); countercontrol (off the circle, at `(0, 0)`, the phase does not fix `σ₀`, so the hypothesis is load-bearing) |

## 2. CI record (dispatch 1 of 3)

- **Run.** 38099134414: `verify.yml`, `workflow_dispatch` on `dev-bridge/r3-dict` @ 3d554e7e, queued 00:38:50Z. The dev
  commit's parent is research/bridge 7fd01094. It adds the module and one root import line.
- **Mathlib bridge job 114351216052.**
  - **Build: success**, 00:39:40–00:42:00Z: "⚠ [3642/3644] Built OIBridge.BridgeDictionary (23s)", warnings only,
    then "Build completed successfully (3644 jobs)".
  - **`#print axioms`: 20/20 on `[propext, Classical.choice, Quot.sound]`.** The 20 declarations are `dict_tens`,
    `dict_prodState`, `dict_cnot`, `rotZ_cos_sin`, `zPhase_conjTranspose`, `zPhase_pauli0` … `zPhase_pauli3`,
    `conj_dict_right`, `conj_dict_left`, `dict_actT_rotZ`, `dict_actC_rotZ`, `dict_actT_nflip`, `dict_actC_nflip`,
    `monomial_extension_admissible`, `zPhase_unitary`, `transfer_phase`, `dict_actT_rotZ_345` and
    `zPhase_pauli0_counter`.
  - **Release gate.** `lean-axioms` **PASS** ("OK (5880 named result(s) reported, no sorr…"). It fails only on
    `claims`, `duplicate` and `lean-manuscript` (1 problem: no census disposition for a design module), red by
    construction on research branches.
- **Not touched.** No job of the run was cancelled. The numerical-probe shards were still running when the bridge job
  was read; they do not bear on B11.
- **The warnings.**
  - Unused simp arguments.
  - "Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice".
  - "This tactic is never executed" for the fallback branches. These are the second alternatives of `rotZ`'s
    linearity proofs, the `simp` fallbacks of `rotZ_cos_sin` and of every `homMap_*` lemma (`rfl` or the kernel lemma
    closed them), the `first | rfl | ring1` tails of `x_pauli*`, the `show IsMonomial` fallback, and the later
    `linear_combination` certificates.
- **Which branches ran.**
  - In `zPhase_pauli1` every `linear_combination` alternative is reported unexecuted: `ring1` closed all entries, and
    no `I²` arises (as analysed before the dispatch).
  - In `zPhase_pauli0`, `zPhase_pauli3` and `zPhase_unitary`, only the first one or two alternatives
    (`ring1`, `hc − s²·I_sq`, and for `σ₃` also `−hc + s²·I_sq`) can have run.
  - In `zPhase_pauli2`, only `ring1` and `s·I_sq` can have run. These are the certificates predicted in the design.

## 3. Reading and verdict

- **(D1) and (D2) are design statements built in CI ([D]).** This supersedes B9-5's OPEN for the formalization; B9-5
  is not edited.
- **B9-1's exact [X] facts are now also kernel-checkable design statements**: the dictionary's product law, the gate,
  and the monomial images on both tokens.
- **The pull-back of (T)** to the phase rotations (`transfer_phase`) is formal modulo the dictionary's injectivity,
  which the module does not prove.
- **Gem classification: ELABORATING**, as predicted. This is a formalization. The preflight [X] and the build agree,
  and no convention error in B9's [X] statements was exposed.
- **Not claimed.**
  - Injectivity of `dict`.
  - That `TransferClause` holds for any pair cone. It is a definition here; for the monomial class it is (b) for the
    monomial images (B9-1), and B10 locates its H-level premise.
  - Any census disposition or certification. The module is [D], CONJECTURE until a governed round.

## 4. Run completion (appended 2026-10-11T01:28:50Z)

Run 38099134414 completed at 01:03:02Z (head 3d554e7e): 33 jobs, 32 success and 1 failure. The failure is the
Mathlib bridge job 114351216052, through its release gate (red by construction on a research branch). "Lean kernel
check" and every numerical-probe shard succeeded. No job was cancelled.

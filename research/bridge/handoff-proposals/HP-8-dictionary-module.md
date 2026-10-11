# HP-8 — the two-token dictionary as a design module built in CI

From `research/bridge`, node B11 (round 3). Proposed for the equivalence thread (the K2 schema's lemmas 1–2, any
formalization of the dictionary) and the countermodels thread (conjugation formulas for pair-cone checks). The
coordinator routes.

## Statements and labels

1. **The dictionary, (D1) and (D2)** (B11-1). The module `BridgeDictionary.lean` defines
   `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν` on the kernel's `tensorOf` (MonoidalCompletion.lean) and proves:
   - (D1) the product law `dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` (`dict_tens`, `dict_prodState`);
   - (D2) the gate `dict (cnot ω) = cnotMat * dict ω * cnotMat`, `cnotMat = |0⟩⟨0| ⊗ 1 + |1⟩⟨1| ⊗ X` (`dict_cnot`);
   - the monomial images on the unit circle `c² + s² = 1`:
     - `dict (actT (rotZ c s) ω) = Ad(1 ⊗ diag(1, c + is))(dict ω)`;
     - `dict (actC (rotZ c s) ω) = Ad(diag(1, c + is) ⊗ 1)(dict ω)`;
   - the NOT on either token, `Ad(1 ⊗ X)` and `Ad(X ⊗ 1)`;
   - `rotZ (cos t) (sin t) = rotLin t`, the kernel's flow (KInfFoundations.lean:386).

   Controls: positive at `(3/5, 4/5)`; countercontrol at `(0, 0)`, where the circle hypothesis is load-bearing.
   Label: CONJECTURE ([D]: built in CI; not certified; no census disposition).
2. **The pull-back of (T) to the phase circle** (B11-2, `transfer_phase`). On a pair cone `K` with
   `TransferClause substratumClass K`, every `actT (rotZ c s) ω` with `ω ∈ K` and `c² + s² = 1` has the dictionary
   image of a member of `K`.
   Label: CONJECTURE ([D], same run). Injectivity of `dict` is OPEN in the module (a standard Pauli-basis fact [W]).

## Evidence

| item | pointer |
|---|---|
| module | `research/bridge/lean/BridgeDictionary.lean`, sha256 `48fc4a7e…`; dev blob `fece97f4` |
| CI | `dev-bridge/r3-dict` @ `3d554e7e`, run 38099134414, Mathlib bridge job 114351216052: Build success ("Built OIBridge.BridgeDictionary (23s)"); 20/20 `#print axioms` on `[propext, Classical.choice, Quot.sound]`; `lean-axioms` PASS (5880 named results, no sorry); gate red only on `claims`, `duplicate`, `lean-manuscript` (research branch, by construction) |
| preflight | `experiments/b11_preflight.py`, 10/10, VERDICT B11-PREFLIGHT-OK, replay byte-identical |
| notes, results | `NOTES-B11.md` §1–§3; `RESULTS.md` rows B11-1, B11-2 |

## What the recipient may assume

Items 1–2 at their labels: (D1) and (D2) as Lean statements that build against Mathlib `v4.33.0` and the kernel at
L, with the standard axiom footprint. The module's code builds unchanged. A governed round adopting it would still
owe the census disposition the release gate's `lean-manuscript` step requires (§A.35). The dev branch adds one root
import line, a deviation recorded in the thread's LOG.

## What the recipient may not assume

- certification, or any census disposition: the module is a design module on a disposable branch;
- injectivity of `dict`;
- that `TransferClause` holds for any pair cone: it is a definition. For the monomial class it is (b) for the
  monomial images, and its H-level premise is H-T (HP-7);
- that the dictionary is a premise about any cone: it is a comparison and construction tool.

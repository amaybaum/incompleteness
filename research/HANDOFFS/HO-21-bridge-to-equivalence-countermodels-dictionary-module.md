# HO-21 (v1) — bridge → equivalence, countermodels: the two-token dictionary module built in CI — (D1) the product law, (D2) the gate and the monomial images, `transfer_phase`

**From** `research/bridge` (round 3, node B11). **To** `research/equivalence` (the K2 schema's lemmas 1–2, any
formalization of the dictionary; the convergence with HO-18) and `research/countermodels` (conjugation formulas for
pair-cone checks). Written by the coordinator from the source thread's committed record; version 1, 2026-10-11.
Answers HO-6 and HO-12 item 1 from the bridge side; to be read with HO-18, which carries the equivalence thread's
module on the same definitions.

## Statements and labels

1. **The dictionary, (D1) and (D2)** (B11-1). `BridgeDictionary.lean` defines `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν` on the
   kernel's `tensorOf` (MonoidalCompletion.lean) and proves:
   - (D1) the product law `dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` (`dict_tens`, `dict_prodState`);
   - (D2) the gate `dict (cnot ω) = cnotMat * dict ω * cnotMat`, `cnotMat = |0⟩⟨0| ⊗ 1 + |1⟩⟨1| ⊗ X` (`dict_cnot`);
   - the monomial images on the unit circle `c² + s² = 1`: `dict (actT (rotZ c s) ω) = Ad(1 ⊗ diag(1, c + is))(dict ω)`
     and `dict (actC (rotZ c s) ω) = Ad(diag(1, c + is) ⊗ 1)(dict ω)`;
   - the NOT on either token, `Ad(1 ⊗ X)` and `Ad(X ⊗ 1)`;
   - `rotZ (cos t) (sin t) = rotLin t`, the kernel's flow (KInfFoundations.lean:386).

   Controls: positive at `(3/5, 4/5)`; countercontrol at `(0, 0)`, where the circle hypothesis is load-bearing. Label:
   CONJECTURE ([D]: built in CI; not certified; no census disposition).
2. **The pull-back of (T) to the phase circle** (B11-2, `transfer_phase`). On a pair cone `K` with
   `TransferClause substratumClass K`, every `actT (rotZ c s) ω` with `ω ∈ K` and `c² + s² = 1` has the dictionary
   image of a member of `K`. Label: CONJECTURE ([D], same run). **Injectivity of `dict` is OPEN in this module** (a
   standard Pauli-basis fact [W]); it is [D] in the equivalence thread's `EqvK2Schema` on the same definitions (HO-18
   items 1 and 5), so the two modules together close it at the design level.
3. **The rendering of the `dict_tens` proof** (coordinator, from HO-18 item 4). This module renders the expansion in
   two stages (`simp only [dict, tokMat, tens_apply, Matrix.sum_apply, …]`, then `simp only [Fin.sum_univ_four]`, then
   `ring`) and builds; the one-list rendering fails in Lean v4.33.0 / Mathlib v4.33.0 and needs `Matrix.add_apply`.
   Either rendering is usable.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `7abe4da4` (round-3 commits `0ccc1bef` … `7abe4da4`) |
| proposal | `research/bridge/handoff-proposals/HP-8-dictionary-module.md`, sha256 `2a7f71c85f2c0ed37b2768ed5a16f1f1144615b50ab7e3121e5e6286bae27f3f` |
| results, notes | `research/bridge/RESULTS.md` sha256 `07b89737cb13ac2efe04f58b8af834ac968c5c71433e16439af31204600055c0` (rows B11-1, B11-2); `NOTES-B11.md` `2c2a0d05952a26293adbc1f0adc9560a0a1f70e0b04955d6e17d8322cbd5ad9d` (§1–§3) |
| script, output | `experiments/b11_preflight.py` `237b70117811ca9e16d60075a6233f78f94e426f3f7cda619a09653aad22c899` / `.out` `b50fd38bd92a2bd2968ad530f355b4cc275e154adabbcdf8cbfa8ff38bcc7147` (10/10, VERDICT B11-PREFLIGHT-OK; replayed byte-identically) |
| design module | `research/bridge/lean/BridgeDictionary.lean` sha256 `48fc4a7e5b1f27d433ffb38cfd89f69a74544a803605465b2d0bd8b7a932156d` (dev blob `fece97f4`; the round-2 draft kept beside it, `BridgeDictionary.round2-draft.lean` `e4b60411ebbb58660c227b04d3abe4698ee3bcd9589962a0c718f3e38a5e74e8`); `dev-bridge/r3-dict` @ `3d554e7e` (run 38099134414, Mathlib bridge job 114351216052: Build success, `Built OIBridge.BridgeDictionary (23s)`, 20/20 prints on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` OK 5880 no sorry; gate red on `claims` (7), `duplicate` (104), `lean-manuscript` (1) — the dev branch is cut from `research/bridge`, which carries `research/archive/`) — `research/AUDITS/2026-10-11-round3/CI-RUNS-R3.md` |
| coordinator audit | `indep_checkB3.py` run 2 4/4 — X1, against the kernel's own definitions transcribed from L and independently of the module: the kernel's `cnotFun` (`sgn`, `pc`, `pt`, CompositeDimension.lean:741–:758) equals `Ad(CNOT)` through the dictionary on all 16 basis tables and is an involution; `actT (rotZ c s)` and `actC (rotZ c s)` (`homMap` :112, `actT` :198, `actC` :201) equal `Ad(1 ⊗ diag(1, c + is))` and `Ad(diag ⊗ 1)` at `(3/5, 4/5)`, `(−5/13, 12/13)` and symbolically on `c² + s² = 1`; `nflip = diag(1, −1, −1)` (:797) gives `Ad(1 ⊗ X)` and `Ad(X ⊗ 1)`; at `(0, 0)` the phase conjugation does not fix `σ₀`; `pauliW(prodState x y) = ρ(x) ⊗ ρ(y)`; the module's statements read; the job log read line by line (20/20) — `research/AUDITS/2026-10-11-round3/AUDIT-BRIDGE-R3.md` |

## What the receiving threads may assume

Items 1–3 at their labels: (D1) and (D2) as Lean statements that build against Mathlib `v4.33.0` and the kernel at
L, with the standard axiom footprint; the module's code builds unchanged. **Equivalence:** the gate (D2), the monomial
images and `transfer_phase` as the statements its own module lacks (HO-18 item 5); a governed round adopting either
module would still owe the census disposition the release gate's `lean-manuscript` step requires (§A.35).
**Countermodels:** the conjugation formulas — `Ad(CNOT)`, `Ad(1 ⊗ diag(1, c + is))`, `Ad(diag(1, c + is) ⊗ 1)`,
`Ad(1 ⊗ X)`, `Ad(X ⊗ 1)` — as exact identities between the kernel's table actions and matrix conjugations, verified
by the coordinator against the kernel's definitions at L.

## What they may not assume

- certification, or any census disposition: the module is a design module on a disposable branch; the dev branch adds
  one root import line, a deviation recorded in the thread's LOG;
- injectivity of `dict` from this module (OPEN here; [D] in `EqvK2Schema`);
- that `TransferClause` holds for any pair cone: it is a definition; for the monomial class it is (b) for the monomial
  images, and its H-level premise is H-T (HO-20);
- that the dictionary is a premise about any cone: it is a comparison and construction tool;
- anything beyond two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-21 v1` and records in its `LOG.md`
whether and how it relies on it.

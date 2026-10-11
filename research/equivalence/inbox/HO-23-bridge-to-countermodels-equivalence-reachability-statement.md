# HO-23 (v1) — bridge → countermodels, equivalence: the reachability theorem B7-1 as the formal statements `ReachUnitary` and `ReachAnti`, with the finite case built in CI

**From** `research/bridge` (round 3, node B13). **To** `research/countermodels` (B3.C and the composite-cone
classification; HO-16's cone side) and `research/equivalence` (the reachability lemma of the K2 schema, `ReachPure`).
Written by the coordinator from the source thread's committed record; version 1, 2026-10-11.

## Statements and labels

1. **The statements** (B13-1). `BridgeReach.lean` defines two propositions in `U(4)`, which loses nothing against
   `PU(4)`:
   - `ReachUnitary`: every closed subgroup `H` of `Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ` whose identity component (taken
     in the subgroup) is commutative has some `v ≠ 0` that no `h ∈ H` carries to a product `a ⊗ b`;
   - `ReachAnti`: the same for `H ∪ Hκ`, `κ = K ∘ conj`, under the two conditions that make it a group,
     `K conj(h) K* ∈ H` and `K conj(K) ∈ H`.

   Together they are B7-1 (NOTES-B7). Label: the statements are definitions; B7-1 itself remains CONJECTURE (complete
   written proof, not kernel-checked) for subgroups of positive dimension.
2. **The finite case** (B13-1). For every finite subgroup `H` and every `K`, the conclusions hold, with no hypothesis on
   the identity component or on `K` (`reachUnitary_finite`, `reachAnti_finite`), so each statement reduces to its
   infinite closed subgroups (`reachUnitary_of_infinite`, `reachAnti_of_infinite`). The proof is an avoidance lemma
   (`exists_avoid`): finitely many functions, each nonzero somewhere and quadratic along lines, have a common non-root.
   Label: CONJECTURE ([D]: built in CI; not certified; no census disposition).
3. **Propagation to B7-4** (B13-2). For a fixed finite pair substratum, the reachability step of B7-4 is the finite
   case, now [D]; the cone step still rests on claim (D) [A], and B7-4's label is unchanged. Label: CONDITIONAL (on claim
   (D) [A]) for the fixed-finite case. Read with HO-24 item 6: for finite groups of unitary conjugations containing
   `cnot`, the cone step is now supplied by an explicit surgery (Theorem S′ [W]) rather than claim (D).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `7abe4da4` (round-3 commits `0ccc1bef` … `7abe4da4`) |
| proposal | `research/bridge/handoff-proposals/HP-10-reachability-statement.md`, sha256 `8c9e3f1a8e7b509e2f33fb18961e86fe01b9f4a37b818835f538b0c2b499b1f0` |
| results, notes | `research/bridge/RESULTS.md` sha256 `07b89737cb13ac2efe04f58b8af834ac968c5c71433e16439af31204600055c0` (rows B13-1, B13-2); `NOTES-B13.md` `177d33cd2df1efc43f50fc3be4f8f0f49feed330b9807c24674e438c045789f4` |
| script, output | `experiments/b13_preflight.py` `9b293e4550efdb17f68e3b489b5898af379c3f360be2a8aaf281af1e6e5dc6eb` / `.out` `06370a7c7f879c19efa1916342f28ae6c906576e78f9fbd7f229abbff93cdbd1` (7/7, VERDICT B13-PREFLIGHT-OK; replayed byte-identically) |
| design module | `research/bridge/lean/BridgeReach.lean` sha256 `a6e055e4b594b6523df53b03e8c69b71fa23fc8348242920cc56df4dcde51831` (dev blob `7a279393`); `dev-bridge/r3-reach` @ `747bcf94` (run 38101591388, Mathlib bridge job 114358450003: Build success, `Built OIBridge.BridgeReach (1.7s)`, 21/21 prints on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` OK 5881 no sorry; gate red on `claims` (7), `duplicate` (104), `lean-manuscript` (1) by construction of the dev branch) — `research/AUDITS/2026-10-11-round3/CI-RUNS-R3.md` |
| coordinator audit | `indep_checkB3.py` run 2 4/4 — X4 (`prodDet(1,2,3,5) = −1` and `−7` after CNOT; the polarisation identity; the three-root lemma on an instance; a common non-root on five points of a line for two unitaries); the module's two propositions and the finite-case theorems read (the identity component taken in the subgroup; the two coset conditions; no hypothesis on the identity component or `K` in the finite case); the job log read line by line (21/21) — `research/AUDITS/2026-10-11-round3/AUDIT-BRIDGE-R3.md` |

## What the receiving threads may assume

Items 1–3 at their labels. `ReachUnitary` and `ReachAnti` can be taken as the formal target for B7-1 and, through
claim (D), for B3.C (HO-10; HO-16 item 3); their finite case is a design statement with the standard axiom footprint.
**Countermodels:** what remains open on the reachability side is the tori and their finite extensions, where HO-16's
residual region lies (HO-25 item 4 carries the cone side of that region). **Equivalence:** the finite case as the
reachability input for any finite-group instance of the K2 schema's `ReachPure`; the infinite case stays [W].

## What they may not assume

- B7-1 for subgroups of positive dimension: the module states it and does not prove it;
- certification, or any census disposition;
- that the hypothesis `IdCompComm` is formally shown non-vacuous: that `U(4)` itself is excluded is argued, not
  formalized;
- the identification of table-level pair groups on `W 3` with groups of conjugations, beyond the dictionary statements
  [D] of HO-18 and HO-21;
- anything beyond two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-23 v1` and records in its `LOG.md`
whether and how it relies on it.

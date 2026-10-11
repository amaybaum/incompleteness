# HP-10 — the reachability theorem B7-1 as a formal statement, with its finite case built in CI

From `research/bridge`, node B13 (round 3). Proposed for the countermodels thread (B3.C and the composite-cone
classification, HO-16's cone side) and the equivalence thread (the reachability lemma of the K2 schema). The
coordinator routes.

## Statements and labels

1. **The statement** (B13-1). `BridgeReach.lean` defines two propositions.
   - `ReachUnitary`: every closed subgroup `H` of `Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ` whose identity component
     is commutative has some `v ≠ 0` that no `h ∈ H` carries to a product `a ⊗ b`.
   - `ReachAnti`: the same for `H ∪ Hκ`, `κ = K ∘ conj`, under the two conditions that make it a group,
     `K conj(h) K* ∈ H` and `K conj(K) ∈ H`.

   Together they are B7-1 (NOTES-B7) in `U(4)`, which loses nothing against `PU(4)`. Label: the statements are
   definitions. B7-1 itself remains CONJECTURE (complete written proof, not kernel-checked) for subgroups of positive
   dimension.
2. **The finite case** (B13-1). For every finite subgroup `H` and every `K`, the conclusions hold, with no hypothesis
   on the identity component or on `K` (`reachUnitary_finite`, `reachAnti_finite`). So each statement reduces to its
   infinite closed subgroups (`reachUnitary_of_infinite`, `reachAnti_of_infinite`). The proof is an avoidance lemma
   (`exists_avoid`): finitely many functions, each nonzero somewhere and quadratic along lines, have a common
   non-root. Label: CONJECTURE ([D]: built in CI; not certified; no census disposition).
3. **Propagation to B7-4** (B13-2). For a fixed finite pair substratum, the reachability step of B7-4 is the finite
   case. That step is now [D]; the cone step still rests on claim (D) [A], and B7-4's label is unchanged. Label:
   CONDITIONAL (on claim (D) [A]) for the fixed-finite case.

## Evidence

| item | pointer |
|---|---|
| module | `research/bridge/lean/BridgeReach.lean`, sha256 `a6e055e4…`; dev blob `7a279393` |
| CI | `dev-bridge/r3-reach` @ `747bcf94`, run 38101591388, Mathlib bridge job 114358450003: Build success ("Built OIBridge.BridgeReach (1.7s)"); 21/21 `#print axioms` on `[propext, Classical.choice, Quot.sound]`; `lean-axioms` PASS (5881 named results, no sorry); gate red only on `claims`, `duplicate`, `lean-manuscript` (research branch, by construction) |
| preflight | `experiments/b13_preflight.py`, 7/7, VERDICT B13-PREFLIGHT-OK, replay byte-identical |
| notes, results | `NOTES-B13.md`; `RESULTS.md` rows B13-1, B13-2 |

## What the recipient may assume

Items 1–3 at their labels. `ReachUnitary` and `ReachAnti` can be taken as the formal target for B7-1, and through
claim (D) for B3.C (HO-10; HO-16 item 3). Their finite case is a design statement with the standard axiom footprint.
What remains open is the tori and their finite extensions, where HO-16's residual region lies.

## What the recipient may not assume

- B7-1 for subgroups of positive dimension: the module states it and does not prove it;
- certification, or any census disposition;
- that the hypothesis `IdCompComm` is formally shown non-vacuous: that `U(4)` itself is excluded is argued, not
  formalized;
- the identification of table-level pair groups on `W 3` with groups of conjugations, beyond B11's dictionary
  statements [D];
- anything beyond two tokens.

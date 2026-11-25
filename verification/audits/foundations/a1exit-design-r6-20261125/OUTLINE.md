# Design r6 outline and requirement identifiers (drafting aid, not adopted)

r6 is one self-contained design. It supersedes v6.0e, r4 and r5 on adoption (OD-3), and incorporates
nothing by reference. Each requirement has an id `R6.<SEC>.<n>`. A mapping row names the section code
and, after numbering, the requirement id. Expected control results are stated in the authoritative
expectation file, not in r6's prose (OD-1, OD-2). r6 states, for each requirement, the ids of the
controls that test it.

| Code | r6 section | Draws on |
|---|---|---|
| STAT | 0. Status, authority, scope, goal link; what r6 supersedes | v6.0e Status; r5 Status; OD-3; MC-6 |
| NOTE | 1. Notation and symbols (E, H, P, T1', W, X, C, L, M, F and so on; collisions resolved) | v6.0e Notation; v2 notation; r5 A.2 (renamed per OD-31) |
| PUR | 2. Purpose, non-goals, residual limits | v6.0e 1; v1 and v2 goal and non-goals |
| PIPE | 3. Pipeline stages, subject kinds, operations, ledger fields | v6.0e 2; v1 3.1-3.3 (segments, chain, default segmentation); v2 ops |
| ANCH | 4. Pin, anchors, translation and relocation, file conformance, content search | v1 4.1-4.4, 4.6-4.7 (as restated or withdrawn); v6.0e 3.4, 4, 5 boundary cases; VD-2, VD-3 |
| HP | 5. Historical provenance obligation (E..H): merges, regions, adjudication, resumed tracking | v6.0e 3 |
| CTX | 6. Context rule and indicators | v6.0e 4 |
| OUT | 7. Outcomes, exit codes, precedence, result schema (complete field list) | v6.0e 5; OD-24; v1/v2 schema chain |
| SPLIT | 8. Sentence splitter version 2 (restated from v5.2) | OD-23 |
| PROF | 9. Scan profiles (including register and infinity; P's per-edit unit) | v6.0e 6.1 |
| RULE | 10. Rule schema, rule lint, fingerprints, residual testing | v6.0e 6.2; v2 rule lint (OD-25) |
| REC | 11. Records, review records, record lint, admission, execution identity, object integrity | v6.0e 6.3; r5 B.3 (record_id); OD-4, OD-28, OD-29 |
| DENY | 12. Rule records: deny, allow, resid (plan records; tool tests the mechanism) | v6.0e 6.4-6.6; OD-8 |
| DELEG | 13. Delegation contract and classes | v6.0e 7 |
| HIT | 14. Hit classification and review load | v6.0e 8; OD-16 |
| CLASS | 15. FAIL and REVIEW conditions (complete class list with conditions) | v6.0e 9; OD-15; MC-14, MC-17 |
| GATE | 16. Verification architecture: expectation file, runner evidence, independent gate, correspondence check, NOT RUN rule | OD-1, OD-2; Q1; VD-1, VD-10, VD-11 |
| CTRL | 17. Control catalogue: one row per control id (id, requirement ids it tests, runner, predicate kind); expected results in the expectation file | v6.0e 10, 13.2, 16.5; v1 8.1-8.2; v2 9.1, 13.4; r5 A.9, A.10, B.4; OD-17 to OD-22 |
| PLAN | 18. Mapping of P's mandatory checks to tool commands; transferred plan-amendment obligations (blockers) | v6.0e 11; OD-30; ME-1, ME-2; Q5 |
| PLACE | 19. Placement, governance, landing paths, authority constants | v6.0e 12; OD-5, OD-6, OD-7, OD-26 |
| TREE | 20. Four trees: roles, invariants, landing composition, own-diff rule | v6.0e 13.1; v2 13.1-13.2; OD-9 to OD-13 |
| RDIR | 21. The plan's record directory on M (r5 change 1) | r5 A |
| ITEM2 | 22. Item-2 records (r5 change 2) | r5 B |
| RECON | 23. Reconciliation records; re-resolving M; sequencing safeguard (three-valued) | v6.0e 13.3, 13.4; OD-18; Q2 |
| CORE | 24. Engine, purity scope (Z9), generality | v6.0e 16.1 |
| CFG | 25. Configuration record, widening, admission | v6.0e 16.2; OD-27 |
| ADAPT | 26. Adapter interfaces (replay equalities named; read_entries dropped) | v6.0e 16.3; v1 3.2; OD-16, OD-19c |
| A1CFG | 27. A1 as the first configuration | v6.0e 16.4 |
| SYN | 28. Synthetic configuration and git fixtures | v6.0e 16.5; r5 git fixture |
| VALID | 29. Fail-closed configuration validation | v6.0e 16.6; OD-4, OD-27 |
| REPRO | 30. Reproducibility and the double run | v6.0e 16.7 |
| EVID | 31. Evidence and figures: acceptance references (reproduced on main) versus historical measurements | v6.0e 0.3, 14; ME-3, ME-4 |
| OBL | 32. Outstanding obligations: transferred requirements, each a named blocker on the execution it gates | Q5; ME-1, ME-2, ME-8; OD-18 release condition |
| RET | 33. Retired identifiers and mechanisms, each with the disposition of its underlying requirement | OD-15, OD-16, OD-19, OD-20, OD-25; Q3, Q4 |
| MIG | 34. Identifier migration index (old id to new id; nothing reused) | OD-31 |
| HIST | Appendix: historical (status history, review history, derivation figures), never normative | v6.0e Status history, 0.1, 0.2, 14; v1/v2 history items |

Disposition values for each inventory item:
- `retained`: restated in r6 with the same meaning.
- `translated`: restated in r6's vocabulary, classes or exit codes; the translation is stated.
- `merged`: combined with another item into one r6 requirement.
- `superseded`: replaced by a named r6 requirement that differs.
- `retired`: no longer a requirement, with the disposition of the underlying verification requirement
  stated as one of:
  - `preserved-at <id or code>`: the property is still verified elsewhere;
  - `obsolete: <reason>`: the property no longer exists;
  - `withdrawal-needs-decision`: residual decision (Q3, Q4).
- `transferred`: moved to the plan amendment as an outstanding obligation (`OBL`); not discharged.
- `historical`: kept in the appendix as history, not a requirement.
- `unresolved`: residual owner decision.

# A9. Schema of the gate-outcome table

**Governs:** base lines 192–194 ("a gate-outcome table in a stated schema").

**Addition.** The table is the file `gate-table.json` in the round's record directory: one JSON object with the keys
`schema` (`"k1rdy-gate-table"`), `version` (`1`), `controls`, `rows` and `class_tokens`.

- `controls`: one object per S0 control of §6, with `id`, `gate` (the single gate it ran), `outcome` (`"pass"`,
  `"fail"` or `"undecided"`) and `derivation` (the section of the execution record that decides it).
- `rows`: one object per row, with `candidate` (`"P0"`, `"P1"` or `"P3"`), `member` (`"pi0"`, the cycle's
  lexicographically least state as a 10-character string of `0` and `1` in A2's cell order, or `null`), `branch`
  (`"B-pl"`, `"B-eq"` or `"B-ct"`), `gates` (an object with keys `G1` to `G7`, each `"pass"`, a token, or `"not-reached"`),
  `w_rule` (the rule that fixes `W`, line 268) and `w_inputs` (its listed inputs), `g2` (an object with `a`, `t1` and
  `t2`, each `true` if it flags, and `hsel_content`, the list of functions recorded as H-sel content, line 259),
  `sharp_w` (a list of values of `W`, each a string of `0` and `1` in A2's cell order of `W`'s cells; in B-pl, where `W`
  is trivial, the only value is the empty string `""`), `weak` (an object from each positive-mass `w` to an exact
  rational written `"p/q"`), `nb` (an object from each sharp `w` to `true` or `false`), `w_certified` (`true` or
  `false`, lines 55–56), `usefulness` (for a positive row, the operational-usefulness report of lines 144–147: the
  pairs `σ, σ′` with disjoint readout supports and the pairs that differ in law only; `null` otherwise, line 269),
  `hypotheses` (the list `Λ`, sorted), `ledger` (a string) and `token` (a string from §5.4's table).
- `class_tokens`: an object from each branch to the P1 class token, with A2's fields.

Each token is recomputed from this file by §5.4, A2 and A8. Verdict text quotes tokens read from this file, never from
printed output (`AGENTS.md` §A.44).

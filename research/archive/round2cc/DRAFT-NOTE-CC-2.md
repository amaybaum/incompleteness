# CC-2 draft note (off-repo; 2026-10-03)

Status: DRAFT, held until CC-1's halted record lands (its landing is CC-2's `D`). Nothing pushed.

## What CC-2 is

The same round as CC-1 — the 27 ledger items, the same three dispositions, the same 60 frozen substitutions,
the same deferred set, guardrails and closure steps — plus governance of the two verification surfaces the
release gate reads against the manuscripts, and, as frozen instances, exactly the consequences the 60
substitutions have on them (preregistration §3.2, V-1 … V-5):

| Instance | File | Forced by | Content |
|---|---|---|---|
| V-1 | `verification/coverage/LEDGER.json` | T-A1-1.1 | corollary fingerprint `9330e1f409e986c0` → `f7e912991de09137`; mapping unchanged (GAP) |
| V-2 (two) | same | T-A3-1 | unnamed area-law lemma: id `SM:L-unnamed-332dde89` → `SM:L-unnamed-ff7b7d06`, fingerprint `332dde89a60f07d3` → `ff7b7d068e326e1f` |
| V-3 | same | T-A6-2.1 | entry `SM:T-unnamed-f1d3c661` removed (the Theorem header leaves the census; GAP, no checks, no backlog or unattached row); 130 → 129 entries |
| V-4 | `verification/lean/edge_rigidity_probe.py` | T-A6-1.1 | R7-A6P P5 delimiter `now derived rather than postulated.` → `That the link dynamics is governed by this functional is not derived here.` |
| V-5 | same | T-A6-1.1 | the sub-check's docstring names the old delimiter; reworded |

## Design evidence (measured today, base 0f2687b7)

- CC-1's candidate E run 37143464345 (32 jobs): the only failures were `coverage` (4 findings: the three
  entries above, the moved id counting twice) and `R7-A6P` (delimiter only; every pinned passage present).
  Every other gate step, guard and probe shard passed on the 60-substitution tree.
- Predicted E tree (`wt-cc1` = S1 93bbeb15 + `verification-surface.diff`): `coverage_check: OK (129
  canonical statements, 19 unattached checkers)`; `edge_rigidity_probe: ALL CHECKS PASS`.
- Mutation control: remove the anchoring sentence from SM.md → `FAIL R7-A6P`, `edge_rigidity_probe: FAILURE`;
  restore → ALL PASS. The re-anchored guard discriminates.
- `controls2.py`: SELF-TEST OK (mutation-missing 5, mutation-register 6); `--check D` OK at D; `--check E` OK
  on the predicted E tree (including the census / ledger-count / coverage / delimiter checks of closure step 9).

## Artifacts

- `PREREG-CC-2.md` (generated from CC-1's F preregistration by `gen_prereg2.py`; §3 table verbatim)
- `controls2.py` (generated from CC-1's controls by `gen_controls2.py`)
- `verification-surface.diff` (the V-instances as a diff against S1)

## Placeholders to fill at drafting

- `D-CC-2-PLACEHOLDER` (preregistration "objects", `controls2.py` `D_COMMIT`) = CC-1's halted landing on main.
- Before F: re-measure `--check D` at the real `D` (every execution path should be byte-identical to
  0f2687b7's, since the halted landing changed record paths only), and rerun the coverage check and probe at `D`.

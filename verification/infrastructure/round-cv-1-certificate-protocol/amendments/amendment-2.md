# CV-1, Amendment 2: two historical controls read the live tree instead of CV-1's historical subject

Append-only. The preregistration is not edited, and nothing in this amendment changes `B_CV1`,
`E_CV1`, `L_CV1`, `A_CV1`, the certificate blob at `E`, the committed census, the result note, or
any adjudicated verdict. It records two defects in CV-1's own guard logic, freezes their exact
current text, and freezes the replacement rule. It is a guard-logic amendment, not a research
amendment: no measurement is re-taken and no census is re-run.

## What was observed, and when

Act 29's pin commit `P` writes `verification/seals/PRA.json`, the manifest record its own
preregistration authorizes and the protocol requires. On the tree carrying that record, and only
because of it, `R7-CV1` fails two legs:

```
R7-CV1 contracts: 101 checks, 16 control group(s); chronology ATTESTED ...;
  failures: census-equal-to-committed, s234:S2/S3/S4 the superseded predicate passes on
  this tree's own seals directory, so the successor's rejection is the added record's
edge_rigidity_probe: FAILURE
```

The same tree without that one file — the landing `L_PRA` =
`c03939c2341c7085f0a55bddb61be2d175264dba` — reports `R7-CV1 ... failures: none` in three
independent measurements: exact-`L` run 35744698210, main-push run 35747091969, and a local run.

The census computed on the pinned tree differs from the committed census in exactly three values,
and in nothing else:

```
/6a/on_the_census_head/C-S2   without the record: true   with it: false
/6a/on_the_census_head/C-S3   without the record: true   with it: false
/6a/on_the_census_head/C-S4   without the record: true   with it: false
```

Both failing legs are therefore one defect surfacing twice.

## The two defects, with their text frozen

### D1 — `on_the_census_head` is computed against the live working tree

In `_cv1_census`, at the census head:

```python
    # on the census head itself C-S2, C-S3 and C-S4 agree: CV-1 adds no seal record
    on_head = {'C-S2': _gr1_seals_ok(_GR1_B), 'C-S3': _gr1_seals_ok(_GR2_B),
               'C-S4': _gr1_seals_ok(_GR1_B)}
```

`_gr1_seals_ok(base, cwd=None)` reads the seals tree at `base` from git and compares it to the
directory on disk:

```python
    here = {}
    d = os.path.join(VERIFICATION, 'seals')
```

The comment states the intended proposition exactly: *on the census head* CV-1 adds no seal record.
That is a fact about CV-1's own head, which is `E_CV1` = `9332019aed34e33e83adc5e8740f1ef7c38742da`
and is fixed forever. The code instead asks it of whatever working tree the guard is running in. A
later round's authorized seal addition therefore falsifies a statement about a head that predates
it. The census's own docstring says it carries "no head-dependent value, so that the stage-4
measurement and the one at E compare equal"; these three entries are head-dependent, which is the
defect.

### D2 — the `s234` non-vacuity row is computed against the live working tree

In `_cv1_seals_controls`:

```python
    live_seals = os.path.join(VERIFICATION, 'seals')
```

```python
        # the successor is not vacuous: the old predicate accepts this tree's own seals directory
        res.append(('S2/S3/S4 the superseded predicate passes on this tree\'s own seals directory, '
                    'so the successor\'s rejection is the added record\'s',
                    old(_GR1_B, live_seals) is True and old(_GR2_B, live_seals) is True))
```

The row's purpose is sound: it establishes that the superseded predicate is not simply false
everywhere, so that its rejection of the synthetic successor is attributable to the added record.
But the witness it uses for "accepts" is the live directory, so the row stops holding the moment
any authorized record is added — exactly the circumstance it exists to reason about.

The neighbouring `control 3` row, `old(_GR1_B, live_seals) == _gr1_seals_ok(_GR1_B)`, compares two
predicates evaluated on the same tree and is an equality between them, not an assertion about the
tree's content. It is not in scope for this amendment and is not changed.

## The replacement rule, frozen

The replacement is the abstraction CV-1 exists to enforce, not a stem-specific exception, and it
names no round:

> After a round has landed, a historical control evaluates its round's certified historical
> subject. Later authorized repository additions are not reinterpreted as evidence about that
> historical measurement.

This is `AGENTS.md` §A.37's standing rule — "A closed round's contracts are read over the records
it manifested ... a later round's authorized additions are outside that historical scope" — applied
to the two legs above, which do not implement it.

Concretely, and this is what the execution is authorized to write:

1. A history-scoped comparator that takes both sides from git: the seals tree at a base commit
   against the seals tree at a named head commit, with no reference to the working tree. It fails
   closed where either tree is unreadable.
2. `on_the_census_head` evaluates that comparator at CV-1's certified head `E_CV1` =
   `9332019aed34e33e83adc5e8740f1ef7c38742da` once CV-1 is landed, so the three entries state the
   fact about the census head that the comment already claims.
3. The `s234` group's witness and the synthetic successor it is compared against are both taken
   from the same historical subject rather than from `live_seals`. Taking only the witness would
   leave the successor built from the live tree, so that with a later authorized record present the
   successor's rejection could be attributable to that record rather than to the synthetic one the
   control adds — which is exactly what the non-vacuity row exists to exclude.
4. Where CV-1 is not yet landed, the live-tree reading is the correct execution-mode behaviour and
   is unchanged. The switch is on CV-1's own lifecycle state, not on the presence or absence of any
   particular record, and not on any stem name.

## What the execution may not do

- No census is re-measured, and `census.json` is not rewritten. Its committed value is a certified
  historical measurement pinned by blob, and the repair's success condition is that the live
  computation equals it again, not that it be edited to match.
- No result note, preregistration or adjudicated verdict changes.
- `B_CV1`, `E_CV1`, `L_CV1`, `A_CV1` and the attestation record do not change.
- No other round's contracts change; in particular `R7-GR1` and `R7-GR2` keep their current
  counts and verdicts, and `_MANIFEST_BASELINE` is untouched.
- The repair is not a hard-coded exemption for `PRA.json` or for any named file.

## Controls the execution carries

- The live census equals the committed census again, byte for byte, with the record present:
  `census-equal-to-committed` passes.
- The `s234` row passes with the record present, and its non-vacuity is still real: the
  history-scoped witness accepts CV-1's historical subject.
- Negative: a mutated seals tree at the historical subject makes the comparator fail, so the
  replacement is not vacuously true.
- Negative: an unreadable or absent historical subject fails closed rather than skipping.
- `R7-CV1` keeps its 16 control groups, chronology `ATTESTED`, both censuses at their frozen
  outcomes, and no failure. Its check count rises by exactly the controls this repair adds, which
  are carried inside the existing `s234` group; the new total is reported in the execution's own
  record rather than asserted here in advance.
- `R7-GR1` stays 86 checks over 24 control groups and `R7-GR2` 63 over 7, both `LANDED-UNRECORDED`
  with no failure, and the existing `control 5` row that asserts exactly those counts continues to
  pass unchanged.

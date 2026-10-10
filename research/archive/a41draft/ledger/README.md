# Act 41 edit ledger (draft)

- `ledger41.json` holds 117 splice entries against D41 = `78ea3c39`.
- `render41.py` provides three functions:
  - `render(template, values)`;
  - `apply_ledger(values)`;
  - `values_from_measurements(meas)`, which maps a `measurements.json` object `{"production", "independent", "hulls"}` to the slot dict. `measurements_from_logs()` reads that object from `../probes/run_*.log`. Until `run_hulls.log` prints its object, it takes the hull values from `HULLS_D41_STUB`, which holds the D41 values.
- Running `render41.py` as a script writes `rendered/<path>` from the D41 values in `schema41.md`.
- `ledger_check.py` reads the blobs with `git show 78ea3c39:<path>`. It passes, ending with `ledger_check: OK -- 117 entries over 11 paths`. The probes are parsed and never run.

## Entry counts

| path | kind | n |
| --- | --- | --- |
| `verification/lean/dita_hierarchy_probe.py` | string / docstring | 9 / 1 |
| `verification/lean/dita_arc_exclusivity_probe.py` | string / docstring | 28 / 2 |
| `verification/lean/dita_local_escape_probe.py` | string / docstring / bugfix | 24 / 2 / 1 |
| `verification/lean/dita_torus_probe.py` | string / docstring | 1 / 2 |
| `verification/lean/dita_torus_locus_probe.py` | string / docstring | 14 / 2 |
| `OIBridge/DitaHierarchy.lean`, `DitaArcExclusivity.lean`, `DitaLocalEscape.lean`, `DitaTorusLocus.lean` | docstring | 1, 2, 3, 2 |
| `verification/lean-manuscript-census.json` | registry | 15 |
| `verification/ROADMAP.md` | roadmap / append | 7 / 1 |

Seven "string" entries change comments only: X27c, X31, L25, L32, T4, Y3 and Y20. `ast` cannot see these edits.

## What the checker verifies

1. **Ledger integrity.**
   - Every `old` occurs exactly once in its D41 file, and the spans are disjoint.
   - Applying the entries one after another in ledger order gives the same result as splicing them by their D41 spans.
   - Each kind fits its path, and there is exactly one "append" entry, placed last.
2. **Rendered texts and vocabulary.** No rendered text carries a slot or selector. Every rendered text passes a lint:
   - no bare "class";
   - no bare count of "structures";
   - none of the words "formerly", "now", "corrected" or "no longer";
   - no runs of capitals;
   - every "exact computation over every … index map" is cited as "(act 41)" or "(acts 40 and 41)".
3. **Probes.**
   - `ast.dump` with every string constant masked equals D41's for each probe.
   - The bugfix at L21 (line 541) removes exactly `any(x[2] == GEN_ONE for x in [])` and its expected `False`.
   - Every `%`-conversion in a format string is kept.
4. **Lean modules.** Each is byte-identical to D41 outside its `/-! … -/` block.
5. **JSON registry.** It parses, only `name` and `note` strings change, and all 10 outcome labels are kept.
6. **ROADMAP.** The line count and the table separators are unchanged.
7. **False branches.** Each flag is flipped in turn, and every entry still renders and passes the lint.
8. **Rendering from the measured objects.**
   - The production and independent objects agree case by case.
   - Every slot and flag the ledger uses can be derived from the objects, and the derived values equal the D41 values in `schema41.md`.
   - The rendering from the objects equals the rendering from the D41 values, file by file.

## Follow-up changes

1. **Measured verdicts are now under flags.** Each of these entries renders its verdict through a flag, and its false branch states what was found rather than drawing the conclusion:

   | flag | entries |
   | --- | --- |
   | `p.no_44_82` | R2, LH2, J4 |
   | `w.exclusive` | LA2 |
   | `h3.five_faces` | R7, LL2, J17, J18 |
   | `e.exc_is_pm1` | R4, J13 |

   `p.no_44_82`, `e.exc_is_pm1` and `h3.maximal` were added to `schema41.md`. A list of strings, such as the maximal flats, renders comma-separated with the Unicode minus.
2. **Act 37's nine classes.** LL1 and J19 now read "the nine named index maps of act 37's sorted-alignment census, in both orientations".
3. **Attribution of the converse.** J17 now reads "the converse by exact computation over every index map (acts 40 and 41)". J17 is itself a five-face verdict, so it also sits under `h3.five_faces`. For consistency, J18, R7 and LL2 attribute the converse to "(acts 40 and 41)". J18 adds that act 40 supplied the candidates and act 41 their loci under every alignment. Act 40's own probe claim reads "at the sorted alignment" everywhere: J18, and probe rows Y1–Y18.
4. **Act 41 probe paths.** H12, X1, L1 and Y1 cite act 41's probes by their repository paths.
5. **Hull counts.** J3 states the matrix-family count and the modulo-gauge count separately ("and, counted separately"). Act 36's 492 is stated as "hull parametrizations … at the sorted alignment", in both J3 and H6.

## Census rows left unedited

The census has 138 rows. The kind-c rows get no edit, except LL1, J17 and J19, which were edited by owner direction. R1 and R6 need no change.

## Rows added beyond the census

- H12
- L32, T4, Y20 (mirrors of X31)
- X27c
- R-A41 (the append)

## Material departures from the census replacements

- **Vocabulary.** Throughout the ledger, bare "class" and bare counts of "structures" were rewritten as "partition structure", "partition orbit" or "named index map".
- **H6.** Changed to "parametrizations".
- **Measured values templated.** LE2, LE3, R3, R4, J9, J13 and J18 take their values from templates.
- **Act 41 values added.** J2, J3, J7, J9, J13 and J18 now carry act 41's values.
- **Verdicts under flags.** R2, LH2, LA2, R7, LL2, J4 and J17 put their verdicts under flags.

## Not exact / to review

1. **`values_from_measurements` derives every slot except `h3.sorted_nonempty`.** That slot holds act 40's recorded 30. No measured object carries it, and no template uses it.
2. **`sig.sorted_partitions` and `sig.sorted_porbits` are derived, not read.**
   - `sig.sorted_partitions` is the census size minus the strict entries for SIG in `added_reconstructed`.
   - `sig.sorted_porbits` also relies on the full-stabilizer orbits being transpose pairs. The function checks that condition and raises an error if it fails.
3. **`p.partitions` must be the same at P and at Pu(u5).** The function raises an error if the two differ.
4. **Hull slots come from the stub.** `run_hulls.log` has not yet printed its object, so the hull values are the D41 stub values, not measured ones.
5. **Rendering details.**
   - `{hull.dims}` renders as the set `{14}`.
   - The appended `P0` sentence is the draft's text verbatim.
   - The append's `old` includes the ` |` at the end of the cell. The lint skips the act 40 clause that the append carries over, which contains "reaches any class".
6. **Replay.** The probe label edits are not replay-neutral under `tools/probe_replay_check.py`.

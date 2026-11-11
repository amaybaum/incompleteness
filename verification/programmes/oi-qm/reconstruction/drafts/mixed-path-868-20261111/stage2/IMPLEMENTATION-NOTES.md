# MIXED-PATH-1 Stage 2 — implementation notes

Program for `../STAGE2-PREREG.md` (sha256 `1ee9fd8f7322921bee73e3069ee8cfa9d86e5b380981ea6018f799a2cc43fb74`).
WIP, unverified. Each item below is a choice made where the preregistration leaves the implementation open.
None changes a control's criterion, a size, a bound, an order or the decision rule.

## Layout

- `stage2_mixedpath.py` (driver), `s2_stepper.py` (the two steppers), `s2_linalg.py` (affine rules by linear
  algebra; imports no stepper), `s2_solver.py` (locality decision, CHSH maximum), `s2_verify.py` (separate
  certificate verifier).
- `program_sha256` is the SHA-256 over the five files in the fixed order `s2_linalg.py`, `s2_solver.py`,
  `s2_stepper.py`, `s2_verify.py`, `stage2_mixedpath.py`, each contributing `name NUL length NUL bytes`.
- `invocations.jsonl`, `staging/` and `runs/<n>/` are beside the program. `n` is the line number of the
  execution's start line. Planted self-test cases publish to `runs/<n>-planted-<i>/` and are covered by the
  self-test's own start and exit lines.

## Arithmetic, bounds

- No floating-point value is used anywhere, timing included (`time.monotonic_ns`, integer division). The
  static check parses the five files and fails on true division, a float constant, `float`, `math`, `time.time`
  and a list of float-valued numpy attributes.
- The memory bound is enforced in the program: resident size (`/proc/self/statm`) is read at every block
  boundary and a value above 2 GB stops the pass (`memory`). The wall-clock bound of 90 minutes per pass is
  read at the same points (`timeout`). No `ulimit` or `timeout` wrapper is used. Thread count is held at one
  through the BLAS environment variables and is recorded in `timing.threads`.
- Enumeration block size: `2^16` configurations.

## Generators and orders

- The first output of the generator `s <- (1103515245 s + 12345) mod 2^31` is the successor of `s0`.
- C2 seeded states: value `(s div 2^16) mod q`; 256 states, each `u` slice then `v` slice, sites in
  `(x, y, z)` lexicographic order.
- Invariant (i)/(v) arrays: one stream (`s0 = 871`) over `L = 6, 8, 10, 12` in that order, 16 arrays per
  lattice, entries in `(x, y, z)` order.
- Class coordinates are ordered: current-slice coordinates (sites in `(x, y, z)` order), then retarded-slice
  coordinates. Hidden configuration index `n` gives hidden coordinate `i` the value `(n div q^i) mod q`. F_all
  content labels are the digits of the visible non-generator coordinates in the same order.
- C8: CHSH of a deterministic strategy is `A0B0 + A0B1 + A1B0 - A1B1` with output bit `x` mapped to `(-1)^x`.

## Locality decision

- Method: exact phase-1 simplex with integer-preserving pivots on a reduced form of the local-decomposition
  linear program (variables `f(x0,x1,y0)`, `g(x0,x1,y1)`; constraints: the four context tables and
  `sum_y0 f = sum_y1 g`). A feasible point gives strategy weights `f g / r`; an infeasible end gives a Farkas
  vector, turned into a Bell functional with a negative coefficient on every zero-probability entry. Pivots run
  in 64-bit arithmetic when a magnitude bound computed in Python integers shows the exact quotient fits, and
  in Python integers otherwise. Dantzig pricing, Bland's rule after 30 pivots without decrease.
- Whatever the solver returns is passed to `s2_verify.verify_certificate`; a certificate that fails is
  exit status 4. The time bounds (10 minutes each, 30 minutes total) are the only source of "no certificate".
- Identical 2x2 sub-tables share one certificate, verified once (cache keyed by the SHA-256 of the sub-table).
  Certificates are written to `certificates/certificates.json`, keyed by that hash.
- `chsh_max`: letters of probability zero are dropped before enumeration. Constant maps are included, so the
  value is at least 2 for every table.
- C11: the LOCAL certificate of C8 table 200 has `1/7` added to its first weight; the NONLOCAL certificate of
  C7 has `100 (max|beta| + 1)` added to its first coefficient on a zero-probability entry.

## Controls

- C3 is evaluated for both step types of the class-restricted stepper (current slice on even sites, current
  slice on odd sites); both must be green. For `q = 3` the same sample is used for both.
- C2b: on the states of `B` through six ticks for both classes; on every state of C3 for one step, the other
  class set to zero.
- C6: `sig_B > 0` is required for every `c` of F_const.
- C1': the count is the sum over `c` of `dep_B` of window (2,2), whose only record tick is 2.
- C10: translation is a second run of the instance with every site shifted by 2 along `x`; reflection is
  checked on the instance's own tables, `N[c][a][b][x][y] = N[c'][b][a][y][x]`, `c'` the reflected content.
- C5 non-vacuity: windows (2,2), (2,3), (4,4), (4,5) must all occur among the covered instances ((2,2), (2,3)
  in `--selftest`).
- C4 compares, per instance, window and `c`: `dep_A`, `dep_B`, `sig_A`, `sig_B` against the corresponding
  column tests.
- A control not evaluated when a pass stops is recorded red.
- Order: planted tables (C7, C8, C9, C11, C14) and C12; C2, C2b, C3 on `T(6)`; the patch rows, C13 and the
  `T(6)` linear-algebra instances of C4; then the thin-torus instances by increasing `L`.

## Results

- Families of more than 4096 contents (F_all under cb4/hor, `2^22` contents, `|H| = 1`): `per_content` is
  `null`; `per_content_aggregate` lists each distinct count table once with the number of contents carrying
  it and one example content; `table_digest` is one digest over the whole family. `tables/<id>.json` lists the
  distinct tables.
- Pi_reg with wing type S: F_const is one entry with label `*`; F_all is one entry with the empty label.
- `same_histories_as` holds the `k` of the earlier window with the same record ticks.
- Pi_hor entries are copies of the Pi_cb4 entries with `computed_as` naming the source.
- Linear-algebra instances: `dep_*` and `sig_*` are indicators (0 or 1), `hidden_count` is `null`
  (`hidden_dimension` gives the number of hidden class coordinates), the sub-menus are one aggregate entry,
  `chsh_max` is `null`, and every token from this path carries `-BY-THEOREM-L`.
- `verdicts.counts` counts every primary (R-round) window with `same_histories_as = null`, Pi_cb4 and Pi_hor
  included; `verdicts.counts_by_partition` gives the same counts per partition. The headline uses Pi_cb3 and
  Pi_reg as section 6 states.
- Canonical serialisation for digests: a JSON header (sorted keys, no whitespace) followed by the count array
  as little-endian 64-bit integers in `(a, b, h_A, h_B)` order, or, for aggregated families, the joint history
  codes as little-endian 16-bit integers in `(content, a, b)` order. `tables_digest` is the SHA-256 of the
  lines `key:digest` in computation order.
- Fields added to the schema of section 8: `selftest`, `exit_status`, `resource_bound`, `timing.threads`,
  `timing.lp_solved`, `timing.lp_milliseconds`, `invocations[].line`, per-instance `method` and `primary`.
- Stepper source hashes are recorded in `invariants`; their equality between `--selftest` and the registered
  run follows from equal `program_sha256` in the two `results.json` files.

## Self-test content beyond section 5.1

`--selftest` runs what section 5.1 lists. After that, in the non-planted execution only, it runs an extra
coverage block recorded as the single invariant `selftest-extra-coverage`, to execute the code paths of the
registered run that the dummy pipeline does not reach. It uses rules outside the corpus only:

- the dummy table `T` on further instances (`T(6)`: all partitions, F_const and F_all; `T(8)`: cb4/hor;
  `T(10)`: cb3, `D = 4`, wing types S, I, O);
- a second table for `q = 3`, `(1,2,2,0,1,0,0,2,1,1,0,2,0)`, not affine in the neighbour sum (C2, C2b, C3
  sample path and `T(6)` instances);
- an affine rule `u' = 3 Sigma(u) - v mod 7` for the linear-algebra path (patch rows at `Lambda = 24, 28` and
  the `T(6)` operator).

Only counts (comparisons, violations, equality flags) are recorded. No rule of section 2.2 is stepped.

## Not done by the program or the executor

- The program hash is not posted on #868 (no GitHub write is made in this task). It is in the commit that
  precedes the registered run and in `invocations.jsonl`.

## Executions before the registered run

All with `--selftest` (see `invocations.jsonl`): line 1, exit 0, an earlier program version without the extra
coverage block; line 4, exit 1 (a `KeyError` in the instance list of the extra coverage block, which named a
Pi_hor instance without its Pi_cb4 source; nothing published); line 7, exit 0, program
`f35ae6b58033d0f8568ae6f20f9a0107ebd3cf27854fef639186dfeb9b2794fe`, the program of the registered run.
The solver was also exercised during development on generic tables (planted PR and Z4 tables, random
mixtures of deterministic strategies); no lattice rule was involved.

## Registered run

`invocations.jsonl` line 10: one execution without `--selftest`, program
`f35ae6b58033d0f8568ae6f20f9a0107ebd3cf27854fef639186dfeb9b2794fe` (commit `68c2d2d9`), exit status 0,
`published: true`, output `runs/10/`. `runs/10/SHA256SUMS` (written after publication, by `sha256sum`) lists
every published file. One published file is not committed because of its size (1.35 MB):
`tables/R-round__q2__T6__cb3__S__D2__v__F_all.json`; its digest is in `SHA256SUMS` and its per-content
measurements and table digests are in `results.json`.

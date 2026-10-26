# NP-AVG-1 Stage 0, Layer 2: implementation plan (r2, for re-review)

**Status: WIP / UNREVIEWED, not frozen. The v8 enumeration is not authorized.** Nothing in this
directory has run on v8's configuration class. v8 setups are constructed only to check that they
are refused, and v8's record space is used only for combinatorics (counts, orbits, shard ranges and
context sizes), with no context constructed and no closure computed. No grant for v8 is
constructed; the only grants built are deliberate forgeries, which must be refused (§7).

**This revision.** r1 (`99a9797e`) was reviewed in `../../review/LAYER2-REVIEW.md` (`a63db7ba`):
ACCEPT WITH CHANGES, with required changes L2-R1 to L2-R9 and owner decisions. r2 applies L2-R1 to
L2-R8 and the accepted part of L2-R9; `CHANGES-L2-r2.md` maps each item to its edit. Every owner
ruling is left as an explicit placeholder (§4.2), and the production entry points refuse the v8
profile while any placeholder remains.

**Authority.** The owner, 2026-10-26: "NP-AVG-1 — Yes, write Layer 2 for independent review. Keep
the v8 lock intact and run no v8 experiments. Retain rule T's current wording provisionally, with
the reviewer specifically instructed to test whether it is mathematically unambiguous and whether
the proposed Layer 2 argument genuinely follows from the frozen assumptions. Do not treat an
unreviewed Layer 2 as proved."

**What this implements.** Layer 1 is frozen at `f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966`
(`../LAYER1-FREEZE.md`). The specification is `../r5/STAGE0-PLAN-r5.md`, SHA-256
`1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e`, cited below as "L1 §n". This
plan implements L1 §5b: the production enumerator, the controls, the configuration hashes and the
execution certificate. Layer 1 is not changed. Where Layer 1 leaves something unspecified or
ambiguous, the reading Layer 2 implements is stated where it is used (§4), and the points that need
an owner ruling are listed in §4.2 and §13. None is resolved by editing a frozen file.

**What a bounded run shows.** The local evidence (§12) runs on toy, planted and small-window
instances, on S6's 21-bit carrier and on v8 combinatorics only. It shows that the code runs, that the
controls can fail and that the toy outputs agree with an independent computation. It proves nothing
about v8's class. In the proof-obligation table (§9), "proved here" means an argument is written in
this plan; the r1 review's verdict is cited where it exists, and the r2 additions are unreviewed.

## 1. Files

`code/` (production, reference and controls; standard library only, Python 3.13):

| file | role |
| --- | --- |
| `s0geom.py` | production engine: contexts, cones, tips, the L3/L3′ closure, `analyse` (copied from code-r5, §2) |
| `s0ref.py` | independent reference closure, contexts, direction tables, P_A/P_G checks (copied, §2) |
| `s0native.py` | independent native evaluator (copied unchanged) |
| `s0controls.py` | the control suite C0–C18, refusal, native self-test (copied, §2) |
| `s0s6.py`, `s0symcheck.py` | S6 proof-check; C0's v8 combinatorics (copied unchanged) |
| `l2config.py` | every configuration constant, the owner placeholders, the accepted readings; `config_sha256()`, `placeholders()` |
| `l2manifest.py`, `LAYER2-MANIFEST.json` | code SHA-256 values, configuration digest, `code_digest` (certificate item 1) |
| `l2auth.py` | the v8 authorization: `decide()` and `issue_grant()` (item 6) |
| `l2landing.py` | the post-hoc check of the owner's designation against the host at landing (item 6, L2-R4 c) |
| `l2analysis.py` | C4v group, canonical representatives, orbits, `post_closure`, degeneracies, the 54 counts, structure attributes |
| `l2refcheck.py` | reference gates C7, C11 (i), C11 (ii), C17, C18, and their streamed forms (near-only for L3); imports only `s0ref` |
| `l2plan.py` | the dry run: index space, Burnside orbit count, shard plan, context sizes, the complete cost estimate; imports no engine |
| `l2calib.py` | timing calibration on planted sets for the estimate |
| `l2preflight.py` | pre-flight controls (item 2) |
| `l2mutants.py` | the mutant campaign, quick (local) and full (CI) (item 3) |
| `l2s1a.py` | the S1a driver: global bounds, per-line closures, L_A, L_G |
| `l2enum.py` | the record driver and per-record analysis, one shard per run |
| `l2merge.py` | the merge, the label generator, rule T |
| `l2cert.py` | start-up checks and the certificate builder (items 1–8) |
| `l2selftest.py` | controls of the Layer-2 machinery (20 cases) and its 18 machinery mutants |
| `l2run.py` | the bounded local evidence driver |

`design/`: the design-evidence scripts (`planted_shard.py`, `refusal_probe.py`, `crosscheck.py`,
`r5_equivalence.py`), the retained stdout and stderr of every step in `runs/`, the toy run's
structured files in `toyrun/`, and `RUN-MANIFEST.json` and `.md` (commands, exit codes, `-O`
identity, SHA-256 values of code, outputs and toy-run files, and the commit caveat of §12).

## 2. Provenance of the copied code

Each file was copied from `stage0/code-r5/` at `f33d8d63`; nothing is imported across directories.

| file | source blob at `f33d8d63` | source SHA-256 | Layer-2 change |
| --- | --- | --- | --- |
| `s0native.py` | `47a5e394` | `4206549e…8526` | none (byte-identical) |
| `s0s6.py` | `a92eae87` | `110f275c…289a` | none (byte-identical) |
| `s0symcheck.py` | `5b64720b` | `ffe390ae…18f2` | none (byte-identical) |
| `s0geom.py` | `231272ab` | `1b076aea…a867` | (a) the v8 guard: `_guard(setup, auth)`, a module function that accepts only the exact `Setup` type, reads `(dim, n, port)` from the attributes and compares with the literal `(3, 6, (0, 0, −3))`; the refusal is lifted only by an exact `V8Grant` with well-formed fields whose digests equal the running digests bound by `bind_running_digests` (L2-R4 d); `authorized_v8=True` is refused; (b) `Context` memoizes the G eligibility test per (pair, frame sources). Geometry, closure, `Rule` and `analyse` unchanged |
| `s0ref.py` | `62c6dfb0` | `39ef1d46…b227` | `ref_context`'s refusal is lifted only by an exact `RefGrant` whose commit is well formed and whose digests equal the running digests bound by the reference's own `bind_running_digests` |
| `s0controls.py` | `29790f8a` | `e8c40a5d…1a43` | `--only` (targeted mutant runs); the refusal check extended by ten Layer-2 attempts (46 in all); C14 extended to `l2analysis.py` and `l2refcheck.py`. Every control body otherwise unchanged |

The SHA-256 values of the Layer-2 files are in `code/LAYER2-MANIFEST.json` and
`design/RUN-MANIFEST.json`.

**Behaviour preserved.** Step `code_r5_equivalence_quick` runs code-r5's own quick suite and compares
its JSON with the Layer-2 suite's: every control agrees except the refusal block, which Layer 2
extends (§12). That is a toy-class check of change (b) and of the guard edit, not a proof; PO-L2-8
gives the argument for (b). The review confirmed (its §4) that geometry and closure are
byte-identical to code-r5.

## 3. Execution design

### 3.1 Record driver (L1 §5b item 1)

- **Index space.** `s0geom.record_at(setup, i, grant)` for `i` in `[0, N)`: singles first, then
  two-site pairs by (site pair, t1, t2). N = 3,225 + C(129, 2)·25² = 5,163,225 (L1 §1). It is
  authorization-bound: on v8 every call needs the grant.
- **Orbit representatives (S4).** For each index the driver forms the record, its canonical image
  (the minimum over C4v of the sorted image) and keeps the record only if it equals that image
  (`l2enum.scan`). The kept records are the representatives; each carries its orbit, with one group
  element per member. 816,050 orbits on v8 (875 single, 815,175 pair; Burnside, `l2plan`).
- **Shards.** S = 32 contiguous ranges `[⌊sN/S⌋, ⌊(s+1)N/S⌋)` (161,350 or 161,351 indices each),
  fixed by the dry run and read from `dryrun.json` by each shard.

### 3.2 Per-record analysis (item 2)

For each representative R: four closures through the engine, A and G under L3′ (`Rule()`) and L3
(`Rule(far=False)`), and `s0geom.analyse` on each. For each orbit member gR, the retained sets are
carried by g, and every attribute of gR is computed from gR's own record and the carried retained
set (`l2analysis.post_closure`, the post-closure part of `analyse`). So G-linkage, source cells,
degeneracies, in-clear sets and the (b) sets are computed per record, never transferred (L1 §6 C8,
R4-6). Each member contributes to the additive counts of the closed list (54 counts, L1 §6 C8); the
observer-class counts and the masking-equivalent count are formed by the merge (§3.7).

For survivor orbits, every member is also closed directly (§3.3), and the shard records the §3
structure of the representative: the survivor sets, linkage, (b) sets, per-member G-linkage and
source cells, shared aligned tips, cover-graph components, residual support (§4) and rule
dependence.

### 3.3 In-run gates (item 4)

| gate | runs on | verdict class on failure |
| --- | --- | --- |
| C0 (contexts) | every record on which a reference gate runs: production context equals `s0ref`'s for that record | VOID |
| C7 | every member of every survivor orbit (both conventions); on non-survivor orbits, the representative when it has a shared tip under the profile's C7 scope (§4.2, F3), and a 1-in-1,000 sample | VOID |
| C8 | every survivor orbit, every orbit with a computed MISMATCH, and a 1-in-100 sample of orbits: every member's closures computed directly and compared with the carried ones, attribute by attribute, and its count contributions compared | VOID |
| C9 | every record (every member, carried): ret_L3′ ⊆ ret_L3, and each within the S1a bound of its rule | MISMATCH |
| C10 (i) | every closure: no fixed quantity in a log | MISMATCH (L1 §5, "a fixed quantity is eliminated") |
| C11 (i) | every member of every survivor orbit (both conventions); a 1-in-1,000 sample of the other representatives | VOID |
| C11 (ii) | every survivor record (members, carried): P_A-dir and P_A (A), P_G-dir and P_G (G), by `s0ref` | MISMATCH |
| C17, C18 | every member of every survivor orbit (both conventions); a 1-in-1,000 sample each of the other representatives | VOID |

On survivor orbits the reference gates run on each member with that member's own reference context
and the closure computed directly for that member (L2-R2), so L1's "every survivor" is met without
an equivariance assumption on the reference (PO-L2-14 states what remains assumed).

**The survivor cap** (L2-R3, L2-R6). Survivor gates and residue detail run for at most
`survivor_cap_per_shard` (10) survivor orbits per shard. A shard that meets more records
`survivor_cap_exceeded = true`, still computes and counts every record, and the merge labels the run
INCOMPLETE: no survivor is left without its gates, and none is dropped from the residue silently.

**Samples** are deterministic: representative index i is sampled for gate X at rate R iff
SHA-256(salt | X | i), read as an integer from its first eight bytes, is 0 mod R. The salt and rates
are configuration constants (item 1). L1 fixes C7's rate (1 in 1,000) and C8's (1 in 100); C11 (i),
C17 and C18 are Layer-2 constants under L1 N6, each 1 in 1,000 (accepted reading F8).

**Minimal witness** (C16; L2-R1). Whenever an orbit is closed directly (survivor, flagged or sampled
orbits), the MISMATCH conditions (C9, C10 (i), C11 (ii)) are evaluated on every member's direct
results, and each record that meets one is offered to the shard's running minimum by the C16 key
(k, number of even-class context quantities, sorted items). Every candidate is compared; the shard
writes the minimum and the number of candidates seen. The merge takes the minimum over the shards'
minima. Nothing is capped.

### 3.4 S1a driver (item 5)

`l2s1a.py` computes the closures of U = {(x, 23) : x ∈ Reg}, whose context is the union of every
item's samples, under A and G with L3′ and L3 (the C9 bounds), and the L3′ closures of the items on
each of the 123 axis-parallel lines meeting Reg (reported only, N5). It writes L_A and L_G from the
L3′ bounds (the T1 reading, §4.2), and their L3 values beside them. Its own validity checks: C17
and C18 with the reference on both bounds, the L3 bound with near tips only (L2-R8), and C0 contexts
(VOID on failure); C10 (i) and ret_L3′ ⊆ ret_L3 on the bounds (MISMATCH). The reference checks
stream one explicit cone at a time (`l2refcheck.cover_index`), since the bound has 1,584 non-fixed
quantities.

### 3.5 Sharding and the stop rule (S7)

| job | timeout |
| --- | --- |
| dry run | 10 min |
| pre-flight | 30 min |
| S1a (normal and `-O`) | 40 min |
| each of 32 shards (normal and `-O`) | 40 min |
| merge and certificate (normal and `-O`) | 20 min |

The timeouts sum to 23 h (1,380 runner-minutes), within S7's 24 runner-hours over at most 32 shards.
The normal and `-O` runs of a shard may also be run as two replica jobs of 20 minutes each; they are
replicas of one shard, not additional shards, and total runner time is unchanged.

The stop rule:
1. **Before launch.** The dry run's complete estimate (§3.6) must satisfy κ · total ≤ S7's budget
   and κ · (each job's estimate) ≤ that job's timeout. κ is the launch margin, an owner-set resource
   constant fixed with its basis before the complete estimate is computed (L2-R7; review §6). It is
   an OWNER placeholder in this draft, so no launch decision can be computed, and `l2cert.startup`
   refuses the v8 profile.
2. **During the run.** A shard that reaches its timeout is cancelled by the host; its file is
   missing, and the merge labels the run INCOMPLETE. A shard that exceeds the survivor cap is
   INCOMPLETE. Nothing is retried automatically.
3. **After a stop.** A re-dispatch is a new owner decision (§A.43 item 4).

The full mutant campaign is a separate dispatch with its own budget: about 33 minutes locally on the
r3 measurements (L1 §10), plus the 18 machinery mutants at a few seconds each. It is not counted in
the 24 hours.

### 3.6 Dry run and the complete cost estimate

The dry run (`l2plan.py`) is mandatory: every computing entry point refuses to run without a
`dryrun.json` for the same configuration with `closures_computed = 0`, and for v8 without a launch
decision that admits the run (certificate item 7). It imports neither engine nor reference; it
constructs no context and calls no guarded entry point (the review ran it under an import trap). Its
formulas are checked against the engine on the toy class (L2-PLAN, L2-MASK, L2-SHTIP).

It prints:
- N, the Burnside orbit count and the shard plan;
- the histogram of non-fixed context sizes over all records, from per-item sample counts by
  convolution, with no record enumerated;
- for the toy profile only, the masking-equivalent count (on v8 the merge computes it);
- with `--shared-tips`, the number of records whose initial context has a shared near tip, by
  combinatorial enumeration with no closure. For v8 this count is part of the owner's F3 decision
  and is not run locally.

**The estimate** (L2-R6), in runner-seconds, term by term, with t_A(m), t_G(m) the calibrated
closure times and r_A(m), r_G(m) the calibrated reference-closure times at m non-fixed quantities
(`l2calib.py`, planted sets only; beyond the largest calibrated size scaled quadratically), m̄ the
mean context size and m_max the largest; each run-time term is doubled for the `-O` copy:
1. **closures:** Σ_m count(m) · (orbits/N) · [2 t_A(m) + 2 t_G(m)] · overhead (2, a configuration
   constant covering analysis and member attributes);
2. **sampled gates:** (1/1,000 for each of C7, C11 (i), C17, C18) · reps · [r_A(m̄) + r_G(m̄)], and
   C8 on 1 in 100 orbits · 8 members · [2 t_A(m̄) + 2 t_G(m̄)];
3. **C7 under the chosen scope (F3):** reps with a shared tip under that scope · r(m̄), per
   convention. The term is given for each candidate scope when `--shared-tips` has been run, and
   always as seconds per percent of representatives; while the scope is an OWNER placeholder the
   total is not computed;
4. **survivor gates, capped:** cap · S · 8 · [2 t_A + 2 t_G + 4 (r_A + r_G)] at m_max;
5. **pre-flight** (300 s) and **merge** (300 s per run): stated allowances with their basis in
   `l2config`;
6. **S1a:** four bound closures and four streamed reference checks at the universe size, and two
   closures per axis line.

Launch is decided by κ as in §3.5; `launch_within_budget` is `null` with the reason stated while κ
or the C7 scope is a placeholder. The local figures are in §12.

### 3.7 Merge, labels and rule T (items 5–8)

`l2merge.py` reads only structured files (§5). A shard is refused, and counts as missing, if any of
the following holds:
- its self-digest, schema, profile or index is wrong;
- its `code_digest`, configuration digest, dry-run digest or S1a digest differs;
- its range differs from the plan, or its scanned count differs from the range length;
- its `-O` copy differs byte for byte.

**Coverage.** The accepted ranges must be a disjoint exact cover of [0, N). Recount: the orbit
weights must sum to N and the representatives must number Burnside's orbits (PO-L2-2). A failure is
INCOMPLETE.

**Residue completeness** (L2-R3). Each shard must list one survivor detail per survivor
representative it counted, and must not have exceeded the survivor cap; otherwise INCOMPLETE
(PO-L2-15).

**Counts.**
- The additive counts are summed.
- Observer classes are Σ |orbit(K)| over the distinct canonical public sets K, per convention and
  category (PO-L2-5).
- `masking_equivalent_records` is computed by the analytic formula of PO-L2-6, in the L1 reading
  (accepted reading F5).

**Labels** (L1 §5), first match:
1. **VOID:** a pre-flight control of VOID class, a VOID gate, the manifest, or the authorization fails.
2. **MISMATCH:** C6's execution instances, C9, C10 (i), C10 (ii), C11 (ii) or C12 fails.
3. **INCOMPLETE.**
4. **BASE_RESIDUE** (unreachable while F1 holds, §13).
5. **COLLAPSE_ALL.**
6. **RESIDUE_UNLINKED:** survivors exist, and none is Φ-linked under A or G-linked under G.
7. **RESIDUE.**

**Recorded with the label:** the commits recorded by pre-flight, S1a and every shard; the CI run
identity; the authorization echo with the owner check; the owner rulings still pending; the accepted
readings. **Rule T** is evaluated as in §8.

## 4. Layer-2 readings

### 4.1 Readings in force

| point | Layer-2 reading | status | where |
| --- | --- | --- | --- |
| residual support (L1 §3) | under A, 3 bits per pair cell in Φ's seven cells ∪ the cones of S_A; under G, 3 bits per seed in the union of the cones of S_G; compared with S_max = 27; reported only | accepted (review F4) | `l2analysis.residual_support_bits` |
| masking equivalence (E2) | equal even-class contexts, with E1 merges, as L1 §1 states; code-r5's record-sample keying reported beside it | accepted (F5) | `l2plan.masking_equivalent` |
| C12's per-record clause | checked once on the universe of quantities, which covers every record (PO-L2-9) | accepted (F7) | `l2preflight.c12_universe` |
| C11 (i), C17, C18 sample rates | 1 in 1,000 each, plus every survivor record | accepted (F8) | `l2config` |
| "s0geom's frozen engine" (§5b) | the engine implementing the frozen rule; the guard and memo edits leave geometry and closure unchanged | accepted (F10) | §2 |
| C6 execution instances, C10 (ii), C12 on v8 | run in the authorized pre-flight only | accepted (F11) | `l2preflight` |
| BASE_RESIDUE | reachable only after the MISMATCH-resolution amendment L1 §5 requires; §5's precedence is implemented | accepted (F1) | `l2merge.label` |
| base-relative survivors | literal text; reported only under BASE_RESIDUE | moot while F1 holds (F2) | `l2enum` |

The accepted readings are also recorded in `l2config.CONFIG['accepted_readings']` and echoed into
`result.json`.

### 4.2 Owner rulings pending (placeholders)

Each is an `OWNER-PLACEHOLDER` in `l2config`. `l2cert.startup` refuses the v8 profile while any
placeholder remains (certificate item 1), and `result.json` lists the pending ones.

| ruling | question | what the code does meanwhile |
| --- | --- | --- |
| T1 (rule T erratum) | rule T's bound: L3′ or L3 | computes L_A and L_G from the L3′ bound (review's recommendation) and reports L3 beside them |
| T2 (rule T erratum) | S1a's status | implements the definition of §4.3 (review's recommendation) |
| T5 (rule T erratum) | the L_G wording | reads "a quantity with a seed tip, whose cone contains a source cell" (review's recommendation) |
| F3 | C7's shared-tip scope | v8 profile: none (placeholder); toy profile: the literal initial-context reading, to exercise the path; the estimate gives the C7 term per candidate scope |
| κ | launch margin and budget (S7) | no launch decision is computed |
| F6 | C8's closed list (54) or a 4-count erratum (58) | computes the 54 counts of C8's list |

### 4.3 S1a status (T2, Layer-2 reading pending the owner's ruling)

VOID if pre-flight fails or S1a's reference checks fail (C17, C18 or C0 on either bound); MISMATCH if
S1a's C10 (i) or ret_L3′ ⊆ ret_L3 fails on the bounds, or any shard's C9 fails against the bounds;
INCOMPLETE if `s1a.json` is missing, has differing digests or differs under `-O`. The review found
this admissible under rule T's neutrality clause (its inputs are validity facts, not the k ≤ 2
label).

## 5. Structured outputs (§A.44)

Every verdict reads exit statuses and these files. No log text is read. Where printed output carries
a fact (pre-flight's subprocesses), the producing step parses the JSON object that the subprocess
prints as its whole stdout and records its exit status; a non-JSON stdout counts as failure. The
schema names are recorded in each file.

| file | schema | content |
| --- | --- | --- |
| `dryrun.json` | `…/dryrun/1` | records, orbits (single, pair), group order, shard plan [{shard, lo, hi, count}], context-size histograms, max context size, `closures_computed: 0`, `contexts_constructed: 0`, configuration digest, optional `shared_tip_records`, optional `cost` {terms, total, total without the C7 term, per-job estimates, timeouts, κ, C7 by scope and per percent, survivor cap, `launch_within_budget`, launch rule}, expected checks, `pass` |
| `preflight.json` | `…/preflight/1` | profile, mode, `code_digest`, configuration digest, `commit`, `tree_clean`, `ci_run`, authorization echo, `controls` {name: {pass, class, …}}, `base_collapsed` {A, G}, the full control-suite, self-test and S6 objects, `pass` |
| `mutant-campaign.json` | `…/mutant-campaign/1` | mode, `code_digest`, the unmodified-suite precondition, per mutant {named case, exit, failed, killed, run}, demonstration fields, killed/total, `pass` |
| `s1a.json` | `…/s1a/2` | bounds per (convention, rule) as flat integer lists, sizes, L_A, L_G, L3 values, linked quantities, per-line results, reference checks per convention and rule, `status`, reasons, digests, `commit`, `tree_clean`, `ci_run`, `sha256` |
| `shard-<s>.json` | `…/shard/2` | profile, shard, range, records, scanned, representatives, orbit weight, digests (code, config, dry run, S1a), `commit`, `tree_clean`, `ci_run`, authorization echo {decision, artifact, owner check, CI run}, base retained sets, additive counts, canonical class keys with orbit sizes, base-relative and L3-only tallies, gate tallies and first failures (diagnostics), `witness_min`, `witness_candidates_seen`, `survivor_representatives`, `survivor_cap`, `survivor_cap_exceeded`, survivor detail, `sha256` (of the canonical JSON without it) |
| `result.json` | `…/result/1` | label, `label_source`, VOID/MISMATCH/INCOMPLETE reasons, base precondition, 54 counts, record-sample masking reading, structure tallies, in-run gate totals, minimal witness and candidates seen, coverage, S1a {status, L_A, L_G, L3 values, bound sizes, lines}, `rule_T` (with the T1, T2, T5 readings and their ruling status), authorization echo, `ci_run`, `commits` {pre-flight, S1a, shards}, `owner_rulings_pending`, `accepted_readings`, digests, coverage limits (L1 §11), input digests, residue file digest |
| `expected-controls.json` | `…/expected-controls/1` | the hand-derived and recorded expected values (`l2config.CONFIG['expected']`) and the observed pre-flight results |
| `residue.json` | `…/residue/1` | survivor representatives with the §3 structure (only when survivors exist) |
| `certificate.json` | `…/certificate/1` | items 1–8, each with `holds` and its evidence, including the commit binding and the landing requirement; `holds` overall |
| `fetched.json` (landing) | `…/v8-designation-fetch/1` | written at landing from the host API: comment URL, author login, body SHA-256, whether the body contains the required line |

All files are canonical JSON, with sorted keys and integers and strings only. Normal and `-O` runs
write byte-identical shard, S1a and result files (item 7).

## 6. The execution certificate (L1 §5b item 8)

| item | implementation | fails closed by |
| --- | --- | --- |
| 1 frozen manifest | `l2manifest.verify`: every `.py` SHA-256, the configuration digest and `code_digest` equal `LAYER2-MANIFEST.json`, and `vars(Rule())` equals the configuration's rule fields; then the running digests are bound in the engine and the reference; for v8, no OWNER placeholder may remain | printing VOID and exit 2 before anything is computed |
| 2 pre-flight | `l2preflight.py` in the same job and commit: the full control suite (C0–C3, C6, C7–C18, refusal, native self-test), the two C11 direction mutants (each must fail C11), S6, C0's v8 combinatorics, the Layer-2 self-test, C12 on the universe, and for v8 C6's execution instances and C10 (ii); its commit must be the run's commit (L2-R5) | startup refusing without a passing `preflight.json` for this `code_digest`; certificate item fails on a commit mismatch |
| 3 mutant campaign | `l2mutants.py --full` in CI; startup refuses without a passing `mutant-campaign.json` with mode `full` for this `code_digest` | VOID, exit 2 |
| 4 in-run gates | §3.3 | VOID or MISMATCH in the merge, never a label of their own |
| 5 merge | §3.7, including residue completeness | INCOMPLETE |
| 6 authorization | §7: granted at start-up; the shards and `result.json` echo the owner check and the CI run identity; the designation is re-verified from the host at landing (`l2landing.py`), which the certificate records as required for v8 | VOID, exit 2, before any context exists; the result does not land if the landing check fails |
| 7 determinism and commit binding | normal and `-O` shard, S1a and result files compared byte for byte; dry run mandatory; `preflight.json`, `s1a.json`, every shard and `result.json` record one and the same commit, equal to the authorization artifact's commit for v8, and for v8 every one records a clean tree (L2-R5) | INCOMPLETE (shards, S1a); certificate item fails (result, commits) |
| 8 labels | only `l2merge.label`, from structured files; `label_source` recorded | — |

`l2cert.py --build` writes `certificate.json` from the files alone. A certificate that holds attests
that the run followed Layer 2. It does not turn the label into a proof.

## 7. The v8 lock

- **Content-keyed refusal, kept.** `Context`, `num_records`, `record_at` and `record_samples` refuse
  any `Setup` whose (dim, n, port) equal (3, 6, (0, 0, −3)), whatever its region, slice range or
  sources. The comparison is against a literal, and the port is compared as a tuple. `s0ref.ref_context`
  does the same. A `Setup` subclass is refused.
- **Default refuses.** The refusal is lifted only by an exact `V8Grant` (engine) and `RefGrant`
  (reference), with well-formed fields whose digests equal the running `code_digest` and
  configuration digest. Those are bound once per process by `bind_running_digests`, which
  `l2cert.startup` calls after verifying the manifest; with nothing bound, every grant is refused, and
  a second binding to other values is refused (L2-R4 d). `True`, other truthy values, duck-typed
  objects, subclass instances and uninitialized instances are refused (refusal check, 46 attempts;
  L2-GUARD).
- **What the lock is (L2-R4 a).** No file in the repository other than `l2auth` constructs a grant
  (static check L2-S1); a grant can be forged in-process, so the lock prevents accidental runs, and
  the authoritative gate is the CI owner-check job and the post-hoc verification below. The review's
  in-process forgeries are run as controls (`refusal_probe`): a well-formed `V8Grant` and `RefGrant`
  built directly are refused both before and after the running digests are bound, because their
  digests are not the running ones. A forger who also supplies the running digests is not excluded
  by any in-process check; nothing in this directory constructs such a grant.
- **How a grant is issued.** `l2auth.issue_grant` mints only when `decide()` returns `ok` on three
  inputs.
  1. **The authorization artifact** (JSON, supplied as a dispatch input, outside the frozen tree,
     since a commit cannot contain its own SHA). Its fields:
     - `schema` and `scope`, each a fixed literal;
     - `commit`: 40 lowercase hex, equal to the checked-out HEAD;
     - `code_digest`, equal to the verified manifest's;
     - `config_sha256`;
     - `owner = amaybaum`;
     - `designation_url`: a comment URL in this repository;
     - `designated_at`.
  2. **The owner check** (JSON), written by the workflow from the host API's record of that comment:
     - the author's login, which must be the owner;
     - whether the body contains the exact line
       `NP-AVG-1 Stage 0 v8 enumeration authorized at <commit> code_digest <digest>`;
     - the body's SHA-256;
     - the commit.
  3. **The checkout's facts:** HEAD, a clean Layer-2 directory, manifest verification and the
     configuration digest.
- **Echo (L2-R4 b).** Pre-flight, every shard and `result.json` echo the decision, the artifact, the
  full owner check and the CI run identity (`GITHUB_RUN_ID`, attempt, repository, workflow).
- **Verification at landing (L2-R4 c).** Before the result lands (the landing or evidence-retention
  step), the workflow re-fetches the designation comment from the host and writes `fetched.json`;
  `l2landing.py` requires the same comment, written by the owner, with the body SHA-256 echoed in
  `result.json`, containing the required line, and one commit across artifact, owner check and
  result. A failure blocks the landing. This is the check a local forgery of the owner-check file
  cannot pass. Certificate item 6 records it as required for v8.
- **Testing.** `decide()` is pure, so each of its 17 refusal paths is tested without minting
  (L2-AUTH); on fabricated inputs and fabricated facts it returns `ok`, which is the documented limit
  the landing check addresses (`refusal_probe` records it). The landing check is tested on synthetic
  data (L2-LAND). The design evidence never constructs a valid grant.
- **The dry run.** `l2plan.py` runs for v8 without a grant. It never reaches a guarded entry point,
  and it computes combinatorics only.

## 8. Rule T, as frozen (provisional wording)

**Implementation.** `l2merge.rule_T(s1a_status, L_A, L_G)`, a function of those three values only:

| case | outcome | recorded consequence |
| --- | --- | --- |
| S1a status not OK | `not_evaluated` | S1b and S1c not proposed (L1 text verbatim) |
| L_A = 0 and L_G = 0 | `L_A = L_G = 0` | the L1 text verbatim, the geometric fact only, no law statement for k > 2; S1b and S1c not undertaken |
| L_A > 0 or L_G > 0 | `L_A > 0 or L_G > 0` | S1b put to the owner as a new preregistration (L1 text verbatim) |

`wording_status` is recorded as "provisional: retained pending owner confirmation". Each output also
records the T1, T2 and T5 readings and that their rulings are pending. The cost clause is recorded as
not evaluable in Stage 0 (the review agrees, T3).

**Neutrality** is tested in two ways (L2-RT). The function's signature contains no label. Through the
merge, the outcome is the same under COLLAPSE_ALL, RESIDUE_UNLINKED, RESIDUE and BASE_RESIDUE. The
review found it admissible as implemented.

**The argument for the L_A = L_G = 0 consequence (PO-L2-7).** Let R be any finite set of items in
Reg × {−1, …, 23}, and U = {(x, 23) : x ∈ Reg}.

1. **Nesting.** The samples of an item (x, t) are the even-class site-times (x, s) with −1 ≤ s ≤ t,
   a subset of the samples of (x, 23). The fixed quantities and port samples are the same in every
   context. So Ctx(R) ⊆ Ctx(U). (L1 §1.)
2. **Monotonicity.** By PO4 (a larger context retains a superset), ret(R) ⊆ ret(U), under A and
   under G, for L3′. Under G the eligibility predicate is the same for both contexts, because the
   frame is the union of the G cones of Φ, V, p and the even port samples, which are in every
   context and do not depend on the record (L1 §2).
3. **Linked survivors.**
   - Under A, S_A(R) = ret_A(R) ⊆ ret_A(U). R has a Φ-linked survivor iff some q ∈ S_A(R) has a Φ
     cell in its cone. Such a q is counted by L_A.
   - Under G, S_G(R) is the set of q ∈ ret_G(R) with a seed tip. Whether q has a seed tip is
     intrinsic to q given the frame (L1 PO7), so S_G(R) is contained in the quantities of ret_G(U)
     with a seed tip. R is G-linked iff some q ∈ S_G(R) has a source cell in its cone. Such a q is
     counted by L_G.
4. Hence L_A = 0 implies that no such R has a Φ-linked (in particular J-linked) survivor under A, and
   L_G = 0 implies that no such R has a G-linked survivor under G.

**Review verdict** (its §2): the consequence follows from L1 §1, §2, PO4 and PO7 under the T1, T2
and T5 readings; the text is not unambiguous in T1, T2 and T5, which need an owner ruling (a Layer-1
erratum), with T3 and T4 as notes. The converse does not hold and is not used: L_A > 0 does not imply
that any record has a linked survivor.

## 9. Proof obligations of Layer 2

| id | statement | status |
| --- | --- | --- |
| PO-L2-1 | `record_at` is a bijection from [0, N) onto the record space, and the shard ranges are a disjoint exact cover of [0, N) | **Proved here; review: valid.** Ranges: ⌊sN/S⌋ is non-decreasing from 0 to N. Bijection: standard unranking (singles; divmod by 25²; lexicographic pair decoding). **Checked:** toy, C13 recount and L2-ORB; v8 indirectly by the merge's recount |
| PO-L2-2 | Keeping exactly the records equal to their canonical image keeps one record per C4v orbit; the orbit weights sum to N, and the representatives number the orbits | **Proved here; review: valid.** **Checked** in every run by the merge's recount against Burnside's count; toy: 488 and 1,400 |
| PO-L2-3 | Equivariance of the true closure: ret(gR) = g·ret(R) for g ∈ C4v, under A and G, for L3′ and L3 | **Proved here from L1 PO4 and §1 E4; review: valid for the true closure.** **Checked** in-run by C8 on sampled, flagged and survivor orbits; on toy, all 488 orbits |
| PO-L2-4 | `post_closure(ctx_gR, g·ret(R))` equals `analyse(ctx_gR)` | **Follows from PO-L2-3 as code identity; review: valid.** **Checked:** L2-POST, all toy records, both conventions, both rules; C8 in-run |
| PO-L2-5 | The merged counts equal the full per-record computation (additive counts; observer classes as Σ \|orbit(K)\| over distinct canonical public sets) | **Proved here given PO-L2-3; review: valid.** **Checked:** toy, all 54 counts equal to code-r5's full computation |
| PO-L2-6 | Masking-equivalence canonical form and the analytic class count | **Proved here; review: valid.** **Checked:** brute force on three toy variants, both readings (L2-MASK) |
| PO-L2-7 | Rule T's L_A = L_G = 0 consequence (§8) | **Review: valid under the T1, T2 and T5 readings**, from L1 §1, §2, PO4 and PO7; the readings await the owner's ruling (§4.2) |
| PO-L2-8 | Memoizing the G eligibility per (pair, frame sources) does not change any result | **Proved here; review: valid.** **Checked:** quick suite identical to code-r5's except the refusal block |
| PO-L2-9 | C12 on the universe covers every record | **Proved here; review: valid** |
| PO-L2-10 | **Restated (L2-R1).** The witness is minimal among the records whose computed results — carried, or directly recomputed on flagged and sampled orbits — meet a MISMATCH condition. Precisely: the candidates are the members of every orbit closed directly (survivor orbits, orbits whose carried results meet a MISMATCH condition, and the 1-in-100 C8 sample), each confirmed on its direct results; the shard keeps the running minimum over all of them and the merge the minimum over the shards | **Proved here (by construction: every candidate is compared, nothing is capped).** **Checked:** L2-WIT (300 candidates in random order), L2-C16, the planted negative control. **Not claimed:** minimality over records whose fault is seen neither in the carried results nor in a directly recomputed orbit; that would need the computed closure to be equivariant, which is sampled (C8), not proved |
| PO-L2-11 | Normal and `-O` runs give identical outputs | **Not proved; checked per file.** No control logic uses `assert` in Layer-2 modules; `s0symcheck.py` relies on `assert`, so pre-flight always runs it without `-O` |
| PO-L2-12 | The S1a bounds are C9 bounds: ret(R) ⊆ ret(U) for every record, for L3′ and for L3 | **Follows from L1 PO4** (PO-L2-7 steps 1–2); review: valid. Both bounds are reference-checked (L2-R8) |
| PO-L2-13 | The dry run's formulas (N, Burnside, context histogram, shared-tip count) equal the engine's | **Checked on toy only** (L2-PLAN, L2-SHTIP); review: N and Burnside on v8 independently confirmed by `s0symcheck` |
| PO-L2-14 | **New (L2-R2).** Survivor-gate coverage: C0, C7, C11 (i), C17 and C18 run on every record the computation classifies as a survivor, each with its own reference context and its own direct closure | **Proved here for the orbits whose representative is a survivor:** every member is closed directly and gated (up to the cap; beyond it the run is INCOMPLETE). A member that would be a survivor under direct closure in an orbit whose representative's computed closure is collapsed is reached only through the 1-in-100 C8 sample; its absence rests on the equivariance of the computed closure, which is sampled (C8), not proved. No equivariance of the reference is assumed. **Checked:** L2-SURV (4 members × 2 conventions on the planted block orbit); `planted_survivor_path` |
| PO-L2-15 | **New (L2-R3).** Residue completeness: a label other than INCOMPLETE implies that every survivor representative counted by a shard has its detail in the residue | **Proved here:** the merge's `residue_complete` requires, per accepted shard, `survivor_cap_exceeded = false` and exactly `survivor_representatives` details; the shard appends one detail per gated survivor representative and sets the flag when it meets one beyond the cap. **Checked:** L2-MRG (truncated residue and exceeded cap give INCOMPLETE); M_residue_ignored |

Nothing in this table is claimed beyond its status. "Checked" items are evidence on the instances
named, not proofs.

## 10. Invariant → checkpoint (§A.41)

**Layer-1 invariants** (L1 §7). For each: the implementing code, its checkpoint in Layer 2, and the
local evidence (§12).

| L1 invariant | code | Layer-2 checkpoint | local evidence |
| --- | --- | --- | --- |
| configuration space and counts | `s0symcheck`, `l2plan.Space` | pre-flight `C0_v8_combinatorics`; dry run `expected_checks`; merge recount | symcheck exit 0; v8 dry run: 5,163,225 records, 816,050 orbits, group order 8 |
| C4v with correct orbit counts | `l2analysis.group`, `l2plan.orbits_burnside` | L2-ORB; merge recount | toy 488/1,400 |
| orbit representatives preserve every reported count; per-record results for invariant attributes | `l2enum.Shard.rep`, `l2analysis` | in-run C8 (1/100 orbits, survivor orbits, flagged orbits); merge recount | toy: all orbits, 0 failures; 54 counts equal to full computation |
| source-dependent attributes per record | `l2analysis.post_closure` per member | C8 compares `g_linked` and `source_cells` with direct closure | toy C8 in-run, 0 failures |
| cones match the native rule | `s0geom.in_cone` | pre-flight C1 (full depths in CI) | quick C1: 5,000 perturbations, pass |
| tips bijective, off-axis not | `s0geom.tip_labels` | pre-flight C2 | quick: 133 tips, 8 contrasts |
| planted families survive; planted non-survivors collapse | — | pre-flight C3, C11 (iii) | quick C3 block (8, 0); C11 (iii) 96 sets, 0 failures |
| elimination exact | `s0native` | pre-flight C15 | quick: 0 violations (2^21, 2^18 worlds) |
| every logged elimination justified | `l2refcheck.c18`, `c18_stream` | pre-flight C18; in-run C18 (1/1,000; every survivor member); S1a C18 on both bounds | toy in-run 976 checks, 0; planted survivor orbits 16, 0 |
| every required elimination applied | `l2refcheck.c17`, `c7` | pre-flight C17, C7; in-run C17, C7; the unapplied-elimination mutant | killed at C17 |
| every eligible configuration considered | `l2enum.scan`, `l2merge.coverage_ok`, `recount_ok` | merge coverage and recount; C13; M_skip_index | killed at L2-ORB |
| planted survivors vs non-survivors (B, G, Φ- and frame-adjacent) | — | pre-flight C3, C6, C11 (iii) | pass |
| S6 | `s0s6` | pre-flight S6 | pass; positive control holds; negative control 64 non-target classes |
| v8 not run without authorization; refusal keyed on (dim, n, port) | `s0geom._guard`, `s0ref._ref_granted`, `l2auth`, `l2cert.startup`, `l2landing` | refusal check (46); L2-GUARD; L2-AUTH; L2-S1; L2-LAND; `refusal_probe` (entry points and forgeries) | 46/46; 9/9 entry-point attempts; 9/9 forgeries refused |
| frozen code and configuration are the ones run | `l2manifest`, `l2cert.startup` | items 1–3 at start-up; L2-MAN; placeholders refused for v8 | M_manifest_blind killed |
| no over-elimination in any convention, type or depth | — | C3, C15, C11 (i) and (iii), mutants | quick campaign 17/17 rule mutants |
| far tips load-bearing beyond L3 | — | C3 block minus centre; near-only mutant | killed at C3 |
| closure correct by independent code | `l2refcheck.c7` | pre-flight C6, C7; in-run C7 (every survivor member) | toy in-run 976 checks, 0; planted survivor orbits 16, 0 |
| base context collapsed | `l2preflight.v8_execution` (v8); C6 toy | pre-flight `C6_execution` (MISMATCH); `base_collapsed` | toy base collapsed |
| monotonicity | `l2enum.c9_ok` | pre-flight C9; in-run C9 per member; S1a L3′ ⊆ L3 | toy in-run 2,800 checks, 0; M_c9_off killed |
| no fixed quantity eliminated | `l2enum.c10i_ok` | in-run C10 (i) on every closure (MISMATCH) | 1,952 checks, 0 |
| port samples in-frame under G | `l2preflight` | pre-flight C10 (ii) (toy), `C10ii_v8` (v8) | toy pass |
| per-direction tables match and decisions agree | `l2refcheck.c11i` | pre-flight C11 (i); in-run C11 (i) (every survivor member) | toy in-run 5,328 tables, 0 |
| P_A-dir, P_G-dir, P_A, P_G on survivors and planted sets | `l2refcheck.props` | pre-flight C11 (ii); in-run C11 (ii) on every survivor member | planted survivor run: 16 checks, 0 |
| planted directional retention | — | pre-flight C11 (iii) | 96 sets, 0 failures |
| per-direction control detects single-direction errors | — | pre-flight non-vacuity mutants; quick campaign | both demonstrations fail C11 only |
| every proof-dependent rule rests on a complete statement | — | document property; §9 for Layer 2's own | independent review |
| rule T applied as preregistered | `l2merge.rule_T` | `result.json` `rule_T`; L2-RT; M_ruleT_or | toy: evaluated, recorded |
| frame is B8; in-frame cones stay in it | `l2preflight.c12_universe` | pre-flight C12, `C12_universe` | toy: 129 = 129, 15 in-frame quantities checked |
| design evidence retained and deterministic | `l2run` | `RUN-MANIFEST`, `-O` identity | §12 |
| Layer-2 evidence structured, complete, retained | `l2merge`, `l2cert` | items 5, 7, 8; residue completeness; commit binding; certificate | toy certificate holds |
| integer-only, no repository read in the engine | — | C14 (extended) | pass |
| minimal witness well defined | `l2enum.Shard.add_witness`, `l2merge.minimal_witness` | C16; L2-WIT; L2-C16; planted negative control | M_witness_first and M_witness_max killed |
| distinguishability classes (a)–(c) | `l2analysis.post_closure`, canonical keys | C8 (invariant parts), C7 | toy |
| every control can fail | — | the mutant campaign, quick now and full in CI | 35/35 quick |

**Layer-1 controls** (L1 §6). For each: the implementing code, where it runs, and its class on
failure.

| control | code | where it runs | class |
| --- | --- | --- | --- |
| C0 | `s0symcheck.py`; `s0controls.c0_context_sizes`; `l2enum` reference contexts | pre-flight; in-run (every reference context); dry run (counts) | VOID |
| C1, C2 | `s0controls.c1_cones`, `c2_tips` (native lanes) | pre-flight (full depths) | VOID |
| C3 | `s0controls.c3_planted` | pre-flight | VOID |
| C6 | `s0controls.c6_hand` (toy); `l2preflight.v8_execution` (base, (q9, 9)) | pre-flight | toy VOID; execution instances MISMATCH |
| C7 | `s0controls.c7_reference`; `l2refcheck.c7` | pre-flight; in-run | VOID |
| C8 | `s0controls.c8_symmetry`; `l2enum.Shard.rep` (direct member closures) | pre-flight; in-run | VOID |
| C9 | `s0controls.c9_monotone`; `l2enum.c9_ok`; `l2s1a` | pre-flight; in-run; S1a | MISMATCH |
| C10 (i) | `l2enum.c10i_ok`; `l2s1a` | in-run; S1a | MISMATCH ("a fixed quantity is eliminated") |
| C10 (ii) | `s0controls.c10_fixed`; `l2preflight.v8_execution` | pre-flight | MISMATCH |
| C11 (i) | `s0controls.c11_dir_tables`; `l2refcheck.c11i` | pre-flight; in-run | VOID |
| C11 (ii) | `s0controls.c11_props`; `l2refcheck.props` | pre-flight; in-run | MISMATCH |
| C11 (iii) and non-vacuity | `s0controls.c11_planted`; the two direction mutants in `l2preflight` | pre-flight | VOID |
| C12 | `s0controls.c12_frame`; `l2preflight.c12_universe` | pre-flight | MISMATCH |
| C13 | `s0controls.c13_coverage`; `l2merge.coverage_ok`, `recount_ok`, `residue_complete`; `l2run` retention | pre-flight; merge | INCOMPLETE (coverage, residue); VOID (suite) |
| C14 | `s0controls.c14_static` (extended); L2-S1 | pre-flight | VOID |
| C15 | `s0controls.c15_exact` | pre-flight | VOID |
| C16 | `s0controls.c16_witness`; `l2enum.Shard.add_witness`; `l2merge.minimal_witness` | pre-flight; in-run; merge | VOID (self-test) |
| C17, C18 | `s0controls.c17_fixed_point`, `c18_audit`; `l2refcheck.c17`, `c18`, `c17_stream`, `c18_stream` | pre-flight; in-run; S1a (both bounds) | VOID |
| refusal | `s0controls.refusal` (46 attempts); `l2selftest` L2-GUARD, L2-AUTH; `l2cert.startup`; `refusal_probe` | pre-flight; every entry point | VOID |
| native self-test | `s0controls.native_self_test` | pre-flight | VOID |
| S6 | `s0s6.py` | pre-flight | VOID |

**Layer-2 invariants**:

| invariant | checkpoint |
| --- | --- |
| no repository file but `l2auth` constructs a grant; only `l2cert` binds the running digests | L2-S1 (static) |
| a grant is accepted only with the running digests; forgeries refused | L2-GUARD; `refusal_probe` forgeries; M_guard_truthy, M_grant_unbound |
| the authorization binds commit, code, configuration and owner | L2-AUTH (17 refusal cases, one accepting case, no mint); M_auth_no_commit |
| the designation is re-verified from the host at landing | L2-LAND; certificate item 6 records the requirement |
| the certificate binds the run's commits | L2-CERT; M_commits_unbound |
| no owner placeholder remains for v8 | `l2cert.startup` (item 1); `result.json` `owner_rulings_pending` |
| the dry run computes no closure | `closures_computed = 0` in `dryrun.json`, checked by start-up; L2-S1 (no engine import) |
| the carried attributes equal direct ones | L2-POST; C8 in-run |
| survivor gates on every member | L2-SURV; M_survivor_rep_only |
| the witness is the running minimum | L2-WIT; M_witness_first |
| residue complete or the run INCOMPLETE | L2-MRG; M_residue_ignored |
| shard coverage and recount | merge; L2-MRG; M_merge_no_coverage, M_skip_index, M_every_record_rep |
| label precedence | L2-LBL (11 cases); M_label_mismatch_first |
| sampling is deterministic and non-empty | L2-SAMPLE; M_sampler_never |
| masking count reading | L2-MASK (three toy variants, both readings); M_mask_no_merge |
| behaviour of the copied engine preserved | `code_r5_equivalence_quick` |

## 11. CI workflow design (proposal only; no file is added under `.github/`)

Two dispatch-only workflows, each launched only on the owner's separate approval (§A.43 item 4), on
a branch whose head is the frozen Layer-2 commit, after the owner rulings of §4.2 are recorded.

**A. `np-avg-1-stage0-mutants` (the full campaign, item 3).**
- **Inputs:** none.
- **Jobs:**
  - `preflight-toy`: `l2preflight.py --profile toy`, full mode.
  - `mutants`: `l2mutants.py --full`, which needs the first job's `preflight.json`. The 17 rule
    mutants run the whole full suite, the 2 equivalents run, and the 18 machinery mutants run
    `l2selftest.py`. A matrix by mutant is possible; the aggregation step then rebuilds
    `mutant-campaign.json` from the per-mutant JSON objects.
- **Output:** `mutant-campaign.json` (mode `full`, `code_digest`). A marker step,
  "mutant campaign passed for code_digest", has an `if:` on the step's exit status.

**B. `np-avg-1-stage0-v8` (the enumeration).**
- **Inputs:**
  - `authorization`, the artifact JSON;
  - `designation_comment`, the comment id;
  - `mutants_run`, the run id of a passing workflow A run.
- **Permissions:** `contents: read`, `issues: read`, `actions: read`.
- **Jobs**, each checking out exactly `github.sha` and running `python3 -I -B` with the pinned
  Python 3.13 patch version; every job's outputs record `GITHUB_RUN_ID` (§7, echo):
  1. `owner-check` (5 min).
     - It fails unless `github.sha` equals the artifact's `commit`.
     - It reads the comment through the API and writes `owner-check.json`: author login, body
       SHA-256, the exact-line test computed in the step, the commit.
     - Marker step: "owner designation verified".
  2. `dryrun` (10 min).
     - `l2calib.py`, then `l2plan.py --profile v8 --calib calib.json --out dryrun.json`, with
       `--shared-tips` only if the owner's F3 ruling uses it (the review recommends the count be
       computed before that decision, as combinatorics with no grant; it is not run in this draft).
     - Output `launch` = `cost.launch_within_budget`, under the owner's κ.
     - If `launch` is not true, no later job runs except `report-not-undertaken`, which writes the
       estimate as the result.
  3. `preflight` (30 min).
     - `l2preflight.py --profile v8`, full mode, with the artifact and owner check.
     - Downloads `mutant-campaign.json` from `mutants_run`.
  4. `s1a` (40 min): `l2s1a.py` normal and `-O`.
  5. `shard` (matrix s = 0…31, 40 min each, or two 20-minute replica jobs per shard): `l2enum.py`
     normal and `-O`.
  6. `merge` (20 min, `if: always()` after the shards).
     - Runs `l2merge.py` normal and `-O`, then `l2cert.py`.
     - Uploads `result.json`, `expected-controls.json`, `residue.json` if present, and
       `certificate.json`.
     - Marker step: "certificate holds".
- **Landing (L2-R4 c).** The evidence-retention pull request's check re-fetches the designation
  comment from the host, writes `fetched.json` and runs `l2landing.py`; the result lands only if it
  exits 0.
- **Verdicts** read the jobs' and steps' conclusions and these files only. The label is
  `result.json`'s `label`.
- **Retention (§A.42).** The evidence-retention pull request records under the record directory:
  `result.json` (the expected result), `expected-controls.json`, `certificate.json`, `fetched.json`,
  and a reproduce recipe (commit, commands, comparison). The shard files' digests are in
  `result.json` and `certificate.json`. Logs are diagnostics only.

## 12. Local evidence (`design/`)

Run by `code/l2run.py` with `python3 -I -B` on Python 3.13.16. Every step's stdout and stderr is in
`runs/`. `RUN-MANIFEST.json` records:
- commands, exit codes and durations;
- `-O` identity, by stdout or by the files written;
- SHA-256 values of code, outputs and toy-run files;
- the HEAD at run time and whether the Layer-2 tree was clean.

**Commit caveat (L2-R5).** The evidence was produced on an uncommitted working tree. The structured
files record the HEAD at run time and `tree_clean = false`; the commit binding holds among them (one
commit throughout), but that commit does not contain these files. They are design evidence only. At
the Layer-2 freeze the evidence is regenerated at a recorded commit.

| step | result |
| --- | --- |
| `manifest_verify` | the manifest matches |
| `l2_selftest` | 20 cases pass (L2-S1, GUARD, POST, ORB, AUTH, MAN, MRG, LBL, RT, C16, WIT, SURV, CERT, LAND, SAMPLE, MASK, PLAN, SHTIP, GATES, CFG) |
| `calibration_planted` | timings on planted sets (not deterministic) |
| `dryrun_toy` | 1,400 records, 488 orbits, 4 shards; masking-equivalent 1,398 in both readings; the complete estimate, with the C7 term for both candidate scopes from the toy shared-tip count; launch not decided (κ is a placeholder) |
| `dryrun_v8_plan_no_closure` | v8 shard plan without enumeration or closure: 5,163,225 records, 816,050 orbits (875 + 815,175), group order 8, 32 ranges; non-fixed context sizes up to 29 (37 with the fixed quantities); `closures_computed = 0` |
| `dryrun_v8_estimate` | see below |
| `preflight_toy_quick` | every pre-flight control passes (quick mode): refusal 46 of 46; C11 (i) 4,193 tables, (ii) 24 sets, (iii) 96 sets, 0 failures; both direction mutants fail C11; S6 pass; C12 on the toy universe |
| `mutants_quick` | 35 of 35 killed at their named cases: 17 rule mutants (L1 §6 table) and 18 machinery mutants, including the five r2 mutants `M_witness_first` (L2-WIT), `M_survivor_rep_only` (L2-SURV), `M_residue_ignored` (L2-MRG), `M_commits_unbound` (L2-CERT) and `M_grant_unbound` (L2-GUARD). The two demonstrations fail C11 only, with counts equal to the frozen rule's. `M_witness_max` also fails L2-LBL, L2-MRG and L2-RT, since its replacement does not skip empty shard minima |
| `s1a_toy` | status OK; reference checks pass on the L3′ and L3 bounds under A and G; toy L_A = 15, L_G = 7 (toy geometry, not a statement about v8) |
| `shard_toy_0`…`3` | 488 representatives, every gate at rate 1: C0 976, C7 976 (739 with a shared tip), C8 488 orbits, C9 2,800, C10 (i) 1,952, C11 (i) 976 (5,328 tables), C17 976, C18 976; 0 failures; no survivors |
| `merge_toy` | COLLAPSE_ALL on the toy class (design evidence, no statement); coverage exact; recount 1,400 and 488; residue complete; rule T evaluated |
| `certificate_toy` | items 1–8 hold, including the commit binding (item 3 with the quick campaign, which the toy profile admits) |
| `crosscheck_toy_counts` | all 54 merged counts equal code-r5's full per-record computation; 32 identically zero |
| `code_r5_equivalence_quick` | the quick suite equals code-r5's except the extended refusal block |
| `planted_survivor_path` | the survivor path on planted toy records (two orbits of 4): C0, C7, C11 (i), C17, C18 each run on all 8 members in both conventions (16 each), with 0 failures; C11 (ii) 16, C8 2; negative control: a bound missing one retained quantity gives C9 failures and a running-minimum witness confirmed by direct closure |
| `refusal_probe_v8` | 9 of 9 entry-point attempts refused with VOID and item 6, before any file is written; 9 of 9 forgeries refused (the review's direct `V8Grant` and `RefGrant`, before and after the running digests are bound, the r1 `RefGrant` signature, and a rebinding); `decide()` on fabricated inputs returns `ok`, recorded as the documented limit |

Every deterministic step is `-O`-identical.

**Not run locally, pending.**
- The full mutant campaign: the full suite for every rule mutant, and the equivalent mutants. It is
  CI-only and needs an owner-approved dispatch.
- The full-depth control suite (C1 F 0–15, B 0–8, G 0–23, …). It runs in CI pre-flight.
- `l2plan --shared-tips` on v8 (part of the owner's F3 decision).
- Everything on v8's class.

**The v8 cost estimate** from this calibration (planted sets on this machine; timings vary between
runs; `runs/dryrun_v8_estimate.out`), in runner-seconds:

| term | runner-seconds |
| --- | --- |
| closures (with overhead 2 and the `-O` copy) | 59,190 |
| sampled gates (C7, C11 (i), C17, C18 at 1 in 1,000; C8 at 1 in 100) | 2,591 |
| survivor gates, capped at 10 orbits per shard | 7,794 |
| S1a | 348 |
| pre-flight | 300 |
| merge | 600 |
| **total without the C7 scope term** | **70,821 (about 19.7 h)** |
| C7 under the chosen scope | pending (F3): 350 s (A) and 1,495 s (G) per percent of representatives with a shared tip |

At the toy class's literal-reading shares (about 76 % under A and 48 % under G; the v8 shares are not
computed) the C7 term alone would be about 98,000 runner-seconds. No launch decision is computed: κ
and the C7 scope are placeholders. The per-shard job estimate is likewise pending the C7 term.

## 13. Findings: status after the review

**Rule T** (review §2).
- **T1, T2, T5:** owner ruling needed (an append-only Layer-1 erratum before the Layer-2 freeze and
  before any S1a output). Layer 2 implements the review's recommended readings meanwhile (§4.2).
- **T3** (cost clause not evaluable in Stage 0) and **T4** (citations: L1 §1, §2, PO7 besides PO4):
  notes for the erratum; no change needed in Layer 2.

**Other findings.**
- **F1:** accepted reading (§4.1).
- **F2:** moot while F1 holds; to be fixed in any BASE_RESIDUE amendment.
- **F3:** owner decision (C7's scope), with an append-only amendment to C7's pass condition. The
  estimate now prices each candidate scope (§3.6, §12); the v8 shared-tip count is not computed in
  this draft.
- **F4, F5, F7, F8, F10, F11:** accepted readings (§4.1).
- **F6:** owner decision (C8's list or a 4-count erratum).
- **F9:** owner decision on κ and the budget (S7); the half-budget threshold of r1 is removed.

## 14. Freezing Layer 2

After the re-review, and once the owner has ruled on T1, T2, T5, F3, κ and F6:
1. Replace the placeholders in `l2config` with the rulings, and apply any accepted changes.
2. Regenerate `LAYER2-MANIFEST.json`, commit, and re-run `l2run.py` at that recorded commit, so that
   the design evidence's commit is the freeze commit's parent or the freeze commit itself, as the
   freeze note states.
3. Record the plan's SHA-256, the manifest's `code_digest` and the configuration digest in a freeze
   note.

Before any v8 dispatch, the owner then makes three separate decisions: the workflow edit, the full
mutant campaign, and the enumeration itself, by an authorization artifact naming the frozen commit
and `code_digest`.

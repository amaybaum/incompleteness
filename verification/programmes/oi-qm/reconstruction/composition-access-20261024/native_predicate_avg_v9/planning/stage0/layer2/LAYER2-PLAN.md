# NP-AVG-1 Stage 0, Layer 2: implementation plan (draft for independent review)

**Status: WIP / UNREVIEWED, not frozen. The v8 enumeration is not authorized.** Nothing in this
directory has run on v8's configuration class. v8 setups are constructed only to check that they
are refused, and v8's record space is used only for combinatorics (counts, orbits, shard ranges and
context sizes), with no context constructed and no closure computed.

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
ambiguous, the reading Layer 2 implements is stated where it is used, and every such point is listed
in §13 for the reviewer. None of them is resolved by editing a frozen file.

**What a bounded run shows.** The local evidence (§12) runs on toy, planted and small-window
instances, on S6's 21-bit carrier and on v8 combinatorics only. It shows that the code runs, that the
controls can fail and that the toy outputs agree with an independent computation. It proves nothing
about v8's class. The statuses in the proof-obligation table (§9) are those of this draft: "proved
here" means an argument is written in this plan and has not yet been reviewed.

## 1. Files

`code/` (production, reference and controls; standard library only, Python 3.13):

| file | role |
| --- | --- |
| `s0geom.py` | production engine: contexts, cones, tips, the L3/L3′ closure, `analyse` (copied from code-r5, §2) |
| `s0ref.py` | independent reference closure, contexts, direction tables, P_A/P_G checks (copied, §2) |
| `s0native.py` | independent native evaluator (copied unchanged) |
| `s0controls.py` | the control suite C0–C18, refusal, native self-test (copied, §2) |
| `s0s6.py`, `s0symcheck.py` | S6 proof-check; C0's v8 combinatorics (copied unchanged) |
| `l2config.py` | every configuration constant; `config_sha256()` |
| `l2manifest.py`, `LAYER2-MANIFEST.json` | code SHA-256 values, configuration digest, `code_digest` (certificate item 1) |
| `l2auth.py` | the v8 authorization: `decide()` and `issue_grant()` (item 6) |
| `l2analysis.py` | C4v group, canonical representatives, orbits, `post_closure`, degeneracies, the 54 counts, structure attributes |
| `l2refcheck.py` | in-run reference gates C7, C11 (i), C11 (ii), C17, C18; imports only `s0ref` |
| `l2plan.py` | the dry run: index space, Burnside orbit count, shard plan, context sizes, cost estimate; imports no engine |
| `l2calib.py` | timing calibration on planted sets for the estimate |
| `l2preflight.py` | pre-flight controls (item 2) |
| `l2mutants.py` | the mutant campaign, quick (local) and full (CI) (item 3) |
| `l2s1a.py` | the S1a driver: global bound, per-line closures, L_A, L_G |
| `l2enum.py` | the record driver and per-record analysis, one shard per run |
| `l2merge.py` | the merge, the label generator, rule T |
| `l2cert.py` | start-up checks and the certificate builder (items 1–8) |
| `l2selftest.py` | controls of the Layer-2 machinery and its 13 machinery mutants |
| `l2run.py` | the bounded local evidence driver |

`design/`: the design-evidence scripts (`planted_shard.py`, `refusal_probe.py`, `crosscheck.py`,
`r5_equivalence.py`), the retained stdout and stderr of every step in `runs/`, the toy run's
structured files in `toyrun/`, and `RUN-MANIFEST.json` and `.md` (commands, exit codes, `-O`
identity, SHA-256 values of code, outputs and toy-run files).

## 2. Provenance of the copied code

Each file was copied from `stage0/code-r5/` at `f33d8d63`; nothing is imported across directories.

| file | source blob at `f33d8d63` | source SHA-256 | Layer-2 change |
| --- | --- | --- | --- |
| `s0native.py` | `47a5e394` | `4206549e…8526` | none (byte-identical) |
| `s0s6.py` | `a92eae87` | `110f275c…289a` | none (byte-identical) |
| `s0symcheck.py` | `5b64720b` | `ffe390ae…18f2` | none (byte-identical) |
| `s0geom.py` | `231272ab` | `1b076aea…a867` | (a) the v8 guard: `_guard(setup, auth)`, a module function that accepts only the exact `Setup` type, reads `(dim, n, port)` from the attributes and compares with the literal `(3, 6, (0, 0, -3))`; the refusal is lifted only by an exact `V8Grant` instance with well-formed fields, so `authorized_v8=True` is refused; (b) `Context` memoizes the G eligibility test per (pair, frame sources). Geometry, closure, `Rule` and `analyse` unchanged |
| `s0ref.py` | `62c6dfb0` | `39ef1d46…b227` | `ref_context`'s refusal is lifted only by an exact `RefGrant` instance |
| `s0controls.py` | `29790f8a` | `e8c40a5d…1a43` | `--only` (targeted mutant runs); the refusal check extended by ten Layer-2 attempts (46 in all); C14 extended to `l2analysis.py` and `l2refcheck.py`. Every control body otherwise unchanged |

The SHA-256 values of the Layer-2 files are in `code/LAYER2-MANIFEST.json` and
`design/RUN-MANIFEST.json`.

**Behaviour preserved.** Step `code_r5_equivalence_quick` runs code-r5's own quick suite and compares
its JSON with the Layer-2 suite's: every control agrees except the refusal block, which Layer 2
extends (§12). That is a toy-class check of change (b) and of the guard edit, not a proof; PO-L2-8
gives the argument for (b).

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

For survivor representatives the shard also records the §3 structure: the survivor sets, linkage,
(b) sets, per-member G-linkage and source cells, shared aligned tips, cover-graph components,
residual support (Layer-2 definition, §4), and rule dependence.

### 3.3 In-run gates (item 4)

| gate | runs on | verdict class on failure |
| --- | --- | --- |
| C0 (contexts) | every representative where a reference context is built: production context equals `s0ref`'s | VOID |
| C7 | every survivor representative; every representative with a shared tip (§4); a 1-in-1,000 sample | VOID |
| C8 | every survivor orbit; every orbit with a mismatch; a 1-in-100 sample of orbits: every member's closures computed directly and compared with the carried ones, attribute by attribute, and its count contributions compared | VOID |
| C9 | every record (every member, carried): ret_L3′ ⊆ ret_L3, and each within the S1a bound of its rule | MISMATCH |
| C10 (i) | every closure: no fixed quantity in a log | MISMATCH (L1 §5, "a fixed quantity is eliminated") |
| C11 (i) | every survivor representative; a 1-in-1,000 sample | VOID |
| C11 (ii) | every survivor record (members, carried): P_A-dir and P_A (A), P_G-dir and P_G (G), by `s0ref` | MISMATCH |
| C17, C18 | every survivor representative; a 1-in-1,000 sample each | VOID |

Samples are deterministic: representative index i is sampled for gate X at rate R iff
SHA-256(salt | X | i), read as an integer from its first eight bytes, is 0 mod R. The salt and rates
are configuration constants (item 1). L1 fixes C7's rate (1 in 1,000) and C8's (1 in 100); C11 (i),
C17 and C18 are "a deterministic sample" in L1, and Layer 2 sets each to 1 in 1,000 (§13, F8).

Minimal witness (item 4, C16): when any MISMATCH condition holds on a representative, every member's
closures are recomputed directly, the condition is re-evaluated on each, and each confirmed record is
a candidate with key (k, number of even-class context quantities, sorted items). The merge selects
the minimum.

### 3.4 S1a driver (item 5)

`l2s1a.py` computes the closures of U = {(x, 23) : x ∈ Reg}, whose context is the union of every
item's samples, under A and G with L3′ and L3 (the C9 bounds), and the L3′ closures of the items on
each of the 123 axis-parallel lines meeting Reg (reported only, N5). It writes L_A and L_G from the
L3′ bounds, and their L3 values beside them (reported only). Its own validity checks: C17 and C18
with the reference on the L3′ bounds and C0 contexts (VOID on failure), and C10 (i) and
ret_L3′ ⊆ ret_L3 on the bounds (MISMATCH). The reference checks stream one explicit cone at a time
(`l2refcheck.cover_index`), since the bound has about 1,600 quantities.

### 3.5 Sharding and the stop rule (S7)

| job | timeout |
| --- | --- |
| dry run | 10 min |
| pre-flight | 30 min |
| S1a (normal and `-O`) | 40 min |
| each of 32 shards (normal and `-O`) | 40 min |
| merge and certificate | 20 min |

The timeouts sum to 23 h (1,380 runner-minutes), within S7's 24 runner-hours over at most 32 shards. The stop rule:

1. **Before launch.** The dry run's cost estimate must be at most half the budget in total and at
   most half the shard timeout per shard (configuration constants). Otherwise the run is not
   launched and the estimate goes to the owner.
2. **During the run.** A shard that reaches its timeout is cancelled by the host; its file is
   missing, and the merge labels the run INCOMPLETE. Nothing is retried automatically.
3. **After a stop.** A re-dispatch is a new owner decision (§A.43 item 4).

The full mutant campaign is a separate dispatch with its own budget: about 33 minutes locally on the
r3 measurements (L1 §10), plus the 13 machinery mutants at a few seconds each. It is not counted in
the 24 hours.

### 3.6 Dry run and cost estimate

The dry run (`l2plan.py`) is mandatory: every computing entry point refuses to run without a
`dryrun.json` for the same configuration with `closures_computed = 0` (certificate item 7). It imports
neither engine nor reference; it constructs no context and calls no guarded entry point. Its formulas
are checked against the engine on the toy class (L2-PLAN, L2-MASK, L2-SHTIP).

It prints:
- N;
- the Burnside orbit count;
- the shard plan;
- the histogram of non-fixed context sizes over all records, from per-item sample counts by
  convolution, with no record enumerated;
- for the toy profile only, the masking-equivalent count. On v8 that is a reported count, computed
  by the authorized merge.

In CI it also runs with `--shared-tips`, which enumerates the record space combinatorially, with no
closure, to count the representatives C7 must check under §4's reading.

**Estimate.** In runner-seconds:

    Σ_m count(m) · (orbits/N) · [2 t_A(m) + 2 t_G(m)] · overhead · 2

- t_A(m) and t_G(m) are measured by `l2calib.py` on planted sets of m quantities, drawn from a
  displaced ball, with a planted frame under G. Only timings are recorded.
- The factor 2 at the end is the `-O` run.
- `overhead` (2, a configuration constant) covers the analysis, the member attributes and the
  sampled gates.
- Survivor gates and C7 on shared-tip representatives are excluded and reported separately: their
  cost depends on counts known only in the run.

The local figures are in §12. They do not meet launch condition 1.

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

**Counts.**
- The additive counts are summed.
- Observer classes are Σ |orbit(K)| over the distinct canonical public sets K, per convention and
  category (PO-L2-5).
- `masking_equivalent_records` is computed by the analytic formula of PO-L2-6, in the L1 reading
  (§4).

**Labels** (L1 §5), first match:
1. **VOID:** a pre-flight control of VOID class, a VOID gate, the manifest, or the authorization fails.
2. **MISMATCH:** C6's execution instances, C9, C10 (i), C10 (ii), C11 (ii) or C12 fails.
3. **INCOMPLETE.**
4. **BASE_RESIDUE.**
5. **COLLAPSE_ALL.**
6. **RESIDUE_UNLINKED:** survivors exist, and none is Φ-linked under A or G-linked under G.
7. **RESIDUE.**

**Rule T** is evaluated as in §8.

## 4. Layer-2 readings where Layer 1 does not fix a value

| point | Layer-2 reading | where |
| --- | --- | --- |
| "record containing a shared tip" (C7) | in the record's initial context, under that convention's pair, some cell is the e-near-tip of two distinct non-fixed quantities for the same direction e (`C7_shared_tip_scope = 'initial_context'`, the literal reading) | `l2analysis.shared_near_tip` |
| residual support (L1 §3) | under A, 3 bits per pair cell in Φ's seven cells ∪ the cones of S_A; under G, 3 bits per seed in the union of the cones of S_G; compared with S_max = 27; reported only | `l2analysis.residual_support_bits` |
| masking equivalence (E2) | equal even-class contexts, with E1 merges (fixed quantities and port samples identified), as L1 §1 states; code-r5's record-sample keying is reported beside it | `l2plan.masking_equivalent` |
| C11 (i), C17, C18 sample rates | 1 in 1,000 each, plus every survivor | `l2config` |
| S1a's own status (rule T's precondition) | VOID if pre-flight fails or S1a's reference checks fail; MISMATCH if S1a's C10 (i) or L3′ ⊆ L3 fails on the bound, or any shard's C9 fails against the bound; INCOMPLETE if `s1a.json` is missing, has differing digests or differs under `-O` | `l2s1a.run`, `l2merge.merge` |
| rule of rule T's bound | L3′ (the label rule, S2); L3 values reported | `l2s1a.run` |
| base-relative survivors (BASE_RESIDUE) | literal: retained set contains a quantity outside ret(∅); reported only under BASE_RESIDUE | `l2enum.Shard.rep` |
| C12's per-record clause | checked once on the universe of quantities, which covers every record (PO-L2-9) | `l2preflight.c12_universe` |

## 5. Structured outputs (§A.44)

Every verdict reads exit statuses and these files. No log text is read. Where printed output carries
a fact (pre-flight's subprocesses), the producing step parses the JSON object that the subprocess
prints as its whole stdout and records its exit status; a non-JSON stdout counts as failure. The
schema names are recorded in each file.

| file | schema | content |
| --- | --- | --- |
| `dryrun.json` | `…/dryrun/1` | records, orbits (single, pair), group order, shard plan [{shard, lo, hi, count}], context-size histograms, max context size, `closures_computed: 0`, `contexts_constructed: 0`, configuration digest, optional `cost` and `shared_tip_records`, expected checks, `pass` |
| `preflight.json` | `…/preflight/1` | profile, mode, `code_digest`, configuration digest, commit, `controls` {name: {pass, class, …}}, `base_collapsed` {A, G}, the full control-suite, self-test and S6 objects, `pass` |
| `mutant-campaign.json` | `…/mutant-campaign/1` | mode, `code_digest`, the unmodified-suite precondition, per mutant {named case, exit, failed, killed, run}, demonstration fields, killed/total, `pass` |
| `s1a.json` | `…/s1a/1` | bounds per (convention, rule) as flat integer lists, sizes, L_A, L_G, L3 values, linked quantities, per-line results, checks, `status`, reasons, digests, commit, `sha256` |
| `shard-<s>.json` | `…/shard/1` | profile, shard, range, records, scanned, representatives, orbit weight, digests (code, config, dry run, S1a), commit, authorization echo, base retained sets, additive counts, canonical class keys with orbit sizes, base-relative and L3-only tallies, gate tallies and first failures, witness candidates, survivor detail, `sha256` (of the canonical JSON without it) |
| `result.json` | `…/result/1` | label, `label_source`, VOID/MISMATCH/INCOMPLETE reasons, base precondition, 54 counts, record-sample masking reading, structure tallies, in-run gate totals, minimal witness, coverage, S1a {status, L_A, L_G, L3 values, bound sizes, lines}, `rule_T`, authorization echo, digests, commit, coverage limits (L1 §11), input digests, residue file digest |
| `expected-controls.json` | `…/expected-controls/1` | the hand-derived and recorded expected values (`l2config.CONFIG['expected']`) and the observed pre-flight results |
| `residue.json` | `…/residue/1` | survivor representatives with the §3 structure (only when survivors exist) |
| `certificate.json` | `…/certificate/1` | items 1–8, each with `holds` and its evidence; `holds` overall |

All files are canonical JSON, with sorted keys and integers and strings only. Normal and `-O` runs
write byte-identical shard, S1a and result files (item 7).

## 6. The execution certificate (L1 §5b item 8)

| item | implementation | fails closed by |
| --- | --- | --- |
| 1 frozen manifest | `l2manifest.verify`: every `.py` SHA-256, the configuration digest and `code_digest` equal `LAYER2-MANIFEST.json`, and `vars(Rule())` equals the configuration's rule fields; run by `l2cert.startup` before anything is computed | printing VOID and exit 2 |
| 2 pre-flight | `l2preflight.py` in the same job and commit: the full control suite (C0–C3, C6, C7–C18, refusal, native self-test), the two C11 direction mutants (each must fail C11), S6, C0's v8 combinatorics, the Layer-2 self-test, C12 on the universe, and for v8 C6's execution instances and C10 (ii) | startup refusing without a passing `preflight.json` for this `code_digest` |
| 3 mutant campaign | `l2mutants.py --full` in CI; startup refuses without a passing `mutant-campaign.json` with mode `full` for this `code_digest` | VOID, exit 2 |
| 4 in-run gates | §3.3 | VOID or MISMATCH in the merge, never a label of their own |
| 5 merge | §3.7 | INCOMPLETE |
| 6 authorization | §7 | VOID, exit 2, before any context exists |
| 7 determinism | normal and `-O` shard, S1a and result files compared byte for byte; dry run mandatory | INCOMPLETE (shards, S1a); certificate item fails (result) |
| 8 labels | only `l2merge.label`, from structured files; `label_source` recorded | — |

`l2cert.py --build` writes `certificate.json` from the files alone. A certificate that holds attests
that the run followed Layer 2. It does not turn the label into a proof.

## 7. The v8 lock

- **Content-keyed refusal, kept.** `Context`, `num_records`, `record_at` and `record_samples` refuse
  any `Setup` whose (dim, n, port) equal (3, 6, (0, 0, −3)), whatever its region, slice range or
  sources. The comparison is against a literal, and the port is compared as a tuple. `s0ref.ref_context`
  does the same. A `Setup` subclass is refused.
- **Default refuses.** The refusal is lifted only by an exact `V8Grant` (engine) and `RefGrant`
  (reference), with well-formed fields. `True`, other truthy values, duck-typed objects, subclass
  instances and uninitialized instances are refused (refusal check, 46 attempts; L2-GUARD).
- **Who can grant.** Only `l2auth.issue_grant` constructs a grant. Static check L2-S1 verifies that
  no other file does, and that production modules pass to the guarded entry points only a variable
  named `grant` or `refgrant`. `issue_grant` mints only when `decide()` returns `ok` on three inputs.
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
- **Testing.** `decide()` is pure, so each of its 17 refusal paths is tested without minting
  (L2-AUTH). The design evidence never constructs a valid grant.
- **Limit.** A Python process cannot exclude in-process tampering, such as monkeypatching the guard.
  The gate against that is the manifest (item 1), the CI job running only the frozen entry points,
  and the host-side owner check. The mutant `M_guard_truthy` shows that weakening the guard is
  caught by L2-GUARD.
- **The dry run.** `l2plan.py` runs for v8 without a grant. It never reaches a guarded entry point,
  and it computes combinatorics only.

## 8. Rule T, as frozen (provisional wording)

**Implementation.** `l2merge.rule_T(s1a_status, L_A, L_G)`, a function of those three values only:

| case | outcome | recorded consequence |
| --- | --- | --- |
| S1a status not OK | `not_evaluated` | S1b and S1c not proposed (L1 text verbatim) |
| L_A = 0 and L_G = 0 | `L_A = L_G = 0` | the L1 text verbatim, the geometric fact only, no law statement for k > 2; S1b and S1c not undertaken |
| L_A > 0 or L_G > 0 | `L_A > 0 or L_G > 0` | S1b put to the owner as a new preregistration (L1 text verbatim) |

`wording_status` is recorded as "provisional: retained pending owner confirmation". The cost clause
is recorded as not evaluable in Stage 0 (§13, T3).

**Neutrality** is tested in two ways (L2-RT). The function's signature contains no label. Through the
merge, the outcome is the same under COLLAPSE_ALL, RESIDUE_UNLINKED, RESIDUE and BASE_RESIDUE.

**The argument for the L_A = L_G = 0 consequence (PO-L2-7).** It is stated for the reviewer to test.
Let R be any finite set of items in Reg × {−1, …, 23}, and U = {(x, 23) : x ∈ Reg}.

1. **Nesting.** The samples of an item (x, t) are the even-class site-times (x, s) with −1 ≤ s ≤ t,
   a subset of the samples of (x, 23). The fixed quantities and port samples are the same in every
   context. So Ctx(R) ⊆ Ctx(U). (From L1 §1's definition of Ctx.)
2. **Monotonicity.** By PO4 (a larger context retains a superset), ret(R) ⊆ ret(U), under A and
   under G, for L3′. Under G the eligibility predicate is the same for both contexts, because the
   frame is the union of the G cones of Φ, V, p and the even port samples. These are in every
   context and do not depend on the record (L1 §2).
3. **Linked survivors.**
   - Under A, S_A(R) = ret_A(R) ⊆ ret_A(U). R has a Φ-linked survivor iff some q ∈ S_A(R) has a Φ
     cell in its cone. Such a q is counted by L_A.
   - Under G, S_G(R) is the set of q ∈ ret_G(R) with a seed tip. Whether q has a seed tip depends
     only on q and the frame, so S_G(R) is contained in the quantities of ret_G(U) with a seed tip.
     R is G-linked iff some q ∈ S_G(R) has a source cell in its cone. Such a q is counted by L_G.
4. Hence L_A = 0 implies that no such R has a Φ-linked (in particular J-linked) survivor under A, and
   L_G = 0 implies that no such R has a G-linked survivor under G.

The argument uses PO4 and two facts that rule T does not cite: step 1, and the record-independence of
the frame in step 2. Both are read from L1's definitions, not from a proof obligation. The converse
does not hold and is not used: L_A > 0 does not imply that any record has a linked survivor.

**What the reviewer is asked to test.**
1. Is rule T unambiguous as written? §13 lists T1–T5.
2. Does the argument above follow from the frozen assumptions alone?
3. Is the Layer-2 definition of S1a's status (§4) admissible under rule T's neutrality clause? It
   makes rule T wait for the shards' C9 results, which are not the k ≤ 2 label.

## 9. Proof obligations of Layer 2

| id | statement | status |
| --- | --- | --- |
| PO-L2-1 | `record_at` is a bijection from [0, N) onto the record space (singles; unordered two-site pairs with independent slices), and the shard ranges are a disjoint exact cover of [0, N) | **Proved here, unreviewed.** Ranges: ⌊sN/S⌋ is non-decreasing and runs from 0 to N. Bijection: singles index the item list directly; for pairs, idx ↦ (sp, rest) = divmod(idx, 25²) is a bijection onto [0, C(129, 2)) × [0, 625); the loop decodes sp to the sp-th pair (i < j) in lexicographic order, the standard unranking; rest ↦ (t1, t2) is a bijection. **Checked:** toy, C13 recount and L2-ORB. v8 is not enumerated locally |
| PO-L2-2 | Keeping exactly the records equal to their canonical image keeps one record per C4v orbit; the orbit weights then sum to N, and the representatives number the orbits | **Proved here.** The canonical image is a function of the orbit, and it is an element of the orbit, so each orbit has exactly one fixed point of "equals its canonical image". **Checked** in every run by the merge's recount against Burnside's count; toy: 488 and 1,400 |
| PO-L2-3 | Equivariance: ret(gR) = g·ret(R) for g ∈ C4v, under A and G, for L3′ and L3 | **Proved here, from L1 PO4 and §1 E4.** g is a signed coordinate permutation fixing the slices, q9, Φ's site set, the port and Reg, so it maps the fixed quantities, port samples, cones, tips, the frame and eligibility to themselves. Hence S is self-supporting in Ctx(R) iff gS is self-supporting in Ctx(gR), and by PO4 the closure is the greatest self-supporting subset. **Checked** in-run by C8 on sampled and survivor orbits; on toy, all 488 orbits |
| PO-L2-4 | `post_closure(ctx_gR, g·ret(R))` equals `analyse(ctx_gR)` | **Follows from PO-L2-3:** `post_closure` is `analyse`'s code after the closure. **Checked:** L2-POST, all toy records, both conventions, both rules; C8 in-run |
| PO-L2-5 | The merged counts equal the full per-record computation. Additive counts: sum of per-member contributions. Observer classes: Σ |orbit(K)| over distinct canonical public sets K | **Proved here, given PO-L2-3:** public(gR) = g·public(R), so the classes met by an orbit are exactly the orbit of its representative's public set; orbits of sets partition the classes. **Checked:** toy, all 54 counts equal to code-r5's full computation (`crosscheck`) |
| PO-L2-6 | Masking equivalence (L1 reading): map an item to (x, m), m the largest slice of its non-fixed, non-port sample set, dropping items whose set is empty. Two records have equal contexts iff their canonical forms are equal; class sizes follow by counting | **Proved here.** The set of an item is {(x, s): s ≤ m, parity} minus the removed cells at x, so it is determined by (x, m); distinct sites give disjoint sets. **Checked:** brute force on three toy variants, in both readings (L2-MASK) |
| PO-L2-7 | Rule T's L_A = L_G = 0 consequence (§8) | **Argued here, from L1 PO4 and L1 §1–§2 definitions; for independent review (owner instruction)** |
| PO-L2-8 | Memoizing the G eligibility per (pair, frame sources) does not change any result | **Proved here:** eligibility is a function of (pair, frame sources, u), and the cache is keyed by the first two. **Checked:** quick suite identical to code-r5's except the refusal block |
| PO-L2-9 | C12 on the universe covers every record: every context is contained in the universe together with the fixed quantities, and "in-frame with its cone inside the frame" is a property of the quantity | **Proved here** (as PO-L2-7 step 1) |
| PO-L2-10 | The minimal witness found is minimal over all MISMATCH records | **Follows from PO-L2-3.** The MISMATCH conditions are C4v-invariant: the bound is invariant because U is; P_A-dir and P_G-dir permute directions; so every MISMATCH record lies in a flagged orbit, and the shard confirms each member by direct closure |
| PO-L2-11 | Normal and `-O` runs give identical outputs | **Not proved; checked per shard.** No control logic uses `assert` in Layer-2 modules; iteration over integer tuples does not depend on hash seeds. `s0symcheck.py` relies on `assert`, so pre-flight always runs it without `-O` |
| PO-L2-12 | The S1a bounds are C9 bounds: ret(R) ⊆ ret(U) for every record | **Follows from L1 PO4** (PO-L2-7 steps 1–2) |
| PO-L2-13 | The dry run's formulas (N, Burnside, context histogram, shared-tip count) equal the engine's | **Checked on toy only** (L2-PLAN, L2-SHTIP); for v8 they rest on the same code |

Nothing in this table is claimed beyond its status. "Checked" items are evidence on the instances
named, not proofs.

## 10. Invariant → checkpoint (§A.41)

**Layer-1 invariants** (L1 §7). For each: the implementing code, its checkpoint in Layer 2, and the
local evidence (§12).

| L1 invariant | code | Layer-2 checkpoint | local evidence |
| --- | --- | --- | --- |
| configuration space and counts | `s0symcheck`, `l2plan.Space` | pre-flight `C0_v8_combinatorics`; dry run `expected_checks`; merge recount | symcheck exit 0; v8 dry run: 5,163,225 records, 816,050 orbits, group order 8 |
| C4v with correct orbit counts | `l2analysis.group`, `l2plan.orbits_burnside` | L2-ORB; merge recount | toy 488/1,400 |
| orbit representatives preserve every reported count; per-record results for invariant attributes | `l2enum.Shard.rep`, `l2analysis` | in-run C8 (1/100 orbits, survivor orbits, mismatch orbits); merge recount | toy: all orbits, 0 failures; 54 counts equal to full computation |
| source-dependent attributes per record | `l2analysis.post_closure` per member | C8 compares `g_linked` and `source_cells` with direct closure | toy C8 in-run, 0 failures |
| cones match the native rule | `s0geom.in_cone` | pre-flight C1 (full depths in CI) | quick C1: 5,000 perturbations, pass |
| tips bijective, off-axis not | `s0geom.tip_labels` | pre-flight C2 | quick: 133 tips, 8 contrasts |
| planted families survive; planted non-survivors collapse | — | pre-flight C3, C11 (iii) | quick C3 block (8, 0); C11 (iii) 96 sets, 0 failures |
| elimination exact | `s0native` | pre-flight C15 | quick: 0 violations (2^21, 2^18 worlds) |
| every logged elimination justified | `l2refcheck.c18` | pre-flight C18; in-run C18 (1/1,000, survivors); S1a C18 | toy in-run 976 checks, 0 |
| every required elimination applied | `l2refcheck.c17`, `c7` | pre-flight C17, C7; in-run C17, C7; the unapplied-elimination mutant | killed at C17 |
| every eligible configuration considered | `l2enum.scan`, `l2merge.coverage_ok`, `recount_ok` | merge coverage and recount; C13; M_skip_index | killed at L2-ORB |
| planted survivors vs non-survivors (B, G, Φ- and frame-adjacent) | — | pre-flight C3, C6, C11 (iii) | pass |
| S6 | `s0s6` | pre-flight S6 | pass; positive control holds; negative control 64 non-target classes |
| v8 not run without authorization; refusal keyed on (dim, n, port) | `s0geom._guard`, `s0ref._ref_granted`, `l2auth`, `l2cert.startup` | refusal check (46); L2-GUARD; L2-AUTH; L2-S1; `refusal_probe` | 46/46; 9/9 entry-point attempts refused |
| frozen code and configuration are the ones run | `l2manifest`, `l2cert.startup` | items 1–3 at start-up; L2-MAN | M_manifest_blind killed |
| no over-elimination in any convention, type or depth | — | C3, C15, C11 (i) and (iii), mutants | quick campaign 17/17 rule mutants |
| far tips load-bearing beyond L3 | — | C3 block minus centre; near-only mutant | killed at C3 |
| closure correct by independent code | `l2refcheck.c7` | pre-flight C6, C7; in-run C7 | toy in-run 976 checks, 0 |
| base context collapsed | `l2preflight.v8_execution` (v8); C6 toy | pre-flight `C6_execution` (MISMATCH); `base_collapsed` | toy base collapsed |
| monotonicity | `l2enum.c9_ok` | pre-flight C9; in-run C9 per member; S1a L3′ ⊆ L3 | toy in-run 2,800 checks, 0; M_c9_off killed |
| no fixed quantity eliminated | `l2enum.c10i_ok` | in-run C10 (i) on every closure (MISMATCH) | 1,952 checks, 0 |
| port samples in-frame under G | `l2preflight` | pre-flight C10 (ii) (toy), `C10ii_v8` (v8) | toy pass |
| per-direction tables match and decisions agree | `l2refcheck.c11i` | pre-flight C11 (i); in-run C11 (i) | toy in-run 5,328 tables, 0 |
| P_A-dir, P_G-dir, P_A, P_G on survivors and planted sets | `l2refcheck.props` | pre-flight C11 (ii); in-run C11 (ii) on every survivor member | planted survivor run: 16 checks, 0 |
| planted directional retention | — | pre-flight C11 (iii) | 96 sets, 0 failures |
| per-direction control detects single-direction errors | — | pre-flight non-vacuity mutants; quick campaign | both demonstrations fail C11 only |
| every proof-dependent rule rests on a complete statement | — | document property; §9 for Layer 2's own | independent review |
| rule T applied as preregistered | `l2merge.rule_T` | `result.json` `rule_T`; L2-RT; M_ruleT_or | toy: evaluated, recorded |
| frame is B8; in-frame cones stay in it | `l2preflight.c12_universe` | pre-flight C12, `C12_universe` | toy: 129 = 129, 15 in-frame quantities checked |
| design evidence retained and deterministic | `l2run` | `RUN-MANIFEST`, `-O` identity | §12 |
| Layer-2 evidence structured, complete, retained | `l2merge`, `l2cert` | items 5, 7, 8; certificate | toy certificate holds |
| integer-only, no repository read in the engine | — | C14 (extended) | pass |
| minimal witness well defined | `l2merge.minimal_witness` | C16; L2-C16; planted negative control | M_witness_max killed |
| distinguishability classes (a)–(c) | `l2analysis.post_closure`, canonical keys | C8 (invariant parts), C7 | toy |
| every control can fail | — | the mutant campaign, quick now and full in CI | 30/30 quick |

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
| C13 | `s0controls.c13_coverage`; `l2merge.coverage_ok`, `recount_ok`; `l2run` retention | pre-flight; merge | INCOMPLETE (coverage); VOID (suite) |
| C14 | `s0controls.c14_static` (extended); L2-S1 | pre-flight | VOID |
| C15 | `s0controls.c15_exact` | pre-flight | VOID |
| C16 | `s0controls.c16_witness`; `l2merge.minimal_witness`; witness candidates in `l2enum` | pre-flight; merge | VOID (self-test) |
| C17, C18 | `s0controls.c17_fixed_point`, `c18_audit`; `l2refcheck.c17`, `c18`, `c17_stream`, `c18_stream` | pre-flight; in-run; S1a | VOID |
| refusal | `s0controls.refusal` (46 attempts); `l2selftest` L2-GUARD, L2-AUTH; `l2cert.startup` | pre-flight; every entry point | VOID |
| native self-test | `s0controls.native_self_test` | pre-flight | VOID |
| S6 | `s0s6.py` | pre-flight | VOID |

**Layer-2 invariants**:

| invariant | checkpoint |
| --- | --- |
| a grant exists only via `l2auth` | L2-S1 (static); L2-GUARD; M_guard_truthy |
| the authorization binds commit, code, configuration and owner | L2-AUTH (17 refusal cases, one accepting case, no mint); M_auth_no_commit |
| the dry run computes no closure | `closures_computed = 0` in `dryrun.json`, checked by start-up; L2-S1 (no engine import) |
| the carried attributes equal direct ones | L2-POST; C8 in-run |
| shard coverage and recount | merge; L2-MRG (six refusal cases); M_merge_no_coverage, M_skip_index, M_every_record_rep |
| label precedence | L2-LBL (11 cases); M_label_mismatch_first |
| sampling is deterministic and non-empty | L2-SAMPLE; M_sampler_never |
| masking count reading | L2-MASK (three toy variants, both readings); M_mask_no_merge |
| behaviour of the copied engine preserved | `code_r5_equivalence_quick` |

## 11. CI workflow design (proposal only; no file is added under `.github/`)

Two dispatch-only workflows, each launched only on the owner's separate approval (§A.43 item 4), on
a branch whose head is the frozen Layer-2 commit.

**A. `np-avg-1-stage0-mutants` (the full campaign, item 3).**
- **Inputs:** none.
- **Jobs:**
  - `preflight-toy`: `l2preflight.py --profile toy`, full mode.
  - `mutants`: `l2mutants.py --full`, which needs the first job's `preflight.json`. The 17 rule
    mutants run the whole full suite, the 2 equivalents run, and the 13 machinery mutants run
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
  Python 3.13 patch version:
  1. `owner-check` (5 min).
     - It fails unless `github.sha` equals the artifact's `commit`.
     - It reads the comment through the API and writes `owner-check.json`: author login, body
       SHA-256, the exact-line test computed in the step, the commit.
     - Marker step: "owner designation verified".
  2. `dryrun` (10 min).
     - `l2calib.py`, then `l2plan.py --profile v8 --calib calib.json --shared-tips --out
       dryrun.json`.
     - Output `launch` = `cost.launch_within_budget`.
     - If `launch` is false, no later job runs except `report-not-undertaken`, which writes the
       estimate as the result.
  3. `preflight` (30 min).
     - `l2preflight.py --profile v8`, full mode, with the artifact and owner check.
     - Downloads `mutant-campaign.json` from `mutants_run`.
  4. `s1a` (40 min): `l2s1a.py` normal and `-O`.
  5. `shard` (matrix s = 0…31, 40 min each): `l2enum.py` normal and `-O`.
  6. `merge` (20 min, `if: always()` after the shards).
     - Runs `l2merge.py` normal and `-O`, then `l2cert.py`.
     - Uploads `result.json`, `expected-controls.json`, `residue.json` if present, and
       `certificate.json`.
     - Marker step: "certificate holds".
- **Verdicts** read the jobs' and steps' conclusions and these files only. The label is
  `result.json`'s `label`.
- **Retention (§A.42).** An evidence-retention pull request records three things under the record
  directory: `result.json` (the expected result), `expected-controls.json`, and a reproduce recipe
  (commit, commands, comparison). The shard files' digests are in `result.json` and
  `certificate.json`. Logs are diagnostics only.

## 12. Local evidence (`design/`)

Run by `code/l2run.py` with `python3 -I -B` on Python 3.13.16, in about six minutes. Every step's
stdout and stderr is in `runs/`. `RUN-MANIFEST.json` records:
- commands, exit codes and durations;
- `-O` identity, by stdout or by the files written;
- SHA-256 values of code, outputs and toy-run files.

| step | result |
| --- | --- |
| `manifest_verify` | the manifest matches |
| `l2_selftest` | 16 cases pass (L2-S1, GUARD, POST, ORB, AUTH, MAN, MRG, LBL, RT, C16, SAMPLE, MASK, PLAN, SHTIP, GATES, CFG) |
| `dryrun_toy` | 1,400 records, 488 orbits, 4 shards; masking-equivalent 1,398 in both readings |
| `dryrun_v8_plan_no_closure` | v8 shard plan without enumeration or closure: 5,163,225 records, 816,050 orbits (875 + 815,175), group order 8, 32 ranges; non-fixed context sizes up to 29 (37 with the fixed quantities); `closures_computed = 0` |
| `calibration_planted` | timings on planted sets (not deterministic) |
| `dryrun_v8_estimate` | see below |
| `preflight_toy_quick` | every pre-flight control passes (quick mode): refusal 46 of 46; C11 (i) 4,193 tables, (ii) 24 sets, (iii) 96 sets, 0 failures; both direction mutants fail C11; S6 pass; C12 on the toy universe |
| `mutants_quick` | 30 of 30 killed at their named cases: 17 rule mutants (§6 table of L1) and 13 machinery mutants. The two demonstrations fail C11 only, with counts equal to the frozen rule's |
| `s1a_toy` | status OK; toy L_A = 15, L_G = 7 (toy geometry, not a statement about v8) |
| `shard_toy_0`…`3` | 488 representatives, every gate at rate 1: C0 976, C7 976 (739 with a shared tip), C8 488 orbits, C9 2,800, C10 (i) 1,952, C11 (i) 976 (5,328 tables), C17 976, C18 976; 0 failures |
| `merge_toy` | COLLAPSE_ALL on the toy class (design evidence, no statement); coverage exact; recount 1,400 and 488; rule T evaluated |
| `certificate_toy` | items 1–8 hold (item 3 with the quick campaign, which the toy profile admits) |
| `crosscheck_toy_counts` | all 54 merged counts equal code-r5's full per-record computation; 32 identically zero |
| `code_r5_equivalence_quick` | the quick suite equals code-r5's except the extended refusal block |
| `planted_survivor_path` | the shard code's survivor path on planted toy records: survivors retained; C7, C8, C11 (i) and (ii), C17, C18 run with 0 failures; negative control: a bound missing one retained quantity gives C9 failures and a minimal witness confirmed by direct closure |
| `refusal_probe_v8` | 9 of 9 attempts refused, with VOID and item 6, before any file is written: `l2enum`, `l2s1a` and `l2preflight` for v8 with no artifact, an artifact for another commit, and one whose designation is not the owner's |

Every deterministic step is `-O`-identical.

**Not run locally, pending.**
- The full mutant campaign: the full suite for every rule mutant, and the equivalent mutants. It is
  CI-only and needs an owner-approved dispatch.
- The full-depth control suite (C1 F 0–15, B 0–8, G 0–23, …). It runs in CI pre-flight.
- Everything on v8's class.

**The cost estimate,** from this calibration, which is planted sets on this machine:
- **Total:** 62,937 runner-seconds, about 17.5 h, with the `-O` duplicate and an overhead factor of
  2. A development run on the same machine gave 55,893 s; the timings are not deterministic.
- **Per shard:** 1,967 s.
- **Launch condition 1** asks for at most half the budget (43,200 s) and half the shard timeout
  (1,200 s). The estimate meets neither, so the stop rule would not launch.
- **Excluded:** C7 on shared-tip records. On the toy class, 739 of 976 representative–convention
  pairs have a shared tip. The reference closure costs about 20–50 ms under A and 90–280 ms under G per record, at 16–24
  quantities, on the planted sets.
  Under the literal reading, C7 alone would therefore exceed the budget by a large factor (§13, F3).

The exact figures are in `runs/dryrun_v8_estimate.out`.

## 13. Findings for review: ambiguities and gaps in the frozen Layer 1

None is fixed here. Each needs an owner decision or an append-only amendment with its own review.

**Rule T.**
- **T1. Rule.** Rule T's inputs say "the global bound" without naming L3′ or L3; §12 calls S1a's
  closures "the C9 bound". Layer 2 uses L3′, the label rule, and reports L3. On the toy class the two
  agree.
- **T2. S1a's status is undefined.** "If S1a is VOID, MISMATCH or INCOMPLETE" uses the k ≤ 2 run's
  label names, but L1 defines no status for S1a. §4 gives Layer 2's reading, which includes the
  shards' C9 results. If the owner intends S1a's status to depend on S1a's own computation only,
  rule T could be evaluated before the shards finish.
- **T3. The cost clause.** "In either case, if the dry-run cost estimate exceeds S7's budget, the
  search is reported as not undertaken for cost":
  - in the L_A = L_G = 0 branch nothing is undertaken, so the clause is vacuous there;
  - in the other branch, S1b exists only as a future preregistration with no dry run in Stage 0;
  - it is not stated whose dry run is meant.

  Layer 2 records the clause as not evaluable in Stage 0.
- **T4. Citation.** The consequence follows from PO4 together with two definitional facts that rule
  T does not cite: context nesting, and the record-independence of the frame and of seed-tip status
  (§8, PO-L2-7). The argument appears complete. Whether it is complete is the reviewer's question.
- **T5. Grammar.** In L_G, "with a seed tip whose cone contains a source cell" reads naturally as the
  tip's cone, which is undefined. Layer 2 reads it as the quantity's cone, matching the definition of
  G-linkage.

**Other findings.**
- **F1. BASE_RESIDUE is unreachable as written.** C6 compares the computed base with the hand
  derivation, which concludes "collapsed". A non-collapsed base is therefore a C6 disagreement, which
  is a MISMATCH, and MISMATCH precedes BASE_RESIDUE. §3 nevertheless says that a non-collapsed base
  leads to base-relative labels. Layer 2 follows §5's precedence.
- **F2. Base-relative survivors under G.** "A record whose retained set contains a quantity outside
  ret(∅)" makes every record with a retained in-frame sample a base-relative survivor under G, which
  conflicts with S_G's seed-tip definition. Layer 2 implements the literal text and reports the
  count only under BASE_RESIDUE.
- **F3. C7's "record containing a shared tip" is undefined, and decisive for cost.**
  - Under the literal, initial-context reading, the share of records is large: 739 of 976
    representative–convention pairs on the toy class.
  - At the planted-set reference cost, C7 alone would exceed S7's budget.
  - A retained-set reading (a shared tip among retained quantities) is cheap, but it is a different
    control.

  This needs an owner decision before the Layer-2 freeze.
- **F4. Residual support is undefined in r5.** "Residual support in bits, against S_max = 27" has no
  definition. Layer 2 defines it in §4 and reports it only.
- **F5. Masking equivalence: text and design code differ.** L1 §1 says "equal even-class contexts";
  code-r5 keyed it on record samples alone, without E1 merges. The two readings coincide on the toy
  class (1,398) and differ on a toy variant with last slice 4 (41 against 40). Layer 2 implements the
  L1 text and reports the other.
- **F6. Degeneracies.** §3 says every degeneracy is cross-tabulated with survivors, but C8's closed
  list cross-tabulates eight and lists the masking-equivalent and nontrivial-stabilizer counts plain.
  Layer 2 implements C8's list exactly (54).
- **F7. C12's second clause** ("every retained in-frame cone lies in the frame") is per record, but
  it is listed as pre-flight only. Layer 2 checks it once on the universe of quantities (PO-L2-9).
- **F8. Sample rates.** The rates of C11 (i), C17 and C18 are not fixed in L1. Layer 2 uses 1 in
  1,000 each, plus every survivor.
- **F9. S7's budget looks tight for item 7.** The `-O` duplicate doubles the cost. The estimate in
  §12 is about 17.5 h before C7's shared-tip work and the survivor gates. The calibration uses
  planted sets, not v8 contexts, so it can err either way. At 16 quantities, close to v8's mean
  pair context of 15.7, the planted timings are about 3.4 ms under A and 4.3 ms under G (memoized;
  about 9 ms without the memo). L1 §10 assumed about 3.5 ms per closure.
- **F10. "Through s0geom's frozen engine" (§5b item 2).** Layer 2 changes the engine copy in two
  places (§2). Both are within Layer 2's remit, but the reviewer should confirm that this phrase
  does not mean code-r5's bytes.
- **F11. C12 on v8 needs the grant.** C6's execution instances, C10 (ii) and C12 on v8 need contexts
  of v8's class, so they run only in the authorized pre-flight. Locally they are implemented and
  exercised on the toy profile only.

## 14. Freezing Layer 2

After independent review, and once the owner has decided F3 and confirmed or amended rule T's
wording:
1. Apply the accepted changes and regenerate `LAYER2-MANIFEST.json`.
2. Re-run `l2run.py`.
3. Record the plan's SHA-256, the manifest's `code_digest` and the configuration digest in a freeze
   note.

Before any v8 dispatch, the owner then makes three separate decisions: the workflow edit, the full
mutant campaign, and the enumeration itself, by an authorization artifact naming the frozen commit
and `code_digest`.

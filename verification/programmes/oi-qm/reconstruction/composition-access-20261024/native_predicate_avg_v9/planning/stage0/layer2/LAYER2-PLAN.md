# NP-AVG-1 Stage 0, Layer 2: implementation plan (r3, for re-review)

**Status: WIP / UNREVIEWED, not frozen. The v8 enumeration is not authorized.** Nothing in this
directory has run on v8's configuration class. v8 setups are constructed only to check that they
are refused, and v8's record space is used only for combinatorics (counts, orbits, shard ranges and
context sizes), with no context constructed and no closure computed. No shared-tip, F_G or other
record-enumerating count is computed on v8: the dry run refuses it (§3.6). No grant for v8 is
constructed; the only grants built are deliberate forgeries, which must be refused (§7).

**This revision.** r1 (`99a9797e`) was reviewed in `../../review/LAYER2-REVIEW.md` (`a63db7ba`):
ACCEPT WITH CHANGES. r2 (`4a51c675`) applied L2-R1 to L2-R8 and the accepted part of L2-R9, with
every owner ruling left as a placeholder. r3 implements erratum E1 (`../amendments/E1-LAYER1-ERRATUM.md`),
in effect under `../LAYER1-FREEZE.md`, which carries the owner's rulings; its follow-ups for Layer 2
are listed in `../amendments/E1-CHANGES-r2.md`. `CHANGES-L2-r3.md` maps each E1 item and follow-up to
its edit, control and mutant. The rulings on T1, T2, T5, T6, F3 and F6 are filled in (§4.2). Three
owner decisions stay open placeholders, with no default: κ (the launch margin), the Lemma G-D
reference form and O1 (E_G as a C7 set). The production entry points refuse the v8 profile while any
of them is open. `KAPPA-PROPOSAL.md` is an advisory proposal on κ for the owner; it sets nothing.

**Authority.** The owner, 2026-10-26: "NP-AVG-1 — Yes, write Layer 2 for independent review. Keep
the v8 lock intact and run no v8 experiments. Retain rule T's current wording provisionally, with
the reviewer specifically instructed to test whether it is mathematically unambiguous and whether
the proposed Layer 2 argument genuinely follows from the frozen assumptions. Do not treat an
unreviewed Layer 2 as proved."

**What this implements.** Layer 1 is frozen at `f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966`
(`../LAYER1-FREEZE.md`). The specification is `../r5/STAGE0-PLAN-r5.md`, SHA-256
`1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e`, cited below as "L1 §n", as
governed by erratum E1 (`../amendments/E1-LAYER1-ERRATUM.md`), whose items are cited as "E1-T1",
"E1-F3" and so on. This plan implements L1 §5b: the production enumerator, the controls, the
configuration hashes and the execution certificate. Neither Layer 1 nor E1 is changed. Where they
leave something unspecified or ambiguous, the reading Layer 2 implements is stated where it is used
(§4), and the points that need an owner ruling are listed in §4.2 and §13. None is resolved by
editing a frozen file or the erratum.

**What a bounded run shows.** The local evidence (§12) runs on toy, planted and small-window
instances, on S6's 21-bit carrier and on v8 combinatorics only. It shows that the code runs, that the
controls can fail and that the toy outputs agree with an independent computation. It proves nothing
about v8's class. In the proof-obligation table (§9), "proved here" means an argument is written in
this plan; the r1 review's verdict is cited where it exists, and the r2 and r3 additions are unreviewed.

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
| `l2analysis.py` | C4v group, canonical representatives, orbits, `post_closure`, degeneracies, the r5 list of 54 counts and the reported list of 58 (E1-F6), structure attributes |
| `l2refcheck.py` | reference gates C7, C11 (i), C11 (ii), C17, C18, their streamed forms (near-only for L3), and the reference recomputation of L_A and L_G (E1-T2 case 2 (d)); imports only `s0ref` |
| `l2plan.py` | the dry run: index space, Burnside orbit count, shard plan, context sizes, the complete cost estimate; the record index (`Space.index_of`), the closure-free C7 predicates of E1-F3 (Q⁰, In/Out, F_G, I_c, E_G) and the per-record masking-equivalence test (E1-F6); refuses every record-enumerating count on v8; imports no engine |
| `l2calib.py` | timing calibration on planted sets for the estimate |
| `l2preflight.py` | pre-flight controls (item 2) |
| `l2mutants.py` | the mutant campaign, quick (local) and full (CI) (item 3) |
| `l2s1a.py` | the S1a driver: global bounds, per-line closures, L_A, L_G |
| `l2enum.py` | the record driver and per-record analysis, one shard per run |
| `l2merge.py` | the merge, S1a's diagnostic status σ (E1-T2), the label generator, rule T and its record |
| `l2cert.py` | start-up checks and the certificate builder (items 1–8) |
| `l2selftest.py` | controls of the Layer-2 machinery (34 cases) and its 30 machinery mutants; `--only` runs named cases |
| `l2run.py` | the bounded local evidence driver |

`design/`: the design-evidence scripts (`planted_shard.py`, `refusal_probe.py`, `crosscheck.py`,
`r5_equivalence.py`, `e1check_replay.py`, `kappa_calibration.py`), the retained stdout and stderr of
every step in `runs/`, the toy run's structured files in `toyrun/`, the κ calibration repeats in
`kappa/` (timing data), and `RUN-MANIFEST.json` and `.md` (commands, exit codes, `-O` identity,
SHA-256 values of code, outputs, toy-run and calibration files, and the commit caveat of §12).

`KAPPA-PROPOSAL.md` (beside this plan): an advisory proposal on κ, with the cost model and the
calibration spread; it sets no value.

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
R4-6). Each member contributes to the additive counts of the reported list (58 counts: L1 §6 C8's 54
and the four survivor cells of E1-F6); the observer-class counts and the masking-equivalent count are
formed by the merge (§3.7). The two flags of E1-F6 are per record: a nontrivial stabilizer
(|C4v| / |orbit| > 1) and masking equivalence relative to the record space
(`l2plan.Space.masking_equivalent_record`, PO-L2-20), the latter evaluated only where it can
contribute, on a member that is a survivor under A or G.

For survivor orbits, every member is also closed directly (§3.3), and the shard records the §3
structure of the representative: the survivor sets, linkage, (b) sets, per-member G-linkage and
source cells, shared aligned tips, cover-graph components, residual support (§4) and rule
dependence.

### 3.3 In-run gates (item 4)

| gate | runs on | verdict class on failure |
| --- | --- | --- |
| C0 (contexts) | every record on which a reference gate or C7 runs: production context equals `s0ref`'s for that record | VOID |
| C7 | per record, on every record of E1-F3's sets 1–4 (§3.3a), both conventions; never through orbit representatives | VOID |
| C8 | every survivor orbit, every orbit with a computed MISMATCH, and a 1-in-100 sample of orbits: every member's closures computed directly and compared with the carried ones, attribute by attribute, and its count contributions compared | VOID |
| C9 | every record (every member, carried): ret_L3′ ⊆ ret_L3, and each within the S1a bound of its rule | MISMATCH |
| C10 (i) | every closure: no fixed quantity in a log | MISMATCH (L1 §5, "a fixed quantity is eliminated") |
| C11 (i) | every member of every survivor orbit (both conventions); a 1-in-1,000 sample of the other representatives | VOID |
| C11 (ii) | every survivor record (members, carried): P_A-dir and P_A (A), P_G-dir and P_G (G), by `s0ref` | MISMATCH |
| C17, C18 | every member of every survivor orbit (both conventions); a 1-in-1,000 sample each of the other representatives | VOID |

On survivor orbits the reference gates run on each member with that member's own reference context
and the closure computed directly for that member (L2-R2), so L1's "every survivor" is met without
an equivariance assumption on the reference (PO-L2-14 states what remains assumed). C7 on survivors
is set 1 of §3.3a.

**The survivor cap** (L2-R3, L2-R6). Survivor gates and residue detail run for at most
`survivor_cap_per_shard` (10) survivor orbits per shard. A shard that meets more records
`survivor_cap_exceeded = true`, still computes and counts every record, and the merge labels the run
INCOMPLETE: no survivor is left without its gates, and none is dropped from the residue silently.

**Samples** are deterministic: index i is sampled on stream X at rate R iff SHA-256(salt | X | i),
read as a big-endian integer from its first eight bytes, is 0 mod R. The salt, the stream names and
the rates are configuration constants (item 1). C8 (1 in 100 orbits, L1), C11 (i), C17 and C18 (1 in
1,000 each, Layer-2 constants under L1 N6, accepted reading F8) sample representative indices. C7's
two samples, H₁₀₀ and H₁₀₀₀, are drawn over every record index on their own streams `C7_H100` and
`C7_H1000` (E1-F3, §3.3a).

### 3.3a C7 per record (E1-F3)

**Scope.** For each orbit, in the shard of its representative, and for each member R and convention
c, R is in C7's scope if it is in any of:
1. **Surv_c:** R's carried result is a survivor under c.
2. **Set 2:** under A, T_A: R's carried closure has a shared near tip (T_A ⊆ Surv_A, E1-F3); under
   G, (T_G ∩ Surv_G) ∪ F_G, with F_G = {R : In(R) has a shared near tip} computed by
   `l2plan.Space.c7_flags` from Q⁰(R) and the frame, with no closure (PO-L2-17).
3. **I_c ∩ H₁₀₀:** Q⁰(R) has a shared near tip under c (closure-free) and R's own record index
   (`l2plan.Space.index_of`, PO-L2-19) is in H₁₀₀.
4. **H₁₀₀₀:** R's own record index is in H₁₀₀₀.

Every orbit is processed exactly once (PO-L2-2), so every record of the space is considered exactly
once, representative or not. The closure-free predicates are `l2plan`'s own code, written from L1 §2
and independent of the production engine and of `s0ref` (L2-SCOPE checks that the three agree on
every toy record).

**The check** (`l2enum.Shard.c7_record`). For R in scope under c: R's production L3′ closure is
computed directly on R; R's reference closure is the full `s0ref` greatest self-supporting subset in
R's own reference context; C0 compares the two contexts. C7 fails on R if the direct closure differs
from the reference, or if R's carried result differs from its direct closure. Both comparisons are
tallied (`direct_vs_reference_failed`, `carried_vs_direct_failed`). A failure is VOID (L1 §5). A
record in several sets is checked once and tallied in each.

**Not implemented.** The Lemma G-D reference form (W(Out(R)) ∪ In(R)) is a non-executing proposal
pending the owner (E1 §9; owner decision `G_D`): the only reference form is the full `s0ref` closure
(`l2config` `C7.reference_form = full_s0ref`). E_G is not a check set (owner decision O1, optional,
not adopted).

**The survivor cap.** Set-1 records of a survivor orbit beyond the survivor cap are not checked; they
are tallied as `skipped_beyond_survivor_cap`, and the shard's `survivor_cap_exceeded` makes the run
INCOMPLETE (§3.7), so no survivor is left unchecked in a run that is not INCOMPLETE.

**Coverage reporting.** Each shard writes, per convention and set, records checked and failed,
orbits touched, the sum of the touched orbits' sizes, and the skipped count; `result.json` sums them
(`C7_scope_coverage`).

**The toy profile** uses the v8 sample rates (100, 1,000) for C7, so that the toy run's per-set
coverage can be compared with E1-check part J's independent populations; the pre-flight control
suite still runs C7 on every toy record.

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
L3′ bounds (E1-T1; L_G by the quantity's own cone, E1-T5), and their L3 values in a separate field.
It writes the fields from which the merge derives σ (§4.3): C0, C17 and C18 with the reference on
all four bound closures, the L3 ones with near tips only (L2-R8); L_A and L_G recomputed from the L3′
bounds with `s0ref`'s explicit cones and tips (`l2refcheck.ref_linked_counts`, case 2 (d)), with the
L3 values recomputed and any difference reported only; the bound closures' logs checked for fixed
quantities; and ret_L3′(U) ⊆ ret_L3(U). The reference checks stream one explicit cone at a time
(`l2refcheck.cover_index`), since the bound has 1,584 non-fixed quantities.

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
   constant fixed with its basis before the complete estimate is computed (L2-R7; review §6). The
   owner's answer was "Decide later" (E1 §9). It is an OWNER placeholder with no default value
   anywhere in code or configuration, so no launch decision can be computed, and `l2cert.startup`
   refuses the v8 profile. `KAPPA-PROPOSAL.md` is an advisory proposal for that decision. The launch
   decision also needs the C7 term, whose v8 inputs are not computed (§3.6).
2. **During the run.** A shard that reaches its timeout is cancelled by the host; its file is
   missing, and the merge labels the run INCOMPLETE. A shard that exceeds the survivor cap is
   INCOMPLETE. Nothing is retried automatically.
3. **After a stop.** A re-dispatch is a new owner decision (§A.43 item 4).

The full mutant campaign is a separate dispatch with its own budget: about 33 minutes locally on the
r3 measurements (L1 §10), plus the 30 machinery mutants, each running every self-test case (about half a minute each). It is not counted in
the 24 hours.

### 3.6 Dry run and the complete cost estimate

The dry run (`l2plan.py`) is mandatory: every computing entry point refuses to run without a
`dryrun.json` for the same configuration with `closures_computed = 0`, and for v8 without a launch
decision that admits the run (certificate item 7). It imports neither engine nor reference; it
constructs no context and calls no guarded entry point (the review ran it under an import trap). Its
formulas are checked against the engine on the toy class (L2-PLAN, L2-MASK, L2-SHTIP, L2-INDEX,
L2-SCOPE).

It prints:
- N, the Burnside orbit count and the shard plan;
- the histogram of non-fixed context sizes over all records, from per-item sample counts by
  convolution, with no record enumerated;
- for the toy profile only, the masking-equivalent count (on v8 the merge computes it);
- with `--shared-tips`, for the toy profile only, the records whose initial context has a shared
  near tip per convention, and the closure-free C7 populations of E1-F3: I_A, I_G, F_G and, for
  information, E_G, each as records and orbits, by combinatorial enumeration with no closure.

**On v8 these counts are not computed.** They enumerate v8's record space, which needs an
authorization that does not exist. `--shared-tips` is refused for v8 before anything is computed
(exit 2, a refusal object), and every enumerating function (`shared_tip_records`,
`c7_populations`, the record generator) refuses a space whose (dim, n, port) are v8's at entry
(L2-V8COUNTS; `refusal_probe`). The v8 dry run reports each of |F_G| (records and orbits), |I_A|,
|I_G| and |E_G| as "not computed (requires authorization)". E1-F3's checkpoint ("The dry run
computes |F_G|, records and orbits, without any closure, and the C7 cost term from it") is therefore
met on the toy profile only (§13). An owner authorization of a combinatorial-only v8 count would need
a grant-gated path in `l2plan`, which this revision does not contain.

**The estimate** (L2-R6, E1-F3), in runner-seconds, term by term, with t_A(m), t_G(m) the calibrated
production closure times and r_A(m), r_G(m) the calibrated full-reference closure times at m
non-fixed quantities (`l2calib.py`, planted sets only; beyond the largest calibrated size scaled
quadratically), m̄ the mean context size and m_max the largest; each run-time term is doubled for
the `-O` copy. `dryrun.json` carries each term's formula beside its value (`cost.formulas`):
1. **closures:** Σ_m count(m) · (orbits/N) · [2 t_A(m) + 2 t_G(m)] · overhead (2, a configuration
   constant covering analysis and member attributes);
2. **sampled gates on representatives:** (1/1,000 for each of C11 (i), C17, C18) · orbits ·
   [r_A(m̄) + r_G(m̄)], and C8 on 1 in 100 orbits · 8 members · [2 t_A(m̄) + 2 t_G(m̄)];
3. **C7 on its E1-F3 scope**, per record: c7_c = 2 · [t_c(m) + r_c(m)] (a direct production closure
   and a full reference closure, normal and `-O`), evaluated at the record-weighted mean over the
   context-size histogram (central) and at m_max (upper):

   C7 = |F_G| · c7_G + (|I_A| / 100) · c7_A + (|I_G| / 100) · c7_G + (N / 1,000) · (c7_A + c7_G),

   with set 1 inside term 4, and set 2 under A inside set 1 (T_A ⊆ Surv_A). The last summand is known
   (its expected sample size is N/1,000); the first three need |F_G|, |I_A| and |I_G|, which on v8 are
   not computed, so the v8 term is reported as this formula with its coefficients
   (`cost.C7.coefficients_seconds_per_record_central`) and the value "not computed (requires
   authorization)". A trivial upper bound (|F_G| = |I_A| = |I_G| = N, at m_max) is printed and
   labelled "not an estimate";
4. **survivor gates, capped:** cap · S · 8 · [2 t_A + 2 t_G + 4 (r_A + r_G)] at m_max, which includes
   C7 on set 1;
5. **pre-flight** (300 s) and **merge** (300 s per run): stated allowances with their basis in
   `l2config`;
6. **S1a:** four bound closures; per bound, three streamed reference passes (C17, C18 and the case
   2 (d) recomputation), each costed as a reference closure at the largest calibrated size scaled
   linearly to the universe size; and two closures per axis line.

No value is assumed for an uncomputed input. On v8 the total, the shard job's estimate and the
launch decision are "not computed"; `cost.known_terms_runner_seconds` and
`cost.known_terms_plus_C7_set4_runner_seconds` give the sum of the terms that are known.
`launch_within_budget` is `null`, with the reasons listed (`launch_not_decided_because`): κ is a
placeholder, and the C7 inputs are not computed. The local figures are in §12.

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

**Counts.** The 58 counts of E1-F6.
- The additive counts are summed, including E1-F6's four survivor cells.
- Observer classes are Σ |orbit(K)| over the distinct canonical public sets K, per convention and
  category (PO-L2-5).
- `masking_equivalent_records` is computed by the analytic formula of PO-L2-6, in the L1 reading
  (accepted reading F5).

**C7 coverage.** The shards' per-set tallies are summed into `C7_scope_coverage` (§3.3a).

**S1a's status σ** is derived from `s1a.json`'s fields by `l2merge.sigma`, as §4.3 states. Every
failing condition enters the run's reason lists (case 1 as INCOMPLETE, case 2 as VOID, case 3 as
MISMATCH); σ is the name of the first matching case. σ never overrides the label.

**Labels** (L1 §5), first match, from every mandatory check:
1. **VOID:** a pre-flight control of VOID class, a VOID gate (C0, C7, C8, C11 (i), C17, C18), S1a's
   case 2, the manifest, or the authorization fails.
2. **MISMATCH:** C6's execution instances, C9, C10 (i), C10 (ii), C11 (ii), C12, or S1a's case 3 (a)
   or (b) fails.
3. **INCOMPLETE:** a shard is missing, refused or incomplete, the coverage or residue check fails, or
   S1a's case 1 holds.
4. **BASE_RESIDUE** (unreachable while F1 holds, §13).
5. **COLLAPSE_ALL.**
6. **RESIDUE_UNLINKED:** survivors exist, and none is Φ-linked under A or G-linked under G.
7. **RESIDUE.**

**Recorded with the label:** the commits recorded by pre-flight, S1a and every shard; the CI run
identity; the authorization echo with the owner check; the owner rulings and the decisions still
open; the accepted readings. **Rule T** is evaluated iff σ = OK, and recorded as in §8.

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
| E1-F3 "computed closure" for set membership | the carried result (the representative's closure carried by the group action); on orbits closed directly (survivor, flagged and C8-sampled orbits), C8 compares carried and direct results and fails VOID on any difference, so the choice cannot hide a failure there | r3 reading, unreviewed | `l2enum.Shard.c7_orbit` |
| E1-F3 set 1 beyond the survivor cap | set-1 records of an orbit beyond the cap are tallied as skipped; the run is INCOMPLETE (L2-R3) | r3 reading, unreviewed | `l2enum`, `l2merge` |
| E1-T2 case 1 (a) | `s1a.json` missing, unreadable, or lacking a field σ reads | r3 reading, unreviewed | `l2merge.sigma` |
| E1-T6 `rule_T.statement_scope` | recorded in every outcome, as the standing of rule T's consequence; the zero branch's text is the same | r3 reading, unreviewed | `l2merge.rule_T` |
| C7 sample rates on the toy profile | 100 and 1,000, as on v8, so that the toy run's coverage is comparable with E1-check part J | r3 design choice | `l2config` |

The accepted readings are also recorded in `l2config.CONFIG['accepted_readings']` and echoed into
`result.json`.

### 4.2 Owner rulings (erratum E1) and the decisions still open

E1's rulings are recorded in `l2config.CONFIG['owner_rulings']` and echoed into `result.json`. The
open decisions are `OWNER-PLACEHOLDER` values; `l2cert.startup` refuses the v8 profile while any
remains (certificate item 1; L2-PLACEHOLDER), and `result.json` lists them.

| ruling | E1 item | implemented as |
| --- | --- | --- |
| T1, the bound rule T reads | E1-T1: ret^{L3′}_c(U); L3 values reported only | `l2s1a` writes L_A, L_G from the L3′ bounds and `L_reported_L3` separately; `l2merge.rule_T_inputs` reads the L3′ fields (L2-T1) |
| T2, S1a's status | E1-T2: σ, cases 1–4 with 2 (d); diagnostic, never overriding the label | §4.3; `l2merge.sigma`, `rule_T`, `rule_T_record` (L2-SIGMA, L2-PREC, L2-2D) |
| T5, what L_G counts | E1-T5: quantities with a seed tip whose own cone contains a source cell | `l2s1a.linked_counts`; reference `l2refcheck.ref_linked_counts` (L2-T5) |
| T6, the standing of rule T's consequence | E1-T6: geometric fact only, with the owner's qualification | `rule_T.statement_scope` carries E1-T6's text verbatim (L2-T6) |
| F3, C7's scope | E1-F3: sets 1–4, per record, every record index | §3.3a (L2-C7COV, L2-F1, L2-F2, L2-SCOPE, L2-INDEX) |
| F6, the count list | E1-F6: 58 counts | `l2analysis.reported_count_keys` (L2-COUNTS); `crosscheck` |

| open decision | question | what the code does meanwhile |
| --- | --- | --- |
| κ | the launch margin and budget (S7); the owner: "Decide later" | no value anywhere; no launch decision is computed; the v8 profile is refused. `KAPPA-PROPOSAL.md` is advisory |
| G_D | Lemma G-D in C7's reference computation (E1 §9: conditionally approved; non-executing until the owner confirms the proof) | not implemented; the full `s0ref` closure is the only reference form |
| O1 | E_G as a fifth C7 set under G (E1 §9; optional, not adopted) | not a check set; |E_G| is reported for information on the toy profile |

### 4.3 S1a's status σ (E1-T2)

σ ∈ {OK, VOID, MISMATCH, INCOMPLETE} is a diagnostic status of the S1a computation, not a run label.
`l2merge.sigma` derives it from `s1a.json`'s fields and the shards' C9 tallies; the first matching
case applies:
1. **INCOMPLETE** if (a) `s1a.json` is missing (including every case in which S1a refused to start)
   or lacks a field σ reads; (b) its normal and `-O` outputs are not byte-identical, or one is
   missing; (c) its code or configuration digest differs from the manifest.
2. **VOID** if, on any of the four bound closures ret^ρ_c(U): (a) C0 fails (production context of U
   ≠ `s0ref`'s); (b) C17 fails (`s0ref` finds a free eligible tip); (c) C18 fails (a logged elimination
   not justified by `s0ref`); the L3 closures with near tips only; or (d) L_A or L_G recomputed from
   the L3′ bounds with `s0ref`'s explicit cones and tips differs from the production value. The L3
   values are recomputed the same way; a difference is reported (`L_reference_L3_differs`) and is not
   a σ condition.
3. **MISMATCH** if (a) a fixed quantity appears in a bound closure's elimination log; (b)
   ret^{L3′}_c(U) ⊄ ret^{L3}_c(U); (c) the in-run C9 gate fails on a record of an accepted shard (the
   run's computed closure, against the S1a bounds).
4. **OK** otherwise.

**Precedence.** Rule T is evaluated iff σ = OK. Every condition that holds enters the run's label as
an INCOMPLETE, VOID or MISMATCH reason (case 1, 2, 3 respectively); the label is generated by L1 §5
from every mandatory check, and a run cannot pass because σ = OK if any other mandatory check fails.
When rule T is evaluated in a run whose label is VOID, MISMATCH or INCOMPLETE, `rule_T` records its
outcome with `beside_label` set to that label, and `S1b_S1c` reads "no proposal from this run"; no S1b
proposal is made from such a run without the owner's separate decision. σ reads C9 only on accepted
shards; shard completeness is not an input of σ.

`result.json` records σ under `S1a.status` and every failing condition, by case, under
`S1a.status_reasons`.

## 5. Structured outputs (§A.44)

Every verdict reads exit statuses and these files. No log text is read. Where printed output carries
a fact (pre-flight's subprocesses), the producing step parses the JSON object that the subprocess
prints as its whole stdout and records its exit status; a non-JSON stdout counts as failure. The
schema names are recorded in each file.

| file | schema | content |
| --- | --- | --- |
| `dryrun.json` | `…/dryrun/2` | records, orbits (single, pair), group order, shard plan [{shard, lo, hi, count}], context-size histograms, max context size, `closures_computed: 0`, `contexts_constructed: 0`, configuration digest, `C7_populations` (toy with `--shared-tips`: I_A, I_G, F_G, E_G as records and orbits; v8: "not computed (requires authorization)"), optional `shared_tip_records` (toy), optional `cost` {terms (each a value or "not computed"), `formulas`, total, known terms, known terms plus C7 set 4, per-job estimates, timeouts, κ, `C7` {scope, reference form, per-record seconds (central, at m_max), the set formulas, the inputs with their values or "not computed", coefficients, trivial upper bound}, survivor cap, `launch_within_budget`, `launch_not_decided_because`, launch rule}, expected checks, `pass` |
| `preflight.json` | `…/preflight/1` | profile, mode, `code_digest`, configuration digest, `commit`, `tree_clean`, `ci_run`, authorization echo, `controls` {name: {pass, class, …}}, `base_collapsed` {A, G}, the full control-suite, self-test and S6 objects, `pass` |
| `mutant-campaign.json` | `…/mutant-campaign/1` | mode, `code_digest`, the unmodified-suite precondition, per mutant {named case, exit, failed, killed, run}, demonstration fields, killed/total, `pass` |
| `s1a.json` | `…/s1a/2` | bounds per (convention, rule) as flat integer lists, sizes, L_A, L_G (`L_bound_rule` L3′), `L_reported_L3`, `L_reference` (L3′ and L3, case 2 (d)), `L_reference_L3_differs`, linked quantities, per-line results, reference checks per convention and rule, `fixed_in_log`, `L3prime_within_L3`, `status` (from these fields; the merge re-derives σ), reasons, digests, `commit`, `tree_clean`, `ci_run`, `sha256` |
| `shard-<s>.json` | `…/shard/3` | profile, shard, range, records, scanned, representatives, orbit weight, digests (code, config, dry run, S1a), `commit`, `tree_clean`, `ci_run`, authorization echo {decision, artifact, owner check, CI run}, base retained sets, additive counts, canonical class keys with orbit sizes, base-relative and L3-only tallies, gate tallies and first failures (diagnostics), `witness_min`, `witness_candidates_seen`, `survivor_representatives`, `survivor_cap`, `survivor_cap_exceeded`, survivor detail, `C7_scope_coverage` {convention: {set: records checked and failed, orbits touched, sum of touched orbit sizes, skipped beyond the cap}}, `sha256` (of the canonical JSON without it) |
| `result.json` | `…/result/1` | label, `label_source`, VOID/MISMATCH/INCOMPLETE reasons, base precondition, 58 counts (`n_counts`, `count_list`), record-sample masking reading, structure tallies, in-run gate totals, `C7_scope_coverage` and `C7_scope` (definition, reference form, samples), minimal witness and candidates seen, coverage, S1a {status σ, `status_reasons` by case, `status_kind`, L_A, L_G, `L_reference`, L3 values, bound sizes, lines}, `rule_T` {evaluated, outcome, `bound_rule`, `statement_scope` (E1-T6 verbatim), `cost_clause`, rulings, `run_label`, `beside_label` and "no proposal" when the label is not passing, `L_reported_L3`}, authorization echo, `ci_run`, `commits` {pre-flight, S1a, shards}, `owner_rulings`, `owner_rulings_pending`, `accepted_readings`, digests, coverage limits (L1 §11), input digests, residue file digest |
| `expected-controls.json` | `…/expected-controls/1` | the hand-derived and recorded expected values (`l2config.CONFIG['expected']`) and the observed pre-flight results |
| `residue.json` | `…/residue/1` | survivor representatives with the §3 structure (only when survivors exist) |
| `certificate.json` | `…/certificate/1` | items 1–8, each with `holds` and its evidence, including the commit binding and the landing requirement; `holds` overall |
| `fetched.json` (landing) | `…/v8-designation-fetch/1` | written at landing from the host API: comment URL, author login, body SHA-256, whether the body contains the required line |

All files are canonical JSON, with sorted keys and integers and strings only. Normal and `-O` runs
write byte-identical shard, S1a and result files (item 7).

## 6. The execution certificate (L1 §5b item 8)

| item | implementation | fails closed by |
| --- | --- | --- |
| 1 frozen manifest | `l2manifest.verify`: every `.py` SHA-256, the configuration digest and `code_digest` equal `LAYER2-MANIFEST.json`, and `vars(Rule())` equals the configuration's rule fields; then the running digests are bound in the engine and the reference; for v8, no OWNER placeholder may remain (open now: κ, G_D, O1). The configuration digest covers the C7 salt, stream names and rates (E1-F3) | printing VOID and exit 2 before anything is computed |
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

## 8. Rule T (L1 §12 with E1-T1 to E1-T6)

**Implementation.** `l2merge.rule_T(s1a_status, L_A, L_G)`, a function of those three values only;
`l2merge.rule_T_inputs` reads L_A and L_G from the L3′ fields of `s1a.json` (E1-T1); L_G counts the
quantities of ret^{L3′}_G(U) with a seed tip whose own cone contains a source cell (E1-T5).

| case | outcome | recorded consequence |
| --- | --- | --- |
| σ not OK | `not_evaluated` | S1b and S1c not proposed (L1 text verbatim) |
| σ = OK, L_A = 0 and L_G = 0 | `L_A = L_G = 0` | E1-T6's text: "No record whose items lie in Reg × {−1, …, 23}, of any size, has a linked survivor under the specified closure (L3′, the declared conventions and frame). This is a geometric property of that closure. It is not a probabilistic result, an empirical observation, or an independent theorem about the full model, and no law statement is made beyond k ≤ 2."; S1b and S1c not undertaken |
| σ = OK, L_A > 0 or L_G > 0 | `L_A > 0 or L_G > 0` | S1b put to the owner as a new preregistration (L1 text verbatim) |

`l2merge.rule_T_record` writes the outcome into `result.json` with the run's label beside it. When
the outcome is evaluated and the label is VOID, MISMATCH or INCOMPLETE, it records `beside_label`
and replaces the S1b proposal by "no proposal from this run (label …); the owner's separate
decision is needed" (E1-T2). `rule_T.statement_scope` carries E1-T6's text verbatim in every outcome;
the zero branch's statement is that text and must not be presented as a probabilistic result, an
empirical observation or an independent theorem about the full model. The L3 values are recorded in
`rule_T.L_reported_L3`, never as inputs. `rule_T.cost_clause` reads "not evaluable in Stage 0"
(E1-T3). `wording_status` reads "confirmed with qualification (E1-T6)".

**Neutrality** is tested in two ways (L2-RT). The function's signature contains no label. Through the
merge, the outcome is the same under COLLAPSE_ALL, RESIDUE_UNLINKED, RESIDUE and BASE_RESIDUE. σ's
inputs are validity facts about S1a and the records' C9 results, not the k ≤ 2 label or its
direction (E1-T2).

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
and T5 readings. E1 fixed those readings as rulings (E1-T1, E1-T2, E1-T5) and recorded the four
citations as note E1-T4. The converse does not hold and is not used: L_A > 0 does not imply that any
record has a linked survivor.

## 9. Proof obligations of Layer 2

| id | statement | status |
| --- | --- | --- |
| PO-L2-1 | `record_at` is a bijection from [0, N) onto the record space, and the shard ranges are a disjoint exact cover of [0, N) | **Proved here; review: valid.** Ranges: ⌊sN/S⌋ is non-decreasing from 0 to N. Bijection: standard unranking (singles; divmod by 25²; lexicographic pair decoding). **Checked:** toy, C13 recount and L2-ORB; v8 indirectly by the merge's recount |
| PO-L2-2 | Keeping exactly the records equal to their canonical image keeps one record per C4v orbit; the orbit weights sum to N, and the representatives number the orbits | **Proved here; review: valid.** **Checked** in every run by the merge's recount against Burnside's count; toy: 488 and 1,400 |
| PO-L2-3 | Equivariance of the true closure: ret(gR) = g·ret(R) for g ∈ C4v, under A and G, for L3′ and L3 | **Proved here from L1 PO4 and §1 E4; review: valid for the true closure.** **Checked** in-run by C8 on sampled, flagged and survivor orbits; on toy, all 488 orbits |
| PO-L2-4 | `post_closure(ctx_gR, g·ret(R))` equals `analyse(ctx_gR)` | **Follows from PO-L2-3 as code identity; review: valid.** **Checked:** L2-POST, all toy records, both conventions, both rules; C8 in-run |
| PO-L2-5 | The merged counts equal the full per-record computation (additive counts; observer classes as Σ \|orbit(K)\| over distinct canonical public sets) | **Proved here given PO-L2-3; review: valid (for 54).** The four E1-F6 cells are additive per member like the other degeneracy cells (PO-L2-21). **Checked:** toy, all 58 counts: the 54 against code-r5's full computation, the four against an independent per-record computation with code-r5's `s0ref` (`crosscheck_toy_counts`) |
| PO-L2-6 | Masking-equivalence canonical form and the analytic class count | **Proved here; review: valid.** **Checked:** brute force on three toy variants, both readings (L2-MASK) |
| PO-L2-7 | Rule T's L_A = L_G = 0 consequence (§8) | **Review: valid under the T1, T2 and T5 readings**, from L1 §1, §2, PO4 and PO7; those readings are now E1's rulings (E1-T1, E1-T2, E1-T5), and E1-T4 records the four facts. Its standing is E1-T6's: a geometric property of the specified closure. Not re-reviewed in r3 |
| PO-L2-8 | Memoizing the G eligibility per (pair, frame sources) does not change any result | **Proved here; review: valid.** **Checked:** quick suite identical to code-r5's except the refusal block |
| PO-L2-9 | C12 on the universe covers every record | **Proved here; review: valid** |
| PO-L2-10 | **Restated (L2-R1).** The witness is minimal among the records whose computed results — carried, or directly recomputed on flagged and sampled orbits — meet a MISMATCH condition. Precisely: the candidates are the members of every orbit closed directly (survivor orbits, orbits whose carried results meet a MISMATCH condition, and the 1-in-100 C8 sample), each confirmed on its direct results; the shard keeps the running minimum over all of them and the merge the minimum over the shards | **Proved here (by construction: every candidate is compared, nothing is capped).** **Checked:** L2-WIT (300 candidates in random order), L2-C16, the planted negative control. **Not claimed:** minimality over records whose fault is seen neither in the carried results nor in a directly recomputed orbit; that would need the computed closure to be equivariant, which is sampled (C8), not proved |
| PO-L2-11 | Normal and `-O` runs give identical outputs | **Not proved; checked per file.** No control logic uses `assert` in Layer-2 modules; `s0symcheck.py` relies on `assert`, so pre-flight always runs it without `-O` |
| PO-L2-12 | The S1a bounds are C9 bounds: ret(R) ⊆ ret(U) for every record, for L3′ and for L3 | **Follows from L1 PO4** (PO-L2-7 steps 1–2); review: valid. Both bounds are reference-checked (L2-R8) |
| PO-L2-13 | The dry run's formulas (N, Burnside, context histogram, shared-tip count, the C7 populations) equal the engine's | **Checked on toy only** (L2-PLAN, L2-SHTIP, L2-SCOPE: I_A 1,071, I_G 667, F_G 595 in 283 orbits, E_G 12, equal to E1-check parts H and J); review: N and Burnside on v8 independently confirmed by `s0symcheck`. The populations are not computed on v8 (§3.6) |
| PO-L2-14 | **(L2-R2; r3: C7 by set 1.)** Survivor-gate coverage: C0, C7, C11 (i), C17 and C18 run on every record the computation classifies as a survivor, each with its own reference context and its own direct closure | **Proved here for the orbits whose representative is a survivor:** every member is closed directly and gated (up to the cap; beyond it the run is INCOMPLETE); C7 runs on every survivor record as set 1 of §3.3a. A member that would be a survivor under direct closure in an orbit whose representative's computed closure is collapsed is reached only through the 1-in-100 C8 sample; its absence rests on the equivariance of the computed closure, which is sampled (C8), not proved. No equivariance of the reference is assumed. **Checked:** L2-SURV (4 members × 2 conventions on the planted block orbit); `planted_survivor_path` |
| PO-L2-15 | **New (L2-R3).** Residue completeness: a label other than INCOMPLETE implies that every survivor representative counted by a shard has its detail in the residue | **Proved here:** the merge's `residue_complete` requires, per accepted shard, `survivor_cap_exceeded = false` and exactly `survivor_representatives` details; the shard appends one detail per gated survivor representative and sets the flag when it meets one beyond the cap. **Checked:** L2-MRG (truncated residue and exceeded cap give INCOMPLETE); M_residue_ignored |
| PO-L2-16 | **New (E1-F3).** C7's per-record scope: for every record R and convention c, if R is in set 1, 2, 3 or 4 of §3.3a, the shard closes R directly with the production engine and with the full `s0ref` reference in R's own reference context, and C7 fails on R iff the two closures differ or R's carried result differs from its direct closure; the only exception is a set-1 record of an orbit beyond the survivor cap, which is tallied as skipped in a run that is then INCOMPLETE. No orbit representative substitutes for a member | **Proved here by construction:** `Shard.c7_orbit` iterates every member of every orbit it processes, each orbit is processed exactly once (PO-L2-2), and `c7_record` computes both closures for the member itself. **Checked:** L2-C7COV (the toy run's per-set coverage equals an independent computation with `s0ref`, an independent hash and `l2plan`'s group action, sampled non-representative records included: A set 3 12/12/45, set 4 1/1/4; G set 2 595/283/595, set 3 6/6/24, set 4 1/1/4, as E1-check part J); L2-F1 (F1 caught on all 595 affected records of set 2); L2-F2 (F2, invisible in every carried result, caught on all 312 affected records); mutants M_C7_set2_computed, M_C7_carried_only, M_C7_sample_rep_index. **Not claimed:** that the production engine computes the specified closure on v8's records; that is what C7 tests there |
| PO-L2-17 | **New (E1-F3).** Set 2 under G is closure-free: the shard's set 2 is (T_G ∩ Surv_G) ∪ F_G, with F_G evaluated by `l2plan` from Q⁰(R) and the frame alone; under the specification it equals T_G | **The equality is E1's** (Lemma G-D, proved in E1-F3 and `E1-NOTE-symmetry-and-G-D.md`, Corollary 2; confirmed in `E1-RECHECK-r2.md` §4). **Closure-freeness is proved here by construction:** `Space.c7_flags` reads Q⁰(R), its own cone and tip code and the frame (the union of the G cones of the fixed quantities and even port samples), and no closure. **Checked, toy only:** L2-SCOPE (on every toy record `l2plan`'s I_A, I_G, F_G, E_G equal those computed with `s0ref`'s contexts, tips and frame, and I_c equals the production context's); L2-F1. **The frame:** pre-flight `C12_universe` requires `l2plan`'s frame to equal the production frame on the box of radius n + 6 at slices −1 and 0 (toy: 129 cells, equal; on v8 this runs only in the authorized pre-flight, with B8's 833 cells). **Not checked on v8 in this revision:** the per-record predicates, beyond what the frame equality and the toy class show |
| PO-L2-18 | **New (E1-T2).** σ is derived as E1-T2 defines it: first matching case of 1 (a)–(c), 2 (a)–(d), 3 (a)–(c), else OK; every holding condition enters the label's reason lists; rule T is evaluated iff σ = OK; a rule-T outcome evaluated in a VOID, MISMATCH or INCOMPLETE run is recorded beside the label with no S1b proposal | **Proved here by construction** (`l2merge.sigma`, `rule_T`, `rule_T_record`; the label is computed by `label` from every reason list, and σ is not one of its inputs). The fields σ reads under case 2 are produced by `l2refcheck`, which imports only `s0ref` (L2-S1). That σ = OK certifies the bound is E1-T2's argument ("Why σ = OK certifies the bound"), which rests on C0, C17, C18, case 2 (d) and the closure code's retained/logged partition (a code invariant). **Checked:** L2-SIGMA (each of the ten conditions gives its case and `not_evaluated`; the valid run gives OK and an evaluated rule T), L2-PREC (σ = OK with a failing VOID gate, MISMATCH control or missing shard keeps that label, with the outcome beside it and no proposal), L2-2D, L2-T1; mutants M_ruleT_ignores_sigma, M_sigma_overrides_label, M_proposal_on_failed_label, M_sigma_no_2d, M_ruleT_reads_L3 |
| PO-L2-19 | **New (E1-F3).** `l2plan.Space.index_of` is the inverse of `s0geom.record_at` on the record space | **Proved here:** a closed form of the same order (singles by (site, slice); pairs by the lexicographic rank of the site pair i < j, i(n_s − 1) − i(i − 1)/2 + (j − i − 1), then (t1, t2)). **Checked, toy only:** L2-INDEX (every index, k = 2 and k = 1). Not checked on v8, which would need `record_at` on v8 |
| PO-L2-20 | **New (E1-F6).** The per-record masking-equivalence test: R is masking-equivalent iff the number of records of the space with R's canonical form (PO-L2-6), less one if R is in the space, is at least one | **Proved here** from PO-L2-6's canonical form: a class is empty-form (empty items only), one site (one non-empty item, the other item, if any, empty at another site) or two sites (two non-empty items), with the counts c_x(m), E_x and E_tot of PO-L2-6. **Checked:** L2-MASK, against brute force on every record of three toy variants |
| PO-L2-21 | **New (E1-F6).** The four added counts are preserved by the orbit-reduced computation | **Proved here given PO-L2-3:** each is a per-member contribution from the member's own record (stabilizer order, masking key) and its carried survivor status, both C4v-invariant (E1-F6), as the other degeneracy cells; in-run C8 compares every contribution, these four included, on directly closed orbits. **Checked:** `crosscheck_toy_counts` (58 equal, the four against an independent computation; all four are 0 on the toy class, which has no survivors); L2-COUNTS (a planted survivor orbit with a nontrivial stabilizer gives N_ST = 4 under A and G); `planted_survivor_path` |
| PO-L2-22 | **New (E1-F3).** H₁₀₀ and H₁₀₀₀ are deterministic functions of the record index, on two distinct streams, frozen in the configuration digest | **Proved here by construction** (`c7_sampled` hashes (salt, stream, `index_of(R)`)). **Checked:** L2-C7COV (the sampled records equal an independent hash over [0, N), and include non-representative records); L2-SAMPLE; mutant M_C7_sample_rep_index |
| PO-L2-23 | **New.** No record-enumerating count runs on v8's configuration class: `--shared-tips`, `shared_tip_records`, `c7_populations` and the record generator refuse a space whose (dim, n, port) are v8's before any record is formed | **Proved here by construction** (the first statement of each). **Checked:** L2-V8COUNTS (with a sentinel in place of the record generator, so that a missing refusal is detected without enumerating), `refusal_probe` (the command line, after the in-process refusal is confirmed); mutant M_v8_counts_unrefused |

Nothing in this table is claimed beyond its status. "Checked" items are evidence on the instances
named, not proofs.

## 10. Invariant → checkpoint (§A.41)

**Layer-1 invariants** (L1 §7). For each: the implementing code, its checkpoint in Layer 2, and the
local evidence (§12).

| L1 invariant | code | Layer-2 checkpoint | local evidence |
| --- | --- | --- | --- |
| configuration space and counts | `s0symcheck`, `l2plan.Space` | pre-flight `C0_v8_combinatorics`; dry run `expected_checks`; merge recount | symcheck exit 0; v8 dry run: 5,163,225 records, 816,050 orbits, group order 8 |
| C4v with correct orbit counts | `l2analysis.group`, `l2plan.orbits_burnside` | L2-ORB; merge recount | toy 488/1,400 |
| orbit representatives preserve every reported count (58, E1-F6); per-record results for invariant attributes | `l2enum.Shard.rep`, `l2analysis` | in-run C8 (1/100 orbits, survivor orbits, flagged orbits), contributions of all 58; merge recount | toy: all orbits, 0 failures; 58 counts equal to full computations (`crosscheck_toy_counts`) |
| source-dependent attributes per record | `l2analysis.post_closure` per member | C8 compares `g_linked` and `source_cells` with direct closure | toy C8 in-run, 0 failures |
| cones match the native rule | `s0geom.in_cone` | pre-flight C1 (full depths in CI) | quick C1: 5,000 perturbations, pass |
| tips bijective, off-axis not | `s0geom.tip_labels` | pre-flight C2 | quick: 133 tips, 8 contrasts |
| planted families survive; planted non-survivors collapse | — | pre-flight C3, C11 (iii) | quick C3 block (8, 0); C11 (iii) 96 sets, 0 failures |
| elimination exact | `s0native` | pre-flight C15 | quick: 0 violations (2^21, 2^18 worlds) |
| every logged elimination justified | `l2refcheck.c18`, `c18_stream` | pre-flight C18; in-run C18 (1/1,000; every survivor member); S1a C18 on both bounds | toy in-run 976 checks, 0; planted survivor orbits 16, 0 |
| every required elimination applied | `l2refcheck.c17`, `c7` | pre-flight C17, C7; in-run C17, C7 per record on E1-F3's scope; the unapplied-elimination mutant | killed at C17 |
| every eligible configuration considered | `l2enum.scan`, `l2merge.coverage_ok`, `recount_ok` | merge coverage and recount; C13; M_skip_index | killed at L2-ORB |
| planted survivors vs non-survivors (B, G, Φ- and frame-adjacent) | — | pre-flight C3, C6, C11 (iii) | pass |
| S6 | `s0s6` | pre-flight S6 | pass; positive control holds; negative control 64 non-target classes |
| v8 not run without authorization; refusal keyed on (dim, n, port) | `s0geom._guard`, `s0ref._ref_granted`, `l2auth`, `l2cert.startup`, `l2landing` | refusal check (46); L2-GUARD; L2-AUTH; L2-S1; L2-LAND; `refusal_probe` (entry points and forgeries) | 46/46; 9/9 entry-point attempts; 9/9 forgeries refused |
| frozen code and configuration are the ones run | `l2manifest`, `l2cert.startup` | items 1–3 at start-up; L2-MAN; placeholders refused for v8 | M_manifest_blind killed |
| no over-elimination in any convention, type or depth | — | C3, C15, C11 (i) and (iii), mutants | quick campaign 17/17 rule mutants |
| far tips load-bearing beyond L3 | — | C3 block minus centre; near-only mutant | killed at C3 |
| closure correct by independent code | `l2refcheck.c7`, `l2enum.Shard.c7_record` | pre-flight C6, C7; in-run C7 per record on sets 1–4 (E1-F3) | see `shard_toy_*` and `planted_survivor_path` (§12) |
| base context collapsed | `l2preflight.v8_execution` (v8); C6 toy | pre-flight `C6_execution` (MISMATCH); `base_collapsed` | toy base collapsed |
| monotonicity | `l2enum.c9_ok` | pre-flight C9; in-run C9 per member; S1a L3′ ⊆ L3 | toy in-run 2,800 checks, 0; M_c9_off killed |
| no fixed quantity eliminated | `l2enum.c10i_ok` | in-run C10 (i) on every closure (MISMATCH) | 1,952 checks, 0 |
| port samples in-frame under G | `l2preflight` | pre-flight C10 (ii) (toy), `C10ii_v8` (v8) | toy pass |
| per-direction tables match and decisions agree | `l2refcheck.c11i` | pre-flight C11 (i); in-run C11 (i) (every survivor member) | toy in-run 5,328 tables, 0 |
| P_A-dir, P_G-dir, P_A, P_G on survivors and planted sets | `l2refcheck.props` | pre-flight C11 (ii); in-run C11 (ii) on every survivor member | planted survivor run: 16 checks, 0 |
| planted directional retention | — | pre-flight C11 (iii) | 96 sets, 0 failures |
| per-direction control detects single-direction errors | — | pre-flight non-vacuity mutants; quick campaign | both demonstrations fail C11 only |
| every proof-dependent rule rests on a complete statement | — | document property; §9 for Layer 2's own | independent review |
| rule T applied as preregistered (with E1-T1 to E1-T6) | `l2merge.rule_T`, `rule_T_inputs`, `rule_T_record` | `result.json` `rule_T`; L2-RT, L2-T1, L2-T6; M_ruleT_or, M_ruleT_reads_L3 | toy: evaluated, recorded |
| frame is B8; in-frame cones stay in it; `l2plan`'s frame (C7's closure-free selection) equals the production frame | `l2preflight.c12_universe` | pre-flight C12, `C12_universe` | toy: 129 = 129 = `l2plan`'s, 15 in-frame quantities checked |
| design evidence retained and deterministic | `l2run` | `RUN-MANIFEST`, `-O` identity | §12 |
| Layer-2 evidence structured, complete, retained | `l2merge`, `l2cert` | items 5, 7, 8; residue completeness; commit binding; certificate | toy certificate holds |
| the frozen files are unchanged and E1's quotations stand (E1 §10, row 1) | — | `E1-check` part A, replayed by `e1check_replay` | identical to `e1_check.out` |
| integer-only, no repository read in the engine | — | C14 (extended) | pass |
| minimal witness well defined | `l2enum.Shard.add_witness`, `l2merge.minimal_witness` | C16; L2-WIT; L2-C16; planted negative control | M_witness_first and M_witness_max killed |
| distinguishability classes (a)–(c) | `l2analysis.post_closure`, canonical keys | C8 (invariant parts), C7 | toy |
| every control can fail | — | the mutant campaign, quick now and full in CI | 47/47 quick |

**Layer-1 controls** (L1 §6). For each: the implementing code, where it runs, and its class on
failure.

| control | code | where it runs | class |
| --- | --- | --- | --- |
| C0 | `s0symcheck.py`; `s0controls.c0_context_sizes`; `l2enum` reference contexts | pre-flight; in-run (every reference context); dry run (counts) | VOID |
| C1, C2 | `s0controls.c1_cones`, `c2_tips` (native lanes) | pre-flight (full depths) | VOID |
| C3 | `s0controls.c3_planted` | pre-flight | VOID |
| C6 | `s0controls.c6_hand` (toy); `l2preflight.v8_execution` (base, (q9, 9)) | pre-flight | toy VOID; execution instances MISMATCH |
| C7 | `s0controls.c7_reference`; `l2refcheck.c7`; `l2enum.Shard.c7_orbit`, `c7_record` (E1-F3) | pre-flight (every toy record); in-run (per record, sets 1–4) | VOID |
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

**Erratum E1's invariants** (E1 §10). For each: E1's checkpoint and its Layer-2 implementation.

| E1 invariant | E1 checkpoint | Layer-2 checkpoint | local evidence |
| --- | --- | --- | --- |
| rule T reads L_A and L_G from the L3′ bound; the L3 values are reported only (E1-T1) | `result.json` `rule_T` fields; a self-test with differing L3′ and L3 outcomes; `E1-check` part G | `s1a.json` `L_bound_rule`, `L_reported_L3`; `result.json` `rule_T.bound_rule`, `rule_T.L_reported_L3`; L2-T1; M_ruleT_reads_L3 | L2-T1 passes; mutant killed |
| rule T is evaluated iff σ = OK, with σ as in E1-T2 | `result.json` `S1a.status` and reasons; self-tests 1 (a)–(c), 2 (a)–(d), 3 (a)–(c); a status-ignoring mutant killed | `l2merge.sigma`; `result.json` `S1a.status`, `S1a.status_reasons`; L2-SIGMA (ten conditions); M_ruleT_ignores_sigma | L2-SIGMA passes; mutant killed |
| L_G counts by the quantity's cone (E1-T5) | `s1a.json` L_G; a planted-bound self-test with a tip-reading mutant killed; `E1-check` part G | `l2s1a.linked_counts`, `l2refcheck.ref_linked_counts`; L2-T5 on the toy L3′ bound (L_G = 7 > 0); M_LG_tip_reading | L2-T5 passes; mutant killed |
| the cost clause is recorded as not evaluable in Stage 0 (E1-T3) | `result.json` `rule_T.cost_clause` | `rule_T.cost_clause` from `l2config` | toy `result.json` |
| the consequence rests on §1, §2, PO4 and PO7 (E1-T4) | document property; E1's review | PO-L2-7 (§8) | document property |
| C7 runs per record on sets 1–4 of E1-F3, with H₁₀₀ and H₁₀₀₀ deterministic over record indices and frozen before any v8 output | per-set C7 tallies; configuration digest; self-tests; `E1-check` part J | `l2enum.Shard.c7_orbit`, `c7_record`; shard and `result.json` `C7_scope_coverage`; `l2config` `C7_samples` in the configuration digest; L2-C7COV, L2-INDEX; PO-L2-16, PO-L2-19, PO-L2-22 | toy coverage equal to E1-check part J (§12) |
| "shared near tip" is the shared tip of PO3 (b) | `E1-check` part F | `l2plan.shared_near` agrees with `s0ref`'s and the production context's on every toy record (L2-SCOPE) | L2-SCOPE passes |
| the count list has 58 counts and cross-tabulates every §3 degeneracy with survivor status | `E1-check` part B | `l2analysis.reported_count_keys`; L2-COUNTS (58 keys, rank 3 per degeneracy); M_counts_54 | L2-COUNTS passes; mutant killed |
| the four added counts are preserved by orbit reduction | C8 (pre-flight and in-run); `E1-check` parts C–E | in-run C8 over the 58 contributions; `crosscheck_toy_counts`; PO-L2-21 | 58 equal; N_ST = 4 on the planted orbit |
| Lemma G-D | toy whole-class check (`E1-check` part H); the per-record check of sets 3–4 when the G-D form is enabled (§9) | the G-D form is not implemented (owner decision G_D open); `E1-check` part H, replayed by `e1check_replay` | identical to `e1_check.out` |
| set 2 is closure-free under G | F1 self-test and the computed-closure mutant (`E1-check` part I) | L2-F1 (595 of 595 affected records caught); M_C7_set2_computed; PO-L2-17 | L2-F1 passes; mutant killed |
| per-record C7 detects member-only faults | F2 self-test (`E1-check` part I) | L2-F2 (312 of 312, with no carried result wrong); M_C7_carried_only | L2-F2 passes; mutant killed |
| σ is diagnostic and never overrides the run label | label self-test: σ = OK with another failing check gives that check's label (`E1-check` part K) | L2-PREC; M_sigma_overrides_label, M_proposal_on_failed_label | L2-PREC passes; mutants killed |
| L_A and L_G reference recomputation | case 2 (d) self-test with a perturbed production count (`E1-check` part K) | `l2s1a` `L_reference`; `l2merge.sigma` case 2 (d); L2-2D (both at the S1a and at the merge level); M_sigma_no_2d | L2-2D passes; toy recomputation 15 and 7 |
| rule T's statement scope | `result.json` `rule_T.statement_scope` | L2-T6: E1-T6's text verbatim in `l2config` and in `result.json` | L2-T6 passes |
| record-index sampling | sampling self-test (`E1-check` part J) | L2-C7COV, L2-SAMPLE; M_C7_sample_rep_index | passes; mutant killed |
| coverage reporting, raw and orbit-level | shard and `result.json` fields; `E1-check` part J | `C7_scope_coverage` (records checked and failed, orbits touched, sum of sizes, skipped beyond the cap) | toy `result.json` |

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
| C7's samples are over record indices | L2-C7COV, L2-INDEX; M_C7_sample_rep_index |
| no record-enumerating count runs on v8 | L2-V8COUNTS, `refusal_probe`; M_v8_counts_unrefused |
| the v8 profile is refused while κ, G_D or O1 is open, with no value for κ anywhere | L2-PLACEHOLDER; M_placeholders_ignored |
| the Layer-2 code and toy run keep every value E1-check verified | `e1check_replay` (output identical to `e1_check.out`) |
| masking count reading | L2-MASK (three toy variants, both readings); M_mask_no_merge |
| behaviour of the copied engine preserved | `code_r5_equivalence_quick` |

## 11. CI workflow design (proposal only; no file is added under `.github/`)

Two dispatch-only workflows, each launched only on the owner's separate approval (§A.43 item 4), on
a branch whose head is the frozen Layer-2 commit, after the open decisions of §4.2 (κ, G_D, O1) are
recorded.

**A. `np-avg-1-stage0-mutants` (the full campaign, item 3).**
- **Inputs:** none.
- **Jobs:**
  - `preflight-toy`: `l2preflight.py --profile toy`, full mode.
  - `mutants`: `l2mutants.py --full`, which needs the first job's `preflight.json`. The 17 rule
    mutants run the whole full suite, the 2 equivalents run, and the 30 machinery mutants run
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
     - `l2calib.py`, then `l2plan.py --profile v8 --calib calib.json --out dryrun.json`.
       `--shared-tips` is refused on v8 in this revision, so the C7 term's inputs (|F_G|, |I_A|,
       |I_G|) are "not computed" and `launch_within_budget` is `null`: this workflow cannot launch
       until a separate owner decision authorizes a combinatorial-only count of them and a Layer-2
       amendment adds a grant-gated path for it (see `KAPPA-PROPOSAL.md` §4 for the sequence).
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

Run by `code/l2run.py` with `python3 -I -B` on Python 3.13.16, in about ten minutes. Every step's
stdout and stderr is in `runs/`. `RUN-MANIFEST.json` records:
- commands, exit codes and durations;
- `-O` identity, by stdout or by the files written;
- SHA-256 values of code, outputs, toy-run files and the κ calibration file;
- the HEAD at run time and whether the Layer-2 tree was clean.

**Commit caveat (L2-R5).** The evidence was produced on an uncommitted working tree. The structured
files record the HEAD at run time (`53786e6e`) and `tree_clean = false`; the commit binding holds
among them (one commit throughout), but that commit does not contain these files. They are design
evidence only. At the Layer-2 freeze the evidence is regenerated at a recorded commit.

| step | result |
| --- | --- |
| `manifest_verify` | the manifest matches |
| `l2_selftest` | 34 cases pass: the 20 of r2 and L2-INDEX, L2-SCOPE, L2-C7COV, L2-F1, L2-F2, L2-SIGMA, L2-PREC, L2-T1, L2-T5, L2-2D, L2-COUNTS, L2-V8COUNTS, L2-T6, L2-PLACEHOLDER |
| `calibration_planted` | timings on planted sets (not deterministic) |
| `dryrun_toy` | 1,400 records, 488 orbits, 4 shards; masking-equivalent 1,398 in both readings; C7 populations I_A 1,071 (432 orbits), I_G 667 (307), F_G 595 (283), E_G 12 (6); the complete estimate with the C7 term evaluated; launch not decided (κ is a placeholder) |
| `dryrun_v8_plan_no_closure` | v8 shard plan without enumeration or closure: 5,163,225 records, 816,050 orbits (875 + 815,175), group order 8, 32 ranges; non-fixed context sizes up to 29 (37 with the fixed quantities); `closures_computed = 0`; C7 populations "not computed (requires authorization)" |
| `dryrun_v8_estimate` | see below |
| `preflight_toy_quick` | every pre-flight control passes (quick mode): refusal 46 of 46; C11 (iii) 0 failures; both direction mutants fail C11; S6 pass; the Layer-2 self-test; C12 on the toy universe, with `l2plan`'s frame equal to the production frame (129 cells) |
| `mutants_quick` | 47 of 47 killed at their named cases: 17 rule mutants (L1 §6 table) and 30 machinery mutants, including the twelve r3 mutants M_C7_set2_computed (L2-F1), M_C7_carried_only (L2-F2), M_C7_sample_rep_index (L2-C7COV), M_ruleT_ignores_sigma (L2-SIGMA), M_sigma_overrides_label and M_proposal_on_failed_label (L2-PREC), M_sigma_no_2d (L2-2D), M_ruleT_reads_L3 (L2-T1), M_LG_tip_reading (L2-T5), M_counts_54 (L2-COUNTS), M_v8_counts_unrefused (L2-V8COUNTS) and M_placeholders_ignored (L2-PLACEHOLDER). Machinery mutants run against their named case only in the quick campaign. The two demonstrations fail C11 only, with counts equal to the frozen rule's |
| `s1a_toy` | σ fields all clean (status OK); L_A = 15, L_G = 7, equal to their `s0ref` recomputation, L3 values likewise (toy geometry, not a statement about v8) |
| `shard_toy_0`…`3` | 488 representatives; C0 1,584, C7 608 records (per record, sets 1–4), C8 488 orbits, C9 2,800, C10 (i) 1,952, C11 (i) 976 (5,328 tables), C17 976, C18 976; 0 failures; no survivors. C7 coverage, records / orbits touched / sum of their sizes: A set 3 12 / 12 / 45, set 4 1 / 1 / 4; G set 2 595 / 283 / 595, set 3 6 / 6 / 24, set 4 1 / 1 / 4; sets 1, and set 2 under A, empty. These equal E1-check part J's populations |
| `merge_toy` | COLLAPSE_ALL on the toy class (design evidence, no statement); 58 counts; σ OK; rule T evaluated (toy L_A = 15 > 0, so its outcome is the S1b branch; toy geometry); coverage exact; recount 1,400 and 488; residue complete |
| `certificate_toy` | items 1–8 hold, including the commit binding (item 3 with the quick campaign, which the toy profile admits) |
| `crosscheck_toy_counts` | all 58 merged counts equal full per-record computations: the 54 against code-r5's control suite, the four added against an independent computation with `code-r5/s0ref.py` (all 0: the toy class has no survivors); the marginals 1,398 and 1,176 likewise; 36 counts identically zero |
| `e1check_replay` | E1-check, run against r3's code and toy run, exits 0 and prints output byte-identical to `e1_check.out` (SHA-256 `d2297fb7…8542`) |
| `code_r5_equivalence_quick` | the quick suite equals code-r5's except the extended refusal block |
| `planted_survivor_path` | the survivor path on planted toy records (two orbits of 4): C7 on set 1 runs on all 8 members in both conventions (16), with its C0 check; C11 (i), C17, C18 16 each, C0 32, 0 failures; N_ST = 8 under A and under G; negative control: a bound missing one retained quantity gives C9 failures and a running-minimum witness |
| `refusal_probe_v8` | 9 of 9 entry-point attempts refused with VOID and item 6, before any file is written; 9 of 9 forgeries refused; `l2plan --profile v8 --shared-tips` refused (exit 2), after the function-level refusal is confirmed in-process; `decide()` on fabricated inputs returns `ok`, recorded as the documented limit |
| `kappa_calibration_repeats` | timing data for `KAPPA-PROPOSAL.md`: 5 normal and 5 `-O` calibrations, the v8 estimate's spread across them, and toy-record timings (not deterministic) |

Every deterministic step is `-O`-identical.

**Not run locally, pending.**
- The full mutant campaign: the full suite for every rule mutant, every self-test case for every
  machinery mutant, and the equivalent mutants. It is CI-only and needs an owner-approved dispatch.
- The full-depth control suite (C1 F 0–15, B 0–8, G 0–23, …). It runs in CI pre-flight.
- Any shared-tip, F_G or other record-enumerating count on v8 (refused; §3.6).
- Everything on v8's class.

**The v8 cost estimate** from the step's calibration (planted sets on this machine; timings vary
between runs; `runs/dryrun_v8_estimate.out`), in runner-seconds:

| term | runner-seconds |
| --- | --- |
| closures (with overhead 2 and the `-O` copy) | 65,383 |
| sampled gates (C11 (i), C17, C18 at 1 in 1,000; C8 at 1 in 100) | 2,495 |
| survivor gates, capped at 10 orbits per shard (includes C7 set 1) | 7,587 |
| S1a | 536 |
| pre-flight | 300 |
| merge | 600 |
| **known terms** | **76,900 (about 21.4 h)** |
| C7 set 4 (H₁₀₀₀, expected size N/1,000) | 1,968 |
| C7 sets 2 and 3 | not computed (requires authorization): 0.309 s per F_G record, 0.000727 s per I_A record and 0.003084 s per I_G record (central) |

Over the ten calibrations of `kappa_calibration_repeats` the known terms plus set 4 have median
72,977 s, CV 5.8 % and max/median 1.161. Even with every unknown input at zero they leave the launch
rule room only for κ ≤ 1.18 under S7's 24 runner-hours (`KAPPA-PROPOSAL.md` §c). No launch decision is
computed: κ is a placeholder and the C7 inputs are not computed.

## 13. Findings: status after the review and erratum E1

**Resolved by E1** (in effect): T1, T2 (with case 2 (d) and the diagnostic status), T5, T6 (the
standing of rule T's consequence), T3 and T4 (notes), F3 (C7's scope) and F6 (58 counts). Layer 2
implements them as §4.2 states.

**Other findings.**
- **F1:** accepted reading (§4.1).
- **F2:** moot while F1 holds; to be fixed in any BASE_RESIDUE amendment.
- **F4, F5, F7, F8, F10, F11:** accepted readings (§4.1).
- **F9 / κ:** open owner decision on κ and the budget (S7). `KAPPA-PROPOSAL.md` sets out the cost
  model, the calibration spread and a proposed value for the owner; it sets nothing.

**Open owner decisions** (placeholders; the v8 profile is refused while any is open): κ, G_D, O1.

**Points where E1 is ambiguous, or not implementable as written now** (reported, not resolved):
1. **The dry run's |F_G| on v8.** E1-F3's checkpoint says "The dry run computes |F_G|, records and
   orbits, without any closure, and the C7 cost term from it (L2-R6)", and E1 §9 ties the G-D and κ
   decisions to "once the dry run reports |F_G|". Counting F_G on v8 enumerates v8's record space,
   which is not authorized. Layer 2 computes it on the toy profile and reports it on v8 as "not
   computed (requires authorization)"; the v8 C7 term is a formula. A separate owner decision is
   needed before either decision E1 §9 describes can be taken on the v8 number.
2. **A Layer-2 self-test of the G-D form.** E1-F3's checkpoint lists "Lemma G-D's form equals the full
   reference on the toy class" among Layer-2 self-tests, while E1-F3's check bullet and E1 §9 keep
   the G-D form non-executing until the owner confirms the proof. Layer 2 does not implement the G-D
   form at all; the toy-class equivalence is E1-check part H's (outside Layer 2), which
   `e1check_replay` re-runs unchanged.
3. **"Computed closure" when both a carried and a direct closure exist.** E1-F3 defines the computed
   closure as the carried one "or R's direct closure where the run computes one". Layer 2 uses the
   carried result for set membership; on directly closed orbits C8 fails VOID on any difference, so
   the two readings give the same failure outcome (§4.1).
4. **Set 1 and the survivor cap.** E1 asks for every survivor; Layer 2's cap (L2-R3) skips set-1 C7
   beyond the cap and makes the run INCOMPLETE. No survivor goes unchecked in a run that is not
   INCOMPLETE, but a capped run checks fewer than every survivor (§4.1).
5. **Where `rule_T.statement_scope` is recorded.** E1-T6 says `result.json` records the text under
   that field; Layer 2 records it in every outcome, not only the zero branch (§4.1).
6. **σ case 1 (a)** names a missing output and a refused start; Layer 2 also treats an output
   lacking a field σ reads as case 1 (a) (§4.1).

## 14. Freezing Layer 2

After the re-review of r3, and once the owner has decided κ, G_D and O1 (and, for the C7 term, any
authorization of a combinatorial-only v8 count of F_G and I_c, with the Layer-2 amendment it needs):
1. Replace the placeholders in `l2config` with the decisions, and apply any accepted changes.
2. Regenerate `LAYER2-MANIFEST.json`, commit, and re-run `l2run.py` at that recorded commit, so that
   the design evidence's commit is the freeze commit's parent or the freeze commit itself, as the
   freeze note states.
3. Record the plan's SHA-256, the manifest's `code_digest` and the configuration digest in a freeze
   note.

Before any v8 dispatch, the owner then makes three separate decisions: the workflow edit, the full
mutant campaign, and the enumeration itself, by an authorization artifact naming the frozen commit
and `code_digest`.

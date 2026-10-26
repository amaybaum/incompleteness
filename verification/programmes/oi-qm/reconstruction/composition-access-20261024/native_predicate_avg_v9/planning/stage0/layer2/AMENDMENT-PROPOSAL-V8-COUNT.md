# NP-AVG-1 Stage 0 Layer 2: amendment proposal, the v8 population count (unadopted; r5)

**Status: a design for review. It is not adopted, not implemented, and authorizes nothing.** The v8
count-only pass "stays unauthorized pending its Layer 2 amendment and review" (owner, 2026-10-26).
Layer 2 refuses every record-enumerating count on v8 (`LAYER2-PLAN.md` §3.6, PO-L2-23). This
document sets out the amendment that would add one, so that it can be reviewed before any decision.

**r5 (LAYER2-R4-REVIEW §7, A1–A4).** The representatives-per-shard count is split off (A2): it is the
site-pair count, which the owner has conditionally approved as a separate count-only diagnostic and
which is implemented on its own (`SITE-PAIR-COUNT.md`, `code/l2sitepairs.py`); this proposal no longer
computes it. A1 adds an engine-side mutant and a no-subclass requirement (§3). A3 and A4 are measured
on the mid-size analogue (§3a, §4). Its compute time counts in the campaign's 24-hour ceiling (owner:
"Include calibration, count pass, primary run, mutant campaign, retries, and execution overhead").

## 1. Purpose and sequencing

The pass computes the closure-free C7 populations of erratum E1 (item E1-F3) on v8's record
space: |I_A|, |I_G|, |F_G| and |E_G|, each as records and as orbits. They are the inputs of C7's cost
term, and of the G_D and O1 decisions (E1 §9).

The owner's sequencing (2026-10-26: "Approved. Fix κ, the survivor cap, and budget ceiling before any
v8 count.") puts the pass after those three decisions, and G_D and O1 after it, before the full run.

**The pass also computes** the timing of the pass itself. The representatives per shard are not part
of it (A2): they come from the site-pair count (`SITE-PAIR-COUNT.md`), which needs no Q⁰, frame or
predicate and can be ruled on separately, before the cap is fixed.

**It computes no context through the engine, no closure, no survivor status and no count of the
reported list.** It is combinatorics over Q⁰(R), the frame and the group action, as the toy dry run
does.

## 2. What the amendment changes

1. **`l2plan.py` gains one authorized path.** `c7_populations` runs on v8 only when given a count
   grant:
   - a new token type, `V8CountGrant`, constructed only by `l2auth.issue_count_grant`;
   - its scope is the literal string "NP-AVG-1 Stage 0 v8 combinatorial count only";
   - it is bound to the commit, the `code_digest` and the configuration digest, as `V8Grant` is;
   - **it does not subclass `V8Grant`, and `V8Grant` does not subclass it** (A1); the engine's
     `_guard` checks the exact type, so neither a subclass nor a token with the same digests passes.

   `refuse_v8_enumeration` accepts that token and nothing else. `V8Grant` (the enumeration grant) is
   refused there, and the count grant is refused by every engine and reference entry point (`Context`,
   `record_at`, `num_records`, `record_samples`, `ref_context`). That keeps the two authorizations
   disjoint.
2. **`l2auth.py`:** `decide_count()` checks the same inputs as `decide()`, with its own scope and its
   own required designation line: `NP-AVG-1 Stage 0 v8 count-only pass authorized at <commit>
   code_digest <digest>`.
3. **A sharded entry point**, `l2count.py --shard s`:
   - It runs the count on the enumeration's shard ranges, by record index, enumerating records with
     `l2plan`'s own generator.
   - It writes `count-<s>.json`: records and orbits per predicate, the range, digests, the commit and
     the grant echo. It records no closure and no per-record result.
   - A merge, `l2count_merge.py`, checks the exact cover and disjointness of the ranges and writes
     `counts.json`, a structured file.
4. **The dry run reads `counts.json`** when present (matching digests), and only then reports the C7
   term, the total, the job estimates and the launch decision.
5. **Configuration:** the count's shard count and timeouts as constants under certificate item 1.

## 3. Controls

| control | what it shows |
| --- | --- |
| **import trap** | `l2count.py` and `l2count_merge.py` run with `s0geom`, `s0ref`, `s0native`, `l2analysis`, `l2refcheck`, `l2enum` and `l2s1a` unimportable, and complete; the review's import trap on the dry run is the model |
| **toy equivalence** | on the toy profile, the sharded count equals `c7_populations` and E1-check's populations (I_A 1,071; I_G 667; F_G 595 in 283 orbits; E_G 12) |
| **mid-size equivalence (A3)** | on the mid-size analogue (§3a), `l2plan`'s Q⁰ and I_A, I_G equal the production context's on a sample, and `l2plan`'s frame equals the production frame; to be extended to F_G and E_G against `s0ref` on a sample before the v8 count |
| **grant separation** | the count grant is refused by every engine and reference entry point; the enumeration grant is refused by the count path; default, `True`, subclass, duck-typed and forged-digest grants are refused by both (a probe as `refusal_probe`) |
| **sentinel** | a self-test with the record generator replaced by a sentinel shows that without a count grant nothing is enumerated on v8 (as L2-V8COUNTS) |
| **determinism** | normal and `-O` shard files byte-identical; the merge refuses differing digests or an inexact cover (INCOMPLETE) |
| **mutants** | the refusal removed (killed by the sentinel case); the enumeration grant accepted by the count path; **the engine's `_guard` accepting a `V8CountGrant`, through a subclass or a token with the same digests (A1; killed by the grant-separation probe)**; a skipped index (killed by the cover check); orbits counted by representative index instead of the canonical test (killed by toy equivalence) |
| **landing** | the designation re-fetched from the host and checked, as `l2landing.py` does for the enumeration |

### 3a. A3, measured on the mid-size analogue

`design/midsize_validation.py` (step `midsize_validation`; profile `mid`: v8's dim, n, slices and
sources, region ball(2), port (0, 0, −2), not v8's class) checked every 97th record (1,940 records):
`l2plan`'s Q⁰ equals the production context's quantities, and its I_A and I_G equal the production
shared-near-tip test, with 0 disagreements; `l2plan`'s frame equals the production frame on the C12
box. Contexts there reach 27 quantities, against at most 8 on the toy. F_G and E_G rest on that frame
and the same tip code; their reference check against `s0ref` is on the toy class only, and the
extension above is proposed before the v8 count.

## 4. Cost and limits (for the owner's authorization)

- **Cost (A4, measured on the analogue).** `c7_populations` over the mid profile's 188,125 records
  took about 115 s on this machine, about 0.61 s per thousand records, at contexts up to 27
  (`design/midsize/validation.json`). Scaled linearly in records to v8's 5,163,225, that is about
  3,200 s (0.9 single-core hour), sharded into the enumeration's 32 ranges. The scaling in records is
  an assumption (v8's contexts have the same size distribution per slice pair, its region is larger),
  not a measurement on v8. The pass would time itself and retain the timing; its timeouts would be set
  from this measurement with the κ rule.
- **Budget.** Its compute time counts in the campaign's 24-hour ceiling (owner, 2026-10-26: the count
  pass is included).
- **What it does not authorize.** No closure, no grant for the engine, no S1a, no pre-flight on v8
  and no enumeration.

## 5. Review questions

1. Are the two grants disjoint in every entry point, statically and at run time?
2. Does the import trap cover every module that can construct a context or a closure?
3. Is the population definition the one E1-F3 and Lemma G-D state (Q⁰, In/Out by the frame, near
   tips; E_G with eligible tips)?
4. Is the engine's guard closed against the count grant by type, not by digest (A1)?
5. Are the counts retained under §A.42, with a reproduce recipe, before the decisions that use them?

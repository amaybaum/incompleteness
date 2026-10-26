# NP-AVG-1 Stage 0 Layer 2: amendment proposal, the v8 count-only pass (unadopted)

**Status: a design for review. It is not adopted, not implemented, and authorizes nothing.** The v8
count-only pass "stays unauthorized pending its Layer 2 amendment and review" (owner, 2026-10-26).
Layer 2 r4 refuses every record-enumerating count on v8 (`LAYER2-PLAN.md` §3.6, PO-L2-23). This
document sets out the amendment that would add one, so that it can be reviewed before any decision.

## 1. Purpose and sequencing

The pass computes the closure-free C7 populations of erratum E1 (item E1-F3) on v8's record
space: |I_A|, |I_G|, |F_G| and |E_G|, each as records and as orbits. They are the inputs of C7's cost
term, and of the G_D and O1 decisions (E1 §9).

The owner's sequencing (2026-10-26: "Approved. Fix κ, the survivor cap, and budget ceiling before any
v8 count.") puts the pass after those three decisions, and G_D and O1 after it, before the full run.

**The pass also computes:**
- the number of representatives per shard of the enumeration's shard plan, which the survivor-cap
  model needs (`SURVIVOR-CAP-PROPOSAL.md` §3);
- the timing of the pass itself.

**It computes no context through the engine, no closure, no survivor status and no count of the
reported list.** It is combinatorics over Q⁰(R), the frame and the group action, as the toy dry run
does.

## 2. What the amendment changes

1. **`l2plan.py` gains one authorized path.** `c7_populations` and `shard_representatives` run on
   v8 only when given a count grant:
   - a new token type, `V8CountGrant`, constructed only by `l2auth.issue_count_grant`;
   - its scope is the literal string "NP-AVG-1 Stage 0 v8 combinatorial count only";
   - it is bound to the commit, the `code_digest` and the configuration digest, as `V8Grant` is.

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
   - It writes `count-<s>.json`: records and orbits per predicate, representatives per shard, the
     range, digests, the commit and the grant echo. It records no closure and no per-record result.
   - A merge, `l2count_merge.py`, checks the exact cover and disjointness of the ranges and writes
     `counts.json`, a structured file.
4. **The dry run reads `counts.json`** when present (matching digests), and only then reports the C7
   term, the total, the job estimates and the launch decision.
5. **Configuration:** the count's shard count and timeouts as constants under certificate item 1.

## 3. Controls

| control | what it shows |
| --- | --- |
| **import trap** | `l2count.py` and `l2count_merge.py` run with `s0geom`, `s0ref`, `s0native`, `l2analysis`, `l2refcheck`, `l2enum` and `l2s1a` unimportable, and complete; the review's import trap on the dry run is the model |
| **toy equivalence** | on the toy profile, the sharded count equals `c7_populations` and E1-check's populations (I_A 1,071; I_G 667; F_G 595 in 283 orbits; E_G 12), and the per-shard representatives equal the toy scan's |
| **grant separation** | the count grant is refused by every engine and reference entry point; the enumeration grant is refused by the count path; default, `True`, subclass, duck-typed and forged-digest grants are refused by both (a probe as `refusal_probe`) |
| **sentinel** | a self-test with the record generator replaced by a sentinel shows that without a count grant nothing is enumerated on v8 (as L2-V8COUNTS) |
| **determinism** | normal and `-O` shard files byte-identical; the merge refuses differing digests or an inexact cover (INCOMPLETE) |
| **mutants** | the refusal removed (killed by the sentinel case); the enumeration grant accepted by the count path; a skipped index (killed by the cover check); orbits counted by representative index instead of the canonical test (killed by toy equivalence) |
| **landing** | the designation re-fetched from the host and checked, as `l2landing.py` does for the enumeration |

## 4. Cost and limits (for the owner's authorization)

- **Cost.** The toy enumeration of the populations takes about 0.45 s for 1,400 records, about
  0.3 ms per record at toy context sizes (at most 8 quantities). At v8's mean context size of 16 the
  per-record work, linear in the number of quantities, would be about 0.6–1 ms. Over 5,163,225 records
  that is about one to two single-core hours, sharded into the enumeration's 32 ranges. This is an
  extrapolation from toy timings, not a measurement on v8. The amendment would time the pass and
  retain the timing.
- **Budget.** It runs as a separate dispatch under its own authorization. Its runner time counts
  against whatever budget the owner sets for it, not against the enumeration's 24-hour ceiling,
  unless the owner rules otherwise.
- **What it does not authorize.** No closure, no grant for the engine, no S1a, no pre-flight on v8
  and no enumeration.

## 5. Review questions

1. Are the two grants disjoint in every entry point, statically and at run time?
2. Does the import trap cover every module that can construct a context or a closure?
3. Is the population definition the one E1-F3 and Lemma G-D state (Q⁰, In/Out by the frame, near
   tips; E_G with eligible tips)?
4. Is the per-shard representative count the same quantity the survivor-cap model needs?
5. Are the counts retained under §A.42, with a reproduce recipe, before the decisions that use them?

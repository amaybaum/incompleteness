# NP-AVG-1 Stage 0 Layer 2: the site-pair count, for review and authorization (r5)

**Status: implemented, unreviewed, not dispatched.** The owner (amaybaum, 2026-10-26) ruled on the
v8 site-pair count: "Conditionally approved as a separate, strictly count-only diagnostic, after
independent review of its exact implementation", with these restrictions:
- "Access only the minimum v8 index metadata required to count records by site pair.
- No survivor evaluation, statistical estimation, outcome inspection, or experimental computation.
- No persistence of individual v8 records or hidden result information.
- Publish the exact counting algorithm and its permitted outputs before dispatch.
- Obtain independent review and green tests of the count-only implementation."

"This is not authorization to dispatch the count yet. Return with the exact reviewed implementation
and its resource limit for authorization." This document and `code/l2sitepairs.py` are that return.
**Nothing has run on v8:** the module refuses v8 without an authorization of its own scope, and every
test below runs on the toy profile, the mid-size analogue or ball(1)–(3) analogues, never on v8's
region (ball(4) is not run, since its counts would be v8's).

## 1. What it is for

The deterministic shard subdivision (`LAYER2-PLAN.md` §3.5; the owner: "investigate deterministic
subdivision of heavy site pairs into smaller shards") cuts the record index space at representative
ranks. On v8 the cut points need the representatives per site pair. Those counts are this module's
only output. They settle the representative balance of the shards exactly (the per-job inequality,
LAYER2-R4-REVIEW K1) and the survivor cap's shard weights (K2). They do not settle cost balance
(§6).

## 2. The algorithm (exact; the module docstring is the authoritative text)

Inputs, read from the profile's setup: dim, rho, tlast and the port. Nothing else.
- **Region:** the sites x ∈ Z^dim with |x|₁ ≤ rho, in lexicographic order (site index i).
  **Slices:** −1 … tlast (nt of them).
- **Group:** the signed coordinate permutations that map the region onto itself and fix the port and
  the two axis points (0, …, 0, ∓1). For v8 this is C4v, order 8.
- **A single site i:** nt records. nt representatives if i is the least site of its group orbit,
  else 0.
- **A site pair i < j:** nt² records ((i, t1), (j, t2)). A record is a representative iff no group
  image precedes it in the record order (first site, its slice, second site, its slice). For an
  element with images (a, b) of (i, j):
  - min(a, b) < i, or a = i and b < j: every image precedes its record, so the pair has 0
    representatives;
  - b = i (the element carries j to i): the image is (i, t2, a, t1), which precedes the record iff
    t2 < t1, or t2 = t1 and a < j. A representative therefore needs t1 ≤ t2 if a ≥ j, and t1 < t2 if
    a < j;
  - otherwise: no constraint.

  The pair's count is 0, nt², nt(nt + 1)/2 (t1 ≤ t2) or nt(nt − 1)/2 (t1 < t2): the strictest
  constraint over the group decides. The four values are distinct for nt ≥ 2, so the planner recovers
  each pair's in-pair rule from its count alone.
- **Totals:** N = Σ records; R = Σ representatives. R must equal Burnside's orbit count, computed
  independently from fixed points. If it does not, the count is VOID and nothing is written.

The loop runs over site indices and group images only. No record, slice pair or (site, slice) item is
formed.

## 3. Permitted outputs, exactly

The output object has exactly these keys, each of its stated type, validated before the file is
written:
- `schema`, `profile`, `setup` (dim, rho, tlast, port), `nt`, `sites`, `site_pairs`;
- `singles_representatives`: an integer per site, in index order;
- `pairs_representatives`: an integer per site pair, in index order;
- `records_total` (N), `representatives_total` (R), `burnside_orbits`;
- `module_sha256`, and `authorization` (the decision string).

Nothing else is written or printed. Any other key or type, or R ≠ Burnside, makes the output VOID.

**On v8:** 129 sites and 8,256 site pairs, so the output is 8,385 small integers plus the totals.
`N` (5,163,225) and Burnside's orbit count (816,050) are already reported by the dry run under its
standing permission.

## 4. The guards

| restriction | mechanism | test (L2-COUNTONLY unless stated) |
| --- | --- | --- |
| minimum index metadata | inputs are dim, rho, tlast and port only; the algorithm forms no record | review of the ~60-line `count`; L2-SHARDPLAN checks its results against the engine's canonical-image test |
| no survivor evaluation or experimental computation | static: imports limited to `hashlib`, `json`, `os`, `sys`, `resource`, `subprocess` (for the authorization's git facts, before the guard), `itertools` and `l2config`; at run time: no engine, reference, analysis or run module loaded at start or at the end; after the authorization step an audit hook refuses every import | static import check; a planted engine import is refused (VOID) |
| no outcome inspection | the audit hook refuses every file open except the single write of the output file | a planted read of an outcome file (`result.json`) is refused |
| no persistence of records or hidden information | the output is validated to exactly the permitted keys and types; the audit hook refuses any second file, process launch, network call, removal or rename; standard output and error refuse writes until the validated object is emitted | a record added to the output, a side file, and a printed record are each refused (VOID, nothing written) |
| v8 only with its own authorization | `decide()`: an artifact of scope "NP-AVG-1 Stage 0, the count-only site-pair count on v8's index space (l2sitepairs.py), nothing else", naming the checked-out commit and this module's SHA-256, a clean Layer-2 tree, and the host's owner check of a designation by amaybaum containing `NP-AVG-1 Stage 0 v8 site-pair count authorized at <commit> module_sha256 <sha>` | without it, v8 is refused before any count (a sentinel replaces the count and must not run); `refusal_probe.py` also runs the command line and a forged count file against the dry run |
| exact counts | Burnside equality in the module; the dry run checks N, R and nt against its own index space and the file's module digest | toy: every index against `l2analysis.canon`; ball(3) analogue: every site and every site pair at four slice pairs that separate the in-pair cases |

**Mutants, each killed** (quick campaign): the guard not installed; any output accepted; v8 counted
without the authorization (stopped by the sentinel before any count); one site pair's representatives
dropped; the in-pair case t1 < t2 counted as t1 ≤ t2.

**The limit of the runtime guard.** It catches files, imports, processes, network calls and writes
through `sys.stdout` and `sys.stderr`. It does not catch a deliberate low-level write to file
descriptor 1. As for the CI calibration, the guarantee is the reviewed, pinned module; the runtime
guard is a backstop against accidents and casual edits.

## 5. Resource limit (for the authorization)

| limit | value | basis |
| --- | --- | --- |
| CPU time | 60 s (`RLIMIT_CPU`, set by the module before counting) | measured: ≤ 0.01 s on ball(1)–(3) (`design/subdivision/bounds.json`); v8's 8,256 site pairs × 8 group elements is under a second by the same scaling |
| address space | 1 GiB (`RLIMIT_AS`) | measured peak resident memory about 22 MB on every analogue |
| job timeout | 5 min | for a CI job, if the owner chooses CI |
| output | about 40 kB of JSON | 8,385 integers |

**How it would run.** One process: `python3 -I -B code/l2sitepairs.py --profile v8 --out <file>
--authorization <artifact> --owner-check <owner check>`, at the authorized commit, locally or as one CI
job, as the owner chooses. Its compute time is charged to the campaign ledger (owner: the count pass is
included). The output file is retained under §A.42 before any decision uses it, and the dry run reads it
with `--site-pair-counts`.

## 6. What it unlocks, and what it does not

- **Unlocks:** the v8 shard plan (exact representative balance: every shard holds ⌊R/32⌋ or ⌈R/32⌉
  representatives), the per-shard representative weights of the survivor cap's model, and the per-shard
  modelled closure cost (from these counts and the per-site item-set sizes the dry run already uses).
- **Does not unlock:** C7's populations (|F_G|, |I_c|), the cost of C7's sets 2 and 3, or the cost
  balance of the shards. On the mid-size analogue, representative balance left a measured spread of
  more than threefold in shard time (`LAYER2-PLAN.md` §3.6). The population count is a separate,
  unauthorized amendment (`AMENDMENT-PROPOSAL-V8-COUNT.md`).

## 7. Review questions

1. Is the in-pair rule (§2) correct for every group element, and do the four counts identify it?
2. Do the inputs reach anything beyond the index metadata the owner allowed?
3. Do the guards and the validator make every restriction hold, within the stated limit of the runtime
   guard?
4. Is the authorization disjoint from the enumeration's (`l2auth`), in scope string, schema and
   designation line?
5. Is the resource limit adequate, and is the output retained before use?

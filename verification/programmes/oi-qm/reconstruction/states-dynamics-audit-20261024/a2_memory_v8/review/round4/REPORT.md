BLOCK — 19a33d6fff854deadb9cc4cdb4f20b144202d5e6 (independent certificate audit of a2_memory_v8; single parent aee64f2c0a3d55feded2084c34200e44948b5c2a)

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..19a33d6fff854deadb9cc4cdb4f20b144202d5e6: BLOCK.

**What now works.** The audit fixes the previous gap. Every consistent wrong-bound mutant from re-check 2 is now
caught, and so are my new single-site and main-plus-reported mutants aimed at the audit's shared pieces.

**Why it still blocks.** The owner's two additional criteria are not met:
1. **Scope and identification.** The audit takes its scope from code defaults and never checks the reported family
   against the preregistered 48 members. A consistent narrowing of the k range or the B range passes. So does an
   audit restricted to 4 members while the verdict still claims all 48. A dropped member crashes the checker instead
   of printing VOID.
2. **Disclosure attribution.** The claim "did not compute on RS(B,k), on the census populations or on the decision
   rule" is stated as fact in both REPORT and PROVENANCE. The repository cannot establish it, and the claim is not
   attributed to the author's account.

**What stands.** No reported value is wrong. The theorem, the census, the decoder member, the RS rows and the
comparators stand as previously verified.

Read-only review: `python3 -I -B` (3.13.16), run from empty directories, on files exported with
`git show 19a33d6f:<path>` into `tree/`. Files in this directory:
- `rev_mutants4.py` / `rev_mutants4.out`: mutants A1–A7, aimed at the audit.
- `rev_mutants5.py` / `rev_mutants5.out`: scope and label mutants L1–L6. Their outputs are under `work/rmut5/*/run/`.
- `rev_mutants3.out` and `rev_mutants1.out`: the earlier reviewer sets, rerun.
- `count_certs.py`: an independent count of the certificate checks.
- `leafdiff.out`.

## Changed-file inventory

| range | files | notes |
| --- | --- | --- |
| `aee64f2c..19a33d6f` | 7 modified (+226/−23): `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`, `mutants/mutants.out`, `mutants/run_mutants.py`, `result.json` | `PLAN.md` byte-identical (b7f7eaae…a275) |
| `1dfec979..19a33d6f` | 7 files added under `a2_memory_v8/` (1,798 insertions) | |
| `49e1a119..19a33d6f` | 8 files | nothing outside `a2_memory_v8/` |

## 1. Audit independence (code read)

**What the audit does not share.** Its block laws (`audit_block_counts`) use integer intervals [L, H)/5^t in
absolute coordinates. Its BC and TV sums use integer `isqrt`, with R = 2^200. Its depth search (`audit_least`)
uses its own integer powers and hard-coded thresholds 2, 3/4, 10 and 200. It does not call `retained_seed_runs`,
`block_law`, `bc_enclosure`, `root_lo`/`root_hi`, `power_rule_lower`, `least_n_above`, `least_power_below` or
`tv_of`. I checked its formulas: the interval cut (L + 4H)/5^(t+1), Dn = R·S·F, and the n_half, n_hp, n_lp and
n_tenth definitions match the stated rules.

**What it does share.**
- Main-path code and constants: `tv_iid` (for the k=1 certificates), `digest`, `HALF` and `TENTH`, `check`, `Q`,
  `itertools.product` and `math.isqrt`.
- Inputs: the reported family entries, and the reported enclosure `encl`, which is used only in the overlap check.

A single edit to any of the shared code is caught by an external anchor (`rev_mutants4.out`):

| mutant | edit | caught by |
| --- | --- | --- |
| A1 | `HALF` → 1/4 | exact crossing bracket |
| A2 | `digest` returns a constant | K1 pinned v7 digests |
| A3 | shared `isqrt` biased | root squaring checks |
| A6 | `tv_iid` scaled by 0.9 | K6 (`tv_iid` = `tv_product`, and the pinned T(4096)) |

`tv_iid` produces the reported memoryless crossings but no reported depth. The depths come from the BC enclosure,
so one edit cannot corrupt a depth and its k=1 certificate together.

REPORT's "shares no helper with the main computation" is therefore inaccurate as written. The code comment's list
of helpers it does not share is accurate; use that wording.

**Consistent wrong-result mutants.**

| mutant | change | result |
| --- | --- | --- |
| W1a, W1b, W2, W3, W4, W5 (re-check 2) | wrong enclosure, constant or bound, fed consistently through the main path | all exit 2 VOID: W1a/W1b on the enclosure overlap, W3/W4 on the depth recomputation, W2/W5 on the product bracket |
| A4 | reported depths and the audit's expected n_hp both one block early | caught: certificate T>1/2 contradicted by exact TV (RS(2,5)) |
| A7 | reported enclosure widened upward, depths built from it | caught: audit recomputed depth |
| A5 | main bound **and** the audit's restated definition both made 5% too strong | **exit 0, not caught** |

A5 is the inherent limit of a second implementation: if the control itself is edited to agree, only an exact
certificate inside the affected range can catch the error. Here n//20 = 0 for every n ≤ 16, and the shifted k=1
depths remain true. This needs disclosure, not code. State it in REPORT: the audit's definitions and the main
rules are two codings of the same stated formulas, and agreement between them is checked against REPORT's stated
definitions only by review.

**Earlier reviewer sets on this revision.**
- First-round set, with R1 adapted: 16/16 exit 2.
- W-set: 6/6 exit 2.

## 2. The 212 certificate checks

My independent count from the reported depths (`count_certs.py`) gives 212, matching the audit.
- The T>1/2 certificate is checked against exact TV for only 7 of the 48 members: B=2 k=1..5, B=3 k=1 and B=4
  k=1.
- For the other 41 members, every T>1/2 depth exceeds the enumerable range, so their headline T>1/2 depths rest on
  the independent BC enclosure and the depth recomputation, not on exact TV. That is legitimate, but REPORT's "It
  checks every certificate against exact TV where exact TV is enumerable … 48 members and 212 certificate checks"
  should say how few T>1/2 certificates are actually reached.
- The T ≤ 1/2 and T ≤ 1/10 certificates are reached for most members at n=1.

## 3. Owner addition 1: scope and identification (`rev_mutants5.out`)

| mutant | change | result |
| --- | --- | --- |
| L1 | k range 1..15, changed in both `family()` and `independent_audit()` | **exit 0, not caught.** The verdict label stays `…EVERY_TESTED_MEMBER`; only the text "k=1..15" and the audit counts (45 members, 207 checks) reveal it |
| L2 | k range 1..15 in the main family only | exit 1, `KeyError` crash; not a clean VOID |
| L3 | members B3_k5 and B3_k6 swapped (relabelled) | caught: audit block TV equals reported |
| L3b | member B4_k16 deleted from the reported family | exit 1, `KeyError` crash; not a clean VOID |
| L4 | `TENTH` → 1/5 in the main computation | caught: audit recomputed tenth depth |
| L5 | B range (2, 3), changed in both | **exit 0, not caught** (32 members, 108 checks) |
| L6 | audit restricted to B=2, k≤4; main family unchanged | **exit 0, not caught.** The audit validates 4 members while the verdict claims all 48 |

Relabelling, swapping and threshold changes are caught. Omission, consistent rescoping and a narrowed audit are
not. Nothing requires the audited member set to equal the reported set, or either set to equal the preregistered
B∈{2,3,4} × k∈1..16.

Fix:
- Derive the preregistered scope independently of the code defaults: a frozen literal, preferably parsed from
  `PLAN.md` ("B in {2,3,4}, k = 1..16") with PLAN.md's pinned SHA-256 checked.
- Require set(reported member keys) = set(audited member keys) = that scope, with exactly 48 members.
- Make the audit iterate over the reported keys and VOID on any missing or extra key, instead of crashing with a
  `KeyError`.
- Add L1, L2, L3b, L5 and L6 to the mutant runner.

## 4. Owner addition 2: disclosure attribution

REPORT (Preregistration record) states as fact:
- what ran ("one floating-point exploration … B=1..4, m=0..8");
- what it showed;
- "It did not compute on RS(B,k), on the census populations or on the decision rule".

PROVENANCE `plan_commit_note` says the same.

No artifact of the exploration is in the package or its records, and none is cited. The repository establishes
only two things:
- that `PLAN.md` was committed alone at 1dfec979 before any package file;
- that the execution code postdates it.

So the narrower historical claim cannot be independently established. It is the author's account, and it is not
attributed as such.

Fix: in both REPORT and PROVENANCE, prefix the description, the qualitative findings and the "did not compute on"
sentence with "By the author's account (no artifact of the exploration is retained; the repository cannot
corroborate it)". Keep the possible-influence list as it is. The rest of the disclosure is adequate:
- the influence list;
- "cannot be measured after the fact";
- "the order … cannot be established";
- the removed working-record sentence.

## 5. Narrowed wording

- The power-rule cross-checks row now says that (i)–(iv) share the enclosure, that (i) and (ii) are one-sided with
  slack, and that the mutant results hold only for the listed mutants. That is correct.
- The k=1 range's dependence on n_half is stated.
- Remaining fixes:
  - "shares no helper" (section 1);
  - the coverage of the T>1/2 certificate (section 2);
  - the A5 limit (section 1).

## 6. Leaf diff, replay and hygiene

- **Leaf diff aee64f2c→19a33d6f:** 2 leaves added (the audit counts: 48 members, 212 checks), 1 changed
  (`schema` v3→v4), 0 removed. No value changed.
- **Replay:** normal and `-O` runs are byte-identical to `result.json` (about 4 min each on a shared machine).
- **Author mutant runner:** see the addendum. The first attempt was killed by my background-task time limit.
- **`SHA256SUMS`:** verifies all 7 files. `PROVENANCE.json` parses.
- **Hygiene:** no absolute paths, emails, IPs, tokens or `__pycache__`.
- **Repo tools:** `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all
  pass. The worktree is clean at 19a33d6f.

## 7. Side effect on the clone (disclosure)

While checking provenance I ran `git log --all -S "floor-truncated"` on the clone. The clone is a blobless partial
clone (`remote.origin.promisor=true`, `partialclonefilter=blob:none`), so the command fetched historical blobs on
demand. That started repeated background auto-gc. I stopped it after about two minutes.

**Unchanged:** the worktree, HEAD (19a33d6f) and the refs. There are no alternates, so no other clone borrows from
this object store.

**Changed:** `.git/objects` gained promisor packs. Two leftovers remain:
- `.git/objects/pack/tmp_pack_T0wCZq`, about 146 MB, reported as garbage by `git count-objects`;
- a stale `.git/gc.log.lock`.

No git process is still running. I did not delete either leftover, since the review is read-only. Whoever owns the
clone can remove both once they confirm no git process is running, or run `git gc`.

## Addendum: author mutant runner

On the second attempt, with a longer timeout, `mutants/run_mutants.py` (TMPDIR inside the review directory) exits 0.
Its output is byte-identical to `mutants/mutants.out`: unmodified run plus M1–M25, all caught, 27 lines. The first
attempt was killed by my tool's 30-minute background limit while the machine was shared; it was not a checker
failure.

## Follow-up: a97c852a

Re-checked at a97c852a3a5305a8b4a69eac7173ea526f08624b: ACCEPT WITH NITS. Both blockers above are resolved: the
preregistered scope is parsed from the hash-pinned PLAN.md, and the exploration account is attributed to the
author. Details are in `../recheck4/REVIEW.md`.

BLOCK — aee64f2c0a3d55feded2084c34200e44948b5c2a (re-check revision of a2_memory_v8; single parent fb05dea83b2b61ed9ff6be189f35077426aa2037). The block concerns only the owner's control-independence criterion; no reported result is wrong.

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..aee64f2c0a3d55feded2084c34200e44948b5c2a: BLOCK.

**What stands.** I re-verified each of the following independently:
- the theorem and its proof;
- the census and the FD member;
- the 48 RS rows and the comparator lists;
- the other-neighbour crossings and the monotone-likelihood-ratio argument;
- replay, hashes and hygiene.

No reported value is wrong.

**Why it blocks.** The owner's criterion was that a deliberately wrong depth bound, changed consistently in the
implementation and in the reported result, must make the checker fail. It is not met:
- Four of my six consistent wrong-bound mutants pass every control.
- One of them reports a certificate that exact computation shows to be false, at a depth the checker already
  enumerates exactly.
- REPORT states the opposite ("a consistent change to it is judged by the exact computations"; "Too strong a bound
  fails (i) or (ii); too weak a bound fails (iii)"). That generalises from the finite mutant set to all errors.

The fixes below are cheap.

The review was read-only, with every script run as `python3 -I -B` (3.13.16) from empty directories on files
exported with `git show aee64f2c:<path>` into `tree/`. Files in this directory:
- `rev_mutants3.py` / `rev_mutants3.out`: new consistent wrong-bound mutants W1a, W1b, W2, W3, W4 and W5.
- `rev_mutants1_adapted.py` / `rev_mutants1.out`: the first-round 16 mutants, with R1 retargeted to the shared
  function.
- `leafdiff.py` / `leafdiff.out`.
- `rs25_exact.py`: exact RS(2,k) total variation, using my own block-law code.

## Changed-file inventory

| range | files | notes |
| --- | --- | --- |
| `fb05dea8..aee64f2c` | 7 modified (+196/−53): `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`, `mutants/mutants.out`, `mutants/run_mutants.py`, `result.json` | `PLAN.md` byte-identical (b7f7eaae…a275) |
| `1dfec979..aee64f2c` | 7 added under `a2_memory_v8/` (1,595 insertions) | `PLAN.md` from 1dfec979 |
| `49e1a119..aee64f2c` | 8 files | nothing outside `a2_memory_v8/` |

## Consistent wrong-bound mutants (owner's test)

Each mutant changes the bound or the depth together with every check that restates it.

| mutant | change | effect | result |
| --- | --- | --- | --- |
| W1a | BC enclosure scaled by 0.9999 in `bc_enclosure`, so the wrong enclosure feeds every depth rule and every check | B=4 k=1: preregistered depth 7997→4444, power 5543→3080, upper 1150→639; B=4 k=2: 9196→6300 and 6374→4366; `family_verdict` changes | **exit 0, not caught** |
| W1b | the same, scaled by 1 − 10⁻⁶ | about 1% depth shifts | **exit 0, not caught** |
| W2 | preregistered constant changed (nc > 1/2) together with the bound 1−BC^(2n) | | caught (exact product TV) |
| W3 | shared `power_rule_lower` made 5% too strong: 1−BC^(n+⌊n/20⌋) | | **exit 0, not caught** |
| W4 | depth search and its minimality check changed together, so every depth comes one block early | B=2 k=5: 15→10; B=2 k=16: 48→32; B=3 k=9: 72→63; B=4 k=14: 742→728 | **exit 0, not caught** |
| W5 | preregistered constant ×1.5 together with the bound ×1.5 | | caught (exact product TV) |

**W4 reports a false certificate.** It certifies that RS(2,5) has T > 1/2 for every h ≥ 10. The exact T(10) is
0.463739 (`rs25_exact.py`); the exact first crossing is h = 11. At W4's depths, RS(2,4) has T(8) = 0.4386 and
RS(2,2) has T(6) = 0.4880. The checker already enumerates T(10) for RS(2,5), since n·k = 10 ≤ 16. It only tests
that value against the bound function, never against the reported certificate.

**W1 cannot be caught as the checker stands.** Every constraint (i)–(iv) consumes the same `bh` and `c_low` from
`bc_enclosure`. Its per-term square roots are verified by squaring, but the summation is not checked by anything
independent.

## Code-path review of constraints (i)–(iv)

- `tv_iid` (the binomial engine) and `block_law` / `product_law` / `tv_of` do not call `power_rule_lower`. That
  function is called only by the depth search, its minimality check, the k=1 exact check and the product check.
  The separation claimed for the code paths holds.
- The shared inputs are `bh` and `bl` from `bc_enclosure`, and `n_half` from the same `c_low = 1 − bh`. A single
  edit there moves the bound, the preregistered depth (iii), the range top 2·`n_half` and (iv) together. Hence W1.
- (i) and (ii) are one-sided and have slack. They catch only errors large enough to exceed the exact TV at the
  checked depths; M15, M20, W2 and W5 are of that kind.
- (iii) catches only bounds weaker than nc/(1+nc) (M18).
- (iv) catches only gross early shifts (M19).
- No constraint compares a reported certificate with exact TV, except the k=1 crossing bracket.
- The k=1 range is every h ≤ 600, plus multiples of 1024 to 2·`n_half`, plus `n_hp`±1. It no longer depends on
  `n_hp`, apart from those three added points. At B=4 it is 618 depths up to h = 15,360. REPORT's "do not depend on
  the power-rule depth" should mention the ±1 points and the dependence on the shared `bh` through `n_half`.

## Fixes required to meet the owner's criterion

1. **Certificate-level exact checks.** For every member and every n with n·k ≤ 16 (extendable to about 20 at B=2),
   require exact T(nk) > 1/2 whenever n ≥ `n_hp` or n ≥ `n_half`. Require T(nk) ≤ 1/2 whenever n ≤ `n_lp`, and
   T ≤ 1/10 whenever n ≤ `n_tenth`. This catches W4 at RS(2,5) n=2, using a value the checker already computes.
2. **An independently executed recomputation for the rows no exact TV reaches.**
   - Compute BC by a separately written summation, for example `decimal` at 60 digits, or integer `isqrt` over a
     common denominator. Require bl ≤ BC_ind ≤ bh to within a tolerance below the enclosure width. This catches W1a
     and W1b.
   - Recompute every depth from its stated definition in separate code, for example a log estimate with exact
     boundary verification using its own power evaluation and not `power_rule_lower`. This catches W3 and W4 in
     every row.
3. Add W1a, W1b, W3 and W4 (or equivalents) to `run_mutants.py`.
4. Narrow the REPORT wording ("a consistent change … is judged by the exact computations"; "Too strong a bound fails
   (i) or (ii); too weak a bound fails (iii)") to what is shown, or restate it once fixes 1 and 2 make it true.

## Other items requested

- **Other-neighbour crossings.** The exact first crossings are 4 (agreement 1, B=2), 45 (7/8, B=3) and 127 (12/16,
  B=4). They equal my round-1 values from separate code.
- **MLR argument: valid.** For i.i.d. laws, the count is sufficient for both, so the record TV equals the TV of the
  counts. Take p' > p > 4/5. The likelihood ratio is increasing in the count, so the optimal set A_p is an upper
  set. Then TV(p') ≥ P_p'(A_p) − Q(A_p) ≥ P_p(A_p) − Q(A_p) = TV(p), by stochastic monotonicity. The other side is
  symmetric. So T(h) is pointwise ordered on each side, the latest first crossing is at a neighbour, and comparing
  the two neighbours' exact crossings settles it.
- **Narrowed comparator wording: correct.** It reads "nearest-dyadic i.i.d. reset; best i.i.d. law at the tested
  B; not compared with v7's record-dependent or time-varying controllers". Ordering is claimed only for certified
  members, and the undetermined ones are named.
- **Disclosure: mostly adequate.** It now lists possible influence on K5, the run-mass route, the census
  populations, the small-n mismatch expectation and the exact-stationary-law method. It says the influence cannot be
  measured and that the order cannot be established, and it drops the working-record sentence. Two defects remain:
  - The next bullet says the exploration "touched neither RS(B,k), the census populations nor the decision rule".
    Placed under "may equally have informed the census populations", that reads as a contradiction. Say "did not
    compute on" if that is what is meant.
  - `PROVENANCE.json`'s `plan_commit_note` was not updated; only `post_recheck` mentions the extended list. Mirror
    the extended influence list there.
- **Leaf diff fb05dea8→aee64f2c** (`leafdiff.out`):
  - 6 added: the other-neighbour agreement and crossing for B = 2, 3, 4.
  - 11 changed: `class_verdict` (post-review label), `family_verdict`, `schema`, and 8 k=1 range metadata leaves.
  - 0 removed.
  - No certified depth, census value or RS value changed. This matches the author.
- **Mutants.** The author's runner reproduces `mutants/mutants.out` byte for byte, with M1–M20 all caught. My
  first-round set, with R1 adapted, gives 16/16 caught. W2 and W5 are caught; W1a, W1b, W3 and W4 are not.
- **Replay.** The normal and `-O` runs are byte-identical to `result.json`, at 2 min 53 s each.
- **Hashes.** `SHA256SUMS` verifies all 7 files, and `PROVENANCE.json` parses.
- **Hygiene.** No absolute paths, emails, IPs, tokens or `__pycache__`.
- **Repo checks.** `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all
  pass. The clone is clean at aee64f2c.

ACCEPT WITH CHANGES — `S3-PLAN-r7.md` at `f3cf799466ac20d6a202e30b135c5b212858c49d` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused confirmation of the S3 plan, r7

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r7.md` and `RESPONSE-S3-PLAN-r6.md`. The copies supplied to me are identical to the
  committed files.
- `S3-PLAN-r6.md` is unchanged, and `REVIEW-S3-PLAN-r6.md` is preserved as delivered.
- The full diff from r6 to r7.
- At source on `main`:
  - S-L2, S-L3 and §C in `amendments/MR-star.md` (ll. 511–530, 1295–1300);
  - `amendments/stage1-log.json`:770–776;
  - `observer-interface-obsmu-20261104/ANALYSIS.md`:485–489.

**Line numbers** are r7's.

## 1. R7–R9 and the gating sentence

- **R7: resolved.**
  - "SNR-1" replaces the old label at every use of the rule: ll. 22–26, 40, 43, 338, 600, 624, 636,
    715, 729, 743, 753, 794, 837.
  - "NC-1" survives only at l. 161, which is O-SET's definition, as intended.
  - `git grep SNR-1` over `origin/main` returns nothing. I did not re-check the 542 remote refs.
- **R8: resolved in structure.**
  - SNR-1 has *disproved* as a counting category, "at that result's scope only, and at the result's
    recorded status".
  - The disproved-erasure case is added (ll. 612–630).
  - Its status and scope need two corrections (R10, below).
- **R9: resolved (ll. 342–350, 721–723).** Routes 2 and 3 require a sourced renewal limit or cost
  comparison. The references are target laws under `Θ`, as in AC-1.
- **Gating: partly resolved (ll. 757–762).**
  - The sentence names MR-1 stage 2, for (e′), and #866's σ12 screen, for (c′).
  - Negative closure also needs (b′), the observer-level lift (ll. 737–741). §8.6 places that outside
    U4, as track (a)'s OB-a1.
  - Add (b′), for example "a result on the observer-level lift (OB-a1, #866/#1169)", so the gating
    sentence is complete (R11).

## 2. S-L3's status and scope, at source

**What r7 says (ll. 617–622):** "a paper proof that the independent review of `fc68d333` verified
('It verified S-L1, S-L3, …', `MR-star.md`:1294–1299)".

**"A paper proof verified by review" is accurate only as a report, and it falls short of
verification on `main` (R10(a)).**
- The verdict is MR★'s own account of the review: "The independent review of `fc68d333` returned
  REVISE … It verified S-L1, S-L3, S-L4 …" (MR-star.md:1297–1300).
- `stage1-log.json`:773 records that review as "relayed by the coordinator".
- No review artifact for `fc68d333` is on `main`. The review lived on PR #1023, which was retired
  without merging.
- A record on `main` has already ruled on exactly this report, for S-L4. O-OBSMU's `ANALYSIS.md`:485–489
  says: "MR★:1297–1300 records that the review of `fc68d333` 'verified S-L1, S-L3, S-L4 …' … Under
  §A.46 item 7, though, that report does not count as verification here, so S-L4 is used only as a
  named premise."
- The same holds for S-L3.
- **Fix:** write "a paper proof. MR★ records that the review of `fc68d333` verified it. That report
  is not verification on `main` (§A.46 item 7; cf. O-OBSMU `ANALYSIS.md`:485–489), so S-L3 enters as a
  named premise."
- r7's "not an established premise … not upgraded here" (l. 622) is consistent with this. The word
  "verified" needs the qualification.

**The scope is understated (R10(b)).** S-L3 holds under more than "`K★ = {K1}`, the linear rule":
- MR-1's *frozen availability standard*. S-L2, which S-L3 uses, takes the available
  transformations to be "the time shifts `φ^n`, `n` within the budget"; "observer-side choices
  change only which region and tick are read".
- The budget below recurrence. The global wait `φ^{N−1}` lies beyond it.
- `a` injective with a nonempty neighbour relation, which the proof that `σ` is not a time shift
  uses.
- S-C1(a) for "No region executes `σ` on another".

SNR-1 counts a disproof "under the §3 criterion" (l. 716). The §3 criterion is the one U1 has yet to
fix, with a new frozen access declaration. So S-L3's disproof under MR-1's standard is not yet a
disproof under §3. U4 must re-check it under U1's criterion before it counts.

**Consistency with SNR-1 and §A.46 item 7.**
- Counting S-L3 toward (a′) "at the result's recorded status" (l. 722) is consistent with both, *if*
  the outcome is stated as conditional on S-L3 as a named premise, within the scope above.
- A negative closure that rests on it is then a conditional result, not an established one.
- **Fix:** add to the disproved-erasure case: "Counting it toward (a′) is conditional on S-L3 as a
  named premise and on its re-check under the U1 criterion. The closure it supports carries that
  condition."

## 3. The conjugate-basis carve-out

**Correct.**
- S-L3 disproves subsystem *uncomputation*, that is, reversing the marking coupling.
- Fringes recovered *conditionally*, by reading the marker in a conjugate basis and sorting (MR-1 T4),
  are a readout question, not an inverse.
- On K1 the symplectic structure does supply conjugate readouts: S-L7's slice pairs.

Recommended (nonblocking): say that conditional-fringe recovery is also reproduced by the classical
eraser (CC5; M-2). It therefore falls under (e′) and K-6/M-4 (whole joint laws, full branch masses),
not under S-L3.

## 4. Other changes, and anything new

- **Scope of the diff.** Only the sites listed changed: the header, H-RR routes 2–3, the renamed
  label, the disproved-erasure case, SNR-1's paragraph, (a′), the gating sentence, the U4 row and
  question 6.
- **Minor.** The r6 revision note now names the rule "SNR-1" (ll. 40, 43). r6 itself called it
  "NC-1". The note should say "named NC-1 in r6, renamed SNR-1 in r7", or be left in its r6 wording,
  so the history stays accurate.
- **No new premise and no authorization.**
- **The candidate raw-direct miss on eraser behaviour** (ll. 625–628) is correctly marked [P] and
  conditional on (α)–(δ) and (γ).

## 5. Verdict

**ACCEPT WITH CHANGES.**
- **R10:**
  - (a) qualify "verified by review": it is MR★'s report, not verification on `main` (§A.46 item 7),
    so S-L3 enters as a named premise;
  - (b) state S-L3's full scope and its re-check under the U1 criterion, and make the (a′) contribution
    conditional on both.
- **R11:** add (b′) to the gating sentence.
- **Optional:** the CC5 note on conditional fringes, and the r6-note wording.
- All of these are local wording changes. A diff check suffices.

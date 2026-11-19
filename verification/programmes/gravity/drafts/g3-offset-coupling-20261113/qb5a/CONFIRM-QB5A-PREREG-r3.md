# CONFIRM-QB5A-PREREG-r3: edit check of G3 QB5(a) r3 against REVIEW-QB5A-PREREG-r2

**Verdict: ACCEPT WITH CHANGES.** R2-1 to R2-15 are applied verbatim at the cited lines. The bookkeeping
edits are acceptable, TX-5 and TX-13 are green as reworded, and no other control is affected.

The edit check found two required changes, each a sentence or two, with replacement text below:

- **CF3-1.** Non-decisive rows can still enter decisive steps. This affects the Group P rows, which my R2-10
  text introduced, and also, since r1, the rows whose own passage is excluded (A3x = yes). I missed the
  second case in both earlier reviews.
- **CF3-2.** I-SYM's statement that "no U cell reads A3" is no longer literally true. My R2-5 role
  aggregation reads whether a role is committed.

There is also one nit. Once the two changes are applied, checking the two edits is enough. After that, r3 is
ready for freeze, subject only to the owner's recorded answers to OQ-1 to OQ-5 and OQ-7 and the owner's
designation of F.

**Target.** Branch `research/g3-offset-873-20261113` at `4a157f19eeab7b9d6d4ef8896bf9209a0c84b832`, parent
`c006bf2a3`, fetched by branch name.

- The commit adds three files:
  - `qb5a/G3-QB5A-PREREG-r3.md` (1273 lines, "r3:n");
  - `qb5a/NOTES-QB5A-r3.md` (71 lines);
  - `qb5a/RESPONSE-QB5A-r2.md` (260 lines, "RESP:n").
- `c006bf2a3` adds `qb5a/REVIEW-QB5A-PREREG-r2.md`, byte-identical to the review I issued (`cmp`).
- `diff` of r2 (at `c2b754af`) against r3 gives 42 hunks, as RESP §4 states.

**Method.**

- I compared r2 and r3 hunk by hunk, against my replacement texts.
- I re-ran the affected controls by hand.
- I checked by location only whether the reworded TX-5 resembles corpus wording.
- I classify no inventory passage, state no expected outcome, ran no computation on OI rules and wrote nothing
  to the repository.

***

## 1. R2-1 to R2-15: applied verbatim

Every one of the 42 hunks maps to a finding or to a bookkeeping edit RESP §3 lists. No hunk falls outside
them.

| Finding | r3 | Check |
|---|---|---|
| R2-1 | r3:1085–1086 | verbatim |
| R2-2 | X-18 at r3:1156; I-BLIND item 6 at r3:142–143 | verbatim. The inclusion list also covers the second reader's work at Q-1b, which happens before the Stage-2 commit |
| R2-3 | Q-1b at r3:1053 and r3:1066–1079; Q-4 at r3:1057; X-19 at r3:1157; X-6 at r3:1144; W-e at r3:999 | verbatim. The old Q-6a row is removed |
| R2-4 | TX-13 at r3:1043; example at r3:439–440 | verbatim |
| R2-5 | r3:415–417, r3:426–431; A3n in X-18 and X-5 | verbatim. See CF3-2 for one consequence |
| R2-6 | TX-5 at r3:1035 and r3:580–581; question-form bullet at r3:418–420 | verbatim |
| R2-7 | r3:518, :536–539, :554–555, :560, :648, :665–669, :1256–1259 | verbatim |
| R2-8 | r3:628–631 | verbatim |
| R2-9 | rule at r3:319–321; table at r3:325–333 | verbatim. The re-cut table follows the rule |
| R2-10 | C-GR416 at r3:307; Group P at r3:335–338; X-4 at r3:1142 | verbatim. See CF3-1 |
| R2-11 | r3:1213–1220, :1227–1235, :1239–1240 | verbatim |
| R2-12 | r3:820 | verbatim |
| R2-13 | r3:544–546 | verbatim |
| R2-14 | X-7 at r3:1145; inventory notes at r3:296 and r3:325–333 | verbatim |
| R2-15 | r3:564–565 | verbatim |

**Bookkeeping edits. All are acceptable.**

- **"Q-6a" changed to "Q-1b" at §7.2 (r3:713) and §14.2 (r3:1182).** Necessary: both name the removed node.
  No "Q-6a" remains in r3. The surviving labels Q-6b and Q-6c have no Q-6a beside them. That is cosmetic, and
  I recommend leaving it, so that the line references of the reviews stay valid.
- **I-BLIND item 1's deadline** ("before any row is classified", r3:131–132). Necessary: it now states the
  same deadline as X-19 and Q-1b.
- **OQ-4's applied answer** (r3:1242–1244). It now lists C-GR416 and Group P, which keeps §15 consistent
  with §4.2.
- **Title, history and "r3 carries"** (r3:1, r3:27–33), and the blank line after the Q-1b heading. These are
  pure bookkeeping.

***

## 2. Controls

- **TX-5** ("The coupling of the axion background to spacetime curvature remains an open problem in this
  model."). **Green.**
  - "open" is in the Op list (r3:545).
  - Its scope, the background's coupling to curvature, is the quantity's source role in §5.3's sense
    (entering the field equation). So A3 is Op.
  - The sentence contains no T trigger ("sources", "gravitates" and the rest), and by r3:418–420 a passage
    that states only that whether the quantity sources is open gives no role value. So A1 is not fixed by
    this sentence.
  - **Resemblance, checked by location.** TX-5 shares the words "coupling" and "open" with GR:352, GR:466
    and GR:577, which call the G3 coupling "open". It is no longer a near-paraphrase of any one of them, as
    r2's TX-5 was of T-GR577's clause. The required values follow from the explicit rule text (the Op
    list; r3:418–420), not from the sentence's resemblance. No control of the Op value on a source role
    can avoid that vocabulary altogether. **Acceptable.**
- **TX-13** ("The mass of the Schwarzschild solution, obtained by evaluating the field equation on that
  solution and integrating over a sphere at infinity (the Komar mass)."). **Green.**
  - A1q is yes: the sentence states the value as obtained by evaluating a law of the gravitational
    dynamics, the field equation, on a given solution (r3:380–381 test).
  - There is no role T. The mass is neither a term of a field equation nor said to source.
- **The other controls are unaffected.** RC-P, RC-N, X1–X12, W-a, W-c, W-e, TC-U, TC-K and TX-1 to TX-12
  give the same results as in REVIEW-QB5A-PREREG-r2 §2:
  - Each toy has one row per quantity, so R2-5's role aggregation leaves each toy row's role as stated.
  - No toy uses As|cond, Group K or Group P.
  - Every toy is in β0, so R2-8 does not apply.
  - TX-4 matches "take … to" and "gravitate" (by stem, r3:546).
  - TX-12 requires only A1 = NS, which A3n does not change.
  - W-e's rows m1 and m2 are single-row quantities, so committed status does not change their roles. W-e
    stays green (CF3-2).

***

## 3. GR:346

K-GR346 keeps sentences 1–3 as one row and records sentence 4 as "on §2.2's list and is not a row"
(r3:329; NOTES-QB5A-r3 D-26). R2-9 named K-GR340, K-GR342 and K-Sub385 to K-Sub389, so the writer did not
go beyond it, and GR:346 was already cut at the sentence holding the excluded clause.

The other split passages keep the excluded part as a row with A3x = yes; for example, K-GR340·s2. Read
literally, R2-9's rule would make sentence 4 such a row too. Once CF3-1 is applied, though, an A3x = yes row
enters no aggregation and no decisive step. Whether sentence 4 is a row or a recorded exclusion then makes
no difference to any verdict.

**Acceptable as it stands, given CF3-1.** For uniformity the writer may add "K-GR346·s4 (on §2.2's list)"
as a row, but this is not required.

***

## 4. Findings

### Required

#### CF3-1. Non-decisive rows must enter no decisive step

**Where.** Group P at r3:335–338; X-4 at r3:1142; GRT-4 at r3:687–694 ("some corpus row x (§4.2, Group K
included)"); Q-1b at r3:1068 ("every sentence of a §4.2 row"); role aggregation at r3:425–431; status
aggregation at r3:554–565; A3x at r3:567–571.

**Evidence.**

- **Group P.** Group P sits inside §4.2, and "do not enter the decisive table" is stated, but nothing else
  keeps Group P out of the decisive machinery:
  - X-4 says the decisive table's row IDs equal "§4.2 ∪ §4.4", which includes Group P, and in the next
    sentence that Group P appears only in sensitivity lines.
  - GRT-4 reads every §4.2 row, so Group P could fail or undetermine a carve.
  - Q-1b enumerates every §4.2 sentence, so Group P could supply a Δ9.k.
  - Same-quantity aggregation does not exclude Group P, so a Group P status could create Conflict.
  - Any of these lets a non-decisive surface decide a verdict. The defect is in my R2-10 text.
- **A3x = yes rows** (since r1).
  - The rejecting predicates require A3x = no, and GRT-4 skips excluded rows. The role and status
    aggregations of §5.1 and §5.3 do not.
  - An excluded passage could therefore change a decisive row's aggregate:
    - through Conflict, or through Conflict-R, which makes `Dom` membership Und;
    - or by making a role committed.
  - Either way, an item on §2.2's list would act as the premise of a decisive step, which K4 forbids
    (r3:174–175).
  - Q-1b may keep enumerating excluded clauses: a reason drawn from one fails GRT-2, which is K4 applied as
    designed. That is how r5's emergent-against-classical candidate failed.

**Replacement.**

1. In the Group P paragraph (r3:335–338), replace "They do not enter the decisive table." with:

   > They do not enter the decisive table and enter no decisive step: they are not enumerated at Q-1b, not
   > read by GRT-4, and not aggregated with decisive rows (§5.1, §5.3). Each such use appears only in the
   > sensitivity line.

2. In X-4 (r3:1142), replace "The decisive table's row IDs equal §4.2 ∪ §4.4." with:

   > The decisive table's row IDs equal §4.2 less Group P, together with §4.4.

3. Add to §5.3's A3x bullets (after r3:571):

   > - A row with A3x = yes is recorded and read as vocabulary only (K4). It enters no role or status
   >   aggregation (§5.1, §5.3) and no rejecting predicate. Its sentences are still enumerated at Q-1b,
   >   where a reason resting on them fails GRT-2.

#### CF3-2. I-SYM's "no U cell reads A3" must allow for role aggregation

**Where.** r3:126–127; r3:617–618; W-e at r3:991–999.

**Evidence.**

- By R2-5, a quantity's role depends on whether a role is committed, and committed-ness is read from A3 and
  A3n (r3:426–431). Role sets `Dom(v)` membership, and U reads that membership. So U reads A3 indirectly.
- I-SYM ("No carve predicate and no U cell reads A3") and §6's opening ("No U cell and no class predicate
  reads A3") are therefore not literally true.
- The dependence is principled:
  - it lets a hedged statement give way to a committed one;
  - a W0 quantity is never committed (Cx), so it takes the same default order as an uncommitted corpus
    quantity.
- W-e still tests what it should, because its two rows are single-row quantities, but its scope should be
  stated.

**Replacement.**

1. At r3:126–127, replace the bullet with:

   > - No carve predicate and no U cell reads A3 (stated status), except through §5.1's role aggregation,
   >   which reads only whether a role is committed. Only the rejecting predicates of §6.3 read A3
   >   otherwise. W-e (§10.4) tests this for single-row quantities.

2. At r3:617–618, replace "No U cell and no class predicate reads A3." with:

   > No U cell and no class predicate reads A3, except through §5.1's role aggregation.

### Nit

- **CF3-3.** No action needed. Q-6b and Q-6c no longer have a Q-6a beside them. Leaving the labels keeps the
  reviews' references valid (§1).

***

## 5. Readiness

Once CF3-1 and CF3-2 are applied and that edit is checked against the text above, r3 is **ready for
freeze**. It then depends only on:

- the owner's recorded answers to OQ-1 to OQ-5 and OQ-7. With the recommended answers applied:
  - OQ-2's qualification is met by Q-1b and the deviation route (r3:1066–1079, r3:1182);
  - OQ-7's qualification is met by As, As|cond, the distinct hedge values and the kept per-row statuses
    (r3:516–565, r3:648);
- the owner's designation of F on #873 (OQ-5).

Any answer that departs from §15's alternative texts needs a check of that edit. As NOTES-QB5A-r3 §2
notes, both qualifications reached the writer only as relayed in my r2 review, so they should be recorded on
#873 with the answers.

No inventory passage is classified here, and no expected outcome is stated. No manuscript change is
proposed, and no premise is adopted.

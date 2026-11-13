# CONFIRM-OQ10: independent review of NOTE-OQ10.md

**Verdict: ACCEPT WITH CHANGES.** Every quote checked is accurate, and the facts about #1265 hold, with
three wording slips (F7–F9). Four changes are needed before the note goes to the owner.
- **F1:** the closing sentence weighs against R-b using a #1097 mark, and leaves out the later owner
  acts that bear on that mark.
- **F2:** the readings leave out one variant of R-b, under which the merge decision is itself the
  exception. That variant changes the consequences.
- **F3:** item 4's remediation requirement is presented as specific to R-a, which contradicts owner
  question 2.
- **F4:** the note understates the item 6 consequence under R-b.

The other findings are Low or Info. The note recommends no reading. It implies no waiver or rule
change, and it stays within OQ-10.

**Object.** `verification/audits/integration/integration-assess-20261113/NOTE-OQ10.md` on branch
`research/integration-assess-20261113`. The branch was fetched by name, without `--depth`. The head
is `d82dd02dabf7cab2cd2a3c093a800bd2c2ce7143`, and it is the single child of `c7ce4f28`. That commit
adds this one file (147 lines). Line numbers below refer to that blob. `main` =
`c3b5f37a354bb26437e2e0165c576a347a63c153`, and `origin/main` was still at that commit when fetched.

**What I checked** (read-only: `git show`, `git log`, and REST reads from `api.github.com`):
- **§A.46 items 1, 2 and 4** (note lines 14–30) against `git show c3b5f37a:AGENTS.md`. Compared
  after normalizing whitespace, they are **verbatim**.
- **The adoption-line quote** (lines 32–34): verbatim.
- **Item 6** is not quoted. Its paraphrase at line 126 matches "Removal of research evidence from
  `main` is never automatic" (AGENTS.md at `c3b5f37a`, §A.46 item 6), but see F4.
- **The history of item 2** (lines 34–39):
  - `0ad4bd0f` reads "Research evidence may be kept on `main` whether or not its programme is
    complete".
  - The conditions first appear in `be616ffc`.
  - `e10a9ba2` rewrites the "Work that meets none …" sentence and is the second parent of the #1097
    merge `ce36c262`.
  - The #1097 body quote ("**For the owner to confirm:** this sentence comes from the coordinator's
    proposal …") is verbatim.
- **Owner records:**
  - #1265 c.6846206075: `amaybaum`, 2026-11-13T06:44:20Z. The quotes are accurate; the bullets are
    run together and the opening clause is elided with "…".
  - #1265 c.6848447181: `amaybaum`, 2026-11-13T08:54:09Z. "Merge now (Recommended)" and "What landed:
    … No claim is promoted." are verbatim.
  - #1169 c.6865177667: `amaybaum`, 2026-11-13T21:19:31Z. The OQ-10 text is verbatim from "a short
    paper-only note …".
- **Reviews:**
  - 5888322900 is on #1265 at `a965818e`, and its quote is verbatim (bold removed).
  - 5898122286 is on #1279 at `c7ce4f28`. The "precedent alone …" quote is verbatim, and "reproducibility
    basis" is a fragment of "a specifically explained reproducibility basis".
  - 5895564670 is on #1274 at `d015131d`; see F5.
- **The #1265 PR body** reads "**Draft research archive. Not for merge.**" and "**Landing:** not
  authorized." It was merged at 08:53:50Z, by merge commit `c3b5f37a`.
- **The four `STATUS.md` notes on `main`:**
  - each has the heading "What the record establishes";
  - each has the Basis line as quoted, with #1245 for W1-1;
  - none has a remediation entry;
  - OA-2 and OA-3 cite OA-1 r4, and OA-3 also cites OA-2 r3/r4, each landing in the same PR.
- **The batch-1 Basis wording**: it is at `native-preparation-source-1-20261110/STATUS.md`:87, and
  also in four other batch-1 notes.
- **REVIEW-r1 F7**: it renames the heading "What the record supports, and at what strength".
- **The consequences table** (lines 108–118), against `INTEGRATION-ASSESS-r2.md` §0, §3, §4, §5 and
  §7 at the same head; see F12.
- **The register.** None of the barred strings occurs in the note. It contains no reader-instruction
  or revision-history phrases and no caps emphasis.

***

## Findings

### F1 (Medium): the closing sentence weighs against R-b using a mark the owner later acted on

- **Where:** NOTE-OQ10.md:145–147, and the history paragraph at :32–39.
- **Evidence.**
  - The note ends: "R-b rests on that sentence, which #1097 marked 'For the owner to confirm' before
    it merged." This is the only evaluative remark the note attaches to any reading's textual basis,
    and it counts against R-b.
  - Four facts that bear on the mark are left out:
    1. The conditions follow the owner's own adjustments, which the same #1097 description quotes:
       "New research evidence may also land when it is needed for reproducibility or to support
       existing records, even if the broader scientific programme remains unfinished."
    2. The owner gave a reason for them: "I am concerned that Rule 2 will lead to more issues where
       main will contain unverified data. We should aim to fix the unverified data, or remove it if
       not possible to fix."
    3. #1097 was merged by `amaybaum`, and it has no comments.
    4. §A.46 was amended again the same day, by `ab6211d7` (authored as `amaybaum`, merged in #1103).
       That amendment left item 2 unchanged, and the adoption line records it as "Amended the same
       day by owner decision".
  - Without these facts, the paragraph tilts the question that §5 is meant to leave open.
- **Fix.**
  - Replace :145–147 with: "No recommendation follows from the text alone: R-a and R-d each make
    item 2's "Work that meets none of these conditions …" sentence satisfiable by the landing itself,
    and R-b rests on that sentence."
  - Append to the history paragraph after :39: "The conditions follow the owner's adjustments quoted
    in that description ("New research evidence may also land when it is needed for reproducibility
    or to support existing records …"), given after the owner's concern "I am concerned that Rule 2
    will lead to more issues where main will contain unverified data." #1097 was merged by
    `amaybaum` and has no comments; §A.46 was amended again the same day by owner decision
    (`ab6211d7`, #1103), leaving item 2 unchanged."
  - Alternatively, delete the flag-based clause and keep the history paragraph as it stands.

### F2 (Medium): a coherent variant of R-b is missing, and its consequences differ

- **Where:** NOTE-OQ10.md:90–93 (R-b), the R-b column at :108–118, and owner question 1 at :135–139.
- **Evidence.**
  - R-b says each landing "needs a recorded owner exception per record". It does not say what form
    the exception takes.
  - Every candidate already needs a separate recorded owner merge decision (IA2 §4 preamble). §A.45
    rule 7 makes that decision the integration authorization: "**Integrate:** reviewed work enters
    `main` with its scientific scope preserved".
  - So R-b has a variant, call it R-b′, in which the merge decision is itself the exception provided
    it says so. Under R-b′ the R-b column reads "lands after gates, with the exception recorded in the
    merge decision", not "needs an exception" as a further, unspecified instrument.
  - The variant also changes the consequence at :125–127. The #1265 merge record (c.6848447181) says
    "as research records on their stated scope. No claim is promoted." It names neither §A.46 nor an
    exception. Under R-b′ the question is whether that record could serve as the exception.
- **Fix.**
  - After :93, add: "A variant (R-b′) takes the recorded owner merge decision each landing already
    needs (§A.45 rule 7, "**Integrate:** reviewed work enters `main` with its scientific scope
    preserved") as that exception, where the decision says so; the #1265 merge record
    (c.6848447181) names no exception."
  - After :123, add: "Under R-b′, the R-b column reads: lands after gates, with the exception recorded
    in the merge decision."
  - In owner question 1, after "(R-b)", add: "and, if so, may the recorded owner merge decision itself
    be that exception (R-b′)".

### F3 (Medium): item 4's remediation requirement is presented as specific to R-a

- **Where:** NOTE-OQ10.md:110–116 (R-a cells "status note needs a remediation entry"), :122–123, and
  owner question 2 at :140–141.
- **Evidence.**
  - Item 4 applies to "A claim on `main` whose verification is incomplete", whatever basis the claim
    landed on. A record landed under R-b's exception, or under R-d with open items, is equally on
    `main`.
  - So the note's own owner question 2 ("Whatever the answer, does item 4's remediation plan apply
    …") contradicts :122–123 ("Under R-a, the remediation entry … would be needed").
  - Under R-a, item 4's four-way split is part of "item 4's apparatus" (:86). IA2's #1274 note
    supplies it ("Verification status (§A.46 item 4)"); IA2 steps 2–7 do not. The R-a cells mention
    only the remediation entry.
- **Fix.**
  - In the R-a cells for #1275 to #1276, replace "status note needs a remediation entry" with
    "lands after gates".
  - Replace :122–123 with: "Item 4 applies to any landed claim whose verification is incomplete,
    whatever its basis: IA2 specifies its remediation entry and verification-status split only for
    #1274 (§4 step 1); steps 2–7 list neither (owner question 2)."

### F4 (Medium): the item 6 consequence under R-b is understated

- **Where:** NOTE-OQ10.md:125–127.
- **Evidence.**
  - "item 6 makes no removal automatic" is accurate. Item 6 also says: "For other material that has
    not met the verification standard for its specific claims, the normal proposed disposition is
    removal from the current tree *if the audit establishes that it is unnecessary*". It adds that
    verified evidence "is kept on `main`".
  - Under R-b, the four #1265 records are model-reviewed and are needed by no established claim. They
    therefore fall within that audit, and owner question 3 asks whether the ruling reaches them.
  - Under R-d, if model review meets item 1, they are kept as verified evidence.
  - Leaving out the operative clause understates what owner question 3 decides.
- **Fix.** Replace "item 6 makes no removal automatic" with: "item 6 makes no removal automatic
  ("Removal of research evidence from `main` is never automatic") and, for material that has not met
  the verification standard for its specific claims, makes "the normal proposed disposition …
  removal from the current tree *if the audit establishes that it is unnecessary*", after that audit
  and separate owner authorization".

### F5 (Low): R-d paraphrases a review and compresses item 7 inaccurately

- **Where:** NOTE-OQ10.md:99–100.
- **Evidence.**
  - Review 5895564670 reads: "An ACCEPT by a model is not independent mathematical verification
    (§A.46)". The note's "model ACCEPT is not verification" drops "independent mathematical".
  - "§A.46 item 7 bars unverified premises" omits the scope: item 7 bars them *as premises of an
    established claim*, absent independent validation of that premise.
  - The more exact point bears directly on R-d. The OA-1, OA-2 and OA-3 claims each state that they
    rest "partly on research records not independently established". W1-1's claim does not say this.
- **Fix.** Replace :99–100 from "review 5895564670" with: "review 5895564670 on #1274 states "An ACCEPT
  by a model is not independent mathematical verification (§A.46)"; §A.46 item 7 requires independent
  validation of each material premise of an established claim, and the OA-1, OA-2 and OA-3 claims
  state that they rest "partly on research records not independently established"."

### F6 (Low): OQ-10 does not put the question in R-d's form

- **Where:** NOTE-OQ10.md:97–98.
- **Evidence.**
  - IA2 §6 does pose the R-d question: "Whether model-reviewed paper results meet §A.46 item 1 so that
    item 2's first condition applies is an owner question (OQ-10)."
  - IA2's OQ-10 (§7) is framed differently. It asks whether the #1265 basis is the landing basis "or
    must each meet §A.46 item 2's literal conditions". That is R-a against the literal text.
  - The owner's OQ-10 (c.6865177667) names items 1, 2 and 4 only.
- **Fix.** Replace "the form in which IA2 §6 and OQ-10 put the question" with "the form in which IA2
  §6 puts the question it refers to OQ-10".

### F7 (Low): the Basis line is misplaced, and one composite quote does not hold for W1-1

- **Where:** NOTE-OQ10.md:54–58.
- **Evidence.**
  - Each note's "Landing" section ends with the **Owner record** bullet. **Basis** is the bullet
    before it (for example `oa-1-20261112/STATUS.md`:123–127). The note's "Each … ends:" is
    therefore wrong.
  - W1-1's claim does not contain the quoted evidence layer "paper-level research findings … not
    adopted; no manuscript claim affected". Its parenthetical reads "paper-level hand derivations
    with independent AI-agent reviews, not machine-checked; the candidate list is not proven
    exhaustive; consistency axis only; no manuscript claim affected".
- **Fix.**
  - Replace "Each of the four `STATUS.md` notes (…) ends:" with "Each of the four `STATUS.md` notes
    (…) states, in its "Landing" section:".
  - Replace the last sentence of the bullet with: "Each gives a "Claim supported by this record" in
    quotation, closing with its evidence layer (OA-1 to OA-3: "paper-level research findings: …; not
    adopted; no manuscript claim affected"; W1-1: "paper-level hand derivations with independent
    AI-agent reviews, not machine-checked; … no manuscript claim affected")."

### F8 (Low): W1-1 carries no evidence tags

- **Where:** NOTE-OQ10.md:72, the row for item 4's stated status.
- **Evidence.** In `w1-1-20261112/STATUS.md` at `c3b5f37a`, a search finds no `[W]`, `[RW]`, `[P]`,
  `[K]` or `[R]`. W1-1 states its layers in words ("hand derivations, independently agent-reviewed,
  on manuscript statements and one Lean statement read on `main`").
- **Fix.** After "evidence tags [W], [RW], [P], [K], [R]", insert "(OA-1 to OA-3; W1-1 states its
  layers in words)".

### F9 (Low): "last sentence" names the wrong sentence, and the mapping omits item 2's actual last sentence

- **Where:** NOTE-OQ10.md:36, :87, :145–146, and the mapping table at :65–76.
- **Evidence.**
  - Item 2's last sentence is "§A.42 item 5 and §A.28 govern what is added; item 6 governs removal."
    The note uses "last sentence" for the sentence before it, "Work that meets none of these
    conditions …". #1097's description uses the same loose wording.
  - The actual last sentence brings §A.42 item 5 into item 2: "Only what a surviving claim needs is
    retained." That bears on every reading. Under R-a, the question is whether the record's own scoped
    claim counts as a "surviving claim".
  - The four `STATUS.md` notes cite neither §A.42 item 5 nor §A.28.
- **Fix.**
  - At :36, :87 and :145–146, replace "last sentence" with "the "Work that meets none of these
    conditions …" sentence".
  - Add a mapping row after :71: `| 2: "§A.42 item 5 and §A.28 govern what is added" (§A.42 item 5:
    "Only what a surviving claim needs is retained.") | Not cited in the four notes | met on R-a if
    the record's own scoped claim is the surviving claim; otherwise as row 1 |`.

### F10 (Low): §A.42 item 8's same-landing closure is relevant context for R-a and for row 3

- **Where:** NOTE-OQ10.md:69 and :84–88.
- **Evidence.**
  - §A.42 item 8 closes a support gap "no later than the record lands", "by landing the content the
    claim needs". The rules therefore expect supporting content to land in the same merge as the
    record that needs it.
  - This is not a basis for the record that needs the support. It is, however, textual context for
    R-a's reading of "already on `main`" as including the same merge.
- **Fix.** Append to R-a (:88): "§A.42 item 8 closes a support gap "no later than the record lands",
  by landing the content the claim needs, so support landing in the same merge as its dependent is
  contemplated there; it does not supply the dependent record's own basis."

### F11 (Low): the consequences table cites IA2 §5 for #1274, and the #1275 R-d cell omits unit 2(a)

- **Where:** NOTE-OQ10.md:105 and :111.
- **Evidence.**
  - IA2 §5 does not list #1274. Its "ready after `STATUS.md`" disposition is in §0 step 1 and in the
    §3 heading.
  - For #1275, IA2 §3 records "Unit 2(a): not traced here" under item 8. Under IA2's option (a),
    unit 2(a) lands with unit 1.
- **Fix.**
  - At :105, replace "dispositions from IA2 §5" with "dispositions from IA2 §0, §3 and §5".
  - In the #1275 R-d cell, append: "; unit 2(a) not yet traced (IA2 §3), under option (a)".

### F12 (Info): two statements could be firmer or more exact

- **Where:** NOTE-OQ10.md:52–53 and :74.
- **Evidence.**
  - **:52–53, "The PR body at merge still read".** The current body has this text. Body edit history
    is not available through the REST API, so the wording "at merge" cannot be confirmed directly.
    The body still names head `2d064a71`, which predates the merged head `a965818e`, so it is
    consistent with no edit after merge.
  - **:74.** I searched all 207 comments on #1169 and all 9 on #1245. None contains "remediat"
    together with OA-1, OA-2, OA-3 or W1-1.
- **Fix (optional).**
  - At :52, say "The PR body reads".
  - At :74, replace "(their comments were not searched)" with "nor does any comment on either Issue
    that names OA-1 to OA-3 or W1-1".

***

## Answers to the review questions

1. **Quotes.** Items 1, 2 and 4 are verbatim against `c3b5f37a`. Item 6 is paraphrased, not quoted,
   and the paraphrase is accurate as far as it goes (F4).
2. **Facts about #1265.** The two owner records, the PR body, the four Basis lines and headings, the
   batch-1 wording and the #1097 quote all hold. The slips are F7 (Basis is not the last bullet; the
   W1-1 evidence-layer quote), F8 (W1-1 has no evidence tags) and F12.
3. **The mapping.** Correct row by row, except that item 2's actual last sentence has no row (F9).
   Item 4 is mapped correctly, but its consequence is attributed to R-a alone (F3).
4. **The readings.** R-a, R-b, R-c and R-d are each coherent. R-b′ is missing (F2). The consequences
   for #1268–#1276 agree with IA2, apart from F3 and F11.
5. **Neutrality.** No reading is recommended, and no waiver or rule change is implied. The one tilt
   is the closing clause (F1). The owner questions are precise; question 1 needs F2's addition.
6. **Register.** Clean.

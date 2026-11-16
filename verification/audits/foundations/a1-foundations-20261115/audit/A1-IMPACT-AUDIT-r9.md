# A1 impact audit, r9: which A1 results have a visible-sector form

**UNREVIEWED.** Paper-only, read-only. No manuscript, Lean module, census entry or record is edited;
nothing is computed, built, committed or pushed, and no GitHub record is written. The comments on #1169
were read through the GitHub connector, only to quote the record; twelve were quoted in r6. Papers, Lean source and the
census registry were read at `main` by `git show`. **r6 is r5 re-pinned from EF-1 r3 to EF-1 r4, with a
consistency pass. It is not a rewrite.** It also applies the adopted directions of #1169 comments 6897859755 and 6897946443 (review text relayed and adopted by the owner; Standing), given after EF-1 r4 was reviewed; the second asks for more than a re-pin (§12.3, §12.4, §14.4). It replaces r5 in full, is self-contained and is not a diff; §17
lists what changed from r5 and why, and nothing else was changed.

**r7.** r7 is r6 with the findings F1–F22 of its review applied, re-pinned to EF-1 r6 (EF-1 r5 with the nits of its recheck applied), and with the in-session requirements of 2026-11-15 applied (adopted direction, c.6898395533). §22 gives a disposition for every finding and lists what r7 did not do. Rows changed in r7 are marked "Changed after review; unreviewed". The paragraph above is r6's description of itself.

**r8.** r8 is r7 with the items that r7's §22 listed as not done completed, and with one correction of attribution made on the record. Ten of the thirteen #1169 comments quoted here hold review text that the owner relayed in session and adopted on 2026-11-15 (#1169 comment 6898760764); r7 and earlier revisions cited them as the owner's words, and r8 cites them as adopted directions (Standing). r8 changes no row's category, reason, class, direct-proof entry or concession, no count and no recommendation. §22 lists what r8 changed, with each cell it rewrote, and what is still not done. The option texts of §19 and the lines r8 added to tables are unreviewed.

**r9.** r9 is r8 (sha256 `f43261fea2b841392bfdafcd344113d01573b9963d430ed31320b79224e70b3d`) with the corrections of its focused confirmation applied (`CONFIRM-A1-IMPACT-r8.md`, sha256 `77159f466edbe4129edd1228c24951db3a21fb260d5c120f8a5d6e1869aaa31b`; independent, non-author, paper-only): its edits E1–E33, of which E18 calls for no edit, and the other corrections it states. r9 changes no row's category, reason, landing, class, direct-proof entry or concession, and no recommendation. Where the confirmation's recommended class differs from this audit's (AM-7.2 and AM-7.3) the audit's class is kept and both positions are shown side by side (§14.1, §20). Each question's "Decision-ready?" field carries the confirmation's verdict and says whether the question depends on the pilot authorized in #1169 comment 6898613777 (§19). §22 lists every edit with its location. The edits were applied by exact replacement at the places the confirmation names; the text as edited has not been re-read by the confirmer. The paragraphs above are the descriptions that r6, r7 and r8 gave of themselves.

**Goal link (§A.47).** Priority item 2: the A1 dependence of the main equivalence and of the results
built on it (#1169 comment 6894872312). For each result that consumes ledger item (ii) of Main §4.5
(Substratum's A1, total finiteness), the audit decides which treatment the owner's visible-sector-only
condition calls for, what each treatment would break, what each recovery would need, and which owner
decisions the treatments wait on. It decides no status, adopts no premise and gives no result recovery
credit.

**Provisional headline (adopted direction, #1169 c.6896771264).** "none of the 56 results currently
establishes a justified observational constraint; that does not mean none can be recovered." The population is now 57 (adopted direction, #1169 c.6898395533: "The population is now 57."): the 56 rows and AM-5b (Main:290–324), which on this audit's unreviewed reading does not establish one either. With the number adjusted for that reason only: none of the 57 results currently establishes a justified observational constraint; that does not mean none can be recovered.

## Standing

- **r7 inputs.** `A1-IMPACT-AUDIT-r6.md` (sha256 `f7e8ce7ee8a557275ad7205f74c91da8f632c70e32b973b9b54424fa2a387d15`, verified) and its independent review `REVIEW-A1-IMPACT-r6.md` (sha256 `fd02b8be963e0fedb2d3e79f0a0cc72669a1427620c6423c2d8021e6e881d871`; ACCEPT WITH CHANGES; findings F1–F22). The comments on #1169 were not re-read for r7. **They were re-read for r8**: comments 6894872312, 6895032895, 6896070253, 6896252651, 6896496410, 6896771264, 6896890693, 6896940222, 6897254631, 6897455387, 6897859755, 6897946443 and 6898395533, through the GitHub connector, and every quotation in this document from those comments, the owner's own words and the adopted directions alike, was compared with them character for character. Comments 6898613777 and 6898760764, recorded after r8 was begun, were read as well; the second corrects the attribution of ten of the thirteen (see "Owner decisions, and review text the owner relayed and adopted" below). Three quotations differed, each by a single quotation mark written for the record's double mark inside the quoted sentence (the coverage sentence, twice, and the rule for FIRM); they are corrected, and each of the three is now set between “ and ” so that the record's own marks stand inside it. The words r7 gave as said in session after the review of r6 are recorded in 6898395533 and are cited to it. In 6896070253 the sentences beginning "Remove A1 (total finiteness)" and "Results that need the total to be finite" are the coordinator's proposal, which the owner accepted in the same record with "Yes proceed as suggested."; they are cited below as the proposal the owner accepted, not as the owner's words. In table cells `|…|` in a quotation is written `\lvert…\rvert`, and a bar inside a formula of this audit's own is written `∣`, so that no bar splits a cell. The bullets below that describe r6's inputs are r6's.
- **Inputs.** `A1-IMPACT-AUDIT-r5.md` (sha256
  `38cf2fbbf789c71df9cf5b6173ba7fd07c77b0debd1d025a3e90e19c9df0170f`, 2726 lines, verified), which r6 starts
  from and which has no review. Behind it: `A1-IMPACT-AUDIT-r4.md` (sha256
  `04f42e7c53d1eaa894a9ae56ab1a10a7c874f1cbd3b1660bd27514fa6c5d1324`, 2173 lines, verified) and its
  independent review `REVIEW-A1-IMPACT-r4.md` (sha256
  `b0787d3095e0a731ce6849abd71c99b80aa215a02f04dfc16b78e7300a9e4a4f`, verified; verdict ACCEPT WITH CHANGES;
  changes C1–C13; sections A, B, C). r5 checked every change of that review first-hand at `main` before
  applying it (§1); r6 carries those responses and re-checks what the re-pin touches.
- **Wording.** Below, "r5" marks a position or a change that r5 made and that r6 carries unchanged; "r6" marks
  what this revision adds or changes; "this audit" covers both. "r4", "r3" and "r2" without "EF-1" are earlier
  revisions of this audit.
- **EF-1, pinned to r6.** From the sibling EF-1 unit, read only and not touched: `EF-1-r6.md`, sha256 `34f3ec8f019053cb0755cc089d94a91f45ef6c19ac354e763b5b8285e6fe6d9f` (3171 lines; hash verified for r8). By its own table "r6 changes", read for r7 and again for r8, it is `EF-1-r5.md` (sha256 `3cf761f0313e57eb6718f82bf3d6dc54dbbe710a85736c3a5858c84ae0beb16d`) with the eight nits of its recheck (`RECHECK-EF-1-r5.md`, CONFIRMED WITH NITS; read in full for r7) applied and nothing else changed; no nit touches a proof. **Every citation of EF-1 below is to r6.** For r8 each citation that r7 wrote as r5 was moved to r6 after comparing the cited place with that table: the places the nits changed are the summary, the status section, the tier table, the marks on N2.10 (in N3.5 and EF-G10), questions 9 and 10 of §11, and two rows of the second §4.2 table (Lemma 3; the one-step coherence results). Four statements here cite one of those places and were brought to r6's wording: the proof-status tiers (nit 8), the one-step coherence row AM-5b (nit 5), and the descriptions of questions 9 and 10 (§19, concordance; §20, D15). Every other citation is to a place the table does not list, where r6 is r5 word for word. For r8, §4.2 of EF-1 r6 (both tables), its §11 (questions 9 and 10) and its changes table were read first-hand; the rest of EF-1 r6 was not re-read, and the re-pin otherwise follows the delta R1–R21 of the review of r6 (§21, §22). History of the pin: r5 of this audit was pinned to EF-1 r3, r6 to `EF-1-r4.md` (sha256 `b429d3afa017bfc260b1eea1eee169632902d5a5bb485019eaf27b55f537d1b1`), whose review is `REVIEW-EF-1-r4.md` (sha256 `64ec14f4d973de24cb8be619ae3b80bb17377727d3c47399045b06e1d85e2d81`, ACCEPT WITH CHANGES); EF-1 r5 is a targeted correction of r4. A citation below that names EF-1 r4, or its review, names a position taken at that revision. EF-1 r6 keeps r4's labels; r4's groups A, B, C are r6's claims 1, 2, 3. Every use of EF-1 remains provisional [IR]: paper proofs in unpushed drafts, not kernel-checked.
- **Proof status of EF-1 r6's statements** (the review of EF-1 r4; the recheck of EF-1 r5).
  - **Checked, under their stated hypotheses:** the full-system measure theorem (M-full), whose hypotheses are a bijection of the full system, each site reading finitely many sites and read by finitely many, and a finite alphabet at every site; the intervention lemma PM-I; the compactness lemma K; the necessity result (Proposition N) and its one-law refinement; Lemma C, both directions; Corollary C1; Lemma C′. Each has had one independent check; all are paper proofs.
  - **Still unproved:** whether a closure preserves everything a particular audited result needs.

  **No recovery credit anywhere, and no recovery class here rests on any of these statements.** The three tiers of adopted direction c.6897859755 (quoted below) predate the recheck and place the closure characterization under "Still unchecked"; whether the recheck moves it is the owner's to accept. The review of this audit did not, on what it reported, overturn the checked EF-1 mathematics; it did not re-derive it. EF-1 labels below (N1.3, N1.5, N3.6, §P, §4.0, §4.2, F1–F7, P1–P2, D1–D8, FS-all, (M-full), (M-desc-own), (M-desc-some), Lemma K, Lemma C, Corollary C1, Lemma C′, EF-G1, …) are r6's, unchanged from r5. Since r4, EF-1 has completed two rows of its §4.2, added a row for the §3.4 obstructions and added a second table (window confinement; direct-proof target); those cells are compared with this audit in §14.3 (Table 5) and §20 (T22–T32).
- **The properties each proof uses are traced here, not taken from EF-1.** The review of EF-1 r3 found
  r3's §4.2 column incomplete in seven of the eight classes it traced, so r5 read every "properties the proof
  uses" entry of §14.3 from the proof on `main` itself, with file and line; where a proof was not traced in
  full, the entry says so. EF-1 r4 has since redone its §4.2 from full traces; the review of EF-1 r4 retraced seventeen of its classes and found them complete in fifteen, with proof requirements missing in two and one class absent. r6 leaves
  §14.3's traces as r5 made them, compares them with EF-1 r4 §4.2 class by class, and lists every difference
  in §20 (T1–T21) with both positions; it adopts neither side silently.
- **Read for consistency only.** The A1-validity gem review r3 (`A1-VALIDITY-GEM-r3.md`, sha256
  `21c011585769ed0d4ce211d6667b9be98f7f6e362d587f2b30694efab4003c98`), cited as "the validity review".
  All of these are unpushed drafts.
- **Owner decisions, and review text the owner relayed and adopted** (recorded on #1169 by the account
  `amaybaum` on 2026-11-15; each comment read on GitHub for r8; times UTC). Quotations are exact. Two kinds of
  text are quoted, and they are kept apart throughout (#1169 comment 6898760764, 17:55, read for r8).
  - **The owner's own words** are in comments 6894872312, 6895032895 and 6896070253 (and, outside this audit's
    subject, "Yes, I approve l.  Proceed as suggested." in 6898613777). Only these are cited as the owner's.
  - **Adopted directions.** The texts quoted from comments 6896252651, 6896496410, 6896771264, 6896890693,
    6896940222, 6897254631, 6897455387, 6897859755, 6897946443 and 6898395533 are review text that the owner
    relayed in the coordinating session. The owner did not write them. Asked whether they were the owner's own
    directions or relayed review text, the owner answered (amaybaum, 2026-11-15; 6898760764): "Relayed, and I
    adopt them." Each is cited below as **adopted direction, c.[id]**, which means: review text relayed and
    adopted by the owner (amaybaum, 2026-11-15; #1169 c.[id]). "I", "my" and "your" inside such a quotation are
    the review text's, not the owner's. r7 and the earlier revisions cited these ten as the owner's words; the
    quoted text is unchanged, and only the attribution is corrected.
  - **6894872312** (13:15), the owner's own words. "The whole idea around why it looks quantum is that the visible sector is
    finite. So I think we need to limit A1 results so it only applies to the visible sector, which we
    know is indeed finite." and "Yes, start the impact audit. Anything that can't align with the visible
    sector only condition should be either recovered as such, or removed completely." The record adds:
    "No manuscript edit is made until the owner has seen the audit."
  - **6895032895** (13:28), the owner's own words. "Is A1 a valid assumption or not?" and, on the proposed paper-only validity
    review, "Yes please proceed as suggested".
  - **6896070253** (14:26), the owner's own words. The coordinator's proposal: "Remove A1 (total finiteness) as a claim about
    the whole substratum, because no observation can check it." and "Results that need the total to be
    finite stay as mathematics about finite models, with no claim that nature is one. No manuscript
    changes yet." Owner: "Yes proceed as suggested. Perhaps it's possible to show that the effective
    hidden sector is finite, and therefore the effective total substratum is finite as well?"
  - **6896252651** (14:40), adopted direction. "The key distinction is "these results currently establish no justified
    constraint on observations", rather than "these results cannot constrain observations." The first
    describes the audit's finding; the second would require a stronger proof." The review is to confirm
    "Why each result loses observational force: because A1 is unsupported, because the connection to
    observations is missing, or because the result concerns only the whole system.", "What recovery
    requires: separate results recoverable under weaker premises from those needing genuinely new
    assumptions." and "How Q2(b) changes the disposition: map the original 56 results into the stricter
    outcome, distinguishing removal of a physical claim from deletion of valid mathematics." Also: "is
    effective finiteness justified independently of A1, and is it sufficient for the specific results it
    is meant to recover?" and "I would leave Q2(b) undecided until the reviewed audit and that unit are
    available. Present the 14 questions with recommendations and dependencies so we can resolve the
    foundational choices before their downstream consequences."
  - **6896496410** (15:00), adopted direction. "This gives a promising recovery route: finite observational descriptions
    over any fixed horizon, without assuming a finite universe. It does not yet recover any particular
    result until that result's proof is checked." On the all-time form: "the fixed-horizon argument does
    not, by itself, supply one finite model valid for every horizon. That is narrower than proving such a
    model impossible." On recurrence: "a finite description for a chosen horizon supplies no recurrence
    guarantee within that horizon." On the order of the claims: "For every horizon, there exists a finite
    description: potentially established here." and "There exists one finite description valid for every
    horizon: not established here." and "Any audited result requiring the second cannot be recovered
    merely by proving the first. I'd keep adoption and the 14 decisions pending the two reviews."
  - **6896771264** (15:21), adopted direction. On the patch lemma: "One detail belongs in the patch lemma: when settings or
    inputs are present, the comparison must hold them fixed—or specify the same adaptive policy and
    include the information it uses. Matching the initial patch alone need not give matching observations
    under different interventions." On r4: "The headline remains provisional: none of the 56 results
    currently establishes a justified observational constraint; that does not mean none can be
    recovered." and "Overlapping counts: 47 + 6 + 3 accounts for all 56. State how the 7 fixed-horizon
    candidates overlap with the 11 weaker-premise candidates and the 8 needing new assumptions, so those
    counts cannot be mistaken for separate groups." and "AM-31: identify the exact scope reading that
    permits recovery, its textual basis, and the disposition if that reading is rejected. An unresolved
    interpretation must not silently count as an available premise." and "The revised Q2(b) now preserves
    valid mathematics while addressing unsupported physical claims. That clarifies the option; it does
    not yet settle whether to choose it." and "Bring the 15 questions after both reviews, with any
    remaining disagreements visible. No adoption or cleanup decision is implied by this status update."
  - **6896890693** (15:30), adopted direction. On EF-1: "Including their read sites repairs the dependency statement;
    finiteness still requires those reads to have finite support." and "For Bell experiments, including
    the setting-generation regions establishes dependency coverage; it does not establish measurement
    independence. That remains a separate premise to track." On the review of r4: "The review supports
    proceeding with the corrections, but "mechanical" understates several of them: AM-31's premise
    classification, N-3's replacement status, and relocation destinations affect the scientific
    interpretation." and ""Firm" means the required premises are already available, not that recovery
    has been proved. This applies to the two firm fixed-horizon candidates too." and "N-3 is a
    replacement candidate, so it should not count as recovery of the original result." and "The Q2(b)
    mapping totals 17 results. Label that subset explicitly and connect it to the full 56-row
    disposition. Preserve AM-34's paper proof, and keep the reviewer's A1-free reading of Main:274–278
    visibly attributed until resolved." and "Naming relocation destinations is necessary before Q2(b) is
    decision-ready, particularly where Main's independence could be affected." and "Nothing here
    constitutes adoption, recovery, or a cleanup decision."
  - **6896940222** (15:34), adopted direction. "A finite description of observations need not preserve the original
    system's bijectivity, invariant measure, recurrence structure, or other properties a downstream proof
    uses. That is the main risk: transferring properties of finite whole systems to finite observational
    descriptions without justification." and "keep effective finiteness as a candidate replacement
    premise, but give it no recovery credit until each theorem's actual requirements are checked." The table in that record assesses "That description preserves everything needed by a particular
    A1-dependent theorem" as "Requires a separate proof". The record notes that the assessment rests on
    the coordinator's summaries, not on a reading of the revised proofs.
  - **6897254631** (15:59), adopted direction. "if the required conditions are already established, per-horizon finiteness
    is a derived lemma, not a new assumption. "Candidate replacement" describes its possible role in
    proofs that currently use A1." and "finite dependency sets and finite alphabets establish the finite
    observational description. A normalized starting law supplies probabilities on that description; it
    is not needed merely to establish finiteness. Any stronger distributional properties require their
    own justification." and "My assessment remains: convincing core argument, with downstream recovery
    unproved and the exact premises awaiting verification in the reviewed text." The record's next steps include "The corrected impact audit (r5) is re-pinned to EF-1 r4.", which is this revision.
  - **6897455387** (16:14), adopted direction. On the standing of the work: "This strengthens the case for the core
    effective-finiteness lemma, while showing that the downstream preservation assessment still needs
    substantive work. Missing proof requirements in seven of eight traced classes is more than a minor
    correction." On the uniform measure: "a bijection of the full system may preserve its uniform product
    measure without making the finite observational description an autonomous, measure-preserving system.
    The reviewer's new proof could establish the first; transferring that property to the description remains
    a separate question." and "The reviewer's new measure-preservation proof also needs independent checking
    before it supports any recovery classification." On finite support: "finite support on each individual
    run does not by itself establish one finite patch covering every possible branch. The revised statement
    must make clear which it proves." On the plan and the status: "The planned r4 and re-pinned audit address
    the right issues. My assessment remains: the core argument looks increasingly convincing; its ability to
    recover particular A1-dependent results remains open." r5 had these directions only as a relay from the
    coordinating session and marked them as not recorded; they are quoted here from the record.
  - **6897859755** (16:45), adopted direction, recorded after the review of EF-1 r4. On the description and its measure:
    "Failure of automatic inheritance does not imply that no suitable finite closed model exists. Any wording
    suggesting the latter should be withdrawn." The three tiers of proof status: "Checked: the full-system
    measure theorem, intervention lemma, compactness lemma and necessity result, under their stated
    hypotheses." and "Still unchecked: the reviewer's characterization of when a measure-preserving closure
    exists, including its application to second-order rules." and "Still unproved: whether such a closure
    preserves everything required to recover a particular audited result." On the closure: "So the closure
    result earns no recovery credit yet. Its being a chosen, window-valid model does not automatically
    disqualify it either: it could suffice for a theorem whose requirements are entirely confined to that
    window. That is what the proof-requirements check must determine." On Lemma K: "For compactness, the
    summary should say "finite reads on every run, under the lemma's other hypotheses," so it does not turn a
    conditional theorem into an unrestricted claim." The assessment in the relayed text, which the owner adopted and which is not a finding of this audit: "My assessment has strengthened: effective finiteness now has substantial checked
    mathematical support. Its physical consequences remain unresolved." These directions reached this revision
    first as a message from the coordinating session; they are quoted here from the record.
  - **6897946443** (16:52), adopted direction, the latest comment when r6 was finished. "We should simplify how the conditions
    are organized, and concede limits where necessary. We should not relax a condition merely to make a
    recovery succeed." and "The useful simplification is to stop treating every condition as a requirement
    for every result:", followed by a table, which is quoted in §0 and used there as the organizing
    key. On scope: "What I would concede now is scope: effective finiteness does not, by itself, recover A1's
    full role. Some results may survive only as finite-model mathematics; some may need replacement theorems;
    others may remain conditional. That is an acceptable scientific outcome." On the recovery target: "What I
    would simplify is the recovery target. If a result concerns only a finite experiment, ask whether we can
    prove that observable conclusion directly. We need not reconstruct an autonomous finite universe, global
    recurrence or a global invariant measure unless the proof genuinely requires them. A new direct proof
    could avoid conditions needed by the old proof." The two barred shortcuts: "Adopting a new assumption
    solely because it rescues a desired result." and "Calling a conditional recovery an unconditional
    consequence of OI." The recommendation: "keep the checked effective-finiteness lemma, pursue the weakest
    sufficient proof for each observable claim, and explicitly concede everything that remains unsupported.
    That simplifies the programme without lowering its evidential standard. The exact conditions we can
    remove must come from the reviewed proof traces, not from the summaries alone."
  - **The rule "a recovery candidate is not a recovered result".** Relayed in session on
    2026-11-15. When r6 was begun it was in none of the comments on #1169 (267 then), and r6's brief
    gave its source as "owner, in session, not separately recorded". It has since been recorded: 6897859755
    carries it as a sentence from earlier in the same session, "That addresses all three overstatements
    and preserves the key distinction: a recovery candidate is not a recovered result." It is relayed review
    text adopted by the owner (adopted direction, c.6897859755), and is used below as a rule.
  - **6898395533** (17:27), adopted direction, recorded after the review of r6; read on #1169 for r8. On coverage: “the audit review samples the new columns, so its verdict should identify which rows were checked and which remain unchecked. "Fit for your decisions" need not mean every recovery route has been verified.” On the population: "The population is now 57. The reported direct-proof counts—11 yes, 13 partly, 32 no—still total 56. Classify the added passage or mark it unclassified, and update all affected totals and coverage denominators." On Q5 and Q6: "Q5/Q6 must respect Q12's conditional status. Correcting that contradiction is necessary for an informed decision, not merely a wording improvement." On recommendations: "The reviewer's proposed dispositions, including Q6(e), remain recommendations. I cannot endorse that option without seeing its text and basis." On readiness: "Marking changed rows unreviewed is appropriate, but any change that materially alters a question's basis needs focused confirmation before that question is called decision-ready." On the findings: "The other 13 findings should also have visible dispositions." On status: "The mathematical foundation has strengthened; the audit is still being corrected into a reliable decision document." The rule for FIRM, from the same comment, is quoted in §0.
- **How these records are used.** As authority and scope, not evidence (§A.45 rule 1). An adopted direction has the owner's authority from its adoption on 2026-11-15 (6898760764); before that it governed only wording rules and review checks inside this paper-only unit, as that comment records. Comment 6896070253
  is read as deciding the physical reading (A1 is not asserted of nature) and that the results needing A1
  are kept as mathematics about finite models. It is not read as answering Q2, which concerns where that
  mathematics is stated; Q2(b) is an option only (6896771264) and is not decision-ready until relocation
  destinations are agreed (6896890693; §12.2). No record is read as adopting a premise, crediting a
  recovery or deciding a cleanup.
- **Base.** `main` at `bf89ba133ee9f2926a317e8af067ccaa862ce2db`, fetched by name. Every manuscript,
  Lean and census citation is read at that commit.
- **Abbreviations.** `Main:n` is `papers/Main.md:n`; likewise `GR`, `SM`, `Sub` (Substratum), `Struct`
  (Structure), `Meth` (Methodology), `Comp` (Computation), `Cx` (Complexity), `Intro` (Introduction),
  `Medicine`, `Bioinformatics`. `FULL:n` is `book/The-Incompleteness-of-Observation-FULL.md:n`; book
  chapters by file name (`ch01:n` is `book/ch01-observation.md:n`, and so on). Census family numbers are
  0-based indices of `families` in `verification/lean-manuscript-census.json`. Lean paths are under
  `verification/lean-mathlib/OIBridge/`. "Review C1" to "review C13" and "review section A, B, C" are findings of `REVIEW-A1-IMPACT-r4.md`; "r3 review B1",
  "r3 review R1" are findings of the review of r3, and "review F1" to "review F17" findings of the reviews of r1
  and r2, all carried from r4.
- **Labels.** Support layers: K (kernel), P (paper proof), EX (exhaustive), RR (research record), support
  off `main`. **[IR]**: a reading made here or in an unpushed draft, not stated on `main` and not
  independently verified; no treatment's status rests on it alone. **[needs proof]**: a statement whose
  proof is not on `main`. **[reviewer reading, unresolved]**: a reading made by the review of r4 that r5
  reports with its attribution and does not settle. Claims are stated at their proved scope; for each
  equivalence the two directions are cited separately (§A.34). Premise labels L1–L10, FS and MI are
  defined in §14.2, with their counterparts in EF-1 r6's three groups (F1–F7, P1–P2, D1–D8); (M-full), (M-desc-own) and (M-desc-some) are defined in §0.
- **Scope limits.** The row list is r9 §7's (AM-1 to AM-38, PR #1303), complete relative to its recipe;
  33 L5 Lean modules are unread (r9 §7.4) and are not classified here. Rows N-1 to N-6 and the extra sites
  in §7 were found by r1, its review or r2. A consumer outside these recipes would be missed here as well.

## 0. The test, the categories and the headline rule

**The test applied to every row.** Can the result be stated and proved using only the finite visible
sector (Lemma 1, Main:46), the observer's finite registers and operations on them, and finite
realizations constructed per horizon from the visible law (Main:516, :518; Main:60: "a finite hidden
space is constructed, not assumed"), with no assumption on the cardinality of nature's total or hidden
sector? The Definition and the two axioms do not fix `|S|` (Main:60); total finiteness is ledger item
(ii) (Main:724).

**Why the realization-level reading is not enough by itself.** A realization built per horizon
reproduces the law only up to the horizon: "the realized process after time K is unconstrained"
(Main:520). A property of a realization that the law on the horizon does not fix (its order `L`, its
recurrence cycle, its periodicity, its asymptotic entropy rate) is a choice of the completion, not a
property of nature.

**The two finiteness forms, and what kind of object each is.** A *finite observational description at
horizon `n`* is the information needed to determine the observations over `n` steps; it says nothing
about the actual whole substratum (adopted direction, c.6896496410).
- **F-each.** For every fixed horizon `n` there exists a finite observational description. Status:
  potentially established. It is a **derived lemma, not a premise and not an assumption**: where its
  named premises are established, per-horizon finiteness follows from them. It has two routes.
  - *From Lemma 1 alone (reconstruction direction).* Every finite-horizon law has a finite reversible
    realization (K `S_imp_D`; Main:97, :516–520). This is on `main`.
  - *From locality (forward direction): EF-1 r6's Lemma PM (its N1.3), and Lemma PM-I (its N1.5) where
    settings, inputs or policies act* (paper proofs in an unpushed draft, provisional [IR]; the pointwise
    cone step is kernel-checked for a single readout time and a site type of any cardinality,
    `iterate_dependsOnlyOn_ball`, `RegionTower.lean:283`, section variables `{ι Q : Type} [DecidableEq ι]`,
    :246). EF-1 r6 states each lemma in a deterministic form first and a law form second, and sorts what they
    rest on into three groups (its §4.0). This audit keeps the three apart for every row (§14.3). **Each group
    needs its own justification, and none stands in for another.**
    1. **Finiteness premises (EF-1 r6 group A, F1–F7; no probability).** Site factorization (F1; ledger item
       (viii)), one deterministic update (F2; Main:54), finite reading sets (F3; this audit's L1) and a finite
       visible region with a site-local readout (F4; L8) establish that two initial configurations that agree
       on the finite patch `U_n = ⋃_{k≤n} ball(V, k)` have the same observation history on `[0, n]`, which is
       a function `G_n` of the patch data and of the rules on `U_{n−1}`. Finite site alphabets on the patch
       (F5; L2) make the patch data finitely many: that is the finite observational description. Where
       settings, inputs or policies act, two more premises enter: one protocol shared by the runs compared
       (F6), and finite supports (F7). Finite support has three statements in EF-1 r6, which are kept apart
       here (adopted direction, c.6897455387).
       - **All-branch form (FS-all; this audit's FS).** At each step, the set of all sites the policy could
         read, and that any intervention it could select could read or act on, taken over every record so far,
         every state and every value of the policy information, is finite. Then one finite patch `E_n` covers
         every branch, with an explicit bound (Lemma PM-I (a), (b); checked, with the memory clause, by the review
         of EF-1 r6).
       - **Per-run form (Lemma PM-I (a′); checked by the review of EF-1 r4).** For one run on which the policy's reads and the
         interventions' reads are finite, a finite patch determines the record of that run and of every run
         that agrees with it on that patch. It gives no single patch for all runs and no finite description of
         the law. Finite support on each individual run does not by itself give one finite patch for every
         branch, and neither does a bound on the size of each run's support (EF-1 r6, examples E1–E3).
       - **Lemma K (Lemma PM-I (f); checked by the review of EF-1 r4).** One finite patch for every branch
         also follows from "finite reads on every run, under the lemma's other hypotheses" (the wording of adopted direction c.6897859755). The other hypotheses are a finite alphabet at every site of the carrier and
         finitely many values of the policy information, and "every run" means every initial configuration and
         every value of that information. The proof is by compactness; it gives no bound on the size of the
         patch and no support for any intervention that holds in every state. Each hypothesis is needed: the
         conclusion can fail if one configuration has infinite reads, or if the policy information or an
         alphabet is unbounded. It is a conditional theorem, and no recovery class here rests on it.

       A law over outcomes, a finite observational description, or a comparison across settings needs one
       patch for every branch: under FS-all, with a bound, or from finite reads on every run, under Lemma K's
       other hypotheses, without one. A statement about one run and the runs that agree with it could use the
       per-run form. §14.3 (Table 4) says which each such row needs; no row's class rests on the per-run form
       or on Lemma K.
    2. **Probability premise (EF-1 r6 group B: P1, and P2 with a policy).** A normalized starting law (P1;
       this audit's L9) supplies probabilities on that description: the observation law on `[0, n]` is the
       pushforward of the patch marginal. With a policy it is the joint law of the patch data and the policy
       information that is pushed forward (P2), since equal marginals of the two taken separately do not
       suffice. The probability premise is not needed to establish finiteness: every statement of group A
       holds with no probability.
    3. **Further distributional properties (EF-1 r6 group C, D1–D8).** None is used or supplied by the lemma,
       and each needs its own justification wherever a proof uses it: equal patch marginals in two carriers,
       or a product form across the patch boundary (D1; L4); a uniform product prior (D2); invariance of the
       prior under the dynamics (D3); independence of the visible initial state from the hidden data,
       `P_0 ⊗ μ_H` (D4); stationarity (D5); measurement independence (D6; this audit's MI), which on `main`
       is ledger item (xiv), a separate posit; independence of the policy information from the patch data
       (D7); a prior selected among invariant measures (D8).
  - *Standing of the premises on `main`* (EF-1 r6 §4.0, re-read here). F1 is ledger item (viii), a posit
    (Main:724). F2 is Lemma 3's clause (Main:54). F3 is a clause of item (xiii) on the selected model, whose
    listed role would widen, and a hypothesis of GR:132's infinite case; off the selected model it is not on
    `main` as worded (item (ix) "has content only in family form", Main:724). F5 is in Main:362 ("each $S_i$
    finite") and item (xiii). F4 is used on `main` for the spatial results and is not a separately stated
    premise (Lemma 1, Main:46, gives `|C_V| < ∞` only). F6 is on `main` for one setting step (Main:366–374)
    and not for adaptive spatial policies. F7 is not a separately stated premise (on `main` it follows from
    the finite site set of Main:362). P1 on a carrier of undetermined cardinality appears only as a hypothesis
    (GR:132; Sub:92: "Infinite extensions require specified normalized measures or states"); under A1 the
    counting measure supplies it. P2 is not on `main`. EF-1 r6 flags F3 off the selected model, F4, F6 for
    adaptive policies, F7, P1 for an infinite carrier, and P2; EF-1 r6 flags F5 off the selected model as well: it has no source
    on `main` off the selected model other than Main:362's setup, where it comes with the finite site set
    (the review of EF-1 r4, finding 6). So the lemma is derived exactly as far as those
    premises are available, which is an owner matter for the flagged ones (Q8, Q6(d), Q11).
  - *"Candidate replacement"* describes only the role the lemma might play in a proof that now uses A1.
    It is not a description of the lemma's own status, and it carries no recovery credit (adopted direction,
    c.6896940222). A recovery candidate is not a recovered result (rule; source in Standing).
  - *What the description inherits* (EF-1 r6 §P [IR], with the correction of the review of EF-1 r4, finding
    1): determinism, the causal cone, and the observation law on the window with everything computed from it.
    It does not inherit automatically, as properties of its own, bijectivity or reversibility (the patch has
    no self-map of its own), an invariant measure or a selection among invariant measures, recurrence
    structure, absolute hidden cardinalities, conserved energy shells, spectral statements, typicality of
    individual states, or measurement independence. **That these are not inherited automatically does not
    mean that no suitable finite closed model exists** (adopted direction, c.6897859755). Whether a chosen closure of the
    description could supply what a given proof needs is a separate question, set out under "Two different
    statements" below and answered row by row, as far as this audit's traces allow, in §14.3 (Table 5). EF-1 r6 keeps
    four finite objects apart (its §P.1): (α) the patch description; (β) a finite realization constructed
    from the observation law and faithful on `[0, n]` (Main:516–520); (γ) a finite torus of the native class;
    (δ) an all-horizon model, where one exists. A property of a finite whole system, whether (β), (γ) or
    nature under A1, does not pass to (α) without a proof.
  - *Two different statements about measures* (adopted direction, c.6897455387; EF-1 r6 §P.3, §P.4).
    - **(M-full).** Within the locality class of `main` (each site reads finitely many sites and is read by
      finitely many; item (xiii), Main:724), a bijection of the full system preserves its uniform product
      measure, given a finite alphabet at every site. This is a statement about the whole system. Its proof
      was proposed by the review of EF-1 r3, re-derived in EF-1 r4 and **checked by the review of EF-1 r4**,
      under those hypotheses. For the second-order form alone, EF-1 r6 N3.2 proves the same conclusion by a
      separate argument, which the review of EF-1 r2 checked and which needs only the first locality clause.
      The review of EF-1 r4 notes (finding 8) that what (M-full) adds to N3.2 is the general class of
      bijections with both clauses, which `main` does not select as nature's dynamics. Outside the class the
      conclusion can fail: example B1, a bijection with finite reading sets in which some site is read by
      infinitely many sites, does not preserve the measure.
    - **A measure on the description.** EF-1 r6 withdraws r4's (M-desc) and both of its headline sentences. It states two things apart: the description as defined, which has no autonomous dynamics and for which an invariant measure is not defined (M-desc-own); and a chosen closure on the patch (M-desc-some).
      - *A map of the description's own.* The description, with no added datum, has a self-map with an
        invariant probability. This is not defined, because the description's own maps go between different
        sets, except when the cone has stopped growing, which is an F-one hypothesis. So **the property is
        not inherited automatically**: (M-full) gives the description no bijection of its own.
      - *A chosen closure.* Some bijection of the patch data reproduces the record on `[0, n]` and preserves
        the uniform patch measure. Lemma C (EF-1 r6 §P.4 (b)) says that one exists exactly when the record law from
        the uniform patch measure is the same on `[1, n]` as on `[0, n−1]`, hence whenever the uniform product
        measure is invariant for the full system (Corollary C1). Lemma C′ says that for a rule of second-order form
        every fixed-boundary closure is such a bijection, and that for the shift, a first-order rule, that
        closure is not one. **Lemma C (both directions), Corollary C1 and Lemma C′ were checked by the recheck of EF-1 r5, under their stated hypotheses; they are paper proofs and earn no recovery credit.** Lemma C concerns bijections of the patch data under the uniform patch measure; a failure of its condition says nothing against a finite closed model on another carrier, which exists for every finite-horizon law (Main:516–520). Whether a suitable finite closed model exists
        is therefore a separate question that is open, not a settled negative. A closure is a choice: it
        agrees with nature on the window only, and its order, cycles, eventual image and spectrum are its own.
    - **Rule for rows** (adopted direction, c.6897859755). A row whose proof uses a self-map of a finite carrier, or a
      measure invariant under one, does not get it from (M-full) automatically. Whether a chosen,
      window-valid closure could supply it depends on whether the proof's requirements are confined to the
      observation window. Where they are, a closure could suffice; that is to be determined, and it earns no
      recovery credit yet. Where the proof needs something outside the window that is nature's own (the order
      or return of the bijection, its eventual image, its spectrum, a conserved shell, the total carrier), a
      closure cannot supply it. §14.3 (Table 5) gives the entry for each such row, from this audit's trace of
      its proof. A row whose proof needs only a property of the record law on the window (double
      stochasticity of the `k`-step matrices for `k ≤ n`; stationarity) would have it from full-system
      invariance together with a uniform product prior, which is a further distributional property (D2).
      **No row is classed FIRM, and no row changes recovery class, on the strength of (M-full), of N3.2 or
      of the closure result.**
  - **Condition for settings, inputs and policies (adopted direction, c.6896771264 and c.6896890693; EF-1 r6 N1.5).** A
    comparison of two runs holds the settings the same, or uses the same adaptive policy and includes the
    information that policy uses: one shared protocol (F6). The policy may use the record and its present
    read; EF-1 r6 also lets it use its earlier reads (the memory clause, checked by the review of EF-1 r4). The matched data are
    those on the enlarged patch `E_n` of Lemma PM-I: at every step it contains the observer's sites, the sites
    the policy reads and the declared supports of the permitted interventions; for laws, the joint law of the
    patch data and the policy's information (P2). A support of an intervention is a set of sites outside
    which it changes nothing and inside which its action depends only on the data there, in every state.
    Matching the initial data on `U_n` alone need not give matching observations under different
    interventions (Lemma PM-I (d)). Where a statement compares runs that differ in one intervention (the
    cone's intervention form, Main:362), everything else is held the same and the conclusion holds because
    that intervention's region does not meet the readout's backward set. Every use of F-each below carries
    this condition.
- **F-one.** There exists one finite description valid for every horizon. Status: not established. What
  is on `main` or follows directly: for an autonomous deterministic finite system the record is eventually
  periodic, a transient allowed (periodic for a bijection, Main:638's forward direction); with continuing
  external inputs or settings a finite system can give nonperiodic output. EF-1 r6 (N2.1) proves two
  sufficient conditions, neither known to hold for nature and neither shown necessary: a finite complete
  relevant state, controller or policy memory included, whose evolution is determined by that state (one
  autonomous finite model); or finitely many influencing sites with inputs kept external (one finite model
  with inputs, which carries no periodicity). The geometric neighbourhood `U_n` is distinguished from the
  sites that genuinely influence the observations (EF-1 r6's `J_n ⊆ U_n`). EF-1 r6 adds a necessity statement (Proposition N, checked by the review of EF-1 r4): with finite alphabets, a finite influence set is necessary for one finite autonomous model that reproduces the record from every initial configuration. EF-1 r6 (N2.1): it is not necessary for a law that misses some finite pattern, and it is necessary for a law that gives positive probability to every finite pattern (the one-law refinement, checked by the recheck of EF-1 r5 under its stated hypotheses). Neither is used here. The all-time conclusion drawn
  here is only that **the fixed-horizon argument does not, by itself, supply one finite model valid for
  every horizon**, which is narrower than proving such a model impossible.
- **Use in this audit.** For each row whose candidate route uses EF-1, §14.3 states the properties the
  row's proof on `main` uses, whether the fixed-horizon description preserves them, which form the row
  needs, and what it needs from each of the three ingredients above. A row that needs F-one is not
  recoverable by the fixed-horizon lemma. A row that needs only F-each is a **candidate, not recovered
  until its proof is checked**. **No row has recovery credit.** A recovery candidate is not a recovered result. A finite description for a chosen horizon
  supplies no recurrence guarantee within that horizon.

**The claim-to-conditions key (adopted direction, c.6897946443).** "The useful simplification is to stop treating every
condition as a requirement for every result". The adopted table, quoted exactly in its two columns; the
third and fourth columns are this audit's labels and are not part of the adopted table.

| Claim being made | Conditions it needs | Key | In this audit's and EF-1 r6's labels |
|---|---|---|---|
| Finite description for a fixed observation window | The dependency and finite-state hypotheses of the checked patch/intervention lemmas | K1 | F-each's finiteness premises: F1–F5 (L1, L2, L8), and with settings or policies F6 and F7 (FS-all, or finite reads on every run under Lemma K's other hypotheses). The dependency statement alone needs no finite alphabet |
| Probabilities for that description | A suitable starting probability law | K2 | P1 (L9); with a policy, P2 |
| Uniformity, invariance or measurement independence | Each property's own justification | K3 | D1–D8, each named where it is used: equal patch marginals (D1), a uniform product prior (D2), invariance (D3; for the full system N3.2 and (M-full)), independence of visible and hidden data (D4), measurement independence (D6; MI), a selected prior (D8) |
| A finite closed model reproducing the window | The closure theorem's conditions, once independently checked | K4 | (i) a closure on the patch data: Lemma C, Corollary C1 and Lemma C′ (EF-1 r6 §P.4 (b)), checked under their stated hypotheses, with no recovery credit; (ii) a finite realization constructed on another carrier from the window law: Main:516–520, on `main`, A1-free; §14.3, Table 5 |
| Recovery of a particular A1 result | Only the properties that result's proof actually uses | K5 | §14.3's traces, row by row |
| One finite model valid for all time | A separate all-horizon argument | K6 | F-one; not established |

Population of this table: the six claims of the adopted table (keys K1–K6).

§12.3 uses the key for each of the 57 rows: it names only the claims that the row's content needs, states
whether the row has an observable conclusion about a finite experiment and, where it has, a candidate target
for a direct proof of that conclusion, and gives the row's concession category. §12.4 lists what is conceded.
Two shortcuts are barred (adopted direction, c.6897946443): "Adopting a new assumption solely because it rescues a desired
result." and "Calling a conditional recovery an unconditional consequence of OI." §14.4 checks every NEW row
and every recommendation of §19 against the first, and every FIRM and CONTINGENT statement against the
second. Nothing in §12.3 drops a condition: the adopted rule (c.6897946443) is that "The exact conditions we can remove must
come from the reviewed proof traces, not from the summaries alone", and this audit's traces are unreviewed.

**Categories.** Short codes are used in tables.

- **CV — RECAST-CONSTRAINING.** After rewording, the statement is about nature's visible sector on
  accessible horizons, its proof on `main` uses no total finiteness, and it establishes a constraint on
  some finite-horizon visible law (some law on some accessible horizon is incompatible with it). **No row
  has been shown to belong to this category: at the default answers, and under either answer to Q2, no
  result on `main` establishes a justified constraint on a finite-horizon visible law.** That is what the
  audit found; it is not a proof that none could, since failure to recover is not disproof. The adopted wording for it (c.6896771264): "The headline remains provisional: none of the 56 results currently
  establishes a justified observational constraint; that does not mean none can be recovered." The rows that
  could establish such a constraint, if proved, are recoveries (§14, "lands as") and the A1-test
  conditionals of §11, which would establish a constraint only under the hypothesis that nature's total
  carrier is finite.
- **RD — RECAST-DIAGNOSTIC.** A theorem relating functions of the visible law, true of every law: it
  certifies a property (here P-indivisibility) from a measurement. As stated, it excludes no law; its
  witness is empirical.
- **RU — RECAST-REPRESENTABILITY.** A statement that holds for every finite-horizon law: representability,
  invariance or identifiability ("representability alone does not distinguish", Main:18). As stated, it
  excludes no law.
- **RW — RECAST-WORDING.** A framing sentence, not a theorem.
- **TD — TOTAL-DYNAMICS.** A requirement on, or statement about, nature's total map that assumes no
  cardinality and is not a statement about the visible law. It is not an A1 consumer; whether the owner's
  condition reaches it is Q11.
- **RM — RECAST-MATHEMATICAL.** True of every finite model of the stated class (every finite reversible
  realization, every finite-torus substratum, every finite carrier with the monomial class, every finite
  isolated subsystem), but its subject is a property of the model that the visible law does not fix
  (Main:520), or a model class nature is not known to belong to. Its physical reading is removed under
  either answer to Q2 (owner decision 6896070253, in the words of the proposal the owner accepted there: "stay as mathematics about finite models, with no claim
  that nature is one"). Where its statement is placed is Q2. **No answer to Q2 deletes valid mathematics
  from `main`**: under Q2(b) as reformulated here, a statement whose only proof on `main` is manuscript
  text keeps that proof, in its paper or at a named destination (§12.1, §12.2, Q2).
- **RC — RECOVER.** A visible-sector form exists whose proof is not on `main`; the proof is sketched and
  numbered (§14), with the premises it would add, if any, the recovery class (FIRM, CONTINGENT or NEW, below), the
  finiteness form it needs if its route uses EF-1, and the category the recovered statement would land in.
- **RX — REMOVE.** No visible-sector form was found. The content is about the total or hidden sector of
  nature (global recurrence, global bijectivity, a measure on nature's hidden space, nature being one
  fixed finite system). A recovery attempt is recorded first ("Theorem recovery before concession");
  failure to recover is not disproof, the unrefuted stronger statement is classed open, and the removed
  text stays in Git history (§A.27). Rows marked **A1-test** have a consequence at accessible times that
  A1 gives and the visible sector alone does not (§11); the owner may keep them as explicitly conditional
  statements (Q9).
- **OP — OWNER-PENDING.** The treatment is an owner decision between named options, each with its
  consequences stated.

**Landing label NC — COMPLETION-CLASS NO-GO (r3 review B6).** Used only in "lands as" for RC rows: a
theorem that excludes a class of completions (hidden-variable models) of any cardinality. It constrains
completions, not nature's visible law, and it does not rest on nature belonging to a finite model class,
so it is not RM. AM-7.2 and AM-7.3 land NC.

**Primary reason a row loses observational force (adopted direction, c.6896252651; r3 review item (1)).** Rule,
applied in order: **(i) A1 unsupported** when the link from the result, as stated on `main`, to nature or
to an observation runs through total finiteness; otherwise **(iii) whole-system only** when its subject
is nature's total or hidden sector; otherwise **(ii) missing link** when it holds without A1 but no
derivation on `main` turns it into a constraint on a visible accessible-time quantity. For RC rows the
reason is given for the statement now on `main`. Counts: (i) 48, (ii) 6, (iii) 3 (§12; population 57).

**Recovery classes: three separate counts.** Population: the 19 rows that have a recovery or owner
route (the 16 RC rows and the 3 OP rows). A class says what a candidate proof would need; it records no
recovery, and a row counted in one class is counted in no other.
- **FIRM.** The rule, in the words of adopted direction c.6898395533: “"Firm" needs one consistent rule: all premises required by the proposed route are already available. It still means neither that the route works nor that recovery is proved. Keep replacement separate.” Earlier (adopted direction, c.6896890693): “"Firm" means the required premises are already available, not that recovery has been proved. This applies to the two firm fixed-horizon candidates too.” *Applied here:* a premise is available when it is on `main`, with file and line, as a theorem, a kernel statement, a posit in force or a hypothesis already named in the statement being recovered, and does not depend on an undecided reading. A row whose route requires any premise not on `main`, or one that depends on an undecided reading, is not FIRM. A row is classed for the claim as it lands: what asserting it of nature needs, or, for a row that lands NC or RM, what the statement about the class of models needs. A hypothesis named in a statement on `main` is available for the conditional theorem; it is available for a claim about nature only if `main` also has it of nature (AM-4.4: the measure is named at SM:334 and is not on `main` as nature's). §14.1 lists the premises of each FIRM row and where each is on `main`.
- **CONTINGENT.** The candidate proof needs a premise whose availability depends on an undecided reading
  of a text on `main`. Also classed here: a row whose restated statement must carry a hypothesis that is not worded on `main` and asserts nothing of nature, where the undecided matter is whether such a hypothesis counts as a premise under the rule for FIRM (AM-7.2, AM-7.3; disputed, §14.1). For these two rows the decision is the owner's on the rule itself; no option of Q8 as worded for nature's carrier decides it. §14.1 gives, for each such row, the exact reading, its textual basis quoted with
  file and line, who decides, and the disposition if the reading is accepted and if it is rejected. An
  undecided reading is not counted as an available premise.
- **NEW.** The candidate proof needs a named assumption that no text on `main` states of nature's
  carrier. It is judged under §A.29: the decision that would adopt it states in advance the results it
  preserves and delivers at least one independent prediction or postdiction.
- **Replacement candidate (not a recovery class).** The row's original statement is not recoverable in
  any of the three senses, and what is offered is a different statement in its place. It is not counted
  as a recovery of the original result (adopted direction, c.6896890693, on N-3).
- A row with parts is classed by the route for the statement as it stands on `main`. A part that offers a different statement is a replacement part, reported apart and counted in no class (AM-31, part (3)).
- No class rests on a statement of EF-1 r6: not on (M-full), the per-run form, Lemma K, the memory clause, the necessity statement or its one-law refinement, not on Lemma C, Corollary C1 or Lemma C′ (each checked, under its stated hypotheses), and not on its retraced §4.2. No class changes on the closure result (adopted direction, c.6897859755): whether a closure preserves everything a particular audited result needs is still unproved.

Counts under the one rule (population: the 19 recovery rows; AM-5b is RM and is not among them): **FIRM 4** (AM-2.1, AM-5, AM-31 for the theorem as stated, N-6), **CONTINGENT 5** (AM-7.1, AM-7.2, AM-7.3, AM-23.2, AM-33.1), **NEW 9** (AM-4.4, AM-8, AM-11, AM-21.1, AM-21.2, AM-22, AM-24, AM-30, AM-36), **replacement candidate 1** (N-3); 4 + 5 + 9 + 1 = 19. r6 counted 6, 3, 9, 1 by a rule its review found applied in two ways (F5); the review of r6 gives a range of FIRM 5 to 8 and adjudicates 7, 3, 8, 1. The rows that differ, with both positions, are in §14.1 and §20. Changed after review; unreviewed.

**Does any row, as now supported on `main`, establish a justified constraint on a visible law at
accessible times?** No. At the default answers no surviving row establishes one: the former
"constraining" rows are diagnostics (AM-1.2, AM-1.3a), a representability statement (AM-20.1), a
total-dynamics requirement (AM-3.1) and a finite-model result (AM-33.2). The rows that could establish
such a constraint, if proved, are recoveries that need premises: AM-30 (P6: reciprocity
`T_ij = T_{θj,θi}`; Q5, Q6) and AM-22 (P7: the thermal rate ratio; Q1(b-mode), Q5, Q6), and [IR] AM-4.4
(P13, Q6); AM-7.1 only together with a further link not on `main`, L10 (the identification of the
observer's intervention and readout regions with coupling-graph regions and their graph distance: item
(viii) is site factorization, "the configuration space is identified with a product of local
configuration spaces over a set of sites", Main:724, and supplies no map from apparatus to graph
regions; which propagation sets the physical light cone "is not derived here", Main:414); AM-31's per-horizon
cone bound (its part (3), P9) only together with L10 as well, and only where it is tighter than the
bound from the visible record itself, `min(t, n−t)·log₂|C_V|` (not checked); and AM-36 through P7. The A1-test candidates of §11 would establish a constraint only as conditionals on A1
(Q9).

**Headline rule (review F10 of r2; B6 of r3).**
- **(H1) Abstract, theorem-statement and opening sites** (paper abstracts and openings, Main:80's
  Theorem statement, the book's preface, introduction and chapter "central result" sentences) state no
  RM content and no RX content under either answer to Q2. TD and NC content is not barred by H1. Where
  such a site states a limitation (a negative), the limitation is replaced by the statement of what is
  open for nature, so that removing a negative never strengthens the headline. Main:20's cone and Bell
  sentences are kept once AM-7.1 and AM-7.2 are recovered (landing TD and NC), and leave the abstract
  otherwise.
- **(H2) Summary, status-table and section-scoping sites** (Main:600, :731, :733 and the §3.4 scoping
  remarks) follow Q2: kept as model-class statements under Q2(a); under Q2(b) the summary entry cites only
  statements that remain in Main (body or appendix), or is removed (review C3; §12.2).
- **(H3) A clause whose physical reading inherits an RX row through a premise the owner may adopt**
  follows that owner question. The one such clause found is (C2-structural)'s "holds by reversibility in
  every bijective realization" (Main:18, Main:80 item (2)), whose reading for nature's hidden sector needs
  hidden-sector injectivity (AM-3.2, Q5).

**Main independence.** A recast or recovery in Main may use only Main's own support (Main:60, :354,
§3.3's cone, §3.4's theorems, and kernel modules whose dependencies are Main-level). A recovery that needs
GR §3.2's boundary-only lemma, GR:132 or H-BD is downstream science and belongs in the upstream-most
downstream paper that uses it (Code Review Rules; the validity review's "Use of GR:132" reaches the same
conclusion). Main:700 records that a boundary-entropy bound on `C_B` "would rest on the holographic input
that this layer excludes", so finiteness of the boundary layer is not available inside Main either. EF-1 r6's
Lemma PM uses Main-level inputs only: item (viii), finite reading sets (item (xiii) on the selected model), finite
alphabets, a finite visible site set, a normalized starting law for its law form only, and the cone lemma, whose
proof term uses only `DependsOnlyOn`, `ball` and iteration (EF-1 r6 N1.6; family 8 already has a Main anchor,
`quasiState_unique`). Main:588 is not an input (EF-1 r6 N1.6). Lemma PM's clauses (a) and (b) serve Main
roots (§3.3's cone and Bell ceiling); its comparison clause (c) between carriers serves no named Main root
and belongs downstream with GR:112 and GR:132 (EF-1 r6 N1.6). Of Lemma PM-I, only the form with one setting
step, the settings the same in the runs compared, has a Main consumer (the Bell ceiling); the multi-step
adaptive form has none, and either form would bring FS-all with it as a stated premise (EF-1 r6 N1.6). Notation: Main:362's `V` is the whole site set, so "Finiteness of
`V`" there is global finiteness (EF-1 r6 N1.2); this audit's `V`, as in EF-1, is the visible region.

## 1. Response to the review of r4, and the directions applied

Each change was checked first-hand at `bf89ba13` before it was applied. "Agree" means confirmed and
applied. Where r5 goes further than the review, or differs from it, the row says so and §20 carries both
positions. The table is r5's response to the review of r4. Its citations of EF-1's content are to the current pin, EF-1 r6;
row C9 gives the history of the pin. Classes and counts in it are the current ones.

| Finding | Check made at `main` | Response and change |
|---|---|---|
| C1 (AM-34 is a paper proof) | Sub:331 (Proposition 24.4, "a permutation of a nonempty finite set $\Omega$"); proof Sub:333–342; Sub:344 ("one fixed finite reversible carrier"); Sub:346 ("neither new proposition is claimed Lean-proved"); the derivation record `verification/audits/manuscript/multitime-predictive-recovery-20261028/` is on `main`; census 61 and 62 are the Lemma 24.1 and 24.1A rounds, kernel-only, with no manuscript entry; "Lemma 24.1" does not occur in `papers/Substratum.md`; `FullFutureMemory.lean` (census 112) defines a future-trace code and proves capacity bounds, not the quotient's uniqueness or rank. | Agree. AM-34 is Proposition 24.4 with its paper proof; census 61 and 62 are not its witnesses. Under Q2(b) it stays in Substratum §4.1 with its proof (§5, §12.1, §12.2, §13, Q2). |
| C2 (Main:274–278 does not consume A1) | Main:274 ("for some finite $\mathcal{C}_H$"), Main:276 (the hidden space is built from the Birkhoff–von Neumann decomposition), Main:278, Main:522 ("is the special case and is unchanged"), Main:115 (the denominator `∣C_H∣` of `T`), Main:280 (`ρ_H = I_m/m`). | Applied as adopted direction c.6896890693 asks: the reading is kept marked **[reviewer reading, unresolved]** at every site, and both counts are given. r5's own check [IR] finds the lemma's hidden space constructed, as the review says; its sentence "a uniform-prior bijection marginal preserves the uniform distribution and is therefore doubly stochastic" (Main:274) is true of the finite hidden spaces the lemma constructs and is not a statement about nature's carrier (on an infinite product it is a separate statement about the full system: EF-1 r6 N3.2 proves it for the second-order form; (M-full), checked by the review of EF-1 r4, for the locality class of `main` with finite alphabets; B1 shows it failing when some site is read by infinitely many sites). §20, D3. |
| C3 (Q2(b) names no destination) | Main:157 ("(Scope, above)"), Main:338 item (2), Main:496, Main:558, Main:562, Main:600 ("Per (3)"), Main:731, Main:733; SM:24 and GR:22 ("the reader is directed to [Main] for the proof"); Struct:1140, :1255; Main's citations of companions (Main:20 [Substratum §3.3]; Main:216, :412, :414, :500, :724, :758 [SM §…]; Main:284 [Structure]; none of GR); Main has no appendix at `bf89ba13`. | Agree, and done row by row: §12.2 names a destination for every relocated row and for every relocating landing, and checks Main independence for each. Result: five of the seven rows stay in the paper they are in; AM-9.1 has no safe destination outside Main; AM-1.1 has one safe destination (a new appendix of Main) and one that is safe only with four Main sentences and four companion pointers rewritten in the same change. Q2(b) is stated as not decision-ready until the destinations are agreed (Q2). §8's H2 rows restated. |
| C4 (AM-31: the reading, its basis, the row's parts) | Main:724 item (iv) (a selection: "the measure selection is a maximal-entropy principle"); GR:132 ("given a normalized product prior on it", the hypothesis of a conditional); Sub:262 ("an infinite extension requires its own normalized measure or trace-class state and a well-defined evolution, and is not established by finite uniform counting"); SM:1376 (the C3 clause is `I* ≤ log₂∣C_H∣`), SM:1378 (C1, no finiteness), SM:1382 (`∣H∣ = N − ∣V∣ ≥ 2N/3`); Main:512 (`I* = sup_t …`, with `m ≥ 2^{I*}`); Main:608 (c) (the one-step `M_t`); `fullFutureIstar_le` (`FullFutureMemory.lean:104`, census 112, kernel-only, `[Fintype H]`). | Agree on every point of evidence: no product prior is needed; the normalized law is not a reading of item (iv); the row has three parts. One refinement [IR]: the `I*` form of the C3 clause is Main:512's corollary (kernel-only witness `fullFutureIstar_le`), of which Main:608 (c) is the one-step form. **Difference in the label.** The review counts part (3) as contingent on Q6(d). Under r5's definitions a CONTINGENT row needs an undecided reading of a text, and the review itself shows there is none ("No text on `main` states it"); part (3) therefore needs a named assumption, L9. It is a replacement part, in no class, and the row is **FIRM** for the theorem as stated, parts (1) and (2) (the review of r6, F7; r5 and r6 classed the whole row NEW by part (3)). r5 also notes [IR] that part (3) bounds only a horizon-`n` truncation, so it replaces the content of the C3 clause for an infinite hidden sector and does not recover the horizon-free bound. §5, §14.1, §20 D1. |
| C5 (three counts) | r4 §0, §14.1, §20. | Agree. Three separate counts with definitions (§0), a contingency table (§14.1) and no folding. The counts are FIRM 4, CONTINGENT 5, NEW 9, replacement candidate 1, under the one rule of §0 (§14.1); they differ from the review of r4's 6, 5 and 8 in five rows (§14.1). |
| C6 (the seven F-each rows are a subset; four assignments are r4's own) | r4 §14.1, §14.3; EF-1 r6 §4.2 (its result classes are the finite-horizon equivalence, the hidden-memory theorem, the cone, the Bell ceiling, the baseline `T`, the counting measure, bijectivity, recurrence in its counting form, readback with overlap and return, §3.2's CP-indivisibility theorem, setup and one-step coherence results, Main:638, corner occupancy, the deep-sector gauge, energy shells, Theorem 23, §4.6, the A1-test candidates and Main:638's open question (a); at EF-1 r6 also the §3.4 obstructions for a fixed finite realization, with the coherence class given as Main:292–324: no entry for hypercomputation, SM Theorem 22, GR's universality claim or the universality-class property). | Agree. §14.1 carries the cross-tabulation by row id with the population of every count; §14.3 has a column "Form assigned by" (EF-1 r6 §4.2 for the cone and the Bell ceiling; this audit [IR] for AM-7.3, AM-23.2, AM-31, AM-36 and N-3). |
| C7 (N-3 is a replacement) | `ch09-universality.md:106` ("load-bearing for the recurrence route specifically … requires finiteness for the exact recurrence of a finite bijection"). | Agree, and labelled as adopted direction c.6896890693 asks: N-3 is a **replacement candidate**, outside the three recovery counts and not an F-each recovery (§7, §12, §14.1, §14.3, Q3). |
| C8 (settings condition) | Main:362 ("an intervention that reads and writes only region $A$ cannot alter, $k$ updates later, any component outside $B_{G_\varphi}(A,k)$": the runs compared differ in the intervention); `readout_unaffected_outside_ball` (`RegionTower.lean:304`); EF-1 r6 N1.5 (Lemma PM-I, the patch `E_n`, the hypothesis FS-all, the per-run form) and N3.6 (`Ω_n` on `W_A ∪ W_B ∪ A ∪ B`). | Agree on all four points. §0's condition restated with the enlarged patch; AM-7.1's intervention form corrected; AM-7.2 and P4 use the pre-setting data on `W_A ∪ W_B ∪ A ∪ B` with `A`, `B`, `R_A`, `R_B` finite as a premise; AM-9 and §11 count the data on the enlarged patch. EF-1 r3 replaced r2's Lemma PM-I (r2's patch was false in general), and the review of EF-1 r3 re-derived r3's form and found it correct as stated, with its finite-support hypothesis read over every branch. This audit uses EF-1 r6's statement of that all-branch form, which is r4's; r4's additions to it (the memory clause, the per-run form, Lemma K) were checked by the review of EF-1 r4; no class rests on them. |
| C9 (pin EF-1) | `EF-1-r6.md`, sha256 `34f3ec8f…fe6d9f`, verified for r8. | Agree, at r6 (the review asked for r2; r5 pinned r3; r6 pinned r4; r7 and r8 pin r6): Standing pins r6 and states that every use of it is provisional; the labels are r4's, which r6 keeps; §19 carries the concordance with EF-1 r6's eleven questions. |
| C10 (the #1169 records) | #1169 comments 6894872312, 6895032895, 6896070253, 6896252651, 6896496410, 6896771264, 6896890693, 6896940222, 6897254631, 6897455387, 6897859755 and 6897946443 read on GitHub. | Agree. All twelve are quoted in Standing with author and time. The settings direction and the four statements the review marked as relayed are recorded (6896771264) and are cited to the record. The later directions (the uniform measure; finite support; status), which r5 could cite only as relayed, are recorded in 6897455387 and are quoted from it. The sentence used as a rule, which was in no comment when r6 was begun, is recorded in 6897859755. |
| C11 (order of the questions) | r4's dependency list. | Agree: Q7 and Q10 move before Q4 (§19). |
| C12 (§17 of r4) | r4 §17. | Agree. The plain-language summary (§18) accounts for all 57 rows (18 + 10 + 10 + 19; with AM-5b, added after the review of r6), names the owner decision and Q11, and reports the classes without folding. |
| C13.1 (AM-12 wording) | Sub:262, :268. | Agree: "as stated, they exclude no law". |
| C13.2 (family 34) | The registry holds four (file, string) entries for family 34, and `pIndivisible_of_rooted_identity_return_of_overlap` occurs at Main:137 and Main:143. | Agree: no registry action for family 34 while Main:143 stays (AM-1, §10, Q13). |
| C13.3 (the cone needs L1 only) | `iterate_dependsOnlyOn_ball` has no `Fintype Q`. | Agree: L2 is needed for the description to be finite, not for the dependency (AM-7.1, §14). |
| C13.4 (N-5) | `rootedMap_periodic` (`RootedClassification.lean:135`); `ch18-beyond.md:74`. | Agree: the kernel holds the periodicity; the step to an unbounded sum is a one-line paper inference (§12.1 row 55). |
| C13.5 (Q12) | r4 §14.3's gate tally. | Agree: P4 for a measurable `Ω` is in the first tranche, with the proviso of AM-7.2 that hypothesis (iii) is read with a coupling graph in the dependency sense. |
| C13.6 (Q11's reason) | AM-7.2's landing NC. | Agree: the Bell ceiling is dropped from the list of what Q11(b) removes. |
| C13.7 (Q15) | Main:638, Main:731; EF-1 r6 N2.5, N2.9 (both directions written out; existence, not joining; no inputs; mirrors at Main:731 and Intro:178; census anchor; guard `R7-RCL`). | Agree, with the fuller inventory of EF-1 r3, which r6 keeps. |
| Section A (the three counts and how they overlap) | r4 §12, §14. | Applied in §14.1, with the classes of the one rule of §0. |
| Section B (the contingent rows) | Each quoted line re-read: Main:362, Main:724 (ix), (xiii), `ch14-quantum-computing.md:90`, GR:791, `a2_every_substratum` (`SubstratumInterfaceAudit.lean:106`), `ch09-universality.md:106`. | Applied in §14.1 for the three rows that are CONTINGENT on a reading the review of r4 examined (AM-7.1, AM-23.2, AM-33.1); AM-7.2 and AM-7.3, CONTINGENT since the review of r6 through P4's hypotheses, are in the same subsection; AM-31 and N-3 are shown there with the review's position beside this audit's. The gate of row 31 gains "(Q11 for the reading)". |
| Section C (status of Q2(b); remaining disagreements) | — | Q2(b) is presented as an option only, with no recommendation to adopt it (Q2). §20 lists every remaining disagreement between this audit, the reviews and EF-1, with both positions. |

Population of this table: 22 lines, the changes C1–C12 and C13.1–C13.7 of the review of r4 and its sections A, B and C (12 + 7 + 3).

**Directions applied in r5** (the owner's own words and the adopted directions; each quoted in Standing).

| Direction | Where applied |
|---|---|
| "Firm" means premises available, not recovery proved (6896890693) | §0 definitions; §14.1; every FIRM row says "recovery not proved" |
| N-3 is a replacement candidate, not a recovery (6896890693) | §7, §12, §14.1, §14.3, Q3 |
| Label the 17-row subset and connect it to the 56-row disposition; preserve AM-34's paper proof; keep the A1-free reading of Main:274–278 attributed (6896890693) | §12.1 (one table of 57 rows: the 56 with the adopted 17 (c.6896890693) marked, and AM-5b, marked as the 18th RM row); AM-34; AM-4 |
| Name relocation destinations before Q2(b) is decision-ready (6896890693) | §12.2; Q2 |
| A finite description need not preserve what a downstream proof uses; no recovery credit until each theorem's requirements are checked (6896940222) | §0; §14.3 (properties each proof uses, with file and line, against EF-1 r6 §P) |
| Dependency coverage is not measurement independence (6896890693) | AM-7.2, AM-7.3; §14.2 (MI); §14.3 |
| Finite support of interventions and policies (6896890693) | §0; §14.2 (FS); AM-7.2, AM-9, AM-23.2 |
| Headline wording (6896771264) | Header; §0 under CV; §18 |
| Overlap of the counts; AM-31's reading, basis and disposition (6896771264) | §14.1 |
| Per-horizon finiteness is a derived lemma; "candidate replacement" names only its possible role; the finiteness premises, the probability premise and further distributional properties are kept apart (6897254631) | §0; §14.2; §14.3; every EF-1 row |
| Full-system measure preservation is not an invariant measure on the description; the reviewer's measure-preservation proof supports no classification until checked (6897455387) | §0 ((M-full), (M-desc)); §14.3 (Table 3); no class rests on it |
| Finite support per run is not one finite patch for every branch (6897455387) | §0; §14.2 (FS); §14.3 (Table 4) |
| Missing proof requirements are more than a minor correction (6897455387): the traces are this audit's own, and are compared with EF-1's retraced §4.2 (as at r4) and with its second table (r6) | Standing; §14.3; §20 (T1–T21) |
| Bring the 15 questions after both reviews, with disagreements visible; nothing adopted (6896771264) | §20, §19 |
| A recovery candidate is not a recovered result (adopted direction, c.6897859755; used as a rule) | Standing; §0; §14.3; §18 |
| Proof status in three tiers: checked, still unchecked, still unproved (6897859755) | Standing; §0; §14.1; §16; §18 |
| "Failure of automatic inheritance does not imply that no suitable finite closed model exists": wording withdrawn or restated (6897859755) | §0; §14.3 (Tables 3 and 5); §20 (D22); §18 |
| The closure result earns no recovery credit yet and is not disqualified either; each row that needs a measure or bijectivity gets a window-confinement entry (6897859755) | §14.3 (Table 5); no class changes |
| Lemma K is summarized as "finite reads on every run, under the lemma's other hypotheses" (6897859755) | §0; §14.2 (FS); §14.3 (Table 4); AM-23.2; §18 |
| The assessment in adopted direction c.6897859755 is quoted as that text's, not as a finding of this audit | Standing; §18 |
| Conditions organized by claim: the six-row table is the key, and each row names only the claims its content needs (6897946443) | §0; §12.3 |
| The recovery target is the observable conclusion: a direct-proof target per row, with the old proof's conditions it would avoid (6897946443) | §12.3 |
| Scope conceded: finite-model mathematics, replacement theorems, conditional results (6897946443) | §12.3; §12.4; §18 |
| Two barred shortcuts: no assumption adopted solely to rescue a result; no conditional recovery called unconditional (6897946443) | §14.4; §19 |
| Re-pin to EF-1 r4 (done in r6; the pin has since moved to EF-1 r6, Standing) (the record's next steps in 6897254631; "The planned r4 and re-pinned audit address the right issues", 6897455387) | Standing; every EF-1 citation; §14.1; §20; §17 |

Population of this table: 25 lines, one for each direction applied.

**Carried from r4 without change** (the review of r4 confirmed each): the 56 rows and their categories (AM-5b, added after the review of r6, makes 57);
the reasons column (47, 6, 3 for the 56; 48, 6, 3 with AM-5b); the F-each and F-one definitions; the landings of the 16 RC rows; AM-28's
split; the census table apart from family 34; the Main:332 adjudication; the A1-test list. **Carried from r5 without change in r6:** everything except the passages listed in §17.

## 2. Rows AM-1 to AM-10: the uses Main:60 lists

*Coverage of the site lists.* The sites listed under "Downstream." and elsewhere in this section are those this audit found. They were checked only for existence and for a keyword of the row's subject on the cited line; a site that paraphrases its subject would not have been found, and no list here is claimed to hold every affected site (§21).

### AM-1 Recurrence step and recurrence-scale P-indivisibility

1. **Results and where A1 enters.**
   - AM-1.1 The recurrence-cycle theorems. The non-permutation-witness theorem (Main:113–129; Step 1,
     Main:121: "φ bijective on a finite set ⇒ ∃N: φ^N = id"), its lemma form (Main:435–437), and
     "history readback + finite recurrence implies indivisibility" (Main:135–139; the finite order `L`,
     Main:137). K: `isPermMatrix_of_stochastic_inverse` (`EquivalenceChain.lean`, census 1, cited at
     Main:137, not an anchor), `rootedMap_periodic` (`RootedClassification.lean:135`, census 40). A1
     enters through `C_H` finite "under the total-finiteness posit" (Main:111, :129). The root-independent
     prior the theorem needs is supplied per horizon by the process dilation (Main:516) and the
     response-table form (Main:518), a paper proof whose root-independence clause is not formalized
     (census family 1 note). Not part of this row (§6): the stochastic-inverse lemma (Main:131–133), which
     Main:60 lists among the results that use only Lemma 1; and two A1-free sentences of Main:139's Scope
     (r3 review B3): "For every visible prior, a non-deterministic visible step ... makes some `Γ_s` a
     non-permutation" and "if every `Γ_s` is a permutation, `Γ_s^{-1}Γ_t` is a stochastic divisor".
     Main:157's "(Scope, above)" points to Main:139 for the XOR-control limit, whose statement is also at
     Main:626.
   - AM-1.2 The overlap-and-return theorem (Main:141–143). K:
     `pIndivisible_of_rooted_identity_return_of_overlap`, `c4r_of_rooted_identity_return_of_overlap`,
     and the matrix form `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`,
     census 34), which "assumes only that `Γ_s` is row-stochastic" (Main:143). A1 does not enter; the
     identity return is a hypothesis.
   - AM-1.3a The accessible-window revival criterion (Main:157): "A sufficient further condition is a
     revival of distinguishability within the window". Proof: total variation between two rows does not
     increase under right multiplication by a stochastic matrix (the step of Main:143). K, kernel-only:
     `c4r_implies_pIndivisible` (`CausalReadback.lean:134`) and `c4e_implies_pIndivisible` (:148), Section
     A, stated for any family `Γ : ℕ → Matrix V V ℝ` on a finite `V`, with no hidden carrier, prior or
     reversibility (:28–31); census 33 (kernel-only). Main:157 does not cite them. Worked instance:
     Main:184–200 (§2.4). Cx:496 applies it.
   - AM-1.3b The reading of AM-1.1 as a property of nature's visible process: "P-indivisibility enters
     ... unconditionally at the recurrence scale" (Main:626); "The P-indivisibility proof uses total
     finiteness ... via the recurrence argument" and "with P-indivisibility retained at the recurrence
     scale" (Main:716); "the former establishes P-indivisibility from a non-permutation one-step witness
     and finiteness alone, at the recurrence time" (Main:178); "its role is confined to nontriviality at
     the recurrence scale" (Main:354); the stated device-level prediction (Cx:434).
2. **Test.**
   - AM-1.1: **RM.** Its hypothesis (a non-permutation rooted map, given by any non-deterministic visible
     step, Main:139) is a property of the law; its conclusion (failure of P-divisibility on
     `{0, …, L}`, `L` the realization's order) is a property of the completion past the horizon
     (Main:520).
   - AM-1.2: **RD.** The matrix form holds for every family of stochastic matrices: an observed overlap at
     `s` and an observed identity return at an accessible `n > s` certify P-indivisibility on
     `{0, …, n}`. As stated, it excludes no law.
   - AM-1.3a: **RD.** A measured revival on an accessible window certifies P-indivisibility on that window.
     As stated, it excludes no law; the witness is empirical: no A1-free derivation of a revival from C1–C4 is on
     `main` (Cx:496; the XOR control, Main:139, :626, shows C4 does not force P-indivisibility on windows).
   - AM-1.3b: **RX.** Exact synchronized return of nature's rooted visible maps is a property of nature's
     total dynamics.
3. **Recovery attempt (AM-1.3b).**
   - Strongest A1-free results: AM-1.3a (K, kernel-only; P), AM-1.2's matrix form (K), the empirical route
     ("P-indivisible dynamics are documented in open-system experiments", Main:626), and the readback
     lemma's accessible conditional memory (Main:60, A1-free).
   - Candidate derivation: obtain an identity return, or a revival, at an accessible time from visible
     data or from a premise on the visible sector alone.
   - Countercontrols: Poincaré recurrence of a finite-measure system returns almost every point at its own
     time, not synchronously (Main:155; `ch18-beyond.md:172`); DEPENDENCY-AUDIT.md:285 control 3 (a
     countable union of finite cycles, full-support invariant probability, measured visible matrix the
     identity at no positive step; audit record, review independence not established); in the OBL class
     the identity return fails (support off `main`, PR #1303).
   - Remaining gap: no A1-free derivation from C1–C4, or from any other visible-sector premise on `main`,
     of a synchronized return or of a revival on an accessible window. Recurrence-scale P-indivisibility
     of nature is open; on `main` the witness is empirical.
   - Not a recovery: Main:155 (continuous-time form) assumes total-flow hypotheses; not an A1 consumer
     (Q11).
   - The fixed-horizon description (EF-1 r6 N3.1) [IR]: a finite bijective realization
     faithful on `[0, n]` with order `L ≤ n` forces an exact visible return inside the window; otherwise its
     recurrence lies beyond the horizon on which it reproduces the law. A finite description for a chosen
     horizon supplies no recurrence guarantee within that horizon. So F-each does not carry this row; the
     row would need F-one together with an exact return, which is not established. The in-window
     certificate (AM-1.2's matrix form) is A1-free. EF-1 r6 §4.2 splits this class: the counting form (Main:113–129) uses a bijection of a finite carrier with its counting measure and the return at that bijection's order, which lies outside any window shorter than the order, so a window-valid closure cannot supply it (§14.3, Table 5); the return of the rooted maps at the order `L` needs F-one (§20, T8, T9).
4. **Downstream** (grep of `P-indivisib|recurren|finite reversible representative` over `papers/`,
   `book/`; sites read in context where listed by line).
   - Headline sites (H1; §8): Main:18 (three sentences, "On one fixed finite reversible representative
     ..." to "... Markov on every accessible window."), Main:80 item (2) (the recurrence-cycle clause);
     Intro:12, :24; `preface.md:3` (FULL:64); `ch00-introduction.md:53` (FULL:280); `ch01-observation.md:93`
     (FULL:428).
   - Main body, RM (theorem about a fixed finite realization): Main:111, :113–129, :135–139, :145 (AM-28),
     :157 (first sentence), :180, :338 item (2), :435–437, :731 (consolidation clause, with AM-9), :733
     ("bare-recurrence form ... at `t_R`").
   - Main body, RX (nature reading): Main:60 (the list item "recurrence-scale P-indivisibility", with
     AM-10), :178, :354 (last clause), :626 ("unconditionally at the recurrence scale"), :716 (second
     sentence and "retained at the recurrence scale").
   - Main body, RD: Main:141–143, :157 (second and third sentences), :626 (the empirical route).
   - Companions: GR:22, :90, :138, :585, :587; SM:24, :44, :90, :106, :112, :236, :308; Sub:44, :52, :92,
     :137, :268; Struct:1024, :1138 (§14.3 heading), :1140, :1146, :1174, :1177, :1179 (RM), :1189, :1193,
     :1211 (RX), :1248, :1255; Intro:87–93, :151, :185; Medicine:13, :25; Bioinformatics:14; Cx:374 (RX),
     :430–434 (RX), :474.
   - Book: `ch01-observation.md:89` (FULL:424), :95–121 (FULL:430–456; :121 RM), :133 (FULL:468, RX), :181
     (FULL:516), :201 (FULL:536); `ch02-substratum.md:32` (FULL:666); `ch03-structural-realism.md:36`
     (FULL:901), :102 (FULL:967), :114 (FULL:979), :240 (FULL:1105); `ch05-gauge-structure.md:41`
     (FULL:1359), :95 (FULL:1413); `ch09-universality.md:106` (FULL:2573); `ch15-quantum-engineering.md:114`
     (FULL:4063); `ch18-beyond.md:74` (FULL:4880, row N-5) and §18.7 (row N-1); `appendix-b-derivations.md:22`
     (FULL:5776), :194, :413–421 (FULL:6167–6171), :451 (FULL:6205), :454 (FULL:6208);
     `appendix-c-objections.md:120` (FULL:6350); `glossary.md:105` (FULL:6689), :117 (FULL:6701, RM). Sites
     not marked above are split by the rule of §0 in the correction unit [IR].
   - Census: 34 (anchors Main:137, :141, :143), 35 and 36 (Main:145), 40 (Main:638), 33 (kernel-only;
     becomes carried if Main:157 cites it). See §10.
5. **Treatment.**
   - AM-1.1 RM. Headline sentences leave the headline (H1). In the body, under Q2(a): Main:111 and :129
     replace "under the total-finiteness posit" by the realization's hidden space, and the theorems are
     stated of a fixed finite reversible realization with a root-independent prior (Main:516, :518). Under Q2(b) as reformulated (§12.1, Q2): the theorems of Main:111–129, :135–137, the recurrence clauses of :139
     and :435–437 keep their paper proofs (the root-independence clause and three steps of Main:137 are proved on
     paper only) and move to a named destination; nothing is deleted. §12.2 names the destinations: a new
     appendix of Main is the one with no Main-independence exposure; a move to a companion paper is safe only if
     Main:157's first sentence, Main:180, Main:338 item (2) and Main:733's bare-recurrence clause are rewritten,
     and SM:24, GR:22, Struct:1140 and Struct:1255, which send the reader to Main for this proof, are repointed,
     in the same change.
     Main:131–133 and Main:139's A1-free sentences stay; Main:157's pointer is repointed to them or to
     Main:626. [IR] The stochastic-inverse lemma's uses on `main` are Main:137 and Main:139 (Main:332's "the
     Lemma" is the diagonal-preservation lemma of Main:326, as the r3 review confirmed); if no remaining
     Main root uses the lemma, the Main-root rule relocates it with its proof to the upstream-most
     downstream paper that uses it; it is not deleted, and `isPermMatrix_of_stochastic_inverse` stays in the
     kernel.
   - AM-1.2 RD: kept; the matrix form is the statement that bears on measured data.
   - AM-1.3a RD: kept at Main:157, optionally with the kernel citation (§10, family 33).
   - AM-1.3b RX: the RX sites above are rewritten to the visible statement (accessible conditional
     memory, the readback lemma; P-indivisibility certified by a measured revival or identity return).
   - What breaks: the headline recurrence-cycle sentences; the stated derivation of the device-level
     prediction that memory is "specifically P-indivisible" (Cx:434; §13); no census anchor under Q2(a);
     under Q2(b) family 34 needs no registry action while Main:143 stays, since the registry holds one (file,
     string) entry per anchor and `pIndivisible_of_rooted_identity_return_of_overlap` occurs at Main:137 and
     Main:143 (review C13.2); families 35 and 36 keep their definitional anchors (and 36 its separation identifiers), and
     family 40 becomes kernel-only if Main:638 is withdrawn (§10). Main:80's "three exact layers and one explicitly conditional extension" unchanged.
     Main independence: unaffected.
6. **Goal link.** Decides whether "nontrivial at the recurrence scale" can be stated of nature's visible
   process, or only of finite realizations, and what replaces it at the headline.

### AM-2 CP-indivisibility theorem, framework scope

1. **Result.** Main:330–332 (P), with diagonal preservation Main:326–328 (K `isDiag_Phi`,
   `EquivalenceChain.lean:253`, census 1 anchor at Main:550). Book Theorem B.2.5,
   `appendix-b-derivations.md:92` (FULL:5846). A1 enters through the §3.2 setup (AM-5: finite `C_H`, uniform
   `ρ_H`) and through its premise, recurrence-scale P-indivisibility (AM-1). [IR] Main:326 already writes
   the channels with `μ_H` (`Tr_H[U^t(ρ ⊗ μ_H)U^{-t}]`), while Main:280 sets `ρ_H = I_m/m`.
2. **Test.**
   - AM-2.1 **RC (P1).** Statement [needs proof, one line]: for the permutation-dilation family of a
     finite reversible realization with root-independent prior `μ_H` (Main:516), built with
     `ρ_H = diag μ_H`, P-indivisibility of the visible population law on a window implies
     CP-indivisibility of that family on the window. Main:332's argument (diagonal preservation and
     stochasticity of the induced matrix) is unchanged once P1 identifies the family's diagonal action with
     the law's `Γ_t`. **Lands as RM**: the diagonal action is fixed by the law, but the CP structure belongs
     to the chosen realization; its physical content is AM-1.3a's (a measured revival supplies the premise).
   - AM-2.2 **RX.** The reading as a property of nature's channel at the recurrence scale (B.2.5's
     "P-indivisibility of the substratum dynamics across its recurrence cycle") inherits AM-1.3b.
3. **Recovery attempt (AM-2.2).** As AM-1.3b. Remaining gap: AM-1.3b's.
4. **Downstream.** Main:326–338, :354; Intro:111; `appendix-b-derivations.md:12` (FULL:5766), :92–96
   (FULL:5846–5850); census 1 anchor `isDiag_Phi` at Main:550 (not touched).
5. **Treatment.** AM-2.1 RECOVER (P1), landing RM; under Q2(b) the recovered statement stays in Main §3.2, since kept Main text refers to it (Main:338, :354; §12.2). AM-2.2 REMOVE.
   Nothing else breaks.
6. **Goal link.** Decides whether the §3.2 route to CP-indivisibility bears on nature's law or only on
   chosen realizations.

### AM-3 Bijectivity: eventual image, surjectivity, hidden-sector injectivity

1. **Results.**
   - AM-3.1 Injectivity on states with distinct registered content, the record prong (Main:36, :60:
     "injectivity is the requirement that the dynamics preserve the observer's records"). No A1.
   - AM-3.2 Bijectivity of nature's `φ`: the hidden-sector prong (double stochasticity under the uniform
     prior on a finite product carrier; restriction to the eventual image of a map on a finite set), "On a
     finite set, injectivity implies surjectivity" (Main:60), Lemma 3's "as the reversible representative
     of §1.2, a bijection" (Main:54), ledger item (iii) (Main:724). K `injective_imp_bijective`
     (`CanonicalMeasure.lean:63`, `[Fintype S]`; census 1, not an anchor).
2. **Test.**
   - AM-3.1: **TD.** A requirement on nature's total map (`φ(s) ≠ φ(s')` whenever the registered content
     of `s` and `s'` differs), stated as record preservation. It is not a statement about the visible law
     and assumes no cardinality; it is of Q11's kind.
   - AM-3.2: **RX** as a derived property of nature. [IR] No visible-form result needs it: every class-D
     realization is a bijection by construction (Main:97, :520 "extends to a bijection of the finite
     product").
   - (C2-structural) clause (Main:18, Main:80 item (2): "holds by reversibility in every bijective
     realization"): true of every bijective realization; [IR] its reading for nature's stored hidden
     record needs injectivity on the hidden sector, which is AM-3.2's open part, so it follows H3 (§0) and
     Q5. r2's reading that it is "unaffected" is withdrawn.
3. **Recovery attempt (AM-3.2).** The paused AM-3 unit (preregistration r2 and two pre-freeze reviews,
   unpushed drafts; [IR] throughout): strongest existing results are the finite statement (P; K) and the
   record prong; candidate weaker premises W1 (conservativity), W2 (invariant probability), W3 (W2 with
   uniform visible marginal); conservativity of a σ-finite measure gives surjectivity mod 0, W2 gives only
   `μ(φX) = 1`; a null-set redefinition of `φ` keeps every W1–W3 hypothesis and merges two visibly equal
   states, so pointwise hidden-sector injectivity is unreachable for every member; no named consequence
   passes the independent-consequence test. A further route, recorded by the validity review (G4) and
   checked here at `SubstratumInterfaceAudit.lean:81` and `:106`: on the selected structure `φ` is
   `leapEquiv`, an `Equiv`, so `a2_every_substratum` holds on any site set; it is definitional and rests on
   posit (xiii), whose stated scope (Main:724) is the continuous path of *-automorphisms, so using it for
   A2 widens that posit's role [IR]. Remaining gap: a premise that excludes hidden-only merges directly (W4,
   a translation-commuting finite-range rule, gated on that unit's Q2; a reference-prior member; or the
   (xiii) route), or the Rohlin natural-extension route for W2. None is authorized. Ledger item (iii)
   allows adopting reversibility as a postulate instead (Main:724); that adds a premise (Q5(b), §A.29).
4. **Downstream.** Main:18 and :80 item (2) (the C2-structural clause, H3), :36, :44, :54, :60, :724 (iii);
   Meth:146, :156, :158, :166, :253, :261; Sub:94 and the A1–A6 class (Sub:92–104, :205–223); SM:44; GR:605
   (the A.8 model); `ch01-observation.md:41` (FULL:376); `ch09-universality.md:108` (FULL:2575). Census: no
   anchor.
5. **Treatment.** AM-3.1 TOTAL-DYNAMICS (no change; Q11). AM-3.2 REMOVE as a derived property of nature
   (default), unless Q5 adopts a postulate or the (xiii) route. Lemma 3 would state that finite
   realizations are bijective by construction and that nature's dynamics is injective on registered
   content; hidden-sector injectivity and surjectivity of nature's dynamics are open. The C2-structural
   clause follows Q5 (H3). What breaks: rung 6's "rest of it ... on A1" (Meth:166), A2's justification
   (Sub:94), the information-conservation premise at `ch09-universality.md:108` and Chapter 7 §7.6, and the
   proofs gated on Q5 (§14). No prediction is lost.
6. **Goal link.** Decides whether bijectivity of nature is derived, postulated or open, and which
   recoveries and headline clauses wait on that decision.

### AM-4 Counting measure of Lemma 3, the uniform hidden prior, Proposition 4b

1. **Results.**
   - AM-4.1 Lemma 3's finite-cycle clause and the maximal-entropy property of the counting measure on a
     finite set: K `orbit_invariant_unique` (`CanonicalMeasure.lean:178`), `counting_maximal_entropy`
     (:227), `[Fintype S]`; census 1, no anchor.
   - AM-4.2 The baseline matrices `T_ij` with denominator `|C_H|` (Main:113–117) and the uniform prior that
     defines them. r4 also placed the reverse-direction lemma of Main:274–278 in this row. **[reviewer reading,
     unresolved]** (review C2): that lemma realizes a doubly stochastic matrix "for some finite
     $\mathcal{C}_H$" (Main:274), a hidden space it constructs (Main:276), so it does not consume A1 and
     belongs with the results of §6. r5 reports both positions (§20, D3) and settles neither.
   - AM-4.3 Ledger item (iv) read for nature: nature's measure is the maximal-entropy invariant (counting)
     measure (Main:54, :58, :60, :724 (iv)).
   - AM-4.4 SM Proposition 4b (SM:334–336): custodial scalarity of the observer's quadratic response, for
     the selected counting measure, and for "extensions of the rule whose dynamics, measure and observer
     σ-algebra are equivariant under signed permutations of the six components (H-blind)".
2. **Test.** AM-4.1, AM-4.2: **RM** (lemmas and definitions on a finite realization under its default
   prior; Main:58 already makes the prior "part of the realization datum"). AM-4.3: **RX**; on infinite `S` the
   counting measure is not normalizable (DEPENDENCY-AUDIT.md:291, control 6; Sub:262). Not an A1-test
   (§11): [IR] an invariant normalized prior with uniform visible marginal on an infinite carrier gives the
   same doubly stochastic one-step matrix (EF-G5); EF-1 r6 N3.2 derives the invariance of the uniform
   product measure under the selected phase-space map on any site set from Main inputs (a shear and
   Tonelli argument, checked by the review of EF-1 r2; a statement about the full system), which replaces EF-1's off-`main` support, and notes the bearing on ledger item
   (iii)'s "uniform-prior doubly stochastic scope" (Main:724). The extension to every bijection of the locality class of `main` rests on (M-full), which the review of EF-1 r4 checked; no class uses it. AM-4.4: **RC (P13)** [IR]: the extension clause covers a
   normalized signed-permutation-equivariant product measure on an infinite lattice, provided the
   memory-resummed response is defined for it; the measure is a premise of the posit (iv) kind (Q6).
   **Lands as CV** under Q6(c) [IR]: it would exclude visible responses whose spatial-to-temporal ratio
   differs among `T_1`, `E` and `A_1`. The counting-measure statement itself is RM.
3. **Recovery attempt (AM-4.3).** Strongest existing result: Main:58's realization-datum reading. A
   visible-form selection would select a prior on each constructed realization, and the §3.4 construction
   carries a structured prior, not a uniform one (Main:520–522). In the OBL class the uniform product
   measure is invariant and Lemma 3's principle does not select it (support off `main`, PR #1303); the
   validity review (N1.5, [IR]) names maximal entropy density among translation-invariant measures as the
   replacement on the selected model, not on `main`. Remaining gap: a selection principle for a normalized
   prior on nature's hidden sector without finiteness; any such principle is a premise (Q6, §A.29).
4. **Dependency (review F4).** AM-21's theorems use `T` as their benchmark: "the reference prior defining
   `T`" (Main:449), "with `π_H` the *reference prior defining `T`* — the uniform hidden prior of the model
   above" (Main:453). Moving AM-4.2's text (Q2(b)) without restating `T` from a realization's reference
   prior `π_H` in the same change breaks AM-21. [IR] Per horizon, the uniform product family is consistent
   on any site type (`uniform_family_consistent`, `RegionTower.lean:447`; EF-1 r6 N3.3), so the baseline
   matrices have a per-horizon form on an infinite carrier; read of nature, that prior is a selection
   (Q6(c)). Their double stochasticity is a property of the record law that needs invariance on the full system (EF-1 r6 N3.2 for the second-order form; (M-full) for the locality class; no class uses either); Lemma 3's selection needs the invariant measures of nature's own map, which the description does not inherit (§14.3, Tables 3 and 5).
5. **Downstream.** Main:54, :58, :60, :113–117, :129, :266, :274–280, :449, :453; SM:252, :292, :334–336, :641
   (AM-30), :1225, :1227; GR:58, :70 (AM-22); Sub:253, :262, :459; Comp:120; `ch01-observation.md:38`, :85;
   DEPENDENCY-AUDIT.md:291. Census 1 (no anchor for the two lemmas).
6. **Treatment.** AM-4.1, AM-4.2 RECAST-MATHEMATICAL; under Q2(b) AM-4.1's statements are withdrawn (the
   kernel keeps them), and `T` is restated from a realization's prior `π_H` in the same change. For
   Main:274–278 the two positions differ: **[reviewer reading, unresolved]** it stays in place as an A1-free
   lemma (kept text uses it: Main:522, ledger item (iii)'s "uniform-prior doubly stochastic scope", Main:724);
   on r4's reading it is part of this row and would move with its paper proof, and then only to an appendix of
   Main, because that kept text refers to it (§12.2). AM-4.3 REMOVE as a claim about nature (default), or restrict item (iv) to
   the default prior of a constructed realization, or adopt a normalized reference-state premise (Q6).
   AM-4.4 RECOVER (P13, gated on Q6). Nothing headline breaks.
7. **Goal link.** Decides which prior defines the baseline matrices and whether any measure on nature's
   hidden sector is asserted.

### AM-5 The §3.2 setup, channel and Born form

1. **Results.** Setup Main:266 (`C_H` "under the total-finiteness posit"); permutation unitarity
   Main:268–270 (K `permMatrix_mem_unitaryGroup`, census 1 anchor at Main:550); the channel with
   `ρ_H = I_m/m`, Main:280–284; the Born-form representation theorem, Main:286–288 (P).
2. **Test.** **RC (P1).** As stated, the channel and the Born-form identity use the uniform prior, so they
   compute the uniform-prior marginal, which is doubly stochastic (Main:276–278, :522), not the law a §3.4
   realization reproduces. Statement [needs proof, one line; P1]: with `C_H` and a root-independent prior
   `μ_H` of a finite realization (Main:516), `Φ(ρ) = Tr_H[U(ρ ⊗ diag μ_H)U†]` has Kraus operators
   `√μ_H(k) ⟨l|U|k⟩`, and `P(j|i) = Σ_k μ_H(k) δ_{j, π_V φ(i,h_k)} = Γ_1(i, j)`. The kernel's channel already
   carries a general hidden weight (`Phi φ μ t ρ`, `μ : H → ℂ`; `isDiag_Phi` for every `μ`,
   `EquivalenceChain.lean:241–253`). **Lands as RU**: every finite-horizon law of nature has such a
   representation (Main:354, :552); as stated, it excludes no law. The permutation-unitarity lemma is RM and is
   unchanged.
3. **Recovery.** P1 (Main, Main's own support, no premise).
4. **Downstream.** Main:264–288, :326–332, :352, :354, :716; Sub:110; GR:667 (S4);
   `appendix-b-derivations.md:12` (FULL:5766), §B.2; census 1 anchors at Main:550 (not touched).
5. **Treatment.** RECOVER (P1), landing RU. Main:266 reads "`C_H` and `μ_H` the hidden space and prior of a
   finite realization (§3.4)"; Main:280 replaces `I_m/m` by `diag μ_H`, with the uniform state kept as the
   special case of the doubly stochastic lemma. Sub:110 and GR:667 lose their A1 link once P1 holds.
6. **Goal link.** Decides whether §3.2's route represents nature's law or only uniform-prior models.

### AM-5b One-step coherence results of §3.2 (Main:290–324)

**Added in r7 (the review of r6, F9; adopted direction, c.6898395533: "The population is now 57."). Unreviewed.** Every line cited in this row was read at `main` for r8 and matches: Main:60, :266, :280–282, :292, :304–320 (Lemma 2 at :304, the threshold theorem at :312, Corollaries 1 and 2 at :316 and :318), :310, :316, :322, :324.

1. **Result.** Lemma 2, the separability threshold and Corollaries 1–2 (Main:304–320); the Theorem itself (Main:312) is a statement about abelian Weyl subgroups on `s` qubits and uses no hidden sector, so A1 enters Lemma 2 (iii) and the Corollaries only, on "the substratum of §1.2 on a lattice $\Lambda$" (Main:292). A1 enters through the §3.2 channel with a finite `C_H` and `ρ_H = I_m/m` (Main:266, :280–282); Lemma 2 (iii) is computed with the hidden input uniform (Main:310), and Corollary 1 assumes the hidden sector initially uncorrelated and maximally mixed (Main:316). Main:60 lists "the finite hidden space of the §3.2 setup" among the uses of the finite representative.
2. **Test.** **RM.** Properties of the one-step channel of one displayed realization ("All of this concerns the realization displayed above", Main:324). Reason (i): the link to nature runs through A1 (Main:266). Not of AM-5's kind, which lands RU.
3. **Recovery.** None claimed. Only the boundary sites enter ("the criterion carries no dependence on $|H|$", Main:322), so a form with a uniform, uncorrelated law on the hidden boundary sites (D2, D4) is a candidate [IR], with no recovery credit. EF-1 r6 (nit 5 of its recheck) states the target for one step of the displayed update over `F_2` (Corollary 1, Main:316; stated for `q = 2`, Main:324). The result concerns off-diagonal action, which depends on the closure chosen (the recheck of EF-1 r5, §1.6, unchecked).
4. **Columns.** Category RM; reason (i); lands as: not applicable; class: none (not a recovery row); Q2 subset: yes, the 18th; observable conclusion about a finite experiment: no; concession: FM; window confinement: yes for one step. Kernel witnesses for the threshold Theorem are named at Main:314 (`entanglementBreaking_twirl`, `not_entanglementBreaking_twirl`, `exists_lagrangian_tuple`, `isotropic_iff_commute`, `separable_imp_ppt`). Census: family 1, anchors "separability threshold" (Main:312) and `` `entanglementBreaking_twirl` `` (Main:314); no registry action while Main:312–314 stay, which every option of Q2 provides.
5. **Treatment.** RECAST-MATHEMATICAL; stays in Main §3.2. If P1 replaces `I_m/m` by `diag μ_H` at Main:280, the uniform hidden state is written into the statements of Lemma 2 (Main:304–308) and Corollary 2 (Main:318), which now inherit it from Main:280; Corollary 1 (Main:316) states it already.
6. **Goal link.** Decides whether the one-step coherence results are stated of nature or of the displayed realization.

### AM-6 Corner occupancy (Main:216)

1. **Result.** "a finite deterministic substratum observed by marginalization cannot generate first-order
   leakage, and its emergent dynamics is thereby confined to the near-unitary corner ... the framework
   occupies the corner Doukas identifies not by selection but by structural necessity, conditional on the
   total-finiteness posit", with the prediction "fundamental dynamics of continuous-time Markov type would
   require an actually infinite hidden sector" and `𝒟` "the corner-occupancy claim's falsifiable residue".
   Doukas's bound is external and continuous-time.
2. **Test.**
   - AM-6.1 **RM.** The finite-model clause (marginalization over a finite environment produces no
     first-order dissipative term), an external import, stated in continuous time and applied by analogy
     to the discrete substratum.
   - AM-6.2 **RX, A1-test** (§11, candidate 2). The corner occupancy of nature and its prediction: their
     content is the cardinality of nature's hidden environment.
3. **Recovery attempt (AM-6.2).** [IR] Per horizon the visible law depends only on the finite cone sector
   `C_V × C_{B_n}` (GR:132; infinite deep sector allowed given a normalized product prior, a locally finite
   coupling graph and well-defined dynamics; proof GR:134). Gap: the cone-restricted dynamics is not an
   isolated finite system (boundary sites read outside the cone), so the finite-environment bound does not
   apply as stated; the bound is continuous-time; and the route uses GR §3.2, downstream of Main. The
   validity review (G5, [IR]) adds that every finite-horizon discrete-time law, Markov ones included, has a
   finite reversible realization (`S_imp_D`, Main:97), so the prediction has content only in continuum time
   or at all times. EF-1 r6 (N1.8, N3.5) [IR]: in the native class, under a uniform product prior in both carriers (a
   further distributional property, D2, which needs its own justification), a finite torus of side
   `L > 2n + diam V` gives the infinite lattice's visible law on `[0, n]` (Lemma PM (c); F-each). So, in that
   class, the finite-versus-infinite alternative of Main:216 is not distinguished by an observation over a
   fixed horizon. EF-1 r6 (N3.5) traces the clause on first-order leakage to the estimate of Main:340 and gives the form as mixed: the cardinality clause is not a fixed-horizon statement in the native class, and the estimate of Main:340 is undetermined (§20, D14, T14). The fixed-horizon lemma
   does not carry this row.
4. **Downstream.** Main:216 only. Intro:91 cites Doukas's Prop. 1 for the contraction argument, not the
   corner; unaffected. No book mirror (r9). No census anchor.
5. **Treatment.** AM-6.1 RECAST-MATHEMATICAL (external import named; continuous-time scope stated). AM-6.2
   REMOVE the corner-occupancy sentence, "structural necessity" and the prediction, unless Q9 keeps it as
   an explicitly conditional statement. The `𝒟` estimate stays in §3.2 (Main:352). A downstream recovery
   is possible only through Q1(b-loc), Q6 and Q8 and needs its own unit.
6. **Goal link.** Housekeeping of a scope clause of the §3.1 route: decides whether the corner-occupancy
   prediction can be stated without A1.

### AM-7 The coupling-graph causal cone and the Bell results

1. **Results.**
   - AM-7.1 The cone (Main:362): `S = ∏_{i∈V} S_i`, "V and each S_i finite" (here `V` is the whole site
     set); "Finiteness of V is used in the first step".
   - AM-7.2 The Bell ceiling for a screened local completion (Main:364–383, P; pointwise bound EX, check
     11), summing over `Ω`.
   - AM-7.3 The Bell–lattice corollary (Main:414) and its mirrors Main:650 (ii), :770; abstract Main:20.
2. **Test.**
   - AM-7.1 **RC (P3).** Statement: if each site's update depends on a finite set of sites, the component
     `(φ^k(s))_i` depends only on initial components in the union cone `⋃_{m≤k} ball(i, m)` (EF-1 r6 N1.1:
     with the exact-step ball the statement fails for updates in which a site does not read itself, e.g.
     the shift `φ(s)_i = s_{i+1}`; the union, or the hypothesis `i ∈ N(i)`, repairs it). Kernel, for a
     site type of any cardinality with a `Finset` neighbourhood per site: `iterate_dependsOnlyOn_ball`
     (`RegionTower.lean:283`), `readout_unaffected_outside_ball` (:304), given `CouplingGraph` (:254);
     census 8. The kernel lemma is one-time and `Q`-valued with one alphabet `Q` for every site
     (:246–256), while Main:362 has site-dependent alphabets `S_i`; the paper step [needs proof, short]
     embeds the `S_i` into one alphabet preserving each dependency set and assembles the joint `C_V`-valued
     form per site and per time (`site_iterate_dependsOnlyOn`, :297). What changes: Main:362 derives the
     graph from the dynamics, and without finiteness the derivation fails (EF-1 r6 N1.2's countercontrol on
     `(Z/q)^ℕ`: a tail function insensitive to every single coordinate and a function of no finite set);
     finite reading sets (L1) become a stated hypothesis whose ledger source is an undecided reading (Q8;
     §14.1): item (ix) is "one degree bound across the family of finite representatives — at a single
     finite lattice the bound holds automatically" (Main:724); item (xiii) states finite reading sets but is
     scoped to "the continuous path of $*$-automorphisms from the identity to the update in §3.2 and §3.4".
     *What the row takes from the fixed-horizon lemma:* its pointwise dependency statement only (EF-1 r6
     Lemma PM (a)), which needs finite dependency sets (L1; EF-1 r6's F3) and nothing else: no finite alphabet (review
     C13.3: L2 is needed for the description to be finite, not for the dependency), no starting law and no
     further distributional property. **F-each. CONTINGENT (Q8). A candidate; no recovery credit.**
     *The intervention form* ("an intervention that reads and writes only region $A$ cannot alter, $k$
     updates later, any component outside $B_{G_\varphi}(A,k)$", Main:362): the two runs differ only in
     the intervention applied on `A`; every other setting, input and policy, with its information, is the
     same. The conclusion holds because `A` does not meet the backward set of `R` within `k` updates. In EF-1 r6's terms this is the single-step form of Lemma PM-I with one intervention whose declared support is `A`; the support must hold in every state (§20, T3).
     Where `A` meets it, matching initial data does not give matching readouts (review C8). **Lands as
     TD**: a statement about nature's total dynamics that assumes no cardinality. A CV part [IR] would
     exclude visible interventional laws in which an intervention on `A` changes a readout `R` with
     `d(A, R) > k` within `k` updates, but only with link L10 (the identification of the observer's
     intervention and readout regions with coupling-graph regions and their graph distance), which is not
     on `main`: item (viii) is site factorization only (Main:724), and Main:414 records that which
     propagation sets the physical light cone "is not derived here".
   - AM-7.2 **RC (P4).** RM as stated (finite `Ω`). Two candidate routes.
     (1) *P4* [needs proof, standard]: the theorem for a probability space `Ω` with measurable response
     functions, the sums of Main:378 replaced by integrals. It needs no finiteness of `Ω` or of the
     regions. [IR] Its proof uses the cone lemma ("by the cone lemma and (iii)", Main:384; the proof begins at Main:383), so on a carrier
     of undetermined cardinality hypothesis (iii) is read with a coupling graph in the dependency sense
     (each site's update depends only on its declared finite neighbourhood). As a property of the class
     of completions the theorem excludes, that is a hypothesis of the statement, not a premise about
     nature. r6 classed the row FIRM on that footing; under the one rule of §0 the dependency-sense reading and the measurability of the response functions are not on `main`, so the row is CONTINGENT on that reading (§14.1); asserted of nature's own lattice it would inherit
     AM-7.1's contingency.
     (2) *The fixed-horizon route* (EF-1 r6 N3.6; its patch was checked by the review of EF-1 r3; provisional [IR]): for lattice
     completions and an experiment of finite duration, each wing's outcome is a function of its own
     setting and of `Ω_n`, the pre-setting data on `W_A ∪ W_B ∪ A ∪ B`, where `W_A`, `W_B` are the backward
     sets of the readout regions from the setting step and `A`, `B` are the setting regions (review C8;
     where the settings are generated inside the substratum, the generator regions are added). The
     finite-`Ω` proof then applies to `Ω_n` as written.
     *What route (2) takes from each group.* Finiteness premises: L1, L2, and `A`, `B`, `R_A`, `R_B` finite,
     which is a premise not separately stated on `main` (EF-1 r6 N3.6: FS-all for the one setting step). The
     route needs the **all-branch** form: the theorem compares four setting pairs on one ensemble with one
     weight `p(Ω)`, so one patch must serve every setting; a per-run patch could differ between settings and
     between runs, and no single `p(Ω_n)` would be defined on it. The reading sets are the actual one-step
     dependency sets, so that each backward set lies inside the ball of the graph in which Main measures the
     distance. Probability premise: the probabilities `p(Ω_n)`. Further distributional property:
     **measurement independence (MI)**, `p(Ω_n | a, b) = p(Ω_n)`, hypothesis (iv) of the theorem
     (Main:372–374) and ledger item (xiv), "a posit about the initial condition, not derived" (Main:724).
     Route (2) gives dependency coverage only; it does not supply MI, which needs its own justification and
     is tracked separately, as a separate posit (adopted direction, c.6896890693; EF-1 r6's D6). So the row is **not FIRM on the fixed-horizon lemma
     alone**: route (1) is a conditional no-go whose hypotheses (i)–(iv), MI among
     them, are named on `main`. Recovery is not proved by either route. **Lands as NC**: a no-go for the
     class of screened local completions of any cardinality; it constrains completions, not visible laws.
   - AM-7.3 **RC (P3, P4).** The nearest-neighbour wave update is finite range by construction (K
     `leapFiniteRange`, `SecondOrderDrive.lean:306`, `nbhd := gateRegion R`, and `i ∈ gateRegion i`,
     `SecondOrderLayer.lean:208`), on one alphabet, for a site type of any cardinality, so its cone needs
     no Q8 (r3 review R1). The corollary is stated for "every measurement-independent response-complete
     deterministic completion" (Main:414): MI is a hypothesis of the statement, as in AM-7.2, and is not
     supplied by any dependency argument. **CONTINGENT** (r6: FIRM) through the kernel cone and P4, whose measurable-response hypothesis is not on `main`; **not FIRM on the
     fixed-horizon lemma alone**, whose `Ω_n` route would add the finiteness of the wing regions as a
     premise. Recovery is not proved. **Lands as NC**: a no-go for the reference graph's response-complete
     completions of such wings, with the settings the same in the runs compared.
3. **Recovery.** P3, P4 (or the fixed-horizon `Ω_n` route of EF-1 r6 N3.6), inside Main. Candidates; no recovery
   credit.
4. **Downstream.** Main:20, :360–414, :650, :770; GR:112; Sub:109, :123, :481; Bell mirrors in
   `ch01-observation.md` §1.7, `appendix-c-objections.md`, `glossary.md`; census 8.
5. **Treatment.** RECOVER (P3, P4). Main:20's cone and Bell sentences are kept under H1 once AM-7.1 and
   AM-7.2 are recovered (TD and NC content). If not recovered, the Bell ceiling stays a theorem about
   finite realizations (RM) and those sentences leave the abstract (H1).
6. **Goal link.** Decides whether the composite and Bell layer of the target holds for an infinite
   lattice.

### AM-8 §4.6, structural exclusion of equilibrium-phase observers

1. **Result.** Main:742–760: the observer-selection theorem (Main:746–748, conditional on (EM)), the
   anti-Boltzmann-brain corollary (Main:754) and the observer-selection rule (Main:756). A1 enters through
   "a finite bijective (S, φ)" (Main:742), the scope "finiteness of S" (Main:758), the finite Koopman
   permutation operator (Main:744, :758 (ii)) and canonical typicality [31], a result for a finite total
   system [IR]; ledger item (ii)'s "§4.6, whose conclusions hold on the finite representative" (Main:724).
2. **Test (corrected, review F5).** [IR] The theorem's proof (Main:752) uses the cone for the round trip
   within `Σ_loc(V)` (AM-7.1) and (EM), a hypothesis on the compression `𝒦_Σ = P_Σ 𝒰_φ P_Σ` of a finite region
   (Main:744). Neither uses `|S| < ∞` except through the definition of `P_Σ`, which needs a normalized
   reference state on the total carrier. Canonical typicality enters in three places: the proof says it
   "supplies the local-equilibrium *state*, not the temporal mixing" (Main:752); the theorem's "in
   particular" clause (Main:750); and the main step of the observer-selection-rule corollary: "For `(S, φ)`
   in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its
   local equilibrium" (Main:756). The Scope (Main:758) lists "the canonical-typicality result [31]" among the
   theorem's uses. `Σ_loc(V)` is finite by bounded diameter and bounded degree (Main:758 (i); item (ix)).
   So a visible-plus-cone form of the theorem's inequality exists if a normalized reference state is
   given (a premise of the posit (iv) kind, Q6); the second corollary needs a further typicality input.
   The fixed-horizon lemma (EF-1 r6 N3.9) [IR] carries the cone step only (the round trip stays in
   `Σ_loc(V)`; F-each): it does not supply the invariant reference state, the Koopman-spectrum step of
   Main:758 (ii), or canonical typicality for individual states (Main:756). In EF-1 r6's terms (§4.2) the Koopman statements need a permutation of a finite carrier, and the compression needs an invariant reference measure on the full system; the description inherits neither automatically from (M-full) (§14.3, Table 5).
3. **Recovery attempts.**
   - **P8-M (Main-internal)** [needs proof]: for a measure-preserving map `φ` of a product carrier with a
     normalized `φ`-invariant reference state `μ`, whose Koopman operator is an isometry of `L²(μ)`, with a
     locally finite coupling graph (P3) and `P_Σ` defined on `L²(μ)`, under (EM) for `𝒦_{Σ_loc(V)}`:
     `τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε)`. The anti-Boltzmann-brain corollary follows as at Main:754 [IR]. The
     observer-selection rule (Main:756) needs, in place of canonical typicality for a finite total system,
     either (a) a typicality statement for finite regions of an infinite carrier under `μ`, not on `main`, or
     (b) a named hypothesis **(LE)**: every bounded-diameter region `Σ_loc(V)` of the equilibrium macrostate is
     in its local equilibrium state under `μ`. Option (a) is a premise (§A.29); option (b) is a named
     hypothesis of the corollary, carried where it enters like (EM), or, if adopted as a posit, a new ledger
     item (§9). The "in particular" clause (Main:750) is restated with "local equilibrium state" as a
     hypothesis or removed. Check: [needs proof] that the proof uses no invertibility of `φ`; if it does, P8-M
     is stated for an invertible map and is gated on Q5 as well. Scope (ii)'s reason ("the exact Koopman
     operator of a finite permutation has modulus-one spectrum and cannot mix", Main:758) is specific to
     finite carriers; on an infinite carrier the Koopman operator can mix (r9 AM-8, OBL class, support off
     `main`), and (EM) stays a separate hypothesis. Gaps: `μ` (Q6); (LE) or its typicality alternative
     (Q7(a)); the invertibility check (Q5 if it fails); the cone (P3, Q8); whether the exact compressions
     follow `𝒦_Σ^n` on the window, already open at Main:758 (ii). Main independence: Main's cone and (EM)
     only; no H-BD; §4.6 stays in Main, so Main:159, :169 and :656 keep pointing inside Main (Main:656's
     "canonical typicality [31], which ... §4.6 uses" changes if (LE) replaces typicality).
   - **P8-S (relocation)** [needs proof]: canonical typicality on a finite region `R ⊃ Σ_loc` approximately
     isolated over `τ_S` under H-BD (GR §3.2, posited). Gap: the typicality statement for an approximately
     isolated region (the same corollary step as P8-M's, with the same (LE) alternative) and the normalized
     equilibrium state, which H-BD does not supply; so this route is gated on Q6 as well. H-BD is
     downstream, so the result moves to Substratum (Sub:401). Breakage in Main: Main:159, Main:169 and
     Main:656 would cite a downstream paper; to keep Main independent, (EM) and the Scope (ii) definition of
     `τ_B` (definitions, not results) would move into §1.3 or §2.3, and Main:169's and Main:656's references
     to the corollary and its import would be removed.
4. **Downstream.** Main:60 (list item "§4.6"), :159, :169, :656, :724 (ii) and (ix), :742–760; Cx:212; Sub:56,
   :371–377, :401, :407, :409, :413; Struct:522, :532, :718, :733; Meth:162, :283; `ch01-observation.md:125`
   (FULL:460), :223 (FULL:558); `ch02-substratum.md:192–200` (FULL:826–834); `ch03-structural-realism.md:58`
   (FULL:923), :62; `ch04-methodology.md:36` (FULL:1144), :178 (FULL:1286), :182 (FULL:1290). No census
   anchor.
5. **Treatment.** OWNER-PENDING (Q7): (a) P8-M in Main, gated on Q6, Q8 and the (LE) choice, and on Q5 if
   the invertibility check fails; (b) P8-S with relocation and the Main rewrites above, gated on Q6 and the
   same typicality step; (c) REMOVE; or (d) keep §4.6 as theorems about a finite bijective `(S, φ)` (RM),
   with the observer-selection reading for nature removed, as owner decision 6896070253 provides for
   results that need A1; under (d) the row becomes RM and Q2 applies (its proofs are paper proofs; under Q2(b) they stay in Main
   §4.6 or a Main appendix, §12.2). If removed: the conditional anti-Boltzmann-brain exclusion, the
   observer-selection rule that replaces the past hypothesis, and the selection content of Substratum's
   arrow-of-time projection (Sub:401; Sub:371–377, `ch02-substratum.md:192–200`) are lost, and Main:159,
   :169, :656 and the companion and book lines above are rewritten. Either recovery lands as TD [IR]: a
   conditional statement about where observers can sit; it establishes no constraint on the visible law
   at accessible times.
6. **Goal link.** Decides whether the conditional observer-selection results can be stated without A1,
   and where they live.

### AM-9 The §3.4 obstructions for a fixed finite realization

1. **Results.** No uniform finite realization (Main:486); generic intervention combs (Main:496, :556); the
   classical-dimension obstruction (Main:558; Main:600 item (3); unboundedness imported [55]); all-time
   periodicity and the rooted all-time classification (Main:638; K, census 40: the forward direction
   `pper_of_finiteRootedRealizable` and the converse `pper_has_responseRealization`, assembled in
   `finiteRootedRealizable_iff_pper`, each direction witnessed separately, §A.34); "every fixed finite
   representative has finite predictive dimension" (Main:356), with the completion-level boundary at Main:562
   ("What no fixed finite carrier can do ..."). A1 enters only through Main:60's clause "the obstructions
   ... bear on nature through it".
2. **Test.** AM-9.1, the theorems: **RM**, each a theorem about every fixed finite realization; their role
   of scoping the equivalence ("it is precisely why the equivalence carries its subscript", Main:558; "Per
   (3), the equivalence cannot be strengthened to exact class identity at any fixed carrier", Main:600)
   needs no physical reading and survives under Q2(a). AM-9.2, their bearing on nature: **RX, A1-test**
   (§11, candidate 1).
3. **Recovery.** Not needed for AM-9.1. The fixed-horizon lemma [IR]: per horizon, with each preparation and measurement a
   fixed protocol of finite support over every branch (FS-all), Lemma PM-I gives `N_eff(n)`, the number of data on the enlarged patch,
   so every prepare-and-measure behaviour of horizon `n` factors nonnegatively through `N_eff(n)` states (F-each;
   review C8; EF-1 r6 N3.11 gives the count on the autonomous patch, §20, T19; EF-1 r6 §4.2 now has a row for these obstructions, F-one in the form of one fixed finite model serving every experiment, not carried by F-each, which agrees with this row), a true and very weak statement; AM-9.2's fixed-`N` form
   needs one finite description for every horizon (F-one) and is not carried. For AM-9.2, [IR] what holds without A1 is contrapositive and
   conditional: nature is not exactly operationally quantum through any one fixed finite realization under
   the stated interface; that is a statement about a model class, not a recovery. The validity review
   (N1.6, [IR]) reads the same: the obstruction bears on nature only for repertoires larger than any
   observer's, and A1 leaves `N` unbounded.
4. **Downstream.** Main:60, :356, :486, :496, :556, :558, :562, :600, :638 (open question (b), "by one fixed
   substratum before its recurrence"), :731; Intro:67; `ch18-beyond.md:74` (FULL:4880, row N-5); census 40
   anchors at Main:638.
5. **Treatment.** AM-9.1 RECAST-MATHEMATICAL ("fixed finite realization" kept; Intro:67's "world" becomes
   "model"; Main:356's "The finite physical layer supplies" becomes a statement about fixed finite
   representatives; Main:638 (b) restated without nature's `t_R`, the family 40 anchor phrase kept verbatim).
   Under Q2(b) as reformulated: Main:496, :558, :562 and :600 state the scope of the headline equivalence, so no
   destination outside Main is safe for the statements they cite (§12.2). The paper-only statements (Main:356's
   clause, :486, :496, :556, :558's factorization half; Main:558 cites only a probe script) stay in Main with
   their proofs, at most moved to a Main appendix, and Main:638's kernel-witnessed classification keeps its
   anchors; Main:600 (3) and "Per (3)" follow H2. Separately [IR]: EF-1 r6 (N2.5, N2.9) writes out, with both directions, a candidate
   that bears on Main:638's open question (a), "exact all-time gluing for recurrent families of multi-time laws":
   without inputs, an all-time realization exists exactly for families that are pathwise periodic with one
   common period. It proves existence, not that given per-horizon realizations join; it is a statement of the
   one-description-for-every-horizon kind, which adopted direction c.6896496410 lists as not established here; and it
   changes nothing in this row until it is reviewed (Q15). AM-9.2 REMOVE the
   "bear on nature through it" clause, unless Q9 keeps it as a conditional.
6. **Goal link.** Decides whether the fixed-model obstructions are stated of nature or of the model class.

### AM-10 Statements of the framework's claim that name A1, and framing sites

1. **Results.** Main:14 ("An observer embedded in a finite deterministic system"); Main:718
   (falsifiability: "*the hidden sector is a classical substratum* — a finite set with a deterministic
   bijection, finiteness being the total-finiteness posit"); Main:36, :44, :60 (status Remark), :222 (the
   continuous-spectra paragraph's closing clause, "with the total-finiteness posit (§1.2 Remark, §4.5)
   where a result also needs the hidden sector finite"), :700, :706, :710; GR:20, :705; SM:22, :250, :1592;
   Sub:14, :16, :22, :92, :367, :429, :465; Struct:21, :45, :108, :377, :528, :741; Meth:337, :517; Intro:36;
   Cx:21, :27; Comp:21, :180; `ch19-open-problems.md:212` (FULL:5359); the r9 §7.6 (iii) sites.
2. **Test.** **RW.** Statements, not theorems. Main:718 restates as: the hidden sector is a deterministic
   substratum of undetermined cardinality; every finite-horizon visible law has finite reversible
   realizations (§3.4). Main:44: the load-bearing finiteness is the visible sector's (Lemma 1). Main:700:
   the forward-construction clause is removed and "In the reconstruction direction it is *constructed*" is
   kept. Main:222: the closing clause is restated with the realization's hidden space.
3. **Recovery.** Not needed.
4. **Downstream.** The held change map's 137 sites (papers 67, book 70, 69 FULL mirrors) cover the framing
   family; this audit's removals change some of those sentences further.
5. **Treatment.** RECAST-WORDING, folded into one correction with the held wording commit. Main:718's
   change is substantive (from "a finite set" to undetermined cardinality) on a headline falsifiability
   statement.
6. **Goal link.** Decides the wording of the framework's structural claim under the owner's condition.

## 3. Rows AM-11 to AM-19: companions, book, Lean, records

*Coverage of the site lists.* The sites listed under "Downstream." and elsewhere in this section are those this audit found. They were checked only for existence and for a keyword of the row's subject on the cited line; a site that paraphrases its subject would not have been found, and no list here is claimed to hold every affected site (§21).

### AM-11 Substratum Theorem 23 and Lemma 23.0

1. **Result.** Sub:193 (Theorem 23), Sub:189 (Lemma 23.0); Sub:104–129; Struct:47; GR:342;
   `ch02-substratum.md:88–122` (FULL:722–756); DEPENDENCY-AUDIT.md:287. A1 is a hypothesis of both. Where it
   enters: Stage 1's output "S finite" (Sub:125); the §3.2 forward dilation (Sub:110; AM-5); the slow-bath
   form of C2 necessity (Sub:193; AM-21); Theorem 19's reciprocal counts (Sub:116; AM-30); E3 as "the
   interpretive premise of A1" (Sub:268 (i)); A2's justification (Sub:94; AM-3); `ħ` through Stage 3 (AM-22); the recurrence-cycle sentence of Stage 1's derivation (Sub:137; follows AM-1.1 and AM-1.3b); A4's finite periodic lattice in Stage 2 (a) (Sub:157; Q3); reciprocal transition counts in Stage 2 (f) (Sub:167; AM-30). Changed after review; unreviewed.
2. **Test.** **RC (P12).** Modified statement [IR]: Theorem 23 with A1 replaced by Lemma 1 and E3's bound on
   `C_V × C_B` (Sub:92), Stage 1's output replaced by "a finite reversible realization of the M1-T temporal
   law per accessible horizon" (Main §3.4, A1-free), the §3.2 dilation by P1, C2's slow-bath form by P5b,
   reciprocity by P6, and Stage 3 by P7. Census 53 records the kernel negative `cx3b_complex_not_A1`
   (`A6Instantiation.lean:512`, kernel-only); [IR] whether the gauge-sector stages are carried on it is not
   traced. The validity review (G2, [IR]) reads E3 as a dimension cutoff as in conflict with the
   framework's own volume-law lattice; P12 does not rely on E3 for any finiteness beyond `C_V × C_B`.
   **Lands as**: a class theorem for the restated class; whether it excludes a visible law is not traced
   here [IR].
3. **Recovery attempt.** Gap: Stages 2(a)–(e) and 3 are not traced for A1 (r9 §7.4); Lemma 23.0 compares
   two A1–A6 substrata and must be restated for substrata of undetermined cardinality; A2 is Q5. Unit P12
   after P1, P5b, P6, P7. Its premises are those of its inputs: the class definition (Q3), Q5, Q6, and,
   through P7, Q1(b-mode) [IR; r2 listed Q3, Q5, Q6].
4. **Downstream.** Sub:104–129, :189, :193, :205–223, :268; Struct:47, :646, :1100; GR:342; Meth:339–369
   (AM-24); `ch02-substratum.md:88–122`; `ch04-methodology.md:210` (FULL:1318); `README.md:54`;
   DEPENDENCY-AUDIT.md:287. Census: no Theorem 23 anchor found [IR].
5. **Treatment.** RECOVER (P12). If not recovered, Theorem 23 stays conditional on A1, which the owner's
   condition does not permit, and the reconstruction would be stated on finite models only (finite tori,
   G-fam), which changes the synthesis claim's subject.
6. **Goal link.** Decides whether the SM reconstruction is stated for a substratum of undetermined
   cardinality.

### AM-12 Theorem 24 (i), (iii), its Corollary, Proposition 9.5

1. **Results.** Sub:251–268; Struct:646. (i) hidden relabelling with `ω_H = 𝟙/|C_H|` (Sub:253); (iii)
   adjoining a finite decoupled factor (Sub:262); Corollary (i): E3 "is the interpretive premise of A1"
   (Sub:268). (ii) not traced; (iv) not a consumer.
2. **Test.** **RU.** (i) and (iii) state what the visible law does not depend on; as stated, they exclude no law.
   (iii)'s argument (Main:60: "the visible coordinate of the product map does not depend on the added
   coordinate and the added prior has total mass one") uses no total finiteness of the original hidden
   sector; (i) as stated is for the uniform prior on a finite `C_H`, that is, for a realization's hidden
   sector. P11 [needs proof, routine] extends (iii) to any normalized decoupled factor and (i) to
   relabellings preserving a stated normalized prior; that extension is a conditional theorem, and its
   application to nature's infinite deep sector needs the normalized prior to be true of nature, a Q6-type
   premise (review F16 (c)). Corollary (i): E3 bounds `C_V × C_B` (Sub:92); the validity review (G2, N3.1)
   reads "interpretive premise of A1" as unsupported [IR].
3. **Recovery.** P11 optional. [IR] EF-1 r6 Lemma PM (b), (c), applied at each horizon: under any normalized initial law, sites outside
   `U_∞ = ⋃_n U_n` enter no finite-horizon observation law, an infinite-factor form of (iii). It is a
   comparison between carriers, so it needs equal patch marginals (a product form with the same patch
   factor suffices: a further distributional property, D1, with its own justification) and belongs downstream
   with GR:112 and GR:132 (EF-1 r6 N1.6). A candidate; no recovery credit.
4. **Downstream.** Sub:251–268; Struct:646; GR:138; Main:60, :724 (ii).
5. **Treatment.** RECAST-REPRESENTABILITY (Corollary (i) loses "of A1"). Nothing breaks.
6. **Goal link.** Decides how the unobservability of a decoupled deep factor is stated without A1.

### AM-13 Comp:118, the finite-size consequence

1. **Result.** A proposal conditional on the patch-budget hypothesis and stated conjectures; "The
   total-finiteness posit ... takes S finite."
2. **Test.** **RW** [IR]: the patch-budget hypothesis already caps the observed patch's resources; the A1
   sentence adds nothing the proposal uses.
3. **Downstream.** Comp:118 and its §4.3 references; `ch14-quantum-computing.md` §14.4 (not traced by line).
4. **Treatment.** RECAST-WORDING: delete the A1 sentence (Comp:118 is one of the ten by-name sites, §9; found by search, not claimed complete).
5. **Goal link.** Housekeeping: decides whether the proposal states A1.

### AM-14 GR boundary-only dependence lemma and deep-sector corollary

1. **Result.** GR:112–114 (lemma, "a finite product of site configuration spaces", uniform hidden prior);
   GR:132–138 (corollary; its first statement "holds also for an infinite deep sector, given a normalized
   product prior on it, a locally finite coupling graph and well-defined dynamics", proof GR:134).
2. **Test.** **RU** for the corollary's first statement: no quantity determined by the visible transition
   data on `[0, nΔt]` depends on the cardinality of the hidden sector beyond the cone `B_n`. As stated, it excludes no
   law. Its infinite form needs a normalized product prior on the deep sector (a Q6-type premise if read of
   nature) and a locally finite coupling graph (P3's hypothesis, Q8); its subject is the cone sector
   (Q1(b-loc)). The validity review (G1, [IR]) adds that what is gauge is `|C_{D_n}|`, not the influence of a
   deep sector the cone has reached, and that the deep prior must be independent of a uniform cone prior.
   The H-BD statement (`O(t/τ_BD)`) is stated "for every finite deep sector", and the lemma itself is a
   finite-model statement.
3. **Recovery.** Not needed. [IR] This row is the tool for P7, P8-S and the AM-6 note. EF-G1 (EF-1 r6 N1.4): the visible law on `[0, n]` depends on the initial law only through its marginal on the
   cone, for every normalized prior; a product prior is needed only to make two carriers' cone marginals
   equal. So the corollary's product hypothesis is a condition of the comparison, not of locality, and P9
   no longer needs it (AM-31).
4. **Downstream.** GR:138, :585; Sub:92, :262, :268; `ch18-beyond.md:170` (FULL:4976).
5. **Treatment.** RECAST-REPRESENTABILITY (GR:138's "the recurrence proof requires S finite" follows
   AM-1.3b). Its physical reading, and its use as a tool, are gated on Q1(b-loc), Q6 and Q8.
6. **Goal link.** Decides which A1-free tool the GR recoveries use.

### AM-15 Methodology on A1 (mirror; no own count)

Meth:156, :158, :166, :253, :261 follow AM-1.3b and AM-3.2: rung 6 becomes injectivity on registered content
(the TD requirement of AM-3.1) plus bijectivity of constructed realizations by construction; "together with
finiteness of the total space, which is A1" (Meth:158) is removed. Meth:162, :283 follow AM-8.

### AM-16 SM finite-torus theorems and counting-measure results

1. **Result.** SM:294–296, :1606 (finite torus, cycle structure of the exact linear rule); K
   `waveSubstratum_A1` (`SubstratumInterfaceAudit.lean:185`, census 15, kernel-only), `hexSubstratum_A1`
   (`HexLatticeGas.lean:312`, census 49, kernel-only).
2. **Test.** **RM**: theorems about finite models (G-fam); the kernel results prove that finite tori satisfy
   the kernel predicate `A1 := Finite Conf` (`SubstratumInterfaceAudit.lean:84`), a property of the models.
3. **Downstream.** SM:294–296, :1225, :1227, :1606, :1654.
4. **Treatment.** RECAST-MATHEMATICAL: the scope is "the finite-torus model", not "OI's substratum". Under
   Q2(b) SM:296's cycle-structure remark (a paper derivation; census 15 and 49 prove only the `A1`
   predicate for the models) stays in SM §4.2 with its derivation, reframed (§12.2), and the kernel results stay (§A.46 item 6).
5. **Goal link.** Decides how the finite-torus results are scoped.

### AM-17 Book mirrors and framing (no own count)

Each book site takes the treatment of the row it mirrors, with its FULL line (§A.14). `glossary.md:11` and
`readers-guide.md:79` name "the finiteness posit" in topic lists and follow AM-10.

### AM-18 Verification records (no own count)

DEPENDENCY-AUDIT.md:281–291 (audit record; review independence not established, :17–19) and
`continuous-substates/` (RR). Context only; a correction goes by the record's own route (§A.42 item 6;
§A.46 item 4).

### AM-19 The phase-locking lemma (Main:228–260)

**RU.** A finite-dimensional identifiability statement on `C^n`, `n` from Lemma 1, under (G1)–(G4) (Main:228);
its substratum application runs through AM-5 (P1). Census 2 (`ShellAssignment`, GR:174–210, anchor Main:242)
not touched. Treatment: RECAST-REPRESENTABILITY (no change). Goal link: decides whether the lemma uses any
hidden-sector finiteness.

## 4. Rows AM-20 to AM-26

*Coverage of the site lists.* The sites listed under "Downstream." and elsewhere in this section are those this audit found. They were checked only for existence and for a keyword of the row's subject on the cited line; a site that paraphrases its subject would not have been found, and no list here is claimed to hold every affected site (§21).

### AM-20 The characterization theorem

1. **Results.**
   - AM-20.1 The law-level content: (ii) ⟺ (iii), and (i) under (T) (Main:536–544). Directions sourced
     separately (§A.34): (ii) ⇒ (iii) constructively per horizon (Main:516–520, status row Main:731);
     (iii) ⇒ (ii) by the readback lemma (status row Main:733). A1 enters only through "on accessible
     timescales `t ≪ t_R` where `t_R` is the Poincaré recurrence time of any realizing substrate"
     (Main:536) and "`k τ_S ≪ t_R`" (Main:540).
   - AM-20.2 The physical reading: "the identification of nature with a finite reversible substratum"
     (Main:60).
   - AM-20.3 The bare-recurrence form (Main:733) is AM-1.1 (counted there).
2. **Test.** AM-20.1: **RU** (review F1). Read one direction at a time, it says that a law has memory at an
   accessible order exactly when it has, per horizon, a finite reversible realization with C1, C3 and C4
   (Main:542). Every law either has such memory or not, so the theorem classifies laws by
   representability over the memory class and, as stated, excludes none ("representability alone does not
   distinguish", Main:18). The qualifier is restated as "at some accessible order `k` within the accessible
   horizon". [IR] Both directions are per finite horizon and do not use `t_R`; this is a check (P15), not a
   new proof. AM-20.2: **RX**.
3. **Recovery attempt (AM-20.2).** None possible: it is A1 stated as an identification. Main:60 already
   gives the law-level equivalence "for every finite-horizon law".
4. **Downstream.** Main:18, :60, :80 item (2), :536–544, :626, :731, :733; Cx:374; Sub:112; GR:585;
   `glossary.md:105` (FULL:6689); `preface.md:3` (FULL:64); `ch01-observation.md:201` (FULL:536);
   `appendix-b-derivations.md:451–454` (FULL:6205–6208).
5. **Treatment.** AM-20.1 RECAST-REPRESENTABILITY (qualifier reworded; P15). AM-20.2 REMOVE (Main:60's
   sentence keeps only its law-level clause). No count changes.
6. **Goal link.** Decides how the characterization theorem's timescale qualifier is stated without `t_R`.

### AM-21 The C2-necessity theorems

1. **Results.** Quantitative mixing form (Main:453–463), physical-memory process form (Main:467–471),
   persistence form (Main:469), mechanism (Main:445–449), slow-bath remark (Main:502). Each is stated for
   "the uniform-prior bijection marginal of §3.2's construction" (Main:453), with `T` as the benchmark ("the
   reference prior defining `T`", Main:449, :453; `T` is AM-4.2's), and the mechanism cites recurrence "at
   `t_R` exponentially large in the system size" (Main:445) and "recurrence only at `t ∼ t_R`" (Main:449).
2. **Test.**
   - AM-21.1 Persistence form: **RC (P5a)** [IR]. Statement [needs proof, routine]: for a deterministic
     coupling step with any measurable hidden space and any reference prior `π_H`, with `ε` the realized
     maximum of `TV(P(H_k = · | x_{≤k}), π_H)`, observed `M_k > 0` forces `ε ≥ ε_min(M_k, n_V)`. Total
     variation contracts under Markov kernels (the `k = 2` step of Main:463 with sums replaced by integrals);
     the telescoping is unchanged; Fannes–Audenaert needs only `n_V` finite (Lemma 1). The validity review
     (N1.3, [IR]) reads the same. **Lands as TD**: an implication from visible memory to nature's hidden
     conditionals; as stated, it establishes no constraint on the visible law.
   - AM-21.2 Mixing and process forms: **RC (P5b)**: the same bounds with `ε` read as the residue of
     relaxation toward `π_H`; the physical reading needs `π_H` to be a physically selected reference prior
     toward which the hidden sector relaxes (Main:453, :469), a premise of the posit (iv)/(v) kind (Q6).
     **Lands as TD** under Q6(c) [IR]; the bound `‖T^{(k)} − T^k‖_TV ≤ (k−1)ε` could establish a constraint on the visible
     law only together with an independent bound on `ε`. Optimality (Main:463) is a finite example and stays.
3. **Recovery.** P5a (as a conditional theorem; asserted of nature it needs a joint law, L9, so the row is NEW under the one rule of §0); P5b (gated on Q6). The mechanism paragraph (Main:445–449) is narrative:
   its `t_R` clauses are restated for a realization or deleted. Both recoveries state `T` from `π_H`, so they
   do not depend on AM-4.2's uniform-prior text; if Q2(b) removes that text, `T`'s definition from `π_H` is
   written in the same change.
4. **Downstream.** Main:180, :445–502, :536, :724 (v); Sub:112, :129, :193; the C2 sections of
   `ch01-observation.md`; `ch13-quantum-biology.md`, `ch15-quantum-engineering.md`, `ch16-medicine.md` and
   Cx, which use the `τ_S/τ_B` reading (not traced by line).
5. **Treatment.** AM-21.1 RECOVER (P5a); AM-21.2 RECOVER (P5b, gated on Q6). If P5b fails or Q6 adopts no
   premise, the slow-bath necessity stays a theorem about coupling-step models with a stated reference
   prior, and Theorem 23 loses its stated C2 input (AM-11).
6. **Goal link.** Decides whether C2's necessity bears on nature's hidden sector or only on models.

### AM-22 GR:58 and GR:70: counting temperature and thermal rate ratio

1. **Results.** GR:58 ("Restrict the finite total system to a conserved energy shell ... uniform counting
   gives `P(i) = Ω_H(E−e_i)/Σ_j Ω_H(E−e_j)`", under H-count); GR:70 (`N_ij = N_ji` from time-reversal
   invariance; "the thermal rate ratio from finite deterministic reversible counting"); framed by GR:28.
2. **Test.** **RC (P7)** [IR]. Statement: the same on the energy shell of `C_V × C_B`, the boundary layer finite
   by the boundary mode count `A/ε²` (GR:90; S3 at GR:665; a GR premise, not A1, and not available in Main,
   Main:700), with the deep sector a normalized factor carrying no energy-dependent multiplicity (H-count's
   own content, GR:58); exact when the deep sector is decoupled (Theorem 24(iii); Main:60), to `O(t/τ_BD)`
   under H-BD. [needs proof]: for GR:58, that the uniform prior on the boundary shell times the deep
   normalized factor gives `P(i)`; for GR:70, that `N_ij = N_ji` holds on the boundary shell, which needs the
   restricted dynamics to be a time-reversal-invariant bijection of that finite shell, exact only for a
   decoupled deep sector. Consistency: the validity review (G7) finds that energy-shell priors are not
   product priors, so the gauge statements do not cover them, and that the only replacement is an
   infinite-carrier restatement of H-count with a shell measure; P7 is such a restatement and is not on
   `main`. The validity review (AW-4, [IR]) also records that H-BD fails for the framework's own linear rule
   at cuts with deep-boundary coupling (GR:128), so P7's H-BD branch may be vacuous on the selected model.
   **Lands as CV** under its premises: the rate ratio and the counting temperature tie measurable transition
   rates to energies. The fixed-horizon lemma does not carry it (EF-1 r6 N3.7) [IR]: the cone sector is not
   self-contained and has no energy shell, and shells on growing tori stay consistent only at a stated
   energy density, in a Gibbs-type limit that is not a product prior. The proof needs an invariant shell measure of a bijection of a finite carrier, which (M-full), a statement about the uniform product measure, does not concern (EF-1 r6 §4.2). GR:68 adds that the relation reduces to `N_ij = N_ji` "only when the coarse states are time-reversal even"; that condition, and the negligible boundary interaction of GR:58, are carried by P7. The form of the weights comes from shell counting (GR:58), not from H-count. Changed after review; unreviewed.
3. **Recovery attempt.** Strongest existing results: GR:132's infinite form; the finite-factor invariance
   (Main:60; Sub:262). Gap: GR:70's microreversibility on the boundary shell when the deep sector couples;
   H-BD gives a correction to the transition law, not an exact count identity [IR]. DEPENDENCY-AUDIT.md:289
   records the same item. Premises: uniform counting on the shell (Q6), a time-reversal bijection on the
   shell (Q5), the boundary-layer reading of the condition (Q1(b-mode)).
4. **Downstream.** GR:28, :58–70, the calibration `ħ = c³ε²/(4Gσ)`, `ε = 2√σ l_p` and the 1/4 coefficient
   (GR:28; GR:669), (U1) (AM-36), Sub:189 and :193 (Stage 3), Lemma 23.0;
   `appendix-a-prediction-status.md:117` (FULL:5641) and the G2/G5 rows' horizon conditions; book Chapter 7
   §7.3–§7.5.
5. **Treatment.** RECOVER (GR, P7, gated on Q1(b-mode), Q5, Q6(c)). If P7 fails, the classical half of the horizon
   calibration loses its counting link and the `ħ` calibration, the 1/4 coefficient and Theorem 23's Stage 3
   become conditional on a premise the owner's condition excludes.
6. **Goal link.** Decides whether the GR horizon calibration's counting link survives without A1 (#1169
   comment 6894553525, #1309 row).

### AM-23 Super-BQP and infinite-time computation

1. **Results.** AM-23.1 Comp:100: super-BQP capabilities "would require either continuum precision
   (violating A1), unbounded coupling (violating A3), operations outside the operational-closure model ...,
   or violation of these efficiency hypotheses". AM-23.2 `ch14-quantum-computing.md:90` (FULL:3756):
   "infinite-time computation requires actual infinity, which the framework's finite substratum precludes
   (a structural exclusion)".
2. **Test.** AM-23.1: **RW** [IR]: the efficiency hypotheses already require "polynomial physical time at
   polynomial precision"; accessible registers are finite by Lemma 1; the A1 leg is redundant (the validity
   review, G6, attributes the continuum-precision exclusion to finite site alphabets with the discrete,
   locally finite site structure, not to finitely many sites [IR]). AM-23.2: **RC (P16)** [IR]. The sentence on `main` gives no proof; its stated ground is the
   finiteness of the substratum ("which the framework's finite substratum precludes"). Candidate route for a
   restricted statement: by EF-1 r6's Lemma PM-I (provisional), the visible record up to step `t` is a
   function of the initial data on a patch and of the inputs applied, with the inputs the same in the runs
   compared or the adaptive policy and its information included (§0), so no visible output at a finite step
   depends on infinitely many sites or computation steps, provided that patch is finite. *Which form.* The
   sentence is one description of the output for every input rule and every run, so it needs the
   **all-branch** form, under FS-all. The per-run form gives each run with finite reads a finite patch of its
   own, which is not a description of the output as a function of the initial data (EF-1 r6, examples E1–E3).
   Lemma K gives one patch, with no bound on its size, from finite reads on every run, under the lemma's
   other hypotheses (a finite alphabet at every site; finitely many values of the policy information); as
   named hypotheses these could stand in place of FS-all. The per-run form, Lemma K and the clause that lets
   an input rule remember its earlier reads were checked by the review of EF-1 r4; the class below is the
   same on either set of hypotheses. *From the finiteness premises it needs:* finite reading sets (L1) and finite
   site alphabets (L2), whose source is the undecided reading of Q8; a finite visible region with a site-local
   readout (L8) and inputs of finite support over every branch (FS-all), neither a separately stated premise
   on `main` (EF-1 r6 §4.0, where both are flagged), which this audit treats as named hypotheses of the
   restated sentence [IR]; and one protocol shared by the runs compared. *From the probability premise:*
   nothing; the statement is pointwise. *Further distributional property:* none. **F-each, all-branch form.
   CONTINGENT (Q8). A candidate; no recovery credit.** Limit:
   it excludes infinite-time computation within finite time, not a non-computable bit carried in the
   initial data on the cone (an oracle), which A1 does not exclude either. **Lands as TD** [IR]: since
   oracle initial data are not excluded, it establishes no constraint on visible laws (no proof is on
   `main` that every visible law is reproduced with oracle data).
3. **Downstream.** Comp:100; `ch14-quantum-computing.md:18`, :40, :42, :90, :140; `README.md:82`;
   `ch00-introduction.md` and `glossary.md` super-BQP mentions; `appendix-a-prediction-status.md` A.6.
4. **Treatment.** AM-23.1 RECAST-WORDING (drop "violating A1"; cite Lemma 1 and the precision hypothesis).
   AM-23.2 RECOVER (P16, uses P3, gated on Q8); if not recovered, REMOVE the structural exclusion. The BQP
   ceiling is unaffected.
5. **Goal link.** Housekeeping: decides whether the hypercomputation exclusion is stated without A1.

### AM-24 Methodology's constructive-OSR claim (Meth:339–369)

Inherits AM-11: **RC (with P12)**, gated on Q1, Q3, Q5, Q6; lands as AM-11 (untraced). "within the
nearest-neighbor A1–A6 class" (Meth:367) is restated with the class redefined (Q3). Downstream: Struct:1100,
`ch04-methodology.md:210` (FULL:1318), `README.md:54`. Goal link: decides whether constructive structural
realism is claimed for a substratum of undetermined cardinality.

### AM-25 Lean, carrier 3: census 15 and 31 (kernel-only)

**RM.** `obsTheory` (`SubstratumInterfaceAudit.lean:764–800`) and `obsTheory_nonnegBounded`
(`FrozenSourcing.lean:84`) are theorems on finite-torus substrata (finite site group and alphabet,
translation rule; `SubstratumInterfaceAudit.lean:60–66`). No manuscript anchor and no manuscript statement.
Treatment: RECAST-MATHEMATICAL; unchanged under either answer to Q2 (§A.46 item 6); no census change. Goal
link: decides the stated scope of the carrier-3 kernel results.

### AM-26 MR-1 preregistration (record; no own count)

`verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md:260`, :361,
:372 cite the posit as kinematics. Research-only record; correction by its own route (§A.42 item 6, §A.46
item 4).

## 5. Rows AM-27 to AM-38

*Coverage of the site lists.* The sites listed under "Downstream." and elsewhere in this section are those this audit found. They were checked only for existence and for a keyword of the row's subject on the cited line; a site that paraphrases its subject would not have been found, and no list here is claimed to hold every affected site (§21).

### AM-27 Sourcing negatives and monomial-class results on finite carriers (EXACT)

1. **Results.** Main:588 (the substratum-source form: "the concrete OI substratum supplies the structural
   architecture ... but, under finite bijective read-write dynamics, not the continuously tunable
   state-mixing operation", with `substratum_plus_control_qm` and its converse
   `qm_generated_by_substratum_extension`; the layer-flow sentence with `derivedOI_qm_iff_layerFlowExecutable'`
   and `substratumTheory_not_layerFlowExecutable`; the observer-access sentence with
   `obs_not_layerFlowExecutable` and `coherentLiftClass_eq_substratumClass`); Main:80 item (4) (the negative
   clause, kernel `substratumGen_not_control` on the two-state carrier); GR:224, :256–274; Intro:129; book
   mirrors `ch01-observation.md:165` (FULL:500) and `ch19-open-problems.md:126` (FULL:5273).
2. **Sorted by kind (review F12; Lean source read).**
   - (α) **Definitions**, which state nothing: `substratumClass` (`StructuralClosure.lean:180`, `def`, the
     monomial class), `substratumTheory` (`RouteB.lean:284`, `abbrev`, the theory it generates).
   - (β) **Theory-general results that do not consume A1**, moved to §6: `derivedOI_qm_iff_layerFlowExecutable'`
     (`DerivedQ3.lean:222`, for any `FiniteOperationalTheory` with `DerivedOI`; necessity through
     `layerFlowExecutable_of_control`, sufficiency through `qm_of_derivedOI_layerFlowExecutable`, each
     direction witnessed separately, §A.34); `layerFlowExecutable_of_control` (`LiftAudit.lean:117`, any
     theory with composite unitary control); `genTheory_qm_of_quantumArchitecture` (GR:256, any quantum
     architecture). They never mention the monomial class. Kept under either answer to Q2; the substratum
     wording of their sentences ("within the substratum's closure", GR:264) is re-scoped to the closure
     `DerivedOI` they assume.
   - (γ) **Monomial-class facts**, true on every finite carrier of the stated size: the class identity
     `coherentLiftClass_eq_substratumClass` (`LiftSource.lean:164`); the positive
     `substratumClass_not_onesFixing` (`PhaseSource.lean:200`: the phase intervention is admissible and moves
     the all-ones ray, witnessed at `Fin 2`); the characterization `substratum_plus_control_qm` with its
     converse (two directions, §A.34); `substratumGen_not_control` (two-state carrier).
   - (δ) **The carrier-general sourcing negative**: `substratumTheory_not_layerFlowExecutable`
     (`LiftAudit.lean:200`, any `σ` with a moved point, so `|S| ≥ 2`).
   - (ε) **Observer-theory statements on `Substratum`**: `obs_not_layerFlowExecutable` (`ExecSource.lean:129`,
     `[Fintype 𝒮.ι] [Fintype 𝒮.V]`) and the `obs_*` family, on finite-torus substrata only.
3. **Test.**
   - AM-27.1, (γ) and (δ): **RM**. [IR] Their bearing on nature needs nature's available operations on a
     finite accessible carrier to be monomial; `main` derives that from finite bijective read-write dynamics
     of the whole carrier (Main:588). With an infinite hidden sector the operation induced on a finite
     accessible carrier is a channel obtained by tracing out, not monomial in general.
   - AM-27.2, (ε): **RM**, on finite-torus substrata only.
   - The nature-level negative needs an infinite-region form (P14, the quasilocal completion; optional,
     [needs proof]). A negative is stated only for the class it rules out (Code Review Rules).
4. **Downstream.** Main:80 item (4) (H1, §8), :588; GR:224, :256 ("The concrete OI substratum — finite states
   and bijective microscopic dynamics"), :258–274; Intro:129; ch01:165 (FULL:500); ch19:126 (FULL:5273).
   Census families 5, 6, 7, 8, 10, 11, 14, 19, 20, 21, 22 (current) and kernel-only 18, 23–27, 29: §10. Family 7
   (`typed_determined_iff`, `typed_determined_of_oiPlusPos`, GR:272) lies inside the GR:256–274 range this row
   rewrites; its identifier anchors are kept under either answer (the typed paragraph proper is
   carrier-general [IR]).
5. **Treatment.** RECAST-MATHEMATICAL: scope "on every nonempty finite carrier with the monomial class"
   (AM-27.1) and "on every finite-torus substratum" (AM-27.2); the physical reading ("the concrete OI
   substratum ... supplies", "does not itself generate") is restated as a statement about that class. Main:80
   item (4)'s negative clause leaves the theorem statement (H1) and is replaced by "whether nature's available
   operations supply (iv) is open", with the monomial-class negative stated in §3.4 under Q2(a). Under Q2(b),
   (γ), (δ) and (ε) leave the manuscripts; (α) stays wherever kept text uses it; (β) stays. Every census anchor
   phrase in kept text is kept verbatim or the registry is updated in the same commit (§10). P14 optional.
6. **Goal link.** Decides the stated scope of the EXACT sourcing negatives (carrier 3).

### AM-28 Routed readback: the forcing theorems (Main:145; census 35, 36)

**RM.** Main:145 carries three kinds of content (r3 review B3). (1) The two formalizations of (C4)'s
realization clause (storage-time and seed-conditioned readings), definitions of the clause the
characterization theorem's (iii) quantifies over; (2) the two separations, "Neither reading implies the
other: each holds at `K = 2` on an exhibited finite reversible realization on which the other fails"
(`storageReadback_not_implies_routedReadback`, `PhysicalC4StorageReadback.lean:488`;
`routedReadback_not_implies_storageReadback`, :689), proved on exhibited carriers with no period, return or
recurrence; (3) the forcing theorems (`routed_forces_*`, `routedAtStorage_forces_*`), which use a return
`Γ_n = I` or the period `rootedMap_periodic`. Parts (1) and (2) are A1-free and realization-level; they
move to §6 and are kept under either answer to Q2. This row is part (3): "and so for some `n`, because
`(Γ_t)` is periodic" is a property of a finite realization; its visible content is AM-1.2. Treatment:
RECAST-MATHEMATICAL; under Q2(a) the anchors at Main:145 are unchanged; under Q2(b) the forcing sentence is
withdrawn (the kernel keeps it) and the registry drops the four forcing-identifier anchors of families 35
and 36 in the same commit, while family 35 keeps "in the seed-conditioned reading it is that of the initial
hidden state" and family 36 keeps "In the storage-time reading the hidden law is that of the hidden state
at the storage time" and both separation identifiers, so both stay carried [IR, conditional on the
correction keeping those sentences] (§10). Goal link: decides whether C4's realization clause is stated of
nature or of realizations.

### AM-29 Census 32, the stochastic observer interface (kernel-only)

**RM**: on finite sites and alphabet (the `Substratum` structure). r9 records [IR] that the underdetermination
carries to the OBL class (support off `main`). No anchor and no manuscript statement. Treatment:
RECAST-MATHEMATICAL; unchanged under either answer to Q2. Goal link: decides the stated scope of the census 32
result.

### AM-30 SM Theorem 19, reciprocity

1. **Result.** SM:641–643; K `theorem_19` (`Reciprocity.lean:129`, the count form with `Fintype.card H`;
   census 1 anchor at SM:643); a dependency of Theorem 23 (Sub:116). A1 enters at "Dividing by `|C_H|`".
2. **Test.** RM for a finite realization with the counting prior (K). **RC (P6)** for a measurable hidden
   space. Statement [needs proof, short; P6]: if `φ` is a bijection of a measurable carrier `C_V × C_H`,
   T-invariant (`φ^{-1} = 𝒯 φ 𝒯`, Theorem 17), (counting on `C_V`) ⊗ `μ_H` is `φ`-invariant and `μ_H` is
   `θ_H`-invariant, then `T_ij(n) = T_{θj,θi}(n)` for all `n` (the review verified the `n = 1` step and the
   step to every `n` through `φ^{-n} = 𝒯 φ^n 𝒯`). Hypotheses: bijectivity and T-invariance on the infinite
   carrier (Q5); `φ`-invariance of (counting) ⊗ `μ_H`, [IR] a W3-type premise of the paused AM-3 unit (Q6).
   Both are premises; §A.29 applies if adopted. **Lands as CV** under those premises: if proved, it would
   establish a constraint, excluding visible laws without the reciprocity.
3. **Downstream.** SM:641–643 and its uses (13 "Theorem 19|reciprocity" hits in SM); Sub:116;
   `ch06-matter-content.md` (3 hits), `ch00-introduction.md`, `ch04-methodology.md`, `ch18-beyond.md`,
   `ch19-open-problems.md` (not traced by line).
4. **Treatment.** RECOVER (SM, P6, gated on Q5 and Q6), needed by AM-11. The kernel identifier stays, cited
   for the counting-prior statement it proves (§10, family 1).
5. **Goal link.** Decides whether reciprocity is stated for a hidden sector of undetermined cardinality,
   and on which premises.

### AM-31 SM Theorem 22, genericity of observers, and its Corollary

1. **Result.** SM:1376–1388 (and SM:52, :92); `PhysicalC4Discharge.lean:574` (`Cut` section, kernel-only part
   of census 35). A1 enters through `|V| ≤ N/3` on a finite graph and `log₂|C_H| = |H| log₂ q` (SM:1382);
   Corollary SM:1388: "Any finite deterministic system ...".
2. **Test.** **RC (P9).** The row has three parts (review C4).
   - **(1) C1 genericity.** On a connected bounded-degree coupling graph of any cardinality, every proper
     connected subgraph `V` (finite by Lemma 1) satisfies C1: the proof at SM:1378 uses no finiteness.
     FIRM, no premise beyond the theorem's own graph hypothesis.
   - **(2) The C3 clause as stated**, "the C3 capacity floor holding for the realized process by the
     data-processing bound $I^* \leq \log_2|\mathcal{C}_H|$ ([Main §3.4])" (SM:1376). It is Main:512's
     corollary, with Main:608 (c) its one-step form (kernel-only witness for a finite hidden space:
     `fullFutureIstar_le`, `FullFutureMemory.lean:104`, census 112) [IR]. It holds for every faithful
     finite realization without A1. For a hidden sector of undetermined cardinality it is true and, when
     that sector is infinite, vacuous. FIRM, no premise; but for an infinite hidden sector it then says
     nothing.
   - **(3) A per-horizon cone bound** [needs proof, including its form]. The proof on `main` uses the
     absolute hidden count, `|H| = N − |V| ≥ 2N/3` and `log₂|C_H| = |H| log₂ q` (SM:1382), and data
     processing through the hidden state at time `t` (Main:610 (c)). Neither is carried by the
     fixed-horizon description: absolute hidden cardinalities are not preserved, and the patch has no
     self-map and so no hidden state at time `t` (EF-1 r6 §P). What the description does give [IR, one
     line, not checked by a review]: the history on `[0, n]` is a function of the patch datum, so, given a
     starting law, `I(X_{<t}; X_{>t} | X_t) ≤ H(X_{0:n}) ≤ log₂|C_{U_n}|` for the future truncated at `n`;
     whether the visible sites can be left out of the count is part of the proof. *From the finiteness
     premises it needs:* finite reading sets and a finite subgraph `V` (both hypotheses of
     Theorem 22 itself, SM:1376) and finite alphabets (L2). *From the probability premise:* it needs a normalized starting law
     (L9; EF-1 r6's P1), since the bound is on an information quantity. *Further distributional property:* none; no
     product prior is needed (EF-G1). **F-each**, and only for the truncated quantity: `I*` is a supremum
     over every time (Main:512), and a finite bound on `I*` itself is an F-one statement.
     **Standing of part (3): a replacement part that needs L9.** L9 is not a reading of ledger item (iv), which asserts a selection
     ("the measure selection is a maximal-entropy principle", Main:724); no text on `main` asserts a
     normalized law on a carrier of undetermined cardinality except as the hypothesis of a conditional
     (GR:132: "given a normalized product prior on it"; Sub:262: "an infinite extension requires its own
     normalized measure or trace-class state and a well-defined evolution, and is not established by
     finite uniform counting"). It is a replacement of item (iv) for nature (Q6(d)), judged like any
     premise (Q11(a), §A.29). The review of r4 labels the same part "contingent on Q6(d)"; both positions
     are in §14.1 and §20 (D1). Part (3) is also a restatement, not a recovery, of the C3 clause's content
     for an infinite hidden sector: it bounds a horizon-`n` truncation by a count that grows with `n`
     [IR].
   - **Row.** Parts (1) and (2) keep Theorem 22 as stated, with no premise beyond those on `main` (FIRM under the one rule of §0). Part (3) is new content: a replacement part for an upper bound, conditional on a starting probability law (K2); it is not a recovery and is counted in no class. r6 counted the row NEW by part (3); both positions are in §20. Changed after review; unreviewed. If Q6(d) is declined, part (3) is not stated and the row is kept
     in parts (1) and (2) only. A candidate; no recovery credit. SM is downstream of Main either way.
     **Lands as** TD for (1); RU for (2); TD for (3), with a CV part only together with L10 and only where
     the bound is tighter than the bound from the visible record itself, `min(t, n−t)·log₂|C_V|` [IR; not checked].
3. **Downstream.** SM:52, :92, :1376–1388; Medicine:31, :98 (C3 mirrors).
4. **Treatment.** RECOVER (SM, P9): parts (1) and (2) need no premise; part (3) waits on Q6(d) with Q11 and
   Q1(b-loc). The Corollary's "Any finite deterministic system" becomes "any deterministic system with a
   finite visible sector" and follows parts (1) and (2).
5. **Goal link.** Decides whether observer genericity is stated without A1.

### AM-32 SM finite-ring and finite-torus statements and mirrors

**RM** for the models: SM:112, :1654 (G-fam). SM:22 follows AM-10 (wording); SM:44, :236, :308 follow AM-1 and
AM-3; SM:336 follows AM-4.4. Treatment: RECAST-MATHEMATICAL; under Q2(b) SM:112's explicit construction and
SM:1654's marginalization argument, for which no kernel counterpart was identified [IR], stay in SM (§3.1, Appendix A)
with their arguments, reframed as model statements (§12.2). Goal link: decides how SM's model statements are
scoped.

### AM-33 GR Appendix A.7–A.9: purity, cycle typicality, cycle-averaged Page curve

1. **Results.** Setup GR:715 (finite `C_V`, `C_B`, `C_D`, a bijection); A.7 (GR:791); A.8 (GR:797–809, finite
   cycle decomposition of `Σ_E = C_B × C_R`); A.9 (GR:835–839); GR:605, :861.
2. **Test.**
   - AM-33.1 A.7: **RC (P10).** [IR] The proof (GR:791) uses injectivity of `φ_t`, finitely many basis terms
     over `C_V × C_B`, and a Schmidt decomposition across the finite-dimensional factor `VB`; all hold in
     `ℓ²(C_D)` for an index set `C_D` of any cardinality, with `U_φ` an isometry. No countability hypothesis is
     needed (the review confirmed). "The total system evolves unitarily" needs bijectivity; the proof needs
     injectivity on the whole carrier, including the hidden sector (Q5). **Lands as TD**: a statement about the
     joint `VB` state with the hidden `B` (Q11's kind).
   - AM-33.2 A.8, A.9: **RM** (review F2). GR:787 says Theorems A.8–A.9 treat `B ∪ R` as an isolated system on
     which `φ` acts as a bijection of `C_B × C_R`, under H-decouple, which is "not established here" (GR:787; GR:795 states the condition);
     A.8's proof uses "Since `Σ_E` is finite" for the cycle decomposition (GR:807); A.9's averages are
     full-cycle averages (GR:839); the subsystem's size is set by the mode counts (`n_B(0)` modes of
     dimension `q`, GR:835). `B` is the black-hole interior, a hidden sector, not GR §3.2's boundary layer
     `C_B`. A.8 "has no instance" as stated (GR:805). These are theorems about a finite isolated `B ∪ R` model,
     with recurrence-scale conclusions. Their physical reading is gated on H-decouple and on Q1(c). Status
     unchanged: G11 Open. The validity review (N1.10, [IR]) reads the finiteness used as that of a subsystem
     made isolated by H-decouple, not total finiteness, which agrees.
3. **Downstream.** GR:605, :709–861; `appendix-a-prediction-status.md:111` (G11); `ch07-gravity.md:149`
   (FULL:2015) and three further ch07 hits; `ch18-beyond.md`, `ch19-open-problems.md`, `glossary.md` (one hit
   each); Intro (one hit).
4. **Treatment.** AM-33.1 RECOVER (GR, P10, minor, gated on Q5). AM-33.2 RECAST-MATHEMATICAL: stated as
   theorems about the finite isolated `B ∪ R` model under H-decouple and the mode counts; their only proofs
   on `main` are GR A.8–A.9 (GR:807, :835–839), so under Q2(b) they stay in GR's appendix as model theorems
   with the physical framing removed, and G11's row text is adjusted (§13).
5. **Goal link.** Decides whether the Page-curve appendix needs A1, and what its cycle results are about.

### AM-34 Substratum Proposition 24.4 (paper proof); census 61, 62 (kernel-only)

**RM.** Proposition 24.4 (Sub:331) is a theorem about a permutation of a nonempty finite set with a passive
readout; its bearing on the substratum is through A1 only. Its proof is a paper proof (Sub:333–342; "neither
new proposition is claimed Lean-proved", Sub:346), with a derivation record on `main`
(`verification/audits/manuscript/multitime-predictive-recovery-20261028/`). Census 61 and 62 are kernel-only
rounds (the semigroup-transfer step and the word-trace kernel) with no manuscript statement; they are not its
witnesses, and "Lemma 24.1" does not occur in `papers/Substratum.md` (review C1). Treatment:
RECAST-MATHEMATICAL; the proposition already states its scope ("one fixed finite reversible carrier",
Sub:344). Under Q2(b) it stays in Substratum §4.1 as a finite-model theorem with its paper proof, as AM-33.2
stays in GR's appendix; the kernel-only families are unchanged. Goal link: decides its stated scope.

### AM-35 Records using the posit as a premise (no own count)

`.../measurement-record-formation/amendments/MR-star.md:296`;
`.../native-apparatus-source-20261113/support/tune-confirmed/TUNE-1-SOURCING-r2.md:139` (and the
`tune-published` copy). Context; correction by the record's route (§A.42 item 6, §A.46 item 4).

### AM-36 GR's universality claim (U1)–(U3), (C1′)–(C3′), S1–S4

1. **Result.** GR:613–669, framed by GR:28. A1 enters through GR:613's "any finite deterministic substratum",
   (U1)'s identification under H-count (AM-22), S2's C3 through `|C_H|` (GR:663), and S4's citation of the §3.2
   construction (AM-5).
2. **Test.** **RC** [IR]. (U2) uses the boundary mode count (S3) and (U3) is structural (GR:621): both hold with
   GR:613's hypothesis restated as "any deterministic substratum with a finite visible sector and a finite
   boundary layer" (Q1(b-mode)). (U1)'s energy-shell identification inherits P7; S4 inherits P1; S2's "high capacity (C3)"
   (GR:663; "$N_H \gg N_V$ the comfortable regime", GR:613) is a lower bound on hidden capacity and holds for a
   hidden sector of any cardinality with no finiteness form and no cone bound (review C4). **Lands as** mixed
   [IR]: (U1) CV under P7's premises; S4 RU; S2 unchanged. The row is NEW through (U1)'s premises (P7).
3. **Downstream.** GR:28, :613–669; `ch07-gravity.md:14` (FULL:1880); `ch09-universality.md:14` (FULL:2481),
   :42, :61, :84, :118.
4. **Treatment.** RECOVER (via P1, P7), gated on Q1(b-mode), Q5, Q6(c).
5. **Goal link.** Decides whether GR's universality claim is stated without A1.

### AM-37 Struct:1255, zero asymptotic entropy rate

**RM** as a statement about every finite realization; its nature reading is removed ([IR]: an infinite carrier
with a normalized measure can have a visible factor of positive entropy rate, r9). Not accessible-time, so not
an A1-test. Treatment: RECAST-MATHEMATICAL; "proved in OI here only at recurrence scale" follows AM-1.3b. Under Q2(b)
the sentence (a one-line fact; no kernel counterpart identified [IR]) stays in Structure with its argument (§12.2). Goal
link: decides how the entropy-rate statement is scoped.

### AM-38 Census 3's quotient modules

**RM**, no change: the observability, passive and controlled quotients "underwrite no manuscript statement"
(census family 3 note); family 3's anchor (GR:188, :194) is not touched. Unchanged under either answer to Q2.
Goal link: housekeeping.

## 6. Results not consuming A1

No treatment: the stochastic-inverse lemma (Main:131–133; listed by Main:60 as using only Lemma 1), the
readback lemma, the §3.4 equivalence and its dilations, reverse finite realization, C3 necessity and hidden
memory (census 1, 33, 41–47, 111, 112), the exhaustive enumerations, the quasilocal completion (census 8,
infinite by construction), census 2, 4, 5, 13, 53 (r9 §7.2). Added here from AM-27 (review F12): the
theory-general results `derivedOI_qm_iff_layerFlowExecutable'`, `layerFlowExecutable_of_control` and
`genTheory_qm_of_quantumArchitecture` (§5, AM-27 (β)), with the typed completion of GR:272 (family 7) [IR]. These
are the visible-plus-constructed and theory-general core; none is removed under either answer to Q2. Census 33
is also the kernel witness of AM-1.3a. Added in r4 (r3 review B3, R3): Main:139's two A1-free sentences (a
non-deterministic visible step makes some `Γ_s` a non-permutation; if every `Γ_s` is a permutation,
`Γ_s^{-1}Γ_t` is a stochastic divisor); Main:145's two formalizations of (C4)'s realization clause and the
two separations `storageReadback_not_implies_routedReadback` and `routedReadback_not_implies_storageReadback`
(census 36). **[reviewer reading, unresolved]** (review C2): the reverse-direction lemma of §3.2
(Main:274–278), which constructs its finite hidden space, also belongs here; r4 placed it in AM-4.2 (§20, D3).
Not on `main` and not added here: EF-1 r6's Lemma PM and Lemma PM-I, derived lemmas in an unpushed draft
(§0, §14).

## 7. Rows N-1 to N-6, and sites found outside r9 §7

*Coverage of the site lists.* The sites listed under "Downstream." and elsewhere in this section are those this audit found. They were checked only for existence and for a keyword of the row's subject on the cited line; a site that paraphrases its subject would not have been found, and no list here is claimed to hold every affected site (§21).

- **N-1 Exact cosmic recurrence and its prediction.** `ch18-beyond.md` §18.7, :164–194 (FULL:4970–5000), with :20
  (FULL:4826), :28 (FULL:4834), :40 (FULL:4846), :244 (FULL:5050), :290 (FULL:5096), :328 (FULL:5134);
  `appendix-a-prediction-status.md:181` (F8, FULL:5705); `README.md:90`; `appendix-c-objections.md:132`
  (FULL:6362). **RX**: global recurrence of nature's dynamics, period at most `g(|S|)`. Recovery: none without
  A1; the measure-theoretic Poincaré theorem gives non-synchronized return (`ch18-beyond.md:172`; Main:155).
  Treatment: REMOVE §18.7's prediction for nature and F8 (ID retired, not reused or renumbered, gap not
  annotated, §A.30); Q10(c) would keep the period bound for a finite permutation as a statement about finite
  models (r3 review R6; owner decision 6896070253). Not accessible-time; not an A1-test. The validity review (G3) records that ch18:244–250
  conflicts with A4's wording at Sub:98 ("a finite periodic lattice"); that is a topology question for Q3,
  not part of this row.
- **N-2 Finite information content.** `ch18-beyond.md:168` (FULL:4974); :170 (FULL:4976). **RX**. Treatment:
  REMOVE the finiteness of total information content; keep the bound on accessible information (boundary
  layer, Q1(b-mode)), or state it per horizon through the patch (F-each, Q1(b-loc); it needs the
  finiteness and dependency premises and, for an information quantity, a normalized starting law) [IR]. A finite
  observational description at each horizon is not finite total information content.
- **N-3 The universality-class commitment "Finiteness".** `ch09-universality.md:104–108` (FULL:2571–2575);
  `ch19-open-problems.md:212` (FULL:5359). **OP (Q3)**. The property as stated serves exact recurrence only ("load-bearing for the
  recurrence route specifically: the recurrence theorem (Chapter 18 §18.7) requires finiteness for the exact
  recurrence of a finite bijection", `ch09-universality.md:106`). Exact recurrence is not carried by a
  fixed-horizon description (EF-1 r6 §P; it would need F-one with an exact return, or a finite carrier). The
  owner's choice is between retiring the property (RX) and replacing it by a different commitment: a finite
  visible sector with finite reading sets and finite alphabets (L1, L2, depending on Q8), the boundary layer
  only as an optional GR premise. That is a **replacement candidate**, a wording (RW); it is **not counted as
  a recovery of the original property** (adopted direction, c.6896890693; review C7). Counts: §9.
- **N-4 Layer 0 example.** `appendix-a-prediction-status.md:48` (FULL:5572): "finite cardinality". **RX**;
  "deterministic bijection structure" follows Q5.
- **N-5 The periodicity clause of the restricted quantum-statistical regime.** `ch18-beyond.md:74` (FULL:4880),
  the clause "on a finite reversible system the rooted laws are periodic ([Main §2.3]), so a revival in one
  recurrence period recurs in every later one, and the sum grows without bound" only (r3 review R2). **RM** as a
  statement about finite realizations. The revival measure `𝒩` on an accessible window is an A1-free visible
  diagnostic of AM-1.3a's kind and is not part of this row.
- **N-6 Ledger item (ii) and the ledger count.** Main:724 item (ii), "Fourteen items, of unequal weight, and not
  fourteen independent physical assumptions", and "the total finiteness of item (ii) and items (iv)–(xiv) lie
  outside the layer it treats"; item (ii) cited by number at Main:60, :700, :718 and GR:585; the posit cited by
  name ("total-finiteness posit") at Main:44, :60, :111, :129, :216, :222, :266, :716, :718 and Comp:118. **OP
  (Q4)**: retire item (ii), or restate it (§9, Q4).
- **Further sites found and assigned to rows above.** Main:356 (AM-9); Main:222 (AM-10); Main:435–437, :700;
  Main:80 item (4); Intro:12, :24; ch01:121, :133; glossary:117; Struct:1138, :1179, :1211; ch01:165 (FULL:500);
  ch19:126 (FULL:5273); ch19:212 (FULL:5359); ch18:244, :290; the AM-8 citing lines (Main:159, :169, :656;
  ch01:125, :223; ch04:36, :182; Meth:162, :283; Struct:522, :532; Sub:407, :409). Earlier additions:
  `ch00-introduction.md:53`; `ch03-structural-realism.md:36`, :102, :114, :240; `ch05-gauge-structure.md:95`;
  `ch15-quantum-engineering.md:114`; `preface.md:3`; `glossary.md:105`; Struct:718, :733, :1174, :1177, :1189,
  :1248; Sub:56, :401; Cx:474.

## 8. Headline, abstract and summary sites

Generated from the rule H1–H3 of §0.

| Site | Content | Row | Rule | Proposed action |
|---|---|---|---|---|
| Main:14 (abstract) | "An observer embedded in a finite deterministic system" | AM-10 | RW | "a deterministic system with a finite visible sector" or equivalent |
| Main:18 (abstract) | three sentences from "On one fixed finite reversible representative" to "... Markov on every accessible window." | AM-1.1 | H1 | remove from the abstract |
| Main:18 (abstract) | "(C2-structural) ... holds by reversibility in every bijective realization and constrains coarse-grained descriptions of the hidden sector" | AM-3.2 (via hidden-sector injectivity) | H3 | under Q5(b) or (d): keep; under Q5(a) or while Q5(c) is pending: leave the abstract, or state that its reading for nature's hidden sector is open |
| Main:20 (abstract) | coupling-graph causal cones; the Bell ceiling for a screened deterministic completion | AM-7.1 (TD), AM-7.2 (NC) | H1 | keep once P3 and P4 (or the fixed-horizon `Ω_n` route) are proved and checked, with finite reading sets and measurement independence stated as hypotheses; otherwise leave the abstract |
| Main:80 item (2) | recurrence-cycle clause ("indivisibility somewhere in the recurrence cycle of a fixed finite reversible representative ... as C4 asserts (§2.3)") | AM-1.1 | H1 | remove from the theorem statement |
| Main:80 item (2) | C2-structural clause, as Main:18 | AM-3.2 | H3 | as Main:18 |
| Main:80 item (4) | "Under the substratum's stated interventions (its finite bijective read-write dynamics and the phase intervention), (iv), full reversible control, is not supplied" | AM-27.1 | H1 | replace by "whether nature's available operations supply (iv) is open"; the monomial-class negative is stated where Q2 places it |
| Main:600 (§3.4 summary) | "(3) No fixed finite classical carrier reproduces full qubit operational behavior" | AM-9.1 | H2 | keep under Q2(a); under Q2(b) the entry cites only statements that remain in Main (body or appendix), or is removed. Main:558 and "Per (3)" state the scope of the headline equivalence, so no destination outside Main is safe for the result they cite (§12.2) |
| Main:716 (§4.5) | "The P-indivisibility proof uses total finiteness ... retained at the recurrence scale" | AM-1.3b | RX | rewrite |
| Main:718 (§4.5 Falsifiability) | "a finite set with a deterministic bijection" | AM-10 | RW | substantive rewording |
| Main:731, :733 (status ledger) | consolidation clause; "bare-recurrence form ... at `t_R`" | AM-1.1, AM-9.1 | H2 | "of a fixed finite realization" under Q2(a); under Q2(b) each row cites only statements that remain in Main (body or appendix), or the clause is removed (§12.2) |
| Intro:12, :24 | "finite recurrence also forces a failure of step-by-step forecasting"; "the consequence of recurrence for forecasts" | AM-1.1 | H1 | remove from the paper's opening |
| SM:24; GR:22 | "the P-indivisibility of reduced dynamics on finite bijections (used in §2.1)"; "the P-indivisibility/recurrence argument" | AM-1 | H1 | follow AM-1.1/AM-1.3b per use |
| `preface.md:3` (FULL:64) | "Indivisibility across the recurrence cycle of a fixed finite reversible representative is a separate fact" | AM-1.1 | H1 | remove from the preface |
| `ch00-introduction.md:53` (FULL:280) | "on a fixed finite reversible system, recurrence forces the rooted visible process to be indivisible" | AM-1.1 | H1 | remove from the introduction |
| `ch01-observation.md:93` (FULL:428) | "The central technical result of the chapter is that the marginalized process is P-indivisible across the recurrence cycle" | AM-1.1 | H1 | re-scope the chapter's stated central result to the readback lemma and AM-1.3a |
| `book/README.md:90`; `appendix-a-prediction-status.md:181` | cosmic recurrence; F8 | N-1 | RX | remove (Q10) |
| `ch09-universality.md:104–106` (FULL:2571–2573) | "six structural properties", "Finiteness" | N-3 | OP | Q3 |

Population of this table: the 18 headline, abstract and summary sites found by this audit; the list is not claimed complete (§21).

## 9. Counts corpus-wide (§A.30)

Each count below is the number of lines matching the stated pattern at `bf89ba13`. A paraphrase would not be counted (§21).

1. **Posit ledger.** "Fourteen items, of unequal weight, and not fourteen independent physical
   assumptions" (Main:724, the only occurrence at `bf89ba13`). The count after the correction is
   `14 − r + a`, with `r = 1` if Q4(a) retires item (ii), and `a` the number of items added: one if Q6(c)
   adopts a reference state as a new item rather than rewriting item (iv), and one if (LE) of P8-M is
   adopted as a posit rather than carried as a named hypothesis (Main:724: "the named hypotheses of the matter, gauge and gravity sectors are carried where they enter"). Q6(d) rewrites item (iv) to normalization of the initial law (count
   unchanged). Q5(b) rewrites item (iii) as a postulate (count unchanged). Q8(a) restates item (ix), Q8(b)
   extends item (xiii)'s consumers, Q8(c) carries finite reading sets as a named hypothesis (count unchanged
   in all three). Q4(b) keeps the count. So the count can be 13 to 16, and both "Fourteen" and "fourteen"
   change with it. If item (ii) is retired: item numbers (iii)–(xiv) unchanged, the gap not annotated; "the
   total finiteness of item (ii) and items (iv)–(xiv) lie outside the layer it treats" becomes "items
   (iv)–(xiv) lie outside ..."; a new item takes the next unused numeral. Ledger numbers are cited as
   identifiers at SM:68, :348; GR:128, :585; Main:60, :362, :414, :652, :700, :718; Comp:120; only the
   citations of (ii) change (by number: Main:60, :700, :718; GR:585). Label sites by name
   ("total-finiteness posit", nine lines of Main and one of Comp): Main:44 (AM-10), :60 (AM-10), :111
   (AM-1.1), :129 (AM-1.1), :216 (AM-6), :222 (AM-10), :266 (AM-5), :716 (AM-1.3b), :718 (AM-10), Comp:118
   (AM-13); none in GR, SM, Sub, Struct, Cx or `book/`. `papers/Main.tex` and `papers/Main.pdf` (and the
   Computation artifacts) are regenerated with the change (§A.25 step 5).
2. **"six structural properties".** `ch09-universality.md:104` (FULL:2571) counts a set whose first member is
   finiteness (Q3). `ch19-open-problems.md:198` (FULL:5345) and :212 (FULL:5359): [IR] which set they count is to
   be read at correction time. `ch09-universality.md:139` (FULL:2606) and :324 (FULL:2791) count Chapter 5's six
   and are not affected.
3. **"A1–A6" ranges.** 65 lines match `A1–A6|A1-A6` at `bf89ba13` in 10 files (GR 3, Meth 4, Struct 29, Sub 9,
   FULL 10, `ch02` 3, `ch03` 2, `ch04` 3, `ch05` 1, `glossary` 1). If A1 is retired (Q3(a)) each range is
   rewritten; A2–A6 keep their numbers. Occurrences of the word `A1` (grep `-o -w`, ranges included): Struct 50,
   FULL 36, Sub 18, Meth 13, `ch02` 8, `appendix-c` 7, `ch04` 6, `ch03` 5, GR 4, `glossary` 2, `ch05` 2, `ch01` 2,
   `appendix-b` 2, Main 1, Comp 1, `ch18` 1, `ch09` 1.
4. **Main:80** "three exact layers and one explicitly conditional extension": unchanged.
5. **Main:600** "Four claims": unchanged under Q2(a); under Q2(b) claim (3) can stay only while the result it cites stays in Main, which §12.2 finds it must [IR: the list
   labels are ordinals of a summary, not identifiers].
6. **Main:60** "Of the two finiteness statements": rewritten with the Remark (AM-10).
7. **Forward predictions.** F8 retired (ID kept, not reused) under every option of Q10. No total count of
   F-rows was found in appendix A by grep [IR].
8. **Substratum's "three projections"** (Sub:371–377): unchanged; the third projection loses its selection
   content if AM-8 is removed (Q7(c)) or kept only as a finite-model theorem (Q7(d)).
9. **Audit-internal counts.** 57 rows (§12): the 56 of r4 to r6 and AM-5b, the one further consumer found (EF-1's coherence class; the review of r6, F9); A1-test rows 2 (AM-6.2, AM-9.2; AM-4.3 is no longer one, §11);
   the held change map's 137 sites change with this audit's removals (a draft count, not a manuscript count).

## 10. Census impact (`verification/lean-manuscript-census.json`, §A.35)

Every manuscript anchor of the registry (107 anchor entries over 27 families) was located at `bf89ba13` and
compared with the sites each treatment rewrites. No Lean module changes under any treatment, so no
supersession entry is needed. The census tool's checks are affected where a kernel-only family becomes
carried, a carried family loses all its anchors, or a listed anchor leaves the manuscripts or changes file.

**Q2(b) in this revision** (§12.1, §12.2, Q2) changes placement and framing only: kernel-witnessed RM statements are
withdrawn from the text (the mathematics stays in Lean), paper-only RM statements keep their proofs in their paper
or at a named destination, and every A1-free result, definition and theory-general result stays.

| Family | Status | Anchors (site) | Rows | Q2(a) | Q2(b) | Same-commit registry action |
|---|---|---|---|---|---|---|
| 1 | current | Main:550 `permMatrix_mem_unitaryGroup`, `isDiag_Phi`; Main:97, :520, :550, :552, :592, :612 `S_imp_D`; Main:608, :514, :612, :314, :312, :778; SM:643 `theorem_19` | AM-2.1, AM-5, AM-5b, AM-30 | kept (P1 edits Main:266, :280–288, not :550) | same | if SM states Theorem 19 for a measurable prior (P6), the SM:643 citation says the kernel proves the counting-prior count form, and the family note says so |
| 2 | scope-consistent | Main:242; GR:174–210; `appendix-b-derivations.md:443` (FULL:6197) | AM-19 | none | none | none |
| 3 | current | GR:188, :194 | AM-38 | none | none | none |
| 5, 10, 11 | current | Main:272, :588; GR:216, :242, :246, :252, :254, :288; ch01:165; ch19:126; FULL:500, :5273 | AM-27 (not its content) | phrase anchors kept verbatim while the surrounding wording is re-scoped | same | update anchors for any phrase that changes |
| 6 | current | GR:258, :274 (box phrase "current OI substratum + continuous off-diagonal controllability"); Main:588 `substratum_plus_control_qm` | AM-27.1 (γ) | keep the box phrase verbatim or update | every anchor lost | kernel-only (status, note) |
| 7 | current | GR:272 `typed_determined_iff`, `typed_determined_of_oiPlusPos` | AM-27 range | identifier anchors kept | kept | none |
| 8 | current | GR:278, :282; Main:588 `quasiState_unique` | AM-7 (P3) | none; P3 may cite `iterate_dependsOnlyOn_ball`, `readout_unaffected_outside_ball`, `site_iterate_dependsOnlyOn` at Main:362 (the family already has a Main anchor; the proof term uses no GR mathematics, EF-1 r6 N1.6) | same | optional new anchor for the P3 citation |
| 9 | scope-consistent | GR:284 | — | none | none | none |
| 14 | current | GR:266 `layerFlowExecutable_of_control`, `substratumTheory_not_layerFlowExecutable`; Main:588 `substratumTheory_not_layerFlowExecutable` | AM-27 (β), (δ) | kept | keeps `layerFlowExecutable_of_control` (GR:266, A1-free) [IR]; loses both `substratumTheory_not_layerFlowExecutable` anchors | drop the lost anchors; note updated; stays carried |
| 19 | current | GR:256 `substratumClass_not_onesFixing` and "The phase intervention enters as an assumption on the substratum class"; Main:588 "as a stated intervention principle rather than a consequence of its finite states and bije[ctive dynamics]" | AM-27.1 (γ) | the Main:588 phrase contains wording AM-27 re-scopes: keep it verbatim or update the anchor | every anchor lost | kernel-only |
| 20 | current | GR:266 and Main:588 `derivedOI_qm_iff_layerFlowExecutable'`; GR:264, :268 "one nontrivial layer flow executable" | AM-27 (β) | kept | kept at GR:264, :266, Main:588 [IR]; the GR:268 occurrence goes with family 21's box | drop the GR:268 anchor if that occurrence goes |
| 21 | current | GR:266, Main:588 `obs_not_layerFlowExecutable`; GR:268 box "stated substratum dynamics with observer access" | AM-27.2 | keep the box phrase verbatim | every anchor lost | kernel-only |
| 22 | current | GR:266, Main:588 `coherentLiftClass_eq_substratumClass`; GR:266 "unresolved rather than excluded" | AM-27.1 (γ) | kept | every anchor lost | kernel-only |
| 33 | kernel-only | none | AM-1.3a | if Main:157 cites `c4r_implies_pIndivisible`, the family becomes carried | same | status, anchor and note updated |
| 34 | current | four (file, string) entries: "**Theorem (overlap and return).**" (Main:141); `pIndivisible_of_rooted_identity_return_of_overlap` (Main:137, :143); `c4r_of_rooted_identity_return_of_overlap`, `pIndivisible_of_identity_return_of_overlap` (Main:143) | AM-1.1 (:137), AM-1.2 (:141, :143) | kept | kept: every entry still occurs at Main:141 or :143 if Main:137 moves | none while Main:143 stays (review C13.2) |
| 35 | current | Main:145: `routed_forces_indivisible_somewhere`, `routed_forces_return_indivisibility`; "in the seed-conditioned reading it is that of the initial hidden state" | AM-28 (forcing); §6 (definition) | kept | the two forcing identifiers lost; the definitional phrase kept [IR] | drop the two anchors; stays carried |
| 36 | current | Main:145: `routedAtStorage_forces_indivisible_somewhere`, `routedAtStorage_forces_return_indivisibility`, `storageReadback_not_implies_routedReadback`, `routedReadback_not_implies_storageReadback`; "In the storage-time reading the hidden law is that of the hidden state at the storage time" | AM-28 (forcing); §6 (definition, separations) | kept | the two forcing identifiers lost; the separations and the definitional phrase kept [IR] | drop the two anchors; stays carried |
| 39 | current | Main:590 | — | none | none | none |
| 40 | current | Main:638: `finiteRootedRealizable_iff_pper`, `pper_of_finiteRootedRealizable`, `pper_has_responseRealization`; "exact all-time gluing for recurrent families of multi-time laws" | AM-9.1 | kept; open question (b) reworded around the phrase anchor | stays in Main with its anchors: §12.2 finds no destination outside Main safe for AM-9.1 (r4 had: withdrawn, every anchor lost, or relocated with its anchors) | none while Main:638 stays (§12.2). If a later reviewed unit settles open question (a) (Q15), the phrase anchor changes in that commit, together with its mirrors at Main:731 and Intro:178 and the guard `R7-RCL` (`verification/lean/edge_rigidity_probe.py:6928`), which pins the wording (EF-1 r6 N2.9) |
| 42, 55, 85 | current | Main:644; ch01:187; ch19:285, :293; glossary:67 | — | none | none | none |
| 54 | current | Main:338 heading "Remark (three notions, kept apart)"; Main:644; ch01:187 | AM-1 | heading kept; item (2) re-scoped | same | none if the heading is kept |
| 52 | current | Sub:102; ch02:86; glossary:13 | Q3 | none (A6 keeps its number) | none | none |
| 0, 110 | current | SM:266–605; SM:304 | — | none | none | none |

Population of this table: 23 lines covering 29 census families (three lines cover several: 5, 10, 11; 42, 55, 85; 0, 110).

**Totals.** Under Q2(a): no family loses all anchors. Under Q2(b) as reformulated: five families become
kernel-only in the same commit (6, 19, 21, 22, 40; family 40 only if Main:638 is withdrawn rather than
relocated with its anchors); families 14, 20, 35 and 36 keep A1-free anchors and drop the lost ones, which
depends on the correction keeping those sentences [IR]; family 34 needs no action while Main:143 stays. If
AM-9.1 stays in Main, as §12.2 finds it must, family 40 keeps its anchors and four families become kernel-only,
not five. Under the
r2 wording of Q2(b) (every RM row removed whole): nine families (those five with 14, 20, 35, 36). Family 33 may
become carried under either answer.

**Families whose registry entries use A1 (r2 review F6).** Built by searching each family's whole entry (name,
modules, note, anchors) for `A1`; family 55 matched only through the guard name `R7-A12P` and is excluded.
Result: families **12, 13, 15, 48, 49, 53**, all kernel-only. By use [IR]: the manuscripts' A1–A6 class in 12
("not entailed by A1-A6"), 13 ("no manuscript-level A1-A6 conjunct"), 48 ("none fixed by the manuscripts or by
A1-A6") and 49 ("A1-A6 unchanged"); the kernel predicate or its images in 13 (`A1Realized`,
`substratumTheory_A1`), 15 ("A1, A2, A5 stated"), 49 (`hexSubstratum_A1`, "the A1-A4, not-A5 class") and 53
(`pk3a_A1`, `cx3b_complex_not_A1`, "A1 is NOT weakened", read here as the kernel interface predicate). Separately,
Lean modules whose source names the substratum axiom A1 (excluding `chiA1` in `QuarterTurn.lean`, an irrep
character, and Averaging.lean's "§A1", a section label): `SubstratumInterfaceAudit` (`A1`, `a1_of_finite`,
`waveSubstratum_A1`, `obs_a1`), `ManuscriptAxioms` (`A1Realized`, `A1A2Realized`, `substratumTheory_A1`,
`substratumTheory_A1A2`, `a1_every_theory`), `HexLatticeGas` (`hexSubstratum_A1`), `A6Instantiation` (`pk3a_A1`,
`cx3b_complex_not_A1`), and comments in `SubstratumSource.lean:48`, `RouteB.lean:106`, `FrozenSourcing.lean:83`,
`HydroSourceAudit.lean:88`. Under Q3(a) the kernel predicate keeps its meaning (a property of models,
consistent with RM rows AM-16, AM-25) and the class-referring notes (12, 13, 48, 49) are updated or flagged in
the correction. Under Q3(b) the kernel identifiers above keep the old content under a name the manuscripts
would use for the new one: a Lean naming and registry decision for families 13, 15, 49 and 53 at least.

**§A.35 contract.** The correction strengthens no kernel theorem; it changes manuscript statements around
anchors. The registry actions in the table belong to the same commit as the manuscript change.

## 11. A1-test candidates

Results where A1 gives a consequence at accessible times that the visible sector alone does not. Each is an
implication from A1 (with the stated co-premises) to an accessible-time visible property; the owner may keep it
as an explicitly labelled conditional or remove it (Q9). None is a derived prediction with a computed
magnitude, and none establishes a constraint on nature unless its antecedent is adopted.

1. **Fixed finite carrier: the qubit obstruction and finite predictive dimension (AM-9.2).**
   - Statement: if nature is one fixed finite reversible system with `N` ontic configurations, a fixed prior
     and observation map, and the operational interface is the ordinary preparation → finite ontic system →
     measurement one (Main:558; "proved under the stated operational interface", Main:600 (3)), then every
     prepare-and-measure behavior matrix factors nonnegatively through `N` states (Main:558, the factorization
     half, P), so for every `N` some finite qubit prepare-and-measure experiment is not reproduced exactly (the
     unboundedness half, imported [55]); it supports only finitely many distinct action-labelled conditional
     families (Main:486); and its visible process has finite predictive dimension (Main:356), so the ranks of
     its visible multi-time law matrices are bounded by `N` [IR].
   - Accessibility: single-time and finite-horizon experiments, but only for a stated bound on `N`: the size of
     the decisive experiment grows with `N`.
   - Limits: `N` is not fixed by visible data, and the size of the deviation at physical `N` is not estimated;
     a finite realization reproduces any `d`-dimensional quantum experiment of horizon `K` to any stated
     accuracy (Main:600 item (4)). The test is exact-equality only. The fixed-horizon lemma does not turn it into a
     test: per horizon, with each preparation and measurement a fixed protocol of finite support over every branch (FS-all), `N_eff(n)`
     counts the data on the enlarged patch (F-each; review C8), which grows with `n`; the fixed-`N`
     antecedent is a one-description-for-every-horizon statement (F-one), which is not established.
   - A visible form of the antecedent, if the owner keeps one (Q9): for an autonomous finite bijective system
     the visible record is periodic (Main:638's forward direction), and for an autonomous finite deterministic
     system eventually periodic, with no bound on the period or transient. With continuing external inputs or
     settings a finite system can give nonperiodic output, so the visible form applies to the autonomous case
     only. No converse is used.
2. **Corner occupancy (AM-6.2, Main:216).**
   - Statement: if nature's hidden environment is finite and the embedded observer's dynamics is its
     marginalization, there is no first-order leakage (Doukas's bound, external, continuous-time), so
     fundamental embedded-observer dynamics lies in the near-unitary corner, displaced only by `𝒟`; observed
     first-order leakage in fundamental (not engineered) dynamics would refute the conjunction.
   - Accessibility: a short-time property of open-system dynamics.
   - Limits: the bound is continuous-time and is applied to a discrete substratum by analogy; Main:718 records
     that an outcome-independent rule identifying the fundamental open-system processes is not supplied. The
     validity review (G5, [IR]) adds that every finite-horizon discrete-time law, Markov ones included, has a
     finite reversible realization (`S_imp_D`, Main:97), so the test has content only in continuum time or at
     all times; EF-1 r6 (N1.8, N3.5) [IR] adds that in the native class, under a uniform product prior in both carriers,
     a finite torus reproduces the infinite lattice's law on any fixed horizon, and gives the form of the first-order clause as mixed (the cardinality clause is not a fixed-horizon statement; the estimate of Main:340 is undetermined). This candidate's accessibility is
     therefore contested; it is listed with that limit.
3. **Not a candidate, listed so it is not mistaken for one: double stochasticity of the one-step law (AM-4.3
   with AM-3.2, Main:60, :276–278).** r3 listed it as candidate 3. [IR] An infinite carrier with an invariant
   normalized prior of uniform visible marginal gives a doubly stochastic one-step matrix too (EF-G5), and EF-1 r6
   N3.2 derives the needed invariance of the uniform product measure under the selected phase-space map on
   any site set from Main inputs (a statement about the full system; checked by the review of EF-1 r2; provisional), which replaces the earlier
   off-`main` support. (M-full), checked by the review of EF-1 r4, extends this to every bijection of the locality class of `main` with finite alphabets; outside that class it can fail (B1). So it does not discriminate between
   finite and infinite carriers. It remains a scope condition of ledger item (iii) (Main:724), not an A1 test.
4. **Not a candidate: "specifically P-indivisible" device memory (Cx:434).** Its accessible form is the revival
   witness (AM-1.3a), which needs no A1.

Not accessible-time, so not candidates: N-1, AM-1.3b, AM-2.2, AM-37, N-2, AM-23.2, the all-time periodicity of
Main:638. AM-8's exclusion is conditional on (EM) and is not an accessible-time observable of A1. EF-1's
finite-hidden-memory draft (H-mem) is not proposed (EF-1 r6 §5.6: not hard to vary with a free dimension bound) and
carries none of the rows.

## 12. Summary table, reasons, the Q2 mapping, and counts

Impact: S (one or two sites, no headline), M (several papers or a book section), L (headline, abstract, a GR
or SM theorem, or a section across papers and book). Reason: the primary reason the row, as now on `main`,
loses observational force (§0: i, ii, iii). Class: recovery class of the 19 RC and OP rows (FIRM, CONTINGENT, NEW, or replacement candidate; §0, §14.1); a class
records no recovery. Gate: owner
questions the treatment waits on. Every forward-direction recovery also presupposes Q11's answer (§19).

| # | Row | Result | Category | Reason | Lands as | Class | Unit | Gate | Impact |
|---|---|---|---|---|---|---|---|---|---|
| 1 | AM-1.1 | recurrence-cycle theorems | RM | i | — | — | — | Q2 | L |
| 2 | AM-1.2 | overlap and return (matrix form) | RD | ii | — | — | — | — | S |
| 3 | AM-1.3a | revival criterion on a window | RD | ii | — | — | optional kernel citation | — | S |
| 4 | AM-1.3b | recurrence-scale P-indivisibility of nature | RX | i | — | — | — | — | L |
| 5 | AM-2.1 | CP-indivisibility, realization form | RC | i | RM | FIRM | P1 | Q2 (landing) | S |
| 6 | AM-2.2 | CP-indivisibility of nature's channel | RX | i | — | — | — | — | S |
| 7 | AM-3.1 | record-prong injectivity | TD | iii | — | — | — | Q11 | S |
| 8 | AM-3.2 | bijectivity of nature | RX | i | — | — | — | Q5 | M |
| 9 | AM-4.1 | Lemma 3 finite-cycle and maximal-entropy lemmas | RM | i | — | — | — | Q2 | S |
| 10 | AM-4.2 | baseline matrices, double-stochasticity lemma (AM-21 uses `T`) | RM | i | — | — | — | Q2 | S |
| 11 | AM-4.3 | nature's measure, item (iv) | RX | i | — | — | — | Q6 | M |
| 12 | AM-4.4 | Proposition 4b, extension clause | RC | i | CV [IR] | NEW | P13 | Q6 | S |
| 13 | AM-5 | §3.2 setup, channel, Born form | RC | i | RU | FIRM | P1 | — | M |
| 14 | AM-6.1 | finite-environment no-leakage clause | RM | i | — | — | — | Q2 | S |
| 15 | AM-6.2 | corner occupancy of nature; A1-test | RX | i | — | — | — | Q9 | S |
| 16 | AM-7.1 | coupling-graph cone | RC | i | TD; CV part [IR] only with L10 | CONTINGENT | P3 | Q8, Q11; L10 | M |
| 17 | AM-7.2 | Bell ceiling | RC | i | NC | CONTINGENT (r6: FIRM) | P4 or finite-`Ω_n` route | — (the `Ω_n` route: Q8); none for the proof as a conditional theorem; the row's class is disputed (§14.1) | M |
| 18 | AM-7.3 | Bell–lattice corollary | RC | i | NC | CONTINGENT (r6: FIRM) | P3, P4 | —; none for the proof as a conditional theorem; the row's class is disputed (§14.1) | S |
| 19 | AM-8 | §4.6 observer selection | OP | i | TD [IR] (Q7(a), (b)); RM (Q7(d)) | NEW | P8-M or P8-S | Q6, Q7, Q8; Q5 if P8-M's check fails | L |
| 20 | AM-9.1 | §3.4 fixed-realization obstructions | RM | i | — | — | — | Q2 | M |
| 21 | AM-9.2 | their bearing on nature; A1-test | RX | i | — | — | — | Q9 | S |
| 22 | AM-10 | statements naming A1, framing | RW | i | — | — | with the held map | — | L |
| 23 | AM-11 | Theorem 23, Lemma 23.0 | RC | i | untraced | NEW | P12 | Q1(b-mode), Q3, Q5, Q6 | L |
| 24 | AM-12 | Theorem 24 (i), (iii), Corollary | RU | ii | — | — | P11 optional | (Q6 for P11's application) | S |
| 25 | AM-13 | Comp:118 | RW | i | — | — | — | — | S |
| 26 | AM-14 | GR boundary-only lemma, deep-sector corollary | RU | ii | — | — | — | Q1(b-loc), Q6, Q8 | S |
| 27 | AM-16 | SM finite-torus theorems | RM | i | — | — | — | Q2 | S |
| 28 | AM-19 | phase-locking lemma | RU | ii | — | — | — | — | S |
| 29 | AM-20.1 | characterization theorem, law level | RU | ii | — | — | P15 check | — | M |
| 30 | AM-20.2 | identification of nature with a finite substratum | RX | i | — | — | — | — | L |
| 31 | AM-21.1 | C2 persistence form | RC | i | TD | NEW; conditional theorem available (r6: FIRM) | P5a | (Q11 for the reading) | M |
| 32 | AM-21.2 | C2 mixing and process forms | RC | i | TD | NEW | P5b | Q6 | M |
| 33 | AM-22 | GR counting temperature and rate ratio | RC | i | CV | NEW | P7 | Q1(b-mode), Q5, Q6 | L |
| 34 | AM-23.1 | super-BQP, A1 leg | RW | i | — | — | — | — | S |
| 35 | AM-23.2 | infinite-time computation exclusion | RC | i | TD [IR] | CONTINGENT | P16 | Q8, Q11 | S |
| 36 | AM-24 | constructive OSR | RC | i | untraced | NEW | with P12 | Q1(b-mode), Q3, Q5, Q6 | M |
| 37 | AM-25 | census 15, 31 (finite tori; kernel-only) | RM | i | — | — | — | none | S |
| 38 | AM-27.1 | monomial-class facts and the carrier-general negative | RM | i | — | — | P14 optional | Q2 | L |
| 39 | AM-27.2 | observer-theory negatives, finite tori | RM | i | — | — | P14 optional | Q2 | M |
| 40 | AM-28 | routed readback: forcing theorems | RM | i | — | — | — | Q2 | S |
| 41 | AM-29 | census 32 (kernel-only) | RM | i | — | — | — | none | S |
| 42 | AM-30 | Theorem 19 | RC | i | CV | NEW | P6 | Q5, Q6 | M |
| 43 | AM-31 | Theorem 22 and Corollary | RC | i | TD (1); RU (2); TD (3), a CV part only with L10 [IR] | FIRM for the theorem as stated (parts (1), (2)); part (3) a replacement part, in no class (r6: NEW) | P9 | Q6(d), Q11, Q1(b-loc); L10 for a CV part | M |
| 44 | AM-32 | SM finite-ring statements | RM | i | — | — | — | Q2 | S |
| 45 | AM-33.1 | A.7 | RC | iii | TD | CONTINGENT (else NEW) | P10 | Q5(d), Q8(b) | S |
| 46 | AM-33.2 | A.8, A.9 on a finite isolated `B ∪ R` | RM | iii | — | — | — | Q1(c), Q2 | S |
| 47 | AM-34 | Proposition 24.4, Lemmas 24.1, 24.1A | RM | i | — | — | — | Q2 | S |
| 48 | AM-36 | GR universality (U1)–(U3) | RC | i | mixed: CV (U1), RU (S4) [IR] | NEW | via P1, P7 | Q1(b-mode), Q5, Q6(c) | M |
| 49 | AM-37 | zero entropy rate | RM | i | — | — | — | Q2 | S |
| 50 | AM-38 | census 3 quotients (kernel-only) | RM | i | — | — | — | none | S |
| 51 | N-1 | cosmic recurrence, §18.7, F8 | RX | i | — | — | — | Q10 | M |
| 52 | N-2 | finite information content | RX | i | — | — | — | — | S |
| 53 | N-3 | universality-class "Finiteness" | OP | i | — | replacement candidate (not a recovery) | count | Q3, Q8 | S |
| 54 | N-4 | Layer 0 "finite cardinality" | RX | i | — | — | — | — | S |
| 55 | N-5 | periodicity clause of the revival sum | RM | i | — | — | — | Q2 | S |
| 56 | N-6 | ledger item (ii) and its count | OP | i | — | FIRM | count | Q4 | M |
| 57 | AM-5b | one-step coherence results of §3.2 (Main:290–324) | RM | i | — | — | — | Q2 | S |

Mirrors and records without their own count: AM-15, AM-17 (follow the rows they mirror), AM-18, AM-26, AM-35
(records; context).

**Evidence for the reasons.** The reasons column is the r3 review's table, adopted after checking its citations and
confirmed by the review of r4 for every row it checked; the line evidence for each row is in that row's section above (for example AM-1.1: `C_H` finite
"under the total-finiteness posit", Main:111, :129; AM-7.1: "Finiteness of V is used in the first step",
Main:362; AM-33.2: an isolated `B ∪ R` under H-decouple, GR:787, :807, :839, whose finiteness is the
subsystem's). No row was disputed.

**Counts (default answers).** 57 rows: RECAST-CONSTRAINING 0; RECAST-DIAGNOSTIC 2 (AM-1.2, AM-1.3a);
RECAST-REPRESENTABILITY 4 (AM-12, AM-14, AM-19, AM-20.1); RECAST-WORDING 3 (AM-10, AM-13, AM-23.1); TOTAL-DYNAMICS
1 (AM-3.1); RECAST-MATHEMATICAL 18 (AM-1.1, AM-5b, AM-4.1, AM-4.2, AM-6.1, AM-9.1, AM-16, AM-25, AM-27.1, AM-27.2, AM-28,
AM-29, AM-32, AM-33.2, AM-34, AM-37, AM-38, N-5); RECOVER 16; REMOVE 10 (two of them A1-test candidates: AM-6.2,
AM-9.2); OWNER-PENDING 3 (AM-8, N-3, N-6). 0 + 2 + 4 + 3 + 1 + 18 + 16 + 10 + 3 = 57. Population 57: the 56 rows of r4 to r6 and AM-5b, added in r7.

**Reasons.** (i) A1 unsupported 48 (the 47 of r6 and AM-5b); (ii) missing link 6 (AM-1.2, AM-1.3a, AM-12, AM-14, AM-19, AM-20.1);
(iii) whole-system only 3 (AM-3.1, AM-33.1, AM-33.2). 48 + 6 + 3 = 57 (population 57).

**No surviving recast row establishes a justified constraint on the visible law.** Under the default answers,
and under either answer to Q2, no row in any recast category establishes a constraint on a finite-horizon
visible law. Of the 16 RECOVER rows, the recovered statements would land: CV under their premises 2 (AM-22,
AM-30) and 1 more [IR] (AM-4.4); TD 5 (AM-7.1, with a CV part only if L10 is supplied; AM-21.1, AM-21.2,
AM-23.2, AM-33.1); NC 2 (AM-7.2, AM-7.3); mixed with a conditional CV part 2 [IR] (AM-31, AM-36); RU 1 (AM-5);
RM 1 (AM-2.1); untraced 2 (AM-11, AM-24). 2 + 1 + 5 + 2 + 2 + 1 + 1 + 2 = 16. The CV landings of AM-22, AM-30
and AM-4.4 need premises under §A.29 (Q5, Q6, Q1(b-mode)); AM-7.1's CV part needs an owner decision on a reading of existing locality posits (Q8) and the link L10; AM-31's
CV part, if any, needs a normalized starting law for nature (L9: a replacement of item (iv), Q6(d), not a reading
of its text) and L10.

### 12.1 Disposition of all 57 rows, with the Q2 subset marked

**The Q2 subset.** Q2 concerns only the **18 RECAST-MATHEMATICAL rows**: the 17 marked **Q2-17** below, which are the 17 of adopted direction c.6896890693, and AM-5b, added in r7 and marked **Q2 (18th)**. The other
39 rows are not reached by Q2: their disposition is the same under every answer to it. **Q2(b) is an option
only; it is not chosen here, and it is not decision-ready until the destinations of §12.2 are agreed**
(adopted direction, c.6896771264 and c.6896890693).

Columns. *Now*: the disposition at the default answers, which for the Q2-17 rows is Q2(a) (the statement
kept in place as a theorem about its model class). *Physical claim*: what happens to the row's reading for
nature; it is the same under every answer to Q2. *Under Q2(b)*: the disposition under Q2(b) as reformulated
(placement and framing change; no mathematics is deleted). *Mathematics under Q2(b)*: **stays in its paper**
(the paper proof stays in the paper it is in, reframed); **moves** (the paper proof goes to a named
destination, §12.2); **in place** (the statement stays, a definition is restated); **withdrawn, Lean keeps
it** (the manuscript statement is withdrawn and the mathematics stays in a Lean module on `main`);
**import withdrawn** (an application of an external result, with no proof on `main` to keep);
**kernel-only** (no manuscript statement; unchanged); "same" (Q2 does not reach the row).

| # | Row | Cat. | Subset | Now (default answers) | Physical claim (every answer to Q2) | Under Q2(b) | Mathematics under Q2(b) |
|---|---|---|---|---|---|---|---|
| 1 | AM-1.1 | RM | **Q2-17** | kept in Main as finite-realization theorems | nature reading removed | Main:111–129, :135–137, the recurrence clauses of :139 and :435–437 keep their paper proofs at a destination to be agreed; Main:131–133 and :139's A1-free sentences stay; Main:157 repointed | moves (§12.2: a Main appendix, or a companion with rewrites) |
| 2 | AM-1.2 | RD | — | kept (diagnostic) | kept | same | same |
| 3 | AM-1.3a | RD | — | kept | kept | same | same |
| 4 | AM-1.3b | RX | — | removed; rewritten to the visible statement | removed | same | same |
| 5 | AM-2.1 | RC | — | recover (P1), FIRM, landing RM; no recovery credit | reading for nature not asserted | same; if recovered, the RM landing follows Q2 | same (landing: stays in Main §3.2, §12.2) |
| 6 | AM-2.2 | RX | — | removed | removed | same | same |
| 7 | AM-3.1 | TD | — | kept (Q11) | kept (Q11) | same | same |
| 8 | AM-3.2 | RX | — | removed as a derived property of nature (Q5) | removed | same | same |
| 9 | AM-4.1 | RM | **Q2-17** | kept as finite-set lemmas | none asserted (finite-set lemmas) | withdrawn from the text | withdrawn, Lean keeps it (`orbit_invariant_unique`, `counting_maximal_entropy`) |
| 10 | AM-4.2 | RM | **Q2-17** | kept as a realization's default prior | none asserted (a realization's prior) | `T` restated from a realization's prior `π_H`; Main:274–278 stays as an A1-free lemma **[reviewer reading, unresolved]**. On r4's reading Main:274–278 belongs to this row and moves with its paper proof | in place **[reviewer reading, unresolved]**; on r4's reading: moves, and only to a Main appendix (§12.2) |
| 11 | AM-4.3 | RX | — | removed, or Q6 | removed | same | same |
| 12 | AM-4.4 | RC | — | recover (P13), NEW; no recovery credit | waits on Q6(c) | same | same |
| 13 | AM-5 | RC | — | recover (P1), FIRM; no recovery credit | representation statement (RU) if recovered | same | same |
| 14 | AM-6.1 | RM | **Q2-17** | kept as a model clause naming the import | none asserted (finite-environment clause) | withdrawn | import withdrawn |
| 15 | AM-6.2 | RX | — | removed, or Q9 | removed | same | same |
| 16 | AM-7.1 | RC | — | recover (P3), CONTINGENT; no recovery credit | TD if recovered (Q11) | same | same |
| 17 | AM-7.2 | RC | — | recover (P4), CONTINGENT; no recovery credit | NC if recovered | same | same |
| 18 | AM-7.3 | RC | — | recover (P3, P4), CONTINGENT; no recovery credit | NC if recovered | same | same |
| 19 | AM-8 | OP | — | owner (Q7), NEW | owner (Q7) | same; under Q7(d) the row is RM and follows Q2 | same (under Q7(d): stays in Main §4.6, §12.2) |
| 20 | AM-9.1 | RM | **Q2-17** | kept in Main as fixed-realization obstructions | "bear on nature" removed (AM-9.2) | stays in Main: Main:496, :558, :562 and :600 state the scope of the headline equivalence, so no destination outside Main is safe; at most a move inside Main; Main:638's classification keeps its anchors | stays in its paper (Main) |
| 21 | AM-9.2 | RX | — | removed, or Q9 | removed | same | same |
| 22 | AM-10 | RW | — | reworded | reworded | same | same |
| 23 | AM-11 | RC | — | recover (P12), NEW; no recovery credit | waits on its gates | same | same |
| 24 | AM-12 | RU | — | kept | kept | same | same |
| 25 | AM-13 | RW | — | reworded | reworded | same | same |
| 26 | AM-14 | RU | — | kept | kept | same | same |
| 27 | AM-16 | RM | **Q2-17** | kept in SM, scoped to the finite-torus model | "OI's substratum" scope removed | stays in SM (§4.2, Appendix A) as finite-torus statements; census 15, 49 stay | stays in its paper (SM) |
| 28 | AM-19 | RU | — | kept | kept | same | same |
| 29 | AM-20.1 | RU | — | kept, qualifier reworded | kept | same | same |
| 30 | AM-20.2 | RX | — | removed | removed | same | same |
| 31 | AM-21.1 | RC | — | recover (P5a), NEW (conditional theorem available); no recovery credit | TD if recovered (Q11) | same | same |
| 32 | AM-21.2 | RC | — | recover (P5b), NEW; no recovery credit | waits on Q6(c) | same | same |
| 33 | AM-22 | RC | — | recover (P7), NEW; no recovery credit | waits on its gates | same | same |
| 34 | AM-23.1 | RW | — | reworded | reworded | same | same |
| 35 | AM-23.2 | RC | — | recover (P16), CONTINGENT, else remove; no recovery credit | TD if recovered | same | same |
| 36 | AM-24 | RC | — | recover with P12, NEW; no recovery credit | waits on its gates | same | same |
| 37 | AM-25 | RM | **Q2-17** | unchanged (no manuscript statement) | none asserted | unchanged | kernel-only |
| 38 | AM-27.1 | RM | **Q2-17** | kept as monomial-class statements | "the concrete OI substratum supplies" restated as a class statement | withdrawn; (α) kept where kept text uses it, (β) kept | withdrawn, Lean keeps it |
| 39 | AM-27.2 | RM | **Q2-17** | kept, finite tori | as row 38 | withdrawn | withdrawn, Lean keeps it |
| 40 | AM-28 | RM | **Q2-17** | kept | none asserted | forcing sentence withdrawn; definitions and separations kept (§6) | withdrawn, Lean keeps it |
| 41 | AM-29 | RM | **Q2-17** | unchanged (no manuscript statement) | none asserted | unchanged | kernel-only |
| 42 | AM-30 | RC | — | recover (P6), NEW; no recovery credit | waits on Q5, Q6(c) | same | same |
| 43 | AM-31 | RC | — | recover (P9): parts (1), (2) FIRM; part (3) a replacement part; no recovery credit | TD and RU if recovered | same | same |
| 44 | AM-32 | RM | **Q2-17** | kept in SM as model statements | none asserted (model statements) | stays in SM (§3.1, Appendix A) with its arguments [IR: no kernel counterpart identified] | stays in its paper (SM) |
| 45 | AM-33.1 | RC | — | recover (P10), CONTINGENT, else NEW; no recovery credit | TD if recovered (Q11) | same | same |
| 46 | AM-33.2 | RM | **Q2-17** | kept as finite `B ∪ R` model theorems | reading gated on Q1(c) and H-decouple | stays in GR's Appendix A as model theorems (their only proof on `main`), framing changed | stays in its paper (GR) |
| 47 | AM-34 | RM | **Q2-17** | kept in Substratum, scoped | bearing "through A1 only" removed | stays in Substratum §4.1 as a finite-model theorem with its paper proof (Sub:333–342; not Lean-proved, Sub:346); census 61, 62 unchanged | stays in its paper (Substratum) |
| 48 | AM-36 | RC | — | recover (via P1, P7), NEW; no recovery credit | waits on its gates | same | same |
| 49 | AM-37 | RM | **Q2-17** | kept in Structure, scoped | nature reading removed | Struct:1255's sentence stays in Structure with its one-line argument [IR] | stays in its paper (Structure) |
| 50 | AM-38 | RM | **Q2-17** | unchanged (no manuscript statement) | none asserted | unchanged | kernel-only |
| 51 | N-1 | RX | — | removed (Q10) | removed | same; under Q10(c) the period bound is kept as a model statement and then follows Q2 | same (under Q10(c): stays in `ch18-beyond.md` §18.7) |
| 52 | N-2 | RX | — | removed | removed | same | same |
| 53 | N-3 | OP | — | owner (Q3): retire, or replace (a replacement candidate, not a recovery) | owner (Q3) | same | same |
| 54 | N-4 | RX | — | removed | removed | same | same |
| 55 | N-5 | RM | **Q2-17** | kept, scoped | none asserted (the clause only) | clause withdrawn; `𝒩` kept | withdrawn, Lean keeps the periodicity (`rootedMap_periodic`); the step to an unbounded sum is a one-line paper inference (review C13.4) |
| 56 | N-6 | OP | — | owner (Q4), FIRM | owner (Q4) | same | same |
| 57 | AM-5b | RM | **Q2 (18th)** | kept in Main §3.2 as results about the displayed realization's one-step channel under a uniform hidden input | reading for nature not asserted | stays in Main §3.2 with its proofs and its hypothesis (the hidden input uniform and uncorrelated with the visible input, Main:310, :316), as under Q2(a). The threshold Theorem (Main:312–314) is A1-free and is unchanged. Changed after review; unreviewed. | stays in its paper (Main) |

**Counts of the table.** 57 rows (population 57); Q2 subset: 18 (the 17 marked Q2-17 and AM-5b); not reached by Q2: 39. 18 + 39 = 57.

**Counts of the Q2 subset (18 rows) under Q2(b).**
- Paper proof kept, **8**: AM-1.1, AM-5b, AM-9.1, AM-16, AM-32, AM-33.2, AM-34, AM-37. Of these, five stay in the
  paper they are in (AM-16, AM-32, AM-33.2, AM-34, AM-37), AM-9.1 and AM-5b stay in Main, and AM-1.1 is the only one
  that moves, to a destination not yet agreed (§12.2).
- Kept in place with a definition restated, **1**: AM-4.2 **[reviewer reading, unresolved]**.
- Withdrawn from the text with the mathematics kept in Lean, **5**: AM-4.1, AM-27.1, AM-27.2, AM-28, N-5.
- An external import's application withdrawn, **1**: AM-6.1.
- Kernel-only, unchanged, **3**: AM-25, AM-29, AM-38.

8 + 1 + 5 + 1 + 3 = 18. On r4's reading of Main:274–278 (the lemma is part of AM-4.2 and moves with its
proof) the first two lines read 9 and 0: 9 + 0 + 5 + 1 + 3 = 18. Valid mathematics deleted from `main`: 0
under either answer and either reading.

**Physical-claim removal versus mathematics.** The physical claims removed are the 10 RX rows and the
readings for nature of the 18 RM rows, identically under Q2(a) and Q2(b): Q2 changes no physical claim and
no category count. What Q2(b) changes is how 14 rows' statements are placed or framed (the 8, the 5 and the 1 import), with
AM-4.2's definition restated, and with them four or five census families (§10). Q2(b) also applies, by
the same rule, to the one RM landing (AM-2.1), to AM-8 under Q7(d), to N-1's period bound under Q10(c), and
to the finite-model form of any recovery that fails.

### 12.2 Named destinations under Q2(b), and the Main-independence check for each

Main "must not reference or cite downstream results", and "the statements of their premises and scope" of
Main's headline results are roots of its proof graph (Code Review Rules). At `bf89ba13` Main has no
appendix; "a Main appendix" below is a new section at the end of Main, which is still Main. No order of the
companion papers is declared on `main`, and SM and GR cite each other (33 bracket citations of GR in SM, 34
of SM in GR, counted at `bf89ba13`) [IR], so "the upstream-most downstream paper" is not determined there
for a result both use.

| Row (site now) | Kept text that refers to it | Named destination | Main independence | Safe? |
|---|---|---|---|---|
| AM-1.1 (Main:111–129, :135–137, recurrence clauses of :139; Main:435–437) | In Main: Main:157 (first sentence and "(Scope, above)"), Main:180, Main:338 item (2) ("on one fixed finite reversible representative is what the recurrence-scale theorem delivers"), Main:733 ("bare-recurrence form from a non-permutation rooted map at $t_R$"). In companions, sending the reader to Main for this proof: SM:24 ("the reader is directed to [Main] for the proof"), GR:22, Struct:1140, Struct:1255 ("[Main §3.4]'s non-permutation-witness lemma") | **(a) A Main appendix** of theorems about a fixed finite reversible realization. **(b) A companion**: SM names the result as an input "used in §2.1" (SM:24), GR for its §3.2 lemma and §8 (GR:22), Structure discusses it in §14.3 (Struct:1138–1140) | (a) No exposure: the appendix cites only Main's own lemmas (Main:131–133, :141–143, :516). Whether the Main-root rule allows it there depends on whether any root still uses it once the recurrence-cycle clause leaves Main:80 item (2) (H1) [needs trace]. (b) Main would then cite a companion at Main:157, :180, :338 (2) and :733 unless all four are rewritten to cite only AM-1.2 and AM-1.3a, which stay in Main | (a) yes. (b) only with those four Main sentences rewritten and SM:24, GR:22, Struct:1140, :1255 repointed in the same change; SM:24's "reproves none of [Main]'s foundational results" would also change. Which companion is not determined on `main` |
| AM-9.1 (Main:356's clause, :486, :496, :556, :558, :638) | Main:496 ("the per-horizon qualifier is load-bearing"), Main:558 ("it is precisely why the equivalence carries its subscript"), Main:562, Main:600 item (3) and "Per (3)", Main:731 (consolidation clause); family 40's four anchors at Main:638; guard `R7-RCL` pins Main:638's wording | **Main** (body, or the same Main appendix) | These sentences state the scope of Main's headline equivalence and are roots; the results they cite must stay in Main | **No destination outside Main is safe.** For this row Q2(b) reduces to Q2(a), or to a move inside Main |
| AM-16 (SM:294–296 in §4.2; SM:1606 in Appendix A) | Main cites [SM §4.2] at Main:500, :724 and :758 | **Stays in SM** (same sections), reframed as statements about the finite-torus model | Not changed by Q2(b). Main's existing citations of [SM §4.2] are citations of a companion by Main; whether they meet the Main-independence rule is outside this audit and is flagged here [IR] | yes |
| AM-32 (SM:112 in §3.1; SM:1654 in Appendix A) | Main cites [SM §3.1] at Main:412 and :414 | **Stays in SM** (same sections) | As AM-16 [IR] | yes |
| AM-33.2 (GR A.8, A.9: GR:797–809, :835–839) | none in Main (Main cites no GR section) | **Stays in GR's Appendix A** | No exposure | yes |
| AM-34 (Sub:331–346, §4.1) | none in Main (Main cites [Substratum §3.3] at Main:20 only) | **Stays in Substratum §4.1** | No exposure | yes |
| AM-37 (Struct:1255) | none in Main (Main cites [Structure] at Main:284 only, for Definition 9.2 and Propositions 9.7a–9.7b) | **Stays in Structure**, where it stands (Struct:1255) | No exposure | yes |
| Main:274–278, on r4's reading only | Main:278, Main:522 ("is the special case and is unchanged"), Main:724 item (iii) ("the uniform-prior doubly stochastic scope"), AM-5's kept special case | **A Main appendix only** | A companion destination would make Main:522 and ledger item (iii) cite it | only inside Main; **[reviewer reading, unresolved]**: it does not move at all |
| Landing AM-2.1 (Main:330–332), if recovered | Main:60, :338, :354; Intro:111; book B.2.5 | **Stays in Main §3.2** | No exposure | yes |
| AM-8 under Q7(d) (Main:742–760) | Main:159, :169, :656, :724 items (ii), (ix) | **Stays in Main §4.6**, or the Main appendix | No exposure. A move to Substratum (Sub:401) would need (EM) and `τ_B` moved into Main §1.3 or §2.3 and Main:169's and :656's references removed (AM-8, P8-S) | yes in Main; in Substratum only with those rewrites |
| N-1's period bound under Q10(c) (`ch18-beyond.md` §18.7) | book only | **Stays in the chapter**, with its FULL mirror | No paper exposure | yes |
| AM-5b (Main:290–324) | the census anchors at Main:312 and :314; other kept text that refers to the passage was not searched for (focused confirmation of r8) | **Stays in Main §3.2** | No exposure | yes |
| A recovery that fails (its finite-model form) | as the row's present statement | **Stays where the row's statement is now** | Unchanged | yes |

Population of this table: 13 lines: the 7 rows of the adopted 17 that are kept with their paper proofs under Q2(b) (AM-1.1, AM-9.1, AM-16, AM-32, AM-33.2, AM-34, AM-37), Main:274–278 on r4's reading, three RM landings (AM-2.1; AM-8 under Q7(d); N-1's bound under Q10(c)), AM-5b and the general case of a recovery that fails (7 + 1 + 3 + 1 + 1). The column "Kept text that refers to it", and the list under "Withdrawals need the same check" below, give the sentences this audit found; neither is claimed complete (§21).

**Withdrawals need the same check** [IR]. A statement withdrawn from the text under Q2(b) leaves kept
sentences that refer to it, which are reworded in the same change: AM-4.1 (Lemma 3's finite-cycle and
maximal-entropy clauses, Main:54; referred to at Main:58, :60, :280 and ledger item (iv), Main:724); AM-27.1
and AM-27.2 (Main:588, Main:80 item (4), GR:256–274, Intro:129, `ch01-observation.md:165`,
`ch19-open-problems.md:126`); AM-28 (the forcing sentence of Main:145); N-5 (`ch18-beyond.md:74`); AM-6.1
(Main:216).

**Result.** With destinations named, Q2(b) moves one row between sections or papers (AM-1.1), reframes five
where they stand, cannot move AM-9.1 out of Main, and withdraws six statements whose mathematics stays in
Lean or was an import. **Q2(b) is not decision-ready until the owner agrees the destination of AM-1.1 and
the standing of Main:274–278, and until the root trace for AM-1.1 is made** [needs trace]. It is an option
only; nothing here chooses it.

**Counts conditional on owner answers.**
- Q2: no category count changes under either answer; only placement does (§12.1).
- Q7: (a) or (b) moves AM-8 to RECOVER (17), landing TD [IR]; (c) moves it to REMOVE (11); (d) moves it to
  RECAST-MATHEMATICAL (18).
- Q3: replacing N-3 by the different commitment moves it to RECAST-WORDING (4), as a replacement and not a recovery
  of the original property; retiring it moves it to REMOVE (11).
- Q4: (a) retiring item (ii) moves N-6 to REMOVE (11); (b1) restating it as the named hypothesis of kept
  A1-test conditionals moves it to RECAST-WORDING (4); (b2) restating it with new content replaces it by a
  stated premise under §A.29 (not REMOVE).
- Q5(b), Q5(d) or Q6(c) adopting a premise: AM-3.2 or AM-4.3 is replaced by a stated premise under §A.29 (not
  REMOVE), and the RECOVER rows gated on that question can proceed. Q6(d) changes no row's category.
- Q1(a) only: P7 and part (3) of P9 are unavailable, so AM-22 and AM-36 cannot be recovered as planned and would
  become RM (their finite-model forms) or REMOVE, and AM-31 is kept in its parts (1) and (2); AM-11 and AM-24 lose
  P7. Q1(c) no: AM-33.2 stays RM with no
  physical reading.
- Q9 keeping the A1-test candidates: two REMOVE rows become explicitly conditional statements.
- Q11 extending the condition to total-sector statements: AM-3.1 and the TD landings (AM-7.1, AM-21.1, AM-21.2,
  AM-23.2, AM-33.1, and AM-8 under Q7(a), (b)) lose their forward reading; the RECOVER rows that need a premise
  about the total carrier (L1, L9) cannot proceed.
- A RECOVER row whose proof fails becomes RECAST-MATHEMATICAL (its finite-model form stays true) or REMOVE. No row has recovery credit; a row whose route uses EF-1 r6 is a candidate, and not a recovered result, until its proof is checked against the
  properties its theorem uses (§0, §14.3).

### 12.3 Claims needed, direct-proof target and concession, row by row

Adopted direction (c.6897946443): "If a result concerns only a finite experiment, ask whether we can prove that observable
conclusion directly. We need not reconstruct an autonomous finite universe, global recurrence or a global
invariant measure unless the proof genuinely requires them. A new direct proof could avoid conditions needed
by the old proof." The table applies that to all 57 rows, with the key K1–K6 of §0.

Columns. *Claims the content needs*: only those of the six that the row's content needs, with anything it
needs outside the six named. *Observable?*: whether the row's content is an observable conclusion about a
finite experiment: yes, partly or no. *Target or reason*: for yes and partly, (b) the observable conclusion
stated on its own, the weakest sufficient direct route found in this audit's trace of the proof, and the
conditions of the old proof that the direct route would avoid; for no, (c) why: the content is about the whole
system, about all time, or about a model property. *Concession*: the category of adopted direction c.6897946443 if recovery is not available: FM, "survive only as finite-model mathematics"; RT, "need replacement theorems"; CD, "remain
conditional", with the condition named; "—", nothing to concede (the row is kept as stated, or is wording).

Every (b) entry that names a route not on `main` carries the marking **[IR; candidate direct-proof target; no proof given; not a recovery]**.
It names a target, not a result. The routes and the "avoided" conditions are read from this audit's own
traces (§14.3), which are unreviewed; no condition is removed on the strength of this table, and none may be
until a reviewed trace supports it (adopted direction, c.6897946443: "The exact conditions we can remove must come from the reviewed
proof traces, not from the summaries alone."). A recovery class is not changed by a target, and the categories
and classes of §12 and §14.1 stand as they are.

| # | Row | Claims the content needs | Observable? | Target or reason | Concession |
|---|---|---|---|---|---|
| 1 | AM-1.1 | K6, and for the counting form a counting prior on a finite carrier (Main:115, :121) | no | (c) A model property and all time: the conclusion is the return at the order of a finite bijection, beyond any accessible window | FM |
| 2 | AM-1.2 | none of the six: a statement about any family of stochastic matrices | yes | (b) Conclusion: an observed overlap at `s` and an observed identity return at an accessible `n > s` certify P-indivisibility on `{0, …, n}`. Route: already direct on `main` (Main:141–143; kernel). Avoided: a finite carrier, a bijection, a hidden prior | — |
| 3 | AM-1.3a | none of the six | yes | (b) Conclusion: a measured revival of distinguishability on an accessible window certifies P-indivisibility on that window. Route: already direct (Main:157; kernel-only `c4r_implies_pIndivisible`). Avoided: every hidden-sector condition | — |
| 4 | AM-1.3b | as stated K6 with an exact return; the observable part needs K2 only | partly | (b) Conclusion: nature's visible process is P-indivisible on some accessible window. Route: none known. AM-1.3a certifies it from a measured revival, which is a witness and not a derivation; a derivation of a revival from C1–C4 or another visible-sector premise is not on `main`. Avoided, if one is found: the finite carrier and its recurrence. [IR; candidate direct-proof target; no proof given; not a recovery]. The recurrence-scale part is all time (c) | RT |
| 5 | AM-2.1 | K2 and a constructed realization (Main:516, from Lemma 1); a constructed realization is K4 (ii); not the closure result (K4 (i)), not K6 | no | (c) A model property: the CP structure belongs to the chosen realization; its observable premise is AM-1.3a's | FM (its landing) |
| 6 | AM-2.2 | K6 with an exact return | no | (c) All time: nature's channel at the recurrence scale | FM (as AM-2.1); its input is AM-1.3b's (RT) |
| 7 | AM-3.1 | none of the six: a requirement on the total map that assumes no size | no | (c) The whole system: a requirement on nature's total dynamics (Q11) | — (kept as a stated requirement) |
| 8 | AM-3.2 | none of the six: bijectivity of nature's own map on its whole carrier | no | (c) The whole system | CD: on reversibility as a named hypothesis; by item (xiii)'s form on the selected model |
| 9 | AM-4.1 | none of the six: lemmas about a bijection of a finite set | no | (c) A model property | FM |
| 10 | AM-4.2 | K1, K2, K3 (a uniform product prior, D2; its invariance, D3, for double stochasticity; D4) | partly | (b) Conclusion: the `k`-step visible transition matrices under a uniform product prior, for `k` inside the window, and their double stochasticity. Route: K1 + K2 + K3, as statements about the full system's record law (N3.2 for second-order rules; (M-full) for the locality class). Avoided: a finite hidden space, the division by its cardinality, K4, K6. Not avoided: that nature's prior is that one. [IR; candidate direct-proof target; no proof given; not a recovery] | FM; the direct target is conditional on D2 |
| 11 | AM-4.3 | none of the six: a selection among the invariant measures of nature's map | no | (c) The whole system | FM: the selection survives only as the default prior of a finite realization |
| 12 | AM-4.4 | K2, K3 (a measure equivariant under signed permutations) | partly | (b) Conclusion [IR]: the observer's quadratic response has the same spatial-to-temporal ratio in `T_1`, `E` and `A_1`. Route: K2 + K3 (equivariance), if the memory-resummed response is defined on a window; that definition was not traced, so whether the conclusion is one about a finite experiment is undetermined. Avoided: the counting measure of a finite carrier. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on an equivariant normalized measure, already a hypothesis of the extension clause (SM:334) |
| 13 | AM-5 | K2 and a constructed realization; none of K3, K4, K6 | yes | (b) Conclusion: the one-step visible law has the Born-form representation `P(j∣i) = Γ_1(i, j)`. Route: P1 on `main`'s finite-horizon equivalence. Avoided: a finite hidden space under A1, the uniform hidden state. [IR; candidate direct-proof target; no proof given; not a recovery] | — (lands RU; if P1 fails, FM) |
| 14 | AM-6.1 | none of the six: a finite environment (an external import) | no | (c) A model property | FM (import) |
| 15 | AM-6.2 | as stated, the carrier finite; the short-time estimate would need K1, K2, K3 | partly | (b) Conclusion: fundamental embedded-observer dynamics shows no first-order dissipative term at short times. Route: undetermined; the estimate of Main:340 with a window state in place of the finite hidden space has not been derived. Avoided, if it is: the finite hidden environment. [IR; candidate direct-proof target; no proof given; not a recovery]. The cardinality prediction is about the whole system (c) | removed under Q9(c), the recommended answer; CD on A1 only under Q9(a) |
| 16 | AM-7.1 | K1's dependency hypotheses only (finite reading sets); no finite alphabet, no K2 | partly | (b) Conclusion: an intervention on a region cannot change a readout at graph distance greater than `k` within `k` updates. Route: K1's dependency statement, with link L10 from apparatus to graph regions for the observable form. Avoided: finiteness of the whole site set, finite alphabets, any probability. [IR; candidate direct-proof target; no proof given; not a recovery]. Without L10 the statement is about the total dynamics (c) | CD: on finite reading sets as a named hypothesis; L10 for an observable form |
| 17 | AM-7.2 | K2, K3 (measurement independence), and the dependency statement with declared supports; not K1's finiteness, not K4, not K6; hypothesis (iii) read with a coupling graph in the dependency sense, and measurable response functions, both hypotheses on the class of completions excluded | yes | (b) Conclusion: no measurement-independent screened local deterministic completion gives observed correlations above the Bell ceiling (the statement lands NC: it constrains completions, not visible laws). Route: P4, for a measurable `Ω`. Avoided: a finite `Ω`, a finite site set, finite wing regions. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on measurement independence (item (xiv), a posit) and the theorem's other hypotheses |
| 18 | AM-7.3 | as AM-7.2, with the kernel's cone for the wave update | yes | (b) Conclusion: as AM-7.2, for response-complete completions on the reference graph. Route: the kernel cone and P4. Avoided: as AM-7.2. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on measurement independence, a hypothesis of the statement |
| 19 | AM-8 | K1 (the cone step), K2, K3 (an invariant reference state; (EM); typicality or (LE)); as stated, the carrier finite | no | (c) The whole system: where observers can sit; it establishes no constraint on the visible law at accessible times | FM, under Q7(d); otherwise CD on a reference state, (EM) and (LE) |
| 20 | AM-9.1 | K6: one fixed finite model for every experiment | no | (c) A model property | FM |
| 21 | AM-9.2 | K6; the per-window remark needs K1 only | partly | (b) Conclusion: prepare-and-measure behaviours over a window factor through the number of patch data. Route: K1 (with FS-all for the preparations and measurements); a true and very weak statement. Avoided: one fixed carrier. [IR; candidate direct-proof target; no proof given; not a recovery]. The obstruction for nature needs one model for all time (c) | removed under Q9(c), the recommended answer; CD on A1 only under Q9(a) |
| 22 | AM-10 | none: statements, not theorems | no | (c) Wording | — (wording) |
| 23 | AM-11 | a constructed realization per horizon; K2; K3 (a reference prior, the invariances of reciprocity, a shell measure); K6 for Stage 1's recurrence-cycle sentence | partly | (b) Conclusion: the observed temporal law has a finite reversible realization per accessible horizon (on `main`). The rest of the theorem is not traced here (P12), so no direct target is stated for it. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on the hypotheses of its inputs (AM-21.2, AM-22, AM-30) and on the class definition |
| 24 | AM-12 | K1, K2; K3 (equal patch marginals, D1) for the infinite-factor comparison | yes | (b) Conclusion: no finite-horizon visible law depends on a decoupled deep factor. Route: Main:60's argument, on `main`, for a finite factor; K1 + K2 + D1 for an infinite one. Avoided: the uniform prior on a finite hidden space. [IR; candidate direct-proof target; no proof given; not a recovery] | — |
| 25 | AM-13 | none | no | (c) Wording | — (wording) |
| 26 | AM-14 | K1, K2; K3 (D1) for a comparison of two carriers | yes | (b) Conclusion: the visible transition data on a window do not depend on the hidden sector beyond the cone. Route: K1 + K2 (Lemma PM (a), (b)); D1 for a comparison. Avoided: bijectivity, a finite product, the uniform prior. [IR; candidate direct-proof target; no proof given; not a recovery] | — (its H-BD statement stays conditional on H-BD) |
| 27 | AM-16 | none of the six: finite-torus models | no | (c) A model property | FM |
| 28 | AM-19 | none of the six: a finite-dimensional identifiability statement with `n` from Lemma 1 | yes | (b) Already direct on `main` (Main:228–260); nothing hidden is used | — |
| 29 | AM-20.1 | K2 and a constructed realization per horizon | yes | (b) Conclusion: a finite-horizon law has accessible memory exactly when it has, per horizon, a finite reversible realization with C1, C3 and C4. Route: on `main`, one direction at a time; P15 checks that no recurrence time is used. Avoided: `t_R`. [IR; candidate direct-proof target; no proof given; not a recovery] | — |
| 30 | AM-20.2 | none of the six: A1 stated as an identification | no | (c) The whole system | removed; the statement is A1 itself |
| 31 | AM-21.1 | K2 (a joint law of record and hidden state) | no | (c) The conclusion bounds nature's hidden conditional laws; the antecedent is observable. Changed after review; unreviewed. | CD: on a joint law (K2), as a conditional theorem |
| 32 | AM-21.2 | K2, K3 (a reference prior toward which the hidden sector relaxes; the mixing hypothesis) | partly | (b) Conclusion: the `k`-step visible matrix differs from the `k`-th power of the one-step matrix by at most `(k−1)ε` in total variation. Route: K2 + K3, with an independent bound on `ε`, which is not on `main`. Avoided: the uniform-prior marginal of a finite bijection, `t_R`. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on a reference prior as a named hypothesis |
| 33 | AM-22 | K2, K3 (a stationary law invariant under the dynamics and under time reversal, with time-reversal-even coarse states); the weights' form is the shell measure's (GR:58); as stated, the total system finite | yes | (b) Conclusion: the ratio of forward and backward visible transition rates is fixed by the energies, with the counting temperature. Route: none identified that avoids the shell measure. Detailed balance for the full system needs an invertible time-reversal-covariant rule, a stationary time-reversal-symmetric law, time-reversal-even coarse states (GR:68) and negligible boundary interaction (GR:58); the weights `Ω_H(E−e_i)` need that law to be the shell-counting one, which on a carrier of undetermined cardinality is a premise and not a product law. Avoided: a finite total system as such. Not avoided: the shell measure, H-count, the boundary mode count. [IR; candidate direct-proof target; no proof given; not a recovery] Changed after review; unreviewed. | CD: on a shell measure, H-count, an invertible time-reversal-covariant rule and the boundary mode count |
| 34 | AM-23.1 | none | no | (c) Wording: the A1 leg is redundant | — (wording) |
| 35 | AM-23.2 | K1 only | partly | (b) The dependence statement is about the total dynamics (c); an observable form would need oracle initial data excluded, which is not on `main`. Changed after review; unreviewed. Conclusion: no visible output at a finite step depends on infinitely many sites or computation steps. Route: K1, with finite supports over every branch or Lemma K's hypotheses. Avoided: a finite substratum. It does not exclude oracle initial data. [IR; candidate direct-proof target; no proof given; not a recovery] | RT: the restricted statement replaces the structural exclusion; conditional on K1's hypotheses |
| 36 | AM-24 | as AM-11 | partly | (b) As AM-11. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: as AM-11 |
| 37 | AM-25 | none of the six: kernel results on finite tori | no | (c) A model property | FM |
| 38 | AM-27.1 | none of the six: the monomial class on a finite carrier | no | (c) A model property: a negative for one model class | FM |
| 39 | AM-27.2 | none of the six: finite-torus substrata | no | (c) A model property | FM |
| 40 | AM-28 | K6: the period of a finite realization | no | (c) A model property and all time | FM |
| 41 | AM-29 | none of the six: kernel-only, finite sites and alphabet | no | (c) A model property | FM |
| 42 | AM-30 | K2, K3 (a prior of the form counting on `C_V` ⊗ `μ_H`, invariant under the dynamics, with `μ_H` invariant under `θ_H`); an invertible rule with `φ^{-1} = 𝒯φ𝒯` (SM:643); as stated, a finite hidden space | yes | (b) Conclusion: reciprocity of the `n`-step visible matrices, `T_ij(n) = T_{θj,θi}(n)`, for `n` inside the window. Route [IR]: time-reversal symmetry and invariance of the prior for the full system (N3.2 for second-order rules), as a statement about the record law. Avoided: the count over a finite hidden space, K4, K6. Not avoided: that nature's prior is that one. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: on an invariant, time-reversal-symmetric prior; bijectivity and T-invariance hold by item (xiii)'s form on the selected model |
| 43 | AM-31 | parts (1), (2): none; part (3): K1, K2 | partly | (b) Conclusion (part (3)): the conditional past-future information of the record, truncated at the horizon, is at most the logarithm of the number of patch data. Route: K1 + K2. Avoided: the total and hidden site counts, a hidden state at time `t`, a product prior. [IR; candidate direct-proof target; no proof given; not a recovery]. Part (1) is a property of the graph (c) | RT for part (3) (a per-window bound in place of the horizon-free one; conditional on a starting law); parts (1), (2) nothing to concede. Changed after review; unreviewed. |
| 44 | AM-32 | none of the six: finite-ring and finite-torus models | no | (c) A model property | FM |
| 45 | AM-33.1 | none of the six: injectivity of the dynamics on the whole carrier | no | (c) The whole system: the joint state with the hidden sector | CD: on injectivity as a named hypothesis; by item (xiii)'s form on the selected model |
| 46 | AM-33.2 | K6: full cycles of a finite isolated subsystem | no | (c) A model property and all time | FM |
| 47 | AM-34 | none of the six: a permutation of a finite set | no | (c) A model property | FM |
| 48 | AM-36 | (U1) as AM-22; (U2) the boundary mode count; S4 as AM-5; S2 none | partly | (b) Through (U1), AM-22's conclusion, for which no route that avoids the shell measure was found; S4 through AM-5's. [IR; candidate direct-proof target; no proof given; not a recovery] | CD: as AM-22 |
| 49 | AM-37 | K6: an asymptotic rate of a finite realization | no | (c) All time | FM |
| 50 | AM-38 | none of the six: kernel-only | no | (c) A model property | FM |
| 51 | N-1 | none of the six: the total carrier finite | no | (c) The whole system and all time | FM: the period bound of a finite permutation (Q10(c)) |
| 52 | N-2 | the total form: the carrier finite; the kept bound: K1, and K2 for an information quantity | partly | (b) Conclusion: the information accessible over a window is bounded by the number of patch data. Route: K1 + K2. Avoided: a finite total configuration space. [IR; candidate direct-proof target; no proof given; not a recovery]. Total information content is about the whole system (c) | RT: a per-window bound replaces the total one |
| 53 | N-3 | as stated: exact recurrence (K6 with a return, or the carrier finite) | no | (c) All time | RT: a different commitment under its own name; a replacement candidate, not a recovery |
| 54 | N-4 | none of the six: the carrier finite | no | (c) The whole system | removed; the statement is A1 itself |
| 55 | N-5 | K6: periodicity of the rooted laws of a finite realization | no | (c) A model property and all time | FM |
| 56 | N-6 | none: a ledger disposition | no | (c) Not a result | — (ledger; Q4) |
| 57 | AM-5b | K2, K3 (a uniform hidden input uncorrelated with the visible input: D2, D4), for one step; as stated, the finite `C_H` of §3.2 | no | (c) A model property: one-step properties of the channel of one displayed realization (Main:324). Changed after review; unreviewed. | FM |

**Counts of the direct-proof targets (population 57).** Observable conclusion about a finite experiment: **yes 11** (AM-1.2, AM-1.3a, AM-5, AM-7.2, AM-7.3, AM-12, AM-14, AM-19, AM-20.1, AM-22, AM-30); **partly 13** (AM-1.3b, AM-4.2, AM-4.4, AM-6.2, AM-7.1, AM-9.2, AM-11, AM-21.2, AM-23.2, AM-24, AM-31, AM-36, N-2); **no 33** (the 31 of r6, AM-21.1 and AM-5b). 11 + 13 + 33 = 57. Of the eleven "yes" rows, six are already direct on `main` (AM-1.2, AM-1.3a, AM-12 for a finite factor, AM-14 given GR:132's own hypotheses, AM-19, AM-20.1 subject to the check P15). Of the other five, AM-5 uses K2 with a constructed realization; AM-7.2 and AM-7.3 use K2 with measurement independence; AM-30 uses K2 with an invariant prior and an invertible time-reversal-covariant rule; for AM-22 no route was found that avoids a shell measure. No target's route uses the closure result (K4 (i)) or K6. Five rows (AM-2.1, AM-5, AM-11, AM-20.1, AM-24) use a constructed realization (K4 (ii)), which is on `main`. Of the thirteen "partly" rows, two have no route known (AM-1.3b, AM-6.2) and two have no observable conclusion to target beyond what is on `main` (AM-11 with AM-24).

**Counts of the concession categories (population 57).** FM **23**; RT **5**; CD **13**; removed with no surviving form **4**; nothing to concede **12**. 23 + 5 + 13 + 4 + 12 = 57. The rows are listed in §12.4. These counts are a second classification of the same 57 rows.


### 12.4 Conceded

Adopted direction (c.6897946443): "effective finiteness does not, by itself, recover A1's full role. Some results may
survive only as finite-model mathematics; some may need replacement theorems; others may remain conditional.
That is an acceptable scientific outcome."

What this audit concedes, at the default answers and on the evidence it has. Nothing here is a decision; each
entry follows the row's treatment in §2 to §7 and its class in §14.1.

- **Survive only as finite-model mathematics (23; population 57).** AM-1.1, AM-2.1, AM-2.2, AM-5b, AM-4.1, AM-4.2, AM-4.3, AM-6.1, AM-8, AM-9.1, AM-16, AM-25, AM-27.1, AM-27.2, AM-28, AM-29, AM-32, AM-33.2, AM-34, AM-37, AM-38, N-1, N-5. For each, the
  statement is true of the finite models it is about, and its reading for nature is not asserted. AM-2.1 is
  here by its landing (a statement about a chosen realization), AM-4.2 with a direct target that is conditional
  on a uniform product prior, AM-8 under the recommended Q7(d), and N-1 for its period bound only.
- **Need replacement theorems (5).** AM-1.3b, AM-23.2, AM-31 (part (3) only), N-2, N-3. AM-1.3b: a derivation of P-indivisibility on an
  accessible window from visible-sector premises, which is not on `main`; until one exists the claim for
  nature rests on a measured witness. AM-23.2: the restricted statement P16 in place of the structural
  exclusion. N-2: a per-window bound in place of finite total information content. N-3: a different commitment
  under its own name; it is a replacement candidate and not a recovery of the original property.
- **Remain conditional (13).** AM-3.2, AM-4.4, AM-7.1, AM-7.2, AM-7.3, AM-11, AM-21.1, AM-21.2, AM-22, AM-24, AM-30, AM-33.1, AM-36. The condition for each is in the table: bijectivity or injectivity of nature's dynamics (AM-3.2, AM-33.1); the locality hypotheses (AM-7.1); a joint law (AM-21.1); measurement independence and the theorem's other hypotheses (AM-7.2, AM-7.3); an equivariant measure (AM-4.4); a reference prior (AM-21.2); a shell measure with H-count (AM-22, AM-36); an invariant prior and an invertible time-reversal-covariant rule (AM-30); the hypotheses of its inputs (AM-11, AM-24).
- **Removed with no surviving form (4).** AM-6.2 and AM-9.2 (removed under Q9(c), the recommended answer; conditional on A1 only under Q9(a)); AM-20.2 and N-4 (the statement is A1 itself). r6 counted these four as "remain conditional"; the review of r6 (F3) separates them, and r7 agrees.
- **Nothing to concede (12).** AM-1.2, AM-1.3a, AM-3.1, AM-5, AM-10, AM-12, AM-13, AM-14, AM-19, AM-20.1, AM-23.1, N-6. They are A1-free on `main`, or kept as
  stated requirements or representability statements, or are wording and a ledger disposition.

**Also conceded, across rows.** One finite model valid for all time (K6) is not established, and no route
here supplies it. The closure result (K4 (i)) is checked under its stated hypotheses and earns no recovery credit: whether a closure preserves everything a particular audited result needs is unproved. No row, as now supported
on `main`, establishes a justified constraint on a visible law at accessible times (the provisional headline).

## 13. What would be lost (predictions and falsifiable claims)

The sites cited in this section are those this audit found; the lists are not claimed complete (§21).

If the REMOVE treatments are applied:
1. **Corner occupancy** (Main:216): "fundamental dynamics of continuous-time Markov type would require an
   actually infinite hidden sector", and `𝒟` read as its falsifiable residue (A1-test candidate 2).
2. **Cosmic recurrence** (F8, `appendix-a-prediction-status.md:181`; §18.7; `book/README.md:90`;
   `appendix-c-objections.md:132`): the prediction that nature's period is at most `g(|S|)`; with it the
   compact-topology remark's premise (`ch18-beyond.md:244`) and the constraint on theories of consciousness
   (`ch18-beyond.md:290`). Under Q10(c) the bound for a finite permutation stays as a statement about finite
   models.
3. **Recurrence-scale P-indivisibility of nature's visible process** (Main:626 "unconditionally"), the
   CP-indivisibility of nature's channel (B.2.5's reading), and the derivation behind the stated
   "framework-distinctive prediction, that this memory is specifically P-indivisible" (Cx:434), which is
   undecided by its venue and has no other derivation on `main` (Cx:430). P-indivisibility remains testable
   through a measured revival (AM-1.3a), a witness, not a prediction.
4. **The structural claim of the falsifiability statement** (Main:718) changes from "a finite set with a
   deterministic bijection" to undetermined cardinality.
5. **Finite total information content** (`ch18-beyond.md:168`) and the Layer 0 example "finite cardinality"
   (`appendix-a-prediction-status.md:48`).
6. **The fixed-finite-carrier consequences for nature** (Main:60's "bear on nature through it"; Main:356, :486,
   :558; A1-test candidate 1). Double stochasticity is not lost as a consequence of A1, since it is not one
   (§11 item 3).
7. **Book Chapter 1's stated central result** (`ch01-observation.md:93`, FULL:428) and the preface and
   introduction sentences of §8 lose their physical reading.
8. **If AM-8 is removed (Q7(c)) or kept only as a finite-model theorem (Q7(d)):** the conditional
   anti-Boltzmann-brain exclusion for nature (Main:754; Cx:212), the observer-selection rule that replaces the
   past hypothesis (Main:742, :756), and the selection content of Substratum's arrow-of-time projection
   (Sub:401). Under Q7(d) the theorems stay as mathematics about finite models.
9. **If AM-22 is not recovered:** the counting link of the horizon calibration (`ħ = c³ε²/(4Gσ)`,
   `ε = 2√σ l_p`, the 1/4 coefficient; `appendix-a-prediction-status.md:117`) and Stage 3 of Theorem 23.
10. **If AM-7 is not recovered:** the Bell ceiling's and the Bell–lattice corollary's bearing on an infinite
    lattice (Main:20, :414, :650, :770).
11. **If P16 is not proved:** the structural exclusion of infinite-time hypercomputation
    (`ch14-quantum-computing.md:90`).
12. **Under Q2(b):** no mathematics is lost. Five RM statements are withdrawn from the text with their
    mathematics kept in Lean (among them the EXACT sourcing negatives and the monomial-class characterization
    boxes, GR:258, :268, :274); seven keep their paper proofs, five of them in the paper they are in (GR A.8–A.9,
    Substratum's Proposition 24.4, the SM finite-torus and finite-ring statements, Struct:1255; G11 stays Open),
    the §3.4 fixed-carrier obstructions inside Main, and the finite recurrence-cycle theorems at a destination
    still to be agreed (§12.2); one definition is restated in place [reviewer reading, unresolved]; and AM-6.1's
    application of an external import is withdrawn.

Master tables: F8 is the one table row removed (ID retired). By this audit's reading [IR] the SM, neutrino and
biology rows do not consume A1.

## 14. New proofs and checks needed; recovery requirements; finiteness premises

P2 is retired (answered on `main`, Main:516, :518; ID not reused). "Premises added" names every premise a proof
would need that is not already a named hypothesis on `main`; a proof marked **§A.29** waits on an owner decision
that would adopt a premise, and that decision must state in advance the existing results the premise preserves
(its controls) and deliver at least one independent prediction or postdiction. "Lands as" is the category of
the recovered statement (§0). "Form" is the finiteness form a route through EF-1 r6 needs (§0): F-each, F-one, or "—" when the route does not use
EF-1. Every F-each route is a candidate with no recovery credit until its proof is checked against the properties
its theorem uses (§14.3), and carries §0's condition on settings, inputs and adaptive policies. EF-1 r6 is pinned
while it awaits review, so every such route is provisional. "Premises added" keeps EF-1 r6's three groups apart: the
finiteness premises, the probability premise (a normalized starting law) and any further distributional property, each of which needs its own justification.

| Id | Statement | Proof route | Premises added | Gates | Form | Lands as | Effort | Paper | Rows |
|---|---|---|---|---|---|---|---|---|---|
| P1 | §3.2 channel and Born form with `ρ_H = diag μ_H`, `μ_H` a root-independent realization prior: `P(j∣i) = Γ_1(i, j)` | Main:288's computation with weights `μ_H(k)` in place of `1/m`; Kraus operators `√μ_H(k)⟨l∣U∣k⟩`; diagonal preservation already kernel-proved for any weight (`isDiag_Phi`) | none | — | — | RU (AM-5); RM (AM-2.1) | one line | Main | AM-5, AM-2.1, AM-36 |
| P3 | causal cone for finite reading sets on a carrier of any cardinality, with the union cone `U_k` and site-dependent alphabets; readout into another alphabet; the intervention form for two runs that differ only in the intervention on `A` | EF-1 r6's Lemma PM (a), pointwise form: kernel `iterate_dependsOnlyOn_ball`, `readout_unaffected_outside_ball` (`RegionTower.lean:283`, :304), one alphabet `Q`; paper step embedding the `S_i` into one alphabet and assembling the joint form (`site_iterate_dependsOnlyOn`, :297); the rule clause by the induction of EF-1 r6 N1.3 | finiteness and dependency: finite reading sets (L1) as a stated hypothesis, whose source is an undecided reading of item (ix) or (xiii), or a named hypothesis (Q8); no finite alphabet needed for the dependency; for the intervention form, a support of the intervention that holds in every state, which is the statement's own hypothesis. Probability premise: none. Further distributional property: none | Q8, Q11 | F-each (pointwise) | TD; CV part [IR] only with L10 | short | Main | AM-7, AM-8, AM-23.2 |
| P4 | Bell ceiling for a probability space `Ω` with measurable response functions; or, for lattice completions and a finite duration, the fixed-horizon `Ω_n` route | Main:364–383 with sums replaced by integrals, hypothesis (iii) read with a coupling graph in the dependency sense [IR]; or the finite-`Ω` proof applied to `Ω_n`, the pre-setting data on `W_A ∪ W_B ∪ A ∪ B` (EF-1 r6 N3.6; provisional) | measurable-`Ω` route: hypothesis (iii) read with a coupling graph in the dependency sense, and measurable response functions; both are hypotheses on the class of completions excluded, not premises about nature, and neither is on `main` as worded. `Ω_n` route: L1, L2 and finite `A`, `B`, `R_A`, `R_B` (FS-all for the one setting step; not separately stated on `main`), and a starting law for `p(Ω_n)`. Further distributional property, both routes: measurement independence (MI; EF-1 r6's D6), hypothesis (iv) and ledger item (xiv), a separate posit; not supplied by either route | — (the `Ω_n` route also Q8); none for the proof as a conditional theorem; the row's class is disputed (§14.1) | — (measurable `Ω`); F-each in the all-branch form, with the settings the same in the runs compared (`Ω_n` route; dependency coverage only) | NC | short, standard | Main | AM-7.2, AM-7.3 |
| P5a | C2 persistence form for a measurable hidden space and any reference prior | TV contraction under Markov kernels; telescoping; Fannes–Audenaert on finite `n_V` | none | — | — | TD | short | Main | AM-21.1, AM-11 |
| P5b | C2 mixing and process forms, `ε` the residue of relaxation toward `π_H` | P5a plus the mixing hypothesis (item (v)) | a physically selected reference prior `π_H` on nature's hidden sector — **§A.29** | Q6(c) | — | TD | short given P5a | Main | AM-21.2, AM-11 |
| P6 | Theorem 19: `T_ij(n) = T_{θj,θi}(n)` for a bijective, T-invariant `φ` on a measurable carrier with (counting on `C_V`) ⊗ `μ_H` `φ`-invariant and `μ_H` `θ_H`-invariant | SM:643's fibre map, with mass preservation from the two invariances | bijectivity and T-invariance on the infinite carrier; `φ`-invariance of (counting) ⊗ `μ_H` — **§A.29** | Q5, Q6(c) | — | CV | short | SM | AM-30, AM-11 |
| P7 | GR:58 and GR:70 on the boundary-layer energy shell with a normalized deep factor; exact when decoupled, approximate under H-BD | GR:58's counting on the finite shell, under its condition that the boundary interaction is negligible at the shell scale; GR:70's trajectory bijection on the shell, with GR:68's condition that the coarse states are time-reversal even | uniform counting on the boundary shell; a time-reversal-invariant bijection of the shell — **§A.29**; H-count, H-BD existing | Q1(b-mode), Q5, Q6(c) | not carried by the fixed-horizon lemma (EF-1 r6 N3.7); it needs an invariant shell measure, which (M-full) does not concern | CV | substantive | GR | AM-22, AM-36, AM-11 |
| P8-M | §4.6 in Main for a measure-preserving map with isometric Koopman operator: `τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε)` under (EM), `P_Σ` defined by a normalized invariant reference state; the anti-Boltzmann-brain corollary; the observer-selection rule under (LE) or a typicality premise | Main:752's proof with P3 for the round trip; check that invertibility is not used | a normalized invariant reference state on the total carrier — **§A.29**; (LE) as a named hypothesis, or a typicality statement for finite regions of an infinite carrier as a premise — **§A.29**; (EM) existing | Q6(c), Q7(a), Q8; Q5 if the invertibility check fails | F-each for the cone step only; the rest not carried | TD [IR] | moderate | Main | AM-8 |
| P8-S | §4.6 on a finite enclosing region approximately isolated under H-BD | canonical typicality on the region (or (LE)); H-BD bound | the normalized equilibrium state — **§A.29**; H-BD existing | Q6(c), Q7(b) | — | TD [IR] | substantive | Substratum | AM-8 (alternative) |
| P9 | Theorem 22 on a graph of any cardinality: (1) C1; (2) the C3 clause as stated; (3) a per-horizon cone bound on the horizon-`n` truncation of `I*` | (1) SM:1378 unchanged; (2) Main:512, :608 (c); (3) the history is a function of the patch datum (EF-1 r6 Lemma PM), so the truncated quantity is at most `log₂∣C_{U_n}∣` [IR; needs proof, including its form] | (1), (2): none. (3): finiteness and dependency: finite reading sets and a finite `V` (the theorem's own hypotheses), L2; starting law: a normalized one (L9), not a reading of item (iv) and not on `main` for a carrier of undetermined cardinality — **§A.29** (Q6(d)); further distributional property: none (no product prior, EF-G1) | (3): Q6(d), Q11, Q1(b-loc) | F-each, for the truncated quantity only; `I*` itself is F-one | TD (1); RU (2); TD (3), a CV part only with L10 [IR] | short | SM | AM-31 |
| P10 | A.7 for `C_D` an index set of any cardinality, `ℓ²(C_D)`, `φ_t` injective, `U_φ` an isometry | GR:791 unchanged; Schmidt across the finite-dimensional `VB` factor | injectivity of nature's dynamics on the hidden sector — **§A.29** if postulated | Q5 | — | TD | minor | GR | AM-33.1 |
| P11 | Theorem 24 (i) and (iii) for a normalized decoupled factor and a prior-preserving relabelling | Main:60's argument; for (iii)'s infinite-factor form, EF-1 r6 Lemma PM (b), (c) | none for the conditional theorem; a Q6-type premise for its application to nature's infinite deep sector | (Q6) | F-each (comparison; needs equal patch marginals, a further distributional property, D1) | RU | routine | Substratum | AM-12 (optional) |
| P12 | trace of Theorem 23's Stages 2–3 for A1; restated Theorem 23 and Lemma 23.0 for substrata of undetermined cardinality | trace, then substitution of P1, P5b, P6, P7; Stage 1's output replaced by a per-horizon finite realization | those of its inputs and the class definition | Q1(b-mode) (via P7), Q3, Q5, Q6(c) | F-each for Stage 1's constructed realization; its recurrence-cycle sentence (Sub:137) is not carried and is restated or dropped as AM-1.3b; Stages 2–3 untraced, possibly F-one (§20, T17) | untraced | substantive | Substratum | AM-11, AM-24 |
| P13 | Proposition 4b's extension clause on the infinite lattice: the memory-resummed response is defined for a normalized signed-permutation-equivariant product measure | check of SM:334–336's response definition | a normalized equivariant measure — **§A.29** | Q6(c) | — | CV [IR] | routine check | SM | AM-4.4 |
| P14 | the sourcing negatives on the quasilocal completion | open | none identified [IR] | — | — | RM | substantive | Main/GR | AM-27 (optional) |
| P15 | the characterization theorem's proof uses no `t_R` | read Main:516–520 and the readback lemma for `t_R` | none | — | — | RU | check | Main | AM-20.1 |
| P16 | no visible output at a finite step depends on infinitely many sites or computation steps | EF-1 r6's Lemma PM-I (a), (b), the all-branch form (provisional): the output at step `t` is a function of the initial data on one finite patch and of the inputs applied | finiteness and dependency: L1, L2 (Q8); a finite visible region with a site-local readout (L8) and inputs of finite support over every branch (FS-all), carried as named hypotheses [IR]; in place of FS-all, finite reads on every run, under Lemma K's other hypotheses, would serve. Probability premise: none. Further distributional property: none. Does not exclude oracle initial data | Q8, Q11 | F-each in the all-branch form, inputs the same in the runs compared or policy included | TD [IR] | short | Comp; `ch14` | AM-23.2 |

Population of this table: 17 proof units (P1, P3, P4, P5a, P5b, P6, P7, P8-M, P8-S, P9 to P16). P2 is retired and its identifier is not reused.

**Where they live.** P1, P3, P4, P5a, P5b, P8-M and P15 are inside Main with Main's own support (P3's Lemma PM inputs
are Main-level, §0). P6, P7, P8-S, P9, P10, P11, P12, P13 are downstream. P14 is optional.

### 14.1 Recovery classes: three separate counts, the contingent rows, and the fixed-horizon cross-tabulation

**Population.** The 19 rows with a recovery or owner route: the 16 RC rows and the 3 OP rows (AM-8, N-3,
N-6). The other 38 rows have no class. Definitions are in §0. **A class records no recovery, and no row has
recovery credit.**

| Row | Unit | Class | What the candidate proof needs | Uses EF-1 r6? | Status of the route |
|---|---|---|---|---|---|
| AM-2.1 | P1 | **FIRM** | none: a realization's root-independent prior (Main:516); `isDiag_Phi` for any weight | no | proof sketched; not on `main`; recovery not proved |
| AM-5 | P1 | **FIRM** | none | no | proof sketched; recovery not proved |
| AM-7.2 | P4 | **CONTINGENT** (disputed: FIRM in r6 and in the review of r6; both positions in the table "Classes under the one rule" below) | the theorem's own hypotheses (i)–(iv), measurement independence among them (ledger item (xiv), a posit); hypothesis (iii) read with a coupling graph in the dependency sense [IR]; measurable response functions (the review of r6, F10). The last two are not on `main` as worded; the reading is whether they count as hypotheses of the statement (Q8) | alternative route only (`Ω_n`; all-branch form; dependency coverage only; adds finite wing regions) | candidate; recovery not proved; the class does not rest on the fixed-horizon lemma |
| AM-7.3 | P3, P4 | **CONTINGENT** (disputed: FIRM in r6 and in the review of r6; both positions below) | finite range by construction (`leapFiniteRange`); measurement independence as a hypothesis of the corollary (Main:414); P4's measurable-response hypothesis, as AM-7.2, which is not on `main` as worded (Q8) | the pointwise cone, in its kernel form | candidate; recovery not proved; the class does not rest on the fixed-horizon lemma |
| AM-21.1 | P5a | **NEW**; a conditional theorem is available (disputed: FIRM in r6; FIRM by the conditional theorem and NEW for nature in the review of r6; both positions below) | for nature's hidden conditionals: that nature's joint process of record and hidden state has a law (L9), which is on `main` only as a hypothesis (GR:132; Sub:262) and falls under Q11. None for the conditional theorem, which is stated for any hidden space carrying a joint law (Lemma 1 for `n_V`) | no | proof sketched; recovery not proved |
| N-6 | owner | **FIRM** | nothing to prove: a ledger disposition (Q4(a) retire, or Q4(b1) restate as a named hypothesis that is not posited); Q4(b2) would be NEW | no | owner choice |
| AM-7.1 | P3 | **CONTINGENT** | finite reading sets (L1), by a reading of item (ix) or (xiii) (Q8); L10 for any visible-law constraint | yes (Lemma PM (a), pointwise) | candidate |
| AM-23.2 | P16 | **CONTINGENT** | L1, L2 by the same reading (Q8); a finite visible region (L8) and inputs of finite support over every branch (FS-all) as named hypotheses [IR] | yes (Lemma PM-I (a), (b), the all-branch form; provisional) | candidate, for a restricted statement |
| AM-33.1 | P10 | **CONTINGENT** (else NEW) | hidden-sector injectivity through posit (xiii)'s definitional invertibility (`a2_every_substratum`), a reading that widens that posit's listed role (Q5(d)); otherwise a postulate (Q5(b)) | no | proof sketched |
| AM-4.4 | P13 | **NEW**; a conditional theorem is available | a normalized signed-permutation-equivariant product measure on the infinite lattice (Q6(c)) | no | waits on Q6 |
| AM-8 | P8-M / P8-S | **NEW** | a normalized invariant reference state (Q6(c)); (LE) or a typicality premise (Q7); P3 | for the cone step only | waits on Q6, Q7 |
| AM-11 | P12 | **NEW** | through P5b, P6, P7 (Q5, Q6(c), Q1(b-mode)); the class definition (Q3) | Stage 1 uses the Lemma 1 route, not the patch lemma | waits |
| AM-21.2 | P5b | **NEW** | a physically selected reference prior `π_H` (Q6(c)) | no | waits on Q6 |
| AM-22 | P7 | **NEW** | uniform counting on the boundary shell (Q6(c)); a time-reversal bijection of the shell (Q5); the boundary layer finite by mode count (L5, Q1(b-mode)) | no (not carried, EF-1 r6 N3.7) | waits |
| AM-24 | with P12 | **NEW** | as AM-11 | as AM-11 | waits |
| AM-30 | P6 | **NEW** | bijectivity and T-invariance on the infinite carrier (Q5); `φ`-invariance of counting ⊗ `μ_H` (Q6(c)) | no | waits |
| AM-31 | P9 | **FIRM** for the theorem as stated; part (3) is a replacement part, in no class | for the theorem as stated (parts (1), (2)): Theorem 22's graph hypothesis (SM:1376); C1 proved without finiteness (SM:1378); the bound of Main:506–512; Lemma 1 (Main:46). For part (3), outside the class: a normalized starting law for nature (L9, Q6(d)); finite reading sets, a finite `V` and finite alphabets | part (3) only | candidate; parts (1), (2) need no premise beyond those listed; recovery not proved |
| AM-36 | P1, P7 | **NEW** | those of P7; (U2), (U3) on GR's boundary mode count (L5) | no (S2 needs no finiteness form) | waits |
| N-3 | owner | **replacement candidate** | the original property (exact recurrence) is not recoverable by any route found; the replacement uses L1, L2 (Q8) | no | owner choice (Q3); not a recovery |

**Counts.** FIRM **4** (AM-2.1, AM-5, AM-31, N-6). CONTINGENT **5** (AM-7.1, AM-7.2, AM-7.3, AM-23.2,
AM-33.1). NEW **9** (AM-4.4, AM-8, AM-11, AM-21.1, AM-21.2, AM-22, AM-24, AM-30, AM-36). Replacement candidate
**1** (N-3), outside the three recovery counts. 4 + 5 + 9 + 1 = 19 = 16 RC + 3 OP. By category: the 16 RC
rows are FIRM 3 (AM-2.1, AM-5, AM-31), CONTINGENT 5, NEW 8; the 3 OP rows are FIRM 1 (N-6), NEW 1 (AM-8),
replacement candidate 1 (N-3). By reason: 18 of the 19 have reason (i); AM-33.1 has reason (iii). FIRM means
neither that the route works nor that recovery is proved (§0). Three of these classes are disputed with the
review of r6 (AM-7.2, AM-7.3, AM-21.1); with the review's figure for those three rows (r6's rule, with AM-31 moved) the counts are
FIRM 7, CONTINGENT 3, NEW 8, replacement candidate 1, and the review gives its range for FIRM as 5 to 8. Under the review's proposed rule of application (F5) AM-21.1 is NEW, as here; the counts are then 6, 3, 9, 1.

**Dependence of the classes on EF-1.** No class rests on a statement of EF-1, and the re-pin to EF-1 r6
moves no row. Class by class:
- *The FIRM rows.* AM-2.1, AM-5 and AM-31 (the theorem as stated) use no EF-1 route, and N-6 is a ledger
  disposition.
- *The CONTINGENT rows.* AM-7.1 needs finite reading sets only, by the undecided reading of Q8; EF-1 r6 flags
  that premise off the selected model and assigns no class. AM-7.2 is routed through the measurable-`Ω`
  restatement (P4), which uses the dependency statement with declared supports `A` and `B` and no finite patch
  (Lemma PM-I (a)), and AM-7.3 through the kernel cone and P4; neither uses the per-run form, Lemma K, the
  memory clause, (M-full) or the closure result, and both are CONTINGENT on whether P4's two added hypotheses
  count as hypotheses of the statement (Q8; the review of r6, F10). AM-23.2 keeps a finite visible region and
  FS-all as named hypotheses. Lemma K, checked, would let finite reads on every run, under the lemma's other
  hypotheses, stand in place of FS-all, and the memory clause widens the input rules covered; either way the
  hypotheses are named ones and the reading of Q8 is still needed, so the row stays CONTINGENT. AM-33.1 uses
  no EF-1 route.
- *The NEW rows.* (M-full), checked, gives for a uniform product state on a carrier of the locality
  class, with finite alphabets, the invariance that AM-8 (P8-M) and AM-30 (P6) list among their premises.
  Each of those rows also needs a premise that (M-full) does not touch (that nature's reference state is that
  one, Q6(c); bijectivity and T-invariance on the infinite carrier, Q5), so each stays NEW with (M-full)
  counted or not. AM-22 and AM-36 need a shell measure, which (M-full) does not concern. AM-21.1 is NEW by
  L9, which no EF-1 statement supplies. AM-31's part (3), a replacement part in no class, needs the
  probability premise for nature's carrier.
- *The replacement candidate.* N-3's original property needs exact recurrence, which lies outside every
  window and which a window-valid closure does not supply.
- *The closure result* (Lemma C, Corollary C1 and Lemma C′; one independent check, the recheck of EF-1 r5).
  It earns no recovery credit yet, and no row changes class on it (adopted direction, c.6897859755). Table 5 of §14.3
  records, row by row, whether a closure could suffice; a "yes" there is a matter to be determined, not a class.
- *The trace comparison* (§20, T1–T32) found no difference that bears on a class.

**Classes under the one rule, with the positions of r6 and of the review of r6.** Changed after review; unreviewed. Population: the 19 recovery rows. For each FIRM row the last column lists the premises of the proposed route with their locations on `main`.

| Row | r6 | Review of r6 (adjudication 7, 3, 8, 1) | This audit, one rule | Premises (FIRM rows); reason (other rows) |
|---|---|---|---|---|
| AM-2.1 | FIRM | FIRM | FIRM | premises: Lemma 1 (Main:46); a finite realization with a root-independent prior (Main:516); diagonal preservation (Main:326–328; `isDiag_Phi`, `EquivalenceChain.lean:253`); the argument of Main:332; P-indivisibility of the population process on the window, the theorem's own hypothesis (Main:330) |
| AM-5 | FIRM | FIRM | FIRM | premises: Lemma 1 (Main:46); the finite-horizon realization (Main:97, :516); the kernel channel with a general hidden weight (`EquivalenceChain.lean:241–253`) |
| AM-31 | NEW by part (3) | FIRM; part (3) a replacement part | FIRM for the theorem as stated; part (3) a replacement part, in no class | premises: Theorem 22's graph hypothesis (SM:1376); C1 proved without finiteness (SM:1378); the bound of Main:506–512; Lemma 1 (Main:46) |
| N-6 | FIRM | FIRM | FIRM | a ledger disposition (Main:724); the route requires no premise |
| AM-7.1 | CONTINGENT | CONTINGENT | CONTINGENT | reading: whether item (ix) or (xiii) supplies finite reading sets (Q8) |
| AM-7.2 | FIRM | FIRM | CONTINGENT | P4 needs hypothesis (iii) read in the dependency sense and measurable response functions (F10); neither is on `main` as worded. Reading: whether they count as hypotheses of the statement (Q8) |
| AM-7.3 | FIRM | FIRM | CONTINGENT | P4's measurable-response hypothesis, as AM-7.2; the cone is the kernel's |
| AM-23.2 | CONTINGENT | CONTINGENT (NEW if L8 or FS-all is an assumption about nature) | CONTINGENT | reading: Q8; L8 and FS-all carried as named hypotheses |
| AM-33.1 | CONTINGENT (else NEW) | the same | CONTINGENT (else NEW) | reading: Q5(d) |
| AM-21.1 | FIRM | FIRM by the conditional theorem; NEW for nature | NEW; conditional theorem available | a joint law of record and hidden state (L9) is on `main` only as a hypothesis (GR:132; Sub:262) |
| AM-4.4 | NEW | NEW (FIRM by the conditional theorem) | NEW; conditional theorem available | the measure is named at SM:334; that the response is defined for it is not on `main` |
| AM-8, AM-11, AM-21.2, AM-22, AM-24, AM-30, AM-36 | NEW | NEW | NEW | a reference state, a shell measure or an invariant prior not on `main` |
| N-3 | replacement candidate | the same | replacement candidate | kept apart; in no class |

Counts: FIRM 4, CONTINGENT 5, NEW 9, replacement candidate 1; 4 + 5 + 9 + 1 = 19. The review's range is FIRM 5 to 8; this audit's 4 lies below it because the adopted rule (c.6898395533, quoted in §0), given after the review, excludes a route with any premise not on `main`, which removes AM-7.2 and AM-7.3 (F10's two hypotheses) and AM-21.1. **The three rows in dispute, both positions.** AM-7.2: the review of r6, FIRM in its adjudication, with P4's two added hypotheses (hypothesis (iii) read with a coupling graph in the dependency sense; measurable response functions) taken as "hypotheses on the class of completions excluded, not premises about nature" (its F10); the review also says that P4 "is not premise-free" and that the comparison of routes is "undetermined until P4 is written" (its section 11, item 5). For the reading as FIRM: the dependency-sense graph is the hypothesis of the kernel cone lemma on `main` (`CouplingGraph`, `RegionTower.lean:254`; `iterate_dependsOnlyOn_ball`, :283); this audit, CONTINGENT, because neither hypothesis is on `main` as worded, so whether they count as hypotheses of the statement is a reading the owner decides (Q8). AM-7.3: the review, FIRM in its adjudication, on the same ground; this audit, CONTINGENT, because the corollary's route passes through P4 and inherits its measurable-response hypothesis, the cone itself being the kernel's (`leapFiniteRange`). AM-21.1: the review, FIRM classed by the conditional theorem and NEW classed by what asserting the result of nature needs (its F5); this audit, NEW with the conditional theorem available, because the row's claim concerns nature's hidden conditionals and a joint law of record and hidden state (L9) is on `main` only as a hypothesis (GR:132; Sub:262). Neither side is settled; the owner decides (§20). The kernel identifiers cited were read by r5 and r6, not by the review.

**AM-7.2 and AM-7.3 after the focused confirmation of r8: both positions, side by side.** Added in r9; this audit's classes are unchanged. The rule for FIRM is the one quoted once in §0 (adopted direction, c.6898395533) and is not restated here. Two tests of "available" are in use under it (the focused confirmation of r8, its section 2). *Test 1, worded on `main`:* every hypothesis that the restated statement carries is on `main` as worded. *Test 2, needed of nature:* nothing further is needed to assert the row's claim as it lands. The two positions differ in the tests they apply. The adopted words do not choose between them: the difference is whether a hypothesis that only narrows the class a no-go excludes is a "premise required by the proposed route".

| | This audit (classes unchanged in r9) | Focused confirmation of r8 (a recommendation; the owner decides) |
|---|---|---|
| Test applied | both: FIRM only if nothing further is needed of nature (test 2) and every hypothesis the restated statement carries is worded on `main` (test 1) | test 2 in full; test 1 is not applied to a hypothesis that only narrows the class a no-go excludes, which it does not count as a premise required by the route |
| AM-7.2 | CONTINGENT: P4's two added hypotheses (hypothesis (iii) with a coupling graph in the dependency sense; measurable response functions) are not on `main` as worded | FIRM, with the scope of the excluded class stated. The row lands NC and asserts nothing of nature; the cone lemma for a dependency-sense graph on a carrier of any cardinality is a kernel statement on `main` (`RegionTower.lean:254–283`), so hypothesis (iii) read with that graph uses a hypothesis already named on `main`, though not in the prose of Main:362–386; measurable response functions are a condition for the statement's own objects to exist (the confirmation's own one-line argument; not on `main`; unreviewed); no ledger item and no option of Q8 changes whether the Bell statement must carry the two hypotheses. What the restatement costs is scope, not a premise: the class excluded is the class of completions with a dependency-sense graph and defined outcome probabilities, and the row must say so |
| AM-7.3 | CONTINGENT: the corollary's route passes through P4 and inherits its measurable-response hypothesis; the cone is the kernel's | FIRM, with the same scope note. The cone is the kernel's by construction (`leapFiniteRange`, `SecondOrderDrive.lean:306`; `gateRegion`, `SecondOrderLayer.lean:208`), for a site type of any cardinality; measurement independence is a hypothesis of the corollary as stated (Main:414) |
| AM-21.1 | NEW; a conditional theorem is available | NEW; a conditional theorem is available (as this audit) |
| Counts: FIRM, CONTINGENT, NEW, replacement candidate | 4, 5, 9, 1 | 6, 3, 9, 1 (FIRM: AM-2.1, AM-5, AM-7.2, AM-7.3, AM-31, N-6; CONTINGENT: AM-7.1, AM-23.2, AM-33.1) |

Both are consistent applications of the one rule. The range for FIRM is 4 to 6, and AM-7.2 and AM-7.3 are the only rows that move. Limits of the confirmation's recommendation, in its own statement: its argument for measurable response functions was made there and checked by no one, and P4 has not been written. Under either position FIRM means neither that the route works nor that recovery is proved, and no row has recovery credit. Neither position is settled; the owner decides, on the rule itself (§0; §20).

**How this differs from the review of r4's 6, 5 and 8.** Five rows. N-3: contingent there, a replacement
candidate here (adopted direction, c.6896890693). AM-31: contingent there by its part (3); FIRM here for the theorem as it is
stated on `main`, which parts (1) and (2) cover, with part (3) a replacement part in no class (the review of r6,
F7); for an infinite hidden sector part (2) says nothing, so the row's content beyond part (1) is then carried
only by part (3). AM-7.2, AM-7.3: firm there, CONTINGENT here (F10). AM-21.1: firm there, NEW here (L9).

**The CONTINGENT rows: reading, basis, decision, disposition.** "Decides" is the owner in every row. No
CONTINGENT row is counted as recoverable under available premises.

| Row | Exact reading needed | Textual basis (file:line, quoted) | Who decides | If the reading is accepted | If it is rejected |
|---|---|---|---|---|---|
| AM-7.1 | Finite reading sets hold on one carrier of undetermined cardinality, taken from item (ix) restated for one carrier, or from item (xiii) with its listed consumers extended to §3.3, or carried as a named hypothesis of the §3.3 statement | Main:362: "Finiteness of $V$ is used in the first step". Main:724 (ix): "one degree bound across the family of finite representatives — at a single finite lattice the bound holds automatically, so the item has content only in family form". Main:724 (xiii): "for the continuous path of $*$-automorphisms from the identity to the update in §3.2 and §3.4, (xiii) the second-order form of the update, a posit of the selected lattice model, not derived and not an axiom of OI" and "with each $F_i$ reading the current values at finitely many sites" | owner, Q8, with Q11 | candidate (P3), not recovered until checked; lands TD; under Q8(c) a conditional theorem whose hypothesis is named | Main:362 stays a statement for a finite site set (RM); Main:20's cone sentence leaves the abstract (H1); AM-8 and AM-23.2 lose P3; AM-7.3 is unaffected |
| AM-23.2 | The same reading, and a finite alphabet at each site, for the substratum the book speaks of. (Beyond the reading, the restated sentence carries a finite visible region and inputs of finite support as named hypotheses [IR]; if the owner counts either as an assumption about nature the row is NEW) | `ch14-quantum-computing.md:90`: "infinite-time computation requires actual infinity, which the framework's finite substratum precludes (a structural exclusion)". Main:724 (xiii): "each site of (viii) carries a previous and a current value in a finite abelian group" | owner, Q8, with Q11 | candidate (P16) for the restricted statement; lands TD | the structural exclusion is removed (RX) |
| AM-33.1 | Posit (xiii)'s second-order form supplies injectivity of the whole dynamics on any site set, beyond its listed role | Main:724 (xiii): "in phase-space form $(x(t-1), x(t)) \mapsto (x(t), F(x(t)) - x(t-1))$"; `a2_every_substratum` (`SubstratumInterfaceAudit.lean:106`), definitional. GR:791 uses "Since $\varphi_t$ is injective" | owner, Q5(d), with Q8(b) | proof sketched (P10), selected model only; lands TD | Q5(b): NEW, a postulate under §A.29. Q5(a): A.7 is stated with injectivity as a named open hypothesis, or for finite models (RM) |
| AM-7.2 | P4's two added hypotheses count as hypotheses of the Bell statement, that is, as properties of the class of completions it excludes, and not as premises about nature: hypothesis (iii) read with a coupling graph in the dependency sense, and response functions measurable for the σ-algebra on which `p` is defined. Added in r8 from §14.1's class table; unreviewed | Main:384: "by the cone lemma and (iii)"; Main:362: "Finiteness of $V$ is used in the first step"; Main:372–374 states hypothesis (iv) and Main:364–365 that `Ω` "fixes each wing's response to every setting"; neither added hypothesis is worded on `main` (the review of r6, F10) | owner, Q8 | candidate (P4) for the ceiling on a carrier of undetermined cardinality, a conditional no-go about completions, landing NC; no recovery credit | the two hypotheses are then premises to be assumed, the row is not recoverable under available premises, and the statement stays conditional on them (§12.4, CD) [this audit's reading] |
| AM-7.3 | The same for measurable response functions alone; the cone is the kernel's and needs no reading. Added in r8 from §14.1's class table; unreviewed | Main:414: "every measurement-independent response-complete deterministic completion"; `leapFiniteRange` (`SecondOrderDrive.lean:306`) | owner, Q8 | candidate (P3, P4) for the corollary on the reference graph, landing NC; no recovery credit | as AM-7.2 |

Population of this table: the 5 CONTINGENT rows (AM-7.1, AM-23.2, AM-33.1; AM-7.2 and AM-7.3, whose lines were added in r8).

**Two rows the review of r4 listed as contingent, with both positions.**

| Row | The review of r4 | This audit |
|---|---|---|
| AM-31, part (3) | "Exact reading needed: For nature, item (iv) is replaced by bare normalization of the initial law on the patch data"; textual basis "No text on `main` states it"; decided by Q6(d) with Q11 and Q1(b-loc); if accepted, a candidate (P9) for the truncated bound, landing TD, a CV part only with L10; if rejected, "part (3) is class (b) or not stated; parts (1) and (2) stand without it (firm)" | The same evidence, a different label: since no text states it, there is no reading to accept or reject, and what is needed is a named assumption (L9). Part (3) is therefore a replacement part, in no class, and the row is FIRM for the theorem as stated (parts (1), (2)). Disposition if Q6(d) adopts L9: a candidate (P9) for the truncated bound, with no recovery credit. If Q6(d) declines it: part (3) is not stated; parts (1) and (2) stand; the Corollary follows them |
| N-3 | contingent: "The class property may be replaced by a different commitment"; decided by Q3 with Q8; if accepted, "replacement wording (RW)"; if rejected, retired (RX) | replacement candidate, outside the recovery counts, as adopted direction c.6896890693 asks. The dispositions are the same |

**The fixed-horizon candidates, cross-tabulated.** Population: the seven rows of the 19 for which r4 named
the fixed-horizon description as carrying the row or a named part of it. They are a **subset of the 19**,
not a further group, and every one of the seven is also counted in exactly one class above. Reason
categories (i), (ii), (iii) are those of §12, whose 48 + 6 + 3 covers all 57 rows.

| Row | Cat. | Reason | Class | Class (review of r4) | What the fixed-horizon lemma would carry | Finiteness premises (EF-1 r6 group A) | Probability premise (group B) | Further distributional property (group C) | Form assigned by |
|---|---|---|---|---|---|---|---|---|---|
| AM-7.1 | RC | (i) | CONTINGENT | contingent | the cone statement (pointwise) | L1 (Q8) | not needed | none | EF-1 r6 §4.2 |
| AM-7.2 | RC | (i) | CONTINGENT (by P4's added hypotheses, not by this route) | firm | the dependency part, for a finite duration (second route only) | L1, L2; finite `A`, `B`, `R_A`, `R_B` (FS-all for the one setting step; not separately stated on `main`) | the probabilities `p(Ω_n)` | measurement independence (D6): a separate posit, ledger item (xiv), needing its own justification | EF-1 r6 §4.2 |
| AM-7.3 | RC | (i) | CONTINGENT (the kernel cone; P4's measurable-response hypothesis) | firm | the cone (kernel, finite range by construction) | none beyond the rule's own form; the `Ω_n` route would add finite wing regions | as AM-7.2 on the `Ω_n` route | measurement independence, a hypothesis of the corollary | this audit [IR] |
| AM-23.2 | RC | (i) | CONTINGENT | contingent | the restricted statement | L1, L2 (Q8); L8, FS-all as named hypotheses [IR] | not needed | none | this audit [IR] |
| AM-31 | RC | (i) | FIRM for the theorem as stated; part (3) a replacement part, in no class | contingent (part (3)) | part (3) only, and only a truncated bound | finite reading sets, finite `V` (the theorem's hypotheses); L2 | needed (L9, Q6(d)) | none | this audit [IR] |
| N-3 | OP | (i) | replacement candidate | contingent | nothing of the original property; a replacement wording | L1, L2 (Q8) for the replacement | not needed | none | this audit [IR] |
| AM-36 | RC | (i) | NEW | NEW | nothing: S2 needs no finiteness form (review C4) | — | — | (U1) needs a shell measure (P7) | this audit [IR] |

**Totals of the overlap.** Of the seven: FIRM 1 (AM-31), CONTINGENT 4 (AM-7.1, AM-7.2, AM-7.3, AM-23.2), NEW 1
(AM-36), replacement candidate 1 (N-3); 1 + 4 + 1 + 1 = 7. With the labels of the review of r4: firm 2,
contingent 4, NEW 1. By reason: (i) 7, (ii) 0, (iii) 0. By category: RC 6, OP 1. The other 12 of the 19:
FIRM 3 (AM-2.1, AM-5, N-6), CONTINGENT 1 (AM-33.1), NEW 8 (AM-4.4, AM-8, AM-11, AM-21.1, AM-21.2, AM-22,
AM-24, AM-30); 3 + 1 + 8 = 12. Check: FIRM 1 + 3 = 4; CONTINGENT 4 + 1 = 5; NEW 1 + 8 = 9; replacement
candidate 1 + 0 = 1; 7 + 12 = 19.

**The cross-tabulation and EF-1.** The forms of AM-7.1 and AM-7.2 are those of EF-1 r6 §4.2, which adds that
AM-7.2's route needs the all-branch form (FS-all). EF-1 r6's own list of classes for which the fixed-horizon
form looks sufficient is a different population: five classes, two of them among these seven. §20, D23, gives
both.

**What the cross-tabulation shows.** No class among the seven rests on the fixed-horizon lemma. The one
FIRM row, AM-31, is FIRM through parts (1) and (2) of the theorem as stated, which use no finite patch; the
lemma would carry only its part (3), a replacement part. AM-7.2 is routed through the measurable-`Ω`
restatement and AM-7.3 through the kernel's finite-range cone; both are CONTINGENT through P4's added
hypotheses, and both carry measurement independence as a hypothesis the lemma does not supply. Of the seven, the
lemma would carry the whole of a row's statement only for AM-7.1 and AM-23.2 (both CONTINGENT), a part for
AM-7.2, AM-7.3 and AM-31, and nothing for N-3 and AM-36. Three NEW rows (AM-8, AM-11, AM-24) use a
fixed-horizon step for one stage and need more. Outside the 19, F-each appears as a remark in AM-12 and
AM-14 (RU, reason (ii)), AM-4.2 (RM), AM-6.2, AM-9 and N-2; none is a recovery. Rows whose content needs
F-one or a finite carrier, and are therefore not candidates: AM-1.1, AM-1.3b, AM-2.2, AM-9.1 and AM-9.2
(Main:638), N-1, N-2's total form, N-3 as stated, the horizon-free `I*` of AM-31, and possibly Stages 2–3 of
AM-11 and AM-24. **No row is recovered.**

**After recovery, if proved:** AM-2.1, AM-7.2, AM-7.3 constrain completions or chosen realizations, not the
visible law; AM-5 holds for every law; AM-21.1, AM-21.2, AM-23.2, AM-33.1 and AM-8 concern the hidden or
total sector (Q11), and AM-7.1 the total dynamics; AM-22, AM-30, AM-4.4 and, with L10, AM-7.1 could
establish a constraint; AM-31's part (3) and AM-36's (U1) in part; AM-11 and AM-24 untraced.

### 14.2 Premises of the fixed-horizon lemma and of the physically named finite sectors

"Open" means this audit cannot settle it from `main`.

| Premise | Where on `main` | Independent of A1? |
|---|---|---|
| L1. Each site's update reads finitely many sites (EF-1 r6's F3) | item (ix) "bounded coupling degree (A3)" and item (xiii) "each `F_i` reading the current values at finitely many sites" (Main:724); A3 (Sub:96); `leapFiniteRange` for the reference rule | As a statement, yes (none fixes `∣S∣`); it is a statement about every site of the total carrier, asserting no cardinality (Q11's kind). Open: item (ix) has content "only in family form", item (xiii) is a posit of the selected model with a stated consumer scope, and on an infinite product it cannot be obtained from single-component insensitivity, the step Main:362 uses finiteness for (EF-1 r6 N1.2; Q8). The cone is the union `U_n`, or the exact-step ball under `i ∈ N(i)`, which holds on the selected model (`gateRegion`) (EF-1 r6 N1.1) |
| L2. Finite per-site alphabet (EF-1 r6's F5, on the patch) | item (xiii) ("a finite abelian group"); A4's `ℤ_q` (Sub:98) | As a statement, yes. Open: A4's parenthesis "a finite periodic lattice" carries lattice finiteness and must be restated (Q3) |
| L3. Uniform degree bound on one carrier | A3; item (ix) in family form | Yes once restated for one carrier; open (Q8). Not needed for per-horizon finiteness, only for growth bounds (`∣U_n∣ ≤ ∣V∣ Σ_{k≤n} Δ^k`) and Main:758 (i)'s bounded-diameter regions |
| L4. Normalized product prior on the deep sector (of the kind of EF-1 r6's D1) | GR:132, as a hypothesis of a conditional theorem | Yes; needed only to compare two carriers' cone marginals (EF-G1); as a statement about nature it is not on `main`: new (Q6(c), §A.29) |
| L5. Boundary layer finite by mode count `A/ε²` | GR:90; S3 (GR:665); E3 (Sub:92) | Yes; a GR premise resting on the holographic input Main excludes (Main:700). Whether it is justified is open (the validity review's reading of E3, [IR]) |
| L6. Deep-boundary influence bound H-BD | GR §3.2, posited | Yes; open, including whether it holds for the framework's own linear rule at cuts with deep-boundary coupling (GR:128) |
| L7. Isolated hidden subsystem finite by mode count, under H-decouple | GR:787, :795, :835 | Yes; H-decouple "is not established here" (GR:787; GR:795 states the condition); open (Q1(c)) |
| L8. A finite visible region with a site-local readout (EF-1 r6's F4) | used on `main` for the spatial results, where the visible sector is a region of sites (Main:296; Main:744–746; GR:112); not stated as a separate premise, and finite there only through the finite site set (EF-1 r6 §4.0, where it is flagged) | Yes. Lemma 1 gives `∣C_V∣ < ∞`, not a readout depending on finitely many sites (EF-1 r6 AW-EF4); a premise of the spatial constitution (Q8). A finiteness premise |
| L9. A normalized starting law on the carrier (EF-1 r6's P1; with a policy, the joint law of the patch data and the policy information, its P2, which is not on `main`) | under A1, item (iv)'s counting measure supplies it; Main:58 makes a realization's prior "part of the realization datum"; for a carrier of undetermined cardinality it appears only as the hypothesis of a conditional (GR:132) or as a stated requirement (Sub:262) | Yes. The probability premise: it asserts no cardinality, but it is a statement about the total carrier (Q11's kind). It supplies probabilities on the finite description and is **not needed to establish finiteness** (adopted direction, c.6897254631). Needed for every forward-direction law statement; the reconstruction direction does not use it (EF-1 r6 N1.4). Not a reading of item (iv), which asserts a selection: a replacement of it for nature (Q6(d)), judged like any premise |
| L10. Identification of the observer's intervention and readout regions with coupling-graph regions, with their graph distance | not on `main`; Main:414: which propagation sets the physical light cone "is not derived here" | Yes; open. Needed for any CV part of the cone (r3 review B5) |
| FS. Finite support of interventions and policies, **all-branch form** (EF-1 r6's FS-all, its F7): at each step the set of all sites the policy could read, and that any intervention it could select could read or act on, taken over every record so far, every state and every value of the policy information, is finite | not stated as a separate premise; on `main` it follows from the finite site set of Main:362 ("with $V$ and each $S_i$ finite"); Main:366–369 says interventions read and write "only" their region without saying the region is finite; no read support of a setting generator or policy is stated (Main:406–407) | Yes. A premise to track (EF-1 r6 N1.5). The **per-run form** (finite reads of the policy and of the interventions on one given run; Lemma PM-I (a′)) gives a finite patch for that run and the runs that agree with it there; finite support on each individual run does not by itself give one finite patch for every branch, and neither does a bound on the size of each run's support (adopted direction, c.6897455387; EF-1 r6, examples E1–E3). **Lemma K** gives one such patch, with no bound on its size, from finite reads on every run, under the lemma's other hypotheses (a finite alphabet at every site; finitely many values of the policy information). Both were checked by the review of EF-1 r4; no class rests on either. A finiteness premise, as is the shared protocol the runs compared must have (EF-1 r6's F6, flagged for adaptive spatial policies) |
| MI. Measurement independence, `p(Ω ∣ a, b) = p(Ω)` | ledger item (xiv), "a posit about the initial condition, not derived" (Main:724); hypothesis (iv) of the Bell theorem (Main:372–374); "retained as a posit" (Main:404–405) | Yes, and independent of every dependency statement: including the setting and setting-generation regions gives dependency coverage, not MI (adopted direction, c.6896890693). A further distributional property (EF-1 r6's D6) and a separate posit; needs its own justification |

Population of this table: 12 premises (L1 to L10, FS, MI).

**The three groups, in these labels** (EF-1 r6 §4.0; each group needs its own justification, and none stands
in for another). *Finiteness premises (group A):* item (viii) (F1), determinism (F2), L1 (F3), L8 (F4) and,
with interventions, one shared protocol (F6) and FS-all (F7) give the dependency statement and a finite patch;
L2 (F5) then makes the set of patch data finite. This is the derived lemma (EF-1 r6 Lemma PM (a), Lemma PM-I
(a), (b)); it uses no probability. With finite reads on single runs only, the per-run form (Lemma PM-I (a′))
gives a patch for each such run and no description of the law. *Probability premise (group B):*
L9 (P1) puts a law on the description (Lemma PM (b)); with a policy it is the joint law of the patch data
and the policy information (P2; Lemma PM-I (c)). *Further distributional properties (group C),* none of which
the lemma uses or supplies: a product form across the patch boundary or equal patch marginals in two carriers
(D1; L4; a condition of comparisons); a uniform product prior (D2); invariance under the dynamics (D3), which
for the full system is (M-full) and which the description does not inherit automatically; independence of the visible initial
state from the hidden data (D4; `P_0 ⊗ μ_H`, Main:516); stationarity (D5); MI (D6); independence of the policy
information from the patch data (D7); a prior selected among invariant measures (D8). L3 adds growth bounds.
L5–L7 concern physically named sectors and L10 the link from apparatus to graph regions; EF-1 r6 has no
counterpart for L3, L5–L7 or L10. None gives F-one.

| Row | Rests on |
|---|---|
| AM-7.1 (P3) | L1 for the dependency (L2 only for a finite description); L10 for a CV part |
| AM-7.2 (`Ω_n` route) | L1, L2; finite `A`, `B`, `R_A`, `R_B` (FS-all, for the one setting step); L9 for `p(Ω_n)`; MI separately |
| AM-7.3 | L1, L2 by construction; MI as a hypothesis of the corollary |
| AM-8 (P8-M) | L1–L3 for `Σ_loc(V)`; a reference state of L4's kind (Q6(c)) |
| AM-23.2 (P16) | L1, L2; L8; FS-all (the restated sentence is one description for every input rule, so it needs one patch for every branch: FS-all, or finite reads on every run under Lemma K's other hypotheses) |
| AM-31 (P9), part (3) | L1 and a finite `V` (the theorem's hypotheses), L2; L9 |
| AM-36 | L5 for (U2); P7's premises for (U1); nothing for S2 |
| AM-22 (P7) | L5; L6 when the deep sector couples; a shell measure of L4's kind |
| AM-14 (tool) | L1, L9 for the law; L4 for the comparison |
| AM-6.2 (recovery note) | L1, L9; the cone sector is not isolated, so the finite-environment bound does not apply as stated |
| AM-11, AM-24 | L5 with L6 (E3's bound under H-BD); L1, L2, L9 for Stage 1's replacement |
| AM-12, Corollary (i) | L5; (iii)'s infinite-factor form L1, L9 |
| AM-33.2 | L7 |
| N-2 (kept accessible bound) | L5, or L1, L2, L9 per horizon |
| N-3 (replacement candidate) | Lemma 1, L1, L2; L5 optional |

Population of this table: 15 lines covering 16 rows (AM-11 and AM-24 share a line): the rows whose route or remark rests on a physically named finite sector or on the fixed-horizon lemma.

### 14.3 The adopted check on the fixed-horizon lemma, row by row

The question (adopted direction, c.6896252651): "is effective finiteness justified independently of A1, and is it sufficient for
the specific results it is meant to recover?" The standard (6896940222): a finite description "need not
preserve the original system's bijectivity, invariant measure, recurrence structure, or other properties a
downstream proof uses", and it has "no recovery credit until each theorem's actual requirements are checked."

*Justification.* Per-horizon finiteness is a derived lemma (§0). Its finiteness and dependency premises are
item (viii), determinism, L1, L8 and, with interventions, a shared protocol and FS-all; L2 makes the patch data
finitely many. None is A1. Two of them (L8, FS-all) are not separately stated premises on `main`, and L1's source
is an undecided reading (Q8). A normalized starting law (L9) adds probabilities and is not needed for
finiteness. F-one is not established. In EF-1 r6's labels these are F1–F5 with F6 and F7, and P1; its §4.0 flags F3 off the selected model, F4, F6 for adaptive policies, F7, and P1 for an infinite carrier.

*Sufficiency.* The tables below give, for every row whose candidate route uses EF-1 r6, the properties the
row's proof on `main` uses, **traced here from the proof itself with file and line**, and whether the
fixed-horizon description carries each (EF-1 r6 §P, with the correction of its review's finding 1). The traces
are r5's own: they were made after the review of EF-1 r3 had found r3's §4.2 column incomplete, and they are
carried unchanged. EF-1 r6 has since retraced its §4.2, and its review has checked that retrace. §20 (T1–T21) lists every difference
between the two sets of traces, and a cell below that is affected carries a pointer to its entry. **Every
row: no recovery credit; a recovery candidate is not a recovered result.** "Form assigned by" says whether the
form is in EF-1 r6 §4.2 or is this audit's own reading [IR], which no EF-1 review has checked. In Tables 1 and
2, "not defined on the patch", "not preserved" and "not carried" describe what the description has of its own;
they do not say that no suitable finite closed model exists, which is Table 5's question.

**Table 1. Rows whose candidate route uses the fixed-horizon lemma for the row or a named part.**

| Row / route | Properties the proof on `main` uses (traced; file:line) | Carried by the fixed-horizon description? | Form; assigned by | From the finiteness premises | From the probability premise | Further distributional property | Credit |
|---|---|---|---|---|---|---|---|
| AM-7.1 cone (P3) | Main:362: site factorization "$S=\prod_{i\in V}S_i$, with $V$ and each $S_i$ finite"; a coupling graph defined by one-step dependence, symmetrized; induction on `k`; "Finiteness of $V$ is used in the first step, where insensitivity to each single component outside the dependency set makes the $i$th output a function of the components in it"; an intervention that "reads and writes only region $A$" | Induction and cone: yes (Lemma PM (a); kernel `iterate_dependsOnlyOn_ball`). The first step: no; on an infinite carrier single-component insensitivity does not give finite dependency (EF-1 r6 N1.2), so finite reading sets become a hypothesis, and the reading sets must be the dependency sets of the graph Main measures distance in (EF-1 r6 N3.6) | F-each, pointwise; EF-1 r6 §4.2 (§20, T3, on the label of the intervention clause) | L1 only | nothing | none | none; candidate |
| AM-7.2 Bell ceiling, `Ω_n` route | Main:364–365: `Ω` "fixes each wing's response to every setting"; :366 determinism; :366–369 a product setting operation on disjoint regions at one step, "each intervention reading and writing only its own region"; :369–372 a `±1` readout on `R_A`, `k_A` updates after the setting, with $d(B, R_A) > k_A$, and symmetrically; :372–374 one common pre-setting ensemble, $p(\Omega\mid a,b)=p(\Omega)$; :374–375 "the protocol records a $\pm1$ outcome in every run"; :378–379 a sum over `Ω` with weights `p(Ω)`; proof :383–388: the post-setting state outside `B` does not depend on `b`, the cone lemma, determinism giving point masses, the common ensemble giving measurement independence, the pointwise identity and its average; :389 the sixteen tables checked exhaustively | Determinism, cone: yes. One variable covering every setting: yes, as the pre-setting data on `W_A ∪ W_B ∪ A ∪ B` (dependency coverage only). Its finiteness: only with `A`, `B`, `R_A`, `R_B` finite. The weights `p(Ω_n)`: only with a starting law. The common ensemble (MI): **not supplied**. An outcome in every run: a protocol hypothesis, unaffected | F-each for a given duration, in the all-branch form; EF-1 r6 §4.2 | L1, L2; finite `A`, `B`, `R_A`, `R_B` (FS-all for the one setting step; not separately stated on `main`) | `p(Ω_n)` (P1) | MI (D6): ledger item (xiv), a separate posit; needs its own justification | none; candidate for the dependency part only. The row's class (CONTINGENT) is set by P4's added hypotheses, not by this route |
| AM-7.3 Bell–lattice corollary | Main:414: the Bell-relevant degrees of freedom "governed entirely by the nearest-neighbor cubic wave-equation update"; settings "applied at one step to disjoint wing regions, each reading and writing only its own"; each wing's `±1` outcome "recorded in every run" and read from a region whose graph distance from the other wing's setting region "exceeds the number of updates from setting to readout"; the conclusion for "every measurement-independent response-complete deterministic completion" | Cone: yes, and in the kernel for a site type of any cardinality (`leapFiniteRange`). MI: a hypothesis of the statement, not supplied | F-each; this audit [IR] | none beyond the rule's own finite range; the `Ω_n` route would add finite wing regions | as AM-7.2 on the `Ω_n` route | MI, as a hypothesis | none; candidate. CONTINGENT: the kernel cone, with P4's measurable-response hypothesis |
| AM-23.2 hypercomputation (P16) | `ch14-quantum-computing.md:90`: no proof; the stated ground is that "the framework's finite substratum precludes" actual infinity, that is, finiteness of the carrier | Finiteness of the carrier: supplied by neither form. The restricted statement uses determinism and the cone with inputs: carried on one finite patch under FS-all (Lemma PM-I (a), (b)) | F-each; this audit [IR] | L1, L2 (Q8); L8; FS-all | nothing | none | none; candidate for a restricted statement |
| AM-31 part (3) (P9) | SM:1376: a connected bounded-degree coupling graph with diameter `D ≥ 4`, energy-conserving dynamics, a connected subgraph `V` with $\lvert V\rvert \leq N/3$; SM:1378 (C1): `G_φ` connected, `V` proper, so `∂V ≠ ∅`, and every edge a dynamical coupling; SM:1382 (C3): $\lvert H\rvert = N - \lvert V\rvert \geq 2N/3$, $\log_2\lvert\mathcal{C}_H\rvert = \lvert H\rvert \log_2 q$, and $I^* \leq \log_2\lvert\mathcal{C}_H\rvert$, which is Main:512, whose proof (Main:610 (c)) uses the Markov chain `X_{<t} → H_t → X_{t+1}` given `X_t` and `H(H_t) ≤ log₂∣C_H∣` | Connectivity and the boundary: unaffected by cardinality. `N`, `∣H∣`, `∣C_H∣`: absolute hidden counts, **not preserved**. A hidden state at time `t`: **not defined** on the patch (no self-map). The law of the record on `[0, n]`: preserved given a starting law, which bounds the truncated quantity by `log₂∣C_{U_n}∣` [IR] | F-each for the truncated quantity; `I*` itself F-one; this audit [IR] | finite reading sets and a finite `V` (the theorem's hypotheses); L2 | needed (L9) | none | none; candidate, and a restatement of the C3 clause, not a recovery of its horizon-free bound |
| N-3 "Finiteness" | `ch09-universality.md:106`: "the recurrence theorem (Chapter 18 §18.7) requires finiteness for the exact recurrence of a finite bijection, which supplies recurrence-scale P-indivisibility" | Exact recurrence: **not carried** (recurrence structure is not defined on the patch and is not shared between nature and a finite model, EF-1 r6 §P) | the original needs a finite carrier, or F-one with an exact return; this audit [IR] | for the replacement only: L1, L2 | nothing | none | none; **replacement candidate, not a recovery** |
| AM-36, S2 | GR:613: "any finite deterministic substratum"; C3 as "sufficient memory capacity — $N_H \gg N_V$ the comfortable regime"; GR:663: "high capacity (C3)" | nothing to carry: a lower bound on hidden capacity, true for a hidden sector of any cardinality | none needed; this audit [IR] | — | — | (U1) needs a shell measure (P7) | none |

Population of Table 1: the seven fixed-horizon candidates of §14.1 (AM-7.1, AM-7.2, AM-7.3, AM-23.2, AM-31, N-3, AM-36), a subset of the 19 recovery rows.

**Table 2. Rows that use a fixed-horizon step for one stage, or as a remark.**

| Row / route | Properties the proof on `main` uses (traced; file:line) | Carried? | Form | Further distributional property | Disposition |
|---|---|---|---|---|---|
| AM-8 §4.6 (P8-M), cone step | Main:742: "a finite bijective $(S, \varphi)$"; Main:744: `Σ_loc(V)` reached in at most `τ_S/Δt` steps; the exact Koopman operator "a permutation operator: unitary, with modulus-one spectrum and exact recurrence"; the compression $\mathcal{K}_\Sigma := P_\Sigma\, \mathcal{U}_\varphi\, P_\Sigma$; (EM); Main:746, :758 (i): `V` of bounded coupling-graph diameter; Main:750, :752, :756: canonical typicality [31] for the local-equilibrium state; Main:752: the round trip "stays within $\Sigma_{\text{loc}}(V)$" by the cone; Main:756: the rate condition $\tau_{\rm mix}\ll\tau_S$; Main:758: "bounded coupling, finiteness of $S$, the canonical-typicality result [31], and the effective-mixing hypothesis (EM)" | Cone: yes. The compression: needs a reference measure on the carrier, not supplied. Koopman spectrum and exact recurrence: not defined on the patch. Typicality of individual states: not preserved as stated | carrier finite; cone step F-each | an invariant normalized reference state; typicality or (LE) | NEW; waits on Q6(c), Q7 (§20, T18) |
| AM-11, AM-24 (P12), Stage 1 | Sub:125: "a triple $(S, \varphi, V)$ with $S$ finite, $\varphi$ a bijection on $S$". Stages 2–3 are **not traced here** (r9 §7.4) | Stage 1's output can be replaced by a per-horizon finite realization from Lemma 1 (Main:516–520), which is a constructed whole system, not the patch description; whether Stages 2–3 use anything uniform in the horizon is open | F-each for Stage 1's constructed realization; its recurrence-cycle sentence (Sub:137) is not carried; the rest undetermined | those of P5b, P6, P7 | NEW; waits (§20, T17: EF-1 r6 finds a recurrence-cycle clause inside Stage 1 and traces parts of Stages 2–3) |
| AM-12 (iii), infinite decoupled factor (P11) | Main:60: "the visible coordinate of the product map does not depend on the added coordinate and the added prior has total mass one"; Sub:262: "an infinite extension requires its own normalized measure or trace-class state and a well-defined evolution, and is not established by finite uniform counting". Theorem 24's own proof is **not traced in full here** | The dependence statement: yes. The comparison of two carriers: only with equal patch marginals | F-each, comparison | equal patch marginals (a product form with the same patch factor) | RU unchanged; P11 optional |
| AM-14 deep-sector corollary (tool) | GR:112: a bijective update on "a finite product of site configuration spaces", a coupling graph, a uniform hidden prior; GR:132: for an infinite deep sector "a normalized product prior on it, a locally finite coupling graph and well-defined dynamics … in which each component's update depends on finitely many components"; GR:134: sums over `C_{B_n}`, the update on `V ∪ B_{n−1}`, and "each visible component after $n$ updates is a function of finitely many initial components". The lemma's proof: (a) GR:124, the cone and the uniform prior only; (b) GR:126, injectivity of `φ` and H-BD | The dependence: yes (Lemma PM (a), (c)); bijectivity is not used by it. Equality of two carriers' laws: only with equal patch marginals | F-each, comparison | a normalized product prior (GR:132's own hypothesis) | RU unchanged (§20, T15: the lemma's proof is at GR:124–126, not GR:114) |
| AM-4.2 baseline `T` on an infinite carrier | Main:113: `φ` a bijection of a product of two finite sets; Main:115: `T_ij` a count over `C_H` divided by `∣C_H∣`; Main:129: "under the uniform hidden prior that defines $T$" | The ratio: yes, as a count over the patch under a uniform product prior. `∣C_H∣` itself: no. Double stochasticity: not by the description (see the measure table) | F-each | a uniform product prior; invariance for double stochasticity | RM unchanged; read of nature, the prior is a selection (Q6(c)) (§20, T5) |
| AM-6.2 corner occupancy | Main:216: Doukas's bound, "marginalization over a *finite* environment produces no first-order dissipative term, secular leakage requiring an infinite reservoir", called "the same structural fact as the second-order estimate of §3.2"; "conditional on the total-finiteness posit". That estimate is Main:340: a slow bath, a generator exactly Hamiltonian at `t = 0`, a bath state moving at rate `1/τ_B`, a bounded coupling `V_int`, and a weak-coupling condition | Not determined: Main:340 is a continuous-time estimate on a channel with a bath state, none of which is a property of the patch. In the native class a finite torus and the infinite lattice give the same observation law on a fixed horizon under a uniform product prior (EF-1 r6 N3.5), so the finite-versus-infinite alternative is not distinguished there | mixed (EF-1 r6 §4.2) | a uniform product prior in both carriers | RX; not carried |
| AM-9 remark; §11 item 1 | Main:558: one realization of `N < ∞` ontic configurations; the factorization `B = ΞM` through `N` states | Per horizon a count `N_eff(n)` of data on the enlarged patch exists; the fixed `N` is a one-description-for-every-horizon statement | F-each for the remark; the row needs F-one | — (FS-all for the preparations and measurements; §20, T19) | RM / RX unchanged |
| N-2 accessible information per horizon | `ch18-beyond.md:168`: the information content is "$\log_2 \lvert S\rvert$ bits — finite for any finite $S$", and "under the finiteness posit A1 … it is finite"; a count, with no proof beyond it | the per-horizon count: yes; total information content: no | F-each for the kept bound | a starting law for an information quantity | RX; the per-horizon form is optional |

Population of Table 2: 8 lines covering 8 rows (AM-8; AM-11 and AM-24; AM-12; AM-14; AM-4.2; AM-6.2; N-2), with one line for the remark under AM-9 (rows AM-9.1, AM-9.2) and §11 item 1, which is not a row.

**Table 3. Rows whose proof uses an invariant, uniform or counting measure.** Two things are kept apart for
each, as adopted directions c.6897455387 and c.6897859755 ask, in EF-1 r6's terms (§0). (a) **The full system.** On a
finite set every bijection preserves the counting measure (the step behind Main:274's "a uniform-prior
bijection marginal preserves the uniform distribution"). On an infinite product, preservation of the uniform
product measure is a separate statement about the whole system: EF-1 r6 N3.2 proves it for the second-order
form (checked by the review of EF-1 r2), and (M-full) proves it for every bijection of the locality class of
`main` with finite alphabets (checked by the review of EF-1 r4). (b) **What the proof needs of a finite
model:** a self-map of a finite carrier, a measure invariant under one, or only a property of the record law.
The description does not inherit a self-map or an invariant measure automatically from (a). That is not a
finding that no suitable finite closed model exists: whether a chosen, window-valid closure exists is the
subject of Lemma C, Corollary C1 and Lemma C′ of EF-1 r6, each checked once, under its stated hypotheses, by
the recheck of EF-1 r5 (the tiers of adopted direction c.6897859755 predate that check), and whether one could suffice for
the row is the window question of Table 5. r5 marked (b) open for every row, and it stays open (§20, D22). **No class in
this audit rests on (a), on (b) or on the closure result, and no class changes on it.** In column (b), where
EF-1 r6 §4.2 covers the row its requirement is given; elsewhere the entry is this audit's reading [IR].

| Row | The measure the proof uses (file:line) | (a) the full system | (b) what the proof needs of a finite model | Class, and why it does not rest on either |
|---|---|---|---|---|
| AM-1.1 | the uniform hidden prior defining `T` (Main:115, :129); a prior `μ_H` shared by every root, drawn independently of the root (Main:135) | holds on the finite realization the theorem is about | a bijection of a finite carrier with its counting measure, and its order (EF-1 r6 §4.2: needs the return `φ^N = id` of nature's own bijection, with its counting measure); the description has no such map of its own; for an all-horizon model the counting prior is a further requirement (§20, T8); Table 5 | RM; a theorem about finite models |
| AM-3.2 | double stochasticity of a bijection's marginal under the uniform prior, "each set $\{x_j\} \times \mathcal{C}_H$ has exactly $\lvert\mathcal{C}_H\rvert$ preimages" (Main:60) | finite-set statement; for an infinite carrier a separate statement about the full system (N3.2 for the second-order form; (M-full) for the locality class; false for B1) | a self-map of a finite set, its eventual image, and injective implies surjective (EF-1 r6 §4.2: needs nature's own map on a finite set, with its eventual image and the step from injective to surjective); these concern nature's own map; Table 5 | RX |
| AM-4.1, AM-4.3 | the counting measure, unique and uniform on each finite cycle, selected as maximal-entropy (Main:54) | finite-set statement; the selection has no infinite-carrier form on `main` | the set of invariant measures of a self-map (EF-1 r6 §4.2: needs the invariant measures of nature's own map on a finite set, and its orbits); the description has no map of its own, and a chosen closure's invariant measures are its own; Table 5 | RM; RX |
| AM-4.2 | the uniform prior defining `T` (Main:115) | as AM-1.1; for an infinite carrier the ratio needs a uniform patch marginal (D2, a premise), and double stochasticity needs invariance on the full system (D3): N3.2 for the second-order form; (M-full) for the locality class; no class uses either | record law only, for the ratio and for double stochasticity (EF-1 r6 §4.2: a uniform patch marginal (D2); for double stochasticity, invariance on the full system; no property of nature's own map beyond the window); the absolute count of hidden states is the model's, not the window's; Table 5 | RM |
| AM-4.4 | SM:334: "the selected counting measure, which is invariant under signed permutations of the components"; extensions "whose dynamics, measure and observer $\sigma$-algebra are equivariant under signed permutations of the six components (H-blind)"; SM:336: the counting measure "a product of identical factors" | a premise for an infinite lattice (Q6(c)) | no class in EF-1 r6; this audit [IR]: not traced as needing a finite model's map; whether the memory-resummed response uses invariance under the dynamics is part of P13's check; Table 5 | NEW, by that premise |
| AM-5 | `ρ_H = I_m/m` (Main:280), with `m^{-1/2}` in the Kraus operators (Main:284) | not needed: P1 replaces the uniform state by a constructed realization's prior `μ_H` | not needed by P1, which works on a constructed realization; as stated on `main` the setup uses a bijection of a finite product with its uniform state (EF-1 r6 §4.2: needs a bijection of a finite product with its uniform hidden state, for one step; a window-faithful closure, where one is chosen, supplies both on the window as a chosen model, for the populations only); §20, T11; Table 5 | FIRM, because P1 uses no uniform or invariant measure |
| AM-6.2 | a uniform product prior in the torus comparison (EF-1 r6 N3.5) | assumed there (D2) | through the §3.2 setup, a bijection of a finite product with its uniform state (EF-1 r6 §4.2: through the §3.2 setup, as that row); Table 5 | RX |
| AM-8 | the Koopman operator as a unitary permutation operator and the projection `P_Σ` (Main:744) | an invariant normalized reference state is a premise (Q6(c)). For a uniform product state its invariance is what (M-full) gives in the locality class (checked; not used for the class); that nature's reference state is that one stays a premise (D2) | the Koopman statements use a unitary permutation operator with modulus-one spectrum and exact recurrence (EF-1 r6 §4.2: the Koopman statements need the spectrum and recurrence of nature's own permutation); the compression needs a reference measure on the full system; Table 5 | NEW, by that premise; (M-full) does not change it |
| AM-12, AM-14 | "uniform hidden prior $\omega_H = \mathbb{1}/\lvert\mathcal{C}_H\rvert$" (Sub:253); a uniform hidden prior (GR:112); a normalized product prior (GR:132) | not used by the dependence statement | not used | RU; the comparison's product prior is its own hypothesis (D1) |
| AM-21.2 | "the reference prior defining $T$ — the uniform hidden prior of the model above", toward which the hidden conditional relaxes (Main:453) | a physically selected reference prior is a premise (Q6(c)) | no class in EF-1 r6; this audit [IR]: as stated, the theorems are for "the uniform-prior bijection marginal of §3.2's construction" (Main:453), a bijection of a finite product, P5b restates them for a reference prior taken as a premise; Table 5 | NEW, by that premise |
| AM-22, AM-36 (U1) | "uniform counting" on "a conserved energy shell" of "the finite total system" (GR:58); "time-reversal invariance gives a bijection between $i\to j$ and $j\to i$ trajectories, so $N_{ij}=N_{ji}$" (GR:70) | a shell measure on an infinite carrier is a premise; a shell prior is not a product prior, and (M-full) concerns the uniform product measure only | an invariant shell measure of a bijection of a finite carrier, with its trajectory pairing (EF-1 r6 §4.2: needs an invariant shell measure of nature's own bijection of a finite carrier (D8)); shells are not defined on the patch; Table 5 | NEW, by those premises |
| AM-30 | SM:641: "let the hidden prior be the counting measure"; SM:643: T-invariance, a fibre map with a mutual inverse giving sets of equal cardinality, then "Dividing by $\lvert\mathcal{C}_H\rvert$"; the kernel's count form with `Fintype.card H` (`Reciprocity.lean:129`) | `φ`-invariance of counting ⊗ `μ_H` is P6's premise. For a uniform product `μ_H` it is of the kind (M-full) gives (checked; not used for the class); bijectivity and T-invariance on the infinite carrier are premises as well (Q5) | no class in EF-1 r6; this audit [IR]: as stated on `main` the proof counts over a finite hidden space; P6 restates it on the full system; Table 5 | NEW, by those premises; (M-full) does not change it |
| AM-33.2 | exact time averages on the cycles of a finite `Σ_E` (GR:807) | holds on the finite isolated model | no class in EF-1 r6; this audit [IR]: the cycles of a bijection of a finite set; Table 5 | RM |
| §11 item 3 (not a candidate) | double stochasticity under an invariant uniform prior | EF-1 r6 N3.2, second-order form; (M-full) extends it to the locality class with finite alphabets; it can fail outside that class (B1) | record law only | no class; the item only says double stochasticity does not discriminate finite from infinite carriers |

Population of Table 3: 14 lines, 13 of them covering 16 rows (AM-1.1; AM-3.2; AM-4.1, AM-4.3; AM-4.2; AM-4.4; AM-5; AM-6.2; AM-8; AM-12, AM-14; AM-21.2; AM-22, AM-36; AM-30; AM-33.2) and §11 item 3, which is not a row.

**Table 4. Rows with settings, interventions or adaptive policies: which form of Lemma PM-I each needs.** The
all-branch form (under FS-all), the per-run form and Lemma K are defined in §0 and §14.2 (EF-1 r6 N1.5). A law
over outcomes, a finite description, or a comparison across settings needs one finite patch for every branch,
which is proved under FS-all, with a bound, or from finite reads on every run, under Lemma K's other
hypotheses, without one. No row's class rests on the per-run form or on Lemma K.

| Row / route | What is compared or asserted | Form needed | Established for the row? | Consequence |
|---|---|---|---|---|
| AM-7.1, intervention form | two runs that differ only in the intervention on `A` | neither a per-run nor an all-branch patch: the statement is pointwise and uses no finite patch. It needs the intervention's support, taken over every state, to lie in `A` ("reads and writes only region $A$", Main:362). EF-1 r6 §4.2 calls this the single-step all-branch form with a declared support (§20, T3) | yes, as the statement's own hypothesis | none for the class (CONTINGENT by L1) |
| AM-7.2, P4 (measurable `Ω`) | a law over outcomes for every setting pair | no finite patch is used. It needs one pre-setting variable that fixes the responses to every setting (Main:364–365), which holds for supports of any size because every `u^A_a` acts on `A` and every `u^B_b` on `B` (hypothesis (ii)). In EF-1 r6's terms this is the all-branch dependency statement, Lemma PM-I (a), which has no finiteness hypothesis | yes, as hypotheses of the theorem | the row is CONTINGENT on this route: P4 adds hypothesis (iii) read in the dependency sense and measurable response functions, neither on `main` as worded (F10; Q8). The review of r6 keeps FIRM (§14.1) |
| AM-7.2, `Ω_n` route | the same law, from one finite patch | **all-branch** (FS-all): one finite patch for all setting pairs and, where the settings are generated inside the substratum, for every branch of the generators. A per-run patch could differ between settings and between runs, and no single `p(Ω_n)` would be defined on it (EF-1 r6 N3.6) | only under the premise that `A`, `B`, `R_A`, `R_B` (and the generator regions) are finite, which is not separately stated on `main` | this route is **not FIRM** |
| AM-7.3 | as AM-7.2 | as AM-7.2 | as AM-7.2: the wing regions of Main:414 are not said to be finite | CONTINGENT through P4 and the kernel cone (§14.1); its `Ω_n` route adds finite wing regions and is not FIRM either |
| AM-23.2 (P16) | one finite description of the output for an input rule | **all-branch** (FS-all), if the sentence is to hold for adaptive inputs: a rule that reads two sites in every run can still depend on unboundedly distant sites across runs (EF-1 r6, example E2). The per-run form gives each run with finite reads a patch of its own, which is not one description of the output. Lemma K gives one patch from finite reads on every run, under the lemma's other hypotheses (a finite alphabet at every site; finitely many values of the policy information) | no: FS-all, or Lemma K's hypotheses in its place, would be carried as named hypotheses of the restated sentence [IR] | the row is not FIRM (it is CONTINGENT, and NEW if the owner counts FS-all as an assumption about nature) |
| AM-9 remark; §11 item 1 | a behaviour matrix over all preparations and measurements | **all-branch** (FS-all) | no; a hypothesis of the remark (EF-1 r6 N3.11 counts on the autonomous patch; §20, T19) | none: a remark only |

Population of Table 4: 6 lines covering 4 rows (AM-7.1; AM-7.2, by two routes; AM-7.3; AM-23.2) and the remark under AM-9 with §11 item 1.

No row is served by the per-run form alone; EF-1 r6 §4.2 says the same of its own classes.

**Rows the fixed-horizon lemma does not carry** (each traced at the lines given).

| Row | What the proof uses that the description does not have | Form it would need | Disposition |
|---|---|---|---|
| AM-1.1, AM-1.3b, AM-2.2 | Main:121: "$\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$. Thus $T^{(N)} = I$"; Main:137: finite order `L`, `Γ_L = I`, `Γ_{t+L} = Γ_t`. (Main:123–127's strict contraction at one step is a property of the law on `[0, 1]` and is carried) | the counting form (Main:113–129): a finite carrier with its counting prior; F-one does not supply the prior. The rooted form (Main:135–137): F-one with an exact return | RM / RX unchanged; a finite description for a chosen horizon supplies no recurrence guarantee within that horizon (§20, T8, T9) |
| AM-9.1, AM-9.2 | Main:638: "a bijection on a finite set has finite order $L$"; Main:558: one fixed `N` | F-one | RM / RX unchanged |
| AM-3.2 | Main:60: "a map $f$ on a finite set $X$", its eventual image, `f^L = id` on it | a finite carrier; the patch has no self-map | RX (§20, T7) |
| AM-4.1, AM-4.3 | Main:54: finite cycles; the maximal-entropy selection among invariant measures | a finite carrier | RM / RX (§20, T6) |
| AM-22 (P7) | GR:58: "Restrict the finite total system to a conserved energy shell", "If the boundary interaction is negligible at the shell scale"; GR:68: the symmetric relation holds "only when the coarse states are time-reversal even"; GR:70: a trajectory bijection on the shell | a finite carrier, or a Gibbs-type restatement with a shell measure | NEW; waits on its premises (§20, T16) |
| N-1; N-2's total form | global recurrence; total information content | a finite carrier | RX |

Population of this table: 6 lines covering 11 rows (AM-1.1, AM-1.3b, AM-2.2; AM-9.1, AM-9.2; AM-3.2; AM-4.1, AM-4.3; AM-22; N-1; N-2 in its total form).

Each row of this table needs something that lies outside the observation window and is nature's own (an
order, a return, an eventual image, a conserved shell, the total carrier). The description does not inherit
it, and a window-valid closure cannot supply it; Table 5 names the requirement row by row.

**Table 5. Rows that need an invariant or uniform measure, or bijectivity: are the proof's requirements
confined to the observation window?** (adopted direction, c.6897859755). The window is `[0, n]`, the horizon of the
fixed-horizon description. A *window-valid closure* is a finite bijective, measure-preserving model on the
patch data, chosen so that it reproduces the record on the window. When one exists is Lemma C, Corollary C1
and Lemma C′ of EF-1 r6, each **checked once**, under its stated hypotheses, by the recheck of EF-1 r5 (the tiers of adopted direction c.6897859755 predate that check); whether one preserves what a given result needs is **unproved**. Each entry is
read from this audit's trace of the proof on `main` (the lines are in the row's own section and in Tables
1–3). **Yes** means that every requirement traced is a statement about the window; the consequence is then
"closure could suffice; to be determined; no recovery credit yet". **No** names the requirement that lies
outside the window; the consequence is then "closure cannot supply it". **Undetermined** means that the trace
does not settle it. **No row's recovery class changes on the closure result.** A "yes" is not a recovery: a
recovery candidate is not a recovered result. The entries are this audit's reading [IR] and are unreviewed. The last column gives the window entry of EF-1 r6
§4.2 (its second table) for the class that covers the line, or says that EF-1 has no class for it; where the two
differ the trace entry of §20 is named, and neither side is adopted.

| Row | Requirement of a measure or of bijectivity (from the trace) | Requirements confined to the observation window? | Consequence | Class | EF-1 r6 §4.2, window entry |
|---|---|---|---|---|---|
| AM-1.1; AM-1.3b; AM-2.2 | the return at the order of the bijection: `T^{(N)} = I` (Main:121); `Γ_L = I` and `Γ_{t+L} = Γ_t` (Main:137) | **no**: the order and the return of the bijection, which lie beyond any window shorter than the order | closure cannot supply it: a closure's order is its own. (The one-step strict contraction, Main:123–127, is inside the window) | RM; RX; RX | **no** (the return `T^{(N)} = I` at the order of the bijection; the one-step contraction, Main:123–125, is a window statement). Agrees |
| AM-2.1 (P1) | a permutation unitary of a finite realization with a root-independent prior, for an implication between two properties on one window (Main:326–332) | **yes** [IR] | closure could suffice; to be determined; no recovery credit yet. P1 does not need one: it works on a constructed realization. The action off the diagonal belongs to the chosen model | FIRM (by P1) | **mixed**: the reduction for diagonal-preserving channels (Main:332), yes; its input, P-indivisibility at the recurrence scale (Main:330), no. Differs in labelling (§20, T25) |
| AM-3.2 | injectivity and surjectivity of nature's own map on its whole carrier; the eventual image of a map on a finite set (Main:60) | **no**: bijectivity of nature's dynamics on the total carrier | closure cannot supply it: a closure's bijectivity is its own | RX | **no**; the statistical prong alone, double stochasticity at each step order, is a window statement about the record law (§20, T24) |
| AM-4.1; AM-4.3 | the invariant measures of the bijection on its cycles, and the maximal-entropy selection among them (Main:54, :60) | **no**: the cycles and invariant measures of nature's own map | closure cannot supply it | RM; RX | **no** (cycles, the orbit of the actual microstate, the set of invariant measures). Agrees |
| AM-4.2 | the uniform hidden prior that defines `T`; the `k`-step matrices; their double stochasticity (Main:115–117, :129) | **yes**, for the matrices up to the horizon and their double stochasticity; **no** for the hidden cardinality as an absolute number | closure could suffice; to be determined; no recovery credit yet | RM (no class) | **yes** for `T^{(k)}`, `k ≤ n`; the absolute size of the hidden space is not a window quantity. Agrees |
| AM-4.4 (P13) | a measure equivariant under signed permutations; a memory-resummed response (SM:334–336) | **undetermined**: the definition of the response was not traced, and a sum over every memory order would not be confined to a window | to be settled by P13's check | NEW | no class in EF-1 r6 |
| AM-5 (P1) | a bijection of a finite product and a hidden state, for the one-step channel and the Born form (Main:266–288) | **yes** [IR]: one step | closure could suffice; to be determined; no recovery credit yet. P1 does not need one. On the reading of the review of EF-1 r4 a closure gives the populations only; the channel off the diagonal depends on the closure | FIRM (by P1) | **yes**: each statement concerns one step. Agrees on the window entry (§20, T26, for the direct-proof column) |
| AM-6.2 | the §3.2 setup with `ρ_H = I_m/m`, for the estimate of Main:340; the cardinality of nature's hidden environment, for the prediction (Main:216) | the estimate: **undetermined**; the cardinality clause: **no** | for the clause, closure cannot supply it: it concerns the total hidden sector | RX | **mixed**: the estimate of Main:340, yes as far as traced; the cardinality clause, no (§20, T27) |
| AM-8 (P8-M) | a normalized invariant reference state that defines `P_Σ`; the Koopman operator; canonical typicality of the total system's equilibrium macrostate (Main:744, :752, :756, :758) | the theorem's inequality: **undetermined** [IR] (the round trip and the compression are taken over `t ≤ τ_S`, but the reference state is one of the total carrier); the observer-selection rule: **no**, typicality of the total system (Main:756); the Koopman spectrum and exact recurrence: **no** | for the rule and the spectral statements, closure cannot supply it | NEW | **mixed**: the cone step for `t ≤ τ_S` (Main:752), yes; the Koopman spectrum, exact recurrence, finiteness of `S` and canonical typicality, no (§20, T31) |
| AM-9.1; AM-9.2 | a bijection of finite order `L`, and one fixed carrier of `N` states for every experiment (Main:638, :558) | **no**: the order, and one model for every horizon (F-one) | closure cannot supply it: a closure is chosen for one window | RM; RX | **no** (all-time by its statement; one fixed finite realization for every experiment). Agrees |
| AM-11; AM-24 (P12) | Stage 1's bijection on a finite `S` and its recurrence-cycle sentence (Sub:125, :137); Stages 2–3 not traced here | the constructed realization: **yes**; the recurrence-cycle sentence: **no** (§20, T17); Stages 2–3: **undetermined** | mixed; nothing to credit | NEW | **mixed**: Stage 1's constructed realization, yes; the recurrence-cycle clause (Sub:137), no; the periodic lattice, transition counts and shell counting (Sub:157, :167, :181), no; Stage 2 (b)–(e), undetermined (§20, T30) |
| AM-12 (i); AM-14 | a uniform hidden prior for the comparison (Sub:253; GR:112, :124); injectivity for the H-BD bound (GR:126) | GR:112 (a) and the relabelling: **yes** (statements about the transition data on `[0, nΔt]`); GR:112 (b): **no** (injectivity of the whole map and a bound over the whole deep sector, GR:126) | closure could suffice for (a); to be determined; no recovery credit yet. The rows are RU and need no recovery | RU (no class) | **mixed**: GR:112 (a) and the first statement of GR:132, yes; GR:112 (b), no (GR:126). Agrees (§20, T28) |
| AM-21.2 (P5b) | a reference prior toward which the hidden conditional relaxes; the uniform-prior bijection marginal (Main:453) | **undetermined** [IR]: the bounds are for finite `k`, but `ε` is defined through hidden conditionals, which belong to whichever model carries them | to be settled when P5b is written | NEW | no class in EF-1 r6 |
| AM-22; AM-36 (U1) (P7) | a conserved energy shell of the finite total system with uniform counting; the hidden sector's energy-dependent multiplicity; a time-reversal pairing of shell trajectories (GR:58, :70) | **no**: a conserved shell of the whole carrier, and the hidden multiplicity | closure cannot supply it | NEW | **no** (a conserved shell of the finite total system and a pairing of shell trajectories). Agrees (§20, T29, for the direct-proof column) |
| AM-30 (P6) | bijectivity and T-invariance of the dynamics; a counting hidden prior; a count over a finite hidden space (SM:641–643) | **yes**, for the `n`-step matrices up to the horizon [IR] | closure could suffice; to be determined; no recovery credit yet. The closure would also have to be T-invariant, which is part of what is to be determined | NEW | no class of its own; under Theorem 23, reciprocal transition counts (Sub:167): no, properties of the whole carrier (§20, T30: a different statement from the `n`-step matrices) |
| AM-33.1 (P10) | injectivity of the dynamics on the whole carrier, hidden sector included (GR:791) | **no**: a property of the joint state with the hidden sector, not of the observation record | closure cannot supply it | CONTINGENT (else NEW) | no class in EF-1 r6 |
| AM-33.2 | the cycles of a bijection of a finite `Σ_E`, and full-cycle averages (GR:807, :839) | **no**: full cycles | closure cannot supply it | RM | no class in EF-1 r6 |
| AM-28; N-5; AM-37; N-1; N-3 | the period of a finite bijection; an asymptotic rate; global recurrence | **no**: periods, asymptotic rates and global returns | closure cannot supply it | RM; RM; RM; RX; replacement candidate | no class in EF-1 r6 |
| §11 item 3 | double stochasticity of the one-step matrix under an invariant uniform prior | **yes** | not a candidate; nothing to recover | none | **yes** (A1-test candidate 3: a one-step matrix, a property of the record law). Agrees |
| AM-16; AM-25; AM-27; AM-29; AM-32; AM-34; AM-38 | bijective dynamics of a finite model (finite tori; the monomial class; a permutation of a finite set) | **undetermined**: not traced for this question (AM-16's cycle structure is not confined to a window) | these rows are statements about finite models and are kept as such | RM | no class in EF-1 r6 |
| AM-5b | the §3.2 channel with a finite `C_H` and `ρ_H = I_m/m` (Main:280–282); one step; only the hidden boundary sites enter, "the criterion carries no dependence on $\lvert H\rvert$" (Main:322) | **yes**, for one step [IR; unreviewed] | closure could suffice; to be determined; no recovery credit yet. The result concerns the action on off-diagonal inputs, which depends on the closure chosen | RM (no class) | **yes**: one step; open within that, the dependence on the closure (§P.4). Agrees |

Counts of Table 5, by line (21 lines): yes 6 (AM-2.1, AM-4.2, AM-5, AM-30, AM-5b, §11 item 3); no 8, covering 17 rows
(AM-1.1, AM-1.3b, AM-2.2; AM-3.2; AM-4.1, AM-4.3; AM-9.1, AM-9.2; AM-22, AM-36; AM-33.1; AM-33.2; AM-28, N-5,
AM-37, N-1, N-3); undetermined 3, covering 10 rows (AM-4.4; AM-21.2; the eight finite-model rows AM-16, AM-25,
AM-27.1, AM-27.2, AM-29, AM-32, AM-34, AM-38); mixed 4, covering 6 rows (AM-6.2; AM-8; AM-11 with AM-24; AM-12
with AM-14). 6 + 8 + 3 + 4 = 21 lines. **Population: 38 rows** (17 under "no", 5 under "yes", 10 under
"undetermined", 6 under "mixed"; 17 + 5 + 10 + 6 = 38) and §11 item 3, which is in the table and is not a row. The
other 19 of the 57 rows use no measure and no bijectivity; 38 + 19 = 57. Each line was recounted for r8 against
the row list of §12.1. None of these is a recovery class, and the counts of §14.1 do not depend on this table.
EF-1 r6's second §4.2 table differs from this table, or from §12.3, in eleven entries, listed in §20 (T22–T32).

**Gate tally.** Seven proofs cannot be asserted of nature before Q6(c): P5b, P6, P7, P8-M, P8-S, P12, P13. As conditional theorems, with the measure as a named hypothesis, P5b, P6 and P13 wait on no owner question beyond Q11 and Q12; part (3) of P9 cannot be asserted of nature before Q6(d), and as a conditional theorem with a starting law as a named hypothesis it waits on Q11 and Q1(b-loc) only, and its parts (1) and (2) wait on no owner question. Four cannot be asserted of nature before Q5 (P6, P7, P10, P12); as conditional theorems with bijectivity or injectivity as a named hypothesis P6 and P10 wait on Q11 and Q12 only; and P8-M also waits on Q5 if its invertibility check
fails. Three wait on Q8 (P3, P8-M, P16), and P4's `Ω_n` route also does. Q1(b-mode) gates P7 directly and
P12 through P7; Q1(b-loc) gates part (3) of P9. P12 also waits on Q3. P8-M and P8-S wait on the (LE) choice of Q7. Q11 is
presupposed by every forward-direction route (P3, P4's `Ω_n` route, P6–P10, P13, P16). P1, P4 (measurable
`Ω`), P5a, P11 (as a conditional theorem), P14 and P15 wait on no owner question beyond authorization (Q12). P4 and P5a do so as conditional theorems whose statements carry hypotheses that are not all worded on `main` (Q12).

**Order by impact.** P7 (GR calibration); P12 with P1, P5a/P5b and P6 (Theorem 23); P3 and P4 (Bell layer and
abstract); P8 (Q7); P9; P10, P13, P16; P11, P14, P15.

### 14.4 The two barred shortcuts, checked

Adopted direction (c.6897946443): "But two shortcuts would be unjustified:" "Adopting a new assumption solely because it
rescues a desired result." and "Calling a conditional recovery an unconditional consequence of OI."

**First shortcut, against every NEW row and against AM-31's replacement part.** "Support beyond the rescue" means support found on `main`, or in a
checked lemma, for the hypothesis itself and not for the result it would recover. Where none was found, the
hypothesis is not recommended for adoption and the row is conceded as conditional or as finite-model
mathematics (§12.4).

| Row | Hypothesis the route needs | Support beyond rescuing the row | Recommendation |
|---|---|---|---|
| AM-4.4 (P13) | a normalized measure equivariant under signed permutations, on the infinite lattice | The uniform product family exists and is consistent on any site type (kernel, `uniform_family_consistent`), and the extension clause already names equivariance as its own hypothesis (SM:334). That nature's measure is such a one: none found | Do not adopt. Concede: the clause stays conditional on its stated hypothesis |
| AM-8 (P8-M, P8-S) | a normalized invariant reference state; (LE) or a typicality statement for an infinite carrier | Invariance of a uniform product state is derived ((M-full), checked; N3.2). That nature's reference state is that one: none found. (LE) was introduced by this audit only to replace canonical typicality in the corollary; it has no other support | Do not adopt (LE) or a reference state for this purpose. Concede: finite-model mathematics (Q7(d)) |
| AM-11, AM-24 (P12) | those of P5b, P6 and P7; the class definition | as the three rows below | Concede: conditional on those hypotheses; the theorem is not stated as unconditional |
| AM-21.1 (P5a) | that nature's joint process of record and hidden state has a law (L9) | It is the adopted table's condition for any probability statement (K2, "A suitable starting probability law") and is used by every forward-direction law statement, so it is not specific to this row. On `main` it is a hypothesis only (GR:132; Sub:262) | Carry it as a named hypothesis of the theorem (Q6(e)), not as a posit (Q6(d)). Concede: the theorem is conditional on a joint law (§12.3, CD) |
| AM-21.2 (P5b) | a physically selected reference prior toward which the hidden sector relaxes | Main:453 has "the reference prior defining $T$" as a datum of the model. A selection for nature's hidden sector: none found | Do not adopt. Concede: the bound stays a theorem about coupling-step models with a stated reference prior, or conditional on that prior as a named hypothesis |
| AM-22 (P7); AM-36 (U1) | uniform counting on a boundary shell, or a stationary time-reversal-invariant law; a time-reversal pairing; the boundary mode count | H-count (GR:58) and the mode count (GR:90) are existing named GR hypotheses, with their own open justification. A shell or stationary measure on a carrier of undetermined cardinality: none found | Do not adopt a shell measure for this purpose. Concede: conditional on H-count and on a named stationary law, with the direct target of §12.3 as the thing to prove |
| AM-30 (P6) | bijectivity and T-invariance on the infinite carrier; an invariant, time-reversal-symmetric prior | Bijectivity and T-invariance hold by the form of item (xiii)'s rule on the selected model (kernel `a2_every_substratum`; SM Theorem 17), which is support of their own, at the cost of widening (xiii)'s listed role. Invariance of the uniform product prior is derived (N3.2). That nature's prior is that one: none found | Adopt nothing. Concede: conditional on the prior as a named hypothesis; the selected-model facts may be cited as what they are |
| AM-31, part (3) (P9); a replacement part, in no class | a normalized starting law on nature's carrier | It is the adopted table's condition for any probability statement (K2, "A suitable starting probability law") and is used by every forward-direction law statement, so it is not specific to this row. It is not on `main` for a carrier of undetermined cardinality | Carry it as a named hypothesis (Q6(e)), not as a posit (Q6(d)). Concede: part (3) is conditional |

Population of this table: 8 lines: the 9 NEW rows in 7 lines (AM-11 with AM-24; AM-22 with AM-36) and AM-31's replacement part.

Result: of the nine NEW rows (AM-4.4, AM-8, AM-11, AM-21.1, AM-21.2, AM-22, AM-24, AM-30, AM-36) and AM-31's replacement part, none has a hypothesis that this audit recommends adopting. Two hypotheses have
no support at all beyond the rescue ((LE); a selected reference prior for AM-21.2), and for four more the
missing part is the same one, that a particular normalized law is nature's (AM-4.4, AM-8, AM-22 with AM-36,
AM-30).

**First shortcut, against the recommendations of §19.** Q11(a), Q1, Q8(c), Q6(a) with (e), Q5(a), Q9(c),
Q10(c), Q4(a), Q3(a) with (n1), Q15(b), Q13(a), Q14(c) and Q12(b) adopt no assumption: each either removes a
claim, keeps finite-model mathematics, or carries a condition as a named hypothesis of the statement that
uses it. Three options would adopt one, and none of them is recommended: Q6(c) and Q6(d) (a reference state,
or normalization, posited of nature), Q5(b) (reversibility as a postulate, whose only uses found are P6, P10
and the headline clause H3), and Q7(a) with (LE). r5's rider on Q7, "unless Q6(c) is adopted, in which case
(a)", is withdrawn in §19 for this reason.

**Second shortcut, against every FIRM and CONTINGENT statement and the two conditional theorems.** FIRM is defined once, in §0, by the adopted rule (c.6898395533). It does not mean unconditional. Population: the 4 FIRM rows, the 5
CONTINGENT rows, and the two NEW rows marked "conditional theorem available" (AM-21.1, AM-4.4); 11 rows. The
condition each such statement carries:

| Row | Class | What it would establish, if proved | Conditional on | May it be called an unconditional consequence of OI? |
|---|---|---|---|---|
| AM-2.1 | FIRM | CP-indivisibility of a chosen realization's channel family on a window | a constructed realization; P-indivisibility on that window as its premise | No: a statement about a chosen finite model (FM) |
| AM-5 | FIRM | a Born-form representation of every one-step visible law | Lemma 1 and `main`'s finite-horizon equivalence | It holds for every law and excludes none; it must be worded as a representation, not as a constraint |
| AM-31 | FIRM (the theorem as stated) | C1 for every proper connected subgraph of a connected bounded-degree coupling graph (part (1)); the C3 capacity clause as stated (part (2)), which says nothing when the hidden sector is infinite | Theorem 22's graph hypothesis (SM:1376); part (3), if stated, on a starting probability law (K2) | No: a theorem under its graph hypothesis |
| AM-7.2 | CONTINGENT | a ceiling on correlations for one class of completions | determinism, the locality hypotheses and measurement independence (item (xiv), a posit); P4's two added hypotheses (F10) | No: a conditional no-go about completions |
| AM-7.3 | CONTINGENT | the same for the reference graph | measurement independence and response completeness, hypotheses of the statement; P4's measurable-response hypothesis | No |
| AM-21.1 | NEW; conditional theorem available | a bound on hidden conditional laws from observed memory | a joint law of record and hidden state (K2); the reading for nature also Q11 | No: a conditional theorem |
| N-6 | FIRM | nothing: a ledger disposition | — | Not applicable |
| AM-7.1 | CONTINGENT | the cone on a carrier of any cardinality | finite reading sets, by an undecided reading or as a named hypothesis; L10 for any observable form | No |
| AM-23.2 | CONTINGENT | a restricted statement about finite-step outputs | K1's hypotheses, with finite supports over every branch or Lemma K's hypotheses, as named hypotheses | No |
| AM-33.1 | CONTINGENT | purity of a joint state | injectivity of the dynamics on the whole carrier | No |
| AM-4.4 | NEW; conditional theorem available | custodial scalarity of the observer's quadratic response, in the extension clause of SM Proposition 4b (SM:334–336) | the clause's own hypothesis (SM:334): dynamics, measure and observer σ-algebra equivariant; that the response is defined for that measure is not on `main` | No: a conditional theorem |

Result: every FIRM and CONTINGENT statement, and each of the two conditional theorems, is conditional or is a
representation statement, and each is labelled so here and in §12.3. Headline sites that would cite them (Main:20, for AM-7.1 and AM-7.2) keep
their hypotheses in the sentence (§8).

## 15. Effects on Substratum Theorem 23 and on GR

- **Theorem 23 and Lemma 23.0 (Sub:189, :193; class A1–A6).** A1 is a stated hypothesis. Its traced uses are
  Stage 1's output (Sub:125; replaced by Main §3.4's per-horizon realization: F-each for Stage 1's constructed
  realization; its recurrence-cycle sentence, Sub:137, is not carried and is restated or dropped as AM-1.3b), the §3.2
  dilation (P1), C2's slow-bath form (P5b, gated on Q6(c)), reciprocity (P6, gated on Q5 and Q6(c)), A2's
  justification (Q5), and, through `ħ`, P7 (gated on Q1(b-mode), Q5, Q6(c)). The gauge-sector Stages 2–3 are
  untraced (P12); if any uses a property uniform in the horizon, EF-1 does not supply it. The class "A1–A6"
  (Sub:92–104, :205–223; Struct:47, :646; GR:342, :669; Meth:367; `ch09-universality.md:104`) changes definition,
  and its range is rewritten at 65 lines (a count by the pattern of §9 item 3; not claimed complete, §21), under Q3; A4's own wording at Sub:98 ("a finite periodic lattice")
  also carries finiteness (validity review G3, [IR]), so restating A1 requires restating A4's parenthesis. If
  P12 is not completed, the theorem cannot be stated under the owner's condition except on finite models, which
  changes the synthesis claim's subject. Constructive structural realism (AM-24) follows the same path.
- **GR.** The deep-sector corollary's first statement is already stated for an infinite deep sector, given a
  normalized product prior and a locally finite coupling graph (GR:132; AM-14, RU); after EF-G1 the product
  prior is a condition of its comparison only. The horizon calibration's counting link (AM-22, P7) is the one
  substantive GR proof needed, and it waits on Q1(b-mode), Q5 and Q6(c); the fixed-horizon lemma does not carry it.
  The universality claim (AM-36) has a candidate route through P1 and P7; its S2 needs no finiteness form. The Page-curve appendix needs P10 for A.7
  (waiting on Q5); A.8–A.9 are theorems about the finite isolated `B ∪ R` model under H-decouple (AM-33.2, RM),
  kept in GR's appendix under either answer to Q2; their physical reading needs Q1(c) and H-decouple; G11
  stays Open. The substratum-source paragraphs (GR:224, :256–274; AM-27) are re-scoped to the monomial class on
  finite carriers and to finite tori; their theory-general content (AM-27 (β)) stays under either answer; their
  census consequences are in §10. GR:90, :138, :585, :587 follow AM-1.
- **What GR and Theorem 23 do not lose.** No GR or SM census anchor disappears under Q2(a); SM:643's `theorem_19`
  stays cited for the counting-prior statement it proves. Under Q2(b), GR loses the anchors of families 6, 19, 21,
  22 and keeps those of 5, 7, 8, 10, 11, 14 (in part) and 20.

## 16. Off-`main` references (§A.42 item 8)

Each reference is classified against the claim it is attached to.
- **PR #1303**, branch `research/ro3-carrier-inventory-1055-20261114` at `59514344` (RO-3 inventory r9 and its
  reviews): the row list this audit takes as input (owner accepted at its reviewed scope, #1169 comment
  6894553525). Support off `main` for the row list's completeness; no row's treatment rests on it beyond its
  inclusion, and every row was re-read at `bf89ba13`.
- **`OBL-RO3-2-r2.md`** (PR #1303): cited only as r9 cites it, for the OBL-class countercontrols in AM-1.3b, AM-4.3,
  AM-8 and AM-37. Provenance; no treatment rests on it.
- **The AM-3 preregistration r2 and its two reviews; the held change map `CHANGEMAP-A1W-r2.md`, branch
  `paper/a1-wording-20261115`, commit `cbb0a8f0`**: unpushed drafts. The AM-3 findings in AM-3.2 and the W3 reading
  in AM-30 are [IR]; the 137-site count is context. Provenance.
- **r1 to r5 of this audit and the reviews of r1 to r4** (unpushed drafts; r5 has no review): the inputs of this revision. Provenance; every
  finding was re-checked at `bf89ba13` (§1).
- **EF-1 r6** (unpushed draft, sibling directory, sha256 `b429d3af…537d1b1`), **the review of EF-1 r4**
  (unpushed draft, sha256 `64ec14f4…e85e2d81`, ACCEPT WITH CHANGES), and behind them **EF-1 r3 and the review
  of EF-1 r3** (unpushed drafts, sha256 `bba62a14…c208c224` and `57391991…b8574926`), to which r5 was pinned.
  EF-1 r6 is cited for Lemma PM, Lemma PM-I (the all-branch form, the per-run form, Lemma K), §P (objects
  (α)–(δ), (M-full), (M-desc), B1), §4.0 (F1–F7, P1–P2, D1–D8), §4.2, EF-G1, EF-G5, N1.1, N1.2, N1.4, N1.5,
  N1.6, N1.8, N2.1, N2.5, N2.9 and N3.1–N3.11; its review for the proof status of those statements, for its
  findings 1 to 8 and 11, for Lemmas C and C′ (its own, unchecked) and for its retrace of §4.2. Support off
  `main` for the candidate routes only: each cited statement is marked [IR] or provisional, changes recovery
  classes and routes and never a row's status, and gives no row recovery credit. **No class rests on (M-full),
  on N3.2, on the per-run form, on Lemma K, on the memory clause, on the necessity statement or on the
  closure result.** The Lean statements they rely on were re-read at `main` (`RegionTower.lean:246–307`,
  :408, :447; `SecondOrderDrive.lean:306`; `SecondOrderLayer.lean:208–210`). EF-1 r6 cites this audit at its
  r2 for labels, so its Q-, P- and candidate numbers can lag this revision's (§20, D20). 

- **The A1-validity gem review r3** (unpushed draft, sibling directory): cited for consistency notes (AM-3.2's
  (xiii) route, AM-4.3, AM-6, AM-12, AM-14, AM-21, AM-22, AM-33.2, §11 candidate 2, §15's A4 note). Provenance; each
  cited point was re-read at its `main` source where one is named (`SubstratumInterfaceAudit.lean:81`, `:106`;
  Sub:98; GR:128, :132), and no treatment rests on that review alone.
- **#1169 comments 6894553525, 6894697123, 6894872312, 6895032895, 6896070253, 6896252651, 6896496410,
  6896771264, 6896890693, 6896940222, 6897254631, 6897455387, 6897859755, 6897946443**: authority and scope, not
  evidence.
  The sentence used as a rule is recorded in 6897859755. **#1309**: cited in AM-22's goal link as the
  planning row; provenance.
- **DEPENDENCY-AUDIT.md** (`verification/audits/manuscript/observer-relative-finiteness-20261030/`, on `main`;
  audit record, review independence not established): context for AM-1.3b, AM-4.3, AM-11, AM-22.

## 17. r6 changes (r6's record; attributions corrected in r8)

What changed from r5, and why. r6 was written in three passes: the re-pin to EF-1 r4 and the consistency pass
that this round was opened for; a second pass after EF-1 r4 was reviewed and the adopted directions of #1169 comment 6897859755 were given; and a third pass for the adopted direction of comment 6897946443, which goes
beyond a re-pin. Everything not listed is carried from r5 unchanged: the 56 rows and their categories, the
reasons (47, 6, 3), every recovery class and count, the landings, §8, §9, §12.1, §12.2, §13, §15, the order of
the 15 questions, and every recommendation except Q7's rider.

**Pass 1: the re-pin to EF-1 r4 and the consistency pass.**

| Where | What changed from r5 | Why |
|---|---|---|
| Title and header | "r5" becomes "r6"; the revision is described as a re-pin and consistency pass | The task of this round |
| Standing, inputs and wording | r5 is named as the starting text, with its sha256; a rule for reading "r5", "r6" and "this audit" | r6 starts from r5, which has no review |
| Standing, EF-1 | The pin moves from EF-1 r3 to EF-1 r4 (sha256 `b429d3af…537d1b1`) | EF-1 r4 is the text the record names for the re-pin |
| Standing, traces | States that §14.3's traces are r5's and are compared with EF-1 r4's retraced §4.2 in §20 | Task item 2 |
| Standing, owner records | The directions r5 marked as relayed and not recorded are quoted from #1169 comment 6897455387; the entry for 6897254631 gains the record's next-step sentence | The relay is now recorded |
| §0, F-each | The three ingredients are restated as EF-1 r4's three premise groups (finiteness premises F1–F7; probability premise P1, P2; further distributional properties D1–D8), each needing its own justification, with each premise's standing on `main` from EF-1 r4 §4.0. The all-branch form is named FS-all; the per-run form and Lemma K are stated with what each gives. The four finite objects (α)–(δ) are named | EF-1 r4's statements; adopted direction, c.6897254631 and c.6897455387 |
| §0, measures | Full-system measure preservation is named (M-full) and kept apart from a measure on the description | Adopted direction, c.6897455387; EF-1 r4 §P.3 and §P.4 |
| §0, the rest | The settings condition cites the shared protocol, the memory clause and Lemma PM-I (d); F-one notes the necessity statement as unused; the class definitions gain one bullet and "unchanged by the re-pin"; the Main-independence note is re-pinned and names FS-all | Re-pin |
| §1 | Rows C2, C6, C8, C9, C10, C13.7 and "Section C" are re-pinned; the owner-directions table cites the recorded comments and gains rows | Re-pin; the recorded comments |
| §2 to §7 | Every EF-1 citation moves to r4, in AM-1, AM-4, AM-6, AM-7, AM-8, AM-9, AM-12, AM-14, AM-22, AM-23.2, AM-31, §6 and N-3. Added: AM-1, EF-1 r4's split of the recurrence class; AM-4, the standing of N3.2 and (M-full); AM-6, that EF-1 r4 traces the first-order clause to Main:340 and finds its form undetermined; AM-7.1, the intervention clause in EF-1 r4's terms; AM-7.2, that the `Ω_n` route needs the all-branch form, and why; AM-8 and AM-22, what the proof needs of a finite model; AM-9, FS-all; AM-23.2, which form of Lemma PM-I the sentence needs | Task item 1 |
| §10, §11, §12 | EF-1 citations move to r4. §11 item 1 names FS-all; item 2 notes the undetermined first-order clause; item 3 notes N3.2 and (M-full). The row counts are marked "unchanged from r4 and from r5" | Re-pin |
| §14, proof table | P3, P4, P7, P9, P11, P16: EF-1 citations and group names; P4 and P16 name the all-branch form and FS-all; P12 points to T17 | Re-pin |
| §14.1 | Column head "Uses EF-1 r4?"; cells for AM-7.2, AM-22 and AM-23.2 re-pinned; a recheck paragraph for the three counts; cross-tabulation headers in EF-1 r4's group names; a recheck paragraph for the cross-tabulation | Task item 4 |
| §14.2 | L1, L2, L4, L8, L9 and MI are cross-labelled with F3, F5, D1, F4, P1 and P2, D6; the FS row is restated; the paragraph on the three ingredients becomes one on the three groups | Task item 1 |
| §14.3 | Lead paragraphs re-pinned. Tables 1 and 2: group names, EF-1 citations, pointers to §20's T entries. Table 3: recast with (M-full) and what each proof needs of a finite model. Table 4: recast with the all-branch form, the per-run form and Lemma K | Task items 1 and 2 |
| §16 | The EF-1 entry is re-pinned; the recorded comments are added; r5 is named among the inputs | Re-pin |
| §20 | New lead paragraph. D3 gains EF-1 r4's position; D6, D8 to D15 and D20 are restated against EF-1 r4; D21 to D25 are added; the trace comparison T1 to T21 is added, with the rows that have no EF-1 r4 class and a summary | Task items 2 and 5 |
| §19 | "all fifteen questions are open"; the concordance is with EF-1 r4's eleven questions; Q8, Q12 and Q15 are re-pinned | Task item 6 |

**Pass 2: after the review of EF-1 r4** (adopted direction, c.6897859755; `REVIEW-EF-1-r4.md`, ACCEPT WITH CHANGES). r6
stays pinned to EF-1 r4.

| Where | What changed | Why |
|---|---|---|
| Standing | The review of EF-1 r4 is named with its sha256; proof status is given in the three tiers of adopted direction c.6897859755 (checked; still unchecked; still unproved); comment 6897859755 is quoted; the rule "a recovery candidate is not a recovered result" is cited to that record, where it is now recorded | Adopted items (1) and (5); the record |
| §0; §14.2; §14.3; rows AM-1, AM-4, AM-8, AM-23.2; §11; §14.1 | (M-full), the per-run form, the memory clause, Lemma K and the necessity statement are marked as checked by the review of EF-1 r4, under their stated hypotheses, where the first pass had "unreviewed" | Adopted item (1) |
| §0, "What the description inherits" and "A measure on the description"; §14.3, its lead, Table 3 and the sentence under the last table; rows AM-1, AM-4, AM-8; §20, D22 | Wording that said, or suggested, that the measure property fails for the description or cannot be had is withdrawn. The text now says that the property is not inherited automatically, and that whether a suitable finite closed model exists is a separate question, which the reviewer's Lemmas C and C′ address and which is unchecked | Adopted item (2): "Failure of automatic inheritance does not imply that no suitable finite closed model exists." |
| §14.3, Table 5 (new) | For each row that needs an invariant or uniform measure, or bijectivity: whether the proof's requirements are confined to the observation window (yes, no with the requirement named, or undetermined), and the consequence for a window-valid closure. 20 lines: yes 5, no 8, undetermined 3, mixed 4 | Adopted item (3) |
| §0; §14.2 (FS); §14.3 (Table 4); AM-23.2; §14.1; §18 | Lemma K is summarized as finite reads on every run, under the lemma's other hypotheses; "fails if" becomes "can fail if" | Adopted item (4); review of EF-1 r4, finding 2 |
| §14.1 | The recheck paragraph is rewritten: no class rests on the checked statements, and none would change if they were used; no class changes on the closure result | Adopted item (3) |
| §16; §20 | The review of EF-1 r4 is entered as a source. D9, D11, D12, D13, D14, D15, D22, D24 and D25 take its findings; T11 and the summary under the trace table take its retrace; T21 is added (a class missing from EF-1 r4, present here as AM-9) | The review |
| §19; §18 | The concordance and Q12 note that the check of EF-1 r4's new proofs has been made; the summary gives the three tiers and quotes the assessment in the adopted text as that text's | Adopted items (1) and (5) |

**Pass 3: conditions by claim, direct-proof targets, concessions** (adopted direction, c.6897946443).

| Where | What changed | Why |
|---|---|---|
| Standing; §1 | Comment 6897946443 is quoted, and the owner-directions table gains four rows | The record |
| §0 | The adopted claim-to-conditions table (c.6897946443), quoted exactly, with keys K1–K6 and this audit's labels beside it; the two barred shortcuts | Adopted item (1) |
| §12.3 (new) | For each of the 56 rows: which of the six claims its content needs; whether its content is an observable conclusion about a finite experiment (yes 12, partly 13, no 31); for yes and partly, the conclusion, the weakest direct route found and the old proof's conditions it would avoid, each marked as a candidate target with no proof given; for no, why; and the concession category | Adopted items (1), (2), (3) |
| §12.4 (new) | "Conceded": finite-model mathematics 22, replacement theorems 4, conditional 18, nothing to concede 12, with the rows of each | Adopted item (3) |
| §14.4 (new) | The first barred shortcut checked against the nine NEW rows and against every recommendation of §19; the second against the six FIRM and three CONTINGENT statements | Adopted item (4) |
| §19 | Six questions carry a bullet "Changed in r6": Q1, Q6, Q5, Q7, Q9, Q12. Q7's recommendation loses its rider "unless Q6(c) is adopted, in which case (a)". Nine questions are unchanged. The order is unchanged and every question is pending | Adopted item (5) |
| §18 | One paragraph on the reframing | Adopted items (1) to (5) |

**Counts.** None of r5's counts changed: FIRM 6, CONTINGENT 3, NEW 9, replacement candidate 1; the
cross-tabulation's seven rows and its totals; 56 rows; reasons 47, 6, 3; the Q2-17 subset and its counts. New
counts in r6: Table 5's lines (yes 5, no 8, undetermined 3, mixed 4); the direct-proof targets (yes 12, partly
13, no 31); the concession categories (22, 4, 18, 12); the disagreements (D1 to D25, T1 to T21).

**Found by the comparison and left uncorrected in place** (each is in §20 with both positions, for the next
review): the citation "GR:114" for the proof of GR's boundary-only lemma in §14.3's Table 2, where the proof
is at GR:124–126 (T15); and the form "F-each for Stage 1" for Theorem 23, where Stage 1's derivation also
contains a recurrence-cycle sentence (Sub:137) that a fixed-horizon form does not carry (T17).

**Departures from this round's brief, each caused by a later record.** The brief asked that the rule sentence
be sourced as "owner, in session, not separately recorded"; it has since been recorded in 6897859755 and is
cited there. The brief described EF-1 r4's new proofs as unreviewed; the review of EF-1 r4 has since checked
four of them, and r6 reports that status while still resting no class on them. The brief asked that nothing
beyond the re-pin be changed; the third pass follows the later adopted direction (c.6897946443).


## 18. Summary for the owner (plain language)

The audit now covers 57 results that the row list ties to A1; in 48 of them the link to nature runs through A1: the 56 of earlier rounds and one passage found since, the one-step coherence results of Main §3.2 (row AM-5b, unreviewed). The provisional headline, in the words you relayed and adopted (c.6896771264): "none of the 56 results currently establishes a justified observational constraint; that does not mean none can be recovered." On this audit's reading the added row does not establish one either, so the number becomes 57.

Of the 57: 18 are kept as mathematics about finite models; 10 are kept: seven as statements and three as rewordings, one of which changes the falsifiability sentence (Main:718); 10 are removed as claims about nature; 19 have a recovery or owner route. Of those 19, under the one rule for "firm" that you relayed and adopted (c.6898395533): 4 are firm (three results and the ledger entry itself; premises already on main; nothing proved), 5 depend on an undecided reading, 9 need a new assumption, and 1 is a replacement, counted apart. A recovery candidate is not a recovered result. No result has recovery credit.

If recovery fails: 23 survive only as finite-model mathematics, 5 need replacement theorems, 13 stay conditional, 4 are removed, 12 need nothing conceded.

Status, in the words you relayed and adopted (c.6898395533): "The mathematical foundation has strengthened; the audit is still being corrected into a reliable decision document." The review of this audit did not, on what it reported, overturn the checked EF-1 mathematics; it did not re-derive it.

Fifteen questions follow, all pending. After the focused confirmation of r8, with its corrections applied in r9, all are marked ready, except that option (b) of Q2 is not decision-ready until the destinations of §12.2 are agreed. Ready means that the question's text, options, basis and dependencies were checked; it does not mean that any recovery route was verified. One question (Q8) depends on the pilot of the fixed-horizon lemma, and four depend on it in part (§19). Nothing is adopted.

## 19. Owner questions

**All fifteen are pending.** After the focused confirmation of r8 (`CONFIRM-A1-IMPACT-r8.md`), with its corrections applied in r9, every question is READY, with one exception inside Q2: Q2(b) is an option only and is not decision-ready until the destinations of §12.2 are agreed. Verdicts of the confirmation: confirmed, Q5 and Q9; confirmed with correction, Q11, Q1, Q8, Q6, Q3, Q2, Q13, Q14 and Q12; basis untouched by r7 and r8, Q7 (one correction to its option (b)), Q10, Q4 (the wording of its site counts) and Q15. "READY" means only that the question's text, options, basis and dependencies were checked and stand with the listed corrections applied. It does not mean that any recovery route was verified; none was. The corrections as applied in r9 have not been re-read by the confirmer. **Dependence on the pilot** (the bounded pilot of the fixed-horizon lemma authorized in #1169 comment 6898613777; the split is the coordinator's, supplied for r9; the pilot has not reported, and the focused confirmation did not check the split): yes, Q8; in part, Q1 (option (b-loc)), Q3 (option (n2)), Q13 (the family-8 registry action) and Q12 (the fixed-horizon stage); no, Q11, Q6, Q5, Q7, Q9, Q10, Q4, Q15, Q2 and Q14. Each question ends with its readiness, the unchecked rows it rests on and any disagreement attached to it. Recommendations, this audit's and the reviewer's, are recommendations and settle nothing.


**Adoption and every decision below are pending: all fifteen questions are open and none has been answered.** Nothing in this audit adopts a premise, credits a
recovery or decides a cleanup. The questions come to the owner after both reviews, with §20's disagreements
visible (adopted direction, c.6896771264). Q2(b) is an option only. The recommendations are recommendations only. Question
numbers are identifiers, not ordinals: Q1–Q14 keep their numbers from r3, and Q15 was added in r4.

**Changed in r6 by adopted direction c.6897946443** (conditions by claim; direct-proof targets;
concessions; the two barred shortcuts). Six questions change in an option, a reason or a recommendation: Q1
(option (b-loc) is restated by claim), Q6 (the reason for (e) is now the adopted table of c.6897946443; (c) and (d) are
marked against the first shortcut), Q5 (option (b) is marked against the first shortcut), Q7 (the
recommendation loses its rider), Q9 (option (a) is an outcome the adopted direction calls acceptable; the recommendation
is unchanged) and Q12 (the order follows the direct-proof targets). Nine are unchanged: Q11, Q8, Q10, Q4, Q3,
Q15, Q2, Q13, Q14. The order and the dependency diagram are unchanged, and every question is pending. Each
changed question ends with a bullet "Changed in r6".

**Order of decision** (by dependency; foundational choices first): Q11 → Q1 → Q8 → Q6 → Q5 → Q7 → Q9 → Q10 →
Q4 → Q3 → Q15 → Q2 → Q13 → Q14 → Q12. Q7 and Q10 come before Q4, as the review of r4 asks: Q4's count waits
on Q7's (LE) choice, and Q10(b) is a conditional of the kind Q4(a) refers to. Q8(b) and Q5(d) are one decision (whether to widen item (xiii)'s listed role); if either is wanted, decide both at Q5.

**Dependency diagram** ("X ← Y" means X is decided after Y).

```
Q11                    (first; no prerequisite)
 ├─ Q1  ← Q11
 │   ├─ Q8  ← Q11, Q1(b-loc)        [Q8(b) is read together with Q5(d)]
 │   └─ Q9  ← Q1, Q6
 ├─ Q6  ← Q11
 │   └─ Q5  ← Q11, Q6               [Q5(d) is read together with Q8(b)]
 │        └─ Q7  ← Q6, Q8, Q5
 └─ Q10 ← Q11                       [Q10(b) ← Q9]
Q4  ← Q9, Q10, Q6, Q7
Q3  ← Q4, Q8
Q15                    (no prerequisite)
Q2  ← Q1(c), Q7, Q9, Q10, Q15, and the destinations of §12.2
Q13 ← Q2, Q3, Q8, Q15
Q14                    (no prerequisite)
Q12 ← every question above
```

No circular dependency was found. The two pairs marked "read together" are options that widen the same
posit (item (xiii)).

**Concordance with EF-1 r6's eleven questions** (provisional; EF-1 r4 was reviewed, r5 rechecked, and r6 is r5 with the recheck's nits applied). Its 1 (a
fixed-horizon lemma in Main, and which intervention form) ↔ Q1(b-loc) and Q12. Its 2 (Main:362) ↔ Q8. Its 3
(where the carrier comparison belongs) ↔ no question here; §0's Main-independence note. Its 4 (the starting
law) ↔ Q6(d), (e) and Q11. Its 5 (three premises to track: a finite visible region, finite supports over every
branch, finite setting and readout regions) ↔ attached to Q8 here as a sub-item. Its 6 (double stochasticity
as a test; ledger item (iii)) ↔ §11 item 3 and Q9. Its 7 (Main:638 (a)) ↔ Q15. Its 8 (A1's visible content) ↔
Q9(c) and Q4. Its 9 (whether one independent check is enough before anything rests on its proofs: of full-system measure
preservation, the compactness lemma for finite reads on every run, necessity of a finite influence set and the
intervention lemma, each checked by the review of EF-1 r4; and of the closure characterization and the one-law
necessity refinement, each re-derived by the recheck of EF-1 r5) ↔ none among the 15; it is named under Q12.
This audit classes nothing on any of them (§20, D22). Its 10 (which theorem to check first, and which direct
proof to attempt first) ↔ Q12. Its 11 (the finite-hidden-memory draft) ↔ none.

### Q11. Total-dynamics statements and total-sector premises other than A1
- **Plain statement.** Some kept or candidate results are about nature's whole dynamics but assume nothing
  about its size (injectivity on registered content; the cone; C2's hidden conditionals; A.7). Some candidate
  proofs need premises about the whole carrier that assert no size (each site reads finitely many sites, L1; the
  starting law is a probability measure, L9). Does the visible-sector-only condition reach these, or only
  statements that assume total finiteness?
- **Options, each in full.**
  - (a) *A1 consumers only.* The visible-sector-only condition applies to the statements whose proof uses total finiteness, which are the 57 rows of this audit. A statement about nature's whole dynamics that assumes no size stays, or, where it is the landing of a candidate recovery, may land, with its status label. Only the first of the following is on `main` in that form; the others are landings of candidates that have no recovery credit: injectivity on states with distinct registered content (AM-3.1); the coupling-graph cone (AM-7.1); the bounds of the C2-necessity theorems on hidden conditional laws (AM-21.1, as a conditional theorem on a joint law; AM-21.2, which also needs a reference prior under Q6(c)); the restricted statement about finite-step outputs (AM-23.2); purity of the joint state (AM-33.1). A premise about the whole carrier that asserts no size, namely that each site's update reads finitely many sites (L1) or that the starting law is a probability measure (L9), may be proposed and is judged under §A.29 like any premise. *Asserted of nature:* nothing by this answer itself; each such statement keeps its own status and conditions. Basis: the row landing TD in §12.1 (AM-3.1) and the TD landings of AM-7.1, AM-21.1, AM-21.2, AM-23.2, AM-33.1; §14.2 (L1, L9); owner, 6894872312 ("limit A1 results"); the proposal the owner accepted in 6896070253.
  - (b) *Every total-sector statement.* The condition applies to every statement about nature's total or hidden sector, whether or not it assumes a size. No forward-direction statement then stays: the update rule, the cone, and every candidate proof that uses L1 or L9 go, and the rows and landings named under (a) are removed with them. *Asserted of nature:* nothing about the total or hidden sector. Basis: the same rows; §14.2 (L1, L9); the texts of 6894872312 and 6896070253 do not ask for it.
- **Recommendation: (a).** Reason: the decisions are framed on A1 ("limit A1 results", 6894872312; "Remove A1
  (total finiteness) as a claim about the whole substratum", the proposal the owner accepted in 6896070253). Under (b) no forward-direction
  statement survives: the update rule, the cone and every candidate that uses L1 or L9 would go, which the
  decisions' text does not ask for.
- **Dependencies.** None; it is first.
- **What it changes.** Whether the TD row and the TD landings stand (AM-3.1; AM-7.1, AM-21.1, AM-21.2, AM-23.2,
  AM-33.1; AM-8 under Q7(a), (b)) and whether premises L1 and L9 are admissible at all; so every
  forward-direction route.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E11) are all applied in r9 (§22). **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7, AM-21.1 moved to NEW with a conditional theorem available, and to "no" in §12.3 (F5, F6), and AM-23.2 to "partly" (F6); both are TD landings that option (a) keeps and option (b) removes. Rows: AM-21.1, AM-23.2. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** the TD rows AM-3.1, AM-7.1, AM-21.1, AM-21.2, AM-23.2, AM-33.1; 6894872312; 6896070253.
- **Status.** Pending.

### Q1. What "the visible sector" admits
- **Plain statement.** Which finite sectors besides the observer's own may a candidate proof use?
- **Options, each in full.** The options are cumulative: each admits what the one before admits.
  - (a) *The observer's own sector, and constructed realizations.* A candidate proof may use the visible configuration space `C_V` and the observer's registers, finite by Lemma 1 (Main:46), and finite realizations constructed per horizon from the visible law (Main:516). Under (a) alone, P7 (the thermal rate ratio on a boundary shell) and part (3) of P9 (a replacement part, not a recovery) (a per-horizon bound for Theorem 22) are unavailable. *Asserted of nature:* nothing beyond Lemma 1. Basis: Main:46; Main:516; rows AM-2.1, AM-5 (P1).
  - (b-loc) *Also the finite patch within a horizon.* Also the finite set of sites on which the visible record depends within a fixed observation window. It is finite by the fixed-horizon lemma (EF-1 r6, Lemma PM and Lemma PM-I; paper proofs in an unpushed draft, each with one independent check) under that lemma's premises: each site's update reads finitely many sites (L1); a finite alphabet at each site (L2); a finite visible region with a site-local readout (L8); and, where interventions act, finite support over every branch (FS-all). This is the first claim of the adopted table, "Finite description for a fixed observation window" (adopted direction, c.6897946443), and it is available to a row only for that claim: a row that also needs probabilities, a distributional property, a closed model or an all-time model needs those separately (§0, key; §12.3). Admitting the patch adopts none of L1, L8 or FS-all; they stay hypotheses, and where they are recorded is Q8. *Asserted of nature:* nothing. Basis: §14.2 (L1, L2, L8, FS); §14.3, Tables 1 and 2; rows AM-7.1, AM-23.2, AM-31 part (3), N-3's replacement; no row has recovery credit until its requirements are checked.
  - (b-mode) *Also the boundary layer, by mode count.* Also the boundary layer, taken as finite by GR's mode count `A/ε²` (L5). *Asserted of nature:* that count, as an existing named GR premise of conditional results. It rests on the holographic input that Main excludes (Main:700) and on E3, whose justification is open. P7 needs it (AM-22, AM-36, and through P7 AM-11 and AM-24). P7 also needs a shell measure (Q6(c)) and an invertible time-reversal-covariant rule (Q5(b) or (d)), and no route for AM-22 was found that avoids a shell measure (§12.3). Under the recommended answers to Q6 and Q5, P7 is not attempted, and (b-mode) then changes nothing for these four rows beyond keeping GR's existing conditional statements. Basis: GR:90; GR:665 (S3); Sub:92 (E3); Main:700; rows AM-22, AM-36.
  - (c) *Also an isolated hidden subsystem.* Also a hidden subsystem that is finite by a mode count and is treated with its radiation as an isolated system under H-decouple (L7), such as the black-hole interior `B` of GR Appendix A. H-decouple "is not established here" (GR:787; GR:795 states the condition). Without (c), AM-33.2 (cycle typicality and the cycle-averaged Page curve) stays finite-model mathematics with no physical reading. *Asserted of nature:* H-decouple for that subsystem. Basis: GR:787, :795, :835; row AM-33.2.
- **Recommendation: (a) with (b-loc); keep (b-mode) only as a named GR premise of conditional results; not (c)
  for now.** Reason: (b-loc) is a derived lemma on Main-level premises, with no recovery credit for any row
  until that row's requirements are checked (§14.3); (b-mode) rests on the holographic input Main excludes
  (Main:700) and on E3, whose justification is open; (c) needs H-decouple, "not established here" (GR:787).
- **Dependencies.** After Q11.
- **What it changes.** Under (a) only, P7 and part (3) of P9 (a replacement part, not a recovery) are unavailable (AM-22 and AM-36 not recoverable
  as planned; AM-31 kept in parts (1), (2); AM-11 and AM-24 lose P7; AM-14 not a tool). Without (c), AM-33.2
  stays RM with no physical reading. Also N-2 and N-3's replacement.
- **Changed in r6** (6897946443). Option (b-loc) is the first claim of the adopted table, "Finite description for a fixed
  observation window", and it is available to a row only for that claim: a row that also needs probabilities,
  a distributional property, a closed model or an all-time model needs those separately (§0, key; §12.3). The
  recommendation is unchanged.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E12) are all applied in r9 (§22). **Depends on the pilot:** in part (option (b-loc)). r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7, AM-22 lost its direct-proof route (no route avoids a shell measure, F4), which bears on what (b-mode) is for, and AM-31 became FIRM for the theorem as stated with part (3) a replacement part (F7), which bears on what (b-loc) is for. Rows: AM-22, AM-31, AM-36. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** AM-24; Main:700 was not read by the review.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** the review of r6 asks that (b-loc) be read "under its named hypotheses": admitting the patch adopts none of L1, L8 or FS-all; r7 agrees.
- **Basis of the options.** GR:787, :795; Main:700; rows AM-14, AM-22, AM-31, AM-33.2, AM-36, N-2.
- **Status.** Pending.

### Q8. Locality inputs for the cone, the Bell layer and the fixed-horizon lemma
- **Plain statement.** The cone needs each site's update to read finitely many sites (L1). Main:362 derives
  that from global finiteness, which goes. A finite description also needs a finite visible region with a
  site-local readout (L8) and, where interventions act, finite support over every branch (FS); on `main` both
  follow only from the finite site set. How should these be stated? (The last two are parts (a) and (b) of EF-1 r6's question 5; its part (c), finite setting and readout regions for the Bell theorem, is the same premise for the one setting step.)
- **Options, each in full.** The ledger count is unchanged under each.
  - (a) *Restate ledger item (ix).* Item (ix), "bounded coupling degree (A3)" (Main:724), now stated for a family, is restated for one carrier of undetermined cardinality in the dependency sense: each site's update is a function of the values at a bounded number of sites. A bound on the degree of the graph that Main:362 reads from single-component sensitivity would not give this on an infinite carrier (EF-1 r6 N1.2). *Asserted of nature:* that each site's update reads finitely many sites, as a posit in force. The wording of item (ix) changes. Basis: Main:724 (ix); Sub:96 (A3); the contingency of AM-7.1 (§14.1).
  - (b) *Extend item (xiii)'s listed consumers.* Item (xiii), the second-order update "with each $F_i$ reading the current values at finitely many sites" (Main:724), has its listed consumers extended to §3.3's cone. The cone then holds for the selected lattice model only. *Asserted of nature:* nothing beyond item (xiii), whose listed role widens. This widens the same posit as Q5(d); the two are one decision, taken at Q5. Basis: Main:724 (xiii); the kernel's `leapFiniteRange` for the reference rule; rows AM-7.1, AM-7.3.
  - (c) *Named hypotheses, carried where they enter.* No ledger item changes. Each statement that uses them carries as named hypotheses of its own: finite reading sets (L1); a finite visible or readout region with a site-local readout (L8); and, where interventions act, finite support in the all-branch form (FS-all). Item (xiii) is cited as the instance of the first on the selected model. *Asserted of nature:* nothing. *Asserted conditionally:* the cone (P3), the restricted statement about finite-step outputs (P16) and the `Ω_n` route of the Bell ceiling, each in the form "if these hold, then …". [This audit's reading; unreviewed:] the same choice is the one under which P4's two added hypotheses (hypothesis (iii) read with a coupling graph in the dependency sense; measurable response functions) are carried as hypotheses of the Bell statement, which is the reading AM-7.2 and AM-7.3 are CONTINGENT on (§14.1). Basis: Main:724 ("the named hypotheses of the matter, gauge and gravity sectors are carried where they enter"); applying that convention to this hypothesis is this audit's proposal and is not stated by Main; Main:362; rows AM-7.1, AM-7.2, AM-7.3, AM-23.2; EF-1 r6, question 5.
- **Recommendation: (c).** Reason: it changes no ledger item, keeps the cone's generality beyond the selected
  model (Main:362 is stated for the full spatial constitution), states every condition where it enters
  (Main:724: "the named hypotheses of the matter, gauge and gravity sectors are carried where they enter"), and asserts nothing new of nature. The
  cone is stated with the union `U_n` (EF-1 r6 N1.1).
- **Dependencies.** After Q11 and Q1(b-loc). Option (b) widens the same posit as Q5(d); read Q5 before
  choosing (b).
- **What it changes.** Two CONTINGENT rows, AM-7.1 and AM-23.2, through finite reading sets; and, on this audit's disputed classification only, AM-7.2 and AM-7.3 through P4's two added hypotheses (§14.1). Those two hypotheses are properties of completions, and under each of (a), (b) and (c) the Bell statement would carry them itself; P3, P4 (both routes),
  P8-M and P16; Main:20's headline status (H1); the ledger wording of (ix) or (xiii). AM-7.3's cone is the kernel's and does not need L1; its class waits on P4's measurable-response hypothesis only.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E13, E14, E15) are all applied in r9 (§22). **Depends on the pilot:** yes. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7, AM-7.2 and AM-7.3 moved to CONTINGENT on a reading assigned to this question (F5, F10), a class the review of r6 disputes (§14.1), and AM-23.2 changed to "partly" (F6). In r8, "What it changes" counts four CONTINGENT rows where r7's text still said two of three, and option (c) says in words that it is the option under which P4's two added hypotheses are carried; that sentence is this audit's reading and is unreviewed. Rows: AM-7.1, AM-7.2, AM-7.3, AM-23.2. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 items 5 and 8; Q8(b) and Q5(d) are one decision. Also the class of AM-7.2 and AM-7.3: this audit, CONTINGENT; the focused confirmation of r8 recommends FIRM with a scope note (§14.1; §20, "Disagreement with the focused confirmation of r8"). Neither is settled.
- **Basis of the options.** Main:362; Main:724 (ix), (xiii); rows AM-7.1, AM-7.2, AM-7.3, AM-23.2, N-3.
- **Status.** Pending.

### Q6. The measure (item (iv))
- **Plain statement.** Some results need probabilities for what is hidden. With A1 the papers get them by counting equally over a finite set (ledger item (iv), Main:724; Lemma 3, Main:54). Without A1 that counting measure cannot be normalized (Sub:262). What, if anything, is said about nature's starting probability law?
- **Options, each in full.**
  - (a) *Realization only.* Item (iv)'s maximal-entropy selection is kept as the default prior of a constructed finite realization (Main:58; Main:516). *Asserted of nature:* nothing. Basis: AM-4.1, AM-4.2, AM-4.3.
  - (b) *Retire item (iv).* No measure selection is stated, for nature or for realizations. *Asserted of nature:* nothing. Basis: AM-4.3; Main:724.
  - (c) *Adopt a reference state.* A normalized reference state on nature's hidden sector, with the properties each proof needs (invariant, uniform on shells, equivariant), is adopted as a premise under §A.29, by rewriting item (iv) (count unchanged) or as a new item (count plus one). *Asserted of nature:* that state. Basis: the needs of P5b, P6, P7, P8, P12, P13 (AM-21.2, AM-30, AM-22, AM-8, AM-11, AM-4.4); no §A.29 case is drafted.
  - (d) *Normalization only.* Item (iv) is restated for nature as: the starting law is a probability measure, with no selection (L9; count unchanged). It replaces item (iv) and is not a reading of it (Main:724 (iv) states a selection); it is judged under §A.29. *Asserted of nature:* that a normalized starting law exists. Basis: AM-31 part (3), AM-21.1, N-2; GR:132 and Sub:262 state such a law only as a hypothesis.
  - (e) *Hypothesis carried, nothing posited.* Nothing is posited of nature. Each forward-direction statement that uses probabilities carries "a normalized starting law", and each further property it uses (invariance, uniformity, time-reversal symmetry, equivariance, a reference prior), as named hypotheses in its own statement, where they enter. *Asserted of nature:* nothing. *Asserted conditionally:* each such theorem, in the form "if the starting law is of this kind, then …". Basis: Main:724 ("the named hypotheses of the matter, gauge and gravity sectors are carried where they enter"); applying that convention to this hypothesis is this audit's proposal and is not stated by Main; the table of adopted direction c.6897946443 (probabilities need "A suitable starting probability law"); rows AM-21.1, AM-21.2, AM-30, AM-4.4, AM-31 part (3).
- **What each choice allows, consistent with Q12.** *Conditionally:* under (a), (b) or (e), without (c), P5b, P6 and P13 may be written and proved as conditional theorems with the measure as a named hypothesis; they wait on Q11 and Q12 only and assert nothing of nature. *Of nature:* none of P5b, P6, P7, P8-M, P8-S, P12, P13 can be asserted of nature before (c). P7, P8-M, P8-S and P12 are not scheduled as conditional theorems either (AM-22 has no route that avoids a shell measure, §12.3; AM-8 and AM-11 are conceded, §12.4). Under (d), part (3) of AM-31 could be asserted of nature; under (e) without (d) it is a conditional theorem only. The same holds for P5a (AM-21.1): under (d) its bound could be read of nature's hidden conditionals, with Q11(a); under (e) without (d) it is a conditional theorem on a joint law (§14.4). The ledger count rises by one only under (c) as a new item.
- **Recommendation (this audit's; the review of r6 recommends (e) and does not dispute (a), its section 11, item 4; neither is settled): (a) together with (e); neither (c) nor (d) now.** Reason: (a) keeps every realization-level result; (e) shows each condition where it enters and adopts nothing; for (c) no support was found beyond rescuing the rows that need it, which is the first barred shortcut (§14.4); for (d) no §A.29 case is drafted (which results it preserves, and what it predicts), and under (e) every statement that needs probabilities is still available as a conditional theorem. r4 and its review recommended (a) with (d) (§20, D17). Option (e) is not endorsed (adopted direction, c.6898395533: "I cannot endorse that option without seeing its text and basis.").
- **Dependencies.** After Q11 (whether a premise about the total sector, L9, is admissible at all).
- **Rows.** AM-4.3, AM-4.4, AM-21.1, AM-21.2, AM-22, AM-30, AM-31, AM-36, AM-8, AM-11.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E15, E16, E17; E18 calls for no edit) are all applied in r9 (§22). **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7 the question text was rewritten (F2; adopted direction, c.6898395533), AM-21.1 moved to NEW, AM-22 lost its direct route (F4) and AM-31's part (3) became a replacement part (F7). In r8 the option texts are unchanged; §14.4's first table gains a line for AM-21.1 (L9 carried as a named hypothesis, the treatment option (e) describes), which applies the option to that row and is unreviewed. Rows: AM-21.1, AM-22, AM-31, AM-4.4.
- **Unchecked rows it rests on.** AM-24.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 item 4: (e) or (d). The review of r6 recommends (e); that is a recommendation, and the owner has not endorsed it.
- **Basis of the options.** in each option above.
- **Status.** Pending.

### Q5. Bijectivity of nature (A2, item (iii))
- **Plain statement.** The papers take nature's update rule to be reversible: no two states merge, and every state has a predecessor. On a finite set, no merging gives the rest (Main:60). Without A1 that step fails, and the paused AM-3 unit found no weaker premise among W1–W3 that recovers it. What is said of nature?
- **Options, each in full.**
  - (a) *Record prong only.* Nature's dynamics is stated as injective on states with distinct registered content (Main:36, :60). Bijectivity is kept for constructed realizations, where it holds by construction (Main:97, :520). Injectivity on the hidden sector, and surjectivity, are stated as open for nature. *Asserted of nature:* record preservation only. Basis: AM-3.1, AM-3.2.
  - (b) *Postulate.* Reversibility of nature's dynamics is adopted as a postulate, the alternative that item (iii) names (Main:724), under §A.29; item (iii) is rewritten and the ledger count is unchanged. *Asserted of nature:* bijectivity. Basis: its only uses found are P6, P10 and the headline clause H3 (AM-30, AM-33.1, AM-3.2).
  - (c) *Resume the AM-3 unit* with a candidate premise outside W1–W3. *Asserted of nature:* nothing until that unit reports. Basis: AM-3.2, recovery attempt.
  - (d) *From the form of the selected rule.* On the selected model the update has the second-order form of item (xiii) (Main:724), which is invertible by its form on any site set (`a2_every_substratum`, `SubstratumInterfaceAudit.lean:106`, definitional; not read by the review of r6). Taking A2 from it widens item (xiii)'s listed role beyond §3.2 and §3.4. *Asserted of nature:* bijectivity, as far as nature's rule is the selected one. Basis: AM-3.2; AM-33.1, which is CONTINGENT on this reading. It is one decision with Q8(b).
- **What each choice allows, consistent with Q12.** *Conditionally:* under (a), P6 and P10 may be written and proved as conditional theorems with bijectivity (P6) or injectivity (P10) as a named hypothesis; they wait on Q11 and Q12 only and assert nothing of nature. *Of nature:* none of P6, P7, P10, P12 can be asserted of nature before (b) or (d), nor P8-M if its invertibility check fails. P7 and P12 are not scheduled as conditional theorems either (AM-22 has no route that avoids a shell measure; AM-11 is conceded). Under (a) the C2-structural clause leaves the abstract or is stated as open (H3).
- **Recommendation (this audit's; not settled): (a).** Reason: it loses no prediction, adds no premise and matches the record prong on `main`. As things stand (b) would be adopted only to rescue P6, P10 and H3, the first barred shortcut. (d) has support of its own, the form of the rule, and is the alternative if P6, P10 or H3 are wanted of nature.
- **Dependencies.** After Q11 and Q6; with Q8 for (d).
- **Rows.** AM-3.2, AM-30, AM-33.1, AM-22, AM-11, AM-8.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED; no correction. **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7 the question text was rewritten (F2; adopted direction, c.6898395533) and AM-22 lost its direct route (F4). In r8 nothing in this question changes. Rows: AM-22, AM-30, AM-33.1.
- **Unchecked rows it rests on.** AM-24; `a2_every_substratum` was not read by the review.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** in each option above.
- **Status.** Pending.

### Q7. §4.6 (observer selection)
- **Plain statement.** The §4.6 theorems are proved for a finite bijective total system. How are they treated?
- **Options, each in full.**
  - (a) *Recover in Main (P8-M).* §4.6 is restated in Main for a measure-preserving map with an isometric Koopman operator: `τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε)` under (EM), with the projection `P_Σ` defined by a normalized invariant reference state. It needs Main's cone (P3; Q8); a reference state adopted under Q6(c); and (LE), that every bounded-diameter region of the equilibrium macrostate is in its local equilibrium state under the reference state, carried like (EM) or adopted as a posit, or a typicality premise in its place. *Asserted of nature:* the reference state; (LE) if it is posited (the ledger count then rises by one). (LE) was introduced by this audit only to keep the observer-selection rule and has no support beyond that (§14.4). Basis: Main:742–758; row AM-8; §14 (P8-M).
  - (b) *Relocate to Substratum (P8-S).* §4.6 is restated in Substratum on a finite enclosing region that is approximately isolated under H-BD, with the normalized equilibrium state as a premise (Q6(c)); (EM) and `τ_B` move into Main §1.3 or §2.3, so that Main stays independent, and the references at Main:169 and Main:656 are removed. *Asserted of nature:* the equilibrium state; H-BD, an existing GR posit. Basis: row AM-8; §14 (P8-S); Main:169, :656; Sub:401.
  - (c) *Remove.* The §4.6 theorems are deleted, with the losses listed in §13 item 8. *Asserted of nature:* nothing. Valid finite-model mathematics would leave `main`. Basis: §13 item 8; row AM-8.
  - (d) *Keep as finite-model mathematics.* The theorems stay as theorems about "a finite bijective $(S, \varphi)$" (Main:742), category RM, and the observer-selection reading for nature is removed. *Asserted of nature:* nothing. Nothing is deleted. Basis: Main:742; the proposal the owner accepted in 6896070253; §12.4.
- **Recommendation: (d).** Reason: (a) and (b) both need a Q6(c)
  premise, and the fixed-horizon lemma carries only the cone step (§14.3, Table 2); (d) follows 6896070253
  (the proposal the owner accepted there: "stay as mathematics about finite models") and deletes nothing; (c) would delete valid finite-model
  mathematics without need.
- **Dependencies.** After Q6, Q8 and Q5.
- **What it changes.** AM-8 (RC 17, RX 11 or RM 18); Main:159, :169, :656; Sub:401; the ledger count if (LE)
  becomes a posit, which is why Q4 follows.
- **Changed in r6** (6897946443). r5 recommended "(d), unless Q6(c) is adopted, in which case (a)". The rider
  is withdrawn. Option (a) needs, besides a reference state, the hypothesis (LE) or a typicality premise, and
  (LE) was introduced by this audit only to keep the observer-selection rule; it has no support beyond that
  (§14.4). §4.6 has no observable conclusion about a finite experiment (§12.3), so there is no direct-proof
  target to pursue instead. The recommendation is (d): the theorems survive as finite-model mathematics.
- **Decision-ready?** READY. Focused confirmation of r8: basis untouched by r7 and r8; one error in r8's text of option (b); its listed corrections (E27) are all applied in r9 (§22). **Depends on the pilot:** no. r8's entry: Basis reviewed (Main:744, :752, :756, :758). No change in r7 or r8 materially alters it: r7 only states (LE) in full (F17). r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20, T31 (window entry for AM-8); no bearing on the recommendation.
- **Basis of the options.** Main:742–760; row AM-8.
- **Status.** Pending.

### Q9. A1-test conditionals (§11)
- **Plain statement.** Two results say what A1 would imply at accessible times (candidates 1 and 2: (1) one fixed finite carrier cannot reproduce every qubit experiment; (2) corner occupancy, Main:216). Keep them as
  labelled conditionals, or remove them? (Double stochasticity is not a test of A1, §11.)
- **Options, each in full.**
  - (a) *Keep both as labelled conditionals.* Candidate 1 (one fixed finite carrier of `N` states cannot reproduce every qubit experiment; Main:558; row AM-9.2) and candidate 2 (corner occupancy; Main:216; row AM-6.2) are kept in the form "if nature's total carrier is finite, then …": candidate 1 under the stated interface and accessible only for a stated bound on `N`; candidate 2 with its contested accessibility. Each is labelled as conditional on A1 and is not presented as a consequence of OI (the second barred shortcut). *Asserted of nature:* nothing; A1 survives as the named hypothesis of the two conditionals. Adopted direction c.6897946443 names "remain conditional" as an acceptable outcome. Basis: Main:216, :558, :600; rows AM-6.2, AM-9.2; §11.
  - (b) *Remove both.* Both conditionals are removed with their rows; A1 then survives as a hypothesis only if Q10(b) keeps it. *Asserted of nature:* nothing. Basis: the same rows; §11.
  - (c) *Remove both, and keep at most one model-class sentence.* Both are removed, and at most one sentence of A1's visible form is kept, for the autonomous case, as mathematics about finite models: the record of a finite bijection is periodic; that of a finite deterministic map is eventually periodic; no bound on the period or the transient is given; it does not apply with continuing inputs. *Asserted of nature:* nothing. Basis: §11; the proposal the owner accepted in 6896070253; adopted direction, c.6896496410, on eventual periodicity and continuing inputs.
- **Recommendation: (c).** Reason: neither candidate gives an accessible test without a bound on `N` that nothing
  on `main` supplies, so with `N` free each can be fitted to any outcome (§A.29); candidate 2's
  finite-versus-infinite alternative is not distinguished at a fixed horizon in the native class [IR]. The
  visible-form sentence is true mathematics about finite models (6896070253) and asserts nothing about nature.
- **Dependencies.** After Q1 and Q6.
- **What it changes.** AM-6.2, AM-9.2 (two RX rows) and §11; whether A1 survives as a named hypothesis, which
  Q4 and Q10(b) use.
- **Changed in r6** (6897946443). The adopted direction names "remain conditional" as an acceptable outcome, so option (a) is within what it accepts, provided each statement is labelled as conditional on A1 and is not
  presented as a consequence of OI (the second barred shortcut). The recommendation, (c), is unchanged, for
  its own reason: with the size of the carrier free, neither conditional yields an accessible test.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED; no correction. **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Change that materially alters its basis: in r7 the two rows are conceded as removed under the recommended answer, where r6 counted them as remaining conditional (F3); under option (a) they would remain conditional. Rows: AM-6.2, AM-9.2. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 item 14; the review of r6 recommends (c), as this audit does.
- **Basis of the options.** Main:216, :558, :600; rows AM-6.2, AM-9.2.
- **Status.** Pending.

### Q10. Cosmic recurrence (F8) and §18.7
- **Plain statement.** §18.7 predicts that nature recurs with period at most `g(|S|)`; without A1 there is no
  `|S|`.
- **Options, each in full.** F8 is retired as a falsifier under every option.
  - (a) *Remove.* §18.7's recurrence content and F8 are removed, with `ch18-beyond.md:244` and :290. Nothing of the bound is kept. *Asserted of nature:* nothing. Basis: row N-1.
  - (b) *Keep as a conditional on A1.* §18.7's statement is kept in the form "if nature's total carrier is finite with `|S|` states, it recurs with period at most `g(|S|)`", a conditional of the kind Q9(a) keeps, labelled as conditional on A1. *Asserted of nature:* nothing; A1 survives as its named hypothesis. Basis: row N-1; Q9.
  - (c) *Remove the prediction; keep the bound as finite-model mathematics.* The prediction for nature and F8 are removed, and the period bound for a permutation of a finite set stays in the chapter as a statement about finite models (§12.2). *Asserted of nature:* nothing. Basis: row N-1; the proposal the owner accepted in 6896070253; adopted direction, c.6896496410 ("a finite description for a chosen horizon supplies no recurrence guarantee within that horizon").
- **Recommendation: (c).** Reason: 6896070253 keeps A1-needing results as mathematics about finite models; the
  bound is standard mathematics; the prediction has no accessible-time content, and a finite description for a
  chosen horizon supplies no recurrence guarantee within that horizon (6896496410).
- **Dependencies.** After Q11; after Q9 for option (b).
- **What it changes.** N-1; F8 (retired under every option); §18.7; `book/README.md:90`;
  `appendix-c-objections.md:132`. Under (c) the kept bound stays in the chapter (§12.2).
- **Decision-ready?** READY. Focused confirmation of r8: basis untouched by r7 and r8; no correction. **Depends on the pilot:** no. r8's entry: Basis reviewed in part (the opening of §18.7; `ch18-beyond.md:168`, :172). No change in r7 or r8 materially alters it. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** row N-1.
- **Status.** Pending.

### Q4. Ledger item (ii) and the ledger count
- **Plain statement.** Item (ii) is A1 itself. Owner decision 6896070253 removes A1 as a claim about the whole
  substratum. How is the ledger entry handled?
- **Options, each in full.**
  - (a) *Retire item (ii).* The item's number is kept and is not reused (§A.30). "Fourteen items … not fourteen" becomes "Thirteen … thirteen", or `14 − 1 + a` if items are added, where `a` counts a reference state added as a new item under Q6(c) and (LE) adopted as a posit under Q7(a) (§9 item 1). The citations of the item are rewritten (four by number and ten by name were found by search, §9 item 1; the corpus search of §A.25 is repeated at correction time). A1 survives, if at all, only as the named hypothesis of conditionals kept under Q9 or Q10(b). *Asserted of nature:* nothing. Basis: Main:724; row N-6; §9 item 1.
  - (b1) *Restate as a hypothesis that is not posited.* Item (ii) stays in the ledger, restated as the named hypothesis of the conditionals kept under Q9 or Q10(b), and marked as not posited. The count stays fourteen. *Asserted of nature:* nothing. The ledger's own convention carries named hypotheses where they enter, not as items (Main:724). Basis: Main:724; row N-6.
  - (b2) *Restate with new content.* Item (ii) is given new content, for example finite alphabets with finite dependency sets (L1, L2), which is a premise judged under §A.29. The count stays fourteen. *Asserted of nature:* the new content. It would duplicate what items (ix) and (xiii) already state on the selected model, and under it N-6 is NEW (§14.1). Basis: Main:724 (ix), (xiii); row N-6.
- **Recommendation: (a).** Reason: it implements 6896070253 directly; (b1) would put a named hypothesis in a
  ledger whose own convention carries named hypotheses where they enter, not as items (Main:724); (b2) would
  duplicate L1 and L2, which items (ix) and (xiii) already state on the selected model.
- **Dependencies.** After Q9 and Q10; its final count after Q6(c) and Q7's (LE).
- **What it changes.** N-6 (REMOVE under (a)); the count, 13 to 16; Main:60, :700, :718, GR:585 and the ten
  by-name sites (found by search; not claimed complete, §21); Main.tex and Main.pdf regenerated.
- **Decision-ready?** READY. Focused confirmation of r8: basis untouched by r7 and r8; the wording of the site counts corrected; its listed corrections (E33) are all applied in r9 (§22). **Depends on the pilot:** no. r8's entry: Basis reviewed in part (Main:724; the site lists were not recounted). No change in r7 or r8 materially alters it. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** AM-10.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** Main:724; row N-6; §9 item 1.
- **Status.** Pending.

### Q3. A1 as an identifier and the A1–A6 class; N-3
- **Plain statement.** If A1 is no longer a premise, what happens to the label "A1", the class "A1–A6", and the
  universality-class property "Finiteness" (N-3)?
- **Options, each in full.** Two choices: one for the label, one for N-3.
  - (a) *Retire the identifier A1.* The identifier is kept and is not reused (§A.30). The lines that say "A1–A6" are rewritten (65 by the pattern of §9 item 3; paraphrases are found at correction time by the corpus search of §A.25); A4's parenthesis, "a finite periodic lattice" (Sub:98), is restated, with the sentence of Stage 2 (a) that uses it (Sub:157); the census notes of families 12, 13, 48 and 49 are updated. Basis: Sub:92–104; §9 item 3; §10; §15.
  - (b) *Reuse the identifier.* "A1" is reused for finiteness of the visible sector and of the boundary layer. The kernel's `A1` and the identifiers of census families 13, 15, 49 and 53 would then mean something else, which needs a Lean naming decision and a registry decision. §A.30 bars reusing a retired identifier. Basis: §10; §9 item 3.
  - (n1) *Retire the property.* The universality-class property "Finiteness" (`ch09-universality.md:106`) is retired; the "six structural properties" count changes with it. N-3 lands RX. *Asserted of nature:* nothing. Basis: `ch09-universality.md:106`; row N-3.
  - (n2) *Replace the property.* A different commitment takes its place: a finite visible sector with finite reading sets and finite alphabets (L1, L2). It is a replacement candidate and not a recovery of the original property (adopted direction, c.6896890693), which serves exact recurrence and which no route found recovers. N-3 lands RW; it needs Q8's answer. *Asserted of nature:* L1 and L2, in the form Q8 gives them. Basis: row N-3; §14.1; §14.2 (L1, L2).
- **Recommendation: (a); for N-3, (n1), with (n2) added under its own name only if Q8 is answered.** Reason:
  §A.30 bars reusing a retired identifier, and (b) creates a name clash with the kernel's predicate. The
  property as stated serves exact recurrence only (`ch09-universality.md:106`), which no route found recovers;
  (n2) is a replacement candidate, not a recovery (adopted direction, c.6896890693), so it should not keep the old property's
  name or its role in the recurrence route.
- **Dependencies.** After Q4 and Q8.
- **What it changes.** N-3 (RW 4 or RX 11); the "six structural properties" count; the class of Theorem 23
  (P12); the census notes.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E19, E33) are all applied in r9 (§22). **Depends on the pilot:** in part (option (n2)). r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Change that materially alters its basis: in r7, AM-11's entry points for A1 gained the recurrence-cycle sentence of Stage 1 (Sub:137), A4's finite periodic lattice (Sub:157) and reciprocal transition counts (Sub:167) (F11), which bear on what restating the class A1–A6 requires; r8 carries the same into §15's first bullet. Rows: AM-11, AM-24, N-3. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** AM-24, AM-25.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** `ch09-universality.md:106`; Sub:92–104; rows N-3, AM-11; §9 item 3.
- **Status.** Pending.

### Q15. Main:638's open question (a)
- **Plain statement.** Main:638 leaves open "exact all-time gluing for recurrent families of multi-time laws".
  EF-1 r6 (N2.5, N2.9) writes out, with both directions, a candidate: without inputs, one all-time realization
  exists exactly for families that repeat with one common period along every path. It proves existence, not
  that given per-horizon realizations join, and it does not cover experiments with interventions. It is a
  one-description-for-every-horizon statement, which adopted direction c.6896496410 lists as not established here.
- **Options, each in full.**
  - (a) *Commission a proof note.* A separately scoped and independently reviewed proof note is commissioned before any change to Main. It fixes which reading of "recurrent" and of "gluing" Main:638 intends and gives each direction its own proof (§A.34). Main:638 is unchanged until it reports. Basis: Main:638; EF-1 r6 N2.5 and N2.9 (a candidate only: existence, not joining; without inputs).
  - (b) *Leave the open question as stated.* Main:638 is unchanged, and so are Main:731, Intro:178, the phrase anchor of census family 40 and the guard `R7-RCL`. Basis: Main:638; row AM-9.1; §10, family 40.
  - (c) *Treat it within the review of EF-1.* The candidate of N2.5 and N2.9 is assessed as part of the EF-1 unit's own review, and nothing is commissioned here. r6 worded this option "within the review of EF-1 r4". That review, and the recheck of EF-1 r5, have since been made; this audit has not checked whether either examined N2.9, so the option stands as worded and may already be spent. Basis: EF-1 r6 N2.5, N2.9; §16.
- **Recommendation: (b) now; (a) if the owner wants Main:638 narrowed.** Reason: the candidate does not answer
  the question as Main:638 and Intro:178 word it (joining); saying it is answered would be a status change
  with two directions neither of which is in the kernel (§A.34); and a rewording touches Main:731, Intro:178,
  the census anchor of family 40 and the guard `R7-RCL` in one commit.
- **Dependencies.** None.
- **What it changes.** AM-9.1's Main:638 and family 40's phrase anchor; it feeds Q2 and Q13.
- **Decision-ready?** READY. Focused confirmation of r8: basis untouched by r7 and r8; no correction. **Depends on the pilot:** no. r8's entry: Basis reviewed in part (Main:638). No change in r7 or r8 materially alters it: r7 corrects one stale census cell (F12). r8 notes under option (c) that the review it names has since been made, which the owner may wish to weigh. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 item 6: four kernel-only families; the review of r6 agrees.
- **Basis of the options.** Main:638; row AM-9.1; §10 family 40.
- **Status.** Pending.

### Q2. Placement of the RECAST-MATHEMATICAL rows
- **Plain statement.** Eighteen rows (the 17 of adopted direction c.6896890693, marked Q2-17 in §12.1, and AM-5b) are true of every finite model of their
  class; their readings for nature go under every answer (6896070253). Where are the statements written?
- **Options, each in full.** Population: the 18 RECAST-MATHEMATICAL rows of §12.1 (the adopted 17 and AM-5b). No option changes a physical claim: the readings for nature go under every answer.
  - (a) *Keep in place.* Each of the 18 statements stays where it stands, as a theorem about its stated model class, with no physical reading. *Mathematics moved or withdrawn:* none. Basis: §12.1, column "Now"; the proposal the owner accepted in 6896070253.
  - (b) *Reformulated placement; **an option only**.* Of the adopted 17: the statements whose mathematics is kernel-checked on `main` are withdrawn from the text (5 rows: AM-4.1, AM-27.1, AM-27.2, AM-28, N-5; their Lean modules stay, and families 6, 19, 21 and 22 become kernel-only in the same commit); the statements whose only proof on `main` is manuscript text are kept with their paper proofs (7 rows: AM-16, AM-32, AM-33.2, AM-34 and AM-37 in the paper they are in, AM-9.1 in Main, and AM-1.1 at a destination to be agreed, §12.2); AM-4.2 stays in place with `T` restated from a realization's prior `π_H`, so that AM-21 keeps its benchmark (1 row; **[reviewer reading, unresolved]** for the reverse-direction lemma of Main:274–278; on r4's reading it moves, to a Main appendix); AM-6.1's application of an external import is withdrawn (1 row); and the three kernel-only rows (AM-25, AM-29, AM-38) are unchanged (3 rows); 5 + 7 + 1 + 1 + 3 = 17. AM-5b, the 18th, stays in Main §3.2 with its proofs and its hypothesis, as under (a). A form with a uniform law on the hidden boundary sites alone is a candidate with no proof on `main` and no recovery credit (AM-5b, item 3); it is not part of this option. Every A1-free result inside these rows stays in place: the stochastic-inverse lemma (Main:131–133); Main:139's two A1-free sentences; Main:145's definitions and separations; AM-27's theory-general results; the separability-threshold Theorem (Main:312–314, with the kernel witnesses named there); and the definitions that kept text uses. Under (b) no valid mathematics leaves `main`. Basis: §12.1, columns "Under Q2(b)" and "Mathematics under Q2(b)"; §12.2; §10; adopted direction, c.6896771264 and c.6896890693.
  - (c) *Row by row.* Each of the 18 is placed on its own, for example keeping in the body the model-class statements that a kept root of Main uses and moving the rest to a Main appendix. Basis: §12.2 (the Main-independence check for each destination).
  - Under every option the headline sites follow H1–H3 (§8).
- **Recommendation: no choice yet.** Q2(b) is **not decision-ready until the destinations are agreed**: where
  AM-1.1 goes (a Main appendix, or a companion with four Main sentences and four companion pointers rewritten),
  the root trace that decides whether the Main-root rule allows it to stay in Main, and the standing of
  Main:274–278 (§12.2). If a choice is wanted before that, (a): under (a) and (b) the physical claims removed
  are the same and no mathematics is deleted, so (b) changes placement only, and §A.25's
  minimum-necessary-change rule favours the smaller change. This is a recommendation only (§20, D16).
- **Dependencies.** After Q1(c), Q7, Q9, Q10 and Q15, which decide which content is RM; and after the destinations
  of §12.2.
- **What it changes.** The placement of the 18 RM rows and of the RM landings (AM-2.1; AM-8 under Q7(d); N-1's
  bound under Q10(c)) and the model-class sentence kept under Q9(c), whose content is already at Main:638 ("any fixed realization with a fixed prior has an exactly $L$-periodic multi-time law"), which stays in Main as AM-9.1 [the focused confirmation's reading]; the census actions of §10; Main:600 (3) (H2). It changes no category count and no
  physical claim.
- **Decision-ready?** READY for the question, options (a) and (c) and the recommendation; option (b) stays not decision-ready until the destinations of §12.2 are agreed (adopted direction, c.6896890693). Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E20, E21, E22, E23, E29) are all applied in r9 (§22). **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7, AM-5b joined the subset, now 18 (F9), and Q9 was added to the dependencies (F18). In r8 the plain statement and option (b) give the 18 with their arithmetic (5 + 7 + 1 + 1 + 3 = 17, and AM-5b), read from §12.1. Rows: AM-5b, AM-4.2, AM-1.1. Q2(b) is an option only and is not decision-ready until the destinations of §12.2 are agreed. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** AM-16, AM-25, AM-27.1, AM-27.2, AM-29, AM-32, AM-38, AM-5b.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 items 3, 6, 7 and 11. Also §20, T32 (the finite-experiment entry for AM-5b: EF-1 r6 "Partly", this audit "no"; both can stand; no bearing on a class).
- **Basis of the options.** §12.1, §12.2; the 18 RM rows.
- **Status.** Pending.

### Q13. Census
- **Plain statement.** Some changes move or remove sentences that the Lean-to-paper registry points to.
- **Options, each in full.**
  - (a) *One commit.* The single correction carries every registry action of §10 in the same commit (§A.35): family 1's note at SM:643 if P6 is stated; family 33 if Main:157 cites `c4r_implies_pIndivisible`; family 8 if Main:362 cites the cone lemma; under Q2(b), families 6, 19, 21 and 22 made kernel-only and the lost anchors of families 14, 20, 35 and 36 dropped; family 40's phrase anchor, with the guard `R7-RCL`, if Q15 changes Main:638; the notes of families 12, 13, 48 and 49, and of 15 and 53 under Q3(b). Family 34 needs no action while Main:143 stays. AM-5b is in family 1 (anchors at Main:312 and :314) and needs no action while those lines stay. Basis: §10; §A.35.
  - (b) *A separate commit.* The registry changes are made in a commit of their own, after the manuscript change. The census check would fail between the two commits. Basis: §10; §A.35.
- **Recommendation: (a).** Reason: §A.35 makes the registry part of the change; a separate commit would leave
  the census check failing in between.
- **Dependencies.** After Q2, Q3, Q8 and Q15.
- **What it changes.** The registry actions of §10.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E24, E25) are all applied in r9 (§22). **Depends on the pilot:** in part (the family-8 registry action). r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7, AM-5b was added with its census entry unclassified (F9; in r9 the entry is family 1), and option (a) gained family 1's note (F20). Rows: AM-5b, AM-30. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** AM-27.1, AM-27.2, AM-5b.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** §10.
- **Status.** Pending.

### Q14. Records
- **Plain statement.** Three verification records cite A1 as a premise (AM-18 DEPENDENCY-AUDIT.md, AM-26, AM-35).
- **Options, each in full.** The records are those of AM-18 (`DEPENDENCY-AUDIT.md`), AM-26 and AM-35; none was read by the review of r6. None of these files is governed by a receipt, a seal record or the legacy manifest (a search of `verification/receipts/`, `verification/seals/` and `verification/infrastructure/` at `main` for their directories finds nothing), and MR-1's preregistration says of itself that it is "not a native V3 control plane and not an `F` candidate". On that evidence none is a frozen record in the sense of §A.39; all are research or audit records [focused confirmation of r8; a search, not a reading of every receipt].
  - (a) *Correct each by its own route.* Each record is corrected by the route its kind allows: a mutable record in place, a frozen one by a new reviewed round (§A.42 item 6; §A.46 item 4). Basis: rows AM-18, AM-26, AM-35.
  - (b) *Leave them as historical records.* Nothing is changed and nothing is added. Basis: the same rows.
  - (c) *Frozen records unchanged; a mutable note where needed.* The records are left as they stand, as records of what was premised when they were written, and only where a surviving claim cites one is a mutable note added on `main` that names the change. Were any of them frozen, it would be left unchanged for that reason as well. Basis: §A.42 item 6; §A.46 item 4; the same rows.
- **Recommendation: (c).** Reason: none of the three is frozen, so §A.42 item 6 does not decide the matter. They are historical research and audit records, and the Code Review Rules keep such records as they stand ("do not rewrite historical commits or status records merely to make the history agree with the latest result"). §A.46 item 4 asks for a stated status where a surviving claim relies on one, which a mutable note supplies. MR-1 is a live stage-0 preregistration and takes the change in its own next revision if it proceeds.
- **Dependencies.** None.
- **What it changes.** The records of AM-18, AM-26 and AM-35.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E26) are all applied in r9 (§22). **Depends on the pilot:** no. r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: No change in r7 or r8 alters its basis; it is marked so because the basis has had no review (the records of AM-18, AM-26 and AM-35 were not read by the review of r6). Rows: AM-18, AM-26, AM-35, which are records outside the 57. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none among the 57 rows.
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** none.
- **Basis of the options.** AM-18, AM-26, AM-35.
- **Status.** Pending.

### Q12. Order and authorization (§A.45 rule 3)
- **Plain statement.** Which of P1–P16 may start, with which writers and reviewers, and in what order? (EF-1
  r6's question 10, which theorem to check first and which direct proof to attempt first, is the same question for the fixed-horizon rows. Its question 9 asks whether one independent check of its proofs is enough before anything rests on them; no class here rests on any of them.)
- **Options, each in full.** "P" numbers are the proof units of §14. No option grants recovery credit or adopts a premise.
  - (a) *Authorize none yet.* No proof unit starts until both reviews are done and the questions above are answered. Basis: §A.45 rule 3.
  - (b) *A first tranche.* After the two reviews, the units whose proof can be written without an owner answer, and which assert nothing of nature, are authorized first, in two groups. Group 1, no premise beyond those on `main` and no reading: P1 (the §3.2 channel and Born form for a realization's prior; AM-5, AM-2.1); P15 (the characterization theorem's proof uses no `t_R`; AM-20.1); parts (1) and (2) of P9 (AM-31). Group 2, conditional theorems whose statements carry hypotheses that are not all worded on `main`: P5a (the C2 persistence form, for any hidden space carrying a joint law of record and hidden state; AM-21.1, which is NEW for nature); P4 for a measurable `Ω` (the Bell ceiling under hypotheses (i)–(iv), with hypothesis (iii) taken with a coupling graph in the dependency sense, and with measurable response functions; AM-7.2 and AM-7.3, whose class is disputed, §14.1). P4's proof cites the cone in its dependency form (kernel, `iterate_dependsOnlyOn_ball`, `RegionTower.lean:283`, for one alphabet); for site-dependent alphabets it also needs the short embedding step that §14 lists as unproved under P3, which is written with it. The later stages are in the recommendation and in "Changed in r6" below. Basis: §14, column "Gate" (these units have none); §12.3; §14.1.
  - (c) *Impact order.* The units are started in the order of §14's impact column, whatever their gates. Basis: §14.
- **Recommendation: (b), after the two reviews.** First tranche: P1, P5a, P15, P4 for a measurable `Ω` (with
  hypothesis (iii) read as in AM-7.2), and parts (1) and (2) of P9. Then P3 and P16 once Q8 and Q11 are
  answered; part (3) of P9 once Q6 and Q1 are answered; the rest wait on their gates. Of the fixed-horizon
  rows, the cone (AM-7.1) is checked first, since AM-7.2's second route, AM-8's cone step and AM-23.2 use it.
  Reason: every unit of the first tranche can be written and proved without an owner answer and asserts nothing of nature. P1, P15 and parts (1) and (2) of P9 need no premise beyond those on `main` and no reading. P5a and P4 are conditional theorems: each names in its statement hypotheses that are not all worded on `main` (P5a: a joint law of record and hidden state; P4: hypothesis (iii) with a coupling graph in the dependency sense, and measurable response functions), and proving them adopts neither a premise nor a reading. What a proved P5a or P4 counts for is decided elsewhere: P5a's reading for nature at Q11 and Q6 (AM-21.1 is NEW); the class of AM-7.2 and AM-7.3 under the rule for FIRM (§14.1, disputed; on this audit's classification, at Q8). P1, P4, P5a and P15 are inside Main; P9 is in SM (§14). A proof counts for a row only when it has been checked against the properties that row's theorem uses (§14.3).
- **Dependencies.** Last: after every question above.
- **What it changes.** Which proofs start. It grants no recovery credit and adopts nothing. No option names a writer or a reviewer, which the plain statement asks about: under §A.45 rule 3 each unit that starts also needs a designated writer recorded, and that is a separate record.
- **Changed in r6** (6897946443), **corrected in r7** (F2, F4, F6). After the first tranche, the order follows the direct-proof targets of §12.3: first the rows whose route needs K1 alone or K1 with K2 (AM-23.2, a "partly" row; part (3) of AM-31, a replacement part; AM-14 only for a form without GR:132's own hypotheses, since with them it is already direct on `main`, §12.3), then the row whose route needs one named property of K3 and is not already in the first tranche (AM-30, by P6; AM-7.2 and AM-7.3 are served by P4, which is in the first tranche). Each is proved as a conditional theorem with its condition named. For P6 the conditional form (the measure, bijectivity and time-reversal covariance as named hypotheses) is what this stage proves. P10 (AM-33.1) has no direct-proof target in §12.3; its conditional form (injectivity as a named hypothesis) may be written in the same stage. Neither asserts anything of nature (Q5, Q6). AM-22 is not in this stage: no route was found that avoids a shell measure. A closed finite model or an all-time model (K4 (i), K6) is not pursued unless a proof is shown to need one, and P8-M and P12 are not started while their rows are conceded (§12.4). Before any condition is dropped from a statement, the trace that supports dropping it is reviewed. The first tranche is unchanged.
- **Decision-ready?** READY. Focused confirmation of r8: CONFIRMED WITH CORRECTION; its listed corrections (E1, E2, E3, E4, E5, E6, E7) are all applied in r9 (§22). **Depends on the pilot:** in part (the fixed-horizon stage). r8 marked it NEEDS FOCUSED CONFIRMATION, with this entry: Changes that materially alter its basis: in r7 the second stage was rewritten (F2, F4, F6), and AM-7.2, AM-7.3 and AM-21.1 changed class (F5, F10). The first tranche's membership is unchanged. Its reason is restated so that it holds whichever class AM-7.2 and AM-7.3 take, and the later stage no longer lists them (focused confirmation of r8). Rows: AM-7.2, AM-7.3, AM-21.1, AM-22. r8 writes each option out in full with its basis and changes no option, row or recommendation; that text is unreviewed.
- **Unchecked rows it rests on.** none in the first tranche; AM-24 later (P12).
- **Disagreement attached; the reviewer's view (a recommendation, not settled).** §20 items 12 and 13. Also the class of AM-7.2 and AM-7.3, served by P4 (§14.1; §20, "Disagreement with the focused confirmation of r8"); the first tranche is worded to hold under either class.
- **Basis of the options.** §14 and its gate tally; §12.3.
- **Status.** Pending.

## 20. Remaining disagreements

Each entry D1–D25 and T1–T21 gives the two positions as their parties took them, and its last column, "Standing now", gives where the entry stands at the current pin (EF-1 r6) and after the review of r6; where this audit's own position has changed since r6 the cell says so. The reviewer's adjudications are recommendations; none is settled. The eleven trace differences T22–T32, the disagreements with the review of r6 and the disagreement with the focused confirmation of r8 follow in the three subsections at the end of this section.

Every unresolved difference between this audit, the review of r4, EF-1 r4 and the review of EF-1 r3, with
both positions. The review of EF-1 r4 is a further party to several entries, and each such entry names it.
Nothing here is settled by r6; "settles" names where it can be. Identifiers are not reused
or renumbered: D1–D20 are r5's and keep their numbers; D21–D25 and the trace comparison T1–T21 are added by
r6. Where the re-pin to EF-1 r4 changed one side of an r5 entry, the entry says so. "r5" in an entry is a
position r5 took and r6 carries unchanged; "this audit" means the same.

**Disputes with the review of r4, all kept visible:** D1 and D2 (AM-31, part (3)); D3 and D4 (Main:274–278);
D5 (the three counts); D7 (the dependency-graph hypothesis of P4); D16 (Q2); D17 (Q6: (e) or (d)); D18 (four
or five kernel-only families); D19; and D21 (twenty entries where the review listed fourteen). The review of
r4 has not seen r5's position on any of them, and no review of r5 exists.

| # | Subject | One position | The other position | Settles | Standing now |
|---|---|---|---|---|---|
| D1 | Class of AM-31, part (3) | Review of r4: contingent on Q6(d) ("a\* contingent on Q6(d) and Q11 (part 3), else b"), counted among five contingent rows | This audit: the row is FIRM for the theorem as stated (parts (1), (2)), and part (3) is a replacement part, in no class. The premise part (3) needs (a normalized starting law for nature, L9) is not a reading of any text on `main`, as the review itself shows, so it is a named assumption and not a contingent reading. r5 and r6 classed the whole row NEW by part (3). The evidence is agreed; the label and the counts differ | the next review; in substance the owner at Q6(d) | The review of r6 (F7): FIRM by parts (1) and (2), with part (3) a replacement part. This audit agrees on the evidence (SM:1376, :1382; Main:506–512) and applies it. How L9 is treated stays with the owner at Q6(d), (e) |
| D2 | Whether AM-31's part (3) recovers anything | Review of r4: a candidate recovery of the row's C3 content | r5 [IR]: a per-horizon restatement. It bounds a truncation of `I*` by a count that grows with the horizon; the horizon-free bound by `log₂∣C_H∣` is not recovered for an infinite hidden sector, where the stated clause is vacuous | the next review | Agreed with the review of r6 (F7): part (3) is a replacement part, not a recovery |
| D3 | Main:274–278 | r4: part of AM-4.2; under Q2(b) it moves with its paper proof | Review of r4 **[reviewer reading, unresolved]**: a constructed-realization lemma that does not consume A1; it stays in place and joins §6. r5's own check [IR] agrees that the lemma constructs its hidden space, and adds that its sentence on uniform-prior marginals is true of the finite hidden spaces it constructs and is not established on `main` for an infinite carrier (EF-1 r4: N3.2 proves it for the second-order form; (M-full), checked by its review, for the locality class of `main` with finite alphabets; it is false for B1). EF-1 r4 §4.2 is a third position: it traces the lemma's sentence and its Birkhoff–von Neumann step (Main:274–276) inside the §3.2 setup class, which it marks as needing a bijection of a finite product with its uniform state, and does not say whether the lemma consumes A1 | the owner or the next review; either way it can only stay in Main (§12.2) | The review of r6 reads Main:274–278 as A1-free; this audit's check agrees. Kept attributed and unresolved until it is resolved (adopted direction, c.6896890693) |
| D4 | Counts of the Q2-17 subset under Q2(b) | With the reviewer's reading of D3: 7 + 1 + 5 + 1 + 3 | With r4's reading of D3: 8 + 0 + 5 + 1 + 3. (r4's own 7 + 6 + 1 + 3 is withdrawn: AM-34 is a paper proof) | follows D3 | Follows D3; unresolved |
| D5 | The three counts | Review of r4: firm 6, contingent 5, new 8 (also the figures in the #1169 record 6896890693) | This audit, under the one rule of adopted direction c.6898395533: FIRM 4, CONTINGENT 5, NEW 9, replacement candidate 1. The differences from the review of r4 are N-3 (adopted direction, c.6896890693), AM-31 (D1), AM-7.2 and AM-7.3 (D6, D7) and AM-21.1 (D10). r5 and r6 counted 6, 3, 9, 1 | D1; the owner | In dispute with the review of r6, which adjudicates 7, 3, 8, 1 and gives a range of FIRM 5 to 8: the rows are AM-7.2, AM-7.3 and AM-21.1, with both positions in §14.1. The owner |
| D6 | Route for the Bell ceiling | EF-1 r4 N3.6 (unchanged from r3): "The fixed-horizon form appears sufficient for the *dependency* part of the theorem for experiments of finite duration; the audit's proposed restatement P4 would not be needed for that part." | r5: P4 (a measurable `Ω`) first. It uses no finite patch, so it needs neither finite wing regions nor finite support over every branch; the fixed-horizon route needs both (EF-1 r4 N3.6 agrees that the route needs the all-branch form and that "Finiteness of `A`, `B`, `R_A` and `R_B` is a premise here"), and neither route supplies measurement independence. The row's class is set by P4 only: CONTINGENT in this audit, FIRM in r6 and in the review of r6 (§14.1) | the proof of P4, when written and checked | P4 is not premise-free (the review of r6, F10). Undetermined until P4 is written; EF-1 r6's own route for the ceiling is in T23 |
| D7 | Hypotheses of P4 | r4 and the review of r4: P4 adds no premise ("none for P4") | r5 [IR]: P4's proof uses the cone lemma (Main:383–384), so on a carrier of undetermined cardinality hypothesis (iii) must be read with a coupling graph in the dependency sense. r5 and r6 held that, as a property of the class of completions the theorem excludes, that is a hypothesis of the statement, and kept the row FIRM. This audit now classes the row CONTINGENT: with measurable response functions (the review of r6, F10) it is one of two hypotheses that are not on `main` as worded, and whether they count as hypotheses of the statement is an undecided reading (Q8) | the next review | In dispute with the review of r6, which keeps FIRM (the two hypotheses are "hypotheses on the class of completions excluded, not premises about nature"). Undetermined until P4 is written; the owner (Q8) |
| D8 | Standing of a finite visible region with a site-local readout (L8; EF-1 r4's F4) | EF-1 r4 §4.0, changed from r3 as its review asked: "Used on `main` for the spatial results (Main:296; Main:744–746; GR:112); not stated as a separate premise, and finite there only through the finite site set", flagged; its question 5 (a) asks where it should be recorded | r4 and the review of r4: a premise of the spatial constitution, under Q8. r5: a named hypothesis of the statements that use it. If it is an assumption about nature, AM-23.2 is NEW, not CONTINGENT. After the re-pin the texts agree on the evidence; what stays open is where the premise is recorded and whether it counts as an assumption about nature | the owner at Q8 | Open; the owner (Q8). The texts agree on the evidence |
| D9 | Standing of finite support (FS; EF-1 r4's FS-all, F7) | EF-1 r4 N1.5 and §4.0: FS-all is not on `main` as a separate premise, flagged, "a premise to track". r4 adds a per-run form and Lemma K. The review of EF-1 r4 checked both and finds four sentences of r4 that contradict Lemma K (its finding 2): one finite patch for every branch is proved under FS-all, with a bound, or from finite reads on every run, under the lemma's other hypotheses, without one | r4 and the review of r4 did not carry FS. r5: a named hypothesis in the all-branch form wherever a row needs one patch for every branch (§14.3, Table 4). r6: the same, with Lemma K's hypotheses noted as a second set of named hypotheses that would serve; no class rests on the per-run form or on Lemma K. Where FS-all is recorded is an open owner matter (EF-1 r4's question 5 (b), (c)) | the owner at Q8 | Closed between the texts: EF-1 r6 corrects the four sentences (from r5). Where FS-all is recorded stays with the owner (Q8) |
| D10 | Standing of a normalized starting law (L9; EF-1 r4's P1) | EF-1 r4 §4.0, changed from r3 as adopted direction c.6897254631 asked: the probability premise, "not needed for finiteness", "**Flagged** for the infinite case. It asserts no cardinality"; its question 4 asks whether it is acceptable as the premise that supplies probabilities | r5: the same separation; and, separately, for nature's carrier L9 is not on `main`, so a row that needs it for a statement about nature is NEW (AM-21.1) or, in AM-31, has a replacement part (part (3)), and the recommendation at Q6 is (e), not (d). [IR] The same L9 is presupposed by the reading for nature of AM-21.1, which r5 and r6 kept FIRM as a conditional theorem and which this audit now classes NEW, with the conditional theorem available. After the re-pin the premise separation is agreed; the class and the recommendation remain this audit's | the owner at Q6 | Open; the owner (Q6, Q11). The premise separation is agreed between the texts |
| D11 | Example B1 and preservation of the uniform product measure | EF-1 r4 §P.3, changed from r3: B1 "lies outside the locality class of `main`"; inside that class invariance is the proposition (M-full). The review of EF-1 r4 re-derived (M-full) step by step and found it sound, with the scope note that for item (xiii) itself N3.2 already gives invariance and that `main` does not select the wider class as nature's dynamics (its finding 8) | r5: uses neither invariance proof for any class; preservation by the full system and an invariant measure on the description are kept apart (§14.3, Table 3). r6: the same; (M-full) is recorded as checked, no class uses it, and §14.1 shows none would change if it were used. EF-1 r4, its review and this audit agree on B1 and on (M-full). What stays open is whether one independent check is enough for (M-full) to support a recovery classification, which the review leaves to the owner (its finding 11) | the owner | Open; the owner (EF-1 r6's question 9). No class uses (M-full) |
| D12 | "Properties the proof uses" | EF-1 r4 §4.2: every class redone from a trace of its proof on `main`; "**Substantially revised in r4 and unreviewed**". The review of EF-1 r4 has since retraced seventeen classes and found r4's entries complete in fifteen, with requirements missing in the readback class and the one-step coherence class, and one class absent (its section 4; findings 4, 5) | r5: its own traces (§14.3), made before EF-1 r4 existed and carried unchanged in r6. The two sets of traces differ in the places listed under T1–T21 below; r6 adopts neither and gives, for each difference, the lines it read at `main` | the next review of this audit | EF-1 r6 completes the two rows and adds the row for the §3.4 obstructions (from r5; those cells have had no check). Its second table is compared with this audit in T22–T32 |
| D13 | Necessity of the finite-influence condition for one finite model | EF-1 r4 N2.1 (Proposition N, checked by the review of EF-1 r4): with finite alphabets, a finite influence set is necessary as well as sufficient for one finite autonomous model that reproduces the record from every initial configuration; "not necessary for one fixed initial law". The review of EF-1 r4 (finding 3; its own argument, unchecked): that last clause is exact only for a law that misses some finite pattern; for a law that charges every finite pattern, the uniform product prior included, necessity holds as well | r5 states F-one as not established and uses neither direction; r6 the same | EF-1 r6; an independent check of the review's refinement | The one-law refinement is adopted in EF-1 r6 (N2.1) and has one independent check, the recheck of EF-1 r5, under its stated hypotheses. This audit uses neither direction |
| D14 | Main:216's first-order clause | Review of EF-1 r2: a fixed-horizon statement. Review of EF-1 r4 (finding 7): keep "undetermined" for the estimate, and call the class "mixed", because the cardinality clause of Main:216 is not a fixed-horizon statement in the native class | EF-1 r4 N3.5, new in r4: the clause is traced to the estimate of Main:340, a short-time statement with nothing uniform in the horizon, whose written derivation runs inside the §3.2 setup with a finite hidden space; "the weakest sufficient form for this class is undetermined". r5: undetermined as well (§14.3, Table 2), and A1-test candidate 2's accessibility is listed as contested (§11). After the re-pin EF-1 r4 and this audit agree; the reading of the review of EF-1 r2 is the other position | a derivation of the estimate with a patch in place of the finite hidden space | Closed between the texts: EF-1 r6's form is "mixed", as this audit's (§14.3, Table 2, AM-6.2). The estimate's window entry differs (T27) |
| D15 | Two lists of owner questions | This audit: 15 | EF-1 r6: eleven of its own. Its questions 5 (where a finite visible region, finite supports over every branch and finite wing regions are recorded), 9 (whether one independent check of its proofs is enough before anything rests on them: the review of EF-1 r4 for four of them, the recheck of EF-1 r5 for the closure characterization and the one-law refinement) and 11 (the finite-hidden-memory draft) have no counterpart among the 15. This audit attaches question 5 to Q8 as a sub-item, names question 9 under Q12, and does not change the count (§19) | the owner | No conflict. EF-1 r6 keeps eleven questions; its 9 now asks whether one independent check is enough, and its 10 adds which direct proof to attempt first (§19, concordance) |
| D16 | Recommendation on Q2 | r4: (a), labelled a recommendation only | Review of r4: no recommendation; Q2(b) is undecided. r5: no choice until the destinations of §12.2 are agreed; if one is wanted before that, (a) as the smaller change | the owner | Unchanged: no choice on Q2; the review of r6 makes none |
| D17 | Recommendation on Q6 | r4, accepted by the review of r4: (a) together with (d) | r5: (a) together with (e), a normalized starting law carried as a named hypothesis where it enters; (d) would posit it of nature and is NEW (D1, D10) | the owner at Q6 | The review of r6 recommends (e); this audit (a) with (e). Both are recommendations; option (e) is not endorsed (adopted direction, c.6898395533) |
| D18 | Census families made kernel-only under Q2(b) | r4 and the review of r4: five (6, 19, 21, 22, 40) | r5: four, because §12.2 finds no destination outside Main for AM-9.1, so family 40 keeps its anchors | follows Q2 and §12.2 | Four families; the review of r6 agrees |
| D19 | Source of the C3 clause's bound | Review of r4: "an instance of Main:608 (c)" | r5 [IR]: Main:512's corollary for `I*`, with Main:608 (c) the one-step form and `fullFutureIstar_le` a kernel-only witness for a finite hidden space | the next review | The review of r6: Main:506–510 with Main:512. No class rests on it |
| D20 | Labels | EF-1 r4 still cites this audit at its r2, "for labels only": its N3.11 and §4.2 list three A1-test candidates, and its question 6 asks whether the third should be removed | r5 lists double stochasticity as not a candidate (§11 item 3). The substance agrees: EF-1 r4 N3.11 concludes that none of the three becomes a test of A1 | a later EF-1 revision; the re-pin does not settle it | Labels only; no difference of substance. EF-1 r6 still cites this audit at its r2 and lists three candidates |
| D21 | How many disagreements remain | Review of r4, section C: fourteen (its D1–D14) | r5: twenty (D1–D20). Of the review's fourteen, six are closed: five by applying its changes (its D2, AM-34; D5, N-3; D9, the Bell patch; D10, Main:638; D13, the order of the questions) and one in EF-1 (its D12, the wording of the all-time sentence, which EF-1 r4 has as the #1169 record has it). Eight are carried (as D1, D3, D4, D6, D10, D15, D16 and D20 here). The other twelve (D2, D5, D7, D8, D9, D11, D12, D13, D14, D17, D18, D19) were opened by r5's own positions or taken from EF-1 r3 and its review. r6 keeps all twenty and adds D21–D25 and T1–T21 | the next review | Not checked by the review of r6 |
| D22 | A measure on the description: what is true, and how it is worded | EF-1 r4 §P.4: "(M-full) does not imply (M-desc)"; (M-desc) is not defined for the description as given, "fails for the closures the description determines", and holds only for closures that add structure by choice. r5: "a separate open question for every row" | Review of EF-1 r4 (finding 1; its section 7, item 1): the case proofs are right and those two sentences are wrong as written. With a uniform product prior, full-system invariance implies that a measure-preserving bijection of the patch data reproducing the record exists (its Lemma C), and for a second-order rule every fixed-boundary closure is one (its Lemma C′); both lemmas are its own and unchecked. All agree that the description has no map of its own, that any such map is a choice valid on the window only, and that no class gains recovery credit. Adopted direction (c.6897859755): "Failure of automatic inheritance does not imply that no suitable finite closed model exists." r6: as first written it followed EF-1 r4's two sentences; that wording is withdrawn. r6 now says that the property is not inherited automatically, that the existence of a suitable closed model is a separate and unchecked question, and, row by row, whether the proof's requirements are confined to the window (§14.3, Table 5) | an independent check of Lemmas C and C′; EF-1 r6 | Closed in substance: EF-1 r6 withdraws both sentences and states the description as defined (M-desc-own) and a chosen closure (M-desc-some) apart (from r5). Lemma C, Corollary C1 and Lemma C′ have one independent check, the recheck of EF-1 r5; whether a closure preserves what a given result needs is unproved |
| D23 | Which results are fixed-horizon candidates | EF-1 r4 §4.2 and its question 10: five classes "for which the fixed-horizon form looks sufficient", each labelled a recovery candidate: the causal cone, the dependency part of the Bell ceiling, the baseline matrices under a uniform hidden prior, the deep-sector comparison (GR:112 (a)), and the in-window form of overlap and return | This audit (§14.1): seven rows, AM-7.1, AM-7.2, AM-7.3, AM-23.2, AM-31, N-3 and AM-36. Two of EF-1 r4's five are among them (the cone, the Bell ceiling). The other three are rows with no recovery class here, because nothing of theirs is to be recovered: the baseline matrices (AM-4.2, RM: a definition on a finite realization, its per-horizon form a remark); the deep-sector comparison (AM-12 and AM-14, RU: GR:132 already states it for an infinite deep sector); overlap and return (AM-1.2, RD: A1 does not enter it on `main`, as EF-1 r4 N3.1 also says). Five of this audit's seven (AM-7.3, AM-23.2, AM-31, N-3, AM-36) have no class in EF-1 r4. The population of 19 and the counts do not change either way | the next review; the owner, if the three are to be counted as candidates | The review of r6 takes this audit's seven rows as the right population; EF-1 r6 keeps its five "recovery candidate" labels. No class rests on either list |
| D24 | The one-step coherence results of §3.2 (Main:292–322) | EF-1 r4 §4.2: a result class of its own, "Not examined before r4"; F-each for one step, unchecked; it uses a uniform prior on the hidden boundary sites (D2), uncorrelated with the visible input (D4) | This audit: row AM-5b (RM; unreviewed), added on finding F9 of the review of r6; population 57. r6 had no row for it: the row list is r9 §7's; AM-5 covers the §3.2 setup at Main:266–288 and its downstream list does not include Main:292–322; Main:60 names "the finite hidden space of the §3.2 setup" among the uses of the finite representative and does not name these results separately. r6 read the passage at `main`: it takes "the substratum of §1.2 on a lattice $\Lambda$" (Main:292), its hypothesis is "the hidden sector initially uncorrelated and maximally mixed" (Main:316), and the criterion has no dependence on the size of the hidden sector, "since the coupling reads only the boundary" (Main:322). The review of EF-1 r4 (its section 4) adds that the channel of these results is the §3.2 channel, with a finite hidden space, `ρ_H = I_m/m` and a partial trace (Main:280–282), which r6 confirmed at `main`. r6 [IR]: on that evidence the passage uses the finite hidden space of the §3.2 setup and belongs among AM-5's downstream sites, which is a site added to an existing row and not a new row; r6 does not add it. The row count stays 56 | the row-list recipe (r9 §7), or the next review | Answered by row AM-5b. EF-1 r6 gives the class as Main:292–324, through Main:280–282, :310 and :324 |
| D25 | Source of the sentence "a recovery candidate is not a recovered result" | EF-1 r4 (header; §12, item 6): a rule of its brief, "not found in the ten comments read", so "used here as a rule and not attributed to a comment"; "It may be owner wording given in the session and not recorded" | This round's brief: owner, in session on 2026-11-15, not separately recorded. r6 searched the 267 comments on #1169 that existed when it first read the issue and found the sentence in none. It has since been recorded, in 6897859755, as a sentence from earlier in the same session, and r6 cites that record. The difference is now only that EF-1 r4 predates the record | closed by the record; EF-1 r6 can cite it | Closed by the record (6897859755); EF-1 r6 cites it |

Population of this table: 25 entries, D1 to D25.

**Agreed in r5 and no longer open:** AM-34 is a paper proof (review C1); N-3 is a replacement candidate (review
C7; adopted direction, c.6896890693); the settings condition and the enlarged patch (review C8); the order of the questions (review C11);
family 34 needs no registry action (review C13.2). **Settled in earlier rounds and not reopened:** the Main:332
adjudication; r2's disputes of r1's F1, F5 and F17. **Narrowed by the re-pin, not closed:** D8, D10, D11 and
D14, where EF-1 r4 moved to the position its review or the adopted directions gave; each entry says what remains.

**Trace comparison: §14.3's proof-requirement traces against EF-1 r4 §4.2, class by class.** §14.3's traces
were made for r5 from the proofs on `main`, before EF-1 r4 existed; EF-1 r4's are its own, also from the
proofs; its review retraced seventeen of its classes and marks fifteen "Complete". Every difference found is
listed. r6 adopts neither side: §14.3's cells are left
as r5 wrote them, with a pointer to the entry here, and "checked" says what r6 read at `main` (`bf89ba13`).
"Bearing" is the effect on a recovery class or count if EF-1 r4's entry is right.

| # | EF-1 §4.2 class | Row here | EF-1 §4.2 (its entry as first compared, at r4; a mark of r4 that EF-1 r6 words differently is given in r6's words) | This audit (§14.3) | Difference, and what r6 checked at `main` | Bearing | Standing now |
|---|---|---|---|---|---|---|---|
| T1 | Finite-horizon equivalence and dilations (Main:516–522, :546–552) | §6 (not an A1 consumer; no trace in §14.3) | Traced: a finite horizon, rational kernels or the response-table form, a constructed finite hidden space, an injective step extended to a permutation, a structured prior whose independence from the visible initial state "is not formalized" (Main:520). F-each; "Nothing to transfer"; A1-free | Listed in §6 as not consuming A1; the unformalized root-independence clause is noted under AM-1.1 from the census family 1 note | No conflict. EF-1 r4 has a trace where this audit has none, because the row is not an EF-1 route | none | No difference |
| T2 | Hidden-memory theorem, capacity floor, canonical quotient (Main:506–512, :602–620) | §6; AM-31, part (2) | Traced at Main:602, :610, :508, :510, :97, :614, :620. F-each: "statements about every finite faithful realization at a horizon"; A1-free | AM-31 part (2): Main:512's corollary for `I*`, Main:608 (c) its one-step form, proof at Main:610 (c); kernel-only witness `fullFutureIstar_le` | The same content with different lines cited. Checked: Main:506–510 is the bound and its proof, Main:512 the corollary for `I*`, Main:608 (c) the capacity floor, Main:610 its proof; both sets of citations are right. EF-1 r4 has no entry for the truncated bound of AM-31 part (3) | none | No difference |
| T3 | §3.3 causal cone (Main:362) | AM-7.1 | Intervention clause: "PM-I: one intervention with a declared support (all-branch, single step)"; carried "for an intervention with a support valid in every state" | Table 4: "neither" form, because the statement is pointwise and uses no finite patch; it needs the intervention's support, taken over every state, to lie in `A` | A label only. Both require a support valid in every state, and neither requires a finite patch for the dependency (Lemma PM-I (a) has no finiteness hypothesis). The traces otherwise agree, including that Main:362's first step fails on an infinite carrier | none (CONTINGENT by L1) | A label only |
| T4 | Bell ceiling (Main:364–389) | AM-7.2 | The same hypotheses and proof steps, with "(i) determinism" named and the pointwise bound over sixteen response tables followed by the average (Main:388–389). All-branch form. "Recovery candidate for the dependency part" | Table 1: the same lines (Main:364–375, :378–379, :383–388, :389). Candidate for the dependency part only; the row's class (CONTINGENT) is set by P4 | The traces agree. The difference is the route (D6) | none | No difference in the trace; the route and class are D6, D7 |
| T5 | Baseline `T_ij` with uniform hidden prior (Main:115–117, :129; Main:58; Main:266) | AM-4.2 | Main:115, :117, :129; the prior is the uniform probability on the product carrier of a bijection, distinct from the counting probability on an eventual image (Main:58, :266); the preimage count behind double stochasticity (Main:60, :274). F-each; double stochasticity needs invariance on the full system (D3); no property of nature's own map beyond the window; "Recovery candidate" | Table 2: Main:113, :115, :129. Table 3: Main:115. F-each as a remark; RM | (i) EF-1 r4 cites four sites that this audit's tables do not: Main:117 (the `k`-step matrix, "by applying $\varphi^k$"), Main:58 and Main:266 (the two priors), and Main:60 with Main:274 (the preimage count, which this audit has under AM-3.2). Checked: each is as EF-1 r4 says. (ii) The label "recovery candidate" (D23) | none (the row has no class) | EF-1's extra sites are as cited; no difference of form |
| T6 | Lemma 3 counting and maximal-entropy selection (Main:54, :58, :60) | AM-4.1, AM-4.3 | Adds Main:60: "on the orbit of the actual microstate, the uniform measure is the unique $\varphi$-invariant measure". "carrier finite"; needs the invariant measures of nature's own map on a finite set, and its orbits | Main:54 only; "a finite carrier" | EF-1 r4 has one more clause; checked, as quoted. The forms agree | none (RM; RX) | Not checked by the review of r6; the forms agree |
| T7 | Bijectivity (Main:60, :724) | AM-3.2 | Adds: the two prongs; "On a finite set, injectivity implies surjectivity"; the counting measure on the eventual image, which "need not reproduce the uniform-prior statistics" (Main:60); ledger item (iii)'s scope clause (Main:724). "carrier finite"; needs nature's own map on a finite set, with its eventual image and the step from injective to surjective | §14.3: the map on a finite set, its eventual image and `f^L = id` on it (Main:60); the preimage count (Main:60). The surjectivity step and ledger item (iii) are in the row's own section (§2, AM-3) | EF-1 r4 has the clause on the measure on the eventual image, which this audit's tables lack; checked, as quoted. The forms agree | none (RX) | EF-1's extra sites are as cited; the statistical prong is T24 |
| T8 | Recurrence-scale P-indivisibility, counting form (Main:113–129) | AM-1.1 (with AM-1.3b, AM-2.2) | Main:113 (at least two visible states), :115, :129, :119 (only one direction of the total-variation statement is used), :121, :123–125. Form "F-one, with a counting prior": an all-horizon model does not supply the counting prior (its §P.5). Needs the return `φ^N = id` of nature's own bijection, with its counting measure | Main:121 and :137; the strict contraction of Main:123–127 carried; Table 3: Main:115, :129, :135. Form: "F-one with an exact return, or a finite carrier" | (i) EF-1 r4 cites Main:113 and Main:119, which this audit's tables do not; checked, as cited. (ii) Form: EF-1 r4 holds that F-one is not enough for the counting form, because `T` is defined by a count over the hidden space (Main:115) and an all-horizon model need not have a uniform prior or a product carrier; this audit's cell names F-one with an exact return and does not mention the prior. r6 [IR]: Main:115 and Main:129 ("under the uniform hidden prior that defines $T$") support EF-1 r4's refinement for the counting form; this audit's "F-one with an exact return" fits the return of the rooted maps under a shared prior (Main:135–137), which is T9 | none (RM; RX) | EF-1's refinement is taken for the counting form (the review of r6, F14): §14.3's form cell for AM-1.1 says so |
| T9 | History readback with finite recurrence; overlap and return (Main:131–143) | §6 (Main:131–133); AM-1.1 (Main:135–139); AM-1.2 (Main:141–143) | One class: the stochastic-inverse lemma (Main:131–133); a bijection of order `L`, a prior shared by every root, root and hidden state drawn independently (Main:135); `Γ_L = I`, every row kept (Main:137); overlap and return for any shared prior (Main:141–143). The return at the order `L`: F-one. Overlap and return with a return inside the window: F-each, "a recovery candidate" | Three places: Main:131–133 in §6 (uses only Lemma 1); Main:135–139 in AM-1.1 (RM; not carried, Main:137; Table 3, Main:135); Main:141–143 as AM-1.2 (RD; A1 does not enter; no trace in §14.3, since it is not an EF-1 route) | Agreement on what is carried (the in-window form) and what is not (the return at the order `L`). The differences are the grouping and the label "recovery candidate" for a theorem into which A1 does not enter on `main` (D23) | none | Grouping only. EF-1 r6 adds the hypothesis and range of Main:135 and the paper-proved steps of Main:137 (from r5) |
| T10 | §3.2 CP-indivisibility (Main:326–332) | AM-2.1, AM-2.2 | Assessed on the patch description: the permutation unitary is not defined for the description as given; a chosen closure supplies one for itself on the window; its input needs the return of nature's own bijection and is F-one; "Not carried by F-each" | AM-2.1: RC by P1, FIRM, with no EF-1 route. P1 works on a constructed finite realization with a root-independent prior, which has a permutation unitary by construction, and lands RM. AM-2.2 (nature's channel): RX | Different objects: EF-1 r4's patch description (α) and its constructed realization (β). The two verdicts are compatible; EF-1 r4's is no objection to P1, and this audit does not claim that the patch description carries the theorem | none (FIRM without EF-1) | Different objects, compatible: EF-1 assesses the patch description, this audit a constructed realization (T25) |
| T11 | §3.2 finite hidden space, channel, Born form, reverse direction (Main:266–288) | AM-5; Main:274–278 (D3) | Form "undetermined" on the patch; needs a bijection of a finite product with its uniform hidden state, for one step, not defined for the description as given; a reduced channel exists through the stage formula by steps not written out | AM-5: RC by P1, FIRM, with no EF-1 route (as T10), landing RU. Main:274–278: D3 | As T10. In addition EF-1 r4 places the reverse-direction lemma's steps (Main:274–276) in this class (D3), and its review notes that a window-valid closure would be an object to which the setup applies on the window (D22) | none | Different objects, compatible (T26) |
| T12 | §3.2 one-step coherence results (Main:292–322) | none | A class, F-each for one step, unchecked | row AM-5b (RM; unreviewed), added on D24 | none remaining on coverage; the window entries agree (§14.3, Table 5) | none on a class | Closed: row AM-5b |
| T13 | §3.4 all-time periodicity of a single realization (Main:638) | AM-9.1, AM-9.2 | F-one; needs the order `L` of nature's own bijection; not carried | F-one; not carried | none | none | No difference |
| T14 | Corner occupancy (Main:216, with Main:340 and Main:272) | AM-6.2 | Adds Main:272 (the continuous interpolation, "chosen rather than derived") and the dependence of Main:340's estimate on the §3.2 setup with `ρ_H = I_m/m`. form "mixed" (r4: "undetermined"); through the §3.2 setup, as that row | Table 2: Main:216 and five items of Main:340; "Not determined". Table 3: a uniform product prior in the torus comparison | The forms agree. EF-1 r4 has Main:272 and the dependence on the setup, which this audit's tables lack; checked, Main:272 as quoted. This audit calls Main:340 a continuous-time estimate; EF-1 r4 calls it a short-time statement for `t` of order `τ_S`; both describe the same passage | none (RX) | The forms agree ("mixed"); the estimate's window entry is T27 |
| T15 | Deep-sector gauge (Main:60; GR:112, :124–126, :132) | AM-12, AM-14 | "GR:112 (a)'s proof uses the cone and the uniform prior only (GR:124); (b) uses injectivity and H-BD (GR:126)". F-each for (a), given equal patch marginals (D1); "Recovery candidate for (a)" | Table 2 (AM-14): GR:112, :132 and :134 traced; the lemma's proof: (a) GR:124, the cone and the uniform prior only; (b) GR:126, injectivity of `φ` and H-BD. Table 5: GR:112 (b) "no". RU; recovery not needed. (r6's cell said the proof was not traced, with a wrong line, GR:114) | (i) A line error in this audit: checked, GR:114 is the displayed formula of the lemma's statement, and its proof is at GR:124 (part (a)) and GR:126 (part (b)). (ii) EF-1 r4 has traced that proof. Checked: GR:124 argues that "after $n$ updates each visible component depends only on initial components in $B_{G_\varphi}(V, n)$" and then uses the uniform prior; GR:126 uses that "injectivity of $\varphi$ makes their $D$ components at step $s$ distinct" and H-BD. The lines support EF-1 r4's entry. (iii) The label (D23) | none (RU) | EF-1 was right; corrected in this audit (the review of r6, F11): §14.3, Table 2 and Table 5 (T28) |
| T16 | Energy shells (GR:58, :68–70) | AM-22; AM-36 (U1) | Adds GR:68 (a time-reversal involution; coarse states that are time-reversal even) and GR:58's condition "If the boundary interaction is negligible at the shell scale". "carrier finite"; needs an invariant shell measure of nature's own bijection of a finite carrier (D8) | §14.3 and P7: GR:58, GR:68 and GR:70, with GR:68's condition that the coarse states are time-reversal even (r6's tables lacked GR:68) | EF-1 r4 has GR:68, which this audit's tables lack. Checked: the relation reduces to `N_ij = N_ji` "only when the coarse states are time-reversal even". r6 [IR]: P7's GR:70 step would carry that condition as well. The forms agree | none (NEW) | EF-1 was right; corrected in this audit (F11 (vi), F4): GR:68's condition is carried, and AM-22 has no direct route that avoids shell counting (T29) |
| T17 | Substratum Theorem 23 (Sub:123–195) | AM-11, AM-24 | Stage 1: A1 among the inputs (Sub:123); the output triple (Sub:125), obtained as a constructed realization; and a recurrence-cycle statement on a fixed finite representative (Sub:137). Stage 2 (a): "a finite periodic lattice" from A4 (Sub:98, :157); (f): reciprocal transition counts (Sub:167); (b)–(e) not traced. Stage 3: the gap equation under H-slope (Sub:181), with the shell counting of GR:58–70. Form "mixed": the constructed realization F-each; the recurrence-cycle clause F-one; the lattice, the counts and the shells "carrier finite"; the SM theorems undetermined | Table 2: Sub:125; "Stages 2–3 are **not traced here**"; F-each for Stage 1's constructed realization; its recurrence-cycle sentence (Sub:137) is not carried and is restated or dropped as AM-1.3b; the rest undetermined. P12: "Stages 2–3 untraced, possibly F-one". AM-11 item 1 lists Sub:137, Sub:157 and Sub:167 (r6's cell read "F-each for Stage 1") | EF-1 r4 traced more, and one item touches Stage 1. Checked: Sub:137 says Main §2.3 "proves that on a fixed finite representative a non-permutation rooted map, which C4 readback supplies, forces indivisibility somewhere in the recurrence cycle". That is AM-1.1's content inside Stage 1's derivation, which a fixed-horizon form does not carry, so "F-each for Stage 1" covers the constructed realization only. Sub:157 ("Within A4's assumed periodic-lattice class"), Sub:167 and Sub:181 are as EF-1 r4 cites them. r6 [IR]: P12 would have to restate or drop that sentence as AM-1.1 and AM-1.3b do; Stage 2 (a) meets A4's wording, already noted in §15 | none: AM-11 and AM-24 are NEW through P5b, P6 and P7 | EF-1 was right; corrected in this audit (F11 (iii)–(v)): AM-11 item 1, Table 2, P12 and §15 (T30) |
| T18 | §4.6 (Main:742–758) | AM-8 | Adds Main:754 (the fast-bath erasure lemma "under its uniform-erosion hypothesis") and Main:758 (the exact compressions "need not equal" the iterated one-step compression). "carrier finite (cone step: F-each)"; the Koopman statements need the spectrum and recurrence of nature's own permutation, with an invariant reference measure on the full system for the compression (D2, D3) | Table 2: Main:742, :744, :746, :750, :752, :756, :758; the row's own section has the compressions as open at Main:758 (ii). Carrier finite; cone step F-each | The forms agree. EF-1 r4 has Main:754's hypothesis, which this audit's table lacks. Checked: "by the fast-bath erasure lemma of §2.3, under its uniform-erosion hypothesis" (Main:754); "need not equal" (Main:758). r6 [IR]: P8-M's anti-Boltzmann-brain corollary carries that hypothesis | none (NEW) | The forms agree; the window entries are T31 |
| T19 | A1-test candidates 1–3 (audit §11) | §11; the remark under AM-9 | Three candidates, taken from this audit's r2. Candidate 1's fixed-horizon count is the number of data on the autonomous patch `U_n` (its N3.11). "Every other class is autonomous" (other than the Bell ceiling and the cone) | Two candidates; double stochasticity is listed as not a candidate (§11 item 3). The per-horizon count is on the enlarged patch, with finite support in the all-branch form, because a prepare-and-measure behaviour ranges over preparations and measurements (review C8) | (i) D20. (ii) The patch: EF-1 r4 counts on the autonomous patch, this audit on the enlarged one. With no intervention after time 0 the two coincide (`E_n = U_n`, EF-1 r4 N1.5); with preparations or measurements applied later they do not | none (a remark; no class) | Not checked by the review of r6 |
| T20 | Main:638 open question (a) | Q15; AM-9.1 | F-one; a candidate answer for existence, without inputs; an owner question | the same (Q15) | none | none | No difference |
| T21 | none: the §3.4 obstructions for a fixed finite realization (Main:486, :556–558, :562) | AM-9.1, AM-9.2 | No class. The review of EF-1 r4 (finding 4) notes that Main:60 names these among the consumers of the finite representative and asks EF-1 for a row: one fixed finite carrier serving every experiment, form F-one, not carried by F-each, kept as mathematics about finite models | AM-9.1 (RM) and AM-9.2 (RX, an A1-test candidate): F-one; not carried | The class is missing from EF-1 r4, not from this audit. The review's description agrees with AM-9's treatment | none | Closed: EF-1 r6 has the row (from r5) and it agrees with AM-9 |

Population of this table: 21 entries, T1 to T21.

**Rows of §14.3 with no class in EF-1 r4 §4.2.** AM-7.3 (Main:414; EF-1 r4's Bell class is Main:364–389), AM-23.2,
AM-31 part (3), N-3, AM-36, AM-4.4, AM-21.2, AM-30, AM-33.2 and N-2. No comparison can be made for them; their
forms and requirements remain this audit's own reading [IR], which no review of EF-1 has checked.

**What the comparison changes.** No class and no count. It finds one wrong line citation and one incomplete
trace in this audit (T15 (i); T17), seven places where EF-1 r4 cites lines that this audit's tables lack (T5,
T6, T7, T8, T14, T16, T18), three differences of label or grouping (T3, T9, T19), two places where the two
texts assess different objects (T10, T11), one class with no row here (T12) and one row with no class there
(T21). T1, T2, T4, T13 and T20 show no difference of substance. The review of EF-1 r4 marks EF-1 r4's
entries "Complete" for the classes of T5 to T8 and T14 to T18, which supports EF-1 r4's line citations
there; for T9 it adds requirements that EF-1 r4 lacks (the hypothesis and range of Main:135; three steps of
Main:137 proved on paper, which this audit's AM-1 section already notes). Where a cell above reports EF-1
r4's marking "needs (M-desc)", that review asks for the marking to be replaced by the requirement itself
(its finding 1); this audit's corresponding entries are in §14.3, Table 5.


### T22–T32: differences between this audit and the second §4.2 table of EF-1 r6

None bears on a class. "Side" is the reviewer's reading of the evidence, a recommendation.

| # | Row | EF-1 r6 | This audit | Evidence at `main`; side |
|---|---|---|---|---|
| T22 | AM-7.1 | finite-experiment "yes" | "partly": observable only with L10 | Main:414 ("is not derived here"); this audit |
| T23 | AM-7.2 | direct proof needs finite `A`, `B`, `R_A`, `R_B` | P4, with no finite regions | undetermined until P4 is written (F10) |
| T24 | AM-3.2 | "partly": the statistical prong is a window statement | "no" | Main:60; EF-1, for that prong only |
| T25 | AM-2.1 | window "mixed"; target needs claim 4 or the channel form of N1.7 | window "yes [IR]"; a constructed realization | a labelling difference, removed by K4 (ii) (F8) |
| T26 | AM-5 | "partly": the channel is a representation | "yes" | Main:286–288 not read by the review; undetermined |
| T27 | AM-6.2 | the estimate: "yes as far as traced" | the estimate: "undetermined" | Main:340; undetermined |
| T28 | AM-14 | GR:112 (b): "no" | "no" (r6: "undetermined") | GR:126; EF-1; no difference remains |
| T29 | AM-22 | no target named | no route that avoids a shell measure (r6: a target with a route) | GR:58, :68; EF-1; no difference remains |
| T30 | AM-11, AM-30 | "undetermined"; reciprocal counts "no" | AM-11 "partly"; AM-30 window "yes [IR]" | the count form is a whole-carrier statement, the matrix form a window statement; both can stand |
| T31 | AM-8 | "partly" (the cone step) | "no"; the inequality "undetermined" | Main:752; both can stand |
| T32 | AM-5b | finite-experiment "Partly": a direct proof for one step of the displayed update | "no": a property of a model's one-step channel | Main:316, :324; both can stand; no bearing on a class |

Population of this table: 11 entries, T22 to T32.

### Disagreements with the review of r6

| # | Subject | r6 | Review of r6 (a recommendation) | r7's view, and what r7 did |
|---|---|---|---|---|
| 1 | AM-31 | NEW by part (3); 6, 3, 9, 1 | FIRM by parts (1), (2); part (3) a replacement part; 7, 3, 8, 1 | agrees on the evidence (SM:1376, :1382; Main:506–512); applied |
| 2 | The rule for FIRM | AM-21.1 FIRM; AM-4.4, AM-31 NEW | two rules were in use; range FIRM 5 to 8; owner to choose | one rule was given after the review (adopted direction, c.6898395533); under it r7 counts 4, 5, 9, 1. **Kept as a disagreement:** r7 classes AM-7.2 and AM-7.3 CONTINGENT and AM-21.1 NEW; the review's figure 7, 3, 8, 1 keeps AM-7.2 and AM-7.3 FIRM. For AM-21.1 the review gives FIRM by the conditional theorem and NEW by its own proposed rule of application (its F5), so on that rule it agrees with r7. Under the review's F5 rule and F7 together the counts are 6, 3, 9, 1, and the rows in dispute are AM-7.2 and AM-7.3 only |
| 3 | Main:274–278 | part of AM-4.2 on r4's reading; unresolved | A1-free; stays | r7's check agrees with the reviewer; kept attributed until the owner resolves it |
| 4 | Q6: (e) or (d) | (a) with (e) | (e) | (a) with (e), as a recommendation; the owner has not endorsed (e) |
| 5 | The Bell ceiling | P4 first; FIRM | P4 is the weaker route in finiteness and is not premise-free | agrees; r7 goes further and classes the row CONTINGENT |
| 6 | Kernel-only families under Q2(b) | four | four | four |
| 7 | Main:290–324 | a downstream site of AM-5; 56 rows | a disposition is missing; a separate row is the consistent treatment | row AM-5b added; population 57 (adopted direction, c.6898395533) |
| 8 | Where L8, FS-all and L9 are recorded | named hypotheses | owner (Q8, Q6); if assumptions about nature, AM-23.2 is NEW | owner |
| 9 | One check of (M-full) | owner | owner | owner; no class uses it |
| 10 | Fixed-horizon candidates | seven rows | r6's population is the right one | unchanged |
| 11 | Q2 | no choice | no choice | no choice |
| 12 | AM-22's direct route | a route avoiding shell counting | none; the weights come from shell counting | agrees after reading GR:58 and GR:68; applied |
| 13 | AM-23.2, AM-21.1 as observable conclusions | "yes", "partly" | "partly", "no" | agrees; applied |
| 14 | Removed rows in the concession counts | counted as conditional | a separate line | agrees; applied |
| 15 | The constructed realization | outside K4 | inside the fourth claim of the adopted table | agrees; K4 (i) and K4 (ii) |
| 16 | Window entries T24, T26, T27, T30, T31 | as r6 | none bears on a class; T26, T27 undetermined | both positions kept |

Population of this table: 16 items, the remaining disagreements listed by the review of r6 (its section 11).

### Disagreement with the focused confirmation of r8

Added in r9. The rule for FIRM is quoted once, in §0; the two tests are named in §14.1.

| # | Subject | This audit (unchanged in r9) | Focused confirmation of r8 (a recommendation) | Standing |
|---|---|---|---|---|
| 1 | The class of AM-7.2 and AM-7.3 under the rule for FIRM | CONTINGENT, both; counts 4, 5, 9, 1. Test applied: nothing further needed of nature, and every hypothesis the restated statement carries worded on `main` | FIRM, both, with the scope of the excluded class stated; AM-21.1 NEW, as this audit; counts 6, 3, 9, 1. Test applied: nothing further needed of nature; the worded-on-`main` test is not applied to a hypothesis that only narrows the class a no-go excludes, which it does not count as a premise required by the route | not settled; the owner decides, on the rule itself. Range for FIRM: 4 to 6. Both positions in full: §14.1 |

Population of this table: 1 item. Every other correction of the focused confirmation is applied in r9 (§22). Its entry for AM-5b against EF-1 r6 is T32 above.

## 21. Limits on review coverage

Adopted direction (c.6898395533): “the audit review samples the new columns, so its verdict should identify which rows were checked and which remain unchecked. "Fit for your decisions" need not mean every recovery route has been verified.”

- **Rows.** Population 57. The review of r6 compared 46 rows with the statement and proof text at `main`. Not checked, 11: AM-10, AM-16, AM-19 (statement only), AM-24, AM-25, AM-27.1, AM-27.2, AM-29, AM-32, AM-38, and AM-5b (added after the review). 46 + 11 = 57. A check was a reading of the cited text, not a re-derivation.
- **Changed after review; unreviewed.** AM-5b (new); AM-6.2, AM-9.2, AM-20.2, N-4 (concession); AM-7.2, AM-7.3 (class; hypotheses); AM-11 (entry points; form); AM-14 (trace); AM-21.1 (class; classification); AM-22, AM-36 (target); AM-23.2 (classification); AM-30 (hypotheses); AM-31 (class; concession); AM-1.1, AM-2.1, AM-2.2 (cells). Of the 46 rows checked, 17 were changed and 29 are unchanged since the review.
- **Lean.** The reviewer read no Lean statement. Every kernel identifier cited here is unverified by the review.
- **Proofs.** No recovery route and no direct-proof target was verified. Every target in §12.3 is a candidate with no proof given.
- **Window confinement.** Of the 38 rows of Table 5, 29 were checked; not checked, 9: AM-16, AM-24, AM-25, AM-27.1, AM-27.2, AM-29, AM-32, AM-38, AM-5b.
- **Per question.** Each question in §19 lists the unchecked rows it rests on. Stated basis checked by the review: Q11, Q8, Q6, Q5, Q7, Q9, Q12 (the Q5, Q6 and Q12 texts were rewritten in r7, and the option texts of the other twelve were written out in full in r8; none of these texts has been reviewed); in part: Q1, Q10, Q4, Q3, Q15, Q2, Q13; not checked: Q14. The focused confirmation of r8 read all fifteen questions in full (next bullet).
- **EF-1.** The review of r6 did not, on what it reported, overturn the checked EF-1 mathematics; it did not re-derive it, and it read EF-1 r6 only in part.
- **Changed in r8; unreviewed.** No row's values. New text only: the option texts of the fifteen questions (§19); the lines for AM-7.2 and AM-7.3 in the CONTINGENT table and the rewritten class cells of §14.1; the lines for AM-21.1, AM-31 and AM-4.4 in §14.4; the column "EF-1 r6 §4.2, window entry" and the AM-5b line of Table 5; the column "Standing now" of §20; the population lines under the tables.
- **Citations and site lists.** For r8 the citations of the 19 recovery rows and of AM-5b were checked at `main`. The lists of downstream sites in the rows of §2 to §7 were checked only for existence and for a keyword of the row's subject on the cited line. The site counts of §8 and §9 are counts relative to the search patterns stated there and were not recounted for r8. A site that paraphrases its subject, or lies outside those patterns, would not have been found. No list in this audit is claimed to hold every affected site.
- **The limits of r7 and r8.** See §22, "Still not done".
- **Focused confirmation of r8** (`CONFIRM-A1-IMPACT-r8.md`; its own statement of coverage, its sections 11 and 12). It read r8 by section and by search, not in full. *Rows.* Of the 57 rows it checked 21 against `main`, for the purpose of a question or of the rule for FIRM: AM-2.1, AM-5, AM-5b, AM-6.2, AM-7.1, AM-7.2, AM-7.3, AM-8, AM-9.2, AM-11, AM-21.1, AM-22, AM-23.2, AM-30, AM-31, AM-33.1, AM-4.4, N-3, N-6, and, for their cells only, AM-36 and N-1. A check was a reading of the cited text and of the cited Lean statement, not a derivation, and for most of these rows it covered only the lines that the question or the class rests on. The other 36 rows were not checked; the eleven rows the review of r6 did not check stay unchecked except AM-5b. *Questions.* All fifteen were read in full, with the readiness field, options, basis, recommendation and dependencies of each. *Proofs.* No recovery route, no direct-proof target and no proof sketch was verified; P4 and the confirmation's own measurability argument are unwritten and unchecked; the Lean statements were read, not built. *EF-1 r6.* Read only for its coherence class (its two §4.2 lines and nit 5); no other citation of EF-1 and none of its mathematics was checked. *Sections not read:* §1 beyond three lines, §2 to §7 outside the rows named, §13, §14.2, §14.3 outside Table 5's counts and the gate tally, §15 beyond its first bullet, §16, §17, and §20's tables D1–D25 and T1–T21. *Citations not checked:* Q1's statement that E3's justification is open; GR:835; `appendix-c-objections.md:132` and `book/README.md:90`; the FULL mirrors; Main:155, :157, :338, :354; the 107 census anchors of §10 other than family 1 and the cells of families 8, 33, 34 and 40. *Records of Q14.* The files and the cited lines were read; whether a surviving claim cites any of them was not traced. *Quotations.* Compared with GitHub by reading, not by a byte-for-byte tool. *The pilot* authorized in c.6898613777, and which questions wait on it, were not checked. Its verdicts mean only that a question's text, options, basis and dependencies were checked and stand with the listed corrections applied.
- **Changed in r9; unreviewed as applied.** The corrections of the focused confirmation were applied by exact replacement at the places it names (§22, "r9 changes"). The text as edited has not been re-read by the confirmer. The split of the questions by dependence on the pilot (§19) is the coordinator's and has not been reviewed.

## 22. r7 changes, r8 changes, r9 changes, and what is still not done

### r7: findings of the review of r6, and the requirements of 2026-11-15

**Findings of the review of r6.** "Material" names the questions whose basis the change alters.

| Finding | Disposition | What changed | Where | Material to |
|---|---|---|---|---|
| F1 re-pin | applied (r7 in part; completed in r8) | pinned to EF-1 r6 (r5 with wording nits); every body citation is to r6; R1–R15, R18, R20, R21 edited in place; R16 applied cell by cell in Table 3, R17 as a column of Table 5, R19 as the column "Standing now" of §20; ten trace differences T22–T31; the Standing note that asked the reader to read "r5" as "r6" is removed | Standing; §0; §1; §14.3; §19; §20 | none |
| F2 gates | applied; a substantive correction (adopted direction, c.6898395533) | Q5 and Q6 rewritten: each option in full, what is asserted conditionally and what of nature; gate tally split; Q12's second stage restated | §14.3; §19 | Q5, Q6, Q12 |
| F3 removed rows | applied | four rows conceded as removed; counts 23, 5, 13, 4, 12 | §12.3, §12.4 | Q9 |
| F4 AM-22 | applied; GR:58, :68 read | target has no route avoiding the shell measure; AM-30's hypotheses reduced to P6's; AM-22 out of Q12's stage | AM-22; §12.3; §19 | Q1, Q5, Q6, Q12 |
| F5 FIRM rule | applied by the adopted rule (c.6898395533); the reviewer's count disputed | one rule; 4, 5, 9, 1; premises of each FIRM row | §0; §14.1 | Q6, Q8, Q11 |
| F6 | applied | AM-23.2 "partly"; AM-21.1 "no"; 11, 13, 33 | §12.3 | Q8, Q11, Q12 |
| F7 AM-31 | applied | FIRM for the theorem as stated; part (3) a replacement part; RT; the visible-record bound | AM-31; §0; §12.3 | Q1, Q6 |
| F8 K4 | applied | K4 (i) and K4 (ii); five rows use a constructed realization | §0; §12.3 | Q12 |
| F9 Main:290–324 | applied as a row (adopted direction, c.6898395533) | AM-5b; population 57; totals | AM-5b; §9; §12 | Q2, Q13 |
| F10 P4 | applied | two added hypotheses | §14; §12.3 | Q8 |
| F11 T15, T17 | applied (r7 in part; completed in r8) | (i)–(vi): r8 adds (v), §15's first bullet; completes (iv) in Table 2 ("restated or dropped as AM-1.3b"); and completes (vi) by adding GR:68's condition to P7 and to the AM-22 line of §14.3 | §14; §14.3; §15; AM-11; AM-22 | Q3 |
| F12 | applied | family 40 cell | §10 | none |
| F13 | applied (r7 in part; completed in r8) | "eight"; each line of Table 5 recounted against §12.1: 21 lines, 38 rows and §11 item 3; the population is stated under the table | §14.3 | none |
| F14 | applied | AM-1.1's form cell | §14.3 | none |
| F15 | applied (r7 in part; completed in r9) | summary rewritten; in r9 the three sentences the focused confirmation found inexact are corrected | §18 | none |
| F16 | applied | (i)–(iv) | §12.3 | none |
| F17 | applied | (LE) and the two candidates stated | §19 | none (wording) |
| F18 | applied | Q9 added to Q2's dependencies | §19 | Q2 |
| F19 | applied | Q8(b) and Q5(d) one decision | §19 | none |
| F20 | applied | family 1's note in Q13 (a) | §19 | Q13 |
| F21 | applied (r7 in part; completed in r8) | the cells of §14 (P1) and §14.2 (MI), and nine further rows found by counting the cells of every table row (32 bars in all), now use `∣`; no table row splits | §1; §12.3; §14; §14.1; §14.2; §14.3; §20 | none |
| F22 | applied | C6 row | §1 | none |

**Requirements of 2026-11-15** (adopted direction, c.6898395533). (1) Population 57: AM-5b has a value in every column, "unclassified" for its census entry only; in r9 its census entry is family 1, anchors at Main:312 and :314 (§10); totals in §0, §9, §12, §12.1, §12.3, §12.4, §14.1, §14.3, §18, §21 (r7). (2) One rule for FIRM, stated once in §0 in the adopted words, with the premises of each FIRM row and their places on `main` in §14.1 (r7; the older class cells rewritten in r8). (3) Q5, Q6, Q12: rewritten in r7; substantive. (4) Options in full with basis: Q5, Q6 and Q12 in r7; the other twelve, and Q12 option by option, in r8. (5) "Decision-ready?" on all fifteen (r7); in r8 each names the r7 and r8 changes and the rows that materially alter its basis. (6) The table above. (7) The status sentence: Standing, §18.

### r8 changes

r8 changes no row's category, reason, landing, class, direct-proof entry or concession, no count, and no recommendation. The entries marked † add a line or a sentence that states a consequence of a value r7 already had; each is unreviewed.

| Item | What r8 did | Where |
|---|---|---|
| Attribution (coordinator's correction; #1169 comment 6898760764) | The texts quoted from comments 6896252651, 6896496410, 6896771264, 6896890693, 6896940222, 6897254631, 6897455387, 6897859755, 6897946443 and 6898395533 are review text the owner relayed and adopted ("Relayed, and I adopt them."). Every citation of them as the owner's words is changed to "adopted direction, c.[id]", defined once in Standing; "the owner's rule, table, tiers, check, 17, first claim, assessment" become "the adopted …". The quoted text is unchanged. Comments 6894872312, 6895032895 and 6896070253 stay attributed to the owner. In §17, "Owner item" becomes "Adopted item" | Standing; throughout |
| 1. Quotations | The thirteen comments re-read on #1169, and 6898613777 and 6898760764 read; every quotation from them compared character for character. Three corrected, each a single mark written for the record's double mark inside the sentence: the coverage sentence (Standing; §21) and the rule for FIRM (§0). Each quotation carries its comment id; the six that r7 gave as "in session" are cited to 6898395533. Three citations of the accepted proposal in 6896070253 now say that it is the coordinator's proposal, which the owner accepted | Standing; §0; AM-5b; §18; §19 (Q11, Q6, Q7); §21 |
| 2. §14.1 | Notice deleted. Class cells rewritten: AM-7.2 FIRM to CONTINGENT; AM-7.3 FIRM to CONTINGENT; AM-21.1 FIRM to NEW, conditional theorem available; AM-4.4 marked "conditional theorem available"; AM-31 "NEW, by part (3)" to FIRM for the theorem as stated, part (3) a replacement part. "Counts" 6, 3, 9, 1 to 4, 5, 9, 1, with the RC and OP split (RC: 3, 5, 8; OP: FIRM 1, NEW 1, replacement 1). The recheck paragraph rewritten for the current classes. "How this differs from the review of r4": two rows to five. The cross-tabulation's class column and totals: of the seven, 2, 2, 2, 1 to 1, 4, 1, 1; the other twelve, 4, 1, 7 to 3, 1, 8. "What the cross-tabulation shows" rewritten. The three disputed rows are given with both positions, the review's in its own terms (its F5, F10) | §14.1 |
| 2. §14.1 † | The CONTINGENT readings table gains lines for AM-7.2 and AM-7.3, which were CONTINGENT in r7 without a line | §14.1 |
| 2. §14.4 | Class cells of the second table: AM-7.2 and AM-7.3 to CONTINGENT, AM-21.1 to NEW with a conditional theorem available. The first table's AM-31 line is labelled a replacement part. FIRM is no longer redefined here | §14.4 |
| 2. §14.4 † | First table: a line for AM-21.1 (L9 carried as a named hypothesis, as for AM-31 part (3)). Second table: lines for AM-31 (FIRM) and AM-4.4 (conditional theorem); population 11 stated | §14.4 |
| 2. §14.3 (R16, R17) | Table 3, column (b): seven quoted marks of EF-1 r4 replaced by EF-1 r6's requirement (AM-1.1, AM-3.2, AM-4.1 with AM-4.3, AM-4.2, AM-5, AM-8, AM-22 with AM-36), each checked against EF-1 r6 §4.2; AM-6.2's cell given r6's entry. Table 5: the notice folded in: the AM-5b line, a column for EF-1 r6's window entry, the counts by line (21) and by row (38). Tables 1 and 4: four class cells for AM-7.2 and AM-7.3 to CONTINGENT. The closure lemmas are described as checked once, not as unchecked | §14.3 |
| 2. §20 (R19) | The notice and the subsection "Standing of D1–D25 and T1–T21" are deleted; each of the 46 entries has its standing in a last column. Cells rewritten where this audit's position had changed: D1, D5, D6, D7, D10 (twice), D15, D24; T4, T12, T15, T16, T17, T28, T29. EF-1's r4 marks "(M-desc)" in T5, T6, T7, T8, T10, T11, T13, T14, T16, T18 are given in EF-1 r6's words | §20 |
| 2. §1 | The lead says what the table now cites. Rewritten: the C4 line (AM-31), the C5 line (counts), C9 (the pin), C12 (57 rows), sections A and B, two lines of the directions table, "Carried from r4" (57; 48, 6, 3). Seven EF-1 citations moved to r6 | §1 |
| 3. F1 | 149 body citations "EF-1 r5" moved to "EF-1 r6" after reading EF-1 r6's changes table; the cited places are unchanged except four, brought to r6's wording (Standing). "The recheck of EF-1 r5" keeps its name. The concordance and D15 describe questions 9 and 10 as r6 words them. Standing's pin paragraph rewritten and the reading note removed | Standing; §0; §2–§16; §19; §20 |
| 3. F11 (v), F13, F21 | As the table above | §15; §14; §14.3; nine table rows |
| 4. Questions | Each option of Q11, Q1, Q8, Q7, Q9, Q10, Q4, Q3, Q15, Q2, Q13, Q14 and Q12 written out in full with what it asserts of nature and its basis; Q5 and Q6 unchanged. "Decision-ready?" rewritten on all fifteen: READY for Q7, Q10, Q4, Q15; NEEDS FOCUSED CONFIRMATION for the other eleven, as in r7. Q2's plain statement says eighteen rows. Q12's plain statement describes EF-1 r6's questions 9 and 10 | §19 |
| 4. Questions † | Q8, "What it changes": "two of the three CONTINGENT rows" to "four of the five". Q8(c) says that it is the option under which P4's two added hypotheses are carried. Q15(c) notes that the review it names has since been made. Q12's readiness line notes that the reason for the first tranche predates P4's change of class; the tranche is not changed | §19 |
| 5. Citations | Two corrections and one confirmation. "H-decouple is not established here" is at GR:787, not GR:795, which states the condition (five places: AM-33, L7, Q1 twice, Q1's basis). "by the cone lemma and (iii)" is at Main:384; the proof begins at Main:383 (AM-7; D7). AM-5b: every line it cites was read and matches | AM-7; AM-33; AM-5b; §14.2; §19; §20 |
| 6. Consistency | The three 57-row tables recounted by script: categories 2 + 1 + 4 + 3 + 18 + 16 + 10 + 3 = 57; reasons 48 + 6 + 3; classes 4 + 5 + 9 + 1 = 19, with 38 rows in no class; direct-proof entries 11 + 13 + 33; concessions 23 + 5 + 13 + 4 + 12. A population line is placed under each table that lacked one. One stale total corrected ("47 + 6 + 3 covers all 56 rows" to "48 + 6 + 3 covers all 57 rows", §14.1) | §0; §1; §8; §10; §12.2; §14–§14.4; §20 |

### r9 changes

r9 applies the corrections of the focused confirmation of r8, records its verdicts in the readiness fields of §19, and records the coordinator's split of the questions by dependence on the pilot. It changes nothing else: no row's category, reason, landing, class, direct-proof entry or concession, and no recommendation. Totals that changed, each for the reason given in its line: §14.1's "37" to "38" (a stale total); §12.2, 12 lines to 13 (a line for AM-5b); the trace table, 10 entries to 11 (T32). No numeric total depended on AM-5b's census entry; its four mentions are corrected (row AM-5b item 4; Q13(a); Q13's readiness line; §22, requirements item (1)) and §10's family 1 line names the row. "E" numbers are those of the confirmation's section 10. Lines without an E number are its other stated corrections and the changes that follow from them.

| Edit | Location and subject | Applied? |
|---|---|---|
| round label | title line: "r8" to "r9" | done |
| E1 | §19, Q12, option (b): the first tranche in two groups | done |
| E2 | §19, Q12, recommendation: the reason for the first tranche | done |
| E3 | §19, Q12, "Changed in r6 …, corrected in r7": (a) the K1/K2 list | done |
| E3 | §19, Q12, "Changed in r6 …, corrected in r7": (b) the K3 stage, P6 and P10 | done |
| E4 | §19, Q12, "Decision-ready?": the two sentences on the first tranche's reason | done |
| E5 | §14.3, gate tally: (a) part (3) of P9 | done |
| E5 | §14.3, gate tally: (b) sentence on P4 and P5a added | done |
| E6 | §12, row 17 (AM-7.2), gate cell | done |
| E6 | §12, row 18 (AM-7.3), gate cell | done |
| E6 | §14, P4, gate cell | done |
| E6 | §22, "Still not done": the bullet "Q12." deleted | done |
| E7 | §19, Q12, "What it changes": writer and reviewer | done |
| E8 | §0, FIRM: the rule of application | done |
| E9 | §0, CONTINGENT: second clause (applies, since AM-7.2 and AM-7.3 stay CONTINGENT in r9) | done |
| E10 | §14.1, table "Classes under the one rule", AM-2.1, last cell | done |
| E10 | §14.1, dispute paragraph, AM-7.2 sentence, after "(its F10)" | done |
| E28 | §20, "Disagreements with the review of r6", item 2 | done |
| E28 | §14.1, "Counts.": the review's figure | done |
| E28 | §14.1, "Counts.": after "5 to 8." | done |
| E11 | §19, Q11, option (a): which statements stay or may land | done |
| E11 | §19, Q11, option (a): the C2-necessity rows | done |
| E12 | §19, Q1, option (b-mode): what P7 also needs | done |
| E12 | §19, Q1, option (a) and "What it changes": "(a replacement part, not a recovery)" after "part (3) of P9" (two places) | done |
| E13 | §19, Q8, option (a): the dependency sense | done |
| E14 | §19, Q8, "What it changes": two CONTINGENT rows, and two on the disputed classification | done |
| E15 | §19, Q8(c), "Basis": Main:724 quoted in full | done |
| E15 | §19, Q6(e), "Basis": Main:724 quoted in full | done |
| E15 | §19, Q8, recommendation: the same full quotation | done |
| E15 | §9 item 1: the same full quotation | done |
| E16 | §19, Q6, recommendation: separate reasons for (c) and (d) | done |
| E16 | §19, Q6, recommendation: what the review of r6 recommends | done |
| E17 | §19, Q6, "What each choice allows": P5a | done |
| E18 | §19, Q6, option (e) | done (no edit called for by the confirmation; with E15 the basis is quoted in full) |
| E19 | §19, Q3, option (a): Sub:157 | done |
| E20 | §12.1, row 57 (AM-5b), column "Under Q2(b)" | done |
| E21 | §19, Q2, option (b): AM-5b's hypothesis is not restated | done |
| E21 | §19, Q2, option (b): the threshold Theorem added to the A1-free results that stay | done |
| E22 | §19, Q2, "What it changes": the model-class sentence of Q9(c) | done ("[this confirmation's reading]" written as "[the focused confirmation's reading]") |
| E22 | §12.2: a line for AM-5b added | done ("not searched for here" written as "not searched for (focused confirmation of r8)") |
| E22 | §12.2: population line, 12 lines to 13 | done |
| E23 | row AM-5b, item 1: the Theorem is A1-free | done (inserted at the place named, inside the sentence, before 'on "the substratum of §1.2 …"') |
| E23 | row AM-5b, item 5: what P1 forces | done |
| E24 | row AM-5b, item 4: census family 1 in place of "unclassified" | done |
| E24 | §19, Q13, option (a): AM-5b is in family 1 | done |
| E24 | §19, Q13, "Decision-ready?": "its kernel witnesses not located" dropped | done ("Unchecked rows" of Q13 does not contain the phrase; nothing to drop there) |
| E25 | §10, family 1, column "Rows" | done |
| E26 | §19, Q14, options lead: none of the three records is frozen | done |
| E26 | §19, Q14, option (c) | done |
| E26 | §19, Q14, recommendation: the reason | done |
| E27 | §19, Q7, option (b): Main, not Substratum | done |
| E29 | §20, trace table: entry T32 added after T31 | done |
| E29 | §20, trace table: population 10 to 11 | done |
| E29 | §20, trace table: heading follows the new entry | done (consequential on the edit named) |
| E29 | §20, lead: "ten trace differences T22–T31" to eleven, T22–T32 | done (consequential on the edit named) |
| E29 | §14.3, under Table 5: "ten entries … (T22–T31)" to eleven, T22–T32 | done (consequential on the edit named) |
| E29 | §14.1, "The trace comparison": T1–T31 to T1–T32 | done (consequential on the edit named) |
| E29 | Standing: pointer "T22–T31" to "T22–T32" | done (consequential on the edit named) |
| E29 | §20 D-table pointer | done (consequential on the edit named) |
| E29 | §19, Q2, "Disagreement attached": pointer to T32 | done (consequential on the edit named) |
| E30 | §14.1, "Population.": 37 to 38 | done |
| E31 | §18: what the 57 rows are | done |
| E31 | §18: the ten kept rows | done |
| E31 | §18: the four firm rows | done |
| E31 | §22, response table, F15: disposition says where it was completed | done (consequential on the edit named) |
| E32 | header: "only to quote the owner; twelve are quoted" | done |
| E32 | §0: "are not the owner's" | done |
| E32 | §1 heading | done |
| E32 | §1: "C10 (owner records)" | done |
| E32 | §22, F2 disposition | done |
| E32 | §22, F5 disposition | done |
| E32 | §22, F9 disposition | done |
| E33 | §21: bullet "Citations." replaced by "Citations and site lists." | done |
| E33 | §8: population line | done |
| E33 | §9: note at its head | done |
| E33 | §19, Q3(a): the "A1–A6" lines | done |
| E33 | §19, Q4(a): the citations of item (ii) | done |
| site-list limit (confirmation §9) | §2 head: coverage limit of the site lists stated | done |
| site-list limit (confirmation §9) | §3 head: coverage limit of the site lists stated | done |
| site-list limit (confirmation §9) | §4 head: coverage limit of the site lists stated | done |
| site-list limit (confirmation §9) | §5 head: coverage limit of the site lists stated | done |
| site-list limit (confirmation §9) | §7 head: coverage limit of the site lists stated | done |
| site-list limit (confirmation §9) | §19, Q4, "What it changes": the site list is by search | done |
| site-list limit (confirmation §9) | §15: "rewritten at 65 lines" is a count by pattern | done |
| site-list limit (confirmation §9) | row AM-13: "one of the ten by-name sites" | done |
| site-list limit (confirmation §9) | §22, "Still not done", "Site counts.": pointer to §21 | done |
| site-list limit (confirmation §9) | §12.2: the column of kept text is a list of the sites found | done |
| site-list limit (confirmation §9) | §13 head: the sites cited are those found | done |
| AM-5b census (confirmation §4) | §22, requirements of 2026-11-15, item (1): the census entry | done |
| FIRM classes (confirmation §2) | §14.1 (recovery classes): both positions on AM-7.2 and AM-7.3 side by side, with the test each applies; the audit's classes unchanged | done |
| FIRM classes (confirmation §2) | §20 (remaining disagreements): subsection with both positions | done |
| FIRM classes (confirmation §2) | §19, Q8, "Disagreement attached": pointer to the two positions | done |
| FIRM classes (confirmation §2) | §19, Q12, "Disagreement attached": pointer to the two positions | done |
| readiness and pilot | §19, Q11, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q1, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q8, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q6, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q5, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q9, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q3, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q2, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q13, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q14, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q12, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q7, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q10, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q4, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, Q15, "Decision-ready?": the confirmation's verdict and the pilot line | done |
| readiness and pilot | §19, lead: the readiness summary | done |
| readiness and pilot | §18, last paragraph: the readiness sentence | done |
| coverage (confirmation §11, §12) | §21, "Per question.": the confirmation read all fifteen | done |
| coverage (confirmation §11, §12) | §21: the focused confirmation's own coverage statement added | done |
| §22, consequential | §22 heading | done |
| §22, consequential | §22, "Still not done", "Review.": the confirmation has been made | done |
| §22, consequential | §22, "Still not done", "The pilot.": the split is recorded; the selection is not done | done |
| round label | header: paragraph "r9." added before "Goal link" | done |

Population of this table: 116 lines, covering the 33 edits E1 to E33 and the confirmation's other stated corrections. Not applied: none.

Left as r8 has them: the two classes the confirmation would move (AM-7.2 and AM-7.3, CONTINGENT here; both positions in §14.1 and §20); the counts 4, 5, 9, 1 wherever they are stated; r7's and r8's own change records in this section, apart from the lines named above; and the quotations of #1169, which are the record's words.

### Still not done

- **Review.** The focused confirmation that eleven questions waited on has been made (`CONFIRM-A1-IMPACT-r8.md`). It read r8 by section and by search, not in full, and verified no recovery route (§21). What r8 wrote outside the parts it read has not been reviewed, and the edits applied in r9 have not been re-read by the confirmer.
- **Citations, how far the check went.** In the sections of the 19 recovery rows (AM-2, AM-4, AM-5, AM-7, AM-8, AM-11, AM-21, AM-22, AM-23, AM-24, AM-30, AM-31, AM-33, AM-36, and §7 for N-3 and N-6) and of AM-5b: every quotation that stands beside a file and line was compared with that line at `main` by script, and every mismatch was read (two were real and are corrected; the others were differences of mathematical typesetting or a quotation placed beside a second citation). The lines that carry a row's result, the premises of the four FIRM rows, the textual bases of the five CONTINGENT rows, the lines of AM-5b and the lines the option texts cite were read one by one. The long lists of downstream sites (book chapters and their FULL mirrors, 267 distinct citations in these sections) were checked only for existence and for a keyword of the row's subject on the cited line, and the 22 that failed that test were read; a downstream line that mentions the subject without supporting the stated use would not have been caught. Citations in other sections were not checked for r8, except where they were read for another item.
- **Lean.** Read for r8: `isDiag_Phi` and `Phi` (`EquivalenceChain.lean:242`, :253), `leapFiniteRange` (`SecondOrderDrive.lean:306`), `gateRegion` (`SecondOrderLayer.lean:208`), `a2_every_substratum` (`SubstratumInterfaceAudit.lean:106`). No other kernel identifier was read, and none was built.
- **EF-1 r6.** Read for r8: both tables of its §4.2, questions 9 and 10 of its §11, and its changes table. The rest was not re-read. In Table 5 and in §20, "no class in EF-1 r6" was decided by matching the names of its classes to rows, not by searching it for each row.
- **§20, the positions.** The two position columns of D1–D25 and T1–T21 give each party's position as it was taken, some at EF-1 r4, and the last column gives the current standing. The EF-1 column of T1–T21 was not compared cell by cell with EF-1 r6's first table beyond the marks listed above.
- **§17.** It is r6's change record. Its counts and its pin are r6's; only its attributions were changed.
- **Row sections.** §2 to §7 were not re-read in full for r8. They were searched for class statements about AM-7.2, AM-7.3, AM-21.1 and AM-31 and for the two citation errors; other wording there is r7's.
- **Site counts.** The 65 "A1–A6" lines, the four by-number and ten by-name citations of item (ii), the 18 headline sites and the sites of §9 were not recounted. Each is a count relative to its search pattern, and no list in this audit is claimed to hold every affected site (§21).
- **The pilot.** Comment 6898613777 authorizes selecting two candidate claims for a bounded pilot of the fixed-horizon lemma and identifying which of the fifteen questions depend on its outcome. The selection is not done here. The split of the fifteen questions by dependence on the pilot is recorded in §19 as the coordinator supplied it for r9; it has not been checked against the pilot, which has not reported.

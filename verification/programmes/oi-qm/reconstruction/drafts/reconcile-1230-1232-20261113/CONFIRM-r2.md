# Focused confirmation: #1230 / #1232 reconcile r2

**Reviewer.** The independent reviewer of r1 (Claude Code subagent), 2026-11-13. This is a read-only
confirmation: no commit, push, comment, edit or dispatch, and no computation on any OI rule. It is
model-written and is not verification (§A.46 item 7).

**Object.** Branch `research/reconcile-1230-1232-20261113`, fetched by name, at exact head
`b36bba60948657617a990a8186973912e4e990e7`.
- That commit is a single-parent child of `main` `c3b5f37a`.
- It adds only the five files under
  `verification/programmes/oi-qm/reconstruction/drafts/reconcile-1230-1232-20261113/`.

## Verdict: ACCEPT WITH CHANGES (two strings in the added paragraph)

### (1) All 20 replacements were applied exactly: confirmed

**Method.** I parsed the 25 old→new strings of `REVIEW.md` §3 by script and applied them to r1. The
reviewed `RECONCILE.md` has sha256 `05ad46b2…`. The appended sentence of change 5 was placed after
"set up to examine.". The result was diffed against the committed `RECONCILE-r2.md`.

**The diff has exactly two hunks.**
- **Change 20.** "working-area record" became "working record". The rest of the sentence is identical.
  This matches the stated modification.
- **The added paragraph "Conclusion, at its exact strength".** It sits after §5's "None supplies an
  operation outside 𝒦 …".

There is no other difference.

### (2) The added paragraph adds two claims beyond the stated strength

The paragraph's first sentence restates the owner's guidance as RESPONSE-r1 records it. "Physically
reachable under the currently demonstrated OI premises" excludes designed maps. It is therefore
consistent with §2's scoping and its treatment of the saturation register.

The following parts also match the record:
- the non-impossibility clause, with C-dyn, E_r, non-spanning preparations and the O2 window open;
- the separation of mathematical existence from physical reachability;
- the distinction between N2.1 (the reachable laws do not span) and 𝔊_K (M-INACC). This matches
  change 5 and OA2:302–323, :442–467.

Two parts go beyond the record:

- **a. "T5 are proved".** T5 is a paper argument [A]. It is not kernel-checked (INTERVENE §6: "no
  claim here says they are kernel-checked"), it was hand-checked only in REVIEW-r1, and it is off
  `main`. Grouping it with the kernel theorem `realized_of_instAvail` as "proved" promotes a paper
  argument to the kernel layer (Code Review Rules: "Keep verification layers distinct"). It also
  conflicts with r2's own §5 heading ("not established under §A.46 item 1"). The owner's example
  named only `realized_of_instAvail`.
- **b. "what the drafts and the corpus supply".** This reconciliation audited the two drafts against
  selected records. It did not run the corpus-wide search that a negative claim about the corpus
  requires (§A.19). REC-1 also classes corpus items as Q2-F: rows 6, 17, 20 and 42 are designed or
  proposal-rule maps. The clause is therefore broader than the evidence and is easy to misread.

**Required replacements in `RECONCILE-r2.md` (each old string occurs once):**
- old: `This is a finding about what the drafts and the corpus supply, not a documentation gap.`
  new: `This is a finding about what the two drafts supply, read against the records cited above, not a documentation gap.`
- old: ``For example, `realized_of_instAvail` [K] and T5 are proved, and conditional on their hypotheses, but they concern representations and generated theories, not physical reachability.``
  new: ``For example, `realized_of_instAvail` is a kernel theorem [K] and T5 is a hand-checked paper argument [A], not kernel-checked and off `main`; both are conditional on their hypotheses, and both concern representations and generated theories, not physical reachability.``

### (3) The review copy and the hashes in OBJECTS.md: confirmed

**`REVIEW-r1.md`.**
- The committed sha256 is `4fbcf865…`.
- Restoring "working-area" → "working-area" gives sha256
  `4785ec424f30ccd9c24b2ed16c170b167d063ed448770b0be1b86173729e0b69`. That is byte-identical to my
  `REVIEW.md`, whose git blob is `7cd190ce`.
- The diff touches only lines 199, 273 and 274, as OBJECTS.md lists.

**`RECONCILE-r1.md`.** Restoring the word on line 5 gives `05ad46b2…`, which equals the reviewed r1.
Its reviewed blob is `c03fe146`.

**Every committed sha256 and every reviewed sha256/blob in OBJECTS.md is correct.**
- `RECONCILE-r2.md`: blob `1753a236`, sha `bf9c2acc…`.
- `RESPONSE-r1.md`: blob `67bb83d4`, sha `6818a0a8…`.

Neither r2 nor RESPONSE-r1 contains the barred word.

### (4) No new overclaim elsewhere

- **RESPONSE-r1** describes each disposition accurately.
- **Its source checks** match what I verified: OA2 lines, APPROX r4a :455–483, INTERVENE :108, :123
  and :222, the Q-868-H commits, and the fact that Bell-scope does not cite INTERVENE.
- **Its "Not changed" items are accurate.**
  - The Main:414 nit carried no replacement.
  - The owner's adoption of option (c) (c.6854728636) is not recorded in r2. That is a correct
    omission, since recording it was outside the 20 changes.

Apart from (2a) and (2b), r2 states no conditional as unconditional and no interface-specific result
as OI-wide.

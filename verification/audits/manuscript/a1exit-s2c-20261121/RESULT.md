# A1-EXIT Step 2, unit S2-C — R1/R2 scoping and criterion-3 qualifications: result

**Status.** Writer's result, WIP / UNVERIFIED. Independent non-author review is required; merge is a
separate owner decision. Bands unchanged (consistency work, §A.23).

**Authorization and goal link.** As in `PREREG.md` (owner `amaybaum`, #1169 comment 7056875845,
2026-11-21T03:51:25Z; goal: the A1-exit objective, #1169).

**Commits.** PREREG `e9ebf3ab8`; edits, rebuilt artifacts and coverage ledger `5cf892c69`; RESULT
`05d2ab4f3`. After review round 1 (§8): amendment A1 `0d17087b2`, then its edits and this revision of
the record. Base `main` at `1c7eedc4`. No edit adds or removes a line, so every site keeps its base line
number on this branch.

## 1. Edits as applied

All 27 splices of `PREREG.md` §5 were applied verbatim, with no deviation. After applying, each new string
occurs exactly once in its file and each replaced old string is gone.

| ID | Site (line on this branch) | Ledger row | Kind |
|---|---|---|---|
| C1 | `papers/Main.md:131` | X-20 | return form, introduction |
| C2 | `papers/Main.md:141` | X-23 (X-20) | return form |
| C3 | `papers/Main.md:180` | X-20 | return form |
| C4 | `papers/Main.md:224` | X-20, X-23 | "assumed as hypotheses and not adopted" and the return form |
| C5 | `papers/Main.md:724` | X-20 | return form |
| C6 | `papers/Main.md:280` | X-15 | law form, (IP) |
| C7 | `papers/Main.md:766` | X-60, X-61 | law form, (IL) |
| C8 | `papers/Main.md:159` | X-20 (sitemap) | finite-representative scope |
| C9 | `papers/Main.md:732`, clause (iv) only | X-12 | "on a finite representative" |
| C10 | `papers/SM.md:122` | X-41 | "assumed … not adopted" and the law form, H-μ(φ,Θ) |
| C11 | `papers/SM.md:252` | X-41 | the same, at the selected invariant measure, on ℤ^d |
| C12 | `papers/SM.md:334` | X-17 | the same, H-μ(sp) |
| C13 | `papers/SM.md:44` | X-20 (Phase 2 S1) | return form |
| C14 | `papers/GR.md:138` | X-20 (Phase 2 G1) | return form |
| C15 | `papers/GR.md:589` | X-20 (Phase 2 G2) | return form |
| C16 | `papers/Substratum.md:92` | X-20 (Phase 2 B1) | return form |
| C17 | `papers/Structure.md:1224` | X-20 (review B1) | finite-representative scope |
| C18 | `book/ch01-observation.md:121` = FULL:454 | X-20 (mirror of M:131) | return form |
| C19 | `book/ch01-observation.md:161` = FULL:494 | X-20 (review B1) | finite-representative scope |
| C20 | `book/ch01-observation.md:179` = FULL:512 | X-20 | "assumed … not adopted" and the return form |
| C21 | `book/appendix-c-objections.md:104` = FULL:6259 | X-20 | return form |
| C22 | `book/appendix-b-derivations.md:46` = FULL:5723 | X-15 (mirror of M:280) | law form, (IP) |

**Not edited, as decided in PREREG §2.**

| Item | Outcome | Reason |
|---|---|---|
| X-25 (M:147) | option (a), F as printed | LEDGER §12 N1. The finite scope is visible at the site through "instances of the overlap-and-return theorem" (finite sets, a bijection; M:145) and "$(\Gamma_t)$ is periodic" |
| X-50 | handled by S2-B | S2-B (#1473) prints the X-50 wording at its Main:336 (its E2); confirmed from the PR body and diff |
| X-13 | no site | criterion 3 met (LEDGER §3.1) |
| M:356 | no edit | it states the role of P-indivisibility, not that it holds |
| Cx:474, ch15:113 = FULL:3990 | no edit | each sentence opens "On a fixed finite reversible representative" |
| R1 (X-11) | check found nothing | No site in Main, SM, GR, Substratum or the book states a selected law on an infinite carrier unconditionally. Main's (iv) keeps "a standard but substantive epistemic postulate, not derived". M:58 calls the counting measure "the default, not a constraint on representations". Each A1-free result names its law hypothesis: ρ is any root-shared probability (M:131), (IP) (M:280), (IL) (M:766), H-μ(φ,Θ) and H-μ(sp) (SM:122, :252, :334). With (iv) scoped to a finite representative (X-12), R1 is named through these per-result law hypotheses: no result uses a selected law on an infinite carrier without naming its law condition as assumed and not adopted |
| C1 (X-71) | check found nothing | GR:58 is stated "Under A1" for a finite total system with the boundary interaction negligible at the shell scale. No text in `papers/` or `book/` claims a normalized invariant shell law for coupled bijections |

## 2. Wording for S2-E (exact final text)

**Return form, at a site that introduces (NR) or opens a sentence with it (Main):**

> (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected
> update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to
> satisfy it.

**Return form, as a parenthesis after "assumed … not adopted" at a restatement (Main):**

> (it concerns a time that need not be accessible and then has no finite-window test; for the selected
> update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to
> satisfy it)

- In the companions write "of [Main §3.2]".
- In the book write "of Main §3.2". The book's restatements, which say "the near-return condition of
  Chapter 1 §1.5", take the parenthesis form (appC:104; ch01:179 after amendment A1).
- Where "assumed … not adopted" is missing, it is added as ", assumed as a hypothesis and not adopted,"
  (ch01:179), or, for several conditions, "assumed as hypotheses and not adopted" (M:224).

**Law form** (sentence after the statement of the condition, with X its label):

> X is a condition on a law on the whole carrier; finite-window data can test some of its consequences
> but cannot establish it, and do not distinguish it from a finite carrier's counting law.

Inside a clause (SM:122, :252) the same text stands in parentheses after "assumed as a hypothesis and not
adopted". For an extension with several clauses (SM:334) it reads "assumed as a hypothesis of this
extension and not adopted; the measure clause is a condition on a law … counting law".

At SM:252 the lemma opens "Let $\mu$ be the invariant measure — the selected counting measure of [Main]
Lemma 3, or a stated structured prior, or, on $\mathbb{Z}^d$, a law …", so that the assumed law is not
called "selected" (amendment A1-2).

**Finite-only scope** of a recurrence-cycle statement: "on a finite representative" (C8, C17, C19).

## 3. Propagation (§A.25, §A.14)

Re-grep on this branch:

- **Return form** ("has no finite-window test"): 15 occurrences.
  - Main 5 (:131, :141, :180, :224, :724).
  - SM 1 (:44), GR 2 (:138, :589), Substratum 1 (:92).
  - ch01 2 (:121, :179), appC 1 (:104), FULL 3 (:454, :512, :6259).
- **Law form** ("do not distinguish it from a finite carrier's counting law"): 7 occurrences.
  - Main 2 (:280, :766), SM 3 (:122, :252, :334).
  - appB 1 (:46), FULL 1 (:5723).
- **Lines with "(NR)" or "near-return" and no return form.** Four remain:
  - M:60 and M:732 item (ii), which are S2-B sites;
  - ch01:284 = FULL:617, the NR-1 citation, a negative result that uses no (NR) hypothesis.

  Meth, ch18 and glossary:105 carry their own wording and are S2-E's Q3 sites.
- **Book mirrors.** ch01:121/161/179, appC:104 and appB:46 are byte-identical to FULL:454/494/512/6259/5723.
- **No book mirror** for the edited M:141, :180, :224, :724, :766, :159 and :732 (iv), SM:122, :252,
  :334, or Str:1224. The distinctive-phrase grep at the base found one occurrence of each.
- **Not edited.** M:224's mention of (IP) is a pointer to §3.2's remark, which carries both parts, and
  LEDGER §3.1 does not list it.

## 4. Build, coverage and checks

- `sh ./build.sh Main SM GR Substratum Structure` and `sh ./build.sh --book`: build OK, no dropped glyphs.

  | Artifact | Pages (base → branch) | Median characters per page (base → branch) |
  |---|---|---|
  | Main | 106 → 107 | 3338 → 3317 |
  | SM | 148 → 148 | 3153 → 3144 |
  | GR | 84 → 84 | 3178 → 3185 |
  | Substratum | 53 → 54 | 3240 → 3190 |
  | Structure | 94 → 94 | 2908 → 2914 |
  | book | 489 → 489 | 2998 → 2997 |

- `python3 tools/coverage_check.py`: OK (132 canonical statements) after three re-affirmations in
  `verification/coverage/LEDGER.json`:
  - the area-law lemma, `SM:L-unnamed-ff7b7d06` → `SM:L-unnamed-675607a6` (its id is derived from its
    fingerprint), fingerprint `675607a6c305eeb8`;
  - Lemma 1c, fingerprint `242ff16786e66342` (after amendment A1-2), with its assumptions field naming the H-μ(φ,Θ) law on
    ℤ^d;
  - Proposition 4b, fingerprint `e7cb872ef111a22a`.

  Levels and deltas are unchanged.
- `tools/lean_manuscript_census.py` OK; `tools/artifact_placement_check.py` OK.
- `tools/legacy_records_check.py`: the self-test passed. The check itself was undecidable because the
  local clone is shallow, so it is left to CI.
- Register scan of the added text (§A.32, §A.33): no revision-history words, no reader instructions, no
  capitals for emphasis.
- `ledger_check.py check` (for information; the ledger is reconciled after Step 2): PIN MISMATCH, as
  expected. The rebuilt map has one site that the committed map lacks, `papers/SM.md:122`. The law form's
  phrase "a finite carrier's counting law" matches the extended criterion-5 scan there. The other
  sites where the law form was added were already mapped. The reconciliation maps SM:122 to X-41.

## 5. Overlaps with parallel units (for landing)

- **M:732.** S2-B (#1473) edits item (ii) of the same line; this unit edits clause (iv) only (C9). A
  line conflict is expected and is resolved by keeping both.
- **Sub:92.** S2-B rewrites this line but keeps its (NR) sentence. When it lands, C16's appended
  sentence goes after S2-B's text.
- **M:766.** S2-D edits Main §4.6. This unit appends one sentence after the statement of (IL).
- **appB.** S2-B edits appB:92 = FULL:5769; this unit edits appB:46 = FULL:5723.
- **Main line numbers.** S2-B shifts the Main lines after 334 by +4.
- **Wording difference with S2-B.**
  - S2-B's X-50 sentence at its Main:336 reads "for the selected update on $\mathbb{Z}^d$" without
    "of §3.2".
  - Its appB Theorem B.2.5 carries only the first clause of the return form.

  Harmonizing these is for the coordinator. The pointer "of §3.2" is needed for accuracy, not only for
  grammar: under NR-1 Prop. 5.1, a nilpotent coupling coefficient α makes the Bernoulli law satisfy (NR),
  so the sentence would be false for "the selected update on ℤ^d" without a pin. Main §3.2's instance
  (q = 2, α = 1) is covered by NR-1 Prop. 2.3, where (NR) fails under the Haar product law. The ledger's
  queued X-20 wordings carry the same unpinned phrase and the superseded "the only laws known …" clause;
  both are for the reconciliation.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| PR #1473 (S2-B) and its diff | "X-50 is handled by S2-B"; the overlap notes | provenance: no manuscript claim of this unit uses its content |
| #1169 comment 7056875845 | authorization | provenance (owner record, quoted) |

All support (the A1-EXIT ledger, O-A4, NR-1, Phase 2) is on `main` at the base.

## 7. Verification status (§A.46 item 4)

- **Verified by the writer.**
  - The splices match the preregistration byte for byte.
  - The builds, coverage and census pass.
  - The mirrors are identical.
- **Missing.** A delta review of the amendment A1 edits at this head.
- **Accountable Issue.** #1169. The regression audit is #1468.
- **What resolves it.** An accepting review on PR #1474, then the ledger reconciliation after Step 2,
  then a separate owner merge decision.

## 8. Review round 1 (`05d2ab4f`, ACCEPT-WITH-NITS)

The record is on #1474. As directed by the coordinator, this unit applied N1, N2, N3, N5 and N7 by
amendment A1 (`amendments/A1.md`, pushed before the edits), skipped N4, N6 and N8, and records N6 and N8
here.

- **N1 (applied, A1-1).** Every one of the 15 return-form sites reads "no law that is not supported on
  periodic configurations is known to satisfy it", and the superseded phrase has no occurrences. The
  sites are:
  - Main 5;
  - SM 1, GR 2, Substratum 1;
  - ch01 2, appC 1, FULL 3.

  The wording rests on NR-1 Prop. 2.3. No law satisfying the root-shared (NR) is on record.
- **N2 (applied).** The accuracy reason for "of §3.2" is in §5.
- **N3 (applied).** The naming of R1 is in §1, in the R1 row.
- **N4 (skipped).** M:224's "(IP)" stays a pointer to §3.2's remark.
- **N5 (applied, A1-2).** At SM:252, "the invariant measure — the selected counting measure …".
- **N6 (recorded for reconciliation).** SM:122 and SM:252 write H-$\mu(\varphi,\Theta)$, and Θ also
  denotes time reversal at SM:647. The reconciliation, or a later unit, may rename the reversal symbol
  in the hypothesis label.
- **N7 (applied, A1-3).** At ch01:179 = FULL:512 the return form is in parentheses, as at appC:104.
- **N8 (recorded for reconciliation).** SM:150 is a pointer to the area law. It is out of scope for
  this unit.

**After A1.**
- **Builds.** All builds pass with no dropped glyphs:

  | Artifact | Pages | Median characters per page |
  |---|---|---|
  | Main | 107 | 3317 |
  | SM | 148 | 3144 |
  | GR | 84 | 3185 |
  | Substratum | 54 | 3190 |
  | book | 489 | 2997 |

- **Coverage.** `coverage_check` reports OK after the Lemma 1c fingerprint was re-affirmed
  (`711478cf44840d32` → `242ff16786e66342`).
- **Mirrors.** ch01:121/179 and appC:104 are byte-identical to FULL:454/512/6259.

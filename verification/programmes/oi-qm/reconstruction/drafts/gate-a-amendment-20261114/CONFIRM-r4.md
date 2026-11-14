# Closing focused confirmation of the Gate A amendment r4 at an exact head

**This is a model review of the text at the head below.** It is a non-author, paper-only review:
reading, `git diff`, `diff`, grep and hand reasoning. It is not independent verification, not a
human review and not an owner decision. Nothing was computed on OI models, no Lean was built, and
nothing in the repository or on GitHub was edited or posted.

**Head.** Branch `research/gate-a-amendment-1169-20261114`, commit
`eb5151504d0514c4690c2b0a7972293119d9a800` (draft PR #1289).
- `git rev-parse HEAD` returns that SHA, and `git status --porcelain` is empty.
- Its parent is `cea2691261f14272221c14f7819f0d62df71584a`. The chain back to `main` at `c3b5f37a`
  is `eb515150` ← `cea26912` ← `ae2de57a` ← `65b0a929` ← `c3b5f37a`.
- No file outside `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/`
  differs from `c3b5f37a`. The `oi-qm-ext-1/` folder, which holds `endpoints.md`, is unchanged.

`r4:n` is line n of `GATE-A-AMEND-r4.md`, `OQ4:n` is line n of `OWNER-QUESTIONS-r4.md`, and `EP:n`
is line n of `endpoints.md`, blob `d9d92e03`.

## Overall verdict: ACCEPT

`GATE-A-AMEND-r4.md` and `OWNER-QUESTIONS-r4.md` are accepted as the final text of this amendment
cycle. No change to either file is required.

One sentence of `README.md` is inaccurate at this head (question 5). `README.md` is a record file,
not amendment text, and it has to be updated in any case to record this review. The exact
replacement is given under question 5.

Acceptance here means the text is internally consistent, faithful to its sources and within the
authorization. It proves no obligation, adopts no E or C, and changes no scientific status.

| Question | Verdict |
| --- | --- |
| 1. RC1–RC4 and the owner-questions correction applied as described | Yes. The modified RC1(c) is right on its merits |
| 2(a). One consistent domain and meaning for C | Yes |
| 2(b). Necessity uses the full equivalence; "answers itself" is conditional | Yes |
| 3. Contract preserved; anti-fitting openings closed; no new opening | Yes |
| 4. O6 and O7 applied accurately; the four questions correct | Yes |
| 5. Earlier files byte-identical; README account accurate | Files: yes. README: accurate except one sentence |
| 6. New claim, status or scope discrepancy | None |

## 1. The required changes of CONFIRM-r3

`git diff cea26912 eb515150` shows four files:
- added: `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md` and `RESPONSE-CONFIRM-r3.md`;
- modified: `README.md`.

Every hunk of `diff GATE-A-AMEND-r3.md GATE-A-AMEND-r4.md` is accounted for below. There is no
hunk outside this table.

| Hunk in r4 | Change | Source |
| --- | --- | --- |
| r4:1, r4:5–12 | Title; status paragraph (r3 confirmed at `65b0a929`, r4 unreviewed, r3 trace stands) | Housekeeping. Accurate at this head |
| r4:78–86 | Fam(M) and ≃ defined | RC1(a), verbatim |
| r4:220–224 | "Type and domain of C"; one meaning of C(M) | RC1(b), verbatim |
| r4:228 | C-law row | RC1(c), modified in its last clause |
| r4:229 | C-model row | RC2(b), verbatim |
| r4:237–244 | C-1 exclusions | RC3(a), verbatim |
| r4:258–261 | C-1 to C-3 applied to conditions in E | RC3(b), verbatim |
| r4:279–280 | S-A gives M ≃ T | RC1(d), verbatim |
| r4:296–309 | S⇐ᴺ with antecedent ≃ and the invariance condition | RC2(a), verbatim |
| r4:320–321 | Meaning of "satisfies C" on `J_Bell` | RC1(e), verbatim |
| r4:324–327 | B⇐ requires membership in `M(E, J_Bell(A₁, A₂))` | RC4, verbatim |
| r4:370, r4:373–377 | R1 heading and text | RC2(c), verbatim; the heading is matched to §5.2 |
| r4:412–421 | §8 items 1 and 2 | RC2(d), verbatim |

Every hunk of `diff OWNER-QUESTIONS-r3.md OWNER-QUESTIONS-r4.md` is also accounted for:
- OQ4:1 and OQ4:3: the file name is updated.
- OQ4:6–13 and OQ4:21–23: RC2(e), verbatim.
- OQ4:35–37: O6.
- OQ4:41: "the reading taken in the amendment".
- OQ4:46–47: O7.

The line references in `RESPONSE-CONFIRM-r3.md` to r4 are correct.

**RC1(c) as modified.** r4:228 ends "so S-A is then an obligation on the admitted class, that is on
E", where CONFIRM-r3 had "on E and 𝔄". The modification is right. S-A quantifies over every member
of `M(E, J_exact(A))` with C(M), and a sector member need not be an instance of 𝔄. Suppose C is a
function of the labelled law alone. Then C cannot separate members that differ only in their
unlabelled procedures, so S-A can hold only through what the admission condition admits. The
rules of 𝔄 bind its instances only, and they cannot secure S-A for the other members. The text of
CONFIRM-r3 was imprecise on this point.

## 2. The two decisive checks

**(a) One domain and one meaning for C.** r4:220–224 fixes the meaning of "C(M)", "M satisfies C"
and "M is inside C". Under C-law it means that Fam(M) satisfies C. Under C-model it means that the
native data of M satisfy C. Fam(M) is defined once (r4:78–83), with its restricted reading tied to
owner question 4. Each use was checked against that definition:
- S⇒ (r4:265–266) and S-A (r4:273–274): "with C(M)".
- S⇐ (r4:286–287): "C(M)".
- S⇐ᴺ (r4:296).
- S-J: stated through `M_C(E, A)`, which is defined from the same predicate (r4:223).
- B: "satisfies C in the sense fixed above", applied to the restriction to `J_exact(A₁ × A₂)`
  (r4:320–321).
- C-4 and C-5: stated through `M_C(E, A)`.

No use departs from the fixed meaning. The conclusion of S-A coincides with the second clause of ≃
(r4:83–85). "Experiment family" therefore has a single sense in the complete reading.

**(b) Necessity and the full equivalence.**
- S⇐ᴺ has antecedent M ≃ T (r4:296).
- ≃ is defined with the comparator's whole domain (every p, π and h of `J_exact(A)`, EP:110) and,
  beyond it, the domain of S-A (r4:85–86).
- The implication from coverage to necessity is conditional on ≃-invariance, for the same A and
  the same T (r4:298–301). Weaker invariances are excluded by name (r4:301–302).

I re-checked the three implications by hand:
- S⇐, S-A and invariance give S⇐ᴺ. For a given T, S⇐ supplies M₀ with C(M₀) and M₀ ≡ T. S-A gives
  M₀ ≃ T. For any M′ ≃ T, invariance gives C(M′).
- A C that is a function of p_M over the whole of `J_exact(A)` is ≃-invariant, because ≃ implies
  ≡.
- S⇐ᴺ with I gives S⇐ when the witnesses of I satisfy ≃.

The statement that owner question 2 "answers itself" is conditional (OQ4:8–13): it holds "only if
C depends on nothing but the statistics of the labelled Gate A experiments, all of them". Otherwise
question 2 stays open, "unless C is shown to give the same answer for any two models fully
equivalent to the same quantum theory". OQ4:21–23, r4:228, r4:373–376 and r4:412–419 agree with
it.

## 3. Preservation and anti-fitting

**Preservation.** r4 changes no line of §3 (residual clause, kept requirements) or §4 (superseded
lines); the diff has no hunk there. `GATE-A-AMEND-r3-TRACE.md` is byte-identical between `cea26912`
and `eb515150`, and r4 cites it (r4:10–11, and the unchanged §3, §4.2 and §6). Its cross-references
("the amendment §5.1", "§5.2", "R4") resolve in r4. The dispositions stand:
- EP:56–59 is superseded.
- The forward half of EP:157 is superseded.
- EP:51 is partly superseded.
- Every other line is kept or record, and the comparator law EP:110 is kept.

**Anti-fitting.** All four openings identified in CONFIRM-r3 are closed.
- The instances of 𝔄 and the S⇐ witnesses (r4:237–238).
- Choice among candidate conditions (r4:241–242).
- Quantum-derived thresholds and data selected for agreement (r4:240–241).
- Folding a condition into E (r4:258–261).

Routes (a) and (b) are closed. C cannot be defined as the image of the inclusion construction, and
its parameters cannot be selected after matching. C-2 and C-3 are unchanged, so the sector
obligation cannot be met by construction while its physical justification is absent.

No new opening is introduced.
- The sentence "a C revised after a comparison is a new condition and meets C-1 to C-5 afresh"
  does not license iterated revision. The revised condition must itself be "stated … before any
  law is compared", must not be chosen according to agreement, and falls under C-2 and C-3. An
  optional clarification is offered in O-a.
- "If a C stated independently coincides with one of the excluded sets, that coincidence is a
  theorem to be proved" keeps the exclusion on the definition and adds a proof burden.
- The clause on E tightens the target and relaxes nothing in EP. EP:102 already requires E to be
  specified independently of the comparator.

## 4. OWNER-QUESTIONS-r4.md

**O6 (OQ4:34–37).** Accurate. #914 c.6875548603 quotes the coordinator's proposal, "**Inclusion:**
every finite quantum experiment is realized by one common OI model", and the owner's reply "Yes
proceed as suggested." The same comment's restatement reads "QM_fin ⟹ OI + E on one common
substratum–observer realization." Both quoted fragments are exact.

**O7 (OQ4:46–47).** Accurate. #1169 c.6703342848 reads "The accepted Gate A contract already
requires … It requires both target coverage and a quantum counterpart for every behavior admitted
by the physical OI interface."

**The four questions.**
- Question 1 gives two options, with the regime note and the conditional link to question 2.
- Question 2 states both answers with what each commits to, and correctly says that no owner
  record states the "yes" form.
- Question 3 states both readings with their commitments. Each is attributed to its record.
- Question 4 states both readings and quotes the recorded positions neutrally.

All four state their options and commitments correctly. The quotations at OQ4:7, OQ4:15,
OQ4:31–32, OQ4:45, OQ4:46–47 and OQ4:47–48 are exact.

## 5. Earlier files and the README

**Files.** `git diff --quiet cea26912 eb515150` reports no difference for any of the eleven earlier
files:

- `CONFIRM-r2.md`, `CONFIRM-r3.md`, `REVIEW-r1.md`, `RESPONSE-r1.md`, `NOTES-r1.md`
- `GATE-A-AMEND-r1.md`, `GATE-A-AMEND-r2.md`, `GATE-A-AMEND-r3.md`
- `GATE-A-AMEND-r2-TRACE.md`, `GATE-A-AMEND-r3-TRACE.md`
- `OWNER-QUESTIONS-r3.md`

Only `README.md` is modified.

For the record, `CONFIRM-r3.md` in the branch differs from the reviewer's working copy in two
ways. One word is replaced twice in the byte-identity paragraph, and a coordinator's note is
appended that says so. Both were made at `cea26912`, before the range examined here. The note is
accurate.

**README.** Its account of r4 (lines 47–51) is accurate, except for the clause "the other six are
not applied". CONFIRM-r3's O1 concerned the README sentence "The owner confirmed in the
coordinating session that both paper-only units of that day were authorized and may continue."
That sentence was removed at `ae2de57a`, so O1 has been acted on.

**Record correction to `README.md` (not a change to the amendment text).** Replace lines 47–51
with:

> - r4 applies RC1–RC4 and the owner-questions correction, RC1(c) in modified form
>   (`RESPONSE-CONFIRM-r3.md`). No trace disposition changes, and every earlier file is unchanged. Of
>   the confirmation's eight optional suggestions, three are acted on by the coordinator: the
>   unrecorded owner-confirmation sentence of this README is removed (O1), and the two on
>   attribution are applied in `OWNER-QUESTIONS-r4.md` (O6, O7). The other five are not applied.
> - `CONFIRM-r4.md` confirmed r4 at `eb515150`: ACCEPT. `GATE-A-AMEND-r4.md` and
>   `OWNER-QUESTIONS-r4.md` are accepted as the final text of this amendment cycle, with no change
>   to either.

Add a matching row for `CONFIRM-r4.md` to the contents table.

## 6. New claim, status or scope

None found. The additions in r4 are definitions (Fam, ≃, the meaning of C(M)), conditions on a
future C or E, and conditional logical statements, each checked above. No result is claimed, and no
E or C is proposed or adopted. No status of an existing result changes, and the status table stands
unchanged in the r3 trace. No interface beyond `J_exact(A)` is typed. The status paragraph
(r4:7–12) describes r4 as unreviewed, which was accurate when it was written.

## 7. Optional suggestions (none required)

- **O-a, r4:242–243.** For readers who might take "meets C-1 to C-5 afresh" as permitting revision
  toward agreement, the sentence could read: "a C revised after a comparison is a new condition: it
  meets C-1 to C-5 afresh, its revision is justified independently of that comparison's outcome,
  and the earlier comparison is not evidence for it."
- **O-b, `README.md`:21.** The trace's dispositions are "kept, record, superseded or partly
  superseded", not "(kept, superseded or replaced)". This is CONFIRM-r3's O2, still open.
- **O-c, `RESPONSE-CONFIRM-r3.md`:24 and :36–42.** "The file is 46 lines", "None of O1–O8 is
  applied" and the references OQ4:34–35 and OQ4:43–45 describe the files before the coordinator
  applied O6 and O7. The file is 48 lines at this head. A one-line coordinator's note at the end of
  that file, as was done for `CONFIRM-r3.md`, would reconcile it with the README.
- **O-d, OQ4:15–16 and OQ4:26.** CONFIRM-r3's O4 ("C can then be read physically") and O5 ("only
  coverage is required") remain open. They are wording points, not errors.
- **O-e, OQ4:47.** One line is unwrapped. This is cosmetic.

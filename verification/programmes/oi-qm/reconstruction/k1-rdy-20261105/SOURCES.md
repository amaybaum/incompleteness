# K1-RDY recovered preregistration: sources, concordance and open points

**Status: WIP / UNVERIFIED. Not frozen.** This ledger serves the independent review that #1031 c.6649482038
requires. It decides nothing. "Line N" means line N of `PREREG-RECOVERED.md` in this directory.

## 1. Provenance

**The recovered text.** `PREREG-RECOVERED.md` is lines 5 to 317 of the body of #1031 comment **6567522034**
(amaybaum, 2026-11-02T02:20:43Z), "K1-RDY record, 1 of 2: decision-complete preregistration (verbatim; sha256 prefix
`a93f3f33f0c5a6e8`). Not frozen." Lines 1 to 4 of the comment are its record header, a blank line, a `***` rule and a
blank line. Lines 318 onward are a blank line and the comment footer. The 313 lines are joined with LF and end in one LF.
No byte is added, removed or changed.

**Digest recipe** (§A.42 item 1). Run at this file's commit on this branch:

```sh
sha256sum verification/programmes/oi-qm/reconstruction/k1-rdy-20261105/PREREG-RECOVERED.md
```

Expected: `a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`, 313 lines. The same digest results from
the comment body as the GitHub API returns it, using lines 5 to 317 as above. The prefix equals the one recorded in
c.6567522034's header and in #1031 c.6567502036's table.

**The review record.** #1031 comment **6567537517** (2026-11-02T02:22:00Z). Its body lines 5 to 182 (178 lines, LF,
final LF) hash to `fa6c9e0430d4adf2b4466d6f90f55d774234bdaaa1b044b22c83c393684c8812`, which matches the recorded prefix
`fa6c9e0430d4adf2`. It is not copied here; it stays on #1031.

**What was run.** Only the integrity checks above: a sha256 of text and line counts. These are not scientific
computations. No hand check, enumeration, model calculation, Lean or workflow was run. No statement in the text was
re-derived.

**Search for other copies.**
- `git log --all -S` over the repository's 310 remote branches, for the strings `POS-X`, `CC-PASS`, `CC-T2`, `W_ct`,
  `k1rdy`, `G2(b)` and `CC-IMP″`, finds nothing. `K1-RDY` finds only O-RET's `SOURCES.md` (`ff4d4beb`, `29ec36be`).
  This agrees with c.6649454594's branch search.
- Earlier revisions of the preregistration are not retained anywhere found: r1 (275 lines, the review's first pass)
  and r2 (312 lines, the final check, diffed against `PREREG.r1.md`).
- Also verbatim on GitHub, with recorded digests that the posted bodies match:
  - the K1-RDY *proposal* r3 that the text cites as its technical source: #914 c.6564008455 (321 lines,
    `6ef06b1695d02a14…`);
  - that proposal's review: #914 c.6564018307 (147 lines, `74e4ead9793c6870…`).

## 2. Why the posted text is identified with the accepted r3

1. **The gate record** (#1031 c.6567502036, 02:19:04Z) lists "Preregistration (313 lines) | `a93f3f33f0c5a6e8` |
   decision-complete; implements K-1–K-18 …, D-07(a), and the owner's O-1/O-2/O-3 decisions". It says the
   preregistration and the review "follow verbatim in the next two comments". They are c.6567522034 and c.6567537517.
2. **The review's Confirmation** accepts "r3 → current, 313 lines". The recovered text has 313 lines.
3. **Concordance** (§3). Every change the Confirmation and the final check record as applied is present. The one change
   the Confirmation offers as optional, and c.6567502036 records as not applied, is absent.
4. **Redaction.** c.6567502036 records one edit before posting: two lines of the *review*. "No other change was made to
   either document."

**Limit.** The reviewer's record names the file (`f2/k1rdy/PREREG.md`) and its line count, not its digest. The digest
was recorded by the coordinating session that posted both records. The identification therefore rests on items 1 to 4,
not on a digest in the reviewer's own hand (ambiguity A-2).

## 3. Concordance: the review record and decisions against the recovered text

Sources: R = review record c.6567537517 (first pass F1–F9 and Q1–Q6; "Final check (r2)"; "Confirmation (r3 →
current)"); G = gate record c.6567502036; K = #914 c.6566997020; I = #1031 body.

### 3.1 Review findings and fixes

| Item | What the record requires or records | Recovered text | In text |
|---|---|---|---|
| F1, CC-PASS | R F1 fix; R final check "F1, landed" | line 213 (fixture, stated image `{x_1+y_1=0, x_0+x_2=0}`, H-sel content `x_1+y_1` in B-pl, none in B-eq) | yes |
| F1, CC-T2 | R F1 fix; landed | line 214 ("differs" disjunct; T1 silent) | yes |
| F1, T1 sentence for §6 constants | R F1 fix; landed | line 130 | yes |
| F1, CC-IMP″ relabelled | R F1 "relabel what it tests"; landed | line 212 (G2(a); T1; T2's no-image disjunct) | yes |
| F1, S0 count eleven | R final check "count of eleven is correct" | line 187; table lines 206–216 hold 11 controls | yes |
| F2, POS-X `Λ` with finite-`S` posit | R F2; final check "F2, landed" | line 215 | yes |
| F2, `Λ` compared as a set | R F2; landed | line 184; line 215 "equal as a set" | yes |
| F3(a), G1 records `NB`, decides nothing | R F3(a); landed | lines 122–124 | yes |
| F3(b), Z1-VOID supersedes; P1 member vs class | R F3(b); landed | lines 136–138; 182–183 | yes |
| F3(c), VOID[row] before BLIND; ABSENT excludes both | R F3(c); landed | lines 142–143; 183 | yes |
| F4, B-ct region | R F4 → O-1; landed "pending O-1", then O-1(b) | lines 44–47; 276; 289–290 | yes (as O-1(b)) |
| F5, "rows fixed in advance", no token values | R F5; landed "without stating any token values" | lines 232–239 | yes |
| R1, P1 class tokens "as not positive" | R final check R1, wording given | line 236, R1's wording verbatim | yes |
| F6, three checkpoints | R F6; landed | lines 267 (isolation), 268 (`W` by rule), 270 (no post-selection, structural) | yes |
| F6, G6 "independently" defined | R F6; landed | lines 151–152 | yes |
| F7, P3 B-pl row flagged | R F7 → O-2 | lines 83–85; 276–277; 291 | yes (as O-2) |
| F8, ceiling order | R final check: "not required before freeze" | line 261 unchanged in form | not applied, as recorded |
| F9(a), CC-LEDGER injected | R final check: cosmetic | line 209 says "a row asserting B-pl sharp readiness" | not applied as a separate change |
| F9(b), §5.3's last sentence | R final check: applied | line 163 | yes |
| F9(c), lexicographic cell order | R final check: "member order does not affect any token" | line 157, order undefined | not applied, as recorded (see A-1) |
| F9(d), §10 fixture list | R final check: applied | lines 283–284 (`E := site 2`, `W_ct`, `{y_4, x_0}`) | yes |
| F9(e), "three words" on D-07(a)'s counting-measure scope | R final check: cosmetic | line 57 cites (K-8, D-07(a)) without the scope words | not applied, as recorded |
| F9(f), held-head drift note | R final check: cosmetic | line 263 records drafting heads only | not applied, as recorded (see P-2) |
| Optional T1 nit, "scalar constants" | R final check: optional; Confirmation: "applied" | line 130 | yes |
| Confirmation (1), §7 "P0 B-ct from POS-X" line removed | R Confirmation | lines 232–236 list P0 B-pl, P0 B-eq, P3, P1 only; line 199–200 "No candidate row uses it" | yes |
| Confirmation optional nit, P0 B-ct under O-1(b) | R Confirmation optional; G point 2 "not applied" | absent from lines 232–236 | not applied, as recorded |
| Confirmation, "no other line changed" | R Confirmation | not checkable without r2's text (A-2) | — |

### 3.2 Owner decisions O-1 to O-3

| Decision | Record | Recovered text |
|---|---|---|
| O-1(b): `W_eq` at `t_u = t_0 − 1`, H-ret and H-2s (declared), never native; non-positive row stands, no switch | R Confirmation "O-1(b) landed with its no-switch safeguard (§2, §11)"; G | lines 44–47 ("no other readout region is substituted"); 276; 289–290 |
| O-2 KEEP: P3 B-pl as starting-measure diagnostic, ledger line kept | R Confirmation; G | lines 83–85; 276–277; 291 |
| O-3 confirmed: Q1 scoping with F3(a)'s precedence; report reporting-only, with checkpoint | R Confirmation; G | lines 122–124; 144–147; 269; 292–293 |

### 3.3 Writer's questions Q1–Q6

| Q | Record | Recovered text |
|---|---|---|
| Q1 | R: sound; owner confirmation is O-3 | lines 122–124; 292–293 |
| Q2 | R: new choice → O-1 | lines 44–47; 289–290 |
| Q3 | R: consistent, H-2s (declared) | lines 57–59; 296–297 |
| Q4 | R: within K-17(a) | lines 156–163; 298 |
| Q5 | R: correct and minimal | lines 50–54; 60–62; 299–300 |
| Q6 | R: needed, see F1 | §3.1, F1 rows |

### 3.4 Owner decisions K-1 to K-18, D-07(a), and the #1031 body

| Source | Content | Recovered text |
|---|---|---|
| K-1, K-2, K-11 | paper-only; separate issue; freeze needs separate authorization | lines 3–5; 186 |
| K-3 | finite tori, `ℤ/q`, unit `a`; no infinite/Haar extrapolation | line 31; 220–221 |
| K-4 | P0 then P1; P2 inside P1; P3 under K-12(b); P4 ineligible | lines 69–76; 78; 92; 279–280 |
| K-5 | Main:62 as H-sel; ceiling RR-AVAILABLE[H-sel] | lines 25–27; 81–82 |
| K-6 | P3 event value-free, configurations not records | lines 79–81; 278 |
| K-7 | sharp decides; weak reported; no TV threshold | lines 24–25; 50–54; 281 |
| K-8, D-07(a) | H-cur declared; H-2s, H-ret conditional | lines 57–59; 282 |
| K-9 | `E` the dependency set, not the backward cone | lines 36–38; 275 |
| K-10 | bounded hand checks for controls only | lines 189–191; 303–313 |
| K-12(b) | `W` = `V`'s site set, both slices; `O` over `[t_u − 2, t_u]`; `t_u = t_0` | lines 43; 78–80; 278 |
| K-13 | `R_E = {0}` | line 39 |
| K-14 | `V ∩ Σ = ∅`; blindness lemma not extended | lines 34; 97–100 |
| K-15 | single use at `t_0` | lines 23–24; 220 |
| K-16(b) | tailoring G2(b); rule not coordinates; ceiling | lines 125–138; 40–41 |
| K-17(a) | all invariant measures incl. `π_0`; no post-selection | lines 72–76; 156–163; 270 |
| K-18(b) | `(1,5,2,1, site 1 current, site 0 both, 1)` | lines 31–34 |
| D-19 | `V ∩ Σ = ∅` (master-matrix question, #914 c.6563412926 line 315, answered by K-14) | line 34 |
| I, "Required next gates" 1 | nits: rule-defined `W`; L-O quantifiers | line 41 ("review nit 1"); line 102 ("review nit 2") |
| I, fixed study choices | instance, priors, G2(b) tailoring, P3 rule, `E`, `R_E`, access, ceiling, single use, hand checks | as the K rows above |

No row of §3 finds a difference between the recovered text and what the records say it carries.

## 4. Items left open before freeze (as recorded; not resolved here)

- **G point 1.** "Distinguishable carrier-dependent records" is read as `V`'s declared readout on `[t_0, t_0+T]` only
  (lines 144–147). The reviewer found this fair and non-filtering. The owner "may want it widened".
- **G point 2 / R Confirmation optional nit.** P0's B-ct row could be added to "Rows fixed in advance". Not applied.
- **F8, F9(a), (c), (e), (f).** Not required before freeze (R final check).

## 5. Points for the independent review

These concern records and rules that post-date the acceptance, or references the text makes. None is resolved here,
and no text is changed for them.

- **P-1 (§A.45, adopted 2026-11-03).** Rule 7 retires the formal holds on #1009, #1023, #1011, #1003 and #918 as a
  scheduling mechanism. Lines 229 and 263, and lines 226–228 on readiness-dependent work, keep the hold wording of
  2026-11-02. #1031's body records the supersession at the planning level. Whether the text needs an
  amendment before freeze is an owner question. An amendment would reopen accepted text.
- **P-2 (held heads; F9(f)).** Read on 2026-11-05 with `git ls-remote`:
  - `refs/pull/1009/head` `d4a80fc8`, 1023 `af1e9be2`, 1011 `947761dd`, 1003 `0efd67a6` and 1025 `e02544d5` equal
    line 263's drafting values;
  - `refs/pull/918/head` is `44236326`, a descendant of the drafting value `fa32b043` (commit of 2026-11-04 22:42 UTC).
  
  #1025 was closed without merge on 2026-11-04 with its branch kept at `e02544d5`, so line 229's "#1025 is untouched"
  still holds of its head.
- **P-3 (§A.42 item 8, §A.46 item 7: references off `main` or unretained).**
  - On `main`: `07d94f2c` and `02009693` (Main, SM); `af1e9be2` (MR★, MR-pre).
  - Off `main`: `e02544d5` (RR, kept branch), used at lines 24, 56 and 181.
  - Not found on any branch: the working records TA, TD, MAP and P2 (line 12), cited at lines 47, 49, 60, 81, 90, 127,
    206, 234 and 243.

  Each reference needs classifying as provenance or support before any landing on `main`. For the review, a writer's
  observation that is not a finding: each fact the gates use from TA or RR appears to be stated in the text itself, so
  those references may classify as provenance. They are the overlap rule (lines 48–49), (c1)/(c2) (lines 60–62), the
  W-certified test (lines 55–56) and `D(μ_O)` from index 8 (lines 88–90). The exceptions are line 206's "TA (c4)" and
  line 234's use of it, which cite `π_0`'s equal-time independence of disjoint cells as a result.
- **P-4 (RR-1 carry-forward; #1025 c.6559037887, `stage1/REVIEW.md` at `e02544d5`).** #1031 c.6625842789
  (2026-11-04) requires any successor readiness test to address these findings. The requirement post-dates the
  acceptance. Writer's mapping, for the reviewer to check:
  - Finding 1 (overlap rule) → K1-RDY states one (lines 48–49) and has no pin-ablation step.
  - Finding 2 (an order the text never names) → the nearest K1-RDY analogue is §5.3's member order (A-1).
  - Findings 3–5 (RR-1 candidates C2–C4) → no counterpart.
  - Finding 6 (`t_u ≤ t_r`) → K1-RDY fixes `t_u` per branch (lines 42–45).
  - Finding 8 (executor member choice) → §5.3 evaluates every member.
  - Finding 9 (token labels) → §5.4's fixed table.
  - Findings 7, 10–12 → specific to RR-1's record.
- **P-5 (c.6567152798).** A coordinating-session paper diagnostic, posted on #1031 at 01:49Z before the preregistration
  record and marked UNREVIEWED, evaluates P3 at the fixed instance. The text discloses that P3's rows follow from its
  image statement (lines 232–235). It does not mention the diagnostic. Line 252's checkpoint covers the *drafting* log
  ("reads and HC-1 only"). Whether the diagnostic bears on that invariant or needs disclosure is for the review.

## 6. Ambiguities

| Id | Where the record underdetermines | Choice made here | Alternatives | Could it change a gate outcome? |
|---|---|---|---|---|
| A-1 | Line 158: the P1 class token is "the first of VOID[row], Z1-VOID, UNDECIDED(Gk), ABSENT, BLIND attained by a member row". "First" may mean first in that list or first in member order (line 157). Member order rests on a cell order that is never defined (F9(c), not applied). | None; the text is recovered as is. The final check reads it as list precedence ("member order does not affect any token"). | Member-order reading. | Under list precedence, no. Under the member-order reading, the *label* of a non-positive P1 class token could depend on the undefined order. The class is not positive under either reading (line 236). This is RR-1's Finding 2 failure mode, so it merits an explicit review ruling. |
| A-2 | The reviewer's record does not carry the accepted text's digest, and r2's text is lost, so "no other line changed" (R Confirmation) cannot be checked line by line. | The posted text is identified with the accepted r3 by §2's chain. | That the posted text differs from the reviewed file. Nothing found supports this. | Only if the texts differ. §3 finds no difference in any item the record names. |
| A-3 | "r3" means two things. The preregistration's revisions are r1 (275), r2 (312) and r3 (313, "current"). Lines 7, 95 and 201 use "r3" for the *proposal* r3 (#914 c.6564008455). The brief's "accepted r3" means the preregistration. | Kept as written. | — | No. |

## 7. Contradictions between sources

- **C-1.** #1031 c.6649454594 states that the accepted text "appears to have been held only in a session's local work
  area. Its content is not retained." #1031's planning block repeats "the accepted r3 text is not retained". c.6567522034
  holds that text verbatim, and its digest matches the recorded one. The branch search in c.6649454594 is correct. Its
  conclusion does not follow from the search, because the Issue's own comments were not covered. Resolving this means
  updating the planning block and choosing between this recovery and the authorized reconstruction. That is for the
  coordinator and the owner. It is not done here.
- No contradiction was found between the review record, the gate record, #914's decisions and the recovered text.

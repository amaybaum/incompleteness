# Independent review of S3-U4 r2 (route M and the parked-record case)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U4-r2.md`
(blob `d8cced4c`) with `RESPONSE-S3-U4-r1.md` (blob `a1ceebbd`), at PR #1294 commit `95c7e066`.
Both blobs are unchanged at the later head `ea1c1b5d`. r1 (`e6d8101a`) is byte-identical at
`3a08a446` and `95c7e066`.

**Reviewer.** A separate, non-author Claude reviewer. Read-only and paper-only: no computation, no
Lean, no manuscript or repository edit, no commit, no GitHub post. Git and the GitHub API were used
only to read files and comments.

**Baseline.** `REVIEW-S3-U4-r1.md` (blob `63c95b30`, 13 findings).

**Inputs checked.**
- `S3-PLAN-r9` §8.4 and §8.6 (SNR-1, gating), and `S3-U1-r5` (G4, AD-1(d), the parked-record clause
  at :570–574).
- `VERIFY-SL3-CC-r2` §§1.3–1.5 (Sup-1 to Sup-3, verdicts, "not verified under the gloss"), and the
  CC4, CC5 and CC7 verdicts (§§3.4, 4.4, 5.4).
- `LIT-ERASER-r3` (blob `2b414173`): §1.7, §1.12, §1.13, C1–C10, §3 and §4.
- `U4-CALC-r2` (blob `bef634e2` at `213e3981`): Theorem 1, Theorem 1′, Props. 1.4–1.6, Instances
  1.1–1.2, Theorem 2, Props. 2.5–2.8, §3 and CALC-F1 to F5. `REVIEW-U4-CALC-r2.md` (ACCEPT).
- Corpus at `75cc5100`:
  - Main:74, :157, :200, :326–328, :439, :588 and :682;
  - Substratum:463, GR:350, SM:252;
  - ch15:156 and :214, ch18:74 and :78;
  - MR★ S-L5 (:584–593), S-L7 (:603–618), C-9 (:1433–1440) and :636–651.
- Owner records #1169 c.6891511297, c.6891710167 and c.6891808569, read through the API. All three
  are by `amaybaum`, and U4's quotations of them are accurate.
- A fresh API search of #1169 comments since 2026-11-15T00:00Z for "explanatory compatib" and
  "independent experimental support". It returned no hit, which confirms U4's statement that no
  comment carrying the refinement exists.

## Verdict: ACCEPT WITH CHANGES

r2 answers all 13 r1 findings in substance:
- PK-4 is correctly withdrawn and restated;
- QM-4 is now a trade-off;
- the compatibility label is removed from the native mechanism;
- the status inputs follow c.6891511297;
- the three cases are kept apart.

D-1 stays undecided at (γ), and nothing counts under SNR-1. The new potential conflict of PK-2 with
Schwindt 1999 and Walborn 2002 Fig. 3 is stated as conditional on (γ), as "potential", and as not
counting. It is not presented as an established conflict.

Six required changes remain. They are small scope and wording repairs, plus an incomplete change
list in the response:
- the conflict is missing one load-bearing condition (R1);
- one CALC citation is stated beyond its hypotheses (R2);
- one QM-4 sentence is false (R3);
- one scope caveat was dropped without being listed (R4);
- the typing of the delayed-choice experiments as Case Pk is unconditional (R5);
- several changes are not listed in the response (R6).

## 1. The r1 findings, one by one

| # | r1 finding | r2 location | Status |
|---|---|---|---|
| 1 | PK-4 / U4-F4 false | §6.1 PK-4 (r2:502–520); U4-F4 (r2:706); AW-U4-1 (r2:517–520) | **RESOLVED.** Bracket `(U_{k−1}(A))_{vw}` re-checked: `δ_{vw}` at `k = 1` reproduces S-L7's second pair (MR★:612–613); `a` at `k = 2` for neighbours. The recovery set is isotropic. "Reading both slices under A-reg removes it" is S-L7's first pair. "Exactly when" is the definition of isotropy for linear readouts, by bilinearity (O7) |
| 2 | QM-4 overstated | QM-4 (r2:568–576); §6.3 (r2:584–588); Englert labelled [LIT: ABSTRACT, theory] (r2:552) | **RESOLVED**, with one new false sentence (R3). `D_whole` and `D_acc` are separated. The cross-tick comparison cites QM-1's invariance. The process reading is taken from LIT C6 |
| 3 | Compatibility label misapplied | §6.3 (r2:601–618); U4-F8 (r2:710); §10 (r2:773–776) | **PARTLY.** The label is correctly confined to class (ii), and the conflict is stated as potential, undecided at (γ) and not counting. The r2 extension needs R1 and R2 |
| 4 | Status inputs out of date | §2.2 (r2:187–227); §4.2 (r2:311–313); §4.3 U row; PK-1 / U4-F10; §6.4 (r2:653–660); owner questions (r2:804) | **RESOLVED.** Each attribution was checked against VER r2: S-L3 for the four bullets, Sup-1 and Sup-2 credited to the record, Sup-3 reflected, and the μ-datum bullet corrected. The CC4, CC5 and CC7 scopes match VER §§3.4, 4.4 and 5.4 verbatim in substance |
| 5 | Two kinds of restoration conflated | §4.2 Route 1 / Route 2 (r2:315–356); U4-F2 | **RESOLVED.** Route 2 is placed as Case S, outside the branch (PLAN §8.4:684–688). "Does not count" is marked as a U4 finding pending owner question 3 (see O4 and O5) |
| 6 | Accessibility reading inconsistent | §6.3 AV-p / AV-t (r2:628–643); owner question 2 | **RESOLVED.** The G4 time index is applied. The Schwindt test is stated "provided an unanalysed polarization counts as unheld" and is carried as conditional in §7 and §10 |
| 7 | "Any eraser phenomenology" | §6.4 (r2:661–664) | **RESOLVED** |
| 8 | Experiment typing | §5 (r2:401–462); raw-direct checks (r2:452–457) | **RESOLVED.** Every type and read status matches LIT §4. The Case Pk typing raises a new point (R5) |
| 9 | C/Q agreement condition | §7 (r2:688–692) | **RESOLVED** |
| 10 | Tier stated favourably | §10 (r2:743–750) | **RESOLVED** |
| 11 | C-9 wording | §2.1 (r2:155–157, 168–170); PK-2 (r2:491–494) | **RESOLVED** for the wording. The scope of the accompanying CALC citation is wrong (R2) |
| 12 | `t = 1` sharpening | §3.2 (r2:253–256); U4-F1 | **RESOLVED** (CALC Prop. 1.4). One slip at r2:255 (O2) |
| 13 | Provenance and minor items | header (r2:44–52, 56–70); §6.1 PK-1 (r2:483–485); §§6.2–6.3 | **RESOLVED.** (a) Not located, and re-confirmed by this review. (b) Re-pinned. (c) R-c and R-b replaced. (d) QM-5 split. (e) Joint statistic. (f) ch18:78 continuation and ch15:156 checked verbatim, with ch15:214 supporting "distinctive among the alternatives". (g) PK-1 scoped |

## 2. r1 against r2: changes not accounted for in the response

The response accounts for the changes driven by the findings, and for the LIT, CALC and three-case
inputs in general terms. The following changes are not listed. They are collected in R6.

1. **New claims.**
   - PK-7, which gives a per-tick Case Pk profile from Theorem 1 and Prop. 1.6.
   - U4-F11.
   - Routing item 2 (r2:787).
2. **Status changed.** §4.3's R row moves from "unsourced" (r1:255) to "single-tick R1 derived under
   strict μ-G for the partition by `q_t`" (r2:370). This is CALC §1.7's [A-inf], so the move is
   sourced, but it changes a U1 outcome and should be listed.
3. **The accepted criterion is restated differently.** U1 r5:573–574 says "A return by recurrence
   (S-L6) is global and lies beyond the budget, so it is not retention". r1:309 carried this. r2:468
   drops "is global and lies beyond the budget" without saying so. CALC AW-1 is a reason to question
   that clause (owner question 1 cites it), but a [P] restatement of an accepted definition should
   quote it as accepted and raise AW-1 separately.
4. **A caveat removed.** PK-6 dropped "Per-law realizations are representable, not available (K-4)"
   and "Whether the K1 step executes such a readback of a which-path record under AD-1 is C-4's trace
   route, undecided" (r1:355–357). See R4.
5. **Other drops.**
   - PK-1's scrambled-return sentence (r1:321–322).
   - §3.1's "S-L5 applies only on the reference class" (r1:163).
   - The c.6890079967 decision-A quotation and its "Not authorized" list (r1:13–17).
   - The OCP input (r1:46).
   - §6.3's backflow sentence citing Main:153.
   - M-8's "needs no §A.29 premise".
   - The #1007 row.

   Each is minor, but none is listed.
6. **New text.**
   - §2.2's AD-1(f) bullet citing CALC AW-1.
   - §4.5's addition of Prop. 2.8(i), and its authorization note (c.6891808569 item 4, verified).
   - §3.3's G1 note (verified).

## 3. Overreach checks

**(β) "generically fails" (r2:274–276; U4-F1).**
- "Holds only where masking is complete" is correct (CALC Theorem 1(b); §3). The listed instances
  of complete masking and of failure match CALC-F2 exactly.
- Two precisions are missing, both optional (O3):
  - Masking is pair-relative. For a given point-path pair the condition is `M_t(x_L − x_R) ∈ K_t`,
    so a pair can be masked where `K_t ≠ R_A`; Instance 1.2's mirror-related pairs are an example.
  - CALC §3 notes that "generic" has no defined sense, since no measure over geometries is on record.
- No overreach.

**PK-4 and S-L7.** Correct, at the scope of linear current-slice reads. The restriction is broken by a
retained conjugate pair, not by parking or recovery. No overreach (O7 is wording only).

**The PK-2 / Prop. 2.8(i) conflict with Schwindt 1999 and Walborn 2002 Fig. 3.** It is stated as
conditional on (γ):
- "if (γ) were supplied";
- "a potential raw-direct conflict, undecided at (γ)";
- "resting on an assumed carrier preparation";
- "does not count";
- routed to the γ plan.

It is not stated as established. Its conditional is missing one load-bearing condition (R1), and its
quiet-marker branch cites a result whose hypotheses exclude it (R2).

**Three-case typing.** Case S, Case Rv and Case Pk are defined and kept apart. No experiment of one
case is used as evidence for another:
- Schwindt's change of wave-plate is excluded from Case Rv (r2:363–364, from LIT C8);
- spin echo is a reversal of a non-record (CC7's class);
- QM-1 states Case S applied after Case Pk.

One typing is stated unconditionally where it depends on an open classification (R5).

## 4. SNR-1

Nothing is counted toward (a′)–(e′), and every negative names the capability that keeps it from
counting:
- (β)–(δ): unsourced retention, and a quiet marker that is assumed;
- the S-L3 branch: CALC Theorem 2 rests on an assumed aperiodic carrier and on S-L2 [NP], and does
  not reach the raw-direct observable;
- the native-marker miss: (γ), T0 and the carrier preparation are unsourced;
- the PK-2 conflict: (γ), the carrier, and the quiet marker are open or assumed;
- (e′): the controls are verified at scope but not run (MR-1 stage 2).

r2:760–762 states the rule explicitly. This check is **satisfied**.

The U1 re-check of S-L3 in §2.2 is author-side. This review read it clause by clause against U1 r5 and
VER r2 and found no gap. AW-1 concerns returns measured from tick 0, not the operation `φ^{N−1}`, and
does not touch S-L3's verified content (see O5).

## 5. Repository text rules

A grep of both files for the repository's banned words, machine-local paths and closing keywords
returned **no hits**. r1's
"state-varying" (r1:274) is correctly rephrased at r2:389.

## 6. Findings

### Required

**R1. The PK-2 conflict needs its fixed-geometry condition.** This affects r2:601–611, U4-F8 and the
§10 routing at r2:794.
- PK-2 and Prop. 2.8(i) say that, *at fixed geometry, tick and background*, no marker declaration
  changes `D`'s law (r1 review table: "Confirmed at fixed geometry").
- The performed data the conflict cites are comparisons across apparatus settings:
  - Schwindt's `V` varies with the marking wave-plate's setting between runs (LIT C8, which U4
    itself quotes at r2:363–364);
  - Walborn's Fig. 3, with the QWPs in, is read against Fig. 2, with the QWPs out (LIT §1.7).
- PK-2 alone does not predict visibility at `D` in any one configuration. Whether `D` shows fringes is
  `D`'s own masking condition `K^D_t`. So a conflict needs (γ) to map the compared runs to K1
  configurations with the same carrier transfer `Φ_{DΣ}` and the same background at `D`. If (γ) maps a
  change of marking setting to a change of geometry, PK-2 is silent and there is no conflict.

*Required change:* state the conflict as conditional on (γ) *and* on that mapping of the compared runs.
Cross-reference §2.1's first scope observation and the routed "mapping of marker coupling and phase
settings" (r2:795–796). Also say that the native-marker part of the tension is §4.1's native-marker
miss branch, which §4.1 finds not reachable.

**R2. Prop. 2.8(i)'s hypothesis is H-μ, not "a product law".** This affects r2:168–170, r2:493–494 and
U4-F3 (r2:705).
- CALC Prop. 2.8 is stated "under H-μ": every non-carrier region uniform and independent
  (CALC :84–89, :421).
- U4 says the result "assumes a product law of the non-carrier regions, independent of the carrier".
  That is broader than CALC proves.
- The difference bears on r2:603. The quiet-marker branch of the conflict ("That holds with a quiet
  marker") is not covered by Prop. 2.8(i), because a quiet marker is not uniform. That branch rests on
  S-L5 [NP] alone, or on a Theorem 1′-type statement at `D` for an arbitrary non-carrier law
  independent of the carrier. U4 would have to state the latter as its own [A-inf], since CALC does not
  state it for `D`.

*Required change:* restate the scope as "under μ-G background (H-μ)", and give the support for the
quiet-marker branch separately.

**R3. QM-4's "It excludes only …" is false (r2:570).** The trade-off excludes every pair with
`V > √(1 − D²)`, for example `D = V = 0.8`. In U4's pure-complement model, which has the equality, it
excludes every pair off the circle. LIT §3 lists this ("generally `V > √(1 − D²)`").

*Required change:* say that it excludes every pair outside the disc. As an exclusion of *any* nonzero
value of the other quantity, it is total only at `D_whole = 1` and at `V = 1`.

**R4. Restore PK-6's availability caveat, or justify removing it (r2:525–530).** r1 carried two
qualifications:
- Main:200's readback is a per-law realization, "representable, not available (K-4)";
- whether K1 executes such a readback of a which-path record under AD-1 is C-4's trace route,
  undecided.

r2 drops both, and the response does not list the drop. Without them, PK-6's [M] heading ("parking and
return is Main's hidden-memory readback") reads closer to an available native mechanism than the source
supports (available → derived). The other half of the r1 review's point is kept ("a (γ)-type step").

*Required change:* restore the two qualifications, or give the reason for dropping them in the
response.

**R5. Make the Case Pk typing of the delayed-choice experiments conditional (r2:440–446; U4-F6).**
- The owner's Case Pk is "recovering a record after a period of *inaccessibility*" (c.6891710167).
- LIT C2 and C4 record only that the record is held in an *unread* degree of freedom (a photon in
  flight) and is later made accessible by projective detection.
- LIT C5 leaves open whether an unread degree of freedom that is readable in principle counts as
  inaccessible or unheld, as "an OI-side definitional matter". U4 itself puts that classification to
  the owner as question 2.
- r2:443 nonetheless says that the experiments "realize the period of inaccessibility", and U4-F6 is
  classed CONFIRMING.

*Required change:* state the typing under the same proviso as AV-t, namely if an unread in-flight
photon counts as unheld or inaccessible under U1 G4 (owner question 2). Otherwise use LIT's word,
"unread".

**R6. Complete the response's change list** with the items of §2 above. For item 3, quote U1's
parked-record clause verbatim in §6 and keep the AW-1 doubt in owner question 1.

### Optional

- **O1 (nit, stale status).** CALC r2 is now ACCEPT at `213e3981` (`REVIEW-U4-CALC-r2.md`). Update
  "not yet re-reviewed" or "unreviewed" at r2:12, :65–69, :91–92, :722 and :760–762 (the CALC part),
  and in the response at :13–14.
- **O2.** r2:255, "r1's coset statement is therefore exact", should read "the PLAN §8.4 sentence is
  exact at `t ≤ 1`" (CALC Prop. 1.4). The coset statement was exact at every tick.
- **O3.** Add the pair-relative condition and CALC's "generic has no defined sense" at r2:274 and in
  U4-F1.
- **O4.** Route 1's heading "(Case Rv, and K1's only counterpart of it)" (r2:315) is an unlabelled
  [A-inf]. Label it and narrow it to "the counterpart considered here". Also name the μ-G background
  in the T3 bullet, since CALC-F5 makes the negative specific to it.
- **O5.** r2:354–355, "and not S-L3's standing": the U1 re-check it relies on is author-side (§2.2).
  This review finds no gap in it. Cite the review once it is accepted, or say "not S-L3's standing
  alone".
- **O6.** "Relative to a `μ`-datum" (r2:216–217, §4.3 U row, U4-F10) is U4's reading of Sup-3, which VER
  states for a fixed content of the complement. Label it [A-inf] where it carries [V].
- **O7.** PK-4's "exactly when" is definitional (isotropy of a set of linear readouts is the vanishing
  of every pairwise bracket). Scope it to held linear readouts.
- **O8.** Main:326–328 is the diagonal-preservation lemma. It does not state that an available copy is a
  permutation (§4.4, carried unchanged from PLAN §8.3). The sentence already calls this "a property of
  the definition".
- **O9.** U4-F8's class "NEW" is a correction prompted by review. ELABORATING, or a correction note,
  would fit §A.31 better.

## 7. Checked and not checked

**Checked:**
- every r1 finding against r2's text;
- the full r1 → r2 content by section;
- r1's immutability, and the blob pins of LIT, CALC and the r1 review;
- all owner quotations against the comments themselves;
- every corpus line listed under Inputs;
- every CALC result U4 cites, against CALC's own statements and hypotheses;
- every LIT attribution in §§4.2, 5 and 6.2–6.3, against LIT;
- VER's Sup-3, its verdict scopes and its "not verified" list;
- the bracket algebra of PK-4, by hand;
- SNR-1 and the gating;
- the text-rule grep.

**Not checked:**
- the external literature itself (LIT is accepted);
- CALC's proofs beyond what REVIEW-U4-CALC-r1 and r2 confirm;
- U2, U3, GAMMA-G1 and the σ12 screen;
- SEL-EXCL-1 at `0ecfddeb`, which is off `main`;
- INV beyond the items cited.

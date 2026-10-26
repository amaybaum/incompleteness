# Independent re-check: PR #937, 6f257cda..4fe0ebff

This is a read-only, diff-only re-check of `4fe0ebff` ("apply the review's corrections and the owner's decisions on the
counts"), against `S/cc2/DIFF-REVIEW.md` and the owner's decisions of 2026-10-26:
- the headline is 2 + 5;
- S is read relative to Tier 2;
- R3(a): G1 and G3 are retired, and G2 is kept.

How the checks ran:
- Every check used `git show` / `git archive` snapshots (`S/cc2/review2/regen2`).
- No worktree was created and nothing was committed.
- Every git command ran with `-c gc.auto=0 -c maintenance.auto=false`.
- Python ran with `python3 -I`.
- `4fe0ebff`'s parent is `6f257cda`, whose parent is `22cb6da0`. `6f257cda` adds only the review record.

## Verdict: REVISE (four small mechanical fixes, exact text below)

R1–R5 and R3(a) are applied as specified. The departures are acceptable. Mirrors, artifacts and all checks pass.

Three things remain:
- **Two stale counts.** One count was introduced by this commit (F1). The other is an untouched inventory carrying the
  same two consistency rows that this PR removed elsewhere under owner item 2 (F2).
- **A numeric change not propagated.** The Koide Q match was changed at two sites and left at seven (F3).
- **The ch06:196 defect.** It must be fixed now (F4).

With F1–F4 applied verbatim, the verdict is **ACCEPT**. F5–F7 are nits.

***

## 1. R1–R5 applied?

| Item | Applied | Notes |
|---|---|---|
| R1 "unconditional" | ✓ | No headline "unconditional" remains (grep of papers/ and book/; the 13 residual "unconditional" hits are unrelated uses, plus Juno:59, which already pairs the unconditional geometry with the hypothesis-level identification). Scope sentences landed at SM:1255 and SM:1298 (verbatim), SM:1426, ch04:132, ch04:142 and ch04:204. Acceptable extensions of the scope rule: appendix-a:28/:42 (S definition), ch04:42, ch06:318, and the ch04:132 heading "(structural)". |
| R2 SM:1310 | ✓ verbatim | |
| R3(a) | ✓, except F1 and F2 | See §2. |
| R4 | ✓ verbatim | ch09:63, GR:454, Explainer:699 |
| R5a ch06:179 | ✓ verbatim | Assert-then-qualify removed. |
| R5b ch00:77 | ✓ verbatim | Also applied at glossary:97, which is correct, but see F3. |
| Record fixes | ✓ | REVIEW.md line 9 fixed; CHANGE-NOTE updated (§9) |

## 2. R3(a) completeness

**Done:**
- G1 and G3 are deleted from A.4.2.
- The IDs are not reused, successors are not renumbered, and the gap is not annotated. The table starts at G2. No
  manuscript reference to the G1/G3 *rows* remains; the many "G1"/"G3" hits are the GR dependency-ladder rungs, a
  different label family.
- A.4.2 reads "6 C + 2 L. Total: 8." Recount: G2, G5, G6, G9, G11, G13 C; G8, G12 L = 8 ✓.
- "ten gravitational" → "eight" at every source site (appendix-a:8, :225; appendix-c:8, :273; preface:7; ch08:272;
  ch09:8, :325; ch17:234; ch18:335; ch19:362) and their 11 FULL mirrors. 0 stale "ten gravitational".
- ch07 table: 10 rows; ch07:321 "ten entries" ✓.
- GR §7.4: 6 rows ✓.
- The calibration is stated as a self-consistency condition at appendix-a:117, ch07:36, ch07:305 and GR:551, consistent
  with GR:310 and GR:358.
- G2 is kept, per the owner.

**Not done:**
- **F1:** appendix-a:225 still says "three consistency relations".
- **F2:** ch09's Tier 1 inventory still counts the two consistency rows.

## 3. Propagation sites

| Site | Review |
|---|---|
| **Substratum Class B restructure** | Correct and now identical in membership to ch04 Class B: B-S {A}; B-C {λ, θ₀}; B-L {m_d/m_s, m_u/m_d, m_b/m_τ, sin²θ₁₂, sin²θ₂₃, a₀} = 6; B-M 2; B-R 2; total 13 ✓. The 1/4 moved to a consistency-relation paragraph after the summary ✓. The removed "empirical match holds for all 14 within ~1% or ~1σ" was an overclaim, so removing it is correct. Membership changed: the old Substratum B-S was {λ, m_d/m_s, θ₀, sin²θ₁₃}, not ch04's {λ, A, m_d/m_s, θ₀}. Adopting ch04's membership is an acceptable §A.25 alignment. Nits F5 and F6. |
| **Juno:395, :417** | Correct: sin²θ₁₃ is Layer 1 conditional through λ. The citation "[18, §7.1]" follows Juno's existing convention. Juno:59 is consistent (geometry unconditional, identification hypothesis). Juno:401 "Koide θ₀ (0.02%)" is θ₀'s figure, correct as written. |
| glossary:97 | Q figure corrected ✓ (see F3) |
| appendix-a:28, :30, :42 | S definition scoped to Tier 2; the calibration dropped from the C examples (no longer counted) ✓ |
| Medicine:554 | CC made conditional; the hierarchy clause is left, being deferred ✓ |
| ch04:42, ch06:318, ch06:196 | Scope ✓; ch06:196 see F4 |
| ch07:36, ch07:106 | Calibration "fixes only ε/√σ", per GR:310 ✓; 1/4 "a consistency relation …, not a counted Class B prediction" ✓ |

## 4. ch06:196 — fix now (F4)

**The sentence at 4fe0ebff:** "the Koide relation $Q = 2/3$ is Class B-C Layer 1 from the cubic-group Casimir
$C_2(T_1)/d^2 = 2/9$; the phase input $\theta_0 = 2/9$ is Class B-C Layer 1 from the same Casimir structure, … both are
conditional on the dynamical closure of the Koide amplitude, whose value $A^2 = C_2$ is not yet derived from the
dynamics."

**Why the error is wrong.** $C_2/d^2 = 2/9$ is θ₀'s formula. Q follows from $Q = \tfrac13 + \tfrac{A^2}{6}$ with
$A^2 = C_2(T_1) = 2$ (SM:895).

**Why it is exposed by this PR, not merely pre-existing.**
- The error itself is pre-existing; it was in `687e885b` with "B-S".
- But this PR edited the sentence twice: the class, and then the appended clause.
- The appended clause names $A^2 = C_2$ as the quantity Q is conditional on. The edited sentence therefore now derives
  Q from $C_2/d^2$ and makes it conditional on $A^2 = C_2$ in the same breath. That is the R5b situation, fixed for the
  same reason.

**Replacement:**
> "the Koide relation $Q = \tfrac13 + \tfrac{A^2}{6} = 2/3$ is Class B-C Layer 1 from the cubic-group Casimir through
> the amplitude $A^2 = C_2(T_1) = 2$; the phase input $\theta_0 = C_2(T_1)/d^2 = 2/9$ is Class B-C Layer 1 from the same
> Casimir structure, with the amplitude prefactor computed equal to one (SM §7.2); both are conditional on the dynamical
> closure of the Koide amplitude, whose value $A^2 = C_2$ is not yet derived from the dynamics."

Mirror the change in FULL.

**Can be deferred.** The drafter's noticed ch06:205 ("$Q = 2/3$ from $C_2(T_1)/d^2$") was not edited by this PR.

## 5. Mechanical checks (all pass)

- **FULL mirror.** The FULL diff equals the union of the chapter diffs as multisets (41/41 added, 45/45 removed).
  `mirror_check`: 0 absent.
- **.tex.** The `source-sha256` stamps match their `.md` for GR, SM, Substratum, Structure, Explainer, Juno, Medicine and
  FULL. Every changed `.md` has a changed `.tex`. Regenerated with pandoc 3.1.3 and the shared header, Juno.tex,
  Substratum.tex, Medicine.tex and FULL.tex are **byte-identical** to the committed files.
- **.pdf.** All eight rebuilt. Page counts are unchanged except Juno, 21 → 22. That is text growth: the Juno.tex diff is
  only the two edited paragraphs, reflowed.
- **Repo checks on the snapshot:** `claims_check` OK, `voice_check` OK (40 files), `duplicate_check` OK,
  `mirror_check` 0.
- **§A.32/§A.33 scan of added text:** no history phrases, no caps emphasis, no meta-commentary.
- **Assert-then-qualify:** none new.
- **Recounts:**
  - SM: 2 S + 5 C + 6 L + 3 R + 2 E + 3 M + 1 P = 22.
  - A.4.1: 3 S + 7 C + … = 23.
  - A.4.2: 6 C + 2 L = 8.
  - A.4.3: 1 S + 1 C + 5 L.
  - Class B: ch04 = Substratum = 13 (1 + 2 + 6 + 2 + 2).
  - ch06 Class: 3 S + 6 C.
  - ch07 table: 10.
  - GR §7.4: 6.
  - GR:358: 5.
  - All match their stated totals.

***

## 6. Findings

**Required:**

1. **F1. appendix-a:225 [FULL:5764], stale count introduced here.**
   - "with three consistency relations stated beside them" → "with four consistency or descriptive relations stated
     beside them".
   - This matches A.4.2's paragraph "Four gravitational-sector results are consistency or descriptive relations".
2. **F2. ch09 Tier 1 inventory still counts the two consistency rows** that owner item 2 removed from the ch07 and
   GR §7.4 tables in this PR. Edit ch09 [FULL mirrors]:
   - delete the rows `| $S = A/(4 l_p^2)$ | conditional on H-slope; no direct test | Ch 7 §7.5 |` and
     `| CC dissolution (descriptive) | … | Ch 7 §7.7 |` (ch09:124, :126);
   - ch09:132: "Seven universality-class entries tested against current empirical evidence: one confirmed at high
     precision (the area law), the $1/4$ coefficient without a direct test and conditional on H-slope, and the remainder
     consistent with the empirical record at concordance level (the descriptive dissolution, information preservation,
     dark sector budget, no DM particle, no proton decay)." → "Five universality-class entries tested against current
     empirical evidence: one confirmed at high precision (the area law) and the remainder consistent with the empirical
     record at concordance level (information preservation, dark sector budget, no DM particle, no proton decay). The
     Bekenstein-Hawking coefficient and the descriptive vacuum-energy distinction are consistency relations
     (Chapter 7 §7.10) and are not tabulated.";
   - ch09:179: "Tier 1 has seven entries: the area theorem is measured, the conditional entropy coefficient has no
     direct test, and the remaining entries" → "Tier 1 has five entries: the area theorem is measured, and the remaining
     entries";
   - ch09:181: "The three tiers contain twenty-two entries" → "The three tiers contain twenty entries".
3. **F3. Koide Q match figure changed at two sites, left at seven (§A.25 numeric propagation).**
   - The figure was changed at ch00:77 and glossary:97.
   - Observed Q from the PDG lepton masses is 0.666661 ± 0.000007, i.e. 0.0009% from 2/3 (I re-derived it). The "0.02%"
     is θ₀'s figure.
   - Several of these sites are sentences this PR already edited: appendix-a:79's class, appendix-a:98's "23", and
     Structure:56.
   - Changes [and FULL mirrors]:
     - appendix-a:79: `| **0.02%** |` → `| **<0.001%** |`;
     - appendix-a:98: "Koide $Q = 2/3$ at **0.02%**" → "Koide $Q = 2/3$ to better than **0.001%**";
     - appendix-a:211: "Koide $Q$ at 0.02%" → "Koide $Q$ to better than 0.001%";
     - appendix-a:215: "Koide $Q = 2/3$ at 0.02% (entry 10)" → "Koide $Q = 2/3$ to better than 0.001% (entry 10)";
     - ch09:169: `| Koide relation $Q = 2/3$ | $0.02\%$ |` → `| Koide relation $Q = 2/3$ | $<0.001\%$ |`;
     - Structure:56: "the Koide ratio $2/3$ matching at 0.02%" → "the Koide ratio $2/3$ matching to better than 0.001%";
     - Structure:940: "Confirmed at $0.02\%$" → "Confirmed to better than $0.001\%$".
   - Leave the θ₀ "0.02%" sites (SM:14, Juno:401, ch06 table θ₀, Substratum θ₀ bullet) as they are. The SM-table θ₀
     "0.001%" disagreement is pre-existing and deferred.
4. **F4. ch06:196 [FULL].** Replace as in §4.

**Nits (non-blocking):**

5. **F5. Substratum B-S falsification clause applied to A.** "A move outside $3\sigma$ on precision upgrade falsifies
   the framework directly with no recoverable error mode" now governs only Wolfenstein A. SM:865 says the A comparison
   carries an open O(λ²) correction and that "A global-fit A drifting outside √(2/3)(1 ± λ²) would strain the
   leading-order identification". Suggested: "A global-fit $A$ outside $\sqrt{2/3}\,(1 \pm \lambda^2)$ would strain the
   leading-order identification, while the protected $\sin\theta_{13} = A^2\lambda$ comparison tests the geometry
   directly ([SM §7.1])." The same clause in ch04:132 is pre-existing.
6. **F6. Substratum, sin²θ₁₃'s place in Class B.** The PMNS bullet says it "inherits the Cabibbo λ and is conditional
   with it", but it is in no counted sub-class. Suggested: append "(class C in [SM §7.6]; not counted separately in
   Class B, as in Chapter 4)". ch04 omits it too, so the counts are consistent.
7. **F7. Noticed, deferrable:**
   - ch06:205 Q-from-$C_2/d^2$ (not edited);
   - SM table θ₀ 0.001% vs ch06 table 0.02%;
   - ch04:142 "in honest summary" (book register; exempt from §A.32).

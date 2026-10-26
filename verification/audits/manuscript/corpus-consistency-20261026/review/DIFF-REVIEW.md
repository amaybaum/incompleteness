# Independent review: PR #937 manuscript edits (head 22cb6da0)

Reviewer: independent of the drafter. I also reviewed the audit (S/cc2/REVIEW.md, committed as the record's `REVIEW.md`).
Read-only: nothing in the repository was edited, committed or pushed.
- Every git command ran with `-c gc.auto=0 -c maintenance.auto=false`.
- No git worktree was created. Checks ran on a `git archive` snapshot of `22cb6da0`, at `S/cc2/review2/tree`, and on
  `git show` extracts.
- Python ran with `python3 -I`.

Object: `20ceef33` (corrections) → `a40d8830` (merge of main `17b830bc`, #936) → `22cb6da0` (five follow-ups).
Edits reviewed as `git diff 17b830bc 22cb6da0`.

## Verdict: ACCEPT WITH CHANGES

Most of the work is accurate and mechanically clean:
- the mirrors are exact;
- the generated artifacts are current;
- the merge is faithful;
- #936's text is intact;
- the deferred items are untouched.

Five required changes (R1–R5) remain. None needs new analysis; each has exact text below.
- **R1.** The new headline word "unconditional" is contradicted by the corpus itself, at about 30 sites.
- **R2.** One edited SM sentence classifies the Wolfenstein-A family as C, while A stays S.
- **R3.** The gravitational count removes the 1/4 as a consistency relation. It keeps the ħ/ε calibration that the PR's own
  GR:358 now calls the same consistency relation.
- **R4.** Two cosmological-constant "dissolves" sites and one ħ overclaim were missed.
- **R5.** Two small defects were introduced inside edited sentences: an assert-then-qualify at ch06:179, and a wrong
  Koide match figure at ch00:77.

One owner confirmation is needed: the headline "two + five" departs from the owner's literal "four + three". It is the
correct result of the "same standard" audit the owner asked for.

***

## 1. Mechanical checks (all pass)

| Check | Result |
|---|---|
| Merge faithfulness | sha256 of the sorted ± line sets (`*.md *.py *.json`): `687e885b..20ceef33` = `17b830bc..a40d8830` = `6dd14525…8e70` |
| Overlap with #936 | `20ceef33`'s changed lines ∩ #936's changed lines (`687e885b..17b830bc`): **0**, adjacent: **0** |
| Follow-up commit | `a40d8830..22cb6da0` touches README:64, ch07:12, ch07:110, ch18:146, ch18:158, their FULL mirrors, the book .tex/.pdf and CHANGE-NOTE only. Word diff: only the quoted 1/4 / CC fragments change. #936's H-scramble, H-decouple, full-product-space, cycle-averaged and "(the 1/4 coefficient itself has no direct test)" text is intact. |
| FULL mirror | FULL diff added/removed lines = union of the chapter diffs as multisets (114 = 114 added, 126 = 126 removed). `mirror_check.py`: 0 absent. |
| Generated .tex | The `source-sha256` stamps match their `.md` for GR, SM, Substratum, Structure, Explainer, Methodology and FULL. I regenerated GR.tex, SM.tex and FULL.tex with pandoc 3.1.3 and the shared header: **byte-identical** to the committed files. Main, Complexity and Juno are untouched. |
| Repo checks on the snapshot | `claims_check` OK; `voice_check` OK (40 files); `duplicate_check` OK; `mirror_check` 0 |
| Added-text scan | No history phrases (now / no longer / formerly / previously / earlier / withdrawn), no caps emphasis (§A.27/§A.30/§A.33) |
| Retired IDs | G4, G7, G14 and F5 deleted. No reuse, no renumbering, no gap annotation. No manuscript reference to G4/G7/G14/F5/"entry 24" remains (the other "G7"/"F5" hits are V3-protocol labels) |
| Deferred items | Main:726/740/666, Substratum:56/350/356, Complexity:204, Explainer:930/671, ch02:196, ch19:64/116/118/333/336/339, GR:709, glossary:103 are all byte-identical to `17b830bc` |

## 2. Recounts (all match the edited totals)

| Inventory | Recount from table at 22cb6da0 | Stated |
|---|---|---|
| SM §7.6 | 2 S (A, λ(M_Pl)) + 5 C (λ, \|V_cb\|, Q, θ₀, sin²θ₁₃) + 6 L + 3 R + 2 E + 3 M + 1 P = 22 | ✓ (SM:1298; SM:1300 2 + 5 + 6 = 13) |
| A.4.1 | 3 S (1, 6, 22) + 7 C (2, 5, 7, 10, 11, 13, 23) + 8 L + 1 M + 2 R + 2 E = 23 | ✓ (:94) |
| A.4.2 | 8 C (G1, G2, G3, G5, G6, G9, G11, G13) + 2 L (G8, G12) = 10 | ✓ (:117), but see R3 |
| A.4.3 | 1 S (N5) + 1 C (N2) + 5 L = 7 | ✓ (:137) |
| ch04 Class B | 1 B-S + 2 B-C + 6 B-L + 2 B-M + 2 B-R = 13 | ✓ (ch04:142) |
| ch06 table (24 rows) | Class 3 S (1/α₀, A, λ(M_Pl)) + 6 C (A·B + five); Category columns unchanged | ✓ |
| ch07 table | 12 rows | ✓ (ch07:323 "twelve") |
| GR §7.4 table | 8 rows | ✓ (see R3) |
| GR:358 | (5), (6), (7), (9), (11) = 5 | ✓ arithmetic. Not re-audited: the mutual independence of (6), (9) and (11), all of which use a₀ = cH/6. |
| ch18:335 (was :349) | 2 + 5; ten entries; G6, G8 measured, G12 bounds | ✓ |
| ch19:362, preface, appendix-c:8, ch08:272, ch09:8/:325, ch17:234 | "ten gravitational" | ✓ |

Re-grep at head (papers/ and book/ chapters):
- "seven parameter-free", "thirteen gravitational", "recovered as a prediction", "F5", "never enters the stress",
  "eliminates the 122", "precisely observed", "derivable quantity", "becomes a derivation", "independent reason to
  expect": all 0.
- The surviving "thirteen", "fourteen" and "seven independent" hits are other counts: ch04:128 LIV orders; SM:1310
  "thirteen observable entries" (S + C + L, correct); ch06:332 Category A; ch09:158; Explainer:769.

***

## 3. Adjudication of the coordinator's points

### Point 1 — Koide, and whether Wolfenstein A and λ(M_Pl) = 0 stay S

**Koide → C is correct.**
- SM:895 states that the amplitude A² = C₂ is "not yet derived from the dynamics", with one loop giving 0.34.
- SM:849 ranks Cabibbo's open link as not on the same footing.
- Keeping Koide at S while Cabibbo went to C would have inverted the ranking.

**A and λ(M_Pl) = 0 do not have open links of their own at leading order, but neither is "unconditional".**
- **Wolfenstein A.**
  - The value is a fixed lattice angle (SM:857, :865). The open items are:
    - the O(λ²) correction to the *measured* A, "observed, not derived" (SM:865);
    - the cluster magnitude normalization ("conditional only on the substrate criterion", SM:928). SM:928 lists A in
      that cluster, but A's value does not use the PT normalization.
  - The identification "the CKM mixing is driven by the perpendicular component" (SM:855) is asserted, not argued. The
    corpus does not grade it as a hypothesis, unlike Cabibbo's (SM:849).
  - Under the drafter's stated rule (an open link the corpus states, at leading order, specific to the entry), A stays
    S. I agree, with the SM:855 and SM:928 caveats recorded.
- **λ(M_Pl) = 0.**
  - It rests on the Higgs as the composite singlet-taste scalar. Theorem 11 (SM:462) is a *consistency* theorem that
    takes the Higgs doublet "as phenomenological input". Its proof uses "Theorem 9a, under H-spin'", and H-spin' is open
    (SM:450, :1302).
  - The matching scale is a convention, μ = M_Pl versus 1/ε = M_Pl/(2√σ) (SM:1112, GR:310). The σ-dependence is
    negligible for σ = O(1), because β_λ ≈ 0 near M_Pl, but it is not negligible for σ ≪ 1.
  - The H-spin' dependence is the same standing Tier-2 condition that SM:32 places under *all* downstream SM
    calculations ("results *on that branch*"). It is not a link specific to this entry. So, relative to Tier 2,
    λ(M_Pl) = 0 stays S.

**The consequence is R1.**
- Both entries stay S *relative to the Tier-2 chain*, which every matter-sector entry, Cabibbo included, shares.
- The word "unconditional" is therefore false for every S entry:
  - SM:32 says so;
  - Theorem 11's proof says so;
  - ch00:77's own last sentence says so ("the matter sector's physical reading under H-spin'"), in the same paragraph
    that now says "two as unconditional".
- If "unconditional" is kept in the AGENTS "all links Solid" sense, the S count is 0, not 2.

### Point 2 — Is G7 a consistency identity?

**Yes; removing it from the count is justified.**
- G7's quantitative content, ρ_QFT/ρ_crit ~ S_dS, holds for any theory with a Planck cutoff and a Hubble-scale density,
  up to 1/(96π²) to 8/3 (my REVIEW 2.7, re-derived). That makes it a Consistency result, not a prediction.
- Its qualitative content, the level distinction, is descriptive, and no measurement compares with it.
- Recommended, not required: the A.4.2 paragraph calls all three "consistency relations" but then calls G7
  "descriptive". Title it **"Consistency and descriptive relations."** and open it "Three gravitational-sector results
  are consistency or descriptive relations rather than predictions…".

**The same rule was not applied to G1 and G3 (R3).**
- GR:310: ε = 2√σ l_p "is algebraically equivalent to the formula for ħ … a self-consistency condition, not an
  independent determination".
- The PR's own GR:358 now reads "items (2) and (3) are one consistency relation with no direct test". Item (2) is
  ħ = c³ε²/(4Gσ) (G3, with G1 equivalent to it); item (3) is the 1/4 (G4).
- The CHANGE-NOTE (§5) itself calls it "the ħ calibration identity".
- G4 left the count while G1 and G3, the same relation, stay in as two conditional predictions. GR §7.4 still tabulates
  ħ and ε as "structural" matches.

### Point 3 — Counts

All recounts match the edited totals (§2). R3 would change A.4.2, ch07 and GR §7.4 again.

### Point 4 — Replacements against REVIEW.md
- REVIEW's wording is used faithfully at 1.5, 1.6, 1.7, 3.1 (placeholder resolved), 3.3, 3.6 (appendix-c:273), echoes and
  ch19:38.
- No retired ID is annotated or renumbered.
- No §A.27/§A.30 self-narration in the added text.

The nine departures (CHANGE-NOTE §3):

| # | Departure | Review |
|---|---|---|
| 1 | "retrodiction" for "postdiction" (appendix-a:74) | Accept: the appendix's own vocabulary |
| 2 | GR:320 cites Bekenstein (1973) and Hawking (1975) in prose | Accept. Now that #936 has landed, *recommended*: numbered GR references (next free numbers after #936's [61]). The bibliography entries (book) are correct (PRD 7, 2333; CMP 43, 199) and in alphabetical order |
| 3 | ch18:349 / appendix-c:273 adapted to ten entries | Accept |
| 4 | ch19:28 keeps the (T) clause on the quantum side | Accept. *Recommended*: align the term with GR:358's new wording, "with the consequences collected in [GR §6.2] — five mutually independent comparisons with data, several conditional on G3, …" (ch19:28 says "consistency relations", GR:358 now "comparisons with data") |
| 5 | ch19:38 lead also made non-assertive | Accept: needed to avoid assert-then-qualify |
| 6 | GR:603 adapted ("On this argument … no echo amplitude is derived"; numerical clause removed) | Accept: §A.42-consistent narrowing per the owner's item 3 |
| 7 | ch00:89 "… and the named hypotheses of each chapter" | Accept (a₀ clause deferred per owner) |
| 8 | Rewrite rather than delete at GR:162 / ch07:63 / Explainer:477, :1043 | Accept |
| 9 | Additions beyond REVIEW | Accept all (point 5) |

### Point 5 — Extra sites
- **CC conditionality, all in scope and correct:**
  - GR:362 (same inference as GR:583);
  - GR:587 heading;
  - SM:1534;
  - Structure:975;
  - glossary:51;
  - ch09:259 (repeated GR:583's INCORRECT "nothing physical was there"; now correct).
- **1/4:**
  - Methodology:21 (in scope, correct);
  - ch03:118 removal, justified by GR:30 (the 1/4 is universality-class level). *Recommended*: apply the same reasoning
    to ch03:42, which still lists "the Bekenstein-Hawking 1/4 factor as a consistency relation" among *Level D*
    content. New text: delete ", the Bekenstein-Hawking $1/4$ factor as a consistency relation" from that list.
- **λ inheritance** (SM:1010, :1296, :1341; appendix-a:139; ch06:267; ch08:138): correct and in scope.
- **ch04 m_d/m_s B-S → B-L:** correct (SM table class L).
- **§A.33 removals** (ch06:179, SM:1426 "v1.9.5"): correct.
- **ch00:77, 2/9 → 2/3:** correct. The observed 0.666661 is Q. But see R5b: the same sentence still quotes "a 0.02%
  match", which is θ₀'s figure; Q matches to 0.00085% (0.8σ).

### Point 6 — Follow-ups F1–F5′
All five keep #936's merged wording intact (§1). Each is a correct application of 1.1, 1.3, 2.3 and 2.7.

### Point 7 — Mirrors, .tex, deferred items
All pass (§1).

***

## 4. Required changes

### R1 — "unconditional" overclaims the two S entries (≈ 30 sites + FULL mirrors)

**Evidence.**
- SM:32: downstream SM calculations "are results *on that branch*" of the conditional Tier-2 chain (H-link, H-spin',
  H-χ').
- SM:462: Theorem 11's proof is "under H-spin'", and the Higgs doublet is "taken as phenomenological input".
- ch00:77 (same paragraph): "the matter sector's physical reading under H-spin'".

The PR inserted "unconditional" into the headline at every site that previously read "seven parameter-free
structural". That turns a pre-existing SM:1298 overclaim into a corpus-wide one. Keep the S/C distinction the owner
asked for, without the word.

**Mechanical substitutions** (sources and FULL alike):
- "two unconditional and five conditional parameter-free structural" → "two parameter-free structural and five
  conditional structural". Sites: ch00:97, ch02:228, ch03:42, ch04:204 ("two unconditional and five conditional
  structural entries" → "two structural and five conditional structural entries"), ch05:13, ch05:196, ch08:272, ch09:8,
  ch09:231, ch09:325, ch17:234, ch19:362, appendix-c:8, appendix-c:273, ch07:8, Explainer:679, :862, Structure:197,
  :944, Substratum:198, :228, ch00:89, Explainer:858 (here "two are unconditional and five conditional parameter-free
  structural retrodictions" → "two are parameter-free structural and five conditional structural retrodictions").
- ch00:21 and preface:7: "two as unconditional parameter-free structural retrodictions and five as conditional ones" /
  "two of the Standard Model set as unconditional parameter-free retrodictions and five as conditional ones" → "two as
  parameter-free structural retrodictions and five as conditional structural ones" / "two of the Standard Model set as
  parameter-free structural retrodictions and five as conditional structural ones".
- ch00:77: "two as unconditional parameter-free structural retrodictions, five as conditional ones" → "two as
  parameter-free structural retrodictions, five as conditional structural ones".
- appendix-a:94: "*two* unconditional and *five* conditional parameter-free structural predictions" → "*two*
  parameter-free structural and *five* conditional structural predictions".
- appendix-a:227 and ch18:335: "two are unconditional parameter-free structural retrodictions, five are conditional
  structural retrodictions" / "two are unconditional parameter-free structural retrodictions and five are conditional
  ones" → "two are parameter-free structural retrodictions, five are conditional structural retrodictions" / "two are
  parameter-free structural retrodictions and five are conditional structural ones".

**SM text:**
- **SM:1298:** "**2 are unconditional parameter-free structural predictions** (**S**, Layer 1: Wolfenstein $A$ and
  $\lambda(M_{\text{Pl}}) = 0$)" → "**2 are parameter-free structural predictions with no open link of their own**
  (**S**, Layer 1: Wolfenstein $A$ and $\lambda(M_{\text{Pl}}) = 0$)".
- **Add after the C clause:** "Both classes are assigned on the conditional physical-carrier chain of Tier 2 (H-spin'
  and H-χ' for the matter-sector reading), which every matter-sector entry shares."
- **SM:1255 legend:** "**S** = parameter-free structural (no fitted input; …" → "**S** = parameter-free structural (no
  fitted input and no open link specific to the entry; …".
- **SM:1426:** "items marked **S** are unconditional structural (Layer 0 or Layer 1, fully derived)" → "items marked
  **S** are structural with no open link specific to the entry (Layer 0 or Layer 1)".

**ch04:**
- **ch04:132:** "These are layer-0 or layer-1 retrodictions with no open assumptions in their derivation." → "These are
  layer-0 or layer-1 retrodictions with no open link specific to the entry; like every Class B entry they rest on the
  matter-sector hypotheses H-spin' and H-χ'."
- **ch04:142:** "one prediction is unconditional structural (B-S)" → "one prediction is structural with no open link of
  its own (B-S)".

**Owner alternative.** If the owner wants "unconditional" in the AGENTS "all links Solid" sense, the S count is 0, with
all seven entries C. In that case the headline is "seven conditional parameter-free structural". The text above is the
minimal accurate version of the drafter's result.

### R2 — SM:1310 classifies the A family as C

- The edit appended "until that closure both are classified **C** in §7.6".
- The same sentence groups Wolfenstein A with the Cabibbo family ("the same one-loop lattice integral structure
  (Cabibbo λ, Wolfenstein A, |V_cb|, m_d/m_s)"), and A remains **S**.
- **New:** replace "; until that closure both are classified **C** in §7.6." with "; until that closure the entries that
  carry these links — the Cabibbo $\lambda$ with $|V_{cb}|$ and $\sin^2\theta_{13}$, and Koide $Q$ and $\theta_0$ — are
  classified **C** in §7.6."

### R3 — The ħ/ε calibration is the consistency relation the 1/4 was removed for

**Evidence.**
- GR:310: "a self-consistency condition, not an independent determination".
- The PR's GR:358: "items (2) and (3) are one consistency relation with no direct test".
- CHANGE-NOTE §5: "the ħ calibration identity".

Apply owner item 2 uniformly. Option (a) is recommended. Option (b) is the minimum consistent alternative, if the owner
wants the calibration inventoried.

**(a) Move G1 and G3 out of the count.**
- **appendix-a A.4.2:**
  - delete the G1 and G3 rows;
  - summary "Counts: 8 C + 2 L. Total: 10." → "Counts: 6 C + 2 L. Total: 8.";
  - consistency paragraph, "Three gravitational-sector results are consistency relations rather than predictions" →
    "Four gravitational-sector results are consistency or descriptive relations rather than predictions";
  - prepend: "The horizon calibration — the discreteness scale $\epsilon = 2\sqrt{\sigma}\,l_p$ and the action scale
    $\hbar = c^3\epsilon^2/(4G\sigma)$, algebraically one relation — is a self-consistency condition that fixes only
    $\epsilon/\sqrt{\sigma} = 2\,l_p$, not an independent determination (Ch 7 §7.3–§7.4)."
- **IDs.** G1 and G3 are retired by §A.30: not reused, successors not renumbered, gap not annotated.
- **Propagate "ten gravitational" → "eight gravitational"** at every site the PR set to "ten": appendix-a:8, :227;
  preface:7; appendix-c:8, :273; ch08:272; ch09:8, :325; ch17:234; ch18:335; ch19:362; plus FULL.
- **ch07 table:** move the ħ and ε rows into the consistency sentence after the table; ch07:323 "twelve" → "ten".
- **GR §7.4:** move the "Emergent action scale" and "Discreteness scale" rows into the consistency sentence after the
  table ("Two further horizon results" → "Three further horizon results", adding: "the calibration $\hbar = c^3
  \epsilon^2/(4G\sigma)$, equivalently $\epsilon = 2\sqrt{\sigma}\,l_p$, a self-consistency condition fixing only
  $\epsilon/\sqrt{\sigma}$ (§4)").
- **G2** ($S_{\rm dS}\sim10^{122}$, "order-of-magnitude estimate") is the 1/4 formula evaluated at the measured Hubble
  radius. It is the owner's call whether it follows. If it does, the count is 5 C + 2 L = 7.

**(b) Keep them, stated honestly.**
- A.4.2 summary: append "G1 and G3 are one self-consistency condition of the horizon calibration (Ch 7 §7.4), counted
  here as calibration entries; the coefficient they fix is listed among the consistency relations below."
- GR §7.4: the "Match" cells for ħ and ε, "structural" → "calibration (§4)".

### R4 — Missed sites and one retained overclaim

- **ch09:63 [FULL mirror].** "The cosmological constant dissolution is determined at the structural-properties level:
  the two-level description of the framework dissolves the conventional discrepancy regardless of the specific
  bijection." → "The descriptive distinction behind the proposed cosmological constant dissolution is determined at the
  structural-properties level, regardless of the specific bijection; the dissolution itself is conditional on the
  coupling step that [GR §6.2] leaves open."
- **GR:454.** "conditional on the same geometry-first ordering that dissolves the CC problem in §6.2" → "conditional on
  the same geometry-first ordering that underlies the conditional dissolution of the CC problem in §6.2". Rebuild GR.
- **Explainer:699.** "it reproduces the Bekenstein-Hawking $1/4$ factor and the value of $\hbar$ as consistency relations
  of its horizon calibration" → "it reproduces the Bekenstein-Hawking $1/4$ factor as a consistency relation of its
  horizon calibration, which relates $\hbar$ to the discreteness scale". The value of ħ is not reproduced: GR:310, and
  AUDIT/REVIEW 1.6. Rebuild Explainer.

### R5 — Two defects inside edited sentences

**(a) ch06:179 [FULL].** The edit created assert-then-qualify (§A.30): "The $1/d$ amplitude is therefore forced by the
framework's structural commitments rather than chosen empirically. The Koide prediction is Class B-C, Layer 1: the
magnitude normalization is conditional on the substrate-eigenvalue criterion …". Replace these two sentences with:

> "The $1/d$ amplitude is therefore fixed by the framework's structural commitments rather than chosen empirically,
> conditional on the substrate-eigenvalue criterion that selects a loop without a time direction (below). The Koide
> prediction is Class B-C, Layer 1, because the Koide amplitude $A^2 = C_2$ is not yet derived from the dynamics
> (SM §7.2)."

**(b) ch00:77 [FULL 313].**
- The value was corrected to 2/3, but "a $0.02\%$ match" is θ₀'s figure.
- (2/3 − 0.666661)/(2/3) = 8.5×10⁻⁶ ≈ 0.00085%; the pull is 0.81σ against ±0.000007.
- **New:** "the observed value is $0.666661 \pm 0.000007$, a match to better than $0.001\%$ ($0.8\sigma$)."

***

## 5. Recommended (non-blocking)

- **GR:320:** numbered references for Bekenstein (1973) and Hawking (1975), now that #936 has landed.
- **ch19:28:** align "consistency relations" with GR:358's "five mutually independent comparisons with data".
- **ch03:42:** drop the 1/4 from the Level D list (as at ch03:118).
- **A.4.2 paragraph title:** "Consistency and descriptive relations".
- **Record hygiene.**
  - CHANGE-NOTE line 3 ("head `5221b53e` … They are uncommitted") and §8 ("uncommitted") are stale.
  - CHANGE-NOTE §7: "sin²θ₁₃₂" → "sin²θ₁₂".
  - The committed `REVIEW.md` line 9 reads "`S` = `S`"; make it "`S` is the session scratch directory (absolute prefix
    elided)", as in AUDIT.md.
- **Noticed, outside scope** (add to CHANGE-NOTE §4):
  - glossary:127 and appendix-c:8 call the Rett window a "pre-registered prediction" / "empirically confirmed
    prediction", but preface:7 and appendix-a say it is a retrodiction (Guy et al. 2007 predates the framework);
  - ch09:63 says the a₀ factor 1/6 "arises from the cubic-lattice geometry", but G6 says "factor imported" (deferred
    a₀ item);
  - SM:928 opens "remains an open task" and later says "has now been computed … discharged" (pre-existing §A.30/§A.33);
  - SM:1100 "The Higgs is the $A_1$ taste" vs Theorem 11's E projection (wording);
  - Koide/θ₀ match figures disagree across SM table, ch06 table, appendix-a:79/:98, ch04:134 and Structure:56 (the
    drafter lists most of these).

## 6. Owner decisions
1. **Headline "two + five" vs the owner's "four + three".** The owner's instruction also said to audit Koide under the
   same standard. Doing so moves Koide Q and θ₀ to C (SM:895), so two + five is the evidence-settled outcome of that
   instruction. Confirm.
2. **R1 alternative:** keep S relative to Tier 2 (the text above), or declare S empty under strict AGENTS.
3. **R3:** option (a) or (b); and whether G2 follows G1/G3.
4. **G7:** removal confirmed on the evidence; no decision needed.

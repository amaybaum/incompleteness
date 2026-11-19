# Review of GAMMA-1 unit G3 r1 (independent, non-author, read-only)

**Object.** `GAMMA-G3-r1.md` on branch `research/ro1-sector-c-1169-20261114` (PR #1294) at
`e4ffa3b50fab4bf52dfd283598679473a1218d4a`, directory
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`; file SHA-256
`0cb8c4ca…e69f`, matching the README row. Cited inputs checked at that commit: `GAMMA-G1-r4.md` blob
`91a5d656` (the same blob as at `6ab9515d` and at the G1 r4 confirmation commit `942f4404`),
`GAMMA-PLAN-r1.md` blob `77f1fcd8`, `LIT-ERASER-r3.md` blob `2b414173`. All three match G3's input list.

**Reviewer.** Claude, a separate non-author agent. No repository edits, commits, pushes or GitHub
writes. GitHub was read through the REST API only: #1305 body; #1169 c.6893331779, c.6893456888 and
c.6893542076.

**Verdict: ACCEPT WITH CHANGES.** No transcribed number was found wrong. Every table row, every quoted
value and every DOI agrees with the source as read. The changes needed are these: one misattributed
cause; a selective quotation; two qualifications in the Grangier thesis that G3 omits, one on the
classical bound and one on the quantum formula; two inconsistencies with G1 r4 (normalization and the
target typing); and a sharper statement of both new markers. None of them needs a new source read
beyond pages already open. G3 draws no verdict on D-1 or (γ).

***

## 1. What was checked, and how

Sources were fetched and read for this review:

| Source | Copy read by the reviewer | Result |
|---|---|---|
| Schwindt, Kwiat, Englert 1999 | arXiv quant-ph/9908072v1, full text | all quotes and numbers verified (§1 of G3) |
| Grangier–Roger–Aspect 1986 (EPL) | IOP article page, abstract | abstract quoted verbatim, verified |
| Grangier 1986 thesis | HAL tel-00009436, 287-page scan; pages read as images: front matter (English abstract, table of contents), pp. 61–62, 78–91 (sampled), 98–110, 140–149 | Tables II-3, II-4, III-2, III-3, Eqs. II-52 to II-58 and III-16 to III-19, and the pp. 98, 104, 141, 144, 147, 149 quotes verified |
| Jacques et al. 2005 | arXiv 2011.12664v1, full text | Table I (all 20 `N_C` and `α`), 1.00 ± 0.06, 0.13 ± 0.01 (95 %), 100 ns gate, 90 %, 444/436 ns, Fig. 4 counts, 88 %, 94 % fit, classical-optics quote all verified |
| Bach et al. 2013 | arXiv 1210.6243v1, full text | dimensions, 600 eV, 230 µm, 1 Hz, 2 h, 2/7/209/1004/6235 verified; one cause misattributed (finding 1) |
| Sorkin 1994 | arXiv gr-qc/9401003v2, full text | lemma, sum-rule wording, footnote, ensemble-frequency quote verified; one verb overstated (finding 9) |
| Sinha et al. 2010 | arXiv 1007.4193v1, full text | Eqs. 4–6, all three `κ` values (0.0119 caption / 0.0120 text discrepancy confirmed), 8 µm, ±3 %, `|κ|` = 0.01, 0.5 %, 0.003, randomized order, 100 runs, 30 million, ~40000 s⁻¹, ~200 fW, < 100,000 s⁻¹, fibre 62.5 µm at ~180 mm, "less than 10⁻²" verified |
| De Raedt, Michielsen, Hess 2012 | arXiv 1112.2665v1 (arXiv comment: "Accepted for publication in Physical Review A") | 0.5 % range, 4 × 10⁻⁵, < 7 × 10⁻⁵, "a factor 100 smaller", the no-theorem and Schrödinger quotes, Fig. 4 dimensions 30 µm / 100 µm verified. arXiv's metadata attaches the PRA DOI to 1103.0121, not to 1112.2665; G3's note on 1103.0121 is accurate |
| Sawant et al. 2014 | arXiv 1308.2022v2, full text | "not exactly equal", "three different boundary conditions", "of the order of 10⁻⁶", the 4 cm microwave case giving 10⁻³, the Sinha-sensitivity sentence, and the Fig. 3 caption (30 µm, 100 µm, 810 nm, 18 cm) verified |
| Eberly, Qian, Vamivakas 2017 | arXiv 1712.10046v1, full text | Eqs. 4, 5, 10 and the Schwarz step verified; see finding 10 |
| Ma et al. 2013 | arXiv 1206.6578v2 | Eq. 3 wording, 98.0 % / 96.9 % without background subtraction, 0.955(7), 0.951(18) verified |
| Tonomura 1989, Arndt 1999 | Crossref JATS abstract; nature.com abstract | both abstracts quoted verbatim, verified |
| All fourteen DOIs | Crossref REST API | titles, authors, volumes, pages and dates agree; no Crossref update or erratum on Sinha 2010 |

**Not reached by the reviewer:** the GRA EPL full text, the Sinha supporting material, the published
versions, Thorn 2004, De Zela 2014, Söllner 2012, Park 2012 and the Kwiat–Schwindt–Englert AIP
proceedings. G3 marks all of these NOT READ or ABSTRACT, and the reviewer did not read them either.

**By-hand arithmetic (reviewer).** Table II-3: `N₁N₂T/N_A` reproduces the printed `N_Class T` to
rounding in every row. The 20 400 s⁻¹ row computes to 201.6 against the printed 204, a 1.2 % gap from
rounded rates in the source. `α = N_cT/N_ClassT` with `Δα = α/√(N_cT)` reproduces the printed
`(1 − α)/Δα` column; the 8 870 s⁻¹ row gives 0.177 ± 0.059. Table II-4 gives ratios between 0.94 and
1.10. Jacques Table I: `α = N_C (t/P)/(N₁N₂)` reproduces the tabulated `α` with `P = 436 ns` for 9 of
the 10 rows checked; row (a)2 matches `P = 444 ns` instead. III-18 at `x = 0.06` gives 0.110, as G3 says.

## 2. Checks requested

1. **Numbers, formulas and attributions.** All verified, with the exceptions in findings 1, 2, 3 and 9.
   - `α_M.Q = x(x+2)/(x+1)²` is printed on p. 149 as III-18, for the interferometer outputs `α̃`. That
     page states its link to Chapter II: "Le but de ces définitions est de conserver à α̃ la même
     expression qu'au Chapitre II en fonction du paramètre x". The Chapter II form, on p. 82 (not read
     by G3), is `α ≅ (2x + x²)/(1 + x)²`, with x given by II-43.
   - The attribution to the GRA source therefore holds. The owner record #1169 c.6893542076 classifies
     it the same way ("the quantum prediction for the Grangier–Roger–Aspect 1986 source").
   - `α_exp = 0.18 ± 0.06` (II-54) is exact as printed.
   - Jacques's α values, Sinha's `|κ|` bound below 10⁻², Sawant's ~10⁻⁶ and De Raedt's 4 × 10⁻⁵ are
     exact as printed.
2. **Read status.** Every status label matches what could be read. One claim reaches past the read
   pages (finding 3). Two statements are G3's own readings but are not labelled as such (findings 1
   and 10).
3. **Finite total substratum.** Nothing in G3 assumes it. G3 uses no recurrence, orbit, period or
   cardinality argument, and it inherits none from G1 into its own claims. This agrees with
   #1169 c.6893456888, under which total finiteness is posit (ii) / A1 and is not an axiom. Pass.
4. **Consistency with G1 r4.** Mostly consistent. There are two inconsistencies (findings 4 and 5) and
   one stale review state (finding 8).
5. **AW-σ and AW-bc.** Both are well-posed as questions. Each needs to be sharpened before G5 relies
   on it (findings 6 and 7).
6. **No verdict on D-1 or (γ).** Pass. Every negative is scoped to "the sources read" or "the version
   read". Every unread capability is marked, so G3 counts no negative under SNR-1. The §6 X-3
   paragraph should be labelled (finding 11).

## 3. Findings

**1. Bach 2013: the cause of the single-slit residual structure is misattributed (medium).**
- G3 §3 says the single-slit patterns show residual double-slit structure "from partial mask
  transmission".
- The source gives a different cause: "Because of the finite separation of the mask and double-slit,
  weak double-slit diffraction can be seen in the negative first order".
- Change: replace G3's cause with the source's. The distinction matters for AW-bc: the source
  attributes the residue to the geometry of the mask, which is the same mechanism Sinha 2010 reports
  (an 8 µm mask offset at 50 µm separation).
- Also label as a reading [A-inf] the clause "each pattern is **separately normalized**". The source
  says only that "the images were summed up by adding each frame's intensity, then normalized"; the
  conclusion that the patterns are separately normalized is the natural reading, but it is a reading.

**2. Schwindt 1999: selective quotation (medium).**
- G3 §1.3 and G3-F2 quote the paper's statement that its count rates are "proportional to the
  intensities of the corresponding classical electromagnetic field". They also quote the clause that a
  Bell violation "implies nothing about … local-hidden-variable theories".
- They omit the sentence that clause qualifies: appropriate measurements "would show that the
  entanglement is indeed so strong that Bell's inequality [30] is violated — clear evidence that a
  description based solely on classical electrodynamics cannot account for all features of our
  experiment".
- They also omit note 14, which says semiclassical models are shown by [13] to fail in some situations.
- The Bell statement is counterfactual ("would show"), so G3's data-side point stands: no such
  measurement is reported. But F2 is a NEW finding whose reading favours the classical side. Under
  §A.31's pressure-test clause, both of the source's statements should be on the record.
- In addition, G3 §5 and F2 call the pure-input source an "attenuated laser". The text says only that
  the "input source, described below, was greatly attenuated", at 670 nm. "Laser 670 nm" appears only
  in Fig. 1(b), the tunable scheme. Say "a 670 nm source", or mark "laser" as [A-inf].

**3. Grangier thesis: two qualifications in the source are omitted (medium).**
- (a) **The classical bound.** G3 §2.2 states that "every semi-classical model gives α_Class ≥ 1
  (pp. 102, 108, Fig. II-18)". That is accurate for those pages. On p. 82, however, the thesis itself
  qualifies the bound: when the gates `w₁`, `w₂` are unequal or offset, "en toute rigueur on aura
  seulement α_Class ≥ (1 − β₁)(1 − β₂)", with `β` "de quelques pour cents". G3 records
  `w₁ = 8.7 ns ≠ w₂ = 9.1 ns` (II-57) but not this consequence.
- The same scope condition applies to G1 §7.2's PC-wave construction, which assumes one field per run
  read through one gate. Change: record the p. 82 qualification, with that page added to the read
  status. Alternatively, state that the bound as used holds for identical gates and that the source
  qualifies it elsewhere. Either way it does not change the size of the violation: 0.18 against about
  0.95.
- (b) **The quantum formula.** Quote p. 149's sentence linking III-18 to Chapter II ("la même
  expression qu'au Chapitre II"), since G3-F3 rests on it. Note that the Chapter II form is stated as
  an approximation (`≅`, p. 82, cf. II-28).
- (c) **Two sources for x.** Table II-2 (p. 99, inside G3's read range) gives x per run directly:
  0.065, 0.125, 0.175, 0.300, 0.540, 0.750 and 1.00. II-58 gives `1.5 × 10⁻⁵ N_A`: 0.071, 0.133,
  0.182, 0.306, 0.548, 0.755 and 1.006. The two differ by up to 8 % at small x. A row-by-row
  comparison with `α_M.Q(x)` needs a declared choice between them. Record both.
- (d) **The headline row.** The "violation maximale" row (8 870 s⁻¹) is selected by the source for
  maximal `(1 − α)/Δα`. Any G5 comparison should use all seven rows, with the trial count. G3 lists
  all seven rows; §6 should say this.

**4. C0's `Δ` from Sinha 2010: normalization and background are stated inconsistently with G1 §5.3
and §5.4 (medium).**
- (a) G3 §6, row C0, gives the gap as "normalization per trigger count (heralded) … not per incident
  particle". Under G1 §5.3, however, per-herald normalization by the herald-executed mass is the
  per-incident-particle normalization whenever a herald process exists. Sinha's heralded runs, with
  30 million triggers per combination, meet it as stated. The laser runs are normalized per
  integration time at a flux assumed constant, and only that half of the gap stands.
- (b) Sinha's `I_AB = p_AB − p_A − p_B + p₀` includes the all-slits-blocked count `p₀`, which Sinha
  identifies as background. G1's `Δ_j = c_{a1} − c_{a2} − c_{a3}` has no such term. A constant
  background cancels in `ε` and in `δ` (the coefficients of each sum to zero), but not in `Δ`: the raw
  `p_AB − p_A − p_B = I_AB − p₀`.
- Change: state the mapping explicitly. Under G1 §5.4, `I_AB` is a background-corrected quantity,
  while `p_AB − p_A − p_B` together with `p₀` added to the model is the raw-direct route. Also say
  that `κ` itself is background-invariant by construction, which supports G3's "derived"
  classification of `κ`.

**5. G1's target typing (§5.4) is not applied to the new data (medium).**
- G1 §12 hands G3 "the target typing (§5.4)". G3 gives each datum its §A.24 class but no §5.4 type.
- The X-1 images are T-sing. The Jacques images are clock-gated, and the heralded Sinha runs are
  conditioned on the trigger.
- The X-2 data fit none of the four types as G1 defines them. They are herald- or clock-gated
  two-detector coincidences, and they are normalizable per herald, because `N_A` and `N_T` are reported
  or derivable, which G1's T-coinc rule says is not the case for coincidence data.
- Change: type each datum, and state that X-2 needs either a fifth type or a declared extension of
  T-coinc. This is an item for G1 or G5, not a G3 decision.

**6. AW-σ is well-posed but incomplete, and its own illustration pre-views an outcome (medium).**
- (a) G1 §5.7 already carries a fallback rule: a stated interval is converted to `σ` "under the
  source's own stated error model; if it cannot be, the target is used qualitatively only". AW-σ
  should say how that rule applies to Sinha. The source states its systematic error as a worst-case
  bound (`|κ|` = 0.01), not as a `σ`, and gives no model for combining it with the random part. The
  open question is whether that case falls under the fallback rule or needs a new rule. It is not a
  wholly unaddressed choice.
- (b) Add a second dimension of ambiguity. Sinha's Fig. 3 caption distinguishes "error bars" (from the
  Allan variance) from "a band of one standard deviation of the distribution of κ values around the
  mean". It is not stated whether the printed `± 0.0018` is the spread of individual `κ` values or the
  uncertainty of the mean. The "about 4σ from 0" in G3-F5 depends on that reading.
- (c) F5 computes a deviation before the rule is settled. The deviation is against 0 and is not a
  comparison under `κ_cmp`. But a resolution of AW-σ chosen after seeing it risks K-2 / NC-γ5.
  Change: state that AW-σ is settled on target-neutral grounds, declared as an instance change with
  its trial count under NC-γ5, and not informed by the 4σ figure.

**7. AW-bc is well-posed in substance; its juxtaposition and scope need care (medium).**
- (a) The two magnitudes come from different idealizations:
  - De Raedt: a two-dimensional FDTD at 405 nm, with a 25 µm iron plate and the blocking mask 50 µm
    away.
  - Sawant: a thin-slit path integral at 810 nm with Sinha's distances.

  So the difference between 4 × 10⁻⁵ and 10⁻⁶ is not a contrast between classical and quantum physics.
  De Raedt states that the same argument "applies to the Schrödinger equation as well". G3 §6 ("~10⁻⁶
  (quantum path integral, Sawant) and ~4 × 10⁻⁵ (classical Maxwell, De Raedt) for Sinha's geometry")
  and F4 invite a reading in which the two numbers would separate PC-wave from the reference. Change:
  say that they are model-dependent estimates of one boundary-value effect, each under its own
  idealization.
- (b) For C0, additivity across slit configurations is an explicit clause of G1 §7.1 (`r_π`
  "independent of whether the other path is open"). AW-bc therefore marks a declared property of C0,
  not a hidden one. For the reference and PC-wave it is implicit, as F4 says.
- (c) State that AW-bc concerns the law-level identities of the reference and the controls. For
  OI's native laws on K1 the same structure is already carried by the O11 stop and H-3. The marker
  cross-references them and does not add a new stop.

**8. Provenance (low).**
- The wave-2 authorization G3 could not locate is #1169 c.6893331779 (`amaybaum`, 2026-11-15T11:00:45Z,
  "Proceed as suggested"). It names "G3: first-hand reading of the X-1 to X-3 sources, Schwindt's raw
  counts and the sources for the quantum reference" and requires that "Each unit gets an independent
  review before it is presented". Cite it.
- §9 row 1 should give G1 r4's own review state: reviewed, with a focused review returning ACCEPT
  WITH CHANGES and the confirmation ACCEPT at `942f4404`. It should not cite only r3's acceptance.

**9. Sorkin 1994: one verb is overstated (low).** G3 says the quadratic form `|X| = I(X, X)/2` "follows"
with `I` bi-additive. The source has bi-additivity on disjoint arguments following from the lemma.
Full bi-additivity holds "supposing such an extension to have been made". The identification
`I(X, X) = 2|X|` is adopted ("If we adopt this"). Self-consistency is from "a short computation which
will appear elsewhere". Replace "follows" with "is obtained under an adopted extension".

**10. Eberly et al. 2017: the appendix is not recorded (low).** The appendix writes the field behind a
polarization analyzer as `F = ŝ · E` and applies (10) to it. That is a classical construction for
analyzer-sorted single-photon visibility, the configuration of Schwindt's sorting eraser (G3 §5,
X-5). It does not derive `K`, so G3's X-4 statement stands. It should be recorded beside §5's X-5
remark, so that G5 does not treat that entry as having no classical construction in the sources read.

**11. Labels in §6 (low).**
- The paragraph "At the stated precision X-3 does not distinguish the idealized reference, these
  corrections, or the linear-regime PC-wave" is a comparison made by hand. Label it [A-inf], for G5 to
  check, consistent with "No entry says that a separation holds".
- The Jacques repetition period: by the reviewer's arithmetic, 436 ns reproduces the tabulated `α` in
  9 of the 10 rows checked. G3 may record this as [A-inf] beside the 444/436 discrepancy.

## 4. What is sound and should be kept

- The read-status discipline: the FULL / SECTIONS / ABSTRACT / NOT READ labels, with the versions
  stated.
- The clear separation of the herald- or clock-conditioned X-2 data from unconditioned data.
- The positive controls on the data side (GRA Table II-4; Jacques (a)).
- G3-F3's correction of the declared X-2 reference to the source-specific `α_M.Q(x)`. It agrees with
  the owner's correction note.
- G3-F1's confirmation that Schwindt reports no Max, Min or signal rate.
- AW-hyb's candidate joint observable, with its values unread.
- The off-`main` trace.

Neither a verdict nor a credit is implied anywhere.

## 5. Disposition

Findings 1 to 7 should be applied before G5 consumes G3; they amount to a short r2. Findings 8 to 11
can be applied with them. None of them changes a number G3 transcribed, and none requires a new
external source: only p. 82 of the thesis, which is already open in the same scan, has to be added.

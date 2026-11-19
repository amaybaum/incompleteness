# REVIEW of LIT-ERASER-r1 (independent, non-author)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/LIT-ERASER-r1.md`
at PR #1294 head `e18126ee4d4605f70ec73628ba9d4ff8b34f8ebb`. Context read: `S3-U4-r1.md` §§4.2, 5,
6.2–6.3; `U4-SOURCES-r1.md` §5 (INV rows); `REVIEW-S3-U4-r1.md` (eraser findings).
**Authorization.** Issue #1169 comment 6891511297, item (2a). Read-only review: no repository edits,
commits, pushes, Issue changes or computation.
**Reviewer.** Claude (independent of the writer). **Date.** 2026-11-15.

## Verdict: ACCEPT WITH CHANGES

Every quotation and number spot-checked against the primary texts is present as stated, the read
statuses are honest, and no invented content was found. The attribution check separates reported
measurements from standard-QM predictions correctly. The required changes are one incorrect
statement in §3 (finding 1), one unlabelled inference (finding 3), and clarifications (findings 2,
4, 5). Findings 6–8 are advisory.

## Findings

**1. §3 "strict inequality for (partially) mixed marker states" is wrong, and the note's own example
contradicts it (required change).** Schwindt et al. write "The equality holds for pure initial states
of the WWM, while the inequality applies to (partially-)mixed states". That is `≤` in general, not
`<`. The note's own hand example (maximally mixed qubit marker, path couplings `(1, 1)`) gives
`D = 0`, `V = 1`, which is equality with a mixed marker. The example itself checks out: for
`ρ = I/2`, couplings `(1, Z)` give conditional marker states `ρ` and `ZρZ = ρ`, so `D = 0`, and
`V = |Tr(Zρ)| = 0`. Couplings `(1, 1)` give `D = 0` and `V = 1`. So the example is correct; the
summary sentence is not. Fix: "equality for a pure marker state; for mixed marker states the
inequality holds, in general strictly". Also, `V² + D² = 2 Tr(ρ²) − 1` is Schwindt's theory curve
for their half-wave-plate coupling, under which a maximally mixed input gives `V = 0` at every
setting (their §II.B). The note already says "for their polarization marker", and that qualifier
must stay.

**2. C6 and §3 "Bearing on QM-4": state that U4's model lies inside the pure case (clarification).**
U4 §6.2 defines `|Ψ⟩ = (|L⟩|E_L⟩ + e^{iθ}|R⟩|E_R⟩)/√2` with `|E_·⟩` "the state of the whole
complement, hidden part included". These are pure states, so Englert's equality `D² + V² = 1` holds
at every tick of that model. The mixed-complement counterexample therefore applies only to a
complement that is not in a pure state, which is outside U4's own setup. The note half-says this
("the sentence holds there"). It should say plainly that the C6 PARTLY rests on two narrower
points:
(a) U4 cites the inequality where its argument uses the equality.
(b) "Exclude each other" has two readings. Read as a statement about states, that partial `D` and
partial `V` cannot coexist, it is false even under equality (`D = V = 1/√2`). Read as a statement
about processes, that `D` and `V` cannot both increase, it is true under equality.

The note argues only against reading (a)'s literal form and reading (b)'s first sense. Without
this, the verdict reads as if QM-4 were wrong in U4's own model, which the note does not show.

**3. C3 carries an unlabelled inference (required change).** "(or, by implication, operations on
the environment)" is not in Schlosshauer 2019. The source sentence, checked at arXiv:1911.06282,
says only that undoing entanglement-type decoherence "will require appropriate measurements on the
environment to gather information that has leaked from the system". Mark the parenthesis
[writer's inference] or remove it.

**4. Walborn Fig. 3: the marker description is imprecise (minor).** In Walborn et al. the path
label is the `s` photon's own polarization, set by QWP1/QWP2 and correlated with `p` through the
polarization entanglement. In Fig. 3, POL1 is absent and neither photon's polarization is analysed.
"Coincidences with the marker photon detected but unanalyzed" (C1, C2) should read "coincidences
with `p` detected and no polarization analysis of either photon". This does not change the
verdicts.

**5. C10 quotes "the brief", which is not a resolvable source (minor).** The quoted phrase "Ma et
al. 2013 ... delayed-choice entanglement swapping/eraser" does not appear in `S3-U4-r1.md` or
`U4-SOURCES-r1.md` (grep at the head). Name the document it comes from, or drop the quotation and
keep the substantive point (PNAS 110, 1221 is the causally disconnected eraser; *Nature Phys.* 8,
480 (2012) is the entanglement-swapping paper).

**6. Kim discrepancy (advisory).** I confirmed the arXiv v1 text: type-II BBO, "Glen-Thompson"
prism (spelled so in the source; the note normalizes it to Glan), ≈2.5 m, "at least 8ns". I also
confirmed the RMP text: type-I SPDC, ≈2.3 m (7.7 ns). arXiv holds only v1 (the v2 URL returns 404).
A web-search summary of a copy of the published PRL hosted on a university site reports "7.7 ns".
I could not open that copy (host unreachable), so this is unverified. It suggests the RMP follows
the published version. The note's "unresolved" flag is the correct status. Adding "arXiv carries
v1 only" would be useful.

**7. Scope of "no unsorted singles" (advisory; the note is correct, but summaries of it must keep
its scope).** The note limits the claim to "none of the three delayed experiments read" (C2) and to
Kim, Walborn and Ma (C4, C5). That is accurate. It is not true of all the papers read:
- Schwindt 1999's `V` is unconditional single-photon count data with the marker unread.
- Dürr 1998's atom patterns (SECONDARY) are unconditional.

The note itself uses both in this way (C1, C5(a)). A summary such as "no paper read reports
unsorted singles of the interfering particle" would overstate the note and should not be used in a
PR description or a downstream citation.

**8. C8 search scope (advisory).** The "not a finding that none exists" scoping is correct. The
read set has two gaps for C8:
- The RMP read for the note names Eichmann et al. 1993 as an atomic erasure realization. The note
  does not list it.
- Cavity-QED complementarity experiments, in which which-path information is stored in a cavity
  field (for example Bertet et al., *Nature* 411, 166 (2001); reviewer's recollection, not read
  here), are the most obvious candidates for a reversal-type test.

If C8 is to carry weight downstream, list these as unread candidates.

## Checked

- **Kim 2000:** arXiv v1 read in full by me. Joint-detection rates only; no `D0` singles. "Recorded
  at the same time during one scanning". Fig. 5 "absence of interference"; `R04` "no significant
  difference ... except the small shift of the center". 0.3 mm and 0.7 mm. 351.1 nm. 2.5 m and 8 ns,
  1 ns response. Passive beam-splitter choice. "Reduced to the level close to the observation". Axis
  tick 140. The conclusion quotation matches the conclusion paragraph; the abstract's wording
  differs slightly.
- **Walborn 2002:** arXiv v1 read in full by me. The "Nearly all interference ... destroyed",
  "residual interference ... small error in aligning", "detection time was doubled", "averaged sum
  ... roughly equal to that of figure 3" and "no 'choice' available to the observer" quotations are
  all present, as are "it is enough that the which-path information is available" and "This can be
  verified experimentally" (§III.A). Integration times 400/400/800/800/500/500/1000/1000 s for
  Figs. 2–9. Geometry: 42 cm, 125 cm, 98 cm, 2 m, 200 µm, 1 nm filters. Every plot is coincidence
  counts; "single" does not occur in the results.
- **Ma 2013:** arXiv v2 read by me. Every number in the note's 1.8 row is present:
  0.023(5), 0.978(5), 0.955(7), 0.521(16), 0.478(16), 0.077(22), 0.951(18); Table I ranges;
  20 s per point; 5 kHz and 50 kHz; 98.0 % and 96.9 %; the `V = 0.95 √(1 − (I/0.97)²)` curve; 33 dB
  with background subtraction; ≈450 µs; 1 ns window; 55 m, 50 m, 28 m and 2 m fibres; QRNG in Lab 3.
  Conditioning on Det 4 is explicit. The "bipartite complementarity inequality" quotation and the
  introduction quotation ("anywhere in the universe ... irrelevant whether a future observer") are
  present. The path probabilities come from 120 s path-blocked runs, as the note says.
- **Schwindt 1999:** arXiv v1 read by me. 670 nm; rates below 50,000 s⁻¹; analyzer lowered for `V`;
  background 100–400 s⁻¹; 1.11 ± 0.01; 0.976 ± 0.017; 0.998; ~98 %; "V > 4.4% even though
  L > 99.9%"; 0.003 ± 0.001 against 0.017 ± 0.003; purity 0.65 ± 0.01; `D = max{K}` and "or even
  zero"; the equality and inequality sentence; "sorts the photons into sub-ensembles"; fringes and
  anti-fringes.
- **Ma–Kofler–Zeilinger RMP (arXiv v3):**
  - "where equality holds for pure states" (Jacques et al.).
  - SEW: "can only be seen in coincidence with the corresponding photon projections" and
    "independent of whether an observer takes note of it".
  - Herzog: type-I, markers and erasers.
  - Dürr: (75 ± 1) % and (44 ± 1) % at 105 and 255 µs; "four orders of magnitude"; the "mere fact"
    quotation.
  - Kim: type-I; 2.3 m (7.7 ns); "made randomly by photon 2".
- **De Zela comment (arXiv:1305.0861):** "first derived by Jaeger, Shimony and Vaidman"; the
  `D ≤ Σ D_k √(1−|u_k|²)` and `V = |Σ D_k u_k|` steps; "slight technical flaw"; "Neither the
  physical content ... questioned".
- **Abstracts:** I fetched these and they match the note's quotations: Scully–Drühl 1982, Englert
  1996, Herzog 1995, Dürr PRL 1998 and Greenberger–Yasin 1988 (INSPIRE), Wootters–Zurek 1979
  (INSPIRE record 152058), and Kwiat 1992 (OpenAlex).
- **Schlosshauer:** the 2019 Phys. Rep. passages (unitary noise and spin echo; local reversal;
  Brune numbers `n̄ ≈ 10`, `χ = 0.31π`, overlap below 3×10⁻⁵, two-atom `P_ee`). The 2004 RMP
  recurrence passage ("Poincaré type with τ_r ∼ N!", "always remains finite"); arXiv v4 is dated
  2005.
- **Bibliographic data:** volume, page and year confirmed for every primary cited; no citation error
  found.
- **U4 quotations in C1–C8:** these match `S3-U4-r1.md` at the head (lines 246–249, 295–303,
  368–379, 418–422).
- **Measured against predicted:** C2's "whatever the later choice", C4's "while unread ... no
  fringes" and C5's "while parked" are correctly classed as standard-QM predictions, not reported
  observables. The recovered fringes in Kim, Walborn and Ma are correctly classed as conditional.
- **§3 bounds:** the quarter-disc region and its exclusions are correct (`V = 1 ⇒ D = 0`,
  `D = 1 ⇒ V = 0`). The predictability form is weaker because `P ≤ D`. The intact-return argument
  (a unitary on the complement preserves the trace distance and `|Tr|` of the off-diagonal block)
  is correct.

## Not checked

- The Dürr 1998 *Nature* abstract (nature.com unreachable from the review environment), and
  therefore the quotation "correlations between the which-way detector and the atomic motion".
- The SEW 1991 abstract (nature.com).
- Any published (journal) version, including Kim's PRL; see finding 6.
- Full texts of the items marked ABSTRACT or NOT READ in the note.
- The note's Kim figure-level details beyond the text and axis labels: the plotted visibilities,
  and whether `R04` was plotted.
- U4's OI-internal reasoning, which is outside the note's scope and this review's.

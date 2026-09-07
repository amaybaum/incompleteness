# Barandes exact-input and indivisibility-role audit

Owner-called from `main` at `44cb78080d48c786a27257271bff78cf99afd530`, the merge of #538.
This file is the preregistration only. It is committed before any primary-source conclusion is recorded.
No Lean theorem, manuscript text, census status, or sourcing claim is changed in this commit.

## Why this round exists

The current OI corpus separates two claims that have not yet been checked directly against the Barandes primary sources:

1. finite stochastic laws admit a Hilbert/unitary/Born-form representation without requiring C4 or P-indivisibility;
2. indivisibility supplies specifically nonclassical/quantum content rather than the mere existence of that representation.

#537 tested a stronger object: whether the reduced substratum dynamics uniquely determines a global invariant law on the whole configuration space. #538, by contrast, works with a rooted family

`Γ_t(a,j) = P(X_t=j | X_0=a)`

coming from a finite visible/hidden realization with one common hidden preparation law. Before any further observer-interface sourcing work, this audit asks whether Barandes actually requires the stronger global-ensemble datum at all.

## Primary-source restriction

The execution phase may use only Barandes primary sources, including official arXiv versions and/or publisher versions of the three source records:

- arXiv:2302.10778
- arXiv:2309.03085
- arXiv:2507.21192

Secondary summaries, search snippets, the OI manuscript's own paraphrases, and later commentary may be used only to locate a primary source, never as evidence for a verdict.

The audit must record source title, version/date, theorem/definition location, and any change of terminology across versions. If the three papers alter the role of indivisibility over time, the latest statement is not silently projected backward onto the earlier theorem.

## Frozen questions

### Q1 — minimal input object

What is the smallest mathematical data structure on which the relevant stochastic-to-quantum representation theorem is stated?

The answer must distinguish, if present:

- state/configuration set;
- time labels or ordered pairs of times;
- stochastic transition matrices or conditional probabilities;
- composition/consistency conditions;
- initial/rooted preparation data;
- any sample-space/global process law;
- any invariant/stationary measure;
- any divisibility/indivisibility hypothesis.

No OI object is identified with a Barandes object until the source definition has been written exactly enough to compare them.

### Q2 — ensemble requirement

Does the representation theorem require an initial global ensemble at all?

Test separately:

1. a probability law on the full state/configuration space;
2. a stationary or invariant law;
3. a family of rooted/conditional transition probabilities;
4. a fixed preparation distribution used only for a particular experiment.

The verdict must state whether #537's `EnsembleDetermined φ` problem is necessary, sufficient-but-stronger-than-needed, irrelevant, or required only for a different Barandes statement.

### Q3 — role of indivisibility

What exactly does indivisibility add?

The audit must distinguish at least:

- existence of a Hilbert-space representation;
- existence of a unitary representation;
- Born-form transition probabilities;
- interference/nonclassicality;
- impossibility of a classical divisible description;
- uniqueness or preferredness of a representation;
- any physical interpretation claimed by Barandes.

If the 2025 indivisibility paper strengthens or reinterprets the earlier correspondence, record the logical delta rather than merging the papers into one theorem.

### Q4 — representation freedom

What freedom remains after the stochastic object is represented quantum mechanically?

Audit explicitly:

- phase freedom;
- basis/relabeling freedom;
- gauge freedom;
- dilation/ancilla freedom;
- Hamiltonian/logarithm ambiguity;
- nonuniqueness of amplitudes/unitaries producing the same stochastic data;
- any conditions under which uniqueness is recovered.

This question is descriptive: no OI phase-sourcing conclusion is drawn until the exact primary-source freedom is known.

## Provenance sub-audit

Resolve the corpus's inconsistent bibliographic dating of arXiv:2309.03085 and the presence/absence of arXiv:2507.21192. Record the actual submission/publication chronology from the primary records. Do not edit bibliographies in this round.

## Admissible headline outcomes

Exactly one headline outcome, with separate answers Q1-Q4.

**A — global ensemble genuinely required.** The relevant Barandes theorem requires a global initial ensemble in a way materially aligned with #537.

**B — rooted/conditional stochastic data suffice.** The theorem is stated on stochastic transition/conditional data and no unique global invariant ensemble is required. In this case #537 remains a correct theorem about a stronger statistical-mechanics question, but its gap is not a prerequisite for applying the correspondence.

**C — mixed boundary.** One Barandes result needs only transition data while a later indivisibility/physical theorem requires additional process or ensemble structure. The exact split is recorded.

## Prediction recorded before source inspection

Outcome B or C is expected. The working hypothesis is that the representation theorem is broader than the indivisible subclass and that indivisibility identifies specifically nonclassical structure rather than creating Hilbert/unitary representability itself. This is a prediction, not a result.

## Consequence discipline

If Q2 finds that no global invariant ensemble is required, the next OI sourcing target becomes the weaker realization-level object actually needed for a rooted observer family:

`visible/hidden split + visible root preparation + one common hidden prior + reversible evolution + visible readout`.

That later sourcing audit must ask whether these are already supplied by the intended C1-C4 physical realization. It must not reopen canonical statistical mechanics on all of `Substratum.Conf` unless Barandes actually requires it.

Separately, any future `CausalReadback` predicate must live at the realization level rich enough to see both history-conditioned laws and rooted one-time marginals. It may then be tested independently for implications toward history memory and toward marginal revival. This audit does not define that predicate.

## Non-doings

This round does not:

- edit any manuscript;
- add or alter Lean;
- rename or redefine C4;
- claim `C4w => C4e` or `C4r`;
- source a hidden prior from OI;
- apply Barandes to OI before Q1-Q4 are settled;
- treat a search-engine snippet as primary-source evidence;
- infer a phase resource or operational quantum repertoire from mere representability.

Status: **preregistered; primary-source execution not yet recorded.**
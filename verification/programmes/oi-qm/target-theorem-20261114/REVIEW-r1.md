# Independent non-author review of TARGET-THEOREM-r1

**Verdict: REVISE.** Three blocking findings (B1–B3), twelve should-fix (S1–S12), nits (N1–N14).
Most of the document's citations hold; the blocking items are one status that is wrong in
direction, one "refuted" label attached to a statement that is true as worded, and a set of
recorded decisions and corpus definitions the owner questions do not show.

**Method.** Read-only, paper-only. Every cited manuscript line was opened in `wt-mainread`
(`c3b5f37a`); every cited Lean declaration was located and its statement read (not built). The
off-`main` status notes were read in `wt-bellplan` (`a0fa2502`) and `wt-tune1plan` (`ea9bff9c`).
GitHub was read, not written: bodies of #914, #1169, #1216, #875, #899, #1060 and the title list
of the 90 open Issues. No computation on any OI model. Hand reasoning is marked **[hand]** and is
not a kernel statement.

Paths: `M:` = `papers/Main.md`, `OB/` = `verification/lean-mathlib/OIBridge/`,
`PG:` = `verification/programmes/oi-qm/PROGRAMME.md`, others as in the document.

***

## 0. What was confirmed

- **The line number of every cited Lean declaration matches** (`RevReal`:157 … `iterate_dependsOnlyOn_ball`:283).
- Manuscript quotations at M:42, :60, :66, :70, :80, :360, :381, :414, :416, :427, :549–:562, :564–:582,
  :584–:600, :724, :774; GR:226, :256–:260, :282–:284; Sub:123–:133, :171, :193–:195; PG:40, :84, :86,
  :197–:206; EP:25, :33–:45, :53–:69, :102, :123; RD:320, :404–:408, :446–:447; S4:423, :464; coverage
  ledger id `MAIN:T-finite-operational-realization-gluing-form` ("no Lean statement") are accurate.
- T1 both directions, T3 (a), (b), (c), T5a (all three rows), T5c (⇒) carrier and hypotheses, the
  Jordan uniqueness statement, `q3_countermodel`, `finiteSupport_iff_kraus`, the cone lemma and
  O1/O2/O4/O6 are as the Lean or manuscript states them, on the stated carriers.
- BL and TL status-note line cites (STATUS-BS:50–51, :53, :61, :92; STATUS-LADDER:53, :56, :57, :59;
  STATUS-SB-L3:65; STATUS-STEP3A:49, :59; STATUS-SOURCING:43, :49; LANDING-PLAN:243–252, :264) are
  accurate, except the compression noted in S2.

***

## 1. Blocking

### B1. T3 (d) is labelled a kernel-checked biconditional; the two witnesses are on different predicates, and on the (⇐) witness's predicate the (⇒) direction is false

*Location:* §2 T3, statement and both rows, item (d); §3 Summary "T3 ([K], kinematics given)".

*Sources.*
- `substratum_plus_control_qm`, OB/StructuralClosure.lean:414: conclusion is
  `ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 hc.arch A)`. It is a statement about the one
  theory `genTheory 𝓘`, whose availability is *defined* as instrument realization by `𝓘` on the
  system and at every level (OB/ImplementationLocality.lean:852–855). The hypothesis
  `ExtendsSubstratum 𝓘` is bound to `_` and unused.
- `qm_generated_by_substratum_extension`, OB/StructuralClosure.lean:423: conclusion is
  `∃ 𝓘, ExtendsSubstratum 𝓘 ∧ StructurallyClosed 𝓘 ∧ DrivesElementary 𝓘 ∧ ImplementationGenerated T 𝓘`,
  witness `fullClass`. `ImplementationGenerated` (OB/ImplementationLocality.lean:352) constrains
  `availExt` **at positive levels only**; it says nothing about `T.avail` on the system.
- `generated_of_qm` (OB/ImplementationLocality.lean:1004) uses only `h.2`, the composite half.
- `systemLoose` (OB/LevelOneSeam.lean:302–341, `levelOne_independent` :353): valid, inert, full
  control, iterated closure, exact composites, **not** exact on the system.

*Why it matters (§A.34).* With Ext(d) read as the (⇐) theorem's conclusion, (⇒) is not the cited
theorem and is false **[hand]**: `systemLoose` has exact composite operations
(`exactComposite_of_validity_general`, OB/GeneralCarrier.lean:79), so the proof term of
`generated_of_qm` gives `ImplementationGenerated systemLoose fullClass`; `fullClass` extends the
monomial class, is structurally closed and drives the elementary transitions; and
`systemLoose_not_exact` (:328) holds. With Ext(d) read as "`T = genTheory 𝓘`", (⇐) is not the cited
theorem (no statement that an exact `T` equals `genTheory fullClass`, whose `prepAvail` is fixed
by definition). Either way one direction has no witness. In the package (c) the gap is closed by
the separate conjunct `EmbeddedObservation` (`systemToLevelOne_of_embeddedObservation`,
OB/EmbeddedObservation.lean:223); (d) has no such conjunct.

*Also:* the clause "extends the monomial class" does no work in either direction (unused in (⇒);
trivially met by the class of all operators in (⇐)), and `DrivesElementary`
(OB/SubstratumSource.lean:77) is the whole elementary repertoire on every carrier: every
transition flow at every real time, every exchange, every quarter phase.

*Proposed replacement* (T3 statement, item (d), and its two rows):

> (d) is not a biconditional on one predicate. **(d⇒)** [K] `substratum_plus_control_qm`,
> OB/StructuralClosure.lean:414: for every structurally closed class `𝓘` that drives the
> elementary transitions (all transition flows at all real times, the exchanges and the quarter
> phases, on every carrier), the theory `genTheory 𝓘` — availability defined as instrument
> realization by `𝓘` on the system and at every level — is Q_op. The hypothesis that `𝓘` extends
> the monomial class is not used. **(d⇐)** [K] `qm_generated_by_substratum_extension`, :423: every
> Q_op theory is, at every positive ancilla level, instrument-realized by some such class; the
> witness is the class of all operators. No kernel statement gives Q_op from that conclusion, and
> a theory with exact composites and a non-quantum system level satisfies it (`systemLoose`,
> OB/LevelOneSeam.lean:353; this composition is this document's reading, not a named theorem).

and in the Summary: "T3 (a), (b), (c) ([K], kinematics given); (d) and (e) as stated in §2".
Add to "Documents that differ": the display at GR:258 is a boxed `⟺` citing these two theorems
and M:588 calls the second "the converse".

### B2. T2 (⇒), T4b (⇒) and O3 call "refuted" a statement that, as worded, is true and is T1 (⇒)

*Location:* T2 row (⇒) ("every law of the OI realization is within ε/2 of a quantum law … refuted
for the class of finite reversible realizations"); T4b (⇒); O3; Summary; owner question 6.

*Sources.* `D_imp_Qfb`, OB/Equivalence.lean:294: every visible law of every finite reversible
realization **is** a fixed-basis Born law, exactly. M:598: "its closure contains non-quantum
operational **theories** too" — the object is a behaviour set / operational theory at fixed
`(d, m)`, not a single law. M:360: the PR table is non-quantum only relative to the local
subsystem structure ("a global stochastic law can be represented unitarily while failing the
*local subsystem* conditions").

*Why it matters.* Law by law, OI ⊆ QM holds with ε = 0 by T1. What M:598 denies is that the
action-labelled behaviour of an arbitrary realization is the behaviour of one `d`-dimensional
quantum model with ≤ `m`-outcome instruments. The document's wording lets question 6 read as if a
selection principle were needed already at the level of individual laws. M:598 also exhibits no
witness; it is an assertion inside a Corollary, so the tag is [P].

*Proposed replacement* (T2 (⇒), Statement and Status cells):

> Statement: the action-labelled behaviour of the OI side — the laws of all its protocols jointly,
> with each label read as one fixed instrument — is within ε/2 of the behaviour of one model in
> Q^(d,m)_K. Status: [P] for the constructed family R (M:596 (ii)). For the class of finite
> reversible realizations it fails at the level of behaviour sets, [P], asserted without an
> exhibited witness (M:598: "its closure contains non-quantum operational theories too"); for
> composites the witness is the PR table relative to the wing structure (M:360). Law by law the
> inclusion holds exactly ([K], `D_imp_Qfb`), so the failure is one of joint structure at fixed
> `(d, m)` and labels, not of any single law.

O3, first column: split the witnesses — "`oi_alone_not_qm` ([K], two-state carrier): exact
operational level only; M:598 ([P]): behaviour sets at ε level; M:360 ([P]): composites with wing
structure".

### B3. §6 presents as open several choices that have recorded decisions, and omits the corpus's own definitions of the target

*Location:* §6 questions 1, 3, 5, 6, 8; "Documents that differ" F3; §2 candidate list.

*Sources.*
- PG:19–36: "Ultimate objective … `OI + C <-> operational quantum mechanics`", with the two
  acceptable endpoints *Equivalence* and *Classification*.
- PG:44–64: three notions "that must not be conflated": A quantum representation, B quantum
  operational repertoire, **C "Full physical equivalence to QM"** ("including composition,
  locality, dynamics, measurement, state preparation, correlations, and the relevant
  infinite-system/continuum qualifications").
- PG:509–545 (Arc F): endpoints F1 (full conditional equivalence), F2 (minimal extension theorem;
  "The active form proves sufficiency first … with the necessity of each added principle …
  assessed separately"), F3 (exact classification without uniqueness), and the retirement rule;
  PG:40 and PG:632–634: F1 retired for the presently stated architecture, F2 active.
- M:774: "the phrase *equivalence of quantum mechanics and embedded observation* has a precise
  theorem-level meaning: **exact bidirectional equivalence of finite observable stochastic laws
  and their quantum representations, with history readback selecting the memory-bearing sector.**
  … Full equality with the standard local operational quantum theory requires a common compatible
  representation of the complete coherent instrument/composite hierarchy."
- #875 [I] (open, tier foundational), "Owner decisions (2026-10-17) … adopted … explicitly, one by
  one": "(a) Target: A1 exact with B1 qubit-power registers (F2-reg). All finite dimensions
  (F2-fin) stays the named later obligation Γ11. (b) Extension criterion: strict, with gates
  G1–G8 … (c) Monitored law: M1 … (d) Necessity scope: narrowed to holds-in-target (N1) and
  drop-one (N3′)." Read at Issue-body level only; the memo it cites is off `main` and was not read.
- #1216 [I] (open, tier foundational, "the owner's ranking, 2026-11-09"): Level A (finite-horizon
  statistical approximation) and Level B (uniform operational approximation, "the main target"),
  "distinct from #1169's exact question".
- #914 [I] §1 itself records F1 as retired and F2 as active.

*Why it matters.* The owner is asked "which is the theorem meant by full equivalence", "exact or
ε", "may the left side carry named added principles", "containment or realization" without being
shown that the programme map and two Issues already carry answers to parts of these, or that the
corpus defines "full" in two places. A choice made from §6 as it stands could silently supersede
them. F3 is also not a discrepancy: #914's goal sentence is disjunctive and its §1 agrees with
PG:40; and the phrase quoted is in #914's body, not its title.

*Proposed changes.*
1. Add §1.3 "What the corpus already calls the target", quoting PG:19–36, PG:44–64, PG:509–545,
   M:774 and M:431, and a table mapping T1–T5 and clause B onto A / B / C and F1 / F2 / F3
   (T1, T1∞: A; T2, T3, T4a, T5a, T5c: B; C = T5b with clause B and the continuum qualification
   T4c; F2's active form is a (⇒)-only target; F3 is a classification, not an equivalence).
2. Replace F3 with: "PG:40, PG:632 and #914 §1 [I] agree that F1 is retired for the presently
   stated architecture and F2 is active; #914's body states the goal as 'the full equivalence … or
   a precise identification of the additional physical principle it needs'. No difference between
   them was found."
3. Head §6 with a "Recorded decisions" table (PG:40 F1/F2; #875 (a)–(d); #1216 Level B; the
   Gate A contract EP:71–106 accepted for #1169) and phrase questions 1, 3, 5 and 8 as "keep,
   narrow or supersede".
4. Rename the document's findings F1–F3 (they collide with PG's endpoint names).

***

## 2. Should-fix

### S1. Missing candidate: Main's own "Characterization theorem" and the readback clause

*Location:* §2 (no entry). NOTES §1 records M:604–:716 as unread apart from :716–:724.

*Sources.* M:536–:542: "**Characterization theorem.** … Then (ii) ⟺ (iii); and, under (T), (i)
holds" with (i) "𝒮 is mathematically equivalent to unitarily evolving QM", (ii) non-Markovian on
accessible timescales, (iii) per-horizon marginal of a bijection with (C1), (C3), (C4). M:628:
"Both directions are proved here in prose and neither is formalized in the kernel". M:632
"*Remark (retired direction).* (i) alone does not imply (ii)". M:526–:528: (i) means the imported
representation (Q1) under translation hypothesis (T), instantiation-checked on three sizes.
M:600 (2): "M_t > 0 ⟺ readout-relevant hidden predictive memory in every faithful completion —
proved: clauses (a)–(c) … in the kernel for a joint law …, with the reading of a realization's
time-t law as that joint law not formalized; … both directions using the vanishing criterion for
conditional mutual information, which is not formalized" (`unavoidable_hidden_predictive_memory`,
OB/HiddenMemory.lean:185). M:696 restates (ii) ⟺ (iii).

*Proposed addition* (new candidate before T1):

> **T0. Characterization form (Main §3.4).** For a time-homogeneous finite process on accessible
> timescales: (ii) non-Markovian at an accessible order ⟺ (iii) per-horizon marginal of a
> bijection with (C1), (C3), (C4) at that order. (iii ⇒ ii): [P], readback lemma (M:628).
> (ii ⇒ iii): [P], process dilation (M:516, :628). "neither is formalized in the kernel" (M:628).
> Quantum side (i): holds under (T) by an imported correspondence [11, 12]; (i) ⇒ (ii) fails
> (M:632). Companion: M_t > 0 ⟺ hidden predictive memory in every faithful completion, [K] for
> clauses (a)–(c) on a joint law, with two unformalized steps (M:600 (2), M:608). M:774 gives T1
> together with this readback clause as the theorem-level meaning of the phrase. Bell: outside.

### S2. T1 (⇐) and the measure: the status depends on the initial-law clause, and the document's Gap P cell misstates the measure dependence

*Location:* T1 (⇐) Hypotheses; OI-L row ("so (iv) is not used"); §4 T5b "native preparation" row;
§6 (no question).

*Sources.* M:516: the independent-hidden-prior dilation is stated for processes "whose conditional
kernels … are rational"; "Rationality tracks the prior … for a finite realization whose prior μ_H
is rational and independent of the visible initial state … the conditional kernels … are
rational". M:522: "The realization uses a structured prior". M:600: exact realization of a fixed
instrument family is "with a product prior carrying the quantum conditionals". OB/Equivalence.lean
:150–156: `(D)`'s initial law "is not required to factor". M:58: "the counting measure is the
default, not a constraint on representations". TL/STATUS-SOURCING.md:43: "an unconditional supply
excluded under μ-G (Lemma P-1), heralding the only route there …; not supplied unconditionally
under μ-O, conditional route open; undecided under μ-R"; TL/LANDING-PLAN.md:136: μ-R is "posited
through (iv) as maximal entropy compatible with the observer's records".

*Why it matters.* Under a uniform hidden prior on a finite hidden set every kernel is a ratio of
counts **[hand]**, so a quantum law with an irrational probability is not a (D) law with ledger
(iv)'s counting measure as the hidden prior. T1 (⇐) is exact for all laws only when the prior is
a free realization datum. The §4 cell assigns μ-O's wording ("not supplied unconditionally") to
the global counting measure, where the note says "excluded", and drops μ-R.

*Proposed replacements.*
- T1 (⇐) Hypotheses: "… [K] with an arbitrary real-valued initial law on V × Hid, which may
  correlate the coordinates (OB/Equivalence.lean:150–156). With a hidden prior independent of the
  visible initial state: [P] for rational conditional kernels (M:516); a real-valued structured
  prior is needed otherwise (M:522, M:600). With the uniform (counting) hidden prior of ledger
  (iv) the kernels of a realization are rational, so (⇐) then covers rational-kernel laws only
  (this document's reading)."
- §4 T5b row, evidence cell: "an unconditional supply is excluded under the uniform global law
  μ-G, heralding the only route there; not supplied unconditionally under μ-O, conditional route
  open; undecided under μ-R ([D], TL/STATUS-SOURCING.md:43); named only as …".
- New owner question: "**Initial law.** Is the OI side's initial law a free realization datum
  (M:58), the global counting measure (ledger (iv); μ-G), or a law conditioned on the observer's
  records (μ-R)? T1 (⇐) for irrational laws, the product prior of T2 and the ready resource of
  T5b each depend on the answer; #914 row 14 [I] records the pair (Obs, μ) as unsourced."

### S3. The Summary's O1 exclusion is wider than M:558, and three proved obstructions are missing

*Location:* §3 Summary ("any exact form whose OI side is one fixed finite realization (O1)"); O1
"What it excludes: … any exact reading of T2"; O-table.

*Sources.* M:558 excludes exact reproduction of "even a single qubit's **full** theory", i.e. all
preparations and effects, with the unbounded half imported [55]. M:600: "a fixed finite instrument
family is realized exactly by the intervention dilation". M:480: one fixed realization serves all
action sequences of a finite action-labelled family. Missing: M:486 (Proposition, no uniform
finite realization of the instrument continuum, by counting); M:492, :496 (Proposition, no
horizon-independent intervened representation; three successor problems (a)–(c)); M:638 ("the
universal all-time form is settled *negative*"); M:644 with ROADMAP:73 (the visible family does
not fix the relating evolution; P0, open).

*Proposed replacement* (Summary): "any exact form whose QM side contains the full qubit
prepare-and-measure theory and whose OI side is one fixed finite realization with the
preparation → ontic state → measurement interface (O1); an exact form for a fixed finite
instrument menu is not excluded (M:480, M:600)". Add rows O7 (M:486), O8 (M:492; "generic
action-labelled combs are not hostable on any fixed passive representation"), and O9 (M:644;
ROADMAP:73; #914 row 13 [I]; #866: no selection of the relating evolution — bears on any target
whose QM side includes dynamics).

### S4. Issue assignments: two "none traced" entries have Issues, and four obligations are assigned to a neighbour of the accountable Issue

*Location:* §4, Issue column.

| Row | Document | Records (titles read; bodies read where marked *) |
|---|---|---|
| T2 finite-precision bound | none traced | **#945** "ε-realization at finite precision: the negativity-ledger step fails (Main.md:556); repair or narrow the theorem" (foundational, blocked); parent programme of the ε target **#1216*** |
| T4a converse | none traced | **#899*** "L3-CONV-1: what the converse direction of Level III proves relative to its target class": "Level III is a uniqueness theorem (`canon_unique`, `systemEquiv_dyn`), not an equivalence" |
| T1 quadratic exponent | #914 row 1e | add **#1059** "BORN-SEL: does OI select the quadratic Born exponent and the probability measure?" |
| B, H-Bell (i)–(iii) and the 2√2 selector | #868; #1169; #914 row 16 | accountable: **#1060*** "BELL-SEL: H-Bell composite closure and Tsirelson selection" (status source #914 row 16); #868 is its K2 prerequisite ("Physical source of joint-test validity and composition") |
| T4c | #914 row 18 | add **#872** "Full finite-to-continuum operational completion", **#1007** "observer-relative finiteness without a finite-total-carrier requirement", **#1055** "A1-NECESSITY: can OI's results that use total finiteness be recovered without the posit A1?" |
| T2 selection principle | #1169 (Gate B/D) | unconfirmed; **#1143** "OI-QM-SEL: finite-dimensional operational selection and native distinguishability" is the nearer title (body not read) |
| T2 / T5c as ε targets | — | **#1216*** Levels A and B |
| target and extension criterion | — | **#875*** (B3) |

Confirmed as written: #914 rows 1, 1e, 3–7, 8, 9, 11, 12, 16, 18 and O-IF-SELECT; #1169 for the
interface rules (EP is its Gate A), for native control (oa-1 `STATUS.md`:124 "The accountable
Issue is #1169"), for the status trace of conditions (i), (ii), (iii), (v) and for both quoted
passages; #1236 (TUNE-1); #1147 (O-RDY); #866; #868 for the pair; #1217 (title matches the
document's description). Not found by this review either (titles of 90 open Issues scanned,
closed Issues not searched): an Issue for the unitary/transpose orientation and for a kernel
statement of the ε-theorems — keep "none traced".

### S5. T1∞ (⇐): the non-membership half is in the kernel

*Location:* T1∞ ("the non-membership half of that witness not traced"); O5; NOTES §3 item 4.

*Sources.* `qStar_not_subset_finiteRootedRealizable`, OB/QuantumRepresentationT2.lean:163;
`qStar_not_subset_pper`, :169; `pdFamily_not_finiteRootedRealizable`,
OB/RootedClassificationAllTime.lean:239; `pdFamily_not_periodicFamily`, :220.

*Proposed replacement:* "(⇐) fails at V = Fin 2 ([K], `qStar_not_subset_finiteRootedRealizable`,
OB/QuantumRepresentationT2.lean:163, through `qStar_pdFamily` :157 and
`pdFamily_not_finiteRootedRealizable`, OB/RootedClassificationAllTime.lean:239; PG:203)."

### S6. T4a (⇒): the [K] label covers the algebraic uniqueness only; the dynamics witnesses are missing and the OI_Q hypothesis is not in the kernel statement

*Location:* T4a (⇒) row.

*Sources.* `oiSystem` (OB/QuasilocalCharacterization.lean:187) has the single hypothesis
`[Nonempty Q]`; `QuasilocalSystem` (:168) is defined with stage maps from "the matrix algebra of
the region's configurations" — no controllability or OI_Q predicate occurs. The dynamics clause is
`OISystem` :463, `oiDynamical` :471, `canon_dyn` :487, `systemEquiv_dyn` :497, none cited. The
module header (:51–:53): "uniqueness among systems with THESE local stages … not a classification
of all quasilocal C*-systems". GR:284 supplies the reading of the stages as OI_Q's.

*Proposed replacement* (Witness and Hypotheses cells): add "`oiDynamical` :471, `canon_dyn` :487,
`systemEquiv_dyn` :497 for the dynamics"; Hypotheses: "the kernel statement takes the finite-region
stages to be the full matrix algebras on the region's configurations and has no hypothesis naming
OI_Q; that these are the stages of the quantum-completed substratum is the manuscript's reading
(GR:284), resting on the Level I and II results. Uniqueness is among systems with these stages."

### S7. T5c's two rows are not the two directions of one statement; T3 (e) (⇐) is a composition and its sides differ from the T3 header

*Location:* T5c rows; T3 (e).

*Sources.* `krausDense_of_fixedGate` (OB/DenseInstrumentBridge.lean:502) concludes `KrausDense T`:
every Kraus instrument has an available approximant — the inclusion QM ⊆_ε OI-side, which T2
calls (⇐). The opposite inclusion is the hypothesis `KrausSoundExt` of
`denseFiniteQM_of_denseControl` (:496). The row labelled T5c (⇐) is again QM ⊆_ε OI, at native
model level. `shadowQuantum_of_typed` (OB/TypedCompletion.lean:838) concludes `𝒯.ShadowQuantum`,
not `OIPlusMin` of the shadows; reaching Ext needs `oiPlusMin_of_qm` per shadow. The object in (e)
is a `TypedOperationalTheory`, the QM side Q_typed.

*Proposed replacement.* For the ε-forms (T2, T4b, T5c) label rows "completeness (QM ⊆_ε OI)" and
"soundness (OI ⊆_ε QM)". T5c: "completeness at interface level: [K], conditional on the gate;
soundness at interface level: a hypothesis of the cited theorem; completeness at native-model
level: open; soundness at native-model level: not stated in any record read". T3 (e) (⇐):
"`shadowQuantum_of_typed` :838 then `oiPlusMin_of_qm` on each shadow (a composition, not a named
theorem); the object is a typed theory and the QM side is Q_typed".

### S8. Clause B, adopted branch: "conditional on H-Bell" overstates what is derived

*Location:* Clause B row "B ⇒, adopted branch".

*Sources.* Sub:133: "H-Bell is therefore an explicit curvature-stability/**composite-existence
hypothesis**"; its clauses (i) and (ii) are the row's statement. Sub:193: the completion "exists
only conditional on H-Bell". M:414: "What remains to be proved for this branch is … that the
prepared graph family supplies the required response dependence while preserving operational
no-signaling". M:427: "its realization by the proposed SM/GR prepared graphs is an open H-Bell
obligation". #1060 [I]: the H-Bell round is "frozen and never executed".

*Proposed replacement* (Status cell): "posited: H-Bell (i) and (ii) are this statement
(Sub:133, 'composite-existence hypothesis'); no record derives Bell-violating correlations, or
the quantum set, from a further premise; uniqueness open (Sub:193)".

### S9. Open obligations missing from §4

*Location:* §4.

| Obligation | Source |
|---|---|
| Kochen–Specker inheritance | M:582 "remains conditional exactly at that operational-algebra layer"; `papers/Methodology.md`:399 ("conditional"); M:570 (implementation-fixedness "not Spekkens noncontextuality, which … is not claimed") |
| Born statistics across settings derived, not only represented | #914 row 17c [I], "O"; #1059 |
| the stochastic interface (Obs, μ) | #914 row 14 [I]; `ensemble_underdetermined`, OB/StochasticInterface.lean:118 |
| physical C4 at the cuts | #914 row 15 [I]; #1061 |
| native preparation-and-measurement instrument | #914 row 20 and O-INS [I]; ROADMAP "valid-measurement clause", frozen record |
| records, retention, reuse | #1169 [I] table ("#1032 and #913 (O-REUSE)") |
| run repetition and the law of the unread world | TL/STATUS-STEP3A.md:94 ("run repetition, used but not stated"); H-μ, :88; TL/STATUS-SOURCING.md:84 |
| selection of the relating evolution | S3, O9 |
| the three successor problems for intervened representations | M:496 (a)–(c) |

### S10. Delimitation of the OI side: OI-I consumes ledger (ii); two statements in §1.1 are wider than their sources

*Location:* §1.1 table and the sentence "The corpus attaches the name to four different objects".

*Sources.* `obsTheory` (OB/SubstratumInterfaceAudit.lean:770) is a theory on `𝒮.Conf`, the
**whole** configuration space, "under the finiteness A1 supplies" (`[Fintype 𝒮.ι] [Fintype 𝒮.V]`).
The module header (:33–:35) and `obsTheory_rule_independent` (:780) say "consumes nothing of
A3–A6"; (viii) and (xiii) are built into the type `Conf = ι → V × V` (:78), though the theory
depends on it only as a finite type. "Bare (finite) OI" is used for OI-L (M:360) and for OI-C
(M:356, M:562, GR:240); OI-I and OI-S are called "the concrete OI substratum" / "the current OI
substratum" and are contrasted with bare OI (GR:260, GR:284).

*Proposed replacements.* OI-I, last cell: "ledger (ii) (the carrier is the total configuration
space, finite by A1) and (iii); independent of the rule (`obsTheory_rule_independent`), 'consumes
nothing of A3–A6'; (viii) and (xiii) enter only through the type of the configuration space".
Sentence: "The corpus uses 'bare (finite) OI' for two objects, OI-L (M:360) and OI-C (M:356,
M:562), and distinguishes both from the concrete substratum (OI-I, OI-S; GR:260, GR:284)."
Also: "in none of the four" is inconsistent with the OI-I row, whose second object includes the
phase intervention; say "in none of OI-L, OI-C, OI-S or the permutation form of OI-I".

### S11. "Documents that differ": one more surface for F1, and the F1 composition is confirmed

*Location:* F1.

*Confirmed.* M:80, :214, :352, :582, :774 and Sub:373 say that which of conditions (i), (ii),
(iii), (v) the substratum supplies is open; M:588, GR:260 and RD:320–322 say the substratum
supplies the structural architecture / "every structural requirement". The lemma statements
behind the document's composition were opened and say what it needs:
`validity_of_implementationLocality` (OB/ImplementationLocality.lean:971, nonempty carrier),
`systemToLevelOne_of_embeddedObservation` (OB/EmbeddedObservation.lean:223),
`observationalIndependence_of_implementationLocality` (OB/ImplementationLocality.lean:957) with
`observationalIndependence_iff_inert` (OB/CarrierGeneralOIPlus.lean:75), `closure_of_embeddedObservation`
(OB/EmbeddedObservation.lean:211; named for `DerivedOI` as `DerivedOI.closure`, OB/RouteB.lean:158).
So for `obsTheory 𝒮` and `substratumTheory A` on nonempty carriers the four predicates hold.

*Qualification to add:* "These are predicates of the generated formal theory, whose preparation,
readout and discard rules are fixed by the definition of `genTheory`; EP:25 records the physical
reading of those fields as an obligation, and #1169 [I] calls its trace 'not a native physical
derivation'." Add M:214, M:352 and Sub:373 to the list of surfaces. F2 is confirmed, and PG:86
already reconciles it ("Historical statements …"); say so.

### S12. T2 Bell cell omits the manuscript's own locality claim

*Location:* T2 (⇐) Bell cell ("no locality constraint"); §5 item 2.

*Source.* M:572 (4): "necessarily joint for entangled preparations, **in the
factorizability-failing, locality-retaining pattern of §3.3**".

*Proposed replacement:* "inside, by the product construction on a joint branch register,
'necessarily joint for entangled preparations, in the factorizability-failing, locality-retaining
pattern of §3.3' (M:572 (4)). The theorem states no own-wing read/write condition; by M:381 and
the bound of §5 item 2 a realization within ε < (√2−1)/4 of a Tsirelson experiment cannot satisfy
hypothesis (ii) of M:366–368 together with (xiv), and its no-signalling holds to accuracy ε (this
document's reading)."

***

## 3. Nits

- **N1.** T5a: `permTheory_phase_ceiling` (OB/FrozenSourcing.lean:106) holds on every nonempty
  carrier; O2's "two-state carrier for the first two" understates the phase half (#914 §1 [I]:
  "phases: every nonempty `A`; dense control: `Fin 2`").
- **N2.** "`obs_not_layerFlowExecutable` … (every substratum with a moved configuration)" → "every
  substratum and every permutation of its configurations that moves one".
- **N3.** T2 (⇐): cite also ledger id `MAIN:T-uniform-continuum-realization-mutual-density`
  ("The net argument is the analytic step and the probe does not reach it").
- **N4.** T1 [K]: `QfbReal.chain` and `QfbReal.law` (OB/Equivalence.lean:209, :213) *define* the every-step projective
  record as the chain of Born weights; say "class as formalized".
- **N5.** OI-L consumes ledger (i) as well (a multi-time trajectory).
- **N6.** OI-S "Defined at … Sub:123, :193 (A1–A6)": those lines list inputs; A1–A6 are stated
  elsewhere in Substratum.
- **N7.** T3: `qm_iff_derivedOI_pairFlowSourced` (OB/PairFlowEquivalence.lean:199, two-state
  carrier) is a further exact form of the T3 family; NOTES lists it as read.
- **N8.** T4c: add M:356 ("stagewise finiteness does not prove that this completion retains finite
  predictive rank").
- **N9.** §5 item 5: S4's own header is "WIP / UNVERIFIED research record" and NL-C is tagged [W]
  there; say so beside [R].
- **N10.** `papers/Methodology.md`:399 calls S ⟺ D ⟺ Q_fb "a full equivalence there"; worth one
  line in §1, since the word "full" is the subject.
- **N11.** #1188 [I] "KERNEL-VAC-1: `ReadWriteSourced` is vacuous" concerns
  `readWriteSourced_not_qm` in OB/ReadWriteControl.lean, the module M:588 cites for
  `readWriteControl_independent`; the document cites neither, but a reader following M:588 should
  know.
- **N12.** B (⇒), reference rule, Hypotheses: add (iv) of M:372 (one common pre-setting ensemble)
  and response-completeness.
- **N13.** #914 [I] cites M:20, M:556, M:560, M:566–580 from an older `main`; where the document
  repeats a #914 row, use the current lines (M:554, :558, :564–:580).
- **N14.** Neutrality wording: "per surviving candidate" → "per candidate not excluded in §3";
  question 10 "the uniqueness theorem it is" → "as a uniqueness theorem (its kernel form)".

***

## 4. The seven review points

1. **Status labels and witnesses.** Sound except B1 (direction/predicate), B2 ("refuted" wider
   than, and worded against, its support), S5 (a kernel witness exists), S6 and S7 (a [K] label
   covering part of the stated row), S8 ("conditional" where the hypothesis is the statement) and
   S3 (Summary exclusion wider than O1). No direction was found whose witness is an extension or
   density theorem presented as a converse; T4a (⇐) is correctly marked open.
2. **Completeness.** Missing candidate T0 (S1); missing corpus definitions of the target and the
   classification endpoint F3 (B3); missing obstructions (S3) and obligations (S9). Born-exponent
   selection, complex kinematics, total finiteness, composites, H-Bell and preparation are
   present; Kochen–Specker, the measure, apparatus/instrument sourcing and the run law are absent
   or partial.
3. **Definitions of the two sides.** Match the manuscript and ledger, with S2 (measure), S10
   (OI-I and the use of "bare") and N5–N6.
4. **Reported discrepancies.** F1 confirmed, lemma statements opened (S11). F2 confirmed and
   already reconciled at PG:86. F3 is not a discrepancy (B3). One to add: GR:258 / M:588 on T3 (d)
   (B1).
5. **Issue numbers.** S4.
6. **Neutrality.** No candidate is recommended and OI's truth is not assessed. N14 only.
7. **Owner questions.** All eleven are real. Questions 1 and 10 overlap (10 is the T4a branch of
   1). Questions 1, 3, 5, 8 have recorded partial answers (B3). Missing: the initial law (S2); the
   realization quantifier — one realization per law and horizon (T1), per bound `(d, m, K, ε)`
   (T2), or one for all experiments, with the resource law (M:580, #1216 Level A against Level B);
   the endpoint type — equivalence, sufficiency with necessity assessed separately (F2's active
   form), or classification (F3); the carrier scope — two-state, every finite carrier, typed,
   quasilocal (#875: F2-reg against F2-fin); whether the readback sector of M:774 is part of the
   target; whether the Gate A admissibility contract (EP:71–106) is the definition of the native
   model class; and, for Bell, complete-history against selected-read no-signalling
   (BL/STATUS-LADDER.md:56–57) and which cone is the physical one (M:414, "not derived here").

***

## 5. Limits of this review

- No Lean build; statements and proof terms were read. B1's countermodel is a hand composition of
  kernel statements.
- #875's memo, #1216's unit-1 drafts, `wt-3a/`, the Bell and TUNE-1 reports beneath their status
  notes, and closed Issues were not read. #1143, #945, #1059, #872, #1007, #1055 by title only.
- `papers/SM.md`, `Structure.md`, `Introduction.md` and the book were searched for "full
  equivalence/equality" and "bare OI" only; Main §2 and §3.1–§3.2 were read at heading level.

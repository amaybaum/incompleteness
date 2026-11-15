# RO-3: carrier and exactness inventory, r6

**UNREVIEWED.** r6 revises r5, which is left unchanged, as are r1–r4, `OBL-RO3-2-r1.md`,
`OBL-RO3-2-r2.md` and every review. It applies the independent review of r5 (delivered as
`REVIEW-1303-INVENTORY-r5.md`, ACCEPT WITH CHANGES, no label refuted; SHA-256
`16b5d919d9a1b44cad60c55eaead6d258db8676bdc6316184f5de23445faa8d1`): its required changes H1–H5,
the minor items H6 and H6′, and the completion of findings F6–F12 of the review of r4, which it
found applied only in part. The disposition of each item is in `RESPONSE-r5.md`. r6 has not been
reviewed.

**Goal link.** Priority item 2: the A1 dependence of the main equivalence (§7.3).

Changes from r5:
- Standing: the scope of the map is stated as bounded by the searches of §5 (H3); the D-CQ reading
  covers the exclusion purpose of answer 4's last sentence (H4); the r6 authorization record.
- Labels: the full "support off `main` (PR #1303)" label at every OBL-class statement, including
  1.2 G-fact, §0, 2.3, the §3 preservation controls and AM-16 (H5, completing F6 and F7).
- §1.6: the audit's qualifier on the equivalence (H2).
- §3: the review's recommended first recovery target, recorded as a recommendation only, with its
  first missing step, controls, countercontrols and decision rule. No target is chosen.
- §4 Q13: answer 4's last sentence quoted verbatim, with its exclusion purpose read as amended (H4).
- §5: the statement of what the map's search covered, corrected (H3).
- §6: the "Use here" cell of the OBL row extended (H5).
- §7: AM-3 (H6), AM-5 (H1), AM-7 (H6′), AM-1, AM-11, AM-15–AM-17 (mirrors, H3), new rows AM-20 to
  AM-26 (H3), §7.2 (census 53, H3), and §7.3 rewritten (H1, H2). This completes F8–F11.

r5's changes from r4: Standing (authorization, base `7ac74a4b`, ledger on `main`, scope, review
status of r4, D-CQ); the OBL-RO3-2 label; the OBL class in §0; the OBL-class cells of 1.1–1.3; 1.1
G-fam; 1.4; 1.6; 1.7 F; 2.3, 2.5, 2.6, 2.7; §3; §4 Q2, Q6, Q9, Q13; §5, §6; and the new §7. They
applied findings F1–F17 of the review of r4 (`REVIEW-r4.md`, delivered as
`REVIEW-1303-INVENTORY-r4.md`, SHA-256 `f06d9f16…4e20`); dispositions in `RESPONSE-r4.md`.

Review status of r5: independently reviewed, ACCEPT WITH CHANGES (above). No label of r5 was
refuted at its stated scope.

Review status of r4: the focused confirmation `REVIEW-OBL-r2.md` (ACCEPT, at `ef8d353e`) checked
r4 against r3 (its §3), and `REVIEW-OBL-r2-ADDENDUM.md` checked r4's links among recurrence, exact
return and P-indivisibility. The independent review of r4 as an inventory is ACCEPT WITH CHANGES
(`REVIEW-r4.md`).

Earlier revisions: r4 applied item m8 of `REVIEW-OBL-r1.md` (one wording correction). r3 applied
nits N1–N3 of ChatGPT review 5906337933 and recorded the Q10–Q12 decisions (#914 comment
6883249235). r2 applied `REVIEW-r1.md`; its dispositions are in `RESPONSE-r1.md`.

## Standing

- **Authorization of r6.** Requested by the coordinator after the independent review of r5. No owner
  comment authorizing r6 by name was found on #914, #1055, #1169 or #1303 after 2026-11-15T11:34Z.
  The authorization below covers r5 and its independent review; whether it covers r6 is for the
  owner to confirm.
- **Authorization of r5.** #1169 comment 6893687398 (`amaybaum`, 2026-11-15T11:33:23Z). The owner
  decision, quoted verbatim: "Confirmed, proceed as suggested". Its #1303 row, quoted verbatim:
  "Write inventory r5, applying the 17 findings of the independent inventory review (ACCEPT WITH
  CHANGES), followed by an independent review. No #1055 recovery target is chosen before then."
  The same comment, quoted verbatim: "**Not authorized:** merges, CI dispatch, new premises,
  manuscript promotion or any status upgrade."
- **Authorization of RO-3.** #1055 comment 6881390849 (`amaybaum`, 2026-11-14T17:23:23Z), quoted
  verbatim: "Yes, I authorize RO-3 on these terms". Writer: Claude Code. Reviewers: separate
  non-author agents (#1169 comment 6893687398).
- **Scope.** The owner's Q5 text, #1055 comment 6880024537 (2026-11-14T15:46:34Z), quoted verbatim:
  "Inventory recurrence, recurrence-based P-indivisibility and A.8 cycle averages for each candidate
  carrier. Preserve their finite-carrier scopes and identify what extra hypotheses or replacement
  proofs a completion would require. Include finite stages as an intermediate case and countable or
  infinite completions as candidates. The ultimate test remains one fixed underlying model
  supporting arbitrarily large finite quantum carriers with explicit encodings and resources."
- **Scope of this record.** §1–§6 cover the Q5 family: recurrence, recurrence-based
  P-indivisibility and the A.8 cycle averages, with the exactness context of 1.7. They are not an
  inventory of A1's consumers. §7 maps the consumers of A1 that the searches of §5 found in the
  papers, the book, the Lean modules and the verification records. It is bounded by those searches
  and is not a complete corpus closure. For each result that uses A1 it gives where A1 enters, what
  survives without it, and the status at proved scope. §7 recovers nothing and changes no status.
- **Target this serves.** EXACT, #1169 comment 6877981234 ("exact operational law-equality across
  the agreed interface, with carrier, encoding, resources and any completion policy explicit"),
  with its prerequisite set in #1169 comment 6880022363.
  - The target theorem (#914 comment 6875046763): "the target cannot assume one fixed finite total
    carrier. An infinite or completed carrier is an admissible candidate, but its sufficiency is not
    established. Finite access by an embedded observer must remain distinct from finiteness of the
    underlying dynamics."
  - Gate A answer 3 (#1169 comment 6876591512): "One fixed model, with one common extension E, must
    support subsystems realizing every quantum carrier in the agreed scope. ... The ultimate model
    must accommodate arbitrarily large finite carriers, with the permitted encodings and resource
    requirements stated explicitly."
  - Gate A answer 4 (same comment), quoted in full: "Require quantum behaviour for every physically
    performable experiment within C. This includes accessible preparations, interventions,
    compositions and complete records under the retained contract. Access closure must prevent a
    model from qualifying through selected quantum experiments while also permitting
    stronger-than-quantum experiments."
  - **D-CQ, the C/Q target decision.** #1169 comment 6891338304 (`amaybaum`, 2026-11-15T07:54:33Z,
    "RO-1: owner decision — the hypothesis and the C/Q distinction (target amended)"; the owner's
    words: "Ok sounds good to me"). The comment does not carry the label; #914 comment 6893722503 §3
    cites it as D-CQ. Quoted verbatim:
    - "**C (physical sector)** is defined independently, by the limits of embedded observation.
      Nothing in its definition refers to quantum outcomes. The noncircularity requirement on C
      stands."
    - "**Coverage is required.** C contains realizations of the quantum phenomena we perceive."
    - "**Agreement with performed experiments is required.** Whatever OI predicts inside C for an
      experiment that has already been performed must match the observed data".
    - "**The relation between C and Q is open.** It is a question to discover, not a requirement. C
      may lie inside Q (soundness), or C may intersect other subsets of OI with different
      properties. An intersection with stronger-than-quantum behaviour in experiments not yet
      performed would be a testable prediction, not a defect."
    - "This amends the soundness requirement in the Gate A answers (c.6876591512). Soundness is now
      an open question, subject to the agreement-with-data requirement. Coverage remains required,
      and necessity remains optional."
    - In the restated AC-1: "Excluding PR is no longer a goal."
    - "This decision adopts no new physical premise and authorizes no new work, merge or
      computation."
  - **How D-CQ bears on answers 2, 3 and 4.** D-CQ names "the soundness requirement in the Gate A
    answers" without numbering the answers. The reading below is the inventory's ([IR]).
    - **Amended.**
      - Answer 2's soundness half, "Require coverage and soundness": soundness is open; coverage
        stays required.
      - Answer 4's first sentence, "Require quantum behaviour for every physically performable
        experiment within C": quantum behaviour for every performable experiment within C is an
        open question, and agreement with performed experiments is required.
      - The exclusion purpose of answer 4's last sentence. The sentence reads: "Access closure must
        prevent a model from qualifying through selected quantum experiments while also permitting
        stronger-than-quantum experiments." Its purpose of barring a model that permits
        stronger-than-quantum experiments is what D-CQ sets aside: "Excluding PR is no longer a
        goal", and such an intersection "would be a testable prediction, not a defect".
    - **Not amended by D-CQ's text.**
      - Answer 4's second sentence, the experiments counted: "accessible preparations,
        interventions, compositions and complete records under the retained contract".
      - Answer 3, one fixed model accommodating arbitrarily large finite carriers, a coverage
        requirement.
    - **Open.** Whether the anti-selection part of access closure, that a model may not qualify
      through selected quantum experiments, survives as a coverage and agreement-with-data
      condition. #914 comment 6893722503 §4 states this as a proposal, not adopted (Q13).
    - #914 comment 6893722503 §3 lists r3's "§7 answers 2 and 4" as still stating soundness, which
      agrees with reading answers 2 and 4 as amended.
- **OBL-RO3-2.** The owner accepted the direct proofs of `OBL-RO3-2-r2.md` at its stated scope (#914
  comment 6883931412, `amaybaum`, 2026-11-14T20:43:54Z, item 2): "The direct proofs in
  `OBL-RO3-2-r2.md` are accepted in place of the Halmos/Rokhlin primary-source check that was not
  completed." and "The result is mixing under Haar measure, within its hypotheses." The same decision is recorded on #1055 (comment 6883932722). The
  same item keeps open "`referenceState` invariance, physical realization at the interface, and
  P-indivisibility itself". The acceptance covers that unit only. Cells that rest on it carry the
  label defined below and are moved at the OBL class only.
- **Limits.** Paper-only. Reading, analysis and writing. No computation on OI rules, no Lean, no
  simulation, no repository edit. This record adopts no premise, completion, sector condition C or
  extension E, changes no scientific status and no planning entry, chooses no #1055 recovery target,
  and decides nothing on RO-1 or #1143. EXACT stays open. A1 is a posit throughout; no passage
  assumes the total substratum finite except where A1 is named.
- **Base.** Corpus read at `main` `7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`. r4's base was
  `dfeec843bec08443b25cffe34d33dc8401c3b604`. Between the two, the only changes under `papers/`,
  `book/`, `verification/lean*`, `verification/programmes/substratum/` and
  `verification/audits/manuscript/` are in `book/ch10`, `ch18`, `ch19`, `appendix-a`, FULL,
  `papers/Complexity.*` and a new batch-integration record. Every `path:line` citation retained
  from r4 points to the same text at `7ac74a4b`. New citations in r5 are read at `7ac74a4b`.
- **Ledger.** On `main` at the base:
  `verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/LEDGER-r8.md` (blob
  `d6ceba532ed4e31c4b7e6b2e872887a9e6e039c5`, the same blob as on
  `records/unified-ledger-914-20261114` at `9ff3b8d913abfe720273ff162f6340054cb69437`) and
  `LEDGER-r9.md` (blob `7c69662ad04430a2554d07614dea0e3412b69b73`), retained through #1304 (#1169
  comment 6891337868).
  - The owner accepted r8 (#914 comment 6880700869, `amaybaum`, 2026-11-14T16:31:06Z, quoted
    verbatim: "Yes. I accept ledger r8 as the successor to r5."). r9 is accepted and on `main`
    (#1169 comment 6891337868).
  - On the identifiers cited here (B-QM-1, B-QM-4, B-QM-5, B-QM-8, B-QM-9, B-QM-16, B-QM-27,
    B-BH-3, J-3, J-4, M2, M5, QM–BH, QM–A1, §8.4, §8.5), r9 adds four rows and changes no cited row.
    One uncited row (A-QM) changes a count. "Ledger" below means these rows, whose text is the same
    in r8 and r9.
- **Citations.** `path:line` refers to physical lines at the base. `papers/*.md` paragraphs are
  single long lines, so one line number can cover a whole theorem. Lean modules are under
  `verification/lean-mathlib/OIBridge/`; they were read, not built. Census family numbers are the
  indices of `families` in `verification/lean-manuscript-census.json`. In §3, §4 and §7,
  `Main:n`, `GR:n`, `SM:n`, `Sub:n`, `Struct:n`, `Meth:n` and `Comp:n` abbreviate
  `papers/Main.md:n`, `papers/GR.md:n`, `papers/SM.md:n`, `papers/Substratum.md:n`,
  `papers/Structure.md:n`, `papers/Methodology.md:n` and `papers/Computation.md:n`; `OBL` is
  `OBL-RO3-2-r2.md`.

### Status labels

- **established**: proved at the cited layer for the statement as made, at its stated scope. The
  layer is given: K (kernel on `main`), P (paper proof in a manuscript), EX (exhaustive or exact
  finite computation on `main`).
- **conditional[...]**: proved given the bracketed hypotheses, each with its status at source
  (posited, open, or a named hypothesis).
- **refuted within <class>**: a result on `main` shows that the property fails for every member, or
  for a stated member, of that class. A cell whose refutation rests in part on an imported external
  theorem names that theorem as a cited input.
- **established for that rule and measure, support off `main` (PR #1303)**: proved on paper in
  `OBL-RO3-2-r2.md` (PR #1303, commit `ef8d353e4c05e6e4de2f813478bc279f3fa00eb4`, blob
  `b1edb95f9ed0f331c06f5ecbc69a806dc6631562`, unchanged at head `78089e5e`), for the OBL class of
  §0. The proof was independently reviewed (ACCEPT, with a focused confirmation and an addendum)
  and accepted by the owner at its stated scope (#914 comment 6883931412, item 2). It is not on
  `main`. Under AGENTS.md §A.42 item 8 this is support off `main`, a gap until the record lands.
  Under §A.46 item 1 a claim resting on it is not established on `main`. A refutation proved there
  is written **refuted within the OBL class, support off `main` (PR #1303)**. These labels are used
  for the OBL class only.
- **open**: no proof and no refutation on `main` at the stated scope.
- **RR**: a research record on `main` whose own status note says its proofs are paper-level and not
  independently reviewed (`verification/programmes/substratum/continuous-substates/README.md:3`,
  :23–32). Under AGENTS.md §A.46 items 1 and 7 an RR item is not established and is not used here as
  a premise. Where an RR item bears on a cell, the cell keeps its status and the RR item is listed as
  context.
- **[IR]**: a reading made by this inventory or by a review, not stated on `main`, not
  independently verified. An [IR] item is context or a candidate for a later obligation. No cell's
  status rests on it.

## 0. Three carriers, and the classes compared

The question involves three different carriers, and the inventory keeps them apart.

1. **The total substratum carrier** `S`, with its bijection `φ`. A1 says `S` is finite
   (`papers/Substratum.md:92`). A1 is a posit: item (ii) of the posit ledger
   (`papers/Main.md:724`), "the total-finiteness posit" (`papers/Main.md:60`). The Definition and
   the two axioms do not fix the cardinality of `S` (`papers/Main.md:60`). This inventory keeps A1
   as a posit.
2. **The accessible visible carrier** `C_V`. It is finite by Lemma 1 (`papers/Main.md:46`), a theorem
   from the finite-capacity clause, with its physical premise exposed in the kernel as a finite set
   of boundary modes (`Finiteness.lean:66`); finitely many settings per mode is not enough
   (`Finiteness.lean:104`). Lemma 1 does not supply finiteness of `S` (`papers/GR.md:138`;
   `papers/Main.md:60`).
3. **The operational quantum carrier**: the finite index set of the complex matrices on which an
   operational theory acts (`papers/Main.md:562`, `FiniteOperationalTheory` in
   `OperationalAssembly.lean`). "Arbitrarily large finite quantum carriers" in the target refers to
   this carrier.

Recurrence and the A.8 cycle decomposition are properties of carrier 1, or of a finite invariant part
or finite factor of it. P-indivisibility is a property of the rooted visible maps on carrier 2 that
carrier 1 induces. Exactness is a property of the operational theory on carrier 3. A statement about
one of them does not transfer to another without a stated map.

**Classes compared.**

| Class | What it is | One fixed model? |
|---|---|---|
| **F** finite carrier | one fixed finite `S`, `φ` a bijection, A1 as a hypothesis | yes |
| **G-fam** growing finite stages, as a family | finite models of increasing size, each its own model: the side-`L` torus over `Z/q` (`papers/SM.md:296`, :1606), alphabet change (`papers/Substratum.md:255`), the per-accuracy realizations `R_n` (`papers/Main.md:596–598`), the per-horizon dilations (`papers/Main.md:516–520`) | no: a family of models |
| **G-sub** finite invariant sub-carriers of one model | finite `φ`-invariant subsets of one fixed model: a finite representative of a constraint surface (`papers/GR.md:587`); RR: the finite subgroups `(Z/N)^{2L}` of the torus `(R/Z)^{2L}` (`continuous-substates/README.md:105–107`). Finite regions of an interacting model are not in this class: they are not invariant (2.3) | yes |
| **G-fact** finite factors of one model | finite models that are factors of one fixed model: a map onto the finite model that intertwines the dynamics and pushes the fixed model's normalized prior forward to the finite model's prior. RR: `(Z/p^k)^{2L}` as factors of `(Z_p)^{2L}` under Haar measure (`continuous-substates/README.md:113–121`, :135–137) | yes |
| **I-deep** infinite deep sector | finite visible sector and finite causal cone, with an infinite deep sector carrying a normalized product prior, a locally finite coupling graph and updates that depend on finitely many components (`papers/GR.md:132–134`) | yes |
| **I-qloc** infinite-region completion | the quasilocal algebra at fixed spacing, with the finite-range update as a `*`-automorphism (`papers/Main.md:588`; `verification/audits/operational/quasilocal-completion-audit.md`) and the tracial `referenceState` (`QuasilocalAlgebra.lean:901`) | yes |
| **I-meas** general infinite probability-preserving carriers | countable or continuous sub-states, or other infinite carriers with a normalized invariant measure and a measurable bijection; also continuous-time flows (`papers/Main.md:155`; #1007 options (b), (c)) | yes |
| **OBL class** (a member of I-meas; read in I-qloc through (ii-a) and (ii-b) of 2.5) | the posited linear rule `F(u, v) = (v, Av − u)`, `A = α Σ_j (T_j + T_j^{-1})`, on `X = ((F_p)^2)^{Z^d}`, `d ≥ 1`, `p` prime, `α ≠ 0`, with the uniform product measure `μ`, which is Haar measure (`OBL-RO3-2-r2.md` §0, Step 1). Composite `q`, nonlinear rules, the gauge-coupled rule and every other invariant measure are outside it (OBL §0) | yes |
| **I-nonorm** infinite carriers without a normalized invariant prior | for example an infinite invariant measure | yes, but no rooted law is defined |

Class I-nonorm is listed so that it is not silently merged with I-meas. Every rooted map below is a
probability under a normalized prior, and the corpus states that an infinite extension needs "its
own normalized measure or trace-class state and a well-defined evolution"
(`papers/Substratum.md:262`; also :52, :92; `book/ch02-substratum.md:32`).

Every infinite class above takes a bijection, measurable where a measure is given, as part of its
definition. The corpus derives bijectivity from injectivity through A1 (§7, row AM-3). On these
classes bijectivity is therefore a hypothesis of the class, not a consequence.

G-sub and G-fact differ in how a finite model sits inside the fixed model:
- A finite invariant sub-carrier carries a finite model only for preparations supported on it. In an
  infinite model such a subset is a global constraint, not a subsystem. Under a prior of full
  support it has measure zero. This holds for the periodic sectors of 2.3 and the finite tori under
  `μ` in the OBL class (OBL §4.1; established for that rule and measure, support off `main` (PR
  #1303)), and [IR] for `(Z/N)^{2L}` under Haar measure
  on the torus.
- A finite factor carries a finite model under the fixed model's own normalized prior, for readouts
  that factor through it.

## 1. Source-pinned comparison table

Rows are result × class. "Hyp." names the hypotheses each cell needs beyond the class definition.

### 1.1 Exact recurrence (`φ^L = id` on the carrier)

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (P; K) | A1 (posit); `φ` bijective (A2) | `papers/Main.md:121` (Step 1), :60 (the representative is "defined here for a finite system only"); K: `iterate_return_at_order` (`RootedRecurrenceBridge.lean:47`, census 114, kernel-only) |
| G-fam | established for each member; no common period across members | each member finite and bijective | the side-`L` ring with the unit-coefficient circulant adjacency, prime `q` with `gcd(L, q) = 1`: order `qL` (`papers/SM.md:1606`, Theorem A.1); the `d`-dimensional torus with any translation-invariant coupling over `F_p`, prime `p ∤ L`, `L ≥ 2`: `F^{p(p^{2m}−1)} = I` with `m = ord_L(p) ≤ L−1` (`papers/SM.md:296`) |
| G-sub | conditional[the stage is a finite `φ`-invariant sub-carrier] | invariance and finiteness of the stage | `papers/GR.md:587` (a finite representative of the constraint surface, invariant under `φ`, has finite order `L`). RR context: `(Z/N)^{2L}` in the free 1-D torus map (`continuous-substates/README.md:105–112`) |
| G-fact | recurrence of the finite factor: as F for the factor; the fixed model need not recur | the factor map intertwines the dynamics | RR context: the `p`-adic case (`continuous-substates/README.md:113–121`) |
| I-deep | open; not inherited | — | "The recurrence proof ([Main, §2.3]) requires S finite, which Lemma 1 does not supply" (`papers/GR.md:138`); the transfer corollary "does not imply recurrence of every unobserved sector" (`papers/Substratum.md:268`) |
| I-qloc | open in general. OBL class: refuted within the OBL class, support off `main` (PR #1303), for the configuration map | OBL class | none on `main` (search in §5). OBL 3.2: `F^n ≠ id` for every `n ≥ 1`; no nonzero finitely supported configuration is periodic. [IR] for the algebra: `heisQ^n ≠ id`, because on diagonal stage elements `heisQ^n` acts as `f ↦ f ∘ F^n` (2.5, (ii-b)) and cylinder functions separate points |
| I-meas | open in general as a microscopic statement. OBL class: refuted within the OBL class, support off `main` (PR #1303) | OBL class | `papers/Main.md:155` is a visible statement for continuous-time flows; see 1.2. OBL 3.2: `F` has infinite order; Poincaré recurrence holds `μ`-almost everywhere in the product topology; the periodic points form a `μ`-null set, uncountable for `d ≥ 2`. Neither almost-everywhere recurrence nor a null set of periodic points is exact common visible return (1.2; `REVIEW-OBL-r2-ADDENDUM.md`). RR context: `continuous-substates/README.md:85–91` |
| I-nonorm | no statement possible | — | no normalized prior (`papers/Substratum.md:262`); #1055 body lists the infinite-measure case as a test case |

### 1.2 Exact common visible return (`Γ_L = I` for the rooted maps)

This is the hypothesis the P-indivisibility proofs actually consume (`papers/Main.md:137`, :141).
Main's rooted maps use an independent root and one root-shared hidden prior
(`papers/Main.md:135`, :141). Cells that use another convention say so.

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (P; K) | as 1.1, plus the product carrier `C_V × C_H` with `π` the first projection and a root-shared `μ_H` (H-product) | P: `papers/Main.md:137` (`Γ_L = I`); K: `rootedMap_at_order` (`RootedRecurrenceBridge.lean:55`, census 114, kernel-only), `rootedMap_periodic` (`RootedClassification.lean:135`, census 40, current). H-product as a named assumption: `verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md:290` (audit record; its review independence is not established, :17–19) |
| G-fam | established for each member, at that member's period | as F | as 1.1 |
| G-sub | conditional[invariant finite stage; prior supported on the stage, on each root's fibre] | as F, on the stage | `papers/GR.md:587` (`K_{mL} = I`) |
| G-fact | conditional[the readout factors through a finite factor; the factor map intertwines the dynamics and carries the prior to the factor's prior; H-product on the factor] | as stated | [IR]: under these hypotheses the rooted law computed in the fixed model equals the factor's rooted law, so the factor's return applies. RR instance: the lowest-digit readout of the `p`-adic free map, with `Γ_{ord(F mod p)} = I` "for every sub-state" (`continuous-substates/README.md:113–121`, :135–137). OBL class: no nontrivial finite factor exists, refuted within the OBL class, support off `main` (PR #1303) (2.3; OBL 3.4) |
| I-deep | open | — | none on `main`. For a deep factor that no dynamics couples to the boundary, the finite identity (`papers/Substratum.md:257–262`) would carry the finite visible return over, but its infinite form needs "its own normalized measure or trace-class state and a well-defined evolution, and is not established" (:262) |
| I-qloc | open in general. OBL class: refuted within the OBL class, support off `main` (PR #1303), for readouts of the diagonal (rooted laws formed from the diagonal of `referenceState`), in the cell-conditioned convention; in Main's root-shared convention for restriction readouts `π = res_Λ` only | OBL class; (ii-a) and (ii-b) of 2.5 | OBL 3.1 with OBL §5 (ii-a), (ii-b). The rooted laws are diagonal, so (ii-c) is not needed (OBL §5) |
| I-meas | conditional[`π ∘ T^L = π` almost everywhere]; open otherwise. OBL class: refuted within the OBL class, support off `main` (PR #1303) | a measure; a finite visible partition with cells of positive finite measure. OBL class: every readout with at least two cells of positive measure, `V` restricted to its cells of positive measure | K, cell-conditioned convention: `measuredGamma_eq_one_iff` (`ObservableMeasureReturn.lean:83`; census 120, kernel-only) defines the rooted entry as the ratio of joint-cell mass to initial-cell mass, takes an arbitrary measure, needs positive finite cell masses, and does not use invariance (its docstring, :79–82; header, :14–20). It agrees with Main's convention under H-product. P in RR: `continuous-substates/observable-recurrence.md:15–36`. Main: for continuous-time Hamiltonian flows, near-total common visible return fails at every sufficiently late time for a mixing flow (`papers/Main.md:155`). RR instances: difference readouts of the free 1-D torus wave map and lowest-digit `p`-adic readouts return exactly; the single-site real readout does not (`continuous-substates/README.md:85–121`, :125–144). OBL class: OBL 3.1. In the cell-conditioned convention the refutation covers every readout. In Main's root-shared convention it covers restriction readouts `π = res_Λ` only; a coarse-grained readout with unequal fibres has no root-shared hidden prior in Main's product form (OBL lines 221–228) |
| I-nonorm | no statement possible | — | as 1.1 |

Context. In discrete time, `Γ_n = I` for one `n > 0` makes each visible cell `T^n`-invariant up
to null sets, hence `Γ_{kn} = I` for every `k`. A mixing system sends `μ(C_a ∩ T^{-kn} C_a)` to
`μ(C_a)^2`, which differs from `μ(C_a)` for a cell of measure strictly between 0 and 1. So a mixing
system with a nontrivial finite partition has no positive-time exact visible return. For the OBL
class this is OBL 3.1, with the mixing of OBL Step 8 (established for that rule and measure, support
off `main`, PR #1303). For a general mixing system it is the same argument, and it is [IR] here.
Main states the continuous-time, late-time form for Hamiltonian flows (`papers/Main.md:155`).

### 1.3 Recurrence-based P-indivisibility

The results: the one-step theorem (`papers/Main.md:113–127`); history readback with finite recurrence
(:135–139); overlap and return (:141–143); the constraint-surface form (`papers/GR.md:587`); and the
CP-indivisibility theorem that rests on them for the permutation-dilation family
(`papers/Main.md:330`; listed among the uses of the finite representative at :60; its per-class row
is §7, AM-2). Book mirrors: `book/ch01-observation.md:95–109`;
`book/appendix-b-derivations.md:92`, :413.

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (P; K for the final steps) at recurrence-cycle scope only | A1 (posit); A2; H-product; some rooted map not a permutation (under the uniform prior for :113; any root-shared prior, full support not needed, for :141) | P: `papers/Main.md:113–127`, :135–139; K: `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`, census 34, current), `isPermMatrix_of_stochastic_inverse` (`EquivalenceChain.lean:110`), `pIndivisible_at_order_of_nonperm` (`RootedRecurrenceBridge.lean:104`, kernel-only). Paper-only steps are listed at `papers/Main.md:137`. Scope: "a global recurrence-cycle result", not a statement about accessible windows (:139, :157; `papers/GR.md:587`) |
| G-fam | established for each member at that member's recurrence scale | as F, per member | as F. The recurrence time grows with the member (1.1); a statement on a window `t ≪ t_R` is a different claim (`papers/Main.md:139`, :536; `book/appendix-b-derivations.md:417`) |
| G-sub | conditional[finite `φ`-invariant stage; prior on each root's fibre; a non-permutation rooted map] | as F, on the stage | `papers/GR.md:587` (P; ledger B-QM-27, CD). RR context: the `(Z/N)^{2L}` subgroups (`continuous-substates/README.md:105–112`) |
| G-fact | conditional[the hypotheses of 1.2 G-fact; a non-permutation rooted map of the factor] | as stated | the matrix-level theorems below apply to the factor's rooted family. RR instance: the `p`-adic lowest-digit readout (`continuous-substates/README.md:113–121`) |
| I-deep | open | — | "P-indivisibility at the recurrence scale is proved on a finite representative, while for an infinite deep sector the readback lemma ... gives the weaker accessible-window property, conditional memory" (`papers/GR.md:138`; also :585; `papers/Substratum.md:268`) |
| I-qloc | open. OBL class: the recurrence route is unavailable, because its identity-return hypothesis fails, established for that rule and measure, support off `main` (PR #1303); P-indivisibility itself open | — | OBL 3.3, through 1.2 I-qloc |
| I-meas | conditional[exact common visible return `Γ_L = I` (1.2); a real row-stochastic rooted family with a root-shared normalized prior; an earlier non-permutation `Γ_s`]. Without the return hypothesis: open. OBL class: the recurrence route is unavailable, established for that rule and measure, support off `main` (PR #1303); near-total common return at sufficiently late times excluded; at bounded times open; P-indivisibility itself open | as stated | the matrix-level theorems need only row-stochastic rooted matrices and an identity return: `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`, census 34, current; "the matrix form ... assumes only that Γ_s is row-stochastic", `papers/Main.md:143`), `pIndivisible_of_visible_identity_return_nonperm` (`ObservableFactorRecurrence.lean:68`, census 120, kernel-only). Gap: "Neither module supplies a measurable, real row-stochastic rooted law or composes the measure-based identity with the P-indivisibility result" (`ObservableFactorRecurrence.lean:20–22`; `ObservableMeasureReturn.lean:17`). Continuous time: "Continuous-time P-indivisibility for general Hamiltonian flows is open" (`papers/Main.md:155`). OBL class: OBL 3.3. The route's hypothesis fails; the route itself is not refuted, and not-(b) is not used to infer P-divisibility (`REVIEW-OBL-r2-ADDENDUM.md`). RR context: on infinite reversible carriers with normalized invariant measures, rooted families that are P-divisible at every finite time, one of them with an order-1 C4 gap (`continuous-substates/infinite-xor-counterexample.md:25–27`; `continuous-substates/solenoid-countercontrol.md:41`) |
| I-nonorm | no statement possible | — | rooted maps undefined |

### 1.4 All-time rooted classification (`C_OI(V) = P_per(V)`)

Included because it is the finite-carrier result whose necessity half rests directly on recurrence,
and so it shows what a completion changes.

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (K) | finite `V` and `H`; one bijection; one root-shared prior | `finiteRootedRealizable_iff_pper` (`RootedClassificationAllTime.lean:192`, census 40, current); `papers/Main.md:638`. The two directions have separate witnesses (AGENTS.md §A.34): forward, `pper_of_finiteRootedRealizable` (`RootedClassification.lean:339`); reverse, `pper_has_responseRealization` (`RootedClassificationAllTime.lean:162`) |
| G-fam | established per member (each periodic) | as F | as F |
| G-sub, G-fact | [IR]: the kernel theorem applies to the stage or factor if it is itself a product `C_V × C_H'` with a root-shared prior. No source states the transfer | H-product on the stage or factor | the kernel statement needs `RootedRealization` on `V × H` (`RootedClassificationAllTime.lean:176–193`). GR:587's constraint surface correlates interior and exterior and uses fibre priors, so it is not of that form as stated |
| I-deep, I-qloc, I-meas | necessity half not inherited; open whether the realizable class is larger | — | the forward (necessity) direction is `pper_of_finiteRootedRealizable` (`RootedClassification.lean:339`), which the theorem's docstring describes as "resting on finiteness of `V × H` and reversibility" (`RootedClassificationAllTime.lean:182`); the visible period it asserts comes from the finite order of the microscopic permutation (:186–191). With `H` infinite, that step is unavailable. RR context: nonperiodic rooted families on infinite hidden carriers (`continuous-substates/infinite-xor-counterexample.md:21–25`; `solenoid-countercontrol.md:41`; `README.md:85–88`). [IR] context, from the review of r1: the Bernoulli shift on `{0,1}^Z`, read at coordinate 0 with a root-shared product prior, gives `Γ_0 = I` and `Γ_t = J` for `t ≥ 1`, a nonperiodic realizable family |
| I-nonorm | no statement possible | — | — |

### 1.5 A.8 cycle typicality and the A.9 cycle-averaged Page curve

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | conditional[H-scramble; the full product energy shell on `B ∪ R`]. Refuted within the counted setting: for definite initial configurations at bipartitions aligned with the configuration coordinates, H-scramble fails for every bijection and "the theorem as stated has no instance". Open outside that setting | `B ∪ R` invariant under `φ` as one shell; A.9 also H-decouple | `papers/GR.md:797–821` (the finite cycle decomposition is used at :807); no instance: :805, :813, :823 (P; ledger B-BH-3, DM NEG). Established for every bijection at aligned bipartitions: `S(ρ_R(t)) ≤ H(p_0)` (:823–827). Not given: an ensemble restatement (:827). Open: proper shells (:829); single-trajectory entropy (:839). A.9: :831–837 |
| G-fam | as F, at each stage | as F | A.9 already uses stages `d_B = q^{n_B(t)}` with the bipartition of each stage held fixed (`papers/GR.md:831`, :839) |
| G-sub | as F, with the shell as the invariant finite stage | the shell's invariance is A.8's own hypothesis | `papers/GR.md:797`, :807 |
| G-fact | open | — | no source |
| I-deep, I-qloc, I-meas | open; no counterpart of the cycle decomposition is stated | would need a normalized invariant measure, time averages in place of cycle averages, and the excluded fraction counted in that measure | `papers/GR.md:807` (finite `Σ_E`), :827 ("not given here"). Ledger §9 row QM–BH and J-4 record the same: "undetermined on a completion, where A.8's finite cycle decomposition would need a counterpart (not stated)". The ledger reads the aligned-bipartition failure as coming from configurations being mapped to configurations, not from finiteness (ledger §8.5, citing `papers/GR.md:813`, :823). Whether that failure carries to an infinite carrier is not stated |
| I-nonorm | no statement possible | — | — |

### 1.6 Preserved results: the #1055 controls and the other results that do not use A1

The #1055 body lists the controls any revision must preserve: the finite-horizon equivalence
`S ⟺ D ⟺ Q_fb`; readback and C4 content; reverse finite realization; every finite-carrier theorem;
the phase-locking lemma under (G1)–(G4); Theorem 24(iii) for finite normalized decoupled factors;
and the observer-relative finiteness reading merged in #1053 and #1054. "Every finite-carrier
theorem" covers the F cells of 1.1–1.5. The others are in the table below.

| Result | Status in every class, at its stated scope | Source |
|---|---|---|
| Lemma 1 (finite visible resolution) | established (P; K conditional on finite modes). It bounds carrier 2, not carrier 1 | `papers/Main.md:46`; `Finiteness.lean:66`, :104 |
| Readback lemma; C4 content (accessible conditional memory) | established; uses only Lemma 1 (`papers/Main.md:60`). For I-deep it is the property the source carries there (`papers/GR.md:138`, :585) | `papers/Main.md:60`, :157 |
| `S ⟺ D ⟺ Q_fb` on every finite horizon | established (K in part); a statement about finite visible laws, whatever the carrier. It uses only Lemma 1, "in which a finite hidden space is constructed, not assumed" (`papers/Main.md:60`). It is "existence of finite representatives of finite visible laws; not a characterization of the actual infinite substrate" (DEPENDENCY-AUDIT.md:282, audit record). The physical reading of the characterization theorem is conditional on A1 (`papers/Main.md:60`; §7, AM-20); see §7.3 on #1169 comment 6893456888 | `papers/Main.md:60`, :546, :552; ledger B-QM-1 |
| Reverse finite realization | established at its scope: "every finite stochastic law, including every finite quantum record, has a finite reversible OI realization; bounded quantum instrument families are uniformly realizable to arbitrary finite accuracy". The dilations construct a finite hidden space; they do not assume one (`papers/Main.md:60`) | `papers/Main.md:80` item (3), :516–520, :596 |
| Phase-locking lemma under (G1)–(G4) | preserved unchanged. The lemma is a statement about a Hermitian operator on `C^n`, and its ancilla-marginal form about the dilated space of dimension `n m_a`; it does not consume A1 as stated. Its application to the substratum's emergent Hamiltonian on the §3.2 setup runs through that setup's finite hidden space (§7, AM-19) | `papers/Main.md:228–260` |
| Theorem 24(iii), finite decoupled enlargement | established (P); finite factors only; infinite form not established | `papers/Substratum.md:257–262`, :268 |
| Observer-relative finiteness reading | the cardinality of `S` is not fixed by the Definition and the axioms; accessible finiteness does not establish total finiteness | `papers/Main.md:60`; `papers/Substratum.md:54`, :92 |
| Deep-sector cardinality on `[0, nΔt]` | established (P). For I-deep it is exact, "given a normalized product prior on it, a locally finite coupling graph and well-defined dynamics ... in which each component's update depends on finitely many components" | `papers/GR.md:132–134`, :138 |

These hold at their stated scope in every class, and nothing in this inventory narrows them. They
carry the distinction between finite access and total finiteness: on a finite horizon the visible
data do not fix the size of the carrier beyond the causal cone (`papers/GR.md:138`).

### 1.7 Exactness and quantum carriers (context for the fixed-model test)

| Class | Status | Source |
|---|---|---|
| F | refuted within one fixed finite realization under the ordinary factorization interface, conditional on the imported unboundedness theorem [55] (external, cited input: Heinosaari, Kerppo, Leppäjärvi and Plávala, *Phys. Rev. A* **109**, 032627 (2024), `papers/Main.md:901`): no fixed finite realization is exactly operationally equivalent to a qubit's full theory. The factorization half is proved at `papers/Main.md:558`; the unbounded nonnegative rank is imported | `papers/Main.md:558`, :600 item (3); ledger B-QM-8, J-3 |
| G-fam | established as approximation. For each `(d, m, K, ε)` one finite reversible realization is mutually `ε`-dense with operational QM at horizon `K`. Density holds along `K_n → ∞`, `ε_n → 0` at fixed `(d, m)`; the union over `(d, m)` "is a further limit, not taken here"; "The exact continuum theory stays unreachable at any fixed stage". No fixed representation hosts generic intervention combs as the horizon grows | `papers/Main.md:596–598`, :574 (resources), :496, :556 |
| G-sub, G-fact | open | no source |
| I-qloc, kinematics | established (K): one quasilocal algebra contains the full matrix algebras of every finite region; the update is an isometric `*`-automorphism; the completion is unique given its stages and dynamics. No state or representation is selected at the level of the laws. A normalized tracial state, `referenceState`, exists | `papers/Main.md:588`; `QuasilocalAlgebra.lean:887`, :901, :904; `quasilocal-completion-audit.md:212`; ledger B-QM-9 |
| Carrier 3, operational | exact finite operational QM on every nonempty finite carrier is conditional[an added continuously tunable state-mixing operation, posited as an "empirical controllability resource"; the phases, "a stated intervention principle rather than a consequence of its finite states and bijective dynamics"; complex matrix kinematics taken as given]. The substratum does not supply the state-mixing operation. This is a statement about operational theories on finite carriers, not a property of I-qloc | `papers/Main.md:588`, :562; ledger B-QM-4, B-QM-5, M2 |
| I-qloc, I-deep, I-meas, exact equivalence | open. The completion "removes the finite-region cutoff for the algebra, the state space, and the OI-induced discrete dynamics rather than characterizing all infinite-dimensional quantum instruments"; the all-horizons fixed-representation question is open | `papers/Main.md:588`, :556; ledger M5, J-3, J-4 |

## 2. Per class: what stays, what needs replacement, assumptions, and the first missing step

### 2.1 F: one fixed finite carrier

- **Stays established, at its stated scope.** 1.1–1.4 in full, at recurrence-cycle scope. 1.5 as
  stated (conditional, with no instance in the counted setting). Every result of 1.6. These are
  preserved unchanged; together with 1.6 they cover the #1055 controls.
- **Needs replacement.** Nothing within the class.
- **Encoding, resources, access.**
  - Encoding: the product carrier `C_V × C_H` with `π` the projection and a root-shared prior
    (H-product), which a finite-valued `π : S → V` does not by itself supply (DEPENDENCY-AUDIT.md:290).
  - Resources: hidden capacity at least `2^{I*}` for conditional memory `I*`
    (`papers/Main.md:512`).
  - Access: the recurrence time `t_R` can exceed every accessible window. The observer's statistics
    are the rooted law restricted to accessible windows, on which the recurrence-cycle verdict is
    not witnessed (`papers/Main.md:139`).
- **One fixed model.** Yes. The class is excluded for exactness by `papers/Main.md:558`, conditional
  on the imported [55] (1.7), and by the target (#914 comment 6875046763).
- **First missing proof step.** None for 1.1–1.4 at their scope. For 1.5, the first missing step is
  a preparation or a non-aligned bipartition that the model supplies, under which a scrambling
  statement holds (`papers/GR.md:815`; ledger §8.4). With respect to the target, no proof step
  inside this class reaches exactness, because of the obstruction above.

### 2.2 G-fam: a family of finite models of growing size

- **Stays established.** Every F result, for each member separately, at that member's scope.
- **Needs replacement.** Any statement about the family as one object. The family is not one fixed
  model, and this inventory does not treat it as one (binding control). Gate A answer 3 requires
  one fixed model.
- **Encoding, resources, access.**
  - Encoding: each member has its own carrier. The side-`L` torus has `q^{2L^d}` pair
    configurations (`papers/SM.md:296`). The `R_n` have their own instrument nets, register
    precision `b` and branch registers (`papers/Main.md:574`, :596).
  - Resources: hidden capacity grows with the horizon, the dimension and the accuracy
    (`papers/Main.md:574`). With fixed-point registers this rests on the finite-`b` accuracy bound
    of clause (1), which is open (`papers/Main.md:574`, :596). The instrument net adds
    `O(m d^4 log(2K/ε))` visible bits per step (:596). The recurrence bound grows with `L`
    (`papers/SM.md:296`).
  - Access: each member is used at a bounded horizon.
  - Maps between members: only alphabet change, under the alphabet-size hypothesis
    (`papers/Substratum.md:255`), and only for observables expressed through transition
    probabilities.
- **One fixed model.** No.
- **First missing proof step.** A link that makes each member's rooted law the rooted law of one
  fixed model. Two forms are possible:
  - an injective, dynamics-compatible embedding of each member into the fixed model as an invariant
    sub-carrier (G-sub). Under a prior of full support such a sub-carrier has measure zero, so the
    member's law is the fixed model's law only for a preparation confined to it;
  - a projective system of factor maps that intertwine the dynamics and push the fixed model's
    prior forward to each member's prior (G-fact). Each member's rooted law is then a marginal of
    the fixed model's law under its own prior, with no measure-zero restriction.

  Neither is on `main` for the Z/q lattice update or for the three inventoried results. For the
  OBL class under `μ`, the G-fact form is excluded: there is no nontrivial finite dynamical factor
  (2.3; refuted within the OBL class, support off `main` (PR #1303)). The G-fact form has an RR instance for the free 1-D `p`-adic
  map (`continuous-substates/README.md:113–121`). The quasilocal directed system
  (`papers/Main.md:588`) supplies embeddings of finite regions as algebras. Its finite regions are
  not invariant under the update, so it is neither link for recurrence (2.3).

### 2.3 G-sub and G-fact: finite stages inside one fixed model

- **Stays established.** On a finite `φ`-invariant stage, every F result holds verbatim, provided the
  prior is supported on the stage (`papers/GR.md:587` for 1.3; A.8's own hypothesis for 1.5). On a
  finite factor, 1.2 and 1.3 hold for readouts that factor through it, under the stated conditions
  ([IR] transfer; RR instance only).
- **Needs replacement.** On a finite region that is not invariant, none of 1.1–1.5 applies. The
  region's visible law after `n` steps depends on the radius-`n` cone (`papers/GR.md:112–114`). The
  leading-order closure on `C_V × C_B` needs H-BD (posited; `papers/GR.md:122`). Under the linear
  update (ledger item (vii)), H-BD holds only if the deep sector does not enter the `V × B` update,
  and it fails for the update of `papers/Main.md` §3.2 at every cut where a boundary site has a deep
  neighbour (`papers/GR.md:128`).
- **Encoding, resources, access.**
  - Encoding: the stage is a sub-carrier or a factor of the fixed model.
  - Resources: as F for the stage or factor.
  - Access, for G-sub: the preparation must give the stage full measure. In an infinite model this
    determines the state on infinitely many sites. No native finite-access preparation of such
    global support has been sourced. Whether one is possible depends on interface and resource
    hypotheses that no source states, so finite access alone is not taken here as a no-go.
    Confinement to a finite invariant stage also makes the support of the prior finite. It is
    therefore a finiteness posit of A1's kind, placed on the support of the state rather than on
    `S`, and it does not weaken A1.
    - The owner's Q10 decision applies (§4): "A finite invariant sector defined by a global
      constraint is not automatically an accessible subsystem. Require a physical preparation and
      access argument before counting it toward the single-model target." D-CQ does not mention this
      decision. It concerns counting a sector toward the single-model target, a coverage question,
      and D-CQ leaves coverage required. Under D-CQ, C is defined "by the limits of embedded
      observation", so whether confinement to a sector is such a limit is part of S-J.
    - Sector-C membership and physical confinement grounds (S-J) belong to RO-1 (#1169 comment
      6883250792; §4, Q2). This inventory decides neither.
  - Access, for G-fact: the fixed model's own prior; the readout must factor through the finite
    factor.
- **One fixed model.** Yes.
- **First missing proof step.**
  - G-sub: no statement on `main` gives finite invariant stages for the Z/q lattice update on `Z^d`
    (§5). [IR] For a translation-invariant reversible finite-range update, the configurations
    periodic under the translations by `L e_j` form a finite set mapped onto itself by `φ` and
    `φ^{-1}`. With the operator convention of `papers/SM.md:296`, `A = α Σ_j (T_j + T_j^{-1})`, the
    restriction is the side-`L` torus model for every `L ≥ 1`. Under a simple-graph adjacency
    convention, such as the circulant of `papers/SM.md:1602`, the two differ at `L = 2`. This follows
    almost by construction and carries the access objection above, so this inventory does not
    recommend it (§3). In the OBL class these sets have `μ`-measure zero (OBL §4.1; established
    for that rule and measure, support off `main` (PR #1303)).
  - G-fact, OBL class: there is no nontrivial finite dynamical factor, refuted within the OBL class,
    support off `main` (PR #1303) (OBL 3.4). A finite factor `ψ : X → Y` with `ψ_* μ = ν` and a cell
    of `ν`-mass strictly between 0 and 1 would give `μ(E ∩ F^{-n} E) ∈ {0, ν(y)}` for every `n`,
    which cannot tend to `ν(y)^2`. The G-fact route is therefore excluded for this rule under `μ`.
  - G-fact, other rules and measures: a finite dynamical factor of the fixed model through which a
    finite-access readout factors. None is stated on `main`.

### 2.4 I-deep: an infinite deep sector beyond a finite causal cone

- **Stays established.** 1.6 in full. In particular, the visible transition data on `[0, nΔt]` are
  exactly independent of the deep sector, given the stated prior and dynamics
  (`papers/GR.md:132–134`).
- **Needs replacement.** 1.1–1.5 at recurrence scale. The source says recurrence-scale content lies
  outside this class and that the accessible-window property carried there is conditional memory
  (`papers/GR.md:138`).
- **Encoding, resources, access.**
  - Encoding: a normalized product prior on the deep sector; a locally finite coupling graph;
    updates that depend on finitely many components (`papers/GR.md:132`).
  - Access: finite, through the causal cone.
- **One fixed model.** Yes.
- **First missing proof step.** For a deep sector coupled to the boundary: either an exact common
  visible return (1.2) for the coupled model under that prior, or a replacement for recurrence. For a
  deep sector that no dynamics couples: the infinite form of `papers/Substratum.md:257–262`, with a
  normalized state and a well-defined evolution on the infinite factor (:262). [IR] That identity
  uses only `Tr σ_A = 1` and product dynamics, so its infinite form looks short, but no source
  states it.

### 2.5 I-qloc: the infinite-region completion

- **Stays established.** The completion's kinematics (1.7) and 1.6. A normalized tracial state
  exists: `referenceState` is the extension of the uniform family (`QuasilocalAlgebra.lean:901`),
  the uniform family is a state family (:887), and on each finite stage the state is the normalized
  trace (`referenceState_stage`, :904). The uniform family is "the only preparation the interface
  assumes" and the unique family on each region invariant under every local unitary
  (`RegionTower.lean`, header item (3)). Main:588's "no Hilbert-space representation and no
  superselection sector is selected at the level of the laws" is a statement about selection, not
  about existence.
- **Needs replacement.** 1.1–1.5. Rooted maps on the completion can be formed from the diagonal of
  `referenceState`. For the OBL class, (ii-a) below identifies that diagonal with `μ`, and 1.1–1.3
  are then recorded at the OBL class. No result on `main` uses these maps.
- **Encoding, resources, access.**
  - Encoding: finite regions as full matrix algebras, with complex matrix kinematics taken as given
    (#914 comment 6875046763, decision 4).
  - Resources: for operations, the added control operation and the phase intervention principle,
    both posited (1.7).
  - Access: finite regions.
- **One fixed model.** Yes, at the level of the algebra and the discrete dynamics.
- **Three statements, kept separate, for the OBL class.** The second-order rule is `ruleDynamics`
  (`SecondOrderDrive.lean:339`; `leap` is `(p, c) ↦ (c, F c − p)`), with `heisQ`
  (`QuasilocalAlgebra.lean:1264`), instance `ι = Z^d` and site set `(F_p)^2`.
  - (i) Haar invariance, `μ ∘ F^{-1} = μ`: established for that rule and measure, support off
    `main` (PR #1303) (OBL Step 2).
  - (ii-a) The bridge: on diagonal stage elements `referenceState` is integration against `μ`.
    Established for that rule and measure, support off `main` (PR #1303) (OBL §5). By
    `referenceState_stage` (:904) the stage value is `|Conf Λ|^{-1} tr X`. For `X = diag(f)` this is
    the uniform average of `f` over the configurations of `Λ`, which is `∫ f dμ` for the cylinder
    function `f`.
  - (ii-b) Invariance of `referenceState` under `heisQ (ruleDynamics)` on diagonal elements.
    Established for that rule and measure, support off `main` (PR #1303), as a paper calculation
    from the definitions on `main`; not kernel-checked (OBL §5). The calculation, with the two
    textual corrections asked for by ChatGPT review 5906973051 and by findings F16 and F17 of the
    review of r4 (written here as text; no computation; `OBL-RO3-2-r2.md` is not edited):
    1. `emb Λ (diag g)` sends `δ_s` to `g(glob Λ s) δ_{patch Λ s (glob Λ s)}`
       (`QuasilocalAlgebra.lean:242–245`), and `patch Λ s (glob Λ s) = s` is the kernel theorem
       `patch_glob` (:136). So `emb Λ (diag g)` is the multiplication operator `D_{g ∘ res_Λ}`.
    2. `heis Φ T = permOpInv Φ * T * permOp Φ` (:999). `permOp` is `mapDomain` along `φ` (:966),
       and `permOpInv_apply` (:981) gives `(permOpInv h)(t) = h(φ t)`. Hence
       `heis Φ D_f = D_{f ∘ φ}`.
    3. The stage matrix. `heis_emb` (:1127) gives
       `heis Φ (emb Λ X) = emb (hat Φ Λ) (transported Φ Λ X)`. For `X = diag g`, the sum defining
       `transported` (:1109) at column `h ∈ Conf (hat Φ Λ)` is nonzero only at
       `f₀ = glob Λ (φ (ext (hat Φ Λ) h))`. By the definition of `target` (:1054), `patch_glob` and
       `glob_ext` (:1071), `target Φ Λ (ext (hat Φ Λ) h) f₀ = glob (hat Φ Λ) (ext (hat Φ Λ) h) = h`.
       Hence `transported Φ Λ (diag g) = diag (h ↦ g (glob Λ (φ (ext (hat Φ Λ) h))))` on
       `Conf (hat Φ Λ)`. The value does not depend on the choice of extension, by
       `glob_map_of_glob_eq` (:1074). `emb_injective` (:353, `[Nonempty Q]`) or `kern_patch` (:178)
       gives the same identification at the operator level.
    4. By `heisQ_stage` (:1274) and `referenceState_stage` (:904),
       `referenceState (heisQ (stage Λ (diag g)))` is the uniform average of that diagonal over
       `Conf (hat Φ Λ)`. The function `g ∘ res_Λ ∘ F` depends only on the sites of `hat Φ Λ`, so
       the average is `∫ g ∘ res_Λ ∘ F dμ`, which equals `∫ g ∘ res_Λ dμ` by (i). This takes
       `φ = F`, which holds for `ruleDynamics` with the linear neighbourhood function.
  - (ii-c) Invariance of `referenceState` under `heisQ` on the whole quasilocal algebra,
    off-diagonal elements included: open. Not stated on `main`; (i) does not give it. Candidate
    routes, unverified: stagewise trace preservation of `transported`; uniqueness of the tracial
    state on the completion.
  - (iii) Realization at the physical observer interface: that physical preparations realize `μ`,
    that a physical readout is such a `π` with the product structure, and that the physical
    dynamics is this rule. Open. The rule is posit (vii) (`papers/Main.md:724`). The uniform family
    is the interface's assumed preparation in the kernel (`RegionTower.lean`, header item (3)), not
    a sourced physical one. Physical source remains NOT PASSED.
- **First missing proof step.** For the OBL class: (ii-c), and separately (iii). The rooted laws of
  1.1–1.3 are diagonal and need only (ii-a) and (ii-b); any statement about the full state needs
  (ii-c). For other reversible finite-range updates: invariance of `referenceState` under `heisQ`,
  which no source states, with the same three statements kept apart. [IR] One route to (ii) in
  general: `referenceState ∘ heisQ` is again a tracial state, and the completion of full matrix
  algebras over finite regions is expected to carry a unique tracial state. This route is not
  checked here.

### 2.6 I-meas: general infinite probability-preserving carriers, and continuous time

- **Stays established.** 1.6; the matrix-level P-indivisibility theorems as matrix statements
  (1.3). The set identity `changeEvent_eq_iUnion` and the measured-return equivalence are K for
  their statements (`ObservableFactorRecurrence.lean:48`; `ObservableMeasureReturn.lean:63`, :83;
  kernel-only).
- **Needs replacement.**
  - 1.1 as an unconditional property: not inherited. In the OBL class it is refuted (1.1; support
    off `main`, PR #1303).
  - 1.2 as an unconditional property: not inherited. Main records the failure of near-total common
    visible return at late times for mixing Hamiltonian flows (`papers/Main.md:155`). In the OBL
    class exact common visible return is refuted (1.2; support off `main`, PR #1303).
  - 1.3: conditional on 1.2's return hypothesis. In the OBL class the recurrence route is
    unavailable (1.3; support off `main`, PR #1303).
  - 1.4: the necessity half.
  - 1.5: the whole cycle-average argument.
- **Encoding, resources, access.**
  - Encoding: a normalized invariant measure; a measurable bijection; a measurable finite-valued
    observation with positive-measure cells. The rooted convention must be fixed explicitly (1.2).
  - Resources: none stated.
  - Access: finite.
- **One fixed model.** Yes.
- **First missing proof step.**
  - For the actual OI update (not a free or illustrative map), with a stated normalized invariant
    measure: whether some finite-access readout satisfies `π ∘ T^L = π` almost everywhere. Only the
    free 1-D map is examined, in RR; "Whether an **interacting** map retains any such observable is
    open" (`continuous-substates/README.md:143–144`). For the OBL class and `μ` the answer is
    negative (1.2; support off `main`, PR #1303). Other invariant measures on `X`, composite `q`,
    nonlinear rules and the gauge-coupled rule are untouched (OBL 3.5).
  - Separately, the formal composition from a measurable dynamics to a real row-stochastic rooted
    family (`ObservableFactorRecurrence.lean:20–22`).
  - For 1.5: the ensemble restatement of A.8 (`papers/GR.md:827`).

### 2.7 I-nonorm

No rooted law, no P-indivisibility statement and no cycle average is defined. Poincaré recurrence is
not available without a finite invariant measure or conservativity: conservative infinite-measure
systems also recur. The #1055 body's test-case wording, "Poincaré recurrence needs a finite
invariant measure and fails without one", states a sufficient condition as a necessary one (§4,
Q9). The class is outside every inventoried result.

## 3. OBL-RO3-2 outcome, and candidates for the next unit (none chosen)

**OBL-RO3-2 is accepted at its stated scope.** For the OBL class (§0), the posited linear rule is
mixing under its uniform Haar measure (OBL Step 8). The owner accepted the direct proofs (#914
comment 6883931412, item 2; #1055 comment 6883932722). Every consequence below is labelled
"established for that rule and measure, support off `main` (PR #1303)", or "refuted within the OBL
class, support off `main` (PR #1303)".

- **The first branch of r4's proposed decision rule has fired.** r4 §3 item 3 read: "If (a)–(d) are
  proved: record that under the uniform Haar measure on the fixed infinite-lattice model, the
  recurrence route to 1.3 is unavailable for the linear rule. ... Record also that G-fact has no
  nontrivial finite factor for this rule". r5 records both (1.3, 2.3).
- **How (c) is proved.** Not through the Halmos criterion or Rokhlin's theorem. OBL Step 4 proves the
  two implications it needs directly from the standard facts S1–S3, and gives mixing without
  ergodicity as an intermediate (OBL lines 145–158, 205–207).
- **The primary-source check.** It was not completed: neither text was reached. The owner accepted
  the direct proofs in its place (#1055 comment 6883932722). The attribution of the two criteria to
  Halmos and Rokhlin stays unverified from primary sources, and no step depends on it.
- **Cells moved, at the OBL class only.** 1.1, 1.2 and 1.3 for I-qloc and I-meas; 2.3 G-fact; the
  first missing step of 2.5; §4 Q6. No other cell moves.
- **Preservation controls (r4 §3 item 4) hold.** Each holds at OBL §4, established for that rule and
  measure, support off `main` (PR #1303):
  - the finite tori sit in `X` as `μ`-null sets and keep their periods;
  - SM:294 and SM:296 are reconciled: a different carrier, a different invariant measure, and
    conserved sums that are not functions on `X`;
  - the `p`-adic, finite-dimensional torus, finite-torus and `α = 0` countercontrols each fail at a
    named step.
- **What stays open.**
  - P-indivisibility itself on the OBL class.
  - Near-total common return at bounded times.
  - (ii-c) and (iii) of 2.5.
  - Every other rule and measure, and composite `q`.
  - EXACT.

**r1's OBL-RO3-1 stays withdrawn.** It proposed proving that the spatially periodic configurations
of the lattice model form finite invariant sectors. That follows almost by construction (2.3); it
places the finite model on a global constraint; confinement to it is a finiteness posit of A1's
kind; and it is not the missing link of G-fam (2.2). In the OBL class these sectors are `μ`-null
(2.3).

**Candidates for the next #1055 unit. None is chosen.** The independent review of r5 has reported.
Choosing a target is the owner's decision; this record chooses none (#1169 comment 6893687398). The
candidates on record:
- Bijectivity without A1 on a normalized measure space (§7, AM-3). The review of r5 (§7) recommends
  it first; see below.
- The infinite form of Theorem 24(iii) for a decoupled normalized factor (2.4). The review of r4 (§6)
  states it with preregistered controls, countercontrols and a decision rule; the review of r5
  places it second.
- (ii-c) for the OBL class (2.5).
- The kernel composition from measurable dynamics to a real row-stochastic rooted family (2.6),
  which needs Lean.
- The ensemble restatement of A.8 (2.6).
- [IR] The Bernoulli-shift realization (1.4).
- Recurrence-scale P-indivisibility on a coupled infinite sector by a route that does not use
  recurrence. On the OBL class it is open, and no bounded mechanism is in view (OBL 3.3).

**The review of r5's recommended first target: AM-3, recorded as a recommendation only.** It is
stated here as the review states it, so that the owner can decide. It adopts no premise.

- **Why the review places it first.** The law-level equivalence does not use A1 (Main:60, :354;
  DEPENDENCY-AUDIT.md:282). A1 enters the physical reading of the characterization theorem (Main:60;
  AM-20) and recurrence-scale nontriviality (Main:354: P-indivisibility's "role is confined to
  nontriviality at the recurrence scale"). Every infinite class of §0 already takes bijectivity as a
  hypothesis. So the most upstream A1 use behind the owner's sentence in #1169 comment 6893456888 is
  the bijectivity argument (AM-3).
- **Two questions, preregistered separately.**
  - **Q-A, surjectivity.** Setting: `(X, μ)` a standard Borel probability space; `φ` an injective
    Borel map with `μ ∘ φ^{-1} = μ`. Claim: `X∞ := ⋂_{n≥0} φ^n(X)` is Borel, `μ(X∞) = 1` and
    `φ(X∞) = X∞`, so `φ` restricted to `X∞` is a Borel bijection preserving `μ`. This is the measure
    analogue of Main:60's eventual image `E`.
  - **Q-B, the hidden-sector injectivity prong.** Without A1, does any restriction argument remove a
    merge that leaves no statistical trace? The review's candidate for a negative is the doubling
    map (AM-3).
- **First missing step.**
  - For Q-A: a paper proof, with every hypothesis labelled, that the images `φ^n(X)` are Borel and
    of full measure and that `φ` maps their intersection onto itself. The review's outline: Borel
    images by the Lusin–Souslin theorem, an external standard input to be cited at source;
    `μ(φ^n X) = μ(φ^{-1} φ^n X) ≥ μ(φ^{n−1} X) = 1`; and `φ(⋂ A_n) = ⋂ φ(A_n)` by injectivity. No
    source on `main` states it.
  - For Q-B: a stated class in I-meas, and either an argument that a full-measure restriction
    removes every untraceable merge in it, or an explicit map for which none does.
- **Skepticism, stated in advance (the review's).** Q-A is textbook measure theory. The invariant
  probability is a replacement premise; Lemma 3's selection stays tied to A1 (AM-4), and Sub:262
  already demands such a measure for any infinite extension. Whatever the outcome, it is not to be
  presented as removing the posit. It has no Layer-0 standing under AGENTS.md §A.29 and moves no
  correctness.
- **Controls, fixed in advance.**
  - With `X` finite and counting measure, `X∞ = E`, reproducing Main:60 and `injective_imp_bijective`.
  - Main:60's three-state example, in which the counting measure on `E` is not doubly stochastic,
    is reproduced, so its measure-correspondence caveat stands.
  - Every F cell, `S ⟺ D ⟺ Q_fb`, the readback lemma and Theorem 24(iii) are unchanged.
  - In the OBL class `F` is already bijective, so `X∞ = X`.
- **Countercontrols, each of which must fail at a named step.**
  - `n ↦ n+1` on `N`: no invariant probability, and `X∞ = ∅`; fails at normalization.
  - The doubling map and the one-sided Bernoulli shift: fail at the injectivity hypothesis.
  - A non-Borel injection, or a non-standard space: fails at the Lusin–Souslin step.
- **What counts as what.**
  - **Recovery (Q-A):** a complete paper proof under the controls above. AM-3's surjectivity and
    eventual-image steps would then be recorded as conditional[standard Borel space; invariant
    probability; injectivity].
  - **Negative (Q-B):** an explicit `μ`-preserving map in I-meas with no injective restriction to a
    set of full measure, with its consequence for the visible statistics stated. A1 would then be
    recorded as carrying the hidden-sector injectivity prong, not only surjectivity.
  - **Anything else:** open, with the remaining gap stated. No outcome is expected in advance.
- **Second, per the review:** the infinite form of Theorem 24(iii). **Not first:** the §3.2 route on
  I-qloc, which needs (ii-c); recurrence-scale P-indivisibility on a coupled infinite sector.

## 4. Open owner questions

1. **Admissible completions.** Which of G-sub, G-fact, I-deep, I-qloc and I-meas may serve as
   EXACT's carrier class, or are all to be carried forward? The choice may not be made because a
   completion reproduces quantum predictions.
2. **Sector confinement: assigned to RO-1.** The RO-1 split (#1169 comment 6883250792, `amaybaum`,
   2026-11-14T19:48:20Z), quoted verbatim: "RO-1 owns sector-C membership, physical confinement
   grounds (S-J), closure under permitted operations and compositions (S-A), and non-circularity."
   Whether confinement of preparations to a finite invariant sector is an admissible assumption,
   given that it is a support-level finiteness posit (2.3), is therefore a question for RO-1 and
   S-J. This inventory records only the posit's kind (2.3). The RO-1 and #1143 matters are not
   decided here.
3. **Which property must transfer.** On completions, must recurrence-scale P-indivisibility be a
   preserved control, which would need a replacement proof under a stated return hypothesis? Or may
   it remain scoped to finite representatives, with the readback lemma's accessible-window memory as
   the property carried to completions (`papers/Main.md:139`; `papers/GR.md:138`)? On the OBL class
   the return hypothesis fails (1.2; refuted within the OBL class, support off `main` (PR #1303)), so
   a replacement proof there would need another mechanism.
4. **Accessibility.** For growing carriers the recurrence time grows (`papers/SM.md:296`). Is a
   recurrence-scale property required at all for EXACT, which concerns operational law-equality on
   performable experiments?
5. **A.8 and A.9.** Must the cycle-averaged Page curve be restated on a completion (the ensemble form
   of `papers/GR.md:827`), or does J-4 stay recorded as a finite-carrier statement? A.8 already has
   no instance in its counted setting.
6. **The prior on a completion.** Lemma 3's maximal-entropy selection is finite
   (`CanonicalMeasure.lean:54`, `[Fintype S]`; §7, AM-4). On the OBL class, the uniform product
   measure `μ` is invariant, the diagonal of `referenceState` is `μ`, and `referenceState` is
   invariant on diagonal elements (2.5 (i), (ii-a), (ii-b); established for that rule and measure,
   support off `main`, PR #1303). Invariance off the diagonal, (ii-c), is open. The Q11 decision
   stands: `referenceState` is examined as a candidate, not adopted and not assumed invariant. Which
   normalized measure or state is the completion's prior, and by what criterion other than quantum
   reproduction?
7. **Review of the RR items.** Should the SUBSTATE-1 paper proofs receive independent review? They
   are `observable-recurrence.md`, `infinite-xor-counterexample.md`, `solenoid-countercontrol.md`,
   and the finite-subgroup and `p`-adic findings of `README.md:105–137`. If validated, they would
   change:
   - the I-meas cells of 1.3 and 1.4, from open to "refuted within" a stated class for
     unconditional transfer;
   - the G-sub and G-fact cells, from RR context to source.
8. **Which carrier "arbitrarily large" quantifies.** Is "arbitrarily large finite quantum carriers"
   read at the operational-carrier level only (carrier 3), leaving the size of carrier 1 free, or
   must each quantum carrier of dimension `d` be encoded in a finite invariant sub-carrier or finite
   factor of the substratum?
9. **The consumers of A1.** Main:724 names two consumers ("consumed here by the recurrence step of
   §2.3 and by §4.6") and leaves "the remaining uses of the posit" to the status Remark of §1.2,
   which lists more (Main:60). The #1055 body's "Main names exactly two consumers of A1" is
   therefore narrower than the source, and its §4.6 citation "Main:760" is Main:758 at this base.
   The body's test-case sentence on Poincaré recurrence is the one corrected in 2.7. §7 maps every
   consumer listed at Main:60 and the others found. Is #1055's list of consumers to be read as §7's
   map, and is §4.6 (AM-8) to be covered by a later unit?

Q10–Q12 are decided (#914 comment 6883249235, `amaybaum`, 2026-11-14T19:48:13Z). Each decision is
quoted verbatim after its question. The owner adds: "These decisions do not select a completion or
establish EXACT."

10. **Sectors as subsystems.** Does a sector, a restriction of the state's support that needs a
    preparation over infinitely many sites, count as a "subsystem" under Gate A answer 3, and as an
    accessible preparation under answer 4 (#1169 comment 6876591512)? Answer 4's soundness
    requirement is amended by D-CQ (Standing); the decision below is unchanged by it.
    **Adopted:** "A finite invariant sector defined by a global constraint is not automatically an
    accessible subsystem. Require a physical preparation and access argument before counting it
    toward the single-model target."
11. **The interface's canonical state.** Is the kernel's tracial reference state, the interface's own
    canonical preparation (`RegionTower.lean`, header item (3)), to be examined as the completion's
    prior, without selecting it for quantum reproduction? This sharpens Q6.
    **Adopted:** "Examine the kernel's `referenceState` as a candidate prior for the completion. Do
    not adopt it as the uniquely physical prior or assume its dynamical invariance."
12. **#1055 test case D2.** Can a fixed finite `S` accommodate a growing horizon? Main addresses it in
    part. A fixed finite realization with a fixed prior has an exactly periodic multi-time law, so a
    nonperiodic target has no exact all-time realization by one fixed finite substratum
    (`papers/Main.md:638`). No fixed representation hosts generic intervention combs as the horizon
    grows (`papers/Main.md:496`, :556).
    **Adopted:** "Keep the growing-horizon D2 question as a separately accountable follow-up under
    #1055, coordinating with #1029 for any later manuscript correction." The decision also records
    that RO-3 has not settled the question.

13. **D-CQ and answer 4.** D-CQ (#1169 comment 6891338304) amends "the soundness requirement in the
    Gate A answers" without numbering them. Answer 4's last sentence reads, verbatim: "Access closure
    must prevent a model from qualifying through selected quantum experiments while also permitting
    stronger-than-quantum experiments." This inventory reads D-CQ as amending answer 2's soundness
    half, answer 4's first sentence and the exclusion purpose of answer 4's last sentence (Standing,
    [IR]). Is that the owner's reading? And does the anti-selection part of the last sentence, that a
    model may not qualify through selected quantum experiments, survive as a coverage and
    agreement-with-data condition (#914 comment 6893722503 §4 states this as a proposal)?

## 5. Searches behind the negative statements

- **No recurrence or period statement for the quasilocal completion.**
  - Searched `recurr`, `period`, `orderOf` and `finite order` in `QuasilocalAlgebra.lean`,
    `QuasilocalCharacterization.lean`, `RegionLimit.lean` and `SecondOrderDrive.lean`.
  - Searched `recurren` in `verification/audits/operational/quasilocal-completion-audit.md` and
    `verification/audits/physical-realization/continuous-time-audit.md`.
  - No hits. The OBL class statements of 1.1 come from `OBL-RO3-2-r2.md`, off `main`.
- **No invariance statement for `referenceState` on `main`.** Read `QuasilocalAlgebra.lean:880–910`,
  the `heisQ` definitions (:1264–1280) and the header of `RegionTower.lean`. The kernel establishes
  that the state exists, its stage values, and the invariance of the uniform family under local
  unitaries at finite stages. Invariance under the update is not stated there. The diagonal
  invariance of 2.5 (ii-b) is a paper calculation off `main`.
- **No finite invariant stage or finite factor for the Z/q lattice update on `Z^d` on `main`.**
  - r1 searched `papers/`, `book/` and `verification/` for "periodic configurations",
    "translation-periodic", "invariant sector", "finite invariant subset", "invariant
    representative", "periodic boundary" and "torus". r2 added "invariant subgroup" and "factor".
  - Hits on `main`:
    - `papers/GR.md:587` (a constraint surface);
    - the finite subgroups `(Z/N)^{2L}` of the free 1-D torus map and the `p`-adic factors
      `Z_p → Z/p^k` (`continuous-substates/README.md:105–137`, RR).
  - Neither RR hit concerns the Z/q lattice update on `Z^d`. The torus appears in the papers as the
    finite model itself (`papers/SM.md:294–296`), not as a sector of an infinite one.
- **No A.8 counterpart on a completion.** `papers/GR.md:797–861` and ledger §8, §9.
- **The A1-dependency map (§7).** At `7ac74a4b`, searched `papers/*.md` and `book/*.md` for
  "total-finiteness", "total finiteness", "A1", "(A1)", "finite deep", "deep sector",
  "injectivity implies surjectivity", "eventual image", "counting measure", "corner" and "Doukas";
  `verification/lean-mathlib/OIBridge/` for `Fintype S`, `injective_imp_bijective`,
  `causal cone`, `DependsOnlyOn` and the §3.2 lemma names; the census for the families that hold
  them; and `verification/audits/manuscript/observer-relative-finiteness-20261030/DEPENDENCY-AUDIT.md`
  for its proof-dependency matrix. Main:60's list of uses was taken as the starting set.
  - **Correction.** r5 said that each hit was read in context. That was not so. r5's search for
    "A1" used the string with a trailing space, which misses "A1)" and "A1,". Computation:100
    ("violating A1)") was missed that way, and the other items the review of r5 lists were missed
    by the phrase list.
  - r6 adds the review's phrases, run as whole-word searches over `papers/*.md` and `book/*.md` at
    `7ac74a4b`: `\bA1\b`, "finiteness posit", "finite total", "finite representative" and
    "recurrence time". It also reads the review's census entries 15, 31, 49 and 53 and the lines the
    review cites. The hits in `papers/Main.md`, `GR.md`, `Methodology.md` and `Computation.md` were
    read in context. Hits in `papers/Structure.md` (39) and `papers/Substratum.md` (15) were
    classified by the passages §7 cites and §7.2 lists. Book hits are classified as mirrors or
    framing in AM-17. The map is bounded by these searches.
- **D-CQ.** A search for the string "D-CQ" in the comments of #914, #945, #1007, #1055, #1143,
  #1147, #1169, #1221, #1294 and #1303, and in other bodies, reviews and branch heads, found only
  #1169 comment 6893687398. That search could not find the decision, which does not carry the
  label. The decision is #1169 comment 6891338304, read first-hand. Its label is assigned in #914
  comment 6893722503 §3.
- These searches are bounded by the phrases listed. A paraphrase outside them could have been
  missed. r1's list missed the RR hits above.

## 6. Off-`main` references (AGENTS.md §A.42 item 8)

This inventory is not a record landing on `main`. The trace is given so that a later landing can
check it.

| Reference | Use here | Classification |
|---|---|---|
| `OBL-RO3-2-r2.md`, PR #1303, commit `ef8d353e`, blob `b1edb95f`, unchanged at head `78089e5e` | the proofs behind every cell labelled "support off `main` (PR #1303)": 1.1, 1.2, 1.3 for I-qloc and I-meas; 1.2 G-fact; 2.2; 2.3 G-sub and G-fact; 2.5 (i), (ii-a), (ii-b); 2.6; §3, including the preservation controls; §4 Q3 and Q6; the null-measure statements of §0 and 2.3; §7 rows AM-1, AM-2, AM-4, AM-8, AM-16 and AM-20 | **support off `main`: a gap.** The cells are labelled accordingly and are not recorded as established on `main`. The gap is narrowed to the moved cells; it is shut only by landing `OBL-RO3-2-r2.md` on `main` no later than any record that relies on it |
| `REVIEW-OBL-r2.md`, `REVIEW-OBL-r2-ADDENDUM.md` (PR #1303); ChatGPT review 5906973051 at `78089e5e` | the review standing of OBL-RO3-2 r2; nits n1–n4; the two textual corrections applied in 2.5 | review records; support no claim |
| `REVIEW-r4.md` (the independent review of r4) | findings F1–F17 | review record; supports no claim |
| #914 comment 6883931412 item 2; #1055 comment 6883932722 | owner acceptance of the OBL-RO3-2 direct proofs | governance; supports no scientific claim |
| #1169 comment 6893687398 | authorization of r5 | governance |
| #1169 comment 6891338304 (D-CQ); #914 comment 6893722503 §3–§4 | the C/Q target decision and its amendment of the soundness requirement; the label D-CQ and the access-closure proposal | governance; supports no scientific claim |
| #1169 comment 6893456888 | the correction on total finiteness | governance; its reading of the equivalence is a finding (§7.3) |
| `REVIEW-1303-INVENTORY-r5.md` (the independent review of r5) | H1–H6′; the [IR] countercontrols of AM-3 and AM-7; the recommended recovery target in §3 | review record; supports no claim |
| `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md` | AM-26 | on `main`; a research-only record, context only |
| #1169 comment 6883250792 | the RO-1 split (Q2) | governance |
| #1169 comment 6891337868; #914 comment 6880700869 | retention of ledger r9 on `main`; acceptance of r8 | governance |
| Ledger r8 and r9 on `main` (Standing) | cross-references to B-QM-1, B-QM-4, B-QM-5, B-QM-8, B-QM-9, B-QM-27, B-BH-3, J-3, J-4, M2, M5, §8.4, §8.5; the attributed reading of §8.5 | **on `main`.** The identifiers are provenance. The attributed §8.5 reading is support on `main` for the statement that the ledger makes that reading, together with `papers/GR.md:813`, :823. Every status above is traced to a source |
| `records/unified-ledger-914-20261114` at `9ff3b8d9` | r4's reading copy of r8 | provenance; the same blob is on `main` |
| #1055 comments 6881390849, 6880024537; #1055 body | authorization, scope, controls, test cases; the consumer list and the Poincaré wording discussed in Q9 and 2.7 | governance; supports no scientific claim |
| #1169 comments 6880022363, 6877981234, 6876591512; #914 comment 6875046763 | target and EXACT's wording; Gate A answers 3 and 4 | governance; supports no scientific claim |
| #914 comment 6883249235; PR #1303 review 5906337933 | the owner's Q10–Q12 decisions and the r3 authorization; the r2 review's nits N1–N3 | governance and review record; support no scientific claim |
| #1007 body; #872 body | carrier foundations; completion sub-obligation | context; supports no scientific claim |
| `REVIEW-r1.md` at `0d6d8812`; `REVIEW-OBL-r1.md` at `76ca4c3d` | findings; the [IR] readings | review records; support no claim |
| Heads of PRs #1221, #1289, #1294; `e4ffa3b5` | searched for the string "D-CQ" only | provenance |
| #1009 and its branch | not used | — |

## 7. A1-dependency map (bounded by the searches of §5)

### 7.1 What the map is

Main:60 lists the uses of the finite representative: "The finite representative is used by the
recurrence step of §2.3 and the results resting on it (recurrence-scale P-indivisibility, the
CP-indivisibility theorem of §3.2, the all-time periodicity of a fixed realization in §3.4), by the
eventual-image and surjectivity steps of the bijectivity argument below, by the counting measure of
Lemma 3 and the uniform hidden prior that defines the baseline transition matrices, by the finite
hidden space of the §3.2 setup, by the corner-occupancy claim of §3.1, by the coupling-graph causal
cone of §3.3, and by §4.6; the obstructions stated in §3.4 for a fixed finite realization bear on
nature through it." Rows AM-1 to AM-10 take that list in order. AM-11 to AM-19 are the companion
papers, the book, the Lean modules and the verification records. AM-20 to AM-26 were added after the
review of r5: the characterization theorem, the C2-necessity theorems, GR:58, Comp:100,
Methodology's constructive-OSR claim, two kernel-only census entries and one record. §7.2 lists the
results checked and found not to consume A1. The map is bounded by the searches of §5; it is not a
complete corpus closure.

For each row: **where A1 enters** names the step; **what survives** states what holds without A1,
with its support; **status** is at proved scope. "Without A1: open" means that no source on `main`
states the result without A1 and none refutes it.

| Row | Result and source | Where A1 enters | What survives without A1 | Status at proved scope |
|---|---|---|---|---|
| AM-1 | Recurrence step of §2.3 and the results resting on it: Main:111, :121, :129, :135–143, :716; GR:90, :138, :585, :587; Sub:52, :92; `book/ch01-observation.md:95–109`, :119 (FULL:454); `book/appendix-b-derivations.md:413` | Step 1, "φ bijective on a finite set ⇒ ∃N: φ^N = id" (Main:121); the finite order `L` of a permutation of a finite set (Main:137); `C_H` finite "under the total-finiteness posit" (Main:111, :129). GR:90 restates the result "on a finite representative" | the matrix-level theorems with identity return as a hypothesis (1.3); the readback lemma and its accessible-window memory (1.6) | per class in 1.1–1.4. F: established at recurrence-cycle scope. OBL class: the route unavailable, established for that rule and measure, support off `main` (PR #1303). Elsewhere open |
| AM-2 | CP-indivisibility theorem, framework scope (Main:330–332); book `appendix-b-derivations.md:92` (Theorem B.2.5) | (a) the family `Φ_t` is defined on the §3.2 setup (AM-5); (b) its premise is §2.3's recurrence-scale P-indivisibility (AM-1). The implication "P-indivisible population process ⇒ CP-indivisible family" uses diagonal preservation (Main:326) and the stochasticity of the induced matrix `M` (Main:332), not A1 | [IR] the implication carries to any carrier on which the family and diagonal preservation are defined. No source defines the family beyond finite `V × H` | F: established (P; diagonal preservation K, `isDiag_Phi`, `EquivalenceChain.lean:253`, finite `V` and `H`, census 1, current) at recurrence-cycle scope. G-fam: per member. G-sub, G-fact: conditional as 1.3, with the family defined on the stage or factor [IR]. I-deep, I-qloc, I-meas: open. OBL class: the recurrence premise is unavailable (support off `main`, PR #1303), and CP-indivisibility is open. I-nonorm: no statement |
| AM-3 | Eventual-image and surjectivity steps of the bijectivity argument, and its hidden-sector injectivity prong: Main:60 ("On a finite set, injectivity implies surjectivity, so φ is a bijection"; the eventual image "defined here for a finite system only ... no construction is given for an infinite S"); Main:54; Main:724 (iii); Meth:156, :158, :166, :253, :261; `book/ch01-observation.md:41` (FULL:376) | surjectivity from injectivity on a finite set; restriction to the eventual image `E = ⋂ f^n(X)` of a map on a finite set. K: `injective_imp_bijective` (`CanonicalMeasure.lean:63`, under `[Fintype S]` at :54; census 1, current). The injectivity argument has two prongs (Main:60). The hidden-sector prong uses double stochasticity under the uniform prior on a finite product carrier, or the eventual-image restriction; both are finite constructions | the record prong: injectivity on states with distinct registered records. The hidden-sector prong is unsupported without A1. [IR], from the review of r5, checked on paper by the writer: the doubling map on the circle with Lebesgue measure preserves the measure, is onto and is 2-to-1 everywhere; its eventual image is the whole circle, so no restriction removes the merge. Its infinite substitute, the natural extension, is a factor relation, not a restriction, and Main:60 keeps restriction and factor apart. Surjectivity does not follow either: `n ↦ n+1` on `N` is injective and not onto. Main:724 (iii) allows adopting reversibility as the standard information-conservation postulate instead; that substitutes a premise and recovers nothing. Every infinite class of §0 takes a bijection as part of its definition (§0) | established (P; K) on finite `S`. Without A1: surjectivity and the hidden-sector injectivity prong are both unsupported; bijectivity is not derived; open. The review of r5 recommends this row as the first recovery target (§3, Q-A and Q-B), a recommendation only |
| AM-4 | Lemma 3's counting measure and the uniform hidden prior that defines the baseline matrices: Main:54, :58, :113–117 (`T_ij` with denominator `|C_H|`), :129, :60; K: `orbit_invariant_unique` (`CanonicalMeasure.lean:178`), `counting_maximal_entropy` (:227), under `[Fintype S]` (:54), census 1, current; DEPENDENCY-AUDIT.md:291; `book/ch01-observation.md:38`; downstream: SM:252, :334, :641 | the counting measure is a probability only on a finite set; the uniform prior `1/|C_H|` needs `C_H` finite | a normalized invariant measure must be specified separately (Sub:52, :92, :262). The audit row (:291) and its control 6 (`S = Z` with the shift: no normalized invariant probability) record the same; the audit is a record whose review independence is not established (:17–19). In the OBL class the uniform product measure `μ` is invariant (support off `main`, PR #1303); Lemma 3's maximal-entropy principle does not select it | established (P; K) on finite `S`. Without A1: the selection principle has no stated counterpart; open (Q6). SM:252 admits "a stated structured prior"; SM:334 and SM:641 take the counting measure; not traced further |
| AM-5 | The §3.2 setup's finite hidden space and the results on it: setup (Main:264–266); permutation unitarity (Main:268–270; K `permMatrix_mem_unitaryGroup`, `EquivalenceChain.lean:179`, `[Fintype V]`, `[Fintype H]`); the channel with `ρ_H = I_m/m` (Main:280–284); the Born-form representation theorem (Main:286–288, P; no kernel pointer at :288); diagonal preservation (Main:326–328; K `isDiag_Phi`, :253); CP-indivisibility (AM-2); the C2-necessity theorems built on this construction (AM-21) | `C_H = {h_1, …, h_m}` "under the total-finiteness posit" (Main:266); `H_H = C^m`; `ρ_H = I_m/m` | Main:716's "two routes" to the transition-statistics layer are §3.1, the Barandes route, and §3.2, the Stinespring route (Main:352: "The two routes agree on the configuration-transition probabilities"; Main:356: "Both routes above are constructive"). The §3.1 route needs finite `C_V` and (T) (Main:208, :354), not a finite `C_H`. The in-house fixed-basis representation, by the permutation unitary of any realization, exists for every finite-horizon law (Main:354), and the §3.4 equivalence constructs its finite hidden space (Main:60). So a route to the transition statistics that does not use A1 exists, on Main:354 and :60. On I-qloc: one quasilocal algebra, `heisQ` a `*`-automorphism, a tracial `referenceState` (K; 1.7). [IR] `I_m/m` has no counterpart as a normalized density operator on an infinite-dimensional Hilbert space; the counterpart of the channel would be the stagewise restriction of `referenceState` composed with `heisQ`, which no source states | established (P; K for unitarity and diagonal preservation) on the finite setup; as a statement about the substratum, conditional[A1]. Without A1: open |
| AM-6 | Corner-occupancy claim of §3.1 (Main:216) | "a finite deterministic substratum observed by marginalization cannot generate first-order leakage ... the framework occupies the corner Doukas identifies ... conditional on the total-finiteness posit" | no statement without A1. The source reads the contrapositive as a prediction: "fundamental dynamics of continuous-time Markov type would require an actually infinite hidden sector" | conditional[A1], with the correspondence's compressed-representation clause resting on an external result (Main:216); the source calls it "explanatory unification rather than corroboration". Without A1: open. No book mirror found (no hit for "Doukas" in `book/`) |
| AM-7 | Coupling-graph causal cone of §3.3 (Main:362) and the Bell results built on it: Bell ceiling for a screened local completion (Main:364–383), its corollary (Main:414), Main:650 (ii), Main:770 | `S = ∏_{i∈V} S_i` "with V and each S_i finite"; "Finiteness of V is used in the first step, where insensitivity to each single component outside the dependency set makes the i-th output a function of the components in it". The Bell ceiling's proof sums over the pre-setting variable `Ω` | K: `iterate_dependsOnlyOn_ball` (`RegionTower.lean:283`) and `readout_unaffected_outside_ball` (:304) prove the cone for any site type, with no finiteness of the site set or alphabet (section variables, :246), given a `CouplingGraph` (:254): each site's next value depends only on a finite neighbourhood. Census 8, current. The kernel statement is for `Q`-valued functions `f : (ι → Q) → Q`; a readout into another alphabet needs a one-line paper step through `site_iterate_dependsOnlyOn` (:297). **The coupling-graph hypothesis is not derived without A1.** [IR] countercontrol, from the review of r5, checked on paper by the writer: on `(Z/q)^Z` let `T` be the set of `s` with `s_i ≠ s_{i+1}` for infinitely many `i`, and `φ(s) = s + 1_T(s)·(1, 1, …)`. `φ` is a bijection, each output `φ(s)_i` is insensitive to every single component `j ≠ i`, and yet `φ(s)_i` is a function of no finite set of components. On the classes used here the hypothesis comes from named posits: posit (xiii), "each F_i reading the current values at finitely many sites and each site read by finitely many F_i", and posit (viii), site factorization (Main:724); for I-deep, GR:132's "each component's update depends on finitely many components"; in the kernel, `FiniteRange`, which extends `CouplingGraph` (`QuasilocalAlgebra.lean:919`), with `leapFiniteRange` (`SecondOrderDrive.lean:306`) for `ruleDynamics`. I-meas carries no such structure, so the cone is unavailable there unless the hypothesis is added. [IR] With a probability measure on `Ω` the Bell ceiling's argument gives `|S_CHSH| ≤ 2` unchanged | cone: established (K) on infinite site sets, conditional[the coupling-graph hypothesis, from posits (xiii) and (viii), or GR:132]; Main:362's derivation of that hypothesis needs finite `V`. Bell ceiling: established (P) at finite scope; infinite form [IR], open on `main` |
| AM-8 | §4.6, structural exclusion of equilibrium-phase observers (Main:740–760) | "where in a finite bijective (S, φ) observers can exist" (Main:742); the scope "uses bounded coupling, finiteness of S, the canonical-typicality result [31], and the effective-mixing hypothesis (EM)" (Main:758); Main:724 (ii): §4.6's "conclusions hold on the finite representative" | not stated. [IR] context: Main:758 (ii) places the needed gap in the coarse-grained channel because "the exact Koopman operator of a finite permutation has modulus-one spectrum and cannot mix". On the OBL class the Koopman operator is mixing (support off `main`, PR #1303), so that reason is specific to finite permutations. Mixing does not supply a spectral gap, and (EM) stays a separate hypothesis | conditional[A1; bounded coupling; [31], external; (EM), posited]. Without A1: open (Q9) |
| AM-9 | The §3.4 obstructions for a fixed finite realization: Main:486 (no uniform finite realization), :496 and :556 (generic intervention combs), :558 and :600 item (3) (classical-dimension obstruction), :638 (all-time periodicity) | each is a theorem about one fixed finite `S`; Main:60: they "bear on nature through it" | each stays true of every finite realization (1.4, 1.7) and none applies to an infinite class. Main:486's counting argument does not extend to an infinite `S` | established at scope (Main:558 conditional on the imported [55], 1.7). As statements about nature: conditional[A1] |
| AM-10 | Statements of the framework's claim that name A1: falsifiability (Main:718, "a finite set with a deterministic bijection, finiteness being the total-finiteness posit"); Main:36, :44, :222 | the claim is stated with A1 | nothing to recover: each is conditional on A1 by its wording | statements, not theorems |
| AM-11 | Substratum Theorem 23 (Sub:193) and Lemma 23.0 (Sub:189); Sub:104, :106–117, :123–129; Struct:47; GR:342 (framing with A1–A6); `book/ch02-substratum.md:88–122`; DEPENDENCY-AUDIT.md:287 | A1 is a hypothesis of both; Stage 1's output asserts "S finite" (Sub:125); the critical dependencies include the §3.2 forward dilation (Sub:110; AM-5) and the slow-bath form of C2 necessity (Sub:193; AM-21) | no A1-free form on `main`. The audit row (:287): "No unrestricted generalization"; "Keep explicit A1_finite and other physical hypotheses" | conditional[E1–E7, M1-T, M1-B, A1–A6, the hidden-sector mixing hypothesis, the nearest-neighbour premise, and the SM hypotheses named in the statement], as stated. Without A1: open. Which stages beyond Stage 1, the §3.2 dilation and C2 necessity consume A1 is not traced here |
| AM-12 | Theorem 24 beyond (iii), and its Corollary (Sub:251–268); Struct:646 (Proposition 9.5) | (i) hidden relabelling with the uniform hidden prior `1/|C_H|` (Sub:253); (iii) finite factors only (Sub:262); Corollary (i): E3 "is the interpretive premise of A1" (Sub:268) | (i): [IR] an infinite form would need a relabelling that preserves a stated normalized prior; not stated. (ii) alphabet change (Sub:255) is stated under the alphabet-size hypothesis; whether it uses A1 is not traced (SM §2.7). (iii): finite only; infinite form not established (1.6). (iv) is a structural comparison through the finite-law representation of Main §3.4, which uses Lemma 1 only (Main:60) | (i), (iii): established (P) on finite carriers; infinite forms open. (iv): not a consumer. Proposition 9.5 restates (i) and (iii) for substrata satisfying A1–A6 |
| AM-13 | Computation:118, the finite-size consequence | "The total-finiteness posit ... takes S finite"; the §4.3 characterization is exact in the limit `S → ∞` and does not use A1 | the `S → ∞` characterization | a proposal conditional on the patch-budget hypothesis and the stated conjectures; "not entailed by Main" |
| AM-14 | GR boundary-only dependence lemma (GR:112–114) and the deep-sector corollary (GR:132–138) | the lemma is stated for "a finite product of site configuration spaces" with a uniform hidden prior | the corollary's first statement "holds also for an infinite deep sector, given a normalized product prior on it, a locally finite coupling graph and well-defined dynamics ... in which each component's update depends on finitely many components" (GR:132, proof :134) | established (P), including the infinite deep-sector form of the first statement. Recurrence-scale content is AM-1 |
| AM-15 | Methodology on A1: Meth:156 ("the exact-recurrence step and the eventual-image restriction of the injectivity recovery — consume finiteness of the hidden factor as well ... it is the structural assumption A1"); rung 6 (Meth:158, :166, :253, :261) | "Bijectivity of φ holds on the finite total representative, from injectivity ... together with finiteness of the total space, which is A1" | as AM-1 and AM-3 | as AM-1 and AM-3 |
| AM-16 | SM's finite-torus theorems (SM:294–296, :1606) and the counting-measure results (SM:252, :334, :641) | each is stated on a finite torus or under the counting measure; the wave substratum on a finite torus satisfies A1 in the kernel (`waveSubstratum_A1`, `SubstratumInterfaceAudit.lean:185`, from `a1_of_finite` :109; census 15, kernel-only), as does the reversible hexagonal lattice gas (`hexSubstratum_A1`, `HexLatticeGas.lean:312`; census 49, kernel-only) | the finite-torus theorems are G-fam members and keep their scope; the infinite lattice is a different carrier (OBL §4.1; established for that rule and measure, support off `main` (PR #1303)) | established at their scope. Whether other SM results need A1 or only a finite alphabet and locality is not traced here. Census 53 is recorded in §7.2 |
| AM-17 | Book mirrors and framing: `ch01-observation.md:28`, :119; `ch02-substratum.md:16`, :76 (FULL:710); `ch18-beyond.md:168` (FULL:4974); `appendix-c-objections.md:112–124` (FULL:6342); `glossary.md:11`; `ch03-structural-realism.md:22`, :34, :44; `ch04-methodology.md:10–26`; `ch05-gauge-structure.md:19`, :23; `ch09-universality.md:194`; `README.md:100` and `readers-guide.md:79` (topic lists naming "the finiteness posit") | each restates A1, frames the setting with it, or mirrors a row above. `ch18-beyond.md:168`: the substratum's information content "under the finiteness posit A1 ... is finite" | as the row each mirrors | conditional on A1 by their wording; each was read at the hits listed. FULL mirrors carry the same text at the lines given |
| AM-18 | Verification records: DEPENDENCY-AUDIT.md:281–291 (audit record; review independence not established, :17–19); `continuous-substates/` (RR) | the audit's matrix records the finite-`S` proof retained for each row | rows :287 (AM-11), :288 (AM-14), :290 (H-product, 1.2) and :291 (AM-4) are used above. Row :289, finite boundary entropy and the ħ gap: "Requires a physical finite-mode/boundary state and H-slope/KMS/thermal match hypotheses; not deduced from `|V_O|<infty` alone". Whether it consumes A1 beyond the boundary layer is not traced here. Row :285, control 3: a binary readout of a countable union of finite cycles, with full-support invariant probability, pointwise periodicity and Poincaré recurrence, whose measured visible matrix is the identity at no positive step; I-meas context for 1.2, not established | audit record and RR: context only |
| AM-19 | The phase-locking lemma and its ancilla-marginal form (Main:228–260) | none in the lemma as stated: a Hermitian operator on `C^n`, with `n` from Lemma 1, and a dilated space of dimension `n m_a` with `m_a` a parameter (Main:250, :256). [IR] Its application to the substratum's emergent Hamiltonian runs through the §3.2 setup (AM-5) | the lemma as a finite-dimensional statement | established (P; K for the two-branch identification cited at Main:242). The substratum application inherits AM-5 [IR] |
| AM-20 | The characterization theorem (Main:536–544) and its recurrence-scale content: Main:536 ("consider dynamics on accessible timescales t ≪ t_R where t_R is the Poincaré recurrence time of any realizing substrate"); item (ii), "k τ_S ≪ t_R" (Main:540); Main:733 (the "bare-recurrence form from a non-permutation rooted map at t_R"); Main:18 and Main:80 item (2) (indivisibility "somewhere in the recurrence cycle of a fixed finite reversible representative"); Main:626 (P-indivisibility "unconditionally at the recurrence scale"); Main:60, quoted verbatim: "The physical reading of the characterization theorem — the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice, an empirically motivated reconstruction rather than a pure derivation; the law-level equivalence of §3.4 itself holds for every finite-horizon law." | `t_R` is defined through exact recurrence of the realizing substrate, which holds on a finite substrate; A1 makes nature's substrate finite. Exact recurrence fails in the OBL class, where `F` has infinite order (refuted within the OBL class, support off `main` (PR #1303); 1.1). The physical reading uses A1 by Main:60's own sentence | (ii) ⟺ (iii), and (i) under (T), as law-level statements: (iii) builds a finite `C_H` for each horizon, and Main:60 and :354 place the readback lemma and the in-house representation outside A1 | law-level content: established at its scope (1.6). The accessible-timescale qualifier, read for an infinite substrate, is not stated on `main`: open. The physical reading: conditional[A1]. The bare-recurrence form (Main:733) is AM-1 |
| AM-21 | The C2-necessity theorems: the quantitative mixing form (Main:453) and the physical-memory process form (Main:467), with the mechanism (Main:445–449) and the slow-bath remark (Main:502) | each is stated for "the uniform-prior bijection marginal of §3.2's construction", with `π_H` the uniform hidden prior defining `T`; so they inherit AM-5 (`C_H` under A1, Main:266). The mechanism cites Poincaré recurrence "at t_R exponentially large in the system size" (Main:445) | the persistence form of C2 necessity holds without a mixing hypothesis (Main:536, :502), on the finite coupling-step model. No form for an infinite hidden sector is stated | conditional[A1; the mixing hypothesis for the slow-bath form, posited]. Without A1: open. Theorem 23 consumes the slow-bath form (Sub:193; AM-11) |
| AM-22 | GR:58, the classical horizon temperature as a counting derivative, under H-count | "Restrict the finite total system to a conserved energy shell ... uniform counting gives P(i)=Ω_H(E−e_i)/Σ_j Ω_H(E−e_j)": A1 and the counting measure (AM-4), with the named hypothesis H-count. The finite-reservoir correction is a finite-total statement | not stated without A1. DEPENDENCY-AUDIT.md:289 (finite boundary entropy and the ħ gap) is probably the same item; not traced further | conditional[A1; H-count, named hypothesis]. Without A1: open |
| AM-23 | Comp:100, the super-BQP exclusion | "Hypercomputation [6], oracle access [7], and other super-BQP capabilities would require either continuum precision (violating A1), unbounded coupling (violating A3), operations outside the operational-closure model ..., or violation of these efficiency hypotheses" | without A1 the exclusion loses the continuum-precision leg; the other legs and the efficiency hypotheses stand as stated | conditional[A1, A3, the efficiency hypotheses] as stated. Without A1: the first leg is open |
| AM-24 | Methodology's constructive-OSR claim (Meth:339–369), "constructive OSR within the nearest-neighbor A1–A6 class" (Meth:367) | it restates Theorem 23 (Meth:339) and states the claim within the A1–A6 class | as AM-11 | conditional on A1–A6 and the nearest-neighbour premise by its own wording (Meth:367); a consumer of the AM-11 kind |
| AM-25 | Lean, carrier 3: census 15 (`SubstratumInterfaceAudit.lean` Section E, :764–800: `obsTheory`, "the sourced theory on its configuration space, under the finiteness A1 supplies", with `[Fintype 𝒮.ι] [Fintype 𝒮.V]`, and the sourcing theorems that follow) and census 31 (`obsTheory_nonnegBounded`, `FrozenSourcing.lean:84`, "at every substratum satisfying the finiteness A1 supplies"); both kernel-only | `obsTheory` is a `FiniteOperationalTheory` on the configuration space, which needs that space finite; the sites and alphabet carry `Fintype` | not stated for an infinite configuration space | established (K) under A1, kernel-only. These face carrier 3, the operational theory, and so bear on EXACT. Without A1: open |
| AM-26 | Record: MR-1 preregistration, `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md:260`, :361, :372 | "(P-set) kinematics: S is a set of states (finite under the total-finiteness posit, Main:62)"; its "Main:62" is Main:60 at this base | — | research-only preregistration (its own status line); context only |

### 7.2 Results checked and found not to consume A1

- The stochastic-inverse lemma, the readback lemma, the §3.4 equivalence and its process and
  intervention dilations, and reverse finite realization: Main:60 states that they use only Lemma 1,
  "in which a finite hidden space is constructed, not assumed" (1.6).
- GR's universality-class results (U1)–(U3), which rest on S1–S4: "A1 (finiteness) implies S3 with
  finite ε" (GR:669). A1 is sufficient for S3 there; it is not a premise of those results.
- Structure's comparisons of other programmes with A1–A6 (Struct:80, :134–140, :230, :256–331,
  :1030–1040) and `book/ch09-universality.md:194`: classifications of programmes, not consumers.
- Theorem 24(iv) (AM-12).
- Census 53, `cx3b_complex_not_A1` (`A6Instantiation.lean:512`, kernel-only): a kernel negative.
  The complex carrier on which the SM derivation of `SM.md:114` and Theorem 5 is conducted is not an
  A1 substratum, and the docstring adds that "A1 is not weakened". It records an SM derivation
  carried out on an infinite carrier, and it consumes no A1.
- Substratum's class-defining and defence statements for A1–A6 (for example Sub:205–223): they
  delimit AM-11's class and are not separate consumers.
- GR:260 ("The controllability resource is not entailed by A1–A6"): a statement of what A1–A6 do
  not supply.
- Main:14, "An observer embedded in a finite deterministic system": the class D of the equivalence
  is finite by construction (Main:546). The sentence frames the setting and is the premise of no
  result.

### 7.3 Finding for the owner: the reading in #1169 comment 6893456888

The comment (`amaybaum`, 2026-11-15T11:12:09Z) records a correction. It also contains a reading of
the corpus that the source supports in one sense and not in another. The difference is recorded here
as a finding. It is not settled here: the source governs (AGENTS.md §A.45 rule 1).

- **The comment.** Total finiteness "is a premise only of the results that use it, for example the
  per-horizon equivalence's finite hidden configuration space (Main.md:111, :266)". Its decision
  text adds: "Unless the A1-dependent results are recovered without A1, or through #1007, the main
  equivalence stays conditional on that posit."
- **The source.**
  - Main:111 is the setup of §2.3, the recurrence argument. Main:266 is the setup of §3.2, the
    Stinespring route. Neither is the setup of the §3.4 equivalence (Main:546).
  - Main:60, both halves, quoted verbatim. First: "the following results use only that of Lemma 1:
    the stochastic-inverse lemma and the readback lemma (accessible conditional memory) of §2.3,
    and the equivalence of §3.4 with its process and intervention dilations, in which a finite
    hidden space is constructed, not assumed." Second: "The physical reading of the
    characterization theorem — the identification of nature with a finite reversible substratum —
    is accordingly conditional on that representation choice, an empirically motivated
    reconstruction rather than a pure derivation; the law-level equivalence of §3.4 itself holds
    for every finite-horizon law."
  - DEPENDENCY-AUDIT.md:282 (audit record) says of the equivalence: "existence of finite
    representatives of finite visible laws; not a characterization of the actual infinite
    substrate".
  - Main:716's "two routes" to the transition-statistics layer are §3.1, the Barandes route, and
    §3.2, the Stinespring route (Main:352, :356). The §3.2 route uses A1 (AM-5). A route that does
    not use A1 exists on other support: the §3.1 route needs finite `C_V` and (T) (Main:208, :354),
    and the in-house fixed-basis representation exists for every finite-horizon law (Main:354, :60).
- **Three readings of "the main equivalence".**
  1. The law-level §3.4 equivalence `S ⟺ D ⟺ Q_fb`. By Main:60 it uses Lemma 1 only and is not
     conditional on A1.
  2. The §3.2 route: the channel with `ρ_H = I_m/m`, the Born-form representation, permutation
     unitarity, diagonal preservation and CP-indivisibility. These use A1 (AM-2, AM-5).
  3. The characterization theorem (Main:536), and in particular its physical reading, the
     identification of nature with a finite reversible substratum. By Main:60's second sentence that
     reading is conditional on A1 (AM-20). This reading is the closest to the comment's words.
- **For the owner.** Which of the three readings the decision text means. This inventory follows
  Main:60: it does not treat the law-level §3.4 equivalence as conditional on A1 (1.6), and it
  records the physical reading of the characterization theorem as conditional on A1 (AM-20). The
  comment's correction itself, that "the Definition and the two axioms do not fix the cardinality of
  S", agrees with Main:60.

### 7.4 Limits of the map

- The searches are bounded by the phrases in §5; a paraphrase outside them could have been missed,
  as r5's list missed the items added in r6. Items marked "not traced here" are listed in their
  rows: the later stages of Theorem 23, Theorem 24(ii), SM results beyond those cited, and audit
  row :289 (probably AM-22).
- Rows give status at proved scope. No row recovers a result without A1, and no row changes a
  status on `main`. Cells resting on OBL-RO3-2 are labelled support off `main`.
- Where a row names a replacement hypothesis (the coupling-graph hypothesis of AM-7, from posits
  (xiii) and (viii); a stated normalized measure in AM-4; the invariant probability of §3's Q-A), it
  records a hypothesis the source or kernel uses or the review proposes. It does not adopt one.

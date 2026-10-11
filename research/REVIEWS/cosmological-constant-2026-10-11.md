# Review — the cosmological-constant argument (GR §6, book chapter 7 §§7.7–7.8, the G3 coupling map)

An independent review thread, requested by the owner on 2026-10-11 ("Review as another independent research
thread"): the owner's external assessment of the cosmological-constant argument was checked against the corpus at
the certified base L = `9f9f8257`. Findings only; no manuscript file is changed (manuscript hold). The owner's
reply of the same day is recorded in §4 with attribution. Evidence levels: [W] written in the corpus; [K] kernel; [L]
literature; [A] audited record.

## 1. What the corpus states

- **GR §6** (papers/GR.md:322–365). §6.1 states the vacuum-energy problem in the standard form (the computed
  zero-point density against the observed dark-energy density). §6.2 states the framework's reading: the emergent
  quantum description has a vacuum-energy *offset ambiguity*, which the framework calls a description artifact; it
  distinguishes a *descriptive* distinction (the offset is not an observable of the emergent description) from the
  *dynamical* decoupling (the offset does not gravitate), and makes the second **conditional on the covariant
  matter-to-boundary coupling, the G3 map**, which is OPEN. Two gravitational completions are described there with
  the same emergent quantum transition statistics and different gravitational responses. Later sentences of §6.2
  then assert the decoupling without the condition (finding F2). §8.3 (567–582) and §8.5 (609–666) repeat the
  dissolution in the paper's summary register; the §7.4 table (532–553) carries a row for it; line 398 carries a
  remark on the scale identity.
- **Book chapter 7 §7.7** (book/ch07-gravity.md:155–193) presents the dissolution as achieved: the vacuum-energy
  discrepancy is "exact, not approximate" (the ratio of the Planck density to the observed dark-energy density is
  identified with the horizon entropy), and the decoupling is asserted; §7.8 (197) opens from it; the table row (288)
  and the close (305) restate it. `The-Incompleteness-of-Observation-FULL.md` mirrors these at 2074, 2165, 2560 and
  5202.
- **verification/ROADMAP.md**: P2 rows (73–74) and the §P2 text (1136–1144) name "Covariant matter→boundary coupling
  (the G3 map)" as OPEN.
- **verification/lean-manuscript-census.json**: no gravitational family; nothing of §6 is kernel content.

## 2. The external assessment, checked

| claim in the assessment | corpus | verdict |
|---|---|---|
| the framework reproduces the standard statement of the problem | GR §6.1 | accurate |
| the framework's resolution is an offset ambiguity of the emergent description | GR §6.2 first part | accurate |
| the dynamical decoupling is conditional on an open coupling result (G3) | GR §6.2, ROADMAP P2 | accurate for GR §6.2's conditional sentences; the book and GR §8 assert it unconditionally (F1, F2) |
| the ratio ρ_Planck/ρ_Λ ~ S_dS ~ 10¹²² is an exact identity of the framework | book §7.7 "exact, not approximate" | overstated: a scale identity with a convention-dependent coefficient (F3) |
| G3 is the critical missing result, alongside the full quantum-equivalence proof | ROADMAP P2 | accurate |

## 3. Findings (corpus defects; propagation items recorded, not applied)

- **F1 — the book leads the paper (§A.25).** Chapter 7 §7.7–§7.8 and the FULL.md mirrors assert the dynamical
  decoupling that GR §6.2 conditions on G3. Propagation item: make the book's statements conditional in the same
  words as GR §6.2's conditional sentences, at the four mirror sites.
- **F2 — GR §6.2 qualifies, then asserts.** After the conditional statement, later sentences of §6.2 (and §8.3,
  §8.5, the §7.4 row) state the decoupling without the condition. Propagation item: remove the unconditional
  sentences or carry the condition into each (§A.30: never assert-then-qualify).
- **F3 — "exact, not approximate" overstates a scale identity.** With ρ_Planck = c⁷/(ħG²), ρ_Λ = Ω_Λ·3H₀²c²/(8πG)
  and the horizon entropy S_H = A/(4ℓ_P²) with A = 4π(c/H₀)², i.e. S_H = πc⁵/(ħGH₀²), the exact relation between the
  defined quantities is

  ρ_Planck / ρ_Λ = (8 / (3 Ω_Λ)) · S_H,

  a coefficient 3.86 at Ω_Λ = 0.69 (the owner's closed form, verified by the coordinator; the coordinator's earlier
  numerical ratio ρ_Planck/ρ_Λ ÷ S_dS = 3.86 is the same statement). The coefficient changes with the horizon and
  cutoff conventions. The correspondence is an order-of-magnitude scale identity, not an exact equality, and by
  itself not an independent prediction of the framework. Propagation item: replace "exact, not approximate" by the
  scale statement with its coefficient and conventions.
- **F4 — "precisely observed" conflates ρ_crit with ρ_Λ.** The observed quantity entering the comparison is the
  dark-energy density Ω_Λ·ρ_crit (ρ_crit c² between 7.7×10⁻¹⁰ and 9.0×10⁻¹⁰ J/m³ for H₀ between 67 and 73 km/s/Mpc),
  not ρ_crit. Propagation item: name the quantity.
- **F5 — the label G3 is undefined in GR.md and collides.** GR §6.2 uses "G3" for the coupling map without defining
  it there; Main.md uses G3 for the genericity condition and Structure.md uses G3 for the gauge Level G3. Propagation
  item: define the coupling map locally in GR §6.2 and give it an unambiguous label corpus-wide (the owner proposes
  `G3-grav`), with the ROADMAP row renamed to match.
- **F6 — status and axis (§A.23).** Nothing of §6 is kernel content; the dissolution is a written argument [W]
  whose physical half is CONDITIONAL on an OPEN theorem. It sits on the consistency axis (the framework's claims
  follow from its premises), not on the correctness axis: the scale identity is a retrodiction of a known number and
  moves no band. Bands unchanged.

## 4. The owner's refinement (2026-10-11, recorded with attribution)

- **The critical distinction.** The corpus supports: OI substratum → emergent quantum description → vacuum-energy
  offset ambiguity. What remains unproved is: offset ambiguity ⇒ no gravitational contribution. The two
  gravitational completions of GR §6.2 show why: identical observable quantum transition statistics need not imply
  identical gravitational responses. Classification of the current claim: **a written structural explanation of the
  discrepancy, with its physical resolution conditional on an open gravitational coupling theorem.**
- **The scale relation.** The closed form of F3 is the owner's; the coordinator confirmed it.
- **Proposed success criteria for G3** (proposals, not claims of the repository): (i) derive which underlying energy
  contributions source curvature rather than stipulating that emergent vacuum offsets do not; (ii) establish how
  physically relevant energy differences — particle masses, binding energies, vacuum changes during phase
  transitions — gravitate; (iii) demonstrate covariance, conservation consistency and compatibility with established
  gravitational behaviour; (iv) show that the resulting vacuum-energy suppression does not reintroduce fine-tuning
  through the coupling rule itself. In particular, removing an arbitrary common Hamiltonian offset is distinct from
  explaining the gravitational effects of changing Higgs or QCD vacuum states; a successful G3 result must address
  both.
- **The fundamental-status question.** The current descriptive distinction establishes internal explanatory
  consistency; a G3 theorem would establish a derived gravitational mechanism if it establishes decoupling; the full
  OI–QM equivalence would establish a mathematical reconstruction under its stated premises; only a distinctive
  successful physical prediction would supply empirical evidence favouring OI over competing frameworks. Even a
  completed G3 theorem would not by itself show QM to be physically non-fundamental.
- **Manuscript recommendations.** The owner agrees with F1–F5 and adds the unambiguous label; the edits should keep
  the distinction between a written argument [W], a formally checked theorem and an experimentally discriminating
  prediction. No manuscript change has been made.

## 5. Standing

| item | status |
|---|---|
| the descriptive distinction (offset ambiguity of the emergent description) | written [W], consistent with the kernel's reading of measurement as a trace-out projection |
| the dynamical decoupling (the offset does not gravitate) | CONDITIONAL on the G3 coupling theorem — OPEN (ROADMAP P2) |
| the scale identity ρ_Planck/ρ_Λ = (8/(3Ω_Λ))·S_H | exact between the defined quantities; a convention-dependent coefficient of order one; a retrodiction, not a prediction |
| manuscript propagation (F1–F5, the label) | recorded; awaiting the lifting of the manuscript hold and the owner's direction |
| axis (§A.23) | consistency; correctness bands unchanged |

Pursuing G3 is separable from the OI ⇒ QM work; the owner's criteria (i)–(iv) are the acceptance tests a G3 round
would preregister.

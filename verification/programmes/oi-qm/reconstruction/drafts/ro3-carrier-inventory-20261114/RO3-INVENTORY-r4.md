# RO-3: carrier and exactness inventory, r4

**UNREVIEWED.** r4 is r3 with one wording correction and nothing else. It applies item m8 of the
independent review `REVIEW-OBL-r1.md` (at `76ca4c3d`): in 2.5, "Neither route is checked here"
follows a paragraph that names only one route, so it now reads "This route is not checked here". The
review's required change R1 concerns `OBL-RO3-2-r1.md` §3.2. No passage of r3 rests on it; r3's only
related statement, `φ^L ≠ id` in 1.1 I-qloc, remains true. r1, r2 and r3 are left unchanged. r4 has
not been reviewed.

r3's history: r3 was a minimal editorial revision of r2, which is left unchanged, as are r1 and the
reviews. The owner authorized "an optional minimal r3 applying the three nonblocking wording
corrections" and adopted decisions on Q10–Q12 (#914 comment 6883249235, `amaybaum`,
2026-11-14T19:48:13Z, "I approve, proceed as suggested"). The three corrections are nits N1–N3 of the
ChatGPT exact-head review of r2 (PR #1303 review 5906337933, at `7d265311`, ACCEPT WITH NITS). r3
changes only:
- the wording of the decision rule in §3 (N1);
- the access sentence in 2.3 (N2);
- the separation of Haar invariance from the bridges to `referenceState` and to the observer
  interface in 2.5 and §3 (N3);
- §4 Q10–Q12, which now record the adopted decisions;
- one row in §6 for the two new governance references.

Nothing else differs from r2. r3 has not been reviewed.

r2's history: r2 revised r1 and applied the independent review of r1 (`REVIEW-r1.md`, ACCEPT WITH
CHANGES, at `0d6d8812`); the disposition of each finding is in `RESPONSE-r1.md`.

## Standing

- **Authorization.** #1055 comment 6881390849 (`amaybaum`, 2026-11-14T17:23:23Z), quoted verbatim:
  "Yes, I authorize RO-3 on these terms". Writer: Claude Code. Reviewer: ChatGPT, at the exact
  commit, after an independent review.
- **Scope.** The owner's Q5 text, #1055 comment 6880024537 (2026-11-14T15:46:34Z), quoted verbatim:
  "Inventory recurrence, recurrence-based P-indivisibility and A.8 cycle averages for each candidate
  carrier. Preserve their finite-carrier scopes and identify what extra hypotheses or replacement
  proofs a completion would require. Include finite stages as an intermediate case and countable or
  infinite completions as candidates. The ultimate test remains one fixed underlying model
  supporting arbitrarily large finite quantum carriers with explicit encodings and resources."
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
  - Gate A answer 4 (same comment): "Require quantum behaviour for every physically performable
    experiment within C. This includes accessible preparations, interventions, compositions and
    complete records under the retained contract."
- **Limits.** Paper-only. Reading, analysis and writing. No computation on OI rules, no Lean, no
  simulation, no repository edit. This record adopts no premise, completion, sector condition C or
  extension E, changes no scientific status and no planning entry, and decides nothing on RO-1 or
  #1143. EXACT stays open.
- **Base.** Corpus read at `main` `dfeec843bec08443b25cffe34d33dc8401c3b604`.
- **Ledger.** Read at `records/unified-ledger-914-20261114` `9ff3b8d913abfe720273ff162f6340054cb69437`,
  file `verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/LEDGER-r8.md`
  (cited below as "ledger").
  - The owner accepted r8 at that commit: #914 comment 6880700869 (`amaybaum`,
    2026-11-14T16:31:06Z), quoted verbatim, "Yes. I accept ledger r8 as the successor to r5."
  - A draft r9 now exists on that branch at `4470bd02`, pending review. A diff of r8 against r9 on
    the identifiers cited here (B-QM-8, B-QM-16, B-QM-27, B-BH-3, J-3, J-4, M5, QM–BH, QM–A1) finds
    one added row that cites B-QM-16/17 and no changed row.
  - The ledger is not on `main`; §6 traces its use.
- **Citations.** `path:line` refers to physical lines at the base. `papers/*.md` paragraphs are
  single long lines, so one line number can cover a whole theorem. Lean modules are under
  `verification/lean-mathlib/OIBridge/`; they were not rebuilt here. Census family numbers are the
  indices of `families` in `verification/lean-manuscript-census.json`.

### Status labels

- **established**: proved at the cited layer for the statement as made, at its stated scope. The
  layer is given: K (kernel on `main`), P (paper proof in a manuscript), EX (exhaustive or exact
  finite computation on `main`).
- **conditional[...]**: proved given the bracketed hypotheses, each with its status at source
  (posited, open, or a named hypothesis).
- **refuted within <class>**: a result on `main` shows that the property fails for every member, or
  for a stated member, of that class.
- **open**: no proof and no refutation on `main` at the stated scope.
- **RR**: a research record on `main` whose own status note says its proofs are paper-level and not
  independently reviewed (`verification/programmes/substratum/continuous-substates/README.md:3`,
  :23–32). Under AGENTS.md §A.46 items 1 and 7 an RR item is not established and is not used here as
  a premise. Where an RR item bears on a cell, the cell keeps its status and the RR item is listed as
  context.
- **[IR]**: a reading made by this inventory or by the review, not stated on `main`, not
  independently verified. An [IR] item is context or a candidate for a later obligation. No cell's
  status rests on it.

## 0. Three carriers, and the classes compared

The question involves three different carriers, and the inventory keeps them apart.

1. **The total substratum carrier** `S`, with its bijection `φ`. A1 says `S` is finite
   (`papers/Substratum.md:92`). A1 is a posit: item (ii) of the posit ledger
   (`papers/Main.md:724`), "the total-finiteness posit" (`papers/Main.md:60`). This inventory keeps
   it so.
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
| **I-nonorm** infinite carriers without a normalized invariant prior | for example an infinite invariant measure | yes, but no rooted law is defined |

Class I-nonorm is listed so that it is not silently merged with I-meas. Every rooted map below is a
probability under a normalized prior, and the corpus states that an infinite extension needs "its
own normalized measure or trace-class state and a well-defined evolution"
(`papers/Substratum.md:262`; also :52, :92; `book/ch02-substratum.md:32`).

G-sub and G-fact differ in how a finite model sits inside the fixed model:
- A finite invariant sub-carrier carries a finite model only for preparations supported on it. In an
  infinite model such a subset is a global constraint, not a subsystem. Under a prior of full
  support it has measure zero; [IR] this is so for the periodic sectors of 2.3 under the uniform
  product measure and for `(Z/N)^{2L}` under Haar measure on the torus.
- A finite factor carries a finite model under the fixed model's own normalized prior, for readouts
  that factor through it.

## 1. Source-pinned comparison table

Rows are result × class. "Hyp." names the hypotheses each cell needs beyond the class definition.

### 1.1 Exact recurrence (`φ^L = id` on the carrier)

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (P; K) | A1 (posit); `φ` bijective (A2) | `papers/Main.md:121` (Step 1), :60 (the representative is "defined here for a finite system only"); K: `iterate_return_at_order` (`RootedRecurrenceBridge.lean:47`, census 114, kernel-only) |
| G-fam | established for each member; no common period across members | each member finite and bijective | side-`L` ring, prime `q ∤ L`: order `qL` (`papers/SM.md:1606`, Theorem A.1); `d`-dimensional torus, prime `p ∤ L`: `F^{p(p^{2m}−1)} = I` with `m = ord_L(p) ≤ L−1` (`papers/SM.md:296`) |
| G-sub | conditional[the stage is a finite `φ`-invariant sub-carrier] | invariance and finiteness of the stage | `papers/GR.md:587` (a finite representative of the constraint surface, invariant under `φ`, has finite order `L`). RR context: `(Z/N)^{2L}` in the free 1-D torus map (`continuous-substates/README.md:105–112`) |
| G-fact | recurrence of the finite factor: as F for the factor; the fixed model need not recur | the factor map intertwines the dynamics | RR context: the `p`-adic case (`continuous-substates/README.md:113–121`) |
| I-deep | open; not inherited | — | "The recurrence proof ([Main, §2.3]) requires S finite, which Lemma 1 does not supply" (`papers/GR.md:138`); the transfer corollary "does not imply recurrence of every unobserved sector" (`papers/Substratum.md:268`) |
| I-qloc | open | — | no recurrence statement for the quasilocal automorphism (`papers/Main.md:588`; search in §5). [IR] context, from the review: for the posited linear rule at prime `q` with `α ≢ 0`, no nonzero finitely supported configuration is periodic, so `φ^L ≠ id` for every `L ≥ 1` (§3) |
| I-meas | open as a microscopic statement | — | `papers/Main.md:155` is a visible statement for continuous-time flows; see 1.2. RR context: `continuous-substates/README.md:85–91` |
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
| G-fact | conditional[the readout factors through a finite factor; the factor map intertwines the dynamics and carries the prior to the factor's prior; H-product on the factor] | as stated | [IR]: under these hypotheses the rooted law computed in the fixed model equals the factor's rooted law, so the factor's return applies. RR instance: the lowest-digit readout of the `p`-adic free map, with `Γ_{ord(F mod p)} = I` "for every sub-state" (`continuous-substates/README.md:113–121`, :135–137) |
| I-deep | open | — | none on `main`. For a deep factor that no dynamics couples to the boundary, the finite identity (`papers/Substratum.md:257–262`) would carry the finite visible return over, but its infinite form needs "its own normalized measure or trace-class state and a well-defined evolution, and is not established" (:262) |
| I-qloc | open | — | none on `main`. [IR] context: §3 (the reviewer's mixing reading) |
| I-meas | conditional[`π ∘ T^L = π` almost everywhere]; open otherwise | a measure; a finite visible partition with cells of positive finite measure | K, cell-conditioned convention: `measuredGamma_eq_one_iff` (`ObservableMeasureReturn.lean:83`; census 120, kernel-only) defines the rooted entry as the ratio of joint-cell mass to initial-cell mass, takes an arbitrary measure, needs positive finite cell masses, and does not use invariance (its docstring, :79–82; header, :14–20). It agrees with Main's convention under H-product. P in RR: `continuous-substates/observable-recurrence.md:15–36`. Main: for continuous-time Hamiltonian flows, near-total common visible return fails at every sufficiently late time for a mixing flow (`papers/Main.md:155`). RR instances: difference readouts of the free 1-D torus wave map and lowest-digit `p`-adic readouts return exactly; the single-site real readout does not (`continuous-substates/README.md:85–121`, :125–144) |
| I-nonorm | no statement possible | — | as 1.1 |

Context [IR]. In discrete time, `Γ_n = I` for one `n > 0` makes each visible cell `T^n`-invariant up
to null sets, hence `Γ_{kn} = I` for every `k`. A mixing system sends `μ(C_a ∩ T^{-kn} C_a)` to
`μ(C_a)^2`, which differs from `μ(C_a)` for a cell of measure strictly between 0 and 1. So a mixing
system with a nontrivial finite partition has no positive-time exact visible return. Main states the
continuous-time, late-time form for Hamiltonian flows (`papers/Main.md:155`). The discrete-time
statement for every positive time is not on record, and no cell above rests on it.

### 1.3 Recurrence-based P-indivisibility

The results: the one-step theorem (`papers/Main.md:113–127`); history readback with finite recurrence
(:135–139); overlap and return (:141–143); the constraint-surface form (`papers/GR.md:587`); and the
CP-indivisibility theorem that rests on them for the permutation-dilation family
(`papers/Main.md:330`; listed among the uses of the finite representative at :60). Book mirrors:
`book/ch01-observation.md:95–109`; `book/appendix-b-derivations.md:92`, :413.

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (P; K for the final steps) at recurrence-cycle scope only | A1 (posit); A2; H-product; some rooted map not a permutation (under the uniform prior for :113; any root-shared prior, full support not needed, for :141) | P: `papers/Main.md:113–127`, :135–139; K: `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`, census 34, current), `isPermMatrix_of_stochastic_inverse` (`EquivalenceChain.lean`), `pIndivisible_at_order_of_nonperm` (`RootedRecurrenceBridge.lean:104`, kernel-only). Paper-only steps are listed at `papers/Main.md:137`. Scope: "a global recurrence-cycle result", not a statement about accessible windows (:139, :157; `papers/GR.md:587`) |
| G-fam | established for each member at that member's recurrence scale | as F, per member | as F. The recurrence time grows with the member (1.1); a statement on a window `t ≪ t_R` is a different claim (`papers/Main.md:139`, :536; `book/appendix-b-derivations.md:417`) |
| G-sub | conditional[finite `φ`-invariant stage; prior on each root's fibre; a non-permutation rooted map] | as F, on the stage | `papers/GR.md:587` (P; ledger B-QM-27, CD). RR context: the `(Z/N)^{2L}` subgroups (`continuous-substates/README.md:105–112`) |
| G-fact | conditional[the hypotheses of 1.2 G-fact; a non-permutation rooted map of the factor] | as stated | the matrix-level theorems below apply to the factor's rooted family. RR instance: the `p`-adic lowest-digit readout (`continuous-substates/README.md:113–121`) |
| I-deep | open | — | "P-indivisibility at the recurrence scale is proved on a finite representative, while for an infinite deep sector the readback lemma ... gives the weaker accessible-window property, conditional memory" (`papers/GR.md:138`; also :585; `papers/Substratum.md:268`) |
| I-qloc | open | — | none on `main` |
| I-meas | conditional[exact common visible return `Γ_L = I` (1.2); a real row-stochastic rooted family with a root-shared normalized prior; an earlier non-permutation `Γ_s`]. Without the return hypothesis: open | as stated | the matrix-level theorems need only row-stochastic rooted matrices and an identity return: `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`, census 34, current; "the matrix form ... assumes only that Γ_s is row-stochastic", `papers/Main.md:143`), `pIndivisible_of_visible_identity_return_nonperm` (`ObservableFactorRecurrence.lean:68`, census 120, kernel-only). Gap: "Neither module supplies a measurable, real row-stochastic rooted law or composes the measure-based identity with the P-indivisibility result" (`ObservableFactorRecurrence.lean:20–22`; `ObservableMeasureReturn.lean:17`). Continuous time: "Continuous-time P-indivisibility for general Hamiltonian flows is open" (`papers/Main.md:155`). RR context: on infinite reversible carriers with normalized invariant measures, rooted families that are P-divisible at every finite time, one of them with an order-1 C4 gap (`continuous-substates/infinite-xor-counterexample.md:25–27`; `continuous-substates/solenoid-countercontrol.md:41`) |
| I-nonorm | no statement possible | — | rooted maps undefined |

### 1.4 All-time rooted classification (`C_OI(V) = P_per(V)`)

Included because it is the finite-carrier result whose necessity half rests directly on recurrence,
and so it shows what a completion changes.

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | established (K) | finite `V` and `H`; one bijection; one root-shared prior | `finiteRootedRealizable_iff_pper` (`RootedClassificationAllTime.lean:192`, census 40, current); `papers/Main.md:638` |
| G-fam | established per member (each periodic) | as F | as F |
| G-sub, G-fact | [IR]: the kernel theorem applies to the stage or factor if it is itself a product `C_V × C_H'` with a root-shared prior. No source states the transfer | H-product on the stage or factor | the kernel statement needs `RootedRealization` on `V × H` (`RootedClassificationAllTime.lean:176–193`). GR:587's constraint surface correlates interior and exterior and uses fibre priors, so it is not of that form as stated |
| I-deep, I-qloc, I-meas | necessity half not inherited; open whether the realizable class is larger | — | the forward (necessity) direction is "`pper_of_finiteRootedRealizable`, resting on finiteness of `V × H` and reversibility" (`RootedClassificationAllTime.lean:182`); the visible period it asserts comes from the finite order of the microscopic permutation (:186–191). With `H` infinite, that step is unavailable. RR context: nonperiodic rooted families on infinite hidden carriers (`continuous-substates/infinite-xor-counterexample.md:21–25`; `solenoid-countercontrol.md:41`; `README.md:85–88`). [IR] context, from the review: the Bernoulli shift on `{0,1}^Z`, read at coordinate 0 with a root-shared product prior, gives `Γ_0 = I` and `Γ_t = J` for `t ≥ 1`, a nonperiodic realizable family |
| I-nonorm | no statement possible | — | — |

### 1.5 A.8 cycle typicality and the A.9 cycle-averaged Page curve

| Class | Status | Hyp. | Source |
|---|---|---|---|
| F | conditional[H-scramble; the full product energy shell on `B ∪ R`]. Refuted within the counted setting: for definite initial configurations at bipartitions aligned with the configuration coordinates, H-scramble fails for every bijection and "the theorem as stated has no instance". Open outside that setting | `B ∪ R` closed under `φ` as one shell; A.9 also H-decouple | `papers/GR.md:797–821` (the finite cycle decomposition is used at :807); no instance: :805, :813, :823 (P; ledger B-BH-3, DM NEG). Established for every bijection at aligned bipartitions: `S(ρ_R(t)) ≤ H(p_0)` (:823–827). Not given: an ensemble restatement (:827). Open: proper shells (:829); single-trajectory entropy (:839). A.9: :831–837 |
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
theorem" covers the F cells of 1.1–1.5. The others are in the table below. For the phase-locking
lemma, its dependence on A1 is not traced here.

| Result | Status in every class, at its stated scope | Source |
|---|---|---|
| Lemma 1 (finite visible resolution) | established (P; K conditional on finite modes). It bounds carrier 2, not carrier 1 | `papers/Main.md:46`; `Finiteness.lean:66`, :104 |
| Readback lemma; C4 content (accessible conditional memory) | established; uses only Lemma 1 (`papers/Main.md:60`). For I-deep it is the property the source carries there (`papers/GR.md:138`, :585) | `papers/Main.md:60`, :157 |
| `S ⟺ D ⟺ Q_fb` on every finite horizon | established (K in part); applies to finite visible laws whatever the carrier | `papers/Main.md:60`, :552; ledger B-QM-1 |
| Reverse finite realization | established at its scope: "every finite stochastic law, including every finite quantum record, has a finite reversible OI realization; bounded quantum instrument families are uniformly realizable to arbitrary finite accuracy". The dilations construct a finite hidden space; they do not assume one (`papers/Main.md:60`) | `papers/Main.md:80` item (3), :516–520, :596 |
| Phase-locking lemma under (G1)–(G4) | preserved unchanged; not re-traced here | `papers/Main.md:228–260` |
| Theorem 24(iii), finite decoupled enlargement | established (P); finite factors only; infinite form not established | `papers/Substratum.md:257–262`, :268 |
| Observer-relative finiteness reading | the cardinality of `S` is not fixed by the Definition and the axioms; accessible finiteness does not establish total finiteness | `papers/Main.md:60`; `papers/Substratum.md:54`, :92 |
| Deep-sector cardinality on `[0, nΔt]` | established (P). For I-deep it is exact, "given a normalized product prior on it, a locally finite coupling graph and well-defined dynamics ... in which each component's update depends on finitely many components" | `papers/GR.md:132–134`, :138 |

These hold at their stated scope in every class, and nothing in this inventory narrows them. They
carry the distinction between finite access and total finiteness: on a finite horizon the visible
data do not fix the size of the carrier beyond the causal cone (`papers/GR.md:138`).

### 1.7 Exactness and quantum carriers (context for the fixed-model test)

| Class | Status | Source |
|---|---|---|
| F | refuted within one fixed finite realization under the ordinary factorization interface: no fixed finite realization is exactly operationally equivalent to a qubit's full theory (factorization half proved; unboundedness imported from [55]) | `papers/Main.md:558`; ledger B-QM-8, J-3 |
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
- **One fixed model.** Yes. The class is excluded for exactness by `papers/Main.md:558` and by the
  target (#914 comment 6875046763).
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

  Neither is on `main` for the Z/q lattice update or for the three inventoried results. The G-fact
  form has an RR instance for the free 1-D `p`-adic map (`continuous-substates/README.md:113–121`).
  The quasilocal directed system (`papers/Main.md:588`) supplies embeddings of finite regions as
  algebras. Its finite regions are not invariant under the update, so it is neither link for
  recurrence (2.3).

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
    fixes the state on infinitely many sites. No native finite-access preparation of such global
    support has been sourced. Whether one is possible depends on interface and resource hypotheses
    that no source states, so finite access alone is not taken here as a no-go. Confinement to a finite invariant stage also makes the support of the prior finite. It is
    therefore a finiteness posit of A1's kind, placed on the support of the state rather than on
    `S`, and it does not weaken A1. Whether such a stage counts as a subsystem or as an accessible
    preparation under Gate A answers 3 and 4 is an owner question (§4, Q10). It also touches the
    confinement question of RO-1 (S-J), which this inventory does not decide (Q2).
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
    almost by construction and carries the access objection above, so r2 does not recommend it
    (§3).
  - G-fact: a finite dynamical factor of the fixed lattice model through which a finite-access
    readout factors. None is stated for the Z/q lattice update. [IR] If the reviewer's mixing reading
    (§3) holds, a nontrivial finite factor cannot exist there, because a finite factor would be a
    periodic factor of a mixing system.

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
  `referenceState`, read as the uniform product measure on configurations [IR]. That reading is a
  bridge of its own, separate from any invariance statement. No result on `main` uses these maps.
- **Encoding, resources, access.**
  - Encoding: finite regions as full matrix algebras, with complex matrix kinematics taken as given
    (#914 comment 6875046763, decision 4).
  - Resources: for operations, the added control operation and the phase intervention principle,
    both posited (1.7).
  - Access: finite regions.
- **One fixed model.** Yes, at the level of the algebra and the discrete dynamics.
- **First missing proof step.** Invariance of `referenceState` under `heisQ` for the OI update
  (`QuasilocalAlgebra.lean:1264`; the second-order rule is `ruleDynamics`, `SecondOrderDrive.lean:339`,
  cited at `papers/Main.md:724`). No source states it. Three statements are kept separate:
  - (i) invariance of Haar measure on the configuration group under the linear rule. This is a
    classical measure statement;
  - (ii) the bridge from that measure to the diagonal of `referenceState`, and invariance of
    `referenceState` itself under the implemented `heisQ`, off-diagonal elements included;
  - (iii) realization of the state and of the dynamics at the physical observer interface.

  (i) does not by itself give (ii) or (iii). [IR] One route to (ii): `referenceState ∘ heisQ` is
  again a tracial state, and the completion of full matrix algebras over finite regions is expected
  to carry a unique tracial state. This route is not checked here. Once invariance holds, the next questions are those of 1.2 under that
  state (§3).

### 2.6 I-meas: general infinite probability-preserving carriers, and continuous time

- **Stays established.** 1.6; the matrix-level P-indivisibility theorems as matrix statements
  (1.3). The set identity `changeEvent_eq_iUnion` and the measured-return equivalence are K for
  their statements (`ObservableFactorRecurrence.lean:48`; `ObservableMeasureReturn.lean:63`, :83;
  kernel-only).
- **Needs replacement.**
  - 1.1 and 1.2 as unconditional properties: not inherited. Main records the failure of near-total
    common visible return at late times for mixing Hamiltonian flows (`papers/Main.md:155`).
  - 1.3: conditional on 1.2's return hypothesis.
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
    open" (`continuous-substates/README.md:143–144`).
  - Separately, the formal composition from a measurable dynamics to a real row-stochastic rooted
    family (`ObservableFactorRecurrence.lean:20–22`).
  - For 1.5: the ensemble restatement of A.8 (`papers/GR.md:827`).

### 2.7 I-nonorm

No rooted law, no P-indivisibility statement and no cycle average is defined. Poincaré recurrence
needs a finite invariant measure (#1055 body, test cases). The class is outside every inventoried
result.

## 3. Smallest discriminating next obligation (recommendation)

**Recommendation, not a decision.**

**r1's OBL-RO3-1 is withdrawn as the recommendation.** It proposed proving that the spatially
periodic configurations of the lattice model form finite invariant sectors.
- Its main clause follows almost by construction from translation invariance (2.3), so its
  decision rule decides little.
- Its positive branch places the finite model on a global constraint, not a subsystem.
- Confining preparations to a sector makes the support of the state finite, a finiteness posit of
  A1's kind (2.3).
- It is not the missing link of G-fam for one model with one prior of full support (2.2).

It stays in 2.3 as an [IR] reading.

**OBL-RO3-2 (proposed): is the posited linear rule mixing under its uniform Haar measure?**

The argument below comes from the review and is unverified. The writer's paper reading found no gap
in it, which is not a verification.

1. **Setting.**
   - The rule: the posited linear rule, ledger item (vii) at `papers/Main.md:724`, in the
     second-order form `F(u, v) = (v, Av − u)` with `A = α Σ_j (T_j + T_j^{-1})`
     (`papers/SM.md:296`).
   - The carrier and field: the infinite lattice `Z^d`, over `Z/p` with `p` prime and `α ≢ 0 mod p`.
   - The kernel object for the second-order rule on the infinite lattice is `ruleDynamics`
     (`SecondOrderDrive.lean:339`).
   - The rounded bijection and every nonlinear rule are outside the obligation (`papers/SM.md:294`,
     :298).
2. **Statement to prove on paper, with the literature checked first.**
   - (a) `F` is a continuous automorphism of the compact abelian group `((Z/p)^2)^{Z^d}`, so it
     preserves Haar measure, the uniform product measure. This is the classical statement (i) of
     2.5. The bridge to the diagonal of `referenceState`, the invariance of `referenceState` under
     the implemented `heisQ`, and realization at the observer interface are separate obligations
     ((ii) and (iii) of 2.5). (a) does not discharge them.
   - (b) On the dual module, the free module of rank 2 over the Laurent ring `F_p[T_j^{±1}]`, the
     dual of `F` satisfies `t^2 − A t + 1 = 0`. Hence `det(F^n − I) = 2 − D_n(A)`, where `D_n` is the
     monic degree-`n` Dickson polynomial. This is nonzero because `A` is a nonconstant Laurent
     polynomial. So the dual action has no nontrivial finite orbit.
   - (c) By the Halmos criterion, `F` is ergodic for Haar measure. By Rokhlin's theorem for
     automorphisms of compact abelian groups, it is mixing.
   - (d) By the discrete-time reading of 1.2, no readout through finitely many sites, with cells of
     measure strictly between 0 and 1, has an exact common visible return at any positive time.
   - Literature to check before any proof is written: Halmos (1943) and Rokhlin (1949) on
     automorphisms of compact groups, and the standard treatments of algebraic `Z^d`-actions, for
     example Schmidt, *Dynamical Systems of Algebraic Origin*. AGENTS.md Step 4 requires this.
3. **Proposed decision rule.** This rule is proposed, not frozen. It authorizes nothing, and no
   expected outcome is fixed in advance.
   - If (a)–(d) are proved: record that under the uniform Haar measure on the fixed
     infinite-lattice model, the recurrence route to 1.3 is unavailable for the linear rule.
     Recurrence-based P-indivisibility there then needs a different proof, or stays scoped to finite
     representatives (Q3). Record also that G-fact has no nontrivial finite factor for this rule
     (2.3).
   - If (b) fails, because the dual action has a finite orbit: record the finite factor it gives.
     The G-fact route is then open for readouts through that factor, and 1.2 is tested there.
   - If (c) fails for another reason: record which step fails and leave 1.2 I-qloc open.
4. **Preservation controls.**
   - The finite results stay unchanged: the periodic configurations of 2.3 still carry the torus
     periods of `papers/SM.md:1606` and :296. They have Haar measure zero, so (d) does not contradict
     them.
   - SM's statements on the finite torus stay true: there the exact linear rule "is not ergodic on
     its energy shells", conserves further quadratic invariants, and splits its largest shell into
     many cycles (`papers/SM.md:294`, :296). Mixing on the infinite lattice under Haar measure, if
     proved, concerns a different carrier, on which these conserved sums of local densities are not
     functions. The proof must show that it does not contradict them. A proof that implies
     ergodicity on a finite torus is wrong.
   - No cell of §1 outside I-qloc and I-meas changes.
5. **Countercontrols the argument must respect.**
   - The `p`-adic free map: its readouts through a finite factor return exactly (RR,
     `continuous-substates/README.md:113–121`). The dual of `Z_p` has finite orbits, so step (b)
     must fail there.
   - The free map on the finite-dimensional torus `(R/Z)^{2L}`: difference readouts return exactly
     (RR, `continuous-substates/README.md:92–104`), and `F^L − I` is nilpotent there. Step (b) must
     fail there too.
   - An argument that gives mixing in either case is wrong.
6. **What it does not settle.**
   - The gauge-coupled multi-component rule; nonlinear rules; nonprime `q`.
   - Other normalized states, which the obligation does not select. The uniform state is examined
     because the interface already assumes it (`RegionTower.lean`, header item (3)), not because it
     reproduces quantum predictions.
   - Anything about operational quantum carriers (carrier 3).

**Why this one.**
- It decides, for the actual posited rule and its uniform Haar measure, whether the recurrence
  route survives on the completion. That is the crux of Q3.
- It settles the G-fact route for that rule as a byproduct.
- It needs no new premise and no choice of completion.
- If the literature step confirms (c), what remains is the algebra of (b), a paper-only unit with
  independent review.
- It largely tests a negative. If it holds, it narrows the completion candidates for the recurrence
  route rather than opening one.

**Secondary candidates.**
- Invariance of `referenceState` under `heisQ` for a general reversible finite-range update (2.5).
- The infinite form of Theorem 24(iii) for a decoupled normalized factor (2.4).
- The kernel composition from measurable dynamics to a real row-stochastic rooted family (2.6),
  which needs Lean.
- The ensemble restatement of A.8 (2.6).
- Two [IR] readings from the review:
  - `φ^L ≠ id` for the linear rule on finitely supported configurations (1.1 I-qloc);
  - the Bernoulli-shift realization (1.4).

## 4. Open owner questions

1. **Admissible completions.** Which of G-sub, G-fact, I-deep, I-qloc and I-meas may serve as
   EXACT's carrier class, or are all to be carried forward? The choice may not be made because a
   completion reproduces quantum predictions.
2. **Sector confinement and RO-1.** Is confinement of preparations to a finite invariant sector an
   admissible assumption to be stated, given that it is a support-level finiteness posit (2.3)? Does
   stating it fall under RO-1's specification of sector C, or is it separate? The RO-1 and #1143
   matters are not decided here.
3. **Which property must transfer.** On completions, must recurrence-scale P-indivisibility be a
   preserved control, which would need a replacement proof under a stated return hypothesis? Or may
   it remain scoped to finite representatives, with the readback lemma's accessible-window memory as
   the property carried to completions (`papers/Main.md:139`; `papers/GR.md:138`)?
4. **Accessibility.** For growing carriers the recurrence time grows (`papers/SM.md:296`). Is a
   recurrence-scale property required at all for EXACT, which concerns operational law-equality on
   performable experiments?
5. **A.8 and A.9.** Must the cycle-averaged Page curve be restated on a completion (the ensemble form
   of `papers/GR.md:827`), or does J-4 stay recorded as a finite-carrier statement? A.8 already has
   no instance in its counted setting.
6. **The prior on a completion.** Lemma 3's maximal-entropy selection is finite
   (`CanonicalMeasure.lean:54`, `[Fintype S]`). The existing candidate on I-qloc is `referenceState`
   (`QuasilocalAlgebra.lean:901`): it exists in the kernel, and its invariance under the update is
   not stated (2.5). Which normalized measure or state is the completion's prior, and by what
   criterion, other than quantum reproduction?
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
9. **§4.6.** #1055 names §4.6 (`papers/Main.md:758`) as the second consumer of A1. It is outside
   RO-3's stated scope and is not inventoried here. Is it to be covered by a later unit?
Q10–Q12 are decided (#914 comment 6883249235, `amaybaum`, 2026-11-14T19:48:13Z). Each decision is
quoted verbatim after its question. The owner adds: "These decisions do not select a completion or
establish EXACT."

10. **Sectors as subsystems.** Does a sector, a restriction of the state's support that needs a
    preparation over infinitely many sites, count as a "subsystem" under Gate A answer 3, and as an
    accessible preparation under answer 4 (#1169 comment 6876591512)?
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
    #1055, coordinating with #1029 for any later manuscript correction. Do not treat RO-3 as having
    resolved it."

## 5. Searches behind the negative statements

- **No recurrence or period statement for the quasilocal completion.**
  - Searched `recurr`, `period`, `orderOf` and `finite order` in `QuasilocalAlgebra.lean`,
    `QuasilocalCharacterization.lean`, `RegionLimit.lean` and `SecondOrderDrive.lean`.
  - Searched `recurren` in `verification/audits/operational/quasilocal-completion-audit.md` and
    `verification/audits/physical-realization/continuous-time-audit.md`.
  - No hits.
- **No invariance statement for `referenceState`.** Read `QuasilocalAlgebra.lean:880–910`, the
  `heisQ` definitions (:1264–1280) and the header of `RegionTower.lean`. The kernel establishes
  that the state exists, its stage values, and the invariance of the uniform family under local
  unitaries at finite stages. Invariance under the update is not stated there.
- **No finite invariant stage or finite factor for the Z/q lattice update on `Z^d`.**
  - r1 searched `papers/`, `book/` and `verification/` for "periodic configurations",
    "translation-periodic", "invariant sector", "finite invariant subset", "invariant
    representative", "periodic boundary" and "torus". r2 adds "invariant subgroup" and "factor".
  - Hits on `main`:
    - `papers/GR.md:587` (a constraint surface);
    - the finite subgroups `(Z/N)^{2L}` of the free 1-D torus map and the `p`-adic factors
      `Z_p → Z/p^k` (`continuous-substates/README.md:105–137`, RR).
  - Neither RR hit concerns the Z/q lattice update on `Z^d`. The torus appears in the papers as the
    finite model itself (`papers/SM.md:294–296`), not as a sector of an infinite one.
- **No A.8 counterpart on a completion.** `papers/GR.md:797–861` and ledger §8, §9.
- These searches are bounded by the phrases listed. A paraphrase outside them could have been
  missed. r1's list missed the RR hits above.

## 6. Off-`main` references (AGENTS.md §A.42 item 8)

This inventory is not a record landing on `main`. The trace is given so that a later landing can
check it.

| Reference | Use here | Classification |
|---|---|---|
| Ledger r8 on `records/unified-ledger-914-20261114` at `9ff3b8d9` | cross-reference to B-QM-1, B-QM-4, B-QM-5, B-QM-8, B-QM-9, B-QM-27, B-BH-3, J-3, J-4, M2, M5, §8.4, §8.5 | provenance for the row identifiers. Every status above is traced to a source on `main`; in r2 the 1.7 cell that cited only ledger items also cites `papers/Main.md:556`, :588. The one ledger reading quoted as a reading (§8.5, the source of A.8's failure) is attributed to the ledger and to `papers/GR.md:813`, :823 on `main` |
| Ledger r9 at `4470bd02` | checked only for changes to the cited rows | provenance |
| #914 comment 6880700869 | the owner's acceptance of r8 | governance |
| #1055 comments 6881390849, 6880024537; #1055 body | authorization, scope, controls, test cases | governance; supports no scientific claim |
| #1169 comments 6880022363, 6877981234, 6876591512; #914 comment 6875046763 | target and EXACT's wording | governance; supports no scientific claim |
| #1007 body; #872 body | carrier foundations; completion sub-obligation | context; supports no scientific claim |
| `REVIEW-r1.md` at `0d6d8812` | findings and the reviewer readings marked [IR] | review record; supports no claim |
| #914 comment 6883249235; PR #1303 review 5906337933 | the owner's Q10–Q12 decisions and r3 authorization; the r2 review's nits N1–N3 | governance and review record; support no scientific claim |
| #1009 and its branch | not used | — |

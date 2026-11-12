# TUNE-1, Step 2 proposal: derived-access coherent qubit operations

**WIP / UNVERIFIED drafting record. A proposal for owner approval; not executed.** Research unit
under Issue #1236 (owner decision: paper-only). This file plans one question and fixes, before any
work, its definitions, decision rule, controls and stopping rule. It runs no Step 2 work, performs
no computation, adopts no premise, advocates and evaluates no candidate mechanism, changes no
manuscript or Lean file and authorizes nothing. Execution needs the owner's recorded approval of
this text (or of an amended text) after the reviews named in section 10. This is revision r10a,
which applies the nine nits of the delta review of r10 (verdict ACCEPT WITH NITS, at `4b6b4460`)
to r10; r10 was
drafted after the delta review of r9 (verdict REVISE, light, one blocking finding, at `80a012b2`);
r9 was drafted after the external re-review of r8a (verdict REVISE, one blocking finding, at
`7a9e7b79`); r8a applied the four nits of the delta review of r8 (verdict ACCEPT WITH NITS, at `535688ca`) to
r8; r8 was drafted after the delta review of r7 (verdict REVISE, light, at `2ad0aca0`); r7 was drafted after
the delta review of r6 (verdict REVISE, at `b9e9683e`); each was drafted with the owner's approval
to revise as reviewed; r6 was drafted after the external review of r5a (verdict REVISE, at
`9440f8af`); r5a applied the four nits of the delta review of r5 (verdict
ACCEPT WITH NITS, at `c3a0ebf7`) to r5; r5 was drafted after the delta review of r4 (verdict REVISE, light, at `57783cbc`); r4 followed the delta
review of r3 (verdict REVISE, light, at `b47700a6`), r3 that of r2 (verdict REVISE, at `81f50bd0`),
and r2 the first internal review (verdict REVISE, at `9312b805`). The dispositions of these
reviews are kept outside this file.

**Base.** Branch `research/tune-1-20261111`, drafted on head `d3d12426` (TUNE-1-STEP1.md r5a, the
reviewed Step 1 head, unchanged here). The branch descends from the Step 1 pin
`cac5d26441dd33e9348151487e4df7b547195481`, and every line number below is a line number at that
pin; as Step 1 records, each cited line of `papers/Main.md` is two lower at `082c3eaa`.

**Labels.** As in Step 1: **[K]** a Lean statement under `verification/lean-mathlib/OIBridge/`
("OB/" below), statement read, nothing built; **[P]** a manuscript statement on `main`
(**[P-imp]** with an imported half); **[R]** a research record on `main` that states it is not
independently reviewed; **[W]** this writer's own short argument, unreviewed and not
kernel-checked. A [W] step that extends a [K] statement beyond its scope is tagged [W], never [K].
"Step 1" means `TUNE-1-STEP1.md` in this directory, with its section labels (B.12, C, D1–D12,
F.1, F.2).

***

## 0. Plain-language summary

Step 1 found that wherever `main` gets quantum-like behaviour from a world that only reshuffles
its configurations, someone chose by hand what the observer may prepare and read. Can that
hand-choice be removed?

Take one lattice rule and fix once a region as the observer's apparatus. The observer reads
everything in the region at every step, nothing outside it, and chooses only settings, stored at
the start in unread cells or (an assumption) rewritten each round. Does what it can do and see behave like one quantum bit, to any wanted
precision, over experiments of any length? That means finely adjustable reversible operations
that compose, two incompatible measurements, every qubit state, and outcome statistics
produced by the dynamics from a declared random state of the unobserved world (an assumption,
not derived).

It counts only if one apparatus serves every setting and nothing quantum is put in, as apparatus
or settings; the owner
decides how a programmed quantum simulator is classed. Controls give the test teeth: models with
hand-chosen access or a stored quantum answer must be classed "supplied"; a classical random walk
must fail, for a reason that does not rule out every hidden-variable model.

For the linear rule, a lemma on `main` may settle it, probably negatively, if a gap in that
argument closes; the nonlinear rule is the open case, studied only under a named hypothesis. The
owner chooses the rule and the random state.

Outcomes: pass; fail, for a stated class only; inconclusive; or void, if a control fails. A pass
would show only that this follows from the chosen rule and stated assumptions (for the
nonlinear rule: OI's posits, the linear rule replaced by named hypothesis H-nl); it would not be
evidence that OI is correct, nor establish the Born rule. Paper work only; nothing adopted.

***

## 1. The question

### 1.1 Rule and carrier: what "a single fixed OI dynamics" means

**Alphabet and phase space.** Fix an integer `q ≥ 2` and `V = ℤ/qℤ`. For a set of sites `Λ` the
phase space is `X_Λ = (V × V)^Λ`, a pair (previous value, current value) at each site.

**Rule class 𝓡.** One step is the second-order update

> `Φ_F : (y, x) ↦ (x, F(x) − y)`,

the form of Main:726 item (xiii), "a posit of the selected lattice model, not derived and not an
axiom of OI", already in the posit ledger [P]; its kernel form is `ruleDynamics`
(OB/SecondOrderDrive.lean:339) [K]. Using it adds no premise. Two members are named; the owner
chooses which enter (section 9, choice 1).

- **R-lin** (reference). `F` is the nearest-neighbour sum on the simple cubic lattice, the
  instance of Main §3.2 at `q = 2` (Main:726 item (xiii)) and the exact rule of SM:296 with
  `α = 1` at general `q`. It is linear (item (vii)), translation-invariant, of range one (item (ix)), on a
  site-factorized configuration space (item (viii)). One fixed `F`; no class of couplings is
  quantified over, so no coupling can be fitted.
- **R-nl** (owner option only). The rounded bijection of SM:294,
  `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on the representatives `0, …, q−1`. It has the
  second-order form, so it is a bijection [W: `(x, z) ↦ (g(x) − z, x)` inverts it], but it is not
  linear and so is not covered by ledger item (vii); SM:298 and SM:1416 call it a separate
  realization. What `main` states about it [P]: SM §4.2 introduces it to test numerically whether
  rounding breaks the linear rule's integrability, as full-shell sampling needs (SM:294); it
  "behaves chaotically at the sizes measured" on three numerical diagnostics, and no nonconstant
  polynomial invariant of degree at most two was found in the computed instances (SM:292, :294);
  away from alphabet-boundary crossings its floor differs from the real linear update by at most
  1/3 per site and step, and a crossing can change that by order `q/3` (SM:298); "numerical chaos
  of the rounded rule supplies neither that sampling nor its identification with the normalized
  observer-level operator" (SM:298); it "does not inherit A5 or exact amplitude-scale invariance"
  (SM:1416). In Main it appears only in ledger item (v), as the source of numerical motivation for
  the hidden-sector mixing hypothesis: "numerical motivation comes from the rounded candidate of
  [SM §4.2]" (Main:726). It is therefore a candidate realization, not a ledger posit: it meets the
  second-order form of item (xiii) and items (viii), (x) and (xi) [W], and it does not meet item
  (vii). It enters only under the named hypothesis **H-nl** ("the world's rule is R-nl"), which
  replaces item (vii) for that subclass, is carried into every conclusion that uses it, and is not
  adopted (Issue #1236; adopting it as a premise would be a Layer-0 revision, section 6). SM's
  chaos diagnostics are numerical evidence and are not premises of any Step 2 derivation (§A.46
  item 7; Code Review Rules, "Exactness and controls"). No record read for this proposal states
  anything about R-nl's record laws through a region or about its computational capacity
  (section 10 lists the reading).

**Excluded from 𝓡**, because Step 1 shows each is unsourced (Step 1 B.12, row
`two-mode-drive.md`; section C, B1 row): real-valued sites (E-real), an isolated pair (E-pair),
an externally loaded or switched coefficient (E-control), and any carrier added to the lattice
(per-site continua, `p`-adic or recursive substates, a continuum sphere). Recursive structure
enters only as structure of the fixed rule acting on the lattice, for example nested or
multi-scale apparatus regions (section 1.2); it does not enter as an added carrier.

**Carrier class 𝓛.**

- `𝓛_fin`: the tori `Λ_L = (ℤ/Lℤ)^3`, `L ≥ 1`. The world is finite for each `L`; `L` is a
  resource and may grow with the requested precision and horizon. This stays inside the
  manuscripts' finite construction (Main:726 item (ii)).
- `𝓛_∞`: the lattice `ℤ^3` with the finite alphabet `V`, the setting of the kernel's quasilocal
  interface (Step 1 B.12). It enters only under a named hypothesis **H-∞** ("the world is the
  infinite lattice"), carried into every conclusion that uses it. H-∞ is not adopted (Issue #1236:
  no new physical premise; Step 1 B.0).

**The alphabet is fixed.** `q` is fixed for each verdict; statements are made for each fixed `q`.
A family in growing `q` needs a correspondence between alphabets that SM §2.7 states "is not
constructed here" (SM:94) and is not part of this question.

### 1.2 The embedded apparatus

An **interface** is `I = (Λ, O, C, τ, r_O, μ)`, and, in initial-condition mode, the layout `(P_j)`
of its program blocks (below):

- `Λ ∈ 𝓛`, the world;
- `O ⊂ Λ`, a finite **observer region**, and `C ⊆ O`, its **control cells**;
- `τ ≥ 1`, the duration of one **round**, in ticks, the same for every label;
- `r_O ∈ (V × V)^O`, a fixed **ready configuration** of `O`;
- `μ`, the law of the configuration of `Λ ∖ O` (in initial-condition mode, of `Λ ∖ (O ∪ P)`) at
  time zero, independent of everything the observer does (hypothesis **H-μ**, section 1.3, D3).

**Labels.** A label is a configuration `c ∈ (V × V)^C`. The menu is every configuration of `C`;
no label is selected or excluded. The **label encoder** of a family is the whole of the rules by
which the submitted proofs of the Q-conditions assign labels to targets: the gate map
`θ ↦ c(θ)` of Q3, the labels of Q5's two reads, and the preparation prefixes of Q1 and Q6 with
their heralds and any continuation a proof names. In initial-condition mode the labels it assigns are the initial content of the
program blocks `P_j` (below), and it covers the content of every block. It names labels of the
menu and removes none from it; D6(b) tests it (section 1.3).

**Rounds and protocols (exchange mode).** At the start of round `j` the label register `R_lab`,
which holds one configuration of `C`, is reset to the label `c_j`, and its content is exchanged
with the content of `C`. Then `Φ_F` runs `τ` ticks on the whole world, unchanged. The register,
its reset and the exchange are part of the apparatus. They are a classical write access to `C`
that `Φ_F` does not supply, assumed as the named hypothesis **H-write** (classical write access)
and carried into every conclusion obtained in exchange mode. `obs_exchangesAvailable`
(OB/SubstratumInterfaceAudit.lean:816) [K] states that exchanges of configurations are available
in the observer theory `obsTheory 𝒮`. That theory is `permTheory` on the configuration space
(`obsTheory_eq_permTheory`, :775), the theory of an observer "with read and write access to its
visible configurations" (:9), and it is the same for every rule on the same sites and alphabet
(`obsTheory_rule_independent`, :780) [K]. The availability therefore comes from the chosen access
architecture and not from `F`. It does not show that a locally acting controller, its register or
per-round writes follow from R-lin or R-nl, and it is not used as warrant for them. The record of the round is the **complete history of `O`**:
its configuration at each of the `τ` ticks, `h_j ∈ ((V × V)^O)^τ`, together with `c_j`. The
content the exchange moves into `R_lab` is the configuration of `C` at the last tick of round
`j − 1`, part of `h_{j−1}` (for `j = 1`, the restriction of `r_O`), so the reset erases nothing that
is not recorded; `c_j` is a function of the earlier records and adds nothing to the record law.
A **protocol of horizon `K`**
is a policy that chooses `c_1, …, c_K`, each `c_j` a function of `h_1, …, h_{j−1}` (adaptive), and
may declare a **herald**, an event on the records on which the run is accepted, with its raw
acceptance probability `p_acc > 0` reported and no renormalization of rejected runs
(`observation-context-protocol.md`:45 [R]). A herald of probability zero defines no conditional
state and is not admitted. The distance `d_K` of section 1.4 compares joint
laws, so it controls a law conditional on a herald only to within `2 d_K / p_acc` [W]. Every
condition stated on heralded preparations (Q1, Q5, Q6) is therefore required at *conditional*
error `ε`, which holds when `2 d_K / p_acc ≤ ε`, and the `p_acc` of each heralded preparation used
is reported. `Π_K(I)` is the set of such protocols. The **record
law** `P^I_π` is the law of `(h_1, …, h_K)` under `μ`, the ready configuration and the dynamics.

**Initial-condition mode** (owner option, section 9, choice 5): the labels of a non-adaptive
protocol are written at time zero into disjoint **program blocks** `P_1, P_2, … ⊂ Λ ∖ O`, each the
image of `C` under a translation fixed by the layout, through which a label `c ∈ (V × V)^C` is
placed in `P_j`; the layout is fixed by a rule that is part of the generating rule (D1) and depends
on neither the labels nor the protocol, and nothing is written afterwards. At `I_n` the generating
rule lays out `K_n` blocks, with `K_n ≥ K` whenever `n = n(ε, K)`, and `P = P_1 ∪ ⋯ ∪ P_{K_n}` is
the same for every protocol; a protocol assigns a label to every block, and one of horizon
`K ≤ K_n` is compared on its first `K` rounds.
The blocks lie outside `O` and so are not read (D4); a label reaches `O` only through `Φ_F`. In
this mode `μ` is the law of the configuration of `Λ ∖ (O ∪ P)`, and the record
law is the law of `(h_1, …, h_K)` for the given label sequence. Every observer choice is then an
initial condition, as in Main's program register (Main:582); there is no label register, and the
only dynamics after time zero is `Φ_F`, under which the blocks evolve like every other cell: their
content is part of the declared initial condition, not a write. It is chosen through the labels,
and D6(b) tests it as it tests the ready configuration (section 1.3). This mode does not use H-write and
is the strictly rule-only target; its protocols are non-adaptive and may declare heralds as above.
Blocks inside `O` are excluded because the definitions alone would then fail every rule [W]: `O` is
read at every tick and `Φ_F` copies each cell's current value into its previous-value component,
so the first round's record would contain the current component of every later label, while the
comparator's round-1 record law depends on `c_1` alone; two protocols whose labels `c_K` differ in
the current component of one cell, and in nothing else, would give round-1 records at
total variation 1 and equal round-1 comparator laws, so Q2 would fail at every `ε < 1/2` for every
`K ≥ 2`, whatever the rule. With the blocks outside `O`, range one lets a layout place `P_j` at
graph distance greater than `(j − 1)τ` from `O` (the least distance between a cell of `P_j` and a
cell of `O` in the cubic lattice of `Λ`), so that no record before round `j` depends on `c_j`;
whether the later records carry the action that Q2–Q6 require is a property of `Φ_F` and `μ` [W].

**Family.** A family is `{I_n}_{n ∈ ℕ}` produced by one generating rule `n ↦ I_n` (for example the
`n`-fold scaling of a fixed pattern of `O` and `C`), stated in full as part of the family's
specification and a function of `n` alone (D1).
The resource of `I_n` is `N(I_n) = |Λ_n|` on `𝓛_fin`, which counts the program blocks, and on
`𝓛_∞` the number of sites of
`O_n ∪ P` plus those of its light cone over the protocol's duration (`P` empty in exchange mode),
finite by the range bound. `N` counts sites. Generating the labels is work done outside the
lattice and is not in `N`: a full resource claim states beside `N` the **label-generation cost**
`G(ε, K)`, which is the number of label cells written (`K|C|` in exchange mode, `K_n|C|` in
initial-condition mode) together with the cost, in a stated measure, of computing the label
encoder's labels from the targets; where a label is shown only to exist, that is stated in place
of the second figure.

### 1.3 Derived versus supplied: the criterion

A family is **derived** iff it satisfies D1–D7. It is **supplied** iff it fails at least one.
Each clause is stated so that a reader can check it from the construction as submitted: the
specification of the family and, for D6(b), the proofs of the Q-conditions submitted with it,
which state the label encoder (section 1.2), read with the proofs of the capacity statements they
rest on (D6(b)).

- **D1 (one interface for all targets).** The generating rule `n ↦ I_n` is part of the family's
  specification and is a function of `n` alone: its statement takes no target operation,
  requested angle, protocol, outcome, record statistic or comparator model as an argument. For
  each `n` one `I_n` serves every label, every protocol of `Π_K` and every target. Only `n` may
  depend on the requested `(ε, K)`, through the stated function `n(ε, K)`.
- **D2 (embedding).** The only dynamics is `Φ_F` with `F` from 𝓡 on the whole world. The observer
  acts only by the label exchanges of section 1.2, through the register and write access of H-write
  (or by the initial content of the program blocks, in initial-condition mode). No coefficient is loaded, no step is switched off or replaced, no
  region is isolated, and the round duration `τ` is the same for every label and every
  configuration.
- **D3 (ensemble).** `μ` is given by one generating prescription for the whole family, stated in
  its specification and the same for every `n`, which assigns to each `I_n` a law `μ_n` on the
  configurations of `Λ_n ∖ O_n`, or of `Λ_n ∖ (O_n ∪ P)` in initial-condition mode (the sample
  spaces change with `n`); the prescription is taken
  from the list the owner fixes at M0 (section 9, choice 6), and "law" below means such a
  prescription. The list
  as drafted: the uniform law on `(V × V)^{Λ∖O}` (on `ℤ^3`, the uniform product law); the
  level-set law, on `𝓛_fin` only: the conditional, given `O = r_O`, of the uniform law on the level
  set `{E = e}` in `X_{Λ_L}` of the conserved quantity `E(u, v)` of SM:296, with the level value
  `e ∈ ℤ/qℤ` fixed once in the specification, the same for every `L`, and defined when the event
  `{E = e, O = r_O}` is non-empty (on `ℤ^3`, choice 6 states what replaces it, or that its row is
  not defined); a translation- and `O_h`-invariant product law with a non-uniform site marginal.
  A family for which the event `{E = e, O = r_O}` is empty at some `n` has no admissible level-set law.
  The level-set law is not offered in initial-condition mode: conditioned also on the
  configuration of `P`, the law of `Λ ∖ (O ∪ P)` would depend on the label sequence, contrary to
  the independence clause of H-μ, and the labels would act on the unread world other than through
  `Φ_F`; choice 6 (iii) states what replaces it there. Which of
  them a pass must hold under is choice 6. Requiring the uniform law is not part of the owner's
  question, and by the expectation recorded in M3, with the gap recorded there closed, that
  requirement alone decides R-lin. The stated
  architecture fixes no ensemble (stochastic observer-interface audit,
  `verification/audits/operational/stochastic-observer-interface-audit.md`:369–381; Step 1 B.12
  (ix)), so H-μ is a named hypothesis and every conclusion carries it. Main's posit ledger item
  (iv) posits a maximal-entropy measure selection ("the maximal-entropy invariant measure
  compatible with the observer's records", Main:726) [P]; reading it as selecting the uniform law
  on the unprepared part is [W] and is not used as a premise (`measurement-source.md`:148 [R]
  reads Main's selection premise as selecting the global counting measure). Robustness
  requirement: a result counts as derived only if it is also stated under one second law `μ′` of
  the list with the same symmetries (choice 6); if it holds under `μ` and fails under `μ′`, the
  verdict records the measure as supplied (Step 1 F.1, control 2).
- **D4 (readout).** The observer's record is the complete history of `O`. No pointer function,
  response function, threshold or decoder is chosen. Outcome probabilities are the pushforward of
  `μ` through the dynamics; this is the **derived readout rule** the owner requires, and nothing
  else is called a readout rule. The two-class coarse-grainings of Q5 test a property of the
  comparator `𝔔`; they are not a readout rule and do not change `d_K`, which compares complete
  records.
- **D5 (no access by declaration).** Every protocol of `Π_K(I)` is admitted. No read, label or
  herald is declared unavailable. Information is inaccessible only if it lies outside `O` when it
  would be read. A restriction that is not a consequence of D1–D4 makes the family supplied.
- **D6 (no quantum input).** Under choice 11(a) or (b), D6 consists of the two tests (a) and (b),
  and failing either makes the family supplied; under 11(b), a family that meets Q0–Q6 for every
  `(ε, K)` and fails D6(b) and no other D-clause (D7 included) is classified `PASS-COMPILED`
  (section 2.1). Under choice 11(c), D6 consists of test (a) alone, and test (b) is not applied.
  - *(a) Vocabulary.* The specification of the family uses no quantum object or target quantity:
    no amplitude, density matrix, unitary, Kraus operator, Born weight, rotation, cosine or sine,
    orthogonal-matrix dynamics, or operational-control predicate (the boundary frozen in the
    pair-flow equivalence audit, quoted in Step 1 F.1, control 12). These words occur only in the
    comparator (section 1.4).
  - *(b) Compilation.* None of `r_O`, the shapes of `O` and `C`, `τ`, `μ`, the generating rule or
    the label encoder (section 1.2)
    is defined as the encoding into configurations of a program, table or data stream that
    computes a **D6 quantity** (an amplitude, a rotation angle's cosine or sine, a Born weight, or
    a matrix entry of a density operator, unitary or instrument), or that samples from a law
    defined by one (a Born law, a cosine law, the sphere model's hemisphere law). The test is
    applied to how each item is defined, including how a configuration given explicitly was
    obtained, and to every submitted proof of a Q-condition: if any one of
    them identifies the configurations of some set of cells, label cells and program blocks
    included, with numerals or tables of a D6
    quantity, and the dynamics with an algorithm acting on them, the family fails (b), whatever its
    bit pattern contains (the identification test). It can also fail (b) through a proof step that
    rests on a **capacity statement**: a statement about `Φ_F`, cited, assumed or proved in the submission
    and whatever verb it uses, that the dynamics executes, interprets, simulates or reproduces
    another system (a machine, a controller, a circuit, another dynamics), or that for each
    member of a class of systems, record laws, channels or instruments some configuration makes
    it do so. The family fails if by that statement or by its proof an item encodes the system's
    program or table (for a class, those of the member the proof step instantiates; *Encoding*
    below), and the system's own specification has a hit under the word list of (a) or computes
    or samples as above (the capacity-statement test). The proof of a capacity statement is
    read, for this test and for the identification test, as a submitted proof is; if it is not
    in the submitted text or at a cited file and line, the D6 row is not `proved`. A submitted
    proof stays part of the record, so withdrawing it does not change the family's
    classification. The test is not failed because the rule could compute, nor by a proof that
    obtains the record law from the structure of the dynamics without such an identification or
    encoding.
    It is aimed at Main's single controlled dynamics, in which "Quantum mechanics enters as the
    instrument data and as the state held in the hidden register" (Main:582) [P], compiled into
    the apparatus region, the labels or the program blocks; the protocol table of its "read-only
    program register" holds the protocol's choices of instrument, which are `parameter` labels.
    It is exercised by controls C-PROG and C-PROG-P.
    - *Encoding.* A statement or proof makes an item encode a system when it contains both of
      the following, found by reading it, and takes the agreement with the target through them
      (the deciding question below). (i) A **code**: a correspondence, in either direction
      and exhibited or only shown to exist, between configurations of the item and descriptions
      of systems (a program, a transition table, a circuit, a table of matrix entries, weights
      or probabilities), where a description fixes its system's behaviour without reference to
      `Φ_F`. (ii) A **simulation step**: a statement that on a configuration that corresponds to
      a description the dynamics does what is described (executes the program, looks up the
      table, reproduces the described system), from which the proof takes the item's action.
      The item then encodes every system whose description the proof puts through the code. A
      numeral or index of the target's parameter is not a description in this sense. Nor is an
      operation of the comparator `𝔔` (an instrument it assigns to a label, or a composition of
      such instruments): a step that bounds the distance between an action or record law that
      the proof derives from `Φ_F`, `r_O` and `μ` and such an operation, or between two such
      operations, is the comparison and not a simulation step, whether it is made for one label,
      for finitely many generating labels or for a configuration built from them. A table,
      numeral or program that holds a comparator operation in cells is a description, and the
      identification test applies to it. What
      decides is where the proof takes the agreement with the target from: from the behaviour of
      a described system, fixed by its description, or from the record law that it derives for
      the item's configuration from `Φ_F`, `r_O` and `μ` and compares with the comparator's. In
      the second case nothing is encoded; a proof that does both makes the item encode the
      described systems, each tested by its own specification. A proof of the second kind may
      show by any means (continuity,
      counting, density, inverting a derived map from labels to actions) that a label with the
      required action exists, and its conclusion may have the form of a capacity statement, as
      Q3 has: no statement is a hit by its form, the correspondence between targets and labels
      that a Q-condition states is not by that fact a code, and such a label is `selected`
      (below). A statement that a proof cites for the agreement is followed into its own proof
      until one of the two cases is reached. A quotient, factor or marginal of `Φ_F` on the
      interface under `μ` is defined from them and is not another system; a step that equates
      one with a system specified without `Φ_F` is a capacity statement. The ledger entries do
      not depend on where a program is held, on whether a configuration is exhibited or shown to
      exist, on whether a step is written out or cited, or on the verbs used. A cited step whose
      proof is not available leaves the entry `unclassified` and the row not `proved`; a hit
      that the statement alone gives stands.
    - *Source ledger.* The D6 row of a family (section 3) carries a source ledger. For each of
      `r_O`, `O`, `C`, `τ`, `μ`, the generating rule and each component of the label encoder (the
      gate map `c(θ)`, each of Q5's two labels, each preparation prefix with its herald, each
      continuation a proof names, and in
      initial-condition mode the initial content of the program blocks) it records how the item
      is defined, every capacity statement that a proof using the item rests on (the Q-condition
      being proved is not entered), and every system that such a statement or its proof makes
      the item encode, with the word-list search of that system's specification, quoted or cited
      at file and line. An item whose entry cannot be read from the
      submitted text leaves the D6 row not `proved` (section 2.2, step 2).
    - *Settings and programs.* For each component of the label encoder the ledger also records
      what the label holds, read from its definition, from the proofs that use it and from the
      capacity statements they rest on, with their proofs, as one of
      three classes. `parameter`: a numeral or index of the target's parameter itself (the angle
      `θ`; the direction or index of a read or of a preparation), not of a D6 quantity computed
      from it, in a notation that is the same for
      every target, and nothing else. `selected`: a configuration chosen by its action as the proofs derive that
      action from `Φ_F`, `r_O` and `μ`, explicitly or by an existence argument, where no
      statement or proof makes the label encode a system (*Encoding* above). `content`:
      anything that a definition, a submitted proof, or a capacity statement or its proof gives
      as instructions, a table, a data stream, a sampler or the encoding of another system,
      whether the label is exhibited or only shown to exist. Where more than one class applies,
      `content` is entered before the other two, and `parameter` before `selected`. A label
      that fits none of the three classes, or whose class cannot be read from the submitted text
      and the proofs read with it, is entered as `unclassified` and, where (b) is applied,
      leaves the D6 row not `proved`; `selected` is not a default. A component whose labels fall
      in different classes takes `content` if any label does, otherwise `unclassified` if any
      does, otherwise `selected`. A `parameter` or `selected` label is a device setting and is
      not a hit by its class; the identification test and the capacity-statement test above
      apply to it as to any cells. A
      `content` label is a hit exactly when what it holds is a program, table or data stream that
      computes or samples as above, or encodes a system whose specification does so or has a hit
      under the word list of (a). That is the test applied to `r_O`, so a program that fails (b)
      in `r_O` fails it when it is placed in the labels or in the program blocks instead: moving
      it does not change the outcome of (b), and so, where (b) is applied (choice 11(a) or (b)),
      cannot make a supplied family derived (section 2.1). Nor does dividing it: a program,
      table, data stream or code that a definition or proof spreads over several items (`r_O`,
      the generating rule and its layout, the labels, the program blocks) is tested as one, and
      each item that holds part of it takes the entry the whole would have in a single item.
      Two things are not hits: that a
      label depends on the target, as every encoder's labels do; and that the correspondence
      between targets and labels is stated with the comparator's quantities, as Q3 states it.
      Neither exempts a label from the capacity-statement test: an encoder that states only that
      a label with the target's record law exists is classed by the ground its proofs give for
      that existence.
      The encoder belongs to the proofs of the Q-conditions and is not part of the specification
      searched under (a).
    - *A rule that interprets.* That `F` can compute, universally or otherwise, is not a hit,
      and D7 does not test it: D7 fixes the rule class, not what a rule in it can compute. A
      ready configuration from which
      `Φ_F` executes a program delivered elsewhere (an interpreter) is not a hit either, whether
      the proofs derive it from `F` or its definition gives it, provided it holds no program,
      table or data stream that computes or samples as above; the hit is in the item that holds
      the delivered program. A family whose labels or program blocks deliver a qubit simulator
      to such a rule therefore has the D6(b) entries of C-PROG-P in every presentation whose
      proofs are available, and one
      that holds the simulator in `r_O` has those of C-PROG. If such a family meets Q0–Q6 for
      every `(ε, K)` and D1, D3, D4, D5 and D6(a), then D2, D7 and choice 11 fix its token. Where it
      also meets D2 and D7 (so `F ∈ 𝓡`): `OPERATIONAL-ONLY` under 11(a), `PASS-COMPILED` under
      11(b), and `PASS-DERIVED` under 11(c), where test (b) is not applied. For `F ∉ 𝓡`:
      `OPERATIONAL-ONLY` under every option, since D2 and D7 fail. A family on a rule of 𝓡 that
      fails D2 or D7 for another reason is `OPERATIONAL-ONLY` likewise. No control exercises the
      entries for `F ∈ 𝓡`: no rule of 𝓡 is known to interpret (section 1.1). That a compilation of the
      target would also exist for a rule does not make a hit of a family whose definitions and
      proofs encode nothing.
- **D7 (rule class).** `F ∈ 𝓡` as fixed by the owner; `Λ ∈ 𝓛`; none of E-real, E-pair,
  E-control or an added carrier.

The criterion is aimed at the two ways the answer has been supplied on `main`: a per-target choice
of access, measure or decoder (D1, D3, D4, D5), and the quantum rule placed in the hidden state
or in the settings, by declaration or by compilation (D6), as in Main's realization theorems, where "Quantum
mechanics enters as the instrument data and as the state held in the hidden register" (Main:582)
[P].

### 1.4 The operational target: what "approximately coherent two-state operations" means

**Comparator.** A **qubit model** `𝔔 = (ρ₀, {𝓘_c})` is a density operator `ρ₀` on `ℂ²` and, for
each label `c`, an instrument `𝓘_c = {𝓘_{c,h}}_h` on `ℂ²` with outcome set the round records `h`.
For a protocol `π`, `P^𝔔_π(h_1, …, h_K) = Tr(𝓘_{c_K,h_K} ∘ ⋯ ∘ 𝓘_{c_1,h_1}(ρ₀))`, with the
labels chosen by the same policy and the same herald. The model is fixed for all protocols at a
given `n`: it is chosen once, not per protocol, setting or outcome (`endpoints.md`:67 [R]).

**Distance.** `d_K(I, 𝔔) = sup_{π ∈ Π_K(I)} TV(P^I_π, P^𝔔_π)`: total variation on complete
multi-time records, over every adaptive protocol of horizon at most `K`. Later reads in the same
protocol test every outgoing state, so no separate state distance is needed. A diamond-norm
bound on the comparator side converts to this distance by Main's telescoping Lemma (Main:596)
[P].

**Operational conditions** at error `ε` and horizon `K`, for one interface `I`:

- **Q0 (resources).** `N(I) ≤ N(ε, K)` for an explicit function `N`, finite at every `(ε, K)`.
  The count includes the program blocks; the label-generation cost `G(ε, K)` is reported beside
  it and is not a condition (section 1.2).
- **Q1 (two-state capacity; model-free).** Some two preparations (protocol prefixes, heralded or
  not) are distinguished with error at most `ε` from the records of some common continuation
  alone, and no three are pairwise
  so distinguished; for heralded preparations the errors are conditional (section 1.2).
- **Q2 (one fixed qubit model).** There is a qubit model `𝔔` with `d_K(I, 𝔔) ≤ ε`.
- **Q3 (a dense coherent family).** For a fixed axis `n̂`, every `θ ∈ [0, 2π)` (the channel
  `Ad(e^{−iθ n̂·σ/2})` has period `2π` in `θ`) has a label `c(θ)`
  with `Σ_h ‖𝓘_{c(θ),h} − p_h(θ) · Ad(e^{−iθ n̂·σ/2})‖_⋄ ≤ ε` for some probability vector
  `p(θ)`: the round acts on the qubit as the unitary channel, and its record carries at most `ε`
  information about the qubit.
- **Q4 (composition; model-free).** For all `θ₁, θ₂` and every pair of protocols of horizon `K`
  that share a prefix (which may be adaptive, in exchange mode) and the same post-gate continuation, and differ only
  in that two consecutive gate rounds after the prefix have labels `c(θ₁), c(θ₂)` in one and
  `c((θ₁ + θ₂) mod 2π), c(0)` in the other, the unconditioned joint law of the records of all
  rounds other than the two gate rounds differs between the two protocols by at most `ε`. The
  continuation's labels are fixed in advance or depend on the prefix records only; no label of the
  continuation is a function of the records of the two gate rounds. Q2 is still taken over complete
  adaptive histories; only this replacement test restricts the continuation, because an adaptive
  continuation that reads the gate records can separate the two protocols through those records
  alone, even under exactly composing unitary channels.
- **Q5 (incompatible sharp reads).** Two labels, with two-class coarse-grainings of their records,
  are represented in `𝔔` within `ε` of rank-one projective measurements `{P_a, 1 − P_a}` and
  `{P_b, 1 − P_b}` with `Tr(P_a P_b) ∈ [1/4, 3/4]`. The coarse-grainings test a property of `𝔔`;
  they are not a readout rule and leave `d_K` unchanged (D4).
- **Q6 (the whole Bloch ball).** The states `𝔔` assigns to preparation prefixes are `ε`-dense in
  the pure states of `ℂ²`, not only in one great circle; for heralded prefixes, at conditional
  error `ε` (section 1.2).

**One direction each, to be proved in method step M2** (§A.34). Q2 implies the upper half of Q1
for `ε` below an explicit constant (approximate form of Lemma 2 of `whole-model-bridge.md`:167–178
[R]). Q2 and Q3 imply Q4 with error `4ε` (L3, [W]). Neither converse is claimed. Q1 and
Q4 are kept as separate conditions because they can be checked without any model. Q5 is close to
implied by Q1, Q2, Q3 and Q6 (not proved); it is kept because it names the two reads, and the
overlap does no harm.

**Uniformity.** "Uniform finite-precision error bound" means: one `ε` holds for every target `θ`
and every protocol of `Π_K`, at the one interface `I_{n(ε,K)}`.

**Relation to the kernel's two obligations.** The C5 discovery audit separates a relative-phase
resource (O1) from a continuous coherent transition (O2), each with a countermodel lacking the
other (`verification/audits/foundations/c5-discovery-audit.md`:25–37, :59–62) [K for the modules the audit cites, as it reports].
On the operational quotient Q3 plays the part of O2, and Q6 carries the complex structure that a
one-axis family with real reads lacks: rotations about one axis acting on reads in one plane give
real quantum theory of one system, a disk (a rebit) [W]. Q3 without Q6 is therefore reported
separately (token `PARTIAL-REBIT`, section 2).

### 1.5 The question, stated once

> **TUNE-1/Q2.** For the rule class 𝓡, carrier class 𝓛 and mode fixed by the owner
> (initial-condition mode, or exchange mode under H-write), does there exist a derived family of interfaces `{I_n}` (D1–D7) and an explicit function `N(ε, K)` such that, for
> every `ε > 0` and every horizon `K`, the interface `I_{n(ε,K)}` satisfies Q0–Q6 at error `ε` and
> horizon `K`?

In words: can one fixed OI dynamics, observed through an apparatus region chosen once and read
completely, produce operations that agree, to any requested precision over complete multi-time
records of any requested length, with one qubit carrying a dense one-parameter family of
coherent reversible operations that compose, two incompatible sharp measurements and every pure
state, with no gate, preparation law or decoder chosen for the target?

This is the question proposed in the external assessment of Step 1, with each word made
operational: "single fixed OI dynamics" is section 1.1; "observational access derived from an
embedded apparatus" is section 1.2 with D1–D7; "approximately coherent two-state operations" is
Q2 and Q3; "uniform finite-precision error bounds" is Q0 and the uniformity clause; "preserving
composition" is Q4; "complete observable histories" is the distance `d_K`; "one reusable physical
interface" is D1.

### 1.6 Owner decisions this question implements

| Owner decision (Issue #1236, 2026-11-11, and the original authorization) | Where it enters |
|---|---|
| Target reading (B): what an embedded observer can prepare and measure; agreement in experiments, not a quantum description of configurations | Q2 compares record laws only; no clause reads a representation of the configurations (control C-REP) |
| Approximate first | Q0–Q6 at error `ε`; exact rotations are not asked |
| One quantum bit | The comparator is `ℂ²`; Q6 asks for the whole Bloch ball |
| Amplitude rotations count only together with a derived readout rule | Q3 is never sufficient alone; D4 fixes the readout as the pushforward of `μ` |
| "without introducing an independently postulated quantum rule" | D6 |
| "I do not want us to assume that finite observational access necessarily means finite underlying dynamics" | Both carrier classes are admitted; neither is inferred from the other; control C-CARD |
| Born probabilities, Kochen–Specker contextuality and Bell are separate obligations (Step 3) | Section 2.3: none is decided or claimed here; H-μ stays a named hypothesis |

### 1.7 Why D1–D7 leave room for a pass, and where restricted access enters (rationale; [W])

This is the first internal review's answer to whether a pass is possible at all under D1–D7 with
full access inside the region. It is recorded as an unreviewed rationale, not a result.

- Full access inside `O` does not reduce the question to the configuration-level reading.
  `Λ ∖ O` is never read, and the record theory is a quotient of laws, so Step 1's
  configuration-indexed obstructions (section 5, rows 1–3) do not apply to it.
- C-POS-1 and C-POS-2 show that classical hidden state with restricted access can meet Q1–Q6, and
  C-POS-2 meets Q0 as well at a fixed menu.
- A pass would therefore plausibly need a rule that carries information out of `O`, keeps it
  unread, and returns it only through randomly sampled outcomes. The reviewer's example is
  one-time-pad masking at the region boundary, which the second-order form allows (not examined
  here).

This is where the owner's third class, "Restricted observational access" (Step 1 B), does the
work in this question: through the boundary of `O` and the unread law `μ`, not through a declared
restriction (D5 forbids those). For R-lin, the expectation recorded in M3, with the gap recorded there closed, is that it does no
work.

***

## 2. Decision rule

### 2.1 Tokens and conditions

Let `𝕀_D` be the set of derived families for the owner's 𝓡 and 𝓛. The tokens:

- **`PASS-DERIVED[R, 𝓛, λ, m | H]`**: a family in `𝕀_D` and an explicit `N(ε, K)` are exhibited,
  and Q0–Q6 are proved for every `ε > 0` and every `K`, under the hypotheses `H`, with the
  robustness clause of D3 met. The token names the rule `R`, the carrier class `𝓛` (`𝓛_fin`, or
  `𝓛_∞`), the law `λ`, the mode `m` (`init`, initial-condition mode, over its non-adaptive
  protocols; `exch`, exchange mode, over adaptive protocols) and every hypothesis used: H-μ
  always, H-∞ with `𝓛_∞`, H-nl with R-nl, H-write with `exch`. For example
  `PASS-DERIVED[R-lin, 𝓛_fin, uniform, init | H-μ]` and
  `PASS-DERIVED[R-lin, 𝓛_∞, uniform, exch | H-μ, H-∞, H-write]` are distinct tokens. Only an
  `init` token is a result about the rule alone; an `exch` token assumes the observer's writes and
  does not obtain them from `Φ_F`.
- **`FAIL-CLASS(𝓢)`**: for a stated subclass `𝓢 ⊆ 𝕀_D` it is proved that there are `ε₀ > 0` and
  `K₀` such that no member of any family in `𝓢`, at any resource, satisfies Q1–Q6 at `(ε₀, K₀)`.
  `𝓢` is named by its rule, carrier, ensemble, mode (with H-write for exchange mode) and any
  further restriction; the token never states more than `𝓢`.
- **`PARTIAL-x`** (reported only if the owner says so; section 9, choice 8): a family in `𝕀_D`
  for which a stated proper subset holds, named with rule, carrier, law, mode and hypotheses as
  for `PASS-DERIVED`. `x` is one of: `REBIT` (Q0–Q5 without Q6); `NOCOMP`
  (Q3 without Q4 at the uniform bound); `FIXEDK` (Q0–Q6 for one stated `K` only);
  `NONADAPTIVE` (in exchange mode, Q0–Q6 for non-adaptive protocols only).
- **`OPERATIONAL-ONLY`**: Q0–Q6 hold at a stated scope (a stated set of `(ε, K)`, protocol class
  or menu; Q0 is not applied to a construction that is not a lattice interface), some D-clause
  fails, and the family is not classified `PASS-COMPILED`. For a control, the Q-conditions are
  taken from its source records at the scope they state (section 3), not derived. This is the
  classification of a supplied construction. It is not a verdict on the question and never counts
  towards a pass.
- **`PASS-COMPILED`** (exists only if the owner picks choice 11(b)): Q0–Q6 hold for every
  `(ε, K)`, D7 holds, and D6(b) is the only D-clause that fails. It is reported apart and never
  counts towards a pass. A family that fails D7, or any D-clause besides D6(b), is
  `OPERATIONAL-ONLY`; so is a family that fails only D6(b) and meets Q0–Q6 at a restricted scope
  only. Where D6(b) is applied (choice 11(a) or (b)), it is failed alike by a program held in
  `r_O`, in the labels or in the program blocks, and whether the label that holds it is
  exhibited or only shown to exist (section 1.3), so neither this token nor `OPERATIONAL-ONLY`
  is avoided by moving the program or by restating the encoder.
- **`INCONCLUSIVE(gap)`**: none of the above is reached within the effort bound (section 7). The
  gap names the lemma that was not proved, with its exact statement.
- **`VOID(control)`**: some control of section 3 is not green when the verdict would be rendered,
  or a link of the verdict rests on a premise that section 5 shows unsupported.

Controls (section 3) are classified with these tokens and with the Q- and D-clauses. Every token a
control's row expects is one of the tokens above; an expected "not `PASS-DERIVED`" (or "never
`PASS-DERIVED`") is met by any obtained classification other than `PASS-DERIVED`, and an expected
"supplied" by the failure of a D-clause (section 1.3). Expectations stated as Q- or D-clauses
(C-TAB, C-B1, C-CARD, C-EXACT, and the clause entries of every row) are compared clause by clause;
besides holding (met) or failing, a clause entry may be `not applicable`, where the row states why
the clause cannot be posed for that construction, or, for D6(b), `unclassified`, where the row
states that a label's class cannot be read and the D6 row is not `proved` (section 1.3).

### 2.2 How the token is generated

The result note carries two tables in a stated schema (§A.44): a **condition table** with one row
per condition used (identifier, exact statement, status `proved` / `refuted` / `open`, layer
[K]/[P]/[P-imp]/[R]/[W], source file:line; `not applicable` occurs only in clause entries of the
control table), and a **control table** (section 3; identifier,
expected classification, obtained classification, status `green` / `red`). The token is computed
from the two tables in this order, and from nothing else:

1. If any control is red, or any row the verdict relies on as established has status ≠ `proved`:
   `VOID(that row)`. A refuted condition enters the verdict as the `proved` row that states its
   negation for the named subclass.
2. Else, if Q0–Q6 and D1–D7 are `proved` for one family over every `(ε, K)`:
   `PASS-DERIVED[R, 𝓛, λ, m | H]` for that family. Every `FAIL-CLASS(𝓢)` proved for another
   subclass is reported with it, row for row.
3. Else, if a `FAIL-CLASS` theorem is `proved` for `𝓢 = 𝕀_D`: `FAIL-CLASS(𝕀_D)`. If it is proved
   for a proper subclass only: `FAIL-CLASS(𝓢)` together with `INCONCLUSIVE(gap)` for
   `𝕀_D ∖ 𝓢`.
4. Else, if a `PARTIAL-x` row set is `proved` and the owner has asked for partials: `PARTIAL-x`
   together with `INCONCLUSIVE(gap)` for the rest.
5. Else: `INCONCLUSIVE(gap)`.

A candidate family encountered during the work that is classified `OPERATIONAL-ONLY` (or
`PASS-COMPILED`), or that fails a Q-condition, is recorded with its classification and does not
change the token.

### 2.3 What each outcome would and would not establish

**`PASS-DERIVED` would establish**, at the layer of its weakest link (most likely [W], a paper
derivation awaiting review): for the stated rule, carrier class, ensemble and mode, an observer
region chosen once and read completely has a record theory within `ε`, over complete records of
horizon `K`, of one qubit with a dense coherent one-parameter family, two incompatible sharp reads
and every pure state, with explicit resources `N(ε, K)` and the label-generation cost `G(ε, K)`
reported beside them (section 1.2). In mode `init` it would be the first
construction on `main` of quantum operational behaviour in which neither the access nor the
quantum rule is supplied (Step 1 B.12 (ii)), over non-adaptive protocols. In mode `exch` it would
establish the same over adaptive protocols given the observer's classical write access H-write; it
would not show that `Φ_F` supplies those writes.

**It would not establish:** the selection of the Born rule (H-μ remains a hypothesis: why the
world's unprepared part has law `μ` is the measure question, and agreement for one qubit with
`d = 2` is not the general rule); Kochen–Specker contextuality or any nonclassicality (the
Kochen–Specker sphere model reproduces one qubit with a classical hidden variable, so one-qubit
agreement is compatible with a noncontextual model); Bell correlations or any composite system;
exact rotations (reading B-exact); quantum mechanics or the five completion conditions
(`exactAll_iff_physical_general`, Step 1 A.1); a quantum description of the configurations
(reading A); that a physical apparatus of this kind exists in nature; any change in correctness
(it would be a consistency-axis result, §A.23); any manuscript statement.

**`FAIL-CLASS(𝓢)` would establish** that the stated subclass does not reach the target at
`(ε₀, K₀)`. **It would not establish** a no-go for other rules, other ensembles, other access
modes, other carriers, exact forms, other observer-level extensions or OI generally (Code Review
Rules, "Bridge and no-go scope"). A result proved on `𝓛_fin` is not transferred to `𝓛_∞` or
conversely without its own proof.

**`INCONCLUSIVE(gap)`** establishes nothing about the question and records the gap.
**`VOID`** establishes nothing.

***

## 3. Controls

Each control is a paper derivation, carried out first (method step M1), and is a checkpoint: its
expected classification is stated now, its obtained classification is entered in the control
table, and the verdict is generated only when every row is green (§A.29, §A.41). A control turns
red if its obtained classification differs from the expected one; that means the criterion is
wrong, and the step returns to the owner with the definitions, not with a verdict.

| ID | Construction | Why it is a control | Expected classification | Source |
|---|---|---|---|---|
| C-SUP-1 | Main's uniform continuum realization: one finite reversible realization per `(d, m, K, ε)`, built from a net of quantum instruments | Supplied access with the quantum rule inside; shows D6 has teeth | Q0–Q6 at the stated `(ε, K)` [P]; D6 fails ("Quantum mechanics enters as the instrument data and as the state held in the hidden register", Main:582); D1 fails (the realization is built from the target net). `OPERATIONAL-ONLY` | Main:566, :582, :596, :598 [P] |
| C-SUP-2 | Per-target access: for each `θ`, a world, region or law chosen so that the record law of that one target is reproduced | Shows D1 and Q4 have teeth: per-target worlds cannot be composed in one world | D1 fails; Q4: not applicable (no single interface across targets). Supplied | Gate A, `endpoints.md`:67 [R]; `whole-model-bridge.md`:283–287 ("It cannot simply identify states that an available sensor distinguishes") [R] |
| C-POS-1 | The Kochen–Specker sphere model with its supplied contract | Known positive: exercises the two halves of the criterion separately | Not a lattice interface, so Q1–Q6 (Q0 does not apply): `ε = 0` for every finite adaptive rank-one projective protocol (the record states this; general instruments not covered, so Q2 is checked on that protocol class); D3 fails (cosine-hemisphere law supplied), D5 fails (preparation cone, private workspace and seeds by declaration), D6 fails (rotation primitives), D7 fails (continuum carrier). `OPERATIONAL-ONLY` | `history-architecture-v5/REPORT.md`:305–312 [R]; Kochen–Specker 1967 (imported there) |
| C-POS-2 | Its finite discretization `finite-a2-v5` | Positive control for the approximate form and for Q0 | Q0–Q6 at a fixed finite menu and horizon `h = K`: Q2, Q3, Q5 and Q6 at every `ε ≥ b + δ`; Q4 from the floor that the L3 budget (M2) gives from Q2 and Q3; Q1 on the range of `ε` where its upper half holds; the last two stated at M1 [W]; a menu for which the Q4 floor lies outside the range on which Q1's upper half holds is outside this row's scope. Here `b` is the record bound of :36–37 at that `h` and at the parameters `M, W, B` of :23, and `δ` is the larger of the largest gap between a requested angle and the nearest menu angle (the diamond distance between the two rotations being at most that gap) and the largest trace distance from a pure state to the nearest pure state `R_w n` prepared by a menu prefix of horizon at most `K` (a menu preparation or reset direction `n` followed by a word `w` of menu rotations) [W]. The record fixes a finite menu of rotations, rank-one projective measurements and preparations (:11–12) and states nothing about the density of prepared states; `δ` carries it. The classification is stated for menus containing two rank-one measurements with `Tr(P_a P_b) ∈ [1/4, 3/4]` (Q5), which the record does not require. Q3 and Q6 therefore hold only to the menu's resolution. D fails as for C-POS-1. `OPERATIONAL-ONLY` (with the menu restriction recorded) | `finite-a2-v5/REPORT.md`:11–14, :23, :36–37, :105–115 [R] |
| C-ISO-1 | A classical wave on the cubic lattice with real amplitudes (the real lift of R-lin), read completely in a region; its large-scale propagation is isotropic | The external assessment's countercontrol: isotropy and interference without a qubit. Out of class: it fails D7 trivially and has no `μ` specified. Its value is that operations which vary continuously and compose (Q4) are still rejected by Q1 [W]. The external countercontrol's in-class wave is R-lin itself, which L5 tests | Q1 fails: complete reads of real amplitudes distinguish arbitrarily many preparations (the mechanism of the bridge's Lemma 1) [W]; D7 fails (E-real). Interference statistics alone are not a failure of the control (`observation-context-protocol.md`:37–38, "interference alone is insufficient") [R]. Not `PASS-DERIVED` | SM:258–268, Corollary 1a (`ohInvariant_iff`, OB/CubicIsotropy.lean:116) [K]; `whole-model-bridge.md`:132–197 [R] |
| C-ISO-2 | **A classical diffusion: one lazy random walker.** *World:* `Λ ∈ 𝓛` and one walker, whose position `X_t ∈ Λ` is the whole state. *Dynamics:* each tick moves the walker by the `O_h`-symmetric lazy kernel `K(x, ·) = ½ δ_x + Σ_{j = 1, 2, 3} Σ_{s = ±1} (1/12) δ_{x + s e_j}`, the contributions of directed neighbours that coincide on a small torus being added (so `K(x, x + e_j) = 1/6` when `L = 2`, and `K(x, x) = 1` when `L = 1`), with fresh randomness each tick; the walker's law obeys the lattice heat equation and spreads isotropically at large scales. *Interface:* `O` a box, `C ⊆ O`. A label is a permutation `g_c` of `C`. At the start of a round the walker is moved to `g_c(X)` if it is in `C`, and nothing happens otherwise; then `τ` ticks of `K` run. The record at each tick is the walker's position if it is in `O`, and a blank symbol otherwise. At time zero the walker is outside `O`, with any law `μ` on `Λ ∖ O` (the argument does not use `μ`) | Isotropic classical propagation in which the labels do act on the walker. The negative must not come from a property that every classical hidden-variable model has (proves-too-much check below) | Q1, Q2, Q3, Q5 and Q6 cannot hold together at `ε < ε_D`, an explicit constant stated at M1 with the conditional-error factor of section 1.2 (these are the conditions the argument uses: Q2's model `𝔔`, of which Q3 and Q6 are statements, and Q5's reads); D7 fails (a stochastic rule outside 𝓡). Not `PASS-DERIVED`. Argument [W]. (i) The whole state is the walker's position, so a label can act only when the walker is in `C ⊆ O`, where the preceding tick has read it. Conditional on a prefix's complete records, either the walker is at a recorded `x ∈ O`, and the effective state is fixed by `x` alone (Markov property), or it is outside `O`, and every label acts exactly as `c(0)` does. (ii) A state of the second kind, as a state of the model `𝔔` of Q2, satisfies `Ad(U_θ)ρ ≈ ρ` for every `θ` under Q3, read out through Q5's reads, so it lies within `O(ε)` of the `n̂` axis. (iii) By laziness, from `x ∈ O` the round's first-tick record shows the walker at `g_c(x)` with probability at least 1/2, while any other starting point puts mass at most 1/6 there (at most 1/12 when `L ≥ 3` or on `ℤ^3`). Round record laws from distinct starting points therefore differ in total variation by at least 1/3, whereas Q3 makes the round's record law independent of the input within `ε`. So below `ε_D` all effective states are of one kind: either all lie near the axis (Q6 fails), or there is a single state (Q1 fails). The argument uses two properties: the whole state is read whenever a label acts, and the walk is lazy. It does not use that the walk is classical. Strict contraction of `K^τ` is not used, because it is not uniform in `L` and a contraction can act isometrically on a quotient [W] | SM:258–268 (isotropy of `O_h`-equivariant kernels) [P]; the argument is [W] |
| C-FIN | The eight-point model with the first-moment decoder | A supplied finite access quotient with a known error floor; checks Q3's detection of a finite group | Q2 with Q3 fails below `ε = 1/15`: the model has 24 Clifford actions, and 1/15 is a record-level error floor for one non-Clifford rotation, reached through the comparator (Q2), not a direct diamond bound on Q3; D fails (supplied contract). Not `PASS-DERIVED` | `operational-quotient-v3/REPORT.md`:20–23, :218–227 [R] |
| C-REBIT | Real quantum theory of one system (state space a disk); the kernel's `realClass`, which has `rot` and lacks the phases, is its configuration-level analogue | Exercises the separation of Q3 from Q6 | Not a lattice interface: Q1–Q5 hold and Q6 fails, the pattern that `PARTIAL-REBIT` reports for a family in `𝕀_D`. Never `PASS-DERIVED` | `realTheory_rot`, `realTheory_not_phases` (OB/F2CoherenceControls.lean:306, :317) [K]; the disk is [W] |
| C-TAB | The finite-menu table representation: any `N` listed preparations represented on `ℂ^N` | Shows Q2's fixed dimension has teeth | Q2 holds only with `d = N`; with three pairwise distinguishable preparations, Q1 and Q2 at `d = 2` fail | `whole-model-bridge.md`:204–211 [R] |
| C-B1 | B1 with the bridge's access: one isolated real pair, a loaded coefficient, point preparations, a sign read | The one record on `main` with continuous mixing in the substratum | Q1 fails (the bridge's Proposition, `d + 1` perfectly distinguishable preparations for every `d`) [R]; D2 fails (E-control), D7 fails (E-pair, E-real) | `two-mode-drive.md`:22–32, :124–147; `whole-model-bridge.md`:132–197 [R] |
| C-REP | A "construction" whose only evidence is a Hilbert-space representation of the records containing a mixing unitary | The Arc D result that representation is a disqualified ground | No Q-condition reads a representation; padding by an ancilla unitary (`padData_rooted`, OB/OperationalSourcing.lean:476) changes no record law and so cannot move `d_K`; not `PASS-DERIVED` | `PROGRAMME.md`:216 [K for the module, as the map reports] |
| C-CARD | (a) A fixed finite world (`L` fixed). (b) The infinite lattice under H-∞. (c) A finite cyclic surrogate of an infinite carrier | Checks that the criterion assumes neither a finite nor an infinite world | (a) For fixed `L` there is `ε₀(L) > 0` below which Q3 and Q6 fail together: a fixed finite realization cannot reproduce a qubit's full theory (Main:560 [P, P-imp]), and for a fixed finite experiment family its behaviours form a compact set (Step 1 C, B.7 row, column (2)) [W]. The criterion must not certify a fixed `L`; Q0 lets `L` grow. (b) Every definition of sections 1.2–1.4 is well-defined on `ℤ^3` (product law; finite `O`; finite records; finite light cone by range one) [W], except the level-set law of D3, which is defined on `𝓛_fin` only and which no option of choice 6 requires on `ℤ^3`, and no clause uses finiteness of `Λ` except the resource count. (c) Verdicts are indexed by `K`: a finite surrogate agrees with an infinite carrier up to a horizon and differs after it (finiteness audit, control (1), Step 1 B.12) [R] | Main:560 [P, P-imp]; Step 1 B.0, C |
| C-MEAS | B2: B1's carrier with the posited quadratic sensor `t(z)`, seeds with an atomless law `μ`, and the one-read law `p_1(θ) = F(cos²θ)`, with `F(t) = μ((0, t))`. The law matches the quantum value for every `θ` exactly when `μ` is uniform in the detector coordinate. It is run here under that uniform law and under one of the record's predeclared symmetric seed laws as `μ′` | Supplied-measure control on a concrete construction: shows that the robustness clause of D3 has teeth | The one-read match holds under the tuned law and fails under `μ′`, so D3's robustness clause classifies the measure as supplied. Independently, D4 fails (a posited response function), D7 fails (B1's carrier), and Q2 fails on the two-read law (no fixed `ℂ²` instrument matches it). Not `PASS-DERIVED` | `measurement-source.md`:29, :57–63, :87, :118, :141 [R]; Step 1 F.1, control 2 |
| C-NULL | The interface of section 1.2 with the labels decoupled: the exchange writes into cells that no `F_i` reads (in initial-condition mode, the program blocks lie in such cells), so `μ` alone drives the records | The cheapest check that Q3 is not met vacuously. Out of class: under a rule of 𝓡 every cell is read by its neighbours' `F_i` | Every label acts as `c(0)` does, so under Q3, read out through Q5's reads, every state of the model `𝔔` of Q2 that the data constrain lies within `O(ε)` of the `n̂` axis, and Q2, Q3, Q5 and Q6 cannot hold together below an explicit constant [W]; these are the conditions the argument uses. Q3 alone is a diamond-norm statement about `𝔔`, constrained by data only through the states reached, so the expected failure is of Q2, Q3, Q5 and Q6 together, not of Q3 alone. Not `PASS-DERIVED` | this proposal, section 1.4 [W] |
| C-PROG | finite-a2-v5's controller (REPORT:11–19), or Main's single controlled dynamics with its read-only program register (Main:582), compiled into `r_O` under a hypothetical rule `F_U` in second-order form that can simulate any finite controller. `F_U` is stipulated for this control only, as a rule distinct from every member of 𝓡 (in particular from R-lin and R-nl); whether R-nl has this capacity is not assumed either way. The family's specification gives `r_O` as the explicit configuration the compilation outputs and does not name the controller; the compilation is recorded as how `r_O` is defined (D6(b)). The labels are indices of the controller's menu settings (for Main:582, of the instruments its protocol table selects). The fair bits are drawn from the uniform environment `Λ ∖ O`, and the private workspace is kept outside `O` | A simulator moved into the apparatus meets D3, D5 and D6(a). Shows that D6(b) has teeth, and fixes the classification of compiled simulators before any result | Clause by clause, for the option of choice 11 fixed at M0. *Q-conditions:* not derived; `F_U` is assumed to reproduce the compiled controller's record law, its workspace starting `μ`-random included, so Q0–Q6 are taken from the controller's source record at the scope it states (as C-POS-2 for finite-a2-v5; at the stated `(ε, K)` for Main:582). *D3, D5, D6(a):* met (the vocabulary search of the specification, which states `r_O` as a configuration only, has no hit). *D6(b):* fails under 11(a) and 11(b), because `r_O` is defined as the compilation of a controller whose specification uses sphere rotations and a hemisphere-law sampler (finite-a2-v5) or the instrument data of quantum mechanics (Main:582); the ledger class of every component of the label encoder is `parameter`, and none is a hit; not applied under 11(c), where D6 is (a) alone. *D2, D7:* fail under every option, since `F_U ∉ 𝓡`. *D1, D4:* entered as obtained; they do not affect the token. *Token:* `OPERATIONAL-ONLY` under every option; under 11(b) it is not `PASS-COMPILED`, because D7 fails. It is not a pass under any option. Under 11(c) the control exercises D7 alone, and D6(b) has no teeth there | `finite-a2-v5/REPORT.md`:11–19 [R]; Main:582 [P] |
| C-PROG-P | C-PROG's controller under the same stipulated rule `F_U`, with the compiled program moved out of the ready configuration into the labels. `r_O` is a configuration that encodes no controller: the one from which `F_U` executes a program delivered through the label cells, the same whatever program is delivered. Each label is the configuration the compilation outputs for the controller together with one of its menu settings. In initial-condition mode the labels are the initial content of the program blocks `P_j`; in exchange mode they are exchanged into `C`. The family's specification gives `r_O` as an explicit configuration and does not name the controller; the label encoder gives each label as an explicit configuration, and the compilation is recorded in the source ledger as how the encoder is defined (D6(b)). Fair bits and workspace as in C-PROG. A second presentation of the same family is entered beside the first. Its encoder names no compilation: it states only that for each target a label with the target's record law exists, and cites the capacity of `F_U` in existence form (for each finite controller some label makes `F_U` reproduce its record law), which the stipulation realizes by the compilation. A third presentation is entered beside them. Its encoder cites, without proof, that for each record law of a finite adaptive qubit protocol some label of `F_U` has it within `ε`, and names no controller | C-PROG's supplied program, placed where a test of `r_O`, `O`, `C`, `τ`, `μ` and the generating rule alone does not look. Shows that D6(b) has teeth for the label encoder and the program blocks, and that neither moving a program out of `r_O` nor stating the encoder in existence form changes the outcome of D6(b); with C-PROG, checks the encoder test in both directions. The third presentation exercises the `unclassified` default | Clause by clause, for the option of choice 11 fixed at M0, and in each mode. *Q-conditions:* as C-PROG, not derived, at the scope the controller's source record states and over the labels the compilation outputs; other labels are not classified. *D3, D5, D6(a):* met (the vocabulary search of the specification, which states `r_O` as a configuration only, has no hit). *D6(b):* the ledger entries of `r_O`, `O`, `C`, `τ`, `μ` and the generating rule have no hit; the ledger class of every component of the label encoder is `content`, and each is a hit, because each label is defined as the compilation of the controller of C-PROG's D6(b) entry; in the second presentation the cited ground is a capacity statement, its proof is the compilation (a code with a simulation step), the label it supplies encodes the controller, and the class is again `content` and a hit, with every other entry and the token unchanged; so in these two presentations D6(b) fails under 11(a) and 11(b), and is not applied under 11(c). In the third presentation the proof of the cited capacity statement is not available, the class of every component of the label encoder is `unclassified`, and the D6 row is not `proved` under 11(a) and 11(b), with every other entry and the token unchanged. *D2, D7:* fail under every option, since `F_U ∉ 𝓡`. *D1, D4:* entered as obtained; they do not affect the token. *Token:* `OPERATIONAL-ONLY` under every option; under 11(b) it is not `PASS-COMPILED`, because D7 fails. It is not a pass under any option. Under 11(c) the control exercises D7 alone | `finite-a2-v5/REPORT.md`:11–19 [R]; Main:582 [P]; section 1.3, D6(b) |
| C-EXACT | The definitions applied to the exact cases: C-POS-1 at `ε = 0` on its protocol class, and C-ISO-2, which must fail at every `ε` below its stated constant | §A.21: the operation modelled must preserve what it provably must; a definition that misclassifies an exact case is wrong | Both exact cases classified as stated above, with no slack | as above |

**Proves-too-much check** (every negative control). The negative controls are the rows whose
expectation includes a failed Q-condition: C-ISO-1, C-ISO-2, C-FIN, C-REBIT, C-TAB, C-B1,
C-CARD (a), C-MEAS and C-NULL (C-EXACT's negative case is C-ISO-2's argument and is checked under
that row). Each negative control's argument names the properties of its construction that it uses
(C-ISO-2 lists them in its row). At M1 each such property is checked against three cases, each at
the scope at which its classification is stated:

- C-POS-1, on its protocol class at `ε = 0`;
- C-POS-2, for each fixed finite menu containing a non-Clifford rotation and two rank-one
  measurements with `Tr(P_a P_b) ∈ [1/4, 3/4]`, and each resolution parameter `M` of
  `finite-a2-v5/REPORT.md`:23, at the floors its row states;
- the class of reversible deterministic rules acting on `O` and on an environment that is never
  read, under a uniform law, taken as families with growing resources.

*Definitions.* A property **holds** in C-POS-1 or C-POS-2 if it is true of that construction at
that scope; it **holds** in the third case only if it holds for every member of the class. An
argument **applies** to a case if every property it uses holds there and its conclusion
contradicts the case's stated classification at the scope that classification states. The stated
classifications are the C-POS-1 and C-POS-2 rows of the control table and, for the third case,
that section 1.7 leaves it open, so that no control may exclude it. If an argument applies to
any of the three, the control is red: the argument proves too much, and the criterion goes back
to the owner (section 7). The properties listed for an argument are all those its conclusion is
derived from; at M1 the reviewer checks that the argument uses no property it does not list.

What the check is expected to find, as [W]:

- *C-ISO-2.* Its first property, that the whole state is read whenever a label acts, fails in
  all three cases, and the argument needs both properties. In C-POS-1 the hidden sphere point that
  the rotations act on is never read. In C-POS-2 the controller acts on a private workspace that
  is never read. In a reversible rule with an unread environment, the environment's state stays
  unread when `O` is read.
- *C-ISO-1, C-B1 and C-TAB.* Their arguments use more distinguishable preparations than two, and
  that property does not hold in any of the three cases.
- *C-FIN and C-CARD (a).* C-FIN's argument uses that the label actions form the 24-element
  Clifford group, which contains no non-Clifford rotation. That property fails in C-POS-1, in
  C-POS-2 at each of its menus, and for every member of the third class that has a non-Clifford
  operation. C-CARD (a)'s argument uses a fixed `L`, and its conclusion is an unspecified
  `ε₀(L) > 0`. That conclusion contradicts no stated classification: C-POS-2 has its own floor
  `b + δ` for Q3 and Q6, and the third case is taken at growing resources. Neither argument applies, by the
  definitions above.
- *C-REBIT.* Its argument uses that every state and every operation is real in one fixed basis,
  so that the states fill a disk, and its conclusion is that Q6 fails below `1/2`, the trace
  distance to the disk from either pole of the Bloch ball on the axis normal to it. The property concerns the states and
  operations of the record theory, not a hidden variable. It fails in C-POS-1, which prepares
  every pure state on its protocol class (`history-architecture-v5/REPORT.md`:13–14, :38–67). In
  C-POS-2 it fails at every menu whose prepared states do not lie in one great disk. At a menu
  whose prepared states do lie in one, the pure prefix states lie on its great circle and
  `δ ≥ 1/√2`, the trace distance to that circle from either pole of the Bloch ball on the axis
  normal to the disk, so Q6 is classified only at
  `ε ≥ b + δ > 1/2` and C-REBIT's conclusion contradicts no stated classification. It is not true
  of every member of the third class (for example, of one that hosts C-PROG's compiled controller
  under `F_U`).
- *C-MEAS.* Its Q2 failure uses that a read leaves the point signal unchanged and draws a fresh,
  independent seed (`measurement-source.md`:87). That property does not hold in any of the three
  cases: in C-POS-1 and C-POS-2 a projective outcome is followed by a fresh preparation along the
  outcome's direction (the continuous model, `finite-a2-v5/REPORT.md`:53–56; C-POS-2's finite
  controller discretizes it, drawing a fresh index from `ν_(s a)`, :113–115), and not every
  member of the third class has it.
- *C-NULL.* Its argument uses labels that act on nothing, and that property does not hold in any
  of the three cases.

**Two-way check of the encoder test** (D6(b), section 1.3; at M1). The ledger class of every
component of the label encoder must be obtained as `parameter` and not a hit on C-PROG, and as
`content` and a hit on C-PROG-P in its first two presentations, and as `unclassified` in its
third; an entry obtained otherwise turns
that control red. The check is run on the recorded ledger under every option of choice 11;
under 11(c) the entries are recorded and do not enter the classification. The property "the
family's label encoder is a hit" is also checked against the third case above, by the same
definition: it must not hold for every member of the class, and if it does the C-PROG-P row is
red. Expected, as
[W]: it fails for any member whose labels are all `parameter` or `selected`, and the definitions
of those two classes exclude no rule: a derivation that makes no label encode a system leaves
its labels `selected` whatever the form of its conclusion (section 1.3, *Encoding*). That is
read from the
test's wording and does not assume that such a member meets Q0–Q6, which is the question. No
control row has a `selected` label; that entry is first made for a
candidate family (M4, Route P).
C-POS-1 and C-POS-2 are not lattice interfaces and have no label encoder; their D6 entries are
those of their rows.

**Invariant → checkpoint table** (§A.41). Every property this proposal asserts of its own
execution, with the checkpoint that measures it.

| Invariant | Checkpoint |
|---|---|
| No computation is run in Step 2 | The result note's disclosure lists every command run; the reviewer checks it contains no interpreter, probe, checker or Lean build |
| Definitions and decision rule fixed before work | The owner-approved text of this file is identified by its sha256 in the result note; every definition used is quoted from it; any change is an amendment approved by the owner before work resumes |
| Controls green before the verdict | The control table; step 1 of section 2.2 |
| No negative control proves too much | A proves-too-much row for each negative control and for the L5 argument (M3; against the third case) in the control table: the properties its argument uses; for each of C-POS-1, C-POS-2 and the reversible-rule class with an unread uniform environment, at the scope stated in section 3, whether each property holds there (for the class, whether it holds for every member); and whether the argument's conclusion contradicts that case's stated classification at that scope. The proves-too-much entry is red if and only if, in some case, every property holds and the conclusion contradicts the stated classification; a red entry turns the control red, and a red entry for the L5 argument is a red row of the control table and counts as a red control in section 2.1 (`VOID(control)`), section 2.2 step 1 and section 7 |
| Compiled simulators classified as fixed in advance, wherever the program is held and however the encoder is presented | Choice 11 is recorded at M0; the obtained clause entries and tokens of C-PROG and of C-PROG-P, in each of its three presentations, are compared with those their rows state for the option chosen; the two-way check of the encoder test (section 3) |
| Verdict computed from the tables | Section 2.2; the reviewer recomputes the token from the two tables |
| No premise adopted | A hypothesis ledger in the result note lists H-μ, H-∞, H-nl and H-write if used, and every [R] statement used, each with its status, and each appears in every conclusion that uses it |
| Rule class respected | A D7 row for every family considered |
| No quantum input (D6) | A D6 row for every family considered, with two entries. (a) The search of its specification for the D6 word list. (b) The source ledger of section 1.3: for each of `r_O`, `O`, `C`, `τ`, `μ`, the generating rule and each component of the label encoder (the gate map `c(θ)`, each of Q5's two labels, each preparation prefix with its herald, each continuation a proof names, and in initial-condition mode the initial content of the program blocks), how it is defined, including how a configuration given explicitly was obtained; every capacity statement used and every system such a statement or its proof makes it encode (a code with a simulation step), with the word-list search of that system's specification; for each component of the encoder, its class (`parameter`, `selected` or `content`), or `unclassified`; and whether any definition, any submitted proof of a Q-condition, or the proof of a capacity statement one rests on, identifies configurations of cells, label cells and program blocks included, with numerals, tables or a sampler of a D6 quantity. Under 11(a) or (b), a hit on either entry makes the family supplied, classified by section 2.1, and an item whose ledger entry cannot be read from the submitted text, an `unclassified` component, or a capacity statement whose proof is not in the submitted text or at a cited file and line, leaves the row not `proved`; under 11(c), entry (b) is recorded and does not enter the classification |
| Resource claims complete | The Q0 row of the condition table states `N(ε, K)`, with the program blocks counted, and beside it `G(ε, K)` or the statement that a label is shown only to exist (section 1.2) |
| Error budget of a pass | The condition table states, for each of Q1–Q6, the error at which it is proved at `I_{n(ε,K)}`; the Q4 row is at most `ε`, with Q2 and Q3 at `ε/4` where Q4 is obtained through L3 (M2); `N` and `G` are stated for that interface |
| Layer tags kept distinct | Every link of every proof carries one tag; no [W] extension is tagged [K] (in particular no extension of `nonnegBounded_not_denseUnitaryControl` beyond its statement) |
| Negatives scoped | Every `FAIL-CLASS` row names `𝓢` |
| No manuscript or Lean change | `git diff --stat` of the unit touches only this directory |
| Paper register | The added text is searched for the §A.32/§A.33 phrase families before review |

***

## 4. Method (paper derivation only)

Depth-first (§A.12, §A.31): each step is a numbered node closed by an explicit check, with its
verdict recorded at the node; the decisive branch is chosen at each level. A favourable branch is
pressure-tested before it is accepted.

**M0. Freeze.** The owner approves this file or an amended one; its sha256 is recorded. Owner
choices of section 9 are fixed then and are not reopened after a verdict to obtain a different one
(Gate A, `endpoints.md`:119–123: an approximation target may not retrospectively replace a failed
one; here, equally, a failed verdict may not be replaced by changing a choice). A later different choice is a new question with its own
proposal. The owner's approval record states: "A `PASS-DERIVED` would be a consistency-axis
result (§A.23); it would move no correctness assessment."

**M1. Controls.** Derive each row of section 3 on paper from the cited records, and enter the
obtained classification. Then apply the proves-too-much check to every negative control, and the
two-way check of the encoder test (section 3). Rests
on: Main:560, :566, :582, :596, :598 [P]; the records cited in the control table [R];
OB/CubicIsotropy.lean:116, OB/OperationalSourcing.lean:476, OB/F2CoherenceControls.lean:306,
:317 [K]. If any control is red, stop and return to the owner (section 7).

**M2. Lemmas about the criterion** (route-independent; each proved as [W] for review).

- L1 (well-posedness on both carrier classes): the record law, `d_K` and Q0–Q6 are defined on
  `𝓛_fin` and on `ℤ^3`; on `ℤ^3` with the uniform product law the record law exists (product
  measure) and depends on finitely many sites for each `K` (finite range).
- L2 (Q2 ⇒ upper half of Q1, for `ε` below an explicit constant): from Lemma 2 of
  `whole-model-bridge.md`:167–178 [R], re-derived here in approximate form (three qubit states
  cannot be pairwise distinguished with small error).
- L3 (Q2 ∧ Q3 ⇒ Q4 with error `4ε`, `‖·‖_⋄` the diamond norm induced by the trace norm and TV
  half the `ℓ¹` distance) [W, unreviewed]. Error budget: (1) Q2 bounds the distance of each
  protocol's record law from its comparator law by `ε`, and marginalizing the two gate rounds'
  records does not increase it: `ε + ε`. (2) In `𝔔`, by Q3 and `Σ_h p_h(θ) = 1`, each summed gate
  channel `Σ_h 𝓘_{c(θ),h}` is within `ε` of `Ad(U_θ)`; each summed instrument is a channel, of
  diamond norm 1, so errors add under composition; for one axis `Ad(U_{θ₂}) ∘ Ad(U_{θ₁}) =
  Ad(U_{θ₁+θ₂})` and `U_0 = 1`, so each pair of gate rounds is within `2ε` of `Ad(U_{θ₁+θ₂})` and the
  two pairs are within `4ε` of each other. Given the prefix records, the continuation is the same
  fixed measurement of the state after the gate rounds, because none of its labels reads the gate
  records, and the comparator's laws are averaged over prefix records with total weight 1, so the
  comparator's two laws differ by at most `½ · 4ε = 2ε` (Main:596 [P] for the conversion). Total
  `4ε`. Without the restriction on the continuation in Q4 the implication is
  false: with each gate round exactly `Ad(U_θ)` and a record that tags its label (Q3 holds with
  error 0), a continuation that measures `Z` after one tag and `X` after the other separates the
  two protocols on input `|0⟩`, `θ₁ ≠ 0` and `θ₁ + θ₂ = 0` by total variation `1/2` (the external
  review's counterexample). In exchange mode every round's record contains its label `c_j`, so
  such tags are always present. Error budget of a pass: L3 gives Q4 at `4ε` from Q2 and Q3 at
  `ε`, not Q4 at `ε`. A pass at `(ε, K)` that obtains Q4 through L3 therefore proves Q2 and Q3
  at error `ε/4` at the interface it uses for `(ε, K)`, and `n(ε, K)` and `N(ε, K)` are stated
  for that interface; the other conditions are proved there at `ε`.
- L4 (escape audit, necessary conditions on any `PASS-DERIVED`): (a) the map from preparation
  prefixes to qubit states in `𝔔` is not injective on laws over configurations, and is not a
  fixed orthogonal linear frame with H-LIFT; otherwise MECH-2 Lemma F and Theorem U2(ii)
  (`mechanism-2-20261108/DESIGN.md`:307–345, :404–416) [R] would give a finite group of encoded
  unitaries, contradicting Q3; (b) the resource `N(ε, K)` is unbounded as `ε → 0` (C-CARD (a)).
  The parts of Lemma F and U2(ii) used are re-derived in the unit, since an [R] statement cannot
  serve as an established premise (§A.46 item 7), or the conclusion is stated as conditional on
  them (section 9, choice 9).

**M3. The decisive branch for R-lin** (if choice 1 admits R-lin). Before any constructive
attempt, decide the following question. It is stated here and not answered: no work on it was done
in drafting beyond recording the first internal review's sketch below.

- L5 (structure of R-lin record laws). For R-lin under the uniform law, in initial-condition mode
  and without heralds, what is the form of the record law of a label sequence? For R-lin each
  `Φ_F^t` is an endomorphism of the group `X_Λ` [W], and MECH-1 Lemma A states that under one
  fixed affine rule a setting held in the state "can only translate values"
  (`mechanism-1-20261107/DESIGN.md`:96–97, :404–430) [R]. If L5 determines the record laws as a
  family of translates, it bounds which operational distances can occur, and so bears directly on
  Q1, Q2 and Q5 for that subclass. The node then records which of the following leave L5's hypotheses:
  heralded preparations, adaptive label choice (exchange mode), the second law `μ′`, R-nl. Each
  such departure is a separate child node, taken in the owner's order (section 9).

L5 is first because it is the cheapest node whose answer can close or open a whole subclass, and
because MECH-1 Lemma A already bears on it. Its outcome may yield `FAIL-CLASS(𝓢)` for a subclass
only; by section 2.3 that is not a statement about the other subclasses.

**Expected outcome of L5.** This is an unreviewed expectation, not a result. It is the first
internal review's sketch [W], not evaluated in drafting:

1. By Lemma A(i)–(iii) [R], labels only translate the state. A label exchange is affine with a
   fixed linear part, so exchange mode is covered as well.
2. Under a law uniform on a coset, every record law is uniform on a coset of a subgroup that does
   not depend on the labels. The uniform law with a fixed `r_O` (in initial-condition mode, with
   fixed `r_O` and program blocks) is such a law, on both carriers.
3. Take two preparations whose prefixes have equal length and whose complete prefix records are
   fixed. Their continuation laws are equal for every continuation, or disjoint for every
   non-adaptive one, so their distinguishability is 0 or 1. What heralds and adaptivity change: a
   heralded or adaptive preparation is a mixture of such continuation laws, weighted over the
   accepted prefix records, and mixtures can have intermediate distances. What they do not
   change: the continuation laws given one complete prefix record are the extreme points, they are
   pairwise equal or disjoint (a simplex), and each is itself a heralded preparation, since D5
   admits the herald that accepts one complete prefix record. A near-pure state of `𝔔` is
   approximately extreme, so step 4 is applied to extreme preparations carrying most of the weight
   of preparations near `|a+⟩` and `|b+⟩`, at the conditional error of section 1.2. (This step
   records the delta review's comment on the sketch; unreviewed.)
4. Pad the prefixes to equal length with `c(0)`, and take states near the `|a+⟩`, `|b+⟩` of Q5
   and Q6. The comparator then needs a distinguishability bounded away from 0 and 1: two pure
   states with `Tr(P_a P_b) ∈ [1/4, 3/4]` have trace distance in `[1/2, √3/2]` [W]. That is a
   contradiction for `ε` below a small explicit constant, at `K₀ ≈ 3`.

**Gap in the sketch** (recorded, not resolved). The herald of step 3 that accepts one complete
prefix record can have `p_acc` exponentially small in the record length. By the `2 d_K / p_acc`
factor of section 1.2, Q2 at error `ε` then gives no control at conditional error `ε` for that
preparation, so the conclusion of step 4 for `ε` below a small explicit constant does not follow
from steps 3 and 4 as stated. Independently of `p_acc`, the subclass of the conclusion below has
no heralds, so the herald of step 3 is a device of the proof and not a protocol of that subclass,
and the Q-conditions stated for heralded preparations at conditional error cannot be invoked by
its proof [W]. Running steps 3 and 4 on joint prefix–continuation laws, without conditioning on one
complete record, is a route the delta review of r2 named, and it is needed in either case; it is
not worked out here.

MECH-1 records the same direction: "Any in-world source of setting selection must make the rule
non-affine in the joint state" (`mechanism-1-20261107/DESIGN.md`:434–435) [R].

If L5 confirms the sketch, with the gap above closed and after Lemma A has been re-derived under
choice 9(a), the node yields `FAIL-CLASS(R-lin, coset-uniform law, initial-condition mode, no
heralds)` for every `q` on both carriers. That subclass would be closed by the structure of R-lin's
record laws (step 1 uses R-lin's affinity), not by the obstruction of section 1.2, which the
program blocks remove. Whether any rule meets the initial-condition definitions is open; no
rule-independent obstruction is known, and none is excluded [W]. At L5 the argument is therefore
checked as a negative control is: the properties it uses are listed, each property that fails in
the third case with the step of the argument that uses it; the reviewer checks, as at M1 (section
3), that the argument uses no property it does not list and that the contradiction is not reached
without the properties that fail in the third case; and the listed properties are checked against
the third case of the proves-too-much check (section 3), and if every one holds there, the argument proves
too much and the step returns to the owner (section 7).
Exchange mode (under H-write), adaptivity and heralds are child nodes,
and the subclass is widened to each only when its own node is proved (steps 1 and 3). The R-lin
child nodes left open also include those under a law that is not uniform on a coset (choice 6): a
level set of the quadratic `E` (SM:296) (on `𝓛_fin`, in exchange mode), or a non-uniform product
law. Whether the
sketch extends to them is not settled. This is why choices 1 and 6 bear directly on the outcome.

**M4. The remaining branches**, depth-first, in the order the owner fixes.

- *Route N (obstruction) for a subclass `𝓢`.* State an invariant of the record theory that every
  member of `𝓢` preserves and that the qubit target violates at a fixed `(ε₀, K₀)`. Candidate
  sources of such invariants on `main`: MECH-1 Theorem W and Proposition C (stabilizer closure at
  odd prime `q` under the access posits P1–P3, `mechanism-1-20261107/DESIGN.md`:751–766) [R],
  whose hypotheses (Gross's frame, posited access) differ from D1–D7 and must be re-established
  or replaced, not assumed; apparatus-1 §5.3, the finite-carrier argument against exact `rot`
  (`apparatus-1-20261107/DESIGN.md`:955–1023) [R], which is about exactness and bears here only
  on the growth of `N` with `K`.
- *Route P (construction) for a subclass `𝓢`.* Exhibit a family in `𝓢`, prove D1–D7 from its
  specification and, for D6(b), its source ledger with the label encoder stated and every
  capacity statement its proofs rest on given with its proof, and prove Q0–Q6
  with explicit `N(ε, K)`. Every link is tagged; the C-SUP and
  C-MEAS checks are applied to the exhibited family before Q is attempted.

No mechanism is named here as a candidate. The proposal fixes what a construction must satisfy,
not what it is.

**M5. Verdict.** Fill in the two tables and compute the token by section 2.2.

**If the question cannot be decided on paper.** A later step, separately authorized, would need
exact computation: for R-lin (and R-nl if chosen) on small tori (for example `L ≤ 4`,
`q ∈ {2, 3}`) and small observer regions, the exact record laws of every label sequence up to a
small horizon under the reference law and `μ′`; from them the operational distance spectrum, the
capacity (Q1), the best fixed `d = 2` model (Q2) as an exact or certified optimization, and the
group induced on the operational quotient; with the controls C-POS-2, C-ISO-2 and C-FIN replayed in
the same harness as positive and negative controls; in exact integer or rational arithmetic, with a
frozen decision rule, as a native V3 round under §A.39. Nothing of this is planned to run in
Step 2.

***

## 5. Prior results that constrain the answer

Each row states what any `PASS-DERIVED` must be consistent with, and why the result does not decide
the question as posed. Layer tags are Step 1's.

| Result | Layer | What it excludes | Why it does not decide TUNE-1/Q2 | What a pass must respect |
|---|---|---|---|---|
| Configuration-basis obstructions: `substratumGen_not_control`, `obs_not_control`, `configurationLevel_not_qm` (Step 1 B.1, B.5) | K | Mixing in a matrix indexed by the configurations, for the monomial and sourced classes | Reading A; Q2 compares record laws, and the qubit is an image of an operational quotient, not a matrix over configurations. `operational-quotient-v3`: "not a map-independent no-go for all operational quotients" [R] | The OI-side operations stay nonnegativity-preserving at the configuration level; a pass must not imply configuration-indexed availability of `rot` or the quarter phase |
| `nonnegBounded_not_denseUnitaryControl` (OB/FrozenSourcing.lean:173–174) | K | Dense unitary control for a nonnegativity-bounded theory on the two-state carrier, where availability is conjugation by configuration-indexed matrices | The kernel statement is on `FiniteOperationalTheory (Fin 2)` with configuration-indexed availability; it is not an observer-level quotient no-go. Its extension to other carriers or interfaces is [W] (Step 1 C) and is not cited as kernel-checked | As above |
| `phaseQ_ne_heisQ` (OB/QuasilocalCharacterization.lean:792) | K | The one-site quarter phase as the automorphism of a reversible finite-range dynamics, on a lattice with any site set | Exactness, one dynamics, configuration algebra; no statement about approximation or a quotient | Same as row 1 |
| Counting: `countable_not_layerFlowExecutable` (OB/PolarizationClosure.lean:87–92) and the polarization closure audit (:54–85) | K | Exact flows in a class countable up to scalar | Exactness only. The same audit records non-Clifford operations of infinite order at finite level ("What it cannot contain is a continuum", :84–85; the infinite order of the hexagon product is from a numerical check, not proved, :233) | Q3 is approximate: a countable dense family is admissible |
| `flow_endpoint_refuted` (OB/FlowEndpoint.lean:149) | K | Sufficiency of a tunable flow for quantum mechanics | Not an obstruction; a necessity-only warning | Q1, Q5 and Q6 are required beside Q3 (controls C-ISO-1, C-ISO-2) |
| C5 discovery audit, O1 and O2 with countermodels (:25–37, :59–62) | K (as the audit reports) | — | Separation of two obligations at configuration level | `PARTIAL-REBIT` is reported apart; a pass needs Q3 and Q6 |
| Main:560, finite-substratum obstruction | P, P-imp | Exact reproduction of one qubit by one fixed finite realization | Exactness and fixed `N`; approximation by growing `N` is not excluded (Main:598) | `N(ε, K) → ∞` as `ε → 0` (C-CARD (a), L4 (b)) |
| Main:566, :582, :598, ε-realization and gluing | P | — | Positive, with the quantum rule supplied | Is control C-SUP-1; a pass may not resemble it in the respect D6 forbids |
| MECH-2 Lemma F, Theorem U2(ii), §6.4 (`mechanism-2-20261108/DESIGN.md`:307–345, :404–416, :901–911) | R | Encoded unitaries of infinite order under a fixed orthogonal injective frame with H-LIFT, for every dynamics on a finite set | Hypothesis on the identification (Step 1 B.12 (v)); D2 of Step 1 is the opening of non-injective encodings | L4 (a): the qubit image must be non-injective |
| MECH-1 Theorem W, Proposition C, Lemma A and its consequence (`mechanism-1-20261107/DESIGN.md`:404–435, :751–766) | R | Non-Clifford encoded unitaries for class N at odd prime `q` under P1–P3 in Gross's frame; non-translational setting dependence under one fixed affine rule | Posited access and a fixed frame; Lemma A is the input to L5 and bears on R-lin only | A pass on R-lin must be consistent with Lemma A, or show where its hypotheses fail |
| apparatus-1 Lemma 5, C-ROT and dense control (`apparatus-1-20261107/DESIGN.md`:731–784); §5.3 (:955–1023) | R | The encoded quarter phase and dense control in the one-cell frame R1 at `q = 2`; exact `rot` on any finite carrier | R1 and posits P1–P3; §5.3 is about exactness | The resource must grow with the horizon for an irrational angle [W, from §5.3's periodicity argument] |
| `whole-model-bridge.md` Proposition (:132–197) | R | Any fixed finite-dimensional quantum carrier for point preparations with a sign read | Out-of-class carrier and access (E-real, E-control) | The derived access must leave no read that separates more than two preparations (Q1) |
| `a2_depth_v7`, `a2_memory_v8` (`a2_memory_v8/REPORT.md`:26) | R | Depth-uniform agreement by one controller with finite persistent state and dyadic fresh bits on one protocol | One protocol and one controller class | `N(ε, K)` is stated as a function of `K`; a `K`-independent claim must show why the class does not apply |
| Arc D round 1, `padData_rooted` (OB/OperationalSourcing.lean:476; `PROGRAMME.md`:216) | K | Representation as evidence of a resource | — | Control C-REP |
| Stochastic observer-interface audit (:369–381) | K (ensemble leg) | — | The architecture fixes neither an observation map nor an ensemble | D4 removes the first choice (complete reads); H-μ names the second |
| Observer-level isotropy, SM Corollary 1a (SM:258–268; OB/CubicIsotropy.lean:116) | K | Quadratic anisotropy of a projected `O_h`-equivariant kernel | Classical and positive; isotropy is not the target | Controls C-ISO-1, C-ISO-2 |

**Openings this question uses** (Step 1 D). D2 (non-injective encodings): the qubit is a quotient
image. D7 (access as coarser operational equivalence), here derived from a region chosen once
rather than posited. D11 (an access quotient on a carrier with continuous mixing) in its finite
and approximate form, which Step 1 records as "not posed in any record read". D12 (approximation
by finite systems of growing size from ingredients other than the quantum rule). D1 (an infinite
underlying space) only under H-∞.

**Openings it does not use.** D10 (Q-B), which asks for an "additional OI principle"; D3
(input-correlated memory outside a carrier), except as it arises inside the fixed world; exact
forms.

***

## 6. Hard-to-vary statement (§A.29)

The question adopts no premise and is not a Layer-0 revision; the statement is made because the
owner asked for it. Studying R-nl under H-nl as a conditional does not adopt H-nl. Adopting H-nl
as a premise would be a Layer-0 revision under §A.29: it would replace ledger item (vii) for the
world's rule, and it would need, stated in advance, the existing results it preserves and at
least one independent prediction or postdiction beyond the problem it is built to fix, and it would
have to exclude any variant adjustable to fit any outcome. A TUNE-1
pass on R-nl would not by itself meet that requirement.

**What the investigation preserves.** Every row of section 5 stays true whatever the verdict, and
each is a control or a necessary condition of a pass (sections 3, 4 L4). In particular a pass
leaves every kernel obstruction on the configuration-basis interface intact, because it is stated
on the operational quotient.

**Where it could be varied, and how that is closed.** The rule is one fixed `F`; the ensemble is
one law (a generating prescription, D3) from the list fixed at M0, with a robustness check; the label menu is every configuration of `C`; the read
is the complete history of `O`. What remains existential is the shape of `O` and `C`, `τ`, the
generating rule `n ↦ I_n` and the comparator `𝔔`. These are fixed once for all targets and all
protocols (D1), and the comparator is a single `ℂ²` model, so they cannot be adjusted per outcome.
The label encoder is existential as well (Q1, Q3, Q5, Q6). It assigns labels of the fixed menu to
targets and changes the record law of no label, and D6(b), where it is applied (choice 11(a) or
(b)), tests what its labels hold.
Q4, Q5 and Q6 are not tuned by any of them: they are checks the family either passes or fails.

**Independent prediction or postdiction a pass would have to deliver.** None can be stated with
confidence in advance. Two candidates are named so that a pass can be held to them:

1. the error law `ε(N, K)` of the passing family, fixed by `F`, `q` and `μ` with no free
   parameter: a statement about how a finite apparatus departs from a qubit. A comparison with
   precision tests of single-qubit rotations would further need a bridge from the apparatus
   region to a laboratory apparatus, which this question does not supply;
2. what the same generating rule gives, unchanged, for two disjoint apparatus regions: whether
   the joint record theory composes as `ℂ² ⊗ ℂ²` or as a classical or other composite. This was
   not designed in and could fail. Its evaluation belongs to the separately gated Step 3.

If neither is stated and checked, a pass stands as a conditional consistency-axis result and moves
no correctness assessment (§A.23).

***

## 7. Scope, cost and stopping rule

**Scope.** Paper derivation only. No computation, no Lean build, no manuscript or Lean change, no
premise adopted, no GitHub comment by the writer. Records cited are read at the pin. A premise
taken from an [R] record is either re-derived in the unit or carried as a named condition (section
9, choice 9).

**Cost.** Bounded effort: by default at most three writer sessions for M1–M5 (section 9,
choice 10), each followed by a review, inside §A.40's resource limits.

**The step ends** at the first of:

- a token of section 2.1 computed by section 2.2;
- a red control (then `VOID`; the definitions go back to the owner before any further work);
- the effort bound (then `INCONCLUSIVE(gap)`, the gap stated as the exact lemma not proved).

**What happens next.** In every case the result goes to independent review and then to the owner.
No next step starts without the owner's recorded decision.

- `PASS-DERIVED`: the owner decides whether to open Step 3 (the measure question for H-μ,
  contextuality, composites and Bell, and the independent consequences of section 6), and whether
  a verification round is wanted.
- `FAIL-CLASS(𝓢)`: the owner decides whether to stop TUNE-1 or to pose a different question
  (another rule, ensemble or mode) under a new proposal.
- `PARTIAL-x` or `INCONCLUSIVE(gap)`: the owner decides whether to pursue the named gap, on paper
  or by a separately authorized computation (section 4, last paragraph).
- `VOID`: the owner decides on amended definitions.

***

## 8. Not part of this question

Exact rotations (B-exact); the Born rule's selection, including the justification of `μ`;
contextuality; Bell correlations; composite systems beyond the postdiction named in section 6;
reading A; real-valued sites, an isolated pair, a loaded coefficient or any added carrier;
growing alphabet size; any statement about OI's correctness; any manuscript change.

***

## 9. Open choices for the owner

Each choice has options, and every choice but the first has a recommendation. The choices are
fixed at M0 and are not reopened afterwards. Choices 1 and 6 very probably decide much of the
outcome by themselves, as follows. These are unreviewed expectations, not results.

1. **Which rule.** No recommendation: this choice decides what Step 2 can find.
   - (a) **R-lin only.** This is probably cheap, and it is probably negative. By the expectation
     recorded in M3, MECH-1 Lemma A with a law uniform on a coset gives record laws uniform on
     cosets of a label-independent subgroup. Then two equal-length preparations are
     distinguishable with probability exactly 0 or 1, while Q5 and Q6 need intermediate values.
     MECH-1 already concludes that in-world setting selection "must make the rule non-affine in
     the joint state" (:434–435) [R]. If L5 confirms this, with the gap recorded in M3 closed, (a)
     yields `FAIL-CLASS(R-lin, coset-uniform law, initial-condition mode, no heralds)` in
     essentially one node, with exchange mode, adaptivity and heralds as its child nodes (M3).
     That closes the subclass and leaves TUNE-1/Q2 open for every other rule. Inside R-lin, only
     a law not uniform on a coset escapes the sketch (choice 6).
     No new premise is involved: R-lin is the rule of ledger items (vii) and (xiii).
   - (b) **R-lin first (L5), then R-nl as a separate verdict.**
   - (c) **R-nl only.** Here the question is actually open. R-nl is non-affine, so Lemma A and the
     sketch do not apply to it. Section 1.1 gives what `main` states about R-nl: a candidate
     realization used for numerical motivation of ledger item (v) (Main:726; SM:294, :298,
     :1416), with chaos diagnostics that are numerical evidence only; nothing about its record
     laws through a region or its computational capacity. Because it is a candidate and not a
     ledger posit (it does not meet item (vii)), it enters only under the named hypothesis H-nl,
     not adopted, and carried into every conclusion. A verdict on R-nl is then a statement about
     a rule `main` does not posit. It says nothing about the ledger's linear rule, and the R-lin
     verdict says nothing about R-nl. Within "no new physical premise" (Issue #1236) this is
     admissible only as a conditional study, in the way H-∞ is. It is the owner's decision whether
     that is wanted. Cost: open-ended within the effort bound (choice 10). Because R-nl's
     computational capacity is unknown, choice 11 bears on it.
   - (d) **Both together**, each with its own token.
2. **Alphabet.** (a) Statements for each fixed `q ≥ 2`; (b) `q = 2` only (Main §3.2's instance);
   (c) a family in growing `q`. *Recommendation: (a)*, with `q = 2` first. (c) needs the
   correspondence between alphabets SM §2.7 leaves unbuilt.
3. **World.** (a) Finite tori only; (b) finite tori, and the infinite lattice under the named
   hypothesis H-∞ as a separately labelled conditional result, with its own token
   (`PASS-DERIVED[…, 𝓛_∞, …, … | H-μ, H-∞, …]`, or a `FAIL-CLASS` naming `𝓛_∞`).
   *Recommendation: (b).* It honours "finite observational access" not implying "finite
   underlying dynamics" without adopting an infinite world.
4. **Error measure and horizon.** (a) Total variation on complete records over all protocols of
   horizon `K`, for every `K`, with `N(ε, K)` explicit; (b) the same for one fixed `K` (for
   example `K = 3`, as in `finite-a2-v5`) as the target. *Recommendation: (a)* as the pass
   condition, a fixed-`K` result reported as `PARTIAL-FIXEDK`. The owner's Q-B record asks that
   errors under repetition, adaptive measurement and recombination be controlled (Step 1 F.2).
5. **How the observer chooses.** (a) Exchange mode with adaptive protocols (label choice may
   depend on earlier records), heralded preparations allowed with raw rates, conditional on the
   named hypothesis H-write: the label register, its reset and the per-round writes are a
   classical write access counted in the apparatus and the record (section 1.2), not obtained from
   `Φ_F`; (b) initial-condition mode only (every choice an initial condition, stored in program
   blocks outside `O`; no adaptivity; heralds allowed with raw rates), the strictly rule-only
   target; (c) both, reported separately, each with its own token.
   *Recommendation: (c).* (b) is the strictly rule-only target, and only its token is a result
   about the rule alone; (a) is the form Main §3.4 and Gate A use, adds adaptivity, and its token
   carries H-write. `obs_exchangesAvailable` does not discharge H-write: the observer theory it is
   stated for does not depend on `F` (`obsTheory_rule_independent`, section 1.2) [K].
   *Not offered: the program inside `O`.* In (b) the settings could instead be stored inside `O`,
   in one of two variants. In the first, each round's instrument depends on its own label alone,
   and the label cells are excluded from the records or conditioned on. In the second, the
   comparator is given the whole label sequence in advance, each round's instrument a function of
   every label of the protocol. Neither is offered, for two reasons [W]. In the first variant,
   label content that `Φ_F` carries within one tick into cells of `O` that are not label cells
   separates protocols as in section 1.2 wherever it arrives unmasked by unread cells, unless
   reads are restricted, which D4 and D5 forbid. In the second, the model is chosen per experiment
   and does not preserve sequential composition,
   which `endpoints.md`:67 [R] excludes. And since initial-condition protocols are non-adaptive
   already, neither would add adaptivity. What the program blocks outside `O` cost instead: in a
   layout that meets the distance condition of section 1.2, each later label `c_j` starts at graph
   distance greater than `(j − 1)τ` from `O` and reaches it only
   through unread cells, distributed by `μ` outside the program blocks, so initial-condition mode
   also tests whether `Φ_F` carries a label through the unread world [W]. Adopting either variant
   is the owner's choice; it would change what "rule-only" means, from "every choice is an initial
   condition of unread cells" to "the apparatus region holds its program" (in the second variant,
   "and the comparator is told it"), and it would need its own definitions and controls.
6. **Ensemble.** For R-lin, this choice probably decides the outcome. By the expectation recorded
   in M3, with the gap recorded there closed, a law uniform on a coset gives `FAIL-CLASS` for
   R-lin, and the uniform law is such a law, so requiring it is the premise that decides R-lin.
   Requiring it is not part of the owner's question. The list of section 1.3 (D3): the uniform
   law; the level-set law of D3 (SM:296); a translation- and `O_h`-invariant product law with a
   non-uniform site marginal.
   - (i) *Which law a pass must hold under.* (a) The uniform law, as the mandatory reference,
     and `μ′`. (b) One law of the list, declared at M0, and `μ′ ≠` that law. (c) Every law of the
     list, each reported with its own token; under D3's robustness clause, a pass under one law
     then counts as derived only if it also holds under a second law of the list.
     *Recommendation: (c).* No law is then picked after the results are known, and the
     uniform-law row is reported whatever the others give. Main's ledger item (iv) bears on (a)
     only through the [W] reading recorded in D3. Under (a) with choice 1(a), the expected outcome,
     with the gap recorded in M3 closed, is `FAIL-CLASS`.
   - (ii) *The second law `μ′`, if (a) or (b).* (a) The level-set law on `𝓛_fin` in exchange
     mode, and on `ℤ^3` and in initial-condition mode the law (iii) puts in its place (the
     non-uniform product law, unless that is already the other law). The level-set law is defined
     on `𝓛_fin` only, and is not offered in initial-condition mode (D3): the uniform
     law on one level set of `E` on the whole world `X_{Λ_L}`, a finite set, with the level value
     fixed as in D3 and with the same symmetries as the uniform law. There it is invariant under
     R-lin's free dynamics, because `E` is conserved on the torus (SM:296) [P]; the time-zero law
     on `Λ ∖ O` with `r_O` fixed is a conditional of it and is not invariant, and label exchanges
     change `E` [W]. The tested level sets are not invariant under R-nl (SM:1416) [P]. On `ℤ^3` it
     is undefined: no limit construction is given here, and one would be a new definition, tagged
     [W]. (b) The non-uniform product law; (c) the uniform law, under (i)(b) only.
     *Recommendation: (a)*, for the reasons given. Whenever the uniform law is one of the two laws
     a pass must hold under, R-lin is decided as above whatever the other law is.
   - (iii) *On `ℤ^3`, and in initial-condition mode.* Under (i)(a) or (b), wherever an option of
     (i) or (ii) names the level-set law, the non-uniform product law takes its place there, or
     the uniform (product) law if the non-uniform product law is already the other of the two
     laws. Under (i)(c), the level-set row on `ℤ^3`, and in initial-condition mode, is entered as
     "not defined", not as a token. No option therefore makes a pass on `𝓛_∞`, or in
     initial-condition mode, undefinable.
7. **Rebit or qubit.** (a) A pass requires the whole Bloch ball (Q6); (b) a disk suffices.
   *Recommendation: (a)*, with a disk reported as `PARTIAL-REBIT`. The owner asked for one
   quantum bit, and a disk is real quantum theory.
8. **Partial results.** (a) Report the `PARTIAL-x` tokens, each labelled as not answering the
   question; (b) report only the final token. *Recommendation: (a).*
9. **Premises from unreviewed records in a negative.** (a) Re-derive in the unit every [R]
   statement a `FAIL-CLASS` uses (MECH-1 Lemma A, MECH-2 Lemma F); (b) cite them and state the
   negative as conditional on them. *Recommendation: (a)*, so that a negative does not rest on an
   unverified premise (§A.46 item 7).
10. **Effort bound.** (a) Three writer sessions with reviews; (b) another bound.
    *Recommendation: (a).*
11. **Compiled simulators.** The question is how a family is classified when it meets Q0–Q6 for
    every `(ε, K)` and fails only D6(b), because its ready configuration, its generating rule or
    its label encoder (the labels, and in initial-condition mode the content of the program
    blocks)
    implements a qubit simulator or a Born- or cosine-law sampler. This choice fixes the D6(b)
    entries of controls C-PROG and C-PROG-P; the token of each is `OPERATIONAL-ONLY` under every
    option, because each fails D7 (section 3). The choice is how such a family is classed, not
    where its program is held or how its encoder is presented: under (a) and (b) the outcome of
    D6(b) is the same for a program in `r_O`, in the labels or in the program blocks, and for a
    label that is exhibited or only shown to exist, and under (c) test (b) is applied to none of
    them (section 1.3). For a rule that executes a program delivered through its labels,
    section 1.3 (*A rule that interprets*) states the token under each option.
    (a) Supplied (`OPERATIONAL-ONLY`). The quantum rule is in the hidden state or in the settings, as in Main's
    single controlled dynamics (Main:582), whether it is placed there by declaration or compiled into
    `r_O`, the labels or the program blocks. (b) A separate token `PASS-COMPILED` for a family that meets D7 and fails only D6(b),
    reported apart and never a pass of TUNE-1/Q2. It records that the rule can host such a
    simulator, held in a region chosen once or delivered through the labels, which is a statement about the rule's computational
    capacity. (c) Derived (`PASS-DERIVED`): D6 consists of test (a) alone, and test (b) is not
    applied. A family on a rule of 𝓡 that meets Q0–Q6 for every `(ε, K)` and every other
    D-clause by holding a qubit simulator in `r_O`, or by delivering one through its labels or
    program blocks, is then a pass of TUNE-1/Q2, and no control separates it from a family whose
    proofs encode nothing: under this option C-PROG and C-PROG-P exercise D7 alone.
    *Recommendation: (a)*: a compiled
    simulator is the hand-choice of Step 1 made through the ready configuration or the labels. Under (a), any
    such family found is still recorded with its classification (section 2.2), so the
    information (b) would carry is kept.

***

## 10. Disclosure and review status

- **No computation was run.** Commands used in drafting r1: `git` (rev-parse, status, log,
  merge-base, branch, add, commit, push), `grep`, `sed`, `awk`, `cut`, `tr`, `wc`, `ls`, `find`,
  `head`, `tail`, `df`, `sha256sum`. `python3` was invoked once by mistake, with the one-line
  script `print(1)`, output discarded; it computed nothing about any OI rule. Commands used in
  drafting r2: `git` (status, log, show, ls-tree, diff, add, commit, push), `grep`, `sed`, `cut`,
  `fold`, `diff`, `wc`, `ls`, `sha256sum`. No interpreter was run in r2. Commands used in drafting
  r3: `git` (status, rev-parse, branch, show, diff, add, commit, push), `sed`, `cut`, `grep`,
  `sort`, `head`, `wc`, `df`, `sha256sum`. No interpreter was run in r3. Commands used in drafting
  r4: `git` (status, log, branch, ls-tree, show, diff, add, commit, push), `grep`, `sed`, `cut`,
  `fold`, `cat`, `awk`, `head`, `wc`, `ls`, `sha256sum`. No interpreter was run in r4. Commands
  used in drafting r5: `git` (rev-parse, status, log, ls-tree, cat-file, show, diff, add, commit,
  push), `grep`, `sed`, `awk`, `cut`, `cat`, `head`, `tail`, `tee`, `mv`, `wc`, `sha256sum`.
  `python3 --version` was invoked once, printing the interpreter's version only; it ran no script
  and computed nothing about any OI rule. Commands used in drafting r6: `git` (status,
  rev-parse, log, show, add, commit, push), `grep`, `sed`, `cut`, `wc`, `df`, `sha256sum`.
  `python3 --version` was invoked once in r6, printing the interpreter's version only; it ran no
  script and computed nothing about any OI rule. Commands used in drafting r7: `git` (rev-parse,
  status, branch, log, diff, add, commit, push), `grep`, `cut`, `sed`, `ls`, `df`, `wc`,
  `sha256sum`. No interpreter was run in r7. Commands used in drafting r8: `git` (rev-parse,
  status, branch, diff, add, commit, push), `grep`, `ls`, `sed`, `wc`, `sha256sum`. No interpreter
  was run in r8. Commands used in drafting r8a: `git` (rev-parse, status, branch, add, commit,
  push), `grep`, `cut`, `sed`, `cat`, `sha256sum`. No interpreter was run in r8a. Commands used
  in drafting r9: `git` (status, rev-parse, branch, log, ls-files, diff, add, commit, push),
  `grep`, `cut`, `sed`, `ls`, `wc`, `sha256sum`. No interpreter was run in r9. Commands used
  in drafting r10: `git` (status, log, rev-parse, show, ls-files, diff, add, commit, push),
  `grep`, `sed`, `cut`, `fold`, `sort`, `uniq`, `cat`, `head`, `ls`, `wc`, `sha256sum`. No
  interpreter was run in r10. Commands used in drafting r10a: `git` (status, rev-parse, branch,
  diff, add, commit, push), `grep`, `cut`, `head`, `tail`, `wc`, `sha256sum`. No interpreter was
  run in r10a.
  No probe, checker or Lean build. No GitHub comment.
- **Read for r10a:** the delta review of `4b6b4460` (in full). No further record was read.
- **Read for r10:** the delta review of `80a012b2` (in full); at the pin, `papers/Main.md`:582.
- **Read for r9:** the required change and the two nonblocking notes of the external re-review
  of `7a9e7b79` (PR #1237, review 5867105524), as relayed to the writer verbatim; the rest of
  that review was not read. At the pin, `finite-a2-v5/REPORT.md`:9–24.
- **Read for r8a:** the delta review of `535688ca` (in full). No further record was read.
- **Read for r8:** the delta review of `2ad0aca0` (in full). No further record was read.
- **Read for r7:** the delta review of `b9e9683e` (in full). No further record was read.
- **Read for r6:** the external review of `9440f8af` (in full); at the pin,
  OB/SubstratumInterfaceAudit.lean:1–37 and :765–830 and OB/RouteB.lean:125–129
  (`ExchangesAvailable`).
- **Read for r5:** the delta review of `57783cbc` (in full); at the pin,
  `finite-a2-v5/REPORT.md` (whole) and `history-architecture-v5/REPORT.md`:9–20, :34–68 and
  :295–320.
- **Read for r4:** the delta review of `b47700a6` (in full) and the delta review of `81f50bd0`
  (its nits); at the pin, `finite-a2-v5/REPORT.md`:1–8, :9–60 and :86–88,
  `oi-qm-ext-1/measurement-source.md`:29, :57–63, :87, :118, :141, and `papers/SM.md`:296.
- **Read for r3:** the delta review of `81f50bd0` (in full); at the pin, `papers/SM.md`:296 and
  :1416.
- **Read for r2**, at the pin: the first internal review of `9312b805` (in full);
  `papers/SM.md`:290–298 and the sentences of :811, :1225, :1227 and :1416 that name the rounded
  rule; `papers/Main.md`:582 and :726 (the posit ledger, in full) and the opening of :564;
  `mechanism-1-20261107/DESIGN.md`:92–100, :404–440, :990–1004;
  `finite-a2-v5/REPORT.md`:1–45; `oi-qm-ext-1/measurement-source.md`, only the lines located by
  search and cited in C-MEAS and D3 (:29, :32, :57–63, :73, :87, :118, :141, :148, :160); Step 1
  B (the owner's three classes) and its summary item 3.
- **Read for this proposal**, at the pin: Step 1 (its summary, A.1–A.4, B.0–B.12, C, D, F.1,
  F.2); `apparatus-1-20261107/DESIGN.md`:725–790, :955–1025, :1072–1090; `mechanism-1-20261107/
  DESIGN.md`:92–100, :211–243, :404–440, :751–770, :1060–1080; `mechanism-2-20261108/DESIGN.md`:
  305–345, :400–420, :737–756, :810–830, :901–912; `oi-qm-ext-1/two-mode-drive.md` (whole);
  `oi-qm-ext-1/whole-model-bridge.md`:1–48, :132–307; `oi-qm-ext-1/endpoints.md` (the lines
  cited); `c5-discovery-audit.md`:25–65; `polarization-closure-audit.md`:50–90;
  `observation-context-protocol.md` (whole); `PROGRAMME.md`:216; the statements cited in
  OB/FrozenSourcing.lean, OB/DiscreteCompletion.lean:40–62, OB/SecondOrderDrive.lean:339; Main:4,
  :268, :554, :564, :566, :582, :584, :590, :596, :598, :602, :726; SM:88–90, :256–270, :294–298;
  the lines of the `states-dynamics-audit-20261024` reports cited. Statements whose line numbers
  were located by search and not read in full are the Lean names listed in sections 3 and 5 other
  than those above, and the record lines cited from Step 1's tables.
- **Not done:** Step 2 itself; any evaluation of L5 or of any family (the M3 sketch is the
  first internal review's, recorded and not checked); any check that the controls behave as
  expected (that is M1).
- **Review status.** r1 (`9312b805`) received one fresh internal review (same model family,
  verdict REVISE, three blocking findings and twelve nits). r2 (`81f50bd0`) received a fresh
  delta review (same model family, verdict REVISE, two blocking findings and seven nits). r3
  (`b47700a6`) received a fresh delta review (same model family, verdict REVISE, light, three
  blocking findings and nine nits). r4 (`57783cbc`) received a fresh delta review (same model
  family, verdict REVISE, light, one blocking finding and seven nits). r5 (`c3a0ebf7`)
  received a fresh delta review (same model family, verdict ACCEPT WITH NITS, no blocking
  findings and four nits), and r5a (`9440f8af`) applied the four nits. r5a received the external
  ChatGPT review (verdict REVISE, two blocking findings, B1 on the composition test and B2 on
  write access, and three precision requests), and r6 (`b9e9683e`) applied all five. r6 received a
  fresh delta review (same model family, verdict REVISE, one blocking finding, B-r6-1 on
  initial-condition mode, and six nits), and r7 (`2ad0aca0`) applied the finding and the nits. r7
  received a fresh delta review (same model family, verdict REVISE, light, one blocking finding,
  B-r7-1 on M3's statement about initial-condition mode, and five nits), and r8 (`535688ca`)
  applied the finding and the nits. r8 received a fresh delta review (same model family, verdict
  ACCEPT WITH NITS, no blocking findings and four nits), and r8a (`7a9e7b79`) applied the four
  nits. r8a received the external ChatGPT re-review (verdict REVISE, one blocking finding, on the
  label encoder and the program blocks under D6, and two nonblocking notes), and r9 (`80a012b2`)
  applied the finding and both notes. r9 received a fresh delta review (same model family,
  verdict REVISE, light, one blocking finding, B-r9-1 on capacity statements cited in existence
  form and the missing default class, and eight nits), and r10 (`4b6b4460`) applied the finding
  and seven of the nits; the eighth, marked optional, was not applied as proposed, and the
  two-way check of section 3 states what no control exercises. r10 received a fresh delta review
  (same model family, verdict ACCEPT WITH NITS, no blocking findings and nine nits), and this
  revision r10a applies the nine nits. Its changes have had no review; it needs the external
  ChatGPT re-review before it goes to the owner for approval.

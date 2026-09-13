# Hydrodynamics round H-D — the status of A5 relative to the hydrodynamic target: CONTROL PLANE

Owner-called, under `../PROGRAMME.md`. This file is the whole of round H-D's control plane and is
merged **alone**, before any execution object exists. The round is an **adjudication and sourcing**
round, not a construction round: it audits one condition, A5, and answers **three independent
questions** about it — whether observational incompleteness itself requires it, where and how
specifically the quantum route uses it, and whether any step of the hydrodynamic ladder requires it.
It constructs no substratum, proves no hydrodynamic statement, and writes no Lean.

**The three questions are answered independently and may disagree.** They are not three values of
one label, not a partition, and not two axes: each has its own targets, its own evidence standard
and its own permitted outcomes, and **no answer to one may be inferred from an answer to another**
(hazard 17).

**The round label `H-D` is an identifier, not an ordinal**, in the sense of the repository's rule
that claim IDs are identifiers. Executing it before `../PROGRAMME.md` §6's H-C entry is not a
reordering of the H1–H7 ladder: H-D asks a question about the ladder's inputs, and the ladder is
untouched by it. **`H-D` the round label is not `HD` the outcome label** ("Derived") of the
programme's §4 taxonomy; the round applies no taxonomy label to A5 at all (hazard 6, status
rule 8). The round's targets carry the prefix `A5S` for that reason.

**Blob identity is authoritative.** The result note pins this file by content.

**Parallel-track separation.** This round runs on its own branch from `main` at
`be2ec3667ccfe6c03d4bfb00ad4d7ccfe5b25994`. It neither consumes nor produces evidence for the
OI → QM chain (Track B, Track I), for Bell, or for gravity; the programme's control 1 applies in
full. It reads the OI → QM chain's manuscript sources **as the location of a condition's warrant**,
which is a source-audit reading and not an import of evidence (hazard 12).

## Start state

| | |
| --- | --- |
| Merged `main` | `be2ec3667ccfe6c03d4bfb00ad4d7ccfe5b25994` (PR #615) |
| The programme roadmap | `../PROGRAMME.md`, blob `b7b24112a462aee083c3e8f3c2980283b38cd10f` — consumed as the taxonomy, the H1–H7 obligation list and the round list; its §8 one-line state and its status-base line are not edited by this PR |
| Round H-A, the frozen control plane | `../round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` — the format model for a source-audit round; the `H0` linearity gate, the `H1` `q`-gauge test, the `H2b` stencil finding |
| Round H-A, the result | `../round-h-a-source-audit/result.md`, blob `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` — the first executed data point |
| Round H-B, the frozen control plane | `../round-h-b-reversible-fluid-substratum/preregistration.md`, blob `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` — the frozen candidate, the status rule this round's status rule is modelled on, the owner question this round takes up |
| Round H-B, the result | `../round-h-b-reversible-fluid-substratum/result.md`, blob `dc03b582ed718d374c471b27403b282a295d5c85` — the second executed data point |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `Substratum`, `shiftBy`, `A1`, `A2`, `A3`, `A3Family`, `A4Exact`, `A4`, `A5`, `a1_of_finite`, `a2_every_substratum`, `a3_of_fintype`, `a4_of_exact`, `waveSubstratum`, `waveSubstratum_A1`–`waveSubstratum_A5` |
| Round H-A's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean`, blob `fd5f54d8cbba4f68b67335c111d39a2add0c642f` — `map_zero_of_additive`, `coarse_evolution_additive`, `coarseCloses_additive_on_range`, `coarseCloses_nsmul`, `wave_coarse_evolution_additive`, `wave_coarseCloses_additive_on_range`, `CoarseCloses`, `totalSum`, `blockSum`, `axisMoment4` and its lemmas |
| Round H-B's module | `verification/lean-mathlib/OIBridge/HexLatticeGas.lean`, blob `374db0387337960888a67f4e98609446c8a1b871` — `hexSubstratum`, `hexSubstratum_A1`–`hexSubstratum_A4`, `hexSubstratum_A5_witness`, `hexSubstratum_not_A5`, `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`, `hexSum_leap_sector`, `hexMoment4_isotropic`, `hexGas_hexRot` |
| The manuscript-axiom audit, kernel side | `verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean`, blob `f7befdc7b5e814677e6220d91e06fc35b8950c49` — the determination that no manuscript-level conjunct of A1–A6 is a faithful predicate of the bare operational theory; `A1Realized`, `A2Realized`, `A1A2Realized` |
| The manuscript-axiom audit, prose side | `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` |
| The A6 definition round | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` — `A6Inv`, `A6Cov`, `A6Glob`, `A6-sd`, and the record that the singleton-`K` rescalings of the wave carrier are the A5 amplitude-scale freedom |
| The A5-consuming interface audit outside hydrodynamics | `verification/lean-mathlib/OIBridge/StochasticInterface.lean`, blob `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` — `phi_fixes_zero`, `ensemble_underdetermined` and the results taking `𝒮.A5` as a hypothesis |
| The substratum axioms and their status notes | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — §3.1's E1–E7 and A1–A6 with their parenthetical statuses; §3.6's hypothesis-dependency remark; §4 Theorem 24, its amplitude-scale-gauge remark, that remark's *Status* note and its formalization-status note on the linearity step |
| The rule, the gauge principles and the linearity lemma | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — §2.7 "The alphabet as gauge freedom"; §4.1 "Observer-level propagation and the lattice Klein–Gordon branch", its wave-equation uniqueness and its amplitude-scale-gauge lemma; §4.6's multiplicity reduction |
| The observation hierarchy and the observer-admission conditions | `papers/Structure.md`, blob `dd5432d70b2a4ab2238a08ea0f30a5101d6ac898` — §2.1's Levels A, B, C, D; C1–C4 as it states them; §9.6's Definition 9.9, Proposition 9.10 and Corollary 9.11; the per-level statement of what A1–A6 are conditions for |
| The observation axiom and the admission conditions at source | `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` — §1 and §3 |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `bb689f5072d9f146c71a6a1750c12add08c46e20` — `R7-HYA`, `R7-HYB` and their archive pins, consumed as context and not modified |

## The frozen objects, part 1 — A1–A6 as the kernel states them

Consumed unmodified from `SubstratumInterfaceAudit.lean`. `𝒮 : Substratum` carries a site type `ι`
(an additive group with decidable equality), an alphabet `V` (an additive group), and a
finite-range second-order rule `R : Rule ι V`; `Conf := ι → V × V` and `φ := leapEquiv R.F`.

| | kernel statement | note carried by the kernel |
| --- | --- | --- |
| `A1` | `Finite 𝒮.Conf` | holds for finite sites and alphabet, `a1_of_finite` |
| `A2` | `Function.Bijective 𝒮.φ` | holds for **every** substratum of the structure, `a2_every_substratum` |
| `A3 D` | `∀ i, (𝒮.R.N i).card ≤ D` | vacuous at one finite lattice (`a3_of_fintype`); the content is the family form `A3Family` |
| `A4Exact` | `∀ v c, 𝒮.R.F (shiftBy v c) = shiftBy v (𝒮.R.F c)` | `A4 ⊥` follows, `a4_of_exact` |
| `A4 G` | center independence up to the gauge `G : Subgroup (Equiv.Perm 𝒮.Conf)` | the gauge is a parameter |
| **`A5`** | **`∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'`** | **additivity of the rule over the alphabet** |
| `A6` | **no predicate**; the `ROADMAP` carries it as a `GAP` | four readings are frozen in `BackgroundIndependence.lean` and none is adopted |

**The kernel's A5 is additivity of `F`; the manuscripts' A5 is linearity of the wave equation.**
These are two statements, related by the kernel's instance theorem `waveSubstratum_A5` for the one
rule where both are in play. **No identification theorem between them exists in the tree, and this
round does not build one** (`A5S-0a`, hazard 11).

## The frozen objects, part 2 — where each condition is sourced in the manuscripts

All six are introduced at [Substratum §3.1] under the heading **Structural assumptions**, as
*restrictions on the class of candidate substrates* `(S, φ)`, alongside the empirical inputs E1–E7,
as **inputs to the reconstruction theorem**. Each carries a parenthetical status note in that
section, and the round consumes those notes as written.

| | [Substratum §3.1] statement | the status the section attaches |
| --- | --- | --- |
| A1 | finiteness of `S` | two-part: an E3 dimension-cutoff reading bounding what observation reaches, plus a gauge choice of representative under Theorem 24 (iii) |
| A2 | `φ` a bijection | two-part: partly structural, partly anchored by one empirical input, the observed unitarity |
| A3 | bounded coupling degree | required for locality and a coupling graph of well-defined dimension; the specific degree is gauge (Theorem 24 (iv)) |
| A4 | center independence | required to derive the wave equation in Stage 2; anchored by the homogeneity of physical law |
| **A5** | **linearity of the wave equation** | **equivalent to amplitude-scale gauge invariance via [SM §4.1]'s linearity-equivalence lemma; necessary *given* that gauge principle, and "partly derived" in exactly that sense; the entailment question from [SM §2.7]'s `q`-size freedom carried as an identified open step** |
| A6 | background independence | the promotion of the global commutant symmetry to local gauge invariance is a derivation step ([SM §3.1]), not part of the assumption |

[Substratum §3.1]'s closing paragraph records that the set A1–A6 is sufficient for the
reconstruction and that its independence is not established, and that A4 and A6 overlap in physical
content; [Substratum §3.6]'s hypothesis-dependency remark records that A5 is the strongest
restriction — equivalent to amplitude-scale gauge invariance, "so nonlinear wave equations on
finite lattices are the separate class one obtains exactly when that gauge principle is dropped."

[Substratum §4]'s amplitude-scale-gauge remark is named there as that principle's "single
authoritative home", and its *Status* note records the principle as **adjoined as an explicit
operational principle**, not one of Theorem 24's four generators, so that "the results invoking it
are conditional on it", with "the status of an operational input on a par with center independence
and isotropy, not a theorem". Its formalization-status note on the linearity step records the
outcome in the framework's three-tier classification: linearity is **not** promoted to a forced
(Tier-1) consequence; it is a **Tier-3 definitional stipulation**, sharpened by replacing the bare
assumption of linear dynamics with the assumption that the alphabet's additive automorphisms are
gauge, from which linearity follows.

[Structure §2.1] places the whole list: A1–A6 are Level D — the conditions by which the framework
selects its specific universality class and representative — and it states of A3–A6 that they are
"pure class-specific: required for OI's specific gauge-structure derivation, not necessary for
observer-admission", observer-admission being Level B's C1–C4.

## The frozen objects, part 3 — the two executed data points

**Round H-A** (`../round-h-a-source-audit/result.md`) audited the manuscripts' wave representative,
which satisfies A5 (`waveSubstratum_A5`). Its `H0` linearity gate takes A5 as its hypothesis
(`coarse_evolution_additive`, `coarseCloses_additive_on_range`) and returns: under `ZMod q`-linear
coarse variables no closed coarse description carries an advective term — **HI for the advection
obligation, conditional on that coarse-variable class**, with real-valued and nonlinear coarse
variables **HO**. Its `H1` returned HI for the total-sum candidate field under the `q`-gauge
principle and HO for every other candidate field; its `H2b` proved the axis stencil's fourth moment
anisotropic, conditional HI if H5's stress closure consumes that tensor and otherwise HO; `H3` and
`H4` are HO.

**Round H-B** (`../round-h-b-reversible-fluid-substratum/result.md`) executed one frozen candidate
inside the same `Substratum` interface: a six-channel Boolean streaming-and-collision gas on the
`L × L` periodic lattice in the hexagonal basis. It satisfies `A1`, `A2`, `A3 6` and `A4Exact`, and
**fails `A5`** with a witness pinned by equation (`hexSubstratum_A5_witness`,
`hexSubstratum_not_A5`). On its invariant graph sector it carries **exactly conserved mass and both
momentum components, on every configuration for every lattice size**, these being the only
conserved site-independent channel-weighted totals; its stencil's fourth moment is
**rotation-isotropic** and its sixth is not; it commutes with the lattice's `60°` rotation. Its
frozen status rule forbade reporting H-B closed, forbade any label written "for OI", and recorded
as **open** whether the A1–A4, ¬A5 class is admissible as an OI substratum.

**THE GUARDRAIL ON H-B, FROZEN, and carried wherever H-B is consumed:**

> **H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with the right
> microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
> Euler/Navier–Stokes limit.**

This sentence is the round's central scientific guardrail. It appears as status rule 2, it is
attached to `A5S-3b` where H-B's results are read, it binds `A5S-4a`'s report, and it is repeated
in the allowed final report. **The round may not be read as having obtained the stronger sentence
from H-B alone, and no execution artifact may state the stronger sentence on H-B's evidence**
(hazard 16, the evidence bar of status rule 6).

**Those two rounds are the round's data, and the round adds no third data point.**

## The round's organizing frame — three obligation sets, separated

The frame is the round's bookkeeping over obligations, and it is what makes the three questions
askable separately. It is **not a theorem, not a new condition, and not a claim that the three sets
are disjoint or nested**: a condition may sit in more than one set or in none.

### Set 1 — bare OI requirements

Conditions genuinely required by observational incompleteness itself. **Precise meaning here:** a
condition `X` is a bare-OI requirement iff every substratum admissible under observational
incompleteness satisfies `X` — admissibility being what [Main §1]'s observation axiom and
[Main §3]'s observer-admission conditions C1–C4 impose, as [Structure §2.1] Levels A and B state
them and [Structure §9.6]'s Definition 9.9 formalizes observer-admission. On the kernel side this
set lives at the interface that carries no distinguished substratum — the finite operational
theory, the sealed OI core and `DerivedOICore` — where `ManuscriptAxioms.lean` records that no
manuscript-level conjunct of A1–A6 is a faithful predicate of the bare theory, A1 and A2 having
realized-core *images* and A3–A6 having neither images nor weakened predicates.

### Set 2 — QM completion requirements

Conditions needed specifically to obtain finite operational quantum mechanics or the quantum
substratum structure. **Precise meaning here:** a condition `X` is a QM completion requirement iff
a step of the reconstruction chain consumes it — [Substratum §3.1]'s input list, [Substratum §3.5]'s
Theorem 23, Stage 2's derivations, [SM §4.1]'s wave-equation uniqueness and amplitude-scale-gauge
lemma, [SM §4.6]'s multiplicity reduction — or, on the kernel side, a module of the OI → QM chain
takes it as a hypothesis. [Structure §2.1]'s Level D is this set's manuscript name.

### Set 3 — hydrodynamic requirements

Conservation, locality, isotropy, mixing/local equilibrium, scaling and the rest, needed
specifically for Euler/Navier–Stokes. **Precise meaning here:** a condition `X` is a hydrodynamic
requirement iff one of `../PROGRAMME.md` §3's obligations H1–H7 requires it — in the obligation as
stated, or in a derivation that closes it — or a round executed under the programme consumed it in
closing one. The executed instances are H-A's `H0`–`H4a` and H-B's `HB0`–`HB3`. **The obligations
H3–H7 are `HO` and no derivation closes them**, which is why question (c) below carries its own
evidence bar rather than resting on the statements as written.

**What the frame is for.** The programme's §3 ladder asks what a Navier–Stokes limit needs.
Membership in the A-list records that the reconstruction takes the condition as one of its inputs;
that record settles nothing about sets 1 and 3, and importing a condition into the hydrodynamics
programme on the strength of its A-list membership alone is the inference this frame is built to
block. This round performs, for A5 and for A5 only, the necessity analysis the separation calls
for. **The frame is applied to no other condition in this round**: A1, A2, A3, A4 and A6 are not
adjudicated here, and their appearance in the tables above is sourcing, not classification.

## Why this round exists, and the scope of what it delivers

H-B's candidate carries, at the scope H-B reports them, the H1 obligation's conservation content —
exact local conservation of mass and momentum on its sector — and the H2 obligation's
stencil-tensor content — fourth-order isotropy — and the same candidate fails A5 by construction,
so neither proof can have used additivity. H-B's freeze recorded, as an owner-level question it set
up and did not answer, whether the class obtained by dropping A5's amplitude-scale gauge principle
is admissible. The hydrodynamics programme has a different target from the OI → QM route, so a
condition belongs in it only if something there requires it; the round supplies that necessity
analysis for A5.

**THE SCOPE STATEMENT, FROZEN.** The programme-level objective is:

> what is the weakest OI substratum structure sufficient to produce a Navier–Stokes hydrodynamic
> limit?

**That objective is the programme's, not this round's**, and one round auditing one condition
cannot characterize the structure it asks for. **This round's deliverable is narrower and exactly
this: the logical status of A5 relative to that objective** — whether observational incompleteness
requires it, where the quantum route uses it, and whether the hydrodynamic ladder requires it.
**A negative finding about A5, at any of the three questions, is a finding about A5 and is never a
characterization of the sufficient structure**: removing one condition from a candidate list
neither identifies the weakest sufficient structure nor shows that the remaining conditions
suffice. Any sentence of the result note that reads as such a characterization is a defect
(status rule 10, hazard 18).

**What the round can decide:** where, in the corpus and the kernel as they stand at the start
state, A5's warrant is sourced; which named kernel results take `𝒮.A5` as a hypothesis; whether a
clean OI-admissible substratum without A5 is exhibited anywhere in the tree; where and how
specifically the reconstruction chain uses A5; whether any of `../PROGRAMME.md` §3's obligations
H1–H7 requires it at the level the round can actually examine; and, under the decision rules frozen
below, what may be reported for each of the three questions.

**What the round cannot decide, and does not claim to:** whether observational incompleteness
requires A5 — a search that finds no derivation on a named record is not a proof that none exists
(status rule 1, hazard 1); whether an A1–A4, ¬A5 class reaches a hydrodynamic limit, which is
H3–H7 and H-C and which the guardrail above forbids reading out of H-B; whether the A1–A4, ¬A5
class is admissible as an **OI substratum**, which is H-B's open owner question and a different
question from hydrodynamic candidacy (hazard 3); anything about `d = 3`; anything about the
OI → QM chain's own standing.

## Recorded source readings — the one permitted pre-execution object

Every citation below was located and read by hand **before this file was written**, and is recorded
here so that no execution-specific artifact precedes the freeze. Nothing here is evidence at any
level above "recorded reading"; the execution re-reads each source at the mandated base and reports
what it finds, including any divergence from what is recorded here.

1. **A5 in the kernel** is `∀ c c', F (c + c') = F c + F c'` on the rule of a `Substratum`
   (`SubstratumInterfaceAudit.lean`). The module's own header records A1, A2 and A5 as "stated
   outright", A3 with the degree as a parameter and in family form, A4 with the gauge as a
   parameter, and A6 as a gap with no predicate.
2. **The named kernel results whose statements carry `𝒮.A5` or an instance of it**, as located by
   reading the tree: `A5` itself and `waveSubstratum_A5` (`SubstratumInterfaceAudit.lean`);
   `map_zero_of_additive`, `coarse_evolution_additive`, `coarseCloses_additive_on_range`,
   `coarseCloses_nsmul`, `wave_coarse_evolution_additive`,
   `wave_coarseCloses_additive_on_range` (`HydroSourceAudit.lean`); `phi_fixes_zero`,
   `ensemble_underdetermined`, `stochastic_interface_gap`,
   `waveSubstratum_stochastic_interface_gap` (`StochasticInterface.lean`);
   `hexSubstratum_A5_witness` and `hexSubstratum_not_A5` (`HexLatticeGas.lean`). **No module of the
   OI → QM chain appeared in this reading.** Two properties of the list were read with it and are
   recorded here: in `StochasticInterface.lean` A5 is the hypothesis of a **gap** result —
   additivity fixes the zero configuration, which closes the single-orbit route to a determined
   ensemble — and not of a derivation; in `HydroSourceAudit.lean` it is the hypothesis of a
   conditional no-go. The reading is a reading of statements, not a transitive dependency analysis,
   and `A5S-1b` states the two questions separately for that reason.
3. **[Structure §2.1] Level B** states four observer-admission conditions on `φ` — coupling,
   record persistence, sufficient capacity, history readback — and none of the four mentions the
   alphabet, its additive structure, or the functional form of the update. Level D states A1–A6 and
   says of A3–A6 that they are class-specific and not necessary for observer-admission.
4. **[Substratum §3.1]** introduces A1–A6 as structural assumptions restricting the class of
   candidate substrates, as inputs to the reconstruction, and gives A5 the parenthetical recorded
   in the sourcing table above.
5. **[Substratum §4]'s amplitude-scale-gauge remark, *Status* note**: the principle is adjoined as
   an explicit operational principle; it is not one of Theorem 24's generators (generator (i)
   over-counts, generator (ii) is alphabet-size only); the results invoking it are conditional on
   it; and the route that would make linearity unconditional — deriving the unobservability of
   absolute amplitude from the observer architecture — is recorded there as circular, since what
   the embedded observer can resolve through the trace-out is itself dynamics-dependent.
6. **[Substratum §4]'s formalization-status note on the linearity step** records the
   linearity-equivalence lemma as a complete elementary result, resolves the entailment question
   from [SM §2.7]'s `q`-size freedom **in the negative**, and classifies linearity as a Tier-3
   definitional stipulation rather than a forced Tier-1 consequence.
7. **Two statements of the entailment question's status stand in the corpus**: the parenthetical at
   [Substratum §3.1] (A5) and the closing sentence of [SM §2.7] carry it as an identified open
   step or open structural question, and the formalization-status note of item 6 records it as
   resolved in the negative. The round records both, adopts neither over the other, and edits
   neither (`A5S-2d`; the propagation question is named for the owner and is outside this round).
8. **H-B's positive results** — `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`,
   `hexSum_leap_sector`, `hexMoment4_eq`, `hexMoment4_isotropic` — are stated about
   `hexSubstratum L`, `hexGas L` and `hexMoment4`, and `hexSubstratum_not_A5` is a theorem about the
   same object. Reading them together is a reading of proved statements about one object and adds
   no new kernel content (`A5S-3b`, hazard 9). **Nothing in that reading reaches a limit**: no
   result of H-B mentions a scaling map, a continuum field or a PDE, which is the kernel-side form
   of the guardrail above.

## Targets, FROZEN

Every target carries an evidence type in the programme's control 9 vocabulary: **type P** —
prose/source audit; **type K-cited** — a statement re-read from an existing kernel-checked result,
consumed at that result's own evidence level and **not re-proved, not strengthened, and not
promoted by being cited here**. The round produces **no new kernel evidence**.

`A5S-0` is preliminary. `A5S-1`, `A5S-2` and `A5S-3` are the three independent questions, in the
owner's order. `A5S-4` is the report, `A5S-5` the scope and the successor.

### `A5S-0` — the frozen statement of the condition, and its sourcing

**`A5S-0a` (type P).** Record A5 in both of its statements — the kernel's additivity of `𝒮.R.F`,
and [Substratum §3.1]'s linearity of the wave equation — and record that the tree contains no
theorem identifying the two, `waveSubstratum_A5` being an instance result for one rule rather than
an identification. **Prediction: positive (the two statements are recorded as two, and no
identification is found), full strength.** *Reason:* the kernel's header states the predicate; the
manuscript states the condition; a search of the tree for an identification returned none, and an
identification would have to quantify over rules that the kernel's `Rule` interface does not
constrain to be wave-like.

**`A5S-0b` (type P).** Record, for each of A1–A6, the manuscript location and the status the
manuscripts attach, as the sourcing table above has it, and record that all six are introduced as
inputs to the reconstruction. **Prediction: positive, full strength.** *Reason:* the section is
explicit and was read before the freeze (recorded reading 4).

### `A5S-1` — QUESTION (a), BARE-OI NECESSITY

**Can A5 be derived from observational incompleteness itself, independent of the quantum
reconstruction? If it cannot, is there a clean OI-admissible counterexample without A5?**

**`A5S-1a` (type P) — the derivation question.** Search the named bare-OI record — [Main §1],
[Main §3]'s C1–C4, [Structure §2.1] Levels A and B, [Structure §9.6]'s Definition 9.9,
Proposition 9.10 and Corollary 9.11 — for any statement entailing additivity of the substratum
rule, or entailing the amplitude-scale gauge principle A5 is equivalent to, for every admissible
substratum, **without passing through the reconstruction chain**. Report what is found, and report
the boundary of the search: the exact set of sources read. **Prediction: negative — no such
derivation is found — at high strength for the record searched, and at no strength at all as a
statement about what exists off that record.** *Reason:* [Structure §2.1] states of A3–A6 that they
are not necessary for observer-admission; C1–C4 are conditions on coupling, persistence, capacity
and readback and name no property of the update's functional form; and [Substratum §4]'s *Status*
note records the one derivation route that would supply such a warrant as circular.

**`A5S-1b` (type P over kernel objects) — the kernel's A5-consumers.** Enumerate, at the mandated
base, (i) every named kernel result whose **statement** carries `Substratum.A5` or an instance of
it, and (ii) every named kernel result whose **proof** consumes one of those, and record for each
the module and the programme it belongs to. Report whether any module of the OI → QM chain appears
in either list. **Prediction: positive for the enumeration, and negative for OI → QM appearance** —
(i) closes at full strength (a mechanical search over the tree), (ii) at high strength (a
dependency reading, in which a missed downstream consumer is the plausible error). *Reason:*
recorded reading 2. **The frozen reading:** a condition that no step of the kernel's OI → QM chain
takes as a hypothesis is not thereby shown unnecessary to that chain — the chain is not complete in
the kernel, and the manuscripts' Stage 2 consumes A5 where the kernel is silent. The enumeration is
a fact about the kernel, and `A5S-2a` is where the manuscript consumption is located.

**`A5S-1c` (type P) — the counterexample question, a target in its own right.** Determine whether
the tree exhibits a **clean OI-admissible substratum without A5**, and report the determination.

**"OI-admissible", defined in terms of objects already in the tree:** there is a partition `V ⊂ S`
such that `(S, φ, V)` satisfies C1–C4 as [Main §3] states them, which is [Structure §9.6]'s
Definition 9.9 of an observer-admitting substratum. The kernel carries **no** predicate for
observer-admission on a `Substratum`: `ManuscriptAxioms.lean` records realized-core images for A1
and A2 on the bare operational theory and no predicate at all for A3–A6, and its configuration-level
sourcing results bound what a substratum's own interventions generate without supplying an
admission predicate.

**"Clean", defined as five conditions, all required:** (i) the object is **exhibited**, not
posited or assumed to exist; (ii) it instantiates the kernel's `Substratum` interface **unmodified**;
(iii) its failure of A5 is a **theorem** about it, not the absence of a proof that it holds;
(iv) its **observer-admission is established**, not assumed, at the definition above; (v) nothing
in the exhibition weakens, reinterprets or parameterizes C1–C4 or the interfaces to obtain (iv).

**Prediction: UNDECIDED, at high strength that UNDECIDED is the outcome.** *Reason:* condition (iv)
has no carrier in the tree — no concrete substratum has its observer-admission established, and
this round's definition budget is zero, so it may not supply one. H-B's candidate satisfies (i),
(ii) and (iii) and is silent on (iv); that makes it **a candidate for such a counterexample and not
one**, and the result note says so in those words. **What would change the outcome:** an existing
result, anywhere in the tree, establishing observer-admission for a concrete substratum that fails
A5 — then the counterexample is reported exhibited, with that result cited. **What the execution
may not do:** construct the object, weaken (iv), or report H-B's candidate as the counterexample
(hazard 19).

**Permitted outcomes for question (a):** *derivable* — a derivation from bare-OI conditions alone is
exhibited and cited; *no derivation on the record searched* — with the record named in the same
paragraph; *counterexample exhibited* — `A5S-1c` positive, with the five conditions checked; or
**UNDECIDED**. The evidence bar for reporting the sentence "A5 is not a bare-OI requirement" is
status rule 7.

### `A5S-2` — QUESTION (b), QUANTUM-ROUTE NECESSITY

**Where exactly is A5 used in the chain to quantum mechanics and to the substratum, and is that use
genuinely quantum-specific?** These are **two obligations and are kept separate**: `A5S-2a` locates
the uses; `A5S-2b` judges their quantum-specificity. **A located use is not thereby a
quantum-specific use**, and the result note reports the two findings separately for each use
(hazard 20).

**`A5S-2a` (type P) — locate the uses.** Locate every load-bearing consumption of A5, or of the
amplitude-scale gauge principle it is equivalent to, in the reconstruction chain: [Substratum §3.1]'s
input list, [Substratum §3.3] Stage 2(b)'s wave-equation selection, [Substratum §3.3] Stage 2(d)'s
reduction of the block stabilizer to the Standard-Model group, [Substratum §3.5]'s Theorem 23
hypothesis list, [SM §4.1]'s wave-equation uniqueness and its amplitude-scale-gauge lemma,
[SM §4.6]. For each, record **where** it is used and **what the step concludes from it**, in the
manuscripts' own words and not in the round's. **Prediction: positive, full strength** — the
consumptions exist and are explicit. *Reason:* recorded readings 4 and 5; Stage 2(b) names A5 in
its input list in terms, and Stage 2(d)'s phase stripping names amplitude-scale invariance in terms.

**`A5S-2b` (type P) — judge the quantum-specificity, per use.** For each use located by `A5S-2a`,
determine whether the use is **quantum-specific**, defined for this round as: the conclusion the
step draws from A5 is consumed **only** inside the reconstruction/QM chain — the wave-equation
selection, the `(3,2,1)` decomposition and the gauge group, Theorem 23's local residue, the
Stage-3 constants — and is required by no obligation outside that chain. Report **per use**:
quantum-specific; not quantum-specific, with the outside consumer named; or **UNDECIDED**.
**Prediction: quantum-specific for the located uses, at medium strength.** *Reason:* the located
conclusions are Level D objects by [Structure §2.1]'s own placement, and [Structure §2.1] states of
A3–A6 that they are required for the gauge-structure derivation; the strength is medium and not
higher because the judgment is an audit of downstream consumption across the whole corpus, where a
missed consumer is the plausible error and where §A.25's propagation discipline means such a
consumer could sit far from the step. **The frozen reading:** "quantum-specific" in this round's
sense is a statement about **where the step's conclusion is consumed on the present record**. It is
**not** a proof that no other emergent theory could need the same conclusion, and it is not a claim
about A5's truth, its standing, or its necessity anywhere else (hazard 2).

**`A5S-2c` (type P) — the status the corpus gives the principle.** Record it at its authoritative
home: adjoined operational principle, not one of Theorem 24's generators, results invoking it
conditional on it, on a par with center independence and isotropy and not a theorem; and linearity
classified Tier-3 definitional stipulation rather than forced Tier-1. **Prediction: positive, full
strength.** *Reason:* recorded readings 5 and 6, both quoted from a single dedicated status note.

**`A5S-2d` (type P) — the entailment question, both statements.** Record, side by side and without
adopting either over the other, the two statements the corpus carries about whether [SM §2.7]'s
`q`-size gauge freedom entails amplitude-scale gauge: the identified-open-step form at
[Substratum §3.1] (A5) and the closing sentence of [SM §2.7], and the resolved-in-the-negative form
at [Substratum §4]'s formalization-status note. **Prediction: positive (both are found, as
recorded), high strength** — the risk is that a further statement of the same question stands
elsewhere in the corpus and is missed, which would add to the record and not change its shape.
**The frozen discipline:** the round **edits no manuscript** and resolves no divergence; it names
the propagation question for the owner and stops. On **either** reading the principle remains
adjoined rather than derived — an open entailment leaves it adjoined, a negative entailment makes
it separately adjoined — so question (b)'s answer does not turn on which reading is taken
(hazard 8).

**Permitted outcomes for question (b):** per use — *located and quantum-specific*; *located and not
quantum-specific*, with the outside consumer named; or **UNDECIDED**. A summary sentence about the
chain as a whole is permitted only as the conjunction of the per-use findings, and carries their
weakest strength.

### `A5S-3` — QUESTION (c), HYDRODYNAMIC NECESSITY

**Does any step H3–H7 actually require A5, or can an A1–A4, ¬A5 class reach the hydrodynamic
limit?**

**`A5S-3a` (type P) — the obligations as stated.** Walk `../PROGRAMME.md` §3's obligations H1, H2,
H3, H4, H5, H6, H7 one at a time and record, for each, whether the obligation **as stated** names
A5, names additivity of the rule, or has a stated content that requires either. **Prediction:
negative for all seven, full strength for the record** — the obligations as stated name local
conserved observables, isotropic tensor structure, mixing/local equilibrium, a scaling map, an
Euler-level limit, a viscous correction and an incompressible limit, and none of the seven mentions
the alphabet's additive structure or the update's functional form. *Reason:* the section was read
before the freeze. **The frozen reading, and it is the reason this target cannot answer question (c)
on its own:** an obligation's *statement* is a statement of what is to be shown, not of what a
derivation of it consumes. H3–H7 have no derivation, so **the absence of A5 from their statements
is not evidence that a derivation of them would not require A5**, and status rule 6 forbids
reporting the stronger sentence on this target's strength (hazard 16).

**`A5S-3b` (type K-cited) — what H-B's results do and do not establish.** Read together, for one
object, H-B's `hexSubstratum_not_A5` and the results carrying H-B's positive findings —
`hexSum_mass_hexGas`, `hexSum_momentum_hexGas`, `hexSum_leap_sector`, `hexMoment4_eq`,
`hexMoment4_isotropic` — and record the consequence: **the conjunction of [exact conservation of
mass and both momentum components, on the sector, for every configuration and every lattice size]
with [fourth-order rotation-isotropy of the stencil] does not entail A5**, `hexSubstratum L` being
a lawful witness to its failure. **A5 is therefore not necessary for the content those two
obligations name, at the scope H-B states it.** **Prediction: positive, full strength** — one
exhibited witness refutes one universal statement, and the round adds nothing to the kernel, the
witness and both conjuncts being theorems already.

**The guardrail, carried here in terms:** *H-B shows that A5 is not needed to obtain a promising
reversible fluid candidate with the right microscopic ingredients; it does not yet show that A5 is
unnecessary for an actual Euler/Navier–Stokes limit.* The non-entailment above is about the
**microscopic content** H1 and H2 name, at H-B's scope. No result of H-B mentions a scaling map, a
continuum field, a closure or a PDE, so nothing in this target reaches H3–H7, and **this target may
not be cited, alone or with `A5S-3a`, in support of "A5 is not required by the hydrodynamic route"**
(status rule 6). **The frozen bound on the labels:** they stay H-B's labels — H1 HD for mass and
momentum **for the candidate, on the sector**, H2 HD for the stencil tensor with the stress status
conditional — the round writes no label "for OI", moves no obligation and reports none closed
(status rules 3 and 4).

**`A5S-3c` (type K-cited) — the finding that cuts the other way.** Record it, as H-A proved it:
`coarse_evolution_additive` and `coarseCloses_additive_on_range` take A5 as their hypothesis, so on
substrata satisfying A5 no closed `ZMod q`-linear coarse description carries an advective term.
**Prediction: positive, full strength.** **Why this target is here:** it is evidence that A5 is
**not neutral** for the hydrodynamic target on at least one named class, which is exactly why
question (c) is kept independent of questions (a) and (b) and why a naive reading of A5 as
"irrelevant to the Navier–Stokes derivation" is not available to the execution. **The frozen
reading, stated in advance because this is the target a careless execution would over-read:** this
is a conditional no-go on **one named class of coarse variables**, for substrata satisfying A5;
real-valued and nonlinear coarse variables are **HO** by H-A's own statement; and it is therefore
**not** a proof that A5 excludes a Navier–Stokes limit, **not** a proof that Navier–Stokes requires
the failure of A5, and **not** a ground on which the round labels A5 anything at all (hazard 7).
The round records it as what it is: an obstruction found, under a stated hypothesis, on a stated
class.

**`A5S-3d` (type P) — the boundary, and what would settle question (c) either way.** Record that
H3, H4, H5, H6 and H7 are **HO**, that no derivation closes them, and that a future derivation
could consume additivity in a step not yet written. Record what would settle the question:
**positively** — a derivation of some step of H3–H7 that takes A5 as a hypothesis and is shown to
need it, or a no-go showing no ¬A5 rule can close one of those steps; **negatively** — a derivation
of the Euler-level limit, the viscous correction or the incompressible limit for a rule in the
A1–A4, ¬A5 class, at a stated scaling map and convergence topology. **Prediction: neither is found
at the start state, so question (c) is answered UNDECIDED; the boundary and the two settling
conditions are recorded. This target carries no sign.** *Reason:* the programme's own statuses, and
the fact that the round writes no Lean and takes no limit.

**Permitted outcomes for question (c):** *required* — a step of H3–H7 is shown to require A5, with
the derivation cited; *not required by the hydrodynamic route* — only on evidence meeting status
rule 6's bar; or **UNDECIDED**, which is what `A5S-3a`–`A5S-3d` are predicted to return.

### `A5S-4` — the three answers, reported independently

**`A5S-4a` (type P).** Report an answer to each of (a), (b) and (c) **separately**, each with its
evidence and the boundary of that evidence, under the permitted outcomes above and the status rule
below. **The three answers may disagree, and a mixed report is the expected shape.**

**Prediction, per question:** (a) *no derivation on the record searched*, with `A5S-1c`
**UNDECIDED**; (b) the uses located, and quantum-specific at medium strength; (c) **UNDECIDED**.
**So the predicted report is the first of the two worked examples frozen below.** *Reason:*
recorded readings 3, 5 and 6 for (a) and (b); for (c), `A5S-3d` — H3–H7 are HO and the evidence
bar of status rule 6 is not met by `A5S-3a` and `A5S-3b`. **Strength:** high for (a) as stated,
medium for (b), and for (c) full strength that the answer is UNDECIDED. **UNDECIDED is a permitted
outcome of every one of the three**, reported with the obstruction named.

**`A5S-4b` (type P).** Report the consequence for H-B's candidate under the disqualification rule
frozen below: whether any **established** ground disqualifies it as a **hydrodynamic candidate** on
its A5 failure. **Prediction: none is established, on the findings `A5S-4a` predicts; the note says
that and no more.** **Strength: full, conditional on `A5S-4a`.** **Frozen in advance:** "no
established ground for disqualification" is **not** "the candidate reaches a hydrodynamic limit",
is **not** a ruling that the A1–A4, ¬A5 class is admissible as an OI substratum — that separate
owner decision **stays open** — and is bounded by the guardrail in terms (hazards 3, 16).

### `A5S-5` — scope, and what the successor inherits

**`A5S-5a` (type P).** Record what remains attached to H-B's candidate after this round, whatever
`A5S-4` lands: A6 is a `GAP` on its own branch and is untouched; the candidate is two-dimensional
and nothing about `d = 3` is said; H3 and H4 are HO for it and H5–H7 are not begun; its
observer-admission is not established, so `A5S-1c` does not close on it; the OI-substratum
admissibility of its class is open; and no statement of this round is evidence that the candidate
is selected by anything. **Prediction: the list is recorded, in these terms, with no item
resolved.** **Strength: full.**

**`A5S-5b` (type P).** Restate the scope statement in the result note, and record that the
programme-level objective — the weakest OI substratum structure sufficient to produce a
Navier–Stokes hydrodynamic limit — **is not characterized by this round**, which delivers the
logical status of A5 relative to it and nothing more; and that the sufficiency question belongs to
H3–H7 and H-C. **Prediction: the statement is carried and the objective is left open.**
**Strength: full.**

## The preregistered predictions, and their strengths

| target | question | type | prediction | strength | what would falsify it |
| --- | --- | --- | --- | --- | --- |
| `A5S-0a` | — | P | positive: two statements of A5, no identification theorem in the tree | full | an identification theorem found in the tree; then it is cited and the round records it |
| `A5S-0b` | — | P | positive: the sourcing table, all six conditions, as inputs to the reconstruction | full | a misread section reference; repaired, not reinterpreted |
| `A5S-1a` | (a) | P | **negative**: no bare-OI derivation of A5 on the record searched | high, **for the record searched only** | a derivation from bare-OI conditions alone; then (a) is answered *derivable* |
| `A5S-1b` | (a) | P over kernel | positive enumeration; **negative** for OI → QM appearance | full for statements; high for the dependency reading | a missed downstream consumer; the list grows and the shape of the finding is unchanged unless the consumer is in the OI → QM chain |
| `A5S-1c` | (a) | P | **UNDECIDED**: no clean OI-admissible ¬A5 substratum is exhibited in the tree, condition (iv) having no carrier | high, that UNDECIDED is the outcome | an existing result establishing observer-admission for a concrete ¬A5 substratum; then the counterexample is reported exhibited |
| `A5S-2a` | (b) | P | positive: the uses located, with what each step concludes, in the manuscripts' words | full | a cited step that on reading does not consume A5; then that step comes off the list |
| `A5S-2b` | (b) | P | positive: the located uses are quantum-specific in this round's sense | **medium** | an obligation outside the reconstruction/QM chain that requires the same conclusion; then that use is reported not quantum-specific |
| `A5S-2c` | (b) | P | positive: adjoined operational principle, Tier-3 stipulation, not a theorem | full | — |
| `A5S-2d` | (b) | P | positive: both statements of the entailment question found, neither adopted | high | a further statement elsewhere in the corpus; it is added to the record |
| `A5S-3a` | (c) | P | **negative** for all seven of H1–H7 **as stated**, which does not answer (c) | full, for the statements only | an obligation whose stated content needs additivity; then (c) is answered *required* |
| `A5S-3b` | (c) | K-cited | positive: that conservation content together with that stencil content does not entail A5, H-B's candidate witnessing the failure — and nothing about a limit | full | an error in reading H-B's statements; they are re-read, not reinterpreted |
| `A5S-3c` | (c) | K-cited | positive: A5 is the hypothesis of H-A's advection gate on its named class, so A5 is not neutral for the target | full | — |
| `A5S-3d` | (c) | P | the boundary and the two settling conditions recorded; neither is met at the start state | **no sign** | a derivation at the H3–H7 level, either way |
| `A5S-4a` | all | P | (a) no derivation on the record searched, counterexample UNDECIDED; (b) located, quantum-specific; (c) **UNDECIDED** — the first worked example | high (a); medium (b); full that (c) is UNDECIDED | any of the three questions landing elsewhere; each is reported on its own evidence |
| `A5S-4b` | all | P | no **established** ground disqualifies H-B's candidate as a hydrodynamic candidate | full, conditional on `A5S-4a` | (a) answered *derivable*, or (c) answered *required* |
| `A5S-5a` | — | P | the residual list recorded, no item resolved | full | — |
| `A5S-5b` | — | P | the scope statement carried, the programme objective left open | full | — |

**UNDECIDED remains a permitted label for every target and for every one of the three questions**,
reported with the obstruction named.

## The three questions, and how each may be answered — FROZEN

The three questions are **logically independent**. Each is answered on its own targets and its own
evidence, each has its own permitted outcomes as listed with its target group, and **no answer to
one question may be inferred from, strengthened by, or traded against an answer to another**
(hazard 17). In particular: a negative at (a) is not evidence at (c); a positive at (b) is not
evidence at (a); and a non-entailment at (c) established on microscopic content is not an answer to
(c) at the level of a limit.

**Mixed outcomes are permitted and expected.** These two report forms are frozen as worked
examples, in the owner's words, and the result note may use either verbatim when its evidence bar
is met:

> **"A5 is not a bare-OI requirement, is needed by the current quantum-completion route, and its
> necessity for Navier–Stokes remains undecided."**

> **"A5 is QM-specific and not required by the hydrodynamic route."**

The first is the round's predicted report. The second is the stronger one, and it carries the
evidence bar of status rule 6; the first carries the bar of status rule 7 on its opening clause.

**The disqualification rule, FROZEN.** H-B's candidate is disqualified as a **hydrodynamic
candidate** by its A5 failure **only if** question (a) is answered *derivable* — A5 derived from
observational incompleteness itself — **or** question (c) is answered *required*. On any other
outcome the round reports that **no established ground disqualifies it on that basis**, and reports
nothing further: in particular nothing about whether it reaches a limit (the guardrail), and
nothing about its class's admissibility as an OI substratum, which stays open.

## The status rule for the execution, FROZEN

Whatever the execution lands, the following binds the result note and every propagation of it.

1. **The execution may not report A5 disqualifying, or non-disqualifying, beyond what it proves.**
   Where the finding is that no derivation was found on a named record, the note says *no
   derivation was found on the record searched*, names the record, and states that this is not a
   proof that none exists. Where the finding is that no obligation **as stated** requires A5, the
   note says *as stated* and carries `A5S-3d`'s boundary.
2. **THE GUARDRAIL ON H-B.** Every place the result note consumes H-B, it carries this sentence:
   **"H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with the
   right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
   Euler/Navier–Stokes limit."** The stronger sentence may not be written on H-B's evidence, in any
   paraphrase, anywhere in the round's artifacts, and no summary, abstract or propagation line may
   compress the two halves into the second.
3. **The execution may not report the hydrodynamics obligation discharged.** Not H-B's, not H1's,
   not H2's, not any of H3–H7. No obligation moves status in this round; H-B is not reported
   closed; the programme's H-B entry is not reported discharged. H-B's own labels are cited at
   H-B's scope and are not restated more strongly. **No repair, extension or re-execution of H-B is
   attempted.**
4. **No label is written "for OI."** Every status, classification or finding in this round is a
   statement about a named object — a condition, a candidate, an obligation, a manuscript section —
   and never about observational incompleteness as such. "OI requires", "OI does not require", "OI
   has a fluid" and every variant are forbidden in terms; where the round's subject really is
   question (a), the sentence names the record searched and what it says.
5. **The three answers are reported independently, and mixed outcomes are permitted.** Each of (a),
   (b) and (c) is answered on its own evidence, with its own boundary; disagreement among them is
   reported as such and is not resolved by preferring one; **where a question is undecided it is
   recorded UNDECIDED**, with the obstruction named, and no other question's answer is enlarged to
   cover it.
6. **THE EVIDENCE BAR ON "A5 is QM-specific and not required by the hydrodynamic route."** That
   sentence, and every paraphrase of it, requires **actual evidence at the H3–H7 level** — a
   derivation of the Euler-level limit, the viscous correction or the incompressible limit for a
   rule in the A1–A4, ¬A5 class, at a stated scaling map and convergence topology, or an equivalent
   result at that level. **H-B alone may never support it**, and **the absence of A5 from the
   H1–H7 statements as they are currently written may never support it**, alone or together with
   H-B. Absent such evidence, question (c) is reported **UNDECIDED** (hazard 16).
7. **THE EVIDENCE BAR ON "A5 is not a bare-OI requirement."** That clause may be reported only when
   either `A5S-1c` exhibits a clean OI-admissible counterexample at the five conditions, **or** the
   paragraph carrying it names, in the same paragraph, the record `A5S-1a` searched and states that
   the finding is the absence of a derivation on that record. Otherwise question (a) is reported
   **UNDECIDED**.
8. **The programme's HD/HC/HI/HO taxonomy is not applied to A5.** A5 is a condition, not a
   hydrodynamic obligation; the taxonomy labels obligations. The round's outputs are the three
   answers, and the round applies no taxonomy label to any obligation either (status rule 3).
9. **No manuscript is edited, and no divergence found in the corpus is resolved by this round.**
   `A5S-2d`'s finding is recorded and named for the owner.
10. **THE SCOPE STATEMENT.** The weakest OI substratum structure sufficient for hydrodynamics is
    the **programme-level** objective; this round delivers the logical status of A5 relative to it.
    **No negative finding about A5 may be reported, summarized or propagated as a characterization
    of that structure**, and no sentence may suggest that removing A5 from a candidate list
    identifies what suffices or shows that what remains suffices (hazard 18).
11. `../PROGRAMME.md` §8's one-line state, when a later action refreshes it, carries the three
    answers and the disqualification-rule consequence in the words this file uses, and nothing
    stronger. If the round lands where it predicts, that is: "A5 is not derivable from
    observational incompleteness on the record searched, with the counterexample question
    undecided; it is used at located steps of the reconstruction, quantum-specific on the present
    record; its necessity for Navier–Stokes is undecided; no established ground disqualifies H-B's
    candidate on its A5 failure, and OI-substratum admissibility of the A1–A4, ¬A5 class remains
    open."

## What none of these outcomes licenses

- **Nothing here says that A5 is unnecessary for an Euler or Navier–Stokes limit.** H-B shows that
  A5 is not needed to obtain a promising reversible fluid candidate with the right microscopic
  ingredients; it does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit,
  and no other input of this round reaches that level (status rules 2 and 6, hazard 16).
- **Nothing here characterizes the weakest OI substratum structure sufficient for hydrodynamics.**
  That is the programme's objective; this round delivers the logical status of one condition
  relative to it (status rule 10, hazard 18).
- **Nothing here says observational incompleteness does not require A5.** A search that finds no
  derivation is not a no-go, and question (a)'s counterexample half is predicted UNDECIDED
  (status rules 1 and 7, hazard 1).
- **Nothing here weakens A5's standing in the reconstruction chain.** Locating a condition's uses
  and judging them quantum-specific is a statement about where their conclusions are consumed, not
  about whether A5 holds or whether the chain may use it. [SM §4.1]'s uniqueness argument, Stage 2's
  derivations and Theorem 23 consume A5 exactly as the manuscripts state, and this round changes
  none of them (hazard 2).
- **Nothing here rules the A1–A4, ¬A5 class admissible as an OI substratum.** That is the owner
  decision H-B recorded as open; hydrodynamic candidacy and OI-substratum admissibility are
  different questions, and only the first is in this round's scope (hazard 3).
- **Nothing here says OI yields Navier–Stokes**, or that any candidate has a hydrodynamic limit.
  The programme's control 2 applies; H3–H7 are HO and untouched.
- **Nothing here is a continuum statement.** No limit is taken, no PDE is written, no scaling map
  is fixed, and the continuum-breakdown branch S1–S5 stays closed until H4–H7 exist, per the
  programme's control 5.
- **Nothing here says Navier–Stokes requires the failure of A5.** `A5S-3c` is a conditional
  obstruction on one named class of coarse variables, with real-valued and nonlinear coarse
  variables HO by H-A's own statement (hazard 7).
- **Nothing here repairs, extends or re-executes H-B.** H-B's result stands as H-B states it
  (status rule 3).
- **Nothing here changes A1–A6, their status, or their number.** A6 remains a `GAP` on its own
  branch; the wave representative's A1–A5 are consumed as proved; **no condition is added to the
  A-list or to the C-list, and none is named** (hazard 11).
- **Nothing here establishes that observational incompleteness has more than one emergent effective
  theory.** The three-set separation is bookkeeping over obligations. That two targets may need
  different completion packages is the round's organizing frame, not a result of it (hazard 10).
- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity —
  control 1. The chain's manuscript sections are read as the location of a condition's uses and for
  nothing else (hazard 12).
- **No manuscript is edited by this round.** Publication-facing claims wait, per the programme's
  control 10.

## Immutable inputs

Cited and consumed **unmodified**: `Substratum`, `Substratum.Conf`, `Substratum.φ`, `shiftBy`,
`A1`, `A2`, `A3`, `A3Family`, `A4Exact`, `A4`, `A5`, `a1_of_finite`, `a2_every_substratum`,
`a3_of_fintype`, `a4_of_exact`, `waveSubstratum`, `waveSubstratum_A1`–`waveSubstratum_A5`;
`map_zero_of_additive`, `coarse_evolution_additive`, `coarseCloses_additive_on_range`,
`coarseCloses_nsmul`, `wave_coarse_evolution_additive`, `wave_coarseCloses_additive_on_range`,
`CoarseCloses`, `totalSum`, `blockSum`, `axisMoment4` and its lemmas; `hexSubstratum` and its
A-profile results, `hexSubstratum_A5_witness`, `hexSubstratum_not_A5`, `hexSum_mass_hexGas`,
`hexSum_momentum_hexGas`, `hexSum_leap_sector`, `hexMoment4_eq`, `hexMoment4_isotropic`,
`hexGas_hexRot`; `A1Realized`, `A2Realized`, `A1A2Realized` and the configuration-level sourcing
results; `A6Inv`, `A6Cov`, `A6Glob`; `phi_fixes_zero`, `ensemble_underdetermined`,
`stochastic_interface_gap`, `waveSubstratum_stochastic_interface_gap`;
[Main §1], [Main §3]; [Structure §2.1], [Structure §9.6] Definition 9.9, Proposition 9.10 and
Corollary 9.11; [Substratum §3.1], [Substratum §3.3], [Substratum §3.5], [Substratum §3.6],
[Substratum §4] Theorem 24 with its amplitude-scale-gauge remark, that remark's *Status* note and
its formalization-status note; [SM §2.7], [SM §4.1], [SM §4.6]; `../PROGRAMME.md` §3, §4, §6, §7;
`../round-h-a-source-audit/` and `../round-h-b-reversible-fluid-substratum/` in full.

## The chronology control

This round writes no kernel object, so there is no execution-specific Lean artifact for an ancestry
guard of the `R7-HY*` shape to order. The control is correspondingly the part of act 10's mechanism
that applies:

1. **This preregistration blob is merged into `main` before any execution-specific H-D object
   enters the repository tree** — any result note, any probe, any audit artifact of this round's
   targets. **The single permitted exception is the reading recorded inside this control-plane blob
   itself**, merged *as* the freeze, including recorded readings 1–8.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The result note pins this file's blob SHA by content**, and records the base it executed on.
4. **No new guard file is added by this round**, and no existing guard is modified. Whether the
   `R7-HY*` family is extended to cover prose-only rounds of this programme is an owner decision
   this round records and does not make.
5. **The claim is scoped to the repository record.**

## Definition budget

**Zero.** The execution introduces **no** top-level definition, adds **no** Lean module, and edits
**no** existing one. It cites kernel results and re-proves none. In particular it does **not**
construct the counterexample `A5S-1c` asks about, and does not define an observer-admission
predicate.

**A single definition requires its own append-only amendment**, separately frozen and merged before
the work it affects, naming the definition and the target it serves. If a target turns out not to be
settleable without a kernel statement, the frozen response is to record that target **UNDECIDED**
with the obstruction named — not to write the statement under this freeze.

## Evidence level

**Evidence type: prose/source audit throughout** (programme control 9), for every target. The
kernel results the round cites carry their own evidence level 2 from the rounds that proved them
(H-A, H-B, the interface audit), and **citing them here promotes nothing**: the round reports each
cited statement at that statement's own scope, and adds no kernel evidence of its own. Recorded
readings 1–8 are analysis, not evidence.

## Named hazards

1. **Reading question (a)'s negative as a theorem.** "No derivation found on the record searched"
   is not "observational incompleteness does not require A5". The record searched is named, and the
   distinction is written into every sentence that reports the negative (status rule 7).
2. **Reading question (b)'s answer as a demotion of A5.** Locating A5's uses and judging them
   quantum-specific says where their conclusions are consumed; it does not weaken the
   reconstruction, and the chain consumes A5 exactly as the manuscripts state.
3. **Reading the round as ruling on OI-substratum admissibility.** Hydrodynamic candidacy is what
   the disqualification rule decides. The admissibility of the A1–A4, ¬A5 class as an OI substratum
   is H-B's open owner question and stays open in those words.
4. **Reading H-B's A5 failure as a criticism of the manuscripts' linear rule**, which A5 is there
   to secure. H-A's and H-B's findings stand as those rounds state them, for their own objects.
5. **Confusing the substratum axiom A5 with the act-level target labels `A4` and `A5` of
   `../oi-qm/PROGRAMME.md`'s Track B.** They are different namespaces, and no sentence of this
   round may read across them.
6. **Confusing the round label `H-D` with the outcome label `HD`.** The round applies no taxonomy
   label; its targets carry the `A5S` prefix for that reason.
7. **Over-reading `A5S-3c`.** H-A's advection gate is conditional on a named coarse-variable class
   and takes A5 as its hypothesis. "Navier–Stokes requires ¬A5", "A5 excludes a hydrodynamic
   limit", and "the advection obligation is settled" are each forbidden in terms; real-valued and
   nonlinear coarse variables are HO.
8. **Identifying the alphabet-size gauge principle with the amplitude-scale gauge principle**, or
   treating either as entailing the other. The corpus carries the entailment question in two forms
   (`A5S-2d`); the round records both and adopts neither, and question (b)'s answer does not turn
   on which is taken.
9. **Promoting a cited kernel result.** Nothing cited here gains strength by being cited, and no
   cited statement may be restated more broadly than the theorem that carries it.
10. **Building a bridge out of the three-set frame.** That two targets may descend through
    different completion packages is the frame this round works in, not a result it establishes; no
    claim that observational incompleteness carries multiple emergent effective theories follows
    from anything here.
11. **Naming a new condition.** The round adds nothing to the A-list or to the C-list, names no
    further condition, and does not renumber or reinterpret an existing one.
12. **Importing OI → QM results or Track B labels as evidence here, or exporting these findings
    there** — control 1.
13. **Speaking about singularities.** S1–S5 remain closed until a continuum map exists.
14. **Treating the enumeration of `A5S-1b` as exhaustive over proofs.** It is exhaustive over the
    tree searched at the mandated base, by the search the result note describes; the boundary is
    recorded with the finding.
15. **Using the word that the repository's style rule bans for constructions.** Weakest, least,
    smallest sufficient.
16. **Reading H-B as showing A5 unnecessary for a limit — the round's central hazard.** H-B's
    object is a microscopic candidate; no result of it mentions a scaling map, a continuum field, a
    closure or a PDE. The guardrail sentence of status rule 2 is carried wherever H-B is consumed,
    and the sentence "A5 is QM-specific and not required by the hydrodynamic route" may not be
    written on H-B's evidence, nor on the absence of A5 from the H1–H7 statements as written, nor
    on the two together (status rule 6). An execution that reaches for the stronger sentence on
    that evidence has committed this round's characteristic error.
17. **Inferring one question's answer from another's.** The three questions are independent: a
    negative at (a) is not evidence at (c), a positive at (b) is not evidence at (a), and no
    question's UNDECIDED is filled in from another's answer (status rule 5).
18. **Reading a negative about A5 as a characterization of the sufficient structure.** Dropping one
    condition from a candidate list neither identifies what suffices for a hydrodynamic limit nor
    shows that what remains does (status rule 10).
19. **Reporting H-B's candidate as question (a)'s counterexample.** It meets three of `A5S-1c`'s
    five conditions and is silent on observer-admission; it is a candidate for such a counterexample
    and not one, and the round may not close the gap by weakening the definition or by constructing
    an object.
20. **Collapsing `A5S-2a` into `A5S-2b`.** Locating a use and judging it quantum-specific are two
    obligations with different evidence; a located use is not thereby quantum-specific, and the
    result note reports the two findings separately for each use.

## Non-doings

The round does not: construct any substratum, candidate, stencil, coarse variable or
observer-admission predicate; write or edit any Lean; re-prove any cited result; repair, extend or
re-execute H-B; attempt a derivation of A5 from bare-OI conditions, or a proof that none exists;
take any continuum limit or assert any PDE; assert any statistical closure, mixing or
local-equilibrium statement; adjudicate any condition other than A5; test, weaken or strengthen the
alphabet-as-gauge or amplitude-scale-gauge principles; edit A1–A6, their kernel status, or their
number; resolve the divergence `A5S-2d` records; close or discharge any obligation; characterize
the sufficient structure for a hydrodynamic limit; edit `PROGRAMME.md`, `ROADMAP.md`, `README.md`,
the census or any guard in this PR; touch any manuscript; say anything about Track B, Track I, Bell,
gravity or singularities.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the result
  note and the propagation the owner directs. **No Lean, no guard, no manuscript changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## The programme objective, and this round's place in it

The programme-level objective is **the weakest OI substratum structure sufficient to produce a
Navier–Stokes hydrodynamic limit**. This round does not characterize it and does not answer it.
Its narrower deliverable is **the logical status of A5 relative to that objective**: whether
observational incompleteness requires A5, where and how specifically the quantum route uses it, and
whether the hydrodynamic ladder requires it. The sufficiency question belongs to the programme's
H3–H7 and to H-C, which fix the mixing/local-equilibrium condition, the scaling map and the
convergence topology before any limit is taken. If this round lands where it predicts, the
immediate successor on this branch is H3 and H4 for H-B's candidate — the level at which
question (c) becomes answerable at all — with the candidate's A6 status, its dimension, its
observer-admission and its class's OI-substratum admissibility all still open.

## Allowed final report

1. **`A5S-0`** — the two statements of A5, the absence of an identification theorem, and the
   sourcing of all six conditions as inputs to the reconstruction;
2. **question (a), `A5S-1`** — the bare-OI search with the record named, the result stated as
   absence of a derivation and not as a no-go; the kernel enumeration with its two lists and the
   OI → QM finding, with the frozen reading attached; the counterexample question against its five
   conditions, with H-B's candidate recorded as a candidate for one and not one, and UNDECIDED
   where undecided;
3. **question (b), `A5S-2`** — the located uses with what each step concludes, in the manuscripts'
   own words; **separately**, the per-use quantum-specificity judgment with its frozen meaning and
   its medium strength; the corpus's own status for the principle; the two statements of the
   entailment question, side by side and neither adopted, with the propagation question named for
   the owner;
4. **question (c), `A5S-3`** — H1–H7 walked one at a time **as stated**, with the reason that
   cannot answer the question; H-B's positive results read together with its A5 failure, at H-B's
   labels and scope, **carrying the guardrail sentence**; H-A's advection gate with its hypothesis
   and its class named, as the finding that cuts the other way; the boundary and the two settling
   conditions; UNDECIDED unless status rule 6's bar is met;
5. **`A5S-4`** — the three answers reported **independently**, each with its evidence and boundary,
   mixed outcomes as such, UNDECIDED where undecided, one of the two frozen worked examples where
   its bar is met; and the disqualification-rule consequence for H-B's candidate, in this file's
   words and no further;
6. **`A5S-5`** — the residual list, no item resolved; the scope statement, with the programme
   objective named and left uncharacterized;
7. what the outcomes do **not** license, in this file's wording, the guardrail among them;
8. the definition budget, recorded as zero definitions introduced;
9. the chronology certification: the blob pin by content, the base, and the record that no guard
   was added or modified.

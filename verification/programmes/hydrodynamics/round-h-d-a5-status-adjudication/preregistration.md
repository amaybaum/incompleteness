# Hydrodynamics round H-D — the status of A5 relative to the hydrodynamic target: CONTROL PLANE

Owner-called, under `../PROGRAMME.md`. This file is the whole of round H-D's control plane and is
merged **alone**, before any execution object exists. The round is an **adjudication and sourcing**
round, not a construction round: it audits one condition, A5, against three separate obligation
sets, and reports where the condition's warrant is sourced and which obligations consume it. It
constructs no substratum, proves no hydrodynamic statement, and writes no Lean.

**The round label `H-D` is an identifier, not an ordinal**, in the sense of the repository's rule
that claim IDs are identifiers. Executing it before `../PROGRAMME.md` §6's H-C entry is not a
reordering of the H1–H7 ladder: H-D asks a question about the ladder's inputs, and the ladder is
untouched by it. **`H-D` the round label is not `HD` the outcome label** ("Derived") of the
programme's §4 taxonomy; the round applies no taxonomy label to A5 at all (hazard 6, status rule 5).
The round's targets carry the prefix `A5S` for that reason.

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
| The observation hierarchy and the observer-admission conditions | `papers/Structure.md`, blob `dd5432d70b2a4ab2238a08ea0f30a5101d6ac898` — §2.1's Levels A, B, C, D; C1–C4 as it states them; the per-level statement of what A1–A6 are conditions for |
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

**Those two rounds are the round's data, and the round adds no third data point.**

## The round's organizing frame — three layers, separated

The frame is the round's bookkeeping over obligations. It is **not a theorem, not a new condition,
and not a claim that the three sets are disjoint or nested**: a condition may sit in more than one
layer or in none, and the classification is per condition.

### Layer 1 — bare OI requirements

Conditions genuinely required by observational incompleteness itself. **Precise meaning here:** a
condition `X` is a layer-1 requirement iff every substratum admissible under observational
incompleteness satisfies `X` — admissibility being what [Main §1]'s observation axiom and
[Main §3]'s observer-admission conditions C1–C4 impose, as [Structure §2.1] Levels A and B state
them and [Structure §9.6]'s Definition 9.9 formalizes observer-admission. On the kernel side layer 1
is the interface that carries no distinguished substratum — the finite operational theory, the
sealed OI core and `DerivedOICore` — where `ManuscriptAxioms.lean` records that no manuscript-level
conjunct of A1–A6 is a faithful predicate of the bare theory, A1 and A2 having realized-core
*images* and A3–A6 having neither images nor weakened predicates.

### Layer 2 — QM completion requirements

Conditions needed specifically to obtain finite operational quantum mechanics or the quantum
substratum structure. **Precise meaning here:** a condition `X` is a layer-2 requirement iff a step
of the reconstruction chain consumes it — [Substratum §3.1]'s input list, [Substratum §3.5]'s
Theorem 23, Stage 2's derivations, [SM §4.1]'s wave-equation uniqueness and amplitude-scale-gauge
lemma, [SM §4.6]'s multiplicity reduction — or, on the kernel side, a module of the OI → QM chain
takes it as a hypothesis. [Structure §2.1]'s Level D is this layer's manuscript name.

### Layer 3 — hydrodynamic requirements

Conservation, locality, isotropy, mixing/local equilibrium, scaling and the rest, needed
specifically for Euler/Navier–Stokes. **Precise meaning here:** a condition `X` is a layer-3
requirement iff one of `../PROGRAMME.md` §3's obligations H1–H7 consumes it at the scope that
obligation states, or a round executed under the programme consumed it in discharging one. The
executed instances are H-A's `H0`–`H4a` and H-B's `HB0`–`HB3`.

**What the frame is for.** The programme's §3 ladder asks what a Navier–Stokes limit needs.
Membership in the A-list records that the reconstruction takes the condition as one of its inputs;
that record settles nothing about layers 1 and 3, and importing a condition into the hydrodynamics
programme on the strength of its A-list membership alone is the inference this frame is built to
block. This round performs, for A5 and for A5 only, the necessity analysis the separation calls
for.
**The frame is applied to no other condition in this round**: A1, A2, A3, A4 and A6 are not
adjudicated here, and their appearance in the tables above is sourcing, not classification.

## Why this round exists, and what it can and cannot decide

H-B's candidate carries, at the scope H-B reports them, the H1 obligation's conservation content —
exact local conservation of mass and momentum on its sector — and the H2 obligation's
stencil-tensor content — fourth-order isotropy — and the same candidate fails A5 by construction,
so neither proof can have used additivity. H-B's freeze recorded, as an owner-level
question it set up and did not answer, whether the class obtained by dropping A5's amplitude-scale
gauge principle is admissible. The question as the programme now needs it is sharper and different
in kind: **what is the weakest OI substratum structure sufficient to produce a Navier–Stokes
hydrodynamic limit?** A condition belongs in that answer only if something requires it there.

The round therefore asks of A5, and of nothing else, the necessity question at each layer, and
reports the adjudication under a decision rule frozen below.

**What the round can decide:** where, in the corpus and the kernel as they stand at the start
state, A5's warrant is sourced; which named kernel results take `𝒮.A5` as a hypothesis; whether any
of `../PROGRAMME.md` §3's obligations H1–H7 names additivity or consumes it; whether the two
executed rounds consumed it; and, under the frozen decision rule, which of the three classifications
the record supports.

**What the round cannot decide, and does not claim to:** whether observational incompleteness
requires A5 — a search that finds no warrant on a named record is not a proof that none exists, and
the round says so wherever it reports a layer-1 negative (`A5S-4a`, status rule 1, hazard 1);
whether the A1–A4, ¬A5 class is admissible as an **OI substratum**, which is H-B's open owner
question and a different question from hydrodynamic candidacy (hazard 3); whether H-B's candidate
has a hydrodynamic limit of any kind, which is H3–H7 and H-C; whether a future H5–H7 derivation
might consume additivity in a step not yet written (`A5S-3d`); anything about `d = 3`; anything
about the OI → QM chain's own standing.

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
   neither (`A5S-2c`; the propagation question is named for the owner and is outside this round).
8. **The results carrying H-B's positive findings** — `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`,
   `hexSum_leap_sector`, `hexMoment4_eq`, `hexMoment4_isotropic` — are stated about
   `hexSubstratum L`, `hexGas L` and `hexMoment4`, and `hexSubstratum_not_A5` is a theorem about the
   same object. Reading them together is a reading of proved statements about one object and adds
   no new kernel content (`A5S-3b`, hazard 9).

## Targets, FROZEN

Every target carries an evidence type in the programme's control 9 vocabulary: **type P** —
prose/source audit; **type K-cited** — a statement re-read from an existing kernel-checked result,
consumed at that result's own evidence level and **not re-proved, not strengthened, and not
promoted by being cited here**. The round produces **no new kernel evidence**.

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

### `A5S-1` — layer 1: does observational incompleteness itself require A5?

**`A5S-1a` (type P).** Search the named layer-1 record — [Main §1], [Main §3]'s C1–C4,
[Structure §2.1] Levels A and B, [Structure §9.6]'s Definition 9.9, Proposition 9.10 and
Corollary 9.11 — for any statement entailing additivity of the substratum rule, or entailing the
amplitude-scale gauge principle A5 is equivalent to, for every admissible substratum. Report what
is found, and report the boundary of the search: the exact set of sources read. **Prediction:
negative — no such entailment is found — at high strength for the record searched, and at no
strength at all as a statement about what exists off that record.** *Reason:* [Structure §2.1]
states of A3–A6 that they are not necessary for observer-admission; C1–C4 are conditions on
coupling, persistence, capacity and readback and name no property of the update's functional form;
and [Substratum §4]'s *Status* note records the one derivation route that would supply a layer-1
warrant as circular.

**`A5S-1b` (type P over kernel objects).** Enumerate, at the mandated base, (i) every named kernel
result whose **statement** carries `Substratum.A5` or an instance of it, and (ii) every named
kernel result whose **proof** consumes one of those, and record for each the module and the
programme it belongs to. Report whether any module of the OI → QM chain appears in either list.
**Prediction: positive for the enumeration, and negative for OI → QM appearance** — (i) closes at
full strength (a mechanical search over the tree), (ii) at high strength (a dependency reading, in
which a missed downstream consumer is the plausible error). *Reason:* recorded reading 2. **The
frozen reading:** a condition that no step of the kernel's OI → QM chain takes as a hypothesis is
not thereby shown unnecessary to that chain — the chain is not complete in the kernel, and the
manuscripts' Stage 2 consumes A5 where the kernel is silent. The enumeration is a fact about the
kernel, and `A5S-2a` is where the manuscript consumption is located.

**What would settle the layer-1 branch positively.** A theorem, or a manuscript derivation, whose
hypotheses are layer-1 conditions alone and whose conclusion is `𝒮.A5` — or the amplitude-scale
gauge principle — for every admissible substratum. **The round does not attempt to construct one**
(non-doings). If the execution finds one on the record, `A5S-4a` reports the layer-1 branch and the
round's prediction is recorded as falsified.

### `A5S-2` — layer 2: is A5 a completion principle of the quantum route?

**`A5S-2a` (type P).** Locate every load-bearing consumption of A5, or of the amplitude-scale gauge
principle it is equivalent to, in the reconstruction chain: [Substratum §3.1]'s input list,
[Substratum §3.3] Stage 2(b)'s wave-equation selection, [Substratum §3.3] Stage 2(d)'s reduction of
the block stabilizer to the Standard-Model group, [Substratum §3.5]'s Theorem 23 hypothesis list,
[SM §4.1]'s wave-equation uniqueness and its amplitude-scale-gauge lemma, [SM §4.6]. For each,
record what fails to be derivable if the condition is dropped, **in the manuscripts' own words and
not in the round's**. **Prediction: positive, full strength** — the consumptions exist and are
explicit. *Reason:* recorded readings 4 and 5; Stage 2(b) names A5 in its input list in terms, and
Stage 2(d)'s phase stripping names amplitude-scale invariance in terms.

**`A5S-2b` (type P).** Record the status the corpus gives the principle at its authoritative home:
adjoined operational principle, not one of Theorem 24's generators, results invoking it conditional
on it, on a par with center independence and isotropy and not a theorem; and linearity classified
Tier-3 definitional stipulation rather than forced Tier-1. **Prediction: positive, full strength.**
*Reason:* recorded readings 5 and 6, both quoted from a single dedicated status note.

**`A5S-2c` (type P).** Record, side by side and without adopting either over the other, the two
statements the corpus carries about whether [SM §2.7]'s `q`-size gauge freedom entails
amplitude-scale gauge: the identified-open-step form at [Substratum §3.1] (A5) and the closing
sentence of [SM §2.7], and the resolved-in-the-negative form at [Substratum §4]'s
formalization-status note. **Prediction: positive (both are found, as recorded), high strength** —
the risk is that a further statement of the same question stands elsewhere in the corpus and is
missed, which would add to the record and not change its shape. **The frozen discipline:** the
round **edits no manuscript** and resolves no divergence; it names the propagation question for the
owner and stops. Note that on **either** reading A5's warrant stays at layer 2 — an open entailment
leaves the principle adjoined, and a negative entailment makes it separately adjoined — so
`A5S-4a`'s adjudication does not turn on which reading is taken (hazard 8).

**What would settle the layer-2 branch.** That every recorded warrant for A5 is a consumption
inside the reconstruction/QM chain, together with `A5S-1a`'s and `A5S-1b`'s layer-1 negative.
**What would refute it:** a warrant at layer 1, which is the layer-1 branch, or a warrant at
layer 3, which is `A5S-3`.

### `A5S-3` — layer 3: does a Navier–Stokes limit require A5?

**`A5S-3a` (type P).** Walk `../PROGRAMME.md` §3's obligations H1, H2, H3, H4, H5, H6, H7 one at a
time and record, for each, whether the obligation as stated names A5, names additivity of the rule,
or has a stated content that requires either. **Prediction: negative for all seven, full strength
for the record** — the obligations as stated name local conserved observables, isotropic tensor
structure, mixing/local equilibrium, a scaling map, an Euler-level limit, a viscous correction and
an incompressible limit, and none of the seven mentions the alphabet's additive structure or the
update's functional form. *Reason:* the section was read before the freeze. **The frozen reading:**
this is a statement about the obligations **as `../PROGRAMME.md` §3 states them**, which is the
form in which the programme has committed to them; it is not a statement about every derivation
that might discharge them (`A5S-3d`).

**`A5S-3b` (type K-cited).** Read together, for one object, H-B's `hexSubstratum_not_A5` and the
results carrying H-B's positive findings — `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`,
`hexSum_leap_sector`, `hexMoment4_eq`, `hexMoment4_isotropic` — and record the consequence:
**the conjunction of [exact conservation of mass and both momentum components, on the sector, for
every configuration and every lattice size] with [fourth-order rotation-isotropy of the stencil]
does not entail A5**, `hexSubstratum L` being a lawful witness to its failure. **A5 is therefore
not necessary for the content those two obligations name, at the scope H-B states it.**
**Prediction: positive, full strength** — one exhibited witness refutes one universal statement,
and the round adds nothing to the kernel, the witness and both conjuncts being theorems already.
**The frozen bound:** the labels stay H-B's labels — H1 HD for mass and momentum **for the
candidate, on the sector**, H2 HD for the stencil tensor with the stress status conditional — the
round writes no label "for OI", moves no obligation and reports none closed (status rules 2 and 3),
and the non-entailment above is a statement about the **content** those obligations name, not about
the obligations' status.

**`A5S-3c` (type K-cited).** Record the other direction, as H-A proved it: `coarse_evolution_additive`
and `coarseCloses_additive_on_range` take A5 as their hypothesis, so on substrata satisfying A5 no
closed `ZMod q`-linear coarse description carries an advective term. **Prediction: positive, full
strength.** **The frozen reading, stated in advance because this is the target a careless execution
would over-read:** this is a conditional no-go on **one named class of coarse variables**, for
substrata satisfying A5; real-valued and nonlinear coarse variables are **HO** by H-A's own
statement; and it is therefore **not** a proof that A5 excludes a Navier–Stokes limit, **not** a
proof that Navier–Stokes requires the failure of A5, and **not** a ground on which the round labels
A5 anything at all (hazard 7). The round records it as what it is: an obstruction found, under a
stated hypothesis, on a stated class.

**`A5S-3d` (type P).** Record the boundary of the layer-3 negative: H3, H4, H5, H6 and H7 are
**HO**, no derivation closing them exists, and a future derivation could consume additivity in
a step not yet written; the negative of `A5S-3a`–`A5S-3c` is therefore a statement about the
obligations as stated and the two rounds executed. **Prediction: the boundary is recorded; this
target carries no sign.** *Reason:* the programme's own statuses.

### `A5S-4` — the adjudication

**`A5S-4a` (type P).** Report the classification of A5 under the decision rule frozen in the next
section, with the evidence for the branch reported and the boundary of that evidence named.
**Prediction: the round expects to report A5 as a completion principle of the quantum route,
together with the layer-3 negative — that is, branch (ii) with branch (iii) — and expects not to
establish branch (i).** **Strength: medium-to-high for branch (ii)**, the residual risk being a
warrant at layer 1 standing somewhere in the corpus that the named search does not cover;
**high for branch (iii) as `A5S-3a`–`A5S-3c` state it**, bounded by `A5S-3d`. *Reason:* recorded
readings 3, 5, 6 for the layer-2 warrant and the layer-1 silence; recorded reading 8 and H-A's
`H0` hypothesis for layer 3. **Frozen in advance:** **not establishing branch (i) is not refuting
branch (i)**, and the result note says so in terms wherever it reports the layer-1 negative
(status rule 1, hazard 1). **UNDECIDED is a permitted outcome of this target**, reported with the
obstruction named.

**`A5S-4b` (type P).** Report the consequence for H-B's candidate under the disqualification rule
frozen below: whether the candidate's A5 failure, on this round's findings, disqualifies it as a
**hydrodynamic candidate**. **Prediction: it does not, on the findings `A5S-4a` predicts; and the
round reports exactly that and no more.** **Strength: full, conditional on `A5S-4a`.** **Frozen in
advance:** this is a statement about hydrodynamic candidacy only. It is **not** a ruling that the
A1–A4, ¬A5 class is admissible as an OI substratum — that is the separate owner decision H-B
recorded as open, and it **stays open** (hazard 3, status rule 3).

### `A5S-5` — what the successor inherits

**`A5S-5a` (type P).** Record what remains attached to H-B's candidate after this round, whatever
`A5S-4` lands: A6 is a `GAP` on its own branch and is untouched; the candidate is two-dimensional
and nothing about `d = 3` is said; H3 and H4 are HO for it and H5–H7 are not begun; the
OI-substratum admissibility of its class is open; and no statement of this round is evidence that
the candidate is selected by anything. **Prediction: the list is recorded, in these terms, with no
item resolved.** **Strength: full.**

**`A5S-5b` (type P).** Name the successor question in the form the programme needs it, and record
that this round does not answer it: **what is the weakest OI substratum structure sufficient to
produce a Navier–Stokes hydrodynamic limit?** Record that this round contributes to it exactly one
thing — a determination of where A5's warrant is sourced and which obligations consume it — and
that the sufficiency question is H-C's and H3–H7's. **Prediction: the question is named and left
open.** **Strength: full.**

## The preregistered predictions, and their strengths

| target | type | prediction | strength | what would falsify it |
| --- | --- | --- | --- | --- |
| `A5S-0a` | P | positive: two statements of A5, no identification theorem in the tree | full | an identification theorem found in the tree; then it is cited and the round records it |
| `A5S-0b` | P | positive: the sourcing table, all six conditions, as inputs to the reconstruction | full | a misread section reference; repaired, not reinterpreted |
| `A5S-1a` | P | **negative**: no layer-1 entailment of A5 on the record searched | high, **for the record searched only** | a derivation of additivity, or of amplitude-scale gauge, from layer-1 conditions alone; then branch (i) is reported |
| `A5S-1b` | P over kernel | positive enumeration; **negative** for OI → QM appearance | full for statements; high for the dependency reading | a missed downstream consumer; the list grows and the shape of the finding is unchanged unless the consumer is in the OI → QM chain |
| `A5S-2a` | P | positive: the consumptions located, in the manuscripts' words | full | a cited step that on reading does not consume A5; then that step comes off the list |
| `A5S-2b` | P | positive: adjoined operational principle, Tier-3 stipulation, not a theorem | full | — |
| `A5S-2c` | P | positive: both statements of the entailment question found, neither adopted | high | a further statement elsewhere in the corpus; it is added to the record |
| `A5S-3a` | P | **negative** for all seven of H1–H7 as stated | full, for the obligations as stated | an obligation whose stated content needs additivity; then A5 is a layer-3 requirement and `A5S-4a` reports it |
| `A5S-3b` | K-cited | positive: that conservation content together with that stencil content does not entail A5, H-B's candidate witnessing the failure | full | an error in reading H-B's statements; they are re-read, not reinterpreted |
| `A5S-3c` | K-cited | positive: A5 is the hypothesis of H-A's advection gate on its named class | full | — |
| `A5S-3d` | P | the boundary recorded; **no sign** | — | — |
| `A5S-4a` | P | branch (ii) with branch (iii); branch (i) not established, and not refuted | medium-to-high for (ii); high for (iii) as stated | a layer-1 warrant, or a layer-3 consumer; either reroutes the branch |
| `A5S-4b` | P | the A5 failure does not disqualify H-B's candidate as a **hydrodynamic** candidate | full, conditional on `A5S-4a` | `A5S-4a` landing at branch (i) or at a layer-3 requirement |
| `A5S-5a` | P | the residual list recorded, no item resolved | full | — |
| `A5S-5b` | P | the successor question named and left open | full | — |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction named.

## The adjudication rule, FROZEN

The classification is made on **two axes**, and the owner's three outcomes are the three readings
the round may report off them. The axes are stated separately because they are separately
falsifiable, and because a condition can be warranted at one layer and needed at none.

**Axis 1 — where A5's warrant is sourced.** Decided by `A5S-1` and `A5S-2`.

**Axis 2 — whether layer 3 needs A5.** Decided by `A5S-3`.

The three branches:

1. **A universal requirement of observational incompleteness itself.** Reported **iff** `A5S-1a` or
   `A5S-1b` exhibits a derivation of A5 — or of the amplitude-scale gauge principle it is
   equivalent to — whose hypotheses are layer-1 conditions alone and whose conclusion holds for
   every admissible substratum. **Absence of such a derivation on the record searched is not this
   branch's negation**; it is the absence of this branch's evidence, and the result note writes it
   that way.
2. **A completion principle specific to the quantum route.** Reported **iff** `A5S-2a` locates
   load-bearing consumptions inside the reconstruction/QM chain, `A5S-2b` records the corpus's own
   status for the principle as adjoined rather than derived, **and** branch 1's evidence is absent.
3. **Not a requirement of the Navier–Stokes target.** Reported **iff** `A5S-3a` finds no obligation
   among H1–H7, as stated, that names or needs A5, **and** `A5S-3b` stands. Reported with
   `A5S-3d`'s boundary attached, always.

**Branches 2 and 3 are compatible and may both be reported. Branch 1 and branch 3 are also
compatible** — a condition can be required of every admissible substratum and needed by no
hydrodynamic obligation — and the result note does not treat either as excluding the other. What
the round may **not** do is report a branch whose "iff" is unmet, or report the absence of one
branch's evidence as the presence of another's.

**The disqualification rule, FROZEN.** H-B's candidate is disqualified as a **hydrodynamic
candidate** by its A5 failure **only if** branch 1 is reported, **or** `A5S-3a` finds a layer-3
requirement. On any other outcome the round reports that the A5 failure does not disqualify it as a
hydrodynamic candidate, **and reports nothing further** — in particular nothing about the class's
admissibility as an OI substratum, which stays open.

## The status rule for the execution, FROZEN

Whatever the execution lands, the following binds the result note and every propagation of it.

1. **The execution may not report A5 disqualifying, or non-disqualifying, beyond what it proves.**
   Where the finding is that no warrant was found on a named record, the note says *no warrant was
   found on the record searched*, names the record, and states that this is not a proof that none
   exists. Where the finding is that no obligation as stated consumes A5, the note says *as stated*
   and carries `A5S-3d`'s boundary.
2. **The execution may not report the hydrodynamics obligation discharged.** Not H-B's, not H1's,
   not H2's, not any of H3–H7. No obligation moves status in this round; H-B is not reported closed;
   the programme's H-B entry is not reported discharged. H-B's own labels are cited at H-B's scope
   and are not restated more strongly.
3. **No label is written "for OI."** Every status, classification or finding in this round is a
   statement about a named object — a condition, a candidate, an obligation, a manuscript section —
   and never about observational incompleteness as such. "OI requires", "OI does not require", "OI
   has a fluid" and every variant are forbidden in terms; where the round's subject really is
   layer 1, the sentence names the record searched and what it says.
4. **Where the adjudication is undecided it is recorded UNDECIDED**, with the obstruction named,
   and the branch is not reported.
5. **The programme's HD/HC/HI/HO taxonomy is not applied to A5.** A5 is a condition, not a
   hydrodynamic obligation; the taxonomy labels obligations. The round's outputs are the branch
   classifications of the adjudication rule, and the round applies no taxonomy label to any
   obligation either (status rule 2).
6. **No manuscript is edited, and no divergence found in the corpus is resolved by this round.**
   `A5S-2c`'s finding is recorded and named for the owner.
7. `../PROGRAMME.md` §8's one-line state, when a later action refreshes it, carries the branch
   reported and the disqualification-rule consequence in the words this file uses, and nothing
   stronger. If the round lands where it predicts, that is: "A5's warrant is sourced at the
   reconstruction/QM layer on the record searched and no H1–H7 obligation as stated consumes it, so
   H-B's A5 failure does not disqualify its candidate as a hydrodynamic candidate; OI-substratum
   admissibility of the A1–A4, ¬A5 class remains open."

## What none of these outcomes licenses

- **Nothing here says observational incompleteness does not require A5.** A search that finds no
  warrant is not a no-go, and the round's layer-1 output is the absence of evidence on a named
  record (status rule 1, hazard 1).
- **Nothing here weakens A5's standing in the reconstruction chain.** Locating a condition's
  warrant at layer 2 is a statement about where it is warranted, not about whether it holds or
  whether the chain may use it. [SM §4.1]'s uniqueness argument, Stage 2's derivations and
  Theorem 23 consume A5 exactly as the manuscripts state, and this round changes none of them
  (hazard 2).
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
- **Nothing here changes A1–A6, their status, or their number.** A6 remains a `GAP` on its own
  branch; the wave representative's A1–A5 are consumed as proved; **no condition is added to the
  A-list or to the C-list, and none is named** (hazard 11).
- **Nothing here establishes that observational incompleteness has more than one emergent effective
  theory.** The three-layer separation is bookkeeping over obligations. That two targets may need
  different completion packages is the round's organizing frame, not a result of it (hazard 10).
- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity —
  control 1. The chain's manuscript sections are read as the location of a condition's warrant and
  for nothing else (hazard 12).
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
[Main §1], [Main §3]; [Structure §2.1], [Structure §9.6]; [Substratum §3.1], [Substratum §3.3],
[Substratum §3.5], [Substratum §3.6], [Substratum §4] Theorem 24 with its amplitude-scale-gauge
remark, that remark's *Status* note and its formalization-status note; [SM §2.7], [SM §4.1],
[SM §4.6]; `../PROGRAMME.md` §3, §4, §6, §7; `../round-h-a-source-audit/` and
`../round-h-b-reversible-fluid-substratum/` in full.

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
**no** existing one. It cites kernel results and re-proves none.

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

1. **Reading a layer-1 negative as a theorem.** "No warrant found on the record searched" is not
   "observational incompleteness does not require A5". The record searched is named, and the
   distinction is written into every sentence that reports the negative.
2. **Reading branch (ii) as a demotion of A5.** Locating A5's warrant at the reconstruction layer
   says where it is warranted; it does not weaken the reconstruction, and the chain consumes A5
   exactly as the manuscripts state.
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
   (`A5S-2c`); the round records both and adopts neither, and its adjudication does not turn on
   which is taken.
9. **Promoting a cited kernel result.** Nothing cited here gains strength by being cited, and no
   cited statement may be restated more broadly than the theorem that carries it.
10. **Building a bridge out of the layer frame.** That two targets may descend through different
    completion packages is the frame this round works in, not a result it establishes; no claim
    that observational incompleteness carries multiple emergent effective theories follows from
    anything here.
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

## Non-doings

The round does not: construct any substratum, candidate, stencil or coarse variable; write or edit
any Lean; re-prove any cited result; attempt a derivation of A5 from layer-1 conditions, or a proof
that none exists; take any continuum limit or assert any PDE; assert any statistical closure,
mixing or local-equilibrium statement; adjudicate any condition other than A5; test, weaken or
strengthen the alphabet-as-gauge or amplitude-scale-gauge principles; edit A1–A6, their kernel
status, or their number; resolve the divergence `A5S-2c` records; close or discharge any
obligation; edit `PROGRAMME.md`, `ROADMAP.md`, `README.md`, the census or any guard in this PR;
touch any manuscript; say anything about Track B, Track I, Bell, gravity or singularities.

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

## The named successor question

**What is the weakest OI substratum structure sufficient to produce a Navier–Stokes hydrodynamic
limit?** This round does not answer it. It supplies one input to it — the status of A5 relative to
the hydrodynamic target, adjudicated under the rule frozen above — and leaves the sufficiency
question to the programme's H3–H7 and to H-C, which fix the mixing/local-equilibrium condition, the
scaling map and the convergence topology before any limit is taken. If this round lands where it
predicts, the immediate successor on this branch is H3 and H4 for H-B's candidate, with the
candidate's A6 status, its dimension, and its class's OI-substratum admissibility all still open.

## Allowed final report

1. **`A5S-0`** — the two statements of A5, the absence of an identification theorem, and the
   sourcing of all six conditions as inputs to the reconstruction;
2. **`A5S-1`** — the layer-1 search, the record searched named, the result stated as absence of
   evidence and not as a no-go; the kernel enumeration with its two lists and the OI → QM finding,
   with the frozen reading attached;
3. **`A5S-2`** — the located consumptions in the manuscripts' own words; the corpus's own status
   for the principle; the two statements of the entailment question, recorded side by side and
   neither adopted, with the propagation question named for the owner;
4. **`A5S-3`** — H1–H7 walked one at a time as stated; H-B's positive results read together with
   its A5 failure, at H-B's labels and scope; H-A's advection gate with its hypothesis and its
   class named; and the boundary of the negative;
5. **`A5S-4`** — the branch or branches reported under the adjudication rule, with the evidence and
   its boundary; UNDECIDED where undecided; the disqualification-rule consequence for H-B's
   candidate, in this file's words and no further;
6. **`A5S-5`** — the residual list, no item resolved; the successor question, named and open;
7. what the outcomes do **not** license, in this file's wording;
8. the definition budget, recorded as zero definitions introduced;
9. the chronology certification: the blob pin by content, the base, and the record that no guard
   was added or modified.

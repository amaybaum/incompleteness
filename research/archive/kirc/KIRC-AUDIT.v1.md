# K/I/R/C assumption audit — read-only, from L42

Baseline `fdebc6e39498367e15a8352fe0f01f8f75ab3671` (A42 landed). Nothing here is committed, frozen or claimed; it is a
map of where each assumption of the operational endpoint comes from. Supporting files beside this one:
`kernel_defs.md` (verbatim Lean, file:line), `literature.md` (citation verification, with UNVERIFIED tags).

**Status vocabulary.**
- **DERIVED** — a kernel theorem produces it from weaker premises.
- **NATIVE** — an OI premise (A1–A6, C1–C4, the substratum) supplies it directly.
- **EQUIV** — it matches, or is equivalent to, a known reconstruction principle (literature cited).
- **IMPORTED** — it is built into a type or taken as a hypothesis, with no derivation in the corpus.
- **OPEN** — the audit could not decide it.

Several rows carry two labels, for example IMPORTED + EQUIV: assumed in the kernel, and the same as a known principle.

***

## 0. The headline findings

1. **The representation theorem uses no complex numbers.** `S ⇔ D ⇔ Q_fb` (`Equivalence.lean`) takes the unitary of
   `D_imp_Qfb` (:294) to be `Equiv.Perm.permMatrix ℂ R.step.symm`, a 0/1 permutation matrix. `Qfb_imp_S` (:245) uses
   only unit-norm columns, and the other half of `QuantumRepresentationT2`/`T3` uses a permutation matrix and a real
   Hadamard. The equivalence would hold verbatim over permutation or real orthogonal `U` (a reading of the proof; no
   restricted version is formalized). So the fixed-basis/Born layer, the one bridge the corpus has from OI's
   stochastic laws toward quantum kinematics, **selects no number field.**
2. **The whole operational layer is hard-coded to complex matrices.** `FiniteOperationalTheory`
   (`OperationalAssembly.lean:594`) has no field parameter. Its carriers are `Matrix A A ℂ`, its composites are Kronecker
   products, and its operations are `→ₗ[ℂ]` maps. No type in the kernel can express real, quaternionic, Jordan-algebraic
   or non-matrix theories, and no comparison with them exists. The corpus never states this as a presupposition;
   `Main.md:262`'s "introduces no quantum postulates" is correct only for the diagonal embedding of classical
   distributions it describes.
3. **ℂ enters the proofs exactly through R.** The reversible-richness certificate `HControl`
   (`MonoidalCompletion.lean:349`) takes the real Lie span of `−i·U_g H U_g†` and flows by `exp(−itH)`; `Complex.I` is
   in the generators. The kernel's own native-repertoire results point the same way:
   - `MinimalRepertoire.lean` shows drive-plus-permutation sets generate only (phase-conjugated) real antisymmetric
     matrices (`not_hControl_two` at :362);
   - `RealPairFlow.lean` reaches QM from a real rotation flow only when complex `phaseGate`s
     (`LieRankSource.lean:209`) are added as a separate hypothesis;
   - the corpus calls this "an empirical controllability resource", not entailed by A1–A6 (`GR.md:260`,
     `Main.md:568`, `PROGRAMME.md:80`).

   **So K (the field) and R are coupled in this corpus.** The one place a complex phase is consumed is the control
   resource that is already recorded as imported.
4. **In the literature, what picks ℂ over ℝ and ℍ is almost always local tomography or composition**: Hardy's
   `K = N^r`, CDP's local distinguishability, Masanes–Müller, Dakić–Brukner, Barnum–Wilce, and Renou et al. through
   tensor-product composition. The only exception found is Barnum–Müller–Ududec, where energy observability does it
   among single-system postulates. The kernel proves local tomography only inside ℂ (`local_tomography_physical`,
   `InstrumentDilation.lean:440`) and never uses it to exclude ℝ. The manuscripts say the substratum's kinematic
   locality "does **not**, by itself, prove local tomography" (`Main.md:212`, `:542`, `:628`; `Substratum.md:138`).
5. **I, R and C are each close to a standard reconstruction ingredient.** None is new in kind; what is new is their
   isolation as three independent axes over one OI core. I is the trivial-extension argument for complete
   positivity, R is Lie-rank controllability, C is purification-as-closure or discard-closure. §2 gives the details.
6. **A tension for I (a lead, not a result).** The standard critique of the trivial-extension argument is that reduced
   dynamics need not be CP when system and environment start correlated (Pechukas 1994; Buscemi 2014 gives the exact
   condition). OI's visible system is by construction correlated with a hidden sector. The kernel's spectators are
   fresh, adjoined systems (`withSpectator`), so the tension bites only if the hidden sector plays the spectator's
   role. The corpus cites Pechukas once (`Main.md:149`) and never connects it to I.

***

## 1. K — the ambient kinematics

| # | assumption | where it enters | status | literature equivalent | notes |
| --- | --- | --- | --- | --- | --- |
| K1 | finite dimension | substratum finite set; `Fintype` carriers | NATIVE (A1) | MM "finite information capacity" | the one kinematic item OI supplies |
| K2 | scalar field ℂ | `FiniteOperationalTheory` type; `HControl` generators (`Complex.I`); `phaseGate` | IMPORTED | selected by local tomography (Hardy, CDP, MM, DB, BW), by energy observability (BMU 2014), or by tensor composition (Renou 2021) | not used by `S ⇔ D ⇔ Q_fb`; consumed only through R |
| K3 | full matrix algebra, as opposed to a general cone or Jordan algebra | carrier `Matrix A A ℂ` | IMPORTED | self-duality from bit symmetry (Müller–Ududec 2012); Koecher–Vinberg ⇒ Euclidean Jordan algebras; no higher-order interference (BMU) | Solèr narrows to ℝ/ℂ/ℍ but does not choose |
| K4 | composition = Kronecker product | `tensorOf`, `withSpectator`, `A × Fin n` | IMPORTED | composition postulates; local tomography ⇔ `K_AB = K_A K_B`; quaternionic QM fails the tensor product (Adler) | `Main.md:212` says kinematic locality does not by itself give local tomography |
| K5 | operations linear | `→ₗ[ℂ]` maps | IMPORTED (+ EQUIV) | in GPTs, linearity follows from convex mixing of preparations | standard, but not derived here |
| K6 | positive semidefinite states, trace normalization | enter only through `CompositeOperationalValidity` (WF) | IMPORTED via WF | the GPT state cone; for matrices, self-dual PSD | no state type in the structure |
| K7 | fixed-basis Lüders readout | `readout`; `readout_is_localLuders` | DERIVED | — | the readout is forced, not assumed |
| K8 | pure seed | only uniform attachment is assumed; the pure seed is derived | DERIVED | — | |
| K9 | stochastic laws ⇔ reversible ⇔ fixed-basis unitary | `finite_horizon_equivalence` | DERIVED, field-free | Barandes' correspondence | holds with permutation `U`; selects no field |

**Reading.** K1 is native; K7–K9 are derived; K2–K6 are imported at the level of types. The corpus's only native
bridge toward quantum kinematics (K9) is field-independent. Nothing in the corpus derives ℂ, the matrix algebra or the
tensor product.

## 2. The principles

| principle | kernel definition | status | closest literature | criticism in hand |
| --- | --- | --- | --- | --- |
| WF-1 valid probabilities | `CompositeOperationalValidity` (`OperationalValidity.lean:88`): PSD ↦ PSD per branch, aggregate trace-preserving | IMPORTED + EQUIV | the basic GPT consistency requirement | — |
| WF-2 trivial-ancilla consistency | `SystemToLevelOne` | IMPORTED + EQUIV | consistency of the subsystem description | — |
| **I** inert spectators, also called observational independence | `InertSpectatorCompositionality` (`SpectatorBridge.lean:223`); `ObservationalIndependence` (`CompletedOI.lean`), proved equivalent | IMPORTED + EQUIV | trivial-extension argument for CP (Kraus 1983, Stinespring, Choi) | Pechukas 1994; Alicki 1995; Jordan–Shaji–Sudarshan 2004; Buscemi 2014 (CP ⇔ no backward information flow from the environment). Census cells with I failing: `countermodel`, `diagTwoPosTheory`, `cappedTheory`, `cappedDiagTheory` (2-positive, non-CP) |
| **R** reversible richness | `ReversibleRichness` (`CompletedOI.lean:171`, `CarrierGeneralOIPlus.lean:110`): "undo" (if conjugation by `V` is available, so is conjugation by `V†`) plus the `HControl` certificate (drift `H`, unitary controls, real Lie span of `−i U H U†` ⊇ traceless skew-Hermitian) | IMPORTED + EQUIV | Lie-algebra rank condition (Jurdjevic–Sussmann 1972; Ramakrishna et al. 1995); in reconstructions, Hardy's continuity axiom, MM symmetry, BMU strong symmetry, Müller–Ududec bit symmetry | carries ℂ itself (`−i`). Native-repertoire obstructions: `MinimalRepertoire` (real antisymmetric only), flow-extension audit (gate-flow algebra ≠ su(D)). Census cells with R failing: `diagTheory`, `diagTwoPosTheory`, `diagGapTheory`, `cappedDiagTheory` (diagonal-preserving) |
| **C** iterated composition, also called observer recursion | `IteratedAncillaClosure` (`AncillaClosure.lean:247`); `ObserverRecursion`/`IsShiftedTheory`, proved equivalent | IMPORTED + EQUIV | purification as closure (CDP 2010: every process is a reversible interaction with a discarded environment); Huot–Staton 2018 (freely adding discarding to isometries gives CPTP); Hardy 2011 "compound permutability" (closeness not checked) | census cells with C failing: `gapTheory`, `cappedTheory`, `diagGapTheory`, `cappedDiagTheory` (level-capped or rank-gap classes) |

**Reading.** Each principle is a known ingredient in operational form. What the corpus adds is the three facts
together:
- they are pairwise independent over one sealed OI core (`substantive_census`, `no_boolean_relation`);
- CP follows from I plus validity (`krausSoundExt_of_validity_inert`);
- the characterization holds on every finite carrier (`exactAll_iff_physical_general`, `oiPlus_iff_qm`).

All of this sits inside K2–K6.

## 3. The criticism set

**(a) Inside the kernel's kinematics — the eight census cells.** All are qubit theories that are well-formed and
realize the sealed OI core. They are in `kernel_defs.md`.

| failing principles | theory | composite maps |
| --- | --- | --- |
| none | `fullQuantum` | CP |
| I | `countermodel` | 2-positive |
| R | `diagTheory` | CP, diagonal-preserving |
| C | `gapTheory` | rank-gap Kraus sums |
| I, R | `diagTwoPosTheory` | 2-positive, diagonal-preserving |
| I, C | `cappedTheory` | 2-positive, CP at levels ≤ 3 |
| R, C | `diagGapTheory` | CP, diagonal-preserving, rank-gap at levels ≤ 3 |
| I, R, C | `cappedDiagTheory` | 2-positive, diagonal-preserving, CP at levels ≤ 3 |

**(b) Outside the kernel's kinematics — alternatives the types cannot express.** Each needs a field-free or cone-level
framework before any OI principle can be tested against it.

| alternative | OI-native status | what excludes it in the literature |
| --- | --- | --- |
| classical simplex | **realized**: the OI core and `D` are permutation dynamics; `S ⇔ D ⇔ Q_fb` works with permutation `U` | continuity of reversible dynamics (Hardy axiom 5); purification (CDP) |
| real QM (Stueckelberg) | not expressible; permutation and real-orthogonal lifts are enough for `K9` | local tomography; Renou et al. under tensor composition (Hoffreumon–Woods 2026 dispute testability) |
| quaternionic QM | not expressible | composition / tensor product (Adler); local tomography |
| spin factors, other Jordan algebras | not expressible | local tomography with a qubit (Barnum–Wilce); BMU postulates plus energy observability |
| boxworld / PR boxes | not expressible | purification; boxworld's reversible dynamics are trivial (Gross et al. 2010, UNVERIFIED) |
| theories with higher-order interference | not expressible | no higher-order interference (BMU) |

**(c) Native OI facts that already discriminate kinematics (leads to check, not results).**
- **The trivial-ancilla lift is field-sensitive.** A45's trivial-ancilla lift needs a unitary `U` with `G = |U|²`, so
  the slice must be unistochastic. Over ℝ it would have to be orthostochastic, which is strictly smaller.
  - The flat three-state law `J/3` is an OI visible law: a Latin-square bijection with a three-state hidden sector
    realizes it.
  - It has the complex Fourier lift but no real orthogonal lift, because two ±1 rows of odd length are never
    orthogonal.
  - So at trivial ancilla, ℝ cannot represent some OI visible laws that ℂ can. This does not separate ℂ from ℍ, and
    with a carried ancilla the permutation dilation is always available.
- **P0's continuous lift freedom depends on the field.** At the certified 16-state point, real flat lifts are real
  Hadamard matrices. There are finitely many up to equivalence (five for order 16 per Hall 1961: UNVERIFIED count).
  The continuous complex Hadamard families that acts 11–45 classify (the Diţă strata, defects 33–49) exist because the
  field is ℂ. Part of `P0`'s underdetermination is therefore a consequence of K2.

## 4. What the map says, and what it suggests

1. **K is untouched by the corpus's derivations.** The one native bridge (`K9`) is field-free, and every other
   kinematic item beyond finiteness is imported by type. The honest current statement is:
   `OI⁺ ⟺ exact finite endomorphic operational QM` holds **within complex-matrix kinematics with Kronecker
   composition**. The manuscripts do not say "within complex-matrix kinematics"; that is a scope sentence worth adding
   eventually, by the corpus's own claim/evidence rule, but it is not edited here.
2. **K and R do not separate cleanly.** ℂ is consumed only through R's certificate. This matches the literature, where
   continuous reversible interaction plus local tomography is what fixes the complex Bloch ball (Masanes–Müller). A
   field-free restatement therefore likely has two parts:
   - (i) a native local-tomography statement for OI composites;
   - (ii) a reversibility or transitivity statement without `−i`.

   The ℂ-selection would then be a theorem instead of a type.
3. **I is the ingredient most exposed to physical criticism.** Its standard justification fails under initial
   correlations, and OI's visible systems are correlated with the hidden sector. The first question is which physical
   system realizes the spectator or reference in OI: a fresh independent system (I is safe) or the hidden sector
   (Pechukas/Buscemi apply). A45's result that an ancilla carried between steps separates two lifts of one law is
   adjacent evidence that hidden correlations can matter.
4. **C is closest to a known closure principle.** It is effectively purification-closure or discard-closure, and it
   already reads as structural.

**Suggested order (not started):**
1. **K/R jointly:** field-free local tomography plus field-free reversibility, with real QM, quaternionic QM and the
   classical simplex as controls, and the two leads above as native discriminators to check first.
2. **I:** the spectator-identity question and the Buscemi condition for OI's visible/hidden split.
3. **C** last.

## 5. Items to verify before any citation

These come from `literature.md`; the primary sources could not be fetched.
- the full postulate list of Selby–Scandolo–Coecke and which postulate selects ℂ;
- that real QM satisfies every CDP principle except local distinguishability;
- whether Hardy 2001 derives complete positivity;
- whether Masanes–Müller's symmetry requirement includes continuity;
- the Vinberg citation;
- Renou et al.'s author list;
- Gross et al. 2010 on boxworld dynamics;
- Hall 1961's count of order-16 Hadamard classes;
- some page and volume numbers.

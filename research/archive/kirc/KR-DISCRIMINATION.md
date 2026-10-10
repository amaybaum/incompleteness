# K/R discrimination — read-only, from L42

Baseline `fdebc6e3`. The question: can a native principle — local tomography, compositional distinguishability,
continuous reversible mixing, or a combination — rule out real, quaternionic, Jordan-algebraic and GPT alternatives
**without** putting ℂ, `SU(D)` or `su(D)` into its premise? This establishes what each candidate discriminates. No
theorem work, no freeze, nothing committed.

Evidence tags: **[P#]** an exact check in `kr_probes.py` (sympy and Fractions; 20 PASS, 0 FAIL, log `kr_probes.log`);
**[kernel]** a landed Lean result; **[lit]** literature (verification status in `literature.md`); **[open]** undecided.

## 1. The candidates, stated field-free

| id | candidate | field-free statement |
| --- | --- | --- |
| **LT** | local tomography, also called compositional distinguishability or local distinguishability | a joint state of a composite is determined by the statistics of products of local effects; in counting form `K_AB = K_A K_B` |
| **CRM** | continuous reversible mixing on a pair | a continuous one-parameter group of reversible transformations acting transitively on a two-level system's pure states |
| **CRI** | continuous reversible interaction | a continuous reversible transformation of two elementary systems that is not a product (it entangles) |
| **PUR** | purification | every state is the marginal of a pure state of a larger system, unique up to a reversible map on the purifying system (Chiribella–D'Ariano–Perinotti) |
| **TAL** | trivial-ancilla lift universality | every visible law has a reversible lift with trivial ancilla |

## 2. The discrimination matrix

✓ = the control satisfies the candidate, ✗ = the candidate excludes it.

| candidate ↓ / control → | classical simplex (OI core) | real QM | complex QM | quaternionic QM | spin factors / balls, d ≥ 4 | boxworld | census no-control cell `diagTheory` | `J/3` | `(J−I)/2` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LT** | ✓ [P1] | ✗ [P1, P2] | ✓ [P1; kernel `local_tomography_physical`] | ✗ [P1; lit Adler] | ✗ with a qubit and composition [lit Barnum–Wilce] | ✓ [lit, UNVERIFIED] | — (ℂ by type) | n/a (single system) | n/a |
| **CRM** | ✗ (only finite permutations) | ✓: real rotations generate `so(D)` [P5] | ✓: complex drives generate `su(D)` [P5] | ✓ [lit, not probed] | ✓ (rotations of the ball) [lit] | ✗ [lit Gross et al., UNVERIFIED] | ✗: diagonal generators are abelian of dimension `D` [P6] | real CRM cannot give the lift [P3] | no field gives the lift [P4] |
| **LT + CRM / CRI** | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | — | — |
| **LT + PUR** (with the other CDP axioms; no continuity) | ✗ (no purification) | ✗ (LT) | ✓ | ✗ | ✗ | ✗ | — | — | — |
| **TAL** | ✗ | ✗ [P3] | ✗ [P4] | ✗ [P4] | ✗ [P4] | — | — | ℂ ✓, ℝ ✗ [P3] | every field ✗ [P4] |

Notes on the matrix.
- **LT alone** removes real and quaternionic QM by parameter counting. Real QM has *more* global parameters than local
  products (`K(4) = 10 > K(2)² = 9`); quaternionic has fewer (`28 < 36`) [P1]. The real-QM witness is explicit:
  `σ_y ⊗ σ_y` is real symmetric and orthogonal to all nine products of real symmetric local observables, so
  `ρ_± = (I⊗I ± σ_y⊗σ_y)/4` are distinct real states with identical local statistics; over ℂ, `σ_y` is observable and
  separates them [P2]. **LT does not remove the classical simplex or boxworld.**
- **CRM alone** removes the classical simplex, boxworld and the no-control cell, but **not** real, quaternionic or ball
  kinematics. The field of the pair flow decides the algebra:
  - one real rotation generator with its permutation conjugates closes on `so(D)`: dimensions 3, 6, 10 for D = 3, 4, 5;
  - one complex drive `−iX` with its conjugates closes on `su(D)`: dimensions 8, 15, 24;
  - the two-state drive plus swap gives dimension 1, the kernel's bipartite obstruction [P5, reproducing
    `MinimalRepertoire` independently].

  So a field-free CRM chooses nothing; the field is carried by the generator.
- **LT + continuity (CRM/CRI)** is the Hardy / Masanes–Müller / Dakić–Brukner route: it isolates complex QM among the
  controls, but only inside a GPT framework with further postulates. Masanes–Müller use five requirements, not these
  two alone. de la Torre et al. assume quantum qubits locally and derive the global theory, so it is not a local-field
  selection [lit].
- **LT + PUR** is the Chiribella–D'Ariano–Perinotti route. It needs **no continuity axiom** [lit].
- **TAL is refuted for every field** [P4], so it is not a candidate. `J/3` is a comparative discriminator only, and it
  does not bear on `D_imp_Qfb`, whose dilated realization is a permutation [kernel].

## 3. What this establishes

1. **No single native candidate selects ℂ.**
   - LT separates ℂ from ℝ and ℍ but leaves the classical simplex and boxworld.
   - Continuity (CRM) separates quantum from classical and boxworld but leaves ℝ and ℍ.
   - Complex QM is isolated only by a pair: LT + continuity, or LT + purification, each inside a GPT framework with
     further postulates.

   The finite shadow is exact in P1, P2 and P5: real rotations give `so(D)` and fail LT; complex drives give `su(D)`
   and pass it.
2. **R's `−i` is the field choice itself, not an extra.** A field-free CRM supplies continuity and nothing about the
   field [P5]. If the native field-selector is to be LT, then with a real pair flow LT must itself **produce the phase
   gates** that `RealPairFlow` currently takes as a separate hypothesis. That is a precisely posed target, and it is
   where the literature's local-field results (Barnum–Wilce; Hardy's counting) would have to be matched natively.
3. **Continuity is not native to a finite substratum.** OI's A1 makes the substratum finite and discrete. The corpus
   records continuous controllability as an imported, empirical resource (`GR.md:260`, `Main.md:568`,
   `PROGRAMME.md:80`) and dense control from the present architecture as settled negatively (`ROADMAP.md:1266`).
   Every continuity-based route (Hardy, Masanes–Müller, the LT + CRI results) therefore imports exactly what OI does
   not supply.
4. **The continuity-free route is LT + purification.** Among the reconstructions compared, only Chiribella–D'Ariano–
   Perinotti selects complex QM without a continuity axiom. Their purification (existence with essential uniqueness)
   is close to the corpus's C: C is closure under attaching and discarding an ancilla, and purification is equivalent
   to every process being a reversible interaction with a discarded environment. The kernel proves purification
   existence and Uhlmann uniqueness **as mathematics inside ℂ** (`Purification.lean`, `UhlmannUniqueness.lean`), not as
   axioms. **Lead:** the natural K-selector for a finite substratum may be LT together with a C-type purification
   principle rather than R. That would move the field question from R to C, the most kinematically neutral of the
   three. [open]

## 4. Controls, as requested

| control | role | result |
| --- | --- | --- |
| `J/3` | trivial-ancilla lift, ℝ vs ℂ | complex Fourier lift exact; no real lift [P3]. Comparative only: `(J−I)/2` has no lift over any field [P4]. |
| real QM | must be excluded by the candidate | excluded by LT [P1, P2]; not by CRM [P5] |
| quaternionic QM / Jordan | must be excluded | ℍ excluded by LT counting [P1] and composition [lit]; spin factors by LT with a qubit [lit Barnum–Wilce] |
| no-control census cell `diagTheory` | the R-failure cell | fails CRM: diagonal generators are abelian, no superposition [P6]; its ℂ is by type, so LT is vacuous there |
| classical simplex | the OI core itself | passes LT, fails CRM and PUR — continuity or purification is what separates it |

## 5. The next read-only questions, in order (none started)

1. **LT natively.** State local tomography for OI visible composites without ℂ, as joint visible statistics
   determined by local visible statistics. Check whether the substratum's composition — graph cones, product
   partitions — implies it. The corpus says kinematic locality alone does not (`Main.md:212`).
2. **LT ⇒ phase gates?** Given a real pair flow, does LT force the phase gates `RealPairFlow` assumes? Check first
   whether this matches or contradicts Barnum–Wilce and Hardy in the finite setting.
3. **LT + PUR / C.** Compare the corpus's C (iterated ancilla closure) with CDP purification: exact equivalence,
   strict strengthening, or neither. If C is close to PUR, the K-selector could avoid continuity entirely.
4. **Verification.** The citations marked UNVERIFIED in `literature.md` and the de la Torre et al. details are to be
   checked against full texts before any written use.

# Conditional complex-QM benchmark: premise ledger, dependency map and control scores

> **DRAFT — NOT FROZEN.** Design note for the owner. It preregisters nothing, adopts nothing and changes no manuscript.
> Its verdict rules are proposals until the owner fixes them.

Base: `main` at `fc9018e8`. Drafted on owner instruction (2026-10-22) to keep two routes side by side.
The first deliverable has three parts: the premise ledger, the theorem-dependency map, and scores for the established
controls. Proposed OI constructions are scored only after the control scores are reviewed.

Evidence tags:
- **[kernel `name`]** is a Lean result cited from GR §3.3 at `fc9018e8`; no `lake` build was run for this note.
- **[lit, owner-checked]** is a literature theorem whose statement and surrounding definitions the owner checked on
  2026-10-22. The scope below is the owner's reading. This environment cannot reach the sources (§7).
- **[std]** is a standard textbook fact.
- **[exact, file]** is a computation in this directory or a cited sibling directory.
- **[arg]** is a short written argument, not reviewed.
- **[open]** is undecided.

## 1. Two routes, two jobs

| Route | What it establishes | What it does not establish |
|---|---|---|
| **L**, literature | It selects complex quantum theory within a specified class of operational theories | That OI supplies the premises |
| **K**, kernel | It characterizes quantum-complete operations within the declared complex-matrix framework | Real-versus-complex selection, or a physical implementation |

The two routes are not equivalent, and no formal map between their premise sets is claimed (§A.34). A candidate is
scored against each route separately.

## 2. Premise ledger

### 2.1 Route K (GR §3.3)

**Framework (fixed, not a premise to score).**
- A nonempty finite carrier.
- An operational theory on it: for the system and every finite ancilla level, the available finite outcome families of
  linear maps on complex matrices. These are closed under coarse-graining and outcome-conditioned composition, with a
  spectator-independent local ancilla readout.
- **Conclusion scope:** exact finite endomorphic operational QM on that carrier. It says nothing beyond that.

| ID | Premise | Kernel |
|---|---|---|
| K-W1 | (i) Valid probabilities: positive states go to positive states, and the outcomes' traces sum to the input trace | part of `OIPlus`; `exactAll_iff_physical_general` |
| K-W2 | (ii) Trivial-ancilla consistency | same |
| K1 | (iii) Observational independence (inert spectators) | `observationalIndependence_iff_inert` |
| K2 | (iv) Reversible richness: operational inverses and a Lie-rank certificate at every composite level, giving full composite unitary control | `control_of_reversibleRichness`, `control_of_lieRank` |
| K3 | (v) Observer recursion (iterated composition) | `closure_of_observerRecursion` |

- **Theorem.** K-W1, K-W2, K1, K2 and K3 hold if and only if the theory is exact finite endomorphic operational QM
  (`carrier_general_oiPlus`, `oiPlus_iff_completedOI`).
- **Independence.** Each of the five conditions is independent of the other four (`five_way_minimality`).

**Alternative certificate K2′, the primitive-source form** (`carrier_general_oiPlusMin`, `oiPlusMin_iff_qm`).
- Implementation locality, phase-free richness and embedded observation together are equivalent to the same
  conclusion.
- Phase-free richness asks for one continuously drivable pair of distinguishable states and every exchange, at every
  composite level with at least two states. No quarter phase is postulated (`control_of_phaseFree`).
- **What K2′ still needs a source for:** the continuously driven transition.
- **Layer-flow form** (`derivedOI_qm_iff_layerFlowExecutable'`). Within the substratum's closure, with the phase
  intervention stated, QM holds exactly when one nontrivial layer flow is executable.
- **Substratum-source form.** The current substratum plus continuous off-diagonal controllability is equivalent to QM.
  There, the phase intervention is an assumption on the substratum class.

### 2.2 Route L (Krumm–Müller, then de la Torre–Masanes–Short–Müller) [lit, owner-checked]

| ID | Premise |
|---|---|
| L1 | Each elementary system's state space is a Euclidean ball Bᵈ with **d ≥ 2**, with the specified state/effect pairing: sharp directional tests p(+ \| a, b) = (1 + a·b)/2 |
| L2 | All local SO(d) rotations are available reversible transformations |
| L3 | Operational no-signalling |
| L4 | Local tomography: joint probabilities of local measurements, correlations between local outcomes included, determine the joint state |
| L5 | The reversible transformations of composites form a **closed, connected group** that contains the local rotations and includes a **genuine interaction**, i.e. one not a product of local transformations |
| L6 | Consistent extension to **arbitrary numbers of identical systems**, including spectators and relabelling |

- **Step 1, Krumm–Müller Theorem 1** [lit, owner-checked]. The hypotheses are:
  - ball state spaces;
  - all local rotations;
  - no-signalling;
  - local tomography;
  - a closed connected reversible group.

  Under them, a genuine interaction requires ball dimension d = 3.
- **Step 2, de la Torre et al. Theorem 2** [lit, owner-checked]. The hypotheses are:
  - identical local qubits;
  - local tomography;
  - continuous reversible interaction;
  - consistent extension to additional systems.

  Under them, the quantum composite theory is recovered.
- Local tomography alone does not select complex QM.
- **Partial kernel coverage:**
  - The conditional pair-cone theorem (`round-oi-pair-maxcone-1`) identifies the two-system cone given eball 3 and its
    other hypotheses. A two-system result does not complete step 2, which needs the identical-system extension.
  - COMP-1 makes local tomography an explicit, independent premise of composite structure (padding control).
- **Coverage obligation.** Route L reaches finite collections of qubits. Identifying every OI system with an encoded
  system in that family is a further obligation, scored as its own line (L7) where a candidate claims it.

## 3. Theorem-dependency map

```
Route L
  L1 (d ≥ 2, pairing) ┐
  L2 (all SO(d))      │
  L3 (no-signalling)  ├─ Krumm–Müller Thm 1 ──> d = 3 ─┐
  L4 (local tomogr.)  │                                 ├─ de la Torre et al. Thm 2 ──> complex QM,
  L5 (closed connected│                                 │                               finite qubit collections
      group + genuine │  L4, L5 (continuous), L6 ───────┘          └─ L7 (coverage) ──> every OI system
      interaction)    │
  L6 (n identical)    ┘

Route K (complex-matrix framework fixed)
  K-W1, K-W2, K1, K2, K3 ── carrier_general_oiPlus ──> exact finite endomorphic operational QM
  K2 <── K2′: implementation locality + phase-free richness + embedded observation (carrier_general_oiPlusMin)
                 └─ needs a source for one continuously driven transition
```

The arrows are only the cited theorems. A premise discharged for one candidate under one operational interpretation
is not reused for another interpretation or another completion.

## 4. Scoring rules (proposed)

**Marks.** Each premise, for each candidate, gets one mark and one evidence entry.

| Mark | Meaning |
|---|---|
| Native | Follows from the **frozen baseline** (below), with evidence |
| Added | Supplied by structure not in the frozen baseline. Its content and dependencies are recorded in words |
| Fails | An exact witness shows the premise fails, for the stated encoding and operations |
| Open | Undecided |

| Evidence | Meaning |
|---|---|
| proof | kernel, written proof, or standard result |
| bounded | exact finite computation within stated bounds |
| assumption | taken as given |

**Frozen baseline for Native.**
- It is the corpus at `fc9018e8`: A1–A6, C1–C4, the displayed update (Main.md:290), the whole-site visible partition
  (Main.md:292, :316), the observer sourcing of `SubstratumInterface`, and the counting measure (Main.md Lemma 3).
- An observer restriction declared later stays **Added**, even if it is made part of the interface. Examples are
  positions-only reads, compatible records, and the polarization map.

**Verdicts.**
- **Theorem verdict, "conditional complex QM reached (route X)".** Every hypothesis of route X's theorems is
  discharged as Native or Added with proof-level evidence. All of them must hold for the **same** candidate, the
  same operational interpretation and the same completion.
  - Bounded evidence can establish Fails, or support Open. It never discharges a universal premise.
  - Any control red voids every verdict.
- **Added premises are not counted as a distance from a derivation.** One compact assumption can contain nearly the
  whole target. The ledger records what each Added premise says and what it depends on.
- **Adoption verdict, kept separate (§A.29).** A candidate can reach the theorem verdict and still fail the project's
  adoption criterion.
  - Adoption needs at least one consequence outside the examples used to choose or tune the candidate, with the
    evidential independence explained.
  - The consequence need not be a deviation from QM.

**Exact versus approximate.** Exact-endpoint claims and finite-accuracy claims sit in separate columns. A sequence of
increasingly successful finite models establishes an endpoint premise only with two things:
- a declared convergence notion;
- a proof that the premise survives the limit (LIMIT-DESIGN's declarations 1–4).

## 5. Diagnostics, kept apart from conclusions

| Diagnostic | Role |
|---|---|
| D1 Quarter phase available (the C5 audit's O1) | Diagnostic only. A rich enough continuous control structure generates it, as K2′ does |
| D2 Operations beyond Clifford/stabilizer | Diagnostic only. Reaching D1 does not reach D2 |
| D3 Product-effect span versus closed joint span | A finite test of L4. A strict increase under an interaction witnesses missing joint information |
| D4 Continuous endpoint (O2) | Needs the convergence notion of §4 |
| D5 Exclusion controls (PR box and others) | One exclusion control each. Excluding all non-quantum states, effects and operations needs the reconstruction argument, not a finite set of Bell tests |

## 6. Control scores (the first deliverable)

Each row's mark is for the stated encoding and operations only. In the tables below, Pass means the control satisfies
that premise; the theorem verdict counts only Native or Added, as §4 defines them. D3 for four rows is computed in
`bench_controls_span.py` [exact]: product span 16 of 16 for complex QM and the stabilizer theory, and 9 below the joint
10 for the rebit and the real Clifford class.

### 6.1 Route L

| Control | L1 | L2 | L3 | L4 | L5 | L6 | Route L verdict |
|---|---|---|---|---|---|---|---|
| Complex QM, finite qubits | Pass, B³ [std] | Pass [std] | Pass [std] | Pass [exact; std] | Pass, genuine interaction e.g. CNOT [std] | Pass [std] | **positive control:** reached |
| Report 3/4 interpreter | Added, quantum rules imported | Added | Added | Added | Fails at any fixed carrier (fixed-carrier recurrence lemma, report 3) | Added for bounded families | calibration only; never a witness |
| Real QM (rebits) | Pass, B², d = 2 [std] | Pass, SO(2) [std] | Pass [std] | **Fails** [exact: ρ± agree on the 9-dimensional product span; report 5] | Pass, exp(θ J⊗X) [exact, report 5] | Pass [std] | not reached; fails at L4 |
| Real Clifford class (test-8 N2: H, CZ, Paulis, relabellings, position encoding) | **Fails**: one-site states form a square in x–z [arg] | **Fails**: finite group | Pass [arg] | **Fails** [exact: ρ± prepared in the class, report 5 check] | **Fails**: no connected group (countable) | Open | not reached. Distinct from full real QM |
| Qubit stabilizer: finite preparations | **Fails**: 6 points [std] | **Fails**: 24 rotations [std] | Pass [std] | Pass [exact; std] | **Fails**: finite group [std] | Pass [std] | not reached |
| Qubit stabilizer: convex closure | **Fails**: octahedron, not B³ [std] | **Fails** | Pass | Pass | **Fails** | Pass | not reached |
| Spekkens toy theory | **Fails**: polytope of 6 epistemic states [std] | **Fails**: finite group (S₄ symmetries) [std] | Pass [arg] | Open | **Fails**: finite group | Open | not reached |
| Classical bit | **Fails** the declared d ≥ 2; its interval is both a simplex and B¹ [std] | trivial | Pass | Pass [std] | **Fails**: permutations only | Pass | not reached |
| Boxworld (gbits, maximal tensor product, reversible dynamics) | **Fails**: square state space, not a disc [std] | **Fails**: finite symmetry group | Pass, by construction | Pass [std] | **Fails**: no genuine reversible interaction; only local operations and permutations [lit, owner-checked: Gross–Müller–Colbeck–Dahlsten 2010, Theorem 1. In the specified full boxworld, reversible transformations are local relabellings and subsystem permutations. This is not a theorem about every theory containing a PR box; the paper discusses exceptions for classical–boxworld hybrids] | Pass | not reached; fails L1, L2, L5 |
| PR box (exclusion control D5) | n/a | n/a | Pass | n/a | n/a | n/a | admitted by a candidate means D5 fails for that candidate |
| Native memory constructions (owner reports, 2026-10-22: product-ready six-site, relay, two-record, heralding; `../owner-checks/report9/`) | n/a | n/a | n/a | n/a | n/a | n/a | positive calibration: native evolution within a declared memory construction, with added preparation and readout premises (isotropic known coordinates, u-only terminal read). Not a geometry candidate. Bears on the compatible-records interface candidate only |

### 6.2 Route K

| Control | K-W1 | K-W2 | K1 | K2 (or K2′) | K3 | Route K verdict |
|---|---|---|---|---|---|---|
| Complex QM | Pass | Pass | Pass | Pass | Pass | **positive control:** reached (necessity direction of `carrier_general_oiPlus`) |
| `five_way_minimality` witnesses | each fails exactly one of the five [kernel] | | | | | **negative controls:** each must fail its own condition |
| Real QM in the complex framework | Pass | Pass | Pass | **Fails**: so(n) does not contain su(n) [std] | Pass | not reached |
| Real Clifford class | Pass | Pass | Pass [arg] | **Fails**: finitely generated, hence countable and without a continuous drive; no quarter phase on the corpus rule (test-8 N2) [arg]. `polC_countable_upToScalar` covers the audit's PolC, not this class | Pass [arg] | not reached |
| Permutation theory (`permTheory`) | Pass | Pass | Pass | **Fails**: configuration-level (`configurationLevel_not_phaseFree`) | Pass | not reached |
| PolC (polarization closure) | Pass | Pass | Pass | **Fails**: no layer flow (`polarizedTheoryC_not_layerFlowExecutable`) | Pass | not reached; also `polarizedTheoryC_not_qm` |

The Pass marks for well-formedness and K1/K3 on the kernel countermodels follow the kernel definitions as cited. They
are to be checked against the definitions before the table is relied on [open].

## 7. Gates and what remains before freeze

- **Literature, owner-checked on 2026-10-22.** The hypotheses of Krumm–Müller Theorem 1, de la Torre et al. Theorem 2
  and Gross et al. Theorem 1 are recorded in §2.2 and §6.1 as the owner's checked scope.
  - Still to do: a verbatim quotation with section and page locations. The owner's session can supply it; this
    environment's proxy denies `arxiv.org`, `journals.aps.org` and `link.springer.com`.
  - Until those quotations are recorded, verdicts that cite these theorems name the owner check as their source.
- **Rows marked [arg] or [open].** These need a check or a citation before the control table is used:
  - the real Clifford class's L1–L3 and L6;
  - Spekkens L3, L4 and L6;
  - the K-route Pass marks on the countermodels.
- **Candidates, after the control table is reviewed:**
  - the polarization map, as added mathematical structure;
  - a ℤ/4-extended substratum state;
  - a centre (self-coupling) term, which changes the displayed update;
  - a different sourcing map, audited first for consistency across preparations, interventions and composites;
  - the compatible-records memory interface.

  Each is scored on both routes with the §4 marks. The aim is to see whether a candidate supplies a missing
  ingredient, or only moves it into an interface definition.

## 8. Invariant → checkpoint (§A.41)

| Invariant | Checkpoint |
|---|---|
| The positive control reaches both routes | Complex QM row: every premise Pass |
| Each negative control fails at its named premise | Each row's Fails mark names a witness or citation; a row that passes everything voids the table |
| Native is measured against the frozen baseline | Every Native mark cites a baseline source at `fc9018e8` |
| No universal premise is discharged by bounded evidence | The evidence column is checked mechanically: bounded paired with Native/Added on a universal premise is refused |
| Literature premises are quoted before use | §7 gate closed, with the quoted text and source location recorded |
| D3 is exact | `bench_controls_span.py` uses integers and Fractions; replays byte for byte (`SHA256SUMS`) |

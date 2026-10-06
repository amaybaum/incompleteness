# The Incompleteness of Observation

**Author:** Alex Maybaum  
**Field:** Theoretical physics / foundations

This repository develops the **Observational Incompleteness (OI)** framework: a programme for asking what laws are accessible to an observer embedded inside a finite, reversible system with only partial access to its state.

The framework is inspired by the same broad kind of self-reference constraint that appears in Gödel and Turing: an embedded system cannot, in general, obtain complete access to itself. OI studies the physical consequences of that limitation.

> **Scope note.** Throughout the project, “derived” means derived **relative to the named structural and empirical premises**. The framework is best read as a compression of physics onto a small set of commitments, not as a derivation of known physics from the bare fact of observation alone. See the book §4.7 and `SM` §8.3.

## Start here

| If you want | Start with |
| --- | --- |
| The foundational finite-observer result | [`papers/Main.md`](papers/Main.md) |
| A short, self-contained phenomenology paper | [`papers/Juno.md`](papers/Juno.md) |
| The current formal-verification programme | [`verification/README.md`](verification/README.md) |
| The live list of proved, conditional, open and refuted obligations | [`verification/ROADMAP.md`](verification/ROADMAP.md) |
| The full book-length exposition | [`book/README.md`](book/README.md) |
| The physics papers | [`papers/`](papers/) |

## The foundational correspondence

At finite observational horizon, the framework relates three descriptions:

```text
finite stochastic law (S)
        ⇅ exact
finite reversible realization (D)
        ⇅ exact
fixed-basis unitary/Born representation (Q_fb)
```

The representation equivalence is universal at this finite-record level. The specifically OI content is the embedded-observer structure: coupling, hidden capacity, persistence and history readback constrain what a faithful realization must contain.

`Main` develops this finite-horizon correspondence together with the hidden-memory and recurrence results. The strongest coherent instrument/composite lift is a separate question, and Bell-completion and later physics-layer bridges are tracked separately rather than folded into the base theorem.

## What is core, conditional, and conjectural

The repository deliberately separates three levels of claim.

### 1. Core mathematical and physical programme

The physics core is developed in `Main`, `SM`, `GR`, `Substratum`, `Structure`, `Methodology`, and the focused `Juno` paper. Formal and computational certificates live under [`verification/`](verification/).

### 2. Conditional bridges

Several later physics conclusions require explicitly named hypotheses or bridge statements. These are not silently promoted to consequences of OI. Important examples include:

- **H-link** — identifies the exact six-link cubic representation with a physical gauge carrier; the single-copy clause gives the (K=6) reading.
- **H-cust** — the custodial kinetic/condensate premise used by the stabilizer route.
- **H-Bell** — the open requirement that the preparation-dependent graph construction preserve operational no-signaling and the intended metric/continuum structure.
- the remaining instrument/composite, running, chirality, generation and related manuscript-specific hypotheses recorded in the papers and verification roadmap.

### 3. Conjectural extensions

Applications outside the physics core are exploratory and carry **no evidential weight for the core framework**:

- [`papers/Complexity.md`](papers/Complexity.md) and [`papers/Computation.md`](papers/Computation.md) — computation and complexity;
- [`papers/Medicine.md`](papers/Medicine.md) — medicine;
- [`papers/Bioinformatics.md`](papers/Bioinformatics.md) — computational biology;
- the consciousness discussion in the book.

Each extension should be judged on its own test-or-break conditions.

## Core papers

| Work | Role |
| --- | --- |
| [`Main`](papers/Main.md) | Finite embedded observers, hidden memory, the finite-horizon (S \iff D \iff Q_{\mathrm{fb}}) correspondence, and falsification conditions. |
| [`SM`](papers/SM.md) | The (d=3) simple-cubic branch, exact lattice/representation results, and the Standard-Model phenomenology with its named bridge assumptions. |
| [`GR`](papers/GR.md) | The cosmological-horizon route to the gravitational and dark-sector programme, with assumptions and open calculations stated where they enter. |
| [`Substratum`](papers/Substratum.md) | Reconstruction and substratum gauge structure; the proved converse is scoped to the local propagating lattice/gauge residue under its stated hypotheses. Bell-inclusive uniqueness remains separate. |
| [`Structure`](papers/Structure.md) | Observation/gauge hierarchies, universality classes of embedded observers, and comparison with other unification programmes. |
| [`Methodology`](papers/Methodology.md) | Developmental foundations and philosophy-of-physics treatment of the framework and its axiom structure. |
| [`Juno`](papers/Juno.md) | Focused presentation of the parameter-free solar-mixing value and its retrodictive/forward-test status. |

## A focused empirical example: JUNO

`Juno` presents

\[
\sin^2\theta_{12}=\frac13-\frac{1}{4\pi^2}=0.3080.
\]

The value was derived after JUNO's first measurement, so the existing agreement is a **retrodiction**, not a prediction made in advance. The paper treats JUNO's design-lifetime precision as the forward test. Full numerical and classification details belong in [`papers/Juno.md`](papers/Juno.md) and the relevant physics papers rather than being duplicated here.

## Verification

The verification suite is the authoritative place for machine-checked status. It has three main layers:

- [`verification/lean/`](verification/lean/) — dependency-free Lean 4 kernels plus concrete numerical probes;
- [`verification/lean-mathlib/`](verification/lean-mathlib/) — the Mathlib-based `OIBridge` theorem programme;
- [`verification/coverage/`](verification/coverage/) — the manuscript-to-certificate coverage ledger.

CI checks the proof layers, probes, coverage and governed receipts. Exact theorem counts and current obligations change as the programme advances, so this README intentionally does **not** hard-code those counts.

For current status, use:

- [`verification/README.md`](verification/README.md) — verification architecture and flagship formal results;
- [`verification/ROADMAP.md`](verification/ROADMAP.md) — the live obligation queue;
- [`verification/lean/VERIFYING.md`](verification/lean/VERIFYING.md) — how to run the zero-import checks;
- [`verification/lean/ROADMAP.md`](verification/lean/ROADMAP.md) — the narrower zero-import formalization roadmap.

## Repository map

```text
incompleteness/
├── papers/           Research papers and lattice-computation source
├── book/             Book-length exposition
├── verification/     Lean proofs, Mathlib bridge, probes, coverage and receipts
├── tools/            Build, audit and release-gate tooling
└── README.md
```

### Other papers and materials

- [`papers/Explainer.md`](papers/Explainer.md) — older overview, superseded by the book and retained for reference.
- [`papers/Complexity.md`](papers/Complexity.md) — conjectural extension from the framework toward evolution and complexity.
- [`papers/Computation.md`](papers/Computation.md) — conjectural extension toward computation and complexity theory.
- [`papers/Medicine.md`](papers/Medicine.md) — conjectural medical extension.
- [`papers/Bioinformatics.md`](papers/Bioinformatics.md) — conjectural computational-biology extension.
- [`papers/oi_lattice_code/`](papers/oi_lattice_code/) — lattice Monte Carlo and related numerical source.

## What remains open

The project keeps open seams explicit rather than treating them as established consequences. Among the important ones are:

- the strongest common coherent instrument/composite representation;
- the physical-carrier identification beyond the exact cubic representation;
- the remaining chirality/generation and related Standard-Model bridge conditions;
- Bell-compatible completion of the adopted state-dependent graph route;
- parts of the gravity/running chain that remain conditional or reported rather than independently verified;
- the smooth continuum emergence and other manuscript-specific obligations tracked in the live roadmap.

The authoritative status of any current obligation is [`verification/ROADMAP.md`](verification/ROADMAP.md).

## Book

**The Incompleteness of Observation: A Unified Framework from Quantum Mechanics to Computational Biology** develops the framework across 20 chapters with expanded exposition, appendices, glossary and bibliography.

See [`book/README.md`](book/README.md) for the reader's guide and [`book/The-Incompleteness-of-Observation-FULL.pdf`](book/The-Incompleteness-of-Observation-FULL.pdf) for the compiled manuscript.

## Citation and archive

The repository is archived on Zenodo under concept DOI **10.5281/zenodo.19060318**, which resolves to the latest version. For a claim tied to a particular release, cite that release's version DOI.

> Maybaum, A. (2026). *The Observational Incompleteness Framework*. Zenodo. https://doi.org/10.5281/zenodo.19060318

## Licensing

This repository contains both code and authored research material:

| Scope | License |
| --- | --- |
| Source code — including `papers/oi_lattice_code/`, `verification/`, `tools/`, and other program source | **MIT**, per [`LICENSE`](LICENSE) |
| Manuscripts — the papers and book | **CC-BY-4.0** |

`LICENSE` is intentionally the repository's machine-detected MIT license file; the manuscript licence applies by scope to the authored research works.

## Contact

Alex Maybaum — Independent Researcher  
[LinkedIn](https://www.linkedin.com/in/amaybaum)

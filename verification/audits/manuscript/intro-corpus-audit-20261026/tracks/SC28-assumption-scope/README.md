# SC-28: generalizations stated without their assumptions (#942 / #946)

Base: `main` at `0d917665`. Each claim is restated at the strength of its anchor. Where the corpus adopts the
missing assumption elsewhere, the dependency is cited; otherwise the claim is narrowed to what is proved. No new
physical assumption is introduced. The owner's decision for the type II and dS-cancellation claims is binding: they
stay removed as results and may appear only as open research directions.

| Site | Was | Anchor | Now |
|---|---|---|---|
| Main §2.3, Continuous-time extension | "By Poincaré recurrence, ∃ t_R": near-total return of every cell at a common time, giving continuous-time P-indivisibility for a general Hamiltonian flow | Main §2.3, Theorem (history readback + finite recurrence implies indivisibility): Γ_L = I for a bijection of finite order; lemma `isPermMatrix_of_stochastic_inverse`. No continuous-time theorem. | Conditional: common-time near-total return implies P-indivisibility, and that return is the counterpart of Γ_L = I. Poincaré recurrence gives a.e. return at state-dependent times; for a mixing flow T_ii(t) → μ(cell) < 1. General Hamiltonian flows: open. |
| Main §2.3, Role of (C2)–(C4) | "The Poincaré recurrence argument" | Same theorem (finite) | "The finite-recurrence argument" |
| Main §2.3, Weak-coupling and fast-bath regimes | The P-divisible JC and Davies–Merkli examples "illustrate the necessity of (C2)"; "the §3.4 necessity proof for (C2) establishes this formally" | The §2.3 recurrence theorem uses no (C2). (C2-structural) holds by reversibility (Main §1.3). §3.4 Theorem (physical memory: C2, process form) bounds conditional memory for ε ≤ 1 − 1/n_V; its timescale form is conditional on mixing. | The examples have continuum reservoirs and fall outside the finite-recurrence hypothesis. The theorem uses no form of (C2), so the timescale form is not necessary. The §3.4 bound concerns conditional memory, not P-divisibility, holds under mixing, and carries its range condition. |
| Main §4.4, convergence paragraph | "type II structure as a consequence rather than a postulate"; "the cancellation is structurally forced"; dimension "computed directly from the partition geometry", with AAIL's formula "matching"; Slagle–Preskill: "achieves the same emergence with neither"; evidential self-assessment | No construction in the corpus gives a von Neumann algebra of any type, the dS sphere partition function, or d_Ob·e^{2S_0}. The anchors that do exist are: finite-region matrix algebras; the quasilocal C*-completion with no state or representation selected (GR §3.3, `instCStarAlgebraQuasilocal`, `closure_iUnion_stage`); U_φ on H_V ⊗ H_H (Main §3.2); and S ⟺ D ⟺ Q_fb (Main §3.4). | No type II algebra, no von Neumann closure, no relation to CLPW's algebra, and no entropy identification. Whether the construction reproduces CLPW's algebra and entropy is open. The cancellation is not computed, and its reproduction is open. Dimensions are finite partition counts, and the AAIL scaling is not derived. Slagle–Preskill: what is obtained is the fixed-basis equivalence on finite horizons; the continuous-time law is additional structure, and operational QM needs the quantum-complete extension. The self-assessment is removed. |
| GR §6.3, Maldacena paragraph | "arrives at the same cancellation … structurally forced"; entropy "pinned to the substratum's log\|G_sub\|"; "microscopic realization" of the HUZ dimension; "converges … on substantive content" | 𝒢_sub is the substratum gauge group (Substratum §4, Theorem 24). No computation identifies an entropy with log\|𝒢_sub\|, and the group is not given as a finite group. GR §5: each boundary mode carries entropy σ, and σ·N_modes = S_dS under the §3 calibration. GR §3.3 gives the completion. | The observer is present from the outset, but the phase is not computed and its reproduction is open. No type II algebra is derived; the completion is a quasilocal C*-algebra with no state or representation selected, and no von Neumann closure, relation to CLPW or entropy identification is derived, all open. The horizon entropy is σ per mode over the N_modes of §5, which recovers S_dS. Shares the starting point. |
| SM §7.5 bridge gap (ii) | "by P-indivisibility (Main Theorem 4), the stationary distribution is unique, hence ρ∘T = ρ"; "Part A … Level 1 closed"; "gap (ii) is Level 2 closed framework-essentially" | "Main Theorem 4" does not exist. The φ-invariant distributions of a finite bijection are exactly those constant on its cycles. Cycle ergodicity is the residual of gap (i) and is discussed in SM §4.2. For the §4.2 rule, E(a,b) = a·a + b·b − a·Nb is conserved (N symmetric) and even under T:(a,b)↦(b,a) of Theorem 17. This was checked exactly over ℤ and ℤ/qℤ on random states. | The whole gap is conditional on cycle ergodicity. That ρ∘T is φ-invariant holds unconditionally. Uniqueness holds exactly for a single cycle. The level sets of E are φ- and T-invariant, so under cycle ergodicity on the shell carrying ρ, ρ∘T = ρ. Both parts carry gap (i)'s residual. |
| SM §4.2 :294, chaos diagnostic | "Way out (i) is … empirically demonstrated"; "The cycle-ergodicity question … is closed at chat-track numerical scale" | Lyapunov exponent λ_max and four further diagnostics, all numerical | The diagnostics demonstrate chaos numerically. Chaos is necessary for full-shell sampling, not sufficient. No single-cycle theorem exists, and the measurements are limited to the sizes, ensembles and protocols sampled. The paragraph's opening sentence, "deserves explicit acknowledgment", is dropped (§A.32). |
| Structure :1115 | "beyond chat-track scope" | Register | "beyond the scope of this section" |
| SM Bridge Theorem (c) | "the bijection's stationary distribution" | As gap (ii) | "a stationary distribution of the bijection" |
| SM §8.5, positioning | "the unique member of this convergence … the comparison programs do not currently match" | Self-assessment (§A.32) | States the derivation from a finite deterministic substratum, carried to the twenty-two classified observables of §7. |
| Explainer, FAQ on observers | "a comparable empirical record is not currently produced by the alternatives … encouraging context … makes the case" | Self-assessment | States the classified predictions. Neither the dS phase nor a type II algebra is computed, and reproducing either is open. |
| Book ch01 §1.5 (+FULL) | Poincaré recurrence is "the same statement as the discrete recurrence", playing the role of φ^N = id in continuous time | As Main §2.3 | Mirrors the narrowed Main text. |
| Book ch07 §7.7 (+FULL) | "microscopic realization of these results … structurally forced" | As GR §6.3 | Shares the starting point. Finite-region matrix algebras and the C*-completion are stated, with nothing further derived. The CLPW algebra, its entropy and the cancellation are open research questions. |
| Book ch18 §18.7 (+FULL) | The route "applies only to finite (or, more precisely, finite-measure) dynamical systems" | Main §2.3 theorem: needs Γ_n = I | Needs every root's visible law to return, Γ_n = I, almost surely over the hidden prior. A finite bijection supplies this (Γ_N = I); finite-measure Poincaré recurrence does not. |
| Book ch18 §18.7 (+FULL) | "with the cycle including every configuration the substratum can be in" | The period is the lcm of the cycle lengths. The SM §4.2 rule maps (0,0) to (0,0). | No single cycle covers S, since the zero configuration is fixed. The SM §4.2 question concerns sampling within an energy shell. |
| Book ch18 :174 and :193, ch09 :106, ch02 :32 (+FULL) | "Poincaré recurrence" or "(Poincaré)" used for the exact recurrence of a finite bijection | As above | "exact recurrence" or "finite recurrence"; at :174 a clause separates it from Poincaré's finite-measure theorem. |

**Provenance.** The decision to keep the GR §6 heading is recorded on the audit branch (`audit/intro-corpus-20261026`,
commit `9ff27719`, `tracks/FINAL-AUDIT/GR6-heading-decision.md`). It is cited here as provenance only. Nothing on this
branch depends on its content beyond leaving that heading unchanged.

Re-grep over `papers/*.md` and `book/*.md`:

- **Zero hits** remain for each of:
  - "type II structure as a consequence"
  - `G_{\text{sub}}|`
  - "Main Theorem 4"
  - "the stationary distribution is unique"
  - "or, more precisely, finite-measure"
  - "same statement as the discrete recurrence"
  - "microscopic realization of these results"
  - "has measure $> 1 - \delta$ for any"
  - "necessity proof for (C2) establishes"
  - "do not currently match"
  - "unique member of this convergence"
  - "deserve more weight"
  - "unique stationary"
  - "chat-track"
  - "Poincaré recurrence argument"
  - "achieves the same emergence"
  - "does not bear on this"
- **"finite-dimensional Hilbert spaces"** (excluding "infinite-…") has 1 surviving use, Main :708 ("Witten's Type II
  program achieves finite entropy without finite-dimensional Hilbert spaces"), which describes external work.
- **"structurally forced"** has 3 surviving uses: SM :1241 (spatial d = 3), Structure :1059 (cubic class) and Structure :1073 (compositeness scale). All three are other claims.
- **"pinned to"** has 2 surviving uses: ch07 :197 and its FULL copy. Both describe CLPW's own result.
- **Type II algebra** sites other than the corrected ones describe external work only: Main :704 and :708, SM :1456, ch07 :197, ch09 :297 and :301, and their FULL copies.

Regenerated: Main, GR, SM, Structure, Explainer, and the book (`.tex` and `.pdf`).

# SC-28: generalizations stated without their assumptions (#942 / #946)

Base: `main` at `0d917665`. Each claim is restated at the strength of its anchor. Where the corpus adopts the
missing assumption elsewhere, the dependency is cited. Otherwise the claim is narrowed to what is proved. No new
physical assumption is introduced.

| Site | Was | Anchor | Now |
|---|---|---|---|
| Main §2.3, Continuous-time extension | "By Poincaré recurrence, ∃ t_R" with near-total return of every cell at a common time, giving continuous-time P-indivisibility for a general Hamiltonian flow | Main §2.3, Theorem (history readback + finite recurrence implies indivisibility): Γ_L = I for a bijection of finite order. Lemma `isPermMatrix_of_stochastic_inverse`. No continuous-time theorem. | Conditional: common-time near-total return implies P-indivisibility. That return is the counterpart of Γ_L = I. Poincaré recurrence gives a.e. return at state-dependent times, and a mixing flow has T_ii(t) → μ(cell) < 1. General Hamiltonian flows: open. |
| Main §2.3, Role of (C2)–(C4) | "The Poincaré recurrence argument" | Same theorem (finite) | "The finite-recurrence argument" |
| Main §2.3, Weak-coupling and fast-bath regimes | P-divisible JC / Davies–Merkli examples "illustrate the necessity of (C2)"; "the §3.4 necessity proof for (C2) establishes this formally" | §2.3 recurrence theorem (uses no (C2)). §3.4 Theorem (physical memory: C2, process form): bounds conditional memory, and its timescale form is conditional on the mixing hypothesis. | The examples have continuum reservoirs, outside the finite-recurrence hypothesis. (C2) is not necessary for recurrence-cycle P-indivisibility. The §3.4 theorem bounds conditional memory, not P-divisibility, and only under mixing. |
| Main §4.4, convergence paragraph | "type II structure as a consequence rather than a postulate"; "the cancellation is structurally forced"; dimension "computed directly from the partition geometry", with AAIL's formula "matching"; plus evidential self-assessment (strengthens the empirical case; record the others do not match; triangulation, more weight) | None. The corpus constructs no von Neumann algebra of any type, no dS sphere partition function, and no d_Ob·e^{2S_0}. Main §3.1 and §3.2: representations are finite-dimensional, and U_φ acts on H_V ⊗ H_H. | Type II not derived. Cancellation not computed, so its reproduction is open. Dimensions are finite partition counts, and AAIL scaling is not derived. Self-assessment removed. |
| GR §6.3, Maldacena paragraph (heading of §6 kept, per `GR6-heading-decision.md` at `9ff27719`) | "arrives at the same cancellation … structurally forced"; entropy "pinned to the substratum's log\|G_sub\|"; "microscopic realization" of the HUZ dimension; "converges … on substantive content" | None. `G_sub` is defined nowhere in the corpus. GR §5 gives N_modes = S_dS/σ under the §3 calibration. | Observer present from the outset, but the phase is not computed and its reproduction is open. No type II algebra and no entropy identification are derived. Horizon entropy is the §5 mode count. Shares the starting point. |
| SM §7.5 bridge gap (ii) Part A | "by P-indivisibility (Main Theorem 4), the stationary distribution is unique, hence ρ∘T = ρ"; "Level 1 closed" | None for the inference. "Main Theorem 4" does not exist. φ-invariant distributions of a finite bijection are exactly those constant on its cycles. Cycle ergodicity is SM §4.2's gap (i) residual. | Uniqueness holds exactly for a single cycle, and P-indivisibility does not bear on it. ρ∘T = ρ holds under cycle ergodicity on a φ-invariant set carrying ρ and ρ∘T. Part A is "Level 1 given the cycle ergodicity of gap (i)". |
| SM Bridge Theorem (c) | "the bijection's stationary distribution" | As above | "a stationary distribution of the bijection" |
| SM §8.5 positioning | "the unique member of this convergence … empirical record … the comparison programs do not currently match" | Self-assessment (§A.32) | States the derivation from a finite deterministic substratum, carried to the twenty-two classified observables of §7. |
| Explainer FAQ (observers) | "a comparable empirical record is not currently produced by the alternatives … encouraging context … makes the case" | Self-assessment | States the classified predictions. Neither the dS phase nor a type II algebra is computed, and both are open. |
| Book ch01 §1.5 (+FULL) | Poincaré recurrence "the same statement as the discrete recurrence", playing the role of φ^N = id in continuous time | As Main §2.3 | Mirrors the narrowed Main text. |
| Book ch07 §7.7 (+FULL) | "microscopic realization of these results … structurally forced" | As GR §6.3 | Shares the starting point. Neither the phase nor a type II algebra is computed, and the cancellation is open. |
| Book ch18 §18.7 (+FULL) | route "applies only to finite (or, more precisely, finite-measure) dynamical systems" | As Main §2.3 | Needs common-time exact return. A finite bijection supplies it, and finite-measure Poincaré recurrence does not. |
| Book ch18 §18.7 (+FULL) | "with the cycle including every configuration the substratum can be in" | None. The period is the lcm of the cycle lengths. | Single cycle through every configuration not established. SM §4.2's question concerns energy-shell sampling. |

Re-grep over `papers/*.md`, `book/*.md`:

- **Zero hits remain** for each of: "type II structure as a consequence", `G_{\text{sub}}|`, "Main Theorem 4", "the stationary
  distribution is unique", "or, more precisely, finite-measure", "same statement as the discrete recurrence", "microscopic
  realization of these results", "has measure $> 1 - \delta$ for any", "necessity proof for (C2) establishes", "do not
  currently match", "unique member of this convergence", "deserve more weight" and "unique stationary".
- **"structurally forced"** has 2 surviving uses, Structure :1059 and :1073 (cubic-class and compositeness scale). Both are
  other claims.
- **"pinned to"** has 2 surviving uses, ch07 :197 and FULL. Both describe CLPW's own result.
- **"Poincaré recurrence argument"** has 2 surviving uses, ch02 :32 and FULL. Both concern the finite substratum.
- **Type II algebra** sites outside the corrected ones describe external work only: Main :704 and :708, SM :1456, ch07
  :197, ch09 :297 and :301, and FULL.

Regenerated: Main, GR, SM, Explainer, and the book (`.tex` and `.pdf`).

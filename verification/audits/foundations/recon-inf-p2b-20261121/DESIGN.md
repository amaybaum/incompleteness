# RECON-INF P2-B: Stage 3 of Theorem 23 without finite counting (research design)

**Status.** Writer's research design, WIP / UNVERIFIED. It plans an investigation and executes
none of it: no proof is attempted, no computation is run, and no manuscript, Lean, registry, ledger
or #1477 file is changed. Independent review of this design is required before any node is
authorized.

**Authorization.** Owner `amaybaum`, [#1169 comment 7068325638](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7068325638),
2026-11-21T19:51:15Z: "RECON-INF Phase 2 | Research planning authorized | Plan Stage 1, Stage 3 and
the cross-stage bridge separately; no proof execution yet". The P2-B item reads: "**P2-B (Stage 3).**
Can normalized measures on infinite configuration spaces carry the entropy and boundary
calculations? Invariant product measures for special coupled rules stay distinct from a measure
justified for the selected native dynamics." Order item 5: "Phase 2 investigations, only after
their plans are reviewed". Phase 3 is not authorized.

**Goal link.** Issue #1531 (RECON-INF) and thread #1169. Phase 1 (draft PR #1532, head
`0bc9628ab3ee4e6955df8980815ecead869578ee`, `verification/audits/foundations/recon-inf-p1-20261121/AUDIT.md`,
confirmed in #1532 c.7068298957 after c.7068213461 and c.7068281368) records Stage 3's H-count as one
of the two finiteness uses with no infinite-system replacement on `main` (AUDIT rows 38–43, §2, §6
item 3). This design plans the test of whether a normalized law on an infinite carrier can take the
place of that count.

**Source pin.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed` (Phase 1's baseline B1).
`GR:n`, `Sub:n`, `SM:n`, `Main:n` are lines of `papers/GR.md`, `Substratum.md`, `SM.md`, `Main.md` at
the pin. Records are under `verification/audits/foundations/`:

| Short name | Path | Standing as its record states it |
|---|---|---|
| P1 | `recon-inf-p1-20261121/AUDIT.md` at `0bc9628a` (#1532, not on `main`) | Confirmed (c.7068298957) |
| P7-B | `p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| R1-INF | `r1-inf-20261119/RESULT.md` | Revised after REVISE; delta review outstanding. Every use below carries "(delta review outstanding)" |
| O-A4 | `o-a4-20261120/RESULT.md` | Merged in #1441; owner-accepted |
| NR-1 | `nr1-near-return-20261116/NR-1.md` | ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| A1-03 | `a1-free-p7-coupled/DECISION.md` | SOURCE GAP at normalized invariant coupled-shell states |
| A1-07 | `a1-07-p7-energy-state/DECISION.md` | SOURCE GAP at the energy check (RD6 cut) |
| LEDGER | `a1exit-ledger-20261120/LEDGER.md` | Rows X-70 (F), X-71 (O), X-72 (F) |

## 1. The question

**Setting.** The native carrier is `Ω = (A×A)^{ℤ³}` with `A = ℤ_q`. The **selected native dynamics**
`F_sel` is the second-order form of Main:736 item (xiii) with the centre-free isotropic linear rule
of SM:224, `x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1) (mod q)`, in phase-space form
`(u, v) ↦ (αSu − v, u)` (R1-INF §2), with reversal `Θ` the slice swap. `main` fixes neither `q` nor `α`
(NR-1:101, row (Q)), so every statement below is indexed by `(q, α)`. The rounded rule of SM:292 is a
second candidate native rule; it is named where a node covers it and is otherwise outside the grid.

**Question Q.** Is there a normalized Borel probability law `μ` on an infinite configuration space
such that

1. `μ` is invariant under the update and under `Θ`;
2. each Stage 3 calculation of §2.1 is defined for `μ`, with finite cardinalities replaced by
   `μ`-masses or by entropies of finite marginals; and
3. the values those calculations return, in particular the visible weights and the slope `β_E`
   entering `a_* = τ_K/β_E` (GR:78–80), are fixed by `μ` and the dynamics, with no continuous
   parameter set from the target?

And, kept separate from Q: **for which dynamics** does such a `μ` exist, and **by what** is it
selected?

**Tiers (owner's distinction).** Every positive finding carries exactly one tier, and no finding moves
to a higher tier without a node check of its own.

| Tier | Meaning |
|---|---|
| T-spec | Exists for some coupled rule in a stated class that is not `F_sel` on `Ω` |
| T-nat-ex | Exists for `F_sel` on `Ω`, for stated `(q, α)`; nothing about selection |
| T-nat-pos | Selected for `F_sel` only under named posits added to the corpus (for example R1-INF (G3)+(G4), delta review outstanding) |
| T-nat-dyn | Selected by `F_sel`, `Θ` and the observer partition among a class of laws defined without posits beyond the corpus, with no free continuous parameter |

**Outcome set, fixed in advance.** (Y-dyn) Q holds at T-nat-dyn; (Y-pos) Q holds only at T-nat-pos;
(Y-spec) Q holds only at T-spec; (N-scoped) Q fails for a stated construction class, with a
countermodel or proof scoped to that class; (U) undetermined, parked at a named node. The design does
not favour any of these.

## 2. What Stage 3 needs from a measure

### 2.1 The required calculations

Stage 3 (Sub:175–185) derives `ħ = c³ε²/(4Gσ)` from the gap equation of GR §2.3 and §3.2, under
H-slope, H-count and GR §8.5(b) (GR:627). The entropy calculations (S) and boundary calculations (B)
it uses:

| Id | Calculation | Source | What it needs from a measure | Finite form |
|---|---|---|---|---|
| S1 | Restriction to a conserved energy shell, `E_tot = e_i + E_H` | GR:58 (first sentence); GR:88 | A real-valued additive conserved quantity; no measure for the definition | Assumed (GR:88 lists the conserved shell among the calibration's requirements) |
| S2 | Visible weights `P(i) = Ω_H(E−e_i)/Σ_j Ω_H(E−e_j)` | GR:58 | A normalized law on the shell, invariant under `φ` and `Θ`, fixing the weights (P7-B roles (a1)–(a2), P7-B:63) | Uniform counting on a finite shell |
| S3 | Hidden entropy and slope `s_H = ln Ω_H`, `β_E = s_H'(E) = 8πGσ/(c²κε²)` | GR:58; GR:78 | Only energy-resolved ratios of hidden masses (to be confirmed at N1); the area-law profile is H-count's second clause (P7-B H6) | Posit H6 |
| S4 | Finite-reservoir correction `δ_bath ∼ 1/(4s_H)` | GR:58 | An absolute hidden entropy | Finite `s_H ∼ 10^{122}` |
| S5 | Pair counts `N_ij = N_ji`, `N_i P_ij = N_j P_ji` | GR:68–70 | Masses `J_ij` of one law invariant under `φ` and `Θ`, time-even cells (P7-B 6.1, P7-B:177) | Counting |
| S6 | Deep clause: no energy-dependent multiplicity, no energy | GR:58 | A law form (P7-B H4); the cardinality form has no content on an infinite carrier (P7-B:169) | Cardinality equation (a3) |
| S7 | Matching and gap equation `β_E a_* = τ_K` | GR:74; GR:78–80; GR:144–150; Sub:181–183 | Nothing beyond `β_E`; detector side H-slope | Algebra |
| B1 | Mode count `N_modes = A/ε²`; crossing-link count, `κ_m = 3/2` on the spherical horizon | GR:98; GR:104; GR:156 | None (geometry under the single-link reading of H-link) | Exact link count (GR:104) |
| B2 | Entropy per mode `σ ≤ ln q` | Sub:191; GR:98; GR:102; GR:156 | The entropy of one mode's marginal under the law | Counting bound |
| B3 | Absolute boundary entropy `S = σA/ε² = ηA` | GR:98–104; GR:623 (U2) | An absolute entropy of the boundary layer | Count of boundary configurations |
| B4 | Finite boundary configuration set | P7-B H2 (posited); GR:132 (D4) | Finiteness of `C_B` only | Posit |
| B5 | Boundary-only dependence; deep-cardinality gauge | GR:112–138; GR:871–905, (D5) at GR:883 | A product prior `u_{B_n} ⊗ ν` (Appendix B) or a measure form of H-BD (open, REMAINDER L10). GR:144 states that the matching does not use it | Uniform prior on finite `C_H` |

### 2.2 Candidate measures

| Id | Candidate | Carrier and rules covered |
|---|---|---|
| M0 | Counting on finite restrictions: finite shells, tori `Per_L`, finite invariant truncations | Finite restrictions of any rule; cylinder limit on `Ω` is `β_A` for injective CA (R1-INF Lemma 1 (b), :83, delta review outstanding) |
| M1 | Uniform Bernoulli product law `β_A` (Haar for linear rules) | Invariant for every second-order rule over a finite abelian group (O-A4 Lemma U, :69) |
| M2 | Non-uniform product laws, including product Gibbs laws `∝ ∏_z e^{−βφ(x_z)}` | Invariance depends on the rule; fails for `F_sel` with `q = 2, α = 1` under `Bern(1/4)` (R1-INF C7 (i), delta review outstanding) |
| M3 | P7-B's H4 product: counting on a finite boundary shell times a normalized deep law `ν` | Decoupled dynamics (P7-B 6.3, proved); some coupled bijections with a `φ`-adapted `ν` (P7-B 6.3 (i)) |
| M4 | Translation-invariant Gibbs/DLR laws of an interaction with summable variations | Invariant under a surjective CA iff the CA conserves the interaction (Kari–Taati 2015, Thm. 41, as cited in R1-INF Prop. 6 (c), delta review outstanding; to be verified at L1) |
| M5 | Laws maximizing entropy density at fixed densities of conserved quantities | Exist when conserved quantities exist (Kari–Taati Thm. 42, same citation) |
| M6 | P-ED: maximal entropy density among `F`- and translation-invariant laws | Selects `β_A` for every surjective CA under (G1)–(G4) (R1-INF Prop. 3, :114, delta review outstanding) |
| M7 | Laws that are not translation invariant: Haar on a closed invariant subgroup, periodic-orbit measures, laws inhomogeneous across the cut | `m_H` of R1-INF Prop. 9 (b), :280, delta review outstanding; NU9 periodic orbits (P1 §3 (R-b), status C) |

### 2.3 Relations, labelled

Status: **E** Established (source named), **A** Assumed (posited or named hypothesis), **M** Missing.
**(N)**: stated with corpus inputs and standard mathematics only. **(I)**: imports a named assumption.

| # | Relation | Status | (N)/(I) | Source |
|---|---|---|---|---|
| R1 | A finite boundary count does not fix a profile; a finite set admits every energy-resolved profile | E | (N) | P7-B 3.1, :87 |
| R2 | The slope `β_E` is H-count's density-of-states clause, not a consequence of any count | E (as a statement about the derivation); the clause itself A | (I): Jacobson first law (GR:98, [1]), horizon area–energy relation (P7-B H7) | P7-B node 3; P1 §2.1 |
| R3 | A generic normalized invariant law leaves the visible weights and slope undetermined (every real slope occurs) | E | (N) | P7-B node 5, :154–173 |
| R4 | No probability on a countably infinite set is invariant under all its permutations | E | (N) | P7-B Lemma 5.1, :171 |
| R5 | Pair counts are replaced by masses of one `φ`,`Θ`-invariant law: `J_ij = J_ji` for time-even cells | E | (N) | P7-B 6.1, :177; Lean `MeasuredReciprocity.reciprocal_flux`:90 |
| R6 | H4 product law gives `p_i = Ω_B(E−e_i)/Z` with a deep sector of any cardinality, decoupled dynamics | E (record) | (N) given H2, H4 (A) | P7-B 6.2–6.3, Theorem :207 |
| R7 | Some deep-coupled bijections have no normalized invariant shell law; others have an invariant product law | E | (N) | P7-B 6.3, :185–189 |
| R8 | Existence of a normalized invariant shell law for coupled bijections in general | M | — | LEDGER X-71 (O); A1-03 |
| R9 | A normalized `F`-,`Θ`-invariant law exists on the native carrier (`β_A`) | E | (N) | O-A4 Lemma U |
| R10 | `β_A` selected among `F`- and translation-invariant laws by entropy density | E under (G3)+(G4) (A) | (N) for the mathematics; (G3), (G4) are added posits | R1-INF Prop. 3, delta review outstanding |
| R11 | Selection of a law by `F_sel` alone on `ℤ^d`, `d ≥ 2`, `q` prime, `α ≠ 0` | M (uniqueness fails without (G3)) | — | R1-INF Prop. 9 (b), delta review outstanding |
| R12 | A real-valued conserved energy for `F_sel`: the exact rule conserves its quadratic only modulo `q` | E (negative for the quadratic); a real conserved energy M | — | SM:292; A1-07 |
| R13 | Real finite-range additive conserved quantities of `F_sel` in `d ≥ 2` | M (not determined) | — | R1-INF Prop. 6 consequence, :238–244, delta review outstanding |
| R14 | In `d = 1`, `α² ≡ 1 (mod q)`: mover densities are conserved; a `2(q−1)`-parameter invariant generalized Gibbs family exists | E (record) | (N) | R1-INF Prop. 6 (b), delta review outstanding |
| R15 | Under `β_A` with window readout the rooted maps are doubly stochastic | E (record) | (N) | R1-INF Lemma 8, :268, delta review outstanding |
| R16 | P-ED gives no shell and no temperature for GR:58's coupled case | E (record) | (N) | R1-INF :385, delta review outstanding |
| R17 | Mode count and orientation factor `κ_m = 3/2` | E under the single-link reading of H-link (A) | (N) | GR:104 |
| R18 | `σ ≤ ln q` for the entropy of any law's mode marginal | E (Shannon bound) | (N) | Sub:191; GR:98 |
| R19 | `S3`: Lemma 1's `ε` equals the boundary counting unit | A; not derivable from Lemma 1 | (N) as a posit | P7-B node 4; GR:669 |
| R20 | H-slope, H-frame, H-Hawking, KMS/H-spectrum on the detector side | A | (I): emergent QFT state class, KMS | GR:74; GR:86; GR:144 |
| R21 | Deep-sector corollary for a deep sector of any cardinality under (D1)–(D5) | E (paper) | (N) with the product prior (D5) as a model hypothesis | GR:871–905 |
| R22 | Identification of a conserved substratum quantity with the horizon first-law energy | M | (I) when supplied: first law (H7) | A1-07; GR:88 |

## 3. Literature step (plan only; precedes every closure node, AGENTS Step 4)

Each item states what it must settle. A bibliographic detail written here is to be confirmed against
the source at this step; nothing below is used as established until then.

| # | Topic | Items to locate and read | What it must settle |
|---|---|---|---|
| L1 | Conservation laws and invariant Gibbs measures of CA | Kari and Taati, J. Stat. Phys. 160 (2015) 1198–1243 (Thms. 12, 41, 42); Formenti, Kari and Taati, on the hierarchy of conservation laws in a CA | The exact hypotheses (surjectivity, strongly irreducible SFT, summable variations) and whether "F-invariant translation-invariant Gibbs measure for `f`" is equivalent to "F conserves `f`" in both directions |
| L2 | Deciding additive conserved quantities | Hattori and Takesue, Physica D 49 (1991) 295–322; Pivato, Nonlinearity 15 (2002) 1781–1793; Durand, Formenti and Róka, Theor. Comput. Sci. 304 (2003) | A finite exact criterion for conservation of a range-`r` potential on `ℤ^d`, `d ≥ 2`; equivalence of conservation on finite, periodic and arbitrary configurations; the precise sense in which torus equations are necessary conditions (R1-INF :540–541, delta review outstanding) |
| L3 | Second-order and reversible CA invariants | Pomeau, J. Phys. A 17 (1984) L415; Takesue, Phys. Rev. Lett. 59 (1987) 2499 and J. Stat. Phys. 56 (1989) 371; Toffoli and Margolus, Physica D 45 (1990) | Known conserved quantities of second-order rules; thermalization and ergodicity of reversible CA with additive conserved quantities |
| L4 | Entropy density and the variational principle for `ℤ^d` actions | Ruelle, *Thermodynamic Formalism*; Georgii, *Gibbs Measures and Phase Transitions* (1988), Ch. 15; Misiurewicz (1976) on pressure for `ℤ^d` actions; Walters (1982), Ch. 9 | The relation `s'(e) = β` between entropy density and energy density; which entropy functional is extensive and which is boundary-scaling |
| L5 | Equivalence of ensembles | Georgii, J. Stat. Phys. 80 (1995); Lewis, Pfister and Sullivan (1994–1995) | Whether torus microcanonical counting laws at fixed conserved density converge to a Gibbs law, and under which hypotheses on the conserved quantity |
| L6 | Invariant measures and rigidity of algebraic and permutive CA | Hedlund (1969); Host, Maass and Martínez, Discrete Contin. Dyn. Syst. 9 (2003); Pivato, Discrete Contin. Dyn. Syst. 12 (2005); Einsiedler (2004); Pivato's survey on the ergodic theory of CA | Conditions under which Haar is the only invariant law (for T-nat-dyn versus T-nat-pos at N7); whether those conditions are posits of the (G3) kind |
| L7 | Area laws for classical Gibbs states | Wolf, Verstraete, Hastings and Cirac, Phys. Rev. Lett. 100 (2008) 070502; Eisert, Cramer and Plenio, Rev. Mod. Phys. 82 (2010) 277 | The mutual-information area law for finite-range classical Gibbs/Markov fields, and its exact hypotheses |
| L8 | Stationary laws with a temperature step | Reversible CA and deterministic lattice dynamics literature located from L3 | Whether laws invariant under a coupled reversible energy-conserving dynamics and its reversal can carry different conserved-density statistics on two sides of a cut |
| L9 | Corpus search (§A.19) | `papers/`, `book/` (chapters and FULL), `verification/` for: energy shell, conserved quantity, Gibbs, invariant measure, entropy density, area law, Kari, Takesue, Pomeau, mover | Any treatment already present, so that no node re-derives a recorded result |

Decision rule for L: an item enters a node only with the statement quoted and its hypotheses checked
against the node's setting. An item whose hypotheses the setting does not meet is recorded as not
applicable, with the failing hypothesis named.

## 4. Branch nodes (depth-first, §A.31)

Each node has a decisive check, a decision rule fixed here, and for a computational node an
exactness or symmetry control (§A.21) and a countercontrol. Verdict text is generated from the
recorded outcome by the rule; a verdict over a failed or vacuous control is void (§A.29). Exact
identities, ranks and zeros are decided by exact arithmetic (integers, rationals, finite fields,
cyclotomic integers); floating point is not used as evidence for any of them.

**Order and branching.** N0 → N1 → N2. N2's outcome selects the next branch: a native conserved
quantity sends N3 and N4 to `F_sel`; none sends N3 and N4 to the T-spec models only, and the native
verdict is generated at N7. N5 and N6 run in either case. N8 closes.

### N0. Literature and corpus step

Run L1–L9. **Decision rule.** If L2 yields a finite exact criterion valid on `ℤ^d`, N2 uses it as
method B; otherwise method B is restricted to torus equations, which bound the conserved space from
above only, and N2's positive results need a lower-bound construction. If L1's equivalence holds in
one direction only, N3's existence step cites that direction alone (§A.34).

### N1. What the calculations need: ratios or absolute entropies

**Question.** Which uses of `s_H` and of the counts in GR:58–88, GR:98–104, GR:144–156 and Sub:177–191
enter only through energy-resolved ratios (`Ω_H(E−e_i)/Ω_H(E−e_j)`, `β_E`), and which need an absolute
entropy or a cardinality?

**Check.** A line-by-line reading at the pin, each use classified as ratio, absolute or cardinality.
Documentary; no computation.

**Decision rule.** A use is "ratio" if every formula it feeds is invariant under multiplying all
`Ω_H(x)` by one constant; otherwise "absolute". Ratio uses need only the law's energy-resolved masses;
absolute uses (S4, B3 at least, as listed in §2.1) need a finite entropy, which N5 treats. The node's
output is the list, with the count of each class.

**Control.** The classification is checked against P7-B 6.2, which recovers S2 with the deep sector of
any cardinality; S2 must classify as ratio. A use classified as ratio that P7-B 6.2 does not recover
is re-examined before the list is accepted.

### N2. A conserved energy for the selected native dynamics

**Question.** For `F_sel` on `ℤ^d` with `d = 3` (`d = 1, 2` as controls), does a nontrivial real-valued
additive conserved quantity of finite range exist, for each `(q, α)` in the grid? "Nontrivial" means
not a constant plus a translation coboundary. Additivity is required by GR:58's split
`E_tot = e_i + E_H`. This is prior to every shell calculation: without such a quantity S1 has no
content for `F_sel`, and by L1 no translation-invariant Gibbs law of a nonzero finite-range
interaction is `F_sel`-invariant.

**Method A (character orbits; linear rules).** A real range-`W` potential is a combination of
characters of `A^W` and their conjugates. For a linear rule, composition with `F` maps characters to
characters through the dual map `F^*`, which commutes with translations. The planned reduction is
that a nontrivial conserved range-`W` quantity exists iff some nonzero finitely supported dual
configuration has a finite `F^*`-orbit modulo translations, every member of which has a translate
supported in `W`. **N2.0** proves this reduction in writing before any use; until then method A is
not evidence.

**Method B (direct linear algebra).** The conservation condition on range-`W` potentials, as a
linear system over `ℚ` (by L2's criterion where available, otherwise torus equations), solved by exact
fraction-free elimination.

**Grid (preregistered).** `d ∈ {1, 2, 3}`; `q ∈ {2, 3, 5}`; every `α ∈ ℤ_q`, with `α = 0` as a
countercontrol (`F^4 = id`); `W` the cubes of side 1 and 2, and side 3 for `d ≤ 2`. A cell whose
dual space exceeds `2^{24}` elements runs in CI only (§A.40), which needs owner approval; it is not
run locally. The rounded rule of SM:292 is outside method A; method B covers it in `d = 1, 2` cells
that fit the bound.

**N2.3 (written, all ranges; later authorization).** For prime `q`: is there a nonzero finitely
supported `ξ`, `n ≥ 1`, a translation `g` and `c ∈ ℤ_q^×` with `F^{*n} ξ = c·τ_g ξ`? This is a
statement about eigenvalues of the companion matrix `[[αS, −1], [1, 0]]` over the Laurent ring
`ℤ_q[x_1^{±1}, …, x_d^{±1}]`, `S = Σ_j (x_j + x_j^{−1})`. A comparison of Newton polytopes is one
candidate method; it is not carried out here, and the node is open in both directions.

**Decision rule.**
- Methods A and B disagree on any cell where both run → halt; the node's verdict is void.
- A cell with excess dimension 0 by an upper-bound method (B on tori, or A after N2.0) → "no
  nontrivial real additive conserved quantity of range `W` for `F_sel` at `(d, q, α)`". The statement
  is scoped to that `W` and those parameters.
- A cell with excess dimension `k > 0` → record a basis; a lower bound needs an explicit conserved
  quantity checked exactly on `ℤ^d` (by the L2 criterion or a written proof). Only then is the
  quantity a native candidate for S1.
- N2.3 proved → the scoped statement extends to all finite ranges for that `(d, q)` and every
  `α ≠ 0`. N2.3 refuted by an explicit `ξ` → native candidate. Neither within the authorized budget →
  parked at N2.3, named gap.
- A native candidate, if any, is a mathematical conserved quantity only. Its identification with the
  horizon first-law energy remains R22 (M), and no node here supplies it.

**Controls.**
- *Positive control:* `d = 1`, `α² ≡ 1 (mod q)`: both methods must find the movers of R1-INF Prop. 6,
  and the excess dimensions must equal R1-INF §9 E's reported values (2, 4, 2 for `(q, α) = (2,1),
  (3,1), (3,2)` at range 2). R1-INF is under delta review, so agreement of the two methods with each
  other is the control; agreement with R1-INF is a cross-check.
- *Exactness control:* the identity CA and the shift CA (every potential conserved): the computed
  dimension must equal the full dimension minus the trivial part, by a count computed independently.
- *Symmetry control:* the conserved space must be invariant under `Θ` and the cubic point group acting
  on supports; its dimension must equal a sum of orbit sizes of that action.
- *Countercontrols:* (i) an injected non-conserved potential (a single-site value of `u`) must be
  rejected and an injected mover (`d = 1`) accepted by the checker; (ii) `α = 0` must report the
  conserved quantities of a finite-order map, which differ from the `α ≠ 0` cells.
- *Replay:* each run is deterministic and its output must replay byte for byte (§A.26 item 3).

### N3. Gibbs laws of a conserved quantity: does anything fix the slope?

Runs on N2's native candidates if any; otherwise on T-spec models only: (a) `F_sel` in `d = 1` with
`α² ≡ 1` (a different dynamics from `F_sel` on `ℤ³`, hence T-spec), (b) P7-B's decoupled models,
(c) a rule built with a site-additive conserved energy, chosen before the check and recorded.

**N3.1 Existence.** For a conserved interaction `Φ`, the translation-invariant Gibbs laws `μ_β` that
are `F`-invariant (L1), and their `Θ`-invariance (which needs `Φ∘Θ` equivalent to `Φ`).
**Decision rule:** existence is recorded per `β` only with L1's hypotheses verified for `Φ`; otherwise
"not established for `Φ`".

**N3.2 Visible weights.** Under the DLR conditional, compare the visible cell masses `p_i` with
`e^{−βe_i}` normalized. **Decision rule:** equality holds exactly, or the deviation is a stated
function of the visible–boundary interaction (the H-shell condition of GR:60). Computed in the models
with partition functions as integer polynomials in `x = e^{−β}`.

**N3.3 Selection of `β`.** Candidates: P-ED (gives `β = 0`), maximal entropy at fixed conserved
density (M5), torus microcanonical limits at fixed density (M0 with L5), ergodic decomposition.
**Decision rule:** if every candidate leaves `β`, or the conserved density, as a free continuous
parameter, the verdict is "the Gibbs route supplies S2's form without counting; the slope is carried
by the choice of `β`, a parameter of the law"; if one candidate fixes `β` from the dynamics and the
partition with no target input, the verdict is provisional favourable and goes to N8.

**N3.4 Bulk `β` and horizon `β_E`.** Is the Gibbs parameter of a bulk conserved density related to
H6's `β_E = 8πGσ/(c²κε²)` by anything other than a posit? **Decision rule:** "Assumed (I)" unless a
derivation is supplied; a derivation is accepted only if it does not use the target value.

**Controls (computational parts of N3.2–N3.3).** Exactness: in a decoupled product model with a known
answer, torus counting at fixed energy must reproduce the product formula exactly at every size.
Countercontrol: P7-B node 5's model, in which invariant laws realize every slope, must be reported as
non-unique by the same procedure. A finite torus comparison is an illustration of L5's limit, not a
certificate of it.

### N4. The deep clause and the reservoir

**Question.** S6 requires the deep sector to contribute no energy-dependent multiplicity and no
energy. Under coupled dynamics (GR:128: `L ≠ 0` at every cut of the displayed update):

- **N4.1** Is there a translation-invariant law, invariant under `F` and `Θ`, for which S6 holds in
  law form and the visible weights are energy-resolved?
- **N4.2** If not, is there a law that is not translation invariant (deep sector at constant
  conserved density, boundary layer resolved) and is invariant under a coupled `F` and `Θ` (L8)?
- **N4.3** Under a coupled invariant Gibbs law, which sector sets the visible slope: the boundary
  count, or the bulk parameter `β`?

**Check.** Written argument for N4.1 and N4.3; for N4.2, the literature step L8 followed by an exact
search in small coupled models (finite shells, exact rational masses), chosen and recorded before
the search.

**Decision rule.** N4.1 answered "no" by a proof → "for translation-invariant laws S6 and energy
resolution are incompatible", scoped to translation-invariant laws and the stated conserved
quantities. N4.1 "yes" → record the law and send it to N8. N4.2: an explicit invariant law → T-spec
(or T-nat-ex if for `F_sel`); none found in the models → no statement beyond those models. N4.3 →
record which quantity the visible weights depend on, from N3.2's formula.

**Controls.** Positive: P7-B's decoupled H4 model, where S6 holds by construction, must be reported
compatible. Countercontrol: P7-B 6.3 (ii), where no normalized invariant shell law exists, must be
reported as having none.

### N5. Boundary calculations under a normalized law

- **N5.1 (B2).** The per-mode entropy is the Shannon entropy of the mode marginal; `σ ≤ ln q` with
  equality iff that marginal is uniform. **Check:** confirm against Sub:191 and GR:98–102 that `σ`
  is used as an entropy of a law and not only as a capacity.
- **N5.2 (B3).** The absolute boundary entropy as `H(μ|_{C_B})`: equals the capacity
  `N_modes ln q` under `β_A`, and is below it under a non-uniform marginal. **Check:** which reading
  GR:98–104 and GR:623 (U2) use. **Decision rule:** if they use the capacity, B3 needs only B4 and no
  law; if they use an entropy of the hidden state, B3 needs the selected law, and N7's verdict
  governs it.
- **N5.3 (area scaling).** Which entropy functional scales with area: the boundary-layer marginal
  entropy, the mutual information between a region and its complement (L7), or neither; and the
  extensive entropy density of a region's marginal (L4) as the contrast. **Decision rule:** a
  functional qualifies as an infinite-carrier reading of `s_H` only if its energy dependence can be
  defined and it scales with area for the laws of N3; otherwise it is recorded as not qualifying.
- **N5.4 (B4, H2/H4 necessity).** In P7-B's decoupled scope, replace `#_{C_B}` by any normalized
  boundary law `ρ_B` invariant under the boundary permutation, with `C_B` allowed infinite (compact),
  and H6 by the law form H6′: `ρ_B(E_B = x) ∝ e^{σA(x)/ε_c²}`. **Check:** a written proof attempt of
  P7-B Theorem items 1–4 under H6′. **Decision rule:** a proof → finite counting on the boundary shell
  is not necessary for P7-B's replacement, and the posit moves from H2+H6 to H6′; a failure → the
  step at which it fails is named. Either outcome is about P7-B's decoupled theorem only.
- **N5.5 (B1, B5).** Measure-independent (B1) or not used by the matching (B5, GR:144). Recorded,
  not investigated.

**Control for N5.2 and N5.3.** Entropies are compared through exact counts and rational masses; a
logarithm appears only symbolically. Countercontrol: under the non-invariant product law
`Unif(V) ⊗ δ_0` (R1-INF §9 C), any equality claimed for invariant laws must fail.

### N6. Special coupled rules (T-spec classification)

**Question.** For which coupled rules does an invariant product law exist, and does it resolve
energy?

- `β_A` for every second-order rule (O-A4 Lemma U): T-nat-ex for `F_sel`; uniform weights.
- P7-B 6.3 (i): a coupled bijection with a `φ`-adapted `ν`: T-spec.
- Product Gibbs laws `∝ ∏_z e^{−βφ(x_z)}`: by L1, invariant iff the rule conserves the single-site
  potential `φ`, which is N2's cell `W` = one site. For `F_sel` this node reads N2's result and adds
  nothing to it.

**Decision rule.** Each law is listed with its rule class, its tier, and whether it resolves energy.
A law that is invariant for some coupled rule and not shown invariant for `F_sel` stays T-spec in
every later sentence.

### N7. Justification for the selected native dynamics

**Question.** Among laws found invariant for `F_sel` (T-nat-ex), which, if any, are selected at
T-nat-dyn, and which only at T-nat-pos?

**Check.** R1-INF Props. 3 and 9 (delta review outstanding) and L6's rigidity results, each with
its hypotheses listed and classified as a corpus input or an added posit.

**Decision rule.** T-nat-dyn requires uniqueness among all `F_sel`-,`Θ`-invariant laws of a class
defined without translation invariance or entropy conditions beyond the corpus, with no free
continuous parameter. A uniqueness that needs translation invariance, ergodicity under shifts or a
positive-entropy condition not in the corpus is T-nat-pos, with the condition named. If the selected
law is `β_A`, the verdict on Stage 3 is generated from R15–R16 and P7-B 6.1: uniform visible
marginal on windows, unit paired rate ratio, `β_E = 0` for any additive energy. That verdict is
recorded for `β_A` only.

**Positive control.** The `β_A` verdict must reproduce R1-INF:385. **Countercontrol.** The identity CA
and a lattice translation, for which every translation-invariant law is invariant, must come out with
no selection at T-nat-dyn.

### N8. Pressure on favourable branches; fixed point

Every branch whose outcome favours a replacement of counting (N3.3 fixing `β`, N4.1 "yes", N5.4
proof, N7 at T-nat-dyn) is re-examined for: a hidden use of a finite set or of the target value; a
tier promotion; a sufficiency result stated as necessity; a conditional stated unconditionally (Code
Review Rules). Passes continue until three consecutive passes give no NEW finding (§A.31).

## 5. Productivity test (fixed before N0)

The investigation is a gem iff it gives a statement strictly stronger than "Stage 3 needs a selected
law, the slope is H6, and the coupled case is open" (P7-B; R1-INF; LEDGER X-71), and in addition at
least one of:

1. a decision of N2 for `d = 3` at some `(q, α)` and range, in either direction, beyond what any
   record states (R1-INF leaves `d ≥ 2` undetermined);
2. a proof or a countermodel for N4.1 or N4.2;
3. a native selection fixing `β` (N3.3), surviving N8;
4. an assumption of Stage 3 not recorded at GR:58–104, P7-B H1–H14, P1 rows 38–43 or LEDGER
   X-70–X-72.

Otherwise the outcome is recorded as a relabelling. Findings are classified NEW, POSITIVE,
ELABORATING, CONFIRMING or BORDERLINE (§A.31). N1, N5.1 and the `β_A` verdict of N7 are expected to
be CONFIRMING or ELABORATING and do not count toward the test.

## 6. Invariant→checkpoint table (§A.41)

| # | Invariant asserted of the execution | Checkpoint |
|---|---|---|
| I1 | This unit adds only `DESIGN.md` in this directory | `git diff --stat origin/main` at the head lists one file |
| I2 | No manuscript, Lean, registry, ledger or #1477 file changes in any P2-B commit | Same diff at every pushed head; the reviewer re-runs it |
| I3 | Decision rules precede results | The commit of this design is an ancestor of every execution commit; any rule change is an amendment in `amendments/` with a reason, made before the node it affects is run |
| I4 | Tiers are never promoted | Each node's verdict table has a tier column; the N8 pass checks every T-spec item against every later sentence |
| I5 | Exact arithmetic for exact claims | Every computational script asserts that its numeric types are integers, `Fraction`s or finite-field elements, and fails on a float; the reviewer greps the script for float literals and float division |
| I6 | Verdicts only over green controls | Each script runs its controls first and prints no verdict line if any control fails; the output file records the control lines |
| I7 | Two methods agree in N2 | The script prints both dimensions per cell and halts on disagreement |
| I8 | Deterministic replay | A second run's output is byte-identical; its digest is recorded beside the expected result (§A.42 item 1) |
| I9 | Citations of R1-INF carry its review standing | Grep of the execution records for "R1-INF" lines without "delta review outstanding" returns none |
| I10 | Negative results are scoped | Each negative verdict names its rule, `(d, q, α)`, range and law class; the N8 pass checks each |
| I11 | Local cost bound (§A.40) | Cells over `2^{24}` dual elements are listed for CI and not run locally |
| I12 | Repository text constraints | A grep of every added file for the excluded vocabulary and for local paths returns none |

## 7. Stop conditions and scope of negative results

**Stop.**
- Any control fails or is vacuous: the node halts and its verdict is void.
- A provenance anomaly (§A.26): sweep, then halt.
- A node needs a posit adopted, or a manuscript or ledger change: halt and refer to the owner.
- A local computation exceeds the I11 bound: stop, publish the partial state and a CI plan.
- N2 returns "none" for `d = 3` at every grid cell: the native Gibbs branch (N3, N4 for `F_sel`) is not
  run; N5–N7 still run, and the native verdict is generated at N7 from the T-nat-ex laws available.
- The fixed point of N8 is reached, or the authorized budget is spent: the open nodes are parked with
  named gaps.

**Scope.** A negative result is stated for the rule, parameters, range and law class tested, and
for nothing wider: "no conserved quantity of range ≤ `W` for `F_sel` at `(d, q, α)`" does not become
"no energy for OI's substratum"; failure of translation-invariant laws at N4.1 does not become
failure of every law; failure of P-ED or `β_A` to give a nonzero slope does not become failure of
every normalized law. A failure of the current construction is not an impossibility for an
observer-level extension.

## 8. Out of scope

- No proof is executed and no computation is run in this unit; every node above is a plan.
- No change to any manuscript (`papers/`, `book/`), to Theorem 23 or its scope, to the #1477
  retirement plan or its files, to LEDGER rows, to the Lean bridge, or to any registry.
- No adoption of any posit, including (G3), (G4), H2, H4, H6, H6′ or a selected law.
- Stage 1's return condition (P2-A) and the cross-stage identification (P2-C) are separate designs;
  this design neither uses nor anticipates their results.
- The identification of any conserved substratum quantity with the horizon first-law energy (R22),
  and the detector side (R20), are recorded and not investigated.

## 9. References outside `main` (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1532 at `0bc9628a`, `recon-inf-p1-20261121/AUDIT.md` | Phase 1 findings for Stage 3 | Provenance; confirmed draft, not on `main` |
| #1532 c.7068213461, c.7068281368, c.7068298957 | Review standing of Phase 1 | Provenance |
| #1169 c.7068325638 | Authorization | Quoted with author and time |

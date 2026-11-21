# RECON-INF P2-B: Stage 3 of Theorem 23 without finite counting (research design)

**Status.** Writer's research design, WIP / UNVERIFIED. It plans an investigation and executes
none of it: no proof is attempted, no computation is run, and no manuscript, Lean, registry, ledger
or #1477 file is changed. Revision answering the independent review of `b44cebe6` (REVISE, #1536)
and the owner's required resolutions (#1169 c.7068602936); an exact-head delta review is required.
No node is authorized; execution needs an accepted design and separate owner authorization.

**Authorization.** Owner `amaybaum`, [#1169 comment 7068325638](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7068325638),
2026-11-21T19:51:15Z: "RECON-INF Phase 2 | Research planning authorized | Plan Stage 1, Stage 3 and
the cross-stage bridge separately; no proof execution yet". Order item 5: "Phase 2 investigations,
only after their plans are reviewed". Phase 3 is not authorized.

**Scope, verbatim.** Owner `amaybaum`, [#1169 comment 7068447675](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7068447675),
2026-11-21T20:01:28Z: "**P2-B — Stage 3: Replace counting.** Test whether normalized measures on
infinite configuration spaces can support the required entropy and boundary calculations.
Distinguish invariant product measures for special coupled rules from a measure justified for the
selected native dynamics." The earlier comment's summary of the same item, for context: "Can
normalized measures on infinite configuration spaces carry the entropy and boundary calculations?
Invariant product measures for special coupled rules stay distinct from a measure justified for the
selected native dynamics."

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
| O-A4 | `o-a4-20261120/RESULT.md` | The record's own status section (:407–411) names REVISE on `1c69ea84` and a missing delta review; the merge commit `68d5759c` (#1441) records ACCEPT WITH NITS (c.7031523612) and CONFIRMED (c.7031576598), and the owner decision #1169 c.7031779559, item 1, as a preservation merge |
| REMAINDER | `a1-remainder-20261119/REMAINDER.md` | Consumer table at pin `21e16c61` (as in P1) |
| NR-1 | `nr1-near-return-20261116/NR-1.md` | ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| A1-03 | `a1-free-p7-coupled/DECISION.md` | SOURCE GAP at normalized invariant coupled-shell states |
| A1-07 | `a1-07-p7-energy-state/DECISION.md` | SOURCE GAP at the energy check (RD6 cut) |
| LEDGER | `a1exit-ledger-20261120/LEDGER.md` | Rows X-70 (F), X-71 (O), X-72 (F) |

## 1. The question

**Setting.** The native carrier is `Ω = (A×A)^{ℤ³}` with `A = ℤ_q`. The **selected native dynamics**
`F_sel` is the second-order form of Main:736 item (xiii) with the centre-free isotropic linear rule
of SM:224, `x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1) (mod q)`, in phase-space form
`(u, v) ↦ (αSu − v, u)` (R1-INF §2, delta review outstanding), with reversal `Θ` the slice swap.
`main` fixes neither `q` nor `α` (NR-1:101, row (Q)), so every statement below is indexed by
`(q, α)`. The rounded rule of SM:294 is a second candidate native rule; it is named where a node
covers it and is otherwise outside the grid.

**Observer partition.** Wherever a node uses the observer partition, it is the finite visible window
`V ⊂ ℤ³` with window (coordinate) readout `π = x|_V`, the hidden boundary layer `B` within the
interaction range of `V` (GR:116) and the deep remainder `D`, as in GR:112–122. The visible cells are
either the window configurations themselves (fine cells) or the classes of a stated energy function on
window configurations (coarse cells); every verdict states which.

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
| T-spec | A law on an infinite carrier, invariant for some coupled rule in a stated class that is not `F_sel` on `Ω` |
| T-fin | A law on a finite model or a finite restriction (a finite shell, a torus `Per_L`, a finite invariant truncation), of `F_sel` or of another rule; a finite illustration, outside the Q outcomes |
| T-nat-ex | A law on `Ω` invariant under `F_sel` and `Θ`, for stated `(q, α)`, only after a written construction of the law on `Ω` and a proof of its invariance; nothing about selection |
| T-nat-pos | Selected for `F_sel` only under named posits added to the corpus (for example R1-INF (G3)+(G4), delta review outstanding) |
| T-nat-dyn | Unique, with no free continuous parameter, among the `F_sel`-,`Θ`-invariant laws of one of the admissible classes K0–K4 frozen in N7, with N7.0 run before N2, all of whose restrictions are manuscript premises in the sense of N7.0; "unique" means the class is a singleton (N7); the class uses the observer partition above where it names a readout |

A T-fin result is never cited as T-nat-ex; promotion needs a construction on `Ω` as its own node.

**Outcome set, fixed in advance.** (Y-dyn) Q holds at T-nat-dyn; (Y-pos) Q holds only at T-nat-pos;
(Y-ex) the calculations of Q items 1–2 go through for an `F_sel`-invariant law on `Ω` that is only
T-nat-ex, so Q item 3 (values fixed by `μ` and the dynamics) is not met; recorded as (Y-ex) and parked
at N7 for selection; (Y-spec) Q holds only at T-spec, for a law on an infinite carrier; (N-scoped) Q fails for a stated
construction class, with a countermodel or proof scoped to that class; (U) undetermined, parked at a
named node. T-fin findings are recorded as finite illustrations and are not Q outcomes. The design
does not favour any of these.

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
| B4 | Finite boundary configuration set | P7-B H2 (posited); GR:882 (D4) | Finiteness of `C_B` only | Posit |
| B5 | Boundary-only dependence; deep-cardinality gauge | GR:112–138; GR:871–905, (D5) at GR:883 | A product prior `u_{B_n} ⊗ ν` (Appendix B) or a measure form of H-BD (open, REMAINDER L10). GR:144 states that the matching does not use it | Uniform prior on finite `C_H` |

### 2.2 Candidate measures

| Id | Candidate | Carrier and rules covered |
|---|---|---|
| M0 | Counting on finite restrictions: finite shells, tori `Per_L`, finite invariant truncations | Finite restrictions of any rule; cylinder limit on `Ω` is `β_A` for injective CA (R1-INF Lemma 1 (b), :83, delta review outstanding) |
| M1 | Uniform Bernoulli product law `β_A` (Haar for linear rules) | Invariant for every second-order rule over a finite abelian group (O-A4 Lemma U, :69) |
| M2 | Non-uniform product laws, including product Gibbs laws `∝ ∏_z e^{−βφ(x_z)}` | Invariance depends on the rule; fails for `F_sel` with `q = 2, α = 1` under `Bern(1/4)` (R1-INF C7 (i), delta review outstanding) |
| M3 | P7-B's H4 product: counting on a finite boundary shell times a normalized deep law `ν` | Decoupled dynamics (P7-B 6.3, proved); some coupled bijections with a `φ`-adapted `ν` (P7-B 6.3 (i)) |
| M4 | Translation-invariant Gibbs/DLR laws of an interaction with summable variations | Set level, as quoted in R1-INF Prop. 6 (c), :222–226 (delta review outstanding; to be verified at L1): a surjective CA conserves the interaction iff it maps the set of shift-invariant Gibbs laws of that interaction onto itself, iff it maps one such law into that set (Kari–Taati 2015, Thm. 41). Law by law only one direction follows: an invariant Gibbs law implies conservation. Conservation does not make each Gibbs law invariant when several exist; an invariant law inside the set is an L1 item |
| M5 | Laws maximizing entropy density at fixed densities of conserved quantities | The set of such laws at a fixed density is mapped onto itself under conservation (Kari–Taati Thm. 42, one direction, same citation, delta review outstanding) |
| M6 | P-ED: maximal entropy density among `F`- and translation-invariant laws | Selects `β_A` for every injective CA on a full site product under (G1)–(G4) (R1-INF Prop. 3, :114–122, delta review outstanding) |
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

**Order and branching.** N0 (with N7.0) → N1 → N2.0 → N2. N7.0 is documentary, runs inside N0, and
its outcome is committed as an amendment before N2 starts; K0–K4 are frozen from that commit. Method A
is evidence only after N2.0, so productivity item 1 and N2's branch both depend on N2.0. N2's outcome
selects the next branch: a native conserved
quantity sends N3 and N4 to `F_sel`; none within N2's range grid sends N3 and N4 to the T-spec models
only, pending N2.3, and the native verdict is generated at N7 conditional on N2's range bound. This is
a resource choice: a range-bounded "none" is not a statement that `F_sel` has no conserved energy. N5
and N6 run in either case. N8 closes.

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
content for `F_sel`, and by the law-level direction of L1 (an invariant Gibbs law implies
conservation) no translation-invariant Gibbs law of a finite-range interaction not physically
equivalent to zero is `F_sel`-invariant.

**Method A (character orbits; linear rules).** A real range-`W` potential is a combination of
characters of `A^W` and their conjugates. For a linear rule, composition with `F` maps characters to
characters through the dual map `F^*`, which commutes with translations. The planned reduction is
that a nontrivial conserved range-`W` quantity exists iff some nonzero finitely supported dual
configuration has a finite `F^*`-orbit modulo translations, every member of which has a translate
supported in `W`. **N2.0** proves this reduction in writing before any use; until then method A is
not evidence.

**Method B (direct linear algebra).** The conservation condition on range-`W` potentials, as a
linear system over `ℚ`, solved by exact fraction-free elimination. Two forms, recorded per cell:
**B-exact**, by an L2 criterion valid on `ℤ^d` (only if N0 finds one); **B-torus**, by torus
equations. B-torus is one-sided: at a size `L` that passes the injectivity check below it bounds the
`ℤ^d` conserved space from above (R1-INF :540–541, delta review outstanding, states this direction;
L2 is to confirm it), and it never bounds it from below. A zero on finite tori is never taken, by
itself, as absence on `ℤ^d`.

**Algorithm for method A (preregistered).** Enumerate the nonzero translation classes of characters
supported in `W`; build the functional graph sending a class to the class of its `F^*`-image when that
image has a translate supported in `W`, and to an absorbing "out" node otherwise; the conserved range-`W`
quantities are spanned by the class sums over the cycles of this graph. Cost is one image computation
per class plus linear-time cycle detection.

**Torus sizes and injectivity (B-torus).** For a window of side `s` and update radius 1, the torus
sizes are `L ∈ {2s+3, 2s+4, 2s+5, 2s+6}`, fixed here; the set contains both parities and, for each
`q ∈ {2, 3, 5}`, sizes divisible and not divisible by `q` where the range allows, since period
properties of the exact rule depend on divisibility (SM:296). For each `L`:
- an exact rank check that range-`W` potentials modulo the `ℤ^d`-trivial ones (constants and
  translation coboundaries of range `W`) inject into torus functions modulo the torus-trivial ones;
- the trivial-part dimension is computed for each `L` by a routine separate from the solver.

A cell with a failed injectivity check at some `L` gives no B-torus value at that `L`. Once L2
confirms the upper-bound direction for the check used, the value `B_L` at each single `L` that passes
the injectivity check is a certified upper bound by itself. The B-torus excess is reported as a
function of `L`; it is called stable only if it is the same at every preregistered `L` that passes the
injectivity check, with at least two such `L`, and stability is the condition for reporting "torus
upper bound `k`". Without L2's confirmation every B-torus value is an uncertified torus observation.

**Grid and cost (preregistered, §A.40).** `d ∈ {1, 2, 3}`; `q ∈ {2, 3, 5}`; every `α ∈ ℤ_q`, with
`α = 0` as a countercontrol (`F^4 = id`); `W` the cubes of side `s ∈ {1, 2}`, and `s = 3` for `d ≤ 2`.
Write `N = q^{2s^d}` for the number of characters supported in `W`. Method A costs about
`N·s^d·(2d+1)` finite-field operations per `α`; method B has `N` unknowns, and B-torus has
`E_L = q^{2L^d}` equations at each preregistered `L`. Exact elimination costs about
`E_L · N · rank ≤ E_L · N²` operations per `L` and per `α`; the B-torus estimate of a cell is that
bound summed over its preregistered `L` and over `α`. B-torus runs in a cell only if that total is
within the local budget; the `L` set is not reduced to fit. In `d = 2` and `d = 3`, `L ≥ 5` gives at
least `q^{50}` equations, and B-torus is not run. Classification of each cell by total cost over all
`α`:

| `d` | `s` | `N` at `q = 2, 3, 5` | Method A | Method B |
|---|---|---|---|---|
| 1 | 1, 2, 3 | `q^{2s}`: at most `5^6 = 15 625` | local | B-torus local only at `q = 2`, `s = 1` (`2^{16}·4²` at `L = 8`, about `10^6`) and `q = 2`, `s = 2` (`2^{20}·16²` at `L = 10`, about `3·10^8`; under `10^9` summed over `L` and `α`). Above the budget, not run: `q = 2`, `s = 3` (`2^{24}·64²`, about `7·10^{10}`); `q = 3`, `s = 1` (`3^{16}·9²`, about `3.5·10^9`); every other `q = 3` and `q = 5` cell |
| 2 | 1 | 4, 9, 25 | local | not run (B-exact only, if N0 supplies a criterion) |
| 2 | 2 | 256, 6 561, 390 625 | local | not run (B-exact only, if N0 supplies a criterion) |
| 2 | 3 | 262 144; 3.9·10⁸; 3.8·10¹² | `q = 2` local; `q = 3` CI; `q = 5` not run | not run |
| 3 | 1 | 4, 9, 25 | local | not run (B-exact only) |
| 3 | 2 | 65 536; 4.3·10⁷; 1.5·10¹¹ | `q = 2` local; `q = 3` CI; `q = 5` not run | not run (B-exact only) |

"Local" means an estimated total below about `10^9` operations and `10^8` stored classes. "CI" marks
the cells whose estimated cost exceeds the local budget. P2-B CI computations are not authorized (#1169
c.7068602936): a CI cell runs only after this preregistration is accepted and the owner separately
approves that cell's cost (§A.40, §A.43 item 4). No CI cell is run locally. "Not run" cells are
reported as not computed, with no verdict. Before any cell runs, the estimate is re-measured on the
smallest instance and the table is amended (in `amendments/`, before that cell) if the measurement
moves a cell across a class. A cell's class changes only by such an amendment made before that cell
runs, and no cell runs, locally or in CI, without the owner's authorization of execution. The `d = 3`
verdicts rest on method A after N2.0, and on B-exact only if N0 supplies an `ℤ^d` criterion with its
own cost estimate; B-torus is not used in `d = 3`.

**Single-site cells are not decisive.** For `s = 1` and `α ≠ 0` (every grid `q` is prime, so `α` is a
unit), no cycle exists, in any `d`, by a support argument. The dual map is
`F^*(a, b) = (αSa + b, −a)`, from `(a·(αSu − v) + b·u)` with `S` symmetric. A single-site character
with `a ≠ 0` has `u`-part `αSa + b`, which is nonzero on the `2d` neighbours, so its image has no
translate supported on one site. A single-site character with `a = 0`, `b ≠ 0` maps to `(b, 0)`, which
then maps out of `W` by the same argument. So the `s = 1`, `α ≠ 0` cells serve as checks of the code,
not as findings. The one local `d = 3` cell with content is `s = 2`, `q = 2`, `α = 1`, and it is
evidence only after N2.0. The `s = 2`, `q = 3` cells are CI cells, and so need an accepted
preregistration and the owner's separate approval of their cost, which P2-B does not have. The rounded
rule of SM:294 is outside method A; method B covers it only in the local `d = 1` B-torus cells above.

**N2.3 (written, all ranges; later authorization).** For prime `q`: is there a nonzero finitely
supported `ξ`, `n ≥ 1`, a translation `τ_t` and `c ∈ ℤ_q^×` with `F^{*n} ξ = c·τ_t ξ`? This is a
statement about eigenvalues of the companion matrix `[[αS, −1], [1, 0]]` over the Laurent ring
`ℤ_q[x_1^{±1}, …, x_d^{±1}]`, `S = Σ_j (x_j + x_j^{−1})`. A comparison of Newton polytopes is one
candidate method; it is not carried out here, and the node is open in both directions.

**Decision rule.** Comparison of the methods, by what each measures:
- A (after N2.0) and B-exact both run → any difference in the excess dimension halts the node; its
  verdict is void.
- A (after N2.0) and certified B-torus values both run → the compatible relation is `B_L ≥ A` at
  every certified `L`; `B_L < A` at any single certified injective `L` halts the node and voids the
  cell, since that pair of certified results is incompatible. A gap `B_L > A` is not a conflict: it is
  recorded, and the cell's value is A's, scoped to N2.0's theorem.
- Uncertified results (A before N2.0, B-torus without L2's confirmation or without stability) never
  halt the node and never yield a verdict; they are recorded as observations.
- Only B-torus runs (A not yet licensed by N2.0) → no `ℤ^d` verdict in either direction. A stable
  certified B-torus excess 0 is recorded as "torus upper bound 0 at the preregistered `L`", and an
  absence verdict on `ℤ^d` waits for A after N2.0 or for B-exact.

Verdicts:
- Excess 0 by A after N2.0, or by B-exact → "no nontrivial real additive conserved quantity of range
  `W` for `F_sel` at `(d, q, α)`, pending N2.3". Scoped to that `W` and those parameters.
- Excess `k > 0` by A after N2.0 or by B-exact → record a basis; each basis element is checked exactly
  on `ℤ^d` (by the L2 criterion or a written proof) before it is a native candidate for S1.
- N2.3 proved → the scoped statement extends to all finite ranges for that `(d, q)` and every
  `α ≠ 0`. N2.3 refuted by an explicit `ξ` → native candidate. Neither within the authorized budget →
  parked at N2.3, named gap.
- A native candidate, if any, is a mathematical conserved quantity only. Its identification with the
  horizon first-law energy remains R22 (M), and no node here supplies it.

**Controls.**
- *Positive control, two methods:* runs only where both methods run under the cost table, which is
  `d = 1`, `(q, α) = (2, 1)`, range 2 (`s = 2`). Both values must satisfy the comparison rule above.
- *Positive control, independent recount:* for every `d = 1` cell with `α² ≡ 1 (mod q)` and `s = 2`,
  a routine separate from the functional-graph code builds the mover characters
  `c·a_0` and `c·b_0`, `c ∈ ℤ_q∖{0}`, with `a_z = u_z − αv_{z+1}` and `b_z = u_{z+1} − αv_z`; it checks
  by direct evaluation of `ξ∘F` on configurations (not by the dual formula) that each maps to a
  translate of `cα·a_0` or `cα·b_0`, and counts the resulting cycles, which is `2·#(ℤ_q^×/⟨α⟩)`
  computed by that routine. Method A's excess must be at least this count (the movers are a lower
  bound); A below it voids the cell. Equality, and agreement with
  R1-INF §9 E (delta review outstanding), are recorded as cross-checks.
- *Exactness control:* the identity CA and the shift CA (every potential conserved): the computed
  dimension must equal the full dimension minus the trivial part, by a count computed independently.
- *Symmetry control:* the action of `Θ` and of each generator `h` of the cubic point group on
  supports must map the computed basis into its span, checked exactly; this tests equivariance. The
  dimension of each isotypic component is compared as follows. Where method B runs, B's solution space
  is decomposed and compared with A's. In cells where only A runs, the permutation character of the
  point group on the cycles is computed by a routine independent of the functional-graph code: its own
  canonicalization of translation classes, and its own orbit enumeration by direct evaluation of
  `F^{*n}ξ = τ_t ξ` (`τ_t` a translation, `h` a point-group element, `χ(h)` the number of cycles with
  `h·C = C`); the isotypic dimensions from that character must equal A's. `Θ`-invariance of the
  conserved space follows from `ΘFΘ = F^{−1}` and is a necessary property, not a discriminating one.
- *Countercontrols:* (i) an injected non-conserved potential (a single-site value of `u`) must be
  rejected and an injected mover (`d = 1`) accepted by the checker; (ii) `α = 0`: here `F` acts site
  by site with `F^4 = id`, so every character supported in `W` has a finite orbit and stays supported
  in `W`; the computed excess must equal the value from a Burnside count of `⟨F^*⟩`-orbits on the
  nonzero translation classes supported in `W`, under the trivial-part convention written down before
  the run.
- *Replay:* each run is deterministic and its output must replay byte for byte (§A.26 item 3).

### N3. Gibbs laws of a conserved quantity: does anything fix the slope?

Runs on N2's native candidates if any; otherwise on T-spec models only: (a) `F_sel` in `d = 1` with
`α² ≡ 1` (a different dynamics from `F_sel` on `ℤ³`, hence T-spec), (b) P7-B's decoupled models,
(c) a rule built with a site-additive conserved energy, chosen before the check and recorded; (d) the
real lift of the linear rule, whose quadratic is positive definite for `|α| < 1/d` (SM:292), a
different carrier from `Ω` and hence T-spec. Every N3 verdict carries a tier column.

**N3.1 Existence.** For a conserved interaction `Φ`: the set of translation-invariant Gibbs laws of
`βΦ` is mapped onto itself (L1, set level); an `F`-invariant law inside that set (L1 item: a fixed
point of the affine continuous map `F_*` on a compact convex set); and its `Θ`-invariance (which needs
`Φ∘Θ` physically equivalent to `Φ`). **Decision rule:** existence of an invariant Gibbs law is recorded
per `β` only with L1's hypotheses verified for `Φ` and the fixed-point step written out; where the Gibbs
set at `β` has one element, that element is invariant; otherwise the record says which law is
invariant, or "not established for `Φ`".

**N3.2 Visible weights.** Under the DLR conditional, compare the visible cell masses `p_i` with
`e^{−βe_i}` normalized. Computed in the models with partition functions as integer polynomials in
`x = e^{−β}`. **Decision rule:** "equality" iff `p_i Σ_j x^{e_j} = x^{e_i}` holds as an identity of
integer polynomials (after clearing denominators) for every `i`; otherwise "deviation", with the
deviation factor `p_i/(x^{e_i}/Σ_j x^{e_j})` recorded exactly as a rational function of `x`, and its
dependence on the visible–boundary interaction (the H-shell condition of GR:60) stated.

**N3.3 Selection of `β`.** Candidates: P-ED (gives `β = 0`), maximal entropy at fixed conserved
density (M5), torus microcanonical limits at fixed density (M0 with L5), ergodic decomposition.
**Decision rule (conditional on N3.2, with tier):**
- every candidate leaves `β`, or the conserved density, as a free continuous parameter, and N3.2
  recorded "equality" → "for `Φ` at tier T, the Gibbs route gives S2's form without counting; the
  slope is carried by the choice of `β`, a parameter of the law";
- the same, with N3.2 "deviation" → "for `Φ` at tier T, the Gibbs route gives S2's form only up to
  the recorded deviation factor; the slope is carried by `β`";
- one candidate fixes `β` from the dynamics and the partition with no target input → provisional
  favourable at tier T, sent to N8;
- T is the tier of `Φ` and of its rule (T-spec for models (a)–(d)); a T-spec verdict is never
  restated for `F_sel`.

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
energy. Under coupled dynamics (GR:128: the update displayed in Main §3.2 has `L ≠ 0` "at every cut
where a boundary site has a deep neighbour"):

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
quantities. N4.1 "yes" → record the law and send it to N8. N4.2: an explicit invariant law found on
a finite model, of `F_sel` or of another rule, is T-fin; it is never T-spec or T-nat-ex, since both
need a law on an infinite carrier. Promotion to T-nat-ex needs its own node: a written construction of a law on `Ω` (for
example a cylinder limit) with a proof of its invariance under `F_sel` and `Θ`. None found in the
models → no statement beyond those models. N4.3 → record which quantity the visible weights depend
on, from N3.2's formula.

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
`Unif(V) ⊗ δ_0` (R1-INF §9 C, delta review outstanding), any equality claimed for invariant laws
must fail.

### N6. Special coupled rules (T-spec classification)

**Question.** For which coupled rules does an invariant product law exist, and does it resolve
energy?

- `β_A` for every second-order rule (O-A4 Lemma U, a construction on `Ω` with its invariance proof):
  T-nat-ex for `F_sel`. Its fine-cell window marginal is uniform because it is a product law; its
  coarse-cell weights are derived at N7.
- P7-B 6.3 (i): a coupled bijection with a `φ`-adapted `ν`: T-spec.
- Product Gibbs laws `∝ ∏_z e^{−βφ(x_z)}`: by L1, invariant iff the rule conserves the single-site
  potential `φ`, which is N2's cell `W` = one site. For `F_sel` this node reads N2's result and adds
  nothing to it.

**Decision rule.** Each law is listed with its rule class, its tier, and whether it resolves energy.
A law that is invariant for some coupled rule and not shown invariant for `F_sel` stays T-spec in
every later sentence.

### N7. Justification for the selected native dynamics

**Question.** Among laws on `Ω` established as T-nat-ex (a construction on `Ω` and a proof of
invariance under `F_sel` and `Θ`), which, if any, are unique within an admissible class, and is that
class T-nat-dyn or T-nat-pos? The verdict is conditional on N2's range bound and on N2.3's status.

**Admissible classes (frozen here, before any outcome is examined).** Each is the set of Borel
probability laws on `Ω` invariant under `F_sel` and `Θ`, further restricted as follows:

| Class | Restriction added | Classification of the restriction |
|---|---|---|
| K0 | none | manuscript premise (the update and reversal only) |
| K1 | K0 and full support (every cylinder has positive mass) | added posit, unless N7.0 finds it adopted as a manuscript premise for infinite carriers |
| K2 | K1 and product form `u_V ⊗ ν` at the visible window of the observer partition (§1) | added posit: H-μ(φ,Θ), a named hypothesis not adopted (O-A4 :64) |
| K3 | K2 and translation invariance | added posit (R1-INF (G3), delta review outstanding) |
| K4 | K3 and maximal entropy density | added posit (R1-INF (G4), delta review outstanding) |

**Ergodic variants (frozen here).** For each `Kj`, `Kj^erg` is the set of laws in `Kj` that are
ergodic for the group generated by `F_sel` and `Θ`, and also by the translations for `j ≥ 3`.
Ergodicity is an added posit, so uniqueness within a `Kj^erg` is at most T-nat-pos.

**N7.0 (documentary; runs in N0, before N2).** For each restriction of K1–K4, search `papers/` and
`book/` (chapters and FULL) at the pin. A restriction counts as a manuscript premise only if a
manuscript adopts it as a premise for infinite carriers: an axiom, or a posit-ledger item not stated
"on a finite representative". Named hypotheses (for example H-μ(φ,Θ)), hypotheses of records under
`verification/` (for example R1-INF (G3), (G4), delta review outstanding) and statements about
examples do not count. Ledger item (iv) (Main:736) is stated "on a finite representative" and does
not count. The search terms and the per-row result are committed as an amendment in `amendments/`
before N2 starts; K0–K4 and their `Kj^erg` variants are frozen from that commit and are not changed
afterwards.

**Decision rule.** Uniqueness is tested within K0–K4 and `K0^erg`–`K4^erg` only. The classes `Kj` are
convex, so "unique" in `Kj` means `Kj` is a singleton `{μ}`; in `Kj^erg` it means exactly one ergodic
law. A singleton class all of whose restrictions are manuscript premises gives T-nat-dyn; a singleton
class, or a unique ergodic law, needing an added posit gives T-nat-pos, with the posits named; no
uniqueness in any class → no selection, outcome (Y-ex) or (U) at N7. No other class is admissible for
these tiers.

**Stage 3 under the selected law, if any (outcome-neutral).** For each law at T-nat-dyn or T-nat-pos,
and for `β_A` as the T-nat-ex law of N6, derive at execution, exactly, for each readout of §1 (fine
window cells; coarse cells of each energy function supplied by N2 or stated in advance, each such
function required to be `Θ`-even, `E∘Θ = E` on window configurations, so that `θ` maps each coarse
cell to itself; a function that is not `Θ`-even is not used for coarse cells):
- the visible masses `p_i`;
- the paired fluxes `J_ij` and the rate ratios `T_ij/T_ji`;
- the divided-difference slope where an energy is defined.

The verdict text is generated from those values, scoped to the readout and to the law, and carries
"delta review outstanding" wherever an R1-INF result enters.

**Controls (independent of the verdict's sources).**
- *Positive control:* on a small torus restriction, exact rational masses and fluxes under the uniform
  law, computed by brute force over the hidden light cone (the method of O-A4 §11 part A, :161), must
  satisfy `J_ij = J_{θj,θi}` exactly (P6; Lean `MeasuredReciprocity.reciprocal_flux`:90), for both
  fine and coarse cells.
- *Countercontrol (preregistered):* `d = 1`, `q = 2`, `α = 1`; the law `μ_c` obtained from
  `λ = π^{⊗ℤ} ⊗ π^{⊗ℤ}` on the mover coordinates `(a, b)`, with `π = (3/4, 1/4)` on `ℤ_2`, lifted by the
  uniform law on the fibres (the construction of R1-INF Prop. 6 (b), delta review outstanding, used
  only as a definition); readout `a_0 = u_0 − v_1`; cell pair `(0, 1)`; one step. The control first
  verifies exactly, with rational cylinder masses computed from the definition, that
  `μ_c(F^{−1}C) = μ_c(C)` and `μ_c(Θ^{−1}C) = μ_c(C)` for every cylinder `C` on the window `[−2, 3]`. If
  either check fails, the countercontrol is void and so is the node's verdict. If both pass, the same
  procedure as the verdict must report `T_01/T_10 ≠ 1`; if it does not, the procedure cannot detect a
  slope and the node's verdict is void.
- *Class countercontrol:* the identity CA and a lattice translation, for which every
  translation-invariant law is invariant, must come out non-unique in K3.

### N8. Pressure on favourable branches; fixed point

Every branch whose outcome favours a replacement of counting (N3.3 fixing `β`, N4.1 "yes", N5.4
proof, N7 at T-nat-dyn) is re-examined for: a hidden use of a finite set or of the target value; a
tier promotion; a sufficiency result stated as necessity; a conditional stated unconditionally (Code
Review Rules). Passes continue until three consecutive passes give no NEW finding (§A.31).

## 5. Productivity test (fixed before N0)

The investigation is a gem iff it gives a statement strictly stronger than "Stage 3 needs a selected
law, the slope is H6, and the coupled case is open" (P7-B; R1-INF, delta review outstanding; LEDGER
X-71), and in addition at
least one of:

1. a decision of N2 for `d = 3` at some `(q, α)` and a window of side `s ≥ 2` (the `s = 1` cells are
   settled by the support argument in N2), in either direction, beyond what any
   record states (R1-INF, delta review outstanding, leaves `d ≥ 2` undetermined);
2. a proof or a countermodel for N4.1 or N4.2;
3. a native selection fixing `β` (N3.3), surviving N8;
4. an assumption of Stage 3 not recorded at GR:58–104, P7-B H1–H14, P1 rows 38–43 or LEDGER
   X-70–X-72.

Otherwise the outcome is recorded as a relabelling. Findings are classified NEW, POSITIVE,
ELABORATING, CONFIRMING or BORDERLINE (§A.31). N1, N5.1 and the N7 derivation for `β_A` do not count
toward the test.

## 6. Invariant→checkpoint table (§A.41)

| # | Invariant asserted of the execution | Checkpoint |
|---|---|---|
| I1 | This unit adds only `DESIGN.md` in this directory | the diff stat against the pin `df6da1c6101e811acdc7952d5748aff57028e8ed` at the head lists one file |
| I2 | No manuscript, Lean, registry, ledger or #1477 file changes in any P2-B commit | Same diff at every pushed head; the reviewer re-runs it |
| I3 | Decision rules precede results; K0–K4 frozen before N2 | The commit of this design is an ancestor of every execution commit; any rule change is an amendment in `amendments/` with a reason, made before the node it affects is run; the N7.0 amendment is an ancestor of every N2 commit |
| I4 | Tiers are never promoted | Each node's verdict table has a tier column; the N8 pass checks every T-spec item against every later sentence |
| I5 | Exact arithmetic for exact claims | Every computational script asserts that its numeric types are integers, `Fraction`s or finite-field elements, and fails on a float; the reviewer greps the script for float literals and float division |
| I6 | Verdicts only over green controls | Each script runs its controls first and prints no verdict line if any control fails; the output file records the control lines |
| I7 | N2's methods are compatible | The script prints both values per cell with their certification status; it halts only when A and B-exact differ, or a certified B-torus value at any single injective `L` is below A's |
| I8 | Deterministic replay | A second run's output is byte-identical; its digest is recorded beside the expected result (§A.42 item 1) |
| I9 | Citations of R1-INF carry its review standing | Grep of the execution records for "R1-INF" lines without "delta review outstanding" returns none |
| I10 | Negative results are scoped | Each negative verdict names its rule, `(d, q, α)`, range and law class; the N8 pass checks each |
| I11 | Cost classes (§A.40) | Each cell's estimated cost and class are recorded in the N2 table; a class changes only by an amendment made before that cell runs; no cell runs, locally or in CI, without the owner's authorization of execution; "CI" cells also need an accepted preregistration and the owner's separate approval of their cost; "not run" cells report no verdict |
| I12 | Repository text constraints | A grep of every added file for the excluded vocabulary and for local paths returns none |

## 7. Stop conditions and scope of negative results

**Stop.**
- Any control fails or is vacuous: the node halts and its verdict is void.
- A provenance anomaly (§A.26): sweep, then halt.
- A node needs a posit adopted, or a manuscript or ledger change: halt and refer to the owner.
- A local computation exceeds its estimate class: stop and publish the partial state and a CI plan;
  the CI plan runs only after an accepted preregistration and the owner's separate approval of each
  cell's cost.
- N2 returns "none" for `d = 3` at every certified grid cell: the native Gibbs branch (N3, N4 for
  `F_sel`) is not run, pending N2.3; N5–N7 still run, and the native verdict is generated at N7 from
  the T-nat-ex laws available, stated as conditional on N2's range bound.
- The fixed point of N8 is reached, or the authorized budget is spent: the open nodes are parked with
  named gaps.

**Scope.** A negative result is stated for the rule, parameters, range and law class tested, and
for nothing wider: "no conserved quantity of range ≤ `W` for `F_sel` at `(d, q, α)`" does not become
"no energy for OI's substratum"; failure of translation-invariant laws at N4.1 does not become
failure of every law; failure of P-ED or `β_A` to give a nonzero slope does not become failure of
every normalized law. A failure of the current construction is not an impossibility for an
observer-level extension.

## 8. Out of scope

- No proof is executed and no computation is run in this unit; every node above is a plan. Execution
  is not authorized (#1169 c.7068602936). P2-B CI computations in particular are not authorized: each
  needs an accepted preregistration and the owner's separate approval of that case's cost.
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
| #1169 c.7068447675 | Verbatim P2-B scope | Quoted with author and time |
| #1169 c.7068602936 | Owner's required resolutions of the review; CI not authorized | Provenance |
| #1536 review of `b44cebe6` (REVISE) | Findings answered by this revision | Provenance |

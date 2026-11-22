# G3-OFFDS: the off-de-Sitter horizon functional, temperature and exchange law

**Standing.** Author record of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). WIP / UNVERIFIED. Independent non-author review at `96ffff23`: REVISE (#1545
c.7076925155). This revision answers its findings 1–5 and nits 6–9. The preregistration `PLAN.md`
(commit `bd8255f4`) was pushed before this record and is unchanged. The guiding PR's description
predates this revision and is not updated, since PR-description writes are halted (owner, #1169
c.7076910606). Where the two differ, this record governs. The unit adopts no premise, runs no computation,
and edits no manuscript, Lean module, registry or shared record. Authorization, snapshot, sources,
assumptions (A-…), decision rule and goal link are as in `PLAN.md`.

**Labels.** ESTABLISHED: derived on paper here [W], or a quoted standard result [L], at the stated
scope. ASSUMED: a premise of the `PLAN.md` table. MISSING: supplied neither by the corpus nor by this
unit. [W] derivations are not independently reviewed and not kernel-checked. Conjectures are marked
as such where they occur.

**Notation.** Units ħ = c = k_B = 1, G kept. Flat FLRW (A-FLRW), areal radius R = a r, Hubble rate H,
ε ≡ −Ḣ/H², apparent horizon R_A = 1/H (so Ṙ_A = ε), event horizon R_E = a∫_t^∞ dt′/a (so
Ṙ_E = HR_E − 1), V = 4πR³/3, S = πR²/G. For matter, m ≡ 8πGρ_m/3 and x ≡ ln a; a prime is d/dx.
R1, R2, R3 are G3-HOM's completions (`PLAN.md`).

***

## 0. Verdict

**Outcome under the decision rule: selected, conditional on A-KH.** Under the Kodama–Hayward
completion A-KH (imported, not adopted), the off-de-Sitter energy functional is the Misner–Sharp
mass on the trapping (apparent) horizon, its temperature is GR:56's T_A, and it carries no exchange
law because it describes the total (ρ, p) and no separate component. This selects R1 in its
Misner–Sharp reading: the value E = R_A/(2G) is kept exactly off de Sitter, and R1's label T = H/2π
is not kept. The selection holds only on that value reading, which `PLAN.md`'s definition of R1
("which G3-HOM 2.1 identifies with the Misner–Sharp mass") admits. Read with its temperature label
H/2π, R1 contradicts A-TA and A-KH, as G3-HOM Node 4 records. On that reading no candidate is
consistent under A-KH, a case the decision rule's branches do not cover. R2 and R3 contradict A-KH
(§4). The selected completion has no dynamics: it fixes no
w(z) and no Λ_eff, and it makes the GR §7.2 identity the Friedmann constraint. So under A-KH the
horizon budget supplies no separately gravitating homogeneous component, and the vacuum-energy
question passes wholly to the native source (W1-0 with its stress).

**Without A-KH, none is selected.** The corpus alone does not fix the off-de-Sitter functional
(GR:56). Its native partition (GR:40, A-PART) is the event horizon, which A-KH does not use, and
G3-HOM's R2/R3 counterexample stands. Under the decision rule, the minimal discriminating input
is **the temperature law on a non-Killing horizon, together with the surface in the T = 1/(2πR)
branch only**. The Kodama–Hayward law separates R2 from R1 and R3 by itself. The 1/(2πR) law
excludes R2, and the surface then separates R1 from R3. The exchange law is not needed to separate
the candidates. It is needed to fix w(z) within R2 or R3 (3.3, 3.4), which is G3-HOM's
missing-input sense. Off R_A, the Kodama–Hayward scalar κ(R) is a formal extension (2.2). If the
law is taken to be defined on R_A only, specifying it fixes the surface as well, and the answer is
the same. The preregistered primary outcome (selected, conditional on A-KH) is unchanged by this
correction. Only the statement of the minimal discriminating input in the no-premise branch is
corrected.

| Item | Corpus alone | Under A-KH | Under A-CK |
|---|---|---|---|
| (a) functional and surface | MISSING (GR:56); partition = event horizon (GR:40), counted area = apparent horizon (GR:56) | Misner–Sharp mass on the trapping horizon R_A [L, W] | Matter flux through R_A; ∫T dS = R_A/G = 2S·T, a state function of the area [W] |
| (b) temperature | Quoted value T_A at R_A (GR:56); its off-de-Sitter derivation is MISSING (GR:56, GR:58) | T_A = \|κ_KH\|/2π [L, W] | 1/(2πR_A) [L] |
| (c) exchange law | MISSING; Type I and Type II are named alternatives (GR:382) | None: one conserved total (Kodama current) [L] | None stated |

**Productivity test (§A.31): met.** Items (i), (ii) and (iii) of the test are each met by a fact
stronger than G3-HOM Node 4's restatement: (i) R2 and R3 are excluded under A-KH (§4); (ii) the
surface is shown not to be needed for the λS·T/V density under the Kodama–Hayward temperature law
(2.2); (iii) GR:58's counting derivation assumes a state-function energy. Off de Sitter, the first-law
energy is a state function of the area under the Cai–Kim temperature 1/(2πR_A), which contradicts
GR:56's T_A, and is not one under the Kodama–Hayward temperature T_A (1.4, §5).

***

## 1. Node 1: the energy functional and its surface

**1.1 What the corpus states (source check).** GR:56 restricts the calibration to exact de Sitter.
It notes that the event horizon of GR:40 and the apparent horizon of the counted area "coincide only
in exact de Sitter", and that a Kodama–Hayward extension "is not established here". GR §7.2
(GR:420–436) computes E_s = S·T_cl with κ = H on R_A and states that "its use as a physical source is
a separate question". GR:58 uses as shell energy the horizon first-law energy, E = R/G on exact de
Sitter. Str:409 and Str:459 restate the Type II reading and asymptotic de Sitter and add no
off-de-Sitter functional. Verdict: ESTABLISHED (source fact), the corpus states no off-de-Sitter
energy functional. CONFIRMING.

**1.2 The Kodama–Hayward objects [L, with the FLRW evaluation W].** In a spherically symmetric
spacetime with normal-space metric h_ab, the Kodama vector K^a = −ε^{ab}∇_b R gives a current
J^a = −T^a_b K^b that is conserved for any conserved T_ab (Kodama, Prog. Theor. Phys. 63, 1217
(1980)). Its charge is the Misner–Sharp mass E_MS = (R/2G)(1 − ∇R·∇R) (Misner and Sharp, Phys. Rev.
136, B571 (1964); Hayward, PRD 53, 1938 (1996), gr-qc/9408002). The trapping horizon is where ∇R is
null. There the dynamic surface gravity is κ = ½□_h R (Hayward, CQG 15, 3147 (1998), gr-qc/9710089;
Hayward, Mukohyama and Ashworth, gr-qc/9810006, where the trapping-horizon entropy is a quarter of
its area). In flat FLRW, with h = −dt² + a²dr²:

- ∇R·∇R = 1 − H²R², so K·K = −(1 − H²R²). K is timelike inside R_A, null on R_A and spacelike
  outside. The trapping horizon is R_A.
- E_MS(R) = H²R³/(2G) = (4π/3)R³ρ_tot, by the Friedmann constraint. On R_A, E_MS = R_A/(2G).
- □_h R = −(ä/a + H²)R = −(2H² + Ḣ)R, so κ(R) = −(H² + Ḣ/2)R. On R_A, κ = −H(1 − ε/2), and
  |κ|/2π = T_A of GR:56.

**1.3 The value of each candidate's functional against E_MS [W].**

- R1: S·(H/2π) = (πR_A²/G)/(2πR_A) = R_A/(2G) = E_MS(R_A), for every H(t). The value of R1 is the
  Misner–Sharp mass inside R_A exactly (G3-HOM 2.1 identified the identity; the point added here is
  that it holds with no reference to the temperature label H/2π).
- R2: S·T_A = (R_A/2G)(1 − ε/2) = E_MS(R_A)(1 − ε/2), and
  E_MS − S·T_A = (ε/2)E_MS = (3/4)(ρ_tot + p_tot)V_A. So S·T_A is the Kodama charge only when
  ρ + p = 0, that is on exact de Sitter.
- R3: S·(1/2πR_E) = R_E/(2G), and E_MS(R_E) = H²R_E³/(2G), so
  S·T/E_MS(R_E) = 1/(HR_E)² = Ω_de. The attributed energy is the fraction Ω_de of the Kodama charge
  inside R_E, which restates R3's definition.

**1.4 Under κ = κ_KH the first-law energy off de Sitter is not a state function of the area [W].** Hayward's
unified first law projected along the trapping horizon reads (κ/8πG) dA = dE_MS − W dV with
W = (ρ − p)/2 and κ < 0 for this horizon. In flat FLRW, per unit time:

- (κ/8πG)Ȧ_A = −H(1 − ε/2)·8πR_AṘ_A/(8πG) = −ε(1 − ε/2)/G;
- Ė_MS = ε/(2G) and W V̇_A = ((ρ − p)/2)·4πR_A²ε = (3ε − ε²)/(2G), using
  ρ − p = (3H²/8πG)(2 − 2ε/3).

Both sides equal −ε(1 − ε/2)/G. The law is an identity of the Friedmann equations (as Akbar and
Cai, PRD 75, 084003 (2007), hep-th/0609128, state). The corpus normalization dE = κ dA/(8πG)
(A-FL), read off de Sitter with κ = κ_KH, is therefore the heat dE_MS − W dV, and

  ∫ (|κ|/8πG) dA = (1/G) ∫ (1 − Ṙ_A/2) dR_A

depends on the rate Ṙ_A along the history and not only on its endpoints. No function E(A) satisfies
dE = |κ_KH| dA/(8πG) on all histories. On one exact de Sitter history dR_A = 0, and the integral
vanishes. Taken quasi-statically over the family of de Sitter states from R = 0 to R_A, it is
R_A/G, which is GR:58's shell energy. Under the Cai–Kim temperature 1/(2πR_A) instead,
T dS = dR_A/G, and ∫T dS = R_A/G = 2S·T is a state function of the area off de Sitter, at the cost
of a temperature H/2π that contradicts GR:56's T_A (A-TA). Two corollaries:

- On exact de Sitter the corpus carries two different horizon energies: GR:58's first-law energy
  R/G and GR §7.2's S·T = R/(2G) = E_MS. Only the second is A-KH's conserved charge. (G3-HOM 3.3
  records that λ = 2 fails the exact-de-Sitter control for the attribution; the point added here is
  that the energy H-count uses is the λ = 2 one.)
- E = S·T is not ∫T dS for either temperature law off de Sitter. It is a state function only in the
  Smarr-type form, and that form is the Kodama charge only for R1's value.

**Node 1 verdict.** (a) is MISSING from the corpus. Under A-KH it is the Misner–Sharp mass on R_A,
whose value is R1's [L, W]. NEW: 1.4 (the first-law energy is path-dependent heat off de Sitter, and
H-count's energy is twice the Kodama charge on de Sitter); 1.3 for R2's deficit (3/4)(ρ + p)V.

## 2. Node 2: the temperature on a non-Killing horizon

**2.1 First-law consistency alone does not fix the temperature on R_A [W, L].** Two apparent-horizon
first laws are identities of flat FLRW:

- A-CK: −dE = T dS with −dE = 4πR_A³H(ρ + p)dt, T = 1/(2πR_A) and S = A/(4G). Then
  T dS = Ṙ_A dt/G = ε dt/G, and equality is Ḣ = −4πG(ρ + p), the Raychaudhuri equation (Cai and
  Kim, JHEP 02 (2005) 050, hep-th/0501055).
- A-KH: 1.4, with T = T_A and a work term.

They differ in the split of dE_MS into heat and work, and so in T: H/2π against T_A, a factor
1 − ε/2 (≈ 0.775 today in GR:56's ΛCDM illustration). The literature records the disagreement. Cai, Cao and Hu (CQG 26,
155018 (2009), arXiv:0809.1554) derive a tunnelling temperature for the apparent horizon seen by
Kodama observers. Later papers address the conflicting temperature assignments, for example
arXiv:1411.6547 and arXiv:1502.04235. This record does not settle which one is physical.
ESTABLISHED: both laws are identities. ASSUMED: the choice between them (A-KH or A-CK).

**2.2 Under A-KH's surface-gravity function the surface drops out [W].** Evaluate the λS·T/V family
with T(R) = |κ(R)|/2π = (H² + Ḣ/2)R/(2π) (1.2) on any sphere centred on the observer, on the domain
w_tot ≤ 1/3 where H² + Ḣ/2 ≥ 0:

  ρ = λ·(πR²/G)·(H² + Ḣ/2)R/(2π)·3/(4πR³) = 3λ(H² + Ḣ/2)/(8πG) = λ(ρ_tot − 3p_tot)/4,

independent of R. With λ = 1 (A-dS) this is R2's density on every surface, R_E included. Under the
T = 1/(2πR) law, ρ = 3λ/(8πGR²) depends on the surface, which is what separates R1 from R3.
κ = ½□_h R has the trapping-horizon interpretation only on R_A. Its use off R_A is a formal
extension, labelled as such. It is used here only to show that R3's T = 1/(2πR_E) is not the
Kodama–Hayward scalar at R_E: the two agree only where H²(1 − ε/2)R_E² = 1. ESTABLISHED at this
scope. NEW: within the λS·T/V family the surface is an independent input only under the 1/(2πR)
temperature law.

**2.3 The event horizon carries no Kodama–Hayward first law [W, L].**

- *Not a trapping horizon.* R_E = R_A on an open time interval requires Ṙ_E = HR_E − 1 = 0 and
  Ṙ_A = ε = 0, that is exact de Sitter. Where HR_E > 1 (Li's c = 1 law has HR_E = Ω_de^{−1/2} > 1),
  K is spacelike on R_E, and no Kodama observer is at rest there.
- *The Cai–Kim flux law fails there.* With −dE = 4πR_E³H(ρ + p)dt = −R_E³HḢ dt/G, T = 1/(2πR_E) and
  S = A/(4G), T dS = Ṙ_E dt/G = (HR_E − 1)dt/G. The law holds at t iff f(R_E) = 0, where
  f(R) = HḢR³ + HR − 1. With H, Ḣ fixed at t, f is a nonzero polynomial of degree at most 3, so it
  has at most three roots. Changing a(t′) only for t′ > t + Δ leaves H(t) and Ḣ(t) fixed and moves
  R_E(t) continuously through an interval. So, for each t and each fixed (H(t), Ḣ(t)), the law
  fails for all but at most three values in an interval of R_E(t) values that flat-FLRW histories
  with an event horizon realize. It is not an identity, and imposing it would be a new dynamical premise.
  This reproduces in elementary form the failure Wang, Gong and Abdalla report (PRD 74, 083520
  (2006), gr-qc/0511051). For related event-horizon thermodynamics, see Davies, CQG 5, 1349 (1988).

**Node 2 verdict.** (b) is MISSING natively. On R_A it is fixed only by the choice of A-KH (T_A) or
A-CK (H/2π). On R_E neither construction supplies a first-law temperature. ESTABLISHED: 2.1–2.3 at
their scopes. NEW: 2.2. ELABORATING: 2.3 (a known failure, given a short proof).

## 3. Node 3: the exchange law

Write ρ̇_x + 3H(1 + w_x)ρ_x = −Q and ρ̇_m + 3Hρ_m = Q (A-Q).

**3.1 A-KH supplies none [L].** The Kodama current is conserved for the total T_ab. Any split into
components with exchange Q leaves J conserved, so A-KH neither fixes nor constrains Q. In the
selected completion there is no second component, and the exchange question does not arise.

**3.2 R1 as a component is not rescued by exchange [W].** At λ = 1, ρ_x = 3H²/(8πG) = ρ_tot forces
ρ_m = 0 for every Q. Hubble-scale holographic models with exchange (Pavón and Zimdahl, PLB 628, 206
(2005), gr-qc/0505020) use a coefficient c² < 1. That fails the exact-de-Sitter control A-dS
(G3-HOM 3.3).

**3.3 R2's dynamics, exactly [W].** R2's density is a function of the total, ρ_x = 3(H² + Ḣ/2)/(8πG)
(2.2). With h = H² and Ḣ = h′/2, Friedmann reads h = m + h + h′/4, so h′ = −4m for every Q.

- *Q = 0.* Then m = m₀a⁻³ and h = (4/3)m₀a⁻³ + C, with C a free integration constant. The
  background is exactly flat ΛCDM, with Λ_eff = 3C undetermined and effective matter (4/3)ρ_m. The
  attributed component is Λ_eff plus a smooth dust equal to ρ_m/3:
  ρ_x = (3/8πG)(C + m/3) and w_x = −C/(C + m/3). This reproduces G3-HOM's
  dΩ/dx = (1 − Ω)(4Ω − 1), with past attractor Ω = 1/4 (w_x = 0) and future attractor Ω = 1, and it
  shows that R2's Λ_eff is an integration constant, as G3-HOM's table records ("not fixed"). R2 is
  the α = 1/2 member of the Ricci-scalar holographic class (Gao, Wu, Chen and Shen, PRD 79, 043511
  (2009), arXiv:0712.1394), since ρ_x = (3/8πG)·½(Ḣ + 2H²).
- *Q ≠ 0.* m′ = −3m + 8πGQ/(3H), and h follows from h′ = −4m. The expansion history depends on Q.

**3.4 R3's w(z) depends on Q continuously [W].** From ρ_x = 3/(8πGR_E²) and Ṙ_E = HR_E − 1,

  w = −1/3 − (2/3)√Ω_de − Q/(3Hρ_x).

For Q = 3b²H(ρ_m + ρ_x) the last term is −b²/Ω_de, the interacting form of Wang, Gong and Abdalla
(PLB 624, 141 (2005), hep-th/0506069). Only Q = 0 (G3-HOM's P-sep) is free of an adjustable
coefficient. A b² chosen to fit is rejected under §A.29.

**3.5 The exact-de-Sitter control constrains the exchange law [W].** A-dS requires exact de Sitter,
with the attributed component alone, to be a solution: ρ_m = 0 and Ḣ = 0. Then ρ̇_m = Q must vanish,
so Q(ρ_m = 0, Ḣ = 0) = 0. This excludes, for R1–R3 read as components, every exchange law that
does not vanish at ρ_m = 0 on de Sitter, for example Q = 3b²Hρ_tot or Q ∝ ρ_x with b ≠ 0. It admits
laws proportional to ρ_m, such as GR:382's Type I example Q = 3νHρ_dm. The control does not fix Q.

**Node 3 verdict.** (c) is MISSING from the corpus and from A-KH and A-CK. It is constrained only by
3.5. ESTABLISHED: 3.2–3.5. NEW: 3.3's exact ΛCDM form of R2 with free Λ_eff, and 3.5.

## 4. Node 4: discrimination under the decision rule

**Under A-KH (one named selection premise, (I)).**

- R1: its value E = R_A/(2G) is E_MS(R_A), the Kodama charge on the trapping horizon, for every
  history (1.3). Consistent. Its label T = H/2π is replaced by T_A (2.1), and E ≠ S·T_A off de
  Sitter. As a separate component it contradicts Ω_B > 0 (G3-HOM 2.1; 3.2), so the consistent
  reading is the total restated. Read with its label T = H/2π, R1 contradicts A-TA and A-KH, and
  this bullet then excludes it too.
- R2: S·T_A ≠ E_MS off de Sitter, with deficit (3/4)(ρ + p)V_A (1.3), and S·T_A ≠ ∫T_A dS (1.4).
  It contradicts A-KH's energy.
- R3: R_E is not the trapping horizon off de Sitter (2.3), T = 1/(2πR_E) is not the Kodama–Hayward
  surface gravity there (2.2), and S·T is not E_MS(R_E) (1.3). It contradicts A-KH's surface and
  temperature.

On R1's value reading, exactly one candidate is consistent. **Selected: R1 in its Misner–Sharp
reading, conditional on A-KH.** On the label reading, none is consistent under A-KH. The selected completion fixes no w(z) and no Λ_eff (G3-HOM 3.2).

**Under A-CK.** R1 is consistent with T = 1/(2πR_A). R3 fails the flux law on R_E (2.3). A-CK
states no energy functional, so it does not decide R2's E = S·T_A. It narrows the field to R1 and R2
but does not select, and this record does not rely on it.

**Without a selection premise.** R2 and R3 each satisfy every listed input (G3-HOM Node 4), and
nothing found here contradicts that. **None selected.** The minimal discriminating input, in the
sense of the decision rule, is the temperature law on a non-Killing horizon, together with the
surface in the T = 1/(2πR) branch only:

- Kodama–Hayward law: every surface gives R2's density (2.2), so R1 and R3, which use 1/(2πR), are
  excluded. Off R_A the law is a formal extension; read as defined on R_A only, it fixes the surface
  too.
- 1/(2πR) law: R2 is excluded, and the surface (R_A or R_E) separates R1 from R3.

The exchange law is not needed to separate the candidates. It is needed to fix w(z) within R2 or
R3 (3.3, 3.4).

**Exact classes excluded under A-KH (negative result).** Fix λ = 1 (A-dS). Attributions
ρ_x = S·T/V of a uniformly spread horizon energy, read as the horizon's first-law energy, are
excluded in flat FLRW on any time interval on which ε ≢ 0, and for the first and third pairs also
ε ≢ 4, when (R, T) is one of:

- (R_A, T_A): S·T_A = E_MS|1 − ε/2|, equal to E_MS iff ε ∈ {0, 4};
- (R_E, 1/(2πR_E)): equality needs HR_E = 1 on the interval, which forces ε = 0 (2.3);
- (R_E, |κ(R_E)|/2π): S·T = E_MS(R_E)|1 − ε/2|, equal to E_MS(R_E) iff ε ∈ {0, 4}.

The survivor is the value (R_A, 1/(2πR_A)), which equals E_MS and gives no component. Three cases
are not excluded, and are outside the class:

- ε ≡ 4 on the interval (w_tot = 5/3, a ∝ t^{1/4}) for (R_A, T_A) and (R_E, |κ(R_E)|/2π), where
  |1 − ε/2| = 1. A-FLRW does not exclude it; it lies outside §2.2's domain w_tot ≤ 1/3.

- λ ≠ 1, which fails A-dS but can equal E_MS off de Sitter: for example λ = 4/3 with T_A on R_A
  on a ∝ t² (constant ε = 1/2), and generally λ(1 − ε/2) = 1 at constant ε = 2(1 − 1/λ).
- "T_A on R_E" read as GR:56's value (H/2π)(1 − ε/2). Equality with E_MS(R_E) is
  HR_E = 1 − ε/2. With Ṙ_E = HR_E − 1 this holds on an interval iff ε̇ = Hε(3 − ε), which has
  solutions with ε ≠ 0, and the future expansion can be chosen to realize them (the freedom used in
  2.3).

Unconditionally (A-FLRW only): the Cai–Kim flux first
law with T = 1/(2πR_E) and S = A/(4G) on the event horizon is not an identity of flat FLRW (2.3).
Under A-dS: exchange laws with Q ≠ 0 at ρ_m = 0 on de Sitter (3.5). These are not exclusions of
R2 or R3 as phenomenological dark-energy models, which A-KH does not address, nor of attributions
outside the λS·T/V family or beyond spherical symmetry.

**Skeptical pass on the selection (§A.31).** The selection was pressed on five points.

- *Uniqueness of the energy.* Misner–Sharp is unique as the Kodama charge. Other quasi-local
  energies exist, such as Brown–York, which needs a reference embedding, and Padmanabhan's
  Komar-type 2S·T (Padmanabhan, Rep. Prog. Phys. 73, 046901 (2010), arXiv:0911.5004). Under the
  Komar reading at constant w:
  - 2S·T_A = (ρ − 3p)V/2 equals |ρ + 3p|V at w = −1 and w = −1/9;
  - 2S·(H/2π) = 2ρV equals it at w = −1 and w = 1/3.

  With the signed Komar energy (ρ + 3p)V, w = −1 is not a root, since ρ + 3p = −2ρ there; the
  roots are w = −1/9 and w = 1/3 respectively. So the equipartition reading is an identity on
  these constant-w (power-law) backgrounds, and in its absolute-value form also on de Sitter. It
  is not an identity of flat FLRW. It is a condition on the total (ρ, p), G3-HOM's R6, and attributes no separate
  component on any background, so it does not revive R2 or R3 as attributions. The selection
  remains conditional on A-KH's choice of the Kodama charge.
- *Spherical symmetry.* A-KH needs it. The homogeneous sector about one observer has it. The
  selection says nothing about inhomogeneous cuts.
- *Agreement with G3-HOM's exclusion of R1 from the counterexample pair.* G3-HOM excluded R1 for its
  temperature label H/2π. Here the label is dropped and the value survives as E_MS. The two records
  agree.
- *Not a native derivation.* GR:56 states that the Kodama–Hayward extension is not established. The
  selection is reported as conditional, and A-KH is not adopted.
- *Not favourable to a dark-energy prediction.* The selected completion has no dynamics. It
  relocates the question to the native source rather than answering it.

## 5. Node 5: consistency with W1-0 and G3-W1

- **G3-W1 [W].** E_MS is a function of the emergent metric, and its conservation is the Bianchi
  identity of the emergent geometry. It is not an additive function of substratum configurations, so
  it lies in none of G3-W1's 47 excluded classes (G3-W1 §4), and nothing here conflicts with them.
- **W1-0 [W].** The selection does not supply W1-0. G3-HOM's statement that a native conserved
  energy–momentum on a non-stationary cut would replace the horizon attribution stands.
- **GR:58 off de Sitter (assumption-watch marker) [W].** The counting derivation
  T_micro = (∂s_H/∂E)⁻¹ treats E as a state variable on a conserved shell, with E the horizon
  first-law energy. By 1.4 that energy is path-dependent heat off de Sitter under A-KH, and the
  Kodama charge E_MS is not it (it is half of it on de Sitter). The ratio of rates along a history
  gives T = ε²|κ|/(8πGσ) formally, but the microcanonical step needs Ω_H(E) as a function of E. So
  under A-KH the off-de-Sitter extension of T_cl = T_micro needs a state-function energy that
  neither the corpus nor A-KH supplies. The A-CK branch supplies one, E = ∫T dS = R_A/G (1.4), but
  only with the temperature H/2π, which contradicts GR:56's T_A (A-TA). A consistent extension
  therefore needs either a reason to set A-TA aside or a native state-function energy: W1-0, or a conserved quantity outside G3-W1's classes (G3-W1 §4, "not
  excluded"), for example a coarse-grained one. MISSING. This marker bears on every off-de-Sitter use
  of the calibration, including a₀ = cH/6 off de Sitter (G3-HOM 3.4).
- **Partition against count (assumption-watch marker).** Off de Sitter, H-count's boundary count
  (A-AREA, apparent horizon) and the causal partition (A-PART, event horizon) are different surfaces
  (GR:56). The A-KH selection places the thermodynamics on the count's surface, not the partition's.
  An extension of H-count off de Sitter therefore needs a statement of which hidden sector the count
  belongs to. MISSING.

## 6. Classification and stop

**ESTABLISHED.** 1.2–1.4, 2.1–2.3, 3.2–3.5 and §4's conditional selection, at their stated scopes,
by [W] derivation with the [L] inputs cited.

**ASSUMED.** A-FLRW, A-FL, A-dS, A-AREA and A-TA as inputs; A-KH for the selection; A-CK and A-Q
where used.

**MISSING.**
- A native off-de-Sitter energy functional and its surface (GR:56).
- A native temperature law on a non-Killing horizon, including the extension of GR:58's counting
  derivation (§5).
- A native exchange law (GR:382 leaves Type I and Type II open).
- A native reason to prefer A-KH over the event-horizon partition of GR:40.
- W1-0.

**Findings (§A.31).**
- NEW: 1.4, 2.2, 3.3 (the exact ΛCDM form of R2) and 3.5, and §4's conditional selection with its
  excluded classes.
- ELABORATING: 1.3, 2.1, 2.3 and the §5 markers.
- CONFIRMING: 1.1 and 3.1.

**Findings for routing (no edits made).**
- GR:58 and GR §7.2 use different horizon energies on de Sitter, R/G and R/(2G). Only the second is
  the Kodama charge (1.4). This is consistent as stated, because §7.2 defers sourcing, but any
  off-de-Sitter use of either has to name which.
- G3-HOM's description of R2 as a "w = 0 tracker" is its past limit. Its background is exactly ΛCDM
  with free Λ_eff and matter rescaled by 4/3 (3.3).

**Stop.** The first stop condition is reached: the question is answered under the decision rule.
One depth-first pass was made. A fixed point is not claimed. No branch needed a computation.

## References and their role (§A.42 item 8)

| Reference | Classification |
|---|---|
| #1169 c.7076731666; #873 | Governance and planning provenance |
| G3-HOM, G3-W1 and G3-CF records; GR and Structure lines at `D` | Support on `main` at `D` |
| Kodama (1980); Misner–Sharp (1964); Hayward (1996, 1998); Hayward–Mukohyama–Ashworth (gr-qc/9810006); Akbar–Cai (2007); Cai–Kim (2005) | Standard results quoted [L] for A-KH and A-CK; the FLRW evaluations are re-derived here |
| Cai–Cao–Hu (2009); arXiv:1411.6547; arXiv:1502.04235 | Literature on the apparent-horizon temperature; cited for the existence of the disagreement only |
| Wang–Gong–Abdalla (PRD 2006; PLB 2005); Davies (1988); Pavón–Zimdahl (2005); Gao–Wu–Chen–Shen (2009); Li (2004), hep-th/0403127; Hsu, PLB 594, 13 (2004), hep-th/0403052; Padmanabhan, Rep. Prog. Phys. 73, 046901 (2010), arXiv:0911.5004 | Literature on event-horizon thermodynamics and holographic models; each use is stated where it is made, and the formulas used are re-derived here |

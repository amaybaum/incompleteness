# G3-TEMP: the temperature law on a non-Killing horizon

**Standing.** Author record of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). WIP / UNVERIFIED. Independent non-author review at `16f1a7f6`: REVISE (minor), relayed by
the coordinating session and not posted on GitHub, since the write halt covers comments. This
revision answers its findings 1–5 and nits 6–8. The preregistration `PLAN.md` (commit
`666708b0`) was pushed before this record and is unchanged. Authorization, snapshot `D`, sources,
assumption IDs, decision rule, productivity test, stop conditions and goal link are as in
`PLAN.md`. The unit adopts no premise, runs no computation, and edits no manuscript, Lean module,
registry or shared record.

**Labels.** ESTABLISHED: derived on paper here [W], or a quoted standard result [L], or a source
fact [S], at the stated scope. ASSUMED: a premise of the `PLAN.md` table, or a hypothesis named
here and not adopted. MISSING: supplied neither by the corpus nor by this unit. [W] derivations are
not independently reviewed and not kernel-checked. Estimates are marked as such.

**Notation.** c = k_B = 1; ħ is kept, because it is the calibrated quantity, and G is kept. Flat FLRW (I-FLRW), Hubble rate H, ε ≡ −Ḣ/H², apparent horizon R_A = 1/H (Ṙ_A = ε),
event horizon R_E (Ṙ_E = HR_E − 1), A = 4πR². The boundary entropy density is η = σ/ϵ² (GR §3.1,
ϵ the discreteness scale of the count), so the count is s = ηA. The exact-de-Sitter calibration
gives ħ = 1/(4Gη) (GR:78). T_A ≡ (ħH/2π)|1 − ε/2| is the Kodama–Hayward value quoted at GR:56.
R1, R2, R3 are G3-HOM's completions as in G3-OFFDS.

***

## 0. Verdict

**Bare construction (N-OBS + N-TRACE), the unconditional verdict: INCONCLUSIVE, with one class
excluded.** The substratum triple (S, φ, V), the partition and the trace-out fix no temperature
law, on a Killing horizon or off one. Every finite family of visible rate ratios, thermal at T_A,
thermal at ħ/(2πR), or thermal at no temperature, has a finite reversible realization (GR:76; Main
§1.3, theorem statement item (3); Main §3.4, intervention dilation, Main:490), and the bare permutation does not fix the frequency gaps that a rate-ratio law is
stated in (GR:84). Excluded: every temperature law claimed to follow from N-OBS + N-TRACE alone,
that is, to hold on every finite reversible realization (§2). This excludes no law for the
specific substratum rule, which is a different and open question.

**The missing native ingredient, named exactly.** A native conserved shell energy for the hidden
sector at a non-Killing horizon (W1-0), together with the dependence of the hidden-sector count on
it off de Sitter: whether that count is a function of the shell energy alone or also of a second
shell variable. §3 shows that this one fact decides between the candidate laws on the counting
route. The dynamical route (H-slope off a Killing horizon) additionally needs the hidden-state
class there (H-spectrum), which GR:144 records as underivable from S1–S4; §4 shows that its κ is
then forced by the counting route under N-UNIV, so it adds no independent selection.

**Under the named hypothesis H-COUNT-1 (§3; not adopted), derived and excluded.** If H-count holds
on non-de-Sitter states with one history-independent count s_H(E) of the shell energy alone, then,
with the exact-de-Sitter first law and calibration at every radius,

  T = 1/(8πGηR) = ħ/(2πR) on the counted surface, on every admissible state,

where the ħ form carries the calibration conditions of GR:88 (§3.2), and the Kodama–Hayward T_A, and every law that depends on Ḣ at fixed R, is excluded for that class
on any instant with ε ∉ {0, 4}. With N-AREA (the count is on R_A), T = ħH/2π: the 1/(2πR) branch
on R_A, which by G3-OFFDS §4 selects R1, on its value reading and also on its label reading. Adding
N-SLOPE off de Sitter and N-UNIV, the KMS-side surface gravity is forced to |κ| = 1/R on the counted
surface, and κ = κ_KH is excluded there too (§4.2): the de Sitter states of H-COUNT-1 fix a_* = ħ,
and with κ_KH the action scale would be a_* = ħ/|1 − ε/2| ≠ ħ wherever ε ∉ {0, 4}, about 1.29ħ
today in GR:56's ΛCDM illustration.

**Exposed assumption.** GR:56 states that extending the calibration off de Sitter "would require a
Kodama–Hayward treatment showing the same factor enters both the classical and emergent thermal
descriptions and cancels". In the class H-COUNT-1 the classical (counting) side carries no factor
(1 − ε/2), so the cancellation cannot occur there. The route GR:56 names is open only if the
hidden-sector count depends on a second shell variable, or if the shell energy is not a function of
the count (§3.3).

| Premise set | Temperature on a non-Killing horizon | Outcome |
|---|---|---|
| N-OBS + N-TRACE (bare) | Not fixed; every finite rate-ratio family realizable | INCONCLUSIVE; class of bare derivations excluded |
| + N-FL | T_cl = ε-independent multiple of κ, κ an input | Not fixed |
| + H-COUNT-1 (+ N-dS, N-FL at every radius, N-UNIV) | ħ/(2πR) on the counted surface | Derived (conditional); T_A excluded in the class |
| + N-AREA | ħH/2π on R_A | Derived (conditional); selects R1 via G3-OFFDS §4 |
| + N-SLOPE off de Sitter, N-UNIV | KMS-side \|κ\| = 1/R on the counted surface | Derived (conditional); κ_KH excluded in the class |
| Count with a second shell variable X | Not fixed; T_A reachable | INCONCLUSIVE |

**Productivity test (§A.31): met.** (i) T_A is excluded for the stated class H-COUNT-1 (§3.2,
§4.2); (ii) the bare construction is shown unable to supply any law (§2); (iii) GR:56's
cancellation route is shown to need a second shell variable or a non-state-function shell energy
(§3.3), and Sub:393's "temperature determined by the partition geometry" holds on the exact-de-Sitter
calibration only (§1.2).

***

## 1. Node 1: native objects that carry a temperature

**1.1 Inventory [S].**

- *N-OBS, N-TRACE.* Main §1.2 gives a discrete tick, x_t = φ^t(x_0), a finite visible sector and a
  partition. Main §1.4 gives the reduced law T(φ, P, μ_H). Neither contains a metric, a surface
  gravity or a temperature.
- *N-FL.* GR §3.1: dE = κ dA/(8πG) and dS = η dA give T_cl = κ/(8πGη). This is linear in κ, and κ
  is an input taken from the supplied geometry. On a Killing horizon κ is the Killing surface
  gravity; off one, GR:56 states that no Killing vector exists and that the extension is not
  established.
- *N-COUNT.* GR:58: T_micro = (∂s_H/∂E)⁻¹ under H-count, with E the horizon first-law energy, on
  a conserved energy shell; on the exact-de-Sitter calibration E = R/G.
- *N-SLOPE.* GR:74–78: the observer's infrared detailed-balance slope equals τ_K = 2π/κ, and
  ħ = a_* = τ_K/β_E. GR:144: "the KMS temperature parameter is fixed kinematically by κ; whether
  the emergent state belongs to that KMS class is state-dependent, and which class it occupies is
  H-spectrum, which §2 records as underivable from S1–S4".
- *N-FRAME.* The preferred foliation is the comoving one (GR:470).

**1.2 Verdict.** N-FL and N-SLOPE are linear in an unspecified κ off a Killing horizon. Only
N-COUNT's definition T = (∂s_H/∂E)⁻¹ is free of κ, and it stays free of κ only when the shell
energy E is a state variable specified without κ, as in H-COUNT-1 (a) (§3.1). GR:58 takes E to be
the first-law energy, dE = κ dA/(8πG), so κ re-enters through E off de Sitter (G3-OFFDS 1.4).
ESTABLISHED [S]. Routing finding
(no edit): Sub:393 states that the trace-out projects onto "classical horizon thermodynamics …
with the metric, the surface gravity, the entropy, and the temperature determined by the partition
geometry". The partition of GR:40 is the event horizon, which off de Sitter is not a Killing
horizon and carries no Kodama–Hayward first law (G3-OFFDS 2.3); the statement holds on the GR:56
calibration and not off it. CONFIRMING (1.1); ELABORATING (the Sub:393 scope).

## 2. Node 2: the bare construction fixes no temperature law

**2.1 Every finite rate-ratio family is realizable [S, W].** Main §1.3, theorem statement item (3)
(reverse finite realization), and Main §3.4's intervention-dilation theorem (Main:490, the finite
classical action-labelled comb; cited at GR:76) realize every finite action-labelled conditional
family with one finite reversible dynamics, a fixed hidden prior and permutation interventions.
Here μ_H ranges over fixed hidden priors, which are realization data (Main §1.2, Remark *the
measure as a realization datum*); the theorems construct the prior. Whether the same families are
realizable under Lemma 3's counting prior is not decided here, and that case stays outside the
class of 2.3. GR:76 applies this to a two-gap probe that is thermal at no common
temperature. The same construction realizes, on any finite probe window, a family thermal at
T_A(t), one thermal at ħ/(2πR(t)), and one thermal at neither. A constraint satisfied on every
finite reversible realization is therefore satisfied by all three, so it selects none of them.

**2.2 The frequency variable is not fixed either [S].** GR:84: U_φ = e^{−iΩ} has a non-unique
Hermitian logarithm, ω_a = θ_a + 2πn_a, so the bare permutation does not determine the frequency
gaps that a rate ratio R(ω) and its slope are stated in. A temperature law needs both a rate-ratio
law and a normalized time generator, and the bare construction supplies neither.

**2.3 Excluded class (negative result).** Every temperature law, on a Killing or non-Killing
horizon, offered as a consequence of N-OBS + N-TRACE alone, that is, as a property of every finite
reversible realization (φ, partition, μ_H), μ_H ranging over fixed hidden priors, with its visible
rate ratios. Not excluded: a law that holds for the specific substratum rule and partition, or for
every realization under the counting prior selected by Lemma 3 (2.1);
that is H-spectrum for the actual realization, which GR:144 records as open and which no paper
argument in this unit decides (stop condition: it would need the rule's spectral data).

**Node 2 verdict.** ESTABLISHED at the stated scope. NEW: the excluded class is stated for the
non-Killing case, where G3-OFFDS recorded the law only as MISSING. The native ingredient left open
by this node is the hidden-state class of the actual realization at the horizon, with a native
frequency normalization. MISSING.

## 3. Node 3: the counting route off de Sitter

**3.1 The hypothesis [ASSUMED, named, not adopted].** H-COUNT-1, an extension of N-COUNT to flat-FLRW
states with Ḣ ≠ 0:

- (a) the shell energy E of the hidden sector at the horizon is defined on every admissible state,
  and the hidden sector's energy-dependent entropy is one history-independent, strictly increasing
  function s_H(E) of E alone (positive temperature);
- (b) s_H(E) = ηA + const on every admissible state, A the counted area, η fixed;
- (c) the admissible states include exact de Sitter of every radius R > 0, with the first law of
  N-FL at κ = 1/R (N-dS), and the calibration ħ = 1/(4Gη) is the same for all of them (N-UNIV,
  GR:56 "does not depend on which de Sitter H calibrates it").

GR:58 states H-count without restricting it to de Sitter and evaluates it on the exact-de-Sitter
calibration (`PLAN.md`'s N-COUNT row describes it as stated on exact de Sitter; the source line
carries no such restriction). Its application to non-de-Sitter states, and the one-variable form (a), are not
stated in the corpus. H-COUNT-1 also requires a conserved shell, which is W1-0 (Node 5).

**3.2 Derivation [W].** By (a) and (b), A = (s_H(E) − const)/η is a strictly increasing function
of E, so E = E(A) is a function of the counted area alone, on every admissible state. By (c), on
the de Sitter state of radius R, dE/dA = κ/(8πG) = 1/(8πGR). Every R > 0 is the radius of some de
Sitter state, and E(A) is one function, so dE/dR = (dE/dA)(8πR) = 1/G for every R:

  E = R/G + E_0.

This is GR:58's E = c⁴R/G, now on every admissible state. Then

  T = (∂s_H/∂E)⁻¹ = (dE/dA)/η = 1/(8πGηR) = ħ/(2πR),

using ħ = 1/(4Gη). The form free of ħ is T = 1/(8πGηR). The ħ form uses the exact-de-Sitter
calibration, which carries GR:88's conditions: H-count, H-slope on identified transitions, H-frame,
the H-Hawking horizon and frame conditions, local boost structure and the symmetric detailed-balance
rate ratio. The exclusion of 3.3 does not need them, since it uses only T ∝ 1/R at fixed η and
compares states of the same radius; 4.2 does need them. The temperature depends on the counted
radius only. On a non-de-Sitter state it
equals the de Sitter temperature at the same counted radius.

**3.3 What it excludes, and what it leaves [W].**

- *Excluded class.* Within H-COUNT-1 on I-FLRW, every temperature law that at fixed counted radius
  depends on Ḣ. The counting temperature is the same, 1/(8πGηR), on every admissible state of
  counted radius R, the de Sitter state of (c) included. T_A on R_A takes the values
  (ħ/2πR_A)|1 − ε/2|, which differ between two admissible states of the same R_A whose values of
  |1 − ε/2| differ; one of them may be taken to be the de Sitter state, where |1 − ε/2| = 1. So T_A
  cannot equal the counting temperature on both, which excludes T_A on every state with ε ∉ {0, 4}.
  With the calibration, T_A/(ħH/2π) = |1 − ε/2|. (ε ≡ 4, w_tot = 5/3, is outside the exclusion, as
  in G3-OFFDS §4.) The Kodama–Hayward law read on R_E, |κ(R_E)|/2π = (ħ/2π)|H² + Ḣ/2|R_E, is
  excluded on R_E for the same reason wherever it differs from ħ/(2πR_E).
- *Cai–Kim comparison (I-CK, labelled).* On R_A, with T = ħ/(2πR_A) and S = ηA, η = 1/(4Għ),
  T dS = (ħ/2πR_A)·(8πR_A dR_A)/(4Għ) = dR_A/G = dE. The change of E is
  dE/dt = ε/G, and the flux of total energy through R_A, 4πR_A³H(ρ + p) with
  ρ + p = εH²/(4πG), is also ε/G. So E changes by exactly the Cai–Kim flux (G3-OFFDS 2.1). This is
  an identity of I-FLRW; it does not show that E belongs to a conserved shell.
- *Exposed assumption (GR:56).* For T_A to arise as a counting temperature, (∂s_H/∂E) must carry
  the factor (1 − ε/2). Under (a) and (b) it cannot, since T is a function of A alone. Two ways out
  remain, both outside H-COUNT-1: a count s_H(E, X) depending on a second shell variable X, with T
  = (∂s_H/∂E)_X⁻¹ able to depend on X; or a shell energy that is not a function of the count, which
  G3-OFFDS 1.4 shows is what dE = |κ_KH| dA/(8πG) gives (path-dependent heat). On a sphere V is a
  function of A, so X cannot be the volume of Hayward's work term W dV; it would have to be a
  further conserved variable of the hidden sector. Neither is in the corpus. MISSING.
- *Surface.* The derivation fixes T as a function of the counted radius and leaves the counted
  surface to N-AREA (R_A, GR:56) or N-PART (R_E, GR:40). By G3-OFFDS §4, under the 1/(2πR) law,
  R2 is excluded and the surface separates R1 (R_A) from R3 (R_E).

**3.4 Skeptical pass (§A.31; the branch gives a definite law).**

- *(a) carries the result.* Relaxing it to s_H(E, X) removes the exclusion (3.3). The excluded
  class is stated with (a) for that reason.
- *Positivity.* A non-monotone s_H would make A(E) many-valued; T < 0 branches are outside the
  class, as at GR:58.
- *Constant η and ħ.* (c) uses GR:56's statement that the calibration is the same for every de
  Sitter H. If η varied between states the derivation would not go through; GR:58 treats η as fixed.
- *Conserved shell.* GR:58's microcanonical step needs a conserved energy shell. Off de Sitter the
  horizon energy E = R_A/G changes in time (3.3), so the conserved quantity must be the shell's
  total, not E alone; which total is conserved is W1-0, not supplied. The derivation is therefore
  conditional on H-COUNT-1 including that conserved shell, and is not a native derivation.
- *Not favourable to a dark-energy prediction.* With N-AREA the law selects R1, which has no
  dynamics and attributes no separate component (G3-HOM 2.1; G3-OFFDS 3.2). It relocates the
  vacuum-energy question to the native source as the A-KH branch of G3-OFFDS does.

**Node 3 verdict.** ESTABLISHED [W]: 3.2 and 3.3 under H-COUNT-1. ASSUMED: H-COUNT-1. MISSING: the
conserved shell energy (W1-0) and whether the hidden-sector count depends on a second shell
variable. NEW: 3.2, 3.3's exclusion and exposed assumption.

## 4. Node 4: the dynamical route off a Killing horizon

**4.1 What fixes τ_K [S, W, L].** τ_K = 2π/κ needs a vector field and its normalization (GR:144).

- *Normalization from N-FRAME [W].* In flat FLRW with comoving radius r, the Kodama vector is
  K = ∂_t − Hr∂_r (it preserves R = ar: ȧr − Hra = 0), with K·K = −(1 − H²R²). On the observer's
  worldline R = 0 it equals the comoving four-velocity. So N-FRAME, with normalization on the
  observer's worldline, fixes the same normalization as I-KH. It does not fix which definition of
  surface gravity applies to a non-Killing vector.
- *Definitions disagree off Killing horizons [L].* Several inequivalent definitions of dynamical
  surface gravity exist and agree on Killing horizons: Hayward's trapping-horizon κ = ½□_h R
  (Hayward, CQG 15, 3147 (1998), gr-qc/9710089), the definition of Fodor, Nakamura, Oshiro and
  Tomimatsu (PRD 54, 3882 (1996), gr-qc/9603034), and those compared by Nielsen and Visser (CQG 23,
  4637 (2006), gr-qc/0510083) and by Pielahn, Kunstatter and Nielsen (PRD 84, 104008 (2011),
  arXiv:1103.0750), who find that they converge to the Killing value at different rates in
  collapse. On isolated and dynamical horizons the normalization of the null generator, and hence
  κ, is not fixed by the horizon geometry alone (Ashtekar and Krishnan, Living Rev. Relativ. 7, 10
  (2004), gr-qc/0407042). This record does not evaluate each definition in FLRW.
- *Field-theoretic temperatures (I-QFT, comparison only) [L].* A tunnelling calculation for Kodama
  observers gives T_A at the FLRW apparent horizon (Cai, Cao and Hu, CQG 26, 155018 (2009),
  arXiv:0809.1554). For evolving horizons, a Hawking-like flux with a slowly varying temperature
  follows under an adiabatic condition on the geometry (Barceló, Liberati, Sonego and Visser, JHEP
  02 (2011) 003, arXiv:1011.5911; the minimal conditions in PRD 83, 041501 (2011),
  arXiv:1011.5593). Jacobson's local-horizon derivation uses an approximate local Killing vector
  and equilibrium at a point (PRL 75, 1260 (1995), gr-qc/9504004). These results presuppose a
  quantum field, a state and a detector model, which are the emergent description, not native
  inputs.
- *Order of the discrepancy [W, estimate].* On R_A the fractional rate of change of κ ∝ H per
  Hubble time is |Ḣ|/H² = ε, up to O(ε̇/H) terms. T_A and ħH/2π differ by the fraction ε/2. The two
  candidate laws therefore differ at first order in the adiabatic parameter, the order at which a
  temperature defined only as the leading term of an adiabatic expansion is not fixed. An
  infrared slope at ω ≲ H needs an accessible window of order 1/H or longer, over which H changes
  by a fraction of order ε. This is an order-of-magnitude statement about the observer interface,
  not a theorem.

**4.2 Consistency of the gap equation off de Sitter [W].** Suppose H-COUNT-1 (so β_E = ∂s_H/∂E =
8πGηR, 3.2) and N-SLOPE on the same transitions with τ_K = 2π/|κ| for some κ on the counted
surface. Then

  a_* = τ_K/β_E = 2π/(|κ|·8πGηR) = ħ/(|κ|R).

H-COUNT-1 (c) places the de Sitter states, on which |κ|R = 1 and a_* = ħ, in the admissible class,
so N-UNIV (a_* universal, GR:78) requires a_* = ħ on every admissible state, that is |κ| = 1/R. For
κ = κ_KH on R_A, |κ|R_A = |1 − ε/2|, so a_* = ħ/|1 − ε/2|, which differs from ħ at every instant with
ε ∉ {0, 4}. On a power-law epoch ε is constant and so is a_*, at a value other than ħ: 4ħ in matter
domination (ε = 3/2); in radiation (ε = 2) κ_KH = 0 and there is no KMS period. At GR:56's ΛCDM
value 1 − ε/2 ≈ 0.775 it is about 1.29ħ. Excluded class: within H-COUNT-1 with
N-SLOPE and N-UNIV, every KMS-side surface gravity other than 1/R on the counted surface, κ_KH
included. This is the explicit form of GR:56's requirement that "the same factor enters both … and
cancels": in H-COUNT-1 the factor does not enter the counting side, so universality forces it out
of the KMS side.

**4.3 Without H-COUNT-1 [W].** If the count depends on a second shell variable X (3.3), β_E can
carry a factor that cancels κ_KH's, and a_* can be universal with κ = κ_KH. The dynamical route
then needs H-spectrum off the Killing horizon to fix κ, which GR:144 records as underivable from
S1–S4. INCONCLUSIVE.

**Node 4 verdict.** ESTABLISHED: 4.1's normalization and literature facts at their scopes; 4.2
under H-COUNT-1 + N-SLOPE + N-UNIV. MISSING: H-spectrum at a non-Killing horizon and a native
choice among the definitions of dynamical surface gravity. NEW: 4.2. ELABORATING: 4.1.

## 5. Node 5: consistency with G3-OFFDS, G3-HOM, G3-W1 and W1-0

- **G3-OFFDS.** Its no-premise branch named the temperature law, and the surface in the 1/(2πR)
  branch only, as the minimal discriminating input. This record leaves that input undetermined
  natively (Node 2) and fixes it under H-COUNT-1 (Node 3). Its A-KH branch (T_A, Misner–Sharp mass)
  and the H-COUNT-1 branch (ħ/(2πR)) disagree on the temperature and agree on R1's value:
  S·T = ηA·ħH/2π = R_A/(2G) = E_MS(R_A). Both relocate the
  vacuum-energy question to the native source. G3-OFFDS 1.4 derives a state-function energy,
  ∫T dS = R_A/G, from the 1/(2πR_A) temperature; 3.2 derives that temperature from a state-function
  energy under H-COUNT-1. On R_A these are converse directions, and neither result supplies the
  other (§A.34).
- **G3-HOM.** Unchanged: R1–R3 and its counterexample stand without a premise. H-COUNT-1 is a named
  hypothesis that would select R1 under N-AREA and R3 under a count on R_E.
- **G3-W1 (47 excluded classes).** H-COUNT-1 needs a conserved shell energy, and the T_A route
  needs, in addition, a second conserved shell variable (3.3). Each would be a conserved real
  quantity of the substratum. G3-W1 excludes nontrivial conserved additive quantities in its 47
  classes (G3-W1 §4), so any such quantity lies outside them: non-additive, of wider support or
  higher degree than its classes, outside their residue windows, or approximate or adiabatic
  (G3-W1 §4, "not excluded"). Nothing here asserts that such a quantity exists, so nothing conflicts
  with G3-W1.
- **W1-0.** Unchanged and open (G3-HOM Node 1, "narrowed, not closed"). This record makes the
  native temperature law on the counting route depend on W1-0 explicitly, together with the
  one-variable question of 3.3.

## 6. Classification and stop

**ESTABLISHED.** 1.2 [S]; 2.1–2.3 [S, W]; 3.2–3.3 [W] under H-COUNT-1; 4.1 [S, W, L] at its scope;
4.2 [W] under H-COUNT-1 + N-SLOPE + N-UNIV.

**ASSUMED.** N-OBS, N-TRACE, N-FL, N-COUNT, N-SLOPE, N-FRAME, N-UNIV, N-dS, N-AREA, N-PART at their
corpus status; I-FLRW; the named hypothesis H-COUNT-1 (§3.1), not adopted. I-KH, I-CK and I-QFT
are used only as labelled comparisons.

**MISSING.**
- A native conserved shell energy for the hidden sector at a non-Killing horizon (W1-0).
- Whether the hidden-sector count off de Sitter depends on the shell energy alone (giving
  ħ/(2πR)) or on a further conserved shell variable (leaving T_A possible).
- H-spectrum at a non-Killing horizon for the actual realization, with a native frequency
  normalization and a native choice among the definitions of dynamical surface gravity.
- A native choice of counted surface off de Sitter (N-AREA against N-PART; G3-OFFDS §5).

**Outcome under the decision rule.** Bare construction: INCONCLUSIVE, naming the missing native
ingredient above, with the class of bare derivations excluded (2.3). Under H-COUNT-1 with N-dS, N-FL
and N-UNIV: derived, T = ħ/(2πR) on the counted surface, and T_A excluded for that class (3.3);
with N-SLOPE added, κ_KH excluded on the KMS side for that class (4.2). Under a count with a second
shell variable: INCONCLUSIVE.

**Findings (§A.31).**
- NEW: 2.3's excluded class; 3.2 and 3.3 (the counting law, its exclusion of T_A, and the exposed
  assumption behind GR:56's cancellation route); 4.2.
- ELABORATING: 4.1; the Sub:393 scope (1.2); the Cai–Kim flux identity in 3.3.
- CONFIRMING: 1.1; Node 5.

**Findings for routing (no edits made).**
- GR:56's route for extending the calibration needs the factor (1 − ε/2) on the counting side,
  which a hidden-sector count that is a function of the shell energy alone cannot carry (3.3, 4.2).
- Sub:393's statement that the partition geometry determines the surface gravity and temperature
  holds on the exact-de-Sitter calibration only (1.2).
- GR:56 quotes T_A, and the counting derivative of GR:58 extended as in H-COUNT-1 gives ħH/2π on
  R_A. Any off-de-Sitter use of either has to name which (as G3-OFFDS records for the two horizon
  energies).

**Stop.** The first stop condition is reached: the question is answered under the decision rule
for the bare construction and for each premise set examined. One depth-first pass was made; a fixed
point is not claimed. The branch that would decide H-spectrum for the actual rule stops at the
second stop condition (it needs the rule's spectral data). No premise was adopted. There is no
successor round.

## References and their role (§A.42 item 8)

| Reference | Classification |
|---|---|
| #1169 c.7078857457, c.7076910606; #873 | Governance and planning provenance |
| G3-OFFDS at `9b84dbe9` (branch `research/g3-offds-20261122`), with #1545 c.7076925155, c.7076975935, c.7076996839 | Support off `main`: G3-OFFDS 1.4, 2.1, 2.3, 3.2 and §4 are used, and that record is on its branch only, accepted as a completed research record (#1169 c.7077211553). This record's results inherit that status |
| G3-HOM, G3-W1 records; GR, Main, Substratum lines at `D` | Support on `main` at `D` |
| Kodama (1980); Hayward (1998); Cai–Kim (2005); Cai–Cao–Hu (2009) | Standard results quoted [L] for I-KH, I-CK and I-QFT comparisons; as cited in G3-OFFDS |
| Fodor–Nakamura–Oshiro–Tomimatsu (1996); Nielsen–Visser (2006); Pielahn–Kunstatter–Nielsen (2011); Ashtekar–Krishnan (2004) | Literature on dynamical surface gravity; cited for the existence of inequivalent definitions and the normalization freedom only |
| Barceló–Liberati–Sonego–Visser (2011, two papers); Jacobson (1995) | Literature on Hawking-like temperatures of evolving and local horizons; cited for the adiabatic or local-equilibrium scope of their temperatures only |

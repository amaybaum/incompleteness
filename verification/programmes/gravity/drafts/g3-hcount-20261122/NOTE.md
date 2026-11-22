# G3-HCOUNT: H-COUNT-1 against the native dynamics

**Standing.** Author record of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). WIP / UNVERIFIED: no independent non-author review yet. The preregistration `PLAN.md`
(commit `b04cf7e5`) was committed before this record and is unchanged. Authorization, snapshot `D`,
sources, assumption IDs, decision rule, productivity test, stop conditions and goal link are as in
`PLAN.md`. The unit adopts no premise, H-COUNT-1 included, and edits no manuscript, Lean module,
registry or shared record. Its one computation is the tiny exact check `checks/sublattice_checks.py`
(§11).

**Labels.** ESTABLISHED: derived on paper here [W], a tiny exact check [EC], a quoted standard
result [L], or a source fact [S], at the stated scope. ASSUMED: a premise of the `PLAN.md` table or
a hypothesis named here, not adopted. MISSING: supplied neither by the corpus nor by this unit. [W]
derivations are not independently reviewed and not kernel-checked. Estimates are marked as such.

**Notation.** As in G3-TEMP: c = k_B = 1, η = σ/ϵ², s = ηA, ħ = 1/(4Gη) on the exact-de-Sitter
calibration, ε ≡ −Ḣ/H². |n| = n_1 + n_2 + n_3 for a site n of the cubic lattice. A configuration
at step t is the pair (u, v) = (x(t−1), x(t)). The spacetime sublattices are Λ_0 = {(n, t) : |n| + t
even} and Λ_1 = {(n, t) : |n| + t odd}; the Λ_k-data at step t are the values of u and v at the
points of Λ_k with times t − 1 and t. A density is **parity-pure** if each of its monomials (or,
for a general function, each of its terms) reads values at points of a single Λ_k. For an additive
Φ = Σ_n h(window_n) with a parity-pure density, Φ_k(t) is the sum of the terms supported on Λ_k at
step t, so Φ = Φ_0(t) + Φ_1(t).

***

## 0. Verdict

**H-COUNT-1 is not justified by OI's native dynamics.** Component by component:

| Component of H-COUNT-1 | Verdict | Support |
|---|---|---|
| (a1) a conserved real shell energy E (W1-0) | Open. No native candidate at d = 3; one class G3-W1 left open is reduced to its excluded classes | §2 [W, S] |
| (a2) the count depends on E alone, read at fixed values of all conserved variables | Refuted on a stated class: on checkerboard lattices every conserved additive energy with a parity-pure density has two separately conserved sublattice parts; at RD6 also the mover counts | §3 [W, EC, S] |
| (a2) read as the marginal count over the E-shell | Holds by definition; carries no content | §4.1 [W] |
| (a′3) the realized values of the further conserved variables are slope-typical | Imposed: needs the measure posit T-MEAS and a concavity property of the count that the corpus does not supply, and that H-count's de Sitter form contradicts if inherited by each sublattice part | §4 [W, L] |
| (a3) one function of E across histories | Imposed: needs the partition to enter the count only through E, which the supplied partition does not do off de Sitter | §6 [W, S] |
| (b) s_H = ηA | Imposed (W1, an additional physical assumption per W1-1) | §1 [S] |
| (c) de Sitter family and one calibration | As stated in the corpus (N-dS, N-UNIV) | §1 [S] |

**A further conserved shell variable is required, on the class of §3.** Under N-2ND, N-NN, N-CI
and N-BIP (Main:736 items (xiii), (x), (xi); SM:539) the dynamics is a product of two autonomous
systems, one on each spacetime sublattice; in phase-space form F² is a product map (§3.2). Consequently (§3.4), for every additive energy
with a parity-pure density that is conserved on all configurations, the two sublattice parts E_0,
E_1 are each conserved, and X = E_0 − E_1 is a second conserved shell variable; it is nontrivial on
every shell on which E_0 takes more than one value. This covers SM's quadratic E (conserved modulo q
by the exact linear rule, exactly by its real lift, and exactly as an integer at RD6, G3-HOM 1.2).
No energy of this class is known to be conserved by the rounded d = 3 rule; the statement is
therefore: any resolution of W1-0 by a parity-pure additive energy carries this second variable.

**What the temperature law needs from (a), stated exactly.** By an exact identity (§4.1), the
slope of the marginal E-shell count is the p(X | E)-average of the slopes at fixed X. A further
conserved variable changes the counting temperature only through its realized value. The
temperature of the reachable set is the one-variable value at leading order when the realized
values lie where p(X | E) concentrates and the fixed-X slope there is the marginal one (slope
typicality, §4.1). That condition is the load-bearing content of (a), and it is not native (§4).

**Strengthened conditional law (§5).** G3-TEMP's T = 1/(8πGηR) on the counted surface (ħ/(2πR)
under GR:88's calibration conditions), its exclusion of T_A at fixed counted radius for ε ∉ {0, 4},
and its KMS-side result |κ| = 1/R, follow at leading order from H-COUNT-1′: (a1); the marginal count
s_1(E) is one history-independent strictly increasing function; the realized values of all further
conserved variables are slope-typical at leading order; (b) for s_1; (c). H-COUNT-1′ is implied by
H-COUNT-1 and admits the second variables that §3 proves present. Strengthened, conditionally.

**The T_A route (§7).** A second conserved variable yields T_A only if its realized value labels
the expansion history, with (∂E/∂A)_X = (1 − ε/2)/(8πGR), and is slope-atypical by the fraction
(1 − ε/2)⁻¹ − 1, an entropy deficit of order s under extensivity (estimate). No native candidate
(orbit labels, the sublattice split, the invariants of the exact linear rule, the RD6 movers, the
partition) is linked to ε. MISSING.

**Overall outcome: missing native mechanism, with a proof refuting the fixed-variable reading of
(a2) on the stated class.** The missing native mechanisms are: (M1) a real conserved additive shell
energy for the d = 3 rule (W1-0); (M2) a native reason that the realized values of the further
conserved variables are slope-typical; (M3) a native partition off de Sitter, entering the count
only through E; (M4) the boundary count of the whole hidden sector (W1). For the T_A alternative:
(M5) a conserved variable tied to the expansion history.

**Productivity test (§A.31): met.** (i) the fixed-variable reading of (a2) is refuted on a stated
class from native items (§3); (ii) G3-TEMP's law is derived under the strictly weaker H-COUNT-1′
(§5), and the conditions under which T_A stays reachable are narrowed (§7); (iii) the ambiguity of
(a) between the marginal and the fixed-variable count, and the concavity condition hidden in the
typical-split step, are exposed (§4).

***

## 1. Node 1: the components of H-COUNT-1 and their corpus status

**1.1 Decomposition [S].** H-COUNT-1 (G3-TEMP §3.1):

- (a1) a shell energy E of the hidden sector is defined on every admissible state and is conserved
  on the shell, as GR:58's microcanonical step requires ("restrict the finite total system to a
  conserved energy shell"). This is W1-0 (W1-1 §8: "a real-valued energy, conserved by φ, additive
  across V/H at the shell scale, and identified with the energy H receives in the horizon first
  law").
- (a2) the hidden sector's energy-dependent entropy is a function of E alone, strictly increasing.
- (a3) it is one function for every admissible state (history independence).
- (b) s_H(E) = ηA + const.
- (c) exact de Sitter of every radius is admissible, with the first law at κ = 1/R and one
  calibration (N-dS, N-UNIV).

**1.2 Status at `D` [S].**

- (a1): GR:88 lists "the conserved energy shell (§2.3)" as a requirement; GR:699 states "The shell
  is assumed, as in §2.3; it is not a consequence of Lemma 3, which supplies determinism,
  injectivity and the selected measure but no conserved energy." SM:294: "Nor is exact energy
  conservation shown" for the rounded rule. G3-HOM Node 1: "narrowed, not closed". G3-W1: no
  conserved additive quantity in 47 classes. Open.
- (a2), (a3): not stated in the corpus for non-de-Sitter states (G3-TEMP 3.1). GR:58 states H-count
  with E "the energy of the horizon first law" and evaluates it on the exact-de-Sitter calibration.
- (b): GR:58, "S1–S4 do not supply it". W1-1 `STATUS.md`: "W1 is an additional physical
  assumption, not a derived result." In the real lift of the linear rule the whole-hidden-sector
  slope exceeds the boundary slope by r ≈ +7×10⁵⁹ (W1-1 C6(a′)).
- (c): GR:56, GR:78, conditional on GR:88's list.

**Node 1 verdict.** ESTABLISHED [S]. (b) and (c) have recorded corpus status and are not re-examined
here beyond their use. The native question concerns (a1)–(a3). CONFIRMING.

## 2. Node 2: W1-0

**2.1 Corpus after G3-TEMP [S].** The records on `main` and on the G3-OFFDS and G3-TEMP branches
were searched for a conserved real shell energy (search terms: conserved, shell, W1-0, sublattice,
checkerboard, staggered). None supplies one for the rounded d = 3 rule. G3-W1 §4 lists as not
excluded, among others, "densities that are not translation invariant (for example
parity-staggered), quantities with E(t+1) = −E(t)".

**2.2 A reduction of the staggered alternating class [W].** Let h be a translation-invariant,
parity-pure density with h(0) = 0, Φ = Σ_n h, and Y(c) = Φ_0(0) − Φ_1(0), the sublattice difference
evaluated with the labelling of step 0. Suppose Y∘F = −Y on all finite-support configurations of ℤ³
(equivalently, Φ_0(t) − Φ_1(t) is conserved in the running labelling). By Lemma 3.4's argument
applied to Φ_0 − Φ_1, each Φ_k(t) is conserved, so Φ is conserved on finite-support configurations,
hence on all periodic configurations (G3-W1 Lemma 4, for RZ, the rule over ℤ of G3-W1 §1; for Q
through G3-W1 Lemma 6). If h lies in G3-W1's direct 3D classes P3(2)
or P3(3) (star polynomials of degree ≤ 2 or ≤ 3), Φ is trivial: Φ = λN on every periodic
configuration (G3-W1 §0 item 1). On a checkerboard torus Φ_0 is a function of the Λ_0-data alone
and λN − Φ_1 a function of the Λ_1-data alone; they are equal on the product of the two data sets,
so both are constant, and Y is constant on that torus. With Y∘F = −Y, Y = 0. So every such
alternating staggered quantity vanishes on checkerboard periodic configurations. Scope: parity-pure
densities in P3(2), P3(3); the residue classes P3r(2), whose coefficients read (S y)_n and (S p)_n
at both parities, and densities that are not parity-pure, are not covered.

**2.3 Skeptical pass.** The reduction uses G3-W1's certificates, which are WIP / UNVERIFIED author
results (G3-W1 standing). It narrows one item of G3-W1 §4 and supplies no conserved quantity.

**Node 2 verdict.** W1-0 at d = 3: open, MISSING (M1). ESTABLISHED [W]: 2.2 at its scope,
conditional on G3-W1's certificates. NEW (author): 2.2.

## 3. Node 3: is a further conserved shell variable required?

**3.1 The conserved functions of a finite bijection [W, S].** For a bijection φ of a finite set, a
real function is conserved iff it is constant on every cycle; the conserved functions are the
functions of the cycle label (G3-HOM 1.2). A conserved E has shells that are unions of cycles. The
E-shell is the accessible set of an orbit iff it is a single cycle (SM:292: "Single-cycle
ergodicity is needed to identify the empirical law of one occupied orbit with the uniform law on
the whole shell"). So the cycle label is always a conserved variable beyond E, and it is a function
of E on a shell only when that shell is one cycle. For the exact linear rule at prime q ∤ L, the
largest energy shell is not a single cycle and for d ≥ 2 carries exponentially many cycles (SM:296,
*Remark (cycle structure of the exact linear rule)*); for the rounded rule, exact censuses at d = 3,
L = 2 give a largest cycle of at most 1.9% of phase space (SM:294).

**3.2 Sublattice decoupling [W, EC K1].** Assume N-2ND, N-NN, N-CI (second clause: F_n reads no
copy of x_t(n)) and N-BIP. The value x(t+1)(n) = F_n(x(t)) − x(t−1)(n) reads the values at (m, t),
m ∼ n, and at (n, t − 1). Since |m| = |n| ± 1, all of these points have the parity of (n, t + 1).
So the restriction of a trajectory to Λ_k is determined by its Λ_k-data at any one step, whatever
the Λ_{1−k}-data. In fixed phase-space coordinates let P_0 = (u on |n| odd, v on |n| even) and
P_1 = (u on |n| even, v on |n| odd). At even t, P_0 holds the Λ_0-data. Then

  F(p_0, p_1) = (g(p_1), f(p_0)),  F² = (g∘f) × (f∘g),

with f : X_{P_0} → X_{P_1} and g : X_{P_1} → X_{P_0} bijections. On a torus whose period vectors
include one of odd coordinate sum the parity is not defined and the decoupling fails (SM:539).
Check K1: for the rounded rule and the linear rule at q = 2^16, on d = 1, L = 6 and d = 3, L = 2, 4,
changing the Λ_1-data at step 0 leaves the Λ_0-trajectory unchanged for 12 steps; the countercontrols
(odd tori d = 1, L = 5 and d = 3, L = 3; a rule whose F_n also reads x_t(n)) change it. SM:294
records the same confinement in its separation measurement ("saturates the perturbed parity
sublattice"). ELABORATING: the bipartite coupling is SM:539's; the product form of F² is stated
here.

**3.3 Sublattice orbit labels [W].** Write [p]_{gf} for the cycle of p under g∘f. The unordered pair
{[p_0]_{gf}, [g(p_1)]_{gf}} is conserved by F: F(p_0, p_1) = (g p_1, f p_0) has the pair
{[g p_1]_{gf}, [g f p_0]_{gf}} = {[g p_1]_{gf}, [p_0]_{gf}}. So every F-cycle lies in the product of
one Λ_0-orbit and one Λ_1-orbit, and an E-shell that is a single F-cycle has all its states on the
same two sublattice orbits. This holds for every conserved E, parity-pure or not.

**3.4 Lemma (separate conservation) [W, EC K2].** Under 3.2's assumptions, let Φ be additive with a
time-translation-invariant, parity-pure density, conserved on all configurations with values in an
abelian group (ℝ, ℤ, or ℤ/q), and let the rule map the zero Λ_0-data to zero Λ_0-data (true for the
rounded rule, G(0) = 0, and for the linear rule). Then Φ_0(t) and Φ_1(t) are each conserved.

*Proof.* Δ_0 = Φ_0(t+1) − Φ_0(t) is a function of the Λ_0-data at step t alone (3.2), and Δ_1 of
the Λ_1-data alone. Δ_0 + Δ_1 = 0 for all pairs of data, which range independently over X_{P_0} ×
X_{P_1}; so Δ_0 is a constant c. At zero Λ_0-data both Φ_0(t) and Φ_0(t+1) are sums of the same
terms of the zero data, so c = 0. □

SM's E = u·u + v·v − u·Av is parity-pure: u_n² and v_n² are single points, and u_n v_m with m ∼ n
joins (n, t − 1) to (m, t), of equal parity. (The decomposition |v − u|² + u·(2 − A)v of SM:296 is
not term-wise pure; its cross terms u_n v_n cancel.) Check K2 (exhaustive): the two parts are each
conserved modulo q for the exact linear rule at (d, L, q) = (1, 4, 3), (1, 6, 3), (2, 2, 3), and as
integers on binary configurations at RD6 (d = 1, q = 2, α = 1; L = 4, 6, 8); with the labelling of
step 0 frozen they exchange, so Y = E_0 − E_1 alternates; on some E-shell E_0 takes 3 to 5 distinct
values (nontriviality); the countercontrol split by the spatial parity of the site alone is not
conserved.

**3.5 Consequence [W].** On the class of 3.4, X = E_0 − E_1 (running labelling) is a conserved shell
variable beyond E, nontrivial wherever an E-shell contains states with different E_0. Its existence
is forced by N-2ND, N-NN, N-CI and N-BIP together with the existence of a parity-pure conserved E;
it is not an additional posit. The set a state can reach lies in its (E, X) shell, a proper subset
of the E-shell wherever X is nontrivial there, so the entropy of the reachable set at fixed
conserved variables is not the E-shell entropy s_1(E). At RD6 there are further additive invariants,
the mover counts N_L, N_R, and the mover patterns are transported rigidly, so the orbit of a state
keeps its full pattern up to translation (G3-HOM 1.2).

**3.6 Skeptical pass (the branch is unfavourable to H-COUNT-1; checked for overreach).**

- *Scope of the lattice.* N-BIP holds on ℤ³ and on quotients with all period vectors of even
  coordinate sum, the lattices on which SM's checkerboard results are stated (SM:539). It fails on
  odd tori; the side of the finite representative is not fixed in the corpus.
- *Scope of the energy.* The rounded rule conserves no energy known to the corpus. 3.5 is a
  conditional: if W1-0 is met by a parity-pure additive energy, the second variable is present.
  Energies that are not parity-pure are covered only by 3.3.
- *Relevance.* A conserved X refutes the reading of (a2) at fixed conserved variables; it does not
  by itself change the counting temperature. That is Node 4.

**Node 3 verdict.** ESTABLISHED: 3.1 [W, S]; 3.2 [W, EC]; 3.3 [W]; 3.4 [W, EC]; 3.5 [W]. Refuted on
a class: the reading of (a2) as "the count at fixed values of all conserved variables depends on E
alone", on checkerboard lattices under N-2ND, N-NN, N-CI, for every conserved parity-pure additive
energy (proof), and at RD6 (d = 1, q = 2, α = 1, every L ≥ 3) by the mover counts (G3-HOM 1.2;
K2). NEW (author): 3.3–3.5 and their bearing on H-count. ELABORATING: 3.2. CONFIRMING: 3.1.

## 4. Node 4: does a further conserved variable change the counting temperature?

**4.1 Exact identity [W].** Let X be conserved, Ω(E, X) the number of states of the counted set
with energy E and value X, Ω(E) = Σ_X Ω(E, X) the marginal count, and p(X | E) = Ω(E, X)/Ω(E).
For an energy step δ,

  Ω(E+δ)/Ω(E) = Σ_{X: Ω(E,X)>0} p(X | E)·Ω(E+δ, X)/Ω(E, X) + Σ_{X: Ω(E,X)=0} Ω(E+δ, X)/Ω(E),

the same structure as W1-1 N2's lattice identity. So the marginal slope β_1(E) is a p(X | E)-weighted
exponential average of the fixed-X slopes β(E, X), up to the second sum. On the marginal reading of
(a2), s_1(E) = ln Ω(E) is a function of E by definition. On the fixed-X reading, the count relevant
to an orbit, whose X is conserved, is Ω(E, X_r) at its realized value X_r; its slope equals β_1 at
leading order when X_r lies where p(X | E) concentrates and the slopes there agree (the envelope
statement d/dE max_X s(E, X) = ∂_E s(E, X*)). Call X_r **slope-typical** when it lies where
p(X | E) concentrates and β(E, X_r) = β_1(E) at leading order.

**4.2 The sublattice symmetry [W].** A unit translation T_1 commutes with F (N-CI first clause; the
rounded rule on a torus is translation-invariant) and maps Λ_0 to Λ_1. For a translation-invariant
parity-pure density, Φ_1∘T_1 = Φ_0, so the counts ω_k(e) of Λ_k-data with Φ_k = e are one function
ω, and Ω(E, X) = ω((E+X)/2)·ω((E−X)/2), symmetric in X.

**4.3 Where p(X | E) concentrates [W, L].**

- If ln ω is concave (positive heat capacity, the ordinary case for an extensive count), the split
  X = 0 maximizes Ω(E, X) and β(E, 0) = (ln ω)'(E/2) = β_1(E) at leading order.
- If ln ω is convex, X = 0 minimizes Ω(E, X), p(X | E) concentrates at the extreme splits, and the
  symmetric split has a different slope. For ω = e^{c e²}, β(E, 0) = cE while β_1(E) = 2cE at
  leading order: a factor 2 in the temperature. That the equal split of two weakly coupled copies
  with negative heat capacity is an entropy minimum is the standard result for gravitating systems
  (Lynden-Bell and Wood, MNRAS 138, 495 (1968); Thirring, Z. Phys. 235, 339 (1970); Padmanabhan,
  Phys. Rep. 188, 285 (1990)) [L].
- H-count's de Sitter form is convex: s_H = 4πσG²E²/ϵ² with s_H'' = β/E > 0 (GR:58). Whether each
  sublattice part carries a count of this form is not supplied; if it does, the typical split is
  extreme and the symmetric one is not slope-typical.

**4.4 Two temperatures at X ≠ 0 [W].** With per-sublattice additivity (H-shell's additivity part,
W1-1 W1-add, applied to each Λ_k), the hidden count at visible configuration i factorizes,
Ω_{H,0}(E_0 − e_{i,0})·Ω_{H,1}(E_1 − e_{i,1}), and GR:70's rate ratio reads
ln(P_ij/P_ji) = −β^(0)(e_{j,0} − e_{i,0}) − β^(1)(e_{j,1} − e_{i,1}) + …, with β^(k) the slope of
Ω_{H,k}. A single detailed-balance slope on all identified transitions, as H-slope uses, then
requires β^(0) = β^(1) on those transitions.

**4.5 Native or imposed [W, S].** The identity 4.1, the symmetry 4.2 and the factorization 4.4 are
deductions from φ and the counted set. Slope typicality is not: it is a statement about the realized
values X_r, which φ conserves and does not select. Under T-MEAS (Main:736 (iv), the maximal-entropy
invariant measure compatible with the records, "a standard but substantive epistemic postulate, not
derived") values of X not fixed by the records are weighted by Ω(E, X), so X_r lies where
p(X | E) concentrates with probability close to one, if it concentrates. Which value that is
depends on the concavity or convexity of the count (4.3), which the corpus does not supply. T-MIX
(Main:736 (v)) does not help: X is exactly conserved, so no mixing moves it.

**4.6 Skeptical pass (the branch is favourable to the one-variable law).** The favourable reading is
"further conserved variables are harmless because they sit at their typical values". Three limits:
it rests on T-MEAS, a posit; the typical value is the symmetric split only for a concave count,
while H-count's own de Sitter form is convex (4.3); and the realized universe need not be a T-MEAS
typical state, since the measure is an epistemic selection, not a law of φ. The favourable reading is
therefore recorded as a hypothesis, (a′3) of §5, not as a result.

**Node 4 verdict.** ESTABLISHED [W]: 4.1, 4.2, 4.4; 4.3 [W, L]. Imposed: slope typicality, supplied
only by T-MEAS together with an unsupplied concavity property. MISSING (M2): a native reason that
the realized values of the further conserved variables are slope-typical. NEW (author): 4.1's use to
locate the content of (a), 4.3's concavity condition and its tension with GR:58's convex form, 4.4.

## 5. Node 5: strengthening G3-TEMP's conditional law

**5.1 H-COUNT-1′ [ASSUMED, named, not adopted].**

- (a1) as in H-COUNT-1;
- (a′2) the counted set at the horizon may carry further conserved variables X (any number,
  including the sublattice split and the orbit labels of §3); the marginal count s_1(E) = ln Ω(E)
  is one history-independent, strictly increasing function on every admissible state;
- (a′3) slope typicality at leading order: on every admissible state, the realized values X_r give
  β(E, X_r) = β_1(E)(1 + δ) with δ → 0 in the limit of large count;
- (b′) s_1(E) = ηA + const;
- (c) as in H-COUNT-1.

H-COUNT-1 implies H-COUNT-1′ (no further variables, δ = 0). The converse fails: the class of §3.4,
with its conserved second variable, satisfies (a′2) and can satisfy (a′3) while violating the
fixed-variable reading of (a2).

**5.2 Derivation [W].** G3-TEMP 3.2 uses only the marginal count: by (a′2), (b′) and (c),
E = R/G + E_0 on every admissible state, and β_1 = 8πGηR. By (a′3) the counting temperature of the
realized state is T = 1/(β_1(1 + δ)) = 1/(8πGηR)·(1 + o(1)), and ħ/(2πR)(1 + o(1)) under GR:88's
calibration conditions. G3-TEMP 3.3's exclusion carries over at leading order: T_A/T =
|1 − ε/2|(1 + δ) differs from 1 for ε ∉ {0, 4} once δ is small. G3-TEMP 4.2 carries over: with
N-SLOPE and N-UNIV, a_* = ħ(1 + o(1))/(|κ|R), so |κ| = 1/R at leading order on the counted surface
and κ_KH is excluded there. With N-AREA, T = ħH/2π at leading order, the R1 branch as in G3-TEMP.

**5.3 Skeptical pass (favourable branch).** The strengthening moves the load from (a2) to (a′3); it
supplies none of (a1), (a′3), (b′), (a′2)'s history independence. Its gain is that it is consistent
with the second variables §3 proves present, whereas the fixed-variable reading of (a) is refuted
on that class. The o(1) is not bounded here: for the exclusion at a given ε the realized δ must be
smaller than (1 − ε/2)⁻¹ − 1 in magnitude (about 0.29 at GR:56's ΛCDM value 1 − ε/2 ≈ 0.775), and
4.3's convex case gives δ = −1/2 at the symmetric split, which is not small.

**Node 5 verdict.** Strengthened, conditionally: G3-TEMP's law and exclusions hold at leading order
under H-COUNT-1′, strictly weaker than H-COUNT-1. ESTABLISHED [W] under H-COUNT-1′. ASSUMED:
H-COUNT-1′. NEW (author).

## 6. Node 6: history independence and the moving partition

**6.1 What (a3) requires [W, S].** The count is a property of the counted set and the energy
function (W1-1 N1: "β_E depends only on the configuration set, the energy function and E"). The
counted set is the hidden sector of the partition, which GR:40 takes from "the supplied causal
geometry", the event horizon (N-PART). One function s_1(E) for every admissible state therefore
requires the partition to enter the count only through E. On exact de Sitter this holds through
E = R/G. Off de Sitter:

- the event horizon R_E = a∫_t^∞ dt′/a depends on the future history, and is not a function of R_A
  (H R_E varies with the composition; G3-OFFDS §5 records the surface as an open choice);
- under N-PART with N-AREA (the counted area on R_A, GR:56), the count of a hidden set bounded by
  R_E is set equal to the area count of a different surface; the partition radius is then a second
  label of the count, of the kind (a′2) excludes unless it is a function of E;
- the partition moves, so cells cross it (W1-1 N3, CE-M), and the hidden sector's energy changes by
  the Cai–Kim flux (G3-TEMP 3.3); the conserved quantity is the total shell energy, not the hidden
  sector's.

**6.2 Verdict.** (a3) and the history independence in (a′2) are imposed; they are the counted-surface
question of G3-OFFDS §5 in counting form. The partition is supplied geometry and not a conserved
variable of φ. MISSING (M3): a native partition off de Sitter that enters the count only through E.
ESTABLISHED [W, S]. ELABORATING.

## 7. Node 7: what the T_A route needs

**7.1 Conditions [W].** Suppose X is conserved along each history and the count at fixed X keeps the
area form s(E, X) = ηA. Then T = (∂s/∂E)_X⁻¹ = (∂E/∂A)_X/η, so for ε < 2 the condition T = T_A
on R_A reads (∂E/∂A)_X = (1 − ε/2)/(8πGR_A), that is

  E(A, X) = (1/G)∫^{R_A}(1 − ε_X(R′)/2) dR′ + const,

with ε_X(R) the history labelled by X (R_A is monotone when ε > 0). So X must label expansion
histories: its realized value must fix ε as a function of R_A. The de Sitter states remain
admissible (ε = 0, a single radius each), and N-UNIV holds with κ = κ_KH (G3-TEMP 4.3).

**7.2 Atypicality [W, estimate].** The fixed-X slope must differ from the marginal slope β_1 by the
fraction (1 − ε/2)⁻¹ − 1. For an extensive count s(E, X) = N f(E/N, X/N) this needs an O(1)
displacement of X/N from the concentration point and costs an entropy deficit of order N, that is
of order s. Under T-MEAS such a value has weight e^{−O(s)}. This is an order-of-magnitude statement
conditional on extensivity; the horizon count of (b) is not extensive in the ordinary sense (4.3).

**7.3 Native candidates [W, S].** None satisfies 7.1:

- the orbit labels (3.1, 3.3): conserved, not linked to ε;
- the sublattice split (3.4): symmetric in X (4.2), not linked to ε; at an extreme split it changes
  T by a factor fixed by the count's shape (4.3), not by ε;
- the quadratic invariants Q_B, P_C of the exact linear rule (SM:296): conserved modulo q, not shown
  for the rounded rule (SM:294), not linked to ε;
- the RD6 movers (G3-HOM 1.2): d = 1 only;
- the partition (6.1): supplied geometry, not a conserved variable of φ.

Conserved charges of the emergent matter description (comoving numbers that fix the composition and
hence ε) are emergent objects; using them as substratum shell variables would place an emergent
input at the substratum layer, the Step-5 mismatch of the audit method.

**Node 7 verdict.** MISSING (M5): a conserved shell variable of φ whose realized value labels the
expansion history and is slope-atypical by (1 − ε/2)⁻¹ − 1. G3-TEMP's "T_A reachable" with a second
shell variable is narrowed to this class. ESTABLISHED [W] for 7.1; 7.2 an estimate. NEW (author).

## 8. Node 8: native deductions and imposed assumptions

| Item | Kind | Where |
|---|---|---|
| Conserved functions are functions of the cycle label; shells are unions of cycles | Deduction from N-BIJ | 3.1 |
| Sublattice decoupling, F² = (g∘f) × (f∘g) | Deduction from N-2ND, N-NN, N-CI, N-BIP | 3.2 |
| Conserved pair of sublattice orbit labels | Deduction (same items) | 3.3 |
| Separate conservation of the sublattice parts of a parity-pure conserved energy | Deduction (same items, plus a conserved parity-pure E and the zero fixed point) | 3.4 |
| Marginal slope as the p(X \| E)-average of fixed-X slopes | Deduction (counting) | 4.1 |
| Count symmetric in the sublattice split | Deduction from N-CI | 4.2 |
| Detailed balance on any reversal-invariant counted set | Deduction from N-BIJ, N-REV | GR:70 |
| A real conserved shell energy (W1-0) | Open | §2 |
| Slope typicality of further conserved variables | Imposed: T-MEAS plus an unsupplied concavity property | §4 |
| One count function across histories; the partition entering through E | Imposed | §6 |
| s_H = ηA (W1) | Imposed | §1; W1-1 |
| De Sitter family and one calibration | Corpus conditions (N-dS, N-UNIV, GR:88) | §1 |

**8.1 Overall verdict under the decision rule.** H-COUNT-1 is not derived. Its fixed-variable
reading of (a2) is refuted on the class of §3.4 (proof) and at RD6. Its marginal reading is a
definition. Its load-bearing content, slope typicality (§4), its history independence (§6) and its
area count (b) are imposed. W1-0 is open. Under H-COUNT-1′ (§5) G3-TEMP's law holds at leading
order. Outcome: missing native mechanism (M1–M5), with a proof refuting the fixed-variable reading
of (a2) on the stated class.

## 9. Consistency with G3-TEMP, G3-OFFDS, G3-HOM, G3-W1 and W1-1

- **G3-TEMP.** Its 3.2–3.3 and 4.2 are reproduced under H-COUNT-1′ at leading order (§5). Its 3.3
  "way out" through a count s_H(E, X) is refined: a second variable is present natively (§3), and
  yields T_A only under 7.1–7.2. Its Node 5 G3-W1 bullet is unaffected: the second variable of 3.5
  is, in fixed labelling, a staggered quantity that alternates in sign, a kind G3-W1 §4 lists as not
  excluded; it is conserved only if E is (3.4), and 2.2 reduces it to G3-W1's classes for
  parity-pure densities in P3(2), P3(3).
- **G3-OFFDS.** The counted-surface question (§5 there) appears here as (a3) (§6).
- **G3-HOM.** Node 1's RD6 energy is an instance of 3.4 (K2) and carries the further invariants of
  3.5; its 1.3 observation that all RD6 energy sits on cut-crossing bonds concerns additivity across
  V/H, which this record does not address.
- **G3-W1.** Its exclusions are used in 2.2 and not re-derived.
- **W1-1.** Its W1-min′ (the slope of the realized, dynamically connected sector) is the
  orbit-level form of slope typicality; 4.1 gives its relation to the marginal slope when the
  connected sector is a fixed-X shell. Its comparison "GR:58's setting with H-count implies W1-0 and
  W1-min(L)" is unaffected; §3 shows that, on the class of 3.4, that setting cannot hold with the
  count at fixed conserved variables a function of E alone.

## 10. Classification and stop

**ESTABLISHED.** 1.2 [S]; 2.2 [W] conditional on G3-W1's certificates; 3.1 [W, S]; 3.2 [W, EC];
3.3 [W]; 3.4 [W, EC]; 3.5 [W]; 4.1, 4.2, 4.4 [W]; 4.3 [W, L]; 5.2 [W] under H-COUNT-1′; 6.1 [W, S];
7.1 [W]; 7.2 an estimate.

**ASSUMED.** N-BIJ, N-2ND, N-NN, N-CI, N-BIP, N-REV, T-MEAS, T-MIX, T-AREA at their corpus status;
the G3-TEMP set; H-COUNT-1 and H-COUNT-1′, named and not adopted.

**MISSING.** (M1) a real conserved additive shell energy for the d = 3 rule (W1-0); (M2) a native
reason for slope typicality of the further conserved variables; (M3) a native partition off de
Sitter entering the count only through E; (M4) the whole-hidden-sector boundary count (W1); (M5) for
T_A, a conserved variable tied to the expansion history.

**Findings (§A.31).**
- NEW (author): 2.2; 3.3–3.5 (the second conserved shell variable forced on the parity-pure class);
  4.1's location of the content of (a), 4.3's concavity condition, 4.4; §5's H-COUNT-1′ and the
  strengthened law; 7.1–7.2.
- ELABORATING: 3.2; §6.
- CONFIRMING: 1.2; 3.1.

**Findings for routing (no edits made).**
- GR:58's "restrict the finite total system to a conserved energy shell": on the class of 3.4 the
  conserved shell carries a second conserved variable, so the shell on which uniform counting is the
  accessible-set law is the (E, X) shell, or the orbit (SM:292).
- GR:58's de Sitter form s_H'' = β/E > 0 is a convex count; the step from a symmetric split to a
  typical one needs concavity (4.3).
- G3-W1 §4's not-excluded item "parity-staggered … E(t+1) = −E(t)" is reduced, for parity-pure
  densities in P3(2) and P3(3), to its excluded classes (2.2).

**Stop.** The first stop condition is reached: each component and the second-variable question is
answered under the decision rule. One depth-first pass was made; a fixed point is not claimed. No
premise was adopted. There is no successor round.

## 11. Reproduction

`python3 -I verification/programmes/gravity/drafts/g3-hcount-20261122/checks/sublattice_checks.py`
at this record's commit: exit status 0, final line `ALL PASS`, about half a minute of CPU. K1 prints
`True` for the six decoupling cases and `decoupled=False` for the three countercontrols; K2 prints
`spacetime parts conserved=True`, `frozen-label parts exchange=True`, a nonzero count of states on
which the site-parity part changes, and a maximum of 3, 3, 3, 3, 4, 5 distinct E_A values (E_0 in
the text) on one E-shell for its six cases.

## References and their role (§A.42 item 8)

| Reference | Classification |
|---|---|
| #1169 c.7079945577; #873 | Governance and planning provenance |
| G3-TEMP at `c92dd48d` (branch `research/g3-temp-20261122`) | Support off `main`: H-COUNT-1 (3.1), the derivations 3.2–3.3 and 4.2–4.3 are used; that record is on its branch only, with the standing its `NOTE.md` records; #1169 c.7079945577 names its conditional law as this round's input. This record's §5 and §7 inherit that status |
| G3-OFFDS (branch `research/g3-offds-20261122`), as cited by G3-TEMP | Support off `main` for 6.1's reference to its §5; inherited through G3-TEMP |
| G3-HOM, G3-W1, W1-1 records; GR, Main, SM lines at `D` | Support on `main` at `D` |
| Lynden-Bell–Wood (1968); Thirring (1970); Padmanabhan (1990) | Standard results quoted [L] for the entropy minimum at the equal split under negative heat capacity only |

# G3-HOM: the homogeneous sector of the native source

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form).
WIP / UNVERIFIED. Independent non-author review: REVISE (text only) at `46056261`
([#1430 c.7025180852](https://github.com/amaybaum/incompleteness/pull/1430#issuecomment-7025180852)).
The revision at `75a170d3` answers F1–F7, F2b and the nits. Re-review: ACCEPT WITH NITS at
`75a170d3`
([#1430 c.7025309840](https://github.com/amaybaum/incompleteness/pull/1430#issuecomment-7025309840)).
This revision makes its required g† correction (3.4) and its §1.2 wording nit. It adopts no premise and edits no manuscript, Lean
module or registry. Three small check scripts under `checks/` are controls and probes (§7).

- **Authorization.** Owner `amaybaum`, P3 row of
  [#1169 c.7023834853](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7023834853),
  2026-11-19T22:21:00Z: "**G3-HOM** (#873) · Try to derive the cosmological energy source; do not
  assume the desired source term". Boundary in the same comment: "These are investigation only.
  None adopts a premise. Each needs independent non-author review, and each needs its own merge
  decision."
- **Goal link (§A.47), from the authorization.** "P3 is the vacuum-energy half of the target". The
  unit decides, for the inputs on `main`, whether OI supplies a conserved homogeneous (ρ, p) for the
  horizon budget that fixes w(z), Λ_eff and ν, or which physical input is missing.
- **Accountable Issue.** #873. Planning basis: G3-SCOPE,
  [#873 c.7022640763](https://github.com/amaybaum/incompleteness/issues/873#issuecomment-7022640763),
  unit U1.
- **Snapshot.** `main` at `bae5cfdd80758abe86586f47e18cc478c0e1664a`. `GR:n` and `SM:n` are line `n`
  of `papers/GR.md` and `papers/SM.md` there. `G3-CF` is
  `verification/programmes/gravity/drafts/g3-coupling-feasibility-20261118/G3-COUPLING-FEASIBILITY.md`
  (#1379). `A1-07` is `verification/audits/foundations/a1-07-p7-energy-state/DECISION.md` (#1328).
- **Productivity test (fixed in advance by the assignment).** The unit is a gem iff it gives
  either (i) a derived attribution rule with a definite w(z) not fitted to data, or (ii) a scoped
  obstruction that identifies the irreducible missing physical input. Anything else is relabelling.
  G3-SCOPE's decision rule is applied with it: derived / conditional on named inputs /
  counterexample (completions agreeing on the shared data and differing in Λ_eff or w(z)) /
  unresolved; a coefficient adjustable to any w(z) is rejected (§A.29).

Units ħ = c = k_B = 1 in the derivations unless stated.

## Result

**Productivity verdict: (ii), a scoped obstruction.** The corpus fixes the horizon attribution only
on exact de Sitter, where every candidate rule gives ρ = 3H²/(8πG) and w = −1 with coefficient 1
(σ and ε cancel). The candidate completions agree on all exact-de-Sitter data, and so on every GR
retrodiction stated on the exact-de-Sitter calibration (3.3). They do not all agree on a₀ = cH/6
evaluated today: under the record's own temperature link its z = 0 value moves by −0.06 to
−0.11 dex (3.4). Off de Sitter the completions give respectively no dynamics (R1), a w = 0 tracker
(R2) and a definite event-horizon law w = −1/3 − (2/3)√Ω_de (R3). The counterexample rests on R2
against R3 (Node 4). Within the family ρ = λS·T/V spread uniformly over the volume, the missing
physical input is therefore the **off-de-Sitter extension of the horizon energy functional**: the
surface that carries it (event or apparent horizon) and its temperature on a non-Killing horizon,
together with the exchange law between the attributed component and matter. The candidate upstream
input is a native conserved energy–momentum for the traced sector on a non-stationary cut, which is
W1-0 with its stress, together with a native choice of its density (1.3). It would replace the
horizon attribution rather than supply its temperature, and it is not on `main`. No candidate is a
native derivation, so (i) is not met.

**W1-0 verdict: narrowed, not closed.** The traced corpus after A1-07 does not change A1-07's
SOURCE GAP. This unit's exact probe finds that on the RD6 rule class (d = 1, q = 2, α = 1) the
real-lift quadratic, evaluated as an integer on binary configurations, is exactly conserved. It is
the sum of left- and right-mover counts. That supplies a conserved real quantity at RD6. It does
not supply what A1-07 requires of it, a physical real energy: there is no first-law
identification, and on RD6 every bond carrying this energy crosses the cut. The integer
conservation fails for q = 3, and for d = 2, 3 at L ≥ 3.

## Node 1 — W1-0: a conserved real energy on the declared cut

**1.1 Corpus after A1-07 (trace).** A1-07 (2026-11-16) stops at "a physically interpreted
E : Conf_RD6 → ℝ conserved under that dynamics". Records on `main` written later were searched for
conserved, real, shell and first-law energy:

| Record | What it says on W1-0 |
|---|---|
| `verification/programmes/oi-qm/reconstruction/physical-source-hypotheses-20261118/LEDGER.md` :95, :316 | E01 open: "modular invariant and separate real lift apply to different propositions" |
| `verification/audits/foundations/a1-09-dependency-census/CENSUS.md` :88, :634 | Keeps H-count conditional; cites the A1-07 SOURCE GAP |
| `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` :86 | Coupled shell case parked at P7-B node 6.3 |
| `verification/audits/foundations/a1-08-observer-field/FIELD-SOURCE.md` :40–42 | No map from the binary records to real amplitudes |
| `verification/audits/foundations/a1-ds-20261117/A1-DS.md` :295 | Finite area or entropy does not select a conserved horizon energy |
| `verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`, `.../deliver-1-20261119/RESULT.md` | Use no real energy |
| GR:699 | "The shell is assumed … Lemma 3 … supplies … no conserved energy" |
| SM:292 | "The exact linear rule over ℤ/qℤ conserves E below only modulo q" |

Verdict 1.1: no record after A1-07 supplies the energy. CONFIRMING.

**1.2 Existence is trivial; locality is the content.** Every function constant on the cycles of a
finite bijection is a conserved real function. RD6 (L = 4, q = 2) has 256 configurations in 70
cycles, so its conserved real functions form a 70-dimensional space (`local_conservation_probe.py`).
The question with physical content is whether a conserved real quantity is a sum of local
densities, E_h(x) = Σ_i h(window_i(x)), since only such a quantity has a local current and hence a
stress. (Hattori and Takesue, Physica D 49, 295 (1991), treat this question for lattice maps.)

*Probe.* The rule is F(u, v) = (v, Av − u) mod q on ℤ/L with (Av)_i = v_{i−1} + v_{i+1}, the RD6
update of A1-07. For each window width w (both time slices on w consecutive sites), the number of
independent non-constant additive conserved quantities is rank M − rank D − 1. Here M maps h to
E_h and D = (P_F − I)M. Ranks are exact, by Bareiss elimination of the integer Gram matrices.

*Controls (green before any measurement).* Rule 184 has exactly one such quantity (particle
number) at w = 2. Lattice translation conserves every additive quantity. A seeded random bijection
of the same configuration set has none. F is a bijection on each probed ring.

*Measured.* The counts are stable in L over the ranges tested. (The reviewer's independent
recomputation found that at w = 4 the count depends on L, from wrap-around at small L.)

| q | w = 1 | w = 2 | w = 3 |
|---|---|---|---|
| 2 | 0 (L = 3–8) | 2 (L = 4–8) | 4 (L = 5–8) |
| 3 | 0 (L = 3–6) | 4 (L = 4–6) | not run |

*Identification (derived, then checked).* In d = 1 with α = 1 the update is the discrete
d'Alembert equation x(t+1, i) + x(t−1, i) = x(t, i−1) + x(t, i+1). Substitution shows that every
x(t, i) = f(i+t) + g(i−t) over ℤ/q is a solution. Over 𝔽₂ the converse, that every solution has
this form, is proved on `main` as Lemma 1 of
`verification/audits/physical-realization/ct3-r2b-q2-period-and-cycles.md` (:32); over ℤ/q with
q > 2 this record does not claim it. Nothing below uses the converse. Directly from the update,
a_i = v_{i+1} − u_i satisfies a′_i = a_{i+1}, so it is transported rigidly to the left. Likewise
b_i = u_{i+1} − v_i satisfies b′_i = b_{i−1}, so it is transported to the right. Any
additive function of the a-pattern or of the b-pattern is conserved. At q = 2, w = 2 these are
N_L = Σ_i [u_i ⊕ v_{i+1}] and N_R = Σ_i [u_{i+1} ⊕ v_i]. They are independent, which accounts for
the count of 2. Window-2 functions of the a- and b-patterns account for the 4 at w = 3. At q = 3,
w = 2 the counts of a_i = 1, a_i = 2, b_i = 1 and b_i = 2 account for the 4. For binary values
(u − v)² = u ⊕ v, so

  2 E(u, v) = Σ_i [(u_i − v_{i+1})² + (u_{i+1} − v_i)²] = N_L + N_R,

where E = u·u + v·v − u·Av is SM's quadratic, evaluated as an integer on the representatives 0, 1.
The first equality holds over ℤ for all integer u, v. Since the a- and b-patterns shift rigidly,
the identity and the conservation hold for every L ≥ 3. `binary_energy_checks.py` verifies both
exhaustively for L = 3–10. Reversal (u, v) ↦ (v, u) exchanges N_L and N_R. So E is the unique
reversal-even additive conserved quantity at w = 2, up to affine change, while N_L − N_R is
reversal-odd. At w ≥ 3 the reversal-even family grows.

*Countercontrols.* E evaluated as an integer is not conserved for d = 1, q = 3 at L = 5. The
witness is u = 0, v = (0,0,2,0,2), with E going 8 → 5. It is not conserved for d = 2, q = 2 at
L = 3 (exhaustive) or for d = 3, q = 2 at L = 3, 4 (sparse search). These are statements about
L ≥ 3: at L = 2, q = 2, Av ≡ 0 in any d, F is the swap, and E as an integer is conserved trivially.
On every configuration visited, the script also checks conservation of E modulo q, which SM:296
proves for symmetric A. That check is not vacuous: its countercontrol, the asymmetric coupling
(Av)_i = v_{i+1} at d = 1, q = 2, L = 3, violates it, and the script must find that violation.

Verdict 1.2: at RD6 a conserved, real, additive, reversal-even quantity exists. It is SM's real-lift
quadratic restricted to binary configurations. A1-07 asks for "a map or independent conservation
statement for a physical real energy on the binary update". This supplies the conservation
statement and the map (the inclusion of the representatives 0, 1). It does not establish that the
quantity is physical energy. The mechanism is special to d = 1: the rule is free transport of
non-interacting movers, whose structure is ct3 Lemma 1. Its energy shells carry
extensively many further local invariants (the full a- and b-patterns up to translation), so the
shell is not thermal in the sense H-count uses. The integer conservation does not extend to q = 3 or
to d ≥ 2, so nothing here transfers to the d = 3 cosmological class. Whether that class has any
real additive conserved quantity was not probed. NEW, at its scope: the additive invariants N_L and
N_R, the integer identity for E, and the uniqueness of the reversal-even quantity at w = 2. The
mover structure itself is ct3 Lemma 1. Finding for routing: SM:292's "only modulo q" fails for
d = 1, q = 2, α = 1 at every L ≥ 3. SM's conclusion in that paragraph, that no required
real positive-definite energy is supplied, is unaffected: E is positive semidefinite there with null
patterns, and the dynamics is integrable.

**1.3 Attribution already at the micro level.** The density of E lives on bonds:
e_{i,i+1} = ½[(u_i ⊕ v_{i+1}) + (u_{i+1} ⊕ v_i)]. On RD6's cut, V = {0}, B = {1, 3}, D = {2}, the
four bonds are (0,1) and (3,0) between V and B, and (1,2) and (2,3) between B and D. All of E sits
on cut-crossing bonds. An additive density is defined only up to a lattice divergence
(h → h + g∘T − g), and a divergence moves energy between sites without changing the total. So the
split of the conserved total into visible, boundary and deep energies is a choice that conservation
does not fix. H-count's "negligible boundary interaction" (GR:58) fails at this cut: none of the
energy sits on bonds within one region. This
is the lattice counterpart of G3-CF's flat-space ambiguity
(∂_μ∂_ν − η_μν□)f, which changes the local tensor and not the integrated energy. NEW.

**Node 1 verdict.** W1-0 at RD6: existence of a conserved real local energy, yes (new). Its
first-law identification and its attribution across the cut, no. At the d = 3 class: open. The
SOURCE GAP of A1-07 is narrowed to identification and attribution at RD6, and stands for d = 3.

## Node 2 — candidate attribution rules

Common notation: horizon radius R, entropy S = σA/ε² = πR²/G under the calibration, classical
temperature T_cl = ε²κ/(8πGσ) (GR §3.1), volume V = 4πR³/3. With κ = 1/R,
**S·T = R/(2G) and ρ = S·T/V = 3/(8πG R²), independent of σ and ε** (check A1). Ω_de is the
fraction of the flat Friedmann density, and Ω_de0 = 0.69 below is a supplied illustration, not a
fit.

| # | Rule | Source | Native / imported / posited | Implied w(z) | Λ_eff | ν |
|---|---|---|---|---|---|---|
| R1 | E = S·T on the apparent horizon R_A = 1/H with T = H/2π; ρ = E/V | GR §7.2 (GR:422–438) | First-law normalization imported (Gibbons–Hawking area law; Jacobson); count conditional on H-count; attribution posited (GR:438) | None: ρ = 3H²/(8πG) for every H(t) (2.1) | Not fixed | Read as vacuum, ν = 1 |
| R2 | E = S·T_A on R_A with the Kodama–Hayward T_A = (H/2π)\|1 + Ḣ/2H²\| | GR:56 supplies T_A; the combination is this unit's variant | Posited | As a derived function of the total (ρ, p): none. Equated with the total: forces Ḣ = 0. As a separately conserved component: w = (1 − 4Ω)/(3Ω), tracking to Ω = 1/4, w = 0 in matter domination (2.2) | Not fixed | ν = 1 with an Ḣ term ½ |
| R3 | E = S·T on the event horizon R_E = a∫_t^∞dt′/a with T = 1/(2πR_E) | Li, Phys. Lett. B 603, 1 (2004), hep-th/0403127, with c = 1 | Imported; T at a non-Killing horizon posited; separate conservation posited | w = −1/3 − (2/3)√Ω_de(z) (2.3) | No constant; asymptotically de Sitter at a rate set by the solution | Not H-local; local slope ν_eff ≈ 0.20 at z = 0 |
| R3′ | As R3 with E = ∫T dS = 2S·T, or Padmanabhan's ½N T with N = 4S | Padmanabhan, Rep. Prog. Phys. 73, 046901 (2010), arXiv:0911.5004 | Imported | Read as ρV: c² = 2, w0 = −0.725; fails the exact-de-Sitter control (3.3) | — | — |
| R4 | Local Rindler δQ = T dS, with heat = matter flux T_ab k^a k^b | Jacobson, PRL 75, 1260 (1995), gr-qc/9504004: heat flux eq. (2), Λ as integration constant eq. (6) | Imported (gravity side) | The matter's own | Integration constant | Not defined |
| R5 | Apparent-horizon first law −dE = T dS | Cai and Kim, JHEP 02 (2005) 050, hep-th/0501055; Akbar and Cai, PRD 75, 084003 (2007), hep-th/0609128 | Imported (gravity side) | The matter's own; R1 is its integrated form (2.1) | Integration constant | Not defined |
| R6 | Holographic equipartition dV/dt = L_p²(N_sur − N_bulk), N_bulk = −2E_Komar/T | Padmanabhan, arXiv:1206.4916 | Imported (gravity side) | Expansion law for supplied (ρ, p); N_sur = N_bulk holds exactly in de Sitter | Any H_∞ | 0 |
| R7 | Bound L³ρ ≲ L/G | Cohen, Kaplan and Nelson, PRL 82, 4971 (1999), hep-th/9803132 | Imported | An inequality; saturation with L = R_A gives R1 and with L = R_E gives R3 | — | — |
| R8 | One-loop running of the emergent matter theory | GR §7.1 (GR:390–402), Shapiro–Solà | Imported (emergent) | ≈ −1 | ρ_Λ(H_0) supplied | ν_QFT ~ 10⁻³², conditional on the source split |
| R9 | G + Λ_* g = 8πG(T^ref + ΔT) | G3-CF | Form only | T^ref and Λ_* are inputs | Input | — |

R4–R6 are statements about how geometry responds to a supplied (ρ, p), with Λ as an integration
constant or an undetermined equilibrium. They are not attribution rules. R7 is a bound. R8 is the
emergent channel whose gravitational assignment G3-CF leaves open. R9 is the slot an attribution
rule would fill. So the candidates that attribute the boundary energy are R1–R3′.

**2.1 R1 is the Misner–Sharp identity and carries no dynamics.** At R_A = 1/H,
E_s = S·T = R_A/(2G). The Misner–Sharp mass inside the apparent horizon of flat FLRW is
(4π/3)R_A³ρ_tot (Misner and Sharp, Phys. Rev. 136, B571 (1964); Hayward, Class. Quantum Grav. 15,
3147 (1998), gr-qc/9710089). The equality E_s = (4π/3)R_A³ρ_tot is the Friedmann constraint
H² = 8πGρ_tot/3 (check A3). Take ρ_s = 3H²/(8πG) with the pressure fixed by conservation,
p_s = −ρ_s − ρ̇_s/(3H) = −(3H² + 2Ḣ)/(8πG). This pair satisfies both Friedmann equations for
every (H, Ḣ) (check A4), so it constrains no expansion history and fixes no w. Read as a
running-vacuum density it has ν = 1 (check A5). Read as a vacuum component beside matter it gives
Ω_tot = 1 + Ω_B > 1 in flat FLRW, which contradicts the supplied Ω_B > 0. R1 is therefore the
total density restated, as GR §7.2 states it ("normalization").

**2.2 R2, GR's own dynamical temperature, gives a matter-era tracker.** GR:56 gives
T_A = (H/2π)|1 + Ḣ/(2H²)|. For w_tot ≤ 1/3 the bracket is non-negative, and on that domain
ρ_A = S·T_A/V_A = 3(H² + Ḣ/2)/(8πG) = (ρ_tot − 3p_tot)/4 (check A6). Read as a derived function of
the total (ρ, p), and not as a separately conserved component, it constrains no expansion history,
so it has no dynamics. Equated with the total density instead, Friedmann forces Ḣ = 0: de Sitter
only, which contradicts Ω_B > 0 as R1 read as a vacuum component does. Read as a separately
conserved component beside conserved matter,
Ω = (1 − 3wΩ)/4 gives w = (1 − 4Ω)/(3Ω) and dΩ/d ln a = (1 − Ω)(4Ω − 1) (check A7). Ω = 1/4 is the
past attractor in matter domination, where w = 0. The component then becomes a smooth
non-clustering dust making up a quarter of the density. This reproduces Hsu's w = 0 result for
Hubble-scale holographic energy (Phys. Lett. B 594, 13 (2004), hep-th/0403052), which Hsu
describes as strongly disfavoured. The new element is only that GR's own T_A, used in GR's §7.2
rule, gives it. A quantitative confrontation of this variant was not performed.

**2.3 R3, the event horizon, gives definite dynamics.** From Ṙ_E = HR_E − 1 and
ρ = 3/(8πG R_E²), ρ̇ = −2ρ(H − 1/R_E). Conservation then gives w = −1/3 − 2/(3HR_E), and
Ω_de = 1/(HR_E)² gives **w = −1/3 − (2/3)√Ω_de**, with
dΩ_de/d ln a = Ω_de(1 − Ω_de)(1 + 2√Ω_de) (check A8). This is Li's model at c = 1. The coefficient
is not adjustable: the exact-de-Sitter control (3.3) fixes c = 1. At Ω_de0 = 0.69 (supplied) the
curve is w(0, 0.5, 1, 2, 3) = −0.887, −0.779, −0.698, −0.602, −0.550. It has w ≥ −1 throughout,
w → −1/3 as Ω_de → 0 in the past and w → −1 as Ω_de → 1 in the future (numerical, RK4). An
independent control rebuilds H(a) from conserved matter, integrates R_E by quadrature and recovers
H_0R_E0 = 1/√Ω_de0 = 1.20386. The local running slope along the solution,
ν_eff = d(Ω_deH²)/d(H²) at z = 0, is 0.20.

Posits of R3, none supplied on `main`:
- (P-T) The temperature 1/(2πR_E), that is κ = 1/R_E, on an event horizon with no Killing field.
  GR:56 states that exact KMS periodicity is unavailable off de Sitter. Wang, Gong and Abdalla
  (PRD 74, 083520 (2006), gr-qc/0511051) report that the first and second laws hold on the apparent
  horizon and fail on the event horizon with these definitions.
- (P-sep) The attributed energy is a separately conserved component with no exchange with matter.
  Type I and Type II implementations (GR:382) differ exactly here.
- (P-vol) The boundary energy is spread as a uniform bulk density. GR:436 states that the matching
  mean density leaves the interior field undetermined.
- R_E depends on the future expansion, so the rule determines the history only self-consistently.

The microscopic constants σ and ε cancel from every candidate (check A1). Even if adopted, R3's
w(z) would be the c = 1 member of the Li class, a background holographic model, and not a
prediction that depends on OI's substratum (Code Review Rules, "ambient/background calculation →
native OI prediction").

## Node 3 — controls

**3.1 G3-CF's conserved-relative-stress rows.** For binding and Casimir, the homogeneous rules
supply no local stress map, and G3-CF's first missing input is unchanged. None of R1–R3 obstructs
those rows. For the common offset, R1–R3 are functions of horizon geometry. A uniform emergent
offset with geometry fixed leaves them unchanged, so the offset row holds by construction for each.
Their response to a physical change of vacuum state, such as latent heat released in a transition,
passes only through the expansion history and is not otherwise specified. On G3-CF's structure,
R1 cannot serve as T^ref: setting T^ref_00 = ρ_crit with ΔT_00 ≠ 0 gives a total above ρ_crit and
violates the constraint, so R1 counts the total twice. R3 can serve as T^ref with Λ_* = 0, because
P-sep makes it separately conserved. That conservation is posited, not derived.

**3.2 ρ = ρ_crit at every H.** R1 satisfies both Friedmann equations for an arbitrary history (2.1).
Under the assignment's rule it is classified as **no dynamics**. So is R2 read as a derived
function of the total (ρ, p) (2.2).

**3.3 GR's retrodictions on the exact-de-Sitter calibration, preserved and not refitted.** On exact de Sitter, Ḣ = 0 and
R_E = R_A = 1/H, so R1, R2 and R3 coincide (ρ = 3H²/(8πG), w = −1). For R3, Ω_de = 1 gives w = −1.
The family E = λS·T with T = 1/(2πR) gives ρ = 3λ/(8πG R²). Exact de Sitter with the attributed
component as the only one requires λ = 1. E = ∫T dS (= 2S·T for S ∝ R², T ∝ 1/R) and Padmanabhan's
½N T read as ρV have λ = 2 and give 2ρ_crit (checks A2, A9). They fail this control. Padmanabhan's own
reading assigns 2S·T to the Komar energy |ρ + 3p|V, which equals 2ρV in de Sitter; that is R6, not
an attribution. The following are all stated on the exact-de-Sitter calibration, with κ cancelling
(GR:56), and are untouched by every candidate:
- ħ = c³ε²/(4Gσ), ε = 2√σ l_p and S = A/(4l_p²);
- ρ_QFT/ρ_cl ~ S_dS (GR §6.3);
- ρ_s/ρ_crit = 2/(d − 1) (GR:440).

No parameter was refitted. The same fact means these retrodictions cannot discriminate between the
candidates. a₀ = cH/6 (GR §7.3) is not in this list: it is evaluated at today's H₀ off exact de
Sitter, and 3.4 gives its offset under each candidate temperature.

**3.4 Event horizon against Hubble horizon.** GR:56 separates the causal event horizon from the
apparent horizon whose area the calibration uses. In flat ΛCDM with Ω_m = 0.31 (supplied
illustration), H_0R_E0 = 1.147 against H_0R_A = 1. The choice is load-bearing: at one and the same
exact-de-Sitter normalization it separates no dynamics (R1) from definite dynamics (R3).

*Assumption-watch marker (cross-propagation).* §7.3's a_0 = cH/6 uses the de Sitter temperature
H/2π. If the off-de-Sitter temperature belongs to the event horizon (P-T), the scaling becomes
a_0 ∝ 1/R_E. Its z = 0 value then moves as well:
- by 1/(H_0R_E0) under P-T: −0.059 dex in the ΛCDM background, −0.081 dex in R3's own background
  at Ω_de0 = 0.69;
- by T_A/(H/2π) = 0.7675 under R2's temperature (ΛCDM, Ω_m = 0.31): −0.115 dex.

The systematic uncertainty on the empirical acceleration scale is g† = (1.20 ± 0.24) × 10⁻¹⁰ m/s²
(McGaugh, Lelli and Schombert, PRL 117, 201101 (2016)). That is about +0.08/−0.10 dex. The two
event-horizon shifts (−0.059 and −0.081 dex) lie within it. The T_A shift (−0.115 dex) lies outside
it. So under R2's temperature, §7.3's a₀ = cH₀/6 at z = 0 would be displaced beyond the systematic
of the empirical scale, at the scope of §7.3's other inputs (Q = M_Bc², the imported factor 1/6).
This is a consequence for the a₀ retrodiction only. It does not affect the counterexample, which is
stated for w(z) off de Sitter. Normalized at z = 0, the Hubble and event-horizon scalings differ by +0.17 dex
at z = 1 and +0.31 dex at z = 2 in the same ΛCDM background. The latter is comparable to
G3-SCOPE's 0.48 dex sensitivity scale for BTFR-z (U2), whose preregistration would need to state
which temperature it tests. Related unreviewed work: the BTFR-z record on draft PR #1429 (head
`9b1d609f`, WIP / UNVERIFIED) reports the Hubble-horizon scaling a₀(z) ∝ H(z) in tension with the
KMOS³D sample at its stated scope. Its amendment 1 scopes that test to the de Sitter temperature on
the Hubble horizon. This record's conclusions do not depend on it.

## Node 4 — the obstruction

*Statement (scoped).* Take the inputs on `main` at the snapshot:
- the horizon first-law normalization dE = κ dA/(8πG);
- the count σA/ε² under H-count;
- the exact-de-Sitter calibration;
- the temperatures of GR:56;
- the supplied Friedmann scale;
- G3-CF's conditional field equation.

For an attribution ρ = λS·T/V on a horizon surface, spread uniformly over the volume, these inputs
fix the coefficient on exact de Sitter (λ = 1) and nothing off it. The counterexample rests on R2
against R3. R2 uses GR:56's own apparent-horizon temperature T_A. R3 uses the event horizon, whose
off-de-Sitter temperature GR:56 does not supply, so R3 contradicts no listed input. Both satisfy
every listed input and every exact-de-Sitter consequence. Off de Sitter, R2 gives a w = 0
matter-era tracker as a separate component and R3 gives w = −1/3 − (2/3)√Ω_de. So w(z) and Λ_eff
are not determined by the corpus. This is the counterexample category of G3-SCOPE's rule. R1 is
excluded from the pair: off de Sitter it puts T = H/2π on R_A, and GR:56 states that T_A, not H/2π,
is the apparent-horizon temperature there.

*Missing input.* Within the λS·T family with uniform spreading, supplying the surface, its
off-de-Sitter temperature and the exchange law fixes w(z) in each case above. The pair shows that
the remaining inputs do not fix them, so each of the three is needed. Sufficiency outside that
family is not shown: the spreading (P-vol) and the functional form E[S, T] off the curve
ST² = 1/(4πG) also vary, and R2's E[S, T] is already off that curve. "Irreducible" is claimed only
within the family. The candidate upstream input is a native conserved energy–momentum of the traced
sector on a non-stationary cut, that is W1-0 together with its stress. Such a stress would make the
horizon attribution unnecessary rather than supply its temperature. By 1.3 it would itself need a
native choice of density and current, because a conserved density is defined only up to a
divergence (or, in the continuum, an improvement term). Node 1 shows this at RD6: a native
conserved real energy exists, and conservation does not fix its regional attribution across the
cut. The attribution input is thus needed at the micro level too, not only at the horizon. The
smallest decisive next step is a native law for that energy's density and current on a cut, in a
class (d = 3) where the energy is conserved.

*Skeptical pass on the favourable branch (§A.31).* R3 is the one branch with definite w(z). It
was pressed on five points:
- Its coefficient comes from the Friedmann constraint at exact de Sitter, not from OI's count,
  since σ and ε cancel.
- Its temperature posit is contradicted in the thermodynamic literature cited above.
- Its local slope ν_eff ≈ 0.20 is not near-null. If OI adopted R3, GR §7.1's near-null Type II
  reading (|ν| ~ 10⁻³²) would not describe it.
- GR:691's "sign and ∼10⁻³² magnitude … predicted here" has no attribution behind it. This supports
  the GR-PRED-1 narrowing already queued (P4).
- No observational status of the c = 1 member was established here. Its confrontation needs a fit
  at the measured level (§A.24), as in G3-SCOPE's U3.

**Classification of findings (§A.31).**
- NEW: 1.2 (the additive invariants N_L and N_R at RD6, the integer identity for E, the uniqueness
  of the reversal-even quantity at w = 2, and its failure for q = 3 and for d ≥ 2 at L ≥ 3; the
  mover structure is ct3 Lemma 1); 1.3 (all RD6 energy on cut-crossing bonds; attribution defined
  only up to a divergence); 3.3 (the exact-de-Sitter control fixes λ = 1 and makes every
  retrodiction stated on that calibration blind to the attribution); Node 4.
- ELABORATING: 2.1 (R1 identified as the Misner–Sharp form of the Friedmann constraint); 2.2 (it
  reproduces Hsu's w = 0; the only new element is that GR:56's T_A in the §7.2 rule gives it); 2.3
  (Li with c = 1 and ν_eff); the a_0 marker and its z = 0 offsets.
- CONFIRMING: 1.1.

**Findings for routing (no edits made).**
- SM:292, "conserves E below only modulo q", fails for d = 1, q = 2, α = 1 at every L ≥ 3 (1.2).
- GR:691 against GR:398–402: the only dynamical attribution found is not near-null (supports P4
  GR-PRED-1).
- U2 BTFR-z should name the off-de-Sitter temperature it tests (3.4).

## 7. Reproduction

From `verification/programmes/gravity/drafts/g3-hom-20261119/checks/` at this record's commit,
Python 3 with NumPy:

| Command | Expected result |
|---|---|
| `python3 -I local_conservation_probe.py` | Exit 0; `CONTROLS GREEN`; RD6 has 70 cycles; the `MEASURED` lines give the counts of the table in 1.2 |
| `python3 -I binary_energy_checks.py` | Exit 0; every check passes, including the d = 1, q = 3 witness u = 0, v = (0,0,2,0,2), E: 8 → 5, the modulo-q conservation check on every visited configuration, and its asymmetric-coupling countercontrol, which must violate it |
| `python3 -I attribution_checks.py` | Exit 0; checks A1–A9 pass; event-horizon w(z) values, H_0R_E0 = 1.20386 by quadrature and closed form, ν_eff = 0.2008, the ΛCDM horizon numbers of 3.4 and the z = 0 a₀ offsets −0.059, −0.081 and −0.115 dex |

Check labels A1–A9 in the text refer to the nine exact-identity checks of `attribution_checks.py`,
in order. The exact checks use integer or Fraction arithmetic, and Fraction checks evaluate each
identity at 200 seeded rational points. They guard the algebra derived above; they do not replace
it. The w(z), R_E and ν_eff values are numerical (RK4 and trapezoid quadrature in floats) and are
illustrations at supplied Ω values.

## References and their role (§A.42 item 8)

| Reference | Classification |
|---|---|
| #1169 c.7023834853; #873 c.7022640763 | Governance and planning provenance |
| G3-CF, A1-07 and the node 1.1 records; GR, SM lines at the snapshot | Support on `main` at the snapshot |
| #1379, #1328 | Provenance; their records are on `main` |
| `verification/audits/physical-realization/ct3-r2b-q2-period-and-cycles.md` Lemma 1 | Support on `main` for the mover structure in 1.2 |
| Reviews [#1430 c.7025180852](https://github.com/amaybaum/incompleteness/pull/1430#issuecomment-7025180852) and [c.7025309840](https://github.com/amaybaum/incompleteness/pull/1430#issuecomment-7025309840) | Provenance for the w = 4 observation, the a₀ offset figures (recomputed here) and the g† systematic comparison |
| PR #1429 (BTFR-z, head `9b1d609f`, draft, off `main`) | Provenance only: related unreviewed work cited in 3.4; no conclusion here uses it |
| External literature (Gibbons and Hawking, PRD 15, 2738 (1977); Jacobson; Cai–Kim; Akbar–Cai; Hayward; Misner–Sharp; Padmanabhan; Cohen–Kaplan–Nelson; Li; Hsu; Wang–Gong–Abdalla; Hattori–Takesue) | Cited for the forms of imported rules and their reported properties; each use is stated where it is made |

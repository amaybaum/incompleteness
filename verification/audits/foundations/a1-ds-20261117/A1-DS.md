# A1-DS — Does de Sitter physics supply a finite, closed, reversible OI system?

## Status

**Paper-only check, not yet independently reviewed.** Complete author candidate: source assessment, exact countercontrols, geometry, reproducible scale estimates and class-scoped closure obstruction. Sole scientific writer: Codex in the owner-authorized session of 2026-11-17. A separate non-author reviewer must inspect the pushed exact head on [draft PR #1354](https://github.com/amaybaum/incompleteness/pull/1354). Paper proofs are not Lean certification or empirical verification. **A1 is OPEN / UNADOPTED; A4 is unchanged; physical source is NOT PASSED.**

## Authority and goal link

Owner **amaybaum**, **2026-11-17**, coordinating session, as quoted in the supplied instruction brief and [Issue #1353](https://github.com/amaybaum/incompleteness/issues/1353):

> I think we still need to settle the A1 issue once and for all. The entire physical argument relies on it.

> Let's run A1-DS in Codex.

The owner instructed this executing session, on the same date: **“Proceed with A1-DS”.** These are relayed chat instructions, not claims that the owner personally wrote a GitHub review. Authorization covers this one research record, its research branch and guiding draft PR, and independent review. No manuscript, Lean or registry edit, simulation, adopted premise, special workflow dispatch or merge is authorized here.

**Goal link (§A.47).** [#1353](https://github.com/amaybaum/incompleteness/issues/1353), under [#1169](https://github.com/amaybaum/incompleteness/issues/1169): decide whether independently supplied de Sitter physics establishes the finite reversible patch needed by the recurrence route, and identify its bearing on recurrence-scale P-indivisibility, P8, P12(b) and GR:58. The goal is truth about the physical chains, including a bounded negative result. The Issue assigns return to [O-ACC #914](https://github.com/amaybaum/incompleteness/issues/914) if the literature or closure gate fails; this record authorizes no work on that unit.

## Source pin and preflight

Fresh `main`, checked twice before writing on 2026-11-17: **`59d063784a2640fab2533660e4f96bcc9bc09b09`**. All repository source links below use this pin unless individually labelled otherwise. The target was absent; the worktree was clean, no matching A1-DS branch or open PR was found, and #1353 designated Codex with no competing writer record. Available resources before allocation: approximately 58 GiB disk and 9 GiB RAM. The branch is `research/a1-ds-1353-20261117`. Applicable push triggers were inspected; this path invokes ordinary PR verification, not a special research launch.

The gates, stop rule and controls were fixed in #1353 and reiterated in the [start record](https://github.com/amaybaum/incompleteness/issues/1353#issuecomment-6940728252) before calculation or proof drafting. **Productivity test:** a quantitative restriction, checkable obstruction or consequence beyond the bare assertion of finite horizon area. Stop the positive derivation at the first unsupported implication. Later gates may receive conditional diagnostics and countercontrols, without promoting them into an established physical chain.

| Source | Inspected content and role |
|---|---|
| [Main:42–60](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Main.md#L42-L60), [Main:111–160](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Main.md#L111-L160) | Visible finiteness versus total finiteness; selected measure; common exact return and earlier rooted overlap. |
| [Main:728](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Main.md#L728), [Substratum:98](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Substratum.md#L98) | A1 open; site factorization, nearest-neighbour and second-order inputs; A4 retains its finite periodic carrier. |
| [Main:746–762](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Main.md#L746-L762) | Effective compression, mixing and rate assumptions; exact compression versus iterates; the explicit de Sitter slow-bath qualification at :760. |
| [A1-10, F10/F11 and §§3.1–3.4](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md#L58-L105) | Measured versus root-shared conventions; exact and quantitative common-return routes. |
| [REC-1, contract](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L43-L70), [Props 3.6′–3.8](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L349-L398) | Invariant normalized laws do not supply exact common return; conditional visible periodicity and zero entropy rate. |
| [NR-1, setting](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L69-L105), [Thm 3.3 / Props 4.1–4.3](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L237-L333), [Prop 5.1 and qualifications](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L335-L390) | Exact prewrap agreement; prime/convex revival obstruction; distinct composite-alphabet exceptions. No NR-1 enumeration rerun here. |
| [P7-B, hypotheses and needs](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L26-L73), [slope countercontrol](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md#L155-L173) | Boundary capacity does not supply energy-shell weights, entropy slope, S3 or detector matching. |
| [KM-1, hypotheses and link count](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/km1-orientation-factor-20261116/KM-1.md#L25-L46), [GR:98–104](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/GR.md#L98-L104), [ch07:59–61](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/book/ch07-gravity.md#L59-L61) | Counting length versus lattice spacing; spherical factor 3/2, conditional single-link reading and entropy per mode. The manuscript correction associated with #1347 is present in this pin. |
| [GR:40–58](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/GR.md#L40-L58), [GR:665–669](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/GR.md#L665-L669), [ch18:166–172](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/book/ch18-beyond.md#L166-L172) | Event versus apparent horizon; H-count explicitly uses A1; finite information and the exact finite-recurrence route. |

**Off-main reference trace (§A.42 item 8).** #1353 and its start comment support planning/authority only; their substantive instructions and owner quotes are stated here. #1169 is the coordination link; #914 is the Issue's scheduling destination, not scientific evidence. #1347 identifies the correction history; all scientific content used is cited on the pinned main. [A1-FCLASS #1349](https://github.com/amaybaum/incompleteness/pull/1349), head `08ec00896c3c1008475b63e7fe3022ce27f0f478`, and [#1348](https://github.com/amaybaum/incompleteness/issues/1348) are provenance only: the PR is a review-confirmed draft, not on main, and no proof here depends on its matrix. Its non-author delta-review comment 6938834763 reports CONFIRMED WITH NITS; its PR description still says pending. That discrepancy does not alter the source status. Definitions and controls needed here are stated directly or traced to main above.

## Question and hypotheses

The target is a finite set of complete configurations for one observer's causal region, including whatever horizon variables are required, and a **single** bijection
$$\varphi_{\rm patch}:S_{\rm patch}\longrightarrow S_{\rm patch},\qquad |S_{\rm patch}|<\infty,$$
with fixed readout and preparation law reproducing that observer's dynamics over the declared time domain. Neither a finite-dimensional complex vector space nor one finite realization for each separate observation window is this target. Global A1 is stronger than a patch result and is not inferred from it.

| Id | Hypothesis or input | Status |
|---|---|---|
| H1 | Eternal exact de Sitter geometry for the test observer, or a future approaching stable de Sitter for an unbounded duration | **Posited external cosmology**, not observationally established; not a consequence of positive Λ alone. |
| H2 | Classical causal geometry and semiclassical Gibbons–Hawking area entropy and temperature | **Standard and cited**, within their GR/QFT assumptions; externally imported, not derived from OI. |
| H3 | Physical site-to-geometry map with positive physical lattice spacing and finite alphabet at all relevant times | **Open as physical input**; particular maps are conditional diagnostics below. OI's site/alphabet structure is **on main as a posit**. |
| H4 | Single-link spherical counting, σ per boundary mode, ε² = (2/3)ε_lat² and ε_lat = sqrt(6σ) l_p | **On main, conditional**, at GR:98–104; the counting identity is proved in KM-1, its physical identification remains posited. |
| H5 | Every independent physical configuration of the complete patch is included in the entropy budget, with admissible uniform mixtures | **Posited stronger interpretation**; not implied by a finite entropy value or finite observational capacity. |
| H6 | Independent assignments to all lattice variables | **Countercontrol assumption**, not adopted; to be checked against H5. |
| H7 | Horizon complementarity provides an autonomous, information-preserving microscopic patch | **Externally motivated proposal; open here**, not supplied by causal geometry. |
| H8 | That patch has finitely many ontic configurations and a bijective update reproducing the law for all specified times | **Open target**, stronger than finite Hilbert dimension and unitary evolution. |
| H9 | Main-compatible readout, one shared hidden prior, and earlier non-permutation rooted map | **On main as theorem premises; physically open** for this candidate. |
| H10 | A common exact return, or a same-time near-return with F11's strict margin | **On main as sufficient return premises; not sourced here**. |
| H11 | EM, local equilibrium, fast mixing relative to processing, uniform erosion, and applicability of iterated compression to actual observations | **On main as distinct conditional/open inputs**, not consequences of de Sitter thermality or H8. |
| H12 | Common physical realization/gluing for P12(b), and energy-shell, slope, S3 and detector conditions for GR:58 | **On main as conditional/open obligations**, not supplied by finiteness. |
| H13 | Numerical benchmark H0 = 67.4 km/s/Mpc, ΩΛ = 0.685, and SI constants; σ = 1 with q = 3, or σ = ln 2 with q = 2 | **Posited benchmark**, using cited model-inferred Planck values and constants, not a new fit or an observed eternal future. |
| H14 | Unchanged scalar nearest-neighbour second-order rule on the unrestricted product over Z³, α nonzero | **On main as the NR-1 comparison class**, not an adopted replacement of A4. Additional prime/Haar/convex or nonnilpotence assumptions are carried separately wherever NR-1 is used. |
| H15 | Admissible finite invariant subset or a finite quotient compatible with both forward and inverse evolution, including horizon records | **Open proposed remedy**, not supplied or adopted. Its sufficiency for a well-defined bijection is proved in §3.3; its physical existence is not. |
| D1–D5 | Entropy/cardinality separation; finite-unitary countercontrol; conditional finite site count and entropy restriction; direct-restriction obstruction; quotient criterion | **Proved here on paper** in §§1.1–1.2, 2.1–2.3 and 3.2–3.3. Review pending; none is a new physical premise. |

## Gate 1 — Literature and non-circularity

**Verdict: the external evidence supplies conditional geometry and thermodynamics, not the OI target. The first unsupported implication is finite horizon entropy → a finite complete configuration set.** Even granting a finite Hilbert space as an additional external input leaves a second, exact dynamical obstruction below. No new premise is adopted to pass either gap.

Primary papers were searched on the web and read first-hand as PDFs; page numbers in the following table are the papers' printed pages. The claims are attributed to their actual scope, rather than inferred from abstracts.

| Source and exact locator | What it establishes or proposes; limit relevant here |
|---|---|
| T. Banks and W. Fischler, *M-theory observables for cosmological space-times*, [hep-th/0102077v1](https://arxiv.org/abs/hep-th/0102077v1), introduction p. 3 and §4, pp. 18–21 | Motivates a finite-dimensional asymptotic-de-Sitter quantum description and observer complementarity. This is a proposed framework, not a derivation of a finite ontic lattice or an OI permutation. Its patch-dependent quantum observables are not identified with independently settable OI sites. |
| R. Bousso, *A Covariant Entropy Conjecture*, [hep-th/9905177v3](https://arxiv.org/abs/hep-th/9905177v3), §2, pp. 5–9 | Bounds entropy on suitable null light-sheets by the initial area under the conjecture's conditions. It is not an arbitrary spatial-volume cell count and supplies no autonomous update. |
| R. Bousso, *Positive Vacuum Energy and the N-bound*, [hep-th/0010252v2](https://arxiv.org/abs/hep-th/0010252v2), §1.1 pp. 1–3, §2.3 pp. 8–9, §5 pp. 13–17, §6 pp. 18–19 | Distinguishes the finite-Hilbert proposal from its entropy consequence; uses causal diamonds. The §5 argument invokes the covariant and D-bounds and is explicitly restricted to spherical symmetry at p. 17. Its conclusion is not an unrestricted proof that Λ > 0 makes all ontic configurations finite. |
| L. Dyson, M. Kleban and L. Susskind, *Disturbing Implications of a Cosmological Constant*, [hep-th/0208013v3](https://arxiv.org/abs/hep-th/0208013v3), §1 pp. 1–2, §3 pp. 7–11, §5 pp. 15–18 and appendix §7.1 pp. 22–23 | Assumes an isolated unitary causal patch motivated by holography/complementarity and analyzes equilibrium fluctuations and problematic cosmological histories. Its equilibrium recurrence estimate is not an exact common permutation order. The troubling histories are consequences of its assumptions, not evidence that those assumptions hold. |
| N. Goheer, M. Kleban and L. Susskind, *The Trouble with de Sitter Space*, [hep-th/0212209v3](https://arxiv.org/abs/hep-th/0212209v3), §§3–5 pp. 7–11 | Gives a symmetry obstruction under its quantum finite-entropy/discrete-spectrum implementation of exact de Sitter symmetry. Its discussion includes metastability and operational limits. It does not prove every finite approximate patch impossible, nor universal decay of every positive-Λ cosmology. |
| T. Banks, W. Fischler and S. Paban, *Recurrent Nightmares? Measurement Theory in de Sitter Space*, [hep-th/0210160v2](https://arxiv.org/abs/hep-th/0210160v2), §§4–5 pp. 9–16 | Argues, under its finite-quantum-system and apparatus assumptions, that reliable measurements cannot verify the formal recurrence regime. Operational accessibility must therefore be checked separately from mathematical recurrence. This is not a new OI observer theorem. |
| V. Chandrasekaran, R. Longo, G. Penington and E. Witten, *An Algebra of Observables for de Sitter Space*, [2206.10780v5](https://arxiv.org/abs/2206.10780v5), §§1.1–1.3 pp. 2–7 | Constructs a Type II₁ observable algebra in the small-G limit, with a maximum renormalized entropy. The algebra is not a finite matrix algebra; the finite-Hilbert interpretation and its limit are distinguished. This supports keeping entropy, dimension and ontic cardinality separate; it does not disprove a finite microscopic completion. |
| Z. Wang, *Microscopic origin of the entropy of de Sitter spacetime*, [2506.03058v3](https://arxiv.org/abs/2506.03058v3), §§4–6 pp. 9–12, equations (4.9), (5.6)–(5.7) | A favourable recent development: a semiclassical Euclidean wormhole/overlap calculation gives a finite rank for the constructed microcanonical family, involving the sum of two horizon entropies. It uses thin-shell states and Dirichlet-wall ensembles; it is not an OI lattice count or an exact patch permutation. We do not treat the regulated wall as a physical property of a cosmological horizon. |
| J. de Boer, D. Liska and K. Salehi Vaziri, *Microstate counting from defects in de Sitter*, [2511.09624v3](https://arxiv.org/abs/2511.09624v3), §4.3 pp. 34–35, equations (4.33)–(4.37), §5 pp. 36–39 (preprint pagination) | A Lorentzian wormhole calculation estimates the microstate count through averaged overlaps. The authors explicitly retain approximation/correction terms, neglect specified topologies, and discuss the failure within their tested configurations to satisfy both NEC and matching-background conditions. This is stronger evidence for the finite-dimensional interpretation than entropy alone, but supplies no exact OI carrier or map. |

These recent papers were included to pressure-test the favourable route. The conclusion is **not** that the literature contains no finite-state-counting construction. It is that none of the cited constructions supplies the particular classical configurations, physical site map and single bijection required here. Even an exact finite quantum dimension would still face Countercontrol 1.2. The literature search is bounded to these foundational and recent routes, not a completeness claim about all quantum-gravity proposals.

The complementarity proposal is independently motivated in the limited sense that it predates and does not invoke OI: information conservation, black-hole analogies and holographic entropy motivate it. Those motivations do not supply the specific patch carrier, horizon coupling, update or observer law. Importing quantum gravity to constrain a candidate is allowed here; using that import as an OI derivation of quantum mechanics would be circular. Likewise, OI's A1-conditioned H-count cannot first establish the horizon entropy and then use that entropy to prove A1. H2 is external throughout; H4 is only a conditional scale comparison.

### Countercontrol 1.1 — Finite entropy need not mean finite configurations

On the countably infinite set of positive integers assign probability p_n = 2^(-n). Its total mass is one, and its Shannon entropy is
$$-\sum_{n=1}^{\infty}p_n\ln p_n=\ln2\sum_{n=1}^{\infty}n2^{-n}=2\ln2<\infty.$$
For completeness, differentiating the absolutely convergent geometric series for |x| < 1 gives sum(n x^n) = x/(1-x)^2, which at x=1/2 equals 2. Thus even full support plus a finite entropy value does not bound cardinality. A different statement would suffice: if every uniform mixture over every finite subset of physically distinct configurations were admissible and had entropy at most S_max, a subset of M configurations would give ln M ≤ S_max; arbitrarily large subsets would be impossible. That universal admissibility-and-counting interpretation is H5, not a consequence of measuring one thermal entropy. Its application to hidden ontic configurations is precisely at issue.

### Countercontrol 1.2 — Finite quantum dimension does not imply an exact finite permutation realization

Take the two-dimensional unitary U = diag(1, exp(2πi sqrt(2))), prepare the equal superposition of its two basis vectors, and read the projector onto that superposition. At integer n the outcome probability is
$$p_n=\tfrac12[1+\cos(2\pi n\sqrt2)].$$
For every positive integer N, p_N < p_0 = 1: equality would require N sqrt(2) to be an integer. Hence this one fixed preparation/readout probability sequence is not periodic. Every permutation F on a finite configuration set has a common positive order L (the least common multiple of its cycle lengths). With any fixed initial distribution and readout, its probabilities obey p_(n+L) = p_n. Therefore no such finite permutation realizes this quantum sequence exactly at all integer times. This is a class obstruction to the claimed implication, not a no-go for quantum descriptions of OI finite permutations, finite-window realizations, approximate models or specially commensurate quantum spectra.

The distinction persists without choosing a time unit: a three-level Hamiltonian with energies 0, ħω and sqrt(2)ħω has no positive common exact period even up to global phase, since ωT and sqrt(2)ωT would both have to be integer multiples of 2π. Special finite quantum systems can have exact periods; finite dimension alone does not guarantee them.

Finite dimension does give arbitrarily close common returns for a fixed time-homogeneous unitary. Write its d eigenphases relative to the first as 2πθ_j. For an integer m > 1, place the m^(d-1)+1 points kθ modulo one, k=0,…,m^(d-1), in m^(d-1) boxes of side 1/m. Two share a box; their difference gives an integer 1 ≤ n ≤ m^(d-1) with every relative phase within 1/m of an integer. In operator norm, U^n is within 2π/m of a scalar identity. This elementary bound neither makes the error zero nor supplies the missing OI readout, root-shared prior, overlap, physical time step or laboratory accessibility. F11 permits a sufficiently accurate common return after overlap, so approximate recurrence is not dismissed as useless; its application would require those additional data.

## Gate 2 — Geometry and state count

**Verdict: finite geometric sections, and finite site support under an extra discrete site map; no closed dynamical patch.** The diagnostics in this gate do not cross Gate 1's unsupported implication. There are two distinct routes: an entropy interpretation requires H5; a literal finite-lattice interpretation requires H3 and then closure. Neither is supplied by the area formula alone.

### 2.1 Observer, region, time and site map

Fix 3+1-dimensional exact de Sitter with radius R = c/H, H > 0, and the geodesic observer γ at the origin. In the expanding flat chart,
$$ds^2=-c^2dt^2+a(t)^2d\mathbf x^2,\qquad a(t)=e^{H(t-t_0)}.$$
The region whose signals can reach γ at some future proper time is J^-(γ(+∞)); its section has comoving radius
$$\chi_{\rm event}(t)=\int_t^\infty c\,dt'/a(t')=R/a(t),$$
so physical radius a(t)χ_event(t) = R. This is an **event** horizon. For a finite experiment from p = γ(t_i) to q = γ(t_f), use the smaller causal diamond J^+(p) ∩ J^-(q), whose section radius is
$$\chi_D(t)=\min\left\{\int_{t_i}^{t}c\,dt'/a(t'),\int_t^{t_f}c\,dt'/a(t')\right\},\quad t_i\le t\le t_f.$$
The full eternal static patch is the diamond of the complete geodesic between its past and future endpoints. In its static coordinates the radius is r < R, with
$$ds^2=-(1-r^2/R^2)c^2dT^2+\frac{dr^2}{1-r^2/R^2}+r^2d\Omega^2.$$
The unbounded-time target would require one law for T ≥ 0 (and an inverse); a separate finite-diamond realization per pair (t_i,t_f) does not deliver it. For a merely asymptotic cosmology, R = c/H∞ is the limiting de Sitter radius, not today's apparent-horizon radius c/H0. GR:56 already distinguishes these horizons. H1 must be supplied independently: Λ > 0 alone neither establishes this global causal structure nor guarantees a vacuum stable forever. The observational benchmark below is conditional on a cosmological fit and does not observe the infinite future.

**Comoving lattice diagnostic.** Set x_n = ε0 n, n ∈ Z³, with ε0 > 0 fixed. The sites inside the future patch at t form
$$W(t)=\{n:|n|<R/[a(t)\epsilon_0]\}.$$
This set is finite at each finite t, and for t ≥ t0 its union is contained in W(t0). But its membership changes and its physical spacing grows as a(t)ε0. On all real t in the expanding chart, the union is infinite as t → -∞. On a fixed finite time interval, positive minimum spacing and bounded radius give finite support. Proof: a bounded Euclidean ball contains at most (2⌈R/(a_min ε0)⌉+1)^3 integer sites. This counting assertion does not preserve lost site records or identify the evolving W(t) with one autonomous reversible state space.

**Fixed physical spacing diagnostic.** For a flat spatial slice with physical positions r_n = ε_lat n, the ball contains
$$N_{\rm flat}=\frac{4\pi R^3}{3\epsilon_{\rm lat}^3}+O((R/\epsilon_{\rm lat})^2).$$
The estimate follows by surrounding each site with its lattice cube: only cubes within one cube diagonal of the spherical boundary affect the volume comparison. A fixed positive spacing, finite components per site and finite local alphabet give a finite instantaneous configuration set. This is a conditional mathematical count, not a derived physical lattice. Such sites cannot simultaneously keep fixed comoving labels and constant physical separations in an expanding universe. Keeping physical positions fixed requires a different congruence/transport rule; maintaining a comoving interpretation requires refinement or new variables. Neither a rule for that operation nor its reversible horizon memory is supplied here. Thus H-frame's comoving/free-fall reading and a time-independent Planck lattice cannot silently be identified for all future times.

**Foliation control.** The static T = constant section has proper volume
$$V_{\rm static}=4\pi\int_0^R\frac{r^2\,dr}{\sqrt{1-r^2/R^2}}=\pi^2R^3.$$
Substitute r = R sin θ to obtain the integral 4πR³∫_0^(π/2)sin²θ dθ. It is finite and is 3π/4 times the flat-slice ball volume. Dividing it by ε_lat³ is an alternative uniform-proper-density estimate, **not** the same cubic site map: the curved static slice does not carry the flat cubic tiling used by KM-1. Counts depend on the declared spatial slice and sampling rule. Both estimates are displayed to make the order of magnitude transparent; no equality of their microscopic dynamics is asserted.

### 2.2 Three different quantities and reproducible numbers

Use dimensionless entropy in nats, s_dS = S_dS/k_B. External semiclassical input H2 gives
$$s_{\rm dS}=\frac{A}{4l_p^2}=\frac{\pi R^2}{l_p^2},\qquad T_{\rm GH}=\frac{\hbar H}{2\pi k_B}.$$
For the scale comparison only, H4 gives ε = 2 sqrt(σ) l_p, ε_lat = sqrt(6σ) l_p and κ_m = 3/2 on the spherical single-link premises. **ε is the counting length**, not the lattice edge. These are OI's conditional calibrated relations, not independent support for A1 or an independently derived Planck-scale substrate.

Inputs: the historical flat-ΛCDM reference H0 = 67.4 km/s/Mpc and Ωm = 0.315 from the abstract of [Planck 2018 VI, 1807.06209v4](https://arxiv.org/abs/1807.06209v4); set ΩΛ = 1 - Ωm = 0.685, neglecting today's small radiation term for this illustrative scale estimate. Define the exact-de-Sitter benchmark H = H0 sqrt(ΩΛ). These are model-inferred values, not raw observations or a claim to the latest best fit. Constants use the central [CODATA 2022 values](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958143), with SI h, c and k_B exact. Their experimental uncertainty is immaterial to the area/volume hierarchy; the printed digits are reproducibility digits, not an uncertainty claim.

| Quantity | Value in the σ = 1 benchmark | Meaning |
|---|---|---|
| H; Λ = 3H²/c² | 1.807818 × 10^-18 s^-1; 1.090911 × 10^-52 m^-2 | External exact-de-Sitter benchmark |
| R; l_p; ε_lat | 1.658311 × 10^26 m; 1.616255 × 10^-35 m; 3.959000 × 10^-35 m | Geometry and conditional lattice scale |
| s_dS; s_dS/ln 2 | 3.307213 × 10^122 nats; 4.771300 × 10^122 bits | Horizon entropy, and its information-unit conversion |
| N_flat; alternative N_static | 3.078437 × 10^182; 7.253396 × 10^182 | Volume site estimates; hence the brief's rough 10^183 scale, with slice and coefficient explicit |
| N_modes = s_dS/σ | 3.307213 × 10^122 | Boundary modes under H4; not bulk sites or total configurations |

The three objects must remain distinct: **(a)** horizon entropy s_dS; **(b)** the number M of admissible microscopic configurations (whose maximum counting entropy would be ln M); **(c)** the observer's distinguishable records/capacity. Main:42–46 supplies a finite visible alphabet from its definition, not equality of all three. The book itself distinguishes total information from boundary accessibility at ch18:168. Reinterpreting a boundary capacity as a bound on all hidden configurations would be H5, a substantive addition.

For q alphabet values, K components per site and the selected second-order rule, there are 2K entries per site. If every entry can be independently set, the product count is
$$M_{\rm product}=q^{2KN_{\rm flat}},\qquad \ln M_{\rm product}=2KN_{\rm flat}\ln q.$$
Thus **10^183 is a site scale, not the configuration count**. For a conservative scalar K = 1, take q = 3 at σ = 1; this respects σ ≤ ln q. Using q = 2 with σ = 1 for a single boundary mode would violate GR:102's explicit constraint. The independent binary control instead uses σ = ln 2. The physical six-component reading K = 6 would multiply the scalar log-count by six and strengthen the tension; it is not needed for the obstruction.

Run the following with Python 3 and its standard library. No lattice enumeration or dynamical simulation is involved. The tests check the entropy-unit/counting relations, a separately simplified dimensionless volume/area ratio, the σ/alphabet constraint and the geometric scaling. They certify the calculation as written, not H1–H8.

```python
from math import pi, sqrt, log, isclose

c = 299792458.0
G = 6.67430e-11
h = 6.62607015e-34
k_B = 1.380649e-23
hbar = h / (2 * pi)
Mpc = 3.0856775814913673e22
H0 = 67.4 * 1000 / Mpc
Omega_L = 0.685
H = H0 * sqrt(Omega_L)
Lambda = 3 * H**2 / c**2
lp = sqrt(hbar * G / c**3)
R = c / H
A = 4 * pi * R**2
s = A / (4 * lp**2)
volume = 4 * pi * R**3 / 3

for name, value in [
    ("H_s-1", H), ("Lambda_m-2", Lambda), ("R_m", R),
    ("lp_m", lp), ("entropy_nats", s), ("capacity_bits", s / log(2)),
    ("T_K", hbar * H / (2 * pi * k_B)),
    ("thermal_time_s", 2 * pi / H),
]:
    print(name, f"{value:.6e}")

for sigma, q in [(1.0, 3), (log(2), 2)]:
    assert sigma <= log(q)
    eps = 2 * sqrt(sigma) * lp
    ell = sqrt(6 * sigma) * lp
    sites = volume / ell**3
    raw = 2 * sites * log(q)  # K = 1; two time slices
    ell_required = (2 * volume * log(q) / s)**(1/3)
    assert isclose(sites / s, 4 * R / (3 * (6*sigma)**1.5 * lp), rel_tol=1e-12)
    assert isclose((4*pi*(2*R)**3/3) / volume, 8, rel_tol=1e-12)
    assert isclose((pi*(2*R)**2/lp**2) / s, 4, rel_tol=1e-12)
    for name, value in [
        ("sigma", sigma), ("q", q), ("counting_length_m", eps),
        ("lattice_spacing_m", ell), ("sites_flat", sites),
        ("sites_static_volume", sites * 3*pi/4),
        ("raw_entropy_nats_K1", raw), ("raw_over_bound_K1", raw/s),
        ("independent_fraction_K1", s/raw),
        ("minimum_spacing_m_K1", ell_required),
    ]:
        print(name, f"{value:.6e}")
    assert abs(sigma * A / eps**2 / s - 1) < 1e-12
    assert abs((1.5*A/ell**2) / (s/sigma) - 1) < 1e-12
    print("controls PASS")
```

Expected output (last printed digit can depend on platform rounding):

```text
H_s-1 1.807818e-18
Lambda_m-2 1.090911e-52
R_m 1.658311e+26
lp_m 1.616255e-35
entropy_nats 3.307213e+122
capacity_bits 4.771300e+122
T_K 2.197696e-30
thermal_time_s 3.475564e+18
sigma 1.000000e+00
q 3.000000e+00
counting_length_m 3.232510e-35
lattice_spacing_m 3.959000e-35
sites_flat 3.078437e+182
sites_static_volume 7.253396e+182
raw_entropy_nats_K1 6.764017e+182
raw_over_bound_K1 2.045232e+60
independent_fraction_K1 4.889422e-61
minimum_spacing_m_K1 5.025350e-15
controls PASS
sigma 6.931472e-01
q 2.000000e+00
counting_length_m 2.691241e-35
lattice_spacing_m 3.296084e-35
sites_flat 5.334480e+182
sites_static_volume 1.256907e+183
raw_entropy_nats_K1 7.395159e+182
raw_over_bound_K1 2.236070e+60
independent_fraction_K1 4.472133e-61
minimum_spacing_m_K1 4.310160e-15
controls PASS
```

### 2.3 Consequence beyond bare finiteness: the independence restriction

If H5 imposes ln M ≤ s_dS on the whole physical patch, H6's product count violates that bound by a factor **2.045232 × 10^60 in log-count** already for K = 1, q = 3, σ = 1. Explicitly, if m independently assignable q-valued coordinates remain and every joint assignment is admissible, then M ≥ q^m and
$$m\le\frac{s_{\rm dS}}{\ln q},\qquad \frac{m}{2KN_{\rm flat}}\le\frac{s_{\rm dS}}{2KN_{\rm flat}\ln q}.$$
This gives the 4.889422 × 10^-61 fraction in the scalar benchmark. It is a bound on the count of independently assignable coordinates, **not** the fraction of all configurations retained, and not a prediction for real matter. Alternatively, retaining unrestricted independent scalar sites would require
$$\epsilon_{\rm lat}\ge\left(\frac{2K(4\pi R^3/3)\ln q}{s_{\rm dS}}\right)^{1/3},$$
about 5.0 × 10^-15 m for K = 1, q = 3. That contradicts the particular Planck-spacing/counting interpretation being tested; it is not an endorsed replacement spacing. The parametric conflict is volume versus area, N/s ∝ R/l_p, so rounding the cosmological inputs cannot repair it.

What can restrict the count? A physically selected invariant subset, gravitational constraints with a proved state count, a gauge quotient, or a non-product holographic encoding could do so in principle. None is constructed for the OI patch here, and the referenced quantum counts do not supply that map. Correlating probabilities while leaving every configuration admissible does **not** lower the cardinality. Conversely, if the horizon bound applies only to accessible entropy, there is no contradiction with a much larger hidden ontic space—but the bound then does not establish H5 or A1. This is a conditional inconsistency of **H3 + H4 + H5 + H6 at the benchmark**, not an unconditional contradiction of OI or holography. A4's finite periodic model remains unchanged.

## Gate 3 — Dynamical closure

**Verdict: NOT ESTABLISHED.** No cited external source supplies a horizon-inclusive OI configuration space and one autonomous bijection. There is a direct obstruction for the unchanged unrestricted finite-window restriction of NR-1's rule. It does not exclude an independently justified nonlocal horizon encoding or a constrained invariant carrier.

### 3.1 What the horizon does and does not supply

An event horizon is a null causal boundary, not a reflecting wall and not a periodic spatial identification. A matter packet can leave an observer's accessible region; its information is absent from a bulk-only later description. In the complete eternal static-patch diagram, incoming classical characteristics can originate on the **past** horizon and outgoing ones end on the **future** horizon. One must not describe that as arbitrary signals entering from beyond the observer's future event horizon. In semiclassical QFT the static observer detects Gibbons–Hawking thermality; that does not by itself amount to a specified classical stream of new independent inputs crossing the future horizon. Thermality can be the restriction of an entangled global state.

These distinctions matter for closure. An autonomous Hamiltonian description of observables in a static wedge can be formulated in QFT; an event horizon does not prove that **every** patch description is open. But that field algebra is not a finite ontic configuration set, nor does its existence prove that a bulk lattice restriction is a finite reversible factor. Complementarity proposes a complete patch description with horizon records, so that apparent loss to the horizon is encoded internally. It is motivated independently of OI (Gate 1), but the proposal must specify the variables, count, law, readout, preparation and reversible transport to meet this task's target. H7 cannot be silently substituted for H8.

### 3.2 Exact obstruction for a direct finite restriction

Take H14's full product configuration space X = (Z_q²)^(Z³) and F(u,v) = (αSu - v,u), where S is the nearest-neighbour sum and α ≠ 0 in Z_q. Let W be any finite nonempty set of sites and π_W the restriction of both time slices to W. **There is no map f on the W configurations satisfying π_W F = f π_W on all X.**

Proof. Choose w ∈ W with maximal first coordinate; z = w + e_1 lies outside W. Take x and y with identical previous/current values everywhere except for a unit change of u(z). Then π_W x = π_W y, but the first output at w changes by α ≠ 0. Thus π_W Fx ≠ π_W Fy, contradicting the asserted factorization. This proves failure of a deterministic autonomous restriction before asking about bijectivity. Adding any fixed finite halo gives the same argument on the enlarged finite set. The proof needs neither primality, Haar measure, convexity nor an assumed thermodynamic state. If α = 0, the sites decouple and the argument does not apply, as required by NR-1's control.

This is a negative result for **unrestricted product assignments, the unchanged rule and coordinate restriction**. It is not a proof about a cosmologically transported lattice with different propagation, a constrained subset where the two assignments are forbidden, or a holographic encoding. In particular, imposing a fixed geometric sphere on this rule has not been shown to respect de Sitter's null horizon. That missing site/geometry dynamics is H3/H7, not evidence that a genuine future event horizon transmits forbidden signals.

Replacing the excluded neighbours by fixed values, reflecting rules or torus identifications changes the map. Such a finite replacement may be bijective by its second-order form, but its agreement with the original dynamics lasts only while its boundary modifications cannot affect the readout. No physical justification for one of these replacements is added here.

### 3.3 What a valid reduction would need

Let F be a bijection of a proposed physical carrier X, and let π map X onto a finite set C. A necessary condition for an autonomous factor f is: πx = πy implies πFx = πFy. Necessity follows by applying f to the common value. If the same implication holds for F and F^(-1), define f(πx) = πFx and g(πx) = πF^(-1)x. Both are well-defined; fg(πx) = πx and gf(πx) = πx, so f is a bijection with inverse g. Conversely, if a bijective f satisfies πF = fπ, composition with F^(-1) and f^(-1) gives πF^(-1) = f^(-1)π, which gives the inverse compatibility as well. These directions establish the criterion separately.

For a finite admissible subset Y rather than a quotient, one needs F(Y) = Y; then restriction of the global bijection is bijective. Merely naming an entropy-bound subset, counting a shell, or discarding exterior sites proves neither invariance nor factor compatibility. Matching the actual observer's law additionally needs its readout and preparation distribution to descend correctly. H15 names these missing conditions without asserting that a physical Y or π exists.

### 3.4 NR-1 negative control: no boundary return imported from a torus

For NR-1's declared rule, two-slice window W and uniform/Haar priors, Prop. 4.1 gives equality of rooted maps through t only if
$$\operatorname{ext}_j(W)+2t<L\quad\text{for every coordinate }j.$$
Cor. 4.2 then locates any F11 near-return, under **nonnilpotent α**, at n ≥ (L - max_j ext_j(W))/2. With **prime q, nonzero α and lattice-convex W**, Theorem 3.3 excludes revival on the infinite lattice; any torus C4r/C4e witness must have its later time at or beyond the same bound. These are boundary-sensitive times, and the lower bounds diverge as L grows. A prewrap finite-cone match cannot transfer torus recurrence to the infinite rule.

The qualifications are essential. NR-1 Prop. 5.1 gives exact periods for nonzero nilpotent α on suitable composite alphabets; a nonzero nilpotent **primary component** can supply revival even in a mixed composite case with a propagating unit component. The witness lies in the bounded-support component. The general nonconvex and prime-power-unit revival questions are not settled by the prime/convex theorem. This record does not turn the torus bound into an arbitrary-q no-go.

What demonstrably distinguishes a physical horizon from the torus cut is its null causal geometry, thermality under the external quantum assumptions, and lack of spatial wraparound. None of these facts specifies a return channel that restores the lost root information. What would distinguish it **dynamically** in the required sense is an explicit physical horizon encoding satisfying §3.3, the entropy constraint and observed readback tests. That evidence is missing. Simply placing the cut at radius c/H does not change the restriction obstruction or prove that a finite torus models the horizon.

## Gate 4 — Recurrence and consequences

**Not entered:** closure of the physical OI patch has not been established. No de Sitter recurrence theorem, exact common period, recurrence timescale for an OI update, Boltzmann-brain population or restored physical chain is computed. The following is the required downstream **scope check**, not execution of the stopped positive branch.

| Chain | Bearing of this record and first remaining requirements |
|---|---|
| Recurrence-scale P-indivisibility | **Not recovered.** Main:121's finite-permutation return has not been physically supplied. H8, a compatible root-shared prior and earlier non-permutation map are absent. A1-10 F11 is a separate sufficient route: same-time return error ε with 2ε smaller than the earlier overlap mass. Approximate quantum recurrence might support it only after the missing quantum/OI law and time map are established; exact return is not logically necessary for every P-indivisibility route. |
| P8, observer selection / arrow | **Not recovered.** Even a finite bijection would not establish EM, local equilibrium, the fast-mixing rate, uniform erosion or the use of (PUP)^n for the exact compressions PU^nP. Main:746–762 explicitly separates these. The GH thermal scale is not the fast warm-bath scale used in the illustrative brain estimate. |
| P12(b), observer-level / physical reconstruction | **Not recovered.** No common carrier, law, readout or cross-window gluing has been supplied. A1-free local gauge algebra and per-window reversible realizations retain their existing status; they do not identify a physical de Sitter realization. [Substratum:121–139](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Substratum.md#L121-L139), [A1 recovery matrix, P12(b)](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md#L39-L60). |
| GR:58, H-count / horizon counting | **Not recovered.** Finite area, finite site support or an entropy ceiling does not select an invariant microcanonical law, conserved horizon energy, weak-coupling factorization, the energy-dependent density of states or its detector match. The P7-B countercontrol varies the slope with the same finite boundary. H4's calibration cannot prove the A1 condition it already uses. |

**Boltzmann brains and time direction.** DKS's fluctuation problem and BFP's apparatus limitation remain conditional external comparisons, not OI predictions. The inline calculation gives T_GH = 2.20 × 10^-30 K and ħ/(k_B T_GH) = 2π/H = 3.48 × 10^18 s. Even identifying this with a memory time would require an extra dynamical assumption. It does not supply τ_mix ≪ τ_S for laboratory or brain processing; Main:760 expressly records this point. A warm fluctuation's local bath, protected modes and preparation would have to be assessed separately; no universal brain exclusion follows from horizon temperature. Main:758's anti-brain statement is restricted to EM, its rate/erosion conditions and iterated-compression description. Exact de Sitter also has dA/dt = 0, so its horizon area supplies no strictly increasing clock. This is consistent with the background qualification at [ch02:192–196](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/book/ch02-substratum.md#L192-L196); finite reversibility alone selects no time direction or low-entropy preparation.

**Corpus search and limit.** Searches for `Boltzmann`, `anti-Boltzmann`, `past hypothesis`, `past-hypothesis`, `de Sitter`, `complementarity`, `horizon`, `finite` and `recurrence` covered the available textual corpus in papers, book (including FULL), verification records and Lean sources. The principal brain mirrors inspected are [Complexity:212](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/papers/Complexity.md#L212), [ch03:58–62](https://github.com/amaybaum/incompleteness/blob/59d063784a2640fab2533660e4f96bcc9bc09b09/book/ch03-structural-realism.md#L58-L62), ch02:192–196 and their FULL copies. Their claims must retain Main's conditional scope. This is a check of this route, not a new exhaustive inventory of every A1 consumer. No broader manuscript reclassification or correction is made. REC-1 Props 3.6′–3.8 remain conditional results on visible periodicity/rigidity under their normalized-law contract; they do not supply the patch or its law and are not prerequisites passed here.

## Result and open questions

**Verdict class:** at most **F4-type causal finiteness, not A1**, conditional on a discrete site map on a declared window; additionally, **negative results for specified classes** (finite entropy as a cardinality argument, generic finite-unitary to exact finite-permutation inference, and direct coordinate restriction of the unchanged unrestricted NR-1 rule). There is **no conditional patch-A1 recovery from independently supported de Sitter inputs** in this record. Merely assuming H8 would repeat the target.

The strongest positive statements are conditional geometric/site counts, a quantitative necessary restriction on independent bulk assignments if H5 is imposed, and the exact criterion a finite reversible factor must satisfy. Starting with external H1/H2, the entropy route stops at the missing universal microscopic-count interpretation H5/H8. The literal lattice route also needs H3 and then fails to establish H7/H15. Finite quantum dimension, even if independently established, would still not imply the target exact finite permutation. None of these findings proves global A1 false or excludes every horizon completion.

**Consequence beyond finiteness (§A.29).** An unrestricted Planck-spacing bulk product and a complete-patch area entropy budget cannot both hold in the specified benchmark: the scalar log-count already exceeds the budget by about 2 × 10^60. Any candidate using both must supply a restriction/encoding with the quantified reduction and prove its preservation by dynamics. This is an independently checkable consistency constraint on that interpretation, not a novel empirical prediction. No Layer-0 revision or new physical premise has been proposed for adoption, so no physical-prediction credit is taken.

Open questions, accountable to #1353 under #1169:

1. Does a specified external quantum-gravity construction give a justified finite **ontic** patch representation and the required observer laws, rather than only an entropy or Hilbert dimension? What claim of exactness and time domain is physically supportable?
2. What site congruence, spacing history and horizon transport implement the OI update while respecting causal geometry? Can H3 be supplied without changing A4 or importing an unproved lattice identification?
3. What constraints or quotient enforce the area budget if it applies to the complete carrier? Prove invariance or the two factor-compatibility directions in §3.3, and preservation of physical readouts and preparations.
4. What independently justified memory and observer-lifetime bound permits a usable rooted return? No recurrence timescale, overlap or experimental discrimination is supplied by the entropy count alone.
5. If a patch is eventually established, recheck P8, P12(b) and GR:58 separately with their full premises. A local patch theorem would not establish global A1.

**Verification and preservation.** The count script reproduces the printed values and controls; paper proofs are fully given here. No physical simulation, new Lean theorem or empirical test was run. New scientific claims await independent non-author exact-head review on #1354. The evidence inherited from main is distinguished from newly proved paper countercontrols; reading the NR-1 record is not a rerun of its computation. Local artifact-placement and V3 self-tests pass; full-history V3/legacy checks cannot decide ancestry in the deliberately shallow checkout and remain for ordinary PR CI. The PR records the actual CI conclusions. For every current verification gap, the remediation is the missing independent proof review or the expressly named physical input above, under #1353; listing it authorizes no new programme. A future preservation proposal would retain the nonredundant closure obstruction and reproducible area/volume constraint with these limits, and require separate owner merge authorization. #1354 and any CI/review links are review provenance, not substitutes for the proofs in this file.

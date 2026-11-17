# A1-DS — Does de Sitter physics supply a finite, closed, reversible OI system?

## Status

**Paper-only check, not yet independently reviewed.** First substantive checkpoint: literature assessment and two exact countercontrols; geometry, counts and the remaining scope audit are in preparation. Sole scientific writer: Codex in the owner-authorized session of 2026-11-17. A separate non-author reviewer must inspect the pushed exact head. Paper proofs are not Lean certification or empirical verification. **A1 is OPEN / UNADOPTED; A4 is unchanged; physical source is NOT PASSED.**

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

## Gate 1 — Literature and non-circularity

**Verdict: the external evidence supplies conditional geometry and thermodynamics, not the OI target. The first unsupported implication is finite horizon entropy → a finite complete configuration set.** Even granting a finite Hilbert space as an additional external input leaves a second, exact dynamical obstruction below. No new premise is adopted to pass either gap.

Primary papers were searched on the web and read first-hand as PDFs; page numbers in the following table are the papers' printed pages. The claims are attributed to their actual scope, rather than inferred from abstracts.

| Source and exact locator | What it establishes or proposes; limit relevant here |
|---|---|
| T. Banks and W. Fischler, *M-theory observables for cosmological space-times*, [hep-th/0102077v1](https://arxiv.org/abs/hep-th/0102077v1), introduction p. 3 and §5, pp. 17–21 | Motivates a finite-dimensional asymptotic-de-Sitter quantum description and observer complementarity. This is a proposed framework, not a derivation of a finite ontic lattice or an OI permutation. Its patch-dependent quantum observables are not identified with independently settable OI sites. |
| R. Bousso, *A Covariant Entropy Conjecture*, [hep-th/9905177v3](https://arxiv.org/abs/hep-th/9905177v3), §2, pp. 5–9 | Bounds entropy on suitable null light-sheets by the initial area under the conjecture's conditions. It is not an arbitrary spatial-volume cell count and supplies no autonomous update. |
| R. Bousso, *Positive Vacuum Energy and the N-bound*, [hep-th/0010252v2](https://arxiv.org/abs/hep-th/0010252v2), §1.1 pp. 1–3, §2.3 pp. 8–9, §5 pp. 13–17, §6 pp. 18–19 | Distinguishes the finite-Hilbert proposal from its entropy consequence; uses causal diamonds. The §5 argument invokes the covariant and D-bounds and is explicitly restricted to spherical symmetry at p. 17. Its conclusion is not an unrestricted proof that Λ > 0 makes all ontic configurations finite. |
| L. Dyson, M. Kleban and L. Susskind, *Disturbing Implications of a Cosmological Constant*, [hep-th/0208013v3](https://arxiv.org/abs/hep-th/0208013v3), §1 pp. 1–5, §3 | Assumes an isolated unitary causal patch motivated by holography/complementarity and analyzes equilibrium fluctuations and problematic cosmological histories. Its equilibrium recurrence estimate is not an exact common permutation order. The troubling histories are consequences of its assumptions, not evidence that those assumptions hold. |
| N. Goheer, M. Kleban and L. Susskind, *The Trouble with de Sitter Space*, [hep-th/0212209v3](https://arxiv.org/abs/hep-th/0212209v3), §§3–5 pp. 7–11 | Gives a symmetry obstruction under its quantum finite-entropy/discrete-spectrum implementation of exact de Sitter symmetry. Its discussion includes metastability and operational limits. It does not prove every finite approximate patch impossible, nor universal decay of every positive-Λ cosmology. |
| T. Banks, W. Fischler and S. Paban, *Recurrent Nightmares? Measurement Theory in de Sitter Space*, [hep-th/0210160v2](https://arxiv.org/abs/hep-th/0210160v2), §§4–5 pp. 9–16 | Argues, under its finite-quantum-system and apparatus assumptions, that reliable measurements cannot verify the formal recurrence regime. Operational accessibility must therefore be checked separately from mathematical recurrence. This is not a new OI observer theorem. |
| V. Chandrasekaran, R. Longo, G. Penington and E. Witten, *An Algebra of Observables for de Sitter Space*, [2206.10780v5](https://arxiv.org/abs/2206.10780v5), §§1.1–1.3 pp. 2–7 | Constructs a Type II₁ observable algebra in the small-G limit, with a maximum renormalized entropy. The algebra is not a finite matrix algebra; the finite-Hilbert interpretation and its limit are distinguished. This supports keeping entropy, dimension and ontic cardinality separate; it does not disprove a finite microscopic completion. |

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

Pending at this checkpoint. The comparison will keep fixed physical spacing distinct from fixed comoving spacing, and horizon entropy distinct from independent configurations and observational capacity. No result from this gate is yet asserted.

## Gate 3 — Dynamical closure

Pending as a scoped diagnostic of the missing implication. The literature's unitary-patch proposal does not yet specify the required OI system.

## Gate 4 — Recurrence and consequences

**Not entered:** closure of the physical OI patch has not been established. No recurrence-scale or downstream recovery is claimed.

## Result and open questions

At this checkpoint, the positive inference stops at finite horizon entropy → finite complete configuration set. A separate exact countercontrol shows why even finite quantum dimension and unitarity do not entail the target finite permutation. No A1-dependent chain is restored. The remaining record will quantify the volume/area tension, test direct patch restriction, preserve NR-1's scope and audit the downstream claims without crossing this stop.

Open obligations remain with #1353/#1169: a physical site map, admissible configurations and entropy interpretation; autonomous horizon-inclusive dynamics; a fixed observer law; and any justified downstream application. Independent non-author review and ordinary CI are pending. Preservation, if later proposed, would retain the scoped obstruction and reproducible diagnostics; it would need separate owner authorization and would adopt no premise.

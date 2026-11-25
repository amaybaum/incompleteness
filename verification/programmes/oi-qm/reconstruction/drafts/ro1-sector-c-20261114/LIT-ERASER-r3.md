# LIT-ERASER, r3: first-hand reading of the eraser and complementarity literature cited by S3-U4

**Purpose.** Record what the performed which-path and quantum-eraser experiments, and the
complementarity relations, cited by S3 unit U4 (`S3-U4-r1.md`, §§4.2, 5, 6.2–6.3, 7, 8) and its
source inventory (`U4-SOURCES-r1.md`, §5) actually state and measure, with raw-direct observables
separated from inferred ones (§A.24). For each U4 literature claim, record whether the sources read
support it. This note assesses attributions only; it does not assess U4's OI-internal reasoning,
adopts no premise, and changes no classification.

**Authorization.** Owner `amaybaum`, 2026-11-15, Issue #1169 comment 6891511297, item (2a):
first-hand reading of the quantum-eraser and complementarity literature U4 relies on, and recording
what the performed experiments actually measured (raw-direct observables). Paper-only: no repository
edits, commits, pushes, Issue changes, computation or Lean.

**Read date.** 2026-11-15. **Writer:** Claude. **Review:** r1 reviewed in `REVIEW-LIT-ERASER-r1.md`
(ACCEPT WITH CHANGES); this revision applies that review's required changes and clarifications and
two of its advisory points, as listed in `RESPONSE-LIT-ERASER-r1.md`. r3 applies the one required wording fix of the r2 review,
as listed in `RESPONSE-LIT-ERASER-r2.md`. Nothing else is changed.

**Method.**
- Full texts were read only where an open preprint exists: arXiv PDFs were downloaded and converted
  to text, and the converted text was read in full by the writer (figures through their captions and
  axis labels). The arXiv version is the version read; where it is a submitted version, differences
  from the published version are possible and are flagged where a secondary source disagrees.
- Abstracts of paywalled items were read from the INSPIRE-HEP API and the OpenAlex API (both carry
  the publisher's abstract) and from the publisher's article page on nature.com. The APS site
  (journals.aps.org) was not reachable from the reading environment (connection refused or a
  challenge page), so no APS full text or APS page was read directly.
- Bibliographic data were checked against Crossref and the arXiv API.
- Secondary sources (reviews describing an experiment) are used only where marked **SECONDARY**, and
  never as a substitute for the primary's own statement.
- Status labels: **FULL** (whole text read, version stated); **ABSTRACT** (abstract only);
  **SECONDARY** (content taken from a named review that describes the paper); **NOT READ**.
- Nothing below is invented; where a number or statement was not found in a text read, it is marked
  "not reported in the version read" or NOT READ.

***

## 1. Per-paper records

### 1.1 Scully & Drühl 1982

| Field | Record |
|---|---|
| Citation | M. O. Scully, K. Drühl, "Quantum eraser: A proposed photon correlation experiment concerning observation and 'delayed choice' in quantum mechanics", *Phys. Rev. A* 25(4), 2208–2213 (1982), doi:10.1103/PhysRevA.25.2208 |
| URL read | https://inspirehep.net/api/literature?q=doi:10.1103/PhysRevA.25.2208 (abstract); https://arxiv.org/abs/1407.2930 §II.E (SECONDARY) |
| Read status | ABSTRACT; SECONDARY (Ma–Kofler–Zeilinger 2016) |
| Raw-direct observables | None: a proposal and analysis, not a performed experiment. The title names the observable class: a photon-correlation (joint-detection) experiment |
| Key numbers | None |
| Paper's own claim (abstract) | "We propose and analyze an experiment designed to probe the extent to which information accessible to an observer and the 'eraser' of this information affects measured results. The proposed experiment could also be operated in a 'delayed-choice' mode." |
| Secondary description | Light scattered from two atoms with two-, three- and four-level schemes; in the four-level case a second photon φ carries the which-path record of γ; an electro-optical shutter, a photodetector and two elliptical cavities implement erasure, in a delayed-choice arrangement (RMP §II.E) |

### 1.2 Scully, Englert & Walther 1991

| Field | Record |
|---|---|
| Citation | M. O. Scully, B.-G. Englert, H. Walther, "Quantum optical tests of complementarity", *Nature* 351(6322), 111–116 (1991), doi:10.1038/351111a0 |
| URL read | https://www.nature.com/articles/351111a0 (abstract); https://arxiv.org/abs/1407.2930 §II.E (SECONDARY) |
| Read status | ABSTRACT; SECONDARY |
| Raw-direct observables | None: a proposal (gedanken experiment with micromaser cavities as which-path detectors for an atomic beam). No experiment was performed in this paper |
| Key numbers | None |
| Paper's own claim (abstract) | "Simultaneous observation of wave and particle behaviour is prohibited, usually by the position–momentum uncertainty relation. New detectors, constructed with the aid of modern quantum optics, provide a way around this obstacle in atom interferometers, and allow the investigation of other mechanisms that enforce complementarity." |
| Secondary description | Two micromaser cavities before a double slit; a photon left in one cavity marks the path; a detector wall between two electro-optic shutters performs erasure; with shutters closed, no interference; with both open, fringes or antifringes appear "only ... in coincidence with the corresponding photon projections" (RMP's wording). The RMP's statement that loss of interference holds "independent of whether an observer takes note of it" is the review's gloss, not a quotation of SEW read here |

### 1.3 Englert 1996

| Field | Record |
|---|---|
| Citation | B.-G. Englert, "Fringe Visibility and Which-Way Information: An Inequality", *Phys. Rev. Lett.* 77(11), 2154–2157 (1996), doi:10.1103/PhysRevLett.77.2154 |
| URL read | https://inspirehep.net/api/literature/439199 (abstract, source APS); https://arxiv.org/abs/1305.0861 (F. De Zela, comment, FULL; restates the proof's structure) |
| Read status | ABSTRACT (primary); the comment read FULL |
| Raw-direct observables | None: a theoretical inequality |
| Key numbers | None |
| Paper's own claim (abstract) | "An inequality is derived according to which the fringe visibility in a two-way interferometer sets an absolute upper bound on the amount of which-way information that is potentially stored in a which-way detector. In some sense, this inequality can be regarded as quantifying the notion of wave-particle duality. The derivation of the inequality does not make use of Heisenberg's uncertainty relation in any form." |
| From the comment (FULL) | The relation `D² + V² ≤ 1` "was first derived by Jaeger, Shimony and Vaidman" (*Phys. Rev. A* 51, 54 (1995)) and independently by Englert. Englert's proof uses `D ≤ Σ_k D_k √(1−|u_k|²)` and `V = |Σ_k D_k u_k|`; the comment identifies a "slight technical flaw" (an unproved bound on a bracketed term) and repairs it; "Neither the physical content of (1) nor its validity is thereby questioned." |

### 1.4 Kwiat, Steinberg & Chiao 1992

| Field | Record |
|---|---|
| Citation | P. G. Kwiat, A. M. Steinberg, R. Y. Chiao, "Observation of a 'quantum eraser': A revival of coherence in a two-photon interference experiment", *Phys. Rev. A* 45(11), 7729–7739 (1992), doi:10.1103/PhysRevA.45.7729 |
| URL read | https://api.openalex.org/works/doi:10.1103/PhysRevA.45.7729 (abstract, from APS) |
| Read status | ABSTRACT. Full text NOT READ (paywalled; no preprint located) |
| Raw-direct observables (per abstract) | Coincidence detection in a Hong–Ou–Mandel interferometer. Marking: a half-wave plate in one arm rotates polarization by 90°. Erasure: "two polarizers in front of our detectors", i.e. after the output beam splitter. Interference reappears "upon coincidence detection". Visibility reported as a function of the relative orientation of the polarizers, with theoretical curves |
| Key numbers | NOT READ |
| Paper's own claim (abstract) | The eraser "removes this information from the state vector, after the output port of the interferometer, but in time to cause interference effects to reappear upon coincidence detection"; "the degree of erasure (which determines the visibility of the interference) depends on the relative orientation of the polarizers"; "pasting together" two paths "can introduce a new relative phase between them" |
| Notes | The interference observable of a Hong–Ou–Mandel setup is itself a two-photon coincidence rate; the erasure acts as a polarization filter on both detected photons. No delayed-choice arrangement is described in the abstract. "Revival of coherence" in the title denotes recovery of coincidence interference by polarization filtering, not an autonomous return of coherence |

### 1.5 Herzog, Kwiat, Weinfurter & Zeilinger 1995

| Field | Record |
|---|---|
| Citation | T. J. Herzog, P. G. Kwiat, H. Weinfurter, A. Zeilinger, "Complementarity and the Quantum Eraser", *Phys. Rev. Lett.* 75(17), 3034–3037 (1995), doi:10.1103/PhysRevLett.75.3034 |
| URL read | https://inspirehep.net/api/literature?q=doi:10.1103/PhysRevLett.75.3034 (abstract); https://arxiv.org/abs/1407.2930 §IV.A (SECONDARY) |
| Read status | ABSTRACT; SECONDARY. Full text NOT READ |
| Raw-direct observables | NOT READ. Per the RMP: photon pairs from type-I down-conversion; polarization and time delay as markers; wave plates and narrow-bandwidth interference filters as erasers; remote measurements on one photon reveal or erase which-path information of the other |
| Key numbers | NOT READ |
| Paper's own claim (abstract) | "various experiments demonstrating the mutual exclusivity of observing interference and which-path information ... no which-path measurements need to be performed on the interfering photon itself. Instead the other photon can be used to introduce distinguishability, which consequently destroys interference. However, a suitable measurement erases this distinguishability and interference can be recovered." |
| Open point | Whether the recovered interference is in coincidences or in single counts, and with what visibilities, is not determinable from the abstract |

### 1.6 Kim, Yu, Kulik, Shih & Scully 2000

| Field | Record |
|---|---|
| Citation | Y.-H. Kim, R. Yu, S. P. Kulik, Y. Shih, M. O. Scully, "Delayed 'Choice' Quantum Eraser", *Phys. Rev. Lett.* 84(1), 1–5 (2000), doi:10.1103/PhysRevLett.84.1 |
| URL read | https://arxiv.org/abs/quant-ph/9903047 (v1, 13 Mar 1999, "submitted to PRL", titled "A Delayed Choice Quantum Eraser"); published abstract via https://api.semanticscholar.org (DOI record) |
| Read status | FULL (arXiv v1, submitted version). Published version NOT READ |
| Raw-direct observables | Joint-detection (coincidence) counts `R01, R02, R03, R04` between the signal detector `D0` and idler detectors `D1–D4`, as functions of `D0`'s transverse position (0–3 mm). The four rates were "recorded at the same time during one scanning of D0". Singles at `D0` (the unsorted signal pattern) are **not reported**. No integration time, error bars or visibility number appear in the text read |
| Setup (as read) | 351.1 nm pump through a double slit onto a type-II BBO at two regions A, B (width ≈0.3 mm, centre separation ≈0.7 mm); signal to `D0` in the focal plane of lens `LS`; idler to beam splitters `BSA`, `BSB` (transmission → `D3`/`D4`, which-path) or via `BS` (→ `D1`/`D2`, erasing). Idler optical path longer by ≈2.5 m, so idler detection is "at least 8ns later" than signal registration; detector response ≈1 ns. The "choice" is passive: random transmission or reflection at `BSA`/`BSB` |
| Key results | Fig. 3/4: `R01` and `R02` show double-slit interference with a π phase shift between them. Fig. 5: `R03` shows "an absence of interference"; `R04` stated to show "no significant difference" from `R03` "except the small shift of the center" (not plotted). Peak coincidence counts ≈ 140 per point (axis scale). Theory: `R01 ∝ sinc²(xπa/λf) cos²(xπd/λf)`, `R02 ∝ sinc² sin²`; finite detector size and pump divergence reduce the visibility "to the level close to the observation" (no number given). The sum `R01 + R02` is not compared with any unsorted pattern |
| Paper's own claim | "The experimental results demonstrate the possibility of observing both particle-like and wave-like behavior of a light quantum via quantum mechanical entanglement. The which-path or both-path information of a quantum can be erased or marked by its entangled twin even after the registration of the quantum." Published abstract adds "(where the 'choice' is made randomly by a photon at a beam splitter)" |
| Commonly attributed vs paper | Popular accounts attribute to this experiment a change of `D0`'s own pattern by a later choice. The paper reports only coincidence rates sorted by the idler outcome; it reports no `D0` singles pattern and makes no claim that singles depend on the idler's fate |
| Discrepancy flagged | The RMP review (SECONDARY) describes the source as type-I down-conversion with momentum entanglement and the extra idler path as ≈2.3 m (7.7 ns); the arXiv v1 text read states type-II BBO with a Glan-Thompson prism and ≈2.5 m (8 ns). The published text was not read; which description it carries is unresolved. arXiv carries v1 only. The reviewer of r1 reports a web-search summary of a copy of the published PRL giving "7.7 ns"; that copy was not opened by the reviewer or by the writer, so the published figure is NOT READ |

### 1.7 Walborn, Terra Cunha, Pádua & Monken 2002

| Field | Record |
|---|---|
| Citation | S. P. Walborn, M. O. Terra Cunha, S. Pádua, C. H. Monken, "Double-slit quantum eraser", *Phys. Rev. A* 65(3), 033818 (2002), doi:10.1103/PhysRevA.65.033818 |
| URL read | https://arxiv.org/abs/quant-ph/0106078 (v1, 13 Jun 2001) |
| Read status | FULL (arXiv v1). Published version NOT READ |
| Raw-direct observables | Coincidence counts between `Ds` (scanned, −4 to +4 mm) and `Dp`, per fixed integration time. No singles patterns reported. No numerical visibilities reported; patterns given as plotted counts |
| Setup (as read) | 351.1 nm Ar laser (≈200 mW), 1 mm type-II BBO; polarization-entangled pairs; double slit (200 µm openings, 200 µm separation) at 42 cm in path s, with quarter-wave plates QWP1, QWP2 (fast axes orthogonal) in front of the slits as markers; polarizer POL1 in path p as eraser; `Ds` at 125 cm, `Dp` at 98 cm (non-delayed) or 2 m (delayed erasure); 1 nm filters; Bell-inequality tests performed beforehand (no values given) |
| Key results | Fig. 2 (no QWPs, no POL1, 400 s): interference. Fig. 3 (QWPs in, POL1 absent, 400 s): "Nearly all interference ... was destroyed. The residual interference present is due to a small error in aligning the quarter-wave plates." Fig. 4 (POL1 at θ, 800 s, time "doubled in order to compensate for the decrease in coincidence counts"): fringes. Fig. 5 (POL1 at θ+π/2, 800 s): antifringes. "The averaged sum of these two interference patterns gives a pattern roughly equal to that of figure 3." Figs. 6–9 (delayed erasure, `s` detected before `p`; 500 s and 1000 s): "comparable" results |
| What was not done | No active or delayed choice: "there is no 'choice' available to the observer in the time period after the detection of photons s and before the detection of photon p." A path readout (polarization of both photons) is described theoretically in §III.A ("This can be verified experimentally") but no path-sorted data are reported among the results |
| Paper's own claim | "The which-path marker's presence alone is sufficient to make the two terms ... orthogonal ... it is enough that the which-path information is available to destroy interference"; erasure is recovered "by correlating the particle detection with an appropriate measurement on the which-path markers"; in delayed erasure, "the order of detection is not important" |

### 1.8 Ma et al. 2013 (PNAS)

| Field | Record |
|---|---|
| Citation | X.-S. Ma, J. Kofler, A. Qarry, N. Tetik, T. Scheidl, R. Ursin, S. Ramelow, T. Herbst, L. Ratschbacher, A. Fedrizzi, T. Jennewein, A. Zeilinger, "Quantum erasure with causally disconnected choice", *Proc. Natl. Acad. Sci. USA* 110(4), 1221–1226 (2013), doi:10.1073/pnas.1213201110 |
| URL read | https://arxiv.org/abs/1206.6578 (v2, 29 Jan 2013, with supplementary information) |
| Read status | FULL (arXiv v2) |
| Scope note | This paper is a quantum eraser with active, space-like separated choice, not delayed-choice entanglement swapping. The entanglement-swapping experiment is a different paper (cited in this one as Ma et al., *Nature Phys.* 8, 480–485 (2012)); NOT READ |
| Raw-direct observables | Time tags of all four detectors, recorded by two independent units and matched afterwards within a 1 ns window. Reported quantities are counts of the system photon at Det 1/Det 2 **conditioned on detection of the environment photon at Det 4**, for each basis setting. Path probabilities measured by blocking one path. No unconditional (unsorted) system-photon pattern is reported |
| Setup (as read) | Hybrid path–polarization entangled pairs, `(|b⟩_s|V⟩_e + |a⟩_s|H⟩_e)/√2`. Vienna: environment photon via 55 m fibre to a lab 50 m away; an EOM switched by a quantum random number generator in a third lab selects H/V (path information) or R/L (erasure); system photon delayed by 28 m fibre into a 2 m fibre interferometer. Six space-time scenarios, including projection of the environment photon space-like separated from, and time-like after, the system photon's interferometer events. Canary Islands: 144 km free-space link; in one arrangement the choice occurs ≈450 µs after the system-photon events in the source frame |
| Key numbers | H/V setting, outcome V: `P(a|V) = 0.023(5)`, `P(b|V) = 0.978(5)`, `I(i) = 0.955(7)`; phase-insensitive counts. R/L setting, outcome R: `P(a|R) = 0.521(16)`, `P(b|R) = 0.478(16)`, `I(ii) = 0.077(22)`, conditional visibility `V(ii) = 0.951(18)`, with `V = (C_max − C_min)/(C_max + C_min)` on counts conditioned on Det 4; outcome L stated to give a π-shifted pattern (no number). 20 s per point. Table I, six scenarios: `I(i)` 0.953(9)–0.957(7), `V(ii)` 0.943(21)–0.952(18). Source: ≈5 kHz coincidences, ≈50 kHz singles; polarization-correlation visibilities 98.0 % (H/V) and 96.9 % (R/L) without background subtraction. Complementarity: `I² + V² ≤ 1` measured in sequential runs across EOM voltages, with the corrected curve `V = 0.95 √(1 − (I/0.97)²)`. Canary data after background subtraction (33 dB link attenuation) |
| Paper's own claim | "All results obtained indeed agree with the expectation within statistical errors"; "whether the correlations between two entangled photons reveal welcher-weg information or an interference pattern of one (system) photon, depends on the choice of measurement on the other (environment) photon"; "we should not have any naive realistic picture for interpreting quantum phenomena". The introduction states, as standard theory and not as a measured result of this paper: "The presence of path information anywhere in the universe is sufficient to prohibit any possibility of interference. It is irrelevant whether a future observer might decide to acquire it." |
| Note on the inequality used | Eq. (3), `I² + V² ≤ 1`, is called a "bipartite complementarity inequality": `I` is obtained from one measurement on the environment photon and `V` is the visibility **conditioned** on the outcome of a complementary measurement on it, in different runs. This is not the single-particle form, in which `V` is unconditional (§3) |

### 1.9 Ma, Kofler & Zeilinger 2016 (review; INV 5.13)

| Field | Record |
|---|---|
| Citation | X.-S. Ma, J. Kofler, A. Zeilinger, "Delayed-choice gedanken experiments and their realizations", *Rev. Mod. Phys.* 88, 015005 (2016), doi:10.1103/RevModPhys.88.015005 |
| URL read | https://arxiv.org/abs/1407.2930 (v3, 19 Mar 2016) |
| Read status | FULL for §II.E (delayed-choice quantum erasure), §III's complementarity relation passage, and §IV (realizations of delayed-choice quantum erasers); remainder not read |
| Role | Review; used here as SECONDARY for items 1.1, 1.2, 1.5, 1.6, 1.11 |
| Statements used | Single-particle relation `V² + D² ≤ 1` "where equality holds for pure states", tested by Jacques et al. 2008 with an adjustable beam splitter (Jacques et al. NOT READ). Kim et al.: "The 'choice' of observing interference or not was made randomly by photon 2". Dürr et al. 1998: see 1.11 |

### 1.10 Greenberger & Yasin 1988; Wootters & Zurek 1979

| Field | Greenberger & Yasin 1988 | Wootters & Zurek 1979 |
|---|---|---|
| Citation | D. M. Greenberger, A. Yasin, "Simultaneous wave and particle knowledge in a neutron interferometer", *Phys. Lett. A* 128(8), 391–394 (1988), doi:10.1016/0375-9601(88)90114-4 | W. K. Wootters, W. H. Zurek, "Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle", *Phys. Rev. D* 19, 473–484 (1979), doi:10.1103/PhysRevD.19.473 |
| URL read | https://inspirehep.net/api/literature?q=doi:10.1016/0375-9601(88)90114-4 | https://inspirehep.net/api/literature/152058 |
| Read status | ABSTRACT | ABSTRACT |
| Raw-direct observables | None (theory) | None (theory, with a proposed experiment) |
| Paper's own claim (abstract) | A measure of particle knowledge that "reflects one's ability to predict in which beam a neutron is located"; wave knowledge by fringe contrast; "simultaneous knowledge of both is determined by a single parameter (not an uncertainty relation)"; extended to partially coherent beams | Analysis of Einstein's recoiling-slit version; the interference pattern "proves to be surprisingly sharp even when the trajectories of the photons have been determined with fairly high accuracy"; "An information-theoretic approach ... leads to a quantitative formulation of Bohr's complementarity principle" |
| Commonly attributed | `P² + V² ≤ 1` with `P` an a-priori predictability (attribution in Schwindt et al. 1999 and the RMP); the exact form in the paper NOT READ | Cited as a precursor of `D² + V² ≤ 1`; per its abstract its formulation is information-theoretic, so the quadratic form is not this paper's statement as far as the abstract shows |

### 1.11 Dürr, Nonn & Rempe 1998 (Nature) and companion PRL

| Field | Record |
|---|---|
| Citation | S. Dürr, T. Nonn, G. Rempe, "Origin of quantum-mechanical complementarity probed by a 'which-way' experiment in an atom interferometer", *Nature* 395(6697), 33–37 (1998), doi:10.1038/25653. Companion: S. Dürr, T. Nonn, G. Rempe, "Fringe Visibility and Which-Way Information in an Atom Interferometer", *Phys. Rev. Lett.* 81(26), 5705–5709 (1998), doi:10.1103/PhysRevLett.81.5705 |
| URL read | https://www.nature.com/articles/25653 (abstract); https://inspirehep.net/api/literature?q=doi:10.1103/PhysRevLett.81.5705 (PRL abstract); https://arxiv.org/abs/1407.2930 §IV.B (SECONDARY) |
| Read status | ABSTRACT (both); SECONDARY for numbers. Full texts NOT READ |
| Raw-direct observables (SECONDARY) | Far-field spatial fringe patterns of atoms after a two-grating (standing-wave light) interferometer; internal hyperfine states `|2⟩`, `|3⟩`, manipulated by microwave π/2 pulses, used as a which-path detector |
| Key numbers (SECONDARY) | Without which-path storage: visibilities (75 ± 1) % at `t_sep` = 105 µs and (44 ± 1) % at 255 µs; with which-path information stored in the internal state, "the interference patterns vanished"; the path disturbance by the microwave pulses was "four orders of magnitude smaller than the fringe period". Whether the internal state was read out in the runs that show no fringes: NOT READ |
| Paper's own claim (Nature abstract) | "the 'back action' of path detection on the atom's momentum is too small to explain the disappearance of the interference pattern. We attribute it instead to correlations between the which-way detector and the atomic motion, rather than to the uncertainty principle." The RMP quotes the paper: "the mere fact that which-path information is stored in the detector and could be read out already destroys the interference pattern" (quotation not verified at source) |
| PRL abstract | "We focus on the case of incomplete which-way information and use the distinguishability D to quantify how much information is stored. For a given value of D, the fringe visibility V is limited by the duality relation D²+V²≤1. We have measured D and V independently. Combining the results, we find good agreement with the duality relation." Numbers NOT READ |

### 1.12 Schwindt, Kwiat & Englert 1999 (read in addition: a first-hand test of the D–V relation)

| Field | Record |
|---|---|
| Citation | P. D. D. Schwindt, P. G. Kwiat, B.-G. Englert, "Quantitative wave-particle duality and nonerasing quantum erasure", *Phys. Rev. A* 60(6), 4285–4290 (1999), doi:10.1103/PhysRevA.60.4285 |
| URL read | https://arxiv.org/abs/quant-ph/9908072 (v1, 23 Aug 1999, "to appear in Physical Review A") |
| Read status | FULL (arXiv v1) |
| Raw-direct observables | Single-photon Mach–Zehnder (670 nm, attenuated, count rates below 5×10⁴ s⁻¹), a half-wave plate in path 1 as which-way marker (polarization). `V` from maximum and minimum counts at detector 1 as path length is scanned, **with the polarization analyzer removed** (marker unread), background (100–400 s⁻¹) subtracted. Knowledge `K = 2L − 1` from path-blocked counts with the analyzer in place, detector-efficiency ratio 1.11 ± 0.01, Wootters–Zurek betting strategy, optimized basis |
| Key numbers | Pure input: mean `V² + K²` = 0.976 ± 0.017 over all settings; 0.998 at the minimum-visibility setting; intrinsic interferometer visibility ≈98 %; "V > 4.4% even though L > 99.9%". Nearly completely mixed input: `V² + K²` = 0.003 ± 0.001 (theory 0.017 ± 0.003). Partially mixed input, purity 0.65 ± 0.01. Uncorrected theory curve `V² + D² = 2 Tr(ρ²) − 1`, `ρ` the marker's density matrix |
| Paper's own claim | `V² + K² ≤ 1`; "The equality holds for pure initial states of the WWM, while the inequality applies to (partially-)mixed states"; `D = max{K}`, and a non-optimal measurement "may yield less, or even zero"; the eraser "sorts the photons into sub-ensembles ... each exhibiting high-visibility fringes" (fringes along one eigenmode, antifringes along the other); for mixed markers, fringes are recoverable "even when no which-way information is available to erase" |

### 1.13 Decoherence, revivals and recoherence in finite environments (U4 E-3; INV 5.22–5.25)

| Item | Status | What was read |
|---|---|---|
| Jaynes–Cummings collapse and revival (Eberly et al. 1980; Rempe, Walther, Klein 1987) | NOT READ | — |
| Brune et al., *Phys. Rev. Lett.* 77, 4887 (1996) | NOT READ (primary); SECONDARY via Schlosshauer 2019 | A Rydberg atom imprints a phase shift on a cavity coherent field (n̄ ≈ 10, χ up to 0.31π, overlap below 3×10⁻⁵); the decoherence of the resulting field superposition is probed by a second atom through the two-atom correlation `P_ee` |
| Hahn 1950; Loschmidt echo (Peres 1984; Jalabert & Pastawski 2001; Gorin et al. 2006) | NOT READ | — |
| M. Schlosshauer, "Quantum decoherence", *Phys. Rep.* 831, 1–57 (2019), doi:10.1016/j.physrep.2019.10.001, https://arxiv.org/abs/1911.06282 | Sections read (§2.6; the cavity-QED experiment section) | Classical noise averaged over realizations reduces off-diagonal terms, but "for an individual instance of the noise process ... the evolution is completely unitary ... no creation of entanglement between the system and an environment"; such dephasing can be undone locally ("the basis of the spin-echo method"); "Such a local reversal is not possible for decoherence resulting from environmental entanglement; 'undoing' decoherence to restore an (unknown) pre-decoherence state of the system will require appropriate measurements on the environment" |
| M. Schlosshauer, "Decoherence, the measurement problem, and interpretations of quantum mechanics", *Rev. Mod. Phys.* 76, 1267–1305 (arXiv journal-ref year 2004; INV gives 2005), https://arxiv.org/abs/quant-ph/0312059 | Recurrence passage read | For an N-spin environment (Zurek 1982), coherence "will reappear after a certain time τ_r, which can be shown to be very long and of the Poincaré type with τ_r ∼ N!"; for finite environments τ_r "always remains finite" |

***

## 2. U4 attribution check

Each entry quotes the U4 passage, then states the verdict against the sources read. MATCHES: the
sources read support the passage as written. PARTLY: some clauses are supported and others are not
reported, are inferred rather than measured, or are stronger than the sources. DOES NOT MATCH: a
source read contradicts it. NOT CHECKABLE: the sources needed were not read.

**C1. §5, row E-1** (sources: SEW 1991, Dürr–Nonn–Rempe 1998, Englert 1996). "Fringes are lost when
path information is stored in a marker that nobody reads; the loss tracks the markers'
distinguishability (`D² + V² ≤ 1`), not whether they are read."
**PARTLY.**
- Of the three cited sources, only Dürr–Nonn–Rempe 1998 is a performed experiment; SEW 1991 is a
  proposal and Englert 1996 a theorem. The performed-experiment content of the row rests on one
  item read at ABSTRACT and SECONDARY level.
- "Fringes are lost when path information is stored in a marker": supported by Dürr 1998 (abstract:
  loss attributed "to correlations between the which-way detector and the atomic motion"; SECONDARY:
  fringes vanished with the record stored in the internal state). Supported at FULL level by items
  not cited in the row: Walborn 2002 Fig. 3 (coincidences with `p` detected and no polarization
  analysis of either photon; the path label is the `s` photon's own polarization, set by the
  quarter-wave plates and correlated with `p` through the entanglement) and Schwindt 1999 (`V` measured with the analyzer removed, essentially zero at the
  full-marking setting).
- "that nobody reads": for Dürr 1998, whether the marker was read in the fringe-free runs was NOT
  READ. For Schwindt 1999 it holds (analyzer removed in the `V` runs). For Walborn 2002 Fig. 3 neither
  photon's polarization is analysed.
- "the loss tracks the markers' distinguishability (`D² + V² ≤ 1`)": an inequality bounds rather
  than tracks. Tracking (a one-to-one relation) holds for pure marker states, where the relation is
  an equality; Schwindt 1999 shows the mixed-marker case, where `V` and `K` are both near zero
  (`V² + K²` = 0.003 ± 0.001). Dürr's PRL abstract reports agreement with the inequality for
  incomplete which-way information, numbers NOT READ.
- "not whether they are read": matches Englert's abstract ("which-way information that is
  *potentially* stored") and the paper statements of Walborn ("it is enough that the which-path
  information is available") and Ma 2013's introduction. These are statements of theory; the
  experiments read support it in the sense that `V` measured without reading the marker is low
  when `D` is high.

**C2. §5, row E-2** (sources: Kwiat 1992, Herzog 1995, Kim 2000, Walborn 2002, Ma–Kofler–Zeilinger
2016). "The record is retained in an unread degree of freedom and later made accessible. The
unsorted pattern shows no fringes whatever the later choice; sorting by a complementary readout
gives fringes and antifringes summing to the unsorted pattern; sorting by a path readout gives none."
**PARTLY**, clause by clause:
- *Record retained, later made accessible*: matches Kim 2000 (idler in flight ≈8 ns after `D0`
  registration), Walborn 2002 delayed erasure (`p` detected after `s`), Ma 2013 (projection
  space-like or time-like after the system photon's events; ≈450 µs in the Canary arrangement). The
  retaining degree of freedom is a photon in flight; it is measured, not returned to the
  interfering system. Kwiat 1992 (abstract) is not a delayed arrangement. Herzog 1995 NOT READ.
- *Unsorted pattern shows no fringes*: shown in Walborn 2002 Figs. 3 and 7 as **coincidence counts
  with `p` detected and no polarization analysis of either photon**. Not reported in Kim 2000 (no `D0` singles, no
  marginal pattern) or Ma 2013 (only patterns conditioned on Det 4). Unsorted **singles** at the
  interfering detector are reported in none of the three delayed experiments read (Kim, Walborn,
  Ma). This is limited to those three: Schwindt 1999's `V` is unconditional data taken with the
  marker unread; Dürr 1998's atom patterns are unconditional (SECONDARY); whether the marker was
  read: NOT READ. Both are non-delayed arrangements (C1, C5(a)).
- *"whatever the later choice"*: no paper read reports the unsorted pattern per choice. Kim's choice
  is passive (random beam-splitter outcome), Walborn has none ("there is no 'choice' available"),
  Ma's is active (QRNG). As stated, the clause is the standard-QM (no-signalling) prediction, not a
  reported raw-direct observable: NOT CHECKABLE from the data read.
- *Fringes and antifringes summing to the unsorted pattern*: Walborn 2002 states "the averaged sum
  of these two interference patterns gives a pattern roughly equal to that of figure 3"
  (qualitative; fringe and antifringe data taken at 800 s against 400 s for Fig. 3). Kim 2000 shows
  π-shifted `R01`, `R02` but makes no sum comparison. Ma 2013 states the L outcome gives a π-shifted
  pattern, no sum. Kwiat 1992 and Herzog 1995 NOT READ beyond abstracts.
- *Path readout gives none*: matches Kim 2000 (`R03`, and `R04` as stated) and Ma 2013 (setting (i):
  `I(i)` = 0.955(7), phase-insensitive counts). Walborn 2002 reports no path-sorted data.
- *Source list*: Ma–Kofler–Zeilinger 2016 is a review, so it is secondary for this row; the primary
  with active choice is Ma et al. 2013 (1.8).
- Every recovered interference pattern in the experiments read is conditional on the
  detection outcome of the marker or of the partner photon correlated with it (or, in Kwiat 1992 per abstract, on transmission through polarizers before
  coincidence detection).

**C3. §5, row E-3.** "Coherence returns when the environment's conditional states re-overlap
(autonomous revival), or when an applied reversal undoes a dephasing; in Hahn's case the dephasing
is by static inhomogeneity with no record (CC7's class)."
**NOT CHECKABLE at primary level** (Jaynes–Cummings sources, Brune 1996, Hahn 1950 and the Loschmidt
sources NOT READ). At SECONDARY level the reviews read are consistent with it: finite environments
give finite recurrence times (Schlosshauer 2004); spin echo reverses dephasing from classical
inhomogeneity, which creates no system–environment entanglement (Schlosshauer 2019). One
qualification from the 2019 review bears on "applied reversal": a *local* reversal on the system
undoes classical dephasing only; reversing entanglement-type decoherence "will require appropriate
measurements on the environment" (the review's words, continuing "to gather information that has
leaked from the system"); that operations on the environment could serve instead is a writer's
inference, not stated in the review.

**C4. §5, closing paragraph.** "Delayed-choice erasers are performed parked-record experiments ... a
which-path record is held in a degree of freedom the experimenter does not read (an idler in
flight) and is later made accessible ... Its raw-direct outcome, as attributed: while the record is
unread, the unsorted pattern has no fringes; on access, the record sorts the data."
**PARTLY.**
- Held in an unread degree of freedom, later made accessible, and sorting on access: matches Kim
  2000, Walborn 2002 (delayed erasure) and Ma 2013.
- "while the record is unread, the unsorted pattern has no fringes": not a raw-direct observable
  reported by any of the three. In Walborn the fringe-free pattern is assembled from coincidences,
  i.e. after `p` is detected; Kim and Ma report no unsorted pattern. The statement is
  the standard-QM prediction for the interfering photon's marginal, not a reported measurement.
- The "access" in these experiments is a projective detection of the marker or partner photon, not a return of the
  record to a region from which it could be read again; the record is consumed at detection.

**C5. §6.3, the accessibility reading.** "E-2's delayed-choice erasers park a record in an unread
degree of freedom and later retrieve it, and the unsorted pattern shows no fringes while it is
parked (E-1, E-2; to verify first-hand). So the accessibility reading disagrees with performed
experiments as attributed."
**PARTLY.**
- Against the experiments read, the measured content that bears on this reading is: (a) `V` near
  zero measured with the marker unread, at full marking (Schwindt 1999, FULL; Walborn 2002 Fig. 3,
  FULL, coincidence level; Dürr 1998: unconditional (SECONDARY); whether the marker was read: NOT
  READ); (b) path-sorted patterns show no fringes after the
  record is measured (Kim, Ma).
- The specific configuration the reading needs, the interfering particle's **unsorted singles
  pattern recorded while the marker is in flight**, is not reported in Kim 2000, Walborn 2002 or
  Ma 2013 (versions read). The "while parked" clause therefore rests on (a), which concerns records
  that are unread but not specifically parked-then-retrieved, and on the theoretical marginal.
- Whether (a) disconfirms the accessibility reading depends on how that reading classifies a marker
  that is unread but readable in principle (as in Schwindt and Walborn). That classification is an
  OI-side definitional matter outside this note.

**C6. §6.2, QM-4.** "Return of a record and revival of coherence exclude each other. With `D` the best
path discrimination over the whole complement, `D² + V² ≤ 1` (Englert 1996, as cited at
PREREG:232–233). An intact return keeps `D` and `V` where they were; a revival raises `V` only by
lowering `D`."
**PARTLY.** See §3. The quoted inequality and its attribution match Englert's abstract and the
literature's usage (V unconditional; D the maximal stored which-way information). U4 §6.2 defines
`|E_L⟩`, `|E_R⟩` as "the state of the whole complement, hidden part included": these are pure
states, so in U4's own model the equality `D² + V² = 1` holds at every tick, and the mixed-complement
example of §3 lies outside that model. This note does not show QM-4 wrong in U4's model. The PARTLY
rests on two narrower points:
- (a) U4 cites the inequality where its argument uses the equality. "A revival raises `V` only by
  lowering `D`" follows from the equality, not from the inequality in general.
- (b) "Exclude each other" has two readings. As a statement about states (partial `D` and partial
  `V` cannot coexist) it is false even under the equality (`D = V = 1/√2`). As a statement about
  processes (`D` and `V` cannot both increase) it is true under the equality. Extending `D` from a marker to
"the whole complement" is U4's application, not Englert's wording; it is the same mathematics with
the detector taken to be the whole complement.

**C7. §6.2, QM-1.** "On return, a complementary readout of the record gives conditional fringes whose
full masses sum to the unsorted pattern (T4, PREREG:490–491); a path readout gives none."
**PARTLY** as an empirical attribution (U4 states it as a class (ii) derivation, which this note does
not assess). Empirically: the sum is reported qualitatively in one paper read (Walborn 2002,
"roughly equal"); not tested in Kim 2000 or Ma 2013. Schwindt 1999 states the same structure
("fringes" and "anti-fringes" along the two eigenmodes) for a single-photon marker.

**C8. §4.2, the empirical leg of the S-L3 branch.** "the candidate miss presupposes performed
experiments that restore *unconditional* fringes by reversing the marking interaction. The erasers
in the inventory ... are listed as sorting erasers or proposals; ... Whether a performed
reversal-type eraser exists, with what raw visibilities, is to verify first-hand."
**MATCHES for the items read; NOT CHECKABLE beyond them.** Scully–Drühl 1982 and SEW 1991 are
proposals. Every performed eraser read (Kim 2000, Walborn 2002, Ma 2013, Schwindt 1999 FULL;
Kwiat 1992 by abstract) recovers fringes conditionally, by sorting or filtering on a marker
measurement. In Schwindt 1999 the unconditional `V` changes with the marking wave-plate's setting,
which is a change of apparatus setting between runs, not a reversal of a marking already made. No
performed experiment restoring unconditional fringes by reversing the marking interaction was found
among the items read; this is not a finding that none exists. Unread candidates for this check:
U. Eichmann et al., *Phys. Rev. Lett.* 70, 2359 (1993) (light scattered from two ions; named as an
atomic erasure realization in the RMP review), NOT READ; and cavity-QED complementarity
experiments, in which which-path information is stored in a cavity field, among them Brune et al.
1996 (NOT READ) and P. Bertet et al., *Nature* 411, 166 (2001), doi:10.1038/35075517, of which only
the abstract was seen (https://www.nature.com/articles/35075517: a Ramsey interferometer with one
beam-splitting pulse a small coherent cavity field; fringe visibility increases with its mean
photon number). The abstract does not describe a reversal of a stored record; full text NOT READ.

**C9. INV 5.9 gloss "Two-photon eraser, 'revival of coherence'"** (title of Kwiat 1992).
**MATCHES** the title; the abstract shows that "revival of coherence" there means recovery of
coincidence interference by polarizer filtering after the output port, not an autonomous return of
coherence of the kind in E-3. Any use of the phrase as evidence for revivals would not match.

**C10. Identity of the Ma et al. items (INV 5.13; PNAS 110, 1221).**
PNAS 110, 1221 (2013) is the eraser with causally disconnected choice (1.8), not a delayed-choice
entanglement-swapping experiment. Delayed-choice entanglement
swapping is a separate paper (*Nature Phys.* 8, 480–485 (2012), as cited in the PNAS reference
list), NOT READ. INV 5.13 (the 2016 review) is a
review, not a primary experiment.

***

## 3. What `D² + V² ≤ 1` bounds

**Statement and definitions (sources: Englert 1996 abstract; De Zela 2013 FULL; Schwindt 1999 FULL;
RMP 2016 FULL for the passage).**
- Setting: a two-way interferometer whose paths are correlated with a which-way detector (marker).
- `V`: fringe visibility of the interfering particle, measured **without** conditioning on the
  marker (Schwindt: analyzer removed; `V = (max − min)/(max + min)`).
- `D`: the which-way information "potentially stored" in the marker (Englert's abstract): the
  largest knowledge `K = 2L − 1` obtainable by an optimal measurement on the marker, `L` the
  probability of guessing the path correctly (Schwindt: `D = max{K}`; a non-optimal measurement may
  give less, or zero). It includes a-priori predictability `P` (`P ≤ K`).
- Relation: `D² + V² ≤ 1`, with equality for a pure initial marker state; for (partially) mixed
  marker states the inequality holds, in general strictly, and equality remains possible (the
  `(1, 1)` example below). Sources: Schwindt ("the inequality applies to (partially-)mixed states");
  RMP ("equality holds for pure states"). For their polarization marker under their half-wave-plate
  coupling, Schwindt give the theory curve `V² + D² = 2 Tr(ρ²) − 1`, under which a maximally mixed
  input gives `V = 0` at every setting; that curve is specific to their coupling.

**What it permits.** Every pair `(D, V)` in the quarter disc `D, V ≥ 0`, `D² + V² ≤ 1`. In particular:
- partial distinguishability with partial visibility, on the boundary for pure markers (for example
  `D = V = 1/√2`) and inside or on it for mixed markers;
- both near zero (a maximally mixed marker: Schwindt measured `V² + K²` = 0.003 ± 0.001);
- `V = 1` only with `D = 0`, and `D = 1` only with `V = 0`.

**What it excludes.** Any pair outside the disc: full which-way information together with any
nonzero visibility, full visibility together with any nonzero distinguishability, and generally
`V > √(1 − D²)`.

**Two forms in the literature, not to be conflated.**
1. *Single-particle (Englert; Jaeger–Shimony–Vaidman):* `V` unconditional, `D` stored in the marker.
   This is the form U4 cites in QM-4 and the form tested by Schwindt 1999 and, per its abstract, by
   Dürr–Nonn–Rempe (PRL 1998).
2. *Bipartite or erasure form (Ma 2013, Eq. 3):* `I² + V² ≤ 1`, with `I` from one measurement on the
   marker and `V` the **conditional** visibility after a complementary measurement on it, in separate
   runs. Here `V` near 1 is reached by sorting, while the unconditional visibility stays near zero.
   Predictability forms (`P² + V² ≤ 1`, attributed to Greenberger–Yasin) are a third, weaker variant,
   since `P ≤ D`.

**Bearing on U4's QM-4 (writer's inferences, by hand, labelled as such).**
- "*Exclude each other*" overstates the inequality. The relation excludes a **full** return of the
  record (`D` → 1) together with any visibility and a **full** revival (`V` → 1) together with any
  distinguishability; it does not exclude a partial return of distinguishability alongside partial
  visibility. A precise wording is "trade off": `V ≤ √(1 − D²)`.
- "*A revival raises `V` only by lowering `D`*": in U4's model (§6.2, the complement in pure
  conditional states `|E_L⟩`, `|E_R⟩` with equal weights) the relation is the equality
  `D² + V² = 1` (PREREG §3.5 derives this pure-marker equality), so any rise of `V` is a fall of `D`;
  the sentence holds there, and U4's complement is pure by definition. It does not follow from the
  inequality alone. With a mixed complement, outside U4's model, the two are not tied: for a maximally mixed qubit marker, path couplings `(1, Z)` give `D = 0`,
  `V = 0`, and couplings `(1, 1)` give `D = 0`, `V = 1` (equality with a mixed marker), so `V`
  changes while `D` stays at zero [writer's inference].
- "*An intact return keeps `D` and `V` where they were*": a unitary acting on the complement alone
  leaves the trace distance between the complement's conditional states (hence `D`) and the overlap
  that fixes `V` unchanged, for pure and mixed complements alike [writer's inference]. Consistent
  with QM-1.
- Using `D` over "the whole complement" is a legitimate application (the detector is whatever holds
  the record), but the experimentally measured quantity is `K` over an accessible marker with a
  chosen measurement, which can be below `D` (Schwindt).

***

## 4. Summary of read status

| Item | Status |
|---|---|
| Scully & Drühl 1982 | ABSTRACT; SECONDARY |
| Scully, Englert & Walther 1991 | ABSTRACT; SECONDARY |
| Englert 1996 | ABSTRACT; proof structure via De Zela 2013 (FULL) |
| Kwiat, Steinberg & Chiao 1992 | ABSTRACT |
| Herzog, Kwiat, Weinfurter & Zeilinger 1995 | ABSTRACT; SECONDARY |
| Kim, Yu, Kulik, Shih & Scully 2000 | FULL (arXiv v1, submitted version) |
| Walborn, Terra Cunha, Pádua & Monken 2002 | FULL (arXiv v1) |
| Ma et al. 2013, PNAS | FULL (arXiv v2 with supplement) |
| Ma, Kofler & Zeilinger 2016, RMP | FULL for the sections named |
| Greenberger & Yasin 1988 | ABSTRACT |
| Wootters & Zurek 1979 | ABSTRACT |
| Dürr, Nonn & Rempe 1998 (Nature; PRL) | ABSTRACT; SECONDARY |
| Schwindt, Kwiat & Englert 1999 | FULL (arXiv v1) |
| Jacques et al. 2008; Ma et al. 2012 (entanglement swapping); Jaeger–Shimony–Vaidman 1995 | NOT READ |
| Jaynes–Cummings sources, Brune 1996, Hahn 1950, Loschmidt sources | NOT READ (Brune 1996 and spin echo SECONDARY via Schlosshauer 2019) |
| Schlosshauer 2019 (Phys. Rep.); Schlosshauer 2004 (RMP) | sections read |

**Not reachable from the reading environment:** journals.aps.org (no APS full text or page read);
paywalled Nature and Elsevier full texts. Reading the APS and Nature full texts of Kwiat 1992,
Herzog 1995, Englert 1996, Dürr 1998 (both), SEW 1991 and Scully–Drühl 1982 would close the ABSTRACT
entries, in particular the open points in 1.5, 1.6 and 1.11.

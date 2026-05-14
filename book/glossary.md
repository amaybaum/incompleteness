# Glossary

This glossary defines the framework's distinctive terminology and the technical vocabulary used throughout the book. Entries are organized alphabetically. Cross-references to chapter and appendix sections point to where each concept is most fully developed.

**Note on convention:** terms in *italics* within definitions indicate other glossary entries. Where the framework's usage differs from standard physics or mathematics usage, the difference is noted explicitly.

---

**Anomaly cancellation.** A condition in quantum field theory requiring that the sum of contributions from chiral fermions to certain triangle diagrams vanishes. In the Standard Model, anomaly cancellation between fermion generations is a structural consistency requirement that constrains the allowed hypercharge assignments. The framework derives the *unique* hypercharge assignment $(Y_Q, Y_u, Y_d, Y_L, Y_e) = (1/6, 2/3, -1/3, -1/2, -1)$ from the six anomaly conditions of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$, with no free parameters. Developed in Chapter 6 §6.7 and Appendix B §B.5.

**Axiom 2 (Finiteness).** The framework's foundational assumption that the substratum has finitely many degrees of freedom. Motivated physically by the Bekenstein bound at the cosmological horizon ($\sim 10^{122}$ distinguishable states). Discussed in Chapter 2 §2.5, with defense in Appendix C §C.6.

**Barandes correspondence.** The mathematical result establishing that *P-indivisible* stochastic processes correspond structurally to unitary quantum dynamics under specific conditions. One of the two independent routes by which the framework derives emergent quantum mechanics from a deterministic substratum (the other being *Stinespring dilation*). Developed in Chapter 1 §1.6 and Appendix B §B.2.

**Bekenstein-Hawking entropy.** The entropy $S = A/(4 l_p^2)$ assigned to a horizon of area $A$ in units of the Planck length $l_p$. The factor of $1/4$ is conventionally treated as a postulate of black-hole thermodynamics. The framework *derives* the $1/4$ factor as a structural consequence of mode counting on the cosmological horizon partition. Confirmed at $99.999\%$ confidence by the LIGO/Virgo/KAGRA analysis of GW250114 in September 2025. Developed in Chapter 7 §7.5.

**Bell-inequality violations.** Empirical correlations exceeding bounds derivable from local hidden-variable theories. The framework reproduces the full quantum predictions including the Tsirelson bound $2\sqrt{2}$ for CHSH correlations through *P-indivisibility* of joint dynamics, which violates Bell's factorizability condition while preserving locality (no signaling) and measurement independence. Developed in Chapter 1 §1.7 and Appendix C §C.2.

**Born rule.** The quantum-mechanical prescription that the probability of measurement outcome $i$ on state $|\psi\rangle$ is $|\langle i|\psi\rangle|^2$. Conventionally treated as a postulate of quantum mechanics. The framework derives the Born rule as the equilibrium distribution of the *read-write cycle* between *visible* and *hidden sectors* of an *embedded observer*'s partition. Developed in Chapter 1 §1.6 and Chapter 18 §18.2 (with the framework's distinctive prediction of transient Born-rule violations in the very early universe).

**BQP (Bounded-error Quantum Polynomial time).** The computational complexity class of decision problems solvable by a quantum computer in polynomial time with error probability bounded by $1/3$. Conventionally treated as an empirical conjecture about what quantum computers can achieve. The framework derives BQP as the *unique* computational class accessible to embedded observers satisfying C1-C3, with both a lower bound (the framework's emergent quantum mechanics provides the BQP toolkit) and an upper bound (the quantum description is informationally complete for the embedded observer). Falsifiable by any super-BQP demonstration. Developed in Chapter 14.

**C1 (Coupling).** The first of the framework's three structural conditions. Requires non-trivial coupling between the *visible* and *hidden sectors* of the *embedded observer*'s partition. Mathematically: the transition matrix $T$ on the visible sector is not a permutation. Physically: information crosses the partition boundary in both directions. C1 fails when the visible sector is causally disconnected from the hidden sector. Discussed in Chapter 1 §1.3.

**C2 (Slow-bath timescale separation).** The second of the framework's three structural conditions. Requires the hidden sector to evolve much more slowly than the visible sector: $\tau_S / \tau_B \ll 1$. Physically: the hidden sector is essentially frozen on the timescale of any visible-sector measurement. For our universe at the cosmological horizon, $\tau_S / \tau_B \sim 10^{-32}$. C2 fails when the hidden sector thermalizes between measurements, producing classical Markovian dynamics. Discussed in Chapter 1 §1.3.

**C3 (Hidden-sector capacity).** The third of the framework's three structural conditions. Requires the hidden sector to have substantially more degrees of freedom than the visible sector: $N_H \gg N_V$. For our universe at the cosmological horizon, $N_H \sim 10^{122}$. C3 fails as $N_H \to N_V$, with the marginal-capacity regime producing the *partially-quantum* regime distinctive to the framework. Discussed in Chapter 1 §1.3, with the partially-quantum regime in Chapter 15 §15.7 and Chapter 18 §18.3.

**Cabibbo angle.** The CKM mixing parameter $\lambda = \sin\theta_C \approx 0.225$ governing first/second-generation quark mixing in the Standard Model. Conventionally a fitted empirical parameter. The framework derives $\lambda = 1/(\pi\sqrt{2})$ from a single Brillouin-zone distance on the substratum lattice, matching observation at $0.04\%$. Developed in Chapter 6 §6.5.

**CaMKII (Calcium/calmodulin-dependent protein kinase II).** A neuronal signaling kinase forming dodecameric holoenzymes with bistable autophosphorylation states. Canonical molecular memory device in long-term potentiation. The framework identifies CaMKII as the prototypical molecular *C1-C3* system in neurons, with the kinase domain as fast subsystem and the regulatory/association domain as slow hidden sector. Pathological $\tau_B$ shifts produce the framework's account of neurodegeneration. Discussed in Chapter 16 §16.4.

**Characterization theorem.** The framework's central result: an embedded observer's reduced description is mathematically equivalent to unitarily evolving quantum mechanics if and only if the three structural conditions *C1*, *C2*, *C3* are satisfied. Forward direction (sufficiency): C1-C3 $\Longrightarrow$ emergent QM. Reverse direction (necessity): three contrapositive theorems, one per condition. Developed in Chapter 1 §§1.8-1.9, with necessity proofs in Appendix C §C.5.

**Chk1 (Checkpoint kinase 1).** A serine/threonine kinase regulating cell-cycle checkpoint responses to DNA damage. The framework identifies Chk1 as a canonical example of regulatory-domain *memory asymmetry*: Chk1 inhibitors selectively sensitize tumor cells because tumor cells rely on non-Markovian checkpoint dynamics that normal cells with intact G1 checkpoints do not require. Discussed in Chapter 16 §16.3.

**Chirality (in the framework).** The framework's commitment to chiral SU(2) electroweak structure derives from the staggered bipartite structure on the cubic lattice combined with the trace-out operation. Propagates through molecular physics to produce the parity-violating energy difference (PVED) between mirror-image molecules, predicting L-amino acids as the slightly more stable enantiomer. Discussed in Chapter 10 §10.7.

**Chromatin.** The protein-DNA complex organizing eukaryotic genomes, including nucleosome positioning, histone modifications (acetylation, methylation), DNA methylation patterns, and three-dimensional chromatin architecture. The framework treats chromatin as the *hidden sector* of the biological *C1-C3* partition with the transcriptional machinery as visible sector. Developed in Chapter 16 §16.9.

**CKM (Cabibbo-Kobayashi-Maskawa) matrix.** The unitary mixing matrix between Standard Model quark mass and weak interaction eigenstates. Conventionally parameterized by three mixing angles and one CP-violating phase. The framework derives the Cabibbo angle structurally and provides partial content for the broader CKM structure. Developed in Chapter 6 §6.5.

**CHSH inequality.** The Clauser-Horne-Shimony-Holt formulation of Bell's inequality, with the classical bound of 2 and the quantum (Tsirelson) bound of $2\sqrt{2}$. The framework reproduces exactly the quantum maximum through *P-indivisibility*. Discussed in Appendix C §C.2.

**Cosmological constant problem.** The discrepancy of approximately $10^{122}$ between quantum field theory's predicted vacuum energy ($\sim 10^{113}$ J/m³) and the observed value inferred from cosmic expansion ($\sim 6 \times 10^{-10}$ J/m³). The framework *dissolves* this problem by identifying the two quantities as properties of logically distinct descriptions: the quantum vacuum energy is the emergent QFT's prediction within a partition; the observed cosmological constant is the gravitational consequence of the substratum's full content. Developed in Chapter 7 §7.7.

**Cryptochrome.** A flavoprotein in animal retinas whose photoexcitation produces a radical pair (FADH• and Trp•) with millisecond singlet/triplet interconversion. The substrate for the avian magnetic compass. The framework identifies cryptochrome as a canonical *C1-C3* system in biology with the radical-pair electron spins as fast subsystem and the protein matrix as slow bath. Discussed in Chapter 13 §13.5.

**Cubic decomposition.** The framework's structural result that the six-dimensional representation of the cubic rotation group $O$ on internal lattice components decomposes as $\mathbf{6} = T_1 \oplus E \oplus A_1$ — multiplicities $(3, 2, 1)$ identifying the Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. Developed in Chapter 5 §5.5 and Appendix B §B.6.

**DSW (Danielson-Satishchandran-Wald) horizon decoherence.** A 2022 result by Danielson, Satishchandran, and Wald proving within standard QFT in curved spacetime that Killing horizons impose fundamental decoherence on nearby quantum superpositions, with rate determined by horizon geometry. External convergence with the framework's universality-class content. Discussed in Chapter 9 §9.7 and Chapter 15 §15.8.

**Embedded observer.** The framework's technical term for an observer who is a substructure of the system they are trying to describe — coupled to the system, bounded in extent, unable to access the full state from outside. The central object of the framework's analysis. Defined precisely in Chapter 1 §1.2, characterized by C1-C3 in §1.3.

**Emergent description.** The reduced description of the visible sector after marginalizing over (tracing out) the hidden sector. In the framework, the emergent description of any system satisfying C1-C3 is mathematically equivalent to unitary quantum mechanics. Developed throughout Chapter 1.

**Epigenome.** The set of chromatin marks and methylation patterns that regulate gene expression while remaining heritable across cell divisions and (partially) generations. The biological instantiation of the framework's *substratum-emergent operator distinction* at the molecular scale. Discussed in Chapter 16 §§16.9-16.10.

**Extended Church-Turing Thesis (ECT).** The conjecture that any physically realizable computation can be efficiently simulated by a Turing machine. Conventionally treated as an empirical hypothesis subject to potential refutation by quantum computing. The framework derives the ECT as a *theorem*: any physically realizable computation by an *embedded observer* satisfies the BQP bound. Developed in Chapter 14 §14.6.

**Fine-tuning.** The observation that certain physical parameters (fine-structure constant, mass ratios, cosmological constant) appear to occupy narrow ranges supporting chemistry and complexity. The framework's reading: most chemistry-supporting features are *structural* (derived from the framework's commitments) rather than parametric, dissolving the conventional fine-tuning problem. Discussed in Chapter 10 §10.8.

**Frauchiger-Renner theorem.** A 2018 no-go theorem identifying contradictions in scenarios where quantum mechanics is applied to systems containing observers who themselves apply quantum mechanics. The framework's response: the contradictions dissolve under *partition-relativity*, with observer-internal and external descriptions corresponding to different partitions. Discussed in Appendix C §C.3.

**Gap equation (for $\hbar$).** The thermal self-consistency condition between the classical horizon temperature $T_{cl} = c^2\epsilon^2 \kappa/(8\pi G k_B)$ and the KMS temperature $T_Q = \hbar\kappa/(2\pi c k_B)$ of the emergent QFT, producing $\hbar = c^3 \epsilon^2/(4G)$. The framework's derivation of Planck's constant from horizon thermodynamics. Developed in Chapter 7 §7.3 and Appendix B §B.4.

**Gauge group.** A continuous group of local symmetries under which the dynamics is invariant. The Standard Model gauge group is $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$. The framework derives this gauge group as the unique commutant of a cubic-symmetric coupling matrix on the substratum lattice. Developed in Chapter 5.

**Generation (fermion).** In the Standard Model, the three sets of fermions with identical gauge-quantum-number assignments but different masses: $(u, d, e, \nu_e)$, $(c, s, \mu, \nu_\mu)$, $(t, b, \tau, \nu_\tau)$. The framework derives three generations from the staggered taste structure on the cubic lattice. Discussed in Chapter 6 §6.2.

**God's-eye view.** A hypothetical observer coextensive with the universe, with complete knowledge of all degrees of freedom. The framework identifies the God's-eye view as the *C3* failure limit and shows that it is not a limit case of observation but a category outside it — observation is partition-relative, and without a partition, observation does not occur. Discussed in Chapter 1 §1.10.

**GW250114.** A high-signal-to-noise binary black-hole merger observed by LIGO on January 14, 2025 (hence "GW250114"), with the LIGO/Virgo/KAGRA analysis paper published in *Physical Review Letters* on September 10, 2025, confirming Hawking's area law (the Bekenstein-Hawking factor of $1/4$) at $99.999\%$ confidence. The framework's strongest empirical confirmation in the gravitational sector. Discussed in Chapter 7 §7.5.

**Hidden sector.** The portion of the framework's partition that the embedded observer does not directly access. The framework's three structural conditions specify properties of this sector (coupling, slow evolution, large capacity). For laboratory observers in our universe, the hidden sector is everything beyond the cosmological horizon plus the trans-horizon degrees of freedom of any local environment. Defined in Chapter 1 §1.2.

**Higgs (in the framework).** The framework treats the Higgs as the *singlet* ($A_1$) taste of the staggered decomposition — a *composite scalar* in the framework's account rather than a fundamental field. The Higgs quartic coupling at the compositeness scale is exactly zero, with the observed value at low energies generated by RGE running. Developed in Chapter 6 §6.2.

**Hsp90.** A molecular chaperone that buffers genetic variation by chaperoning mutant proteins into functional conformations. The canonical evolutionary capacitor (Rutherford and Lindquist 1998). The framework identifies Hsp90-client conformational states as a *C1-C3* hidden sector with stress-induced release of accumulated variation. Discussed in Chapter 17 §17.9.

**Hypercharge.** The Standard Model U(1) quantum number of fermion multiplets, with values $(Y_Q, Y_u, Y_d, Y_L, Y_e) = (1/6, 2/3, -1/3, -1/2, -1)$. Conventionally fitted empirical inputs. The framework derives these values as the unique anomaly-free solution. Developed in Chapter 6 §6.7 and Appendix B §B.5.

**Information backflow.** In the framework, the return of correlations from the hidden sector to the visible sector on the bath's correlation timescale $\tau_B$. The structural signature of *non-Markovian* dynamics and the framework's distinctive prediction across multiple empirical domains. Discussed in Chapter 1 §1.5.

**Jordan-Chevalley projection.** The algebraic decomposition of an operator into commuting semisimple and nilpotent parts: $F = F_{ss} \cdot F_u$ with $F_u = I + N$ and $N^2 = 0$. The framework's content: the trace-out operation extracts $F_{ss}$ and discards $N$, organizing the emergent description by the representation theory of the partition. Developed in Appendix B §B.3.

**JUNO (Jiangmen Underground Neutrino Observatory).** A reactor neutrino experiment that in November 2025 reported the first world-leading direct measurement of the solar neutrino mixing angle: $\sin^2\theta_{12} = 0.3092 \pm 0.0087$. The framework's prediction $1/3 - 1/(4\pi^2) = 0.3080$ matches this at $0.07\sigma$. The framework's strongest empirical anchor. Discussed in Chapter 8.

**Koide relation.** An empirical relation among the three charged-lepton masses: $Q = (m_e + m_\mu + m_\tau)/(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2$. Observed value $Q = 0.666661 \pm 0.000007$. The framework predicts $Q = 2/3$ from cubic-group quadratic Casimir; the match is $0.02\%$. Developed in Chapter 6 §6.6.

**Markovian.** A stochastic process whose future depends only on the present state, with no memory of past states. Standard chemical kinetics is Markovian; the framework's emergent quantum mechanics is *non-Markovian* through *P-indivisibility*. Contrasted throughout Chapter 1.

**Memory asymmetry.** The framework's unifying therapeutic principle in medicine: when a disease process depends on non-Markovian signaling dynamics that the corresponding normal tissue does not depend on, therapies can target the memory structure rather than the catalytic function, with the framework predicting wider therapeutic windows. Developed in Chapter 16 §16.13.

**MOND (Modified Newtonian Dynamics).** A phenomenological framework for galactic rotation curves involving an acceleration scale $a_0 \approx 1.2 \times 10^{-10}$ m/s². Conventionally treated as a phenomenological alternative to dark matter. The framework derives $a_0 = cH/6$ as a structural consequence of entropy displacement at the cosmological boundary, with no free parameters. Developed in Chapter 7 §7.9.

**Non-Markovian.** A stochastic process whose future depends on past states beyond the present. The framework's emergent quantum mechanics is fundamentally non-Markovian through *P-indivisibility*, distinguishing it structurally from classical Markovian dynamics. Predicted to appear at multiple scales: cosmological (quantum mechanics), biological (enzyme kinetics, gene expression), engineered (qubit noise). Defined in Chapter 1 §1.5.

**NV (Nitrogen-vacancy) center.** A point defect in diamond where a nitrogen atom replaces a carbon atom adjacent to a lattice vacancy. The basis for room-temperature quantum sensing with current sensitivity limited by the NV electron-spin coherence time. The framework predicts up to $10^3 \times$ sensitivity improvement through backflow-aware sensing protocols exploiting the diamond lattice's slow nuclear-spin bath. Discussed in Chapter 15 §15.6.

**Operator distinction (substratum-emergent).** The framework's structural distinction between operators acting at the substratum level (with specific conservation properties at the molecular or quantum-field level) and operators acting at the emergent level (with conservation properties at the coarse-grained level). The two operators can be functionally distinct even when they look identical at the emergent level. Developed in Chapter 6 §6.3 (for fundamental physics) and Chapter 16 §16.10 (for chromatin biology).

**Page curve.** The time-dependence of black-hole entanglement entropy: rising during the early evaporation phase, reaching a peak at the Page time, then falling as the black hole evaporates fully. The framework derives the Page curve from cycle typicality with structural Page time $t_P \approx 0.646 t_{evap}$ independent of mass and greybody factors. Developed in Chapter 7 §6.

**Partially-quantum regime.** The framework's distinctive prediction of dynamics distinct from both fully-quantum and fully-classical regimes, accessible at intermediate $\tau_S/\tau_B$ values or marginal *C3* capacity. Empirically diagnosable through multi-time correlation measurements, with the functional form $\mathcal{F}(r) = 2r - r^2$ for capacity-controlled non-Markovianity. Developed in Chapter 13 §13.7, Chapter 15 §§15.7-15.8, Chapter 18 §18.3.

**Partition-relativity.** The framework's structural feature that the same physical substratum admits multiple visible/hidden partitions, each producing its own emergent description. The emergent description depends on the partition choice; the underlying substratum does not. Resolves several no-go theorems including Frauchiger-Renner. Developed in Chapter 1 §1.4.

**P-indivisibility.** The framework's central technical concept: a stochastic process is P-indivisible if its transition matrix at time $t_2 > t_1$ cannot be expressed as the composition of the transition matrix at $t_1$ with a positive transition matrix. Equivalently: no Markovian process with intermediate state at $t_1$ can produce the same statistics. P-indivisibility is the framework's structural mechanism for emergent quantum mechanics, and it follows from C1-C3 jointly. Developed in Chapter 1 §1.5 and Appendix B §B.7.

**PMNS (Pontecorvo-Maki-Nakagawa-Sakata) matrix.** The unitary mixing matrix between Standard Model neutrino mass and flavor eigenstates. The framework derives all three PMNS mixing angles from the cubic-group flavor structure, including the JUNO-confirmed solar angle $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$. Discussed in Chapter 8.

**Read-write cycle.** The framework's equilibrium dynamics between the visible and hidden sectors of the partition. The observer reads the visible sector, writes correlations into the hidden sector through the partition coupling, and reads back those correlations on subsequent measurements. The cycle produces emergent quantum mechanics at the cosmological scale and heredity at the molecular scale. Defined in Chapter 1 §1.6.

**Reader/writer/eraser pharmacology.** The framework's three-axis organization of epigenetic therapeutics, corresponding directly to the operator distinction at chromatin. *Writers* establish substrate-level marks (DNMT and HMT inhibitors); *erasers* remove them (HDAC and HDM inhibitors); *readers* translate marks to functional output (BET bromodomain inhibitors). The framework's structural prediction: reader-writer disorders show wider therapeutic windows than substrate-gene disorders, empirically confirmed for Rett syndrome. Developed in Chapter 16 §§16.11-16.12.

**Rett syndrome.** A neurodevelopmental disorder caused by loss-of-function mutations in MECP2, a methyl-CpG binding reader protein. Guy et al. (2007) demonstrated that restoration of MECP2 expression in adult MECP2-knockout mice reverses the neurological phenotype, confirming the framework's pre-registered prediction of wider therapeutic windows for reader-writer disorders. The framework's strongest empirical anchor outside fundamental physics. Discussed in Chapter 16 §16.12.

**RNA world.** The hypothesis that early life used RNA for both information storage and catalysis before DNA and proteins evolved their specialized roles. The framework's structural reading: RNA-like architecture is the simplest single-molecule C1-C3 system (simultaneously template and catalyst), making the RNA world a structural prediction rather than a historical accident. Developed in Chapter 11 §11.7.

**Staggered (fermion structure).** The placement of independent fermion modes at alternating cubic lattice sites, producing the chiral structure of the framework's emergent QFT and the multiple-taste structure that gives rise to three generations. Developed in Chapter 5 §5.6 and Chapter 6 §6.2.

**Standard Model.** The current best theory of fundamental particle physics: a chiral gauge theory with gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$, three fermion generations, one Higgs doublet, and approximately 19 free parameters. The framework derives the gauge group, the matter content, the chirality structure, the anomaly-free hypercharges, and 22 of the parameters as structural consequences with no free inputs. Developed in Chapters 5-6.

**Stinespring dilation.** A 1955 theorem of operator algebra establishing that any completely-positive trace-preserving map on a Hilbert space can be realized as a unitary evolution on a larger Hilbert space with subsequent tracing-out. The framework uses Stinespring dilation as the second independent route from the deterministic substratum to emergent quantum mechanics (alongside the *Barandes correspondence*). Developed in Chapter 1 §1.6 and Appendix B §B.2.

**Substratum.** The framework's underlying deterministic, finite-dimensional, bijective dynamical system $(S, \varphi)$ from which emergent quantum mechanics is derived through the trace-out operation. The substratum is the framework's primitive ontological commitment — the "what is really there" beneath the emergent quantum-mechanical description. Constructed concretely in Chapter 2.

**Substratum-emergent operator distinction.** *See operator distinction.*

**Tier 1, Tier 2, Tier 3.** The framework's stratification of predictions by their robustness across substratum representatives. *Tier 1*: results that follow from the framework's universality class (shared across all substrata satisfying the structural conditions). *Tier 2*: results dependent on broader structural commitments but not on specific lattice details. *Tier 3*: solution-specific results dependent on the particular cubic-lattice realization. Developed in Chapter 9 §§9.3-9.4.

**TLS (Two-level system).** Structural defects in amorphous oxide substrates of superconducting qubits, characterized by flipping between two configurations at characteristic rates. The framework identifies the TLS bath as the *hidden sector* in superconducting qubit C1-C3 systems, with $\tau_S/\tau_B \sim 10^{-3}$ producing the framework's predicted correlated error structure. Discussed in Chapter 15 §15.3.

**Trace-out.** The mathematical operation of marginalizing over (summing or integrating out) the hidden-sector degrees of freedom, producing the reduced description on the visible sector. The framework's central technical operation. Equivalent to partial trace in quantum mechanics. Defined throughout Chapter 1.

**Tsirelson bound.** The maximum CHSH inequality violation achievable by quantum mechanics: $2\sqrt{2}$. The framework reproduces exactly this bound through *P-indivisibility*, distinguishing it from theories predicting weaker (classical) or stronger (PR-box) violations. Discussed in Appendix C §C.2.

**U-parity.** The framework's grading structure in the neutrino sector, distinguishing $U^+$ and $U^-$ states in the cubic-group flavor classification. Produces the framework's distinctive sum rule and structural relation among the three PMNS mixing angles. Developed in Chapter 8 §8.4.

**Universality class.** A set of substrata that share the same emergent description at the framework's Tier 1 level. The framework's content: the substratum-to-emergent map is many-to-one, with multiple bijections producing the same observable physics. Developed in Chapter 9 §9.3.

**Vibronic coherence.** Quantum coherence between electronic exciton states and specific vibrational modes of the protein environment. The framework identifies the picosecond-scale coherences observed in photosynthetic complexes (FMO, LH2, photosystem II) as vibronic rather than purely electronic, consistent with the framework's C1-C3 architecture. Discussed in Chapter 13 §13.4.

**Visible sector.** The portion of the framework's partition that the embedded observer directly accesses. Contrasted with the *hidden sector*. The visible sector is where measurements occur and where the emergent description applies. Defined in Chapter 1 §1.2.

**Wolpert's theorem.** David Wolpert's 1992 result on fundamental limits of inference devices embedded in the system they are trying to predict. A physical analog of Gödel's incompleteness theorem and Turing's halting problem result. The framework identifies the partition-induced trace-out as the specific mechanism for the Wolpert limit, with quantum mechanics as the specific cost. Discussed in Chapter 12 §12.8, Appendix C §C.7.

**Yamanaka factors.** The four transcription factors (Oct4, Sox2, Klf4, c-Myc) whose transient expression reprograms somatic cells to induced pluripotent stem cells. The framework identifies iPSC reprogramming as confirming the *substratum-emergent operator distinction* at chromatin: the emergent operator (cell identity) flips while substantial residual substrate-level operator (DNA methylation patterns reflecting source cell type) persists. Discussed in Chapter 16 §16.10.

---

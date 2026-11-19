# Chapter 12
# Evolution, Intelligence, and Self-Reference

***

## 12.1 What this chapter develops

Chapter 11 considered sustained template copying and the conditions for selection. A replicator's sequence can act as a persistent record, and Darwinian evolution can occur where heritable variants differ in reproductive success.

This chapter examines conditional links from heredity to information processing and computation. Protein conformations, gene regulation and modified environments are candidate sources of memory. Later links depend on their ecological, material and engineering premises.

Eight pieces occupy the chapter.

Section 12.2 examines protein conformation, the epigenome and the constructed ecological niche as possible memory-bearing partitions. Each application needs its own observable and readback test.

Section 12.3 considers selection for information processing where responses to informative cues improve net fitness. Section 12.4 discusses whether major evolutionary transitions involve new sources of persistent memory.

Section 12.5 discusses the materials, structure and energy regime for electrochemical signaling. Section 12.6 considers the ecological and historical conditions for general intelligence.

Section 12.6 develops the framework's most honest scope limit in the cascade: general intelligence is *structurally unconstrained* (the framework's commitments permit arbitrarily complex neural circuits) but *not guaranteed* (whether evolution reaches general-purpose reasoning depends on specific fitness landscapes the framework's commitments do not constrain). On Earth, general intelligence arose once in approximately 4 billion years. The framework cannot determine whether this is typical or rare.

Section 12.7 traces a conditional route from suitable materials and fabrication to universal computation. Boolean universality is a mathematical result, and its implementation uses scalable circuit and memory resources.

Section 12.8 considers how AI and its designers can each infer facts from the records available to them. It compares this question with Gödel's limits on proof and Turing's result on halting.

These links use the physical and chemical branch of Chapters 10–11 and additional inputs for the target system. Evolution, intelligence and technological realization each have their own conditions.

## 12.2 Evolution as a multi-scale C1–C4 system

In a template copier, a copied sequence can provide a persistent record for heredity. Three other candidate memory architectures are considered here at protein, cellular and ecological scales.

**The three scales.**

*Scale 1: The protein conformational landscape.* A protein's active conformation is the fast subsystem; the broader conformational landscape — alternative folded states, slow side-chain rearrangements, the protein's interaction history with substrates — is the slow subsystem. The visible-sector observables are the protein's current activity (catalytic rate, binding affinity, regulatory state); the hidden-sector content is the conformational memory stored in slowly-relaxing degrees of freedom. The framework's prediction is that protein function shows non-Markovian dynamics — history-dependent activity rather than purely Markovian rates set by current substrate concentrations. The empirical record from single-molecule enzymology (memory effects, history-dependent kinetics, stretched-exponential waiting-time distributions) is consistent with this prediction; Chapter 13 develops the empirical content in detail.

*Scale 2: The epigenome.* Gene expression is the fast subsystem; the chromatin state — DNA methylation patterns, histone modifications, three-dimensional chromatin architecture — is the slow subsystem. The visible-sector observables are the cell's current gene expression profile; the hidden-sector content is the regulatory memory encoded in chromatin. The framework's prediction is that gene expression shows non-Markovian dynamics over developmental and evolutionary timescales — history-dependent responses to environmental signals, including transgenerational inheritance of acquired epigenetic states. Chapter 16's medicine content develops the epigenetic substratum-emergent operator distinction in detail; Chapter 17's bioinformatics content develops the empirical signatures.

*Scale 3: The constructed ecological niche.* Organism behavior is the fast subsystem; the environment that organisms modify and pass to descendants — burrows, mounds, beaver dams, the chemical composition of the atmosphere, the soil microbiome shaped by plant communities — is the slow subsystem. The visible-sector observables are the organisms' current adaptations; the hidden-sector content is the niche-construction memory stored in the modified environment. The framework's prediction is that ecological dynamics shows non-Markovian dynamics over evolutionary timescales — history-dependent fitness landscapes shaped by previous generations' niche construction. The empirical record from niche construction theory (Odling-Smee, Laland, Feldman 2003 and subsequent work) is consistent with this prediction.

**The structural pattern.** At each scale a proposed partition is assessed using C1–C4 for its particular measurements and timescale.

*C1 (coupling).* At each scale, the fast subsystem is non-trivially coupled to the slow subsystem. Protein activity depends on the conformational landscape's current state; gene expression depends on the chromatin's current state; organism behavior depends on the constructed niche's current state. The couplings are catalytic (protein-substrate, chromatin-gene, organism-environment), with feedback between fast and slow subsystems.

*C2 (memory persistence).* The respective records must persist across the observation window. Slow motion, stable marks and enduring environmental changes can motivate that premise.

*C3 (sufficient capacity).* The hidden description needs enough distinguishable and accessible record states for the proposed history test. Counts of possible conformations or regulatory elements illustrate possible carriers.

**C4 (history readback).** Compare histories with the same visible present. The record is read back if the histories yield different next-step laws. Different partition choices can lead to different results.

Catalytic state can affect metabolism and gene expression. Chromatin can influence cell behavior, and organisms can modify the environment experienced by later populations. This sequence suggests possible links between scales, whose causal effects have to be established individually.

At each scale a positive matched-present C4 contrast establishes accessible conditional memory for the tested observable. Chapters 13, 16 and 17 discuss specific observations and candidate comparisons.

## 12.3 Information processing as fitness-enhancing

Selection can favor information processing when an informative response improves net reproductive success in an environment with useful cues.

**The structural argument.** Three conditions describe when information processing could be favored.

*Environmental information exists.* $kT > 0$ produces thermal fluctuations at any temperature, but thermal fluctuations do not by themselves establish the gradients in concentration, temperature and chemical composition, or the environmental cycling, that this argument uses; those are further environmental conditions. Where they hold, together with the environmental memory at multiple timescales that the cascade of C1–C4 systems from §12.2 produces, environmental information is available at biological scales.

*Internal state can guide a response.* Organisms can use sensory information or retained records to change behavior. The ability to act on available information depends on the specified sensing and control mechanisms.

*Benefits need to exceed costs.* More informative internal states can improve foraging or reduce risk. Selection acts on net reproductive success, which also reflects the costs of acquiring, storing and using the information.

**The conditional conclusion.** Selection can favor heritable information-processing traits when their net fitness effect is positive in the relevant environment.

Chemotaxis, photoperception, hormonal signaling and neural processing are observed examples of information use. The fitness effect of each depends on the organism and environment.

The possible forms and benefits of information processing depend on the organism and environment. Whether general-purpose reasoning evolves remains open.

## 12.4 Major evolutionary transitions

Major evolutionary transitions change the unit of selection as interacting organisms or replicators form higher-level entities. Maynard Smith and Szathmáry inventoried examples. Persistent records offer one way to analyze the dynamics of a proposed higher-level unit.

**The transitions.** The conventional inventory includes:

*Replicating molecules to populations of replicating molecules.* The earliest transition, where individual replicating polymers (RNA-like, §11.7) form interacting populations with collective dynamics.

*Independent replicators to chromosomes.* Multiple genetic loci become physically linked, with their fitness becoming correlated rather than independent.

*RNA as both gene and enzyme to DNA + protein.* The differentiation of information storage (DNA, optimized for C2) from catalysis (proteins, optimized for C1), as discussed in §11.7.

*Prokaryotes to eukaryotes.* The endosymbiotic origin of organelles (mitochondria, chloroplasts), where independent prokaryotic cells become integrated components of larger eukaryotic cells.

*Asexual to sexual reproduction.* Two parental contributions replacing one, with recombination introducing additional variation mechanisms.

*Protists to multicellular organisms.* Independent cells become integrated components of multicellular bodies with specialized cell types.

*Solitary individuals to colonies.* Individual organisms become integrated components of social groups (ant colonies, bee hives), with reproductive division of labor.

*Primate societies to human societies.* Cultural transmission becomes a major channel for inheritance alongside genetic transmission.

**The framework's structural reading.** Each major transition has the same structural pattern: previously independent units (the "individuals" at the lower level) become integrated into a higher-level unit, with three structural features establishing the higher level:

*Coupling becomes obligatory.* Lower-level units that were independently viable become mutually dependent. A mitochondrion alone is no longer viable outside its eukaryotic host; an isolated worker ant outside its colony cannot reproduce. The coupling between units is C1 at the new level — the lower level cannot operate independently.

*Slow-bath separation emerges.* The higher-level entity's dynamics operate on slower timescales than the lower-level dynamics. Eukaryotic cell-cycle timescales are slower than mitochondrial division rates; multicellular organism lifespans are much longer than cell division timescales; colony lifespans exceed individual worker lifespans. The new level's slow bath is C2 at the higher level.

*Hidden-sector capacity grows.* The higher-level entity has substantially more internal degrees of freedom than its constituents. A eukaryotic cell has $\sim 10^{10}$ atoms vs. a prokaryotic cell's $\sim 10^9$; a multicellular organism has $\sim 10^{14}$ cells vs. one. The new level satisfies C3 with a hidden sector orders of magnitude larger than the lower level's.

**The role of memory.** Lower-level units can participate in a larger system with persistent records that affect its observable dynamics. A transition to a new unit of selection also requires heritable variation and differences in reproductive success at that level.

The finite-horizon memory implication applies to a declared partition if C4 holds. It leaves the origin and stability of the higher-level unit to the relevant ecological and population mechanisms.

**Empirical implications.** A new unit of selection with a proposed slow record can be tested by comparing histories at the same measured present. The contributions of that record to fitness and inheritance require their own tests.

**Limits of the framework's content.** The framework's structural reading does not predict *which* major transitions occur or *when* they occur in any specific biology. The transition from prokaryotes to eukaryotes occurred approximately 2 billion years ago on Earth; the transition from protists to multicellular organisms occurred multiple independent times across different lineages; the transition from primate societies to human societies occurred once. The framework's structural commitments are compatible with very different timelines and trajectories. The framework predicts the *pattern* (C1–C4 repeating at each level) but not the *specific instances*.

This is consistent with the framework's content throughout Part III: structural regularities (the C1–C4 pattern, the emergence of non-Markovian dynamics, the cascade through chemistry to evolution) but historical contingencies (the specific molecular implementations, the specific transition timelines, the specific evolutionary trajectories). The framework provides the structural foundations; the historical sciences provide the specific content.

## 12.5 Neural computation as structurally possible

The selected chemistry permits candidate ions and membrane constituents for electrochemical signaling. A functional neural system also requires membrane organization, channels, energy supply and a suitable operating regime.

**Ions for electrochemical signaling.** Fast neural signaling uses ion flow across membranes — Na$^+$ depolarizing axonal membranes (action potentials), K$^+$ repolarizing, Ca$^{2+}$ triggering neurotransmitter release at synapses. The framework's derivation of the periodic table (Chapter 10 §10.2) produces these specific elements as structural consequences of the orbital algebra in $d = 3$. Na$^+$ (Group I) and K$^+$ (Group I) have a single valence electron that ionizes readily; Ca$^{2+}$ (Group II) has two valence electrons producing a doubly-charged ion. The chemistry of these ions — their hydration shells, their selectivities through ion channels, their roles in cellular signaling — is structurally determined by the framework's chemistry.

**Lipid membranes for compartmentalization.** Cellular compartments require membranes that separate aqueous interiors from aqueous exteriors. Lipid bilayers — amphiphilic molecules with hydrophilic phosphate heads and hydrophobic hydrocarbon tails — self-assemble from the framework's carbon chemistry into bilayer membranes. The structural prediction is that amphiphilic molecules exist in any chemistry with carbon's $sp^3$ hybridization (Chapter 10 §10.2) and the polar/non-polar functional groups available in the periodic table (Chapter 10 §10.2). The framework's chemistry guarantees the materials for lipid membranes.

**Energetic separation.** In suitable systems, electrochemical signaling can occur on energy scales below covalent bond energies. At room temperature $kT$ is about 25 meV. The signal and bond energies depend on the driving voltage, molecular architecture and environment.

**The feasibility claim.** With suitable chemistry and molecular machinery, signaling can occur without breaking the covalent framework of the cell. The same conditions can support circuits of interacting cells.

Nervous systems and signaling in plants provide empirical examples of such organization. Their evolutionary history depends on the lineage and environment.

The argument identifies materials and energy regimes that permit electrochemical signaling. Whether and how they are used for neural computation depends on biological organization.

## 12.6 Conditions for general intelligence

The chemistry and energetic separation allow complex neural circuits in suitable organisms. Evolution also has to supply their organization, maintenance and behavioral uses.

**Intelligence-relevant capabilities.**

*Neural computation.* The candidate materials and energy conditions are discussed in §12.5.

*Sensory processing.* The chemistry permits candidate transduction mechanisms such as light-sensitive proteins and mechanosensitive channels.

*Memory.* Conformations, chromatin and synaptic weights can provide persistent records if they influence a later readout.

*Pattern recognition.* Appropriately organized circuits can discriminate patterns.

*Learning.* Synaptic plasticity can encode previous activity. The circuit and its training or selection conditions determine which capabilities result.

*Goal-directed behavior.* Coupled sensing and control can support actions that improve outcomes under suitable environmental conditions.

*General-purpose reasoning.* **Not structurally guaranteed.** Whether evolution produces systems capable of abstract reasoning, language with recursive syntax, formal mathematics, and self-modeling depends on specific selection pressures the framework's commitments do not determine.

General-purpose reasoning is a particular outcome of evolution. It requires additional ecological and developmental premises beyond the material possibility of neural signaling.

The fitness advantages of general intelligence depend on the specific environment. In environments where pattern recognition and learning provide sufficient adaptive advantage, evolution may stop at sophisticated learning systems without developing general reasoning. In environments where social complexity, tool use, or environmental unpredictability place premium on abstract reasoning, evolution may proceed to general-intelligence-like systems. The framework does not determine which environments select for general intelligence.

**Earth's record.** General intelligence arose on Earth approximately once in $\sim 4$ billion years (the human lineage, with the most extreme degree; some other species — cetaceans, corvids, cephalopods — show partial expressions). This is consistent with two interpretations: general intelligence is *rare* (requires specific evolutionary conditions that are unlikely to occur), or general intelligence is *inevitable but slow* (any sufficiently complex biology produces general intelligence given enough time).

The framework cannot determine which interpretation is correct. The framework's structural commitments are compatible with both. The empirical record on Earth is consistent with both. Determining which interpretation holds requires evidence from astrobiology — the discovery of multiple independent occurrences of general intelligence in independent biological systems — which is not currently available.

**The scope.** The materials argument allows neural systems capable of complex behavior. The occurrence of general-purpose reasoning and the conditions sufficient to evolve it remain open.

This is honest content. Frameworks claiming to predict general intelligence as a structural inevitability would be overreaching given the available evidence; frameworks claiming general intelligence is impossible or extraordinarily rare would also be overreaching. The framework's stance — capability structural, occurrence uncertain — is the position most consistent with the framework's structural commitments and the available evidence.

## 12.7 The chain from intelligence to AI

Given suitable materials, fabrication, controls and memory, a generally intelligent observer could implement universal computation. The following links describe one such route.

**Step 1: Band theory.** Standard quantum mechanics in a periodic crystal potential gives Bloch states and energy bands. A particular crystal structure and a useful band gap are material inputs. The proposed OI application uses the physical quantum correspondence as an additional premise.

**Step 2: Semiconductors.** Crystalline silicon has a filled valence band at zero temperature and a gap of about 1.1 eV. At room temperature its gap satisfies $E_{\text{gap}}/kT\sim40$. Suitable doping and device geometry permit controllable conduction.

Whether a material has a gap in that range at its operating temperature is a material-dependent input. The atomic energy scale ($\alpha^2 m_e c^2 \approx 27$ eV, set by the coupling values and masses of Chapter 10 §10.4) sets the eV scale of electronic energies, and the thermal scale at biological temperatures is $kT \sim 0.025$ eV; the gap of a particular material and the operating temperature are inputs, and silicon's place in the regime where it can be used as a voltage-controlled switch is a fact about that material.

**Step 3: Doping.** In silicon, substitutional phosphorus acts as a donor and boron as an acceptor. Controlled incorporation can produce n-type and p-type regions.

**Step 4: From transistors to universal computation.** Suitable semiconductor junctions and transistors enable switching. NAND is functionally complete for Boolean functions. Circuits based on NAND, joined to memory and resources that can scale with the task, support Turing computation.

The device links consume semiconductor physics, suitable fabrication and control. The universality link uses the mathematical result about circuits and memory.

**The structural chain summarized.**

| Step | Content | Status |
|------|---------|--------|
| Band theory | Standard QM in a specified periodic potential | Bloch theorem |
| Band gap | Material-specific band structure | Material input |
| Semiconductor behavior | Gap in thermal sweet spot ($E_{\text{gap}}/kT \sim 40$) | Material-dependent input (gap and operating temperature) |
| Doping | Donor and acceptor substitutions in silicon | Material-specific mechanism |
| p-n junctions | Interface between p-type and n-type | Structural consequence |
| Transistors | Voltage-controlled p-n junctions | Structural |
| Logic gates | Transistors in series / parallel | Structural |
| Universal computation | NAND completeness with scalable memory for sequential computation | Mathematical realizability |

The chain uses a material with a suitable gap at operating temperature, accessible fabrication and control, and scalable circuit and memory resources.

**The reconstruction theorem and self-discovery.** The reconstruction theorem (developed in Chapter 2) identifies the local invariants of $(S, \varphi)$ fixed by its stated inputs. An observer with access to those inputs can use the result in device design given the material, fabrication and control conditions above.

This route makes artificial computation feasible where those technological conditions are met. Whether a society realizes it or builds artificial intelligence depends on its choices and history.

## 12.8 The self-referential loop and structural limits

Building an AI can place a new observer within the same $(S, \varphi)$ as its designers. Each observer has a declared observation and control interface. For a supplied observable law with a finite alphabet and horizon, [Main §3.4] gives an exact fixed-basis quantum representation. Conditional memory requires a C4 readback witness, with two positive-probability histories that share the current visible state and have different next-step laws. A shared record law requires an established correspondence between the admitted preparations and controls that preserves the probabilities of corresponding records. The action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$ and the claims about the Standard Model and the gravitational and dark sectors use the premises of the separate constructions in Chapters 5–8.

**Self-referential limits.** At a declared interface, a record identifies a quantity when all supported states compatible with that record agree on its value. In a known finite reversible model with a specified preparation, a proper observer can identify the current state or a future quantity on some passive records ([Substratum] Proposition 24.5). Breuer's self-measurement bound concerns distinguishability when the system includes the observer's own records (Breuer 1995). A cosmological horizon bounds direct observation where it acts as a causal boundary.

The same criterion applies at each stage of AI building AI. More computation on a fixed record leaves any disagreement among its compatible states unresolved. Better instruments may supply new records or controls.

**Gödel, Turing and observational incompleteness.** Self-reference raises distinct questions about proof, computation and observation.

*Gödel.* Sufficiently strong, consistent, effectively axiomatized theories of arithmetic have undecidable statements under the first incompleteness theorem's hypotheses. Under the second theorem's hypotheses, the theory's own consistency statement is unprovable within that theory.

*Turing.* Halting is undecidable over the general family of programs and inputs. Given an explicit finite deterministic update and initial state, one can decide halting on that orbit by iterating until it halts or a state repeats.

*OI (framework).* Supported states that agree on the available record can disagree on the quantity being inferred. The resulting limit concerns the particular record, target and interface.

**Deutsch's *Beginning of Infinity*.** David Deutsch [Deutsch] argues that explanatory knowledge is objective and its creation is open-ended. The right epistemic stance toward any current best explanation is therefore *provisional but committed* — take the explanation seriously enough to commit to it operationally and hold it accountable to its predictions, while remaining open to its eventual successor.

The growth of knowledge is a philosophical parallel to these mathematical limits. OI supplies a particular example of a limit on empirical knowledge. At a fixed interface, representatives related by an established record-preserving correspondence have the same accessible record laws ([Substratum] Theorem 24). Empirical explanations using those records leave the choice among those representatives undetermined. Deutsch's case for open-ended explanatory growth is independent of that example.

One feature of Deutsch's broader program is read differently by the framework, and the divergence is worth stating precisely. Deutsch's *Beginning of Infinity* defends the many-worlds interpretation of quantum mechanics as a corollary of taking the wave function as fundamental ontology. From the framework's perspective, that commitment rests on a category error. On the framework's proposal, quantum mechanics is not fundamental: it is emergent, the post-trace-out description of how observation operates for embedded observers, and the wave function is the mathematical object that emerges. The Everettian "branches" are then not a parallel-ontologies claim about fundamental reality; they are features of the compressed emergent description, analogous to the way the partition function is a mathematical structure of statistical mechanics rather than a claim about parallel ensembles. Asking "do the branches really exist?" presupposes the wave function's formalism as direct ontology — a presupposition OI specifically denies, since the substratum is the deeper description and the wave function is what observation produces from it. The Everettian measure problem dissolves on the framework's reading because the branches are not ontological objects requiring measure assignment ([Main] §4.1); the question MWI is trying to answer is dissolved by relocating the wave function's apparent ontology one level down. The same substratum and observable descriptions also organize the distinct premise checks for Bell, Kochen-Specker, Pusey-Barrett-Rudolph and Frauchiger-Renner ([Methodology] Part III; Appendix C). Those checks retain their separate operational, preparation and agent-consistency assumptions; relocating a description alone does not establish a no-go resolution. The framework's divergence from MWI is therefore not disagreement at the epistemic-status level — where OI and BoI align — but a diagnosis: MWI is reading at the wrong level of the substrate-emergent architecture.

**What AI can infer and implement.**

| Capability | Status |
|-----------|--------|
| Discover the local invariants of $(S, \varphi)$ from observations | Possible under the reconstruction theorem's conditions |
| Build better models of the visible sector | Depends on available records, controls and resources |
| Identify the complete state from retained records | In the passive finite reversible model, requires a single supported compatible state ([Substratum] Proposition 24.5) |
| Receive a signal from beyond a cosmological causal horizon | Excluded by the assumed causal partition |
| Build faster computers | Possible given suitable implementations and resources |
| Replace a visible process with nonzero conditional memory by a faithful memoryless (Markov) model at the same horizon | Provably impossible ([Main §3.4]) |
| Decide a language outside BQP with bounded error and polynomial resources | Excluded under global coverage of Chapter 14's operational-closure and efficient simulation hypotheses |
| Achieve consciousness in the phenomenal sense | Not addressed (Ch 18 §18.10) |

**The framework's self-reference.** The framework is an account of embedded observation developed by observers within the system it describes. Its authors, readers and any AI using it can infer a quantity from their records when the supported compatible states agree on that quantity. Chapter 19 §19.3.5 discusses the separate question of initial conditions.

**Forward pointers.** Chapter 13 discusses possible implementations of conditional memory in biology. Chapter 14 characterizes BQP under a scalable model that supplies quantum control, efficient simulation and charged conditioning. A super-BQP result on physical hardware would test global coverage of that model.

The preceding links describe replication and selection under stated premises, the possible net benefits of information processing, and materials and control for neural and artificial computation. Chapters 13–17 discuss specific applications and tests.

***

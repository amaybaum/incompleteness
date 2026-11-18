# Chapter 16
# Medicine

***

> **Status — conjectural extension.** The cited observations include reversal after Mecp2 reactivation in a mouse model of Rett syndrome. They motivate tests of the proposed mechanisms. Comparative therapeutic windows and clinical benefits remain open.

## 16.1 What this chapter develops

Chapter 13 develops tests of conditional memory. Chapter 14 uses a scalable model with quantum control, efficient simulation and charged conditioning for its BQP result. Chapter 15 proposes controlled engineering tests. This chapter considers medical applications with their own experimental premises.

This chapter discusses proposed memory mechanisms and tests in pharmacology, neurodegeneration, immune signaling and epigenetics. It draws on prior experimental and clinical observations with the endpoints reported in those studies.

The chapter has explicit two-half structure.

The *first half* (§§16.2-16.8) develops the framework's content across six conventional pharmacology domains: cancer pharmacology (with checkpoint kinase inhibitors and the framework's account of why Chk1 inhibitor selectivity emerges), neurodegeneration (with CaMKII as the canonical molecular memory device and PTSD reconsolidation as $\tau_B$ pathology), antibiotic resistance (with persister cells as memory accumulation), immunotherapy (with T-cell exhaustion as TCR memory pathology), cardiac pharmacology (with use-dependent block as non-Markovian channel dynamics), and autoimmune disease (with partial JAK inhibition exploiting memory architecture). Each section identifies the C1–C4 architecture of the relevant biological system, develops the framework's structural prediction, and identifies distinguishing predictions where the framework gives different answers than standard pharmacology.

Sections 16.9–16.12 compare measurable chromatin features with expression and function. The operator distinction of Chapter 6 motivates an analogy. The evidence concerns particular molecular observations and clinical endpoints.

Section 16.13 closes the chapter with a unifying therapeutic principle: *memory asymmetry*. When a disease process depends on non-Markovian signaling dynamics that the corresponding normal tissue does not, therapies can target the *memory structure* rather than the *catalytic function* — predicting wider therapeutic windows because memory dependence is more disease-specific than catalytic activity.

Guy et al. (2007) observed neurological reversal after reactivating Mecp2 in symptomatic adult mice. This provides a prior comparison for the proposed role of reader restoration. A wider therapeutic window across disorders is a separate prediction.

## 16.2 The enzyme as a read-write system

Before developing specific disease domains, the chapter establishes the framework's structural account of enzymes as read-write systems. The account organizes the subsequent disease-by-disease content under a unified structural pattern: each disease involves a specific C1–C4 architecture, with pathology arising through alteration of the architecture's memory dynamics.

**Molecular memory mechanisms.** The framework's prediction that enzyme activity history is physically encoded in the enzyme's structure and persists across multiple catalytic cycles is well-established in molecular biology through multiple mechanisms.

*Multisite post-translational modification.* PTMs — phosphorylation, acetylation, ubiquitination, methylation — covalently alter specific residues, changing the protein's conformational landscape and activity. A protein with $N$ modifiable sites, each with $k$ possible states, has $k^N$ distinct modification patterns. For Chk1 with approximately ten regulatory phosphorylation sites, $2^{10} \approx 1{,}000$ distinct states constitute a physical memory register encoding the enzyme's recent history. Gunawardena (2012) explicitly describes this as "history-based encoding": the same cellular condition can produce different modification patterns depending on the prior history.

*Sequential phosphorylation.* Wilsker et al. (2008) found S317-dependent S345 phosphorylation in the DNA-damage response. They distinguished a mitotic mode of S345 phosphorylation independent of S317. The sequence is a biochemical result. A C4 test requires comparing histories at the same declared visible state.

*Conformational hysteresis.* Proteins occupy multiple distinct conformational states, with transitions depending on the protein's history. For kinases, the autoinhibited vs. active conformation persists on timescales much longer than individual phosphorylation events. The Chk1-S splice variant acts as an endogenous repressor whose binding/unbinding is the slow process storing the history.

*Chromatin as long-term memory.* At the network level, the histone code provides the most dramatic example. DNA damage induces histone modifications ($\gamma$H2AX, H4K20me) that persist for hours to days — far longer than the kinase cascade that wrote them.

**The memory hierarchy.** The framework's content extends across many decades of biological timescale, with each scale satisfying C1–C4 with its own characteristic $\tau_B$.

| Memory mechanism | Write operation | Storage medium | $\tau_B$ | C1–C4 role |
|---|---|---|---|---|
| Conformational hysteresis | Ligand binding | Oligomeric/regulatory state | $\mu$s-ms | C2 |
| Sequential phosphorylation | Ordered modification | Conformational accessibility | Minutes | C2 + C3 |
| Multisite PTM | Phosphorylation | Modification pattern ($2^N$ states) | Min-hrs | C3 |
| Chromatin marks | $\gamma$H2AX, methylation | Histone modification state | Hrs-days | C2 + C3 |
| DNA methylation | Methyltransferase activity | CpG state | Months-generations | C2 + C3 |

In multicellular tissues — particularly the nervous system — the same C1–C4 architecture extends upward through additional layers, each treating the layer below as its hidden sector. Synaptic-layer LTP/LTD changes (hours to days), circuit-layer engram-cell ensembles (days to months), systems-layer hippocampal-cortical dialogue (months to years), and cortical-layer distributed semantic representation (years to decades) form a five-layer architecture nested above the molecular level.

The hierarchical structure means that a perturbation at one layer (a drug, a disease process) can have effects propagating upward through layers with progressively longer $\tau_B$. The clinical time-course of memory-related diseases — and the schedule-dependence of memory-targeted drugs — reflects this layered architecture.

**The core therapeutic principle.** The framework identifies a specific therapeutic axis: *memory asymmetry*. When a disease process depends on non-Markovian signaling dynamics that the corresponding normal tissue does not depend on (or depends on differently), therapies can target the *memory structure* rather than the *catalytic function*. This is pharmacologically distinct from standard inhibition and predicts *wider therapeutic windows* because memory dependence is more disease-specific than catalytic activity.

The memory-asymmetry principle organizes the chapter's content across the disease domains in §§16.3-16.12. Each disease's pharmacology is reframed in terms of the relevant C1–C4 architecture; each therapeutic intervention is reframed in terms of its effect on the architecture's memory dynamics; each distinguishing prediction follows from this reframing.

## 16.3 Cancer pharmacology

Checkpoint kinases and their regulatory regions give candidate fast and slow variables in the DNA-damage response. Testing their contribution to cancer pharmacology requires a specified model and readout.

**Checkpoint kinase inhibitors and sensitization.** Parsels et al. report preclinical gemcitabine sensitization by Chk1 inhibition in pancreatic cancer cells. The catalytic and regulatory domains motivate a proposed partition. Coupling and retained post-translational states need their own matched-present readback test ([Medicine §3.1]).

The proposed Chk1 mechanism is that prior activation changes the next response through a retained modification or conformation. Testing it requires a history comparison at the same declared present state.

*A selectivity hypothesis.* Tumor and normal cells can depend differently on checkpoint pathways. The specific role of a persistent Chk1 state in selectivity is open.

*Why schedule matters.* Preclinical schedule effects motivate a readback hypothesis. A Markov model including present damage and cell-cycle state can also yield order effects. A matched-present comparison would test whether additional history affects sensitization.

**Radiation adaptive response.** Priming responses in particular experimental systems motivate a hypothesis involving retained chromatin changes. A history contrast with controlled current state and measure of the candidate record is required to assess that mechanism.

**Distinguishing predictions for cancer pharmacology.**

*Memory-selective scheduling.* Measure candidate checkpoint relaxation and compare schedules at matched present and exposure in a controlled model. Whether the timing predicts sensitization is open.

*Low-dose memory priming.* A controlled preclinical comparison could measure history effects at matched exposure and the same recorded present state. Exposure and toxicity require a specified comparator and direct measurements.

*Memory-targeted drugs.* Drugs that specifically disrupt the *memory structure* without blocking catalysis: accelerating the regulatory domain's slowest conformational mode (decreasing $\tau_B$) to erase checkpoint memory without blocking checkpoint activation. Such a drug would be invisible to standard kinase inhibitor screens, which measure catalytic inhibition.

These cancer applications propose measurements of checkpoint readback and treatment response. A therapeutic index benefit would need its own evidence.

## 16.4 Neurodegeneration

Lecanemab and donanemab trials reported slower decline in early Alzheimer's disease without restoration of cognition ([Medicine §4.1]). Those endpoints do not establish the proposed kinase mechanism below.

**CaMKII as a candidate memory system.** CaMKII participates in synaptic plasticity. The following features motivate a test of accessible readback:

- *C1.* The kinase domain is coupled to the regulatory/association domain through the autoinhibitory segment.
- *C2.* Autophosphorylation at T286 creates a bistable switch with persistence time of minutes to hours — much longer than individual calcium transients (~ms). $\tau_S/\tau_B \sim 10^{-4}$ to $10^{-5}$.
- *C3.* CaMKII forms dodecameric holoenzymes with 12 subunits, each independently phosphorylatable — $2^{12} = 4{,}096$ distinct modification states.
- *C4.* Test whether a measured synaptic response differs between histories of the same measured present through a retained state.
CaMKII is implicated in synaptic plasticity. Its contribution to an accessible C4 contrast and to a disease mechanism requires direct evidence.

**Kinase dynamics as a disease hypothesis.** The proposal is that changes in the relaxation time $\tau_B$ of a regulatory mode contribute to some neurodegenerative outcomes.

*Normal aging.* One hypothesis is that oxidative damage changes conformational relaxation and thereby affects plasticity.

*Alzheimer's disease.* Test whether A$\beta$ oligomers change CaMKII regulatory kinetics and whether those changes affect plasticity or tau phosphorylation.

*Parkinson's disease.* Test whether aggregate-associated changes in regulatory kinase kinetics contribute to neuronal dysfunction.

**Candidate $\tau_B$-normalizing interventions.** Test whether restoring a measured regulatory relaxation time improves a specified synaptic endpoint independently of changes in aggregate burden.

*Testable prediction.* Measure CaMKII conformational dynamics (by FRET or HDX-MS) in neurons exposed to A$\beta$ oligomers versus controls. The framework predicts that A$\beta$ shifts $\tau_B$ of CaMKII's regulatory domain. A compound that reverses this $\tau_B$ shift should rescue synaptic plasticity (measurable by long-term potentiation induction) independently of A$\beta$ clearance.

**PTSD and reconsolidation.** Intrusive memories motivate a candidate persistence model. A clinical treatment effect and the responsible memory mechanism require separate evidence.

Brunet et al. reported a benefit with propranolol and trauma reactivation. Roullet et al. found no overall PTSD symptom advantage over reactivation with placebo ([Medicine §4.5]). A proposed effect on noradrenergic re-encoding remains a mechanistic hypothesis.

Generalizing a reconsolidation intervention requires identifying the relevant memory component, checking its sensitivity to the timing of treatment and measuring the outcome.

**Focused ultrasound as a candidate perturbation.** Focused ultrasound can open the blood–brain barrier in controlled protocols. Whether it changes the relaxation time of a particular kinase requires a molecular measurement.

The proposed comparison measures the candidate $\tau_B$ and asks whether it mediates an independently measured response.

Ye et al. (2025) reported an exploratory open-label blood–brain barrier opening study in six people with Alzheimer's disease. The study did not measure CaMKII conformational dynamics or molecular timescale normalization ([Medicine §4.6]). A controlled comparison is needed to estimate efficacy.

**Proposed tests.** Compare variation in pulse timing against a measured relaxation time, with matched conditions and controls for nonspecific effects. Measure the molecular and clinical endpoints separately.

A test must distinguish the proposed kinase mechanism from other effects of the intervention.

## 16.5 Antibiotic resistance

Phenotypic tolerance and genetic resistance are distinct. A persistent cellular state is a candidate contributor to tolerance, and the proposed mechanism needs a specified readout and matched-present comparison.

**Persister cells and candidate records.** The hypothesis is that part of the stress response persists across observations and affects a later response. A model with explicit current-state variables provides a comparison.

A history contrast would ask whether different prior exposures affect the next measured response at fixed present. That result would constrain the observation law. Assigning the effect to a particular mechanism would require additional evidence.

**Memory-optimized antibiotic scheduling.** The framework's reading implies that *scheduling* of antibiotic doses matters in ways standard pharmacokinetics does not capture. Specifically:

*Continuous exposure.* The conventional "keep antibiotic above MIC for as long as possible" strategy maximizes SOS memory accumulation and therefore persister formation. This is the worst possible scheduling from the framework's perspective.

*Pulsed exposure with $\tau_B$-matched intervals.* Antibiotic pulses separated by intervals matching the SOS memory's $\tau_B$ allow the memory to relax between pulses, preventing the cumulative accumulation that produces persisters. The framework predicts this pulsed scheduling produces fewer persisters than continuous exposure at equivalent total drug exposure.

*Combination scheduling.* Combinations of antibiotics targeting different memory architectures (different bacterial signaling pathways with different $\tau_B$) can interfere with each other's memory dynamics, producing effects beyond simple additive killing. The framework predicts specific combinations and timings that exploit memory interference.

**Distinguishing predictions.**

*$\tau_B$-matched pulsed dosing.* The framework predicts that pulsed dosing with $\tau_B$-matched intervals produces fewer persister cells than continuous dosing at equivalent total drug exposure. The prediction is testable in animal models of chronic bacterial infection with measured RecA filament dynamics. Standard pharmacokinetic models predict no benefit to pulsed dosing if total exposure is matched; the framework predicts a specific benefit from $\tau_B$ matching.

*Anti-persister drugs.* Drugs that specifically accelerate RecA filament dissociation (decreasing $\tau_B$ of the SOS memory) should eliminate persisters without killing growing bacteria. This is a new drug class that the framework predicts is pharmacologically distinct from standard antibiotics; such drugs would be invisible to growth-inhibition screens.

*Memory-erasing combinations.* Combinations of $\beta$-lactams (acting on rapidly-growing bacteria) with memory-erasing agents (preventing persister formation) should produce dramatically improved outcomes in chronic infections. The framework predicts specific drug combinations from the memory architecture of bacterial signaling networks.

## 16.6 Immunotherapy and T-cell exhaustion

T-cell exhaustion — the progressive loss of T-cell effector function during chronic antigen exposure — is the dominant clinical limitation of cancer immunotherapy. Checkpoint inhibitors (anti-PD-1, anti-CTLA-4) reverse exhaustion partially but only in a fraction of patients. The framework's reading: T-cell receptor (TCR) signaling is a C1–C4 system with the exhaustion state corresponding to a specific pathological memory configuration of the regulatory machinery.

**TCR signaling as a C1–C4 system.** The T-cell receptor's signaling cascade involves multiple kinases (Lck, ZAP-70, LAT) with regulatory phosphorylation sites, all coupled to the downstream transcription factor network. C1 is satisfied through the regulatory phosphorylation network; C2 through the slow dynamics of transcription factor accumulation and dissipation; C3 through the combinatorial space of phosphorylation patterns across the cascade.

The framework's prediction: TCR signaling is non-Markovian. Chronic antigen exposure progressively writes specific PTM patterns into the kinase cascade, driving the cell toward the "exhaustion" memory state characterized by upregulated inhibitory receptors (PD-1, TIM-3, LAG-3) and downregulated effector function. The exhaustion state is not an absorbing classical phenotype but a specific memory configuration that can in principle be rewritten.

**Therapeutic implication.** Standard checkpoint inhibition (blocking PD-1/PD-L1) acts on the *effector phase* of T-cell function. The framework predicts that targeting the *memory writers* (kinases that write the exhaustion PTM pattern) or the *memory erasers* (phosphatases that remove these patterns) should be pharmacologically distinct and synergistic with standard checkpoint inhibition.

*Specifically:* The serine/threonine kinases responsible for the exhaustion-specific phosphorylation patterns (likely candidates: PKC, MAPK, and downstream effectors) are framework-predicted to be the *upstream writers* of the exhaustion state. Inhibiting these writers should prevent exhaustion development; activating the corresponding erasers should reverse established exhaustion. This is a new therapeutic axis distinct from standard checkpoint blockade.

**Distinguishing prediction: kinase regulatory-domain accelerators.** Drugs that accelerate the regulatory-domain dynamics of TCR-pathway kinases (decreasing $\tau_B$ without blocking catalytic activity) should reverse exhaustion. These drugs would be invisible to standard kinase inhibitor screens, which measure catalytic inhibition. The framework predicts that screening compound libraries against measured regulatory-domain dynamics (rather than catalytic inhibition) would identify a new class of immuno-oncology agents.

## 16.7 Cardiac pharmacology

Cardiac antiarrhythmic drugs exhibit *use-dependent block*: the drug's binding to the sodium or calcium channel depends on the channel's activation history rather than just on instantaneous membrane voltage. The phenomenon is well-established empirically (Vaughan-Williams class I antiarrhythmics, lidocaine, propafenone, flecainide) but is treated as an empirical complication of channel pharmacology. The framework's reading: use-dependent block is non-Markovian channel dynamics, with the channel acting as a C1–C4 system whose conformational memory determines drug binding affinity.

**Use-dependent block as non-Markovian channel dynamics.** Voltage-gated ion channels (Na$_V$, Ca$_V$, K$_V$) have multiple conformational states (closed, open, inactivated, slow-inactivated) with transitions on different timescales. The fast subsystem is the open/closed conformational equilibrium (microseconds); the slow subsystem is the inactivated-state dynamics (milliseconds to seconds). C1–C4 are satisfied with the standard $\tau_S/\tau_B \sim 10^{-3}$ regime characteristic of the framework's engineered partition examples.

The framework's prediction: drug binding to voltage-gated channels is non-Markovian. The drug's effective affinity depends on the channel's activation history through the slow-inactivated state's memory of recent activations. This produces the observed use-dependence: rapidly cycling channels (during tachyarrhythmias) accumulate more inactivated-state occupancy and bind drug more avidly; slowly cycling channels (during normal rhythm) accumulate less and bind less avidly.

**Therapeutic implication.** Use-dependent block produces *frequency-selective* antiarrhythmic effects: drugs preferentially affect rapidly firing pathological tissue (arrhythmic foci, reentry circuits) while sparing normally firing tissue. This is the framework's memory-asymmetry principle in cardiac pharmacology: the pathological tissue's high-frequency firing writes more memory into the channels, making them more susceptible to drug binding. The therapeutic window between antiarrhythmic effect and toxicity is determined by the difference in channel memory states between pathological and normal tissue.

**Distinguishing predictions.**

*Optimal dosing intervals.* The framework predicts that the optimal interval between antiarrhythmic doses depends on the channel's $\tau_B$ at the inactivated state. Dose intervals matching $\tau_B$ maximize the memory-write while minimizing baseline blockade; intervals much shorter or longer reduce therapeutic index. Current dosing is empirically optimized; the framework predicts calculable optima from channel kinetics.

*Memory-targeted antiarrhythmics.* Drugs that accelerate channel recovery from inactivation (decreasing $\tau_B$ of the inactivated state) should eliminate arrhythmias by erasing the memory-accumulation that produces them. This is a new therapeutic axis distinct from standard channel-blocking antiarrhythmics; such drugs would not show standard channel-blocking pharmacology and would be invisible to standard antiarrhythmic screens.

*Frequency-selective combinations.* Combinations of drugs with different channel memory profiles (different $\tau_B$ values) can produce frequency-selective effects beyond simple additivity. The framework predicts specific combinations and dosing for arrhythmias at different cycle lengths.

## 16.8 Autoimmune disease

Autoimmune disease — rheumatoid arthritis, lupus, psoriasis, inflammatory bowel disease — involves chronic activation of cytokine signaling networks centered on the Janus kinase (JAK) family. Standard immunosuppression uses high-dose, often broad-spectrum agents (corticosteroids, methotrexate, anti-TNF) with substantial side effects. JAK inhibitors (tofacitinib, baricitinib, upadacitinib) provide more targeted intervention but with characteristic dose-response patterns that conventional pharmacology has difficulty explaining. The framework's reading: JAK signaling is a C1–C4 system, and partial JAK inhibition exploits the network's memory architecture for disproportionate clinical efficacy.

**Disproportionate efficacy of partial JAK inhibition.** Clinical experience with JAK inhibitors shows that *partial* JAK inhibition (binding less than ~50% of available JAK kinases at clinically tolerable doses) produces substantial clinical efficacy in many autoimmune conditions. This is unexpected on standard Markovian models, which predict that the suppression of cytokine signaling should be roughly linear in the fraction of inhibited kinase.

The framework's account: JAK signaling is non-Markovian, with the cytokine response depending on the cumulative phosphorylation state of the JAK-STAT pathway over multiple signaling cycles. Partial inhibition produces disproportionate effects because it disrupts the memory accumulation that drives the chronic activation, even though instantaneous catalytic activity remains substantial.

**Therapeutic implication.** The framework predicts that JAK inhibitor dose-response curves should show *threshold behavior* — clinical efficacy emerges above a specific dose threshold corresponding to disruption of memory accumulation, rather than linear with kinase inhibition. Below threshold: minimal efficacy regardless of partial inhibition. Above threshold: substantial efficacy from memory disruption. This pattern matches the clinical observation of "minimum effective dose" thresholds with rapid efficacy gains above threshold.

**Distinguishing prediction: optimal scheduling.** The framework predicts that *intermittent* JAK inhibitor dosing (with intervals matching the cytokine memory's $\tau_B$, typically hours to days) should produce equivalent or superior efficacy to continuous dosing at lower cumulative drug exposure. Standard pharmacokinetic models predict continuous dosing is optimal; the framework predicts intermittent dosing exploiting memory dynamics could improve therapeutic index.

A second distinguishing prediction: combinations of JAK inhibitors with phosphatase activators (drugs that accelerate the memory erasure of the JAK-STAT pathway) should be synergistic, producing equivalent clinical effect at lower JAK inhibitor doses. This combination would be invisible to standard pharmacology screens that focus on catalytic inhibition.

***

## 16.9 Epigenetics as biological hidden sector

The second half examines chromatin features as candidate records and gene expression and phenotype as possible readouts. The relation motivates an analogy to the operator distinction from Chapter 6 §6.3.

**The C1–C4 architecture of chromatin.** The transcriptional machinery — RNA polymerase II, transcription factors, mediator complex — is the visible sector. The chromatin state — DNA methylation patterns, histone modifications, chromatin compaction, three-dimensional architecture — is the hidden sector. The four conditions are satisfied with overwhelming margin.

*C1 (coupling).* The transcriptional machinery and chromatin state are coupled through multiple mechanisms: direct physical coupling (nucleosome positioning controls promoter access, DNA methylation modulates transcription factor binding, histone tail modifications recruit reader proteins), writer-reader feedback (transcription recruits chromatin-modifying enzymes that alter the chromatin state, which modulates future transcription), and structural coupling (chromatin looping by CTCF and cohesin brings distal regulatory elements into proximity with promoters).

*C2 (memory persistence).* The chromatin state changes on timescales far slower than individual transcription events. The hierarchy is multi-scale:

| Mechanism | $\tau_B$ | $\tau_S/\tau_B$ |
|---|---|---|
| DNA methylation (CpG) | Cell generations | $\sim 10^{-6}$ |
| Histone methylation | Hours to days | $\sim 10^{-3}$ to $10^{-2}$ |
| Histone acetylation | Minutes to hours | $\sim 10^{-1}$ to $1$ |
| Chromatin compaction | Cell generations | $\sim 10^{-6}$ |
| CTCF/cohesin loops | Hours to cell generations | $\sim 10^{-3}$ to $10^{-6}$ |

The framework predicts a *hierarchy of memory range*: genes regulated primarily by DNA methylation should show history-dependence reaching furthest back (the longest retention, of order $\tau_B/\tau_S$ transcriptional events), while genes regulated primarily by histone acetylation should show the shortest-range history-dependence (approaching Markovian behavior beyond a few events). The ratio orders retention, not the size of the effect at a given lag.

*C3 (capacity).* The chromatin memory register has astronomical capacity. Approximately $28 \times 10^6$ CpG sites in the human genome with binary methylation states give $\sim 2^{28 \times 10^6}$ possible CpG methylation patterns — vastly exceeding any conceivable transcriptional state space. C3 is satisfied by approximately seven million orders of magnitude.

**Cancer as pathological epigenetic memory.** Cancer is, in the framework's language, a disease of the epigenetic hidden sector. The malignant transcriptional program is maintained not only by genetic mutations but by an aberrant epigenetic memory state — stable patterns of DNA methylation and histone modifications that lock the cell into a proliferative program. This memory is self-reinforcing: the malignant transcription writes further aberrant marks through recruited chromatin modifiers, which stabilize the malignant transcription.

The framework predicts that disrupting the memory *structure* (the stability and capacity of the epigenetic hidden sector) is a more selective anti-cancer strategy than disrupting the memory *content* (reactivating specific silenced genes). A memory-structure drug would reduce $\tau_B$ of the aberrant methylation and histone marks (making them less stable), not affect $\tau_B$ of constitutive marks (housekeeping genes, developmental identity), and selectively destabilize the tumor's pathological memory without affecting normal cellular memory.

**Aging as memory accumulation.** Aging involves progressive accumulation of epigenetic marks — the "epigenetic clock" of Horvath 2013 — that alter gene expression in ways associated with declining function. In the framework's language, aging is the accumulation of memory in the slowest epigenetic layers (DNA methylation, chromatin compaction) beyond the cell's ability to maintain functional homeostasis.

The framework predicts that aging-associated gene expression changes should show the strongest non-Markovian signatures (longest autocorrelation times) — consistent with the observation that aged cells have more stable, less plastic epigenetic states than young cells. Partial reprogramming through transient Yamanaka factor expression erases recent epigenetic memory while preserving deeper developmental identity. Conditional on the marks eroding on their retention times, the framework predicts that pulses long enough to erase recent marks but short compared with the $\tau_B$ of developmental memory preserve identity; how identity changes for longer pulses, gradually or sharply, depends on the identity network's mixing, coupling and readback, and is model-dependent unless a specific mechanism establishes it.

## 16.10 The substratum-emergent operator distinction at chromatin

The proposal distinguishes measurable chromatin states from measured downstream expression and function. The relationship depends on the particular molecular system.

**Chromatin state and downstream readout.**

*Molecular state.* Bisulfite sequencing, ChIP-seq and ATAC-seq address different features of DNA methylation, histone modifications and chromatin accessibility.

*Downstream response.* RNA-seq and functional assays measure gene expression or cellular phenotype.

Transcriptional machinery and other regulatory mechanisms relate these layers. Their molecular observables can have different dynamics.

**Empirical comparisons at chromatin.**

*iPSC reprogramming residuals.* Lin et al. (2024) describe residual source-cell epigenetic features in studied systems after a change in cell identity. Buckberry et al. (2023) show that resetting depends on the reprogramming protocol ([Medicine §9.4]).

These comparisons illustrate that epigenetic marks and phenotype can change differently. The residual marks and their magnitude depend on the protocol.

*Bivalent chromatin states.* Bernstein et al. (2006) reported coexisting H3K4me3 and H3K27me3 at lineage-control loci with low or poised expression. The observation concerns the marks and expression, without a conservation or exact-cancellation result.

*Multi-timescale chromatin dynamics.* Single-molecule and single-cell measurements directly observe distinct dynamics on subsecond and minutes timescales for the same histone modifications on the same nucleosomes (Stasevich et al. 2014; Saxton et al. 2023). Histone acetylation modulates transcriptional burst frequency rather than burst size (Nicolas-Phillips et al. 2018), a stochastic-emergent-output pattern consistent with the framework's prediction that emergent operators have specific functional relationships to substratum operators rather than being identical to them.

These results motivate studying chromatin marks and measured output separately.

Applying the formal physical operator distinction would require a specified molecular model and correspondence.

The observed chromatin and expression comparisons supply inputs to that proposal.

## 16.11 Reader, writer, and eraser pharmacology

Current epigenetic therapeutics are organized along three axes that correspond directly to the framework's substratum-emergent operator distinction at the operational drug-development level. The three-axis pharmacology — *readers*, *writers*, *erasers* — is the structural pattern of any therapeutic approach to a substratum-emergent operator pair: target the substratum maintenance machinery (writers and erasers, which establish and remove substrate marks) or the substratum-to-emergent translation machinery (readers, which couple substrate state to downstream function).

**The three axes.**

*Writers.* DNA methyltransferase inhibitors (DNMT inhibitors): 5-azacytidine, decitabine. Histone methyltransferase inhibitors (HMT inhibitors): EZH2 inhibitors (tazemetostat for follicular lymphoma), DOT1L inhibitors (under investigation). Writers act on the substratum-maintenance machinery — they prevent or accelerate the writing of substrate-level marks.

*Erasers.* Histone deacetylase inhibitors (HDAC inhibitors): vorinostat, romidepsin (approved for cutaneous T-cell lymphoma), panobinostat. Histone demethylase inhibitors (LSD1, KDM5 family inhibitors under investigation). Erasers act on the substratum-erasing machinery — they prevent or accelerate the removal of substrate-level marks.

*Readers.* BET bromodomain inhibitors: JQ1 (preclinical), ZEN-3694, BI 894999 (clinical investigation). Methyl-lysine reader inhibitors (under investigation). Readers act on the substratum-to-emergent translation machinery — they prevent the substrate-level marks from being read as downstream functional output.

**The framework's structural reading.** The three-axis organization follows structurally from the operator distinction. Any therapeutic approach to a substratum-emergent operator pair must target one of three functional roles: substratum maintenance (writers), substratum erasure (erasers), or substratum-to-emergent translation (readers). The empirical organization of epigenetic drugs into exactly these three classes is the framework's substratum-emergent operator distinction made operational.

**Combination and scheduling hypothesis.** The proposed link between measured relaxation times and combination scheduling can be tested for particular targets and regimens.

- *Writer + reader.* The cited p300/CBP and BET work reports preclinical combination results in NUT carcinoma.
- *Eraser + reader.* HDAC inhibitor + BET inhibitor combinations are under clinical investigation in NUT carcinoma and other contexts.
- *Writer + eraser.* DNMT and HDAC inhibitor combinations have preclinical evidence. Trial E1905 compared azacitidine with and without entinostat in MDS/AML ([Medicine §9.5]). It did not measure a relaxation-time-matched optimum.

Clinical activity and preclinical synergy are distinct outcomes. Schedule comparisons need specified doses, timing, and endpoints.

The proposed test asks whether a measured $\tau_B$ predicts combination response at a specified interval.

## 16.12 A therapeutic-window hypothesis for reader-writer disorders

Rett mouse rescue provides prior evidence of reversibility after restoring Mecp2. A wider therapeutic-window pattern across disorders and mechanisms is a separate comparative hypothesis.

**The reader-writer disorder class.** Several genetic disorders are caused by mutations affecting epigenetic reader or writer proteins:

*Rett syndrome.* MECP2 (methyl-CpG binding protein 2) — a reader of DNA methylation. Loss-of-function mutations produce severe neurodevelopmental disability primarily in females.

*Fragile X syndrome.* FMR1 — controls RNA binding and translation. Loss-of-function produces intellectual disability. Strictly an RNA-binding protein rather than a chromatin reader, but with structural similarities to chromatin readers in its functional role.

*Angelman syndrome.* UBE3A — ubiquitin ligase. Loss-of-function on the maternal allele produces severe developmental disability. Related to chromatin biology through ubiquitin-mediated histone modification.

*Kabuki syndrome.* KMT2D is an H3K4 methyltransferase, and KDM6A removes H3K27 methylation. Pathogenic variants in either gene can cause Kabuki syndrome ([Medicine §10.7]).

*ATR-X syndrome.* ATRX — chromatin remodeler involved in heterochromatin maintenance. Loss-of-function produces $\alpha$-thalassemia with X-linked intellectual disability.

**The framework's hypothesis.** Compare the age or time after onset at which targeted restoration still improves a specified endpoint with that for a defined alternative. The usable window depends on the disorder, intervention, restored activity and outcome.

Guy et al. (2007) observed neurological rescue including in symptomatic adult mice after reactivating endogenous Mecp2, and recovery of hippocampal long-term potentiation. The study establishes reversibility under that intervention in the mouse model.

The comparison motivating a wider window for some reader-writer disorders would require matched treatment ages or stages, restored activity and endpoints. Methylation preservation and its relevance to rescue need separate evidence.

**Proposed generalization.** Test reversibility across disorders with appropriately matched comparisons and measured restoration of function.

*Fragile X.* A proposed test is whether restoration of FMR1 improves a specified functional endpoint after symptom onset. The outcome and its dose dependence need to be established.

*Angelman syndrome.* Topoisomerase inhibitors and antisense oligonucleotides targeting UBE3A-ATS show preclinical efficacy with restored UBE3A function. The framework predicts substantive phenotypic improvement at partial restoration levels.

*Kabuki syndrome and ATR-X.* Studies could test whether restoring affected chromatin machinery improves a declared outcome at different stages. Responsiveness across disorders remains open.

A class-wide pattern requires comparisons that distinguish timing and extent of response from other influences on phenotype.

**The cancer methylome classifier comparison.** Capper et al. developed an earlier CNS tumor classifier and reported diagnostic changes in up to 12% of a prospective series. Sill et al. report 95% subclass accuracy in nested cross-validation for Heidelberg v12.8 (see Chapter 17 §17.7). These are results for specific classifiers and validation designs.

The clinical classification results motivate comparing the information in methylation with other assays on the same target and cohort. They do not show that the methylation state remains unchanged or establish an OI mechanism.

## 16.13 Chapter close: memory asymmetry as unifying principle

The framework's content across the chapter is organized by a single therapeutic principle: *memory asymmetry*. When a disease process depends on non-Markovian signaling dynamics that the corresponding normal tissue does not depend on (or depends on differently), therapies can target the memory structure rather than the catalytic function. The framework predicts wider therapeutic windows for memory-structure therapies because memory dependence is more disease-specific than catalytic activity.

**The unifying principle across the chapter's content.**

*Cancer.* Preclinical Chk1 sensitization and scheduling results motivate matched-present tests of regulatory memory and an independent therapeutic comparison.

*Neurodegeneration.* Test whether kinase kinetics mediate a synaptic response independently of amyloid clearance. Propranolol trials in reconsolidation give mixed clinical evidence, and the exploratory focused ultrasound study leaves the molecular mechanism untested.

*Antibiotic response.* Persistent cellular states can motivate tests of a history-dependent response. A treatment effect and mechanism need evidence under specified conditions.

*Immunotherapy.* A proposed test is whether changes to a candidate persistent signaling state alter exhaustion-related outcomes while preserving acute responses.

*Cardiac pharmacology.* Use-dependent block can be modeled through channel state. A conditional-memory test requires histories matched on a declared present readout.

*Autoimmune disease.* A memory-mediated account of nonlinear responses to partial inhibition is a hypothesis to test against alternative signaling models.

*Epigenetics.* Mouse Rett rescue motivates comparative tests of targeted functional restoration. Therapeutic windows in other disorders are open.

**Three categories of empirical content.**

The chapter's content sorts into three empirical categories.

*Prior observations.* Adult mouse rescue, specific methylation classifier results and preclinical Chk1 scheduling effects provide comparisons. Each supports the finding at its measured endpoint.

*Proposed tests.* Controlled timing comparisons and molecular readouts could assess the Chk1, CaMKII and focused-ultrasound mechanisms. The reader-writer window hypothesis requires disorder-specific comparisons.

*Open clinical development.* The framework predicts new drug classes — memory-targeted drugs (Chk1 regulatory-domain accelerators), $\tau_B$-normalizing drugs (neurodegeneration), anti-persister drugs (antibiotic resistance), regulatory-domain accelerators (immunotherapy) — that are pharmacologically distinct from current standards. These drug classes are not currently in development; they would require dedicated screening programs measuring regulatory dynamics rather than catalytic inhibition.

The medical proposals share a conditional readback diagnostic. Their mechanisms and intervention effects require independent evidence.

The observed comparisons motivate further tests of the specified mechanisms and clinical hypotheses.

**Forward pointers.** Chapter 17 discusses limits of prediction with a declared observation set, tissue-specific benchmarks and descriptive evolutionary trends, together with tests of candidate mechanisms.

The applications in Chapters 13–17 range from empirical comparisons to proposed tests. The claims depend on their stated observables, interventions and models.

***

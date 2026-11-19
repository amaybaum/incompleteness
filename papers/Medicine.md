# Non-Markovian Dynamics in Biology and Medicine
### Molecular Memory as a Unifying Framework for Disease Mechanisms and Therapeutic Design

**Author:** Alex Maybaum  
**Date:** April 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Biology / Pharmacology

---

## Abstract

The finite-horizon result of the Observational Incompleteness (OI) framework [1] identifies accessible memory when two histories ending at the same measured present give different next-step laws through the hidden record (C4). Coupling, persistence and capacity can enable this contrast. The molecular examples below are applications to specified observables. Their readback mechanisms and any accessible-window P-indivisibility need separate evidence.

We develop applications in seven areas: cancer pharmacology, neurodegeneration and reconsolidation, antibiotic responses, immunotherapy, cardiac pharmacology, autoimmune disease, and management of genetic disorders. We propose testing for differences in the retention and readback of regulatory states between disease and comparison tissues. The layered-memory hypotheses include chromatin, synaptic and slower records. A role for focused ultrasound in modifying a molecular timescale is a proposed mechanism. We give twenty-six numbered predictions and three layer-specific sub-predictions on reconsolidation and ultrasound. Section 11 distinguishes comparisons with earlier evidence and proposed tests.

---

> **Status — conjectural extension.** Prior observations, including reversal after Mecp2 reactivation in a mouse model of Rett syndrome (Guy et al. 2007), motivate the applications. The comparative therapeutic window, the proposed mechanism and the clinical intervention effects remain open.

## 1. Introduction

Standard pharmacological models treat enzyme catalysis, receptor signaling, and ion channel gating as Markovian processes — each event is independent of prior history, and the system's future depends only on its current state. Michaelis-Menten kinetics, Hodgkin-Huxley channel models, and Hill-equation dose-response curves all embed this assumption. When history-dependent behavior is observed (use-dependent drug block, adaptive radiation responses, schedule-dependent chemotherapy efficacy), it is accommodated by adding internal states to the Markov model — often many states, without a unifying principle for when they are needed or how many to include.

The Observational Incompleteness (OI) framework [1] provides such a principle. It was originally developed for fundamental physics, where it proves three results about an embedded observer's finite observable law. First, on every finite horizon every finite stochastic law has a finite reversible deterministic realization and an exact representation by a finite-dimensional unitary system with Born-rule readout, measured projectively in one fixed basis at every step from an initial state diagonal in it [1, §3.4]. The representation is universal, Markov laws included, so representability alone does not distinguish memory-bearing laws; history readback does. Second, history readback (C4) holds exactly when the observable law has positive conditional memory $M_t = I(X_{<t}; X_{t+1} \mid X_t)$ at some accessible time — a failure of the Markov factorization at that order — and every faithful deterministic realization of such a law then carries readout-relevant hidden predictive memory at that time; conversely, such memory in any one faithful realization forces $M_t > 0$ [1, §3.4]. Quantitatively, a readback gap at order $k$ between two histories, each occurring together with the common present state with probability at least $p_0$, whose next-step laws are at total-variation distance at least $\delta$, gives $M_k \geq p_0\delta^2/\ln 2$ bits [1, §2.3]. Coupling, persistence and capacity do not imply readback: they admit realizations whose visible law has $I(X_{<t}; X_{>t} \mid X_t) = 0$ at every time on arbitrarily long accessible horizons [1, §2.3]. Third, on one fixed finite reversible representative, with a hidden prior shared by every root and drawn independently of it, the rooted visible family is P-indivisible somewhere in its recurrence cycle whenever some rooted visible map is not a permutation [1, §2.3]. Every non-deterministic visible step supplies such a map, so recurrence-scale indivisibility occurs also in laws that are Markov on every accessible window. With a full-support visible prior this indivisibility is equivalent to $M_k > 0$ at some order $k$ below the recurrence time; that memory obstruction may lie at any order below the recurrence time, and accessible statistics witness it only through a readback gap at an accessible order, which recurrence does not guarantee and C4 asserts [1, §2.3]. The framework's core theorem is abstract and scale-independent. It identifies four conditions under which a fast subsystem's observable law carries conditional memory on accessible timescales:

**C1 (Coupling).** Hidden degrees of freedom affect the evolution of the fast subsystem (visible sector) at some accessible step: the conditional law of some visible transition depends on the hidden state. In the biological realizations below the coupling is bidirectional.

**C2 (Memory persistence).** The written record persists to readback — realized here by a slow hidden sector, its relaxation timescale $\tau_B$ greatly exceeding the fast subsystem's event timescale $\tau_S$ ($\tau_S / \tau_B \ll 1$), one sufficient route. The hidden sector retains correlations from past interactions across many fast events.

**C3 (Capacity).** The hidden sector has enough distinguishable states to encode the observed conditional past–future information, $\log_2|\mathcal{C}_H| \geq I^*$ with $I^* = \sup_t I(X_{<t}; X_{>t} \mid X_t)$. In the biological realizations below it has many more accessible states than the fast subsystem, room to store the interaction history without saturation.

**C4 (History readback).** At some accessible order, two visible histories ending in the same present state induce different next-step laws, the difference mediated through the hidden sector's state.

When C1–C4 are satisfied, the characterization theorem [1, §3.4] proves that the fast subsystem's dynamics is memory-bearing — non-Markovian (P-indivisibility, which holds at the recurrence scale from a non-permutation rooted map and finiteness, is a distinct property — on a common window, with a full-support visible prior, the stronger one) — so that transition probabilities at time $t$ depend on the system's history, stored in the hidden sector's state and returned through the coupling. The ratio $\tau_S / \tau_B$ of fast to slow timescales sets how long the record is retained, not how large the history-dependence is (§2.2).

Enzymes, kinases, ion channels and receptors provide candidate systems with fast and slow degrees of freedom. The rate, accessible state and persistence of the proposed record depend on the system. Testing memory requires the history comparison in C4.

This paper develops the medical implications of this observation across seven domains, identifies a unifying therapeutic principle (memory asymmetry), and presents twenty-six numbered predictions and three sub-predictions, including retrospective comparisons and proposed discriminating tests.

---

## 2. The Enzyme as a Read-Write System

### 2.1 Molecular memory mechanisms

The OI prediction requires that an enzyme's activity history is physically encoded in its structure and persists across multiple catalytic cycles. This is well-established through multiple mechanisms.

**Multisite post-translational modification.** PTMs — phosphorylation, acetylation, ubiquitination, methylation — covalently alter specific residues, changing the protein's conformational landscape and activity. A protein with $N$ modifiable sites, each with $k$ possible states, has $k^N$ distinct modification patterns. For Chk1 (with $\sim 10$ regulatory phosphorylation sites): $2^{10} \approx 1{,}000$ distinct states — a physical memory register encoding the enzyme's recent history. Gunawardena (2012) explicitly describes this as "history-based encoding" — the same cellular condition can produce different modification patterns depending on the prior history.

**Sequential phosphorylation.** Wilsker et al. [17] found S317-dependent S345 phosphorylation for Chk1 in the DNA-damage response and distinguished a mitotic mode of S345 phosphorylation that is independent of S317. A sequential mechanism documented in an enlarged biochemical state does not by itself measure the C4 contrast at fixed present.

**Conformational hysteresis.** Proteins occupy multiple distinct conformational states, with transitions depending on the protein's history. For kinases, the autoinhibited vs. active conformation persists on timescales much longer than individual phosphorylation events. The Chk1-S splice variant acts as an endogenous repressor whose binding/unbinding is the slow process (C2) storing the history.

**Chromatin as long-term memory.** At the network level, the histone code provides the most dramatic example. DNA damage induces histone modifications ($\gamma$H2AX, H4K20me) that persist for hours to days — far longer than the kinase cascade that wrote them.

### 2.2 The key parameter

The ratio $\tau_S / \tau_B$ sets how long a written record survives, not how large its effect is. Under uniform erosion of the hidden record it fixes the loss per event, of order $\tau_S / \tau_B$, and a retention window of order $\tau_B / \tau_S$ events [1, §2.3]. The size of the history-dependence is set by how strongly the coupling writes the record and reads it back, bounded by capacity. When the ratio is very small (e.g., $10^{-12}$ for enzyme active site electronics vs. scaffold motions), the record persists across very many events. When the ratio approaches 1 (e.g., for allosteric sites where regulatory dynamics is comparable to the catalytic cycle), the record decays within a few events, and history-dependence is confined to short lags.

The memory hierarchy spans many decades of timescale. At the molecular level:

| Memory mechanism | Write operation | Storage medium | $\tau_B$ | C1–C4 role |
|---|---|---|---|---|
| Conformational hysteresis | Ligand binding | Oligomeric/regulatory state | $\mu$s–ms | C2 |
| Sequential phosphorylation | Ordered modification | Conformational accessibility | Minutes | C2 + C3 |
| Multisite PTM | Phosphorylation | Modification pattern ($2^N$ states) | Min–hrs | C3 |
| Chromatin marks | $\gamma$H2AX, methylation | Histone modification state | Hrs–days | C2 + C3 |
| DNA methylation | Methyltransferase activity | CpG state | Months–generations | C2 + C3 |

In multicellular tissues — particularly the nervous system — the same C1–C4 architecture extends upward through additional layers, each treating the layer below as its hidden sector:

| Memory layer | Substrate | $\tau_B$ |
|---|---|---|
| Synaptic | LTP/LTD weight changes (AMPA trafficking) | hr–days |
| Circuit | Engram-cell ensembles, recurrent dynamics | days–months |
| Systems | Hippocampal–cortical consolidation dialogue | months–years |
| Cortical | Distributed semantic representation | years–decades |

The hierarchical structure means that a perturbation at one layer (a drug, a disease process) can have effects propagating upward through layers with progressively longer $\tau_B$. The clinical timecourse of memory-related diseases — and the schedule-dependence of memory-targeted drugs — reflects this layered architecture.

### 2.3 The core therapeutic principle

In disease contexts, the framework identifies a specific therapeutic axis: **memory asymmetry**. When a disease process depends on non-Markovian signaling dynamics that the corresponding normal tissue does not depend on (or depends on differently), therapies can target the *memory structure* rather than the *catalytic function*. This is pharmacologically distinct from standard inhibition and predicts wider therapeutic windows because the target (memory dependence) is more disease-specific than the target (catalytic activity).

### 2.4 Reconstructive consequences of memory access

C1–C4 do not by themselves make memory access disturb the stored record. Readback requires that the hidden state influence the visible transition (C1); it does not require the visible sector to act back on the hidden state. In the bijection $(v,h)\mapsto(v\oplus h,\,h)$ on two bits, C1–C4 hold, every step reads the hidden bit, and the hidden bit never changes [1, §3.4]. In the biological realizations considered here the coupling is bidirectional (§1). Under that premise, wherever the hidden update at an access step depends on the visible state, the re-stored trace is a function of both the original hidden state and the visible-sector context at the moment of access.

This conditional connects the architecture to the *reconstructive nature of recall*, a phenomenon long established in cognitive science, without deriving it: pure address-store memory, where access leaves the substrate unchanged, is compatible with C1–C4, as the example above shows. That biological recall is reconstructive is an empirical finding, and the bidirectional coupling it presupposes is a premise about the biological realization.

**Clinical comparison: reconsolidation.** Recall can make some memory traces susceptible to change. In trials of propranolol with trauma reactivation, Brunet et al. reported a symptomatic benefit, while Roullet et al. found no overall advantage in post-traumatic stress symptoms over reactivation with placebo [21, 22]. The model proposes that intervention during re-storage could affect a specific trace, with the mediator requiring direct evidence.

The framework predicts that this approach generalizes: any memory layer with a measurable $\tau_B$ should have a corresponding "reconsolidation window" during which targeted intervention can rewrite the memory at that layer without affecting memories already consolidated to slower layers. The selectivity is not coincidental — it follows from the layered architecture of §2.2.

### 2.5 Forgetting and finite capacity

Standard accounts treat forgetting as a failure of memory. C1–C4 do not require forgetting: they bound persistence from below, and a hidden sector with infinite $\tau_B$ can satisfy them while the visible record keeps changing, as in the example of §2.4. A weaker statement holds for any finite register. If $U_1, \ldots, U_n$ are mutually independent inputs and $H$ is the state, after those inputs, of a hidden register with state space $\mathcal{C}_H$, then $\sum_i I(U_i; H) \leq \log_2|\mathcal{C}_H|$: by the chain rule $I(U_1, \ldots, U_n; H) = \sum_i I(U_i; H \mid U_{<i})$; independence gives $I(U_i; H \mid U_{<i}) = I(U_i; H, U_{<i}) \geq I(U_i; H)$; and $I(U_1, \ldots, U_n; H) \leq \log_2|\mathcal{C}_H|$, the largest entropy a variable on $\mathcal{C}_H$ can have. A finite register therefore cannot retain an unbounded stream of independent inputs: on average it forgets or fails to encode them. Finite, layer-matched $\tau_B$ is a hypothesis about how biological memory meets that constraint, not a requirement of C1–C4.

The brain operates in the parameter regime where each layer's $\tau_B$ is matched to that layer's functional role. Pattern separation requires fast forgetting at the molecular layer; generalization requires consolidation transfer from fast to slow layers; fear extinction and mood regulation require active erasure at intermediate layers.

**Clinical consequence: memory disorders are $\tau_B$ disorders.** From the framework's perspective, the relevant clinical question for any memory-related condition is not "is the memory intact or damaged?" but "which layer's $\tau_B$ has shifted, and in which direction?" This reframes:

- **Excessive retention** (PTSD, OCD intrusive thoughts, depressive rumination) → $\tau_B$ too long at the affected layer
- **Failure of new encoding** (anterograde amnesia, attention deficits) → $\tau_B$ too short, or write-rate too low
- **Selective loss of old content** (retrograde amnesia, semantic dementia) → loss of substrate at affected layer
- **Failure of cross-layer transfer** (Korsakoff's syndrome, sleep-deprivation-induced consolidation failure) → disruption of layer-coupling mechanisms
- **Mixed pattern** (normal aging, Alzheimer's) → $\tau_B$ shifts at multiple layers in opposite directions

The therapeutic axis follows directly: $\tau_B$-normalizing interventions targeting the specific affected layer, rather than broad-spectrum receptor pharmacology.

---

## 3. Cancer Pharmacology

### 3.1 Checkpoint kinase inhibitors and selective tumor sensitization

Chk1 inhibition has sensitized pancreatic cancer cells to gemcitabine in preclinical work [4]. Chk1's catalytic and regulatory regions suggest a candidate partition for follow-up. Measuring conditional memory would require specifying the present observable and comparing different histories at its fixed value.

**The prediction.** Previous damage could alter the next checkpoint response through retained phosphorylation or conformational states. This proposal concerns history beyond a declared present measurement. A perturbation of the candidate regulatory record could help test its contribution.

**A selectivity hypothesis.** Sensitization could differ between tumor and normal cells if they rely differently on the checkpoint. The contribution of regulatory memory to that difference remains to be tested.

**Why schedule matters.** Preclinical schedule dependence motivates a history test. A Markov model including current damage, phosphorylation and cell-cycle state can also respond differently to two drug sequences. A matched-present comparison is needed to identify C4 for the chosen observables.

### 3.2 Radiation adaptive response

Radiation-adaptive responses have been reported in particular experimental systems. Retained chromatin changes are a candidate mediator. Testing that account requires a contrast at fixed measured present and controls for other damage-response states.

### 3.3 Therapeutic strategies from memory asymmetry

**Memory-selective scheduling.** A hypothesis is that timing affects sensitization through a retained checkpoint state. Compare schedules in a controlled model with measured retention and matched comparator exposure. The interval and magnitude of any benefit remain open.

**Low-dose memory priming.** A controlled preclinical comparison could test whether a priming history affects subsequent sensitization at matched present and exposure. Effects on total exposure and toxicity would require a specified comparator regimen and direct measurements.

**Memory-targeted drugs.** A candidate intervention would alter a slow regulatory mode while preserving acute catalysis. Its effects on later checkpoint response and matched controls would test the hypothesis.

---

## 4. Neurodegeneration

### 4.1 The failure of the amyloid hypothesis

Anti-amyloid trials of lecanemab and donanemab reported slower decline in early Alzheimer’s disease without restoration of cognition [23, 24]. A proposed kinase mechanism and its causal contribution to clinical outcomes require separate tests.

### 4.2 CaMKII as the canonical C1–C4 system

CaMKII is involved in synaptic plasticity. The following features motivate a candidate partition for a readback test:

- **C1:** The kinase domain is coupled to the regulatory/association domain through the autoinhibitory segment
- **C2:** Autophosphorylation at T286 creates a bistable switch with persistence time of minutes to hours — far longer than individual calcium transients ($\sim$ms)
- **C3:** CaMKII forms dodecameric holoenzymes with 12 subunits, each independently phosphorylatable — $2^{12} = 4{,}096$ distinct modification states

CaMKII provides a candidate molecular record in synaptic plasticity. Showing a history-dependent response at fixed present and its role in neurodegeneration requires further evidence.

### 4.3 The OI prediction

The medical hypothesis is that changes in regulatory kinetics of synaptic kinases contribute to some neurodegenerative phenotypes. The following mechanisms are proposed.

- **Normal aging:** Gradual increase in $\tau_B$ (slower conformational relaxation due to oxidative damage) $\to$ excessive memory retention $\to$ synaptic rigidity $\to$ reduced plasticity
- **Alzheimer's:** A$\beta$ exposure could alter CaMKII regulatory dynamics and thereby affect synaptic function. Pathway effects, including proposed links to tau phosphorylation, need independent measurement.
- **Parkinson's:** $\alpha$-synuclein aggregates alter the conformational dynamics of LRRK2 and other PD-associated kinases

### 4.4 Therapeutic implication

**Candidate $\tau_B$-normalizing interventions.** Test whether changing a measured kinase relaxation time preserves synaptic function and whether the effect can occur independently of changes in aggregate burden.

**Testable prediction:** Measure CaMKII conformational dynamics (by FRET or HDX-MS) in neurons exposed to A$\beta$ oligomers vs. controls. The framework predicts that A$\beta$ shifts $\tau_B$ of CaMKII's regulatory domain. A compound that reverses this $\tau_B$ shift should rescue synaptic plasticity (measurable by LTP induction) independently of A$\beta$ clearance.

### 4.5 PTSD as $\tau_B$ pathology with reconsolidation as therapy

PTSD involves abnormally persistent and intrusive memory of traumatic events. From the framework's perspective, this is a representative case of *failure of $\tau_B$ to be appropriately finite* at the relevant memory layer — the trauma-encoded trace persists at a layer where it should have decayed and continues to drive visible-sector dynamics (intrusive re-experiencing, hyperarousal).

Brunet et al. reported a clinical benefit for propranolol with trauma reactivation. Roullet et al. found no overall symptom advantage over reactivation with placebo [21, 22]. The proposal attributes a possible effect to altered noradrenergic processing during recall. The clinical comparison does not identify that mediator.

**Predictions for further development:**

- The same approach should generalize to other layers. Targeting memory layers slower than noradrenergic emotional encoding (e.g., the cortical-layer trace itself) would require longer-acting interventions during longer reconsolidation windows.
- The optimal interval between reconsolidation-and-blockade sessions should match the targeted layer's $\tau_B$. Single-session protocols are likely sub-optimal for memories that have consolidated to slower layers.
A layer-selective intervention would need to establish which timing window and memory component it affects.

### 4.6 Direct mechanical access via low-intensity focused ultrasound

Focused ultrasound can perturb tissue mechanically and can be used in protocols that open the blood–brain barrier. Whether a particular protocol changes conformational dynamics of a target kinase is a separate molecular question.

The proposal is to test whether the intervention changes a specified molecular relaxation timescale $\tau_B$ and whether that change mediates a relevant response.

**Clinical comparison.**

Ye et al. [25] reported an exploratory six-person open-label blood–brain barrier opening study in Alzheimer's disease. It measured clinical and imaging outcomes without an assay of CaMKII kinetics. A controlled study would be needed to estimate a treatment effect, with a molecular assay to test the proposed mediator.
Reports of neuromodulation with focused ultrasound motivate separate tests of the cellular pathways involved.

**Proposed mechanism tests for focused ultrasound.**

- Measure the target relaxation time and test whether effects vary with pulse timing under matched exposure and readout conditions.
- Compare protocols at defined intervals and measure any persistence of the target response.
- Separate any target response from nonspecific tissue effects and assess safety independently.

A mechanistic comparison needs the target readout, a matched control and distinct molecular and clinical endpoints.

### 4.7 The brain memory hierarchy (extension)

The five-layer extension introduced in §2.2 — synaptic, circuit, systems, cortical — applies most directly to the brain. Each layer is the hidden sector for the layer above; each layer has its own $\tau_B$ inherited from but coarse-grained relative to the layer below.

This hierarchical picture provides natural framework-level interpretations of several established neuroscience phenomena:

- **Long-term potentiation** is the canonical example of cross-layer information transfer. A fast input (Ca²⁺ transient) writes to a fast molecular memory (CaMKII), which writes to synaptic-layer state (AMPA receptor density), which writes to slower structural state (spine enlargement), which eventually writes to the slowest available layer (gene expression and protein synthesis). Each transition is information transfer between hidden-sector layers.
- **Sleep consolidation** is the period during which the systems-layer $\tau_B$ becomes accessible. Waking input dominates the cortex; sleep allows the natural relaxation dynamics of the slow hidden sector to proceed. The replay events documented in slow-wave sleep and REM are the framework-required mechanism for inter-layer transfer.
- **Phenomenology of remembering across timescales** — recent memories with rich sensory detail, medium-age memories with preserved event structure but fading sensory content, old memories with semantic gist but reconstructed episodic detail — maps onto the layered $\tau_B$ architecture quantitatively.

These are *extensions* of the framework's primary content (molecular memory and disease pharmacology) rather than independent derivations. They provide a coherent interpretive frame for brain memory phenomena without claiming the framework derives the specific phenomenology of episodic recall, the hippocampal indexing role, or working memory as distinct from long-term storage. These remain biological and cognitive-science questions outside the framework's current scope.

---

## 5. Antibiotic Resistance

### 5.1 Persister cells as memory accumulation

Persister cells can survive antibiotic treatment through transient phenotypic tolerance. The SOS response is one candidate variable omitted by a coarse description. The proposed persistence mechanism and its matched-present history effect require independent evidence.

### 5.2 The OI prediction

The proposal tests whether a persistent stress-response state contributes to phenotypic tolerance beyond what the measured present predicts. Switching models with additional state variables provide a relevant comparison.

### 5.3 Memory-optimized antibiotic scheduling

The interval between doses should be optimized for the bacterial SOS memory timescale ($\tau_B$ of RecA filament dynamics), not just the drug's pharmacokinetic half-life:

- *Dose interval $< \tau_B$:* SOS memory accumulates $\to$ drives persister formation (counterproductive)
- *Dose interval $> \tau_B$:* Memory decays $\to$ each dose is independent (no accumulation)
- *Optimal interval $\approx \tau_B$:* Partial memory decay prevents persister threshold crossing while residual memory maintains sensitization

Clinical studies showing pulsed antibiotic regimens outperforming continuous regimens are consistent with this prediction — the mechanism is disruption of bacterial memory, not pharmacokinetic optimization.

---

## 6. Immunotherapy and T Cell Exhaustion

### 6.1 The exhaustion problem

PD-1/PD-L1 checkpoint inhibitors work in only $\sim 20$–$30\%$ of patients. The primary barrier is T cell exhaustion — progressive loss of effector function due to chronic antigen stimulation.

### 6.2 TCR signaling as a C1–C4 system

The TCR cascade contains kinases with multiple phosphorylation sites and regulatory domains. These provide candidate persistent states. Testing C4 requires specifying the measured present and assessing the effect of earlier histories.

### 6.3 The OI prediction

A proposed mechanism is that repeated stimulation leaves regulatory records which influence later T-cell responses. The relationship between those records, transcriptional changes and exhaustion needs a causal comparison at specified times and conditions.

### 6.4 Therapeutic implication

**Memory erasure + checkpoint inhibition.** PD-1 inhibitors release the inhibitory brake but do not erase accumulated TCR signaling memory. Combining PD-1 inhibitor with a "memory eraser" — a drug that accelerates conformational relaxation of TCR signaling kinases (decreasing $\tau_B$) — should rescue T cell function more effectively than PD-1 inhibitor alone.

---

## 7. Cardiac Pharmacology

### 7.1 Use-dependent block as non-Markovian channel dynamics

Use-dependent channel block provides a candidate history effect in a reduced readout. A kinetic model that includes current channel occupancy can also account for use dependence. A C4 test must specify the present measurements and compare histories at their fixed values.

### 7.2 Therapeutic implication

**Heart-rate-adapted dosing.** Antiarrhythmic dosing should be adapted to the patient's *heart rate pattern*, which determines the channel memory state. A patient with persistent tachycardia has channels in a different memory state than a patient with intermittent tachycardia. For drugs with strong use-dependence (flecainide, lidocaine), this could substantially improve the therapeutic window by avoiding pro-arrhythmic effects at high heart rates.

---

## 8. Autoimmune Disease

### 8.1 Disproportionate efficacy of partial JAK inhibition

Partial JAK inhibition can have nonlinear effects on signaling. A proposed role for a persistent regulatory state would require a matched-present history comparison and a quantitative account of response.

### 8.2 The OI prediction

Partial inhibition disrupts the *memory structure* of JAK signaling without fully blocking transduction. The pathological signaling in autoimmune disease involves accumulated PTM/conformational memory from chronic cytokine stimulation. Partial inhibition erases this memory faster than it blocks acute signaling, producing disproportionate reduction in the chronic (memory-dependent) disease component.

### 8.3 Therapeutic implication

**Memory-selective JAK modulation.** Drugs that selectively accelerate JH2 conformational relaxation — erasing accumulated inflammatory memory without blocking acute immune responses — would predict wider therapeutic windows than current JAK inhibitors: disease activity reduced while acute immune competence is preserved.

---

## 9. Epigenetics as the Biological Hidden Sector

### 9.1 The C1–C4 architecture of chromatin

Chromatin marks can persist and influence later expression. Their presence and lifetime motivate a test of readback at fixed present expression or another declared observable.

The chromatin hidden sector operates at multiple nested timescales:

| Layer | Mechanism | $\tau_B$ | Biological function |
|---|---|---|---|
| 1 (fastest) | Histone acetylation | Minutes–hours | Rapid signal response |
| 2 | Histone methylation | Hours–days | Lineage commitment |
| 3 | DNA methylation | Cell generations | Cell type memory |
| 4 | Chromatin compaction | Cell generations | Permanent silencing |
| 5 (slowest) | Germline methylation | Transgenerational | Intergenerational memory |

### 9.2 Cancer as pathological epigenetic memory

Cancer is, in OI language, a disease of the epigenetic hidden sector. The malignant transcriptional program is maintained by aberrant epigenetic memory — stable patterns of methylation and histone modifications that lock the cell into a proliferative program. Disrupting the memory *structure* (the stability of the hidden sector) is predicted to be more selective than disrupting the memory *content* (reactivating specific genes).

### 9.3 Aging as memory accumulation

The epigenetic clock (Horvath 2013) quantifies progressive accumulation of methylation marks associated with declining function. In OI language, aging is memory accumulation in the slowest epigenetic layers beyond the cell's ability to maintain homeostasis. Partial reprogramming (transient Yamanaka factor expression) erases recent epigenetic memory while preserving deeper developmental identity — conditional on those marks eroding on their retention time $\tau_B$, the framework predicts that the pulse durations that erase aging-associated marks are of the order of that $\tau_B$; whether deeper identity then changes gradually or sharply depends on the identity network's mixing, coupling and readback, and is model-dependent unless a specific mechanism establishes it.

### 9.4 The substratum-emergent operator distinction at chromatin

The companion paper's treatment of the Standard Model identifies a *substratum-emergent operator distinction* [SM §8.7]: operators that look identical at the emergent level can have distinct conservation properties depending on whether they act at the substratum (substrate) level or at the emergent (coarse-grained, observable) level. The canonical example: baryon number is exactly conserved at the OI substratum level (a property of the bilinear, block-diagonal lattice dynamics) but is violated at the emergent level through sphaleron processes that have no substratum analog.

Chromatin provides a proposed biological analogy to the operator distinction. The measurable molecular marks and the downstream expression readouts can vary separately in particular systems.

- **Substratum-level memory operator**: the molecular pattern of DNA methylation, histone modifications, and chromatin-state assignments. This is a directly measurable molecular substrate.
- **Emergent-level memory operator**: the gene expression program, the transcriptional phenotype, the cellular function readout. This is what cells display and what clinical phenotypes measure.

Cellular regulation relates the marks to downstream expression and function. The framework uses this relation as a coarse-graining analogy whose molecular inputs depend on the system.

Three empirical examples motivate the analogy.

(i) *iPSC reprogramming residuals* (Lin et al. 2024). Some studied protocols retain source-cell epigenetic features despite a change in cell identity. Buckberry et al. [26] report different resetting with a different reprogramming protocol. Residual memory is protocol-dependent.

(ii) *Bivalent chromatin states* (Bernstein et al. 2006). Marks associated with active and repressed transcription, H3K4me3 and H3K27me3, can coexist at lineage-control genes with low or poised expression. The measured state does not imply exact cancellation or an operator conservation law.

(iii) *Multi-timescale chromatin dynamics* (Stasevich et al. 2014; Saxton et al. 2023). Single-molecule and single-cell measurements directly observe distinct dynamics on subsecond and minutes timescales for the same histone modifications on the same nucleosomes. Histone acetylation modulates transcriptional burst frequency rather than burst size (Nicolas-Phillips et al. 2018), a stochastic-emergent-output pattern consistent with the framework's prediction that emergent operators have specific functional relationships to substratum operators rather than being identical to them.

These studies motivate separating persistent molecular marks from measured expression. The correspondence with the formal operators of [SM §8.7] remains an analogy.

### 9.5 Reader, writer, and eraser pharmacology as the operational substratum-emergent axis

Current epigenetic therapeutics are organized along three axes — drugs targeting **writers** (DNA methyltransferase inhibitors like 5-azacytidine, decitabine), **erasers** (histone deacetylase inhibitors like vorinostat, romidepsin), and **readers** (BET bromodomain inhibitors like JQ1, ZEN-3694, BI 894999). This three-axis organization is the substratum-emergent operator distinction made operational at the drug-development level: the substratum-level memory operator at chromatin is constructed and maintained by readers, writers, and erasers as the molecular machinery, and pharmacology can target any of these three functional roles independently.

This three-axis organization follows structurally from the operator distinction: any therapeutic approach to a substratum-emergent operator pair must target the substratum maintenance machinery (writers and erasers, which establish and remove substrate marks) or the substratum-to-emergent translation machinery (readers, which couple substrate state to downstream function). The three axes correspond to the three distinct functional roles in maintaining a substratum-emergent operator pair.

**Combination and scheduling hypothesis.** The proposal is to compare agents acting on different chromatin functions and test whether memory timescales predict their interactions. The existing evidence has several scopes:

- *Writer + reader.* The cited NUT carcinoma studies report preclinical evidence for combined targeting of p300/CBP and BET.
- *Eraser + reader* combination (HDAC inhibitor + BET inhibitor) is under clinical investigation in NUT carcinoma and other contexts.
- *Writer + eraser.* DNMT and HDAC inhibitor combinations have shown preclinical synergy. The E1905 trial [27] compared azacitidine with and without entinostat in MDS/AML. The study did not measure a memory-matched optimum.

The link from a measured mark relaxation time to a combination schedule remains a hypothesis. Comparing schedules requires matched exposure and appropriate response endpoints.

A proposed test is whether a measured $\tau_B$ predicts the response to intervals between agents targeting different chromatin functions.

---

## 10. Genetic Disorders: Non-Markovian Treatment Management

### 10.1 The boundary of the framework

Pure loss-of-function genetic disorders — hemophilia (absent Factor VIII/IX), cystic fibrosis (absent/misfolded CFTR), PKU (deficient phenylalanine hydroxylase), Tay-Sachs (absent hexosaminidase A) — are not memory diseases. The core problem is that a protein is missing or non-functional. There is no $\tau_B$ to normalize when the protein does not exist. The framework does not claim otherwise.

However, the *management* of genetic disorders — replacement therapy scheduling, immune responses to replacement proteins, gene therapy durability, and compensatory pathway dynamics — involves non-Markovian dynamics at every level. The framework's contribution is to these surrounding problems.

### 10.2 Coagulation cascade memory and factor replacement

The intrinsic and extrinsic clotting pathways converge at Factor X activation, followed by thrombin and fibrin formation. Thrombin activates Factor V and Factor VIII, while antithrombin and TFPI provide negative feedback. These interactions motivate a test of whether prior subthreshold activation changes the subsequent response at the same measured present.

For patients receiving replacement factor, recent bleeding or subthreshold activation could contribute to how the cascade responds. A history-dependent effect on dosing requires evidence that differences in activation history predict later response after matching the defined present, including factor level.

**Prediction.** The proposed benefit is a lower breakthrough bleeding rate for scheduling that accounts for activation history compared with pharmacokinetic-based scheduling at equivalent total factor consumption. An association with time since prior activation would motivate a matched-present test.

### 10.3 Inhibitor development as immune memory

Approximately 30% of severe hemophilia A patients develop inhibitory antibodies against replacement Factor VIII — the most serious complication in hemophilia management. This is squarely within the framework's territory. The immune system's response to repeated Factor VIII exposure is non-Markovian: each infusion writes information into the B cell and T cell memory compartments through the same TCR/BCR signaling cascades described in §6.

Inhibitor development is not random — it depends on the patient's exposure history, the timing and intensity of prior infusions, and concurrent immune status. The same architecture applies to immune reactions against enzyme replacement therapy in lysosomal storage diseases (Gaucher, Fabry, Pompe) and against gene therapy vectors (anti-AAV antibodies).

**Prediction:** Inhibitor risk correlates with the *schedule* of factor exposure (which determines immune memory state), not just cumulative dose. Specifically, initial exposure regimens with intervals tuned to the $\tau_B$ of the relevant B cell memory compartment should show lower inhibitor rates than standard intensive prophylaxis schedules. *Test:* Compare inhibitor development rates in patients started on different prophylaxis schedules (daily low-dose vs. twice-weekly standard-dose) at equivalent cumulative factor exposure over the first year.

Immune tolerance induction (ITI) — frequent high-dose factor infusion to overcome inhibitors — works by overwriting pathological immune memory. The framework predicts that ITI success depends on matching the infusion schedule to $\tau_B$ of the relevant B cell memory compartment, and that optimized ITI schedules calculated from measured B cell memory kinetics would show higher success rates.

### 10.4 Gene therapy durability as epigenetic memory

Hemgenix and Roctavian use AAV vectors to deliver functional Factor IX and VIII transgenes respectively. The vector DNA is predominantly episomal [28, 29]. Expression durability for these products cannot be assigned generally to host integration-site chromatin.

In a model where integrated copies measurably contribute to expression, chromatin at those loci could affect their expression and durability.

**Prediction:** Where integrated transgenes measurably contribute to expression, test whether their expression persists differently across loci with distinct chromatin dynamics. The test requires separating integrated and episomal contributions and measuring chromatin at the integrated loci.

### 10.5 Compensatory pathway memory

In many genetic disorders, compensatory pathways develop over time and partially mask the deficiency. In spinal muscular atrophy (SMA), for example, SMN2 partially compensates for lost SMN1 — but the degree of compensation is variable and depends on the patient's developmental history. In sickle cell disease, fetal hemoglobin (HbF) reactivation provides partial compensation, with levels influenced by the patient's prior erythropoietic history and epigenetic state.

These compensatory responses are non-Markovian: their current strength depends on the cumulative history of demands placed on them, stored in the epigenetic and signaling memory of the relevant cell populations. The framework predicts that interventions to boost compensatory pathways (HbF inducers in sickle cell, SMN2 upregulators in SMA) would be more effective if timed to the memory state of the compensatory system — analogous to the memory-priming strategy in cancer pharmacology (§3.3).

### 10.6 The general principle

For genetic disorders, the framework's contribution is not to the genetic defect itself but to three categories of treatment challenge:

| Treatment challenge | C1–C4 system | OI prediction |
|---|---|---|
| Replacement therapy scheduling | Coagulation cascade / metabolic pathway | Timing relative to cascade memory state improves efficacy |
| Immune reactions to therapy | TCR/BCR signaling cascades | Inhibitor risk depends on exposure *schedule*, not just dose |
| Gene therapy durability | Chromatin at expressed integrated copies | Test an integration-site effect where those copies contribute to expression |
| Compensatory pathway optimization | Epigenetic regulation of backup genes | Compensation strength depends on developmental history |
| Enzyme replacement therapy tolerance | B cell memory compartment | Tolerance induction schedule matches immune $\tau_B$ |

The summary: genetic disorders are not memory diseases. But the treatments for genetic disorders operate through biological systems that are memory systems. Optimizing these treatments for the non-Markovian dynamics of the underlying biology is a distinct and testable therapeutic strategy.

### 10.7 Reader-writer disorders as substratum-emergent operator disruption

A specific class of genetic disorders falls within the framework's scope of memory diseases rather than the §10.1 surrounding-treatment category. These are disorders caused by loss-of-function mutations in the *readers, writers, or erasers* of epigenetic memory rather than disorders of the substrate itself. In framework language, these are disorders of the substratum-to-emergent translation machinery, not disorders of the substratum.

**Rett syndrome as a case.** MECP2 encodes a methyl-CpG-binding protein, with loss-of-function variants a cause of Rett syndrome. The distinction between chromatin marks and the protein's functions motivates a proposed mechanism. The overall methylation landscape and its role in rescue are separate empirical questions.

Guy et al. [19] reactivated endogenous Mecp2 in a mouse model and observed reversal of neurological signs including in symptomatic adults, with recovery of hippocampal long-term potentiation. The result supplies prior evidence for reversibility in that model. A wider post-onset window than for other mechanisms needs a comparison of timing, dose and outcomes.

**Other disorders.** Effects of restoration must be tested separately for each affected function and developmental context.

- *Fragile X syndrome.* FMR1 loss affects an RNA-binding protein. The consequences of restoring that function depend on the model, age and outcomes.
- *Angelman syndrome* (UBE3A ubiquitin ligase loss, a writer of degradation marks): paternal allele substrate is preserved; loss is in the writer of one parental imprint. UBE3A reactivation via antisense oligonucleotides is in clinical investigation.
- *Kabuki syndrome.* KMT2D is an H3K4 methyltransferase. KDM6A removes H3K27 methylation [30]. Model evidence of phenotypic plasticity motivates disorder-specific tests.
- *ATR-X syndrome.* ATRX is a chromatin remodeler. Retained marks, residual function and effects of restoration are empirical questions.

**Therapeutic hypothesis.** Test whether targeted restoration of a disrupted function produces benefit at later treatment ages than a specified comparison, at measured levels of restored activity. MECP2 restoration is the example above. Trofinetide is an approved Rett treatment whose mechanism of therapeutic effect is unknown [20].

The effect of restoring particular chromatin functions and any broader therapeutic-window pattern remain open across disorders.

---

## 11. Distinguishing Predictions

Alternative models of use-dependence, hysteresis, priming and chronotherapy provide comparators for these proposals. Classical dynamic-disorder models can reproduce positive event autocorrelation and stretched-exponential waiting times. A grade-ii memory test requires a matched-present contrast, and grade-iii P-indivisibility requires a separate map-family witness (§2). The quantitative proposals use independently measured quantities. Prediction 8b tests whether molecular relaxation predicts the pulse-timing dependence of a prespecified focused-ultrasound response. Other proposals concern $\tau_B$-matched dosing (Prediction 9), methylation entropy at controlled mean level (Prediction 16) and decoupling of specified effects (Predictions 7 and 12).

### 11.1 Cancer

**Prediction 1:** In a specified Chk1 inhibitor system, compare resistance-associated changes in slow conformational modes with changes in catalytic parameters. The proposed regulatory mechanism could show larger changes in $\tau_B$ than in $k_{\text{cat}}$ or $K_m$.

**Prediction 2:** Test whether checkpoint recovery at the same measured present depends on prior damage history. Correlations across successive damage events can guide the choice of timescale. They need not distinguish a retained mode from a model with a richer current state.

**Prediction 3:** Compare sensitization after prior damage-and-recovery cycles with matched present measures of damage, cell-cycle state and exposure. The proposed direction is greater sensitization after priming. The mechanism requires additional controls.

**Prediction 4:** Test whether a chromatin-targeted intervention between radiation fractions changes the adaptive response and whether the change tracks measured chromatin state. A timing effect could have other mediators.

**Prediction 5:** Test a stretched-exponential model $P(t)\sim\exp(-(t/\tau)^\beta)$ for single-molecule Chk1 turnover. The form is a model hypothesis. Distinguishing retained history from a mixture of rates requires the separate conditional test.

### 11.2 Neurodegeneration

**Prediction 6:** A$\beta$ oligomers shift CaMKII's regulatory domain $\tau_B$, measurable by FRET or HDX-MS. *Test:* Compare CaMKII conformational dynamics in A$\beta$-exposed vs. control neurons.

**Prediction 7:** Reversing the $\tau_B$ shift rescues LTP independently of A$\beta$ clearance. *Test:* Treat A$\beta$-exposed neurons with a CaMKII conformational modulator; measure LTP induction.

**Prediction 8:** Normal aging shows gradual increase in CaMKII $\tau_B$, correlating with synaptic rigidity. *Test:* Measure CaMKII regulatory domain dynamics as a function of age in animal models.

**Prediction 8a:** Test whether a specified reconsolidation intervention has different effects on emotional, cognitive and sensory memory readouts. The cited propranolol trials give mixed clinical evidence. The layer-specific mechanism is proposed.

**Prediction 8b:** Test whether a measured molecular relaxation time predicts the pulse-timing dependence of a prespecified focused-ultrasound response in a controlled model.

**Prediction 8c:** Test in a controlled comparison whether focused ultrasound changes CaMKII conformational dynamics and whether that change predicts an independently measured cognitive outcome. Ye et al. [25] motivates the setting without measuring the proposed mediator.

### 11.3 Antibiotic resistance

**Prediction 9:** Pulsed antibiotic dosing with interval $\approx \tau_B$ of RecA filament dynamics outperforms continuous dosing and pulsing at intervals $\ll \tau_B$ or $\gg \tau_B$. *Test:* Measure persister fraction under different pulsing intervals.

**Prediction 10:** RecA filament length/conformation at the time of the second antibiotic pulse predicts survival probability. *Test:* Single-cell imaging of RecA-GFP filaments during pulsed antibiotic treatment.

### 11.4 Immunotherapy

**Prediction 11:** Temporal correlations between successive calcium flux events in repeatedly stimulated T cells are positive and decay on $\tau_B$ of TCR signaling kinases. *Test:* Time-lapse calcium imaging under repeated anti-CD3 stimulation.

**Prediction 12:** A kinase regulatory domain "accelerator" (increasing Lck SH2 flexibility) delays functional exhaustion markers (PD-1, Tim-3, LAG-3) in ex vivo exhaustion assays.

### 11.5 Cardiac pharmacology

**Prediction 13:** Antiarrhythmic drug efficacy at fixed plasma concentration differs between patients with persistent vs. intermittent tachycardia, beyond what Markovian models predict. *Test:* Correlate drug efficacy with heart rate pattern history, not just current rate.

### 11.6 Autoimmune disease

**Prediction 14:** Partial JAK inhibition reverses chronic cytokine-induced gene expression changes more effectively than proportional reduction in acute STAT phosphorylation. *Test:* Compare chronic vs. acute transcriptional effects of partial vs. full JAK inhibition.

### 11.7 Epigenetics

**Prediction 15:** Gene expression autocorrelation across cell divisions correlates with $\tau_B$ of the dominant epigenetic mark: methylation-regulated genes show stronger memory than histone-regulated genes.

**Prediction 16:** DNMT inhibitor efficacy correlates with methylation entropy (memory stability), not methylation level.

**Prediction 17:** Pulsed DNMT inhibitor administration achieves equivalent tumor response at lower toxicity than continuous administration (by allowing normal tissue memory to recover between pulses).

**Prediction 18:** During iPSC reprogramming, epigenetic marks are erased in order of increasing $\tau_B$: acetylation first, then methylation, then DNA methylation.

**Prediction 19:** Partial reprogramming (Yamanaka factor pulse): conditional on the marks eroding on their retention times, methylation age decreases with pulse length on the timescale $\tau_B$ of aging-associated marks, while cell-type identity is preserved for pulses short compared with the $\tau_B$ of developmental memory; whether identity is then lost gradually or sharply depends on the identity network's mixing, coupling and readback, and is model-dependent unless a specific mechanism establishes it.

### 11.8 Allosteric pharmacology

**Prediction 20:** RGS4 allosteric inhibitor selectivity across RGS family members correlates with B-site conformational dynamics ($\tau_B$), not sequence identity. *Test:* Plot IC$_{50}$ against B-site flexibility (from MD simulation) vs. sequence identity.

**Prediction 21:** Different active-site inhibitors of the same kinase produce different effects on distant regulatory domains because each writes different conformational information into the memory structure.

### 11.9 Drug resistance

**Prediction 22:** Resistance mutations far from the active site work by altering the *memory capacity* (C3) or *memory timescale* (C2) of the enzyme, not by blocking catalysis. *Test:* Normal mode analysis of resistance mutants — OI predicts changes in slowest modes, not catalytic modes.

**Prediction 23:** Drug selectivity among family members (RGS, BTK, Abl) correlates with conformational dynamics, not binding-site sequence. Existing data on BTK inhibitor-specific regulatory effects (Joseph et al. 2020) and RGS4 selectivity (Blazer et al. 2010) already support this prediction.

### 11.10 Genetic disorder treatment

**Prediction 24:** In hemophilia patients on prophylaxis, breakthrough bleeding frequency correlates with the interval between the most recent cascade activation event and the next prophylactic dose — not just trough factor level. *Test:* Track bleed timing relative to prior subthreshold activations via thrombin generation assays.

**Prediction 25:** Inhibitor development rates in hemophilia A correlate with the *schedule* of initial Factor VIII exposure (which determines immune memory state), not just cumulative dose. *Test:* Compare inhibitor rates between daily low-dose vs. twice-weekly standard-dose prophylaxis at equivalent cumulative factor exposure.

**Prediction 26:** Where integrated transgene copies measurably contribute to expression, test whether their durability covaries with the chromatin dynamics at the integration sites after separating any episomal expression.

---

## 12. Existing Evidence

The following published results motivate specific tests. Their designs and measured endpoints determine what they establish.

**Resistance through dynamics, not catalysis (Prediction 22).** Taldaev et al. (PNAS, 2021) identified an Abl kinase imatinib-resistance mutation that preserves drug binding affinity but increases conformational dynamics — altering $\tau_B$, not $K_d$. The BTK T316A mutation (Joseph et al., eLife, 2020) causes resistance by shifting the conformational ensemble, not by blocking drug binding. Deep mutational scanning of Src (Chakraborty et al. 2024) found that 25–45% of resistance mutations for each inhibitor were unique to that inhibitor's conformational binding mode.

**Selectivity through dynamics, not sequence (Prediction 23).** RGS4 allosteric inhibitor selectivity does not correlate with B-site sequence conservation (Blazer et al. 2010). Five different BTK active-site inhibitors produce five qualitatively different effects on distant regulatory domains of the *same* protein (Joseph et al. 2020).

**Checkpoint responses (Prediction 2).** Chao et al. [15] reported phase-dependent checkpoint responses. Current cell-cycle state can account for some differences. A comparison at fixed present is needed to test the proposed Chk1 mechanism.

**Nonexponential enzyme kinetics (Prediction 5).** The cited enzyme assays [7, 14] motivate testing comparable kinetics for Chk1. Waiting-time fits do not independently establish accessible conditional memory.

---

## 13. Discussion

### 13.1 The unifying principle

Each application proposes a slow record, a readout and a possible asymmetry between disease and comparison states. Whether the record persists, influences matched-present response and can be targeted needs evidence for each case.

| Disease | Memory mechanism | Current target | OI target |
|---|---|---|---|
| Cancer (Chk1) | Checkpoint PTM accumulation | Kinase catalysis | Regulatory domain $\tau_B$ |
| Alzheimer's | CaMKII $\tau_B$ shift by A$\beta$ | Protein aggregates | $\tau_B$ normalization |
| Parkinson's | LRRK2 $\tau_B$ shift by $\alpha$-syn | Protein aggregates | $\tau_B$ normalization |
| Antibiotic resistance | SOS/RecA filament memory | Bacterial growth | RecA memory timescale |
| T cell exhaustion | TCR kinase PTM accumulation | PD-1 brake | TCR kinase $\tau_B$ |
| Cardiac arrhythmia | Ion channel slow inactivation | Channel block | Heart-rate-adapted dosing |
| Autoimmune disease | JAK-STAT memory | JAK catalysis | JH2 conformational relaxation |
| Cancer (epigenetic) | Aberrant methylation/histone marks | Gene reactivation | Memory stability ($\tau_B$) |
| Aging | Epigenetic clock accumulation | Symptom management | $\tau_B$-selective erasure |
| Hemophilia (treatment) | Coagulation cascade memory | PK-based factor dosing | Cascade memory-state dosing |
| Genetic disorders (immune) | B/T cell memory from replacement therapy | Dose reduction | Exposure schedule matching immune $\tau_B$ |
| Gene therapy durability | Candidate chromatin effect where integrated copies are expressed | Measure integrated and episomal contributions | Test whether the local chromatin state predicts durability |

### 13.2 Implications for drug discovery

The framework identifies a new class of drug targets — conformational memory timescale — that current screening assays do not measure. A "memory-targeted" drug screen would assay temporal correlations in enzyme activity, not steady-state kinetic parameters. This requires single-molecule or single-cell time-series measurements, which are technically mature but not routinely used in drug discovery.

### 13.3 Implications for clinical trial design

Two predictions are immediately testable with existing drugs and standard clinical infrastructure: (1) memory-selective scheduling of gemcitabine + Chk1 inhibitor (modified dosing protocol, no new drugs); (2) inter-fraction HDAC inhibitor for radiation adaptive response erasure (standard radiation biology experiment). Both could be evaluated in Phase I/II settings with minimal additional cost.

### 13.4 Connection to fundamental physics

The finite-horizon result supplies a conditional diagnostic for defined observables. Its implications apply if the molecular law satisfies the premises. The candidate regulatory records, treatment responses and mechanism attributions require independent empirical tests.

The chromatin examples motivate an analogy between molecular marks and downstream function. The studies compare measured quantities without establishing the formal operator correspondence of [SM §8.7].

A timescale separation can allow persistence of a molecular record. Its magnitude, the loss of records and their accessibility to later readout depend on the particular system.

The same structural picture applied to computational analysis methods is developed in the companion Bioinformatics paper [18], which addresses non-Markovian dynamics in single-cell trajectory inference, gene regulatory network inference, perturbation prediction, multi-omics integration, and cancer methylome classification. The framework's reader-writer disorder class (§10.7) extends into specific bioinformatic patterns there.

---

## Acknowledgements

AI assistance in preparing this work is disclosed at\
<https://github.com/amaybaum/incompleteness#ai-assistance>.

---

## References

[1] A. Maybaum, "The Incompleteness of Observation," (2026).


[2] J. Gunawardena, "A linear framework for time-scale separation in nonlinear biochemical systems," *PLoS ONE* **7**, e36321 (2012).

[3] K. K. Bhatt et al., "Essential function of Chk1 can be uncoupled from DNA damage checkpoint and replication control," *PNAS* **105**, 20752 (2008).

[4] L. A. Parsels et al., "Gemcitabine sensitization by Chk1 inhibition correlates with inhibition of a Rad51 DNA damage response in pancreatic cancer cells," *Mol. Cancer Ther.* **8**, 45 (2009).

[5] L. L. Blazer et al., "Reversible, allosteric small-molecule inhibitors of regulator of G protein signaling proteins," *Mol. Pharmacol.* **78**, 524 (2010).

[6] B. P. English et al., "Ever-fluctuating single enzyme molecules: Michaelis-Menten equation revisited," *Nature Chemical Biology* **2**, 87 (2006).

[7] L. Edman and R. Rigler, "Memory landscapes of single-enzyme molecules," *PNAS* **97**, 8266 (2000).

[8] R. E. Joseph et al., "Allosteric communication in BTK," *eLife* **9**, e60470 (2020).

[9] A. Taldaev et al., "A kinetic view of imatinib resistance in chronic myeloid leukemia," *PNAS* **118**, e2106566118 (2021).

[10] S. Horvath, "DNA methylation age of human tissues and cell types," *Genome Biol.* **14**, R115 (2013).

[11] Y. Lu et al., "Reprogramming to recover youthful epigenetic information and restore vision," *Nature* **588**, 124 (2020).

[12] H. X. Chao et al., "Evidence that the human cell cycle is a series of uncoupled, memoryless phases," *Mol. Syst. Biol.* **15**, e8604 (2019).

[13] K. K. Bhatt et al., "Chk1-S is a splice variant and endogenous inhibitor of Chk1," *PNAS* **109**, 197 (2012).

[14] H. P. Lu, L. Xun, X. S. Xie, "Single-molecule enzymatic dynamics," *Science* **282**, 1877 (1998).

[15] H. X. Chao, C. E. Poovey, A. A. Privette, G. D. Grant, H. Y. Chao, J. G. Cook, J. E. Purvis, "Orchestration of DNA damage checkpoint dynamics across the human cell cycle," *Cell Systems* **5**, 445 (2017).

[16] S. Chakraborty, E. Ahler, J. J. Simon, L. Fang, Z. E. Potter, K. A. Sitko, J. J. Stephany, M. Guttman, D. M. Fowler, D. J. Maly, "Profiling of drug resistance in Src kinase at scale uncovers a regulatory network coupling autoinhibition and catalytic domain dynamics," *Cell Chemical Biology* **31**, 207 (2024).

[17] D. Wilsker, E. Petermann, T. Helleday, F. Bunz, "Essential function of Chk1 can be uncoupled from DNA damage checkpoint and replication control," *PNAS* **105**, 20752 (2008).

[18] A. Maybaum, "Non-Markovian Dynamics in Computational Biology," companion paper (2026).

[19] J. Guy et al., “Reversal of neurological defects in a mouse model of Rett syndrome,” *Science* **315**, 1143–1147 (2007). doi:10.1126/science.1138389.

[20] U.S. prescribing information for trofinetide, [§12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=67e6f2d9-21f6-466f-9def-826c6a4b8257).

[21] A. Brunet et al., randomized trial of propranolol with trauma reactivation (2018), [PubMed 29325446](https://pubmed.ncbi.nlm.nih.gov/29325446/).

[22] P. Roullet et al., randomized trial of trauma reactivation with or without propranolol (2021), [PubMed 33612830](https://pubmed.ncbi.nlm.nih.gov/33612830/).

[23] C. H. van Dyck et al., “Lecanemab in early Alzheimer's disease,” [PubMed 36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/).

[24] J. R. Sims et al., randomized trial of donanemab in early symptomatic Alzheimer disease (2023), [PubMed 37459141](https://pubmed.ncbi.nlm.nih.gov/37459141/).

[25] Ye et al., focused ultrasound blood–brain barrier opening in Alzheimer's disease, [PubMed 39793012](https://pubmed.ncbi.nlm.nih.gov/39793012/).

[26] S. Buckberry et al., “Transient naive reprogramming corrects hiPSC epigenetic memory,” [*Nature* (2023)](https://www.nature.com/articles/s41586-023-06424-7).

[27] T. Prébet et al., US Leukemia Intergroup trial E1905, [PubMed 24663049](https://pubmed.ncbi.nlm.nih.gov/24663049/).

[28] European Medicines Agency, [Hemgenix risk-management plan](https://www.ema.europa.eu/en/documents/rmp/hemgenix-epar-risk-management-plan_en.pdf).

[29] U.S. Food and Drug Administration, [Roctavian prescribing information](https://www.fda.gov/media/169937/download).

[30] M. Adam et al., “Kabuki syndrome,” [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK62111/).

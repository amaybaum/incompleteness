# Non-Markovian Dynamics in Computational Biology
### Hidden-Sector Memory and the Methodological Limits of Single-Cell Analysis

**Author:** Alex Maybaum
**Date:** May 2026
**Classification:** Computational Biology / Bioinformatics

---

## Abstract

Single-cell bioinformatics benchmarks report setting-specific limitations in RNA velocity, gene regulatory network inference and perturbation prediction. Multi-modal studies and methylation-based tumor classifiers provide distinct empirical comparisons.

We apply the finite-horizon readback diagnostic to candidate cellular observables. A history effect at a fixed measured present gives accessible conditional memory. Coupling, persistence and capacity motivate possible record carriers. The cellular mechanisms and relevant observables require further evidence.

The applications cover trajectory inference, regulatory networks, perturbation prediction, multi-omics integration and methylation-based classification. The benchmarks specify their data, tasks and baselines. For instance, Heidelberg v12.8 achieved 95% subclass accuracy in nested cross-validation on its reference data. The mechanism and transfer to other assays or cohorts are separate questions.

The information constraint is conditional on the target and data. A target that differs between two completions sharing the law of the available observations cannot be uniquely identified from that law. We discuss where this condition could apply and how new measurements could make an otherwise unresolved target distinguishable.

---

> **Status — conditional information result and conjectural applications.** The benchmarks below are prior observations. Which cellular targets differ across completions, which extra measurements resolve them and which underlying mechanisms account for the comparisons remain separate empirical questions.

## 1. Introduction

### 1.1 The bioinformatics field's persistent puzzles

Single-cell transcriptomics has revolutionized biology over the past decade, producing datasets of millions of cells with detailed gene expression profiles. The computational methodology has evolved rapidly: dimensionality reduction (UMAP, t-SNE), clustering (Leiden, Louvain), trajectory inference (Monocle, Slingshot, scVelo), gene regulatory network inference (SCENIC, GENIE3), perturbation modeling (CPA, GEARS, scGPT), and multi-omics integration (MOFA, Seurat, LIGER). Each new method generation has promised improved accuracy and broader applicability, and the field's expected trajectory has been continuous improvement.

A different pattern has emerged. Recent benchmarking studies have documented systematic failures across multiple method classes:

- **RNA velocity.** Gorin et al. [3] report failures including trajectory reversal on particular datasets.

- **Gene regulatory network inference.** Published GRN evaluations report limited prediction accuracy or performance close to correlation baselines in some settings [4, 5].

- **Deep-learning models.** A perturbation-prediction benchmark found no consistent improvement of its deep-learning methods over the simple baselines [6]. A different zero-shot study [7] evaluated cell clustering and other tasks.

- **Multi-omics integration** methods (MOFA, MOFA+) treat different molecular modalities as parallel measurements of the same cell state, despite the fact that "the timescale of (phospho)proteome changes falls into a minute regime, whereas most significant transcriptome changes are observed after hours" [8].

Each puzzle has been addressed within the field as a methodological problem to be solved with better algorithms. The proposed solutions follow a common pattern: incorporate additional data modalities (chromatin accessibility, ATAC-seq, methylation), incorporate prior knowledge (knowledge graphs, motif libraries), or move to more complex architectures (transformers, foundation models, graph neural networks). Some of these solutions help; others do not. The field lacks a structural framework for predicting *which* methodological improvements will help and *why*.

### 1.2 The OI framework and its C1–C4 conditions

The finite-horizon readback lemma gives conditional memory when histories ending at the same present state induce different next-step laws. The potential contributions of coupling, persistence and capacity can be assessed for the declared partition. Those features alone allow zero accessible memory.

The Medicine paper [2] considers chromatin, histone modifications and other slow variables as candidate biological record carriers. Whether measured gene expression reads back a particular retained record is a separate test.

An identification limit arises where a particular cellular target differs between completions sharing the entire law of the transcriptome observations available to the method. Whether that condition holds depends on the target, assay and interventions.

### 1.3 Thesis and structure

This paper applies a conditional identification bound to targets in five domains of single-cell bioinformatics. Each application specifies the target and available observations, considers possible identification gaps and discusses the reported task-specific comparisons.

§2 discusses RNA and multi-omic trajectory inference. §3 considers benchmarks for gene regulatory network inference. §4 compares perturbation predictors on the cited tasks. §5 discusses differences in response times across modalities. §6 reports a cancer methylome classification example. §7 proposes variant-pathogenicity comparisons for reader, writer and eraser genes. §8 considers bioinformatic readouts for the disorders discussed in [Medicine §10.7]. §9 synthesizes the cross-domain findings. §10 catalogs open questions and limits.

The bound applies when candidate completions agree on the available observation law and disagree on the target. Whether this explains a benchmark result requires additional evidence about the target, observations and competing explanations for the performance difference.

---

## 2. Trajectory Inference

### 2.1 The RNA velocity paradigm and its assumptions

RNA velocity, introduced by La Manno et al. (2018) [9] and operationalized in the velocyto and scVelo tools, infers the direction of cellular state change from the ratio of unspliced to spliced mRNA in single-cell RNA sequencing data. The method's appeal is that it extracts dynamic information from static snapshots: by measuring the relative abundance of pre-mRNA (unspliced, recently transcribed) and mature mRNA (spliced, accumulated), it estimates whether a gene is in an induction phase (more unspliced relative to expected steady state) or repression phase (more spliced relative to expected steady state). Aggregating across genes produces a velocity vector for each cell, which can be visualized as a flow field over the dimensionally-reduced state space.

RNA velocity estimates local changes using observed spliced and unspliced RNA under a kinetic model. The original velocyto framework and the scVelo dynamical extension use different assumptions about steady state and rates [9, 10]. Model adequacy depends on the tissue, sampling and kinetic regime.

### 2.2 Documented failure modes

Gorin et al. (2022) [3] discuss examples where RNA velocity methods fail to recover direction or reverse a known trajectory.

Heterogeneous kinetics and violations of a model's assumptions are possible explanations for errors [11]. The relevant kinetic and sampling conditions vary by experiment.

Flexible kinetic models and latent state models address some failures under their own assumptions. The results depend on the available data and benchmark.

### 2.3 The framework's structural explanation

Chromatin state is a candidate variable in a kinetic model for RNA trajectories. It can affect accessibility and transcription rates while remaining latent in an RNA-only assay.

To establish accessible readback, compare later transcriptome laws for histories with the same measured present. An association between chromatin state and RNA measurements can motivate this test.

The sign of a velocity error depends on the model, omitted variables and sampling design. A chromatin transition is one possible contributor.

The reported direction errors motivate testing whether adding chromatin measurements resolves specific cases. Benchmark comparisons alone do not isolate this cause.

### 2.4 Multi-omic velocity as empirical convergence

MultiVelo [17] adds chromatin accessibility to RNA velocity and reports results on the studied development and differentiation datasets.

mmVelo [18] considers single-peak representation, and MoFlow [19] develops a multimodal velocity method. Their evaluations cover particular data and tasks.

These studies motivate comparisons at matched targets and samples. Extra chromatin measurements can help if they provide task-relevant information unavailable in the RNA readout.

### 2.5 Practical consequences

The framework provides three practical predictions for trajectory inference methodology:

(P1) Test whether direction or fate is unidentifiable under the RNA-only observation design in a setting with independently characterized chromatin dynamics.

(P2) Compare paired RNA and chromatin data with RNA-only data at matched benchmark conditions. A gain is plausible if the added data resolve target differences left undetermined by RNA.

(P3) Test which measured modality adds predictive information on the timescale of the specified trajectory.

A controlled benchmark can compare modalities and estimator classes across prespecified trajectories.

---

## 3. Gene Regulatory Network Inference

### 3.1 The GRN inference paradigm and the "persistent puzzle"

Gene regulatory networks (GRNs) describe the directed influence of transcription factors on target genes. Inferring GRNs from single-cell expression data is a foundational task in computational biology, with applications ranging from drug-target identification to mechanistic understanding of differentiation programs. The methodology has produced a series of method generations: correlation-based methods (Pearson, mutual information), ensemble methods (GENIE3, GRNBoost2), expression-cell-type specific methods (SCENIC), causal methods (PC algorithm, NOTEARS, DeepSEM), and most recently deep-learning foundation models (scGPT, Geneformer) repurposed for GRN inference.

Existing comparisons report low GRN inference accuracy in some settings [20]. Fernandez-de-Retana et al. [5] compare causal and correlational GRN methods under controlled benchmark conditions.

Multiple comprehensive benchmarking studies have confirmed this pattern. McCalla et al. [21] evaluated 13 GRN inference methods on 7 published datasets using diverse gold standards; the methods rank similarly across gold standards, with no method showing decisive advantage. Nguyen et al. [22] benchmarked 15 methods on 139 simulated datasets and found extensive failure modes related to dropout rate and sparsity. The conclusion across the literature is consistent: GRN inference from single-cell data is hard, and current methods perform near baseline.

### 3.2 A conditional limit on causal recovery

Learning a causal graph from observations requires assumptions about variables, interventions or mechanisms. Different causal structures can represent the same observational distribution.

Chromatin state, protein concentrations and modifications are candidates for omitted variables. Which causal target differs between observationally equivalent completions remains open for each assay design.

Co-expression estimates association in the observed data. Whether that association is useful for the intended regulatory target depends on the target and reference standard.

RNA data may leave particular causal relationships unidentified. This does not order the predictive performance of specific correlation or causal methods.

### 3.3 Multi-modal methods as the predicted improvement

SCENIC+ [23] incorporates chromatin accessibility and motif information to infer candidate regulatory relationships. Its reported comparisons concern particular data and evaluation targets.

LINGER [24] uses external atlas-scale data and motif priors. The study reports its benchmark gains under those inputs and task definitions.

Additional observations or relevant priors could constrain the set of compatible regulatory mechanisms. The benchmark results leave the responsible information source and general performance ordering open.

### 3.4 Information-theoretic ceiling

Beyond a relative improvement from multi-modal data, the framework gives an information-theoretic ceiling. A visible law with accessible conditional memory carries that memory in a hidden sector (the hidden-memory theorem), and every faithful completion of the law shares one canonical predictive quotient while the hidden fibers above it may differ (the canonical-predictive-quotient theorem, with certified fiber freedom) [Main §3.4]. Hence, where the causal GRN differs between completions that share the scRNA-seq law, no method using only that law can recover it, regardless of model complexity or training data scale. Whether the causal structure of a given GRN lies in those fibers is open.

scGPT [25] and Geneformer [26] offer ways to model transcriptome associations. Kendiukhov [27] examines their attention patterns, co-expression and prediction on the specified datasets and tasks. These comparisons do not establish which causal relationships are identifiable from the inputs.

Where the GRN differs across completions sharing the same available law, scaling an RNA-only estimator cannot identify the differing part. Evidence that the condition holds for a given target requires specifying the observations and ruling out identification under those data.

### 3.5 Practical consequences

Three framework-grounded predictions for GRN inference methodology:

(P4) Test which regulatory targets vary among completions of the same RNA law. The bound alone does not locate existing estimators relative to the best achievable risk.

(P5) Additional measurements can help where they resolve differences in the specific regulatory target. Compare modalities and baselines at fixed evaluation design.

(P6) The same identification bound applies to models using the same RNA observation law at any scale. Paired modalities can aid recovery if they distinguish previously equivalent completions.

The third prediction is testable in the near term as multi-modal foundation models become available.

---

## 4. Perturbation Prediction

### 4.1 The perturbation prediction paradigm

Single-cell perturbation experiments — CRISPR knockouts (Perturb-seq, CROP-seq), CRISPRa/i activation/repression (Replogle et al. 2022 [28]), drug treatments (sci-Plex), and combinatorial perturbations (Norman et al. 2019 [29]) — produce datasets where individual cells are labeled by the perturbation they received and the resulting transcriptional state is measured. The computational task is to predict the transcriptional state for *unseen* perturbations: combinations of perturbations not in the training data, perturbations applied to new cell types, or perturbations with new drugs.

This task has attracted substantial methodological investment. Generative models (CPA [30], chemCPA [31]) learn compositional representations of perturbation effects. Graph neural networks (GEARS [32]) incorporate Gene Ontology and protein-protein interaction graphs as priors. Optimal transport methods (CellOT [33]) match unperturbed and perturbed distributions. Most recently, single-cell foundation models (scGPT [25], Geneformer [26], scFoundation [34], scPRINT) have been adapted for perturbation prediction tasks, with the expectation that pretraining on tens of millions of cells would enable strong zero-shot and few-shot performance.

### 4.2 The empirical failure of deep learning on perturbation prediction

Ahlmann-Eltze et al. [6] evaluated deep-learning methods, including a graph-based model [32], against mean and linear baselines on the reported perturbation tasks. The evaluated methods did not consistently outperform the simple baselines on those datasets and metrics.

The benchmark of Fernandez-de-Retana et al. [5] addresses GRN inference. Kedzierska et al. [7] evaluate separate zero-shot tasks, and Kendiukhov [27] examines attention and regulatory signals in specific foundation models.

These studies leave open how much of the benchmark outcome is attributable to measurement limits, training design, task definition or model fit.

### 4.3 The framework's structural prediction

Let T denote the information supplied to a predictor, including the training and intervention information it can use, and Y the defined target. The part of a perturbation response that differs across completions sharing the available observation law is unidentified under that design.

If $\widehat{Y}$ is produced from $T$ alone, with any extra randomness independent of $Y$ given $T$, data processing gives $I(Y;\widehat{Y})\le I(Y;T)$. For added observations $S$, the additional information is $I(Y;S\mid T)$. With finite discrete outcomes and log loss this equals the Bayes-risk reduction $H(Y\mid T)-H(Y\mid T,S)$. Its value depends on the design and the target.

For squared loss, the Bayes predictor from T is the conditional mean. The observable conditional law can also identify variance and quantiles of the target on its measured support. A training-set mean baseline and an optimal conditional predictor are distinct. A benchmark tie with the former does not establish that the methods approach the latter.

### 4.4 Knowledge-graph methods as the predicted improvement

GEARS [32] uses biological graphs as priors, while PerturbNet [35] uses its own data, training and evaluation setup. Their reported results concern the specific benchmarks. The study in [6] also evaluated the graph-based model.

A relevant graph can supply assumptions or additional evidence for a particular target. Performance relative to other methods remains a benchmark question.

### 4.5 Compositional generalization and what scaling cannot fix

Compositional generalization can be unidentifiable when single-perturbation data leave multiple possible joint responses. A specified response model or additional measurements may constrain those alternatives.

This is testable. Norman et al. (2019) [29] published a combinatorial perturbation dataset with 287 single-gene knockdowns and 131 pairs of knockdowns. The framework predicts that pairs where both genes act on the same chromatin domain (likely to interact through hidden-sector variables) should be harder to predict from single-gene training data than pairs where the genes act on disjoint pathways. The empirical pattern in compositional generalization benchmarks should track the chromatin co-localization of the perturbed genes, not just their expression patterns. This prediction has not been directly tested in the existing benchmarking literature.

### 4.6 Practical consequences

Four framework-grounded predictions for perturbation prediction methodology:

(P7) For an unidentified perturbation target, RNA-only methods share the identification limit under the declared observation law. Predictive risk for observed outcomes depends on the loss and on how well the estimator learns the observable conditional law.

(P8) Test whether additional chromatin information improves prediction of specified perturbation responses on paired data and matched baselines.

(P9) Compare relevant graph or motif priors with matched data-only methods. The effect depends on the utility of the prior for the declared task.

(P10) Compositional generalization (predicting double perturbations from single-perturbation training) will be systematically harder for perturbations co-localized at the chromatin level than for perturbations acting on disjoint pathways. This is testable through benchmarking on Norman et al.'s combinatorial dataset stratified by chromatin co-localization of the perturbed gene pairs.

The fourth prediction is a proposed comparison. A positive result would have to be distinguished from alternative explanations for the performance difference before attributing it to chromatin co-localization.

---

## 5. Multi-Omics Integration

### 5.1 The multi-omics integration paradigm

Single-cell multi-omics technologies measure multiple molecular modalities in the same cell: G&T-seq (genome + transcriptome), scNMT-seq (chromatin accessibility + transcriptome + methylation), CITE-seq (transcriptome + surface protein), QuRIE-seq (transcriptome + intracellular phosphoprotein), and increasingly multimodal Perturb-seq variants. The data architecture is: $N$ cells × $M$ modalities × $G_m$ features per modality, with the modalities measuring different aspects of cellular state on different timescales.

The standard computational task is integration: combining information across modalities to produce unified cell embeddings, joint trajectories, and integrated regulatory networks. The principal methods are Multi-Omics Factor Analysis (MOFA [36] and MOFA+ [37]), Seurat's weighted nearest neighbor (WNN) [38], LIGER [39], and totalVI [40]. These methods share a common assumption: different modalities are parallel measurements of the same underlying cell state, and integration combines them into a single low-dimensional latent space.

### 5.2 The timescale problem

The parallel-measurements assumption fails when modalities measure different memory layers operating on different timescales. The QuRIE-seq paper [8] explicitly states: "The timescale of (phospho)proteome changes falls into a minute regime, whereas most significant transcriptome changes are observed after hours." The same cells, measured at the same instant, contain information from different points in their dynamical history — phosphoprotein measurements reflect minute-scale signaling state, transcriptome measurements reflect hour-scale gene expression state, and methylation measurements reflect day-to-week-scale chromatin state.

The framework's perspective on this is direct: each modality measures a different memory layer with a different $\tau_B$. The visible-sector / hidden-sector partition is modality-dependent. From the perspective of phosphoprotein dynamics, the transcriptome state is part of the slow hidden sector (chromatin sets transcriptional rates, which set protein production rates). From the perspective of methylation dynamics, the transcriptome is part of the fast visible sector (transcription happens fast on the methylation timescale). The static factor-analysis assumption — that all modalities reflect the same cell state — misses this hierarchical structure.

The empirical consequences are documentable. Static integration methods produce embeddings that are dominated by the modality with the largest dynamic range during the measurement window — typically transcriptome — and the other modalities contribute mostly as confirmation of the transcriptome-derived structure rather than as independent information. The integration improves accuracy modestly compared to single-modality methods, but does not fully exploit the temporal information present in the multi-modal data.

### 5.3 Emerging timescale-aware methods

Recent methodological work has begun to address the timescale problem explicitly. The QuRIE-seq paper [8] used time-series sampling combined with MOFA+ factors to capture dynamics across modalities. Heyne et al. (2024) [41] introduced pseudotemporal integration of single-cell RNA-Seq and single-cell proteomics by mass spectrometry, building cell-state trajectories separately for each modality and aligning them through shared markers. The approach yields "time-dependent, nonlinear relationships between transcript and protein levels" that static methods cannot recover.

MultiVelo [17] models chromatin and transcription with distinct switch times and reports benchmark performance on its studied systems.

One hypothesis is that a model of finite lags improves inference where the lagged information is present in the data and relevant to the target. Estimating $\tau_B$ and the shape of the response requires a paired time-series design.

### 5.4 The hierarchy of biological memory layers

The following timescales illustrate possible differences across molecular modalities.

| Modality | Typical $\tau_B$ | Memory layer |
|---|---|---|
| Phosphoproteins | seconds–minutes | Signaling state |
| Metabolites | seconds–minutes | Metabolic state |
| Transcriptome | minutes–hours | Gene expression state |
| Histone acetylation | minutes–hours | Active chromatin state |
| Histone methylation | hours–days | Stable chromatin state |
| Proteome | hours–days | Translation state |
| Chromatin accessibility | hours–days | Regulatory element state |
| DNA methylation | days–weeks | Stable epigenetic state |
| Genome (sequence) | $\to \infty$ | Heritable state |
| Chromatin 3D architecture (Hi-C) | hours–generations | Genome organization |

Timescales and their ordering can depend on the process and tissue. A performance comparison requires estimating the relevant dynamics on the data in question.

### 5.5 Static factor analysis under the framework

MOFA and MOFA+ are widely used and produce useful cell embeddings. They do not, however, capture the temporal hierarchy across modalities. The framework's prediction is that MOFA-style methods extract the *static covariance structure* shared across modalities — what is common to all measurements of a cell at one instant — but miss the *dynamical relationships* between modalities — how chromatin state at one time predicts transcriptome state at a later time. The static covariance is informative but incomplete; the dynamical relationships contain additional information that static methods cannot access.

This is testable. A direct comparison of MOFA+ integration with a timescale-aware method on time-series data should show the timescale-aware method recovering dynamical relationships that MOFA misses. The QuRIE-seq paper [8] and subsequent time-series multi-omics studies provide the data substrate for such comparisons; the comparison has not been systematically performed across the methodological literature.

### 5.6 Practical consequences

Three framework-grounded predictions for multi-omics integration:

(P11) For time-indexed observations, compare static factor analysis with models of lagged dependence on the same data and prediction targets.

(P12) Test whether accounting for measured time lags improves dynamic predictions beyond matched baselines.

(P13) Compare modality combinations at time resolutions appropriate to the biological process and target.

Timing and modality comparisons can assess which additional measurements or lag models aid a given task.

---

## 6. Cancer Methylome Classification

### 6.1 The methylation-based tumor classification paradigm

Capper et al. [42] developed their CNS tumor methylation classifier on 2,801 reference samples and reported diagnostic changes in up to 12% of prospective cases. Sill et al. [43] report 95% subclass-level accuracy in nested cross-validation for Heidelberg v12.8, with 7,495 methylation profiles and 184 subclasses. This percentage concerns that reference validation design.

The classifier maps measured CpG methylation profiles to curated reference classes. Its clinical use and performance depend on reference coverage, assay quality and the population assessed.

### 6.2 Methylome arrest in cancer

Capper et al. [42] discuss the potential of cell-of-origin and tumor-associated features to inform classification. A stable signal for some classes does not establish an unchanged global methylome during disease.

The utility of methylation profiles for particular diagnoses motivates longitudinal or matched-assay comparisons of which features are retained.

### 6.3 The substratum-emergent operator distinction in cancer

One hypothesis is that some methylation features retain information about origins that is useful for a specified classification task. This can be assessed alongside tumor-associated changes.

The 95% result is an estimate for subclass classification within the v12.8 reference validation design. A comparison with other assays needs matched data and endpoints. Classification accuracy alone does not establish which molecular features were preserved.

The chromatin and expression distinction in [Medicine §9.4] motivates asking which assay is informative about which target in a specified system.

### 6.4 Unclassifiable tumors and substratum disruption

Drexler et al. [45] studied Heidelberg v11.4 and used calibrated score thresholds of 0.84 and 0.3 to define analysis groups. Tumor purity, reference coverage and other cohort features can affect classification.

A proposed contributor to low scores is altered methylation maintenance in some tumors. Other explanations include low purity, technical factors and classes absent from the reference.

A test of this hypothesis would compare prespecified maintenance-site patterns at matched tumor purity, coverage and other clinical covariates.

### 6.5 Methylation classification beyond CNS tumors

Methylation-based approaches have been evaluated in additional settings, including sarcomas [46] and pan-cancer studies [47]. Each reported performance result uses its own reference set, validation design and target.

An open prediction is whether changes in chromatin maintenance explain part of the variation in classification across tumors after controlling for reference coverage, tissue and purity.

### 6.6 Practical consequences

Three framework-grounded predictions for cancer methylome bioinformatics:

(P14) Test whether methylation features associated with specific classes remain informative on independent samples from other tumor settings.

(P15) Compare whether maintenance-site patterns explain some low scores after accounting for purity, reference coverage and other factors.

(P16) Test whether chromatin-maintenance covariates improve a specified methylation classifier in held-out validation.

The third prediction is testable through reanalysis of the existing Heidelberg cohort with maintenance machinery integrity as a stratification variable.

---

## 7. Variant Pathogenicity for Reader/Writer/Eraser Genes

### 7.1 Variant effect prediction methods

Predicting the functional impact of missense variants on protein-coding genes is a core task in clinical genetics. Methods range from sequence-conservation methods (SIFT [48], PolyPhen-2 [49]) through structure-aware methods (CADD [50], REVEL [51]) to AI-based methods (AlphaMissense [52]). AlphaMissense, introduced by Cheng et al. (Science 2023) [52], applies the AlphaFold2 architecture [53] to variant effect prediction and achieves state-of-the-art performance across multiple benchmarks, providing pathogenicity scores for every possible single-amino-acid substitution in the human proteome [54].

The methods operate on a common assumption: variant pathogenicity is determined by the variant's impact on the protein it directly affects. Conservation features capture evolutionary intolerance to variation at the residue; structural features capture the variant's disruption of folding or function; AI features capture the integration of structural and conservation information at a higher level. The methods do not, in general, account for the variant's *functional role* in the broader regulatory architecture — whether the affected gene is a substrate gene, a reader of epigenetic marks, a writer that establishes marks, or an eraser that removes marks.

### 7.2 The framework's prediction

The Medicine paper proposes comparing disorders affecting readers, writers, erasers or remodelers with disorders affecting other molecular functions. Restoration outcomes and underlying substrate changes need to be assessed per disorder.

The proposed variant benchmark asks whether functional grouping predicts differences in scores or their relationship with clinical labels.

(i) Test whether a declared measure of residual machinery function tracks graded outcomes for variants in specified genes, with appropriate within-gene comparisons.

(ii) Compare the relationship between variant scores and independently assessed phenotype severity across predeclared groups.

(iii) Compare the discrimination and, for any score interpreted as a probability, the calibration of predictors across matched gene groups.

### 7.3 The proposed empirical test

The framework's predictions can be tested through reanalysis of existing AlphaMissense predictions stratified by gene functional role. The protocol:

1. Classify genes into three categories: substrate genes (encoding enzymes, transporters, structural proteins, ligands, receptors), machinery genes (encoding epigenetic readers, writers, erasers, chromatin remodelers, transcription factors), and architectural genes (encoding scaffolds and connecting structures). Standard ontologies (GO Molecular Function, ChromBase, Eukaryotic Linear Motif database) provide the classification.

2. For each gene category, examine the distribution of AlphaMissense pathogenicity scores conditional on ClinVar pathogenicity assignment.

3. Compare discrimination using AUC and fixed-threshold sensitivity or specificity at matched conservation and other covariates. If scores are interpreted as probabilities, assess calibration against observed frequencies.

4. Test prediction (i): within machinery genes, the variance of pathogenicity scores for clinically observed variants should be higher than within substrate genes, reflecting the graded relationship between machinery function and phenotype.

5. Test prediction (ii): correlate variant pathogenicity score with phenotype severity (where available from clinical literature) and compare slopes across gene categories.

These comparisons can use existing public variant data. A positive result would establish a benchmark difference under that design, with separate evidence needed for mechanism and clinical utility.

### 7.4 Implications for clinical variant interpretation

AlphaMissense supplies computational predictions [52]. Clinical variant classification under professional standards [57] uses multiple evidence types. A benchmark can test whether performance differs by gene role.

A detected difference could motivate follow-up analyses with independent functional and clinical evidence. Computational scores alone do not establish clinical significance.

### 7.5 Practical consequences

Three framework-grounded predictions for variant effect prediction methodology:

(P17) Test whether score discrimination or probability calibration differs across prespecified gene groups on held-out clinical labels.

(P18) Compare specialized and general predictors on the same held-out machinery-gene data.

(P19) Test whether including gene functional role improves predictions on an independent benchmark. Clinical classification still requires the relevant independent evidence.

The third prediction has direct clinical implications and is testable through retrospective audit of diagnostic genetic testing outcomes stratified by gene category.

---

## 8. Reader-Writer Disorder Bioinformatics

### 8.1 The framework's reader-writer disorder class

The proposed comparisons span distinct mechanisms: MECP2 binding to methylated DNA, FMR1 RNA binding, UBE3A ubiquitin ligase activity, KMT2D methyltransferase activity, KDM6A H3K27 demethylation and chromatin remodeling in ATR-X syndrome. A shared pattern of retained and altered molecular features is a hypothesis.

### 8.2 Bioinformatic patterns in Rett syndrome

Rett syndrome provides a case for comparing affected readouts. MECP2 binds methylated DNA. The extent and interpretation of global methylation changes in MECP2 loss-of-function remain open [60].

Picard and Fagiolini [60] review unresolved effects of MeCP2 malfunction on DNA methylation. Qian et al. [59] studied restoration in a human neuronal model.

Transcriptional changes described in MECP2 models include changes affecting long genes [61]. These results motivate paired measurement of methylation and transcriptome readouts under the specified conditions.

### 8.3 Generalization to other reader-writer disorders

The proposed pattern can be assessed in the following disorders with distinct molecular functions.

**Fragile X syndrome (FMR1).** FMR1 encodes an RNA-binding protein that regulates translation. Compare RNA and protein readouts in a specified model to assess the effects of altered FMR1 function.

**Angelman syndrome (UBE3A).** UBE3A encodes an E3 ubiquitin ligase. Joint protein, ubiquitination and RNA readouts can test which effects follow loss or restoration under a specified condition.

**Kabuki syndrome (KMT2D and KDM6A).** KMT2D is an H3K4 methyltransferase and KDM6A removes H3K27 methylation. Whether other features are retained and which respond to restoration depend on the disorder and model.

**ATR-X syndrome (ATRX).** ATRX remodels chromatin at sites including repetitive DNA. The distribution of altered and retained features is an empirical question.

Whether a profile of retained and altered features generalizes across these disorders remains open.

### 8.4 Differential diagnosis through multi-omic bioinformatics

A proposed differential analysis would compare paired molecular readouts under matched sampling and clinical conditions.

1. **DNA methylation.** Compare the measured loci and global profiles under a declared assay.

2. **Histone modifications.** Compare relevant marks at prespecified loci.

3. **Chromatin accessibility.** Test for locus-level or broader differences while accounting for cell composition.

4. **Transcriptome.** Test for reproducible expression differences under the specified disorder and model.

The usefulness of a combined profile for differential diagnosis requires validation against known diagnoses in independent data.

### 8.5 Therapeutic implications and bioinformatic monitoring

Mecp2 reactivation in Rett mice produced neurological rescue (Guy et al. 2007, [Medicine §10.7]). This motivates examining biomarkers of restoration. Class-wide substrate preservation and wider treatment windows remain open. Trofinetide is a separate approved Rett treatment with unknown mechanism of therapeutic effect [67].

(i) Test how expression and methylation change after restoration in a specified model, with measured levels of restored function.

(ii) Test whether baseline methylation predicts response among matched cases alongside alternative reasons for nonresponse.

(iii) Compare candidate molecular and functional markers over follow-up to assess whether they predict sustained response.

### 8.6 Practical consequences

Three framework-grounded predictions for reader-writer disorder bioinformatics:

(P20) Test whether a proposed profile of retained marks and altered expression generalizes across named disorders.

(P21) Evaluate whether multi-omic profiles distinguish defined disorder groups on an independent diagnostic cohort.

(P22) Test whether a specified baseline substrate measure predicts response to restoration of function.

The second and third predictions have direct clinical applications and motivate prospective multi-omic studies in reader-writer disorder cohorts.

---

## 9. Synthesis

### 9.1 Empirical comparisons and proposed mechanisms

The preceding sections have developed framework predictions across five active methodological domains in single-cell bioinformatics. The findings are summarized in Table 1.

| Domain | Reported comparison | Proposed factor to test | Candidate additional input | Scope of evidence |
|---|---|---|---|---|
| Trajectory inference (§2) | Direction errors in named datasets [3] | Omitted kinetics or chromatin state | Multi-omic velocity | Method-specific reports [17–19] |
| GRN inference (§3) | Variable performance relative to correlation [5] | Different GRNs consistent with RNA data | Modalities and independent priors | Benchmarks for SCENIC+ [23] and LINGER [24] |
| Perturbation prediction (§4) | Deep models compared with mean and linear baselines [6] | Target differences invisible to specified inputs | Relevant external observations or priors | Design-specific performance |
| Multi-omics integration (§5) | Modalities can have different response times [8] | Lag structure | Time-indexed multi-omics data | Method-specific evaluations [8, 41] |
| Cancer methylome (§6) | 95% subclass accuracy for Heidelberg v12.8 [43] | Which features carry diagnostic information | Additional assays on matched cases | Nested cross-validation for the specified classifier |

A shared question is whether the available data distinguish the target under study. Task-specific comparisons motivate testing that question alongside alternative explanations.

### 9.2 The information-theoretic ceiling

A quantity that differs between completions sharing the law of all observations available to the method is unidentified from that law. The target and observational design determine whether this limit applies.

The quantities proposed as subject to the ceiling include: the cell's causal regulatory network structure (§3), the response to unseen perturbations (§4), the temporal lag relationships between chromatin and transcription (§5), and the substratum-level memory operator (§6). For each, the underlying biology integrates over hidden-sector variables before the data is collected; whether the quantity lies in the hidden fibers is open.

Foundation-model benchmarks [6, 7] motivate testing candidate identification gaps. Their scores also depend on estimators, training data and evaluation design.

If the gap holds, resolving the unidentified part requires information or independently justified assumptions that distinguish the candidate completions.

### 9.3 The roadmap forward

The following approaches can be compared on targets with specified observation limits.

**Pathway 1: Multi-modal data.** Chromatin accessibility (10x Multiome, scNMT-seq), histone modifications (CITE-seq variants, Paired-Tag), methylation (scNMT-seq) and chromatin architecture (scHi-C) provide measurements beyond the transcriptome. The reported comparisons of paired-data methods, including MultiVelo and SCENIC+, concern specific tasks, datasets and baselines. Benefit for another target depends on the additional information and how the estimator uses it.

**Pathway 2: Prior biological knowledge.** Knowledge graphs (Gene Ontology, KEGG pathways, protein-protein interaction networks), motif libraries (JASPAR, HOCOMOCO) and curated regulatory databases (Regulome, ENCODE TFBS) provide candidate priors from other sources. Methods such as GEARS, SCENIC and LINGER use such constraints. Their reported performance is specific to the task, data and comparator.

**Pathway 3: Explicit memory state representation.** Models that maintain explicit chromatin-state variables alongside transcriptome variables — separate from the latent representations of deep learning models — can in principle capture non-Markovian dynamics. This approach is less developed but theoretically aligned with the framework's prediction. Mechanistic models in the MultiVelo style (coupled ODEs for chromatin and transcription) are early examples.

The three pathways are complementary, not competing. The empirical pattern suggests that combining them — multi-modal data analyzed with knowledge-graph priors using methods that maintain explicit memory state — represents the most promising methodological direction.

### 9.4 Measurements of persistent state and expression

Chromatin, DNA methylation and protein assays can measure features left unobserved by RNA assays. Whether these measurements resolve a susceptibility, causal or predictive target depends on the design.

The operator distinction motivates the comparison of molecular state with downstream expression and function. The empirical studies test particular readouts.

Methylation-based classification and specific restoration studies illustrate different applications. Neither establishes a common physical mechanism or class-wide preservation of a molecular substrate.

---

## 10. Open Questions and Limits

### 10.1 What the framework predicts but has not been tested

Several framework predictions in this paper are testable but not yet empirically verified:

(i) **Variant benchmark** (§7). Compare classification, discrimination and any probability calibration across prespecified gene groups.

(ii) **Compositional generalization and chromatin co-localization** (§4.5). The prediction that double-perturbation prediction difficulty correlates with the chromatin co-localization of the perturbed genes can be tested using existing Perturb-seq datasets stratified by chromatin features.

(iii) **Unclassifiable tumor substratum disruption** (§6.4). The prediction that unclassifiable CNS tumors have specifically altered methylation at maintenance sites versus content sites is testable in the existing Heidelberg dataset.

(iv) **Timescale-aware integration** (§5.6). Test whether measured lag structure improves specified tasks on controlled benchmark data.

Each is a discrete empirical test with clear positive and negative outcomes. The framework's bioinformatic predictions are falsifiable in a specific operational sense.

### 10.2 What the framework does not predict

The framework's predictions are limited to information-theoretic constraints and structural patterns. It does not predict:

(i) **Algorithm performance.** The conditional identification limit alone does not rank named estimators. Additional measurements can lower optimal risk when relevant to the target and loss.

(ii) **Effect sizes.** Benefits from a knowledge graph depend on the source of the prior, its relevance and the estimator.

(iii) **Failure modes outside the ceiling-bounded tasks.** The framework's information-theoretic ceiling applies to tasks requiring hidden-sector information. Other failure modes (batch effects, technical noise, dropouts, low cell numbers) are real and important but outside the framework's prediction scope.

(iv) **Specific molecular mechanisms.** The framework predicts structural patterns at the level of memory layers and information flows, not specific molecular pathways. Mechanistic biology continues to require domain-specific theoretical and experimental work.

### 10.3 Open structural questions

Three open questions remain at the structural level:

**Q1. What is the empirical $\tau_B$ hierarchy across biological systems?** The framework predicts that different memory layers have different characteristic timescales, with consequences for which modalities matter for which questions (§5.4). The actual $\tau_B$ values are tissue- and process-dependent, and have not been systematically characterized. A program of measurements characterizing $\tau_B$ across cell types, tissues, and biological processes would substantially refine the framework's bioinformatic predictions.

**Q2. How do different machinery genes contribute to the trace-out?** The framework treats epigenetic readers, writers, and erasers as components of the trace-out machinery, but the specific contribution of each to the substratum-to-emergent translation is not characterized in detail. Different machinery genes may produce different patterns of substratum-emergent dissociation, with consequences for the differential bioinformatic signatures of different reader-writer disorders (§8.3).

**Q3. What is the relationship between the framework's bioinformatic predictions and explicit kinetic models?** The framework's predictions are information-theoretic and structural. Specific kinetic models (mass-action models of gene regulation, stochastic gene expression models, polymer models of chromatin) are mechanistic. The relationship between the framework's structural picture and the mechanistic models has not been worked out in detail. A formal connection would clarify which aspects of mechanistic modeling correspond to which framework structural features.

### 10.4 Limits

The framework's bioinformatic predictions have inherent limits:

(i) **Scope of conditional memory.** C4 concerns a specified matched-present history effect. Other data limitations, such as unmeasured variables or poor reference coverage, can constrain a prediction independently of C4.

(ii) **Attainable performance.** Estimation error, model design and limited training data can keep a method below the performance achievable from its inputs.

(iii) **Empirical validation.** A comparison needs a specified target, data, loss and controls. Confounders include batch effects, dataset selection and evaluation design.

(iv) **The framework does not replace mechanistic biology.** Bioinformatic methods aim to extract biological insight from data, and biological insight requires understanding mechanisms. The framework provides a structural perspective on what mechanisms determine method performance, but does not substitute for the mechanistic understanding itself.

The mathematical limit is conditional on observational equivalence and target differences. The cellular mechanisms and relative performance proposals remain separate tests.

---

## Acknowledgements

AI assistance in preparing this work is disclosed at\
<https://github.com/amaybaum/incompleteness#ai-assistance>.

---

## References

[1] A. Maybaum, "The Incompleteness of Observation," (2026).

[2] A. Maybaum, "Non-Markovian Dynamics in Biology and Medicine," companion paper (2026).

[3] G. Gorin, M. Fang, T. Chari, and L. Pachter, "RNA velocity unraveled," *PLOS Computational Biology* **18**, e1010492 (2022).

[4] X. Yuan et al., "Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data," *Nature Biotechnology* (2024). doi:10.1038/s41587-024-02182-7.

[5] M. Fernandez-de-Retana, R. Sanchez-Corcuera, U. Zulaika, A. Bilbao-Jayo, and A. Almeida, "When Does Gene Regulatory Network Inference Break? A Controlled Diagnostic Study of Causal and Correlational Methods on Single-Cell Data," arXiv:2605.04930 (2026).

[6] C. Ahlmann-Eltze et al., "Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines," *Nature Methods* (2025). doi:10.1038/s41592-025-02772-6.

[7] K. Kedzierska et al., "Zero-shot evaluation reveals limitations of single-cell foundation models," *Genome Biology* 26, 101 (2025). doi:10.1186/s13059-025-03574-x.

[8] M. Reimegård et al., "Single-cell intracellular epitope and transcript detection reveals signal transduction dynamics" (QuRIE-seq), *Cell Reports Methods* 1, 100165 (2021).

[9] G. La Manno et al., "RNA velocity of single cells," *Nature* 560, 494–498 (2018).

[10] V. Bergen et al., "Generalizing RNA velocity to transient cell states through dynamical modeling" (scVelo), *Nature Biotechnology* 38, 1408–1414 (2020).

[11] M. Barile et al., "Coordinated changes in gene expression kinetics underlie both mouse and human erythroid maturation," *Genome Biology* 22, 197 (2021).

[12] H. Cui et al., "DeepVelo: Deep Learning extends RNA velocity to multi-lineage systems with cell-specific kinetics," bioRxiv (2022).

[13] L. Liang et al., "LatentVelo: structured latent gene expression dynamics for RNA velocity estimation," bioRxiv (2022).

[14] A. Gayoso et al., "Deep generative modeling of transcriptional dynamics for RNA velocity analysis in single cells" (veloVI), *Nature Methods* 21, 50–59 (2024).

[15] L. Liang et al., "LatentVelo: structured latent gene expression dynamics," bioRxiv (2022).

[16] A. Gayoso et al., "veloVI: deep generative modeling of transcriptional dynamics," *Nature Methods* 21, 50–59 (2024).

[17] C. Li et al., "Multi-omic single-cell velocity models epigenome-transcriptome interactions and improves cell fate prediction" (MultiVelo), *Nature Biotechnology* 40, 1690–1698 (2022).

[18] N. Yamanaka et al., "mmVelo: A deep generative model for estimating cell state-dependent dynamics across multiple modalities," bioRxiv (2024). doi:10.1101/2024.12.11.628059.

[19] T. Tang et al., "MoFlow: Multi-omic relay velocity modeling uncovers dynamic chromatin-transcription regulation across cell states," *Nature Communications* (2025). doi:10.1038/s41467-025-67259-6.

[20] X. Yuan et al., "Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data," *Nature Biotechnology* 42, 247–257 (2024).

[21] S. McCalla et al., "Comprehensive Benchmarking of Single-Cell Gene Regulatory Network Inference," *Genome Biology* 24, 21 (2023).

[22] H. Nguyen et al., "A comprehensive survey of regulatory network inference methods using single cell RNA sequencing data," *Briefings in Bioinformatics* 22, bbaa190 (2021).

[23] C. Bravo González-Blas et al., "SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks," *Nature Methods* 20, 1355–1367 (2023).

[24] X. Yuan et al., "LINGER: Lifelong neural network for gene regulation from single-cell multiome data," *Nature Biotechnology* 42, 247–257 (2024).

[25] H. Cui et al., "scGPT: toward building a foundation model for single-cell multi-omics using generative AI," *Nature Methods* 21, 1470–1480 (2024).

[26] C. V. Theodoris et al., "Transfer learning enables predictions in network biology" (Geneformer), *Nature* 618, 616–624 (2023).

[27] I. Kendiukhov, "Systematic Evaluation of Single-Cell Foundation Model Interpretability Reveals Attention Captures Co-Expression Rather Than Unique Regulatory Signal," arXiv:2602.17532 (2026).

[28] J. M. Replogle et al., "Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq," *Cell* 185, 2559–2575 (2022).

[29] T. M. Norman et al., "Exploring genetic interaction manifolds constructed from rich single-cell phenotypes," *Science* 365, 786–793 (2019).

[30] M. Lotfollahi et al., "Predicting cellular responses to complex perturbations in high-throughput screens" (CPA), *Molecular Systems Biology* 19, e11517 (2023).

[31] L. Hetzel et al., "chemCPA: Predicting Cellular Responses to Novel Drug Perturbations at a Single-Cell Resolution," NeurIPS (2022).

[32] Y. Roohani, K. Huang, J. Leskovec, "Predicting transcriptional outcomes of novel multigene perturbations with GEARS," *Nature Biotechnology* 42, 927–935 (2024).

[33] C. Bunne et al., "Learning single-cell perturbation responses using neural optimal transport," *Nature Methods* 20, 1759–1768 (2023).

[34] M. Hao et al., "Large-scale foundation model on single-cell transcriptomics" (scFoundation), *Nature Methods* 21, 1481–1491 (2024).

[35] H. Yu et al., "PerturbNet predicts single-cell responses to unseen chemical and genetic perturbations," *Molecular Systems Biology* (2025).

[36] R. Argelaguet et al., "Multi-Omics Factor Analysis (MOFA) — a framework for unsupervised integration of multi-omics data sets," *Molecular Systems Biology* 14, e8124 (2018).

[37] R. Argelaguet et al., "MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data," *Genome Biology* 21, 111 (2020).

[38] Y. Hao et al., "Integrated analysis of multimodal single-cell data" (Seurat v4), *Cell* 184, 3573–3587 (2021).

[39] J. D. Welch et al., "Single-cell multi-omic integration compares and contrasts features of brain cell identity" (LIGER), *Cell* 177, 1873–1887 (2019).

[40] A. Gayoso et al., "Joint probabilistic modeling of single-cell multi-omic data with totalVI," *Nature Methods* 18, 272–282 (2021).

[41] R. Heyne et al., "Resolving Single-Cell Gene Expression by Pseudotemporal Integration of Transcriptomic and Proteomic Datasets," *PLOS Computational Biology* (2024).

[42] D. Capper et al., "DNA methylation-based classification of central nervous system tumours," *Nature* 555, 469–474 (2018).

[43] M. Sill et al., "Advancing CNS tumor diagnostics with expanded DNA methylation-based classification" (Heidelberg classifier v12.8), *Cancer Cell*. doi:10.1016/j.ccell.2025.11.002.

[44] D. N. Louis et al., "The 2021 WHO Classification of Tumors of the Central Nervous System: a summary," *Neuro-Oncology* 23, 1231–1251 (2021).

[45] R. Drexler et al., "Unclassifiable CNS tumors in DNA methylation-based classification: clinical challenges and prognostic impact," *Acta Neuropathologica Communications* (2024). doi:10.1186/s40478-024-01728-9.

[46] C. Koelsche et al., "Sarcoma classification by DNA methylation profiling," *Nature Communications* 12, 498 (2021).

[47] M. Renaud et al., "Pan-cancer DNA methylation classification," *Genome Medicine* 14, 80 (2022).

[48] P. C. Ng, S. Henikoff, "SIFT: predicting amino acid changes that affect protein function," *Nucleic Acids Research* 31, 3812–3814 (2003).

[49] I. A. Adzhubei et al., "A method and server for predicting damaging missense mutations" (PolyPhen-2), *Nature Methods* 7, 248–249 (2010).

[50] M. Kircher et al., "A general framework for estimating the relative pathogenicity of human genetic variants" (CADD), *Nature Genetics* 46, 310–315 (2014).

[51] N. M. Ioannidis et al., "REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense Variants," *American Journal of Human Genetics* 99, 877–885 (2016).

[52] J. Cheng et al., "Accurate proteome-wide missense variant effect prediction with AlphaMissense," *Science* 381, eadg7492 (2023).

[53] J. Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596, 583–589 (2021).

[54] L. Geistlinger et al., "AlphaMissenseR: an integrated framework for investigating missense mutations in human protein-coding genes," *Bioinformatics* (2025). doi:10.1093/bioinformatics/btaf093.

[55] J. Guy et al., "Reversal of neurological defects in a mouse model of Rett syndrome," *Science* 315, 1143–1147 (2007).

[56] D. C. Tarquinio et al., "The course of awake breathing disturbances across the lifespan in Rett syndrome," *Brain & Development* 40, 515–529 (2018).

[57] S. Richards et al., "Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology," *Genetics in Medicine* 17, 405–423 (2015).

[58] J. Kaufmann et al., "Expert Recommendations for Trofinetide Use in Individuals with Rett Syndrome," *Pediatric Neurology* (2024).

[59] J. Qian et al., "Multiplex epigenome editing of MECP2 to rescue Rett syndrome neurons," *Science Translational Medicine* 15, eadd4666 (2023).

[60] N. Picard, M. Fagiolini, "Transcriptomic and Epigenomic Landscape in Rett Syndrome," *Genes* 12, 967 (2021).

[61] H. W. Gabel et al., "Disruption of DNA-methylation-dependent long gene repression in Rett syndrome," *Nature* 522, 89–93 (2015).

[62] J. C. Darnell et al., "FMRP stalls ribosomal translocation on mRNAs linked to synaptic function and autism," *Cell* 146, 247–261 (2011).

[63] M. R. Sawicka et al., "FMRP has a cell-type-specific role in CA1 pyramidal neurons to regulate autism-related transcripts and circadian memory," *eLife* 8, e46919 (2019).

[64] Y. Yi et al., "An autism-linked mutation disables phosphorylation control of UBE3A," *Cell* 162, 795–807 (2015).

[65] R. C. Cuellar et al., "KMT2D and chromatin in development and disease," *Genes & Development* 36, 1083–1100 (2022).

[66] G. Goldberg et al., "Distinct factors control histone variant H3.3 localization at specific genomic regions," *Cell* 140, 678–691 (2010).

[67] U.S. prescribing information for trofinetide, [§12.1 Mechanism of Action](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=67e6f2d9-21f6-466f-9def-826c6a4b8257).

# Chapter 17
# Bioinformatics

***

> **Status — conditional information result and conjectural applications.** The empirical comparisons below predate the framework. A common mechanism and a relation between accessible capacity and Hurst scaling are proposed tests.

## 17.1 What this chapter develops

Chapter 16 describes prior observations including mouse Rett rescue after Mecp2 reactivation. Its comparative therapeutic-window and molecular-mechanism hypotheses remain open.

This chapter applies an identification limit to specified bioinformatics tasks and discusses observational comparisons in molecular evolution.

A target that differs between hidden-sector completions sharing the law of the available transcriptome observations is unidentified from those data. The existence and magnitude of such a gap for a given biological target have to be established.

The evolutionary comparisons include reported substitution-count dispersion, phylogenetic rate autocorrelation and mean fitness trends in the Long-Term Evolution Experiment. They describe different observables.

Eight pieces occupy the chapter.

Section 17.2 states the information bound for a specified target and observation design. The effect of adding a molecular assay depends on the information it carries about that target.

Sections 17.3–17.6 relate the conditional bound to particular benchmark results. Section 17.7 discusses methylation-based tumor classification and its validation.

Section 17.8 proposes a stratified variant-effect benchmark. Section 17.9 distinguishes descriptive evolutionary trends from tests of conditional memory.

The conditional result identifies when a target is unresolved by available observations. The applications ask whether specific measurements or independently justified assumptions resolve it.

## 17.2 The information-theoretic ceiling on transcriptome-only methods

Gene expression and chromatin assays measure different variables. To determine what can be recovered from RNA alone requires a target and a precise account of the available observations.

**The structural argument.** Chapter 16 §16.10 discusses the distinction between measured molecular marks and downstream readouts. In the finite-law result, several hidden completions can share the same observable law.

If those completions differ in a target such as a regulatory edge, that target cannot be uniquely recovered from their shared observation law. Any feature common to those completions can still be identifiable.

**The information-theoretic bound.** Let $Y$ be a discrete target, $T$ the observations available for prediction and $S$ additional molecular measurements. If a predictor uses only $T$, data processing gives $I(Y;\widehat{Y})\le I(Y;T)$. Added measurements improve optimal log-loss risk by $H(Y\mid T)-H(Y\mid T,S)=I(Y;S\mid T)$. A strict gap for the specified assay requires $I(Y;S\mid T)>0$.

With squared loss, the optimal prediction is the conditional mean from the known inputs. The conditional law can also identify variance and quantiles where the relevant target is observed. Comparing practical methods requires the target, observation design and evaluation metric.

**Scaling with fixed information.** More training data can help estimate the observable law. Where completions still share that law and differ in the target, improving its estimate leaves that part of the target unidentified.

The size of a possible prediction improvement depends on the added measurements and the loss.

**Empirical motivation.** Benchmark underperformance can come from data limitations, model fit or evaluation choices. Independent contrasts are needed to establish the proposed identification gap.

## 17.3 Trajectory inference and the RNA velocity paradigm

Trajectory inference methods attempt to reconstruct cell-state transitions from single-cell snapshot data. RNA velocity (La Manno et al. 2018) is the dominant paradigm: by comparing spliced and unspliced mRNA, the method estimates the rate of change of expression for each gene, producing a vector field that points each cell toward its predicted future state. The method has been widely adopted in developmental biology, cancer research, and stem cell biology.

**The framework's structural reading.** RNA velocity measures one specific time-derivative signature in the visible-sector data (spliced-unspliced ratio) and projects it onto a low-dimensional cell-state manifold. The method assumes that this projection captures the relevant dynamics. The framework's prediction: this assumption fails when cell-state transitions depend on substratum memory not visible in the transcriptome.

Velocity methods infer local dynamics under their kinetic assumptions. Chromatin is one candidate variable affecting rates, while model assumptions and sampling can also influence direction estimates.

**Documented failures.** Gorin et al. (2022) describe failures including trajectory reversal on particular data ([Bioinformatics §2.2]). Which modeling or measurement assumption causes a particular error needs a separate test.

An RNA-only method can improve where its kinetic model or estimation is at fault. An unidentifiable direction under the entire RNA observation law would require assumptions or observations that distinguish competing completions.

**Multi-omic velocity.** MultiVelo (Li et al., 2022) includes chromatin accessibility with RNA. It reports benefits on specified datasets. Later multi-modal methods extend the available models and comparisons ([Bioinformatics §2.4]).

A paired benchmark can test whether added data improve the target under matched conditions.

## 17.4 Gene regulatory network inference

Gene regulatory network (GRN) inference attempts to reconstruct the causal regulatory architecture of cells from expression data. The methodological problem is well-defined: given expression measurements across many conditions or single cells, infer the regulatory relationships (which gene regulates which) that produced the observed patterns. Methods range from correlation-based (co-expression networks) through linear models (LASSO, regression-based methods) to deep-learning approaches.

**Benchmark results.** Some GRN evaluations report that causal methods match or underperform correlation baselines under the chosen reference networks and data design ([Bioinformatics §3.1]).

**A candidate information limit.** DNA binding, chromatin and other unmeasured states can affect transcription. Their omission matters for identification if different regulatory mechanisms remain compatible with the observed data.

Where a regulatory target differs across completions sharing the RNA law, the differing part remains unidentified. Association estimators can recover quantities defined by the RNA law.

The conditional result leaves the performance of particular causal and correlation estimators to benchmark tests.

**Multi-modal methods.** Additional measurements may distinguish the target if they resolve a difference among observationally equivalent completions.

SCENIC+ and LINGER incorporate accessibility or external priors and report performance on specific regulatory tasks ([Bioinformatics §3.3]). The reported comparisons depend on the data and reference targets.

The information increment for a specified added modality depends on the target and on what is already observed.

## 17.5 Perturbation prediction and the failure of scaling

Perturbation prediction is the bioinformatics task of predicting cellular response to genetic, chemical, or environmental perturbations from training data on related perturbations. The task is central to drug discovery (predicting effects of small molecules from training compounds) and functional genomics (predicting effects of CRISPR perturbations from training screens).

**The empirical failure of deep learning.** The bioinformatics community has invested substantial resources in foundation models trained on scRNA-seq data — large-scale neural networks trained on millions of single cells from public datasets. Models including scGPT (Cui et al. 2023, replaced by 2024 versions), Geneformer (Theodoris et al. 2023), and scFoundation have been positioned as the bioinformatics analog of language model foundation models, with the promise that scaling will produce comparable improvements.

**Perturbation benchmarks.** Ahlmann-Eltze et al. (2025) compared deep-learning approaches including GEARS with simple mean and linear baselines on the reported datasets. The evaluated models did not consistently outperform those baselines. Kedzierska et al. (2025) address separate zero-shot tasks ([Bioinformatics §4.2]).

Several explanations can contribute to these outcomes, including the available information, training design, model fit and evaluation setup.

**The conditional explanation.** For an unseen perturbation, consider whether completions agreeing on the observed inputs predict different outcomes. In that case the difference is unresolved under those inputs.

A competitive training-set mean baseline does not show that models have reached the best possible risk given the observed data.

**Use of biological priors.** GEARS and related methods use biological representations to constrain predictions. Whether those priors improve a specific target is assessed by matched model and data comparisons.

A useful prior can distinguish target-relevant models or improve estimation. It can also impose assumptions that need validation.

**Compositional generalization.** Predicting unseen combinations from single-perturbation training depends on assumptions about the joint response.

If several joint responses fit the same single-perturbation law, treated combinations or an independently supported response model can help distinguish them.

The benchmark results motivate testing which perturbation tasks have identification gaps and which benefit from different measurements or models.

## 17.6 Multi-omics integration and timescale-aware methods

Multi-omics integration combines transcriptome data with other molecular measurements — proteome, epigenome, metabolome, single-cell chromatin accessibility — into unified analyses. The methodological challenge is that different omics modalities operate at different timescales: transcript abundance changes on minutes-to-hours timescales, protein abundance on hours-to-days, chromatin state on days-to-cell-generations, DNA methylation on cell-generations-to-organism-lifetime.

**The timescale problem.** Measurements taken together can reflect biological processes with different delays. Static covariance and lagged effects address different relationships.

Histone marks, methylation, expression and chromatin organization can change on different timescales. The timescales must be measured or modeled for the experiment in question.

A time-indexed model can use lag structure when the sampling and target make it identifiable. Its predictive effect requires a matched comparison.

MultiVelo fits time-dependent chromatin and expression components. Lineage and time-series methods use other sources of temporal information. The studies’ conclusions have their own benchmarks and endpoints.

Testing the timing hypothesis requires comparing specified dynamic and static models on the same data and target.

## 17.7 Cancer methylome classification

Methylation profiles support tumor classification in specific clinical and validation settings. The following comparisons distinguish classifier performance from a possible molecular explanation.

**Heidelberg CNS tumor classifiers.** Capper et al. (2018) developed a classifier on 2,801 reference samples and reported diagnostic changes in up to 12% of prospective cases. Sill et al. report 95% subclass accuracy in nested cross-validation for v12.8, trained on 7,495 profiles with 184 subclasses ([Bioinformatics §6.1]). The percentage pertains to that design.

**A proposed molecular interpretation.** Some diagnostic methylation features could preserve information about a cell of origin. The classification result leaves the stability of the entire methylome open.

Comparisons with transcriptomic or histological methods require matched clinical targets, assays and samples.

**Cross-cancer extension.** Methylation-based classifiers have been studied in sarcomas and other cancers. Performance depends on the reference set and validation design.

A follow-up test could ask whether alteration of a specific maintenance process explains accuracy differences across tumors at controlled sampling and reference coverage.

**Unclassifiable tumors.** Drexler et al. (2024) studied v11.4 groups defined with calibrated score thresholds of 0.84 and 0.3 ([Bioinformatics §6.4]). Low purity, reference coverage and clinical sampling are among the factors that can affect confidence.

Altered methylation maintenance could contribute to low classifier scores for some cases. Its contribution remains to be separated from differences in sampling, purity and tumor types.

A test could compare predefined maintenance-associated features across cases matched for tumor type, purity and relevant clinical covariates.

## 17.8 Variant pathogenicity for reader/writer/eraser genes

Variant-effect predictors supply computational scores. Their performance can be tested by variant and gene class against independent evidence.

**Candidate gene groups.** MECP2 is a reader, KMT2D writes H3K4 marks, KDM6A removes H3K27 methylation and ATRX remodels chromatin. Their phenotypic effects and responses to restoration require disorder-specific evidence.

The proposed benchmark compares score behavior and functional readouts across prespecified groups.

*Graded outcomes.* Compare residual activity and independently measured phenotypic severity within and across specific genes.

*Pathogenicity and severity.* Test whether the relationship between a computational score and a separate severity measure differs across groups.

*Predictor performance.* Compare discrimination and any probability calibration on the same held-out data, with appropriate controls for gene, variant and reference-label differences.

**Proposed test.** The comparison could use published variant scores and suitable independent reference labels.

(i) Prespecify the functional groups and assignment criteria, including readers, writers, erasers and remodelers.

(ii) Compare sensitivity and specificity at defined thresholds and use AUC for discrimination. To evaluate calibration, compare predicted probabilities with observed frequencies.

(iii) Compare associations with independently measured severity, with uncertainty and relevant covariates accounted for.

These comparisons are proposed. Performance estimates will depend on the reference labels and data split.

**Clinical interpretation.** A computational score is one possible line of evidence. Clinical significance requires independent evidence and variant interpretation under the applicable standards ([Bioinformatics §7.4]).

## 17.9 Evolutionary observations and candidate memory tests

Studies of substitution rates and adaptation report statistical patterns at different evolutionary scales. Those patterns motivate tests of particular dynamical models.

C4 gives history dependence at a fixed recorded present. It does not force a particular count variance, autocorrelation function or mean fitness trend.

**Molecular clock overdispersion.** The molecular clock — Zuckerkandl and Pauling's proposal that protein and DNA substitutions accumulate at approximately constant rates over time — has been recognized to violate strict Poisson statistics since the 1980s. The index of dispersion $R(t) = \text{Var}/\text{Mean}$ for substitutions on a single lineage should equal 1 for a Poisson process; empirical measurements consistently exceed this value.

Positive conditional memory need not imply $R(t)>1$. For example, the finite binary law $B,0,1-B$ for a fair bit $B$ has one event in total. At the middle time the next outcome depends on the earlier bit even though the present is fixed.

Reported dispersion indices depend on taxa, genes and method. The cited mammalian analyses include estimates around $R(t)\approx5$. Bedford and Hartl and the cited Drosophila analyses report different values in their datasets.

A gamma mixture of Poisson rates can give negative-binomial overdispersion without establishing a matched-present history effect. The Bedford–Hartl comparisons motivate testing models of substitution-rate heterogeneity.

**Phylogenetic rate autocorrelation.** Correlation between inferred rates is a statistic of the fitted evolutionary model. Relating it to C4 requires a declared present observable and a conditional contrast.

Tao et al. (2019, *Molecular Biology and Evolution*) applied CorrTest to large phylogenies across the tree of life and found "extensive rate autocorrelation in DNA and amino acid sequence evolution of mammals, birds, insects, metazoans, plants, fungi, parasitic protozoans, and prokaryotes." The autocorrelation parameter $1/\nu$ ranges from 1.2 to 40 across datasets, with both synonymous and nonsynonymous rates showing significant autocorrelation. This matches the non-Markovian (grade-ii) memory signature the framework's architecture predicts; per the scope note, it is consistent with --- but does not isolate --- grade-iii P-indivisibility, since classical gamma-distributed-rate (dynamic-disorder) models reproduce the same autocorrelation.

Differences across substitution types can inform models of rate variation. The strength and explanation of the correlation depend on the phylogeny and fitted model.

**LTEE mean fitness trajectories.** A mean trend is distinct from the temporal dependence of deviations about that trend. Inferring stochastic memory requires a process model or a separate analysis of the residual trajectory.

Wiser, Ribeck and Lenski (2013) reported a power-law fit $w(t)=(1+t/\tau)^\beta$ to the measured mean fitness trend in the LTEE and discussed a model with clonal interference and diminishing returns.

The fitness-trend exponent does not determine a stochastic Hurst exponent. The latter requires a specified scaling law and suitable time-series data.

The value $0.79\pm0.03$ in [Complexity §8.11] is a retrospective description of selected kinetic and spectral inputs under stated conversions. It supplies no estimate for taxa. Whether memory scaling varies with accessible capacity remains open.

**Punctuated equilibrium.** Stasis and intervals of rapid change can motivate models with slow variables. Establishing a particular history mechanism requires comparison with other processes that produce the same pattern.

The fossil pattern is a comparison for candidate models, with the aspects of the past available to the data defined by the setting.

**Evolutionary capacitance.** A buffering mechanism can retain variation that becomes visible under a change in conditions. Its history dependence can be tested for a declared present and perturbation.

The cited Hsp90 experiments motivate such tests in a particular buffering system. A change after stress leaves open the kinetics of the proposed readback.

Overdispersion, autocorrelation, mean fitness fits and buffering concern different observables. Each motivates tests with a specified present state and candidate record.

These are comparisons with prior observations. The proposed connection to a common capacity-dependent model remains to be demonstrated.

## 17.10 Chapter close: the structural roadmap forward

The identification limit applies to targets that vary across completions of the available observation law. Existing methodological and evolutionary comparisons suggest where to test for that gap or for a specific history effect.

**Three components of the roadmap.**

*Multi-modal data.* Test whether the added assay resolves differences in the target left open by the existing data.

*Knowledge graphs and prior structure.* Test whether a justified prior improves prediction relative to matched estimation on the same data.

*Explicit memory state.* A parameterized dynamical model can represent candidate slow states. Predictive benefits and identifiability need testing on the chosen task.

**Five predictions for empirical work.**

(P1) Under observational equivalence, an unseen perturbation target that differs among completions is unidentified from the common transcriptome law.

(P2) Test whether additional molecular measurements improve the optimal prediction or distinguish otherwise equivalent target models for a specified perturbation.

(P3) Compare variant scores across declared groups with held-out performance and appropriate calibration measures.

(P4) Test whether measured chromatin-maintenance features predict classification outcomes after accounting for reference coverage and sample characteristics.

(P5) Test whether independently estimated stochastic memory scaling varies with calibrated accessible capacity in prespecified systems.

The empirical studies motivate additional experiments. Their conclusions retain the scopes of their measurements and validation designs.

The information limit and readback criterion specify conditional tests. The proposed biological causes require evidence independent of compatibility with existing comparisons.

**Forward pointers.** The chapter closes the chapter sequence of the book. Chapter 18 has already developed the framework's distinctive forward predictions beyond standard QM and GR. Chapter 19 has developed the systematic inventory of resolved and open problems in fundamental physics. The remaining work consists of the back-matter appendices: prediction status (Appendix A), mathematical derivations (Appendix B), and the new common objections appendix (Appendix C) that systematically addresses the most frequent challenges to the framework's content.

Chapters 13–17 connect conditional results to particular biological and engineered systems. The applications include prior observations, reported benchmark outcomes and proposed mechanism tests.

The evidence for each application and for the underlying physical claims is assessed under its own premises.

***

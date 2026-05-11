# Phase 1 Spec — Machinery-vs-Substrate Selection Signature Test

**Date:** May 11, 2026
**Methodology:** §A.13 fifth refinement (Phase 1 deliverables 1–4)
**Origin:** §B.2.109.y open prediction
**Domain:** Evolutionary bioinformatics (empirical reanalysis of human selection scans)

---

## 1. The prediction

The framework's substratum-emergent operator distinction (Medicine §9.4, Bioinformatics §7) plus the reader-writer disorder class (Medicine §10.7) implies that **machinery genes** (epigenetic readers, writers, erasers, chromatin remodelers, transcription factors) and **substrate genes** (enzymes, structural proteins, transporters) produce *qualitatively different evolutionary signatures* under positive selection.

**Quantitative prediction:**
- Selection on machinery genes produces *weaker per-variant signals* (effect distributed across many downstream targets — no single variant has a sharply localized fitness effect of large magnitude)
- Selection on machinery genes produces *stronger aggregate gene-level signals* (cumulative effect across the gene is substantial because the gene's function is broadly important)
- Selection on substrate genes produces *concentrated per-variant signals* (a single variant in a key catalytic residue can have a large localized fitness effect)

**Methodological consequence:**
- Per-variant selection scans (iHS, nSL, XP-EHH, single-marker tests) should *underdetect* machinery-gene adaptive events relative to gene-burden tests
- Gene-aggregation tests (SKAT, gene-burden, regional selection scans) should detect machinery-gene selection more readily
- The asymmetry between detection-by-method should be *systematically different* between gene functional categories

## 2. Why this needs a Phase 1 spec

The §B.2.109.y entry stated the prediction but classified it as "needs careful empirical control for confounders (gene length, mutation rate, recombination rate, pleiotropy)." Without a precise Phase 1 spec, the empirical work risks:

1. **Garden-of-forking-paths failure**: many gene categorization schemes (GO Molecular Function, ChromBase, custom curation) and many selection statistics (iHS, nSL, XP-EHH, integrated haplotype score, CMS, derived allele frequency) and many controls (gene length, recombination, mutation rate); without pre-registration, post-hoc selection of categorization × statistic × control combination becomes possible.

2. **Confounder failure**: machinery genes are systematically *longer* than substrate genes (chromatin regulators tend to be larger proteins than enzymes). Gene-length confounding alone could produce the predicted signal pattern. Without explicit length matching, a positive result would be uninterpretable.

3. **Reverse-causation failure**: if a machinery gene's per-variant signal is weak because the gene is *not* actually under selection (rather than because selection is diffused across variants), the prediction's interpretation flips.

The fifth refinement's measurement-procedure pre-registration addresses all three.

## 3. The four Phase 1 deliverables

### 3.1 Computational scoping

**Dataset.** The 1000 Genomes Project Phase 3 (2,504 individuals, 26 populations) is the canonical reference. Alternative datasets for cross-replication: gnomAD v3 (76,156 individuals, more variants); UK Biobank (500,000 individuals, but mostly European ancestry). Recommended primary: 1000 Genomes for population diversity; secondary: gnomAD for variant density.

**Pre-computed selection statistics.** Use published genome-wide scans:
- iHS, nSL, XP-EHH: 1000 Genomes Selection Browser (selscan output from Voight et al. 2006 methodology, updated)
- CMS (Composite Multi-Signal): Grossman et al. 2013 / Ferrer-Admetlla et al. 2014 methodology
- SDS (Singleton Density Score): Field et al. 2016 methodology — recent selection
- Gene-burden: SKAT-O or SAIGE-GENE+ outputs on 1000 Genomes or gnomAD

**Gene functional categorization.** Two classification schemes, both pre-registered:
- *Scheme A (canonical):* ChromBase (Marakulina et al. 2023) for chromatin regulators; UniProt enzyme/structural categories for substrate genes; Eukaryotic Linear Motif (ELM) database for short linear motif-containing TF genes.
- *Scheme B (validation):* Gene Ontology Molecular Function categories filtered to: chromatin binding, transcription factor activity, histone-modifier activity (machinery); catalytic activity, transporter activity, structural molecule activity (substrate). Excludes ambiguous genes.

**Sample size and gene-set composition.**
- Machinery genes: ~600-800 in Scheme A (ChromBase has ~800 chromatin regulators; ELM-curated TFs add ~400 but overlap exists)
- Substrate genes: ~3000-5000 in Scheme A (filtered to remove pleiotropic genes with both catalytic and regulatory roles)
- Both sets need length matching (see below)

**Computational resources.** All Phase 2 work uses published per-gene statistics tables (not raw genotypes). Tractable on a desktop workstation; not chat-tractable for execution (depends on access to selection-scan output tables).

### 3.2 Decomposition

**Smallest informative version.** Restrict to *human* selection scans within the last 100,000 years (positive selection signatures detectable in 1000 Genomes). Don't extend to:
- Cross-species comparisons (different timescales, different selection pressures)
- Negative selection / purifying selection (different statistical methods)
- Balancing selection (different signatures, different timescales)

**Minimum gene set.** Pre-register a curated list of:
- 100 *machinery exemplars*: high-confidence chromatin regulators (e.g., EZH2, DOT1L, KDM6A, ARID1A, SMARCA4, BRD4)
- 100 *substrate exemplars*: high-confidence enzymes/transporters (e.g., LCT, CYP2D6, ADH1B, SLC24A5, MCM6 — known under recent positive selection)

Including known-selected substrate exemplars (LCT, ADH1B, SLC24A5, MCM6) is essential for *positive control* — if these don't show strong per-variant signals, the methodology is broken.

### 3.3 Measurement procedure (the new requirement from §A.13 fifth refinement)

**The precise quantities computed:**

For each gene $g$ in {machinery, substrate} categories:

**Statistic 1 — Per-variant selection score (PVS).** Maximum per-variant iHS or nSL score within the gene's coding region. Reported as $\max_v |iHS(v)|$ where $v$ ranges over all common (MAF > 0.05) variants in gene $g$. *Confounder-corrected version:* permutation-adjusted PVS controlling for gene length.

**Statistic 2 — Gene-level burden score (GBS).** SKAT-O or SAIGE-GENE+ p-value treating all variants in the gene as a set, weighted by frequency and predicted functional impact. *Confounder-corrected version:* permutation-adjusted GBS controlling for gene length.

**Statistic 3 — Asymmetry ratio (AR).** $AR(g) = -\log_{10}(\text{GBS}) / |\text{PVS}|$ (smoothed for division by zero). High AR means gene-level signal dominates; low AR means per-variant signal dominates.

**The pre-registered test:**

The framework predicts $\langle AR \rangle_{\text{machinery}} > \langle AR \rangle_{\text{substrate}}$ at statistically significant level after length matching.

**Length matching procedure.** Compare gene-length-matched subsets:
1. Compute gene lengths (CDS length in bp) for all machinery and substrate genes
2. Bin in 5 length quintiles
3. Within each bin, sample equal numbers from each category
4. Compute $\langle AR \rangle$ separately within each bin; pool with bin-weights inversely proportional to bin sample size

**Confounders to control:**
- Gene length (handled by length matching)
- Recombination rate (handled by including local recombination rate as covariate)
- Mutation rate (handled by including substitution rate as covariate)
- Pleiotropy (handled by excluding genes with > 10 GTEx tissue annotations)

**The pre-registered statistical test:**
- Primary: Wilcoxon rank-sum on $AR(\text{machinery}) - AR(\text{substrate})$ across length-matched pairs
- Secondary: linear regression $AR \sim$ category + length + recombination + mutation + pleiotropy
- Bonferroni-corrected for the two tests (effective $\alpha = 0.025$)

### 3.4 Outcome pre-registration

**Outcome A — Prediction confirmed.** $\langle AR \rangle_{\text{machinery}} > \langle AR \rangle_{\text{substrate}}$ at $p < 0.025$ after length matching and confounder control, with effect size $\Delta AR / \sigma_{AR} > 0.3$ (medium-to-large).
- Confidence impact: Bioinformatics cluster upgraded substantially. Adds a novel empirical signature confirming the framework's substrate-machinery distinction at evolutionary timescales. Likely worth a separate Bioinformatics §8 (Evolution) section in the standalone paper.

**Outcome B — Marginal effect.** $p \in [0.025, 0.10]$ or effect size $\Delta AR/\sigma_{AR} \in [0.1, 0.3]$ after controls.
- Confidence impact: Modest evidence; documented as supportive but not conclusive. Bioinformatics §7 reader-writer disorder class gets a footnote about evolutionary extension being suggestive.
- Recommend follow-up with larger dataset (UK Biobank) or finer functional categorization (Scheme B).

**Outcome C — No effect.** $p > 0.10$ or effect size $< 0.1$ after controls.
- Confidence impact: Prediction refuted at this resolution. Framework's evolutionary scope confirmed limited to within-lifetime dynamics. The prediction is removed from "open" status and marked refuted in §B.2.109.y.
- Bioinformatics cluster confidence unchanged (the prediction was always speculative).

**Outcome D — Confounded.** Effect size driven by an unanticipated confounder identified during analysis (e.g., gene-set selection bias, hidden population structure, batch effect in selection scan).
- Confidence impact: Inconclusive; requires more careful empirical design before re-testing.

**Outcome E — Reverse effect.** $\langle AR \rangle_{\text{machinery}} < \langle AR \rangle_{\text{substrate}}$ at $p < 0.025$ — the framework's prediction is *inverted*.
- Confidence impact: Strong refutation. The framework's machinery-substrate distinction at evolutionary timescales is operating in the opposite direction from predicted. This would be a substantive negative result requiring reassessment of the substratum-emergent extension to evolution.

### 3.5 Falsification of the speculative direction

The prediction is **refuted** by Outcome C or E.

The prediction is **confirmed** by Outcome A.

Outcomes B and D leave the line open with documented findings.

## 4. Honest pre-execution assessment

**Prior probability of Outcome A (confirmation):** Moderate (~35%).

Reason: the machinery-substrate distinction is biologically real (chromatin regulators do regulate many downstream targets), and the statistical reasoning (effects diffused across variants → weaker per-variant signal) is sound. But the same logic applies to *any* gene with broad pleiotropic effects, not specifically to "machinery" in the framework's sense. If the framework's prediction *just is* a restatement of "pleiotropic gene effects are diffused," it's not novel.

**Prior probability of Outcome B (marginal):** Moderate (~30%).

Reason: real biological effects of moderate size are common in selection scan reanalysis. The asymmetry might exist but be entangled with confounders that take effort to disentangle cleanly.

**Prior probability of Outcome C (no effect):** Moderate (~20%).

Reason: gene-length and pleiotropy controls might absorb the apparent signal, leaving no residual effect.

**Prior probability of Outcome D (confounded):** Modest (~10%).

Reason: selection scan reanalysis is methodologically tricky; unexpected confounders are common.

**Prior probability of Outcome E (reverse):** Low (~5%).

Reason: the logical structure of the prediction is sound; a reverse effect would be surprising.

**Total: ~100%, with A and B together ~65%. The expected value of doing the test is high.**

This is a **research line where the positive or marginal result is most likely**. The test is informative whether positive or negative.

## 5. Resource estimates and execution plan

**Phase 1 (this spec):** Complete. Chat-tractable.

**Phase 2 (execution, OFFLINE).** This is empirical bioinformatics work, requires:
- Download of 1000 Genomes selection-scan outputs (iHS, nSL, XP-EHH per-variant) — ~few GB
- ChromBase + UniProt + ELM gene categorizations — ~MB
- Gene-length, recombination, mutation, pleiotropy annotations — derivable from public data
- Python/R pipeline implementing the length-matched, confounder-controlled comparison
- Estimated 1-2 weeks of focused bioinformatics work

**Phase 3 (analysis, chat-tractable).** Once Phase 2 results are available:
- Compare measured $AR$ distributions against pre-registered thresholds
- Classify outcome A/B/C/D/E
- Propagate to Bioinformatics document and OI_MASTER

**Phase 2 is not chat-tractable but Phase 1 and Phase 3 are.**

## 6. Recommendation

**This Phase 1 spec is complete and ready for Phase 2 execution.** Phase 2 requires user-side bioinformatics resources (compute + analyst time).

**Two options for proceeding:**

A. **Hold Phase 2 for user-side execution** (or collaboration), proceed in chat to Bioinformatics standalone paper extraction (Suggestion 2). The Phase 1 spec can be cited in the paper as a pre-registered empirical test of the substrate-machinery prediction.

B. **Attempt a chat-tractable mini-version**: pull selection-scan summary statistics from published supplementary tables, do a crude comparison without full confounder control, treat as pilot study. This would be informative but not conclusive — Outcome A here would not constitute strong evidence; Outcome C might be due to lack of controls. The full Phase 2 protocol is necessary for a definitive test.

The Phase 1 spec serves both options.

---

## Appendix: alternative gene categorizations to investigate

If Phase 2 returns Outcome B (marginal), the following alternative categorizations may sharpen the test:

1. **By signaling pathway position**: upstream signaling genes (kinases, GPCRs) — machinery-like; downstream effectors (enzymes producing metabolites) — substrate-like.
2. **By information processing role**: epigenetic readers (BRD, PHD-finger proteins) — pure machinery; histone modifiers — machinery; histones themselves — substrate.
3. **By expression specificity**: broadly expressed (machinery) vs tissue-specific (substrate).

These are pre-registered as *secondary* analyses to be run only if primary Scheme A returns marginal results; they do not constitute additional primary tests.

---

This spec is Phase 1 complete per §A.13 fifth refinement deliverables 1-4. Phase 2 is offline-bioinformatics work; Phase 3 is chat-tractable.

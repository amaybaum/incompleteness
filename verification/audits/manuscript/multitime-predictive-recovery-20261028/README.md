# Conditional multitime predictive recovery

This audit retains the byte-frozen v2 mathematical note, exact standard-library rational controls, results, pinned-source manifest and replay provenance supporting Substratum Propositions 24.3–24.4. It is a manuscript/proof audit, not a new native V3 round, an execution of frozen 24.1B/24.1C, a kernel-status upgrade, or publication acceptance.

The manuscript contains complete proofs. The adjacent frozen note develops the hypotheses, countercontrols, physical-access boundary and standard realization-theory provenance in more detail. Its historical sources/ references refer to the original scratch audit workspace; source-manifest.json identifies exact recoverable Git bytes rather than requiring duplicate manuscript copies in this directory.

Run the bounded controls with:

    python verification/audits/manuscript/multitime-predictive-recovery-20261028/exact-controls-v2.py

The original and independent replay result hash is recorded in provenance.json. The script emits its own source hash and uses exact fractions throughout. Its 768 four-state cases and two one-state cases verify the common-length retained-word cone, singleton effects and exact quotient Hankel rank. The controls are finite evidence; the universal results are the written proofs.

Coverage remains GAP with checks=[] because the coverage schema does not permit a named probe under GAP. Actual control provenance is retained in the coverage notes and this directory; no Lean theorem or CI execution is inferred.

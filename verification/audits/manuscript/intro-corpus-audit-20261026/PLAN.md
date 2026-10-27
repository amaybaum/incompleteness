# Introduction corpus audit: plan

## Purpose

The owner (amaybaum, 2026-10-26) put the Introduction (#918) on hold:

> "The Introduction must not merge until a comprehensive scientific consistency audit across the full core OI physics
> corpus is complete."

The audit's goal, in the owner's words: "not merely to make the Introduction internally consistent. It is to ensure
that the Introduction faithfully represents what the entire OI framework actually proves, what it conditionally
derives, and what remains open."

This directory is the audit's record. It is separate from #918 so that its findings can be tracked without disturbing
the Introduction branch.

## Objects

- **Under audit:** `papers/Introduction.md` as it stands on #918 at `4a260ca9d6414e4d504a629ba5a0eb3c70bd4704`
  (sha256 `beb0a5202419a71a8a633f5999f7f48a5e8768a922b7681b7576c470b936feb8`).
- **Corpus:** `main` at `b64919cdae300c787ff51c8c9bf0355ed6dc1c0e`, the corpus commit the Introduction cites. If
  `main` moves during the audit, findings are re-checked against the new commit before the Introduction is revised.

## Scope: the core physics corpus

The corpus is audited as a whole. `papers/Main.md` presents the central results and is not the complete proof corpus
(owner, 2026-10-26; AGENTS.md, Code Review Rules, "Whole-framework scope", proposed in #940). No result is classed
unsupported because Main omits its derivation, and no document is assumed to supersede a more detailed proof
elsewhere.

**Papers:**
- `papers/Main.md`
- `papers/GR.md`
- `papers/SM.md`
- `papers/Substratum.md`
- `papers/Structure.md`
- `papers/Methodology.md`
- `papers/Juno.md`

The exploratory papers (`Complexity`, `Computation`, `Medicine`, `Bioinformatics`) and the superseded `Explainer`
are in scope only where the Introduction or a core paper relies on them.

**Book:**
- `appendix-a-prediction-status.md`
- `appendix-b-derivations.md`
- `appendix-c-objections.md`
- the physics chapters `ch01`–`ch09`, `ch18` and `ch19`, as mirrors and as carriers of status statements
- `The-Incompleteness-of-Observation-FULL.md`, as the mirror of those chapters

**Formal proofs:**
- `verification/lean/`
- `verification/lean-mathlib/` (the `OIBridge` programme)
- the Lean-to-manuscript registry `verification/lean-manuscript-census.json`

**Verification records:**
- `verification/coverage/LEDGER.json`, the manuscript-to-certificate ledger
- `verification/ROADMAP.md`, the live obligation queue
- the programme and audit records under `verification/programmes/` and `verification/audits/` that a traced claim
  depends on
- the retained Lean result `papers/introduction_repro/`

## Method

The method follows the owner's requirements.

1. **Proof inventory.** Index the theorems, derivations, hypotheses and supporting evidence the core corpus contains,
   using the corpus's own tools wherever they apply:
   - `tools/proof_census.py --json` for displayed statements;
   - the coverage ledger for their verification levels;
   - the census registry for kernel anchors;
   - ROADMAP for open obligations;
   - appendix A for prediction status.

   The inventory records each item's location, its stated hypotheses and its verification layer.
2. **Claim inventory and claim-to-proof mapping.**
   - Enumerate every substantive scientific claim in the Introduction, with a stable ID, its line and its verbatim
     text.
   - Trace each to the source that actually proves, derives or supports it, following dependencies and hypotheses
     across documents to the place where the work is done.
   - Record the full chain: the claim, the cited section, the proving source, its hypotheses, and the kernel
     declaration where there is one.
3. **Status verification.** Classify each claim by what its strongest supporting source establishes, and no more:
   - **proved:** kernel-checked, or proved on paper;
   - **conditional derivation:** with its named hypotheses;
   - **calibration identity:** a relation fitted or fixed by an empirical input;
   - **numerical observation:** a finite computation or measurement comparison;
   - **conjecture;**
   - **open problem.**

   Conditionality is recorded separately from the layer of support: a kernel proof or a paper derivation can each be
   conditional on named hypotheses. Each link of a claim's chain takes the strongest support it has anywhere in the
   corpus, and the claim takes its weakest link and every link's hypotheses. A source supports only what its own proof
   establishes for the statement as made. Rigor decides, not detail: a more detailed document does not outrank a less
   detailed but more rigorous one. An equivalence is traced one direction at a time (AGENTS.md §A.34). Where the
   Introduction's wording implies a different status from the source's, that is a finding. So is a corpus document
   that asserts more than its own proof reaches.
4. **Cross-paper consistency.** For each traced claim, compare its formulations across the corpus. Record each:
   - conflicting statement;
   - missing assumption;
   - outdated claim;
   - discrepancy in a numerical value or a prediction count.

   The authoritative anchor for a discrepancy is the maintained, most careful derivation (AGENTS.md §A.25 step 2).
   Discrepancies outside the Introduction are recorded as corpus findings for separate correction, not fixed here.
5. **Completeness.** The audit checks for understatement as well as overclaim (owner, 2026-10-26). It identifies
   results the corpus establishes that are stronger than, or absent from, what the Introduction states. Each such
   omission is a finding, with its source and status, together with whether the Introduction's scope should carry it.
   The aim is neither to exaggerate OI's achievements nor to understate what the framework has established.
6. **Independent review.** A reviewer who did not take part in steps 1–5 reviews the complete audit, including the evidence verification of step 7, and then any
   Introduction revisions that follow from it.
7. **Evidence verification.** Tracing a claim to a source is not the same as verifying the evidence behind it
   (owner, 2026-10-26). For every result the Introduction cites, the audit checks the evidence itself, by type:

   | Evidence type | Required verification |
   |---|---|
   | Lean certificates | Theorem names, axioms and dependencies, and whether kernel checking succeeded |
   | Formal proof coverage | The manuscript claim matches the precise Lean statement |
   | Exhaustive computations | Search domain, completeness, and retained certificates or witnesses |
   | Numerical results | Input data, precision, error bounds and reproducibility |
   | CI and verification receipts | Exact commit SHAs, test outcomes and retained evidence |
   | Open obligations | Assumptions or missing results that limit claims |

   Each claim in the matrix records its **evidence level**:
   - **reproduced:** the audit regenerated the result itself and compared it;
   - **certificate-checked:** checked against a retained certificate, expected result or kernel output;
   - **traced-only:** traced to an existing report whose evidence the audit did not check.

   Historical experiments are not all re-run. A bounded result is reproduced where that is cheap (§A.40). A heavy one
   is checked against its retained evidence, or proposed for a CI reproduction that needs the owner's authorization.
   Every claim must end in a verifiable chain to trustworthy evidence, or its evidence level says why not.
8. **Final landing gate.** The revised Introduction is re-checked at its exact commit: its Lean references, its corpus
   pointers, and CI on that head. Only then is fresh merge authorization requested.

Steps 9–12 extend the audit from faithfulness to scientific soundness (owner, 2026-10-27). They stay within the
claims the Introduction makes and the results those claims rest on. The whole framework's soundness is a separate
audit.

9. **Proof review.** A reviewer who did not write the proof checks the written-only proofs that the Introduction's
   central results rest on, line by line. The following are required:
   - the ε-realization: Main's finite operational realization and gluing theorem in ε-form, and its uniform
     continuum realization (`papers/Main.md:544` and `:576` at `eae01647`; R-07);
   - the finite-horizon realization with a hidden prior independent of the visible initial state, and its
     arbitrary-prior extension (Main.md:496 and :498; I-071);
   - the CP-indivisibility theorem in its framework scope (Main.md:326; I-129);
   - the Pinsker lower bound on the conditional past–future information (Main.md:167; I-103, L84);
   - BH-01's C1–C3, the written proofs in `verification/programmes/black-hole-information/bh01_access_v1/`.

   Every other claim the Introduction states as proved, whose weakest link is a paper derivation, gets a disposition:
   reviewed, or not reviewed with the reason. Each proof gets one of three verdicts:
   - **valid;**
   - **valid with named gaps:** each gap becomes a finding, with the hypothesis or step it needs;
   - **invalid:** the claim's status drops, and the drop is propagated through the matrix and FINDINGS.

   A computation that confirms a proof's instances is not a review of the proof.
10. **Results assessment.** For the results the Introduction states, separate four kinds:
    - unconditional results;
    - conditional derivations, with their named hypotheses;
    - computational findings, exhaustive-exact or numerical;
    - unresolved claims.

    For each central result, keep three questions apart: whether it is mathematically consistent, whether its
    premises are independently justified as physics, and whether it has been confronted with data (AGENTS.md §A.23).
    The priority is a precise account of how far OI explains quantum mechanics and gravity from observational
    incompleteness, and which assumptions and results are still missing.
11. **Prior-work assessment.** For each central result, identify the nearest prior work and state what the result
    adds to it: a new theorem, a new proof of a known theorem, a new reading, or nothing. Sources are read first-hand.
    A claim of novelty with no source identified is a finding.
12. **Report.** `REPORT.md` answers three questions from steps 1–11:
    - Is the Introduction correct?
    - What does OI establish?
    - What would establish or falsify the larger theory?

    For the third it names the remaining obstacles to quantum equivalence, the independent empirical predictions
    or their absence, and the research directions whose outcome would decide.

## Outputs

All outputs go in this directory:

| File | Content |
|---|---|
| `inventory/claims.json` | The Introduction's claims, with IDs, lines and verbatim text |
| `inventory/proofs.json` | The proof inventory |
| `MATRIX.md` and `matrix.json` | The claim-to-proof matrix. For each claim: its ID and text; its strongest verified source (the chain, link by link, with the layer of each link); the required assumptions; its proof status; any contradiction elsewhere in the corpus; and the status the Introduction's wording implies |
| `CONSISTENCY.md` | Cross-paper findings, each with its sites, the anchor and a proposed resolution |
| `COMPLETENESS.md` | Established results the Introduction omits or understates, each with its source, status and a recommendation |
| `FINDINGS.md` | The audit's findings for the Introduction, ranked: overclaims, understatements and omissions. Each says what the Introduction should change, or that it is faithful as written |
| `EVIDENCE.md` and `evidence.json` | The evidence verification of step 7: each cited result, its evidence type, the check made, the outcome and the evidence level |
| `proofs/` | The proof reviews of step 9: one file per proof, with the verdict and any gaps, and the dispositions of the other written-only proofs |
| `REPORT.md` | The report of step 12, with the results assessment of step 10 and the prior-work assessment of step 11 |
| `review/` | The independent reviews of the audit |

## What counts as done

The audit is complete when:
- every claim in `claims.json` has a mapping and a status;
- every finding has a disposition;
- every claim has an evidence level and every cited result has passed the evidence verification of step 7, or is
  recorded as not passing it;
- the independent review accepts the audit, including the evidence verification;
- each of the five proofs required in step 9 has an independent verdict, and every other written-only proof
  in step 9's scope has a disposition;
- `REPORT.md` answers the questions of step 12;
- an independent review accepts `proofs/` and `REPORT.md`;
- every substantive finding has a source-fix PR or a recorded no-change reason on the source-correction gate (section *Source corrections*).

The Introduction lands only after each source correction it depends on has merged, or after the finding is stated in the Introduction as an open problem.

The audit does not require every written proof in the corpus to be reviewed.

The Introduction is then revised on #918 from `FINDINGS.md`. Each revision is reviewed, and the landing gate is run
again.

## Source corrections

The owner set this requirement on 2026-10-27: "The Introduction must not become more accurate than the underlying framework it cites while leaving known errors uncorrected." Each substantive finding goes through six steps:

1. **Identify:** the exact flawed claim, its source location, and the counterexample or proof.
2. **Correct the source:** amend the original manuscript, theorem, proof or computational artifact. Historical evidence is kept, and corrections are made forward.
3. **Check dependencies:** find the downstream results and other papers that rely on the flawed statement, and correct them as well (AGENTS.md §A.25).
4. **Correct the Introduction:** align #918 with the corrected source.
5. **Verify independently:** re-review the correction and its downstream implications.
6. **Close:** a finding closes only when its corrections are merged and their evidence is recorded.

A substantive finding is any finding in FINDINGS (a) whose corpus side is a correction, every row of FINDINGS (d), and every S9 finding in `proofs/README.md` other than a documentation issue that touches only the audit's own record. Each has either a source-fix PR, or a recorded reason why no source change is needed, on the source-correction gate (the gate Issue linked from #941 and #944).

An open problem may be reported as open. The Introduction does not cite as established a result the audit has found invalid, whether or not the source has been corrected yet.

## Authority

- #918 stays on hold whatever its CI or earlier reviews show. No merge authorization is in effect.
- This audit changes no manuscript text itself. Corpus corrections go through separate source-fix PRs (section *Source corrections*), each with its own review and owner approval.

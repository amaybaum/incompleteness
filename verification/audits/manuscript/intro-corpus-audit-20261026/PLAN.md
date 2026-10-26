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

The method follows the owner's six requirements.

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
   establishes for the statement as made. An equivalence is traced one direction at a time (AGENTS.md §A.34). Where the
   Introduction's wording implies a different status from the source's, that is a finding. So is a corpus document
   that asserts more than its own proof reaches.
4. **Cross-paper consistency.** For each traced claim, compare its formulations across the corpus. Record each:
   - conflicting statement;
   - missing assumption;
   - outdated claim;
   - discrepancy in a numerical value or a prediction count.

   The authoritative anchor for a discrepancy is the maintained, most careful derivation (AGENTS.md §A.25 step 2).
   Discrepancies outside the Introduction are recorded as corpus findings for separate correction, not fixed here.
5. **Independent review.** A reviewer who did not take part in steps 1–4 reviews the complete audit, and then any
   Introduction revisions that follow from it.
6. **Final landing gate.** The revised Introduction is re-checked at its exact commit: its Lean references, its corpus
   pointers, and CI on that head. Only then is fresh merge authorization requested.

## Outputs

All outputs go in this directory:

| File | Content |
|---|---|
| `inventory/claims.json` | The Introduction's claims, with IDs, lines and verbatim text |
| `inventory/proofs.json` | The proof inventory |
| `MAPPING.md` | Claim → source chain, hypotheses and status for every claim; `mapping.json` holds the same |
| `CONSISTENCY.md` | Cross-paper findings, each with its sites, the anchor and a proposed resolution |
| `FINDINGS.md` | The audit's findings for the Introduction, ranked. Each says what the Introduction should change, or that it is faithful as written |
| `review/` | The independent review of the audit |

## What counts as done

The audit is complete when:
- every claim in `claims.json` has a mapping and a status;
- every finding has a disposition;
- the independent review accepts the audit.

The Introduction is then revised on #918 from `FINDINGS.md`. Each revision is reviewed, and the landing gate is run
again.

## Authority

- #918 stays on hold whatever its CI or earlier reviews show. No merge authorization is in effect.
- This audit changes no manuscript text. Corpus corrections it identifies go to the owner as separate proposals.

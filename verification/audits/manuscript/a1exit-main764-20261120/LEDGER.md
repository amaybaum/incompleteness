# A1-EXIT Main:764 — the typical-state qualification of canonical typicality

**Status.** Writer's correction ledger for the Main:764 unit of the A1-exit objective, WIP /
UNVERIFIED. Independent non-author exact-head review is required; merge is a separate owner
decision. One sentence of `papers/Main.md` is corrected; no physical premise is added, no
conditional mechanism is promoted or dropped, and no §A.23 correctness band moves (bands unchanged:
consistency work).

**Authorization.** Owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, Step 1 table, row "Main:764": "Restore the typical-state qualification of
[31]; it does not apply to single configuration microstates (Stage 1(ii) O1(a), G1)" — "Minimal
correction", "Separately controlled manuscript edit". Goal link (§A.47), as recorded there: "Make
OI's foundational formulation independent of the assumption that the whole universe is finite,
while keeping honest limitations on the results that still require finiteness." This unit decides
whether the corollary's typicality step is stated with the scope [31] proves.

**Base.** `main` at `9db518844` (merge of #1460). `M:n` is line `n` of `papers/Main.md`; the edit
changes no line count.

## Finding corrected

`verification/audits/foundations/r1-l8-stage1ii-20261120/AUDIT.md` (on `main`; support):

- **O1 (a).** M:764 states that [31] "implies every local subsystem is also in its local
  equilibrium". [31] gives this only for typical ψ and a fixed subsystem; the typical-state
  quantifier and its measure are dropped.
- **G1.** For a configuration |s⟩ = |s_Σ⟩ ⊗ |s_rest⟩ (site factorization, M:732 posit (viii)) the
  reduced state is pure and D(|s_Σ⟩⟨s_Σ|, Ω_Σ) ≥ 1 − ⟨s_Σ|Ω_Σ|s_Σ⟩ ≥ 1 − λ_max(Ω_Σ), so
  configuration microstates lie outside [31]'s typical set when Ω_Σ is spread; for the uniform law
  on the shell the conclusion is that law's exact marginal and needs no typicality.

## Hunk

| Hunk | Site | Anchor | Correction |
|---|---|---|---|
| H1 | M:764, the corollary's sentence beginning "For $(S, \varphi)$ in its equilibrium macrostate" | [31] (M:861; the published result: typical pure states of a shell subspace under the unitarily invariant measure, per fixed subsystem); AUDIT O1 (a), G1 | Typical-state quantifier, its measure and the fixed-subsystem form restored; G1's elementary bound and ensemble reading stated |

**Before (M:764, base):**

> For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies every local
> subsystem is also in its local equilibrium.

**After** (review round 1 restatement, commit after `94876956`; the first version, at `94876956`, is
in the PR history):

> For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies that, for a
> fixed local subsystem and a shell of dimension large compared with the subsystem's, the reduced
> state of a typical pure state of the equilibrium shell (typical for the unitarily invariant measure
> on it) is close to the shell's marginal on the subsystem, its local equilibrium. A configuration
> microstate $|s\rangle$ of $(S,\varphi)$ has on a subsystem $\Sigma$ the pure reduced state
> $|s_\Sigma\rangle\langle s_\Sigma|$, at trace distance at least $1-\lambda_{\max}$ from that
> marginal, $\lambda_{\max}$ its largest eigenvalue, so configuration microstates lie outside that
> typical set whenever $\lambda_{\max}$ is small. For the uniform law on the shell the conclusion
> holds exactly and needs no typicality: the shell's marginal is that law's marginal.

## Scope kept out

- The remainder of the corollary is unchanged: the τ_B bound per region under (EM), the
  region-level exclusion of (C2-slow) (AUDIT T7a, RETAINED), and the posit that every relevant
  equilibrium region mixes fast.
- The twelve global-phase statements the audit classifies NOT FOLLOWING (T6, T7b, T11b, T11c, T12,
  T14–T16, T17b, T18, T20b, T22), including M:764's "observers therefore exist only in the
  non-equilibrium phase of $(S, \varphi)$" and the §4.6 heading M:748, are not restated or narrowed
  here. They are a separate, queued Step-2 decision (owner record above, "Step 2: queued, not
  authorized") and are carried in the A1-EXIT ledger. Until that decision, the sentence after H1
  still asserts the phase conclusion; H1 removes only the quantifier defect in the step that
  precedes it.
- M:664, M:758, M:760 and M:766 (AUDIT T23, T2, T3, T8; O1 (b), weak) are unchanged.

## Main independence

The corrected sentence uses only [31] (an external published theorem Main already imports, M:664),
the site factorization of Main's own fixed-basis representation (M:732), and the elementary
trace-distance inequality D(ρ, σ) ≥ tr P(ρ − σ) for a projector P. No companion paper, book passage
or downstream record is cited or needed, directly or through a label.

## Propagation (§A.25, §A.14)

Corpus grep at the base over `papers/*.md`, `book/*.md` and FULL for "canonical typicality",
"canonical-typicality", "typicality", "every local subsystem", "local subsystem is also", "local
equilibrium", "equilibrium macrostate", "Goldstein" and "cond-mat/0511091":

- The global-to-local typicality step ("every local subsystem"): 1 hit, M:764 only.
- [31] / canonical typicality: M:664, :732, :758, :760, :764, :766, :861 only; no companion paper
  and no book file cites [31].
- "typicality" in the book (ch07:126, :147, :151; ch18:140 and their FULL mirrors) and in GR is
  Popescu–Short–Winter cycle typicality for the Page curve, unrelated to §4.6 (AUDIT control K5).
- The book's §4.6 restatements (ch02:192, ch04:178 and their FULL mirrors) restate the phase
  conclusion (AUDIT T15, T16; Step-2 scope), not the typicality step.

No exact restatement of the defect exists outside M:764; no other manuscript file changes. SM.md and
FULL are not touched (no coordination conflict with Q2). Surviving count after the edit: 0
occurrences of "every local subsystem" in `papers/` and `book/`.

## Regenerated artifacts and checks

- `sh ./build.sh Main`: ok, 106 pages (base 106), no dropped glyphs. `papers/Main.tex` and
  `papers/Main.pdf` regenerated.
- `verification/coverage/LEDGER.json`, entry `MAIN:C-observer-selection-rule-rate-condition`:
  fingerprint `99ffb12c63ad9c8a` → `cca8d157b7df0fbe` (at `94876956`) → `9830ad9513ecc4f8` (round 1). Re-affirmed: kernel `GAP`, delta "not
  formalized", assumptions unchanged and still accurate (the corrected sentence adds no
  assumption). `tools/coverage_check.py`: OK.
- SC-42 (`check_sc42_integration.py`, normal and `--self-test`): output byte-identical to the
  checked-in `sc42-integration-result.json` and `sc42-integration-controls.json`; no SC-42 record
  quotes M:764.
- staleness, voice, voice-scope, claims, duplicate, mirror, citation, architecture,
  dependency-label `--strict`, artifact-placement, manifest-drift `--check`, lean-manuscript
  census: all exit 0. legacy-records: self-test OK; the full check is undecidable in the local
  shallow worktree and runs in CI (Mathlib bridge job, full history).
- §A.32/§A.33 scan of the added text: no register, reader-instruction, self-assessment, caps
  emphasis or revision-history phrase.
- `verification/audits/foundations/a1-scope-phase0-20261120/sites.json` quotes the base sentence;
  it is a frozen phase-0 record read by no CI step and is not edited.

## Review round 1 (`94876956`, ACCEPT-WITH-NITS)

The independent review, relayed by the coordinating session, found [31] to be Goldstein–Lebowitz–Tumulka–Zanghì,
Phys. Rev. Lett. 96, 050403. It also found the G1 bound correct, Main independence clean, no mirrors, and
build, SC-42 and CI clean. The nits are handled as follows:

- **N1 (large-dimension condition), N2 (the λ_max wording), N5 (readability).** The reviewer's restatement
  is applied verbatim (the After text above).
  - *Check against [31]'s hypotheses.* In arXiv:cond-mat/0511091v2 the wave function is drawn from "the
    uniform (surface area) measure on the unit sphere" of the energy-shell subspace, which is the unitarily
    invariant measure. The system S is fixed. The conclusion is "≈" for "the overwhelming majority of wave
    functions", argued asymptotically: the bath must be "sufficiently large", in the thermodynamic limit.
    Weak coupling is needed only for the canonical form.
  - The source gives no explicit dimension inequality; a quantitative bound in terms of the subsystem's
    dimension and the shell's effective dimension is Popescu–Short–Winter's. "A shell of dimension large
    compared with the subsystem's" is therefore the qualitative form of [31]'s large-bath condition, and it
    does not claim a quantitative bound. "Close to the shell's marginal" matches the microcanonical-marginal
    statement before weak coupling is used.
- **N3 (accountable Issue for the phase statements).** The global-phase statements left in place after H1,
  M:764's "observers therefore exist only in the non-equilibrium phase of $(S, \varphi)$" among them, are
  tracked as follows:
  - accountable Issue: #1169, the A1-exit objective, Step 2 (queued, not authorized);
  - in the A1-EXIT ledger (PR #1466): row X-63 (the twelve global-phase rows T6, T7b, T11b, T11c, T12, T14,
    T15, T16, T17b, T18, T20b, T22) and row X-62 (this step).
- **N4 (vestigial lead-ins).** Left for Step 2, by instruction. The corollary's lead-ins are worded for the
  global-phase conclusion: "Under $\tau_{\rm mix}\ll\tau_S$: For $(S, \varphi)$ in its equilibrium
  macrostate". Their restatement belongs with X-63.

The checks after round 1 are as follows:

- `sh ./build.sh Main` runs ok: 106 pages, no dropped glyphs.
- The coverage fingerprint is re-affirmed, and `tools/coverage_check.py` reports OK.
- SC-42, normal and self-test, is byte-identical to the checked-in records.
- staleness, voice, voice-scope, claims, duplicate, mirror, citation, architecture, dependency-label
  `--strict`, artifact-placement, manifest-drift `--check` and the lean-manuscript census all exit 0.
- The §A.32/§A.33 scan of the added text is clean.
- Propagation is unchanged: there is still no mirror of the step in `papers/`, `book/` or FULL.

## Review checklist

1. The after-text states exactly what [31] proves (typical pure states, unitarily invariant
   measure on the shell, fixed subsystem) and nothing stronger.
2. The G1 bound is correct as stated (trace distance as half the trace norm).
3. No downstream dependency enters Main.
4. No global-phase claim is restated, narrowed or strengthened.
5. No mirror of the defective sentence remains in `papers/`, `book/` or FULL.
6. The coverage fingerprint re-affirmation is accurate; Main.tex/pdf are regenerated from the
   final source.

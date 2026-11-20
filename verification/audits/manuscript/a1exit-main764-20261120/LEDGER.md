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

**After:**

> For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies that, for a
> fixed local subsystem, the reduced state of a typical state of the equilibrium shell, typical for
> the unitarily invariant measure on that shell, is close to the shell's marginal on the subsystem,
> its local equilibrium. The reduced state of a configuration microstate $|s\rangle$ of
> $(S, \varphi)$ on a subsystem $\Sigma$ is the pure state $|s_\Sigma\rangle\langle s_\Sigma|$, at
> trace distance at least $1-\lambda_{\max}$ from the marginal, $\lambda_{\max}$ its largest
> eigenvalue, so configuration microstates lie outside that typical set whenever the marginal is
> spread over many configurations; for the uniform law on the shell the conclusion holds exactly,
> the shell's marginal being that law's marginal, and needs no typicality.

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
  fingerprint `99ffb12c63ad9c8a` → `cca8d157b7df0fbe`. Re-affirmed: kernel `GAP`, delta "not
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

## Review checklist

1. The after-text states exactly what [31] proves (typical pure states, unitarily invariant
   measure on the shell, fixed subsystem) and nothing stronger.
2. The G1 bound is correct as stated (trace distance as half the trace norm).
3. No downstream dependency enters Main.
4. No global-phase claim is restated, narrowed or strengthened.
5. No mirror of the defective sentence remains in `papers/`, `book/` or FULL.
6. The coverage fingerprint re-affirmation is accurate; Main.tex/pdf are regenerated from the
   final source.

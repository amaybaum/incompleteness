# AGENTS.md — contributor & agent guide

This repo holds the manuscript for *The Incompleteness of Observation*:

- `papers/` — the technical papers (`SM`, `GR`, `Substratum`, `Structure`, `Main`, …).
- `book/`   — the book chapters and the consolidated `The-Incompleteness-of-Observation-FULL.*`.
- `audit/` — the self-audit procedure (`AUDIT_METHODOLOGY.md`) and the canonical build script
  (`build.sh`). **No `.tex`, no `.pdf`.** `AUDIT_METHODOLOGY.md` is not a
  journal artifact; it rides along with the repo so that the method the manuscripts were audited
  under is versioned beside them. It is a *derived* document — the working methodology, operational
  state, reference cards, session journal, and task queue all live in the project's private records.
  Do not hand-edit it to record project state, and keep it free of journal citations, work-plan
  detail, per-cluster confidence figures, and engagement strategy: the repo is public, so anything
  added here is published whether or not it is typeset.

**`.md` is the source of truth. `.tex` and `.pdf` are generated from it** (pandoc + xelatex) — never
hand-edit them; regenerate. This applies to `papers/` and `book/`; `audit/` is markdown-only
and has no build step. This file is the condensed, repo-enforced subset of `AUDIT_METHODOLOGY.md` (§A);
when they disagree, fix the disagreement in the same commit.

---

## RULE — Whole-corpus propagation & consistency check (§A.25)

**A claim edit is not complete until it is propagated corpus-wide.** A single-location edit silently
desynchronizes the corpus — this has bitten us in both directions (the book once lagged the papers on the
dark-energy downgrade; the book once *led* the papers on the Cabibbo `c_λ` closure).

Whenever you change a **claim**, its **classification** (status / layer / tier; any of
*theorem / derived / forced / open / hypothesis / conditional / retrodiction*), or a **numeric value**:

1. **Grep the whole corpus, not the file you're in.** Search every `papers/*.{md,tex}`, `book/*.md`, and
   `book/The-Incompleteness-of-Observation-FULL.md` (plus any derivatives) for the phrase **and its
   paraphrases/symbols**. Shared claims recur in abstracts, bodies, §9-style conclusions, summary tables
   (e.g. appendix-a `G`-rows), cross-reference remarks, and the book mirror.
2. **Propagate from the authoritative anchor** — the maintained / most-careful statement (usually the body,
   or a referee-grade *Status* note). `git log -1 --format=%ci -- <path>` settles vintage when unclear.
   **Propagation is bidirectional** — check whether the book lags *or* leads the papers; don't assume.
3. **Mirror every mirror.** `FULL.md` duplicates each chapter — a chapter edit must be mirrored into
   `FULL.md` and vice-versa. Companion papers that restate a shared claim must agree.
4. **Preserve legitimate non-target uses.** The same phrase can be correct elsewhere (e.g. "theorem level"
   is right for the characterization theorem and the Brandner 2025 theorems; only the dark-energy
   *magnitude* was the overclaim). Verify each hit's context before editing.
5. **Regenerate or flag derived artifacts.** After a content edit, regenerate the affected `.tex/.pdf`
   (see below) **or** flag them stale **in the same commit**. Never leave a distributed PDF inconsistent
   with its source.
6. **Verify by re-grep.** Confirm zero stale occurrences remain and the legitimate uses survive; state the
   surviving count in the commit/PR.

**Abuse-guard:** *"I only edited the one place I was looking at"* is exactly the failure this rule prevents.

---

## RULE — Provenance integrity: anomaly sweep, quarantine-don't-delete, deterministic replay (§A.26)

Added 2026-07-25 after an integrity event: a second uncoordinated writer (most likely a concurrent
session on a shared container) produced 26 unaccounted files in the gate work area, detected only by a
filename collision.

*[Amended 2026-07-25: this rule originally opened with a "one writer at a time" clause requiring a
`REPO_LOCK` file carrying session id + timestamp + scope, and forbidding writes when an unowned fresh
lock was present. That requirement is withdrawn. In practice it added an artifact to maintain without
preventing anything, and a hand-written lock whose timestamp and scope drift out of date is itself a
source of error rather than a guard against one. The detection and containment rules below — which are
what actually caught and bounded the originating event — are unaffected.]*

1. **Anomaly ⇒ full sweep, then halt.** Any file you didn't write and can't source to the pristine
   upload/checkout triggers a complete integrity sweep (working copy vs pristine vs your own logged
   writes) *before* any further substantive work. Decisive measurements never run over an unresolved
   provenance anomaly.
2. **Quarantine, never delete.** Unaccounted artifacts move to `evidence/<event>/` with a hash+mtime
   manifest, content untouched. They may later be *verified read-only* (replay-matches, internal-claim
   checks) but are never adopted as data; if their content is right, re-derive it under your own trail
   and credit the quarantined source for priority.
3. **Deterministic replay is the integrity primitive.** Checkpoints carry full-precision parameters and
   observable series; regeneration must replay-match elementwise or the run halts. (This gate caught a
   real precision defect on 2026-07-25 before it could contaminate a verdict.)

---

## RULE — Status annotations in manuscripts: dated, superseding, manuscript-voice (§A.27)

Empirical or archival status changes reach their manuscript dependents as **dated bracketed status
notes** — `*[Status note, YYYY-MM-DD: …]*` — appended in place, superseding rather than deleting
(a correction quotes or summarizes what it replaces). Two constraints, both learned the hard way:

- **Same-session propagation.** An empirical result that bears on a manuscript claim gets its status
  note in the same session the result is accepted (this is §A.25 applied to results, not just edits).
- **Manuscript voice only.** No internal-ledger vocabulary (*graded motivated-unverified*,
  *implementation-unrecovered*), no internal filenames or phase labels, no process jargon a reader
  cannot resolve. State what is established, for which object, at what precision, and what remains
  unverified — in the paper's own register. Internal bookkeeping stays in the off-repo working logs.

---

## RULE — Governing principle: truth-seeking; hard-to-vary revisions (§A.29)

**The project's goal is truth about nature — good explanations in Deutsch's sense: hard to vary,
reaching beyond the data they were built on, open to criticism** (*The Beginning of Infinity*).
The framework's survival is subordinate to it. A route closed by controlled computation is
progress of the same kind as a route opened, and is recorded with the same care; sunk cost
confers no protection, and "the framework needs this to be true" is never an argument.

- **Computational verdicts print only over green controls.** Preregister the decision *rule*,
  not the expected numbers; generate verdict text from the measurements. A verdict rendered
  over a failed control is void.
- **Layer-0 revisions must be hard to vary:** state *in advance* the existing results the
  revision preserves (these become its controls); deliver at least one independent prediction
  or postdiction beyond the problem it was built to fix; reject any variant that can be
  adjusted to fit any outcome.

---

## RULE — Editorial integrity: assertions, status, self-narration, identifiers (§A.30)

- **Remove the assertion; keep the derivation.** A result that loses its support comes *out* of
  abstracts, enumerations, blurbs, and counts; the situation is stated declaratively where the
  result is derived. Never assert-then-qualify: a claim tagged "unsupported" in the
  manuscript's voice has been asserted and disclaimed in the same breath.
- **Status lives in status artifacts, in the artifact's own idiom** — scope sections, dated
  notes (§A.27), status tables. A status table licenses status, not editorial voice: if every
  other cell is two words, the changed cell is two words.
- **The document never narrates its own history.** No "formerly," no "is not listed," no
  "withdrawn from" in the manuscript's voice; the record of change lives in dated notes, the
  ledger, and version history.
- **Fix the root cause, not the label.**
- **Claim IDs are identifiers, not ordinals** (e.g. appendix-a `G`-rows): never renumber
  successors, never reuse a retired ID, never annotate the gap. And a removed claim can hide in
  a **count** — after any inventory change, grep the totals corpus-wide (§A.25).

---

## RULE — Gem-finding investigation mode, depth-first (§A.31)

Added 2026-08-07 by owner instruction, condensed from the project's private methodology
(Part VII), so the mode is invocable from the public subset.

Two investigation modes exist and are prioritized differently. **Closure mode** is
structured around closing a claim: identify the residual gap → hypothesize the derivation
that fills it → test → update the classification. **Gem-finding mode** is structured
around exposing hidden assumptions: identify the load-bearing step → ask *what assumption
am I implicitly making here that could be wrong?* → investigate (literature, dimensional
analysis, re-derivation, code check) → update the methodology, and the claim's status only
if a real issue is found. The gem-finding question is *what could go wrong*, not *how do I
make this work* — bias toward skepticism, not extension. Closure attempts that produce
structural understanding without binary closure are positive outcomes.

**Triggers:** (1) a claim repeatedly fails to close across sessions — the diagnostic
refines without closure; (2) methodology output accumulates faster than classification
changes; (3) the target is recognized as high-instrumental-yield — its hidden assumptions,
if found, propagate to other claims — in which case gem-finding may be the right *initial*
framing and should run *before* lower-yield investigations, so the assumption-watch
markers help those catch their own issues earlier.

**Depth-first execution (the DFS form).** Fix a PRODUCTIVITY TEST before starting: the
investigation is a gem iff it yields a fact strictly stronger than the obvious restatement
AND either constrains something or exposes a hidden assumption; otherwise it is a non-gem
(coherence relabeling). The propagation bar is better-than-coherence; below it,
record-only. Then walk the fork depth-first as numbered branch nodes, each closed by an
explicit check (code, algebra, citation) with the verdict recorded at the node; select the
decisive branch at each level rather than surveying breadth. When a branch's outcome is
favorable to the framework, apply maximum skepticism to that branch specifically —
pressure-test the favorable reading before accepting it.

**Output classification:** NEW (a structural blind spot not previously characterized) /
POSITIVE (validates an inheritance or assumption — also valuable) / ELABORATING /
CONFIRMING / BORDERLINE. **Fixed point:** continue until ~3–4 consecutive passes yield no
NEW findings. **Cross-propagation:** a hidden assumption found in one claim's audit often
applies to others; record it as an assumption-watch marker, not just a local fix.

---

## Build recipe (regenerating `.tex` / `.pdf`)

Requires `pandoc` + a LaTeX engine with `xelatex` (e.g. `brew install pandoc texlive`).

**Use `./audit/build.sh`.** It loops over the sources with the header include written in, so
the flag cannot be omitted. `./audit/build.sh` builds everything;
`./audit/build.sh SM GR` builds named papers; `--book` builds only the book. It runs from any
directory. It reports the *distinct* glyphs xelatex
dropped, which is what tells you what to add to `unicode-fix.tex`. Five papers were once
published with artifacts built without the header — the recipe below was correct and was
simply not followed, which is why the loop exists.

The equivalent commands, for reference:

```sh
# Papers (no TOC, no section numbering):
pandoc papers/<NAME>.md -s --pdf-engine=xelatex \
  --include-in-header=papers/unicode-fix.tex -o papers/<NAME>.tex
pandoc papers/<NAME>.md -s --pdf-engine=xelatex \
  --include-in-header=papers/unicode-fix.tex -o papers/<NAME>.pdf

# Book (adds a table of contents):
pandoc book/The-Incompleteness-of-Observation-FULL.md -s --toc --toc-depth=3 \
  --pdf-engine=xelatex --include-in-header=book/unicode-fix.tex \
  -o book/The-Incompleteness-of-Observation-FULL.tex   # and .pdf
```

`unicode-fix.tex` (in both `book/` and `papers/`) maps raw-Unicode Greek/math glyphs to Computer-Modern
equivalents via `newunicodechar`, so xelatex doesn't silently drop them (e.g. a title's `ℏ`, or `φ`) while
keeping the Computer Modern look. Always pass it with `--include-in-header`. After building, check the
xelatex log for `Missing character` warnings.

**Horizontal rules: use `***`, never `---`.** A bare `---` line is ambiguous in pandoc's
markdown — it can be read as a YAML metadata delimiter *or* as a table rule. The latter is the
dangerous one: it silently typesets the rest of the document into a narrow table column
(one word per line, headings rendered as literal `##`), inflating one 37-page document to 198
mostly-blank pages before it was caught. It produces no error. **Check page count and median
characters-per-page after building any new document**; a plausible page count is part of the
build, not a nicety. Note `papers/SM.md` (17), `papers/Main.md` (8) and the book (80) still
contain bare `---` rules that happen to render correctly; switch them to `***` if touched.

**Constrained-environment caveat:** if the build environment lacks a package (e.g. `lmodern.sty` absent,
no network) and a shim or workaround is used, the resulting PDFs are provisional — flag them (STALE
note or commit message) and rebuild on the canonical toolchain before any release or DOI deposit.
The `.tex` outputs are unaffected (pandoc emits them without invoking LaTeX).

---

## Honesty conventions

- **Consistency ≠ correctness — track them separately.** *Consistency* = internal coherence (no
  contradictions; claims match their stated support). *Correctness* = the estimated probability the
  framework actually matches reality.
- **Consistency / honesty edits do not, by themselves, move correctness.** Relabeling a claim adds no new
  evidence, and matching an already-known value is a *retrodiction* (discounted — already priced into the
  band) — so a pure cleanup/alignment PR is logged "bands unchanged." Correctness moves only from genuine
  new confrontation: a *novel* prediction confirmed by new data (↑), a prediction falsified (↓), or a
  first-principles derivation that closes a previously-open gap (↑) or is excluded (↓).
- **The asymmetry that does hold:** an honesty *downgrade* — conceding a claimed proof is actually
  open/conditional — can only hold or lower correctness, never raise it (you don't become more likely-true
  by admitting you proved less). And consistency work is a *force-multiplier* on the correctness tests, not
  a direct band-mover. (Full treatment: `audit/AUDIT_METHODOLOGY.md` §A.23.)
- Prefer *conditional / retrodiction / empirically-anchored / open* over *derived / theorem / proved* when
  the body doesn't fully support the stronger word.
- **Adding to the repo requires the same burden of proof as a claim (§A.28).** Before committing a file,
  section, or status note: is the risk it addresses *verified* rather than anticipated, will it still be
  true after the next change, and can it not live in a commit message or the off-repo log instead? If any
  answer is no, leave it out. Where a check is cheap, run it and remove the hazard rather than document it.

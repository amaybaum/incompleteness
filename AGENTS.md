# AGENTS.md — contributor & agent guide

This repo holds the manuscript for *The Incompleteness of Observation*:

- `papers/` — the technical papers (`SM`, `GR`, `Substratum`, `Structure`, `Main`, …).
- `book/`   — the book chapters and the consolidated `The-Incompleteness-of-Observation-FULL.*`.

**`.md` is the source of truth. `.tex` and `.pdf` are generated from it** (pandoc + xelatex) — never
hand-edit them; regenerate. The fuller working methodology lives outside git in the OI_MASTER bundle
(`01_methodology.md`, §A); this file is the condensed, repo-enforced subset.

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

## Build recipe (regenerating `.tex` / `.pdf`)

Requires `pandoc` + a LaTeX engine with `xelatex` (e.g. `brew install pandoc texlive`).

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
  a direct band-mover. (Full treatment: bundle `01_methodology.md` §A.23.)
- Prefer *conditional / retrodiction / empirically-anchored / open* over *derived / theorem / proved* when
  the body doesn't fully support the stronger word.

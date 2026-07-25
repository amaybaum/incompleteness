# Build note — derived artifacts (2026-07-25)

`.tex` and `.pdf` for `papers/{SM,GR,Explainer}` and
`book/The-Incompleteness-of-Observation-FULL` were regenerated from their
Markdown sources with the recipe in `AGENTS.md` (pandoc + xelatex,
`--include-in-header=unicode-fix.tex`; `--toc --toc-depth=3` for the book).
All other derived artifacts are unchanged, their sources being unchanged.

**The PDFs are provisional.** `lmodern.sty` was unavailable in the build
environment, and a no-op stub was supplied on `TEXINPUTS` — xelatex resolves
fonts through fontspec, and `lmodern` is a pdfTeX-era package. Per the
constrained-environment caveat in `AGENTS.md`, these PDFs should be rebuilt on
the canonical toolchain before any release or DOI deposit. The `.tex` outputs
are unaffected: pandoc emits them without invoking LaTeX.

Shim fidelity was measured rather than assumed. An unmodified source rebuilt
under the stub produced 212,144 bytes and 38 pages, against 212,140 bytes and
38 pages for the canonical build of the same source.

Page counts after rebuild, against the preceding canonical build:

| document  | new | previous |
|-----------|-----|----------|
| SM        | 127 | 126      |
| GR        |  57 |  57      |
| Explainer |  59 |  59      |
| book FULL | 503 | 502      |

The two single-page increases correspond to added text. `Missing character:
∼ (U+223C)` warnings in the SM and GR builds are pre-existing and are not
introduced by this build.

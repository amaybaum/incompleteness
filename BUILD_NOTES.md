# Build notes — §A.25 propagation sweep, phase 1 (2026-07-25)

## Artifacts WERE regenerated

`.tex` and `.pdf` were rebuilt from `.md` for every changed document using the
AGENTS.md recipe (pandoc + xelatex, `--include-in-header=unicode-fix.tex`;
`--toc --toc-depth=3` for the book).

## One shim was used — PDFs are PROVISIONAL

`lmodern.sty` is absent from this environment and there is no network to fetch
it. Per the constrained-environment caveat in AGENTS.md, a no-op stub was
supplied on `TEXINPUTS` (xelatex resolves fonts through fontspec; `lmodern` is
a pdfTeX-era package). **The resulting PDFs are therefore provisional and
should be rebuilt on the canonical toolchain before any release or DOI
deposit.** The `.tex` outputs are unaffected — pandoc emits them without
invoking LaTeX.

**Shim fidelity was controlled, not assumed.** `Main.md` was reverted to its
pristine state during this pass, so it served as a control: rebuilding it under
the shim produced 212,144 bytes / 38 pages against the canonical 212,140 bytes
/ 38 pages. The shim reproduces the canonical build.

## Page-count sanity check (AGENTS.md requires this)

| document   | pages (new) | pages (pristine) |
|------------|-------------|------------------|
| SM         | 127         | 126              |
| GR         | 57          | 57               |
| Explainer  | 59          | 59               |
| book FULL  | 503         | 502              |

The two +1 deltas are accounted for by added text (the named cross-reference
anchors in SM; the DESI tension sentence, the refined M_X tier, and the
mirrored m_t paragraph in the book). No sign of the `---` table-inflation
failure mode.

`Missing character: ∼ (U+223C)` warnings appear in the SM and GR builds. These
are pre-existing — the same glyph path exists in the pristine sources — and
were not introduced by this pass.

## Not rebuilt

`Main` and `Structure` were touched during the pass and then reverted to
pristine (see below), so their `.md`, `.tex` and `.pdf` are unchanged from the
upload and are excluded from this bundle.

## Correction to an earlier note

An earlier version of this file claimed the environment had "no pandoc/xelatex."
That was asserted without checking and was wrong: both are present. Only
`lmodern.sty` is missing.

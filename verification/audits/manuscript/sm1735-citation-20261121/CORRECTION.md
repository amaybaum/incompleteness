# SM:1735 citation correction — package (not applied)

Owner routing: #1169 (separate, minimal correction; not folded into #1477's frozen edits). Found by
NOVELTY-LEDGER (#1525, PR #1528, ledger §1.4). Drafted from `main` at `df6da1c6`. **No manuscript
is edited by this package.** It is applied, after the A1 retirement, by a separately approved commit.

## 1. The error

`papers/SM.md:1735` cites arXiv:2302.10778 to *Foundations of Physics* **53**, 82 (2023). That
journal reference belongs to a different paper.

| Source | Record |
|---|---|
| arXiv abstract page of 2302.10778 | "Journal reference: Philosophy of Physics 3(1): 8 (2025)"; related DOI 10.31389/pop.186; v1 20 Feb 2023, v3 30 Jul 2025 |
| Crossref, DOI 10.31389/pop.186 | "The Stochastic-Quantum Correspondence", *Philosophy of Physics*, vol. 3, issue 1, article 8, 2025, author Barandes |
| Crossref, *Foundations of Physics* 53, article 82 | DOI 10.1007/s10701-023-00714-w: "The Non-vanishing Imprint of Gravitational Waves as the Result of Its Nonlinear Evolution in Space" (Gurwich), 5 Sep 2023 |

## 2. Exact edits

**E1 — `papers/SM.md:1735`** (reference [28]).

Old:
```
[28] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Foundations of Physics* **53**, 82 (2023); arXiv:2302.10778.
```
New (same form as GR:998):
```
[28] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1), 8 (2025), DOI 10.31389/pop.186; arXiv:2302.10778.
```

**E2 — `papers/SM.tex:8968–8969`** (generated; not hand-edited). Current text:
```
{[}28{]} J. A. Barandes, ``The Stochastic-Quantum Correspondence,''
\emph{Foundations of Physics} \textbf{53}, 82 (2023); arXiv:2302.10778.
```
It is regenerated from E1 by `sh ./build.sh SM`, together with `papers/SM.pdf`. The expected
regenerated text carries `\emph{Philosophy of Physics} \textbf{3}(1), 8 (2025), DOI
10.31389/pop.186; arXiv:2302.10778.`

**E3 — `papers/SM.pdf`** (generated artifact; not hand-edited). Its reference list carries the same
error; text extraction of the PDF at `df6da1c6` reads "[28] J. A. Barandes, “The Stochastic-Quantum
Correspondence,” Foundations of Physics 53, 82 (2023); arXiv:2302.10778." It is regenerated
from E1 by the same `sh ./build.sh SM` run as E2, and the regenerated PDF's text is re-checked for
the corrected reference.

The in-text citation `[28]` in SM is unchanged, since the reference number does not move.

## 3. Every occurrence of this citation in the corpus (at `df6da1c6`)

Search: `2302.10778`, `Stochastic-Quantum Correspondence`, and the wrong volume (`53**, 82`,
`\textbf{53}, 82`) across `papers/*.{md,tex}`, `book/*.{md,tex}`. No `.bib` file exists in the
repository.

| Site | Text (journal part) | Status |
|---|---|---|
| `papers/SM.md:1735` | *Foundations of Physics* **53**, 82 (2023) | **Wrong** — E1 |
| `papers/SM.tex:8969` | `\emph{Foundations of Physics} \textbf{53}, 82 (2023)` | **Wrong** — E2 (regenerated) |
| `papers/SM.pdf` (reference [28]) | Foundations of Physics 53, 82 (2023) | **Wrong** — E3 (regenerated) |
| `papers/GR.md:998` / `GR.tex:5023` | *Philosophy of Physics* **3**(1), 8 (2025), DOI 10.31389/pop.186 | Correct |
| `papers/Main.md:827` | *Philosophy of Physics* **3**(1):8 (2025), no arXiv id | Correct |
| `papers/Introduction.md:224` / `Introduction.tex:965` | *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778v3 | Correct |
| `papers/Juno.md:431` / `Juno.tex:1203` | arXiv:2302.10778 (2023), no journal | Not wrong |
| `papers/Structure.md:1326` / `Structure.tex:5324` | (2023, revised 2025), arXiv only | Not wrong |
| `book/bibliography.md:25` | arXiv only (2023) | Not wrong |
| `book/The-Incompleteness-of-Observation-FULL.md:6678` / `.tex:26326` | arXiv only (2023) | Not wrong |

The wrong volume and page appear only at E1, E2 and E3. Under "minimal", the arXiv-only sites are left
as they are. Adding the journal reference there would be a separate, optional harmonization and is
not proposed here.

## 4. Dependency check against #1477

`verification/audits/foundations/a1exit-deletion-20261121/edits.json` was read at `55544cc3`,
read-only. Its schema is "a1exit deletion edit list v1", its drafting base `97070c98`, and it has 373
edits.

- **No edit touches any line in §3.** Its `papers/SM.md` sites are 22, 30, 60, 158, 222, 232 and 316.
  Its largest sites are GR.md 673, Structure.md 1303, Main.md 732 and FULL.md 360. It has no edits
  to Introduction.md, Juno.md or book/bibliography.md.
- No `old` or `new` string contains `2302.10778` or "Foundations of Physics".
- At the drafting base `97070c98`, `SM.md:1735` carries the same wrong text.

So the correction does not sit under #1477's ledger. The ledger does edit SM.md above line 1735,
so the line number can shift after the retirement.

**Application after the retirement.**
1. Refresh `main`.
2. Locate E1 by its exact old text, not by line number, and confirm that exactly one occurrence
   remains.
3. Re-run the §3 grep to confirm no new occurrence.
4. Apply E1.
5. Regenerate SM with `sh ./build.sh SM` (E2 `SM.tex` and E3 `SM.pdf`). Check that no glyphs were dropped, and
   that the page count and median characters per page are plausible (AGENTS.md build recipe).
6. Re-grep: expect zero `53**, 82` and zero `\textbf{53}, 82` hits, and no "Foundations of Physics 53, 82" in the text extracted from the regenerated `SM.pdf`, with the correct sites in §3
   unchanged.

Do this as its own commit and PR with independent review.

## 5. Status

- Classification: bibliographic error; no claim, status or numeric value changes.
- Both generated artifacts, `papers/SM.tex` (E2) and `papers/SM.pdf` (E3), must be regenerated in the same commit that applies E1 (§A.25 step 5).
- Not applied. Needs owner approval to apply after the retirement.

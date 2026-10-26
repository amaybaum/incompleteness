# Introduction draft r10: changes from r9 (publication readiness)

## Inputs

- **Base:** r9, accepted (#918 at `87fa227c`), sha256 `880ee98d…c552`. r9 is unchanged.
- **Owner decisions of 2026-10-26:** title without a hyphen; main text at most 12 pp, shortened only by cutting
  repetition, transitions and nonessential explanation; Weinberg 1989 explicitly marked as not read first-hand; the
  "Code, data and formal verification" section left as it is.
- **Method.** `draft/scripts/build_r10.py` applies 7 edits, each an exact, uniquely matching
  replacement. Every sentence it does not touch is byte-identical to r9. r10 adds no section, application or claim.

## 1. Title

r9's `#` heading and its Author and Date lines become a pandoc title block:

```
% Observational Incompleteness: From Deterministic Dynamics to Quantum Observations
% Alex Maybaum
% October 2026
```

The Status and Classification lines are kept. The title now sets on three centred lines with no hyphen, and there
are 0 overfull boxes. No cleaner route without raw LaTeX was found:
- A YAML `title:` block gives the same `\maketitle` output.
- A `#` heading cannot take a line break without raw LaTeX.

The title block costs about 0.35 pp against r9: the coordinator's prototype `tt/tb.md` measures 12.11 pp, against
11.76 for r9.

## 2. Length trims

The owner's rule allows cutting repetition, transitions and nonessential explanation. It excludes theorem
hypotheses, evidence qualifications, mathematical arguments and limitations. No limitation statement is shortened,
including those that are repeated across sections.

| # | Where | Old | New | Why it is within the rule |
|---|---|---|---|---|
| T1 | §2, opening paragraph | "This section defines three classes of finite-horizon law, shows that they coincide, identifies what the coincidence leaves (where a law's memory must sit), and states what finite recurrence does with that memory. Each result is stated with its reference; the proofs are in the cited papers." | *(deleted)* | **Transition and repetition.** §1.2 already gives this roadmap ("the content lies in where the memory of a law must sit (§2.4) and what finite recurrence does with it (§2.5)") and says where the proofs are ("Proofs … are in [Main]"). The subsection headings §2.1–§2.5 carry the rest |
| T2 | §2.2, after Theorem 1 | "[Main] writes Theorem 1 as $S\iff D\iff Q_{\mathrm{fb}}$. Theorem 1 is machine-checked …" | "Theorem 1 is machine-checked …" | **Nonessential explanation.** It is a notation cross-reference only; the Lean names that follow already identify each inclusion |
| T3 | §2.2, Realization | "[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]" | "[Main §3.4; EGGH26, Prop. 13]" | **Repetition.** The theorem's name and source are already in Theorem 1's label just above: "(finite-horizon stochastic–reversible–unitary equivalence [Main §3.4])" |
| T4 | §3.2, Theorem 4 label | "(operational-completion characterization [GR §3.3, Theorem (operational-completion characterization)])" | "(operational-completion characterization [GR §3.3])" | **Repetition** of the label inside its own citation. It now matches the form of Theorems 1–3. The §A.34 witnesses for both directions are unchanged (next paragraph) |
| T5 | §2.5, last paragraph | "Appendix B works a minimal model of Theorem 3 with six hidden states, a process with memory but no short-window indivisibility, and the smallest realization of Theorem 3, a two-card game, with its classical and quantum scope." | "Appendix B works examples: a minimal model of Theorem 3 with six hidden states, memory without short-window indivisibility, and a two-card game, the smallest realization of Theorem 3." | **Transition and repetition.** Every item is kept. Only "with its classical and quantum scope" is removed, because B.3 states that scope itself (classical stochastic on card inputs; entanglement-breaking one-step channel; classical-memory decomposition; no Bell violation) and §6.2 item 6 repeats it. "A process with memory but no" is shortened to "memory without" |

**Not trimmed: the "written proof is in [Main §3.4, Theorem (…)]" sentence of §2.4.** It is the wording of an
earlier editorial nit, and it states the verification layer.

## 3. Weinberg 1989

The OWNER landing-gate marker before §4's first sentence becomes a VERIFY marker:

> `<!-- VERIFY: Weinberg 1989 (Rev. Mod. Phys. 61, 1) is not read first-hand and is not treated as verified: the APS copy is paywalled, and the UT ScholarWorks copy (hdl 2152/61094) is blocked by its bot check from this environment; see draft/review/references/FINDINGS.md. No claim in the next sentence is attributed to Weinberg; it is cited for that sentence only once the source is read and checked. -->`

The sentence itself and the bibliography are unchanged. No claim is attributed to Weinberg.

## 4. Unchanged by instruction

The "Code, data and formal verification" section, including its commit reference `687e885b`, is byte-identical to
r9. The two §A.42 OWNER markers are kept.

## Build and checks

- **Build:** 17 pp; 0 overfull boxes; 0 missing glyphs; median 2,666 characters per page. The title has no hyphen.
- **Main text:** abstract to §6.4 ends at **p. 12, line 40**, which is **11.82 pp** by the editorial measure. "Code,
  data and formal verification" starts at the top of p. 13. For comparison, r9 measures 11.76 and the
  title-block prototype 12.11.
- **Repository checks** on a fresh `git archive 17b830bc`, with r10 as `papers/Introduction.md`:
  `voice_check` (41 files), `claims_check` and `duplicate_check` are OK.
- **Identifiers:** `identcheck.py` finds 28 identifiers, 0 unresolved and 0 mismatches.
- **Bibliography:** 38 keys, none uncited.
- **§A.32/§A.33 scan of the 8 added lines:** 0 phrase hits. The only all-caps words are VERIFY and FINDINGS,
  both inside the VERIFY comment.
- **Markers:** 2 OWNER (§A.42) and 4 VERIFY: r9's 3 plus Weinberg.
- **Raw LaTeX:** the two approved lines are unchanged, and no new raw LaTeX is added.

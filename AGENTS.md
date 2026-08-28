# AGENTS.md — contributor & agent guide

This repo holds the manuscript for *The Incompleteness of Observation*:

- `papers/` — the technical papers (`SM`, `GR`, `Substratum`, `Structure`, `Main`, …).
- `book/`   — the book chapters and the consolidated `The-Incompleteness-of-Observation-FULL.*`.
- `build.sh` — the canonical build script, at the repo root.

**This file is the single rules-and-method document in the repository.** The full working
methodology — session journal, operational state, long-form case studies, reference cards, task
queue — lives in the project's private records; what is here is the operative distillate, and it
is the document an agent loads at the start of a session. Keep it free of journal citations,
work-plan detail, per-cluster confidence figures, and engagement strategy: the repo is public, so
anything added here is published whether or not it is typeset.

The build has one entry point — `sh ./build.sh <papers…|--book>` — detailed in the build
recipe below; dropped glyphs are a hard failure. There is no other build step.

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

---

## Code Review Rules

### Claim/evidence boundary

- Flag a review blocker when a changed mathematical, physical, or status claim is
  stronger than the evidence supplied by the PR. In particular check for:
  witness → theorem, finite test → universal claim, necessary → sufficient,
  available → derived, conditional → unconditional, and ambient/background
  calculation → native OI prediction.
  Safe path: narrow the statement to the proved scope or supply an independent
  derivation/control establishing the stronger claim.

- When a probe claims a result about the framework's actual construction, verify
  that the quantity tested is derived from that construction rather than from an
  invented surrogate or illustrative distribution.

### Exactness and controls

- Do not accept floating-point evidence as certification of an exact zero, exact
  rank, exact identity, exact leading order, or algebraic obstruction when an
  exact/combinatorial calculation is available.

- A computational verdict is invalid if a required control fails, is vacuous, or
  merely reproduces the claimed formula. Decisive probes need an independent
  control or countercontrol appropriate to the claim.

### Status, propagation, and provenance

- A change to a claim, numeric value, or theorem/status classification must be
  checked across its maintained corpus mirrors. Flag stale contradictory status
  surfaces or generated artifacts.

- Preserve historical provenance. Correct current working-draft text forward;
  do not rewrite historical commits or status records merely to make the history
  agree with the latest result.

- Keep verification layers distinct: Lean/kernel certification, exact algebra,
  exhaustive finite computation, numerical evidence, and prose/status checks do
  not substitute for one another.

### Bridge and no-go scope

- Do not promote a shared necessary ingredient into an identification of two
  obstructions, a bridge, or an equivalence without an explicit formal map.

- State negative results only for the construction or class actually ruled out;
  do not turn failure of the current construction into impossibility of every
  observer-level extension.

## The audit method (condensed)

### S/C/L/R/P/M/E — the primary classifications

- **S** — Strictly parameter-free structural prediction. No fitted
 parameters; chain walks end-to-end with all links Solid.
- **C** — Conditional structural. Chain walks modulo a stated open
 assumption (e.g., "conditional on Cond 2"). Empirical match
 unaffected.
- **L** — Layered conditional. Chain walks given Layer 2 inputs;
 closure path is a specific active research direction (e.g., "S → L
 pending Direction 10").
- **R** — Retrodiction. Fitted to observation by construction; cannot
 falsify in the precision-upgrade sense. The structural content lives
 in *what's predicted given the fit* (universality, structure of
 remaining quantities), not in the fitted value.
- **P** — Phenomenological input. A specific quantity is taken from
 experiment because the framework doesn't yet derive it.
- **M** — Mass-chain inheritance. Empirical match given a single
 upstream empirical input (e.g., $m_e, m_\mu$ given $m_\tau$).
- **E** — Explicit empirical input. Some specific input enters the
 chain from experiment (acknowledged honestly).


### The four-layer framing

A separate axis from S/C/L/R/P/M/E. Captures *where in the substratum-
to-emergent stack* a prediction's derivation lives:

- **Layer 0** — Gauge structure (what gauge groups exist, what
 representations, structural constraints from C1-C3).
- **Layer 1** — Structural form (Cabibbo's $1/(\pi\sqrt{2})$, Wolfenstein
 $\sqrt{2/3}$ — pure substratum geometry/representation theory).
- **Layer 2(a)** — Operator-relation structural (e.g., the structural
 form of Cond 2 *given* that the relevant operators exist).
- **Layer 2(b)** — Solution-specific (mixing-angle values within a fixed
 operator structure).
- **Layer 3** — Mass-scale and bijection-specific (the specific values
 of $m_s$, $\mu_c$, $\mu_w$, etc., that pick out which $\varphi$).

Predictions span layers. The §7.6-style table needs both a
classification (S/C/L/...) and a layer assignment for each entry.


### Substratum / emergent / mixed (architectural classification)

Used in Step 5 (architectural review). Every load-bearing element of
a calculation lives in one of three architectural layers:

- **Substratum** — Bijection $(S, \varphi)$ on cubic lattice with
 coupling matrix $M(\mathbf{n}, \hat e_j)$. Predictions: pure
 structural ratios from geometry/representation theory.
- **Emergent** — Unitary QFT after trace-out: induced gauge couplings,
 RG running, Coleman-Weinberg potentials, $Z$-factors. Predictions:
 PT/RG outputs.
- **Mixed** — QFT machinery in derivation, but specific substratum-level
 inputs constrain the output (the most typical case for §7's
 quantitative predictions).

Framework's stated rule: *"group structural, couplings emergent."*

### Per-prediction procedure (Steps 1–7)

1. **Identify the derivation chain** — every link from substratum premise to the quoted number.
2. **Classify each link** — Solid / Motivated / Sketch, with the weakest link governing.
3. **Triage the chain** — decide what the weakest link makes the prediction (S/C/L/R/P/M/E).
4. **Literature search before closure attempts** — a gap may already be closed externally, or
   known to be hard; neither should be discovered after the work.
5. **Framework-architecture review** — place every load-bearing element as substratum / emergent /
   mixed and check the QM-emergence interface; most historical overclaims entered here.
6. **Probe sketch-grade links** — cheapest decisive computation first; "park with named gap" is
   the precise demote when a probe is out of reach.
7. **Update the prediction's classification** — and propagate it corpus-wide per §A.25.

### External comparison under OI (§A.24)

Measurements in OI are trace-out projections and the dark sector is a description artifact, so
classify any external datum before comparing: **raw/direct** observables (baryonic masses, lensing
deflections, decay rates, line and peak positions) must be reproduced as-is; **inferred**
quantities that pass through a ΛCDM-style pipeline are compared at the level of what the pipeline
measured, not its model-dependent summary. The comparison is checkable and never immunizing: a
raw-direct miss is a miss.

### Correctness vs consistency (§A.23)

A result sits on the **correctness** axis iff it is a novel empirical confrontation — a framework
output not fit to the data, against an independent measurement. Everything that confirms the
framework's claims follow from its premises sits on the **consistency** axis. External
replication/review *banks* a result on whichever axis it already occupies; it does not move a
consistency result onto the correctness axis. Internal work — however careful — moves consistency
only.

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
   surviving count in the change record.

**Abuse-guard:** *"I only edited the one place I was looking at"* is exactly the failure this rule prevents.

---

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

---

## RULE — Status changes in a working draft: correct in place, no in-manuscript change records (§A.27)

The repository is a **working draft**: the latest revision is the canonical text, and the
manuscript carries only the current state. Empirical or archival status changes therefore reach
their manuscript dependents **as corrections to the text itself** — the affected statement is
rewritten where it is derived and the superseded wording is deleted, not annotated. No dated
bracketed status notes, no "earlier revisions stated …", no reader-side version tracking. A date
stamp does not convert self-narration into a status artifact. What changed is recorded in the
repository's own history and in the change note accompanying the change; readers of the draft see
the draft.

Three constraints, all learned the hard way:

- **Same-session propagation.** A result that bears on a manuscript claim is applied to the text
  in the same session it is accepted — §A.25 applied to results, not just edits — and to every
  parallel source, per §A.14.
- **Manuscript voice only.** No internal-ledger vocabulary (*graded motivated-unverified*,
  *implementation-unrecovered*), no internal filenames or phase labels, no process jargon a reader
  cannot resolve. State what is established, for which object, at what precision, and what remains
  unverified — in the paper's own register. Internal bookkeeping stays in the off-repo working logs.
- **Never assert-then-qualify.** A claim that has lost its support is removed, not tagged; a
  correction appended beneath a surviving assertion leaves the claim asserted and disclaimed in the
  same breath (§A.30).

One exception: a document that is deliberately **not** the canonical draft — a frozen or superseded
file — may carry a standing notice of that fact, since that states current standing rather than a
revision record.

---

---

## RULE — Editorial integrity: assertions, status, self-narration, identifiers (§A.30)

- **Remove the assertion; keep the derivation.** A result that loses its support comes *out* of
  abstracts, enumerations, blurbs, and counts; the situation is stated declaratively where the
  result is derived. Never assert-then-qualify: a claim tagged "unsupported" in the
  manuscript's voice has been asserted and disclaimed in the same breath.
- **Status lives in status artifacts, in the artifact's own idiom** — scope sections, dated
  status tables (§A.27). A status table licenses status, not editorial voice: if every
  other cell is two words, the changed cell is two words.
- **The document never narrates its own history.** No "formerly," no "is not listed," no
  "withdrawn from" in the manuscript's voice, and a date stamp does not make such narration
  admissible; the record of change lives in the repository's history and the change note (§A.27),
  never in the manuscript.
- **Fix the root cause, not the label.**
- **Claim IDs are identifiers, not ordinals** (e.g. appendix-a `G`-rows): never renumber
  successors, never reuse a retired ID, never annotate the gap. And a removed claim can hide in
  a **count** — after any inventory change, grep the totals corpus-wide (§A.25).

---

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

**Use `sh ./build.sh`.** It loops over the sources with the header include written in, so
the flag cannot be omitted. `sh ./build.sh` builds everything;
`sh ./build.sh SM GR` builds named papers; `--book` builds only the book. It runs from any
directory. It reports the *distinct* glyphs xelatex
dropped, which is what tells you what to add to `unicode-fix.tex`. Five papers were once
published with artifacts built without the header — the recipe below was correct and was
simply not followed, which is why the loop exists.

The equivalent commands, for reference:

```sh
# Papers (no TOC, no section numbering):
pandoc papers/<NAME>.md -s --pdf-engine=xelatex \
  --include-in-header=tools/unicode-fix.tex -o papers/<NAME>.tex
pandoc papers/<NAME>.md -s --pdf-engine=xelatex \
  --include-in-header=tools/unicode-fix.tex -o papers/<NAME>.pdf

# Book (adds a table of contents):
pandoc book/The-Incompleteness-of-Observation-FULL.md -s --toc --toc-depth=3 \
  --pdf-engine=xelatex --include-in-header=tools/unicode-fix.tex \
  -o book/The-Incompleteness-of-Observation-FULL.tex   # and .pdf
```

`tools/unicode-fix.tex` — one shared copy for papers and book — maps raw-Unicode Greek/math glyphs to Computer-Modern
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
  band) — so a pure cleanup/alignment change is logged "bands unchanged." Correctness moves only from genuine
  new confrontation: a *novel* prediction confirmed by new data (↑), a prediction falsified (↓), or a
  first-principles derivation that closes a previously-open gap (↑) or is excluded (↓).
- **The asymmetry that does hold:** an honesty *downgrade* — conceding a claimed proof is actually
  open/conditional — can only hold or lower correctness, never raise it (you don't become more likely-true
  by admitting you proved less). And consistency work is a *force-multiplier* on the correctness tests, not
  a direct band-mover. (Condensed as §A.23 above; full treatment in the private records.)
- Prefer *conditional / retrodiction / empirically-anchored / open* over *derived / theorem / proved* when
  the body doesn't fully support the stronger word.
- **Adding to the repo requires the same burden of proof as a claim (§A.28).** Before committing a file,
  section, or status note: is the risk it addresses *verified* rather than anticipated, will it still be
  true after the next change, and can it not live in a commit message or the off-repo log instead? If any
  answer is no, leave it out. Where a check is cheap, run it and remove the hazard rather than document it.

---

## Working rules — short form

- **§A.12 Depth-first investigation.** Multi-avenue questions are driven one avenue at a time to
  exhaustion or a genuine wall before pivoting; breadth-first scoping that reports partial results
  across many avenues is the recorded failure mode. (Operationalized for gem-finding in §A.31.)
- **§A.14 Parallel manuscript sources.** `book/The-Incompleteness-of-Observation-FULL.md` and
  `book/ch*.md` are parallel sources, not derived from each other; the same content edit lands in
  both, and the propagation audit greps distinctive phrases across the pair (§A.25 step 1 covers
  this corpus-wide).
- **§A.16 Run the cheap probe.** Understanding is the terminal aim and computation is instrumental
  to it: when a computation might bear on the question, the default is to run it and see. "This
  can't bear on it" is itself an unverified claim.
- **§A.17 Peer review is the verification stage.** Its absence is the normal condition of
  in-progress work, not a constraint on development. Proceed; bank externally later (§A.23).
- **§A.18 Guard the recency ratchet.** The newest thread is always the one in working memory;
  rebuild the assessment of what matters from the whole record, not from the latest marker.
- **§A.19 Read the whole framework first.** Answers are distributed across companion papers;
  before any negative or gap claim ("the framework is silent on / omits / contradicts X"), search
  the full corpus — the answer is often already there.
- **§A.21 A probe's sign can be an artifact.** Before trusting the direction of a numerical
  result, run an exactness or symmetry control that checks the modeled operation preserves what it
  provably must.
- **§A.22 Valence moves need new results.** A conclusion may not become stronger or weaker by
  re-narration; every valence shift is backed by a new computation, representation-theory result,
  or external input.
- **§A.28 Repo minimalism.** The repo is public and permanent; the burden of proof is on adding,
  not omitting. Before committing a file: it must be needed by a reader of the manuscripts or the
  code, be maintained, and not leak process. Process artifacts are cheap to add and expensive to
  retire.

---

## Lessons register (why the rules exist — one line each)

- Dark-energy "theorem-level" overclaim recurred in 7+ places across five documents; the first fix
  left the book asserting the stronger claim for weeks — and the book has also *led* the papers
  (Cabibbo c_λ). Hence §A.25 and its abuse-guard.
- A second uncoordinated writer once left 26 unaccounted files in an active work area, found only
  by filename collision. Hence §A.26: sweep-then-halt, quarantine-never-delete, replay-match.
- Fifteen dated status notes accumulated under a rule that prescribed them; four sites asserted a
  claim and withdrew it in the same breath. Hence §A.27 as it now stands, and §A.30's
  no-self-narration clause — a date stamp does not make narration admissible.
- A mechanical status-word swap across nineteen sites once labeled a chain proved while calling its
  conclusion unsupported. Hence §A.30's remove-the-assertion rule.
- One removed claim left a stale count quoted at twenty-two sites in nine files. Hence: after any
  inventory change, grep the totals corpus-wide.
- A numerical probe once returned a confidently wrong-signed verdict from an unfaithful
  approximation that survived several turns. Hence §A.21's control requirement.
- The seven manifestations of the QM-emergence-interface antipattern (catalogued in the private
  records) are the recurring reason Step 5 exists; every historical overclaim audited traced to
  one of them.

---

## §A.32 Technical register only in paper prose

Inserted or edited text in `papers/` uses a neutral technical
register. Prohibited there (the book's essay chapters keep their own
register by design):

- meta-commentary on the corpus's own discipline, honesty, or history
  ("the discipline maintained throughout…", "stated in that register
  throughout", "the temptation resisted…");
- reader-instruction phrases ("should not be read as…", "the reader
  should note…");
- rhetorical parallelism doing the work of argument ("neither borrows
  the other's strength");
- self-assessment of the framework, favorable or unfavorable, outside
  status labels (proved / conditional / open / named hypothesis).

State the mathematical content and its status; nothing else. Review
notes and DELTA-NOTES are exempt. Enforcement:
every block's closing battery greps the diff's ADDED lines for the
phrase family above (and additions to it as found); any hit blocks
the ship until neutralized. Adopted 2026-08-10 after the b68 sweep
(nine sites neutralized in Main the same day).

## §A.33 No label-restating, caps emphasis, or revision-history voice in paper prose

Extends §A.32. Additionally prohibited in `papers/`:

- **Tautological label-restating**: sentences whose predicate restates
  the subject's own type ("Lemma 1 is a lemma", "this posit is a
  posit"). State the claim the classification makes, not the label
  assignment.
- **ALL-CAPS emphasis** in prose. Capitals are reserved for acronyms,
  named conditions and hypotheses ((C1)–(C4), (EM), H-χ, H-spin), and
  code identifiers. Status vocabulary in ledgers uses the same
  lowercase register as claims ("proved", "conditional", "open",
  "impossible").
- **Revision-history self-reference** in claims: "is now settled",
  "in its current form", "the corrected form", "as redefined",
  "no longer". Claims are stated timelessly; the revision history
  is kept out of the paper.

Enforcement: the closing battery's added-lines scan (§A.32) gains a
caps-emphasis regex (mid-sentence [A-Z]{4,} outside the whitelist) and
the history-phrase family; hits block the ship. Adopted 2026-08-10
after the b70 catch; the same-day audit swept the existing corpus.

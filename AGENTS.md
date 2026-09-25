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

- Frozen control-plane blob after head movement. When a control-plane
  preregistration is frozen by exact commit SHA and blob SHA, the blob identity is
  authoritative. If the PR head changes after freeze approval, re-read the frozen
  file at the new head and verify its blob SHA. If the approved blob is unchanged,
  the freeze remains valid; record the new head and the unchanged blob without
  requiring a full repeat review. If the blob changes at all, the freeze approval
  lapses and a fresh exact-head/blob freeze review is required before merge or
  execution. A branch sync, merge-from-base, or unrelated commit therefore does not
  invalidate a freeze merely by moving the head; it invalidates it only if it
  changes the frozen blob. This exception applies to the freeze itself, not to
  ordinary final exact-head review of execution/result PRs.

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
- Two sealed executions had their pull-request builds go red for one reason only: an archive
  clause had entered main after their base was cut, so the synthetic merge ran a newer guard
  against an older head. One was first reported as a stale watcher, and the job log said
  otherwise. Hence §A.37's diagnostic rule — check the exact-head certification before calling a
  red badge a research failure, and never cure it by merging main into a sealed execution.
- A landing's obligation table collided on four rows at once, three of which a sibling round had
  moved since the base; taking either side wholesale would have silently reverted a label merged
  twenty minutes earlier. Hence §A.37's resolve-by-merits rule and its check that a landing adds
  exactly the execution's own diff.
- The Act 21 control plane used one name, `B`, for its drafting snapshot and for the execution
  base its chronology control defined; after the merge two of its mechanical preconditions could
  not hold at the real base, one naming the drafting SHA as `B` and one requiring a token absent
  from a tree that now contained the preregistration carrying it. Caught in owner review and
  corrected by append-only amendment. Hence §A.37's `D` / `B` / `M` vocabulary subsection and
  the control-plane lint.

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

## §A.34 Directional witnesses for every displayed equivalence

Every displayed equivalence in exposition — a boxed `iff`, a biconditional,
"is equivalent to", "exactly when" — requires **separately identified kernel
witnesses for each direction**, named in the citation beside it. The check is
directional, not a count: a citation list under a box satisfies §A.25 while
still leaving one direction unproved.

Explicitly, none of the following is a converse:

- an **extension** theorem (every finite-stage object extends to the limit);
- a **uniqueness** or **canonical isomorphism** theorem (any two objects
  satisfying the hypotheses are isomorphic);
- a **density** or **closure** theorem (the constructed object is the closure
  of the stages);
- a **characterization relative to fixed data** (the object is unique *given*
  those stages and that dynamics).

Each of these derives a conclusion *from* the hypotheses. A converse derives
the hypotheses from the conclusion, and needs its own theorem. Where only one
direction is proved, the display states that direction — an isomorphism, a
uniqueness, an inclusion — rather than an equivalence.

Adopted 2026-09-03 after the Level III freeze: the propagation round drafted
`OI_Q iff quasilocal fixed-lattice QM`, propagated it to six sites, and passed
the gate, while the kernel proved only that the region completion is the unique
quasilocal system carrying the substratum's stages and dynamics. Nothing in the
kernel derived the OI_Q conditions from the existence of such a system. The
error was in prose strengthening the directionality of a proved theorem, and it
was caught in owner review rather than by any check; the same-session
correction restated the box as the uniqueness theorem and added the missing
scope guard at all six sites.

Enforcement: reviewers check each displayed equivalence against its cited
theorem statements, one direction at a time. In a research thread whose target
is an equivalence, the audit file carries the two directions as separate
pre-registered questions with their own status.

## §A.35 Registry contract for the Lean-to-manuscript census

`tools/lean_manuscript_census.py` (release-gate step `lean-manuscript`) is
complete **relative to the maintained registry**
`verification/lean-manuscript-census.json`: it resolves every cited kernel
identifier, refuses a paragraph that cites a superseded identifier without its
successor, requires every `OIBridge` module to carry a disposition, and
requires every family the manuscripts carry to name at least one anchor that is
present. It cannot infer that a theorem inside an existing module has become
stronger. A strengthening whose supersession entry or anchor is not recorded
passes all four checks.

The contract that closes the gap: **every publication-facing strengthening of a
theorem inside an existing module updates the registry in the same commit**,
with a supersession entry for the identifier it replaces and an anchor for the
statement the manuscripts must now carry. A new module is caught mechanically
(it has no family); a stronger theorem in an old module is caught only by this
contract. The registry is part of the change, as the `.tex` is part of a
manuscript edit (§A.25 step 5).

Adopted 2026-09-05 at the census round: the census note first promised that any
kernel strengthening reaching the guards and not the papers would be caught at
the next run, which the mechanism does not deliver on its own; one family
recorded as carried by the SM paper named no anchor, so its result could have
left the paper unnoticed. Both were corrected in owner review.

Enforcement: guard `R7-MSP` pins this section, the anchor requirement in the
census tool and the contract sentence in the registry; reviewers check that a
commit strengthening a theorem in an existing module touches the registry.

## §A.36 Placement of verification artifacts

New audits, preregistrations, results and amendments go under a **programme**
or **audit** directory inside `verification/`, never at the `verification/`
root. A new artifact's home is decided by the **programme/audit hierarchy** —
and by the programme's own index once one is present — placed with the round
or the audit family it belongs to; a round whose category is genuinely new
adds a directory rather than a root file.

`verification/MIGRATION-MANIFEST.md` governs a narrower thing: the migration
destinations of the **existing grandfathered root artifacts**. It is not, and
cannot be, the authority on where a future artifact belongs — a new round has
no source entry in a mapping built from the old root set.

The root is reserved for `README.md` (the landing page), `ROADMAP.md` (the live
obligation queue) and the manifest itself.

Preregistration and outcome stay **together**, inside the round that produced
them, with amendments in that round's `amendments/` subdirectory. They are not
split into global `preregistrations/` and `results/` folders: the split-PR
protocol already separates them in time, and separating them in space as well
leaves the relationship recoverable only from filenames.

`lean/`, `lean-mathlib/` and `coverage/` are out of scope for this rule. They
are technical subsystems with their own structure, and their layout is governed
by their own conventions.

Enforcement: `tools/artifact_placement_check.py` (release-gate step
`artifact-placement`) fails on any root-level `verification/*.md` the manifest
does not account for — the manifest serving there as a grandfather list, not as
a destination authority. The check is one-directional — it never complains that
a manifest entry has moved to its destination — so it holds across the
migration without amendment. It carries a self-test that drives the real
comparison through an unlisted name, a grandfathered name and an
already-migrated name.

The manifest's two forms are rendered from one mapping in
`tools/build_migration_manifest.py`, and release-gate step `manifest-drift`
runs that script's `--check` mode, which re-renders both and compares them to
what is checked in. A hand-edit to either generated file fails the gate. That
mode requires no particular layout on disk, so it holds after the migration as
well as before; the separate `--verify-tree` mode, which asserts the mapping is
in bijection with the root artifacts, is meaningful only beforehand and is
opt-in for that reason.

---

## §A.37 Round lifecycle: control plane, then execution and landing

A round is run in **two pull requests**. The **control plane** carries the
preregistration alone. The **execution pull request** carries the round's work,
and after that work is certified the same pull request carries the landing that
brings it into main.

### What this rule governs

This rule governs **rounds begun after it was written**. Rounds already
complete were run under a three-pull-request arrangement in which the landing
was a third, separate pull request, and they stay governed by that
arrangement — their frozen chronology controls say so in terms, and a
preregistration is not reinterpreted after its outcome is known. Nothing below
reaches back into a merged round, and no merged artifact changes because of it.

The vocabulary has since changed too. Freezes written before this wording say
**guarded** and **unguarded** where this rule now says *sealing* and
*non-sealing*. Earlier freezes retain the meaning fixed by their own chronology
controls; the later vocabulary does not reinterpret them. In particular #631 —
the only two-pull-request freeze written between the two wordings — states its
shape explicitly as no guard, no pin, `E` → `L`, so its meaning is unchanged. A
preregistration is not amended to track later vocabulary, and none needs to be.

### The invariant

> The **sealed execution commit never changes.** Before certification the
> execution branch never absorbs later main. After exact-head certification the
> branch may advance **only** through the canonical landing merge whose second
> parent is that sealed commit, followed by the archive pin where the round has
> one.

The invariant is attached to the **sealed execution object, not permanently to
the branch name**. That is the whole reason the third pull request can be
dropped without weakening chronology or auditability: what the guard certifies,
what review approved, and what the record must be able to identify forever is a
commit — `E` — and `E` remains exactly identifiable as the landing merge's
second parent no matter where the branch pointer has since moved.

### The control plane

The preregistration alone — targets, predictions with their signs and
strengths, recorded reasons, the status rule, the hazards, the definition
budget and the chronology control. It is reviewed, amended as the owner
directs, and merged **before any execution object exists**. Amendment happens
before the merge and only then: once merged the preregistration is
**immutable**, and an execution that diverges from it **records the
discrepancy** rather than repairing the freeze. A freeze that can be edited
after the outcome is known is not a freeze.

The control plane's **merge commit is the mandated execution base**. The
execution branches from exactly that commit and from nothing else, and its
first act is to verify that the preregistration at that base has the blob the
freeze names, before any target is executed.

### Drafting snapshots and mandated execution bases are different objects

Every control plane uses the following commit vocabulary, and no other meaning
of "base" is permitted where the distinction matters.

- "D" — the drafting snapshot. "D" is the commit against which the control
  plane was written and its pre-merge measurements were taken:
  locating-control coordinates, pinned source blobs, inventories, name-freedom
  checks, simulations and other drafting-time facts. "D" is fixed when those
  measurements are made. "D" is never the mandated execution base merely
  because the control plane was drafted from it.
- "B" — the mandated execution base. "B" is the certified merge commit on
  "main" of the latest control-plane artifact governing the round: the
  preregistration itself if there is no later amendment, otherwise the latest
  execution-affecting append-only amendment. Before that merge exists, "B" has
  no SHA. A control plane therefore must not assign its drafting snapshot's SHA
  to "B".
- "M" — a candidate control-plane merge. Before the control plane lands,
  continuous integration may construct or inspect a candidate merge solely to
  test conditions that are intended to hold at "B". "M" is predictive test
  state only and is never used as execution ancestry, seal state or historical
  evidence. The actual merge commit must be checked again after landing.

Every mechanical precondition names its evaluation scope explicitly as at "D",
at "B", or from "D" to "B".

A condition at "D" records a drafting-time fact and is not reinterpreted as a
condition on "B". In particular, name-freedom checks — that a round tag, stem,
module name, directory or other reserved identifier did not previously exist —
are checks at "D".

A condition at "B" describes the repository after the frozen control plane
itself has entered the tree. It therefore must account for the control-plane
artifacts and the names they necessarily contain. A "B"-scoped condition must
not require the absence of the preregistration, its amendments, or names whose
only occurrence is in those frozen control-plane artifacts. Where the intended
invariant is that execution has not begun, the check states that directly: no
execution module, result note, guard clause, prospective declaration, manifest
record, or other execution-specific object exists.

A condition from "D" to "B" states provenance or preservation explicitly: for
example that "D" is an ancestor of "B", that the reviewed frozen blobs occur
unchanged at "B", or that specified drafting-time source blobs remain the blobs
the round consumes.

Before a control plane may merge, continuous integration evaluates every
"B"-scoped tree/state precondition against "M". After it merges, the
"main"-push certification evaluates the same conditions against the actual
merge commit "B" and verifies every frozen control-plane blob. No execution
branch may be created until this post-merge base certification is green.

An execution-affecting append-only amendment repeats this lifecycle. Its
certified merge becomes the new "B"; every earlier control-plane merge becomes
provenance, and execution never resumes from it.

**Machine-checkable form.** A control plane that wants its preconditions run
mechanically carries one fenced block whose info string is
`control-plane-preconditions`. Header lines are `key: value` — `d:` the
drafting snapshot's SHA, `b:` the mandated base's SHA (only once it exists),
`merged: true` once the artifact is on `main`, and any number of
`frozen-blob: <path> <blob-sha>` lines naming blobs that must be found
unchanged at the evaluated commit. Every other non-comment line is one JSON
object, one precondition row: `{"id": ..., "scope": "D" | "B" | "D->B",
"check": "<shell command run at the repository root with $D, $B and $REF
exported>", "expect": "empty" | "nonempty" | "exit0"}`. `tools/control_plane_base_check.py`
runs the `B` and `D->B` rows against a candidate merge (`--mode M`) or the
actual merge commit (`--mode B`) through one code path, checks each `D` row's
`d:` for ancestry only, and verifies the frozen blobs; it exits non-zero on any
failed row. `tools/control_plane_lint.py` (release-gate step
`control-plane-lint`) reads the block and the file around it: a row without a
scope tag fails the lint, as does a file that gives "D" and "B" one SHA, a
literal SHA for "B" in an artifact not marked `merged: true`, or a "B"-scoped
`git grep` for a token that expects nothing while the round's own control-plane
files already carry the token. Both tools apply only to control-plane files that
carry the block or are added or modified in the change under check; artifacts
merged before the block existed are neither rewritten nor linted.

### The execution, up to certification

**Before certification an execution never absorbs later main.** No merge from
main, no rebase, no amend, no force-push. Its head is the object the guard
certifies, and changing it destroys the ancestry the chronology control exists
to establish. The branch will show as behind, and often as conflicted, for as
long as it sits there. That is the protocol working, not a defect to repair.

Certification fixes the sealed commit `E`. From that point `E` can never
change, and **the certification of record is the run whose `head_sha` is `E`** —
identified by that SHA, not by which run happens to be latest on the branch,
because the branch advances past `E` at landing.

### Certifying the exact head

The guard asks its ancestry question of the real `pull_request.head.sha`, never
of the synthetic merge commit that continuous integration builds. The two can
disagree, and there is one situation where they reliably do.

Continuous integration builds a pull request as its head merged into the
**current** base. When an archive clause enters main **after** an execution's
base was cut, that build runs main's newer guard file against the older head,
and the clause demands a sealed head the execution cannot reach. It fails
closed, correctly. On the exact head the guard file is the base's own, which
carries no such clause, and the check passes.

So: **a red badge on a pull request sitting at its sealed head is not by itself
a research failure.** Ask first whether the execution's own exact-head
certification is green, and whether the red comes solely from an archive clause
that entered main after the base. If both, the execution stands certified and
is left untouched.

**Dispatch is the fallback, not the routine.** The ordinary pull-request build
certifies the exact head whenever the guard-bearing job succeeds, because the
guard asks its question of the real `pull_request.head.sha` — of `E` — even
though the job runs on the synthetic merge. That is the common case: it holds
whenever no archive clause has entered main since the base, and the round needs
nothing further. **`workflow_dispatch` on the branch is for the other case**,
where the synthetic merge imports later archive state and the build fails for
chronology alone; dispatching builds the branch itself, with no synthetic
merge, and certifies `E` directly. Reach for it only then.

This transient red remains possible under the two-pull-request lifecycle, for
the same reason and for as long as the pull request sits at `E`. **It does not
invalidate an exact-SHA certification**, and it is not cured by merging main
into the execution.

When it clears is worth stating exactly, because the two halves come apart.
Putting `L` on makes the **sibling rounds' sealed heads reachable**, so their
archive clauses stop failing. But a sealing round's **own** ancestry check is
still in execution mode at that point, and execution mode rejects the sibling
history `L` has just brought in. So for a sealing round the synthetic-archive
red may clear at `L` while the round is **not final-certifiable until `P`**;
only the pin moves its own check to archive mode. For a non-sealing round,
which has no check of its own to switch, `L` is the end of it.

A **control plane** carries no mandated historical base, so the opposite rule
applies to it: when a newly landed archive clause reddens its build, merging
current main into the branch is the correct cure. Confirm afterwards that the
frozen blob is unchanged, so what freezes is what was reviewed.

### The landing phase, on the same pull request

Once `E` is certified, the execution pull request transitions into landing mode
by **appending** to it. Nothing is rewritten.

**The landing merge `L`** goes on first, always. Its first parent is **current
green main**; its second parent is **exactly `E`**. Conflicts are resolved
**in `L`, never in `E`** — the sealed commit stays byte-identical, and `L` is
where the reconciliation with everything main gained since the freeze lives.

**Then the shape splits on what the round owns — not on what it touches:**

1. **A sealing round — a round whose preregistration prospectively owns seal
   state: either it creates new seal and pin state, or it explicitly takes
   ownership of changing existing seal state — takes a pin commit `P`, and `P`
   is mandatory.** `P` writes the round's own **manifest record** —
   `sealed_head` = `E` and `merge` = `L`, under `verification/seals/` — and not
   a legacy constant; see *Sealing through the manifest* at the end of this
   section. (Before `SI-2`'s landing, `P` set the constants it owns to `E` and
   to `L`.) Mandatory
   is not a stylistic preference: in execution mode the guard requires every
   commit of `git rev-list HEAD ^base` to descend from the base, and once `L`
   is on the head, that set reaches the sibling rounds merged into main since
   the freeze, which do not descend from it. Without `P` the guard fails closed
   on the landing and the round cannot land at all. `P` is what moves the guard
   to archive mode, where the landing is certifiable.
2. **A non-sealing round — a round that owns no seal state — takes `L`
   alone.** It **may** modify other contracts inside an existing guard; it
   **may not** alter existing seal constants. It has nothing to pin, and a pin
   commit added there would pin nothing.

That **may** / **may not** pair is worth stating in terms, because the older
guarded/unguarded wording got it wrong by implication:

> **An archive seal belongs to the round that set it, and stays immutable
> afterwards.** A later round does not re-pin it, and does not acquire a pin
> commit merely by touching the guard file that carries it. An existing seal
> constant changes only in a round whose own preregistration says in advance
> that it changes it — and such a round is *sealing*, because it has taken
> ownership of that state prospectively rather than as a side effect of its
> diff.

So the freeze names the shape, and the diff does not. Read the freeze before
building a landing rather than inferring a shape from which files moved.

In **archive mode** the strong ancestry check is re-run against the sealed
object rather than against the current target, the pinned merge's second parent
is required to equal the sealed head, and the pinned merge is required to still
be visible. Visibility asks after the **merge alone**: the second-parent check
has already established that the sealed head is carried by it, so a second
reachability test on the sealed head would be a second escape hatch rather than
a second check, and the sealed head's own reachability is printed as a
diagnostic only. On a push the merge must be reachable from `HEAD`; on a pull
request, from the real `pull_request.head.sha` **or from the current tip of the
base branch**, resolved by name as `refs/remotes/origin/<base ref>`.

The base side is that remote-tracking ref and **nothing else**. It is not
`pull_request.base.sha`, which is no reliable source of the live tip: #644 still
carried base `b78eac870ba3` after the base branch had advanced through three
later landings, with its head pushed to in between. It is also not a local
`refs/heads/<base ref>`, which is whatever an earlier operation left behind
rather than evidence of the remote branch. Under `A.37` an execution branches
from its own control plane's merge and from nothing else, so without the live
base tip every long-lived pull request eventually fails this leg on rounds it
does not touch — a false negative, the leg existing only to catch a landing that
has been rewritten or has vanished. Fail-closed throughout, including when the
remote-tracking ref does not resolve: a shallow or single-branch checkout is a
reason to fetch properly, not to substitute a local branch or the snapshot. A
result note recording that the pins were unset at execution stays true, being a
statement about the execution.

Landing conflicts are resolved **by merits, not by side**. Where an obligation
table or a section collides, take each row or block from whichever branch
actually owns that content: the execution owns the round's own row, and main
owns every row a sibling round has moved since the base. Taking either side
wholesale silently reverts someone else's landing. Verify the resolution
against main afterwards: the landing should add **exactly the execution's own
diff against its own base**, and nothing else. A clean automatic merge is not
evidence of a correct one where both sides touched the same files — compare the
two diffs and account for every difference.

**Full continuous integration must pass again on the final head** — `P` for a
sealing round, `L` for a non-sealing one — before that pull request merges, and
the resulting main build must be green before the next round's landing is
constructed. **One landing at a time, with green main between rounds.**

### Why the execution and the landing share one pull request

What must never change is the sealed commit, and appending to a branch does not
change a commit. `E` stays byte-identical, stays the second parent of `L`,
stays the object the guard re-certifies in archive mode, and stays the
`head_sha` of the certification of record. Every property the chronology
control exists to establish is a property of `E`, and every one of them
survives.

What a separate landing pull request bought was the branch pointer never
moving, which nothing depends on. What it cost was a third review surface, a
second subscription, and an execution pull request left to be auto-closed by
reachability.

Two things still cannot be done. **A pin cannot be folded into the execution
proper**, before certification: it would make the execution's own head depend
on where it landed, which is circular — hence the pin goes on *after* `E` is
fixed, and pins `E` rather than being pinned by it. And **a needed pin cannot
be split into its own pull request after the merge**, which would place main,
between the two merges, in a state the guard rejects. `L` and `P` travelling
together, in that order, on the branch that already holds `E`, avoids both.

### Sealing through the manifest, from `SI-2`'s landing

This subsection governs **rounds begun after `SI-2`'s landing merge**. It
amends the landing shape above prospectively: rounds already landed keep the
chronology their frozen controls state, and nothing here reaches back into
them. It is the protocol `SI2-7` wrote, and the retirement round named below
is the first round that lands under it.

**The seal record is data, not code.** A round's seal state lives in one JSON
record per round under `verification/seals/`, `<STEM>.json`, validated by the
generic validator `SI-2` made authoritative: the discriminated union `SI-1`
built, `kind: "sealed"` carrying `base`, `sealed_head` and `merge`, or
`kind: "base-only"` carrying `base` alone and forbidding the other two, a
forbidden field being a failure even as null. The guard's clause for a round
is a call to that validator keyed on the round's record, and nothing else
gates. Manifest integrity is data-driven: against the record set fixed at a
round's start, a record mutated, removed or added is reported as such, and a
round's only permitted change to the set is the addition its own
preregistration authorizes.

**What a sealing round's `P` writes.** The pin commit `P` writes **the
round's own manifest record**: `verification/seals/<STEM>.json` with
`kind: "sealed"`, `base` = the mandated execution base, `sealed_head` = `E`
and `merge` = `L`. It writes **no legacy constant** — no `_<STEM>_BASE`,
`_<STEM>_SEALED_HEAD` or `_<STEM>_MERGE` in the guard file.

**How a new `sealed` record is created.** While a sealing round executes it
has no record: the state machine classifies it `EXECUTION`, and its guard
certifies chronology against its mandated base through act 10's strengthened
check, the bootstrap form `R7-SI2` itself keeps. At `L` the round is
`LANDED-PENDING-PIN`, and a head descending from that unpinned landing fails
as *seal pending*. `P`, appended on the same pull request after `L`, creates
the record with all three fields; from then on the validator classifies the
round `ARCHIVED`, re-derives `L` from `E` on every run over the union of the
event's visibility targets, and requires the derived landing to equal the
pinned one.

**How a completed non-sealing round's `base-only` record is created.** A
non-sealing round lands `E` → `L` with no `P`, and writes **no record during
its own execution**: a `base-only` record written while the round runs would
classify it `not-applicable` and switch off its own chronology check. Its
record — `kind: "base-only"`, `base` = its mandated base — is created
**afterwards**, as an authorized manifest addition named in the
preregistration of the round that adds it, exactly as `SI2-1` added
`SI1.json` for `SI-1` and as the retirement round adds `SI2.json` for
`SI-2`.

**The legacy constants, in two halves, both of which held until `SI-3`'s
landing.** From `SI-2`'s landing the sixty-one legacy seal-constant
assignments in the guard file **cease to GATE**: no check's verdict depends on
them, they are read only as shadows of the manifest, and a round that writes a
new one has recreated the representation `SI-2` retired. And until the
retirement round they remained **PROTECTED HISTORICAL SEAL STATE**: altering
or removing any of them constitutes taking ownership of existing seal state
under this section, and makes the round that does it *sealing*. The
retirement round, `SI-3`, took that ownership prospectively in its freeze and
removed them; what holds from its landing is stated below.

**The retirement round is sealing.** It follows that the round which deletes
the fifty-nine names and sixty-one statements against `SI-2`'s frozen
inventory, and removes the per-round seal-integrity comparisons the
data-driven rule shadows, is **sealing** under this section, and its `P`
writes its own `sealed` manifest record under this protocol — `sealed_head` =
its `E`, `merge` = its `L` — and writes no legacy constant.

### The representation retired, from `SI-3`'s landing

This subsection governs **rounds begun after `SI-3`'s landing merge**. It is
the protocol `SI3-6` wrote, and it states what the retirement left in force.

**The legacy representation is retired.** From `SI-3`'s landing the guard
file carries **no legacy seal constant** — no module-level `_<STEM>_BASE`,
`_<STEM>_SEALED_HEAD` or `_<STEM>_MERGE` — **no shadow** of a manifest
verdict, and **no per-round seal-integrity comparison**. `SI-3` removed them
against `SI-2`'s frozen inventory plus `SI-2`'s own base constant: sixty-two
statements over sixty names, twenty-three shadows, five comparators. A round
that writes any of them again fails the standing contract `SI-3`'s guard
keeps — **zero legacy assignment statements in the file** — and has
recreated the representation that was retired. Every read of a round's seal
state goes through the **manifest accessor**, one function that returns a
named field of one round's record and fails closed where the record or the
field is missing.

**How a sealing round carries its base while it executes.** It writes no
constant. It declares its mandated execution base, by stem, in the
**prospective declaration** — a stem-free mapping outside the validator's
marker-bounded regions, handed to the validator as its prospective input —
and the validator classifies the round `EXECUTION` against that base through
act 10's strengthened check, and `LANDED-PENDING-PIN` at its landing merge.
**`P` removes the entry when it writes the record**, so that from `P` on the
round is classified from its record alone; a stem that is both declared and
recorded is a failure.

**How manifest integrity is declared.** The data-driven rule holds the
manifest against a **declared baseline**: the seals tree at the current
round's mandated execution base, read from git, plus the additions the
current round's preregistration authorizes, by stem. An authorized addition
is admitted by stem here and validated by content by the validator; anything
else added, and anything mutated or removed, is reported as such and fails.
Each round declares its own baseline; no round's guard hard-codes another's.

**A closed round's contracts are read over the records it manifested.** A
landed round's manifest-cardinality and integrity contracts — its record
count, its authorized-addition set, its census and its probes — are evaluated
over the records that round manifested, and a later round's authorized
additions are outside that historical scope. This is the rule `SI-2`'s
Amendment 1 applied to `SI-1` and `SI-3` applied to both `SI-1` and `SI-2`;
stated here once, it needs no per-round amendment again.

**The censuses are history.** `SI-1`'s and `SI-2`'s `census.json` are
certified historical measurements of those rounds' checkpoints under those
rounds' rules, pinned by their blob identities. Their old side no longer
exists: they are not re-measured, never read as evidence about a later head,
and never the ground of an old/new equivalence claim after retirement.

---

## §A.39 Provisional native V3 rounds

§A.37 remains the default lifecycle for every round, and it governs the round that adopted this
rule, `V3-9`. A round whose preregistration the owner authorizes as a **provisional V3 pilot** runs
instead under the native lifecycle of `verification/infrastructure/v3/architecture.md`, which is
operative for such rounds and no others:

1. **One pull request from `D`.** The round's control plane — its preregistration, carrying one
   `v3-round` block and one `v3-governed-paths` block, and any amendments — is drafted on a single
   pull request from the drafting snapshot `D`. Drafting ends when the owner designates the exact
   commit `F`. No commit after `F` changes the control plane.
2. **Linear execution to `E`.** The execution commits follow `F` linearly. The owner designates the
   certified execution head `E`.
3. **Reconciliation, if needed.** Later history enters the round only through reconciliation
   merges after `E`: first parent a later base on whose first-parent chain `D` lies, second parent
   `E` or the previous receipt commit. The last reconciliation is `Λ`.
4. **The receipt.** `tools/v3_receipt.py` builds the receipt from the round's exact object ids and
   the attestation records the host holds. `Q` is a single-parent child of `Λ` that adds only the
   receipt and, for a sealing round, its seal record. `tools/v3_verifier.py --verify-round Q` must
   print `VERDICT  HOLDS` before the pull request lands.
5. **Landing.** The pull request lands through ordinary review and merge. How it lands is not part
   of the round's validity.

**The check runs at `F` and `E`.** A `check-run` attestation names the commit it was run on. Before
`F` is designated, the pilot's branch is held at exactly `F` and the workflow is dispatched on it
(`workflow_dispatch`); the run whose `head_sha` is `F`, with every job green, is `F`'s `check-run`
attestation, and only then is `F` designated and the branch moved on. `E` is attested the same way
before it is designated. A pull-request run tests a synthetic merge, not `F` or `E`, and is not
recorded as their attestation. These are host attestations, which the receipt records and no
predicate of `tools/v3_verifier.py` reads.

**A halted pilot.** A pilot that halts after `F` instead of reaching a designated `E` follows the
specification's `S12`: it appends the withdrawal commit `W` when execution commits exist, or,
when none exist, the single-parent child of `F` that changes only record paths and carries the
result note; it reconciles as `S9` requires; it builds a halted receipt with
`tools/v3_receipt.py`, which carries `F`'s owner-designation and `check-run` attestations and none
for `E`; `--verify-round Q` must hold; and it lands through the same ordinary pull request.

A provisional pilot carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. It leaves `V1` and `V2` authority unchanged. The guard and the release gate run on
its pull request as on any other, and they remain the repository's authoritative checks until a
later round makes V3 the default.

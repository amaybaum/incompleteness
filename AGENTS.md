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

- Freeze and head movement. A round's freeze is the exact commit `F` the owner
  designates, and the verifier rejects any change to its control-plane files after
  `F` (§A.39). A head that moves after `E` moves by reconciliation: review what
  the reconciliation brings in, and check that the landing adds exactly the
  execution's own changes, each conflict resolved by merits (§A.39).

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
- **§A.40 Where verification runs; CI-first resource discipline.** Run bounded, deterministic
  smoke checks locally before a push: one tool self-test, the V3 verifier's self-test and corpus,
  `legacy_records_check.py`, cheap round controls, and Python compilation/static checks.
  **Classify work by total cost, not the cost of one iteration.** Repeated self-tests, mutation
  campaigns, large enumerations, full probe suites, Lean kernel/Mathlib builds and the release
  gate run in CI; shard independent cases with a matrix where useful. If a local task becomes
  heavy, stop and publish the partial state and proposed CI plan instead of running for hours.
  The exact-head host runs dispatched on exactly `F` and `E` are the `check-run` attestations
  a receipt records: verification evidence, not protocol validity, which remains
  `tools/v3_verifier.py --verify-round Q` printing `VERDICT  HOLDS` (§A.39). A local run is
  evidence for the executor and is never recorded as a `check-run` attestation. Any special
  dispatch or launch still requires owner approval (§A.43).
  **Evidence-retention batteries run in CI.** The checks and self-tests of
  `verification/audits/evidence-retention/` (`check_retention.py`, its `--gate`,
  `check_objects.py`) and mutation campaigns against them run through the dispatch-only
  `retention-tests` workflow, as parallel jobs on a pushed branch head; mutants run only after
  every unmodified check has passed. Dispatching that workflow on a branch other than `main`,
  within its own limits (its fixed checks and at most 20 mutants), is routine verification and
  needs no separate owner approval; every other dispatch remains under §A.43 item 4. Its runs are
  evidence for the executor, never `check-run` attestations. Locally, run only the one smoke
  check that guards a push.
  **Keep local checkouts small.** Prefer repository APIs and reuse of an existing worktree,
  sparse checkout or partial clone over repeated full clones and duplicate object stores.
  Full-history gates and isolated, no-alternates recovery tests belong in CI with the complete
  required objects; a shallow or shared-store test is not equivalent. Never delete unapproved
  evidence to make room. RAM-backed scratch is disposable: preserve substantive work and review
  evidence durably before it can be lost.
  **Disk thresholds.** Measure free space on the filesystem that holds session and agent
  transcripts before starting an agent or allocating a checkout. Below 500 MB free, start no
  additional agents; below 250 MB free, suspend nonessential work and preserve its progress.
  Measure actual consumption and apply stricter limits when it warrants them.
  **Shared object stores.** A store that other clones borrow objects from (`--shared`,
  alternates, linked worktrees) has a named owner and a recorded list of its dependents. While
  any dependent exists, nobody, its owner included, deletes, replaces, reinitializes, prunes or
  garbage-collects it; it is retired only by coordinated retirement, after every dependent has
  been made independent or itself retired. Prefer independently recoverable clones that can
  refetch every object from the GitHub repository whenever practical.
- **§A.41 Every stated invariant is measured.** A preregistration carries an invariant→checkpoint
  table: every property it asserts of its execution names the checkpoint that measures it, and an
  invariant with no checkpoint is either given one or not asserted. A named hazard whose mitigation
  is cheap carries the mitigation as a frozen precondition or checkpoint; naming it is not enough.

- **§A.43 Issues for planning; draft PRs for active work.** Unstarted and inactive plans
  belong in open Issues; active research, implementations and native V3 rounds have one
  guiding draft PR with continuously pushed safe checkpoints. Migrate planning-only PRs
  to cross-linked Issues and close without merge or branch deletion. The §A.39 pre-F
  control-plane chain, candidate-F/E holds and separate launch approvals remain intact.

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
  otherwise. Hence §A.39's exact-head rule — a pull-request run tests a synthetic merge, so check
  the exact-head run before calling a red badge a research failure, and never cure it by merging
  main into a certified execution.
- A landing's obligation table collided on four rows at once, three of which a sibling round had
  moved since the base; taking either side wholesale would have silently reverted a label merged
  twenty minutes earlier. Hence §A.39's resolve-by-merits rule and its check that a landing adds
  exactly the execution's own diff.
- The Act 21 control plane used one name, `B`, for its drafting snapshot and for the execution
  base its chronology control defined; after the merge two of its mechanical preconditions could
  not hold at the real base, one naming the drafting SHA as `B` and one requiring a token absent
  from a tree that now contained the preregistration carrying it. Caught in owner review and
  corrected by append-only amendment. Hence the `D` / `B` / `M` vocabulary §A.37 records; a
  native round has no mandated base, its execution anchored at the designated commit `F`.
- A retirement round's transformation reproduced its frozen output byte for byte and passed every
  local check, while deleting ten statements of the code it retained: six of them control flow,
  one a flag set late in a loop and read by the loop's condition, and three loops that changed a
  copied registry through their loop variable. Only running the output in CI exposed them, the last
  three in the successor round's run before its freeze. Reproducing a frozen blob shows the plan
  was executed faithfully, not that the plan was valid. Hence §A.39's rule for destructive
  transformations and §A.41.

- An audit of `main` found frozen records citing design trees on disposable branches, CI logs that
  expire, and four logs held only in a session scratchpad. Pinning such content by SHA had been
  treated as retaining it. Hence §A.42: evidence for an enduring claim is retained on `main`, with a
  manifest for records already frozen.
- One agent deleted and reinitialized a shared base clone in RAM scratch while six other
  agents' clones borrowed objects from it. Five lost the objects their trees referenced mid-task,
  and every result read from them after the deletion was void until each clone was repaired and
  the checks re-run; a successful refetch alone did not revalidate earlier results. Hence §A.40's
  shared-object-store rule: no deletion, replacement, reinitialization, prune or garbage
  collection while dependents exist, with a named owner, tracked dependents and coordinated
  retirement.
- A preservation plan once proposed archiving every historical run head in an inventory and
  extracting every expiring log, because their refs and logs were at risk. It did so before asking
  which surviving claims needed them. Hence §A.42 item 8: retention follows necessity, not
  exposure.

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

## §A.37 Round lifecycle before V3 (record)

This section is a record. It governs no new round and provides for none: every round begun after
`V3-11`'s landing runs under §A.39. It keeps what is needed to read the records of the rounds that
landed before V3, each of which keeps the protocol under which it landed. The full text of this
section as it governed those rounds is `AGENTS.md` at `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`,
and each round's own frozen chronology control states its shape in terms; a preregistration is not
reinterpreted after its outcome is known.

### How those rounds ran

The earliest rounds ran in three pull requests: a control plane carrying the preregistration
alone, an execution, and a separate landing. From this section's adoption they ran in two: the
control plane, then one execution pull request that, once its head was certified, carried the
landing as well. The control plane was reviewed, amended before its merge and only then, and
merged before any execution object existed; merged, it was immutable, and an execution that
diverged from it recorded the discrepancy rather than repairing the freeze. Its merge commit was
the mandated execution base, from which the execution branched and from nothing else.

Before certification an execution never absorbed later main: no merge from main, no rebase, no
amend, no force-push. Certification fixed the sealed execution commit, which never changed. The
landing merge took current green main as first parent and exactly that commit as second, with
conflicts resolved in the landing and never in the sealed commit. A **sealing** round, one whose
preregistration prospectively owned seal state, then took a pin commit that recorded its sealed
head and landing merge; a **non-sealing** round took the landing alone. Freezes written before
that wording say **guarded** and **unguarded** for the same distinction, and keep the meaning
their own chronology controls fix.

### The vocabulary of their records

- `D` — the drafting snapshot: the commit against which a control plane was written and its
  drafting-time measurements taken. Never the mandated execution base merely because the control
  plane was drafted from it.
- `B` — the mandated execution base: the certified merge commit on `main` of the latest
  control-plane artifact governing the round, the preregistration or its latest
  execution-affecting append-only amendment.
- `M` — a candidate control-plane merge, built by continuous integration to test `B`-scoped
  conditions before `B` existed; predictive test state only.
- `E` — the sealed execution commit, certified at its exact head.
- `L` — the landing merge, first parent main and second parent `E`.
- `P` — a sealing round's pin commit, after `L`.
- **execution mode** and **archive mode** — the guard's two ancestry checks for a sealing round:
  against its base while it executed, and, once pinned, against the sealed object, whose pinned
  merge's second parent had to equal the sealed head.
- **seal records** — from `SI-2`'s landing, one JSON record per round under
  `verification/seals/`: `kind: "sealed"` with `base`, `sealed_head` and `merge`, or
  `kind: "base-only"` with `base` alone. Before `SI-2` the same state was legacy constants in the
  guard file, which `SI-3` removed.
- **`control-plane-preconditions` blocks** — rows scoped at `D`, at `B` or from `D` to `B`,
  which a control plane could carry for mechanical checking.

### Their records now

The records of those rounds — their preregistrations, amendments, result notes, seal records under
`verification/seals/` and `V2` certificates under `verification/certificates/` — are listed with
their blobs in `verification/infrastructure/legacy-records.json`, and the release gate's
`legacy-records` step keeps every one unchanged and admits no new file under a closed namespace
(§A.39). The mechanisms that checked their chronology at every later head — the guard's ancestry
and seal clauses, the control-plane base check and lint, and the `V2` certificate verifier — were
retired by round `V3-14`, whose preregistration lists what each checked and what now protects it.

A question one of those rounds left open, or froze and never executed, is taken up by a new native
round, which cites the old freeze as provenance and leaves the old record as it stands.

---

## §A.39 Native V3 rounds

From `V3-11`'s landing every new round runs under the native lifecycle of
`verification/infrastructure/v3/architecture.md`. `V3-9`, which adopted this section, ran under
§A.37; `V3-10` and `V3-11` ran under it as provisional pilots. Each round keeps the protocol under
which it landed:

1. **One pull request from `D`.** The round's control plane — its preregistration, carrying one
   `v3-round` block and one `v3-governed-paths` block, and any amendments — is drafted on a single
   pull request from the drafting snapshot `D`. Drafting ends when the owner designates the exact
   commit `F`. No commit after `F` changes the control plane.
2. **Linear execution to `E`.** The execution commits follow `F` linearly. The owner designates the
   certified execution head `E`.
3. **Reconciliation, if needed.** Later history enters the round only through reconciliation
   merges after `E`: first parent a later base on whose first-parent chain `D` lies, second parent
   `E` or the previous receipt commit. The last reconciliation is `Λ`. Conflicts are resolved in the
   reconciliation, never in `E`, and **by merits, not by side**: each row or block is taken from
   the branch that owns it, the round's own from `E` and every row a later round has moved from
   the base. A clean automatic merge is not evidence of a correct one where both sides touched the
   same files; compare the landing with the execution's own diff and account for every difference.
4. **The receipt.** `tools/v3_receipt.py` builds the receipt from the round's exact object ids and
   the attestation records the host holds. `Q` is a single-parent child of `Λ` that adds only the
   receipt and, for a sealing round, its seal record. `tools/v3_verifier.py --verify-round Q` must
   print `VERDICT  HOLDS` before the pull request lands.
5. **Landing.** The pull request lands through ordinary review and merge. How it lands is not part
   of the round's validity.

**The check runs at `F` and `E`.** A `check-run` attestation names the commit it was run on. Before
`F` is designated, the round's branch is held at exactly `F` and the workflow is dispatched on it
(`workflow_dispatch`); the run whose `head_sha` is `F`, with every job green, is `F`'s `check-run`
attestation, and only then is `F` designated and the branch moved on. `E` is attested the same way
before it is designated. A pull-request run tests a synthetic merge, not `F` or `E`, and is not
recorded as their attestation. These are host attestations, which the receipt records and no
predicate of `tools/v3_verifier.py` reads. So a red pull-request badge on a round held at `F` or `E`
is diagnosed against the exact-head run first; it is never cured by merging main into the round
before `E`.

**A halted round.** A round that halts after `F` instead of reaching a designated `E` follows the
specification's `S12`: it appends the withdrawal commit `W` when execution commits exist, or,
when none exist, the single-parent child of `F` that changes only record paths and carries the
result note; it reconciles as `S9` requires; it builds a halted receipt with
`tools/v3_receipt.py`, which carries `F`'s owner-designation and `check-run` attestations and none
for `E`; `--verify-round Q` must hold; and it lands through the same ordinary pull request.

**Authority.** A native round is protocol-valid exactly when `tools/v3_verifier.py --verify-round Q`
prints `VERDICT  HOLDS` on its receipt commit `Q`. The release gate's `v3-receipts` step runs
`tools/v3_verifier.py --receipts` at the commit under check: it verifies every receipt in the tree
from the commit that last wrote it and fails on any that does not hold, so the required
`Mathlib bridge` check carries the V3 verdict. The host attestations a receipt records, the owner's
designations and the check runs, are outside the verifier's semantics: no predicate reads them.

A native round carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. The guard (`V1`) keeps running on its pull request as on any other and still
fails the release gate on a failed check, but it checks content — kernel modules, manuscripts and
notes — and never a round's chronology; it does not decide whether a native round is
protocol-valid.

**Two immutabilities, kept apart.** They protect different populations by different mechanisms, and
neither stands in for the other:

- **Native rounds' records** — each round's record directory and seal record — are kept by
  `tools/v3_verifier.py --receipts` (the specification's `G13`): once a round's receipt holds, its
  record directory and seal record at every later commit must be exactly those at its receipt
  commit. A correction is made by a new native round in its own record.
- **The records of the rounds landed before V3** are kept by the release gate's `legacy-records`
  step, `tools/legacy_records_check.py`: every record listed in
  `verification/infrastructure/legacy-records.json` keeps its blob, and no file is added under a
  closed namespace. The manifest changes only as the governed work of a native round whose receipt
  holds and whose governed paths name the manifest: a migration, a repair or a change to the
  population is a native round, and a commit that changes a record and the manifest together
  fails.

**Destructive transformations.** A mechanically destructive round states separately whether it
retires authority, reachability and physical presence. Every physical edit is frozen explicitly;
no deletion is authorized solely because an algorithm inferred the deleted code to be dead.
Preservation is checked independently, mutation-tested in both directions, and the exact generated
executable tree is exercised in CI before freeze. Beside the transformation, the freeze therefore
carries:

- **the edit ledger** — every change as a splice of the base: its span, the hash of the old text,
  the new text and its hash, and the reason for it. The ledger is the authorization; nothing
  outside it may change. An algorithm that finds dead code is a discovery mechanism: a deletion it
  proposes exists only as its own entry in the frozen ledger;
- **a preservation checker independent of the transformation** — it imports nothing from it,
  rebuilds the expected output from the base and the ledger alone and compares bytes, and checks
  what is retained structurally: retained functions untouched, control flow removed only with its
  governing block, nothing removed from a surviving block but what the round retires, no in-place
  change removed from an object, or an alias of one, that surviving code reads, and no binding
  removed that surviving code still resolves to. Deleting or rewriting retained code must fail it,
  and so must restoring retired code;
- **the execution evidence** — the workflow run, on a disposable branch, on exactly the predicted
  execution tree less the result note, and in every event mode used to certify `E`. The runs are
  design evidence recorded in the preregistration, not `check-run` attestations.

---

## §A.42 Durable evidence and self-contained verification

Every enduring research result, certification claim or governed decision rests on evidence an
independent reviewer can reproduce from `main`: the commit the claim is about, the result it
expects, and the recipe that regenerates that result, with the regeneration compared to the
expectation as item 7 states. A log records one observation of a result; a rebuild tests the
claim. Scratchpads, `/tmp`, local worktrees, disposable and research branches, external CI logs,
host comments and reviews, and commits not reachable from `main` are working material and
provenance. None of them is the sole source of an enduring claim, and an object id or digest that
names such content neither retains nor establishes it.

1. **What is retained, and in what form.** For every computational claim a record relies on — a
   verdict, a check run, an axiom report, a measured hazard, a design result — the expected
   result, as a small structured file: the deterministic outputs the claim rests on (for a
   bridge build: build success, the release gate's steps and verdict, each governed module's
   `#print axioms` reports, and the failure markers), and nothing that varies between runs
   (timestamps, durations, cache behaviour, output order).
   - Each expected result names the commit it holds at, the recipe that regenerates it, and its
     provenance: the run, job and the digest of the text it was read from. The digest is
     provenance of the extraction, not independent proof.
   - Its form is stated: **complete** (a file of the record's own), **derived** (read from a
     named source, with that source's digest), or **complete-as-cited** (byte-identical to an
     artifact a frozen record names by digest).
   - A raw log or transcript is not committed as evidence. The one exception is an artifact a
     frozen record pins by digest, whose line positions and digest that record asserts: it is
     kept byte for byte, labelled as such, and its substantive claims are recorded as an expected
     result as well.
   - §A.28 bounds the amount; it does not send such evidence to the off-repo log.
2. **When.** Before the citing record lands.
   - **A native round's design evidence, drafting-time measurements and `F`'s exact-head run**
     are committed to its record directory, outside `amendments/`, by its first execution
     commit. In a halted round without one, the commit in `W`'s place carries them.
     - The preregistration pins the pre-`F` items by hash.
     - Drafting commits change only control-plane files (`S2`).
   - **`E`'s exact-head run cannot be carried by any later commit of the round** (`S9`
     condition 2, `S10`).
     - An evidence-retention commit, landed on `main` through its own pull request, adds it
       under the record directory, outside its control-plane files.
     - The round's reconciliation takes a base containing that commit.
     - The receipt's candidate entry for `E` names each retained file's digest.
     - Nothing writes to the record directory after `Q` is built. A later write fails `G13` at
       the landing, and the round builds again (`S10`).
3. **Where.**
   - For a round before its receipt commit: its record directory.
   - For an audit: its own directory.
   - For a paper: beside its code and data, never as a `.md` under `papers/`.
   - For frozen records: `verification/audits/evidence-retention/`, whose manifest maps each
     citing `file:line` to its retained copy and states which claims made there the copy carries.
4. **Forward only.**
   - A frozen record is never edited to point at retained evidence. That covers a native
     round's record under `G13`, a receipt, and a legacy record. The archive's manifest maps
     frozen records only.
   - A mutable file citing such content is corrected in place to cite the retained copy
     (§A.27, §A.30).
   - Retention never strengthens a claim, never repairs a failed check by changing its evidence,
     and never presents a re-cut or redacted copy as the original. A copy that is not
     byte-identical to its cited digest carries its own digest and says so.
   - Evidence that cannot be recovered is recorded as missing. A claim resting only on missing
     evidence is corrected in its mutable dependents (§A.30), and in a frozen record only by a
     new native round (`G13`).
5. **Public repository.**
   - Before a log is committed, it is scanned for secrets and sensitive operational data:
     tokens, keys, signed URLs, IP and e-mail addresses.
   - A redaction is recorded, with what was removed and where, and the redacted copy gets its own
     digest.
6. **V3 host attestations.** §A.42 adds retention, not verification.
   - Receipts record host attestations as §A.39 and the specification define them, and
     `tools/v3_verifier.py`'s verdict is unchanged: no predicate reads them.
   - A retained copy is evidence of an attestation, not the attestation (`S5`). The receipt's
     `record` still names the host object, and no retained or local output is recorded as a
     `check-run` attestation (§A.40).
   - From the attested host run itself, whatever the round's records cite is retained, including
     the job conclusions, the release-gate block and the cited axiom reports.
   - An owner designation is retained as its text, its author and its time.
7. **Checking and reproduction.**
   - `verification/audits/evidence-retention/check_retention.py` verifies the archive from the
     repository tree alone:
     - archived bytes match their hashes;
     - every mapped citation still reads as recorded, in a file whose blob id is unchanged;
     - every recorded claim stands verbatim in its citing file and names the retained files that
       carry it, so a reviewer can read those files to check it;
     - every expected result is well formed and names its commit, job and recipe;
     - the manifest's gaps and the claims no retained file carries are printed.
   - As the release gate's `evidence-retention` step it also runs in history mode, reading git:
     - R9's scope is the receipts and certificate attestations at the archive's base;
     - R10 checks that the base is an ancestor and that no path named as later existed there;
     - R11 re-derives the module table of each expected result whose run a receipt or
       certificate attestation at the base names: from the attesting rounds'
       `v3-governed-paths` blocks, read at the run's commit at the blobs and digest the receipts
       pin, or, for CV-1's runs, which no such block governs, from the contributions of
       `verification/certificates/CV1.json` at the blob its attestation pins. The runs it checks
       must be exactly the runs those attestations name. R11 is a consistency check: it shows the
       archive applied those blocks faithfully, not that they name the right modules.
   - `verification/audits/evidence-retention/reproduce.py`, run by the `reproduce evidence`
     workflow, regenerates an expected result at its commit and compares it with
     `compare_result.py`, which fails closed: a missing report, an unexpected axiom, an absent
     gate step, an extraction failure or any mismatch fails it. The verifier is the checkout
     the workflow runs on; the historical commit supplies only its sources and its own gate.
     It writes `verdict.json` on every exit once its work directory is writable, an exception
     included, and the verdict holds only on a clean exit.
   - For a round, each hash pin of item 2 is a row of its invariant→checkpoint table (§A.41).
8. **Necessity, not exposure.** Retention serves surviving claims, not the history of the work.
   Items 1–6 state what must be retained. This item limits retention beyond them; it never waives
   any of it, and it governs only what is newly retained. Beyond items 1–6, content is retained
   only when both of the following hold, and only the smallest set that meets them is retained:
   - a claim depends on it, where the claim has landed on `main`, is frozen in a governed
     record, or belongs to a native round between the designation of its `F` and the landing of
     its receipt; and
   - it has not been shown redundant.

   Further:
   - Imminent loss is not a reason to retain. That covers an expiring log, a ref that may be
     deleted, and a commit reachable only from a temporary branch. Membership in a run inventory
     or a list of historical heads is not a reason either, and a temporary branch has no value of
     its own.
   - Superseded experiments, exploratory runs and failed runs used only for debugging are not
     retained unless a surviving claim cites them. A failed run that a conclusion explicitly rests
     on is evidence like any other.
   - Before any bulk retention, log extraction or batch of protective refs, a necessity audit
     classifies each candidate:
     - **required**, **redundant** (regenerated and matched, as below), **optional** (useful, but
       no surviving claim needs it; not retained) or **undetermined**;
     - naming the claim it serves (`file:line`) for a required or redundant item, and how
       reconstruction was checked.
   - An item is redundant only when it has actually been regenerated and compared with the
     original:
     - regenerated from `main` or from content already retained;
     - compared byte-identical, or, for a candidate expected result not yet retained, identical
       under `compare_result.py`;
     - with the recipe, the commit and the comparison recorded in the audit.

     A similar source file, an unrun recipe or a repeatable experiment does not make an item
     redundant. An item whose original is no longer available for comparison is undetermined.
     An expected result of item 1 is never redundant: regenerating it is item 7's check against
     it, not a substitute for it.
   - A later run does not reconstruct a specific run, even a green run at the same commit.
     Evidence of an `F` or `E` `check-run` attestation, or of any run a record cites, is never
     redundant while the citing claim stands.
   - Only required items are retained. An undetermined item is investigated and resolved before
     it is retained. Nothing that holds it is deleted or released until then. CI time spent
     extracting historical evidence meets the same test.
   - A temporary protective ref is not retention; it holds an object while the audit decides.
     - This item never authorizes deleting a ref, branch, archive entry, retained file or record,
       and it does not affect §A.26 quarantine.
     - Any such removal needs the owner's separate authorization (§A.43 items 3–4).
     - Retained and frozen content stays forward-only (item 4, §A.39).
     - A ref that §A.43 requires is not a protective ref and needs no audit.

Enforcement:
- `check_retention.py` and its self-test run locally before any push that touches the archive
  (§A.40).
- The release gate's `evidence-retention` step runs it in history mode. That mode reads from git
  the receipts and certificate attestations at the archive's base, requires each to be covered,
  and treats a receipt landed after the base as outside the archive's scope. It also runs R10
  and R11 (item 7), and `check_objects.py --reconstitute` and `--self-test` on the retained
  off-main objects under `objects/`.
- Reviewers check that `E`'s evidence reached `main` through its own pull request before the
  round's reconciliation.
- Reviewers check that each hash pin of item 2 resolves to retained content.

Adopted 2026-10-16, after an audit of `main` at `fc5abade` found:
- 107 commits and 75 objects not reachable from `main`, cited in frozen records and, once, in a
  mutable script;
- 842 citations of CI runs and jobs, whose logs expire;
- four cited logs held only in a session scratchpad.

Rounds landed, or frozen at `F`, before this section keep their records unchanged. Their evidence
is retained by the archive under 3, or listed there as not yet retained.

---

## §A.43 Issues for plans; PR-first publication for active work

**Planning-only, inactive and not-yet-started threads use open GitHub Issues**, not
placeholder pull requests. An Issue states the question, scope, next action, dependencies
and activation condition; it is not evidence or a governed native-round control plane.
**Active research, formalization, native V3 round drafting, audits, extractors and repairs
use one guiding draft pull request**, opened after the first scoped active commit.
A research-only thread currently producing or independently reviewing substantive
calculations is active even if no result is adopted or merge is planned; historical
results on a paused thread do not alone keep its PR active. The PR tracks pushed work in progress; a
local checkout, agent scratchpad or private worktree is not the authoritative tracker.
Reuse a thread's guiding PR; reviewers and checkpoints do not each need separate PRs.
A draft PR is neither approval nor certification nor the durable evidence on `main`
required by §A.42.

1. **Make the work visible at the right stage.** Open an Issue for a proposal or backlog
   item. When substantive work starts, open or reuse its guiding draft PR after the first
   scoped active commit and link Issue ↔ PR, before extended work or independent review.
   Identify the objective, base or drafting snapshot `D`, authority limits, dependencies
   and next check. For native rounds, opening and drafting the control plane from `D`
   is already active work requiring the §A.39 one-PR-from-`D` lifecycle; an Issue cannot
   replace that PR. Before `F`, the round PR branch may receive only single-parent commits
   changing that round's permitted preregistration/control-plane files. Every other
   checkpoint must go to a linked research or staging branch; push its safe commits and
   link their exact SHAs from the guiding PR. Do not leave substantive work only locally.
2. **Publish checkpoints continuously.** Run the applicable cheap local checks (§A.40),
   then commit and push each meaningful milestone promptly to its workstream branch,
   rather than holding it until independent review, F designation or merge approval.
   Incomplete or failing work may be published as clearly labelled `WIP / UNVERIFIED`,
   with the failing checks and limitations stated. Keep the guiding PR's head, description
   and checkpoint comments aligned with the actual current work and its exact SHAs.
   Reviewers inspect pushed immutable SHAs and record verdicts and outstanding findings
   on the guiding PR. A reviewer's local-only results are not a substitute for a pushed
   author checkpoint.
3. **Keep history and freezes intact.** Do not silently amend, force-push away or delete
   prior reviewed candidates or evidence. If the next candidate must be re-cut from an
   incompatible `D`, preserve the old head under a named remote ref before a separately
   authorized, lease-checked head update, or open a linked successor draft PR; any
   re-cut must still satisfy §A.39's single-parent, control-plane-only path from `D`.
   From the start of a candidate `F` or `E` exact-head hold until owner designation or
   explicit release of that hold, the round's branch must not move. After `F` is
   designated, §A.39's linear `F`→`E` execution and reconciliation rules govern it.
4. **Do not confuse publication with authorization.** A normal WIP branch push or draft
   PR update is allowed by default. It does **not** authorize `workflow_dispatch`, a
   special workflow launch, F/E designation, acceptance, merge to `main`, destructive
   ref movement, branch deletion or evidence-retention promotion. Before pushing, inspect
   all `push`-triggered workflows, including path-filtered workflows whose triggers depend
   on the diff or branch history (especially a non-fast-forward update). A push to a
   special trigger branch that starts a governed launch is itself a launch and still
   needs separate owner authorization. Ordinary automatic draft-PR CI is not an
   exact-head F/E attestation (§A.39, §A.40).
5. **Exceptions are narrow and explicit.** An owner-imposed hold on pushing must name
   its affected ref or artifact, reason and release condition and be recorded on the
   guiding PR where safe. Never infer a blanket `no push` rule from `no merge`,
   `no dispatch`, `no F/E designation`, or a hold on a special launch branch. §A.28's
   permanent-repository burden remains decisive for what lands on `main`; the following
   public-branch exclusions apply to *every* push, including WIP. Do not publish secrets,
   unredacted sensitive logs, prohibited artifacts or bulky temporary repositories;
   follow §A.28 and §A.42 and publish safe source, structured evidence, digests and
   traceable omission notes instead.
6. **Retire inactive planning PRs without losing work.** When a PR is only a plan or
   backlog placeholder, first open an Issue carrying its open work, decisions and links
   to the original PR, branch, immutable commit SHAs and source/evidence paths. Cross-link
   the Issue from the PR and close that PR **without merging**; preserve its branch,
   commits, discussion and research artifacts. Do not delete refs, rewrite evidence or
   imply that unlanded claims are adopted. Link any subsequent active draft PR to the
   Issue, checking its actual base and existing evidence anew. A PR merely waiting for
   CI, review or a governed authorization is still an active PR, not a planning-only PR;
   do not close it to satisfy a count. A native V3 round with no designated `F` may be
   retired to an Issue only after any candidate-`F` exact-head hold is explicitly
   released; resumption requires a new guiding PR from a current `D`, citing the closed
   PR's control plane and immutable commits as provenance. Native V3 rounds otherwise
   retain §A.39's protocol throughout.

# Reconstruction round BG-3 — the scope-transfer module after the premise refutation: PREREGISTRATION (draft)

**Status: drafting, native V3; not a candidate `F`.** Drafted on a pull request from `D`. The owner decisions are
recorded below, including the scope reduction made after the first design run (*Design evidence*). The reduced
predicted execution tree — `D`, this control plane, `controls.py`, the edit ledger and the two governed files, less the
result note — is to be tested on a fresh disposable branch; the blobs below are predicted and become frozen only with
that evidence. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a
designation.

```v3-round
round BG-3
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/
record AM verification/receipts/BG-3.json
execution M verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean
execution M verification/ROADMAP.md
```

D: e3ad5d7a71910ce5413ef6dacd25bf5a63d5a1e0. It is `main` after #826, and its push run 38800143579 concluded `success`.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, other landed module, census entry, probe, workflow, coverage-ledger entry, BG-2 record or file of the design
package changes under any outcome**, and no statement of a landed declaration changes.
`CongruentReconstruction.lean` is among the unchanged modules.

## What the round is

**Provenance.** BG-2 (landed by #826; receipt `verification/receipts/BG-2.json`) certifies
`OIBridge.PremiseOrientation.not_BGIntegerClassification` and its controls, and changes no landed module. Its owner
decisions (`round-bg-2-premise-orientation/preregistration.md:292–307`) make the correction of
`TurnpikeScopeTransfer.lean` a separate governed round: the docstring that calls the refuted premise "the ONLY
unproved input", and moving into the module the reduction that the design package's `SignedRepairDesign.lean`
factors as `real_to_integer_surrogate`. ROADMAP.md:1143 tracks both under P2. This round is that correction. It
adopts no sign-aware classification and replaces no design-package citation; both are separate.

**The defect, at `D`.** `TurnpikeScopeTransfer.lean` describes the refuted proposition as the published
classification and as established input:
- the title (:2–4) gives the two-branch theorem "the INTEGER Bekir–Golomb classification as its only unproved
  premise";
- the header (:6–14) says Bekir–Golomb "is then consumed in the integer scope its text unambiguously uses, and the
  real classification is derived, not assumed";
- the header (:30–41) says `BGIntegerClassification` "states the external premise — the 2007 classification for
  INTEGER spanning rulers";
- the definition's docstring (:535–541) is headed "THE EXTERNAL INTEGER PREMISE — Bekir–Golomb 2007, in the spectral
  form this repository consumes" and ends "This `Prop` is the ONLY unproved input of the reconstruction programme";
- `spectral_classification_of_BG` (:555) is headed "THE REAL SPECTRAL CLASSIFICATION, derived";
- `twoBranch_of_BGClassification` (:820–822) is headed "CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE" and calls
  its premise "the INTEGER Bekir–Golomb classification".

The statements are correct as implications; the docstrings are not. `spectral_classification_of_BG`'s proof
(:573–751) also carries inline the real-to-integer reduction that the design package states once.

**The same omission in `CongruentReconstruction.lean`, deferred.** A corpus sweep for the defect's phrasing (§A.25,
§A.19) finds it in the module whose theorem `TurnpikeScopeTransfer` feeds. `twoBranch_of_spectral_classification`
takes a three-way hypothesis `hclass` about the given pair — translation-congruent, reflection-congruent, or `mu` in
one orientation. The theorem is a valid conditional. Its docstrings (:2–3, :24–30, :709–712, :749–751) say `hclass` is
what the Piccard/Bekir–Golomb turnpike classification supplies. That derivation is not established: the non-congruent
pair (0,1,4,10,12,17), (0,4,6,9,16,17) realizes `mu` reversed and in no relabeling in the orientation `hclass` lists
(`not_muForm_r1_r2refl`, `revMuForm_r1_r2refl`), so a derivation of `hclass` from a classification of rulers must also
exclude the reversed branch. BG-2's pair contradicts a formal premise; it says nothing against the published
classification or a physical reconstruction theorem.

Correcting those four docstrings changes the compiled module, and 188 of the library's 223 OIBridge modules import
it. The first design run measured the cost (*Design evidence*): a 57-minute rebuild whose output put this round's
axiom reports outside the log window the executor reads. So this round leaves `CongruentReconstruction.lean`
unchanged, and its correction is a separate round, tracked in the ROADMAP paragraph this round applies. Nothing BG-3
writes repeats or endorses the docstrings' claim.

**Assumption-watch marker.** A docstring that names a hypothesis's source ("what the classification supplies") is a
claim about a second proposition, and a refutation of that proposition reaches the docstring even when the theorem
statement is unaffected.

## The edits

Every change is a splice of `D`'s text. The **edit ledger** `edit-ledger.json` records, for each governed file, its
sha256 at `D`, its sha256 after the round, and each splice: a 1-based line span of `D`'s text, the sha256 of the old
text, the new text and its sha256, and a reason. It is the authorization: nothing outside it changes in the two
files. It is a record artifact of this round, committed at stage 1 beside `controls.py`, and is pinned twice: its blob
is frozen below, and `controls.py` carries its sha256 (`LEDGER_SHA256`). `controls.py` rebuilds each file from `D`'s
blob and the ledger alone.

| file | span at `D` | change |
| --- | --- | --- |
| `TurnpikeScopeTransfer.lean` | :2–4 | title: the transfer, and the classification and two-branch theorem as implications from the refuted premise |
| | :6–14 | why the file exists: the integer-presented model and the real spectra, without identifying the premise with the paper |
| | :30–41 | the reduction lemma; the premise, its refutation and its two consumers as implications |
| | before :532 | `real_to_integer_surrogate`, statement and proof byte-identical to `SignedRepairDesign.lean` at `D`, with its own docstring |
| | :532 | section title |
| | :535–541 | the definition's docstring: the unsigned premise in μ-form, false, refuted at the named pair |
| | :555–562 | `spectral_classification_of_BG`'s docstring: an implication, through the reduction |
| | :573–751 | `spectral_classification_of_BG`'s proof: the design package's `example` proof, applying the lemma |
| | :820–825 | `twoBranch_of_BGClassification`'s docstring: an implication; GR §3.3 assumes the sign-aware H-BG |
| | before :851 | `#print axioms real_to_integer_surrogate` |
| `verification/ROADMAP.md` | :1143 | the kernel-side items: the docstrings record the refutation, the reduction is adopted, and the `CongruentReconstruction.lean` correction is a separate round |

**What stays.** Every declaration of the module keeps its name and its statement byte for byte; the only added
declaration is `real_to_integer_surrogate`. `BGIntegerClassification`, `AscPair` and the two consumers keep their
names, as `TurnpikePremiseOrientation.lean`, the R7 lint of `edge_rigidity_probe.py` (:365–369) and the manuscript
and ledger sites cite them. The probe's lint list does not gain the lemma. `CongruentReconstruction.lean` is unchanged.

The added statement:

```lean
theorem real_to_integer_surrogate {n : ℕ} (E E' : Fin n → ℝ)
    (hgapE : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapE' : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hsets : Finset.image (fun q : Fin n × Fin n => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin n × Fin n => E' q.2 - E' q.1) Finset.univ) :
    (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
    ∨ (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀)
    ∨ ∃ (σ σ' : Equiv.Perm (Fin n)) (F F' : Fin n → ℤ),
        StrictMono F ∧ StrictMono F' ∧
        (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d) ∧
        (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d) ∧
        (Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
          = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ) ∧
        (¬ ∃ c : ℤ, ∀ i, F' i = F i + c) ∧
        (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) ∧
        (∀ a b c d : Fin n, a ≠ b → F' d - F' c = F b - F a →
          (E' ∘ σ') d - (E' ∘ σ') c = (E ∘ σ) b - (E ∘ σ) a)
```

It assumes no classification. The design package compiled it in the namespace `OIBridge.ScopeTransferSigned` (run
38534906783), with no print of its own; `spectral_classification_of_BGSigned`, which applies it, reports only the three
standard axioms (`axiom-reports.txt`). Here it joins `OIBridge.ScopeTransfer` with its own print.

## The decision rules

Four cells, each read by its own rule from measurements at `E`; none reads another's outcome.

- **Q-RED.** `BG-3-REDUCTION-FACTORED` iff `real_to_integer_surrogate` at `E`, statement and proof, is byte-identical
  to the design package's at `D`; `spectral_classification_of_BG`'s proof applies it and not
  `integer_realization_of_real_realization`; that transfer is applied exactly once in the module's code, inside the
  lemma; and the ledger at `E` is the frozen one. Otherwise `BG-3-REDUCTION-NOT-FACTORED`.
- **Q-PRES.** `BG-3-STATEMENTS-PRESERVED` iff every declaration of the module at `D` has a byte-identical statement at
  `E` (a definition's whole body); `E` declares `D`'s names and `real_to_integer_surrogate` and no other; the print
  lines at `E` are `D`'s and `#print axioms real_to_integer_surrogate`; no `sorry`, `admit`, `native_decide` or `axiom`
  enters the code; and each governed file at `E` equals the edit ledger applied to `D`, byte for byte. Otherwise
  `BG-3-STATEMENTS-CHANGED`.
- **Q-DOC.** `BG-3-DOCSTRINGS-CORRECTED` iff no excluded phrase (*The controls*) occurs in the module or in the result
  note at `E`, and the refutation's identifier occurs in the module's header, in the definition's docstring and in
  both consumers' docstrings. Otherwise `BG-3-DOCSTRINGS-NOT-CORRECTED`.
- **Q-KER.** `BG-3-KERNEL-CLEAN` iff the saved tail of `E`'s exact-head Mathlib bridge log shows:
  - `Build completed successfully`;
  - the `#print axioms` report of each of the module's eight prints, `real_to_integer_surrogate` among them, each
    within `propext`, `Classical.choice` and `Quot.sound`;
  - no `sorryAx` and no `Lean.ofReduceBool`;
  - `release gate: PASS`, with `lean-axioms` reporting 5989 named results: `D`'s 5988 and the lemma.

  `lean_axiom_check.py` itself fails on `sorryAx`, on an axiom outside the three, and on a print with no report
  (:15–23), so the passing gate also covers every print of the tree. Otherwise `BG-3-KERNEL-NOT-ESTABLISHED`.

**Preconditions for Q-KER (§A.41).** The module's reports are printed when CI builds it. The executor reads the last
4999 lines of the bridge log, whose bulk is the replayed output of `DitaTorusLocus` (*Design evidence*); reports printed
before that block are out of view. Three measured conditions keep them after it:
- **a small rebuild.** Only the module, its one dependent `TurnpikePremiseOrientation`, and the root rebuild;
  `CongruentReconstruction.lean` stays unchanged (G);
- **`C-FRESH`.** `E`'s exact-head run is the first `verify.yml` run on the round branch at a commit whose OIBridge
  sources differ from `D`'s. Stages 1–3 are pushed together, and no run is dispatched between `F` and `E`. So the run
  restores `main`'s build cache, not one the branch saved for another tree. The checkpoint lists the branch's runs
  before `E`'s;
- **`C-ORDER`.** At `E` the exact-head `verify.yml` run is dispatched first and its bridge log saved; only then is
  `bg2-orientation-design.yml` dispatched. The design workflow restores the build cache and saves none
  (`actions/cache/restore@v4`), so the order costs nothing and removes any doubt.

## The earned reading and the non-inference rule

The earned reading, printed by `controls.py verdict` exactly when all four cells are positive (without code formatting):

> `TurnpikeScopeTransfer.lean` states the real-to-integer reduction once, as `real_to_integer_surrogate`, and
> `spectral_classification_of_BG` factors through it. Its docstrings describe `BGIntegerClassification` as an unsigned
> integer premise refuted by `OIBridge.PremiseOrientation.not_BGIntegerClassification`, and its two consumers as
> implications from it. No statement of the module changes, and `CongruentReconstruction.lean` is unchanged.

> Non-inference rule: this round proves no classification, adopts no sign-aware classification, and discharges no
> hypothesis; `real_to_integer_surrogate` restates a reduction the adopted proof already carried, and assumes no
> classification. The round does not show the published classification false, nor a physical reconstruction theorem;
> it does not change the status of the two-branch theorem, which `papers/GR.md` §3.3 states conditional on H-BG, nor
> of any ledger, census or manuscript site; and it does not retire the design package. It leaves
> `CongruentReconstruction.lean`'s docstrings as they are; their correction is a separate round.

**Premises this round does not source:** the published classification and its comparison with any formal premise;
the sign-aware classification; the exclusion of the reversed correspondence in the adopted library.

## The ROADMAP wording the round applies

ROADMAP.md:1143 at `D` describes the module this round changes: "its docstring calls it the only unproved input of
the reconstruction programme" and "`spectral_classification_of_BG` carries inline the real-to-integer reduction".
Stage 2 replaces that paragraph with the ledger's text. That text:
- states the corrected docstrings and the adopted reduction;
- records that `CongruentReconstruction.lean`'s docstrings describe the three-way hypothesis as what the turnpike
  classification supplies, that the theorem is a valid conditional, that the derivation of its hypothesis from the
  cited classification is not established and that the hypothesis omits the reversed branch, and that correcting the
  docstrings is a separate round;
- keeps the design package's retirement condition unchanged, and marks no classification established.

The P2 row (:72) and :1141 are not changed. :1141 still describes BG-2's control plane as drafted on #826; the citation
swap and the remaining P2 status update, which are separate, correct it.

## The design package

The package stays as it stands, as historical design evidence. Its README (:59–62) and `SignedRepairDesign.lean`
(:14–17) say that the adopted `spectral_classification_of_BG` carries the reduction inline. That describes the
pre-BG-3 implementation. The package records its own baseline (README :7), and the signed-repair round, which retires
it, removes both sentences.

## The controls

- **C1, C2.** This file at `E` is the one at `F`; `git rev-parse <commit>:<path>` equals the frozen blobs for
  `controls.py` and `edit-ledger.json` at stage 1, and for all four files at `E`.
- **L0, L (ledger).** The ledger at `E` has sha256 `LEDGER_SHA256`. Each governed file at `E` equals `D`'s blob with
  the ledger's splices applied, byte for byte; every base, old-text, new-text and result hash must hold.
- **P (preservation).** Independent of the ledger: declarations and their statements are parsed from code only, with
  every `/- … -/` (nested) and `--` comment blanked, so a docstring line beginning `theorem` is not a declaration
  (`CongruentReconstruction.lean:750` at `D` is one). Statements compared byte for byte; names and prints as sets.
- **R (reduction).** The lemma's raw lines compared with the design file's at `D`; applications of
  `integer_realization_of_real_realization` counted in code.
- **S (phrases).** Matched case-insensitively after collapsing whitespace, since a phrase can cross a line break (:3–4
  at `D`). Excluded in the module and the result note at `E`: "only unproved", "Bekir–Golomb 2007, in the spectral
  form", "the 2007 classification for INTEGER", "THE EXTERNAL INTEGER PREMISE", "THE REAL SPECTRAL CLASSIFICATION,
  derived", "CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE", "INTEGER Bekir–Golomb classification", "will eventually
  supply", "can actually feed", "turnpike classification supplies", "Bekir–Golomb is refuted", "the classification is
  false", "the two-branch theorem is false", "the premise is discharged", "H-BG is proved". The first seven occur in the
  module at `D` and the other eight do not, so the check is not vacuous; the eighth to tenth are
  `CongruentReconstruction.lean`'s phrasing, excluded so that this round's text does not take it up.
- **G.** `git diff --no-renames --name-status D E` lies inside the governed paths; exactly the two execution files are
  modified; `CongruentReconstruction.lean`, BG-2's record directory, the design package, `legacy-records.json`,
  `lean-manuscript-census.json`, `verification/coverage/`, `verification/lean/`, `.github/`, `papers/` and `book/` are
  unchanged.
- **K.** The Q-KER rule over the saved tail of `E`'s bridge log.
- **Self-test.** It reads `D` through `git show`, and the preregistration and ledger beside it, never the working tree's
  modules, so a later round that edits the module does not make it fail. It applies the ledger to `D`, accepts the
  output under P, R and S, and rejects each mutation:
  - P: a changed theorem statement; a changed definition body; the lemma's print dropped; an extra print; an extra
    declaration;
  - R: the inline reduction restored in the consumer; a changed lemma statement;
  - S: an excluded phrase reinserted; one across a line break; the refutation dropped from the definition's docstring;
  - L: a byte changed outside every span, which P, R and S accept; a span whose old-text hash does not hold;
  - G: a manuscript, the design package, a probe, `CongruentReconstruction.lean` and the census flagged; a third
    modified file, or a missing one;
  - K: a timestamped log with a report wrapped over three lines, accepted; the same with an extra axiom on a
    continuation line, rejected; synthetic logs with the lemma's report missing, `sorryAx` in it, a non-permitted
    axiom, the count 5988, or a failed gate.

  It also checks that the parser skips the docstring line at `CongruentReconstruction.lean:750`, and that S's phrase
  list splits seven and eight at `D`.
- **Not a CI shard.** `controls.py` runs locally (§A.40). A shard reading the module at every head would fail the next
  round that edits it.
- **`verdict`** exits 1 unless the static controls pass and all four tokens are positive. The tokens are the decision.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane, with the frozen controls, ledger and files | `C1`, `C2` |
| nothing changes outside the ledger, and the ledger's spans hold at `D` | L0, L |
| no declaration's statement changes; the only new declaration is the lemma | P |
| the reduction is stated once and is the design-compiled lemma | R |
| no docstring identifies the premise with the published classification or calls it established input, and the round's text does not take up the claim that the classification supplies `hclass` | S |
| the module builds, and every print, the lemma's among them, reports within the three axioms with no `sorry` | K over `E`'s bridge log |
| the reports are inside the log window the executor reads | a small rebuild (G); `C-FRESH`; `C-ORDER`; *Design evidence* (report positions) |
| the dependents build: `TurnpikePremiseOrientation`, BG-2's shard, the root | `C3`: the exact-head run at `E`, every job `success` |
| the design package still compiles against the changed module | `C-DES`: `bg2-orientation-design.yml` dispatched at the predicted tree's exact SHA and at `E`, after the verify run (`C-ORDER`), `success` |
| the change stays inside the governed paths; `CongruentReconstruction.lean`, the census, the probes, the workflows and the manuscripts unchanged | G; the release gate's `lean-manuscript` at `E` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Hazards measured at drafting

- **BG-2's controls.** Its self-test reads only `TurnpikePremiseOrientation.lean` and its preregistration from the
  working tree (`controls.py:247–291`). Its line-pinned S2 (:45–56, :166–176) reads `TurnpikeScopeTransfer.lean` at
  BG-2's own commits through `git show`. So the change does not fail BG-2's shard. `BGIntegerClassification` and
  `AscPair` keep their names, which BG-2's module imports.
- **Name resolution in the design file.** `SignedRepairDesign.lean` declares its own `real_to_integer_surrogate` in
  `OIBridge.ScopeTransferSigned` and opens `ScopeTransfer`. The first design run compiled it against the changed
  module (`C-DES`, run 38808918711).
- **The design workflow** runs only on changes to the package or its workflow file, and on dispatch
  (`bg2-orientation-design.yml:3–12`). Hence the dispatch in `C-DES`.
- **The census (§A.35).** No statement in an existing module becomes stronger, and the module list of the family
  "Hamiltonian reconstruction" (`lean-manuscript-census.json:143–170`) is unchanged; the registry does not change.
- **The rebuild size.** A change to `CongruentReconstruction.lean` rebuilds 188 of the 223 OIBridge modules; a change
  to `TurnpikeScopeTransfer.lean` rebuilds it, `TurnpikePremiseOrientation` and the root.
- **Branch-scoped build caches.** On a cache miss the bridge restores the most recent cache with the key prefix in its
  own branch's scope before the default branch's. A disposable branch that has built one tree saves a cache that a
  second tree on the same branch would restore. The first design branch holds such a cache, built with the changed
  `CongruentReconstruction.lean` (run 38808914622). So the reduced tree is tested on a fresh branch. The round branch
  saves none before `E`: `F`'s run matches `main`'s key exactly.

## Design evidence

**The first predicted tree, superseded.** `3218e8d052e01650baae645e7eb92355e56e7b34` on `tmp/bg3-predicted-20261015`
carried the edits above and the four `CongruentReconstruction.lean` docstrings.
- `verify.yml` dispatch run 38808914622, attempt 1: every job `success`, 37 of 37.
  - The Mathlib bridge (job 116676857951) took 57 minutes to build. Its release gate passed every step: `lean-axioms`
    5989, no `sorry`; `lean-manuscript` OK; 303 legacy records intact; 47 receipts holding.
  - The last 4999 lines of its log hold 114 `DitaTorusLocus` reports with their output (lines 13–4924), then the root's
    19 (4926–4944), `Build completed successfully` (4945) and the gate. None of the module's eight reports is in them.
- `controls.py verdict 3218e8d0 --freeze 7c221e98` over that tail: C1, C2, L0, L, P, R, S and G pass;
  `BG-3-REDUCTION-FACTORED`, `BG-3-STATEMENTS-PRESERVED`, `BG-3-DOCSTRINGS-CORRECTED`, `BG-3-KERNEL-NOT-ESTABLISHED`.
- `bg2-orientation-design.yml` dispatch run 38808918711 at the same SHA: `success`. Both design files compiled against
  the changed module; all 10 axiom reports matched `axiom-reports.txt`; 303 legacy records and 47 receipts.
- For comparison, BG-2's stage-2 run (bridge job 116481534373), a small rebuild, printed its new module's reports at
  line 4918 of its window, after the same `DitaTorusLocus` block and before the root's.

**The reduced predicted tree, first form.** `6c160ad26a9831448e6e4cfca5761efb876a1baf` on
`tmp/bg3-predicted-reduced-20261015`: this scope, with the previous form of `controls.py` (blob `1b5c4489`).
- `verify.yml` dispatch run 38834744516, attempt 1, the branch's first run: every job `success`, 37 of 37.
  - The Mathlib bridge (job 116761232088) took 3 minutes 16 seconds and rebuilt `TurnpikeScopeTransfer` (6.6 s),
    `TurnpikePremiseOrientation` (5.8 s) and the root. Its release gate passed every step: `lean-axioms` 5989, no
    `sorry`; `lean-manuscript` OK; 303 legacy records intact; 47 receipts holding.
  - In the last 4999 lines of its log (sha256 `e77b0ded140a70ae90514a2d923bae20a062415c45ab3c8ec62ed65ce26bac47`) the
    module's eight reports are at lines 4908–4917, after the `DitaTorusLocus` block and before
    `TurnpikePremiseOrientation`'s and the root's. Each is within `propext`, `Classical.choice` and `Quot.sound`;
    `real_to_integer_surrogate`'s is at line 4914. The window contains no `sorryAx` and no `Lean.ofReduceBool`.
- `controls.py verdict 6c160ad2 --freeze f33b2fa2` over that tail, with the checker in that tree: C1, C2, L0, L, P, R,
  S and G pass; `BG-3-REDUCTION-FACTORED`, `BG-3-STATEMENTS-PRESERVED`, `BG-3-DOCSTRINGS-CORRECTED`,
  `BG-3-KERNEL-NOT-ESTABLISHED`. The last is a checker defect, recorded below.

**Two defects of the checker, found by the design runs and fixed before the freeze.**
- *The verdict's status line.* With the static controls passing and a token negative, the first form printed
  `controls: FAILED (0 failure(s))`. It now prints `controls: static checks OK; not every token is positive`. The exit
  status was right in both forms.
- *Reports wrapped over several log lines.* The host prefixes every log line with a timestamp, and the report of
  `integer_realization_of_real_realization` wraps its axiom list over three lines (4911–4913). The first form read the
  prefixes into the axiom names, so `Classical.choice` failed the permitted-axiom test. K now removes the prefixes
  before reading the reports. The self-test gains two cases: a timestamped log with a report wrapped over three lines,
  accepted; and the same with an extra axiom on a continuation line, rejected. Under the first form the accepted case
  fails, so the case covers the defect. Over the two saved bridge tails, the first form's K reads 8 and 0 reports and
  rejects both; the corrected K reads the same reports, accepts the first and rejects the second, which has none. The
  corrected checker's verdict over run 38834744516's tail prints the four positive tokens and the earned reading.

**The reduced predicted tree, corrected checker.** To come, on the fresh disposable branch
`tmp/bg3-predicted-reduced2-20261016`, at one exact SHA. The first branch now holds a build cache for these Lean
sources, and a run that hits it replays the reports in an order that can put them outside the window (BG-2's `E`), so
the corrected tree is not run there:
- its `verify.yml` dispatch run: every job `success`; the gate's `lean-axioms` count; the eight report lines and their
  positions in the executor's log window; then the verdict with the checker in the tree; then
- `bg2-orientation-design.yml` dispatched at the same SHA (`C-ORDER`);
- `controls.py --self-test`, and `controls.py check` over the predicted commit with this file's commit as `--freeze`.

These runs are design evidence, not `check-run` attestations. The four files' blobs are frozen there:

```bg3-frozen-blobs
verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/controls.py 52b52095c6609166f428a4a61f8aae2a23f0efa0
verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/edit-ledger.json 1e82e5a628e9f12b8cb0b2882caeba5d8205013c
verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean 6c2e3e33c6aedcf04672259d4b0588a42c36c6b7
verification/ROADMAP.md 3209f8b0d010f6ce6a7b76bbfb9189352b3d1cbe
```

The ledger's sha256 is `178a70a51da011f1a6259bded32d45a581bd87d9bb764a3f1ad0052de0052dfb`.

## Owner decisions

Owner decisions (2026-10-15):
- the label BG-3 and the record directory `round-bg-3-scope-transfer-correction`;
- the round applies the ROADMAP :1143 paragraph; the citation swap and the remaining P2 status update stay separate;
- the design package stays untouched, as historical design evidence;
- the R7 lint list of `edge_rigidity_probe.py` stays unchanged;
- drafting on `draft/bg-3-scope-transfer-20261015` with a draft pull request, and design testing on a disposable
  branch, both from `D`. This authorizes no designation of `F`, no execution and no merge;
- at `E`, the exact-head `verify.yml` run first and its bridge log saved, then the design dispatch;
- the corrected checker is tested on the fresh disposable branch `tmp/bg3-predicted-reduced2-20261016` (2026-10-16);
- `CongruentReconstruction.lean`'s four docstrings were first included. After the first design run hid the module's
  axiom reports, the owner's standing instruction applied: their correction is deferred to a separate round, the scope
  is revised before the freeze, the deferral stays explicitly tracked, and BG-3 neither restores nor endorses the
  stronger claim.

Before `F` is presented: the independent splice checks, the mutation controls, the design workflow, the Lean build and
the release gate, all reproducible at the reduced predicted tree's exact SHA. After `F`, any change to a frozen artifact
follows the governed halt procedure (`S12`).

## Stages and outcomes

Stage 1 commits `controls.py` and `edit-ledger.json` at their frozen blobs; stage 2 the module and the ROADMAP at their
frozen blobs; stage 3 the result note, candidate `E`. The three stages are pushed together (`C-FRESH`).
**`BG-3-READ`**: `controls.py check E --freeze F` OK (C1, C2, L0, L, P, R, S, G), `verdict` printing the four positive
tokens over `E`'s bridge log, the exact-head run at `E` green on every job (`C3`), `C-FRESH`, `C-ORDER`, and `C-DES`
green at `E`. **`BG-3-HALTED`**: anything else (`S12`). No outcome changes a manuscript, the census, a probe, a
workflow, `CongruentReconstruction.lean`, BG-2's record or the design package; correctness bands unchanged
(consistency axis).

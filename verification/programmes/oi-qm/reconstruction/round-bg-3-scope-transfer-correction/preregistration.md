# Reconstruction round BG-3 — the scope-transfer modules after the premise refutation: PREREGISTRATION (draft)

**Status: drafting, native V3; not a candidate `F`.** Drafted on a pull request from `D`. The owner decisions are
recorded below. The predicted execution tree — `D`, this control plane, `controls.py`, the edit ledger and the three
governed files, less the result note — is under test on the disposable branch `tmp/bg3-predicted-20261015`
(*Design evidence*); the blobs below are predicted and become frozen only with that evidence. Nothing is executed.
Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round BG-3
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/
record AM verification/receipts/BG-3.json
execution M verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean
execution M verification/lean-mathlib/OIBridge/CongruentReconstruction.lean
execution M verification/ROADMAP.md
```

D: e3ad5d7a71910ce5413ef6dacd25bf5a63d5a1e0. It is `main` after #826, and its push run 38800143579 concluded `success`.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, other landed module, census entry, probe, workflow, coverage-ledger entry, BG-2 record or file of the design package
changes under any outcome**, and no statement of a landed declaration changes.

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

**The same omission in `CongruentReconstruction.lean`.** A corpus sweep for the defect's phrasing (§A.25, §A.19) finds
it in the module whose theorem `TurnpikeScopeTransfer` feeds. `twoBranch_of_spectral_classification` takes a
three-way hypothesis `hclass` about the given pair — translation-congruent, reflection-congruent, or `mu` in one
orientation. The theorem is a valid conditional. Its docstrings say where `hclass` comes from:
- :2–3: "the conditional two-branch theorem with the Piccard classification as its only unproved premise";
- :24–30: "the premise is what the Piccard/Bekir–Golomb turnpike classification … will eventually supply";
- :709–712: the classification premise "is what the Piccard/Bekir–Golomb turnpike classification supplies";
- :749–751: "the theorem in the form the Piccard/Bekir–Golomb turnpike classification can actually feed".

That derivation is not established. The non-congruent pair (0,1,4,10,12,17), (0,4,6,9,16,17) realizes `mu` reversed
and in no relabeling in the orientation `hclass` lists (`not_muForm_r1_r2refl`, `revMuForm_r1_r2refl`), so any
derivation of `hclass` from a classification of rulers must also exclude the reversed branch. The design package's
`reversed_exceptional_impossible` does so; the adopted library does not. BG-2's pair contradicts a formal premise; it
says nothing against the published classification or a physical reconstruction theorem. This round corrects the four
docstrings and none of the module's statements.

**Assumption-watch marker.** A docstring that names a hypothesis's source ("what the classification supplies") is a
claim about a second proposition, and a refutation of that proposition reaches the docstring even when the theorem
statement is unaffected.

## The edits

Every change is a splice of `D`'s text. The **edit ledger** `edit-ledger.json` records, for each governed file, its
sha256 at `D`, its sha256 after the round, and each splice: a 1-based line span of `D`'s text, the sha256 of the old
text, the new text and its sha256, and a reason. It is the authorization: nothing outside it changes in the three
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
| `CongruentReconstruction.lean` | :2–3, :24–30, :709–712, :749–751 | the theorem is a valid conditional; the derivation of `hclass` from the published classification is not established and needs an exclusion of the reversed branch |
| `verification/ROADMAP.md` | :1143 | the kernel-side items: the docstrings record the refutation, the reduction is adopted |

**What stays.** Every declaration of both modules keeps its name and its statement byte for byte; the only added
declaration is `real_to_integer_surrogate`. `BGIntegerClassification`, `AscPair` and the two consumers keep their
names, as `TurnpikePremiseOrientation.lean`, the R7 lint of `edge_rigidity_probe.py` (:365–369) and the manuscript
and ledger sites cite them. The probe's lint list does not gain the lemma.

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
- **Q-PRES.** `BG-3-STATEMENTS-PRESERVED` iff, in both modules, every declaration at `D` has a byte-identical
  statement at `E` (a definition's whole body); `E` declares `D`'s names and `real_to_integer_surrogate` and no other;
  the print lines at `E` are `D`'s and `#print axioms real_to_integer_surrogate`; no `sorry`, `admit`, `native_decide`
  or `axiom` enters the code; and each governed file at `E` equals the edit ledger applied to `D`, byte for byte.
  Otherwise `BG-3-STATEMENTS-CHANGED`.
- **Q-DOC.** `BG-3-DOCSTRINGS-CORRECTED` iff no excluded phrase (*The controls*) occurs in either module or in the
  result note at `E`; the refutation's identifier occurs in `TurnpikeScopeTransfer.lean`'s header, in the definition's
  docstring and in both consumers' docstrings; and `revMuForm_r1_r2refl` occurs in `CongruentReconstruction.lean`'s
  header. Otherwise `BG-3-DOCSTRINGS-NOT-CORRECTED`.
- **Q-KER.** `BG-3-KERNEL-CLEAN` iff the saved tail of `E`'s exact-head Mathlib bridge log shows:
  - `Build completed successfully`;
  - the `#print axioms` report of each of the module's eight prints, `real_to_integer_surrogate` among them, each
    within `propext`, `Classical.choice` and `Quot.sound`;
  - no `sorryAx` and no `Lean.ofReduceBool`;
  - `release gate: PASS`, with `lean-axioms` reporting 5989 named results: `D`'s 5988 and the lemma.

  `lean_axiom_check.py` itself fails on `sorryAx`, on an axiom outside the three, and on a print with no report
  (:15–23), so the passing gate also covers every print of the tree. Otherwise `BG-3-KERNEL-NOT-ESTABLISHED`.

**A precondition for Q-KER (§A.41).** The module's reports are printed when CI builds it, and a later run that hits
the build cache replays them in an order that can put them outside the executor's 4999-line log window (BG-2's `E`).
So `E`'s exact-head run is the first `verify.yml` run on the round branch at a commit whose OIBridge sources differ from
`D`'s: stages 1–3 are pushed together, and no run is dispatched between `F` and `E`. Checkpoint `C-FRESH` lists the
branch's runs before `E`'s. *Design evidence* measures where the reports land in a fresh build.

## The earned reading and the non-inference rule

The earned reading, printed by `controls.py verdict` exactly when all four cells are positive (without code formatting):

> `TurnpikeScopeTransfer.lean` states the real-to-integer reduction once, as `real_to_integer_surrogate`, and
> `spectral_classification_of_BG` factors through it. Its docstrings describe `BGIntegerClassification` as an unsigned
> integer premise refuted by `OIBridge.PremiseOrientation.not_BGIntegerClassification`, and its two consumers as
> implications from it. `CongruentReconstruction.lean`'s docstrings describe `hclass` as a hypothesis about the given
> pair whose derivation from the published classification is not established, and which omits the reversed
> exceptional branch. No statement of either module changes.

> Non-inference rule: this round proves no classification, adopts no sign-aware classification, and discharges no
> hypothesis; `real_to_integer_surrogate` restates a reduction the adopted proof already carried, and assumes no
> classification. The round does not show the published classification false, nor a physical reconstruction theorem;
> it does not change the status of the two-branch theorem, which `papers/GR.md` §3.3 states conditional on H-BG, nor
> of any ledger, census or manuscript site; and it does not retire the design package.

**Premises this round does not source:** the published classification and its comparison with any formal premise;
the sign-aware classification; the exclusion of the reversed correspondence in the adopted library.

## The ROADMAP wording the round applies

ROADMAP.md:1143 at `D` describes the module this round changes: "its docstring calls it the only unproved input of
the reconstruction programme" and "`spectral_classification_of_BG` carries inline the real-to-integer reduction".
Stage 2 replaces that paragraph with the ledger's text. That text states the corrected docstrings and the adopted
reduction, keeps the design package's retirement condition unchanged, and marks no classification established. The P2
row (:72) and :1141 are not changed. :1141 still describes BG-2's control plane as drafted on #826; the citation swap and
the remaining P2 status update, which are separate, correct it.

## The design package

The package stays as it stands, as historical design evidence. Its README (:59–62) and `SignedRepairDesign.lean`
(:14–17) say that the adopted `spectral_classification_of_BG` carries the reduction inline. That describes the
pre-BG-3 implementation. The package records its own baseline (README :7), and the signed-repair round, which retires
it, removes both sentences.

## The controls

- **C1, C2.** This file at `E` is the one at `F`; `git rev-parse <commit>:<path>` equals the frozen blobs for
  `controls.py` and `edit-ledger.json` at stage 1, and for all five files at `E`.
- **L0, L (ledger).** The ledger at `E` has sha256 `LEDGER_SHA256`. Each governed file at `E` equals `D`'s blob with
  the ledger's splices applied, byte for byte; every base, old-text, new-text and result hash must hold.
- **P (preservation).** Independent of the ledger: declarations and their statements are parsed from code only, with
  every `/- … -/` (nested) and `--` comment blanked, so a docstring line beginning `theorem` is not a declaration
  (`CongruentReconstruction.lean:750` at `D` is one). Statements compared byte for byte; names and prints as sets.
- **R (reduction).** The lemma's raw lines compared with the design file's at `D`; applications of
  `integer_realization_of_real_realization` counted in code.
- **S (phrases).** Matched case-insensitively after collapsing whitespace, since a phrase can cross a line break (:3–4
  at `D`). Excluded in both modules and the result note at `E`: "only unproved", "Bekir–Golomb 2007, in the spectral
  form", "the 2007 classification for INTEGER", "THE EXTERNAL INTEGER PREMISE", "THE REAL SPECTRAL CLASSIFICATION,
  derived", "CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE", "INTEGER Bekir–Golomb classification", "will eventually
  supply", "can actually feed", "turnpike classification supplies", "Bekir–Golomb is refuted", "the classification is
  false", "the two-branch theorem is false", "the premise is discharged", "H-BG is proved". The first ten occur at `D`
  and the other five do not, so the check is not vacuous.
- **G.** `git diff --no-renames --name-status D E` lies inside the governed paths; exactly the three execution files
  are modified; BG-2's record directory, the design package, `legacy-records.json`, `lean-manuscript-census.json`,
  `verification/coverage/`, `verification/lean/`, `.github/`, `papers/` and `book/` are unchanged.
- **K.** The Q-KER rule over the saved tail of `E`'s bridge log.
- **Self-test.** It reads `D` through `git show`, and the preregistration and ledger beside it, never the working tree's
  modules, so a later round that edits the modules does not make it fail. It applies the ledger to `D`, accepts the
  output under P, R and S, and rejects each mutation:
  - P: a changed theorem statement; a changed definition body; the lemma's print dropped; an extra print; an extra
    declaration; a changed statement in `CongruentReconstruction.lean`;
  - R: the inline reduction restored in the consumer; a changed lemma statement;
  - S: an excluded phrase reinserted; one across a line break; the refutation dropped from the definition's docstring;
  - L: a byte changed outside every span, which P, R and S accept; a span whose old-text hash does not hold;
  - G: a manuscript, the design package, a probe and the census flagged; a fourth modified file, or a missing one;
  - K: synthetic logs with the lemma's report missing, `sorryAx` in it, a non-permitted axiom, the count 5988, or a
    failed gate.

  It also checks that the parser skips the docstring line at `CongruentReconstruction.lean:750`, and that S's phrase
  list splits ten and five at `D`.
- **Not a CI shard.** `controls.py` runs locally (§A.40). A shard reading these modules at every head would fail the
  next round that edits them.
- **`verdict`** exits 1 unless the static controls pass and all four tokens are positive. The tokens are the decision.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane, with the frozen controls, ledger and files | `C1`, `C2` |
| nothing changes outside the ledger, and the ledger's spans hold at `D` | L0, L |
| no declaration's statement changes; the only new declaration is the lemma | P |
| the reduction is stated once and is the design-compiled lemma | R |
| no docstring identifies the premise with the published classification, calls it established input, or claims `hclass` is supplied by it | S |
| the module builds, and every print, the lemma's among them, reports within the three axioms with no `sorry` | K over `E`'s bridge log |
| the reports are inside the log window the executor reads | `C-FRESH`; *Design evidence* (report positions in a fresh build) |
| the dependents build: BG-2's module and shard, `ThermalOrientation`, the root | `C3`: the exact-head run at `E`, every job `success` |
| the design package still compiles against the changed modules | `C-DES`: `bg2-orientation-design.yml` dispatched at the predicted tree's exact SHA and at `E`, `success` |
| the change stays inside the governed paths; no census, probe, workflow or manuscript change | G; the release gate's `lean-manuscript` at `E` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Hazards measured at drafting

- **BG-2's controls.** Its self-test reads only `TurnpikePremiseOrientation.lean` and its preregistration from the
  working tree (`controls.py:247–291`). Its line-pinned S2 (:45–56, :166–176) reads `TurnpikeScopeTransfer.lean` at
  BG-2's own commits through `git show`. So the change does not fail BG-2's shard. `BGIntegerClassification` and
  `AscPair` keep their names, which BG-2's module imports.
- **Name resolution in the design file.** `SignedRepairDesign.lean` declares its own `real_to_integer_surrogate` in
  `OIBridge.ScopeTransferSigned` and opens `ScopeTransfer`. Lean resolves the current namespace before opened ones, so
  its references stay unambiguous. `C-DES` measures this rather than relying on it.
- **The design workflow** runs only on changes to the package or its workflow file, and on dispatch
  (`bg2-orientation-design.yml:3–12`). Hence the dispatch in `C-DES`.
- **The census (§A.35).** No statement in an existing module becomes stronger, and the module list of the family
  "Hamiltonian reconstruction" (`lean-manuscript-census.json:143–170`) is unchanged; the registry does not change.
- **The bridge log window.** Q-KER's report lines are printed during the build. `C-FRESH` keeps `E`'s build fresh, and
  the gate summary, which carries the count, is at the log's end.

## Design evidence

To come, on `tmp/bg3-predicted-20261015` at one exact SHA:
- its `verify.yml` dispatch run: every job `success`; the gate's `lean-axioms` count; the eight report lines and
  their line positions in the executor's log window;
- `bg2-orientation-design.yml` dispatched at the same SHA;
- `controls.py --self-test`, and `controls.py check` and `verdict` over the predicted commit with this file's commit as
  `--freeze`.

These runs are design evidence, not `check-run` attestations. The five files' blobs are frozen there:

```bg3-frozen-blobs
verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/controls.py 2420bbb5b15b282831958bd630270c51b35b645c
verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/edit-ledger.json 3428e239b4c12e790be30e1411a24a50abfb3d13
verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean 6c2e3e33c6aedcf04672259d4b0588a42c36c6b7
verification/lean-mathlib/OIBridge/CongruentReconstruction.lean cc52b5a2b71a6e7e4a5fac84e84d03befaed73d7
verification/ROADMAP.md 29ca2b903bca1fafc5254380a4e63f8a17777e2b
```

The ledger's sha256 is `7ad8dbef706b6deafd868100f43fa846f67a0236c8b57013180a6b2641527352`.

## Owner decisions

Owner decisions (2026-10-15):
- the label BG-3 and the record directory `round-bg-3-scope-transfer-correction`;
- `CongruentReconstruction.lean`'s four docstrings are corrected in this round, to say that the theorem is a valid
  conditional and that the derivation of `hclass` from the cited classification is not established;
- the round applies the ROADMAP :1143 paragraph; the citation swap and the remaining P2 status update stay separate;
- the design package stays untouched, as historical design evidence;
- the R7 lint list of `edge_rigidity_probe.py` stays unchanged;
- drafting on `draft/bg-3-scope-transfer-20261015` with a draft pull request, and design testing on
  `tmp/bg3-predicted-20261015`, both from `D`. This authorizes no designation of `F`, no execution and no merge.

Before `F` is presented: the independent splice checks, the mutation controls, the design workflow, the Lean build and
the release gate, all reproducible at the predicted tree's exact SHA. After `F`, any change to a frozen artifact follows
the governed halt procedure (`S12`).

## Stages and outcomes

Stage 1 commits `controls.py` and `edit-ledger.json` at their frozen blobs; stage 2 the two modules and the ROADMAP at
their frozen blobs; stage 3 the result note, candidate `E`. The three stages are pushed together (`C-FRESH`).
**`BG-3-READ`**: `controls.py check E --freeze F` OK (C1, C2, L0, L, P, R, S, G), `verdict` printing the four positive
tokens over `E`'s bridge log, the exact-head run at `E` green on every job (`C3`), `C-FRESH`, and `C-DES` green at `E`.
**`BG-3-HALTED`**: anything else (`S12`). No outcome changes a manuscript, the census, a probe, a workflow, BG-2's
record or the design package; correctness bands unchanged (consistency axis).

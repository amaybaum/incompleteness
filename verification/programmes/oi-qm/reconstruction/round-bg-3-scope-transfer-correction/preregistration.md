# Reconstruction round BG-3 — the scope-transfer modules after the premise refutation: PREREGISTRATION (draft)

**Status: drafting, native V3; not a candidate `F`.** Nothing is frozen or executed. The predicted modules, the edit
ledger and `controls.py` are not yet built on a disposable branch or run at its exact head (*Design evidence*, to
come), and the owner decisions below are open. Only the owner designates `F` under AGENTS §A.39; an instruction to
proceed is not a designation.

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

D: e3ad5d7a71910ce5413ef6dacd25bf5a63d5a1e0. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory. **No manuscript, built artifact, other landed module, census entry, probe, workflow, BG-2
record or file of the design package changes under any outcome**, and no statement of a landed declaration changes.

## What the round is

**Provenance.** BG-2 (landed by #826 at `D`; receipt `verification/receipts/BG-2.json`) certifies
`OIBridge.PremiseOrientation.not_BGIntegerClassification` and its controls, and changes no landed module. Its owner
decisions (`round-bg-2-premise-orientation/preregistration.md:292–307`) make the correction of
`TurnpikeScopeTransfer.lean` a separate governed round: the docstring that calls the refuted premise "the ONLY
unproved input", and moving into the module the reduction that the design package's `SignedRepairDesign.lean`
factors as `real_to_integer_surrogate`. ROADMAP.md:1143 tracks both under P2. This round is that correction. It
adopts no sign-aware premise and replaces no design-package citation; those are separate.

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
orientation — and its statement is a correct conditional. Its docstrings name the source of `hclass`:
- :2–3: "the conditional two-branch theorem with the Piccard classification as its only unproved premise";
- :24–30: "the premise is what the Piccard/Bekir–Golomb turnpike classification … will eventually supply";
- :709–712: the classification premise "is what the Piccard/Bekir–Golomb turnpike classification supplies";
- :749–751: "the theorem in the form the Piccard/Bekir–Golomb turnpike classification can actually feed".

BG-2's pair refutes this too. (0,1,4,10,12,17), (0,4,6,9,16,17) is non-congruent and realizes `mu` only reversed
(`not_muForm_r1_r2refl`, `revMuForm_r1_r2refl`), so `hclass` fails for it. A classification of rulers supplies
`hclass` only together with a separate exclusion of the reversed branch, which the design package's
`reversed_exceptional_impossible` provides and the adopted library does not. This round corrects these four
docstrings and none of the module's statements (owner decision 2 below).

**Assumption-watch marker.** A docstring that names a hypothesis's source ("what the classification supplies") is a
claim about a second proposition, and a refutation of that proposition reaches the docstring even when the theorem
statement is unaffected.

## The edits

Every change is a splice of `D`'s text, recorded in the edit ledger that `controls.py` carries. A splice has a span, the
sha256 of the old text, the new text and its sha256, and a reason. Nothing outside the ledger changes in the three
files.

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
| `CongruentReconstruction.lean` | :2–3, :24–30, :709–712, :749–751 | the hypothesis is about the given pair, and omits the reversed branch |
| `verification/ROADMAP.md` | :1143 | the kernel-side items: the docstrings record the refutation, the reduction is adopted |

The predicted blobs are `6c2e3e33` (`TurnpikeScopeTransfer.lean`), `2780cc4c` (`CongruentReconstruction.lean`) and
`29ca2b90` (`ROADMAP.md`). They are not frozen; *Design evidence* will freeze them.

**What stays.** Every declaration of both modules keeps its name and its statement byte for byte; the only added
declaration is `real_to_integer_surrogate`. `BGIntegerClassification`, `AscPair` and the two consumers keep their
names, as `TurnpikePremiseOrientation.lean`, the R7 lint of `edge_rigidity_probe.py` (:365–369) and the manuscript
and ledger sites cite them.

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
  to the design package's at `D`; `spectral_classification_of_BG`'s proof applies it; and
  `integer_realization_of_real_realization` is applied exactly once in the module, inside the lemma. Otherwise
  `BG-3-REDUCTION-NOT-FACTORED`.
- **Q-PRES.** `BG-3-STATEMENTS-PRESERVED` iff, in both modules, every declaration at `D` has a byte-identical
  statement at `E`; `E` declares `D`'s names and `real_to_integer_surrogate` and no other; the print lines at `E` are
  `D`'s and `#print axioms real_to_integer_surrogate`; and each file at `E` equals the edit ledger applied to `D`, byte
  for byte. Otherwise `BG-3-STATEMENTS-CHANGED`.
- **Q-DOC.** `BG-3-DOCSTRINGS-CORRECTED` iff no excluded phrase (*The controls*) occurs in either module at `E`, the
  refutation's identifier occurs in `TurnpikeScopeTransfer.lean`'s header, the definition's docstring and both
  consumers' docstrings, and `revMuForm_r1_r2refl` occurs in `CongruentReconstruction.lean`'s header. Otherwise
  `BG-3-DOCSTRINGS-NOT-CORRECTED`.
- **Q-KER.** `BG-3-KERNEL-CLEAN` iff the exact-head run at `E` has every job `success`, and its Mathlib bridge's
  release gate passes every step with `lean-axioms` reporting 5989 named results: `D`'s 5988 and
  `real_to_integer_surrogate`. `lean_axiom_check.py` fails on `sorryAx`, on any axiom outside `propext`,
  `Classical.choice` and `Quot.sound`, and on a print with no report (:15–23), so a passing gate with that count
  establishes the new print's axioms. The gate summary is at the end of the job's log, inside the window the executor
  can read. Otherwise `BG-3-KERNEL-NOT-ESTABLISHED`.

## The earned reading and the non-inference rule

The earned reading, printed exactly when all four cells are positive:

> `TurnpikeScopeTransfer.lean` states the real-to-integer reduction once, as `real_to_integer_surrogate`, and
> `spectral_classification_of_BG` factors through it. Its docstrings describe `BGIntegerClassification` as an unsigned
> integer premise refuted by `OIBridge.PremiseOrientation.not_BGIntegerClassification`, and its two consumers as
> implications from it. `CongruentReconstruction.lean`'s docstrings describe `hclass` as a hypothesis about the given
> pair that omits the reversed exceptional branch. No statement of either module changes.

> Non-inference rule: this round proves no classification, adopts no sign-aware premise, and discharges no
> hypothesis; `real_to_integer_surrogate` restates a reduction the adopted proof already carried. It does not change
> the status of the two-branch theorem, which `papers/GR.md` §3.3 states conditional on H-BG, nor of any ledger,
> census or manuscript site, and it does not retire the design package.

**Premises this round does not source:** the published classification and its comparison with any formal premise;
the sign-aware premise; the exclusion of the reversed correspondence in the adopted library.

## The ROADMAP wording the round applies

ROADMAP.md:1143 at `D` describes the module this round changes: "its docstring calls it the only unproved input of
the reconstruction programme" and "`spectral_classification_of_BG` carries inline the real-to-integer reduction".
Stage 2 replaces that paragraph with the ledger's text, which keeps its last sentence (the design package's retirement
condition) unchanged. The P2 row (:72), its label and :1141 are not changed; replacing the design-package citations
is the separate status update.

## The controls

- **C1, C2.** This file's blob at `F`; `git rev-parse <commit>:<path>` equal to the frozen blobs for `controls.py` at
  stage 1 and for all four files at `E`.
- **L (ledger).** `controls.py check E --freeze F` rebuilds each governed file from `D`'s blob and the frozen ledger
  alone, and compares bytes with `E`. It asserts each span's old-text hash at `D`.
- **P (preservation).** Independent of the ledger: declarations and their statements are parsed from code only, outside
  `/- … -/` and `--` comments, so a docstring line beginning `theorem` is not a declaration (at `D`,
  `CongruentReconstruction.lean:750` is one). Statements compared byte for byte; names and prints compared as sets.
- **R (reduction).** The lemma compared with the design file's text at `D`; applications of
  `integer_realization_of_real_realization` counted in code.
- **S (phrases).** Matched after collapsing whitespace, since a phrase can cross a line break (:3–4 at `D`). Excluded
  in both modules at `E` and in the result note: "only unproved", "ONLY unproved",
  "Bekir–Golomb 2007, in the spectral form", "the 2007 classification for INTEGER", "THE EXTERNAL INTEGER PREMISE",
  "THE REAL SPECTRAL CLASSIFICATION, derived", "CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE", "INTEGER
  Bekir–Golomb classification", "will eventually supply", "can actually feed", "turnpike classification supplies",
  "Bekir–Golomb is refuted", "the classification is false", "the two-branch theorem is false", "the premise is
  discharged", "H-BG is proved". The first eleven occur at `D` (eight in `TurnpikeScopeTransfer.lean`, four in
  `CongruentReconstruction.lean`, "only unproved" in both), so the check is not vacuous.
- **G.** `git diff --no-renames --name-status D E` lies inside the governed paths; BG-2's record directory, the
  design package, `legacy-records.json`, `lean-manuscript-census.json`, every probe and every workflow unchanged.
- **K.** The Q-KER rule over the saved tail of `E`'s bridge log.
- **Self-test.** It reads `D` and `F` through `git show`, never the working tree, so it does not fail when a later
  round changes these modules. It accepts the predicted files and rejects each mutation:
  - a changed statement of an existing declaration;
  - the inline reduction restored in `spectral_classification_of_BG`;
  - an excluded phrase reinserted;
  - a print dropped, or an extra print;
  - a changed lemma statement;
  - an extra declaration;
  - a byte outside the ledger's spans;
  - a docstring line beginning `theorem` counted as a declaration (the parser must not).
- **Not a CI shard.** `controls.py` runs locally (§A.40). A shard reading these modules at every head would fail the
  next round that edits them.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane, with the frozen controls and modules | `C1`, `C2` |
| nothing changes outside the ledger, and the ledger's spans hold at `D` | L |
| no declaration's statement changes; the only new declaration is the lemma | P |
| the reduction is stated once and is the design-compiled lemma | R |
| no docstring identifies the premise with the published classification or calls it established input | S |
| every print elaborates within the three axioms, with no `sorry` | K: the release gate at `E` |
| the dependents build: BG-2's module, its shard, `ThermalOrientation`, the root | K: every job `success` at `E` |
| the design package still compiles against the changed modules | `C-DES`: `bg2-orientation-design.yml` dispatched at the predicted tree and at `E`, `success` |
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
- **The bridge log window.** Q-KER reads only the gate summary at the log's end; no cell needs a report line inside
  the build output.

## Design evidence

To come: the predicted tree (`D` with the three files and `controls.py`, less the result note) on a disposable branch;
its exact-head `verify.yml` run, every job `success`, with the gate's `lean-axioms` count; `bg2-orientation-design.yml`
dispatched on it; `controls.py --self-test` and `check` over it. Those runs are design evidence, not `check-run`
attestations, and the four files' blobs are frozen there.

## Owner decisions (open)

1. The label BG-3 and the record directory `round-bg-3-scope-transfer-correction`.
2. Whether `CongruentReconstruction.lean`'s four docstrings are corrected in this round (drafted: yes) or in a separate
   one.
3. Whether the round applies the ROADMAP :1143 paragraph (drafted: yes) or leaves it to the status update.
4. The design package stays untouched. Its README (:59–62) and `SignedRepairDesign.lean` (:14–17) say the adopted proof
   carries the reduction inline; after the round that describes `D`, the package's stated baseline being older still
   (README :7). The signed-repair round, which retires the package, removes both.
5. The R7 lint names of `edge_rigidity_probe.py` stay as they are (drafted), or gain `real_to_integer_surrogate`, which
   adds the probe to the governed paths.
6. The drafting branch and pull request.

## Stages and outcomes

Stage 1 commits `controls.py` at its frozen blob; stage 2 the two modules and the ROADMAP at their frozen blobs; stage 3
the result note, candidate `E`. **`BG-3-READ`**: `controls.py check E --freeze F` OK (L, P, R, S, G), the four tokens
printed, the frozen blobs at `E` (`C2`), the exact-head run at `E` green on every job, `C-DES` green at `E`.
**`BG-3-HALTED`**: anything else (`S12`). No outcome changes a manuscript, the census, a probe, a workflow, BG-2's record
or the design package; correctness bands unchanged (consistency axis).

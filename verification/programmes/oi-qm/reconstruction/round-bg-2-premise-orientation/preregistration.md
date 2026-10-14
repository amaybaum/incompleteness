# Reconstruction round BG-2 — does the cited Bekir–Golomb premise hold as the kernel states it?: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from BG-1's freeze (merge `d7d3094d835502f5e7248e406f5dc5952211480c`, #645; preregistration blob
`9a74bcc7b9cacbd70d5e62d0182695ca2cefff85`, drafted at `b78eac87`; never executed), the landed modules cited below and
the design package `verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/` (landed with
#842), which compiles the proposed declarations in the research namespace `OIBridge.PremiseOrientationDesign`, outside
the adopted library; the research branches hold no later BG work
(`origin/research/equivalence:research/equivalence/LEDGER.md:75` is an inventory row). The design package is design
evidence, not this round's execution: the module, probe and `controls.py` named below do not exist yet, and the
statement surface below is proposed and is fixed only by design runs before `F`.
Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round BG-2
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-bg-2-premise-orientation/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-bg-2-premise-orientation/
record AM verification/receipts/BG-2.json
execution A verification/lean-mathlib/OIBridge/TurnpikePremiseOrientation.lean
execution A verification/lean/bg2_orientation_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: bb49766edbaa3b82e27c8255e8c8ba60e311c5be. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, `verification/ROADMAP.md`, landed kernel module or other
round's record changes under any outcome.** BG-1's directory is not a governed path and stays as it stands; nor is
the design package, which stays as it stands.

## What the round is

**Provenance.** AGENTS.md:726–727 at `D`: "A question one of those rounds left open, or froze and never executed, is
taken up by a new native round, which cites the old freeze as provenance and leaves the old record as it stands."
`legacy-records.json` closes BG-1's directory (:32) and pins its one record, blob `9a74bcc7` (:247); V3-12 lists it
among five legacy rounds frozen and never executed (`round-v3-12-retirement-census/preregistration.md:223–229`). BG-1
asked for a kernel proof of `BGIntegerClassification` (TurnpikeScopeTransfer.lean:542), taken as `hBG` by
`spectral_classification_of_BG` (:563, applied :701) and `twoBranch_of_BGClassification` (:826, applied :844).
Nothing landed answers it: none of `BGClassificationAt`, `BGResidual`, `TurnpikeClassification`, `R7-BGC` occurs at
`D` outside BG-1's directory, nor any BG receipt or seal; the design package proves `¬ BGIntegerClassification`
outside the adopted library, and `OIBridge.lean` imports nothing from it. ROADMAP.md:71: `| **P2** | Sign-aware integer
classification | Reconstruction | **OPEN** | repair the premise and justify the classification |`. Moved since BG-1's
base:

| object | at `b78eac87` | at `D` |
| --- | --- | --- |
| TurnpikeScopeTransfer, CongruentReconstruction, HomometricSix, HomometricKill, PiccardBridge, FrequencyMatching, EdgeRigidity, BohrFrequency | blobs BG-1 pins | identical |
| `gap_correspondence_probe.py` / `PROGRAMME.md` | `7a951f22` / `56b39944` (BG-1's pins) | `a46ff78d` / `2b1ea7ed`; the scope block (:953–956) states the unsigned premise refuted and reconstruction conditional on H-BG, and :597 states it refuted and the publication-facing reconstruction conditional on the sign-aware classification |
| `papers/GR.md` / `LEDGER.json` / `ROADMAP.md` | `0258ccb7` / `7fd6a369` / P2 row :68, section :774–781 | `b7d6257b` / `82744f50` / :71, :1116–1120; the two-branch theorem (GR.md:176) assumes H-BG and GR.md:180 states the unsigned premise refuted; the entry `GR:T-d-gauge-completeness-two-branch` (:2602, backlog :3110) and the P2 row and section record the premise refuted and its replacement open |
| `verification/lean/edge_rigidity_probe.py` | `6e334e83`, scope block :20037–20043 | `36dfadab`, block at :14676–14680, stating the unsigned premise refuted; the guard's ancestry and seal clauses, which BG-1's `R7-BGC` clause and `_BGC_*` constants would have joined, are retired (AGENTS.md:722–724) |
| `AGENTS.md` / `OIBridge.lean` | sealing-round text BG-1 quotes / `0bff51eb` | §A.37 a record (:665), §A.39 native rounds (:731) / `9c84d95e`, last import `EqvK2MaxCone` (:268) |
| design package `bekir-golomb-orientation-design/` | absent | `OrientationDesign.lean`, `SignedRepairDesign.lean`, three exact checks with committed outputs, `SHA256SUMS`; workflow `bg2-orientation-design.yml` |

**The correction that frames BG-2.** Reflecting the second ruler (`F' ↦ c − F' ∘ rev`) keeps the seven hypotheses
(order, Golombness and difference set are preserved; the two exclusions exchange — a written argument). The conclusion
`F' (eT (mu a b).2) − F' (eT (mu a b).1) = F (eS b) − F (eS a)`, over relabelings `eS eT : Fin 6 ≃ Fin n`, fixes
the orientation of `mu` (HomometricSix.lean:59); `piccard_realizes_mu` (PiccardBridge.lean:95) exhibits it for the
quoted family in one source/target order only. The design package's `exact_check.py` (standard library, exact
integers) takes `n = 6`, `F = r1 = (0,1,4,10,12,17)` (:51), `F' = 17 − r2 ∘ rev = (0,4,6,9,16,17)`
(`r2`, :55): the hypotheses hold, no pair `(eS, eT)` of the 720 × 720 satisfies the conclusion, and three satisfy it
with the sign reversed. `independent_check.py`, which shares no arithmetic with it but reads `r1`, `r2` and `mu`
with the same parse, reproduces the counts and its control: `(r1, r2)` 3 signed, 0 reversed; `(r1, 17 − r2 ∘ rev)`
0 signed, 3 reversed. The package's `OrientationDesign.lean` proves the refutation and both controls in the kernel,
outside the adopted library (dedicated workflow push run 38572607301 at `2dd2f94c`, axiom reports within
`[propext, Classical.choice, Quot.sound]`): `BGIntegerClassification` is false as stated, `hBG` is refutable in both
consumers, and BG-1's main target and narrowed residual (`∀ n ≥ 6`) were unreachable. The round asks whether the same
declarations, adopted as a module of `OIBridge` and built by the release gate, meet the frozen controls at `E`.

- **Q-REF (kernel).** Is `¬ BGIntegerClassification` provable, by name, from the instance `(r1, 17 − r2 ∘ rev)`?
- **Q-CTRL (kernel).** Is the conclusion attained at `(r1, r2)` (`mu_gap`, :85), and reversed at the instance?
- **Q-EXACT (exact layer).** Do two exact algorithms reproduce the orientation table, family sweep and census?

BG-1's BG0/BG1 are settled above, Q-REF names the premise without BG2's bridge, Q-CTRL subsumes BG3, BG4–BG5 target a
statement Q-REF refutes at six marks. A premise closed under reflecting either ruler, consumers re-derived and the
reversed correspondence excluded (`reflect_conj`, BohrFrequency.lean:265; HomometricKill.lean:442) is a later question;
the design package's `SignedRepairDesign.lean` compiles a candidate outside this round.

## The proposed statement surface

Module `OIBridge/TurnpikePremiseOrientation.lean`, importing `OIBridge.TurnpikeScopeTransfer` and
`OIBridge.PiccardBridge`; namespace `OIBridge.PremiseOrientation`; `open ScopeTransfer HomometricSix`. Proposals:

```lean
def r2refl : Fin 6 → ℤ := fun i => 17 - r2 i.rev
theorem hyps_r1_r2refl : StrictMono r1 ∧ StrictMono r2refl
    ∧ (∀ a b c d : Fin 6, a < b → c < d → r1 b - r1 a = r1 d - r1 c → a = c ∧ b = d)
    ∧ (∀ a b c d : Fin 6, a < b → c < d → r2refl b - r2refl a = r2refl d - r2refl c → a = c ∧ b = d)
    ∧ Finset.image (fun p : AscPair 6 => r1 p.1.2 - r1 p.1.1) Finset.univ
        = Finset.image (fun p : AscPair 6 => r2refl p.1.2 - r2refl p.1.1) Finset.univ
    ∧ (¬ ∃ c : ℤ, ∀ i, r2refl i = r1 i + c) ∧ (¬ ∃ c : ℤ, ∀ i, r2refl i = c - r1 i.rev)
theorem source_difference_cases : ∀ e : Equiv.Perm (Fin 6),
    r1 (e 5) + 2 * r1 (e 0) = r1 (e 1) + r1 (e 2) + r1 (e 4) →
    2 * r1 (e 1) + r1 (e 3) = 2 * r1 (e 0) + r1 (e 4) →
    r1 (e 1) + 2 * r1 (e 3) = r1 (e 0) + r1 (e 2) + r1 (e 5) →
    (r1 (e 1) - r1 (e 0) = 1 ∧ r1 (e 5) - r1 (e 0) = 17)
    ∨ (r1 (e 1) - r1 (e 0) = -6 ∧ r1 (e 5) - r1 (e 0) = -9)
    ∨ (r1 (e 1) - r1 (e 0) = 5 ∧ r1 (e 5) - r1 (e 0) = -8)
theorem reflected_difference_obstruction : ∀ i j k : Fin 6,
    ¬ ((r2refl j - r2refl i = 1 ∧ r2refl k - r2refl i = 17)
      ∨ (r2refl j - r2refl i = -6 ∧ r2refl k - r2refl i = -9)
      ∨ (r2refl j - r2refl i = 5 ∧ r2refl k - r2refl i = -8))
theorem not_muForm_r1_r2refl : ¬ ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2refl (eT (mu a b).2) - r2refl (eT (mu a b).1) = r1 (eS b) - r1 (eS a)
theorem not_BGIntegerClassification : ¬ BGIntegerClassification
theorem muForm_r1_r2 : ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2 (eT (mu a b).2) - r2 (eT (mu a b).1) = r1 (eS b) - r1 (eS a)
theorem revMuForm_r1_r2refl : ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2refl (eT (mu a b).2) - r2refl (eT (mu a b).1) = r1 (eS a) - r1 (eS b)
```

Landed objects, at `D`: `BGIntegerClassification` TurnpikeScopeTransfer.lean:542, `AscPair` :309; `r1`
HomometricSix.lean:51, `r2` :55, `mu` :59, `golomb_r1` :77, `golomb_r2` :81, `mu_gap` :85. The refutation applies its
hypothesis at `6 r1 r2refl` to `hyps_r1_r2refl` and closes with `not_muForm_r1_r2refl`; the controls are
`⟨Equiv.refl _, Equiv.refl _, _⟩` and `⟨Equiv.refl _, Fin.revPerm, _⟩` from `mu_gap` (`Fin.revPerm`: :662). For
`not_muForm_r1_r2refl` the route is the one the design package measured: eight of the conclusion's gap identities give
three linear relations on `r1 ∘ eS`; `source_difference_cases`, by `decide +kernel` over `Equiv.Perm (Fin 6)`
(precedent OrbitIsometryGroup.lean:73), reduces them to three difference patterns; `reflected_difference_obstruction`,
by `decide +kernel` over the 216 target triples, shows `r2refl` realizes none. No `native_decide`; the design sets
`maxRecDepth 100000` and `maxHeartbeats 0`. Eight declarations (`r2refl` and seven theorems), seven `#print axioms`
lines, no displayed equivalence. Import line after
`import OIBridge.EqvK2MaxCone`; census family "the Bekir–Golomb premise as the kernel states it is refuted at six marks
(round BG-2, reconstruction)", `modules: ["TurnpikePremiseOrientation"]`, `status: "kernel-only"`, `manuscript: []`.

## The exact layer

Probe `verification/lean/bg2_orientation_probe.py`, standard library, exact integers, `python3 -I`. **O0** parses
`r1`, `r2`, `mu` and `piccardX`, `piccardY` (PiccardBridge.lean:50, :56) from the kernel files. **O1** the eight
orientation variants of the printed pair (order swapped, either ruler reflected) satisfy the hypotheses. **O2**
exhaustive `eS × eT` counts of signed and reversed solutions per variant; **O3** an independent forced-`eT` algorithm
reproduces them. **O4** on a frozen box of the family the signed form holds at `(X,Y)`, `(Y,X)`, `(RX,RY)`, never at
`(X,RY)`, `(RX,Y)`. **O5** among Golomb rulers of span ≤ 40: no nontrivial homometric pair at 3, 4, 5 or 7 marks;
each nontrivial six-mark ordered pair attains exactly one form. **K1** `mu 0 2 ↔ mu 0 3` gives no solution at
`(r1, r2)`; **K2** the checker rejects `(r1, 17 − r1 ∘ rev)`, `(r1, r1 + 3)`. Drafting values (to be re-measured):
O2/O3 3/0 with zero or two reflections, 0/3 with one, as the design package's two exact checks also record; O4 146
members (`p1 ≤ 7`, `p2 ≤ 29`); O5 248 pairs, 124 signed, 124 reversed, 0 neither. The design package's
`quoted_family_check.py` checks the family's gap identities algebraically in both parameters rather than on a box;
whether O4 takes that form is a design choice. Verdict `VERDICT PREMISE-ORIENTATION-EXACT`; shard `probes_bg2`.

## The decision rules

| Cell | Token | Rule |
|---|---|---|
| Q-REF | `BG-2-PREMISE-REFUTED` | the module's statements are exactly the frozen ones (S1) and resolve to the landed objects (S2); `not_BGIntegerClassification` states `¬ OIBridge.ScopeTransfer.BGIntegerClassification` by name and its proof term names `hyps_r1_r2refl` and `not_muForm_r1_r2refl` (S3); the exact-head run at `E` builds the module with those three prints within `[propext, Classical.choice, Quot.sound]` |
| Q-REF | `BG-2-PREMISE-UNDECIDED` | otherwise |
| Q-CTRL | `BG-2-CONTROLS-PROVED` | S1 and S2 for `muForm_r1_r2` and `revMuForm_r1_r2refl`, and the build at `E` with both prints within the three axioms |
| Q-CTRL | `BG-2-CONTROLS-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `BG-2-ORIENTATION-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for O0–O5, K1, K2, no `FAIL`, `checks: 8, failures: 0` and the verdict line |
| Q-EXACT | `BG-2-ORIENTATION-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `BG-2-READ` when the three cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule

> Earned reading (only when all three cells are positive): `BGIntegerClassification` as stated at
> TurnpikeScopeTransfer.lean:542 is false: the six-mark integer rulers (0,1,4,10,12,17), (0,4,6,9,16,17) satisfy its
> hypotheses, no relabelings realize mu in the orientation its conclusion fixes, and the pair realizes mu reversed.
> `spectral_classification_of_BG` and `twoBranch_of_BGClassification` remain implications with refutable `hBG`.

> Non-inference rule: this round does not show that the 2007 classification, its exceptional family or the two-branch
> theorem of GR is false, nor that a reversed exceptional correspondence is realizable by unitary eigenbases; it
> refutes one formal statement at one instance and formalizes no classification, slice or corrected premise. The
> sites its outcome bears on — GR.md:176 and :180, LEDGER.json:2602 and :3110, ROADMAP.md:71 and :1118,
> PROGRAMME.md:597, the census family "Hamiltonian reconstruction" (lean-manuscript-census.json:144) and the scope blocks
> at edge_rigidity_probe.py:14676–14680, bohr_frequency_probe.py:10082–10085 and gap_correspondence_probe.py:953–956 —
> already state at `D` the unsigned premise refuted, on the design package, and reconstruction conditional on H-BG;
> none of them changes here. The probe is not a kernel proof.

**Premises this round does not source:** the 2007 classification and its scope; the correct form of the exceptional
clause; the exclusion of the reversed correspondence; the integer-to-real passage for any corrected premise.

## The ROADMAP wording the round would license

Not applied by the round. At `D`, ROADMAP :1118 already records the refutation on the strength of #842's design
package. Under `BG-2-READ` with Q-REF positive, that citation may become the adopted
`OIBridge.PremiseOrientation.not_BGIntegerClassification` in `TurnpikePremiseOrientation.lean`. Label and "Unlocks"
cell are the owner's; the obligation stays open in every outcome.

## The controls

- **S1 surface:** preamble, eight declarations in order with frozen signatures, seven prints. Mutations, each failing:
  `r2` for `r2refl` in `not_muForm_r1_r2refl`; the reflection clause dropped from `hyps_r1_r2refl`; the unreversed
  sign in `revMuForm_r1_r2refl`; the premise restated by hand in `not_BGIntegerClassification`; an eighth print.
- **S2, S3:** `BGIntegerClassification`, `AscPair`, `r1`, `r2`, `mu`, `mu_gap`, `golomb_r1`, `golomb_r2`, `piccardX`,
  `piccardY` resolve to the landed declarations at `D`'s blobs; the refutation's proof names its two lemmas (a term
  naming neither fails S3 alone); no print names `sorryAx` or `Lean.ofReduceBool`; K1, K2 are the countercontrols.
- **S4 phrases** (header, result note): "the classification is false", "Bekir–Golomb is refuted", "the two-branch
  theorem is false", "the premise is removed", "the premise is discharged", "kernel proof of" (for the probe).
- **V, G:** three tokens, the earned reading exactly when all are positive; `git diff --no-renames --name-status D E`
  inside the governed paths, nothing under BG-1's directory, `legacy-records.json` unchanged.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; controls and probe are the frozen ones | `C1`: this file's blob at `F`; `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms, without `native_decide` | `C3`: the dispatch run at exactly `E`, every job `success`; the seven prints |
| the refutation names the premise and its two lemmas | `C5`: S1 and S3 in `controls.py check E --freeze F` |
| the exact layer tests the kernel's own objects, replays and renders | `C3`: shard `probes_bg2` green with O0 and the verdict line; the aggregate job green |
| the module is registered, no manuscript changes, the change stays inside the governed paths, BG-1's record untouched | `C4`: the release gate at `E` passing every step; `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design work required before F

1. Build the module on a disposable branch from `D`, porting the design package's declarations into the namespace
   `OIBridge.PremiseOrientation`; record the run, the seven prints, the absence of `sorryAx` and `Lean.ofReduceBool`,
   and the elaboration time of `not_muForm_r1_r2refl` under the design's route.
2. Write the probe (O0's parsing; O4's box and O5's bound frozen; replay 3/3) and `controls.py` with a self-test
   running every mutation; edit workflow, import line and census; dispatch the predicted tree less the result note.
3. Owner choices: slug and module name; whether a corrected premise joins (excluded here; `SignedRepairDesign.lean`
   is a candidate); which change replaces the design-package citations at the sites the non-inference rule lists with
   the adopted module (§A.27: same session once accepted) — none governed here; and whether this round or a later
   one changes `TurnpikeScopeTransfer.lean` itself, whose docstring (:535–541) calls the premise "the ONLY unproved
   input" and whose `spectral_classification_of_BG` carries inline the reduction `SignedRepairDesign.lean` factors as
   `real_to_integer_surrogate`. Doing so here would add it as an `execution M` path and drop it from the identical-blob
   row above; as drafted, no landed module changes under any outcome.

## Stages and outcomes

Stage 1 commits `controls.py`; stage 2 the module, probe, workflow edit, import line and family (proof repairs only);
stage 3 the result note, candidate `E`. **`BG-2-READ`**: `controls.py check E --freeze F` OK, three tokens printed, the
exact-head run at `E` green on every job. **`BG-2-HALTED`**: anything else (`S12`). No outcome edits BG-1's record, a
manuscript, the ROADMAP or a landed module; correctness bands unchanged (consistency axis).

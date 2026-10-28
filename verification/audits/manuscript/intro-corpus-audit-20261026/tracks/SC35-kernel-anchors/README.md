# SC-35 (PR-G): kernel-only results into the manuscripts, with census anchors

Base: `main` at `0d917665`. Branch `corpus/sc35-kernel-anchors`.

## The finding

Three kernel results that the Introduction states, or would state, were carried by no manuscript.
Their census families were `kernel-only`, so the census checked none of them.

| Id | Finding | Source |
|---|---|---|
| CON-41, R-12, B-B6/A-B9 | Main §2.3 understates the kernel. It names only the stochastic-inverse lemma as machine-checked and calls "its composition with P-divisibility" a paper proof. `pIndivisible_of_rooted_identity_return_of_overlap` proves overlap plus identity return implies not P-divisible, for the rooted family with one hidden prior shared by every root. | FINDINGS R-12, OD-4; VERIFY B-B6/A-B9 |
| CON-43, R-13, OD-5, B-B7/A-B6 | No manuscript states the routed-readback conclusion. Two readings are formalized and they are incomparable. OD-5 makes the storage-time reading primary. | FINDINGS R-13, OD-5; VERIFY A-B6/B-B7 |
| CON-28, R-09, O-6 | `finiteRootedRealizable_iff_pper` classifies all-time realizability of rooted families. Main's consolidation remark omits it, and its open item (a) still lists the rooted case as open. | FINDINGS R-09, OD-4 |
| OD-4 (census) | The four families were `kernel-only`. The registry's `manuscripts` list omits the Introduction. | FINDINGS OD-4; VERIFY B-B6 |

Every Lean statement cited below was read before any prose was written. The prose transcribes it and
does not go beyond it. `sc35_check.py` checks the transcription mechanically; its output is in
`sc35_check.out`.

## Per claim

### 1. The recurrence theorem's kernel status (CON-41)

- **Original** (`papers/Main.md:139`, at `0d917665`):
  > (kernel: the lemma is `isPermMatrix_of_stochastic_inverse` in `OIBridge/EquivalenceChain.lean`; its composition with P-divisibility and the step from two positive-probability histories with a common endpoint to a non-permutation rooted map are proved on paper)
- **Defect.** The text understates the kernel. "Its composition with P-divisibility" is kernel-proved by another route:
  `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`). That theorem
  takes an identity return `rootedMap R n = 1` and an overlap at `s < n` of two distinct roots' rows,
  `0 < rootedMap R s a x` and `0 < rootedMap R s b x`, and concludes `PIndivisibleWithin n`.
  - Its setting is `RootedRealization`: a bijection `step : V × H ≃ V × H`, and one prior on `H`.
    The prior is nonnegative and normalized, has no support condition, and is shared by every root.
  - `V` and `H` are finite.
  - Main stated the general rooted form nowhere.
- **Correction.**
  - Main §2.3 gains **Theorem (overlap and return)** (`Main.md:143`). It states every hypothesis of the
    kernel theorem:
    - finite visible and hidden sets;
    - a bijection;
    - one hidden prior from which the hidden state is drawn whatever the root, not required to have full support;
    - rooted maps for every root;
    - `Γ_n = I`;
    - an overlap of two distinct roots' rows at some `s < n`.
  - Its conclusion is the kernel's: the rooted family is not P-divisible on {0,…,n}.
  - It carries a total-variation proof and a kernel parenthetical. The parenthetical also cites the
    matrix form, `pIndivisible_of_identity_return_of_overlap`, which assumes only that `Γ_s` is row-stochastic.
  - The history-readback theorem's parenthetical now says what is in the kernel and what is on paper:
    - in the kernel: the lemma, and the final clause through the new theorem;
    - on paper:
      - the step from histories to a non-permutation `Γ_s`;
      - the step from a non-permutation square stochastic matrix to two overlapping rows;
      - `Γ_L = I`.
  - The theorem statement at `Main.md:137` is unchanged; its fingerprint is `88428cc80fcebe48`.
- **Downstream.**
  - The Introduction's Theorem 3 (R-12) can keep "[Main §2.3]", since Main now states the general rooted form with a census anchor.
  - Coverage:
    - new entry `MAIN:T-overlap-return`, K3;
    - `MAIN:T-history-readback-finite-recurrence-implies` stays at P, its base grade. The step that distinguishes this theorem, two histories with a common endpoint giving a non-permutation `Γ_s`, has no Lean statement, and the final clause is credited at K3 to the separate `MAIN:T-overlap-return` entry. The entry's note records this: the final clause is kernel-proved through `MAIN:T-overlap-return`; the history-to-non-permutation step, the non-permutation-to-overlap step and `Γ_L = I` stay on paper. Its checks list no Lean theorem, since the coverage tool forbids one in a P row. The review of `7b25ac69` reversed an interim K2 grade (F1).

### 2. Routed readback (CON-43)

- **Original.** No manuscript states it.
  - `papers/GR.md:52` carries the clause: "a visible-history record written into hidden boundary degrees is routed back into future visible conditionals within the accessible window".
  - Main §1.3 (`Main.md:80`) names the read-write cycle as "a property to be independently demonstrated".
- **Defect.**
  - The kernel conclusion appeared in no manuscript.
  - The Introduction's draft Appendix A cited the seed-conditioned predicate for a gloss that is the storage-time reading. The two predicates are incomparable: `storageReadback_not_implies_routedReadback` (`PhysicalC4StorageReadback.lean:488`) and `routedReadback_not_implies_storageReadback` (`:689`).
- **Correction.** Main §2.3 gains a *Routed readback* paragraph (`Main.md:147`).
  - It gives the clauses shared by both readings, transcribed from `RoutedReadback` and `RoutedReadbackAtStorage`:
    - write;
    - store;
    - read;
    - reappearance;
    - timing `0 < w ≤ s < t ≤ K`.
  - It defines the two readings by the hidden law each uses:
    - `Law(H_s | X_s = x, X_0 = a)` for `rootedStatePosterior`;
    - `Law(H_0 | X_s = x, X_0 = a)` for `rootedPosterior`.
  - It states the conclusion under either reading: not P-divisible on {0,…,n} for every `n > s` with `Γ_n = I`, and so for some `n`.
  - The storage-time reading is listed first, per OD-5:
    - storage-time: `routedAtStorage_forces_return_indivisibility` and `routedAtStorage_forces_indivisible_somewhere` (`PhysicalC4StorageReadback.lean:244, :256`);
    - seed-conditioned: `routed_forces_return_indivisibility` and `routed_forces_indivisible_somewhere` (`PhysicalC4Discharge.lean:109, :122`);
    - `rootedMap_periodic` and `rootedMap_zero`.
  - It states that both proofs use only the store clause's positivity conditions, so both are instances of the overlap-and-return theorem, at a return horizon and not at an accessible window.
  - It states the incomparability exactly as exhibited: each reading holds at `K = 2` on a carrier where the other fails at `K = 2`. For the core carrier the seed reading fails at every `K`; the separating carrier is certified only at `K = 2`.
  - It states that the clause is not established at a physical cut, in either reading.
- **Downstream.**
  - R-13 can cite both declarations, with the storage-time one first.
  - GR:52's "Not presently discharged" stays true and is unchanged.
  - Main §1.3 is unchanged.

### 3. Rooted classification (CON-28)

- **Original** (`papers/Main.md:634`):
  > The honest open questions are (a) exact gluing for recurrent target families — which compatibility conditions on the per-horizon realizations suffice — and (b) …
  - `Main.md:727` (status ledger): "recurrent-family gluing and pre-recurrence window approximation open".
  - `verification/ROADMAP.md:1571`: "Recurrent-family gluing and pre-recurrence-window approximation remain open in `Main.md`".
- **Defect.**
  - For rooted visible maps the all-time question has an exact kernel answer: `finiteRootedRealizable_iff_pper` (`RootedClassificationAllTime.lean:192`).
  - Item (a) listed the rooted case as open.
- **Correction.** The consolidation remark (`Main.md:640`) states the classification with its hypotheses.
  - The hypotheses:
    - finite `C_V`;
    - some finite `C_H`;
    - one bijection;
    - one prior shared by every root, not required to have full support;
    - equality at every `t ≥ 0`.
  - The condition: `Γ_0 = I`, every `Γ_t` row-stochastic, and `Γ_{t+M} = Γ_t` for some `M > 0`.
  - Under §A.34 each direction has its own witness:
    - forward: `pper_of_finiteRootedRealizable` (`RootedClassification.lean:339`);
    - converse: `pper_has_responseRealization` (`RootedClassificationAllTime.lean:162`);
    - the two directions are assembled in `finiteRootedRealizable_iff_pper`.
  - Item (a) is narrowed to "exact all-time gluing for recurrent families of multi-time laws".
  - The ledger row and the ROADMAP entry carry the same narrowing.
  - The self-assessing "honest" is dropped (§A.32).
- **Downstream.** R-09 can use "multi-time laws", and O-6 can cite [Main §3.4] for the rooted case.

### 4. Census (OD-4)

- The four families move from `kernel-only` to `current` in `verification/lean-manuscript-census.json`, with Main anchors (§A.35):
  - recurrence horizon (base `:719`);
  - physical C4 discharge (`:728`);
  - physical C4 round 2 (`:737`);
  - rooted classification (`:801`).
- Each family's note gains one sentence saying where Main carries it.
- `verification/audits/manuscript/lean-manuscript-census.md`:
  - the two existing rows move to `current`;
  - rows for the two physical C4 families, missing from that table, are added.
- Guards `R7-RCH` and `R7-RCL` (`verification/lean/edge_rigidity_probe.py`, base `:6658`, `:6897`) pinned `kernel-only` and the absence of the module names from every manuscript.
  - Both are re-pinned to the new state:
    - the family is `current` with Main anchors;
    - the census row reads `current`;
    - Main's statement carries every hypothesis.
  - Each audit's vocabulary (`RECURRENCE-TIGHTNESS`, `N_CR`, `horizon_verdict`, `PIndivisibleWithin`, `FiniteRootedRealizable`, `PPer`, `OI-ROOTED-CLASSIFICATION`) is still forbidden in every manuscript.
  - The module names `RecurrenceHorizon` and `RootedClassification` are allowed in `papers/Main.md` only, because Main cites module paths. They stay forbidden in every other manuscript the guards scan.
  - R7-RCH also pins that the paragraph starting `*Routed readback.*` contains "not an accessible window" and "is not established".
  - Mutation test: `sc35_guard_mutations.py`, with its output in `sc35_guard_mutations.out`. Each of six mutations is applied one at a time and the file restored byte for byte. Each makes its guard FAIL:
    - a module name added to GR, once for each module;
    - each of the two routed-readback phrases altered;
    - the support hypothesis dropped from the theorem;
    - the support hypothesis dropped from the classification.
- `R7-C4R` is untouched and passes. Main cites no `CausalReadback` identifier, so that family stays `kernel-only`.
- **Introduction in the `manuscripts` list: not added.**
  - No tool reads the list. `tools/lean_manuscript_census.py` globs every `papers/*.md` and `book/*.md`, and no other tool or guard reads the key.
  - `papers/Introduction.md` does not exist on `main`.
  - Once it lands, the census scans it automatically. Its identifiers are resolved only if it uses the `(kernel: …)` parenthetical form.

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| Main.md:139 | composition with P-divisibility "proved on paper" | final clause kernel-checked via the new theorem; three named steps on paper | RecurrenceHorizon:148 |
| Main.md:143 (new) | — | Theorem (overlap and return), with proof and kernel note | RecurrenceHorizon:119, :140, :148 |
| Main.md:147 (new) | — | Routed readback, storage-time reading primary, incomparability, not established at a physical cut | PhysicalC4StorageReadback:244, :256, :488, :689; PhysicalC4Discharge:109, :122; RootedClassification:123, :135 |
| Main.md:640 | (a) exact gluing for recurrent target families | rooted classification with per-direction witnesses; (a) for multi-time laws | RootedClassification:339; RootedClassificationAllTime:162, :192 |
| Main.md:733 | recurrent-family gluing … open | rooted maps classified (kernel); multi-time-law gluing … open | as above |
| ROADMAP.md:1571 | Recurrent-family gluing … remain open | rooted case classified; multi-time-law gluing … remain open | as above |
| lean-manuscript-census.json | 4 families `kernel-only` | `current`, 18 Main anchors | §A.35 |
| lean-manuscript-census.md | 2 rows `kernel-only`, 2 rows absent | 4 rows `current` | registry |
| edge_rigidity_probe.py R7-RCH, R7-RCL | pin `kernel-only`, no manuscript mention | pin `current`, the Main statement's hypotheses, the routed-readback scope, no audit vocabulary, module names in Main only | registry |
| coverage/LEDGER.json | history theorem P; no entry for the new theorem | history theorem still P, its note naming the kernel route and the paper steps; `MAIN:T-overlap-return` K3 | Lean names above |
| Main.tex / Main.pdf | — | rebuilt; 96 → 98 pages, median 3274 → 3318 characters per page | `sh ./build.sh Main` |

## Evidence level of each corrected claim

| Claim | Level |
|---|---|
| Overlap and return implies not P-divisible on {0,…,n} | kernel (exact statement; K3) |
| History readback + recurrence: final clause from an overlap and `Γ_n = I` | kernel, through the overlap-and-return theorem; the history theorem itself is graded P |
| History readback + recurrence: histories → non-permutation `Γ_s`; non-permutation → overlap; `Γ_L = I` | paper |
| Routed readback, either reading, implies indivisibility at every return after `s`, and somewhere | kernel |
| The two readings are incomparable | kernel (exhibited carriers at `K = 2`) |
| The realization clause holds at a physical cut | not established (stated as such) |
| Rooted all-time classification, each direction | kernel |
| Exact all-time gluing for multi-time laws; pre-recurrence approximation | open |

## Re-grep

`sc35_check.py` section 4 checks the following over `papers/*.md`, `book/*.md` and `verification/ROADMAP.md`:

- **Removed, 0 hits:** each of the four superseded phrasings.
- **Added, once each:**
  - Main: the new theorem header and the *Routed readback* paragraph;
  - Main: the item (a) narrowing and the ledger-row narrowing;
  - ROADMAP: the narrowing.
- **Identifier counts:**
  - `pIndivisible_of_rooted_identity_return_of_overlap`: Main 2;
  - `routedAtStorage_forces_indivisible_somewhere`: Main 1;
  - `routed_forces_indivisible_somewhere`: Main 1, ROADMAP 1 (pre-existing P1 row);
  - `finiteRootedRealizable_iff_pper`: Main 1, ROADMAP 1.

Checked mirrors, unchanged, because none states a proof status or the open item:

- Book `ch01-observation.md:181` and `FULL.md:525` (Readback theorem);
- `glossary.md:119` and `FULL.md:6719` (P-indivisibility);
- `ch01` §1.5 and `FULL.md:437–463` (uniform-prior theorem);
- `ch07-gravity.md:30` and `FULL.md:1909` (C4 not discharged at the cosmological cut);
- Explainer `:135`, `:272`, `:351`, `:1005`, `:900`.

Each of these is consistent with the corrected Main text.

## Made conditional or removed

- Nothing is made conditional. Nothing is removed except the rooted case from open item (a), which is now a theorem.
- The routed-readback conclusion is stated as an implication from the clause. The clause itself is stated as not established at a physical cut.

## Requires formal change

None. No Lean file is edited; `sc35_check.py` section 5 checks this.

## Cross-unit dependencies

These are shared statements this unit changes:

- **Main §2.3, `Main.md:139`.** The kernel parenthetical of the history-readback theorem. The statement at `:137` is unchanged.
- **Main §2.3, `Main.md:143–147`.** New text between *Scope* and **Genericity**.
  - The open branches `corpus/sc28-assumption-scope`, `corpus/sc31-period-growth` and `corpus/sc34-cycle-ergodicity` edit `Main.md:151`, the continuous-time paragraph. That line is within a few lines of this insertion, but the hunks do not overlap.
- **Main §3.4.** The consolidation remark (`:634` at base) and the status-ledger row (`:727` at base). The SC-33 PR edits `:700`, a different line.
- **Coverage ledger.** The `MAIN:T-history-readback-finite-recurrence-implies` entry, and a new entry inserted after it. Several open PRs edit `LEDGER.json` (SC-29, SC-31, SC-32, SC-34), but not this entry.
- **Census registry and census note.** The four family entries and rows. SC-29/SC-31 edit the registry at base `:411` and the note at `:59` and `:132`.
- **Guard file.** R7-RCH and R7-RCL. SC-29/SC-31 edit R7-CTN (about `:3001–3044`), a different block.
- **`verification/ROADMAP.md:1569–1573`.**
- **Merge check.** `git merge-tree` of this branch against each open `corpus/*` branch (sc17, sc22, sc28, sc29, sc31, sc32, sc33, sc34) merges without conflict; a textual check only.
- **Introduction r32.** R-09, R-12, R-13 and O-6 depend on this unit's Main text:
  - "[Main §2.3]" for Theorem 3 and for routed readback;
  - "[Main §3.4]" for the rooted classification;
  - "multi-time laws" in open problem (3).

## Open, for #970

- The grading question. The history-readback theorem stays at P because its distinguishing step has no Lean statement, though its final clause is kernel-proved through `MAIN:T-overlap-return`. Whether such a partial kernel route should ever raise a grade is for the owner to decide.
- A kernel statement of the history step: two positive-probability histories with a common endpoint, under a visible prior independent of `μ_H`, give an overlap at some `s ≤ min(k, L−1)`. Proving it, with the non-permutation-to-overlap step and `Γ_L = I`, would give a Lean statement for the whole theorem through the overlap route.
- Exact all-time gluing for recurrent multi-time laws, and quantitative pre-recurrence approximation.
- Whether either routed-readback reading holds at a physical cut. ROADMAP P1 stays OPEN.

## Checks

| Check | Result |
|---|---|
| `sc35_check.py` (run under `python3 -I`) | OK |
| `sc35_guard_mutations.py` (run under `python3 -I`) | OK, 6 of 6 mutations caught |
| `tools/lean_manuscript_census.py` | OK, 24 current families |
| `tools/release_gate.py` | all steps pass except `lean-axioms`, which needs the local toolchain |
| `tools/coverage_check.py` | OK, 129 canonical statements |
| `verification/lean/edge_rigidity_probe.py` | ALL CHECKS PASS |
| §A.32/§A.33, revision-voice and caps scan of added lines | 0 hits |
| Secrets and local-path scan | 0 hits |

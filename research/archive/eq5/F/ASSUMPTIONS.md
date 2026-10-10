# Assumptions ledger for `kt4_forward_ie1` (EQ4-F, design only)

Object: `OIBridge.FourCopy.kt4_forward_ie1` (`FourCopyHeadline.lean`), as built in design run 4: run 37948419430
(workflow_dispatch, attempt 1) on `ff9c3a35`, on the disposable branch `claude/network-tool-access-8jtdhm`.

    kt4_forward_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
      (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
      (hcl : ∀ p, IsClosed (K p)) (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
      (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
      (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p))

Base for SUPPLIES: certified main `bcbc516f`. Nothing here is adopted, frozen or governed.

## 0. Kernel status of the theorem

**Proved, conditional on its five hypotheses.** In run 4, `#print axioms kt4_forward_ie1` reports
`[propext, Classical.choice, Quot.sound]`. The report covers the theorem's whole dependency closure, so no lemma it
reaches uses `sorry`.

- `FourCopyIE1`: 58 prints, all standard. No `declaration uses sorry`.
- `FourCopyHeadline`: 6 prints, all standard: `ie1_all`, `parity_all`, `kt4_general_ie1`, `kt4_forward_ie1`,
  `kt4_forward_ie1_kt4`, `kt4_forward_ie1_lt`.
- Bipolar 8, Bridge 14, Core 1, Defs 2, Euler 7, Local 26, Parity 17, Tables 16: all standard.
- `FourCopyPackage`: 3 prints with `sorryAx` (`fourCopyCoherent_of_kt4Cone`, `kt4_forward`, `kt4_forward_lt`) and 36
  `declaration uses sorry`. This is the Pauli stage, which was not started; no module on the headline path imports it.
- Build: completed, 3655 jobs, no errors. FourCopyIE1 has 17 warnings, all linter warnings: 16 report fallback
  alternatives inside `first | … | …` that were never needed, and one is a `<;>` style lint.
- Release gate: FAILED at exactly two steps, every other step passing (42 receipts hold, 303 legacy records intact).
  - `lean-axioms`, 6 problems: the Package's three `sorryAx` prints, two problems each. This is the Pauli stage.
  - `lean-manuscript`, 11 problems: the eleven FourCopy modules have no registry family. These are the unregistered
    modules; registry changes were not authorized.
- Reproduction:
  - `lean_axiom_check --log` on the fetched job log gives the same three SORRY and three AXIOM entries (the 5771
    SILENT entries are artifacts of the log's 5000-line tail);
  - `lean_manuscript_census` at `ff9c3a35` lists the same eleven modules as in run 3.
- Run 4 is a design run on a disposable branch: nothing in it is certified.

The eleven Pauli-free path obligations are G5, G9a–G9d, G10, G10′, G11 and G12, proved in run 3, and G7 (`link_mem`)
and G14b (`parity_witnesses`), proved in run 4. Run 4 also proves G6 (`cross_rel_symm`, off the path), G7's two table
identities (`cnot_prodState_rot`, `actC_rotWord_phiW`) and 35 helper declarations, each with its own print.

## 1. Columns

- **USES.** Where the proof consumes the hypothesis, read from the code at `ff9c3a35`. Every consuming lemma prints
  standard axioms in run 4.
- **SUPPLIES at the base.** As in the EQ4-SOURCE and EQ5-PREM ledgers:
  - **[K]** landed;
  - **[T]** transported;
  - **[U]** unsourced, with a route or with a countermodel.
- **Cannot be dropped?** A model of the other four hypotheses in which the conclusion fails. Such a model shows that the
  other hypotheses do not suffice. It does not show necessity.
- **Necessary?** Under the P/A/C rule:
  - "not necessary" is shown by a model of the other hypotheses and the conclusion in which the hypothesis fails;
  - "necessary" needs a proof that the other hypotheses and the conclusion imply the hypothesis.

## 2. The hypotheses

### hcls — N-CLASS gates

**USES**
- (R) `inv_mem_of_orth`, through `NClass.ipW_map`.
- `bell_mem` and `bell_mem_dual`.
- `ie1_all`:
  - orthogonality of A and B feeds `cross_rel`, `rot_of_words` and G9a–d;
  - the gate form at products feeds `link_mem`, through `NClass.apply_prodState`.
- `parity_witnesses`: the bit `orient A B`, and the chart `chartOf A B`.

**SUPPLIES:** **[U] route.**
- EQ2-B's derivation IsNot ∧ CtrlGate (∧ NormPres) ⇒ N-CLASS is written with exact certificates and is unbuilt in Lean.
- Its K1 inputs, `IsNot` and the native-gate and entangling hypotheses, are unsourced (ROADMAP:995–996).

**Cannot be dropped?** Yes [W].
- Model: uniform Q3 with `cnot` gates, A_13 = reflY, and every other local I.
- The other hypotheses hold, and EvenCycle fails.

**Necessary?** No [W + X O2].
- Model: N = id at every pair, every local I, uniform Q3.
- hadm and hcl hold. hgate holds, since the identity preserves K. H holds, cited as for the D-gate model below. The
  conclusion holds: IE₁ for Q3, and every orientation bit is false.
- NClass fails at every pair. An N-CLASS gate maps a product state to `bellOf A B` (`NClass.bell_state`), which has
  table rank 4 because `phiW` has rank 4 and the locals are invertible. The identity returns the product, of rank 1.

### hadm — admissible pair cones

**USES**
- Products in K: `bell_mem`, `link_mem`, `parity_witnesses`, and `bidual_of_adm` (for nonemptiness).
- K ⊆ maxCone:
  - Lemma B1, through the slice bounds;
  - `bell_mem_dual`, through `sharp_mem_dualW`;
  - `parity_witnesses`.
- Convex cone: the bipolar step `dualW_dualW`, and the scaling in Lemma B1.

**SUPPLIES:** **[T].** Transported from COMP-1's body bounds. The two-copy composite K2 is OPEN (ROADMAP:1001–1006).

**Cannot be dropped?** Not tested.

**Necessary?** No [W]. The model is degenerate and settles only the logical question.
- Model: K = {0} at every pair, with `cnot` gates and identity locals.
- hcls, hcl and hgate hold.
- H holds:
  - its cone-independent fields come from any COMP-1 pre-composite [K];
  - its positivity and token clauses hold vacuously, since every pair body is empty.
- IE₁ and EvenCycle hold.
- CandidateCone fails: no product state lies in {0}.

### hcl — closed pair cones

**USES**
- (R) `inv_mem_of_orth`, at its last step: a limit of forward iterates lies in K.
- `bidual_of_adm` gives `hbi`, which `cross_rel`, G9a–d and `ie1_of_dualW` consume.

**SUPPLIES:** **[U] countermodel.** The closure foil, below [X SOURCE s2 C1–C3 + W].
- A stage-completion body is closed by definition [K `body_isClosed`], so a pair cone given as such a body would be
  closed.
- ROADMAP:1014 states K∞-Act for the elementary ball only. No pair-level version is stated.

**Cannot be dropped?** **Yes. New:** the ledger previously had "not established" [X premise K1–K4 + X SOURCE s2 C1–C3 + W].
- Model: uniform K_cl = int Q3 ∪ conv(SEP ∪ cnot SEP), with `cnot` gates and identity locals.
- hcls, hadm and hgate hold [SOURCE §3.8, W].
- H holds [W]:
  - cl K_cl = Q3 and a dual is unchanged by closure, so dualW K_cl = dualW Q3;
  - FCC for uniform K_cl is therefore FCC for uniform Q3 [X SOURCE s1 I1 + W P5], restricted to K_cl;
  - SOURCE §3.6 (⇒) builds KT4 for admissible cones, and `KT4.toCore` gives KT4Core.
- hcl fails, and so does IE₁:
  - the target-side rotation R_H = [[0,0,1],[0,−1,0],[1,0,0]] ∈ SO(3) carries `phiW` = cnot(prodState xplus z3) ∈ K_cl
    to T_ψ, the table of ψ = (|00⟩+|01⟩+|10⟩−|11⟩)/2 [X K1, K2];
  - T_ψ ∉ K_cl. Independent evidence: X SOURCE s2 C1–C3, and X K3 (a rank-one state, of table rank 4, whose cnot
    image has table rank 4); K4 is the countercontrol;
  - so actT R_H '' K_cl ≠ K_cl.

**Necessary?** **Yes, relative to the other four hypotheses, by a written argument [W + L] that is not kernel-checked
(§4.1).**
- The other hypotheses and IE₁ force each pair cone to be Q3 or its twin, and both are closed.
- The necessity runs through hgate. Without hgate, uniform int(maxCone) ∪ Q3 with `cnot` gates satisfies hcls, hadm, H
  and the conclusion, and it is not closed [W]: idW lies in maxCone but not in this set.

### hgate — forward gate preservation

**USES**
- At the cone level, only in (R) `inv_mem_of_orth`, which iterates the gate along an orbit to derive hinv.
- At products only: `bell_mem`, `link_mem`, and `parity_witnesses` through `bell_mem`. This was checked on every
  occurrence in the headline-path modules.

**SUPPLIES:** **[U] countermodel.** Unchanged:
- MAX and MIN violate it;
- PREM Part B refutes every non-restating formulation it tested.

**Cannot be dropped?** Yes, by the D-gate model. Unchanged.
- Uniform Q3, with `cnot` at 01, 23 and 02, and actT reflY ∘ cnot at 13.
- hgate fails at 13, and EvenCycle fails.

**Necessary?** **No. New** [X premise M1–M4 + X SOURCE s2 G1 + W].
- Model: uniform maxCone(eball 3), with `cnot` gates and identity locals.
- hcls holds. hadm holds: maxCone contains the products [K `prodState_mem_maxCone`] and is a convex cone. hcl holds:
  maxCone is an intersection of closed half-spaces.
- H holds [W]:
  - dualW(maxCone) is the closed cone generated by the product effect tables (bipolar);
  - on product effect tables, famI factorizes as (αᵀXβ)(γᵀYδ) ≥ 0 [X M2];
  - the countercontrol M3 shows that entangled effects would give −2;
  - so FCC holds, and SOURCE §3.6 (⇒) gives KT4, hence KT4Core.
- The conclusion holds:
  - maxCone is invariant under local rotations, because the rotation's transpose carries ball effects to ball effects
    [X M4 + W];
  - every orientation bit is false.
- hgate fails: idW ∈ maxCone [X SOURCE s2 G1], while cnot idW = chainW takes −1/2 at the sharp pair u = (−1,0,0),
  w = (0,0,−1) [X M1].

### H : KT4Core — the four-copy data

**USES:** Lemma B1 only. Every field is consumed. Unchanged.

**SUPPLIES**
- The PreComposite parts are [K].
- posBA and posAB are [U] route (the anchor sum).
- tokA and tokB (`TokenCoherent` at product states) are **[U] countermodel**: no structure with three or more tokens
  exists at the base [X SOURCE s0], and PREM Part A is not sourced.

**Cannot be dropped?** tok: yes [X SOURCE s1]. M_ρ and M_tw satisfy every other hypothesis, and the conclusion fails.

**Necessary?** tok: no [X SOURCE s1 I1–I2 + W]. M_id and M_T satisfy every other hypothesis and the conclusion, while
tok fails.

### Derived, not assumed (unchanged)

- hinv, from hcls ∧ hcl ∧ hgate by (R). This is sufficiency only.
- hbi, from hadm ∧ hcl.
- hbs and hbe: the Bell table lies in K and in dualW K.
- FCC, from H by Lemma B1.

## 3. Summary

| hypothesis | SUPPLIES at `bcbc516f` | cannot be dropped? | necessary? |
|---|---|---|---|
| hcls | [U] route (EQ2-B unbuilt; K1 inputs unsourced) | yes [W] | no [W + X] (identity gate) |
| hadm | [T] (COMP-1 bounds; K2 OPEN) | not tested | no [W] (K = {0}, degenerate) |
| hcl | [U] (closure foil) | **yes** [X + W] (uniform K_cl fails IE₁) | **yes, relative to the other four** [W + L, §4.1] |
| hgate | [U] (MAX, MIN; PREM Part B) | yes (D-gate) | **no** [X + W] (uniform maxCone) |
| H: tok | [U] (M_ρ, M_tw; PREM Part A) | yes [X SOURCE] | no [X SOURCE] (M_id, M_T) |

**Merely sufficient.** hcls, hadm, hgate and tok are sufficient for the current proof, but each fails in some model of
the other hypotheses together with the conclusion. Each could in principle be replaced by a weaker premise.

**Necessary.** hcl is the only hypothesis shown necessary relative to the others. The argument is written, uses one
literature fact, and is not kernel-checked.

## 4. Routes to an unconditional result

### 4.1 Written argument: IE₁ with hcls, hadm and hgate forces Q3 or its twin [W + L]

This uses no H, no tok and no hcl. The exact steps are checked in `premise/classification_probe.py` (4/4).

1. **Reduce to a reflection-pattern gate.** Write each local as a rotation times reflY^ε. IE₁ absorbs the rotations, so
   N K ⊆ K becomes N₀ K ⊆ K, where N₀ = (reflY-locals) ∘ cnot ∘ (reflY-locals).
   - N₀ is a signed permutation of the 16 table entries, of order 2 or 4 [X C2]. So N₀ K = K.
   - Conjugating by the pre-local reflections reduces N₀ to actC reflY^α ∘ actT reflY^β ∘ cnot.
2. **Mixed patterns, (α, β) = (0, 1) or (1, 0).** The orbit of `prodState xplus z3` leaves maxCone [X C3, O1, M1]: it
   reaches idW, then chainW. So no admissible K exists.
3. **Matched patterns, (α, β) = (0, 0) or (1, 1).**
   - The full transpose commutes with cnot [X C1], so in both cases the conjugated cone is invariant under the local
     rotations and under their conjugates by cnot.
   - Local unitaries and CNOT generate every two-qubit unitary [L: Kraus–Cirac 2001, Khaneja–Glaser 2001, Vidal–Dawson
     2004; not verified here]. So the cone is unitarily invariant.
   - It contains the pure products, hence every pure state, hence Q3.
   - It lies in maxCone and is unitarily invariant, hence lies in Q3.
   - So K is Q3, or its twin according to the orientation bit [X C4 consistency], and K is closed.

### 4.2 What each hypothesis still needs

- **hcl and hgate.** One route covers both: a pair cone given as the closed body of a stage completion on which the
  pair gate acts as reversible operation data.
  - Closedness is then [K `body_isClosed`], and gate preservation is the action.
  - This needs a pair-level analog of K∞-Act, which the ROADMAP does not state; it states K∞-Act for the elementary
    ball (ROADMAP:1014).
  - hcl is necessary relative to the rest (§4.1), so it has to be supplied; it cannot be removed.
  - hgate is not necessary, but no weaker sourced premise is known.
- **tok.**
  - There is no structure with three or more tokens at the base.
  - One route is Theorem A (IP₁ᴮᴬ ∧ LT ∧ one body ∧ PairAdm ⇒ tok), which is written and has unsourced inputs.
  - Another is a premise such as TokProdState, equivalent to tok relative to the rest (SOURCE §3.7). It would need the
    owner's adoption.
- **hcls.** Building EQ2-B in Lean would reduce it to its K1 inputs, which remain unsourced (ROADMAP:995–996).
- **hadm.** It needs K2 (ROADMAP:1001–1006).

**Shortest route.** No hypothesis can be removed outright. The four groups rest on four distinct open items:
- the pair-level completion action;
- a three-token structure;
- K1;
- K2.

The pair-level completion action is the single item that would supply two hypotheses at once (hcl and hgate).

### 4.3 Note for the Pauli stage (not started)

§4.1 identifies each pair cone with Q3 or its twin from IE₁, hadm, hcls and hgate alone, by unitary universality. No
four-copy input enters. That is the Pauli stage's content, and it was not started in Lean or CI. It is recorded here
only because it settles the status of hcl.

## 5. What is not claimed

- No hypothesis is adopted, and none is claimed sourced.
- "Necessary" is used only for hcl. It is the conclusion of a written argument with one literature ingredient, and it
  is not kernel-checked.
- Every model above is a model of the stated hypothesis set only.
- Nothing here says that the observational axioms force quantum cones.

## 6. Evidence (sha256, first 16 hex digits)

| artifact | hash | result |
|---|---|---|
| `run4_bridge_job.log` (job 113880632651, 5000-line tail) | `55746948a035d908` | build OK; prints as in §0 |
| `parse_run.py` | `809a66371e5c9cef` | per-module counts |
| `run4_axiomcheck.out` | `b54dc52d1304e2e0` | 3 SORRY + 3 AXIOM (Package) + truncation SILENT |
| `run4_census_local.out` | `9bd9d4af92774442` | 11 UNCLASSIFIED FourCopy modules |
| `stmt_check.py` | `50c544a9f72d6661` | IE1 23/23 and Headline 6/6 statements identical to `bef3c68a` |
| `precheck_hommap.py` / `.out` | `f2af7f46ad471d2d` / `408e3c28acbc0baf` | 10/10, first run |
| `premise/premise_probe.py` / `.out` | `439ee5aa7c899878` / `f36b4e630f2c8371` | 14/14, first run; replay identical |
| `premise/classification_probe.py` / `.out` | `a34d442d9dff4de4` / `a58642edda368f45` | 4/4, first run; replay identical |
| `FourCopyIE1.lean` blob at `ff9c3a35` | `65cc5bcb3c92` | 58 declarations, 58 prints |
| `FourCopyHeadline.lean` blob at `ff9c3a35` | `a254873d8d8f` | header comment only changed |

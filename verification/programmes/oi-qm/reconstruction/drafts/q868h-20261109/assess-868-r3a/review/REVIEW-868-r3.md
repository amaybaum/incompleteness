# Independent review of ASSESS-868 r3 (#868 re-assessment: joint-test validity and composition)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09), fresh independent reviewer of r3.** This review
authorizes nothing. An ACCEPT adopts no premise and authorizes no further unit, edit, freeze, dispatch or merge.

- **Under review:** `ASSESS-868.md` r3, sha256 `4cd2fb04da73060cb0e4ffac0287fd0a1f48ace60f9361fec5e57e3cf50f3228`, and
  `DISPOSITIONS-r3.md`, `514061d81a3eb40ca669c14089257a71fb1bc1de542aac8948e64b6de58e2b2b`. I confirmed both before
  reading. Also confirmed:
  - `review/REVIEW-868-r2.md` `d37cb1b1…8f11` and `r2/ASSESS-868.md` `f4873a44…ff34ae`;
  - `probes/r2_validity_scope.py` `cedf6112…7101` (edited) and `r2/probes/r2_validity_scope.py` `60095dc0…0ea2`
    (original);
  - `probes/r3_scope_checks.py` `e6afb063…9575`, `.out` `394b6fd8…`, `.run1.out` `ec76650a…`;
  - `rv_868_checks.py` `b460abd4…` and `rv2_868_checks.py` `791556c5…`;
  - bridge `REVIEW-UNIT1-r4.md` `e489fc19…`, `r4/BRIDGE-UNIT1.md` `4e97610d…85e2` and `r3/BRIDGE-UNIT1.md`
    `ee1c83c0…8219`.
- **Corpus:** `git fetch origin main` gave `fd539e150759a6ea51ab279aeeac80fc06050ade`. Every `main` read was a
  `git show fd539e15:<path>`. I used no `--depth`, `gc` or `prune`, and made no git or GitHub write.
- **Authorization:** #868 c.6740118315 (paper-only; exact generic checks only). My probe uses generic matrices and
  tables and hand re-typings of kernel definitions. It runs no OI mechanism.
- **My probe:** `review/probes/rv3_868_checks.py` (sha256 `cbc896dd8a03a830…`; full hash in §6), with output
  `rv3_868_checks.out` (`9a078144ecb0351a…`). It runs 24 checks with 0 failures, exit 0, using `python3 -I` and
  sympy 1.14.0. It imports no earlier probe. Every check that asserts a failure carries an exact nonzero witness, so
  it cannot pass because `simplify` failed to reduce an expression. The checks are cited below as K1–K6, N3 and N7.
- **Re-runs** (`python3 -I`, outputs in `review/probes/rv3/`): `r2_validity_scope.py` (edited and original),
  `r3_scope_checks.py`, `g868_generic_checks.py`, `rv2_868_checks.py` and `rv_868_checks.py` all exit 0. Each output
  is byte-identical to its recorded `.out`.

## Verdict: ACCEPT WITH NITS

- **B1 is fixed correctly at every site the r2 review listed.** J3's second necessity is now *a non-real operation*,
  defined operationally. O1 is named as one source of it, and the layer flow and the driven transition as others.
  Independence is stated only as O1 versus O2.
- **The coordinator's correction from the bridge r4 review is applied correctly.** The drive carries the phase, and
  moving the all-ones ray is necessary, not sufficient.
- **N1–N7 are fixed.**
- **Independent checks.** I verified the drive identity, its agreement with the kernel's `gateFlow_isolation`, the
  quarter-phase claim, the N3 identity and the transposition step, and W1 and W3, each with its own controls.
- **Remaining issues.** I found no blocker. Six nits remain: four are wording or attribution, and two are optional
  sharpenings.

***

## 1. The r2 findings

| r2 | fixed? | check |
| --- | --- | --- |
| B1 | yes | **Sites.** All listed sites carry the restatement: §0 Q1 *Missing* (l.54–60); §0 Q2 first and second bullets (l.72–80); the J3 row, columns (ii) and status (l.244); §4.4 (l.305–343); §5 J3 (l.381–383); the §6 FI-1 row and verdict (l.397, 414–415); §8 (l.487–489); §10 Q1 and Q2 (l.510–515); the V5 docstring. A grep for "phase needed", "needs the phase", "needs O1" and "no phase input" finds no hit in the text or the probes. **Definition.** l.311–312 defines a non-real operation operationally: "takes some state real in the configuration basis to a non-real one". That is the right definition. A matrix that is non-real but proportional to a real one keeps every real state real (K5), so a matrix-level definition would be wrong. For unitaries the two readings agree. **Necessity.** Real Kraus maps keep ⟨Y⟩ = 0 when they act on the system with a uniform ancilla and are followed by a partial trace (K5; r3 W6). **Independence.** The only independence claims in the text concern O1 versus O2: l.73–75, l.337–340 ("does not make a non-real operation independent of a non-monomial one") and l.397. Elsewhere "independent" means either "does not depend on" in the partial order (l.382–388) or the pre-existing statement at l.443. Neither is an independence theorem. `obligations_independent` (`C5Discovery.lean:59-67`) matches the text: `PhasesAvailable ∧ ¬LayerFlowExecutable` on `substratumTheory (Fin 2)`, and `LayerFlowExecutable ∧ ¬PhasesAvailable` on `onesTheory (Fin 2)`. |
| B1, bridge r4 correction | yes | **Drive identity, generic θ.** `e^{−iθX_ab} = e^{−iθ} G_(ab)(2θ/π) diag(1,1,e^{iθ})` holds exactly for generic θ (K2). I first checked that the closed form solves `U′ = −iX_ab U`, `U(0) = 1` (K1). Three mutations fail with exact nonzero witnesses: the conjugate phase, gate time θ/π, and a missing prefactor (K2). **Against `LiftAudit.lean:660`.** I re-typed `gateFlow_isolation` from its statement, with `phaseFun` and `signFun` (`:582-587`). On four states with τ = (01)(23) and a = 0, where the sign conjugation is active, `diag(phaseFun)·G(t)·(sign·G(t)·sign)` equals `exp(−iπt X_01)` for generic t. Without the sign conjugation the (23) block does not cancel (K3, control). On three states with τ = (01), the kernel's left side equals W10's right side at θ = πt (K3). So W10 is the kernel identity specialised to one transposition (nit n2 on the wording). **Quarter phase (W10).** `drive(π/2)·swap_ab = −i·phaseGate(c)`, with `phaseGate` as at `LieRankSource.lean:209`. The two conjugation channels agree on a generic Hermitian ρ (K4). At the quarter turn the drive is monomial and non-real, and it is non-monomial at π/3 (K4). That fits "non-monomial at generic times" (l.59, l.316) and bridge r4-n6. **Countercontrol.** A real rotation at the quarter turn, composed with the swap, is real and gives a different channel (K4). §4.4's countercontrol and the R4-B2 wording ("necessary … not shown sufficient", GR:258–260 at `fd539e15`) are correct. **GR line numbers.** The quotations are on these lines: "No phase operation enters" GR:250; "dispensable at every level" GR:258; "is not shown sufficient" GR:260. |
| N1 | yes | l.75–77: H-Bell is "not derived from FI-1 or the phase and derives neither, and no independence theorem is stated". The sentence is in BRIDGE r4 `l.542`, and it is also in r5 `l.575`. |
| N2 | yes, with a new staleness (n5) | The r4 hash `4e97610d…85e2` is confirmed for `bridge/r4/BRIDGE-UNIT1.md`. The r3 hash `ee1c83c0…8219` is confirmed. The verdicts of REVIEW-UNIT1-r3 and -r4 are REVISE. |
| N3 | yes | **Identity.** `⟨a⊗b|X|a⊗b⟩ = ⟨b|σ_a|b⟩` holds for generic complex X, a and b, with real and imaginary parts explicit, and σ_a is Hermitian when X is (N3). So "block-positive ⟺ every σ_a ⪰ 0" follows in both directions from one identity. **Control.** `diag(1,−1,1,1)` gives a non-PSD σ_{e0} and a negative product value at the same (a, b). **Transposition step.** `h_a(ω) = (ahatᵀω)ᵀ = toOp(ωᵀ) ahat`, which with `toOp ω = Matrix.toLin' (Matrix.of ω)` (`CompositeDimension.lean:406`) and `pairVal(ω,a,b) = pairVal(ωᵀ,b,a)` (N3) gives the `h_a` orientation from `lor_toOp_of_maxCone` (`:1049`) applied to ωᵀ. Since both wings carry `eball d`, `ωᵀ ∈ maxCone` (§4.1, l.195–197). The orientation is not vacuous: w3's heralds by +x are (1,1,1,0) on A and (1,1,0,0) on B (N3). **Citation and grep.** `source-assessment.md:17-19` at `fd539e15` says what l.202–203 quotes. `git grep -il block-positiv` gives exactly the two hits §8 reports. **Labels.** (⇒) and (⇐) CONFIRMING, native form ELABORATING. |
| N4 | yes, with wording nit n1 | The six hypotheses (`hH1`, `hadd`, `hsmul`, `hmax`, `hH2`, `hA`) match `EqvK2MaxCone.lean:153-160`. They are all on `K`. |
| N5 | yes | T2 §6 is under its own *Conditional (W)* bullet (l.36–37), consistent with §5. |
| N6 | yes | §11 l.536–540 states the cause correctly. W9 checks it. |
| N7 | yes | **W1.** The equality is correct and not vacuous. The H-form of the dual of the six effects is `{t ± v_i ≥ 0}` by definition. W1 proves that it equals the conic hull of the eight cube vertices: `Σλ_s = t` and `Σλ_s s = v` hold identically, and each `λ_s` is a product of the dual's own inequalities. I re-checked this on a 125-point rational grid, where every `λ_s ≥ 0`, the reconstruction is exact and all six effects are ≥ 0. Six points with one `|v_i| = 11/10` each violate an effect (N7). **W3.** The SOS identity expands exactly (N7). Each term is ≥ 0 on the ball, because `1 − a₁² − a₃² ≥ 1 − |a|²`. The certificate is not vacuous: T has eigenvalues {3/4, 1/4, 1/4, −1/4}, so validity does not come from positivity; T's value at (+x, −x) is 0, so it is tight; and with c = 11/10 the value is negative (N7). |

## 2. The direct edit of `r2_validity_scope.py`

- **Acceptable.**
  - The code ASTs of the original (`r2/probes/`, `60095dc0…`, byte-identical to the hash r2 recorded) and the edited
    file are identical. Only the module docstring differs, and only in the V5 line (`diff`: lines 19–20).
  - Both versions run to exit 0, with output byte-identical to `r2_validity_scope.out` (`d86e03c1…`).
  - §11 (l.530–532) and the dispositions record both hashes and where the original is kept.
  - Leaving the B1 overclaim in a live docstring would have kept the defect in an artifact. Replacing the file
    without keeping the original would have broken the provenance r2 cites. The edit does neither.
- **Residual.** A reader who follows r2's path `probes/r2_validity_scope.py` now gets a different hash. r3 §11 explains
  why. Nothing further is needed for a scratchpad record.

## 3. Product-test validity versus quantum states

There is no conflation:
- §0 Q1 (l.48–53), §4.1 (l.232–236), J5 column (iii), §4.3 item 1, §5's column discipline and §7's "None of the
  outcomes makes the composite a quantum state" all keep validity apart from quantumness.
- The B1 rewrite touches only J3 (product inclusion) and does not reach J5.
- The new sentence l.235 ("Product tests do not decide whether a table is a quantum joint state") is right, and so is
  r3 W3/W4.

The owner's four distinctions are kept:
- configuration versus encoded carrier: l.341–343;
- availability versus derivation: each source of a non-real operation carries its status, and "none derived";
- mixing versus the composition rules: l.348–350, and the countercontrol keeps "mixing" apart from "non-real".

## 4. Three-column separation, scope, register

- **Columns.** No column (ii) is answered from column (iii). J3 column (ii) states necessities and sources with their
  status, and column (iii) is "yes". J11 is unchanged and clean.
- **Scope.** The necessities are scoped to Main:564's interface on the configuration carrier (l.341). The layer flow
  is explicitly not claimed to settle J3 on `Fin 2` (l.321–322). "One operation can meet both necessities" is a
  statement about necessary conditions, not sufficiency.
- **Register.** This is a record, not `papers/`. Every token of four or more capitals is an identifier, a status
  word or a §A.31 label. I found no reader-instruction or self-assessment phrase. "Column discipline" (l.389) names a
  check, not a self-assessment.

## 5. Nits

- **n1 (§0 Q1, l.52–53).** "Only with all six is `K = Q3`" reads as the converse (K = Q3 ⇒ all six). The converse
  is true, because Q3 satisfies all six, but only `driveInvariant_of_eq_Q3` is a named witness for any part of it.
  Under §A.34, write "With all six, `K = Q3` (kernel)".
- **n2 (§4.4 l.327–328; §11).** "`gateFlow_isolation` … states the relation from the other side" is imprecise. W10
  is the kernel identity specialised to one transposition on three states: the sign conjugation is trivial and
  `G(t)² = G(2t)` (K3). Say that.
- **n3 (§4.4 l.323–324; DISPOSITIONS owner-direction table).** "added as an empirical controllability resource"
  (Main:590; also GR:260) describes the state-mixing operation added to the substratum class *beside the stated
  phases*, not the drive of phase-free richness. For phase-free richness, the non-derivation is in GR:258 ("it is not
  a claim that bare observation incompleteness entails these principles"). Attribute each quotation to its context.
  The status "none derived from OI" is unaffected.
- **n4 (§8 l.487–489).** "It follows from Main:564, Main:590, GR:250–260, `obligations_independent` … ,
  `gateFlow_isolation` …" lists the sources of non-real operations and the scope of independence as if they were
  premises. The necessity rests on G7 and R6d/W6 under Main:564. List the others as the sources and context the
  CONFIRMING label compares against.
- **n5 (§2 l.141–147).** "r4, `4e97610d…85e2`, the current working file" is now stale. `bridge/BRIDGE-UNIT1.md` is
  r5 (`78f1098e…`, mtime 13:54:00Z, after r3's save at 13:50:16Z). Pin it as "r4, the working file when read". The
  two r4 sentences r3 relies on are also in r5 (`l.469`, `l.575`).
- **n6 (optional, §4.4 l.329–330).** In W8's x+ ⊗ z+ preparation, the second drive at π/2 followed by the exchange
  on wing A's pair is, as a channel, the inverse quarter phase on wing A (K4 on that pair). Saying so would make "the
  phase content is carried by the drive" concrete at the preparation where it is used.

## 6. Probe record

- `review/probes/rv3_868_checks.py`: sha256 `cbc896dd8a03a830…` (full hash below).
- `review/probes/rv3_868_checks.out`: sha256 `9a078144ecb0351a…`. 24 checks, 0 failures.
- Re-run outputs: `review/probes/rv3/{r2_edited,r2_orig,r3,g868,rv2,rv}.out`, each byte-identical to its recorded
  output.

Full hashes:

```
cbc896dd8a03a830673e76e2ab8583c1d9a551b23b26c74b54d4ddfaa2fc999f  review/probes/rv3_868_checks.py
9a078144ecb0351abcedab5c2095df60a96ea30ce4910f4eddec32ba9fb63a22  review/probes/rv3_868_checks.out
```

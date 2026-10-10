# Coordinator's audit of EQ5-PREM (research only)

Thread result: `scratchpad/eq5/PREM/RESULT.md` (619 lines, read in full). Protocol: `scratchpad/eq5/PROTOCOL-PREM.md`
(sha `7d3dcf6f44455650…`), with the shared rules of `scratchpad/eq5/PROTOCOL.md`.

## Verdict

The exact content stands. So do both outcomes:
- Part A, four-token coherence: NOT SOURCED.
- Part B, gate preservation: NOT SOURCED.

Evidence:
- Every replay is byte-identical.
- An independent exact audit (own code, 14/14) confirms every exact claim it covers.
- The integrity anomaly the thread recorded is resolved. The eight files are the coordinator's own writes (§4).

Seven wording items overstate the scope of the evidence (§3). None changes a verdict, a countermodel or an exact check.
They must be corrected before any of the text is reused.

## 1. Replays

| script | script sha (matches RESULT §3) | output sha | verdict | thread replay | coordinator replay |
|---|---|---|---|---|---|
| `q0_census.py` | `a64bf2636650ea77` | `db99032569b6e59e` | `Q0-CENSUS-COMPLETE` | identical | identical |
| `q1_tok_models.py` | `db688057771bfe0a` | `9dded6d5707e9406` | `Q1-PART-A-MODELS-EXACT` | identical | identical |
| `q2_purity.py` | `a9f95269a0a61cb6` | `d24a769210c29707` | `Q2-PURITY-LEMMA-INGREDIENTS-EXACT` (+ 4 leads) | identical | identical |
| `q3_gate.py` | `4be541b1f28d8637` | `5907132ff66297e1` | `Q3-PART-B-GATE-EXACT` | identical | identical |
| `q4_pair_gates.py` | `2d92ca5af97c3b71` | `5e643f28a4bd4e19` | `Q4-PAIR-GATES-EXACT` | identical | identical |
| `q5_resets.py` | `38b448576fc7e746` | `04a05cb6916c85d9` | `Q5-RESETS-EXACT` | identical | identical |

- **Thread replay:** `eq5/PREM/q*.replay.{out,err}`, compared with `cmp` against the run-1 outputs.
- **Coordinator replay:** `eqreview/prem-audit/q*.audit.{out,err}`, run at 11:45Z with the arguments recorded in RESULT
  §3 and compared the same way.
- Each `.err` holds only the appended `exit=0`.

## 2. Independent exact audit

`eqreview/prem-audit/audit_prem.py`:
- Script sha `1fb41cc247b42741`; output sha `0d0b5b799292b394`.
- Result: 14/14, `PREM-AUDIT-CHECKS-PASS`, on the first run. The replay is identical. `.err` holds only `exit=0`
  (`19eaf43821a7660e`).
- The decision rule is in the script header and was fixed before the first run.
- Independence:
  - The script reads no file of `eq5/PREM/`.
  - The Pauli map, the standard CNOT conjugation and the table actions are implemented from their definitions.
  - The base's `cnot` (`sgn`, `pc`, `pt`) is read from the base snapshot and compared with the standard CNOT.

| id | what was checked | result |
|---|---|---|
| C1 | one token: σ_y ρᵀ σ_y = (I − r·σ)/2 for symbolic r, so θ = Ad(σ_y)∘T | pass |
| C2 | θ∘actT reflY = actT diag(−1,1,−1) is Ad(I⊗σ_y); actT reflY is the token-2 partial transpose (symbolic) | pass |
| C3 | the base `cnotFun` equals standard CNOT conjugation (control token 1); the transcribed base lines match | pass |
| C4 | `cnot(prodState xplus z3) = phiW = diag(1,1,−1,1)`; `pauliW(phiW) = |Φ⁺⟩⟨Φ⁺|` | pass |
| C5 | `actT reflY phiW = idW`; `pauliW(idW) = SWAP/2` with vᵀ pauliW(idW) v = −1 (eigenvalues ½ ×3, −½); `actT reflY` fixes `prodState xplus z3` — TWIN's hgate failure | pass |
| C6 | MAX: `idW` pairs as the Euclidean product; generator values 1, ½, ½, (1+b·c)/4; `cnot(idW)` at the sharp pair (−eₓ, −e_z) is **−½** | pass |
| C7 | MIN: F(prodState x y) = 1 − x·(reflY y), with certificate \|x−w\|²/2 + (1−\|x\|²)/2 + (1−\|w\|²)/2 for \|w\| = \|y\|; F(phiW) = **−2** | pass |
| C8 | CC2: pure marginals (z, z), g and f sharp, T(g, f) = **−1/40**, T not a product | pass |
| C9 | purity core (symbolic, modulo z·z = 1): T(g_z, f) = −½ zᵀCf and \|c⃗_f\|² − c_f0² = 2f(y) zᵀCf + \|Cf\|² | pass |
| C10 | the homogenized e_x, e_y, e_z, −e_z are linearly independent (det −2), so the 4⁴ = 256 fourfold products span W4 | pass |
| C11 | −I commutes with every 3×3 matrix | pass |
| C12 | `fourVal` factorizes on product generators | pass |
| C13 | 16 cited base lines carry the names RESULT attributes to them | pass |
| C14 | no float enters a checked quantity | pass |

## 3. Wording and scope (P/A/C, claim/evidence boundary)

1. **"Every formulation … that does not restate gate preservation is refuted"** (§0 lines 67–68; §Outcome B line 436).
   - The evidence is a finite census (§2.B rows 1–8) plus one structural class. The universal "every formulation"
     goes from a finite test to a universal claim.
   - Correct form: "Each tested formulation that does not restate gate preservation (§2.B rows 1–8) is refuted by an
     exact countermodel. So is every predicate of the chart-blind form defined in §1.B2."
2. **"No principle that is blind to that alignment can supply it"** (§0 line 77).
   - The statement is true only with §1.B2's definition, and it must carry that definition inline: P = P_gate(N) ∧
     P_cone(K), where P_gate holds for `cnot` and P_cone holds for Q3 and is invariant under K ↦ actT reflY K.
   - Content: TWIN satisfies every such P and violates hgate. So no such P implies hgate. This is insufficiency only.
   - Predicates that fail at (Q3, `cnot`), or that are not of the factorized form, are not covered.
3. **"The weakest additional principle is 'the native gate is an automorphism of the standalone pair's state space'"**
   (§0 line 85; §Outcome B line 431). This is not established.
   - "Weakest" compares against all principles. Only the census was tested.
   - Within the census, every survivor is a restatement. Given N-CLASS, closedness and convexity, all survivors are
     equivalent to hgate:
     - PR = hgate ∧ hinv by scaling, and hgate ⇒ hinv by (R).
     - Effect-side availability ⟺ hgate by the bipolar theorem.
   - (R) is `inv_mem_of_orth`: N preserves `ipW`, K is closed, and N maps K into K; then N⁻¹ maps K into K. No convexity
     is used. It printed standard axioms only in design run 2 (37928497993 at `614d6913`, disposable branch). That run's
     gate failed for unrelated reasons. This is design evidence, not certification.
   - Without orthogonality and closedness, "automorphism" (hgate ∧ hinv) is stronger than hgate. So if any principle is
     "weakest" it is hgate itself, which is the restatement.
   - Correct form: "Every surviving formulation restates hgate. Given N-CLASS, closedness and convexity they are
     mutually equivalent and equivalent to hgate. No strength ordering among non-restating principles is established
     beyond the tested census."
   - Part A's "Weakest additional principle **found**: IP₁ᴮᴬ" (line 342) is acceptable. It is census-relative and
     says so.
4. **"It reduces what a source must deliver"** (line 321). This reads as necessity ("must"). Correct form, as
   sufficiency: "A source that delivers IP₁ᴮᴬ, together with local tomography of one grouping, one body and PairAdm,
   suffices for `tok` (Theorem A). IP₁ is not necessary for the headline conclusion (M_id, M_T)."
5. **"No landed or adopted principle implies `TokProdState` or `tok`"** (lines 27, 338). This is acceptable only as
   census-relative.
   - Scope: the q0 census at `bcbc516f` (§2.A).
   - Each field-neutral entry, and each field-neutral shadow of a complex-typed entry, is refuted by an exact
     countermodel (q1).
   - The complex-typed originals are not refuted. They are not predicates on these data: they are import-separated and
     flagged as circular.
   - The sentence should name the census and the two kinds of disposition.
6. **"Load-bearing"** (lines 56, 176, 178, 202, 204, 221).
   - Each instance is a model of (P without A) ∧ ¬C. That shows the remaining premises do not suffice, so A cannot be
     dropped from this premise set. It is not necessity of A.
   - RESULT §5 already disclaims necessity. The term should still be replaced at each site by "cannot be dropped:
     ⟨model⟩ satisfies the remaining hypotheses and violates the conclusion."
7. **TWIN and the IIP-1 isometry** (lines 385–386, §2.B row 5).
   - "The IIP-1 form of twin is Euclidean" is a written argument (t7 plus irreducibility of Ad SU(4)). Neither the
     thread's scripts nor this audit compute it.
   - So row 5's refutation by TWIN, and "the IIP-1 isometry: refuted by TWIN" (line 72, line 394), carry [W], not [X].
   - TWIN's self-duality (line 381) is also [W]. Its argument is short and correct: actT reflY is an `ipW`-isometric
     involution, so dualW(actT reflY Q3) = actT reflY (dualW Q3) = twin. It is likewise not computed here.

Items 1–3 and 7 are claim/evidence-boundary corrections. Items 4–6 are P/A/C wording. Every negative result in RESULT is
a model of the stated premises in which the target fails, and RESULT §5 states that this shows insufficiency only. That
framing is correct.

## 4. Integrity

**The anomaly** (RESULT §4): eight untracked `FourCopy*.lean` files appeared under `verification/lean-mathlib/OIBridge/`
during the thread, with mtimes 10:54–11:12Z. The thread recorded them with hashes, did not read them, did not repair
them, and ran no measurement after finding them. That handling is correct under §A.26.

**Resolution.**
- The coordinator wrote them, as drafts for EQ4-F design run 1 (the Pauli-free split), in the repository working tree.
- Method: reverse the coordinator's later edits, as exact strings, to reconstruct each file. Each reconstruction hashes
  to the value the thread recorded:

  | file | recorded (PREM) | reconstructed | blob at `1310e629` |
  |---|---|---|---|
  | `FourCopyBipolar.lean` | `661d292675661310` | MATCH | `4324b83b33dbad04` (edited after) |
  | `FourCopyBridge.lean` | `febb3d1fc9658275` | MATCH | `ea6abc557a7d1c51` (edited after) |
  | `FourCopyCore.lean` | `9fce26e66fdec1e9` | MATCH | identical |
  | `FourCopyEuler.lean` | `13c03eb6f9506543` | MATCH | `d4a7257f9478447d` (edited after) |
  | `FourCopyHeadline.lean` | `7a544c11d1c77a35` | MATCH | `7f21ca55424a52ba` (edited after) |
  | `FourCopyIE1.lean` | `ddb33c259eac1326` | MATCH | identical |
  | `FourCopyLocal.lean` | `12c1cd6cc79a651b` | MATCH | `1b842961ff3c5e3f` (edited after) |
  | `FourCopyTables.lean` | `defae9a298f3a602` | MATCH | identical |

- All eight files were committed in `1310e629` (11:42Z) on the disposable branch. Five had been edited further first.
- No PREM measurement depends on them. The thread's scripts read only the base snapshot, the inputs package and one
  Mathlib file, and those verify unchanged.

**Other checks.**
- The base manifest (`8f31917b…`) and the inputs manifest (`9108b62b…`) are silent, with exit 0. They were checked
  from their own roots, during the audit and again when this note was written. One earlier invocation from the wrong
  directory gave a spurious exit code and was re-run.
- The thread's writes are confined to `eq5/PREM/`.

## 5. Not checked by this audit

- **Written arguments.** Theorem A, R1–R10, the purity lemma's induction, the chart-blindness argument and the OLTIres
  derivation are written arguments. This audit checks their exact ingredients (C8–C10, C12) and read the written steps.
  None is kernel-checked.
- **M_θ.** The assembly of M_θ was not independently re-derived. RESULT §5 says it is the M_tw assembly with θ in place
  of ρ.
- **SOURCE countermodels.** Their PSD assembly is audited in `EQ5-SOURCE-AUDIT.md` and is not repeated here.
- **TWIN.** Its IIP-1 entry and its self-duality are written only (§3 item 7). The IIP-1 entries for MAX and MIN are not
  evaluated, as RESULT §5 states.

Consistency-axis work only; bands unchanged.

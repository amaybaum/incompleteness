# Independent review of ASSESS-868 r2 (#868 re-assessment: joint-test validity and composition)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09), fresh independent reviewer of r2.** This review
authorizes nothing. An ACCEPT, if a later round reaches one, adopts no premise and authorizes no further unit, edit,
freeze, dispatch or merge.

- **Under review:** `ASSESS-868.md` r2, sha256 `f4873a4494193b521d33b642156c2f611773e90947211849e50bcb3142ff34ae`
  (confirmed before reading). Also read: `DISPOSITIONS-r2.md`; `r1/ASSESS-868.md` (`3499d405…13c3`, confirmed);
  `review/REVIEW-868.md` (`c8da0967…d763`, confirmed). All probe hashes cited in r2 §11 and in the dispositions are
  confirmed: `g868_generic_checks.py` `292d16b0…`, `.out` `e93f6541…`, `.run1-misspecified.out` `d4521708…`;
  `r2_validity_scope.py` `60095dc0…`, `.out` `d86e03c1…`, `.run1-float.out` `a101caf5…`; `rv_868_checks.py`
  `b460abd4…`, `.out` `c83449e4…`; `reassess/rerun-868/rv_868_checks.out` `c83449e4…`.
- **Corpus:** `git fetch origin main` → `fd539e150759a6ea51ab279aeeac80fc06050ade`. Every `main` read was
  `git show fd539e15:<path>`. No `--depth`, `gc` or `prune`; no git or GitHub write.
- **Authorization:** #868 c.6740118315 (paper-only; exact generic checks only). Owner direction #1169 c.6740778880,
  as relayed. My probe uses generic matrices, generic correlation tables and a hand re-typing of the kernel's
  `unit`/`gateFlow` definition on `Fin 2`; it runs no OI mechanism.
- **Re-runs (`python3 -I`, sympy 1.14.0):** `r2_validity_scope.py`, `g868_generic_checks.py` and `rv_868_checks.py`
  all exit 0 with output byte-identical to the recorded outputs (`review/probes/rv2/`).
- **My probe:** `review/probes/rv2_868_checks.py` (sha256
  `791556c5a3f108c281da46c89dae7a9b11d3b955d8f2fcf2b6cfdd3f7ddc7a6c`), output `rv2_868_checks.out`
  (`b7eaf2a782a36414ca5c09de646eed596b9f82533b157b2e51d1fac10e332d14`): 26 checks, 0 failures. Imports no earlier
  probe. Checks are cited below as A1–E1.

## Verdict: REVISE (narrow)

Fifteen of the sixteen r1 findings are fixed correctly. B6 is fixed except for its J3 part, which carries the
blocker. The three independently requested verifications hold (§1). The (V)/(C) split of Q-868-H is right in both directions, and product-test validity is kept apart from
quantumness everywhere, including the swap and node-10 tables. One blocker remains. It entered r2 through the r1
review's own B6 safe-path wording, and it is the same scope error that `REVIEW-UNIT1-r3.md` B2 found in BRIDGE r3
nine minutes before r2 was saved: the necessity of **the phase (O1)** for J3 is asserted where the argument proves
only the necessity of **a non-real operation**, and the kernel's own layer flow is a non-real operation without O1.

***

## 1. The r1 findings

| r1 | fixed? | check |
| --- | --- | --- |
| B1 | yes | §4.1 *Native form*: the dual of the six Pauli sharp effects is the cube cone; octahedron ⊂ cube; w3 witnesses (V) ⇏ (C). Independently: every cube vertex is in the dual with exactly three tight effects and `(1, 101/100, 0, 0)` is not (A1); octahedron vertices lie in the cube, the cube vertex lies outside the octahedron and `Lor` (A2); w3 has all 36 Pauli values ≥ 0, **every** Pauli herald on **either** wing in the cube cone, and its +x herald `(1,1,1,0)` outside the octahedron and `Lor` (A3). Additionally w3 fails a full-ball product test (`1 − √2`, A3c), consistent with "validity on native tests" being strictly weaker than `maxCone (eball 3)`. Q-868-H is split, with separate outcomes; the "If no" overreach is gone. |
| B2 | yes | The three r1 sentences are gone (grep). §4.1 *Reading, one direction at a time* keeps the composite quantifier, makes `hsharp` separate (matches `EqvK2MaxCone.lean:208-209`) and states the NS step as one-directional prose. §9 Q2 is reworded to a sufficient route. |
| B3 | yes | `lor_toOp_of_maxCone` is at `CompositeDimension.lean:1049` with docstring "A maximal-cone vector, read as an operator, carries the cone into itself" and statement `ω ∈ maxCone (eball d) → Lor f → Lor (toOp ω f)`; `toOp ω = Matrix.toLin' (Matrix.of ω)` (`:406`), i.e. `ω·f`, the herald of the control wing — the mirror orientation, as r2 says. `lor_pair_bound` `:877`, `lor_of_forall_pair` `:1015`, `lor_ehom` `:930`, `isEffectOn_affOf` `:916`. DIM-1 `result.md:32, :101` and `preregistration.md:71-72, :147, :180` say what r2 quotes. The CONFIRMING label for (⇒) is correct. See nit N3 for (⇐). |
| B4 | yes | Witness (1, 1, 1, ½): p ≥ 0, zero marginals on both wings (B1); exactly eight CHSH forms, max 5/2 < 2√2 (B2). Not quantum by two independent routes: the Tsirelson vector-Gram minors on {u0, v0, v1} and {u1, v0, v1} are −(q−1)² and −(q−½)², so no `v0·v1 = q` makes both nonnegative (B3); the TLM arcsine sum is 3·(π/2) − π/6 = 4π/3 > π, with the Tsirelson point at exactly π as control (B3c). r2's ‖Aψ − Bψ‖² argument is correct for ±1 observables, and binary POVMs dilate to these. The J11 row and §6 M20 row now keep J9's quantum premise in column (iii); SHARED §9's "none identified" stands; `composition-source-map.md:166` quoted correctly. |
| B5 | yes | §6: M17 "shared part, not identity", R6.11 "part of", R6.9 ↔ J12 "containment, one direction", M18 = J13 and R6.12 = J2 kept as identities. Verdict and §0 Q2 match. |
| B6 | partly | "earliest" and "downstream" are gone; BRIDGE status updated; J3 now names two inputs. The second input is mis-identified with O1: **blocker B1 below**. |
| N1–N10 | yes | Each disposition entry located in the text and checked. N1 §2; N2 §11; N3 §4.3 item 2 (kernel `nflip` control, Z-conjugation control described); N4 §4.3 item 1 split (independently: `(I+XX)(I+ZZ)/4` is the rank-1 projector Φ⁺ with ⟨YY⟩ = −1, C2); N5 fifth premise, MECH-1 `DESIGN.md:199` ("determinant `−1` … which is not CP") and literature; N6 J8 scoped; N7 §4.4 and §6 scoped to coherent pair sources; N8 partial order (§5, §10); N9 G5/V6 cited; N10 A6.1 [D], Main §3.3 [P], (D), (L′), MI held. |

Owner direction (three pairs plus validity vs quantum): kept. §1 states the four distinctions; node 10 is named an
encoded carrier; J3 and §4.4 are scoped to the configuration carrier; J7 separates the mathematically available
`cnot` from its native availability; §4.4 separates mixing from the composition rules.

## 2. Q-868-H, both directions (§A.34)

- **(C) ⇒ (V).** (C) asks that every remote herald lie in the cone over the octahedron (with a sound dictionary);
  (V) asks that it lie in the dual of the native tests, the cube cone. Octahedron ⊂ cube (A2), and by Lemma H's
  available-family form (V) is J5 on native tests. Holds.
- **(V) ⇏ (C).** w3 satisfies (V) on both wings (A3) and its +x herald leaves the octahedron. The non-implication is
  between conditions on tables; r2 does not claim that w3 is a native preparation, and should not (it is not
  needed). Holds.
- The outcome bullets are consistent with these: "(C) no, (V) yes" is stated as a closure finding, not a failure of
  validity; "None of the outcomes makes the composite a quantum state".

## 3. Validity versus quantum states

No conflation found. §0 "Validity is not quantumness", §4.1 closing paragraph, J5 column (iii) "yes, but
non-selective", §4.3 item 1 ("product-test validity holds and the table is not a quantum state") and §7 all keep
the two apart. Swap: Pauli table `2·I₄`, heralds `2(1, a) ∈ Lor`, eigenvalue −1 (C3). Node-10 table: heralds
`(1, a₁, 0, a₃)`, and `1 − a₁² − a₃² = (1 − |a|²) + a₂² ≥ 0` (C1, the inequality V3 leaves to a comment),
eigenvalue −1/4. One imprecision in how the K2 route is summarized: nit N4.

## 4. The probe disclosure

Accurate. Reconstructing V4 with Python `int`s and the float `1/2` gives the same numbers (0.5, 2.5) while
sympy 1.14's strict `Rational == float` comparisons return `False`; with exact coefficients the same comparisons
hold (E1, E1c). The recorded r2 code carries the same expectations r2 states (NS, max CHSH 5/2, PR box 4). The
run-1 source was not retained, so "no expectation was changed" is checkable only through this reconstruction, which
is consistent with it. Wording: nit N6.

## 5. Blocker

### B1. "J3 needs the phase (O1)" is stronger than its argument; the kernel's layer flow is a non-real operation without O1 (claim/evidence; §A.34 one direction at a time)

- **What r2 asserts.** J3 at full-ball scope on the configuration carrier, under Main:564's rules, needs "both a
  non-monomial operation (FI-1's content) and a phase not in {0, π} (O1, adjoined as a stated intervention principle,
  Main:590)", the phase being "an obligation independent of the flow (K `obligations_independent`)". Sites: §0 Q1
  *Missing*; §0 Q2 second bullet; J3 row (column (ii) and status); §4.4 first bullet; §5 *Missing* (J3); §6 FI-1
  row and verdict; §8 "J3 needs a non-monomial operation and the phase … CONFIRMING"; §10 Q1 and Q2; probe V5's
  docstring "(phase needed)".
- **What the argument proves.** R6d / V5 show that real operations keep ⟨Y⟩ = 0 on real states. That proves J3 needs
  **a non-real operation**. It does not prove J3 needs O1 (`PhasesAvailable`, the quarter phase gate,
  `RouteB.lean:132`), and it does not make that need independent of the flow.
- **Counterexample in the kernel's own objects.** `LayerFlowExecutable` (`LiftAudit.lean:112`) makes
  `conjChannel (gateFlow σ t)` available, with `gateFlow σ t = unit (permMat σ) t` (`:47`) and
  `unit g t = 1 + (exp(iπt) − 1)·(1 − g)/2` (`SecondOrderCircuit.lean:356`). On `Fin 2`, `unit(X, 1/2)` is unitary,
  non-monomial, fixes the all-ones vector, and takes `z+` to `y−` (Bloch vector (0, −1, 0)); in general
  ⟨Y⟩ = −sin πt, ⟨X⟩ = 0 (D1). This is the flow of `onesTheory`, the very witness by which
  `obligations_independent` (`C5Discovery.lean:59`) shows flow **without** phase. So the flow that holds without O1
  already supplies y-axis states. Control: real non-monomial H keeps ⟨Y⟩ = 0, and the quarter phase moves the
  all-ones ray while the flow does not (D1c), so the two operations are genuinely different.
- **The full-ball case.** On `Fin 2` the layer flow alone stays in the y–z plane (D1), so it does not settle J3 at
  full-ball scope either way. But GR:250–258 at `fd539e15` states phase-free richness ("No phase operation enters":
  a continuously drivable pair and the exchanges), which with implementation locality and embedded observation is
  equivalent to exact finite endomorphic operational QM. Drives `exp(−isX_ab)` at s = π/4, π/2 and one exchange,
  with no phase gate, prepare `x+ ⊗ z+` exactly from `|10⟩` (D2). Under that mixing form the phase is not a separate
  input; it is separate only beside the layer flow. `REVIEW-UNIT1-r3.md` B2 (13:17:28Z, before r2's save at
  13:26:03Z) states the same for BRIDGE, and the working BRIDGE (r4, §5.1(b)) now says "Under that form of the
  mixing resource the phase is not a separate obligation; beside the layer flow it is."
- **Safe path.** State J3's second necessary input as *a non-real operation* (some available operation not
  proportional to a real one). Say that one operation can meet both necessities (the kernel's gate flow for the
  y-axis; the phase-free drives of GR:250–258 for the full set, D2), and that O1, adjoined as a stated principle at
  Main:590, is one source of it. State `obligations_independent` as O1 versus O2, the layer flow. Carry this to every
  site listed above; §8's CONFIRMING item becomes "J3 needs a non-monomial operation and a non-real operation".
  Neither the K2 analysis nor Q-868-H depends on the change.

## 6. Nits

- **N1 (§0 Q2).** "H-Bell is a third, independent gap": no independence theorem is stated. BRIDGE r3 §5.1(c) says
  only that no source read derives either from the other. Say that.
- **N2 (§2 provenance).** The cited BRIDGE r3 hash `a5d7aad1…78c1` matches no file I found in the scratchpad. The
  archived `bridge/r3/BRIDGE-UNIT1.md` and the r3 that `REVIEW-UNIT1-r3.md` verified are both `ee1c83c0…8219`. "r3,
  pending a fresh review" is also stale: `REVIEW-UNIT1-r3.md` is REVISE (13:17:28Z), and the working file is now r4
  (`4e97610d…`). Correct the hash and the status.
- **N3 (§8, §4.1 (⇐)).** The `block-positiv` term of r2's own search hits
  `bridge-compatibility-audit/source-assessment.md:17-19` [W], which §11 lists as read in full: "For block-positive
  X and a unit local vector a, the conditional matrix sigma_a … is PSD: its quadratic form at b is the nonnegative
  product pairing at a tensor b." That is Lemma H in operator form, and the identity it uses gives both directions.
  It is also the standard fact that block positivity is positivity of every local conditional (L). Report the hit
  and label (⇐) CONFIRMING, not ELABORATING. Also say that the K theorem covers the wing-exchanged orientation and
  that the `h_a` orientation follows by transposition [A]. The native form stays ELABORATING.
- **N4 (§0 Q1, §4.1).** "A table that passes every product test is a quantum joint state only with further
  hypotheses, which in the K2 route are `hH1`, `hH2` and `hA`" omits cone closure (`hadd`, `hsmul`). These are also
  hypotheses on the cone `K` the table belongs to, not on the table. §0's "selects Q3 only with `cnot` invariance and
  the drive" omits `hH1` and closure in the same way.
- **N5 (§0 Q1 vs §5).** T2 §6 [W] sits under §0's "Established" heading but under §5's "Conditional (W/D/A)". Align
  them under §1's layer rule. This was carried over from r1.
- **N6 (§11, dispositions).** "Python integer division (floats)": Python 3's `/` on integers is true division
  (integer division is `//`). Say "Python arithmetic with the float `1/2`". The run-1 source is not retained (§4).
- **N7 (probe `r2_validity_scope.py`).** V1 tests one cube vertex and one outside point, so it does not test the
  claim that the dual *is* the cube. V3 does not evaluate the `a₁² + a₃² ≤ 1` step. V5's docstring "(phase needed)"
  carries B1. A1 and C1 cover the first two. Either strengthen the checks or cite them as illustrations.

## 7. Full re-read, scope and register

- The new text was checked against `fd539e15`:
  - Main:218 (the "does **not**, by itself" quote, inside line 218), :564 ("taken as given" kinematics), :590 ("as a
    stated intervention principle"), :652;
  - `EqvK2MaxCone.lean:153-212` (hypotheses as tabulated; the iff is relative to fixed `hH1`, `hadd`, `hsmul`,
    `hmax`);
  - QP `DESIGN.md:211` (C-CP), :555-558 (C-LEAK, C-EAR "Encoded laws lie in the octahedron"), :727-731 (`Y ↦ −Y`);
  - `C5Discovery.lean:59`.
- The drafts cited are consistent with r2's use of them, given the hashes r2 records at reading time:
  - SHARED's M17 row and QX-6's R6.9, R6.11 and R6.12 rows (current files, since revised);
  - BRIDGE r3 §0 item 8 and §5.1.
- **Columns.** No row's column (ii) is answered from column (iii). J11 is clean.
- **Negatives.** Every negative is scoped to the files read and the search run (§11), except B1 above and N1.
- **Register.** This is a record, not `papers/`. All capitalized tokens are identifiers or §A.31 labels. I found no
  reader instruction and no self-assessment. Revision references ("r2", "r1 text kept") are provenance in a record,
  and the dispositions carry the change map.
- **Authorization.** The unit stayed paper-only, with generic exact checks. Q-868-H is proposed, not activated.

## 8. What r3 needs for ACCEPT

B1 at all listed sites, with the probe V5 docstring. Nits N1–N7 are recommended. No new computation on an OI
mechanism is needed: the counterexample uses the kernel's stated definitions and generic matrices.

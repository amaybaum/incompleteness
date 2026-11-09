# Independent review of ASSESS-868 (#868 re-assessment: joint-test validity and composition)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09), fresh independent reviewer.** This review
authorizes nothing: an ACCEPT, if a later round reaches one, adopts no premise and authorizes no further unit, edit,
freeze, dispatch or merge.

- **Under review:** `scratchpad/reassess/868/ASSESS-868.md`, sha256
  `3499d405ca75c9b83bef58508cf1a413689fdff5d69b114f342f8c0d732013c3` (confirmed). Its probe
  `probes/g868_generic_checks.py` (`292d16b0…ef335`) and outputs `g868_generic_checks.out` (`e93f6541…83e3`) and
  `g868_generic_checks.run1-misspecified.out` (`d4521708…6a9f`), all confirmed.
- **Corpus:** `git fetch origin main` → `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`. All `main` reads by
  `git show fd539e15:<path>`. No `--depth`, `gc` or `prune`; no git or GitHub write.
- **Authorization checked:** #868 c.6740118315 (amaybaum, 2026-11-09T12:31:16Z) and #1169 c.6740116927 (12:31:12Z):
  paper-only, "Exact generic checks only"; "Not authorized: computation on an OI mechanism, new physical assumptions,
  freeze, dispatch, manuscript changes or merges." The unit stays inside it: its probe and mine use generic matrices
  and the kernel's own table maps only.
- **My probe:** `review/probes/rv_868_checks.py` (sha256 `b460abd4f19d30e3cacd05cd664cef356b3a5c2f85b87db994268aba0af70bc4`),
  output `rv_868_checks.out` (`c83449e42fd61a52d48c1ce263fca3bc2b6dc7140709ec432ebeb321ee28b2cb`), `python3 -I`, sympy
  1.14.0: 27 checks, 0 failures. It does not import the writer's probe. It re-types the kernel's signed-permutation
  `cnot` (`CompositeDimension.lean:741-775`) and table conventions. I also re-ran the writer's probe: its output is
  byte-identical to `g868_generic_checks.out` (`review/probes/writer_rerun.out`).

## Verdict: REVISE

The mathematics checked is right: Lemma H holds in both directions on `eball d`, the node-10 table and K2-GUARD-1 facts
reproduce exactly, and the provenance holds. Six blockers remain:
- three on how Lemma H is classified and applied (B1–B3);
- one on a wrong non-implication witness (B4);
- one on identification overclaims in the overlap table (B5);
- one on the FI-1 anchor, whose source draft drew a REVISE on exactly this point 11 seconds before the assessment was
  saved (B6).

None of them needs new computation on an OI mechanism. All can be fixed inside the current authorization.

***

## 1. Blockers

### B1. Lemma H does not transfer to the native body: closure of a non-self-dual body is sufficient, not necessary (§A.34; claim/evidence "necessary → sufficient")

- §4.1's available-family form is correct. `maxConeOf avail` holds iff heralds by available A-effects land in the
  **dual cone of the available B-effects**.
- §0, J5's row, §5, §6's M3 row and §7 then replace that dual cone with "the cone over its single-token body", i.e.
  the SA-1(c)-restricted encoded body. On `eball d` the two coincide, because the Lorentz cone is self-dual
  (`lor_ehom`, `isEffectOn_affOf`, `lor_of_forall_pair`). On the native data they do not:
  - QP's C-EAR row: "Encoded laws lie in the octahedron".
  - J6: the native tests are the Pauli reads.
  - The dual of the six Pauli sharp effects is the cone over the **cube**, not the octahedron.
- Counterexample (R3), a generic table with zero marginals, ⟨XX⟩ = ⟨XY⟩ = 1 and all other entries 0:
  - all 36 Pauli product values are ≥ 0 (R3a);
  - its herald by the A-test +x is (1, 1, 1, 0) (R3b);
  - that herald is outside the octahedron cone and outside Lor (R3c), and inside the cube cone (R3d).
- So validity on the native tests does **not** imply closure of the native body. The converse does hold, since the
  octahedron lies inside the cube (R3f).

**Consequences:**
- "J5 on the native body inherits SA-1(c)'s QM-only status" is unsupported as stated.
- Q-868-H is not decisive in both directions. Its "If no" branch (a herald leaves the body) does not make J5 fail
  natively. It shows only that the native composite's heralded preparations leave the native single-token state set.
  That is a separate closure (no-restriction) condition, not product-test validity.

**Safe path:**
- State Lemma H's native form with the dual of the native tests.
- Present body closure as sufficient for J5 on native tests.
- Either rephrase Q-868-H's question as "do heralds stay in the cube cone (J5)" and "do heralds stay in the native
  body (closure)" separately, with their separate outcomes, or add the self-duality / no-restriction premise
  explicitly and carry it into the conclusion.

### B2. "Its content is a single-system property" overstates a rewriting (claim/evidence; §A.31 productivity test)

- Lemma H turns `ω ∈ maxCone` into "every heralded slice of ω lies in the (effect-dual) cone".
- The slices are those of the composite ω. Their quantifier runs over every composite preparation the pair source and
  dictionary admit, which are J13 and J1.
- Nothing composite-specific is removed. The decomposition into (a) availability, (b) closure and (c) NS in §4.1's
  "Reading" is not proved as an equivalence, and its directions differ:
  - (b) alone gives validity, by Lemma H (⇐);
  - validity gives (b), by Lemma H (⇒);
  - validity does not give (a), which is the separate hypothesis `hsharp`, nor (c).
- Q-868-H itself needs a two-wing analysis, which contradicts §0's "its OI status is the status of the single-token
  body".

**Safe path:**
- Remove "Joint-test validity is therefore not an independent composite principle", "Its content is a single-system
  property" and "Its OI status is the status of the single-token body" from §0, J5 and §8.
- State instead: validity ⟺ every remote herald lies in the effect-dual cone (both directions); availability (`hsharp`)
  is a separate hypothesis.
- Give the soundness-via-NS step as one-directional prose [A], not as part of the equivalence.

### B3. §A.19: Lemma H (⇒) is a kernel theorem on `main`; "not found stated" is false; layer and §A.31 label wrong

- `lor_toOp_of_maxCone` (`OIBridge/CompositeDimension.lean:1049`, round DIM-1) proves the (⇒) direction:
  "`ω ∈ maxCone (eball d) → Lor f → Lor (toOp ω f)`", i.e. "a maximal-cone vector read as an operator carries the cone
  into itself".
- `toOp ω f = ω·f` is the herald of the control wing by a target effect. It is the mirror orientation of the
  assessment's `h_a`; R2f checks it on `chainW`.
- The theorem is listed in DIM-1's `result.md:32, :101` ("proved; control S10") and `preregistration.md:71-72, :147`.
- The (⇐) direction is one line from the Lor pairing bound (`lor_pair_bound`) and self-duality (`lor_of_forall_pair`),
  also in that module. It is not stated there as one theorem.
- My R1a–R1c re-derive each direction symbolically:
  - Lagrange identity for (⇐);
  - the witness `b* = −v/|v|` for (⇒);
  - the effect reduction `c ≥ |u|`.

**Safe path:**
- Lemma H (⇒) is layer **K** (DIM-1). Lemma H (⇐) is an elementary [A] converse.
- §8 should label (⇒) **CONFIRMING** and drop "Both directions … were not found stated".
- Add `lor_toOp_of_maxCone` to §11's read list and to §3's table.
- The searched terms (`joint-test`, `product-test positivity`, …) missed it; the module docstring's phrase is "carries
  the cone into itself".

### B4. J9 ⇒ M20 "not ⇐": the stated witness does not witness it; the SHARED §9 "omission" is not a column-(ii) route (§A.34; three-column rule)

- J9 ⇒ complete-history NS and |S| ≤ 2√2 is T2 §6 [W], and it is correct as stated.
- The converse claim cites "the PR box is NS (T2 §5.2)". The PR box has S = 4 > 2√2 (R5a), so it fails M20's
  Tsirelson half and cannot show M20 ⇏ J9. It shows only NS ⇏ J9.
- A correct witness is the zero-marginal law with correlators (c₀₀, c₀₁, c₁₀, c₁₁) = (1, 1, 1, 1/2) (R5b):
  - probabilities `(1 + ab c)/4 ≥ 0`, so NS;
  - every one of the 8 CHSH forms is ≤ 5/2 < 2√2;
  - it is not quantum. For ±1 observables, `‖Aψ − Bψ‖² = 2 − 2⟨AB⟩` (control R5c). So c₀₀ = c₀₁ = c₁₀ = 1 force
    `A₀ψ = B₀ψ = B₁ψ` and `A₁ψ = B₀ψ`, hence ⟨A₁B₁⟩ = 1.
  - Hence it is not J9-representable.
- The "SHARED §9's 'none identified' omits this conditional route" finding (§0, J11, §6, §8) is not a column-(ii)
  route. T2 §6's premise (1) is a positive representation onto local CP instruments on a quantum state, and T2 §6
  says the bound "is conditional on the common representation, not a derivation of it from OI".
  - Listing it in (ii), even conditionally, puts quantum structure (column iii) in column (ii).
  - SHARED §9's "none identified" for (ii) is correct as it stands.

**Safe path:**
- Replace the PR-box witness with a correct one (above), or narrow to "NS ⇏ J9".
- Recast the SHARED §9 item as a cross-reference (J9 would imply M20; J9 is itself a quantum-representation premise),
  not as an omission finding, and drop it from §8.

### B5. Overlap table: "identical / same object / coincides" where the support is containment (Bridge and no-go scope: no identification without a formal map)

- **M17** ("cone separation, per-observer access maps, local tomography") contains a proved part (the cone lemma, Main
  §3.3 [P]) and R6.3's access maps. The row's own text says "= J2 and part of J1". That is an overlap, not identity.
- **R6.11** is "part of J9" in the table, yet the row's direction column and §6's verdict say "identical" /
  "coincides".
- **R6.9 ↔ J12:** R6.9 is a class that makes R6.7's cross-wing response balance. J12 / `C_i` is T2's domain of
  positivity for `D_i`. The argument given (under J9 with a response present, `C_i` must mask it) is [A] and
  one-directional: `C_i` ⊆ a masking class. It does not identify the two.
- §6's verdict and §0 Q2 ("coincides with … M17, M18, R6.9, R6.11 and R6.12") inherit all three.

**Safe path:** state each relation as a directed containment or a shared part, with its direction and the clause
compared. M18 = J13 and R6.12 = J2 may stay as identities: same clause, same anchor.

### B6. The FI-1 anchor: ordering claims rest on a draft now under REVISE on that point; J3 also needs the phase

- §6 and §0 Q2 frame #868 against "#1211's earliest unsupported forward step FI-1" and conclude "#868's gap is …
  downstream of it".
- `scratchpad/bridge/review/REVIEW-UNIT1-r2.md` (mtime 12:46:58Z, 11 s before ASSESS-868 was saved, so plausibly
  unseen) is **REVISE** on BRIDGE r2. RB1 is exactly this ordering. On `main`, `obligations_independent`
  (`OIBridge/C5Discovery.lean:59`) separates the phase (O1) from the flow (O2): each holds without the other, and
  "FI-1 comes first only once the phase is granted".
- This bears directly on #868: full-ball product inclusion (J3) needs y-axis states.
  - Real operations, monomial or not, keep a real symmetric ρ at ⟨Y⟩ = 0.
  - The monomial phase S after a real non-monomial H reaches y+ (R6d).
  - So J3 at full-ball scope needs FI-1's non-monomial content **and** a phase not in {0, π}. The phase is supplied as
    a stated intervention principle (Main:590), not derived.
- What survives:
  - "a non-monomial operation is necessary for J3 under Main:564's rules" (G7, R6a–b);
  - "FI-1 is not sufficient" (rebit witness: H⊗H is real and non-monomial, and local tomography fails; R6c, writer
    G5).

**Safe path:**
- Drop "earliest" from the FI-1 citations.
- State J3's two necessary inputs: non-monomial operation (FI-1 content) and phase (O1), both under Main:564's
  interface.
- Phrase the overlap as "#868 needs FI-1's content for J3/J8 and is not reached by it", not as a position in a linear
  order.
- Update §2's BRIDGE status: r2 is REVISE, not "awaits a fresh review".

## 2. Nits

- **N1 (§2, planning finding).** #868's body does not link the deleted branch by name.
  - It links commit-pinned URLs at `e306143d`, which still resolve because `e306143d` is reachable from `main`, and PR
    #1173.
  - The stale text is "#1173 draft/unmerged", in two obligation rows.
  - The only branch it names, `research/oi-qm-composition-source-20261107`, still exists (`2de820fb`).
- **N2 (§11, run-1 disclosure).** The disclosure of the G3b misnormalization is accurate. It omits two things:
  - G7 (two checks) was added between runs (16 → 18 checks, diff of the two outputs);
  - run 1's label "(probability −1/8)" was also wrong.
- **N3 (G3).** The writer's determinant-+1 control is conjugation by Z, i.e. `diag(−1, −1, 1)`. The kernel's own
  control is `nflip = diag(1, −1, −1)`, which gives 0 (R2g). The writer also checks only the end value, against a
  quantum surrogate.
  - R2a shows the surrogate equals the kernel `cnot` on all 16 Pauli inputs.
  - R2b–R2d reproduce `phiW`, `idW` and `chainW` entrywise.
  - Cite these, or use the kernel control.
- **N4 (§4.3 item 1).** The non-quantumness of node 10 does not depend on the [A] zero completion.
  - Any PSD unit-trace ρ with ⟨XX⟩ = ⟨ZZ⟩ = 1 is Φ⁺ and has ⟨YY⟩ = −1 (R4a–b).
  - Full-ball `maxCone` membership does depend on it: adding ⟨XZ⟩ = 1/2 keeps all 36 Pauli values ≥ 0 but gives −1/4
    on a full-ball product (R4d).
  - State the two separately.
- **N5 (§4.3 item 2, §8).**
  - The K2-GUARD-1 ↔ C-CP link is the standard fact that a determinant −1 one-copy reflection (the transpose) is
    positive but not completely positive (Peres 1996; Horodecki 1996; L). `mechanism-1-20261107/DESIGN.md:199` already
    states that the determinant −1 class "is not CP".
  - Label it CONFIRMING with the literature.
  - Add a fifth premise to the four listed: sequential composability of the operation, the translation and the
    operation again on the intermediate preparations.
  - The "consistency only" label itself is correct, because J7's target is the quantum `cnot`.
- **N6 (J8).** `hA` is invariance of `K` under one-copy rotations (`EqvK2MaxCone.lean:159-160`, `:212-213`), not availability of
  rotations. "FI-1 is necessary" holds on the availability route only. Scope it.
- **N7 (§6 FI-1 row).** "Not upstream of J13" holds for a classically correlated source. Under Main:564's rules, any
  non-diagonal pair state needs a non-monomial operation by the same G7 argument on the 4-state carrier (R6a). Scope
  the row.
- **N8 (§10 "in order").** The missing inputs form a partial order: J13 → J1/J2 → J9–J12. J3/J8, J6 and J7 do not
  depend on J13. Say "partial order" or list the dependencies.
- **N9 (§0, §6).** "FI-1 is not sufficient" has a ready witness (R6c / G5: real QM). Cite it.
- **N10 (§0 Bell bullet).**
  - Label A6.1 [D] (draft, model-reviewed off `main`) where it is used.
  - The one-step case is Main §3.3 [P].
  - Name the hypotheses held: (D), (L′) and MI by design and branch choice, so the only remaining escape is a failure
    of (R) by a coupling path, i.e. R6.7/M19.

## 3. Checks requested, with results

1. **Lemma H.**
   - Each direction re-derived (R1a–c); the hypotheses suffice on `eball d`, d ≥ 1.
   - (⇒) is the kernel's `lor_toOp_of_maxCone`; see B3.
   - The native application fails; see B1.
   - The decomposition is not an equivalence; see B2.
2. **Claim 2.**
   - QP node 10 (`quarter-phase-native-20261107/DESIGN.md:746-768`) reports `⟨XX⟩ = ⟨ZZ⟩ = 1`, `⟨YY⟩ = 0`; confirmed.
   - `(I+XX+ZZ)/4` has eigenvalue −1/4 and lies in `maxCone(eball 3)` (R4c, writer G4); confirmed.
   - K2-GUARD-1 (`K2Guard.lean`, `no_candidateCone_cnot_reflY`): `CandidateCone` = all ball products and
     `K ⊆ maxCone`; with `cnot` and `actT reflY` invariance it gives `False`. The chain uses only `(x+, z+)` and the
     sharp effects along −e₁ and −e₃, as stated; `chain_value = −1/2` reproduced (R2e).
   - C-CP (`:211`) and its comparator-based motive (`:214`) and the U′ translation `Y ↦ −Y` (`:727-731`) are confirmed.
     Neither record cites the other (grep).
   - The "consistency only" label is correct (N5).
3. **Ordering and support.** Partly supported: B5, B6, N6–N8. The drafts were used as hypotheses only.
   - BRIDGE r2 (`3905569b…`) is now REVISE.
   - SHARED r5 (`a7206701…`), QX-6 r5 (`9e9c0d02…`) and QX-4 r5 (`7f4cd21d…`) hashes match the writer's.
   - SHARED §9 rows confirmed for SA-1(c) "QM-only" (row M3), R6.9, M20 and Tsirelson.
4. **Provenance.** Confirmed by REST and git:
   - #1173: `merged_at` 2026-11-07T20:04:12Z, merge commit `dc0b333a` (parents `e61e5673`, `62502618`), head
     `research/oi-qm-ext-1-gate-a-20261106`;
   - `e306143d` is an ancestor of `fd539e15`;
   - the blob is `1e6ced53…` at both commits;
   - the head branch is absent (`ls-remote` empty; REST 404);
   - `prepared-pair-source.md` blob `9123157c…`;
   - review c.6707141951 was posted by `amaybaum` at 12:48:17Z;
   - `0e0b3ddc` is not on `main`, and its branch exists.
   - The body-staleness wording needs N1.
5. **Probe misspecification.**
   - The disclosure is accurate on G3b. The corrected check matches the kernel: `chain_value` is
     `prodEffVal (sharpEff …)`, i.e. `pairVal` of `sharpVec = (1/2, a/2)`, which is `pairVal(hats)/4`, giving −1/2.
   - It is incomplete on the G7 addition (N2).
6. **Remaining checks.**
   - **§A.19.** `git grep` at `fd539e15` over `papers/`, `book/` and `verification/` for `herald`, `steer`,
     `self-dual`, `no-restriction`, `block-positiv`, `product-test validity`, `joint-test validity` and
     `carries the cone into itself` finds no record that sources joint-test validity physically. The `herald` hits are
     boundary-law bookkeeping in `oi-qm-ext-1/` and `composition-access`. It finds the DIM-1 kernel lemma (B3).
   - **Negatives.** Scoped, except:
     - "not found stated" (B3);
     - "not upstream of J13" (N7);
     - the PR-box non-implication (B4);
     - "J5 fails natively" in Q-868-H's "If no" branch (B1).
   - **Three columns.** Kept separate except J11/§6's Tsirelson item, which puts a quantum-representation premise in
     (ii) (B4). No row's (ii) is answered from (iii) otherwise.
   - **Register.** No §A.32/§A.33 problems. This is a record, not `papers/`; capitalized words are identifiers or
     §A.31 labels. "It is now on `main`" and "no longer on `origin`" are provenance statements and acceptable there.

## 4. What is sound and should be kept

- The J1–J14 ledger structure and its column discipline, apart from B4.
- The node-10 placement (in `maxCone`, outside Q3), with N4's strengthening.
- The C-CP consistency link, relabelled per N5.
- The FI-1-necessity of a non-monomial operation for J3 under Main:564 (G7), with B6's addition of the phase.
- The provenance record.
- The owner questions in §9, whose wording becomes conditional after B1–B2. D-02's proposed L-edge, for example,
  should not say the validity clause "reduces to a single-token body property".

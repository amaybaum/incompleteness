# QPHEN Phase 1 r5: independent full-text review

## Standing

- **Reviewer.** An independent, model-written review. It is read-only on the repository, git and GitHub. It writes
  only this file and the probe `review/probes/p10_r5rev_checks.py` with its output `p10_r5rev_checks.out`.
- **Files reviewed** (sha256 verified before reading; all match the brief and DISPOSITIONS-r5):

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `e231a795508769ce…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `7f4cd21d02a0dbf7…` |
  | `QX6-BELL-CHSH.md` | `9e9c0d02c48dfc74…` |
  | `SHARED-MECHANISM.md` | `a72067015789371a…` |
  | `DISPOSITIONS-r5.md` | `01ef37655352c0d8…` |

  The r4 texts under `r4/` match the hashes DISPOSITIONS-r5 lists. `REVIEW-PHASE1-r4.md` is `755c3af0…`.
- **Corpus.** `git fetch origin main` (no depth, gc or prune): `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`.
  `papers/Main.md` at that commit equals `main_fd.md` (`6144cd4a…`). Read at that commit: Main:44, :50, :56, :60,
  :362-421, :652, :726; Substratum:44, :48, :94-104, :270-276, :481; SM:240; AP1 (`apparatus-1-20261107/DESIGN.md`)
  :280-362.
- **Owner records read** (read-only): #1210 c.6739286623 (amaybaum, 11:47:25Z), c.6739311717 (11:48:47Z),
  c.6739250392 (11:45:26Z), c.6738866690 (11:25:06Z, decisions O1/O2).
- **Method.** All four specifications and DISPOSITIONS-r5 were read in full, and `diff r4/ r5` was read for every
  file. The writer's `p9_r5_symplectic_detector.py` (`47cd22cc…`) was re-run with `python3 -I` from a separate
  directory: exit 0, output identical to `p9_r5_symplectic_detector.out` (`de508afb…`); it imports only `itertools` and
  `sys`. The new probe `p10_r5rev_checks.py` imports no earlier probe and passes 32 of 32 checks.

## Verdict: **REVISE (narrow)**

r5 fixes B1, B2 and N1–N12 of the r4 review correctly. Q4-P19's three-line argument and its count
(0 of 11,520) are verified by hand and by an independent exhaustive probe. The five extra summary sites the writer
changed are correct.

One blocker remains. It is pre-existing, and it is one of the three findings from other drafts:
- **B1.** In SHARED §9, column (ii) states the N2 and SA-1(a) answers more strongly than Main's own posit ledger
  (Main:726). The N2 row answers "yes" for a selection that Main lists as a posit, "not derived". The table answers
  "no" for MI, which is also a Main posit and shares N2's conditional (Main:726 (v)).

The summary-scope check finds seven further must-fix mismatches (N1–N7). Two of them come from r5's own additions:
- N3: Q4-P19's "records" is defined too weakly for the reading that R4.9 and T2 give it;
- N4: Q4-P19 is not propagated to M16's "none identified".

The owner's added check (necessary physical conditions against design assumptions; coordinator relay of amaybaum,
chat, 2026-11-09) finds five further must-fix mismatches (N14–N18) and two precision items (N19–N20). In each, a
"needs", "must" or "required" rests on a design assumption, a protocol target or a W record without saying so.
(L′), (R), the comparator protocol, the `NCONS` domain, the `⊥` rule and (H2)/(H4) are labelled correctly wherever
they are named.

No theorem in the four files is false. Each fix is a sentence or a cell.

***

## Blocker

### B1. SHARED §9 column (ii): the N2 and SA-1(a) rows are stronger than Main's posit ledger

**N2 row.**
- **The cell.** Column (ii) reads "yes for the counting measure, Main's maximal-entropy selection, 'a selection
  principle, not uniqueness from invariance alone' (Main:56, Lemma 3)". The standing reads "native measure".
- **The source.** Main's posit ledger (Main:726) lists "(iv) the measure selection is a maximal-entropy principle
  … — a standard but substantive epistemic postulate, not derived". Item (v) ties the "typicality selection in (iv)"
  and the setting/preparation decorrelation of §3.3 to one open dynamical question: "one conditional wearing three
  hats".
- **The inconsistency.** The same table answers MI (Main (iv) of §3.3) "no: 'retained as a posit about the initial
  condition, not derived' (Main:406-412)", standing "posit, in Main". Two Main posits that share one conditional are
  typed in opposite ways.
- **Why it is a blocker.** A "yes" in column (ii) for an item its source calls "not derived" is the posited → derived
  pattern that the Code Review Rules make a blocker. Column (ii) is also exactly what the owner's three-question rule
  governs (c.6738337450; c.6739286623: "proving that a model reproduces quantum predictions under specified conditions
  is not proving that OI independently supplies those conditions").

**SA-1(a) row.**
- **The cell.** Column (ii) reads "yes, conditional on Substratum (A4)–(A5) …: the step's form, symmetry and
  symplecticity are native for the wave branch on that condition".
- **What the step's form needs.**
  - Main:726 (xiii) lists "the second-order form of the update, a posit of the selected lattice model, not derived
    and not an axiom of OI".
  - The uniqueness the row cites (Substratum:48) is "the unique second-order reversible nearest-neighbor dynamics …
    compatible with center independence, isotropy, and linearity". Second order and the nearest-neighbour premise are
    inputs to it, and the symmetric coefficients that symplecticity needs come from isotropy (E4; Main:726 (vi)).
  - (A4)–(A5) alone do not give the step's form or its symmetry.
- **The condition list is also wider than needed.** The row conditions on all of (A5), but only its affine part is
  used. A translation is symplectic, so the affine-symplectic class (A4.1, A3.1, Q4-P19) never uses linearity
  beyond affine. The affine part is itself conditional on amplitude-scale gauge "in the form that every first
  difference of the update is independent of its base point" (Main:726 (vii); SM:240; Substratum:100, :270-272: "an
  operational input …, not a theorem").

**Required fix.**
- **N2 row.**
  - Column (ii): type the measure selection as Main's posit (iv), "not derived" (Main:56, :726), consistently with
    the MI row. Either answer "no: a posit in Main", with its stated reason, or answer "conditional on Main's posit
    (iv)". Keep "open for its application to supplied ready cells (H-PREP)".
  - Standing: "posit in Main (iv); application conditional on H-PREP".
- **SA-1(a) row.**
  - Column (ii): "conditional on Main's posits for the selected lattice step: the second-order form (xiii), center
    independence (A4), the coefficient symmetry from isotropy (E4), and the affine part of (A5), which amplitude-scale
    gauge yields in its first-difference form (an operational input, open). Linearity beyond affine is not used."
  - Standing: "native element of the selected lattice model, conditional on those posits".
- **Rows that inherit.** The M15 row inherits the condition ("on the same condition as the SA-1(a) row"), so it needs
  no separate edit.

***

## Nits

**Must fix before freeze consideration** (N1–N7 are summary-scope mismatches under the owner's instruction,
c.6739311717)

- **N1. Some summary sites cite A6.1 with (L′) and (R) only, and omit (D) and (MI).**
  - Q6-P2 is "conditional on (D), (L′), (R) with the `⊥` rule, and (MI)". These sites drop (D) and (MI):
    - Q6-P10's header ("conditional on (L′) and (R)") and its first bullet ("Own-wing operations satisfying (L′) and
      (R) do not exceed 2");
    - QX-6 §8 item 2 ("A6.1 (multi-tick local settings under (L′) and (R), [A])");
    - QX-6 `A_6` ("for multi-tick ones that satisfy the design assumptions (L′) and (R)");
    - SHARED §4 controls, third item;
    - SHARED §3 "Cross-wing dynamics", first bullet.
  - Q6-P10's first bullet is false as written: measurement-dependent models with own-wing operations reach `S = 4`
    (Main:421).
  - Write "under A6.1's hypotheses ((D), (MI), and the design assumptions (L′) and (R))" at each site.
- **N2. "Insufficient separation" (QX-6 §3.2) is, as defined, every failure of (R). The new "Counting" necessity
  entry relies on it.**
  - §3.2 defines insufficient separation as `d_{G_B}(B, R_A) ≤ T_A − t_B`. That is exactly the failure of (R), and
    so the same condition as "a coupling path between the wings' regions shorter than the run". If the design
    excludes it, nothing is left.
  - SHARED §3 "Counting" (M19) and the new §8.4 proved entry then conclude that "the failure left is a coupling path
    … shorter than the run". The conclusion is true, but its stated route is incoherent.
  - Fix either way:
    - define insufficient separation in the designed reference graph (`d_{G_ref}(B, R_A) ≤ T_A − t_B`), so that the
      third case is `d_{G_B} ≤ T_A − t_B < d_{G_ref}`, a path through edges outside the design (as the r4 review
      noted, (R) is stated on `G_B`, which the dynamics fixes); or
    - derive M19's necessity directly. Under (D) and (MI), `|S| > 2` needs some outcome to depend on the remote
      setting (A6.1 step 6 in contrapositive). That dependence is a cross-wing response.
- **N3. Q4-P19's "records occupation" is weaker than the reading that R4.9, T2 and A4.4 give it.**
  - Q4-P19 defines "records" as "changes a meter slot on `c = 1`". Under that definition the translation
    `m ← m + 1` records, and it "acts on its silent branch" only through the meter, not the system (p10 (7b)).
    T2 uses "act on its silent branch" for M16, `K_null ≠ id`.
  - The intended strong form holds. Let `T` be affine-symplectic, location-preserving (`c′ = c`), with a meter write
    that depends on `c`. Then `T` changes the carrier conjugate `x` on some state with `c = 0`.
  - Proof:
    - Suppose `T` fixes `x` on `{c = 0}`. Then rows `c` and `x` of `M` vanish on the `m` and `m′` columns.
    - So `M e_m` and `M e_m′` lie in the meter span, and their meter block `B` is invertible, since
      `ω(Me_m, Me_m′) = 1`.
    - Symplecticity gives `ω(M e_c, M e_m) = ω(M e_c, M e_m′) = 0`. So the meter components `(β, γ)` of `M e_c`
      satisfy `(γ, β) B = 0`, hence vanish. That contradicts the meter write's dependence on `c`. ∎
  - Exhaustive check: 288 such maps, none an exception (p10 (7a)).
  - Restate Q4-P19 with this definition and conclusion. The 0 / 11,520 identity-on-`c = 0` statement is unchanged.
- **N4. Q4-P19 is not propagated to M16.**
  - In its strong form (N3), every location-preserving affine-symplectic detector coupling that records occupation
    has `K_null ≠ id` on the system. If the detector coupling is an SA-1(a) step, null-result invasiveness then
    follows, on the SA-1(a) row's condition (B1).
  - These sites still say the only support is agreement with QM:
    - SHARED §1 M16 ("its only identified support is agreement with QM");
    - §2 M16 × QX-4 ("QM-only");
    - §9's null-result row ("open; none identified"; standing "QM-only").
  - O1 (c.6738866690) prescribes "none identified (open)" only "wherever no QM-independent justification has been
    found". Restate column (ii) as for M15: "conditional: yes for detector couplings in the affine-symplectic class,
    from SA-1(a)'s step on that row's condition (Q4-P19); none identified for non-affine couplings (open)".
  - Keep "hypothesis under test" (O1), and restrict "QM-only" to non-affine couplings.
  - §A.31 caution, because this reading favours the framework: the route is conditional on SA-1(a)'s posits (B1);
    it covers only couplings that are SA-1(a) steps; and it gives no QM-matching value by itself.
- **N5. SHARED §1 M15's status, "holds in the affine-symplectic class", is wider than its proved support.**
  - Q4-P19 (strong form, N3) proves it for location detectors on `F_2⁴`.
  - For encoded meters the support is AP1 §3.2 [W], which Q3-O5 lists as open.
  - Write "holds for location detectors in the affine-symplectic class (Q4-P19); for encoded meters AP1 [W] (Q3-O5)".
- **N6. QX-6 §7, first block: "If any is missing → QX-6 is limited to `A_6` / `B_6-loc`".**
  - This holds when R6.5 or R6.7 is missing.
  - Missing R6.8 removes Level-2 credit (QX-6 §9). It does not bound `|S|`.
  - Missing R6.10 removes Level 3 only. Level 2 does not require Tsirelson soundness.
  - State the consequence for each prerequisite.
- **N7. QX-4 §7 item 3: "under (H1), (H2) and (H4) it needs null-result invasiveness (A4.4)".** A4.4 gives this only
  for a construction that matches the comparator protocol's prediction under INM. Add "to match the comparator
  protocol".

**Must fix: the owner's added check, necessary physical conditions against design assumptions**

Every "needs", "must", "required" and "necessary" in the four specifications was read: 109 sites, by grep. Each one
was classified in one of four ways:
- proved necessary under stated hypotheses;
- a requirement of the credited target (Level 2 or 3) or of a protocol;
- a design or programme choice;
- unsupported.

The following are mismatches.

- **N14. SHARED §3 "Core. Every column needs: M1, M2, M4 and M5; M6 …; M9 …; M21".**
  - These are construction B's design elements: N2 counting, H-PREP supplies, SA-1(b) meters, P3 arming,
    identifications typed IR, and the validation layer. No necessity is proved for them.
  - The only cited support for "needed" is `DESIGN-DS.md` §2 [D] (QX-3 `A_3`), and under §8's rule a claim resting on
    D alone is open.
  - Write "Every column uses, by the design of construction B: …". Alternatively, mark the necessity open [D].
- **N15. The necessity of a restricted preparation class rests on a W record that the ledger lists as open.**
  - The sites:
    - QX-6 §3.2: "Over an unrestricted preparation class this is impossible (prepared-pair-source §5 (W)), so a
      restricted preparation class is required";
    - A6.4: "R6.9 must be some state restriction";
    - QX-6 §8 item 4: "No-signalling needs supply laws in the kernel of the balance map (A6.4; W)".
  - Q6-O8 lists "the balance-map statements of prepared-pair-source §§4–5" as open (W only).
  - The necessity is also conditional on complete-history no-signalling. That is a requirement of the chosen branch
    and of the Level-2 witness ("stated and not derived", §9), not a derived physical condition. The preparation class
    fixed by balance equations is itself a design-type restriction, as §9's R6.9 row says.
  - Theorem recovery is cheap. Let a deterministic completion satisfy (MI), and let it satisfy complete-history
    no-signalling for every point-mass preparation `δ_Ω`. Then each wing's history at each `Ω` is independent of the
    remote setting, so the response functions are local and `|S| ≤ 2`. By linearity, the same holds for any class
    whose affine hull contains the point masses.
  - Record that argument [A] and state the conclusion conditionally: "if `|S| > 2` with complete-history
    no-signalling (Level 2's target), the admitted preparation class must exclude some point masses". Otherwise mark
    the sites as resting on W (open, Q6-O8).
- **N16. "Must exclude PR-type sources" (QX-6 §8 item 4; SHARED §3, H-SDC obstacle 4).**
  - This is the definition of R6.10, Tsirelson soundness, and R6.10 is a Level-3 target and a hypothesis under test
    (QM-only, §9). It is not a physical necessity.
  - Write "for Level 3 (R6.10, a hypothesis under test)".
- **N17. Bell prerequisites stated as needs without their basis.**
  - The sites:
    - QX-6 §8 item 2: "A Bell excess needs R6.7 (H-Bell)";
    - A6.2 "For #1210": "the binding prerequisites are R6.5, R6.7 and R6.8";
    - SHARED §5 QX-6: "the binding prerequisites are a pair source (M18), H-Bell's cross-wing response (M19) and
      complete-history no-signalling (M20)".
  - The three items have different bases:
    - R6.7 is necessary only under (D) and (MI) with the design assumptions (L′) and (R)-separation (A6.1; N1, N2);
    - R6.5 is presupposed by the protocol;
    - R6.8 is a condition of Level-2 credit, not a physical necessity.
  - Label each item by its basis.
- **N18. Obligation C "needed" or "needs" for QM-matching settings omits A6.2's premises.**
  - The sites: QX-6 §8 item 6; SHARED §5 QX-6, first bullet; SHARED §3 "Counting" (M12 for QX-6).
  - A6.2's necessity holds only when settings are identified as local read directions (an L-CAL-type
    identification, a representation choice) and local operations are Clifford-class. The §2 matrix cell and A6.2's
    title carry "QM-matching settings", but not the identification.
  - Add "with settings identified as local read directions and Clifford-class local operations (A6.2)".

**Precision (added check)**

- **N19.** SHARED §4 lists "`K₃ ≤ 1` at one mode, and at two modes under SA-1(c) or environment supplies" among the
  "controls an extension must preserve". The bound holds only with A4.1's read model, which is a design choice. Add
  "with A4.1's read model".
- **N20.** QX-4 §4 says "`G` must be C's, QX-1's or QX-7's operation". This is the programme rule of one shared
  mechanism (#1210 requirement 1; SHARED §0), not a physical condition. Cite the rule there, as QX-3 §7 item 3 does
  for FIX.

Correctly labelled, and checked:
- (L′) and (R): "excluded by the experimental design …, not by any theorem" (QX-6 §3.2), and the design-assumption
  typing at every site listed under the owner requirements below.
- The comparator protocol: defined in QX-4 §2, typed a comparator declaration in §9, with "QM-matching" defined
  relative to it.
- The `NCONS` domain: "a declared choice, not a derived one" (A3.1(d)), and owner question Q3-2.
- The `⊥` rule and full-mass accounting: protocol (§9).
- (H2) and (H4): protocol conditions (A4.4; §9). A4.4's "must violate (H3)" and "must have null-result invasiveness"
  are stated given (H1), (H2) and (H4), and R4.10 is "required if QX-4c-INM is to match the comparator protocol"
  under those hypotheses (QX-4 §7 item 3 excepted: N7).
- FIX: "programme rule" (§9; QX-3 §7 item 3; SHARED §3).
- M18 and M14 in "Counting": "by the protocols' definitions".
- The §2 matrix legend: "required for the experiment's … form", a design-relative notion.
- A3.1(c)'s "must be non-affine": under the declared `NCONS_global`.
- A4.1(c)'s "needs a non-Clifford `G`": under its stated hypotheses and the comparator protocol.

**Precision**

- **N8. Finding 5(c), Tsirelson soundness, §9 column (ii).**
  - "None identified" omits the corpus's conditional routes:
    - Substratum:481's first sentence: the cited stochastic causal-local indivisible sector gives `2√2`;
    - Main:652's "one common tensor-product instrument category", not established. With it, Tsirelson's theorem
      applies.
  - Both premises are quantum-structured. Local tomography alone is not enough: generalized no-signalling theory
    ("boxworld") is locally tomographic and contains PR boxes (L). So "open" and "QM-only" stand.
  - Name the routes and their conditions.
- **N9.** The owner's summary-scope instruction, c.6739311717 (amaybaum, 2026-11-09T11:48:47Z), is not among the owner
  records in QX-3 §0, QX-3 §10 or SHARED §7. DISPOSITIONS-r5 cites it only through `R4-REVIEW-ADDENDA.txt`.
- **N10.** The SHARED §8 rule "the original, narrower claim is listed as open" should add the owner's "unless
  separately established" (c.6739286623). Q4-D3's narrower form is listed as proved (Q4-P19).
- **N11.** QX-4 §10 has no row for R4.9's citations of SHARED Q4-P15 and Q4-P19, and through them p8 and p9. §A.42
  item 8 tracing needs one, in the manner of the row "QX-3 A3.1 (this programme)".
- **N12.** The paper expectations of `A_6` and `B_6-loc` (`|S| ≤ 2`) are stated as consequences of proved results, but
  they are in no ledger list: Q6-O10 covers only `B_6-nl` and the ablations. Add them to Q6-P10, with A6.1's
  hypotheses (N1).
- **N13.** Finding 5(b). Where SA-1(a)'s row names the affine input, name it in its first-difference form (B1). A
  site-uniform gauge does not force affinity in `d ≥ 2` (p10 (6)).

**Optional**

- ABL-G's "`≤ 1` at A4.1(a)–(b)'s scopes" could read "at one mode, and at two modes under SA-1(c) or environment
  supplies", since A4.1(b) also contains `K₃ = 2`.
- The §A.31 method notes ("because that reading favours the framework") remain; as the r4 review noted, they are
  outside §A.32's `papers/` scope.

***

## Items 5(a)–(c): claims from unreviewed drafts, checked against sources

| item | verdict | basis | class |
| --- | --- | --- | --- |
| (a) the N2 row's column (ii) "yes" should be typed as a posit | **correct** | Main:726 (iv) "a standard but substantive epistemic postulate, not derived"; Main:56 "a selection principle". The table answers "no" for MI, a Main posit tied to the same conditional (Main:726 (v); :406-412) | **blocker** (B1) |
| (b) SA-1(a) column (ii) "conditional on A4 and the affine posit; linearity beyond affine not used" | **correct as far as it goes, but incomplete** | Linearity beyond affine is not used: translations are symplectic, and every affine-symplectic result in these files admits them. The wording still omits the second-order-form posit (Main:726 (xiii), "not derived") and the coefficient symmetry from isotropy (Substratum:48). The "affine posit" is amplitude-scale gauge in first-difference form, "an operational input" (Substratum:272) | blocker as part of B1 (the row's condition list); the wording point itself is N13 |
| (b′) companion: the uniform gauge principle does not imply affinity in `d ≥ 2` | **correct**, reading "uniform" as equivariance under one site-uniform additive automorphism | p10 (6): over `Z_5`, `F(nb) = 2·mean + p₂(y)p₃(y)`, with `y` the neighbour values minus their mean, reads the 6 neighbours and not its own site. It is symmetric under all 720 neighbour permutations, satisfies `F(λx + c) = λF(x) + 2c` for every unit `λ` and every `c` (exhaustive over `Z_5⁶`), and is not affine. The second-order step therefore commutes with every global additive automorphism. In `d = 1` with reflection symmetry such a correction is forced to vanish for odd `q`, which is consistent with "`d ≥ 2`". This agrees with Substratum:272 and SM:240, which obtain affinity only from the per-coordinate first-difference form. `q = 2` was not checked | nit (N13); the r5 text makes no claim that uniform gauge implies affinity |
| (c) Tsirelson's "none identified" omits a conditional route | **correct, with a correction** | Local tomography together with a quantum pair dictionary gives no-signalling and `2√2` (Tsirelson's theorem), and the converse fails (L). The bound comes from the dictionary alone: boxworld is locally tomographic and admits PR boxes. The corpus also has Substratum:481's conditional route. Both premises are quantum structure, so column (ii) stays open and the standing QM-only | nit (N8) |

***

## r4 blockers and nits

| r4 item | present in r5 | correct | notes |
| --- | --- | --- | --- |
| B1 (Q4-D3; affine-symplectic form) | yes (Q4-D3 restated; membership adds non-symplecticity; Q4-P19 new; R4.9; Q4-P15; §7 rows) | yes | Q4-P19's argument re-derived by hand. p10 (1)–(2): 20,160 / 720 by two methods (Gram test; closure of transvections). 0 of 11,520 affine-symplectic; 6 of 322,560 affine; the two affine-symplectic maps that are the identity on `c = 0` are the identity and `x ← x + c`. Extension to three modes: `d ∈ span(e_x)` again. Wording of "records": N3 |
| B2 (QX-3 §7 item 5) | yes | yes | Now lists both of A3.1(a)'s hypotheses. p10 (4) realizes `9/50` with a uniform law and non-affine functionals, and re-checks A3.1(a) on every coset of `F_2³` |
| N1 (§8 rule wording) | yes (§8 rule; Q4-D1 "as restated", "Restatement") | yes | "unless separately established": N10 |
| N2 (`K₃ ≤ 1` "only at (a), (b)") | yes (A4.1(c); §7 item 2) | yes | integer and `≤ 3/2` give `≤ 1` |
| N3 ("not sufficient" condition) | yes (A6.2 title; M12 × QX-6) | yes | |
| N4 (§3 "Counting") | yes (§3; §8.4 proved and open entries) | conditions yes; M19's route: N2 | |
| N5 (W2 class) | yes (QX-3 §2, §7 item 7; SHARED §5; and three own-pass sites) | yes | |
| N6 (outcome-independent kick) | yes (T2; A4.4 Consequence) | yes | |
| N7 (`A_4` arm) | yes | yes | |
| N8 (D labels) | yes | yes | a grep finds no residual `(D)` on any probe in the bodies |
| N9 (P-ranges) | yes, per file | yes | |
| N10 (`⊥` rules) | yes (Q6-P10; ABL-BOT) | yes | steps 5–6 re-read: only that each outcome is a function of its readout region is used |
| N11 (R6.4 type) | yes | yes | |
| N12 (second probe) | yes (Q3-P6a; Q4-P7; Q4-D1) | yes | |
| own-pass sites (5) | QX-3 §6 C-SURVIVAL; QX-3 §8 Level 2; QX-3 §9 Q3-1; QX-4 ABL-G; QX-6 ABL-NL | yes, all five | ABL-G wording: optional nit |

## Owner requirements (#1210 c.6739286623; c.6739311717)

| requirement | status | basis |
| --- | --- | --- |
| Bell locality: design assumptions; proof conditional | **met; (D)/(MI) omitted at five sites (N1)** | (L′) and (R) are typed as design assumptions at A6.1, R6.2, R6.4, §9, Q6-P2, A6.2, M12 × QX-6, ABL-NL, `A_6`, §3, §4 and §5. The proof was re-read and is unchanged |
| The three questions stay separate; (iii) never supports (ii) | **not met (B1)** | No (iii) → (ii) citation was found. Column (ii) is stronger than its source for N2 and SA-1(a) |
| Membership; the narrower claim stays open | **met** | 11 of 11 lines valid (table below). Q4-D3's narrower form is proved (Q4-P19), which is allowed ("unless separately established"); rule wording: N10 |
| Leggett–Garg configuration exact | **met** | p10 (5), sympy, Schrödinger picture with Lüders projectors, written independently: `(cos β, sin β, 0)` for G1; `K₃ = cos β + sin β` for G2; `√2` and `7/5`; `H` on the carrier gives `−cos β` and `0`; G1 and G2 unitary |
| Generic checks labelled; probe-only results computation-supported; no computation on an OI mechanism | **met** | Q4-P19 is A + X (not computation-supported, correctly). p9 and p10 act on generic `F_2` and `Z_5` objects only |
| Necessary physical conditions kept distinct from design assumptions (owner, chat, 2026-11-09, via the coordinator) | **not met (N14–N18); precision N19–N20** | (L′), (R), the comparator protocol, the `NCONS` domain, the `⊥` rule and (H2)/(H4) are labelled correctly where named. The mismatches are "needs" or "must" statements whose basis is construction B's design (N14), a W record listed as open (N15), a target's definition (N16, N17) or an omitted representation premise (N18) |
| Full re-read; summary-scope check | **done; seven mismatches (N1–N7)** | New errors traced to r5's edits: N3 and N4 (Q4-P19) and the route in N2 (via "Counting"). Earlier errors not caught in r4: B1, N1, N5, N6 and N7 |

## Membership check of every disproved entry

| entry | counterexample in the refuted class? | verdict |
| --- | --- | --- |
| Q3-D1 | `L(s,1,0)`: `s = 0 ↦ (0,1,0)`, `s = 1 ↦ (1,0,1)`; weights 1→1 and 2→2; linear bijection; own-cell reads | valid |
| Q4-D1 (restated) | ordinary kicking `t₁` read, so (H2) fails as required; (H1) and (H4) hold; mixture `3/4·2 + 1/4·0 = 3/2`; the `t₂` kick misses `z₃` | valid; INM form open (Q4-O8) |
| Q4-D2 (restated) | witness `G` checked symplectic by hand for `(z, x)`, `(v, w)` (all six pairings); two modes; sharp mediator admitted | valid; `A_4` open (Q4-O6) |
| Q4-D3 (restated) | copy coupling: linear, identity on `c = 0`, records; not symplectic (p10 (3a)). The claim is now over affine maps, not necessarily symplectic | valid; affine-symplectic form proved (Q4-P19) |
| Q4-D4 | both instruments trace-preserving with `Z` effects; `G = X` unitary; two-read correlators | valid |
| Q4-D5 | `CNOT` Clifford; Lüders `Z`; preparation unrestricted | valid |
| Q4-D6 | Clifford `G1`, `G2`; Lüders carrier `Z`; two modes; non-stabilizer preparation admitted (p10 (5)) | valid; OI value open (Q4-O2) |
| Q4-D7 | maximally mixed state; Lüders `X` does not commute with `Z` | valid |
| Q6-D1 | one-tick `op_A ∘ φ ∘ op_B`; (D), (L), single-graph (R), (MI) as listed | valid (r4's rebuild; unchanged) |
| Q6-D2 | `X/Z` only; product of the four predictions `−1` against `+1` for any local assignment | valid |
| Q6-D3 | GHZ-1; `x_i = z_i = +1` satisfies `ZZI`, `IZZ`, `ZIZ`, `XXX` | valid |

## Summary-scope mismatches (complete list)

The comparison covered every summary-level statement against its supporting entry: §0 blocks, witness tables and
"Consequence" paragraphs, the requirement tables' type and status columns, derivation titles, arm and ablation
tables, decision trees, obstacle lists, ladder mappings, SHARED §§1–5 and §9, and §8.4.

| # | site | as stated | support's scope and status | fix |
| --- | --- | --- | --- | --- |
| 1 | SHARED §9 N2, column (ii) | "yes"; "native measure" | Main:726 (iv): posit, "not derived" | B1 |
| 2 | SHARED §9 SA-1(a), column (ii) | conditional on (A4)–(A5) only | also (xiii) second-order form, a posit "not derived", and isotropy; linearity unused | B1 |
| 3 | Q6-P10; QX-6 §8 item 2; `A_6`; SHARED §4 controls; §3 cross-wing | A6.1 under (L′), (R) | also (D), (MI) | N1 |
| 4 | SHARED §3 "Counting" (M19); §8.4 proved entry | via "insufficient separation" excluded by design | as defined, that is every failure of (R) | N2 |
| 5 | Q4-P19 statement; R4.9; T2 | "records … acts on its silent branch", read as `K_null ≠ id` | weak "records" admits meter-only maps; strong form true (p10 (7)) | N3 |
| 6 | SHARED §1 M16; §2 M16 × QX-4; §9 null-result row | "only identified support is agreement with QM"; "none identified" | Q4-P19 (strong form) with SA-1(a): conditional support in the affine-symplectic class | N4 |
| 7 | SHARED §1 M15 | "holds in the affine-symplectic class" | Q4-P19 for location detectors; W only (Q3-O5) for encoded meters | N5 |
| 8 | QX-6 §7, first block | any missing prerequisite limits QX-6 to `A_6` / `B_6-loc` | true for R6.5 and R6.7 only (QX-6 §9) | N6 |
| 9 | QX-4 §7 item 3 | "needs null-result invasiveness" | only to match the comparator protocol (A4.4) | N7 |

Checked and consistent, beyond the r4 list:
- QX-3: §2's Consequence, §6, §7 items 1, 5 and 7, §8, §9.
- QX-4: A4.1(c) and its new sentence (an integer `≤ 3/2` is `≤ 1`), A4.2, A4.4 Consequence, §5, §6, §7 items 2 and 8,
  §8.
- QX-6: A6.2 (title and body), §2's witness table, §3.1, §9, ABL-BOT, ABL-NL.
- SHARED: the M12 × QX-6 cell, §3 "Counting" M12 / M18 / M14 conditions, T2, T9, §5, §8.4 other entries, and the
  §9 rows for (L′)/(R), MI, `⊥`, H-PREP, NCONS, FIX and L-*.

## Register and authorization

- **§A.32 and §A.33.** A scan of the 125 added lines finds four-letter capitals only in identifiers (`MECH-OPEN`,
  `NCONS`, `CHSH`, file names), and no history phrase, reader instruction or self-assessment. A full-text scan finds
  only the §A.31 method notes already recorded, and the mathematical "no longer than" (QX-6:324).
- **Authorization.** No text implies a D19–D23 decision, a freeze, a dispatch or construction. Every rule is marked as
  an outline, not frozen. DISPOSITIONS-r5 line 9 keeps D19–D23 separate.

## Probes

| probe | sha256 | result |
| --- | --- | --- |
| `p9_r5_symplectic_detector.py` (writer; re-run) | `47cd22cc6cdd4904…` | 13 of 13 pass; output identical to `.out` (`de508afb…`); exit 0 |
| `p10_r5rev_checks.py` (this review; imports no earlier probe; generic objects only) | `ca3607952c244aa7…` | 32 of 32 pass; output `p10_r5rev_checks.out` (`7ec5713f45268cde…`); exit 0. Exact (integers mod `q`, `Fraction`, sympy). (6b) and (6d) test equivariance exhaustively and non-affinity by an exhibited witness pair |

p10's sections:
1. `GL(4, F_2)` built column by column. `Sp(4, F_2)` built twice, by the Gram test and by closure of transvections.
   Q4-P19's counts.
2. The three-line argument's steps, and its extension to `F_2⁶`.
3. The copy, reciprocal and occupation-conditional couplings.
4. Q3-P11 and B2's non-affine realization; A3.1(a) on `F_2³`.
5. The exact LG configuration.
6. Finding 5(b)'s companion claim.
7. Q4-P19's strong form (N3).

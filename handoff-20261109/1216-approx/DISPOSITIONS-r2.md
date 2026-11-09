# Dispositions, `APPROX-UNIT1.md` r1 → r2 (#1216 unit 1)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Change map for r2. It authorizes
nothing, and no git, repository or GitHub write was made.

- **r1:** `r1/APPROX-UNIT1.md`, sha256 `310b907a7adcab8d81b32be104719e2d9d48934f9cb78c8011fc15e3e892151b`,
  copied byte for byte.
- **r2:** `APPROX-UNIT1.md`; its hash is reported to the coordinator, not recorded in this file.
- **Review:** `review/REVIEW-APPROX-UNIT1.md`, sha256
  `b131792e6d7e6c19832ea6aca9779c65c075c1eb75e2c6e00ccbbaa39b6810c2`, verdict REVISE (B1–B3, N3–N13).
- **Sources:** `git show fd539e15:<path>`. `origin/main` = `cac5d264` differs only in `papers/SM.*`.
  Owner records were read with `gh api`: #1216 c.6741763726, c.6742051100 and c.6742191828, and #1169
  c.6742190154.
- **Verification policy.** Each finding was checked before it was applied, in one of three ways:
  - against the source at `fd539e15`;
  - against the Lean source, by reading definitions and statements (no kernel build);
  - by a new exact check in `probes/r2_*.py`, which imports nothing earlier.

  The four reviewer probes were re-run, and their outputs are byte-identical to the recorded ones.

New r2 probes, each run with `python3 -I -B` from `/tmp`, exit 0, output deterministic:

| File | sha256 | Checks |
| --- | --- | --- |
| `probes/r2_frames.py` | `aa02e479a0d93ba7ccb6ccb5f9a40c7b0e2065e5f3d7c30d3bdbb2d78010548a` | F1–F5 + controls: 30 PASS |
| `probes/r2_frames.out` | `a116e91999a566f9d409f857325be4e1d94a47c24da62f7ec6eb73e491be0209` | |
| `probes/r2_routeC.py` | `b71749e47f742338d6373aaccae08bdaa96c985c29172b36ba1267e60ac72f97` | C1–C7: 24 PASS |
| `probes/r2_routeC.out` | `5626b5a8db40d7ade57542ea297c1c6afb2da32bcd5838ed013d9b02d2e538ec` | |
| `probes/r2_finiteb.py` | `383c21567671c73e9565b65c8846dfdc4ab385bf285321cd22b83b72c9b6e07c` | N5a–c: 3 PASS |
| `probes/r2_finiteb.out` | `6350b5c11822166bff80b9eacde330a14513390cbda0dc117cc45f26ed4df7b1` | |

***

## Blockers

### B1. Route-C quantum compatibility holds; coverage fails

**Verified.**
- The owner's wording in #1216 c.6742051100 is: "quantum compatibility: the resulting joint states
  correspond to quantum states under the stated comparison".
- Under that wording, route C's reachable states are diagonal with nonnegative entries, so they are
  quantum states, and its branches are CP diagonal-preserving maps. Compatibility therefore holds.
- What fails is coverage: TD ≥ ½ for x+⊗z+ and y+⊗z+ against every diagonal state, attained at
  diag ρ (r2 C6, which also includes a compatibility control).

**Changes.**
- **§1 "Three outcomes":**
  - replaced by the owner's verbatim definitions;
  - each claim now states its admissible state space and its comparison;
  - *coverage* is defined as a fourth, separate entry, "not folded into closure".
- **§5.1 table:**
  - new column "Coverage of the target class";
  - the compatibility column is retitled "Quantum compatibility (comparison)", and each row states its
    comparison;
  - route-C row: compatibility "**holds trivially** …"; coverage "**Fails, ε-robustly**: no coherent
    preparation within trace distance < 1/2 … law level: (√2 − 1)/2";
  - the coverage content that r1 had placed in the compatibility column of rows A1, A3 and density
    moves to the new column.
- **§5.1 "Independence witnessed":** route C is dropped from the witness list. One sentence is added:
  route C "is not a witness among the three … the three outcomes together do not give coverage".
- **§5.2:**
  - the reading sentence is rewritten. It keeps the owner's outcomes apart, and says that "#868's J3
    joins coverage and closure in one requirement; here they are reported separately";
  - item 1 is retitled "closure, validity and compatibility hold trivially; coverage fails, ε-robustly,
    at every carrier size";
  - the verdict now reads "keep closure, validity and compatibility, trivially, but do not reach the
    needed joint states".
- **§0 item 6:** rewritten to match: "*configuration carrier:* closure, validity and compatibility hold
  trivially …; coverage of the needed joint states fails, ε-robustly".
- **§9:** new entry F8 (ELABORATING).

**Terminology.** The review's repair text says "inclusion"; r2 uses "coverage", the review's other word
for the same property, throughout. This is a choice of term, not a refusal.

### B2. E_f "states yes" is false under R1; split the frames

**Verified.**
- **Sources.**
  - AP1 §4.2 (AP1:513–519) defines R1 as a law ↔ the Bloch-type vector of expectations of
    ((−1)^z, (−1)^x, (−1)^{z+x}), with |v| = √3. So μ_λ = (1 + v_λ·r)/4, and the frame is orthogonal.
  - MECH-2 node 2 states Lemma F "with an orthogonal frame {A(λ)} … (R1^⊗n at q = 2)".
  - Main:562 is the SIC map p_i = (1 + a_i·r)/4.
- **r2_frames, computed independently of the reviewer's code and in AP1's own (Z, X, Y) convention.**
  - F1: R1 is orthogonal. SIC's reconstruction frame is not (tr D₀D₁ = −1). R1's functionals have an
    eigenvalue of (1−√3)/4, and SIC's are PSD.
  - F2: all 24 single-qubit Clifford unitaries, generated from H and S, have identical frame matrices
    in both frames. 12 are permutation matrices, and the other 12 have a minimum of −1/2.
  - F3: CNOT, in both orientations, has a minimum of −1/4 under R1 and 1/4 − √3/3 under SIC, and its
    two frame matrices differ. Countercontrol: SWAP has the same frame matrix in both frames.
  - F4: r = −v₀/√3 has R1 coordinate (1−√3)/4 and SIC coordinate 0. Φ⁺ has an R1 minimum of −1/8 and
    a SIC minimum of 0.
- **Lemma F's proof** (MECH-2 node 2) uses only that the operations are nonnegative matrices on laws
  and that the identification is linear and injective. Orthogonality enters only Theorem U2's proof
  (node 3, "T_π permutes an orthogonal basis"; ":447 … real orthogonal matrix"). Applying Lemma F to
  SIC is therefore an [A] extension, as the review says (N-E1).

**Changes.**
- **§1 Carriers.** E_f is split into **E_f(R1)**, **E_f(SIC)** and **E_f(U′)**. Each has its
  definition, the orthogonality fact, a [G: r2 F1] citation and a QP line citation. U′ is listed
  because §5.1's r1 E_f row was about QP node 10, which uses U′, not R1 (see W4).
- **§4.2.**
  - The route-E_f class is restricted to the injective identifications (R1, SIC); for U′, "no class is
    fixed here".
  - The witness paragraph is rewritten: single-qubit frame matrices coincide in the two frames, while
    CNOT's minimum is "−1/4 under R1 and 1/4 − √3/3 ≈ −0.327 under SIC, in either orientation".
  - "Where native constructions sit" is split into *E_f(R1)* [W, conditional] and *E_f(SIC)* "[A, this
    unit's extension of Lemma F]", with the reason given. U2 is stated as not extended.
  - "Not sufficient": U2 is scoped "under R1^⊗n".
- **§5.1.** The r1 row "Route E_f, native encodings under R1 (MECH-2, QP node 10)" is replaced by two
  rows: **E_f(U′), QP node 10** and **E_f(R1), MECH-2 P★** (W4).
- **§5.2 item 2.** Rewritten as "frame-dependent", with these parts:
  - *States under SIC — representable*;
  - *States under R1 — not all representable, ε-robustly*, with the exact witnesses, the
    trace-distance bound (W3) and AP1:872–878's single-qubit instances;
  - closure in either frame;
  - entangling continuation, with the CNOT minimum per frame and Lemma F (R1 [W]; SIC [A]);
  - a verdict per frame.
- **§5.2 verdict and §0 item 6.** Frame-dependent wording.
- **§7.**
  - D20's assumptions now begin "orthogonal frame (R1^⊗n)", and its carrier is E_f(R1).
  - D21 is rewritten for E_f(R1): representation fails ε-robustly (proved here, exact); NX-1 and
    entangling remain conditional on D20; CNOT −1/4.
  - New row **D27** for E_f(SIC): representation proved; NX-1 and entangling conditional on the [A]
    extension; CNOT 1/4 − √3/3. D21 is not renumbered.
- **§8.** The R1 row's column (iii) now includes the non-representation. The column (ii) attribution is
  corrected from "MECH-2/QP" to "AP1/MECH-2", because QP does not use R1. A SIC row is added.
- **§9.** New entry F7 (NEW), with an assumption-watch marker: an "encoded" statement names its
  identification.
- **§10 OQ2.** "E_f (under which identification: R1, SIC or U′)".

### B3. Theory-level witnesses for the two non-implications

**Verified in Lean source at `fd539e15`** (statements and definitions read; no build):
- **Definitions.**
  - `Architecture` (ImplementationLocality.lean:506–515) has five fields: one, mul, smul (‖a‖ ≤ 1),
    proj and block.
  - `ancBlock` (AncillaClosure.lean:457) is `K (s, f) (t, e)`.
  - `InstAvail.op` (ImplementationLocality.lean:271–272) requires `Kᴴ * K = 1`.
  - `IsMonomial` (SubstratumInterface.lean:75) is `permMatrix σ * diagonal d`.
  - `genTheory` (:852) makes availability `InstAvail`.
- **`realized_of_instAvail`** (:530) writes every branch as Σ conj(K_i) with 𝓘 K_i.
- **The polarized theory.**
  - `polarizedTheory = genTheory PolGen polGen_arch` (C5Discovery.lean:247).
  - `polarizedTheory_swap_half_level_one` (C5Discovery.lean:325) states the level-one availability of
    the gate flow of `swap 0 1` at ½ in `polarizedTheory (Fin 2)`.
  - `polarizedTheory_not_layerFlowExecutable` (PolarizationClosure.lean:395) holds for every σ with a
    moved point.
- **The gate flow.**
  - `gateFlow_half_not_preservesDiag` (LiftAudit.lean:155) holds for σ a ≠ a.
  - `LayerFlowExecutable` (LiftAudit.lean:112) means ∀ n t, available at `availExt n`.
  - `gateFlow_unitary` (LiftAudit.lean:69) needs σ involutive (W7).
- **r2_routeC exact checks.**
  - C1: CM is closed under the architecture's fields, symbolically (3×3 products, 64² pattern pairs;
    4×4 ancilla blocks, 625 patterns).
  - C2: every CM conjugation preserves diagonals. Countercontrol: the Hadamard.
  - C3: K = |0⟩(⟨0|+⟨1|)/√2 is CM, not monomial, with K†K ≤ I. A CM matrix with K†K = I has a
    permutation pattern.
  - C4: the gate flow at ½ has entries (1±i)/2, and its conjugation of |0⟩⟨0| has off-diagonal i/2.

**Changes.**
- **§4.2.** The r1 paragraph "Relation to FI-1" is replaced by "Relation to FI-1 and to layer-flow
  executability (route C)". It has four directional bullets (§A.34):
  - NX-1 ⇒ FI-1, scoped as in W2;
  - FI-1 ⇏ NX-1, with the column-monomial counter-model in four sub-bullets [A + G, kernel-definition
    level, not kernel-checked]. The r1 operator-only witness is removed;
  - layer-flow executability ⇒ NX-1, for an involution;
  - NX-1 ⇏ layer-flow executability, via `polarizedTheory (Fin 2)`: three kernel theorems composed
    here, not one theorem. It also states that `polarizedTheory` adds two operator images, so the
    witness says nothing about OI's access.

  The summary sentence "So, on route C, NX-1 is strictly stronger than FI-1 and strictly weaker than
  layer-flow executability" now follows the witnesses.
- **§0 item 3, §7 D17, §9 F3.** Updated to cite the counter-models.

## Nits

| Nit | Verified | Change in r2 |
| --- | --- | --- |
| **N3** | `obs_availExt_le_substratum` at SubstratumInterfaceAudit.lean:837 is used at ExecSource.lean:129. `substratumTheory = genTheory substratumClass` (RouteB.lean:284). Main:564 rule (f): "an available preparation, followed by an available family at its level and by discarding the ancilla through the partial trace, induces an available family on the system". | §4.2 route C bullet cites `obs_availExt_le_substratum`, `substratumTheory` and rule (f). **Modified, not as worded.** The review asks for "the reading that a native system-level procedure built with rule (f) is available at `availExt 1`". That reading does not follow for a family at level n > 1. What does follow is an inheritance argument: attaching a uniform ancilla and taking the partial trace both preserve diagonal matrices, so a rule-(f) system map preserves diagonals whenever its level family does [A]. r2 states that argument instead (see also W2). |
| **N4** | C5 is reproduced: TV2 − p(1−p) = (1−q)(1−p); g = 1/4 − g²; attainment at (1/√2, 1); a 41×41 rational-grid control; coherent countercontrol with gap 0 (r2 C5). | §4.2 gains a paragraph "*Law level (route C)*", with the witness and its scope sentence. §1 adds "no memory outside ℂ^S" to C and defines **C-dyn**. Relabelled C-dyn: §2.1 carrier row (A1, A2; A3 "as A2"), and §7 D2, D3, D9, D10, D11. **Beyond the review's list,** by the same criterion: D1 (Q_fb's hidden part) and D24 (H-Bell's ontic-graph dynamics) are C-dyn too. D13–D19 and D26 stay C (route-C identification or exact QM on ℂ^S). |
| **N5** | My own instance (r2 N5) reproduces the reviewer's b = 12, det −325/2097152 under round-to-nearest. It also finds instances under floor rounding and for a rational 3-4-5 rotation. Control: the exact product is rank one. Clipped Z-read probabilities are valid. The window b ≥ log₂(2K C_{d,R}) = 11 at K = 1, d = 2, R = 1 comes from Main:568/:576. | §5.1, "A2 at finite b" closure cell: cites the instance "[G: r2 N5; RV rv_finiteb]", scoped as an instance under a stated reading. §11 states that it does not bear on the open law-level bound. |
| **N6** | Main:578: "Status: the instrument-level inequality is proved". #945 c.6567863298 item 6 and c.6567879503 §6 (owner question 6) say the complex-entry constant is only estimated. The question is undecided (#945 c.6657435508: readiness "blocked: owner questions"). | §7 D5 status: "stated proved on `main` (Main:578 …); the complex-entry constant is contested off `main` (#945 owner question 6, undecided)". Evidence: "[OFF] for the qualifier". |
| **N7** | Each reference was traced: `6d494e30` and `16fc745d` exist locally on `origin/audit/intro-corpus-20261026`, and neither is an ancestor of `origin/main`. The values match #945's comments verbatim. Main at `7c6ceaaa` (an ancestor of main) states two other exact failures (d = 3, d = 4), removed by `4cef4200` ("the instance numbers and the undefined estimate are gone"). | The single group label in r1 §1 is replaced by **§1.1 "References off `main` (§A.42 item 8)"**: a 17-row table classifying each reference separately against its attached claim. The rows cover owner comments; #945's comments, one per claim (D4a, the §2.2 limitation, D4b, the review verdict, the D5 qualifier, planning status); the branch record; the superseded `7c6ceaaa` text (on main's history, not used); the [D] drafts; Issue labels; and literature. D4a, D4b, D5 and §2.2 are marked support off `main`. F0 is marked provenance, its support being on `main`'s history. D4a's status now reads "disproved off `main` [OFF]; on `main` stated as not established (Main:578)", and §0 item 1 says the same. Where a [D] item was re-derived (QP node 10's non-quantumness, r2 C7), the row says the [D] use becomes provenance. |
| **N8** | `git show` confirms that at `7c6ceaaa` and `7c6ceaaa^` the four results sit at 544, 556, 576, 578, and at `02009693` at 566, 578, 598, 600. Both commits are ancestors of `fd539e15`. | F0 now quotes c.6567863298's actual sentence and states that "the uniform +22 offset is this unit's inference, checked on `main`'s history". It also replaces "the negativity-ledger text no longer exists" with the exact state: one remaining "negativity", in the check-16 description. |
| **N9** | Main:574 composes by I_a ⊗ I_b on the joint register. Nothing there relates a component's realization to the composite's marginal. | §0 item 2: "meets Level B's *shape* for one fixed system, a composite counting only as one d_A d_B system … not a compositional mechanism". §3.2 B-3 gains a matching sentence. OQ1 gains the scope clause. |
| **N10** | The bibliographic details match my recollection [L, not re-read]. Solovay–Kitaev's rate assumes an inverse-closed set. | §6 continuity cell: generic density is "[A, by analogy with Lloyd … and Deutsch–Barenco–Ekert …, which concern almost every two-qubit gate applied to chosen qubit pairs [L]]", and the rate is "for an inverse-closed generating set …; inverse-free versions exist, recalled, not checked". D19's assumptions gain "a gate set generating a dense subgroup (inverse-closed, for the stated rate)". |
| **N11** | Main:482 says "for every action sequence". Main:520's \|C_H\| formula has N = Σ_{k=1}^K n^k over history contexts x_{≤k} only. | §2.1 Experiments (A1) labels adaptive coverage "[A: the chain-rule reading …]". §2.1 Resources (A1) says the formula is for the passive comb and that for the action-labelled comb N counts (x_{≤k}, a_{≤k}) contexts plus the ledger factor [A]. |
| **N12** | QP = `quarter-phase-native-20261107/DESIGN.md` (BRIDGE and A1059 define it so). MECH-2 calls the same record "QA". | Defined in the header's source snapshot, and E_f(U′) is defined in §1 with QP:448–450. |
| **N13** | — | §11 now says that the two intermediate G4–G5 versions were not retained, that only r0, r1 and the final version are kept, and that "r1 is a passing run of G1–G3 only". |

## Other review content applied

| Item | Change |
| --- | --- |
| N-E1 (Lemma F under SIC is [A]) | Folded into B2 (§4.2 *E_f(SIC)* bullet; D27). |
| §3 Harrigan–Spekkens precision ("ρ-ontic"; Found. Phys. 40, 125 (2010)) | §1 E_r: the citation is added, scoped "for pure preparations entered as channels", with "precisely, it stores an unnormalized density register ("ρ-ontic")". |
| §5 E_r confirmation (rv_Er) | §5.2 item 3 cites the reviewer's instance as [RV], re-run, with "In exact ring this is exact closure, not an approximation phenomenon" (review wording). §1 [RV] defines how reviewer checks are cited: never as sole support. |
| §8 "G1b's `solve`-based check is weak; the closed form is decisive" | No change. The r1 probe stays unchanged for provenance, and G1b's verdict rests on G1a's closed form, trace norm 2√((a−½)²+¼), minimized at a = ½. |
| §9 §A.31 count | §9 records the review pass and its NEW (F7) and ELABORATING (F8) findings. The fixed point is not reached. |

## Owner context (not review findings)

| Item | Change |
| --- | --- |
| #1216 c.6742051100 is now posted | r1's "relayed by the coordinator … not seen by this writer" is replaced by the quoted record (header "Inherited requirements"). §6's "(coordinator relay of the owner addition; …)" is replaced: the scoped relations are attributed to #1169 decision 4, and "does not show that OI supplies the drive" becomes this unit's [A], with Main:590. |
| #1169 c.6742190154 decision 4 | D26 now records the scoped relations ("phase independent of the layer flow only … on Fin 2; the complex drive carries the phase (GR:250, :258)"). D24 gains "no row here implies H-Bell (#1169 decision 4)". |
| #1169 c.6742190154 decision 8 | No scoring is done. §7's preamble says that row IDs are identifiers and are not reused, that a later §A.29 scoring can name a candidate's controls by ID with status, carrier and assumptions, and that "no row records a candidate condition, a premise adopted here or a score". D27 is appended rather than renumbering D21. |

## Findings from r2's own checking (not in the review)

| ID | Finding | Verification | Change |
| --- | --- | --- | --- |
| W1 | r1's "MECH-2's P★ escapes the stabilizer octahedron **only** through a channel that is not CP" overstates MECH-2. Node 6 exhibits one instance, with non-positive branches and a non-CP unconditioned channel, and leaves open "whether some `G_SM` protocol gives a complete instrument with every branch CP and one non-stabilizer branch". | MECH-2:630–700 read at `fd539e15`. | §4.2 "Not sufficient", last bullet, rewritten to say what P★ shows and what is left open. §9 F9 (BORDERLINE). |
| W2 | r1's "NX-1 on route C ⇒ FI-1" is exact only when the non-diagonal-preserving branch sits at level one. FI-1 is `𝓘 (S × Fin 1) K`, and an architecture is not assumed relabelling-invariant. In general NX-1 gives a non-monomial admissible operator at the branch's level, so 𝓘 is not configuration-level. | `exists_nonMonomial_of_layerFlowExecutable` uses `hex 1`; `ConfigurationLevel` quantifies over all carriers. | §4.2 first directional bullet; §0 items 3–4; §6 table cell and Answer; D17. |
| W3 | Under R1, non-representability is ε-robust. Every R1-represented state is at trace-norm distance ≥ 2 − √3 from r = −v₀/√3 and from Φ⁺ (Hölder with ‖F₀‖_op = (1+√3)/4, ‖F_l⊗F_m‖_op = (2+√3)/8). This matters because the owner's question is about *approximate* closure. | r2 F5 (exact). | §5.2 item 2; D21; §8. |
| W4 | r1's §5.1 row "Route E_f, native encodings under R1 (MECH-2, QP node 10)" attributed QP node 10 to R1. Node 10 uses U′ (QP:446–450, 746–768). | QP read at `fd539e15`. | Split into the U′ and R1 rows (B2). The U′ row's closure cell says "Not assessed for node 10's table". The no-quantum-completion fact is re-derived on `main` + [G] (r2 C7), making the A868 [D] use provenance for it. |
| W5 | D1 and D24 are C-dyn by N4's own criterion. | Main:548 (Q_fb has a hidden part); Sub:131–133. | Listed under N4. |
| W6 | r1 §1's E_f examples named "QP's U′, MECH-2's R1^⊗n" as one class. U′ is non-injective (MECH-2 node 7: "B is not unique"), so Lemma F's uniqueness and NX-1's E_f class do not apply to it. | MECH-2:717–720. | §4.2 restricts the E_f class to injective identifications. |
| W7 | Executability ⇒ NX-1 needs σ involutive, for unitarity of the gate flow. | `gateFlow_unitary` (LiftAudit.lean:69). | §4.2 bullet says "of an involution σ". |

## Refusals

None in full.
- **N3** is applied in a modified form, for the reason given in its row: the review's "available at
  `availExt 1`" reading is replaced by the inheritance argument, which is what the sources support.
- **B1's word "inclusion"** is rendered as "coverage". The meaning is the same.

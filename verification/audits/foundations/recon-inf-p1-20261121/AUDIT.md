# RECON-INF Phase 1: where Theorem 23 uses finiteness

**Status.** The writer's read-only dependency audit. Revision answering the independent review of
`c847969c` (REVISE, [#1532 comment 7068213461](https://github.com/amaybaum/incompleteness/pull/1532#issuecomment-7068213461));
a delta review is required. It is a
reading of the manuscripts, the Lean statements and records already on `main`. It contains no new
proof and no computation, and it changes no manuscript, Lean file, registry file or #1477 file.
Plan: `PLAN.md` in this directory, committed first. Issue #1531; thread #1169; draft PR #1532.

**Authorization.** Owner decision on #1169,
[comment 7067918791](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7067918791)
(`amaybaum`, 2026-11-21T19:17:59Z). Only the audit is authorized; the generalization itself stays
deferred, and Phases 2 and 3 need separate authorization.

## 0. Sources, notation and keys

**Baselines.**
- **B1** is `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`.
- **B2** is T0, `5b6d48b58f45d3032bc33560aa5047c4b400f35a`. It is the predicted tree after the
  retirement plan P* (`55544cc3`; ledger `verification/audits/foundations/a1exit-deletion-20261121/edits.json`
  on `research/a1exit-deletion-20261121`). P* gives the intended edits. Nothing here assumes they
  have landed.

**Line notation.** `Sub:n`, `Main:n`, `SM:n`, `GR:n` and `Str:n` are lines of `papers/Substratum.md`,
`Main.md`, `SM.md`, `GR.md` and `Structure.md`. A reference written `n / m` gives the line in B1, then
in B2. A single number means the line is the same in both, with identical text unless the row says
otherwise. T0 shifts lines as follows:
- `Sub:44–91` → `+2`; B1 `Sub:92–93` (the (A1) entry) are deleted; from `Sub:94` on, the numbers
  agree.
- `Main:45` onward → `+2`.
- SM, GR and Structure keep their line numbers.

Lean paths are relative to `verification/lean-mathlib/OIBridge/`. The declarations cited are at the
same lines in both baselines; T0 changes docstrings only.

**Records cited (all on `main`).**

| Short name | Path under `verification/audits/foundations/` | Standing as its record states it |
|---|---|---|
| O-A4 | `o-a4-20261120/RESULT.md` | Merged in #1441; owner accepted it at #1169 c.7031779559, item 1 |
| REMAINDER | `a1-remainder-20261119/REMAINDER.md` | Consumer table at pin `21e16c61` |
| P7-B | `p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | Review ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| NR-1 | `nr1-near-return-20261116/NR-1.md` | Review ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| R1-INF | `r1-inf-20261119/RESULT.md` | Revised after REVISE; the record says a delta review is required. Cited only for Lemma 4, Prop. 5 and countermodel C4 (i), as O-A4 rows 3 and 23 cite them. Every citation below carries "(delta review outstanding)" |
| LEDGER | `a1exit-ledger-20261120/LEDGER.md`, `rows.json` | The A1-EXIT ledger rows X-nn |
| Q1, R6 | `a1exit-q1-20261120/RESULT.md`, `a1exit-r6-20261120/RESULT.md` | Accepted, per LEDGER X-42 and X-53 |

**Category codes (owner requirement 2).** A row may carry several codes.

| Code | Category |
|---|---|
| TC | The total configuration space is finite. |
| FL | The lattice is finite. |
| FR | The observable region is finite: a finite visible alphabet, finite windows, horizons, setting or readout regions, or a finite boundary layer. |
| NL | A normalizable law is enough. |
| NN | Finiteness is not needed. |

"TC (hidden)" means finiteness of the hidden factor only. "TC (constructed)" means the finite set is
built by the proof, not assumed of nature.

**Status codes (owner requirement 5).**

| Code | Meaning |
|---|---|
| P | An infinite-system result already proved. The layer is named: Lean, a paper proof in a reviewed record, or standard mathematics. |
| C | A conditional candidate: a replacement under named hypotheses that are not established, or a record still under review. |
| O | An open extension. |
| F | Proved for finite systems only, with no infinite-system form on `main`. |

**Reference frame.** The owner's suggested setting is `S = A^{ℤ³}`, with `A` a finite alphabet and
`φ` a reversible finite-range cellular automaton. It is used only to name what "infinite" means in a
row. It is not assumed to support any result. The second-order form `(p, c) ↦ (c, F(c) − p)` of the
corpus is a reversible finite-range CA on `(A×A)^{ℤ³}`.

## 1. Dependency table

### 1.1 Empirical inputs

| # | Item | B1 / B2 | Where finiteness enters | Codes | Conditions needed on `A^{ℤ³}` | Status |
|---|---|---|---|---|---|---|
| 1 | E1 unitary QM | Sub:76 / 78 | Nowhere in the statement. Stage 1 takes the supplied law on a finite visible alphabet and a finite horizon (Sub:137). The finite visible space is Lemma 1, a theorem from the observer definition (Main:46 / 48) | FR | None beyond FR | P (FR is native: Main:46 / 48) |
| 2 | E2 Bell violations, via M1-B | Sub:78 / 80; Main:420 / 422 | Corollary part (2): "on a site set of any cardinality, when the setting regions … and the readout regions … are finite sets of sites", the CHSH cap holds for the reference graph | FR | Finite setting and readout regions | P (paper, Main §3.3) |
| 3 | E3 finite boundary entropy | Sub:80 / 82; Sub:268 (i) (B2 deletes its last sentence, "the interpretive premise of A1", D029) | Finite entropy of every bounded region. Read as a dimension cutoff, it bounds only the visible sector and boundary layer, `|C_V × C_B| ≤ e^{S_∂}`. B1 states that it "does not establish finiteness of every underlying sector" (Sub:92). B2 states that "E3 does not establish finiteness of S" (Sub:216) | FR | None. The cutoff reading is an interpretation | E3 gives no TC in either baseline; the FR bound is an interpretive reading, not a theorem |
| 4 | E4 isotropy | Sub:82 / 84 | — | NN | — | — |
| 5 | E5 propagating gravity | Sub:84 / 86 | — (a continuum Weyl-tensor argument) | NN | — | — |
| 6 | E6 stable matter | Sub:86 / 88 | — (continuum Coulomb/Tangherlini) | NN | — | — |
| 7 | E7 boundary-entropy concordance | Sub:88 / 90; GR:428 | `ρ_s = (σA/ε²)·k_BT_cl/V_H` multiplies a boundary-mode count by the classical temperature of GR §3.1 (GR:102). It needs a finite count per horizon area, not a finite total system. LEDGER X-72's "how" column says E7 inherits H-count, but its exit column says the surviving normalization is Clausius and that ρ_s is an identity of the GR inputs | FR (boundary layer) | The identification of the boundary energy with the source (open, GR §7.2) | Not load-bearing for `d = 3`: E5 ∩ E6 already select 3 (Sub:157) |

### 1.2 Structural assumptions and the modelling clauses

| # | Item | B1 / B2 | Where finiteness enters | Codes | Conditions needed on `A^{ℤ³}` | Status |
|---|---|---|---|---|---|---|
| 8 | A1 | B1 Sub:92; B2 deleted (D232) | B1: "The configuration space S is finite", an open hypothesis, not adopted. B2: the entry is removed. Its content moves to Theorem 23's scope (Sub:193, D022), the Stage 1 input (Sub:123, D019) and the Stage 1 recurrence sentence ((NR) relocated, Sub:137, D245) | TC | — | Definitional |
| 9 | A2 bijectivity | Sub:94 | The statement is NN. Its two-part justification uses TC: a non-injective descent "is removable … every map on a finite set restricting to a bijection on that image". That clause is unchanged in B2. Without TC, bijectivity is the posit (REV) (B2 Main:62; REMAINDER M11, residue R3) | NN (statement); TC (justification) | (REV), a bimeasurable bijection | F (eventual-image argument); the infinite form is a posit |
| 10 | A3 bounded degree | Sub:96 | — | NN | — | — |
| 11 | A4 centre independence | Sub:98 | B1 and B2 both print `ℤ^d` as the standard construction and a finite quotient `ℤ^d/P` as a qualified case "under the conditions on P stated with each result". B2's Theorem 23 then takes "A4 applying in its finite periodic case" (Sub:193, D022). A finite quotient with a finite alphabet gives TC (`SubstratumInterfaceAudit.a1_of_finite`:109) | NN on `ℤ^d`; FL in the quotient case; FL ⇒ TC with finite alphabet | None on `ℤ^d`. A quotient needs Q1's wrapping conditions on P (LEDGER X-42) | P, Lean: `SubstratumInterfaceAudit.A4`:98 has no finiteness clause; `WaveSubstratumUnbounded.waveZ_A4`:54 and `waveZ_A4Exact`:51 hold on `Fin d → ℤ` |
| 12 | A5 linearity | Sub:100 | — The SM:240 countermodel is specific to finite rings (O-A4 §9), but it bears on A5's independence, not on a step of Theorem 23 | NN | — | P, Lean: `waveZ_A5`:58 |
| 13 | A6 background independence | Sub:102 | — | NN | — | Not in the `ℤ^d` Lean module (its scope note) |
| 14 | M1-T history readback | Sub:123 (the M1 clauses are identical; the A1 clause differs, row 17); Main §2.3–§3.4 | The characterization theorem is per accessible horizon on finite `C_V` (Main:546 / 548). The readback theorem uses the finite order `L` for `Γ_L = I` and for the bound `s ≤ min(k, L−1)` (Main:137–139 / 139–141). A non-permutation `Γ_s` from two histories that meet holds with no recurrence and no invariant law (REMAINDER M5, citing REC-1 Prop. 6.1) | FR; TC for the L-indexed parts | Rooted return (R-d), (NR) or (RIG) for the indivisibility conclusion (row 21) | P (FR parts); F (L-indexed parts) |
| 15 | M1-B Bell branch | Sub:123; Main:420 / 422 | As row 2 | FR | — | P (paper) |
| 16 | C2 mixing hypothesis | Sub:129 (B2: "E1–E3 and A2", D020), :135; Main:463 / 465, :477 / 479 | Both theorems are stated on "a measurable space H with a reference probability π_H". ETH, the motivation, is stated for "a finite reversible realization" (Main:455 / 457) | NL | The hypothesis itself | The theorems: P (paper, measurable H). The hypothesis: O in both finite and infinite settings |

### 1.3 Stage 1 (Sub:121–141)

| # | Item | B1 / B2 | Where finiteness enters | Codes | Conditions needed on `A^{ℤ³}` | Status |
|---|---|---|---|---|---|---|
| 17 | Stage 1 inputs | Sub:123 | B1 lists "A1 (finiteness)". B2 lists "finiteness of S (the scope of Theorem 23)" (D019) | TC | — | Scope |
| 18 | Representation (S ⇒ D, finite-horizon dilation) | Sub:137; Main §3.4 | A finite S is **constructed** per finite context, alphabet and horizon ("constructed, not assumed", Main:60 / 62). It is not assumed of nature | FR; TC (constructed) | On `A^{ℤ³}` a finite window's finite-horizon law is again a finite law (O-A4 row 2) | P, Lean: `Equivalence.finite_horizon_equivalence`:462. O-A4 row 2 adds: "The Stage 1 → Stage 2 identification of that finite dilation with the lattice carrier is open on both classes … finiteness does not change it" (row 53) |
| 19 | Reverse-direction lemma | Main:276 / 278 | Finite `C_V`; a uniform prior on the constructed finite `C_H`; exact for rational entries | FR; TC (constructed) | — | F as a construction; nature's carrier is not involved |
| 20 | C3 capacity bound | Main:76 / 78, :522 / 524 | Counts hidden states. It holds for every finite realization and does not bind on an infinite one (REMAINDER M15) | NN | — | P (trivially) |
| 21 | **Recurrence-cycle P-indivisibility** | Sub:137; Main:121 / 123 (Step 1) | "On a finite representative, a non-permutation rooted map and finite return also give recurrence-cycle P-indivisibility". Step 1: "φ bijective on a finite set ⇒ ∃N: φ^N = id". What the step consumes is a **rooted (visible) exact return** `Γ_n = I` at some `n > s` after a non-permutation `Γ_s`, property (R-d) of §3. Global return (R-c) supplies it on a finite representative; (R-d) does not need (R-c) | TC as printed (Step 1); NN for the consumed hypothesis (R-d) | (R-d), or (NR) in its place (Main:131 / 133, "assumed … not adopted"). B1 states (NR) in the (A1) entry (Sub:92); B2 moves it to Sub:137 (D245) | (R-d) route: P, Lean, carrier-independent (`ObservableFactorRecurrence.pIndivisible_of_visible_identity_return_nonperm`:68; `ObservableMeasureReturn.measuredGamma_eq_one_iff`:83: `Γ = I` iff the visible label returns almost everywhere). (NR) route: P, paper (Main:131 / 133), with Lean steps `ObservableRigidity.tv_revives_of_nearReturn`:88 (the total-variation revival) and `CausalReadback.c4r_implies_pIndivisible`:134 (the P-indivisibility conclusion). What is missing is a source for either hypothesis: for the selected update with α non-nilpotent, Haar prior and window readout, `Γ_t(c,c) ≤ 1/2` for every `t ≥ 1` (NR-1 Prop. 2.3), so both (R-d) and (NR) fail; for `q` prime, `α ≠ 0` and lattice-convex windows the rooted family is P-divisible at every horizon (NR-1 Thm 3.3). A physical source of a return condition is LEDGER X-21, status O |
| 22 | C2 persistence form | Sub:129; Main:477 / 479 | — (a measurable hidden space) | NL | — | P (paper) |
| 23 | Forward channel; CP-indivisibility input | Main:282 / 284; Main:336 / 338 | `ρ_H = I_m/m` needs a finite hidden factor. The measurable-carrier corollary gives the P-indivisibility input under (NR). The Koopman channel family on `ℂ^V ⊗ L²(H,ρ)` is not defined in the corpus (REMAINDER L6) | TC (hidden) for the maximally mixed state; NL+(NR) for the corollary | L6 | P (corollary); O (L6) |
| 24 | Stage-1 gauge statement | Sub:139 | "the finite channel/dilation datum actually used". Its relabelling direction is Theorem 24(i), whose coherent form uses `𝟙/|C_H|` (row 45); its enlargement direction is Theorem 24(iii), whose base prior is finite in B2 (row 46) | TC (constructed hidden) | — | F |

### 1.4 Stage 2 (Sub:143–173) and its observer branch (SM §§3–5)

| # | Item | B1 / B2 | Where finiteness enters | Codes | Conditions needed on `A^{ℤ³}` | Status |
|---|---|---|---|---|---|---|
| 25 | (a) integer dimension | Sub:157; SM:202, :210 | Through A4's rank. On `ℤ^d`, `d` is the growth degree for every radius. On a finite quotient the rank depends on the presentation: the `L = 4` torus is `Q_6` (O-A4 row 4) | NN on `ℤ^d`; FL is harmful here | The continuum step (open in both settings) | P (paper, O-A4 rows 4–5) |
| 26 | Area-law lemma (mod q) | SM:122 | Printed as "the uniform state class, for a law invariant under the update and the reversal (H-μ(φ,Θ)), assumed as a hypothesis and not adopted" | NL | H-μ(φ,Θ). On `ℤ^d` the uniform Bernoulli law satisfies it (O-A4 Lemma U) | P (paper, O-A4 Lemma U and row 6) |
| 27 | (b) wave-equation form | Sub:159; SM:222, :224 | None. SM:222 declares the carrier `Λ = ℤ^d`. In B1 it acts "under A1 and A4 … on configurations over a finite periodic quotient Λ/P". In B2 it acts "over Λ or, as a qualified case, over a finite periodic quotient" | NN | — | P (paper, O-A4 row 8); Lean `waveZ_A2`–`waveZ_A5` |
| 28 | Theorem 1a | SM:242 | Printed "Let S be a set" | NN | — | P (paper; O-A4 row 9) |
| 29 | Lemma 1c (i) | SM:252 | Printed with three alternatives: the counting measure, a structured prior, or H-μ(φ,Θ) on `ℤ^d` | NL | H-μ(φ,Θ) | P (paper, O-A4 row 10) |
| 30 | Lemma 1c (ii), pole statement | SM:252 (statement), :254 (proof) | The proof factors `det(λ−U)` and cancels finite factors. Finite pole sets do not pass to the limit in L (O-A4 §6.1) | TC (proof as printed) | H-cont for Koopman compressions; H-Bloch for translation-invariant linear operators | C under H-Bloch; O for H-cont |
| 31 | Corollaries 1a, 1b | SM:258, :270 | — | NN | `O_h` acts on the quotient only if `P` is `O_h`-invariant | P, Lean: `CubicIsotropy.corollary_1a`:616, stated on `Fin 3 → ℤ` |
| 32 | (c) link count; (d) stabilizer algebra | Sub:161–163; SM:340–390 | Finite point groups acting on six local links. Nothing averages over translations. Theorem 5's kinetic H-cust clause is not covered here: it inherits row 33 (O-A4 row 17; LEDGER X-18, disposition F) | NN (algebra) | — | P (paper, O-A4 row 17) for the algebra; kinetic clause as row 33 |
| 33 | (d) H-cust kinetic clause, via Proposition 4b | SM:334 | Printed with "the selected counting measure, which is invariant under signed permutations" | TC (hidden prior as printed) | H-μ(sp) for `|λ| > 1`; H-cont for the continued response (O-A4 row 15) | C for `|λ| > 1` (the replacement is in a record, not printed); O for the continued response and, through it, Theorem 5's kinetic H-cust clause (H-cont open; O-A4 verdict (i)) |
| 34 | (e) staggered tastes, matter | Sub:165; SM:434–456, :535–547 | — on `ℤ³`. A quotient needs `P ⊂ 2ℤ³` for the corners and even-sum `P` for the checkerboard (Q1; O-A4 §7.2) | NN; FL needs conditions | — | P (paper, O-A4 row 18) |
| 35 | (f) Theorems 17, 18; Proposition 20 | Sub:167; SM:625, :633, :647 | — | NN | — | P (O-A4 row 19) |
| 36 | (f) **Theorem 19**, Theorem 21 | SM:641–643, :651 | The printed statement uses "the hidden prior is the counting measure", and the proof divides by `|C_H|`. The kernel statement assumes `[Fintype H]` (`Reciprocity.theorem_19`:129) | TC (hidden prior as printed) | H-μ(φ,Θ): a law invariant under both φ and Θ | Measured form: P, Lean (`MeasuredReciprocity.common_hidden_law_reciprocity`:222, `reciprocal_flux`:90). The `ℤ^d` instance is the uniform Bernoulli law (O-A4 §5, paper). It is degenerate for the selected linear update (O-A4 §5) |
| 37 | The graph G(x) of SM §3.1 that varies with the configuration; H-Bell | Sub:131–133 (B2: "not a consequence of finiteness, of A2–A6", D021); SM:158 | B1 SM:158: "a single bijection on the phase space, finite under A1". B2 drops "finite under A1". H-Bell needs finite setting and readout regions (row 2) | NN (statement); FR | Curvature stability (open, finite or not) | O (H-Bell) |
| 52 | Coupling-graph definition | SM:66 (identical) | Printed on a finite product: "Let S = S₁ × S₂ × ... × S_N be a product of finite sets … the undirected graph on vertices {1, ..., N}". In B2, SM:222 puts the bijection "over Λ" while SM:66 still defines the coupling graph on finitely many sites | FL as printed; NN in substance for finite-range dependence (the same definition reads verbatim on any index set when each component depends on finitely many components, as in Main:368 / 370's arbitrary-site form) | — | The extension to any index set is a reading of the definition, not a printed statement |
| 53 | Stage 1 → Stage 2 identification | Sub:157 (identical: "The coupling graph inherited from Stage 1"); Sub:137 (Stage 1 delivers the constructed finite `S = C_V × C_H`) | The coupling graph Stage 2 reads is said to be inherited from Stage 1, whose output is a constructed finite dilation. The identification of that dilation with the lattice carrier is open whether the carrier is finite or not (O-A4 row 2; A1-01 first row) | Not a finiteness use | — | O (in both settings) |

### 1.5 Stage 3 (Sub:175–185) and the GR results it cites

| # | Item | B1 / B2 | Where finiteness enters | Codes | Conditions needed on `A^{ℤ³}` | Status |
|---|---|---|---|---|---|---|
| 38 | **H-count** | GR:58, :88 | B1: "Under A1, restrict the finite total system to a conserved energy shell … that the total system is finite (A1)". B2: "For a finite total system … that the total system is finite" (LEDGER X-70) | TC | §2.2 | F as printed; C (P7-B, decoupled product dynamics, H2, H4, H6); coupled dynamics: fails for some bijections, holds for others (P7-B 6.3), general case O (LEDGER X-71) |
| 39 | Boundary count `s_H = σA/ε²`; the `ε` identification | GR:58, :98–104, :156 | The density-of-states clause is a posit (P7-B H6). It is not supplied by counting, finite or infinite (P7-B node 3). S3 is independent of Lemma 1 (P7-B node 4) | FR (boundary layer) | H6 and S3 posited | Posit in both settings |
| 40 | Gap equation; uniqueness | Sub:181–183; GR:78, :108, :144–154 | The algebra `a_* = τ_K/β_E`, given β_E from H-count and τ_K from H-slope | NN beyond row 38 | — | Inherits row 38 |
| 41 | H-slope; GR §8.5(b) | Sub:181, :185; GR:74, :627 | H-slope is a detector-side condition. §8.5(b) assumes "H-count holds for the hidden sector" | NN (H-slope); TC through H-count (§8.5(b)) | — | Inherits row 38 |
| 42 | `σ ≤ ln q` (Lemma 23.0) | Sub:191 | A finite alphabet per boundary mode | FR (local alphabet) | — | Not a total-finiteness use |
| 43 | H-BD and the deep-sector corollary | GR:116–138, H-BD at GR:122; Sub:268 (ii) | H-BD counts "a fraction Δt/τ_BD of d ∈ C_D", which is a finite count on `C_D`. Without H-BD, Appendix B gives exact finite-window laws for a deep sector of any cardinality under (D1)–(D5) (GR:871–905) | TC (deep sector, H-BD as stated); FR + NL (Appendix B) | A measure-theoretic H-BD (REMAINDER L10) | P (paper, Appendix B); O (L10) |

### 1.6 Lemma 23.0, Theorem 23, Theorem 24 and the mirrors

| # | Item | B1 / B2 | Where finiteness enters | Codes | Status |
|---|---|---|---|---|---|
| 44 | Lemma 23.0 | Sub:189–191 (identical) | Its proof uses Stage 2, Theorem 24 (i)–(iii) and Stage 3's H-count | Inherits rows 25–36, 38, 42, 45–46 and 54 | — |
| 45 | Theorem 24 (i), relabelling | Sub:253 | The coherent form uses `ω_H = 𝟙/|C_H|`. B2 prints "For finite C_H" (D361, routed to review). The population form survives under a measure-preserving relabelling (O-A4 row 23; LEDGER X-53 (c): the relabelling must preserve ρ) | TC (hidden) for the coherent form; NL for the population form | F (coherent); C (population) |
| 46 | Theorem 24 (iii), enlargement | Sub:257–262 | B1: a factor Hilbert space "of any dimension" in a normalized state. B2 narrows membership to a classical factor of any cardinality with bijective dynamics (D363, D364), and its classical form uses "the uniform hidden prior on a finite $\mathcal{C}_H$ times α" (Sub:262, D362, routed to review). O-A4 row 24: the base channel on `V × H` "must already be defined (finite, or L6)" | NL for the adjoined factor; TC (constructed hidden) for the base prior (B2 Sub:262, D362), or L6 | P (paper, R6 T9; trace-class σ_A) for the adjoined factor; F for the base prior; O (L6) |
| 54 | Theorem 24 (ii), alphabet change | Sub:255 | Stated under the alphabet-size hypothesis, which is open on finite and infinite lattices alike (O-A4 row 25); a finite alphabet per site | FR (local alphabet) | Hypothesis open in both settings |
| 47 | Theorem 23, statement | Sub:193 | B1: "A1–A6". B2: "Let (S,φ) be a finite substratum, with A4 applying in its finite periodic case under the wrapping conditions on P" (D022) | B1 TC; B2 TC + FL | Scope |
| 48 | Theorem 23, proof | Sub:195 (identical) | "Stage 1 supplies the finite reversible/dilation data"; "Stage 2 fixes the local geometry under the periodic nearest-neighbor … assumptions" | FR, TC (constructed); "periodic" covers `ℤ^d` and quotients alike | — |
| 49 | Scope remark | Sub:216 | B1: "A1 … is motivated by E3, which does not establish it". B2: "The finite-substratum scope of Theorem 23 is used by Stage 1's exact return and Stage 3's count" (D026) | — | See §4 |
| 50 | Class exclusions; correspondence | Sub:104, :205–207, :212, :223, :233 | B1: "A1–A6". B2: "finite substratum, A2–A6" (D016–D018, D023–D025, D027–D028) | Scope | — |
| 51 | Structure mirrors | Str:47, :138 (identical); Str:646, :768 | Str:646 Proposition 9.5. B1: "satisfying A1-A6". B2: "finite substrata satisfying A2-A6, with A4 in its finite periodic case". Str:768. B1: "A1-A6". B2: "finiteness, A2-A6". These restate Theorem 23; they are not inputs to it | Scope | — |

### 1.7 Lean modules

The bridge builds every module below: each is imported by `OIBridge.lean`. Line numbers are the
same in B1 and B2.

| Module : line | Statement scope | Finite? | Bears on rows |
|---|---|---|---|
| `WaveSubstratumUnbounded`:45–70 (`waveZ_A2`, `_A3`, `_A4Exact`, `_A4`, `_A5`, control `waveZ_not_A1`) | The wave rule on sites `Fin d → ℤ` | Infinite (the control proves this) | 11, 12, 27. It covers no observer theory, A6, Theorem 19 or Theorem 23 (its scope note) |
| `SubstratumInterfaceAudit.A4`:98; `a1_of_finite`:109; `waveSubstratum_A1`:185 | A4 on an arbitrary additive site group. A finite site set with a finite alphabet gives A1 | Both | 11, 47 |
| `CubicIsotropy.corollary_1a`:616 | Kernels on `Fin 3 → ℤ` | Infinite lattice | 31 |
| `MeasuredReciprocity.reciprocal_flux`:90, `common_hidden_law_reciprocity`:222, `finite_uniform_reciprocity`:311 | A measurable hidden space with a probability law; the finite uniform case is recovered | Any cardinality, normalized | 36 |
| `Reciprocity.theorem_19`:129 | `[Fintype H]` | Finite hidden | 36 |
| `ObservableRigidity.tv_revives_of_nearReturn`:88 | The total-variation revival step under a near-return, on matrices | Finite `V` | 21 |
| `ObservableRigidity.exists_pIndivisibleWithin_of_nonPermutation`:358, `rootedFamily_productLaw`:388 | P-indivisibility from a non-permutation rooted map under the compactness hypothesis `hcompact` (:275), not (NR); rooted family of a product law; on a measurable carrier | Any cardinality, normalized | 21 |
| `CausalReadback.c4r_implies_pIndivisible`:134 | A strict increase of rooted-row distance (C4r) gives P-indivisibility | Finite `V` | 21 |
| `ObservableFactorRecurrence.pIndivisible_of_visible_identity_return_nonperm`:68 | An exact rooted identity return after an earlier non-permutation rooted map gives P-indivisibility; no carrier or cardinality assumption (its docstring: "the measurable realization that gives rise to Gamma is NOT constructed") | Carrier-independent; finite `V` | 21, §3 (R-d) |
| `ObservableMeasureReturn.measuredGamma_eq_one_iff`:83 | The measured rooted matrix equals the identity iff the visible observation returns almost surely after the iterate | Any measure | 21, §3 (R-d) |
| `RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap`:148 | Takes an exact return `Γ_n = I` as a hypothesis | Finite hidden (`[Fintype H]`, :134; `CausalReadback.RootedRealization`:178) | 21 |
| `RootedClassification.pper_of_finiteRootedRealizable`:339 | A finite realization has a periodic rooted family | Finite | §3 (R-c) |
| `Equivalence.finite_horizon_equivalence`:462 | A finite visible law on a finite horizon gives finite witnesses | FR | 18 |

No Lean module on `main` states almost-everywhere recurrence, an invariant Bernoulli law for the
corpus rule, or Stage 3 on an infinite carrier.

## 2. Stage 3: where finite counting is essential (owner requirement 4)

### 2.1 What finiteness does at H-count

P7-B node 1 locates every use of total finiteness in Stage 3. All of them sit at GR:58, and GR:68–70
inherit them. P7-B separates three roles:
- **(a1)** `Ω_H(E)` is finite, so `s_H = ln Ω_H` and the ratio `P(i)` are defined;
- **(a2)** the uniform law on a finite shell exists and is invariant under every bijection that
  preserves the shell, so no law has to be chosen;
- **(a3)** the deep clause becomes an equation between finite cardinalities.

Finiteness does **not** supply:
- the entropy slope (the density-of-states clause, P7-B H6, a posit);
- the identification of `ε` with the boundary counting unit (S3);
- the detector match (H-slope).

These hold, or fail, equally on a finite or an infinite carrier.

### 2.2 Where a normalized law might suffice, and where it does not

- **A generic normalized invariant law does not suffice.** P7-B node 5 gives a counterexample: a
  finite boundary, an infinite deep sector, reversible energy-conserving dynamics and positive rates.
  Normalized invariant laws on that model realize every real slope. Lemma 5.1 there shows that no
  probability on a countably infinite set is invariant under all permutations, so (a2) has no
  infinite counterpart.
- **A specified product law works for decoupled product dynamics.** P7-B's conditional theorem
  (P7-B:207) assumes:
  - H2: a finite boundary configuration set, which is posited;
  - H4: a shell law equal to uniform counting on the finite boundary shell times one normalized
    deep law ν of any cardinality;
  - decoupled product dynamics, H6 and H7–H9.

  Under these it gives `p_i = Ω_B(E − e_i)/Z` and the same relation `a_* = c³ε_c²/(4Gσ)`. The
  product law fixes the visible weights; the slope still comes from H6 (P7-B node 6 verdict). This
  replacement **still assumes finite counting on the boundary shell** (H2 posited, H4). It replaces
  only the deep sector's finiteness. Whether a boundary law that is not a count could replace H2 and
  H4 is not determined by any record: P7-B proves sufficiency, not necessity, and node 5 rules out
  only a generic normalized law.
- **Coupled dynamics: mixed, and open in general.** For some deep-coupled bijections no normalized
  invariant shell law exists (a single `ℤ`-orbit); for others a product law with a φ-adapted ν is
  invariant (P7-B 6.3, P7-B:189). The coupled case is parked, not excluded. It is LEDGER X-71,
  status O.

### 2.3 Consequence for `ħ = c³ε²/(4Gσ)`

The relation inherits β_E from H-count (row 40). In both baselines it is printed for a finite total
system. Its A1-free form for decoupled product dynamics is P7-B's theorem, which exists in a record only
(LEDGER X-70: "An A1-free decoupled form exists in records only").

On `A^{ℤ³}` with a finite-range CA, the boundary and the deep sector are not decoupled in general. So
P7-B's theorem does not cover the reference frame. Whether a coupled invariant shell law exists
there, and whether it would fix the weights, is not determined by any record.

## 3. Three properties kept apart (owner requirement 3)

**(R-a) Almost-everywhere recurrence on `ℤ³`.**
- *What is proved.* For the second-order form on `(A×A)^{ℤ^d}`, with `A` a finite abelian group and
  any Borel `F`, the uniform product law β is invariant under φ and Θ (O-A4 Lemma U, paper, accepted
  with #1441).
- *What it would combine with.* Poincaré's recurrence theorem (standard) applies to any measurable
  map that preserves a probability.
- *What is not on `main`.* The statement that combines them, β-almost-every configuration returning
  to each cylinder neighbourhood. #1504 states it at `31594967` (NOTE:289–299, unreviewed there).
  Status **C**.
- *What it does not give.* An exact return, a time uniform across configurations, or (NR) for the
  rooted maps: for the selected update with α non-nilpotent, Haar prior and window readout,
  `Γ_t(c,c) ≤ 1/2` for every `t ≥ 1` (NR-1 Prop. 2.3), so neither (NR) nor (R-d) holds. (R1-INF
  Lemma 4 (c) and Prop. 5, delta review outstanding, add that the update is mixing for unit `α`.)
- *Axiom 2.* Axiom 2 (Main:36; the line differs in B2, where D001 deletes its last sentence on total finiteness) says that differentiation recurs. Whether a statement about `A^{ℤ³}`
  must keep a form of return, and which form, is the owner question #1504 records. It is not
  decided here.

**(R-b) Periodic bounded orbits under NU9.**
- *What is claimed.* #1523 at `b9d8ce76`: for the rule `R_q` on `ℤ³`, at a uniform background `c`
  with `2 ≤ c ≤ q−3`, one single-site seed has a periodic orbit of exact period 10, with support in
  the cube `{−1, 0, 1}³` at every tick (NOTE:25). An independent hand re-derivation confirmed the
  mathematics at `fa054c24` (REVISE on status only, #1523 c.7067371071), and a delta check confirmed
  `b9d8ce76` (#1523 c.7067390937). The exact re-run is pending and owner acceptance has not been
  given. Status **C**.
- *Its scope.* This concerns particular configurations.
  - It gives no recurrence for a law of positive mass, and no global return.
  - It gives no (NR) for a root-shared prior.
  - For the selected linear update the periodic points have Haar measure zero (R1-INF Lemma 4 (d),
    delta review outstanding).
    The measure of `R_q`'s periodic set is not determined by any record.

**(R-c) Global exact return `φ^N = id`.**
- *Finite carriers.* It holds on every finite carrier (Main:121 / 123). It makes every rooted family
  periodic (`pper_of_finiteRootedRealizable`:339; Main:650 / 652).
- *`ℤ^d`, finite-order members.* It holds for the finite-order members of the corpus form, `α = 0`
  and `q = 4, α = 2` (R1-INF countermodel C4 (i), delta review outstanding; also cited by O-A4 row 3).
- *`ℤ^d`, selected update.* It fails for the selected update with `q` prime and `α ≠ 0`: no nonzero
  finitely supported state has a finite orbit (R1-INF Lemma 4 (a), delta review outstanding).
- *Observed return without global return.* Exact return of the observed law does not entail global
  return. Sub:268 (iii) transfers a recurrence-scale property, established on a finite
  representative, to a decoupled extension of any cardinality. It "does not imply recurrence of
  every unobserved sector".

**(R-d) Rooted (observable) exact return `Γ_n = I`.**
- *What it is.* The rooted visible maps return to the identity at some `n`: equivalently, the visible
  label returns almost surely after `n` steps (`ObservableMeasureReturn.measuredGamma_eq_one_iff`:83).
- *What it gives.* With an earlier non-permutation `Γ_s`, P-indivisibility at that horizon, with no
  carrier or cardinality assumption (`ObservableFactorRecurrence.pIndivisible_of_visible_identity_return_nonperm`:68).
  This is the hypothesis Stage 1's recurrence step consumes (row 21).
- *Where it fails.* For the selected update with α non-nilpotent, Haar prior and window readout,
  `Γ_t(c,c) ≤ 1/2` for every `t ≥ 1` (NR-1 Prop. 2.3).

**Implications used.** Only the trivial ones from (R-c):
- `φ^N = id` makes every orbit periodic with period dividing N, which gives (R-b);
- it makes every point return exactly, which gives (R-a) for any invariant law, and (R-d) at `n = N`
  for any prior.

No converse and no implication among (R-a), (R-b) and (R-d) is asserted; Sub:268 (iii) shows that
(R-d) for the observed law does not give (R-c). Stage 1's recurrence step (row 21) needs (R-d), or
(NR) in its place. (R-c) is sufficient for (R-d), not necessary. Neither (R-a) nor (R-b) supplies
(R-d) or (NR).

## 4. The review questions P* routes here

### 4.1 D026: does any stage other than Stage 1's exact return and Stage 3's count use finiteness?

The two uses D026 names are correct as printed, and they are the two TC uses whose hypothesis has
no source:
- Stage 1's exact return, row 21. The replacement theorem is on `main` in Lean: rooted return (R-d)
  gives the conclusion on any carrier, and (NR) is a weaker sufficient condition. What is missing is
  a source for either. For the selected update with α non-nilpotent, Haar prior and window readout,
  both fail (NR-1 Prop. 2.3), and no other law or mechanism is known to supply them (LEDGER X-21, O).
- Stage 3's H-count, rows 38 and 41. The replacement holds in a record for decoupled product
  dynamics, under posited H2, H4 and H6; for coupled dynamics it is open (X-71).

The chain **as printed in both baselines** has further finiteness uses that D026's sentence does not
list:

1. **A2's justification** (row 9, Sub:94). It uses the eventual image of a map on a finite set. The
   infinite form is the posit (REV).
2. **Theorem 24 (i), coherent form, and Theorem 24 (iii)'s base prior**, which Lemma 23.0 and the
   Stage-1 gauge statement use (rows 24, 45, 46). Both need a finite `C_H`. In Stage 1, `C_H` is the
   constructed finite dilation, so these are uses on the constructed datum, not on nature's carrier.
   B2 prints them (D361 at Sub:253; D362 at Sub:262).
3. **Stage 2 printed with the counting measure.** These are Theorem 19 (SM:641, row 36) and
   Proposition 4b (SM:334, row 33). The measured replacements are proved, in Lean (Theorem 19) or in
   a paper record (Prop. 4b for `|λ| > 1`), but they are not printed.
4. **Stage 2's pole statement**, Lemma 1c (ii) (row 30). Its proof is a finite-determinant argument.
   On an infinite carrier the step needs H-cont, which is open, or H-Bloch.
5. **H-BD as stated** (row 43). It counts a fraction of a finite `C_D`. It enters through E3's
   reading (Sub:268 (ii)) and GR §3.2, not as a hypothesis of Theorem 23.
6. **The coupling-graph definition** (row 52, SM:66) is printed on finitely many sites. It reads
   verbatim on any index set for finite-range dependence.
7. **The Stage 1 → Stage 2 identification** (row 53) is not a finiteness use, but it is an open seam
   in the chain in both settings (O-A4 row 2).
8. **FR uses throughout** (rows 1–3, 14–15, 18, 37, 39, 42, 54). These are finiteness of observable
   regions, not of S.

**Productivity, as found.** Items 1–6 are finiteness uses beyond the two D026's sentence names, so
criterion (a) of PLAN §6 is met against that sentence. But items 1–5 are already LEDGER rows (X-30,
X-53 with D361, X-16 and X-17, X-18, X-73): this record collects them; it did not find them. The
uses not recorded in LEDGER or D026 are D362's finite base prior (item 2, second half) and SM:66
with the Stage 1 → 2 seam (items 6–7). These were found by the independent review of `c847969c`
(findings 4 and 5), not by the first version of this audit. Items 3 and 4 concern the printed proofs:
the hypothesis needed on an infinite carrier is NL (item 3) or H-cont/H-Bloch (item 4), not TC.

### 4.2 D022: do Stages 1 and 3 need exactly the scope "finite substratum, A4 in its finite periodic case"?

- **Stage 1.** It needs TC of the representative for exact return (row 21), and FR for the rest
  (rows 14, 18). More precisely, the recurrence step consumes rooted return (R-d) or (NR), which
  TC supplies on a finite representative (row 21). No step of Stage 1 uses a lattice, finite or not.
- **Stage 3.** It needs TC of the total system through H-count (row 38). No step uses FL.
- **Stage 2.** It uses no finiteness of the lattice:
  - every step survives on `ℤ^d` under the named hypotheses of rows 25–36 (O-A4 verdict (i), accepted
    with #1441), with one qualifier from that verdict: Lemma 1c (ii)'s pole statement for Koopman
    compressions, Prop. 4b's continued response and through it Theorem 5's kinetic H-cust clause
    additionally need H-cont, which is open (rows 30, 33);
  - its A2–A5 instances hold on `ℤ^d` in Lean (`waveZ_*`);
  - the finite periodic case adds wrapping conditions on P that `ℤ³` meets automatically (rows 31,
    34; Q1; O-A4 §7), and the `L = 4` torus enlarges the link symmetry (row 25).

- **The seam.** Stage 2 reads its coupling graph as "inherited from Stage 1" (Sub:157), whose output
  is a constructed finite dilation, and SM:66 defines that graph on finitely many sites. The
  identification of the dilation with the lattice carrier is open in both settings (row 53). The
  stage-by-stage statements above do not cover it.

So B2's FL clause is a scope choice. A finite quotient with a finite alphabet gives TC
(`a1_of_finite`), which supplies the TC that Stages 1 and 3 use. No stage's proof uses FL; the
printed definition at SM:66 does (row 52). This finding is about dependencies only. It proposes no
edit; LEDGER X-45 and Issue #1479 own the wording.

**Productivity, as found.** For Stage 2 this restates LEDGER X-45 and O-A4 verdict (i). PLAN §6
counts restating ledger rows as non-productive, so criterion (b) is not credited here. The new items
in §4.2 are the SM:66 definition and the seam, from the review's finding 5.

## 5. Status summary (owner requirement 5)

**(P) Infinite-system results already proved.** These are local or stage-level results. None of
them is a reconstruction of Theorem 23 on an infinite lattice.
- *Lean:*
  - P-indivisibility from rooted exact return, on any carrier (`ObservableFactorRecurrence`), and
    the equivalence of rooted return with almost-sure visible return (`ObservableMeasureReturn`);
  - A2–A5 for the wave rule on `ℤ^d` (`WaveSubstratumUnbounded`);
  - A4 on an arbitrary site group (`SubstratumInterfaceAudit.A4`);
  - Corollary 1a on `ℤ³` (`CubicIsotropy`);
  - measured reciprocity, the Theorem 19 replacement (`MeasuredReciprocity`);
  - the near-return revival step and the compactness route to P-indivisibility on a measurable
    carrier (`ObservableRigidity`).
- *Paper, accepted records:*
  - Stage 2 (a)–(f) and its observer branch on `ℤ^d` under A4∞, LF, H-μ(φ,Θ), H-μ(sp) and H-Bloch
    (O-A4 verdict (i)), except Lemma 1c (ii) for Koopman compressions, Prop. 4b's continued response
    and Theorem 5's kinetic H-cust clause, which additionally need open H-cont;
  - Lemma U;
  - the Bell cap for any cardinality with finite regions (Main:420 / 422);
  - the C2 theorems on a measurable H (Main:463 / 465, :477 / 479);
  - the deep-sector corollary for any cardinality without H-BD (GR Appendix B);
  - Theorem 24 (iii) for normalized factors of any cardinality (R6).
- *Negative results:*
  - for the selected update on `ℤ^d` with α non-nilpotent, Haar prior and window readout, (NR) and
    rooted return fail (NR-1 Prop. 2.3); for `q` prime, `α ≠ 0` and lattice-convex windows, the
    rooted family is P-divisible at every horizon (NR-1 Thm 3.3);
  - a generic normalized invariant law leaves the Stage 3 slope undetermined (P7-B node 5).

**(C) Conditional candidates.**
- Stage 3 for decoupled product dynamics, under posited H2, H4 and H6 (P7-B theorem).
- Recurrence-cycle P-indivisibility under (R-d) or (NR), for laws that satisfy them. None is known
  for the selected update on `ℤ^d` except laws supported on periodic configurations (Sub:137 in B2;
  Main:728 / 730).
- Lemma 1c (ii) under H-Bloch.
- Prop. 4b for `|λ| > 1` and Theorem 24 (i) in population form under the stated invariant laws.
- Almost-everywhere recurrence (R-a) and NU9 (R-b), both from records under review.

**(O) Genuinely open.**
- Stage 3 for coupled dynamics in general (X-71).
- H-cont for Koopman compressions, and with it Prop. 4b's continued response and Theorem 5's kinetic
  H-cust clause on an infinite carrier.
- The Stage 1 → Stage 2 identification of the constructed dilation with the lattice carrier (row 53;
  open in the finite setting too).
- A measure-theoretic H-BD (L10).
- The Koopman channel family (L6), and a coherent Theorem 24 (i) on an infinite hidden space.
- Selection of a law on an infinite carrier (REMAINDER R1).
- A source of rooted return (R-d) or (NR) for the selected update on `ℤ³` (LEDGER X-21).
- An infinite form of A2's eventual-image argument (otherwise (REV) is posited).
- Composing these into Theorem 23 on `A^{ℤ³}`.

## 6. The owner's standard

**Classification.** This audit is a documentary reading. It proves nothing, so it is neither (N)
nor (I). Theorem 23 as cited is (I): it imports E1 (unitary QM), the Stage-1 operational-lift
hypotheses (Sub:139) and H-slope (GR:74). This audit does not change that.

1. **Established.** The table in §1, with references in both baselines, and the answers in §4.
2. **Assumed.** Nothing new. The infinite-carrier hypotheses named in rows 21, 26, 29, 30, 33, 36,
   38, 43 and 46 are those of their cited sources, and none is adopted.
3. **Missing.** Two steps are the earliest unsupported steps for an infinite-lattice Theorem 23.
   Both need a physical posit, not only mathematics:
   - Stage 1's return hypothesis (row 21): rooted return (R-d) or (NR). The theorem that consumes it
     is on `main`. For the selected update with α non-nilpotent, Haar prior and window readout, both
     fail (NR-1 Prop. 2.3), so a different law or mechanism would be needed (X-21).
   - Stage 3's coupled shell law (row 38), and, for decoupled dynamics, the posits H2, H4 and H6.

   H-cont (rows 30, 33) is a purely mathematical gap. The Stage 1 → 2 identification (row 53) is
   open in both settings.

## 7. Controls and verification status

- **K1.** `git diff --stat origin/main` lists only `PLAN.md` and `AUDIT.md` in this directory.
- **K2.** Every `file:line` was read in both baselines: B1 from the `main` worktree, B2 from
  `git show 5b6d48b5:<path>`. The two baselines are compared at each cited line. Every ledger edit
  cited (D001, D016–D029, D232, D245, D361–D364) was read in `edits.json` at `55544cc3`.
- **K3.** No row gives a stronger status than its source.
  - Rows citing O-A4 use the scope of O-A4 verdict (i).
  - Every citation of R1-INF carries "delta review outstanding".
  - Rows citing #1504 and #1523 are status C.
- **Evidence level.** Reading only. Nothing was built, run or dispatched.
- **Review.** The independent review of `c847969c` was REVISE (#1532 c.7068213461). This revision
  answers findings 1–10. **Missing:** a delta review.

## 8. References outside `main` (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| T0 `5b6d48b5` on `trial/a1exit-T0-55544cc3` | Baseline B2 | Provenance; read only |
| P* `55544cc3`, `edits.json` | The intended edits cited | Provenance; read only |
| #1504 at `31594967`, NOTE:289–299 | (R-a) | Provenance; unreviewed revision of a REVISE head |
| #1523 at `b9d8ce76` | (R-b) | Provenance; hand re-derivation at `fa054c24` (c.7067371071) and delta check at `b9d8ce76` (c.7067390937); exact re-run pending; not owner-accepted |
| #1532 c.7068213461 | Review answered by this revision | Provenance |
| #1169 c.7067918791 | Authorization | Quoted with author and time |

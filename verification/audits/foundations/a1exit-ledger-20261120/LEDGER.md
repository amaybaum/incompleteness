# A1-EXIT ledger — every remaining A1 dependency, its end state, exit route and correction

**Status.** Writer's paper-only ledger, WIP / UNVERIFIED. The schema, sources, completeness check
and deletion criterion were fixed in `PREREG.md` (commit `b352d4a4`, pushed before any row was
populated). The ledger is built from existing records only. It adds no proof, measure construction
or physical premise, and it edits no manuscript, Lean or registry file. No classification of the
source audits is redone. A1 (Main posit ledger item (ii)) remains open and unadopted. Independent
non-author review is required before any use.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, Step 1 row A1-EXIT. Goal link (§A.47): "Make OI's foundational formulation
independent of the assumption that the whole universe is finite, while keeping honest limitations on
the results that still require finiteness."

**Source pin.** `main` at `9db518844`. `File:n` is line `n` at the pin. Abbreviations are those of
PREREG.

## Files

| File | Content |
|---|---|
| `PREREG.md` | Schema, sources, checks CK1–CK8, deletion criterion, decision rule |
| `rows.json` | The 56 dependency rows and the site-assignment rules (P0 row map, class map, site overrides, rules for new sites, Lean entries) |
| `sitemap.json` | 600 sites: the 566 Phase-0 sites relocated to the pin, 11 lines added since Phase 0, 11 Phase-2 census-extension sites and 12 sites placed by override. Each site carries its row, correction code, owner and S3 |
| `ledger_check.py` | `build` regenerates `sitemap.json` from the working tree; `render` writes the generated blocks below; `check` re-runs the build, compares it with the committed map and the blocks, and runs CK1–CK8; `self-test` runs three countercontrols |

The run at the pin is `python3 -I -B verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py check`
→ `CK1-CK8 PASS`, and `… self-test` → `self-test PASS`.

## 1. Summary

<!-- COUNTS:BEGIN -->
| Measure | Counts |
|---|---|
| Rows | 56 |
| Disposition | F 26, J 17, O 13 |
| S1 on J rows | No 14, Relabel 3 |
| Row owner | Main:764 1, Q1 5, Q2 1, Q3 propagation 7, R1/R2 scoping 2, R6 3, Step-2 phase 2, final deletion 9, none 26 |
| Row status | done 24, in progress 10, open 3, queued 19 |
| Sites in the map | 600 (465 mapped to a row; 135 FP, FREE or kept) |
| Mapped sites by correction code | none 159, ptr 186, unit 120 |
| Mapped sites by owner | Q1 26, Q2 1, Q3 propagation 78, Step-2 phase 15, final deletion 186, none 159 |
<!-- COUNTS:END -->

**Reading the counts.**

- **J (17).** Each J row is A1-free as stated, or proved under a weaker condition already printed
  with the result. Three of them carry S1 = `Relabel`:
  - X-20, recurrence-scale P-indivisibility under (NR);
  - X-23, the index-free equivalence;
  - X-25, routed-readback revival.

  Their condition is logically weaker than A1 but has no finite-window test. For the selected update
  it is known to hold only under a law supported on periodic configurations (§3.1).
- **F (26).** Each F row is a true statement about finite systems or finite representatives. With A1
  deleted, it stays as a finite-only statement.
- **O (13).** The O rows fall into four groups:
  - **Q1 and Q2 rows, in progress (X-40–X-44).** These are not marked J in advance (safeguard 2).
  - **Rows with no proof and no unit (X-11 R1 justification, X-21 physical return, X-71 C1 coupled).**
    These stay open and are stated as open.
  - **Step-2 rows (X-63 global phase, X-82 inflow).**
  - **The posit, its pointers and its declarations (X-00–X-02).** These are removed by the deletion
    edit.

## 2. The ledger

Column definitions are in PREREG §3.

- **Status vocabulary:**
  - `done`: no correction is needed before deletion except the pointer rewrites the deletion edit
    makes itself;
  - `in progress`: an authorized Step-1 unit is running;
  - `authorized`;
  - `queued`: Step 2, not authorized;
  - `open`: no unit.
- **Site cell:** each row lists the sites the map assigns to it. S3 is counted by state:
  - `visible`: the finite-only, conditional or open qualification is printed at the site;
  - `per unit`: the owning Step-1 unit decides;
  - `not determined`: a Phase-3 site, decided by the Q3 census.
- **Codes:** `none`, `ptr` (rewritten in the deletion edit) and `unit` (corrected by the owning
  unit).
- **Lines with several rows:** a line carrying several rows is assigned to one primary row. The
  other rows list it after "also".

<!-- TABLE:BEGIN -->
| Id | Dependency (home at the pin) | Sources | How A1 enters | Disp. | Weaker condition (J) | Disguised A1? (S1) | Exit route | Correction | Sites and S3 (qualification visible?) | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-00 | Main posit ledger item (ii), total finiteness of the bijective representative, and the status Remark sentence that carries it (M:732 (ii); M:60) | REM-s3, R1, R2, R3, R5, R6 | The posit itself: "an open hypothesis, not adopted ... carried as one sufficient condition" | O | — | n/a (not J) | Deleted by the final-deletion unit once PREREG §6 holds; until then it stays printed as open and not adopted | M:732: delete item (ii) and renumber nothing (claim IDs are identifiers, §A.30): replace its text by the finite-only scope list it now carries, re-homed as a scope note — "The counting-measure selection of Lemma 3, the exact return and its index L, the orbit capacity, the CP-indivisibility theorem of §3.2, the physical-memory theorem of §3.4 and the canonical-typicality step of §4.6 are statements about finite representatives." M:60: replace "Total finiteness of that representative is one sufficient condition ... carried as item (ii) of the posit ledger (§4.5), the total-finiteness posit, an open hypothesis, not adopted;" by "The results that use a finite representative are statements about finite representatives;" keeping the rest | 2 sites (visible 2); codes ptr 2. M:60, M:732 | final deletion | queued (Step 2; needs PREREG §6) |
| X-01 | Pointers to the posit: item (ii), "the total-finiteness posit", "posit A1", "(ledger item (ii))" (M:36, :44, :111, :129, :224, :268, :594, :646, :708, :726; companion and book counterparts in the site map) | REM-s3 | Each sentence names the posit as the source of a finite hidden sector or of the finite model | O | — | n/a (not J) | Rewritten in the deletion edit (PREREG §6 item 4) | Each: replace the pointer by the scope it carries. M:36 "Total finiteness remains an open physical posit, not adopted, and one sufficient condition among those each result names (...item (ii))" → delete the sentence (the next sentences already state the per-result conditions). M:44, :111, :129, :224, :268 "under the total-finiteness posit (§1.2 Remark, §4.5 ledger)" → "on a finite representative". M:594 and ch01:163, ch19:126 "in its finite model (ledger item (ii))" → "in its finite model". M:646 "(b) the physically operative form under A1" → "(b) the form for a finite substratum". M:708 "item (ii) of the posit ledger (§4.5), an open hypothesis, not adopted, and one sufficient condition" → "a property of finite representatives, not derived from Lemma 1". M:726 "finite under the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii)), an open hypothesis" → "finite in the finite representative, which is not asserted of nature" | 58 sites (not determined 4, visible 54); codes ptr 54, unit 4. FULL:320, FULL:361, FULL:496, FULL:5196, FULL:5282, FULL:5284, FULL:5286, FULL:5430, FULL:6171, FULL:6251, FULL:6253, FULL:6257 … | final deletion | queued (Step 2; 4 Phase-3 sites via Q3) |
| X-02 | Declarations of A1 in companion papers, book and glossary (Substratum (A1), "finite under A1", "A1–A6", "posit A1", appendix C §C.6) (Sub:92; SM:30, :60; ch02:76; gloss:11; appC:96–116; and every "finite under A1" site) | C6, C9, FCLASS-U1 | States A1 or applies it to S | O | — | n/a (not J) | Rewritten in the deletion edit; Phase-3 files by Q3 propagation first | Sub:92 and ch02:76 / FULL mirror: delete the (A1) entry; Theorem 23 then states finiteness as part of its finite-substratum scope (X-45). "finite under A1" / "finite under the open hypothesis A1" → "finite in the finite representative" (where the sentence is about the model) or delete the parenthesis (where finiteness is not used). gloss:11: replace the A1 entry by "Finite representative: ... (finite-only scope; no claim that the substratum is finite)". appC §C.6: restate the objection as answered by the finite-only scope of the listed results | 25 sites (visible 25); codes ptr 25. FULL:638, FULL:706, FULL:766, FULL:788, FULL:842, FULL:945, FULL:1330, FULL:1338, FULL:1983, ch02:8, ch02:76, ch02:136 … | final deletion | queued (Step 2) |
| X-10 | Lemma 3 selection clause: the counting measure is the maximal-entropy invariant measure (M:54; M:58; M:732 (ii) scope list) | M1, S0:M1.a | A uniform probability exists only on a finite carrier; the maximum is over invariant laws relative to counting | F | — | n/a (not J) | Already printed as a statement about finite representatives (M:732 (ii) scope list, kept by X-00's re-homing). Kernel: `CanonicalMeasure.counting_maximal_entropy` (finite S) | none (M:54 states "globally, the counting measure is selected ... a selection principle"; finite scope carried by M:732 list). Book ch01:38, :81, :85 and FULL mirrors: none (Phase 1 dispositions N/B-units) | 19 sites (not determined 5, visible 14); codes none 14, unit 5. FULL:371, FULL:414, FULL:418, FULL:3872, FULL:4767, ch01:38, ch01:81, ch01:85, ch14:272, ch18:36, Comp:122, M:54 … | Q3 propagation | queued (5 Phase-3 sites; done in Main and Phase-1 book files) |
| X-11 | R1: physical justification of a selected law (posit (iv), μ-G; the canonical law's physical selection; P-ED (G3)+(G4)) (M:732 (iv); M:58) | R1, S0:M1.a, L1 | Selection over laws on the whole carrier; P-ED restates the uniform posit (R1-INF §7) | O | — | n/a (not J) | Open (owner safeguard 3: "R1's physical justification ... remain[s] open"). No unit; R1-L8 Stage 1(iv) deferred | none: M:732 (iv) prints the selection as "a standard but substantive epistemic postulate, not derived"; POSIT-MIN (iv) "WEAKEN to H-μ" is a proposal, not adopted | 3 sites (visible 3); codes none 3. SM:803, SM:809, SM:811; also M:732 (iv), M:58 | none | open |
| X-12 | μ-O and μ-R (uniform law on the actual orbit / on the record-compatible orbit union), their static budgets log₂(\|S\|/ℓ), log₂(\|S\|/\|U\|), and the orbit capacity log₂ p (M:60 ("As for the measure on a finite representative"); M:732 (iv)) | M2, M13, S0:M2.b, S0:M2.c | Uniqueness on a finite orbit; counting budgets | F | — | n/a (not J) | Owner decision #1169 c.7041456852 item 3: "(iii) Orbit and record laws (μ-O, μ-R) as finite-only statements ... Adopted as a scope restriction for existing results ... Any manuscript wording change needs its own correction unit" | M:60: none (prefixed "As for the measure on a finite representative"). M:732 (iv): add "on a finite representative" after "maximal entropy compatible with the observer's records" if the R1/R2 scoping unit finds the item read as a law on an infinite carrier. Reconstruction records (OA-1, PREP) are research records, not manuscript | no primary site; also M:60, M:732 (iv) | R1/R2 scoping | queued (Step 2) |
| X-13 | Record budget D(p₀,B‖ν_B) ≥ (N+1)(1 − h₂(ε)) and the no-autonomous-production results (PREP 1.1–1.4, 2.5–2.6 (research record); no manuscript site) | S0:M2.d | Reference u finite, or ν with H-ν | J | H-ν: ν invariant with ν_A = u_H ⊗ ν_{A∖H}, finite cone (PREP 2.6) | No: A finite cone, not a finite carrier; any normalized ν off the cone. Its use to exclude the inflow endpoint needs a reference fixed in advance (X-82) | Already proved under H-ν on a finite cone (PREP 2.6, paper) | none | no primary site | none | done |
| X-14 | Baseline transition matrices and rooted family under the uniform hidden prior (M:113; M:137–143; M:208–210) | M3 | T_ij = \|{h}\|/\|C_H\| counts a finite hidden set | J | Any normalized hidden prior shared by the roots, on a measurable carrier | No: Normalization only; no cardinality | Main already allows an arbitrary shared μ_H (M:135, :141); RIGID `ObservableRigidity.rootedFamily_productLaw` (Lean) | none | no primary site | none | done |
| X-15 | Doubly stochastic one-step and rooted maps; injectivity prong 1; non-permutation witness lemma (M:210; M:276–280; M:441–443; M:530; M:60 (prong 1)) | M3, S0:M3.a, S0:M3.b, S0:M3.c, L3 | Uniform law on a finite product carrier | J | (IP): φ preserves ν⊗ρ with ν uniform on the finite visible alphabet (M:280); window readouts under P-ED (R1-INF Lemma 8) | No: Uniform only on the finite visible factor; β_A on an infinite product satisfies it (R1-INF Lemma 8). STAGE0 R′ counts the uniform factor as a selected law: recorded, not A1 | Main §3.2 prints (IP) as a sufficient condition (M:280, Phase 1 E9; item (ii) list) | none for (IP) sites. M:441 "for the finite bijective model of §3.2 with its common uniform hidden prior" is a finite statement and stays | 10 sites (visible 10); codes none 10. FULL:5719, FULL:5721, FULL:5723, appb:42, appb:44, appb:46, M:210, M:276, M:278, M:280 | none | done (Phase 1) |
| X-16 | Theorem 19 reciprocity T_ij = T_θj,θi and detailed balance; Theorem 21 (SM:641; SM:651) | S0:M1.b, OA4:20, OA4:21 | Counting hidden prior and normalizer 1/\|H\| | F | — | n/a (not J) | Printed with "the hidden prior be the counting measure" (finite). An A1-free form exists in records (P6: Θ-invariant normalized law, equal root masses; `MeasuredReciprocity`, Lean) but owner Q4 (#1169 c.7035888700): "no new companion-paper claims" | none | 1 sites (per unit Q1 1); codes none 1. SM:641 | Q1 | in progress (Q1 may restate it on ℤ^d; the ℤ^d form for the selected linear update is degenerate, O-A4 §5) |
| X-17 | Proposition 4b custodial scalarity at \|λ\| > 1 (SM:334) | S0:M1.c, OA4:15 | Selected counting measure | J | H-blind / H-μ(sp): a law invariant under signed permutations (uniform product law on ℤ^d satisfies it, O-A4 Lemma U) | No: An invariance property of a normalized law; satisfied on an infinite carrier | SM:334 prints the extension clause (law equivariant under signed permutations) | none | no primary site | none | done |
| X-18 | Lemma 1c(ii) pole statement; Proposition 4b continued response; Theorem 5 kinetic H-cust clause (SM:252–254; SM:334–336) | S0:M1.d, OA4:10, OA4:11, OA4:12 | Determinant factorization on a finite carrier | F | — | n/a (not J) | Phase 2 S7/S8 (#1450) state (ii) on a finite carrier and fibrewise under translation invariance, with "On an infinite configuration space without that structure no determinant is available" (SM:254). The general infinite-carrier reading needs H-cont (O-A4 §6.1), open | none | no primary site; also SM:252, SM:254, SM:334, SM:336 | none | done (Phase 2) |
| X-20 | Recurrence-scale P-indivisibility from a non-permutation map (§2.3 theorem, Step 1 exact return) (M:113–131; M:72, :180, :182, :340, :634, :724) | M4, S0:M3.d, OA4:3 | Step 1: a bijection of a finite set has finite order N | J | (NR): a single common near-return with margin after the non-permutation time, any normalized root-shared prior, no invariance (M:131) | Relabel: Logically weaker than A1 (RIGID rotation × Bernoulli satisfies it with no finite order). But at an unspecified time it has no finite-window test (REMAINDER §3), and for the selected update it fails under β_A (NR-1 Thm 3.3) and is known to hold only under the torus counting law μ_L on periodic configurations (STAGE0 F1) — finiteness under another name. Flag for the review | Main §2.3 corollary (near-return), M:131, prints (NR) "assumed ... not adopted"; companions carry it (Phase 2 S1, G1, G2, B1) | none in Main and Phase-2 files; Phase-3 restatements (Meth, ch18, FULL) by Q3 | 64 sites (not determined 3, visible 61); codes none 59, ptr 2, unit 3. FULL:62, FULL:426, FULL:428, FULL:430, FULL:444, FULL:452, FULL:454, FULL:456, FULL:897, FULL:963, FULL:975, FULL:1101 … | Q3 propagation | queued (3 Phase-3 sites and glossary:105; done in Main and Phase-2 files) |
| X-21 | A physical source of a return condition for the selected update (none (REMAINDER R2; STAGE0 F1; NR-1 open question 3)) | R2, L4 | Under β_A, (NR) fails for the selected update (NR-1) | O | — | n/a (not J) | Open; no unit | none: no manuscript asserts a physical return for the selected update on ℤ^d | no primary site; also none: no manuscript site asserts a physical return for the selected update | none | open |
| X-22 | History readback + finite recurrence theorem: exact endpoint Γ_L = I, bound s ≤ min(k, L−1) (M:137–141; GR:591) | M5, R2 | φ of finite order L | F | — | n/a (not J) | Printed for "a bijection ... of order L" on finite C_V × C_H: a finite-representative theorem. The A1-free part (histories meeting ⇒ some non-permutation Γ_s; REC-1 Prop 6.1) is in records only; priors with no invariant product law need L4 (open) | none | 4 sites (visible 4); codes none 4. FULL:6096, appb:419, M:137, M:139 | R1/R2 scoping | done (the statement is finite; R1/R2 scoping may add the REC-1 form) |
| X-23 | Index-free full-support equivalence: readback gap at some finite order ⇔ non-permutation Γ_s ⇔ not P-divisible on some horizon (M:141; M:224; M:80 item (2)) | M7, REC1-U15 | Exact return in the L-indexed proof | J | REC-1 Prop 6.2: (V), (M), (I), (P), (RIG), (FS); or (NR) | Relabel: As X-20 | Printed among measurable-H results (Phase 1 E15, amendment A-E15) | none | no primary site | none | done |
| X-24 | L-indexed form: gap below L ⇔ non-permutation Γ_s with s < L ⇔ indivisible on {0,…,L}; "below the recurrence time" (M:18; M:80; M:141; M:741 (status table row)) | M7, R2, REC1-U11 | Exact return Γ_L = I and its index L | F | — | n/a (not J) | Each printed site names "one fixed finite reversible representative" or L (M:18, M:80, M:141) | none | 9 sites (not determined 1, visible 8); codes none 8, unit 1. FULL:6608, gloss:117, M:18, M:80, M:141, M:451, M:455, M:741, Med:25 | Q3 propagation | queued (1 Phase-3 site; done in Main) |
| X-25 | Routed readback "for some n"; write/store/read clauses (M:147) | M8 | `rootedMap_periodic` on finite carriers | J | Overlap at storage time; (NR)/(RIG) for revival | Relabel: As X-20 for the revival clause; the write/store/read clauses are formalized only on finite carriers (paper transfer) | Only the storage-time overlap is used; later revival under (NR)/(RIG) (paper), RIGID compactness (Lean `ObservableRigidity.exists_reviving_return_of_overlap`) | none | 1 sites (visible 1); codes none 1. M:147 | none | done |
| X-26 | All-time rooted classification and periodicity of a fixed realization; ch18 §18.7 "finite information and exact finite recurrence" (M:646; ch18:20, :162–192, :40; FULL mirrors) | M10, CEN18-ch18, OA4:3 | Finite order of a finite bijection | F | — | n/a (not J) | M:646 is stated for "a bijection on a finite set"; ch18 §18.7 is stated "under A1" | M:646 "(b) the physically operative form under A1" → see X-01. ch18 §18.7 and FULL mirror: Q3 restates as finite-only ("for a finite substratum") and removes "the hypothesis A1 of a finite substratum" as a framework hypothesis | 37 sites (not determined 34, visible 3); codes ptr 3, unit 34. FULL:512, FULL:4751, FULL:4893, FULL:4895, FULL:4897, FULL:4899, FULL:4901, FULL:4903, FULL:4905, FULL:4907, FULL:4909, FULL:4910 … | Q3 propagation | queued (Step 2) |
| X-27 | Orbit capacity log₂ p; genericity count P_perm over bijections of a finite set (M:60; M:149–153) | M13 | Finite orbit; uniform count over a finite set of bijections | F | — | n/a (not J) | Finite-model statements (P0 action N); also X-12 for the capacity | none | 2 sites (visible 2); codes none 2. M:149, M:153 | none | done |
| X-28 | Overlap-and-return theorem; C4r/C4e no-go (M:143) | M6 | Finiteness only in the setup | J | None needed: row-stochastic Γ_s on finite V (`CausalReadback.c4r_implies_pIndivisible`) | No: Finite visible data only (Lemma 1) | A1-free as stated (REMAINDER class (a)) | none | no primary site | none | done |
| X-29 | Substratum Stage 1 recurrence-cycle P-indivisibility on a finite representative (Sub:137) | OA4:3, C6 | Finite order of a permutation | F | — | n/a (not J) | Printed "on a finite representative"; (NR) added by Phase 2 for the conclusion | none | no primary site; also Sub:137 | none | done (Phase 2) |
| X-30 | Bijectivity of the representative: eventual image, injectivity ⇒ surjectivity, merge prong (M:60; M:732 (iii); Sub:94; Meth:146–148; ch01:41) | M11, R3 | Finite-set arguments | J | (REV): φ a bimeasurable bijection of a measurable carrier (M:732 (iii)) | No: A posit, not a lemma; same observational status as A2 under A1 (REMAINDER §3); implies no cardinality | M:60 and M:732 (iii) print (REV) as the alternative; the finite argument stays as a finite statement ("on a finite representative φ is a bijection") | none in Main; Meth:146–148 by Q3 | 8 sites (not determined 3, visible 5); codes none 5, unit 3. FULL:374, FULL:708, ch01:41, ch02:78, Meth:106, Meth:146, Meth:148, Sub:94 | Q3 propagation | queued (3 Phase-3 sites; done in Main) |
| X-31 | §3.2 representation on a finite hidden space (M:268–290) | M12, S0:M3.e | Finite H as the setup | J | None: construction per finite-horizon law | No: Constructed finite witness, not an assumption on nature | Finite hidden spaces are constructed per law (S ⇒ D, `Equivalence.S_imp_D`); the representation is A1-free | M:268 pointer → X-01 | no primary site | none | done |
| X-32 | Characterization window t ≪ t_R (M:542) | M14 | t_R of a realizing substrate | J | None | No: A1-free | Restriction removed (MAIN-TR-1); the proof never consumes t_R | none | no primary site | none | done |
| X-33 | C3 capacity bound log₂\|C_H\| ≥ I* (M:518–520) | M15 | Counts the hidden states of a realization | J | None (finite realizations by definition) | No: A1-free as stated | Holds for every finite realization; class D is finite by definition | none | no primary site | none | done |
| X-34 | Coupling-graph causal cone; Bell ceiling (M:364; M:416–418) | M17 | Finite V in the first step of the finite-site proof | J | Finite read sets (posit (xiii)) | No: Local finiteness only | Arbitrary-site form with finite read sets printed in the same paragraph | none | no primary site | none | done |
| X-40 | A4's finite periodic lattice clause (finite quotient + finite alphabet ⇒ A1 via `a1_of_finite`) (Sub:98; ch02:82; SM:202; ch05:65; FULL mirrors) | C6, C7, R4, OA4:1, O-A4 | The printed class is finite; `SubstratumInterfaceAudit.a1_of_finite`:109 | O | — | n/a (not J) | Q1 (#1454 P2-Q1), in progress: possible outcomes J under A4∞ (kernel predicate `A4`:98 on an arbitrary additive group; LEAN-2(i) A2–A5 at ZMod 0 = ℤ), or a finite-only restriction kept. Not marked J in advance (safeguard 2) | Per Q1 outcome: Sub:98 "a finite periodic lattice, the quotient of a rank-d lattice by a finite-index sublattice" → A4∞ form with named conditions, or kept with "finite-only" stated | 6 sites (per unit Q1 6); codes unit 6. FULL:712, FULL:1380, ch02:82, ch05:65, SM:202, Sub:98 | Q1 | in progress |
| X-41 | Stage 2 chain under A4∞ (O-A4 verdict (i)): area-law lemma, Lemma 1c(i), (iii), Corollaries 1a, 1b, the d = 3 selection corollary SM:210 (SM:122, :202, :210, :252, :258, :270; Sub:157) | C7, OA4:5, OA4:6, OA4:10, OA4:12 | Inherits A4's finite lattice | O | — | n/a (not J) | Q1, in progress (O-A4 verdict (i): survives under A4∞, LF, H-μ(φ,Θ), H-μ(sp), H-Bloch) | Per Q1 outcome | 19 sites (per unit Q1 11, visible 8); codes ptr 8, unit 11. FULL:726, FULL:1340, FULL:1388, FULL:1392, FULL:1398, FULL:1404, ch02:96, ch05:25, ch05:73, ch05:77, ch05:83, ch05:89 … | Q1 | in progress |
| X-42 | Period-lattice conditions on the printed finite class: O_h needs O_h-invariant Λ; checkerboard needs even-sum periods; eight corners need Λ ⊂ 2ℤ³; SM:539 spin–taste; SM:1536 (SM:539; SM:1536; SM:242–374 (O_h uses)) | OA4:16, OA4:18 | Finite quotients that fail Stage-2 inputs (O-A4 §7) | O | — | n/a (not J) | Q1, in progress | Per Q1 outcome (SM:539 already names the odd-torus failure; SM:1536 "bipartite checkerboard structure" unqualified) | 2 sites (per unit Q1 2); codes unit 2. SM:539, SM:1536 | Q1 | in progress |
| X-43 | Fermion theorems on ℤ^d: Theorems 2, 3, 8, 8b, 10, 12, 13 (SM:286–302; SM:434–456; SM:535–547) | OA4:18 | Staggered phases, Brillouin corners, checkerboard | O | — | n/a (not J) | Q1, in progress ("(a) on (Z); (b) on (F)", O-A4 row 18) | Per Q1 outcome | 7 sites (per unit Q1 7); codes unit 7. SM:286, SM:302, SM:434, SM:440, SM:456, SM:535, SM:543 | Q1 | in progress |
| X-44 | Theorem 1a "Let S be finite"; SM:222 carrier; SM:250 caps "FINITE" (SM:242; SM:222; SM:250) | OA4:9, P2-F5 | Hypothesis stated; O-A4 §9a: unused by the proof | O | — | n/a (not J) | Q2 (#1454 P2-Q2), in progress: J (hypothesis removed) if the proof check confirms O-A4 row 9; otherwise kept finite | Per Q2 outcome: SM:242 delete "Let S be finite," (and mirrors) | 1 sites (per unit Q2 1); codes unit 1. SM:242 | Q2 | in progress |
| X-45 | Theorem 23 (reconstruction) under E1–E7 and A1–A6; its uniqueness "within the class A1–A6" (Sub:104–133; Sub:189–195; Sub:205–233; ch02:88–122; ch04:10–26; ch05:19; Str:768; gloss:13) | C6, OA4:26, R4 | A1 listed among the hypotheses; Stage 2 uses A4's finite lattice; Stage 3 H-count (X-70); Stage 1 exact return (X-29) | F | — | n/a (not J) | With A1 deleted, the theorem stands as a theorem about finite substrata satisfying A2–A6 (finite-only). Its infinite-lattice version is open pending Q1 (Stage 2), C1 (Stage 3, X-71) and X-21 (Stage 1) | Sub:104 and mirrors: "under E1–E7 and A1–A6 jointly" → "for a finite substratum satisfying E1–E7 and A2–A6"; "the structural class A1–A6" → "the class of finite substrata satisfying A2–A6"; ch02:122 "(violating A1)" → "(outside the finite class)" | 39 sites (not determined 5, visible 34); codes none 6, ptr 28, unit 5. FULL:718, FULL:720, FULL:748, FULL:752, FULL:1114, FULL:1130, FULL:1334, FULL:6504, ch02:88, ch02:90, ch02:118, ch02:122 … | final deletion | queued (Step 2; after Q1; 5 Phase-3 sites via Q3) |
| X-46 | OI-class substrata "satisfying A1–A6" (Structure Definition 9.9, Proposition 9.5 and dependent statements) (Str:646 and the R6/C11 sites of Structure) | C11 | Class definition | F | — | n/a (not J) | A definitional finite class; narrowing to A2–A6 plus the M4/M18 posits would be a definition change (REMAINDER C11) and is not proposed here | At deletion: "OI-class substrata (satisfying A1–A6)" → "finite OI-class substrata (finite, satisfying A2–A6)" | 57 sites (visible 57); codes none 2, ptr 55. FULL:895, FULL:905, FULL:2433, FULL:2451, FULL:2521, FULL:2597, FULL:2603, FULL:2607, ch03:34, ch03:44, ch09:18, ch09:36 … | final deletion | queued (Step 2) |
| X-50 | CP-indivisibility theorem (permutation-dilation family) (M:332–336) | M9, L6, R6 | Permutation unitary on finite H | F | — | n/a (not J) | Printed as a finite-representative statement (M:732 (ii) list). R6 lemma L6 (Koopman dilation on ℂ^V ⊗ L²(H,ρ)), in progress, may supply J or confirm the finite-only restriction | none at the pin; per R6 outcome | 2 sites (per unit R6 2); codes none 2. M:332, M:336 | R6 | in progress |
| X-51 | Physical-memory theorem and C2 quantitative form (M:459–475) | M16, L7 | Uniform-prior finite coupling model | F | — | n/a (not J) | Printed as a finite-representative statement (M:732 (ii) list). R6 lemma L7, in progress | none at the pin; per R6 outcome | 2 sites (per unit R6 2); codes none 2. M:459, M:473 | R6 | in progress |
| X-52 | Deep-sector cardinality as gauge, finite windows; Theorem 24(i) population law, (ii), (iii) trace-class identity; GR Appendix B (GR:132–138; GR:871–905; Sub:251–264; M:732 (ii) transfer clause) | M21, C3, C8, OA4:23, OA4:24, OA4:25 | Finite decoupled factor; uniform ω_H | J | (D1)–(D5), with (D5) μ_H = u_{B_n}⊗ν, ν any normalized law (GR:877–883); trace-class σ_A (O-A4 row 24) | No: Finite cone and a uniform factor on a finite boundary window; the deep law is of any cardinality | GR Appendix B printed for a site set of any cardinality under (D1)–(D5) | none | 15 sites (visible 15); codes none 15. FULL:5867, FULL:5871, appb:190, appb:194, GR:132, GR:134, GR:136, GR:138, GR:875, GR:883, GR:885, GR:889 … | none | done |
| X-53 | All-time coherent-channel invariance under an infinite normalized decoupled factor; transfer of recurrence-scale content (Theorem 24(i) coherent form, Corollary (iii)) (Sub:262; Sub:268 (iii); ch02:144) | M21, C8, L9, OA4:23 | Finite factor A; uniform ω_H | F | — | n/a (not J) | Printed finite ("This is a finite, fixed-interface result; an infinite extension ... is not established", Sub:262). R6 lemma L9, in progress | none at the pin; per R6 outcome | 4 sites (per unit R6 3, visible 1); codes none 3, ptr 1. FULL:774, ch02:144, Sub:262, Sub:268 | R6 | in progress |
| X-54 | Storage and memory: "S finite capacity (under A1)" (Sub:44; ch02:14–18) | C9 | Explicit | F | — | n/a (not J) | Interpretive; no theorem rests on it (A1-09 §23.2) | At deletion: "finite capacity (under A1)" → "finite capacity in a finite representative" | 10 sites (visible 10); codes none 6, ptr 4. FULL:644, FULL:646, FULL:648, FULL:662, ch02:14, ch02:16, ch02:18, ch02:32, Sub:44, Sub:52 | final deletion | queued (Step 2) |
| X-55 | Computation: finite-carrier capacity comparison; "the framework's finiteness hypothesis (A1)" (Comp:120, :122, :178, :182; ch14:160–272; FULL mirrors) | C12 | A1 by statement | F | — | n/a (not J) | Phase 3 (Q3): restate as conditional statements about finite substrata | Q3 per site; Comp:182 "The framework's finiteness hypothesis (A1)" → "A finite substratum" | 10 sites (not determined 10); codes unit 10. FULL:3760, FULL:3764, FULL:3784, FULL:3862, ch14:160, ch14:164, ch14:184, ch14:262, Comp:178, Comp:182 | Q3 propagation | queued (Step 2) |
| X-56 | Exact linear rule shell splitting into cycles as motivation for (EM) (M:732 (v); M:766 (ii); SM §4.2) | C14 | Cycle counts on a finite lattice | F | — | n/a (not J) | M:766 states the cycle structure does not settle (EM) | none | no primary site; also M:732 (v), M:766 (ii) | none | done |
| X-57 | Appendix A finite sectors; Page value as exact cycle average on a finite configuration space (GR:609; GR:719; GR Thm A.8) | REC1-U12, CEN17-GR-729/753, FCLASS-U1 | Finite configuration spaces | F | — | n/a (not J) | Printed as finite-model statements (Phase 2 N) | none | 2 sites (visible 2); codes none 2. GR:609, GR:719 | none | done |
| X-60 | §4.6 theorem τ_B(V) ≤ τ_mix + O(ε) for the iterated compression (operator step) (M:752–760; M:766 (IL)) | M18, S0:M19.b, T1 | Counting inner product; finite S in the Setup | J | (IL): normalized φ-invariant μ, P the μ-conditional expectation onto declared local observables of a finite readout support, (EM) on μ-centred L²(μ) observables | No: A normalized law with a finite readout support; τ_B transfer is an A1-independent source gap (REMAINDER M18) | M:766 prints (IL) as a hypothesis of the decay estimate (Phase 1 E14); O(ε) and exact recurrence stay finite-representative statements | none | 5 sites (visible 5); codes none 5. M:750, M:752, M:758, M:760, M:766 | none | done |
| X-61 | Anti-Boltzmann-brain corollary (M:762) | M20, S0:M19.b | Inherits M18's setting | J | As X-60 | No: As X-60 | Operator step as X-60; local equilibrium enters as a definition | none | 2 sites (visible 2); codes none 2. M:165, M:762 | none | done |
| X-62 | Typicality step: equilibrium macrostate ⇒ local equilibrium via canonical typicality [31] (M:764) | M19, R5, S0:M19.a, T6, O1(a) | [31] is a finite-dimensional shell theorem; M:764 dropped its typical-state quantifier | F | — | n/a (not J) | Main:764 unit (PR #1463, in progress): restores [31]'s typical-state and fixed-subsystem form and states G1 (configuration microstates outside the typical set; ensemble reading = the shell law's marginal). Then a finite-representative statement, listed as such at M:732 (ii) and M:766. The global-to-local inference for laws on an infinite carrier (L8-sel) needs R1: open, carried by X-63 | M:764: replace "canonical typicality [31] implies every local subsystem is also in its local equilibrium." by the typical-state, fixed-subsystem statement with G1 (exact text in PR #1463 LEDGER) | 1 sites (per unit Main:764 1); codes none 1. M:764 | Main:764 | in progress |
| X-63 | The twelve global-phase claims: "observers exist only in the non-equilibrium phase of (S, φ)", the §4.6 heading, the past-hypothesis replacement and their restatements (M:748 (T22); M:764 (T6, T7b); Sub:56 (T11b, T11c); Sub:401 (T12); Sub:542 (T14); Str:718 (T15); Str:734 (T16); Comp:212 (T17b); ch02:192 = FULL:822 (T18); ch04:178 = FULL:1282 (T20b)) | T6, T7b, T11b, T11c, T12, T14, T15, T16, T17b, T18, T20b, T22, C10, R5 | Global-to-local step T6 (A1 + [31]); and, by G3, no phase-discriminating statement in the iterated description | O | — | n/a (not J) | Step 2 decision (queued, not authorized). Strongest result that does follow: the region-level form W* (STAGE1ii §6), J under fast (EM) on declared regions | Each site: restate as W* ("(C2-slow) observers occur only outside regions whose effective channel satisfies (EM) at τ_mix ≪ τ_S, in the iterated description") or mark the phase statement open; the past-hypothesis replacement (Sub:56, Comp:212) marked open (O-INFLOW, X-82). Exact wording is the Step-2 unit's | 17 sites (not determined 2, per unit Step-2 phase 15); codes unit 17. FULL:822, FULL:919, FULL:1140, FULL:1282, ch02:192, ch03:58, ch04:36, ch04:178, M:748, Meth:283, Meth:441, Str:718 …; also M:764 (T6, T7b; the line is mapped to X-62) | Step-2 phase | queued (Step 2) |
| X-64 | RETAINED-WITH-(LE) rows: the thermal "in particular" clause, the proof's division of labour, the scope lists naming [31] (M:758 (T2); M:760 (T3); M:766 (T8); M:664 (T23); M:732 (T24a)) | T2, T3, T8, T23, T24a | [31] on the finite representative | F | — | n/a (not J) | As printed, statements about the finite representative (M:766 "the canonical-typicality clause ... are statements about the finite representative"). STAGE1ii: each also holds with a declared (LE) in place of [31]; that restatement is optional and Step-2 scoped | none required for A1 exit | 1 sites (visible 1); codes none 1. M:664; also M:664, M:732, M:758, M:760, M:766 | none | done |
| X-70 | H-count: classical horizon temperature as a counting derivative, decoupled case (GR:58; GR:88; ch07:42; Sub:175–185 (Stage 3)) | C1, S0:C1.a, OA4:22 | "Under A1, restrict the finite total system to a conserved energy shell" | F | — | n/a (not J) | Printed conditional on A1 (owner: "GR:58 counting stays conditional", Phase 2 CTL-15). With A1 deleted it reads as a statement about a finite total system. An A1-free decoupled form exists in records only (P7B Theorem under H1–H14; owner Q4: no new companion claims) | At deletion: GR:58 "Under A1, restrict the finite total system" → "For a finite total system, restrict it"; "that the total system is finite (A1)" → "that the total system is finite"; same at GR:88, ch07:42 | 3 sites (visible 3); codes ptr 3. FULL:1907, ch07:42, GR:58 | final deletion | queued (Step 2) |
| X-71 | C1 coupled shell law: existence of a normalized invariant shell law for coupled bijections (GR:58 (coupled case); P7B 6.3) | C1, S0:C1.a | No normalized invariant shell law for some coupled bijections (P7B 6.3 (ii)) | O | — | n/a (not J) | Open (owner safeguard 3: "C1 (coupled shell law) remain[s] open"); R1-L8 Stage 1(iv) deferred | none: GR:58 is stated for a finite total system with the boundary interaction negligible at the shell scale; no claim for the coupled case is printed, so there is nothing to qualify | no primary site; also GR:58 | none | open |
| X-72 | Calibration ħ = c³ε²/(4Gσ), the 1/4, ρ_s = ρ_crit, the 2/(d−1) concordance, a₀ chain (GR:78–88; GR:316–318; GR:422–440; GR:466–500; SM:182–196; Sub:88, :157; appB:169; ch05:59–60; FULL mirrors) | C2, S0:C1.b, S0:C1.c, S0:C1.d, S0:C1.e | Inherits H-count (X-70) | F | — | n/a (not J) | STAGE1i and PROV-CORR (#1458, #1459): the surviving normalization is Clausius; the law-dependent outputs (ħ coefficient, ε, N_modes, the count's equality with A/4l_p²) are unobservable and stated as calibrations; ρ_s and the concordance are identities of the GR inputs; a₀ and Tully–Fisher are imported | none beyond X-70's pointer rewrite | 1 sites (visible 1); codes ptr 1. GR:88 | none | done (PROV-CORR, PROV-CORR-2) |
| X-73 | H-BD and the boundary-only lemma (b) with gauge corollary (GR:112–128; Sub:92 (H-BD sentence); appB:177–194; ch02:44; ch07:46) | C4, S0:C4.a, L10 | Counting on finite C_D with injectivity (GR:126) | F | — | n/a (not J) | Printed with its counting condition (Phase 2 N: "measure condition stated"). L10 (measure-theoretic H-BD with the fibrewise non-expansion of STAGE0 F2) is open; no unit | none | 5 sites (visible 5); codes none 5. GR:112, GR:122, GR:124, GR:126, GR:128 | none | done |
| X-74 | Effective finiteness: E3 bounds \|C_V × C_B\| ≤ e^{S∂}; "the interpretive premise of A1" (Sub:268 (i), (ii); Sub:54; Sub:92) | C4, S0:C4.b | Reading of E3 as the premise of A1 | F | — | n/a (not J) | A bound on the observationally relevant space under H-BD; not finiteness of every sector (Sub:92 says so) | At deletion: Sub:268 (i) "This reading is the interpretive premise of A1." → delete the sentence | no primary site; also Sub:54, Sub:92, Sub:268 | final deletion | queued (Step 2) |
| X-75 | Operational completion, OI⁺, typed and quasilocal identifications; forward local gauge algebra (GR:239–282; A1-11) | C5, C13 | Finite carriers of the operational theory | J | None (finite operational carriers; arbitrary site set with finite local stages) | No: A1-free | A1-free as stated (REMAINDER class (a)); "under A1" at GR:257 is a pointer (X-02) | GR:257 "The concrete OI substratum under A1" → "The concrete OI substratum in its finite model" | no primary site | final deletion | queued (Step 2) |
| X-80 | FCLASS U1 interpretive uses: cosmic topology, consciousness, Page curve, "one way to realize A1 in a model" (ch18:240–288; FULL mirrors; ch19:212–216, :360) | FCLASS-U1 | Statements about realizing or assuming A1 | F | — | n/a (not J) | Phase 3 (Q3) for ch18; ch19 by the deletion edit | Q3 per site; ch19 pointers → X-02 rule | 8 sites (not determined 8); codes unit 8. FULL:4973, FULL:4975, FULL:4991, FULL:5019, ch18:242, ch18:244, ch18:260, ch18:288 | Q3 propagation | queued (Step 2) |
| X-81 | Lean: kernel predicate `SubstratumInterfaceAudit.A1` (Finite Conf) and theorems stated with it (verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:84, :109, :185, :786; WaveSubstratumUnbounded.lean:70; HexLatticeGas.lean:312; A6Instantiation.lean:278, :515; ManuscriptAxioms.lean:76) | CK8 | Finiteness predicate on finite carriers | F | — | n/a (not J) | Kernel statements about finite carriers are finite-only by construction; `waveZ_not_A1` and the A2–A5 predicates at ZMod 0 (LEAN-2(i)) are the infinite controls. No Lean change is needed for the deletion; manuscripts citing these read them as finite-only | none | no primary site; also Lean only (no manuscript site states the predicate) | none | done |
| X-82 | O-INFLOW: finiteness excludes the incoming-stream endpoint; dropping A1 admits it (Sub:56; Cx:212; ch18:40; FULL mirror) | INFLOW, R1 | PREP 1.5(d): the endpoint survives only without A1 | O | — | n/a (not J) | Open obligation (REMAINDER §5, #866); a budget exclusion inherits R1. No unit | Q3 (Cx:212, ch18:40) and Step 2 (Sub:56): state the inflow question as open where the sentence relies on finiteness to exclude it | 3 sites (not determined 3); codes unit 3. FULL:4771, ch18:40, Cx:212; also Sub:56 (mapped to X-63) | Step-2 phase | queued (Step 2) |
<!-- TABLE:END -->

## 3. Safeguard checks

### 3.1 S1 — no disguised A1 (safeguard 1)

Every J row was checked to see whether its weaker condition implies total finiteness or reproduces
A1 under another name. None does: no J row has S1 = `Yes`. That is CK5, and the self-test shows
that one `Yes` fails the check.

- **`No` (14 rows).** The conditions are of these kinds:
  - normalization of a law on a measurable carrier (X-14);
  - finite visible or finite cone data:
    - (IP) uniform on the finite visible factor (X-15);
    - H-ν (X-13);
    - (IL) with a finite readout support (X-60, X-61);
    - (D1)–(D5) with a deep law of any cardinality (X-52);
    - finite read sets (X-34);
  - invariance properties of a normalized law (X-17);
  - (REV), a measurable bijection (X-30);
  - constructions per finite law (X-31);
  - A1-free as stated (X-28, X-32, X-33, X-75).

  For each, a model on an infinite carrier satisfies the condition, as cited in the row: β_A,
  Lemma U, GR Appendix B, or RIGID.
- **`Relabel` (3 rows: X-20, X-23, X-25).** The condition is (NR), (RIG) or compact orbit closure.
  - It is logically weaker than A1: RIGID's rotation × Bernoulli example satisfies it without finite
    order.
  - It is not a disguised A1 in the safeguard's sense.
  - Two qualifications travel with it, and the review should check that the manuscripts do not
    present it as more:
    1. At an unspecified time it has no finite-window test (REMAINDER §3). F11 at an accessible
       time is testable on that window.
    2. For OI's selected update on ℤ^d, (NR) fails under β_A, the law P-ED selects (NR-1 Thm 3.3).
       It holds under the torus counting law μ_L, which is supported on periodic configurations
       (STAGE0 F1; NR-1 open question 3). The only known way the selected update satisfies (NR)
       is therefore finiteness under another name.
  - X-21 records the physical source of a return for the selected update as open.
- **Rows where a weaker condition would be disguised A1.**
  - X-40: A4's finite periodic lattice with a finite alphabet implies A1
    (`SubstratumInterfaceAudit.a1_of_finite`). Deleting item (ii) while A4 keeps its finite clause
    would leave A1 in force under the name A4. This is why X-40 is O and gates the deletion through
    Q1.
  - X-12: μ-O and μ-R are uniform laws on finite orbits. They are finite-only by owner decision, not
    weaker conditions.

### 3.2 S3 — no silent promotion (safeguard 3)

Visibility at the pin, counted over the 465 sites mapped to a row:

- **Visible.** Mostly sites already dispositioned by Phases 0–2, which state A1, a finite
  representative, a finite model or a named hypothesis. This includes the `ptr` sites, which state
  the hypothesis by name and must be rewritten when the name is deleted.
- **Not determined (78).** These are the 77 Phase-3 sites (PREREG CK7) and glossary:105, all owned by
  Q3 propagation (§4). Under the Phase-2 dispositions, sites such as ch18 §18.7 state the finite
  recurrence consequences "under A1". After deletion they must read as finite-only statements, and
  the Q3 census must confirm this site by site.
- **Per unit.** Q1, Q2, R6, Main:764 and the Step-2 phase unit decide these sites.

R1's physical justification (X-11) and C1 coupled (X-71) are O rows with the qualification printed:
M:732 (iv) "not derived", and GR:58 stated for a finite total system.

## 4. The 77 Phase-3 sites (and glossary:105), owner Q3 propagation

These are the out-of-scope sites of A1-PHASE2 §2 and #1454 P2-Q3. Each line below is a pin line
number with its ledger row. The FULL lines are the mirrors of ch14 and ch18.

<!-- PHASE3:BEGIN -->
- **Comp** (4): 120 (X-01), 122 (X-10), 178 (X-55), 182 (X-55)
- **Cx** (1): 212 (X-82)
- **FULL** (28): 3760 (X-55), 3764 (X-55), 3784 (X-55), 3862 (X-55), 3872 (X-10), 4751 (X-26), 4767 (X-10), 4771 (X-82), 4893 (X-26), 4895 (X-26), 4897 (X-26), 4899 (X-26), 4901 (X-26), 4903 (X-26), 4905 (X-26), 4907 (X-26), 4909 (X-26), 4910 (X-26), 4911 (X-26), 4914 (X-26), 4915 (X-26), 4917 (X-26), 4921 (X-26), 4923 (X-26), 4973 (X-80), 4975 (X-80), 4991 (X-80), 5019 (X-80)
- **Intro** (2): 12 (X-20), 93 (X-20)
- **Med** (1): 25 (X-24)
- **Meth** (13): 106 (X-30), 146 (X-30), 148 (X-30), 156 (X-01), 158 (X-01), 283 (X-63), 339 (X-45), 345 (X-45), 357 (X-45), 367 (X-45), 369 (X-45), 441 (X-63), 517 (X-01)
- **ch14** (5): 160 (X-55), 164 (X-55), 184 (X-55), 262 (X-55), 272 (X-10)
- **ch18** (23): 20 (X-26), 36 (X-10), 40 (X-82), 162 (X-26), 164 (X-26), 166 (X-26), 168 (X-26), 170 (X-26), 172 (X-26), 174 (X-26), 176 (X-26), 178 (X-26), 179 (X-26), 180 (X-26), 183 (X-26), 184 (X-26), 186 (X-26), 190 (X-26), 192 (X-26), 242 (X-80), 244 (X-80), 260 (X-80), 288 (X-80)
- **gloss** (1): 105 (X-20)
<!-- PHASE3:END -->

## 5. Item (ii) and every pointer to it (`ptr` sites)

Item (ii) is X-00 (M:732, M:60). Every site below names A1, "total finiteness", "the
total-finiteness posit", "posit (ii)" or "ledger item (ii)" in the sense of the posit. These are P0
patterns core P1, P2 and P5, with the P0 false positives removed: the anomaly conditions "(A1)" at
appB:235 and :246 are FP. Each site is rewritten in the deletion edit by the rule of its row:

- **F row:** the pointer becomes the finite-only scope ("for a finite substratum", "on a finite
  representative", "in its finite model").
- **J row:** the pointer becomes the weaker condition.
- **O row:** the pointer becomes the open statement.

<!-- PTR:BEGIN -->
- **FULL** (51): 320 (X-01), 361 (X-01), 496 (X-01), 512 (X-26), 638 (X-02), 646 (X-54), 706 (X-02), 718 (X-45), 720 (X-45), 748 (X-45), 752 (X-45), 766 (X-02), 788 (X-02), 842 (X-02), 895 (X-46), 905 (X-46), 945 (X-02), 1114 (X-45), 1130 (X-45), 1330 (X-02), 1334 (X-45), 1338 (X-02), 1398 (X-41), 1404 (X-41), 1907 (X-70), 1983 (X-02), 2433 (X-46), 2451 (X-46), 2521 (X-46), 2597 (X-46), 2603 (X-46), 2607 (X-46), 5196 (X-01), 5282 (X-01), 5284 (X-01), 5286 (X-01), 5430 (X-01), 6171 (X-01), 6251 (X-01), 6253 (X-01), 6257 (X-01), 6259 (X-01), 6261 (X-01), 6263 (X-01), 6267 (X-01), 6269 (X-01), 6271 (X-01), 6291 (X-01), 6502 (X-01), 6504 (X-45), 6628 (X-01)
- **GR** (6): 20 (X-01), 58 (X-70), 88 (X-72), 257 (X-01), 261 (X-01), 589 (X-20)
- **M** (12): 36 (X-01), 44 (X-01), 60 (X-00), 111 (X-01), 129 (X-20), 224 (X-01), 268 (X-01), 594 (X-01), 646 (X-26), 708 (X-01), 726 (X-01), 732 (X-00)
- **SM** (7): 22 (X-01), 30 (X-02), 60 (X-02), 158 (X-41), 222 (X-41), 232 (X-41), 316 (X-41)
- **Str** (42): 80 (X-46), 86 (X-46), 134 (X-46), 136 (X-46), 140 (X-46), 196 (X-46), 206 (X-46), 224 (X-46), 230 (X-46), 256 (X-46), 258 (X-46), 260 (X-46), 264 (X-46), 270 (X-46), 272 (X-46), 314 (X-46), 316 (X-46), 320 (X-46), 327 (X-46), 331 (X-46), 339 (X-46), 351 (X-46), 359 (X-46), 375 (X-46), 560 (X-46), 646 (X-46), 701 (X-46), 730 (X-02), 732 (X-02), 746 (X-46), 768 (X-45), 866 (X-46), 1006 (X-46), 1008 (X-46), 1010 (X-46), 1012 (X-46), 1014 (X-46), 1016 (X-46), 1030 (X-46), 1066 (X-46), 1237 (X-46), 1303 (X-46)
- **Sub** (17): 44 (X-54), 52 (X-54), 92 (X-02), 104 (X-45), 123 (X-45), 129 (X-45), 133 (X-45), 193 (X-45), 205 (X-45), 207 (X-45), 212 (X-45), 216 (X-45), 223 (X-45), 233 (X-45), 268 (X-53), 288 (X-02), 389 (X-02)
- **appc** (11): 16 (X-01), 96 (X-01), 98 (X-01), 102 (X-01), 104 (X-01), 106 (X-01), 108 (X-01), 112 (X-01), 114 (X-01), 116 (X-01), 136 (X-01)
- **ch00** (1): 95 (X-01)
- **ch01** (3): 28 (X-01), 163 (X-01), 179 (X-26)
- **ch02** (10): 8 (X-02), 16 (X-54), 76 (X-02), 88 (X-45), 90 (X-45), 118 (X-45), 122 (X-45), 136 (X-02), 158 (X-02), 212 (X-02)
- **ch03** (3): 34 (X-46), 44 (X-46), 84 (X-02)
- **ch04** (2): 10 (X-45), 26 (X-45)
- **ch05** (5): 15 (X-02), 19 (X-45), 23 (X-02), 83 (X-41), 89 (X-41)
- **ch07** (2): 42 (X-70), 118 (X-02)
- **ch09** (6): 18 (X-46), 36 (X-46), 106 (X-46), 182 (X-46), 188 (X-46), 192 (X-46)
- **ch19** (5): 126 (X-01), 212 (X-01), 214 (X-01), 216 (X-01), 360 (X-01)
- **gloss** (3): 11 (X-01), 13 (X-45), 137 (X-01)
<!-- PTR:END -->

## 6. Deletion criterion for item (ii) (PREREG §6) and the distance to it at the pin

Item (ii) may be deleted only when all of the following hold at one exact head, with a separate owner
decision (owner safeguard 4; Step 2):

1. **CK1–CK8 pass at that head.** At the pin: pass.
2. **Every row is closed.** Its status is `done`, or it is an O or F row whose qualification is
   visible at every mapped site. At the pin these remain:
   - **10 rows `in progress`:**
     - Q1: X-16, X-40–X-43;
     - Q2: X-44;
     - R6: X-50, X-51, X-53;
     - Main:764: X-62.
   - **The `queued` rows:**
     - Q3 propagation: X-10, X-20, X-24, X-26, X-30, X-55, X-80;
     - R1/R2 scoping: X-12;
     - Step-2 phase: X-63, X-82;
     - the deletion edit: X-00, X-01, X-02, X-45, X-46, X-54, X-70, X-74, X-75.
   - **The open rows:** X-11, X-21 and X-71 are closed already in the sense of this item, since each
     is stated as open or has no manuscript claim.
3. **No disguised A1.** No J row has S1 = `Yes` (holds at the pin). Each `Relabel` condition must be
   stated as such where the condition is introduced. That means (NR) at M:131 and the
   companion/book restatements need the two qualifications of §3.1. Checking that wording is a
   review item (§8). Adding it, if missing, is a correction for the Step-2 scoping unit.
4. **Pointers rewritten.** All 186 `ptr` sites (§5) are rewritten in the deletion edit by their
   row's rule. After that edit, a fresh P0 pattern scan finds no core P1, P2 or P5 hit outside the
   false positives.
5. **Independent review.** A non-author review of that exact head records that no result silently
   relies on A1. A rerun of `ledger_check.py` at that head is part of the evidence. Its `check`
   mode fails if any line matching the P0 pattern set is unmapped.

**What may remain after deletion.** The F rows stay as finite-only theorems stated as such: X-10,
X-12, X-16, X-18, X-22, X-24, X-26, X-27, X-29, X-45, X-46, X-50, X-51, X-53–X-57, X-62, X-64,
X-70, X-72–X-74, X-80 and X-81. The O rows that are not removed stay as open claims stated as open:
X-11, X-21, X-63, X-71, X-82, and whichever of X-40–X-44 Q1 and Q2 leave open.

**What may not remain.** No claim may remain whose support is A1, presented as a property of nature or
of the framework without its finite-only or open qualification. One example: Theorem 23 "under
A1–A6" (X-45) must become a theorem about finite substrata satisfying A2–A6, with its
infinite-lattice version open pending Q1, X-71 and X-21.

## 7. Deviations from PREREG

- **D1 (site placement).** Twelve sites are placed by override in `rows.json`:
  - A4's clause and its mirrors → X-40;
  - SM:539 and SM:1536 → X-42;
  - the seven fermion theorem lines → X-43;
  - the Stage 1(ii) global-phase lines → X-63;
  - glossary:105 → Q3.

  M:60, M:664, M:732 and Sub:56 are reassigned by override to X-00, X-64, X-00 and X-63. All of these
  lines carry rows that P0's first-row rule would have assigned elsewhere.
- **D2 (shared lines).** CK5 accepts an F or O row whose sites are all primary to another row when the
  row lists them in an explicit `mirrors` field. These rows are X-11, X-12, X-18, X-21, X-29, X-56,
  X-63, X-64, X-71, X-74, X-81 and X-82.
- **D3 (relocation).** P0 quotes are single sentences, so relocation matches a quote inside a line,
  then by the applied Phase-1 and Phase-2 splices, then by 60-character anchors, then by
  longest-common-block ≥ 0.5. The result:
  - 437 exact, 32 by splice, 81 by anchor and 16 fuzzy;
  - every fuzzy match ≥ 0.95;
  - none removed;
  - no two P0 sites on one line.
- **D4 (census extension).** The 11 kept Phase-2 census-extension lines (GR:219, :761, :879, :880,
  :895, :901; Str:734 before override, :800, :821, :972; Sub:333) are included with their Phase-2
  keep reasons, beyond CK3's P0 scope.
- **D5 (status).** The vocabulary adds that `done` allows the pointer rewrites of the deletion edit.

## 8. Review checklist

1. **Row completeness against the sources.**
   - Every REMAINDER row M1–M21, C1–C14 and residue R1–R6 has a row (CK1).
   - Every STAGE0 (b)/(c)/undetermined row, every STAGE1ii NOT FOLLOWING and RETAINED-WITH-(LE) row,
     and every O-A4 (b)/(c) step has a row (CK2).
   - Check by reading, not only by the script, that no dependency in those records is missing.
2. **Disposition per row against PREREG §7.** In particular:
   - (a) No Q1, Q2 or R6 row is J in advance.
   - (b) X-16, X-70, X-73: the A1-free forms exist only in records (P6, P7B), and owner Q4 bars new
     companion claims, so the printed statements are F.
   - (c) X-45: Theorem 23 is F after deletion, with its infinite version open.
3. **S1 on every J row**, with the `Relabel` rows X-20, X-23 and X-25 and the STAGE0 F1 flag. Is
   anything there a disguised A1 that should be F or O?
4. **S3.**
   - Spot-check that the `visible` sites state their qualification.
   - The 78 Q3 sites are undetermined by design.
   - Confirm that no Main, companion or FULL site outside the map asserts an A1-dependent result
     without a qualification. This covers sentences that match no P0 pattern, which is the limit of
     CK4.
5. **The corrections proposed for X-00, X-01, X-02, X-45, X-46, X-70, X-74 and X-75.** They are
   proposals for the deletion edit and are not applied. Check that each preserves the claim's proved
   scope and introduces no new claim.
6. **The deletion criterion (§6).** Check that it is no weaker than owner safeguard 4.
7. **`ledger_check.py check` and `self-test`.** Both pass at the head. The countercontrols must fail
   as stated (an unmapped site, a J row with S1 `Yes`, a dropped Phase-3 site).

## 9. Limits

- The site map reuses P0's lexical census and its pattern set. A1 dependencies carried by sentences
  that match no pattern and are not P0 structural sites are outside CK4 (review item 4).
- Rows inherit the classification of their source audits. Where a source audit is itself awaiting
  review, the row inherits that status.
- Line numbers are at the pin. Q2 edits SM.md in parallel, so SM line numbers may move. `build`
  regenerates the map at any head. At a head whose manuscripts differ from the pin, `check` reports
  "REBUILD differs" until the map is rebuilt and re-reviewed. That is intended, because the map
  certifies one tree.
- Q1, Q2, R6 and the Main:764 unit are in progress. Their rows record possible outcomes, not
  results.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7047514209 | Authorization | Provenance; quoted with author and time |
| #1169 comments 7041456852, 7035888700 | X-12 (μ-O/μ-R finite-only), X-16/X-70 (owner Q4) | Owner decisions quoted as dispositions; provenance for the decision, with no scientific claim resting on them |
| #1454 | Phase-3 scope, Q1, Q2 | Provenance (planning) |
| PR #1463 (Main:764 unit) | X-62 | Provenance: the correction is in progress. X-62's F disposition rests on [31] and STAGE1ii G1, both on `main` |
| Q1, Q2 and R6 records (in progress, not on `main`) | X-16, X-40–X-44, X-50, X-51, X-53 | Provenance: these rows state the disposition at the pin, not those units' results |

## 11. Verification status (§A.46 item 4)

- **Evidence level.** Paper-only ledger, writer-checked. The completeness checks are mechanical and
  reproducible from `main` with `ledger_check.py`. The row dispositions inherit the evidence level of
  the cited records.
- **Missing.** An independent non-author review of this ledger, and of its S1 verdicts in particular.
- **Accountable Issue.** #1454 (with #1169 for the authorization).
- **What would resolve it.** A review recorded on the guiding PR, followed by an owner merge decision.

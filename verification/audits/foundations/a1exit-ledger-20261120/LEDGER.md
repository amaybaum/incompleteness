# A1-EXIT ledger — every remaining A1 dependency, its end state, exit route and correction

**Status.** Writer's paper-only ledger, WIP / UNVERIFIED, revised after the independent review of
`5bda14c5`, round 1 (REVISE, small and additive;
[PR #1466 comment 7048919956](https://github.com/amaybaum/incompleteness/pull/1466#issuecomment-7048919956)).
The response is in §12, and a delta review is required. The schema, sources, completeness check and
deletion criterion were fixed in `PREREG.md` (commit `b352d4a4`, pushed before any row was populated;
unchanged since). The ledger is built from existing records only. It adds no proof, measure construction
or physical premise, and it edits no manuscript, Lean or registry file. No classification of the source
audits is redone. A1 (Main posit ledger item (ii)) remains open and unadopted.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, Step 1 row A1-EXIT. Goal link (§A.47): "Make OI's foundational formulation
independent of the assumption that the whole universe is finite, while keeping honest limitations on the
results that still require finiteness."

**Source pin.** `main` at `fbca1df98f630aa0dd334c6e7f9f9a193da64394` (merge of #1464, Q2). The branch
merged `main` at that commit, and the site map was rebuilt there. `File:n` is line `n` at the pin.
Abbreviations are those of PREREG. The map records the pin and a digest of the manuscript tree. `check`
fails with "PIN MISMATCH" and lists the differing sites on any other tree (D9).

**Owner records after the preregistration.**

- **Q2 merged** (#1169 c.7048183824, `amaybaum`, 2026-11-20T19:04:33Z): SM Theorem 1a holds for any set S.
  X-44 is J at the pin (D9). A pre-existing stale coverage-ledger entry
  (`verification/coverage/LEDGER.json`:1494–1495) is routed to #1462 as PF-6.
- **A4 formulation and deletion requirements** (#1169 c.7048255658, 2026-11-20T19:08:01Z). Rows X-40–X-43
  and X-45 apply the size-independent A4 formulation, and §6.1 records the deletion requirements (D6).
- **Regression audit.** The final regression audit is tracked in #1468. Rows X-47 and X-48 are its inputs.

## Files

| File | Content |
|---|---|
| `PREREG.md` | Schema, sources, checks CK1–CK8, deletion criterion, decision rule (frozen) |
| `rows.json` | The 59 dependency rows and the site-assignment rules (P0 row map, class map, site overrides, new-site rules, Lean entries, the pin) |
| `sitemap.json` | 696 sites at the pin, with the pin and the manuscript-tree digest. The 566 Phase-0 sites are relocated to the pin. Added: 11 lines new since Phase 0, 11 Phase-2 census-extension lines, and 108 sites added by override. The override sites are the review's B1/B2 sites, the classical-dimension family, the Q1 consumer lines, the global-phase lines, and the 44 lines of the extended criterion-5 scan, each read by hand. Each site carries its row, correction code, owner and S3 |
| `ledger_check.py` | `build` regenerates `sitemap.json` and prints the extended scan. `render` writes the generated blocks below. `check` verifies the pin digest, re-runs the build, compares it with the committed map and blocks, runs CK1–CK8, and reports the extended scan (informational). `self-test` runs three countercontrols |

The run at the pin gives these results:

- `python3 -I -B verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py check` reports
  0 unmapped lines in the extended scan and `CK1-CK8 PASS`.
- `… self-test` reports `self-test PASS`.

## 1. Summary

<!-- COUNTS:BEGIN -->
| Measure | Counts |
|---|---|
| Rows | 59 |
| Disposition | F 29, J 17, O 13 |
| S1 on J rows | No 15, Relabel 2 |
| Row owner | Main:764 1, Q1 5, Q2 1, Q3 propagation 6, R1/R2 scoping 5, R6 3, Step-2 phase 2, final deletion 9, none 25, regression audit (#1468) 2 |
| Row status | done 24, in progress 9, open 3, queued 23 |
| Sites in the map | 696 (560 mapped to a row; 136 FP, FREE or kept) |
| Mapped sites by correction code | none 190, ptr 193, unit 177 |
| Mapped sites by owner | Q1 28, Q3 propagation 81, R1/R2 scoping 8, Step-2 phase 15, final deletion 193, none 190, regression audit (#1468) 45 |
<!-- COUNTS:END -->

**Reading the counts.**

- **J (17).** Each J row is A1-free as stated, or proved under a weaker condition already printed with
  the result. Two J rows carry S1 = `Relabel`, and their qualification is not yet printed, so both are
  queued:
  - X-20: recurrence-scale P-indivisibility under (NR);
  - X-23: the index-free equivalence.
- **F (29).** Each F row is a true statement about finite systems or finite representatives. With A1
  deleted, it stays as a finite-only statement.
- **O (13).** The O rows fall into these groups:
  - **Q1 rows, in progress (X-40–X-43).** These are not marked J in advance (safeguard 2).
  - **X-47 (finite-L numerics).** This row has no convergence result. It is an input to #1468.
  - **Rows with no proof and no unit (X-11 R1 justification, X-21 physical return, X-71 C1 coupled).** These
    stay open and are stated as open.
  - **Step-2 rows (X-63 global phase, X-82 inflow).**
  - **The posit, its pointers and its declarations (X-00–X-02).** These are removed by the deletion edit.

## 2. The ledger

Column definitions are in PREREG §3.

- **Status vocabulary:**
  - `done`: no correction is needed before deletion except the pointer rewrites of the deletion edit;
  - `in progress`: an authorized Step-1 unit is running;
  - `queued`: Step 2 or #1468, not authorized;
  - `open`: no unit.
- **Site cell:** each row lists the sites the map assigns to it. S3 is counted by state:
  - `visible`: the qualification is printed at the site;
  - `per unit`: the owning Step-1 unit decides;
  - `not determined`: a Phase-3 site, for the Q3 census.
- **Codes:** `none`, `ptr` (rewritten in the deletion edit) and `unit` (corrected by the owning unit).
- **Lines with several rows:** a line carrying several rows is assigned to one primary row. The other rows
  list it after "also".

<!-- TABLE:BEGIN -->
| Id | Dependency (home at the pin) | Sources | How A1 enters | Disp. | Weaker condition (J) | Disguised A1? (S1) | Exit route | Correction | Sites and S3 (qualification visible?) | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-00 | Main posit ledger item (ii), total finiteness of the bijective representative, and the status Remark sentence that carries it (M:732 (ii); M:60) | REM-s3, R1, R2, R3, R5, R6 | The posit itself: "an open hypothesis, not adopted ... carried as one sufficient condition" | O | — | n/a (not J) | Deleted by the final-deletion unit once PREREG §6 holds; until then it stays printed as open and not adopted | M:732: delete item (ii)'s text; the ID (ii) is retired and not reused or annotated (§A.30). Its content moves to the status Remark M:60, which keeps (a) the per-result weaker sufficient conditions — (NR) for §2.3, (IP) for §3.2, (IL) for §4.6, (REV) for bijectivity, each "assumed as a hypothesis of that result and not adopted"; (b) the finite-representative list — the counting-measure selection of Lemma 3, the exact return and its index L, the orbit capacity, the CP-indivisibility theorem of §3.2, the physical-memory theorem of §3.4 and the canonical-typicality step of §4.6; (c) the deep-sector clauses as printed (gauge invariance of the cardinality of an independently prepared finite decoupled factor; coupled and infinite sectors outside that statement; the transfer across relabelling, finite decoupled enlargement and change of alphabet under the alphabet-size hypothesis, with its proof cited at its source). M:60: "Total finiteness of that representative is one sufficient condition for the results that use it, carried as item (ii) of the posit ledger (§4.5), the total-finiteness posit, an open hypothesis, not adopted;" → "The results that use that representative are statements about finite representatives;". M:60 (P8 hit): "The physical reading of the characterization theorem — the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice" → "The characterization theorem is a statement about finite-horizon laws and their finite representatives; it does not identify nature with a finite reversible substratum" | 2 sites (visible 2); codes ptr 2. M:60, M:732 | final deletion | queued (Step 2; needs PREREG §6) |
| X-01 | Pointers to the posit: item (ii), "the total-finiteness posit", "posit A1", "(ledger item (ii))" (M:36, :44, :111, :129, :224, :268, :594, :646, :708, :726; companion and book counterparts in the site map) | REM-s3 | Each sentence names the posit as the source of a finite hidden sector or of the finite model | O | — | n/a (not J) | Rewritten in the deletion edit (PREREG §6 item 4) | Each: replace the pointer by the scope it carries. M:36 "Total finiteness remains an open physical posit, not adopted, and one sufficient condition among those each result names (...item (ii))" → delete the sentence (the next sentences already state the per-result conditions). M:44, :111, :129, :224, :268 "under the total-finiteness posit (§1.2 Remark, §4.5 ledger)" → "on a finite representative". M:594 and ch01:163, ch19:126 "in its finite model (ledger item (ii))" → "in its finite model". M:646 "(b) the physically operative form under A1" → "(b) the form for a finite substratum". M:708: "Finiteness of the hidden sector is, in the forward construction, item (ii) of the posit ledger (§4.5), an open hypothesis, not adopted, and one sufficient condition among those stated at each use, with the deep-sector scope stated there; it is not derived from Lemma 1" → "Finiteness of the hidden sector is not assumed in the forward construction: results that use a finite hidden sector are statements about finite representatives, each naming the hypotheses it consumes; it is not derived from Lemma 1"; and "compatible with the finiteness hypothesized here and are not premises of it" → "compatible with finite representatives and are not premises of them". M:726 "finite under the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii)), an open hypothesis" → "finite in the finite representative, which is not asserted of nature" B1 pointers (readers-guide:79 = FULL:167, book/README.md:100, ch03:226 = FULL:1087, appC:110 = FULL:6265): "finiteness posit" → "finite-representative scope" (appC §C.6: the objection answered by that scope) | 65 sites (not determined 4, visible 61); codes ptr 61, unit 4. README:100, FULL:167, FULL:320, FULL:361, FULL:496, FULL:1087, FULL:5196, FULL:5282, FULL:5284, FULL:5286, FULL:5430, FULL:6171 … | final deletion | queued (Step 2; 4 Phase-3 sites via Q3) |
| X-02 | Declarations of A1 in companion papers, book and glossary (Substratum (A1), "finite under A1", "A1–A6", "posit A1", appendix C §C.6) (Sub:92; SM:30, :60; ch02:76; gloss:11; appC:96–116; and every "finite under A1" site) | C6, C9, FCLASS-U1 | States A1 or applies it to S | O | — | n/a (not J) | Rewritten in the deletion edit; Phase-3 files by Q3 propagation first | Sub:92 and ch02:76 / FULL mirror: delete the (A1) entry; Theorem 23 then states finiteness as part of its finite-substratum scope (X-45). "finite under A1" / "finite under the open hypothesis A1" → "finite in the finite representative" (where the sentence is about the model) or delete the parenthesis (where finiteness is not used). gloss:11: replace the A1 entry by "Finite representative: ... (finite-only scope; no claim that the substratum is finite)". appC §C.6: restate the objection as answered by the finite-only scope of the listed results | 25 sites (visible 25); codes ptr 25. FULL:638, FULL:706, FULL:766, FULL:788, FULL:842, FULL:945, FULL:1330, FULL:1338, FULL:1983, ch02:8, ch02:76, ch02:136 … | final deletion | queued (Step 2) |
| X-10 | Lemma 3 selection clause: the counting measure is the maximal-entropy invariant measure (M:54; M:58; M:732 (ii) scope list) | M1, S0:M1.a | A uniform probability exists only on a finite carrier; the maximum is over invariant laws relative to counting | F | — | n/a (not J) | Already printed as a statement about finite representatives (M:732 (ii) scope list, kept by X-00's re-homing). Kernel: `CanonicalMeasure.counting_maximal_entropy` (finite S) | none (M:54 states "globally, the counting measure is selected ... a selection principle"; finite scope carried by M:732 list). Book ch01:38, :81, :85 and FULL mirrors: none (Phase 1 dispositions N/B-units) | 19 sites (not determined 5, visible 14); codes none 14, unit 5. FULL:371, FULL:414, FULL:418, FULL:3872, FULL:4767, ch01:38, ch01:81, ch01:85, ch14:272, ch18:36, Comp:122, M:54 … | Q3 propagation | queued (5 Phase-3 sites; done in Main and Phase-1 book files) |
| X-11 | R1: physical justification of a selected law (posit (iv), μ-G; the canonical law's physical selection; P-ED (G3)+(G4)) (M:732 (iv); M:58) | R1, S0:M1.a, L1 | Selection over laws on the whole carrier; P-ED restates the uniform posit (R1-INF §7) | O | — | n/a (not J) | Open (owner safeguard 3: "R1's physical justification ... remain[s] open"). No unit; R1-L8 Stage 1(iv) deferred | none: M:732 (iv) prints the selection as "a standard but substantive epistemic postulate, not derived"; POSIT-MIN (iv) "WEAKEN to H-μ" is a proposal, not adopted | 3 sites (visible 3); codes none 3. SM:803, SM:809, SM:811; also M:732 (iv), M:58 | none | open |
| X-12 | μ-O and μ-R (uniform law on the actual orbit / on the record-compatible orbit union), their static budgets log₂(\|S\|/ℓ), log₂(\|S\|/\|U\|), and the orbit capacity log₂ p (M:60 ("As for the measure on a finite representative"); M:732 (iv)) | M2, M13, S0:M2.b, S0:M2.c | Uniqueness on a finite orbit; counting budgets | F | — | n/a (not J) | Owner decision #1169 c.7041456852 item 3: "(iii) Orbit and record laws (μ-O, μ-R) as finite-only statements ... Adopted as a scope restriction for existing results ... Any manuscript wording change needs its own correction unit" | M:60: none (prefixed "As for the measure on a finite representative"). M:732 (iv): add "on a finite representative" after "maximal entropy compatible with the observer's records" if the R1/R2 scoping unit finds the item read as a law on an infinite carrier. Reconstruction records (OA-1, PREP) are research records, not manuscript | no primary site; also M:60, M:732 (iv) | R1/R2 scoping | queued (Step 2) |
| X-13 | Record budget D(p₀,B‖ν_B) ≥ (N+1)(1 − h₂(ε)) and the no-autonomous-production results (PREP 1.1–1.4, 2.5–2.6 (research record); no manuscript site) | S0:M2.d | Reference u finite, or ν with H-ν | J | H-ν: ν invariant with ν_A = u_H ⊗ ν_{A∖H}, finite cone (PREP 2.6) | No: A finite cone, not a finite carrier; any normalized ν off the cone. Its use to exclude the inflow endpoint needs a reference fixed in advance (X-82) | Already proved under H-ν on a finite cone (PREP 2.6, paper) | none | no primary site | none | done |
| X-14 | Baseline transition matrices and rooted family under the uniform hidden prior (M:113; M:137–143; M:208–210) | M3 | T_ij = \|{h}\|/\|C_H\| counts a finite hidden set | J | Any normalized hidden prior shared by the roots, on a measurable carrier | No: Normalization only; no cardinality | Main already allows an arbitrary shared μ_H (M:135, :141); RIGID `ObservableRigidity.rootedFamily_productLaw` (Lean) | none | no primary site | none | done |
| X-15 | Doubly stochastic one-step and rooted maps; injectivity prong 1; non-permutation witness lemma (M:210; M:276–280; M:441–443; M:530; M:60 (prong 1)) | M3, S0:M3.a, S0:M3.b, S0:M3.c, L3 | Uniform law on a finite product carrier | J | (IP): φ preserves ν⊗ρ with ν uniform on the finite visible alphabet (M:280); window readouts under P-ED (R1-INF Lemma 8) | No: Uniform only on the finite visible factor; β_A on an infinite product satisfies it (R1-INF Lemma 8). STAGE0 R′ counts the uniform factor as a selected law: recorded, not A1 | Main §3.2 prints (IP) as a sufficient condition (M:280, Phase 1 E9; item (ii) list) | none for (IP) sites. M:441 "for the finite bijective model of §3.2 with its common uniform hidden prior" is a finite statement and stays | 10 sites (visible 10); codes none 10. FULL:5719, FULL:5721, FULL:5723, appb:42, appb:44, appb:46, M:210, M:276, M:278, M:280 | none | done (Phase 1) |
| X-16 | Theorem 19 reciprocity T_ij = T_θj,θi and detailed balance; Theorem 21 (SM:641; SM:651) | S0:M1.b, OA4:20, OA4:21 | Counting hidden prior and normalizer 1/\|H\| | F | — | n/a (not J) | Printed with "the hidden prior be the counting measure" (finite). An A1-free form exists in records (P6: Θ-invariant normalized law, equal root masses; `MeasuredReciprocity`, Lean) but owner Q4 (#1169 c.7035888700): "no new companion-paper claims" | none | 18 sites (per unit Q1 18); codes none 18. FULL:1220, FULL:1270, FULL:1510, FULL:1521, FULL:4927, FULL:5150, ch04:116, ch04:166, ch05:195, ch06:10, ch18:196, ch19:80 … | Q1 | in progress (Q1 may restate it on ℤ^d; the ℤ^d form for the selected linear update is degenerate, O-A4 §5) |
| X-17 | Proposition 4b custodial scalarity at \|λ\| > 1 (SM:334) | S0:M1.c, OA4:15 | Selected counting measure | J | H-blind / H-μ(sp): a law invariant under signed permutations (uniform product law on ℤ^d satisfies it, O-A4 Lemma U) | No: An invariance property of a normalized law; satisfied on an infinite carrier | SM:334 prints the extension clause (law equivariant under signed permutations) | none | no primary site | none | done |
| X-18 | Lemma 1c(ii) pole statement; Proposition 4b continued response; Theorem 5 kinetic H-cust clause (SM:252–254; SM:334–336) | S0:M1.d, OA4:10, OA4:11, OA4:12 | Determinant factorization on a finite carrier | F | — | n/a (not J) | Phase 2 S7/S8 (#1450) state (ii) on a finite carrier and fibrewise under translation invariance, with "On an infinite configuration space without that structure no determinant is available" (SM:254). The general infinite-carrier reading needs H-cont (O-A4 §6.1), open | none | no primary site; also SM:252, SM:254, SM:334, SM:336 | none | done (Phase 2) |
| X-20 | Recurrence-scale P-indivisibility from a non-permutation map (§2.3 theorem, Step 1 exact return) (M:113–131; M:72, :180, :182, :340, :634, :724) | M4, S0:M3.d, OA4:3 | Step 1: a bijection of a finite set has finite order N | J | (NR): a single common near-return with margin after the non-permutation time, any normalized root-shared prior, no invariance (M:131) | Relabel: Logically weaker than A1: RIGID's rotation × Bernoulli example satisfies it with no finite order. At an unspecified time it has no finite-window test (REMAINDER §3). For the selected update on ℤ^d, (NR) fails under β_A (NR-1 Prop. 2.3; P-divisible at every horizon, NR-1 Thm 3.3); the torus counting law μ_L on periodic configurations is the only law on main under which a return is exhibited (STAGE0 F1, a [W] reading within RIGID's rooted family) | Main §2.3 corollary (near-return), M:131, prints (NR) "assumed ... not adopted"; companions carry it (Phase 2 S1, G1, G2, B1). Deletion criterion 3 needs the Relabel qualification printed where (NR) is introduced | At M:131 (where (NR) is introduced), M:141 and M:224 (index-free form), M:180 and M:724 (restatements): add the Relabel qualification, e.g. "(NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update on ℤ^d a law satisfying it is not identified (X-21)". The same at the companion and book restatements carrying (NR) (Phase-2 units S1, G1, G2, B1). Exact wording by the scoping unit; Phase-3 restatements (Meth, ch18, FULL) and glossary:105 by Q3; Str:1224 and ch01:161 = FULL:494 (B1) qualified by the scoping unit | 80 sites (not determined 19, visible 61); codes none 66, ptr 2, unit 12. FULL:62, FULL:426, FULL:428, FULL:430, FULL:444, FULL:452, FULL:454, FULL:456, FULL:464, FULL:494, FULL:897, FULL:963 … | R1/R2 scoping | queued (Relabel qualification not printed; Q3 sites) |
| X-21 | A physical source of a return condition for the selected update (none (REMAINDER R2; STAGE0 F1; NR-1 open question 3)) | R2, L4 | Under β_A, (NR) fails for the selected update (NR-1) | O | — | n/a (not J) | Open; no unit | none: no manuscript asserts a physical return for the selected update on ℤ^d | no primary site; also none: no manuscript site asserts a physical return for the selected update | none | open |
| X-22 | History readback + finite recurrence theorem: exact endpoint Γ_L = I, bound s ≤ min(k, L−1) (M:137–141; GR:591) | M5, R2 | φ of finite order L | F | — | n/a (not J) | Printed for "a bijection ... of order L" on finite C_V × C_H: a finite-representative theorem. The A1-free part (histories meeting ⇒ some non-permutation Γ_s; REC-1 Prop 6.1) is in records only; priors with no invariant product law need L4 (open) | none | 4 sites (visible 4); codes none 4. FULL:6096, appb:419, M:137, M:139 | R1/R2 scoping | done (the statement is finite; R1/R2 scoping may add the REC-1 form) |
| X-23 | Index-free full-support equivalence: readback gap at some finite order ⇔ non-permutation Γ_s ⇔ not P-divisible on some horizon (M:141; M:224; M:80 item (2)) | M7, REC1-U15 | Exact return in the L-indexed proof | J | REC-1 Prop 6.2: (V), (M), (I), (P), (RIG), (FS); or (NR) | Relabel: As X-20 | Printed among measurable-H results (Phase 1 E15, amendment A-E15) | As X-20 at M:141 and M:224 | no primary site | R1/R2 scoping | queued (Relabel qualification not printed) |
| X-24 | L-indexed form: gap below L ⇔ non-permutation Γ_s with s < L ⇔ indivisible on {0,…,L}; "below the recurrence time" (M:18; M:80; M:141; M:741 (status table row)) | M7, R2, REC1-U11 | Exact return Γ_L = I and its index L | F | — | n/a (not J) | Each printed site names "one fixed finite reversible representative" or L (M:18, M:80, M:141) | none | 11 sites (not determined 3, visible 8); codes none 10, unit 1. FULL:436, FULL:6608, ch01:103, gloss:117, M:18, M:80, M:141, M:451, M:455, M:741, Med:25 | Q3 propagation | queued (1 Phase-3 site; done in Main) |
| X-25 | Routed readback "for some n"; write/store/read clauses (M:147) | M8 | `rootedMap_periodic` on finite carriers | F | — | n/a (not J) | As printed, a statement about finite rooted maps (§2.3 setting; the write/store/read clauses are formalized on finite carriers only, `PhysicalC4Discharge`, `PhysicalC4StorageReadback`). A J form (revival under (NR)/(RIG); RIGID `exists_reviving_return_of_overlap`) exists in records and would need a printed correction | none for the finite statement; if the scoping unit adopts the J form, add at M:147 that the revival holds under (NR) with the Relabel qualification of X-20 | 1 sites (visible 1); codes none 1. M:147 | R1/R2 scoping | queued (decide F as printed or J with a printed correction) |
| X-26 | All-time rooted classification and periodicity of a fixed realization; ch18 §18.7 "finite information and exact finite recurrence" (M:646; ch18:20, :162–192, :40; FULL mirrors) | M10, CEN18-ch18, OA4:3 | Finite order of a finite bijection | F | — | n/a (not J) | M:646 is stated for "a bijection on a finite set"; ch18 §18.7 is stated "under A1" | M:646 "(b) the physically operative form under A1" → see X-01. ch18 §18.7 and FULL mirror: Q3 restates as finite-only ("for a finite substratum") and removes "the hypothesis A1 of a finite substratum" as a framework hypothesis | 41 sites (not determined 38, visible 3); codes none 2, ptr 3, unit 36. FULL:512, FULL:4751, FULL:4893, FULL:4895, FULL:4897, FULL:4899, FULL:4901, FULL:4903, FULL:4905, FULL:4907, FULL:4909, FULL:4910 … | Q3 propagation | queued (Step 2) |
| X-27 | Orbit capacity log₂ p; genericity count P_perm over bijections of a finite set (M:60; M:149–153) | M13 | Finite orbit; uniform count over a finite set of bijections | F | — | n/a (not J) | Finite-model statements (P0 action N); also X-12 for the capacity | none | 2 sites (visible 2); codes none 2. M:149, M:153 | none | done |
| X-28 | Overlap-and-return theorem; C4r/C4e no-go (M:143) | M6 | Finiteness only in the setup | J | None needed: row-stochastic Γ_s on finite V (`CausalReadback.c4r_implies_pIndivisible`) | No: Finite visible data only (Lemma 1) | A1-free as stated (REMAINDER class (a)) | none | no primary site | none | done |
| X-29 | Substratum Stage 1 recurrence-cycle P-indivisibility on a finite representative (Sub:137) | OA4:3, C6 | Finite order of a permutation | F | — | n/a (not J) | Printed "on a finite representative"; (NR) added by Phase 2 for the conclusion | none | no primary site; also Sub:137 | none | done (Phase 2) |
| X-30 | Bijectivity of the representative: eventual image, injectivity ⇒ surjectivity, merge prong (M:60; M:732 (iii); Sub:94; Meth:146–148; ch01:41) | M11, R3 | Finite-set arguments | J | (REV): φ a bimeasurable bijection of a measurable carrier (M:732 (iii)) | No: A posit, not a lemma; same observational status as A2 under A1 (REMAINDER §3); implies no cardinality | Bijectivity is posited as (REV) (M:732 (iii)), not recovered: the eventual-image and injectivity-to-surjectivity recovery stays a finite statement ("on a finite representative φ is a bijection", M:60) | none in Main; Meth:146–148 by Q3 | 8 sites (not determined 3, visible 5); codes none 5, unit 3. FULL:374, FULL:708, ch01:41, ch02:78, Meth:106, Meth:146, Meth:148, Sub:94 | Q3 propagation | queued (3 Phase-3 sites; done in Main) |
| X-31 | §3.2 representation on a finite hidden space (M:268–290) | M12, S0:M3.e | Finite H as the setup | J | None: construction per finite-horizon law | No: Constructed finite witness, not an assumption on nature | Finite hidden spaces are constructed per law (S ⇒ D, `Equivalence.S_imp_D`); the representation is A1-free | M:268 pointer → X-01 | no primary site | none | done |
| X-32 | Characterization window t ≪ t_R (M:542) | M14 | t_R of a realizing substrate | J | None | No: A1-free | Restriction removed (MAIN-TR-1); the proof never consumes t_R | none | no primary site | none | done |
| X-33 | C3 capacity bound log₂\|C_H\| ≥ I* (M:518–520) | M15 | Counts the hidden states of a realization | J | None (finite realizations by definition) | No: A1-free as stated | Holds for every finite realization; class D is finite by definition | none | no primary site | none | done |
| X-34 | Coupling-graph causal cone; Bell ceiling (M:364; M:416–418) | M17 | Finite V in the first step of the finite-site proof | J | Finite read sets (posit (xiii)) | No: Local finiteness only | Arbitrary-site form with finite read sets printed in the same paragraph | none | no primary site | none | done |
| X-40 | A4's finite periodic lattice clause (finite quotient + finite alphabet ⇒ A1 via `a1_of_finite`) (Sub:98; ch02:82; SM:202; ch05:65; FULL mirrors) | C6, C7, R4, OA4:1, O-A4 | The printed class is finite; `SubstratumInterfaceAudit.a1_of_finite`:109 | O | — | n/a (not J) | Q1, in progress, under the Owner A4 formulation (#1169 c.7048255658): ℤ^d is the standard construction wherever the proofs support it; finite periodic lattices are explicitly qualified cases with the wrapping conditions they need (Q1); finite lattices are not called approximations of ℤ^d unless an approximation or convergence result is established; the infinite discrete lattice and infinite continuous space are kept distinct. This replaces the (α)/(β) choice of the Q1 record. Kernel support for the standard construction: `A4`:98 on an arbitrary additive group; LEAN-2(i) A2–A5 at ZMod 0 = ℤ. Not marked J in advance (safeguard 2) | Per Q1: Sub:98 "a finite periodic lattice, the quotient of a rank-d lattice by a finite-index sublattice" → the coupling graph is ℤ^d (the standard construction) where Stage 2 is proved there, with finite periodic quotients admitted as qualified cases under their stated wrapping conditions (X-42); mirrors ch02:82, FULL:712, SM:202, ch05:65, FULL:1380 | 8 sites (per unit Q1 8); codes unit 8. FULL:712, FULL:1380, FULL:5268, ch02:82, ch05:65, ch19:198, SM:202, Sub:98 | Q1 | in progress |
| X-41 | Stage 2 chain under A4∞ (O-A4 verdict (i)): area-law lemma, Lemma 1c(i), (iii), Corollaries 1a, 1b, the d = 3 selection corollary SM:210 (SM:122, :202, :210, :252, :258, :270; Sub:157) | C7, OA4:5, OA4:6, OA4:10, OA4:12 | Inherits A4's finite lattice | O | — | n/a (not J) | Q1, in progress: stated on ℤ^d where O-A4 verdict (i) and Q1 support it; otherwise a qualified finite-lattice case (owner A4 formulation, #1169 c.7048255658) | Per Q1 outcome | 19 sites (per unit Q1 11, visible 8); codes ptr 8, unit 11. FULL:726, FULL:1340, FULL:1388, FULL:1392, FULL:1398, FULL:1404, ch02:96, ch05:25, ch05:73, ch05:77, ch05:83, ch05:89 … | Q1 | in progress |
| X-42 | Period-lattice conditions on the printed finite class: O_h needs O_h-invariant Λ; checkerboard needs even-sum periods; eight corners need Λ ⊂ 2ℤ³; SM:539 spin–taste; SM:1536 (SM:539; SM:1536; SM:242–374 (O_h uses)) | OA4:16, OA4:18 | Finite quotients that fail Stage-2 inputs (O-A4 §7) | O | — | n/a (not J) | Q1, in progress: each finite periodic lattice is a qualified case carrying its wrapping conditions (O_h-invariant Λ; even-sum periods for the checkerboard; Λ ⊂ 2ℤ³ for the eight corners) (owner A4 formulation, #1169 c.7048255658) | Per Q1 outcome (SM:539 already names the odd-torus failure; SM:1536 "bipartite checkerboard structure" unqualified) | 2 sites (per unit Q1 2); codes unit 2. SM:539, SM:1536; also ch05:160, ch06:58, FULL:1475, FULL:1569 | Q1 | in progress |
| X-43 | Fermion theorems on ℤ^d: Theorems 2, 3, 8, 8b, 10, 12, 13 (SM:286–302; SM:434–456; SM:535–547) | OA4:18 | Staggered phases, Brillouin corners, checkerboard | O | — | n/a (not J) | Q1, in progress: stated on ℤ^d where O-A4 verdict (i) and Q1 support it; otherwise a qualified finite-lattice case (owner A4 formulation, #1169 c.7048255658) | Per Q1 outcome | 7 sites (per unit Q1 7); codes unit 7. SM:286, SM:302, SM:434, SM:440, SM:456, SM:535, SM:543; also ch05:152, ch06:22, ch06:26, appB:378, FULL:1467, FULL:1533, FULL:1537, FULL:6055 | Q1 | in progress |
| X-44 | Theorem 1a "Let S be finite" (RESOLVED); SM:222 carrier; SM:250 attribution (SM:242; SM:222; SM:250) | OA4:9, P2-F5 | Hypothesis stated; O-A4 §9a: unused by the proof | J | None: no hypothesis on S. The proof is ring algebra on the observable space (P + Q = I, linearity of U, commutation with R_g); the existing Lean MZ (verification/lean/OI_Structural_Core.lean) covers infinite S | No: No condition replaces the deleted one; the theorem holds for any set S | RESOLVED by Q2: PR #1464 merged at head eee291d9, merge commit fbca1df98f630aa0dd334c6e7f9f9a193da64394; owner decision record #1169 c.7048183824 (amaybaum, 2026-11-20T19:04:33Z); recovery record verification/audits/foundations/a1exit-q2-20261120/RECOVERY.md (on main) | done on main at fbca1df9 (the ledger's pin): SM:242 "Let $S$ be a set,"; SM:250 attribution "a deterministic bijection". Pre-existing stale coverage-ledger entry verification/coverage/LEDGER.json:1494–1495 routed to #1462 as PF-6 | 1 sites (per unit Q2 1); codes none 1. SM:242 | Q2 | done (Q2 merged, fbca1df9) |
| X-45 | Theorem 23 (reconstruction) under E1–E7 and A1–A6; its uniqueness "within the class A1–A6" (Sub:104–133; Sub:189–195; Sub:205–233; ch02:88–122; ch04:10–26; ch05:19; Str:768; gloss:13) | C6, OA4:26, R4 | A1 listed among the hypotheses; Stage 2 uses A4's finite lattice; Stage 3 H-count (X-70); Stage 1 exact return (X-29) | F | — | n/a (not J) | With A1 deleted and A4 in the owner's size-independent formulation: Stage 2 on ℤ^d where Q1 supports it, finite substrata as qualified cases. The theorem as a whole stays a statement about finite substrata satisfying A2–A6 until Stage 3 (X-70, X-71) and Stage 1 (X-29, X-21) have size-independent forms | Sub:104 and mirrors: "under E1–E7 and A1–A6 jointly" → "for a finite substratum — A4's finite periodic lattice, a qualified case with Q1's wrapping conditions — satisfying E1–E7 and A2–A6"; "the structural class A1–A6" → "the class of such finite substrata"; ch02:122 "(violating A1)" → "(outside the finite class)". Where Q1 establishes Stage 2 on ℤ^d, that stage is stated there as the standard construction | 39 sites (not determined 5, visible 34); codes none 6, ptr 28, unit 5. FULL:718, FULL:720, FULL:748, FULL:752, FULL:1114, FULL:1130, FULL:1334, FULL:6504, ch02:88, ch02:90, ch02:118, ch02:122 … | final deletion | queued (Step 2; after Q1; 5 Phase-3 sites via Q3) |
| X-46 | OI-class substrata "satisfying A1–A6" (Structure Definition 9.9, Proposition 9.5 and dependent statements) (Str:646 and the R6/C11 sites of Structure) | C11 | Class definition | F | — | n/a (not J) | A definitional finite class; narrowing to A2–A6 plus the M4/M18 posits would be a definition change (REMAINDER C11) and is not proposed here | At deletion: "OI-class substrata (satisfying A1–A6)" → "finite OI-class substrata (finite, A4 in its finite periodic qualified case with Q1's wrapping conditions, satisfying A2–A6)" | 57 sites (visible 57); codes none 2, ptr 55. FULL:895, FULL:905, FULL:2433, FULL:2451, FULL:2521, FULL:2597, FULL:2603, FULL:2607, ch03:34, ch03:44, ch09:18, ch09:36 … | final deletion | queued (Step 2) |
| X-47 | Finite-L lattice numerics and the A·B extrapolation family: finite-L Monte Carlo (L = 16–64), L → ∞ extrapolations (Z_S, m_b/m_τ), matching-scale checks; SM:801 a negative finite-L phase result; SM:645 = ch06:62 a finite-torus substratum check (SM:14, :645, :711, :713, :751, :783, :801, :813, :817, :1138–1144, :1261, :1267, :1300, :1302, :1656; appA:30, :85, :217; ch06:62, :94, :208; ch19:152; ch04:48; appC:273; FULL mirrors) | A4-OWNER | Values computed on finite periodic lattices are compared with observation or extrapolated to L → ∞ numerically. Except SM:645 = ch06:62, these are emergent lattice-gauge regulator lattices (Haar / staggered HMC, SM:813), distinct from A4's substratum lattice | O | — | n/a (not J) | Not an A4 consumer: these lattices regulate the emergent gauge theory. The owner rule (#1169 c.7048255658) that a finite lattice is not an approximation of ℤ^d without an established convergence result is applied by analogy: a numerical L → ∞ extrapolation is numerical evidence, not such a result. SM:801 is a negative finite-L phase result (confinement of the purely induced theory). SM:645 = ch06:62 checks Theorem 19 on finite tori (X-16) and is stated with its L values. Input to the regression audit (#1468) | Per the regression audit: each value stated as a finite-L computation with its extrapolation as numerical evidence, unless a convergence result is cited. Cheap probe at the pin: no sentence in papers/ or book/ calls a finite lattice an approximation of ℤ^d | 35 sites (not determined 35); codes unit 35. FULL:1152, FULL:1573, FULL:1605, FULL:1719, FULL:5222, FULL:5477, FULL:5532, FULL:5664, FULL:6428, appa:30, appa:85, appa:217 … | regression audit (#1468) | queued (#1468) |
| X-48 | Classical-dimension obstruction family: no fixed finite carrier (N < ∞ ontic configurations) reproduces the exact continuum operational theory of a qubit; the framework's reading that it "does not require an ontically infinite carrier" (M:358; M:564 (Proposition); M:568; M:588; M:606; M:780; Sub:533; ch04:146 = FULL mirror; Intro:135) | B1-CDO | The theorem is stated for one realization with N < ∞; the framework reading (M:780, Sub:533, ch04:146) places the continuum endpoint beyond every fixed finite carrier | F | — | n/a (not J) | The theorem is a true statement about finite carriers (Proposition M:564; [55]) and stays as such. Its framework reading depends on the carrier's size: on an infinite carrier the obstruction does not apply, so with A1 deleted the sentences that use it to describe OI (M:358, :568, :588, :780; Sub:533; ch04:146; Intro:135) must state that scope. Input to the regression audit (#1468) | Per the regression audit: keep the Proposition; at each framework-reading site state "for a fixed finite carrier" where the sentence speaks of OI's substratum, and do not convert the obstruction into a claim about an unspecified-size substratum | 10 sites (not determined 3, visible 7); codes unit 10. FULL:1250, ch04:146, Intro:135, M:358, M:564, M:568, M:588, M:606, M:780, Sub:533 | regression audit (#1468) | queued (#1468) |
| X-50 | CP-indivisibility theorem (permutation-dilation family) (M:332–336) | M9, L6, R6 | Permutation unitary on finite H | F | — | n/a (not J) | Printed as a finite-representative statement (M:732 (ii) list). R6 lemma L6 (Koopman dilation on ℂ^V ⊗ L²(H,ρ)), in progress, may supply J or confirm the finite-only restriction | none at the pin; per R6 outcome | 4 sites (per unit R6 4); codes none 4. FULL:5769, appb:92, M:332, M:336 | R6 | in progress |
| X-51 | Physical-memory theorem and C2 quantitative form (M:459–475) | M16, L7 | Uniform-prior finite coupling model | F | — | n/a (not J) | Printed as a finite-representative statement (M:732 (ii) list). R6 lemma L7, in progress | none at the pin; per R6 outcome | 2 sites (per unit R6 2); codes none 2. M:459, M:473 | R6 | in progress |
| X-52 | Deep-sector cardinality as gauge, finite windows; Theorem 24(i) population law, (ii), (iii) trace-class identity; GR Appendix B (GR:132–138; GR:871–905; Sub:251–264; M:732 (ii) transfer clause) | M21, C3, C8, OA4:23, OA4:24, OA4:25 | Finite decoupled factor; uniform ω_H | J | (D1)–(D5), with (D5) μ_H = u_{B_n}⊗ν, ν any normalized law (GR:877–883); for Theorem 24(iii), a trace-class state σ_A and a unitary W on the adjoined factor, with the base channel on V × H already defined as a channel (O-A4 row 24) | No: Finite cone and a uniform factor on a finite boundary window; the deep law is of any cardinality | GR Appendix B printed for a site set of any cardinality under (D1)–(D5) | none | 15 sites (visible 15); codes none 15. FULL:5867, FULL:5871, appb:190, appb:194, GR:132, GR:134, GR:136, GR:138, GR:875, GR:883, GR:885, GR:889 … | none | done |
| X-53 | All-time coherent-channel invariance under an infinite normalized decoupled factor; transfer of recurrence-scale content (Theorem 24(i) coherent form, Corollary (iii)) (Sub:262; Sub:268 (iii); ch02:144) | M21, C8, L9, OA4:23 | Finite factor A; uniform ω_H | F | — | n/a (not J) | Printed finite ("This is a finite, fixed-interface result; an infinite extension ... is not established", Sub:262). R6 lemma L9, in progress | none at the pin; per R6 outcome | 4 sites (per unit R6 3, visible 1); codes none 3, ptr 1. FULL:774, ch02:144, Sub:262, Sub:268 | R6 | in progress |
| X-54 | Storage and memory: "S finite capacity (under A1)" (Sub:44; ch02:14–18) | C9 | Explicit | F | — | n/a (not J) | Interpretive; no theorem rests on it (A1-09 §23.2) | At deletion: "finite capacity (under A1)" → "finite capacity in a finite representative" | 10 sites (visible 10); codes none 6, ptr 4. FULL:644, FULL:646, FULL:648, FULL:662, ch02:14, ch02:16, ch02:18, ch02:32, Sub:44, Sub:52 | final deletion | queued (Step 2) |
| X-55 | Computation: finite-carrier capacity comparison; "the framework's finiteness hypothesis (A1)" (Comp:120, :122, :178, :182; ch14:160–272; FULL mirrors) | C12 | A1 by statement | F | — | n/a (not J) | Phase 3 (Q3): restate as conditional statements about finite substrata | Q3 per site; Comp:182 "The framework's finiteness hypothesis (A1)" → "A finite substratum" | 10 sites (not determined 10); codes unit 10. FULL:3760, FULL:3764, FULL:3784, FULL:3862, ch14:160, ch14:164, ch14:184, ch14:262, Comp:178, Comp:182 | Q3 propagation | queued (Step 2) |
| X-56 | Exact linear rule shell splitting into cycles as motivation for (EM) (M:732 (v); M:766 (ii); SM §4.2) | C14 | Cycle counts on a finite lattice | F | — | n/a (not J) | M:766 states the cycle structure does not settle (EM) | none | no primary site; also M:732 (v), M:766 (ii) | none | done |
| X-57 | Appendix A finite sectors; Page value as exact cycle average on a finite configuration space (GR:609; GR:719; GR Thm A.8) | REC1-U12, CEN17-GR-729/753, FCLASS-U1 | Finite configuration spaces | F | — | n/a (not J) | Printed as finite-model statements (Phase 2 N) | none | 2 sites (visible 2); codes none 2. GR:609, GR:719 | none | done |
| X-60 | §4.6 theorem: the decay estimate for the iterated compression (operator step) under (IL) (M:752–760; M:766 (IL)) | M18, S0:M19.b, T1 | Counting inner product; finite S in the Setup | J | (IL): normalized φ-invariant μ, P the μ-conditional expectation onto declared local observables of a finite readout support, (EM) on μ-centred L²(μ) observables | No: A normalized law with a finite readout support; τ_B transfer is an A1-independent source gap (REMAINDER M18) | M:766 prints (IL) as a hypothesis of the decay estimate (Phase 1 E14). The O(ε) corrections and exact recurrence are X-65 | none | 5 sites (visible 5); codes none 5. M:750, M:752, M:758, M:760, M:766 | none | done |
| X-61 | Anti-Boltzmann-brain corollary (M:762) | M20, S0:M19.b | Inherits M18's setting | J | As X-60 | No: As X-60 | Operator step as X-60 (J); its O(ε) and finite-representative parts are X-65 (F); local equilibrium enters as a definition | none | 2 sites (visible 2); codes none 2. M:165, M:762 | none | done |
| X-62 | Typicality step: equilibrium macrostate ⇒ local equilibrium via canonical typicality [31] (M:764) | M19, R5, S0:M19.a, T6, O1(a) | [31] is a finite-dimensional shell theorem; M:764 dropped its typical-state quantifier | F | — | n/a (not J) | Main:764 unit (PR #1463, in progress): restores [31]'s typical-state and fixed-subsystem form and states G1 (configuration microstates outside the typical set; ensemble reading = the shell law's marginal). Then a finite-representative statement, listed as such at M:732 (ii) and M:766. The global-to-local inference for laws on an infinite carrier (L8-sel) needs R1: open, carried by X-63 | M:764: replace "canonical typicality [31] implies every local subsystem is also in its local equilibrium." by the typical-state, fixed-subsystem statement with G1 (exact text in PR #1463 LEDGER) | 1 sites (per unit Main:764 1); codes none 1. M:764 | Main:764 | in progress |
| X-63 | The twelve global-phase claims: "observers exist only in the non-equilibrium phase of (S, φ)", the §4.6 heading, the past-hypothesis replacement and their restatements (M:748 (T22); M:764 (T6, T7b); Sub:56 (T11b, T11c); Sub:401 (T12); Sub:542 (T14); Str:718 (T15); Str:734 (T16); Comp:212 (T17b); ch02:192 = FULL:822 (T18); ch04:178 = FULL:1282 (T20b)) | T6, T7b, T11b, T11c, T12, T14, T15, T16, T17b, T18, T20b, T22, C10, R5 | Global-to-local step T6 (A1 + [31]); and, by G3, no phase-discriminating statement in the iterated description | O | — | n/a (not J) | Step 2 decision (queued, not authorized). Strongest result that does follow: the region-level form W* (STAGE1ii §6), J under fast (EM) on declared regions | Each site: restate as W* ("(C2-slow) observers occur only outside regions whose effective channel satisfies (EM) at τ_mix ≪ τ_S, in the iterated description") or mark the phase statement open; the past-hypothesis replacement (Sub:56, Comp:212) marked open (O-INFLOW, X-82). Exact wording is the Step-2 unit's | 17 sites (not determined 2, per unit Step-2 phase 15); codes unit 17. FULL:822, FULL:919, FULL:1140, FULL:1282, ch02:192, ch03:58, ch04:36, ch04:178, M:748, Meth:283, Meth:441, Str:718 …; also M:764 (T6, T7b; the line is mapped to X-62) | Step-2 phase | queued (Step 2) |
| X-64 | RETAINED-WITH-(LE) rows: the thermal "in particular" clause, the proof's division of labour, the scope lists naming [31] (M:758 (T2); M:760 (T3); M:766 (T8); M:664 (T23); M:732 (T24a)) | T2, T3, T8, T23, T24a | [31] on the finite representative | F | — | n/a (not J) | As printed, statements about the finite representative (M:766 "the canonical-typicality clause ... are statements about the finite representative"). STAGE1ii: each also holds with a declared (LE) in place of [31]; that restatement is optional and Step-2 scoped | none required for A1 exit | 1 sites (visible 1); codes none 1. M:664; also M:664, M:732, M:758, M:760, M:766 | none | done |
| X-65 | §4.6 finite-representative parts: the O(ε) typical-set and finite-size corrections, and the exact recurrence of the Koopman operator of a finite permutation (Setup) (M:752; M:758 (ε); M:766) | M18, M20, S0:M19.b | Finite S in the Setup; ε defined on the finite representative | F | — | n/a (not J) | M:766 states these are "statements about the finite representative" (Phase 1 E14) | none | no primary site; also M:752, M:758, M:766 (lines mapped to X-60) | none | done |
| X-70 | H-count: classical horizon temperature as a counting derivative, decoupled case (GR:58; GR:88; ch07:42; Sub:175–185 (Stage 3)) | C1, S0:C1.a, OA4:22 | "Under A1, restrict the finite total system to a conserved energy shell" | F | — | n/a (not J) | Printed conditional on A1 (owner: "GR:58 counting stays conditional", Phase 2 CTL-15). With A1 deleted it reads as a statement about a finite total system. An A1-free decoupled form exists in records only (P7B Theorem under H1–H14; owner Q4: no new companion claims) | At deletion: GR:58 "Under A1, restrict the finite total system" → "For a finite total system, restrict it"; "that the total system is finite (A1)" → "that the total system is finite"; same at GR:88, ch07:42 | 3 sites (visible 3); codes ptr 3. FULL:1907, ch07:42, GR:58 | final deletion | queued (Step 2) |
| X-71 | C1 coupled shell law: existence of a normalized invariant shell law for coupled bijections (GR:58 (coupled case); P7B 6.3) | C1, S0:C1.a | No normalized invariant shell law for some coupled bijections (P7B 6.3 (ii)) | O | — | n/a (not J) | Open (owner safeguard 3: "C1 (coupled shell law) remain[s] open"); R1-L8 Stage 1(iv) deferred | none: GR:58 is stated for a finite total system with the boundary interaction negligible at the shell scale; no claim for the coupled case is printed, so there is nothing to qualify | no primary site; also GR:58 | none | open |
| X-72 | Calibration ħ = c³ε²/(4Gσ), the 1/4, ρ_s = ρ_crit, the 2/(d−1) concordance, a₀ chain (GR:78–88; GR:316–318; GR:422–440; GR:466–500; SM:182–196; Sub:88, :157; appB:169; ch05:59–60; FULL mirrors) | C2, S0:C1.b, S0:C1.c, S0:C1.d, S0:C1.e | Inherits H-count (X-70) | F | — | n/a (not J) | STAGE1i and PROV-CORR (#1458, #1459): the surviving normalization is Clausius; the law-dependent outputs (ħ coefficient, ε, N_modes, the count's equality with A/4l_p²) are unobservable and stated as calibrations; ρ_s and the concordance are identities of the GR inputs; a₀ and Tully–Fisher are imported | none beyond X-70's pointer rewrite | 1 sites (visible 1); codes ptr 1. GR:88; also GR:78–88, GR:316–318, GR:422–440, GR:466–500, SM:182–196, Sub:88, Sub:157, appB:169, ch05:59–60, ch02:68, ch19:116, appA:117, FULL mirrors of the chapter lines | none | done (PROV-CORR, PROV-CORR-2) |
| X-73 | H-BD and the boundary-only lemma (b) with gauge corollary (GR:112–128; Sub:92 (H-BD sentence); appB:177–194; ch02:44; ch07:46) | C4, S0:C4.a, L10 | Counting on finite C_D with injectivity (GR:126) | F | — | n/a (not J) | Printed with its counting condition (Phase 2 N: "measure condition stated"). L10 (measure-theoretic H-BD with the fibrewise non-expansion of STAGE0 F2) is open; no unit | none | 5 sites (visible 5); codes none 5. GR:112, GR:122, GR:124, GR:126, GR:128 | none | done |
| X-74 | Effective finiteness: E3 bounds \|C_V × C_B\| ≤ e^{S∂}; "the interpretive premise of A1" (Sub:268 (i), (ii); Sub:54; Sub:92) | C4, S0:C4.b | Reading of E3 as the premise of A1 | F | — | n/a (not J) | A bound on the observationally relevant space under H-BD; not finiteness of every sector (Sub:92 says so) | At deletion: Sub:268 (i) "This reading is the interpretive premise of A1." → delete the sentence | no primary site; also Sub:54, Sub:92, Sub:268 | final deletion | queued (Step 2) |
| X-75 | Operational completion, OI⁺, typed and quasilocal identifications; forward local gauge algebra (GR:239–282; A1-11) | C5, C13 | Finite carriers of the operational theory | J | None (finite operational carriers; arbitrary site set with finite local stages) | No: A1-free | A1-free as stated (REMAINDER class (a)); "under A1" at GR:257 is a pointer (X-02) | GR:257 "The concrete OI substratum under A1" → "The concrete OI substratum in its finite model" | no primary site | final deletion | queued (Step 2) |
| X-80 | FCLASS U1 interpretive uses: cosmic topology, consciousness, Page curve, "one way to realize A1 in a model" (ch18:240–288; FULL mirrors; ch19:212–216, :360) | FCLASS-U1 | Statements about realizing or assuming A1 | F | — | n/a (not J) | Phase 3 (Q3) for ch18; ch19 by the deletion edit | Q3 per site; ch19 pointers → X-02 rule | 8 sites (not determined 8); codes unit 8. FULL:4973, FULL:4975, FULL:4991, FULL:5019, ch18:242, ch18:244, ch18:260, ch18:288 | Q3 propagation | queued (Step 2) |
| X-81 | Lean: kernel predicate `SubstratumInterfaceAudit.A1` (Finite Conf) and theorems stated with it (verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:84, :109, :185, :786; WaveSubstratumUnbounded.lean:70; HexLatticeGas.lean:312; A6Instantiation.lean:278, :515; ManuscriptAxioms.lean:76) | CK8 | Finiteness predicate on finite carriers | F | — | n/a (not J) | Kernel statements about finite carriers are finite-only by construction; `waveZ_not_A1` and the A2–A5 predicates at ZMod 0 (LEAN-2(i)) are the infinite controls. No Lean change is needed for the deletion; manuscripts citing these read them as finite-only | none | no primary site; also Lean only (no manuscript site states the predicate) | none | done |
| X-82 | O-INFLOW: finiteness excludes the incoming-stream endpoint; dropping A1 admits it (Sub:56; Cx:212; ch18:40; FULL mirror) | INFLOW, R1 | PREP 1.5(d): the endpoint survives only without A1 | O | — | n/a (not J) | Open obligation (REMAINDER §5, #866); a budget exclusion inherits R1. No unit | Q3 (Cx:212, ch18:40) and Step 2 (Sub:56): state the inflow question as open where the sentence relies on finiteness to exclude it | 3 sites (not determined 3); codes unit 3. FULL:4771, ch18:40, Cx:212; also Sub:56 (mapped to X-63) | Step-2 phase | queued (Step 2) |
<!-- TABLE:END -->

## 3. Safeguard checks

### 3.1 S1 — no disguised A1 (safeguard 1)

Every J row was checked to see whether its weaker condition implies total finiteness or reproduces A1
under another name. None does: no J row has S1 = `Yes` (CK5), and the self-test shows that one `Yes` fails
the check.

- **`No` (15 rows).** The conditions are of these kinds:
  - normalization of a law on a measurable carrier (X-14);
  - finite visible or finite cone data:
    - (IP) uniform on the finite visible factor (X-15);
    - H-ν (X-13);
    - (IL) with a finite readout support (X-60, X-61);
    - (D1)–(D5) with a deep law of any cardinality, and a trace-class state with a defined base channel
      for Theorem 24(iii) (X-52);
    - finite read sets (X-34);
  - invariance properties of a normalized law (X-17);
  - (REV), posited, not recovered (X-30);
  - constructions per finite law (X-31);
  - A1-free as stated (X-28, X-32, X-33, X-75);
  - no condition at all (X-44, Theorem 1a for any set S).

  For each, a model on an infinite carrier satisfies the condition, as cited in the row.
- **`Relabel` (2 rows: X-20, X-23).** The condition is (NR), (RIG) or compact orbit closure.
  - It is logically weaker than A1: RIGID's rotation × Bernoulli example satisfies it with no finite order.
  - At an unspecified time it has no finite-window test (REMAINDER §3).
  - For the selected update on ℤ^d, (NR) fails under β_A (NR-1 Prop. 2.3; P-divisible at every horizon,
    NR-1 Thm 3.3).
  - The torus counting law μ_L on periodic configurations is the only law on `main` under which a return
    is exhibited. This is STAGE0 F1, a [W] reading within RIGID's rooted family.
  - Main does not yet state this qualification where (NR) is introduced, so both rows are queued with a
    printed correction (deletion criterion 3). X-21 records the physical source of a return as open.
- **Finiteness that would re-enter under another name.**
  - X-40: A4's finite periodic lattice with a finite alphabet implies A1 (`a1_of_finite`), so X-40 gates
    the deletion through Q1 under the owner's size-independent A4 formulation.
  - X-12: μ-O and μ-R are finite-only by owner decision, not weaker conditions.
  - X-48: the classical-dimension obstruction is a finite-carrier theorem. Its framework reading must not
    become a claim about a substratum of unspecified size.

### 3.2 S3 — no silent promotion (safeguard 3)

The counts by state are in each row's site cell and in the summary.

- **Visible.** Most mapped sites already state A1, a finite representative, a finite model or a named
  hypothesis. That includes the `ptr` sites, which state the hypothesis by name and must be rewritten
  when the name is deleted.
- **Not determined.** These are the 77 Phase-3 sites plus glossary:105, ch18:188 (with its FULL mirror) and Med:35 (81 sites), owned by Q3
  propagation (§4).
- **Per unit.** Q1, R6, Main:764, the R1/R2 scoping unit, the Step-2 phase unit and the regression audit
  (#1468) decide these sites.
- **SM:803 (N12).** It states the pushforward of the uniform measure without qualification. Its status
  is printed two paragraphs later (SM:809, "a load-bearing commitment"). The review decides whether that
  suffices.
- **R1 and C1 (X-11, X-71).** These are O rows, and the missing premises are named: M:732 (iv) "not
  derived"; GR:58 is stated for a finite total system with negligible boundary interaction and claims no
  coupled-case result. This meets the owner's condition that they "may stay open, provided the papers name
  the missing premises and claim no unconditional results".

## 4. The 77 Phase-3 sites (and glossary:105, ch18:188 with its FULL mirror, Med:35), owner Q3 propagation

These are the out-of-scope sites of A1-PHASE2 §2 and #1454 P2-Q3, plus the three lines added here. Each
line below is a pin line number with its ledger row.

<!-- PHASE3:BEGIN -->
- **Comp** (4): 120 (X-01), 122 (X-10), 178 (X-55), 182 (X-55)
- **Cx** (1): 212 (X-82)
- **FULL** (29): 3760 (X-55), 3764 (X-55), 3784 (X-55), 3862 (X-55), 3872 (X-10), 4751 (X-26), 4767 (X-10), 4771 (X-82), 4893 (X-26), 4895 (X-26), 4897 (X-26), 4899 (X-26), 4901 (X-26), 4903 (X-26), 4905 (X-26), 4907 (X-26), 4909 (X-26), 4910 (X-26), 4911 (X-26), 4914 (X-26), 4915 (X-26), 4917 (X-26), 4919 (X-26), 4921 (X-26), 4923 (X-26), 4973 (X-80), 4975 (X-80), 4991 (X-80), 5019 (X-80)
- **Intro** (2): 12 (X-20), 93 (X-20)
- **Med** (2): 25 (X-24), 35 (X-20)
- **Meth** (13): 106 (X-30), 146 (X-30), 148 (X-30), 156 (X-01), 158 (X-01), 283 (X-63), 339 (X-45), 345 (X-45), 357 (X-45), 367 (X-45), 369 (X-45), 441 (X-63), 517 (X-01)
- **ch14** (5): 160 (X-55), 164 (X-55), 184 (X-55), 262 (X-55), 272 (X-10)
- **ch18** (24): 20 (X-26), 36 (X-10), 40 (X-82), 162 (X-26), 164 (X-26), 166 (X-26), 168 (X-26), 170 (X-26), 172 (X-26), 174 (X-26), 176 (X-26), 178 (X-26), 179 (X-26), 180 (X-26), 183 (X-26), 184 (X-26), 186 (X-26), 188 (X-26), 190 (X-26), 192 (X-26), 242 (X-80), 244 (X-80), 260 (X-80), 288 (X-80)
- **gloss** (1): 105 (X-20)
<!-- PHASE3:END -->

## 5. Item (ii) and every pointer to it (`ptr` sites)

Item (ii) is X-00 (M:732, M:60). Every site below names A1, "total finiteness", "the total-finiteness
posit", "the finiteness posit", "posit (ii)" or "ledger item (ii)" in the sense of the posit. These are the
P0 core patterns P1, P2 and P5, plus the review's B1 "finiteness posit" lines. The anomaly conditions
"(A1)" at appB:235 and :246 are false positives. Each site is rewritten in the deletion edit by the rule
of its row:

- **F row:** the pointer becomes the finite-only scope ("for a finite substratum", "on a finite
  representative", "in its finite model").
- **J row:** the pointer becomes the weaker condition.
- **O row:** the pointer becomes the open statement.

<!-- PTR:BEGIN -->
- **FULL** (54): 167 (X-01), 320 (X-01), 361 (X-01), 496 (X-01), 512 (X-26), 638 (X-02), 646 (X-54), 706 (X-02), 718 (X-45), 720 (X-45), 748 (X-45), 752 (X-45), 766 (X-02), 788 (X-02), 842 (X-02), 895 (X-46), 905 (X-46), 945 (X-02), 1087 (X-01), 1114 (X-45), 1130 (X-45), 1330 (X-02), 1334 (X-45), 1338 (X-02), 1398 (X-41), 1404 (X-41), 1907 (X-70), 1983 (X-02), 2433 (X-46), 2451 (X-46), 2521 (X-46), 2597 (X-46), 2603 (X-46), 2607 (X-46), 5196 (X-01), 5282 (X-01), 5284 (X-01), 5286 (X-01), 5430 (X-01), 6171 (X-01), 6251 (X-01), 6253 (X-01), 6257 (X-01), 6259 (X-01), 6261 (X-01), 6263 (X-01), 6265 (X-01), 6267 (X-01), 6269 (X-01), 6271 (X-01), 6291 (X-01), 6502 (X-01), 6504 (X-45), 6628 (X-01)
- **GR** (6): 20 (X-01), 58 (X-70), 88 (X-72), 257 (X-01), 261 (X-01), 589 (X-20)
- **M** (12): 36 (X-01), 44 (X-01), 60 (X-00), 111 (X-01), 129 (X-20), 224 (X-01), 268 (X-01), 594 (X-01), 646 (X-26), 708 (X-01), 726 (X-01), 732 (X-00)
- **README** (1): 100 (X-01)
- **SM** (7): 22 (X-01), 30 (X-02), 60 (X-02), 158 (X-41), 222 (X-41), 232 (X-41), 316 (X-41)
- **Str** (42): 80 (X-46), 86 (X-46), 134 (X-46), 136 (X-46), 140 (X-46), 196 (X-46), 206 (X-46), 224 (X-46), 230 (X-46), 256 (X-46), 258 (X-46), 260 (X-46), 264 (X-46), 270 (X-46), 272 (X-46), 314 (X-46), 316 (X-46), 320 (X-46), 327 (X-46), 331 (X-46), 339 (X-46), 351 (X-46), 359 (X-46), 375 (X-46), 560 (X-46), 646 (X-46), 701 (X-46), 730 (X-02), 732 (X-02), 746 (X-46), 768 (X-45), 866 (X-46), 1006 (X-46), 1008 (X-46), 1010 (X-46), 1012 (X-46), 1014 (X-46), 1016 (X-46), 1030 (X-46), 1066 (X-46), 1237 (X-46), 1303 (X-46)
- **Sub** (17): 44 (X-54), 52 (X-54), 92 (X-02), 104 (X-45), 123 (X-45), 129 (X-45), 133 (X-45), 193 (X-45), 205 (X-45), 207 (X-45), 212 (X-45), 216 (X-45), 223 (X-45), 233 (X-45), 268 (X-53), 288 (X-02), 389 (X-02)
- **appc** (12): 16 (X-01), 96 (X-01), 98 (X-01), 102 (X-01), 104 (X-01), 106 (X-01), 108 (X-01), 110 (X-01), 112 (X-01), 114 (X-01), 116 (X-01), 136 (X-01)
- **ch00** (1): 95 (X-01)
- **ch01** (3): 28 (X-01), 163 (X-01), 179 (X-26)
- **ch02** (10): 8 (X-02), 16 (X-54), 76 (X-02), 88 (X-45), 90 (X-45), 118 (X-45), 122 (X-45), 136 (X-02), 158 (X-02), 212 (X-02)
- **ch03** (4): 34 (X-46), 44 (X-46), 84 (X-02), 226 (X-01)
- **ch04** (2): 10 (X-45), 26 (X-45)
- **ch05** (5): 15 (X-02), 19 (X-45), 23 (X-02), 83 (X-41), 89 (X-41)
- **ch07** (2): 42 (X-70), 118 (X-02)
- **ch09** (6): 18 (X-46), 36 (X-46), 106 (X-46), 182 (X-46), 188 (X-46), 192 (X-46)
- **ch19** (5): 126 (X-01), 212 (X-01), 214 (X-01), 216 (X-01), 360 (X-01)
- **gloss** (3): 11 (X-01), 13 (X-45), 137 (X-01)
- **readers** (1): 79 (X-01)
<!-- PTR:END -->

## 6. Deletion criterion for item (ii) and the distance to it at the pin

PREREG §6, with the owner requirements of §6.1 applied in addition. Where the two differ, the stricter
governs (D6). Item (ii) may be deleted only when all of the following hold at one exact head, with a
separate owner decision:

1. **CK1–CK8 pass at that head.** The map must have been rebuilt there; `check` fails on a pin mismatch.
   At the pin: pass.
2. **Every row is closed.** Its status is `done`, or it is an O or F row whose qualification is visible at
   every mapped site. At the pin these remain:
   - **9 rows `in progress`:**
     - Q1: X-16, X-40–X-43;
     - R6: X-50, X-51, X-53;
     - Main:764: X-62. Review round 1 was answered at `1d21aed7`, and CI is green.
   - **23 rows `queued`:**
     - Q3 propagation: X-10, X-24, X-26, X-30, X-55, X-80;
     - R1/R2 scoping: X-12, X-20, X-23, X-25;
     - Step-2 phase: X-63, X-82;
     - regression audit #1468: X-47, X-48;
     - the deletion edit: X-00, X-01, X-02, X-45, X-46, X-54, X-70, X-74, X-75.
   - **The open rows** (X-11, X-21, X-71) are closed in this sense, since each is stated as open or has no
     manuscript claim.
3. **No disguised A1.** No J row has S1 = `Yes` (holds at the pin). Each `Relabel` condition must be stated
   as such where it is introduced. That means M:131, :141, :180, :224, :724 and the companion and book
   restatements (X-20, X-23). Not yet met.
4. **Pointers rewritten.** All 193 `ptr` sites (§5) are rewritten in the deletion edit by their row's rule.
5. **Independent review with a fresh scan.** A non-author review of that exact head records that no
   result silently relies on A1, and a rerun of `ledger_check.py` there is part of the evidence. The scan
   is P0's pattern set plus the extended criterion-5 patterns of `ledger_check.EXTENDED_PATTERNS`:
   - "finiteness posit", "posit A1", "finite information";
   - "finite (periodic) lattice", "finite torus", "periodic quotient";
   - "recurrence cycle/scale";
   - "classical-dimension", "N < ∞", "fixed finite carrier";
   - "finite world/universe/model".

   After the deletion edit, the scan must find no unqualified hit. At the pin the extended scan has 0
   unmapped lines.

### 6.1 Owner deletion requirements (#1169 c.7048255658, `amaybaum`, 2026-11-20T19:08:01Z)

Quoted:

1. "Q1 and R6 have been independently reviewed and accepted."
2. "The A1-EXIT ledger is complete, with every dependency classified."
3. "All 77 remaining sites (Q3) are reconciled across the manuscripts, the book and the mirrors."
4. "No finiteness assumption is hidden in definitions, probability measures or proof dependencies."
5. "The integrated changes have had a final independent review."
6. "**A final regression audit** shows that removing A1 has not weakened, strengthened or changed any
   physical prediction without explicit justification."

Also quoted: "The open questions on the probability law (R1) and on gravity (C1) may stay open, provided
the papers name the missing premises and claim no unconditional results."

| Requirement | Ledger rows or checks | State at the pin |
|---|---|---|
| 1 | Q1: X-16, X-40–X-43. R6: X-50, X-51, X-53 | In progress; not reviewed |
| 2 | CK1–CK8; the extended scan | Passing at the pin. Round-1 review REVISE answered (§12); delta review pending |
| 3 | The 81 Q3 sites (§4), including the FULL mirrors of ch14 and ch18 | Queued (Step 2) |
| 4 | Lexical: CK4, CK6 and the extended scan. Definitions: X-02, X-40, X-45, X-46. Measures: X-10–X-16, X-70. Proof dependencies: the J rows' S1 column, CK8 kernel carriers | Partly. CK4 and the extended scan are lexical (§9). A4's finite lattice (X-40) is the known hidden-finiteness route |
| 5 | Final review of the integrated head | Not started |
| 6 | #1468. Inputs: every row whose correction changes a printed statement (X-00–X-02, X-12, X-20, X-23, X-25, X-40–X-46, X-63, X-70, X-74); the physical-prediction rows (X-47 finite-L values, X-48 classical-dimension reading, X-70–X-72 calibration, X-63 observer selection); the P-indivisibility route (X-20) | Tracked in #1468; not part of this ledger |
| R1, C1 | X-11, X-71 | Premises named; no unconditional claim (§3.2) |

**What may remain after deletion.**

- **The F rows,** stated as finite-only: X-10, X-12, X-16, X-18, X-22, X-24–X-27, X-29, X-45, X-46,
  X-48, X-50, X-51, X-53–X-57, X-62, X-64, X-65, X-70, X-72–X-74, X-80, X-81.
- **The O rows that are not removed,** stated as open: X-11, X-21, X-47, X-63, X-71, X-82, and whichever
  of X-40–X-43 Q1 leaves open.

**What may not remain.** No claim may remain whose support is A1, presented as a property of nature or of
the framework without its finite-only or open qualification.

## 7. Deviations from PREREG

- **D1 (site placement).** `rows.json` overrides place sites, and 108 of them are added to the map:
  - A4's clause and its mirrors (X-40);
  - SM:539, SM:1536 (X-42);
  - the fermion theorem lines (X-43);
  - the global-phase lines (X-63);
  - glossary:105 (Q3);
  - the review's B1 and B2 sites with their FULL mirrors (X-01, X-20, X-40, X-47, X-48);
  - ch18:188 (X-26);
  - the 44 extended-scan lines (D8).

  M:60, M:664, M:732, Sub:56, SM:242 and SM:803 are reassigned (X-00, X-64, X-00, X-63, X-44, X-11).
- **D2 (shared lines).** CK5 accepts an F or O row whose sites are all primary to another row when it lists
  them in `mirrors`. X-42, X-43, X-65 and X-72 now carry full mirror lists (N9).
- **D3 (relocation).** P0 quotes are single sentences. They are matched inside a line, then through the
  applied Phase-1 and Phase-2 splices, then by 60-character anchors, then by longest common block ≥ 0.5.
  The result: 436 exact, 32 by splice, 82 by anchor and 16 fuzzy (all ≥ 0.95), with none removed.
- **D4 (census extension).** The 11 kept Phase-2 census-extension lines are included with their keep
  reasons.
- **D5 (status).** `done` allows the pointer rewrites of the deletion edit.
- **D6 (owner decision after the preregistration).** #1169 c.7048255658 fixes the A4 formulation and
  adds the requirements of §6.1. PREREG §6 is not edited, and the stricter rule governs.
- **D7 (F rows with an A1-free form in records, N5).** By PREREG §7 the following would be J, because an
  A1-free proof exists in records on `main`:
  - X-16: Theorem 19 under P6's Θ-invariant law with equal root masses;
  - X-70: H-count, decoupled, under P7B H1–H14.

  They are classified F because the printed statements are the finite ones, and owner Q4
  (#1169 c.7035888700) bars new companion-paper claims. A unit authorized to print the A1-free forms
  would move them to J.
- **D8 (CK4 "by hand").** PREREG CK4 asks for lines with no P0 counterpart to be classified by hand.
  - The 11 such lines found by the P0 pattern set were each read. They are encoded as three
    `new_site_rules` regexes that record that reading, not a mechanical classification.
  - The 44 lines found by the extended criterion-5 scan were each read and placed by override. Each
    override in `rows.json` carries the reading as its `reason`.
- **D9 (pin).** The preregistration pinned `9db51884`. The ledger is re-pinned to `fbca1df9` by merging
  `main` (Q2). At that pin X-44 is J by owner record c.7048183824. `check` now fails on any tree whose
  manuscript digest differs from the recorded one, and lists the differing sites.

## 8. Review checklist

1. **Row completeness against the sources** (CK1, CK2). Check by reading that no dependency in those
   records is missing.
2. **Dispositions against PREREG §7.** Deviations D7 and D9.
3. **S1 on every J row.** Includes the reworded `Relabel` qualification (X-20, X-23) and its printed
   correction.
4. **S3.**
   - Spot-check the `visible` sites.
   - The 81 Q3 sites are undetermined by design.
   - SM:803/:809 (N12).
   - Sentences matching neither the P0 nor the extended patterns.
5. **The deletion-edit wordings proposed for X-00, X-01, X-02, X-45, X-46, X-70, X-74 and X-75.**
   - They must keep the per-result conditions (NR), (IP), (IL), (REV) and the deep-sector clauses.
   - They must retire the ID (ii) without reuse or annotation.
   - They must not extend any claim.
6. **The deletion criterion (§6, §6.1).** It must be no weaker than owner safeguard 4 and c.7048255658.
   The A4 rows must follow the owner's size-independent formulation.
7. **`ledger_check.py check` and `self-test` at the head.** The pin-mismatch path must fail when a
   manuscript differs.

## 9. Limits

- The site map is lexical: P0's pattern set, the extended criterion-5 patterns, and the review's B1 and
  B2 additions. A dependency in a sentence that matches none of these is outside the checks (review item 4).
- Rows inherit the classification of their source audits.
- The map certifies one manuscript tree, the pin. At a later head `check` reports a pin mismatch until the
  map is rebuilt and re-reviewed.
- Q1, R6 and Main:764 are in progress. Their rows record possible outcomes, not results.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7047514209 | Authorization | Provenance; quoted with author and time |
| #1169 comments 7041456852, 7035888700 | X-12 (μ-O/μ-R finite-only); X-16, X-70 (owner Q4, D7) | Owner decisions quoted as dispositions; provenance |
| #1169 comment 7048183824 | X-44 | Owner decision quoted; the support (SM:242/:250 and `a1exit-q2-20261120/RECOVERY.md`) is on `main` at the pin |
| #1169 comment 7048255658 | X-40–X-43, X-45; §6.1; D6 | Owner decision quoted; provenance |
| #1468 | X-47, X-48; §6.1 requirement 6 | Provenance (planning; regression audit) |
| #1462 (PF-6) | X-44 note | Provenance |
| #1454 | Phase-3 scope, Q1, Q2 | Provenance (planning) |
| PR #1463 (Main:764) | X-62 | Provenance. X-62's F disposition rests on [31] and STAGE1ii G1, both on `main` |
| PR #1466 comment 7048919956 | §12 | Provenance (review record) |
| Q1 and R6 records (in progress, not on `main`) | X-16, X-40–X-43, X-50, X-51, X-53 | Provenance: these rows state the disposition at the pin, not those units' results |

## 11. Verification status (§A.46 item 4)

- **Evidence level.** Paper-only ledger, writer-checked. The completeness checks are mechanical and
  reproducible from `main` with `ledger_check.py`. The row dispositions inherit the evidence level of the
  cited records.
- **Missing.** A delta review of the round-1 answers.
- **Accountable Issue.** #1454 (with #1169 for the authorization and #1468 for the regression audit).
- **What would resolve it.** An accepting review recorded on the guiding PR, followed by an owner merge
  decision.

## 12. Answer to the independent review of `5bda14c5` (round 1, REVISE)

**B1 (unmapped dependencies).** Each site is now mapped:

- Str:1224 and ch01:161 = FULL:494 → X-20 (unit, R1/R2 scoping).
- readers-guide:79 = FULL:167, book/README.md:100, ch03:226 = FULL:1087 and appC:110 = FULL:6265 → X-01
  (ptr).
- ch19:198 = FULL:5268 → X-40 (Q1).
- New row **X-48**, the classical-dimension obstruction family (M:358, :564, :568, :588, :606, :780;
  Sub:533; ch04:146 + FULL; Intro:135). The theorem is F (finite carriers), and its framework reading
  depends on the carrier's size. It is an input to #1468.

**B2 (X-47 sites).** X-47 now holds the listed SM, appA, ch06, ch19, ch04 and appC sites, including the
A·B family and SM:645 = ch06:62, with FULL mirrors.

- These are emergent lattice-gauge regulator lattices (Haar / staggered HMC, SM:813), distinct from A4's
  substratum lattice.
- SM:801 is a negative finite-L phase result.
- SM:645 = ch06:62 is a finite-torus substratum check (X-16).
- The owner moves from Q1 to the regression audit (#1468).

**B3 (Relabel rows).**

- X-20 and X-23 now carry printed-qualification corrections at M:131, :141, :180, :224, :724 and the
  companion and book restatements. Owner: R1/R2 scoping. Status: queued.
- X-25 is F (N1).

**N1.** X-25 is F as printed. A J form would need a printed correction (row text).

**N2.** The counting-law flag is reworded in X-20's S1 and §3.1:

- it cites NR-1 Prop. 2.3;
- F1 is described as a [W] reading within RIGID's family;
- it says "the only law on `main` under which a return is exhibited";
- it no longer echoes the safeguard wording.

**N3.** X-60 is split: X-60 is J (the decay estimate under (IL)), and new row **X-65** is F (O(ε),
exact recurrence). X-61 inherits the split.

**N4.** X-52's weaker condition defines the base channel for Theorem 24(iii).

**N5.** Recorded as D7.

**N6.** X-30's exit says "posited, not recovered".

**N7.** Corrected:

- M:708 is rewritten coherently (X-01).
- M:732: item (ii)'s text is deleted. The ID is retired without reuse or annotation, and its content moves
  to M:60, keeping (NR), (IP), (IL), (REV) and the deep-sector clauses (X-00).
- M:60's P8 sentence on "the identification of nature with a finite reversible substratum" has a
  replacement (X-00).
- X-45 and X-46 name A4's finite periodic qualified case with Q1's wrapping conditions.

**N8.** #1468 is linked (X-47, X-48, §6.1).

**N9.**

- CK8 lists the kernel declarations cited by the manuscripts, all on finite H (`Fintype`):
  - `RootedClassification.rootedMap_periodic`, `rootedMap_zero`, `pper_of_finiteRootedRealizable`;
  - `RootedClassificationAllTime.finiteRootedRealizable_iff_pper`;
  - `RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap`;
  - `EquivalenceChain.isPermMatrix_of_stochastic_inverse`;
  - `PhysicalC4StorageReadback.routedAtStorage_forces_return_indivisibility`, `…_indivisible_somewhere`.

  `CausalReadback.c4r_implies_pIndivisible` is listed as finite H of any finite size.
- X-42, X-43 and X-72 carry full mirror lists.
- The `new_site_rules` are recorded as encoded hand readings (D8).

**N10.** X-44 cites c.7048183824. With the re-pin it is J at the pin (D9).

**N11.** Criterion 5's scan is extended (§6 item 5). At the pin it found 44 unmapped lines, each read by
hand and placed:

- 27 are explicit finite-model or finite-torus statements (Theorem 19 reciprocity "under the counting
  hidden prior of a finite model", known finite models, fixed finite worlds), mapped `none`;
- 11 recurrence-scale or CP-indivisibility lines state their finite return, finite representative or
  finiteness, mapped `none`;
- 5 lines lack a qualifier and go to R1/R2 scoping: Main:159, :356; Cx:474; ch15:113 = FULL:3990;
- Med:35 goes to Q3.

**N12.** Recorded in §3.2.

**N13.** ch18:188 → X-26 (Q3).

**Pinning.** `sitemap.json` records the pin and the manuscript digest. `check` reports "PIN MISMATCH" with
the differing sites, verified by appending a line to `book/preface.md` and reverting it. The map is
re-pinned to `fbca1df9`.

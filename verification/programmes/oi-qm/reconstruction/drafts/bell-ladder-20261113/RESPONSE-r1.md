# RESPONSE to the independent review of BELL-LADDER r1

Review verdict: ACCEPT WITH CHANGES, required changes C1–C14 (`REVIEW.md`, this directory). Every required change is
applied in `BELL-LADDER-r2.md` as specified. Each was re-checked by hand against the source it touches before it
was applied. No disagreement is recorded. The record still uses hand reasoning only; nothing was committed, pushed
or posted.

| Item | Disposition | Check made before applying |
|---|---|---|
| C1 AL vs OA2 E2 | Applied. The relation is now "alongside; neither contains the other". | OA2:606–613 @ `c3b5f37a`: E2 assumes (H1), H-AR, `q = 2`, parity outcomes and (xiv), and imposes no NS. AL needs (NS) and a coset law. Each covers cases the other does not. |
| C2 dichotomy | Applied in §0, the §4 conclusion and §4 (ii). | Step 4 of the proof gives disjoint cosets of `π_A M` only at a fixed `x`. With more than two settings, only the class of `y` modulo `β_A(y) − β_A(y′) ∈ π_A M` is identified. |
| C3 fixed, complete regions; witness | Applied: (AL4) now states fixed, state- and setting-independent regions complete in the BS (Rec) sense, and the **Histories** scope bullet adds the witness. The witness is also recorded in NOTES-r2 as a scoped finding and an open interface question. | Hand check: after one tick `λ_B = (ρ, ρ ⊕ x)` and `b = λ_B[y] = ρ ⊕ xy`, so `a ⊕ b = xy` (PR). `(y, λ_B[y])` is uniform for every `(x, y)`, while the full region reveals `x`. The map is linear over GF(2) and an involution, and `μ_0` is a coset law with MI\* holding. Step 1 of AL uses fixed regions, as the review says. |
| C4 scope edits | Applied: the §0 heading now reads "For OI under the ledger (conditional)"; the Theorem N/N′ alternatives are stated; the complete-history criterion is added to both escape lists. | Theorem N needs (GI) together with MI for Ω, and N′ needs MI\* (BS:159–196). r1 cited N′ with (xiv), which presumes (xiv) is read as MI\*. That is the open reading question in §5, so both routes are now named. |
| C5 owner term | Applied: stages 0–4 are relabelled "NOT FORCED (designed witness)". The §1 definition states that these are not escapes demonstrated in the authorization's sense and that for OI's native rule those stages are undetermined. | #868 c.6854708572 defines escape demonstrated as "a native construction with complete records and no-signalling checked". The toys are non-affine designed maps. The owner may instead ratify the r1 reading (NOTES-r2); no verdict depends on the label. |
| C6 check 4 | Applied. | In the symmetrized `G_φ` of `φ_0′`, `d(g_A, R_B) = 3` (`g_A–r_A–λ_A0–r_B`) and `d(g_B, R_A) = 2` (`g_B–r_B–λ_A0`), both above the one-tick window. The r1 statement was false. |
| C7 control row `R_A ∋ r_B` | Applied. | `φ_0′` writes `r_B ⊕= λ_B[g_B]`, so `G_φ` has the edge `g_B → r_B`, and with `r_B ∈ R_A` (Sep) fails at distance 1. The dependence is null only because `λ_B = 0` on the support of `μ_0`. The r1 reading "common cause (SB L3)" was wrong. |
| C8 access claim in §0 | Applied: the claim is scoped to the toy, and no general access-only theorem is claimed. | §3 already limited it to the toy, and NOTES records that the general argument was not completed. |
| C9 PPS scope | Applied: PPS now supports only the branch with stage 3 relaxed and MI kept. | PPS:136 @ `c3b5f37a`: "with each law common across setting interventions", which is MI. |
| C10 Main:484 → :486 | Applied in the stage-1 row and in the item 8 range (now :480–486). | Main:486 is the Proposition (no uniform finite realization), and :484 is the closure remark. The proposition concerns the continuum instrument space. |
| C11 disjoint generator regions | Applied in the §0 blockquote. | BS:142: "Disjoint generator regions `G_A, G_B ⊂ V`". |
| C12 check 5 relabelling | Applied. | With `λ′ = ρ ⊕ x` (uniform and independent of the settings under `μ_0`): `a = ρ = λ′ ⊕ x`, `b = ρ ⊕ x = λ′`. The response functions are local. |
| C13 item 8: RC, QH, SB L4 | Applied. (AL2) cites MP-0a at OA1:556–558 and μ-G at OA1:103–105. Stage 4 cites Main:42 and OA1:111–112. QH's stage-7 use is "support off `main`: gap", on which no verdict rests. The SB L4 citation is removed in favour of Main:362. The RC row is now provenance. The SWAP/2 Bell-locality is tagged [A]. | OA1 r5 @ `c3b5f37a`: :103–105 μ-G; :111–112 "A setting is a configuration of designated cells"; :556–558 MP-0a. Main:42 is the Definition. SWAP/2 over Pauli-axis product tests is a mixture of products of cube vertices (shared uniform triple), so it is Bell-local by hand. QH:68–97 does not state this. |
| C14 #1232 review status | Applied. | Host record: 5858000929 is REVISE at `b94b283a`; 5859960068 is ACCEPT WITH NITS at `86a413c8`. |
| Nonblocking: step 2 `e_{x_0} = f_{y_0} = 0` | Applied. | — |
| Nonblocking: composite converses | Applied: stage 0 cites `Equivalence.lean:466–468`, and the item 8 row lists them. | — |
| Nonblocking: `Z_3` Birkhoff remark | Unchanged in NOTES-r2 and still unreviewed. Nothing rests on it. | — |
| Nonblocking: fixed point | Recorded in NOTES-r2: two passes so far, the second producing a NEW item, so the fixed point is not reached. | — |
| Informational: rec-1 head | NOTES-r2 records the move to `cd38655c` (fetched by name at r2; the review saw `7f465d56`). The REC-1-r7 blob `f1ffac0e…` is unchanged, so every RC citation stands. | `git rev-parse` at r2. |

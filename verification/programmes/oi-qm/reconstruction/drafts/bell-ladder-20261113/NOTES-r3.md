# NOTES r3 — Bell debugging ladder (writer's working notes, not for landing)

r3 accompanies `BELL-LADDER-r3.md`. r2 added the head refresh, the review's witness and the fixed-point count; r3
applies the focused confirmation of r2 (R1, R2, N1, N2).

## Method and limits kept
- Paper-only. No script or probe was written or run; no Lean build; no computation on any OI rule. The §2 toys of
  BELL-LADDER.md are generic finite bijections whose statistics were checked by substitution by hand.
- Git: `git fetch origin <branch>:refs/remotes/origin/<branch>` by name only for main, the bell-scope, q868h,
  substate-bridge and rec-1 branches. No `--depth`, `gc`, `prune`. The writer made no commit, push,
  comment or manuscript edit; the coordinator committed r2 on #1273 at `b8096c79`.
- Authority read from #868 c.6854708572 (last comment on the Issue; 16 comments total, one page).

## Citation verification (done)
- Heads: bell-scope `e1534b08`, q868h `ffc9cda4`, substate-bridge `86a413c8` match the PR heads. rec-1 was read at
  `9f7d2612`; the branch head has since moved to `cd38655c` (fetched by name at r2; the review saw an intermediate
  head `7f465d56`), and the REC-1-r7 blob is unchanged (`f1ffac0e…`), so every RC citation stands.
- #1232 review 5858000929 is REVISE at `b94b283a` (r1 item-8 row grouped it wrongly; corrected in r2, C14).
- Reviews: #1231 5857227567 REVISE @7abf59d7 and 5857981727 ACCEPT WITH NONBLOCKING NITS @e1534b08 (confirmed);
  #1232 5859960068 ACCEPT WITH NITS @86a413c8; #1268 5891524305 ACCEPT @9f7d2612; #1269 review 5891666660 is at
  `acf28d3a`, not `ffc9cda4` (the head adds two record-nit commits, 7 lines changed). The brief's "Q-868-H r3 @
  ffc9cda4" is the current head; its ChatGPT review is at the earlier commit.
- Lean directions: `Qfb_imp_S` :245, `D_imp_Qfb` :294, `S_imp_D` :422, wrapper `finite_horizon_equivalence` :462 in
  `OIBridge/Equivalence.lean` @ c3b5f37a. Main:550 carries `finite_horizon_equivalence`, `S_imp_D`,
  `permMatrix_mem_unitaryGroup`, `isDiag_Phi`; Main:97 carries all three directions inline.
- Lean class (D) permits an initial law correlating hidden and visible coordinates (Equivalence.lean:150–156). The
  independent-prior form is Main:516–518, paper only (census note says not formalized).

## Staleness of inputs against main @ c3b5f37a
- BS and SB are pinned at cac5d264. On main: Main:362 now carries `G_φ^K` and "for a linear update … `G_φ^K = G_φ`
  for every non-empty K; a graph that differs between state classes requires an update outside (vii)"; ledger (x)
  is scoped to `G_φ^ref`; ledger (xiv) is measurement independence (Main:724). So BS findings F1 and F2 are resolved
  on main; BS O1 now reads: under (vii) no preparation-indexed long edge exists, and Main:414 says the adopted branch
  lies outside (vii). For the linear update of (vii), SB L4's content is Main:362; L4 itself is
  broader (any abelian site groups, no finiteness hypothesis).
- BS/SB line citations `Main:364` (cone lemma) and `Main:726` (ledger) are now Main:362 and Main:724.

## Pressure tests (§A.31)
### The escape toys (favourable to escape)
- `φ_×, μ_0`: non-affine (AND), outside ledger (vii); NS only for the uniform-pad preparation and single use; a
  deterministic pad or pad reuse signals. Designed map (RC Q2-F), not a native construction. It shows only that
  stages 1–2 do not obstruct.
- `φ_0, μ_MD`: separated and generator-isolated, but MI fails grossly and `φ_0` is a controlled read (non-affine).
  Excluded by (xiv). Shows only that (Sep) without MI does not obstruct.
- Neither toy bears on OI's own rule; both are logical-sharpness witnesses for the ladder's boundaries.

### Proposition AL (favourable to obstruction)
- Checked each step for hidden use of (Sep), (GI) or MI: none. Admissibility of every menu pair is used in step 2
  (to build `e_x`, `f_y`). Independent review re-derived steps 1–5 and found no error.
- Implicit hypothesis made explicit in r2 (review C3): record regions fixed (independent of state and settings) and
  histories complete. The review's witness (`λ_B0 ⊕= λ_A0`, `λ_B1 ⊕= λ_A0 ⊕ g_A`, `μ_0`; `a = λ_A0`, `b = λ_B[y]`)
  re-checked by hand: after the tick `λ_B = (ρ, ρ ⊕ x)`, `b = ρ ⊕ xy`, PR; `(y, λ_B[y])` is uniform for every
  `(x, y)`; the full region `(ρ, ρ ⊕ x)` reveals `x`. The map is GF(2)-linear and an involution, `μ_0` is a coset
  law, MI\* holds. Scoped finding (NEW in the review, recorded in r2): inside (vii) with a coset law and MI, a PR box
  is reachable when no-signalling is imposed on a setting-selected read rather than the complete fixed-region
  history. Whether an embedded observer's history is the complete fixed region or a setting-selected read is an
  interface question (RC C5/C6 record conventions) that this ladder does not settle; it is an assumption-watch
  marker for every affine-class classicality result.
- Dichotomy narrowed (C2): failure of NS gives TV 1 between two remote settings at a fixed own setting; with more
  than two settings only a class of remote settings modulo `π_A M` is identified.
- Requires NS on the complete fixed-region histories; NS on the part the outputs read does not suffice (the
  selected-read witness above). NS on a larger fixed history implies NS on a smaller fixed one.
- Coset-uniformity is load-bearing. Checked by hand: in `Z_2` and `Z_3`, laws with uniform marginals decompose into
  coset components each satisfying NS (all permutations of `Z_3` are affine; Birkhoff), so they stay local. For
  groups with non-affine permutations, and for non-uniform marginals invariant only under a subgroup, a law
  satisfying NS only jointly is not covered and was not settled. Recorded as open.
- `μ_MD` is the reason MI-type conditions cannot be dropped in general: with a setting-dependent, non-coset law, an
  affine readout `h_A = λ_A`, `h_B = λ_B` gives PR (λ_A uniform, λ_B = λ_A ⊕ xy given the settings). So in AL the
  coset hypothesis does the work MI does elsewhere.
- Prior art searched (§A.19): OA2 Corollary E2 (q=2, parity, (xiv)), OA2 Theorem E, OA1 D5, T1 Lemma A-T (coset
  laws, 0-or-1 dichotomy), obsmu Proposition C (cited in OA2, not re-read), QH (V). No two-wing, any-group,
  NS-hypothesis version was found on main or on the input branches. Classification: ELABORATING (alongside E2,
  neither containing the other: C1); the route-C consequence is NEW relative to BS and SB (both left route C open);
  the reviewer's search of main found no two-wing coset/NS result either.
- Productivity test: stronger than a restatement (drops (Sep), (GI), MI for the affine class; any finite abelian
  group, any extractor) and constrains a live route (C). Passes. Assumption-watch marker: "coset-uniform run law" is
  the hidden premise behind every affine-class classicality result (Lemma A-T, E(b), E2, AL); it should be audited
  wherever (iv) is read as selecting the run law.

## Things the ladder does not claim
- No general access-only theorem: the access controls are shown in the toy. A general statement (record access
  outside (Sep), with local coupling and MI, yields either signalling or a local law) was attempted; a one-sided
  gluing argument works when A's full own-wing content is in its history, but a counterexample search for lossy
  own-wing histories was not completed. Left as a candidate.
- No claim about the native rule's behaviour in the O2 window beyond AL's conditional dichotomy; the mixed-path
  computation remains the place to observe it.
- No reading of physical *c*, of (xiv)'s scope over residues, or of (iv)'s run law is chosen.

## Owner-term relabel (C5)
- The authorization defines "escape demonstrated" as a native construction. r1 used it for designed maps; r2
  relabels stages 0–4 "NOT FORCED (designed witness)" and states that for OI's native rule those stages are
  undetermined unless stated. The owner may instead ratify the r1 reading; nothing else depends on the label.

## Questions for the owner (not decided here)
1. Should "physically admissible" in the question include ledger (vii)? If yes, the ladder's answer for OI is
   conditional: the AL obstruction (and Theorem N or N′ for graph-separated wings) holds for coset-uniform run laws,
   cell-valued settings and complete fixed-region histories, and an escape needs a Layer-0 revision or the failure
   of one of those conditions (§0; Q4); if no, the general-class answer (stage 5) applies.
2. Is (xiv)'s "response-relevant pre-setting variable" meant to include generator residues (then (xiv) = MI*)?
3. AL has had one independent review. If its expectation is used for the mixed-path stage-2 unit, under §A.29
   it informs the decision rule only; it is not entered as an expected outcome in that preregistration.
4. Is an embedded observer's complete history the full fixed record region, or may it be a setting-selected read?
   AL's obstruction holds for the former; the review's witness gives PR for the latter.

## Not done
- One independent review (ACCEPT WITH CHANGES, all fourteen required changes applied). No ChatGPT review yet.
- Fixed point (§A.31): two passes so far (writer r1; review), the second yielding a NEW item (the selected-read
  witness), so the 3–4-passes-without-NEW condition is not met. A further pass should target the history/interface
  convention behind (AL4).
- QH, RC, OA-3 read only where cited; obsmu Proposition C not re-read.

# NOTES — Bell debugging ladder (writer's working notes, not for landing)

## Method and limits kept
- Paper-only. No script or probe was written or run; no Lean build; no computation on any OI rule. The §2 toys of
  BELL-LADDER.md are generic finite bijections whose statistics were checked by substitution by hand.
- Git: `git fetch origin <branch>:refs/remotes/origin/<branch>` by name only for main, the bell-scope, q868h,
  substate-bridge and rec-1 branches. No `--depth`, `gc`, `prune`. No commit, push, comment or manuscript edit.
- Authority read from #868 c.6854708572 (last comment on the Issue; 16 comments total, one page).

## Citation verification (done)
- Heads: bell-scope `e1534b08`, q868h `ffc9cda4`, substate-bridge `86a413c8`, rec-1 `9f7d2612` match the PR heads.
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
  lies outside (vii). SB L4 is superseded by Main:362 (same content, now on main).
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
  (to build `e_x`, `f_y`).
- Requires complete-history NS only for the histories the outputs are read from; NS on a larger history implies it.
- Coset-uniformity is load-bearing. Checked by hand: in `Z_2` and `Z_3`, laws with uniform marginals decompose into
  coset components each satisfying NS (all permutations of `Z_3` are affine; Birkhoff), so they stay local. For
  groups with non-affine permutations, and for non-uniform marginals invariant only under a subgroup, a law
  satisfying NS only jointly is not covered and was not settled. Recorded as open.
- `μ_MD` is the reason MI-type conditions cannot be dropped in general: with a setting-dependent, non-coset law, an
  affine readout `h_A = λ_A`, `h_B = λ_B` gives PR (λ_A uniform, λ_B = λ_A ⊕ xy given the settings). So in AL the
  coset hypothesis does the work MI does elsewhere.
- Prior art searched (§A.19): OA2 Corollary E2 (q=2, parity, (xiv)), OA2 Theorem E, OA1 D5, T1 Lemma A-T (coset
  laws, 0-or-1 dichotomy), obsmu Proposition C (cited in OA2, not re-read), QH (V). No two-wing, any-group,
  NS-hypothesis version was found on main or on the input branches. Classification: ELABORATING of E2; the route-C
  consequence is NEW relative to BS and SB (both left route C open).
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

## Questions for the owner (not decided here)
1. Should "physically admissible" in the question include ledger (vii)? If yes, the ladder's answer for OI is the
   AL/Theorem-N′ obstruction and an escape needs a Layer-0 revision; if no, the general-class answer (stage 5) applies.
2. Is (xiv)'s "response-relevant pre-setting variable" meant to include generator residues (then (xiv) = MI*)?
3. Should AL be routed to an independent review before the mixed-path stage-2 preregistration is fixed, since it
   predicts that unit's outcome under coset laws?

## Not done
- No independent review; no ChatGPT review. No fixed-point passes beyond one (§A.31 asks for 3–4 without NEW).
- QH, RC, OA-3 read only where cited; obsmu Proposition C not re-read.

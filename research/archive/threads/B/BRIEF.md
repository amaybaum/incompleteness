# Thread B — copy structure: NOT-conjugacy reduction and three-copy consistency (read-only, exact)

Read first: threads/PROTOCOL.md; K-INF-DESIGN.md §6, §16–§17; NB-1 preregistration and probe
(wt-threads/verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/preregistration.md,
wt-threads/verification/lean/native_gate_ball_probe.py); k-infinity/two_not_d7.py; k2/*.py for helpers.

1. Conjugacy reduction. If N_B = g N_A g⁻¹ with g a frame-preserving local cone automorphism of the d-ball (fixes u,
   preserves the corners' frame), show G̃ = (I⊗g⁻¹) G (I⊗g) meets NB-1's F, Rt, Rc and P± with one common N_A.
   Write the proof; then check it exactly: (a) on a constructed conjugate pair at d = 3 and d = 5 (must reduce to
   the one-N case); (b) confirm the d = 5 (2,2)/(1,3) and d = 7 (3,3)/(1,5) countermodels are NOT conjugate under
   any frame-preserving g (split classifier), and (c) determine whether, under the frame stabilizer, the split
   (p, q) is a COMPLETE invariant of frame-preserving conjugacy for these involutions. Do not equate split and class
   without (c).
2. Three-copy consistency. With copies A, B, C, pairwise native CNOTs meeting NB-1's relations for each ordered
   pair used, test whether any assignment of NOTs with a mismatched split survives (start d = 5, then d = 7), and
   say exactly which three-copy relations you impose (state them before computing). Countercontrol: the matched
   case must survive.
Deliver threads/B/RESULT.md per the merge rule.

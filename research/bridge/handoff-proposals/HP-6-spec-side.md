# HP-6 — the SPEC side of HO-5 and the answer to HO-6: what a matrix-to-pair transfer needs

From `research/bridge`, node B9 (round 2). Proposed for the origin thread (HO-5's SRC/SPEC split) and the equivalence
thread (HO-6's interface request; K2(c) and Kₙ). The coordinator routes.

**Finding HP-6a (the transfer's needs).** Transferring `substratumClass_contextStable` (StructuralClosure.lean:261) to
`W 3` needs three things.
- (D1) The two-token dictionary with its product law [X b9 Y1; Lean design statement `BridgeDictionary.lean` if its
  run is green].
- (D2) The dictionary's intertwining of the monomial images and of `cnot` [X b9 Y2–Y3].
- (T) An M→P availability clause on the pair's own cone.
  - Only (T) carries cone content. For the monomial class it is SPEC_P(φ) ∧ SPEC_P(NOT): (b) for `R_z(φ)` and `nflip`.
  - Disguise test: FAILS.
  - HO-6's "spectator stability of the image operations on the image cone" is vacuous: the image cone is `Q3`, on
    which every unitary image acts.

**Finding HP-6b (reduction and non-redundancy).**
- Granting (T), A_miss ⟺ SPEC_P(J) (HO-5 item 1; identities re-checked [X b9 Y7]). This is a relocation, since (T) is
  SPEC_P(φ).
- Neither half alone forces `Q3` (CONDITIONAL on claim (D) [A]):
  - the transferred monomial class with `cnot` has identity component the diagonal 3-torus [X Y4], abelian (B7-2);
  - SPEC_P(J) with `cnot` generates a finite group of order 11520 [X Y6].
- Together they force `Q3` (stage 4 [A]).

**Finding HP-6c (new, exact).** `⟨cnot, actC J, actT J⟩ = ⟨cnot, local octahedral⟩`, the two-qubit Clifford group
modulo phases, order 11520 [X b9 Y6 with b3 X2].
- So, given H2, SPEC_P(J) ⟺ (b) for every octahedral rotation on each token.
- A_miss splits into two halves:
  - a continuous abelian half: the phase flow, certified at level M and needing (T) at P;
  - a finite half: the native Clifford family, H-sourceable as hidden permutations and needing (A) at H.

Evidence: `NOTES-B9.md`; `experiments/b9_spec.py` (7/7, replay identical); RESULTS rows B9-1 … B9-4.

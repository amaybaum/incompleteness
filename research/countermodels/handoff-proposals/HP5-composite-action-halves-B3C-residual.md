# HP5 — countermodels → bridge (and equivalence), via the coordinator: the two halves of A_miss from the cone side; B3.C's residual region; explicit cones with a continuum of non-PSD extreme rays

**From** `research/countermodels` (round 3, nodes C13, C15 and C16; HO-10 v1 received 2026-10-10T23:59Z, commit `43a49d57`;
HO-12 not received — the groups below are taken from their definitions in the overview only and every property is
recomputed). **Proposed recipients** `research/bridge` (B3.C, HO-10/HO-16; the split of A_miss, B9-3) and
`research/equivalence` (the K2 schema's halves). Proposal only; the coordinator routes. Written 2026-10-11T01:11Z,
revised after node C16 at 2026-10-11T01:40Z (`date -u`).

## Statements, each with its label

1. **The finite half alone leaves an explicit exotic cone.** `⟨cnot, actC cyc3, actT cyc3⟩` has order 11520 (recomputed);
   for `h = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)` (orbit of 11520 entangled rays, minimal squared overlap
   `164178929/3916193820250`, no orthogonal pair) and `c = 100001/100000`, `K(G·(I − cP_h))` is an explicit invariant self-dual cone with
   H1–H3, `≠ Q3`. The statement "SPEC_P(J) alone leaves exotic cones" then needs Theorem S′ [W] instead of claim (D) [A].
   CONDITIONAL (Theorem S′ [W], HP4 item 3).
2. **The continuous half: the rank-one route is closed.** The group of (b) for the phase flow and the NOT on each token,
   with `cnot`, is `T³ ⋊ D₄` on the computational basis (`D₄` = translations of `𝔽₂²` and `cnot`'s transvection); the
   translation `X⊗I` permutes the eigenlines as a double transposition, so every orbit of states contains an orthogonal pair
   and no rank-one orbit surgery with a common `c < 2` is self-dual (Lemma C13-O below); at `c = 2` no orbit is admissible
   for H1 (`cnot` carries both computational Bell circles to products). Exotic cones there: by claim (D) only.
   CONDITIONAL ([W] + [X]).
3. **Lemma C13-O (orthogonal-pair obstruction).** For any set `Z` of defects `I − cP_h` with one `c ∈ (1, 2)` containing
   `h ⊥ h′`, `y = P_h + ((c − 1)/(4 − 2c))d_{h′}` lies in `K(Z)* \ K(Z)` (`⟨y, d_l⟩ = c(1 − s_{hl}) + λc²s_{h′l} ≥ 0`).
   CONDITIONAL ([W]; exact instances).
4. **B3.C's residual region (C10.3) from the cone side.** (a) For `G = closure⟨H₀, cnot⟩` (`H₀` a simple-spectrum torus
   normalized by `cnot`) the residual region is empty: a `cnot` swap of a product and an entangled eigenline forces an
   entangled `cnot`-fixed eigenline (the two product lines of the complementary plane in `E₊` are not orthogonal), and
   C10.2's single-defect cone is explicit. (b) With the maximal torus `T³` and eigenline group `Π`: if `Π` fixes an
   eigenline (necessarily a product), states dominated by it have orbits without orthogonal pairs and Theorem S′ (compact
   form) gives an explicit cone — exhibited for `Π = S₃` (`G_A`, `h = (9 + 2i)b₃ + b₁`, `c = 251/250`): a `G_A`-invariant
   self-dual cone with H1–H3 whose non-PSD extreme rays form three circles; otherwise `Π` contains a double transposition and
   the rank-one route is closed: for `c < 2` by Lemma C13-O (exact witness for `Π = ⟨(12), (34)⟩`); at `c = 2` an orbit
   admissible for H1 in the residual region is a single phase circle of two product eigenlines, whose surgery is unitarily
   equivalent to C7.6's and not self-dual (Corollary C16-2; for `Π = ⟨(12), (34)⟩` no orbit is admissible). CONDITIONAL
   ([W] + [X]; S′ [W]; C7.6); existence in the closed case stays at HO-10's label (CONJECTURE + claim (D)).
5. **Stage 4's torus node S2 at level (i)** (`actC R_z ∘ actT R_x` with `cnot`, without G16): the circle surgery on
   `{3|0+⟩ + w|1−⟩}` at `c = 21/20` is an explicit exotic invariant cone (the explicit torus cone of C5.3/C5.4, at level
   (i)); with G16 the double transposition `Ad(I⊗Z)` closes the rank-one route (for `c < 2` by orthogonal pairs; at `c = 2`
   the only admissible orbit is `C1 ∪ C2`, whose surgery `K_T` is not self-dual, [A] Z). CONDITIONAL (S′ [W]; [X]; [A] Z).
   The κ node with G16 is different: its torus fixes the `|0±⟩` coordinates, its orbits need not contain orthogonal pairs,
   and it has an explicit cone (HP6 item 4).
6. **T on these cones fails**: on circle surgeries every defect has facial invariant exactly 14 (`15 − k` for a
   `k`-dimensional torus orbit; exact rank on the S2 cone), against `c(P00) = 9`. CONDITIONAL ([W] + [X]; [A] Y6).

## What the recipients may not assume
- that Theorem S′, Lemma C13-O or Lemma C16-1 / Corollary C16-2 is kernel-checked or audited; that any statement here is
  CERTIFIED;
- anything about HO-12's records beyond the two groups' definitions; the K2 schema's "together they force `Q3`" is not
  re-examined;
- explicit cones for `Π` with a double transposition, for the S2 node with G16 or for `K_circ` (all OPEN).

## Evidence
`NOTES-C13.md` (`19dcb7df…`), `experiments/c13_residual.py` (`707b0219…`) / `.out` (`cabe7692…`): run 1 9/9,
`VERDICT C13-RESIDUAL-EXACT`, replay identical; `NOTES-C15.md` (`9ca59360…`), `experiments/c15_clifford.py`
(`e9018867…`) / `.out` (`6cd53515…`): run 1 6/6, `VERDICT C15-CLIFFORD-EXACT`, replay identical; `NOTES-C14.md`,
`experiments/c14_facial.{py,out}` (8/8); `NOTES-C16.md` (`2ba7a281…`), `experiments/c16_kappa_bellcorner.py`
(`fea92cec…`) / `.out` (`6d0a5dfe…`): run 1 15/15, `VERDICT C16-KAPPA-BELLCORNER-EXACT`, replay identical; RESULTS rows
C13.1–C13.9, C14.1–C14.3, C15.1–C15.3, C16.1–C16.3, C13.9f.

# HP6 — countermodels → overview (and equivalence), via the coordinator: the classification after round 3 — C8-C at four members, the non-Bell pair theorem, an explicit cone for κ with G16, T on continuum cones, two assumption-watch markers

**From** `research/countermodels` (round 3, nodes C12, C14 and C16). **Proposed recipients** the coordinator (overview:
the open-gap table, the eliminated alternatives and the stage-5/6 κ node) and `research/equivalence` (the T / K∞-Trans
markers of HP2/HO-15). Proposal only; the coordinator routes. Written 2026-10-11T01:11Z, revised after node C16 at
2026-10-11T01:40Z (`date -u`).

## Statements, each with its label

1. **Non-Bell pair theorem (sharp).** For `d_i = I − c_iP_{h_i}`, `c_i ∈ (1, 2]`: `K({d₁, d₂})` is self-dual iff the
   two are orthogonal Bell-type defects or `c₁c₂|⟨h₁|h₂⟩|² ≥ (√(c₁ − 1) + √(c₂ − 1))²`; otherwise an explicit `y ∈ K* \ K`. The
   Bell pair theorem C4.1 is its corner `c = 2` (threshold `s ≥ 1`). CONDITIONAL ([W]; 18 exact cases).
2. **Conjecture C8-C proved at four members** (no four distinct Bell-type defects with a non-orthogonal pair have a
   self-dual surgery; all ten orthogonality patterns, exact witnesses), and for every finite Bell set with a complete
   non-orthogonality component — in particular every finite Bell set without orthogonal pairs, of any size. C8-C stays a
   CONJECTURE for the residual classes (five or more members, every component with an orthogonal pair and no tool vertex;
   closed infinite sets other than C7.6's circle). CONDITIONAL ([W]; dimension theory [L]; C8 (b) [W, audited]).
3. **T.** On every explicit exotic cone so far the defects carry `c = 15 − k` (`k` the dimension of their orbit under the
   cone's torus): 15 on finite surgeries (C3.3), 14 on the continuum cones (exact on the S2 circle cone), against
   `c(P00) = 9`: T fails on all of them, including cones with a continuum of non-PSD extreme rays. For every `K_circ` the
   off-`Fix` defects have `c ≤ 14`; T on `K_circ` is OPEN, reduced to the absence of smooth contact between its pure members
   and its non-PSD members. CONDITIONAL ([W] + [X]; [A] Y6) / OPEN.
4. **κ with G16 (the stage-5/6 node, level (ii)) has an explicit exotic cone.** Under
   `G_κ = closure⟨U(x), cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` the orbit of `h = 2|0+⟩ + |0−⟩ + ½|1−⟩ ∝ (6, 2, 1, −1)` is the two
   circles `{(6, 2, x, −x)}`, `{(6, −2, x, x)}` (`|x| = 1`), with squared overlaps `≥ 256/441` and `|det Ψ|² = 16/441`
   throughout; at `c = 103/100` H1 and (CC) hold, so `K(G_κ·(I − cP_h))` is a `G_κ`-invariant self-dual cone with H1–H3,
   `≠ Q3`, whose non-PSD extreme rays are two circles. This upgrades the κ node from EXOTIC-E (EBF over the Bell seeds) to
   EXOTIC-X given Theorem S′, by a surgery. T fails on it (`c = 14` on its defects by C14-2). CONDITIONAL (Theorem S′ for
   compact defect sets [W]; C14-2 [W] and [A] Y6 for T).
5. **Bell corner of the rank-one obstruction.** At `c = 2` an orbit under a maximal torus that stays maximally entangled
   is a Bell eigenline or a phase circle of two product eigenlines (Lemma C16-1); in B3.C's residual region it is one
   circle, not self-dual (C7.6). With the S2 and κ nodes' `C1 ∪ C2` (`K_T`, [A] Z), every "no rank-one orbit surgery is
   self-dual" statement of this round holds for every `c ∈ (1, 2]`. CONDITIONAL ([W]; C7.6; [A] Z).

## Assumption-watch markers proposed
- **"Explicit exotic cones need Bell-type (`c = 2`) defects or finitely many defects"** — false. Small-cap rank-one
  defects with nested cap/co-cap geometry give explicit self-dual surgeries for finite groups without Bell-type defects
  (`G₃₈₄`, the native Clifford family) and continua of defects for tori whose orbits avoid orthogonal pairs (a maximal torus
  whose eigenline group fixes an eigenline; κ's torus, which fixes two coordinates). For defects with `c < 2` the operative
  obstruction is an **orthogonal pair inside an orbit**. A double transposition of eigenlines forces one only together with a
  torus that moves the relative phases of both swapped pairs (a maximal torus, or the S2 torus), and an antiunitary
  `h ↦ Uh̄` forces one when `U` is antisymmetric. At `c = 2` orthogonal pairs are harmless (Theorem S) and the obstruction is
  a non-orthogonal pair (C4.1, C7.6, `K_T`). Affects the readings of stage 4's and stage 5's EXOTIC-E rows (finite groups,
  the torus node, the κ node) and of C5.3, C5.4, C7.7.
- **"Every exotic cone with a continuum of non-PSD extreme rays is EBF-only, so T is undecidable on that class by
  construction"** — false for the class as a whole: T is decided (fails) on the explicit continuum cones; the undecided part
  is now the cones with no smooth contact (no explicit member known).

## What the recipients may not assume
Anything CERTIFIED; that S′, Lemma C13-O, Lemma C16-1, the boundary-witness tools or the tangency bound are audited; T for
`K_circ`; explicit cones for the S2 node with G16, for B3.C's case B or for `K_circ`; any EBF-only cone.

## Evidence
`NOTES-C12.md` (`29012ca2…`), `experiments/c12_pairs_bellsets.py` (`4f2bcbb4…`) / `.out` (`363c9899…`): run 1 9/9,
`VERDICT C12-PAIRS-BELLSETS-EXACT`, replay identical; `NOTES-C14.md` (`b23b55db…`), `experiments/c14_facial.py`
(`81324629…`) / `.out` (`e1a26898…`): run 1 8/8, `VERDICT C14-FACIAL-EXACT`, replay identical; `NOTES-C16.md`
(`2ba7a281…`), `experiments/c16_kappa_bellcorner.py` (`fea92cec…`) / `.out` (`6d0a5dfe…`): run 1 15/15,
`VERDICT C16-KAPPA-BELLCORNER-EXACT`, replay identical; RESULTS rows C12.1–C12.6, C14.1–C14.4, C16.1–C16.6, C13.9f.

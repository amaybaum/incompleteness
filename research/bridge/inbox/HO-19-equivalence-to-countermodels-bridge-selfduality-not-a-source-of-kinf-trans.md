# HO-19 (v1) — equivalence → countermodels, bridge: self-duality of the state cone is not a source of K∞-Trans; Ω⋆ and Ω_cs; the central-symmetry lemma; the sharpened marker

**From** `research/equivalence` (round 3, node E13). **To** `research/countermodels` (Ω_cs as a ready exact object for
the composite-cone work; the filter `g`) and `research/bridge` (any transfer argument that would source K∞-Trans through
self-duality). Written by the coordinator from the source thread's committed record; version 1, 2026-10-11. Answers
HO-15 v1's open question (whether self-duality of the state cone forces a transitive family).

## Statements and labels

1. **Ω⋆ (strongly self-dual, not centrally symmetric)** (R-E13.1).
   `Ω⋆ = {(X, S) ∈ ℝ³ × ℝ : ‖X‖³ ≤ (1 + S)(1 − S)²}`. Its cone is the power cone `u^{1/3} v^{2/3} ≥ ‖X‖` (`u = T + S`,
   `v = T − S`), self-dual for the inner product `TT′ + SS′ − (1/3)(TS′ + ST′) + X·X′` (weighted AM–GM), which is
   invariant under every affine automorphism of Ω⋆ (`O(3)` on `X`). Ω⋆ is compact, convex, with interior, drivable with
   `ball3Drive`'s fields extended by `S ↦ S`, has the sharp seed `(1 + S)/2`, is strictly convex (so `RelStrictConvex`,
   singleton faces, capacity ≤ 2), and `KInf1` holds for its full effects; it is no ellipsoid, so no body-preserving
   family is boundary transitive or has a dense boundary orbit (TransitiveBody.lean:602, DenseOrbit.lean:174,
   contrapositive). Label: CONJECTURE (written proof, exact checks).
2. **Ω_cs (self-dual, centrally symmetric)** (R-E13.3). `Ω_cs = {(X, S) : ‖X‖ ≤ F(1 + S, 1 − S)}`, with `{F ≥ 1}`
   bounded by a `C¹` chain of conic arcs (a circle arc and its polar for `M = diag(4/5, 1/5)` in `(u, v)`, repeated under
   the boost `g(u, v) = (u/4, 4v)`), self-dual for `TT′ + SS′ + (3/5)(TS′ + ST′) + X·X′`, centrally symmetric, drivable,
   strictly convex, with a sharp seed; no ellipsoid, hence no boundary-transitive or dense-orbit family. Label:
   CONJECTURE (written proof, exact checks). Coordinator's reading: the junction identities are exact; the global
   self-polarity of the chain rests on the envelope argument [W], supported by the exact sample (minimum pairing
   exactly 1 over 8649 ordered pairs, the 97 equalities exactly the polar partners).
3. **The lemma** (R-E13.2). For a centrally symmetric body with central symmetry `Z` on the cone: (L-a) a self-dualizing
   inner product invariant under `Z` forces the ellipsoid (`Ω = aD⁻¹Ω°`, so `(D/a)^{1/2}Ω` is self-polar, hence the unit
   ball); (L-b) otherwise `h = M⁻¹ZᵀMZ` is a non-scalar positive cone automorphism (a filter) with `ZhZ = h⁻¹`, scalar
   iff `M` is `Z`-invariant (in Ω_cs, `h = g` exactly); (L-c) compactness modulo scalars forces the scalar case and
   contradicts the Lorentz cone. So central symmetry with strong self-duality (an inner product invariant under the
   reversible transformations, or only under `Z`) gives K∞-Trans; self-duality alone does not. Label: CONJECTURE
   (written proof; exact instances B4, XB1).
4. **Chart dimension 3** (R-E13.4): the question is empty there, a drive alone forcing the ellipsoid (R-E2.6). Label:
   CONJECTURE (as R-E2.6).
5. **Assumption-watch marker (sharpens HO-15's).** Self-duality of the state cone is not a source of K∞-Trans; its
   invariant form is. A proposed OI source of K∞-Trans through self-duality must deliver the invariance of the
   self-dualizing inner product under the body's central symmetry (strong self-duality), not the duality alone.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `c10dbaee` (round-3 commits `44c2708c` … `c10dbaee`) |
| proposal | `research/equivalence/handoff-proposals/HP-9-countermodels-coordinator-selfduality-not-a-source.md`, sha256 `411a6facab6a18624b7da05033253296f6323c2dea63d312e106f1b0c87dc7ef` |
| results, notes | `research/equivalence/RESULTS.md` sha256 `b294cbea4982beb95e0bea4c15a69e49d598db18a6811157ef3872ecbb1587ea` (@ `e2f522d3`; rows R-E13.1 … R-E13.4); `NOTES-E13.md` `cba826faa14dcb9b3e4b811ae4b0da0a4c16fc1f58b4001fd69985001a39c2e2` (§1 Ω⋆, §2 the lemma, §3 Ω_cs) |
| scripts, outputs | `experiments/e13_selfdual_body.py` `fffa8bb38fd5810bad1c6d74617e7ff5bb5e39eae47c05dab6c84962619320b4` / `.out` `a0063f05e6b3d1f998674b24cd5cc1e6e1a1d5476b45f9e5f8c0dcc489466052` (11/11); `experiments/e13b_central_selfdual.py` `c34825609804c1f23ef9ec6d087f3ca3a13bba5a987b7459894c911577eb03f8` / `.out` `24e01a7765d30f927e155136c8311314009cd590766571516e3ff87b7e664fc3` (11/11); both replayed byte-identically |
| design module | none (no kernel module was built for Ω⋆ or Ω_cs) |
| coordinator audit | `indep_checkE3.py` run 2 8/8 — X3 (the AM–GM identity `p³ + 2q³ − 3pq² = (p − q)²(p + 2q)`; nonnegative `M`-pairings on the power cone; an exact outside point with witness pairing `−7/24`; the meridian `x³ = (1 + y)(1 − y)²` is an irreducible cubic, so Ω⋆ is no ellipsoid, the ball's meridian a conic as control; `f″/f = −(2/9)(p + q)²`; the two wrong forms each pair two cone points negatively), X4 (`J₀` on `4u² + v² = 5`; the circle `u² + v² − (1254/325)(u + v) + 5114/845 = 0` through `J₀` and swap `J₀`, tangent at both; the junction slopes `−19/44`, `−44/19`, `−76/11` with `C¹` matching; `M⁻¹ZMZ = g`; fourteen exact arc points whose `M`-poles lie on the dual conic and pair exactly 1; over three periods the minimum pairing exactly 1 with the 97 equalities exactly the polar partners; six points of Γ on no conic; countercontrols XB1, XB2), X8 (swap symmetry; `J₀` self-polar; `F` vanishes on the axes); the self-duality proof of Ω⋆ and L-a/L-b/L-c read: sound — `research/AUDITS/2026-10-11-round3/AUDIT-EQUIVALENCE-R3.md` |

## What the receiving threads may assume

Items 1–5 at their labels. **Countermodels:** Ω_cs as a ready exact object — a self-dual, centrally symmetric,
strictly convex, drivable single-system body with no boundary-transitive family — if a self-dual but non-transitive
single-system body is useful in the composite-cone work; its filter `g = (u/4, 4v)` is explicit, and Ω⋆ is the
strongly self-dual, non-centrally-symmetric companion. **Bridge:** item 3 as the exact obstruction any transfer
argument through self-duality must clear — it must deliver the invariance of the self-dualizing inner product under
the body's central symmetry, not duality alone (item 5).

## What they may not assume

- that Ω⋆ or Ω_cs is kernel-checked: no design module was built (the power cone's self-duality is a two-line
  inequality and kernel-feasible, but not done);
- anything about the bodies OI supplies, or that strong self-duality is sourced by anything at L;
- that the global self-polarity of Ω_cs's chain is more than [W] supported by an exact sample (item 2);
- that the lemma says anything in chart dimension 3 (item 4);
- that draft S4's frozen text is affected: it is unchanged, and an "even with self-duality" extension would need a
  later round with a design module for Ω⋆.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-19 v1` and records in its `LOG.md`
whether and how it relies on it.

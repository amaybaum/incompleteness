# A01: amendment to `PREREG.md` (T1a rule, the J1 coupling, T1b reach, P-C rule and geometry)

**Standing. Plan only. Nothing has been run, and no script exists.** This amendment is
append-only: `PREREG.md` is unchanged. Where they differ, this file governs, for every item it
names. It answers the independent review of `4aea2dd0`
([#1501 c.7064987170](https://github.com/amaybaum/incompleteness/pull/1501#issuecomment-7064987170),
R1 and n4–n5). It was written before any computation, and none is authorized.

## 1. The T1a rule (replaces `PREREG.md` §P-A "Decision rule", first bullet, and K6)

**Why the original rule is void.** By Lemma P4, both end sites of every U₂ line with `k ≥ 3`
sites have trivial shear gates. Each end site then contributes at most 2 configurations of fixed
weight, so the largest orbit has at most `2 · 2 · 4^{k−2} = N/4` points. The frozen rule, "some
orbit contains at least half of the configurations", therefore gave T1a-sub on the whole U₂ line
family before any run. That outcome reflects the frozen-boundary ends and says nothing about
scaling. The rule is withdrawn.

**Replacement statistic.** For each member, `c` and region of size `k`, compare `|O_max(k)|` with
a bound computed in the run from the gate list itself:
- `a_k` is the number of sites whose shear gate is the identity permutation on the region;
- `b_k = k − a_k`;
- `B_k = 2^{a_k} q^{2 b_k}`.

`B_k` is P4(3)'s bound for U₂ and its analogue for every member. A site with a trivial shear gate
is acted on only by `SWAP_i`, whose orbits on the site's `q²` states have at most 2 points.

**Replacement rule.** The verdict text is generated from the table of `|O_max(k)|`, `B_k`, the
orbit ranks, and `1 − 1/|O_max(k)|`.
- **T1a-B** if `|O_max(k)| ≥ B_k / 2` at every computed `k`. No invariant beyond the trivial-site
  weights removes more than half of the bound.
- **T1a-D** otherwise. Some further invariant of the rule cuts the largest orbit below half of
  `B_k` at some computed `k`. The first such `k` is reported.

On U₂'s `Λ₃`, `|O_max| = 16 = B_3` is already known from P4(4). It serves as a calibration point
(K7) and not as evidence: T1a's outcome turns on the computed sizes above `k = 3` and on `Λ₄` and
`Λ₈`. Those regions have no trivial sites, so `B_k = N`, and their fixed points and invariants are
not known in advance.

**Replacement K6.** Both controls must pass before any verdict prints.
- *K6a, which must give T1a-B.* On `n = 2k` bits, with every site declared nontrivial, the CNOTs
  in both directions on each adjacent pair of a path through all the bits. These transvections
  generate `SL(n, 2) = GL(n, 2)`, which is transitive on the `2^n − 1 ≥ B/2` nonzero vectors.
- *K6b, which must give T1a-D.* On `k ≥ 2` two-bit sites, with every site declared nontrivial, the
  gates `SWAP_i` and the swap of `p_i` with `p_{i+1}`. These are bit transpositions along a
  connected graph on the `2k` bits, so they generate every bit permutation and conserve total
  weight. Hence `|O_max| = C(2k, k) < 4^k / 2`, for example `6 < 8` at `k = 2`.

## 2. The J1 coupling (replaces `PREREG.md` §P-A "What is pre-declared", third bullet)

The sentence "A T1a-sub outcome keeps that bound away from 1" is withdrawn. It is false: J1's bound
`1 − 1/|O|` depends on the absolute orbit size, not on the fraction `|O|/N`. An orbit of size
`N/4` grows exponentially with `k`, and the bound then tends to 1.

The replacement: T1a reports `1 − 1/|O_max(k)|` for each computed `k`. J1's bound approaches 1
along a region family iff `|O_max(k)|` is unbounded along it. The bound is attained only given
control on the corresponding `W_O`, which is T1b's question. It concerns flow words on the
register alone (`NOTE.md` §4).

## 3. T1b's reach (n5)

The cap `q^{2k} ≤ 64` stays. Under it T1b covers:
- `Λ₃` for U₂ and for L₂ (`N = 64`);
- nothing nontrivial for `R_4`, since `k = 1` is the only region within the cap and its shear
  gates are trivial.

`R_4` is therefore T1a-only. Raising the cap to `Λ₄` (`N = 256`, with `𝔏 ⊆ u(256)` of dimension
65 536) needs a separate amendment with a resource estimate, and a run outside the local limits of
§A.40.

## 4. P-C: geometry frozen, outcomes exclusive (replaces `PREREG.md` §P-C "Object" and "Decision rule")

**Geometry.** The member is U₂, with `c ∈ {0, 1}`.
- `R₁ = {(0,0,0), (1,0,0), (2,0,0)}`, a line along `x`.
- `R₂ = {(2,1,0), (2,2,0), (2,3,0)}`, a line along `y`.
- The only cross-adjacent pair is `(2,0,0)–(2,1,0)`.
- In each region alone both of these sites are end sites, with `m = 1` and a trivial shear gate.
  In `R = R₁ ∪ R₂` each has `m = 2`, so the coupling makes both shear gates nontrivial.
- `N = 2^{12}`, so T1a only on `R`. `V₁` and `V₂` are the largest unlinked constituents that T1b
  reports for each copy of `Λ₃`.

**Outcomes (exclusive).**
- **PC-P** if `V₁ ⊗ V₂` is invariant under the coupled group `G`.
- **PC-M** otherwise. Report the dimension of `span(G·(V₁ ⊗ V₂))` and the coupled constituents
  it meets.

**PC-L is removed, as vacuous.** The coupled orbits are unions of products of uncoupled orbits, so
each coupled indicator is a sum of product indicators `1_{O₁} ⊗ 1_{O₂}`. `V₁ ⊗ V₂` is orthogonal
to all of them, because `V_i ⊥ 1_{O_i}`. For `g ∈ G` and `v ⊥ 1_O`, `⟨1_O, gv⟩ = ⟨g⁻¹1_O, v⟩ = ⟨1_O, v⟩ = 0`. So no image of `V₁ ⊗ V₂` meets an indicator direction, which is Lemma P1
applied to the coupled group.

**Controls.** These are unchanged from `PREREG.md` §P-C, except that the CNOT-coupling control now
checks PC-M exclusively.

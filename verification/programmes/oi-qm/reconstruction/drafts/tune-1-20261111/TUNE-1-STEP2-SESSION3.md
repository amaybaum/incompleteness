# TUNE-1, Step 2, session 3: the R-lin node (L5/M3), the M3 gap, Lemmas A and F

**WIP / UNVERIFIED research record.** Paper derivation only; no interpreter or numerical
computation was run. No manuscript or Lean file is changed, no premise is adopted, and nothing is
frozen, dispatched or merged. The results go to independent review and then ChatGPT review.

**Authorization.** The owner authorized this work: "Start L5/M3 (Recommended)" (PR #1237 comment
6823860494, `amaybaum`, author association `OWNER`, 2026-11-12T12:40:06Z). It runs under the
existing paper-only authorization. The gate is met: Session 2 was CLEAN at `acf293cc` and ChatGPT
accepted it (same comment).

**Governing text:**
- the proposal at `e676c42a` (sha256 `2a081101…7499fd5`);
- `TUNE-1-STEP2-AMENDMENT-1-final.md`;
- addenda 1 and 2.

Q-conditions are written Q1, Q2, Q3′, Q4, Q5′ and Q6′, and `F(ε; 𝒯′)`, credited assignments and
admissibility are as in the final amendment (B1). Labels are [K], [P], [R] and [W]. Every
derivation here is [W] unless tagged otherwise.

**Controls.** All seventeen M1 controls are green under the governing text (Session 2, and its
C-POS-2 rerun with G1 closed). The proves-too-much row for the L5 argument is in §4.

**Sources** were read on `origin/main` at `0cf85e21`:
- `mechanism-1-20261107/DESIGN.md`:88–102 and :398–440;
- `mechanism-2-20261108/DESIGN.md`:300–348 and :398–450.

Both files are unchanged from the Step 1 pin.

***

## 1. Lemma A, re-derived for TUNE-1 (choice 9(a))

**The source** (MECH-1 :404–430 [R]) is stated under one fixed affine bijection `Φ` of `F_q^N`,
with a setting `c` held in the state at time 0 and the rest of the initial law independent of `c`.
It has three parts:
- (i) every slot is `ℓ(x) + β·c + const`;
- (ii) neither the functional a record registers nor the subspace the records determine depends on
  `c`;
- (iii) `c` acts only by translations and relabelling.

TUNE-1 needs it in four further forms:
- for `V = ℤ/qℤ` with any `q ≥ 2`, not only prime `q`;
- for the second-order rule `Φ_F` of R-lin;
- in both modes;
- on both carriers, with the *law* of the records and not only their values.

The re-derivation below is self-contained and does not rest on the [R] text.

**Lemma 0 (pushforward of a uniform law)** [W].
- *Statement.* Let `h : G → H` be a homomorphism of finite abelian groups and `u` uniform on a
  coset `g₀ + G′` of a subgroup `G′ ≤ G`. Then `h(u)` is uniform on the coset `h(g₀) + h(G′)`.
- *Proof.* Each fibre of `h|_{G′}` over a point of `h(G′)` is a coset of `ker h ∩ G′`, so every
  fibre has the same size. ∎

**Lemma A-T (R-lin record laws are coset-uniform)** [W].

*Setting.* R-lin is `Φ_F(y, x) = (x, A x − y)`, with `A` the nearest-neighbour sum over `V = ℤ/qℤ`.
The law of the unread world is uniform on a coset `u₀ + U′` of a subgroup `U′` of its configuration
group: the uniform law, or on `ℤ^3` the uniform product law.

- (a) **Initial-condition mode.** For a label sequence `c`, the complete record of rounds `1, …, m`
  (`O`'s configuration at every tick) is `h = H_O r_O + H_P c + H_U u`. Here `H_O`, `H_P` and `H_U`
  are group homomorphisms that depend on the rule, the layout and `m`, and not on `c`.
- (b) **Exchange mode, non-adaptive protocols.** The same holds with the label sequence entering
  affinely: an exchange replaces `C`'s content by `c_j`, which is the map
  `x ↦ (I − Π_C) x + ι(c_j)`, and it writes `C`'s previous content into the record. The linear
  parts do not depend on `c`. The record also contains each `c_j`, a homomorphic image of `c`.
- (c) **The law.** In both cases the record law of `c` is uniform on the coset
  `H_O r_O + H_P c + H_U u₀ + S_m`, with `S_m = H_U(U′)`. The subgroup `S_m` does not depend on `c`.
  On `ℤ^3` the record of `m` rounds depends on finitely many sites (range one, finite horizon), so
  the statement holds for the uniform product law restricted to that finite light cone.
- (d) **Dichotomy.** Let `c⁽¹⁾` and `c⁽²⁾` be label sequences that coincide from round `ℓ + 1` on,
  with the same `r_O` and the same layout. Then the laws of the records of rounds `ℓ + 1, …, m`
  under `c⁽¹⁾` and `c⁽²⁾` are uniform on two cosets of one subgroup `π(S_m)`, where `π` is the
  projection onto those rounds. Their total variation is therefore `0` or `1`.

*Proof.*
1. `Φ_F` is a group endomorphism of `(V × V)^Λ`: each component of `F` is a sum of neighbour values,
   and `(y, x) ↦ (x, A x − y)` is additive.
2. The tick map is therefore linear in the whole configuration. In initial-condition mode the
   whole configuration at time 0 is `(r_O, c placed in the blocks, u)`, which gives (a).
3. In exchange mode each round composes an affine exchange, whose linear part `I − Π_C` does not
   depend on `c`, with `τ` linear ticks. The register content moved out is a coordinate of the
   configuration, so it too is a linear function, which gives (b).
4. Lemma 0 applied to `h ↦ H_U u` on `u₀ + U′` gives (c).
5. For (d), the projection `π` is a homomorphism, so by Lemma 0 each marginal is uniform on
   `π(t_i) + π(S_m)`. Two cosets of one subgroup are equal or disjoint. ∎

**Correspondence with the source.**
- (a) and (b) are Lemma A(i): `ℓ(x) + β c + const`.
- `S_m` not depending on `c` is Lemma A(ii).
- The coset translation is Lemma A(iii).

The re-derivation extends Lemma A to every `q`, to the exchange mode, to `ℤ^3`, and to the record
law through Lemma 0.

***

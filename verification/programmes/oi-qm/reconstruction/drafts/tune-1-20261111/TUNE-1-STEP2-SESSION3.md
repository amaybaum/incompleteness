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

## 2. The L5 node tree (M3)

The nodes are decided depth-first by the proposal's decision rule (section 2.2), over green controls.

### Node L5.1: the form of the record laws

The question (proposal M3) asks for the form of the record law of a label sequence, for R-lin
under the uniform law, in initial-condition mode, without heralds. By Lemma A-T (a), (c), it is
uniform on a coset of a subgroup `S_m` that does not depend on the labels, for every `q` and on both
carriers. The same holds for every coset-uniform law and for non-adaptive exchange mode
(Lemma A-T (b)). **Verdict: proved [W].**

### Node L5.2: the M3 gap, closed by the joint-law route

**The gap** (proposal M3). The sketch conditioned on one complete prefix record: a herald whose
`p_acc` can be exponentially small, and which the no-herald subclass cannot use.

**The route.** The argument below conditions on nothing. It compares *marginal* continuation laws
of unheralded preparations of equal length (Lemma A-T (d)). It pads unequal preparations with the
gate `c(0)`, using the credited form of Q3′ (final amendment B1.2–B1.3) to control the padding. The
proposal named this route, and the amended definitions make it run without any `1/p_acc` factor.

**Theorem FC-1** [W]. Fix the rule R-lin (any fixed `q ≥ 2`), a law of the unread world that is
uniform on a coset (H-μ), initial-condition mode, and the carrier: `𝓛_fin`, or `𝓛_∞` under H-∞
with the uniform product law. Inside `𝕀_D`, "uniform on a coset" means the uniform law (the uniform
product law on `ℤ^3`).

No interface of any such family, at any resource, satisfies Q3′, Q5′ and Q6′ together at
`(ε₀, K₀) = (1/50, 3)`, nor at any `ε < 1/48` and `K ≥ 3`, **when Q6′ is witnessed by unheralded
preparations**.

The qualifier restricts how Q6′ is witnessed. It does not restrict which families belong to the
class: a family has no witnesses until a proof supplies them. Only Q6′'s witnesses need be
unheralded. No family of R-lin under the uniform law is ruled out outright. For the family class
(R-lin, uniform law, initial-condition mode) itself, the verdict is `INCONCLUSIVE(L5.4)` (§5). `𝓢₁`
below denotes the case FC-1 covers: these families, with Q6′ witnessed without heralds.

**Proof.** Suppose Q3′, Q5′ and Q6′ hold at `(ε, K)` with `ε < 1/48` and `K ≥ 3`, for a declared
target with reads `a, b`, `a·b ∈ [−½, ½]`.

1. **Witnesses.** By Q6′(i), witnessed without heralds, there are unheralded preparations `P₁`
   and `P₂`, of lengths
   `ℓ₁, ℓ₂ ≤ K − 2`, with assignments credited on `𝒯_L`. Their mean states lie within trace
   distance `ε` of the pure states `ψ₁` and `ψ₂` with Bloch vectors `a` and `b`.
2. **The read test.** Let `T_a` be the single round `c_a`, and `π_i` the world's probability of
   class `a1` in `T_a` after `P_i`. Since `T_a ∈ 𝒯_L` fits, credit gives
   `|π_i − (1 + a·r̄_i)/2| ≤ ε`, and `|a·r̄_i − a·ψ_i| ≤ 2ε`. So `|π_i − (1 + a·ψ_i)/2| ≤ 2ε`.
3. **Padding.** Let `P′_i` be `P_i` followed by `k_i = K − 2 − ℓ_i` rounds of `c(0)`. Both `P′_i`
   have length `K − 2`, are non-adaptive and are unheralded. Let `π′_i` be the class-`a1`
   probability of `T_a` after `P′_i`. This is the class probability of the test
   `(c(0)^{k_i}, T_a)` after `P_i`.
   - `F(ε; 𝒯_K)` (Q3′) gives `P_i` one credited assignment, with mean `r′_i`, for both tests `T_a`
     and `(c(0)^{k_i}, T_a)`. Both fit, since `k_i + 1 ≤ K − ℓ_i`.
   - The target's `c(0)` is `p(0)·Ad 𝟙`, with records independent of the state. So both tests have
     the target class probability `(1 + a·r′_i)/2`.
   - Hence `|π′_i − π_i| ≤ 2ε`, and `|π′_i − (1 + a·ψ_i)/2| ≤ 4ε`.
4. **Lower bound.** Let `W′_i` be the world's law of `T_a`'s records after `P′_i`. Then
   `TV(W′_1, W′_2) ≥ |π′_1 − π′_2| ≥ (1 − a·b)/2 − 8ε ≥ ¼ − 8ε > 0`.
5. **Upper bound.**
   - `F(ε; 𝒯_K)` gives `P′_i`, of length `K − 2 ≤ K − 1`, a credited mean `r″_i` with
     `TV(W′_i, 𝔔*(σ̄″_i · T_a)) ≤ ε`, and so `|π′_i − (1 + a·r″_i)/2| ≤ ε`. Then
     `a·r″_i = a·ψ_i ± 10ε`.
   - The target's Lüders read has record law `p(class) · q_a(h | class)`, so two states' laws on
     `T_a` are at total variation `|a·(r″_1 − r″_2)|/2 ≤ (1 − a·b)/2 + 10ε ≤ ¾ + 10ε`.
   - Hence `TV(W′_1, W′_2) ≤ ¾ + 12ε < 1`.
6. **Contradiction.**
   - `P′_1` and `P′_2` have equal length and are followed by the same label `c_a`.
   - The labels of all later blocks are chosen equal.
   - `r_O` and the layout are the same, since the generating rule fixes them independently of the
     protocol (D1, section 1.2).
   - By Lemma A-T (d), `TV(W′_1, W′_2) ∈ {0, 1}`, which contradicts steps 4 and 5. ∎

**What the proof uses.**
- Lemma A-T (d): the coset dichotomy, which needs R-lin's linearity and a coset-uniform law.
- Q3′, only through `F(ε; 𝒯_K)` on the tests `T_a` and `(c(0)^k, T_a)`.
- Q5′, only through the Lüders read `a` with `a·b ∈ [−½, ½]`.
- Q6′(i), for the two states `a` and `b`, through unheralded witnesses.

It does not use Q1, Q2, Q4, Q6′(ii), `c₀` or the resources. So `ε₀` holds uniformly over the
subclass.

**Verdict L5.2:** proved [W]. The M3 gap is closed for the no-herald subclass; no herald is used
anywhere in the proof.

### Node L5.3 (child): exchange mode, non-adaptive witnesses

In exchange mode under H-write, Lemma A-T (b) gives the coset form for non-adaptive protocols. Each
round's record contains its label `c_j`, which is the same for `P′_1` and `P′_2` in the
continuation. The proof of FC-1 then runs unchanged, provided the Q6′ witnesses and their paddings
are non-adaptive and unheralded.

**Theorem FC-2** [W]. Take the families of FC-1, but in exchange mode under H-write, with Q6′ witnessed by
non-adaptive, unheralded preparations. No interface then satisfies Q3′, Q5′ and Q6′ together at any
`ε < 1/48`, `K ≥ 3`. The qualifier restricts the witnesses, not the class, as in FC-1. **Verdict:
proved [W].**

### Node L5.4 (child): heralded witnesses (open)

Let a herald `E` act on the prefix records.
- Lemma A-T (c) gives that, conditional on one complete prefix record `r`, the continuation law
  is uniform on `t_r + S₀`, where `S₀ = {t : (0, t) ∈ S_m}` is one fixed subgroup.
- A heralded preparation's continuation law is therefore the mixture `Σ_{r∈E} w_r U(t_r + S₀)`:
  a mixture of extreme laws that are pairwise equal or disjoint.
- Two heralded preparations can then be at intermediate total variation, so step 6 of FC-1 does not
  apply.

The restricted record theory is a classical simplex theory whose extreme points the labels
translate. Classical models of one qubit exist (control C-POS-1). Rotations about one axis form an
abelian group, so translations need not exclude an approximate one-axis rotation family. No
argument for or against Q3′, Q5′ and Q6′ together was found.

**Verdict: open.**

**Gap L5.4:** "For R-lin under a coset-uniform law, can a family whose Q6′ witnesses are heralded
meet Q3′, Q5′ and Q6′ together at every `ε`?"

### Node L5.5 (child): adaptive witnesses in exchange mode (open)

An adaptive prefix's joint law is a mixture over record-dependent label sequences, so Lemma A-T (d)
does not apply to its marginal.

**Verdict: open.** **Gap L5.5:** as L5.4, for adaptive witnesses in exchange mode.

### Node L5.6 (child): laws that are not coset-uniform (open)

The level-set law of `E` (SM:296; `𝓛_fin`, exchange mode) and the non-uniform product law are not
uniform on a coset, so Lemma A-T (c) does not apply.

**Verdict: open.** **Gap L5.6:** as FC-1, under each of these laws. The level-set row is "not
defined" in initial-condition mode and on `ℤ^3` (choice 6(iii)).

***

## 3. Lemma F and Theorem U2(ii), re-derived (choice 9(a))

FC-1 and FC-2 do not use Lemma F, so choice 9(a) does not require it for them. It is re-derived
here, as deferred from session 1, for the escape audit L4(a) (proposal M2), which is a necessary
condition on any `PASS-DERIVED`.

**Lemma F** (source: MECH-2 :307–345 [R]; re-derived [W]).

*Hypotheses* (as in the source):
- a fixed bijection `Φ` of a finite configuration set;
- the observer's operations are attaching cells in fixed laws, applying `Φ`, feedback on records,
  marginalization, and conditioning on configuration records;
- H-LIFT;
- an identification `μ ↦ Σ_λ μ(λ) A(λ)` with an orthogonal frame of unit-trace operators.

*Claims.*
- (a) Frame coordinates of reachable encoded states are nonnegative.
- (b) Every branch is a nonnegative matrix on frame coordinates, unique on signed laws.
- (c) Read effects have symbols in `[0, 1]`.

*Proof.*
1. The frame coordinates of an encoded state are the probabilities `μ(λ)`, which gives (a).
2. Each operation acts on laws by a nonnegative matrix:
   - applying `Φ`: a permutation matrix;
   - attaching a cell: tensoring with a fixed law;
   - marginalization: summing coordinates;
   - conditioning on a record value: a `0/1` diagonal.
3. A feedback branch is a product of such matrices chosen by the record values, so it is
   nonnegative.
4. Under H-LIFT, the carrier marginal at each operation's input determines the carrier marginal at
   its output, so the carrier-level branch is one fixed matrix `B`.
5. The identification is injective on signed laws, so `B` is unique, which completes (b).
6. A read effect evaluated at a point law `δ_λ` is a probability, which gives (c). ∎

**U2(ii), the part L4(a) uses** (source: MECH-2 :436–450 [R]; re-derived [W]).
- *Statement.* If a branch acts on the encoded carrier as `p · Ad U`, with `p > 0` independent of
  the input, and the frame is complete (it spans the operator space), then `Ad U` permutes the frame
  points.
- *Proof.*
  1. `M = B/p` represents `Ad U` on all signed laws: valid states span, and the identification is
     injective.
  2. The frame is orthogonal with equal Hilbert–Schmidt norms `κ`, so `‖Σ w_λ A(λ)‖²_HS = κ‖w‖²`.
     `Ad U` preserves the Hilbert–Schmidt norm, so `M` is a real orthogonal matrix.
  3. Its columns are orthonormal with nonnegative entries, so their supports are pairwise disjoint.
     `N` columns with nonempty, pairwise disjoint supports in `N` coordinates each have support one
     coordinate, with entry 1. So `M` is a permutation matrix. ∎
- *Consequence, for exact branches.* Under a fixed injective complete orthogonal frame
  identification with H-LIFT, every branch that acts exactly as `p · Ad U` realizes a permutation
  of the frame points. The exactly realizable encoded unitaries therefore form a finite set, at
  most the number of permutations of the frame. L4(a) stands in this exact form [W].
- *Open: the approximate, operational form.* Two steps are not proved here.
  - An approximate rigidity statement with constants: a nonnegative matrix close to an orthogonal
    one is close to a permutation.
  - A link from the record-level Q3′ (credited, final amendment B1) to "the branch acts on the
    encoded carrier approximately as `p · Ad U`".

  The approximate form of L4(a) is therefore open. FC-1 and FC-2 do not use Lemma F, so no token
  depends on it.
- U2(i), the `A_4 ≀ S_n` classification, is not needed for this and was not re-derived.

***

## 4. Proves-too-much row for the L5 argument (proposal section 3, invariant table)

The property that FC-1 and FC-2 use and that could fail elsewhere is (L-1): the record law of any
unheralded, non-adaptive preparation, followed by a fixed continuation, is uniform on a coset of a
subgroup that does not depend on the labels.

| Case | Does (L-1) hold? | Applies? |
|---|---|---|
| C-POS-1, on its protocol class at `ε = 0` | no: cosine-hemisphere response laws are not coset-uniform | no |
| C-POS-2, separating menus | no: hemisphere-law sampling from fair bits through fixed tables is not coset-uniform | no |
| Reversible deterministic rules, unread uniform environment, every member | no: it fails for nonlinear members (for example the one that hosts C-PROG's controller under `F_U`) | no |

The contradiction in FC-1 step 6 is reached only through (L-1). Without it, intermediate total
variation between `W′_1` and `W′_2` is consistent. So the argument does not prove too much, and the
row is **green**. The other steps (credit, padding, Lüders reads) hold in every case and conclude
nothing on their own.

***

## 5. Tokens and the verdict (proposal section 2.2)

**Step 1.** Every control row is green: the seventeen M1 controls (Session 2) and the L5
proves-too-much row (§4). No row relied on as established has status other than `proved`.

**Step 2.** No `PASS-DERIVED` family is proved.

**Step 3.** `FAIL-CLASS` is proved for proper subclasses, so each is reported with
`INCONCLUSIVE(gap)` for the rest. Every token carries H-μ.

The `FAIL-CLASS` rows hold only when Q6′ is witnessed as stated. The qualifier restricts how Q6′ is
witnessed, not which families belong to the class. For each family class, the verdict is the
`INCONCLUSIVE` row (H1 of the session-3 review). Inside `𝕀_D`, "coset-uniform" means the uniform
law, or the uniform product law on `ℤ^3`.

| Law (choice 6(i)(c)) | Carrier, mode | Token | Hypotheses carried |
|---|---|---|---|
| uniform | `𝓛_fin`, `init` | `FAIL-CLASS(R-lin, 𝓛_fin, uniform law, init, Q6′ witnessed unheralded)` at `(1/50, 3)`, for every `q ≥ 2` | H-μ |
| uniform product | `𝓛_∞`, `init` | `FAIL-CLASS(R-lin, 𝓛_∞, uniform product law, init, Q6′ witnessed unheralded)` at `(1/50, 3)` | H-μ, H-∞ |
| uniform | `𝓛_fin`, `exch` | `FAIL-CLASS(R-lin, 𝓛_fin, uniform law, exch, Q6′ witnessed non-adaptive and unheralded)` at `(1/50, 3)` | H-μ, H-write |
| uniform product | `𝓛_∞`, `exch` | as above on `𝓛_∞` | H-μ, H-∞, H-write |
| uniform: family class (R-lin, uniform, init) | `𝓛_fin` | `INCONCLUSIVE(L5.4: Q6′ witnessed with heralds)` | H-μ |
| uniform product: family class (R-lin, uniform product, init) | `𝓛_∞` | `INCONCLUSIVE(L5.4)` | H-μ, H-∞ |
| uniform: family class (R-lin, uniform, exch) | `𝓛_fin` | `INCONCLUSIVE(L5.4; L5.5: adaptive witnesses)` | H-μ, H-write |
| uniform product: family class (R-lin, uniform product, exch) | `𝓛_∞` | `INCONCLUSIVE(L5.4; L5.5)` | H-μ, H-∞, H-write |
| level-set law | `𝓛_fin`, `exch` | `INCONCLUSIVE(L5.6)` | H-μ, H-write |
| level-set law | `init`; `𝓛_∞` | not defined (choice 6(iii)) | — |
| non-uniform product law | `𝓛_fin`, `init` | `INCONCLUSIVE(L5.6)` | H-μ |
| non-uniform product law | `𝓛_∞`, `init` | `INCONCLUSIVE(L5.6)` | H-μ, H-∞ |
| non-uniform product law | `𝓛_fin`, `exch` | `INCONCLUSIVE(L5.6)` | H-μ, H-write |
| non-uniform product law | `𝓛_∞`, `exch` | `INCONCLUSIVE(L5.6)` | H-μ, H-∞, H-write |

**Restriction F-S3-1** (`TUNE-1-STEP2-SESSION4.md` §1.6). Final B3 poses Q6′ only for
`K ≥ L + 1`, so the four `FAIL-CLASS` tokens above, with `K₀ = 3`, hold for families with `L = 2`
only. Each holds, with its qualifiers as stated, under the further restriction `L ≤ L₀` at
`(1/50, L₀ + 1)`, for every `L₀ ≥ 2`. FC-1, FC-2 and "What the tokens establish" below are read
with `K ≥ L + 1` and that restriction, as stated in Session 4 §1.6. Owner decisions: PR #1237
comments 6825956102 (decision 2; `amaybaum`, 2026-11-12T14:12:24Z) and 6828820114 (decision 2;
`amaybaum`, 2026-11-12T16:05:24Z).

**R-nl** (choice 1(b), a separate verdict under H-nl) has not started. It is the next node.

**What the tokens establish** (proposal section 2.3). Each `FAIL-CLASS` establishes only that its
stated subclass does not reach the target at `(1/50, 3)`. It is not a no-go for:
- heralded or adaptive witnesses (for the family classes the verdict is `INCONCLUSIVE`);
- other laws or other rules;
- R-nl;
- OI generally.

Lemma A-T and FC-1 rest on paper derivations [W] awaiting review; nothing here is kernel-checked.

***

## 6. Pressure test (§A.31)

- **Is FC-1's contradiction an artifact of the amended Q3′?** Padding uses `F(ε; 𝒯_K)` only for
  tests built from `c(0)` and a read. Every passing positive control meets these: C-POS-1 at `0`,
  C-POS-2 at `b + Kg`, and C-SUP-1 at `ε`. The step needs nothing beyond what those controls
  supply.
- **Could equal-length padding be avoided by a family?** Q6′ requires witnesses for `a` and for
  `b`. Padding is a construction inside the proof, not a demand on the family, and `c(0)` exists by
  Q3′.
- **Lemma A-T (d) needs every block after round `ℓ + 1` to carry equal labels.** In initial-condition
  mode the two protocols are free to choose them equal, and they are compared on round `ℓ + 1`
  only. The layout and `r_O` are fixed by the generating rule (D1).
- **Is the coset claim right for composite `q`?** Lemma 0 is stated for any finite abelian group
  and does not use field structure.
- **Is the conclusion stronger than proved?** It is stated for unheralded (FC-1) and for
  non-adaptive unheralded (FC-2) witnesses only. The heralded case is open, with a stated reason it
  may differ (L5.4).

***

## 7. Remaining work, and owner questions

**Remaining work:**
- independent review of §§1–6, then ChatGPT review;
- the R-nl branch under H-nl (choice 1(b));
- gaps L5.4–L5.6, if the owner wants them pursued.

**Owner questions:**
1. After review, should the R-nl branch start (choice 1(b))?
2. Should gaps L5.4 (heralded witnesses) and L5.5 (adaptive witnesses) be pursued on paper, or
   recorded as `INCONCLUSIVE` and left?

***

## 8. Disclosure

- **Commands:** `git` (rev-parse, status, fetch, show, diff, add, commit, push), `curl` (GitHub API
  reads of PR #1237 comments), `cat`, `grep`, `sed`, `cut`, `wc`, `sha256sum`. No interpreter was
  run, and all arithmetic was done by hand.
- **Read:**
  - owner comments 6822861666 and 6823860494;
  - `mechanism-1-20261107/DESIGN.md`:88–102 and :398–440;
  - `mechanism-2-20261108/DESIGN.md`:300–348 and :398–450, on `origin/main`;
  - the governing texts.

## 9. Review disposition (session-3 review, ACCEPT WITH CHANGES)

Each item was checked by hand.

- **H1.** Applied in FC-1, FC-2 and §5. "Unheralded witnesses" restricts how Q6′ is witnessed, not
  which families belong to the class, and only Q6′'s witnesses are restricted. Each family class is
  `INCONCLUSIVE(L5.4)`, with `L5.5` added in exchange mode.
- **H2.** Applied in §3. U2(ii) is re-derived for exact branches only, and L4(a) stands in exact
  form. The approximate rigidity statement and the link to the record-level Q3′ are open. No token
  changes.
- **Minor.** Applied in §5: every `INCONCLUSIVE` row carries H-μ, with H-∞ or H-write where they
  apply, and "coset-uniform" is read inside `𝕀_D` as the uniform law.

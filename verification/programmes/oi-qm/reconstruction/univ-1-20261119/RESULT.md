# UNIV-1: computational universality of the published native update

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form).
Independent non-author review: REVISE at `e4e6c997`
([#1432 c.7025788384](https://github.com/amaybaum/incompleteness/pull/1432#issuecomment-7025788384));
re-review ACCEPT WITH NITS at `74ab936a`
([#1432 c.7025985363](https://github.com/amaybaum/incompleteness/pull/1432#issuecomment-7025985363));
delta CONFIRMED at `ec0101ee`
([#1432 c.7026110454](https://github.com/amaybaum/incompleteness/pull/1432#issuecomment-7026110454)).
This revision answers the required corrections 1–6 of the first review. The record adopts no premise and edits no
manuscript, Lean module or registry. Small exact checks and bounded searches are included (§10).

- **Authorization.** Owner `amaybaum`,
  [#866 c.7023969813](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-7023969813),
  2026-11-19T22:27:33Z: "yes, start UNIV-1". Questions: (1) whether the published native OI update
  is computationally universal, by a positive construction or an obstruction naming the blocking
  invariant; (2) if universal, whether preparation, a ready cell, a record and re-arm can be one
  reversible mechanism satisfying NSC-1..7 apart from a designed initial pattern; (3) its cost
  under PREP-REGRESS-1 and its probability under an untuned law. Limits: "The work is paper-only.
  Small exact checks are allowed. No premise adoption, no manuscript edit, no merge." "An
  independent non-author review is required." "The unit coordinates with NATPREP-1 to avoid
  duplicate work."
- **Goal link (§A.47), from the authorization.** "decide whether the native rule can host the
  apparatus side of measurement as a single construction." Unchanged, as recorded there:
  "Physical measurement sourcing remains NOT PASSED; A1 remains OPEN/UNADOPTED."
- **Accountable Issues.** #866 (native preparation source), #1169 (OI projection objective).
  Predecessor record: DELIVER-1 (#1425).
- **Coordination.** NATPREP-1 (`research/natprep-1-20261119`) treats whether U₂ can prepare
  delivering components from an untuned law. This record treats U₂ only in Corollary 1.3, which
  restates a consequence of DELIVER-1 Theorem 2.2 for universality; its main object is the
  `q = 2^16` member.
- **Snapshot.** `main` at `bae5cfdd80758abe86586f47e18cc478c0e1664a`. `SM:n`, `Main:n` are line
  `n` of `papers/SM.md`, `papers/Main.md`. `DL1` is
  `verification/programmes/oi-qm/reconstruction/deliver-1-20261119/RESULT.md`; `PR1` is
  `verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`.
- **Productivity test (fixed in advance by the assignment).** The unit is a gem iff it gives
  (i) a proved universality obstruction for the published rule, with the invariant identified, or
  (ii) a verified universal gate set in the native rule, or (iii) a verified partial gate set
  together with a precise statement of the missing block. Anything else is relabelling.

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`, cited by its record; nothing built here |
| [P] | manuscript statement |
| [R] | research record on `main`, not independently established |
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/univ_checks.py` (integer arithmetic) |
| [S] | bounded exhaustive search in the same file (`--search`); evidence about the searched set only |
| [LIT2] | literature cited from memory, not re-read; marked where a result depends on it, and given otherwise as background only |

***

## 0. Summary

1. **The rule (§1).** The corpus defines a family: second-order updates
   `x(t+1) = F(x(t)) − x(t−1)` (Main ledger (xiii)). Its manuscript members are the linear rule of
   Main §3.2 (`q = 2`), the exact linear rule of SM §4.2 over `ℤ/q`, and the rounded rule of SM
   §4.2, `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on the representatives `0,…,q−1`, measured
   at `q = 2^16`. Main's own selected model (linearity posit A5, coupling `α`, `α = 1/d` on the
   normalized branch) is a linear member. The member taken here as canonical, by choice, is the
   rounded rule at `q = 2^16` on `ℤ³`, called Q. U₂ is its `q = 2` member.
2. **Node 1, invariants (§2).** Linear members with `q` a prime power and any coupling `α ∈ ℤ/q`
   (including Main §3.2, the exact linear rule at `q = 2^16`, and Main's A5 model with
   `α ≡ 3^{−1} mod 2^16`) are not Turing-universal in Definition U: every halting predicate of the
   form "cell `i₀` ever shows `h`" is decidable (Theorem L [W], with a self-contained proof). U₂ is not
   Turing-universal on finite perturbations of its sixteen parity-uniform backgrounds (Corollary
   1.3, from DL1 Theorem 2.2). Q is nonlinear, and is not an affine cellular automaton under any
   relabelling of its pair alphabet into any abelian group (Proposition 1.4 [W, EC A4]: 196 606
   fixed points on an invariant subgroup). The linear-wave energy is not conserved [EC A5]; support
   closure fails, and the vacuum is explosive (the seeds tested grow at the speed of light [EC C1,
   C2]). No obstruction is found for Q. That branch stays open.
3. **Node 2, building blocks (§3).** On a uniform background `c = 2^15`, Q is exactly the integer
   rule RZ, `y(t+1) = ⌊(Σ_nn y(t) + 1)/3⌋ − y(t−1)`: every RZ orbit with `|y| < 2^15` gives the
   Q orbit `c + y` (Lemma 2.1 [W, EC D1]; one direction only). In RZ, configurations on an
   axis-parallel line with values in `{−1,0,1}` stay on the line (Lemma 2.2).
   Verified in Q: two signal types (W1, W2) that move along pre-laid lines at speed 1/3 in either
   direction [EC E1, E2]; crossing by separation in 3D [EC E4]; memory (isolated trits and finite
   frozen lines, period 4) [EC E3, E6]. Not found: a turn, a two-input gate, fan-out, or a clean
   wire end. A plain corner is not transparent to a signal [EC E5]; corner gadgets for W2
   (729 cases, over a passing background control) and inter-wire bridges (324 cases) give no
   transfer [S1, S2]; a signal at a wire end leaves the line sector [EC E6]. Every verified block
   is non-interacting: transport, storage, and a crossing that is automatic in 3D. **Missing block:** a mechanism that moves a line signal off its line (onto
   a line of another direction or a parallel line, or into a second signal's line), with the line
   sector restored. Turn, gate and fan-out each need it.
4. **Node 3 (§4).** Not reached: universality is not established. Recording and re-arming would
   need the missing block.
5. **Node 4 (§5).** For the blocks found: the full sufficient pin of a designed pattern on the
   light-cone base of one site at time `T` costs `16(|B_T| + |B_{T−1}|)` bits of `D(p₀‖u)`
   (`|B_r| = (2r+1)(2r²+2r+3)/3`). Its probability under the uniform i.i.d. law is
   `2^{−16(|B_T|+|B_{T−1}|)}`; §5 gives the bound for other i.i.d. pair laws. A noisy exterior erodes the background at about the light-cone
   speed [EC C3].
6. **Node 5 (§6).** Universality would at most source apparatus. It would not source amplitudes or
   the Born rule.
7. **Productivity (§8).** Test (iii) is met, thinly: a verified partial set {signal on a wire,
   crossing, memory} in Q, all of it non-interacting, together with the missing block stated in
   item 3. Test (i) is met for the linear members (Theorem L) and for U₂ on finite perturbations.
   It is not met for Q. Test (ii) is not met.

***

## 1. Step 0: the published native update

**Family [P].** Main ledger (xiii) (Main:730): "each site of (viii) carries a previous and a
current value in a finite abelian group, and one step is `x(t+1) = F(x(t)) − x(t−1)`, … the update
displayed in §3.2 being its instance with `q = 2` and `F` the nearest-neighbour sum". The members
stated in manuscripts:

| Member | Source | Definition (quoted) | Linear? |
|---|---|---|---|
| L₂ | Main:292–294 | "`q = 2`, state `(u,v) ∈ 𝔽₂^Λ × 𝔽₂^Λ` and the reversible nearest-neighbour update `u'_x = Σ_{z∼x} u_z + v_x, v'_x = u_x`" | yes (over 𝔽₂) |
| L_q | SM:298 | "The exact finite update `f = Σ_nn x − x(t−1)` over `ℤ/qℤ` is modular-linear" | yes (over `ℤ/q`) |
| L_{q,α} | Main:730 (vii); `papers/Substratum.md:100`, `:159` | Main ledger (vii): "linearity of the substratum update (A5)"; Substratum:159: the selected dynamics "has the form `f = α(x_1 + x_2 + ⋯ + x_{2d}) mod q` with coupling coefficient `α`", which "on the observer-level normalized branch … equals `1/d`" | yes (over `ℤ/q`) |
| R_q | SM:294 | "the rounded bijection `x(t+1) = ⌊(Σ_nn x(t)+1)/3⌋ − x(t−1) mod q`, evaluated on the representatives `0,…,q−1`", measured "at `L = 20`, `q = 2^{16}`" | no (§2.3) |

SM:298 adds: "The floor in the rounded rule above is a different operation, evaluated on the chosen
representatives `0,…,q−1`." On `ℤ³` (or the torus `(ℤ/n)³`), with `N(i)` the six nearest
neighbours, R_q is
```text
x_{t+1}(i) = ⌊(Σ_{j∈N(i)} x_t(j) + 1)/3⌋ − x_{t−1}(i)  mod q,   x ∈ {0,…,q−1},
```
with the sum taken over the integer representatives. The state is the two-slice pair
`(x_{t−1}, x_t)`, and the inverse has the same form, so R_q is a reversible cellular automaton
with alphabet `q²`. #1408 calls R_q "the published rounded recurrence" and uses `q = 2`
(`verification/audits/foundations/p8-p12-rounded-cubic-20261119/RESULT.md:19–27`). That member is
U₂ of DL1 [EC A1]. DL1 §2.4 calls `q = 2^16` "the published `q = 2^16`".

**Canonical member.** The corpus defines a family, indexed by `F` and `q`. SM does not fix `q`
(SM §2.7 states results "for every alphabet size `q ≥ 2`"). Main's ledger designates no rounded
member: the model it selects under posit A5 is the linear L_{q,α}, which Theorem L covers for
prime-power `q` (§2.1). The member taken here as canonical is, by this record's choice,
**Q := R_{2^16} on `ℤ³`**, for three reasons: it is the only nonlinear member stated in a paper,
it is the member measured there, and DL1 leaves it open. The linear members and U₂ are treated
because the assignment asks for their classification (§2.1, §2.2).

*Not in scope.* The native-A update `U_{t+1}(v) = U_{t−1}(v) XOR H(XOR_{w∼v} U_t(w))`,
`H(A,B,D) = (B,D,A XOR BD)`
(`native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md`) belongs to a designed
research construction with `q = 8`. It is not a manuscript rule, and it is not treated here.

***

## 2. Node 1: invariant search

**Definition U (Turing universality, used throughout).** A cellular automaton `F` on `Σ^{ℤ^d}` is
*Turing-universal* if there are a Turing machine `M` with undecidable halting set, a computable map
`w ↦ c(w)` into ultimately periodic configurations (periodic outside a finite set), a site `i₀`
and a symbol `h`, such that `M` halts on `w` iff `F^t(c(w))(i₀) = h` for some `t ≥ 0`. This is one
of the standard forms ([LIT2] Durand–Róka; Ollinger). Halting conditions that read a finite window
are reduced to this form by a product alphabet. When a class of initial configurations is named,
`c(w)` is restricted to that class.

### 2.1 Linear members

*Theorem L [W].* Let `q = p^k` with `p` prime, `α ∈ ℤ/q`, and let `F` be the linear member
`x_{t+1}(i) = α Σ_{j∼i} x_t(j) − x_{t−1}(i) mod q` on `ℤ^d`. This covers L₂ (Main §3.2, `α = 1`,
`q = 2`), L_q (SM:298, `α = 1`) and Main's A5 model with `α ≡ d^{−1}` (for `d = 3`, `q = 2^16`:
`α ≡ 3^{−1}`). For every initial configuration in Definition U's class (a periodic two-slice
configuration changed on a finite set), every site `i₀` and every symbol `h`, the set
`{t ≥ 0 : F^t(c)(i₀) = h}` is the set of `t` whose base-`p` digits a finite automaton accepts, and
that automaton is computable from `c`. Its emptiness is therefore decidable, and `F` is not
Turing-universal in Definition U.

*Proof.* (a) *Rational series.* Let `f` be a finitely supported two-slice configuration, and lift
`α` and its values to integers. Put `W(X,T) = Σ_{t≥0} Σ_i x_t(i) X^i T^t` and
`A = Σ_j (X_j + X_j^{-1})`. The recurrence gives `(1 − αAT + T²) W = x_0 + T(x_1 − αA x_0)` over
`ℤ/q`. The support at time `t` lies within ℓ∞-distance `t + R` of the origin. Substituting
`T ↦ T·X_1⋯X_d` and multiplying by `(X_1⋯X_d)^R` moves the coefficient `x_t(i)` to the exponent
`(i + (t+R)𝟙, t) ≥ 0`. The result is `P/Q₀` in `m = d+1` variables `Y = (X, T)`, with
`P, Q₀ ∈ ℤ[Y]`, `Q₀ = 1 − α Σ_j (X_j² + 1) Π_{k≠j} X_k · T + (X_1⋯X_d)² T²` and `Q₀(0) = 1`.

(b) *Frobenius step.* Over `ℤ`, `Q₀(Y)^p ≡ Q₀(Y^p) (mod p)`, and `a ≡ b (mod p^j)` implies
`a^p ≡ b^p (mod p^{j+1})`. So `S := Q₀^{p^{k−1}}` satisfies `S(Y)^p ≡ S(Y^p) (mod p^k)` [EC L1
checks this identity for the `Q₀` above with `p = 2`]. Hence
`P/Q₀ = G(Y)/S(Y^p)` with `G = P · Q₀^{p^{k−1}−1} · S^{p−1}`.

(c) *Finite kernel.* For `r ∈ {0,…,p−1}^m` let `Λ_r(Σ a_n Y^n) = Σ a_{pn+r} Y^n`. Then
`Λ_r(U(Y) V(Y^p)) = Λ_r(U) · V(Y)`, so `Λ_r(G/S(Y^p)) = Λ_r(G)/S`, and for a polynomial `H`,
`Λ_r(H/S) = Λ_r(H S^{p−1})/S`. If every partial degree of `H` is at most `D` and `D ≥ s`, the
largest partial degree of `S`, then `Λ_r(H S^{p−1})` has partial degrees at most
`(D + (p−1)s)/p ≤ D`. With `D ≥ max(s, deg G)` the finite set
`𝒦 = {G/S(Y^p)} ∪ {H/S : partial degrees of H ≤ D}` (coefficients in `ℤ/q`) is closed under every
`Λ_r`.

(d) *Section.* `x_t(i₀)` is the coefficient of `Y^{t𝟙 + e}` with `𝟙 = (1,…,1) ∈ ℕ^m` and
`e = (i₀ + R𝟙, 0) ≥ 0`. For a series `U` put `b_{U,e}(t) = [Y^{t𝟙+e}] U`. Writing
`r + e_j = p e'_j + r'_j` with `0 ≤ r'_j < p` gives `b_{U,e}(pt + r) = b_{Λ_{r'} U, e'}(t)`. If every
`e_j ≤ E` with `E ≥ 1`, then every `e'_j ≤ E`. So the pairs `(U, e)` with `U ∈ 𝒦` and `e ≤ E`
form a finite, computable set of states, closed under these transitions. Reading the base-`p`
digits of `t` from the least significant, the automaton ends in `(U, e)` and outputs
`[Y^e] U = x_t(i₀)`. Leading zeros do not change the output, since `b_{U,e}(0) = b_{Λ_{r'}U,e'}(0)`
for `r = 0`. Definition U's symbol `h` is a two-slice symbol `(x_{t−1}(i₀), x_t(i₀))`. For `t ≥ 1` this
pair is `(b_e(t−1), b_{e+𝟙}(t−1))`, the output of the product of the automata for the offsets `e`
and `e + 𝟙` read at `t − 1`. The case `t = 0` is read from `c` directly.

(e) *Periodic background.* Write `c = b + f`, with `b` periodic and `f` finitely supported
(difference mod `q`). Linearity gives `F^t(c) = F^t(b) + F^t(f)`. The orbit of `b` lies in the
finite, computable set of configurations with `b`'s periods, so `t ↦ F^t(b)(i₀)` is eventually
periodic with computable preperiod `N` and period `P`. Reading digits from the least significant,
an automaton tracks `t mod P` and `min(t, N)`. The product with the automaton of (d) decides
`F^t(c)(i₀) = h` for a two-slice symbol `h` (each slice by (d), (e) and the product of (d)), and
emptiness is a reachability question. ∎

Scope: Definition U's class (one periodic background plus a finite change). Configurations with
different periodic patterns on different half-spaces, which some definitions of universality
admit, are not covered here. Composite `q` with two distinct prime factors is not covered either.
Background [LIT2]: automaticity of linear cellular automata over `ℤ/p^k` from finite configurations
is known (Allouche–von Haeseler–Peitgen–Skordev 1996, in one dimension). The proof above does not
use it. The checks confirm additivity of L₂, L_{2^16} and L_{2^16, 3^{−1}} on sampled pairs
[EC A2]; additivity of these members also holds by inspection of their update. The classifier of
§7 applies Theorem L only within its scope: a rule of the second-order linear form above, `q` a
prime power, and the sampled additivity test passing.

### 2.2 U₂ on parity-uniform backgrounds

*Corollary 1.3 [W, from DL1 Theorem 2.2 and Lemma 2.3(a)].* For U₂, let `c(w)` range over
configurations that differ from one of the sixteen parity-uniform backgrounds β (DL1 2.1) on a
finite set. Then every predicate of Definition U is decidable. So U₂ is not Turing-universal on
this class.
*Proof.* The perturbation `y = x ⊕ β` solves U₂ (DL1 Lemma 2.1), and its support stays in the
bounding box `D` of its initial support at all times (DL1 Theorem 2.2 and Lemma 2.3(a); on `ℤ³`
every box is closed). The orbit therefore lies in a set of `2^{2|D|}` states. Because the map is a
bijection, the orbit is periodic, and one period decides the predicate. ∎

The invariant is the 2-neighbour closure of the support. Open for U₂: other ultimately periodic
backgrounds, where Theorem 2.2 does not apply. NATPREP-1 treats U₂'s preparation question.

### 2.3 Q: the four invariant classes

- **(a) Linearity.** Q is not additive: `F(z + z) ≠ F(z) + F(z)` for one unit at the origin
  [EC A3]. More strongly:

  *Proposition 1.4 [W, EC A4].* No bijection of the pair alphabet `{0,…,q−1}²` onto an abelian
  group `H` makes Q an affine cellular automaton.
  *Proof.* Let `V₁` be the set of two-slice configurations whose slices both have period 4 along
  `e₁`, are constant along `e₂` and `e₃`, and are invariant under `i₁ ↦ 1 − i₁`. A slice then has
  the form `(a, a, b, b)` along `e₁`. Q commutes with translations and with that reflection, so
  `V₁` is invariant. Under any sitewise bijection the image of `V₁` is again the set of
  `H`-configurations with these symmetries, a finite subgroup of order a power of 2
  (`|H| = 2^{32}`). An affine map `w ↦ Lw + e` that preserves a finite subgroup `W` restricts to an
  affine map of `W` (`e = F(0) ∈ W`). Its fixed points form either the empty set or a coset of
  `ker(L − I)|_W`, so their number is 0 or a power of 2. For Q, a fixed point is `x_{t−1} = x_t`
  with `⌊(S+1)/3⌋ ≡ 2x`. On `V₁` an `a`-site has neighbour sum `5a + b`, and the count is
  **196 606 = 2 · 98 303** [EC A4]. That is neither 0 nor a power of 2. ∎

  Countercontrol: L_{2^16} has 8 fixed points on `V₁` [EC A4b]. (The period-(2,1,1) class gives
  65 536 for Q, which does not discriminate.)
- **(b) Conserved quantities.** The quadratic energy of the linear wave with coupling 1/3,
  `E = Σ y_t² + Σ y_{t−1}² − ⅓ Σ_i y_t(i) Σ_{j∼i} y_{t−1}(j)`, goes from 4 to 6 in one step from a
  single seed 2 in RZ [EC A5]. A wider search for local conserved densities was not made, since
  the alphabet is `2^{32}`. A conserved quantity would not by itself block universality: the
  billiard-ball countercontrol conserves particle number and is classified universal (§7).
- **(c) Support closure.** It fails. A symbol 2 in the vacuum reaches all six neighbours in one
  step [EC C1, as DL1 E8]. A seed `(0, 1)` at the origin has support radius `t − 2` for
  `3 ≤ t ≤ 20` [EC C2]. In the seeds tested the vacuum 0 is explosive: a value `−1` is represented as `q − 1`, and its
  neighbours receive `≈ q/3` (the boundary crossings of SM:294).
- **(d) Light cone and permutation structure.** The rule is reversible, with radius 1 and the cubic
  symmetry. Neither property blocks universality: the countercontrol has both.

**Verdict, node 1.** Linear members with `q` a prime power and any coupling: obstruction
(Theorem L), with additivity as the invariant. U₂: obstruction on finite perturbations of parity-uniform
backgrounds (Corollary 1.3), with the closure invariant. Q: no obstruction found. The branch stays
open, and node 2 proceeds.

***

## 3. Node 2: building blocks in Q

**Lemma 2.1 (mid-alphabet embedding) [W, EC D1].** Let `c ∈ {0,…,q−1}`, and let `y_t` be integer
configurations with `0 ≤ c + y_t(i) < q` for all `i` and all `t ∈ [−1, T]`. If `y` is an RZ-orbit
on `[−1, T]`, then `x_t = c + y_t` is the Q-orbit on `[−1, T]`. The converse fails: with all six
neighbours at `y = 2^15 − 1` and `y_{t−1} = −2^15`, Q's next representative is `c + 32766`, inside
the window, while RZ gives `98302` (from the review).
*Proof.* On representatives `S = 6c + Σ y`, and `⌊(6c + Σy + 1)/3⌋ = 2c + ⌊(Σy + 1)/3⌋` since
`3 | 6c`. So `x_{t+1} ≡ c + (⌊(Σ y_t + 1)/3⌋ − y_{t−1}) (mod q)`. When the RZ value `y_{t+1}`
satisfies `c + y_{t+1} ∈ [0, q)`, that is the representative. ∎ Only this direction is used below. With `c = 2^15` the window is
`|y| < 2^15`. All constructions below use `c = 2^15`. On the vacuum `c = 0` the same pattern leaves
the line [EC E1b].

**Properties of RZ.** `G(s) = ⌊(s+1)/3⌋` is the nearest integer to `s/3` and is odd. `G(s) = 0`
iff `|s| ≤ 1`. A site whose neighbour sum stays in `{−1,0,1}` evolves as `y_{t+1} = −y_{t−1}`.

**Lemma 2.2 (line sector) [W].** Let `ℓ` be an axis-parallel lattice line. If an RZ configuration is
zero off `ℓ` and takes values in `{−1,0,1}` on `ℓ` at times `t−1` and `t`, then at time `t+1` it is
zero off `ℓ`. On `ℓ` it follows the one-dimensional rule
`y_{t+1}(k) = ⌊(y_t(k−1) + y_t(k+1) + 1)/3⌋ − y_{t−1}(k)`.
*Proof.* A site off `ℓ` has at most one neighbour on `ℓ`, so `|s| ≤ 1`, `G = 0`, and its previous
value is 0. A site on `ℓ` has exactly two neighbours on `ℓ`. ∎ The lemma applies for as long as the
values stay in `{−1,0,1}`. Each check below tests that condition at every tick.

| Block | Status | Evidence |
|---|---|---|
| **Signal on a wire, W1** | verified in Q | Line `ℓ = ℤe₁`. Background: previous slice `−1` on odd sites, current slice 0 on even sites (a uniform period-6 oscillation, `(a,b) ↦ (b, b−a)`). Signal: previous `+1` at `o+3`; current `−1` at `o+2`, `+1` at `o+4`. It shifts by +2 every 6 ticks; off-line sites stay at `c`; `|y| ≤ 1`; 60 ticks on a ring of 60 [EC E1]. The mirror image moves by −2. Because the state on the ring returns translated after 6 ticks, and the ring (60) is longer than the defect window plus the 6-tick light cone on both sides, the ring and the infinite line agree on every backward cone, and induction carries the translation to all times on the line. On an open line (background on 400 sites, no periodic closure) the translation holds for 120 ticks at every site farther than 120 from the segment ends, for W1 and W2 [EC E2b]. Finite W1 segments leave the line sector [EC E6a], so W1 needs an unbounded line. |
| **Signal on a wire, W2** | verified in Q | Staggered background: both slices `(−1, 1, −1, 1, …)` on their parity sites. Every line site then has neighbour sum 0, and the background is frozen with period 4. Signal: the window `(−1,−1,−1,1 | −1,−1,−1,1)` (odd previous \| even current). It satisfies `y(t+3) = −shift_{−1} y(t)`, i.e. speed 1/3, for 60 ticks [EC E2]. Finite W2 segments are frozen [EC E6]. |
| **Crossing** | verified (3D) | A W1 wire along `e₁` at `z = 0` (signal from `x = 8` to `x = 38`) and a W2 wire along `e₂` at `x = 24`, `z = 3` (signal from `y = 4` through `y = 0`), so both signals traverse the crossing. In Q the joint evolution is the superposition of the two solo evolutions for 90 ticks, with values in `{c−1, c, c+1}`. Countercontrol: at separation `z = 2` the site `(24, 0, 1)` neighbours both wires and superposition fails at `t = 3` [EC E4]. In general, axis lines with no common neighbour evolve independently. |
| **Memory** | verified in Q | An isolated site `(a, b) ∈ {−1,0,1}²` runs `(a,b) → (b,−a) → (−a,−b) → (−b,a)` and leaves its neighbours at `c`. A finite frozen line `(−1,1)/(0,0)`, or a finite W2 segment, stores one trit per site with period 4 [EC E3, E6]. |
| **Turn** | not found | A plain 90° corner of a W2 loop is transparent to the background but not to the signal (first deviation from the 1D reference at `t = 16`). A plain corner of a W1 loop leaks at `t = 2` from the background alone [EC E5], so W1 corners cannot be tested in a loop of plain corners and were not searched. Mechanism: the inner-corner site has the same two path neighbours as the corner site, so it is kicked whenever the corner is kicked. W2 gadgets of three sites (inner corner and two outer sites), two-slice values in `{−1,0,1}`, 729 cases. The background control (no gadget, no signal) passes; the plain corner with the signal fails; no gadget passes [S1]. "Passes" means: the undelayed, unsigned 1D-ring evolution is reproduced at every path site farther than 4 from the gadget corner for 90 ticks, with all values in `{−1,0,1}`. A turn that delays the signal or changes its sign or type would count as a failure. |
| **Two-input gate** | not found | Two parallel W2 wires at `y = 0` and `y = 3` (the second negated) and a two-site bridge at one of four positions, 81 value choices each [S2]. 308 bridges disturb the wires, 12 leave `{−1,0,1}` (not classified further), and 4 have no effect on the second wire (what they do to the signal on the first wire is not checked). None transfers a signal. |
| **Fan-out** | not found | Needs the missing transfer (below). |
| **Wire end** | not clean | A W2 signal that reaches a segment end leaves the line sector (`t = 47–56` for four end positions) [EC E6]. |
| **Free signals** | none found | RZ vacuum seeds in `2×1×1` and `3×1×1` boxes with values in `{−1,0,1}`: 520 oscillators, 288 growing, no glider at horizon 40 [S3]. The line sector on the zero line, windows of width 10: no moving localized pattern [S4]. |

**The missing block.** Every signal found moves along a pre-laid straight line, and every
interaction tried that moves it off the line leaves the ternary sector, disturbs the line, or has
no effect on a second line (S1: no W2 gadget passes; S2: 308 bridges disturb the wires, 12 leave the
ternary sector, 4 have no effect on the second wire).
Turn, gate input coupling and fan-out all require a **controlled transfer of a line signal off its
line, with the line sector restored**. No verified instance exists. Universality by the standard
route needs this block, and the searches cover only the stated small sets (ternary values, gadgets
of at most three sites, one bridge geometry; horizons 90 ticks in S1, 72 in S2, 40 in S3, 60 in
S4). Absence is not shown. The missing block sits exactly where Lemma 2.2 stops applying: at any
junction, some off-line site has two line neighbours.

**Verdict, node 2.** Partial set verified in the published rule: signals on wires (two types),
crossing, memory. Every one of these blocks is non-interacting. Missing: off-line transfer, and
with it turn, gate and fan-out. The positive
branch is neither closed nor established.

***

## 4. Node 3: integrated apparatus (not reached)

Node 3 applies only if Q is universal, and that is not established. What the integrated mechanism
would require is recorded here, with nothing claimed:
- **Exception, stated as required.** Every block in §3 starts from a designed initial pattern: the
  background `c = 2^15` on a region, the pre-laid lines, and the signal windows. Under NSC-3
  ("a newly tuned prepared producer state") and NSC-5 none of them is an independently justified
  supply. An integrated construction would carry the same exception.
- **DT⁺(R).** DL1's delivery task with record formation (R) needs a use of the carrier followed by
  a log that did not hold the result before the use. In §3's set, a signal can be delivered along a
  line to a fixed site: unlike U₂, carriers approach (contrast DL1 2.3(c)). Writing a record of it
  into a separate block, however, needs an interaction between two lines, which is the missing
  block. Re-arming reversibly needs the same.
- **NSC-7.** "Ready" (a known value on designated cells) is available as frozen memory
  (E3, E6). Request and record are not available without the missing block.

***

## 5. Node 4: cost and probability of the blocks found

- **Light-cone sufficiency [W].** The radius is 1 and the rule is second order, so the state of a
  site at time `T` is a function of the time-0 slice on `B_T` and the time-(−1) slice on
  `B_{T−1}`, where `B_r` is the ℓ¹-ball of radius `r`, `|B_r| = (2r+1)(2r²+2r+3)/3`. Pinning that
  base to the designed pattern is sufficient for an exact run.
- **Cost [W].** A deterministic pin of `m` site-slices (each a symbol of `ℤ/2^16`) has
  `D(p_{0,B} ‖ u_B) = 16m` bits. The full sufficient pin for one site at time `T` therefore costs
  `16(|B_T| + |B_{T−1}|)` bits; for `T = 10`, `16·(1561 + 1159) = 43 520` bits. PR1 2.5–2.6 give
  the lower bound `(N+1)(1 − h₂(ε))` bits in the cone base for `N` held records and a ready cell.
  The sufficient pin exceeds that bound by orders of magnitude, so PR1's bound is far from tight
  for these constructions.
- **Probability.** The pin fixes both slices on `B_{T−1}` and the current slice alone on
  `B_T ∖ B_{T−1}`. Under an i.i.d. law with pair marginal π on two-slice site states and current-slice
  marginal π₀, its probability is
  `∏_{i∈B_{T−1}} π(w_i) · ∏_{i∈B_T∖B_{T−1}} π₀(w_i) ≤ π_max^{|B_{T−1}|} · π₀,max^{|B_T|−|B_{T−1}|}`.
  For the uniform law this equals `2^{−32|B_{T−1}| − 16(|B_T| − |B_{T−1}|)} = 2^{−D}` with
  `D = 16(|B_T| + |B_{T−1}|)` (`2^{−43 520}` at `T = 10`).
- **Is the pin needed? [EC C3, one instance].** A slab `|x₁ − 24| ≤ 12` held at `c` inside uniform
  noise first deviates on its centre plane at `t = 15`. That plane is 13 sites from the noise, and
  13 is the light-cone bound. In this instance, then, the noise reaches the interior within two
  ticks of the light cone. Necessity of the full pin is not proved.

***

## 6. Node 5: boundary

Even a universal Q would at most source apparatus: preparation, control, memory and records as
classical configurations of the substratum. A substratum programmed to simulate quantum mechanics
would carry amplitudes and the Born rule as data of the program. It would not derive them.
Nothing here bears on amplitudes, on the Born rule, or on the quantum equivalence. What this record
can source at most, given §3, is classical memory and signal transport along designed lines.
Unchanged, as recorded by the owner: physical measurement sourcing "NOT PASSED", A1
"OPEN/UNADOPTED".

***

## 7. Controls

| Control | Check | Verdict |
|---|---|---|
| S⇔D⇔Q_fb, `finite_horizon_equivalence` [K, as cited in PR1] | Concerns representability of supplied finite-horizon laws. Nothing here restricts or extends it. | untouched |
| DL1 Theorem 2.2, Lemma 2.3, 2.3(c), 2.4 [R] | Used for Corollary 1.3 at its scope (U₂, parity-uniform backgrounds). C1 reproduces DL1 E8. §3 answers DL1's open item for `q = 2^16` only partly: carriers can move (W1, W2), along designed lines. | preserved at its scope |
| PR1 2.1–2.6, NSC-1..7 [R] | Used in §5 as bounds and in §4 as the exclusion list. No new bound is claimed. | unchanged |
| #1408, #1412 (`q = 2`) [R] | Not used beyond A1 (U₂ is the `q = 2` member). | untouched |
| SM:294 numerics [P] | Concern uniformly random states. §3's structures live on a designed background, where Lemma 2.1 removes boundary crossings. C3 shows that noise erodes that background. | consistent |
| Countercontrol: linear rule | L₂, L_{2^16} and L_{2^16, 3^{−1}} pass the additivity test [EC A2], with a power-of-2 fixed-point count [EC A4b]. Given that computed result, the classifier returns "not universal (Theorem L)" [EC F2]. | passes |
| Countercontrol: billiard-ball block rule | The Margolus partition rule (one particle moves to the opposite corner, a diagonal pair rotates, every other block is unchanged), implemented exactly. Verified: a diagonal glider; the interaction-gate truth table (A∧¬B, ¬A∧B, A∧B, A∧B at four output cells); fan-out with B = 1 (A, A, ¬A); a 90° turn by collision with a supplied constant particle, and 180° reflection at a wall. The turn used here is collision-based. It is not the fixed-mirror turn of the literature. A collision turn with a constant input is legitimate in conservative logic, and the same reading was applied to Q (S2); memory (a particle between two walls returns after 18 ticks); a timed crossing [EC F1]. The classifier returns "universal (all blocks verified)" [EC F2]. That this rule is Margolus's BBMCA, and that these blocks compose to universality (Fredkin–Toffoli conservative logic, Margolus 1984), is [LIT2]. | passes |
| Q under the same classifier | Additivity test fails (A3); blocks computed from E1–E6 and, with `--search`, S1–S2: wire, crossing, memory. Fan-out has no test in Q and counts as not verified. Returns "undecided; missing turn, gate, fanout". | as reported |

The classifier is: additive, of the second-order linear form and with `q` a prime power ⇒
"not universal (Theorem L)"; additive outside that scope ⇒ not classified; otherwise all of {wire,
turn, crossing, gate, fan-out, memory} verified ⇒ "universal"; otherwise "undecided" with the
missing list. Every
input is a value computed by the checks: the additivity tests and the block checks. None is
hard-coded. The "universal" branch rests on the composition theorem [LIT2]; the "not universal"
branch rests on Theorem L.

***

## 8. Productivity verdict and classification

- **Test (iii): met, thinly.** In Q (via Lemma 2.1), a verified partial set: signals on wires (W1,
  W2), crossing, memory. Every verified block is non-interacting: transport, storage, and a crossing
  that is automatic in 3D. No verified block makes two signals act on each other. The missing block
  is stated precisely: off-line transfer of a line signal with the line sector restored, which turn,
  gate and fan-out all require. Its negative evidence rests on the W2 corners (S1, E5) and on the
  bridges (S2).
- **Test (i): met for the linear members** (Theorem L, any coupling, `q` a prime power, Definition U)
  **and for U₂ on finite perturbations of parity-uniform backgrounds** (Corollary 1.3).
  Not met for Q.
- **Test (ii): not met.**

Verdict: gem by (iii).

**Pressure test (maximum skepticism on the branch favouring the framework, §A.31).**
1. The signals exist only on pre-laid designed lines inside a designed uniform background `c`. W1
   needs an unbounded line. Neither is a structure an untuned law produces (§5).
2. Exactness rests on Lemma 2.1 and on the ternary condition being met at every tick. Every check
   tests both, and no rounding or wrap-around enters.
3. A moving defect is a carrier of one bit (present or absent). It is not computation. Without the
   missing block the set computes nothing beyond transport and storage.
4. The negative searches are small: ternary values, gadgets of at most three sites, one bridge
   geometry. They are evidence about those sets only.

| Item | Class |
|---|---|
| Lemma 2.1 (mid-alphabet embedding); Lemma 2.2; W1, W2 signals in Q; finite W2 segments as memory | NEW at this scope (author; awaiting review) |
| Proposition 1.4 (Q not affine under any relabelling) | NEW, minor |
| Theorem L (linear members, any coupling) | ELABORATING (known in the literature; self-contained proof here) |
| Corollary 1.3 (U₂) | ELABORATING (DL1 Theorem 2.2) |
| E5, E6, S1–S4 | record-only negative evidence |
| Countercontrols F1, F2 | CONFIRMING (criteria calibrated) |

- **AW-UNIV-1 (vacuum versus background).** In Q the vacuum 0 sits at the alphabet boundary and is
  explosive, while a mid-alphabet uniform background is exactly RZ and supports memory and moving
  signals. A statement about "the `q = 2^16` rule" is a statement about a stated background: DL1's
  E8 and SM:294 concern the vacuum and uniform random states respectively.
- **AW-UNIV-2 (approach).** In U₂ no carrier approaches a block (DL1 2.3(c)). In Q, carriers move
  along designed lines. A delivery construction at `q = 2^16` is therefore not excluded by DL1's
  mechanism, and its remaining obstacle is the missing off-line transfer, not transport.
- **Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached.

***

## 9. What review must check; limits; literature

- Proposition 1.4: that `V₁` is invariant and is mapped to a subgroup by every sitewise bijection;
  that an affine map preserving a finite subgroup restricts to it; and the count 196 606 (A4
  enumerates `a` and solves for `b`; review may re-count by an independent method).
- Theorem L: the Frobenius step (b), the degree bound in (c), the offset bound in (d), and the
  product automaton in (e).
- Lemma 2.1 (the `3 | 6c` step; one direction) and Lemma 2.2 (no off-line site has two neighbours
  on an axis line).
- E1/E2: the ring-length condition. E4: the separation-3 superposition and the separation-2
  countercontrol.
- S1: the background control and the pass criterion (undelayed, unsigned).
- The countercontrol: that the implemented block rule matches the cited model, and that "turn by
  collision with a supplied constant" is the right reading of a turn for that model. The same
  reading was applied to Q, where no collision-based transfer was found either (S2).
- Not done: no Lean; no literature re-read; no search beyond the stated sets; no study of other
  backgrounds of U₂ (NATPREP-1) or of non-uniform backgrounds of Q.

[LIT2], background only, no result here depends on it: G. Christol, Theoret. Comput. Sci. 9
(1979) 141–145; O. Salon, C. R. Acad. Sci. Paris Sér. I 305 (1987) 501–504; J. Denef and
L. Lipshitz, J. Number Theory 26 (1987) 46–67; J.-P. Allouche, F. von Haeseler, H.-O. Peitgen and G. Skordev, Discrete Appl. Math. 66 (1996)
1–22 (linear cellular automata and automaticity); B. Durand and Zs. Róka, in *Cellular Automata*
(Kluwer, 1999), on definitions of universality; N. Ollinger, "Universalities in cellular
automata", *Handbook of Natural Computing* (Springer, 2012); E. Fredkin and T. Toffoli, Int. J.
Theor. Phys. 21 (1982) 219–253 [the composition theorem used by the classifier's "universal" branch];
N. Margolus, Physica D 10 (1984) 81–95; T. Toffoli and
N. Margolus, *Cellular Automata Machines* (MIT Press, 1987).

***

## 10. Exact checks

`checks/univ_checks.py`. From this directory: `python3 -I checks/univ_checks.py` (a few seconds),
or `python3 -I checks/univ_checks.py --search` to add S1–S4 (about 90 seconds). The exit status is
0 iff every check holds. All lattice arithmetic is on integers.

| Check | Statement tested |
|---|---|
| A1 | the `q = 2` member of R_q is U₂ |
| A2 | L₂, L_{2^16} and L_{2^16, 3^{−1}} pass the additivity test (10 random pairs each on `4³`) |
| L1, L1b | Theorem L (b): `S(Y)² ≡ S(Y²) mod 2^k` for the `Q₀` of (a) (`d = 1`, `k ≤ 4`; `d = 3`, `k ≤ 2`; `α = 1, 3^{−1}`); countercontrol: without the lift (`S = Q₀`) it fails mod `2^k` for `k ≥ 2`, and the lifted `S` fails mod `2^{k+1}` |
| A3 | Q violates additivity (one-site witness; random-pair test fails) |
| A4, A4b | fixed points on `V₁`: Q 196 606; L_{2^16} 8 |
| A5 | linear-wave energy 4 → 6 under RZ |
| C1, C2 | vacuum: one-step reach of a symbol 2; light-cone growth of a seed `(0,1)` (`n = 48`) |
| C3 | mid-background slab in uniform noise: centre plane first deviates at `t = 15` (one seeded instance) |
| D1 | Lemma 2.1 (forward direction) on five random configurations, 30 ticks |
| E1, E1b | W1 in Q (60 ticks); countercontrol on the vacuum 0 |
| E2, E2b | W2 in Q (60 ticks); W1 and W2 on open lines (120 ticks, interior) |
| E3 | memory: isolated trits; frozen staggered line |
| E4 | crossing in Q with both signals traversing it: separation 3 superposes (90 ticks); separation 2 fails at `t = 3` |
| E5 | plain corners: first deviation times (none, 2, 16) |
| E6a, E6 | finite W1 segments leave the line sector; finite W2 segments frozen; W2 signal at an end leaves the sector |
| F1, F2 | billiard-ball countercontrol blocks and additivity; classifier outcomes for the linear rule, the billiard-ball rule and Q, on computed inputs |
| S1–S4 (`--search`) | W2 corner gadgets with background control (90 ticks); bridges (72); RZ vacuum seeds (40); line sector on the zero line (60) |

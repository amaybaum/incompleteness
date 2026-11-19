# UNIV-1: computational universality of the published native update

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form).
No independent review yet; one is required by the authorization. The record adopts no premise and
edits no manuscript, Lean module or registry. Small exact checks are included (§9).

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
| [LIT2] | literature cited from memory, not re-read; marked where a result depends on it |

***

## 0. Summary

1. **The rule (§1).** The corpus defines a family: second-order updates
   `x(t+1) = F(x(t)) − x(t−1)` (Main ledger (xiii)). Its manuscript members are the linear rule of
   Main §3.2 (`q = 2`), the exact linear rule of SM §4.2 over `ℤ/q`, and the rounded rule of SM
   §4.2, `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on the representatives `0,…,q−1`, measured
   at `q = 2^16`. The canonical member taken here is the rounded rule at `q = 2^16` on `ℤ³`,
   called Q. U₂ is its `q = 2` member.
2. **Node 1, invariants (§2).** Linear members with `q` a prime power (including Main §3.2 and the
   exact linear rule at `q = 2^16`) are not Turing-universal in Definition U: every halting
   predicate of the form "cell 0 ever shows `h`" is decidable (Theorem L [W, LIT2]). U₂ is not
   Turing-universal on finite perturbations of its sixteen parity-uniform backgrounds (Corollary
   1.3, from DL1 Theorem 2.2). Q is nonlinear, and is not an affine cellular automaton under any
   relabelling of its pair alphabet into any abelian group (Proposition 1.4 [W, EC A4]: 196 606
   fixed points on an invariant subgroup). The linear-wave energy is not conserved [EC A5]; support
   closure fails, and the vacuum is explosive (finite seeds grow at the speed of light [EC C1,
   C2]). No obstruction is found for Q. That branch stays open.
3. **Node 2, building blocks (§3).** On a uniform background `c = 2^15`, Q is exactly the integer
   rule RZ, `y(t+1) = ⌊(Σ_nn y(t) + 1)/3⌋ − y(t−1)`, while `|y| < 2^15` (Lemma 2.1 [W, EC D1]).
   In RZ, configurations on a straight line with values in `{−1,0,1}` stay on the line (Lemma 2.2).
   Verified in Q: two signal types (W1, W2) that move along pre-laid lines at speed 1/3 in either
   direction [EC E1, E2]; crossing by separation in 3D [EC E4]; memory (isolated trits and finite
   frozen lines, period 4) [EC E3, E6]. Not found: a turn, a two-input gate, fan-out, or a clean
   wire end. A plain corner is not transparent to a signal [EC E5]; corner gadgets (1458 cases)
   and inter-wire bridges (324 cases) give no transfer [S1, S2]; a signal at a wire end leaves the
   line sector [EC E6]. **Missing block:** a mechanism that moves a line signal off its line (onto
   a line of another direction or a parallel line, or into a second signal's line), with the line
   sector restored. Turn, gate and fan-out each need it.
4. **Node 3 (§4).** Not reached: universality is not established. Recording and re-arming would
   need the missing block.
5. **Node 4 (§5).** For the blocks found: a designed pattern pinned on its light-cone base costs
   `16(|B_T| + |B_{T−1}|)` bits of `D(p₀‖u)` for a read after `T` ticks
   (`|B_r| = (2r+1)(2r²+2r+3)/3`). Its probability under the uniform i.i.d. law is
   `2^{−16(|B_T|+|B_{T−1}|)}`. A noisy exterior erodes the background at about the light-cone
   speed [EC C3].
6. **Node 5 (§6).** Universality would at most source apparatus. It would not source amplitudes or
   the Born rule.
7. **Productivity (§8).** Test (iii) is met: a verified partial set {signal on a wire, crossing,
   memory} in Q, together with the missing block stated in item 3. Test (i) is met for the linear
   members (conditional on the cited theorems) and for U₂ on finite perturbations. It is not met
   for Q. Test (ii) is not met.

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
(SM §2.7 states results "for every alphabet size `q ≥ 2`"). The member taken here is
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

*Theorem L [W, LIT2].* Let `q = p^k` with `p` prime, and let `F` be L_q on `ℤ^d` (so L₂ when
`q = 2`). For every ultimately periodic two-slice initial configuration `c`, every site `i₀` and
every symbol `h`, the set `{t ≥ 0 : F^t(c)(i₀) = h}` is `p`-automatic, and an automaton for it can
be computed from `c`. So emptiness is decidable, and `F` is not Turing-universal in Definition U.

*Proof.* (a) Finite perturbation of zero. Put `W(X,T) = Σ_{t≥0} Σ_i x_t(i) X^i T^t` with
`A = Σ_j (X_j + X_j^{-1})`. The recurrence `x_{t+1} = A x_t − x_{t−1}` gives
`(1 − AT + T²) W = x_0 + T(x_1 − A x_0)`. The support at time `t` lies within distance `t + R` of
the origin, so substituting `T ↦ T·X_1⋯X_d` and multiplying by `(X_1⋯X_d)^R` gives a series with
non-negative exponents. That series equals `P/Q₀`, with `P, Q₀` integer polynomials and
`Q₀(0) = 1`. It is therefore algebraic over `ℤ_p`, and by Denef–Lipshitz [LIT2] its coefficients
modulo `p^k` form a `p`-automatic `(d+1)`-dimensional array. (For `k = 1`, Christol–Salon [LIT2].)
The set `{t : x_t(i₀) = h}` is first-order definable from that array in `(ℕ, +, V_p)`. Such sets
are `p`-automatic, effectively (Bruyère–Hansel–Michaux–Villemaire [LIT2]). (b) Ultimately periodic
`c`. Write `c = b + f`, with `b` periodic and `f` finitely supported (difference mod `q`).
Linearity gives `F^t(c) = F^t(b) + F^t(f)`. The orbit of `b` lies in the finite set of
configurations with `b`'s periods, so `t ↦ F^t(b)(i₀)` is eventually periodic. The sum of an
eventually periodic sequence and a `p`-automatic sequence is `p`-automatic. ∎

Scope: `q` a prime power. Composite `q` with two distinct prime factors is not covered. The checks
confirm additivity of L₂ and L_{2^16} [EC A2]. The classifier of §7 uses Theorem L for any
additive member.

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
  `3 ≤ t ≤ 20` [EC C2]. The vacuum 0 is explosive: a value `−1` is represented as `q − 1`, and its
  neighbours receive `≈ q/3` (the boundary crossings of SM:294).
- **(d) Light cone and permutation structure.** The rule is reversible, with radius 1 and the cubic
  symmetry. Neither property blocks universality: the countercontrol has both.

**Verdict, node 1.** Linear members with `q` a prime power: obstruction (Theorem L), conditional on
the cited automaticity theorems. U₂: obstruction on finite perturbations of parity-uniform
backgrounds (Corollary 1.3), with the closure invariant. Q: no obstruction found. The branch stays
open, and node 2 proceeds.

***

## 3. Node 2: building blocks in Q

**Lemma 2.1 (mid-alphabet embedding) [W, EC D1].** Let `c ∈ {0,…,q−1}`, and let `y_t` be integer
configurations with `0 ≤ c + y_t(i) < q` for all `i` and all `t ∈ [−1, T]`. Then `x_t = c + y_t`
is the Q-orbit on `[−1, T]` iff `y` is an RZ-orbit there.
*Proof.* On representatives `S = 6c + Σ y`, and `⌊(6c + Σy + 1)/3⌋ = 2c + ⌊(Σy + 1)/3⌋` since
`3 | 6c`. So `x_{t+1} ≡ c + (⌊(Σ y_t + 1)/3⌋ − y_{t−1}) (mod q)`, and the representative equals
`c + y_{t+1}` when that value lies in `[0, q)`. ∎ With `c = 2^15` the window is
`|y| < 2^15`. All constructions below use `c = 2^15`. On the vacuum `c = 0` the same pattern leaves
the line [EC E1b].

**Properties of RZ.** `G(s) = ⌊(s+1)/3⌋` is the nearest integer to `s/3` and is odd. `G(s) = 0`
iff `|s| ≤ 1`. A site whose neighbour sum stays in `{−1,0,1}` evolves as `y_{t+1} = −y_{t−1}`.

**Lemma 2.2 (line sector) [W].** Let `ℓ` be a straight lattice line. If an RZ configuration is
zero off `ℓ` and takes values in `{−1,0,1}` on `ℓ` at times `t−1` and `t`, then at time `t+1` it is
zero off `ℓ`. On `ℓ` it follows the one-dimensional rule
`y_{t+1}(k) = ⌊(y_t(k−1) + y_t(k+1) + 1)/3⌋ − y_{t−1}(k)`.
*Proof.* A site off `ℓ` has at most one neighbour on `ℓ`, so `|s| ≤ 1`, `G = 0`, and its previous
value is 0. A site on `ℓ` has exactly two neighbours on `ℓ`. ∎ The lemma applies for as long as the
values stay in `{−1,0,1}`. Each check below tests that condition at every tick.

| Block | Status | Evidence |
|---|---|---|
| **Signal on a wire, W1** | verified in Q | Line `ℓ = ℤe₁`. Background: previous slice `−1` on odd sites, current slice 0 on even sites (a uniform period-6 oscillation, `(a,b) ↦ (b, b−a)`). Signal: previous `+1` at `o+3`; current `−1` at `o+2`, `+1` at `o+4`. It shifts by +2 every 6 ticks; off-line sites stay at `c`; `|y| ≤ 1`; 60 ticks on a ring of 60 [EC E1]. The mirror image moves by −2. Because the state on the ring returns translated, the orbit is periodic, and by locality the same holds on the infinite line. Finite W1 segments leave the line sector [EC E6a], so W1 needs an unbounded line. |
| **Signal on a wire, W2** | verified in Q | Staggered background: both slices `(−1, 1, −1, 1, …)` on their parity sites. Every line site then has neighbour sum 0, and the background is frozen with period 4. Signal: the window `(−1,−1,−1,1 | −1,−1,−1,1)` (odd previous \| even current). It satisfies `y(t+3) = −shift_{−1} y(t)`, i.e. speed 1/3, for 60 ticks [EC E2]. Finite W2 segments are frozen [EC E6]. |
| **Crossing** | verified (3D) | A W1 wire along `e₁` at `z = 0` and a W2 wire along `e₂` at `z = 3`, both carrying signals. The joint evolution equals the sum of the separate ones for 60 ticks [EC E4]. In general, lines with no common neighbour evolve independently: at every site at most one of the two contributes to the neighbour sum. |
| **Memory** | verified in Q | An isolated site `(a, b) ∈ {−1,0,1}²` runs `(a,b) → (b,−a) → (−a,−b) → (−b,a)` and leaves its neighbours at `c`. A finite frozen line `(−1,1)/(0,0)`, or a finite W2 segment, stores one trit per site with period 4 [EC E3, E6]. |
| **Turn** | not found | A plain 90° corner of a W2 loop is transparent to the background but not to the signal (first deviation from the 1D reference at `t = 16`). A plain corner of a W1 loop leaks at `t = 2` [EC E5]. Mechanism: the inner-corner site has the same two path neighbours as the corner site, so it is kicked whenever the corner is kicked. Gadgets of three sites (inner corner and two outer sites), with two-slice values in `{−1,0,1}`: 729 per signal type, none passes the signal with the line sector intact [S1]. |
| **Two-input gate** | not found | Two parallel W2 wires at `y = 0` and `y = 3` (the second negated) and a two-site bridge at one of four positions, 81 value choices each [S2]. 308 bridges disturb the wires, 12 leave `{−1,0,1}` (not classified further), and 4 pass the signal without affecting the second wire. None transfers a signal. |
| **Fan-out** | not found | Needs the missing transfer (below). |
| **Wire end** | not clean | A W2 signal that reaches a segment end leaves the line sector (`t = 47–56` for four end positions) [EC E6]. |
| **Free signals** | none found | RZ vacuum seeds in `2×1×1` and `3×1×1` boxes with values in `{−1,0,1}`: 520 oscillators, 288 growing, no glider at horizon 40 [S3]. The line sector on the zero line, windows of width 10: no moving localized pattern [S4]. |

**The missing block.** Every signal found moves along a pre-laid straight line, and every
interaction tried that moves it off the line either leaves the ternary sector or does nothing.
Turn, gate input coupling and fan-out all require a **controlled transfer of a line signal off its
line, with the line sector restored**. No verified instance exists. Universality by the standard
route needs this block, and the searches cover only the stated small sets (ternary values, gadgets
of at most three sites, horizons of 72–90 ticks). Absence is not shown.

**Verdict, node 2.** Partial set verified in the published rule: signals on wires (two types),
crossing, memory. Missing: off-line transfer, and with it turn, gate and fan-out. The positive
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
  `D(p_{0,B} ‖ u_B) = 16m` bits, so reading one site after `T` ticks costs `16(|B_T| + |B_{T−1}|)` bits. For `T = 10` that
  is `16·(1561 + 1159) = 43 520` bits. PR1 2.5–2.6 give the lower bound
  `(N+1)(1 − h₂(ε))` bits in the cone base for `N` held records and a ready cell. The designed
  pattern exceeds that bound by orders of magnitude, so the binding constraint here is the
  probability of the pattern, not the budget.
- **Probability.** Under the uniform i.i.d. law on two-slice site states, the pinned base has
  probability `2^{−16(|B_T|+|B_{T−1}|)}` (`2^{−43 520}` at `T = 10`). Under an untuned i.i.d. law
  with site marginal π, it is `∏ π(pattern) ≤ π_max^{|B_T|+|B_{T−1}|}`.
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
| Countercontrol: linear rule | L₂ and L_{2^16} are additive [EC A2], with a power-of-2 fixed-point count [EC A4b]. The classifier returns "not universal (Theorem L)" [EC F2]. | passes |
| Countercontrol: billiard-ball block rule | The Margolus partition rule (one particle moves to the opposite corner, a diagonal pair rotates, every other block is unchanged), implemented exactly. Verified: a diagonal glider; the interaction-gate truth table (A∧¬B, ¬A∧B, A∧B, A∧B at four output cells); fan-out with B = 1 (A, A, ¬A); a 90° turn by collision with a supplied constant particle, and 180° reflection at a wall; memory (a particle between two walls returns after 18 ticks); a timed crossing [EC F1]. The classifier returns "universal (all blocks verified)" [EC F2]. That this rule is Margolus's BBMCA, and that these blocks compose to universality (Fredkin–Toffoli conservative logic, Margolus 1984), is [LIT2]. | passes |
| Q under the same classifier | Non-affine (A3, A4). Blocks: wire, crossing, memory. Returns "undecided; missing turn, gate, fanout". | as reported |

The classifier is: additive ⇒ "not universal (Theorem L)"; otherwise all of {wire, turn, crossing,
gate, fan-out, memory} verified ⇒ "universal"; otherwise "undecided" with the missing list. Its
"universal" branch rests on the composition theorem [LIT2]. Its "not universal" branch rests on
Theorem L.

***

## 8. Productivity verdict and classification

- **Test (iii): met.** In Q (via Lemma 2.1), a verified partial set: signals on wires (W1, W2),
  crossing, memory. The missing block is stated precisely: off-line transfer of a line signal with
  the line sector restored, which turn, gate and fan-out all require.
- **Test (i): met for the linear members** (Theorem L, conditional on the cited automaticity
  theorems) **and for U₂ on finite perturbations of parity-uniform backgrounds** (Corollary 1.3).
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
| Theorem L (linear members) | ELABORATING (application of literature [LIT2]) |
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
- Theorem L: the reduction to rational generating functions, the use of Denef–Lipshitz for
  `q = p^k`, and that definability in `(ℕ, +, V_p)` gives decidability. All literature is [LIT2].
- Lemma 2.1 (the `3 | 6c` step and the window) and Lemma 2.2 (no off-line site has two line
  neighbours).
- E1/E2: that periodic return on a ring implies the same orbit on the infinite line. E4: that
  separation 3 leaves no site adjacent to both wires.
- The countercontrol: that the implemented block rule matches the cited model, and that "turn by
  collision with a supplied constant" is the right reading of a turn for that model. The same
  reading was applied to Q, where no collision-based transfer was found either (S2).
- Not done: no Lean; no literature re-read; no search beyond the stated sets; no study of other
  backgrounds of U₂ (NATPREP-1) or of non-uniform backgrounds of Q.

[LIT2] G. Christol, Theoret. Comput. Sci. 9 (1979) 141–145; O. Salon, C. R. Acad. Sci. Paris
Sér. I 305 (1987) 501–504; J. Denef and L. Lipshitz, J. Number Theory 26 (1987) 46–67;
V. Bruyère, G. Hansel, C. Michaux and R. Villemaire, Bull. Belg. Math. Soc. 1 (1994) 191–238;
J.-P. Allouche, F. von Haeseler, H.-O. Peitgen and G. Skordev, Discrete Appl. Math. 66 (1996)
1–22 (linear cellular automata and automaticity); B. Durand and Zs. Róka, in *Cellular Automata*
(Kluwer, 1999), on definitions of universality; N. Ollinger, "Universalities in cellular
automata", *Handbook of Natural Computing* (Springer, 2012); E. Fredkin and T. Toffoli, Int. J.
Theor. Phys. 21 (1982) 219–253; N. Margolus, Physica D 10 (1984) 81–95; T. Toffoli and
N. Margolus, *Cellular Automata Machines* (MIT Press, 1987).

***

## 10. Exact checks

`checks/univ_checks.py`. From this directory: `python3 -I checks/univ_checks.py` (a few seconds),
or `python3 -I checks/univ_checks.py --search` to add S1–S4 (about 90 seconds). The exit status is
0 iff every check holds. All lattice arithmetic is on integers.

| Check | Statement tested |
|---|---|
| A1 | the `q = 2` member of R_q is U₂ |
| A2 | L₂ and L_{2^16} are additive (20 random pairs on `4³`) |
| A3 | Q violates additivity (one-site witness) |
| A4, A4b | fixed points on `V₁`: Q 196 606; L_{2^16} 8 |
| A5 | linear-wave energy 4 → 6 under RZ |
| C1, C2 | vacuum: one-step reach of a symbol 2; light-cone growth of a seed `(0,1)` (`n = 48`) |
| C3 | mid-background slab in uniform noise: centre plane first deviates at `t = 15` (one seeded instance) |
| D1 | Lemma 2.1 on five random configurations, 30 ticks |
| E1, E1b | W1 in Q (60 ticks); countercontrol on the vacuum 0 |
| E2 | W2 in Q (60 ticks) |
| E3 | memory: isolated trits; frozen staggered line |
| E4 | crossing at separation 3 (60 ticks) |
| E5 | plain corners: first deviation times (none, 2, 16) |
| E6a, E6 | finite W1 segments leave the line sector; finite W2 segments frozen; W2 signal at an end leaves the sector |
| F1, F2 | billiard-ball countercontrol blocks; classifier outcomes for the linear rule, the billiard-ball rule and Q |
| S1–S4 (`--search`) | corner gadgets; bridges; RZ vacuum seeds; line sector on the zero line |

# NATIVE-UNIV, step 1: feasibility of universal computation in OI's native rule

**Standing.** Writer's research record for Issue #1461, order step 1 (feasibility) only.
Independent non-author review at `f87afd04`: REVISE
([#1489 c.7064054072](https://github.com/amaybaum/incompleteness/pull/1489#issuecomment-7064054072)),
mathematics confirmed; its items R1–R3 and N1–N5 are answered in . Delta re-review at
: CONFIRMED WITH NITS
([#1489 c.7064102580](https://github.com/amaybaum/incompleteness/pull/1489#issuecomment-7064102580));
its nits n1–n3 are applied. No construction attempt (step 2 is not authorized), no manuscript, Lean or
registry edit, no premise adoption. One small exact check (§3.1, §7), preregistered in `PREREG.md`
before the script was written.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7063843557](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7063843557):
  NATIVE-UNIV as research only. PM-D3, PM-D4 and PM-D5 (#1454) remain paused; nothing here is
  PM-D5 work.
- **Owner requirements followed.**
  [#1461 c.7045565729](https://github.com/amaybaum/incompleteness/issues/1461#issuecomment-7045565729)
  (the actual published rule and its alphabet; bounded experiments kept apart from proofs; success
  only with encoding, construction and correctness argument) and
  [#1461 c.7047109654](https://github.com/amaybaum/incompleteness/issues/1461#issuecomment-7047109654)
  (Goals A, B, C kept distinct; the literature checks on Margolus and Morita–Harao; a known
  universal rule is a comparison model only).
- **Open prerequisite question (for the owner).** #1461's planning table lists the PM-D5
  feasibility study (#1454) as a prerequisite, and PM-D5 is paused. This record does not resolve
  that; it proceeds with order step 1 only, as instructed, and records the question in §6.
- **Snapshot.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`. `Main:n`, `SM:n`, `Sub:n`
  are line `n` of `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md` at that commit.
  Predecessors on `main`, under `verification/programmes/oi-qm/reconstruction/`: UNIV-1
  `univ-1-20261119/` (U1), UNIV-2 `univ-2-20261120/` (U2), MEAS-Q `meas-q-20261120/` (MQ); and
  POSIT-MIN `verification/audits/foundations/posit-min-20261120/` (PM). Their results are used at
  the standing they state and are not redone.

| Label | Meaning |
|---|---|
| [P] | manuscript statement or published reproduction code |
| [K] | Lean definition on `main`, cited; nothing built here |
| [R] | research record on `main`, at its stated review standing |
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/nu_checks.py`; evidence about the sampled instances only |
| [LIT-R] | literature whose cited passage was read in the source for this record |
| [LIT-B] | literature located by its bibliographic record or abstract only; the cited result is as the abstract states it; background |
| [LIT2] | literature from memory, not re-located; background only |

***

## 0. Summary

1. **F1, the rule.** The corpus fixes a *family*, not one rule: the second-order form
   `x(t+1) = F(x(t)) − x(t−1)` over a finite abelian group (Main ledger (xiii)), with nearest-neighbour
   range on the reference class (x) and no self-term (xi). Its only nonlinear manuscript member is
   the rounded rule `R_q`: `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on representatives
   `0,…,q−1`, on `ℤ³` (SM:294). The corpus does not fix `q`: SM measures `R_q` at `q = 2^16`, the
   published reproduction code also runs `q = 64` and `q = 256`, and SM's cycle censuses use
   `q = 2, 3`. U1's canonical member Q = `R_{2^16}` on `ℤ³` is a choice of that record. Which
   `(q, d)` is "the actual published rule and its fixed alphabet" is an owner decision (§6).
2. **F2, literature.** Universality *is* known for rules of the exact second-order form
   `c(t+1) = f(c(t)) − c(t−1) mod q`: Margolus (1984), Appendix A, gives a two-dimensional,
   three-state, second-order rule that he states is computation-universal [LIT-R]. That rule's `f`
   reads the 3×3 neighbourhood including the centre cell, so it lies outside the narrow class (§3.1), which
   reads only the 2d nearest neighbours and has no self-term (§2, §3.2). Morita–Harao (1989) prove
   universality of one-dimensional reversible CAs through partitioned CAs, with an alphabet that
   depends on the simulated reversible Turing machine [LIT-B]. No published result was found that
   proves or excludes universality for a second-order rule with nearest-neighbour, no-self-term
   coupling on `ℤ^d` at any fixed alphabet. Margolus (1984, p. 84, footnote) already states the
   sublattice decoupling for rules that ignore the centre cell [LIT-R].
3. **F3, structure.**
   - *Component lemma [W, EC].* Every rule whose `F_i` reads only the nearest neighbours at every
     state and has no self-term splits on `ℤ^d` into two independent components. Ledger (x) states
     the range only on the reference class, so this is the *narrow class*; the members of §1 are in
     it. The decoupling itself is Margolus's (1984, p. 84, footnote). Each component is a
     *staggered involution rule*: on alternate half-steps one sublattice is updated by
     `y(i) ← F_i(y|N(i)) − y(i)` while the other is held. This generalizes U2 A1 from Q to the
     whole narrow class. The `q = 2` members are exactly the class of Vichniac's Q2R Ising automaton;
     OI's `q = 2`, `d = 3` rounded member U₂ is the staggered rule "flip iff the neighbour sum is
     2, 3 or 4" [EC C5].
   - *Linearity.* Linear members with prime-power `q` are not universal in Definition U
     (U1 Theorem L) [R]. Q is not affine under any relabelling (U1 Prop. 1.4) [R].
   - *Conserved quantities.* No nontrivial density of U2's template is conserved star by star
     (U2 A2) [R]. A conserved quantity would not by itself block universality (the billiard-ball
     control conserves particle number).
   - *Confinement.* On a uniform background `c`, MQ2(b) [R] keeps closed classes at ℓ1-distance
     at least 3 isolated while no boundary-layer value leaves `[c−1, c+1]` (a *breach*); MQ3 is
     its corollary for carrier use. This obstructs interaction between classes at ℓ1-distance at
     least 3 without a breach. It does not obstruct a turn or gate inside one
     closed class.
   - *No controlled turn.* Not found in U1 S1 and U2 F1–F3 (bounded negatives); every quiescent
     U2 gadget radiates when the signal arrives.
4. **F4, verdict.** Goal A as posed is answered at sketch level; the narrow class and Q are open,
   each with a decisive next question.
   - *Architecture (Goal A, as posed in c.7047109654: second-order form mod `q`, finite
     alphabet, local translation-commuting coupling).* Answered positively at the standing of
     Margolus's construction (1984, Appendix A): `q = 3`, `d = 2`, a 3×3 neighbourhood with the
     centre, a sketch-level reduction to the BBM with undefined cases left free.
   - *Narrow class (nearest neighbours at every state, no self-term).* Open: neither a universal
     member nor an obstruction is known.
   - *The native rule (Goal B).* Obstructed for linear members with prime-power `q`, and for U₂
     on finite perturbations of parity-uniform backgrounds (U1). Open for Q.
   - *Decisive question for Q.* Is there a *bounded breach*: a finite closed gadget on a uniform
     background whose boundary layer leaves `[c−1, c+1]` only transiently and returns to it without
     radiation, giving a controlled transfer of a signal? Or is there a proof that every breach of
     the isolated dynamics grows without bound?
   - *For the alphabet question.* At `q = 2^16` the alphabet size is not what the question turns
     on, and minimal-alphabet results for other rules do not bear on it. At `q = 2` it does, and no
     result is known for that class either.

***

## 1. F1: the exact native rule

**The family [P].** Main:736, ledger item (xiii): "each site of (viii) carries a previous and a
current value in a finite abelian group, and one step is `x(t+1) = F(x(t)) − x(t−1)`, in phase-space
form `(x(t−1), x(t)) ↦ (x(t), F(x(t)) − x(t−1))`, with each `F_i` reading the current values at
finitely many sites and each site read by finitely many `F_i` (kernel: `ruleDynamics` in
`OIBridge/SecondOrderDrive.lean`)". The Lean structure is `Rule` (an `F`, a read set `N i` and an
influence set) in `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean:198–203`, and the
reversible dynamics is `ruleDynamics` in `verification/lean-mathlib/OIBridge/SecondOrderDrive.lean:339–342` [K].
Further ledger constraints on `F`, all at Main:736:
- (vii) linearity (A5);
- (x) nearest-neighbour range "on the reference vacuum/uniform state class";
- (xi) centre independence, whose second clause states that "the update at a site contains no
  explicit copy of that site's present value".

**Members stated in manuscripts** (U1 §1 table, re-located at this snapshot):

| Member | Source | Rule | Alphabet / dimension stated |
|---|---|---|---|
| L₂ | Main:294 | `u'_x = Σ_{z∼x} u_z + v_x`, `v'_x = u_x` over `𝔽₂` | `q = 2`, lattice `Λ` |
| L_q | SM:298 | "`f = Σ_nn x − x(t−1)` over `ℤ/qℤ` is modular-linear" | `q` unspecified |
| L_{q,α} | Sub:159 | `f = α(x_1 + ⋯ + x_{2d}) mod q`, `α = 1/d` on the normalized branch | `q`, `d` unspecified |
| R_q | SM:294 | "the rounded bijection `x(t+1)=⌊(Σ_nn x(t)+1)/3⌋−x(t−1) mod q`, evaluated on the representatives `0,…,q−1`", measured "at `L=20`, `q=2^{16}`" | `q = 2^16` measured; `q = 2, 3` in cycle censuses at `L = 2`; `d = 3` (six neighbours, divisor 3) |

**Published code [P].** `papers/main_repro/lyapunov_v3.py:16–19`: `q = 1 << 16` on a `20³` torus,
`step(cur, prv) = (((nn(cur)+1)//3) - prv) % q`, with `nn` the sum over the six axis neighbours.
The countercontrol in the same file uses `q = 256`. `papers/main_repro/mixing_battery.py:4–6` runs
the same `step_round` at `q = 64`. The code calls it "a rounded candidate map" (`lyapunov_v3.py:2`).

**What is fixed and what is not.**
- *Fixed:* the second-order form; `d = 3` for `R_q` (the divisor 3 and the six-neighbour sum); `F`
  totalistic (a function of the neighbour sum on representatives), cubic-symmetric, with nearest
  neighbours and no self-term; the floor on representatives `0,…,q−1` (SM:298: "a different
  operation" from the modular-linear update).
- *Not fixed:* `q`. The manuscripts state no single alphabet for the native rule. `q = 2^16` is
  the measured value of SM:294, and U1 took Q = `R_{2^16}` on `ℤ³` as canonical "by this record's
  choice" (U1 §1). This record keeps U1's choice for Goal B and treats U₂ = `R_2` where the
  predecessors did. The owner decision in §6 item 2 asks which is meant.
- *Main's selected model is linear.* Main's own selected model under A5 is a linear member, which
  Theorem L covers for prime-power `q` (U1 §2.1). PM recommends FLAG for A5 and places `R_q` in
  its class R_res (PM §0 item 4). Neither changes the rule.

***

## 2. F2: literature

Proved results and constructions are separated. "Universal" means each source's own notion. Margolus
and Morita–Ueno argue universality by simulating a universal logic element (the billiard-ball model,
the Fredkin gate) in infinite configurations. Morita–Harao simulate reversible Turing machines.
Neither notion is checked here against U1's Definition U, which restricts to ultimately periodic
configurations.

| Source | Object | Form | Alphabet, neighbourhood, dimension | What is shown | Bearing on OI |
|---|---|---|---|---|---|
| Margolus 1984, Physica D 10, 81–95, eq. (4) and the text around it [LIT-R] | the general second-order scheme | `c_{i,t+1} = f(c_{{i},t}) − c_{i,t−1}` mod the number of cell values (his eq. (4)), "any `f` at all will do" for reversibility; attributed to Fredkin | any | reversibility for every `f`; "Such rules can be universal (I give an example in the appendix)" | this is exactly ledger (xiii) |
| Margolus 1984, Appendix A, "A second-order, reversible, universal automaton" [LIT-R] | a BBM-type second-order rule | `c_{x,y,t+1} = f(c_{{x,y},t}) − c_{x,y,t−1}`, "'−' is taken mod 3" | 3 states (`−1, 0, +1`); `f` "'looks' at the 3 × 3 neighbourhood with `c_{x,y,t}` as its center cell"; `d = 2` | a construction: balls on diagonals, mirrors, attractive collisions; `f` is defined only on the cases a BBM circuit uses, and "each choice for these undefined cases defines a distinct universal RCA". The correctness argument is the reduction to Fredkin's BBM, given at sketch level with figures | the form matches OI; the neighbourhood does not: it reads diagonals (outside (x)) and, as stated, the centre (outside (xi), second clause). The OCR text does not show whether the rule tables actually depend on the centre value |
| Margolus 1984, §8 [LIT-R] | BBMCA | partitioned (2×2 blocks, alternating grids) | 2 states, 4-cell block | universal via BBM; a direct "change the center cell" BBM rule would need "6 states per cell, and a 17 cell neighbourhood" | not second-order; a comparison model only. U1 F1 implements it as a countercontrol |
| Toffoli–Margolus 1990, Physica D 45, 229–253, §5.4 [LIT-R] | second-order technique | eq. (15) `q_i^{t+1} = f q_{i+X}^t − q_i^{t−1}`; eq. (17) as an ordinary CA on `A × A` | any | from any CA one obtains an invertible second-order CA; the historical section recalls Toffoli's 1977 embedding theorem and Morita–Harao | confirms the form; no universality result for a restricted neighbourhood |
| Toffoli 1977, JCSS 15, 213–231 [LIT-B, via the 1990 review] | reversible CAs | general (not second-order) | `d + 1` dimensions to embed a `d`-dimensional CA | proved: computation- and construction-universal reversible CAs exist (every universal `d`-dimensional CA embeds in a reversible `(d+1)`-dimensional one) | existence for reversible CAs in `d ≥ 2`; neighbourhood and form not OI's |
| Morita–Harao 1989, Trans. IEICE E72(6), 758–762 [LIT-B] | one-dimensional reversible CAs | via 1-D partitioned CAs (PCA), in which local injectivity equals global reversibility | 3-neighbour (radius 1); the state set depends on the simulated reversible TM | proved: 1-D reversible CAs are computation-universal (answers Toffoli's question) | partitioned, not second-order; no fixed alphabet |
| Morita–Ueno 1992, IEICE Trans. Inf. & Syst. E75-D(1), 141–147 [LIT-B] | 2-D reversible PCAs | partitioned | 16 states | construction: Fredkin gate realized, hence universal | partitioned; comparison only |
| Morita 2007, J. Cellular Automata 2 [LIT-B] | 1-D reversible CAs | partitioned | 36 states (infinite configurations, cyclic tag systems); 98 states (finite configurations, with halting) | construction | same |
| Durand-Lose 1997, STACS, LNCS 1200, 439–450 [LIT-B] | 1-D reversible CAs | partitioned | — | an intrinsically universal 1-D reversible CA | notion stronger than computation universality |
| Kari 1996, Math. Systems Theory 29, 47–61; Durand-Lose 2001, DMTCS [LIT-B] | all reversible CAs | block permutations | — | every `d`-dimensional reversible CA is a composition of block permutations (`d + 1` of them in Durand-Lose 2001) | a possible route to a Goal-A comparison model: §3.1's half-steps are block permutations of a special kind (§5 P1) |
| Goles, Montalva-Medel, Montealegre, Ríos-Wilson 2021, arXiv:2108.03335 [LIT-B] | generalized Q2R automaton | staggered involution (Q2R class, §3.1) | `q = 2`, networks | P-hardness of predicting whether a node changes; the abstract makes no universality claim | the only located complexity result on OI's `q = 2` class; P-hardness is not universality |
| Vivaldi and co-workers, rounded rotations (e.g. Reeve-Black and Vivaldi) [LIT-B] | the single-site map `x_{t+1} = ⌊λ x_t⌋ − x_{t−1}` and relatives | second-order, rounded | integers, no space | conjectured: all orbits periodic for `|λ| < 2`; proved for a few `λ` only | the zero-dimensional analogue of `R_q`'s rounding (RZ). Its near-integrability is background for why moving structures in RZ are scarce; it is not a result about the lattice rule |

**Answers to the sub-questions of c.7047109654.**
- *Margolus.* He does give a universal reversible CA in exactly the second-order form (Appendix A).
  The billiard-ball CA of §8 is a separate, partitioned scheme. The second-order example has
  `q = 3` and `d = 2`, and its `f` reads the 3×3 neighbourhood with the centre.
- *Morita–Harao.* Their construction uses partitioned CAs, 3-neighbour in 1-D, with an alphabet
  that grows with the simulated reversible Turing machine. It is not second-order and fixes no
  alphabet. Fixed small alphabets come later (Morita 2007: 36 and 98 states), still partitioned.
- *Fixed alphabet and dimension.* For Goal A's architecture as posed (local,
  translation-commuting coupling), Margolus App. A is a positive answer at `q = 3`, `d = 2`. For
  the narrow neighbourhood (2d nearest neighbours, no self-term, second-order), no source found decides whether a universal rule exists at any `q`. The known
  constructions use either a larger neighbourhood with a self-read (Margolus App. A), a
  partitioned scheme (BBMCA, Morita), or an extra dimension (Toffoli 1977).

Not done: a systematic survey beyond these sources. A result on the narrow class may exist that was
not located. Sources to read first for a broader survey [LIT2]: Toffoli and Margolus, *Cellular
Automata Machines* (MIT Press, 1987), on second-order rules and Q2R; J. Kari's survey of reversible
cellular automata (2018); K. Morita, *Theory of Reversible Computing* (Springer, 2017). The
reviewer's search also found no result deciding the narrow class.

***

## 3. F3: structural obstructions and enablers

### 3.1 Component lemma (the narrow class)

*Prior art.* Part (a) is stated by Margolus (1984, p. 84, footnote) [LIT-R]: "An extreme instance
of 'decoupling' of entire regions occurs with any rule that doesn't depend on the center cell, but
depends on its nearest neighbours", after which "the system decouples into two entirely independent
(but interleaved) sub-lattices". The sublattice split is also standard for Q2R [LIT2]. What NU1
adds here is the staggered-involution form (b)–(c) and its statement for every member of the
narrow class.

**Lemma NU1 [W; EC C1–C4].** Let `F` be a rule on `ℤ^d` such that each `F_i` reads only the values at
the 2d nearest neighbours `N(i)` (no self-term). Put `p(i) = Σ_k i_k mod 2`. Then:
(a) the space-time sets `C_b = {(i, t) : p(i) + t ≡ b mod 2}`, `b = 0, 1`, are each closed under the
dependencies of `x(t+1) = F(x(t)) − x(t−1)`, so the rule is the product of two independent dynamics;
(b) the dynamics on `C_b` is conjugate to the *staggered rule* on one configuration
`y : ℤ^d → G`: at half-step `t → t+1`, every site with `p(i) ≡ t + 1 + b` is set to
`F_i(y|N(i)) − y(i)` and every other site is held;
(c) each half-step is an involution.

*Proof.* (a) `x_{t+1}(i)` depends on `x_t(j)` for `j ∈ N(i)`, with `p(j) = p(i) + 1`, and on
`x_{t−1}(i)`. If `p(i) + t + 1 ≡ b`, then `p(j) + t ≡ b` and `p(i) + t − 1 ≡ b`. (b) At slice `t`,
let `y` hold `x_t(i)` where `p(i) + t ≡ b` and `x_{t−1}(i)` where `p(i) + t ≡ b + 1`. The sites that
receive `x_{t+1}(i)` in `C_b` are the second kind; their new value `F_i(x_t|N(i)) − x_{t−1}(i)`
reads only first-kind sites (opposite parity) and their own `y(i)`, and the first-kind sites keep
`x_t`, which is the "previous" slot at `t + 1`. (c) During a half-step the neighbours of an updated
site are held, so applying `y(i) ↦ F_i − y(i)` twice returns `y(i)`. ∎

On a torus the same holds when every side is even; C4 is the countercontrol with an odd side.

*Scope.* This uses the nearest-neighbour range at every state, which is stronger than ledger (x)
(stated on the reference class only), and (xi) second clause. Call the rules satisfying both the
*narrow class*. Every member of §1 is in it: L₂, L_q, L_{q,α} and R_q. The proof also holds for
site-dependent, non-totalistic `F_i`, and for any `F_i` that reads only opposite-parity sites of a
bipartite graph. For Q it is U2 A1 (component independence).

*Consequences [W].*
1. *One direction only: a universal staggered rule gives a universal member.* Suppose the
   component-`b` staggered rule of a narrow-class `F` is universal under a notion whose encoding
   `w ↦ y(w)` gives ultimately periodic configurations and whose halting predicate reads finitely
   many component-`b` slots. Hold the other component at any fixed periodic configuration `z`;
   no fixed point is needed. By NU1(a) the full orbit is the pair of the two component orbits, so
   `c(w) = (y(w), z)` is ultimately periodic and the same predicate decides halting for the full
   rule.
   - *Not checked here:* whether this transfers to U1's Definition U exactly. Its symbol `h` is
     the two-slice pair at `i₀`, which reads one slot of each component. The slot of component
     `1 − b` is the orbit of `z` at `i₀`, eventually periodic, but turning "a component-`b` slot
     equals `h_b`" into a single-symbol predicate is not done here.
   - *Converse not argued.* A halting predicate of the full rule can read both components, so
     universality of the full rule is not shown to give a universal component. No equivalence is
     claimed (§A.34).
2. *The `q = 2` members are the Q2R class.* Over `𝔽₂`, `F − y = F + y`, so a half-step flips
   `y(i)` iff `F_i(neighbours) = 1`. This is the class of Vichniac's Q2R (2-D, flip iff exactly two
   of four neighbours are up) [LIT2 for Q2R's definition]. U₂ is the 3-D member with flip set
   `{2, 3, 4}` of the six-neighbour sum [EC C5; the table is U1 A1's]. The complexity result
   located for this class is P-hardness of prediction (§2), not universality.
3. *Margolus App. A is outside the class.* Its `f` reads the diagonals and, as stated, the centre.
   With a centre read, (a) fails: C3 is the countercontrol showing that a self-term breaks the
   decomposition. Whether the Appendix rule can be re-expressed in the narrow class is not known.

### 3.2 The four predecessor findings, read for feasibility

| Item | Source, standing | Obstruction or enabler | Class it covers |
|---|---|---|---|
| Linearity | U1 Theorem L [R; reviewed, re-reviewed ACCEPT WITH NITS, delta CONFIRMED] | obstruction: every halting predicate of Definition U is decidable | linear members with `q` a prime power, any coupling, one periodic background plus a finite change. Composite `q` with two primes and multi-background configurations are not covered |
| Parity-uniform backgrounds of U₂ | U1 Cor. 1.3 from DL1 Th. 2.2 [R] | obstruction (support closure) | U₂, finite perturbations of its sixteen parity-uniform backgrounds |
| Non-affinity of Q | U1 Prop. 1.4 [R] | removes Theorem L's route for Q | Q under every sitewise relabelling into an abelian group |
| Conserved densities | U2 A2 [R; ACCEPT-WITH-NITS] | no obstruction of the template | one template, two alphabets |
| Confinement MQ1–MQ3 | MQ §2 [R; delta re-review ACCEPT-WITH-NITS] | obstruction to interaction between closed classes at ℓ1-distance ≥ 3 without a breach; enabler of wires and memory (confined classes are stable) | Q at any uniform background `c` |
| Finite classes periodic, records erased (MQ4) | MQ [R] | obstruction to persistent computation in finite confined classes | finite classes whose boundary never breaches |
| Signals, crossing, memory | U1 §3 [R] | enabler: a partial, non-interacting set | Q at `c = 2^15`, on designed lines |
| No controlled turn | U1 S1, U2 F1–F3 [R; bounded negatives] | no obstruction; evidence about the searched sets only | ≤ 6 gadget sites, small value ranges, three junction shapes, one signal type and launch phase |
| Breach fronts | MQ X2 [R; post hoc] | the breaches observed grow and consume the background | the stored S-B configurations |

**How MQ1–MQ3 bear on a turn or a gate.** A junction where two lines meet is one closed set
(its inner-corner site has two line neighbours), so MQ3 does not require a breach for a turn. What
MQ2 gives is weaker and exact: as long as the boundary layer of the junction's closed class stays
in `[c−1, c+1]`, nothing leaves the class. U2's failures are boundary breaches: the inner-corner
site is kicked and a disturbance leaves (U2 D1, AW-UNIV-3). Two consequences follow [W]:
- a gate between two lines whose closed classes are at ℓ1-distance at least 3 needs a breach
  (MQ2(b), MQ3);
- a turn or gate inside one class needs either a boundary that never breaches, or a breach that
  stays bounded and heals.

Every breach observed so far grows (MQ X2), but none of these observations is a proof. This is
the decisive question for Q in §4.

**The missing controlled turn.** In MQ terms, U1's missing block is a controlled transfer whose
closed class has a non-breaching boundary, or whose breach stays bounded. No construction and no
obstruction is known.

### 3.3 Which sub-questions an exact or exhaustive bounded computation can decide

| Sub-question | Decidable by bounded computation? | Why |
|---|---|---|
| NU1 on given instances | yes, per instance (done: C1–C4) | finite runs; the lemma itself is proved on paper |
| Whether a finite closed gadget on a uniform background ever breaches | yes, exactly, per gadget and initial value | isolated finite class is a bijection on a finite set (MQ4), so the orbit is periodic and one period decides it |
| Whether a given junction with semi-infinite lines turns a signal | not in general; yes for a fixed finite horizon | infinite configuration; a horizon test is evidence only (U2's method) |
| Linearity, affinity or a fixed-point count of a member | yes (U1 A2–A4) | finite tests on invariant subgroups |
| Goal-A census: all `F` in the narrow class at small `q`, `d` (e.g. `q = 2`, `d = 2`: 2^16 neighbour functions, 2^5 totalistic) for linear/affine members, gliders and collision tables | yes for each screen at a fixed size and horizon | a screen finds candidates; universality still needs an encoding, construction and correctness argument |
| Universality of Q, or of any fixed member | no | not decidable by a finite search; needs a proof in either direction |

***

## 4. F4: feasibility verdict

Stated only at the level established, for each goal of c.7047109654.

- **Goal A as posed (second-order form mod `q`, finite alphabet, local translation-commuting
  coupling): answered positively at sketch level.** Margolus (1984, App. A) gives a universal rule
  in that architecture, with `q = 3`, `d = 2` and a 3×3 neighbourhood including the centre. It is a
  construction with a sketch-level reduction to the BBM, and its undefined cases are left free
  [LIT-R]. This is a comparison model only.
- **Narrow class (nearest neighbours at every state, no self-term; ledger (x) states the range on
  the reference class only): open.** No universal member and no obstruction are known.
  - *Decisive question.* Is some staggered involution rule (NU1(b)) universal on `ℤ²` or `ℤ³` at
    some finite `q`? By §3.1 consequence 1, a positive answer, under a notion whose halting reads
    one component, gives a universal member of the narrow class. A negative answer would not by
    itself exclude one, since the converse is not argued.
  - *A sub-question.* Can such a rule simulate a block-permutation CA? The Kari / Durand-Lose
    representation reduces every reversible CA to block permutations.
- **Goal B (the native rule).**
  - *Obstructed* for linear members with prime-power `q` (Theorem L, Definition U's class), and
    for U₂ on finite perturbations of parity-uniform backgrounds.
  - *Open* for Q = `R_{2^16}` on `ℤ³`. Its partial set (signals, crossing, memory) is
    non-interacting. MQ2(b) and MQ3 force every interaction between closed classes at ℓ1-distance
    at least 3 through a breach.
  - *Decisive question for Q.* Does a bounded breach exist: a finite closed gadget on a uniform
    background whose boundary layer leaves `[c−1, c+1]` only transiently, heals without
    radiation, and moves a signal? Or does every breach of the isolated dynamics grow without
    bound, which would be an obstruction on uniform backgrounds?
  - *Not the alphabet.* At `q = 2^16` the pair alphabet has 2^32 symbols, so the minimal-alphabet
    literature does not bear on Q. What has to be shown concerns this particular rounded `F`.
- **Goal C (physical emergence)** is not addressed (#866, AW-MQ-2).
- **For the narrow class and for Q: not feasible-in-principle, not obstructed.** Neither stronger
  verdict is supported for them. A
  universal rule in the second-order form exists. That does not show that the narrow class admits
  one, and it says nothing about Q.

***

## 5. Proposed next steps (plans only; nothing here is run)

Each plan needs owner authorization before it starts. Each is preregistered before it runs. Any
heavy part runs in CI under an approved workflow (§A.40, §A.43 item 4).

- **P1 (Goal A, comparison only).** A census of the narrow class at `q = 2`, `d = 2`: the 2^16
  neighbour functions, or the 2^5 totalistic and 2^6 symmetric ones first.
  - Exclude affine members (Theorem L).
  - Screen each remaining rule for moving localized patterns on uniform and period-2 backgrounds,
    then catalogue the two-signal collisions.
  - Output: candidates only. Any candidate is a comparison model, never a replacement for the
    native rule. A rule change would be a Layer-0 revision under §A.29.
  - Paper task beside it: whether a staggered involution rule can realize a block permutation of
    a Kari / Durand-Lose decomposition at enlarged `q`.
  - The closest located construction for that task is Morita–Ueno's 16-state two-dimensional
    partitioned CA (1992) [LIT-B for the bibliographic record and the 16-state count; LIT2 for the
    neighbourhood description]. The reviewer recalls each new cell state as reading only the
    facing parts of the four neighbours, which is nearest-neighbour and centre-free but first-order
    and partitioned; this record has not re-read it. It is a candidate comparison model only, and
    nothing here simulates it.
- **P2 (Goal B, Q).** An exhaustive bounded-breach search on `c = 2^15`.
  - For every closed set `D` of at most `k` sites (`k` fixed in advance) and every initial
    content in a fixed value range, decide exactly, by the period of the isolated orbit (MQ4),
    whether a breach occurs, and whether it heals.
  - Healing is checked on the infinite background by the light-cone argument at a stated
    horizon. Results are evidence about the searched set only.
  - A healed breach would be a candidate ingredient for a turn. That is a step-2 construction,
    not part of this plan.
- **P3 (paper).** Try to prove the complementary statement: on a uniform background, any breach
  in R_q's RZ window spreads at a positive speed. U2 D1 and MQ X2 suggest the mechanism. A proof
  would be an obstruction for Q on uniform backgrounds, stated only for that class.

***

## 6. Owner decision points

1. **The PM-D5 prerequisite.** #1461's table lists PM-D5 (#1454) as a prerequisite; PM-D5 is
   paused. This record went ahead with order step 1 only, as instructed. Does the prerequisite
   stand for step 2 and for P1–P3, or is it waived for feasibility work?
2. **Which member is "the actual published rule and its fixed alphabet".** The corpus fixes the
   form and, for `R_q`, `d = 3` and `F`, but not `q` (§1). U1 chose `q = 2^16`. Should NATIVE-UNIV
   take Q, U₂, or the family `R_q`? If Main's linear A5 model is meant, Theorem L already decides it
   for prime-power `q`.
3. **Goal A's class.** (a) Does Goal A mean the architecture of c.7047109654 (local,
   translation-commuting coupling), which Margolus 1984 answers at sketch level, or should it
   carry ledger (x) at every state and (xi)'s no-self-term clause (the narrow class)?
   (b) Does a comparison-model construction in the narrow class (P1's paper task) count as step 1,
   where c.7047109654 places Goal A, or is it a construction that needs step-2 authorization?
4. **Authorization for P1–P3** and any CI dispatch.

***

## 7. Checks and classification

**Checks.** `checks/nu_checks.py`, from this directory: `python3 -I checks/nu_checks.py` (under
one second; exit status 0 iff the controls are green and C1, C2, C5 hold). Its output is
`results.json`. The decision rule is in `PREREG.md`, which was committed before the script. The
printed verdict is: "controls green; component lemma consistent with exact runs on the sampled
instances (12 (q,d) pairs x 3 seeds, 24 ticks); every half-step is an involution on them; C5 q=2,d=3
table [0, 0, 1, 1, 1, 0, 0] equals the indicator of {2,3,4}". C3 (self-term) and C4 (odd torus)
fail the comparison, as the controls require. `PREREG.md` and the script call every instance "the
rounded rule `R_q`". Only the `d = 3` instances are SM's rule; at `d = 1, 2` the update
`⌊(Σ_nn x + 1)/3⌋ − x(t−1)` is another member of the narrow class, which is all NU1 needs. The
script's comment is corrected; its output is unchanged. C2 is close to immediate once C1's bipartite
structure holds: the involution property follows from the held neighbours, and C2 checks only the
implementation.

**Productivity test.** Fixed by the assignment: F4 must give one of feasible-in-principle,
obstructed for a stated class, or open with the decisive next question. It gives the third.

| Item | Class (§A.31) |
|---|---|
| Margolus 1984 App. A is a universal rule in the exact second-order form, answering Goal A as posed at sketch level, with a neighbourhood outside the narrow class | NEW for the corpus (the literature check c.7047109654 asked for) |
| NU1 for the narrow class (decoupling credited to Margolus 1984, p. 84); staggered-involution form; `q = 2` members are the Q2R class, U₂ = flip on `{2,3,4}` | ELABORATING (U2 A1, generalized) |
| MQ2(b)/MQ3's bearing: interaction between classes at ℓ1-distance ≥ 3 needs a breach, a turn inside one class does not; the bounded-breach question | ELABORATING (MQ, U2 AW-UNIV-3) |
| Verdict: Goal A as posed answered at sketch level; "open" for the narrow class and for Q | CONFIRMING (no new obstruction or construction) |

**Assumption-watch AW-NU-1 (neighbourhood versus form).** "Universal reversible rules of the form
`x(t+1) = F(x(t)) − x(t−1)` exist" is true (Margolus 1984), but it does not transfer to the narrow
class. A nearest-neighbour range at every state (stronger than (x)) and no self-term (xi) split the
dynamics into two staggered involution rules (NU1). A claim about the form alone does not cover the
narrow class.

**Pressure test (§A.31).** The favourable reading would be "universality is feasible for OI
because the form admits it". It fails, for the reason in AW-NU-1. The literature survey is not
systematic, and a result on staggered involution rules may exist that was not located. Margolus's
Appendix was read in OCR text without its figures, so the centre dependence of its tables is
unverified.

**Fixed point.** One pass; the §A.31 fixed point is not reached.

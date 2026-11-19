# DELIVER-1: delivering a supplied preparation resource to a fixed ready block

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form).
Independent non-author review: REVISE at `95e7d764`
([#1425 c.7023337287](https://github.com/amaybaum/incompleteness/pull/1425#issuecomment-7023337287));
re-review: REVISE at `457d1976`
([#1425 c.7023506974](https://github.com/amaybaum/incompleteness/pull/1425#issuecomment-7023506974));
third review: ACCEPT WITH NITS at `beae0758`
([#1425 c.7023645987](https://github.com/amaybaum/incompleteness/pull/1425#issuecomment-7023645987));
this revision answers all three (B1–B3, N1–N6; C1, C2, N7, N8; N-R1, N-R2). It adopts
no premise, edits no manuscript, Lean module or registry, and runs no simulation. Small exact
checks are included as controls (§10).

- **Authorization.** Owner `amaybaum`, row 1 of
  [#1169 c.7022491049](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7022491049),
  2026-11-19T21:18:20Z ("All of the above, proceed as suggested"). Scope: "Can a native OI update
  move a supplied non-equilibrium resource (from an initial law, from μ-O or μ-R, or from a
  boundary condition) into a local ready cell?" Limits: "Paper-only. No premise adoption and no
  merge. A non-author review is required".
- **Goal link (§A.47), from the authorization.** "Unit 1 attacks the measurement-source
  bottleneck." The work decides, for one declared native update, whether a supplied resource of
  each named type can be delivered repeatedly to a fixed ready block within the exclusions
  NSC-1..7. Unchanged, as recorded there: "A1 OPEN/UNADOPTED; physical measurement sourcing NOT
  PASSED".
- **Accountable Issues.** #866 (native preparation source), #1169 (OI projection objective).
- **Snapshot.** `main` at `21e16c61e4dfa07f5902fdc113fbf8eeb974d441`. Record paths are relative to
  `verification/programmes/oi-qm/reconstruction/` unless they start with `verification/`;
  `foundations/` abbreviates `verification/audits/foundations/`. `PR1` is
  `prep-regress-1-20261119/RESULT.md` and `PR1 2.5` its item 2.5.
- **Productivity test (fixed in advance by the assignment).** The unit is a gem iff it yields
  (i) a native delivery construction meeting NSC-1..7 with a supplied resource of a named type, or
  (ii) a scoped obstruction stronger than PR1's. Anything else is recorded as relabelling.

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`, cited by its record; nothing built here |
| [P] | manuscript statement |
| [R] | research record on `main`, not independently established |
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/deliver_checks.py` (integer and rational arithmetic; entropies as exact `a + b·log₂3`) |
| [LIT2] | literature cited from memory, not re-read; no result depends on it |

***

## 0. Summary

1. **Corpus (§1).** Every screen that reaches a delivery step derives it once, conditional on a
   supplied input: loading from a stipulated bank, exchange with a supplied ready reference, native
   delivery of a record into a neighbouring gate input. None sources renewal. The laboratory
   benchmarks re-arm through an imported actuator, reset, bias or reinitialization. The P8-type
   constructions consume fresh *uniform* inputs, which cost no budget (PR1 AW-PR1-2); none of them
   draws on ready cells.
2. **Node 1 (§2).** The delivery task DT is defined on the declared update U₂, the binary
   rounded-cubic rule of #1408 and #1412. A designed conveyor meets DT's arithmetic with equality in
   PR1's per-cycle bound and fails NSC-1 and NSC-3; the budget alone does not separate it from a
   native mechanism.
3. **Node 2 (§3) [W, EC].** For U₂ and each of its sixteen parity-uniform backgrounds β, the
   2-neighbour closure of a perturbation's support is invariant in time (Theorem 2.2). Hence:
   background sites outside that closure are never perturbed; the budget available to a ready
   block is the relative entropy of its closed component, which excludes every background bit
   outside that component (PR1 2.6 counts them); a carrier affects the block only if it was in
   closure contact with it at `t = 0`, so no carrier approaches; a finite component returns to its
   initial content at every multiple of its period, so every record is erased by then; a
   parity-uniform slab of width ≥ 2 is never entered. So only carriers initially in the block's
   component are ever used. Repetition on such pre-placed carriers occurs, bounded by (2.4) and by
   their number: the reviews' examples deliver once (2.3(f)) and twice on two distinct carriers
   with both records meeting (R) (2.3(i)), all from designed patterns, which NSC-3 and NSC-5
   exclude. Open: bounded
   ready regions inside noise (the closure is then the whole lattice), alphabets `q ≥ 3`, including
   the published `q = 2^16`, and a pure parity-uniform supply with carriers inside the block's
   component beyond the boxes searched (2.3(g)).
4. **Node 3 (§4) [W, EC].** Under any invariant law, an externally scheduled moving block gains
   nothing that the target block lacked at the earlier time (relabelling). A natively pointed block
   has a time-independent law and costs exactly what a fixed block costs. Under μ-O every block has
   entropy at most `log₂ ℓ`, so the static budget `log₂(|S|/ℓ)` and the entropy of carriers trade
   off through the orbit length ℓ.
5. **Node 4 (§5).** What dropping A1 would require, without investigation.
6. **Node 5 (§6).** Controls hold.
7. **Productivity (§7).** Test (ii) is met at the scope of Theorem 2.2, by its clause-free
   consequences. Test (i) is not met: the native deliveries found (2.3(f), (i)) run on U₂ but draw
   on designed initial patterns (NSC-3, NSC-5), and no carrier from outside the block's initial
   component is ever used. Classification: gem, NEW at that scope (the review agrees); Node 3
   ELABORATING.

***

## 1. Corpus read (§A.19): delivery as distinct from supply

| Source | Supply | Delivery | Renewal (refresh) |
|---|---|---|---|
| `native-producer-2-20261117/SOURCE-SCREEN.md:81–93` [R] | Native A pool (fair triples F8, F10, F9) and prepared phase: "begins with those resource distributions"; unsourced | "conditional native propagation results" not denied (:88–89) | "no free history tape, reset or renewed source is supplied" (:112) |
| `native-preparation-source-1-20261110/PREPARATION-SCREEN.md` [R] | quiescent bank β_c: "a proposed incoming resource" (:12); unsourced (:97, :100) | "Actual ordinary F loading — **Derived**, conditional on its incoming state" (:96); one tick places `F(β_c)` in the ready set (:59) | "Renewal/reset — **Unsourced**. Mathematical bijectivity supplies neither an observer-operated inverse nor fresh banks" (:106) |
| `controller-preparation-1-20261108/SELECTION.md:107–121` [R] | common input/resource law not sourced | selected switch not identified as a native interaction | "no free reset or blank supply" (:121) |
| `native-apparatus-source-20261113/ASSESSMENT.md` [R] | "source absent" for ready cells (:71) | conditional loading relation derived (:71); a qualifying source must deliver "a specified operational input law rather than merely its inverse image" and account "for consumed readiness" (:157) | "Repeat-run renewal — Absent producer/reset/resource supply" (:77) |
| `record-control-20261107/DESIGN.md` [R] | Native A preparation assumed | "physical neighbor delivery is present" (:98); "an actual native update on every prepared successful trajectory" (:81) | conversion to a usable operation is the first open gate (:220); no reset or refresh (§5) |
| B3, `oi-qm-ext-1/measurement-exchange.md:72` [R] | supplied ready reference bank | exchange with the ready reference, derived conditionally | "Each detector consumes its ready reference bank … Later cycles or more measurements need fresh banks or an accounted preparation/reset mechanism" |
| `o-ret-routes-20261103/classical-retention-20261107/LEAD.md` [R] | external bead register | external camera read; native map unsourced | the experiment uses "an explicit reinitialization procedure" (:45); "Reset, fresh bath or a new blank camera register cannot be inserted for free" (:125) |
| `mechanical-latch-source-20261119/ASSESSMENT.md` (#1406) [R] | fabricated geometry and unlatched state, supplied | impact write, external | "a powered electrostatic actuator to reset the device between impacts" (:13) |
| `geiger-muller-recovery-20261119/DECISION.md` (#1393) [R] | biased tube, supplied | pulse, external | "restoration of readiness … **UNSOURCED on F**" (:34); the record trace must account for "consumed resources" (:37) |
| `diffusion-readiness-20261118/ASSESSMENT.md` (#1364) [R] | temperature gradient unsourced (:71) | unreached (:72) | replenishment unreached (:73) |
| `foundations/a1-p8-history-bridge-20261119/RESULT.md:13` (#1400) [R] | fresh input of one law ν, independent of the past | positive labelled table, conditional | refresh is the fresh input; ν uniform costs no budget |
| `foundations/p8-p12-bridge-20261119/RESULT.md` (#1404) [R] | "a prepared upstream bath, a chosen site gate" (:281) | rightward bath shift, eq. (2) (:110) | uniform bath symbols, budget-free |
| `foundations/p8-p12-rounded-cubic-20261119/RESULT.md` (#1408) [R] | product-uniform law | first response recoverable next tick | fixed-site obstruction from the centre-free stencil (:103–131) |
| `foundations/p8-p12-forward-request-1411-20261119/RESULT.md` (#1412) [R] | product-uniform law | moving-frame readout; inputs uniform given the past (:129) | strict support fails for every register meeting (N) (:257–) |
| `PR1` §§4–6 [R] | transfer identity, multi-record bound, NEQ-T/NEQ-O proposals | "a native mechanism that makes the resource operationally available … remains open" (§6) | reversible re-arming un-writes (C5) |

**Extracted.** Delivery once, from a supplied input placed where the next update reads it, is
derived wherever a screen gets that far. Renewal is never sourced. The laboratory benchmarks show
renewal as an imported resource. The P8-type constructions renew only budget-free uniform inputs.
The open half named by PR1 is therefore renewal of readiness under a fixed native update, which is
what DT below formalizes.

***

## 2. Node 1 — the delivery task

**Declared update U₂.** The binary specialization of the rounded rule of SM §4.2 used in #1408 and
#1412: on `Λ = ℤ³` or the torus `(ℤ/n)³`, with `N(i)` the six nearest neighbours,
```text
x_{t+1}(i) = g( Σ_{j∈N(i)} x_t(j) ) ⊕ x_{t−1}(i),   g(s) = ⌊(s+1)/3⌋ mod 2,
```
so `g(s) = 1` exactly for `s ∈ {2,3,4}` [EC E1]. The state is the two-slice pair
`W_t = (x_{t−1}, x_t)`; the inverse is `x_{t−1} = g(Σ x_t) ⊕ x_{t+1}`, of the same form.
The reference law is the product-uniform law μ₂ on both slices (#1408).

**Definition DT(H, w\*, ε, N, T).**
- *Block and value.* `H ⊂ Λ` finite; content `W_t(H) ∈ {0,1}^{2|H|}`; a designated value `w*`
  that does not depend on settings or carriers (NSC-7, "fixed known values on designated cells").
- *Ready.* `H` is ε-ready at `t` if `P_t(W_t(H) = w*) ≥ 1 − ε`. Then
  `K_t(H) ≥ D(p_{W_t(H)} ‖ u) ≥ d(1−ε ‖ 2^{−2|H|})`, since `H(H|Rest) ≤ H(H)` and data processing
  applies to the indicator of `{W_t(H) = w*}` (PR1 2.4). This is the K threshold.
- *Carrier.* A balanced binary random variable `c_k`, located at `t = 0` in a region `C_k`: the
  initial content of `C_k` is a function of `c_k` and data independent of `c_k`, and `c_k` is
  independent of the initial content outside `C_k`.
- *Use.* A time `s_k` with `I(W_{s_k}(H); c_k) > 0`.
- *Refresh.* Times `τ_1 < … < τ_N ≤ T` at which `H` is ε-ready, with a use of a distinct carrier
  between consecutive τ's. Each `τ_{k+1}` after a use is a delivery.
- *Retention (budget form).* At `T`, each used carrier's bit is ε-predictable from a log block
  disjoint from the carriers.
- *Record formation (R).* The log block for `c_k` carries no information about `c_k` at any time
  before the first use of `c_k`: `I(W_t(L_k); c_k) = 0` for `t < min s_k`. (R) is this record's
  reading of NSC-7 ("held …, correlated with a functional of Σ, residual handed on") and of
  #1358 ("a second measurement retaining the first result"), not their text: it reads "result" as
  a result of the use, and information that reached the log before the use is not that. (R) is necessary,
  not sufficient, for a record caused by the use. Without (R), retention can be met by information
  that reaches the log by another path (2.3(h)).
- *Exclusions (NSC-1..7 as constraints).* One fixed update, U₂ (NSC-1); the supply is a declared
  initial law, and every conclusion is conditional on it as a regress endpoint, with its standing
  stated (NSC-2, NSC-5); a construction that works only because its initial pattern was chosen for
  it does not solve the regress (NSC-4; NSC-3, "a newly tuned prepared producer state"); the
  schedule is fixed by the update and the initial law, with no controller and no herald outside
  the model (NSC-3); every statement is about laws, with no conditioning on success (NSC-3); the
  initial law is a declared supply, the carriers, and μ₂ elsewhere, with every low-entropy cell
  inside the declared supply (no hidden fresh cell, NSC-3, NSC-5); the measures are those of
  NSC-6 (supply types below); ready means the known value `w*` (NSC-7); carriers are the systems
  measured and lie outside a declared apparatus region `A ⊇ H`. NSC-3 constrains the apparatus and
  supply (tuning, heralds, postselection, hidden distributions, fresh cells, controllers), not where
  a carrier sits.
- *Supply types.* NEQ-T, a time-slice law with a declared low-entropy region; μ-O and μ-R, the
  invariant laws of PR1 1.5(b), (b′); inflow, with A1 dropped (PR1 1.5(d)).

**Check (non-vacuity and countercontrol) [EC D1, D2].** Designed conveyor CR on a ready cell `H`,
a belt `b_0..b_{m−1}` and a carrier stream: each tick writes `H ← H ⊕ k_0`, exchanges `H` with
`b_0`, and advances belt and stream. With `m = 3` ready belt cells, `H` is ready after ticks 1–3
and has probability 1/2 at tick 4, when the first used cell returns. At tick 3 the three records
are held, and `K(H ∪ belt) = D₀ = 4 = (N+1)(1 − h₂(0))`. With belt cells ready with probability
3/4 (a bath-like refresh), readiness is 3/4 at ticks 1–3 and
`K(H ∪ belt) = D₀ = 4(1 − h₂(1/4))`. Both attain PR1's per-cycle bound with equality.

**Verdict, node 1.** DT is fixed and non-vacuous: a designed gate meets its arithmetic. CR and the
bath variant pass only by importing their routing and their fresh cells. Their routing is a
chosen gate, not U₂ (NSC-1); their ready belt is a set of fresh memory cells placed where the gate
reads them (NSC-3). The #1404 bath shift is a conveyor of this kind ("a chosen site gate",
`foundations/p8-p12-bridge-20261119/RESULT.md:281`). Since the bound is attained by an
importing countercontrol, the budget does not discriminate; the discriminating question is the
native mechanism. NSC-1 alone excludes CR; reading its belt as fresh memory cells under NSC-3 is
interpretive, since DT admits a declared low-entropy supply. CONFIRMING relative to PR1.

***

## 3. Node 2 — NEQ-T supply under U₂

**2.1 Backgrounds [W, EC E2].** Let `χ(i) = (i_1 + i_2 + i_3) mod 2` (on a torus, `n` even) and
`P = {0, 1, χ, 1⊕χ}`. Each `c ∈ P` is constant on every neighbourhood `N(i)`, because all
neighbours of `i` have the parity opposite to `i`. Conversely a pattern constant on every
neighbourhood is in `P`: `N(0)` and `N(e_1+e_2)` share `e_1`, so the constant value propagates
along steps of even length, which connect each parity class. Since `g(6−s) = g(s)`,
`g(Σ_{N(i)} (y ⊕ c)) = g(Σ_{N(i)} y)` for `c ∈ P`. For `β_t ∈ P` with `β_{t+1} = β_{t−1}` (sixteen
period-2 backgrounds, the vacuum among them):

*Lemma 2.1.* `x` solves U₂ iff `y = x ⊕ β` solves U₂. *Proof.*
`y_{t+1} = g(Σ x_t) ⊕ x_{t−1} ⊕ β_{t+1} = g(Σ y_t) ⊕ y_{t−1} ⊕ β_{t−1} ⊕ β_{t+1}`; the last two
terms cancel. Taking `y = 0` shows that β solves U₂. ∎

Each β is a ready supply: every block has the known value `β|_H` at every time. Relative to the
counting measure, a region `V` held at β carries `2|V|` bits.

**2.2 Closure invariance [W, EC E3–E6].** For `D ⊆ Λ`, `cl₂(D)` is the smallest superset of `D`
that contains every site having at least two neighbours in it (2-neighbour bootstrap closure,
[LIT2] §9). `D` is *closed* if `cl₂(D) = D`. For a perturbation `y` put
`A_t = supp y_{t−1} ∪ supp y_t`.

*Theorem 2.2.* For every solution `y` of U₂, `cl₂(A_t) = cl₂(A_0)` for all `t ∈ ℤ`; in particular
`supp y_t ⊆ cl₂(A_0)`.

*Proof.* Let `A_t ⊆ D` with `D` closed. For `i ∉ D`, `y_{t−1}(i) = 0`, and `i` has at most one
neighbour in `D ⊇ supp y_t`, so the neighbour sum is at most 1 and `y_{t+1}(i) = 0`. Hence
`A_{t+1} ⊆ D`. With `D = cl₂(A_t)` this gives `cl₂(A_{t+1}) ⊆ cl₂(A_t)`. The inverse step has the
same form, so `cl₂(A_t) ⊆ cl₂(A_{t+1})`. ∎

*Lemma 2.3 (closed sets).* (a) A box (product of intervals) is closed on `ℤ³`, and on `(ℤ/n)³`
when each side is at most `n−2` or the full extent: a site outside it has at most one neighbour
inside. (b) A slab of width `w ≥ 2` has a closed complement. (c) If `D_1, D_2` are closed and at
ℓ1-distance at least 3, `D_1 ∪ D_2` is closed; if moreover `A_0 ⊆ D_1 ∪ D_2`, the content of `D_1`
evolves as a function of the content of `D_1` alone: every neighbour of a site of `D_1` lies in
`D_1` or outside `D_1 ∪ D_2`, where `y` vanishes at every time by Theorem 2.2. ∎ [EC E3, E6, E10; countercontrols: side `n−1`, width 1,
distance 2]

**2.3 Consequences for DT under a parity-uniform supply [W].**

- **(a) Inert supply.** Outside `Ω := cl₂(A_0)` every site holds `β` at every time. Its readiness
  is permanent and is never written or moved. Sites next to `Ω` are read by the updates inside
  `Ω`, but their fixed values do not affect the perturbation dynamics (Lemma 2.1).
- **(b) Deliverable budget.** *Hypothesis (I):* deterministic closed sets `Ω*` (finite) and `Ω′`
  at ℓ1-distance at least 3 with `A_0 ⊆ Ω* ∪ Ω′` almost surely, and the initial content of `Ω*`
  independent of that of `Ω′`. Under (I) the perturbation content of `Ω*` evolves by a fixed
  bijection Ψ of `{0,1}^{2|Ω*|}`, independently of everything else, and the background is
  deterministic; in `x`-coordinates Ψ is composed with the known period-2 XOR by β, which changes
  none of the quantities below. PR1 2.1,
  2.3 and 2.5 therefore apply on `{0,1}^{2|Ω*|}`: for `H ⊆ Ω*`,
  `K_t(H) + D(p_{Ω*∖H,t} ‖ u) = D(p_{Ω*,0} ‖ u)`, and a protocol holding `N` ε-predictable results
  inside `Ω*` with `H` ε-ready at one time needs
  ```text
  (N+1)(1 − h₂(ε)) ≤ D(p_{Ω*,0} ‖ u_{Ω*})          (2.4)
  ```
  under PR1 2.5's hypotheses (fixed blocks, balanced targets, disjoint predictors). PR1 2.6 bounds
  the same quantity by the relative entropy of the cone base, which counts 2 bits for every
  background site in the cone. (2.4) counts none of those outside `Ω*`: the background outside the
  closed component, however large, adds nothing to the budget deliverable at `H`. Sites of `Ω*`
  that hold β at `t = 0` do count, 2 bits each; in E7 the budget `D₀ = 2` is exactly the centre's
  background bits, and that is the resource redistributed there.
- **(c) Carrier admission.** Under (I) the content of `Ω*` at every time is a function of its
  content at `t = 0`. A carrier located in `Ω′` never affects `H ⊆ Ω*`. The component structure
  is fixed at `t = 0`: no carrier approaches `H` over time, and every carrier that is ever used
  was in closure contact with `H`'s component at `t = 0`. If `Ω*` is finite, Ψ has a finite period
  `P`; at `t = P` the content of `Ω*` equals its initial content, at which `c_k` is held only by
  its own cells, so every record of a carrier is erased by the next multiple of `P`, and the
  number of usable carriers is the number initially in `Ω*`. Readiness of `H` can return before
  `P` while a record is held elsewhere in `Ω*` (2.3(f)). [EC E7: in the closed box
  `{−e_1, 0, e_1}` the centre is written with the AND of the end bits; its readiness is
  `1, 3/4, 9/16, 3/4, 1` at `t = 0..4` while `K(centre) = 2 = D₀` throughout; in this box readiness
  returns when the record is un-written.]
- **(d) Insulating slab.** By Lemma 2.3(b) a parity-uniform slab of width at least 2 is never
  perturbed, whatever the law outside it; on `ℤ³` it separates the two half-spaces exactly.
- **(e) Low-entropy world.** If the initial state is almost surely a finitely supported
  perturbation of β, every pattern stays in its bounding box (Lemma 2.3(a)) and every component is
  finite and periodic. A single excitation is a period-2 blinker [EC M3].

- **(f) Delivery inside one component (the review's example) [EC E12].** On the closed segment
  `{0,…,4}·e_1` in the vacuum, take `x_{−1} = 0` and `x_0 = (c, 0, 1, 0, 1)`, with a fair carrier
  `c` at site 0, `H` = site 1 and `w* = (0,0)`. Then `H` is ready at `t = 0`, its content depends
  on `c` at `t = 1..4`, and it is ready again at `t = 5` for both values of `c`, while site 3's
  current slice equals `¬c` at `t = 5`. The orbit lengths are 4 (`c = 0`) and 6 (`c = 1`), with
  common period 12, so the record survives the refresh. This meets DT's arithmetic for two ready
  times with `ε = 0` and `A = {H}`. Against NSC-1..7: the update is U₂, with no controller, herald
  or postselection, and readiness is a known value (NSC-1, NSC-3 as to controllers, NSC-7); the
  supply is a designed initial pattern `(·, 0, 1, 0, 1)` chosen so that this delivery occurs,
  which is a newly tuned prepared producer state (NSC-3) with no independent justification as a
  regress endpoint (NSC-2, NSC-4, NSC-5). The log at site 3 carries no information about `c` at
  `t = 0`, so (R) holds [EC E12b]. It is a native delivery mechanism on U₂ conditional on a tuned
  structured supply, not a native delivery under NSC-1..7; the exclusion rests on the tuned
  pattern, not on where the carrier sits.
- **(g) Negative evidence, not proof [EC E14].** An exhaustive exact (`ε = 0`) search with a pure
  vacuum supply (by Lemma 2.1, the same as any parity-uniform supply) and carriers placed on the
  current slice, the previous slice or both, on lines of length 3–7 and boxes `2×2`, `2×3`,
  `3×3` with 1–2 carriers, and on lines of length 4–6 and `2×3` with 3 carriers, horizon 30,
  finds no delivery whose log determines the carrier. The same routine finds the delivery of (f)
  when given its designed pattern [EC E14b]. A carrier counts as used when the law of `W_s(H)`
  depends on it, which is DT's definition. The review reports a wider search of the same kind,
  cited as provenance. This is evidence about those boxes only.
- **(h) Two deliveries in DT's arithmetic, the second record failing (R) (the re-review's example) [EC E13, E13b].** On
  the same segment, take two-slice initial contents site 0 `(a, a)`, site 1 `(1, 1)`, site 2
  `(1, 1)`, site 3 `(b, 0)`, site 4 `(1, 1)`, with independent fair bits `a`, `b`, `H` = site 1 and
  `w* = (1,1)` (a parity-uniform value). The orbit lengths are 4, 6, 6 and 12. `H` is ready at
  `t = 0, 4, 16` for all four `(a, b)`; `W_t(H)` depends on `a` at `t = 1, 2, 3` and on `b` exactly
  at `t = 5..10`, so the second use is of a carrier not used before `τ_2 = 4`; at `t = 16` the
  two-slice content of sites 2 and 4 determines `(a, b)`. This meets DT's arithmetic with two
  deliveries on distinct carriers. Under (R) it does not: the record of `a` meets (R), but every
  log block that determines `b` at `t = 16` already depends on `b` before `t = 5` (the state at
  `t = 16` equals the state at `t = 4`). It is therefore a delivery whose `b`-record fails (R).
  Its classification against NSC-1..7 is that of (f): a designed pattern (NSC-3, NSC-2, NSC-4,
  NSC-5).
- **(i) Two deliveries with both records meeting (R) (the third review's example) [EC E15].** On
  the segment `{0,…,5}·e_1`, take two-slice initial contents site 0 `(0, 1)`, site 1 `(0, a)`,
  site 2 `(0, b)`, site 3 `(1, 1)`, site 4 `(0, 0)`, site 5 `(1, 1)`, with independent fair bits
  `a`, `b`, `H` = site 3 and `w* = (1,1)`. The segment stays closed. `H` is ready at
  `t = 0, 4, 16` for all four `(a, b)`; `W_t(H)` depends on `a` at `t = 2, 3, 8, 9, 14, 15, 20` and
  on `b` exactly at `t = 7, 8, 17, 18`, so `b` is unused before `τ_2 = 4` and used in `(4, 16)`.
  At `t = 16` site 4 alone determines `a` and determines `b`, and it carries no information about
  `a` before `t = 2` or about `b` before `t = 7`, so both records meet (R). This meets DT with (R)
  for two deliveries on distinct pre-placed carriers. Its classification against NSC-1..7 is that
  of (f): a designed pattern (NSC-3, NSC-2, NSC-4, NSC-5). (R) therefore does not restore an
  obstruction inside a component.

**Consequence of Theorem 2.2 for carriers.** Only carriers in `H`'s initial closure component
are ever used, and no carrier approaches; repetition on carriers pre-placed in that component is
possible ((i)), bounded by (2.4) and by their number, and every record is erased by the next
multiple of `P`. Restated as a convention: if the apparatus region contains `H`'s initial
component, no carrier is ever used. This follows at once from (c) and decides nothing further.

**2.4 Escape checks (maximum skepticism on the branches that would favour a positive answer).**

- **Bounded ready region in noise.** If `V` is bounded and the exterior carries μ₂, `cl₂` of the
  exterior is the whole lattice [EC E11], and Theorem 2.2 gives nothing. At the first tick a
  vacuum site with 1, 2 or 3 noisy neighbours is perturbed with probability 0, 1/4 or 1/2
  [EC E9]: faces hold, edges and corners erode. A single ready site in noise stays 0 with
  probability 7/32 [EC E9], the complement of the 25/32 of #1408's bare-read control
  (`foundations/p8-p12-rounded-cubic-20261119/RESULT.md:133–155`). Whether a carrier can reach `H`
  through the eroding interface and leave `H` ready again, repeatedly, is open; the only bound is
  PR1 2.6.
- **Structured supply.** A known non-background pattern is a perturbation of β. Its content is
  deliverable only inside its own component, by (b) and (c).
- **Other alphabets.** For `q = 3` and for the published `q = 2^16`, a single symbol 2 in the
  vacuum reaches all six neighbours in one step [EC E8]; Lemma 2.3 fails and the question is open.
- **Other rules.** The vacuum of the SM §3.1 ring rule conducts: a single excitation reaches three
  sites in one step [EC E8b]. This agrees with the one-tick loading derived there
  (`native-preparation-source-1-20261110/PREPARATION-SCREEN.md:59, :96`); its renewal remains
  unsourced (:106).
- **Infinite structures.** Content can reach `H` from far away only through a component that
  connects them at `t = 0`; an unbounded supply needs an infinite component (§5).

**2.5 Refresh count.** Under (I), the number of deliveries whose results are all still held is
at most `D(p_{Ω*,0} ‖ u_{Ω*})/(1 − h₂(ε)) − 1` by (2.4), and at most the number of carriers
initially in `Ω*` by (c).

**Verdict, node 2.** For U₂ with a parity-uniform NEQ-T supply under (I): the background outside
the closed component is inert; the deliverable budget is that of the closed component (2.4); no
carrier from outside the block's initial component is ever used, and none approaches; every record
is erased by the next multiple of the component's period. Inside one component, deliveries with
held records meeting (R) on pre-placed carriers are attainable from tuned patterns ((f), (i)),
which NSC-3 and
NSC-5 exclude. This is a scoped obstruction [W, EC]. Open: bounded ready regions in noise; `q ≥ 3`
including `q = 2^16`; infinite components; and a pure parity-uniform supply with carriers inside
the block's component beyond the boxes of (g).

***

## 4. Node 3 — supply from orbit structure (μ-O, μ-R)

Let μ be φ-invariant on finite `S` and `p_0 = μ`. This covers μ-O and μ-R (PR1 1.4).

*Theorem 3.1 (external schedule) [W, EC M1].* For any time-indexed blocks `H_t` and any
`t_0, t_1`: `K_{t_0}(H_{t_1}) = K_{t_1}(H_{t_1})` and `P_{t_0}(W(H_{t_1}) = w) = P_{t_1}(W(H_{t_1}) = w)`.
*Proof.* `p_t = μ` for all `t`. ∎ The gain `K_{t_1}(H_{t_1}) − K_{t_0}(H_{t_0})` of PR1 1.3 (scope)
is a difference between two blocks, each at its own level at every time; no delivery occurs
between `t_0` and `t_1`. In PR1's C13 example, the block gained at `t_1` (cell 0) has `K = 1`
already at `t_0`.

*Theorem 3.2 (native pointer) [W, EC M2].* Let `Q` be a fixed block, `j` a map from its values to
indices, and `H_0, …, H_{r−1}` blocks disjoint from `Q` whose contents each take `M` values (for
two-slice blocks of `m` sites, `M = 2^{2m}`). Put `Y_t = W_t(H_{j(Q_t)})`. Then the joint law of
`(Q_t, Y_t)` does not depend on `t`, and, for `1 − ε ≥ 1/M`, `P(Y = w*) ≥ 1 − ε` requires
`d(1−ε ‖ 1/M) ≤ D(μ ‖ u)`.
*Proof.* Invariance gives the first claim. For the event `E′ = {Y = w*}`,
`u(E′) = Σ_q u(Q=q) u(W(H_{j(q)}) = w*) = 1/M`, because under `u` each block is uniform and
independent of `Q`; then PR1 2.4. ∎
Without disjointness the claim fails: selecting the first ready cell among three by their own
content has `u`-mass 7/8 [EC M2c], which is a postselection rather than a delivery. In the M2
example the pointed cell is ready with probability 1, each fixed cell and the externally
scheduled cell with probability 1/3, at cost `d(1 ‖ 1/2) = 1 ≤ D(μ-O ‖ u) = 3` bits.

*Theorem 3.3 (carrier entropy under μ-O) [W, EC M3].* Under μ-O on an orbit of length ℓ, every
block has entropy at most `log₂ ℓ`. A protocol holding, at one time, `N` jointly uniform carrier bits and
`N` ε-predictable records of them, with `H` ε-ready, needs `N ≤ log₂ ℓ` and, under PR1 2.5's
hypotheses (fixed blocks, targets balanced under `u`, disjoint predictors),
`(N+1)(1 − h₂(ε)) ≤ log₂(|S|/ℓ)`. Joint uniformity is needed: with ℓ = 2, carriers all equal to
the orbit bit give arbitrarily many balanced bits.
*Proof.* Under μ-O the state is `φ^Θ(s_0)` with Θ uniform on `ℤ/ℓ`, so every block is a function
of Θ. The second inequality is PR1 2.5 with `D(μ-O ‖ u) = log₂(|S|/ℓ)`. ∎
A short orbit gives a large static budget and little carrier entropy: in M3 a single excitation of
the U₂ vacuum has ℓ = 2, budget 127 bits on the `4³` torus, and at most one bit of randomness.

**Verdict, node 3.** The μ-O and μ-R gain is either a relabelling (external schedule) or a static
fixed-block resource (native pointer). Neither is a time-varying delivery in law, and refresh
along a finite orbit is recurrence. #1412's moving frame is the invariant case with `D = 0`: it
delivers fresh uniform inputs and no readiness. ELABORATING (PR1 1.3, 1.5(b), AW-PR1-1).

***

## 5. Node 4 — inflow (requirements only; not investigated)

Dropping A1 permits a stationary incoming stream of ready cells (PR1 1.5(d)). Under U₂ a delivery
from infinity would require: (1) an infinite closure component containing `H`, since finite
perturbations stay in their bounding boxes and background sites never move (Theorem 2.2); (2) a
transport mode inside that component that brings ready content to `H` and exports records; (3) an
independently justified law for the stream (NSC-5), which PR1 2.6 locates in the incoming boundary
data.

***

## 6. Node 5 — controls

| Control | Check | Verdict |
|---|---|---|
| S⇔D⇔Q_fb, `finite_horizon_equivalence` [K] (as cited in PR1's node 3 control table) | It quantifies over supplied finite-horizon laws. Theorem 2.2 restricts transport under one update and says nothing about which finite-horizon laws are representable. | untouched |
| P8 bound (#1400) [R] | Conditional on a positive labelled table with a fresh input of law ν. Not used here; its uniform fresh inputs cost no budget (AW-DL1-2). | untouched |
| #1404 bridge [R] | Its result is a mathematical realization on the declared shift-and-permute class. As a delivery mechanism its bath shift is a designed conveyor (node 1). | untouched |
| #1408 fixed-site obstruction [R] | Product-law statement at one site over consecutive ticks; E9 reproduces its 25/32 control. Theorem 2.2 concerns parity-uniform backgrounds. | preserved at its scope |
| #1412 obstruction [R] | Product law and hypothesis (N). Its moving frame preserves μ₂ (node 3). | preserved at its scope |
| PR1 [R] | 2.1, 2.3 and 2.5 are used inside a closed component; (2.4) sharpens 2.6 at the scope of (I); CR attains the per-cycle bound, as PR1 C4 does. | consistent; nothing changed |
| Source screens (§1 rows) [R] | Each stops at a physical map or producer. The latch, Geiger–Müller and detector screens use `q = 2^16`, where Theorem 2.2 does not apply (E8). No screen is promoted or weakened. | each true at its scope |
| Classical countercontrols CR and bath (D1, D2) | They pass DT's arithmetic and fail NSC-1 and NSC-3. Under U₂ with a parity-uniform supply no conveyor exists, since finite patterns do not move (Lemma 2.3(a)). | do not pass |

***

## 7. Productivity verdict and classification

**Test (i)** is not met. The native deliveries found, 2.3(f) and (i) (from the reviews), run on
U₂ without controller or postselection, but their supplies are designed initial patterns with no
independent justification (NSC-3, NSC-5). They are recorded as native mechanisms conditional on
tuned supplies. No carrier from outside the block's initial component is ever used (2.3(c)); the
carriers used are those placed in the component at `t = 0`. For the other supply types examined
no native construction meets DT.
**Test (ii)** is met at the scope of Theorem 2.2: U₂ with `q = 2`, a parity-uniform supply and
hypothesis (I). There (2.4) replaces PR1 2.6's cone-base budget by the budget of the closed
component, which excludes every background bit outside it, and 2.3(c) adds a mechanism exclusion
(no carrier approaches; every record is erased by the next multiple of a finite component's
period) that PR1 does not contain. Verdict: gem.

**Pressure test.**
1. The mathematics is elementary: a bootstrap-closure argument and the second-order reversible
   form. Its content lies in the consequences for DT.
2. The scope is narrow. The published alphabet `q = 2^16` escapes (E8), as do bounded ready
   regions inside noise (E11) and the SM §3.1 ring (E8b). The result is a negative for one rule
   and does not show that every rule fails.
3. The branches that would favour a positive answer, the erosion interface and the μ-O pointer,
   are not claimed as delivery routes. The first is open and the second costs a fixed block.

| Item | Class |
|---|---|
| Node 1: DT; CR and bath countercontrols | CONFIRMING (PR1 2.5, C4) |
| Lemma 2.1; Theorem 2.2; Lemma 2.3; 2.3(a)–(e); (2.4) | NEW at its scope (author; the review agrees) |
| 2.3(f), (h), (i) examples (from the reviews); 2.3(g) search | ELABORATING (scope of 2.3(c)) |
| Theorems 3.1–3.3 | ELABORATING (PR1 1.3, 1.5(b), AW-PR1-1) |

- **AW-DL1-1 (supplied versus deliverable).** For U₂, and for any update with an analogue of
  Theorem 2.2, a low-entropy region counts toward a delivery budget only inside the active
  closure; for U₂ a parity-uniform region outside the closed component counts zero. A NEQ-T
  proposal (PR1 node 4) on such an update should state which part of its boundary event `B₀` is
  deliverable.
- **AW-DL1-2 (fresh inputs versus ready cells).** The P8-type constructions (#1400, #1404, #1412)
  renew fresh uniform inputs, which cost no budget; ready cells cost budget. Under U₂, noise
  conducts, and a ready site whose six neighbours are noisy stays ready one tick with probability
  7/32 (face sites of a vacuum region hold at the first tick, E9); parity-uniform backgrounds hold
  readiness and conduct no finite pattern. A measurement source on U₂ needs both in one region, which is the
  open interface case of 2.4.
- **Fixed point.** One pass, one NEW item; the §A.31 fixed point is not reached.

***

## 8. What this decides for #866 and #1169

For the declared update U₂ (`q = 2`), the supplied resource of the most symmetric NEQ-T form, a
parity-uniform region, cannot be delivered to a ready block from outside its closed component: it
is never moved, carriers cannot approach through it, and every record inside a finite component is
erased by the next multiple of its period. Inside one component, designed patterns can deliver
with held records meeting (R) on pre-placed carriers (2.3(f), (i)), which NSC-3 and NSC-5
exclude. A
measurement source on U₂ would have to work at a ready/noise interface, or on carriers placed in
the block's component by an independently justified law; both are open here. Under μ-O and
μ-R the static budget is usable only as a fixed-block resource. Physical measurement sourcing is
not affected beyond this: it remains "NOT PASSED", and A1 remains "OPEN/UNADOPTED", as recorded by
the owner.

***

## 9. Limits; what an independent reviewer must check; literature

- Theorem 2.2's proof in both time directions, and Lemma 2.1: that every `c ∈ P` is constant on
  every neighbourhood, and that `β_{t+1} = β_{t−1}` is needed.
- Hypothesis (I): that independence of `Ω*` from `Ω′` is preserved, so that `K_t(H)` relative to
  the whole world equals its value relative to `Ω*∖H`, and that (2.4) excludes the background bits.
- 2.3(c): the step from periodicity of Ψ to "every record is erased by the next multiple of `P`".
- DT's record-formation clause (R) and its NSC-7 justification; the classification of 2.3(f) and
  (i) against NSC-1..7.
- The DT exclusions and their mapping to NSC-1..7, and whether the CR countercontrol's failure is
  correctly placed at NSC-1 and NSC-3.
- Theorem 3.2's `u`-mass computation and the role of disjointness (M2c).
- That each exact check tests what is claimed of it (§10). E4 is a one-step exhaustive check for
  one box; E5 checks invariance along three trajectories only; the general statements rest on the
  proofs.
- Not done: no literature re-read; no study of the erosion interface, of `q ≥ 3` or of the SM §3.1
  ring; no Lean.

[LIT2] J. Chalupa, P. L. Leath and G. R. Reich, J. Phys. C 12 (1979) L31, and M. Aizenman and
J. L. Lebowitz, J. Phys. A 21 (1988) 3801, on bootstrap percolation, where the closure `cl₂` is
the final infected set of 2-neighbour bootstrap percolation. T. Toffoli and N. Margolus,
*Cellular Automata Machines* (MIT Press, 1987), on second-order reversible rules
`x_{t+1} = f(x_t) ⊕ x_{t−1}`. No result here depends on them.

***

## 10. Exact checks

`checks/deliver_checks.py`. Command, from this directory: `python3 -I checks/deliver_checks.py`
(about ten seconds). Exit status 0 iff every check holds. The reviews' own scripts (full-orbit
invariance for the `2×2×2` box, random-torus invariance, mutation countercontrols, a wider search)
were run by the reviewer and are provenance only; no claim here rests on them.

| Check | Statement tested |
|---|---|
| D1a–b, D2a–b | node 1: CR and bath countercontrols; readiness sequence; per-cycle bound with equality |
| E1 | `g(s) = 1` exactly for `s ∈ {2,3,4}` |
| E2 | complement invariance of `g`; the four patterns of `P` constant on neighbourhoods; all sixteen backgrounds are period-2 solutions (`n = 4`) |
| E3 | Lemma 2.3(a) on the `n = 6` torus; countercontrol at side `n − 1` |
| E4, E4b | Theorem 2.2's step for all 65,536 two-slice perturbations of a `2×2×2` box, on the vacuum and on `(χ, 1⊕χ)`; identical perturbation dynamics (Lemma 2.1) |
| E5, E5b | Theorem 2.2 along three trajectories of 60 ticks (`n = 10`); countercontrol: the support itself moves |
| E6 | Lemma 2.3(c): independence at distance 3; interaction at distance 2 (countercontrol) |
| E7, E7b | 2.3(c) on the closed box `{−e_1, 0, e_1}`: bijection, orbit lengths dividing 4; in this box readiness returns by un-writing |
| E12, E12b | 2.3(f): the review's five-site example embedded in the `n = 8` torus; clause (R) holds |
| E13, E13b | 2.3(h): the re-review's two-carrier example; (R) holds for `a` and fails for `b` |
| E15 | 2.3(i): the third review's six-site example; both records meet (R) |
| E14, E14b | 2.3(g): reduced exhaustive search with a pure vacuum supply; positive control on the (f) pattern |
| E8, E8b | countercontrols: `q = 3` and `q = 2^16` leak; the SM §3.1 ring vacuum conducts |
| E9 | 2.4: survival 7/32 in noise; erosion probabilities 0, 1/4, 1/2 |
| E10 | Lemma 2.3(b): width-2 slab insulates; width 1 does not (countercontrol) |
| E11 | 2.4: a bounded vacuum box in noise has full closure |
| M1 | Theorem 3.1 on PR1's C13 system |
| M2, M2c | Theorem 3.2; countercontrol without disjointness |
| M3 | Theorem 3.3 and 2.3(e): blinker orbit length 2 |

Output at this record's commit:

```text
CHECK D1a conveyor: P(H ready) after ticks 1..4 = ['1', '1', '1', '1/2']: PASS
CHECK D1b conveyor: D0 = K(H u belt) at tick m = (N+1)(1-h2(eps)) with N=m=3 (per-cycle bound attained): PASS
CHECK D2a bath: P(H ready) after ticks 1..4 = ['3/4', '3/4', '3/4', '1/2']: PASS
CHECK D2b bath: D0 = K(H u belt) at tick m = (N+1)(1-h2(eps)) with N=m=3 (per-cycle bound attained): PASS
CHECK E1 binary stencil value is 1 exactly for neighbour sums {2,3,4}: [0, 0, 1, 1, 1, 0, 0]: PASS
CHECK E2 g(y)=g(complement y) on all 64 neighbourhoods; the 4 parity-uniform patterns are constant on every neighbourhood; all 16 (c_even, c_odd) backgrounds are period-2 solutions (n=4): PASS
CHECK E3 boxes with every side <= n-2 (or the full extent) are closed on the n=6 torus; a box of side n-1 is not (countercontrol): PASS
CHECK E4 all 65536 two-slice perturbations of a 2x2x2 box stay in the box for one step, on the vacuum and on the (cb,1+cb) background (the inverse step has the same form): PASS
CHECK E4b the perturbation's next slice is identical on both backgrounds (symmetry): PASS
CHECK E5 along three trajectories (60 ticks, n=10) the support stays in cl2(A0) and cl2(A_t) = cl2(A0) at every tick: PASS
CHECK E5b countercontrol: the support itself is not invariant (it leaves A0): PASS
CHECK E6 two clusters at l1-distance 3 evolve exactly as if alone (40 ticks); at distance 2 they interact (countercontrol): PASS
CHECK E7 apparatus box {-e1,0,e1} is closed; its dynamics is a bijection of 64 states with every orbit length dividing 4: PASS
CHECK E7b centre readiness 1,3/4,9/16,3/4,1 at t=0..4 while K(centre)=2=D0 at every t (in this box readiness returns when the record is un-written): ['1', '3/4', '9/16', '3/4', '1']: PASS
CHECK E12 review example on the n=8 torus: segment closed; orbit lengths 4 (c=0) and 6 (c=1), common period 12; H ready at t=0, depends on c at t=1..4, ready at t=5 for both c, while site 3 holds not-c at t=5: PASS
CHECK E12b clause (R) for E12: site 3 carries no information about c before the first use (t=0): PASS
CHECK E13 re-review example: segment closed; orbit lengths [4, 6, 6, 12]; H ready at [0, 4, 16]; H depends on a at t=[1, 2, 3], on b exactly at t=[5, 6, 7, 8, 9, 10]; sites 2,4 at t=16 determine (a,b): PASS
CHECK E13b clause (R) at t=16: holds for carrier a (first use t=1); fails for carrier b (first use t=5): every log block determining b at t=16 already depends on b before t=5: PASS
CHECK E15 third review's example: segment closed; H ready at [0, 4, 16]; H depends on a at t=[2, 3, 8, 9, 14, 15, 20], on b at t=[7, 8, 17, 18]; site 4 at t=16 determines a and b; (R) holds for both records: PASS
CHECK E14 reduced exact search, pure vacuum supply: no delivery with a determined log in lines 3..7 and boxes 2x2, 2x3, 3x3 with 1-2 carriers, lines 4..6 and 2x3 with 3 carriers (horizon 30); evidence only: PASS
CHECK E14b positive control: the same search routine finds the E12 delivery when given its designed pattern: PASS
CHECK E8 countercontrol q=3 and q=2^16: a single symbol 2 in the vacuum reaches all six neighbours in one step (no box confinement): PASS
CHECK E8b countercontrol SM 3.1 ring (L=9): a single excitation reaches sites [-2, -1, 1] in one step (insulation is specific to the binary rounded-cubic rule): PASS
CHECK E9 a ready site in product-uniform noise stays 0 w.p. 7/32 (= 1 - 25/32); a vacuum site with 1/2/3 noisy neighbours is perturbed w.p. 0/1/4/1/2: PASS
CHECK E10 the complement of a width-2 slab is closed (noise never enters the slab); for width 1 it is not (countercontrol): PASS
CHECK E11 bounded vacuum box 3x3x3 in noise (n=8): cl2(exterior) = whole torus: PASS
CHECK M1 external schedule cell1@t0 -> cell0@t1 'gains' 0 -> 1, but K_t0(cell0) = K_t1(cell0) = 1 (relabelling): PASS
CHECK M2 mu-O invariant (orbit length 3); pointer-selected cell ready w.p. 1; each fixed cell and the external schedule w.p. 1/3 / ['1/3', '1/3', '1/3']; u(H_Q=0) = 1/2; cost d(1||1/2)=1 <= D(muO||u) = 3: PASS
CHECK M2c countercontrol: selection by the cells' own content has u-mass 7/8 (= 7/8), so disjointness of pointer and cells is needed: PASS
CHECK M3 single excitation in the vacuum (n=4) has orbit length 2, so D(mu-O||u) = 127 bits and every block has entropy <= log2(2) = 1 bit under mu-O: PASS
30/30 checks hold
```

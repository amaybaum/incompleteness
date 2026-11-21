# OIQM-UNBOUNDED P3: does C-T scale beyond the typing layer? (research note)

**Standing.** WIP / UNVERIFIED, paper only. This note walks the nodes of `PLAN.md`, which was committed
before any derivation at `7b99fff5`. Issue #1500. PR #1521, stacked on #1516 at `e1715cdd`.

- **Not done here:** no computation, implementation, manuscript edit or merge, and no premise is
  adopted.
- **Citations:**
  - C-T, Lemma P and Proposition V are those of the #1516 NOTE.
  - D-W is GATE-A r5 (#1503 at `fd3cb064`) §2.2.
  - The **Bell ceiling** is the theorem of Main §3.3 (Main:367–370ff.), cited and not reproved.

**Layer tags.** Each result carries three tags:

- **ont / Born**: the ontic layer (measures on configurations, finite-range bijections, outcomes as
  configuration functions) or the Born layer (KIN).
- **ty / snd / op**: typing (availability), soundness, or operational (record laws of a realization
  compared with C-T's Born laws).
- **E / In / Acc**: effect, instrument, or accessible algebra.

**Labels.** (N) native; (I) imported, with each import named.

## 0. Outcome (PLAN §4)

| Question | Outcome | Layer tags |
|---|---|---|
| Operational completeness of C-T with bounded readout duration, across the tower | **OBSTRUCTION**, (I) on (xiv) (Proposition B) | ont, op, E |
| Operational soundness of a native realization | **OBSTRUCTION** to every selector from the listed structural premises (Proposition S). The premise it cannot do without is a quantum-correlation selector, and none is native. | ont, op, E |
| Operational completeness under A5 with linear readout functions, at any delay | **OBSTRUCTION**, (I) on (xiv) (Lemma L, X). The premise it cannot do without is a nonlinear readout function or nonlinear dynamics. | ont, op, E |
| D-W against C-T | **PASS in sketch, (I)**, at the price of an imported trace rule and readout delay that grows with separation (§4) | ont, op, In |
| A native operationally sound and complete realization | **INCONCLUSIVE** | — |

**Main finding.** Scaling, not size, creates the operational difficulty. The tower contains region pairs
at every separation, and C-T carries Tsirelson correlations at every separation. On a finite-range
ontic layer under (xiv):

- reproducing them forces readout delay at least of the order of the separation (B);
- the freedom that permits the delay also realizes laws outside C-T (S).

Operational soundness and completeness at scale therefore need a premise that bounds correlations at the
quantum set. Finite range, determinism, (xiv) and operational no-signalling do not supply it. D-W
supplies it only by computing the trace rule.

## 1. N1: C-T at every separation (Born; ty; In; X; (I) as C-T)

Fix sites `a, b` at graph distance `D` on the binary tower. Within one C-T family on a stage that
contains `a`, `b` and a path between them:

1. Prepare `|Φ⁺⟩` on adjacent sites. This uses H by CC-1 and then CNOT.
2. Move one half to `b` by swap permutations along the path. These are finite-support bijections in
   𝒩⁺.
3. Measure each wing in a setting-rotated basis, using a phase, H, and then configuration readout.

At standard settings the CHSH value is `2√2`. The family is compatible across the tower in the sense of
T1–T3 (#1516 §4).

*Layer note.* The typing layer carries no durations: "move along the path" is one available operation.
Durations enter only at the ontic layer (§2).

## 2. N2: Proposition B (ont; op; E; P; (I) on (xiv))

**Setting.** A realization of C-T's two-wing families on a site-factorized substratum over `ι`, with:

- (i) deterministic dynamics that is finite-range in the kernel's sense (`FiniteRange`,
  QuasilocalAlgebra.lean:919; cones `bwd`);
- (ii) one-step setting interventions on disjoint wing regions `A ∋ a` and `B ∋ b`, each reading and
  writing only its own region;
- (iii) `±1` outcomes recorded in every run, each a function of a readout region `R_A` (`R_B`)
  `k_A` (`k_B`) updates after the setting;
- (iv) (xiv), `p(Ω | x, y) = p(Ω)`.

**Claim.** Suppose the realization reproduces C-T's wing laws for the family of §1 exactly, or with
CHSH above 2. Then

    k_A ≥ d(B, R_A)   or   k_B ≥ d(A, R_B).

Since `R_A` is the wing-`a` readout, `d(B, R_A) ≥ D − diam(A ∪ R_A)`. **Over the tower `D` is unbounded,
so the readout delay is unbounded.** No fixed readout duration serves every size.

**Proof.** Suppose instead that `k_A < d(B, R_A)` and `k_B < d(A, R_B)`.

- The hypotheses are then exactly those of Main §3.3's Bell ceiling.
- For an infinite `ι`, the coupling-graph cone is supplied by `FiniteRange` directly. Main uses the
  finiteness of `V` only to read that cone off the dynamics.
- So CHSH ≤ 2, which contradicts §1. ∎

**Premises, each load-bearing.**

- **Drop (xiv).** Let the setting generators correlate with `Ω`. A response table conditioned on
  `(x, y)` is then exact at `k = 0`. This is Main §3.3's "operational setting screening" remark.
- **Drop the delay bound.** Allow `k_A ≥ D`. Wing A's outcome may then depend on B's setting, and §3
  realizes even the PR box.

**Relation to V.** V (countable `ι`, (xiv)) forces configuration-dependent single-system readouts over a
continuum of settings. B forces delay linear in separation for two-region laws. B uses no countability.
The two are independent obstructions with a common premise, (xiv).

**Classification.** ELABORATING: Main's Bell ceiling applied along the tower. Gem under PLAN (b), since it
is scaling-specific and each premise is shown load-bearing.

## 3. N3: Proposition S, soundness at scale (ont; op; E; P, sketch; (I) on the rule)

**Claim.** Some realization satisfies all of the following, together with the delay `k_A ≥ D` that B
requires, and still produces a record law outside C-T's laws (the PR box, CHSH = 4):

- finite range;
- determinism;
- (xiv);
- operational no-signalling;
- local one-step settings.

Hence none of these premises, alone or together, gives operational soundness.

**Construction (sketch).**

1. Before the settings, a uniform bit `λ` is copied to both wings. This is shared local randomness, so
   (xiv) holds.
2. Wing B outputs `b = λ` immediately.
3. A finite-range signal channel carries `y` from B to A in `D` steps.
4. Wing A outputs `a = λ ⊕ x·y` at `k_A = D`.

The record law satisfies:

- `a ⊕ b = x·y`;
- both marginals are uniform for every setting pair, so operational no-signalling holds.

This is Main §3.3's remark that coupled setting-dependent dynamics realizes PR boxes, made local by
the delay that B forces.

*What the sketch needs.*
- A finite-range bijection that carries `y` to A.
- A gate `a ← λ ⊕ x·y`, which is nonlinear. The nonlinearity can sit in the dynamics, as in a reversible
  universal rule, or in the **readout function**, the observer's function of the visible configuration.
- Under A5 (a linear update, ledger (vii)), one route remains. Take a deterministic known background and
  a nonzero `D`-step coefficient from `B` to `R_A`. The linear dynamics then delivers `y` (plus a known
  constant) to `R_A`, and the readout function computes `λ ⊕ x·y`. So S also holds under A5, provided
  readout functions may be nonlinear. That `D`-step coefficient is nonzero for some pair `(B, R_A)` on
  the selected rule is asserted here and not checked.

**Lemma L (linear readouts; ont; op; E; X; (I) on (xiv); q = 2).**

*Setting.*
- The update is GF(2)-linear (A5).
- Settings `x`, `y` and all other initial bits `z` enter as initial configuration bits.
- The law of `z` is independent of `(x, y)`, which is (xiv).
- Each outcome is a GF(2)-affine function of the configuration at fixed times.

*Claim.* Then CHSH ≤ 2, **at every delay `k`.**

*Proof.*
- Under the stated setting, `a = u·z ⊕ αx ⊕ βy ⊕ γ` and `b = v·z ⊕ α'x ⊕ β'y ⊕ γ'`.
- Hence `E[(−1)^{a⊕b} | x, y] = c · (−1)^{α''x ⊕ β''y ⊕ γ''}`, where `c = E[(−1)^{(u⊕v)·z}]` lies in
  `[−1, 1]`. The bracket is `±1` and takes the form of an affine function of `(x, y)`.
- An affine `f(x, y)` agrees with `x·y` on at most 3 of the 4 setting pairs.
- So `|CHSH| ≤ 2|c| ≤ 2`. ∎

*Consequences.*
- Under A5 with linear readout functions, neither PR laws nor Tsirelson laws arise at any delay. So
  operational completeness of C-T's two-region laws fails whatever the readout time.
- The premise that cannot be dropped is a **nonlinear readout function** (or nonlinear dynamics). S's
  A5 route is the countermodel.
- This settles, for linear readouts, the question of whether linearity excludes PR laws.
- Whether nonlinear readouts under A5 reach exactly the Tsirelson set, and not beyond it, is open.

**Consequence.** An operationally sound and complete realization at scale needs a premise outside
`{finite range, determinism, (xiv), no-signalling, local settings}` that restricts correlations to the
quantum set.

- No such native premise is identified.
- Known information-theoretic candidates do not recover the quantum set exactly in general:
  - information causality (Pawłowski et al., Nature 461, 1101 (2009));
  - macroscopic locality (Navascués and Wunderlich, Proc. R. Soc. A 466, 881 (2010)).
- That no-signalling alone admits PR boxes is Popescu and Rohrlich, Found. Phys. 24, 379 (1994).

**Classification.** ELABORATING, as a corollary of Main §3.3 combined with B. Gem under PLAN (d): it exposes
that operational soundness at scale is a separate obligation from completeness. Bounded-duration
locality gives soundness without completeness, and the delay needed for completeness removes the
locality that gave soundness.

## 4. N4: D-W against C-T (ont; op; In; P, sketch; (I))

D-W is the stepwise Bennett-style simulator. Its ontic state consists of a seed tape, a register holding
the density matrix, program fields, and append-only records. Each step consumes one seed entry, applies
the current instruction's branch rule to the register, and appends the outcome.

Place it on the tower: the register is at one location, and instructions and outcomes travel along
finite-range channels.

| Clause | Verdict | Reason |
|---|---|---|
| T1, embeddings | pass | Enlarging the region tensors the register with the spectator's state. |
| T2, dynamics | pass | Transport is the permutation acting on the register. |
| T3, interface | pass | An instruction on Λ applies branch ⊗ id. This commutes with inclusion and transport. |
| T4, states | pass | Reduced register states are consistent across regions. |
| Operational soundness | pass, by import | D-W computes the trace rule, so every law is a C-T law. |
| Operational completeness | pass | Any finite Kraus instruction can be programmed. |
| B's delay | met | The two wings' instructions must reach the register, so the delay is at least of order `D`. |
| V's readout | met in sketch | The seeds are non-atomic and are read configuration-dependently (#1516 §5.3, INCONCLUSIVE). |
| (xiv) | holds | The seed law is independent of the program, by EP:79 isolation (GA §2.2). |

**Verdict.** PASS in sketch, (I).

- **Imports:**
  - TR: the register stores the density matrix and applies the trace rule. This is the quantum set
    supplied by hand, and it is exactly S's missing selector.
  - A universal reversible finite-range rule, which conflicts with A5.
  - INF.
- **D-W is a countermodel to "C-T cannot scale operationally".** What is obstructed is only bounded
  duration (B) and soundness without a selector (S).
- **D-W meets C-T's operational clauses without any coherence pair at the Born layer** (#1516 §4: D-W
  fails the Born-layer pair). The operational and Born layers therefore come apart at scale exactly as
  they do at fixed size.

## 5. Established / Assumed / Missing

**Established.**

| Result | Tags | Label | Layer |
|---|---|---|---|
| N1: Tsirelson at every separation | Born, ty, In | (I) as C-T | X |
| Proposition B, with its two countermodels | ont, op, E | (I) on (xiv); native finite range | P |
| Proposition S | ont, op, E | (I) on a nonlinear rule or a nonlinear readout function | P, sketch |
| Lemma L | ont, op, E | (I) on (xiv); A5 native | X |
| D-W test | ont, op, In | (I) on TR, rule, INF | P, sketch |

**Assumed** (where each enters):

- **(xiv):** B(iv), and S's shared randomness.
- **Deterministic, finite-range dynamics:** B(i), S. In the kernel, `FiniteRange`.
- **One-step local settings, and `±1` outcomes in every run:** B(ii)–(iii).
- **Nonlinear rule or nonlinear readout function:** S. A nonlinear reversible rule: D-W.
- **TR:** D-W.
- **KIN, CR, DET:** N1 via C-T.

Not assumed: R-READ, READOUT-ALG's finding, the A1 retirement, and the operational meaning of the full
matrix algebra.

**Missing.**

- **The earliest unsupported step is a physical mechanism.** It must be native, and it must confine
  record correlations to the quantum set at scale. The quantum-correlation selector is one obligation.
  The coherence pair is a separate one (O1's two obligations, #1169 c.7066541026).
- **Mathematics:** whether nonlinear readout functions under A5 reach exactly the Tsirelson set.
  Lattice D-W's rule and reach. Whether the selected rule has a nonzero `D`-step coefficient (S, A5
  route).
- **Owner:** whether the ontic Bell branch with parameter dependence (Main §3.2–3.3, the adopted branch)
  is to be paired with a stated selector, or left as an open obligation. Recurrence stays routed (#1504
  AW-U3).

**Productivity verdict.** Gem under (b), for B and for Lemma L with its countermodel; (c), for the D-W
test; and (d), for S. No (a): operational
soundness is not proved natively. The fixed point is not reached.

## 6. Preregistration

None is needed. The candidate PR-U4 (the maximal CHSH value under A5 with linear readouts) is settled on
paper by Lemma L.

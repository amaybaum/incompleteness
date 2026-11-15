# SIGMA12-SCREEN: the non-additive candidate rules (σ12) against route M's K1-scoped statements, r2

**Status: paper-only screen for #866; r1 reviewed (ACCEPT WITH CHANGES); r2 unreviewed.**

**Revision.** r2 applies the independent review of r1 (`REVIEW-SIGMA12-SCREEN-r1.md`, blob
`4280293a`, at `c0e3dcf5`): R1–R5, O1–O8, N1–N2, and the coordinator's wording point on member L.
r1 (blob `c32d54c8`, SHA-256 `e805df73ea39761603d80f383ca3ac0bc70812ba9915c164bec947df3a971259`) is
left unchanged. Dispositions are in `RESPONSE-SIGMA12-SCREEN-r1.md`. The verdict is unchanged.

Hand reasoning and exact hand algebra only. No
computation, simulation, enumeration by program, Lean, manuscript edit, new premise, Issue change,
commit or push. Every [A-inf] is author-side. Nothing here is verification on `main`, and nothing
here counts under SNR-1 until it is independently reviewed.

**Authorization.** Owner `amaybaum`, 2026-11-15, #1169 comment 6891808569, wave 1 item 4: "#866: a
bounded paper-only screen of the non-additive candidate rules (σ12)" (as relayed in the brief; not
re-fetched). Writer: Claude. Results route to #866 (O-REC, MR-1) and to S3's U4.

**Inputs, at exact objects.**
- RO-1 drafts, directory `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`,
  branch `research/ro1-sector-c-1169-20261114` at `f86dd1f791774f68237c8b82ef810855f14dd6d8`:
  - `S3-PLAN-r9.md`, blob `46ebc72d` (cited PLAN; §8.4 check 2, §8.6 (c′), SNR-1);
  - `S3-U4-r1.md`, blob `e6d8101a` (cited U4; §4.5), reviewed REVISE, cited for its σ12 table only;
  - `U4-CALC-r2.md`, blob `bef634e2` (cited CALC; Theorems 1, 2, Propositions 1.4, 2.6, 2.8),
    reviewed ACCEPT (`REVIEW-U4-CALC-r2.md`, blob `70eddf2d`); r1 (blob `fb3d50f8`) was reviewed
    ACCEPT WITH CHANGES. The statements compared here are the same in r1 and r2, except that
    Theorem 2(c) now carries S-L2 [NP], which this screen does not use. The branch head for these
    two files is `c0e3dcf5`;
  - `U4-SOURCES-r1.md`, blob `2e75b886` (cited INV);
  - `S3-U1-r5.md`, blob `68983f86` (cited U1; G1–G7, outcomes, AD-1, C-PREP, C-INT, C-REC, C-RET,
    C-REN), accepted;
  - `VERIFY-SL3-CC-r2.md`, blob `9f81ad0e` (cited VER), with its confirmation
    `REVIEW-VERIFY-SL3-CC-r2.md` (ACCEPT); owner-accepted as relayed in the brief. Its narrower scope
    for S-L3's erasure gloss is the scope screened here.
- Corpus at `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git show`:
  - MR★: `verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md`,
    blob `45af1678` (σ12 at :667, :670–681; S-L1 to S-L7, S-C1 at :491–618; GAP scope at :855–866);
    PREREG `.../preregistration.md`, blob `c36fb14b`;
  - `papers/SM.md`, blob `a5202371` (§3.1, SM:104–112; §6.5, SM:799–811);
  - native-Y: `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md`,
    blob `03857785`; `native-y-continuation-20261024/CURRENT-HANDOFF.md` (the programme directory,
    one level above `shared_v12/`), blob `bfcfb83f`;
  - MR★:674–678 (SUBSTATE-1's scoped results, at `8af2d904`, reachable from `main`), as MR★ states
    them;
  - NIS2: `verification/programmes/oi-qm/reconstruction/native-interaction-source-2-20261110/SOURCE-SCREEN.md`,
    blob `1daf3861`, and `STATUS.md`, blob `67763ae9`;
  - OA-1 `STATUS.md` (blob `39222596`), OA-3 `STATUS.md` (blob `9b1f6f5a`) under
    `verification/programmes/oi-qm/reconstruction/oa-{1,3}-20261112/`;
  - PC-1: `verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/README.md`, blob `08940747`.
- Issue #866 read with the GitHub read tools (planning block, 2026-11-14 state). It defines no σ12
  rule; its rows NATIVE-INT-SRC-2 and "Common physical experimental interface" use the SM ring.

**Labels.** **[proved here]**: a general statement proved by hand in this note; each was re-derived by the r1 review, and the r2 restatements of scope are unreviewed.
**[instance]**: checked by hand on one explicit instance; as a counterexample it disproves the
universal statement it contradicts, and it establishes nothing beyond that instance otherwise.
**[NP]** named premise (§A.46 item 7). **[M]**, **[M-r]** as U1. **[OFF]** off `main`.
**[A-inf]** author-side inference. Outcomes for statements: **holds** (carries over),
**fails** (counterexample given), **undetermined**.

***

## 1. What σ12 is

**Definition** (MR★:667, verbatim except one paraphrase marked): "σ12. Non-additive native-type
rules | native-Y's rule `U_{t+1} = U_{t−1} ⊕ H(⊕_{w∼v} U_t(w))` with `H(A, B, D) = (B, D, A ⊕ BD)`
(on `main`, `native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md`); SM:104–106,
[a coupling graph that varies with the state]; SM §6.5, dynamical links | These are outside
`K★ = {K1}` as frozen … They are not screened for R or Q here." MR★:680–681: "These are the rules on
which conditional dynamics, and so pointers and settings, are not excluded by S-C1." The stage-1 log
(`stage1-log.json`:706) lists the same three. σ12 therefore has exactly three members:

| # | Member | What the corpus actually specifies | Screened here as |
|---|---|---|---|
| Y | native-Y rule | The full rule, at the native-Y boundary (INTERFACE-CONTRACT: "The dynamics is `U_(t+1)(v)=U_(t-1)(v) XOR H(XOR_(w~v) U_t(w))`, `H(A,B,D)=(B,D,A XOR BD)`"), site alphabet `(ℤ/2)³`, six neighbours on a cubic torus | the rule as stated, on a torus with **every side `≥ 3`**, or with `w ∼ v` read as a set relation (each neighbour counted once). Exception: if every side is 2 and `⊕_{w∼v}` runs over the six offsets, each neighbour occurs twice, `F ≡ H(0) = 0` and `φ = σ`, so `σ` is a time shift (the boundary case VER §1.2 records for K1). Native-Y's own side, `256L+64T+1`, is odd and large |
| G | SM:104–106 | A principle, `s(t+1) = φ_{s(t)}(s(t))` with the coupling graph varying with `s` (SM:104), and the second-order form `x_i(t+1) = f(neighbours of i at t) − x_i(t−1) mod q` (SM:106). One explicit member is given at SM:112: on a ring `ℤ/L`, `L ≥ 4`, alphabet `ℤ/q`, `R(i, x) = i+2` if `x_{i+1} = 0`, else `i+1`; `L(i) = i−1`; `x_i(t+1) = x_{L(i)}(t) + x_{R(i,x(t))}(t) − x_i(t−1)` | **G-ring** = the SM:112 member, any `q ≥ 2`, `L ≥ 4`. The class of SM:104–106 is screened only through the statements proved for every rule of form (2.1) below |
| L | SM §6.5, dynamical links | SM:803: the link variable "is determined by the matter field … (§3.1)". SM:809: the map from matter data to links is "under-determined at several enumerable joints". SM:811 states an explicit **candidate map**, the exponential `M(n, ê_j) = exp((2πi/q) Lie[φ(n+ê_j) − φ(n)])`, under which the links are a function of the matter configuration. No **update rule** is stated: no step in which the links act back on the matter, and so no bijection on the substratum to screen | **not screened**: the missing object is that update rule (§5) |

**Identification check.** The binary SM ring `G_SM` of NIS2, OA-3 and U1 is G-ring at `q = 2`. Over
`ℤ/2`, `x_{R(i,x)} = x_{i+1} ∨ x_{i+2}` (if `x_{i+1} = 1` it is read; otherwise `x_{i+2}`), so the
update is `x_{i−1} ⊕ (x_{i+1} ∨ x_{i+2}) ⊕ x_i(t−1)`. NIS2 SOURCE-SCREEN §3 states
`f_i(u) = u_(i-1) XOR (u_(i+1) OR u_(i+2))`, `F(u,v) = (f(u) XOR v, u)`. They agree. [proved here]

**Prior screens, cited, not repeated.**
- PC-1's 25 candidates: a search of `physical-coupling-pc1/` for the native-Y rule, the SM ring and
  `G_SM` found none of them. PC-1's finding is carried only under an owner exception and is not
  validated on `main` (README). [M-r, not a premise here]
- native-Y: "Actual fields contain nonlinear products of the old sign with actual pool operands …
  It is not an isolated available Toffoli or flag gate"; none of 525 radius-two pointers computes the
  target flag, scoped to its families (CURRENT-HANDOFF:39–58). [M-r; MR★ carries it as a record, [NP]]
- G_SM: NIS2 STOPPED / UNSOURCED: boundary coupling and one-tick retention derived on paper; the
  request and common ready precursor unsourced; "Automatic return to the old ready slice:
  **Disproved for that conditional trajectory as a general reset claim**" (SOURCE-SCREEN §5). [M-r]
- SUBSTATE-1 at `8af2d904`, as MR★:674–678 lists it under σ12 with **provenance** standing: "a clean
  single-register pair violates the preparation; the raw echo is masked; a native random setting
  fails the distinct-interaction test; the audited passive-native and read contract supplies no
  selectable setting operation". MR★ does not say which σ12 member each result concerns, and this
  screen did not re-read SUBSTATE-1. The results bear on §4's C-PREP and C-INT rows. They are not
  used as premises here, since their standing in MR★ is provenance, and reconciling their scope with
  Y and G-ring is a blocker (§5).
- G_SM: OA-3 Lemma OBS and Theorem S (STATUS: an additive observer holding three consecutive sites with
  retained history determines the whole configuration within `2(L−3)` ticks; under its hypotheses
  the prepare–measure fragment is a simplex). [M-r]
- Rule-independent: OA-1 Gap 1 / D2 under μ-G "for every bijection"; Gap 3, the configuration-level
  cap "for every rule" (OA-1 STATUS). [M-r]
- The Codex apparatus screen (#866 c.6863601327, NAS) is cited only through U1's rows. [OFF]

## 2. Common frame and general lemmas

Both screened rules have the second-order form

    φ(x, y) = (y, F(y) − x)                                                     (2.1)

on `S = G^Λ × G^Λ` (previous slice `x`, current slice `y`), with `G` an abelian group:
- **Y:** `G = (ℤ/2)³`, `F(y)(v) = H(⊕_{w∼v} y(w))` (in characteristic 2, `−x = x`);
- **G-ring:** `G = ℤ/q`, `F(y)_i = y_{i−1} + y_{R(i,y)}`.

K1 is (2.1) with `F = A` linear. U1's frame is used throughout: bare model, `φ` the only step, `Obs`
read-only (AD-1(c)), both slice forms A-reg and A-cur (AD-1(b)), budget below recurrence (AD-1(f)),
H-μ of CALC (carrier law `λ`, every non-carrier region uniform and independent; `λ` uniform is μ-G).

**Lemma G-1 (S-L3 bullets L3a, L3b, L3d) [proved here].** (L3a) for every rule (2.1); (L3b) for
every rule (2.1) with `F ≢ 0`; (L3d) for every bijection of a finite set.
- (L3a) `σφσ = φ^{−1}`: `φ^{−1}(a, b) = (F(a) − b, a)` and `σφσ(a, b) = σφ(b, a) = σ(a, F(a) − b)`.
- (L3b) If `F ≢ 0`, `σ` is no time shift. If `σ = φ^k`, then `σφ = φσ`, so `φ = σφσ = φ^{−1}` and
  `φ² = id`. The first component of `φ²(x, y)` is `F(y) − x`; equal to `x` for all `x, y` gives
  `F(y) = 0` at `x = 0`. *Y:* on a torus with some side `≥ 3`, or under the set reading of `∼`, take
  `j ∼ v` along such an axis: `F(rδ_j)(v) = H(r) ≠ 0` for `r ≠ 0` (`H` is a bijection with `H(0) = 0`:
  its inverse is `(p, q, r) ↦ (r ⊕ pq, p, q)`). If every side is 2 under the six-offset reading,
  `F ≡ 0` and `σ = φ` (§1). *G-ring:* for `y = δ_{i−1}`, `y_{i+1} = 0` (so `R = i+2`) and `y_{i+2} = 0`
  since `L ≥ 4`, so `F(y)_i = 1`.
- (L3d) On finite `S`, `φ^{−1} = φ^{N−1}`, `N` the order of `φ`; under G1 every joint-state
  transformation a program effects is some `φ^n`.

**Lemma G-2 (VER Sup-1, block swaps) [proved here, under (CC)].** This is not a statement about every
rule (2.1). It needs the **coupling condition**

    (CC) for every proper nonempty region X there are i ∈ X, j ∉ X and r ≠ 0 with F(rδ_j)_i ≠ 0.

Under (CC), no map `τ = σ_X ⊕ g`, `X` a proper nonempty region, `g` any map on the complement, is a
time shift. *Proof.* With `s = (0, rδ_j)`, `(τs)_X = 0`, so the previous slice of `φτs` vanishes on
`X`, while `τφs` has previous slice `F(rδ_j)|_X` there, nonzero at `i`. `□`
- *(CC) for Y:* on a torus with every side `≥ 3`, or under the set reading of `∼`: any adjacent pair
  `i ∈ X`, `j ∉ X`, which exists on the connected torus, gives `F(rδ_j)_i = H(r) ≠ 0`. With a side 2
  under the six-offset reading, neighbours along that axis cancel, and (CC) can fail.
- *(CC) for G-ring:* `j = i − 1` (the left neighbour is always read, with coefficient `1`); some `i ∈ X`
  has `i − 1 ∉ X` because `X` is proper.
- *Countercontrol (from the review):* over `ℤ/2`, let `F` vanish on `X` and act only within a separate
  component `X^c`. Then `φ = σ_X ⊕ φ|_{X^c}` is itself a block swap and a time shift (`k = 1`). (CC)
  fails there, and so does the lemma.

**Lemma G-3 (VER Sup-2) [proved here].** For every bijection of a finite set: `φ^n φ^m = id` needs
`N | n + m`; with `m ≥ 1`, `n ≤ T`, `m + T < N`, no available `φ^n` inverts an `m`-step marking.

**Lemma G-4 (CALC Proposition 1.4, every rule (2.1)) [proved here].** Under H-μ, a marker region `A`
is completely masked at `t = 0` and `t = 1`, for every carrier law, both slice forms, every geometry.
*Proof.* `t = 0`: `A` holds its own uniform content. `t = 1`: for fixed content of every region but
`A`, `(x_A, y_A) ↦ (y_A, F(y)|_A − x_A)` is a bijection of `S_A` (recover `y_A`, then `x_A`); its
current-slice part is a bijection in `x_A`. `s_A` is uniform and independent of the rest, so the
readable content is uniform and independent of the carrier. `□`

**Lemma G-5 (CALC Proposition 2.8(i), its partition-independence clause, every rule) [proved here].** A readable region's
law depends only on `φ` and the initial law. Under H-μ the law of `Σ^c` is uniform on `S_{Σ^c}`
however `Σ^c` is partitioned, so declaring a marker region changes no law at any tick.

**Lemma G-6 (CALC Proposition 2.6 analogue: no return before the crossing time) [proved here].**
Hypotheses beyond the form (2.1) and finite speed: for Y, that `H` is a bijection; for G-ring, that
the left-neighbour read enters with coefficient `1` and is never the selector of `R`. Both are
properties of the two rules, not of (2.1).
- *Y.* Let `v ∈ Σ`, `e` an axis, `1 ≤ t < ℓ/2` with `ℓ` the torus side along `e`, and
  `p := v − te ∉ Σ`. Then `u_t(v)` is uniform on `(ℤ/2)³` given all initial content except `y_p`.
  *Proof.* Write `p_s = p + se`. Influence spreads at most one site per tick, so at tick `s` the
  neighbours of `p_{s+1}` other than `p_s` (ℓ1 distance `s + 2` from `p`) and `u_{s−1}(p_{s+1})` do not
  depend on `y_p`, also after the torus wrap since `ℓ > 2t`. So
  `u_{s+1}(p_{s+1}) = c ⊕ H(u_s(p_s) ⊕ r)` with `c, r` free of `y_p`. By induction from `u_0(p) = y_p`,
  `u_t(v)` is a bijective function of `y_p` for fixed other content. `□`
- *G-ring.* Let `i ∈ Σ`, `1 ≤ t < L/3`, `i − t ∉ Σ`. Then `u_t(i) = y_{i−t} + G` with `G` not depending
  on `y_{i−t}`. *Proof.* Influence moves right only through the left-neighbour read (+1 per tick) and
  left by up to 2 per tick, so at tick `s` it occupies `[i − t − 2s, i − t + s]`. In
  `u_{s+1}(j) = u_s(j−1) + u_s(R(j)) − u_{s−1}(j)` with `j = i − t + s + 1`, the terms `u_s(j+1)`,
  `u_s(j+2)` (selector and value of `R`) and `u_{s−1}(j)` lie outside that interval on the ring when
  `3s + 3 < L`. The term `u_s(j−1)` enters with coefficient `1` and is never the selector. `□`
- *Consequence.* If `λ`'s marginal on the current slice of `v` (resp. `i`) is not uniform (for example
  a point carrier, an assumed preparation, U1 C-PREP), the carrier–marker joint law does not return
  at `t`, under A-reg and A-cur. In native-Y's actual geometry the torus side is `256L+64T+1` with
  `L = P + 262` (INTERFACE-CONTRACT), so the bound covers every tick of that programme's horizon.
- *Standing under SNR-1.* G-6 is a proved negative. It rests on an assumed carrier preparation
  (U1 C-PREP), so it concerns an assumed apparatus and **does not count** under SNR-1. It concerns
  transport of background into the carrier and return of the joint law, not recording, as CALC-F5
  does on K1.

**Lemma G-7 (no ready region under μ-G, every rule) [proved here].** The counting measure is invariant
under every bijection, so under μ-G every region's marginal is uniform at every tick. This is MR★:642
and OA-1 D2 without the K1 hypothesis.

**Counterexamples.** All are [instance]; rest of the configuration fixed at `0` unless stated.

- **C-1 (Y, operational I-sel, U1 C-INT).** `v` with neighbours `w`, `w₂`. Carrier: sites `{v, w}`;
  selector: site `w₂`, current slice `z`; `Y = v`, `t = 1`. Then
  `pr_v φ(s) = (y_v, x_v ⊕ H(y_w ⊕ z))`. Carrier values `P1 = 0` and `P2`: `x_v = (0,1,0)`,
  `y_w = (0,0,1)`. At `z = 0`: `P1 ↦ (0, 0)`; `P2 ↦ (0, (0,1,0) ⊕ H(0,0,1)) = (0, (0,1,0) ⊕ (0,1,0)) = (0, 0)`:
  one class. At `z = (0,1,0)`: `P1 ↦ (0, H(0,1,0)) = (0, (1,0,0))`;
  `P2 ↦ (0, (0,1,0) ⊕ H(0,1,1)) = (0, (0,1,0) ⊕ (1,1,1)) = (0, (1,0,1))`: two classes. The induced
  partition depends on `z`.
- **C-2 (G-ring, a switch).** Selector `i+1` (current `z`), carrier `i+2` (current `c`), `Y = i`,
  `t = 1`: `u_1(i) = c` if `z = 0`, and `u_1(i) = z` otherwise. Discrete partition of `c` at `z = 0`,
  trivial at `z ≠ 0`. The selector turns the coupling of `i` to the carrier on and off.
- **C-3 (S-L5's separability).** "Records" here means S-L5's structural hypothesis, the analogue of
  `Φ_{AΣ}s_Σ ≠ 0`: the marker's content depends on the carrier's. Under μ-G the marker's own content
  masks it at `t = 1` (G-4), so no informational record is claimed.
  - *Y:* as in C-1, `Σ = {v, w}`, marker `w₂`, and `D = v ⊂ Σ` (S-L5's first bullet, the carrier's
    later state). The marker's content `m` enters `D` as `H(c ⊕ m) ⊕ H(c)`, with `c = y_w`. At
    `m = (0,1,0)` this is `(1,0,0)` for `c = 0` and `(1,0,1)` for `c = (0,0,1)`: it depends on the
    carrier. `w₂` meets the hypothesis through `y_v`: its current slice at `t = 1` is
    `x_{w₂} ⊕ H(y_v ⊕ …)`, bijective in `y_v`. So `w₂` depends on `y_v`, while its effect on `D`
    depends on `y_w`.
  - *G-ring:* as in C-2, with `D = i`. `u_1(i) = m + (c − m)[m = 0]`, so the marker's effect on `D`
    relative to `m = 0` is `(m − c)[m ≠ 0]`, which depends on `c`. Site `i+1` meets the hypothesis:
    `u_1(i+1) = c − x_{i+1}` for every `c` when the rest is `0`.
- **C-4 (S-L7's invariance).** The support `{x = 0}` of the valid epistemic state fixed by all
  previous-slice readouts (a Lagrangian set of readouts) is mapped by `φ` to the graph
  `{(y, F(y))}`. That graph is a coset only if `F` is affine. *Y:* `y_a = (0,1,0)` at `w`,
  `y_b = (0,0,1)` at `w₂`: `F(y_a ⊕ y_b)(v) = H(0,1,1) = (1,1,1)`, but
  `F(y_a)(v) ⊕ F(y_b)(v) ⊕ F(0)(v) = (1,0,0) ⊕ (0,1,0) = (1,1,0)`. *G-ring:* `a = δ_{i+1}`,
  `b = δ_{i+2}`: `F(a)_i = 1`, `F(b)_i = 1`, `F(a+b)_i = 1 ≠ 2 = F(a)_i + F(b)_i − F(0)_i` in every
  `ℤ/q`, `q ≥ 2`.
- **C-5 (G-ring, partial masking under μ-G for two point paths).** CALC Instance 1.1's geometry:
  `L = 4`, `q = 2`, `Σ = {3, 0}`, `A = {1, 2}` uniform, no environment, A-reg at `t = 2`. With `∨` as in
  §1,

      u_1(i) = y_{i−1} + x_i + (y_{i+1} ∨ y_{i+2}),
      u_2(i) = u_1(i−1) + (u_1(i+1) ∨ u_1(i+2)) + y_i.

  `U_1 := u_1(1)` and `U_2 := u_1(2)` contain `x_1` and `x_2` additively, so they are uniform and
  independent of `(y_1, y_2)` and of the carrier. The readable tuple is equivalent to
  `(U_1, U_2, a, b)` with `a = u_2(1)` and `b = u_2(2) + U_1`, and `U_1` drops out. Path L is `y_3 = 1`,
  path R is `y_0 = 1`, other carrier content `0`. Then `(a, b)` as a function of `(y_1, y_2)`:

  | `(y_1,y_2)` | L, `U_2=0` | L, `U_2=1` | R, `U_2=0` | R, `U_2=1` |
  |---|---|---|---|---|
  | (0,0) | (1,1) | (0,1) | (1,1) | (1,1) |
  | (0,1) | (1,0) | (1,0) | (1,0) | (0,0) |
  | (1,0) | (0,1) | (0,1) | (1,1) | (1,1) |
  | (1,1) | (1,1) | (0,1) | (0,0) | (1,0) |

  Checked by direct substitution at `x = y = 0` on `A` (path L): `u_1(0) = 1`, `u_1(1) = u_1(2) = 1`,
  `u_1(3) = 0`, `u_2(1) = u_2(2) = 0`, which agrees with the row (0,0) at `U_2 = 1`. The laws of
  `(U_2, a, b)` given L and R overlap on `(0,1,1)`, `(0,1,0)` and `(1,1,0)`, with equal mass `1/2` on
  the overlap in both. For `W` uniform on {L, R}: **`I(W; Y_2) = 1/2` bit**, strictly between `0` and
  `H(W) = 1`.

## 3. The K1-scoped statements, rule by rule

| Statement (scope screened) | native-Y (Y) | G-ring (SM:112) | Support |
|---|---|---|---|
| **S-L3 at VER's narrower scope** (owner-accepted): (a) no available operation is `σ` | **holds** (some side `≥ 3`, or the set reading) | **holds** | G-1 [proved here]; every rule (2.1) with `F ≢ 0` |
| (b) no global block swap `σ_X ⊕ g` | **holds** (every side `≥ 3`, or the set reading) | **holds** | G-2 [proved here], under (CC), checked for Y and G-ring only |
| (c) no inverse of a marking within a budget below recurrence | **holds** | **holds** | G-3 [proved here]; every bijection |
| (d) no region selects the map applied to another (S-C1(a)) | **fails** | **fails** | C-1, C-2 [instance] |
| VER Sup-3, marginal swap without erasure | holds (`X = {v}`, zero neighbour current: `(y_v, x_v)`) | holds as for K1 (twisted swap; a swap over `ℤ/2`) | direct |
| **S-L5**, structural part: the marker affects a later test of the carrier only through an offset that does not depend on `s_Σ` | **fails** | **fails** | C-3 [instance] |
| S-L5 (ii), loss of *observed interference* only by carrier-independent injection | undetermined | undetermined | needs (γ) and T0 on these rules; the structural premise (S-L1) is absent |
| **S-L7**, single-time kinematics (current-slice readouts isotropic; current and previous slice of one site conjugate) | holds | holds | definitional on `S` with `J`; rule-independent |
| S-L7, invariance in time (`MᵀJM = J`) | **fails** | **fails** | C-4 [instance]: one tick takes a valid epistemic state to a non-coset |
| S-L7, the consecutive-tick pair `(0, e_v)`, `(−e_v, A e_v)` | undetermined | undetermined | the next-tick current readout is a nonlinear functional; the bracket statement has no counterpart |
| **CALC Theorem 1**, Proposition 1.4 (masking at `t ≤ 1`) | **holds** | **holds** | G-4 [proved here], every rule (2.1), independent of CALC |
| Theorem 1(a), (b), (d): the marker holds exactly a class in `R_A/K_t` | does not apply (no homomorphism `M_t`, no subgroup `K_t`) | does not apply | — |
| Theorem 1(c): two point paths are masked all-or-nothing | undetermined at `t ≥ 2` | **fails** at one instance: `I = 1/2` bit | C-5 [instance] (`L = 4`, `q = 2`, one path pair, one tick, point-prepared carriers) |
| **CALC Theorem 2**, Proposition 2.6 analogue: no J-return before the crossing time, for a carrier marginal that is not uniform | **holds**, `t < ℓ/2` | **holds**, `t < L/3` | G-6 [proved here] under its rule-specific hypotheses; conditional on an assumed carrier preparation |
| Theorem 2(a)–(c): returns only at scalar ticks `φ^t = γ·id`; the window condition | undetermined | undetermined | Lemmas 2.1–2.4 use additivity (convolution, the leakage group, Chebyshev form) |
| Theorem 2(d): every return is global | undetermined | undetermined | a conditional subsystem return is not excluded beyond G-6's scope (§4) |
| Proposition 2.8(i), partition-independence clause: no marker declaration changes `D`'s law | holds | holds | G-5 [proved here]; rule-independent |

**Label dependence.** The CALC rows compare with Theorems 1 and 2 as stated in CALC r2, which is
reviewed ACCEPT. The statements compared are the same in r1. G-4 to G-6 and C-5 are proved or checked
here directly and do not use CALC's proofs, so they stand whatever further review of CALC finds. Only
the words "carries over" and "fails to carry over" depend on CALC's K1 statements. If CALC's
Theorem 1(c) were wrong on K1, C-5 would still show that it is false at its G-ring instance.

**What the failures have in common** [A-inf]. On Y and G-ring every failure traces to S-L1
(additivity), through S-C1(a). The surviving statements use bijectivity, the form (2.1) and μ-G's
invariance (G-1(a), G-1(d), G-3, G-4, G-5, G-7). G-1(b) also needs `F ≢ 0`. G-2 also needs the coupling
condition (CC). G-6 also needs finite speed and each rule's own structure: `H` bijective for Y, and for
G-ring the unit coefficient of the left-neighbour read. On Y and G-ring, as on K1, global time reversal
within budget is not available. What fails is the K1 conclusion that no conditional, subsystem-level
operation exists.

## 4. U1: availability of a which-path marker and of a reversal

U1's four outcomes (§2.3): available / unsourced / requires assumed apparatus / not available
(disproved). Only "not available" counts under SNR-1, and only at the disproof's scope and status.

| Action | native-Y | G-ring (G_SM at `q = 2`) | dynamical links |
|---|---|---|---|
| **Which-path marker, C-REC with C-PREP** | **Unsourced.** No ready (quiet) region under μ-G (G-7). A uniform marker is masked at `t ≤ 1` (G-4); `t ≥ 2` is undetermined. Native coupling with nonlinear products exists, but no isolated available gate was found [M-r, scoped]. Retention C-RET is not addressed. SUBSTATE-1's preparation result (MR★:675) is listed in MR★ with provenance standing and is not used (§1) | **Unsourced.** Boundary write and one-tick retention derived; request and ready precursor unsourced (NIS2 [M-r]). [A-inf, from C-5] A uniform two-site marker holds a carrier functional at one tick without retention of `s_A` (`1/2` bit for one path pair). C-5's carriers are point-prepared, which is [assumed] (U1 C-PREP), as for CALC §3's instances. Whether that partition is which-path is (γ); persistence (C-RET) is not addressed. OA-3 Lemma OBS records a whole configuration for an additive observer with retained history, and that retention is itself unsourced (O-RET) | undetermined: no update rule |
| **Reversal U: global inverse, swap, block swap, within budget** | **Not available** at VER's narrower scope (G-1 to G-3; G-2 under (CC)) [proved here; re-derived in the r1 review]. It rests on criterion clauses (G1, AD-1(f)), not on a capability. It counts under SNR-1 only after review | **Not available**, as for Y | undetermined |
| **Reversal U, J-return form:** the carrier–marker joint law returns | **Not available** before `ℓ/2`, i.e. over native-Y's whole horizon, for a carrier whose current marginal is not uniform (G-6). It rests on an assumed carrier preparation, so it concerns an assumed apparatus and **does not count** under SNR-1 | **Not available** before `L/3`, under the same condition and the same SNR-1 standing (G-6) | undetermined |
| **Reversal U, weaker forms** (for example the marker decorrelated from the carrier while the carrier is transported; a subsystem uncomputation at or after the crossing time) | **Unsourced, not disproved.** At VER's narrower scope, the K1 exclusion of a selected subsystem operation rested on S-C1(a) (VER §1.5 notes that MR★'s wording "no subsystem undo" goes beyond what is verified on K1), and S-C1(a) fails here (C-1). [A-inf] Such an uncomputation *may* need a blank supply. That is open: a reversible conditional gate can uncompute a conditional marking without an ancilla, and no source shows a blank is necessary. If one is needed, Lemma R [NP] and G-7 leave none under μ-G (C-REN). A native gate would be needed, and none isolated is found [M-r, scoped] | **Unsourced, not disproved.** C-2 shows conditional coupling. The automatic return of one conditional trajectory is disproved (NIS2 [M-r]), which is not a general obstruction | undetermined |
| **Setting-selected operation (C-INT I-sel)** | present in `φ` (C-1); its setting record and inputs unsourced. SUBSTATE-1's setting results (MR★:677–678) are listed in MR★ with provenance standing and are not used (§1) | present in `φ` (C-2; U1's G_SM row agrees); inputs unsourced | undetermined |

[A-inf] On Y and G-ring the which-path marker is **unsourced**, not disproved. Two negatives are proved
here.
- **No global reversal within budget** (G-1 to G-3). It is the same negative that holds on K1, and it
  does not reach a which-path record.
- **No joint-law return before the crossing time** (G-6). It rests on an assumed carrier preparation,
  so it does not count under SNR-1. It concerns transport and return, not recording.

Weaker forms of undo are not excluded on these rules.

## 5. Consequence for route M's gating item (c′)

PLAN §8.6 (c′): "The σ12 rules (check 2) are screened for recording, with any negative resting on
sourced capabilities only (SNR-1). MR-1 did not screen them. This is #866 work."

**Verdict: partly done.**
- *Done, reviewed at r1:* σ12's members are identified (§1). For Y and G-ring, the K1-scoped
  statements route M uses are classified: what holds, what fails with a counterexample, and what is
  undetermined (§3). U1's availability is set out for the marker and the reversal (§4).
- *Result that bears on gating* [A-inf]. On Y and G-ring, the K1 obstructions that rest on additivity
  fail: S-C1(a), S-L5's structural part and S-L7's invariance on both; Theorem 1(c) at one G-ring
  instance. The K1 obstructions used toward a negative closure of route M therefore do not extend to Y
  and G-ring.
- *The negatives here.* G-1 to G-3 do not reach a which-path record. G-6 concerns an assumed apparatus
  and does not count under SNR-1. So (c′) contributes no negative toward closing route M.
- *Not done, and what it is blocked on:*
  1. **Member L (dynamical links):** SM:811 states a candidate map from matter data to links, and no
     update rule in which the links act back on the matter. The missing object is that update rule. A
     screen conditional on SM:811's candidate map would first need such a rule. No statement is made
     about L.
  2. **SM:104–106 beyond the SM:112 member:** G-1(a), G-1(d), G-3, G-4, G-5 and G-7 apply to every rule
     of form (2.1); G-1(b) needs `F ≢ 0` and G-2 needs (CC). Within the SM class, the counterexamples
     and G-6 are about G-ring only. Further members are not specified in the corpus.
  3. **Carrier preparation (C-PREP):** C-5's point paths and G-6's non-uniform carrier both use an
     assumed preparation. No sourced carrier preparation is on record for Y or G-ring under μ-G (G-7;
     OA-1 Gap 1 for selected hidden carriers, every bijection [M-r]).
  4. **The recording screen proper:**
     - R1 on Y at `t ≥ 2`;
     - R1 on G-ring beyond C-5's single instance (`L = 4`, `q = 2`, one path pair, one tick);
     - persistence under C-RET; R3; R4 (amplification); R5.

     These are blocked on a sourced ready marker region (G-7; MR★ C-3's analogue), on retention
     (O-RET, #1032), and on calculations of the CALC kind at larger `t` and other geometries, which
     this authorization does not cover.
  5. **SUBSTATE-1's scoped results** (MR★:674–678, at `8af2d904`): reconcile which σ12 member each
     concerns, and their bearing on C-PREP and C-INT, from SUBSTATE-1's own record. They carry
     provenance standing in MR★ and are not used here.
  6. **Interference-level statements** (S-L5 (ii), D-1 on σ12): blocked on (γ) (Main:682) and on T0.
  7. **SNR-1 standing:** nothing here counts until r2 is reviewed. G-6 does not count even then, since
     it rests on an assumed preparation (blocker 3).

So the gating sentence's σ12 item is not satisfied. A negative closure of route M through (c′) would
need a negative on recording for Y, G-ring and L that rests on sourced capabilities. This screen finds
none. Of the K1 obstructions it might have used, several are shown to fail on Y and G-ring.

## 6. Findings (§A.31 classes)

| # | Finding | Check | Class |
|---|---|---|---|
| SG-1 | S-L3's narrower-scope components (a) and (c) hold for every rule (2.1) with `F ≢ 0` ((c) for every bijection); (b) holds under (CC), checked for Y and G-ring; component (d) fails on both | G-1 to G-3; C-1, C-2 | NEW at corpus level, routine algebra: separates the part of erasure unavailability that is pure reversibility from the part that is additivity |
| SG-2 | S-L5 fails structurally on Y and G-ring | C-3 | CONFIRMING U4 §4.5's [A-inf] "S-L5 does not hold on these rules", now with instances |
| SG-3 | S-L7's invariance fails: one tick of Y or of G-ring takes a valid epistemic state outside the valid class | C-4 | NEW: AW-MR5's symplectic route to a GNC model (CC4's class) does not transfer to Y and G-ring. For G_SM, OA-3 Theorem S reaches a simplex by another route, under its own hypotheses |
| SG-4 | CALC Proposition 1.4 holds for every rule (2.1); Theorem 1(c)'s all-or-nothing masking fails at one G-ring instance (`I = 1/2` bit) | G-4; C-5 | NEW: on G-ring (one instance), partial masking under μ-G needs no biased marker |
| SG-5 | No joint-law return before the crossing time on Y and G-ring, for a localized prepared carrier; a negative that does not count under SNR-1 | G-6 | ELABORATING CALC-F5: holds on Y and G-ring as on K1 |
| AW-σ1 | Assumption-watch: any route-M statement citing S-C1(a), S-L5 or S-L7 for "no subsystem undo", "marking cannot destroy interference" or "epistemic restriction" is not shown beyond K1, and fails on Y and G-ring. Statements transfer only with the hypotheses listed in §3's closing paragraph | §3 | marker for U4, D-1 and MR-1 stage 2 |
| AW-σ2 | Assumption-watch: a blank supply is not a necessary premise of uncomputation on a rule with conditional dynamics unless sourced | §4 (review R4) | marker for any undo or renewal argument on Y or G-ring |

Fixed-point note: this is a single bounded pass; §A.31's fixed-point criterion is not claimed.

## 7. Not decided

- Theorem 1 on Y at `t ≥ 2`, and on G-ring beyond C-5's instance.
- Theorem 2(a)–(d) on Y and G-ring beyond G-6's bounds. In particular, whether a joint-law return
  below recurrence can be local, that is not a global map.
- Whether a subsystem uncomputation, or another weaker form of undo, is executable on either rule, and
  whether it needs a blank supply.
- Whether a GNC model exists for either rule under single-time current-slice access (S-L7's route
  fails; OA-3 covers G_SM only under its hypotheses).
- Member L as a whole; the SM:104–106 class beyond SM:112; SUBSTATE-1's member scope.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Claim attached | Classification |
|---|---|---|
| PLAN, U4, INV, U1, VER and its review on `research/ro1-sector-c-1169-20261114` at `f86dd1f7`; CALC r2, its review and this screen's review at `c0e3dcf5` | the questions posed; U1's criterion and outcomes; VER's narrower scope; CALC's statements compared; the review findings applied | support off `main` (gap), as in U4 §9 and CALC §6. Every proof here uses only the rules on `main` and lines cited at `75cc5100` |
| SUBSTATE-1 at `8af2d904` (reachable from `main`) | listed only, as MR★:674–678 states it | provenance, as in MR★; not used |
| #1169 c.6891808569; the owner acceptance of VER, as relayed | authorization; the scope screened for S-L3 | governance provenance; not re-fetched |
| #866 c.6863601327 (Codex screen, NAS) | U1's rows only | provenance; not used |

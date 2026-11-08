# M-INACC-1: result

**Standing.** WIP / UNVERIFIED. Checkpoint 2 of the paper-only research unit
M-INACC-1 under #1169. Writer: Claude Code session, 2026-11-08. Independent
review pending. Paper derivation; nothing adopted, no theorem promoted, no
manuscript edited, no Lean built, no V3 round run.

**Governing text.** `DESIGN.md` at `75c0befcb324466cb4bf0e90c7ef3cbe429b58ad`,
as amended by `amendments/A1-prereg-review.md` (at
`bcf2aba49d5f991b404c24dedbce6910470fda27`) and
`amendments/A2-a1-confirmation.md` (at
`90e950e51a452f0aaacb274b4e00657184181bea`). Where they differ, the amendments
govern. None of the three files is edited here. Section numbers prefixed `D`,
`A1.` and `A2.` refer to those files.

**Review record before this result.** The reviewer's records are on draft PR
#1198:

- [c.6719123056](https://github.com/amaybaum/incompleteness/pull/1198#issuecomment-6719123056)
  (DESIGN review, 2026-11-08T08:12:02Z);
- [c.6719242384](https://github.com/amaybaum/incompleteness/pull/1198#issuecomment-6719242384)
  (A1 confirmation, 08:25:17Z);
- [c.6719247117](https://github.com/amaybaum/incompleteness/pull/1198#issuecomment-6719247117)
  (A2 confirmation, accept for derivation, 08:25:49Z).

These are provenance. The A2.5 timing check (confirmation before the first
push of this file) is recorded by the coordinator from the host's PR events.

**Source snapshot.** Analysis sources are pinned to `main@f88c1842`
(`f88c184220453badfc9279ab9a86b6785e4db5ff`). Abbreviations as in `DESIGN.md`:
M2D, QA, PR-QA, FB, M1D, AP1.

## 0. Result

1. **The construction.** `G_σ` (D§2.1), written in closed form, is
   `f_i(u) = OR(u_{i−1}, u_{i−2}) ⊕ OR(u_{i+1}, u_{i+2})`. Each side
   contributes the OR of its two nearest sites. This is an identity of (1),
   since `u_{i+1} + (1 + u_{i+1}) u_{i+2} = u_{i+1} ∨ u_{i+2}` over `F_2`
   (self-check c4).
2. **Node 1.** Step (s1) of Lemma Q(iii)'s proof fails for `G_σ` by
   inspection. (s2), (s3) and (s5) fail with it. (s4) transfers. `Q` is
   conserved (C-EX-Q green); conservation does not carry the protection.
3. **`Π_B`: (B-D).** The protocol `E_B` (§2) arms the gated edge `{−1, 1}`
   alone. It reads both slots of the gate cell 0 without disturbing it. At
   `t = 2` that active, unregistered cell is sharp, and its `u + v`
   (`Q* = 1`) is determined in every record branch. `E_B` relies on the `Π_B`
   multiplier convention and on the A1.5 registrability rule. `Π_B`'s outcome
   does not rest on `E_B` alone, since `E_A` below lies in `Π_A ⊂ Π_B`.
4. **`Π_A`: (B-D).** The protocol `E_A` (§3) uses the fixed rule always on,
   P2 ready cells, and P1 registration with refill. It needs no arming,
   isolation, translations, heralds or feedback. It determines `u + v` of an
   active, unregistered source cell in every record branch.
   - **Mechanism.** The reading cell's unknown slot reaches the target twice:
     through the nearest-neighbour edge, and as the gate of the edge from the
     target to the next site. With that next site at 1 the two contributions
     cancel, because `OR(α, 1) = 1` whatever `α` is. The read then carries no
     backaction.
   - **Variant `E_A′`.** It uses only known-0 supplies (no H-PREP value 1) and
     exposes the same functional in a branch of probability 1/16 under N2
     (B-D). On the stated instance it also biases that functional in every
     other branch, so with known-0 supplies it gives (B-B) with probability 1
     (§3.3).
   - **Controls.** CC-OFF is green: with every gate held at 0 or at 1, the
     same protocols determine and bias nothing of `Q* = 1` type (C-LIN proof,
     and self-checks c1–c3).
5. **Controls.**
   - Green: CC-OFF-1, CC-OFF-0, C-EX-Q, C-P1, C-P2, C-IMPORT, C-AVG, C-NS,
     CC-NC (in its (B) form), and C-LIN for PROT-D and PROT-B (including the
     `G_SM` countercontrol).
   - **C-LIN is red for PROT-R.** PROT-R fails in both linear limits through a
     one-tick protocol (§6.3). A2.1 adopted PROT-R on the premise that the
     linear limits satisfy it, and that premise is false. Every verdict that
     relies on PROT-R is void: no (B-R) verdict is issued here, and outcome
     (A), which requires PROT-R, is unreachable under the amended rule for
     any rule, QA's N included. Neither class's outcome relies on PROT-R.
   - C-L3 (diagnostic): AP1 Lemma 3's isotropy fails under `G_σ`.
   - C-MEAS: not applicable, since no (A) proof is offered.
   - SC-1: none found. SC-2 and SC-3: reported (§8).
6. **Outcome labels** (generated in §8 from D§4.2 and A1.3):
   - `Π_A`: (B), type (B-D);
   - `Π_B`: (B), type (B-D).

   The pair is (B, B). The attribution is to the gate of `G_σ` together with
   the `Π_A` resources used, archive-swap refills included.
7. **Owner tiers (A2.6), one per class, `Π_A` first:**
   - `Π_A`: **Negative**;
   - `Π_B`: **Negative**.

   No combined tier is reported.
8. **What the negative says.** Within the registered scope (`G_σ`, the stated
   classes, P1, P2), the symmetric state-dependent graph does not preserve
   Lemma Q(iii)'s protection. State dependence gives a gate whose influence is
   one-way, and edge symmetry at fixed `u` does not make the full map
   reciprocal.
   - The negative concerns `G_σ` and these classes only.
   - The first premise that would block both exhibited `Π_A` protocols, under
     A2.4, is P-GK (§4): every gate acting on a present edge has a value fixed
     by `K` when it acts. The reviewer ruled P-GK admissible under A2.4's
     intended reading. In `Π_A` it is degenerate: every unknown `v` slot
     becomes an unknown `u` slot, hence an unknown gate, after one tick, and
     the hidden sector enters every cone, so P-GK empties `Π_A` of nontrivial
     protocols. It is reported, not adopted, and CC-RECON applies.

## 1. Node 1: transfer audit of Lemma Q(iii)'s proof

The steps are those of A1.4: (s1)–(s4) from QA's proof
([QA:458](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L458)),
and (s5) from AP1 Lemma 3's affine uniformity
([AP1:533](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L533)).

| Step | Content in the linear class | Status for `G_σ` | Reason |
| --- | --- | --- | --- |
| (s1) | Given all records, each branch is a fixed sequence of symplectic center-free linear steps and constant translations | Fails | A branch is a fixed sequence of the nonlinear bijection `F_σ`, whose quadratic terms `u_{i±1}u_{i±2}` (D§2.2) make it non-affine. It transfers under the added condition P-GK (§4): when every gate of a present edge has a value fixed by `K` at the tick it acts, the step restricted to the branch support is the linear symmetric center-free step of a fixed graph |
| (s2) | AP1 Lemma 3: the determined functionals on active cells are the isotropic span of transported known slots and registered records | Fails with (s1) | The proof needs linear transport. Under `F_σ` a record is a nonlinear function of the initial variables, and conditioning gives non-affine supports. Transfers under P-GK |
| (s3) | `Q*` is preserved when a functional is transported through a step (Lemma Q(ii)) | Fails | The pullback of a linear functional through `F_σ` is not linear, so `Q*` of the transported functional is undefined. Lemma Q(i), conservation of `Q`, holds (C-EX-Q), but (s3) uses the linear transport `M^{−T}`, not `Q` itself. Transfers under P-GK |
| (s4) | `Q*` is additive on an isotropic subspace | Transfers | A fact about quadratic forms over `F_2`, independent of the dynamics |
| (s5) | Conditional laws are uniform on affine subspaces | Fails with (s1) | Nonlinear records give non-affine supports, as M2D's P★ shows. Transfers under P-GK |

The first step that fails to transfer is (s1). As A1.4 notes, this is not
informative on its own; §4 names the premise.

**C-LIN on the audit** (§6.3): applied to `N_1` and `N_0`, every step holds.
Applied to `G_SM`, the audit fails at Lemma Q(i) (M2D Lemma Qσ(b)) and at (s3),
as required.

## 2. Node 2: exposure routes in `Π_B`

### 2.1 R-G: the protocol `E_B`

Sites are labelled relative to the target cell `0`. The ring has `L ≥ 5`.

- **Region and initial cells (`t = 0`).** `R = {−1, 0, 1}`.
  - Cell 0 is a source cell `(u, v) = (x, y)`, both slots unknown.
  - Cell −1 is a ready cell with known `v = 0` and unknown `u = α`.
  - Cell 1 is a ready cell with known `u = 1` (P2 through H-PREP) and unknown
    `v = β`.
  - Every other site holds a hidden source cell.
- **Multipliers at ticks 1 and 2.** The gated edge `{−1, 1}`, whose gate is
  cell 0, has multiplier 1. Every other edge has multiplier 0: the edges
  `{−1, 0}` and `{0, 1}`, every edge joining `R` to its complement (E-iso),
  and the gated edges `{−2, 0}` and `{0, 2}`.
- **Tick 1.**

  ```text
  u_{−1}(1) = v_{−1} + (1 + x)·u_1 = 1 + x,     v_{−1}(1) = α
  u_1(1)    = v_1 + (1 + x)·α = β + (1 + x)α,   v_1(1) = 1
  u_0(1)    = v_0 = y,                          v_0(1) = x
  ```

  Cell 0 has no edge with multiplier 1, so it takes a free tick.
- **Between ticks 1 and 2.** Register `u_{−1}(1)`, giving record
  `r_1 = 1 + x`. Register `u_1(1)`, giving record `s_1 = β + (1 + x)α`. Both
  cells are archived. Refill site −1 with a ready cell (known `v = 0`,
  unknown `u = α′`) and site 1 with a ready cell (known `u = 1`, unknown
  `v = β′`).
- **Tick 2.** `u_{−1}(2) = 0 + (1 + u_0(1))·1 = 1 + y`. Register it, giving
  record `r_2 = 1 + y`. Cell 0 takes a free tick: `(u_0(2), v_0(2)) = (x, y)`.

**Exposure.** In every record branch, cell 0 at `t = 2` is active,
unregistered, and has determined slots `(x, y) = (1 + r_1, 1 + r_2)`. The
functional `u_0 + v_0` (`Q* = 1`) has the point-mass conditional law at
`r_1 + r_2`. Extra records such as `s_1` only shrink the support of a branch
and cannot undo a determination. Exposure type (B-D); PROT-B fails with it.
Self-check c3 confirms the identities on a stated instance.

**Resources and conventions (A2.2 reporting).**

| Item | Used | Note |
| --- | --- | --- |
| Gate of `G_σ` | Yes | CC-OFF below |
| P3 multipliers | Yes | At ticks 1 and 2 the gated edge `{−1, 1}` is armed while the nearest-neighbour edges at its endpoints and gate (`{−1, 0}`, `{0, 1}`) are disarmed. The exposure relies on the `Π_B` multiplier convention |
| Registrability rule (A1.5) | Yes | The only armed edge of cell −1 is gated by an unknown gate (cell 0). The registration of `u_{−1}` relies on the second case of A2.2. Arming in addition a nearest-neighbour edge `{−2, −1}` to a ready cell with known `u = 0` leaves `r_1` unchanged and makes the registration valid under both alternatives of A2.2 as well. That variant is stated, not separately self-checked |
| E-iso | Yes | Isolation of `R` |
| Known-1 cell (H-PREP) | Yes | Cell 1. Not needed in `Π_A` (`E_A′`) |
| P1, P2, refills | Yes | — |
| Vacancies, translations, feedback, heralds | No | — |

**CC-OFF on `E_B`.**

- With every gate held at 1, the edge `{−1, 1}` is absent and `r_1 = r_2 = 0`;
  cell 0 takes free ticks and nothing about it is recorded.
- With every gate held at 0, `r_1 = r_2 = u_1 = 1`.
- In both limits `u_0 + v_0` is uniform given the full joint record
  (self-check c3, and the C-LIN proof of §6.3).
- This control is weak. Under `N_1` the only armed coupling disappears, and
  under `N_0` cell 0 has no coupling to the readers at all. It shows only that
  the gate is the sole channel of `E_B`. `Π_B`'s verdict rests on `E_A`
  (§3.2), whose CC-OFF exercises the reader's backaction itself (§3.4).

### 2.2 The remaining `Π_B` routes

R-G decides `Π_B` as (B-D). Routes R-N, R-R, R-T and R-C are not walked for
`Π_B`, since the walk stops when each class has an outcome (D§4.3).

## 3. Node 3: `Π_A`

`E_B` is not in `Π_A`: it needs multipliers and isolation. The routes are
walked in `Π_A` in order. The first, R-G, exposes.

### 3.1 The mechanism: the reader as a gate

By the OR form, the update of the target cell 0 is

```text
u_0′ = v_0 + OR(u_{−1}, u_{−2}) + OR(u_1, u_2).
```

The left term is the nearest-neighbour edge `{−1, 0}` (coefficient `u_{−1}`)
plus the gated edge `{−2, 0}`, whose gate is cell −1 (coefficient
`(1 + u_{−1}) u_{−2}`). If `u_{−2} = 1`, then `OR(u_{−1}, 1) = 1` whatever
`u_{−1}` is. A reading cell at −1 with an unknown `u` slot then exerts no
backaction on cell 0, while its own update
`u_{−1}′ = v_{−1} + OR(u_{−2}, u_{−3}) + OR(u_0, u_1)` reads `u_0` whenever
`u_1 = 0`.

In the linear class the reader's unknown is exactly the kick that keeps the
conjugate slot hidden (AP1 §4.1). Under `G_σ` the gated edge cancels it.

### 3.2 The protocol `E_A` (exposure in every branch)

- **Region and initial cells (`t = 0`).** `R = {−3, …, 2}`, and every site
  outside `R` holds a hidden source cell. The ring has `L ≥ 6`, and no cone
  winds (H-NW).
  - Cell 0 is a source cell `(x, y)`.
  - Cell −1 is a ready cell with known `v = 0` and unknown `u = α_1`.
  - Cell −2 is a ready cell with known `u = 1` (P2 through H-PREP).
  - Cells −3, 1 and 2 are ready cells with known `u = 0`.
- **Tick 1** (`F_σ` everywhere). `f_{−1}` reads sites −3…1 and `f_0` reads
  −2…2, all in `R`:

  ```text
  u_{−1}(1) = 0 + OR(1, 0) + OR(x, 0) = 1 + x
  u_0(1)    = y + OR(α_1, 1) + OR(0, 0) = y + 1,     v_0(1) = x
  ```
- **Between ticks 1 and 2.** Register `u_{−1}(1)`, giving record
  `r_1 = 1 + x`. Register `u_j(1)` for `j ∈ {−3, −2, 1, 2}`; these records
  exist only to archive the cells. All five cells are archived and their sites
  refilled to the `t = 0` specification:
  - cell −1: known `v = 0`, unknown `u = α_2`;
  - cell −2: known `u = 1`;
  - cells −3, 1 and 2: known `u = 0`.
- **Tick 2.**

  ```text
  u_{−1}(2) = 0 + OR(1, 0) + OR(y + 1, 0) = y          → register: r_2 = y
  u_0(2)    = x + OR(α_2, 1) + OR(0, 0) = x + 1,        v_0(2) = u_0(1) = y + 1
  ```

**Exposure.** In every record branch, cell 0 at `t = 2` is active and
unregistered, with `(u_0(2), v_0(2)) = (r_1, r_2 + 1)`. Its `u + v`
(`Q* = 1`) has the point-mass conditional law at `r_1 + r_2 + 1`. Exposure
type (B-D) with branch probability 1, non-adaptive. PROT-D, PROT-B and AP1
Lemma 3's isotropy all fail for `Π_A`. Determination is a statement about
support, so the verdict holds for every full-support prior (A1.11).
Self-check c1 confirms the four identities pointwise on a stated instance.

### 3.3 The variant `E_A′` (known-0 supplies only)

This variant removes H-PREP's value-1 supply from the exposure.

- **Region and initial cells.** `R = {−4, …, 2}`, with `L ≥ 7`.
  - Cell 0 is a source cell `(x, y)`.
  - Cell −1 is a ready cell with known `v = 0` and unknown `u = α`.
  - Cell −2 is a ready cell with known `v = 0` and unknown `u = w`.
  - Cells −4, −3, 1 and 2 are ready cells with known `u = 0`.
- **Tick 1.**

  ```text
  r_1 := u_{−1}(1) = OR(w, 0) + OR(x, 0) = w + x
  s_1 := u_{−2}(1) = OR(0, 0) + OR(α, x) = α ∨ x
  u_0(1) = y + OR(α, w),   v_0(1) = x
  ```
- **Between ticks 1 and 2.** Register `r_1`, `s_1`, and the `u` slots of
  cells −4, −3, 1 and 2. Archive all six and refill them to the `t = 0`
  specification, with fresh unknowns `α_2` and `w_2` at −1 and −2.
- **Branch `s_1 = 0`** (probability 1/4 under N2). In this branch `α = 0` and
  `x = 0`, so `w = r_1` and `u_0(1) = y + r_1`. Write `z := u_0(1)`.
- **Tick 2.** `r_2 := u_{−1}(2) = w_2 + z` and `s_2 := u_{−2}(2) = α_2 ∨ z`.
  In the branch `s_2 = 0` (conditional probability 1/4), `z = 0`, so
  `u_0(2) = x + OR(α_2, w_2) = 0 + w_2 = r_2` and `v_0(2) = z = 0`.

**Exposure.** In the branch `s_1 = s_2 = 0` (probability 1/16 under N2), cell
0 at `t = 2` is active and sharp, `(u_0(2), v_0(2)) = (r_2, 0)`, and its
`u + v` has the point-mass law at `r_2`. Exposure type (B-D). Self-check c2
confirms the branch probability 1/16, the point mass on that branch, and
uniformity in both linear limits.

**Bias in the other branches.** On c2's instance, under `G_σ`, all 256 record
branches give `u_0(2) + v_0(2)` a non-uniform conditional law. The 64 branches
with `s_1 = s_2 = 0` are determined. The other 192 are biased, with
conditional probabilities of the value 1 in `{1/3, 4/9, 5/9, 2/3}` (the
reviewer's check, repeated by the writer on the same instance). With known-0
supplies only, `E_A′` therefore gives (B-B) with probability 1 on that
instance. This is an additional exposure; the (B-D) verdict is unchanged.

### 3.4 Resources, CC-OFF and attribution for `Π_A`

| Item | `E_A` | `E_A′` |
| --- | --- | --- |
| Gate of `G_σ` | Used (CC-OFF) | Used (CC-OFF) |
| P2 ready cells, known value 0 | Used | Used |
| Known value 1 (H-PREP) | Used (cell −2) | Not used |
| N2 (uniform unknowns) through H-PREP | Not needed for determination | Gives the branch probability 1/16 |
| P1 registration, archive-swap refills used as gate settings (A1.6) | Used: the refills reset `u_{−2}`, `u_{−3}`, `u_1` and `u_2`, which fix the OR terms | Used |
| P3, E-iso, vacancies, translations, feedback, heralds | Not used | Not used |
| Multiplier convention (A2.2) | Not used (`Π_A`) | Not used |
| Registrability rule (A2.2) | Not relied on: every registered cell had nearest-neighbour edges of coefficient 1, fixed by `K` | Not relied on |

- **CC-OFF.** With every gate held at 1 (`N_1`) or at 0 (`N_0`), `u_0 + v_0`
  is uniform given the full joint record in every branch, for both protocols
  (c1, c2). For example, under `N_1`, `u_0(1) = y + α_1` is masked by the
  reader's unknown. This holds for every protocol in the linear limits by the
  C-LIN proof (§6.3).
- **D-ATTR.** The outcome pair is (B, B), so by A1.3 the exposure is
  attributed to the gate of `G_σ` together with the minimal `Π_A` resources:
  P2 ready cells with known value 0, P1 registration, and archive-swap
  refills. N2 enters `E_A′` only through its branch probability.

### 3.5 Remaining `Π_A` routes

R-G decides `Π_A`. Routes R-N, R-R, R-T (`Π_B` only) and R-C are not walked
for this outcome. R-C is treated in §5.

## 4. Node 4: protection proofs, and the premises that would block the exposures

**Protection proofs.** No class is without an exposure. No protection proof
is offered, and outcomes (A), (A′), (C-D), (C-B) and (C-R) do not arise.

**Blocking premises under (B)** (D§4.2 (B); content and reporting rules of
A2.4). Each candidate is a statement about `G_σ`, the protocol class or the
supplies. Candidates are ordered by the earliest step of (s1)–(s5) they
secure. Each is reported and not adopted, and CC-RECON applies to each, since
its only motivation here is to block the exposure.

| Order | Candidate | Step secured | Blocks | Assessment |
| --- | --- | --- | --- | --- |
| 1 | **P-GK** (class): at every tick, every gate of a present edge (in `Π_B`, of an edge with multiplier 1) has its `u` value fixed by `K` when it acts | (s1), hence (s2), (s3) and (s5) | `E_B`, `E_A`, `E_A′` (in each, a gate acting at tick 1 is unknown: cell 0 in `E_B`, cell −1 in `E_A` and `E_A′`). Under P-GK every branch is a fixed sequence of linear symmetric center-free steps of a branch-dependent graph, and QA's proof applies verbatim, giving PROT-D and PROT-B for the class so restricted | In `Π_A` every site is the gate of an edge, so P-GK excludes every unknown `u` slot from the protocol's cone, hidden sector included. It is degenerate in `Π_A`: an unknown `v` slot becomes an unknown `u` slot, hence an unknown gate, after one tick, and the hidden sector enters every cone, so P-GK empties `Π_A` of nontrivial protocols. **Content:** P-GK mentions knowledge of gate slots, which have `Q* = 0`. The reviewer ruled it admissible under A2.4's intended reading, which excludes restatements of the protected `Q* = 1` conclusion and of PROT-*, not restrictions on the protocol class |
| 2 | **P-NR** (supplies): no site within distance 2 of an active cell whose slot is unknown is refilled during a protocol | No step secured | `E_A` and `E_A′` as written (each needs fresh known neighbours for the second read); `E_B` (refills of −1 and 1) | Whether P-NR blocks every exposure in `Π_A` is not decided. In `Π_A`, P1 is implemented by the refill swap, so P-NR forbids registration near unknown active cells, which is close to forbidding all registration in `Π_A`: nearly degenerate |
| 3 | **P-1** (supplies): no ready cell with known value 1 | No step secured | `E_A` and `E_B` as written | Does not block `E_A′` (§3.3), so it does not block the exposure in `Π_A` |
| — | A statement about `G_σ` itself | — | — | **No candidate found.** `G_σ` is fixed (D§2.1, A1.8), and no property of `G_σ` other than its gate dependence was identified as load-bearing |

## 5. Node 5: composition

- **Composites cannot restore protection.** PROT-D fails for one system
  (`E_A`, `E_A′`), and Q1 quantifies over all active functionals (D§3.5).
- **Parallel exposures.** Each identity of `E_A` reads only sites −3…2 of its
  own window. Copies of `E_A` on targets spaced at least 6 sites apart, run in
  parallel, therefore have disjoint windows. They make every target sharp at
  `t = 2` and determine every linear functional supported on those targets.
  This consequence follows by inspection of the windows and is not
  separately self-checked.
- **Cross-system exposure.** With adjacent systems `W_1` and `W_2` in the
  joint class, a cell of `W_2` is exposed by `E_A` whenever sites −3…−1, 1
  and 2 relative to it are sites of the joint region. A system's cells are
  exposed by a neighbour's apparatus within range 2.
- **Relative functionals.** These are moot, since absolute `Q* = 1`
  functionals are exposed.
- **C-NS for separated systems.** Green; see §6.

## 6. Controls and countercontrols

### 6.1 Table

| ID | Pass criterion (preregistered) | Measurement | Status |
| --- | --- | --- | --- |
| CC-OFF-1 | An exposing protocol run with every gate held at 1 exposes nothing (D§5 with A1.7, A2.1) | `E_A`, `E_A′`, `E_B` under `N_1`: `u_0 + v_0` uniform in every branch (c1–c3). For every protocol: §6.3 | Green |
| CC-OFF-0 | The same, with gates held at 0 | The same under `N_0` (c1–c3; §6.3) | Green |
| C-EX-Q | `G_σ` conserves `Q`; `G_SM` and `G_σ` plus a center term must break it; D§2.2 properties hold | `Σ_i u_i f_i(u) = Σ_{e ∈ E(u)} 2u_iu_j = 0`, so `Q` is conserved. c4 at `L = 6`: 0 of 4096 configurations change `Q` under `G_σ`, `N_1` and `N_0`; 1664 under `G_SM`; 2048 under `G_σ` plus center term. OR form and explicit inverse confirmed (c4). Symmetry, center-freeness and gate exclusion by inspection of the OR form | Green |
| C-LIN, PROT-D and PROT-B | The node-1 audit applied to `N_1` and `N_0` reproduces QA's proof under this unit's conventions (A1.7) | §6.3: proof with reserve cells for refills, vacancies, multipliers, direct registration, no heralds | Green |
| C-LIN, `G_SM` countercontrol (A1.17) | The audit applied to `G_SM` fails at Lemma Q(i) and at (s3) | Lemma Q(i) fails by M2D Lemma Qσ(b) (c4: 1664 of 4096 at `L = 6`). (s3) fails because `G_SM`'s step is non-affine (term `u_{i+1}u_{i+2}`), so linear transport is undefined | Green |
| C-LIN, PROT-R (A2.1) | PROT-R verified in `N_1` and `N_0`; if it fails there, C-LIN is red for every verdict that relies on PROT-R | PROT-R **fails** in both limits (§6.3, c5) | **Red.** It voids every PROT-R verdict: no (B-R) verdict is issued, and outcome (A) is unreachable as amended. No outcome of this unit relies on PROT-R |
| C-P1 | P1 removed must expose (A2.7 variant (i); A1.16 variant (ii)) | (i) Registering `u` and `v` of a cell at one moment while it stays active determines its `u + v`, an active `Q* = 1` functional. (ii) Re-coupling a registered meter as in AP1 C9 makes the partner cell sharp. Both by definition, under any rule | Green (breaks as required) |
| C-P2 | P2 removed must expose | A supplied cell with known `u + v` has that functional determined while active, under any rule | Green (breaks as required) |
| C-L3 | Report AP1 Lemma 3 isotropy under `G_σ` | Fails: cell 0 is sharp at `t = 2` in `E_A` (every branch), `E_A′` (branch 1/16) and `E_B` | Reported (diagnostic) |
| CC-NC | Under (B): state that the exposure is configuration-level and Theorem NC is unaffected | Stated (§6.4) | Green (criterion met) |
| C-IMPORT | (i)–(v) of D§5 | §6.5 | Green |
| C-AVG | Verdicts per record branch on the entire joint record | `E_A`, `E_B`: every branch. `E_A′`: the branch `s_1 = s_2 = 0`. No average is used | Green |
| C-MEAS | An (A) proof says where it uses setting quantification | No (A) proof | Not applicable |
| C-NS | Separated systems: complete local history laws independent of remote settings; a violation voids composition verdicts | `G_σ` is a fixed bijection with one-step dependency range 2. For separated systems the dependency cones of the two wings' records and outgoing cells are disjoint, and their initial variables are independent (H-PS). Each wing's complete local history is a function of its own cone's variables and its own settings, so its law is independent of remote settings (Main's cone theorem, [Main:364](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/papers/Main.md#L364), applied to `F_σ`) | Green |
| SC-1 | A positive finding is a C-IMPORT failure | No unitary, interference, CP restriction or comparator enters any premise or verdict | Green (none found) |
| SC-2, SC-3 | Reported | §8 | Reported |

### 6.2 The `Q` invariant does not protect

`Q = Σ u_i v_i` is conserved by `G_σ`. Yet `E_A` produces a sharp active
cell. The two are consistent: `Q` is a single global quadratic invariant
(archived and refill cells included), while Lemma Q(iii)'s protection rests on
the linear transport of `Q*` in (s3). M2D left open whether a symmetric
switched graph, which keeps `Q` (Lemma Qσ(a)), keeps the protection
([M2D:860–864](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L860)).
For `G_σ` it does not.

### 6.3 C-LIN: the linear limits under this unit's conventions

**Setting.** Take `N_1` or `N_0`, in `Π_A` or `Π_B` form. Steps are symmetric,
center-free and linear, with multipliers in `F_2`. Represent:

- every cell ever supplied as a **reserve** cell present from `t = 0`,
  decoupled and taking free ticks until it is injected;
- a refill as the swap of a reserve cell into the site and of the old cell
  into the archive, where it is decoupled thereafter;
- a vacancy as a decoupled cell.

Free ticks, symmetric center-free steps, multipliers and cell swaps are all
linear, symplectic for `ω`, and conserve `Q`: Lemma Q(i), plus the fact that a
cell permutation permutes the terms of `Q`. Given the records, the settings
of each branch are fixed, including adaptive ones. Translations are
constants.

**PROT-D.**

- The knowledge set is an affine subspace of the initial variables, cut out
  by the known slots `I` and the registered slots `R`.
- A linear functional `f` on active cells at `t` is determined iff
  `f ∈ span(I_t ∪ R_t)`.
- `I_0` consists of single slots on distinct cells, so it is isotropic and
  `Q* ≡ 0` on its span (s4). Transport preserves both properties, so they
  hold for `I_t`.
- Each record is a slot of a cell that is archived at once. Records on
  distinct archived cells commute, and a re-registration repeats the same
  transported functional, so `Q* ≡ 0` on `span(R_t)`.
- For `f = κ + ρ` with `κ ∈ span I_t` and `ρ ∈ span R_t`:
  `Q*(f) = Q*(κ) + Q*(ρ) + ω(κ, ρ) = 0 + 0 + ω(f + ρ, ρ) = ω(f, ρ) = 0`.
  The last step holds because `f` lies on active cells and `ρ` on archived
  cells.
- This is AP1 Lemma 3 with QA's Lemma Q argument, extended to reserve cells,
  which have disjoint support. Green.

**PROT-B.** The prior is the uniform product (N2, H-PS) and the constraints
are affine, so the conditional law in a branch is uniform on the affine
knowledge set. A linear functional that is not constant there is uniform
(s5). Green.

**PROT-R fails.** Take any ring, every cell a ready cell with known `u = 0`
and unknown `v`. Tick 1 gives `u_0(1) = v_0(0) + f_0(0) = v_0(0)`. Register
`u_0(1)`. The functional `u_0(0) + v_0(0)` of cell 0, active at `t = 0`, has
`Q* = 1` and is determined at `t′ = 1`. This holds under `N_1`, `N_0` and
`G_σ` alike (c5). The general reason: Lemma 3 bounds what is determined about
**active** cells, but an archived cell can be sharp. Its registered slot and
its transported known slot need not commute, so `span(I_t ∪ R_t)` contains
`Q* = 1` functionals supported on archived cells.

A2.1 rested on the claim that "`span(I_t) + R` has `Q* ≡ 0` on terminal and
active cells together". The claim originated in the reviewer's confirmation of
A1 (finding G1). It is false, and the results review confirms this. PROT-R as amended therefore
fails for QA's N itself, and the exposure it detects here is trivial: the
ready cell's own unknown slot. Consequences under A2.1's own clause:

- C-LIN is red for PROT-R-dependent verdicts;
- no (B-R) verdict is issued;
- (A) is unreachable under the amended rule for every rule.

The defect does not bear on the (B-D) outcomes, which rest on PROT-D and
PROT-B, both green in C-LIN, and it voids no verdict of this record.

**PROT-R′, for successor units only.** Amendment A3, a post-result
amendment that affects no decision of this unit, records the corrected
property:

> PROT-R′(Π): for `t ≤ t′` and a `Q* = 1` functional `f` on the cells active
> at `t`, such that `f(t)` is a function of the configuration of the cells
> active at `t′` alone, `f(t)` is neither determined nor biased given `K` at
> `t′`.

In the linear limits PROT-R′ holds. Transport, free ticks and swaps carry
`f(t)` to a linear functional `f′` on cells active at `t′` with
`Q*(f′) = 1`. Lemma Q(iii) at `t′` (as verified above) then excludes
determination, and (s5) gives uniformity. The countercase above is excluded,
because it depends on the archived cell 0. PROT-R′ is not adopted and decides
nothing here. Under `G_σ` in `Π_A`, `E_A` violates it already at
`t = t′ = 2`, where PROT-R′ reduces to PROT-D.

### 6.4 CC-NC

The exposures are configuration-level facts. A cell of the lattice becomes
sharp. Theorem NC
([M2D:483](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md#L483))
is unaffected, and no nonclassicality is claimed.

Two consequences, stated for context:

- A sharp cell under R1 has `r = ((−1)^z, (−1)^x, (−1)^{z+x})` with
  `|r|² = 3`, which is not a valid encoded state.
- Four sharp preparations of one cell are pairwise perfectly distinguishable.
  That is AP1's E-AR situation
  ([AP1 C4](https://github.com/amaybaum/incompleteness/blob/f88c184220453badfc9279ab9a86b6785e4db5ff/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L677)).

So, under `G_σ`, P1 and P2 do not keep a cell a `C²` carrier in `Π_A`.

### 6.5 C-IMPORT

- (i) D§2.1 contains no quantum quantity.
- (ii) PROT-D and PROT-B were decided at configuration level, over `F_2`. R1
  appears only in §6.4.
- (iii) No restriction was added to `Π_A` or `Π_B` at or after this first
  `RESULT.md` commit. The class definitions applied are those of `DESIGN.md`
  with A1 and A2.
- (iv) The blocking premises of §4 are reported and not adopted, and CC-RECON
  is applied.
- (v) The protected class is QA's `Q* = 1` class.

Green.

## 7. Clause (a), USE-ctx and RO-2

- **Clause (a), USE-ctx.** Not evaluated. A1.1 evaluates clause (a) only under
  (A). Protection fails, so clause (b) of M-INACC fails for the `Q* = 1`
  class in both classes, and USE-ctx does not bear on the outcome.
- **RO-2** (A1.2). In both classes every linear functional of a single cell,
  and every linear functional supported on cells at least 6 sites apart, is
  determinable (§3.2, §5). Whether every linear functional the dynamics uses
  is determinable is not decided: adjacent cells cannot be targeted at once
  by `E_A` as written.

## 8. Outcome per class, tiers, and shortcut checks

**Outcomes, generated from D§4.2 (B) and A1.3.**

| Class | Exposure exhibited | Type | Controls on that verdict | Outcome |
| --- | --- | --- | --- | --- |
| `Π_A` | `E_A` (every branch); `E_A′` (branch probability 1/16) | (B-D); PROT-B also fails | CC-OFF-1 and CC-OFF-0 green; C-EX-Q green; C-LIN green for PROT-D and PROT-B; C-AVG green; C-IMPORT green; C-NS green | **(B)** |
| `Π_B` | `E_B` (every branch); `E_A ∈ Π_A ⊂ Π_B` | (B-D) | As for `Π_A` | **(B)** |

- **Pair.** (B, B), which is admissible.
- **Attribution (A1.3).** To the gate of `G_σ` together with the `Π_A`
  resources used: P2 ready cells with known value 0, P1 registration, and
  archive-swap refills. `Π_B`'s added resources (P3, E-iso, known value 1) are
  sufficient through `E_B` and are not necessary.
- **Hypotheses carried.**
  - Into both verdicts: G-σ, Nq (`q = 2`), P1 with the archive-swap (refill)
    implementation, P2, H-NW, and the finite ring (A1.20).
  - Into `E_A′`'s branch probability: N2 and H-PS.
  - Into `E_A`: H-PREP for the known value 1.
  - Into `E_B`: P3, E-iso, and the A2.2 conventions.

**Owner tiers (A2.6).** These map the outcomes; they change none of them.

| Class (reported in this order) | Tier |
| --- | --- |
| `Π_A` | **Negative**: the mechanism does not satisfy the conditions within its registered scope. `E_A` exposes the protected information |
| `Π_B` | **Negative** |

No combined tier is reported.

**SC-2, hidden external control.**

- Supplied in `E_A`: the region design, the ready cells and their known
  values, the registrations, and the refills. Archive-swap refills act as gate
  settings (A1.6).
- No P3, E-iso, translation or feedback is used in `Π_A`.
- The coupling that cancels backaction is native to `G_σ`: the reader's own
  value gates the compensating edge.

**SC-3, representation versus physical implementation.** The exposed object is
the pair of slots of a lattice cell, a configuration-level object. No encoded
representation enters the verdict.

## 9. Classification (§A.31) and assumption-watch markers

| Finding | Class |
| --- | --- |
| Backaction cancellation by the reader as gate (OR saturation): under `G_σ` a cell's `u` slot is read without disturbing its `v` slot, using only `Π_A` resources. Lemma Q(iii)'s protection and AP1 Lemma 3's isotropy fail for `G_σ` under P1 and P2 | NEW |
| `Q` conservation (Lemma Qσ(a)) does not imply protection; the protection rests on linear `Q*` transport (s3) | NEW (resolves M2D's open item for `G_σ`) |
| PROT-R fails in QA's linear class: archived cells can be sharp, so retrodictive `Q* = 1` protection does not hold even with Lemma Q. The false premise came from the reviewer's G1; PROT-R′ (A3), for successor units only and not adopted, restricts retrodiction to information held by cells still active, and holds in the linear limits | NEW (a defect in amendment A2.1) |
| C-LIN: Lemma Q(iii) and PROT-B extend to refills, vacancies, multipliers and direct registration in the linear limits | CONFIRMING |
| `G_σ`'s closed form `f_i = OR(u_{i−1}, u_{i−2}) ⊕ OR(u_{i+1}, u_{i+2})` | ELABORATING |

**Assumption-watch markers.**

- **Symmetric edges do not make a reciprocal map.** In a state-dependent
  graph the gate's influence is one-way, whatever the symmetry of the edges at
  fixed `u`. A protection argument that uses reciprocity has to treat gates
  separately. This applies to any switched-graph proposal, including
  preparation-indexed edges (H-Bell) whose presence depends on cell values.
- **Saturating nonlinearities cancel backaction.** Any rule in which an
  unknown value enters a target through two paths that can cancel (here
  `a + (1 + a)·1 = 1`) can give backaction-free reads. Linear rules cannot,
  which is QA's case.
- **Retrodictive protection.** A protection statement for hidden information
  has to state whether it covers past values. Lemma Q(iii) covers present
  active functionals only.

## 10. Self-checks (controls on this record's algebra; not evidence)

Each check is one stated instance, sums only over that instance's own unknown
bits (16 at most), and searches no space of protocols, rules or instances.
Arithmetic is integer over `F_2` with `Fraction` conditional laws. The checks
are not committed.

| Check | Instance | Unknown bits | Arithmetic | Purpose |
| --- | --- | --- | --- | --- |
| c1 | `E_A` on `L = 8`: `R = {−3, …, 2}`, hidden sources at sites 3 and 4; mode `G_σ`, `N_1`, `N_0` | 16 (`x`, `y`, `α_1`, 4 unknown `v`, 4 hidden, 5 refill) | Pointwise identities; conditional law of `u_0(2) + v_0(2)` given all 6 records | Identities `r_1 = 1 + x`, `r_2 = y`, `u_0(2) = x + 1`, `v_0(2) = y + 1` hold in all 65 536 assignments. `G_σ`: determined in all 64 branches. `N_1`, `N_0`: uniform (1/2) in all 64 branches |
| c2 | `E_A′` on `L = 8`: `R = {−4, …, 2}`, hidden source at site 3 | 16 | Branch probability; conditional law | `G_σ`: `P(s_1 = s_2 = 0) = 1/16`; point mass on that branch with `(u_0, v_0) = (r_2, 0)`. `N_1`, `N_0`: uniform in all 256 branches. Re-run after the results review: under `G_σ` all 256 branches are non-uniform (64 determined, 192 biased) |
| c3 | `E_B` on `L = 8`: `R = {−1, 0, 1}`, five hidden sources, multipliers as §2.1 | 16 | Pointwise identities; conditional law | Identities hold. `G_σ`: determined in all 8 branches. `N_1`, `N_0`: uniform |
| c4 | The step on a ring `L = 6`, all 12 slots unknown | 12 | Count of `Q` changes; OR form; inverse | `Q` changes: `G_σ` 0, `N_1` 0, `N_0` 0, `G_SM` 1664, `G_σ` plus center term 2048, each of 4096. OR form and explicit inverse hold |
| c5 | Ring `L = 5`, every cell ready with known `u = 0` | 5 | Pointwise identity | `u_0(1) = v_0(0)` under `N_1`, `N_0` and `G_σ` (PROT-R countercase) |

## 11. Sources

All repository sources are on `main@f88c1842` and are cited at their stated
scope.

| Source | Use | Classification (§A.42 item 8) |
| --- | --- | --- |
| `DESIGN.md`, A1, A2 in this directory | Governing preregistration | This record's own preregistration; on `main` once landed |
| QA Lemma Q (L458), §1.2 (L124); AP1 §4.1 (L464), Lemma 3 (L533), C4 (L677) | Proof audited; baseline; E-AR context | Support on `main` (#1184, #1189; #1183) |
| M2D Lemma Qσ (L593), Theorem NC (L483), M-INACC (L832, L862) | `Q` conservation; countercontrol; question | Support on `main` |
| Main:364 | Cone theorem for C-NS | Manuscript text |
| SM:104–112, :224 | Construction's motivation (D§2.3) | Manuscript text |
| #1198 c.6719123056, c.6719242384, c.6719247117; #1169 c.6718997520, c.6719192859 | Review record; authorization; tiers | Provenance |

No Lean identifier of the vacuous `ReadWriteSourced` family is cited. No
odd-`q` statement is made; any would be conditional on #1193.

## 12. Not claimed

- Any statement about symmetric state-dependent graphs other than `G_σ`, or
  about access posits other than P1 and P2 as stated.
- That P-GK, P-NR or P-1, or any other premise, would restore M-INACC; P-NR's
  sufficiency is not decided.
- A physical source for any element of the classes.
- Contextuality, a quantum operation, or anything about OI–QM equivalence.
- Any odd-`q` result.

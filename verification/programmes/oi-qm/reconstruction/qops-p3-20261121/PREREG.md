# QOPS-P3 preregistration: T-WP, the native which-path interferometer

**Standing. Plan only. Nothing has been run, and no script exists.** The owner's decision
(#1169 c.7066630306) authorizes design and preregistration, and not execution. A run needs
separate owner authorization and an independent review of this file. Changes before a run are
append-only amendments under `amendments/`.

- **Goal link.** As in `PLAN.md`.
- **Definitions.** From `NOTE.md`: H-F1, H-RC, Lemma P6, the slots and CC-Δ / CC-M / CC-OI. The
  native class `𝒩` is OPRES's (#1511 `7669e511`).
- **R-READ is unresolved.** The readout arms are instantiated only from READOUT-ALG's (#1513)
  reviewed verdict, through an amendment recorded before any run that names the readout, its
  instrument form (destructive or Lüders) and its support. If the verdict is that R-READ holds,
  only the FLOW × FLOW arm exists.

## Object (frozen)

- Member U₂ (`q = 2`, `SM:294`), background `c = 0` held frozen (FB).
- Sites: `m = (1,0,0)` (register), `r = (1,1,0)` (ready cell), `s = (1,2,0)` (catalyst).
- Initial configuration: `(p_m, c_m) = (1, 0)`; `p_r = c_r = 0`; `p_s = 0`, `c_s = 1`. Every
  other site is at background.
- Elements:
  - `COPY = shear_r`, with its gate read off the native rule;
  - `F₁ = unit S_m (1/2)`;
  - the readout of `c_m` in the configuration basis.

## Arms

| Arm | Creator `Φ₁` | Detector `Φ₂` | Exists if |
|---|---|---|---|
| FF | `F₁` | `F₁` | always (calibration) |
| FR | `F₁` | `R` | READOUT-ALG gives a readout `R` outside the configuration algebra |
| RF | `R_L` | `F₁` | `R` is non-destructive Lüders |
| RR | `R_L` | `R` | `R` is non-destructive Lüders |

When `Φ₂ = R`, the statistic is `R`'s outcome law in place of `P(c_m = 1)`, with the outcome
labelling fixed in the amendment.

## Computation (exact)

Exact arithmetic over `ℚ(ζ₈)`, extended by any algebraic numbers that `R`'s amendment declares.
For each existing arm `a` and each `h ∈ {id, COPY}`, compute:
- `W_a(h)`;
- `W_a^Δ(h)`, every element replaced by `Δ∘Φ∘Δ`;
- the CC-M check, which is the identity `W(COPY) = W(id)` applied to the arm's data;
- the RES count: the number of pinned non-background cells.

## Decision rule (preregistered as a rule)

Per arm, set `gap = [W_a(id) ≠ W_a^Δ(id)]` and `cs = [W_a(COPY) ≠ W_a(id)]`, both decided exactly.
- **WP-NC** if `gap ∧ cs`. This is a non-classical which-path witness: it excludes CC-Δ and every
  CC-M model.
- **WP-C** if `gap ∧ ¬cs`. Coherence is witnessed, but not decohered by the native copy, so CC-M
  is not excluded.
- **WP-X** if `¬gap ∧ cs`. This is anomalous, and it is reported with its laws.
- **WP-D** if `¬gap ∧ ¬cs`. The arm gives no witness in this protocol.

The verdict text is generated from the table. The FF arm's value, WP-NC with `W(id) = 1`,
`W(COPY) = W^Δ = 1/2`, is derived in `NOTE.md` §3.2. It is a **calibration**, and its outcome is
not evidence. A mismatch voids the run.

## Controls (no verdict over a failed control)

- **K1, the native step at `t = 1`.** Replace `Φ₁ h Φ₂` by `S_m` followed by `h`. Then `W = 1`
  exactly for both settings of `h`, and in CC-Δ as well.
- **K2, the copy gate.** On all 2⁶ configurations of `(m, r, s)`, `shear_r` as read off the rule
  equals `p_r ↦ p_r ⊕ c_m` when `c_s = 1`. Lemma P6.
- **K3, the catalyst countercontrol.** With `c_s = 0` (background), `shear_r` is the identity,
  and `W(COPY) = W(id)` on every arm. Lemma P6.
- **K4, no signalling.** Discarding `r` before the readout leaves `W` unchanged.
- **K5, CC-Δ.** It gives `gap = 0` on every arm, by construction. This is checked, not assumed.
- **K6, the FF calibration.** Its values must match `NOTE.md` §3.2.
- **K7, the readout arms' instrument form.** For each `R`:
  - `R`'s effect is checked to lie outside the diagonal algebra (non-DIO);
  - for `R_L`, its post-state on some configuration is checked to be non-diagonal (non-MIO).

  An `R` that fails either check is reported, and its arms are not run.

## Countercontrols

- **CC-M (must fail on WP-NC arms).** Proposition CC-M in `NOTE.md` makes `cs = 0` for every
  noninvasive memoryful model. On every arm whose result is WP-NC, CC-M is excluded.
- **CC-OI (must succeed; scope).** Construct OI's intervention-dilation realization of each arm's
  `{W(id), W(COPY)}`, with a setting-indexed law (`Main:694`). It must reproduce them. This is
  done on paper and needs no computation. It records that T-WP does not separate the hypotheses
  from invasive classical realizations with supplied data.

## Invariant → checkpoint (§A.41)

| Invariant | Checkpoint |
|---|---|
| the native copy is as Lemma P6 states | K2, K3 |
| the flow composes to the native gate | K1 |
| the arithmetic is exact | `ℚ(ζ₈)` with exact equality tests; no floating point |
| the calibration is reproduced | K6 |
| the readout arms use genuine non-configuration elements | K7 |
| the shadow is computed, not assumed | K5 |

## What an outcome would mean (stated in advance)

- **FF only (R-READ holds).** The calibration only. The unit's productivity then resolves to
  NON-GEM (`PLAN.md`, criterion (ii)), since every branch is fixed by `NOTE.md` §3.2.
- **WP-NC on FR, RF or RR.** A native readout that, together with `F₁` or alone, gives a
  non-classical witness in the senses of CC-Δ and CC-M.
- **WP-NC on RR.** A native element that would discharge both halves of O1 at the
  operational level of this protocol.
- **WP-C or WP-D on the readout arms.** That readout does not act as a non-classical detector in
  this geometry.
- **Every outcome** leaves FLOW₁, CTRL and FB as imports, says nothing about native timing, and
  says nothing about `q = 2^16`.

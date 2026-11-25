# G3's findings against G1 (G3-F10, G3-F11), and where G1 r5 applies them

**Goal link.** Priority item 3, substratum-to-detection correspondence (#1169 c.6894115930).

**Record.** #1169 c.6894115930 (`amaybaum`, 2026-11-15T12:11:24Z), read through the API, GAMMA-1 row:
"**G2 r3 and G3 r2 are accepted** at their stated scopes. No verdict on γ or D-1 follows. G2's fringe
candidate rests on six conditions and is not counted as a miss. G3's findings against G1 (G3-F10,
G3-F11) are reconciled in a G1 r5 before any comparison uses them." Findings: `GAMMA-G3-r2.md` §7
(blob `ef416922`, PR #1294 at `075f7fb3`), from finding 4 and finding 5 of `REVIEW-GAMMA-G3-r1.md`
and the optional note of `REVIEW-GAMMA-G3-r2.md`. Revision: `GAMMA-G1-r5.md` (cited r5 §N). G1 r4
(blob `91a5d656`) is unchanged. r5 applies the two findings and their necessary consequences and
nothing else, adopts no physical premise, and edits no G2 or G3 text. Paper-only: no computation,
Lean, manuscript, Issue change or commit. Source check: Sinha et al. 2010, arXiv 1007.4193v1, Eqs. 3, 4
and 6, re-opened for r5; `p₀` is "the probability P0 of detecting particles when all slits are closed",
"a background signal in the experiment", and enters each `I_AB` and `ε`.

**Where the defect lay.** G3's finding names §5.3, but §5.3 as written in r4 already makes per-herald
normalization the per-incident-particle normalization. The contradiction was between §5.3 and §5.4's
coincidence rule (F10(a)), and between §7.1's `Δ ≡ 0` and §5.4's background rule (F10(b)). r5 keeps
§5.3's model-side text, adds the data-side reading it lacked, and corrects §5.4 and §7.1.

## 1. G3-F10(a): per-herald normalization is per incident particle

| Changed passage | Change | Content changes? |
|---|---|---|
| r5 §5.3, new "Data side" [P] | a count normalized per gate is a count per incident particle; a herald detection corresponds to the herald-executed mass `μ(𝔈_a ∧ e = (a, E))`; a clock trigger, an excitation attempt and not a herald (REVIEW-GAMMA-G3-r2's optional note), corresponds to `μ(𝔈_a)`, one run per trigger; counts per integration time with no gate count and no flux are not per incident particle | yes, additive: a data-side reading is added. The model-side definition is unchanged |
| r5 §5.4, coincidence rule | restricted to counts with no reported or derivable gate count; gated counts with one are T-gate data, normalized per gate | yes: the r4 rule no longer covers gated data |
| r5 §5.4, "Gated targets" (new rule) | a T-gate datum is compared with the §5.3 image for its gate; gate durations are apparatus inputs (E); [A-inf] with no herald process and no visible-herald route a herald-gated datum has no image (not a miss); scale-dependent functionals such as `α` need per-gate counts | yes, new rule for the new type |
| r5 §5.5, raw-direct row | gate counts and per-gate counts added | classification only |
| r5 §7.1, C0's test statistic | `Δ` may be formed from T-gate-sing data per gate (Sinha's heralded runs) | yes: the admissible data for `Δ` widen to gated data |
| r5 §7.2, constructions for X-2 | `α`'s probabilities are per incident particle, on the data side per gate, `α = N_c N_A/(N_1 N_2)`; `α` needs the gate count | no change to the constructions; the data-side normalization is stated |
| r5 §7.4, NC-γ4 | — | none: it already requires division by incident mass only (§5.3) |
| r5 §8 | one row: `κ_norm`'s data side and T-gate depend on a herald process or the visible-herald route | dependency recorded |

## 2. G3-F10(b): Sinha's `I_AB` contains `p₀`

| Changed passage | Change | Content changes? |
|---|---|---|
| r5 §5.4, background rule, new item | `I_AB = p_AB − p_A − p_B + p₀` (Sinha Eq. 6) is not `Δ`; `p_AB − p_A − p_B = I_AB − p₀`; under the background rule `I_AB` is background-corrected and not compared as `Δ`; the raw route compares the raw difference with the model's `Δ` image with `p₀` added to each configuration, in one normalization, for a background that does not depend on which paths are open; `𝒜_10` has no all-closed protocol, so `p₀` comes from the source, and where it is not reported the comparison is not made | yes: a rule for all-closed backgrounds is stated. It applies r4's existing background rule; it adds no rule of a different kind |
| r5 §5.5, inferred row; derived row | `I_AB` listed among background-subtracted values; `Δ` "formed from raw counts with no background subtracted". G3 §4.2's table classes `I_AB` as "derived; background-corrected through `p₀`"; r5 follows G1's own rule, under which background-corrected values are inferred, as G3-F10(b) itself states | classification: `I_AB` inferred, not compared |
| r5 §7.1, C0 | [A-inf, by hand] C0's image through `κ` with a background `b_j` independent of the openings is `Δ_j = −b_j`, additive or as a dark probability, agreeing with G2 r3 §6.1; with `b_j = p₀` this is `I_AB = 0`. Required result and void clause read against `−b_j`; `b_j = 0` only where the source states no background; where the background is not stated, no comparison | yes: the reference value of C0's required result changes from 0 to `−b_j` for targets with background. This is G2 r3's three-condition reading (G2-F7, "one finding" with G3-F10(b)) |
| r5 §7.1, PC-wave | required result "`Δ ≠ −b_j`" (`Δ ≠ 0` at `b_j = 0`); its image departs from C0's wherever the cross term is nonzero (G2 r3 §6.2) | yes, the same reference shift; unchanged at `b_j = 0` |
| r5 §5.7, check 5 and the stability note | [A-inf, by hand] with a background, C0's a1 ratio is `u = (e + b)/(e + 2b)`, `1/2 ≤ u < 1`, `V_u < 1/3 < v_+`: never "present"; "absent" only where `V_u ≤ v_−` or `e` is monotone on each run, otherwise "neither". So check 5's C0 miss holds at `b = 0` and, with background, only under that clause; its stability over `𝒮` is stated at `b = 0` | yes: check 5's scope narrows for C0. The countercontrol against vacuity still holds (the rule can return a miss), and C0 is never classified "present" |
| r5 §7.2, X-3 | `I_3` as written is Sinha's Eq. 3; with a background each member's `I_3` becomes `I_3 + b` (or `b + (1 − b) I_3`); Sinha's measured `ε` (Eq. 4) includes `−p₀` and is background-corrected through it; `I_3` meets raw data only through §5.4's raw route | no change to the conclusion that X-3 separates no member; the form compared with data is stated |
| r5 §7.4, NC-γ6, C0 data side | `Δ` needs, for a target with background, the source's stated background, against which C0's image is `−b_j` | yes, the same reference shift carried into the data-side status; the status itself is unchanged (it waits on G3/G5) |
| r5 §7.4, NC-γ6, law level | — | none: `Δ = (+1/2, −1/2)` against `Δ ≡ 0` is a background-free law statement |

## 3. G3-F11: X-2 fits no §5.4 type

**Disposition: a type is added; X-2 is not excluded.** The typing rule is fixed first, and the type
follows from it (§A.29).

| Changed passage | Change | Content changes? |
|---|---|---|
| r5 §5.4, "Typing rule" [P] | a datum is typed by its conditioning and its normalization as the source states them, before any comparison, never by its value or a comparison outcome; a datum fitting no type is not compared until a type is declared with `I` (NC-γ5) | yes: r4 had types and no rule |
| r5 §5.4, new type T-gate [P] | counts within gates opened by a recorded herald or a clock trigger, gate count reported or derivable, normalized per gate; T-gate-sing (one cell per gate) and T-gate-coinc (joint counts within one gate). Protocols: X-2's beam-splitter program (T-gate-coinc, outside `𝒜_10`); herald-gated forms of a1–a3 and X-3's configurations (T-gate-sing). Data at G3 r2's read status: Grangier thesis Tables II-3, II-4; Jacques Table I; the thesis's gated interference counts (plotted); Sinha's heralded runs (values not in the main text) | yes: a fifth type. It also covers G3-F11's second half, the herald-gated single-detector counts that T-sing does not cover |
| r5 §5.4, no-substitution rule | T-gate data are not compared with T-sing, T-coinc or T-coinc-unsorted images, nor conversely | yes, extended to the new type |
| r5 §5.5, derived row | `α` from per-gate T-gate-coinc counts by the source's formula | classification added |
| r5 §7.3, X-2 row | typed "T-gate-coinc, §5.4"; read statuses left as in r4, with a note that G3 r2's are not applied | type added; read status unchanged |
| r5 §7.4, NC-γ1; NC-γ6 PC-wave data side | the target types and typing rule are among the items declared before evaluation; X-2's data are T-gate-coinc, per gate | declared-item list extended; status unchanged |
| r5 §9, outcome-based choice | the typing rule, T-gate and the data side are fixed on target-neutral grounds, declared as `κ^{r5}` | record only |

**Why not exclusion, and the pressure test** (r5 §10). Typing X-2 makes PC-wave's only separating
observable comparable, a reading favourable to credit, so exclusion was tested as the alternative. An
exclusion needs a reason inside the typing rule. The only candidate, that the data are not normalizable
per incident particle, is false for these data under §5.3 as r4 states it. Excluding them would also
leave without data the X-2 constructions of §7.2, §5.2's multiplicity clause and §7.3's X-2 row, all of
which r4 defines. The type uses conditioning and normalization only. It applies alike to the
classical-source controls (thesis Table II-4; Jacques Table I(a)) and to the single-emitter data, and it
has one consequence unfavourable to K1: with no herald process, a herald-gated datum has no image.

## 4. Consequences across the note

| Passage | Change |
|---|---|
| r5 header | goal link; revision note quoting the record; inputs at `075f7fb3` |
| r5 §1, `κ`; §7.4, NC-γ5 | r5's `κ` changes come after G2 r3's evaluation, so they are one further declaration, `κ^{r5}`, reported beside `κ^{r4}`. Its trigger is the two findings, about the data's conditioning, normalization and background terms, and no outcome. The two declarations agree on every comparison G2 r3 made |
| r5 §10 | the findings recorded as reconciled, with both pressure tests and the cross-propagation |
| r5 §11 | rows for G3 r2, G2 r3, G1 r4, Sinha 2010 and c.6894115930 |
| r5 §12 | "From r5, for G5"; "Not applied in r5" |
| r5 §13 (new) | the G2 r3 statements whose scope changes (below) |

## 5. G2 r3 statements whose scope changes (G2 not edited; r5 §13)

| G2 r3 | Scope under r5 |
|---|---|
| §6.1, "One characterization of G1's clause" | describes r4. r5 §7.1 states the `−b_j` reading with G2's three conditions; G2's derivation is unchanged |
| §6.1, "This note changes no definition" | true of G2; r5 changes the definition |
| G2-F7 ("G1 §7.1 and §5.4 disagree") | narrows to r4; for r5, C0's `−b_j` is G1's own statement |
| §13, question 1 | r5 applies the reading asked about, as the reconciliation the record directs; r5 does not record the question as answered |
| §1.2 `α = 1`; §6.4 `α = 0`, `α = 2` | unchanged as laws; a comparison with X-2 data runs through T-gate-coinc and, for herald gates, a herald-conditioned image, which on K1 needs the visible-herald route; G2 makes none |
| §8, "for a1 there is no compared target in the sources read" | narrows to "no compared value": herald-gated single-detector counts are now typed (T-gate-sing), and the Grangier thesis's gated interference counts and Sinha's heralded combinations are typed candidate targets of two-path form; neither gives a value in the versions read, so G2's outcome is unchanged |
| unchanged | §2.5 and §1.2 "per incident mass"; §6.2; §6.3's cross-model `Δ_j = −p_j`; §8's a6 row and the fringe candidate (Walborn and Kim T-coinc data have no gate count) |

## 6. Not applied

- G3-F1 to G3-F9 are not findings against G1 in the record. G3-F3 (the X-2 reference of r5 §7.4 is
  the `x → 0` idealization; the thesis's gate qualification of `α ≥ 1`) and G3-F5 (AW-σ in `κ_cmp`)
  bear on G1 entries and are left as G3 records them, for G5 or a later G1 revision.
- §7.3's read statuses stay r4's.
- No verdict on γ, on D-1, on any credit set or on any separation is drawn; no comparison is made.

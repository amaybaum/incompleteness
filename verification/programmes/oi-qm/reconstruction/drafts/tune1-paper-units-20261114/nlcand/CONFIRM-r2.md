# CONFIRM r2 of NLCAND: confirmation review after REVIEW-r1 (REVISE)

**Verdict: ACCEPT WITH CHANGES.**

Every finding R1–R11 is dispositioned as `RESPONSE-r1.md` reports, and each disposition is right at its
source. The new derivations in r2 hold on re-derivation. Five wording changes remain (N1–N5, all minor, exact
text below). One optional refinement is offered (O1). No verdict changes.

- **Reviewer.** The non-author reviewer of r1. Did not write `NLCAND-r2.md` or `RESPONSE-r1.md`.
- **Method.** Source reading and hand derivation only. No computation on any OI rule or model, no Lean
  build. Read-only: nothing edited outside this file, nothing committed, pushed or posted.
- **Pins and citation forms.** As in r2. `r2:n` is a line of `NLCAND-r2.md`.
- **Tags.** [C] confirmed by my re-derivation or source reading; [Rv] reviewer's hand derivation, new here,
  unreviewed.

***

## 1. Dispositions R1–R11

| # | r2 does what the response says? | Right at source? | Remaining |
|---|---|---|---|
| R1 | Yes: the H-Bell sentence is gone; M3 and Verdict (b) say nothing here tests H-Bell; B7 is its own node; §6 "Order" rewritten | Yes. Sub:131–133; Main:414 | N1 (one sentence in §6) |
| R2 | Yes: conventions H and S in the header; B4 (0)–(iii) and B5 under each; table; F4, F5, F11 | Yes. Main:369–372; 3A:501; LD:198–200, :274; OA2:803–805. The three modifications are correct: the dependence at `g = 0` enters at cell `a+1`; under H the ready cell is not needed; under S the one-cell table returns with a declared record slot (checked below) | O1 (optional) |
| R3 | Yes: J1 conditional; the exclusion sentence withdrawn; J2 added | Yes. LP:245; SS:59–61 | — |
| R4 | Yes: A3 rewritten; P17, F1, §0.4, §0.7, Verdict (a), §6 | Yes; see §4 below | N3 |
| R5 | Yes: no check proposed; owner condition quoted; controls replaced | Yes. The quotation at r2:466–468 matches LP:19–21 word for word; OA2:803–805, :814; OA3:89–92 | — |
| R6 | Yes, with the F9 wording declined | Yes; the decline is correct (§2 below) | — |
| R7 | Yes: label "`K_nz` only; breaks on the vacuum and uniform readings"; graph distinction in B1; wider travelling family | Yes. `h(i−1+t) + h(i+1+t) − h(i+t−1) = h(i+t+1)` and `h(i−1−t) + h(i+1−t) − h(i−t+1) = h(i−(t+1))` both hold when `h` has no zero value [C] | — |
| R8 | Yes: preamble; P19–P21 | Yes. P21 re-derived [C]: from `x(−1) = 0`, `x(0) = y δ_s`, `x(1) = y` at `s−2, s−1, s+1` and `0` at `s`; with `E = u·u + v·v − u·Av` (SM:296), `E = y²` then `y² + 3y² − 2y² = 2y²`; the linear rule gives `y²` twice. P19 is correctly left "not assessed" | — |
| R9 | Yes: sensitivity table; observer row; one-cell row | Yes. SM:112; OA3:89–92 | — |
| R10 | Yes | Yes, with one imprecision on the herald cost | N2 |
| R11 | Yes, all five | Yes | — |

***

## 2. The two wordings that differ from the review

**F9 (declined by the writer). The writer is right.** The review proposed "No `d = 3` rule with a
state-dependent graph is written". For the rounded rule, `h(s) = ⌊(s+1)/3⌋` on `s ∈ {0, …, 6}` is
`0, 0, 1, 1, 1, 2, 2`; at `q = 2` the output changes under a unit change of one neighbour only across
`1 ↔ 2` and `4 ↔ 5` (S4:31–35). So in the sense of Main:362 its dependences are present at some states and
absent at others, and the review's sentence would have been false. r2's "no `d = 3` version of the ring rule
is written" (F9, §0.3) and "no `d = 3`, six-component switched-neighbour member" (M1) are accurate and make
no claim about the rounded rule's graph. No change.

**The general chain bound (not adopted by the writer). Acceptable, and it is used nowhere.** r2 was
searched for it: B4 (ii) uses only the exact one-hop bound; B7's limit (1) cites that one-hop value; B4 (iii)
stays "undecided". No statement of r2 rests on the general bound, so nothing needs to be marked unsupported.
For the record, the step the writer could not re-derive is derivable [Rv]: along a chain the gate cells have
`p − t` strictly decreasing, each gate value is `u_{p−t}(0)` plus a function of other slots (left-neighbour
chain, coefficient one), and a later gate's pad lies outside every earlier gate's dependence range, so the
gate values are jointly uniform. One caveat found on re-derivation: a gate whose pad is a generator cell is
not uniform given the settings and must be dropped from the count. The count of chains was never done. The
bound remains a reviewer's sketch outside r2, which is the right status.

***

## 3. New text in r2, re-derived

| Item | Check | Result |
|---|---|---|
| B4 (0), `g = 0`, `r_O`, label `0` | `x_{a+1}(1) = u_a(0) + sel(u_{a+2}(0), u_{a+3}(0)) − v_{a+1}(0)`; `v_{a+1}(0) = 0` by `r_O`; `u_a(0)` is the previous slot of cell `a` at tick 1; label `u_{a+2}(0) = 0` gives `sel = y` | [C] total variation `1` at label `0` under S and under H; `1/q` with the label left to μ-G and known to `A`. Cell `a+1` is at nearest-neighbour distance two from the generator; the region `{a, a+1}` meets Main's (iii) in the nearest-neighbour graph and fails it in `G_φ`. Under H the ready cell is not needed |
| B4 (ii), H, `|S_CHSH| ≤ 2 + 2/q` | `A`'s one-tick history depends on `y` only through `x_{a+2}(1)`, and only when `w = 0`; `B`'s cells `a+4..a+6` read cells `≥ a+3` at tick 1, so `B`'s history does not depend on any cell of `A`; `w` is neither generator | [C] `N = {w = 0}`, `P(N) = 1/q`, independent of the settings; `2(1 − 1/q) + 4/q = 2 + 2/q`; `< 2√2` for `q ≥ 3`, `= 3` at `q = 2`. Holds for every choice of `A`'s generator cell |
| B4 (ii), S | `v_{a+2}(0)` enters `x_{a+2}(1)` only, is absent from both tick-1 states and is uniform | [C] `x_{a+2}(1)` is uniform and independent of everything else either wing holds, so it can be replaced by a private pad: total variation `0`, table Bell-local. With `r_O`, `x_{a+1}(1)` reads `w`; `B`'s `x_{a+4}(1)` also reads `w` but is masked by `v_{a+4}(0)`, and a shared `w` is a common cause in any case |
| B5, S | `B`'s state at tick 1 is `(x_i(1), u_i(0))`; `x_i(1) = α + sel(y, x) − v_i(0)` | [C] product table. With `v_i(0)` declared, `β = x_i(1) + v_i(0)` is available and the table returns; `A`'s `x_{i−1}(1)` stays masked by `v_{i−1}(0)`, so no-signalling is kept |
| B4 (iii), S "at most the value under H" | the tick-`T` state is a function of the complete history | [C] |
| B7 | case `c_L ≥ 2`: `D > c_L T ≥ 2T`, B2; case `c_L < 2`: B4 (0) with region `{a, a+1}`, distance `2 > c_L` | [C] The conclusion holds for the member as specified (it includes `r_O`). The four limits are stated correctly; limit (2) is accurate |
| C1 herald cost | OA1:156–160: `P(Σ_t = σ | E) ≤ μ(Σ_t = σ)/P(E)`; a herald that fixes `M` slots has `P(E) ≤ q^{−M}` | [C] as a bound; r2 states it as an equality (N2) |

***

## 4. The control section (A3)

Confirmed. A3 states each Lean result at its actual scope:
- the rule is not an input (`obsTheory_rule_independent`, `SubstratumInterfaceAudit.lean`:780–782, `rfl`;
  `sourcing_rule_independent`, `FrozenSourcing.lean`:295–298, `Iff.rfl`);
- the negatives `frozen_sourcing_verdict` and `substratumGen_not_control` are on `Fin 2`, with no substratum
  and no rule;
- the every-`ε` ceiling (`DenseUnitaryControl`, `permTheory_dense_ceiling`) sits at the same interface;
- `obs_not_layerFlowExecutable` and `obsTheory_nonnegBounded` are the statements quantified over every
  substratum.

It draws the line between observer interfaces (operators on the configuration set against record laws of a
region under a law), says the line is not between rules and not between exact and approximate, and scores
nothing against the candidate (A3; P17; Verdict (a); §0.4; §0.7; §6 "Order"; F1). Two precision edits: N3.

***

## 5. Verdict strengths

| Statement in r2 | Supported by | Exact? |
|---|---|---|
| "(b) Member: not supplied at lattice scale" | B7, with B2 and B4 (0) | Yes, for the member with its declared `r_O` and a label `0` in its menu |
| "(b) Rule: not established" | B5 (dependence without signalling for one-cell records under H); B4 (iii) undecided | Yes |
| "wings many cells apart remain undecided" | B4 (iii) | Yes for the member. For S with no declared cell it is decidable (O1); the member has declared cells, so its own case stays undecided |
| "(c) no unconditional supply under μ-G; heralded supply at `q^{−M}`" | C1; OA1 D3 | Yes after N2 |
| "(c) undecided under the other two laws" | C4, C5: no result for this rule | Yes |
| Joint: "not shown to meet the three requirements … a derived defect for (b) at lattice scale"; "not shown that no completion of the ring rule can meet them" | §6 | Yes after N1 |

Each verdict is stated for the one member of §1.4.

***

## 6. The closing section (§9)

No generalization beyond the member was found. The "Shows" list is scoped to the member; its first two
bullets are pointwise properties of the rule and are stated as such. The "Does not show" list covers the
rounded rule, longer edges, a `d = 3` version, H-Bell, T1 and the class, and correctly says that the three
rule-free statements hold for every rule by their own proofs and are not findings of the analysis. Two edits:
N4 (a direction is dropped in one bullet) and N5 (an unexamined item the response says is in §9 and is not).

***

## 7. Remaining changes (all minor), with exact replacement text

**N1. r2:450–453 (§6 "Order").** "the decided instances inside that window signal" is not true under S: the
`g = 1` instance is decided there and does not signal (B4 (ii), S), and B4 (0) lies in the window only for
the readout region `{a, a+1}`. Replace the bullet by:

> - **Order.** The kernel no-go is rule-blind and is not scored. Of the requirements that depend on the rule,
>   (a) is undecided at TUNE-1's interface, and (b) is the first with a derived defect for the member: B2
>   confines any effect to `T < D ≤ 2T` toward decreasing index, and inside that window the member's record at
>   cell `a+1` signals at `g = 0` under both conventions (B4 (0), readout region `{a, a+1}`) and its block
>   signals at `g = 1` under H (B4 (ii)). Under S the `g = 1` instance is decided and does not signal.

**N2. Herald cost: a bound, not an equality.** OA1:156–160 gives `P(E) ≤ q^{−M}`, "with equality for a visible
herald on visible cells".
- r2:67–68 (§0.6): replace "a heralded supply of `M` slots costs `q^{−M}`" by "a herald that fixes `M` slots
  is accepted with probability at most `q^{−M}`".
- r2:413–414 (C1): replace "A heralded supply remains: fixing `M` slots costs probability `q^{−M}`" by "A
  heralded supply remains: a herald that fixes `M` slots is accepted with probability at most `q^{−M}`, with
  equality when it reads those slots directly".
- r2:438–439 (Verdict (c)): replace "a heralded supply costs `q^{−M}` for `M` slots" by "a herald that fixes
  `M` slots is accepted with probability at most `q^{−M}`".

**N3. A3, two precision edits.**
- r2:215–217: replace "hold by `rfl`, the latter with the docstring" by "hold by `rfl` and `Iff.rfl`
  respectively, the latter with the docstring".
- r2:231–232: replace "the every-`ε` ceiling holds at the kernel's interface." by "the every-`ε` ceiling,
  stated on the two-valued carrier, holds at the kernel's interface."

**N4. r2:522 (§9, second "Shows" bullet).** Replace by:

> - Its dependence on remote cells is confined to two cells per tick toward decreasing index and one toward
>   increasing (B1, B2).

**N5. §9, "Does not show".** `RESPONSE-r1.md` (section C, item C4) places the unexamined long-wavelength
behaviour in §9; it is not there. Add after r2:530:

> - Whether any isotropic long-wavelength propagation survives for typical configurations, which have zeros
>   and so leave `K_nz`: not examined (P7, P8).

***

## 8. Optional refinement, for the author to re-derive before any use

**O1. Under S with no declared cell, the in-window case is decidable [Rv].** r2's last table row (r2:342) and
B4 (iii) (r2:327–329) list "H or S, block, none, `g ≥ 5`" as undecided. For S with no declared cell:

1. *Forward pad.* For `s ≥ 1`, `x_j(t_0 + s) = u_{j−s}(t_0) + G`, with `G` free of that slot (r2's own
   argument in B5: rightward speed one, left-neighbour coefficient one).
2. *Reversal.* `x̃(τ) = x(k − τ)` obeys the same recurrence (§1.2). Applying 1 from the reversed state at
   `τ = 1`, whose current slice is `x(k−1)`: `u_b(0) = x_{b−k+1}(k−1) + G_b`, where `G_b` is a function of
   the other slots of the state at tick `k`, within cells `[b−k+1, b+2(k−1)]`. Likewise
   `u_{g_A}(0) = x_{g_A−k+1}(k−1) + G_A`, and `G_b` does not contain `A`'s pad because `g_A − k + 1 < b − k + 1`.
3. *Uniformity.* Under μ-G the state at tick `k` is uniform. For fixed values of all slots other than the two
   pads, `(pad_A, pad_b) ↦ (x, y)` is a bijection (triangular). So `(x, y)` is independent of every set of
   slots at tick `k` that contains neither pad.
4. *Where the pads are.* `pad_b` is the previous slot of cell `b − k + 1`: in `A` only for
   `k ∈ {g+2, g+3, g+4}`, in `B` only for `k = 1`. `pad_A` is at cell `g_A − k + 1`: outside `A` for `k ≥ 4`,
   never in `B`.
5. *Conclusion.* For `4 ≤ k ≤ g + 1` the joint law of the two blocks' tick-`k` states does not depend on
   `(x, y)`. Every in-window instance (`g ≥ 5`, `3 + ⌊g/2⌋ ≤ T ≤ g`) lies in that range: total variation `0`,
   and a table whose hidden variable is the pair of states, so Bell-local.

This does not cover the member, whose `r_O` fixes slots (the tick-`k` state is then not uniform), nor
convention H. If the author re-derives it, the row splits into "S, none: `0`; table Bell-local" and "H, or S
with `r_O`: undecided", and limit (2) of B7 extends from one tick to the whole window. If not, r2's
"undecided" is not an overclaim and may stand.

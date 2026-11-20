# MEAS-Q: delivery and preparation on the published rounded rule

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form),
with small exact computations. It adopts no premise and edits no manuscript, Lean module or
registry.

- **Review.** An independent non-author review at `12a251b0` returned REVISE
  ([#1455 c.7037170075](https://github.com/amaybaum/incompleteness/pull/1455#issuecomment-7037170075)).
  It found the computations reproduced and MQ1–MQ2 correct, and required changes of wording and
  labels (B1–B6, N1–N10).
- **Owner guidance.** Paraphrase relayed by the coordinating session (owner `amaybaum`,
  2026-11-20; provenance, not a GitHub comment). Keep the original decision rule, and do not
  strengthen DT_A retroactively. Report all 297/297/229 as formal successes. Distinguish formal from
  physical success. Bound the negatives. The stronger test is a separate future protocol.
- **This revision.** It answers B1–B6 and N1–N10 in appended commits. A delta re-review at
  `6ca6e3f7` returned ACCEPT-WITH-NITS, and its nits 1–5 are answered in later appended commits.
  `PREREG.md`, A01 and A02 are unchanged.

- **Authorization.** Owner `amaybaum`. Scope:
  [#1169 c.7032429839](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7032429839),
  row MEAS-Q. Condition:
  [#1169 c.7033018172](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033018172)
  ("no unaccounted controller or prepared resource is imported"; "None of these authorizes adopting
  a new physical assumption"). Start:
  [#1169 c.7033513830](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033513830),
  given UNIV-2's accepted re-review
  ([#1444 c.7033699598](https://github.com/amaybaum/incompleteness/pull/1444#issuecomment-7033699598)).
  Each is quoted in `PREREG.md`.
- **Goal link (§A.47), as preregistered.** Serves #866 for #1169. On the published rule Q it decides
  two questions. (Q1) Can content from outside a ready cell's component reach it and leave it ready,
  with a held record? (Q2) Does an untuned law yield delivering configurations with positive
  probability, and at what accounted cost? Unchanged: A1 OPEN/UNADOPTED; physical measurement
  sourcing NOT PASSED.
- **Accountable Issues.** #866, #1169. Guiding draft PR: #1455.
- **Preregistration chain** (branch `research/meas-q-20261120`, from `D` = `main` at `bce3ab0b`).

  | Commit | Content |
  |---|---|
  | `b8bffca2` | `PREREG.md` |
  | `191ae9ab` | A01 (before any run on Q; the only earlier computation was control PC1 on U₂) |
  | `7a899890`, `f5879d6a` | the checks script |
  | `1b4f66fe` | the preregistered outputs (`results.json`), the post hoc diagnostic X1, and A02 (before S-B-long) |
  | `265c6828`, `1efdf496` | the S-B-long script |
  | `12a251b0` | RESULT (reviewed version), S-B-long outputs, post hoc X2 |
  | later commits | the post-review revision (§8): verdict template, K2b, cost of one A02 configuration, and the rerun |

  The claim that each preregistration preceded the runs it governs rests on the order of these
  commits (§A.42 item 8). The PR must therefore land by a merge commit that keeps them in `main`'s
  history.
- **Predecessors.** Records on `main`, under `verification/programmes/oi-qm/reconstruction/`:
  DELIVER-1 `deliver-1-20261119/` (DL1); NATPREP-1 `natprep-1-20261119/` (NP1); PREP-REGRESS-1
  `prep-regress-1-20261119/` (PR1); UNIV-1 `univ-1-20261119/` (U1); UNIV-2 `univ-2-20261120/` (U2R),
  on `main` since `27187dc3`. U2R is provenance only. Its verdict is used to decide what is not
  searched again, and its A1 (component independence) is re-checked here (K4). Nothing here is
  proved from U2R.
- **Not overlapped.** G3-W1 (conserved quantities of the d = 3 rule) and POSIT-MIN (#1451).

| Label | Meaning |
|---|---|
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/measq_checks.py` (integer arithmetic) |
| [S] | bounded search in the same file (`--search`); evidence about the searched set only |
| [PH] | post hoc diagnostic, not preregistered (X1 `checks/posthoc_sb.py`, X2 `checks/posthoc_x2.py`); decides no verdict |
| [A02] | run defined in amendment A02, written after X1 and before the run itself (`checks/sb_long.py`) |
| [R] | research record on `main`, not independently established |

***

## 0. Summary

1. **Verdict (generated from `results.json`, controls green, 20/20 checks).** The script prints:
   "gem (i) not met in the preregistered searches, which did not evaluate DT_A outside the
   carrier's class (S-B horizon 28); PREREG §6 item 1 in its formal (i-cond) form: DT_A on Q
   (re-run in Q) is met by 297 of 398 S-B-long configurations (A02; DT_s 297, DT_A^h 229) and by 7
   of 10 X1 examples; the audit clause was checked on 5 (ok; it holds by construction for runs
   built from the ledger) and the cost clause on 1 (46.3 bits); gem (ii) checks hold (K1, K2, K2b
   green; use outside the carrier's class after a breach in at least 3003 S-B configurations); the
   obstruction itself rests on the written proof of Lemma MQ1 / Theorem MQ2 in RESULT."
   - *Gem (i): formal (i-cond) successes under the preregistered criterion.* They are physically
     not deliveries to a re-armed apparatus (X2, §5). Each is conditional on its enumerated pattern
     and its priced background.
   - *Gem (ii): the preregistered conditions hold.* The content is BORDERLINE: it elaborates DL1
     Theorem 2.2 and U1 Lemma 2.2 (§7).
2. **Node 1: confinement on Q (§2) [W, EC].**
   - On Q, the property that replaces DL1's (P) is Lemma MQ1, and it is sharp: a background site
     with one non-background neighbour stays at `c` iff that neighbour's representative lies in
     `[c−1, c+1]`.
   - Theorem MQ2: support closure and class isolation hold on Q over any window in which the inner
     boundary layer of the closed support stays in `[c−1, c+1]`. The proof places no condition on
     interior or previous-slice values; K2b exercises this in one-tick windows.
   - Corollaries:
     - a carrier is never used outside its initial class without a *breach*, a boundary value
       leaving `[c−1, c+1]` (MQ3);
     - finite confined classes are periodic and erase their records (MQ4);
     - NP1's dilution lemma holds on Q (MQ5).
   - MQ1–MQ3 hold at every background `c`, with `[c−1, c+1]` read as representatives. Only the
     confinement of the ternary sector (all values within ±1 of `c`) needs `1 ≤ c ≤ q−2`. The
     vacuum's explosiveness is the case `c = 0`, where the residue of `−1` lies outside
     `[c−1, c+1]`.
3. **Q1 on Q (§3).**
   - *Inside a class [S, EC]:* the box enumeration S-A finds DT_s deliveries:
     - 1 112 on the `2×2` box, minimum environment weight 1 (on U₂ the minimum is 2, NP1
       Proposition N2.2);
     - 1 610 on line 5;
     - none on lines 3 and 4.
     None meets DT_A: every record is erased within the class period (MQ4).
   - *Along an infinite class [EC]:* a W2 signal approaches and passes a ready line cell (S-C). It
     meets DT_s with the moved signal as the log, and fails DT_A (CC4).
   - *Outside the carrier's class, into the background:* impossible without a breach (MQ3). With a
     breach, contact outside the box occurred in all 3 977 sampled breaching configurations within
     28 ticks. DT_s outside the carrier's class was met in 3 003 of them (S-B). The region reached
     is unprepared background, not a prepared apparatus.
   - *DT_A outside the carrier's class (post hoc and A02):* see item 5.
   - *Latch beside a straight W2 line (S-D) [S]:* there is one distinct case up to exact symmetry,
     4 513 gadgets. Of these:
     - 111 are quiescent;
     - 78 of the quiescent gadgets radiate;
     - 33 restore the line but hold no persistent record;
     - none passes.

     The negative is bounded to pair-flip W2 signals, one arrival geometry up to symmetry, and
     gadgets of at most 2 sites with values `±1, ±2`.
4. **Q2 on Q (§4).**
   - *Positive probability [W, EC].* The weight-1 `2×2` delivery has positive probability under
     every `ν_{c,ρ,κ}` with `κ` of full support. Its selection cost is about 13 bits for a `κ`
     concentrated on the ternary pairs (best `ρ = 1/364`), and 42–44 bits for `κ` uniform on all
     pairs. The delivery needs `N + 1 = 2` bits of budget (DL1 (2.4)).
   - *In law [W].* Use in law is diluted (MQ5).
   - *Noise [S].* For full-support `κ`, the noise contains breaching symbols, and in S-E these
     destroyed the background within 20 ticks even at `ρ = 10⁻³`. Ternary noise at `ρ = 10⁻³` did
     not breach in 40 ticks; at `5·10⁻²` most sites breached.
5. **Pressure test of the favourable branch (§5).**
   - *What X1 found [PH].* DT_A, as defined in PREREG §2, is met by breach configurations: 7 of
     the 10 stored S-B examples. The mechanism is as follows.
     - The carrier decides whether, or how, a breach disturbance grows. In one example one branch
       stays on 2–3 sites while the other covers about 20 000 sites by `t = 87`.
     - The "record" is the difference between the disturbance and its absence, over the region
       `A` of about 1 000 sites.
     - `H` is at `(c, c)` at the instant `τ₂` but not at every later tick.
   - *S-B-long [A02].* It measures DT_s, DT_A and a held-readiness variant DT_A^h on a subsample
     of 398, fixed in A02. DT_s holds in 297, DT_A in 297, and DT_A^h in 229.
   - *X2 [PH].* In all 40 DT_A^h cases examined, the "record" is the breach front spreading
     through `A`. At `τ₂` a median of 4% of `A` differs between the branches; at `τ₂ + 60`, 73%.
     No single site holds the record over the 60 ticks. `H` is passed early and is quiet over the
     hold window, then is reached again by the front: it is not ready at every tick through
     `t = 87` in any case.
   - *Consequence.* The preregistered criterion for gem (i), PREREG §6 item 1, stands. In its
     formal (i-cond) form:
     - DT_A on Q (re-run in Q) is met by 297 of 398 S-B-long configurations (229 of them with
       DT_A^h) and by 7 of the 10 X1 examples;
     - the audit clause was checked on 5; it holds by construction for runs built from the
       ledger;
     - the cost clause was checked on 1 (§5).
     - A02 preceded the S-B-long run but followed X1, which had already shown DT_A in 7 of 10
       examples. A02's clause not to count them is therefore a post hoc decision, and it is not
       applied.
     - X2 shows that these successes are physically not deliveries to a re-armed apparatus. Each is
       a one-shot amplified record: the carrier triggers a breach front, which consumes the priced
       background. Nothing localized is recorded, and readiness is consumed, not restored.
   - *AW markers.* AW-MQ-1 (moving carriers) records a gap in DT. AW-MQ-2 states that PREREG's
     DT_A (`N = 1`) does not separate delivery to an apparatus from a carrier-triggered breach front
     that consumes the prepared background, and proposes a stronger task for a separate protocol.
6. **Productivity.**
   - (i) Not met in the preregistered searches. Met formally, in (i-cond) form, by the A02 and X1
     configurations under the unchanged criterion; physically not met (§7).
   - (ii) The preregistered conditions hold at the scope of MQ1–MQ3 [W, EC]; the content is
     BORDERLINE.
   - AW-MQ-1 and AW-MQ-2 are NEW assumption-watch markers on DL1's task. AW-MQ-2's stronger task is
     proposed for a separate protocol, fixed before any test (Issue #866).

***

## 1. Object, tasks, ledger (as preregistered)

- **Q** is the rounded rule of SM §4.2 at `q = 2^16` on `ℤ³` (U1 §1). Every uniform background `c` is
  a fixed point.
- **RZ** is Q written on `y = x − c` while `0 ≤ c + y < q` (U1 Lemma 2.1, one direction; checked
  at `c ∈ {1, 2^15, q−2}` in K3). Every reported candidate is re-run in Q itself.
- **Tasks.** DT_s is NP1 §1.4, unchanged. DT_A adds two clauses to DT_s:
  - `H` and the log `L` lie in a declared bounded apparatus region `A`, and the carrier starts
    outside `A`;
  - the same `L` determines the carrier at every tick of `[τ₂, τ₂ + 60]`. Per A01 item 1, `L` is
    the largest admissible block.
- **Ledger.** The ledger (PREREG §3) prices every input:
  - the background, at 32 bits per site;
  - designed patterns, at 16 bits per pinned slot, or by their probability and selection cost
    under `ν_{c,ρ,κ}`;
  - carriers, which are fair bits;
  - any controller, which must be declared.

  `ledger_audit` rebuilds the initial state from the ledger and recomputes every tick with Q. Any
  difference is reported as an unaccounted prepared resource or an unaccounted controller (CC2,
  CC3). For runs whose initial state is built by `Ledger.build` and iterated by Q, the audit holds
  by construction. Its force is shown by CC2 and CC3, and it guards the oracle and the re-runs. The
  owner's accounting condition is met by the cost tables (§4.1, §5): every prepared input is
  priced there.

***

## 2. Node 1: confinement on Q

DL1 Theorem 2.2 rests on (P): a background site with at most one perturbed neighbour stays at the
background. NP1 §3.4 shows (P) fails on Q: one neighbour carrying `c + 2` perturbs the site. The
question here is what replaces (P) on Q. Predecessor: U1 notes that `G(s) = 0` iff `|s| ≤ 1`, and
its Lemma 2.2 (line sector) applies this to axis lines in RZ. MQ1 states the same fact on Q's
representatives, for any closed set and any background `c`, together with its converse.

Notation. `c ∈ {0,…,q−1}` is a uniform background. For `D ⊂ ℤ³`, `cl₂(D)` and *closed* are as in
DL1 §2.2. The *inner boundary layer* `∂D` is the set of sites of `D` with a neighbour outside `D`.
Values are representatives in `{0,…,q−1}`; `[c−1, c+1]` means the representatives in that integer
interval (for `c = 0` it is `{0, 1}`; the residue of `−1` is `q − 1` and is outside it).

**Lemma MQ1 (one-step confinement; sharp) [W, EC K1].** Let `D` be closed and suppose
`x_{t−1}(i) = x_t(i) = c` for every `i ∉ D`. Then `x_{t+1}(i) = c` for every `i ∉ D` if
`x_t(j) ∈ [c−1, c+1]` for every `j ∈ ∂D`. Conversely, a background site `i` with
`x_{t−1}(i) = c` whose only non-background neighbour has representative `r` satisfies
`x_{t+1}(i) = c` if and only if `r ∈ [c−1, c+1]`.

*Proof.* A site `i ∉ D` has at most one neighbour in `D` (closed), and that neighbour lies in `∂D`.
Let `r` be its representative, or `r = c` if there is none. The neighbour sum is `5c + r`, so
`x_{t+1}(i) = ⌊(5c + r + 1)/3⌋ − c mod q`. This equals `c` iff `⌊(5c + r + 1)/3⌋ ≡ 2c (mod q)`.
Because `0 ≤ r ≤ q − 1`, the floor lies in `[0, 2q)`, so it is `≡ 2c` only if it equals `2c`,
`2c + q` (possible only when `2c < q`) or `2c − q` (only when `2c ≥ q`). It equals `2c` iff
`6c ≤ 5c + r + 1 < 6c + 3`, i.e. `c − 1 ≤ r ≤ c + 1`. It equals `2c + q` only if
`r ≥ c + 3q − 1 > q − 1`, and `2c − q` only if `r < c − 3q + 2 < 0`; both are impossible. ∎
K1 checks the converse exhaustively, over all `q` values of `r`, at
`c ∈ {0, 1, 2^15, q−2, q−1}`.

The inverse of Q has the same form (`x_{t−1} = ⌊(Σ x_t + 1)/3⌋ − x_{t+1}`), so the same statement
holds backward in time.

**Theorem MQ2 (windowed confinement and class isolation) [W, EC K2, K2b].** Let `D` be closed, let
`x_{t₀−1}` and `x_{t₀}` equal `c` off `D`, and suppose `x_t(j) ∈ [c−1, c+1]` for every `j ∈ ∂D`
and every `t ∈ [t₀, t₁]`. Then:
(a) `x_t = c` off `D` for every `t ∈ [t₀ − 1, t₁ + 1]`;
(b) if `D = D₁ ∪ D₂` with `D₁`, `D₂` closed and at ℓ1-distance at least 3, then for
`t ∈ [t₀, t₁ + 1]` the content of `D₁` is the orbit of `D₁` run alone (`c` outside `D₁`), and the
same holds for `D₂`.
No hypothesis is placed on the values at sites of `D ∖ ∂D`, or on the previous slice: they range
over the full alphabet.

*Proof.* (a) Induction on `t` with Lemma MQ1.

(b) A neighbour of a site of `D₁` lies in `D₁` or at distance 1 from `D₁`; in the second case it
is at distance at least 2 from `D₂`, so outside `D`. Hence `∂D₁ ⊂ ∂D`, and on `[t₀ − 1, t₁ + 1]`
every neighbour of `D₁` outside `D₁` holds `c` by (a). Now compare with the run of `D₁` alone
(`D₁` closed, `c` outside it at `t₀ − 1` and `t₀`). By induction on `t ∈ [t₀, t₁]`:
- if the two runs agree on `D₁` up to `t`, then `∂D₁` carries the same values in both, which lie
  in `[c−1, c+1]` because `∂D₁ ⊂ ∂D`;
- so MQ1 keeps the alone run at `c` outside `D₁` at `t + 1`;
- both runs then update `D₁` from the same values, and agree on `D₁` at `t + 1`. ∎
(`D₁ ∪ D₂` is closed: a site outside it with two neighbours in it has both in one `Dₖ`, which is
closed, or one in each, which puts `D₁` and `D₂` within distance 2.)

K2 tests (a) and (b) on 300 random two-box configurations in Q, at `c ∈ {1, 2, 2^15, q−3, q−2}`,
over every tick at which the hypothesis has held so far (802 instance-ticks, 623 of them at
`t ≥ 3`). In every instance-tick K2 tests, all values of `D` lie in `[c−1, c+1]`: its full-alphabet
configurations fail the hypothesis at `t = 0` and contribute none.

K2b (post-review) holds the inner boundary layer in `[c−1, c+1]` and draws the interior current
slice and the whole previous slice of `D` over the full alphabet. It covers 700 configurations at
`c ∈ {0, 1, 2, 2^15, q−3, q−2, q−1}`, the wrap backgrounds included. All 700 instance-ticks carry
out-of-range interior or previous values, and (a) and (b) hold at each. Each window is one tick
long: the interior kicks the boundary out of range at once. "Unrestricted interior" over longer
windows therefore rests on the proof alone.

**Corollary MQ3 (no use outside the carrier's class without a breach) [W].** Let the two carrier branches
differ only on slots of a set `K`. Let `D` be `cl₂` of the union of the two branches' initial
perturbation supports, `D₁` the union of the classes of `Comp` (NP1 §3) that meet `K`, and
`D₂ = D ∖ D₁`. If in both branches `x_t(j) ∈ [c−1, c+1]` for every `j ∈ ∂D` and every
`t ∈ [0, T]`, then `W_t(H)` is the same in both branches for every `H ∉ D₁` and every
`t ≤ T + 1`. Hence a use of a carrier at a site outside its initial class requires a *breach*:
in some branch, some site of `∂D` takes a value outside `[c−1, c+1]` before the use.
*Proof.* `D₂` runs alone (MQ2(b)) from initial content that is the same in both branches; sites
outside `D` stay at `c` (MQ2(a)). ∎

**Corollary MQ4 (finite classes are periodic; records are erased) [W].** If `D₁` is finite and the
hypothesis of MQ3 holds for all `t ≥ 0`, the content of `D₁` evolves by the isolated map of
`D₁`, a bijection of `{0,…,q−1}^{2|D₁|}`, and so returns to its initial content at a finite period
`P`. At `t = P` any block disjoint from the carrier's slots carries no information about the
carrier, so every record held in `D₁` is erased by `t = P` (DL1 2.3(c), on Q).

**Corollary MQ5 (dilution on Q; NP1 Lemma N2.3) [W, EC D1].** Let `K` single-site carriers sit at
sites `j_k`, each adding `+1` to declared slots whose environment value is `c`, and let the
environment law `ν` be independent of the carriers. For a block `L` not containing `j_k` and
`t ≥ 0`, let `G_k(t)` be the event that every environment slot in `B(L, t)` equals `c`, except
possibly the remaining slot of `j_k`, which lies in `[c−1, c+1]`. Then every estimator of `c_k`
from `W_t(L)` errs with probability at least `2^{−K} ν(G_k(t))`. Under `ν_{c,ρ,κ}`,
`ν(G_k(t)) ≥ (1 − ρ)^{|B(L,t)|}`.
*Proof.* `W_t(L)` depends only on the initial data in `B(L, t)`. On `G_k(t)`, with the other
carriers at 0, that data is supported on `{j_k}` with both slots in `[c−1, c+1]`. In RZ the
singleton runs `(a, b) ↦ (b, −a)` (its neighbour sum is 0), so its values stay in `[c−1, c+1]`,
and `{j_k}` is closed; MQ2(a) keeps `L` at `c` in both values of `c_k`. That event has probability
`2^{−(K−1)} ν(G_k(t))`, and on it any estimator errs with probability `1/2`. ∎ D1 checks the
singleton step in Q at `c ∈ {1, 2^15, q−2}` for all nine pairs over 64 ticks.

**Scope and sharpness.**
- The hypothesis of MQ2 concerns the inner boundary layer only. In the boxes of S-A every site lies
  in the boundary layer, so the hypothesis there is "all values in `[c−1, c+1]`".
- Holding for all `t` is decidable for a finite class (the isolated orbit is periodic).
- CC5: a closed singleton holding `c + 2` (at `c = 2^15`), or the residue `q − 1` of `−1` on the
  vacuum `c = 0`, perturbs all six neighbours in one tick. The vacuum's explosiveness (U1 C1–C2) is
  the case `c = 0`, where `−1` is not in `[c−1, c+1]`.
- Lemma MQ1 holds for every `c`. The family of uniform backgrounds on which the ternary sector is
  confined is therefore `c ∈ {1,…,q−2}`, an open condition, not a single tuned value. The
  mid-alphabet choice `c = 2^15` of U1 matters only for RZ's window `|y| < 2^15` (U1 Lemma 2.1),
  not for confinement.

***

## 3. Node 2: Q1 on Q

**3.1 Inside a class: S-A [S, EC].** Q at `c = 2^15`, in RZ. Boxes: lines 3–5 and `2×2`. One
carrier (`+1` on the current slot, the previous slot or both). Every other slot ranges over
`{−1, 0, 1}`. Every `H`; single-site logs for DT_s; the largest admissible block for DT_A. A
configuration whose values leave `{−1, 0, 1}` is a breach; it is evaluated up to the breach tick
plus one, where the box run is exact.

| Box | Configurations × H | DT_s | DT_A | Breaching configurations | Minimum weight (DT_s) |
|---|---|---|---|---|---|
| line 3 | 3 402 | 0 | 0 | 782 | — |
| line 4 | 61 236 | 0 | 0 | 14 140 | — |
| line 5 | 918 540 | 1 610 | 0 | 184 581 | 3 |
| `2×2` | 61 236 | 1 112 | 0 | 12 912 | 1 |

- **Controls.** The same enumerator, run on U₂, reproduces NP1's counts 0, 184, 1904 and 736
  (PC1). It finds DL1 2.3(f) at `τ₂ = 5` (PC2).
- **Re-run in Q.** The minimum-weight delivery of each box holds in Q itself and passes the ledger
  audit in both branches.
- **The weight-1 delivery.** It is the plaquette: carrier `+1` at `(0,0)`, one excitation `+1` at
  the diagonal `(1,1)` (current slices), `H = (0,1)`, `w* = (0,0)`.
  - In branch 0 the excitation runs `(0,1) → (1,0) → (0,−1) → (−1,0)` alone, with period 4.
  - In branch 1 the two `+1` kick both off-diagonal sites, so `H` is used at `t = 1…4`. `H` is at
    `(0,0)` again at `t = 5`, when site `(1,1)` holds `(1, 0)` in branch 0 and `(−1, 0)` in
    branch 1. Branch 1 has period 6.
  - Both branches are at their initial states at `t = 12`, the common period, and the record is
    erased (MQ4).

  This is the geometry of NP1's S2e. On U₂ that geometry meets only the literal reading of DT; on Q
  it meets DT_s.
- **No DT_A.** Within a confined class a record is erased at the class period (MQ4), so DT_A needs
  a period beyond `τ₂ + 60`. Among the S-A deliveries none holds its record for 60 ticks: the
  measured DT_A count is 0 in every box.

**3.2 Along an infinite class: S-C [EC].** The W2 line of U1 on `ℤe₁` (a torus of length 384 along
the line; every site used is exact by the light cone), run in Q.
- The W2 signal is launched 8 sites away and passes the line cells within 2 of the origin. For
  every such `H`, DT_s holds: `H` is ready before and after the transit, and the log is the line
  site where the signal sits at `τ₂`.
- DT_A fails: once the signal has left `A`, nothing in `A` depends on the carrier.
- No value leaves the line, and the ledger audit holds (CC4).
- **K0.** The launched cells are (phase 0, `+e₁`), (1, `−e₁`), (2, `+e₁`) and (3, `−e₁`). The four
  non-launched cells have no pair-flip launch among A01's candidates. The launched cells are exact
  symmetry images of one case:
  - negation with a phase shift of 2 (K5) maps (0, `+`) to (2, `+`), and (1, `−`) to (3, `−`);
  - the reflection `x ↦ −x` maps (2, `+`) to (1, `−`).

**3.3 Outside the carrier's class, into the background: S-B [S].** Every 7th breaching
configuration of S-A on line 3, line 4 and `2×2` (3 977 of 27 834; PREREG stride rule). Run in Q
itself on `(ℤ/42)³`, horizon 28.

*Exactness.* The box spans at most 3 sites per axis. A site at distance at most 8 from it is at
distance at least `42 − 3 − 8 = 31 > 28` from every periodic copy of the box, so its value up to
`t = 28` is the `ℤ³` value. On `(ℤ/100)³` (X1, S-B-long, X2) the margin is
`100 − 3 − 8 = 89 > 87`.

*Shell.* The tracked shell is truncated on the low side: the box sits at offset 4 and the
distances are not wrapped. Counts by distance, especially at distances 5–8, are therefore lower
bounds.
- Breach times run from 1 to 9 (median 2).
- Every configuration makes contact outside the box. Contact reached distance 8 in 2 852 of them.
- 3 003 configurations contain a site outside the box that is used, returns to `(c,c)` in both
  branches, and has a log holding the carrier at that tick (DT_s outside the carrier's class).
- The two-slice support at `t = 28` has median 196 sites and maximum 509. These breaches grow far
  more slowly than the light cone.
- By MQ3, every such use passes through a breach. S-B shows that breaches produce use outside
  the carrier's class, into unprepared background. This is the boundary condition of the decision
  rule's item (ii).

**3.4 Latch beside a straight line: S-D [S].** One straight W2 line, with a gadget of at most 2
sites in the 24 non-line sites within ℓ∞ distance 1 of the origin (values `±1, ±2`, signal
component only). There are 4 513 gadgets, run at each of the four launched (phase, direction)
cells. The cells are exact symmetry images (§3.2), so the 18 052 runs are about 4 513 distinct
cases. Requirements L1–L5 are those of PREREG §4: quiescence, no radiation, line restoration, DT_A
(`τ₂ ∈ [117, 120]`, persistence 60) and the re-run in Q.

As implemented, L3 and L4 are more lenient than PREREG's wording, which can only admit more
candidates and so does not weaken the negative:
- L3 accepts one window of at most 8 differing line sites anywhere outside `A`;
- L4 does not force `τ₁ = 0`: it accepts any earlier ready instant of `H` with the same value
  before the use.

| Cell | Quiescent (L1) | Fail L2 (radiation) | Fail L3 | Fail L4 (no DT_A) | Pass |
|---|---|---|---|---|---|
| phase 0, `+e₁` | 111 | 78 | 0 | 33 | 0 |
| phase 1, `−e₁` | 111 | 78 | 0 | 33 | 0 |
| phase 2, `+e₁` | 111 | 78 | 0 | 33 | 0 |
| phase 3, `−e₁` | 111 | 78 | 0 | 33 | 0 |

- **Controls.**
  - The calibration oracle passes L1–L4 and is rejected by L5 (PC3); its zero-increment variant
    fails L4 (PC3b).
  - Phases `φ` and `φ + 2` agree under negation of the gadget (K5).
  - Component independence holds on this box (K4).
- **Reading.** For 33 of the quiescent gadgets the signal passes without radiation and the line is
  restored, but nothing in `A` holds the carrier 60 ticks later. The other 78 radiate. The negative
  is bounded to:
  - pair-flip W2 signals;
  - one arrival geometry up to symmetry;
  - gadgets of at most 2 sites in `R_L`, with values `±1, ±2`, signal component only.

***

## 4. Node 3: Q2 on Q

**4.1 Positive probability and cost [W, EC].** Take a DT_s delivery of S-A with `w` non-background
box sites, horizon `τ₂`, and isolation cone `B(box, τ₂) ∖ box`. Under `ν_{c,ρ,κ}`, the event
"pattern on the box, cone at `(c,c)`" has probability at least
`∏_{pattern} ρ κ(z_i) · (1 − ρ)^{|box| − w + |cone|}`. If the cone is at background, the box
evolves as in isolation up to `τ₂`. So the delivery occurs with that probability, which is positive
for every `κ` of full support (U4).

| Delivery | `w` | Cone | Selection cost, `κ` uniform on pairs (`ρ = 10⁻², 10⁻³`) | Selection cost, `κ` on the 8 ternary pairs (`ρ = 10⁻², 10⁻³`; best `ρ`) |
|---|---|---|---|---|
| `2×2`, weight 1, `τ₂ = 5` | 1 | 360 | 43.9, 42.5 bits | 14.9, 13.5 bits; 12.95 bits at `ρ = 1/364` |
| line 5, weight 3, `τ₂ = 5` | 3 | 470 | 122.8, 126.6 bits | 35.8, 39.6 bits; 35.2 bits at `ρ = 3/475` |

The ternary-concentrated `κ` is not of full support. A full-support mixture
`(1 − λ)κ_ter + λu` changes these costs by `O(λ)`.

- **Budget.** DL1 (2.4) needs `(N + 1)(1 − h₂(0)) = 2` bits on the delivering region. The selected
  region carries `32(|box| + |cone|)` bits relative to `u`, so the budget does not bind. The
  binding cost is the selection, as NP1 §4 found on U₂.
- **Transfer identity.** On the two-branch law of any delivery, PR1 2.3 gives
  `K_t(H) + D(p_{Rest,t} ‖ u) = 32n − 1` bits at every `t`, for `n` sites. `K_t(H)` is 32 when the
  rest determines `H`, and 31 when `H` alone carries the carrier bit. The identity holds trivially
  for a deterministic pattern with one fair bit. It records that the delivery redistributes the
  single carrier bit, while the pinned pattern supplies everything else.
- **Weight threshold.** On Q the minimum environment weight for DT_s is 1 (the plaquette). On U₂
  it is 2 (NP1 Proposition N2.2). The leading behaviour of `π` as `ρ → 0` is therefore `ρ`, not
  `ρ²`.

**4.2 In law: dilution [W, EC D1].** Corollary MQ5 transfers NP1 Lemma N2.3 to Q for single-site
carriers whose slots stay in `[c−1, c+1]`: the record error is at least
`2^{−K}(1 − ρ)^{|B(L,t)|}`. While `ρ|B(L,t)|` is small, a fixed apparatus sees records with error
near `2^{−K}`. As on U₂, selecting a delivering pattern returns that designed pattern (NP1 Lemma
N4.1), at the selection cost above.

**4.3 Noise on Q: S-E [S].** Q itself on `(ℤ/32)³`, background `2^15`, three seeds per row.

| `ρ` | `κ` | Fraction at `(c,c)`, `t = 0 / 10 / 20 / 40` | Fraction ever outside `[c−1,c+1]` |
|---|---|---|---|
| `10⁻³` | uniform on all pairs | 0.999 / 0.18–0.32 / 0 / 0 | 1.0 |
| `10⁻³` | 8 ternary pairs | 0.999 / 0.999 / 0.999 / 0.999 | 0 |
| `10⁻²` | uniform on all pairs | 0.99 / 0 / 0 / 0 | 1.0 |
| `10⁻²` | 8 ternary pairs | 0.99 / 0.98–0.99 / 0.98–0.99 / 0.85–0.94 | 0.015–0.046 |
| `5·10⁻²` | uniform on all pairs | 0.95 / 0 / 0 / 0 | 1.0 |
| `5·10⁻²` | 8 ternary pairs | 0.95 / 0.82–0.83 / 0.49–0.53 / 0.11–0.12 | 0.85–0.87 |

- **Reading.** A full-support `κ` (U4) always contains symbols outside `[c−1, c+1]`.
  - In S-E such symbols destroyed the background on the whole torus within 20 ticks, even at
    `ρ = 10⁻³` (about 33 noise sites).
  - Sparse ternary noise stays confined over 40 ticks, as MQ2 requires while no breach occurs.
  - Denser ternary noise breaches through clusters, and the breaches spread.
- **Scope.** This is evidence on a 32³ torus over 40 ticks. Nothing about `ℤ³` beyond the light
  cone is drawn from it. It bears on NP1's open regime (`ρ|B(L,t)|` large): on Q, a full-support
  supply in that regime contains breaching symbols in the cone, and in S-E these did not leave
  readiness intact.

***

## 5. Pressure test of the favourable branch (§A.31)

S-B's DT_s counts outside the carrier's class look favourable. They were pressed in four steps.

1. **X1 [PH].** The ten S-B examples stored in `results.json` were re-run in Q on `(ℤ/100)³`, exact
   to `t = 87` within distance 8 of the box (`posthoc-sb.json`). In all ten, `H` is at `(c,c)` at
   `τ₂` but not at every tick of `[τ₂, 87]`. In all ten, the log at `τ₂` sits inside the
   disturbance (non-background in some branch). In 7 of 10, DT_A as defined holds with `A` = the
   sites at distance 1–8 (about 1 000 sites).
   - In six of the seven, one branch stays on 2–3 sites and the other grows to about 19 000–23 000
     sites by `t = 87`.
   - In the seventh, both branches grow (about 20 000 and 23 000 sites).

   The record is the difference between disturbance and no disturbance (or between two
   disturbances) over a large `A`. The "ready" instant is an isolated return of `H` to `(c,c)`
   inside it.
2. **A02.** A02 was written after X1, which had already shown DT_A in 7 of 10 examples, and
   before the S-B-long run.
   - It defined S-B-long: DT_s, DT_A and DT_A^h, where DT_A^h is DT_A with `H` held at `w*` over
     `[τ₂, τ₂ + 8]`. The sample is every 10th S-B configuration (398).
   - Its clause not to count the results as gem (i) is a post hoc decision. It is not applied: the
     results are reported under the original criterion (§7).
3. **S-B-long [A02].** `results-sb-long.json`; 398 configurations, horizon 87, exact within
   distance 8.

   | Quantity | Count |
   |---|---|
   | DT_s outside the carrier's class (`τ₂ ≤ 27`) | 297 |
   | DT_A (`A` = distance 1–8, persistence 60) | 297 |
   | DT_A^h (`H` held at `w*` over `[τ₂, τ₂ + 8]`) | 229 |
   | exactly one branch confined to the box at `t = 87` | 137 (all among the DT_A cases) |
   | both branches unconfined at `t = 87` | 261 |
   | median support (larger branch) at `t = 87` | 21 454 sites |

4. **X2 [PH].** The first 40 DT_A^h configurations, re-run in Q (`posthoc-x2.json`); the
   ledger audit (streaming: initial state from the ledger, each tick equal to Q's iterate) holds
   on the first 5.

   | Quantity (first qualifying `H`) | Min / median / max, or count |
   |---|---|
   | largest admissible record block `|L|` | median 1 211 sites |
   | fraction of `A` differing between the branches at `τ₂` | 0.028 / 0.038 / 0.253 |
   | the same at `τ₂ + 60` | 0.653 / 0.729 / 0.833 |
   | fraction of `A ∖ {H}` at `(c,c)` in both branches at `τ₂` | 0.676 / 0.962 / 0.971 |
   | a single site of `L` holds the record over `[τ₂, τ₂ + 60]` | 0 of 40 |
   | `H` ready at every tick of `[τ₂, 87]` | 0 of 40 |

   Cost of the first candidate (`results.json`, `A02-cost`):
   - the pattern has weight 2 on line 3, `τ₂ = 17`;
   - the record is read on `A`, up to ℓ1-distance 8 from the box, until `τ₂ + 60`; isolation
     therefore needs the backward cone of radius `τ₂ + 68 = 85` around the box at
     background, which is 862 750 sites;
   - the selection cost under a ternary-concentrated `κ` is 46.3 bits at the best
     `ρ ≈ 2.3·10⁻⁶`, and 1271.2 bits at `ρ = 10⁻³`;
   - under a full-support `κ`, such a cone contains breaching symbols unless `ρ` is very small.

**Reading.**
- *Formal success.* DT_s, DT_A and DT_A^h outside the carrier's class are met on Q by breach
  configurations. Under PREREG §6 item 1 these are formal (i-cond) successes, each conditional on
  its enumerated pattern and priced background.
- *Physical reading.* In every case examined, the mechanism is a one-shot amplified record:
  - the carrier changes whether or how a breach front grows;
  - a site `H` near the box is passed by the leading edge and is quiet for a while;
  - the "record" is the front still sweeping through `A`, which is unprepared background that the
    front consumes.
- Nothing localized is recorded: no single-site record, and most of `A` is still at background at
  `τ₂`. Readiness is consumed, not restored: `H` is overrun again, and `A` does not return to a
  known state.
- These are therefore not deliveries to a re-armed apparatus. This unit runs no test of a stronger
  task (AW-MQ-2).

**AW-MQ-1 (static carriers in DT) [EC CC4].** DL1's DT fixes the carriers' regions at `t = 0` and
requires the log to be disjoint from them. On U₂ carriers never approach (DL1 2.3(c)), so this
excluded nothing. On Q a carrier moves along a W2 line. DT_s is then met by its passage alone, with
the log being the carrier at its new position. DT_A's apparatus and persistence clauses exclude
this. Any reuse of DT on a rule with moving carriers needs such a clause.

**AW-MQ-2 (readiness and record locality) [PH, A02].** PREREG's DT_A (`N = 1`) does not separate
delivery to an apparatus from a carrier-triggered breach front that consumes the prepared
background.
- DT, DT_s and DT_A test readiness at the single instant `τ₂`, at one cell, and accept any
  admissible block as the record, however large.
- In U₂'s finite periodic classes this is harmless: a ready instant recurs with the period, and the
  class is small.
- On Q, a breach front meets all three, and an 8-tick held-readiness variant as well (S-B-long,
  X2).
- *Proposed task for a separate protocol.* It would be fixed before any test, with Issue #866
  accountable. It requires:
  - a record of bounded size fixed in advance;
  - the rest of the apparatus returned to its no-carrier content;
  - readiness held until the next carrier can arrive;
  - `N ≥ 2` deliveries.
- No outcome of that task is attributed here. DL1's and NP1's conclusions use designed patterns in
  finite classes, where these clauses would not change the outcome.

**AW-MQ-3 (background) [W, EC K1].** Confinement of the ternary sector holds at every
`c ∈ {1,…,q−2}`. So the background is a choice among an open set of values, not a tuned one. Its
cost is that of any uniform background: 32 bits per site, or `D(single-site law ‖ u)` per site
under an untuned law. U1's AW-UNIV-1 (vacuum versus background) is this lemma at `c = 0`.

***

## 6. Controls

| Id | Required outcome | Outcome |
|---|---|---|
| PC1 | U₂ counts 0, 184, 1904, 736 | pass |
| PC2 | DL1 2.3(f) found, `τ₂ = 5` | pass |
| PC3 / PC3b | oracle passes L1–L4, fails L5; zero increment fails L4 | pass / pass |
| CC1 | U₂, classes at distance ≥ 3: no cross-class use | pass |
| CC2 | imported controller: DT_s met, audit reports an unaccounted controller; declared, it passes | pass (write at `t = 10`) |
| CC3 | undeclared pattern: audit reports an unaccounted prepared resource | pass |
| CC4 | plain W2 line: DT_s met, DT_A fails | pass |
| CC5 | singleton at `c+2`, and the vacuum with `−1`: breach in one tick | pass |
| K0 | W2 launch per phase (A01 item 2) | pass (4 of 8 cells launched; §3.2) |
| K1 | Lemma MQ1, exhaustive in `r`, five values of `c` | pass |
| K2 | Theorem MQ2 on 300 random configurations (in-range values) | pass (802 instance-ticks) |
| K2b | Theorem MQ2 with out-of-range interior and previous values, seven `c` including wrap (post-review) | pass (700 instance-ticks, all exercised) |
| K3 | U1 Lemma 2.1 at three `c`; countercontrol `c = 0` | pass |
| K4 | component independence on the S-D box | pass |
| K5 | S-D phase symmetry | pass |
| D1 | singleton step of MQ5 in Q | pass |

The verdict function refuses to print a verdict unless every control is green. K5 is in the
control list for `--search` runs (post-review N7).

***

## 7. Productivity verdict and classification

- **(i) Not met in the preregistered searches.** There is no DT_A delivery in S-A, S-C or S-D, and
  S-B did not evaluate DT_A outside the carrier's class (horizon 28).
  - *Formal (i-cond) successes.* Under PREREG §6 item 1 in its formal (i-cond) form:
    - DT_A on Q (re-run in Q) is met by 297 of 398 S-B-long configurations (A02; 229 with DT_A^h)
      and by 7 of the 10 X1 examples;
    - the audit clause was checked on 5; it holds by construction for runs built from the ledger;
    - the cost clause was checked on 1: 46.3 bits at the best `ρ`, ternary-concentrated `κ`,
      over a cone of 862 750 sites.
  - *A02's clause.* A02 preceded S-B-long but followed X1, so its non-counting clause is a post
    hoc decision. The original criterion stands, and these configurations are reported under it.
  - *Physical reading.* The successes are not deliveries to a re-armed apparatus (X2, §5). Each is
    a one-shot amplified record of a carrier-triggered breach front, which consumes the priced
    background; readiness is consumed.
- **(ii) The preregistered conditions hold.** MQ1–MQ3 exclude, on Q, every use of a carrier
  outside its initial class during any window without a breach. Two conditions of PREREG §6 item 2
  hold:
  - the configurations covered are not covered by DL1 or NP1 (q = 2^16, every background, interior
    values unrestricted by the proof);
  - the class boundary matters: in S-B, breaches produce use outside the carrier's class, into the
    background, in at least 3 003 sampled configurations.

  The content is BORDERLINE relative to the productivity test. It elaborates DL1 Theorem 2.2 and
  U1's `G(s) = 0` iff `|s| ≤ 1` (U1 Lemma 2.2). What it adds is the sharp converse, the
  boundary-layer form for any closed set and any `c`, and the location of every channel out of the
  carrier's class at a breach.
- **Classification.**

| Item | Class |
|---|---|
| Lemma MQ1 (sharp), Theorem MQ2, Corollary MQ3 | BORDERLINE (elaborates DL1 Theorem 2.2 and U1 Lemma 2.2) |
| Corollaries MQ4, MQ5 | ELABORATING (DL1 2.3(c), NP1 N2.3 on Q) |
| S-A deliveries on Q; weight 1 on the plaquette | NEW, minor (record-only positive; designed pattern) |
| S-C, CC4 / AW-MQ-1 | NEW assumption-watch marker on DL1's DT |
| X1, S-B-long, X2 / AW-MQ-2 | NEW assumption-watch marker on DL1's DT; stronger task proposed for a separate protocol |
| S-B-long DT_A / DT_A^h configurations (297 / 229), X1 (7 of 10) | formal (i-cond) successes under the preregistered criterion; physically not deliveries to a re-armed apparatus (X2) |
| S-D: no latch | record-only negative, bounded to pair-flip W2 signals, one arrival geometry up to symmetry, gadgets of at most 2 sites with values `±1, ±2` |
| S-E | evidence only |

**Pressure test (§A.31).**
1. MQ1–MQ2 extend DL1 Theorem 2.2's proof in a few lines. The content is the sharp condition
   `r ∈ [c−1, c+1]`, the confinement of the boundary layer only, and the location of every
   channel out of the carrier's class at a breach. Breaches are generic in the searched boxes (S-A: 212 415 of
   the configurations breach), so MQ3 excludes nothing for them.
2. MQ3 is a windowed statement. For a finite class, whether the hypothesis holds for all time is
   decidable. For infinite classes and for noise, MQ3 binds only up to the first breach.
3. The positive in-class deliveries are designed patterns. Their untuned use costs a selection
   (§4.1), as on U₂.
4. The S-D negative covers small gadgets and one arrival geometry only.
5. The formal (i-cond) successes rest on a criterion that admits one-shot amplified records
   (AW-MQ-2). They are reported, not discounted, and their physical reading is stated beside them.

**Fixed point.** One pass, with NEW items. The §A.31 fixed point is not reached.

***

## 8. Deviations

- **K0 launched cells.** A01 item 2 provides for cells with no launch pair. Four of the eight
  (phase, direction) cells have no pair-flip launch among A01's candidates. The S-D family therefore
  ran on 4 cells (18 052 runs), not the 36 104 of PREREG §4. The four launched cells are exact
  symmetry images (§3.2), so the runs amount to about 4 513 distinct cases.
- **S-D torus.** The torus is `384 × 8 × 8` (bipartite), not 7 wide. The first default run used
  width 7, where the wrap seam joins sites of equal parity, and K4 failed for that reason. The S-D
  runs never reach the seam, since L2 stops a candidate at its first value outside line ∪ `R_L⁺`.
- **Implementation bugs fixed before any reported run.**
  - K3's countercontrol first stopped at the window before comparing.
  - K0 first failed where A01 provides "not launched".
  - Both were fixed at `f5879d6a`, before the `--search` run. S-A results were identical in both
    runs.
- **S-B-long.** The first launch was stopped at configuration 0 of 398 because its rate would
  exceed the §A.40 bound. It was switched to an exact int32 step (`1efdf496`; checked equal to the
  int64 step) and re-run.
- **Post hoc material.** X1 and X2 are post hoc and labelled [PH]. S-B-long is defined in A02,
  after X1 and before its own run. X2's ledger audit is the streaming form (initial state built
  from the ledger; every tick equal to Q's int64 iterate), on its first 5 configurations.
- **Post-review changes** (review B1, B3, N3, N7). The changes:
  - The verdict template in `checks/measq_checks.py` was revised to report the preregistered
    searches, the formal (i-cond) count read from `results-sb-long.json`, `posthoc-sb.json` and
    `posthoc-x2.json`, and "use" in place of "contact".
  - K2b was added, and K2's label narrowed.
  - The cost of the first DT_A^h configuration was added (`A02-cost`).
  - K5 was added to the control list for `--search` runs.

  `--search` was then re-run. Against `results.json` at `12a251b0`, every measured value is
  unchanged. The differences are:
  - the verdict block;
  - the label text of K2;
  - the added check K2b (20 checks against 19);
  - the added `A02-cost` entry.

  No measured value, search output or other field differs. The default run is likewise unchanged,
  17 checks against 16. The template change follows the results, as the review requested. The
  decision rule of PREREG §6 is unchanged.
- **Post-re-review fix** (delta review at `6ca6e3f7`, nit 1). The cost cone radius was `τ₂ + 60`,
  which omits `A`'s 8 sites of extent. It is `τ₂ + 68`: 862 750 sites, 46.3 bits at the best `ρ`.
  The verdict wording for the formal criterion (nit 2) was also changed. `--search` was re-run; only
  `A02-cost` and the verdict text differ from `6ca6e3f7`.

***

## 9. What review must check; limits

- **Lemma MQ1.** The case analysis of `⌊(5c + r + 1)/3⌋ ≡ 2c (mod q)` with `0 ≤ r < q`, and K1.
- **Theorem MQ2(b).** Distance ≥ 3 keeps `D₁`'s neighbours out of `D₂`; `∂D₁ ⊂ ∂D`; the
  induction against the run of `D₁` alone; union closedness.
- **Corollary MQ3.** The construction of `D₁` from both branches' supports.
- **Corollary MQ5.** The event `G_k(t)` includes the remaining slot of the carrier site.
- **The S-A enumerator.**
  - PC1/PC2 calibrate it on U₂.
  - Breach handling: exact through breach + 1, because every box site is a boundary site.
  - DT_A's largest-block rule (A01 item 1).
- **S-B and S-B-long exactness.** The distance argument on `(ℤ/42)³`, horizon 28, and on
  `(ℤ/100)³`, horizon 87.
- **S-D classifier.** The L3 window rule (one window of ≤ 8 line sites outside `A`); the PC3
  oracle's rule; K5.
- **The ledger audit (CC2, CC3).** It checks the initial state and every tick. It does not price
  the background beyond 32 bits per site.
- **The formal (i-cond) successes.** 297 of 398 S-B-long configurations, and 7 of 10 X1 examples,
  meet DT_A on Q and are re-run in Q. The audit holds on the 5 audited, and the cost is computed for
  1. They are reported under the unchanged criterion, with their physical reading (X2) beside them.
- **AW-MQ-2.** The proposed task for a separate protocol (Issue #866): a bounded record, a restored
  `A ∖ L`, held readiness and `N ≥ 2`. No outcome of that task is attributed here.
- **Not done.**
  - No Lean.
  - No gadget of more than 2 sites, no signal type other than pair-flip W2, and no other arrival
    geometry.
  - No DT_A evaluation in S-B at horizon 28.
  - No non-uniform background other than the W2 line.
  - No `N = 2` deliveries on Q.
  - No conserved quantities (G3-W1) and no posit audit (POSIT-MIN).

***

## 10. Exact checks and outputs

From this directory:
- `python3 -I checks/measq_checks.py` takes about 25 s: Node 1, controls, S-A, S-C. It writes
  `results-default.json`.
- `python3 -I checks/measq_checks.py --search` takes about 13 minutes on one core. It adds S-B,
  S-D and S-E, and writes `results.json` with the verdict. Exit 0 iff every check holds;
  20/20 hold.
  - The verdict reads `results-sb-long.json`, `posthoc-sb.json` and `posthoc-x2.json` if they are
    present. From scratch, the order is: `--search`, `posthoc_sb.py`, `sb_long.py`,
    `posthoc_x2.py`, then `--search` again.
- `python3 -I checks/posthoc_sb.py` takes about 25 s, writes `posthoc-sb.json`, and runs after
  `--search`.
- `python3 -I checks/sb_long.py` takes about 11 minutes and writes `results-sb-long.json`. Exit 0
  iff the sample has the 398 configurations fixed in A02.
- `python3 -I checks/posthoc_x2.py` takes about 90 s, runs after `sb_long.py`, and writes
  `posthoc-x2.json`.

All lattice arithmetic is integer. Floating point appears only in the printed logarithms of §4.1.

# Review of GAMMA-1 unit G1 r5 (independent, non-author, read-only)

**Object.** `GAMMA-G1-r5.md` (blob `4f3482f9`) and `RESPONSE-G3-FINDINGS-G1.md` (blob `a281e1c6`),
retained on PR #1294 at `91a065e39`. The local copies match those blobs. Inputs checked at the same
commit:
- `GAMMA-G1-r4.md` (blob `91a5d656`, unchanged);
- `GAMMA-G2-r3.md` (blob `43a3f0ca`);
- `GAMMA-G3-r2.md` (blob `ef416922`).

**Authority.** r5 cites #1169 c.6894115930, GAMMA-1 row: "G3's findings against G1 (G3-F10, G3-F11)
are reconciled in a G1 r5 before any comparison uses them". I did not re-read that comment; it is
cited as r5 quotes it.

**Reviewer.** Claude, a separate non-author agent. I reviewed G3 r1 and confirmed G3 r2, so my own
findings are what r5 reconciles. The review is read-only.

**Method.**
- I diffed r4 against r5 in full (260 diff lines).
- I traced each changed passage to G3-F10(a), G3-F10(b) or G3-F11.
- I re-derived every [A-inf] identity r5 adds.
- I read G2 r3 §§1.2, 2.5, 6, 8 and 9 for statements r5 touches.
- I applied §A.31 skepticism to each change that favours a reading.

## Verdict: ACCEPT WITH CHANGES

The reconciliation is sound in substance:
- every change traces to F10 or F11, or to a necessary consequence of one;
- every identity added checks by hand;
- no verdict on γ or D-1 is drawn.

Five changes are needed. Two concern skepticism:
- the herald clause has a protective effect that r5 states with the wrong sign (finding 1);
- NC-γ1 cannot hold for `κ^{r5}`, and r5 does not say so (finding 3).

One concerns §13's completeness (finding 2), one governance (finding 4), and one is wording (finding 5).
A sixth, internal consistency, is optional.

## 1. Re-derivations (all hold)

- **C0's image under background.** With `r_{12} = r_1 + r_2`:
  - additive: `(r_{12} + b) − (r_1 + b) − (r_2 + b) = −b`;
  - dark probability: `−1 + (1 − b)(1 − r_1 − r_2 + r_{12}) = −b`.

  Both equal G2 r3 §6.1.
- **PC-wave, additive form.** The cross term minus `b`.
- **Check 5 with background.** `u = (e + b)/(e + 2b)` lies in `[1/2, 1)` and increases in `e`. So
  `V_u ≤ (1 − ½)/(1 + ½) = 1/3`, which is below every `v_+ ∈ {0.4, 0.5, 0.6}`. "Absent" iff
  `V_u ≤ v_−` or `e` is monotone on each run, because `u` is monotone exactly where `e` is. The dark
  form replaces `e` by `(1 − b)e`. Correct.
- **`I_3` with background.** The coefficients of `I_3` sum to 1, so it becomes `I_3 + b`, or
  `b + (1 − b)I_3`. In Sinha's `ε` (Eq. 4) and in each `I_AB` (Eq. 6) the coefficients sum to 0, so a
  constant background cancels. Correct. "X-3 separates no member" is unchanged.
- **`p_AB − p_A − p_B = I_AB − p₀`.** Correct.
- **The `α` data-side formula.** `α = N_c N_A/(N_1 N_2)` is the sources' own formula (GRA II-53;
  Jacques Eq. 1).

## 2. Minimality

| Change | Traces to | Minimal? |
|---|---|---|
| §5.3 data side (herald vs clock) | F10(a); my G3 r2 optional note | Yes. Additive; model side unchanged. |
| §5.4 coincidence rule restricted | F10(a) | Yes. |
| §5.4 "Gated targets" rule | F10(a), F11 | Yes, apart from the [A-inf] no-image clause: a consequence of r4 §§3.1, 4.2, 5.3 whose effect needs stating (finding 1). |
| §5.4 typing rule | F11 | Beyond the strict minimum, since F11 asks only for a type. It is protective: types are set by conditioning and normalization, never by value (NC-γ1, K-2). Acceptable. |
| §5.4 T-gate (sing, coinc) | F11, both halves | Yes. T-gate-sing is F11's second half (herald-gated single-detector counts). |
| §5.4 all-closed-count item; §5.5 classes | F10(b) | Yes. It applies r4's own background rule. |
| §7.1 C0 `−b_j`, PC-wave `Δ ≠ −b_j` | F10(b) with r4 §§5.1, 5.4 | Yes, forced. F10(b) itself prescribes "`p₀` added to the model", and §5.1 applies `κ` to controls; the alternative, `Δ ≡ 0` against background-subtracted data, is barred by r4 §5.4. See finding 4 on governance. |
| §5.7 check 5 and stability note | consequence of `−b_j` | Yes. The countercontrol still returns a miss at `b = 0`. |
| §7.2 `α` normalization; `I_3` background | F10(a); F10(b) | Yes. No construction changes. |
| §§1, 7.3, 7.4, 8–13 | bookkeeping | Yes, except finding 3. |

No change unrelated to F10 or F11 was found.

## 3. Findings

**1. The herald no-image clause shields K1 from GRA-type misses, and the pressure test states only
the opposite direction (medium).**

What r5 says, at §5.4 "Gated targets" and §10:
- §5.4 states [A-inf] that, with no herald process and no visible-herald route, "a herald-gated datum
  has no image … an absent image, not a miss".
- §10 calls this "a consequence unfavourable to K1".

What the clause does:
- It is unfavourable to K1's coverage credit, since there is no image and so no agreement.
- It is also favourable against K1's falsification. On K1 there is no herald process (MR★:639), and
  G2 r3 §4.2 finds the visible-herald route not available at its scope. So the GRA thesis data
  (`α_exp` = 0.18, herald-gated) can never produce a counted miss against K1's `α`. G2 r3 §1.2 gives
  `α = 1` at the derived level.

Assessment:
- The clause is a defensible consequence of r4 §5.3, under which a herald-conditioned image needs
  `e = (a, E)`, together with SNR-1. It is not tuned to G2's values: it uses no datum value and no law.
- But §A.31 requires a reading that protects the framework to be named and pressure-tested as such.

Change: state both directions in §5.4 and §10. Also state the limit of the shield, which r5 leaves
implicit:
- clock-gated data (Jacques Table I) are normalized by `μ(𝔈_a)`, so they need no herald and keep an
  image on K1;
- X-2 is therefore not removed from K1's comparisons by this clause;
- the remaining blockers are of other kinds: X-2's beam-splitter program lies outside `𝒜_10`, along
  with availability and controls.

**2. §13 is incomplete (medium).** Two G2 r3 statements change scope under `κ^{r5}` and are not
listed.

- **(a) G2 r3 §1.2 "Two-cell coincidences … `α = 1`"; §6.3 "Within one instance the product law has
  `α = 1`".**
  - §13's row says that a comparison with X-2 data "for herald-gated data, a herald-conditioned image,
    which on K1 needs the visible-herald route". It omits the clock-gated case.
  - Under r5 §5.3, Jacques Table I is T-gate-coinc with clock normalization `μ(𝔈_a)`, so it needs no
    herald route. Its typing no longer blocks it from being a candidate X-2 target for a law of this
    form.
  - Jacques reports both α = 0.13 ± 0.01 (single emitter) and α = 1.00 ± 0.06 (faint laser, the
    classical control). Under `κ^{r4}` the data were untyped and not comparable (G3-F11).
  - Add a row. It should say that under `κ^{r5}` typing no longer blocks a clock-gated X-2 comparison.
    It should also say what still blocks one: the X-2 program outside `𝒜_10`, availability, controls
    and AW-σ. The row carries no comparison.
- **(b) G2 r3 §1.2, the fringe candidate's condition 6** ("G1 §7's controls green for the comparison
  … which they are not yet (§6.2)"), **and §6.2** ("Whether the controls are green … needs target
  data").
  - Under r5, C0's required result and its void clause read against `−b_j`, so the criterion for
    green controls that condition 6 refers to has changed.
  - §13 lists §6.2 as "unchanged". The PC-wave law is indeed unchanged, but the greenness criterion it
    defers to is not.
  - Add condition 6 as a scope change. G2's outcome is unchanged: the controls are not evaluated green
    and the candidate stays a candidate.

I checked G2 r3's other statements against r5 and found no further omissions: §§2.5, 6.3, 6.4
(AW-G2-3), 8 and 9, the a6 T-coinc targets and G2-F1 to G2-F7.

**3. NC-γ1 cannot hold for `κ^{r5}`, and r5 does not say so (medium; §A.41).**
- NC-γ1 requires `I`, including `κ`, to be declared "before any `L_a` is evaluated".
- r5 adds "the target types of §5.4 with their typing rule" to NC-γ1's list. But T-gate, the typing
  rule and the data side were declared after G2 r3 evaluated laws and their `κ`-images, so `κ^{r5}`
  does not meet NC-γ1.
- NC-γ5 is the right mechanism: a new instance, reported beside the old, with a trial count. Its row
  in r5 is accurate. But NC-γ5 discloses a late change; it does not certify the change as neutral.

Is the NC-γ5 declaration enough? Here, yes, on three grounds, all of which I checked:
- the trigger is a pair of findings about the form of the data (conditioning, gate counts, all-closed
  backgrounds), recorded in G3 before r5;
- no datum value or model law enters any added rule;
- the change applies alike to the classical controls (Table II-4; Jacques (a)) and to the
  single-emitter data.

Change: say in NC-γ1's row that its checkpoint is not met by `κ^{r5}`. It is met only for instances
declared after r5, and for `κ^{r5}` itself NC-γ5's disclosure stands in for it, on the three grounds
above. Record the trial count after the first evaluation: one added declaration.

**4. The `−b_j` reading answers G2 r3's open owner question 1 in substance (medium; governance).**
- r5 applies the reading and says it "does not record the question as answered". The reading is
  forced by r4 §§5.1 and 5.4 together with F10(b)'s raw route (see §2), and the owner directed the
  reconciliation of F10.
- But r5 changes a required control result: C0's reference value moves from 0 to `−b_j`. That change
  was put to the owner as a question and has not been answered.

Change: either
- state that r4's rules leave no alternative, so question 1 is moot under them, and ask the owner to
  confirm; or
- mark the `−b_j` items as pending that confirmation.

Do not leave the reading applied while the question is formally open. r5's "Direction of `−b_j`" shows
it works against credit; that supports the change on the merits but does not settle authority.

**5. Wording of the rescaling clause (low).**
- §5.4 "Gated targets" says `α` is "not invariant under a common rescaling of the counts". If the
  gate count `N_A` is rescaled with the others, `α = N_c N_A/(N_1 N_2)` is invariant.
- The point is that `α` needs the gate count as a normalization, not only ratios among counts made in
  integration time.
- Change: say "`α` needs per-gate probabilities, hence the gate count". The same wording appears in
  §7.2.

**6. Internal consistency of the read statuses (low, optional).**
- §5.4's T-gate row gives G3 r2's statuses: thesis SECTIONS, Jacques FULL on arXiv.
- §7.3's X-2 row still reads "NOT READ (G3)", with a note that G3 r2's statuses are not applied.
- That keeps r5 within F10 and F11, but leaves two statuses for one datum in the same note. Add
  "see G3 r2 §8" to the §7.3 row.

## 4. Verdicts on γ and D-1

None is drawn. The added text states directions ("work against credit") and scopes, makes no
comparison and counts no miss. §12 states that comparisons using `κ^{r5}` report `κ^{r4}` beside them.
Nothing assumes a finite total substratum beyond the A1 scopes already carried in r4.

## 5. Answers to the coordinator's questions

- **Tuning to an outcome already seen?** No rule uses a datum value or a law. Two effects of the
  changes favour K1 in some respect, and both need explicit statement:
  - the no-image clause (finding 1);
  - X-2 becoming comparable at all, which favours PC-wave's separation and so credit; r5 pressure-tests
    this one.

  The `−b_j` change and the narrowing of check 5 work against credit.
- **Is NC-γ5 enough?** Enough as disclosure, given the three grounds in finding 3. NC-γ1's failure for
  `κ^{r5}` must be stated, not implied.
- **Minimal?** Yes. The typing rule is a protective addition beyond the strict minimum (§2).
- **§13 complete?** No: two rows are missing (finding 2).
- **Verdict on γ or D-1?** None.

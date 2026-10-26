# Independent pre-freeze review: PE-02 plan (charged observer tables), v1 draft

- **Object:** PR #923, branch `research/oi-pseudoentropy-20261025` at `902c4c0d5a7d870e84cf60494955d3ebf3bccd4f`,
  `verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe02_charged_tables_v1/`.
  - `PLAN.md` sha256 `f9e18832…a6f2`.
  - `NOTES.md` sha256 `d06f8d16…1ab`.
  - `design/` holds four files, as committed.
- **Reviewer:** independent of the drafter. Read-only: nothing was edited, committed or pushed.
- **Read:**
  - AGENTS.md: the truth-seeking rule, §A.31, §A.41 and §A.44 (the clone's AGENTS.md has §A.44 at line 1016);
  - the PE-02 PLAN, NOTES and design files;
  - PE-01's PLAN (rev. 5), A1–A3, REPORT, `run.py`, `pe01/generators.py`, `params.preflight` and the retained shards;
  - the thread README's PE-02 passages;
  - Issue #934 and the owner's comment of 2026-10-26.
- **Status of what I ran:** design-only checks on toy instances. No PE-02 experiment was run, no PE-01 cell was
  recomputed, and none of the plan's own advantage cells was evaluated.

## Verdict: **ACCEPT WITH CHANGES** (no freeze until R1–R15 are made and re-reviewed)

- The design answers #934's questions and keeps PE-01 immutable. Its controls are the right kind, and Lemma A-SIM is
  correct.
- Three defects would, as written, void the stage or make its coverage depend on an unsound computation:
  - the `G_weak_mut` control fails at K = 0 (R1);
  - CH-IFF's "names no other condition" clause fails on about 270 PE-01 records (R2);
  - the generalized zero argument is false at K′ = 0, and its rank method does not apply to `G_clkfix`, yet it sets
    Part B's K floor (R3).
- Several design choices lean toward the favourable reading and must be made explicit or neutralized: R4–R8.
- The rest are §A.41/§A.44 and hygiene items.

***

## 1. Lemma A-SIM: correct, with one missing step (R12)

**Proof check (maximum skepticism).**
- **Pathwise identity.** $x_t = x^{\rm p}_t \oplus A_t$ needs the visible update to be $x' = x \oplus b(\text{hidden})$.
  The proof asserts this without justification.
  - It does hold under the hypothesis. If the hidden component of $\varphi(x,\eta)$ does not depend on $x$ and
    $\varphi$ is a bijection, then for fixed $\eta$ the map $x \mapsto x'$ is injective on $\{0,1\}$. It is
    therefore the identity or the flip, i.e. $x' = x \oplus b(\eta)$.
  - The proof should say so, and should state the hypothesis as a one-step property: "the hidden component of
    $\varphi(x,\eta)$ is independent of $x$". "Trajectory" is ambiguous with interventions present.
- **sim's maps are bijections.** $\rho'_y$ is a bijection of $\{0,1\}^{m+1}$; the stated inverse is right. The start
  state $(v_0, 0) = 0^{m+1}$ satisfies EX7.
- **Induction.** With state $(v_t, A_t)$ and input $x^{\rm p}_t$, sim reaches $v_{t+1} = \rho_{x_t}(v_t)$ and
  $A_{t+1}$. The readout event identity holds pathwise, so $\Pr_P$ is equal for every prior on the generator state
  (with prepared memory).
  - $\Pr_{Q_p} = 1/2$ on both sides.
  - Hence `abs` and `signed` are both equal at every K, and the whole window transfers.
- **Consequences.**
  - Under U, activity is worth at most one memory bit on autonomous generators.
  - With CA-EQ, an active m-bit observer on `G_clkfix` (matched prior) equals the passive $(m+1)$-bit $\mathrm{sim}(O)$
    on `G_clk`.
  - Both are correct.

**Exhaustive toy verification.** Script `toy_checks.py`, output `toy_checks.out`. Each case compares the joint law
of $(v_K, x_K)$ for the active O with the law of $(v_K, x^{\rm p}_K \oplus A_K)$ for the explicit passive table
$\mathrm{sim}(O)$, run through the same embedded simulator; every χ is compared exactly.

| Generator | Observers | K | Mismatches |
|---|---|---|---|
| `G_lin`, `G_filt`, `G_clkfix` matched, n = 3 | all active, m ≤ 2 | 0..9 | 0 in 86 530 cases each |
| `G_clkfix` uniform n = 3; `G_lin`, `G_filt`, `G_clkfix` (matched and uniform) n = 4 | all active, m ≤ 1 | 0..9 | 0 |
| 3 random autonomous bijections, H = 8, random non-uniform priors | all active, m ≤ 2 (first), m ≤ 1 (others) | 0..8 | 0 |
| `G_clk` n = 3 (countercontrol) | all active, m ≤ 1 | 0..9 | 39 of 130: the identity fails, as it must |
| Mutant sim with χ′ lacking ⊕A (G_lin) / ρ′ lacking the A-correction (G_filt) | all active, m ≤ 1 | 0..9 | 4 / 12: caught |

**Tightness (`tightness.py`).** On `G_filt` (n = 4, 5), `G_clkfix` (n = 4) and the random autonomous toys, 6/7, 20/21
and 24/28 of the active m = 1 curves are attained by no passive m = 1 observer.
- So A-SIM gives an upper bound, $m' \le m+1$, and m′ = m does not suffice in general (toy evidence only).
- NOTES O9's "turns T2 into a one-line statement" overstates this. Say "gives $m' \le m+1$; minimality open (toy
  instances show m′ = m does not suffice in general)".

**ACT-SIM** must gain the countercontrol and mutants above as required non-vacuity checks (R11). As drafted, the
`G_clk` check is "reported, not required".

**Recommendation:** adopt (O9), with R12.

## 2. Footprint arithmetic: reproduced

- `design/charge_arith.py` and `design/least_primitive.py 24`, rerun with `python3 -I`, reproduce the committed
  `.out` files byte for byte (sha256 `51aa19de…` and `f4c880f4…`); `RULE_REPRODUCES_PE01 True`.
- PE-01's table-size formula $2m2^m + 2^m + 2^{m+1} + c(K)$ equals the recorded `table_size_bits` on all 271 PE-01
  witness records, all with `F = graph of chi`.
- The quoted footprints check: PE-01's witness has $F_U = 6$, $T_R = 31$ ($F_R = 37$) and $T_E = 28$ ($F_E = 34$).
- The §2.4 table rows, the least-n values (R 9/17/36/81/186; E 11/18/31/64/139) and the NOTES $K_{\max}$ table all
  check.
- **"Every charged region empty at n ≤ 8": true.** At θ = 9 the cheapest charged footprint, m = 0 under R, needs
  $2c + 4 \le 9$, so K ≤ 3. Every window needs K ≥ 4.
  - That last step uses K′ = 0 being a zero, which needs $x_0$ uniform. It holds for all five (a′) generators but not
    for `G_weak` (R3).
- **Two facts the plan misses, both exact:**
  - **(i) m = 0 has advantage identically 0 on every (a′) generator, at every K.** The per-round map of an m = 0
    observer ($x \leftarrow x \oplus a$, then φ) is a bijection.
    - For `G_lin`, `G_filt`, `G_clk` and `G_clkfix_u` the prior is uniform on the whole space and invariant, so $x_K$
      is uniform.
    - For `G_clkfix` (matched), the state law after t rounds is uniform on $\{x \oplus q = a t\}$, which is balanced
      in x.
    - Toy-verified, K < 40: maximum |adv| = 0 on all six cases.
    - So `emb_m0_all` can never produce a witness. §3.1's reason for adding it ("the candidates most likely to survive
      the charge") is wrong (R4).
  - **(ii) Under E, every admissible region is contained in R's for m ≤ 1.** $T_E - T_R = \gamma(K{+}1) - c(K) \ge 1$
    (m = 0) and $\gamma(K{+}1) - c(K) - 1 \ge 0$ (m = 1) for K ≥ 1, checked for K < 2²⁰.
    - Within PE-02's computed scope, m ≤ 1, an E-witness is always an R-witness.
    - E is "shorter than $S_R$ for m ≥ 2" only where every region is structurally empty.
    - E therefore adds no independent verdict in scope (R5).

## 3. Model E

**Exactly specified.** Prefix-free, verified on 1 032 668 codewords: m ≤ 2, every table and χ, K ∈ {1, 2, 3, 7, 8, 30,
63}. The lengths match. Two conventions remain unstated:
- the bit order of "x in binary" inside γ (MSB-first);
- the integer labelling of memory states that ρ, a and χ are indexed by (PE-01's labels).

Both must be fixed before freeze (R14).

**θ = n+1 under every model.** It is a defensible choice, but the stated reason is wrong.
- NOTES O1 says option (ii), $\theta = n + 1 + D_C(\varphi)$, with a polynomial code "admits almost nothing".
- In fact any $D_C \ge 0$ makes (ii) admit a superset of (i). Option (i) is the most stringent rule considered, the
  one most favourable to the claim under audit.
- The hard-to-vary property comes from fixing θ independently of the charge, not from (ii) being degenerate.
- Correct the text, and make θ-independence a reported quantity: per witness, $F_C$ and its components; per cell, the
  minimum $F_C$ over U-witnesses in the searched K range. A reader can then apply another θ without re-running (R6).

**Encoding dependence** is acknowledged ("results under E are about E"), and the §2.1 invariance caveat is adequate.

**The charge exceeds #934's literal wording.** #934 says "its transition and action tables, or a fixed encoding of
them". R and E also charge the readout (F, $2^{m+1}$ bits under R, χ under E) and the trigger constant K.
- That moves m = 1's onset from roughly n ≈ 10–13 (transition and action only) to n = 17/18. It is a material choice
  in the favourable direction.
- Charging the readout and trigger is defensible: an interpreter needs them.
- The choice must be stated as a decision with its reason. Each witness must report its component breakdown
  (ρ₀, ρ₁, a, readout, K), so that the transition-and-action-only charge is readable within the searched range (R6,
  new owner decision O10).

**O3.** The reduced-form argument closes existence under reduction for E only. It does not address class-specific
codes.
- A fixed linear-filter code (selector, γ(m+1), GL index, b, c, e, γ(K+1)) would open m = 2 only at K ≤ 7 and n ≥ 22.
  That needs Z ≤ 3 there, which AR-C can confirm is false.
- Add this arithmetic to §2.4, so that "information only" rests on a checked fact (recommendation).

## 4. `G_clkfix`

**A faithful clock ablation.**
- φ^fix is a bijection.
- The hidden pair (h, q) is autonomous.
- With the matched prior the passive record equals `G_clk`'s pathwise: CA-EQ, toy-verified at n = 3, 4, 5 over
  3·2ⁿ steps from every seed.
- Interventions change x and never the emission. CA-STRUCT with its `G_clk` self-test is sound.
- The extra hidden bit is necessary, as NOTES argues.

**Rank method for Z is invalid for `G_clkfix`, and missing for others (part of R3).**
- §4.2 lists `G_clkfix` among the generators "whose hidden step is $\mathbb{F}_2$-linear for each fixed control
  sequence". It is not. The control does not drive the clock; the hidden q does.
- Given $x_0$, the increments are not affine in h: `toy_checks` T6 finds $Y_1..Y_7$ non-affine at n = 4.
- A valid statement is $Z(\texttt{G\_clkfix}) \ge Z(\texttt{G\_clk})$. Given $x_0$, the clock schedule is a function
  of earlier increments, so the PE-01 argument transfers. This is toy-equal at n = 3, 4, 5 (2, 3, 3), and PE-01's
  drafting values are reproduced.
- No method is stated for `G_filt` or `G_clkfix_u` at n > 8.

**θ.** PE-01 (§10, A1) defined θ = n+1 as $\log_2|\mathcal{C}_V \times \mathcal{C}_H|$. `G_clkfix` has n+2 state
bits.
- **Matched prior.** θ = n+1 is justified, but by $\log_2|\mathrm{supp}\,\mu^{\rm fix}| = n+1$: the matched generator
  restricted to its invariant support is isomorphic to `G_clk`. The "LFSR-degree rule" is not the reason.
- **`G_clkfix_u`.** The support is $2^{n+2}$ states, and θ = n+1 departs from PE-01's definition in the stricter,
  favourable direction. Report it at n+1 and n+2, with the governing value an owner decision (R7, O5).

## 5. Controls

**RP-01: sound and can fail.**
- `run.py replay n5-clk --mode result --against … --out …` exists with these arguments and exits 0 or 1.
- `54964146` descends from `af38dc2d`, and `n5-clk.json` and `measurements.json` match the quoted sha256.
- Add pins: PE-01's workflow uses Python 3.12 and numpy 2.2.6, and the replay environment must match (R11).

**CH-IFF: as written it fails spuriously (R2).**
- Of PE-01's 271 witness records, the great majority fail (c), and all but one fail (f_U); only the reported witness
  meets (a)–(e) with (f_U).
- "Every refusal must name (f_C) and no other condition" is false for those records, so the control would void the
  stage.
- Restate it:
  - (1) on records meeting (a′)–(e) and (f_U), admit ⇔ $F_C \le \theta$, and a refusal names exactly (f_C);
  - (2) on every other record, the refusal's condition set equals the independently computed set of failed conditions
    and contains (f_C) iff $F_C > \theta$.
- Specify the synthetic boundary records: (a′)–(e) and (f_U) set true, $F_C \in \{\theta, \theta+1\}$, for m ∈ {0, 1}
  and C ∈ {R, E}, at the n that makes the boundary exact.

**PL: the planted law is correct** (T4: $\Pr[X_K = 0] - \tfrac12 = \tfrac12 - K/2^n$ exactly). The E footprint is
exactly θ = 14 at n = 13, K = 7, which usefully exercises the boundary.
- **Bug (R1).** `G_weak_mut` with $x_0 = 0$ gives advantage 1/2 at K = 0 for χ ≡ 0 (T3: `['1/2', '0', …]`).
- "Every observer must give advantage exactly 0 at every K ≤ 13" fails, and its "zero argument of PE-01 §7" needs
  $x_0$ uniform. Use 1 ≤ K ≤ 13 and cite the generalized argument for K ≥ 1.

**MUT-NC: sound and can fail.**

**ACT-SIM: needs non-vacuity** (R11). The identity must be required to fail on `G_clk` for some observer, and on two
mutant sims.

## 6. §A.41 table and §A.44

**Rows missing for asserted invariants (R11):**
- **RF.** The reduced form (§2.2) is behaviourally equivalent (same exact curves) and is an enumerated member at its
  m′.
- **ZC.** adv = 0 exactly at every 1 ≤ K′ ≤ Z for every computed observer and generator, and at K′ = 0 where $x_0$ is
  uniform; the hypotheses of the generalized argument are checked.
- **M0.** m = 0 advantage is identically 0 on every (a′) generator.
- **INC-RE.** For m ≤ 1, E-admissible implies R-admissible.
- **SIM-P1.** Every `G_clkfix` active m-bit window at (n, K) is a window of the passive (m+1)-bit $\mathrm{sim}(O)$ on
  `G_clk`. Where m + 1 ≤ 3 and the cell is in PE-01's computed range, a passive (m+1) window must be recorded there by
  PE-01.
- **ACT-SIM non-vacuity**, as in §5.
- **RP-01 environment pins**, as in §5.
- **Workflow trigger.** The workflow file has `workflow_dispatch` as its only trigger (§10 asserts this).

EX4 must state that it also reproduces PE-01's $p_n$ and $p'_n$ for n = 3..8, not only §1.1's table.

**§A.44: partly met.**
- "Each checkpoint writes a JSON record … with … the exit status of the check that computed it" is circular: a
  process cannot record its own exit status.
- The plan must state:
  - the schema (file names, keys, types; e.g. `pe02-shard/1`);
  - that exit statuses are read from the host's step conclusions, with marker steps whose `if:` conditions are frozen
    with the workflow;
  - that `verdict.py` reads only those files and conclusions.
- Defer only the field list to an amendment before code, if necessary (R10).

## 7. Departures from PE-01 (are any result-motivated?)

| Departure | Reason fixed in advance? | Finding |
|---|---|---|
| n extended to 9..N_max | Yes: §2.4 arithmetic | Fine. Add a no-extension clause: N_max and every K range fixed by the amendment, never extended after any result (R13). |
| m = 0 added | A reason is given, but it is false | Provably zero on all (a′) generators (§2). Keep it as an exact-zero control (M0), not as a search class with that rationale (R4). |
| Generalized zero argument | Yes: new priors | False at K′ = 0 without uniform $x_0$; rank method misapplied (R3). |
| Recurrence bound under the generator's own prior | Yes | Fine. |
| (a′) includes the ablated generators | Yes | Fine. |
| θ = n+1 for `G_clkfix`/`_u` | Stated as a reading | Departs from PE-01's $\log_2|\mathcal{C}|$ definition in the favourable direction for `_u` (R7). |
| O7, population without (f) | Reason uses PE-01's count (36) | Widening, not narrowing, so acceptable. State in advance what PE-01's retained data already fix (R9). |

## 8. Coverage

- Part B is complete within m ≤ 1 for the enumerated classes. m ≥ 2 is structurally empty for n ≤ 24 under R and E.
- **One coverage hole: Part B's lower K bound $\max(Z+4, w)$ depends on Z,** which §4.2 computes with an invalid
  method for `G_clkfix` and an unstated one for `G_filt` and `G_clkfix_u`.
  - An over-estimated Z silently excludes candidates.
  - Since $K^C_{\max} \le 1023$ (m = 0) and ≤ 63 (m = 1), start every Part B sweep at K = w + 1 = 4, using only the
    K′ = 0 zero, which is proved for the (a′) priors.
  - Use Z for the ZC cross-check only. That removes the dependence at negligible cost (R3).
- **Charge scope** (readout and K charged; R charges $2^{m+1}$ bits for F where prediction needs $2^m$) excludes
  nothing from the search. It shrinks the admissible region in the favourable direction, so it needs an explicit
  decision and breakdown reporting (R6).

## 9. Scope and claims

**No overclaims in the outcome text.**
- §7's non-claims are adequate.
- "A negative result covers only the enumerated class" is stated.
- The resource-model sentence is generated.

**Three wording issues:**
- **Factor outcomes pool across n (R8).**
  - `UNCHARGED_ONLY[C]` compares U-witnesses found at n ≤ 8 (PE-01 data) with C-cells at n ≥ 9. There the U search is
    itself truncated to K ≤ $K^C_{\max}$.
  - The label then reads as "the witness exists but does not survive the charge" when the two were sought on disjoint
    cells. That contradicts §6 item 3's no-pooling rule.
  - Compute factor outcomes per n, or per (n, K-range), and print any union only as a list of per-n labels with the
    n-sets on which U and C were searched.
- **The secondary question is largely fixed by PE-01's retained data (R9).** From the retained shards:
  - no `emb_m1_all` window on `G_clk` at any n, K ≤ K_cx;
  - m = 0 is zero;
  - active m = 2 windows (a)–(e) only at n = 4 (K = 7, 8, 9) and n = 5 (K = 7, 10);
  - `emb_m2_passive` has no window on `G_clk` at any n, K ≤ K_cx.

  Hence:
  - W_act is m = 2 at n ∈ {4, 5} only;
  - every member is `INTERVENTION_NEEDED` by PE-01's data alone;
  - by A-SIM, `BACKACTION_NEEDED` is the question whether $\mathrm{sim}(O)$, a passive m = 3 observer, has the window
    on `G_clk`. PE-01 records passive m = 3 windows there (n = 4: K = 7–9; n = 5: K = 7–20), so it is not
    predetermined.

  The plan should state this in advance and tag the intervention labels "restates PE-01" under the §6 item 10
  productivity test.
- **ACTIVE_ONLY on autonomous generators.** By A-SIM, every active U-witness there has a passive (m+1) twin with
  $F_U + 1$. An `ACTIVE_ONLY` there can be a one-bit footprint artefact. The generated text should print
  $F_U(\mathrm{sim}(O))$ beside each such witness (R9).
- **The backaction sentence** should be scoped: "On `G_clk`(p_n) at (n, m, K), every active window is lost when the
  clock is made unresponsive (`G_clkfix`, matched prior)." That is narrower than "the advantage is tied to …".

## 10. Owner decisions and #934 ambiguities

| Id | Recommendation |
|---|---|
| O1 | (i) θ = n+1, but corrected rationale: it is the most stringent rule; print $F_C$ components and per-cell minimum $F_C$ (R6). |
| O2 | Both, reported separately. State INC-RE: in scope, E ⊆ R, so no E-only witness can arise. |
| O3 | Information only, plus the class-code arithmetic of §3 as a checked design fact. |
| O4 | 24, with a no-extension clause. Optionally drop the m = 0 search beyond the M0 control, since it is provably zero. |
| O5 | Matched primary, uniform variant reported. Governing θ for `G_clkfix_u` is n+2 (PE-01's $\log_2|\mathcal{C}|$, equivalently $\log_2|\mathrm{supp}\,\mu|$), with n+1 also reported. |
| O6 | Not computed. |
| O7 | All (a′)–(e) members, with the population's known extent (m = 2, n ∈ {4, 5}) stated in advance. |
| O8 | Rename this stage. PE-01's immutable PLAN (§3, §7, §10 item 5) binds "PE-02" to the computational-versus-physical stage, and the frozen text cannot be changed. Retitle #934 and rename the directory before freeze, while nothing is frozen. Recommended identifier: the next unused one, PE-04, never reusing PE-02. The README's milestone stays as is. Owner's choice. |
| O9 | Adopt, with R12's added step and the "upper bound" wording. |
| O10 (new) | Charge scope: full description (ρ, a, readout, K) governs, as drafted, with the reason stated and a per-witness component breakdown so that #934's literal "transition and action tables" charge is readable. |

**#934 ambiguities (NOTES §7):**
- **A1:** see O8.
- **A2:** agree with the two label families and the added labels.
- **A3:** agree, but per n (R8).
- **A4, A5, A6, A8:** agree with the drafter's readings.
- **A7:** decide via the support rule (O5).
- **New A9:** "transition and action tables" against the full description (O10).

***

## Required changes

1. **R1.** `G_weak_mut` control: require advantage 0 for 1 ≤ K ≤ 13; K = 0 has advantage 1/2 because $x_0 = 0$.
2. **R2.** Restate CH-IFF as in §5, conditioned on the record's other conditions, and specify the synthetic boundary
   records.
3. **R3.** Fix the generalized zero argument and stop using Z to bound Part B.
   - Restrict the zero to 1 ≤ K′ ≤ Z, with K′ = 0 only when $x_0$ is uniform.
   - Remove `G_clkfix` from the rank method, using exhaustive Z or the bound $Z(\texttt{G\_clkfix}) \ge Z(\texttt{G\_clk})$
     with its proof.
   - State methods for `G_filt` and `G_clkfix_u` at n > 8.
   - Start Part B at K = 4, so that coverage does not depend on Z.
4. **R4.** State and check (M0) that m = 0 is identically zero on every (a′) generator, and replace §3.1's rationale.
5. **R5.** State INC-RE (E ⊆ R for m ≤ 1) in §2.4 and the factor rules, and check it.
6. **R6.** Correct NOTES O1's description of option (ii), and say that (i) is the most stringent. Report per witness
   $F_C$ with its component breakdown, and per cell the minimum $F_C$. Add O10 on charge scope.
7. **R7.** θ for `G_clkfix` justified by $\log_2|\mathrm{supp}\,\mu|$; `G_clkfix_u` at n+2 and n+1 (O5).
8. **R8.** Compute factor outcomes per n; no cross-n pooling between U and C.
9. **R9.** Secondary question:
   - state in advance what PE-01's retained data fix (population extent; `INTERVENTION_NEEDED` for every member);
   - add SIM-P1;
   - print $F_U(\mathrm{sim}(O))$ beside active witnesses on autonomous generators;
   - scope the backaction sentence.
10. **R10.** §A.44: state the output schema and the marker-step / step-conclusion reading. Exit statuses come from the
    host, not from self-written JSON.
11. **R11.** Add §A.41 rows: RF, ZC, M0, INC-RE, SIM-P1, ACT-SIM non-vacuity (`G_clk` countercontrol and two mutant
    sims required to fail), RP-01 environment pins (Python 3.12, numpy 2.2.6), and the workflow-trigger check. EX4
    also reproduces PE-01's n = 3..8 polynomials.
12. **R12.** Lemma A-SIM:
    - state the hypothesis as a one-step property;
    - add the bijectivity step giving $x' = x \oplus b(\eta)$;
    - describe T2 as $m' \le m+1$, with minimality open.
13. **R13.** No-extension clause for N_max and every K range. Complete the `pe02-parameters` block: O1–O10, θ per
    generator, and per-n explicit values cross-checked as in PE-01 A1.
14. **R14.** E conventions: MSB-first binary in γ, and the memory-state integer labelling (PE-01's).
15. **R15.** NOTES hygiene. §1 says "Not committed or pushed" and §4 says the scripts "are not committed", but both
    are committed at `902c4c0d` under `design/`. Correct them.

**Also specify UX:** compare full-subclass window counts (active plus passive) against PE-01's `windows[subclass]`
entries, for K ≤ K_cx, at every n = 3..8, under both `abs` and `signed`.

## Review artifacts

The design-only scripts and outputs are in this directory:

| File | sha256 |
|---|---|
| `toy_checks.py` | `1f82405e…ded2` |
| `toy_checks.out` | `8e797469…02ee` |
| `tightness.py` | `331c9c51…83ee` |
| `tightness.out` | `ed738063…4126` |

PE-01's figures above come from reading the retained shards (`results/shards/*.json`) at `902c4c0d`.

# Independent review: TUNE-1 sourcing unit (TUNE-1-SOURCING.md + NOTES.md)

**Reviewer.** Fresh non-author reviewer (not the writer of this unit, Step 3A, or REC-1). Read-only:
no computation on any OI rule, no commit, push or post. Hand checks only. Branches fetched by name.

**Verdict: ACCEPT WITH CHANGES.** The stop location is right: TC-A's first unsourced part is (b),
the ready resource. NL-C is correctly accepted rather than escaped, and the resource arithmetic is
correct. Six required changes (R1–R6) narrow claims that state more than the cited evidence
supports. None of them moves the stop. R2 to R4 are the §A.31 "negative overstated" items: a
measure-relative or schema-relative negative is worded as unscoped.

***

## 0. Pins verified

- Every blob in the §0 table matches at its stated commit. On `main` at `c3b5f37a`: Main
  `0db17597`, P `84f71030`, AF `ee8582b2`, S3 `a9cbc675`, S4 `17ca08f8`, T1 `84491c8d`, OA1
  `5a16b213`, OA2 `8f8ddf73`, OBS `e657732b`, NPS1 `8f1edce3`, NIS2 `1daf3861`, SUB `9e84cb4f`.
  Off `main`: REC `f1ffac0e` at `9f7d2612`, 3A `7bbec04d` at `8228b3c2`.
- Neither off-`main` head is an ancestor of `c3b5f37a`. Both remote heads equal the pinned commits
  (`git ls-remote`).
- Line citations checked at their commits and found accurate:
  - Main:42, :54, :58, :724 (items (iv), (vii), (viii), (x), (xiii), (xiv));
  - P:85–133, :137–222, :272–280;
  - AF:84–197 (B1.1–B1.3);
  - S3:56–98, :196–214;
  - S4:12, :423–474, :568–575, :616–674, :691–698;
  - OA1:94–135, :141–208, :515–570;
  - OBS:69–73, :100, :121, :449–464, :525–545, :888–918;
  - NPS1:10–16, :83–90; NIS2:14, :128–132; `LA-EQUAL-REVIEW.md` H-rule row (`:164` in its own
    citation);
  - REC:210–226;
  - 3A:200–215, :255–270, :405–520, :531–632, :794–805, :894–906, :966–988.
- Comments read through the REST API:
  - #1236 c.6817129920 (`OWNER`, 2026-11-12T07:04:34Z): "**Not in TUNE-1's scope:**
    continuous-valued cells." Verbatim.
  - #1236 c.6828822665: verbatim.
  - #1169 c.6854241002 and c.6848268369: verbatim.
  - #866 c.6765161496: verbatim, and its scope is NPS1's binary SM ring. The record attributes it
    correctly ("the owner's scope for the native preparation screen").
  - #1147: O-RDY, open, `not authorized`.
- **New:** the owner safeguard the record cites as "relay only" is on GitHub: #1169
  c.6854774010 (`amaybaum`, `OWNER`, 2026-11-13T13:47:03Z). See R1.

***

## 1. NL-C safeguard (check 1)

**Per-interface hypotheses.** All of them hold for TC-A, as N1.1 says. Most hold by the schema's
own definitions:
- the identified test's labels never depend on the preparation's records (AF:98–100);
- a label is a configuration of `C` (P:147);
- the target, with `a·b ∈ [−½, ½]`, is declared (AF:84–91);
- `K ≥ L + 1`.

The bound `|C| ≤ c` holds at every interface with `c = |C_n|`, so NL-C applies to each `I_n` and
gives NL-C′ there. TC-A meets NL-C′ by letting `|C_n|` grow. This is reporting the bound, which the
safeguard requires. It is not an escape.

Wording issue: "No NL-C hypothesis is claimed to fail except the family-level
`sup_n |C_n| ≤ c`" (N1 verdict, §5). This reads as though a hypothesis fails. The family condition
belongs to the FAIL-CLASS rows (S4:641–644), not to the theorem's per-interface hypotheses
(S4:451–456). The safeguard's own terms are "If no hypothesis fails, the bound applies and is
reported". See R1.

**Multi-round reading (N1.3, F-S1), re-derived.**

*Arithmetic.* With `m` fixed, the settings number `M = q^{2m|C|}`. Pigeonhole and NL-C′'s steps
give `q^{2m|C|} ≥ π/arcsin(8ε) − 1 ≥ (1−4ε)/(4ε)`, so `m|C| ≥ ½ log_q((1−4ε)/(4ε))`. Correct.

*Variable lengths 1..m.* Write `Q = q^{2|C|} ≥ 4`. The settings number
`Σ_{j≤m} Q^j ≤ (Q/(Q−1)) Q^m ≤ (4/3) q^{2m|C|}`, so "at most double `M`" is correct. The bound then
loses up to `½ log_q 2`: `m|C| ≥ ½ log_q((1−4ε)/(8ε))`. AW-SRC-1 states the undoubled form
without this correction.

*The proviso is substantive, and the record drops it.* NL-C's step 6 (S4:444–448) uses the fact
that the tests `(c(θ), c_u)` lie in `𝒯_L`, the family on which the Q6′(i) witness is credited
(AF:169–170). An `m`-round gate followed by one read is a test of length `m + 1`. It lies in `𝒯_L`
only if `m + 1 ≤ L`. `L` is a family constant, independent of `n` (AF:171–175). Within the proviso,
therefore:
- `m ≤ L − 1` is bounded;
- the reading gives `|C_n| ≥ ½ log_q((1−4ε)/(4ε)) / (L − 1)`, so `|C_n|` still grows.

"Splitting a gate over rounds moves the growth from space to time" is therefore not what the
reading shows. Within the proviso, time absorbs at most a factor `L − 1`. Beyond it (`m ≥ L`), the
argument as written does not apply, and the case is open.

A possible recovery, not checked to the standard of a result: take the Q6′(i) witness, use Q3′'s
`F(ε; 𝒯_K)` assignment (AF:161), and tie its mean to the Q6′ mean through the separation
`c*_n ≥ c₀` on `𝒯_L`. That would give a bound with a `c₀`-dependent constant for gates with
`ℓ + m + 1 ≤ K`. The writer may attempt it. It must not be asserted without a derivation. See R3.

N1.4 is closed correctly, within finite-cell OI: OA1:111 types settings as configurations of
designated cells, and REC C4 classifies this as following from the premises. N1.5 is closed
correctly for R-lin.

***

## 2. Resource arithmetic (check 2)

All re-derived by hand.

- Sites per run: `|O_n| + K_n|C_n| ≥ (K+1)|C_n|`, since `O ⊇ C` and `K_n ≥ K` disjoint blocks are
  translates of `C` (P:141, :185–191; S4:466–468). Each site is `(y, x) ∈ V × V`, so there are
  `2(K+1)|C_n|` `q`-ary cells. With `q^{2|C_n|} ≥ (1−4ε)/(4ε)` (NL-C′), this gives
  `≥ (K+1) log_q((1−4ε)/(4ε))`. **Correct.** Every designated site is known because `r_O` fixes all
  of `O` (P:143) and every block carries a label (P:190).
- μ-G probability: an event fixing `n` `q`-ary cells has probability `≤ q^{−n}` (D3, OA1:159;
  Lemma P-1). So `≤ q^{−2(K+1)|C_n|} = (q^{−2|C_n|})^{K+1} ≤ (4ε/(1−4ε))^{K+1}`. **Correct.**
- Floor: from `D ≥ 2(K+1)|C_n|`, `q^{D/(K+1)} ≥ q^{2|C_n|} ≥ (1−4ε)/(4ε)`. Hence
  `1/(4ε) ≤ 1 + q^{D/(K+1)}` and `ε ≥ 1/(4(1 + q^{D/(K+1)}))`. **Correct.** It is consistent with
  NL-C′'s range `ε < 1/8`: the floor is `≤ 1/8` for every `D ≥ 0`. For fixed `D` it is weakest at
  `K = L + 1`.
- Scope:
  - The factor `K + 1` comes from the schema: blocks are translates of `C`, and `r_O` fixes all of
    `O`. The scale-free necessity is only `≥ log_q((1−4ε)/(4ε))` `q`-ary cells of θ-content per
    gate.
  - NOTES item 6: within the schema it does not arise. Outside it, the bound survives only as
    `2K|C_n|` from the blocks, unless `C_n` (or `|C_n|` cells of `O_n`) is shown to need
    designation. The replacement of `|O_n|` by `|C_n|` is not shown.

  See R4.

***

## 3. "Premises do not supply it" (check 3)

- **μ-G (N3.1).** Correct.
  - Lemma P-1 (OBS:529–545) is stated for an automorphism of a finite abelian group. R-lin on a
    torus is one.
  - "A bijection cannot produce one" goes beyond Lemma P-1. It is true, because every bijection
    preserves the uniform law and the marginals of a uniform product law are uniform. It should
    cite OA1:147 / :522 ("every bijection") or be marked [W, here]. Minor m2.
- **μ-O (N3.2).** Correct only for **unconditionally** known cells. OA-1, the record's own [R]
  source, states the preparation gap is **measure-relative**: "Under μ-O (derived) and μ-R: N1-K can
  be native (swap); N1-S is open" (OA1:522). OBS:121 records a conditional route: "For rooted laws
  with a full-support visible prior, conditioning on the observed initial value replaces
  preparation" (§3.5, OBS:458–460). The owner recorded this route as a construction step, not a
  physical mechanism (D-OB7, OBS:888–892); H-PREP stays open. N3.2's closing "No ready supply" does
  not follow from its premise. Its own previous sentence routes the question to held records ((e)),
  whose status under μ-O is not settled: D4(b) is μ-G only (OA1:168–170).
- **μ-R (N3.3).** Undecided. This is stated correctly.
- **Consequence.** The header (lines 11–12), the (b) row, the status paragraph after §2's table,
  N3's verdict and §5 say "OI's stated premises do not supply it (N3.1–N3.3)". That overstates N3.3
  (undecided) and N3.2 (unconditional only).

  What the record supports is narrower:
  - excluded under μ-G;
  - under μ-O, not supplied unconditionally, and the conditional route is open;
  - under μ-R, undecided;
  - no producer in any record on `main` (O-RDY open).

  This is enough for the stop: under the stop rule and the record's own marking, (b) is
  *unsourced*. The record does not state an OI-wide impossibility anywhere, and OBS:121 itself says
  "This is not a universal impossibility claim". The unscoped sentences should still be narrowed.
  See R2.
- **Notation collision.** OBS's "H-μ" is the uniform law (OBS:69–73). TUNE-1's H-μ is
  independence of the unread world from the observer (P:145). N3.5 quotes "H-μ has no ready region"
  (OBS:100), and (c) uses H-μ in TUNE-1's sense. See R6.

***

## 4. Rejected alternatives; best candidate (check 4)

**N0.1–N0.4.** Reasons correct and sourced:
- continuous cells are out of scope (c.6817129920, verbatim; P:114–118);
- R-nl needs H-nl, a Layer-0 revision (P:90–112);
- exchange mode needs H-write, and statement (i) fails for it (P:155–167; 3A:413–420);
- `𝓛_∞` needs H-∞ (P:126–129).

**TC-A versus the other candidates.** TC-A is Step 3A's candidate A with free choices fixed:
- the uniform unread-world law;
- the FC-lin-C row `(𝓛_fin, uniform, init)`;
- `INCONCLUSIVE(L5.4)` for `sup = ∞` (S4:654, :668–674).

Candidate C adds an unsourced non-uniform law. B adds H-write. D adds H-nl. **TC-A is the right
choice within TUNE-1's classes.**

**§A.19: one corpus alternative not listed in N0.** OA1:111 admits settings "written by `φ` from
the observer's own records", a native write. It lies outside TUNE-1's schema: init mode is
non-adaptive, and exch mode is H-write. It is not better than TC-A:
- under R-lin such a write still acts by translation (D5: "An affine exchange that writes `c`
  changes neither", OA1:183);
- its write is masked unless a ready cell unmasks it (OA1:522).

It therefore reaches the same ingredient. Add it as a node for completeness (m8).

Also unlisted in N3.5: Main:742's observer-selection rule, which replaces the past hypothesis in its
selecting role, and the mixing hypothesis / (EM) (3A F-3A-2). OA1:561 already disposes of the first
("Main §4.6 supplies only selection"). The second refreshes the hidden sector toward equilibrium,
which is the opposite of known cells. Cite both (m7).

***

## 5. Part-status table (check 5)

| Part | Record's status | Review |
|---|---|---|
| (a) | premise (posit-relative) | Correct under TUNE-1's carrier convention (P:123–125). Also list (ix) (range one, P:87) and (xi). The nearest-neighbour *sum* (coefficient 1) is the reference instance (Main §3.2; SM:296, α = 1), not fixed by the ledger's linearity and range items alone (m1). The record's note that "one fixed substratum for every precision" is met as one rule, and as one world only under H-∞, is correct and matches c.6828822665. |
| (b) | first stop, unsourced | Correct location. Narrow the "do not supply" sentences (R2). "The observer cannot condition on their content" should read "before use": by layout, prefix records do not depend on later blocks (P:206–208) (m4). |
| (c) | mechanism premise (Lemma A-T (a), D5); content as (b); H-μ named, unadopted; encoder etc. unsourced; adequacy is L5.4 | What is derived is the **form** of the action (translation), not that it supplies the required control. OA-1 classes translation-only action as failing OA-1's N2 **under every measure** ("the earliest failure that holds under every measure", OA1:523, :530). Whether it meets TUNE-1's Q3′ is L5.4, open. State both, or "Mechanism: premise" reads as available → derived (R5). The H-xiv handling is correct: designated constant labels, and heralds on prefix records independent of later blocks, so the feedback and herald-conditioning cases do not arise; not derived. |
| (d) | read rule imported; probabilities derived given the law | Correct (P:272–277). |
| (e) | MP-0b only, status undetermined [REC off `main`] | Correct in substance. TC-A's law is the MP-0a form, so D4(b) (μ-G only) is not TC-A's constraint. The relevant line is D4(d): "D4 dissolves under MP-0a" (OA1:174). In-`V` complete records then consume further designated blank cells, beyond F-S2's count. Cite it (m3). |
| (f) | necessity via NL-C′; known-cell, acceptance and floor bounds [W, here]; physical account unsourced | Arithmetic correct (§2). "premise-level consequence of NL-C′": NL-C uses no OI premise (S4:457), so say "follows from TUNE-1's schema (NL-C′ [W, Step 2])" (m10). |

Definable, reachable and physically derived are kept distinct throughout:
- MP-0a: admitted ≠ derived (N5 bullet 1);
- conditioning: not a producer (N5 bullet 2);
- growth: declared ≠ produced (N5 bullet 3).

H-μ and H-xiv are not derived anywhere in the record. Good.

***

## 6. ELABORATING findings (check 6)

- **F-S1.** New relative to 3A, which leaves both routes open [O] at 3A:436–439. S4:697–698 on
  `main` only excludes multi-round gates by definition. As stated it overreaches (§1). Narrowed by
  R3, it remains ELABORATING:
  - within `𝒯_L`, splitting does not remove spatial growth;
  - non-cell encodings are closed in finite-cell OI.
- **F-S2.** Mostly a composition of results already on `main`:
  - NL-C′ already gives `N ≥ (K+1)|C|` sites in init mode (S4:466–468);
  - D3 gives herald cost;
  - 3A:493 (off `main`) already types `r_O` and the blocks as MP-0a cells.

  Its new content: the explicit known-cell rate, the per-run μ-G probability and the floor. That
  meets ELABORATING but not more. "The two unsourced items … are one resource" is an
  identification. The record shows only necessity: control growth entails ready-resource growth at
  that rate. It does not show that a ready supply yields the larger control region, which also
  needs a larger observer region `O_n` and a generating rule (Code Review Rules: necessary →
  sufficient; no identification without a formal map). See R4.
- **F-S3, F-S4, F-S5.** Classified correctly.
  - F-S4 should say "unconditionally known".
  - F-S5 (N3.6) is sound: range one, cones of radius `Kτ`, product law, separation
    `> 2(radius + Kτ)`. It needs H-μ and one designated region per copy, which the record states.
- **Productivity verdict.** "Gem (ELABORATING)" stands after R3 and R4. "Constrain every
  embedded-tunability candidate" must be scoped to TUNE-1's schema with finite alphabet `q`
  (continuous cells are out of scope, not refuted).

***

## 7. §A.42 item 8 table; register (check 7)

- Rows checked against their uses. Classifications correct, with three omissions:
  - #1169 c.6854774010 must replace the "coordinator relay" row (R1);
  - 3A:501 (used in (e)) has no row of its own: provenance, with content on `main` at
    OA1:563–564;
  - 3A:794–805 (§1) is covered only implicitly by the general 3A row (m6).
- The rows marked "support off `main`" (REC:217, REC:220, 3A for the candidate name and the
  wording of statement (i), 3A:896–905) are gaps until landed or narrowed. The record says so. This
  is acceptable for a WIP record that is not landing.
- Register: neutral. All-caps tokens are identifiers or verdict tokens. No self-narration,
  reader-instruction or revision-history phrases. The disclosure of `python3 -I` used only for JSON
  printing and text substitution is adequate; no computation on an OI rule.

***

## 8. Required changes (exact old → new)

**R1 (owner safeguard on record; N1 wording).**
- §0, the bullet beginning "Owner-confirmed safeguard for this unit, as relayed by the
  coordinator": replace the whole bullet with:
  > - #1169 c.6854774010 (`amaybaum`, `OWNER`, 2026-11-13T13:47:03Z), owner decision "Yes, both (Recommended)": "**TUNE-1 sourcing.** The NL-C bounded-control result applies to its per-round bounded label-menu form, including emergent controls of that form. A candidate must show which NL-C hypothesis fails for it, with the source. Calling its control region "emergent" or "growing" is not enough. If no hypothesis fails, the bound applies and is reported." Addressed in node N1.
- N1 verdict:
  - old: "TC-A does not escape NL-C; it accepts the bound and grows. No NL-C hypothesis is claimed to fail except the family-level `sup_n |C_n| ≤ c`."
  - new: "No hypothesis of NL-C fails for any interface of TC-A, so the bound applies at every interface and is reported: NL-C′ at each `I_n`. The FAIL-CLASS rows do not cover TC-A because their family condition `sup_n |C_n| ≤ c` (S4:641–644) is not met. That is not an escape from NL-C: TC-A meets NL-C′ by letting `|C_n|` grow, and the source of that growth is unsourced ((b), (f))."
- §5:
  - old: "Accepted, not escaped: every per-interface hypothesis holds; only the family-level `sup_n |C_n| ≤ c` fails, by the growth NL-C′ requires (N1)."
  - new: "No hypothesis of NL-C fails; the bound applies at every interface and is reported (NL-C′). The FAIL-CLASS rows' family condition `sup_n |C_n| ≤ c` is not met because TC-A grows `|C_n|` as NL-C′ requires (N1)."
- §7: replace the row "Coordinator relay of the owner safeguard (2026-11-13) | §0; N1 | Governance provenance, relay only." with "#1169 c.6854774010 | §0; N1 | Governance provenance, quoted."
- NOTES item 1: resolved; cite c.6854774010.

**R2 (measure-scope the preparation negative).**
- Header:
  - old: "Its first part that OI's stated premises do not supply is the **ready resource**"
  - new: "Its first part not shown to follow from OI's stated premises is the **ready resource**"
- (b) row:
  - old: "OI's stated premises do not supply known-value cells: under posit (iv) read as μ-G"
  - new: "No stated premise is shown to supply known-value cells. Under posit (iv) read as μ-G they are excluded:"
  - Then append after "(Lemma P-1)": "Under μ-O only orbit-constant cells are unconditionally known (N3.2); conditional preparation through held records is open there and under μ-R (OA1:522: "N1-K can be native (swap); N1-S is open"; OBS:121, rooted laws with full-support visible prior, with H-PREP open and D-OB7)."
- Status paragraph after §2's table:
  - old: "Part (b) does not, and it is the first such part in the order (a)–(f)."
  - new: "Part (b) is not shown to, and it is the first such part in the order (a)–(f)."
- N3.2:
  - old: "A time-specific conditional law needs a held record event (D1, OA1:141–143). No ready supply."
  - new: "A time-specific conditional law needs a held record event (D1, OA1:141–143), which is part (e); whether held records supply it under μ-O is open (OA1:522; D4(b) is μ-G only). No unconditional ready supply."
- N3 verdict:
  - old: "It is not supplied by the stated premises (N3.1–N3.3)"
  - new: "The stated premises are not shown to supply it: it is excluded under μ-G (N3.1), not supplied unconditionally under μ-O with the conditional route open (N3.2), and undecided under μ-R (N3.3)"
- §5:
  - old: "OI's stated premises do not supply it (N3.1–N3.3);"
  - new: "OI's stated premises are not shown to supply it (excluded under μ-G; open under μ-O's conditional route and under μ-R; N3.1–N3.3);"
- F-S4:
  - old: "Under μ-O the only known cells are orbit-constant cells,"
  - new: "Under μ-O the only unconditionally known cells are orbit-constant cells,"

**R3 (F-S1 / N1.3 / AW-SRC-1: keep the proviso; drop "space to time").**
- N1.3:
  - old: "at most double `M`. Splitting a gate over rounds moves the growth from space to time; it does not remove it. Unreviewed reading."
  - new: "at most double `M`, giving `m|C| ≥ ½ log_q((1−4ε)/(8ε))`. The proviso is binding: step 6 uses tests in `𝒯_L`, so the reading covers `m + 1 ≤ L`, and `L` is a family constant (AF:171–175). Within it, `m ≤ L − 1` and `|C_n|` still grows; gates with `m ≥ L` are not covered and are open. Unreviewed reading."
- F-S1:
  - old: "NL-C's counting step does not depend on a gate occupying one round: for `m`-round gates the bound reads `m|C| ≥ ½ log_q((1−4ε)/(4ε))`."
  - new: "NL-C's counting step does not depend on a gate occupying one round, for gates whose test lies in `𝒯_L` (`m + 1 ≤ L`): the bound reads `m|C| ≥ ½ log_q((1−4ε)/(4ε))` (fixed length `m`), so `|C_n|` still grows since `m ≤ L − 1`."
- F-S1:
  - old: "do not escape its counting bound."
  - new: "do not escape its counting bound within that proviso; gates longer than `L − 1` rounds are open."
- AW-SRC-1:
  - old: "an embedded control at precision `ε` needs at least `½ log_q((1−4ε)/(4ε))` cells of setting content per gate, spread over space or time."
  - new: "within TUNE-1's schema with a finite alphabet `q`, a gate at precision `ε` needs at least `(1−4ε)/(4ε)` distinct settings, that is, at least `log_q((1−4ε)/(4ε))` `q`-ary cells of setting content."

**R4 (F-S2 necessity only; scope AW-SRC-2 and the productivity verdict).**
- F-S2:
  - old: "is therefore a growth of the ready resource at this rate: the two unsourced items Step 3A lists separately (the ready configuration and the growth of `|C_n|`, 3A:493, :505 [R-off]) are one resource."
  - new: "entails, in initial-condition mode, a growth of the ready resource at least at this rate, so the two unsourced items Step 3A lists separately (3A:493, :505 [R-off]) are linked by necessity. That a ready supply yields the larger control region is not shown: it also needs the larger `O_n` and the generating rule."
- AW-SRC-2:
  - old: "any candidate with a declared ready configuration and designated settings inherits O-RDY at least at this rate."
  - new: "in TUNE-1's initial-condition schema (blocks translates of `C`, `r_O` fixed on all of `O`), any candidate inherits O-RDY at least at this rate; outside the schema the scale-free necessity is `log_q((1−4ε)/(4ε))` `q`-ary cells of setting content per gate."
- Productivity verdict:
  - old: "constrain every embedded-tunability candidate: no candidate escapes NL-C's counting by splitting gates or re-encoding settings, and the growth NL-C′ forces is a growth of the ready resource at a stated rate."
  - new: "constrain every embedded-tunability candidate within TUNE-1's schema (finite alphabet; continuous cells out of scope, not refuted): splitting gates within `𝒯_L` or re-encoding settings does not escape NL-C's counting, and the growth NL-C′ forces entails a growth of the ready resource at a stated rate."

**R5 ((c): the derived form of the action is not derived adequacy).** In the (c) row, after
"Mechanism: **premise** (derived, law-free: Lemma A-T (a); D5)", insert: "What is derived is the
form of the action (translation only). Under OA-1's N2 that form fails controllable interaction
under every measure (OA1:523, :530); whether it meets TUNE-1's Q3′ is L5.4."

**R6 (H-μ notation).** In N3.5, after the quotation "H-μ has no ready region" (OBS:100), insert:
"(OBS's H-μ is the uniform law, OBS:69–73, that is, μ-G; not TUNE-1's H-μ of P:145)."

**Minor (m1–m10).**
- m1: (a): add ledger items (ix) and (xi); note that the coefficient-1 nearest-neighbour sum is
  the reference instance (Main §3.2; SM:296).
- m2: N3.1: cite OA1:147 / :522 for "every bijection", or mark [W, here].
- m3: (e): cite D4(d), "D4 dissolves under MP-0a" (OA1:174).
- m4: (b) row: "cannot condition on their content" → "cannot condition on their content before
  use (prefix records do not depend on later blocks, P:206–208)".
- m5: §1: after "a law Main:58 admits as realization data", add "(admitted, not derived:
  OA1:108–109; selecting it is MP-0a, part (b))".
- m6: §7: add rows for 3A:501 (provenance; content OA1:563–564) and 3A:794–805 (provenance;
  content AF:125–197, P:439–469).
- m7: N3.5: add Main:742 (selection only, OA1:561) and the mixing hypothesis / (EM) (hidden
  refresh, not known cells; Main:443–449, :742) to the searched-and-dismissed list.
- m8: N0: add a node for φ-written settings (OA1:111). It is outside the schema and reaches the
  same ingredient (OA1:183, :522); not selected.
- m9: NOTES item 6: answered in §2 above. Within the schema it does not arise; outside it only
  `2K|C_n|` is shown.
- m10: (f): "premise-level consequence of NL-C′" → "follows from TUNE-1's schema by NL-C′ [W,
  Step 2]".

***

## 9. What stands unchanged

- The candidate selection (N0).
- The stop location: (b), the ready resource.
- MP-0a and H-PREP as the only corpus names, and O-RDY open and not authorized.
- L5.4 and the member specification as non-physical open items.
- Step 3B not eligible.
- All F-S2 arithmetic.
- "Correctness bands unchanged". This is consistency-axis work (§A.23).

# Independent review: TUNE-1 Step 3A author report

**Record reviewed.** `working/tune1-3a/TUNE-1-STEP3A.md` (699 lines, unreviewed author report).
Cited below as `3A:n`.

**Reviewer.** Independent internal review (same model family). Read-only and paper-only: no
computation on any OI rule, no Lean, no commits, pushes or GitHub writes.

**Verdict: ACCEPT WITH CHANGES.** The candidate inventory, the headline and the stop-condition
verdict are correct and phrased as a specification gap, not a quantum failure. The Step 3B gate
statement ("no candidate qualifies") is supported by the records. Seven edits are required:

- **R1.** The NEW finding F-3A-2 does not survive a §A.19 search and has to be reclassified.
- **R2.** (SP) is presented as the single pivot of the classical-only route. That overstates the
  favourable branch.
- **R3.** The "lacks a sourced apparatus" group is applied inconsistently.
- **R4.** Step 2's open L4 escape audit is missing from the inventory, from T1 and from §5.
- **R5.** The owner-guidance source is now on GitHub and has to be cited.
- **R6.** One T2 control row misstates C-POS-1 as a T1 pass, and the summary does not mark T2 as a
  proposal.
- **R7.** One control claim for D overreaches.

## 0. Provenance checks

- **Pins.** `origin/main` is now `62bdc2cf`. `git diff --stat 080cd2be origin/main` is empty on the
  TUNE-1 directory and on `papers/Main.md`, so every `P:`, `AF:`, `S3:`, `S4:`, `T1:` and `Main:`
  line cited at `080cd2be` still holds. The research branch is at `2d064a71`, as pinned.
- **Proposal hash.** The proposal at `080cd2be` has sha256 `2a081101…7499fd5`, which matches M0
  (#1236 c.6816189419).
- **Source copies.** The writer's `src/` copies of the proposal, AMENDMENT-1-final, Sessions 3 and
  4, Main, OA-1 r5, OA-2 r4 and OA-3 r4 are byte-identical (`cmp`) to `git show` of the pinned
  objects. I read from git, not from `src/`.
- **Spot-checked line citations.** All of these resolve to the stated content:
  - proposal: P:85–89, 123–133, 137–150, 155–171, 181–182, 184–199, 211–222, 232–241, 249–258,
    266–271, 272–280, 445–469, 485–486, 563–565, 570–574, 603–623, 642–650, 673–676, 996–1004,
    1028–1030, 1154–1155;
  - amendment: AF:84–197, 245–287, 357–379, 406–420;
  - Session 3: S3:56–88, 196–229, 335–344;
  - Session 4: S4:30–39, 86–101, 383–397, 423–474, 485–497, 572–614, 654–674;
  - OA-2: OA2:157, 173, 381, 476, 499–504, 525–560, 674, 746–750, 765, 775;
  - OA-3: OA3:223–268, 294–347, 383–386;
  - Main: Main:42, 364–381, 564, 596, 724.

## 1. Candidate inventory (check 1)

**Faithful.** The four groups match Step 2's family-class tokens exactly:

| Group | Step 2 token | Hypotheses carried |
|---|---|---|
| A | `(R-lin, uniform / uniform product, init)` families: `INCONCLUSIVE(L5.4)` (S3:335–336) | H-μ (H-∞) |
| B | the `exch` families: `INCONCLUSIVE(L5.4; L5.5)` (S3:337–338) | H-write |
| C | the level-set law (`𝓛_fin`, `exch`) and the non-uniform product law (both carriers, both modes): `INCONCLUSIVE(L5.6)` (S3:339–344) | as listed there |
| D | every R-nl row: `INCONCLUSIVE(NL-A; NL-P)` (S4:579–588) | H-nl |

Each class is narrowed by NL-C to `sup_n |C_n| = ∞` (S4:572–575, :668–674). This is the owner's
list in c.6846408321 and in c.6828822665.

- The gap statements are quoted correctly: L5.4 at S3:213–214, L5.5 at S3:221, L5.6 at S3:228,
  NL-A at S4:595–604 and NL-P at S4:605–606.
- Nothing that Step 2 settled is included. The witness-qualified FC-1, FC-2 and FC-nl rows, and the
  bounded-`|C|` rows, are correctly treated as settled.

**Missing (R4).** Step 2 left one open item that bears on every candidate: the **L4 escape audit**.
It is "necessary conditions on any `PASS-DERIVED`" (P:842–849). Its exact form is proved for R-lin
(S3:276–282) and for R-nl on `𝓛_fin` (S4:519–523). Its approximate, operational form is open
(S3:283–289; S4:523). NL.3 lists L4(a) among the conditions any R-nl candidate must meet
(S4:487–491).

L4 is not a candidate class. It is, however, an open Step 2 condition that a concrete candidate
must meet. Step 3A never mentions it (no hit for `L4`, `Lemma F` or `escape` in 3A). In the same
family, L3′ (Q2, Q3′ and Q6′ imply Q4) is open and "may be false" (AF:409). 3A handles that
correctly by requiring Q4 to be proved directly (3A:476).

## 2. The headline and the stop condition (check 2)

**Correct.**
- Step 2 leaves the shape of `O` and `C`, `τ`, the generating rule, the encoder and `𝔔`
  existential (P:1011–1016).
- No R-lin family is exhibited (S3:206–211).
- No R-nl family is exhibited (S4:485–497; NL-P is "Exhibit…").
- The stop condition is stated as "a **specification gap**. It is not a quantum failure, and it is
  not a negative result about any candidate class" (3A:573–574). §6's last bullet (3A:612–614)
  states that the conditional classification is not an exclusion. I found no implied exclusion.

**Minor (m3).** "Preparation and readout only as a schema" (3A:146, :568) blurs one point. D4 fixes
the readout *rule* completely: the complete history of `O`, with outcome probabilities the
pushforward of `μ` (P:272–277). What is missing is its instantiation, `O_n`, and the preparation
prefixes. Say so in one clause.

## 3. Unsourced ingredients and F-3A-2 (check 3)

**NL-C′ bound: verified.** S4:464–474 gives the bound in 3A:195–196 and :223:

`|C| ≥ ½ log_q(π/arcsin(8ε) − 1) ≥ ½ log_q((1 − 4ε)/(4ε))` for `ε < 1/8`.

The resource bounds `N ≥ |C|` (exch) and `N ≥ (K + 1)|C|` (init) are also from S4:464–474. The
NL-C threshold `sin(π/(q^{2c}+1))/8` matches S4:426–427.

**R1: F-3A-2 is not NEW.** The repetition ensemble "is not stated as an assumption in the governing
texts and has no source" (3A:624–627, :212). A §A.19 search finds that the governing text uses
repetition, and that the corpus already names the relevant premises.

- **The governing text uses it.** Final B4 requires each heralded preparation to report its
  "expected trial count `1/p_acc`", and Q0 requires reporting the trial cost
  `R(ε, K) = max 1/p_acc` (AF:283–287). That presupposes independent repeated trials. The proposal
  speaks of runs accepted or rejected by a herald (P:174–175), and D3 is titled "(ensemble)"
  (P:242). 3A cites only P:181–182, and only as its own reading.
- **Reset is already recorded as underived.** Step 1 lists "a native read and reset" as underived
  (T1:1625). It lists "an unreset carrier" among the access countercontrols that break supplied
  contracts (T1:1696). It records the sphere model's "fresh re-preparation" as supplied (T1:249).
  OA-1's MP-0a, "a past-hypothesis-type supply of ready cells" (OA1:556–562), is the resource that
  resetting `O` to `r_O` before each run consumes.
- **Hidden-sector refresh between runs has a named conditional premise in Main.** Main's mixing
  hypothesis is the corpus's named premise for this. Under it the hidden sector "looks thermalized
  at every coupling event regardless of its post-coupling state". Its `ε = 0` case is "an exact
  reset" (Main:443–449, :498). Its general form is (EM), "an additional conditional physical
  premise" (Main:746–758). Main:758 (ii) also records that a finite permutation's exact Koopman
  operator cannot mix. That is directly relevant to whether successive runs in one deterministic
  world are fresh draws from `μ`.

**What survives.** TUNE-1's interface reads `P^I_π` as frequencies over runs, and its governing
texts do not state which premise makes successive runs reset and independent in one deterministic
world. The nearest named premises are MP-0a (reset) and Main's mixing hypothesis or (EM)
(refresh). Neither is invoked in TUNE-1. This is an **ELABORATING** finding with an
assumption-watch marker, not a structural blind spot "not previously characterized".

Required edit: reclassify F-3A-2 as ELABORATING, cite the antecedents above, and restate the
§3.0 ledger row (3A:212) and the §8 row (3A:652). The current marking reads "sits inside H-μ".
It should read "not stated in TUNE-1's governing texts though used by B4; separate from H-μ (a
time-zero law); nearest corpus premises MP-0a [R-off] and Main's mixing hypothesis/(EM) [P,
conditional], neither applied to TUNE-1 interfaces".

**Productivity verdict (3A:638–640).** The "gem" verdict rested on F-3A-2 as NEW and on F-3A-1.
After R1 and R2 it should read: gem, BORDERLINE. The surviving content constrains a concrete
candidate in two ways: it must name the source of run repetition, and for R-lin it must state
which Theorem E(b) hypothesis it fails. Both points are [W] and conditional on off-`main` work.

**Optional (R8-opt).** The growth of `|C_n|` is marked "unsourced" (3A:223). The question admits
that growth as a resource by design (P:123–125, :211–222; Q0; D1's `n(ε, K)`). The owner requires
that it "must itself be physically explained" (c.6828822665). The cleaner marking is: "admitted
resource; no physical account (owner requirement c.6828822665)". As written, the growth is set
beside H-write as though it were a premise.

## 4. Conditional groupings (check 4)

### OA-2 Theorem E(b): the hypothesis list is correct

| Hypothesis | Source | Note |
|---|---|---|
| (H1) | OA2:499 | R-lin included; a lattice is "taken on a finite-horizon window" |
| H-AR | OA2:182–186 | |
| (H3) | OA2:501 | |
| (H4) | OA2:502 | |
| (xiv) | | |
| (SP) | OA2:519–521 | |

- Transformation noncontextuality is withdrawn (OA2:540–541).
- The measure table (OA2:744–750) supports 3A's claim in C.6: E(b) uses the law only through
  Proposition B(i) and B(ii) (⇐), which hold for every law, and through (xiv).
- (CVX) enters only B(ii) (⇒), which E(b) does not use (OA2:747). Its omission is correct.

### R2: (SP) is not the single pivot

3A states that A and C "turn" on (SP), and that "the escape, if any, would have to come from (SP)
failing" (3A:610–611, :620–622; also :133, :307–309, :589–590). OA-2's own text cuts against this
favourable reading in two ways.

1. **Without (SP), E(b) still yields a preparation-noncontextual model** (OA2:534, :542). Whether
   a preparation-noncontextual prepare–measure model can meet T1 at small `ε` is a question in its
   own right. In the literature a qubit's prepare–measure fragment is preparation-contextual
   ([L] Spekkens, PRA 71, 052108 (2005); the parity-oblivious multiplexing bound 3/4 that 3A itself
   cites at :529–531). So failing (SP) may give a G3 or T2 escape through OA-2's "dual route"
   (OA2:604, N2.1), while T1 remains blocked.
2. **The central question needs T1 and T2 together** (3A:538–540). A non-(SP) member is therefore
   not shown to be an escape for the central question.

Required edit: wherever (SP) is called the pivot, state both halves:
- with (SP), the fragment is simplex-embeddable;
- without (SP), it is still preparation-noncontextual, and whether that alone excludes T1 at
  small `ε` is a Step 3B question at [L] level, not derived.

Places: 3A:133, :307–309, :320–323, :390–392, :589–590, :608–611, :620–623.

*Reviewer remark (not required; [W], unverified).* For R-lin under a coset-uniform law, every
reachable law of `Z₀` is a mixture of uniform laws on cosets of a fixed subgroup (S3:198–204). The
raw (SP) of OA2:519–521 then fails whenever that subgroup is nontrivial. A model on the coset space
might restore measurement noncontextuality. So "(SP) open" may resolve cheaply, in either
direction. This is worth stating as an open item for Step 3B, not as a finding.

### Heralds and record class (m4)

Candidate A is the heralded case (L5.4).
- OA-2's Proc includes heralds and discards (OA2:96–97).
- OA-3 N4.1 records herald typing as an open interface premise (OA3:394–416, :124–127).
- N4.3 shows that (H4) can be replaced by the Lemma 1 effect class (OA3:460–475).

In TUNE-1 the complete history (D4) is retained, which is OA-1's MP-0b. Held-at-use typing is
therefore met by convention. 3A does not cite OA-3 N4. Add one sentence to A.6 saying that heralded
preparations lie inside E(b)'s Proc, and that its herald-typing premise is met by D4/MP-0b. Also
state that the `𝓛_∞` rows of A and C rely on OA2:499's finite-horizon-window reading of (H1).

### B, C and D groupings

- **B (correct).** B is outside E(b). OA2:173 requires "no writes outside `φ`", and (H3) excludes
  supplied control.
- **C (correct).** "Labels act only by translation under every L5.6 law" holds. Lemma A-T (a) and
  (b) are statements about values and do not use the law (S3:59–68, :79–85), and OA-2 E(a) is
  measure-free (OA2:525–527, :748).
- **D (correct, with R7).** "No result excludes it" is correct. OA-2 lists non-affine rules as OPEN
  (OA2:674, :765, :775). OA-2's Corollary E1 (OA2:578–590) is the relevant necessary condition: a G3
  escape needs settings that do not merely translate the joint held record. 3A should cite it.
- **R7 (overreach in D.4, 3A:425–428).** "That shows non-translational setting dependence, which
  is the classical control OA-1 gap 2 asks for" says more than W-nl-2 to W-nl-4 show. Those
  witnesses are single rounds on one- or two-cell regions. They show that the exact total-variation
  dichotomy fails (S4:385–397), and Step 2 says they "say nothing about Q2–Q6" (S4:686–687). What
  they show is that R-nl's record laws are not coset-structured. That is a necessary ingredient of
  MP-1-type control (OA1:556–566), not setting-selective control. Reword accordingly.

### OA-3 scope: stated correctly

Lemma OBS and Theorem S are for one-dimensional rings:
- SM:112's rule, or a rule permutive at an extreme argument with block width `l + r`
  (OA3:225–226, :262–267);
- (PT), and a measurement stage of at least `2(L−2)`;
- horizons `T ≪ L` not covered (OA3:383–386).

3A says these "do not apply to candidate A as stated" (3A:314) and that no three-dimensional
analogue is derived (3A:285). Both statements are correct.

*Reviewer remark ([W], unverified).* R-lin enters every neighbour additively. A face site of a box
`O` has one outside neighbour, which a complete history appears to determine by solving the
update. A three-dimensional analogue of Lemma OBS for R-lin over long horizons may therefore be
short. 3A's "undecided" is the right label, and for A to C, E(b) makes the point moot in any case.

## 5. Test definitions (check 5)

**T1: faithful to the governing texts.**

| Item in 3A | Matches |
|---|---|
| Q0 with `G` and `R` | P:447–449; AF:283–287 |
| Q6′(i) (`ℓ ≤ K − L`), Q6′(ii) (`c₀`) | AF:168–197 |
| Q1 (changed) | AF:147–151 |
| Q3′ | AF:161–167 |
| Q4, proved directly | AF:406–420 |
| Q5′ | AF:153–160 |
| Q2 | P:439–454 |
| D1–D7, uniformity | P:485–486 |
| `K ≥ L + 1` | AF:262–274 |
| Pass is `PASS-DERIVED` | P:603–623 |

- **Omission (R4).** The pass definition omits the L4 escape audit as a necessary condition
  (P:842–849). Add a row: "L4 (necessary): (a) the preparation-to-state map is not an injective
  complete orthogonal frame with H-LIFT (exact form proved for R-lin and R-nl on `𝓛_fin`,
  S3:276–282, S4:519–523; approximate form open, S3:283–289); (b) `N(ε, K)` unbounded." Add it also
  to §5's list (3A:579–590) and to A.2 and D.2.
- **Optional (m1).** Option T1-U (3A:499–501) should also cite Main:496. It records that a
  horizon-independent representation of the intervened process does not exist for generic combs,
  which is prior art for any horizon-uniform requirement. F-3A-5 restates D1 (P:232–236) and
  P:485–486, so it is CONFIRMING, not ELABORATING.

**T2: correctly flagged as a proposal** in §4.2 (3A:512–513).

- **R6(a).** The summary table's "Applicable test" column (3A:146–149) and §1 item 6 (3A:137–138)
  list T2 without that flag. Add "T2 proposed; owner decision" there.
- **R6(b).** The T2 control row says C-POS-1 "passes T1 at `ε = 0` on its protocol class"
  (3A:546). T1's pass is `PASS-DERIVED`, D1–D7 included (3A:479, :485). C-POS-1 is a supplied
  construction (P:675; `OPERATIONAL-ONLY`). Reword to: "meets T1's Q-conditions at `ε = 0` on its
  protocol class; supplied (fails D-clauses), not a T1 pass". The same applies to the classification
  "not classical-reducible [L expectation]", which concerns the operational fragment. It should not
  be read as a statement about the sphere model's ontic model, which is a classical hidden variable.

**KS and Bell: correctly stated.**
- The Kochen–Specker theorem needs dimension at least 3 [L] (3A:552–554).
- Main §3.3's hypotheses (i)–(iv) are at Main:366–381, and the conclusion `|S_CHSH| ≤ 2` at
  Main:381.
- The P:1028–1030 composition postdiction is correctly placed with the larger-system obligations.

## 6. Owner guidance (check 6)

**Applied.** Each candidate gets:
- the three tests (3A:226–241, and per candidate);
- the four-way classification (summary table and the A.7, B.7, C.7 and D.7 nodes);
- the central question, stated and used to frame the verdict (3A:112–116, :576–577);
- interference versus tables (A.5, B.5, C.5, D.5; 3A:493–498);
- the Step 3B gate (3A:576–577).

Persistent incompleteness is tied to the boundary of `O`, the unread law and the dynamics, not to a
forbidden read (D5, P:278–280). That meets the second guidance message in form.

**R3: inconsistent use of "lacks a sourced apparatus".**
- §3.0 concludes "No candidate passes the preparation test as sourced" (3A:231–232), because `r_O`
  and the program blocks are MP-0a-type and unsourced.
- Only B is given the group "lacks a sourced apparatus". A gets an explanation for not receiving it
  (3A:321–323), and D's exchange-mode rows do not get it even though they carry H-write
  (S4:581–583, :587–588).

Required edit, either of two forms:
1. Give every candidate "lacks a sourced apparatus" as a secondary group (`r_O` and program blocks
   per §3.0; H-write additionally for B and for the exchange rows of C and D).
2. Or define the group narrowly, as "requires an unadopted named access hypothesis (H-write)", and
   apply it to the exchange rows of C and D as well as to B.

**R5: guidance source.**
- c.6846442383 (amaybaum, `OWNER`, 2026-11-13T06:59:24Z) is on #1236. It records the writer
  designation "Start; this session writes (Recommended)" and the first guidance message: the three
  tests, the four classes, the central question and the Step 3B gate.
- 3A cites both only "as relayed … not re-fetched" (3A:64–66, :68). §9 says "all seven comments"
  (3A:673), but there are eight.

Required edit: cite c.6846442383 as the record. Note that its wording differs from the relayed
quotation; it is the GitHub version that governs. State that the second guidance message (source of
incompleteness; interference versus tables) is not on GitHub and stands on the coordinator's relay
only.

## 7. NEW labels and readings presented as established (check 7)

- **F-3A-2 NEW: not justified** (R1).
- The other labels are acceptable, with two adjustments:
  - F-3A-5 is CONFIRMING (m1).
  - F-3A-6 (BORDERLINE) should cite D3's robustness clause (P:268–271) as the existing guard
    against tuning the non-uniform marginal (m2).
- **Readings presented as established.** The E(b) hypothesis match is correctly labelled
  "[W, unreviewed]", and the off-`main` OA results are labelled [R-off]. Two passages read as
  established:
  - D.4's control claim (R7);
  - the (SP)-as-sole-pivot statements (R2), which present a reading of OA-2 as deciding where the
    escape must lie.
- §A.46 item 7 is respected: no conclusion uses OA-1, OA-2 or OA-3 as established support (3A:21–23).

## 8. Required edits (exact)

| ID | Location | Edit |
|---|---|---|
| R1 | 3A:212, :624–627, :638–640, :652 | Reclassify F-3A-2 as ELABORATING. Cite AF:283–287 (trial count presupposes repetition), T1:249, :1625, :1696, OA1:556–562 (MP-0a), Main:443–449, :498, :746–758 (mixing hypothesis, (EM), Main:758 (ii)). Restate it as "repetition used but not stated; separate from H-μ; nearest premises MP-0a and (EM), neither applied to TUNE-1". Productivity: gem, BORDERLINE |
| R2 | 3A:133, :307–309, :320–323, :390–392, :589–590, :608–611, :620–623 | Replace "(SP) is the pivot" with both halves: with (SP), simplex-embeddable; without (SP), still preparation-noncontextual (OA2:534, :542). Whether that excludes T1 at small `ε` is [L] and a Step 3B question. Non-(SP) is at most a G3/T2 route (OA2:604) |
| R3 | 3A:146–149, :321–323, :394–396, :447–449 | Apply "lacks a sourced apparatus" consistently (all candidates via §3.0, or narrowly to every H-write row including D's exchange rows) |
| R4 | 3A:256–268, :410–416, T1 table 3A:469–479, §5 list 3A:579–590 | Add the L4 escape audit: exact form proved (S3:276–282; S4:519–523), approximate form open (S3:283–289; S4:523), necessary for `PASS-DERIVED` (P:842–849; S4:487–491) |
| R5 | 3A:64–68, :673 | Cite c.6846442383 for the designation and the first guidance message (its wording governs). Mark the second message as relay-only. Eight comments, not seven |
| R6 | 3A:137–138, :146–149, :546 | Flag T2 as an owner-decision proposal in the summary. C-POS-1 "meets T1's Q-conditions; supplied, not a T1 pass" |
| R7 | 3A:425–428 | Replace "which is the classical control OA-1 gap 2 asks for" with: "record laws not coset-structured for single rounds on one- or two-cell regions; a necessary ingredient of MP-1-type control, not shown to be setting-selective control (S4:686–687)". Cite OA-2 Corollary E1 (OA2:578–590) in D.6 |

Minor edits:
- **m1.** F-3A-5 is CONFIRMING. Cite Main:496 for T1-U.
- **m2.** F-3A-6 should cite P:268–271.
- **m3.** The readout rule is fully fixed by D4; only `O_n` is missing.
- **m4.** In A.6, add heralds inside OA-2's Proc (OA2:96–97), OA-3 N4.1's herald-typing premise met
  by D4/MP-0b (OA3:394–416), and the `𝓛_∞` rows relying on OA2:499's window reading.
- **R8 (optional).** Re-mark the growth of `|C_n|` as an admitted resource with no physical account.

## 9. What Step 3A establishes, and at which layer

Step 3A establishes no theorem and moves no status. It makes three contributions.

1. **A verified record-level finding: the specification gap.** None of the four INCONCLUSIVE
   classes has an exhibited member. The interface, its region and control cells, the ready
   configuration, the layout, the encoder and the generating rule are existential in every Step 2
   record (P:1011–1016; S3:206–211; S4:485–497). This is checkable by search on `main`, and I
   confirmed it. It supports the stop condition and the answer "no candidate qualifies for Step 3B"
   exactly as phrased: a specification gap, neither a quantum failure nor an exclusion.
2. **A paper-level [W] classification, unreviewed until this review.**
   - It is conditional, through a [W] hypothesis match, on OA-2 Theorem E(b). E(b) is an off-`main`
     [R-off] WIP result whose hypotheses include (SP), which is open.
   - It places specified R-lin init members of A and C as classical-only in their prepare–measure
     fragment. After R2 that reads: with (SP), simplex-embeddable; without it, still
     preparation-noncontextual.
   - B and the exchange rows lie outside E(b). D is unclassified by any result.
   - None of this is established in the sense of §A.46 item 1. Every Step 2 input is a paper
     derivation [W], not kernel-checked (#1236 c.6828822665), and every OA input is off `main`.
3. **Test definitions.** T1 is a faithful restatement of Step 2's amended Q-conditions, once R4 adds
   the L4 audit. T2 is a writer's proposal for the owner, not an authorized test.

The whole record is consistency-axis work under §A.23. It moves no correctness assessment, adopts
no premise, and leaves every class INCONCLUSIVE: not excluded, and not shown to survive.

## 10. Reviewer disclosure

**Read.**
- 3A in full.
- From `080cd2be`, the proposal ranges cited above: §§1.1–1.7, §2, M2 (P:814–849) and §6 (P:996–1030).
- AMENDMENT-1-final B1–B4 and B6–B7.
- Session 3, :1–30, :50–400.
- Session 4, :1–60, :84–104, :383–528 and :560–700.
- Step 1, targeted ranges (:240–252, :1618–1628, :1672–1705) and searches.
- OA-1 r5 :90–110, :425–590; OA-2 r4 :1–60, :95–200, :490–620, :735–790; OA-3 r4 :1–130,
  :223–268, :380–500.
- Main at the cited lines, and search hits for frequency, typicality and mixing.
- #1236, all eight comments, through the GitHub MCP read tool.

**Commands.** `git fetch`, `git show`, `git rev-parse`, `git log`, `git diff --stat`, `git ls-tree`,
`git grep`, `sha256sum`, `cmp`, `grep`, `sed`, `cut`, `wc`, `ls`, `mkdir`.

**Not run.** No interpreter, script or computation on any OI rule. No Lean. No commit, push or
GitHub write.

**Files written.** Read-only copies of the sources are in `working/tune1-3a-review/g/`, a
subdirectory. This review is the only other file.

***

## Recheck of r2

**Record.** `working/tune1-3a/TUNE-1-STEP3A-r2.md`: 868 lines, sha256 prefix `a78f6a41b9e658b8`.
r1 is unchanged (sha256 prefix `914f2339b24d8a40`, as stated in r2:4). Method: the full `diff` of
r1 against r2, a grep of r2 for residual wording, and a check of each new citation against `git show`
of the pinned objects. Read-only; nothing computed. Line numbers below are r2's.

**Verdict: ACCEPT.** Every required edit, every minor edit and the optional R8 are applied
faithfully at every site this review listed. The three citation adjustments are correct, and nothing
new overreaches. Two optional wording nits follow below; neither affects any claim.

### 1. Required and minor edits, site by site

- **R1 (F-3A-2 reclassified as ELABORATING).** Applied at four places:
  - the §3.0 repetition row (r2:258), with AF:283–287, P:174–175, OA1:556–562 and Main:443–449,
    :498, :742–758;
  - §7 F-3A-2 (r2:735–752), with T1:249, :1625, :1696 and the statement "neither applied to TUNE-1
    interfaces";
  - the §8 row (r2:778);
  - §1 item 3 (r2:170–171).

  It is stated as "separate from H-μ, which is a time-zero law", which matches P:145. The
  productivity verdict is now "gem, BORDERLINE" (r2:763–766). No residual "NEW" or "repetition
  ensemble" remains.
- **R2 (both halves of (SP)).** Applied at every listed site: §1 item 4 (r2:174–179), the table rows
  for A and C (r2:192, :194), A.4 (r2:343–345), A.6 (r2:362–370), A.7 (r2:392–396), C.6 (r2:466–469),
  C.7 (r2:471–474), §5 item 6 (r2:687–690), §6 (r2:714–721), F-3A-1 (r2:728–732) and F-3A-3 (r2:753).
  - The only remaining "pivot" is the negation "(SP) is not a single pivot" (r2:729).
  - "Escape, if any, would have to come from (SP) failing" is gone.
  - Preparation noncontextuality without (SP) is cited correctly (OA2:534, :542), and the
    literature [L] point is kept at Step 3B level.
- **R3 (form 1: secondary group on every candidate).** Applied in the table preamble (r2:185–188),
  in all four rows, in §3.0 (r2:278–279), and in A.7, B.7, C.7 and D.7. D's exchange rows carry
  H-write (r2:535–536, citing S4:581–583, :587–588).
- **R4 (L4 escape audit).** Applied at:
  - A.2 (r2:316–320);
  - D.2 (r2:495–498): exact form for R-nl on `𝓛_fin`, S4:519–520; not re-derived on `𝓛_∞`, S4:522–523;
  - the T1 "Necessary condition" row (r2:569);
  - §5 item 7 (r2:691–693);
  - the A row of the summary table, and §8.

  All of these citations check.
- **R5 (governing source).** c.6846442383 is quoted verbatim at r2:69–102. I compared it with the
  GitHub comment and it matches. r2 states that this comment governs. The relayed first message is
  kept as context only, and the second message is marked relay-only (r2:134–135, :630). §9 now says
  "eight comments".
- **R6 (T2 status and C-POS-1).** T2 is flagged as a proposal in §1 item 6 (r2:181–182), in the
  "Applicable test" column, and in the §4.2 status line (r2:605–607). The C-POS-1 control now reads
  "meets T1's Q-conditions … supplied … not a T1 pass", and the [L] expectation is scoped to the
  operational fragment (r2:640–643).
- **R7 (D.4 control claim).** D.4 is narrowed (r2:506–511) and §6's first bullet is aligned
  (r2:702–706). Corollary E1 is added to D.6 (r2:523–527) with the correct consequence: W-nl does not
  show more than translation over the horizon. "Gap 2 asks for" is gone.
- **Minor edits.**
  - m1: F-3A-5 is now CONFIRMING (r2:756–758), and Main:496 is cited for T1-U (r2:591–593).
  - m2: P:268–271 is cited at C.3 (r2:450–452) and at F-3A-6 (r2:760–761).
  - m3: the readout wording is fixed at §1 item 2, in the table, at A.3 and in §5 (r2:162–164,
    :323–326, :664–666).
  - m4: covered in A.6 and C.6 (r2:371–376, :469–470).
- **R8 (optional).** Applied at r2:269, :171, :683–684 and :779.
- **Reviewer remarks.** The (SP) remark is recorded at r2:377–381, attributed to the reviewer and
  marked "unverified here and not used". That is acceptable. The remark on a three-dimensional
  Lemma OBS was correctly not applied.

### 2. Citation adjustments

All three are correct.

1. **OA2:102–104.** In OA-2 r4 at `2d064a71`, this is the Proc sentence "It may include heralds
   (conditioning on held records) and discards." My OA2:96–97 was OA-3's citation of an earlier
   revision, so r2's correction is right.
2. **OA2:577–600.** This range runs from Corollary E1's heading (:577) through its "Open exits"
   (:600–604). It covers the quoted statement.
3. **Main:742–758.** (EM) is stated at Main:744, and Main:742 sets out its role. The range is
   correct.

**Optional nit N1.** At r2:409, the quoted words "cannot mix" are attributed to Main:744 and
:758 (ii). The exact words occur only at :758. Main:744 says "exponential mixing cannot hold for it".
Either quote :744's own wording or cite the quotation to :758 alone.

### 3. Overreach and movement

- The following are unchanged from r1:
  - the headline (r2:162–168);
  - the stop condition and its "specification gap … not a quantum failure … not a negative result"
    wording (r2:671–672);
  - the Step 3B answer "No" (r2:674);
  - every primary group and every INCONCLUSIVE label.
- What moved is exactly what was required: the secondary groups (R3), F-3A-2 and F-3A-5 labels (R1,
  m1), and the productivity verdict (R1).
- The new text is hedged where it should be. "At most a route past G3 or T2", "T1 may stay blocked"
  and "a Step 3B question at [L] level, not derived" are all appropriately qualified.
- The hypothesis match is still labelled [W]. §6's last bullet says "without independent
  confirmation", which is accurate: this review checked the match's hypotheses but did not certify
  it.

**Optional nit N2.** A.2 (r2:319) says "Its exact form is proved for R-lin [W] (S3:276–282)", and
the T1 row (r2:569) says "proved for R-lin and for R-nl on `𝓛_fin`". Lemma F assumes "a fixed
bijection `Φ` of a finite configuration set" (S3:241). So the R-lin statement also holds on
`𝓛_fin` only. A covers the `𝓛_∞` rows, so add "on `𝓛_fin`" at r2:319 and make r2:569 unambiguous.

### 4. Disclosure and computation

- §9 (r2:828–836) lists the r2 commands and discloses the stray empty `python3 -`: it waited on
  empty input and was stopped. I cannot observe the writer's process. The disclosure is consistent
  with what I can check:
  - r2 contains no computed output, and its only arithmetic is restated from Step 2;
  - no file in the working root is newer than r1;
  - the only new files in `tune1-3a/` are r2 and this review;
  - `src/` is unchanged (`cmp` against my git extracts).
- No computation on any OI rule is evident.

### 5. Required edits

None. N1 and N2 are optional.

**Nit confirmation (r2 at blob `17076ef7`): CONFIRMED.** Comparing `.r2-pre-nits.md` with r2 shows
exactly the four stated changes, and nothing else:
- r2:319 now reads "on `𝓛_fin`";
- the T1 row at r2:569 now reads "exact form proved on `𝓛_fin` only";
- r2:747 now cites "cannot mix" to Main:758 (ii) alone;
- a recheck-nits note is appended at r2:869–872.

The wording is accurate. Lemma F's hypothesis list opens at S3:241, and its finite-configuration-set
bullet is at S3:242. Main:758 carries the quoted words.

**Commit confirmation (PR #1267 at `b923fa7f`): CONFIRMED.** Against base `62bdc2cf`, the commit adds exactly four files under the TUNE-1 directory: Step 3A, its r2, the review and OBJECTS. Each committed record differs from its reviewed working copy (blobs `4a6c1127`, `17076ef7`, `65217dc0`) only by replacing "working" with "working", on r1:697, r2:832 and review lines 3, 396, 403 and 508; this changes no meaning. Every blob and SHA-256 value in the OBJECTS table matches what I recomputed.

***

## Review of r3 (§2A)

**Record.** `TUNE-1-STEP3A-r3.md` (1,082 lines). The base is r2 (blob `17076ef7`, accepted after
the recheck). Line numbers below are r3's (`r3:n`).

**Method.** I diffed r2 against r3. I checked every §2A citation with `git show` at `origin/main`
`62bdc2cf` (`papers/Main.md` is byte-identical to the copy at `080cd2be`; `papers/SM.md` was read
directly). The off-`main` citations were checked at `2d064a71`. I read #1236 c.6847314661 through the
GitHub API. Read-only and paper-only throughout.

**Verdict: ACCEPT WITH CHANGES.**
- **Fine as written.** The diff is confined to the stated additions. Most citations are exact. Main
  §3.4 is quoted with its hypotheses and both directions. The reformulated question is recorded
  beside the existing one, not in place of it. No classification or verdict moves.
- **Needs correcting.** Seven items need correction (E1–E7):
  - the governing record is not cited;
  - two statements apply the embedded standard as if it held in exchange mode;
  - one [O] sentence reads NL-C's scope favourably;
  - the countermodel list of §2A.5 mislabels three of its supports;
  - Level A's open task inverts TUNE-1's structure;
  - two Main §3.4 statements drop a scope qualifier.

### 1. Diff scope (check 1)

`diff` shows five hunks and nothing else:
- the Standing line (r3:3–7);
- the reformulated question in §1 (r3:160–165);
- the table-preamble pointer (r3:198–200);
- §2A (r3:238–413);
- §11 (r3:1061–1082).

The r2 text, including §1's existing central question and every table entry, is unchanged.

**Nit n1.** The Standing line says "change-map rows in §10", but they are in a new §11.

### 2. Citations (check 2)

**Exact and at the right strength:**

| Cited | What it supports |
|---|---|
| Main:42 | the Definition, quoted |
| Main:26 | "cannot access the complete state … incompleteness is derived" |
| Main:60 | Lemma 1, "only finite visible resolution is a theorem" |
| Main:58 | realization datum `μ_H`, quoted |
| Main:28, :562 | `S ⇔ D ⇔ Q_fb` |
| Main:554 | "representability alone is not the framework's discriminating content" |
| Main:562 | the characterization, quoted with its carrier, kinematics and rules (a)–(f), the five conditions, "each independent … `five_way_minimality`, `oi_alone_not_qm`", and both directions named, as §A.34 requires |
| Main:66, :554 | "none supplied by bare finite OI" |
| Main:360 | PR-box sentence |
| Main:427 | "Removing the screened local-intervention restrictions admits … the PR negative control" |
| Main:431 | converse process dilation |
| Main:580 | "Quantum mechanics enters as the instrument data …" |
| SM:104 | the principle `s(t+1) = φ_{s(t)}(s(t))`, "each `φ_s` is a bijection but `G_{φ_s}` varies with `s`", required by background independence if space is the coupling graph |
| OA3:138–141 | the "not derived or selected by OI" quotation from MECH-2 |
| P:40–42, :147–148, :237–241, :278–280, :422–423 | as cited |
| P:675–676 | C-POS rows |
| AF:316–326 | C-POS rows |

Main §3.4 is not overstated. The characterization is presented as Level A, within complex matrix
kinematics taken as given, and r3:316–318 says what it does not give. Two Main citations lose a
qualifier (E7).

- **E1 (required). The governing record is not cited.** c.6847314661 is on #1236 (`amaybaum`,
  `OWNER`, 2026-11-13T07:51:30Z). It records the decision "Add to Step 3A as r3 (Recommended)" and
  the owner's question verbatim, and its question matches r3's quotation. It also lists §2A's seven
  items, including "Main §3.4 is the nearest existing bridge" and the re-reading of "lacks a sourced
  apparatus".
  - r3 says the decision "is not on #1236 at the time of writing and stands on the relay" (r3:240–245,
    :1077–1082) and cites it as relayed (r3:3, :1063).
  - The comment's paraphrase of the reformulated central question differs in wording from the
    relayed quotation r3 gives at r3:160–165 and :404–409. The comment reads: "what observable
    operational theories emerge from interactions among embedded observers and apparatus, and under
    what intrinsic conditions quantum mechanics emerges rather than classical or supra-quantum
    behaviour".
  - Edit: cite c.6847314661 (author, association and time) as the governing record at §2A's Source
    paragraph, the Standing line, the §11 title and the §11 disclosure. Delete "not on #1236 … stands
    on the relay". At r3:160–165 and §2A.7, give the comment's wording as the record, keep the relayed
    wording as context, and state that the comment governs where they differ.

### 3. The re-reading in §2A.6 (check 3)

- **"Lacks a sourced apparatus" = "not shown derivable from the joint dynamics".** This is faithful
  to c.6847314661 ("will be read as 'not shown derivable from the joint dynamics'").
- **"No classification changes".** This is correct for every candidate's primary, secondary and
  conditional groups, for the stop condition and for the Step 3B answer. Under the re-reading every
  candidate still has `r_O`, the program blocks, run repetition and the growth of `|C_n|` not derived
  (§3.0, F-3A-2).

The edits below concern two statements that apply the embedded standard as if it held in exchange
mode, and one [O] sentence.

- **E2 (required; r3:264–267).** "This is the standard Step 2 already applies to TUNE-1's interface:
  D2 lets only `Φ_F` act and D5 admits no access by declaration" holds only in initial-condition
  mode.
  - D2 also admits "the label exchanges of section 1.2, through the register and write access of
    H-write" (P:237–239).
  - The proposal states that "only an `init` token is a result about the rule alone; an `exch`
    token assumes the observer's writes" (P:563–565).
  - Edit: "This is the standard Step 2 applies in initial-condition mode (D2, D5; P:197–198
    'the strictly rule-only target'). Exchange mode supplies (iii) as the named hypothesis H-write
    (P:155–167, :563–565)."
- **E3 (required; r3:198–200 and the first bullet of §2A.6).** "It does not mean that a separate
  machine is missing … under (i) the apparatus is part of `S` by premise" is false for exchange-mode
  rows.
  - There the register, its reset and the exchange are "a classical write access to `C` that `Φ_F`
    does not supply" (P:157–159).
  - A pass would be "a result about the rule plus an external writer" (r2 B.7; P:563–565).
  - So for B and for the exchange rows of C and D, the apparatus includes an operation not
    implemented by `F`, contrary to (i).
  - Edit: add "For exchange-mode rows (B, and the exchange rows of C and D), the apparatus includes
    the write access H-write, an operation not implemented by `Φ_F`; there the group also records
    that statement (i) itself fails for the apparatus as specified. No classification changes."
- **E4 (required; r3:397–400).** The [O] question, whether NL-C's hypotheses capture "a control
  region that is itself an emergent structure of `F` rather than a designated set of cells", reads
  NL-C's scope favourably.
  - NL-C's proof uses only the finite menu of one-round gate labels and the declared target. It
    uses no rule, law, carrier or designation (S4:441–466; "what it does not use", S4:458–462).
  - Any control whose per-round gate setting is a configuration of a bounded set of cells, whether
    designated or emergent, has a finite menu, so the counting argument applies to it.
  - What NL-C does not cover is outside TUNE-1's schema:
    - gates realized as multi-round sequences, which TUNE-1 excludes by definition ("A gate cannot
      be a sequence of rounds", S4:697; final B1.1);
    - settings not encoded as configurations of a cell set.
  - Edit: "NL-C applies to any control whose per-round gate setting is a configuration of a bounded
    set of cells, whether that set is designated or emergent (S4:441–466). What is open [O] is
    whether interfaces outside TUNE-1's schema, such as gates realized over several rounds
    (excluded by definition, S4:697) or settings not encoded as cell configurations, escape it.
    Whether OA-3's observer model captures other observers is open as OA-3 states (OA3:383–386)."

### 4. Reachable versus definable (check 4)

- **Accurate as written.**
  - The TUNE-1 label menu claim is right (P:147–148), as is its placement by initial condition or
    H-write (P:155–167, :184–199).
  - The SM reading is right: one global map `s ↦ φ_s(s)`, tagged [W].
  - "Which rule operates is … open [O]" is correct. SM:104 states the principle as a requirement
    under the reading that space is the coupling graph, and MECH-2 says its ring example is "not
    derived or selected by OI" (OA3:138–141).
- **Nit n2 (r3:279–280).** "Nothing makes it the world's dynamics" is a reading of Main:580, not
  Main's text. Main:580 says the construction "uses no property of the substratum beyond finiteness
  and reversibility". Tag the clause [W].

### 5. The reformulated central question (check 5)

It is recorded beside the existing question, not in place of it (r3:160–165, :402–409). The
c.6846442383 question at r3:151–155 is unchanged. The governing wording is addressed in E1.

### 6. Overreach and layer tags (check 6)

- **E5 (required; r3:351–377, §2A.5).** The headline is supported: "OI's assumptions … admit
  classical countermodels and supra-quantum constructions". The supra-quantum part is Main:360 and
  :427. The classical part is the Bell-local reference graph (Main:414), the classical
  prepare–measure fragment of the affine class under E(b) [R-off], and Markov laws (Main:431, :554).
  Three of the listed supports are mislabelled:
  - (a) **C-POS-1 and C-POS-2** (r3:368–369) are not constructions under OI's premises. C-POS-1 is
    "Not a lattice interface", its D7 fails and its carrier is a continuum (P:675). Both reproduce
    *quantum* one-qubit statistics with supplied access, which is a different point from a classical
    countermodel. Move them to a separate bullet: "Classical hidden-variable models reproduce
    one-qubit statistics under supplied access (C-POS-1, C-POS-2; not constructions under OI's
    premises, P:675–676; AF:316–326) [R]". That shows quantum statistics do not by themselves
    certify a non-classical substratum.
  - (b) **`𝔊_K`'s** observer sees a contextual gbit, which is neither classical nor quantum. Label it
    "non-quantum (gbit) operational theory from a classical reversible substratum". Note that its
    rule is a "designed non-affine `φ` (posit)" (OA2:769), admitted by Main's Definition but not by
    ledger item (vii).
  - (c) **"Classical, at the level of observable laws"** (r3:361–364): `oi_alone_not_qm` witnesses
    *non-standard*, not necessarily classical, theories. Rewrite as: "Every finite stochastic law,
    Markov laws included, has a finite OI realization (Main:431), and at that level representability
    does not discriminate (Main:554). The same reversible machinery realizes non-quantum finite
    instrument families (Main:582). The five conditions are independent of a fixed C1–C4 process,
    witnessed on the qubit by non-standard theories (`oi_alone_not_qm`, as Main:562 cites it)."
  - (d) **The Bell bullet** (r3:370–372) should carry all of the Corollary's hypotheses (Main:414):
    - the Bell-relevant degrees of freedom are governed entirely by the nearest-neighbour update;
    - one-step interventions on disjoint wings;
    - a ±1 outcome recorded in every run, read outside the other wing's cone;
    - measurement independence and a response-complete deterministic completion.
- **E6 (required; r3:322–324).** "TUNE-1's Q-conditions are one attempt to state such a class
  operationally for one qubit; D6 is what keeps the class from being defined in quantum terms"
  inverts TUNE-1's structure.
  - The Q-conditions are the quantum target, stated against a qubit comparator (P:425–469).
  - The class defined without quantum terms is the derived-family criterion D1–D7, with D6
    excluding quantum vocabulary and compilation.
  - Edit: "TUNE-1's derived-family criterion D1–D7 (P:224–423), with D6 excluding quantum vocabulary
    and compilation (P:281–289), is one attempt to state such a class for one qubit; the
    Q-conditions are the quantum target the class is tested against (P:445–469; AF:80–197)."
- **E7 (required; r3:318–319 and :376).** Two statements drop a scope qualifier.
  - At r3:318–319, "(iv), full reversible control, as not supplied under the substratum's stated
    interventions" omits Main's kernel scope. Add "(kernel `substratumGen_not_control`, on the
    two-state carrier, as Main:80 and :582 cite it)".
  - At r3:376, "which is what §3.4's (i)–(v) name at Level A" should add "within complex matrix
    kinematics taken as given (Main:562)".
- **Nit n3 (r3:340–341).** The mapping "MP-0a is the boundary-condition route, and MP-0b is the
  retained-correlations route" is the writer's reading. Tag it [W].
- **Nit n4 (r3:1077–1079).** The §11 disclosure lists AF:316–319, but §2A.5 cites AF:317–326.
  Align the two to AF:316–326.

**Layer tags otherwise correct.**
- Main is tagged [P], with kernel names "as Main cites them; no Lean was run".
- TUNE-1 records are tagged [R], OA results [R-off], the writer's readings [W], and open questions [O].

### 7. Required edits (summary)

| ID | Location (r3) | Edit |
|---|---|---|
| E1 | :3–7, :240–245, :160–165, :402–409, :1063, :1077–1082 | Cite #1236 c.6847314661 as the governing record. Give its wording of the reformulated question and state that it governs. Delete "not on #1236" |
| E2 | :264–267 | The embedded standard holds in initial-condition mode only. Exchange mode supplies (iii) as H-write (P:155–167, :237–239, :563–565) |
| E3 | :198–200; §2A.6 first bullet | For exchange-mode rows the apparatus includes H-write, not implemented by `Φ_F`, so (i) fails there. Classification unchanged |
| E4 | :397–400 | NL-C covers any one-round gate setting on a bounded cell set, designated or emergent. What is open is multi-round gates or non-configuration settings outside TUNE-1's schema (S4:441–466, :697) |
| E5 | :351–377 | Relabel the supports: C-POS-1/2 as quantum-matching classical models under supplied access (not OI constructions); `𝔊_K` as non-quantum (gbit), with a posited non-affine rule (OA2:769); `oi_alone_not_qm` as non-standard theories; add Main:582; carry all of Main:414's hypotheses |
| E6 | :322–324 | The class without quantum terms is D1–D7 with D6. The Q-conditions are the quantum target |
| E7 | :318–319, :376 | Add "on the two-state carrier" (Main:80, :582) and "within complex matrix kinematics taken as given" (Main:562) |

Nits: n1 (the §10 → §11 reference), n2 ([W] tag on Main:580's reading), n3 ([W] tag on the
MP-0a/MP-0b mapping), n4 (AF:316–326).

**What r3 adds, and at which layer.** r3 adds owner-directed framing only, with no new result. Its
added claims are readings [W] of Main [P], Step 2 records [R] and OA reports [R-off], plus questions
marked [O]. It changes no classification, verdict or Step 3B answer. After E1–E7 its §2A is
accurately sourced and scoped.

***

## Confirmation of r3

**Record.** `TUNE-1-STEP3A-r3.md` (1,157 lines), compared with `.r3-pre-review.md` (1,082 lines).
**Verdict: ACCEPT.** Read-only.

1. **Edits applied at every listed site.**

   | Edit | Applied at | Content |
   |---|---|---|
   | E1 | Standing line, §1 reformulated question, §2A Source, §2A.7, §11 title and disclosure | c.6847314661 cited with author, association and time; "not on #1236 … relay" deleted; comment wording given as the record, relayed wording as context, comment governs |
   | E2 | §2A.1 | standard stated for initial-condition mode only; exchange mode supplies (iii) as H-write |
   | E3 | §1 preamble; §2A.6 first and secondary-group bullets | exchange-mode rows include H-write, outside `Φ_F`; (i) fails there; no classification change |
   | E4 | §2A.6 last bullet | NL-C covers any per-round gate setting on a bounded cell set, designated or emergent; open only outside TUNE-1's schema |
   | E5 | §2A.5 | five relabelled bullets; Main:582 added; Main:414 carried with all its hypotheses; matches the Corollary's text |
   | E6 | §2A.3 | open task restated with D1–D7 as the class and the Q-conditions as the target |
   | E7 | §2A.3, §2A.5 | both qualifiers added |

   The nits are also applied: n1 (§11 reference), n2 (Main:580 clause quoted, [W] tag), n3 ([W]
   tag) and n4 (AF:316–326 in §2A.5 and the disclosure).
2. **Citation adjustments: both correct.**
   - "This mode does not use H-write and is the strictly rule-only target" begins at P:198 and ends
     at :199. My P:197–198 was off by one.
   - NL-C runs from S4:423 to :462. "What it does not use" is S4:457–458. S4:697 is the
     multi-round exclusion.
3. **Added quotations of c.6847314661: verbatim** against the GitHub comment. The two bullets
   joined at §2A.1 keep the comment's own semicolon. The quoted passages are:
   - the decision and question in §2A Source;
   - "observational access, which must be derived … likewise be derived from the joint dynamics";
   - "a configuration being mathematically present …";
   - "Main §3.4 is the nearest existing bridge between the two";
   - "deriving a distribution or ensemble … not building a separate machine";
   - "OI's assumptions still admit classical and supra-quantum models";
   - "will be read as "not shown derivable from the joint dynamics"";
   - the reformulated question.

   No quotation overstates. Each is attributed to the owner record and sits beside the Main or TUNE-1
   source that supports the claim. Main §3.4 is still quoted from Main itself, and the comment is
   cited only for the framing.
4. **Nothing else changed.** Every diff hunk maps to E1–E7, n1–n4 or the §11 disposition and
   disclosure. No primary, secondary or conditional group moves. The stop condition, the Step 3B
   answer and every INCONCLUSIVE label are unchanged.

**Optional note, not required.** "Admitted by Main's Definition (Main:42) but not by ledger item
(vii)" for `𝔊_K` is the writer's reading. It could carry [W].

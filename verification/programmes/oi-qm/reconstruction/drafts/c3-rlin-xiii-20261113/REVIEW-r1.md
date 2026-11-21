# Independent review (r1) of C3-RLIN-r1 and NOTES-r1

**Verdict: REVISE.**

The class-level verdict (C) survives, but it rests on different grounds from the ones the record
gives. The record's main per-reading result, "the exact-copy reading R1 gives (B) for the class
(N1, N2)", holds only for a structural, coefficient-level notion of exact copy. Instance
evaluation in this framework is done on the support, and at that level exact copies are a second
reading that is consistent with the precedents. That reading turns W1 into a gbit in `d = 1` and in
`d = 3`, for every `q` (finding 1). Three things therefore fail as stated: N1's "fresh mixture" claim,
the §7 NEW structural claim, and the conditional R1 bearing in §5. N2 is also unsupported for one of
the two use-time conventions it claims (finding 2). The (B)-branch control is vacuous (finding 3).
Two NEW claims have prior art in the cited sources (finding 5). The algebra I checked is correct:
the W1 table, W1's hypotheses, the R2(i) label sets, the precedent checks for R1, R2(i), R2(ii), R0
and R3, and the C4 directions.

**Target.** Branch `research/c3-rlin-xiii-1169-20261113` at
`00c84af25e101304e78f366d0b026281d5537872` (one commit on `main` `c3b5f37a`; diff = the two files
only). Files: `verification/programmes/oi-qm/reconstruction/drafts/c3-rlin-xiii-20261113/C3-RLIN-r1.md`
(cited `C3:n`) and `NOTES-r1.md` (cited `N:n`).

**Sources read by the reviewer.**
- On `main` at `c3b5f37a`: OA-1 r5, OA-2 r4, OA-3 r4, `TUNE-1-STEP2-PROPOSAL.md`, `papers/Main.md`.
- `research/rec-1-1169-20261113` at `3a3aa146` (fetched by name, no depth): `REC-1-P0-r3.md`,
  `REC-1-P0-CONFIRM-r3.md`, `REC-1-P0-REVIEW-r1.md`, `REC-1-P0-NOTES-r2.md`, `REC-1-r9.md`. The four
  P0 files have the same blobs as at `2a9f10ba`. `REC-1-r9.md` (blob `945b7982`) is not at `2a9f10ba`.
- `research/synthesis-1169-20261113` at `9eeee392`: `SYNTHESIS-r3.md` (MM-2, T5, SQ3).
- GitHub API (read-only): #1169 c.6863414487 (authorization), #1268 review 5892912758 (origin of the
  question), #1268 c.6860582570 (owner's L decision).

**Checks run.** `tools/claims_check.py`, `tools/staleness_check.py`, `tools/voice_check.py` and
`tools/artifact_placement_check.py` all returned OK. `tools/legacy_records_check.py 00c84af2…` returned
self-test OK, 303 records intact. The arithmetic was done by hand; no other script was run.

***

## Answers to the eight review questions, in brief

1. **Decision rule.** It is sound and not rigged. Requiring agreement across admissible readings is
   the right rule when the owner has frozen C-PM and no reading may be adopted. The rule cannot
   produce a spurious (C) as long as the readings that disagree are both admissible. The filter is
   applied correctly to R1, R2(i), R2(ii), R0 and R3. Two weaknesses: the set of readings is not
   exhaustive, which the record itself notes at N:112 (finding 1), and the (B)-branch control is
   vacuous (finding 3).
2. **Faithfulness.** Most of the cited content matches the sources. Two exceptions: C-PM is quoted
   without its own definition of label cells (finding 6), and R3 is identified with P0N's
   "functional variant" (finding 8). No surrogate rule is used. The open carrier question, rings
   versus the simple cubic lattice, does affect R2(i) (finding 4).
3. **Algebra.** N1 is correct structurally and false on the support. The W1 table at ticks 0–2 is
   correct cell by cell, and every class hypothesis holds for W1. The gbit conclusion holds by the
   argument of OA-2 Claim 2, but Claim 2 is a statement about `𝔊_K` and is not applicable "exactly
   as stated" (finding 7).
4. **Reading dependence.** It is genuine, but it is not located where the record puts it. The
   precedents do not distinguish structural from on-the-support provenance, and that choice alone
   decides W1 (finding 1). No reading is forced by the sources; the closest candidate (C-PM's own
   "property of the procedure" clause) does not decide it (finding 6).
5. **C4 and P0.** The two directions are kept apart and are correct. P0 stays O-U. The conditional
   bearings are stated without adoption, but the R1 bearing omits conditions it needs (finding 1(e),
   finding 4).
6. **NEW.** Neither NEW item is new as stated (finding 5).
7. **Bookkeeping.** The classifications are correct. The pins are behind the instructed head, and
   one owner decision the record relies on is cited unquoted (finding 9).
8. **Register.** Clean (finding 11).

***

## Findings

### 1. Major: "exact copy" holds only structurally; the on-the-support exact-copy reading gives (A)

**Where.** C3:132–134 (definition of R1), C3:180–192 (N1), C3:194–210 (N2), C3:285–294 (N5.1),
C3:336–343 (N7), C3:349–352 and :356–359 (§4), C3:380–382 (§5), C3:394 (§6), C3:413–414 (§7 NEW,
structural), C3:426–428 (§8 Q1).

**Evidence.**

(a) R1 as defined is structural. A label passes only to a cell "whose update reads exactly one
cell, with a unit coefficient" (C3:133–134), and inputs are counted from the rule's coefficients
(C3:182–184). Every other object in the record is evaluated on the support: held events, full
retention and C-PM accessibility ("on the support", C3:79–81, :94–97), as in P0 (R2, P0:163–166).
Under `D_0`, designated zeros make a multi-input update an exact copy on the support. The record's own
instance shows this: in W1, `x_3(1) = X_2 + X_4 − Y_3 = a` (C3:236) and `y_3(2) = x_3(1) = a`
(C3:244). So `y_3(2)` is an exact copy of the herald cell `x_2(0)` two ticks after use, which
contradicts "a `y` cell is overwritten by a fresh mixture one tick later" (C3:185). NOTES has the
general case: with `Y ≡ 0`, a single `X_j` gives `x_i(t) = X_j` for `|i−j| ≤ t` of the same parity
(N:46–48). That is an exact, multi-tick light-cone conveyor in R-lin.

(b) Reading R1v (on-the-support exact move), checked by the reviewer. Drop from a cell's update the
inputs that are **fixed constants**: cells whose content at that tick is the same known value under
every admitted procedure (designated cells that are not label or setting cells, P0:116–117, and their
images). `Lab(τ+1)` is then the set of cells whose remaining update has exactly one input, entering
with a unit coefficient, and that input is in `Lab(τ)`. `Lab(t_p)` is as in R1.
- *Instance II* (P0:402–411). `y₀(1) = x₀(0)`: label. `x₁(1) = w + c` has two non-fixed inputs, `w`
  and the setting `c`, which varies with the procedure (P0:116–117): label-free. Reproduced.
  (Counting the setting `c` as a constant would make `x₁(1)` a label and fail this precedent. That is
  why R1v drops only fixed constants.)
- *Instance I* (P0:392–400). `x₀(1) = u + c − p` has three non-fixed inputs: label-free. Reproduced.
- *N8.2(b)* (P0:318–349; P0R:135–144). At tick 4, `r_1`, `r_2` are labels. `s0(4)` reads `s2(3) ∉ Lab`.
  `r_0(4) = r_L(3) + s0(3)` with `s0(3) = 0` fixed, so its one remaining input `r_L(3) = u` is not a
  label. Label-free `(x, u)`. At tick 5, `r_2`, `r_3` are labels, and `r_1(5) = r_0(4)` and
  `r_0(5) = u′ + x` are label-free. Label-free `(y, u′+x, u)`. Reproduced.
- *W1, `d = 1`.* `Lab(1) = {y_1, y_2, y_4, y_7, x_3, x_6}` (`x_3(1) = a`, `x_6(1) = b`, each with one
  non-fixed input in `Lab(0)`), so `Lab(1) ∩ V = {y_7}`. `Lab(2) ∩ V = {y_3}`. `x_4(2) = a − p` and
  `x_7(2) = b + (b+m) − b` each have a non-label non-fixed input. These are exactly R2(i)'s label sets
  on `V` (C3:258–260), so N4's analysis applies unchanged: a gbit.
- *W1, `d = 3`* (embedding of C3:295–297). The transverse inputs of `x_3(1)` are fixed zeros, so
  `x_3(1) ∈ Lab(1)` and `y_3(2) ∈ Lab(2)`. Label-free at tick 2: `(n+5a, a−p, 5b+m, b+m, m)`. This
  gives `b = y_8 − y_10`, and `(n+5a, a−p)` is uniform for each `a`. A tick-1 event is
  label-free-held at tick 2 only through `n+a`, and only when `4 ≡ 0 (mod q)`; then `n+a = n+5a`, and
  the law is still independent of `a`. Retention: `a = y_3`, `n = x_2 − 5a`, `p = a − x_4`, `m`, `b`.
  A gbit for every `q ≥ 2`.

(c) A third reading, R2(iii) (R2 with fixed constant inputs dropped), gives the same label sets as R1v
on all three precedents and on W1. So W1's gbit does not "rest on the two constant cells `x_4(0)`,
`y_3(0)` being herald-record cells" (C3:292–293). That is how R2(i) reaches it. R1v and R2(iii)
reach it by treating those cells as fixed, not as labels.

(d) Consequences.
- The class verdict (C) stands and is more robust: two exact-copy readings that both match the
  precedents, R1 (structural) and R1v (on the support), disagree on W1.
- "Under R1 (exact-move provenance), label-cell-only retention cannot occur" (C3:351–352), N7's R1
  row, and §6 row 1 hold only for the structural reading.
- The NEW item "Second-order rules under (H3) confine exact copies to one tick; multi-tick label
  registers of the N8.2(b) kind do not exist in R-lin" (C3:413–414) is false on the support.
  W1 and W2 are counterexamples: in W2, `x_5(3) = a`, C3:307.

(e) The R1 bearing in §5 (C3:380–382) is stated as if R1 were the exact-copy reading. Fixing
"exact copy" without saying structural or on-the-support fixes nothing.

**Fix.**
- C3:132–134: rename R1 to "R1s (structural exact move)" and add R1v and R2(iii) with the definitions
  in (b) and (c).
- §1.6 precedent paragraph (C3:145–150): add the precedent checks of (b).
- N1 (C3:180–192): restrict the claim to "the only single-input update of the rule's coefficient
  graph is `y_i ← x_i`". Replace "a `y` cell is overwritten by a fresh mixture one tick later" with
  a sentence stating that under `D_0`, multi-input updates can be exact copies on the support
  (W1: `y_3(2) = x_2(0)`; N:46).
- N2, §4, §6, N7: replace "R1" by "R1s" throughout.
- N7 table: add rows "R1v | yes | (A), W1 (`d = 1, 3`, every `q`)" and "R2(iii) | yes | (A), W1".
- N5.1 (C3:292–294): replace the "two constant cells" sentence with (c).
- §4 (C3:356–359): state the gap as two choices the precedents leave open: structural or
  on-the-support provenance, and whether fixed constant cells count as labels or as fixed inputs.
- §5 (C3:380): "if the owner fixes R1s".
- §7: withdraw the NEW structural item, or narrow it to "R-lin's coefficient graph has one
  single-input update, `y_i ← x_i`" and classify it ELABORATING of OA1:335–349, :399 (finding 5).
- §8 Q1: list R1s, R1v, R2(i), R2(ii), R2(iii) and R3.
- N:68 ("R1 as R2(ii) here"): add R1v's label sets.

### 2. Major: N2 is unsupported when the herald is used at the effect's read time

**Where.** C3:196–198 ("any `t_p ≤ T` and either use time"), C3:132–133, C3:395 (§6 row 2).

**Evidence.**
- R1 takes its labels at the use time and propagates them from `t_p` (C3:132–134).
- P0 allows a later use time, "the handoff `t_p` … or a later read" (P0:125–126). Instance II uses
  that case: "held at use in `y₀(1)`, a label cell" (P0:405).
- With use at an effect's read time `τ ≥ t_p + 2`, the herald must be held at `τ`, and the cells
  holding it there are herald records, hence labels (OA3:101–102). R1 never says which cells of
  `V(τ)` those are. Its propagation from `t_p` gives `Lab(τ) = ∅` even though the herald is held at
  `τ`, which conflicts with OA3:101–102 under this convention.
- N3.1 itself observes that under R1 the herald record becomes computable from mixed cells
  (C3:214–218).
- So N2 is established only with use time `t_p`.

**Fix.**
- C3:196–198: replace "either use time" with "use time `t_p`".
- Add one sentence: with use at each effect's read, R1 does not determine which cells of `V(τ)` hold
  the herald, so N2 is open for that convention.
- Carry "use time `t_p`" into §6 row 2 (hypotheses), §4 and the §5 R1s bearing.

### 3. Moderate: the (B)-branch control is vacuous

**Where.** C3:171–173 (control rule), C3:222–224 (N3.3), C3:415 (§7 ELABORATING "W1 as the
multi-tick control P0 lacked").

**Evidence.**
- Under R1s, `Lab(T) = ∅` for every instance with `T ≥ t_p + 2` (N2). So (LF) at `T` holds by
  definition there, and W1 under R1s cannot fail: it reproduces the claimed formula.
- The Code Review Rules ("Exactness and controls") void a verdict whose control "merely reproduces
  the claimed formula".
- The control P0 lacked (P0:387–388) was C3 exercised with several measurement ticks when labels
  remain at `T`. No instance under R1s has that.

**Fix.**
- C3:222–224: state that the R1s multi-tick control is vacuous by construction (`Lab(T) = ∅`).
- Drop "(LF) holds non-trivially" and the §7 claim that W1 is the control P0 lacked.
- If a non-vacuous control for the (B) branch is wanted, use R1s with `T = t_p + 1`, where labels do
  remain at `T` (Instance II already is one), or record that no non-vacuous control exists for R1s
  with `T ≥ t_p + 2`.

### 4. Moderate: R2(i) in `d = 3` is decided for W1's embedding, and the carrier question belongs to the owner

**Where.** C3:61–64, C3:295–300 (N5.2), C3:339 (N7 R2(i) row), C3:349 ("no dynamical gap left under R1
or R2(i)"), C3:432–433 (§8 Q3), N:26–29, N:111.

**Evidence.**
- *The given embedding is classical under R2(i).* With `V` unchanged (chain cells only), `x_3(1)`
  reads the four transverse `x(0)` cells, which are not in `V`, so `x_3(1) ∉ Lab(1)`. The `x` labels
  in `Lab(1)` are then none, and `Lab(2) = ∅`. So `y_3(2) = a` is label-free, the `(a, b)` indicator
  is a function of label-free `V(2)`, and C3 holds. The case is decided negatively, not "not settled"
  (C3:299–300).
- *An enlarged observer may restore it, at `q = 2` only.* This is a reviewer hand check and
  unverified. Add the four transverse `x` cells of site 3 to `V`; they are 0 at ticks 0 and 1. Then
  `x_3(1) ∈ Lab(1)` and `y_3(2) ∈ Lab(2)`. But each added cell holds `2a` at tick 2 and is label-free,
  since its input `x_{(2,1,0)}(1) = a` is not a label. So `a` is exposed unless `2 ≡ 0 (mod q)`. At
  `q = 2`, every other line of N4 appears to go through.
- *Carrier.* R-lin is "the nearest-neighbour sum on the simple cubic lattice" (P:85–86), and ledger
  (x) names the simple-cubic graph (Main:724). P0's instances use rings. Only N:26–29 records the
  difference, and §8 does not ask the owner about it.
- *Effect on the verdict.* If the class carrier is the cubic lattice, R2(i)'s (A) is not yet an
  in-class result for general `q`. The class verdict does not change, because R1v gives (A) in
  `d = 3` (finding 1(b)) and R1s gives (B).

**Fix.**
- N5.2: replace "the `d = 3` case is not settled here" with the statements above, marking the `q = 2`
  enlargement as unverified.
- N7 R2(i) row: "(A) in `d = 1`; W1's `d = 3` embedding classical; `d = 3` open beyond the `q = 2`
  sketch".
- C3:349: delete "with no dynamical gap left under R1 or R2(i)", or restrict it to `d = 1` and use
  time `t_p`.
- §8: add an owner question on the carrier (rings of any `d`, or the simple cubic lattice only),
  citing P:85–86, Main:724 (x) and P0:392, :402.

### 5. Moderate: the NEW classifications have prior art in the sources the record cites

**Where.** C3:410–414 (§7), C3:416–420 (AW-C3-1).

**Evidence.**
- *First NEW item.* "C-PM is undefined after the use time when records are held in `V`" is
  SYNTHESIS-r3 MM-2 item 3 (SY:201–202: "which held cells are preparation labels and which are effects
  under C-PM"). The record cites it itself at C3:121 and C3:357. P0 N8.3 also has it (P0:353–355:
  "Instance II's nontriviality depends on cell-based delimitation"), and so does P0N:36–38. What is
  new is the instance that splits by reading (W1) and the fact that the split arises inside R-lin.
- *Second NEW item.* The structural content that does survive is OA-1's: "Under R-lin no cell is
  inert" (OA1:399), and the own-previous-slot term is not removed by isolation (OA1:339–340). The
  multi-tick part is false on the support (finding 1).
- *AW-C3-1.* This restates AW-P0-2 (P0:488–492) and SY T5 with per-reading entries. It is an
  elaboration of AW-P0-2, not a new marker.

**Fix.**
- First item: rewrite as "NEW: inside R-lin, one in-class instance (W1) is classical under some
  precedent-consistent delimitations (R1s, R2(ii)) and a gbit under others (R1v, R2(i), R2(iii)). The
  unfixed delimitation itself is SY MM-2 item 3 and P0 N8.3."
- Second item: withdraw it, or narrow it per finding 1 and classify it ELABORATING of OA1:335–349, :399.
- AW-C3-1: retitle as "ELABORATING AW-P0-2", and update its R1 clause to R1s (finding 1).

### 6. Minor: C-PM is quoted without its definition of label cells

**Where.** C3:85–87, C3:117–121.

**Evidence.**
- OA2:111–117 continues: "These are the setting and coin cells that select which preparation ran"
  and "the label is a property of the procedure, not of the system it prepared". It adds the physical
  form C-PM′: "the preparation gadget moves its label cells out of reach" (OA2:119–120).
- The record omits both. Both bear on the delimitation question.
- *Reviewer's check of whether these clauses force a reading.* They do not. R3 is their literal
  functional form: a cell is a label iff its content depends only on the procedure. R3 fails N8.2(b),
  because after a point preparation the prepared system's own cells (`s0(4) = x`) are functions of the
  herald alone. Separating "record of the procedure" from "evolved prepared configuration" by cell
  provenance is exactly what the precedents leave open (finding 1). So the omission does not change
  the verdict, but the quotation is incomplete.

**Fix.**
- C3:85–87: quote the two sentences of OA2:111–117 and the C-PM′ clause.
- §1.6: add one sentence saying that the "property of the procedure" clause, read functionally, is
  R3 and fails N8.2(b), so it does not fix the delimitation.

### 7. Minor: OA-2 Claim 2 is stated for `𝔊_K`; W1 uses its argument

**Where.** C3:276–279, C3:398.

**Evidence.**
- Claim 2 reads "No preparation-noncontextual ontological model reproduces `𝔊_K`" (OA2:443–444).
  Its step 3 is specific to `𝔊_K` (OA2:449–456).
- Steps 1, 2 and 4 are generic. P0 R7 abstracts them as "four point preparations with pairwise
  disjoint supports and `½(μ₀₀+μ₁₁) = ½(μ₀₁+μ₁₀)` are incompatible" (P0:182–183).
- For W1 the reviewer checked the inputs: `X = x_1(1) − y_0(1)` and `Y = y_8(2) − y_10(2)` are sharp
  and label-free. The four supports are therefore pairwise disjoint. Every accessible statistic is a
  function of the `a`-marginal or of the `b`-marginal alone, which gives the equivalence. In
  `f(a) + g(b)` form, the `(a, b)` indicator would need `f(0)+g(0) + f(1)+g(1) = 1` and
  `f(0)+g(1) + f(1)+g(0) = 0` at once, which is impossible.
- The conclusion holds. But Claim 2 is not applicable "exactly as stated", and W1's equivalence holds
  only under the reading's label convention. Claim 2's holds with the labels physically out of reach
  (C-PM′) for `p`, `ℓ` and the bath coin (OA2:449–450).

**Fix.**
- C3:278: "The argument of OA-2 Claim 2, steps 1, 2 and 4 (OA2:446–448, :457–458), as abstracted in P0
  R7 (P0:182–183), with step 3 supplied by N4's equivalence under the reading named."
- §6 row (C3:398): "[P] via the argument of OA-2 Claim 2 [R] and P0 R7 [R-off]".

### 8. Minor: R3 is not P0N's "functional variant", and its count of failed precedents depends on the treatment of settings

**Where.** C3:139–141, C3:145–148, C3:341, N:30–34.

**Evidence.**
- P0N:36–38 says: "(LF) is cell-based. Its functional variant (label-free as functionals) was not
  pursued." That variant concerns effects as functionals, for example `z₁ − c₀ = w` revealing the
  herald. R3 is a per-cell label rule. The two are related but not the same.
- R3 includes "setting values" (C3:140). Instance II's `c` is a measurement setting, not one of the
  preparation's labels (P0:403, :410). If R3 counts only the preparation's own settings, `x₁(1) = w + c`
  is not a function of the herald alone, and R3 passes Instance II. It then fails one precedent, not
  two.
- R3 is excluded either way, because it fails N8.2(b).

**Fix.**
- C3:141: replace "This is the 'functional variant' recorded as not pursued at P0N:36–38" with "a
  per-cell counterpart of the functional variant noted at P0N:36–38".
- C3:145–148: state that R3 fails N8.2(b) under either treatment of settings, and fails Instance II
  only if measurement settings count.

### 9. Minor: pins behind the instructed head; an owner decision cited unquoted

**Where.** C3:32–36 and C3:444–448 (pins at `2a9f10ba`; R8), C3:452, N:12.

**Evidence.**
- The source head for this unit is `3a3aa146`, with `REC-1-r9.md` (blob `945b7982`).
- r9 differs from r8 only in its revision line, P5 and §6 provenance rows. r9's P5 records this
  unit's authorization: "the C3 check of the R-lin update with (xiii) by #1169 c.6863414487".
- The cited passages are unchanged in r9, shifted by +4 lines: R8:255–268 → r9:259–272;
  R8:297–303 → r9:301–307; R8:313–316 → r9:317–320.
- The P0, P0C, P0R and P0N blobs are identical at both heads.
- The L reading, which the record relies on for the class definition (C3:72–73), rests on #1268
  c.6860582570, which the record lists as "not fetched" (C3:452). It is fetchable: `amaybaum`,
  2026-11-13T17:47:34Z, "**Adopt L; write r8 fix (Recommended)** … The **literal L reading** of the
  preregistered r7 class is kept. That reading is '(H4) or (V-ii-H)' with held-at-use typing."
- §A.42 item 7 asks for an owner decision a record relies on to be quoted with its author and time.

**Fix.**
- Re-pin P0, P0C, P0R, P0N and R9 at `3a3aa146`, cite `REC-1-r9.md` with the shifted lines, and note
  that the P0 blobs are unchanged.
- In §9, quote c.6860582570 with author and time, and reclassify the row "governance provenance,
  quoted".
- Update N:12.

### 10. Minor: the decision rule is sound, but its standing and scope need stating

**Where.** C3:154–174, C3:115.

**Evidence.**
- *Agreement across readings.* Requiring agreement is legitimate. C-PM is frozen and does not fix
  the delimitation, and adopting a reading would be a rule change (#1169 c.6863414487). A
  reading-independent class verdict therefore needs agreement. The rule does not force (C):
  (B) would follow if every admissible reading gave (LF).
- *What can go wrong.* With a writer-chosen set, the rule can return a spurious (A) or (B) when the
  set is too narrow. It cannot return a spurious (C) when the readings that disagree are admissible.
  The record's (C) is of the second kind, and finding 1 strengthens it. But the record does not say
  that the set is incomplete (N:112) and that (C) is robust to enlarging it.
- *Preregistration.* "Fixed after §1 and before §3" is ordering inside a single-commit file, so it
  cannot be checked from history.
- *Strength of (B).* (B) requires (LF), which is stronger than the obligation's "cannot happen", i.e.
  no label-cell-only retention together with lost common effects. An instance where (LF) fails but C3
  holds gives (C), not (B). This is acceptable, but it is unstated.

**Fix.**
- §2: add three sentences.
  - The reading set is not exhaustive. A class-level (A) or (B) would need every admissible reading,
    and (C) is unchanged by adding readings once two admissible readings disagree.
  - The ordering is within one commit and carries no separate preregistration weight.
  - (B) is sufficient for, not equivalent to, the obligation's "cannot happen".

### 11. Nit: §1.5's form of (LF) failure differs from P0's (LF)

**Where.** C3:110–111.

**Evidence.**
- P0's (LF) covers every measurement-stage read at ticks in `(t_p, T]` (P0:259–260).
- §1.5 restricts to C-PM-accessible reads at `τ₁ ∈ (t_p, T)`. That excludes reads that are labels at
  their own tick, and reads at `T`. W1 fails both forms.
- The sentence "This is the failure of (LF)" is not exact.

**Fix.** Replace it with: "This is the failure of (LF) for the accessible reads. P0's (LF), which
covers every measurement-stage read, fails whenever this does."

### 12. Register: no action

- No meta-commentary, reader instruction, caps emphasis outside identifiers, or revision-history
  voice was found in either file.
- No local path strings.
- `voice_check` (manuscript scope) is OK.
- NOTES:19 says the optional checkers were not run. They are OK at this head (header above);
  the record may say so.

***

## Verified as correct (no action)

- **W1 cell table** (C3:239–249). Every entry at ticks 0, 1 and 2 was recomputed from
  `y_i(1) = X_i`, `x_i(1) = X_{i−1} + X_{i+1} − Y_i` and
  `x_i(2) = X_{i−2} + X_i + X_{i+2} − Y_{i−1} − Y_{i+1}`. Reads stay in sites −2…12 mod 16, with no
  free cell at 14 or 15.
- **W1 hypotheses.**
  - `D_0`: five free cells, the rest designated 0.
  - H-AR at slot level, as in P0's instances.
  - (H3), and H-xiv (no setting).
  - The herald on `V(0)` is held at `t_p = 0` and at ticks 1 and 2.
  - Full retention at every pair of ticks: `V(2) → (a, n, p, m, b)` and `V(1) → (a, b)`.
- **R2(i) label sets** (C3:258–260), and **R2(ii) and R3 on W1** (C3:288–291).
- **W1 effects and C3 failure under R2(i).**
  - `X` is sharp at tick 1 and `Y` at tick 2.
  - `(n+a, a−p)` is uniform for each `a`.
  - Composites depend on `b` only.
  - `S*` is the only `S` meeting C1–C2: a finer `S` is unreachable and a coarser `S` breaks C1 on
    `[ab]`.
  - The joint indicator is not of the form `f(a) + g(b)`.
- **Precedent filter** (C3:145–150). R1(s), R2(i) and R2(ii) reproduce Instance I, Instance II and
  N8.2(b) (P0R:141–144). R0 fails N8.2(b) at ticks 4 and 5 and removes all of `V` for `J*`. R3 fails
  N8.2(b).
- **N1 structural claim and the N2 recursion**, for use time `t_p` under R1s.
- **W2 entries spot-checked** (sites −1, 5, 11 and 15 at tick 3) and W2's retention.
- **§5 C4.**
  - (⇐) on the preparation side holds for every instance: equal coset weights give equal record laws.
  - (⇒) on the preparation side needs C3.
  - Both directions on the measurement side hold from C1–C2.
  - P0 stays O-U, and both bearings are conditional and unadopted.
- **§9 classifications.**
  - Support off `main` for P0, P0R, P0N and R8: correct.
  - Provenance for SY and review 5892912758: correct for the steps. SY is still prior art for §7
    (finding 5).

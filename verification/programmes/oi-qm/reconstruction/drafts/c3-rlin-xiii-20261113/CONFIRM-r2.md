# Focused confirmation (r2) of C3-RLIN-r2, NOTES-r2 and RESPONSE-r1

**Verdict: ACCEPT WITH CHANGES.** All eleven findings of REVIEW-r1 are resolved as RESPONSE-r1
states. I checked W2′ by hand: its cell table, its class hypotheses and its verdict under each
reading, and all are correct. The writer is right about `Lab(1)`, and my REVIEW-r1 set was wrong on
two cells, `y_1` and `y_4`; neither is in `V`. The R2(i) `d = 3`, `q = 2` enlargement holds by hand.
The class verdict (C) is correctly derived. Four minor changes remain (C1–C4 below). None of them
alters a verdict.

**Target.** Branch `research/c3-rlin-xiii-1169-20261113`, fetched by name with no depth. `git log -1`
gives `ee4db4f1c30615c6e7e2b9942541c6b43121f00c`, whose single parent is `a03af682`. `a03af682`
adds only `REVIEW-r1.md`, byte-identical to the reviewer's file. `ee4db4f1` adds only `C3-RLIN-r2.md`,
`NOTES-r2.md` and `RESPONSE-r1.md`. The r1 files are unchanged.

**Checks run at `ee4db4f1`.** `claims_check`, `staleness_check`, `voice_check` and
`artifact_placement_check` all returned OK. `legacy_records_check ee4db4f1…` reports 303 records
intact. No local path strings appear in the three new files. All arithmetic was done by hand.

***

## 1. Findings resolved as RESPONSE-r1 states

| Finding | r2 location checked | Resolved |
|---|---|---|
| 1(a) | N1 r2:227–241 separates the structural claim from the on-the-support statement, citing W1 `y_3(2) = x_2(0)` and the cone formula | yes |
| 1(b) | "Fixed constant" r2:149–151; R1v r2:157–160; precedent rows r2:175–183; W1 label sets r2:314–322; `d = 3` r2:364–368 | yes |
| 1(c) | R2(iii) r2:164–165; r2:357–360 replaces the "two constant cells" sentence | yes |
| 1(d) | R1→R1s throughout; N7 rows r2:423–428; §7 structural item narrowed r2:508–509 | yes |
| 1(e) | §5 R1s bearing r2:472 | yes, with C3 below |
| 2 | N2 claim r2:245–246; use-at-read paragraph r2:255–258; verdict r2:264; N7, §4, §5, §6 carry use time `t_p`; Q6 r2:539–540 | yes |
| 3 | N3.3 r2:275–279; "non-trivially" and "the control P0 lacked" removed (§7 r2:505–515 has neither) | yes, with C2 below |
| 4 | Carrier r2:69–73; R2(i) `d = 3` r2:370–376; N7 r2:425; §4 heading r2:436 without the deleted clause; Q5 r2:535–538 | yes |
| 5 | §7 r2:505–515: the NEW item narrowed to W1's split, with SY MM-2 item 3, P0 N8.3 and P0N:36–38 credited; ELABORATING of OA1:335–349, :399; AW marker retitled | yes |
| 6 | C-PM quoted r2:96–102. The citation OA2:112–120 is correct; my REVIEW-r1 numbering (OA2:111–117, :119–120) was off by one. §1.6 r2:185–187 | yes |
| 7 | r2:335–345, :493 | yes |
| 8 | r2:167–169, :182 | yes |
| 9 | Pins r2:37–48; R9 lines r2:77, :82, :475 checked against `REC-1-r9.md` at `3a3aa146` (R9:259 *Statement*, :301 the L reading, :317 the ordering rule); c.6860582570 quoted r2:82–84, :557 | yes |
| 10 | r2:213–221 | yes |
| 11 | r2:125–127, verbatim | yes |

## 2. W2′ checked by hand

**Construction.**
- Ring `ℤ/24`, `T = 3`, `t_p = 0`.
- Free cells: `X_0 = n`, `X_2 = a`, `X_10 = b`, `X_12 = r`, `X_14 = m`; every `Y` is 0.
- `V` is sites `{−1, 1, 2, 5, 8, 10, 11, 15}`, both slots.
- The radius-3 cones `[−3,3]`, `[−1,5]`, `[7,13]`, `[9,15]`, `[11,17]` do not wrap onto each other
  mod 24.

**Cell table (NOTES-r2:141–150).** I recomputed every `(y, x)` entry at ticks 0–3 from
`x_i(t) = Σ_j X_j [|i−j| ≤ t, |i−j| ≡ t mod 2]` (linear superposition of the single-source
solution, NOTES-r2:34–36) and `y_i(t) = x_i(t−1)`. All 32 entries agree.

**Labels under R1v.**
- `x_9(1)` has one non-fixed input, `x_10(0) ∈ Lab(0)`, so it is a label.
- `x_8(2) = x_7(1) + x_9(1) − y_8(1)`. Here `x_7(1)` and `y_8(1)` are fixed zeros, so `x_8(2)` is a
  label.
- The chain `x_2(0) → x_3(1) → x_4(2) → x_5(3)` has one non-fixed input at each step. `x_5(1)`,
  `y_4(1)`, `x_6(2)` and `y_5(2)` are fixed zeros. So `x_5(3)` is a label.
- `y_8(3)` is a copy of `x_8(2)`, so it is a label.
- `x_10(2) = b + r` reads `x_11(1) = b + r`, which is not a label, so `x_10(2)` is label-free.

**Label-free content.**
- Tick 1: `(n, n+a, b+r, m)`.
- Tick 2: `(n, n+a, n+a, b+r, b+r, m)`.
- Tick 3: `(n+a, n+a, n+a, b+r, b+r+m, r+m)`.
- These match r2:383–384.

**What the effects give.**
- Ticks 1–2 give `X = a` and leave `b` masked by `r`.
- Tick 3 gives `m = (b+r+m) − (b+r)`, then `r`, then `b`. `a` appears only inside `n+a`.
- A composite whose event is at tick 1 or 2 and whose read is at tick 3 depends on `a` only through
  `n+a`.
- A composite whose event is at tick 1 and whose read is at tick 2 depends on `b` only through `b+r`.
- So every accessible statistic has the form `f(a)` or `g(b)`.
- The equivalence `½([00]+[11]) ∼ ½([01]+[10])` holds, and `X` and `Y` are sharp. The argument of
  Claim 2 applies.

**Class hypotheses.**
- `D_0`: the five free cells, everything else designated 0.
- H-AR at site level.
- (H3), and H-xiv (there are no settings).
- The herald on `V(0)` fixes `(a, b)` and is held at `t_p = 0`.
- Full retention at every tick:
  - `V(3)` gives `a = x_5`, `b = y_8`, `r = y_10 − b`, `m = x_15 − r` and `n = x_{−1} − a`.
  - `V(2)` gives `n = y_{−1}`, `a = y_1 − n`, `b = x_8`, `r = x_10 − b` and `m = y_15`.
  - `V(1)` gives `n`, `a`, `b = y_10`, `r = x_11 − b` and `m`.
- Label-cell-only retention: `x_{−1}(1) = n` is a function of `V(3)` (through `x_{−1}(3) − x_5(3)`)
  and is not a function of the label-free part of `V(3)`.
- C3 fails: `S*` is the span of the `n`, `r` and `m` directions, and the `(a, b)` indicator is not of
  the form `f(a) + g(b)`.

**Verdict under each reading.**
- *R2(iii).* Same labels in `V` as R1v.
- *R3.* The cells whose content depends only on the herald are `y_2(1)`, `y_10(1)`, `x_8(2)`,
  `x_5(3)` and `y_8(3)`. These are the same labels.
- *R1s.* `Lab(2) = ∅`, so `x_8(2) = b` is label-free at tick 2 together with `a`: classical.
- *R2(i).* `Lab(0) = V(0)`. No `x` cell has `x_{i−1}`, `x_{i+1}` and `y_i` all in `V`, so the `x`
  labels at tick 1 are none and `Lab(2) = ∅`: classical.
- *R2(ii).* `Lab(1) = {y_2, y_10}` and `Lab(2) = ∅`: classical.
- *The writer's claim about r1's W2.* Without `r`, `x_10(2) = b` has three non-fixed inputs, so
  under R1v it is label-free and the fragment is classical. Confirmed. REVIEW-r1 missed this.

## 3. The `Lab(1)` detail

The writer is right. Under the definition I wrote in REVIEW-r1 (drop fixed-constant inputs, then
require exactly one remaining input), `y_1(1) ← x_1(0)` and `y_4(1) ← x_4(0)` have no remaining input,
because `x_1(0)` and `x_4(0)` are designated 0 and are neither labels nor settings. So they are not
labels. REVIEW-r1's set `{y_1, y_2, y_4, y_7, x_3, x_6}` was wrong on these two cells. Neither is in
`V` and both hold 0, so nothing downstream changes. R1v's `Lab(1) = {y_2, y_7, x_3, x_6}`
(r2:315; NOTES-r2:83–90) is correct.

## 4. The R2(i) `d = 3`, `q = 2` enlargement (r2:372–376; NOTES-r2:115–123)

I re-derived it on `(ℤ/16) × (ℤ/s)²` with `s ≥ 3` and `V′ = V ∪` the four transverse `x` cells of
site 3.

**Values.**
- The added cells are 0 at tick 1: every neighbour of `(3,1,0)` holds 0 at tick 0, and `x_3(0) = 0`.
- At tick 2 each added cell holds `x_{(2,1,0)}(1) + x_3(1) = a + a = 2a`. The other neighbours and
  `y(1)` are 0.

**Labels under R2(i).**
- `Lab(0) = V′(0)`.
- `x_3(1)` reads `x_2`, `x_4`, `y_3` and its four transverse cells, all of which are in `V′`, so
  `x_3(1) ∈ Lab(1)`.
- No other `x` cell has all its inputs in `V′`. In particular `x_{(2,1,0)}(1)` reads `(1,1,0)`,
  which is not in `V′`.
- `Lab(1) ∩ V′ = {y_7}`.
- `Lab(2) ∩ V′ = {y_3}`. Each added cell reads `x_{(2,1,0)}(1)`, which is not a label, and `x_2(2)`,
  `x_4(2)` and `x_7(2)` each read a non-label.

**At `q = 2`.**
- `x_2(2) = n + 5a = n + a` and `x_7(2) = 5b + m = b + m`, and the added cells hold 0.
- So the label-free content at tick 2 is the same as in `d = 1`, and the herald and retention are
  unchanged.
- It is a gbit, and "[A, P], other `q` open" is correct.

**Nit.** NOTES-r2:183 lists only "odd `q`" as not done, while r2:376 says "other `q` open". The
latter is correct, since at `q = 4` the cell `2a` separates `a = 0` from `a = 1`. Align
NOTES-r2:183 with it.

## 5. Outcome clauses compared with r1

- The per-reading outcome clauses (A), (B) and (C) are byte-identical. `cmp` of r1:158–167 against
  r2:195–204 shows no difference; the range includes the first line of the class-level clause.
- Three parts of §2 did change:
  - **The class-level clause.** r1:168 enumerated the readings as "(R1, R2(i), R2(ii))", and r2:205
    deletes the enumeration and leaves the criterion "every precedent-consistent reading". The rule
    is unchanged in substance. But this is an edit to the aggregation clause, and RESPONSE's delta
    row "168–174 → 205–221" describes it only as "control clause; Standing" (C1).
  - **"For each reading R"** (r1:156 → r2:193). The enumeration is dropped here too.
  - **The control clause** (r1:172 → r2:209). "(LF) holds non-trivially" becomes "(LF) is not
    satisfied by construction". This is the change finding 3 asked for, and the delta table records
    it.
- None of these three changes alters a verdict. The heading's "outcome clauses as in r1" (r2:191) is
  true of (A), (B) and (C).

## 6. Overclaim check of the r2 verdict text

- §4 (r2:436–450), N7 (r2:423–430), §6 and §7 match the nodes.
- (C) is derived from the R1s/R1v split, and both readings appear in the precedent table. The heading
  overclaim of REVIEW-r1 finding 4 is gone.
- Three minor residues:

**C2 (minor): R1s's (B) has no §2 control.** §2's control clause requires, for a (B) branch, a
multi-tick instance "in which (LF) is not satisfied by construction" (r2:208–209). N3.3 (r2:275–279)
states that none exists for R1s. §4 bullet 1 (r2:438–440) and N7's R1s row (r2:423) still state (B)
without that qualification. The proof N2 stands on its own, but the rule's own control is unmet.
*Fix:* add to r2:264, N7 row R1s and §4 bullet 1: "(the §2 control cannot be met under R1s, N3.3; the
verdict rests on the proof N2 alone)".

**C3 (minor): the R1s bearing omits the rule-class condition.** r2:472–475 says that if the owner fixes
R1s with use time `t_p`, "P0's pass condition … is met … and the ordering rule … hands Q4 to
AW-OA2-1". Owner question 4 (r2:532–534) states that under R1s the N8.2(b) conveyor is an affine
gbit. So the pass also needs the owner to confirm the R-lin reading of the class. In the same
bullet, "the carrier question (owner question 5) leaves R1s's result unchanged" is a fact (N2 does
not depend on the dimension), but it is written into the list of conditions.
*Fix:* rewrite as "if the owner fixes R1s with use time `t_p` and confirms the R-lin reading of the
class (owner question 4), and the result survives independent review, … (N2 holds for every carrier
of §1.1, so owner question 5 does not affect it)".

**C4 (nit): W2′ is a `d = 1` instance.** r2:443 ("and at site level (W2′)"), N7 rows R1v and R2(iii)
(r2:424, :427) and Q5 (r2:536–538) do not say that W2′ is in `d = 1`. NOTES-r2:185 lists "W2′ in
`d = 3`" as not done.
*Fix:* "at site level in `d = 1` (W2′)" at r2:443 and :424, :427, and add W2′'s `d = 1` scope to Q5.

## 7. Nothing changed outside the delta table

- `diff C3-RLIN-r1.md C3-RLIN-r2.md` has 56 hunks. Each hunk's r1 range lies inside a row of
  RESPONSE-r1's delta table (RESPONSE-r1:66–93).
- The one hunk that crosses a row boundary is `191,192c243` (r1 N1 verdict → r2 N2 heading). It is
  an alignment artefact of `diff`; both sides belong to the N1/N2 rows.
- No r1 line outside the table changed.
- The table's descriptions are accurate except for row 168–174, which does not mention the
  class-level clause edit (C1).

**C1 (nit).** *Fix:*
- In RESPONSE-r1's delta row "168–174", add "class-level clause: the enumerated list
  '(R1, R2(i), R2(ii))' replaced by its criterion (finding 10)".
- In row "154, 156", say "reading enumeration dropped".
- Optionally, extend r2:191's heading note to "outcome clauses (A)–(C) as in r1; reading
  enumerations replaced by the criterion".

# RESPONSE to the independent review of C3-RLIN-r1

**Object.** `REVIEW-r1.md` (verdict REVISE) at `a03af682`, branch
`research/c3-rlin-xiii-1169-20261113`, reviewing r1 at `00c84af2`. The review was fetched by branch
name; it is identical to the working copy (`diff` empty). r1 (`C3-RLIN-r1.md`, `NOTES-r1.md`) is left
unchanged. r2 is `C3-RLIN-r2.md` (cited `r2:n`) and `NOTES-r2.md` (cited `N2:n` by section).

**Standing.** WIP / UNVERIFIED. Paper-only. No premise adopted, no rule changed, nothing committed,
pushed or posted.

**Outcome.** Every finding is applied. One point of detail is noted against finding 1(b) (the
reviewer's `Lab(1)` contains two zero cells that have no non-fixed input under the definition as
written); it changes nothing. Finding 4's `q = 2` enlargement, marked "unverified" by the reviewer,
was checked by hand and is stated as verified. The decision rule's outcome clauses are unchanged.
The reading set of r1 was incomplete (R1v and R2(iii) were missing); r2 says so (r2:214–217) and
applies the rule as it stands. The class-level verdict stays (C), now on the R1s/R1v split as well
as the R1s/R2(i) split.

***

## Dispositions

| Finding | Disposition | r2 location |
|---|---|---|
| **1(a)** R1 is structural; on the support W1 has `y_3(2) = x_3(1) = a` | Accepted. N1 now separates the structural claim from the on-the-support statement and cites W1 and the cone formula | r2:227–241 (N1); N2 §1 |
| **1(b)** add R1v; precedent checks; W1 `d = 1, 3` | Accepted after re-derivation by hand. Definition r2:157–160 ("fixed constant" defined at r2:147–152); precedent rows r2:178; W1 label sets r2:314–322; `d = 3` r2:361–369. Hand checks: N2 §2 (Instance I, Instance II, N8.2(b)), §3 (W1 `d = 1` and `d = 3`). Point of detail: the reviewer's `Lab(1) = {y_1, y_2, y_4, y_7, x_3, x_6}` includes `y_1`, `y_4`, whose only input `x_1(0)`, `x_4(0)` is fixed; under the definition as written they have no remaining input. Both hold 0, so the analysis is unchanged (N2 §3) | r2:147–160, :178, :314–322, :361–369 |
| **1(c)** add R2(iii); replace the "two constant cells" sentence | Accepted after re-derivation. Definition r2:164–165; precedent row r2:181; W1 r2:320–321; the sentence is replaced by the account of how each reading reaches the gbit | r2:164–165, :181, :320–321, :357–360 |
| **1(d)** consequences: R1→R1s throughout; N7 rows; §7 structural item | Accepted. R1 renamed R1s in N2, N3, N5, N7, §4, §5, §6, §7, §8. N7 has rows for R1v and R2(iii). The structural item is narrowed (finding 5) | r2:243–281, :419–432, :436–450, :488–501, :505–515 |
| **1(e)** R1 bearing in §5 | Accepted: "if the owner fixes R1s with use time `t_p`, the carrier question … leaves R1s's result unchanged, and the result survives independent review" | r2:472–476 |
| **1 fix, §4 gap** | Accepted: the gap is stated as the two open choices | r2:445–449 |
| **1 fix, §8 Q1** | Accepted: Q1 lists R1s, R1v, R2(i), R2(ii), R2(iii), R3 and the two sub-choices | r2:521–526 |
| **1 fix, N:68** | Accepted: R1v and R2(iii) label sets for every cell of `V` | N2 §3 |
| **1** additional | Site level: r1's W2 is classical under R1v (`x_10(2) = b` has three non-fixed inputs). W2′ adds site 8 and a mask `r`; it is a gbit under R1v, R2(iii) and R3, and classical under R1s, R2(i), R2(ii). Re-derived from the cone formula | r2:377–396; N2 §4 |
| **2** N2 needs use time `t_p` | Accepted. N2's claim names use time `t_p`; a paragraph states that with use at each effect's read R1s does not say which cells hold the herald and N2 is open; the verdict line, §4, §5, §6 row and N7 carry it; owner question 6 added | r2:243–246, :255–258, :264, :423, :438–440, :444, :472, :490, :539–540 |
| **3** (B)-branch control vacuous | Accepted. N3.3 states the control is vacuous by construction, that `T = t_p + 1` is also immediate, and that no non-vacuous several-tick control exists for R1s. "(LF) holds non-trivially" and "the control P0 lacked" are removed. The control clause of §2 reads "in which (LF) is not satisfied by construction" | r2:209, :275–281, :508–509 |
| **4** R2(i) in `d = 3`; carrier question; heading overclaim | Accepted. W1's `d = 3` embedding is classical under R2(i). The `q = 2` enlargement was checked by hand (transverse cell holds `2a`; at `q = 2` the label-free content equals the `d = 1` one) and is stated as verified, other `q` open. N7 row updated. §4 heading reads "(C) at the frozen scope." without the deleted clause. Owner question 5 (carrier) added; §1.1 notes the carrier is not fixed | r2:69–73, :370–376, :425, :436, :535–538; N2 §3 |
| **5** NEW items have prior art | Accepted. First item rewritten to the in-R-lin split of W1, crediting SY MM-2 item 3, P0 N8.3 and P0N:36–38. Second item narrowed to the structural statement and classified ELABORATING of OA1:335–349, :399. AW-C3-1 retitled ELABORATING AW-P0-2, with R1s | r2:505–515 |
| **6** C-PM quoted without its definition of label cells | Accepted: OA2:112–120 quoted, including "the setting and coin cells that select which preparation ran", the "property of the procedure" clause and C-PM′; §1.6 adds that the clause read functionally is R3 and does not fix the delimitation | r2:96–102, :143–146, :185–187 |
| **7** OA-2 Claim 2 applied by analogy | Accepted: "the argument of OA-2 Claim 2, steps 1, 2 and 4 (OA2:446–448, :457–458), as abstracted in P0 R7 (P0:182–183), with step 3 supplied by the equivalence above under the reading named"; Claim 2's own C-PM′ setting noted; the `f(a) + g(b)` impossibility added; §6 row updated | r2:333–345, :493 |
| **8** R3 is not P0N's variant; precedent count | Accepted: "a per-cell counterpart of the functional variant noted at P0N:36–38"; the precedent table shows R3 failing N8.2(b) under either treatment of settings and Instance II only if measurement settings count | r2:167–169, :182 |
| **9** repin to `3a3aa146`; quote c.6860582570 | Accepted. P0, P0C, P0R, P0N repinned (blobs unchanged); R9 (`945b7982`) replaces R8 with lines +4 (R9:259–272, :301–307, :317–320), checked by `diff` of r8 against r9; c.6860582570 fetched and quoted with author and time in §1.2 and §9 | r2:37–48, :77–84, :476, :548–557; N2 §0 |
| **10** standing and limits of the decision rule | Accepted: three sentences under "Standing and limits of the rule"; the first also states that r1's set was incomplete | r2:213–221 |
| **11** §1.5 (LF) wording | Accepted verbatim | r2:125–127 |
| **12** register | No action required. NOTES-r2 §0 cites the reviewer's checker results; they were not re-run here | N2 §0 |

***

## Re-derivation of the reviewer's new readings (not taken on the reviewer's word)

- **R1v, precedents.** Instance II: `y₀(1)` label; `x₁(1)` keeps `x₀` and the setting `c` (two inputs),
  label-free; `x₀(1)` keeps only `u`, label-free. Instance I: `x₀(1)` keeps `c`, `u`, `p`; `x₂(1)` keeps
  `c`, `u`; both label-free. N8.2(b): at tick 4 `r_1`, `r_2` labels, `s0(4)` and `r_0(4)` (with `s0(3) = 0`
  dropped, input `u`) label-free; at tick 5 `r_2`, `r_3` labels, `r_1`, `r_0`, `s0` label-free. All three
  reproduced (N2 §2).
- **R2(iii), precedents.** Same cell-by-cell outcomes; in Instance II `x₁(1)` reads the non-label `c`
  (N2 §2).
- **W1 under both.** `Lab(1) ∩ V = {y_7}`, `Lab(2) ∩ V = {y_3}` in `d = 1`; in `d = 3` the transverse inputs
  of `x_3(1)` are fixed, so the same; label-free tick-2 content `(n+5a, a−p, 5b+m, b+m, m)` (N2 §3).
- **Agreement with the reviewer.** All label sets agree on `V`. The only difference is the status of
  `y_1`, `y_4` at tick 1 (zero cells), noted above.

***

## r1 → r2 delta (`diff C3-RLIN-r1.md C3-RLIN-r2.md`)

| r1 lines | r2 lines | Change | Finding |
|---|---|---|---|
| 1 | 1–6 | title r2; revision paragraph | 1–11 |
| 32–40 | 37–48 | pins at `3a3aa146`, R9 replaces R8, RV row, blob note | 9 |
| 55–56, 61–64 | 63–64, 69–73 | ledger (x) named; carrier paragraph with owner question 5 | 4 |
| 68–76 | 77–87 | §1.2 cites R9 lines and quotes c.6860582570; owner question 4 cross-reference | 9 |
| 85–87 | 96–102 | C-PM quoted in full (OA2:112–120) | 6 |
| 111 | 126–127 | §1.5 (LF) wording | 11 |
| 120–122, 126 | 136–139, 143 | delimitation paragraph cites OA2:112–113, P0 N8.3, P0N | 5, 6 |
| 130–141 | 147–169 | two open choices; fixed constants defined; R1→R1s; R1v and R2(iii) added; R3 provenance | 1, 8 |
| 145–150 | 173–187 | precedent table for every reading; "property of the procedure" sentence | 1, 6, 8 |
| 154, 156 | 191, 193 | §2 heading notes unchanged outcome clauses; "precedent-consistent" unchanged | 10 |
| 168–174 | 205–221 | control clause; "Standing and limits of the rule" | 3, 10 |
| 180–192 | 227–241 | N1 restricted to the structural claim; on-the-support copies added | 1 |
| 194–210 | 243–264 | N2 renamed R1s, restricted to use time `t_p`; use-at-read paragraph; verdict line | 1, 2 |
| 214–231 | 268–287 | N3 renamed; N3.2 lists all readings; N3.3 vacuous control | 1, 3 |
| 258–265 | 314–327 | W1 label sets under R1v, R2(iii), R2(i), R3; effects "under any of these four" | 1 |
| 273–281 | 335–348 | `f(a)+g(b)` argument; Claim 2 cited by steps and via P0 R7; verdict line lists readings | 7, 1 |
| 286–300 | 353–376 | N5.1 split by reading; N5.2 `d = 3` under R1v, R2(iii), R3, R2(i) embedding and enlargement | 1, 4 |
| 302–314 | 378–399 | W2′ replaces W2; r1's W2 under R1v; verdict line | 1 |
| 317–318 | 402–403 | convention test sentence covers R1s, R1v | 1 |
| 338–341 | 423–428 | N7 rows R1s, R1v, R2(i), R2(iii), R3 | 1, 2, 4 |
| 349–360 | 436–450 | §4 verdict: heading clause removed; R1s with use time; R1v/R2(iii)/R2(i) bullet; two open choices; decisive node | 1, 2, 4 |
| 369–384 | 459–478 | §5 C4 (⇒) and P0 bearings requalified | 1, 2, 4 |
| 394–399 | 488–494 | §6 rows: structural and on-the-support N1; use time; Claim 2 via P0 R7 | 1, 2, 7 |
| 410–420 | 505–515 | §7 NEW rewritten; structural item ELABORATING; AW marker retitled | 5, 1 |
| 427–436 | 522–540 | owner questions 1, 3 updated; 5 (carrier) and 6 (use time) added | 1, 2, 4 |
| 444–452 | 548–557 | §9 repinned; RV row; c.6860582570 quoted | 9 |

`NOTES-r2.md` is a new file. It adds the R1v and R2(iii) precedent checks (§2), the full W1 label
sets and the `d = 3` enlargement check (§3), and W2′ (§4). It also records the r8→r9 comparison and
the c.6860582570 fetch (§0).

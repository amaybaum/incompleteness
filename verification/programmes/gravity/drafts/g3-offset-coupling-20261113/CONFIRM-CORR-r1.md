# CONFIRM-CORR-r1: check of the forward correction of unit 1 (G3-UNIT1-CORR-r1)

**Verdict: CONFIRMED, with three should-fix findings and one nit. Nothing is blocking.**

The record does what QU4 asks: a forward note that corrects unit 1 from unit 2(a) r3, with r5 unedited. Its 20 corrections cover every statement in G3-UNIT1-r5.md that unit 2(a) r3 changes. Each corrected statement matches U2Ar3, and the cited lines are accurate.

Recategorizing Part 2 as "conditional on Reading G of GR:346 and B_G (open)" is correct. In unit 2(a) r3, Reading G with B_G is the only reading on which GR:346 supplies the exclusion. (ii-L) is an added premise whose reach depends on the branch.

The three should-fix findings are:

- **K-1.** Three statements in NOTES-r5 that carry the label "GR:346's argument (ii-L)" are not covered.
- **K-2.** The phrase "(DZ) for the convention-fixed offset" on Reading G omits the §8.3 qualifier: with §8.3 in force, only the absolute part is excluded. U2Ar3:729 carries the same imprecision, and my CONFIRM-U2A-r2 missed it.
- **K-3.** "Part 1 unaffected" needs a scope note for (ii-G), whose bearing on K_cpl^free unit 2(a) does not examine.

**Target.** Branch `research/g3-offset-873-20261113` at `2c25b544399630023d4af0c3f908416f4e0a1345`, parent `1ad01923`.

- `git diff --stat 1ad01923 2c25b544` shows one new file, G3-UNIT1-CORR-r1.md (404 lines).
- G3-UNIT1-r5.md, NOTES-r5.md and CONFIRM-r4.md are unchanged (`git diff --quiet`).

Line references: "CORR:n" means G3-UNIT1-CORR-r1.md, "U1r5:n" means G3-UNIT1-r5.md and "U2Ar3:n" means G3-UNIT2A-r3.md. Corpus lines refer to `main` at `c3b5f37a`.

**Authority read.**

- #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU4: "unit 1 is corrected forward with a short note or r6 that points to unit 2(a). The record r5 itself is not edited."
- PR #1275 review 5898121925 (posted by `amaybaum`, 2026-11-13T21:12:40Z, commit `1ad01923`). Its "Bounded implications" requires that "(ii-L) as GR:346 argued" not be left as an unconditional source for (DZ).

**Checks at `2c25b544`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check 2c25b544…` | 303 records intact |

None of them scans the drafts.

***

## Brief items

### 1. Coverage

I grepped U1r5 for "ii-L", "as argued", "R0", "no entry point" and "(ii-W) applied … absolute emergent". Every hit whose content unit 2(a) r3 changes is covered:

| U1r5 lines | Correction |
|---|---|
| 48–57 (§0 Part 2) | X-1, X-2, X-3 |
| 71–74 (AW-loop in §0) | X-4 |
| 478–479 | X-5 |
| 484–486 | X-6 |
| 517, 520–522 | X-7 |
| 507–510, 525–527 | X-8 |
| 541 | X-9 |
| 565–568 | X-10 |
| 572–581 (R0) | X-11 |
| 630–641 (O0) | X-12 |
| 651–652 (O1) | X-13 |
| 663 (F1) | X-14 |
| 670 (F8) | X-16 |
| 689–694 (AW-loop in §6) | X-17 |

Elsewhere, CONFIRM-r4:92 is covered by X-15, and NOTES-r5:61, :82–84 and :85–87 by X-18 to X-20.

The other sources are covered as follows:

- **Unit 2(a) r3's §6 consequences 1–8 (U2Ar3:672–731):**
  - item 1 → X-1, X-2, X-5;
  - item 2 → X-5, X-6;
  - item 3 → CORR §3 (stands);
  - item 4 → CORR §3 (the fine-tuning statement stands);
  - item 5 → X-4, X-17;
  - item 6 → X-12;
  - item 7 → CORR §3;
  - item 8 → X-14, X-15.
- **U2Ar3 QU4 (:841–843):** "relabel (ii-L) as an added premise on Readings E and D, note Reading G, and scope B5's loop statement". All three are done.
- **The ChatGPT "Bounded implications":**
  - "on E/D it is added" → X-5;
  - "on G its exclusion needs B_G" → X-1;
  - "silent for Z_0 and depends on the §8.3 branch" → X-5, X-11;
  - "GR:400 Reading 1 and the configuration-differential source are not banned without the extra conditions" → X-3, X-11;
  - "no offset convention selected, no coupling across general metrics" → CORR §4.

Missed: three NOTES-r5 statements (K-1).

### 2. The corrected statements against U2Ar3, and the Part 2 recategorization

Each corrected statement matches what U2Ar3 establishes at its stated scope (de Sitter, M1).

**Part 2 (CORR:48–52; X-1).** The category "conditional on Reading G of GR:346 and B_G (open)" is correct:

- GR:346 does not exclude the witness on Readings E and D (U2Ar3:43–48, :675–677).
- On Reading G it excludes the witness if and only if B_G holds (U2Ar3:49–53, :678–679).
- (ii-L) is an added premise. It excludes a member only when ρ_Z varies with the configuration and §8.3 is not in force, and it is silent under Z_0 (U2Ar3:685–689).

CORR:50–52 keeps "conditional on (ii-L)" as accurate only in that branch, which is right. The record does not underclaim: other routes to exclusion are listed, namely (ii-S), P11 and GR:575, as posits or readings the corpus does not adjudicate (X-2, X-3; U2Ar3:682–683). It does not overclaim either: B_G is marked open everywhere, and its narrowing (G3; a view of laws the corpus does not state) is carried (X-1, X-12; U2Ar3:548–552). The one imprecision is the §8.3 qualifier on Reading G (K-2).

X-3's last bullet also correctly withdraws r5's "a reading no corpus text adopts" (U1r5:53–54). U2Ar3 §2.2 finds that the text supports Reading E, on which (ii) is (ii-W).

### 3. Citations

**Unit 1 and its records.** I checked these against the files:

- U1r5:43–57, :71–74, :226–230, :335–337, :356–359, :478–479, :484–486, :496–498, :505–527, :541, :562–568, :572–581, :630–641, :651–652, :663, :670, :689–695;
- NOTES-r5:61, :82–84, :85–87;
- CONFIRM-r4:92 and RESPONSE-r4:20.

Each quotation is exact, or elided with "…" without changing its sense.

**Unit 2(a) r3.** I checked:

- the definitions: :206–231, :253–262, :260, :264–287, :285–287, :315–331, :333–338, :388–390, :425–448, :459–477, :489;
- the verdict and narrowing: :495–515, :548–552, :648–656;
- the consequences: :670, :672–731;
- the findings: U2A-F1 to F6 at :741–746;
- the owner questions: :829–846.

They resolve to the content cited. I also read the owner record (c.6865179466) quoted in X-19 and X-20, and it is quoted correctly.

### 4. Items left unchanged

CORR §3 lists items that stand. They are unaffected, with the exception noted in K-3:

- **Part 1 and the K_cpl^free statements.** U2Ar3:726 says "Part 1 of unit 1 is unaffected", but see K-3.
- **The fine-tuning statement at U1r5:356–359.** U2Ar3:91–93 and :706–708 explicitly leave it unchanged.
- **(DZ)'s definition and K_cpl^conv's violation of it** (U1r5:226–230, :335–337). Unit 2(a) uses both unchanged.
- **The §8.3 reconciliation and the epoch caveat** (U1r5:496–506). They are now placed on Readings D and G (X-4, X-17), which is correct by U2Ar3:715–720.
- **B1–B4, R1–R3, F2–F7, F9, AW-prov, AW-abs and AW-G12.** None of these concerns requirement (ii) or the loop. I checked each against U1r5's text.

### 5. Register

The corrected statements are written in neutral voice. A grep for history-voice phrases (now, no longer, formerly, previously, "r5 said") finds nothing, and there are no barred strings. CORR:22–23 ("where a statement below differs from them, this record states the current position") is framing in a correction record, outside the corrected statements, and is acceptable.

***

## Should-fix

### K-1. Three NOTES-r5 statements with the "GR:346's argument (ii-L)" label are not covered

**Where.**

- NOTES-r5:43–44 (decision 1): "Part 2 is therefore 'conditional on (ii-L)', not 'counterexample'".
- NOTES-r5:47–49 (decision 3): "Whether (ii-L) holds against self-consistent fixed points is an open proof question".
- NOTES-r5:73–74 (Q4(a)): "whether GR:346's argument (ii-L) holds against self-consistent fixed points. This is the smallest proof question that remains for Part 2".

**Evidence.**

- Unit 2(a) answers Q4(a) on Readings E and D (U2Ar3:721–724). On Reading G the remaining question is B_G, not (ii-L).
- The owner selected unit 2(a) under Q4 (c.6863416405) and has authorized the B_G unit under QU5 (c.6865179466).
- Decisions 1 and 3 are log entries, but they carry the same label.

**Fix.** Add an X-21 or a line in CORR §1 or §3:

> "NOTES-r5:43–44, :47–49 and :73–74: Part 2's category is that of §1 of this record. On Readings E and D, GR:346's argument does not exclude a self-consistent fixed point (U2Ar3:721–724). The question that remains for Part 2 is B_G, which the owner authorized as the next unit (#873 c.6865179466, QU5). Q4 was answered by the selection of unit 2(a) (#873 c.6863416405)."

### K-2. On Reading G with §8.3 in force, "(DZ) for the convention-fixed offset" holds only for the absolute part

**Where.** X-14 (CORR:286–287): "on Reading G it settles (DZ) for the convention-fixed offset given B_G (open)". X-15 (CORR:297–298): the same. Also the Reading G bullet of X-1 (CORR:71–72) and row 2 of §1 (CORR:48).

**Evidence.** U2Ar3's §8.3 table (:469):

- (ii-G) with B_G excludes the witness through the absolute part ρ_Z(R₀) in both branches.
- With §8.3 in force, it admits Δρ_Z, the configuration-differential part.

(DZ) is "the source minus T^cl contains no dependence on e_Z([r])" (U1r5:226). A completion whose source carries only −Δρ_Z g violates (DZ), yet with §8.3 in force it is admitted on Reading G given B_G. So with §8.3 in force, Reading G with B_G settles (DZ) for the absolute part only.

Excluding "the convention-fixed coupling", meaning K_cpl^conv itself, is correct in both branches (X-1, X-2). The phrase "settles (DZ)" is not. X-2 and X-11 already state the qualifier correctly.

U2Ar3:729 ("On Reading G, GR:346 settles (DZ) for the convention-fixed offset given B_G") carries the same imprecision. My CONFIRM-U2A-r2 did not catch it.

**Fix.**

- In X-14, X-15, the X-1 Reading G bullet and §1 row 2, append: "with §8.3 in force, for the absolute part `ρ_Z(R₀)`; the configuration-differential part `Δρ_Z` is then admitted (U2Ar3:469)".
- Add one line to CORR §4 noting that U2Ar3:729 is read with this qualifier.

### K-3. "Part 1 unaffected" needs a scope note for (ii-G)

**Where.** CORR §1 row 1 (CORR:47) and §3 (CORR:380–382).

**Evidence.**

- Part 1 is stated on (ii-W), (ii-L) and (ii-S) (U1r5:43–45). Unit 2(a) introduces (ii-G).
- U2Ar3:543 (§4.5, Attempt 2) says: "Its bearing on K_cpl^free is not examined here."
- U2Ar3:726 confirms only that K_cpl^free survives (ii-W) and (ii-L).

So Part 1 is unaffected as stated, but its standing under the new reading is open.

**Fix.** In §1 row 1 and in §3, append:

> "Part 1 is stated on (ii-W), (ii-L) and (ii-S). Whether (ii-G) with B_G excludes K_cpl^free is not examined in unit 2(a) (U2Ar3:543)."

## Nit

### K-4. X-3's last bullet omits the (ii-L) branch

**Where.** X-3's last bullet (CORR:106–108). X-10 reuses it.

**Evidence.** The bullet says "The exclusion of K_cpl^conv therefore rests on (ii-S), P11 or GR:575 … or on GR:346 on Reading G given B_G." It leaves out (ii-L) as an added premise, which excludes a configuration-varying member when §8.3 is not in force (X-2, X-11).

**Fix.** Before the final sentence of that bullet, add: "or on (ii-L) as an added premise, for configuration-varying `ρ_Z` with §8.3 not in force".

***

## Disposition

CONFIRMED, with K-1 to K-3 (should-fix) and K-4 (nit). All four are textual, and no further review round is needed.

The record meets QU4 and the "Bounded implications" of review 5898121925. Once K-1 to K-4 are applied, it is ready to land with unit 2(a) on the owner's separate merge decision.

No manuscript change is proposed. No premise is adopted.

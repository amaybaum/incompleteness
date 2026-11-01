# RR-1 stage 1: independent review of the execution result

**Object.** `STAGE1-RESULT.md` (212 lines) against the frozen `preregistration.md` (PR) at `c41e0e6f`. I confirmed the blob with
`git rev-parse` in the rr1 worktree: `77a471ac4e590554e0f331557c87ad1253a1309d`. The assessment (AS) is at the same commit.
**Sources** (keys as in result §0): `d4a80fc8` (wt-substate1), `af1e9be2` (wt-f2-1), `papers/Main.md` at `5914c17c` (main checkout).
**Method.** Paper-only. Read commands only (`cat`/`sed`/`awk`/`grep`/`git show`/`git rev-parse`), plus a read-only look at PR #1025.
No Python, Lean, commit, push or comment.

## Verdict: **STAGE-VOID** (Finding 1, from the AMB-1 ruling)

The frozen rule does not fix AMB-1, so POS-1 stops at UNRESOLVED(G7) and S0 fails (PR:74–75); no candidate token stands.
*Diagnostic only, not a verdict:* POS-1's pass condition holds under **each** reading taken separately. The void therefore comes from
under-specification in the frozen text, not from a control that failed on substance. Findings 2–12 apply to an owner-authorized
successor or re-run.

## AMB-1 ruling (explicit)

**Frozen text.** PR:95–98: "(4) pins, one inventory item at a time (ready ball, compiled source, named exception, source-law payload) in source-table
  order, **each given π_0 on its cells**. With earlier removals kept, every h other than H-law stays removed iff G2–G5 still pass and
  P(ready) is unchanged; otherwise it is restored. An ablation not decidable on paper gives UNRESOLVED(G7:h)." PR:31–32: π_NY is "the pins (…), with independent-uniform values on every unpinned cell".

**The two readings.**
- **A, the executor's:** ablating X drops X from π_NY's pin list; a cell pinned by a retained item stays pinned. Supported by PR:31–32's
  construction and by "one inventory item at a time"; contradicted by the literal "each given π_0 on its cells".
- **B, override:** all of X's cells get π_0, overriding a retained item's pin on shared cells. Supported by the literal wording of PR:96;
  it strains "one item at a time", but steps are still indexed by single items.

**Ruling: (c), genuinely ambiguous.** Not (a): no frozen sentence determines A, and the literal clause leans toward B. (c) rather than a
clean (b): each reading rests on different words of the same text, and the text never reconciles them.

**Consequence.**
- The text gives the executor no licence to choose a reading (§7 "Rule fixed before assessment"; PR:93 "(fixed order)"). Its stop rules
  are PR:24–25, "Any step not decidable on paper ends in UNRESOLVED(that step)", and PR:98.
- "Ambiguity" is not in the text. I read "decidable on paper" as "decided by the frozen procedure applied to written sources", so a step
  whose operation the procedure leaves undefined is not decided. Evaluating both readings and reporting what they share is not provided
  for either, and would be a rule supplied after the freeze.
- **Where it bites:** the first item. The port-0 ball B_T((0,T,0)) lies inside B_{L+1}(q10), since P+78+T ≤ S+78 = L+1. Under A it is
  removed; under B its zeros on q10-ball cells go to π_0, P(ready) drops below 1, and it is restored.
- So POS-1 gives **UNRESOLVED(G7:port-0 ready ball)**. That meets PR:107's fail condition ("token is not RR-AVAILABLE …"), and PR:74–75
  then gives **STAGE-VOID**: "no candidate token is issued". The executor's own AMB-1 sentence (result:29–30) anticipates this.

**Diagnostic: Reading B checked.** Every inherited ball meeting E's constrained cells is restored, and at the q10-ball step
P(ready) = 8^{−n_E} ≤ 1/8, so the q10-ball pin is restored too. The f-test (step 2) does not depend on the reading. Hence
Λ ⊇ {H-law, q10-ball pin} and W-certified = no under B as well. NEG-1, CC-2(a) and CC-2(b) never reach G7 and are unaffected.

## Findings

1. **Blocker; result §1 AMB-1 and §2 POS-1 G7(4).** The ruling above. *Fix:* an owner-authorized successor preregistration or amendment
   that fixes the overlap rule (A or B) and the order (Finding 2); then re-run S0 and C1–C6.
2. **Medium; AMB-3.** "Source-table order" (PR:96) names no table. Under A, C5's retained pin is "the last covering ball in table order":
   with v15c:384–391 that is the q10 ball, with another order another of the 16 balls covering p5. *Fix:* freeze the order in the
   successor (v15c:384–391, then SG row order, then v15c:541–549, then E, N).
3. **Medium (§A.19); C3 G7(3).** The stop "UNRESOLVED(G7:H-access)" can be decided from the sources.
   - r13c:21–23 defines ROWS as all (x,u,mY,mR,a,b) × (Ecode,Ncode): 4096 rows, covering all 64 contexts, the 16 terminal ones
     included (NC1:87 [draft]).
   - r13c:238–242 asserts, on every row, `nxt[0,0,8] == (0, XM^UM, 0)` ('q8 preserved') at τ=8, i.e. R+8 = L−1. CI:38–40 calls these
     whole-triplet equalities checked constraints, and CI:84–88 puts q8's cone inside the prepared region.
   - So P(ready)=1 under π_NY. (b) holds on Ω under H-law, G2–G5 pass, P(ready) is unchanged, and **H-access is removed**.
   - Reviewer's sketch of step (4), for the executor to redo: the q10 ball is restored, because the free −z axial cell (0,S,−S) at
     distance L−1 gives P=1/4 (h9:116–122; K:61–63). Compiled-source rows that first reach q8 at L−1 (as O does) need a per-row audit.
     The likely result is UNRESOLVED(G7:compiled source).
4. **Medium; C2 G1/G3.** AMB-5's SG schema is undocumented. Its cited support is off-target: P3:103 is the 7,832-entry herald, and
   h10:42–45 is the W program. R_E = g(K) and the G3 parity bound rest on an unsourced reading. *Fix:* C2 stops at **UNRESOLVED(G1)**
   ("not writable from sources").
5. **Low; C4 G7(4).** The stop is genuine, but its stated reason is incomplete.
   - The post-ablation law *is* decidable: J blocks only +z, and the −z cell (0,S,−S) at distance L is free, so U_L(q9) is uniform and
     P(A=0)=1/2.
   - The undecidable part is the pre-ablation P(ready). s12:30–34 gives (0,s,r_old) only "for old masks 00,10,11"; the mask-01 rows are
     the branch_v10 `q9_table_hex` (r13c:525–531; result.json `q9_preserved_rows: 4096`); and the context masses are not stated.
   *Fix:* reword the stop accordingly.
6. **Low–medium; C3 G1.** t_r=L−1 with t_u=L violates t_u ≤ t_r (PR:38). *Fix:* t_r = t_u = L, with R_E on the previous slice. No token
   change.
7. **Low; POS-1/C1 G1/G3 and AMB-2.** G3 conditions on W_0 (stipulated port reads), yet step (3) is called vacuous. *Fix:* either use Ω
   throughout, or run step (3); in the second case readiness survives and G9 runs in full under its third trigger.
8. **Low; member choice for C3 (q8) and C5 (port 5, tick 0).** These are executor choices the frozen text does not fix. Tick 0 is the most
   favourable member, since there E is a coordinate of W_0. *Fix:* log the choice as an AMB and keep the token member-scoped.
9. **Low; tokens.** "Partial Λ" is not on PR:100–101's beside-list; label it non-token. UNRESOLVED(G7:h) should name the item (an SG
   row), not the class.
10. **Low; §6 command log.** `uniq -c` is a count. It entered no verdict, but PR §7 says read commands only.
11. **Low; anchor imprecisions.** v15c:32–33 defines only Q9 and Q10 (q8 is at AB:18 / CI:21; L at v15c:31 / IC:32). K:104–105 defines
    W_u generically (the eight ports come from v15:63–65). C5's bank exclusion argues only from its own port (other rays mismatch in
    coordinates, v15c:552–560). POS-1's R_E leaves previous-slice source positions free, but sources are current-slice only
    (v15c:609–610), so R_E slightly exceeds "its pinned values" (PR:107); harmless.
12. **Low; AMB-0.** PR #1025's body records the freeze: "owner chat, 2026-11-01 … 'freeze the reviewed RR-1 preregistration, then run its
    paper-only gates'"; the PR has no comments. *Fix:* quote that line with author and time (§A.42 item 7), and drop "not read".

## Check 2: G9 for C5, done independently (cures AMB-6 for C5)

**Pullback (definitional route, PR:54–56).** At t=0 the two-slice state is the original configuration, so the joint law of
(U_0(p5), W_0) depends exactly on the eight current-slice port cells (v15:63–65; v15c:377–380). Classifying p5=(0,S,0) under
v15c:563–575: not a named source (v15c:541–549); not SG (SG lies at ≥ L+1 from q10, r13c:258, while p5 is 78 from q10, and SG
coordinates have at most 4 digits); not BANK (own index t=0 ≤ S; every other ray mismatches in x, y or z); so **PINNED**, covered by 16
balls: ports 2, 3, 4 (2T, 2T, 5T ≤ S), port 5, (0,S,−68), the ten chain balls (68+k ≤ R+k), and q10. This **agrees** with both of the
executor's pullbacks.

**Adversarial note.** (a) After the q10-ball ablation, G2–G5 all still pass (P(ready)=1/8 > 0; P(ready | entry=000)=1), so readiness in §2's sense survives
  with no pin. The pin returns only through the "P(ready) unchanged" clause (1 → 1/8). It certifies the blank's mass; readiness and
  access rest wholly on H-access. That is G8's regress in substance, escaping G8 only through the restore clause. (b) W-certified = yes is tautological when E ⊂ W. (c) H-access is in Λ only because H-law is ablated first; ablating H-access first would leave Λ={H-law, pin}, as C1 has. The frozen
  order is applied correctly. (d) Under Reading B, all 16 covering balls stay in Λ.

**Agreement.** My note agrees with the executor's (i)–(v) and adds (a) and (c). The token RR-AVAILABLE[H-access, q10-ball pin] follows
only under Reading A plus the AMB-3 order, and it is void with the stage.

## Check 3: favourable tokens, gate by gate

- **C1 / POS-1.** G1 holds: CI:24–25 and s12:35–37 give the radii; q10 is not a source (v15c:541–549, r13c:258); no BANK cell lies in
  either ball (I checked all eight rays; s12:53–54). G2–G6 hold. The f-test is valid (the 000 vs 001 flip at q10 leaves W_0 the same),
  so W-certified = no. The restore of the q10 pin is valid under A: only source items remain, and they pin only cells R_E leaves free,
  so P(ready) = 8^{−n_E} ≤ 1/8 < 1.
- **C5.** G1–G6 hold. W-certified = yes is correct. H-access belongs in Λ: with H-law removed, a trivial W fails the f-test. G8 passes.
- No candidate uses H-sel, and H-law appears in C1's token, consistent with #914 c. 6558349705.

**Check 4: the UNRESOLVED stops.** C2 should stop at an earlier gate (Finding 4). C3 is decidable at the stated step (Finding 3). C4 is genuine, but its reason needs
correcting (Finding 5). C6's RR-NOT-READY at G3 is correct (K:92, 97–98).

## Check 5: anchors (36 sampled; all resolve at the stated SHA)

**Named keys.** **v15c:541–549:** `local_sources()`, the 17 named exceptions. **v15c:563–568:** `classify`: named source, then inventory,
then PINNED (AMB-4 ✓). **r13c:258:** every SG position at dist ≥ L+1 from (0,S,78). **K:92:** Pr(eta=z|C=c)=8^(−28). **K:97–98:**
"initial packet and complete past record are functions of C". **CI:79–86:** dist(qk,q10)+(R+k)=L+1, so chain cones lie in the q10 balls.

**Also ✓.** v15c: 377–380, 384–391, 552–560, 575, 607–614. r13c: 249–253. K: 47–52, 54–55, 61–63, 77–80, 94–96, 110, 137–138.
CI: 24–25, 84–88, 91–93, 111–121. IC: 32, 38–40, 63. h9: 50–53, 56–59, 61–66, 116–121. s12: 35–37, 51–54, 58.
d14: 23–27, 36, 49–51. v15: 63–67, 73–74, 78, 103, 112–113. AB: 8, 12–16, 21–23, 26, 31–41, 45–48. CR: 8, 11–12. h11: 83–86, 151–152.
P3:110. r7: 17, 19. SG:4 and SG rows 1, 2, 4, 6. MR-pre: 165, 184–187. NC1: 57–59, 150–152. Main:56.

**Imprecise or off-target:** K:104–105, v15c:32–33 (Finding 11); P3:103, h10:42–45 (Finding 4).

## Check 6: §7 table and register

All 15 PR §7 invariants are in result §5. No value is computation-derived and absent from a source (π_0 values are one-line or symbolic;
distances are written arithmetic on the symbolic constants). No Native A anchor (no native_v11, native_x_v12 or IC:44–54; IC:63 and
v15:73–74 are shared-interface lines). Every NC1 citation is tagged [draft] (lines 13, 73, 137, 201). No no-go or adopt wording; the
only hits (lines 182, 202) are scoped.

## Check 7: token definitions

Every token is a frozen form at the correct gate: RR-NOT-READY at G3 (NEG-1, CC-2(a), C6); RR-REPRESENTABLE-ONLY at G4 (CC-2(b));
RR-AVAILABLE[Λ] at G10; UNRESOLVED(G7:h). Improvisations beyond the frozen procedure: the AMB-1 and AMB-3 readings (Findings 1–2),
the AMB-5 schema (Finding 4), member selection (Finding 8), and partial Λ (Finding 9).

**Verdict: REVISE** — `RO1-SPEC-r1.md` at `7156d761440f54469263663f93aaaa0609b25ec6` (PR #1294; file SHA-256 `d7f4380d…a4341`, matching the directory README). Three blocking findings, seven major and twelve minor findings.

# Independent review of RO1-SPEC-r1

**Reviewer:** independent agent, not the writer. **Method:** reading only: no computation, no Lean, no edit, no post.
**Read:** the spec, and `RO1-OVERLAP-r3.md` (blob `9a98a321`, the same at the adoption SHA `e6050035` and at `7156d761`). `main` at `dfeec843` (`papers/Main.md`, `papers/Substratum.md`, `book/ch18-beyond.md`, `B4PRIME.md`). The ledger branch at `9ff3b8d9` (`LEDGER-r8.md`, README). SEL-ACCESS-1 at `1b966a03`, SEL-EXCL-1 at `0ecfddeb` and SEL-DISC-1 at `445b17f7` / `37e19f3d` / `3c445e6c`. Through the API: #914 c.6883249235, c.6880010243, c.6875548603, c.6875046763, c.6877420015 and c.6878200172; #1169 c.6880022363 and c.6876591512; #1143 c.6777830496; the bodies of #1143, #1060 and #914; and the review lists of #1224, #1228 and #1281.

Line numbers refer to `RO1-SPEC-r1.md` at `7156d761`.

## Checked and correct

- **Quotations.** Every quotation of an owner or planning record that I checked is verbatim. That covers §1 (ll. 49–73), the authority (ll. 7–14), item 3 (ll. 391–393), item 4 (ll. 255–261), "Physical source remains NOT PASSED" (l. 237), the #1060 BELL-QSET rule, the #1143 body sentences and verdict vocabulary, the #1143 c.6777830496 sentence, and the #914 O-IF-SELECT row.
- **The citations in §9.** Each one is correct:
  - All three commits exist.
  - The blobs match: `5c125be5`, `1e8892ff` and `ccf2d46d`, with the last identical at `37e19f3d`. At `3c445e6c` only l. 3 differs.
  - The review ids and their `commit_id`s match the stated SHAs: 5840425454@`ea8827ff`, 5840851253@`1b966a03`, 5845436861@`4813bc0b`, 5848321039@`0ecfddeb`, 5897727347 and 5898055055@`445b17f7`, and 5898298958 and 5901719219@`37e19f3d`.
  - #1224, #1228 and #1281 are open drafts, unmerged.
  - Each is marked "Reviewed, not merged", and the §A.42 item 8 gap is stated (ll. 401–403).
  - The stale in-file status lines are noted correctly: SEL-ACCESS-1 l. 5; SEL-EXCL-1 ll. 7, 132 and 192.
- **IC₂.** It is "open, home #1143" (J6, l. 191). It is not a clause of C (l. 254). It enters only as a test (§8 step 7), and the owner's four conditions are quoted and shown unmet (ll. 263–264).
- **Necessity.** It is stated as optional and is neither asserted nor used (ll. 286–288).
- **The clauses.** Each clause names the tuple components it constrains (table, ll. 158–166). None mentions a quantum table, the Born rule or a Tsirelson value.
- **The rename `E` → `Obs`.** It is harmless and consistent with SEL-DISC-1 l. 34 ("embedded observer/readout map"), and no #1143 record is renamed. Note that SEL-DISC-1 P6 (l. 54) writes `(φ, μ, E)`.
- **Off-main availability.** The closure contract covers the three #1143 continuations named in r3 O5 (fresh cell, same seed, one-bit message), and routes their availability to #866 and #913 (§5.1, S3).
- **Main lines.** The `main` line citations I checked are accurate: Main 18, 42, 97, 360, 362, 364–389, 416–423, 558, 584–588, 596–598 and 742–758; Substratum 131–133; ch18 64 and 72; B4PRIME 19. LEDGER 139, 155, 360, 380, 506, 931, 937 and 938 are accurate on the ledger branch.

## Blocking

**B1. §7.2, ll. 314–329, with the outcome paragraph (ll. 36–41) and S2. "The frame admits the PR countercontrol … REFUTED" is not supported, and it contradicts the spec's own rule.**
- **K-acc.** K-acc (l. 163) makes `Γ` "the set of programs that `M`'s own dynamics executes through `Obs`… nothing it cannot execute is added". The source says the opposite of what l. 322 needs:
  - In SEL-EXCL-1, "Alice chooses/records x", and the grammar is declared (l. 44).
  - "This interface is **specified, not derived from the native OI/SM dynamics**" (l. 46).
  - The interface itself is "UNSOURCED" (l. 129), and the menu restriction is "**assumed** rather than OI-derived" (l. 150).
  - `T` leaves `x, y` unchanged and executes no setting program.
  - #1143 c.6777830496 lists "physical setting programs" in the source certificate.

  Whether `Γ` contains the single-use Bell test under K-acc is therefore an open availability question (O10). l. 322 resolves it silently.
- **"Needs none of them" (ll. 328–329).** This is incorrect. The single-use test needs setting actuation, setting sources independent of `r`, and a clock. These are availability questions of the same kind as §5.1 (SEL-DISC-1 l. 95; SEL-EXCL-1 l. 192: "avoid claiming a sourced OI setting writer, clock").
- **§8 step 2 (ll. 361–363).** By the rule's own step 2, this control is UNSOURCED, not REFUTED.
- **Scope of the rule.** §8 says it "applies to any complete statement of C, which needs K-X and a choice of `≈`" (ll. 354–355), and step 1 requires the freeze first. §7.2 and l. 386 apply it to an incomplete frame with `≈` unchosen.
- **Classical control.** Step 3 requires that C *admit* a model with a classical fragment. §7.1 (ll. 303–305) shows only that nothing forbids one, and exhibiting one meets the same K-acc availability question. A verdict over a control that is not green is void (§A.29).
- **Hidden choices.** The verdict silently takes `≈` = (i) (S1) and the class reading (S6). Under the sector reading, a sector inside a model containing the PR gate need not contain the PR programs.

*Safe path:* state §7.2 conditionally: if the setting, use and record programs of SEL-EXCL-1 are executable in the sense of K-acc, the frame admits the PR model. Record the control as UNSOURCED under step 2. Remove "REFUTED" and "cannot yet be sound" (l. 37). Restate S2's premise to match.

**B2. Soundness has no structure-preserving correspondence (ll. 280–284), so §8 steps 5–7 and ll. 229–234 do not follow.**
- **The gap.** Soundness asks only that each program's complete-record law "equals that of some finite quantum experiment, under one program correspondence". Any finite conditional table `P(a,b|x,y)`, PR's included, is the law of some finite quantum experiment: a single device, even a classical channel, taking `(x,y)` jointly. So with this definition the PR model does not fail soundness. Same-seed signalling and `J = 2` do not fail it either.
- **What the inferences need.** They need the correspondence to map:
  - wings to separate quantum subsystems with local instruments;
  - parallel composition to composite systems;
  - classical messages to classical channels with the same alphabet, budget and schedule (S-A3, S-A6).
- **The sources assume this.** SEL-EXCL-1 l. 81 speaks of "the corresponding bipartite dichotomic Bell scenario". SEL-DISC-1 D7 rests on local-instrument and one-classical-bit premises (ll. 129, 190). SEL-ACCESS-1 §1 item 4 speaks of "a predeclared family of … instruments, compositions".
- **The asymmetry.** Coverage (ll. 276–277) requires the correspondence to respect S-A1 to S-A3. Soundness does not.

*Safe path:* add to soundness, as [P], that the one correspondence respects S-A1 to S-A3 and S-A6, in the sense above. Note that this constrains the quantum comparison class. It is not a clause of C, so §6.1 is unaffected. Then re-derive ll. 232–233 and steps 5–7 against it.

**B3. "[R] Every candidate in the corpus falls into one of five kinds" (l. 338) and the outcome trichotomy (ll. 38–40) are unsupported negative claims (§A.19), and the table omits corpus candidates.**
- **J2, (C1)–(C4).** §4 itself records "No result says whether (C1)–(C4) excludes PR" (l. 187), yet J2 is absent from the K-X table. Main l. 78 notes that (C4) is met by "a pre-sampled hidden variable … (the response-table construction)", which is suggestive but not a result.
- **The OI⁺ principles and their refinements.** Main 584–588 gives the OI⁺ principles, their primitive-source form (implementation locality, phase-free richness, embedded observation) and the substratum-source form. These are physically stated principles on `main`, kernel-checked as equivalent to exact finite operational QM on every nonempty finite carrier. They are the corpus's principal candidates for a quantum-selecting condition, and l. 292 cites them only as "not a sector result".
- **The ban at l. 174.** That ban ("No clause mentions a Hilbert space, a density operator …") is stricter than the records: #914 c.6875046763 decision 4 allows complex matrices "as a conditional mathematical input". The ban silently excludes the OI⁺ route. Whether such clauses are circular is an open question to state, not one to settle by wording.
- **Candidate E.** SEL-ACCESS-1 §3 candidate E is also unlisted.
- **The H-Bell row (l. 344).** As stated, H-Bell does not exclude PR. Its clauses are parameter dependence, operational no-signalling and continuum curvature (Substratum l. 133). The PR model satisfies the first two. So "depends on Q7" does not make H-Bell a PR-excluding candidate.

*Safe path:* relabel l. 338 as [A-inf] over a stated search. Add rows for J2 (untested), for OI⁺ and its refinements (with their posited inputs, and the l. 174 ban raised as an owner question) and for candidate E. Correct the H-Bell row. Restate the outcome paragraph and S2 to match.

## Major

**M1. (C1)–(C4) excluded from C silently (ll. 98–99).** "The observer conditions (C1)–(C4) … are not clauses of C" reads as a substantive exclusion of J2's ground, not as notation. Either reword it as notation only (the `K-` names avoid a collision), or list the inclusion of (C1)–(C4) as a stop.

**M2. Parts of the open typing question settled without a stop.** Owner item 1 says "The shared model-identity and typing questions remain open". Two parts are settled here:
- K-dyn folds E into `φ` ("It includes whatever E adds", l. 160; l. 101). An extension may instead add an operation, as Main 588's "empirical controllability resource" does, or add access rules.
- K-acc makes `Γ` a function of `(φ, Obs)` rather than a component of the tuple.

Both are typing decisions on the shared interface (r3 O1). In addition, J7's §A.29 judgement is not shown:
- "preserves every existing control" (l. 192) is asserted, but applying K-acc to SEL-EXCL-1 is exactly the open point of B1.
- "executes through `Obs`" is undefined until O10 is answered, so K-acc as written is open to adjustment (§A.29, "reject any variant that can be adjusted").

List both points under S1 or S3, or as a new stop.

**M3. LEDGER and r3 cited as results on `main`.** `LEDGER-r8.md` is on the records branch at `9ff3b8d9`, not on `main`. Its README reads "UNREVIEWED — NOT AUTHORITATIVE", and its header reads "UNREVIEWED", though a REVIEW-r8 ACCEPT is recorded. Yet it supports items labelled "[R, main]":
- l. 160 (LEDGER §§2.1, 2.2);
- l. 162 (§3.3);
- l. 189 (§3.1);
- l. 290 ("Neither coverage nor soundness is proved for any C", LEDGER:139);
- ll. 309–310 ("No mechanism is stated in the corpus").

The last two are negative claims whose search lives in the ledger. l. 97 labels a statement about r3 (a draft on PR #1294) "[R, main]". Owner item 3 covers #1224, #1228 and #1281 only. *Safe path:* cite the `main` lines directly where they exist. Otherwise label each citation as an off-`main` record at `9ff3b8d9` with its review state, and state the §A.42 item 8 gap in §9.

**M4. J1's C0 control is not supported at the cited commit (l. 186).** SEL-ACCESS-1 §3 does not prove C0. It points to pages outside the repository (SEL-ACCESS-1 l. 26), lists them as "not adopted as main-established evidence" (l. 123), and SEL-DISC-1 l. 30 records that the original review artifacts were not recovered. C0 is also outside §9's "Scope cited here" for SEL-ACCESS-1 (l. 397). Drop the citation, or mark its support as held outside the repository and record the gap.

**M5. K-X defined by its control outcomes (l. 166; ll. 333–336).** "The clause that excludes stronger-than-quantum behaviour while keeping the quantum Bell target" specifies the clause by the outcomes that #1060 and §6.1 forbid using as its selection criterion. Owner item 4's first condition requires the same of IC₂. Reword as follows. K-X is a physically justified clause, stated first with its justification. PR exclusion, the 2√2 reference and the classical fragment are the §8 tests it must then pass, as r3 §4.5.3 proposes.

**M6. The reading of S-J is too narrow, and it depends on S6 (ll. 179–181).** Confinement is read as why observers are embedded as K-obs says, and why programs are only those of K-acc. K-acc holds by definition, so that half is empty. The reading also omits the Bell part of the obligation, "for Bell this includes excluding stronger-than-quantum correlations in the physical sector" (#914 c.6875548603), which is K-X's ground. Under the class reading, confinement asks why the actual world is a C-model; under the sector reading, why observers cannot run programs outside the sector. State both, and tie them to S6.

**M7. O11 narrowed without a stop (ll. 138–142).** The [P] requirement that `≈` never identify models whose menus differ constrains the open choice of `≈`. Under it, any relation coarser than equality of menus is excluded. Move it into S1 as a proposed constraint for the owner.

## Minor

- **m1. Closure contract label (l. 203).** The heading is not labelled "proposed"; only the [P] tag at l. 205 marks it. The decision rule is labelled (ll. 352–354). Add "(proposed)" to the §5 heading.
- **m2. §5.1 omits #1143 continuations.** SEL-DISC-1 l. 71 and SEL-EXCL-1 ll. 91 and 97 name continuations outside the fresh-cell grammar: a probe of `r` or of an unused cell, an arbitrary choice of source index, and a unilateral stop or ready request that alters the remote clock or failure fields. It also omits the single-use test's own setting actuation (see B1). The column "Inside C?" (l. 223) should read "In `Γ`?", because programs are not members of a class of models.
- **m3. S-A5 against §7.2 (ll. 213, 320).** It is unclear whether a finite bank pre-prepared in `μ` counts as "an executed renewal or preparation process".
- **m4. Finiteness hypotheses.**
  - J3 omits finiteness of `S` and canonical typicality (Main 758), which conflicts with K-dyn's "`S` need not be one fixed finite set".
  - J4's cone needs `V` and each `S_i` finite (Main 362).
  - The ceiling's hypotheses are (i)–(iv) of Main 364–376, not only (viii) and (xiv).
  - K-dyn departs from ledger (ii) (A1, total finiteness, posited); say so.
- **m5. K-dyn status (l. 160).** Main 42 gives `φ: S → S`, not a bijection. Bijectivity is ledger (iii), part-empirical. "[R, main] Bare-OI premise" overstates this: the clause adopts a posit.
- **m6. S4 (l. 415).** It is not shown to be needed to state C. K-obs quantifies over each observer and holds under either answer to Q1, which bears instead on coverage's "one stated `Obs`" (l. 273).
- **m7. S2 (l. 413).** It asks the owner "is it native (O4)?". O4 is a scientific question homed at #1143, not an owner decision. r3 owner question 6 (present both routes with their consequences) is not carried forward. It would allow conditional variants of C without deciding Q7.
- **m8. Labels.**
  - l. 112: [A] is used for an alternative reading, which is not an assumption.
  - l. 338: [R] is given without an evidence state.
  - l. 146: "so one record law has many realizations" is an inference from Main 598. Cite M-1 and B4′, or mark it [A-inf].
- **m9. The O12 attribution.** The O12 convention is to name the other objects in full (r3 l. 212), not to introduce `Res`. The rename is harmless, but its attribution is inexact.
- **m10. Coverage wording (ll. 273–275).** It maps an experiment "family `Q`" to one program `g` with "`Q`'s law". It should map each experiment of the family.
- **m11. The outcome paragraph (l. 36).** "the clauses that the corpus can support today" includes K-acc, K-src, K-rec and K-res, which are new [P] proposals.
- **m12. Row 4 of §7.3 (l. 345).** The row does not exclude PR (its bound is `min{4, …}`), and it bears on Q8 (S5) rather than Q7. The trichotomy at ll. 38–40 does not cover it.

## Answers to the brief

1. **C on the model.** The clauses name their components, and none is defined by quantum statistics. K-X's framing selects by outcome (M5). The rename is harmless and consistent.
2. **J1–J9.** Sources and Issues are mostly right. J1's C0 control fails (M4), J3's and J4's hypotheses are incomplete (m4), and the J7 judgement is not shown (M2). IC₂ is "open, home #1143" and is not in C.
3. **The closure contract and the decision rule.** The contract is [P] but its heading is not labelled "proposed" (m1). The rule is labelled. The named continuations are covered and routed to #866 and #913, with gaps (m2).
4. **Coverage and soundness.** They are on one model, and necessity is optional and not asserted. Soundness lacks a correspondence that preserves wings and messages (B2).
5. **Off-`main` citations.** The §9 citations are correct. The LEDGER and r3 are cited as results on `main` (M3).
6. **The six stops.**
   - S1, S3 and S6 are genuine. S2 is genuine in substance, but it rests on B1 and B3. S4 is not shown to be needed (m6). S5 is reasonable.
   - The identity relation is narrowed outside S1 (M7).
   - The claim that the frame admits PR resolves availability silently (B1).
   - The claim that the excluding clause needs Q7 or IC₂/O4 omits J2 and OI⁺ and misreads H-Bell (B3).
   - The exclusion of (C1)–(C4) from C and the typing choices are silent (M1, M2).
7. **Labels.** They are mostly complete, with the exceptions in M3 and m8.

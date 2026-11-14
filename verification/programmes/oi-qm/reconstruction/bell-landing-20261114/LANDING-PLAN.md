# Landing plan: Bell support and ladder package (#868)

**Paper-only plan. It authorizes nothing, changes no scientific conclusion, adopts no premise and
merges nothing.** It traces the load-bearing statements of the Bell debugging ladder to their
sources, fixes the order in which they can land, and states the composition of one combined Bell
landing candidate. The draft STATUS notes in this directory (`STATUS-BS.md`, `STATUS-SB-L3.md`,
`STATUS-LADDER.md`) are written to this plan; `NOTES-PLAN.md` records sources, decisions and open
owner questions.

- **Authority.** #868 comment 6873193841 (`amaybaum`, 2026-11-14T06:34:07Z), recording the owner's
  message verbatim: "Q2: Yes. I authorize the paper-only landing plan now, before #1283 is adopted.
  The authorization covers preparing a dependency-aware integration plan, drafting the necessary
  STATUS notes, and obtaining one independent review of the complete plan." Its boundaries: "This
  authorizes planning, document preparation and independent review only. It does not authorize
  merging #1274, #1273 or their supporting PRs; adopting #1283; changing scientific conclusions; or
  starting new Bell experiments. Each eventual merge still requires its own applicable gates and
  explicit owner decision."
- **Accountable Issue.** #868 (Bell ladder, Bell-scope); #1169 (SUBSTATE-BRIDGE-1 L3, #1274).
- **Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`, unchanged when this plan was
  written. "Main:n" is line n of `papers/Main.md` at that commit (blob `0db17597`). Input heads,
  each equal to its branch head when read:

  | Label | PR | Branch | Head | Principal file (blob) |
  |---|---|---|---|---|
  | BS | #1231 | `research/bell-scope-868-20261111` | `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918` | `BELL-SCOPE-UNIT1.md` (`5814e479`) |
  | SB | #1232 | `research/substate-bridge-1-20261111` | `86a413c88cd14d344aa41b6f47885aeb24da6910` | `SUBSTATE-BRIDGE-UNIT1.md` (`9ff0f077`) |
  | QH | #1269 | `research/q868h-868-20261113` | `ffc9cda4852590d95133a07eda75af824aa3b799` | `Q868H-UNIT1.md` (`ebf5215b`) |
  | LD | #1273 | `research/bell-ladder-868-20261113` | `d8e4f80e71b64972ee3e87a874544c8bd358d5c2` | `BELL-LADDER-r3.md` (`0298088d`) |
  | OC | #1274 | `research/optc-1230-1232-20261113` | `fef9485712fe0b2c72416bfc900654ff64e7453d` | `NEW-RESULTS.md` (`b0e930ab`) |
  | A46 | #1283 | `policy/a46-amendment-oq10-20261113` | `f57e576a87fe65399d9f2db2e532abf2378e3ad0` | `AGENTS.md` §A.46 draft |

  "BS:n", "S:n", "QH:n", "LD:n" and "OC:n" are lines of the principal files at those heads. "…" is
  `verification/programmes/oi-qm/reconstruction`. BS and SB are pinned at `cac5d264`, an ancestor
  of `main`; every `Main:n` they cite with n ≥ 6 is `Main:(n−2)` at `c3b5f37a` (the 2-line deletion at
  Main:4–5 is the only change in line count between the two commits).

**Evidence tags** (as in the inputs). [K] kernel statement on `main`; [P] manuscript on `main`;
[W] research record on `main`, model-reviewed, not verification (§A.46 item 7); [D] draft off
`main`; [A] paper argument in the cited record; [L] literature, recalled; [X] exact generic check in
a probe that encodes no OI rule (supports, does not replace, an argument).

***

## 1. Dependency order and gates

The order is the owner's: "#1283 adoption, then #1274 through its own gates, followed by the Bell
support and ladder package" (c.6873193841).

| Step | Object | Gate (each needs its own recorded owner decision where marked) | Why it comes here |
|---|---|---|---|
| G0 | #1283, §A.46 item 8 | Owner adoption decision; the adoption line's placeholders filled from it; merge (owner). Until then reading R-b stays in force: a record in this plan can land only under an explicit, recorded owner exception, and the owner's order (c.6873193841) defers landing until adoption. | Item 8 is the landing basis used below. If the adopted text differs from `f57e576a`, the per-record condition tables (§7) are re-checked against the adopted text. |
| G1 | #1274 (option-(c) package) | (i) its `STATUS.md` "Landing" section brought into line with the adopted §A.46 basis (review 5901837851: "must be explicitly brought into line with any **adopted** §A.46 basis at integration"); (i′) a focused exact-head review of the edited head, since review 5901837851 accepted `fef94857`; (ii) a current-status note appended to the PR description (same review); (iii) exact-head CI and mergeability; (iv) owner merge decision; (v) merge commit, so the reviewed commits stay ancestors of `main` (OC `STATUS.md`, "Landing"). | The ladder's citations of SB's routes A/B/C (S:177–181), N3 (S:189) and N4 (S:190) resolve on `main` only through OC:490–494, :508 and :509. #1274 does not depend on this package: its gaps D2 (L3) and E2 (Theorem N) are carried as named conditions (OC `DEPENDENCIES.md`:23, :26). |
| G2 | Bell package (§5) | (i) branch from `main` after G1; (ii) merge commits of `e1534b08` (BS) and `d8e4f80e` (LD); (iii) the L3 carried record and the three STATUS notes added; (iv) source drift re-measured against the `main` of that day and the notes re-pinned; (v) checks (§5.4); (vi) reviews: a non-author review of the new text (L3 record, STATUS notes), the review question of NOTES-PLAN OQ-2 for BS and L3, then a ChatGPT exact-head review of the package head; (vii) owner merge decision; (viii) merge commit. | Inside the package BS precedes L3 (L3 reuses Theorem N's step 1, S:169) and both precede LD (LD §0 and stages 3, 5, 6 cite them). One merge lands all three, so every cross-reference resolves at once. |
| G3 | After G2 | A forward note in each STATUS.md quoting the owner's merge record with its author and time (§A.42 item 7), followed by a focused exact-head check, as for #1269 (review 5897397957); planning-status updates on #868 and #1169 under §A.45 rule 3 maintenance, citing the owner's merge record. | Records the landed state; changes no scientific status. The STATUS notes state their own package review and merge decision at the package head only, so the reviewed head is not moved to record them. |

**Inside G2, by record.** BS lands whole and byte-identical if the owner so chooses (NOTES-PLAN
OQ-5): the whole record also lands Lemma G, NBA, §5 and §6, beyond the components named in
c.6873193841; L3 lands as a carried extract (§5.2);
LD lands whole and byte-identical. No accepted text is edited. Each STATUS note states the record's
standing, its superseded lines and its source drift, as in OC `STATUS.md` and the nine notes
reconciled in #1284 (`records/reconcile-1265-oq10-20261113` @ `6e2d1ee8`).

**No promotion.** Landing changes no evidence layer: [A] stays [A], [D] items become [W]-type research
records on `main` and stay model-reviewed, not verified (§A.46 item 7; #1283 item 8: "landing a record
does not change its evidence layer"). No manuscript statement changes; Main:362, :364–389, :414 and
:724 are cited as they stand.

***

## 2. Statement-level dependency table

Each ladder claim is traced to the statement that supports it, at the accepted head. "Where":
**main** = on `main` at `c3b5f37a`; **OC** = carried by #1274 at `fef94857`; **package** = lands in
G2; **context** = cited, not used by any verdict (provenance under §A.42 item 8).

### 2.1 Stages 0–7 (LD:95–104)

| Ladder claim | Source statement (file:line @ head) | Layer | Where |
|---|---|---|---|
| Stage 0, NOT FORCED (designed witness) | `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`, `finite_horizon_equivalence`: `verification/lean-mathlib/OIBridge/Equivalence.lean`:422, :294, :245, :462 @ `c3b5f37a` (blob `9513665b`); composite converses :466–468 | K | main |
| | Main:546–552, :97 (pointers); PR realizable Main:360, :427; response-table prior Main:516–518 | P | main |
| | the PR law is a finite trajectory law (LD:106–118) | A | package (LD) |
| Stage 1, NOT FORCED | one realization for every action sequence, Main:480–482; finite menu vs continuum instrument space, Main:486 | P | main |
| | `φ_×` with `μ_0`: PR with complete-history NS (LD:145–149, check 1) | A | package (LD) |
| Stage 2, NOT FORCED | `φ_×` site-factorized with edge `g_A → r_B` (LD:134, :145) | A | package (LD) |
| | "globally coupled setting-dependent hidden dynamics", Main:360 | P | main |
| Stage 3, NOT FORCED | cone lemma, pointwise parameter independence, Main:362 | P | main |
| | directed form of (Sep): SB L3, S:167–171 | A (on BS Theorem N, Main:362) | package (L3 carried record) |
| | `φ_0` with `μ_MD`: separated, PR, complete-history NS (LD:150–153, check 2) | A | package (LD) |
| Stage 4, NOT FORCED | `φ_0` with `μ_MD` satisfies (Gen), (Rec), (GI) (LD:150–153) | A | package (LD) |
| | (Gen), (Rec), (GI) are protocol properties, BS:156 | A | package (BS) |
| | settings as configuration content, Main:42; `…/oa-1-20261112/OA-1-REPORT-r5.md`:111–112 (blob `5a16b213`) | P; W | main |
| | QH's settings enter through the supplied controller P3, QH:213–214 | D | context (§4) |
| Stage 5, OBSTRUCTION | Theorem N, BS:159–178; Theorem N′, BS:185–196 | A (on Main:362, P) | package (BS) |
| | exogenous form, Main:364–389; ledger (xiv), Main:724 | P | main |
| | CHSH ≤ 2 and ε ≥ (√2−1)/4 to the Tsirelson box, BS:317–330 (bound at :323–327) | A (optimality at :329–330: A + X G3) | package (BS) |
| | directed (Sep) in the controlling condition (LD:56–62) | A | package (L3 carried record) |
| Stage 6, OBSTRUCTION | ⊥-rule and full-history contraction, BS:345–355 | A + X G5 | package (BS) |
| | composition per run with fresh generators, BS:292–294 | A | package (BS) |
| | Proposition AL (LD:187–263) | A | package (LD) |
| | NS for a full-span family forces pointwise locality, `…/oi-qm-ext-1/prepared-pair-source.md`:134–145 (blob `9123157c`) | W | main |
| Stage 7, UNDETERMINED | PR reachable in the relaxed class, Main:360 | P | main |
| | no selector supplied, MI-kept routes: N4, S:190 → OC:509 | A (classification; requirement not supplied) | OC |
| | measurement-dependent branch, not covered by N4 at either head (§2.5): PR reachability, LD:150–153 (check 2); no selector supplied, Main:360 (general sentence), :416 | A; P | package (LD); main |
| | SWAP/2 reached by the native encoded U′ composite, QH:68–97 | D | context (§4) |
| | SWAP/2 Bell-local over Pauli-axis product tests (LD:104) | A | package (LD) |

### 2.2 §0, Proposition AL, controls, open premises

| Ladder claim | Source statement (file:line @ head) | Layer | Where |
|---|---|---|---|
| §0 controlling condition (LD:53–62) | Theorem N/N′ (BS:159–196); Main:364–389; directed (Sep) via L3 (S:167–171) | A on P | package (BS, L3); main |
| §0 "for OI under the ledger" (LD:78–83) | Proposition AL; Theorem N with (GI) and (xiv), or N′ under MI* (BS:159–196); Main:414 (outside (vii)) | A; P | package; main |
| AL step 1 (LD:216) | OA1 D5, `OA-1-REPORT-r5.md`:176–195 | W | main |
| AL (AL2) coverage (LD:192–195) | OA1:556–558 (MP-0a), :103–105 (μ-G); "RC's `D_0`" is a name only, and OA1:556–558 is the support | W | main; RC context |
| AL (AL4) "complete in the sense of BS (Rec)" (LD:198–201) | BS:146–149 | A | package (BS) |
| AL conclusion, ε bound (LD:209–210) | BS §4.1 bound, BS:323–327 (needs Bell locality only) | A | package (BS) |
| AL dichotomy (LD:210–213) | T1 Lemma A-T (d), `…/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md`:73–76 (blob `a9cbc675`) | W | main |
| AL relation to E2 (LD:234–240) | `…/oa-2-20261112/OA-2-REPORT-r4.md`:606–613 (blob `8f8ddf73`) | W | main (provenance for priority, LD:295) |
| AL consequence (ii), route C closed for the affine class (LD:256–259) | route C as defined at S:181 → OC:494; window Main:414 | A; P | OC; main |
| Controls §3, coupling rows (LD:172–173) | toy maps of §2 | A | package (LD) |
| Controls §3, access rows (LD:174–176) | Theorem N′ for the residue row (BS:185–196) | A | package (BS, LD) |
| Controls §3, initial-law row (LD:177) | (Sep) in both forms for `φ_0`; MI fails for `μ_MD` | A | package (LD) |
| §5 NBA row (LD:272) | NBA, BS:232–244; N3, S:189 → OC:508; PPS:134–145; H-Bell, `papers/Substratum.md`:131–133 | A; W; P | package (BS); OC; main |
| §5 escape requirements (LD:280–284) | "the resolution at which masking fails, SB:220" | A (example) | context |
| §5 run law under (iv) (LD:275) | RC C9, C10 (pointer to an open item); OA1:176–195 | D; W | context; main |
| §4 hypotheses (vii), (xiii), (ii), (viii) | Main:724 | P | main |

### 2.3 What each landing addresses

- **BS** closes the ladder's item-8 gap at LD:298. **BS** puts on `main` the Theorem N on which OC's
  narrowed row E2 is conditioned (OC `DEPENDENCIES.md`:26).
- **L3** closes the ladder's L3 gap at LD:299. **L3** puts on `main` the argument on which OC's
  narrowed row D2 (N2's necessity) is conditioned (OC `DEPENDENCIES.md`:23).
- OC's statements stay conditional as written, and SLL's exclusion consequence still needs SB L2
  (gap D3).
- **OC (#1274)** closes the ladder's N4 gap at LD:299 at N4's own scope (N4 at OC:509; the parts of
  LD:104 and LD:271 outside that scope are stated in §2.5), and supplies routes A/B/C
  (OC:490–494) and N3 (OC:508).
- **Not closed by this plan:** OC's gap D3 (SB L2, S:153, and class (a)3, S:263), which the owner's
  package does not name and the ladder does not use (NOTES-PLAN OQ-4); OC's gap A1.

### 2.4 Dependencies the input records do not state

- **L3 rests on Theorem N.** L3's argument is "step 1 of Theorem N goes through with directed
  distance" (S:169). L3 cannot land before BS; it lands with it.
- **The ladder's (Sep) is the directed form.** LD:57–59 states (Sep) by directed paths and cites BS
  for the symmetrized form, "which is sufficient". Without L3 on `main`, stage 5 holds for the
  symmetrized (Sep) only (BS:150), a narrower condition. L3 is load-bearing only for the controlling
  condition (LD:56–62) and stage 5, which uses it (LD:102). At stage 3 (LD:100) and check 4
  (LD:155–156) it is cited, but those verdicts also hold with symmetrized (Sep). The control row at
  LD:176 does not cite L3: (Sep) fails there in both forms.
- **S5 does not test L3's step.** `generic_substate_checks.py`:241–259 @ `86a413c8` draws response
  tables `h_A(m, l_A, a)`, `h_B(m, l_B, b)` that already factorize through the shared mode, with
  setting-independent weights; the check is the standard CHSH bound for local models and cannot
  fail. It does not exercise the directed-cone step that is L3's content. L3's support is the
  argument (S:169); S5 is provenance (as OC `DEPENDENCIES.md` row X treats SB's probe).
- **Lemma G is listed but unused.** LD:298 names Lemma G among the BS items; no ladder statement
  uses it.
- **Two objects named L3.** S:28 and S:272 ("G★ / L3") refer to the L3 source on `main` for the
  operation component (`…/oi-qm-ext-1/observer-interface-source.md`:199, "site/mode wave-operator
  lift"), not to SB's §3.2 lemma. The package names SB's lemma "SB L3" throughout.

### 2.5 Scope checks: N4, L3 and Theorem N/N′ at their accepted heads

The owner's added requirement (2026-11-14, relayed by the coordinating session): "Verify that #1274
actually carries every N4 statement used by the ladder, rather than treating N4 as closed merely
because #1274 is expected to land. L3 and Theorem N/N′ must also be checked at their exact accepted
scope." Each use below is quoted as the ladder makes it and set against the source text. "Match"
means that the source's hypotheses and scope cover the use as made.

**N4.** Source at `86a413c8`, S:190: "| **N4** | every route, for agreement with the quantum set | A
selector: the mechanism yields CHSH in `(2, 2√2]` and not more | channel + pad alone is the PR box
[X S4] | not supplied; Main:362 records the same over-generation for the unrestricted construction |".
Carried at `fef94857`, OC:509: the same row, with "Main:360" for "Main:362" (Δ1, the same line at
`c3b5f37a`), S4's arithmetic hand-checked at OC:511–514. Scope of the carried row: routes A, B and
C, which OC §5 classifies "with measurement independence kept" (OC:485) and for "the coupling-graph
cone of Main:362 with its finite site set V" (OC:555–559); N4 is a requirement, and OC:516 states
"N1–N4 are requirements; none is supplied". The ladder uses N4 four times, once without
attribution:

| Ladder use (quoted) | Carried text | Hypotheses and scope | Result |
|---|---|---|---|
| LD:104 (stage 7): "In the relaxed class PR (CHSH 4) is reachable (Main:360) and no selector is supplied (SB N4, SB:190) [D]." | OC:509, status "not supplied"; OC:511–514 (channel + fair pad gives CHSH 4) | N4's "not supplied" is stated for the routes of OC §5, all with MI kept. The ladder's "relaxed class" also contains the measurement-dependent branch (stage 5 relaxed; `φ_0` with `μ_MD`), which no route of OC §5 covers, at either head. | **Narrower at both heads.** For the MI-kept part the use matches OC:509. For the measurement-dependent part, PR reachability is the record's own check 2 (LD:150–153) [A], and the absence of a selector rests on Main:360's general statement that bare finite OI representability does not select the quantum Bell set and on Main:416, which records measurement dependence as not adopted [P]; neither N4 nor Main:360's construction, which keeps measurement independence, addresses that branch. Landing SB's own row would not widen the scope (S:175 has the same MI-kept restriction), so nothing further needs to land; `STATUS-LADDER.md` records the split. |
| LD:271 (§5, what would settle stage 7): "an OI-sourced principle, independent of the target table, that bounds CHSH by `2√2` and reaches it (SB N4)" | OC:509: "yields CHSH in `(2, 2√2]` and not more" | N4 requires the bound, not attainment of `2√2`. "and reaches it" is not in N4 at either head. | **Partly carried.** The bound matches OC:509. The attainment clause is the ladder's own addition, attributed to N4; it lands with the ladder as ladder text and is not supported by N4. `STATUS-LADDER.md` records it. It is a settlement criterion, not a result, so no classification changes. |
| LD:284 (§5, escape requirements): "and supply a selector. None is supplied." | OC:509 "not supplied" | route B, measurement independence kept | Matches. |
| LD:299 (item 8 table): "**support off `main`: gap** for L3 and N4 if this record lands" | — | — | Closed for the MI-kept part by OC:509 once #1274 lands; see the first row for the rest. |

**L3.** Source at `86a413c8`, S:169: "If there is no directed path from `G_B` to `R_A^t` of length at
most `t − t_s`, then step 1 of Theorem N goes through with directed distance, `M`'s content at `t_s`
is part of Ω, and the conclusion is unchanged: `M` is a common cause." Review 5858000929 records
that "The classical common-cause observation is also correct under MI"; review 5857981727 (on BS)
records the directed point as not weakening Theorem N/N′. S:167–170 are unchanged from r1
(`b94b283a`, lines 153–156), and S:171 differs from r1:157 only by an appended sentence citing
review 5857981727, so the r1 review's remark applies to L3's statement and argument as accepted; the
r2 re-review 5859960068 does not address L3. Not carried by #1274 (OC:641); OC:507 carries N2
"conditional on L3".

| Ladder use (quoted) | Hypotheses and scope at `86a413c8` | Result |
|---|---|---|
| LD:57–59 (§0): "(Sep) no directed `G_φ` path from either generator region to the other wing's record region within the record window (BS states (Sep) with the symmetrized distance, which is sufficient; the directed form is SB L3)" with "(MI\*) … (or (GI) with MI for Ω)" | L3 names Theorem N, which needs (GI) and MI for Ω. The (MI\*) branch uses Theorem N′. N′'s proof reuses step 1 unchanged (BS:190, "Step 1 does not use (GI)"), so the directed reading carries to N′; that composition is not written in SB. | **Matches for the (GI)+MI branch. Wider for the (MI\*) branch:** the extension of L3 to Theorem N′ must be stated in `SB-L3.md` as a marked addition with its one-line justification from BS:190, and reviewed with it. The addition derives nothing beyond S:169 combined with BS:190: N′'s proof consists of step 1 plus steps 3–4, so it is a composition of two cited statements, not a new argument. |
| LD:100 (stage 3): "directed form SB L3 (SB:167–171) [D]" | as above | Matches (with the same N′ note). |
| LD:155–156 (check 4): "The edge `λ_A0 → r_B` leaves both forms of (Sep) intact at the one-tick window …; `λ_A0` is a common cause (SB L3)." | `λ_A0` is written by no setting; no directed path from a generator into the remote record region | Matches; the check also holds under symmetrized (Sep) (`d(g_B, R_A) = 2` > 1), so it does not depend on L3. |

**Theorem N and N′.** Source at `e1534b08`, BS:159–196. The REVISE review 5857227567 required,
among others (CF⇒MI one direction; the O2 window): NBA's antecedent to name (GI) or replace it (answered by Theorem N′ with λ* and the stronger (MI\*));
optimality of (√2−1)/4 scoped to Bell-local tables and attainment shown only in 𝒞_sep as an abstract
class; the rationality aside tied to (M). The re-review 5857981727 kept the result "restricted,
conditional", the OI-wide verdict indeterminate, the symmetrized (Sep) "a conservative sufficient
screening test", and the six-site witness "logical sharpness only".

| Ladder use (quoted) | Hypotheses and scope at `e1534b08` | Result |
|---|---|---|
| LD:49–51: "Generator isolation (stage 4) is not needed: BS Theorem N′ replaces it by the stronger MI* for `λ* = (Ω, ρ_A, ρ_B)`." | BS:185–193 | Matches. |
| LD:53–62 (§0 controlling condition): (D), (F), (Gen), (Rec), (Sep), (MI\*) or (GI)+MI, finite jointly admissible menu, every-run outputs with a fixed local failure rule, no postselection; conclusion "for the whole finite menu and complete local histories" | BS §3.1 (BS:139–157), conclusion BS:162–165, menu-wide step 3 (BS:175–176); NBA domain BS:232–236 | Matches with symmetrized (Sep); the directed form needs L3 (above). |
| LD:102 (stage 5): "BS Theorem N (BS:159–178), N′ (BS:185–196) … CHSH ≤ 2 and `ε ≥ (√2−1)/4` to the Tsirelson box (BS:317–330)" | bound for "any MI Bell-local family" (BS:321–327); optimality over Bell-local tables (BS:329–330); attainment not cited | Matches. The ladder does not use attainment in 𝒞_sep or the rationality aside. |
| LD:78–81: "Theorem N [D] with (GI) and (xiv), or Theorem N′ if (xiv) is read as MI\*" | (xiv) is MI for Ω (Main:724); owner decision Q2 (#1273 c.6860580909): MI\* stays a distinct hypothesis unless (xiv) is shown to contain every residue | Matches; the N′ branch is conditional as written. |
| LD:103 (stage 6): "⊥-rule and full-history contraction BS:345–355 … composition per run with fresh generators BS:292–294" | contraction needs one product extractor on both laws and a target whose pushforward is the Tsirelson box (BS:347–353); per-run use needs run-n settings to satisfy MI given Ω_n (BS:292–294) | Matches. |
| LD:154, :174, :181–183 (checks and controls citing Theorem N′) | the toy maps meet (Sep) with the symmetrized distance at the one-tick window, and `μ_0` makes the generators independent of every other site | Matches. |
| LD:209–210 (AL): "`ε ≥ (√2−1)/4` to the Tsirelson box (BS §4.1 bound, which needs only Bell locality)" | BS:321 states the bound for an "MI Bell-local family"; AL's conclusion gives λ uniform on `M` and independent of the settings, which is that case | Matches. |

**Consequences for the package.** (1) N4: #1274 carries every N4 statement the ladder uses at the
scope N4 has at `86a413c8`, including the unattributed use at LD:284; the ladder's stage-7 sentence
is wider than N4 in its measurement-dependent part, whose PR reachability is the ladder's check 2
and whose absence of a selector rests on Main:360's general sentence and Main:416 on `main`, and its
§5 settlement criterion adds an attainment clause N4
does not contain. Neither needs further landing; both are recorded in `STATUS-LADDER.md`. (2) L3: its
extension to Theorem N′ is load-bearing for the (MI\*) branch of the ladder's §0 and must be written
into `SB-L3.md` as a marked, reviewed addition. (3) Theorem N/N′: every use is within the accepted
scope; the directed form of (Sep) is the only extension, supplied by L3.

**Status unchanged.** Bell ladder r3 is a conditional paper result. It is not a native OI Bell
mechanism, a native escape or an OI-wide no-go, and nothing in this plan states it otherwise.

***

## 3. Input PRs: heads, reviews, limitations, nits, files

### 3.1 #1231, Bell-scope unit 1 r2 (BS)

- **Accepted head.** `e1534b08` (r2; single parent `7abf59d7`, r1; base `cac5d264`).
- **Reviews.** ChatGPT 5857227567 at `7abf59d7`: REVISE (five required fixes). ChatGPT 5857981727 at
  `e1534b08`: ACCEPT WITH NONBLOCKING NITS, "for the corrected paper unit at its **restricted,
  conditional** scope; preserve OI-wide verdict **INDETERMINATE** and escape **NOT ESTABLISHED**."
  No separate non-author review other than ChatGPT is recorded (NOTES-PLAN OQ-2).
- **Limitations.** Verdict (C) indeterminate for OI itself; (A) only for the class 𝒞_sep, whose
  membership no native protocol is shown to have; NBA open (BS:232–244); Lemma G one direction only
  (BS:215–219); attainment of (√2−1)/4 by a member running the native rule open (BS:339–341);
  probes are exact generic checks, not OI-rule execution (BS:298–311); [L] items recalled, none read
  first-hand (BS:467); Theorem N′ and the six-site toy were seen only by the focused re-review.
- **Outstanding nits.** (n1) symmetrized (Sep) is a conservative sufficient test; a directed form
  should be stated in any later synthesis (review 5857981727; met by SB L3 and LD:57–59); (n2) the
  six-site witness shows logical sharpness only; (n3) F1 and F2 reported, not repaired; MI a posit.
  Record-level: BS:3–5 and BS:471–472 still say r2 awaits re-review; the PR description still
  describes r1 ("12/12 PASS", "unreviewed"), while r2's probe has seventeen checks.
- **Source drift.** F1 and F2 are addressed on `main` since #1233: ledger (x) is scoped to
  `G_φ^ref` and (xiv) is measurement independence (Main:724); Main:362 states that a linear update
  has the same graph on every state class; Main:414 states the O2 window and places the adopted
  branch outside (vii). Details in `STATUS-BS.md`.
- **Files that would land.** All four, byte-identical (§5.1).

### 3.2 #1232, SUBSTATE-BRIDGE-1 unit 1 r2 (SB)

- **Accepted head.** `86a413c8` (r2; parent `b94b283a`, r1; base `cac5d264`).
- **Reviews.** ChatGPT 5858000929 at `b94b283a`: REVISE (four required corrections); it records "The
  classical common-cause observation is also correct under MI". ChatGPT 5859960068 at `86a413c8`:
  ACCEPT WITH NITS. The BS re-review 5857981727 records L3's point as a nonblocking note. #1271's
  reconciliation reads L3 as the standard Bell argument (R3:66, off `main`, provenance). No separate
  non-author review of L3 is recorded.
- **Limitations relevant to L3.** L3 is a one-paragraph argument [A; X S5]; S5 does not test its
  step (§2.4); L3 inherits every hypothesis of Theorem N or N′ except that (Sep) is read with
  directed distance; it says nothing about a factor that a setting writes (route A, N2).
  Unit-level: three out-of-brief native-rule scripts were run in the r1 session and are excluded
  from the evidence (S:5, S:340–342); the unit's 2026-11-11 authorization was not located (OC
  `PROVENANCE.md` §4).
- **Outstanding nits.** Review 5859960068: keep H5's saturation permission distinct from sourced
  preparations; E3 needs continuity; N1–N4 and R1–R3 source no mechanism. None concerns L3.
  Record-level: S:3 and S:356 still say r2 awaits re-review; S:157 and S:163 are stale against
  `main` (corrected in OC by Δ10 and Δ11).
- **Which SB statements #1274 carries, and at what scope** (OC `STATUS.md`:86–95, OC:629–641):
  E1 (§2, with a π–λ hand check), G1 and E2 (§3, G1 narrowed by Δ30/Δ31), L1 and L4 for infinite
  site groups (§4), routes A/B/C with N1–N4 as requirements not supplied and SLL open (§5),
  (NS_A), (PAD) and S7 (§6). N4 is carried at OC:509 as a requirement ("not supplied"), with the S4
  arithmetic hand-checked at OC:511–514. N2 is carried conditional on L3 (OC:507); SLL's exclusion
  consequence conditional on L2 and Theorem N (OC:537–542). Not carried: saturation, E3, **L2**,
  **L3**, §2.4 items 1–5, Q3, §5 scoring (OC:641).
- **Files that would land.** None from the branch. L3 lands as a carried extract (§5.2), so that the
  results outside the owner's option-(c) set (#1169 c.6855167580) stay off `main`.

### 3.3 #1269, Q-868-H unit 1 r3 (QH)

- **Accepted head.** `ffc9cda4`.
- **Reviews.** Independent r1 REVISE (`review/REVIEW-Q868H-UNIT1.md`); fresh independent review of r2
  at `82f592db`, ACCEPT WITH CHANGES (RC1–RC5); focused confirmation of r3, ACCEPT
  (`review/CONFIRM-Q868H-UNIT1-r3.md`); ChatGPT 5891666660 at `acf28d3a`, ACCEPT WITH DOCUMENTATION
  NITS; ChatGPT 5897397957 at `ffc9cda4`, ACCEPT ("both prior documentation nits resolved").
- **Limitations.** (V) PASS for native Pauli product tests with (iv) and NNB where Y is needed; (C)
  PASS conditional on P1/P2/N2, A4 at `q = 2`, E-iso, WL, H-PREP, (iv), NNB; QC FAIL for the U′
  composite with NNB carried; NNB a supplied premise, not adopted; probes ratified retroactively
  (#868 c.6853568040).
- **Outstanding nits.** Integration gated (review 5897397957): off-`main` ASSESS-868 support, three
  SC-42 added-text hits in the byte-preserved ASSESS-868 files, §A.42 obligations.
- **Files that would land.** None (§4).

### 3.4 #1273, Bell debugging ladder r3 (LD)

- **Accepted head.** `d8e4f80e` (chain `c3b5f37a` → `b8096c79` → `c4781c93` → `d8e4f80e`).
- **Reviews.** Non-author `REVIEW-r1.md` of r1: ACCEPT WITH CHANGES (C1–C14, applied in r2);
  `CONFIRM-r2.md` of r2 at `b8096c79`: ACCEPT WITH CHANGES (R1–R3, N1–N4, applied in r3);
  `CONFIRM-r3.md` at `c4781c93`: ACCEPT, "nothing left to change"; ChatGPT 5892919040 at `d8e4f80e`:
  "ACCEPT AS A CONDITIONAL PAPER RESULT, with two integration safeguards". Owner decisions on
  NOTES-r3 Q1–Q4: #1273 c.6860580909 ("Adopt all four (Recommended)").
- **Limitations.** Stages 0–4 rest on designed toy maps that are not OI rules; for the native rule
  those stages are undetermined (LD:89–93). AL covers coset-uniform laws, cell-valued settings,
  fixed record regions and complete histories only (LD:242–253). No general access-only theorem
  (LD:179–183). The §A.31 fixed point is not reached (NOTES-r3:107). Quantum selection undetermined.
- **Outstanding nits.** Review 5892919040's two safeguards, decided by the owner as Q2 and Q4.
  REVIEW-r1 §7: the `Z_3` Birkhoff remark (NOTES-r3:63–64) was not reviewed and nothing rests on it.
  Record-level: LD:3–6 and LD:273 say the ChatGPT review is pending; LD:304 lists QH's
  review 5891666660 only, not the recheck 5897397957; NOTES-r3:1 says "not for landing" while LD:240
  and LD:274 cite NOTES; NOTES-r3:94–104 and :106 predate the owner decisions and the ChatGPT review.
  The PR description carries an appended current status (2026-11-14), as c.6873193841 asked; its r2
  text is kept as written.
- **Files that would land.** All twelve, byte-identical (§5.1).

### 3.5 #1274, option-(c) package (OC)

- **Accepted head.** `fef94857`; ChatGPT 5901837851 at that head: "ACCEPT as the complete bounded
  correction-delta package"; earlier reviews listed in OC `STATUS.md`:28–49.
- **Remaining gates.** G1 above.
- **Relation to this package.** OC lands first and carries no Bell-package file. After G2, OC's
  `STATUS.md` remediation rows D2 and E2 (OC `STATUS.md`:162, :164) name records then on `main`;
  OC's statements stay conditional as written (NOTES-PLAN OQ-13).

***

## 4. #1269: determination

**Determination: QH's cited material does not need preservation for this package. It stays off
`main`, identified in the ladder's STATUS note as non-load-bearing context.**

Reasons:

1. **The ladder's own classification.** LD:300 classifies QH as provenance for stage 4 and as an
   illustration for stage 7 "on which no verdict rests".
2. **Stage 7 does not use it.** UNDETERMINED needs no positive witness. Its support is that quantum
   Bell tables are unreachable under stages 0–6 (stage 5, BS), that the relaxed class reaches PR
   (Main:360; check 2 for the measurement-dependent branch) and that no selector is supplied (N4,
   OC:509; Main:360's general sentence and Main:416 for the measurement-dependent branch). Deleting the QH sentence at LD:104
   leaves the classification and its support unchanged.
3. **Stage 4 does not use it.** NOT FORCED rests on `φ_0` with `μ_MD` (LD:150–153). That settings
   are configuration content rests on Main:42 and OA1:111–112 on `main`; QH:213–214 illustrates a
   supplied controller.
4. **No other package record uses QH.** BS cites a session copy of QH r2a as "Provenance only"
   (BS:437); SB does not cite QH; OC cites QH r3 (V) only through the reconciliation's reading of
   L3 (OC `DEPENDENCIES.md`:23), which becomes moot once L3 itself lands.
5. **Necessity, not exposure (§A.42 item 5; §A.28).** Preserving QH would add 57 files, including
   byte-preserved ASSESS-868 files with three SC-42 added-text hits and an off-`main` support chain,
   for a sentence no verdict uses.

**How LD:300's reference is classified.** The stage-7 sentence "The native encoded U′ composite
reaches the non-quantum table SWAP/2 (QH:68–97) [D]" is a statement that uses QH's result, so §A.42
item 8 classifies it as support off `main`; relabelling it does not make it provenance. It remains
support off `main`, landed as owner-identified non-load-bearing context (#868 c.6873193841).
`STATUS-LADDER.md` states it with QH's own conditions: the result is conditional in QH on NNB and on
the supplied posits P2 and H-PREP (QH:68, :85–86, :212, :215), is model-reviewed and is not verified
from `main`; stage 7's classification rests on Main:360, Main:416, check 2 and N4 and does not use
it. The accepted text is unchanged, and no ladder r4 is written (#1169 c.6865177667: "Do not write
narrowing revisions just to unblock integration"). NOTES-PLAN OQ-6 asks the owner whether the merge
decision should also record it under §A.42 item 8's final sentence as a named claim left
unsupported.

QH keeps its own PR (#1269) and its own landing question under #868. Nothing in this plan prejudges it.

***

## 5. Composition of the combined package

### 5.1 Records landed byte-identical, by merge of their accepted heads

Directory `…/drafts/bell-scope-868-20261111/` from `e1534b08`:

| File | Blob | SHA-256 | Lines |
|---|---|---|---|
| `BELL-SCOPE-UNIT1.md` | `5814e479b16929fe8ab045a3f3b8fc4987704633` | `dd7115511e332b1cae20bdda7c3d94ec7f8af20bbd436750d7e6dfccbf078913` | 472 |
| `DISPOSITIONS-r2.md` | `dd8cbc8c5c29ad28d175cbb67dcf23454fc3915a` | `d3a185181747877f2ef977c2be735b0e8b705164b4bfff7ec8635e4808e08d2f` | 37 |
| `probes/generic_bell_checks.py` | `e47f3179b0bd4195d67091b1397490433c0316ca` | `83cecb183cf2a625cf5913b6e287350d514297e0cd94fc66ee8f264e7100b6d0` | 172 |
| `probes/generic_bell_checks.out` | `0798db766ba252dfb01d5622c43adfc8e9edbc6c` | `61deeddd35bedf5ad63b2e133c7067addf30e118f27103208f0965f2ed13e491` | 18 |

The probe lands with the record because BS:439 classifies it as a gap otherwise; its SHA-256 matches
BS:300.

Directory `…/drafts/bell-ladder-20261113/` from `d8e4f80e` (SHA-256 values equal `OBJECTS.md`):

| File | Blob | SHA-256 | Lines |
|---|---|---|---|
| `BELL-LADDER-r1.md` | `87a1971f22a17361ff71868d79925856863fdfef` | `468905ed9dfe7ab3c68fc338d85e07b4a28191afc3e84d9c51b97fcf9157b86e` | 284 |
| `BELL-LADDER-r2.md` | `e2ef1440cdf89bbad51f466b96e8161530df18e3` | `4b8e3a4867c98e9de65c2c004b05d1e74f9a80abce5b0b343fa0de3de8a71ccd` | 302 |
| `BELL-LADDER-r3.md` | `0298088d66547e0aa28b634bacae196991507a8c` | `6e7708ceda86b8121dad6904cbc6c8373e819c08985a481808168a9778ebb5a6` | 304 |
| `NOTES-r1.md` | `b49ee6a7c8b84112e196d144920555cc79bfae69` | `24a304a4eae0801c9522f045e0c786908e02f26b0738e04601f86d6aa9c4acdd` | 77 |
| `NOTES-r2.md` | `97ea8701481ee84b7c80d4204f1fb8bbb8cc014a` | `dd8ee90594f1f17050e7711f15b6853c998fb16eccab841b87873418a0443188` | 105 |
| `NOTES-r3.md` | `963d73523b2449d1674dbd0e6b9f000a7de5e351` | `831554fb18221422e947d6e08735c709d51cdc4a36558634d1a2c5c82a9e7792` | 110 |
| `REVIEW-r1.md` | `c84142dca0b7f554ddb5a449a1698399557a1fef` | `746171e9f5864e1e1ce29426d692d11ff870331c500278914ac0cafe1e6460ef` | 335 |
| `RESPONSE-r1.md` | `fe6301a93f25154681f5079b6d971f1e2cd45327` | `496a2f7b8e9ffd02a1e09b2f950d5580fbbee31b5bcbf27985e93fc4d0077294` | 28 |
| `CONFIRM-r2.md` | `0a629d501c2ee6c752e685b2b881b007acb0430e` | `c68dd910cc47958af481f3798aaac60f9978d332c564abe8223bfb1f9e8ea2f2` | 120 |
| `RESPONSE-r2.md` | `23dc97b1979fca2ce523d073c2a5a6802909a42c` | `e02e0928448db560decc67cf2a0a0b60a70ae8407f897899f9f8b58d76c610c2` | 21 |
| `CONFIRM-r3.md` | `c968776a8c082cc9f685dfa736d79f85f454ce6e` | `5f5e9e4562c2de4313c3114fba23cc7dc90563ff1c2e297577dadaffe51bfaaa` | 50 |
| `OBJECTS.md` | `c2eab16700a69af64132223d655654ad802ab416` | `9be5d5cc1a5577788032cc0fd0bef345bd7a8c6f1d37004c121e8c64883e807b` | 17 |

All twelve land: r1, r2 and the NOTES are cited by the reviews and confirmations by line, and r3
cites NOTES (LD:240, :274).

### 5.2 New files written in G2

| Planned path | Content | Source |
|---|---|---|
| `…/substate-bridge-l3-<date>/SB-L3.md` | S:167–171 copied verbatim and fenced as a quotation. Every non-verbatim line is marked as an addition: the pin block; hypotheses from BS §3.1–3.2; a resolution table for the in-text references (Main:364 → Main:362; Theorem N and (Sep) → BS @ `e1534b08`; B1 → its record on `main`; SB §6 → provenance; S5 → provenance, not support, because S5's response tables already factorize and its check cannot fail); the N′ composition (BS:190); the support-layer paragraph. | `SUBSTATE-BRIDGE-UNIT1.md` @ `86a413c8` (blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`, SHA-256 `662b9cbaab4237a357174b675c7ee7734c4d4512ef68d530555111230bde48fd`), lines 167–171 |
| `…/substate-bridge-l3-<date>/STATUS.md` | from `STATUS-SB-L3.md` here | this plan |
| `…/drafts/bell-scope-868-20261111/STATUS.md` | from `STATUS-BS.md` here | this plan |
| `…/drafts/bell-ladder-20261113/STATUS.md` | from `STATUS-LADDER.md` here | this plan |

Optional, by owner decision (NOTES-PLAN OQ-13): a forward note in OC's `STATUS.md` (then on `main`)
naming the landed records for its rows D2 and E2, keeping OC's "conditional on L3" and "conditional
on L2 and Theorem N" wording and changing no status of OC.

### 5.3 Not in the package

The SB draft directory (all four files at `86a413c8`); SB's probe files (S5 provenance, §2.4); every
QH file (§4); REC-1 (#1268), cited by the ladder as provenance only (LD:301); this plan directory,
which is a planning record (NOTES-PLAN OQ-11).

### 5.4 Mode and checks

- **Mode.** One pull request; merge commits of `e1534b08` and `d8e4f80e` into a branch from `main`
  (new directories only, so no conflict is expected); one commit adding §5.2; landing by merge
  commit, so `7abf59d7`, `e1534b08`, `b8096c79`, `c4781c93` and `d8e4f80e`, which the reviews name,
  stay ancestors of `main` (§A.42 items 2–3).
- **Checks at the package head.** `tools/claims_check.py`, `tools/staleness_check.py`,
  `tools/voice_check.py`, `tools/artifact_placement_check.py`, `python3 tools/legacy_records_check.py
  <head>`, the SC-42 integration check with its `cmp` against `sc42-integration-result.json`, and
  exact-head CI. A replay of `generic_bell_checks.py` from the package head with a byte comparison to
  its `.out` is a computation and needs its own authorization (NOTES-PLAN OQ-8).

***

## 6. §A.42 item 8: every off-`main` reference, classified at package landing

Classification after G1 and G2 (OC and the package on `main`). "Package" means the reference's
content lands in the same merge.

### 6.1 References made by the ladder (LD)

| Reference | Attached to | Classification at landing |
|---|---|---|
| BS @ `e1534b08` (Theorem N, N′, (Rec), §4 bound, §4.2, §3.5 item 5, BS:156, NBA) | §0, stages 4–6, AL (AL4) and conclusion, §5 | **support on `main`** (package; blob `5814e479` unchanged) |
| BS Lemma G (LD:298) | none (listed only) | provenance |
| SB @ `86a413c8`, L3 (S:167–171) | §0 (directed (Sep)), stage 3, check 4 | **support on `main`** in `SB-L3.md` (package); difference: Main:364 re-pinned to Main:362 |
| SB routes A/B/C, route C (S:177–181) | §0 (LD:75–76), §4 consequence (ii) | **support on `main`** in OC:490–494; difference: OC Δ1, Δ12 (routes anchored on Main:412, :414) |
| SB N3 (S:189) | §2 check 1, §5 NBA row | **support on `main`** in OC:508; difference: Δ1, Δ13/Δ14/Δ20 wording |
| SB N4 (S:190) | stage 7 (LD:104), §5 (LD:271, :284) | **support on `main`** in OC:509 at N4's scope (MI-kept routes); difference: Main:362 → Main:360 (Δ1). The measurement-dependent part of LD:104 rests on check 2 (LD:150–153), Main:360's general sentence and Main:416; the attainment clause of LD:271 is ladder text not supported by N4 (§2.5) |
| SB L4 | not cited (LD:299) | its content for (vii) is Main:362: support on `main` |
| SB:220 (resolution at which masking fails) | §5, example of a prediction an escape would need | provenance (example; no verdict uses it) |
| QH @ `ffc9cda4`, QH:213–214 | stage 4, §5 row | provenance |
| QH @ `ffc9cda4`, QH:68–97 | stage 7 sentence | **support off `main`, landed as owner-identified non-load-bearing context**, stated with QH's conditions in `STATUS-LADDER.md` (§4 above; OQ-6) |
| RC @ `9f7d2612` (vocabulary, C9, C10, H-xiv, `D_0`) | vocabulary, §5 pointers, a name | provenance (LD:301); the Q1/Q2 vocabulary is also restated on `main` in OC §0.1 |
| ladder commits `b8096c79`, `c4781c93`, `d8e4f80e` | review objects | on `main` once merged by merge commit |
| #868 c.6854708572, c.6794392080; #1273 c.6860580909 | authority; mixed-path unit; owner Q1–Q4 | governance provenance |
| reviews 5857227567, 5857981727, 5858000929, 5859960068, 5891666660, 5897397957, 5891524305, 5892919040 | input status | provenance (§A.46 item 7) |
| NOTES-r3 references (fetch commands, RC head `cd38655c`, obsmu Proposition C, OA-3) | working notes | provenance |

### 6.2 References made by BS (BS:419–441)

| Reference | Attached to | Classification at landing |
|---|---|---|
| `papers/Main.md`, `papers/Substratum.md`, `papers/SM.md`, `book/ch18-beyond.md` @ `cac5d264` | C1, C2, C8, C10, C13, O1–O3, F1, F2 | support on `main` (`cac5d264` is an ancestor); drift stated in `STATUS-BS.md` |
| `composition-source-map.md` @ `017ae88e` | §2 rows, §3.4 | support on `main`, difference stated by BS:430 (author label, line 5) |
| `prepared-pair-source.md`, `two-system-interface.md`, `NO-SIGNALLING.md`, h-bell preregistration @ `cac5d264` | C9, §0, §2 | support on `main`; unchanged from `cac5d264` to `c3b5f37a` |
| #1210 QX-6 r7c @ `4c7f3f86` | A6.1, A6.4 comparisons | provenance (BS:435) |
| session copies of ASSESS-868 r3a, Q868H r2a, LIT-SURVEY | context | provenance (BS:436–438); ASSESS-868 r3a is byte-preserved on #1269's branch, still off `main` |
| `probes/generic_bell_checks.py` | X tags G1–G7 | lands in the package; **support on `main`** once the owner ratifies the run as covered (OQ-8(a)), otherwise provenance, with the tagged results resting on their arguments [A] |
| r1 at `7abf59d7` | review object | on `main` once merged |
| #868, #1169, #914, #866, #1216 comments; review 5857227567 | authority, scope | provenance |
| [L] Wharton–Argaman, Barrett–Collins–Hardy–Kent–Popescu, de Broglie–Bohm | context in §2, §3.5, §6 | provenance; no claim rests on them |

### 6.3 References made by `SB-L3.md` and the STATUS notes

| Reference | Classification at landing |
|---|---|
| `SUBSTATE-BRIDGE-UNIT1.md` @ `86a413c8` | provenance: the copied content is in `SB-L3.md` |
| `generic_substate_checks.py` S5 @ `86a413c8` | provenance (§2.4) |
| #1271 R3:66 | provenance |
| #1283 @ `f57e576a` | provenance until adopted; the basis then cites the adopted §A.46 on `main` |
| owner comments (#868 c.6873193841, c.6854708572, c.6791565399, c.6791606126; #1169 c.6854728636, c.6855167580, c.6865177667; #1273 c.6860580909) | governance provenance, quoted in the notes |
| #1284 @ `6e2d1ee8` | provenance (format precedent) |
| `LANDING-PLAN.md`, `NOTES-PLAN.md` (this branch) | none after the replacements of review B1: the STATUS notes cite neither file; provenance |
| BS-tagged items in `SB-L3.md` (Theorem N, (Sep)) | support on `main` (package) |
| "B1's static bit" (S:171) | Model B1, `verification/programmes/substratum/recursive-substates/README.md`:23 on `main`; support on `main`, resolved in `SB-L3.md`'s reference table (B1's hidden sequence is infinite, so it falls under the finite-depth limit of `STATUS-SB-L3.md`) |
| SB §6 (S:171) | provenance; not carried |

No reference other than LD:300's stage-7 sentence, which lands as owner-identified non-load-bearing
context (§4), is support off `main` at landing, provided G1 has landed OC.
If G1 does not land, the ladder's routes, N3 and N4 references become gaps and the package cannot
land as composed.

***

## 7. #1283 item 8 conditions, record by record

For records landed after adoption, #1283 item 8 requires every one of its five conditions. The table
checks each condition record by record. The historical-authorization row is recorded as provenance;
it is a condition only for pre-adoption records under the reconciliation sentence.

| Condition (#1283 item 8) | BS | SB L3 (carried) | LD |
|---|---|---|---|
| substantive, nonredundant result | met: Theorem N/N′ (closed native form; `main` carries only the exogenous form, Main:364–389), §4 mean-TV and full-history forms, attainment in 𝒞_sep | met: the directed form of (Sep); not on `main`; excluded from OC (OC:641) | met: Proposition AL (no two-wing coset result with an NS hypothesis on `main`, NOTES-r3:70–74) and the ladder classification |
| scope and limits documented | met in BS §0, §1, §4.4, §8 and `STATUS-BS.md` | met in `STATUS-SB-L3.md`; `SB-L3.md` to state them | met in LD §0, §4 scope limits, §5 and `STATUS-LADDER.md` |
| non-author review; ChatGPT exact-head review | ChatGPT exact-head 5857981727 at `e1534b08`; a separate non-author review: **not recorded** (OQ-2) | ChatGPT reviews of SB at `b94b283a` and `86a413c8`; the carried text and its N′ addition (§2.5): **not yet reviewed** | met: `REVIEW-r1.md`, `CONFIRM-r2.md`, `CONFIRM-r3.md`; ChatGPT 5892919040 at `d8e4f80e` |
| landing checks and §A.42 item 8 tracing | tracing: §6; checks: pending at the package head | as BS | as BS; the STATUS note itself needs the package's ChatGPT exact-head review |
| accountable Issue, verification status, remediation plan | #868; `STATUS-BS.md` | #1169; `STATUS-SB-L3.md` | #868; `STATUS-LADDER.md` |
| explicit rationale | support for the ladder; puts on `main` the Theorem N on which OC's narrowed row E2 is conditioned | support for the ladder's directed (Sep); puts on `main` the argument on which OC's narrowed row D2 is conditioned | the owner's stated preference in c.6873193841 |
| separate owner merge decision | **not recorded** | **not recorded** | **not recorded** |
| historical authorization (provenance, not an item-8 condition for a new landing) | #868 c.6791565399, c.6791606126 | the 2026-11-11 SB approval not located (OQ-7) | #868 c.6854708572 |

***

## 8. What this plan does not do

It commits, pushes and posts nothing; edits no input record, manuscript or frozen record; runs no
computation; and adopts no reading of ledger items (vii), (x) or (xiv) beyond the owner's recorded
decisions. It changes no review verdict and no classification of any input.

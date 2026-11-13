# Focused confirmation of the #1169 synthesis r2

**Verdict: ACCEPT WITH CHANGES (small).** All five blockers of REVIEW-r1 (F1–F5) are resolved.
F6–F21 are resolved as RESPONSE-r1 states. The delta table accounts for every diff hunk, and no
other line changed.

Four residual items need text edits, C1–C4 below. Two of them, C1 and C2, come from wording I
proposed in REVIEW-r1 (F2's (1b′) and F8's dependency line). The writer applied that wording
faithfully, and it was inexact. None of the four changes the order in §1. A check of the diff is
enough to confirm them; no further full review is needed.

**Object.** Branch `research/synthesis-1169-20261113`, fetched by name with full history, at head
`65b70b2d7f134a041e9d915208c0e7bb98ccd14f`.
- Its parent `71253fd4` adds `REVIEW-r1.md`, which is byte-identical (`cmp`) to the review as
  delivered.
- `65b70b2d` adds `SYNTHESIS-r2.md` (765 lines), `NOTES-r2.md` and `RESPONSE-r1.md`.
- `SYNTHESIS-r1.md` and `NOTES-r1.md` are unchanged.

"r2:n" is `SYNTHESIS-r2.md`, "N2:n" is `NOTES-r2.md` and "RESP:n" is `RESPONSE-r1.md`.

**Tools.** `tools/artifact_placement_check.py` OK. `tools/legacy_records_check.py 65b70b2d…`: 303
records intact. A manual scan of the three new files for the §A.32/§A.33 phrase families finds
nothing in `SYNTHESIS-r2.md`; the only hit is in the working notes. Nothing was committed, pushed or
posted.

***

## 1. Delta table and scope

- `diff SYNTHESIS-r1.md SYNTHESIS-r2.md` has 55 hunks. Each appears in RESP:49–103 with matching
  r1 and r2 ranges, in order. No hunk is missing and no row is spurious.
- The RESPONSE line references were spot-checked at F1, F4, F6, F12, F15, F17, F18 and F21, and
  they point to the stated text.
- r8 claims (r2:25–29, :36, :40–41) were checked:
  - `REC-1-r8.md` has blob `615b7de8` at `2a9f10ba`.
  - R8:297–303 states the literal L reading.
  - The r7→r8 hunks are 1c1, 14c14–18, 289–290c293, 293a297–303, 299–300c309–310 and 320–321c330.
    The insertion after r7:293 belongs to the first passage's bullet, so "differs only in its
    header and the three passages" holds.
  - The +4 offset for r7:15–288 holds.

## 2. Findings F1–F21

| F | Resolved? | Note |
|---|---|---|
| F1 | Yes, with C1 | The variation (cite (1b′), not gap 1) is sound: after F2, gap 1's holding problem is a disjunction, so (1b′) is the right support. But (1b′) itself needs C5 (C1). |
| F2 | Yes, with C1 | The two-label variation in §1 (r2:108) matches the owner plan better than my "one disjunct" cell; §0 r2:74–80 defines absence and disjunction as non-labels. (1b) and (1c) are correctly stated (r2:145–158). |
| F3 | Yes | r2:115, :208–212, :341–352, :465–467, :493–494. |
| F4 | Yes | r2:217–225, verbatim. |
| F5 | Yes | r2:550–560; N2:83–87. |
| F6 | Yes | r2:246. All five identifiers verified at their lines. |
| F7 | Yes | r2:109, :275–281, :290, :293–296, :305–309; T6 at r2:600–602. |
| F8 | Yes, with C2 | The "independent" wording is gone. (4d) is a fair placement of OA2:587–604, but its wording (and the dependency line r2:489, from my F8 text) mixes hypotheses kept with exits that drop them (C2). |
| F9 | Yes | r2:112, :200–202. |
| F10 | Yes | r2:113, :321–328, :461–463, :491; T7 at r2:603–604 (nit N2). |
| F11 | Yes | r2:456–457, :487–488. |
| F12 | Yes, with C3 and C4 | The metric is explicit, and the counts were checked (§3 below). |
| F13 | Yes | §8 has one row per reference (r2:705–739). Each row's classification matches the use in the text: the APPROX, SB L3, BS N/N′ and 3A gaps are present, and QH and OICORE-1 are unused. |
| F14 | Yes | r2:632–635, :646–663; SQ1–SQ9 at r2:669–695. |
| F15–F21 | Yes | Verbatim or as specified at the cited r2 lines. |

## 3. The metric and the count table (r2:86–103, :421–476)

**Fixed in advance?**
- No commit history can show this. The metric, the targets and the counts all enter in one commit,
  and N2:51 only asserts that they came in that order.
- What can be checked is that the metric is applied uniformly. Every entry's sub-forms are bundled
  under the entry (MM-1's (1a)/(1b′), MM-4's (4a)–(4d), MM-3's 3a–3e), and the top rank is reported
  as metric-relative with the choice left to the owner (r2:475–476, SQ8). That is an acceptable
  treatment.
- The sensitivity analysis, however, is not applied uniformly (C4).

**Cell by cell.** Each cell was checked against the entry and the source it cites.

| Cell | Check |
|---|---|
| MM-3, T4 (3b(iii)) | Supported. NL-C′ (S4:464–474) makes control-region growth necessary for T4. The same NL-C′ also underlies MM-1's T4 cell (1a). These are two different necessary conditions from one proof, not one condition counted twice. |
| MM-3, T5 (3c, 3d) | Supported. Corollary B′ for `R` injective on `W` (OA2:244, :317–320); Corollary E1 with (H4), (SP), (xiv) (OA2:587–589). |
| MM-3, T6 (3a, 3b(ii), 3e) | Partly supported (C3). T6 is defined at r2:92 as "OA-1's qubit tier: phases and dense control on a qubit". OA-1's qubit tier is T-P, T-C, T-M and T-R at `(ε, K)` (OA1:488–496); phases and dense control are the kernel ceiling that fails it (OA1:474). 3a supports T6. 3e supports T-M on route E_f. 3b(ii) (Main:558) concerns exact reproduction at all precisions, which a target at `(ε, K)` does not demand (Main:562: bounded envelopes to any finite accuracy). The count stays at three targets, so the rank is unaffected. |
| MM-1, T1 (1b′) | Supported once C5 is added (C1). |
| MM-1, T4 (1a) | Supported (TS F-S2; S4:465–468; P:143, :184–199). |
| MM-1, T2 (1c) | Supported as a disjunct (R7:196–200; OA1:522). |
| MM-4, T3 (4a) | Supported (OA1:176–189, :523). Scope: one affine `φ`. |
| MM-4, T5 (4d) | Supported as a disjunct once its wording is fixed (C2). |
| MM-4, T7 (4c) | Supported as a disjunct (BL:78–83, :261–263). |
| MM-7, T7 | Supported. With MI kept, a violation runs through parameter dependence (OC:471–473), and PPS:136–145 then requires restricted span (finite `Λ`). |
| MM-8, T8 | Supported, by definition, relative to the unrestricted class (r2:393–394). |
| MM-2, T1, T2, T4 (disjuncts) | Supported (OA1:522; R7:196–200; TS:380). |
| MM-2, T5, T7 (load-bearing) | Supported (P0:417–422 with N8.2(b); OA3:418–493; BL:249–253). The T7 cell is load-bearing for what counts as T7's no-signalling, since the selected-read PR box does not meet complete-history NS. |
| MM-5, T7 | Supported (BL:78–83). |
| MM-9, MM-6 | Correct. |

The tie rule (MM-7 before MM-8, because T8 presupposes T7) is applied correctly. The route-B
exclusion at r2:436–437 is consistent with T7 being the target.

## 4. Residual items

### C1 (Medium). (1b′) and the MM-1 ranking reason omit C5

- **Where.** r2:108, :142–144, :442–443, :518; N2:61–62.
- **Evidence.**
  - The step behind (1b′) is OA1:345–347: "Under μ-G, for a hidden carrier, `y_i` is uniform and
    independent of everything held **(D2)**, so `m` is uniform unless a ready-cell supply fixes
    `y_i`."
  - D2 needs both μ-G and "held = a function of present `V`" (OA1:149).
  - OA-1's verdict on the same node is "a **retention** failure … MP-0a resolves it classically …,
    and so does MP-0b" (OA1:353–355).
  - The rank reason at r2:443 cites OA1:526–529, which itself reads "only under … μ-G and the
    held-equals-present-`V` convention".
  - The wording "under R-lin and μ-G" without C5 is mine (REVIEW-r1, F2), and the writer applied it
    as given.
- **Fix.** Replace "under R-lin and μ-G" with "under R-lin and μ-G with C5 (held = a function of
  the present `V`)" at r2:108 (label and tied-to cells), :142, :144, :443 and :518, and in N2:61.
  At r2:143, after "(OA1:522)", add "; the step uses D2, so C5 is part of the interface
  (OA1:345–347, :149)".
- **Effect on the count.** None. Within the interface R-lin + μ-G + C5, fixing `y_i` needs a ready
  cell on its own (the alternative SA-1(c) is also a ready cell). MM-2's T1 disjunct concerns the
  holding step, not the write.

### C2 (Medium–Low). (4d) and the dependency line state a vacuous premise and mix kept hypotheses with exits

- **Where.** r2:297–300, :489.
- **Evidence.**
  - "With (H4), (SP), (xiv), H-AR, (H1) and (H3), a G3 escape needs leaving (H1) ∧ (H3)" assumes
    (H1) and (H3) and then requires leaving them. OA-2 records exactly this wording as vacuous and
    replaced it (OA2:593–594).
  - The "other exits" listed from OA2:600–604 are exits with (H1) and (H3) kept. Each drops H-AR,
    (H4) or (SP), which the sentence has just declared kept.
  - The dependency line at r2:489, "MM-3d (with (H4), (SP), (xiv), H-AR) → MM-4 ∨ supplied control
    ∨ the OA2:600–604 exits", has the same mix. That line is my F8 text.
- **Fix.**
  - Replace r2:297–300 with: "**(4d) A G3 escape for an H-AR observer of the affine class.** Under
    (H1), H-AR and (H3) settings act by translation (Theorem E(a)), so with (H4), (SP) and (xiv) kept
    a G3 escape needs leaving (H1) ∧ (H3): MP-1 (a non-affine rule) or supplied P3/E-iso (OA2:587–
    592). Keeping (H1) and (H3) instead and dropping H-AR, (H4) or (SP) leaves the case open
    (OA2:600–604). The non-affine update is one disjunct."
  - Replace r2:489 with: "MM-3d (with (H4), (SP), (xiv), H-AR kept) → MM-4 ∨ supplied control;
    with (H1), (H3) kept, the open exits are dropping H-AR, (H4) or (SP) (OA2:600–604)."
- **Effect on the count.** None. MM-4 stays a disjunct for T5.

### C3 (Low–Medium). T6 does not match OA-1's qubit tier, and 3b(ii) is cited for it

- **Where.** r2:92, :426.
- **Evidence.** See §3, the MM-3 T6 row:
  - OA1:488–496 defines the qubit tier at `(ε, K)`.
  - Main:558 is an exact, all-precision obstruction, and Main:562 states that finite carriers reach
    any finite accuracy.
  - 3b(i) bears only on exact T-C ("Exact T-C … needs growing carriers", OA2:351–353).
- **Fix.**
  - r2:92: "T6, OA-1's qubit tier at `(ε, K)`: T-P, T-C, T-M, T-R and D (OA1:488–496)".
  - r2:426, MM-3 T6 cell: "T6 (3a; 3e on route E_f for T-M; 3b(i) for exact T-C, OA2:351–353)".
    Drop 3b(ii) from the cell, or state it as an exact all-precision variant that is not counted.
  - The key stays (3, 0, 0).

### C4 (Low–Medium). The "MM-3 unbundled" sensitivity unbundles only MM-3

- **Where.** r2:470–471, :691–692; N2:57–58; RESP:30.
- **Evidence.**
  - The primary metric bundles every entry's sub-forms. The alternative splits only MM-3's sub-rows
    and keeps MM-1 ((1a), (1b′)) and MM-4 ((4a)–(4d)) bundled. The result "MM-1 then ranks first
    (r1's top)" depends on that asymmetry.
  - Unbundled uniformly, using the r2 cells, 3b has key (2, 0, 0) and ranks first. Next, at
    (1, 0, 0): 1a, 1b′, 3a, 3c, 3d, 3e, 4a, MM-7 and MM-8. MM-1 does not rank first.
  - After C3, 3b's key depends on whether 3b(i) counts for T6.
- **Fix.**
  - Restate the alternative as "every entry unbundled". Give the resulting top, which is 3b, or 3b
    tied with the other single-target sub-forms after C3, and drop "MM-1 then ranks first (r1's
    top)" and "r1's order is recovered".
  - If an MM-3-only split is kept as a third alternative, label it as such.
  - Update SQ8 (r2:691–692) and N2:57–58 to match.

## 5. Nits (optional)

- **N1.** A6 (r2:566) cites the passages as R7:287–290, :299–300, :320–321, while r2:41 says
  r7:289–290. The changed lines are r7:289–290, plus the insertion after :293. Use one form.
- **N2.** T7 (r2:604): "state that E2 and E(b) need (xiv), not a coset law" → "list (xiv), and no
  coset law, among the hypotheses of E2 and E(b)". BL:237 says this for E2 only; OA2:528 lists E(b)'s
  hypotheses.

## 6. New text: no new overclaim apart from C1–C2

- **(1b′).** Correctly sourced to OA1:522 and :342–348, and correctly labelled the only
  necessity-type form under μ-G. It needs the C5 scope (C1).
- **(4d).** Correctly a disjunct. It needs the hypothesis wording fixed (C2).
- **T6.** States a naming difference, not an error in BL or OC. "Outside (vii)" remains a valid but
  weaker necessary condition, and T6 does not say otherwise. Sourced at BL:81, :261, OC:479, BL:190
  and OC:441–444. No overclaim.
- **T7.** Correct for E2 (BL:236–237) and E(b) (OA2:528–537). It is carried as a tension and as
  SQ9, not as a correction to BL. Nit N2 only.
- **Ranking.** The new order and its counts claim nothing beyond the entries. §5 (r2:532–534)
  scopes the ranking to the metric, and SQ8 leaves the choice to the owner.

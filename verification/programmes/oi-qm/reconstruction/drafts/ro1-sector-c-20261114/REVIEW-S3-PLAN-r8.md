ACCEPT WITH CHANGES — `S3-PLAN-r8.md` at `02ca83a50a249592da2b466d89cfc00ec5614b6b` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused confirmation of the S3 plan, r8

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r8.md` and `RESPONSE-S3-PLAN-r7.md`. The copies supplied to me are identical to the
  committed files.
- `S3-PLAN-r7.md` is unchanged, and `REVIEW-S3-PLAN-r7.md` is preserved as delivered.
- The full diff from r7 to r8.
- At source on `main`:
  - MR-1 `preregistration.md`:486–491, 556–562 and 572;
  - `amendments/MR-star.md` §M.6 (ll. 1018–1075) and §M.9 (ll. 1174–1188).

**Line numbers** are r8's.

## Summary

- **The requested items.** R10(a), R10(b) and R11 are resolved, and the S-L3 sweep is complete.
- **One finding remains, and it is not a nit.** It comes from the CC5 check the coordinator asked
  for. The error behind it is mine: it originates in my r1 review (F2).
  - The plan says the classical controls M-1, M-2 and M-3 are "specified at class level" only.
  - In fact MR★ §M.6 on `main` gives full instances of all three.
  - Their status is what needs labelling, not their specification.
- The correction is local (R12). Apart from it, only one optional point remains.

## 1. R10 and R11

- **R10(a): resolved (ll. 634–642).**
  - The status cites `MR-star.md`:1297–1300 and `stage1-log.json`:773 ("relayed by the
    coordinator"). It records that no review artifact for `fc68d333` is on `main`, and cites §A.46
    item 7 and O-OBSMU `ANALYSIS.md`:485–489.
  - It concludes: "S-L3 enters here as a named premise, not as a sourced disproof".
- **R10(b): resolved (ll. 643–665).**
  - The full scope is stated: K1; S-L2, quoted at `MR-star.md`:511–513; the budget below recurrence;
    `a` injective with a nonempty neighbour relation; and S-C1(a).
  - The case does not count toward (a′) until S-L3 is re-checked under the U1 criterion and
    independently verified.
  - SNR-1 gains the general rule (ll. 761–765), and (a′) (ll. 778–780) and the U4 row (l. 841) carry
    the same condition.
- **R11: resolved (ll. 803–806).** The gating sentence names (b′), as OB-a1 (#866, #1169).
- **The revision-note history (l. 57):** "named NC-1 in r6 and renamed SNR-1 in r7". Accurate.

## 2. The S-L3 sweep

**Complete.** I grepped r8 for "S-L3"; it occurs on 24 lines.
- The sites that state its status (§8.2 l. 493, Point 2 l. 536, D-1 ll. 629–669, SNR-1 l. 765,
  (a′) l. 778, U4 l. 841) all treat it as a named premise and condition its use.
- The remaining hits are the verbatim quotation of the #1023 GAP (ll. 191, 466) and the revision
  notes. None treats S-L3 as verified or sourced.

**Optional.** "Independently verified" (l. 662) has no assigned home. Name one, for example an
independent paper check routed to #866 (O-REC/MR-1), or say it is not authorized here.

## 3. The CC5 claim at source

**R12 (required). The classical controls are fully specified on `main`, as named premises. The
plan's "class level" statements are inaccurate, and its new CC5 sentence is unlabelled.**

**What the source says.** MR★ §M.6, "the frozen stage-2 interface", on `main`, gives full instances:
- **CC5.** "A classical eraser. Markers `m_j = (a_j, b_j)`. `MK_j(1)`: `a_j ← a_j + p`; draw a fresh
  `e`; `k ← k + e`; `b_j ← b_j + e`. `RD_j(0)` reads `a_j`; `RD_j(π/4)` reads `b_j`. `MK_j(−π/2)` is
  unavailable. GNC by Lemma G(i)". Its reference behaviour: "no W1; T4's conditional masses sum to
  the marked law" (`MR-star.md`:1067).
- **CC4.** The Catani et al. field (`MR-star.md`:1066). This is M-1.
- **CC7.** "Classical dephasing with no record … GNC by Lemma G(i)" (`MR-star.md`:1069). This is M-3.
- **All three on a common carrier** (ll. 1044–1056), with the reference result: "PC-Q, CC1, CC4, CC5
  and CC7 pass every applicable row" (l. 1180).

**Their status.**
- These are paper instances, and their properties ("GNC by Lemma G(i)", the reference behaviours)
  are paper claims in MR★.
- The only record of their verification is the same MR★ report used for S-L3: the review of
  `fc68d333` "verified … Lemma G and the countercontrol checks" (MR-star.md:1297–1300).
- So, by the reasoning of R10(a), they are **named premises** (§A.46 item 7).
- What MR-1 stage 2 adds is *executing* them as controls. The README says: "It stands only if a
  controls-only stage 2 … returns every reference result". Stage 2 does not *specify* them.

**Where the plan is wrong.**
- **ll. 499–500:** "They are specified at class level in MR-1, and their full specification needs an
  MR-1 stage-2 authorization".
- **ll. 721, 726–728:** the table header "Specified at class level in MR-1", and "(iv) once
  specified" in the M-1, M-2 and M-3 rows.
- **l. 800:** "(e′) counts only where the generalized-noncontextual model it cites is fully
  specified. M-1 and M-2 are specified only at class level".
- **l. 865:** the stop "including the full specification of M-1 to M-3". The stop is moot, since the
  instances exist. Construction of *new* controls stays a stop.
- **ll. 667–669, new in r8:** "Conditional-fringe recovery is also reproduced by the classical eraser
  (CC5; M-2)". This is stated without a label.

**The error is mine.** It originates in my r1 review: F2 said "M-1 to M-3 … specified at class level
in MR-1". I had read the preregistration, not MR★ §M.6.

**Fix.**
- **Relabel M-1 to M-3** as "fully specified on `main` (MR★ §M.6: CC4, CC5, CC7), [R, record on main]
  named premises (§A.46 item 7). Their execution as reference results is MR-1 stage 2."
- **(e′)** then counts only once the GNC claims of CC4 and CC5 are independently verified, or
  confirmed by an authorized stage 2. Until then it is pending, at named-premise status.
- **The gating sentence (ll. 803–806)** can keep "an MR-1 stage-2 authorization, for (e′)", with "or
  an independent verification of the §M.6 instances" as an alternative.
- **The CC5 sentence (ll. 667–669)** gets the same label: "[R, record on main] CC5's instance
  (`MR-star.md`:1067) reproduces conditional fringes, with masses summing to the marked law, a named
  premise".
- **U4 may use M-1 to M-3** as on-record class-(iv) controls at named-premise status, as it uses M-7
  and M-8, without constructing anything.
- **The §9 stop** reads "constructing new controls", not "full specification of M-1 to M-3".

**Requirement A(iv) is unaffected**, and if anything strengthened: the on-record controls are now
M-7, M-8 and M-1 to M-3, the last three at named-premise status.

## 4. Other changes, and anything new

- **The diff.** It touches only the header, the S-L3 sites, SNR-1, (a′), the gating sentence, the
  U4 row and the CC5 sentence.
- **No new premise** and no authorization.
- **The conditional raw-direct-miss report** (ll. 655–665) is correctly conditional on the S-L3
  premise and on (α)–(δ) and (γ).

## 5. Verdict

**ACCEPT WITH CHANGES.**
- **Required: R12.** A status correction at ll. 499–500, 667–669, 721, 726–728, 800 and 865.
- **Optional:** a home for S-L3's independent verification.
- These are not nits only. R12 corrects a factual status statement that has stood since r2, and the
  error is mine. It is local, and once it is applied a diff check suffices before the plan goes to
  ChatGPT.

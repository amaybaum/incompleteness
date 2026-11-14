ACCEPT WITH CHANGES — `RO1-DEPS-r3.md` at `4fc3f4aad3fedb51ec295ae6aa43723b57fa0ea7` (`research/ro1-sector-c-1169-20261114`, PR #1294); base `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`.

# Focused independent check of RO-1 step 2, `RO1-DEPS-r3.md`

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**Files checked.**
- `RO1-DEPS-r3.md`, SHA-256 `aee284f2…5451d`.
- `RESPONSE-DEPS-r2.md`, SHA-256 `57b65605…70ee`.

The copies supplied to me are identical to the committed files. Also at this commit:
- `RO1-DEPS-r2.md` is unchanged;
- `REVIEW-DEPS-r2.md` is preserved byte-identical to the review delivered.

**Line numbers** are r3's.

## Summary

- **Verdict.** UNDETERMINED is supported.
- **The r2 review.** Every finding of the r2 review is resolved, except the central question, which
  is partly resolved.
- **One new error, which needs correcting.** It originates in my own r2 review. §5.1 says that the
  interface ceilings and the preparation limit "exclude quantum and non-quantum behaviour together".
  They exclude quantum operations but leave PR untouched (C1 below).
- **One reporting gap.** On track (c), the result that holds under global P-vii is not reported in
  the track's own table (C2).

Both changes are local. Nothing else blocks.

## 1. Disposition of the r2 findings

| r2 finding | Status | Check at r3 |
|---|---|---|
| F1, track (a) | **Resolved** | The chain is carrier → typing (S7) → (iv) → co-requisites (ll. 448–464). "First given a carrier and a typing" is stated (l. 461) |
| F1, track (b) | **Resolved** | Reference class (OB-b0) → C-1 → response rule → transfer (ll. 488–500) |
| F1, track (c) | **Resolved** | C-1 → two-wing interface and availability (S3, S6–S8, the "executes through `Obs`" criterion) → bound → enlarged `Γ` (ll. 516–533). The bound is third |
| F1, track (d) | **Resolved** | "Executable" defined → reading (S6) → checked construction (ll. 548–557). INSUFFICIENT's condition is labelled the ultimate goal (l. 537). Minor m2 |
| F2, X1–X4 | **Resolved** | §7.7 (ll. 570–580), with effects carried into S7 (l. 617), OB-a3 (l. 597) and OB-c1 (l. 602). Assessed in §3 |
| Central question | **Partly resolved** | §5.1 adds reuse with retention at the correct scope (ll. 363–378) and the one-interface requirement (ll. 380–382). Its first paragraph is wrong (C1) |
| R1 | **Resolved** | [A-inf] with the one-step argument (ll. 427–431, 453) |
| R2 | **Resolved** | l. 432 |
| R3 | **Resolved** | ll. 344, 347–350 |
| R4 | **Resolved** | l. 639. BH-02 REPORT.md:8, 16 is on `main` |
| R5 | **Resolved** | The (xiii) route is named, marked [P], and not claimed (ll. 482, 497, 593, 660) |
| R6 | **Resolved** | `QuasilocalAlgebra.lean`:1328, "THE ALGEBRAIC CAUSAL CONE", on `main` |
| R7 | **Resolved** | l. 635 |

The new citations were verified at source:
- `OBL-RO3-2-r2.md` §0 at `78089e5e` uses the posited linear rule (ll. 50–57 there);
- SEL-DISC-1 at `445b17f7`, ll. 9, 75, 145 and 186 (D3);
- SEL-EXCL-1 at `0ecfddeb`, l. 33 and §§3, 7;
- `DiscreteCompletion.lean`:45–48.

## 2. Required changes

**C1. §5.1 classifies two limitations as excluding non-quantum behaviour when they do not
(ll. 357–361; also l. 349).**
- §5.1 lists "the interface ceilings (D-iv, D-nonneg, on F₂)" and "the preparation limit (D-A8)" as
  limitations that "exclude both".
- **What the ceilings exclude.** They exclude operations that do not preserve the diagonal, or do not
  preserve nonnegative entries. The PR implementation of record is a bijection of configurations:
  `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-EXCL-1 l. 33). Its conjugation is a permutation,
  which is monomial and preserves nonnegative entries. On one carrier, a PR table is "an ordinary
  classical channel" (RO1-SPEC-r3 §7.4).
- **What D-A8 excludes.** It bounds entanglement from definite configurations and says nothing about
  classical correlations, PR included.
- **So these limitations exclude quantum operations and leave PR.** That is a third category. It is
  the worst case for the central question, not a neutral one.
- **The error is mine.** It originates in my `REVIEW-DEPS-r2.md` (central-question paragraph), which
  r3 reproduced.
- **Correct classification:**
  - *excludes both*: only D-ceil, under global P-vii and P-xiv, for separated wings on F;
  - *excludes quantum only*: D-iv, D-nonneg and D-A8;
  - *excludes neither*: access, capacity and retention as stated;
  - *partial discriminator*: retention with reuse, at §5.1's scope.
- **Consequences.**
  - The answer to the central question becomes stronger in the negative direction. The verdict does
    not change.
  - X4 is sharpened. The PR machinery already lies within permutation-level operations. The restriction
    that soundness needs therefore falls on the executability of settings and renewal (S3, #913), not
    only on the added coverage operation.

**C2. Track (c)'s finding omits what holds under global P-vii (ll. 514, 565).**
- §6 (l. 390) and R3 (§4) report soundness against PR "on F" for separated wings: D-ceil gives
  CHSH ≤ 2, which lies in the quantum set.
- Track (c)'s table and summary say only "Not shown".
- Criterion 4 asks that a stronger result be reported where it holds. Index the finding:
  - *under global P-vii:* sound for separated wings on F, at the cost of Bell coverage (track (b));
    nothing for wings inside each other's cone or with messages;
  - *under the scoped reading:* not shown.
- Step 1's dependence on C-1 is correct as it stands. It comes from `R*`'s requirement to keep 2√2
  (RO1-SPEC-r3 §7.3 test (b)), which is a coverage condition carried by K-X.

## 3. Cross-track compatibility (X1–X4)

- **X1** (l. 577). **Valid.** P-iv's measure on configurations (:54; :724 (iv)) and P-xiv's
  distribution of `Ω` (:724 (xiv)) cannot hold a superposed initial state. The non-aligned cut
  presupposes observables outside the configuration basis. It is correctly not independent of OB-a1.
- **X2** (l. 578). **Valid.** OBL-RO3-2 §0 is stated for the posited linear rule, and D-phaseQ for the
  reversible finite-range update.
- **X3** (l. 579). **Valid.** The same holds for the phases: a complex diagonal is not a bijection of
  configurations. "The added operation" therefore covers P-phase as well as P-mix if either is
  placed in `φ`. A clause would make this explicit (nonblocking).
- **X4** (l. 580). **Valid** and correctly scoped as [A-inf]. C1 sharpens it.
- **Not flagged: X5, the Bell analogue of X4** (nonblocking).
  - Track (b) reaches the quantum value through ontic remote-setting dependence: H-Bell (i), the
    adopted branch (:80).
  - That dependence, left unrestricted, is the mechanism of D-PR, "globally coupled setting-dependent
    hidden dynamics" (:360). PR meets H-Bell (i)–(ii) (l. 130 row; R4).
  - So the route that completes track (b) enlarges what track (c) must bound. Tracks (b) and (c) must
    be settled on one interface.
  - Track (c)'s step 3 carries this in substance ("K-X must then limit the form or extent of that
    dependence", RO1-SPEC-r3 §7.3). It should be named in §7.7.

## 4. Checks for new errors in r3

- **New premise.** None. P-super, P-phase, P-mix, P-CK and P-E1E2 stay inventoried and are barred as
  derivations (ll. 413–415). Adoption remains S10 (l. 620).
- **Conditional stated as established.** One borderline case:
  - **m4 (ll. 369–370).** "Under `Θ` … so this is a soundness failure for the same-seed
    implementation." `Θ` is proposed and not adopted (S8). Write "under `Θ`, if adopted (S8)". The
    executability condition is already stated in the next bullet.
  - The opposite error, a stronger result left unreported, is C2.
- **Defined treated as executable.** None found. §5.1 conditions same-seed reuse on S3 (l. 372).
  X4's enlarged `Γ` is stated under access closure as a requirement (l. 580). The positive evidence
  for track (a) is a sourced operation (l. 467).
- **First step confused with the ultimate goal.** None. Each track states its ultimate goal separately
  (ll. 437, 478, 504, 537), and rule 4 forbids counting the goal as a step (ll. 420–422).

### Minor

- **m1 (ll. 449, 497).** The carrier comes *first* on track (a) and *last* on track (b) (the transfer
  of D-cone). Both orders are defensible:
  - on track (b), C-1 is a consistency question that can be settled on F and then transferred;
  - on track (a), the question on F₂ is already refuted, so what is open is elsewhere.

  State this reason in one sentence, so the asymmetry does not read as an inconsistency.
- **m2 (ll. 546, 553).** Track (d)'s step 3 checks "every premise". That list depends on whether
  P-vii is global or scoped (OB-b0, OB-b1). Add the P-vii reading as a precondition of step 3, beside
  S6.
- **m3 (ll. 89, 650).** Stale labels: "Scope of r2" and "Not inventoried in r2".

## 5. Acceptance criteria, re-scored

1. **Premise completeness: MET.**
   - Every item named in the criterion is inventoried, with its source, domain and status: E1/E2
     (l. 142), P-phase, N2.3, D-A8 (GR:805–827), P-super, and SM's uses of A5.
   - The deferrals in §10 are justified.
2. **Track independence and genuine first steps: MET.**
   - Each track has an ordered chain.
   - Each named first step presupposes only settled steps: carrier and typing (a); reference class (b);
     interface and availability after C-1 (c); "executable" (d).
   - Cross-track conflicts are flagged (X1–X4).
   - X5 and m1–m2 are nonblocking.
3. **Logical correctness: NOT MET at this commit. MET once C1 is applied.**
   - §5.1 uses the interface ceilings and D-A8 for a conclusion they do not support: exclusion of
     non-quantum correlations.
   - Everywhere else, incompatible premises, missing coverage and countermodels are kept apart (rule,
     ll. 410–412), and no finite-to-infinite transfer is made (ll. 416–419).
4. **Verdict support: MET, with C2.**
   - UNDETERMINED follows from the four tracks.
   - The stronger result on track (c) under global P-vii is reported in §§4 and 6, but not in the
     track's table. C2 aligns them.

## 6. Verdict

**ACCEPT WITH CHANGES.**
- **Required:** C1 and C2, both local to §5.1 and §§7.4 and 7.6.
- **Recommended:** X5, m1–m4.
- **Re-review:** a focused diff check of those passages suffices.

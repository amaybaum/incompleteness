ACCEPT — `RO1-DEPS-r4.md` at `dab1852549725765640495c7d8adb7cb234efe2c` (`research/ro1-sector-c-1169-20261114`, PR #1294); base `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`.

# Focused confirmation of RO-1 step 2, `RO1-DEPS-r4.md`

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**Files checked.**
- `RO1-DEPS-r4.md`, SHA-256 `02340bf2…1c87e`.
- `RESPONSE-DEPS-r3.md`, SHA-256 `632ccb36…2bdc`.

**Integrity.**
- The copies supplied to me are identical to the committed files.
- `RO1-DEPS-r3.md` is unchanged.
- `REVIEW-DEPS-r3.md` is preserved as delivered.
- The README rows are updated.

**Method.** I read the full diff from r3 to r4 (124 lines). Line numbers are r4's.

## 1. C1: limitations that exclude quantum only

**Resolved at every site.** The four classes in §5.1 are correct, and each reason given is right
(ll. 370–387):
- *excludes both*: only D-ceil, under global P-vii and P-xiv, for separated wings on F;
- *excludes quantum only*: D-iv, D-nonneg and D-A8;
- *excludes neither*: access, capacity and retention;
- *partial discriminator*: retention with reuse.

The PR gate's conjugation is a permutation, so it passes both ceilings. D-A8 bounds entanglement
only.

Propagation:
- §5 closing paragraph (ll. 360–363).
- R7's cell: "Does not exclude PR at Interface B". The cell says the affine class excludes the stated
  gate only because the gate is not affine, and that no general exclusion is shown (l. 336). This is
  correct, and it is properly not an exclusion.
- §6 grouping: R7 is moved out of "sound against PR" (ll. 416–418).
- X4 is sharpened (l. 619).

Grep of r4 for "excludes both", "exclude(s) PR", "sound against" and "D-A8". The surviving uses are:
- l. 243: D-ceil "excludes PR and the quantum value alike";
- l. 344: "R3 is sufficient to exclude PR on F";
- l. 416: R3, under global P-vii;
- §5.1: the corrected classes.

All of them are legitimate. **No site still credits the interface ceilings or D-A8 with excluding
PR.**

## 2. C2: track (c) under global P-vii

**Recorded with its exact hypotheses and scope.**
- **Hypotheses (l. 545).** The list matches Main:364–376 and Main:20 at source:
  - (i) deterministic dynamics;
  - (ii) setting operations on disjoint regions at one step, each reading and writing only its own
    region;
  - (iii) readouts outside the remote cone;
  - (iv) `p(Ω | a,b) = p(Ω)`;
  - a ±1 outcome recorded in every run.

  Main:20: "is a local hidden-variable model, so `|S_CHSH| ≤ 2`".
- **Scope.** It is limited to separated wings on F. Wings inside the cone (:414), experiments with
  messages, other two-wing experiments, and I (no transfer) are all excluded.
- **Status.** The soundness inference is correctly marked [A-inf].
- **Consistency.** The header (ll. 115–116) and the §7.6 row (l. 604) match.

**The argument for keeping C-1 first and the verdict UNDETERMINED is valid (ll. 566–572).**
- The target requires soundness *together with* Bell coverage. #914 c.6875548603, read through the
  API, says: "Bell as a separate track that the full result requires … excluding stronger-than-quantum
  correlations in the physical sector".
- Under global P-vii, soundness for separated wings holds only because the quantum value is lost.
  So a K-X that keeps 2√2 cannot be tested before C-1 is resolved (RO1-SPEC-r3 §7.3, test (b)).
- The partial result coexists with a coverage failure, so it is not SUFFICIENT.
- It shows no executable supraquantum experiment, so it is not INSUFFICIENT.

## 3. X5 and m1–m4

- **X5 (l. 620). Correct.**
  - Sources checked: H-Bell (i) (Substratum:133), the adopted branch (:80) and D-PR (:360).
  - PR meets H-Bell (i)–(ii).
  - It concludes on one interface for (b) and (c), and it does not change the verdict.
- **X3 clause (l. 618). Correct.** A complex diagonal is not a bijection of configurations, so
  P-phase is covered as well as P-mix.
- **m1 (ll. 478–480). Correct.**
- **m2 (l. 591). Correct.** Step 2 fixes the readings of S6 and of P-vii before step 3.
- **m3 (ll. 100, 690). Correct.**
- **m4 (l. 395). Correct.** "If adopted (S8)".

## 4. New errors

None found.
- **No new premise.** No new premise is introduced.
- **No conditional result stated as established.** The C2 and X5 inferences are [A-inf], with their
  scope.
- **No defined operation treated as executable.** R7 says "does not exclude", not "executes".
  Executability remains S3.
- **First step and ultimate goal stay separate.** They remain separate on every track.

Two optional nits, neither blocking:
- **n1 (l. 370).** "None excludes non-quantum correlations while keeping quantum operations." This
  stands because the reuse discriminator rejects only the same-seed implementation, not PR
  correlations as such. Saying "except partially, retention with reuse" would remove the apparent
  tension with the fourth class.
- **n2 (l. 479).** "On F₂ the track-(a) question is already refuted" is accurate. Elsewhere on F the
  kernel states nothing beyond the carrier-general nonnegativity of Interface B. The sentence's
  conclusion, "what is open lies on another carrier", holds in any case, because the target is not F
  (C-2).

## 5. Acceptance criteria

1. **Premise completeness: MET** (unchanged from r3).
2. **Track independence and genuine first steps: MET.** X5 is added, and the precondition of track
   (d) step 3 is fixed (m2).
3. **Logical correctness: MET.** C1 is resolved at every site. No limitation is credited with
   excluding PR when it does not.
4. **Verdict support: MET.** UNDETERMINED follows from the four tracks. The stronger result under
   global P-vii is reported on track (c) with its exact scope.

## 6. Verdict

**ACCEPT.** r4 is ready for the ChatGPT exact-head review at `dab18525`. n1 and n2 are optional.

# REVIEW-C5-r2 — re-review of AUDIT-C5 r2 against REVIEW-C5.md

Reviewed: `AUDIT-C5.md` r2, sha256 `ff858e471aa34563f68e84208f47364b834fd9a152a957214099223bcaf8b94e`.
Compared against r1, `AUDIT-C5-r1.md`, sha256 `a29c9b8ccbc701a6a0618843faa85313e4ad98ff2560f4ebec71bf63bbc09677`,
by full `diff`. Snapshot: `origin/main` = `5ce4f98e`. Read-only.

The r1→r2 diff touches only the passages that REVIEW-C5 named. Everything else is unchanged from r1, which
was verified in REVIEW-C5.

## Verdict: ACCEPT

All three blockers are closed. N1–N9 are applied. Every new or changed citation checks out at `5ce4f98e`,
except for one off-by-one line range (R1 below), which comes from REVIEW-C5 itself. The two remaining nits
are non-blocking.

## 1. Blockers

- **B1 — closed.** C5-4 now classifies all four sites alike as confirmed (dropped scope): Main:712, GR:368,
  FULL:2065 and ch07:199. The section citations ("(§3.4)", "(§3.3)", "([GR §3.3])") are correctly described
  as attaching to the completion clause. The "qualified by context" list now holds only the OI⁺-paragraph
  "finite theory" sites. The summary and AW-C5-b are updated to match.
- **B2 — closed.** FULL:2765 = ch09:298 (byte-identical, re-checked) is added as a confirmed contradiction.
  Its anchor is Main:590/592, with Main:218 (ii) cited. The Main:218 quote is exact. The audit now also notes
  in AW-C5-b that the search must be by meaning, not by phrase.
- **B3 — closed.**
  - FULL:568 = ch01:233 is added and classified confirmed against Main:656/340, beside FULL:542 and FULL:544.
  - Structure:887 is classified confirmed against Main:556/592. "No book mirror found" is correct:
    `git grep -i "main paper identifies"` over `book/*.md` returns nothing.
  - The summary and AW-C5-d are updated to match.

## 2. Non-blocking items requested

- **N2 — applied.** C5-5 now gives a two-reading classification:
  - on the Ĥ_eff reading, not a contradiction;
  - on the emergent-object reading, tension with Main:260 and both code comments;
  - "needs owner judgement" for which reading governs.

  The unsupported-claim finding is retained. AW-C5-f cites the code comments. For the one line-range error
  in that citation, see R1.
- **N4 — applied.** The PC marker correction is restated at Main:598's strength: one realization that is
  ε-common over all instruments on ℂ^d with at most m outcomes, at horizon K. It also states that:
  - an exact common realization for a fixed finite noncommuting family is open, "not an exact per-family
    positive";
  - exact reproduction of the full theory is excluded (Main:560);
  - per Main:582 (line confirmed; quote exact), the quantum state is held in a hidden register and the
    instruments are data. AW-C5-g records this.

  The A1-label collision is disambiguated.
- **N5 — applied.** R6 N2 is now support on main for the containment step as well as for the
  identification. The supporting citations are accurate:
  - `oi_channel1_check.py:171–176` builds the four defect matrices `(I + s X⊗Z + t Y⊗Y − st Z⊗X)/16`, with no
    statement that they are `Z_F`.
  - Line 56 of blob `62cdd798`, checked with `git cat-file -p` and in the inflated archive copy, reads
    "``z_s = (E00 + s1 E13 + s2 E22 − s1 s2 E31)/4``".
  - result.md, the preregistration and controls.py define neither `Q3` nor `Z_F`. This was re-checked by grep.
- **N7 — applied.** The repair menus at r1:101, :133–134 and :168–169 are removed and replaced by "The correction
  is the owner's". A new preamble states that no repair is proposed. A scan for
  should/repair/fix/suggest/propose finds three survivors:
  - "owner may wish to check" (GR:330, carried over from r1), which is a pointer and not a repair;
  - two lines of assumption-watch guidance to other clusters (r2:528, :540), which concern audit method and
    not manuscript edits.

  None is a manuscript repair.

The other items are also applied:
- **N1:** Main:592, quote exact; FULL:548 = ch01:213; FULL:2483 = ch09:16 and FULL:6337 = appendix-c:108, both
  byte-identical, re-checked.
- **N3:** `permTheory_diagonal_only_scalar` at :675; PhaseSource.lean:55 and :108; RouteB.lean:218.
- **N6:** MR-1 `preregistration.md:87` quote exact ("contract (1), freshness condition, countercontrols");
  `MR-star.md:827`; `stage1-log.json:725` ("git show 2af1d5d5 of the #912 REPORT.md (equation (1))");
  composition-source-map's v6 sentence; native-setting `:40–41`.
- **N8:** the derived-artifact sentence.
- **N9:** Main:712, SM:1472 and Structure:108 are listed as related sites, with no classification asserted.

## 3. Remaining nits (non-blocking)

- **R1 — line range.** `bohr_frequency_probe.py:2365-2367`, at r2 C5-5 and AW-C5-f, is off by one. The
  quoted words "genericity fails AT the permutation limit (root-of-unity eigenphases: maximally
  gap-degenerate)" lie on lines 2367–2368; the sentence begins at 2365. The correct range is **2365–2368**.
  The error originated in REVIEW-C5 N2.
- **R2 — count wording.** C5-4 says "The four sites are classified alike" but has three bullets (Main:712;
  GR:368; FULL:2065 = ch07:199). The count of four is right only if FULL:2065 and ch07:199 are counted
  separately. Saying "four sites (three passages)" would remove the ambiguity.

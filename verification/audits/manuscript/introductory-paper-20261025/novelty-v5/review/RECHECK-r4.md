# Re-check: novelty audit, revision 5, r4

## Objects read

Bundle: `novelty6/r4/introductory-paper-20261025/`.

`sha256sum -c SHA256SUMS` passes for all 15 entries. In particular:
- `novelty-v5/AUDIT.md` (r4): `b896788700f4904719ebe101e3f10c119187a5d6acb6f8ad5fb6b7b77974a781`;
- `novelty-v5/AUDIT-r3.md`: `6dae22ac…99f9`, equal to `introaudit/novelty-v5/AUDIT.md`;
- `novelty-v5/CHANGES.md`: `2cdf5e5b…d004`;
- `novelty-v5/README.md`: `e781a4b8…5ce3`;
- `README.md`: `d65a62bf…a4e`;
- `review/REVIEW.md` and `review/RECHECK-r2.md`: byte-identical to my originals
  (`7ecbb987…`, `7e782f41…`).

## Repository

- `origin/main` is `61930e90` (#916).
- `83d1da1b..61930e90` changes only `tools/citation_roles_check.py` and `tools/release_gate.py`.
  Every blob in r4's §0.1 table is identical at `83d1da1b` and `61930e90`, and the a411 column
  is also correct.
- `a411bf46..83d1da1b` changes nothing under `verification/lean-mathlib/`, nothing in the census,
  nothing under `arc-b-rooted-classification/` and nothing under `papers/oi_lattice_code/`.
- Main's hunks are all one for one, apart from +2 lines at :899–900 for [63].
- PR #930 was read through the REST API, and its head was fetched read-only as a local ref.

**Process note.** One `git show` loop in `novelty5/repo` triggered git's background
auto-gc ("Auto packing the repository"). The clone has no alternates or worktrees, and later
commands used `-c gc.auto=0`. No tracked file was changed, but the clone's object packing was.

## Verdict: ACCEPT WITH NITS

There are two required wording fixes before commit to #918 (R1, R2). Neither needs re-review.
There are seven nits.
- **Re-base and fix statuses.** Every re-based site and every F-note status checked out. Each
  attributed commit touches the files named.
- **New full-text outcomes.** Each was re-verified against an independently downloaded PDF.
  Eight sources were re-fetched from their stated URLs, and all eight sha256 match §8.
- **Classifications.** They follow the PROVISIONAL rule.
- **Novelty.** None is upgraded on absence of evidence.

## 1. Re-base and F-note statuses (at `83d1da1b` = `61930e90` for these files)

**Fixed.** Confirmed at the cited lines:
- **F6.** Main:580(2) and :588 carry the joint-law and CMI caveats.
- **F10.** Main:62: "each set {x_j}×C_H has exactly |C_H| preimages".
- **F12.** Main:167: "Suppose the visible process has a gap … as (C4) asserts".
- **F21.** Main:332 cites [63]; Main:900 holds the [63] entry; `book/bibliography.md:17`
  holds the book's entry. ch01 has no numeric citations left: :32 "Bao, Carroll, and Singh
  2017", :103 "Breuer, Laine, and Piilo (2009)".
- **F22.** Main:149 "witnesses divisibility failure …, and divisibility can fail without it";
  Explainer:143; ch01:103; FULL:447.
- **F23.** GR:20(ii); ch07:46; ch01:77–85; Main:86 and :522 now point at §1.2.
- **F24.** GR:20 and :567.
- **F25.** glossary:39.
- **F27.** `book/README.md:64`.

**Changed, partly open.** Confirmed:
- **F3.** Main:16 and :530 changed; the $e^{-i\hat H}$ remark is still at :532.
- **F4.** Main:28 changed; the title at Main:2 is unchanged.
- **F5.** Main:608 now reads "proved here in prose and neither is formalized"; Main:690 now
  reads "conditions are diagnostics"; Explainer:373 is open.
- **F8.** Only BLP was added. A grep confirms that Capela, Egloff/Milz 2020, Dulmage,
  Buscemi, Egri and 2608.04354 are not cited.

**Open.** Confirmed unchanged: F7 (Main:580(4)), F11 (Main:20, :139), F13 (Explainer:282,
:1015), F14–F20 (Main:210–220, :636, :822), F26 (Explainer:373) and the conflation at
Substratum:126.

**Commits.** Every commit named in §1 exists, and its stat touches the claimed files. #925,
#926 and #927 have 15, 6 and 13 second-parent commits respectively. The F28 provenance is
confirmed: `6250782a` changes Main:332 from "*ancilla-assisted* one:" to "… one [4]:".

## 2. New full-text outcomes

**Hashes.** I re-downloaded the following into new directories. Every sha256 equals §8:
RHP 2014 v2, Strasberg–García Díaz v2, Capela v1, BLP v2, BJA v2, Milz 2020 v3, RHP 2010 v2,
and JDM 1960 (Cambridge Core).

**Quotes.** Located by per-page extraction, in my re-downloaded copies unless marked:
- **XOR, RHP 2014 p. 7.**
  - Def. 2.2 is there, and so is "As an example (see [4, 6])".
  - Eq. (15)'s support is {(0,0,1), (0,1,0), (1,0,0), (1,1,1)}, which is
    x₃ = 1⊕x₁⊕x₂.
  - "Hence the conditions (11), (12) and (13) are clearly fulfilled" is present.
  - Refs. [4] Parzen, [6] van Kampen and [10] Feller 1959 are on p. 46.
  - KNOWN (FT-r4) is correct: RHP 2014 is prior to the repository's 2026-08-11 example. "Who
    first" is correctly left unverified.
- **Capela p. 6.** "x4 = x1 + y2 + y3 (here we have modular addition) … the process is
  divisible". ✓
- **C3, Strasberg p. 2.** Eq. (3), and "is nevertheless a well-defined object in quantum
  mechanics". ✓ REFRAMING without PROVISIONAL is justified: the decisive comparator is now FT.
- **C8, RHP 2014.** Thm 2.4 (p. 8) and "Pmin(fail) increases monotonically" (p. 9). ✓ KNOWN
  is unchanged. The "only if" reading, applied to v = δ_a − δ_b, is correct.
- **C4, Milz 2020.** Def. 1 (p. 5) and the proof sentence "reproduces it correctly" (p. 21)
  are as cited; the Thm 4 statement itself is on p. 20 (N1). The comparison "a different
  question; neither states S ⊆ Q_fb" is fair. PARTLY KNOWN with a PROVISIONAL packaging part is
  correct, since the comb-realization theorem is unread.
- **F28 sources.**
  - BJA abstract (p. 1): "a bijective dynamical map is completely-positive-divisible if and
    only if …". ✓
  - BLP p. 1, "necessarily be non-divisible", and p. 2, "σ ≤ 0 for all quantum processes for
    which the divisibility property (9) holds". ✓
  - RHP 2010: "E(t+ε,t) is CP if and only if f_NCP(t+ε,t) = 1" (p. 4) ✓. "no longer
    constrained" and Fig. 1 are on PDF p. 1, not p. 2 (N1).
- **C5.**
  - JDM p. 4 (journal p. 240): "Let c1 be the smallest (possibly unique) non-zero element of
    A … A⁽¹⁾ = A − c1A1. Repeating this process …". ✓
  - Isbell p. 3: the Peck–Rattray remark is about rational *entries* and existence, as the
    audit says. This was checked in the coordinator's copy, `novelty6/src/infds`.
- **P1.3 absence claim.** "recurren" and "poincar" occur in none of RHP 2014, Milz 2020,
  Milz–Modi, Pleasance, WVB, BD v3 or Milz 2019 (0 hits each). ✓

**PROVISIONAL rule.** Applied consistently:
- PROVISIONAL is removed only where a decisive comparator was read: XOR, and C3.
- C4, C5, C1, C1′ and C8-D keep PROVISIONAL on their "not located" parts.
- C9, C10, C11 and C16e keep it for attribution.

## 3. The two flagged judgments

- **(a) "In-house" at Main:212 and :680, against Main:608.** I agree that F5 is "changed", not
  open, at those lines. "In-house" asserts that the proof is internal, which Main:608 confirms
  ("proved here in prose"). It does not assert formalization. The residual F5 site is
  Explainer:373, as recorded.
- **(b) C5's rational-weight step.** The inference is valid. Each Birkhoff weight $c_i$ is an
  entry of $A^{(i-1)} = A - \sum_{j<i} c_j A_j$, with 0/1 matrices $A_j$, so a rational $A$
  gives rational $c_i$. The audit correctly labels it as its own inference and does not
  attribute it to JDM. It keeps the explicit statement PROVISIONAL (König unread). Realizing a
  rational mixture under a uniform prior is GO's construction (p. 43, FT).

## 4. Novelty on absence of evidence

None.
- C8-R stays NOVEL-CANDIDATE, unverified, with no priority sentence.
- Its gate is narrowed honestly: P1.1 and P1.2 were reached only through open surveys, and
  their primary texts are unread. The §A.31 point that P1.3's silence "carries little weight"
  is apt.
- The admissible "not located" wording in §7 is limited to "the divisibility, process-tensor or
  stochastic–quantum literature", and must not name realization theory or automata. That
  matches what was read.
- The correctness and originality table keeps the two axes apart.
- "Nothing moved up" is accurate: two PROVISIONAL marks were removed and no class rose.

## 5. F28's status line

It should not say "corrected by PR #930". The site is unchanged on `main`. As of this check,
#930 is open, **draft**, not merged, head `ebbb1a97` (its body still cites head `abd4b45a`),
with base `main`. See R1.

## 6. Hygiene

- No absolute local paths. Only `scratchpad/novelty{5,6}/repo` appear, as relative working
  names, disclosed in novelty-v5/README.
- No secrets, tokens, signed URLs or IP addresses.
- No PDF, `.txt` extraction or binary files. The bundle is 508 KB.
- `SHA256SUMS` passes.
- Suitable to commit to #918 once R1 and R2 are applied.

## Required (wording, before commit)

**R1.** **Location:** F28 (§4 table row and the F28 block) and novelty-v5/README.
- *Problem:* "a correction PR is being prepared" is stale.
- *Fix:* replace it with "open at `83d1da1b`; correction proposed in PR #930 (open draft, not
  merged)". Also record two things #930 covers:
  - **The mirror sentence.** At appendix-b:96 / FULL:5885, #930 restricts the claim to bijective
    maps and changes "[Main §3.4]" to "[Main §3.2]". Main:332 lies in §3.2 (Main:258–353). The
    audit's "carry no misattribution of their own. They follow Main's" should note the missing
    bijective scope and the wrong section pointer.
  - **The XOR "Needed" item.** #930 adds "[5], Eq. (15)" at Main:606.

**R2.** **Location:** the bundle's parent `README.md`, sections "Findings carried forward" and
"Unresolved literature and scope questions".
- *Problem:* both sections still list items since resolved:
  - Main:98's bare form, fixed by #922 (v4 F1);
  - the Explainer:120 splice, fixed by #919;
  - the D-gauge migration to B.7, done by #921;
  - "Page 2013's 0.5381 against ch07's 0.646", now stated as conditional on β = 1 by #920
    (C16a);
  - "F3–F8 … F9", whose statuses are now in novelty-v5/AUDIT.md §4.

  The README introduces novelty-v5 r4 as current, so these contradict it.
- *Fix:* either scope the two sections explicitly ("as recorded at `c91bf5dd`; current status
  in `novelty-v5/AUDIT.md` §4"), or update them.

## Nits

**N1.** **Location:** §8 and F28.
- *Problem:* RHP 2010's "no longer constrained" and Fig. 1 are on PDF p. 1, not p. 2. Milz 2020's
  Thm 4 statement is on PDF p. 20; the proof sentence is on p. 21.
- *Fix:* correct the page indices.

**N2.** **Location:** novelty-v5/README's "Primary texts not read" table, and the XOR entry
("Feller 1959 … Project Euclid, bot challenge").
- *Problem:* §0.2 says Feller 1959 and Heller 1965 were *not attempted* (same host as
  Blackwell's challenge). The table and the XOR entry say they hit a bot challenge.
- *Fix:* make all three agree.

**N3.** **Location:** C12.
- *Problem:* the #927 wording at glossary:39, GR:20 and Explainer:353/:373 reads "iff every
  finite accessible horizon containing a memory witness admits a deterministic realization with
  C1, C3 and C4". Read literally, a Markov process, which has no witness, satisfies the right
  side vacuously. Main:522 avoids this only by referring to "(ii)'s conditional mutual
  information". In other words, (iii) presupposes (ii)'s witness order. This is part of C12's
  near-definitional reduction.
- *Fix:* add it to C12 as an owner F-note candidate. F24 and F25 remain fixed for what they
  recorded (C2's placement).

**N4.** **Location:** the correctness and originality table, C8 row.
- *Problem:* "kernel" holds at the matrix and routed levels. From history-level (C4), the step
  is prose (Main:20, :139; F11).
- *Fix:* add the qualifier.

**N5.** **Location:** C3 and C4.
- *Problem:* Strasberg and Milz venues stay "[from memory]". This is optional to fix.
- *Fix:* a Crossref lookup would make them REC, as r4 did for Blackwell and the others.

**N6.** **Location:** F8.
- *Problem:* the parenthetical "the 'Egri' hits in ch12 and Bioinformatics.md are a different
  author" is stale. A case-sensitive grep at `83d1da1b` finds no "Egri" anywhere.
- *Fix:* drop or update the parenthetical.

**N7.** **Location:** §1, the #927 row.
- *Problem:* it says F28 was "introduced". #930's description also identifies the scope omission
  (bijective maps) as a second defect at Main:332, which F28's text does not name.
- *Fix:* add it, so that F28 matches the correction under review.

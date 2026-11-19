# NOTES-BG-r1: working log for G3 unit 2(b), the bridge premise B_G

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. Corpus files were read with
  `git show c3b5f37a:<path>`.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree.
  - The brief names `1ad01923` (unit 2(a) r3). At reading time the worktree head was
    `3945940c62316145ffdf39ab028e66f70c8a6477`.
  - `git log` shows two commits after `1ad01923`: `2c25b544` ("forward correction of unit 1 r5 from
    unit 2(a) r3") and `3945940c` ("unit 1 forward correction check, confirmed").
  - `git diff --stat 1ad01923 3945940c` lists two added files, `G3-UNIT1-CORR-r1.md` and
    `CONFIRM-CORR-r1.md`, and no other change. Every other file this record cites is identical at
    both commits. The two added files are accounted for by the branch history, so no provenance
    anomaly arises (§A.26).
  - The worktree was clean before and after the checks (`git status --short` empty).
- **Files.** `G3-UNIT2B-BG-r1.md` and this file were written in the working area by the writer. The
  writer did not commit, push or post them.
- **Authority.** #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU5, read through the GitHub API.
  It authorizes a paper-only B_G unit that adopts no premise, makes no manuscript change, involves no Lean
  build and makes no claim about Λ.

## 2. Reading log

| Source | What was used |
|---|---|
| #873 c.6865179466 | QU2–QU5 decisions; QU5 scope (quoted in the record) |
| #1275 review 5898121925 (`1ad01923`) | accepts (C); "well-founded grounding can block the loop, but only if a law term … grounds the realized metric, rather than co-constraining it"; QU5 advice |
| #1275 review 5896999577 (`e81e4fb2`) | the "important limit" on (ii-L) |
| G3-UNIT2A-r3.md | in full: §0, §1 rule, §2.2–2.4 (Reading G, N5-G, B_G), §3 witness, §4.1, §4.2 table, §4.3 controls, §4.4, §4.5 attempts, §5 nodes A8–A9, §6, §7 AW-ground, §8, §9 |
| CONFIRM-U2A-r2.md | in full, Y-1 (Substratum.md:385 names the metric) |
| NOTES-U2A-r3.md | the B_G corpus search of unit 2(a) (§2) |
| G3-UNIT1-r5.md | in full; §2 (metric as substratum data, :192), §3.1, B5 |
| G3-UNIT1-CORR-r1.md | lines 1–200 (X-1 to X-9) and the section list (X-1 to X-20) |
| CONFIRM-CORR-r1.md | grep: verdict and K-3 |
| GR.md | :10–14 (G3), :38–44, :76–80, :144–146, :152–166, :338–358 (§6.2), :360–364, :368–402 (incl. :378, :388, :400), :555–608 (§8.3 at :567–581; §8.4), :633, :655, :669, :689–697 (§8.7) |
| Substratum.md | :375–395 |
| SM.md | :140–166 |
| Main.md | :26, :44–56, :684–692; grep for metric, geometry, gravity, causal |
| Structure.md | :134–140 (A1–A6) |
| book/ch07-gravity.md | :178–192 |
| book/appendix-c-objections.md | :246–260 |

## 3. Corpus searches (§A.19)

All searches were run with `git grep` at `c3b5f37a` over `papers/*.md` and `book/*.md`, with FULL.md
excluded where it duplicates a chapter.

1. **Law-status vocabulary.** Patterns: "separate dynamics", "equations of motion", "in virtue of",
   "co-constrain", "regularit", "governing law", "self-consistent by construction", "grounded in".
   - Relevant hits: SM:158, the only occurrence of "separate dynamics" and of "self-consistent by
     construction", which states the status of the lattice gravitational law; GR:597 ("grounded in the
     cosmological horizon", a different sense); Methodology.md:81 (a different question, as unit 2(a)
     recorded); and Substratum.md:389 with its mirror ch02-substratum.md:212.
   - No hit states that a law term grounds a metric.
2. **A1–A6 and E1–E7.** Structure.md:136 lists A1–A6: finiteness, determinism (bijection), bounded
   coupling, center independence, linearity, background independence. GR:669 glosses them. None is a
   gravitational law.
3. **Main on the metric.** Main uses no metric in Lemma 2 (Main:48). The partition there is "the
   definition of embedded observation". Main:26 speaks of "causal reach" without a metric. This is the
   source of AW-part.
4. **Corpus uses of derived relations.** Found by reading the passages listed in §2: GR:144 ("same
   physical degrees of freedom"), GR:581 ("correspond to differences in the coupling structure of φ"),
   GR:655 ("the classical substratum's gravitational dynamics"), Main:686–692, Substratum.md:387 and :393,
   and GR:693 ("emergent-metric geometry"), the source of AW-metric.

Unit 2(a)'s search (NOTES-U2A-r3 §2) used grounding vocabulary and did not reach SM:158 or GR:144. That is
the source of BG-F2.

## 4. Order of work

1. Read the authorization, the two reviews, unit 2(a) r3, CONFIRM-U2A-r2 and unit 1 r5. Extracted the
   corpus passages at `c3b5f37a`.
2. Formed an outline: the governing reading conflicts with the stated ontology, and the per-world reading
   meets N5-G.
3. Ran searches 1–3 of §3. Found SM:158, A1–A6 and Main:48.
4. Wrote §1 of the record (the rule, the premise base, F1–F3, K1–K5, the productivity test). Its clauses
   were not edited afterwards.
5. Wrote §2 (the formalization and the corpus-use table), then §3 (Lemma U, Corollary E, Lemma F, F3).
   Lemma U came from applying unit 2(a)'s C2(b) uniformly: the Einstein left side is grounded in `g`, so
   it cannot ground `g` under N5-G, and the witness's term is grounded in `g` through N1–N3-G.
6. Wrote §4 (two senses of "derived"; the corpus on derived laws; the residual).
7. Ran the controls (§5) and the pressure tests (§6). Branch (A) was tested first, as the branch
   favourable to decoupling. Nodes A5 (diachronic grounding) and B2 (the partition's ground) were added
   during the tests. Both were placed under the rule's clause that adds any further formalization found
   during the analysis.
8. Wrote §7–§12.

## 5. Decisions

1. **Outcome (B), not (C).** Each formalization lands in (b1) or (b2). The open question that remains
   about the witness, G3's determination question, is not B_G.
2. **Scoped to Reading G, case β.** N5-G is Reading G's premise and is not stated in the corpus. Case α
   (Main:48) breaks Reading G's reductio and is recorded as AW-part, not adjudicated.
3. **No premise adopted.** P-F, P-D and P-S are cited as stated commitments, with their support class
   (§4.1 of the record: P-F's derivational support reaches weak-field consistency only).
4. **Consequences stated as conditional on review** for unit 1 r5, CORR r1 and unit 2(a) r3. No record
   edited.
5. **K_cpl^free** (CONFIRM-CORR-r1 K-3) is addressed in one paragraph (§3.4 of the record), since Lemma U
   covers it.
6. **No magnitude claim, no manuscript change, no Lean build.**

## 6. Checks

- No computation, script or build was run apart from the three permitted checks.
- The logic of Lemma U and Corollary E is elementary and done by hand.
- Barred-string scan of both files: no path prefix of the forbidden forms, and none of the §A.32/§A.33
  phrase families.

| Check (worktree at `3945940c`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. They confirm that the manuscripts are unchanged and in the state both
earlier units recorded.

## 7. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Class |
|---|---|---|
| `G3-UNIT2A-r3.md` at `1ad01923` (branch) | the definitions of Reading G, N1–N5, B_G and the witness, which this record uses | support off `main`; lands with #1275 under the joint landing (#1169 OQ-6) |
| `G3-UNIT1-r5.md` (branch) | the witness class (metric as substratum data, U1r5:192); Part 2's wording | support off `main`; lands with #1275 |
| `G3-UNIT1-CORR-r1.md`, `CONFIRM-CORR-r1.md` at `3945940c` (branch) | the consequence statements of record §8.4 | support off `main`; lands with #1275 |
| `CONFIRM-U2A-r2.md`, `NOTES-U2A-r3.md` (branch) | Y-1; unit 2(a)'s search, the basis of BG-F2 | support off `main`; lands with #1275 |
| #873 c.6865179466 | authorization | provenance |
| #1275 reviews 5898121925, 5896999577 | context for B_G's statement | provenance |

Every support reference is to a file on #1275's branch, which lands together with this unit or not at all.

## 8. Limits

- By hand. Scoped to Reading G, case β, and conditional on N5-G.
- Readings of corpus text are [P].
- The literature is recalled, and the Loewer and Lange citations are given without verified details. No
  verdict rests on them.
- The rule and the analysis land in one commit, and the rule was written after an outline had formed.
- The §A.31 fixed point is not reached.

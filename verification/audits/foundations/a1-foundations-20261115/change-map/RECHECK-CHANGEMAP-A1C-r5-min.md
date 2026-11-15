# Recheck of change map A1C r5-min against the review of r4-min

**Reviewer.** The independent reviewer of r1–r4. Paper-only: nothing in the repository was edited, committed, pushed or posted, and no Lean, build, guard or census run was made. Base: the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Every site named below was opened there.

## Verdict

**NOT CONFIRMED.** Narrowly.

What is in order:
- All 18 F1/F2 sites are corrected. Each one-clause fix stops the claim, adds nothing, and keeps A1 open (neither established nor disproved).
- F3–F9, F11–F23 are applied correctly.
- The counts are right.

The F10 dispute goes to the writer in principle. Anchoring A1 where H-count is defined makes the separate edits at GR:28, ch07:12 and appendix-a:117 redundant. Two things keep the anchor from working as intended:
- **R1.** As worded, the anchor restricts H-count's scope ("for a finite total system") rather than adding A1 as part of H-count. A result "under H-count" would then not visibly require A1.
- **R2.** One passage, ch07:16, states the calibration for "any … system … satisfying H-slope", with no H-count and no section pointer, so the anchor never reaches it.

With R1 and R2 fixed, the map would be CONFIRMED WITH NITS.

***

## 1. Findings F1–F23 at their r5 locations

**F1 (15 sites) and F2 (3 sites).** All 18 left-hand quotations match the base text. Each fix:

| Site | r5 fix | Stops the claim | Adds nothing | A1 open |
|---|---|---|---|---|
| SM:14 | delete "finite" | yes | yes | yes |
| SM:1588 | delete "finite" | yes | yes | yes |
| Sub:14 | delete "finite" (the "develops the alternative" sentence stays) | yes | yes | yes |
| Sub:16 | delete "finite" | yes | yes | yes |
| Sub:22 | delete "finite" | yes | yes | yes |
| Sub:44 | "*finite capacity* (under A1)"; "a lossless memory, finite under A1" | yes | yes | yes |
| Sub:389 | "a set (finite under A1)" | yes | yes | yes |
| Sub:429 | delete "finite" | yes | yes | yes |
| ch02:136, :212 | "a set (finite under A1)" | yes | yes | yes |
| ch12:213 | "is, under A1, a finite deterministic system" | yes | yes | yes |
| ch09:106 | "— the open hypothesis A1, not adopted" | yes | yes | yes (see N2) |
| ch05:95 | "on finite reversible representatives" | yes | yes | yes |
| Main:280 | "The default hidden prior of a constructed realization (Lemma 3) corresponds to …" | yes | yes | yes |
| Main:642 (b) | "the physically operative form under A1:" | yes | yes | yes; R7-RCL's pinned phrases are in (a) and are untouched |
| GR:58 | "Under A1, restrict the finite total system", plus the H-count anchor | yes, for the restriction sentence | yes | yes; the H-count wording is R1 |
| ch07:118 | "a configuration space $S$, finite under A1"; "in the framework's bijective models"; "in those models" | yes | yes | yes |
| ch14:160 | "acts on a state space, finite under A1," | yes | yes | yes |
| ch04:178 | "for a finite bijective model" after "Main §4.6" | yes | yes | yes |

**F3–F23.**

| Finding | Status |
|---|---|
| F3 | Applied: the name is kept at Main:60 with "an open hypothesis, not adopted". |
| F4 | Applied: ch01:41's injectivity sentence is restored. |
| F5 | Applied: GR:342 ("of which A1 enters as an open hypothesis rather than a commitment"); ch19:212 and ch09:36 now carry A1 beside the axioms rather than among them. |
| F6 | Applied: appendix-c:124 now reads "which is the open hypothesis A1". |
| F7 | Applied: ch09:18. |
| F8 | Applied: Main:720. |
| F9 | Applied: Main:20, with the exact r3 replacement; the left-hand quote matches. |
| F11 | Applied: Struct:1293. |
| F12 | Applied: the reason codes now follow the dispositions. |
| F13 | Applied: N-M44b. |
| F14 | Applied: ch18:174 ("it returns"). |
| F15 | Applied by choice ("posit" kept as the item's name). Consistent with F3. |
| F16 | Applied: the method/ontology distinction is stated in Part F, and Main's lack of A4 is given as the reason for the difference. |
| F17 | Applied: ch01:235, ch19:214. |
| F18 | Applied: ch07 per-site text; the :157 and :159 quotes match. |
| F19 | Applied (see §3). |
| F20 | Applied: N-U35 cites the Corollary, part (2). |
| F21 | Applied, except N-P03 (N1). |
| F22 | Applied (OQ-A). |
| F23 | Applied. |

## 2. Adjudication of the F10 dispute

**Reach of the anchor.** I listed every line of the papers and the book (FULL excluded) that states $\hbar = c^3\epsilon^2/(4G\sigma)$, $\epsilon = 2\sqrt\sigma\,l_p$ or the $1/4$ coefficient, and checked how each points to H-count.

1. **Lists that name H-count** reach the anchor directly:
   - papers: GR:12 (abstract), :24, :28, :74, :78, :88, :154, :316, :318, :611, :637, :701; SM:1592; Structure:56; Substratum:191;
   - book: ch00:81, :97; ch02:190; ch03:120; ch07:12, :14, :57, :106, :262, :307, :309; ch09:14, :48, :118, :226.
2. **Lists that cite GR §8.5(b)** reach it in one hop, because §8.5(b) (GR:623) itself reads "If, in addition, H-count holds …":
   - papers: GR:685, :749; SM:166; Structure:453, :904, :1319; Substratum:181, :189, :193, :529;
   - book: ch02:110; ch09:88, :92; appendix-a:117; appendix-b:169.
3. **Sentences inside the derivations** reach it through their own section: GR §3.1–§3.2 and §8.5 (GR:30, :42, :56, :66, :102–:162, :625–:629, :669) and ch07 §7.3–§7.5 (ch07:36, :48, :55–:100). For example, GR:669 sits in §8.5 after (b), and GR:30 says "once their named conditions are granted".
4. **Uses of $\epsilon = 2\sqrt\sigma\,l_p$ as the lattice spacing of OI's representative** are statements about the model's parameter, finite through A4 under OQ-6 (a). They are not restatements of the calibration's conditions, and they omitted every condition before A1 was involved, so Q11 (a) does not reach them. These are ch18:22, :144, :258; ch09:324; appendix-c:126, :261; SM:222, :547; Structure:789; Substratum:484, :552; ch07:173; GR:326.
5. **Mentions** in tables of contents, roadmaps, counts and objections (book README:64, :98; readers-guide:77; appendix-b:16; ch00:89; ch03:42, :240; ch09:52, :54, :248, :330; ch12:197; appendix-c:20, :236–:275; GR:32, :547) state no result about nature beyond pointing to the chapter or relation.

Conclusion on reach: the writer is right that GR:28, ch07:12 and appendix-a:117 need no separate edit once H-count carries A1. Each names H-count or cites §8.5(b) and Ch 7 §7.3. Their r4 edits are correctly dropped as redundant under the minimum-change policy.

**R1 (required). The anchor's wording does not make A1 part of H-count.**
r5 inserts "for a finite total system (A1)" inside the H-count clause, at GR:58 ("the energy-dependent entropy of the whole hidden sector at the shell scale, for a finite total system (A1), is the boundary count") and ch07:52.

Read plainly, that limits H-count's scope: it says what holds *for* a finite total system and leaves an infinite one outside it. A result stated "conditional on H-count" would then not show a reader that it needs A1. The reach argument above depends on H-count *containing* A1.

*Fix:* make A1 a conjunct.
- GR:58: "Under the hidden-sector condition **H-count** — that the total system is finite (A1) and that the energy-dependent entropy of the whole hidden sector at the shell scale is the boundary count, …".
- ch07:52: "the total system is finite (A1) and the energy-dependent entropy of the whole hidden-sector reservoir is its boundary count".

This keeps the label H-count, adds no new premise beyond the A1 that OQ-2 (a) names, and is one clause at each site.

**R2 (required). ch07:16 states the calibration without H-count or a pointer.**
The sentence reads: "A conditional result like '$\hbar = c^3\epsilon^2/(4G\sigma)$' is … 'any horizon-bounded embedded-observer system with the framework's structural conditions, and satisfying H-slope at its horizon, gets this functional form for the emergent action scale.'"

This is a universal statement about any such system. It names H-slope only, cites no section, and sits in §7.1, before §7.3. A reader takes it to cover systems of any size. That is the A1-dependent overreach the policy corrects, and the anchor never reaches it.

*Fix (one clause):* "…and satisfying H-slope and H-count (Section 7.3) at its horizon, …".

**Recommended: H-slope-only lists that reach H-count by citation only.**
- glossary:17 ("conditional on H-slope"; it points to the "horizon calibration of Chapter 7");
- glossary:73 ("conditional on H-slope … Developed in Chapter 7 §7.3");
- ch07:305 ("conditional on H-slope … (Sections 7.3–7.4)");
- Substratum:195 ("Stage 3, conditional on H-slope", directly after Theorem 23's "the further conditions of [GR §8.5(b)]").

Each reaches H-count only through the section it cites. That is acceptable under minimum change, but "conditional on H-slope" reads as a complete list. Adding "and H-count" at these four sites would remove the ambiguity. Their omission of H-count predates A1.

## 3. F19: needed, not cleanup

The base title "(reversibility as the conservative assumption)" says reversibility is the assumption made. The remark's new body says "reversibility of nature's dynamics is not adopted as a postulate". Left unchanged, the title would assert what the body disclaims (§A.30). The one-word change to "and" is the minimal correction, and no census anchor or guard pin rests on the title. It is a needed change, not editorial cleanup.

## 4. New errors, recount, OQ-A

**Nits.**
- **N1.** N-P03 (Computation:118) still reads "The total-finiteness hypothesis ([Main] §1.2, §4.5, item (ii), open), however, would take $S$ finite." It renames the posit and uses a second status form, against F3 and F21. Use "The total-finiteness posit ([Main] §1.2, §4.5), an open hypothesis, not adopted, would take $S$ finite."
- **N2.** ch09:104 calls the six properties "universality-class commitments — the conditions that define membership", and ch09:106 now adds "not adopted" to Finiteness. The class condition and the status of A1 for nature are different things. "— as a claim about nature, the open hypothesis A1, not adopted" would remove the apparent tension. Optional.

**Counts confirmed.**
- Part A: 132 rows (118 K, 14 C); no duplicate IDs.
- Part F: 244 drops.
- Part H: 235 corrective rows of r3 — 120 corrected and 115 not unsupported, appendix-a:117 among them as an H-count-citing list (§2).
- Part E: 20 splits.

**No other new error.** The r4 → r5 changes all trace to the review's findings. Part D's statement that the r5 edits touch no census statement other than Main:760 holds: GR:58's bold head is a paragraph title, not a census kind, and ch07:52 is book text.

**OQ-A.**
- **Genuine:** keeping A1 as an open hypothesis makes conditional restatement possible again.
- **Options:** correct.
- **Recommendation (a):** sound, because the owner has not revised Q9 (c) or Q10 (c) and their reason (no accessible test once $|S|$ is free) still holds.
- **The text:** now states the trade-off, that (b) would often be the smaller edit.

## What I could not check

- No guard, census, coverage or build run.
- §2's list of calibration statements comes from a pattern search for the formulas, "1/4 coefficient", "action-scale relation" and "gap equation". A statement of the calibration in words without those strings would not be found.

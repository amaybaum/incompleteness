# Notes for LEDGER-r1

## Commits

- Content read: a read-only checkout of `c3b5f37a354bb26437e2e0165c576a347a63c153`
  (2026-11-13).
- Current `main` when this was written: `dfeec843b Merge pull request #1283` (2026-11-14).
  `git diff --stat c3b5f37a dfeec843` lists one file, `AGENTS.md`: §A.46 items 2 and 4 are
  reworded and item 8 (preserved research records) is added. No `papers/`, `book/` or
  `verification/` file differs, so every line reference in the ledger holds at `dfeec843`.
- The project instructions loaded for this session were the `c3b5f37a` text of `AGENTS.md`. The
  `dfeec843` changes to §A.46 were read from the diff. They bear on landing records, not on what
  the ledger states.

## Read

Owner records, through the GitHub REST API, read-only: #914 comments 6875046763, 6875548603
and 6877420015; #1169 comment 6876591512; the titles of #873, #868, #1211, #1169, #1236 and #914;
the planning block and central question of #1211.

`papers/Main.md`: abstract and §1 (lines 1–98); §3.3 (358–428); §3.4 lines 554–598 in part
(the operational-extension remark, the classical-dimension Proposition, OI⁺, the substratum-source
paragraph, passive observation, the uniform-continuum theorem and its corollary); §4.2–§4.5
(694–726) in full, including the posit ledger (724) and the status ledger (726); lines 214–216,
272, 352, 356 and 770–774 by search.

`papers/GR.md`: abstract (12); §1 (16–32); §2.1–§2.3 to line 60; lines 74, 88, 104, 122 and 162;
§3.3 lines 204–220 and 256; §6 (322–364); §7.1–§7.4 (372–545) by paragraph openings; §8.3
(567–582); §8.4 (583–607); §8.5 line 611; §8.7 (689–697); Appendix A lines 787–863 by paragraph.

`papers/SM.md`: abstract (12–14); §1–§2 (18–60); line 104; §3.1 lines 140–166; §4.1 (220–232);
line 294; lines 374, 390, 434, 464, 543, 589, 641 and 655–669 (theorem statements); §6.5 (799–811);
§6.7 (819–839) by search; §7.6 (1269–1322); §8.3 (1394–1430) by paragraph.

`papers/Substratum.md`: abstract (12–16); §3.1–§3.5 (66–195).

`papers/Introduction.md`: lines 145, 169, 179 and 181. `papers/Structure.md`: headings and line
1118 only.

`book/`: `appendix-a-prediction-status.md` lines 60–120; `ch19-open-problems.md` lines 20–112 and
the "Framework status" line of each later entry; `ch07-gravity.md` lines 12, 44, 46, 110 and 288,
`ch01-observation.md` lines 121, 171 and 185, `ch02-substratum.md` lines 46, 92, 146, 150 and
200, and `ch05-gauge-structure.md` line 17, all found by search.

`verification/`: `lean-manuscript-census.json` (family names, notes and anchors);
`lean/OI_Gauge_Certificates.lean` header; `verification/programmes/oi-qm/PROGRAMME.md` §1, §3.2
and §4; `programmes/black-hole-information/PROGRAMME.md`, `bh01_access_v1/REPORT.md` (verdict
section) and `bh02_scramble_v1/REPORT.md` (verdict section);
`programmes/oi-qm/h-bell/round-hb-1-obligation-shape/preregistration.md` (opening; the round has
no result file on `main`); `programmes/hydrodynamics/round-h-d-a5-status-adjudication/result.md`
(outcome and three answers); `programmes/physical-realization/round-c4-1-physical-discharge/result.md`
(outcome). Lean identifiers cited in the ledger were confirmed by grep to be declared in the named
`OIBridge` modules. A grep for `sorry` and for `axiom` declarations found only occurrences in
comments.

## Not read, or not run

- Not read in full: `papers/Main.md` §2, §3.1, §3.2 and most of §3.4; `papers/SM.md` §3.2,
  §4.2–§4.9 bodies, §5, §6.1–§6.4, §7.1–§7.5 and §8 apart from §8.3; `papers/GR.md` §3.1–§3.2
  bodies, §4, §5 and Appendix A.1–A.6; `papers/Structure.md`; `papers/Methodology.md`; the other
  companion papers; `book/The-Incompleteness-of-Observation-FULL.md` (only the chapter files were
  searched); the book chapters not listed above.
- Not read: `TARGET-THEOREM-r3.md`, `GATE-A-AMEND-r4.md` and `OWNER-QUESTIONS-r4.md`. They are
  on draft pull requests, not on `main`. They are cited only through the owner comments that
  quote them.
- Not run: no Lean build, probe script or computation. Kernel status is as the census and the
  manuscripts state it. "Exhaustive" entries are as the cited records report them.
- Not traced: a Lean statement of the Bell ceiling (no CHSH identifier found in `OIBridge`);
  kernel coverage of the classical-dimension Proposition and of the uniform-continuum theorem (no
  kernel pointer found at `papers/Main.md`:558 and 596); a book mirror of the linearity condition
  on graphs that vary with the state (D4); any source that treats A5 restricted to a reference
  state class; a corpus statement of the sector condition C, of access closure or of an
  extension E. Search terms are recorded in the ledger at D4.

## Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #914 comments 6875046763, 6875548603, 6877420015; #1169 comment 6876591512 | The target and Part 4 wording the ledger serves | Provenance (owner records quoted for scope; no scientific claim rests on them) |
| #873, #1169, #1211, #1236 | Named as accountable Issues in §2.4, §4.1 and §9 | Provenance (planning records; §A.45 rule 1) |
| PR #1289 and the drafts it carries | Not cited as support | Not used |

Every scientific status in the ledger cites a file on `main` at `dfeec843`.

## Method limits

- Statuses are those given at the cited sources. Under §A.46 item 7, the ledger does not
  independently verify the premises it lists.
- "Known not to" in the joint-satisfiability table is used only where a stated result makes the
  premises jointly inconsistent as stated (the linearity condition at `papers/Main.md`:362).
  Every other pair is marked undetermined or consistent, with its reason.
- The ledger uses the AGENTS.md four-layer scheme (Layer 0 to Layer 3) for its classifications.
  `papers/Main.md` §1.5 has its own four layers, which are a different scheme.
- The prompt says that tunable control "leaves linearity". The corpus places that obstruction
  elsewhere: the stated interface operators are monomial, and no bijection realizes a strict
  interpolation toward an exchange (`papers/GR.md`:256). The ledger records the corpus statement.

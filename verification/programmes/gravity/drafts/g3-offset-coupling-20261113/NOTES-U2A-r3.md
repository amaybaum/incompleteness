# NOTES-U2A-r3: working log for G3 unit 2(a), revision 3

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`. The worktree was fast-forward pulled from `origin`; the
  pull reported "Already up to date" at `a87c410d`.
  - `46a548fb` adds r1 (`G3-UNIT2A-r1.md`, `NOTES-U2A-r1.md`).
  - `a87c410d` adds `REVIEW-U2A-r1.md`.
  - The committed r1 files are byte-identical to the writer's r1 (`cmp`). The committed review is
    byte-identical to the working-area copy (`cmp`).
- **Files.**
  - r1 was written in the working area by the writer and committed to the branch at `46a548fb` by the
    coordinator. `NOTES-U2A-r1.md` §1 says "Nothing was committed, pushed or posted"; that was true when
    it was written, and REVIEW-U2A-r1 U-10 notes it is inaccurate at the head.
  - r2 (`G3-UNIT2A-r2.md`, `NOTES-U2A-r2.md` and `RESPONSE-U2A-r1.md`): Written in the working area by
    the writer; committed to the branch at `43cd2cad` by the coordinator.
  - r3 (`G3-UNIT2A-r3.md`, this file and `RESPONSE-U2A-r2.md`) applies CONFIRM-U2A-r2 (`c6d1dd15`) Y-1 to
    Y-5 only. It was written in the working area. The writer did not commit, push or post it.
  - r1 is unchanged.
- **Authority.** #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z): Q4, unit 2(a), paper-only. The
  coordinator's request for r2 is a session message, not an owner record.

## 2. Reading log (additions in r2)

| Source | What was used |
|---|---|
| GR:342 s.1 | "**Ontological commitment.** Classical spacetime is logically prior to QM; QM is emergent." |
| GR:346 s.4 | "exists prior" |
| GR:378(i) | "the emergent vacuum energy inherits an `H`-dependence" |
| GR:162 | the Einstein equations "through Jacobson's relation" |
| GR:12 | G3 open |
| Substratum.md:385, :389 | "the metric is a property of the classical dynamics of the partition boundary"; QM and GR "Both … emergent. Both depend on the trace-out and the partition. … The fundamental object is `(S, φ)`" |
| REVIEW-U2A-r1 | in full |

**Corpus search for B_G (§A.19).** `git grep` at `c3b5f37a` over `papers/*.md` and `book/*.md` for "in
virtue of", "grounds the metric", "grounded in", "ontologically prior/dependent" and "logically prior".

- Relevant hits: GR:342 (the ontological commitment) and Substratum.md:389 with its book mirror
  ch02-substratum.md:212 (both descriptions emergent, both depending on the trace-out and the partition).
- Methodology.md:81 uses "grounded" for a different question.
- No corpus text states whether a term of the gravitational law grounds the metric.

## 3. Order of work

1. Read REVIEW-U2A-r1 in full.
2. Kept §1.2 to §1.5 of r1 unchanged. Added §1.6, which records the reading omitted by r1's enumeration,
   the review-added control C1′ and the corrected reason for one exclusion.
3. Added Reading G (§2.2–2.4). Applied it to the witness (§4.1). Ran C1–C4 and C1′. Re-applied the rule
   (§4.4). The outcome is (C).
4. Attempted both collapses the review allows (§4.5). Ran the corpus search for B_G. Found
   Substratum.md:385–389 and added node A9.
5. Applied §8.3 uniformly (§4.2). Revised the consequences, findings and owner questions.

**On the preregistration.** As REVIEW-U2A-r1 U-6 notes, the claim that r1's rule was written before its
analysis rests on the writer's account; no commit pins it. In r2 the rule's clauses were not edited after
the review. The change of outcome follows from adding a reading to the enumeration, not from a change to
the rule.

## 4. Decisions

1. **The outcome is (C), not (A).** Reading G is valid and not refuted, but whether the witness
   instantiates N4-G is B_G, which neither GR:346 nor the corpus states. Under §1.2 that is "a reading
   whose premise cannot be settled on paper".
2. **The collapse into E is conditional, not established.** It needs G3 (open) and a view of laws the
   corpus does not state, and it would leave (ii) idle (C1′).
3. **The collapse into S fails.** Reading G's exclusion comes from N3-G, N5-G and B_G, not from assuming
   the route ban.
4. **§8.3 runs in two branches**, applied to the witness and to C2(c) alike.
5. **U2A-F2 is ELABORATING**, per U-3.
6. **A9 is added.** The Jacobson route makes B_G's restriction to emergent-class terms load-bearing. It is
   recorded and not adjudicated.
7. **No magnitude claim, no premise adopted, no manuscript change.**

## 5. Checks

- No computation, script or build was run apart from the three permitted checks.
- Algebra: unchanged from r1, and verified by REVIEW-U2A-r1 ("Checked and correct").
- The barred-string scan of the three r2 files finds no hit.
- `diff G3-UNIT2A-r1.md G3-UNIT2A-r2.md` reports 62 hunks, each mapped in RESPONSE-U2A-r1 §3.

| Check (worktree at `a87c410d`) | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. The worktree stayed clean at `a87c410d`.

## 6. Owner questions

QU1–QU5 are in §9 of the record.

- QU2 adds Reading G as a candidate motivation for (ii-L).
- QU3 offers two scopings: the order of explanation or the order of existence.
- QU5 (a) adds B_G as a candidate next unit.

## 7. Limits

- The derivations are by hand.
- The model is exact de Sitter only, under M1.
- Reading G, B_G and the collapse attempts are [P].
- The grounding and laws literature is recalled. No verdict rests on it.
- The §A.31 fixed point is not reached.

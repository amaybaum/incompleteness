# Narrow check of the #1169 synthesis r3

**Verdict: ACCEPT.** The writer's variation on C3, which does not count 3b(i) for T6, is correct.
It is the consistent reading, and my CONFIRM-r2 text was wrong to keep 3b(i) in the T6 cell. With
3b(i) out, the C4 outcome follows: ten sub-forms tie, and there is no single top. C1 and C2 are
applied as specified, C2 verbatim. Nothing changed outside the hunk map. There is one optional nit,
and it needs no further round.

**Object.**
- Branch `research/synthesis-1169-20261113`, fetched by name with full history, at head
  `027f2b93a8f1849b287695c6db5d50fbc96f34b0`.
- Its parent `095bda79` adds `CONFIRM-r2.md`, byte-identical (`cmp`) to the confirmation as
  delivered.
- `027f2b93` adds `SYNTHESIS-r3.md`, `NOTES-r3.md` and `RESPONSE-r2.md`. Every earlier file in the
  directory is unchanged, as checked with `git diff` against `65b70b2d`: SYNTHESIS r1/r2, NOTES
  r1/r2, REVIEW-r1 and RESPONSE-r1.

"r3:n" is `SYNTHESIS-r3.md`. Nothing was run beyond git reads, and nothing was committed, pushed or
posted.

***

## 1. 3b(i) and T6 (r3:94, :432, :443–445)

**The sources.**
- **OA1:488–496.** The target is headed "Single-qubit target, at (ε, K)", and T-C is "consistent
  over `j ≤ K` applications" (OA1:493).
- **OA1 claimed-supply table.** Main's gluing construction meets T-C at "ε" with a finite
  realization (OA1:503). It fails only D, for import reasons. So T-C at `(ε, K)` does not, of
  itself, require carrier growth.
- **OA2:351–353.** This passage concerns *exact* T-C: an exact rotation at `cos θ = 3/5` has
  infinite order, so "Exact T-C … needs growing carriers". Theorem C (OA2:332–347) is a statement
  about exact trace-preserving reversible control at fixed finite `S`.
- **Main:558 and :562.** Main:558 is the exact, all-precision obstruction. Main:562 states that
  finite realizations reach bounded instrument envelopes to any requested finite accuracy. OA1:445
  likewise says "Carrier growth is necessary for exact reproduction by Main:558".

**Conclusion.** At a fixed `(ε, K)`, neither 3b(i) nor 3b(ii) is necessary. Both apply only to exact
variants of the tier, so the uniform treatment at r3:443–445 is right. My CONFIRM-r2 C3 text kept
"3b(i) for exact T-C" in the T6 cell, which applies an exactness requirement that T6 as defined does
not carry.

The remaining T6 support is correct:
- 3a: the configuration identification fails the tier (OA1:474);
- 3e: on route E_f, for T-M.

MM-3's key stays (3, 0, 0): T4 through 3b(iii), T5 through 3c and 3d, T6 through 3a and 3e.

## 2. C4, SQ8 and the notes

**Recount, with every entry unbundled and 3b(i) excluded.** 3b counts for T4 only (3b(iii)), so its
key is (1, 0, 0). The single-target sub-forms at (1, 0, 0) are:
- 1a (T4) and 1b′ (T1);
- 3a (T6), 3b (T4), 3c (T5), 3d (T5) and 3e (T6);
- 4a (T3);
- MM-7 (T7) and MM-8 (T8).

That is ten, as r3:480–481 states. Next comes MM-2 at (0, 3, 2), then 1c, 4c, 4d and MM-5 at
(0, 1, 0), as r3:482 states. 4b is correctly left out, because route B is not a target (r3:442–443).
The tie rule separates MM-7 from MM-8 but leaves no single top.

**Each place where this result is stated follows from it:**
- r3:479–482: "no single top", with the list of ten.
- SQ8 (r3:703–704): "every entry unbundled (ten sub-forms tied, no single top)".
- NOTES-r3:58–62: same outcome. It also records that the order of metric and counts cannot be shown
  from commit history, which answers my CONFIRM-r2 §3 note.

RESPONSE-r2's C4 row correctly says that, had 3b(i) counted, 3b would rank first at (2, 0, 0).

**Nit (optional).** r3:482 stops at the (0, 1, 0) tier. It could add "then MM-9 at (0, 0, 0) and
MM-6 last", for completeness.

## 3. C1 and C2

**C1 is applied.** "μ-G with C5 (held = a function of the present `V`)" appears at all five places
specified: r3:110 (the label and tied-to cells), :144 and :149 (the heading and observer class), :450–452
(the MM-1 rank reason) and :530 (§5, "R-lin with μ-G and C5"). It also appears at NOTES-r3:65. The
sentence I specified, "the step uses D2, so C5 is part of the interface (OA1:345–347, :149)", is at
r3:146.

The writer added two sourced sentences beyond my text, both accurate:
- SA-1(c)'s half-known ready cell is also a ready cell (OA1:346–347);
- OA-1's verdict on the node is "and so does MP-0b" (OA1:353–355).

The second sentence states OA-1's verdict on the whole node, which a change of C5 resolves. It does
not weaken (1b′) inside its stated interface, so it is not an overclaim. The count is unchanged.

**C2 is applied verbatim.** (4d) at r3:302–306 and the dependency line at r3:500–501 match my
CONFIRM-r2 text word for word.

**N1 and N2 are applied** as specified (r3:578, :616).

## 4. Nothing outside the hunk map

- `diff SYNTHESIS-r2.md SYNTHESIS-r3.md` has 16 hunks: 1c1, 8c8, 12c12–14, 92c94, 108c110,
  142–144c144–149, 297–300c302–306, 426c432, 437c443–445, 442–443c450–452, 470–471c479–482,
  489c500–501, 518c530, 566c578, 604c616 and 691–692c703–704. They are exactly the hunks listed at
  RESPONSE-r2:31–33, and each maps to a disposition row.
- The two `diff -u` blocks embedded in RESPONSE-r2 are identical, below their file-header lines, to
  fresh `diff -u` runs of SYNTHESIS r2→r3 and NOTES r2→r3.
- The NOTES diff changes only:
  - the title;
  - the header;
  - lines 58–62 (C4) and line 65 (C1);
  - the new "r3 notes" section at the end.

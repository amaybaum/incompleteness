# Re-check: introductory-paper design, revision 4

- **Objects:** `S/paper/design/OUTLINE-r4.md`, `CONTRIBUTION-r4.md`, `SOURCES-r4.md` and
  `CHANGES-r4.md`, diffed against the r3 files.
- **Read-only.** No repository file changed. No git command was needed.

## Verdict: ACCEPT

RC-A is applied with the exact wording. Nits n-A to n-F are applied. The added sentence is
supported and introduces no overclaim. The r3→r4 diff contains nothing beyond these items and the
header and cross-reference updates of n-C. Revision 3 is unchanged: its sha256 prefixes
`fc5b7d6057af7a67`, `3e9eb43a26e869b6`, `172e073900bd6331` and `9c01d69126429d8c` match
CHANGES-r4.

## Item by item

| Item | Where | Result |
|---|---|---|
| RC-A, §5-h scope | OUTLINE-r4 §5-h (line 226) | Byte for byte the sentence of RECHECK-r3 §2: population notion (2) of Main:334; one-step constant entanglement-breaking channel (Main:286); two-step map the identity; CP-indivisible (Main:326); no classical-memory decomposition (Main:702); no Bell violation. Correct |
| RC-A, non-claim 13 | CONTRIBUTION-r4:182–185 | The re-check's wording, joined to the existing Bell clause. Correct |
| RC-A, item 8 | CONTRIBUTION-r4:107 | "its classical scope" becomes "its scope". Correct |
| RC-A, mirror | SOURCES-r4:135 (§5-h row) | Same scope; cites Main:326 and :334. Consistent with OUTLINE |
| n-A | OUTLINE-r4 §5-h; SOURCES-r4 §5-h | "uniform and independent of the hole card", plus the anticorrelated case. Checked: with b₀ = 1 − h₀, one shuffle gives Γ₁ = the swap permutation and Γ₂ = I = Γ₁², so the game is divisible |
| n-B | OUTLINE-r4:105 | Main:666 is "only as interpretation, class (e) …, never as a result", and the "dissolves" sentence is not carried. Correct |
| n-C | all three headers and cross-references | The titles read "revision 4". A grep finds no `OUTLINE-`, `SOURCES-` or `CONTRIBUTION-` r1–r3 reference left; the only revision names are CHANGES-r* and RECHECK-r* history pointers. Correct |
| n-D | SOURCES-r4:209 | "§5-b to §5-h". Correct |
| n-E | OUTLINE-r4:332–334 | §8 −0.25 plus the variant −0.75 make about 1 pp. §9 is recorded as the next section to give way. The arithmetic is correct. This is only a budget example; decision 1(a) still governs whether the variant is chosen |
| n-F | SOURCES-r4:241–242 | "free of contradiction with the live corpus, though ch18:148 / FULL:4968 remains a conditions-level site against §7-i (R12)". Correct |

## The added sentence

OUTLINE-r4 §5-h adds: "… and a passive look with no replacement also gives 1. So the 1/2 comes
from the intervention on the record, not from observing (RECHECK-r3 §2, an independent exact
check)."

My exact enumeration of the 16 cases (`S/paper/review/r3/mycards.py`) gives these peek odds:

| Peek rule | Odds |
|---|---|
| passive | 1 |
| only the hole card replaced | 1 |
| burn card overwritten | 1/2 |
| both cards replaced | 1/2 |
| revealed card moved to the burn slot | 1/2 |

The sentence attributes the 1/2 to an intervention *on the record*, the burn card. It does not
attribute it to intervention as such, which would be wrong for the hole-only rule. Its wording is
therefore exactly as strong as the computation. No overclaim.

Observation, not a required change: "RECHECK-r3 §2" is design provenance in scratch. In the paper,
the statement should rest on the 16-case hand computation the row already names as its layer, and
should not cite the review.

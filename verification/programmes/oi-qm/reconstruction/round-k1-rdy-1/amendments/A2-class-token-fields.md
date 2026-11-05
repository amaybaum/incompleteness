# A2. Fields of the P1 class token

**Governs:** base lines 156–159, the clauses "in increasing order of each cycle's lexicographically least state" and "the
class token is the first of VOID[row], Z1-VOID, UNDECIDED(Gk), ABSENT, BLIND attained by a member row".

**Addition.** "First" is first in the listed order, VOID[row] before Z1-VOID before UNDECIDED(Gk) before ABSENT before
BLIND. The class token's type is the first type in that order attained by any member row of the branch. Its fields are:

- ABSENT and BLIND: `[𝓘; branch; access]`;
- UNDECIDED: the set of `k` for which some member row ends in UNDECIDED(Gk);
- Z1-VOID: the set of subtypes (IMPORTED, DYN) attained by member rows;
- VOID[row]: the set of member rows that issued it.

Member order fixes the order in which member rows are reported and enters no token. For that order a state is compared
as the sequence of its cells in the order `x_0, …, x_4, y_0, …, y_4`, lexicographically with `0 < 1`.

**Source.** Owner direction, #1031 comment 6649717044 (amaybaum, Claude Code session chat, 2026-11-05): "Resolve the P1
token's "first" ambiguity explicitly before any freeze." The list-order reading is the ruling of the independent review
of PR #1114, #1114 comment 6649791225 (ambiguity A-1). This amendment is adopted by owner decision OD-5, quoted in §12.

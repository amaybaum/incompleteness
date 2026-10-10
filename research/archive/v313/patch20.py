p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/preregistration.md'
t = open(p).read()
R = []
def rep(old, new):
    global t
    assert t.count(old) == 1, old[:70]
    t = t.replace(old, new)

rep("""> **V3-13 retires the checks that re-derive the chronology of the rounds landed before V3.** It
> removes the 1,610 guard predicates `V3-12`'s census retires and the 14 checks it empties, the `V2`
> certificate verifier,""",
"""> **V3-13 retires the checks that re-derive the chronology of the rounds landed before V3.** It
> removes 1,616 guard predicates — the 1,610 `V3-12`'s census retires and six this freeze's
> amendment to the census adds — and the 14 checks the census empties, the `V2` certificate verifier,""")
rep("""| 3. the guard edit | stage 2 removes exactly the 1,610 retired predicates, identified by check, line at `D` and text hash; the 2,492 retained keep their text hashes; the map at `E` is `D`'s without the 14 emptied checks, all `PASS` |""",
"""| 3. the guard edit | adopted with the amendment below: stage 2 removes the census's 1,610 retired predicates and the amendment's six, each identified by check, line at `D` and text hash; the other 2,486 keep their text hashes; the map at `E` is `D`'s without the 14 emptied checks, all `PASS` |""")
rep("""1. every predicate the census classes `redundant`, `retire-history`, `retire-machinery` or
   `retire-whole` — 1,268, 291, 49 and 2, together 1,610 — is removed, located by its line at `D`
   and the first sixteen hexadecimal digits of the SHA-256 of its unparsed text, which must match;""",
"""1. every predicate the census classes `redundant`, `retire-history`, `retire-machinery` or
   `retire-whole` — 1,268, 291, 49 and 2, together 1,610 — and the six of the amendment below are
   removed, 1,616 in all, each located by its line at `D` and the first sixteen hexadecimal digits of
   the SHA-256 of its unparsed text, which must match; an amendment row must also be a `retain` row
   of the census with that hash;""")
rep("""5. the messages of the 41 split checks are replaced by the texts in `messages.json`, and 22 comment
   paragraphs by those in `headers.json`: the headers of 19 retained checks that described retired
   controls, the header of the emptied `R7-BRIDGE` section whose two file readers other checks use,
   and the two paragraphs that introduced `SI-1`'s relocated record reader, one of them removed.
   Each new message and header is the old one with every clause removed that no retained predicate
   tests, joined grammatically, and no clause added; the three section paragraphs name only what
   remains.""",
"""5. the messages of the 41 split checks are replaced by the texts in `messages.json`, and 20 comment
   paragraphs by those in `headers.json`: the headers of 19 retained checks that described retired
   controls, and the header of the emptied `R7-BRIDGE` section, whose two file readers other checks
   use. Each new message and header is the old one with every clause removed that no retained
   predicate tests, joined grammatically, and no clause added; the `R7-BRIDGE` header names only
   what remains.""")
rep("""`retire.py` prints its controls: every retained predicate's unparsed text is present at least as
many times as at `D` (0 missing), 91 checks remain, and the 14 emptied checks are gone. The output
has 14,940 lines and blob `4c1192804dced6d08e5d5d3485ca09121dc25487`; a second run gives the same
bytes.""",
"""`retire.py` prints its controls: 1,616 predicates retired, 1,610 as the census classes them and 6
by the amendment, and 2,486 retained; of the census's 100 `structural` rows, 15 removed with the
emptied checks and 85 kept; every retained predicate's unparsed text present at least as many times
as at `D` (0 missing); 91 checks remain, and the 14 emptied checks are gone. The output has 14,792
lines and blob `d1c6bf660958f870b9e9c8e3d07fe6935ba5f824`; a second run gives the same bytes.
`retire.py --census-only` applies the census without the amendment, the 1,610 transformation
against which the vacuity control measures.

`check` still appends each tag to `CHECK_TAGS`, which after stage 2 nothing reads. It is a line
inside a retained function, `retire.py` does not edit function bodies, and it stays.""")
a = t.index("### Three findings the census left, recorded and not repaired")
b = t.index("### `V2` and `legacy-records`")
t = t[:a] + """### The amendment to `V3-12`'s census

By the owner's direction this freeze reclassifies six predicates the census classes `retain`, and
retires them with the census's 1,610. The census and its record are not edited: the amendment is
this table, and `retire.py` carries it as `AMENDMENT`, refusing a row that is not a `retain` row of
the census with its hash.

| check | line at `D` | text hash | predicate | reclassified as |
|---|---|---|---|---|
| `R7-PC4S` | 17854 | `1459be91d4a5bcbb` | `ok_pc4s &= _pc4s_round1_seal()` | legacy seal read |
| `R7-PC4S` | 17999 | `cfaf77fc616d9bc3` | its mutation on `_base` | legacy seal read |
| `R7-PC4S` | 18000 | `2e5e128c60b1684a` | its mutation on `_sealed` | legacy seal read |
| `R7-PC4S` | 18001 | `3a685893e4885af0` | its mutation on `_merge` | legacy seal read |
| `R7-OLT` | 24113 | `27f4b1d56c51ac71` | `ok_olt &= _olt_supersessions()` (`N15`) | self-satisfying |
| `R7-OLN` | 24549 | `2175b51bb131cb5f` | `ok_oln &= _oln_supersession()` (`N14`) | self-satisfying |

**Legacy seal read.** The four `R7-PC4S` rows compare round `PC4`'s seal record with the values
round 1 set, through the guard's record reader. The census's resolver could not resolve that
reader's path and retained them as unresolved, its hazard 2; its thirteen adjudications class the
same comparison for `R7-HYE` `redundant`. They protect no fact that `legacy-records` does not: the
seal records are records of the closed namespace `verification/seals`. Keeping them would leave
seal-reading machinery in a guard that, after this round, reads none.

**Self-satisfying.** `N15` and `N14` look in the guard's own source for strings of `SI-3`'s
supersession table: two object ids, `_seal_field('SI3', 'sealed_head')`, `_SI3_MANIFESTED`,
`_SI3_MANDATED_BASE`, and `R7-OLT`'s declared-branch baseline equality. After the 1,610
transformation each string occurs only in the predicate's own literal, so neither can fail on any
change to the rest of the guard. `N14` keeps one negative conjunct, the absence of a statement that
reads `_MANIFEST_BASELINE`, a name the transformed guard no longer defines.

**The controls**, in `controls.py`, run at the stage 1 commit:

- `controls.py pc4s <repository> <D>` evaluates the four `R7-PC4S` rows with exactly the guard
  definitions they reach, executed from the guard at `D` over `D`'s tree with every file read and
  directory listing recorded and no child process allowed. Frozen outcome: all four hold; 35 files
  read, 34 of them records of the legacy-records manifest (every record under
  `verification/seals/`) and the 35th `verification/migration-manifest.json`, read as a lookup;
  one directory listed, `verification/seals`, a closed namespace; and a one-byte change to
  `verification/seals/PC4.json` makes the unmutated predicate fail.
- `controls.py vacuity <repository> <commit> <D>` builds the 1,610 transformation of the guard at
  `D` and evaluates `N15` and `N14`, taken from it, on its text, on its text with every occurrence
  of their strings outside their own definitions removed, and on their own definitions alone.
  Frozen outcome: the strings occur 0 times outside the definitions and all six evaluations hold;
  the countercontrols fail as they must — each predicate on a text without its strings, and `N14`
  on the guard with the statement it forbids appended.

The same evaluations on the guard at `D`, which the control reports without requiring them, also
hold: the strings then occurred outside the definitions, 10 times for `N15` and once for `N14`,
but removing them changes neither verdict. The two predicates were self-satisfying at `D` as well;
the transformation removes the occurrences that made it look otherwise.

**The count.** 1,616 retired and 2,486 retained. No `structural` row moves: the six predicates'
checks keep their other predicates, so their accumulators and bookkeeping stay. What goes with the
six is dead code, removed by the same fixpoint and counted as statements, not predicates: the
record reader, schema and accessor with their constants, and the two source reads.

""" + t[b:]
rep("""- **`C2`** (stage 2): `retire.py` exits 0 printing `retained predicates missing: 0` and
  `91 checks remain`; the guard has its frozen blob and compiles; `controls.py history` reports 0
  sites at stage 2 and 213 at `D`.""",
"""- **`C2`** (stage 2): `retire.py` exits 0 printing `1616 predicates retired, 1610 as the census
  classes them and 6 by the amendment; 2486 retained`, `retained predicates missing: 0` and
  `91 checks remain`; the guard has its frozen blob and compiles; `controls.py history` reports 0
  sites at stage 2 and 213 at `D`; `controls.py pc4s` and `controls.py vacuity` give their frozen
  outcomes.""")
rep("""| `Numerical probes` | the companion probes, and the guard's 2,492 retained predicates in 91 checks, reading no history |""",
"""| `Numerical probes` | the companion probes, and the guard's 2,486 retained predicates in 91 checks, reading no history |""")
rep("""2. It retires no check of content: the 2,492 predicates the census retains keep their text, and
   the new messages and headers say less than the old ones, never more.""",
"""2. It retires no check of content beyond the census and the amendment: the 2,486 predicates they
   retain keep their text, and the new messages and headers say less than the old ones, never
   more.""")
rep("""| `V313-1` | does stage 2 remove exactly the census's retirements and keep the rest? | `GUARD-RETIRED` | holds, strong |""",
"""| `V313-1` | does stage 2 remove exactly the census's retirements and the amendment's six, and keep the rest? | `GUARD-RETIRED` | holds, strong |""")
for old, new in (("`86bcdceb345e0c6173e0f7cd162bcb7e03113dbc`", "`1e549b70d131629d45092fdd807c6d61a6fab0d6`"),
                 ("`d9f2fe01d18d41df75fd6a71fd3eb5ece1c3c9ac`", "`96e82a37fe24342a2022829ae78fbf1cd9f0e888`"),
                 ("`83e0a9c1fc4a591de652478654371032d551b16b`", "`8c727cad183a54048064013b3805013d35ed9fc1`"),
                 ("`799c238cc85012f85762590c8ff9ec9dd5051327`", "`0870fdecc54e5a8545b2ab1e72c108c8a4adaa51`"),
                 ("`4c1192804dced6d08e5d5d3485ca09121dc25487`", "`d1c6bf660958f870b9e9c8e3d07fe6935ba5f824`"),
                 ("`c5c7c35407774bb21d531d28897d3dd90cca0dd3`", "`75f767b6ce7dbff72121ba4fb26a449d95880557`")):
    rep(old, new)
open(p, 'w').write(t)

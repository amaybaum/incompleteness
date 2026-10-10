p = 'preregistration.md'
s = open(p).read()
R = []
def r(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)

r("""**Corrected: the damage.** `V3-13`'s result note names five retained statements its transformation
deleted. Measured at `D` by comparing every retained function and module-level block with its text
in `V3-13`'s stage 2 guard, the transformation deleted **seven**.""",
"""**Corrected: the damage.** `V3-13`'s result note names five retained statements its transformation
deleted. Measured at `D`, the transformation deleted **ten**. Seven were found by comparing every
retained function and module-level block with its text in `V3-13`'s stage 2 guard. The other three
were found when this round's first rehearsal ran the guard in CI (see the execution evidence
below).""")

r("""| 26777–26778 | `_cgr_token` | `if depth == 0: break` | the emptied-block rule |
""", """| 26777–26778 | `_cgr_token` | `if depth == 0: break` | the emptied-block rule |
| 14250–14252 | `R7-A12P`'s mutation control `m13` | the loop setting the family's status to `kernel-only` in the copied registry | the sweep saw a store into the loop variable `_f`, not into the registry `_f` belongs to |
| 16548–16551 | `R7-A6P`'s mutation control `m8` | the loop appending an `SM.md` anchor to the copied registry | the same |
| 19401–19404 | `R7-A6I`'s mutation control `m15` | the loop appending an `SM.md` anchor to the copied registry | the same |
""")

r("""Two things follow:
- The two rows at 193 and 292 were missed by `V3-13`'s own damage census, which looked only for
  `if` blocks holding nothing but control flow.
- The guard at `V3-13`'s candidate head crashed in `R4` before `R5` ran, so the lost `changed = True`
  would have failed `R5` next.""",
"""Three things follow:
- The rows at 193 and 292 were missed by `V3-13`'s own damage census, which looked only for `if`
  blocks holding nothing but control flow.
- The guard at `V3-13`'s candidate head crashed in `R4` before `R5` ran, so the lost
  `changed = True` would have failed `R5` next.
- Without the last three rows, each of those mutation controls tests an unmutated registry, and
  its check fails closed; the candidate head never reached them.""")

r("""`retire.py` is `V3-13`'s transformation with three changes.""",
  """`retire.py` is `V3-13`'s transformation with four changes.""")

r("""   292, and the dead store at 2128.
""", """   292, and the dead store at 2128.
4. **A mutation reaches through aliases.** A mutation of a name is also a mutation of what that
   name's reaching definition takes its value from: a loop's iterable, an assigned name or
   subscript, a with-item. Depth is followed: an element of a value is one level down, a shallow
   copy (`dict(x)`, `list(x)`, `sorted(x)` and the like) shares only what lies below its top level,
   and a deep copy (`json.loads`, `copy.deepcopy`) shares nothing. So a loop that mutates a copied
   registry through its loop variable lives while the registry is read.
""")

r("""**Its output:** blob `f4fee29505b572161a22eccee3ae8b35aa48ab61`, 14,805 lines. A second run gives
the same bytes and the same ledger. Its difference from `V3-13`'s stage 2 guard is exactly the
seven damaged sites restored plus the kept dead store at 2128, and nothing else.""",
"""**Its output:** blob `8dad60d0aac870fced7deeec44c0dbdfcb3d45de`, 14,816 lines. A second run gives
the same bytes and the same ledger. Its difference from `V3-13`'s stage 2 guard is exactly the ten
damaged sites restored plus the kept dead store at 2128, and nothing else.""")

r("""It holds 559 splices. Their reasons are:
- 299 census and 4 amendment;
- 6 each of `census-structural` and `emptied-check`;
- 369 dead code, 8 counter and 23 emptied block;""",
"""It holds 556 splices. Their reasons are:
- 299 census and 4 amendment;
- 6 each of `census-structural` and `emptied-check`;
- 366 dead code, 8 counter and 20 emptied block;""")

r("""| `S4` | the seven damaged sites are in no splice |
| `S5` | inside every surviving module-level block, every wholly-spliced statement is a retired predicate, a counter increment, or a block of nothing but those and control flow |""",
"""| `S4` | the ten damaged sites are in no splice |
| `S5` | inside every surviving module-level block, every wholly-spliced statement is a retired predicate, a counter increment, or a block of nothing but those and control flow |
| `S6` | every wholly-spliced module-level statement that is not a retired predicate and changes an object in place changes nothing a surviving statement reads. The object is followed back through its name's definitions with the depth rule above. A name reached must not be read by a surviving module-level statement after the change and before it is rebound, nor by a surviving function |""")

r("""On the real inputs every check holds:
- 559 splices;
- 1,616 predicates retired and 2,486 retained;
- 257 retained functions untouched;
- of 1,635 control-flow statements, 1,228 removed with their governing block;
- 7 regression sites preserved;
- 449 surviving module-level blocks.

`preserve.py --self-test` then requires each of twelve mutants to fail the checks named:

| mutant | must fail |
|---|---|
| each of the seven damaged sites deleted through a consistent splice | `S4`, plus `S2` inside a function or `S5` in a module-level block, plus `S3` where the site is `continue` or `break` |""",
"""On the real inputs every check holds:
- 556 splices;
- 1,616 predicates retired and 2,486 retained;
- 257 retained functions untouched;
- of 1,635 control-flow statements, 1,228 removed with their governing block;
- 10 regression sites preserved;
- 452 surviving module-level blocks;
- 49 removed in-place changes, none to an object a survivor reads.

`preserve.py --self-test` then requires each of fifteen mutants to fail the checks named:

| mutant | must fail |
|---|---|
| each of the ten damaged sites deleted through a consistent splice | `S4`, plus `S2` inside a function, `S5` inside a module-level block, or `S6` for a top-level statement, plus `S3` where the site is `continue` or `break` |""")

r("""guard by a line diff; this diff-derived ledger serves only here. `L1`, `L2` and `S1` hold, and `S2`,
`S3`, `S4` and `S5` fail, with `S4` naming all seven sites. So the checker rejects the guard `V3-13`
produced. `S5` also names the dead store at 2128.""",
"""guard by a line diff; this diff-derived ledger serves only here. `L1`, `L2` and `S1` hold, and `S2`,
`S3`, `S4`, `S5` and `S6` fail, with `S4` naming all ten sites. So the checker rejects the guard
`V3-13` produced. `S5` also names the dead store at 2128.""")

r("""`V3-13`'s stage 2 guard differs from this round's output only by the seven sites and the line at
2128, and this round's ledger passes `S2` and `S3`.""",
"""`V3-13`'s stage 2 guard differs from this round's output only by the ten sites and the line at
2128, and this round's ledger passes `S2` and `S3`.""")

open(p, 'w').write(s)
print('ok')

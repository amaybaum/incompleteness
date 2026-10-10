p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/preregistration.md'
t = open(p).read()
old = """5. the messages of 41 split checks are replaced by `messages.json` and 22 header comments by
   `headers.json`. Each new message is the old one with every clause removed that no retained
   predicate tests, and no clause added; each header likewise."""
new = """5. the messages of the 41 split checks are replaced by the texts in `messages.json`, and 22 comment
   paragraphs by those in `headers.json`: the headers of 19 retained checks that described retired
   controls, the header of the emptied `R7-BRIDGE` section whose two file readers other checks use,
   and the two paragraphs that introduced `SI-1`'s relocated record reader, one of them removed.
   Each new message and header is the old one with every clause removed that no retained predicate
   tests, joined grammatically, and no clause added; the three section paragraphs name only what
   remains."""
assert t.count(old) == 1
open(p, 'w').write(t.replace(old, new))

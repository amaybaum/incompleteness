import json
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/'
h = json.load(open(S + 'headers-all.json'))
pc = h['R7-PC4S']
for a, b in (("its seal constants touched, or", "its seal record touched, or"),
             ("and checks round 1's seal constants unmoved.", "and checks round 1's seal record unmoved.")):
    assert pc.count(a) == 1, a
    pc = pc.replace(a, b)
h['R7-PC4S'] = pc
h['R7-OLT'] = ("# ---- R7-OLT: Track B act 21 -- the rigidity of the cross-time laws act 18 opened, re-frozen at\n"
               "# act 20's certified naturality. The guard checks the module's eight budgeted definitions and\n"
               "# its axiom table, and the frozen P0 sentence VERBATIM in the ROADMAP.")
json.dump(h, open(S + 'headers-all.json', 'w'), indent=1, ensure_ascii=False)
open(S + 'headers-all.json', 'a').write('\n')
p = S + 'retire.py'
t = open(p).read()
old = """4. dead code removed to a fixpoint: a module-level function no remaining code names, an assignment
   or in-place mutation of a name no remaining code reads, an expression statement that reads a
   name nothing defines any longer, an import nothing uses, and a comment-only paragraph whose code
   is gone;
5. the messages of the split checks replaced by the texts in <messages.json>, when given;
6. the comment paragraphs describing the base and seal constants that round SI-3 removed deleted,
   and the header paragraphs of the checks named in <headers.json> replaced by its texts.
"""
new = """4. dead code removed to a fixpoint: a function defined at module level that no remaining code
   names, an assignment or in-place mutation of a name no remaining code reads (a plain assignment
   earlier in the same statement list rebinding the name for what follows), an expression statement
   that reads a name nothing defines any longer, an import nothing uses, a counter increment that
   counted only removed predicates, and a loop left binding only such names;
5. the comments whose code is gone: a comment block all of whose following code is removed, a
   comment-only paragraph all of whose code up to the next such paragraph or section header is
   removed, a paragraph left comment-only by the removals, the header and end marker of every check
   removed whole, the paragraphs describing the base and seal constants round SI-3 removed, and the
   drift-control lines in DRIFT_LINES;
6. the messages of the split checks replaced by the texts in <messages.json>, and the header
   paragraphs named in <headers.json> replaced by its texts, when given.
"""
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)

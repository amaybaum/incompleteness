"""Adversarial parity test of DESIGN-v5.4's selection-and-application rule against P's own variant(),
check() uniqueness, and apply_edits(). My implementation follows the design text; 'occurs exactly once' is
tested under two readings: (N) non-overlapping count, Python str.count, which is P's; (O) overlapping
occurrences (a find loop advancing by one). Random cases use a small alphabet so that overlaps and
interactions between edits are frequent. No splice concept: compares selection, refusal and final text."""
import importlib.util, hashlib, os, random, json
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
assert hashlib.sha256(open(os.path.join(D, 'edits_check.py'), 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('pec', os.path.join(D, 'edits_check.py')); ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
class Src:
    def __init__(self, t): self.t = t
    def read(self, f): return self.t[f]
    def files(self): return list(self.t)
def count_O(text, s):
    if s == '': return len(text) + 1
    n, i = 0, text.find(s)
    while i >= 0: n += 1; i = text.find(s, i + 1)
    return n
def select(e, text, cnt):
    for o, n in [(e['old'], e['new'])] + ([(e['old_step2'], e['new_step2'])] if 'old_step2' in e else []):
        if cnt(text, o) == 1: return o, n
    return None, None
def tool(edits, texts, cnt):
    """v5.4 sec. 6.1: uniqueness at H for every edit; then apply in list order on a running copy."""
    for e in edits:
        if select(e, texts[e['file']], cnt)[0] is None: return ('refuse-H', None)
    run = dict(texts); sel = []
    for e in edits:
        o, n = select(e, run[e['file']], cnt)
        if o is None: return ('refuse-lost', None)
        sel.append(o); run[e['file']] = run[e['file']].replace(o, n, 1)
    return ('ok', (tuple(sel), json.dumps(run, sort_keys=True)))
def p(edits, texts):
    for e in edits:
        if ec.variant(e, texts[e['file']])[0] is None: return ('refuse-H', None)
    run = dict(texts); sel = []
    for e in edits:
        o, n, _ = ec.variant(e, run[e['file']])
        if o is None: return ('refuse-lost', None)
        sel.append(o); run[e['file']] = run[e['file']].replace(o, n, 1)
    # P's own check() on the same data must agree with my transcription of its loop
    return ('ok', (tuple(sel), json.dumps(run, sort_keys=True)))
def p_check(edits, texts):
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        try: return ec.check({'edits': edits}, Src(texts), simulate=False, quiet=True)
        except Exception as x: return 'exc'
crafted = [
 ('overlap: old "aa" in "aaa"', [{'id': 'a', 'file': 'f', 'old': 'aa', 'new': 'b'}], {'f': 'xaaay'}),
 ('empty old', [{'id': 'a', 'file': 'f', 'old': '', 'new': 'b', 'old_step2': 'x', 'new_step2': 'y'}], {'f': 'x'}),
 ('old == old_step2', [{'id': 'a', 'file': 'f', 'old': 'q', 'new': 'r', 'old_step2': 'q', 'new_step2': 's'}], {'f': 'q'}),
 ('edit 2 old created by edit 1', [{'id': 'a', 'file': 'f', 'old': 'A', 'new': 'BB'}, {'id': 'b', 'file': 'f', 'old': 'BB', 'new': 'C', 'old_step2': 'A', 'new_step2': 'C'}], {'f': 'xAy'}),
 ('variant 2 only after edit 1', [{'id': 'a', 'file': 'f', 'old': 'one two', 'new': 'one 2'}, {'id': 'b', 'file': 'f', 'old': 'two three', 'new': 'II three', 'old_step2': '2 three', 'new_step2': 'II three'}], {'f': 'one two three'}),
 ('overlap in variant choice', [{'id': 'a', 'file': 'f', 'old': 'aba', 'new': 'X', 'old_step2': 'ab', 'new_step2': 'Y'}], {'f': 'ababa'}),
]
for label, edits, texts in crafted:
    pt = p(edits, texts); tn = tool(edits, texts, str.count); to = tool(edits, texts, count_O)
    print('%-32s P=%-11s tool(N)=%-11s %s tool(O)=%-11s %s  P.check=%s' % (label, pt[0], tn[0], 'same' if tn == pt else 'DIFF', to[0], 'same' if to == pt else 'DIFF', p_check(edits, texts)))
random.seed(20261123)
diffN = diffO = 0; n_cases = 20000; mism_check = 0
for _ in range(n_cases):
    alpha = 'ab '
    text = ''.join(random.choice(alpha) for _ in range(random.randint(3, 14)))
    edits = []
    for k in range(random.randint(1, 3)):
        e = {'id': 'e%d' % k, 'file': 'f', 'site': 's', 'part': 1, 'old': ''.join(random.choice(alpha) for _ in range(random.randint(1, 3))),
             'new': ''.join(random.choice(alpha) for _ in range(random.randint(0, 3)))}
        if random.random() < 0.6:
            e['old_step2'] = ''.join(random.choice(alpha) for _ in range(random.randint(1, 3)))
            e['new_step2'] = ''.join(random.choice(alpha) for _ in range(random.randint(0, 3)))
        edits.append(e)
    pt = p(edits, {'f': text})
    if (pt[0] != 'refuse-H') != bool(p_check(edits, {'f': text})): mism_check += 1
    if tool(edits, {'f': text}, str.count) != pt: diffN += 1
    if tool(edits, {'f': text}, count_O) != pt: diffO += 1
print('random cases', n_cases, '| tool(N) differs from P:', diffN, '| tool(O) differs from P:', diffO, '| my P transcription vs P.check uniqueness verdict mismatches:', mism_check)

"""DESIGN-v5.5 sec. 6.1 rule (my implementation from the text) against P's own variant()/apply: uniqueness at H,
in-order application with P's str.count selection, segment-based offset mapping (occurrence must lie inside one
original-H segment), splices built from the mapping, and the final text rebuilt from disjoint splices at H.
Random cases use a different seed and generator than the writer's; plus crafted overlap and chained cases; plus A1."""
import importlib.util, hashlib, os, random, json, subprocess, collections
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
assert hashlib.sha256(open(os.path.join(D, 'edits_check.py'), 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('pec', os.path.join(D, 'edits_check.py')); ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
def p_apply(edits, texts):
    for e in edits:
        if ec.variant(e, texts[e['file']])[0] is None: return 'refuse', None
    run = dict(texts)
    for e in edits:
        o, n, _ = ec.variant(e, run[e['file']])
        if o is None: return 'refuse', None
        run[e['file']] = run[e['file']].replace(o, n, 1)
    return 'ok', run
def v55(edits, texts):
    for e in edits:
        if ec.variant(e, texts[e['file']])[0] is None: return 'refuse-H', None
    segs = {f: [('H', 0, t)] for f, t in texts.items()}   # ('H', h_char_start, text) | ('I', None, text)
    splices = collections.defaultdict(list)
    for e in edits:
        f = e['file']; run = ''.join(s[2] for s in segs[f])
        o, n, _ = ec.variant(e, run)
        if o is None: return 'refuse-lost', None
        p = run.index(o); pos = 0; k = None
        for idx, s in enumerate(segs[f]):
            if pos <= p and p + len(o) <= pos + len(s[2]) and (s[0] == 'H') and not (len(o) == 0 and False):
                k = idx; break
            pos += len(s[2])
        if k is None: return 'refuse-chained', None
        s = segs[f][k]; off = p - pos; hstart = s[1] + off
        h = texts[f]; bs = len(h[:hstart].encode()); be = bs + len(o.encode())
        splices[f].append((bs, be, n))
        segs[f][k:k + 1] = [('H', s[1], s[2][:off]), ('I', None, n), ('H', hstart + len(o), s[2][off + len(o):])]
    out = {}
    for f, t in texts.items():   # rebuild from disjoint splices at H
        b = t.encode(); res = b''; last = 0
        for bs, be, n in sorted(splices[f]):
            if bs < last: return 'refuse-overlap', None
            res += b[last:bs] + n.encode(); last = be
        out[f] = (res + b[last:]).decode()
    return 'ok', out
def cmp(edits, texts):
    pr = p_apply(edits, texts); vr = v55(edits, texts)
    if pr[0] == 'refuse': return 'both-refuse' if vr[0] != 'ok' else 'V55-ACCEPTS-P-REFUSES'
    if vr[0] == 'ok': return 'both-ok-same' if vr[1] == pr[1] else 'TEXT-DIFFERS'
    return 'extra-' + vr[0]
crafted = [('overlap "aa" in "xaaay"', [{'id': 'a', 'file': 'f', 'old': 'aa', 'new': 'b'}], {'f': 'xaaay'}),
 ('chained: edit 2 old created by edit 1', [{'id': 'a', 'file': 'f', 'old': 'A', 'new': 'BB'}, {'id': 'b', 'file': 'f', 'old': 'BB', 'new': 'C', 'old_step2': 'A', 'new_step2': 'C'}], {'f': 'xAy'}),
 ('chained across image boundary', [{'id': 'a', 'file': 'f', 'old': 'one two', 'new': 'one 2'}, {'id': 'b', 'file': 'f', 'old': 'two three', 'new': 'II three', 'old_step2': '2 three', 'new_step2': 'II three'}], {'f': 'one two three'}),
 ('occurrence spanning a deletion', [{'id': 'a', 'file': 'f', 'old': 'XY', 'new': ''}, {'id': 'b', 'file': 'f', 'old': 'aXYb', 'new': 'q', 'old_step2': 'ab', 'new_step2': 'q'}], {'f': 'zaXYbz'}),
 ('adjacent independent edits', [{'id': 'a', 'file': 'f', 'old': 'ab', 'new': 'X'}, {'id': 'b', 'file': 'f', 'old': 'cd', 'new': 'Y'}], {'f': 'abcd'}),
 ('unicode offsets', [{'id': 'a', 'file': 'f', 'old': 'é', 'new': 'e'}, {'id': 'b', 'file': 'f', 'old': 'ü!', 'new': 'u'}], {'f': 'aéb ü!'}),
 ('edit 2 selects variant 2 after edit 1 removes old', [{'id': 'a', 'file': 'f', 'old': 'k1', 'new': ''}, {'id': 'b', 'file': 'f', 'old': 'k1 m', 'new': 'Z', 'old_step2': 'm', 'new_step2': 'Z'}], {'f': 'xk1 m'})]
for label, e, t in crafted: print('%-46s %s' % (label, cmp(e, t)))
random.seed(424242); tally = collections.Counter()
for _ in range(30000):
    alpha = random.choice(['ab ', 'abc', 'aé b'])
    text = ''.join(random.choice(alpha) for _ in range(random.randint(2, 16)))
    edits = []
    for k in range(random.randint(1, 4)):
        e = {'id': 'e%d' % k, 'file': 'f', 'old': ''.join(random.choice(alpha) for _ in range(random.randint(1, 3))), 'new': ''.join(random.choice(alpha) for _ in range(random.randint(0, 3)))}
        if random.random() < 0.5: e['old_step2'] = ''.join(random.choice(alpha) for _ in range(random.randint(1, 3))); e['new_step2'] = ''.join(random.choice(alpha) for _ in range(random.randint(0, 3)))
        edits.append(e)
    tally[cmp(edits, {'f': text})] += 1
print('random 30000:', dict(tally))
# A1
H = '53c6601a10419b6b333cc992474272501ab542af'
edits = json.load(open(os.path.join(D, 'edits.json')))['edits']; led = json.load(open(os.path.join(D, 'ledger.json')))
texts = {f: subprocess.run(['git', '-C', '<repo>', 'show', '%s:%s' % (H, f)], capture_output=True, check=True).stdout.decode() for f in sorted({e['file'] for e in edits})}
print('A1:', cmp(edits, texts))

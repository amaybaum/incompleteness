#!/usr/bin/env python3
"""Checker for the A1 deletion edit list (edits.json). Standard library only. It never writes a manuscript.

Usage (from the repository root):
  python3 -I -B verification/audits/foundations/a1exit-deletion-20261121/edits_check.py --commit REV [--simulate]
  python3 -I -B .../edits_check.py --tree DIR [--simulate]
  python3 -I -B .../edits_check.py --static
  python3 -I -B .../edits_check.py --self-test

--commit REV  reads each target file as `git show REV:path` and checks that every edit's old string ("old",
              or "old_step2" where given) occurs exactly once in its file. Exit status 1 on any failure.
--tree DIR    the same on a directory holding papers/ and book/ (for example a projected integration).
--simulate    additionally applies the edits in memory only (nothing is written) and checks the result:
              the residual scan (A1 pointers and their paraphrases, over every papers/*.md and book/*.md
              file of the commit or tree under test) must be empty apart from the listed false positives;
              every criterion-5 or finiteness-paraphrase hit on a changed line must be finite-scoped,
              interrogative or open in its sentence; Main's posit ledger must keep items (i) and (iii)-(xiv),
              print no item (ii) and say "Thirteen items"; the reconstruction counts must read five.
--static      checks the replacement strings ("new" and "new_step2") alone: infinity-assertion scan,
              register scan of §A.32/§A.33 on added text and identifier rule (zero hits each); and
              cross-checks the edit sites against the ledger site map (every ptr site has an edit, every
              ptr edit is at a mapped ptr site), reading the map's pin with git.
"""
import argparse, json, os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
EDITS = os.path.join(HERE, 'edits.json')
SITEMAP = os.path.join(ROOT, 'verification', 'audits', 'foundations', 'a1exit-ledger-20261120', 'sitemap.json')
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'

# Residual pointer scan: ledger P0 core patterns P1, P2, P5, the B1 "finiteness posit" pattern, and the
# paraphrases of the posit found by the round-1 review.
PTR = re.compile(r'\bA1\b|[Tt]otal[- ]finiteness|totally finite|(?<![A-Za-z])finite total (system|configuration|state)'
                 r'|posit \(ii\)|ledger item \(ii\)|item \(ii\) of the posit|ledger \(ii\)|posit-\(ii\)|[Ff]initeness posit'
                 r'|[Ff]initeness hypothesis|configuration finiteness|hypothesis of finite information'
                 r'|open (?:physical )?(?:hypothesis|posit|premise)[^.;]{0,60}finit|finit[^.;]{0,80}open (?:physical )?(?:hypothesis|posit|premise)')
RESIDUAL_ALLOW = [
    ('book/appendix-b-derivations.md', '(A1)', 'ledger FP: anomaly condition (A1), appB:235/246'),
    (FULL, '(A1)', 'ledger FP: FULL mirror of the appB anomaly conditions'),
    ('papers/GR.md', 'For a finite total system, restrict it', 'finite-scope wording of ledger X-70 (P2 matches "finite total system")'),
]
# Ledger criterion-5 patterns (ledger_check.EXTENDED_PATTERNS) and P0 finiteness paraphrases (P0 core P3, P4,
# P8; paraphrase P6, P10), applied to lines the edit list changes.
CRIT5 = re.compile(r'[Ff]initeness posit|posit A1|finite[- ]information|(?<![A-Za-z])finite (periodic )?lattice(?! spacing)'
                   r'|finite torus|periodic quotient|[Rr]ecurrence (cycle|scale)|recurrence-cycle|classical-dimension'
                   r'|N < \\infty|fixed finite carrier|(?<![A-Za-z])finite (world|universe)\b|(?<![A-Za-z])finite configuration space'
                   r'|(?<![A-Za-z])finite cardinality|\$S\$ (is )?finite')
# Phrases that name a finite object (finite representative, substratum, bijection, model, carrier) are finite-scope
# statements by themselves and are not CRIT5 hits; a CRIT5 hit needs one of these scopes in its sentence.
SCOPED = re.compile(r'finite (?:\w+ )?representative|finite substrat|finite model|finite OI|finite class|finite-only'
                    r'|(?:on|for) a (?:fixed )?finite (?:\w+ )?(?:representative|substrat\w*|model|set|system|realization)'
                    r'|for a finite \$S\$|when \$S\$ is finite|finite (?:total )?system|finite set|finite scope'
                    r'|finite candidate|finite periodic case|finite hidden dynamics|finite realization|qualified case'
                    r'|\bneither\b')
# Weak markers (a question, "whether", "open", a disclaimer) exempt a criterion-5 hit only when the sentence does not
# also assert finiteness of the universe, nature, the substratum or S.
WEAK = re.compile(r'\?|\bwhether\b|\bopen\b|not asserted|left open|not fixed|does not identify|unspecified cardinality')
ASSERTS_FINITE = re.compile(r'(?<!\w)(?:the universe|nature|the substratum|the world|\$S\$|S|the total configuration space)'
                            r' (?:is|are|be) (?:a )?finite\b|\b(?:is|are) a finite (?:universe|world|substratum)\b', re.I)
# Hits that a weak marker never exempts: they state a property of the configuration space itself.
STRONG_ONLY = re.compile(r'finite configuration space|finite cardinality', re.I)
CRIT5_ALLOW = [
    ('book/ch02-substratum.md', 'The output of Stage 1 is a triple $(S, \\varphi, V)$ with $S$ finite',
     'Stage 1 constructs a finite realization per law (ledger X-31), inside Theorem 23\'s finite scope'),
    (FULL, 'The output of Stage 1 is a triple $(S, \\varphi, V)$ with $S$ finite', 'FULL mirror of ch02:88'),
    ('papers/Structure.md', 'a discretization scheme for quantum gravity with manifestly finite configuration space',
     'Str:339 describes causal dynamical triangulations, another programme; no claim about the OI substratum (unchanged sentence on a changed line)'),
]
# Infinity assertions that no replacement string may introduce (owner decision: cardinality neutrality).
INF = re.compile(r'(?:\b(?:is|are|be|being|been)\s+infinite\b(?!-))|\b(?:is|are)\s+not\s+finite\b|\binfinitely many\b'
                 r'|\bcountably infinite\b|\buncountably infinite\b'
                 r'|\binfinite (?:substratum|universe|configuration space|carrier|set|number|lattice|system)\b'
                 r'|\|S\|\s*=\s*(?:\\infty|∞)|\bS\s+is\s+infinite\b|\binfinite in (?:extent|size|cardinality)\b'
                 r'|\bthermodynamic limit\b|\bunbounded (?:size|number of (?:sites|configurations|states))\b'
                 r'|\bwithout bound in size\b|\bof infinite cardinality\b|\bno finite bound\b|\bof infinite extent\b'
                 r'|\bextending without end\b|\bnon-finite\b|\binfinitely extended\b|\b[Ff]initeness\b[^.;]{0,40}\bfails\b(?! to)')
# The only exempt form: a symmetric "neither ... finite ... nor ... infinite" disclaimer, the match inside it.
NEUTRAL = re.compile(r'\bneither (?:that )?(?:the substratum|the universe|it|\$S\$|S) (?:is|be) finite nor (?:that )?'
                     r'(?:the substratum|the universe|it|\$S\$|S) (?:is|be) infinite\b')
# §A.32/§A.33 register families and the history-phrase family on added text.
REG = re.compile(r'\b(now|no longer|formerly|previously|corrected|correction|is not listed|withdrawn|retired|superseded'
                 r'|in its current form|the corrected form|as redefined|is now settled|earlier revision\w*|has been removed'
                 r'|was removed|used to|should not be read|the reader should note|honest(?:ly)?|discipline maintained'
                 r'|earlier versions?|originally(?: a posit)?|at one time|hitherto)\b', re.I)
CAPS = re.compile(r'(?<![A-Za-z\\])[A-Z]{3,}(?![A-Za-z])')
CAPS_OK = {'REV', 'OIQ', 'QFT', 'LQG', 'BFSS', 'BMN', 'IKKT', 'ETH', 'BQP', 'CPTP', 'GR', 'SM', 'QM', 'CP', 'MWI', 'PBR',
           'RIG', 'ZFC', 'LHC', 'UV', 'IR', 'CKM', 'PMNS', 'JUNO', 'CSG'}
ROMAN = ['i', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv']


def load():
    with open(EDITS, encoding='utf-8') as f:
        return json.load(f)


class Source:
    def __init__(self, commit=None, tree=None, fn=None, files=None):
        self.commit, self.tree, self.fn, self._files = commit, tree, fn, files

    def read(self, path):
        if self.fn:
            return self.fn(path)
        if self.tree:
            with open(os.path.join(self.tree, path), encoding='utf-8') as f:
                return f.read()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (self.commit, path)], capture_output=True)
        if r.returncode:
            raise SystemExit('cannot read %s at %s' % (path, self.commit))
        return r.stdout.decode('utf-8')

    def files(self):
        """papers/*.md and book/*.md of the commit or tree under test (not of the working checkout)."""
        if self._files is not None:
            return list(self._files)
        out = []
        if self.tree:
            for d in ('papers', 'book'):
                p = os.path.join(self.tree, d)
                if os.path.isdir(p):
                    out += ['%s/%s' % (d, n) for n in sorted(os.listdir(p)) if n.endswith('.md')]
            return out
        r = subprocess.run(['git', '-C', ROOT, 'ls-tree', '--name-only', self.commit, 'papers/', 'book/'],
                           capture_output=True, text=True)
        return [x for x in r.stdout.split() if x.endswith('.md') and x.count('/') == 1]


def variant(e, text):
    cands = [('old', e['old'], e['new'])]
    if 'old_step2' in e:
        cands.append(('old_step2', e['old_step2'], e['new_step2']))
    counts = []
    for label, o, n in cands:
        c = text.count(o)
        counts.append('%s=%d' % (label, c))
        if c == 1:
            return o, n, label
    return None, None, ','.join(counts)


def sentences(t):
    return re.split(r'(?<=[.;:?])\s+', t)


def check(data, src, simulate, quiet=False):
    say = (lambda *a: None) if quiet else print
    texts, fails, used = {}, [], {}
    for e in data['edits']:
        if e['file'] not in texts:
            texts[e['file']] = src.read(e['file'])
    for e in data['edits']:
        o, n, label = variant(e, texts[e['file']])
        if o is None:
            fails.append('%s %s (%s part %d): old string not unique (%s)' % (e['id'], e['file'], e['site'], e['part'], label))
        else:
            used[label] = used.get(label, 0) + 1
    say('uniqueness: %d edits, %d fail; variants used %s' % (len(data['edits']), len(fails), used))
    for x in fails:
        say('  FAIL ' + x)
    if not simulate or fails:
        return not fails
    sim = dict(texts)
    for e in data['edits']:
        o, n, _ = variant(e, sim[e['file']])
        if o is None:
            fails.append('%s: old string lost during in-memory application' % e['id'])
            continue
        sim[e['file']] = sim[e['file']].replace(o, n, 1)
    # residual pointer scan over the whole corpus under test
    res = []
    for path in sorted(set(src.files()) | set(sim)):
        t = sim[path] if path in sim else src.read(path)
        for i, line in enumerate(t.split('\n'), 1):
            m = PTR.search(line)
            if m:
                why = [w for f_, s_, w in RESIDUAL_ALLOW if f_ == path and s_ in line
                       and not PTR.search(line.replace('(A1)', '').replace('For a finite total system', ''))]
                res.append((path, i, why[0] if why else None, m.group(0)))
    bad = [r for r in res if r[2] is None]
    say('simulation: residual pointer lines %d (%d allowed as listed, %d unqualified)' % (len(res), len(res) - len(bad), len(bad)))
    for p, i, w, m in res:
        say('  %s %s:%d [%s]%s' % ('allow' if w else 'RESIDUAL', p, i, m, (' ' + w) if w else ''))
    if bad:
        fails.append('residual pointer lines remain')
    # criterion-5 and paraphrase hits on changed lines must be scoped in their sentence
    unq = []
    for path, t in sim.items():
        before = set(texts[path].split('\n'))
        for i, line in enumerate(t.split('\n'), 1):
            if line in before:
                continue
            for s in re.split(r'(?<=[.?])\s+', line):
                if any(f_ == path and a_ in s for f_, a_, _ in CRIT5_ALLOW):
                    continue
                for m in list(CRIT5.finditer(s)) + list(ASSERTS_FINITE.finditer(s)):
                    weak_ok = WEAK.search(s) and not ASSERTS_FINITE.search(s) and not STRONG_ONLY.search(m.group(0))
                    if not (SCOPED.search(s) or weak_ok):
                        unq.append('%s:%d [%s] %s' % (path, i, m.group(0), s[:110]))
    say('simulation: criterion-5/paraphrase hits on changed lines without a scope in their sentence: %d' % len(unq))
    for x in unq:
        say('  UNSCOPED ' + x)
    if unq:
        fails.append('unscoped criterion-5 hits')
    # identifiers and counts in the simulated corpus
    idf = identifier_sim(sim)
    say('simulation: identifier and count findings: %d' % len(idf))
    for x in idf:
        say('  ID ' + x)
    if idf:
        fails.append('identifier/count findings')
    return not fails


def identifier_sim(sim):
    out = []
    m = sim.get('papers/Main.md')
    if m is not None:
        led = [l for l in m.split('\n') if l.startswith('**The posit ledger.**')]
        if len(led) != 1:
            out.append('Main posit ledger paragraph not found exactly once')
        else:
            L = led[0]
            for r in ROMAN:
                if not re.search(r'\(%s\) ' % r, L):
                    out.append('Main posit ledger lacks item (%s)' % r)
            m3 = re.search(r'\(iii\) (.*?)\(iv\) ', L)
            if not m3 or '(REV)' not in m3.group(1):
                out.append('Main posit ledger item (iii) lacks (REV)')
            if re.search(r'\(ii\) ', L):
                out.append('Main posit ledger prints item (ii)')
            if 'Thirteen items, of unequal weight, and not thirteen independent' not in L:
                out.append('Main posit ledger count is not "Thirteen items ... thirteen"')
            if re.search(r'\b[Ff]ourteen\b', L):
                out.append('Main posit ledger still says fourteen')
            if re.search(r'\((?:iii|iv)\)[–-]\(xiii\)', L) and '(xiv)' not in L:
                out.append('posit ledger range renumbered to end at (xiii)')
    for path, t in sim.items():
        for pat, msg in ((r'satisfying six properties', 'reconstruction properties still "six"'),
                         (r'six structural assumptions', '"six structural assumptions" survives'),
                         (r'sixth of the framework\'s structural assumptions', '"sixth of the ... assumptions" survives'),
                         (r'are six structural properties of the substratum', 'ch09 "six structural properties" survives'),
                         (r'Six structural axioms must be checked', 'ch09 "Six structural axioms" survives'),
                         (r'\bA1\s*[–-]\s*A6\b', 'A1–A6 range survives')):
            if re.search(pat, t):
                out.append('%s: %s' % (path, msg))
    ch = sim.get('book/ch02-substratum.md')
    if ch is not None and 'satisfying five properties' not in ch:
        out.append('ch02: reconstruction properties count is not "five"')
    return out


def inf_key(g):
    """Normalize a matched infinity assertion for the content-based comparison."""
    k = re.sub(r'[\s*_]+', ' ', g.lower()).strip()
    if re.search(r'finiteness\b.*\bfails', k):
        return 'finiteness fails'
    return k


def static_new(data):
    inf, reg, caps, ids = [], [], [], []
    for e in data['edits']:
        pairs = [(e['old'], e['new'])]
        if 'new_step2' in e:
            pairs.append((e['old_step2'], e['new_step2']))
        for old, new in pairs:
            def assertions(text):
                out = []
                for sent in sentences(text):
                    spans = [m.span() for m in NEUTRAL.finditer(sent)]
                    out += [(m.group(0), sent) for m in INF.finditer(sent)
                            if not any(a <= m.start() and m.end() <= b for a, b in spans)]
                return out
            # Content-based: the multiset of normalized assertions in new must not exceed that of old. The rewrite
            # rule maps a statement about A1 to one about finiteness, so old is read with A1 as finiteness.
            a_new = assertions(new)
            a_old = assertions(re.sub(r'\bA1\b(?: \(finiteness\))?', 'finiteness', old))
            extra = Counter(inf_key(g) for g, _ in a_new) - Counter(inf_key(g) for g, _ in a_old)
            for g, sent in a_new:
                k = inf_key(g)
                if extra.get(k, 0) > 0:
                    extra[k] -= 1
                    inf.append((e['id'], g, sent[:120]))
            for tok in set(x.lower() for x in REG.findall(new)) - set(x.lower() for x in REG.findall(old)):
                reg.append((e['id'], tok))
            for tok in set(CAPS.findall(new)) - set(CAPS.findall(old)) - CAPS_OK:
                caps.append((e['id'], tok))
            if re.search(r'\bA1\b', new):
                ids.append((e['id'], 'A1 printed in a replacement'))
            if re.search(r'\bA1\s*[–-]\s*A[2-6]\b', new):
                ids.append((e['id'], 'range starting at A1'))
            if re.search(r'\(ii\)|\bitem ii\b|\bposit ii\b|\bitems? \(?ii\)?\s', new):
                ids.append((e['id'], 'retired ledger identifier (ii) printed'))
            if re.search(r'\bposit\s+[0-9]+\b|\bitem\s+[0-9]+\b|\bA\s?[0-9]\s*[–-]\s*A\s?5\b(?!\s*as stated)', new) and not re.search(r'A2[–-]A5', old):
                ids.append((e['id'], 'numeric posit or renumbered range'))
            if re.search(r'\b[Ff]ourteen\b', new):
                ids.append((e['id'], '"fourteen" printed'))
            if re.search(r'[–-]\(xiii\)', new) and '(xiv)' in old:
                ids.append((e['id'], 'range renumbered to (xiii)'))
            for a in ('A2', 'A3', 'A4', 'A5', 'A6'):
                if old.count(a) and not new.count(a) and new.strip():
                    ids.append((e['id'], '%s dropped from a non-empty replacement' % a))
    return inf, reg, caps, ids


# Content a replacement must keep (it carries a scope, a qualification or relocated text); checked in every
# variant of the replacement, so a redraft at reconciliation cannot drop it.
RET_FORM = 'concerns a time that need not be accessible and then has no finite-window test'
RET_TAIL = 'no law that is not supported on periodic configurations is known to satisfy it'
PRESERVE = {
    'D022': ['finite substratum', 'A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2'],
    'D120': ['finite substratum', 'A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2'],
    'D121': ['finite substratum', 'A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2'],
    'D229': ['each assumed as a hypothesis of that result and not adopted', RET_FORM, RET_TAIL,
             'conditions on a law on the whole carrier; finite-window data can test some of their consequences but cannot establish them',
             "do not distinguish them from a finite carrier's counting law", 'reversibility (REV)'],
    'D254': ['assumed as a hypothesis and not adopted', RET_FORM, RET_TAIL],
    'D245': ['assumed in its place and not adopted', RET_FORM, RET_TAIL],
    'D253': ['carry that finite scope where they are stated'],
}


def preservation(data):
    out = []
    ids = {e['id']: e for e in data['edits']}
    for i, subs in PRESERVE.items():
        e = ids.get(i)
        if e is None:
            out.append('%s: edit missing' % i)
            continue
        for v in [e['new']] + ([e['new_step2']] if 'new_step2' in e else []):
            for sub in subs:
                if sub not in v:
                    out.append('%s: replacement lacks %r' % (i, sub[:60]))
    return out


def mirror_parity(data):
    out = []
    prim = {(e['site'], e['part']): e for e in data['edits'] if e['mirror_of'] is None}
    mirrored = set()
    for e in data['edits']:
        if e['mirror_of'] is None:
            continue
        p = prim.get((e['mirror_of'], e['part']))
        if p is None:
            out.append('%s: mirror without a chapter edit' % e['id'])
            continue
        for k in ('old', 'new', 'old_step2', 'new_step2'):
            if p.get(k) != e.get(k):
                out.append('%s: %s differs from chapter edit %s' % (e['id'], k, p['id']))
        if e['file'] != FULL:
            out.append('%s: mirror is not in FULL' % e['id'])
        mirrored.add((e['mirror_of'], e['part']))
    for (site, part), p in prim.items():
        f = site.rsplit(':', 1)[0]
        if f.startswith('book/') and f not in (FULL, 'book/README.md') and (site, part) not in mirrored:
            out.append('%s: chapter edit at %s has no FULL mirror' % (p['id'], site))
    return out


def sitemap_check(data, read_pin=None):
    sm = json.load(open(SITEMAP, encoding='utf-8'))
    pin = sm['pin']
    ptr = {(x['file'], x['line']) for x in sm['sites'] if x['code'] == 'ptr'}
    cache = {}

    def rd(p):
        if p not in cache:
            if read_pin:
                cache[p] = read_pin(p)
            else:
                r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (pin, p)], capture_output=True)
                cache[p] = r.stdout.decode('utf-8') if r.returncode == 0 else None
        return cache[p]
    have, bad = set(), []
    for e in data['edits']:
        if e['kind'] != 'ptr':
            continue
        t = rd(e['file'])
        if t is None or t.count(e['old']) != 1:
            bad.append('%s: old not unique in %s at the ledger pin' % (e['id'], e['file']))
            continue
        ln = t[:t.index(e['old'])].count('\n') + 1
        if e['mirror_of'] is None:
            f, l = e['site'].rsplit(':', 1)
            if (f, int(l)) not in ptr:
                bad.append('%s: declared site %s is not a ptr site of the map' % (e['id'], e['site']))
            if e['part'] == 1 and ln != int(l):
                bad.append('%s: old string is on line %d, not on its declared site line %s' % (e['id'], ln, l))
            have.add((f, int(l)))
        elif e['part'] == 1:
            if (e['file'], ln) not in ptr:
                bad.append('%s: mirror line %s:%d is not a ptr site of the map' % (e['id'], e['file'], ln))
            have.add((e['file'], ln))
    missing = sorted(ptr - have)
    for f, l in missing:
        bad.append('ptr site %s:%d has no edit' % (f, l))
    return len(ptr), len(have & ptr), bad


def static(data, quiet=False, read_pin=None):
    say = (lambda *a: None) if quiet else print
    inf, reg, caps, ids = static_new(data)
    say('infinity-assertion scan (new and new_step2): %d hits' % len(inf))
    for x in inf:
        say('  HIT %s %r in: %s' % x)
    say('register scan (added text, §A.32/§A.33, history phrases): %d hits; new capitals (3+ letters): %d' % (len(reg), len(caps)))
    for x in reg:
        say('  REG %s %r' % x)
    for x in caps:
        say('  CAPS %s %r' % x)
    say('identifier rule (new and new_step2): %d findings' % len(ids))
    for x in ids:
        say('  ID %s %s' % x)
    pres = preservation(data)
    say('preservation check (required content in every replacement variant): %d findings' % len(pres))
    for x in pres:
        say('  KEEP ' + x)
    mir = mirror_parity(data)
    say('mirror parity (every chapter edit byte-identical to its FULL mirror): %d findings' % len(mir))
    for x in mir:
        say('  MIRROR ' + x)
    n, ok_n, bad = sitemap_check(data, read_pin)
    say('sitemap cross-check: %d ptr sites in the map, %d with an edit; %d findings' % (n, ok_n, len(bad)))
    for x in bad:
        say('  MAP ' + x)
    return not inf and not reg and not caps and not ids and not bad and n == ok_n and not pres and not mir


def self_test():
    ok = True

    def expect(cond, msg):
        nonlocal ok
        print('  %s %s' % ('ok ' if cond else 'BAD', msg))
        ok = ok and cond

    E = lambda i, old, new, **k: dict(dict(id=i, kind='consistency', file='x', site='x:1', part=1, row='X-01', mirror_of=None, old=old, new=new), **k)
    rd = lambda t: Source(fn=lambda p: t, files=['x'])
    # uniqueness
    d1 = {'edits': [E('T1', 'abc', 'abd'), E('T2', 'zz', '', old_step2='qq', new_step2='')]}
    expect(check(d1, rd('abc qq'), False, True), 'unique old strings pass')
    expect(not check(d1, rd('abc abc qq'), False, True), 'a duplicated old string fails')
    expect(not check(d1, rd('abc'), False, True), 'a missing old string fails')
    # infinity scan, each injected form
    for s in ['the substratum is infinite', 'S is not finite', 'with $|S| = \\infty$', 'with |S| = ∞',
              'in the thermodynamic limit', 'a lattice of unbounded size', 'infinitely many configurations',
              'the framework assumes neither that the substratum is finite nor that it is small, and the substratum is infinite']:
        inf = static_new({'edits': [E('I', 'a set (finite under A1)', s)]})[0]
        expect(bool(inf), 'infinity scan catches: %s' % s[:60])
    neutral = 'the framework assumes neither that the substratum is finite nor that it is infinite'
    expect(not static_new({'edits': [E('N', 'x', neutral)]})[0], 'the symmetric neither/nor disclaimer is exempt')
    expect(not static_new({'edits': [E('N2', 'x', 'appearing infinite-dimensional in the continuum limit')]})[0], '"infinite-dimensional" is not an assertion')
    # plumbing: new_step2 is scanned too
    st = static_new({'edits': [E('P', 'a', 'b', old_step2='c', new_step2='the substratum is infinite')]})[0]
    expect(bool(st), 'static scan reads new_step2')
    # register scan
    for s in ['the claim is now settled', 'the posit is no longer used', 'the earlier revision stated', 'A1 was removed', 'it does NOT hold']:
        _, reg, caps, _ = static_new({'edits': [E('R', 'x', s)]})
        expect(bool(reg or caps), 'register scan catches: %s' % s)
    # identifier rule in replacement strings
    for old, new in [('Fourteen items', 'Fourteen items'), ('(iii)–(xiv)', '(iii)–(xiii)'), ('item (ii)', 'posit 2'),
                     ('A1–A6', 'A1–A6 jointly'), ('(ii) total', '(ii) total finiteness'), ('A2–A6', 'A1–A5')]:
        ids = static_new({'edits': [E('D', old, new)]})[3]
        expect(bool(ids), 'identifier rule catches %r -> %r' % (old, new))
    # simulated identifier/count checks
    good = ('**The posit ledger.** (i) a; (iii) (REV) x; ' + ' '.join('(%s) x;' % r for r in ROMAN[2:]) +
            ' Thirteen items, of unequal weight, and not thirteen independent physical assumptions:')
    expect(not identifier_sim({'papers/Main.md': good}), 'a well-formed thirteen-item ledger passes')
    expect(bool(identifier_sim({'papers/Main.md': good.replace('(xiv) x;', '')})), 'a missing item (xiv) is caught')
    expect(bool(identifier_sim({'papers/Main.md': good.replace('(iii) (REV) x;', '(ii) x; (iii) (REV) x;')})), 'a surviving item (ii) is caught')
    expect(bool(identifier_sim({'papers/Main.md': good.replace('Thirteen items', 'Fourteen items')})), '"Fourteen" is caught')
    expect(bool(identifier_sim({'book/ch02-substratum.md': 'satisfying six properties:'})), 'a six/five count is caught')
    # residual scan catches a paraphrased pointer and reads the files of the source under test
    d2 = {'edits': [E('S', 'a set (finite under A1)', 'a set')]}
    corpus = {'x': 'a set (finite under A1). ', 'y': 'Total configuration finiteness remains an open physical hypothesis.'}
    src = Source(fn=lambda p: corpus[p], files=['x', 'y'])
    expect(not check(d2, src, True, True), 'residual scan catches a paraphrased pointer in another file of the source')
    corpus['y'] = 'Nothing here.'
    expect(check(d2, src, True, True), 'residual scan passes once the paraphrase is gone')
    d3 = {'edits': [E('U', 'a set (finite under A1).', 'the universe is a finite universe.')]}
    expect(not check(d3, Source(fn=lambda p: 'a set (finite under A1).', files=['x']), True, True), 'an unscoped criterion-5 hit on a changed line is caught')
    # sitemap cross-check: a ptr edit at an unmapped site is caught
    sm = json.load(open(SITEMAP, encoding='utf-8'))
    s0 = [x for x in sm['sites'] if x['code'] == 'ptr'][0]
    fake = {'edits': [dict(id='M1', kind='ptr', file='papers/Fake.md', site='papers/Fake.md:3', part=1, mirror_of=None, old='zzz', new='')]}
    n, k, bad = sitemap_check(fake, read_pin=lambda p: 'a\nb\nzzz\n')
    expect(bool(bad) and k == 0, 'sitemap cross-check reports an unmapped site and the %d missing ptr sites' % n)
    # round-2 countercontrols
    for s_ in ['a substratum with no finite bound', 'a lattice of infinite extent', 'a chain extending without end',
               'a non-finite carrier', 'an infinitely extended lattice', 'Finiteness of the substratum fails']:
        expect(bool(static_new({'edits': [E('I2', 'a set (finite under A1)', s_)]})[0]), 'infinity scan catches: %s' % s_)
    expect(not static_new({'edits': [E('I3', 'A1 (finiteness) fails for BFSS', 'finiteness fails for BFSS')]})[0],
           'a per-program "finiteness fails" kept from the old string is not an introduced assertion')
    for s_ in ['Earlier versions stated the posit', 'it was originally a posit']:
        expect(bool(static_new({'edits': [E('R2', 'x', s_)]})[1]), 'register scan catches: %s' % s_)
    expect(bool(static_new({'edits': [E('D2', 'item (ii)', 'item ii')]})[3]), 'identifier rule catches "item ii"')
    for s_ in ['Whether this matters is left aside; the universe is finite.', 'The question is open, and the substratum is finite.',
               'Is the universe a finite universe? The universe is finite.']:
        d4 = {'edits': [E('W', 'a set (finite under A1).', s_)]}
        expect(not check(d4, Source(fn=lambda p: 'a set (finite under A1).', files=['x']), True, True),
               'a weak marker does not exempt a finiteness assertion: %s' % s_[:50])
    d5 = {'edits': [E('W2', 'a set (finite under A1).', 'whether the framework assumes a finite universe.')]}
    expect(check(d5, Source(fn=lambda p: 'a set (finite under A1).', files=['x']), True, True), 'an interrogative mention still passes')
    good_p = {'edits': [E('D022', 'o', 'a finite substratum, with A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2 [SM §4.1]')]}
    expect(not [x for x in preservation(good_p) if x.startswith('D022')], 'preservation passes when the wrapping clause is present')
    bad_p = {'edits': [E('D022', 'o', 'a finite substratum'), E('D229', 'o', 'x', old_step2='o2', new_step2='x')]}
    pres = preservation(bad_p)
    expect(any(x.startswith('D022') for x in pres) and any(x.startswith('D229') for x in pres) and any('D245: edit missing' == x for x in pres),
           'preservation catches a dropped clause, a dropped qualification and a missing edit')
    mp = {'edits': [dict(id='C1', kind='ptr', file='book/ch09-x.md', site='book/ch09-x.md:3', part=1, mirror_of=None, old='a', new='b'),
                    dict(id='C2', kind='ptr', file=FULL, site='book/ch09-x.md:3', part=1, mirror_of='book/ch09-x.md:3', old='a', new='c')]}
    expect(bool(mirror_parity(mp)), 'mirror parity catches a FULL mirror that differs from its chapter edit')
    mp['edits'] = mp['edits'][:1]
    expect(bool(mirror_parity(mp)), 'mirror parity catches a chapter edit without a FULL mirror')
    mp['edits'].append(dict(id='C3', kind='ptr', file=FULL, site='book/ch09-x.md:3', part=1, mirror_of='book/ch09-x.md:3', old='a', new='b'))
    expect(not mirror_parity(mp), 'mirror parity passes for identical strings')
    bad_led = good.replace('(iii) (REV) x;', '(iii) y;')
    expect(bool(identifier_sim({'papers/Main.md': bad_led})), 'a posit ledger item (iii) without (REV) is caught')
    # round-3 countercontrols
    d065 = 'The substratum is infinite for continuum BFSS'
    expect(bool(static_new({'edits': [E('D065x', '**Status.** A1 fails for continuum BFSS', d065)]})[0]),
           'content-based infinity scan flags a swapped assertion of equal count (D065 rewritten to "%s")' % d065)
    for o_, n_ in [('**Status.** A1 fails for continuum BFSS', '**Status.** Finiteness fails for continuum BFSS'),
                   ('Per-condition: A1 (finiteness) **fails** in the full theory', 'Per-condition: finiteness **fails** in the full theory'),
                   ('A1 fails in the limit,', 'finiteness fails in the limit,')]:
        expect(not static_new({'edits': [E('F', o_, n_)]})[0], 'kept per-program "finiteness fails" passes: %s' % n_[:40])
    expect(not static_new({'edits': [E('F2', 'x', 'finiteness fails to determine the bound')]})[0], '"fails to" is not an infinity assertion')
    for s_ in ['Whether it matters is left aside; $S$ is finite.', 'The finite configuration space is an open matter.']:
        d6 = {'edits': [E('W3', 'a set (finite under A1).', s_)]}
        expect(not check(d6, Source(fn=lambda p: 'a set (finite under A1).', files=['x']), True, True),
               'a weak marker does not exempt: %s' % s_)
    # round-4 countercontrol: a bare "on a finite" does not scope a sentence
    s_ = 'a deterministic bijection on a finite configuration space, an open matter for physics.'
    d7 = {'edits': [E('W4', 'a set (finite under A1).', s_)]}
    expect(not check(d7, Source(fn=lambda p: 'a set (finite under A1).', files=['x']), True, True),
           'a bare "on a finite" is not a scope: %s' % s_)
    print('self-test %s' % ('PASS' if ok else 'FAIL'))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commit')
    ap.add_argument('--tree')
    ap.add_argument('--simulate', action='store_true')
    ap.add_argument('--static', action='store_true')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test() else 1)
    data = load()
    ok = True
    if a.static:
        ok = static(data) and ok
    if a.commit or a.tree:
        ok = check(data, Source(commit=a.commit, tree=a.tree), a.simulate) and ok
    print('RESULT ' + ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()

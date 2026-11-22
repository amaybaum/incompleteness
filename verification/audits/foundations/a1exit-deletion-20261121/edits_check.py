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
import argparse, ast, json, os, re, subprocess, sys, warnings
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
    ('papers/SM.md', '(ii) On a finite configuration space, and in each Fourier fibre',
     'SM:252, Lemma 1c(ii) states its own finite scope (ledger X-18); unchanged sentence on a line D389 changes (PREREG §31)'),
]
# Infinity assertions that no replacement string may introduce (owner decision: cardinality neutrality).
INF = re.compile(r'(?:\b(?:is|are|be|being|been)\s+infinite\b(?!-))|\b(?:is|are)\s+not\s+finite\b|\binfinitely many\b'
                 r'|\bcountably infinite\b|\buncountably infinite\b'
                 r'|\binfinite (?:substratum|universe|configuration space|carrier|set|number|lattice|system)\b'
                 r'|\|S\|\s*=\s*(?:\\infty|∞)|\bS\s+is\s+infinite\b|\binfinite in (?:extent|size|cardinality)\b'
                 r'|\bthermodynamic limit\b|\bunbounded (?:size|number of (?:sites|configurations|states))\b'
                 r'|\bwithout bound in size\b|\bof infinite cardinality\b|\bno finite bound\b|\bof infinite extent\b'
                 r'|\bextending without end\b|\bnon-finite\b|\binfinitely extended\b|\b[Ff]initeness\b[^.;]{0,40}\bfails\b(?! to)'
                 r'|\b(?:every|any|all|arbitrary) infinite (?:system|substrat\w*|carrier|configuration space|lattice|model)s?\b'
                 r'|\b(?:holds?|works?|appl(?:y|ies)|valid) (?:for|to|on) (?:every|any|all|arbitrary) (?:configuration spaces?|carriers?|substrat\w*|cardinalit(?:y|ies))\b'
                 r'|\bregardless of (?:its |the )?cardinality\b|\bwhatever (?:its|the) cardinality\b|\bindependently of (?:its |the )?cardinality\b'
                 r'|\b(?:extends?|extended|appl(?:y|ies)|carr(?:y|ies) over|generali[sz]es?) to infinite (?:substrat\w*|systems?|configuration spaces?|carriers?|lattices?|models?)\b')
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
            fp = os.path.join(self.tree, path)
            if not os.path.exists(fp) and path.startswith('verification/') and getattr(self, 'fallback', None):
                return git_show(self.fallback, path)
            with open(fp, encoding='utf-8') as f:
                return f.read()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (self.commit, path)], capture_output=True)
        if r.returncode:
            raise SystemExit('cannot read %s at %s' % (path, self.commit))
        return r.stdout.decode('utf-8')

    def all_files(self):
        if self.tree:
            out = []
            for dp, _, fs in os.walk(self.tree):
                out += [os.path.relpath(os.path.join(dp, n), self.tree) for n in fs]
            return sorted(out)
        r = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', self.commit], capture_output=True, text=True)
        return [x for x in r.stdout.split() if not x.endswith(('.pdf', '.png', '.jpg', '.olean', '.gz', '.zip'))]

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


def git_show(rev, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True)
    if r.returncode:
        raise SystemExit('cannot read %s at %s' % (path, rev))
    return r.stdout.decode('utf-8')


def lean_strip(text):
    """Lean source with block comments (doc comments included, nesting respected) and line comments removed."""
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        if text.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth and text.startswith('-/', i):
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if text.startswith('--', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
            continue
        out.append(text[i]); i += 1
    return ''.join(out)


def in_comment(text, start, end):
    """True when text[start:end] lies inside one block comment."""
    i, depth, opened = 0, 0, None
    while i < start:
        if text.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth and text.startswith('-/', i):
            depth -= 1; i += 2; continue
        i += 1
    if depth == 0:
        return False
    seg = text[start:end]
    return '-/' not in seg and '/-' not in seg


def lean_docstring_only(original, edited):
    return lean_strip(original) == lean_strip(edited)


def lean_check(data, read):
    out = []
    by_file = {}
    for e in data['edits']:
        if e['kind'] == 'lean-docstring':
            by_file.setdefault(e['file'], []).append(e)
    for f, es in by_file.items():
        orig = read(f)
        cur = orig
        for e in es:
            if cur.count(e['old']) != 1:
                out.append('%s: old string not unique in %s' % (e['id'], f)); continue
            i = cur.index(e['old'])
            if not in_comment(cur, i, i + len(e['old'])):
                out.append('%s: old string is not inside a comment' % e['id'])
            if '-/' in e['new'] or '/-' in e['new']:
                out.append('%s: replacement opens or closes a comment' % e['id'])
            cur = cur.replace(e['old'], e['new'], 1)
        if not lean_docstring_only(orig, cur):
            out.append('%s: the edited file differs from the original outside comments' % f)
    return out


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
    man = {k: v for k, v in sim.items() if not k.startswith('verification/')}  # manuscripts only; the Lean file is checked by --static
    for path in sorted(set(src.files()) | set(man)):
        t = man[path] if path in man else src.read(path)
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
    for path, t in man.items():
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
    sp = sim_preservation(man)
    say('simulation: finite-scope and configuration-space preservation findings: %d' % len(sp))
    for x in sp:
        say('  KEEP ' + x)
    if sp:
        fails.append('simulated preservation findings')
    idf = identifier_sim(man)
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
            for tok in (set(CAPS.findall(new)) - set(CAPS.findall(old)) - CAPS_OK) if e.get('kind') in ('ptr', 'consistency', 'handoff') else ():
                caps.append((e['id'], tok))
            if e.get('kind') == 'lean-docstring':
                continue  # historical Lean identifiers and the scoped quotation keep A1 by design (owner ruling on H-11)
            if re.search(r'\bA1\b', IDENT.sub('', new) if e.get('kind') in ('repo-active', 'guard-pin') else new):
                ids.append((e['id'], 'A1 printed in a replacement'))
            if re.search(r'\bA1\s*[–-]\s*A[2-6]\b', new):
                ids.append((e['id'], 'range starting at A1'))
            if re.search(r'\(ii\)|\bitem ii\b|\bposit ii\b|\bitems? \(?ii\)?\s', new):
                ids.append((e['id'], 'retired ledger identifier (ii) printed'))
            if re.search(r'\bposit\s+[0-9]+\b|\bitem\s+[0-9]+\b|\bA\s?[0-9]\s*[–-]\s*A\s?5\b(?!\s*as stated)', new) and not re.search(r'A2[–-]A5', old) \
                    and 'finiteness predicate `A1` and A2' not in new:
                ids.append((e['id'], 'numeric posit or renumbered range'))
            if re.search(r'\b[Ff]ourteen\b', new):
                ids.append((e['id'], '"fourteen" printed'))
            if re.search(r'[–-]\(xiii\)', new) and '(xiv)' in old:
                ids.append((e['id'], 'range renumbered to (xiii)'))
            for a in ('A2', 'A3', 'A4', 'A5', 'A6'):
                if e.get('kind') not in ('ptr', 'consistency', 'handoff'):
                    break
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


CS_SENTENCE = ('**Configuration space.** The substratum has a configuration space $S$. No restriction is imposed on its '
               'cardinality; $S$ may be finite or infinite.')
PRESERVE.update({'D259': [CS_SENTENCE], 'D261': [CS_SENTENCE], 'D310': [CS_SENTENCE], 'D114': [CS_SENTENCE, 'the results stated for a finite substratum take it finite'],
                 'D260': ['on a finite representative, the counting measure is selected'],
                 'D312': ['on a finite representative, the counting measure is selected'],
                 'D309': ['of a finite representative (Lemma 2) it is the uniform probability']})
# Amendment §28: the finite scope of Theorem 24(i)/(iii) and the narrowed membership of (iii) must survive any redraft.
PRESERVE.update({'D361': ['For finite $\\mathcal{C}_H$ and any bijection'],
                 'D362': ['bimeasurable bijection $\\psi$ of $A$', 'the uniform hidden prior on a finite $\\mathcal{C}_H$'],
                 'D363': ['bijection $\\psi$ of $A$', 'has bijective dynamics (A2)'],
                 'D364': ['channel-preserving extensions, not members of'],
                 'D367': ['exactly decoupled added factors of any cardinality in a normalized state or law',
                          'an unnormalizable or coupled factor is outside it'],
                 'D368': ['permutation product dynamics', 'as a channel-preserving extension'],
                 'D370': ['a channel-preserving extension rather than a member of the group'],
                 'D371': ['a channel-preserving extension rather than a member of the group'],
                 'D372': ['a bimeasurable bijection as its dynamics', 'as a channel-preserving extension'],
                 'D373': ['a bimeasurable bijection as its dynamics', 'as a channel-preserving extension']})
# Amendment §31: the corrections of the final scientific review (#1477 c.7074137435) must survive any redraft.
FIN_CH = 'of a finite $\\mathcal{C}_H$'
PRESERVE.update({'D026': ['no established form for a substratum of unspecified cardinality',
                          'Corollary (near-return) of [Main §2.3], of which an exact return is a case',
                          'assumed and not adopted, is a weaker sufficient condition for that conclusion',
                          'what is open for a substratum of unspecified cardinality is a source of the return hypothesis',
                          'which [GR §2.3] states for a total system that is finite', 'E3 does not establish finiteness of $S$',
                          'Theorem 23 retains its stated finite-substratum hypothesis',
                          'a meromorphic continuation of the memory-resummed Schur complement that is not established',
                          'These do not by themselves extend the complete reconstruction theorem'],
                 'D231': ['every representative, or channel-preserving extension,'],
                 'D363': ['a density matrix $\\sigma_A$ on $\\ell^2(A)$ with $\\operatorname{Tr}\\sigma_A=1$'],
                 'D364': ['for any density matrix $\\sigma_A$ with $\\operatorname{Tr}\\sigma_A=1$ on a Hilbert space',
                          'for a classical factor with $\\alpha(A)=1$'],
                 'D369': ['uniform hidden-coordinate relabelling ' + FIN_CH],
                 'D374': ['for $S$ of unspecified cardinality bijectivity is the reversibility posit (REV)',
                          'thus, for a finite $S$, partly structural'],
                 'D387': ['of a finite set of hidden configurations'], 'D388': ['of a finite set of hidden states'],
                 'D389': ['Lemma 3 on a finite representative'], 'D390': ['counting measure on a finite representative'],
                 'D391': ['the counting measure on a finite $\\mathcal{C}_H$']})
PRESERVE.update({'D276': ['for a finite torus and a finite alphabet'], 'D332': ['for a finite torus and a finite alphabet'],
                 'D326': ['`A1` for a finite alphabet'],
                 'D392': ['FINITELY MANY SITES, A FINITE ALPHABET'],
                 'D393': ['with finitely many sites and a finite alphabet'], 'D394': ['with finitely many sites and a finite alphabet'],
                 'D395': ['with finitely many sites and a finite alphabet'], 'D396': ['with finitely many sites and a finite alphabet'],
                 'D397': ['with finitely many sites and a finite alphabet'], 'D398': ['with finitely many sites and a finite alphabet'],
                 'D399': ["the manuscripts' finite representatives", '(`SM.md` §4.1, §4.4), are finite objects'],
                 'D319': ['**The finiteness predicate `A1` is\nnot weakened**']})
PRESERVE.update({i: [FIN_CH] for i in ('D375', 'D376', 'D377', 'D378', 'D379', 'D380', 'D381', 'D382', 'D383', 'D384',
                                      'D385', 'D386')})
# Text that must be present in the simulated manuscript: the approved sentence, and the finite scope of every
# finite-only result stated near it (owner decision #1169 c.7058446475).
SIM_PRESERVE = {
    'papers/Main.md': [CS_SENTENCE, 'makes the visible configuration space $\\mathcal{C}_V$ finite',
                       'On each finite cycle of the reversible representative',
                       'globally, on a finite representative, the counting measure is selected',
                       'defined here for a finite system only', 'no construction is given for an infinite $S$',
                       'The finite representative is used by the recurrence step of §2.3',
                       'by the counting measure of Lemma 3', 'On a finite set, injectivity implies surjectivity'],
    'papers/Substratum.md': [CS_SENTENCE, '*finite capacity* when $S$ is finite', 'of finite capacity when $S$ is finite'],
    'book/ch01-observation.md': [CS_SENTENCE, 'makes $\\mathcal{C}_V$ finite', 'On each finite cycle of the reversible representative',
                                 'On a finite representative, or under A2 (Chapter 2 §2.4), $\\varphi$ is a bijection on $S$.',
                                 'globally, on a finite representative, the counting measure is selected',
                                 'On a finite set, injectivity implies surjectivity'],
    'book/ch02-substratum.md': [CS_SENTENCE, 'the results stated for a finite substratum take it finite'],
    'book/The-Incompleteness-of-Observation-FULL.md': [CS_SENTENCE, 'globally, on a finite representative, the counting measure is selected',
                                                        'On a finite representative, or under A2 (Chapter 2 §2.4), $\\varphi$ is a bijection on $S$.',
                                                        'the results stated for a finite substratum take it finite'],
}
# Amendment §31 (§31.7 item 6): the corrected sentences, and #1494's book statement of Theorem 24(i) (F5).
THM24_BOOK = 'For a finite set of hidden configurations $\\mathcal{C}_H$ with the uniform hidden prior and any bijection'
for _f, _subs in {
        'papers/Substratum.md': ['no established form for a substratum of unspecified cardinality',
                                 'of which an exact return is a case',
                                 'what is open for a substratum of unspecified cardinality is a source of the return hypothesis',
                                 'a meromorphic continuation of the memory-resummed Schur complement that is not established',
                                 'These do not by themselves extend the complete reconstruction theorem',
                                 'for any density matrix $\\sigma_A$ with $\\operatorname{Tr}\\sigma_A=1$ on a Hilbert space',
                                 'for a classical factor with $\\alpha(A)=1$', 'a density matrix $\\sigma_A$ on $\\ell^2(A)$',
                                 'for $S$ of unspecified cardinality bijectivity is the reversibility posit (REV)',
                                 'thus, for a finite $S$, partly structural'],
        'papers/Structure.md': ['uniform hidden-coordinate relabelling ' + FIN_CH],
        'papers/SM.md': ['Lemma 3 on a finite representative', 'counting measure on a finite representative',
                         'the counting measure on a finite $\\mathcal{C}_H$'],
        'papers/Main.md': ['every representative, or channel-preserving extension,'],
        'papers/Complexity.md': ['uniform relabelling of a finite set of hidden configurations'],
        'papers/Methodology.md': ['a permutation of a finite set of hidden states'],
        'book/ch02-substratum.md': [THM24_BOOK, 'uniform hidden-coordinate relabelling ' + FIN_CH + ' and',
                                    'uniform hidden-coordinate relabelling ' + FIN_CH + ', with the uniform hidden prior'],
        'book/ch03-structural-realism.md': ['A single hidden permutation ' + FIN_CH,
                                            'A uniform hidden-coordinate relabelling ' + FIN_CH + ' preserves',
                                            'A uniform hidden-coordinate relabelling ' + FIN_CH + ', or'],
        'book/ch04-methodology.md': ['Uniform hidden relabelling ' + FIN_CH],
        FULL: [THM24_BOOK, 'uniform hidden-coordinate relabelling ' + FIN_CH + ' and',
               'uniform hidden-coordinate relabelling ' + FIN_CH + ', with the uniform hidden prior',
               'A single hidden permutation ' + FIN_CH, 'A uniform hidden-coordinate relabelling ' + FIN_CH + ' preserves',
               'A uniform hidden-coordinate relabelling ' + FIN_CH + ', or', 'Uniform hidden relabelling ' + FIN_CH]}.items():
    SIM_PRESERVE.setdefault(_f, []).extend(_subs)
CS_COUNT = {'papers/Main.md': 1, 'papers/Substratum.md': 1, 'book/ch01-observation.md': 1, 'book/ch02-substratum.md': 1,
            'book/The-Incompleteness-of-Observation-FULL.md': 2}


def sim_preservation(man):
    out = []
    for f, subs in SIM_PRESERVE.items():
        if f not in man:
            continue
        for sub in subs:
            if sub not in man[f]:
                out.append('%s lacks %r after the edits' % (f, sub[:70]))
    for f, k in CS_COUNT.items():
        if f in man and man[f].count(CS_SENTENCE) != k:
            out.append('%s carries the configuration-space sentence %d times, not %d' % (f, man[f].count(CS_SENTENCE), k))
    return out


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


def line_map(a_text, b_text):
    """Map line numbers of b to line numbers of a (difflib alignment; replaced blocks by best match)."""
    import difflib
    a, b = a_text.split('\n'), b_text.split('\n')
    m = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal':
            for k in range(j2 - j1):
                m[j1 + k + 1] = i1 + k + 1
        elif tag == 'replace':
            for j in range(j1, j2):
                best, br = None, 0.0
                for i in range(i1, i2):
                    r = difflib.SequenceMatcher(None, a[i], b[j], autojunk=False).quick_ratio()
                    if r > br:
                        best, br = i + 1, r
                m[j + 1] = best
    return m


def sitemap_check(data, read_pin=None, read_base=None):
    """Every ptr site of the ledger map has an edit and every ptr edit sits at a mapped ptr site: the old string is
    located at the drafting base and its line mapped back to the ledger pin."""
    sm = json.load(open(SITEMAP, encoding='utf-8'))
    pin = sm['pin']
    ptr = {(x['file'], x['line']) for x in sm['sites'] if x['code'] == 'ptr'}
    cache, bcache, maps = {}, {}, {}

    def rd(p):
        if p not in cache:
            if read_pin:
                cache[p] = read_pin(p)
            else:
                r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (pin, p)], capture_output=True)
                cache[p] = r.stdout.decode('utf-8') if r.returncode == 0 else None
        return cache[p]

    def rb(p):
        if p not in bcache:
            bcache[p] = read_base(p) if read_base else rd(p)
        return bcache[p]
    have, bad = set(), []
    for e in data['edits']:
        if e['kind'] != 'ptr':
            continue
        t = rb(e['file'])
        if t is None or t.count(e['old']) != 1:
            bad.append('%s: old not unique in %s at the drafting base' % (e['id'], e['file']))
            continue
        bl = t[:t.index(e['old'])].count('\n') + 1
        if read_base:
            if e['file'] not in maps:
                maps[e['file']] = line_map(rd(e['file']), t)
            ln = maps[e['file']].get(bl, -1)
        else:
            ln = bl
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
    lean = lean_check(data, lambda pth: git_show(data.get('drafting_base', 'HEAD'), pth)) if 'drafting_base' in data else []
    say('Lean docstring-only check (edited file equals the original outside comments): %d findings' % len(lean))
    for x in lean:
        say('  LEAN ' + x)
    n, ok_n, bad = sitemap_check(data, read_pin, (lambda pth: git_show(data['drafting_base'], pth)) if 'drafting_base' in data and read_pin is None else None)
    say('sitemap cross-check: %d ptr sites in the map, %d with an edit; %d findings' % (n, ok_n, len(bad)))
    for x in bad:
        say('  MAP ' + x)
    return not inf and not reg and not caps and not ids and not bad and n == ok_n and not pres and not mir and not lean


MIN_PIN = 20
PIN_SKIP = ('verification/audits/', 'verification/infrastructure/', 'verification/receipts/')
# Pin candidates the pins check reports that the probe does not read from the edited file (recorded reasons).
PIN_OK = [
    ('verification/lean/edge_rigidity_probe.py', 'A1–A6 are not `DerivedOI`',
     'the loop at line 3346 reads ROUTE-B-AUDIT.md, a frozen record that keeps the phrase'),
    ('verification/lean/edge_rigidity_probe.py', 'realized-core images of A1 and A2',
     'line 3475 reads verification/audits/manuscript/lean-manuscript-census.md, a record that keeps the phrase'),
]


def py_literals(src):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            tree = ast.parse(src)
    except SyntaxError:
        return []
    return [(n.lineno, ' '.join(n.value.split())) for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) >= MIN_PIN]


def apply_edits(data, read, kinds=None):
    out = {}
    for e in data['edits']:
        if kinds and e['kind'] not in kinds:
            continue
        if e['file'] not in out:
            out[e['file']] = read(e['file'])
        o, n, _ = variant(e, out[e['file']])
        if o is not None:
            out[e['file']] = out[e['file']].replace(o, n, 1)
    return out


def pin_targets_check(data, read):
    """Every literal a guard-pin edit introduces must occur, whitespace-normalized, in the simulated text of each
    file the record names in "targets"."""
    out = []
    after_t = apply_edits(data, read)
    flat = {}
    for e in data['edits']:
        if e['kind'] != 'guard-pin':
            continue
        if e.get('pin_note') in ('message', 'comment'):
            continue  # a check's message or comment, not a pinned literal
        if not e.get('targets'):
            out.append('%s: guard-pin edit without targets' % e['id'])
            continue
        pf = e['file']
        old_lits = {l for _, l in py_literals(read(pf))}
        new_lits = [l for _, l in py_literals(after_t[pf]) if l not in old_lits]
        pieces = [' '.join(x.split()) for x in re.split(r"['\"]", e['new'])]
        pieces = [x for x in pieces if len(x) >= 12 and not x.startswith(('ok', 'in ', '#'))]
        mine = [l for l in new_lits if any(x in l for x in pieces)]
        if not mine:
            out.append('%s: no new literal found in %s' % (e['id'], pf))
        for t in e['targets']:
            if t not in flat:
                flat[t] = ' '.join((after_t[t] if t in after_t else read(t)).split())
            for l in mine:
                if l not in flat[t]:
                    out.append('%s: new pinned literal %r does not occur in the edited %s' % (e['id'], l[:70], t))
    return out


def pins_check(data, rev, quiet=False, read=None, pyfiles=None):
    """String literals of tracked Python checks that pin text the edits remove; each must be updated by a
    guard-pin edit in the same commit or carry a recorded reason (PIN_OK); and every updated pin must occur in its
    target after the edits."""
    say = (lambda *a: None) if quiet else print
    read = read or (lambda pth: git_show(rev, pth))
    before = {f: ' '.join(read(f).split()) for f in {e['file'] for e in data['edits']} if not f.endswith('.py')}
    after_t = apply_edits(data, read)
    after = {f: ' '.join(after_t[f].split()) for f in before}
    if pyfiles is None:
        pyfiles = [x for x in subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', rev], capture_output=True,
                                             text=True).stdout.split() if x.endswith('.py') and not x.startswith(PIN_SKIP)]
    broken = []
    for pf in pyfiles:
        src = read(pf)
        lits = py_literals(src)
        if not lits:
            continue
        new_src = after_t.get(pf, src)
        new_lits = {l for _, l in py_literals(new_src)} if pf in after_t else None
        for ln, lit in lits:
            for f in before:
                if lit in before[f] and lit not in after[f]:
                    if new_lits is not None and lit not in new_lits:
                        continue  # updated by a guard-pin edit
                    if any(pf == a and lit.startswith(b) for a, b, _ in PIN_OK):
                        continue
                    broken.append('%s:%d pins %r in %s' % (pf, ln, lit[:80], f))
    tgt = pin_targets_check(data, read)
    say('pins check: %d unresolved pins (literals of tracked checks that the edits would break); %d updated pins not found in their targets'
        % (len(broken), len(tgt)))
    for x in broken + tgt:
        say('  PIN ' + x)
    return not broken and not tgt


# Repository-wide scan (owner decision #1169 c.7058374016): every tracked active file.
REPO_PAT = re.compile(r'\bA1\b|[Tt]otal[- ]finiteness|[Ff]initeness posit|posit \(ii\)|\bA1\s*[–-]\s*A6\b')
HISTORICAL_PREFIX = ('verification/audits/', 'verification/programmes/', 'verification/infrastructure/',
                     'verification/receipts/', 'verification/seals/', 'verification/certificates/', 'evidence/')
HISTORICAL_FILE = ('verification/ROADMAP.md', 'verification/MIGRATION-MANIFEST.md', 'verification/migration-manifest.json')
# Identifier forms that are not prose about A1: full Lean declaration names, and the predicate written as the
# finiteness predicate (round 5: a bare `A1` in prose is pending unless named the finiteness predicate).
IDENT = re.compile(r'[Ff]initeness predicate `[\w.]*A1`|`[^`\n]*[A-Za-z_.]A1[^`\n]*`|`A1[A-Za-z_][^`\n]*`|\b\w+_A1\w*\b'
                   r'|\bA1Realized\b|\bA1A2Realized\b|\ba1_\w+|\.A1\b|\bdef A1\b|\bA1-RIGID-1\b|\bFINITENESS PREDICATE `A1`')
EXPLAINED = [  # (path or prefix ending in '/', substring or None, class, reason)
    ('.github/workflows/pe01-bounded-tests.yml', None, 'unrelated label', 'amendment A1 of the pe01 plan'),
    # on main from #1484 (df6da1c6), after the ledger base 97070c98 (PREREG §31.2): the programme name A1-EXIT and
    # "A1-retirement" name the retirement itself; neither states A1 as a premise
    ('.github/workflows/a1exit-trial-verify.yml', None, 'unrelated label', 'the programme name A1-EXIT and the A1-retirement trial (#1484)'),
    ('tools/citation_roles_check.py', None, 'unrelated label', 'a phrase list entry "In (A1), "'),
    ('tools/build_migration_manifest.py', 'the A1-A6 audit', 'historical record label', 'names the frozen manuscript-axiom audit record in the grandfather manifest'),
    ('papers/oi_lattice_code/', None, 'unrelated label', 'the A1 irrep (Higgs, O_h, S3) and task labels of the lattice code'),
    ('verification/audit-census.json', None, 'unrelated label', 'finding identifiers A1-* of an audit census'),
    ('verification/lean/link_decomposition_probe.py', None, 'unrelated label', 'the A1 irrep'),
    ('verification/lean/representation_bridge_probe.py', None, 'unrelated label', 'the A1 irrep'),
    ('verification/lean/taste_branching_probe.py', None, 'unrelated label', 'the A1 irrep'),
    ('verification/lean/gauge_certificates_probe.py', None, 'unrelated label', 'the A1 irrep'),
    ('verification/lean/idempotent_trace_probe.py', None, 'unrelated label', 'the A1 irrep'),
    ('verification/lean/cubic_isotropy_probe.py', None, 'unrelated label', 'check identifier A1 of the probe'),
    ('verification/lean/kinf2_foundations_probe.py', None, 'unrelated label', 'a local variable'),
    ('verification/lean/dita_index_map_probe.py', None, 'unrelated label', 'a local variable'),
    ('verification/lean/dita_torus_locus_probe.py', None, 'unrelated label', 'a local variable'),
    ('verification/lean/gap_correspondence_probe.py', None, 'unrelated label', 'a local variable'),
    ('verification/lean/partition_coupling_probe.py', None, 'unrelated label', 'finding A1 of Audit A'),
    ('verification/lean/OI_Structural_Core.lean', None, 'unrelated label', 'a bound variable of susskind3'),
    ('verification/lean/ROADMAP.md', None, 'unrelated label', 'item A1 of the Lean roadmap'),
    ('verification/lean/OI_Regulator_Symmetry.lean', None, 'unrelated label', 'item A1 of the Lean roadmap'),
    ('verification/lean-mathlib/OIBridge/Averaging.lean', None, 'unrelated label', 'item A1 of the Lean roadmap'),
    ('verification/lean-mathlib/OIBridge.lean', None, 'unrelated label', 'items A1/A5 of the Lean roadmap'),
    ('verification/coverage/LEDGER.json', 'A1 = 1, A2 = sign', 'unrelated label', 'the A1 irrep'),
    # the frozen sentence of round H-B, pinned byte-identical by the R7 guard (Z18, W21, the HB module check): preserved
    # historical evidence, unchanged by this plan and by #1482 (owner decision 4, #1169 c.7059136165; PREREG §25.3); the
    # active text beside it states the class by its condition
    ('verification/programmes/hydrodynamics/PROGRAMME.md', 'H-B: one candidate executed in the A1–A4, ¬A5 class', 'preserved historical evidence', 'round H-B frozen sentence, guard-pinned (Z18, W21); D358 states the class beside it'),
    ('verification/lean-mathlib/OIBridge/HexLatticeGas.lean', '**a rigorous reversible fluid witness in the A1–A4, ¬A5 class**', 'preserved historical evidence', 'round H-B frozen module wording, guard-pinned (Z17); the paragraph states the condition'),
    ('verification/lean-manuscript-census.json', "reads 'H-B: one candidate executed in the A1-A4, not-A5 class", 'preserved historical evidence', 'registry quotation of the frozen H-B sentence; D335 states the class by its condition'),
    ('verification/programmes/black-hole-information/PROGRAMME.md', 'A1/A2 exact-QM targets', 'unrelated label', 'the programme targets A1/A2'),
    ('verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/README.md', 'A1 and A2', 'unrelated label', 'the programme targets A1 and A2'),
    ('verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/README.md', None, 'unrelated label', 'rows A1, A2 of a results table'),
    ('verification/programmes/oi-qm/reconstruction/k1-rdy-20261105/README.md', None, 'unrelated label', 'amendment A1 of the round'),
    ('verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/', None, 'unrelated label', 'amendment A1 of the PE-01 plan'),
    ('verification/coverage/LEDGER.json', 'T1 + E + A1', 'unrelated label', 'the A1 irrep'),
    ('verification/coverage/LEDGER.json', 'the A1 inside A1 + E', 'unrelated label', 'the A1 irrep'),
    ('book/appendix-b-derivations.md', '(A1) $\\mathrm{SU}(3)^3$ anomaly', 'unrelated label', 'anomaly condition (A1) (ledger false positive)'),
    ('book/appendix-b-derivations.md', '(A1) is automatically satisfied', 'unrelated label', 'anomaly condition (A1) (ledger false positive)'),
    ('book/The-Incompleteness-of-Observation-FULL.md', '(A1) $\\mathrm{SU}(3)^3$ anomaly', 'unrelated label', 'FULL mirror of the appB anomaly condition'),
    ('book/The-Incompleteness-of-Observation-FULL.md', '(A1) is automatically satisfied', 'unrelated label', 'FULL mirror of the appB anomaly condition'),
    ('verification/lean/edge_rigidity_probe.py', None, 'guard pins', 'R7 guard: pins of frozen records\' text, of kernel identifiers and of forbidden phrases; every pin the edits break is updated by a guard-pin edit (pins check)'),
    ('verification/lean/bohr_frequency_probe.py', None, 'guard pins', 'guard F71: pins and messages; updated by guard-pin edits (pins check)'),
    # kernel-predicate prose: the Lean predicate named A1 (finiteness of the configuration space); resolved by the
    # owner's rename decision R-1 (renamed, or written "the finiteness predicate `A1`"); --final rejects this class
    ('verification/README.md', 'A1, A2 and A5 are stated', 'pending R-1', 'kernel predicates A1, A2, A5 of `Substratum`'),
    ('verification/README.md', 'satisfies A1–A5 as stated', 'pending R-1', 'kernel predicates of `waveSubstratum`'),
    ('verification/README.md', '`HB0`: A1, A2, A3 with', 'pending R-1', 'kernel predicates of `hexSubstratum`'),
    ('verification/README.md', 'A1–A4, ¬A5 class', 'pending R-1', 'the kernel class of predicates A1–A4 without A5'),
    ('verification/lean-manuscript-census.json', 'with A1, A2, A5 stated', 'pending R-1', 'kernel predicates (note of the substratum-interface family)'),
    ('verification/lean-manuscript-census.json', 'A1 fails at L = 0', 'pending R-1', 'kernel predicate in the waveZ_not_A1 control'),
    ('verification/lean-manuscript-census.json', 'HB0: A1, A2, A3', 'pending R-1', 'kernel predicates of hexSubstratum'),
    ('verification/lean-manuscript-census.json', 'put the carrier against A1-A5', 'pending R-1', 'kernel predicates of the packaged carrier'),
    ('verification/lean-manuscript-census.json', '"name": "manuscript axioms A1-A6"', 'registry identifier (kept)', 'registry family name, kept by owner decision #1169 c.7058783437 (§A.35 identifier); its note is rewritten'),
    ('verification/lean-mathlib/OIBridge/A6Instantiation.lean', '**`PK3-a` — A1**', 'pending R-1', 'docstring heading of pk3a_A1'),
    ('verification/lean-mathlib/OIBridge/A6Instantiation.lean', 'NOT A SUBSTRATUM SATISFYING A1', 'pending R-1', 'docstring of cx3b_complex_not_A1'),
    ('verification/lean-mathlib/OIBridge/HexLatticeGas.lean', 'A1–A4, ¬A5 class', 'pending R-1', 'the kernel class A1–A4 without A5 (pinned by the R7 guard)'),
    ('verification/lean-mathlib/OIBridge/HexLatticeGas.lean', '**`HB0-a` — A1**', 'pending R-1', 'docstring heading of hexSubstratum_A1'),
]


ACTIVE_IN_RECORDS = re.compile(r'^verification/programmes/(?:.*/)?(?:PROGRAMME|README)\.md$')


def classify(path, line):
    if (path.startswith(HISTORICAL_PREFIX) and not ACTIVE_IN_RECORDS.match(path)) or path in HISTORICAL_FILE:
        return 'historical record', 'preserved (frozen or landed record; Git history)'
    if (path.startswith('papers/') or path.startswith('book/')) and path.endswith(('.tex', '.pdf')):
        return 'generated artifact', 'regenerated by build.sh from the edited sources'
    rest = line
    found = None
    for pth, sub, cls, why in EXPLAINED:
        if path == pth or (pth.endswith('/') and path.startswith(pth)):
            if sub is None:
                return cls, why
            if sub in rest:
                rest = rest.replace(sub, ' ')
                found = found or (cls, why)
    if found and not REPO_PAT.search(IDENT.sub('', rest)):
        return found
    rest = IDENT.sub('', rest)
    if not REPO_PAT.search(rest):
        return 'kernel identifier', 'names a Lean declaration for the finiteness predicate or a programme; kept pending the rename decision (PREREG §22)'
    if path.startswith('papers/') or path.startswith('book/'):
        return 'manuscript', 'rewritten by the edit list'
    return 'unexplained', ''


def repo_scan(data, src, simulate, quiet=False, final=False):
    say = (lambda *a: None) if quiet else print
    files = src.all_files()
    edited = apply_edits(data, src.read) if simulate else {}
    tally, unexpl = {}, []
    for f in files:
        try:
            t = edited[f] if f in edited else src.read(f)
        except (SystemExit, UnicodeDecodeError):
            continue
        for i, line in enumerate(t.split('\n'), 1):
            if REPO_PAT.search(line):
                cls, why = classify(f, line)
                area = f.split('/')[0] if '/' in f else f
                tally[(cls, area)] = tally.get((cls, area), 0) + 1
                if cls in ('unexplained', 'manuscript') or (final and cls.startswith('pending R-')):
                    unexpl.append('%s:%d [%s] %s' % (f, i, cls, line.strip()[:120]))
    say('repository-wide scan (%s): lines by class and area' % ('after the edits, in memory' if simulate else 'as is'))
    for (c, a), n in sorted(tally.items()):
        say('  %-20s %-14s %d' % (c, a, n))
    say('repository-wide scan: %d unexplained lines' % len(unexpl))
    for x in unexpl:
        say('  UNEXPLAINED ' + x)
    return not unexpl, tally


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
    # H-11 countercontrols: docstring-only edits of a Lean file
    lean_src = '/-! Module doc: assumptions A1–A6 of the paper. -/\n/-- Doc of A1Realized. -/\ndef A1Realized : Prop := True -- note\n'
    ok_e = {'edits': [dict(id='L1', kind='lean-docstring', file='m.lean', old='assumptions A1–A6 of the paper',
                           new='assumptions A1–A6 of the paper at commit X')]}
    expect(not lean_check(ok_e, lambda p: lean_src), 'a Lean edit inside a doc comment passes the docstring-only check')
    bad_e = {'edits': [dict(id='L2', kind='lean-docstring', file='m.lean', old='def A1Realized : Prop := True',
                            new='def A1Realized : Prop := False')]}
    expect(bool(lean_check(bad_e, lambda p: lean_src)), 'a Lean edit to a definition is caught')
    ren_e = {'edits': [dict(id='L3', kind='lean-docstring', file='m.lean', old='def A1Realized', new='def FinRealized')]}
    expect(bool(lean_check(ren_e, lambda p: lean_src)), 'renaming a Lean identifier is caught')
    esc_e = {'edits': [dict(id='L4', kind='lean-docstring', file='m.lean', old='of the paper.', new='of the paper. -/ def x := 1 /-')]}
    expect(bool(lean_check(esc_e, lambda p: lean_src)), 'a replacement that closes the comment is caught')
    # configuration-space sentence and repository-wide scan countercontrols
    expect(not static_new({'edits': [E('CS', 'x', CS_SENTENCE)]})[0], 'the approved configuration-space sentence is not an infinity assertion')
    expect(bool(sim_preservation({'book/The-Incompleteness-of-Observation-FULL.md': CS_SENTENCE})), 'FULL must carry the sentence twice (ch01, ch02)')
    expect(bool(static_new({'edits': [E('CS2', 'x', CS_SENTENCE + ' Here S is infinite.')]})[0]), '"S is infinite" is still flagged next to it')
    expect(bool(sim_preservation({'papers/Main.md': 'no sentence', 'papers/Substratum.md': CS_SENTENCE})), 'a missing sentence or finite scope is caught')
    expect(bool(sim_preservation({'papers/Main.md': CS_SENTENCE * 2})), 'a duplicated sentence is caught')
    expect(classify('verification/README.md', 'whose A1–A6 are not `DerivedOI`')[0] == 'unexplained', 'an active prose A1 hit is unexplained')
    expect(classify('verification/audits/x/RESULT.md', 'A1 is open')[0] == 'historical record', 'a record hit is historical')
    expect(classify('verification/README.md', 'proved by `waveSubstratum_A1`')[0] == 'kernel identifier', 'an identifier-only hit is a kernel identifier')
    expect(classify('AGENTS.md', 'including total finiteness (A1)')[0] == 'unexplained', 'the rules document is not exempt')
    expect(classify('papers/Main.tex', 'A1')[0] == 'generated artifact', 'generated TeX is regenerated')
    expect(classify('verification/README.md', 'the A1–A4, ¬A5 class')[0] == 'pending R-1', 'kernel-predicate prose is pending the rename decision')
    rs3 = Source(fn=lambda pth: 'the A1–A4, ¬A5 class', files=['verification/README.md'])
    rs3.all_files = lambda: ['verification/README.md']
    expect(repo_scan({'edits': []}, rs3, False, True)[0] and not repo_scan({'edits': []}, rs3, False, True, final=True)[0],
           '--final rejects lines pending an owner decision')
    rs = Source(fn=lambda pth: {'a.md': 'Total finiteness is assumed.', 'verification/audits/r.md': 'A1 open'}[pth], files=['a.md'])
    rs.all_files = lambda: ['a.md', 'verification/audits/r.md']
    expect(not repo_scan({'edits': []}, rs, False, True)[0], 'the repository scan reports an unexplained active hit')
    rs2 = Source(fn=lambda pth: {'a.md': 'Total finiteness is assumed.', 'verification/audits/r.md': 'A1 open'}[pth], files=['a.md'])
    rs2.all_files = lambda: ['a.md', 'verification/audits/r.md']
    expect(repo_scan({'edits': [dict(id='Z', kind='repo-active', file='a.md', site='a.md:1', part=1, mirror_of=None, old='Total finiteness is assumed.', new='Nothing.')]}, rs2, True, True)[0],
           'the repository scan passes once the edit is applied in memory')
    # reconciliation countercontrols (owner safeguard; round 5)
    for s_ in ['so the theory works for every infinite system', 'the results hold for any configuration space',
               'valid on arbitrary carriers', 'regardless of its cardinality', 'the result extends to infinite substrata',
               'the theorem applies to infinite configuration spaces']:
        expect(bool(static_new({'edits': [E('IS', 'a set (finite under A1)', s_)]})[0]), 'safeguard: flags "%s"' % s_)
    expect(classify('verification/programmes/hydrodynamics/PROGRAMME.md', 'from A1–A6 to Navier–Stokes')[0] == 'unexplained',
           'a live programme charter is active, not historical')
    expect(classify('verification/README.md', 'satisfying `A1`, since `A1` is finiteness')[0] == 'unexplained',
           'backticked prose `A1` is not an identifier form')
    expect(classify('verification/README.md', 'satisfying the finiteness predicate `A1`')[0] == 'kernel identifier',
           'the finiteness predicate `A1` is an identifier form')
    # pins: the reviewer's three mismatch injections
    gl = {'g.md': "**Background independence (A6).** The structural assumption A6 of the reconstruction theorem (A2–A6): the substratum dynamics is covariant",
          'probe.py': "X = ('**Background independence (A6).** The sixth of the framework\'s structural assumptions '\n     'A1–A6: the substratum dynamics is covariant')\n",
          's.lean': '/-! does not derive a quantum architecture from A1-A6 or from the dynamics -/',
          'p2.py': "ok &= 'does not derive a quantum architecture from A1-A6' in t\n"}
    rd = lambda pth: gl[pth]
    good = {'edits': [dict(id='G1', kind='guard-pin', file='probe.py', site='probe.py:1', part=1, mirror_of=None, targets=['g.md'],
                           old="The sixth of the framework\'s structural assumptions '\n     'A1–A6: the substratum dynamics",
                           new="The structural assumption A6 of the '\n     'reconstruction theorem (A2–A6): the substratum dynamics")]}
    expect(not pin_targets_check(good, rd), 'pins: an updated pin that matches its target passes')
    bad1 = json.loads(json.dumps(good)); bad1['edits'][0]['new'] = "The structural assumption A6 of the '\n     'reconstruction theorem: the substratum dynamics"
    expect(bool(pin_targets_check(bad1, rd)), 'pins: D306-style pin that does not match the glossary is caught')
    bad2 = json.loads(json.dumps(good)); bad2['edits'].append(dict(id='G2', kind='consistency', file='g.md', site='g.md:1', part=1, mirror_of=None,
                                                                   old='(A2–A6): the substratum', new='(A2 to A6): the substratum'))
    expect(bool(pin_targets_check(bad2, rd)), 'pins: a glossary edit (D220/D221-style) that diverges from the updated pin is caught')
    bad3 = {'edits': [dict(id='L', kind='lean-docstring', file='s.lean', site='s.lean:1', part=1, mirror_of=None,
                           old='from A1-A6 or from', new='from the conditions or from'),
                      dict(id='G3', kind='guard-pin', file='p2.py', site='p2.py:1', part=1, mirror_of=None, targets=['s.lean'],
                           old="'does not derive a quantum architecture from A1-A6'", new="'does not derive a quantum architecture from the substratum conditions'")]}
    expect(bool(pin_targets_check(bad3, rd)), 'pins: a Lean docstring (D286-style) that diverges from its updated pins (D300/D301) is caught')
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
    ap.add_argument('--pins', action='store_true', help='check pins of tracked checks at --commit (or the drafting base)')
    ap.add_argument('--repo-scan', action='store_true', help='repository-wide scan of --commit (with --simulate: after the edits)')
    ap.add_argument('--final', action='store_true', help='with --repo-scan: lines pending an owner decision count as unexplained')
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test() else 1)
    data = load()
    ok = True
    if a.static:
        ok = static(data) and ok
    if a.pins:
        ok = pins_check(data, a.commit or data['drafting_base']) and ok
    if a.repo_scan:
        src = Source(commit=a.commit or data['drafting_base'], tree=a.tree)
        src.fallback = data.get('drafting_base')
        ok = repo_scan(data, src, a.simulate, final=a.final)[0] and ok
    elif a.commit or a.tree:
        src = Source(commit=a.commit, tree=a.tree)
        src.fallback = data.get('drafting_base')
        ok = check(data, src, a.simulate) and ok
    print('RESULT ' + ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()

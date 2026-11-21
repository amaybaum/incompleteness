#!/usr/bin/env python3
"""A1-EXIT regression comparison (#1468): frozen inputs, collection, classification and verdict.

Standard library only; run with `python3 -I -B` from a checkout of `main` that contains this record. The
procedure and decision rules are PREREG.md in this directory. Modes:

  collect --head <rev> --out <dir> --frozen-ref <rev> [--del-commit <rev>] [--prep]
      Refuses a non-empty <dir>. Resolves the head H to a full commit id. Runs C0 (frozen tools, inputs
      and ledger, read against FROZEN.json at --frozen-ref), C4 (this tool's self-test), C1-C3 (the
      baseline's check, self-test and self-compare), the comparison `baseline.py --compare <H> --json
      <dir>/compare.json` and the countercontrol C5. With --del-commit, compiles the deletion unit's
      edits from the edits.json landed at that commit into <dir>/edits-del.json. --prep marks a
      preparation run, allowed only with the pin as head, whose frozen ref is the checkout HEAD. Writes
      <dir>/controls.json. Exit 0 when every control passes, 4 otherwise.
  verdict --dir <dir> --classify <classify.json>
      Checks that every input is this run's and names H, runs C0 again, the edit-input control C6, the
      countercontrols C7-C9, classifies every reported item under the rules of PREREG §3 and writes
      <dir>/verdict.json. Exit 0 PASS, 5 FAIL, 3 PENDING, 4 VOID; 2 when it refuses to run. Any other
      status (1 is an uncaught exception) is no verdict.
  compile-s2 [--out <file>]
      Compiles the Step-2 edit lists from the Git objects at PIN_S2 (default: print).
  compile-del --commit <rev> [--out <file>]
      Compiles the deletion unit's edit list from the edits.json landed at <rev>, JSON to JSON.
  check-edits [--del <edits-del.json> --del-commit <rev>]
      Control C6 alone.
  self-test
      Controls of this tool on synthetic data built from the pinned corpus (no after-state is read),
      including the mutants that each of C6-C9 must catch.
  digests
      The SHA-256 of every frozen file (the content of FROZEN.json).

Schemas (JSON, UTF-8):
  edits           a1exit-compare-edits/2: {"schema", "pin", "units": {<unit>: {"pr", "merge", "sources"}},
                  "edits": [{"key", "unit", "pr", "id", "seq", "files", "old", "new", "rows", "components"}]}
                  key = "<unit>:<id>"; seq is the replay order (landing order, then list order).
  classify.json   a1exit-compare-classify/2: {"schema", "head", "classifier", "result_pr", "items":
                  {<item key>: {"class": "J"|"R", "edits": [<edit key>...], "ledger_row": <row or null>,
                  "reason": <text>, "resolution": null | {"outcome": "justified"|"unjustified",
                  "review": <URL>, "reviewer": <login>, "proof": <citation or null>}}}}
                  Item keys: an entry id ("M:780"); "U:<file>:<line>" for an unaccounted line;
                  "D:<file>:<line>" for a deleted line (lines as in compare.json). An item not listed
                  is unclassified and counts as U.
  controls.json   a1exit-compare-controls/2: {"schema", "head", "frozen_ref", "del_commit",
                  "controls": {<name>: {"exit", "pass", "detail"}}, "injection", "files": {<name>: sha256}}
  verdict.json    a1exit-compare-verdict/2: {"schema", "head", "verdict", "counts", "items", "controls",
                  "countercontrols", "resolutions", "inputs", "landed_units", "requirement6_settled",
                  "text"}
                  Replay-missing items are keyed "RM:<file>:<line of the replayed state>" or
                  "RM:edit:<edit key>:<file>"; they are U unless marked R and resolved.
"""
import copy
import difflib
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
RECORD = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(RECORD, '..', '..', '..', '..'))
sys.path.insert(0, RECORD)
import baseline as B  # noqa: E402

FULL = B.FULL
REC_REL = 'verification/audits/foundations/a1exit-regression-20261121'
PIN_S2 = '7f28886f4cc96fbfa7407af1fdc37de2f0e562e5'     # drafting base: all five Step-2 units landed
LEDGER_ROWS = 'verification/audits/foundations/a1exit-ledger-20261120/rows.json'   # read at PIN_S2
DEL_EDITS = 'verification/audits/foundations/a1exit-deletion-20261121/edits.json'
EDITS_S2 = os.path.join(HERE, 'inputs', 'edits-s2.json')
DELETION_UNIT = 'DEL'
REPO_URL = 'https://github.com/amaybaum/incompleteness'
EXIT = {'PASS': 0, 'FAIL': 5, 'PENDING': 3, 'VOID': 4}
SCI_CATEGORIES = {'C-TAB', 'C-PROSE', 'C-FINL', 'C-CDO', 'C-CAL', 'C-OBS', 'C-OPEN'}

# Status and scope terms of J9 (counted, not merely detected).
OPEN_TERMS = re.compile(r'\b(open|conditional(?:ly)?|hypothes[ie]s|assumed|posit(?:ed)?|not established|'
                        r'not derived|conjectur\w*)\b', re.I)
# Finite-scope terms (stems and forms; review c.7061319560, N3): finite, finitely, finiteness,
# finitary and the like, "< \\infty" in any form, bounded, compact. A fall in their count is a J10 hit.
FINITE_TERMS = re.compile(r'\bfinit\w*|<\s*\\infty|\\lt\s*\\infty|<\s*∞|\bbounded\b|\bcompact\b', re.I)
# J10, layer 2: frozen vocabularies, counted on normalized text. A rise in the count of any term below,
# or a fall in the count of FINITE_TERMS, makes a covered item R and flagged. Layer 1, the structural
# token-level gain rule, is `gain`. The only text removed before either layer is the exact ALLOWLIST,
# matched as a whole sentence.
PROMOTION_TERMS = [r'\bunconditional(?:ly)?\b', r'\bproved\b', r'\bproven\b', r'\bproofs?\b', r'\btheorem\b',
                   r'\bestablished\b', r'\bderived\b', r'\bshown\b', r'\bdemonstrated\b', r'\bin general\b',
                   r'\bgeneral(?:ly|ity)?\b', r'\buniversal(?:ly)?\b', r'\balways\b', r'\bwithout exception\b']
INFINITY_TERMS = [r'infinit\w*', r'\\infty', r'∞', r'\\aleph', r'ℵ', r'\b(?:un)?countabl\w*', r'\bcardinal\w*',
                  r'\barbitrar\w*', r'\bfiniteness\b', r'\bfinite or not\b', r'\bnot necessarily finite\b',
                  r'\b(?:for|over) (?:all|every|any|each)\b', r'\b(?:of|for) any (?:size|order|number)\b',
                  r'\bany number of\b', r'\bregardless\b', r'\bwhatever\b', r'\bwhatsoever\b',
                  r'\bnon-?\s*finite\b', r'\bnot\s+(?:necessarily\s+)?finite\b', r'\bneed not be finite\b',
                  r'\bunrestricted\b', r'\birrespective\b', r'\bindependent of\b', r'\buniform(?:ly)?\b',
                  r'\blarge or small\b', r'\bno assumption\b', r'\bbeyond the finite\b', r'\btransfinite\b',
                  r'\bcontinuum\b', r'\\omega', r'ω', r'\\mathbb\s*\{?\s*N\b', r'\|\s*\\?(?:mathcal\s*\{?\s*)?S\s*\}?\s*\|',
                  r'\\kappa', r'κ', r'\\to\s*\\infty',
                  r'\bin (?:either|both|all|every|any) cases?\b', r'\bunbounded\w*', r'\bunlimited\b',
                  r'\bwithout (?:any |a )?(?:finit\w*|bound\w*|restriction|limit\w*)\b',
                  r'\bno (?:restriction|bound|limit)\b', r'\b(?:all|every) (?:sizes?|cardinalit\w*)\b',
                  r'\b(?:every|all|any|each)\s+\$']
# The exact allowlist: the owner's configuration-space sentence (#1169 c.7058446475) verbatim, and its
# rendering with $S$ in the deletion plan of #1477, each matched only as a whole sentence. No other text
# is exempt.
ALLOWLIST = [
    {'phrase': 'The substratum has a configuration space $\\mathcal S$. No restriction is imposed on its '
               'cardinality; $\\mathcal S$ may be finite or infinite.', 'row': None, 'proof': None,
     'authority': '#1169 c.7058446475'},
    {'phrase': 'The substratum has a configuration space $S$. No restriction is imposed on its cardinality; '
               '$S$ may be finite or infinite.', 'row': None, 'proof': None,
     'authority': '#1169 c.7058446475, as rendered in #1477'},
]
J10_SENTENCE = ' The same identity extends to every infinite system.'
PARAPHRASES = [  # review c.7059976436 finding 1: each must hit J10
    'for arbitrary $S$', 'regardless of cardinality', 'in the infinite case', 'for infinite $S$',
    'when $|S| = \\infty$', 'for $S$ of any size', 'for countable or uncountable $S$', 'for every $S$, finite or not',
    'without any finiteness assumption', 'whatever the cardinality of $S$', 'including the infinite case',
    'for all $S$', 'also for infinite $S$', 'regardless of the cardinality of the configuration space',
    'and $S$ may be finite or infinite; the result holds in either case',
    'the configuration space $S$ may be finite or infinite, and the statement holds in both cases']
# Review c.7060670839 (N1): 28 further wordings, inserted after "members" in GR:134, each with a covering
# edit; with the 16 above and the allowlist-plus-claim cases, each must come out flagged.
EVASIONS = [
    ', for unrestricted $S$', ', for non-finite $S$', ', for $S$ not finite', '; $S$ need not be finite',
    ' (also when $S$ is not finite)', ' (including non-finite $S$)', ', for unboundedly large $S$',
    ', irrespective of $|S|$', ', for $S$ large or small', '; no assumption on $|S|$ is made',
    ', holding uniformly in $S$', '. This extends beyond the finite setting', ', for $|S|\\geq\\omega$',
    ', for $S$ of continuum size', ', in the transfinite case', ', for $\\mathbb{N}$-indexed configuration sets',
    ', for in\\-finite $S$', ', for in­finite $S$', ', for infіnite $S$', '[^gen]',
    ', for $|S| = 2^{\\aleph_0}$', ', for every size of $S$', ', for every one of the possible $S$',
    ', for any $S$ whatsoever', ', for $|S|=\\aleph_0$', ', as $N\\to\\infty$', ', for $\\kappa$ any cardinal',
    ', for $S$ countable or not']
ALLOW_PLUS = ['This identity is independent of $|S|$', 'It holds for each such $S$']
GAIN_ONLY = ', as noted in the companion paper'   # no vocabulary term: only the gain rule flags it
# Review c.7061319560 (N3, N4): changes made of deletions, reorderings, operator flips and punctuation,
# each cited to an edit that reproduces it exactly; each must be flagged.
NCASES = [
    ('appB:194', 'a function of finitely many components', 'a function of components', 'X-52', 'N3'),
    ('ch01:121', '\\Gamma_s(b)) \\leq 1 - m$', '\\Gamma_s(b)) \\geq 1 - m$', 'X-20', 'N4a'),
    ('ch01:121', '$d(\\Gamma_s(a), \\Gamma_s(b)) \\leq 1 - m$', '$1 - m \\leq d(\\Gamma_s(a), \\Gamma_s(b))$', 'X-20', 'N4b'),
    ('ch01:95', 'Let $\\mathcal{C}_V$ and $\\mathcal{C}_H$ be finite sets with',
     'Let $\\mathcal{C}_V$ be finite sets and $\\mathcal{C}_H$ with', 'X-20', 'N4c'),
    ('GR:134', 'on all its members. $\\square$', 'on all its members $\\square$', 'X-52', 'N4d'),
    ('appA:30', 'alone does not verify that relation.', 'alone does verify that relation.', 'X-47', 'N4e'),
    ('appB:46', 'invariant-product condition (IP), assumed', 'invariant-product condition, assumed', 'X-15', 'N4f'),
    ('appB:169', '\\epsilon^2/(4G\\sigma)$ between', '\\epsilon^4/(4G\\sigma)$ between', 'X-72', 'N4g'),
    ('GR:134', 'on all its members. $\\square$', 'on all its members. on all its members. $\\square$', 'X-52', 'N4h'),
    ('M:564', 'a substratum of $N < \\infty$ ontic configurations', 'a substratum of ontic configurations', 'X-48', 'N4i'),
    ('ch01:119', 'for a Hamiltonian flow on compact energy surfaces', 'for a Hamiltonian flow on energy surfaces',
     'X-20', 'N4j')]


DEC_RE = re.compile(r'(?<![\w.])\d+\.\d+')
UNIT_AFTER_NUM = re.compile(r'\d\s*\$?\s*(?:\\,|\\;|~)?\s*(?:\\%|%|\\text\{\s*[kMGT]?eV\s*\}|[kMGTm]?eV\b|'
                            r'km/s|Mpc|kpc|ppm|ppb|Gyr|Myr|yr\b|years?\b|[kMG]?Hz\b|nm\b|fm\b|cm\b|mm\b|'
                            r'kg\b|K\b|ms\b|ns\b|s\b|m\b|bits?\b|°|dB\b)')
POW10_RE = re.compile(r'10\s*\^|\\times\s*10|×\s*10|\d[eE][+-]?\d')


def norm(s):
    return ' '.join(s.split())


def sha256_file(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def git_try(*args):
    r = subprocess.run(['git', '-C', ROOT] + list(args), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def resolve(rev):
    out = git_try('rev-parse', '--verify', '--quiet', '%s^{commit}' % rev)
    return out.decode().strip() if out else None


def show(rev, path):
    return B.git('show', '%s:%s' % (rev, path)).decode('utf-8')


def run(argv):
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True).returncode


def write_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    os.replace(tmp, path)


def read_json(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


# =========================================================================== frozen files (C0)

FROZEN_FILES = {'baseline.py': os.path.join(RECORD, 'baseline.py'),
                'snapshot.json': os.path.join(RECORD, 'snapshot.json'),
                'compare/verdict.py': os.path.abspath(__file__),
                'compare/inputs/edits-s2.json': EDITS_S2}


def digests():
    out = {k: sha256_file(p) for k, p in sorted(FROZEN_FILES.items())}
    out['ledger rows.json at PIN_S2'] = sha256_bytes(B.git('show', '%s:%s' % (PIN_S2, LEDGER_ROWS)))
    return out


def main_ref():
    """The checkout's main: origin/main where it resolves, else main."""
    return next((r for r in ('origin/main', 'main') if resolve(r)), None)


def pinned_frozen_commit():
    """The commit on main's first-parent chain that last changed FROZEN.json: this record's merge, or the
    merge of its latest amendment."""
    m = main_ref()
    out = git_try('log', '--first-parent', '-1', '--format=%H', m, '--', REC_REL + '/compare/FROZEN.json') if m else None
    return out.decode().strip() or None if out else None


def c0(frozen_ref, prep=False):
    """C0: the frozen ref is the pinned commit (the commit on main's first-parent chain that last changed
    FROZEN.json); the files in use equal the digests of FROZEN.json read from the Git object at that ref;
    the frozen blobs at that ref have those digests; and PREREG.md at that ref states each digest in full.
    The working-tree FROZEN.json is never read. In a preparation run (prep, only at the pin) the ref is the
    checkout's HEAD instead, and the result says so."""
    ref = resolve(frozen_ref) if frozen_ref else None
    if not ref:
        return False, 'frozen ref %r does not resolve' % frozen_ref
    if prep:
        if ref != resolve('HEAD'):
            return False, 'preparation run: the frozen ref must be the checkout HEAD'
    else:
        pinned = pinned_frozen_commit()
        fp = git_try('rev-list', '--first-parent', main_ref()) if main_ref() else None
        if not pinned or ref != pinned or not fp or ref not in fp.decode().split():
            return False, 'frozen ref %s is not the pinned commit %s on the first-parent chain of main' % (ref, pinned)
    try:
        want = json.loads(show(ref, REC_REL + '/compare/FROZEN.json'))['sha256']
        prereg = show(ref, REC_REL + '/compare/PREREG.md')
    except (subprocess.CalledProcessError, ValueError, KeyError):
        return False, 'FROZEN.json or PREREG.md missing at %s' % ref
    got = digests()
    bad = sorted(k for k in set(want) | set(got) if want.get(k) != got.get(k))
    for k in FROZEN_FILES:
        blob = git_try('show', '%s:%s/%s' % (ref, REC_REL, k))
        if blob is None or sha256_bytes(blob) != want.get(k):
            bad.append('blob at ref: ' + k)
    unstated = sorted(k for k, v in want.items() if v not in prereg)
    if bad or unstated:
        return False, 'mismatch %s; not stated in PREREG.md %s' % (bad, unstated)
    return True, ('preparation run, frozen ref the checkout HEAD %s (not a pinned commit)' % ref) if prep \
        else 'frozen ref %s, the pinned commit' % ref


# =========================================================================== edit inputs

MS = 'verification/audits/manuscript/'
UNITS = [  # unit, PR, merge, record, allowlisted sources in composition order
    ('S2-A', 1470, '0cd5d5bfb4f6641c8b08706c4eb636ee730ebbf0', MS + 'a1exit-s2a-20261121/',
     ['checks/s2a_edits.json']),
    ('S2-B', 1473, 'a1f38284d21338b66119c870a551a670c73e3fa7', MS + 'a1exit-s2b-20261121/',
     ['PREREG.md', 'amendments/A1-round1.md', 'amendments/A2-return-form.md', 'amendments/A3-cptp-register.md']),
    ('S2-C', 1474, '0ba358ccf05eb461c3a5bd686062f65115c293fc', MS + 'a1exit-s2c-20261121/', ['PREREG.md', 'amendments/A1.md', 'RESULT.md']),
    ('S2-D', 1472, '4de2eabd6c7c88dc214db70a813ec44b8641b630', MS + 'a1exit-s2d-20261121/', ['PREREG.md', 'amendments/A1.md']),
    ('S2-E', 1475, '7f28886f4cc96fbfa7407af1fdc37de2f0e562e5', MS + 'a1exit-s2e-20261121/', ['checks/s2e_edits.json', 'checks/s2e_amend1.json']),
]
UNIT_PR = {u[0]: u[1] for u in UNITS}
XROW = re.compile(r'X-\d+')
SITE = re.compile(r'`((?:papers|book)/[^`:]+\.md):(\d+)`')
FENCE = re.compile(r'^(`{3,})text\s*$')
ABBR = {'Main': 'papers/Main.md', 'M': 'papers/Main.md'}


class CompileError(Exception):
    pass


def _fence(L, i, path):
    while i < len(L) and not L[i].strip():
        i += 1
    m = FENCE.match(L[i]) if i < len(L) else None
    if not m:
        raise CompileError('%s:%d: expected a text fence' % (path, i + 1))
    j = i + 1
    while j < len(L) and L[j] != m.group(1):
        j += 1
    if j == len(L):
        raise CompileError('%s:%d: unclosed fence' % (path, i + 1))
    return ('\n'.join(L[i + 1:j]), [i + 2, j]), j + 1


def _block(path, head, L, o, n):
    hl, h = head
    m = re.match(r'^### (\S+) —', h)
    if not m:
        raise CompileError('%s:%d: heading without an edit ID' % (path, hl))
    files = [f for f, _ in SITE.findall(h)]
    if not files:
        k = hl
        while k < len(L) and not re.match(r'^Sites?\b', L[k]):
            k += 1
        files = [f for f, _ in SITE.findall(L[k])] if k < len(L) else []
    if not files:
        raise CompileError('%s:%d: no site' % (path, hl))
    rows = XROW.findall(h.split('ledger', 1)[1]) if 'ledger' in h else XROW.findall(h)
    d = {'id': m.group(1), 'files': files, 'rows': rows, 'source_path': path, 'head_line': hl}
    if o:
        d.update(old=o[0], new=n[0], old_lines=o[1], new_lines=n[1])
    return d


def md_blocks(path, src):
    """Paired `Old ...:` / `New:` fenced blocks under `### <ID> —` headings; `identical to <ID>` copies."""
    L = src.split('\n')
    out, i, head = [], 0, None
    while i < len(L):
        ln = L[i]
        if ln.startswith('### '):
            head = (i + 1, ln)
        if re.match(r'^Old(?: \(unique in (?:each|its) file\))?:\s*$', ln) and head:
            o, i = _fence(L, i + 1, path)
            j = i
            while j < len(L) and not L[j].strip():
                j += 1
            if j == len(L) or L[j].strip() != 'New:':
                raise CompileError('%s:%d: Old block without a New block' % (path, i))
            n, i = _fence(L, j + 1, path)
            out.append(_block(path, head, L, o, n))
            head = None
            continue
        m = re.match(r'^Old and new strings: identical to (\S+) \(unique in FULL\.md\)\.\s*$', ln)
        if m and head:
            out.append(dict(_block(path, head, L, None, None), copy_of=m.group(1), copy_line=i + 1))
            head = None
        i += 1
    return out


def md_table(src, cols):
    out = []
    for k, ln in enumerate(src.split('\n')):
        if not ln.startswith('| ') or ln.startswith(('| ID |', '| Id |', '|---')):
            continue
        cells = [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', ln)[1:-1]]
        if len(cells) != len(cols):
            continue
        d = dict(zip(cols, cells))
        if re.match(r'^[A-Z][\w-]*$', d['id']):
            out.append((k + 1, d))
    return out


def _unquote(s):
    s = s.strip()
    return s[1:-1] if len(s) >= 2 and s[0] == s[-1] and s[0] in '`"' else s


def _site_files(cell):
    fs = [f for f, _ in SITE.findall(cell)]
    if not fs:
        m = re.match(r'^(\w+):\d+$', cell.strip())
        if not m or m.group(1) not in ABBR:
            raise CompileError('unresolvable site %r' % cell)
        fs = [ABBR[m.group(1)]]
    return fs


def md_bullets(src):
    """`**A1-n ...**` items carrying `- old: "..."` and `- new: "..."`; wrapped lines join with one space."""
    L = src.split('\n')
    out, cur = [], None
    for i, ln in enumerate(L):
        m = re.match(r'^\*\*(A1-\d+)\b', ln)
        if m:
            cur = {'id': m.group(1), 'head_line': i + 1, 'intro': ln}
            out.append(cur)
            continue
        if cur is not None and 'old' not in cur and not ln.startswith('- old'):
            cur['intro'] += ' ' + ln
        for key in ('old', 'new'):
            if cur is not None and ln.startswith('- %s: "' % key):
                j, parts = i, [ln[len('- %s: "' % key):]]
                while not parts[-1].endswith('"'):
                    j += 1
                    parts.append(L[j].strip())
                cur[key] = ' '.join(parts)[:-1]
                cur[key + '_lines'] = [i + 1, j + 1]
    return out


def _comp(d):
    return {k: d[k] for k in ('id', 'source_path', 'index', 'line', 'head_line', 'old_lines', 'new_lines',
                              'copy_line', 'old_from') if k in d}


def _unit_raw(unit, merge, rec, srcs, rev):
    base, amends, blobs = [], [], {}
    for s in srcs:
        p = rec + s
        blobs[p] = B.git('rev-parse', '%s:%s' % (rev, p)).decode().strip()
        txt = show(rev, p)
        if s.endswith('.json'):
            for idx, o in enumerate(json.loads(txt)):
                files = ([o['file']] + ([o['mirror'][0]] if o.get('mirror') else [])
                         + ([FULL] if o.get('full_mirror') else []))
                d = {'id': o['id'], 'files': files, 'rows': XROW.findall(o.get('row', '')), 'old': o['old'],
                     'new': o['new'], 'source_path': p, 'index': idx, 'amends': o.get('amends')}
                (amends if o.get('amends') else base).append(d)
        elif unit == 'S2-C' and s == 'PREREG.md':
            for ln, d in md_table(txt, ['id', 'site', 'row', 'finding', 'old', 'new']):
                base.append({'id': d['id'], 'files': _site_files(d['site']), 'rows': XROW.findall(d['row']),
                             'old': d['old'], 'new': d['new'], 'source_path': p, 'line': ln})
        elif unit == 'S2-C' and s == 'amendments/A1.md':
            order = re.search(r'applied in the order (A1-\d), (A1-\d), (A1-\d)', txt).groups()
            nsites = int(re.search(r'\((\d+) sites:', txt).group(1))
            bl = {b['id']: b for b in md_bullets(txt)}
            for bid in order:
                b = bl[bid]
                fs = [f for f, _ in SITE.findall(b['intro'])]
                fs += [FULL] if fs and '= FULL:' in b['intro'] else []
                amends.append({'id': bid, 'files': fs or None, 'rows': [], 'old': b['old'], 'new': b['new'],
                               'source_path': p, 'old_lines': b['old_lines'], 'new_lines': b['new_lines'],
                               'expect_sites': nsites if bid == 'A1-1' else None})
        elif unit == 'S2-C' and s == 'RESULT.md':
            # §9.1: the one catch-up resolution (§9: "each old string occurred once ... except C4's").
            L = txt.split('\n')
            h = L.index('#### M:224')
            q = next(i for i in range(h, len(L)) if L[i].startswith('> '))
            parent = B.git('rev-parse', merge + '^1').decode().strip()
            amends.append({'id': 'C4-resolved', 'files': ['papers/Main.md'], 'rows': [],
                           'old': show(parent, 'papers/Main.md').split('\n')[223], 'new': L[q][2:],
                           'source_path': p, 'new_lines': [q + 1, q + 1], 'replaces': 'C4',
                           'old_from': '%s:papers/Main.md:224' % parent})
        elif s.startswith('amendments/A3'):
            for ln, d in md_table(txt, ['id', 'site', 'old', 'new']):
                amends.append({'id': d['id'], 'files': _site_files(d['site']), 'rows': [],
                               'old': _unquote(d['old']), 'new': _unquote(d['new']), 'source_path': p, 'line': ln})
        else:
            for b in md_blocks(p, txt):
                if 'copy_of' in b:
                    src_b = next(x for x in base if x['id'] == b['copy_of'])
                    b = dict(b, old=src_b['old'], new=src_b['new'])
                (base if s == 'PREREG.md' else amends).append(b)
    return base, amends, blobs


def compile_s2(rev=PIN_S2):
    """The Step-2 edit lists, amendments composed, from the Git objects at rev. Composition rule: an
    amendment with an `amends` field composes into that edit; any other amendment composes into every
    edit of its unit, in its files, whose current new string contains its old string (exactly once
    there); with no such edit it is a standalone edit of its unit."""
    edits, units, seq = [], {}, 0
    for unit, pr, merge, rec, srcs in UNITS:
        base, amends, blobs = _unit_raw(unit, merge, rec, srcs, rev)
        units[unit] = {'pr': pr, 'merge': B.git('rev-parse', merge).decode().strip(), 'sources': blobs}
        eff = [dict(b, components=[_comp(b)]) for b in base]
        for a in amends:
            if a.get('replaces'):
                tgt = next(e for e in eff if e['id'] == a['replaces'])
                eff[eff.index(tgt)] = dict(a, components=tgt['components'] + [_comp(a)], rows=tgt['rows'])
                continue
            if a.get('amends'):
                parents = [e for e in eff if e['id'] == a['amends']]
            else:
                parents = [e for e in eff if a['old'] in e['new']
                           and (not a['files'] or set(a['files']) & set(e['files']))]
            for e in parents:
                if e['new'].count(a['old']) != 1:
                    raise CompileError('%s %s: old string not once in %s' % (unit, a['id'], e['id']))
                e['new'] = e['new'].replace(a['old'], a['new'])
                e['components'].append(_comp(a))
            if not parents:
                eff.append(dict(a, components=[_comp(a)]))
            if a.get('expect_sites') is not None:
                nf = sum(len(e['files']) for e in eff if a['new'] in e['new'])
                if nf != a['expect_sites']:
                    raise CompileError('%s %s: %d sites, record states %d' % (unit, a['id'], nf, a['expect_sites']))
        for e in eff:
            seq += 1
            edits.append({'key': '%s:%s' % (unit, e['id']), 'unit': unit, 'pr': pr, 'id': e['id'], 'seq': seq,
                          'files': e['files'], 'old': e['old'], 'new': e['new'], 'rows': e['rows'],
                          'components': e['components']})
    return {'schema': 'a1exit-compare-edits/2', 'pin': rev, 'units': units, 'edits': edits}


def compile_del(commit):
    """The deletion unit's edits, JSON to JSON from the edits.json landed at commit (manuscript files).
    A record whose old string equals its new string (a site retained unchanged) is not an edit; its ID
    is listed under `retained_unchanged`."""
    c = resolve(commit)
    data = json.loads(show(c, DEL_EDITS))
    blob = B.git('rev-parse', '%s:%s' % (c, DEL_EDITS)).decode().strip()
    edits, retained = [], []
    for idx, o in enumerate(data['edits']):
        f = o['file']
        if not (f.endswith('.md') and f.split('/')[0] in ('papers', 'book') and f.count('/') == 1):
            continue
        if o['old'] == o['new']:
            retained.append(o['id'])   # a site recorded as retained unchanged: no edit, covers nothing
            continue
        edits.append({'key': '%s:%s' % (DELETION_UNIT, o['id']), 'unit': DELETION_UNIT, 'pr': None,
                      'id': o['id'], 'seq': 100000 + idx, 'files': [f], 'old': o['old'], 'new': o['new'],
                      'rows': XROW.findall(o.get('row') or ''),
                      'components': [{'id': o['id'], 'source_path': DEL_EDITS, 'index': idx}]})
    return {'schema': 'a1exit-compare-edits/2', 'pin': c,
            'units': {DELETION_UNIT: {'pr': None, 'merge': c, 'sources': {DEL_EDITS: blob}}}, 'edits': edits,
            'retained_unchanged': retained}


def apply_unit(corpus, edits):
    """Apply a unit's edits in seq order to a corpus copy; every old string exactly once in its file."""
    cur, bad = dict(corpus), []
    for e in sorted(edits, key=lambda x: x['seq']):
        for f in e['files']:
            c = cur.get(f, '').count(e['old'])
            if c != 1:
                bad.append('%s: old string %dx in %s' % (e['key'], c, f))
                continue
            cur[f] = cur[f].replace(e['old'], e['new'])
    return cur, bad


def corpus_diff(a, b):
    return sorted(f for f in set(a) | set(b) if a.get(f) != b.get(f))


def structural(lst, unit_set):
    bad = []
    for e in lst['edits']:
        u = e['unit']
        if u not in unit_set:
            bad.append('%s: unit not a justification source' % e['key'])
            continue
        if e['key'] != '%s:%s' % (u, e['id']):
            bad.append('%s: key' % e['key'])
        if u != DELETION_UNIT and e['pr'] != UNIT_PR[u]:
            bad.append('%s: PR %s is not %s\'s' % (e['key'], e['pr'], u))
        if not e['old'] or e['old'] == e['new']:
            bad.append('%s: empty or no-op edit' % e['key'])
        allowed = set(lst['units'][u]['sources'])
        for c in e['components']:
            if c['source_path'] not in allowed:
                bad.append('%s: source %s is not on %s\'s allowlist' % (e['key'], c['source_path'], u))
    return bad


def c6(edits_s2, edits_del, del_commit, head):
    """C6, the edit inputs: (a) the frozen Step-2 list is reproduced exactly by compile-s2 from the
    records; (b) every edit is non-empty, not a no-op, of a listed unit and PR, with every component
    from that unit's allowlisted sources; (c) replaying each unit's edits from the pin reproduces every
    manuscript file at each unit's merge, in landing order; (d) the deletion list is reproduced exactly
    by compile-del from the landed edits.json, the deletion commit is an ancestor of H, and its edits
    applied to its first parent reproduce its manuscript files."""
    bad = []
    try:
        if compile_s2(edits_s2['pin']) != edits_s2 or edits_s2['pin'] != PIN_S2:
            bad.append('(a) the Step-2 list differs from its compilation from the records')
    except (CompileError, subprocess.CalledProcessError, StopIteration, AttributeError, ValueError) as ex:
        bad.append('(a) compile-s2 failed: %s' % ex)
    bad += ['(b) ' + x for x in structural(edits_s2, set(UNIT_PR))]
    cur = dict(B.PIN_CORPUS())
    for unit, _, _, _, _ in UNITS:
        cur, b = apply_unit(cur, [e for e in edits_s2['edits'] if e['unit'] == unit])
        want = B.corpus_at_commit(edits_s2['units'][unit]['merge'])
        bad += ['(c) ' + x for x in b]
        bad += ['(c) %s: %s differs from the merge' % (unit, f) for f in corpus_diff(cur, want)]
        cur = want
    if edits_del is None:
        if head != B.PIN:
            bad.append('(d) no deletion edit list for a head that is not the pin')
        note = 'deletion list not applicable (head is the pin)' if head == B.PIN else ''
    else:
        note = ''
        try:
            if compile_del(del_commit) != edits_del:
                bad.append('(d) the deletion list differs from its compilation from %s' % del_commit)
            if git_try('merge-base', '--is-ancestor', resolve(del_commit), head) is None:
                bad.append('(d) the deletion commit is not an ancestor of H')
            bad += ['(b) ' + x for x in structural(edits_del, {DELETION_UNIT})]
            dc = resolve(del_commit)
            cur, b = apply_unit(B.corpus_at_commit(dc + '^1'), edits_del['edits'])
            bad += ['(d) ' + x for x in b]
            bad += ['(d) %s differs from the deletion commit' % f for f in corpus_diff(cur, B.corpus_at_commit(dc))]
        except (subprocess.CalledProcessError, KeyError, ValueError, TypeError) as ex:
            bad.append('(d) %s' % ex)
    return not bad, bad, note


# =========================================================================== replay rule (J1-J8)

def _lines_span(text, s, e):
    """Indices of the lines of text that the span [s, e) touches; an empty span takes the line holding
    s, and the line before it when s starts a line."""
    starts = [0] + [m.end() for m in re.finditer('\n', text)]

    def line_of(x):
        lo, hi = 0, len(starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if starts[mid] <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo
    if e > s:
        return line_of(s), line_of(e - 1)
    i = line_of(s)
    return (i - 1 if i > 0 and starts[i] == s else i), i


def replay(text, edits, anchor=None):
    """Apply edits (seq order) to text, each old string exactly once. Returns (text, spans, error).
    A span is [cur_s, cur_e, base_s, base_e, tags]: a region of the replayed text and its baseline
    counterpart. The anchor (a baseline character span) is tracked as a span tagged 'anchor'."""
    spans = [[anchor[0], anchor[1], anchor[0], anchor[1], {'anchor'}]] if anchor else []
    for e in sorted(edits, key=lambda x: x['seq']):
        old, new = e['old'], e['new']
        if text.count(old) != 1:
            return None, None, '%s: old string %dx' % (e['key'], text.count(old))
        p = text.index(old)
        q, d = p + len(old), len(new) - len(old)

        def to_base(x):
            return x - sum((sp[1] - sp[0]) - (sp[3] - sp[2]) for sp in spans if sp[1] <= x)
        hit = [sp for sp in spans if sp[0] <= q and sp[1] >= p]
        bs = min([sp[2] for sp in hit] + ([to_base(p)] if not any(sp[0] <= p <= sp[1] for sp in hit) else []))
        be = max([sp[3] for sp in hit] + ([to_base(q)] if not any(sp[0] <= q <= sp[1] for sp in hit) else []))
        cs = min([sp[0] for sp in hit] + [p])
        ce = max([sp[1] + d if sp[1] > q else p + len(new) for sp in hit] + [p + len(new)])
        tags = set().union(*[sp[4] for sp in hit]) | {'edit:' + e['key']}
        rest = [sp for sp in spans if sp not in hit]
        rest = [sp if sp[1] < p else [sp[0] + d, sp[1] + d, sp[2], sp[3], sp[4]] for sp in rest]
        spans = sorted(rest + [[cs, ce, bs, be, tags]], key=lambda sp: sp[0])
        text = text[:p] + new + text[q:]
    return text, spans, None


def _region(text, s, e):
    a, b = _lines_span(text, s, e)
    return B.lines_of(text)[a:b + 1], a


def _find_block(after_lines, block, at=None):
    nb = [norm(x) for x in block]
    na = [norm(x) for x in after_lines]
    n = len(nb)
    starts = range(max(0, at - n + 1), min(at, len(na) - n) + 1) if at is not None else range(len(na) - n + 1)
    return next((j for j in starts if na[j:j + n] == nb), None)


def cover(item, cited, base_corpus, after_corpus, landed=None):
    """The replay rule. Returns (covered, notes, before region, replayed region, touching edit keys, the
    H text of that region). With the
    landed edits given (every run against a real H), completeness holds as well: every cited edit is
    landed, every landed edit that touches the item's region is cited, and the region replayed from the
    cited edits equals the region of the replayed state (all landed edits)."""
    notes, before, after, touch, ok = [], item['before'] or '', item['after'] or '', set(), True
    cited = [e for e in cited if e['old'] != e['new']]
    ckeys = {e['key'] for e in cited}
    if landed is not None:
        lkeys = {e['key'] for e in landed}
        stray = sorted(ckeys - lkeys)
        if stray:
            return False, ['cited edits not landed at H: %s' % ', '.join(stray)], before, after, touch

    def complete_anchored(f, a, b, blk):
        if landed is None:
            return ''
        text = base_corpus.get(f, '')
        rt2, sp2, err = replay(text, [e for e in landed if f in e['files']], (a, b))
        if err:
            return 'replayed state: ' + err
        s2 = next(s for s in sp2 if 'anchor' in s[4])
        k2 = {t[5:] for t in s2[4] if t.startswith('edit:')}
        miss = sorted(k2 - ckeys)
        if miss:
            return 'landed edits touching the region are not cited: %s' % ', '.join(miss)
        if [norm(x) for x in _region(rt2, s2[0], s2[1])[0]] != [norm(x) for x in blk]:
            return 'the cited replay differs from the replayed state in this region'
        return ''

    def anchored(f, line, at_file, at_line):
        text = base_corpus.get(f, '')
        ls = B.lines_of(text)
        a = sum(len(x) + 1 for x in ls[:line - 1])
        rt, spans, err = replay(text, [e for e in cited if f in e['files']], (a, a + len(ls[line - 1])))
        if err:
            return False, err, None, None, set(), None
        sp = next(s for s in spans if 'anchor' in s[4])
        keys = {t[5:] for t in sp[4] if t.startswith('edit:')}
        if not keys:
            return False, 'no cited edit touches %s:%d' % (f, line), None, None, set(), None
        blk, _ = _region(rt, sp[0], sp[1])
        bblk, _ = _region(text, sp[2], sp[3])
        j = _find_block(B.lines_of(after_corpus.get(at_file, '')), blk, at_line)
        if j is None:
            return False, 'the replayed region of %s:%d is not the after text' % (f, line), None, None, keys, None
        why = complete_anchored(f, a, a + len(ls[line - 1]), blk)
        if why:
            return False, why, None, None, keys, None
        hb = B.lines_of(after_corpus.get(at_file, ''))[j:j + len(blk)]
        return True, '', '\n'.join(bblk), '\n'.join(blk), keys, '\n'.join(hb)

    def at_after(g, line):
        text = base_corpus.get(g, '')
        rt, spans, err = replay(text, [e for e in cited if g in e['files']])
        if err:
            return False, err, None, None, set(), None
        al = B.lines_of(after_corpus.get(g, ''))
        for sp in spans or []:
            if sp[1] <= sp[0]:
                continue
            blk, _ = _region(rt, sp[0], sp[1])
            j = _find_block(al, blk, line - 1)
            if j is not None:
                bblk, _ = _region(text, sp[2], sp[3]) if sp[3] > sp[2] else ([], 0)
                keys = {t[5:] for t in sp[4] if t.startswith('edit:')}
                if landed is not None:
                    rt2, sp2, err = replay(text, [e for e in landed if g in e['files']])
                    if err:
                        return False, 'replayed state: ' + err, None, None, keys, None
                    hit = [s2 for s2 in sp2 or [] if s2[1] > s2[0]
                           and _find_block(al, _region(rt2, s2[0], s2[1])[0], line - 1) is not None]
                    if not hit:
                        return False, 'the replayed state does not yield %s:%d' % (g, line), None, None, keys, None
                    k2 = {t[5:] for t in hit[0][4] if t.startswith('edit:')}
                    if k2 - ckeys:
                        return False, 'landed edits producing the line are not cited: %s' % ', '.join(
                            sorted(k2 - ckeys)), None, None, keys, None
                return True, '', '\n'.join(bblk), '\n'.join(blk), keys, '\n'.join(al[j:j + len(blk)])
        return False, 'no replayed new text yields %s:%d' % (g, line), None, None, set(), None

    kinds = item['kinds']
    if not cited:
        return False, ['no cited edit'], before, after, touch, None
    checks = []
    if 'unaccounted' in kinds:
        checks.append(at_after(item['file'], item['line']))
    elif 'deleted' in kinds:
        checks.append(anchored(item['file'], item['line'], item['file'], None))
    elif 'removed' in kinds:
        checks.append(anchored(item['file'], item['line'], item['file'], None))
    elif 'relocated' in kinds or 'relocated_from_main' in kinds:
        checks.append(anchored(item['file'], item['line'], item['file'], None))
        checks.append(at_after(item['new_file'], item['new_line']))
    else:
        checks.append(anchored(item['file'], item['line'], item['new_file'], item['new_line'] - 1))
    hafter = None
    for good, note, bt, at, keys, ht in checks:
        touch |= keys
        if not good:
            ok = False
            notes.append(note)
        else:
            before, after = (bt if bt is not None else before), (at if at is not None else after)
            hafter = ht if ht is not None else hafter
    return ok, notes, before, after, touch, hafter


def legacy_cover(item, cited, base_corpus, after_corpus, landed=None):
    """Mutant for the self-test only: the containment rule J1 of the earlier draft (old in before, new in
    after), which accepts partial coverage. C7 must fail when it replaces the replay rule."""
    b, a = norm(item['before'] or ''), norm(item['after'] or '')
    ok = any(norm(e['old']) and norm(e['old']) in b and norm(e['new']) in a for e in cited)
    return ok, [] if ok else ['legacy: not contained'], item['before'] or '', item['after'] or '', \
        {e['key'] for e in cited}, item['after']


# =========================================================================== J9, J10, flag

# Normalization (round-4 review c.7060670839): applied to every text J10 and the gain rule read.
PRE_NFKC = {'ℕ': '\\mathbb{N}', 'ℵ': '\\aleph', 'ℤ': '\\mathbb{Z}', 'ℝ': '\\mathbb{R}'}
ZERO_WIDTH = dict.fromkeys(map(ord, '\u00ad\u200b\u200c\u200d\u2060\ufeff\u180e'), None)
CONFUSABLES = str.maketrans({  # Cyrillic and Greek letters that render as ASCII letters
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x', 'і': 'i', 'ј': 'j', 'ѕ': 's',
    'ԁ': 'd', 'һ': 'h', 'ӏ': 'l', 'ɡ': 'g', 'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H',
    'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X', 'І': 'I', 'Ј': 'J', 'Ѕ': 'S',
    'ο': 'o', 'Ο': 'O', 'ι': 'i', 'Ι': 'I', 'Α': 'A', 'Β': 'B', 'Ε': 'E', 'Ζ': 'Z', 'Η': 'H', 'Κ': 'K',
    'Μ': 'M', 'Ν': 'N', 'Ρ': 'P', 'Τ': 'T', 'Υ': 'Y', 'Χ': 'X'})
FOOTNOTE_DEF = re.compile(r'^\[\^([^\]]+)\]:\s*(.*)$', re.M)
FOOTNOTE_REF = re.compile(r'\[\^([^\]]+)\](?!:)')


def normalize_text(t, file_text=None, collapse=True):
    """HTML entities decoded; ℕ-type symbols spelled out; NFKC; soft hyphens, zero-width characters and
    LaTeX discretionary hyphens removed; confusable letters folded to ASCII; footnote references
    expanded inline from the file's definitions (parenthetical content is already inline)."""
    t = html.unescape(t or '')
    for k, v in PRE_NFKC.items():
        t = t.replace(k, v)
    t = unicodedata.normalize('NFKC', t).translate(ZERO_WIDTH).replace('\\-', '').translate(CONFUSABLES)
    if file_text:
        defs = {m.group(1): m.group(2) for m in FOOTNOTE_DEF.finditer(file_text)}
        t = FOOTNOTE_REF.sub(lambda m: ' %s (%s) ' % (m.group(0), defs[m.group(1)]) if m.group(1) in defs
                             else m.group(0), t)
    return norm(t) if collapse else t


def strip_allowlisted(t, allow, collapse=True):
    """Remove each allowlisted phrase where it stands as a whole sentence: at the start or after a
    sentence or heading boundary, and followed by whitespace or the end. With collapse False the text's
    whitespace is otherwise kept exactly."""
    for ph in allow:
        ph = norm(ph)
        k = t.find(ph)
        while k >= 0:
            pre = t[:k].rstrip()
            post = t[k + len(ph):k + len(ph) + 1]
            if (not pre or pre[-1] in '.!?*:>') and (not post or post.isspace()):
                t = t[:k] + t[k + len(ph):]
            k = t.find(ph, k + 1)
    return norm(t) if collapse else t


TOKEN_RE = re.compile(r'[A-Za-z0-9]+|[^\sA-Za-z0-9]')


def tokens_of(t):
    return {x.lower() for x in TOKEN_RE.findall(t or '')}


def gain(before, after, cited_news, allow=None, before_file=None, after_file=None):
    """The token-level gain rule. Returns (added, unsourced): the tokens of the normalized after region,
    allowlisted sentences removed, that the before region lacks (these flag the item), and those that
    neither the before region nor the new text of a cited edit carries (these make the item non-J)."""
    allow = allowlist() if allow is None else allow
    a = tokens_of(strip_allowlisted(normalize_text(after, after_file), allow))
    b = tokens_of(strip_allowlisted(normalize_text(before, before_file), allow))
    src = set(b)
    for n in cited_news:
        src |= tokens_of(normalize_text(n, after_file))
    return sorted(a - b), sorted(a - src)


def token_seq(t, file_text=None, allow=None):
    """The normalized token sequence: ASCII words and every other non-space character, in order and with
    case kept; whitespace is not a token, so whitespace-only differences are not seen."""
    allow = allowlist() if allow is None else allow
    return TOKEN_RE.findall(strip_allowlisted(normalize_text(t, file_text), allow))


def exact_text(t, file_text=None, allow=None):
    """The exact comparison form: the same normalization, whitespace kept character for character."""
    allow = allowlist() if allow is None else allow
    return strip_allowlisted(normalize_text(t, file_text, collapse=False), allow, collapse=False)


def changed(before, after, before_file=None, after_file=None):
    """Layer 1, change flag (owner refinement): the exact normalized texts of the two regions differ,
    whitespace included."""
    return exact_text(before, before_file) != exact_text(after, after_file)


def seq_changed(before, after, before_file=None, after_file=None):
    """Diagnostic: the normalized token sequences differ (whitespace is not a token)."""
    return token_seq(before, before_file) != token_seq(after, after_file)


def set_changed(before, after, before_file=None, after_file=None):
    """Mutant for the self-test only: the earlier set comparison (tokens gained)."""
    return bool(gain(before, after, [], None, before_file, after_file)[0])


def allowlist(rows=None):
    """The exact allowlist: the two sentences of ALLOWLIST, nothing else."""
    return [a['phrase'] for a in ALLOWLIST]


def j10_hits(before, after, promotion=None, infinity=None, allow=None):
    """The vocabulary layer of J10: terms whose count rises from the before text to the after text, both
    normalized and with allowlisted whole sentences removed; and a fall in finite-scope terms."""
    allow = allowlist() if allow is None else allow
    b = strip_allowlisted(normalize_text(before), allow)
    a = strip_allowlisted(normalize_text(after), allow)
    hits = []
    for name, pats in (('promotion', PROMOTION_TERMS if promotion is None else promotion),
                       ('infinity', INFINITY_TERMS if infinity is None else infinity)):
        for p in pats:
            if len(re.findall(p, a, re.I)) > len(re.findall(p, b, re.I)):
                hits.append('%s %s' % (name, p))
    if len(FINITE_TERMS.findall(a)) < len(FINITE_TERMS.findall(b)):
        hits.append('finite-scope term lost')
    return hits


def j9(item, ledger_row, touch_edits, rows, before, after):
    """J9 for items whose kinds include label or text changed. Returns (ok, note)."""
    own = item.get('ledger_rows') or []
    ob, oa = len(OPEN_TERMS.findall(before)), len(OPEN_TERMS.findall(after))
    fb, fa = len(FINITE_TERMS.findall(before)), len(FINITE_TERMS.findall(after))
    if oa < ob:
        return False, 'an open, conditional or hypothesis term is lost'
    if not own:
        if 'label changed' in item['kinds']:
            return False, 'label change on an entry with no ledger row'
        if fa < fb:
            return False, 'a finite-scope term is lost'
        return True, ''
    if ledger_row not in own:
        return False, 'cited ledger row %s is not one of the entry\'s rows %s' % (ledger_row, own)
    if not any(ledger_row in (e.get('rows') or []) for e in touch_edits):
        return False, 'cited ledger row %s is not listed on a covering edit' % ledger_row
    disp = rows.get(ledger_row, {}).get('disposition')
    if disp == 'F' and not (fa >= 1 and fa >= fb):
        return False, 'F row: a finite-scope term is missing or lost'
    if disp == 'O' and not (oa >= 1 and oa >= ob):
        return False, 'O row: no open, conditional or hypothesis term after the change'
    if disp not in ('F', 'O', 'J'):
        return False, 'row %s has no accepted disposition' % ledger_row
    return True, ''


def sci_flag(item, before, after, j10):
    if set(item.get('categories') or []) & SCI_CATEGORIES:
        return True
    if 'value changed' in item['kinds'] or j10:
        return True
    if set(item.get('flags') or []) & {'numbers', 'marker'}:
        return True
    t = (before or '') + '\n' + (after or '')
    return bool(DEC_RE.search(t) or UNIT_AFTER_NUM.search(t) or POW10_RE.search(t) or B.PROSE_MARK_W.search(t))


RULES = {'cover': cover, 'j10': j10_hits, 'j9': j9, 'gain': gain, 'change': changed}


# =========================================================================== items and classification

def items_of(compare, after_corpus):
    snap = {e['id']: e for e in load_snapshot()['entries']}
    out = {}
    for r in compare['entries']:
        e = snap[r['id']]
        st = r['status']
        if st == ['unchanged'] and not r.get('relocated'):
            continue
        kinds = [] if st == ['unchanged'] else list(st)
        if r.get('relocated'):
            kinds.append('relocated_from_main' if r.get('relocated_from_main') else 'relocated')
        after = None
        if 'new_file' in r:
            after = B.lines_of(after_corpus[r['new_file']])[r['new_line'] - 1]
        out[r['id']] = {'kinds': kinds, 'file': e['file'], 'line': e['line'], 'new_file': r.get('new_file'),
                        'new_line': r.get('new_line'), 'before': e['text'], 'after': after,
                        'categories': e['categories'], 'ledger_rows': e.get('ledger_rows') or []}
    for u in compare['unaccounted']:
        out['U:%s:%d' % (u['file'], u['line'])] = {'kinds': ['unaccounted'], 'file': u['file'], 'line': u['line'],
                                                   'before': None, 'after': u['text'], 'flags': u['flags']}
    for d in compare['deleted']:
        out['D:%s:%d' % (d['file'], d['line'])] = {'kinds': ['deleted'], 'file': d['file'], 'line': d['line'],
                                                   'before': d['text'], 'after': None, 'flags': d['flags']}
    return out


def missing_items(landed, base_corpus, after_corpus):
    """Replay-missing items (adopted from 43122ff6, amendment A2): the landed edits are applied in
    order to the baseline giving the replayed state R. A line of R carrying reviewed new text (not a
    baseline line of its file) is an item when H lacks it and H's aligned lines there are all baseline
    lines, or there are none: the reviewed change is absent from H or reverted in it. A landed edit that
    does not apply is an item too. A difference whose H side is itself a change is already a reported
    item of the comparison and is not counted twice."""
    out, cur = {}, dict(base_corpus)
    for e in sorted(landed, key=lambda x: x['seq']):
        for f in e['files']:
            if cur.get(f, '').count(e['old']) != 1:
                out['RM:edit:%s:%s' % (e['key'], f)] = {'kinds': ['replay-missing'], 'file': f, 'line': None,
                                                         'before': e['old'], 'after': None, 'replayed': e['new']}
                continue
            cur[f] = cur[f].replace(e['old'], e['new'])
    for f in sorted(cur):
        if cur[f] == base_corpus.get(f):
            continue
        rl = [norm(x) for x in B.lines_of(cur[f])]
        hl = [norm(x) for x in B.lines_of(after_corpus.get(f, ''))]
        bset = {norm(x) for x in B.lines_of(base_corpus.get(f, ''))}
        sm = difflib.SequenceMatcher(None, rl, hl, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal' or not all(x in bset for x in hl[j1:j2]):
                continue
            for i in range(i1, i2):
                if rl[i] and rl[i] not in bset:
                    out['RM:%s:%d' % (f, i + 1)] = {'kinds': ['replay-missing'], 'file': f, 'line': i + 1,
                                                    'before': None, 'after': None,
                                                    'replayed': B.lines_of(cur[f])[i]}
    return out


REVIEW_URL = re.compile(r'^%s/pull/(\d+)#(?:issuecomment-|pullrequestreview-|discussion_r)\d+$' % re.escape(REPO_URL))


def resolution_ok(resn, cls, needs_proof):
    if not resn or resn.get('outcome') not in ('justified', 'unjustified'):
        return False, 'no resolution'
    m = REVIEW_URL.match(resn.get('review') or '')
    if not m or int(m.group(1)) != cls.get('result_pr'):
        return False, 'resolution review is not a comment URL on the result PR'
    who = (resn.get('reviewer') or '').strip().casefold()
    if not who or who == (cls.get('classifier') or '').strip().casefold():
        return False, 'resolution reviewer is missing or is the classifier'
    if needs_proof and resn.get('outcome') == 'justified' and not (resn.get('proof') or '').strip():
        return False, 'J10 item resolved without citing the proof that covers the generality'
    return True, ''


def classify(compare, edits, cls, rows, base_corpus, after_corpus, rules=RULES, landed=None):
    E = {e['key']: e for e in edits['edits']}
    res = {}
    allitems = items_of(compare, after_corpus)
    for key, item in sorted(missing_items(landed or [], base_corpus, after_corpus).items()):
        c = cls.get('items', {}).get(key)
        klass, notes = 'U', ['a landed reviewed change is absent from H']
        if c is not None and c.get('class') == 'R':
            klass = 'R'
            good, why = resolution_ok(c.get('resolution'), cls, False)
            if good:
                klass = 'R-justified' if c['resolution']['outcome'] == 'justified' else 'U'
                notes.append('resolved by review %s' % c['resolution']['review'])
            elif c.get('resolution'):
                notes.append('resolution not accepted: ' + why)
        j10m = rules['j10'](item['before'] or '', item['replayed'])
        added, _ = rules['gain'](item['before'] or '', item['replayed'], [])
        res[key] = {'kinds': item['kinds'], 'class': klass, 'j10': j10m, 'notes': notes, 'gain_added': added[:20],
                    'scientific_evaluation': True}
    for key, item in sorted(allitems.items()):
        c = cls.get('items', {}).get(key)
        notes, klass, j10, unsourced, seq_diff, inexact = [], 'U', [], [], False, False
        before, after = item['before'] or '', item['after'] or ''
        bf = base_corpus.get(item['file'])
        af = after_corpus.get(item.get('new_file') or item['file'])
        if c is None:
            notes.append('unclassified')
            j10 = rules['j10'](before, after)
            if j10:
                notes.append('J10: ' + '; '.join(j10))
            added, _ = rules['gain'](before, after, [], None, bf, af)
            seq_diff = rules['change'](before, after, bf, af)
        else:
            missing = [k for k in c.get('edits', []) if k not in E]
            if missing:
                notes.append('cited edits not in the compiled lists: %s' % ', '.join(missing))
            cited = [E[k] for k in c.get('edits', []) if k in E]
            covered, cn, before, after, touch, hafter = rules['cover'](item, cited, base_corpus, after_corpus,
                                                                       landed)
            notes += cn
            j10 = rules['j10'](before, after)
            for k in sorted(touch):  # the vocabulary layer on the approved edits' own texts
                if k in E:
                    j10 += ['approved edit %s: %s' % (k, h) for h in rules['j10'](E[k]['old'], E[k]['new'])]
            added, unsourced = rules['gain'](before, after, [e['new'] for e in cited], None, bf, af)
            seq_diff = rules['change'](before, after, bf, af)
            if seq_diff:
                notes.append('changed: %s' % ('token sequence' if seq_changed(before, after, bf, af)
                                              else 'whitespace only'))
            if covered and hafter is not None and exact_text(hafter, af, []) != exact_text(after, af, []):
                why = ('token sequence differs' if token_seq(hafter, af, []) != token_seq(after, af, [])
                       else 'whitespace only')
                notes.append('not exact: H differs from the replayed expected text (%s)' % why)
                inexact = True
            if unsourced:
                notes.append('gain rule: tokens in neither the baseline region nor a cited new text: %s'
                             % ' '.join(unsourced[:20]))
            j9_ok = True
            if covered and set(item['kinds']) & {'label changed', 'text changed'}:
                j9_ok, n9 = rules['j9'](item, c.get('ledger_row'), [E[k] for k in touch if k in E], rows,
                                        before, after)
                if not j9_ok:
                    notes.append('J9: ' + n9)
            if j10:
                notes.append('J10: ' + '; '.join(j10))
            to_r = 'relocated_from_main' in item['kinds']
            if to_r:
                notes.append('relocation out of Main: review of Main independence required')
            if c.get('class') == 'J' and covered and j9_ok and not j10 and not unsourced and not inexact and not to_r:
                klass = 'J'
            elif c.get('class') in ('J', 'R') and covered:
                klass = 'R'
            elif c.get('class') == 'R':
                klass = 'R'
                notes.append('no covering edit; R requires review')
            if klass == 'R':
                good, why = resolution_ok(c.get('resolution'), cls, bool(j10 or unsourced or inexact))
                if good:
                    klass = 'R-justified' if c['resolution']['outcome'] == 'justified' else 'U'
                    notes.append('resolved by review %s' % c['resolution']['review'])
                elif c.get('resolution'):
                    notes.append('resolution not accepted: ' + why)
        res[key] = {'kinds': item['kinds'], 'class': klass, 'j10': j10, 'notes': notes,
                    'gain_added': added[:20], 'gain_unsourced': unsourced[:20],
                    'scientific_evaluation': sci_flag(item, before, after, j10) or seq_diff or bool(unsourced) or inexact,
                    'exact': not inexact}
    return res


def counts_of(res):
    c = {'items': len(res), 'J': 0, 'R-justified': 0, 'R-unresolved': 0, 'U': 0, 'scientific_evaluation': 0}
    for v in res.values():
        c['R-unresolved' if v['class'] == 'R' else v['class']] += 1
        c['scientific_evaluation'] += 1 if v['scientific_evaluation'] else 0
    return c


def verdict_of(counts, controls_ok, cc_ok, prep=False, flagged_edits=0):
    if not controls_ok or not cc_ok:
        v = 'VOID'
    elif counts['U'] > 0:
        v = 'FAIL'
    elif counts['R-unresolved'] > 0:
        v = 'PENDING'
    else:
        v = 'PASS'
    text = ('VERDICT %s: %d reported changes; J %d, R resolved as justified %d, R unresolved %d, U %d; '
            '%d flagged for scientific evaluation; controls %s; countercontrols %s.'
            % (v, counts['items'], counts['J'], counts['R-justified'], counts['R-unresolved'], counts['U'],
               counts['scientific_evaluation'], 'pass' if controls_ok else 'FAIL', 'pass' if cc_ok else 'FAIL'))
    text += (' Owner requirement 6 is settled only by the separate scientific evaluation; scientific evaluation '
             'is open for %d items and %d landed edits.' % (counts['scientific_evaluation'], flagged_edits))
    if prep:
        text = 'PREPARATION RUN at the pin, not a regression verdict. ' + text
    return v, text


def load_snapshot():
    with open(os.path.join(RECORD, 'snapshot.json'), encoding='utf-8') as fh:
        return json.load(fh)


def load_rows():
    return {r['id']: r for r in json.loads(show(PIN_S2, LEDGER_ROWS))['rows']}


# =========================================================================== countercontrols C7-C9

def _num_outside(line, news):
    spans = []
    for n in news:
        for seg in [s for s in n.split('\n') if s]:
            k = line.find(seg)
            while k >= 0:
                spans.append((k, k + len(seg)))
                k = line.find(seg, k + 1)
    for m in B.NUM_RE.finditer(line):
        if not any(a <= m.start() and m.end() <= b for a, b in spans):
            return m
    return None


def _after_loc(item):
    if 'unaccounted' in item['kinds']:
        return item['file'], item['line']
    if item.get('new_file') and not set(item['kinds']) & {'relocated', 'relocated_from_main'}:
        return item['new_file'], item['new_line']
    return None


def _setline(corpus, f, ln, t):
    c = dict(corpus)
    ls = B.lines_of(c[f])
    ls[ln - 1] = t
    c[f] = '\n'.join(ls)
    return c


def _c8_try(pick, items, edits, cls, rows, base, after, rules, landed, snap):
    f, ln = _after_loc(items[pick])
    line = B.lines_of(after[f])[ln - 1]
    c = cls['items'][pick]
    E = {e['key']: e for e in edits['edits']}
    ce = E[c['edits'][0]]
    syn = {'key': 'C8:X', 'unit': ce['unit'], 'pr': ce['pr'], 'id': 'X', 'seq': 10 ** 9, 'files': [f],
           'old': line, 'new': line + J10_SENTENCE,
           'rows': sorted(set(ce['rows']) | ({c['ledger_row']} if c.get('ledger_row') else set())),
           'components': []}
    e8 = copy.deepcopy(edits)
    e8['edits'].append(syn)
    cls8 = copy.deepcopy(cls)
    cls8['items'][pick]['edits'] = list(c['edits']) + ['C8:X']
    l8 = landed + [syn] if landed is not None else None
    a8 = _setline(after, f, ln, line + J10_SENTENCE)
    cm8 = B.compare(snap, a8)
    pre = classify(cm8, e8, cls8, rows, base, a8, dict(rules, j10=lambda b, a: []), l8).get(pick, {})
    got = classify(cm8, e8, cls8, rows, base, a8, rules, l8).get(pick, {})
    return pre.get('class'), got


def countercontrols(compare, res, edits, cls, rows, base, after, rules=RULES, synthetic=None, landed=None):
    """C7 (bad citation) on the first J item with an after line, or on T3's synthetic item when the main
    run has none. C8 (J10 isolated) on the first J item whose C8 copy is J with J10 disabled (its
    precondition), or on C9 (b)'s item when no main-run item meets it. Returns {name: {pass, detail}}."""
    snap = load_snapshot()
    items = items_of(compare, after)
    js = [k for k in sorted(res) if res[k]['class'] == 'J' and k in items and _after_loc(items[k])]
    out = {}
    # C7
    if js:
        pick, src, cm7, ed7, cl7, af7, l7, r0 = js[0], 'main run', compare, edits, cls, after, landed, res
    else:
        cm7, ed7, cl7, af7, pick = synthetic or synthetic_case()
        src, l7 = 'synthetic item (no J item in the main run)', None
        r0 = classify(cm7, ed7, cl7, rows, base, af7, rules)
    if r0.get(pick, {}).get('class') != 'J':
        out['C7'] = {'pass': False, 'detail': 'C7 item not J'}
    else:
        it7 = items_of(cm7, af7)
        f, ln = _after_loc(it7[pick])
        line = B.lines_of(af7[f])[ln - 1]
        E = {e['key']: e for e in ed7['edits']}
        m = _num_outside(line, [E[k]['new'] for k in cl7['items'][pick]['edits'] if k in E])
        line7 = line[:m.end() - 1] + str((int(m.group(0)[-1]) + 1) % 10) + line[m.end():] if m else line + ' 0'
        a7 = _setline(af7, f, ln, line7)
        r7 = classify(B.compare(snap, a7), ed7, cl7, rows, base, a7, rules, l7)
        k7 = pick if pick in r7 else 'U:%s:%d' % (f, ln)
        out['C7'] = {'pass': r7.get(k7, {}).get('class') == 'U' and counts_of(r7)['U'] == counts_of(r0)['U'] + 1,
                     'detail': '%s %s: %s -> %s' % (src, pick, 'token' if m else 'appended', r7.get(k7, {}).get('class'))}
    # C8
    done = None
    for k in js[:5]:
        pre, got = _c8_try(k, items, edits, cls, rows, base, after, rules, landed, snap)
        if pre == 'J':
            done = ('main run', k, pre, got)
            break
    if done is None:
        cm, ed, cl, af, eid = c9_cases(rows)['b']
        pre, got = _c8_try(eid, items_of(cm, af), ed, cl, rows, base, af, rules, None, snap)
        done = ('C9 (b) item (no main-run item meets the precondition)', eid, pre, got)
    src, k, pre, got = done
    out['C8'] = {'pass': pre == 'J' and got.get('class') == 'R' and bool(got.get('j10'))
                 and bool(got.get('scientific_evaluation')),
                 'detail': '%s %s: with J10 off %s, with J10 %s' % (src, k, pre, got.get('class'))}
    return out


def synthetic_case():
    """T3's item: appA:85's value 2.361 -> 2.362, covered by a synthetic S2-E edit, classified J."""
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    e85 = next(e for e in snap['entries'] if e['id'] == 'appA:85')
    after = _setline(pin, e85['file'], e85['line'], e85['text'].replace('2.361', '2.362', 1))
    ed = {'schema': 'a1exit-compare-edits/2', 'edits': [
        {'key': 'S2-E:T3', 'unit': 'S2-E', 'pr': 1475, 'id': 'T3', 'seq': 1, 'files': [e85['file']],
         'old': '$4.28/Z_S(\\lambda g_0^2) = 2.361$', 'new': '$4.28/Z_S(\\lambda g_0^2) = 2.362$',
         'rows': [], 'components': []}]}
    cj = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic', 'classifier': 'writer', 'result_pr': 1,
          'items': {'appA:85': {'class': 'J', 'edits': ['S2-E:T3'], 'ledger_row': None, 'reason': 'synthetic',
                                'resolution': None}}}
    return B.compare(snap, after), ed, cj, after, 'appA:85'


def edit_case(eid, old, new, row, tag):
    """A synthetic case on the pinned corpus: entry eid's text with old replaced by new, cited J to one
    edit carrying exactly that replacement and listing row."""
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    e = next(x for x in snap['entries'] if x['id'] == eid)
    if e['text'].count(old) != 1 or pin[e['file']].count(old) != 1:
        raise CompileError('case %s: old string not unique' % tag)
    after = _setline(pin, e['file'], e['line'], e['text'].replace(old, new, 1))
    key = 'S2-E:%s' % tag
    ed = {'schema': 'a1exit-compare-edits/2', 'edits': [
        {'key': key, 'unit': 'S2-E', 'pr': 1475, 'id': tag, 'seq': 1, 'files': [e['file']], 'old': old,
         'new': new, 'rows': [row] if row else [], 'components': []}]}
    cl = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic', 'classifier': 'writer', 'result_pr': 1,
          'items': {eid: {'class': 'J', 'edits': [key], 'ledger_row': row, 'reason': 'synthetic',
                          'resolution': None}}}
    return B.compare(snap, after), ed, cl, after, eid


GR134_END = 'takes the same value on all its members. $\\square$'


def gr134(insert):
    return edit_case('GR:134', GR134_END, GR134_END.replace('members.', 'members' + insert + '.'), 'X-52', 'GR')


_C9_CACHE = {}


def c9_cases(rows=None):
    """The cases of the decisive control C9, on the pinned corpus:
    (a) ch01:179's "Without A1," rewritten as "For every infinite system," (row X-26);
    (b) GR:134 (row X-52, disposition J) gains the owner's configuration-space sentence, as allowlisted;
    (c) GR:134 gains ", for arbitrary $S$"; (d) GR:134 gains ", and this is proved";
    (e) a J-row entry loses its one open, conditional or hypothesis term;
    (f) appB:42 (row X-15, disposition J) loses "finite" from "a finite configuration space".
    Each is cited J to an edit that reproduces it exactly and lists the row."""
    if 'cases' in _C9_CACHE:
        return copy.deepcopy(_C9_CACHE['cases'])
    rows = rows or load_rows()
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    cases = {'a': edit_case('ch01:179', 'Without A1, the near-return condition',
                            'For every infinite system, the near-return condition', 'X-26', 'C9a'),
             'b': edit_case('GR:134', GR134_END, GR134_END.replace('$\\square$', ALLOWLIST[1]['phrase'] + ' $\\square$'),
                            'X-52', 'C9b'),
             'c': gr134(', for arbitrary $S$'), 'd': gr134(', and this is proved')}
    e5 = next(e for e in snap['entries'] if e['kind'] == 'prose' and e['file'] != FULL
              and any(rows.get(r, {}).get('disposition') == 'J' for r in e['ledger_rows'])
              and len(OPEN_TERMS.findall(e['text'])) == 1 and pin[e['file']].count(e['text']) == 1)
    w = OPEN_TERMS.search(e5['text'])
    seg = e5['text'][max(0, w.start() - 30):w.end() + 10]
    r5 = next(r for r in e5['ledger_rows'] if rows.get(r, {}).get('disposition') == 'J')
    cases['e'] = edit_case(e5['id'], seg, seg.replace(w.group(0), 'stated', 1), r5, 'C9e')
    cases['g'] = edit_case('appB:194', 'a function of finitely many components', 'a function of components',
                           'X-52', 'C9g')
    cases['f'] = edit_case('appB:42', 'one-step doubly stochastic matrix on a finite configuration space',
                           'one-step doubly stochastic matrix on a configuration space', 'X-15', 'C9f')
    _C9_CACHE['cases'] = copy.deepcopy(cases)
    return cases


def evasion_battery(rows, rules=RULES, only=None):
    """The standing J10 battery on GR:134 (row X-52, disposition J), each insertion cited J to an edit
    that reproduces it: the 16 paraphrases, the 28 evasions, the allowlisted sentence followed by an
    unlisted claim, and the gain-only case. Each must be flagged. Returns the cases that are not."""
    base = dict(B.PIN_CORPUS())
    cases = (['p:' + x for x in PARAPHRASES] + ['e:' + x for x in EVASIONS]
             + ['a:' + x for x in ALLOW_PLUS] + ['g:' + GAIN_ONLY])
    bad = []
    for c in cases:
        if only is not None and c not in only:
            continue
        kind, x = c[:1], c[2:]
        ins = ', ' + x if kind == 'p' else ('. ' + ALLOWLIST[1]['phrase'] + ' ' + x if kind == 'a' else x)
        cm, ed, cl, af, eid = gr134(ins)
        r = classify(cm, ed, cl, rows, base, af, rules).get(eid, {})
        if not r.get('scientific_evaluation'):
            bad.append((c, r.get('class')))
    return bad


def n_battery(rows, rules=RULES, only=None):
    """The standing sequence battery: every case of NCASES must be flagged. Returns those that are not."""
    base = dict(B.PIN_CORPUS())
    bad = []
    for eid, old, new, row, tag in NCASES:
        if only is not None and tag not in only:
            continue
        cm, ed, cl, af, e = edit_case(eid, old, new, row, tag)
        r = classify(cm, ed, cl, rows, base, af, rules).get(e, {})
        if not r.get('scientific_evaluation'):
            bad.append((tag, r.get('class')))
    return bad


def c9(rows, rules=RULES):
    """C9 passes iff (a) is R, flagged, J10-hit, and stays R under a review that cites no proof; (b) is J;
    (c), (d), (f) and (g) are R, flagged and J10-hit; (e) is R."""
    base = dict(B.PIN_CORPUS())
    got = {}
    for k, (cm, ed, cl, af, eid) in sorted(c9_cases(rows).items()):
        got[k] = classify(cm, ed, cl, rows, base, af, rules).get(eid, {})
        if k == 'a':
            cl2 = copy.deepcopy(cl)
            cl2['items'][eid]['resolution'] = {'outcome': 'justified', 'review': REPO_URL + '/pull/1#issuecomment-1',
                                               'reviewer': 'someone-else', 'proof': None}
            got['a2'] = classify(cm, ed, cl2, rows, base, af, rules).get(eid, {})

    def flagged_r(x):
        return x.get('class') == 'R' and bool(x.get('j10')) and x.get('scientific_evaluation')
    ok = (flagged_r(got['a']) and got['a2'].get('class') == 'R' and got['b'].get('class') == 'J'
          and flagged_r(got['c']) and flagged_r(got['d']) and got['e'].get('class') == 'R' and flagged_r(got['f'])
          and flagged_r(got['g']))
    return {'pass': bool(ok), 'detail': '; '.join('(%s) %s' % (k, got[k].get('class')) for k in sorted(got))}


# =========================================================================== collect

def pick_injection(compare, corpus):
    """The first C-TAB prediction-table entry reported unchanged, with a decimal token."""
    by_id = {e['id']: e for e in load_snapshot()['entries']}
    for r in compare['entries']:
        e = by_id[r['id']]
        if r['status'] != ['unchanged'] or e['kind'] != 'table' or e['table']['class'] != 'prediction':
            continue
        f, ln = r['new_file'], r['new_line']
        text = B.lines_of(corpus[f])[ln - 1]
        toks = {n['tok'] for c in e['cells'] for n in c['numbers']}
        m = next((m for m in B.PROSE_DEC_RE.finditer(text) if m.group(0) in toks), None)
        if m:
            new_tok = m.group(0)[:-1] + str((int(text[m.end() - 1]) + 1) % 10)
            return {'key': r['id'], 'file': f, 'line': ln, 'old_token': m.group(0), 'new_token': new_tok,
                    'span': [m.start(), m.end()]}
    return None


def injected(corpus, inj):
    ls = B.lines_of(corpus[inj['file']])
    a, b = inj['span']
    t = ls[inj['line'] - 1]
    return _setline(corpus, inj['file'], inj['line'], t[:a] + inj['new_token'] + t[b:])


def _result_ok(path, other, pin_expected=True):
    if not os.path.isfile(path):
        return None, 'not written by this run'
    try:
        r = read_json(path)
    except ValueError:
        return None, 'not JSON'
    if r.get('schema') != B.COMPARE_SCHEMA or r.get('pin') != B.PIN or (other and r.get('other') != other):
        return None, 'schema %s, pin %s, other %s' % (r.get('schema'), r.get('pin'), r.get('other'))
    return r, ''


def collect(head, out, frozen_ref, del_commit, prep=False):
    if os.path.exists(out) and os.listdir(out):
        print('collect: refused, %s is not empty' % out)
        return 2
    os.makedirs(out, exist_ok=True)
    H = resolve(head)
    py = [sys.executable, '-I', '-B', os.path.join(RECORD, 'baseline.py')]
    ctl = {}

    def put(name, code, good, detail=''):
        ctl[name] = {'exit': code, 'pass': bool(good), 'detail': detail}
    put('H-resolves', 0 if H else 1, bool(H), H or 'does not resolve: %s' % head)
    if prep and H != B.PIN:
        put('preparation-only-at-pin', 1, False, 'a preparation run is allowed only with the pin as head')
    ok0, d0 = c0(frozen_ref, prep)
    put('C0-frozen', 0 if ok0 else 1, ok0, d0)
    code = run([sys.executable, '-I', '-B', os.path.abspath(__file__), 'self-test'])
    put('C4-verdict-self-test', code, code == 0)
    code = run(py + ['check'])
    put('C1-check', code, code == 0)
    code = run(py + ['self-test'])
    put('C2-self-test', code, code == 0)
    p3 = os.path.join(out, 'self-compare.json')
    code = run(py + ['--compare', B.PIN, '--json', p3])
    r3, why = _result_ok(p3, B.PIN)
    put('C3-self-compare', code, code == 0 and r3 is not None and not r3['any_change'], why)
    inj, files = None, {}
    if H:
        p = os.path.join(out, 'compare.json')
        code = run(py + ['--compare', H, '--json', p])
        r, why = _result_ok(p, H)
        put('compare', code, r is not None and code == (1 if r['any_change'] else 0), why)
        if r is not None:
            corpus = B.corpus_at_commit(H)
            inj = pick_injection(r, corpus)
            tmp = tempfile.mkdtemp(prefix='a1exit-cc-')
            try:
                cc = injected(corpus, inj) if inj else corpus
                for f, text in cc.items():
                    os.makedirs(os.path.join(tmp, os.path.dirname(f)), exist_ok=True)
                    with open(os.path.join(tmp, f), 'w', encoding='utf-8', newline='') as fh:
                        fh.write(text)
                pi = os.path.join(out, 'injected-compare.json')
                code = run(py + ['--compare-tree', tmp, '--json', pi])
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
            ri, why = _result_ok(pi, None)
            st = next((x['status'] for x in ri['entries'] if inj and x['id'] == inj['key']), []) if ri else []
            put('C5-injected', code, bool(inj) and ri is not None and code == 1 and ri['any_change']
                and 'value changed' in st, why or 'injected %s -> %s' % (inj and inj['key'], st))
    dc = None
    if del_commit:
        dc = resolve(del_commit)
        try:
            write_json(os.path.join(out, 'edits-del.json'), compile_del(dc))
            put('deletion-list-compiled', 0, True, dc)
        except (subprocess.CalledProcessError, KeyError, ValueError, TypeError) as ex:
            put('deletion-list-compiled', 1, False, str(ex))
    for n in sorted(os.listdir(out)):
        if n.endswith('.json'):
            files[n] = sha256_file(os.path.join(out, n))
    del_sha = sha256_bytes(B.git('show', '%s:%s' % (dc, DEL_EDITS))) if dc and ctl.get('deletion-list-compiled', {}).get('pass') else None
    rec = {'schema': 'a1exit-compare-controls/2', 'head': H, 'frozen_ref': resolve(frozen_ref) if frozen_ref else None,
           'del_commit': dc, 'del_edits_sha256': del_sha, 'preparation': bool(prep), 'controls': ctl,
           'injection': inj, 'files': files}
    write_json(os.path.join(out, 'controls.json'), rec)
    print(json.dumps({k: v['pass'] for k, v in ctl.items()}, sort_keys=True))
    return 0 if all(c['pass'] for c in ctl.values()) else 4


# =========================================================================== verdict

CONTROL_EXIT = {'H-resolves': (0,), 'C0-frozen': (0,), 'C1-check': (0,), 'C2-self-test': (0,),
                'C3-self-compare': (0,), 'C4-verdict-self-test': (0,), 'compare': (0, 1), 'C5-injected': (1,),
                'deletion-list-compiled': (0,), 'preparation-only-at-pin': ()}
REQUIRED_CONTROLS = ['H-resolves', 'C0-frozen', 'C1-check', 'C2-self-test', 'C3-self-compare',
                     'C4-verdict-self-test', 'compare', 'C5-injected']


def rederive_compare(path, H, inj=None):
    """N2: re-run the comparison from the frozen inputs (for C5, on H's corpus with the recorded
    injection) and require the stored file to equal it as canonical JSON (`other` aside for a tree)."""
    if not os.path.isfile(path):
        return False, 'missing'
    py = [sys.executable, '-I', '-B', os.path.join(RECORD, 'baseline.py')]
    td = tempfile.mkdtemp(prefix='a1exit-rd-')
    try:
        out = os.path.join(td, 'r.json')
        if inj is None:
            run(py + ['--compare', H, '--json', out])
        else:
            tree = os.path.join(td, 'tree')
            for f, text in injected(B.corpus_at_commit(H), inj).items():
                os.makedirs(os.path.join(tree, os.path.dirname(f)), exist_ok=True)
                with open(os.path.join(tree, f), 'w', encoding='utf-8', newline='') as fh:
                    fh.write(text)
            run(py + ['--compare-tree', tree, '--json', out])
        if not os.path.isfile(out):
            return False, 're-derivation wrote nothing'
        a, b = read_json(path), read_json(out)
        if inj is not None:
            a.pop('other', None)
            b.pop('other', None)
        same = json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
        return same, '' if same else 'the stored file differs from its re-derivation'
    finally:
        shutil.rmtree(td, ignore_errors=True)


def recheck_controls(ctl, d, H):
    """No stored pass flag is trusted (§A.44). A stored entry whose pass contradicts its exit status is a
    refusal. Every control is then re-derived: C1, C2, C3 and C4 are re-run, and the comparison and C5
    outputs are re-checked from their files."""
    for n, c in ctl.get('controls', {}).items():
        if n not in CONTROL_EXIT or c.get('pass') is not (c.get('exit') in CONTROL_EXIT[n]):
            return None, 'controls.json entry %s: pass %r contradicts exit %r' % (n, c.get('pass'), c.get('exit'))
    out = {}
    py = [sys.executable, '-I', '-B', os.path.join(RECORD, 'baseline.py')]
    for n, argv in (('C1-check', py + ['check']), ('C2-self-test', py + ['self-test']),
                    ('C4-verdict-self-test', [sys.executable, '-I', '-B', os.path.abspath(__file__), 'self-test'])):
        code = run(argv)
        out[n] = {'exit': code, 'pass': code == 0 and ctl['controls'].get(n, {}).get('exit') == 0, 'detail': 're-run'}
    td = tempfile.mkdtemp(prefix='a1exit-c3-')
    try:
        p3 = os.path.join(td, 'self-compare.json')
        code = run(py + ['--compare', B.PIN, '--json', p3])
        r3, why = _result_ok(p3, B.PIN)
        out['C3-self-compare'] = {'exit': code, 'pass': code == 0 and r3 is not None and not r3['any_change'],
                                  'detail': 're-run ' + why}
    finally:
        shutil.rmtree(td, ignore_errors=True)
    r, why = _result_ok(os.path.join(d, 'compare.json'), H)
    ce = ctl['controls'].get('compare', {}).get('exit')
    same, why2 = rederive_compare(os.path.join(d, 'compare.json'), H)
    out['compare'] = {'exit': ce, 'pass': r is not None and ce == (1 if r['any_change'] else 0) and same,
                      'detail': 're-checked and re-derived ' + why + why2}
    ri, why = _result_ok(os.path.join(d, 'injected-compare.json'), None)
    inj = ctl.get('injection')
    st = next((x['status'] for x in ri['entries'] if inj and x['id'] == inj['key']), []) if ri else []
    isame, iwhy = rederive_compare(os.path.join(d, 'injected-compare.json'), H, inj) if inj else (False, 'no injection')
    out['C5-injected'] = {'exit': ctl['controls'].get('C5-injected', {}).get('exit'),
                          'pass': bool(inj) and ri is not None and ri['any_change'] and 'value changed' in st
                          and ctl['controls'].get('C5-injected', {}).get('exit') == 1 and isame,
                          'detail': 're-checked and re-derived ' + iwhy}
    out['H-resolves'] = {'exit': 0 if resolve(H) == H else 1, 'pass': resolve(H) == H, 'detail': 're-checked'}
    for n in REQUIRED_CONTROLS:
        if n not in ctl['controls']:
            out[n] = {'exit': None, 'pass': False, 'detail': 'missing from controls.json'}
    if ctl.get('del_commit'):
        dc = ctl['controls'].get('deletion-list-compiled', {})
        out['deletion-list-compiled'] = {'exit': dc.get('exit'), 'pass': dc.get('exit') == 0, 'detail': 're-checked by C6'}
    if 'preparation-only-at-pin' in ctl['controls']:
        out['preparation-only-at-pin'] = {'exit': 1, 'pass': False, 'detail': 'preparation run not at the pin'}
    return out, ''


def verdict(d, cls_path):
    vpath = os.path.join(d, 'verdict.json')
    if os.path.exists(vpath):
        print('verdict: refused, %s exists' % vpath)
        return 2
    ctl = read_json(os.path.join(d, 'controls.json'))
    cls = read_json(cls_path)
    H = ctl.get('head')
    prep = bool(ctl.get('preparation'))
    refuse = []
    for n, sha in sorted(ctl.get('files', {}).items()):
        if not os.path.isfile(os.path.join(d, n)) or sha256_file(os.path.join(d, n)) != sha:
            refuse.append('%s is not the file collect wrote' % n)
    compare = read_json(os.path.join(d, 'compare.json')) if os.path.isfile(os.path.join(d, 'compare.json')) else {}
    if not H or compare.get('other') != H or cls.get('head') != H or resolve(H) != H:
        refuse.append('heads differ: controls %s, compare %s, classify %s' % (H, compare.get('other'), cls.get('head')))
    if cls.get('schema') != 'a1exit-compare-classify/2' or not cls.get('classifier') or not cls.get('result_pr'):
        refuse.append('classify.json lacks schema, classifier or result_pr')
    if prep and H != B.PIN:
        refuse.append('a preparation run is allowed only with the pin as head')
    controls, why = recheck_controls(ctl, d, H) if not refuse else (None, '')
    if why:
        refuse.append(why)
    if refuse:
        print('verdict: refused: ' + '; '.join(refuse))
        return 2
    ok0, d0 = c0(ctl.get('frozen_ref'), prep)
    edits_s2 = read_json(EDITS_S2)
    dpath = os.path.join(d, 'edits-del.json')
    edits_del = read_json(dpath) if ctl.get('del_commit') and os.path.isfile(dpath) else None
    ok6, bad6, note6 = c6(edits_s2, edits_del, ctl.get('del_commit'), H)
    if edits_del is not None:
        blob = git_try('show', '%s:%s' % (ctl['del_commit'], DEL_EDITS))
        if blob is None or sha256_bytes(blob) != ctl.get('del_edits_sha256'):
            ok6, bad6 = False, bad6 + ['(d) the landed edits.json digest differs from the one collect recorded']
    controls['C0-frozen-at-verdict'] = {'exit': 0 if ok0 else 1, 'pass': ok0, 'detail': d0}
    controls['C6-edit-inputs'] = {'exit': 0 if ok6 else 1, 'pass': ok6, 'detail': '; '.join(bad6[:20]) or note6}
    controls_ok = all(c['pass'] for c in controls.values())
    inputs = {n: sha256_file(os.path.join(d, n)) for n in sorted(os.listdir(d)) if n.endswith('.json')}
    inputs['classify'] = sha256_file(cls_path)
    inputs.update({'frozen:' + k: v2 for k, v2 in digests().items()})
    base_out = {'schema': 'a1exit-compare-verdict/2', 'head': H, 'preparation': prep, 'controls': controls,
                'inputs': inputs, 'requirement6_settled': False}
    if not controls_ok:
        # review c.7059580868 finding 3: nothing is classified over failed controls
        counts = {'items': 0, 'J': 0, 'R-justified': 0, 'R-unresolved': 0, 'U': 0, 'scientific_evaluation': 0}
        v, text = verdict_of(counts, False, False, prep)
        text = text.replace('VERDICT VOID: 0 reported changes', 'VERDICT VOID: not classified, a control failed') \
            .replace('countercontrols FAIL', 'countercontrols not run')
        write_json(vpath, dict(base_out, verdict=v, counts=None, items=None, countercontrols=None, text=text))
        print(text)
        return EXIT[v]
    edits = {'edits': edits_s2['edits'] + (edits_del['edits'] if edits_del else [])}
    rows = load_rows()
    base = dict(B.PIN_CORPUS())
    after = B.corpus_at_commit(H)
    landed = [e for e in edits_s2['edits']
              if git_try('merge-base', '--is-ancestor', edits_s2['units'][e['unit']]['merge'], H) is not None]
    landed += edits_del['edits'] if edits_del else []
    flagged_edits = sorted(e['key'] for e in landed if j10_hits(e['old'], e['new']))
    res = classify(compare, edits, cls, rows, base, after, landed=landed)
    counts = counts_of(res)
    inj_c = read_json(os.path.join(d, 'injected-compare.json'))
    inj = ctl.get('injection')
    ires = classify(inj_c, edits, cls, rows, base, injected(after, inj), landed=landed) if inj else {}
    c5 = bool(inj) and ires.get(inj['key'], {}).get('class') == 'U' and counts_of(ires)['U'] == counts['U'] + 1
    cc = countercontrols(compare, res, edits, cls, rows, base, after, landed=landed)
    cc['C5'] = {'pass': c5, 'detail': 'injected %s -> %s' % (inj and inj['key'], ires.get(inj['key'], {}).get('class') if inj else None)}
    cc['C9'] = c9(rows)
    cc_ok = all(c['pass'] for c in cc.values())
    v, text = verdict_of(counts, controls_ok, cc_ok, prep, len(flagged_edits))
    resolutions = {k: cls['items'][k]['resolution'] for k in sorted(cls.get('items', {}))
                   if cls['items'][k].get('resolution')}
    out = dict(base_out, verdict=v, counts=counts, items=res if cc_ok else None, countercontrols=cc,
               resolutions=resolutions, landed_units=sorted({e['unit'] for e in landed}),
               flagged_edits=flagged_edits, text=text)
    write_json(vpath, out)
    print(text)
    return EXIT[v]


def check_edits(del_path=None, del_commit=None):
    ed = read_json(del_path) if del_path else None
    ok, bad, note = c6(read_json(EDITS_S2), ed, del_commit, resolve(del_commit) if del_commit else B.PIN)
    for b in bad:
        print('C6  ' + b)
    print('check-edits: %s%s' % ('PASS' if ok else 'FAIL', ' (%s)' % note if note else ''))
    return 0 if ok else 1


# =========================================================================== self-test

def self_test():
    snap = load_snapshot()
    pin = dict(B.PIN_CORPUS())
    rows = load_rows()
    ent = {e['id']: e for e in snap['entries']}
    ok = True

    def report(name, good, detail=''):
        nonlocal ok
        print('%-64s %s  %s' % (name, 'PASS' if good else 'FAIL', detail))
        ok = ok and bool(good)

    def one(key, after, ed, items, rules=RULES):
        cl = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic', 'classifier': 'writer',
              'result_pr': 1, 'items': items}
        return classify(B.compare(snap, after), ed, cl, rows, pin, after, rules).get(key, {})

    def edl(*es):
        return {'schema': 'a1exit-compare-edits/2', 'edits': [dict(e, seq=i + 1, components=[]) for i, e in enumerate(es)]}

    def jcls(key, keys, row=None):
        return {key: {'class': 'J', 'edits': keys, 'ledger_row': row, 'reason': 'synthetic', 'resolution': None}}

    def ed(key, f, old, new, rows_=()):
        return {'key': key, 'unit': key.split(':')[0], 'pr': UNIT_PR.get(key.split(':')[0]), 'id': key.split(':')[1],
                'files': [f], 'old': old, 'new': new, 'rows': list(rows_)}

    empty_e = {'schema': 'a1exit-compare-edits/2', 'edits': []}
    empty_c = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic', 'classifier': 'writer', 'result_pr': 1,
               'items': {}}
    # T1 the baseline against itself
    r0 = B.compare(snap, pin)
    c0_ = counts_of(classify(r0, empty_e, empty_c, rows, pin, pin))
    report('T1 baseline vs itself: no change, PASS', c0_['items'] == 0 and verdict_of(c0_, True, True)[0] == 'PASS')
    # T2 unjustified value change -> U, flagged
    cmp_s, eds, cls_s, after_s, k_s = synthetic_case()
    r2 = classify(cmp_s, empty_e, empty_c, rows, pin, after_s)
    report('T2 unjustified value change -> U, FAIL, flagged', r2[k_s]['class'] == 'U' and r2[k_s]['scientific_evaluation']
           and verdict_of(counts_of(r2), True, True)[0] == 'FAIL')
    # T3 covered by a replayed edit -> J, flagged
    r3 = classify(cmp_s, eds, cls_s, rows, pin, after_s)
    report('T3 value change reproduced by its cited edit -> J, flagged',
           r3[k_s]['class'] == 'J' and r3[k_s]['scientific_evaluation'], str(r3[k_s]['notes']))
    # T4-T6: wrong strings, foreign PR, edit elsewhere
    e85 = ent['appA:85']
    bad_new = edl(ed('S2-E:T4', e85['file'], '$4.28/Z_S(\\lambda g_0^2) = 2.361$', '$4.28/Z_S(\\lambda g_0^2) = 2.363$'))
    report('T4 cited edit whose new string is not the after text -> U',
           one(k_s, after_s, bad_new, jcls(k_s, ['S2-E:T4'])).get('class') == 'U')
    report('T5 cited edit not in the compiled lists -> U', one(k_s, after_s, empty_e, jcls(k_s, ['S2-X:E1'])).get('class') == 'U')
    report('T6 cited edit that does not touch the line -> U',
           one(k_s, after_s, edl(ed('S2-E:T6', e85['file'], '| L | 2(a) | 0.4%', '| L | 2(a) | 0.4%%')),
               jcls(k_s, ['S2-E:T6'])).get('class') == 'U')
    # T7 R resolution: unresolved PENDING; justified with a valid review PASS; self-review or bad URL unresolved
    url = REPO_URL + '/pull/1#issuecomment-5'

    def rcls(resn):
        c = copy.deepcopy(cls_s)
        c['items'][k_s]['class'] = 'R'
        c['items'][k_s]['resolution'] = resn
        return counts_of(classify(cmp_s, eds, c, rows, pin, after_s))
    t7 = [verdict_of(rcls(None), True, True)[0],
          verdict_of(rcls({'outcome': 'justified', 'review': url, 'reviewer': 'reviewer'}), True, True)[0],
          verdict_of(rcls({'outcome': 'unjustified', 'review': url, 'reviewer': 'reviewer'}), True, True)[0],
          verdict_of(rcls({'outcome': 'justified', 'review': url, 'reviewer': 'writer'}), True, True)[0],
          verdict_of(rcls({'outcome': 'justified', 'review': 'synthetic review', 'reviewer': 'reviewer'}), True, True)[0],
          verdict_of(rcls({'outcome': 'justified', 'review': REPO_URL + '/pull/2#issuecomment-5', 'reviewer': 'r'}),
                     True, True)[0]]
    report('T7 R: PENDING / PASS / FAIL; self-review, non-URL, other PR stay PENDING',
           t7 == ['PENDING', 'PASS', 'FAIL', 'PENDING', 'PENDING', 'PENDING'], str(t7))
    # T8 relocation out of Main is never plain J
    m780 = ent['M:780']
    ls = B.lines_of(pin['papers/Main.md'])
    del ls[779]
    a8 = dict(pin, **{'papers/Main.md': '\n'.join(ls),
                      'papers/Substratum.md': pin['papers/Substratum.md'] + '\n' + m780['text'] + '\n'})
    e8 = edl(ed('S2-E:T8a', 'papers/Main.md', m780['text'] + '\n', ''),
             ed('S2-E:T8b', 'papers/Substratum.md', pin['papers/Substratum.md'][-200:],
                pin['papers/Substratum.md'][-200:] + '\n' + m780['text'] + '\n'))
    r8 = one('M:780', a8, e8, jcls('M:780', ['S2-E:T8a', 'S2-E:T8b']))
    report('T8 relocation out of Main, both sides replayed -> R', r8.get('class') == 'R', str(r8.get('notes')))
    # T9 J9: own O row with an added open term -> J; foreign row -> R; open term lost -> R
    o_ent = next(e for e in snap['entries'] if e['kind'] == 'prose' and e['file'] != FULL
                 and any(rows.get(r, {}).get('disposition') == 'O' for r in e['ledger_rows'])
                 and pin[e['file']].count(e['text'][-30:]) == 1 and len(OPEN_TERMS.findall(e['text'])) == 1
                 and not j10_hits('', e['text'][-30:] + ' This is conditional.'))
    o_row = next(r for r in o_ent['ledger_rows'] if rows.get(r, {}).get('disposition') == 'O')
    tail = o_ent['text'][-30:]
    a9 = _setline(pin, o_ent['file'], o_ent['line'], o_ent['text'] + ' This is conditional.')
    e9 = edl(ed('S2-E:T9', o_ent['file'], tail, tail + ' This is conditional.', [o_row, 'X-44']))
    r9 = one(o_ent['id'], a9, e9, jcls(o_ent['id'], ['S2-E:T9'], o_row))
    r9b = one(o_ent['id'], a9, e9, jcls(o_ent['id'], ['S2-E:T9'], 'X-44'))
    t_open = OPEN_TERMS.search(o_ent['text'])
    lost = o_ent['text'][:t_open.start()] + 'closed' + o_ent['text'][t_open.end():]
    a9c = _setline(pin, o_ent['file'], o_ent['line'], lost)
    e9c = edl(ed('S2-E:T9c', o_ent['file'], o_ent['text'], lost, [o_row]))
    r9c = one(o_ent['id'], a9c, e9c, jcls(o_ent['id'], ['S2-E:T9c'], o_row))
    report('T9 J9: own O row, open term gained -> J; foreign row -> R; open term lost -> R',
           r9.get('class') == 'J' and r9b.get('class') == 'R' and r9c.get('class') == 'R',
           '%s: %s / %s / %s' % (o_ent['id'], r9.get('class'), r9b.get('class'), r9c.get('class')))
    i135 = ent['Intro:135']
    tail = i135['text'][-30:]
    own = i135['ledger_rows']
    # T10 unaccounted new prediction line -> U, flagged
    a10 = dict(pin, **{'papers/Computation.md': 'Predicted 1.234 MeV, observed 1.230 MeV.\n\n' + pin['papers/Computation.md']})
    r10 = classify(B.compare(snap, a10), empty_e, empty_c, rows, pin, a10)
    k10 = [k for k in r10 if k.startswith('U:')]
    report('T10 unaccounted new prediction line -> U, flagged',
           len(k10) == 1 and r10[k10[0]]['class'] == 'U' and r10[k10[0]]['scientific_evaluation'])
    report('T11 failed control -> VOID', verdict_of(c0_, False, True)[0] == 'VOID' and verdict_of(c0_, True, False)[0] == 'VOID')
    # T12 gaming probes of the earlier rules (reviews c.7059099956 G1-G7 and c.7059220314 finding 1)
    probes = []
    tl = e85['text']
    a = _setline(pin, e85['file'], e85['line'], '')                                         # G1 row deleted
    probes.append(('G1 row deleted, cited by a fragment', one(k_s, a, edl(ed('S2-E:G1', e85['file'], '2.361', '2.362')),
                                                              jcls(k_s, ['S2-E:G1']))))
    a = _setline(pin, i135['file'], i135['line'], i135['text'] + ' Predicted 3.14 conditional.')  # G2
    probes.append(('G2 new prediction sentence cited by "conditional"',
                   one('Intro:135', a, edl(ed('S2-E:G2', i135['file'], tail, tail + ' conditional.', own)),
                       jcls('Intro:135', ['S2-E:G2'], own[0]))))
    a = _setline(pin, i135['file'], i135['line'], i135['text'].replace(' ', '  ', 1)[:len(i135['text']) // 2] + ' conditional')
    probes.append(('G3 unreviewed deletion behind a reviewed word edit',
                   one('Intro:135', a, edl(ed('S2-E:G3', i135['file'], tail, tail + ' conditional', own)),
                       jcls('Intro:135', ['S2-E:G3'], own[0]))))
    a = _setline(pin, e85['file'], e85['line'], tl.replace('2.361', '2.361 GeV', 1))                # G4b unit
    probes.append(('G4b unit added', one(k_s, a, eds, jcls(k_s, ['S2-E:T3']))))
    sw = tl.replace('2.361', 'XX').replace('0.4%', '2.361').replace('XX', '0.4%')                  # G5b swap
    a = _setline(pin, e85['file'], e85['line'], sw)
    probes.append(('G5b values swapped', one(k_s, a, eds, jcls(k_s, ['S2-E:T3']))))
    probes.append(('G6 no-op edit', one(k_s, after_s, edl(ed('S2-E:G6', e85['file'], '2.361', '2.361')), jcls(k_s, ['S2-E:G6']))))
    f_ent = next(e for e in snap['entries'] if any(rows.get(r, {}).get('disposition') == 'F' for r in e['ledger_rows'])
                 and 'conditional' in e['text'] and e['text'].count('conditional') == 1)
    f_row = next(r for r in f_ent['ledger_rows'] if rows.get(r, {}).get('disposition') == 'F')
    a = _setline(pin, f_ent['file'], f_ent['line'], f_ent['text'].replace('conditional', 'established'))
    probes.append(('G7 F row promoted conditional -> established',
                   one(f_ent['id'], a, edl(ed('S2-E:G7', f_ent['file'], 'conditional', 'established', [f_row])),
                       jcls(f_ent['id'], ['S2-E:G7'], f_row))))
    m780t = m780['text']
    for k_, ent_ in (('M:780', m780), ('Intro:135', i135)):
        t = ent_['text']
        a = _setline(pin, ent_['file'], ent_['line'], t + ' Hence the result holds unconditionally for every infinite system.')
        for row in ('X-11', 'X-47', 'X-48'):
            probes.append(('finding-1 probe %s row %s' % (k_, row),
                           one(k_, a, edl(ed('S2-E:P1', ent_['file'], t[-25:],
                                             t[-25:] + ' Hence the result holds unconditionally for every infinite system.',
                                             [row])), jcls(k_, ['S2-E:P1'], row))))
    del m780t
    report('T12 gaming probes: none is J', all(p[1].get('class') != 'J' for p in probes),
           '; '.join('%s=%s' % (n, p.get('class')) for n, p in probes if p.get('class') == 'J') or '%d probes' % len(probes))
    # T13 the standing J10 battery: 16 paraphrases, 28 evasions, allowlist plus claim, gain-only; all flagged
    bad13 = evasion_battery(rows)
    basic = (not j10_hits('', ALLOWLIST[0]['phrase']) and not j10_hits('', ALLOWLIST[1]['phrase'])
             and bool(j10_hits('', 'the configuration space $S$ may be finite or infinite'))
             and bool(j10_hits('', ', and this is proved'))
             and bool(j10_hits('on a finite configuration space', 'on a configuration space'))
             and bool(j10_hits('', 'for in\u00adf\u0456n\\-ite $S$'))
             and not j10_hits('Theorem 2 is proved.', 'Theorem 2 is proved here.'))
    g1 = gain('a b', 'a b c d', ['c'])
    g2 = gain('x.', 'x. ' + ALLOWLIST[1]['phrase'], [])
    g3 = gain('x.', 'x ' + ALLOWLIST[1]['phrase'] + 'y', [])
    g4 = gain('a', 'a [^n]', [], None, None, 'a [^n]\n[^n]: holds for every S')
    report('T13 J10 battery: all %d cases flagged; normalization; gain rule; allowlist whole sentence only'
           % (len(PARAPHRASES) + len(EVASIONS) + len(ALLOW_PLUS) + 1),
           not bad13 and basic and g1 == (['c', 'd'], ['d']) and g2 == ([], []) and g3[0] and 'every' in g4[0],
           str(bad13) if bad13 else '')
    m13 = evasion_battery(rows, dict(RULES, gain=lambda *x, **k: ([], []), change=lambda *x, **k: False),
                          only={'e:[^gen]', 'g:' + GAIN_ONLY})
    report('T13b mutant: with layer 1 disabled the battery fails', bool(m13), str(m13))
    # T13c the sequence battery (N3, N4): all flagged; the set-comparison mutant fails it
    bad13c = n_battery(rows)
    m13c = n_battery(rows, dict(RULES, change=set_changed), only={'N4a', 'N4b', 'N4c', 'N4d'})
    seq_ok = (changed('a b c', 'a c b') and changed('x.', 'x') and changed('a  b', 'a b')
              and not seq_changed('a  b', 'a b') and not set_changed('a b c', 'a c b')
              and changed('x.', 'x. ' + ALLOWLIST[1]['phrase']) and not j10_hits('x.', 'x. ' + ALLOWLIST[1]['phrase']))
    # T13d exactness: H equals the replay except for one doubled space -> not J, flagged
    cm, ed, cl, af, e = gr134(', for every $S$')
    f134 = ent['GR:134']['file']
    af2 = dict(af, **{f134: af[f134].replace('all its members, for', 'all its  members, for', 1)})
    x13d = classify(B.compare(snap, af2), ed, cl, rows, pin, af2).get(e, {})
    cm, ed, cl, af, e = edit_case('GR:134', 'on all its members. $\\square$', 'on all its members; QED. $\\square$',
                                  'X-52', 'T13d')
    af3 = dict(af, **{f134: af[f134].replace('members; QED.', 'members;  QED.', 1)})
    y13d = classify(B.compare(snap, af3), ed, cl, rows, pin, af3).get(e, {})
    report('T13d exact expected text: a whitespace-only difference from the replay is not J and is flagged',
           y13d.get('class') != 'J' and y13d.get('scientific_evaluation') and x13d.get('scientific_evaluation'),
           '%s / %s' % (y13d.get('class'), y13d.get('notes')))
    report('T13c sequence battery: all %d cases flagged; set-comparison mutant fails it' % len(NCASES),
           not bad13c and bool(m13c) and seq_ok, '%s | mutant unflagged %s' % (bad13c, m13c))
    # T14 C6 on the frozen inputs, and its mutants (review c.7059220314 finding 4, and an altered edit)
    s2 = read_json(EDITS_S2)
    g6, b6, _ = c6(s2, None, None, B.PIN)
    report('T14 C6 on the frozen Step-2 list passes', g6, '; '.join(b6[:3]))
    muts = []
    m = copy.deepcopy(s2)
    m['edits'].append(dict(m['edits'][0], key='S2-B:F1', unit='S2-B', pr=1473, id='F1', old='conditional', new='finite',
                           components=[{'id': 'F1', 'source_path': UNITS[1][3] + 'PREREG.md'}]))
    muts.append(('fabricated S2-B edit "conditional" -> "finite"', m))
    m = copy.deepcopy(s2)
    m['edits'].append(dict(m['edits'][0], key='S2-A:F2', id='F2', old='', new=''))
    muts.append(('empty edit', m))
    m = copy.deepcopy(s2)
    m['edits'].append(dict(m['edits'][-1], key='S2-E:F3', id='F3',
                           components=[{'id': 'F3', 'source_path': UNITS[2][3] + 'PREREG.md'}]))
    muts.append(('S2-E edit sourced to the S2-C record', m))
    m = copy.deepcopy(s2)
    m['edits'][5]['new'] = m['edits'][5]['new'] + ' x'
    muts.append(('one frozen edit altered', m))
    caught = [(n, not c6(mm, None, None, B.PIN)[0]) for n, mm in muts]
    report('T15 C6 mutants: each is caught', all(c for _, c in caught), str(caught))
    # T16 C7 and C8 on the synthetic items pass; C8's precondition (J with J10 off) holds there
    syn = (cmp_s, eds, cls_s, after_s, k_s)
    cc = countercontrols(cmp_s, {}, eds, cls_s, rows, pin, after_s, synthetic=syn)
    report('T16 C7 and C8 on the synthetic items pass', cc['C7']['pass'] and cc['C8']['pass'], str(cc))
    # T17 mutants: C7 fails under the earlier containment rule; C8 fails with J10 off and with INFINITY_TERMS empty
    cc7 = countercontrols(cmp_s, {}, eds, cls_s, rows, pin, after_s, dict(RULES, cover=legacy_cover), syn)
    cc8 = countercontrols(cmp_s, {}, eds, cls_s, rows, pin, after_s, dict(RULES, j10=lambda b, a: []), syn)
    cc8i = countercontrols(cmp_s, {}, eds, cls_s, rows, pin, after_s,
                           dict(RULES, j10=lambda b, a: j10_hits(b, a, infinity=[])), syn)
    report('T17 mutants: C7 containment rule; C8 J10 off; C8 INFINITY_TERMS empty',
           not cc7['C7']['pass'] and not cc8['C8']['pass'] and not cc8i['C8']['pass'],
           '%s / %s / %s' % (cc7['C7']['detail'], cc8['C8']['detail'], cc8i['C8']['detail']))
    # T18 C9 passes; each mutant fails it
    g9 = c9(rows)
    mut9 = {'J10 off': dict(RULES, j10=lambda b, a: []),
            'PROMOTION_TERMS empty': dict(RULES, j10=lambda b, a: j10_hits(b, a, promotion=[])),
            'INFINITY_TERMS empty': dict(RULES, j10=lambda b, a: j10_hits(b, a, infinity=[])),
            'finite loss ignored': dict(RULES, j10=lambda b, a: [h for h in j10_hits(b, a) if h != 'finite-scope term lost']),
            'allowlist removed': dict(RULES, j10=lambda b, a: j10_hits(b, a, allow=[])),
            'J9 always passes': dict(RULES, j9=lambda *x: (True, ''))}
    m9 = {k: c9(rows, r)['pass'] for k, r in mut9.items()}
    report('T18 C9 passes; fails under each mutant', g9['pass'] and not any(m9.values()),
           '%s | survivors %s' % (g9['detail'], [k for k, v in m9.items() if v]))
    cm9, ed9, cl9, af9, e9 = c9_cases(rows)['a']
    cl9['items'][e9]['resolution'] = {'outcome': 'justified', 'review': REPO_URL + '/pull/1#issuecomment-7',
                                      'reviewer': 'reviewer', 'proof': 'the proof covering the generality'}
    r9p = classify(cm9, ed9, cl9, rows, pin, af9).get(e9, {})
    cl9['items'][e9]['resolution']['reviewer'] = 'Writer'
    r9q = classify(cm9, ed9, cl9, rows, pin, af9).get(e9, {})
    report('T18b J10 item: resolved with a proof-citing review; a self-review in other case stays R',
           r9p.get('class') == 'R-justified' and r9q.get('class') == 'R', '%s / %s' % (r9p.get('class'), r9q.get('class')))
    # T19 the flag: no category exempt; a table of class other with a value change is flagged
    oth = next(e for e in snap['entries'] if e['categories'] == ['C-TAB'] and e.get('table', {}).get('class') == 'other')
    report('T19 flag: a C-TAB entry of an "other" table is flagged',
           sci_flag({'categories': oth['categories'], 'kinds': ['text changed']}, oth['text'], oth['text'], []))
    # T20 collect refuses a non-empty directory; a crashed comparison is not a pass
    td = tempfile.mkdtemp(prefix='a1exit-st-')
    try:
        open(os.path.join(td, 'stale.json'), 'w').close()
        refused = collect('HEAD', td, None, None) == 2
        os.remove(os.path.join(td, 'stale.json'))
        p = os.path.join(td, 'compare.json')
        code = run([sys.executable, '-I', '-B', os.path.join(RECORD, 'baseline.py'), '--compare', 'deadbeef', '--json', p])
        crash_fails = code != 0 and _result_ok(p, 'deadbeef')[0] is None and resolve('deadbeef') is None
    finally:
        shutil.rmtree(td, ignore_errors=True)
    report('T20 non-empty DIR refused; crashed comparison is not a pass', refused and crash_fails)
    # T20b a controls.json whose pass contradicts its exit is refused (review c.7059976436 finding 3)
    forged = {'controls': {'C1-check': {'exit': 1, 'pass': True}}}
    fr = recheck_controls(forged, '.', B.PIN)
    # T20c C0 accepts only the pinned commit on main's first-parent chain (finding 4)
    head = resolve('HEAD')
    c0ok = (not c0(PIN_S2)[0] and not c0('deadbeef')[0]
            and c0(head)[0] == (head == pinned_frozen_commit()) and not c0(PIN_S2, prep=True)[0])
    report('T20b forged controls.json refused; T20c C0 rejects a non-pinned ref', fr[0] is None and c0ok, fr[1])
    # T20d a compare.json rewritten after collect (digest updated alongside) fails its re-derivation (N2)
    td = tempfile.mkdtemp(prefix='a1exit-n2-')
    try:
        p = os.path.join(td, 'compare.json')
        run([sys.executable, '-I', '-B', os.path.join(RECORD, 'baseline.py'), '--compare', B.PIN, '--json', p])
        good_rd = rederive_compare(p, B.PIN)[0]
        doc = read_json(p)
        doc['entries'] = doc['entries'][1:]
        write_json(p, doc)
        bad_rd = rederive_compare(p, B.PIN)[0]
    finally:
        shutil.rmtree(td, ignore_errors=True)
    report('T20d compare.json re-derived: the true file passes, a rewritten one fails', good_rd and not bad_rd)
    # T21 replay-missing: a landed reviewed edit reverted in H is U; the full landing gives no such item
    s2a = [e for e in s2['edits'] if e['unit'] == 'S2-A']
    full, _ = apply_unit(pin, s2a)
    part, _ = apply_unit(pin, s2a[1:])
    m_full = missing_items(s2a, pin, full)
    r21 = classify(B.compare(snap, part), empty_e, empty_c, rows, pin, part, landed=s2a)
    rm = [k for k in r21 if k.startswith('RM:')]
    report('T21 replay-missing: S2-A landed in full -> none; first edit reverted -> U',
           not m_full and rm and all(r21[k]['class'] == 'U' for k in rm), '%d / %s' % (len(m_full), rm[:3]))
    # T21b completeness: one of two reviewed edits on one line reverted in H -> U (ch02:144, ch02:192)
    res21b = []
    for eid, rev in (('ch02:144', 'S2-B:E15b'), ('ch02:192', 'S2-D:E14')):
        en = ent[eid]
        hcorp, _ = apply_unit(pin, [e for e in s2['edits'] if e['key'] != rev])
        txt = pin[en['file']]
        a_ = sum(len(x) + 1 for x in B.lines_of(txt)[:en['line'] - 1])
        _, sp, _ = replay(txt, [e for e in s2['edits'] if en['file'] in e['files']], (a_, a_ + len(en['text'])))
        touching = sorted(t[5:] for t in next(x for x in sp if 'anchor' in x[4])[4] if t.startswith('edit:'))
        cited = [k for k in touching if k != rev]
        cl = {'schema': 'a1exit-compare-classify/2', 'head': 'synthetic', 'classifier': 'writer', 'result_pr': 1,
              'items': {eid: {'class': 'J', 'edits': cited, 'ledger_row': (en['ledger_rows'] or [None])[0],
                              'reason': 'synthetic', 'resolution': None}}}
        x = classify(B.compare(snap, hcorp), s2, cl, rows, pin, hcorp, landed=s2['edits']).get(eid, {})
        res21b.append((eid, rev in touching, x.get('class')))
    report('T21b one of two same-line reviewed edits reverted -> U', all(t and c == 'U' for _, t, c in res21b),
           str(res21b))
    print('self-test ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


def main(argv):
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == 'self-test':
        return self_test()
    if argv[0] == 'digests':
        print(json.dumps({'schema': 'a1exit-compare-frozen/2', 'pin': B.PIN, 'pin_s2': PIN_S2, 'sha256': digests()},
                         indent=1, sort_keys=True))
        return 0
    if argv[0] == 'collect' and opt('--head') and opt('--out') and opt('--frozen-ref'):
        return collect(opt('--head'), opt('--out'), opt('--frozen-ref'), opt('--del-commit'), '--prep' in argv)
    if argv[0] == 'verdict' and opt('--dir') and opt('--classify'):
        return verdict(opt('--dir'), opt('--classify'))
    if argv[0] == 'compile-s2':
        res = compile_s2()
    elif argv[0] == 'compile-del' and opt('--commit'):
        res = compile_del(opt('--commit'))
    elif argv[0] == 'check-edits':
        return check_edits(opt('--del'), opt('--del-commit'))
    else:
        print(__doc__)
        return 2
    if opt('--out'):
        write_json(opt('--out'), res)
    else:
        print(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""check_objects.py -- verifies the retained off-main git objects of the evidence-retention archive.

From the repository root:

    python3 -I verification/audits/evidence-retention/check_objects.py                 # tree mode, no git
    python3 -I verification/audits/evidence-retention/check_objects.py --reconstitute  # history mode, uses git
    python3 -I verification/audits/evidence-retention/check_objects.py --self-test     # needs git and history
    python3 -I verification/audits/evidence-retention/check_objects.py --materialize   # history mode, then adds the
                                                    # stored objects to this repository's object store (no refs)

Each object in objects/manifest.json is a commit, tree or blob that main's records cite (or that a cited object
needs) and that main does not reach. A stored file holds it in one of two forms: `raw`, the object's content without
git's header (a blob's bytes, a commit's text, a tree's entries), or `zlib`, a git loose object.

Tree mode (no git, no network):
  O1  every stored entry's file exists with its recorded size and sha256, and its content hashes to its id as
      sha1("<type> <size>\\0" + content); a zlib file's header names the recorded type and size;
  O2  every file under objects/ is listed, or is manifest.json;
  O3  the manifest is well formed: known schema, mechanisms and forms, unique 40-hex ids, stored entries with a
      file and withheld entries without one, a commit's mechanism consistent with its parent and withheld lists
      (withheld_blobs only on raw:partial-tree and inclusion-proof commits);
  O4  closure: every id a stored commit or fully retained tree names is stored, withheld, or outside the retained
      set (expected on main, which history mode checks); a path tree (raw:proof-path) names its entries off the
      inclusion path without retaining them, and never lies under a fully retained tree; an inclusion path walks
      from its commit through stored trees; a connected commit's parents are retained connected commits or (H3) on
      main; a raw:tree commit has a parent that is neither; parents_not_retained lists only parents that are not
      retained; a raw:partial-tree commit's tree, and an inclusion-proof commit's inclusion paths, withhold exactly
      the commit's listed blobs, and no other commit's tree withholds any;
  O5  excerpt guard: no stored, named or listed id, and no stored file's own blob id, has its sha256 in the
      deny-list (the list holds sha256 digests of ids, so it cites no object itself);
  O6  scan: no stored object's content, decoded, and no file here matches the secret patterns, an IPv4 address or
      an e-mail address, outside the declared exemptions (commit identity lines and Co-Authored-By trailers whose
      address digest is listed; a commit's gpgsig block; reserved example domains);
  O7  every citation's file exists and its cited line holds one of the recorded tokens; a recorded run is on the
      line as a whole number, and a recorded hex token (7 to 40 digits, not all decimal) is a prefix of the entry's
      own id; every recorded id discrepancy
      (a cited full id that names no object, mapped to the retained head of the cited run) holds the cited id on
      its line, maps to a stored object with the same eight-digit prefix, and that object carries the run; and
      the provenance-errata entry it names records the same location, cited id, real head and run;
  O8  every id recorded as missing is retained nowhere here, and each of its citing lines still holds it;
  O9  the withheld entries are exactly APPROVED_WITHHELD (id, mechanism, paths), each non-empty; every one is
      named by a retained tree of a commit that lists it (for an inclusion proof, under
      its inclusion paths); its recorded paths are exactly where those trees name it, each of a file type its
      mechanism covers (.log, .out or .err for a raw log, .txt for a raw output, .pdf for a build output); its
      needed_by entries are among them; and it records a size (which no tree records, so the size is as read from
      the recovery copy when the archive was built, and is not checked). An approval that names commits (archive
      tranche 4) is also bound to them: the commits whose retained trees name the blob are exactly those, and the
      entry records each instance with its commit, path, size, blob id, sha256 and reason;
  O10 the citation lifecycle. A commit carries recorded citations (`cited`, which O7 verifies) or a pending one
      (`awaiting_citation`: pull request, round, the record's path outside this archive, and optionally the run the
      record names beside it, the record's citing lines and the forms of the id it uses), never both and never
      neither; any other entry may carry a pending citation, which is checked alike. A pending citation is judged
      against the tree under check, never against a pull request:
        pending   the named record is not in the tree. This passes, and the entry counts as not cited, however
                  long it stays so: a pull request that never lands leaves it pending, never cited;
        eligible  the named record is in the tree and cites the id (the full id, or a hex word of 7 or more digits
                  that is a prefix of it), on exactly the recorded lines and with the recorded forms when the entry
                  names them, with the recorded run as a whole number on a citing line or a line next to one. This
                  passes and is printed as eligible for promotion: the commit that lands the record need not touch
                  this manifest, and a later archive commit replaces awaiting_citation with the citations, which
                  O7 then verifies;
        failing   the record is in the tree and does not cite the id, cites it on other lines or in other forms
                  than recorded, or does not name the recorded run beside it; or the recorded run is retained
                  under ci/ with another head commit.
      No other rule reads a commit's citation state: its object checks (O1-O9, H1-H7) are the same whether it is
      pending, eligible or cited.
History mode (--reconstitute) adds, in a temporary repository that borrows this repository's objects (H0: a git
command that fails fails the check, rather than leaving a rule to read empty output):
  H1  the base, and each later tranche's base in tranche_bases, is in the repository and an ancestor of HEAD;
  H2  every stored object, written with git, gets exactly its recorded id;
  H3  every id the retained objects name that is not retained or withheld is reachable from the base;
  H4  connectivity, relative to the archive and the base, never to what else this clone holds: with a ref at
      every raw:connected and raw:tree commit and every complete cited tree, every raw:tree commit a shallow
      boundary, git fsck --connectivity-only passes and every object the refs reach is retained or reachable from
      the base; each raw:connected commit's history reaches the base only through retained raw:connected commits;
      what a raw:partial-tree commit's tree, or an inclusion-proof commit's inclusion paths, names beyond the
      archive and the base is exactly its withheld blobs; every inclusion path resolves to a retained or withheld
      object;
  H5  every listed identity digest is the digest of an address in the base's history;
  H6  no deny-listed id is reachable from HEAD of this repository, or from any reconstituted object;
  H7  no entry, stored or withheld, is reachable from its own tranche's base, and no id recorded as missing is
      reachable from the base: what main already holds is never retained here. H3 and H4 count as on main what
      the latest tranche base reaches.
"""
import bisect
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
OBJ = os.path.join(HERE, 'objects')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MECH = {'commit': ('raw:connected', 'raw:tree', 'raw:partial-tree', 'inclusion-proof', 'identity-anchor'),
        'tree': ('raw', 'raw:proof-path'),
        'blob': ('byte-copy', 'withheld:raw-log', 'withheld:raw-output', 'withheld:build-pdf')}
WITHHELD = ('withheld:raw-log', 'withheld:raw-output', 'withheld:build-pdf')
# the file types each withholding mechanism covers: a blob is withheld only at paths of its mechanism's kind
WITHHELD_SUFFIXES = {'withheld:raw-log': ('.log', '.out', '.err'), 'withheld:raw-output': ('.txt',),
                     'withheld:build-pdf': ('.pdf',)}
# The withholding approved by the owner on 2026-10-17 (non-empty raw logs and captured .out/.err output; the three
# raw outputs below; build PDFs), as exact entries. A withheld entry must be one of these, with this mechanism and
# exactly these paths, so neither a file type nor a coordinated manifest and list edit can authorize withholding:
# changing the withheld set changes this checker.
APPROVED_WITHHELD = {
    '12095f6f3a739c988e5d5da28667d1761e352ad5': ('withheld:build-pdf',
        ['book/The-Incompleteness-of-Observation-FULL.pdf']),
    '196d096d52d42ee2df3b4824f5ab6bc3e0939ca0': ('withheld:raw-log',
        ['research/a42-revalidation/c6_control.log']),
    '325c825566c37679bf09ec463a29c96572640cb9': ('withheld:raw-log',
        ['research/round7-channel/CI-REPAIR.log']),
    '38077af8485cb0e1f52c2d69863e1a4ac6ca1d16': ('withheld:raw-log',
        ['research/a42-rerun/ctrl16.log']),
    '3a61f0ca7aefe695fb028dfbaa7acbc594f260bb': ('withheld:raw-log',
        ['research/a42-rerun/lemmas42.log']),
    '43e18150962622cdd84daf5d46cc6f52d7638ee3': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/m0all_b39_b.log']),
    '5c1bf575ba52f67d4d2e31077a5766e8b4c307eb': ('withheld:raw-log',
        ['research/a42-rerun/m0all_b39_a.log']),
    '609e70ae7d669939d25e90edd90ff140dc798668': ('withheld:raw-log',
        ['research/a42-rerun/sat_hr39.log']),
    '68a70d013148a04066a149cb8a45092c6d5baed4': ('withheld:raw-log',
        ['research/a42-rerun/n18_in_a41.log']),
    '6a7a010ab29ab09fc79e0d199222cade753ee505': ('withheld:raw-log',
        ['research/a42-rerun/d01_zero.log']),
    '71f55213eb0bc7c6fbc375c397739354a784ad86': ('withheld:raw-log',
        ['research/round7-channel/native-controls.selftest.final.out']),
    '74badd4d5082acb54b6a8c673a92541f4fd11dd7': ('withheld:raw-log',
        ['research/a42-rerun/d01_two.log']),
    '74bc976f85a728fa905124a63108d40f53bb4e6b': ('withheld:build-pdf',
        ['papers/Main.pdf']),
    '7792971561f0fb122e7742fc23df26ff9c277e2e': ('withheld:raw-output',
        ['research/a42-rerun/Rle13_39_a.txt']),
    '7c9aa5e4481c37eeb582ee4290894173a48599b4': ('withheld:raw-log',
        ['research/a42-revalidation/r5.log']),
    '8a0da161222b988e5300c95de129abf3cbbadf54': ('withheld:raw-log',
        ['research/a42-revalidation/r2b2.log']),
    '8b73bdb948d7f2dfdc05eae8c31ddfb5ca8d6602': ('withheld:raw-log',
        ['research/a42-rerun/spanAll77.log']),
    '95e474b742286e20a60485fc3b65a1a6f6676418': ('withheld:raw-log',
        ['research/a42-rerun/sat_cubes39.log']),
    '9ef11ead5816d767e7f6bf15bfd4104e0d6d9e94': ('withheld:raw-output',
        ['research/a42-rerun/Rle13_39_b.txt']),
    'a1c82766fc8fee04a11ab84477f766c76c10965b': ('withheld:raw-output',
        ['research/a42-rerun/Rall_39.txt']),
    'a4d6527933d6e55612199dfe1e463762694de822': ('withheld:raw-log',
        ['research/a42-revalidation/r2a.log']),
    'aa639a024172876bb9b6dad5e00a180e0dfa4bb8': ('withheld:raw-log',
        ['research/AUDITS/2026-10-11-round6/CI-FAILED-B23.log']),
    'b3a6c133d46819a168393aaeb74af9b51a3b349b': ('withheld:raw-log',
        ['research/round7-channel/channel_check.replay.out', 'research/round7-channel/channel_check.run1.out']),
    'bcdefc3c7091a6f50c1a52f5bb7c198a17538edb': ('withheld:build-pdf',
        ['papers/Explainer.pdf']),
    'd68ca300d27823f5df11c7aeb15dab3d7448129c': ('withheld:raw-log',
        ['research/a42-rerun/cvsize.log']),
    'de2e4b294a5181b28f8d54663641de416ed02978': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/sat_cubes39.log']),
    'ecd7c48de5cb22ca19fa7a4b43fd7c990276e613': ('withheld:raw-log',
        ['research/a42-rerun/quarantine/m0all_b39_a.log']),
    'fbc82c68dd2493e547e45b2fd948638cd325eb93': ('withheld:raw-log',
        ['research/a42-rerun/m0all_b39_b.log']),
    # Archive tranche 4, approved by the owner on 2026-10-17 for exactly these paths in exactly these two commits
    # (#831's research sources): a third element binds the approval to the commits whose trees name the blob.
    'c697b82b8a7d6719d78dfc74bc8183c85fa12255': ('withheld:raw-output',
        ['verification/programmes/oi-qm/reconstruction/preservation-induction-design/exact-output.txt'],
        ['e684897da41b1c3d066b880194c9beb87a19b7ad', 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3']),
    '8cdf3a83f78059d81a701c2e4951e54f3a2b06bd': ('withheld:raw-output',
        ['verification/programmes/oi-qm/reconstruction/preservation-induction-design/independent-output.txt'],
        ['e684897da41b1c3d066b880194c9beb87a19b7ad', 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3']),
}
ERRATA = 'verification/audits/provenance-errata/errata.json'
TOKENS = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}', re.I)
IPV4 = re.compile(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])')
EMAIL_ANY = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
# the union is check_retention.py's SECRET pattern (its R5) plus four token shapes
SECRET = re.compile(TOKENS.pattern + r'|' + IPV4.pattern + r'|' + EMAIL_ANY.pattern, re.I)
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})')
RESERVED = re.compile(r'(^|\.)(example\.(com|org|net|invalid)|[a-z0-9-]+\.(test|invalid))$', re.I)
SIG_BEGIN = re.compile(r'^gpgsig(-sha256)? -{5}BEGIN (SSH|PGP) SIGNATURE-{5}$')


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def git_id(typ, content):
    return hashlib.sha1(typ.encode() + b' %d\0' % len(content) + content).hexdigest()


def tree_entries(data):
    out, i = [], 0
    while i < len(data):
        sp = data.index(b' ', i)
        nul = data.index(b'\0', sp)
        out.append((data[i:sp].decode(), data[sp + 1:nul].decode('utf-8', 'surrogateescape'), data[nul + 1:nul + 21].hex()))
        i = nul + 21
    return out


def commit_fields(data):
    head = data.split(b'\n\n', 1)[0].decode('utf-8', 'surrogateescape').split('\n')
    tree = next(l[5:] for l in head if l.startswith('tree '))
    return tree, [l[7:] for l in head if l.startswith('parent ')]


def read_stored(objdir, e, F):
    """Content bytes of a stored entry, or None (after recording the failure)."""
    path = os.path.join(objdir, e['file'])
    try:
        body = open(path, 'rb').read()
    except OSError:
        F('O1 %s: stored file %s is missing' % (e['oid'][:12], e['file']))
        return None
    if len(body) != e.get('bytes') or sha256(body) != e.get('sha256'):
        F('O1 %s: %s does not have its recorded size and sha256' % (e['oid'][:12], e['file']))
        return None
    if e['form'] == 'zlib':
        try:
            full = zlib.decompress(body)
        except zlib.error:
            F('O1 %s: %s is not a zlib stream' % (e['oid'][:12], e['file']))
            return None
        hdr, _, content = full.partition(b'\0')
        if hdr != e['type'].encode() + b' %d' % len(content):
            F('O1 %s: %s has the header %r' % (e['oid'][:12], e['file'], hdr[:40]))
            return None
    else:
        content = body
    if git_id(e['type'], content) != e['oid']:
        F('O1 %s: the content of %s hashes to %s' % (e['oid'][:12], e['file'], git_id(e['type'], content)[:12]))
        return None
    return content


LOCAL = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._%+-')
DOMAIN = re.compile(r'[A-Za-z0-9.-]+\.[A-Za-z]{2,}')


def candidates(text):
    """(offset, match) of every secret-pattern match: the token shapes, IPv4 addresses and e-mail addresses (found
    from each '@', which is the same set SECRET finds, without its cost on long texts)."""
    for m in TOKENS.finditer(text):
        yield m.start(), m.group(0)
    for m in IPV4.finditer(text):
        yield m.start(), m.group(0)
    k = text.find('@')
    while k != -1:
        a = k
        while a > 0 and text[a - 1] in LOCAL:
            a -= 1
        m = DOMAIN.match(text, k + 1)
        if a < k and m:
            yield a, text[a:m.end()]
        k = text.find('@', k + 1)


# Within one self-test run, the O6 verdict on a text is memoised under the sha256 of the text itself, as decoded in
# that check, and of the identity digests: the scan is a function of these alone, so a mutated byte or manifest
# is a new key and is scanned afresh. Nothing is keyed by an object id. None outside a self-test run.
_SCAN_MEMO = None
# Within one self-test run, the lookups that depend only on this repository's history, keyed by the base and HEAD.
_HISTORY_MEMO = None


def scan_text(label, text, is_commit, idents, F):
    """O6: report the first line with a match that no declared exemption covers."""
    if _SCAN_MEMO is None:
        n = first_unexempt_line(text, is_commit, idents)
    else:
        key = (sha256(text.encode('utf-8', 'surrogatepass')), is_commit, sha256(json.dumps(sorted(idents)).encode()))
        if key not in _SCAN_MEMO:
            _SCAN_MEMO[key] = first_unexempt_line(text, is_commit, idents)
        n = _SCAN_MEMO[key]
    if n is not None:
        F('O6 %s:%d matches a secret pattern' % (label, n + 1))


def first_unexempt_line(text, is_commit, idents):
    """The index of the first line with a match that no declared exemption covers, or None."""
    starts = [0] + [m.end() for m in re.finditer('\n', text)]
    lines = text.split('\n')
    exempt = set()
    if is_commit:                                   # header lines: identities and the signature block
        insig = False
        for n, l in enumerate(lines):
            if l == '':
                body = n + 1
                break
            if insig:
                exempt.add(n)
                insig = not l.strip().startswith('-----END')
            elif SIG_BEGIN.match(l):
                exempt.add(n)
                insig = True
            elif re.match(r'(author|committer|tagger) ', l):
                m = re.search(r'<([^>]*)>', l)
                if m and sha256(m.group(1).encode()) in idents and not TOKENS.search(l) and not IPV4.search(l) \
                        and l.count('@') == 1:
                    exempt.add(n)
        else:
            body = len(lines)
        for n in range(body, len(lines)):
            l = lines[n]
            if l.lower().startswith('co-authored-by:'):
                m = re.search(r'<([^>]*)>', l)
                if m and sha256(m.group(1).encode()) in idents and l.count('@') == 1 and not TOKENS.search(l) \
                        and not IPV4.search(l):
                    exempt.add(n)
    for off, mt in sorted(candidates(text)):
        n = bisect.bisect_right(starts, off) - 1
        if n in exempt:
            continue
        em = EMAIL.fullmatch(mt)
        if em and RESERVED.search(em.group(1)):
            continue
        return n
    return None


ARCHIVE_REL = os.path.relpath(HERE, ROOT).replace(os.sep, '/')
HEXWORD = re.compile(r'(?<![0-9A-Fa-f])[0-9a-f]{7,40}(?![0-9A-Fa-f])')
RUNLIKE = re.compile(r'(?<![0-9])[0-9]{9,20}(?![0-9])')
PENDING_KEYS = {'pull_request', 'round', 'record', 'note', 'run', 'lines', 'tokens'}


def id_forms(oid, line):
    """The forms of oid that line holds: hex words of 7 to 40 digits that are prefixes of oid (a word of decimal
    digits alone counts only at 40, so a run number is never read as an abbreviated id)."""
    return [w for w in HEXWORD.findall(line) if oid.startswith(w) and (len(w) == 40 or not w.isdigit())]


def pending_citation(oid, a, root, F):
    """O10 for an entry that records awaiting_citation: ('pending', None) while its record is not in the tree,
    ('eligible', (citing lines, run lines)) once the record is in the tree and cites it as the entry names, and None
    after recording a failure."""
    rec = a.get('record') if isinstance(a, dict) else None
    run, lines, toks = (a.get(k) for k in ('run', 'lines', 'tokens')) if isinstance(a, dict) else (None,) * 3
    if not isinstance(a, dict) or not set(a) <= PENDING_KEYS or type(a.get('pull_request')) is not int or \
            not isinstance(a.get('round'), str) or not a['round'] or not isinstance(rec, str) or \
            not rec.endswith('.md') or rec.startswith('/') or '..' in rec.split('/') or \
            (rec + '/').startswith(ARCHIVE_REL + '/') or \
            not (run is None or isinstance(run, str) and re.fullmatch(r'[0-9]{1,20}', run)) or \
            not (lines is None or isinstance(lines, list) and lines and len(set(lines)) == len(lines) and
                 all(type(n) is int and n > 0 for n in lines)) or \
            not (toks is None or isinstance(toks, list) and toks and
                 all(isinstance(t, str) and id_forms(oid, t) == [t] for t in toks)):
        F('O10 %s: its pending citation is malformed (pull request, round, a record outside the archive, run, lines '
          'or id forms)' % oid[:12])
        return None
    if run is not None:
        try:
            rhead = json.load(open(os.path.join(root, ARCHIVE_REL, 'ci', run, 'run.json'), encoding='utf-8')).get('head_sha')
        except (OSError, ValueError, AttributeError):
            rhead = oid
        if rhead != oid:
            F('O10 %s: its pending citation names run %s, whose head in ci/%s/run.json is %s'
              % (oid[:12], run, run, str(rhead)[:12]))
            return None
    path = os.path.join(root, rec)
    if not os.path.isfile(path):
        return 'pending', None
    try:
        L = open(path, encoding='utf-8').read().split('\n')
    except (OSError, UnicodeDecodeError):
        F('O10 %s: its record %s is in the tree and cannot be read' % (oid[:12], rec))
        return None
    at = {n: f for n, f in ((n, id_forms(oid, l)) for n, l in enumerate(L, 1)) if f}
    if not at:
        other = sorted({w for n in (lines or []) if n <= len(L) for w in HEXWORD.findall(L[n - 1]) if not w.isdigit()})
        F('O10 %s: its record %s is in the tree and does not cite it%s' % (
            oid[:12], rec, '; the recorded line(s) hold %s' % ', '.join(other) if other else ''))
        return None
    bad = []
    if lines is not None and sorted(at) != sorted(lines):
        bad.append('cites it on line(s) %s, not on the recorded %s' % (sorted(at), sorted(lines)))
    if toks is not None and not set(toks) <= {w for f in at.values() for w in f}:
        bad.append('does not cite it as %s' % ', '.join(sorted(set(toks) - {w for f in at.values() for w in f})))
    runat = []
    if run is not None:
        rx = re.compile(r'(?<![0-9])%s(?![0-9])' % run)
        runat = [n for n, l in enumerate(L, 1) if rx.search(l) and {n - 1, n, n + 1} & set(at)]
        if not runat:
            near = sorted({x for n in at for m in (n - 1, n, n + 1) if 1 <= m <= len(L) for x in RUNLIKE.findall(L[m - 1])})
            bad.append('does not name run %s beside it%s' % (run, ' (beside it: %s)' % ', '.join(near) if near else ''))
    if bad:
        F('O10 %s: its record %s is in the tree and %s' % (oid[:12], rec, '; '.join(bad)))
        return None
    return 'eligible', (sorted(at), runat)


def check(objdir, root):
    fails = []
    F = fails.append
    try:
        man = json.load(open(os.path.join(objdir, 'manifest.json'), encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return ['O3 manifest unreadable: %s' % exc], {}
    if man.get('schema') != 'oi-evidence-objects' or man.get('version') != 1 or \
            not re.fullmatch(r'[0-9a-f]{40}', str(man.get('base', ''))):
        return ['O3 unknown schema, version or base'], {}
    for k in ('excerpt_denylist_sha256_of_id', 'identities_sha256'):
        if not isinstance(man.get(k), list) or not all(isinstance(x, str) and re.fullmatch(r'[0-9a-f]{64}', x)
                                                        for x in man[k]):
            return ['O3 %s is not a list of sha256 digests' % k], {}
    tb = man.get('tranche_bases', {})
    if not isinstance(tb, dict) or not all(re.fullmatch(r'[0-9]+', str(k)) and re.fullmatch(r'[0-9a-f]{40}', str(v))
                                           for k, v in tb.items()):
        return ['O3 tranche_bases is not a map of tranche numbers to commit ids'], {}
    deny = set(man['excerpt_denylist_sha256_of_id'])
    idents = set(man['identities_sha256'])
    ents, listed = {}, {'manifest.json'}
    for e in man.get('objects', []):
        oid = e.get('oid', '')
        if not re.fullmatch(r'[0-9a-f]{40}', oid) or oid in ents:
            F('O3 bad or duplicate id %r' % oid)
            continue
        if e.get('mechanism') not in MECH.get(e.get('type'), ()):
            F('O3 %s: mechanism %r is not one of a %s' % (oid[:12], e.get('mechanism'), e.get('type')))
            continue
        stored = e['mechanism'] not in WITHHELD
        if stored != bool(e.get('file')) or (stored and e.get('form') not in ('raw', 'zlib')):
            F('O3 %s: a %s entry %s a file' % (oid[:12], e['mechanism'], 'lacks' if stored else 'has'))
            continue
        if stored and e['file'] != ('loose/%s/%s' % (oid[:2], oid[2:]) if e['form'] == 'zlib'
                                    else '%s/%s/%s' % (e['type'], oid[:2], oid)):
            F('O3 %s: file %s is not where its form puts it' % (oid[:12], e['file']))
        ents[oid] = e
        if stored:
            listed.add(e['file'])
    for dirpath, _, names in os.walk(objdir):
        for fn in names:
            rel = os.path.relpath(os.path.join(dirpath, fn), objdir).replace(os.sep, '/')
            if rel not in listed:
                F('O2 unlisted file %s' % rel)
            if sha256(git_id('blob', open(os.path.join(dirpath, fn), 'rb').read()).encode()) in deny:
                F('O5 the file %s is itself a deny-listed blob' % rel)
    scan_text('objects/manifest.json', open(os.path.join(objdir, 'manifest.json'), encoding='utf-8').read(), False,
              idents, F)
    content = {}
    for oid, e in ents.items():
        if sha256(oid.encode()) in deny:
            F('O5 %s: a deny-listed (excerpt) id is in the manifest' % oid[:12])
        if e['mechanism'] in WITHHELD:
            continue
        c = read_stored(objdir, e, F)
        if c is None:
            continue
        content[oid] = c
        if e['type'] == 'tree':
            scan_text(e['file'], '\n'.join(n for _, n, _ in tree_entries(c)), False, idents, F)
        else:
            scan_text(e['file'], c.decode('utf-8', 'replace'), e['type'] == 'commit', idents, F)
    # O4 closure, O5 named ids
    external = set()

    def kind(x):
        return 'stored' if x in content else 'withheld' if x in ents and ents[x]['mechanism'] in WITHHELD else \
            'broken' if x in ents else 'external'

    def walk_tree(t, seen, withheld_ok, origin):
        if t in seen:
            return
        seen.add(t)
        if kind(t) != 'stored':
            if kind(t) == 'external':
                external.add(t)
            else:
                F('O4 %s: tree %s is %s' % (origin[:12], t[:12], kind(t)))
            return
        if ents[t]['mechanism'] == 'raw:proof-path':
            F('O4 %s: tree %s is retained as a path tree but lies under a fully retained tree' % (origin[:12], t[:12]))
            return
        for mode, name, x in tree_entries(content[t]):
            if sha256(x.encode()) in deny:
                F('O5 %s: tree %s names a deny-listed (excerpt) id at %s' % (origin[:12], t[:12], name))
            if mode == '160000':
                continue
            if mode == '40000':
                walk_tree(x, seen, withheld_ok, origin)
            elif kind(x) == 'withheld':
                withheld_ok.add(x)
            elif kind(x) == 'external':
                external.add(x)
            elif kind(x) == 'broken':
                F('O4 %s: blob %s is listed but not readable' % (origin[:12], x[:12]))

    incomplete_trees = set()

    for oid, e in ents.items():
        if e['type'] == 'tree' and oid in content and e['mechanism'] == 'raw':
            twh = set()
            walk_tree(oid, set(), twh, oid)
            if twh:
                incomplete_trees.add(oid)
        if e['type'] != 'commit' or oid not in content:
            continue
        tree, parents = commit_fields(content[oid])
        for x in [tree] + parents:
            if sha256(x.encode()) in deny:
                F('O5 %s: commit names a deny-listed (excerpt) id' % oid[:12])
        if parents != e.get('parents'):
            F('O3 %s: the recorded parents are not the commit\'s' % oid[:12])
        named = e.get('parents_not_retained', [])
        if any(p not in parents or p in ents for p in named):
            F('O3 %s: a parent named as not retained is not a parent, or is retained' % oid[:12])
        m = e['mechanism']
        if e.get('withheld_blobs') and m not in ('raw:partial-tree', 'inclusion-proof'):
            F('O3 %s: a %s commit carries a withheld_blobs list' % (oid[:12], m))
        if m == 'identity-anchor':
            continue
        if m == 'inclusion-proof':
            iwh = set()
            for p in e.get('inclusion_paths') or ['(none)']:
                cur = tree
                for part in [x for x in p.split('/') if x]:
                    if cur not in content:
                        F('O4 %s: inclusion path %s leaves the stored trees' % (oid[:12], p))
                        break
                    nxt = [x for mode, name, x in tree_entries(content[cur]) if name == part]
                    if not nxt:
                        F('O4 %s: inclusion path %s does not exist' % (oid[:12], p))
                        break
                    cur = nxt[0]
                else:
                    if kind(cur) != 'stored' and kind(cur) != 'withheld':
                        F('O4 %s: inclusion path %s ends at an object not retained' % (oid[:12], p))
                    elif kind(cur) == 'withheld':
                        iwh.add(cur)
                    elif cur in content and ents[cur]['type'] == 'tree':
                        if not p.endswith('/') or ents[cur]['mechanism'] != 'raw':
                            F('O4 %s: inclusion path %s ends at a tree not retained in full' % (oid[:12], p))
                        walk_tree(cur, set(), iwh, oid)
            if sorted(iwh) != sorted(e.get('withheld_blobs', [])):
                F('O4 %s: the blobs withheld under its inclusion paths are not exactly the recorded ones' % oid[:12])
            continue
        wh = set()
        walk_tree(tree, set(), wh, oid)
        if m == 'raw:partial-tree':
            if not wh or sorted(wh) != sorted(e.get('withheld_blobs', [])):
                F('O4 %s: its tree\'s withheld blobs are not exactly the recorded ones' % oid[:12])
        elif wh:
            F('O4 %s: a %s commit names withheld blobs' % (oid[:12], m))
        # parents_not_retained names the parents that are neither retained nor (H3 checks) on main
        bad = [p for p in parents if (p in ents and ents[p]['mechanism'] != 'raw:connected') or p in named]
        if m == 'raw:connected' and bad:
            F('O4 %s: raw:connected, but parent %s is not connected' % (oid[:12], bad[0][:12]))
        if m == 'raw:tree' and not bad:
            F('O4 %s: raw:tree, but every parent is connected' % oid[:12])
    # O10 the citation lifecycle: cited (O7 verifies it), or pending against the tree: pending, eligible or failing
    states = {}
    for oid, e in ents.items():
        if 'awaiting_citation' not in e:
            if e['type'] == 'commit' and not e.get('cited'):
                F('O10 %s: an uncited commit names no record, round and pull request that are to cite it' % oid[:12])
            elif e['type'] == 'commit':
                states[oid] = ('cited', None)
            continue
        if 'cited' in e:
            F('O10 %s: carries cited and awaiting_citation together' % oid[:12])
            continue
        st = pending_citation(oid, e['awaiting_citation'], root, F)
        if st:
            states[oid] = st
    # O7 citations
    texts = {}
    for oid, e in ents.items():
        for c in e.get('cited', []):
            f, _, ln = c.get('location', '').rpartition(':')
            if f not in texts:
                try:
                    texts[f] = open(os.path.join(root, f), encoding='utf-8').read().split('\n')
                except (OSError, UnicodeDecodeError):
                    texts[f] = None
            lines = texts[f]
            toks = list(c.get('tokens') or []) + ([c['run']] if c.get('run') else [])
            if lines is None or not ln.isdigit() or int(ln) > len(lines):
                F('O7 %s: citing location %s does not exist' % (oid[:12], c.get('location')))
            elif not toks or not any(t in lines[int(ln) - 1] for t in toks):
                F('O7 %s: %s does not hold its token' % (oid[:12], c.get('location')))
            elif c.get('run') and not re.search(r'(?<![0-9])%s(?![0-9])' % re.escape(str(c['run'])), lines[int(ln) - 1]):
                F('O7 %s: %s does not hold its run %s' % (oid[:12], c.get('location'), c['run']))
            elif any(isinstance(t, str) and re.fullmatch(r'[0-9a-f]{7,40}', t) and not t.isdigit() and
                     not oid.startswith(t) for t in toks):
                F('O7 %s: %s records a hex token that is not a prefix of its id' % (oid[:12], c.get('location')))
    for x in man.get('id_discrepancies', []):
        f, _, ln = x.get('location', '').rpartition(':')
        try:
            line = open(os.path.join(root, f), encoding='utf-8').read().split('\n')[int(ln) - 1]
        except (OSError, ValueError, IndexError):
            line = None
        if line is None or x.get('cited_id', '-') not in line or x.get('run', '-') not in line and \
                not any(x['run'] == c.get('run') for c in ents.get(x.get('retained_id'), {}).get('cited', [])):
            F('O7 id discrepancy at %s: the line does not hold the cited id, or the run is not the retained one\'s'
              % x.get('location'))
        elif x['cited_id'] in ents or x.get('retained_id') not in content or x['retained_id'][:8] != x['cited_id'][:8]:
            F('O7 id discrepancy at %s: the retained id is not stored, or does not share the cited prefix' % x['location'])
        else:
            try:
                errata = {y['id']: y for y in json.load(open(os.path.join(root, ERRATA), encoding='utf-8'))['entries']}
            except (OSError, ValueError, KeyError, TypeError):
                errata = {}
            y = errata.get(x.get('erratum'), {})
            if (y.get('location'), y.get('cited_head'), y.get('real_head'), y.get('run_id')) != \
                    (x['location'], x['cited_id'], x['retained_id'], x['run']):
                F('O7 id discrepancy at %s: the erratum %s does not record the same location, ids and run'
                  % (x['location'], x.get('erratum')))
    # O8 ids recorded as missing
    for g in man.get('missing', []):
        gid = g.get('id', '')
        if not re.fullmatch(r'[0-9a-f]{7,40}', gid) or any(o.startswith(gid) for o in ents) or not g.get('cited_at'):
            F('O8 missing id %r is malformed, retained here, or names no citing location' % gid)
            continue
        for loc in g['cited_at']:
            f, _, ln = loc.rpartition(':')
            try:
                line = open(os.path.join(root, f), encoding='utf-8').read().split('\n')[int(ln) - 1]
            except (OSError, ValueError, IndexError):
                line = None
            if line is None or gid[:8] not in line:
                F('O8 missing id %s: %s does not hold it' % (gid[:12], loc))
    # O9 withheld entries: where the retained trees of the commits that list withheld blobs name each one
    occurs = {}
    for c, e in ents.items():
        if e['type'] != 'commit' or c not in content or not e.get('withheld_blobs'):
            continue
        ips = e.get('inclusion_paths') if e['mechanism'] == 'inclusion-proof' else None
        stack = [(commit_fields(content[c])[0], '')]
        while stack:
            t, pre = stack.pop()
            if t not in content or ents[t]['type'] != 'tree':
                continue
            for mode, name, x in tree_entries(content[t]):
                if mode == '40000':
                    stack.append((x, pre + name + '/'))
                elif x in ents and ents[x]['mechanism'] in WITHHELD:
                    path = pre + name
                    if ips is not None and not any(path == ip.rstrip('/') or (ip.endswith('/') and path.startswith(ip))
                                                   for ip in ips):
                        continue
                    occurs.setdefault(x, set()).add((c, path))
    for w, e in sorted(ents.items()):
        if e['mechanism'] not in WITHHELD:
            continue
        occ = occurs.get(w, set())
        if not occ:
            F('O9 withheld %s: no retained tree of a commit that lists withheld blobs names it' % w[:12])
            continue
        if any(w not in ents[c].get('withheld_blobs', []) for c, _ in occ):
            F('O9 withheld %s: a commit whose tree names it does not list it' % w[:12])
        if not e.get('paths') or set(e['paths']) != {p for _, p in occ}:
            F('O9 withheld %s: its recorded paths are not exactly where the retained trees name it' % w[:12])
        elif not all(p.endswith(WITHHELD_SUFFIXES[e['mechanism']]) for p in e['paths']):
            F('O9 withheld %s: a %s entry at a path of another file type' % (w[:12], e['mechanism']))
        if not e.get('needed_by') or any((n.get('object'), n.get('path')) not in occ for n in e['needed_by']):
            F('O9 withheld %s: its needed_by entries are not where the retained trees name it' % w[:12])
        if type(e.get('bytes')) is not int or e['bytes'] <= 0:
            F('O9 withheld %s: it records no size, or a zero size (empty files are stored, not withheld)' % w[:12])
        appr = APPROVED_WITHHELD.get(w)
        if appr is None or appr[:2] != (e['mechanism'], sorted(e.get('paths') or [])):
            F('O9 withheld %s: not withheld as approved (mechanism and exact paths)' % w[:12])
        elif len(appr) > 2:
            # an approval bound to commits: the commits whose trees name the blob are exactly the approved ones, and
            # each withheld instance is recorded with its commit, path, size, blob id, sha256 and reason
            if {c for c, _ in occ} != set(appr[2]):
                F('O9 withheld %s: not withheld as approved (the commits whose trees name it)' % w[:12])
            inst = e.get('instances') or []
            if {(i.get('commit'), i.get('path')) for i in inst} != occ or len(inst) != len(occ) or any(
                    i.get('blob') != w or i.get('bytes') != e.get('bytes') or i.get('sha256') != e.get('content_sha256')
                    or not re.fullmatch(r'[0-9a-f]{64}', str(i.get('sha256'))) or not i.get('reason') for i in inst):
                F('O9 withheld %s: its instances do not record each commit and path with its size, id, sha256 and '
                  'reason' % w[:12])
    for w in sorted(set(APPROVED_WITHHELD) - {o for o, e in ents.items() if e['mechanism'] in WITHHELD}):
        F('O9 approved withheld %s: not withheld here' % w[:12])
    info = {'entries': len(ents), 'stored': len(content), 'external': external, 'man': man, 'ents': ents,
            'content': content, 'incomplete_trees': incomplete_trees, 'citation_states': states}
    return fails, info


def git(args, cwd, inp=None, env=None):
    return subprocess.run(['git'] + args, cwd=cwd, input=inp, capture_output=True, env=env)


class GitFailed(Exception):
    pass


def gitok(args, cwd, inp=None, env=None):
    """Run git and return the completed process; a non-zero exit raises GitFailed, so no check reads empty output."""
    p = git(args, cwd, inp, env)
    if p.returncode:
        raise GitFailed('git %s exited %d: %s' % (' '.join(args[:3]), p.returncode,
                                                  p.stderr.decode('utf-8', 'replace').strip()[:100]))
    return p


def listing(out):
    """(present, missing) ids from a rev-list --objects --missing=print listing."""
    present, missing = set(), set()
    for l in out.decode().split('\n'):
        if l.startswith('?'):
            missing.add(l[1:].split()[0])
        elif l:
            present.add(l.split()[0])
    return present, missing


def base_history(root, base):
    """main's objects and commits, the digests of the addresses in its history, and the objects HEAD reaches."""
    key = (os.path.realpath(root), base, gitok(['rev-parse', 'HEAD'], root).stdout.decode().strip())
    if _HISTORY_MEMO is not None and key in _HISTORY_MEMO:
        return _HISTORY_MEMO[key]
    main_objs = set(l.split()[0] for l in gitok(['rev-list', '--objects', base], root).stdout.decode().split('\n') if l)
    main_commits = set(gitok(['rev-list', base], root).stdout.decode().split())
    log = gitok(['log', '--format=%ae%n%ce%n%B', base], root).stdout.decode('utf-8', 'replace')
    known = {sha256(a.encode()) for a in re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', log)}
    head = set(l.split()[0] for l in gitok(['rev-list', '--objects', 'HEAD'], root).stdout.decode().split('\n') if l)
    if not main_objs or not main_commits or not head:
        raise GitFailed('git returned no objects for the base or HEAD')
    if _HISTORY_MEMO is not None:
        _HISTORY_MEMO[key] = (main_objs, main_commits, known, head)
    return main_objs, main_commits, known, head


def history_checks(root, info, fails, clone_extra=None):
    """H1-H7. clone_extra (self-test only): {type: [content]} written into the temporary repository as if this
    clone held those objects beside the archive; no verdict may depend on them."""
    F = fails.append
    try:
        _history_checks(root, info, fails, clone_extra or {})
    except GitFailed as exc:
        F('H0 %s' % exc)


def _history_checks(root, info, fails, clone_extra):
    F = fails.append
    man, ents, content, external = info['man'], info['ents'], info['content'], info['external']
    base = man['base']
    # each archive tranche has its base: the manifest's for tranche 2, tranche_bases for a later one
    tbases = {str(k): v for k, v in (man.get('tranche_bases') or {}).items()}
    base_of = lambda e: tbases.get(str(e.get('tranche')), base)
    for b in [base] + sorted(set(tbases.values())):
        if git(['cat-file', '-e', b + '^{commit}'], root).returncode or \
                git(['merge-base', '--is-ancestor', b, 'HEAD'], root).returncode:
            F('H1 the base %s is not an ancestor of HEAD in this repository' % b[:12])
            return
    objects = gitok(['rev-parse', '--path-format=absolute', '--git-path', 'objects'], root).stdout.decode().strip()
    deny = set(man.get('excerpt_denylist_sha256_of_id', []))
    withheld = {o for o, e in ents.items() if e['mechanism'] in WITHHELD}
    tmp = tempfile.mkdtemp(prefix='retained-')
    try:
        g = os.path.join(tmp, 'r.git')
        gitok(['init', '-q', '--bare', g], tmp)
        with open(os.path.join(g, 'objects', 'info', 'alternates'), 'w') as fh:
            fh.write(objects + '\n')
        env = dict(os.environ, GIT_DIR=g)

        def write_objects(typ, blobs):
            paths = []
            for i, data in enumerate(blobs):
                pth = os.path.join(tmp, 'w-%s-%d' % (typ, i))
                with open(pth, 'wb') as fh:
                    fh.write(data)
                paths.append(pth)
            p = git(['hash-object', '-w', '-t', typ, '--stdin-paths'], tmp, inp=('\n'.join(paths) + '\n').encode(), env=env)
            for pth in paths:
                os.remove(pth)
            return p
        # H2: git, not this script, computes each id (hash-object also checks a commit's and a tree's format)
        for typ in ('blob', 'tree', 'commit'):
            oids = sorted(o for o in content if ents[o]['type'] == typ)
            if not oids:
                continue
            p = write_objects(typ, [content[o] for o in oids])
            got = p.stdout.decode().split()
            if p.returncode or got != oids:
                bad = next((o for o, x in zip(oids, got) if o != x), oids[len(got)] if len(got) < len(oids) else '?')
                F('H2 git does not write %s %s with its id: %s' % (typ, bad[:12], p.stderr.decode().strip()[:80]))
                return
        for typ, blobs in sorted(clone_extra.items()):
            if write_objects(typ, blobs).returncode:
                raise GitFailed('the self-test could not stage a clone-held %s' % typ)
        per_base = {b: base_history(root, b) for b in [base] + sorted(set(tbases.values()))}
        main_objs, main_commits, known, head = per_base[base]
        for b, (o2, c2, k2, _) in per_base.items():
            if b != base:
                # main at a later tranche's base contains main at the first base (H1 orders both before HEAD)
                main_objs, main_commits, known = main_objs | o2, main_commits | c2, known | k2
        # what the archive or main holds: every verdict below is relative to this, never to what the clone holds
        held = set(content) | main_objs
        # H7: nothing listed here is already on main at its own tranche's base
        for o in sorted(ents):
            if o in per_base[base_of(ents[o])][0]:
                F('H7 %s (%s) is reachable from the base, so it is not off-main' % (o[:12], ents[o]['mechanism']))
        for mg in man.get('missing', []):
            gid = mg.get('id', '')
            if gid and any(x.startswith(gid) for x in main_objs):
                F('H7 missing id %s names an object reachable from the base' % gid[:12])
        # H3: what the retained objects name and do not retain is on main
        for x in sorted(external):
            if x not in main_objs:
                F('H3 %s is named by a retained object, is neither retained nor withheld, and is not on main' % x[:12])
        for c, e in ents.items():
            if e['type'] != 'commit' or c not in content:
                continue
            for par in commit_fields(content[c])[1]:
                named = par in e.get('parents_not_retained', [])
                if par not in ents and not named and par not in main_commits:
                    F('H3 %s: parent %s is neither retained, nor on main, nor named' % (c[:12], par[:12]))
                if named and par in main_commits:
                    F('H3 %s: parent %s is named as not retained but is on main' % (c[:12], par[:12]))
        if any(f.startswith('H3') for f in fails):
            return
        # H4: connectivity, relative to the archive and main. A ref at every raw:connected and raw:tree commit and
        # every complete cited tree, every raw:tree commit a shallow boundary so nothing walks past it.
        refs = sorted(o for o, e in ents.items() if o in content and (e['mechanism'] in ('raw:connected', 'raw:tree') or
                                                                       (e['type'] == 'tree' and e.get('cited') and
                                                                        o not in info['incomplete_trees'])))
        gitok(['update-ref', '--stdin'], tmp, inp=''.join('create refs/retained/%s %s\n' % (o, o) for o in refs).encode(),
              env=env)
        made = gitok(['for-each-ref', '--format=%(objectname)', 'refs/retained/'], tmp, env=env).stdout.decode().split()
        if sorted(made) != refs:
            F('H4 %d of %d refs were created in the temporary repository' % (len(made), len(refs)))
            return
        shallow = sorted(o for o, e in ents.items() if e['mechanism'] == 'raw:tree' and o in content)
        with open(os.path.join(g, 'shallow'), 'w') as fh:
            fh.write(''.join(x + '\n' for x in shallow))
        fs = git(['fsck', '--connectivity-only', '--no-dangling', '--no-progress'], tmp, env=env)
        if fs.returncode:
            msg = [l for l in (fs.stdout + fs.stderr).decode('utf-8', 'replace').split('\n')
                   if l.strip() and not l.startswith('notice:')]
            F('H4 git fsck --connectivity-only fails: %s' % (msg or ['(no message)'])[0][:120])
        # everything the refs reach is held by the archive or main; an object only this clone holds, or one no store
        # holds, fails, whichever it is
        reached, gone = listing(gitok(['rev-list', '--objects', '--missing=print', '--all'], tmp, env=env).stdout)
        for x in sorted((reached | gone) - held):
            F('H4 %s is reached from the retained refs but neither the archive nor main holds it%s'
              % (x[:12], ' (this clone does)' if x in reached else ''))
            break
        for o, e in sorted(ents.items()):
            if e['mechanism'] == 'raw:connected':
                out = gitok(['rev-list', o, '--not', base], tmp, env=env).stdout.decode().split()
                stray = [x for x in out if x not in ents or ents[x]['mechanism'] != 'raw:connected']
                if stray:
                    F('H4 %s: raw:connected, but its history leaves main through %s' % (o[:12], stray[0][:12]))
            if e['mechanism'] == 'raw:partial-tree' and o in content:
                pres, miss = listing(gitok(['rev-list', '--objects', '--no-walk', '--missing=print', o], tmp,
                                           env=env).stdout)
                if sorted((pres | miss) - held) != sorted(e.get('withheld_blobs', [])):
                    F('H4 %s: what its tree names beyond the archive and main is not exactly its withheld blobs' % o[:12])
            if e['mechanism'] == 'inclusion-proof':
                beyond = set()
                for pth in e.get('inclusion_paths', []):
                    r = git(['rev-parse', '--verify', '-q', '%s:%s' % (o, pth.rstrip('/'))], tmp, env=env)
                    tip = r.stdout.decode().strip()
                    if r.returncode or tip not in set(content) | withheld:
                        F('H4 %s: %s does not resolve to a retained or withheld object' % (o[:12], pth))
                    elif tip in withheld:
                        beyond.add(tip)
                    elif ents[tip]['type'] == 'tree':
                        pres, miss = listing(gitok(['rev-list', '--objects', '--missing=print', tip], tmp,
                                                   env=env).stdout)
                        beyond |= (pres | miss) - held
                if sorted(beyond) != sorted(e.get('withheld_blobs', [])):
                    F('H4 %s: what its inclusion paths name beyond the archive and main is not exactly its withheld '
                      'blobs' % o[:12])
        # H5: identities are addresses already public in main's history
        for d in man.get('identities_sha256', []):
            if d not in known:
                F('H5 identity digest %s names no address in the base\'s history' % d[:12])
        # H6: no excerpt reachable from HEAD, or from anything reconstituted
        for name, lst in (('HEAD of this repository', head), ('the reconstituted objects', reached | gone)):
            hit = sorted(x for x in lst if sha256(x.encode()) in deny)
            if hit:
                F('H6 %d deny-listed (excerpt) object(s) reachable from %s, first %s' % (len(hit), name, hit[0][:12]))
        info['reconstituted'] = {'refs': len(made), 'shallow_boundaries': len(shallow)}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


class Fails(list):
    pass


def check_with(objdir, root, history, fails):
    res, info = check(objdir, root)
    fails.extend(res)
    if history and not fails and info:
        history_checks(root, info, fails)
    return fails, info


def self_test(root):
    """Mutate a copy once per failure family, in both directions: the copy passes, each mutation fails as named."""
    global _SCAN_MEMO, _HISTORY_MEMO
    tmp = tempfile.mkdtemp(prefix='objects-selftest-')
    results = []
    _SCAN_MEMO, _HISTORY_MEMO = {}, {}
    try:
        base = os.path.join(tmp, 'objects')
        shutil.copytree(OBJ, base)
        man0 = json.load(open(os.path.join(base, 'manifest.json')))

        def fresh():
            d = os.path.join(tmp, 'case')
            if os.path.isdir(d):
                shutil.rmtree(d)
            shutil.copytree(base, d)
            return d

        def save(d, man):
            json.dump(man, open(os.path.join(d, 'manifest.json'), 'w'), indent=1, sort_keys=True)

        def pick(pred):
            return next(e for e in man0['objects'] if pred(e))

        def expect(name, mutate, rule, history=False):
            d = fresh()
            mutate(d)
            fails, _ = check_with(d, root, history, Fails())
            ok = any(f.startswith(rule) for f in fails)
            results.append((name, rule, 'FAILS as required' if ok else 'NOT DETECTED', fails[:1]))

        def flip(d, rel):
            p = os.path.join(d, rel)
            b = bytearray(open(p, 'rb').read())
            b[len(b) // 2] ^= 0x01
            open(p, 'wb').write(bytes(b))

        def new_blob(d, man, data, cited=None):
            oid = git_id('blob', data)
            rel = 'blob/%s/%s' % (oid[:2], oid)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            man['objects'].append({'oid': oid, 'type': 'blob', 'mechanism': 'byte-copy', 'form': 'raw', 'file': rel,
                                   'bytes': len(data), 'sha256': sha256(data), 'tranche': 1})
            return oid

        for hist in (False, True):
            fails, info = check_with(base, root, hist, Fails())
            results.append(('unmutated copy (%s mode)' % ('history' if hist else 'tree'), '-',
                            'PASSES as required' if not fails else 'FAILS', fails[:3]))
        rawblob = pick(lambda e: e.get('form') == 'raw' and e['type'] == 'blob' and e.get('bytes', 0) > 0)
        rawcommit = pick(lambda e: e.get('form') == 'raw' and e['type'] == 'commit')
        ztree = pick(lambda e: e.get('form') == 'zlib' and e['type'] == 'tree' and not e.get('cited'))
        zblob = pick(lambda e: e.get('form') == 'zlib' and e['type'] == 'blob')
        expect('a corrupted byte in a raw blob', lambda d: flip(d, rawblob['file']), 'O1')
        expect('a corrupted byte in a raw commit', lambda d: flip(d, rawcommit['file']), 'O1')
        expect('a corrupted byte in a zlib tree', lambda d: flip(d, ztree['file']), 'O1')
        expect('a corrupted byte in a zlib blob', lambda d: flip(d, zblob['file']), 'O1')

        def drop_file(d):
            os.remove(os.path.join(d, ztree['file']))
        expect('a missing object file (entry kept)', drop_file, 'O1')

        def drop_object(d):
            os.remove(os.path.join(d, ztree['file']))
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['objects'] = [e for e in man['objects'] if e['oid'] != ztree['oid']]
            save(d, man)
        expect('a missing object (file and entry removed)', drop_object, 'H3', history=True)

        def unlisted(d):
            open(os.path.join(d, 'blob', 'stray'), 'wb').write(b'x\n')
        expect('an unlisted file', unlisted, 'O2')

        def on_main(d):
            # the base's root tree, stored as a fully retained tree: well formed, and on main
            man = json.load(open(os.path.join(d, 'manifest.json')))
            tree = git(['rev-parse', man['base'] + '^{tree}'], root).stdout.decode().strip()
            data = git(['cat-file', 'tree', tree], root).stdout
            rel = 'tree/%s/%s' % (tree[:2], tree)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            man['objects'].append({'oid': tree, 'type': 'tree', 'mechanism': 'raw', 'form': 'raw', 'file': rel,
                                   'bytes': len(data), 'sha256': sha256(data), 'tranche': 2})
            save(d, man)
        expect('an object already on main, stored here', on_main, 'H7', history=True)

        def deny_stored(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['excerpt_denylist_sha256_of_id'].append(sha256(rawblob['oid'].encode()))
            save(d, man)
        expect('an injected excerpt: a stored blob whose id is deny-listed', deny_stored, 'O5')

        def deny_named(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            data = zlib.decompress(open(os.path.join(d, ztree['file']), 'rb').read()).partition(b'\0')[2]
            man['excerpt_denylist_sha256_of_id'].append(sha256(tree_entries(data)[0][2].encode()))
            save(d, man)
        expect('an injected excerpt: a retained tree that names a deny-listed id', deny_named, 'O5')

        def excerpt_new(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            oid = new_blob(d, man, b'synthetic excerpt stand-in\n')
            man['excerpt_denylist_sha256_of_id'].append(sha256(oid.encode()))
            save(d, man)
        expect('an injected excerpt: a new stored blob on the deny-list', excerpt_new, 'O5')

        def excerpt_head(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            # a blob reachable from HEAD that no retained object names: this checker's own committed blob
            own = git(['rev-parse', 'HEAD:verification/audits/evidence-retention/check_objects.py'], root).stdout.decode().strip()
            man['excerpt_denylist_sha256_of_id'].append(sha256(own.encode()))
            save(d, man)
        expect('an injected excerpt: a deny-listed blob reachable from HEAD', excerpt_head, 'H6', history=True)

        def secret(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            new_blob(d, man, b'token = ghp_' + b'A' * 36 + b'\n')
            save(d, man)
        expect('a secret pattern in a stored blob', secret, 'O6')

        def email(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            new_blob(d, man, b'contact someone' + b'@' + b'example-corp.io\n')
            save(d, man)
        expect('an e-mail address in a stored blob', email, 'O6')

        def ident(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'] = man['identities_sha256'][1:]
            save(d, man)
        expect('a commit identity whose digest is not listed', ident, 'O6')

        def fake_ident(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'].append(sha256(b'nobody' + b'@' + b'nowhere.invalid'))
            save(d, man)
        expect('a listed identity absent from main\'s history', fake_ident, 'H5', history=True)

        def relabel(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e['mechanism'] == 'raw:tree')
            e['mechanism'] = 'raw:connected'
            e.pop('parents_not_retained', None)
            save(d, man)
        expect('a raw:tree commit relabelled raw:connected', relabel, 'O4')

        def drop_withheld(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e['mechanism'] == 'raw:partial-tree')
            e['withheld_blobs'] = e['withheld_blobs'][1:]
            save(d, man)
        expect('a withheld blob dropped from its commit\'s list', drop_withheld, 'O4')

        def cite(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(e for e in man['objects'] if e.get('cited'))
            e['cited'][0]['tokens'] = ['f' * 12]
            e['cited'][0].pop('run', None)
            save(d, man)
        expect('a citation whose line lacks its token', cite, 'O7')

        def discrepancy(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['id_discrepancies'][0]['retained_id'] = rawcommit['oid']
            save(d, man)
        expect('an id discrepancy mapped to another commit', discrepancy, 'O7')

        def erratum(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            x = man['id_discrepancies'][0]
            x['erratum'] = next(y['erratum'] for y in man['id_discrepancies'] if y['erratum'] != x['erratum'])
            save(d, man)
        expect('an id discrepancy that names another erratum', erratum, 'O7')

        def missing_moved(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            g = man['missing'][0]
            f, _, ln = g['cited_at'][0].rpartition(':')
            g['cited_at'][0] = '%s:%d' % (f, int(ln) + 1)
            save(d, man)
        expect('a missing id whose citing line does not hold it', missing_moved, 'O8')

        def missing_retained(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['missing'][0]['id'] = rawcommit['oid']
            man['missing'][0]['cited_at'] = [c['location'] for c in rawcommit.get('cited', [])][:1] or \
                man['missing'][0]['cited_at']
            save(d, man)
        expect('a missing id that is retained here', missing_retained, 'O8')
        def bad_mechanism(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            next(e for e in man['objects'] if e['oid'] == rawcommit['oid'])['mechanism'] = 'byte-copy'
            save(d, man)
        expect('a commit entry with a blob\'s mechanism', bad_mechanism, 'O3')

        def bad_digest(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['identities_sha256'].append('not-a-digest')
            save(d, man)
        expect('an identity digest that is not a sha256 digest', bad_digest, 'O3')

        def unknown_base(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['base'] = 'f' * 40
            save(d, man)
        expect('a base this repository does not hold', unknown_base, 'H1', history=True)

        def malformed_commit(d):
            # well formed for tree mode, but git's own format check refuses it: it has no committer line
            man = json.load(open(os.path.join(d, 'manifest.json')))
            data = b'tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\nauthor A <a> 0 +0000\n\nno committer\n'
            oid = git_id('commit', data)
            rel = 'commit/%s/%s' % (oid[:2], oid)
            os.makedirs(os.path.join(d, os.path.dirname(rel)), exist_ok=True)
            open(os.path.join(d, rel), 'wb').write(data)
            # uncited, so it names a record to cite it (O10), and only git's format check (H2) can refuse it
            man['objects'].append({'oid': oid, 'type': 'commit', 'mechanism': 'identity-anchor', 'form': 'raw',
                                   'file': rel, 'bytes': len(data), 'sha256': sha256(data), 'parents': [],
                                   'awaiting_citation': {'pull_request': 1, 'round': 'SELF-TEST', 'record': 'x.md'},
                                   'tranche': 2})
            save(d, man)
        expect('a commit git refuses as malformed', malformed_commit, 'H2', history=True)

        # H4 re-derives connectivity with git. Tree mode (O4) already rejects these states, so each case changes
        # the checked state after tree mode passes, and shows H4 rejects it on its own. clone_extra writes objects
        # into the temporary repository as if this clone held them beside the archive.
        def expect_history(name, mutate, rule):
            fails, info = check(base, root)
            if fails:
                results.append((name, rule or '-', 'FAILS in tree mode', fails[:1]))
                return
            extra = mutate(info) or {}
            hf = Fails()
            history_checks(root, info, hf, extra)
            if rule is None:
                results.append((name, '-', 'PASSES as required' if not hf else 'FAILS', hf[:3]))
            else:
                ok = any(f.startswith(rule) for f in hf)
                results.append((name, rule, 'FAILS as required' if ok else 'NOT DETECTED', hf[:1]))

        part = next(e for e in man0['objects'] if e['mechanism'] == 'raw:partial-tree')
        conn = {e['oid'] for e in man0['objects'] if e['mechanism'] == 'raw:connected'}
        under_conn = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('form') == 'zlib' and
                          not e.get('cited') and e.get('needed_by') and
                          all(n['object'] in conn for n in e['needed_by']))
        under_part = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                          not e.get('cited') and [n['object'] for n in e.get('needed_by', [])] == [part['oid']])

        def drop_needed(info):
            del info['content'][under_conn['oid']]
        expect_history('a required stored object dropped from the archive', drop_needed, 'H4')

        def drop_needed_clone_holds(info):
            data = info['content'].pop(under_conn['oid'])
            return {'blob': [data]}
        expect_history('a required object missing from the archive but held by this clone',
                       drop_needed_clone_holds, 'H4')

        def short_withheld(info):
            info['ents'][part['oid']]['withheld_blobs'] = info['ents'][part['oid']]['withheld_blobs'][1:]
        expect_history('a partial tree whose withheld list omits one of its blobs', short_withheld, 'H4')

        def withheld_clone_holds(info):
            # a blob of the partial tree, withheld from the archive, that this clone happens to hold
            data = info['content'].pop(under_part['oid'])
            info['ents'][under_part['oid']] = dict(info['ents'][under_part['oid']], mechanism='withheld:raw-log')
            info['ents'][part['oid']]['withheld_blobs'] = sorted(info['ents'][part['oid']]['withheld_blobs'] +
                                                                 [under_part['oid']])
            return {'blob': [data]}
        expect_history('a withheld blob that this clone holds', withheld_clone_holds, None)

        incl = next(e for e in man0['objects'] if e['mechanism'] == 'inclusion-proof' and e.get('withheld_blobs'))
        under_incl = next(e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                          [n['object'] for n in e.get('needed_by', [])] == [incl['oid']])

        def incl_relabel(d):
            # a retained blob under an inclusion path deleted, its entry turned into a withheld one
            man = json.load(open(os.path.join(d, 'manifest.json')))
            os.remove(os.path.join(d, under_incl['file']))
            e = next(x for x in man['objects'] if x['oid'] == under_incl['oid'])
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=under_incl['content_bytes'],
                     paths=[under_incl['needed_by'][0]['path']])
            save(d, man)
        expect('a blob under an inclusion path dropped and relabelled withheld', incl_relabel, 'O4')

        def orphan_withheld(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            man['objects'].append({'oid': 'f' * 40, 'type': 'blob', 'mechanism': 'withheld:raw-log', 'bytes': 1,
                                   'paths': ['x.log'], 'needed_by': [{'object': part['oid'], 'path': 'x.log'}],
                                   'tranche': 2})
            save(d, man)
        expect('a withheld entry that no retained tree names', orphan_withheld, 'O9')

        def withheld_path(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(x for x in man['objects'] if x['mechanism'] in WITHHELD)
            e['paths'] = [e['paths'][0] + '.moved']
            save(d, man)
        expect('a withheld entry whose recorded path is not where it is named', withheld_path, 'O9')

        def relabel_listed(d):
            # a stored blob of the partial tree deleted, relabelled a raw log and added to its commit's list
            man = json.load(open(os.path.join(d, 'manifest.json')))
            os.remove(os.path.join(d, under_part['file']))
            e = next(x for x in man['objects'] if x['oid'] == under_part['oid'])
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=under_part['content_bytes'],
                     paths=[under_part['needed_by'][0]['path']])
            c = next(x for x in man['objects'] if x['oid'] == part['oid'])
            c['withheld_blobs'] = sorted(c['withheld_blobs'] + [under_part['oid']])
            save(d, man)
        expect('a stored blob relabelled a raw log, with its commit\'s list edited to match', relabel_listed, 'O9')

        def empty_relabelled(d):
            # the empty blob, stored at log-type paths, deleted and withheld with both commits' lists edited to match
            man = json.load(open(os.path.join(d, 'manifest.json')))
            e = next(x for x in man['objects'] if x['oid'] == 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
            os.remove(os.path.join(d, e['file']))
            paths = ['research/a42-rerun/quarantine/r5.log', 'research/round7-channel/channel_check.replay.err',
                     'research/round7-channel/channel_check.run1.err',
                     'research/round7-channel/native-controls.selftest.final.err']
            for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                e.pop(k, None)
            e.update(mechanism='withheld:raw-log', bytes=1, paths=paths)
            for c in man['objects']:
                if c['oid'] in {n['object'] for n in e['needed_by']}:
                    c['withheld_blobs'] = sorted(set(c.get('withheld_blobs', [])) | {e['oid']})
            save(d, man)
        expect('a stored log-type blob withheld, with the manifest and lists edited to match', empty_relabelled, 'O9')

        def as_pdf(d):
            man = json.load(open(os.path.join(d, 'manifest.json')))
            next(x for x in man['objects'] if x['mechanism'] == 'withheld:raw-log')['mechanism'] = 'withheld:build-pdf'
            save(d, man)
        expect('a raw log relabelled a build output', as_pdf, 'O9')

        def git_fails(info):
            return {'commit': [b'not a commit\n']}
        expect_history('a git command that fails while staging objects', git_fails, 'H0')

        def bad_incl_path(info):
            info['ents'][incl['oid']]['inclusion_paths'] = info['ents'][incl['oid']]['inclusion_paths'] + ['no/such']
        expect_history('an inclusion path that does not resolve', bad_incl_path, 'H4')

        def short_incl_withheld(info):
            info['ents'][incl['oid']]['withheld_blobs'] = info['ents'][incl['oid']]['withheld_blobs'][1:]
        expect_history('an inclusion proof whose withheld list omits one of its blobs', short_incl_withheld, 'H4')

        def missing_on_main(info):
            info['man'] = dict(info['man'], missing=[dict(info['man']['missing'][0], id=info['man']['base'][:12])])
        expect_history('a missing id that names an object on main', missing_on_main, 'H7')

        # archive tranche 4: withholding bound to exact paths and commits, the base per tranche, pending citations
        bound = sorted(w for w, a in APPROVED_WITHHELD.items() if len(a) > 2)
        third = next((e for e in man0['objects'] if e['type'] == 'blob' and e.get('file') and
                      e.get('needed_by') and all(n['path'].endswith('.txt') for n in e['needed_by']) and
                      all(next(x for x in man0['objects'] if x['oid'] == n['object'])['mechanism'] == 'raw:partial-tree'
                          for n in e['needed_by'])), None)
        uncited = next((e for e in man0['objects'] if e['type'] == 'commit' and not e.get('cited')), None)
        t2raw = next((e for e in man0['objects'] if e['type'] == 'blob' and e.get('form') == 'raw' and e.get('tranche') == 2),
                     None)
        if not bound or third is None or uncited is None or t2raw is None or 'tranche_bases' not in man0:
            results.append(('the tranche-4 cases need a commit-bound approval, a stored .txt under a partial tree, an '
                            'uncited commit, a tranche-2 raw blob and tranche bases', '-', 'NOT DETECTED', []))
        else:
            def third_txt(d):
                # a third .txt, stored under a partial tree: deleted, relabelled a raw output, its commit's list and
                # the manifest edited to match; the checker's approved list does not name it
                man = json.load(open(os.path.join(d, 'manifest.json')))
                os.remove(os.path.join(d, third['file']))
                e = next(x for x in man['objects'] if x['oid'] == third['oid'])
                for k in ('file', 'form', 'sha256', 'content_sha256', 'content_bytes', 'cited'):
                    e.pop(k, None)
                e.update(mechanism='withheld:raw-output', bytes=third['content_bytes'],
                         paths=sorted({n['path'] for n in third['needed_by']}))
                for c in man['objects']:
                    if c['oid'] in {n['object'] for n in third['needed_by']}:
                        c['withheld_blobs'] = sorted(set(c['withheld_blobs']) | {third['oid']})
                save(d, man)
            expect('a third, unlisted .txt withheld, with the manifest and its commit\'s list edited to match', third_txt,
                   'O9')

            def one_commit(d):
                # the approval narrowed to one of the two commits whose trees name the blob
                w = bound[0]
                APPROVED_WITHHELD[w] = APPROVED_WITHHELD[w][:2] + (APPROVED_WITHHELD[w][2][:1],)
            saved = dict(APPROVED_WITHHELD)
            try:
                expect('an approved .txt withheld in a commit its approval does not name', one_commit, 'O9')
            finally:
                APPROVED_WITHHELD.clear()
                APPROVED_WITHHELD.update(saved)

            def instance_sha(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                e = next(x for x in man['objects'] if x['oid'] == bound[0])
                e['instances'][0]['sha256'] = '0' * 64
                save(d, man)
            expect('a withheld instance whose sha256 is not the recorded one', instance_sha, 'O9')

            def instance_dropped(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                e = next(x for x in man['objects'] if x['oid'] == bound[0])
                e['instances'] = e['instances'][1:]
                save(d, man)
            expect('a withheld instance not recorded', instance_dropped, 'O9')

            def no_awaiting(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                next(x for x in man['objects'] if x['oid'] == uncited['oid']).pop('awaiting_citation')
                save(d, man)
            expect('an uncited commit that names no record to cite it', no_awaiting, 'O10')

            def awaiting_no_round(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                next(x for x in man['objects'] if x['oid'] == uncited['oid'])['awaiting_citation'].pop('round')
                save(d, man)
            expect('a pending citation without its round', awaiting_no_round, 'O10')

            def bad_bases(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                man['tranche_bases'] = {'4': 'main'}
                save(d, man)
            expect('a tranche base that is not a commit id', bad_bases, 'O3')

            def base_off_head(d):
                man = json.load(open(os.path.join(d, 'manifest.json')))
                man['tranche_bases'] = {'4': uncited['oid']}
                save(d, man)
            expect('a tranche base that is not an ancestor of HEAD', base_off_head, 'H1', history=True)

            def on_tranche_base(d):
                # a tranche-2 blob stored as a plain file, which main reaches from the later base, counted as tranche 4
                man = json.load(open(os.path.join(d, 'manifest.json')))
                next(x for x in man['objects'] if x['oid'] == t2raw['oid'])['tranche'] = 4
                save(d, man)
            expect('an object its own tranche\'s base already reaches', on_tranche_base, 'H7', history=True)

        # O10, the citation lifecycle, on a stand-in for a pending entry's record. Each case checks a copy against a
        # root that shows this repository through symlinks except along the record's directory, where the stand-in
        # is written or left out; nothing is written to this repository.
        pend = next((e for e in man0['objects'] if (e.get('awaiting_citation') or {}).get('run')), None)
        if pend is None:
            results.append(('the citation-lifecycle cases need a pending entry that names its run', '-', 'NOT DETECTED',
                            []))
        else:
            oid, aw = pend['oid'], pend['awaiting_citation']
            rec, rid = aw['record'], aw['run']
            other = hashlib.sha1(b'another commit ' + oid.encode()).hexdigest()
            # the stand-in also cites every other entry pending on the same record, as the landed record must
            siblings = ''.join('- `%s`: another head, run %s.\n' % (x['oid'], x['awaiting_citation'].get('run', ''))
                               for x in man0['objects'] if x['oid'] != oid and
                               (x.get('awaiting_citation') or {}).get('record') == aw['record'])
            stand_in = lambda c, r: ('# a stand-in for the record of %s as it lands on main\n\n'
                                     '- `%s`: the design-run head.\n'
                                     '- The workflow was dispatched on exactly that head: run %s, `head_sha` `%s…`.\n'
                                     % (aw['round'], c, r, c[:8])) + siblings
            good = stand_in(oid, rid)
            n1, n2 = 3, 4

            def overlay(text, extra=None):
                t = os.path.join(tmp, 'root')
                if os.path.isdir(t):
                    shutil.rmtree(t)
                os.makedirs(t)
                src, dst = root, t
                for part in rec.split('/'):
                    for nm in (os.listdir(src) if os.path.isdir(src) else []):
                        if nm != part:
                            os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
                    if part == rec.split('/')[-1]:
                        break
                    src, dst = os.path.join(src, part), os.path.join(dst, part)
                    os.makedirs(dst)
                if text is not None:
                    open(os.path.join(t, rec), 'w', encoding='utf-8').write(text)
                for rel, body in (extra or {}).items():
                    open(os.path.join(t, rel), 'w', encoding='utf-8').write(body)
                return t

            def promoted(m, toks=None, run=None):
                x = next(y for y in m['objects'] if y['oid'] == oid)
                x.pop('awaiting_citation')
                x['cited'] = [{'class': 'native-record', 'location': '%s:%d' % (rec, n1), 'role': 'other:design-run',
                               'tokens': toks or [oid], 'via': 'token'},
                              {'class': 'native-record', 'location': '%s:%d' % (rec, n2), 'role': 'run-head',
                               'run': run or rid, 'tokens': [oid[:8]], 'via': 'run'}]

            def pending_edit(**kw):
                def fn(m):
                    next(y for y in m['objects'] if y['oid'] == oid)['awaiting_citation'].update(kw)
                return fn

            def expect_cite(name, text, edit_man, rule, state=None, extra=None, msg=''):
                d = fresh()
                if edit_man:
                    m = json.load(open(os.path.join(d, 'manifest.json')))
                    edit_man(m)
                    save(d, m)
                fails, info = check(d, overlay(text, extra))
                got = (info.get('citation_states') or {}).get(oid, ('failing',))[0]
                if rule is None:
                    ok = not fails and got == state
                    results.append((name, '-', 'PASSES as required' if ok else 'FAILS',
                                    fails[:1] or ['O10 state %s, not %s' % (got, state)] if not ok else []))
                else:
                    ok = any(f.startswith(rule) and msg in f for f in fails)
                    results.append((name, rule, 'FAILS as required' if ok else 'NOT DETECTED', fails[:1]))
                return info

            # (a)-(e): the record absent, then landed with the manifest unchanged, then the entry promoted; a record
            # that cites another commit; the record removed under a promoted entry
            expect_cite('lifecycle (a): the record not in the tree, the entry pending', None, None, None, 'pending')
            info_b = expect_cite('lifecycle (b): the record lands citing the id and run, the manifest unchanged (eligible)',
                                 good, None, None, 'eligible')
            expect_cite('lifecycle (c): the entry promoted to the record\'s two lines, which O7 verifies', good,
                        promoted, None, 'cited')
            expect_cite('lifecycle (d): the record lands citing another commit id', stand_in(other, rid), None, 'O10',
                        msg='does not cite it')
            expect_cite('lifecycle (e): the record removed while the entry is cited', None, promoted, 'O7',
                        msg='does not exist')
            # the object checks do not read the citation's state: history mode passes with the citation eligible
            hf = Fails()
            if info_b.get('citation_states', {}).get(oid, ('',))[0] == 'eligible':
                history_checks(root, info_b, hf)
            results.append(('history mode with the record landed and the citation still pending (eligible)', '-',
                            'PASSES as required' if not hf and info_b.get('citation_states') else 'FAILS', hf[:1]))
            # a pull request is never evidence: the id cited in a file that is not the named record leaves it pending
            expect_cite('the id cited in another file than the named record: still pending', None, None, None, 'pending',
                        extra={os.path.dirname(rec) + '/ZZ-OTHER.md': good})
            expect_cite('a pending entry that also carries cited', good,
                        lambda m: next(y for y in m['objects'] if y['oid'] == oid).__setitem__(
                            'cited', [{'location': '%s:%d' % (rec, n1), 'tokens': [oid]}]), 'O10', msg='together')
            expect_cite('a pending entry that carries an empty cited list', None,
                        lambda m: next(y for y in m['objects'] if y['oid'] == oid).__setitem__('cited', []), 'O10',
                        msg='together')
            expect_cite('the record lands citing the id beside another run', stand_in(oid, '1' + rid), None, 'O10',
                        msg='does not name run %s' % rid)
            expect_cite('the record lands on other lines than the entry records', good, pending_edit(lines=[n1 + 10]),
                        'O10', msg='not on the recorded')
            expect_cite('the record lands on exactly the lines the entry records', good, pending_edit(lines=[n1, n2]),
                        None, 'eligible')
            expect_cite('the record lands without the id form the entry records', good,
                        pending_edit(tokens=[oid[:12]]), 'O10', msg='does not cite it as')
            expect_cite('a pending entry that records another commit\'s id as its form', None,
                        pending_edit(tokens=[other[:8]]), 'O10', msg='malformed')
            ci_other = None
            for r in sorted(os.listdir(os.path.join(HERE, 'ci'))) if os.path.isdir(os.path.join(HERE, 'ci')) else []:
                p = os.path.join(HERE, 'ci', r, 'run.json')
                if os.path.isfile(p) and json.load(open(p, encoding='utf-8')).get('head_sha') not in (None, oid):
                    ci_other = r
                    break
            if ci_other is None:
                results.append(('a pending entry that names a retained run of another head needs such a run', '-',
                                'NOT DETECTED', []))
            else:
                expect_cite('a pending entry that names a retained run of another head', None, pending_edit(run=ci_other),
                            'O10', msg='whose head')
            expect_cite('a pending record inside the archive', None,
                        pending_edit(record=ARCHIVE_REL + '/x.md'), 'O10', msg='malformed')
            # after promotion, O7: a recorded run not on the line, a hex token of another commit on the line
            expect_cite('a promoted citation that records another run', good, lambda m: promoted(m, run='1' + rid),
                        'O7', msg='does not hold its run')
            expect_cite('a promoted citation that records another commit\'s id the line also holds',
                        good.replace('the design-run head', 'the design-run head, not `%s`' % other),
                        lambda m: promoted(m, toks=[other]), 'O7', msg='not a prefix of its id')
    finally:
        _SCAN_MEMO = _HISTORY_MEMO = None
        shutil.rmtree(tmp, ignore_errors=True)
    width = max(len(r[0]) for r in results)
    bad = 0
    for name, rule, verdict, f in results:
        print('  %-*s  %-3s  %s%s' % (width, name, rule, verdict, ('  [' + f[0][:90] + ']') if f else ''))
        bad += verdict not in ('FAILS as required', 'PASSES as required')
    print('self-test: %s (%d cases)' % ('OK' if not bad else 'FAILED', len(results)))
    return 1 if bad else 0


def materialize(root, info):
    """Write every stored object into this repository's object store (adds objects only; no ref changes), so that
    tools that need a retained commit in the repository, such as reproduce.py, can check it out."""
    tmp = tempfile.mkdtemp(prefix='materialize-')
    try:
        for typ in ('blob', 'tree', 'commit'):
            oids = sorted(o for o in info['content'] if info['ents'][o]['type'] == typ)
            paths = []
            for o in oids:
                pth = os.path.join(tmp, o)
                with open(pth, 'wb') as fh:
                    fh.write(info['content'][o])
                paths.append(pth)
            p = git(['hash-object', '-w', '-t', typ, '--stdin-paths'], root, inp=('\n'.join(paths) + '\n').encode())
            if p.returncode or p.stdout.decode().split() != oids:
                print('FAIL  materialize: git did not write every %s with its id' % typ)
                return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print('materialized: %d objects written to this repository\'s object store' % len(info['content']))
    return 0


def main(argv):
    if '--self-test' in argv:
        return self_test(ROOT)
    history = '--reconstitute' in argv or '--materialize' in argv
    fails, info = check_with(OBJ, ROOT, history, Fails())
    if '--materialize' in argv and not fails:
        if materialize(ROOT, info):
            return 1
    for f in fails:
        print('FAIL  ' + f)
    if info:
        n = info['man']['objects']
        print('objects: %d entries, %d stored and verified, %d withheld, %d ids expected on main%s'
              % (len(n), info['stored'], sum(1 for e in n if e['mechanism'] in WITHHELD), len(info['external']),
                 ' (verified)' if history and not fails else ''))
        if info.get('reconstituted'):
            print('reconstituted: %(refs)d refs, %(shallow_boundaries)d raw:tree commits as shallow boundaries; fsck --connectivity-only clean' % info['reconstituted'])
        by = {}
        for e in n:
            by[e['mechanism']] = by.get(e['mechanism'], 0) + 1
        print('mechanisms: ' + ', '.join('%s %d' % kv for kv in sorted(by.items())))
        named = sorted({p for e in n for p in e.get('parents_not_retained', [])})
        print('parents named, not retained (%d): %s' % (len(named), ' '.join(p[:12] for p in named)))
        part = [e for e in n if e['mechanism'] == 'raw:partial-tree']
        print('partial trees (%d): %s' % (len(part), ', '.join('%s withholds %d' % (e['oid'][:12], len(e['withheld_blobs']))
                                                          for e in part)))
        st = info.get('citation_states', {})
        count = lambda s: sum(1 for v in st.values() if v[0] == s)
        print('citations (O10): %d cited, %d pending (record not in the tree), %d eligible for promotion'
              % (count('cited'), count('pending'), count('eligible')))
        for o, (s, where) in sorted(st.items()):
            a = info['ents'][o].get('awaiting_citation') or {}
            if s == 'pending':
                print('  pending   %s  #%s %s, %s' % (o[:12], a['pull_request'], a['round'], a['record']))
            elif s == 'eligible':
                print('  eligible  %s  %s:%s%s' % (o[:12], a['record'], ','.join(map(str, where[0])),
                                                  ' (run %s at :%s)' % (a['run'], ','.join(map(str, where[1])))
                                                  if where[1] else ''))
    print('check_objects: %s' % ('OK' if not fails else 'FAILED (%d)' % len(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

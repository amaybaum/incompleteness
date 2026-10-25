#!/usr/bin/env python3
"""citation_roles_check.py -- commit ids a record offers as support are reachable (AGENTS §A.42).

Usage:
    python3 tools/citation_roles_check.py <commit>     self-test, then check the commit
    python3 tools/citation_roles_check.py --self-test

Scope. A record opts in by carrying a manifest, `CITATIONS.json`, in its directory. The manifest
covers every file under that directory, subdirectories included, and nothing else; a directory
without one is not read. Records that keep their own form are never covered: a manifest whose
covered tree meets a record or closed namespace of verification/infrastructure/legacy-records.json,
verification/receipts/, verification/seals/ or a native round's record directory (from the
receipts in the tree) fails as `frozen-scope`, and a manifest whose tree holds another manifest
fails as `nested-manifest`.

Manifest:

    {"schema": "oi-citations", "version": 2, "ids": {
      "<40 lowercase hex>": {"role": "support",    "claim": "<path>:<line>",
                             "claim_sha256": "<64 lowercase hex>"},
      "<40 lowercase hex>": {"role": "provenance", "reason": "<why it is not load-bearing>"},
      "<40 lowercase hex>": {"role": "external",   "repository": "<owner>/<repo>"}},
     "retired": {"<40 lowercase hex>": [<downgrade record>, ...]}}

with exactly those fields, `retired` optional and non-empty when present, the ids of each map
in sorted order, each `retired` list non-empty and without repeats, a retired id listed in
`ids` only as `support` (a reworded claim retires its old record), and each entry carrying
exactly its role and that role's fields, each a non-empty string; a `provenance` or `external`
entry may also carry a `downgrade` record (below). Roles are the author's declaration and are
never inferred; each entry states something a reviewer can check:

  support     `claim` is a repository path under the manifest's directory, other than the
              manifest, and a line of that file on which the id appears: the claim it supports.
              `claim_sha256` is the SHA-256 of that line's normalized text (runs of ASCII
              whitespace collapsed to one space, the ends trimmed). The hash is an integrity aid
              for the line `claim` names; the claim is identified by `claim`, never by its hash.
  provenance  `reason` says why the id is historical and not load-bearing.
  external    `repository` names the other repository the object belongs to (not this one), and
              every occurrence of the id in a covered file names it: immediately preceded by
              `<owner>/<repo>@`, or inside a URL `https://github.com/<owner>/<repo>/.../<id>`.

Claim records and downgrades. Each support entry is a claim record: the manifest that holds it,
its id, and its claim, identified by `claim_sha256`; `claim` locates it, and moving the same text
to another line keeps the record. A downgrade record is

    {"from_claim": "<path>:<line>", "from_claim_sha256": "<64 lowercase hex>",
     "reason": "<why the claim was removed, narrowed or moved>"}

and matches the claim record whose id it is keyed or listed under, and whose `claim` and
`claim_sha256` it repeats. Main's claim records are the baseline, compared one by one with the
commit's:

  - a claim record of main that the commit no longer has, at the same manifest, id and claim
    hash, needs a matching record in some manifest of the commit: the `downgrade` of the entry
    that now lists its id, or one under `retired`. That covers an entry relabelled, dropped,
    re-pointed or reworded, its manifest removed, renamed or split, and its id deleted from the
    text, whatever other manifest still declares the same id support;
  - an entry relabelled in place needs a matching `downgrade` of its own, and an entry of another
    manifest that newly lists a downgraded id as `provenance` or `external` needs one matching
    a downgraded record of that id;
  - the claim of a downgraded record must no longer stand: no line anywhere in the tree may
    hash to its `claim_sha256` (except a line that a support record with the same claim hash
    claims, as when a record moves to another manifest), and no paragraph of a file under the
    record's own directory, subdirectories included, may state main's claimed line unless each
    position that held the id holds an id that a current support record claims on a line of
    that statement itself. The comparison:
      - reads each blank-line paragraph as one text, after NFKC, with Unicode format characters
        removed, a markdown link `[text](url)` reduced to its text and the full ids in its url,
        hexadecimal runs of 7 or more characters removed (full ids kept) and 4- to 6-character
        hexadecimal words removed that mix digits and letters, case-folded, so ids inside the
        claim's own words are not compared;
      - reads the claim's own words with any whitespace, a line break included, between them;
      - takes the place of each id as one optional reference slot, a run of reference tokens:
        brackets, quotes, backticks and @ # : =; the connectives at, in, per, see, commit, cf
        and via; any identifier-shaped token (one holding a digit or / # @, so a url, a run or
        pull-request number or a short id), optionally after one label word ("run #12345",
        "from <id>"); a hexadecimal word of 4 or more characters; a -suffix. The slot is read
        as whitespace-separated chunks within 300 characters, each checked in turn. Sentence
        punctuation stays part of the claim;
      - reads the prefix of the statement that holds the match: the text back to a paragraph
        break, a sentence end, a colon, a semicolon or a table bar, or to a line break that
        begins a block (a list, quote, heading or table line, or the line after a heading or
        table row), at most 300 characters, a leading enumerator ("(i)", "a)") aside. The claim
        stands after any prefix unless the prefix narrows it, by a closed rule: the prefix
        holds the word "conditionally" or "conditional"; or one of its comma-separated clauses
        begins with a conditional or restriction word (if, unless, when, whenever, while, for,
        under, assuming, assume, provided, given, only, except, excluding, restricted, whether,
        suppose, supposing, below, above, with), or with "at" or "in" and holds a comparator,
        and holds a bound: a comparator, a parenthesized named condition such as "(C2)", a
        one-letter variable other than "a" and "i", a labelled token such as "h1", or a number
        word (two to twelve, twenty, hundred, thousand, million); or the prefix ends with "that"
        after a negation (not, no, never, false, longer, cannot, fails) in its last clause ("it
        is not shown that"). A digit alone does not narrow. So an opener ("Indeed,", "In
        Section 3,", "For completeness,", "As noted above,") leaves the claim standing, and a
        condition put first, "if ..., then ..." and a negated "that" make a new statement;
      - needs at least three words of claim besides the reference.

Independently of main, a record fails while any line of the tree hashes to its
`from_claim_sha256`, outside lines a support record of the same claim claims. Each failure is
`support-downgrade`.

So a claim that stays in the text while its record is deleted is caught by the missing record;
with a record, by the claim still standing verbatim anywhere, or, in its own record's
directory, reformatted as above or with its reference slot left empty, shortened, replaced by
another identifier, or holding an id no support record claims on a line of the statement.
Every test that compares with main finds nothing when main is the commit, and the rest read the
commit's tree alone, so a change that passes as a pull request passes again as main.

A genuine rewording, narrowing or withdrawal of the claim with a matching record passes, by
design: the record is the reviewable statement of what became of the claim. No syntactic
checker can reliably decide whether an arbitrarily rewritten claim keeps its meaning; these
controls catch the structural evasions listed above, and independent review still decides
whether a downgrade is scientifically justified.

Ids. Every run of exactly 40 lowercase hexadecimal characters, bounded by non-hexadecimal
characters, in a covered file is an object id the record cites: a commit, or a blob or tree id. A
64-hex run (a SHA-256 digest) is not one, and neither is an abbreviated id. A `support` id must
name a commit; a blob or tree id is cited as `provenance`, and its claim is supported by the
commit that holds it.

At the commit under check, read from git objects and nothing else, a manifest fails when:

  malformed               it is not the manifest above;
  unlisted                a covered file cites an id the manifest does not list;
  unused                  the manifest lists an id no covered file cites;
  claim-outside           a support claim names a path outside the manifest's directory, or the
                          manifest itself;
  claim-file-absent       a support claim names a file the commit does not have;
  claim-line-mismatch     the claimed line does not exist or does not carry the id;
  claim-hash-mismatch     the claimed line's normalized text does not hash to `claim_sha256`;
  support-downgrade       a claim record of main is gone without a matching record, or the
                          claim of a downgraded record still stands (Claim records, above);
  absent                  an id names no object in the repository: checked for every `support`
                          id, and for a `provenance` id when it lands, i.e. when main's copy of
                          the same manifest does not list it as provenance;
  support-not-commit      a `support` id names a blob, tree or tag;
  support-unreachable     a `support` id names a commit not reachable from the commit under
                          check (a commit the change under review adds is reachable);
  external-this-repository  an `external` entry names this repository;
  external-unqualified    an occurrence of an `external` id does not name its declared repository;
  external-in-repository  an `external` id names an object of this repository.

Main is refs/remotes/origin/main, else refs/heads/main; with neither, every id is checked as
landing. Reachability needs full history: a shallow repository is undecidable and fails.

Limitations:
  - Uppercase and abbreviated ids are not read, although git resolves both.
  - Every covered file is scanned as bytes, binary or NUL-containing files included, so an id
    inside a compressed or UTF-16 file is not seen. A symlink is scanned as its target path, not
    the target file; a submodule entry is not scanned.
  - `external-in-repository` is checked on every build, so an external object that later enters
    this repository turns main red until the manifest is corrected.
  - A provenance id's existence, and every downgrade, is checked against a main that lacks the
    change, i.e. in pull-request CI; a commit that reaches main without pull-request CI is
    compared against itself and skips both. With no main ref, only the test that a record's
    claim does not stand verbatim runs.
  - A claim moved out of its record's directory is followed only verbatim, by its hash; with a
    matching record, a reformatted or unreferenced copy elsewhere passes. A claim of fewer than
    three words besides its reference (a JSON field, a list item) is compared by its hash alone.
  - The reference slot reads only the tokens named above: a reference written with more than
    one word before it ("as shown by <id>"), or markup inside the claim (emphasis), reads as a
    different statement and, with a record, passes. Without a record, every such change fails
    as a missing record.
  - A value written where the reference stood reads as a replacement reference, so the claim
    stands and its downgrade fails although it is a narrowing: "at T=300", "at n=4", "in 3D",
    "via Lemma 2". So does a condition ended by a colon ("For n <= 4: ..."), the colon read as
    a label. These fail closed and can be reworded ("when T = 300", "for n <= 4, ...").
  - The prefix rule reads form, not meaning. It fails closed on a narrowing with no bound or
    no conditional word ("On the lattice,", "In 3D,", "In dimension three,"), which reads as
    the claim standing and can be reworded ("for d = 3,", "if n <= 4,"). An opener built in
    the rule's form passes as a narrowing with a record: a conditional clause holding a
    one-letter word or a labelled token ("When we ran it on h1,", "If n is anything,"), or a
    negation idiom ending in "that" ("There is no doubt that", "It is no surprise that").
    Review decides those.
  - A record may sit in any manifest of the commit, so removing every manifest of the tree
    leaves nowhere to record a downgrade, and such a commit fails.
  - An unrelated record that newly lists a downgraded support id as provenance needs a
    `downgrade` record of its own.
  - Rewording a supported claim changes its record: the old one needs a `retired` record.
  - A landed record can later be deleted like any manifest entry; once it is gone, nothing
    compares against it, so its claim can return as a claim citing its id as provenance, which
    is a new unsupported claim and is not forbidden.
  - The check reads one tree: two changes that each pass alone, one downgrading a claim and one
    adding a verbatim copy of it, can fail together on main.
  - Files holding a NUL byte are compared by hash only; markdown emphasis or other markup inside
    a claim is not removed, so an emphasized copy with a record passes.
  - Lines inserted above a claim shift it: the entry then fails as `claim-line-mismatch` or
    `claim-hash-mismatch`, depending on what the claimed line now holds, until it is updated.
  - THIS_REPOSITORY is a constant: in a fork or after a rename it must be edited, or an external
    entry naming the new name is not refused as this repository (external-in-repository still
    refuses an object this repository holds).
  - When a claim record of main is downgraded or the commit holds a record, the check reads the
    tree's blobs once (one `git cat-file --batch`) and normalizes only the files of the
    downgraded records' directories. The verbatim test indexes, in one pass over the tree, the
    lines that carry any record's id by their hash, so its cost is the tree's size plus the
    number of records. Normalization, and the search for a claim in a file, are linear in the
    file, each candidate's reference slot and prefix read within 300 characters. The
    own-directory test is not linear in the records: for each downgraded claim record of main,
    the files of its directory are searched once, so its cost is that number times the
    directory's size. Each id also costs a few git calls of its own (its type, its
    reachability, its claimed blob), so a manifest of thousands of support ids takes minutes.
    The self-test takes about 30 s and runs before every check.
  - An `external` entry's repository is the author's declaration: an id that names no object
    here, with a qualifier naming any repository, passes.
  - A 40-hex value that names no git object of any repository (a SHA-1 file digest) has no role.
  - The checker forces a reviewable statement per id; whether a reason is honest, or a claim
    really rests on its id, is for review."""
import bisect
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v3_verifier as v3  # noqa: E402
import legacy_records_check as lr  # noqa: E402

NAME = b'CITATIONS.json'
FIELDS = {'support': ('claim', 'claim_sha256'), 'provenance': ('reason',),
          'external': ('repository',)}
DOWNGRADE = ('from_claim', 'from_claim_sha256', 'reason')
SHA256 = re.compile(r'[0-9a-f]{64}')
HEX_RUN = re.compile(r'[0-9A-Fa-f]{7,}')
THIS_REPOSITORY = 'amaybaum/incompleteness'
PROTECTED = (b'verification/receipts', b'verification/seals')
MAIN_REFS = ('refs/remotes/origin/main', 'refs/heads/main')
OBJECT_ID = re.compile(rb'(?<![0-9A-Fa-f])[0-9a-f]{40}(?![0-9A-Fa-f])')
CLAIM = re.compile(r'([^:\0]+):([1-9][0-9]*)')
REPOSITORY = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+')
NAME_CHARS = rb'[A-Za-z0-9_.-]+'
QUALIFIERS = (re.compile(rb'(?<![A-Za-z0-9_.-])(' + NAME_CHARS + rb')/(' + NAME_CHARS + rb')@\Z'),
              re.compile(rb'https://github\.com/(' + NAME_CHARS + rb')/(' + NAME_CHARS +
                         rb')/[^\s"\'<>()\[\]`]*\Z'))


def repository_name(name):
    name = name.lower()
    return name[:-4] if name.endswith('.git') else name


def qualifier(data, start):
    """The `owner/repo` an id occurrence at `start` names, normalized, or None."""
    before = data[max(0, start - 512):start]
    for rx in QUALIFIERS:
        m = rx.search(before)
        if m:
            return repository_name((m.group(1) + b'/' + m.group(2)).decode())
    return None


def line_sha256(line):
    """SHA-256 of a line's normalized text: ASCII whitespace runs collapsed, the ends trimmed."""
    return hashlib.sha256(b' '.join(line.split())).hexdigest()


def _text(v):
    return isinstance(v, str) and bool(v.strip())


def _downgrade_ok(dg):
    return isinstance(dg, dict) and set(dg) == set(DOWNGRADE) \
        and all(_text(dg[f]) for f in DOWNGRADE) and bool(CLAIM.fullmatch(dg['from_claim'])) \
        and bool(SHA256.fullmatch(dg['from_claim_sha256']))


def load(raw):
    """({id: entry}, {retired id: record}), or None when the manifest is malformed."""
    try:
        pairs = []
        m = json.loads(raw.decode('utf-8'),
                       object_pairs_hook=lambda kv: pairs.append(kv) or dict(kv))
    except (ValueError, UnicodeDecodeError):
        return None
    if any(len({k for k, _ in kv}) != len(kv) for kv in pairs):
        return None
    if not isinstance(m, dict) or not {'schema', 'version', 'ids'} <= set(m) \
            or set(m) - {'schema', 'version', 'ids', 'retired'} \
            or m['schema'] != 'oi-citations' or m['version'] != 2 or type(m['version']) is not int:
        return None
    ids, retired = m['ids'], m.get('retired', {})
    for keyed in (ids, retired):
        if not isinstance(keyed, dict) or list(keyed) != sorted(keyed) or not all(
                isinstance(k, str) and re.fullmatch(r'[0-9a-f]{40}', k) for k in keyed):
            return None
    if 'retired' in m and not retired or not all(
            isinstance(rs, list) and rs and all(_downgrade_ok(r) for r in rs)
            and len({(r['from_claim'], r['from_claim_sha256']) for r in rs}) == len(rs)
            for rs in retired.values()):
        return None
    out = {}
    for k, e in ids.items():
        role = e.get('role') if isinstance(e, dict) else None
        fields = FIELDS.get(role) if isinstance(role, str) else None
        if fields is None:
            return None
        extra = set(e) - {'role'} - set(fields)
        if not set(fields) <= set(e) or not all(_text(e[f]) for f in fields) \
                or extra - ({'downgrade'} if role != 'support' else set()):
            return None
        if role == 'support' and not (CLAIM.fullmatch(e['claim'])
                                      and SHA256.fullmatch(e['claim_sha256'])):
            return None
        if role == 'external' and not REPOSITORY.fullmatch(e['repository']):
            return None
        if 'downgrade' in e and not _downgrade_ok(e['downgrade']):
            return None
        out[k] = dict(e)
    if any(out[k]['role'] != 'support' for k in set(out) & set(retired)):
        return None
    return out, {k: [dict(r) for r in rs] for k, rs in retired.items()}


def manifest_paths(files):
    return sorted(p for p in files if p == NAME or p.endswith(b'/' + NAME))


def main_commit(repo):
    for ref in MAIN_REFS:
        out = repo.run(['rev-parse', '--verify', '-q', ref + '^{commit}'])
        if out:
            return out.decode().strip()
    return None


def protected(repo, files):
    """(directories, files) whose records keep their own form."""
    dirs, recs = set(PROTECTED), set()
    st = files.get(lr.MANIFEST.encode())
    if st is not None:
        m, why = lr.load_manifest(repo.blob(st[1]))
        if m is None:
            raise v3.Undecidable('legacy-' + why)
        dirs.update(n.encode() for n in m['closed_namespaces'])
        recs.update(p.encode() for p in m['records'])
    for p, (_mode, obj) in files.items():
        if not v3.RECEIPT_PATH.fullmatch(p):
            continue
        try:
            r = json.loads(repo.blob(obj).decode('utf-8'))
            dirs.update(b['path'].encode()[:-len('/preregistration.md')]
                        for b in r['control_plane_blobs']
                        if b['path'].endswith('/preregistration.md'))
        except (ValueError, UnicodeDecodeError, KeyError, TypeError, AttributeError):
            continue          # a receipt that does not parse fails v3-receipts, not here
    return dirs, recs


def object_type(repo, oid):
    out = repo.run(['cat-file', '-t', oid])
    return out.decode().strip() if out else None


def claim_problem(repo, files, d, mp, entry, oid):
    """None when `path:line` names a covered file whose line carries the id and hashes to
    `claim_sha256`; else the code."""
    path, line = CLAIM.fullmatch(entry['claim']).groups()
    p = path.encode()
    if not p.startswith(d) or p == mp or any(s in (b'', b'.', b'..') for s in p.split(b'/')):
        return 'claim-outside'
    if p not in files or files[p][0] == '160000':
        return 'claim-file-absent'
    lines = repo.blob(files[p][1]).split(b'\n')
    n = int(line)
    if n > len(lines) or oid.encode() not in OBJECT_ID.findall(lines[n - 1]):
        return 'claim-line-mismatch'
    if line_sha256(lines[n - 1]) != entry['claim_sha256']:
        return 'claim-hash-mismatch'
    return None


FULL_ID = re.compile(r'(?<![0-9A-Fa-f])[0-9a-f]{40}(?![0-9A-Fa-f])')
SHORT_HEX = re.compile(r'(?<![0-9A-Za-z])[0-9A-Fa-f]{4,6}(?![0-9A-Za-z])')
BREAK = re.compile(r'\n[ \t\r\f\v]*\n\s*')
HEX_RUN_BYTES = re.compile(rb'[0-9a-f]{40,}')
WORD = re.compile(r'[^\W\d_]{2,}')
MIN_WORDS = 3
LINK = re.compile(r'\[([^\[\]\n]*)\]\(([^()\[\]\s]*)\)')
_CF = []


def format_characters():
    """The Unicode format (Cf) characters, built on first use."""
    if not _CF:
        _CF.append(frozenset(chr(c) for c in range(sys.maxunicode + 1)
                             if unicodedata.category(chr(c)) == 'Cf'))
    return _CF[0]


PARA = '\x01'


def normalize(text):
    """The text a claim comparison reads: each paragraph break (a blank line) one PARA mark, and
    each other line break kept; NFKC; Unicode format characters removed; a markdown link
    `[text](url)` reduced to its text and the full ids its url holds; every run of 7 or more
    hexadecimal characters removed except a full lowercase id, and every 4- to 6-character
    hexadecimal word that mixes digits and letters; case-folded; other whitespace collapsed to
    one space. So ids inside a claim's own words are not compared."""
    text = BREAK.sub(PARA, text)
    if not text.isascii():
        text = unicodedata.normalize('NFKC', text)
        for ch in format_characters() & set(text):
            text = text.replace(ch, '')
    text = LINK.sub(lambda m: m.group(1) + ' ' + ' '.join(FULL_ID.findall(m.group(2))), text)
    text = HEX_RUN.sub(lambda m: m.group() if FULL_ID.fullmatch(m.group()) else '', text)
    text = SHORT_HEX.sub(lambda m: '' if (re.search('[0-9]', m.group())
                                          and re.search('[A-Fa-f]', m.group())) else m.group(),
                         text)
    text = re.sub(r'[^\S\n]+', ' ', text.casefold())
    return re.sub(r' *\n *', '\n', text).strip(' ')


REF_PUNCT = '()[]{}<>"\'`@#:='
CONNECTIVES = frozenset(('at', 'in', 'per', 'see', 'commit', 'cf', 'via'))
IDENT = re.compile(r'[0-9/#@]')
HEXWORD = re.compile(r'[0-9a-f]{4,}')
SUFFIX = re.compile(r'-\w+')
WORDCHUNK = re.compile(r'[^\W\d_]+')
MAX_GAP = 300


def _ident(chunk):
    """An identifier-shaped chunk: one holding a digit or / # @ (a url, a run or pull-request
    number, a short or full id)."""
    return bool(IDENT.search(chunk))


def _plain(chunk):
    """A chunk that is reference punctuation, a connective, a hexadecimal word or a -suffix, its
    reference punctuation aside."""
    r = chunk.strip(REF_PUNCT)
    return not r or r in CONNECTIVES or bool(HEXWORD.fullmatch(r) or SUFFIX.fullmatch(r))


def reference_chunks(chunks):
    """How many leading chunks form a reference: each identifier-shaped, plain, or a word before
    an identifier-shaped chunk."""
    n = 0
    while n < len(chunks):
        c = chunks[n]
        if not (_ident(c) or _plain(c) or WORDCHUNK.fullmatch(c) and n + 1 < len(chunks)
                and _ident(chunks[n + 1])):
            break
        n += 1
    return n


def is_reference(text):
    """Whether `text`, between two pieces of a claim, is a reference slot (possibly empty)."""
    chunks = text.split()
    return PARA not in text and reference_chunks(chunks) == len(chunks)


def _trim_tail(seg):
    """The text before an id without the reference next to it: trailing chunks that are
    reference punctuation, connectives, full ids or -suffixes."""
    chunks = seg.split()
    while chunks and (not chunks[-1].strip(REF_PUNCT) or chunks[-1] in CONNECTIVES
                      or FULL_ID.fullmatch(chunks[-1]) or SUFFIX.fullmatch(chunks[-1])):
        chunks.pop()
    return ' '.join(chunks)


def _trim_head(seg):
    """The text after an id without the closing brackets and quotes next to it."""
    return seg.lstrip(' )]}>"\'`')


def _words_rx(core):
    """`core` as a regex in which any whitespace, a line break included, separates its words,
    bounded so that it neither starts nor ends inside a word."""
    rx = r'\s+'.join(re.escape(w) for w in core.split())
    if core[:1].isalnum():
        rx = r'(?<!\w)' + rx
    if core[-1:].isalnum():
        rx += r'(?!\w)'
    return re.compile(rx)


class Claim:
    """A support claim's line, read for comparison: `cores`, its fixed pieces with the reference
    around each id taken out, matched in normalized text by regexes; between two pieces, where an
    id stood, a reference slot that is_reference validates. `slots` are the slots that held
    `oid`. `literal` is its longest word. A statement of it whose prefix narrows it
    (statement_prefix, narrowing) is a new statement."""

    def __init__(self, oid, line):
        text = normalize(line.decode('utf-8', 'replace'))
        ids, parts = FULL_ID.findall(text), FULL_ID.split(text)
        cores = []
        for k, part in enumerate(parts):
            if k > 0:
                part = _trim_head(part)
            if k < len(ids):
                part = _trim_tail(part)
            cores.append(part.strip())
        self.cores, self.rx = cores, [_words_rx(c) if c else None for c in cores]
        self.slots = [k for k, t in enumerate(ids) if t == oid]
        words = WORD.findall(' '.join(cores))
        self.literal = max(' '.join(cores).split(), key=len) if words else ''
        self.eligible = bool(self.slots) and len(words) >= MIN_WORDS

    def finditer(self, norm):
        """(start, end, slot texts) of each statement of the claim in normalized text."""
        a = next(k for k, c in enumerate(self.cores) if c)
        for m in self.rx[a].finditer(norm):
            start, pos, gaps = m.start(), m.end(), {}
            for k in range(a, len(self.cores) - 1):
                if not self.cores[k + 1]:
                    if k + 1 < len(self.cores) - 1:
                        gaps[k] = None                  # two ids side by side: one slot
                        continue
                    tail = norm[pos:pos + MAX_GAP].split(PARA, 1)[0]
                    chunks = list(re.finditer(r'\S+', tail))
                    n = reference_chunks([c.group() for c in chunks])
                    end = pos + (chunks[n - 1].end() if n else 0)
                    gaps[k], pos = norm[pos:end], end
                    continue
                for n in self.rx[k + 1].finditer(norm, pos, min(len(norm), pos + MAX_GAP)):
                    if is_reference(norm[pos:n.start()]):
                        gaps[k], pos = norm[pos:n.start()], n.end()
                        break
                else:
                    break
            else:
                for k in range(a - 1, -1, -1):          # a claim that begins with its id
                    head = re.split(PARA, norm[max(0, start - MAX_GAP):start])[-1]
                    chunks = list(re.finditer(r'\S+', head))[::-1]
                    n = 0
                    while n < len(chunks):
                        c = chunks[n].group()
                        if not (_ident(c) or _plain(c) or WORDCHUNK.fullmatch(c) and n > 0
                                and _ident(chunks[n - 1].group())):
                            break
                        n += 1
                    new = start - len(head) + chunks[n - 1].start() if n else start
                    gaps[k], start = norm[new:start], new
                for k in sorted(gaps, reverse=True):
                    if gaps[k] is None:
                        gaps[k] = gaps.get(k + 1) or ''
                yield start, pos, gaps


PREFIX_MAX = 300
BLOCK_START = re.compile(r' *(?:[-*+>#|]|\d+[.)])')
# a clause narrows a statement when it begins with a conditional or restriction word and holds a
# bound; "at" and "in" begin one only with a comparator; a negation narrows a statement it
# introduces with "that"
CONDITIONS = frozenset((
    'if', 'unless', 'when', 'whenever', 'while', 'for', 'under', 'assuming', 'assume', 'provided',
    'given', 'only', 'except', 'excluding', 'restricted', 'whether', 'suppose', 'supposing',
    'below', 'above', 'with'))
LOCATIVES = frozenset(('at', 'in'))
NEGATIONS = frozenset(('not', 'no', 'never', 'false', 'longer', 'cannot', 'fails'))
NUMBER_WORDS = frozenset((
    'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'twenty', 'hundred', 'thousand', 'million'))
COMPARATOR = re.compile(r'[<>=\u2264\u2265]')
NAMED_CONDITION = re.compile(r'\([^\s()]{1,8}\)')
LABELLED = re.compile(r'[^\W\d_]+\d+')
ENUMERATOR = re.compile(r'\(?(?:[0-9]{1,3}|[a-z]|[ivx]{1,5})\) *')
CLAUSE_WORD = re.compile(r'[^\W_]+')


def statement_prefix(norm, i):
    """The text before position `i` within its statement: back to a paragraph break, a sentence
    end, a colon, a semicolon or a table bar, or to a line break that begins a block (a list,
    quote, heading or table line, or the line after a heading or table row); at most PREFIX_MAX
    characters, list and quote markers, quotes, brackets and a leading enumerator ("(i)", "a)",
    "(1)") aside."""
    lo, j = max(0, i - PREFIX_MAX), i
    while j > lo:
        c = norm[j - 1]
        if c in '.!?;:|' + PARA:
            break
        if c == '\n':
            prev = norm[norm.rfind('\n', lo, j - 1) + 1:j - 1].lstrip(' ')
            if BLOCK_START.match(norm, j) or prev[:1] in ('#', '|'):
                break
        j -= 1
    prefix = norm[j:i].strip(' \n-*+>#"\'([{`')
    m = ENUMERATOR.match(prefix)
    return prefix[m.end():] if m else prefix


def narrowing(prefix):
    """Whether a statement's prefix narrows it. It does when it holds the word conditionally or
    conditional; when one of its comma-separated clauses begins with a word of CONDITIONS, or
    with "at" or "in" and holds a comparator, and holds a bound: a comparator, a parenthesized
    named condition such as "(C2)", a one-letter variable other than "a" and "i", a labelled
    token such as "h1", or a number word; or when it ends with "that" after a negation in the
    same clause ("it is not shown that"). Any other prefix ("Indeed,", "In Section 3,", "For
    completeness,") leaves the statement standing; a digit alone does not narrow it."""
    prefix = FULL_ID.sub('', prefix)
    clauses = [CLAUSE_WORD.findall(c) for c in prefix.split(',')]
    if any({'conditionally', 'conditional'} & set(w) for w in clauses):
        return True
    for clause, w in zip(prefix.split(','), clauses):
        if not w:
            continue
        if w[0] in CONDITIONS or w[0] in LOCATIVES and COMPARATOR.search(clause):
            if COMPARATOR.search(clause) or NAMED_CONDITION.search(clause) \
                    or set(w[1:]) & NUMBER_WORDS or any(
                        len(x) == 1 and x.isalpha() and x not in 'ai' or LABELLED.fullmatch(x)
                        for x in w[1:]):
                return True
    last = clauses[-1] if clauses else []
    return len(last) > 1 and last[-1] == 'that' and bool(set(last[:-1]) & NEGATIONS)


class _Lines:
    """Line numbers of positions in a file's normalized text: the file's paragraph start lines,
    and the positions of paragraph marks and line breaks, built once, read by bisection."""

    def __init__(self, raw, norm):
        starts = [0] + [b.end() for b in BREAK.finditer(raw)]
        self.firsts, n, prev = [], 0, 0
        for x in starts:
            n, prev = n + raw.count('\n', prev, x), x
            self.firsts.append(n + 1)
        self.paras = [m.start() for m in re.finditer(PARA, norm)]
        self.breaks = [m.start() for m in re.finditer('\n', norm)]

    def lines(self, begin, end):
        """(first, last) line of the text from `begin` to `end`."""
        k = bisect.bisect_left(self.paras, begin)
        top = self.paras[k - 1] + 1 if k else 0
        first = self.firsts[min(k, len(self.firsts) - 1)] \
            + bisect.bisect_left(self.breaks, begin) - bisect.bisect_left(self.breaks, top)
        return first, first + bisect.bisect_left(self.breaks, end) \
            - bisect.bisect_left(self.breaks, begin)


class TreeText:
    """The blobs of the commit's tree, read on first use in one `git cat-file --batch`, with each
    blob's normalized text cached."""

    def __init__(self, repo, files):
        self.repo, self.files = repo, files
        self._data, self._norm = None, {}
        self._sorted = sorted((p, st) for p, st in files.items() if st[0] != '160000')

    def data(self, obj):
        if self._data is None:
            objs = sorted({o for _p, (mode, o) in self.files.items() if mode != '160000'})
            r = subprocess.run(['git', 'cat-file', '--batch'], cwd=self.repo.cwd, env=v3.GIT_ENV,
                               input=''.join(o + '\n' for o in objs).encode(), capture_output=True)
            if r.returncode != 0:
                raise v3.Undecidable('undecidable:object-absent')
            self._data, out, at = {}, r.stdout, 0
            for o in objs:
                nl = out.index(b'\n', at)
                head = out[at:nl].split()
                if len(head) != 3 or head[0].decode() != o:
                    raise v3.Undecidable('undecidable:object-absent')
                size = int(head[2])
                self._data[o], at = out[nl + 1:nl + 1 + size], nl + 2 + size
        return self._data[obj]

    def verbatim(self, oids):
        """{(id, hash): [(path, line), ...]} for the lines of the commit's tree that carry one of
        `oids`, by the hash of each line's normalized text, in path and line order. Each file is
        read once, whatever the number of ids: only its runs of 40 or more lowercase hexadecimal
        characters are looked at, each 40-character window of a run against the set."""
        wanted, index = {o.encode() for o in oids}, {}
        if not wanted:
            return index
        for p, (_mode, obj) in self._sorted:
            data = self.data(obj)
            n, at, end = 1, 0, -1
            for m in HEX_RUN_BYTES.finditer(data):
                if m.start() > end:                     # the first run on its line
                    n, at = n + data.count(b'\n', at, m.start()), m.start()
                    start = data.rfind(b'\n', 0, m.start()) + 1
                    end = data.find(b'\n', m.start())
                    end, sha, seen = len(data) if end < 0 else end, None, set()
                for k in range(m.start(), m.end() - 39):
                    o = data[k:k + 40]
                    if o in wanted and o not in seen:
                        seen.add(o)
                        sha = sha or line_sha256(data[start:end])
                        index.setdefault((o.decode(), sha), []).append((p, n))
        return index

    def anchored(self, d, claim, claimed_at):
        """`path:line` of a statement, in a file under the record's directory `d`, of `claim` with
        a slot of its id holding no id that a current support record claims on one of the
        statement's own lines, or None. `claimed_at` maps an id to the (path, line) its support
        records claim. A statement whose prefix narrows it is a new one. A file
        holding a NUL byte is not read."""
        for p, (_mode, obj) in self._sorted[bisect.bisect_left(self._sorted, (d,)):]:
            if not p.startswith(d):
                break
            data = self.data(obj)
            if b'\0' in data:
                continue
            norm = self._norm.get(obj)
            if norm is None:
                norm = self._norm[obj] = normalize(data.decode('utf-8', 'replace'))
            if claim.literal not in norm:
                continue
            index = None
            for begin, end, gaps in claim.finditer(norm):
                if narrowing(statement_prefix(norm, begin)):
                    continue
                if index is None:
                    index = _Lines(data.decode('utf-8', 'replace'), norm)
                first, last = index.lines(begin, end)
                if all(any((p, n) in claimed_at.get(y, ()) for y in FULL_ID.findall(gaps[s])
                           for n in range(first, last + 1)) for s in claim.slots):
                    continue
                return '%s:%d' % (p.decode('utf-8', 'replace'), first)
        return None


def old_line(repo, files, claim, cache):
    """The text a tree holds at `path:line`, or None; each blob is read and split once, into
    `cache`."""
    path, n = CLAIM.fullmatch(claim).groups()
    st = files.get(path.encode())
    if st is None or st[0] == '160000':
        return None
    lines = cache.get(st[1])
    if lines is None:
        lines = cache[st[1]] = repo.blob(st[1]).split(b'\n')
    return lines[int(n) - 1] if int(n) <= len(lines) else None


def matches(record, entry):
    return (record['from_claim'], record['from_claim_sha256']) \
        == (entry['claim'], entry['claim_sha256'])


def check(repo, c, main=None):
    """(problems, manifests, ids): problems is a list of (manifest, code, id, detail)."""
    if repo.width() != 40:
        raise v3.Undecidable('object-format')
    repo.need(c)
    files = repo.entries(c)
    manifests = manifest_paths(files)
    main_files = repo.entries(main) if main else {}
    main_entries = {mp: (load(repo.blob(main_files[mp][1])) or ({}, {}))[0]
                    for mp in manifest_paths(main_files)}
    main_support = [(mp, k, e) for mp in sorted(main_entries)
                    for k, e in sorted(main_entries[mp].items()) if e['role'] == 'support']
    if not manifests and not main_support:
        return [], 0, 0
    pdirs, precs = protected(repo, files) if manifests else (set(), set())
    out, n_ids, loaded, broken = [], 0, {}, set()
    for mp in manifests:
        d = mp[:-len(NAME)]                     # b'' or b'dir/'
        name = mp.decode('utf-8', 'replace')
        if any((p + b'/').startswith(d) or d.startswith(p + b'/')
               for p in pdirs) or any(r.startswith(d) for r in precs):
            out.append((name, 'frozen-scope', '', ''))
            broken.add(mp)
            continue
        if any(o != mp and o.startswith(d) for o in manifests):
            out.append((name, 'nested-manifest', '', ''))
            broken.add(mp)
            continue
        man = load(repo.blob(files[mp][1]))
        if man is None:
            out.append((name, 'malformed', '', ''))
            broken.add(mp)
            continue
        ids, loaded[mp] = man[0], man
        n_ids += len(ids)
        cited, quals = {}, {}
        for p in sorted(files):
            mode, obj = files[p]
            if p == mp or not p.startswith(d) or mode == '160000':
                continue
            data = repo.blob(obj)
            for tok in OBJECT_ID.finditer(data):
                oid = tok.group().decode()
                cited.setdefault(oid, p.decode('utf-8', 'replace'))
                quals.setdefault(oid, set()).add(qualifier(data, tok.start()))
        landed = {k: e['role'] for k, e in main_entries.get(mp, {}).items()}
        for oid in sorted(set(cited) - set(ids)):
            out.append((name, 'unlisted', oid, cited[oid]))
        for oid in sorted(set(ids) - set(cited)):
            out.append((name, 'unused', oid, ''))
        for oid, e in ids.items():
            role = e['role']
            if role == 'support':
                why = claim_problem(repo, files, d, mp, e, oid)
                if why:
                    out.append((name, why, oid, e['claim']))
            if role == 'provenance' and landed.get(oid) == 'provenance':
                continue
            t = object_type(repo, oid)
            if role == 'external':
                declared = repository_name(e['repository'])
                if declared == THIS_REPOSITORY:
                    out.append((name, 'external-this-repository', oid, e['repository']))
                elif any(q != declared for q in quals.get(oid, ())):
                    out.append((name, 'external-unqualified', oid, cited.get(oid, '')))
                if t is not None:
                    out.append((name, 'external-in-repository', oid, cited.get(oid, '')))
            elif t is None:
                out.append((name, 'absent', oid, cited.get(oid, '')))
            elif role == 'support' and t != 'commit':
                out.append((name, 'support-not-commit', oid, cited.get(oid, '')))
            elif role == 'support' and not repo.is_ancestor(oid, c):
                out.append((name, 'support-unreachable', oid, cited.get(oid, '')))
    out.extend(downgrades(repo, files, main_files, main_entries, main_support, loaded, broken))
    return out, len(manifests), n_ids


def downgrades(repo, files, main_files, main_entries, main_support, loaded, broken):
    """support-downgrade problems, record by record; see Downgrades in the module docstring."""
    out = []
    current = {(mp, k): e for mp, (ids, _r) in loaded.items() for k, e in ids.items()
               if e['role'] == 'support'}
    support_now = {k for _m, k in current}
    claimed, claimed_at = {}, {}
    for (_mp, k), e in current.items():
        path, n = CLAIM.fullmatch(e['claim']).groups()
        claimed.setdefault((k, e['claim_sha256']), set()).add((path.encode(), int(n)))
        claimed_at.setdefault(k, set()).add((path.encode(), int(n)))
    records = sorted((mp, k, e['downgrade']) for mp, (ids, _r) in loaded.items()
                     for k, e in ids.items() if 'downgrade' in e)
    records += [(mp, k, r) for mp, (_i, retired) in sorted(loaded.items())
                for k, rs in sorted(retired.items()) for r in rs]
    recorded = {(k, r['from_claim'], r['from_claim_sha256']) for _m, k, r in records}
    text, main_lines = TreeText(repo, files), {}
    downgraded = []
    for mp, oid, e in main_support:
        if mp in broken:
            continue
        now = current.get((mp, oid))
        if now is not None and now['claim_sha256'] == e['claim_sha256']:
            continue                                    # the same claim record
        downgraded.append((mp, oid, e))
        name = mp.decode('utf-8', 'replace')
        if (oid, e['claim'], e['claim_sha256']) not in recorded:
            out.append((name, 'support-downgrade', oid,
                        'no downgrade record for the support record of %s' % e['claim']))
        # a verbatim copy anywhere is the record test's, below; here the claim's own directory
        where, line = None, old_line(repo, main_files, e['claim'], main_lines)
        if line is not None and line_sha256(line) == e['claim_sha256']:
            claim = Claim(oid, line)
            if claim.eligible:
                where = text.anchored(mp[:-len(NAME)], claim, claimed_at)
        if where:
            out.append((name, 'support-downgrade', oid,
                        'the claim of %s stands at %s' % (e['claim'], where)))
    by_id = {}
    for mp, oid, e in downgraded:
        by_id.setdefault(oid, []).append(e)
    for mp, (ids, _r) in sorted(loaded.items()):
        name = mp.decode('utf-8', 'replace')
        for oid, e in sorted(ids.items()):
            if e['role'] == 'support':
                continue
            own = main_entries.get(mp, {}).get(oid)
            if own is not None and own['role'] == 'support':
                need = [own]                # relabelled in place: a record of its own claim
            elif own is None and oid in by_id:
                need = by_id[oid]
            else:
                continue
            dg = e.get('downgrade')
            if not (dg and any(matches(dg, w) for w in need)):
                out.append((name, 'support-downgrade', oid, '%s record for the support record of %s'
                            % ('no downgrade' if dg is None else 'a non-matching downgrade',
                               need[0]['claim'])))
    verbatim = text.verbatim({oid for _m, oid, _r in records})
    for mp, oid, r in records:
        key = (oid, r['from_claim_sha256'])
        where = next((x for x in verbatim.get(key, ()) if x not in claimed.get(key, ())), None)
        if where:
            out.append((mp.decode('utf-8', 'replace'), 'support-downgrade', oid,
                        'the claim of %s stands at %s:%d' % (
                            r['from_claim'], where[0].decode('utf-8', 'replace'), where[1])))
    return out


def check_against_main(repo, c):
    """check() with main resolved from the repository's refs: (problems, manifests, ids, main)."""
    m = main_commit(repo)
    return check(repo, c, m) + (m,)


# ---------------------------------------------------------------------------------------------
# self-test: synthetic repositories; each mutant must fail with its target code and no other
# ---------------------------------------------------------------------------------------------
def verdict(target, codes):
    """A mutant is killed only when the check fails with its target code and nothing else."""
    codes = set(codes)
    if codes == {target}:
        return 'killed'
    if target in codes:
        return 'unclean'
    return 'survived'


def _manifest(entries, ordered=False, retired=None):
    ids = entries if ordered else dict(sorted(entries.items()))
    m = {'schema': 'oi-citations', 'version': 2, 'ids': ids}
    if retired is not None:
        m['retired'] = {k: v if isinstance(v, list) else [v] for k, v in sorted(retired.items())}
    return (json.dumps(m, indent=1) + '\n').encode()


def _claim(sets, oid):
    """The first `path:line` among the fixture's files whose line carries the id."""
    for p in sorted(sets):
        for i, line in enumerate(sets[p][1].split(b'\n')):
            if oid.encode() in OBJECT_ID.findall(line):
                return '%s:%d' % (p.decode(), i + 1)
    return 'rec/NOTE.md:1'


def _claim_sha256(sets, claim):
    """The hash of the fixture line `path:line` names, or a placeholder when there is none."""
    m = CLAIM.fullmatch(claim)
    if not m:
        return '0' * 64
    path, n = m.groups()
    lines = sets.get(path.encode(), ('', b''))[1].split(b'\n')
    return line_sha256(lines[int(n) - 1]) if int(n) <= len(lines) else '0' * 64


def _support(sets, oid, claim=None):
    claim = claim or _claim(sets, oid)
    return {'role': 'support', 'claim': claim, 'claim_sha256': _claim_sha256(sets, claim)}


def self_test():
    fails = []
    # live controls on the classifier, before any mutant is scored by it
    for target, codes, want in (('t', ['t'], 'killed'), ('t', ['t', 't'], 'killed'),
                                ('t', [], 'survived'), ('t', ['u'], 'survived'),
                                ('t', ['t', 'u'], 'unclean')):
        if verdict(target, codes) != want:
            fails.append('classifier: %s on %s' % (want, codes))
    with tempfile.TemporaryDirectory() as td:
        sc = v3.Scratch(os.path.join(td, 'r'))
        lone = sc.git(['hash-object', '-w', '--stdin'], data=b'lone\n').decode().strip()
        legacy = (json.dumps({'schema': 'oi-legacy-records', 'version': 1,
                              'closed_namespaces': ['old/round-a'],
                              'records': {'lone/r.md': lone}}) + '\n').encode()
        receipt = json.dumps({'control_plane_blobs': [
            {'path': 'prog/round-r/preregistration.md', 'blob': '0' * 40}]}).encode()
        sc.commit('M0', [], None, {
            b'base.txt': ('100644', b'base\n'),
            lr.MANIFEST.encode(): ('100644', legacy),
            b'old/round-a/r.md': ('100644', b'frozen\n'),
            b'lone/r.md': ('100644', b'lone\n'),
            b'verification/receipts/R-1.json': ('100644', receipt),
            b'prog/round-r/preregistration.md': ('100644', b'round\n')}, [])
        sc.commit('S', ['M0'], 'M0', {b'side.txt': ('100644', b'side\n')}, [])   # off main
        sc.commit('B1', ['M0'], 'M0', {b'branch.txt': ('100644', b'branch\n')}, [])
        m0, s, b1 = sc.labels['M0'], sc.labels['S'], sc.labels['B1']
        blob, tree = sc.repo.state(m0, b'base.txt')[1], sc.repo.tree(m0)
        tag = sc.git(['mktag'], data=('object %s\ntype commit\ntag t1\ntagger t <t@invalid> '
                                      '1700000000 +0000\n\ntag\n' % m0).encode()).decode().strip()
        gone, gone2 = 'ab' * 20, 'cd' * 20
        sc.git(['update-ref', 'refs/heads/main', m0])

        def codes(c, main):
            try:
                return {code for _m, code, _i, _f in check(sc.repo, c, main)[0]}
            except v3.Undecidable as u:     # a crash is a failure of the test, not a kill
                return {u.code}
            except Exception as e:          # noqa: BLE001
                return {'crash:' + type(e).__name__}

        def case(label, sets, main=m0, parent='M0', dels=()):
            sc.commit(label, [parent], parent, sets, list(dels))
            return codes(sc.labels[label], main)

        def rec(text, ids, extra=None, d='rec'):
            """A record d/ citing `text`; ids maps an id to a role, whose fields the fixture
            fills in, or to a literal entry, a support entry's missing hash filled in from its
            claimed line; bytes are a literal manifest."""
            sets = {(d + '/NOTE.md').encode(): ('100644', text.encode())}
            sets.update(extra or {})
            if isinstance(ids, dict):
                fill = {'support': lambda o: _support(sets, o),
                        'provenance': lambda o: {'role': 'provenance', 'reason': 'fixture'},
                        'external': lambda o: {'role': 'external',
                                               'repository': 'actions/checkout'}}
                entries = {}
                for o, e in ids.items():
                    if not isinstance(e, dict):
                        e = fill[e](o)
                    elif e.get('role') == 'support' and 'claim' in e and 'claim_sha256' not in e:
                        e = dict(e, claim_sha256=_claim_sha256(sets, e['claim']))
                    entries[o] = e
                ids = _manifest(entries)
            sets[(d + '/CITATIONS.json').encode()] = ('100644', ids)
            return sets

        good_text = ('support %s; provenance %s; blob %s; sha-256 %s; upper %s; short %s; '
                     'mixed-case run %s\n' % (m0, s, blob, 'e' * 64, gone.upper(), s[:12],
                                                'D' + gone))
        good_ids = {m0: 'support', s: 'provenance', blob: 'provenance'}
        positives = [
            ('positive fixture', rec(good_text, good_ids)),
            ('off-main id cited as provenance', rec('see %s\n' % s, {s: 'provenance'})),
            ('another repository\'s commit cited as external',
             rec('uses: actions/checkout@%s\n' % gone, {gone: 'external'})),
            ('external id in a URL into its repository',
             rec('https://github.com/Actions/Checkout/commit/%s\n' % gone, {gone: 'external'})),
            ('support id a commit the change under check adds, not on main',
             rec('see %s\n' % b1, {b1: 'support'}), 'B1'),
            ('support claimed on a later line of a subdirectory file', rec('x\n', {m0: 'support'}, {
                b'rec/sub/data.json': ('100644', ('{\n "c": "%s"\n}\n' % m0).encode())})),
            ('entries written out literally', rec(
                'see %s\nprovenance %s\nuses: actions/checkout@%s\n' % (m0, s, gone), {
                    m0: {'role': 'support', 'claim': 'rec/NOTE.md:1'},
                    s: {'role': 'provenance', 'reason': 'the run this record replaced'},
                    gone: {'role': 'external', 'repository': 'actions/checkout'}})),
            ('no manifest: not read', {b'other/NOTE.md': ('100644', ('%s\n' % gone).encode())}),
            ('claim hash over whitespace-normalized text', rec(
                '\t see   %s \r\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                                               'claim_sha256': hashlib.sha256(
                                                   ('see %s' % m0).encode()).hexdigest()}})),
        ]
        for name, sets, *parent in positives:
            got = case('P-' + name, sets, parent=(parent or ['M0'])[0])
            if got:
                fails.append('%s: expected pass, got %s' % (name, sorted(got)))

        two = 'see %s\nand nothing here\n' % m0
        dg_ok = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': 'f' * 64, 'reason': 'x'}
        mutants = [
            ('off-main id cited as support', 'support-unreachable',
             rec('see %s\n' % s, {s: 'support'})),
            ('missing object as provenance', 'absent',
             rec('see %s\n' % gone, {gone: 'provenance'})),
            ('missing object as support', 'absent', rec('see %s\n' % gone, {gone: 'support'})),
            ('blob as support', 'support-not-commit', rec('see %s\n' % blob, {blob: 'support'})),
            ('tree as support', 'support-not-commit', rec('see %s\n' % tree, {tree: 'support'})),
            ('tag as support', 'support-not-commit', rec('see %s\n' % tag, {tag: 'support'})),
            ('claim on a line without the id', 'claim-line-mismatch',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:2'}})),
            ('claim past the end of the file', 'claim-line-mismatch',
             rec('x\nsee %s' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:9'}})),
            ('claim outside the manifest directory', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'base.txt:1'}})),
            ('claim escaping the directory by ..', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/../rec/NOTE.md:1'}})),
            ('claim naming the manifest itself', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/CITATIONS.json:4'}})),
            ('claim naming a file the commit lacks', 'claim-file-absent',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/gone.md:1'}})),
            ('external commit of this repository', 'external-in-repository',
             rec('uses: actions/checkout@%s\n' % s, {s: 'external'})),
            ('external id unqualified', 'external-unqualified',
             rec('pinned to %s\n' % gone, {gone: 'external'})),
            ('external id qualified once, unqualified once', 'external-unqualified',
             rec('uses: actions/checkout@%s\n# pinned to %s\n' % (gone, gone),
                 {gone: 'external'})),
            ('external id qualified with another repository', 'external-unqualified',
             rec('uses: actions/setup-python@%s\n' % gone, {gone: 'external'})),
            ('external entry naming this repository', 'external-this-repository',
             rec('uses: amaybaum/incompleteness@%s\n' % gone,
                 {gone: {'role': 'external', 'repository': 'Amaybaum/Incompleteness.git'}})),
            ('unlisted id', 'unlisted', rec('see %s and %s\n' % (m0, s), {m0: 'support'})),
            ('unlisted id in a subdirectory file', 'unlisted',
             rec('see %s\n' % m0, {m0: 'support'},
                 {b'rec/sub/x.out': ('100644', ('run at %s\n' % s).encode())})),
            ('unlisted id in a NUL-containing file', 'unlisted',
             rec('see %s\n' % m0, {m0: 'support'},
                 {b'rec/data.bin': ('100644', b'\x00\x01' + s.encode() + b'\x00\xff')})),
            ('unused id', 'unused', rec('see %s\n' % m0, {m0: 'support', s: 'provenance'})),
            ('malformed: not json', 'malformed', rec('x\n', b'{"schema": \n')),
            ('malformed: wrong schema', 'malformed', rec('x\n', b'{"schema": "oi-legacy-records", '
                                                        b'"version": 2, "ids": {}}')),
            ('malformed: version 1', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                      b'"version": 1, "ids": {}}')),
            ('malformed: version 2.0', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                        b'"version": 2.0, "ids": {}}')),
            ('malformed: version true', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                         b'"version": true, "ids": {}}')),
            ('malformed: unknown field', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                          b'"version": 2, "ids": {}, "x": 1}')),
            ('malformed: bare role string', 'malformed', rec('see %s\n' % s, (
                '{"schema": "oi-citations", "version": 2, "ids": {"%s": "provenance"}}'
                % s).encode())),
            ('malformed: unknown role', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'evidence', 'reason': 'x'}})),
            ('malformed: support without claim', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'support'}})),
            ('malformed: claim without a line', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md'}})),
            ('malformed: provenance without reason', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance'}})),
            ('malformed: provenance with an empty reason', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance', 'reason': ' '}})),
            ('malformed: entry with another role\'s field', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance', 'reason': 'x', 'claim': 'a:1'}})),
            ('malformed: external without an owner', 'malformed',
             rec('uses: checkout@%s\n' % gone, {gone: {'role': 'external',
                                                       'repository': 'checkout'}})),
            ('malformed: unsorted ids', 'malformed', rec('%s %s\n' % (m0, s), _manifest({
                o: {'role': 'provenance', 'reason': 'x'}
                for o in sorted([m0, s], reverse=True)}, ordered=True))),
            ('malformed: duplicate id', 'malformed', rec('%s\n' % m0, (
                '{"schema": "oi-citations", "version": 2, "ids": {"%s": {"role": "provenance", '
                '"reason": "x"}, "%s": {"role": "provenance", "reason": "y"}}}'
                % (m0, m0)).encode())),
            ('malformed: short id', 'malformed', rec('x\n', _manifest({
                m0[:12]: {'role': 'provenance', 'reason': 'x'}}))),
            ('claim hash of another line', 'claim-hash-mismatch',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                            'claim_sha256': line_sha256(b'and nothing here')}})),
            ('claim hash of the line before normalization', 'claim-hash-mismatch',
             rec('see  %s\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                                         'claim_sha256': hashlib.sha256(
                                             ('see  %s' % m0).encode()).hexdigest()}})),
            ('malformed: support without claim_sha256', 'malformed', rec('see %s\n' % m0, _manifest(
                {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1'}}))),
            ('malformed: claim_sha256 in uppercase', 'malformed', rec('see %s\n' % m0, _manifest(
                {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                      'claim_sha256': line_sha256(('see %s' % m0).encode()).upper()}}))),
            ('malformed: downgrade on a support entry', 'malformed', rec('see %s\n' % m0, {m0: dict(
                {'role': 'support', 'claim': 'rec/NOTE.md:1'}, downgrade=dict(dg_ok))})),
            ('malformed: downgrade with an empty reason', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': dict(dg_ok, reason=' ')}})),
            ('malformed: downgrade without from_claim_sha256', 'malformed', rec(
                'see %s\n' % s, {s: {'role': 'provenance', 'reason': 'x', 'downgrade': {
                    'from_claim': 'rec/NOTE.md:2', 'reason': 'x'}}})),
            ('malformed: downgrade with an extra field', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': dict(dg_ok, note='x')}})),
            ('malformed: empty retired', 'malformed', rec('x\n', _manifest({}, retired={}))),
            ('malformed: retired id also listed', 'malformed', rec('see %s\n' % s, _manifest(
                {s: {'role': 'provenance', 'reason': 'x'}}, retired={s: dict(dg_ok)}))),
            ('malformed: retired record without a reason', 'malformed', rec('x\n', _manifest(
                {}, retired={s: {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': 'f' * 64}}))),
            ('malformed: retired ids unsorted', 'malformed', rec('x\n', (
                '{"schema": "oi-citations", "version": 2, "ids": {}, "retired": {"%s": [%s], '
                '"%s": [%s]}}' % (s, json.dumps(dg_ok), m0, json.dumps(dg_ok))).encode()
                if s > m0 else ('{"schema": "oi-citations", "version": 2, "ids": {}, "retired": '
                                '{"%s": [%s], "%s": [%s]}}' % (m0, json.dumps(dg_ok), s,
                                                               json.dumps(dg_ok))).encode())),
            ('malformed: a retired record repeated', 'malformed', rec('x\n', _manifest(
                {}, retired={s: [dict(dg_ok), dict(dg_ok)]}))),
            ('malformed: a retired value not a list', 'malformed', rec('x\n', (
                '{"schema": "oi-citations", "version": 2, "ids": {}, "retired": {"%s": %s}}'
                % (s, json.dumps(dg_ok))).encode())),
            ('malformed: an empty retired list', 'malformed', rec('x\n', (
                '{"schema": "oi-citations", "version": 2, "ids": {}, "retired": {"%s": []}}'
                % s).encode())),
            ('malformed: downgrade as a string', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': 'narrowed'}})),
            ('nested manifest', 'nested-manifest', rec('see %s\n' % m0, {m0: 'support'}, {
                b'rec/sub/CITATIONS.json': ('100644', _manifest({}))})),
            ('manifest over a native round record', 'frozen-scope', {
                b'prog/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest over a legacy closed namespace', 'frozen-scope', {
                b'old/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest over a legacy record', 'frozen-scope', {
                b'lone/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest inside a legacy closed namespace', 'frozen-scope', {
                b'old/round-a/sub/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest in verification/receipts/', 'frozen-scope', {
                b'verification/receipts/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest in verification/seals/', 'frozen-scope', {
                b'verification/seals/CITATIONS.json': ('100644', _manifest({}))}),
        ]
        for name, target, sets in mutants:
            got = case('X-' + name, sets)
            v = verdict(target, got)
            if v != 'killed':
                fails.append('%s: %s (target %s, got %s)' % (name, v, target, sorted(got)))

        # a submodule entry in a covered directory is not scanned, and is no claim file
        def gitlink(label, sets):
            sc.commit(label + '-base', ['M0'], 'M0', sets, [])
            base = sc.labels[label + '-base']
            sub = sc.git(['rev-parse', base + ':rec']).decode().strip()
            rec_tree = sc.git(['mktree', '-z'], data=sc.git(['ls-tree', '-z', sub]) + (
                '160000 commit %s\tmod\0' % m0).encode()).decode().strip()
            root = [e for e in sc.git(['ls-tree', '-z', base]).split(b'\0')
                    if e and not e.endswith(b'\trec')]
            root = b''.join(e + b'\0' for e in root) + ('040000 tree %s\trec\0' % rec_tree).encode()
            tree = sc.git(['mktree', '-z'], data=root).decode().strip()
            return codes(sc.git(['commit-tree', tree, '-p', m0, '-m', label],
                                env=v3.COMMIT_ENV).decode().strip(), m0)
        for name, sets, want in (
                ('submodule entry in a covered directory', rec('see %s\n' % m0, {m0: 'support'}),
                 set()),
                ('support claim naming a submodule entry', rec('see %s\n' % m0, {m0: {
                    'role': 'support', 'claim': 'rec/mod:1', 'claim_sha256': 'f' * 64}}),
                 {'claim-file-absent'}),
                ('a record beside a submodule entry: the tree read skips it', rec(
                    'see %s\n' % m0, {m0: 'support'}), None)):
            if want is None:
                sets[b'rec/CITATIONS.json'] = ('100644', _manifest(json.loads(
                    sets[b'rec/CITATIONS.json'][1])['ids'], retired={gone: {
                        'from_claim': 'rec/NOTE.md:1', 'from_claim_sha256': 'f' * 64,
                        'reason': 'withdrawn'}}))
                want = set()
            got = gitlink('G-' + name, sets)
            if got != want:
                fails.append('%s: expected %s, got %s' % (name, sorted(want), sorted(got)))

        # negative controls, on fixtures of their own: a live unrelated failure (an unused id, no
        # reachability defect) is not a kill of the support-reachability mutant, and a fixture
        # that fails on its target and on something else is unclean, not a kill
        got = case('N-unrelated', rec('see %s\n' % m0, {m0: 'support', blob: 'provenance'}))
        if got != {'unused'} or verdict('support-unreachable', got) != 'survived':
            fails.append('negative control: unrelated failure %s scored %s' % (
                sorted(got), verdict('support-unreachable', got)))
        got = case('N-unclean', rec('see %s and %s\n' % (s, m0), {s: 'support'}))
        if got != {'support-unreachable', 'unlisted'} \
                or verdict('support-unreachable', got) != 'unclean':
            fails.append('negative control: two failures %s scored %s' % (
                sorted(got), verdict('support-unreachable', got)))

        # landing: a provenance id is checked for existence when it lands, not after; an id main
        # already lists stays admitted once its object is gone (e.g. its branch deleted)
        sc.commit('L', ['M0'], 'M0', rec('see %s\n' % gone2, {gone2: 'provenance'}), [])
        lid = sc.labels['L']
        for name, main, want in (('landing', m0, {'absent'}), ('landed, main at it', lid, set()),
                                 ('no main ref given', None, {'absent'})):
            got = codes(lid, main)
            if got != want:
                fails.append('%s: expected %s, got %s' % (name, sorted(want), sorted(got)))
        got = case('L2', {b'rec/more.md': ('100644', b'more\n')}, main=lid, parent='L')
        if got:
            fails.append('after landing: expected pass, got %s' % sorted(got))
        got = case('L3', rec('see %s\n' % gone2, {gone2: 'support'}), main=lid, parent='L')
        if got != {'absent'}:
            fails.append('landed id re-declared support: expected absent, got %s' % sorted(got))
        # an id main lists as external, re-declared provenance, is checked as landing
        sc.commit('LX', ['M0'], 'M0', rec('uses: actions/checkout@%s\n' % gone2,
                                          {gone2: 'external'}), [])
        got = case('LX2', rec('see %s\n' % gone2, {gone2: 'provenance'}), main=sc.labels['LX'],
                   parent='LX')
        if got != {'absent'}:
            fails.append('landed external re-declared provenance: expected absent, got %s'
                         % sorted(got))

        # downgrades: on main D0, rec/ lists m0 as the support of rec/NOTE.md:2; on main DX it lists
        # gone. Each case is a child of its main, checked against it, and must fail with exactly
        # the codes given; support-downgrade is SD.
        SD = 'support-downgrade'
        claim_line = 'The bound holds at %s.' % m0
        h0, h_stale = line_sha256(claim_line.encode()), line_sha256(b'The bound was read off.')
        hist = 'history: %s' % m0
        reworded = 'The bound is established at %s.' % m0
        narrowed = 'The bound holds at %s for n <= 4 only.' % m0
        d0_text = '# Note\n%s\n%s\n' % (claim_line, hist)
        sc.commit('D0', ['M0'], 'M0', rec(d0_text, {m0: 'support'}), [])
        sc.commit('DX', ['M0'], 'M0', rec('# Note\nThe bound holds at %s.\n' % gone,
                                          {gone: 'support'}), [])
        d0 = sc.labels['D0']
        # DO: D0 with other/ already listing m0 as provenance
        sc.commit('DO', ['D0'], 'D0', {
            b'other/x.md': ('100644', (hist + '\n').encode()),
            b'other/CITATIONS.json': ('100644', _manifest({m0: {
                'role': 'provenance', 'reason': 'the run the bound was read from'}}))}, [])
        sc.commit('DI', ['M0'], 'M0', rec('# Note\n%s\n\nend\n' % m0, {m0: 'support'}), [])
        # DS: main's own entry is stale, its claim_sha256 not the hash of the line it names
        sc.commit('DS', ['M0'], 'M0', rec('# Note\nan aside on the run at %s\n' % m0, {m0: {
            'role': 'support', 'claim': 'rec/NOTE.md:2', 'claim_sha256': h_stale}}), [])
        hx = line_sha256(('The bound holds at %s.' % gone).encode())
        if json.loads(sc.files['D0'][b'rec/CITATIONS.json'][1])['ids'][m0]['claim_sha256'] != h0 \
                or codes(sc.labels['D0'], m0) or codes(sc.labels['DX'], m0) != {'absent'}:
            fails.append('downgrade fixtures: D0 does not hold, or DX fails otherwise than absent')
        dg0 = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': h0,
               'reason': 'the bound is withdrawn'}
        dgx = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': hx,
               'reason': 'the action is pinned, not relied on'}

        def prov(dg=None):
            e = {'role': 'provenance', 'reason': 'the run the bound was read from'}
            return dict(e, downgrade=dg) if dg else e

        def ext(dg=None):
            e = {'role': 'external', 'repository': 'actions/checkout'}
            return dict(e, downgrade=dg) if dg else e

        gone_rec = (b'rec/NOTE.md', b'rec/CITATIONS.json')
        note = lambda *ls: '# Note\n' + ''.join(x + '\n' for x in ls)        # noqa: E731
        paren_line = 'The bound holds (%s).' % m0
        sc.commit('DP', ['M0'], 'M0', rec(note(paren_line), {m0: 'support'}), [])
        # DD: D0 with the same claim also supported in rec2/; DQ: a claim that is no sentence
        sc.commit('DD', ['D0'], 'D0', rec(d0_text, {m0: 'support'}, d='rec2'), [])
        # DT: D0 with another claim of the same id supported in rec2/
        gap_line = 'The gap closes at %s.' % m0
        sc.commit('DT', ['D0'], 'D0', rec(note(gap_line), {m0: 'support'}, d='rec2'), [])
        sc.commit('DQ', ['M0'], 'M0', rec(note('the bound holds at %s' % m0), {m0: 'support'}),
                  [])
        sc.commit('DW', ['M0'], 'M0', rec(note('Bound holds at %s.' % m0), {m0: 'support'}), [])
        # DL: a claim that begins with its id; DM: one with two ids side by side
        sc.commit('DL', ['M0'], 'M0', rec(note('%s: the bound holds.' % m0), {m0: 'support'}), [])
        hex_line = 'The bound for run ABCDEF1 and build ab12 holds at %s.' % m0
        sc.commit('DH', ['M0'], 'M0', rec(note(hex_line), {m0: 'support'}), [])
        dgh = dict(dg0, from_claim_sha256=line_sha256(hex_line.encode()))
        sc.commit('DM', ['M0'], 'M0', rec(note('The runs %s %s agree on the bound.' % (m0, s)), {
            m0: 'support', s: 'provenance'}), [])

        def repin(fmt, fixture):
            """A retired record of m0, its claim re-pinned on the same line to the fixture's own
            commit, which its children reach."""
            to = sc.labels[fixture]
            text, base_line = fmt % to, fmt % m0
            return rec(note(text), _manifest(dict({to: {
                'role': 'support', 'claim': 'rec/NOTE.md:2',
                'claim_sha256': line_sha256(text.encode())}}, **({s: {
                    'role': 'provenance', 'reason': 'x'}} if s in text else {})), retired={
                m0: dict(dg0, from_claim_sha256=line_sha256(base_line.encode()))}))
        other_sup = {b'other/x.md': ('100644', ('see %s\n' % d0).encode()),
                     b'other/CITATIONS.json': ('100644', _manifest({d0: _support(
                         {b'other/x.md': ('100644', ('see %s\n' % d0).encode())}, d0)}))}
        dcases = [
            # name, sets, deletions, parent and main, expected codes
            ('support relabelled provenance without a record', rec(d0_text, {m0: prov()}), (),
             'D0', {SD}),
            ('record, the claim unchanged at its line', rec(d0_text, {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('record, the claim moved to another line', rec(note(hist, claim_line),
                                                            {m0: prov(dg0)}), (), 'D0', {SD}),
            ('record, the claim moved with its whitespace changed', rec(note(
                hist, '  ' + claim_line.replace(' ', ' \t ') + ' '), {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('record, the claim moved to a subdirectory file', rec(note(hist), {m0: prov(dg0)}, {
                b'rec/sub/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('the claim reworded, relabelled without a record', rec(note(reworded, hist),
                                                                    {m0: prov()}), (), 'D0', {SD}),
            ('record not matching main\'s claim hash', rec(note(hist), {m0: prov(dict(
                dg0, from_claim_sha256=line_sha256(reworded.encode())))}), (), 'D0', {SD}),
            ('record not matching main\'s claim path', rec(note(hist), {m0: prov(dict(
                dg0, from_claim='rec/NOTE.md:3'))}), (), 'D0', {SD}),
            ('support relabelled external without a record', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext()}), (), 'DX', {SD}),
            ('support entry dropped while the id is cited', rec(note(hist), {}), (), 'D0',
             {'unlisted', SD}),
            ('record, the claim removed', rec(note(hist), {m0: prov(dg0)}), (), 'D0', set()),
            ('record, narrowed text added above the old claim left in place', rec(
                note(narrowed, claim_line), {m0: prov(dg0)}), (), 'D0', {SD}),
            ('record, the claim narrowed with new text', rec(note(narrowed, hist),
                                                             {m0: prov(dg0)}), (), 'D0', set()),
            ('support relabelled external with a record', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext(dgx)}), (), 'DX', set()),
            ('support entry re-pointed to another claim, no record', rec(
                note(hist, claim_line), {m0: 'support'}), (), 'D0', {SD}),
            ('support entry re-pointed, the old claim removed, retired', rec(
                note(hist), _manifest({m0: _support({b'rec/NOTE.md': (
                    '100644', note(hist).encode())}, m0)}, retired={m0: dg0})), (), 'D0', set()),
            ('the claim moved to another line, its entry updated', rec(
                note(hist, claim_line), {m0: {'role': 'support', 'claim': 'rec/NOTE.md:3'}}), (),
             'D0', set()),
            ('support entry dropped with its citations, no record', rec(note(), {}), (), 'D0',
             {SD}),
            ('support entry retired with its citations', rec(note(), _manifest(
                {}, retired={m0: dg0})), (), 'D0', set()),
            ('manifest removed, its directory still citing the id', {},
             (b'rec/CITATIONS.json',), 'D0', {SD}),
            ('manifest removed, the claim reworded, its directory still citing the id', {
                b'rec/NOTE.md': ('100644', note(reworded).encode())}, (b'rec/CITATIONS.json',),
             'D0', {SD}),
            ('manifest removed, the claim moved unchanged out of scope', {
                b'other/x.md': ('100644', (claim_line + '\n').encode())}, gone_rec, 'D0', {SD}),
            ('record removed with its claim, no record', {}, gone_rec, 'D0', {SD}),
            ('record removed with its claim, retired in another manifest', {
                b'other/CITATIONS.json': ('100644', _manifest({}, retired={m0: dg0}))},
             gone_rec, 'D0', set()),
            ('record moved, relabelled without a record', rec(note(hist), {m0: prov()}, d='rec2'),
             gone_rec, 'D0', {SD}),
            ('record moved, a record kept with the claim unchanged', rec(
                d0_text, {m0: prov(dg0)}, d='rec2'), gone_rec, 'D0', {SD}),
            ('record moved, a record kept with the claim removed', rec(
                note(hist), {m0: prov(dg0)}, d='rec2'), gone_rec, 'D0', set()),
            ('record moved to another manifest, still support, no record', rec(
                d0_text, {m0: 'support'}, d='rec2'), gone_rec, 'D0', {SD}),
            ('record moved to another manifest, still support, retired there', rec(
                d0_text, _manifest({m0: _support({b'rec2/NOTE.md': ('100644', d0_text.encode())},
                                                 m0)}, retired={m0: dg0}), d='rec2'), gone_rec,
             'D0', set()),
            ('record moved without a manifest, the claim reworded', {
                b'rec2/NOTE.md': ('100644', note(reworded).encode())}, gone_rec, 'D0', {SD}),
            # the second review's seven bypasses
            ('the id removed from text and manifest, the claim kept', rec(
                note('The bound holds.'), {}), (), 'D0', {SD}),
            ('the id abbreviated on the claim, the entry dropped', rec(
                note('The bound holds at %s.' % m0[:12]), {}), (), 'D0', {SD}),
            ('the id uppercased on the claim, the entry dropped', rec(
                note('The bound holds at %s.' % m0.upper()), {}), (), 'D0', {SD}),
            ('the claim moved verbatim to a directory without a manifest', rec(note('moved'), {}, {
                b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('the claim moved verbatim to another manifest\'s record as provenance', rec(
                note('moved'), {}, {b'other/x.md': ('100644', (claim_line + '\n').encode()),
                                    b'other/CITATIONS.json': ('100644', _manifest(
                                        {m0: prov()}))}), (), 'D0', {SD}),
            ('record kept, the claim moved verbatim out of the covered tree', rec(
                note(hist), {m0: prov(dg0)}, {
                    b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('manifest renamed citations.json, the id removed from the text', {
                b'rec/NOTE.md': ('100644', note('The bound holds.').encode()),
                b'rec/citations.json': ('100644', _manifest({}))}, (b'rec/CITATIONS.json',),
             'D0', {SD}),
            ('manifest removed, the claim kept with its reference deleted', {
                b'rec/NOTE.md': ('100644', note('The bound holds at .').encode())},
             (b'rec/CITATIONS.json',), 'D0', {SD}),
            # the id still declared support on another line: the claim may not stay without it
            ('still support on another line, the reference deleted from the claim', rec(
                note(hist, 'The bound holds at .'), {m0: 'support'}), (), 'D0', {SD}),
            ('still support on another line, the reference abbreviated on the claim', rec(
                note(hist, 'The bound holds at %s.' % m0[:12]), {m0: 'support'}), (), 'D0', {SD}),
            ('still support on another line, the reference uppercased on the claim', rec(
                note(hist, 'The bound holds at %s.' % m0.upper()), {m0: 'support'}), (), 'D0',
             {SD}),
            ('still support in another manifest, the claim kept without its reference', rec(
                note('The bound holds at .'), {}, {
                    b'other/x.md': ('100644', (hist + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: _support(
                        {b'other/x.md': ('100644', (hist + '\n').encode())}, m0)}))}), (),
             'D0', {SD}),
            ('still support, the claim reworded with its reference, no record', rec(
                note(reworded, hist), {m0: 'support'}), (), 'D0', {SD}),
            ('still support, the claim reworded with its reference, retired', rec(
                note(reworded, hist), _manifest({m0: _support({b'rec/NOTE.md': (
                    '100644', note(reworded, hist).encode())}, m0)}, retired={m0: dg0})), (),
             'D0', set()),
            ('still support, the claim also quoted with its reference elsewhere', rec(
                d0_text, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:2'}}, {
                    b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', set()),
            # with a matching record: the claim counts as unchanged when its only edit is to its id
            ('retired, the id abbreviated on the unchanged claim', rec(
                note('The bound holds at %s.' % m0[:12]), _manifest({}, retired={m0: dg0})), (),
             'D0', {SD}),
            ('retired, the id uppercased on the unchanged claim', rec(
                note('The bound holds at %s.' % m0.upper()), _manifest({}, retired={m0: dg0})),
             (), 'D0', {SD}),
            ('retired, the id removed from the unchanged claim', rec(
                note('The bound holds at .'), _manifest({}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, the claim kept with its reference phrase deleted', rec(
                note('The bound holds.'), _manifest({}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, the claim reworded', rec(
                note('The bound is not established.'), _manifest({}, retired={m0: dg0})), (),
             'D0', set()),
            # reformatted claims, with a matching record: the claim still stands
            ('recorded, the claim split over two lines', rec(
                note('The bound holds', 'at %s.' % m0), {m0: prov(dg0)}), (),
             'D0', {SD}),
            ('recorded, the claim reflowed into a longer line', rec(
                note('As before. ' + claim_line + ' Nothing else.'), {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('recorded, a zero-width space in the claim', rec(
                note('The bound\u200b holds at %s.' % m0), {m0: prov(dg0)}), (),
             'D0', {SD}),
            ('recorded, a no-break space in the claim', rec(
                note('The bound\u00a0holds at %s.' % m0), {m0: prov(dg0)}), (),
             'D0', {SD}),
            ('retired, the id abbreviated to 6 characters', rec(
                note('The bound holds at %s.' % m0[:6]), _manifest({}, retired={m0: dg0})), (),
             'D0', {SD}),
            ('retired, the reference in parentheses deleted', rec(
                note('The bound holds.'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(paren_line.encode()))})), (), 'DP', {SD}),
            ('recorded, the claim narrowed over two lines', rec(
                note('The bound holds at %s' % m0, 'for n <= 4 only.'), {m0: prov(dg0)}), (),
             'D0', set()),
            ('retired, the claim kept with its id deleted in a JSON file of the record', rec(
                note(), _manifest({}, retired={m0: dg0}), {b'rec/data.json': (
                    '100644', b'{"claim": "The bound holds at ."}\n')}), (), 'D0', {SD}),
            ('retired, the claim moved verbatim into an uncovered text file', rec(
                note(), _manifest({}, retired={m0: dg0}), {b'loose/x.txt': (
                    '100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('retired under another id', rec(note(), _manifest({}, retired={s: dg0})), (), 'D0',
             {SD}),
            # a replacement id is a re-pin only where a support record of it claims a line of the
            # same paragraph: not an id declared support elsewhere, nor this id supported elsewhere
            ('retired, the reference replaced by an id supported only in another manifest', rec(
                note('The bound holds at %s.' % d0), _manifest(
                    {d0: {'role': 'provenance', 'reason': 'x'}}, retired={m0: dg0}), other_sup),
             (), 'D0', {SD}),
            ('retired, re-pinned to an id whose support record claims another paragraph', rec(
                note('The bound holds at %s.' % d0, '', 'see %s' % d0), _manifest(
                    {d0: {'role': 'support', 'claim': 'rec/NOTE.md:4',
                          'claim_sha256': line_sha256(('see %s' % d0).encode())}},
                    retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, re-pinned to an id supported elsewhere, another id supported beside it',
             rec(note('The bound holds at %s. See %s.' % (d0, m0)), _manifest(
                 {d0: {'role': 'provenance', 'reason': 'x'},
                  m0: {'role': 'support', 'claim': 'rec/NOTE.md:2',
                       'claim_sha256': line_sha256(('The bound holds at %s. See %s.'
                                                    % (d0, m0)).encode())}},
                 retired={m0: dg0}), other_sup), (), 'D0', {SD}),
            ('retired, re-pinned in the second paragraph of a file', rec(
                note('', 'The bound holds at %s.' % d0), _manifest(
                    {d0: {'role': 'support', 'claim': 'rec/NOTE.md:3',
                          'claim_sha256': line_sha256(('The bound holds at %s.'
                                                       % d0).encode())}},
                    retired={m0: dg0})), (), 'D0', set()),
            ('recorded, a fragment claim kept after a negation', rec(
                note('Not that the bound holds at'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(('the bound holds at %s' % m0).encode()))})),
             (), 'DQ', set()),
            ('retired, re-pinned on a line after one holding only a short id', rec(
                note(m0[:7], 'The bound holds at %s.' % d0), _manifest(
                    {d0: {'role': 'support', 'claim': 'rec/NOTE.md:3',
                          'claim_sha256': line_sha256(('The bound holds at %s.'
                                                       % d0).encode())}},
                    retired={m0: dg0})), (), 'D0', set()),
            ('retired, another id inside the claim changed, an uppercase full-length one', rec(
                note(hex_line.replace(m0, '').replace('ABCDEF1', 'ABCDEF2')), _manifest(
                    {}, retired={m0: dgh})), (), 'DH', {SD}),
            ('retired, another id inside the claim changed, a short one', rec(
                note(hex_line.replace(m0, '').replace('ab12', 'cd34')), _manifest(
                    {}, retired={m0: dgh})), (), 'DH', {SD}),
            ('retired, re-pinned through a markdown link to a supported commit', rec(
                note('The bound holds at [%s](https://github.com/o/r/commit/%s).' % (d0[:7], d0)),
                _manifest({d0: {'role': 'support', 'claim': 'rec/NOTE.md:2',
                                'claim_sha256': line_sha256((
                                    'The bound holds at [%s](https://github.com/o/r/commit/%s).'
                                    % (d0[:7], d0)).encode())}}, retired={m0: dg0})), (),
             'D0', set()),
            ('recorded, the claim restated as a list item without its reference', rec(
                note(hist, '- The bound holds at .'), {m0: prov(dg0)}), (), 'D0', {SD}),
            ('recorded, the claim reflowed, its id still support in another manifest', rec(
                note('The bound', 'holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'DD', {SD}),
            ('recorded, the claim removed, its id still support in another manifest', rec(
                note(hist), {m0: prov(dg0)}), (), 'DD', set()),
            # narrowings written before the claim, and negations, are new statements
            ('recorded, the claim narrowed by a condition put first', rec(
                note('For n <= 4, the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (),
             'D0', set()),
            ('recorded, the claim narrowed by "if ..., then"', rec(
                note('If n <= 4, then the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (),
             'D0', set()),
            # a statement also begins after a label colon, a semicolon or a table cell's bar
            ('recorded, the claim kept after a label colon', rec(
                note('Result: the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('recorded, the claim kept after a semicolon', rec(
                note('We ran it; the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (),
             'D0', {SD}),
            ('recorded, the claim kept in a table cell', rec(
                note('| CP-3 | The bound holds at %s. |' % m0, hist), {m0: prov(dg0)}), (),
             'D0', {SD}),
            # a reference replaced by another identifier is still a reference
            ('retired, the reference replaced by a run number', rec(
                note('The bound holds at run #12345.'), _manifest({}, retired={m0: dg0})), (),
             'D0', {SD}),
            ('retired, the reference replaced by a pull-request url', rec(
                note('The bound holds at https://github.com/o/r/pull/885.'), _manifest(
                    {}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, the reference replaced by a markdown link to a pull request', rec(
                note('The bound holds at [#885](https://github.com/o/r/pull/885).'), _manifest(
                    {}, retired={m0: dg0})), (), 'D0', {SD}),
            ('recorded, the reference word changed to "from"', rec(
                note('The bound holds from %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0', {SD}),
            # a re-pin's support record must claim a line of the statement itself
            ('retired, re-pinned to an id whose support record claims another line of the '
             'paragraph', rec(note('The bound holds at %s.' % d0, 'see %s' % d0), _manifest(
                 {d0: {'role': 'support', 'claim': 'rec/NOTE.md:3',
                       'claim_sha256': line_sha256(('see %s' % d0).encode())}},
                 retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, re-pinned on a wrapped claim, its support record claiming its 2nd line',
             rec(note('The bound', 'holds at %s.' % d0), _manifest(
                 {d0: {'role': 'support', 'claim': 'rec/NOTE.md:3',
                       'claim_sha256': line_sha256(('holds at %s.' % d0).encode())}},
                 retired={m0: dg0})), (), 'D0', set()),
            ('recorded, the claim split around a line holding only a short id', rec(
                note('The bound', m0[:7], 'holds at %s.' % m0, hist), {m0: prov(dg0)}), (),
             'D0', {SD}),
            ('recorded, a word continuing the last word of a claim that is no sentence', rec(
                note('the bound holdsx at'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(('the bound holds at %s' % m0).encode()))})),
             (), 'DQ', set()),
            ('retired, the reference replaced by a url without digits', rec(
                note('The bound holds at https://example.org/runs/latest.'), _manifest(
                    {}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, the reference replaced by a letter-only short id', rec(
                note('The bound holds at dcbae.'), _manifest({}, retired={m0: dg0})), (), 'D0',
             {SD}),
            ('retired, the reference replaced by an ellipsis', rec(
                note('The bound holds at ....'), _manifest({}, retired={m0: dg0})), (), 'D0',
             {SD}),
            ('retired, the reference split into the next paragraph: two texts', rec(
                note('The bound holds at', '', '#5.'), _manifest({}, retired={m0: dg0})), (),
             'D0', set()),
            ('retired, a claim beginning with its id, re-pinned', repin(
                '%s: the bound holds.', 'DL'), (), 'DL', set()),
            ('retired, a claim beginning with its id, the id deleted', rec(
                note(': the bound holds.'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(('%s: the bound holds.' % m0).encode()))})),
             (), 'DL', {SD}),
            ('retired, a claim ending with its id, re-pinned', repin(
                'the bound holds at %s', 'DQ'), (), 'DQ', set()),
            ('retired, a claim with two ids side by side, re-pinned', repin(
                'The runs %%s %s agree on the bound.' % s, 'DM'), (), 'DM', set()),
            ('recorded, the claim negated', rec(
                note('It is not shown that the bound holds at %s.' % m0, hist), {m0: prov(dg0)}),
             (), 'D0', set()),
            ('recorded, the claim reflowed in a subdirectory file', rec(note(hist), {
                m0: prov(dg0)}, {b'rec/sub/y.md': (
                    '100644', note('The bound', 'holds at %s.' % m0).encode())}), (), 'D0', {SD}),
            ('recorded, a word ending in the claim\'s first word, of a claim that is no sentence',
             rec(note('lathe bound holds at'), _manifest({}, retired={m0: dict(
                 dg0, from_claim_sha256=line_sha256(('the bound holds at %s' % m0).encode()))})),
             (), 'DQ', set()),
            ('retired, a two-word claim with its reference deleted: compared by its hash alone',
             rec(note('Bound holds at .'), _manifest({}, retired={m0: dict(
                 dg0, from_claim_sha256=line_sha256(('Bound holds at %s.' % m0).encode()))})),
             (), 'DW', set()),
            ('retired, a support record claiming the old claim\'s line under another hash', rec(
                d0_text, _manifest({m0: {'role': 'support', 'claim': 'rec/NOTE.md:2',
                                         'claim_sha256': h_stale}}, retired={m0: dg0})), (),
             'D0', {SD, 'claim-hash-mismatch'}),
            ('retired, another manifest already listing the id as provenance on main', rec(
                note(), _manifest({}, retired={m0: dg0})), (), 'DO', set()),
            ('retired, a copy without its reference outside the record\'s directory: not '
             'followed, the comparison being anchored', rec(note(), _manifest(
                 {}, retired={m0: dg0}), {b'loose/x.md': ('100644', b'The bound holds at .\n')}),
             (), 'D0', set()),
            ('retired, the reference replaced by a provenance id', rec(
                note('The bound holds at %s.' % s), _manifest(
                    {s: {'role': 'provenance', 'reason': 'x'}}, retired={m0: dg0})), (), 'D0',
             {SD}),
            ('retired, the claim re-pinned to another support commit', rec(
                note('The bound holds at %s.' % d0), _manifest({d0: _support({b'rec/NOTE.md': (
                    '100644', note('The bound holds at %s.' % d0).encode())}, d0)},
                    retired={m0: dg0})), (), 'D0', set()),
            ('recorded, the claim in fullwidth letters', rec(
                note('\uff34\uff48\uff45 \uff42\uff4f\uff55\uff4e\uff44 holds at %s.' % m0),
                {m0: prov(dg0)}), (), 'D0', {SD}),
            ('retired, the id abbreviated to a 6-letter prefix of it', rec(
                note('The bound holds at %s.' % gone[:6]), _manifest({}, retired={gone: dgx})),
             (), 'DX', {SD}),
            ('recorded, a claim line of nothing but the id left in place', rec(
                '# Note\n%s\n\nend\n' % m0, {m0: prov(dict(
                    dg0, from_claim_sha256=line_sha256(m0.encode())))}), (), 'DI', {SD}),
            ('manifest removed, retired in other/, provenance in third/ without a record', {
                b'rec/NOTE.md': ('100644', note(hist).encode()),
                b'other/CITATIONS.json': ('100644', _manifest({}, retired={m0: dg0})),
                b'third/x.md': ('100644', (reworded + '\n').encode()),
                b'third/CITATIONS.json': ('100644', _manifest({m0: prov()}))},
             (b'rec/CITATIONS.json',), 'D0', {SD}),
            ('relabelled in place with a non-matching downgrade, retired elsewhere', rec(
                note(hist), {m0: prov(dict(dg0, from_claim='rec/NOTE.md:3'))}, {
                    b'other/CITATIONS.json': ('100644', _manifest({}, retired={m0: dg0}))}), (),
             'D0', {SD}),
            ('relabelled in place with a downgrade of another hash, retired elsewhere', rec(
                note(hist), {m0: prov(dict(dg0, from_claim_sha256=h_stale))}, {
                    b'other/CITATIONS.json': ('100644', _manifest({}, retired={m0: dg0}))}), (),
             'D0', {SD}),
            ('two claims downgraded in two files, the second reflowed in its directory', {
                **rec(note(hist), {m0: prov(dg0)}), **rec(note('The gap', 'closes at %s.' % m0), {
                    m0: prov(dict(dg0, from_claim='rec2/NOTE.md:2',
                                  from_claim_sha256=line_sha256(gap_line.encode())))},
                    d='rec2')}, (), 'DT', {SD}),
            ('two claims downgraded in two files, both withdrawn', {
                **rec(note(hist), {m0: prov(dg0)}), **rec(note(hist), {
                    m0: prov(dict(dg0, from_claim='rec2/NOTE.md:2',
                                  from_claim_sha256=line_sha256(gap_line.encode())))},
                    d='rec2')}, (), 'DT', set()),
            ('a malformed manifest over a support record', {
                b'rec/CITATIONS.json': ('100644', b'{\n')}, (), 'D0', {'malformed'}),
            # relabel in place while the id is support in another manifest
            ('relabelled in place, support in another manifest, no record', rec(
                d0_text, {m0: prov()}, {b'other/x.md': ('100644', (hist + '\n').encode()),
                                        b'other/CITATIONS.json': ('100644', _manifest({m0: _support(
                                            {b'other/x.md': ('100644', (hist + '\n').encode())},
                                            m0)}))}), (), 'D0', {SD}),
            ('relabelled in place, support in another manifest, record, claim unchanged', rec(
                d0_text, {m0: prov(dg0)}, {
                    b'other/x.md': ('100644', (hist + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: _support(
                        {b'other/x.md': ('100644', (hist + '\n').encode())}, m0)}))}), (), 'D0',
             {SD}),
            ('relabelled in place, support in another manifest, record, claim withdrawn', rec(
                note(hist), {m0: prov(dg0)}, {
                    b'other/x.md': ('100644', (hist + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: _support(
                        {b'other/x.md': ('100644', (hist + '\n').encode())}, m0)}))}), (), 'D0',
             set()),
            # a relabel in another manifest needs its own record
            ('retired in rec/, relabelled provenance in other/ without a record', rec(
                note('moved'), _manifest({}, retired={m0: dg0}), {
                    b'other/x.md': ('100644', (reworded + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: prov()}))}), (), 'D0',
             {SD}),
            ('a claim line of nothing but the id, retired and removed', rec(
                '# Note\n\nend\n', _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(m0.encode()))})), (), 'DI', set()),
            ('relabelled external in place, its only record retired in another manifest', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext()}, {
                    b'other/CITATIONS.json': ('100644', _manifest({}, retired={gone: dgx}))}),
             (), 'DX', {SD}),
            ('retired with a record not matching main\'s claim hash', rec(note(), _manifest(
                {}, retired={m0: dict(dg0, from_claim_sha256=h_stale)})), (), 'D0', {SD}),
            ('retired with a record not matching main\'s claim path', rec(note(), _manifest(
                {}, retired={m0: dict(dg0, from_claim='rec/NOTE.md:3')})), (), 'D0', {SD}),
            ('retired, the id removed and only the case of the claim changed', rec(
                note('THE BOUND HOLDS AT .'), _manifest({}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired against a stale main entry: the line it names is not the claim', rec(
                note('an aside on the run at'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=h_stale)})), (), 'DS', set()),
            ('relabelled provenance in place, its only record retired in another manifest', rec(
                note(hist), {m0: prov()}, {b'other/CITATIONS.json': ('100644', _manifest(
                    {}, retired={m0: dg0}))}), (), 'D0', {SD}),
            ('relabelled provenance in other/ with the record, the claim reworded', rec(
                note('moved'), {}, {b'other/x.md': ('100644', (reworded + '\n').encode()),
                                    b'other/CITATIONS.json': ('100644', _manifest(
                                        {m0: prov(dg0)}))}), (), 'D0', set()),
            ('limitation: another record citing a removed manifest\'s support id', dict(rec(
                note(hist), {m0: prov()}, d='other')), (b'rec/CITATIONS.json',), 'D0', {SD}),
        ]
        # the reference slot: the forms it reads, each with a record, the claim unchanged
        for label, ref in (('backticked short id', '`%s`' % m0[:8]),
                           ('a markdown link', '[%s](https://github.com/o/r/commit/%s)'
                            % (m0[:7], m0)),
                           ('commit and a short id', 'commit %s' % m0[:7]),
                           ('a short id with a suffix', m0[:9] + '-dirty'),
                           ('"per" for "at"', 'per %s' % m0), ('"in" for "at"', 'in %s' % m0),
                           ('in parentheses with "see"', '(see %s)' % m0)):
            text = 'The bound holds %s.' % ref if ref.startswith(('per', 'in', '(see', 'commit')) \
                else 'The bound holds at %s.' % ref
            ids = {m0: prov(dg0)} if m0 in text else {}
            man = _manifest(ids, retired=None if ids else {m0: dg0})
            dcases.append(('recorded, the reference given as %s' % label, rec(note(text), man), (),
                           'D0', {SD}))
        # openers leave a statement standing; a restrictive operator in its prefix narrows it
        for opener in ('Indeed, ', 'Moreover ', 'Moreover, ', 'Thus, ', 'Hence, ',
                       'In particular, ', 'Note that ', 'We find that ', 'It follows that ',
                       'Therefore ', 'Clearly, ', 'As expected, ', 'Again, ', 'Crucially, ',
                       'In summary, ', 'Recall that ', 'We show that ', 'Here, ', 'So ', 'And ',
                       # a number, a section or a date, "above" or "below", and operator words
                       # used idiomatically, do not narrow a statement
                       'In Section 3, ', 'In Table 2, ', 'By Lemma 2, ', 'From Table 1, ',
                       'Section 3 shows that ', 'In 2026, ', 'As of 2026-10-24, ', 'Per #885, ',
                       '(1) ', 'As noted above, ', 'As discussed below, ', '(see above) ',
                       'For completeness, ', 'Not surprisingly, ', 'Given the data, ',
                       'No doubt, ', 'Only then ', 'Two things follow, and ',
                       'As we noted (not shown), ', 'Like the run that never finished, ',
                       'As before, and not\nunexpectedly, ', '(a) ', '(i) ', 'a) ',
                       'When I ran it, ', 'For a moment, ', 'Not only that, but ',
                       'Unconditionally, ', 'Step 2: ', 'Theorem 4: ', 'Finally, ',
                       'In short, ', 'Once again, ', 'Not surprisingly ', 'No doubt ',
                       'Not surprisingly, we find that ', 'Like the run with h1, '):
            dcases.append(('recorded, the claim kept after the opener %r' % opener, rec(note(
                opener + 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0', {SD}))
        for cond in ('For n <= 4, ', 'If n <= 4, then ', 'Conditionally, ', 'Under H1, ',
                     'Only for n <= 4 ', 'Assuming (C2), ', 'Unless n > 4, ',
                     'It is not shown that ', 'It is false that ', 'We no longer claim that ',
                     'For even n, ', 'When n is even, ', 'Provided (C2) holds, ',
                     'At T = 300 K, ', 'Except at n = 4, ', 'Below n = 4, ', 'Given two lattices, ',
                     'Given three lattices, ', 'For lattices of size <= 4, ',
                     'If the lattice has at most n <= 4 sites in each direction, ',
                     'Indeed, if n <= 4, ', '(i) If n <= 4, ', 'a) If n <= 4, ',
                     '- (ii) If n <= 4, ', '> (b) If n <= 4, ', '(If n <= 4, '):
            dcases.append(('recorded, the claim narrowed by %r' % cond, rec(note(
                cond + 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0', set()))
        for cond in ('At T > T_c, ', 'With (EM), '):
            dcases.append(('recorded, the claim narrowed by %r: a comparator or condition'
                           % cond, rec(note(cond + 'the bound holds at %s.' % m0, hist),
                                       {m0: prov(dg0)}), (), 'D0', set()))
        # a setting with no bound is read as an opener: the rule fails closed on it
        for cond in ('In 3D, ', 'In dimension three, ', 'On the lattice, '):
            dcases.append(('recorded, the claim after %r: fail-closed, no bound' % cond, rec(note(
                cond + 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0', {SD}))
        # a record's line stands wherever its id sits in the line, inside a longer run included
        run_line = 'x ab%s' % m0
        dcases.append(('retired, a record whose line stands with its id inside a longer run', rec(
            note(run_line), _manifest({}, retired={m0: [dg0, dict(
                dg0, from_claim_sha256=line_sha256(run_line.encode()))]})), (), 'D0', {SD}))
        two_line = 'runs %s and %s agree' % (s, m0)
        dcases.append(('retired, a record whose line stands outside, after another record\'s id',
                       rec(note(), _manifest({}, retired={
                           m0: [dg0, dict(dg0, from_claim_sha256=line_sha256(two_line.encode()))],
                           s: dict(dg0, from_claim_sha256=line_sha256(b'zz'))}),
                           {b'evidence/x.md': ('100644', (two_line + '\n').encode())}), (), 'D0',
                       {SD}))
        # the rule reads form: an opener in a narrowing's form passes with a record (Limitations)
        for opener in ('There is no doubt that ', 'When we ran it on h1, '):
            dcases.append(('limitation: the claim after %r, read as narrowed' % opener, rec(note(
                opener + 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (), 'D0', set()))
        # a full id in a prefix is no bound, though one of letters then digits reads as a token
        if narrowing('for %s' % ('abc' + '1' * 37)) or not narrowing('for h1'):
            fails.append('downgrade, narrowing: a full id read as a bound, or "h1" not read')
        # a prefix is read for at most 300 characters: a condition further back is not the
        # statement's
        dcases.append(('recorded, a condition more than 300 characters back', rec(note(
            'If n <= 4, ' + 'x ' * 160 + 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}),
            (), 'D0', {SD}))
        for label, text in (
                ('an opener citing another commit', 'As in %s, the bound holds at %s.' % (s, m0)),
                ('a negation in the paragraph before', 'It is not shown that\n\nthe bound holds '
                 'at %s.' % m0),
                ('a negation in the sentence before',
                 'This is not new. The bound holds at %s.' % m0),
                ('a negation before a label colon', 'Not new: the bound holds at %s.' % m0),
                ('a negation before a semicolon', 'We did not rerun it; the bound holds at %s.'
                 % m0),
                ('a condition in the table cell before', '| for n | The bound holds at %s. |' % m0),
                ('an operator word on the line before a list item', 'Notes for review\n- the bound '
                 'holds at %s.' % m0),
                # a condition that opens an earlier statement is not this one's
                ('a sentence before that opens with a condition',
                 'If n <= 4 it was run twice. The bound holds at %s.' % m0),
                ('a question before that opens with a condition',
                 'If n <= 4, does it hold? The bound holds at %s.' % m0),
                ('a condition ended by a colon, read as a label', 'For n <= 4: the bound holds at '
                 '%s.' % m0),
                ('a clause before a semicolon that opens with a condition',
                 'If n <= 4 we reran it; the bound holds at %s.' % m0),
                ('a condition on the line before a list item', 'If n <= 4\n- the bound holds at '
                 '%s.' % m0)):
            dcases.append(('recorded, the claim kept after %s' % label, rec(note(text, hist), dict(
                {m0: prov(dg0)}, **({s: 'provenance'} if s in text else {}))), (), 'D0', {SD}))
        dcases.append(('recorded, a negation on the line before, in the same sentence', rec(note(
            'It is not shown that', 'the bound holds at %s.' % m0, hist), {m0: prov(dg0)}), (),
            'D0', set()))
        dcases.append(('recorded, an operator word in the heading above: not the statement\'s',
                       rec(note('the bound holds at %s.' % m0, hist).replace(
                           '# Note', '# Notes for review'), {m0: prov(dg0)}), (), 'D0', {SD}))
        dcases.append(('recorded, a long reference slot of ten markers', rec(note(
            'The bound holds at # # # # # # # # # #.', hist), {m0: prov(dg0)}), (), 'D0', {SD}))
        dcases.append(('retired, a claim ending with its id, the reference moved to the next '
                       'paragraph', rec('# Note\nthe bound holds at\n\n%s\n' % sc.labels['DQ'],
                                        _manifest({sc.labels['DQ']: {
                                            'role': 'support', 'claim': 'rec/NOTE.md:4',
                                            'claim_sha256': line_sha256(
                                                sc.labels['DQ'].encode())}}, retired={m0: dict(
                                            dg0, from_claim_sha256=line_sha256((
                                                'the bound holds at %s' % m0).encode()))})), (),
                       'DQ', {SD}))
        # a reference slot ends at a paragraph break: past one, line numbers in the next paragraph
        # would be read off by the blank line, and a claimed line there taken for the statement's
        for fixture, text, line, base in (
                ('DQ', '# Note\nthe bound holds at\n\n%s\n%s\n%s\n', 4, 'the bound holds at %s'),
                ('DL', '# Note\n%s\n%s\n%s\n\n: the bound holds.\n', 2, '%s: the bound holds.')):
            to = sc.labels[fixture]
            dcases.append((
                'retired, a claim %s its id, a three-line reference paragraph %s it' % (
                    ('ending with', 'after') if fixture == 'DQ' else ('beginning with', 'before')),
                rec(text % (to, to, to), _manifest(
                    {to: {'role': 'support', 'claim': 'rec/NOTE.md:%d' % line,
                          'claim_sha256': line_sha256(to.encode())}},
                    retired={m0: dict(dg0, from_claim_sha256=line_sha256(
                        (base % m0).encode()))})), (), fixture, {SD}))
        n_down = len(dcases) + 5
        for name, sets, dels, parent, want in dcases:
            got = case('D-' + name, sets, main=sc.labels[parent], parent=parent, dels=dels)
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))
        # a green change stays green once it is main: structured claim lines (a JSON field, a list
        # item) beside many look-alike lines elsewhere, checked against main before landing, as
        # main after landing, and from a later unrelated change; then downgraded both ways
        jl, ll = '  "commit": "%s",' % m0, '- %s' % m0
        look = ''.join('{\n  "commit": "%s",\n  "x": %d\n}\n' % (o, i)
                       for i, o in enumerate((s, b1, gone)))
        for tag, path, body, line_no in (('J', b'rec/result.json', '{\n%s\n  "x": 1\n}\n' % jl, 2),
                                         ('K', b'rec/LIST.md', '# runs\n%s\n' % ll, 2)):
            sets = {path: ('100644', body.encode()),
                    b'evidence/run.json': ('100644', look.encode()),
                    b'docs/list.md': ('100644', b'- \n- item\n-\n- %s\n' % s.encode())}
            sets[b'rec/CITATIONS.json'] = ('100644', _manifest({m0: _support(
                sets, m0, '%s:%d' % (path.decode(), line_no))}))
            sc.commit(tag, ['M0'], 'M0', sets, [])
            jc = sc.labels[tag]
            sc.commit(tag + '-later', [tag], tag, {b'z.txt': ('100644', b'z\n')}, [])
            rec_j = {'from_claim': '%s:%d' % (path.decode(), line_no), 'reason': 'withdrawn',
                     'from_claim_sha256': line_sha256((jl if tag == 'J' else ll).encode())}
            for name, got, want in (
                    ('%s: lands against main' % tag, codes(jc, m0), set()),
                    ('%s: checked as main after landing' % tag, codes(jc, jc), set()),
                    ('%s: a later unrelated change' % tag, codes(sc.labels[tag + '-later'], jc),
                     set()),
                    ('%s: relabelled without a record' % tag, case(tag + '-r', {
                        b'rec/CITATIONS.json': ('100644', _manifest({m0: prov()}))}, main=jc,
                        parent=tag), {SD}),
                    ('%s: recorded, the claim line unchanged' % tag, case(tag + '-u', {
                        b'rec/CITATIONS.json': ('100644', _manifest({m0: prov(rec_j)}))}, main=jc,
                        parent=tag), {SD}),
                    ('%s: retired, the id deleted from the line: a short claim, compared by '
                     'its hash alone' % tag, case(tag + '-d', {
                         path: ('100644', body.replace(m0, '').encode()),
                         b'rec/CITATIONS.json': ('100644', _manifest({}, retired={m0: rec_j}))},
                         main=jc, parent=tag), set()),
                    ('%s: retired, the claim line removed' % tag, case(tag + '-w', {
                        path: ('100644', b'{}\n' if tag == 'J' else b'# runs\n'),
                        b'rec/CITATIONS.json': ('100644', _manifest({}, retired={m0: rec_j}))},
                        main=jc, parent=tag), set())):
                n_down += 1
                if got != want:
                    fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                         sorted(got)))
        # with no main ref nothing is compared, but a record whose claim stands still fails; and
        # once a downgrade has landed it needs nothing more, unless its claim comes back
        for name, sets, want in (
                ('no main ref, relabelled without a record', rec(d0_text, {m0: prov()}), set()),
                ('no main ref, a record whose claim stands', rec(d0_text, {m0: prov(dg0)}), {SD})):
            got = case('D-' + name, sets, main=None, parent='D0')
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))
        # negative control on a fixture of its own: an unrelated failure under the same main (an
        # unused id, the support kept) is not a kill of a downgrade mutant
        got = case('N-downgrade', rec(d0_text, {m0: 'support', s: 'provenance'}),
                   main=sc.labels['D0'], parent='D0')
        if got != {'unused'} or verdict(SD, got) != 'survived':
            fails.append('negative control: unrelated failure under D0 %s scored %s' % (
                sorted(got), verdict(SD, got)))
        # the reference slot is validated chunk by chunk, so a long identifier-shaped line beside a
        # downgraded claim costs linear time (a backtracking slot took minutes on such lines)
        long_line = 'The bound holds at ' + 'https://github.com/o/r/pull/885/files/ab1/' * 40
        t0 = time.monotonic()
        got = case('D-long identifier lines beside a downgraded claim', rec(note(), _manifest(
            {}, retired={m0: dg0}), {b'rec/long.md': ('100644', (
                long_line + '\n' + 'a1' * 4000 + '\n' + '#1 ' * 3000 + '\n').encode())}),
            main=sc.labels['D0'], parent='D0')
        if got != {SD} or time.monotonic() - t0 > 10:
            fails.append('downgrade, long identifier lines: %s in %.1f s' % (
                sorted(got), time.monotonic() - t0))
        n_down += 1
        # neither the link reduction nor a statement's prefix rescans what came before it
        for label, blob in (('a 100,000-bracket line', '[' * 100000 + '\nThe bound holds.\n'),
                            ('a 40,000-character marker run before 200 statements',
                             '-' * 40000 + ' x\n' + ''.join(
                                 'If n <= %d, the bound holds at run #%d.\n' % (k, k)
                                 for k in range(200)) + 'The bound holds.\n')):
            t0 = time.monotonic()
            got = case('D-long input: ' + label, rec(note(), _manifest(
                {}, retired={m0: dg0}), {b'rec/long.md': ('100644', blob.encode())}),
                main=sc.labels['D0'], parent='D0')
            if got != {SD} or time.monotonic() - t0 > 10:
                fails.append('downgrade, %s: %s in %.1f s' % (label, sorted(got),
                                                              time.monotonic() - t0))
            n_down += 1
        # a prefix is read back at most 300 characters and a reference slot at most 300, so 5,000
        # narrowed statements in one sentence, or in one paragraph each after its slot, cost
        # linear time; and the verbatim test reads the tree once for any number of records
        many = 5000
        recs = [dg0] + [dict(dg0, from_claim='rec/NOTE.md:%d' % (k + 2),
                             from_claim_sha256=line_sha256(b'%d' % k)) for k in range(1, many)]
        for label, fixture, blobs, records in (
                ('5,000 narrowed statements in one sentence', 'DQ', {b'rec/long.md': (
                    ''.join('if n <= %d, the bound holds at run #%d, ' % (k, k)
                            for k in range(many)) + '\n\nthe bound holds at run #0\n')}, None),
                ('5,000 narrowed statements in one paragraph, each after its slot', 'DL', {
                    b'rec/long.md': ''.join('If n <= %d, #%d: the bound holds.\n' % (k, k)
                                            for k in range(many))
                    + '\nrun #0: the bound holds.\n'}, None),
                ('5,000 records of one id, 5,000 lines carrying it elsewhere', 'D0', {
                    b'evidence/runs.md': ''.join('run %d at %s\n' % (k, m0)
                                                 for k in range(many))}, recs)):
            h = json.loads(sc.files[fixture][b'rec/CITATIONS.json'][1])['ids'][m0]['claim_sha256']
            body = rec(note(), _manifest({}, retired={m0: records or dict(
                dg0, from_claim_sha256=h)}), {f: ('100644', t.encode()) for f, t in blobs.items()})
            t0 = time.monotonic()
            got = case('D-bounded time: ' + label, body, main=sc.labels[fixture], parent=fixture)
            want = set() if records else {SD}
            if got != want or time.monotonic() - t0 > 10:
                fails.append('downgrade, bounded time, %s: %s in %.1f s' % (
                    label, sorted(got), time.monotonic() - t0))
            n_down += 1
        dl = sc.labels['D-record, the claim removed']
        for name, sets, want in (
                ('after a landed downgrade', {b'rec/more.md': ('100644', b'more\n')}, set()),
                ('a landed record whose claim comes back', {b'rec/back.md': (
                    '100644', (claim_line + '\n').encode())}, {SD})):
            got = case('D-' + name, sets, main=dl, parent='D-record, the claim removed')
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))

        # main resolved from real refs, with HEAD at the commit under check: origin/main is
        # preferred over a stale local main, local main is used alone, and with neither every id
        # is checked as landing. L lists gone2 as provenance; M0 does not.
        sc.git(['symbolic-ref', 'HEAD', 'refs/heads/work'])
        sc.git(['update-ref', 'refs/heads/work', lid])
        for name, origin, local, want_main, want in (
                ('origin/main at the commit under check, local main stale', lid, m0, lid, set()),
                ('origin/main without the id, local main with it', m0, lid, m0, {'absent'}),
                ('local main only', None, lid, lid, set()),
                ('neither ref', None, None, None, {'absent'})):
            for ref, at in (('refs/remotes/origin/main', origin), ('refs/heads/main', local)):
                sc.git(['update-ref', ref, at] if at else ['update-ref', '-d', ref])
            try:
                problems, _n, _i, got_main = check_against_main(sc.repo, lid)
                got = {code for _m, code, _o, _f in problems}
            except Exception as e:          # noqa: BLE001
                got, got_main = {'crash:' + type(e).__name__}, '?'
            if got_main != want_main or got != want:
                fails.append('refs, %s: main %s, codes %s' % (name, got_main, sorted(got)))
    for f in fails:
        print('SELF-TEST  FAIL  %s' % f)
    print('citation_roles_check: self-test %s (%d mutants, %d positives, 3 negative controls, '
          '6 landing, 3 submodule, %d downgrade and 4 main-ref cases)' % (
              'OK' if not fails else 'FAILED', len(mutants), len(positives), n_down))
    return not fails


def main(argv):
    if argv == ['--self-test']:
        return 0 if self_test() else 1
    if len(argv) != 1:
        print(__doc__.split('\n\n')[1])
        return 2
    try:
        c = v3.check_oid(argv[0])
    except v3.Refused as rf:
        print('citation_roles_check: refused (%s)' % rf.code)
        return 2
    if not self_test():
        return 1
    repo = v3.Repo(os.getcwd())
    try:
        problems, n_man, n_ids, main_c = check_against_main(repo, c)
    except v3.Undecidable as u:
        print('CITATIONS  UNDECIDABLE  %s' % u.code)
        return 1
    for m, code, oid, f in problems:
        print('CITATION  %s  %s  %s  %s' % (m, code, oid, f))
    if main_c is None:
        print('CITATIONS  no main ref: every provenance id checked as landing')
    print('CITATIONS  %d manifest(s), %d id(s), %s' % (
        n_man, n_ids, 'all hold' if not problems else '%d problem(s)' % len(problems)))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

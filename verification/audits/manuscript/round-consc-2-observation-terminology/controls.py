"""CONSC-2 frozen controls (stage C1).

Self-contained: the round's 34 substitution instances (19 frozen pairs; every book pair applied to its chapter
source and to FULL.md) are embedded below as INSTANCES, with the frozen blobs of the eight edited sources and the
four rebuilt .tex artifacts at E, the frozen re-grep table, and the scan lists.

usage:
  controls.py check <commit> [--freeze F]   run every check of the preregistration on <commit> (S1 or E)
  controls.py --self-test                    drive every check through a passing tree and a set of mutations

Checks (codes as in the preregistration):
  P  paths      delta(D, commit) is exactly the sixteen governed execution paths (all modified) plus files of the
                record directory
  I  instances  at D every old occurs exactly once in its file and its new does not occur
  S  sources    each of the eight sources at commit equals D's with exactly its instances substituted, and has its
                frozen blob
  M  mirror     every non-blank line of each edited chapter occurs in FULL.md; each book pair's new text occurs
                exactly once in its chapter and exactly once in FULL.md (hard parity)
  T  tex        each rebuilt .tex carries the source-sha256 stamp of its .md at commit and has its frozen blob
  B  pdf        each rebuilt .pdf is a PDF and differs from D's (rebuilt, not carried over)
  R  register   A.32/A.33 scan of the paper pairs' new text; revision-history and caps scans of every new text;
                no out-of-scope term in any new text
  G  re-grep    corpus-wide counts (papers/*.md, book/*.md) at commit equal the frozen E column; the invariant
                phrases (counts, axiom counts, ledger) are unchanged from D
  F  freeze     with --freeze F: the preregistration at commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib
import json
import re
import subprocess
import sys

D = '1a5752d07057895dfa7d793d11a197691bf27a0d'
RDIR = 'verification/audits/manuscript/round-consc-2-observation-terminology/'
PREREG = RDIR + 'preregistration.md'
RECORD_FILES = {PREREG, RDIR + 'controls.py', RDIR + 'result.md'}
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
CHAPTERS = ['book/ch01-observation.md', 'book/ch03-structural-realism.md', 'book/ch18-beyond.md', 'book/glossary.md']
PAPERS = ['papers/Main.md', 'papers/GR.md', 'papers/Structure.md']
SOURCES = PAPERS + CHAPTERS + [FULL]
BUILT = {'papers/Main.md': 'papers/Main', 'papers/GR.md': 'papers/GR', 'papers/Structure.md': 'papers/Structure',
         FULL: 'book/The-Incompleteness-of-Observation-FULL'}
GOVERNED = set(SOURCES) | {b + ext for b in BUILT.values() for ext in ('.tex', '.pdf')}

INSTANCES = json.loads(r'''[
 {
  "item": "B1",
  "file": "book/ch01-observation.md",
  "old": "This is the *cogito* of Descartes made mathematical — the framework's one concession to a foundation outside its own theorems.",
  "new": "This is the *cogito* of Descartes made mathematical, without its thinking subject — the framework's one concession to a foundation outside its own theorems."
 },
 {
  "item": "B1",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "This is the *cogito* of Descartes made mathematical — the framework's one concession to a foundation outside its own theorems.",
  "new": "This is the *cogito* of Descartes made mathematical, without its thinking subject — the framework's one concession to a foundation outside its own theorems."
 },
 {
  "item": "B2",
  "file": "book/ch01-observation.md",
  "old": "The definition is weaker than classical mechanics. A shuffled deck of cards satisfies it. A finite cellular automaton satisfies it.",
  "new": "The definition is weaker than classical mechanics. A shuffled deck of cards satisfies it. A finite cellular automaton satisfies it. So does a detector or a protein interior: nothing in the definition requires that anyone be aware of an outcome. What cannot be doubted is that *some* differentiated content is registered — that much is secured from within whatever locus raises the doubt. That a particular deck, automaton or detector registers anything is not indubitable but a physical fact, and the definition covers it all the same."
 },
 {
  "item": "B2",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "The definition is weaker than classical mechanics. A shuffled deck of cards satisfies it. A finite cellular automaton satisfies it.",
  "new": "The definition is weaker than classical mechanics. A shuffled deck of cards satisfies it. A finite cellular automaton satisfies it. So does a detector or a protein interior: nothing in the definition requires that anyone be aware of an outcome. What cannot be doubted is that *some* differentiated content is registered — that much is secured from within whatever locus raises the doubt. That a particular deck, automaton or detector registers anything is not indubitable but a physical fact, and the definition covers it all the same."
 },
 {
  "item": "B3",
  "file": "book/ch01-observation.md",
  "old": "In particular, whether the embedded observer's status as a *proper part* of a larger whole is best regarded as following from the first axiom or as a further foundational posit in its own right is an open question — one that bears on how the framework describes the minimality of its own assumptions, but not on any prediction it makes.",
  "new": "In particular, whether the embedded observer's status as a *proper part* of a larger whole follows from the first axiom or is a further foundational posit in its own right turns on how the first axiom is read. The framework adopts the reading on which the registering occurs from a locus against a remainder, so that embeddedness follows; on a thinner reading it would be a third posit. The choice bears on how the framework counts its assumptions, not on any prediction it makes."
 },
 {
  "item": "B3",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "In particular, whether the embedded observer's status as a *proper part* of a larger whole is best regarded as following from the first axiom or as a further foundational posit in its own right is an open question — one that bears on how the framework describes the minimality of its own assumptions, but not on any prediction it makes.",
  "new": "In particular, whether the embedded observer's status as a *proper part* of a larger whole follows from the first axiom or is a further foundational posit in its own right turns on how the first axiom is read. The framework adopts the reading on which the registering occurs from a locus against a remainder, so that embeddedness follows; on a thinner reading it would be a third posit. The choice bears on how the framework counts its assumptions, not on any prediction it makes."
 },
 {
  "item": "B4",
  "file": "book/ch03-structural-realism.md",
  "old": "from the framework's foundational empirical commitment to its specific predictive content",
  "new": "from the framework's foundational commitment to its specific predictive content"
 },
 {
  "item": "B4",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "from the framework's foundational empirical commitment to its specific predictive content",
  "new": "from the framework's foundational commitment to its specific predictive content"
 },
 {
  "item": "B5",
  "file": "book/ch03-structural-realism.md",
  "old": "At the broadest level, the framework commits only to the empirical fact that observation occurs;",
  "new": "At the broadest level, the framework commits only to the fact that observation occurs;"
 },
 {
  "item": "B5",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "At the broadest level, the framework commits only to the empirical fact that observation occurs;",
  "new": "At the broadest level, the framework commits only to the fact that observation occurs;"
 },
 {
  "item": "B6",
  "file": "book/ch03-structural-realism.md",
  "old": "is the empirical fact that observation occurs: an observer records distinguishable outcomes",
  "new": "is that observation occurs: an observer records distinguishable outcomes"
 },
 {
  "item": "B6",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "is the empirical fact that observation occurs: an observer records distinguishable outcomes",
  "new": "is that observation occurs: an observer records distinguishable outcomes"
 },
 {
  "item": "B6",
  "file": "book/ch03-structural-realism.md",
  "old": "This Cartesian *cogito*, made mathematically precise, is the one premise the framework takes from outside its own theorems.",
  "new": "Its indubitable core — that some differentiated content is registered — is the Cartesian *cogito*, made mathematically precise and without its thinking subject; it is the one premise the framework takes from outside its own theorems. The structure Level A adds to that core is that of the Chapter 1 definition, and it is physical, not mental."
 },
 {
  "item": "B6",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "This Cartesian *cogito*, made mathematically precise, is the one premise the framework takes from outside its own theorems.",
  "new": "Its indubitable core — that some differentiated content is registered — is the Cartesian *cogito*, made mathematically precise and without its thinking subject; it is the one premise the framework takes from outside its own theorems. The structure Level A adds to that core is that of the Chapter 1 definition, and it is physical, not mental."
 },
 {
  "item": "B7",
  "file": "book/ch03-structural-realism.md",
  "old": "the first axiom costs nothing precisely because it is the bare fact of registration itself;",
  "new": "the first axiom costs nothing precisely because it is the bare fact that difference is registered at all;"
 },
 {
  "item": "B7",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "the first axiom costs nothing precisely because it is the bare fact of registration itself;",
  "new": "the first axiom costs nothing precisely because it is the bare fact that difference is registered at all;"
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "The framework provides structural necessary conditions for consciousness without specifying sufficient conditions.",
  "new": "The framework provides structural necessary conditions for consciousness without specifying sufficient conditions. The two directions below differ in standing: Direction 2 follows from the definition of observation, which detectors and horizons satisfy; Direction 1 is a conjecture about consciousness, motivated by the role of memory in conscious information processing, and not a theorem of the framework. Evidence in the framework's sense is perspective-neutral — a record bears its evidential relations through its correlations at the partition, whether or not a conscious system takes it up; whether evidence as experienced requires a conscious perspective is an epistemological question the framework does not address."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "The framework provides structural necessary conditions for consciousness without specifying sufficient conditions.",
  "new": "The framework provides structural necessary conditions for consciousness without specifying sufficient conditions. The two directions below differ in standing: Direction 2 follows from the definition of observation, which detectors and horizons satisfy; Direction 1 is a conjecture about consciousness, motivated by the role of memory in conscious information processing, and not a theorem of the framework. Evidence in the framework's sense is perspective-neutral — a record bears its evidential relations through its correlations at the partition, whether or not a conscious system takes it up; whether evidence as experienced requires a conscious perspective is an epistemological question the framework does not address."
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "None of these is conscious in any phenomenal sense — there is nothing it is like to be the cosmological horizon.",
  "new": "Nothing in the framework attributes phenomenal experience to any of them."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "None of these is conscious in any phenomenal sense — there is nothing it is like to be the cosmological horizon.",
  "new": "Nothing in the framework attributes phenomenal experience to any of them."
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "implement observation structurally without being conscious.",
  "new": "implement observation structurally, and nothing in the definition requires that they be conscious."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "implement observation structurally without being conscious.",
  "new": "implement observation structurally, and nothing in the definition requires that they be conscious."
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "The framework's necessary-condition account makes empirical predictions about the structural features conscious systems should exhibit.",
  "new": "The framework's necessary-condition conjecture implies structural expectations about the features conscious systems should exhibit; they are consistency checks on the conjecture, not evidence for the framework."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "The framework's necessary-condition account makes empirical predictions about the structural features conscious systems should exhibit.",
  "new": "The framework's necessary-condition conjecture implies structural expectations about the features conscious systems should exhibit; they are consistency checks on the conjecture, not evidence for the framework."
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "the arrow of time, consciousness as structural necessary condition.",
  "new": "and the arrow of time. The consciousness conjecture of §18.10 is not part of this case."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "the arrow of time, consciousness as structural necessary condition.",
  "new": "and the arrow of time. The consciousness conjecture of §18.10 is not part of this case."
 },
 {
  "item": "B8",
  "file": "book/ch18-beyond.md",
  "old": "The framework's content beyond conventional physics is not speculative addition to an empirical base but structural extension of the same framework that produced the empirical predictions of Chapters 5-17.",
  "new": "The framework's physical content beyond conventional physics is structural extension of the same framework that produced the empirical predictions of Chapters 5-17, not speculative addition to an empirical base."
 },
 {
  "item": "B8",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "The framework's content beyond conventional physics is not speculative addition to an empirical base but structural extension of the same framework that produced the empirical predictions of Chapters 5-17.",
  "new": "The framework's physical content beyond conventional physics is structural extension of the same framework that produced the empirical predictions of Chapters 5-17, not speculative addition to an empirical base."
 },
 {
  "item": "B9",
  "file": "book/glossary.md",
  "old": "The framework's technical term for an observer who is a substructure of the system they are trying to describe — coupled to the system, bounded in extent, unable to access the full state from outside.",
  "new": "The framework's technical term for an observer that is a proper subsystem of the system it registers — coupled to the system, bounded in extent, unable to access the full state from outside. A detector, a protein interior or a cosmological horizon qualifies; nothing in the definition requires consciousness."
 },
 {
  "item": "B9",
  "file": "book/The-Incompleteness-of-Observation-FULL.md",
  "old": "The framework's technical term for an observer who is a substructure of the system they are trying to describe — coupled to the system, bounded in extent, unable to access the full state from outside.",
  "new": "The framework's technical term for an observer that is a proper subsystem of the system it registers — coupled to the system, bounded in extent, unable to access the full state from outside. A detector, a protein interior or a cosmological horizon qualifies; nothing in the definition requires consciousness."
 },
 {
  "item": "P1",
  "file": "papers/Main.md",
  "old": "the cogito made precise, which is irreducibly perspectival: a doubting *I*, not a free-floating fact. Read this way, the primitive already contains three things that therefore need no separate derivation: a differentiation (the this-not-that), a locus that registers it (the observer), and the remainder it is registered against.",
  "new": "the cogito made precise, which is irreducibly perspectival: a registering from a locus, not a free-floating fact, and not a thinking subject — the primitive asserts no *I* (companion methodology paper, §2.3). Read this way, the primitive already contains three things that therefore need no separate derivation: a differentiation (the this-not-that), a locus that registers it (the observer of the Definition below), and the remainder it is registered against. The indubitability is the warrant available to whatever locus raises the doubt; the Definition covers every registering locus, and for a detector or a horizon that a registering occurs is a physical fact, not an indubitable one."
 },
 {
  "item": "P2",
  "file": "papers/Main.md",
  "old": "The axiom thus commits to our universe being in the observer-admitting subset of substrata — substrata whose bijection structure satisfies the conditions C1–C4 below for some partition.",
  "new": "Applied to our universe, the starting point thus carries a further commitment: that our universe lies in the observer-admitting subset of substrata — substrata whose bijection structure satisfies the conditions C1–C4 below for some partition. This is the C1–C4 selection condition, not a consequence of the first axiom: a momentary registering with no persistent record satisfies the first axiom and fails C2."
 },
 {
  "item": "P3",
  "file": "papers/Structure.md",
  "old": "The framework begins with the empirical fact that *observation occurs* [Main §1].",
  "new": "The framework begins with the fact that *observation occurs* [Main §1]."
 },
 {
  "item": "P4",
  "file": "papers/GR.md",
  "old": "(the empirical fact that observation occurs, the empirical inputs E1–E4, and the structural assumptions A1–A6)",
  "new": "(the fact that observation occurs, the empirical inputs E1–E4, and the structural assumptions A1–A6)"
 }
]''')

SOURCE_BLOBS_AT_E = json.loads(r'''{
 "papers/Main.md": "82ff483e666315a1d5c6f93d74c498d56f9aa948",
 "papers/GR.md": "a4a2e53e9c7c0c725122ba4927c903ac73ea9bdc",
 "papers/Structure.md": "7d571eea27389c0acc56f8921a4b95f3fe0330be",
 "book/ch01-observation.md": "9e64606ff0c9a65130cf58165eb1bfa69159c7b6",
 "book/ch03-structural-realism.md": "2eba44b5b1d640a3c4533639fce6772de3d34df1",
 "book/ch18-beyond.md": "8227ef0b20983c4e7854b872a7dbee579c76d330",
 "book/glossary.md": "32d0b6dc1173b2841be3fad0b6c00f7131bfe6ee",
 "book/The-Incompleteness-of-Observation-FULL.md": "2c0203551bf492299ef4b0e20cd6b03bf43f029b"
}''')
TEX_BLOBS_AT_E = json.loads(r'''{
 "papers/Main.tex": "7209e49a46f3b6db16155b85596fc9cfb8bfe5bc",
 "papers/GR.tex": "98bde4cc7a3542e179c36222c1a0c83157a5ad9b",
 "papers/Structure.tex": "5d84b24a050b42d789adb928473f8d9d2891d66b",
 "book/The-Incompleteness-of-Observation-FULL.tex": "61eae937f54b08781f159e15d761767a4792f94d"
}''')

# phrase -> (count at D, count at E), corpus = papers/*.md + book/*.md
REGREP = json.loads(r'''{
 "a doubting *I*": [
  1,
  0
 ],
 "empirical fact that observation occurs": [
  5,
  0
 ],
 "foundational empirical commitment": [
  2,
  0
 ],
 "is an open question — one that bears on how the framework describes the minimality": [
  2,
  0
 ],
 "nothing it is like to be the cosmological horizon": [
  2,
  0
 ],
 "consciousness as structural necessary condition": [
  2,
  0
 ],
 "is not speculative addition to an empirical base": [
  2,
  0
 ],
 "who is a substructure of the system they are trying to describe": [
  2,
  0
 ],
 "The axiom thus commits": [
  1,
  0
 ],
 "without its thinking subject": [
  0,
  4
 ],
 "nothing in the definition requires": [
  0,
  6
 ],
 "C1–C4 selection condition": [
  0,
  1
 ],
 "two-axiom": [
  23,
  23
 ],
 "two axioms": [
  35,
  35
 ],
 "Seven items": [
  1,
  1
 ],
 "posit ledger": [
  8,
  8
 ],
 "third axiom": [
  3,
  3
 ],
 "cogito": [
  11,
  11
 ]
}''')
INVARIANT = ['two-axiom', 'two axioms', 'Seven items', 'posit ledger', 'third axiom', 'cogito']

REGISTER = [r'discipline', r'honest', r'should not be read', r'the reader should', r'neither borrows', r'temptation']
HISTORY = [r'\bnow\b', r'no longer', r'current form', r'corrected form', r'as redefined', r'is now settled',
           r'formerly', r'withdraw', r'earlier draft', r'previously', r'earlier revision']
CAPS = re.compile(r'(?<![\w$\\{(*])[A-Z]{4,}(?![\w}])')
OUT_OF_SCOPE = ['feed-forward', 'feed forward', 'Appendix C', 'posit ledger', 'ledger', 'Lean', 'kernel',
                'eight items', 'Seven items', 'three axioms']

FAILS = []
COUNT = [0]


def check(code, label, ok):
    COUNT[0] += 1
    if not ok:
        FAILS.append((code, label))
    print('  %s  %-2s %s' % ('PASS' if ok else 'FAIL', code, label))


def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, text=True)


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def blob(commit, path):
    r = git('rev-parse', '%s:%s' % (commit, path))
    return r.stdout.strip() if r.returncode == 0 else None


def tree_text(commit, paths):
    out = {}
    for p in paths:
        b = show(commit, p)
        out[p] = None if b is None else b.decode('utf-8')
    return out


def corpus(commit):
    r = git('ls-tree', '-r', '--name-only', commit, 'papers', 'book')
    names = [n for n in r.stdout.split() if re.fullmatch(r'(papers|book)/[^/]+\.md', n)]
    return tree_text(commit, names)


def git_blob_id(text):
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()


# ---------------------------------------------------------------- pure checks over {path: text}
def instances_at_D(d_tree):
    bad = []
    for i, x in enumerate(INSTANCES):
        t = d_tree.get(x['file']) or ''
        if t.count(x['old']) != 1 or t.count(x['new']) != 0:
            bad.append(i)
    return bad


def expected(d_tree):
    out = {}
    for f in SOURCES:
        t = d_tree[f]
        for x in INSTANCES:
            if x['file'] == f:
                t = t.replace(x['old'], x['new'], 1)
        out[f] = t
    return out


def sources_ok(d_tree, c_tree):
    exp = expected(d_tree)
    return [f for f in SOURCES if c_tree.get(f) != exp[f]]


def source_blobs_ok(c_tree):
    return [f for f in SOURCES if c_tree.get(f) is None or git_blob_id(c_tree[f]) != SOURCE_BLOBS_AT_E[f]]


def mirror_ok(c_tree):
    full = c_tree.get(FULL) or ''
    missing = []
    for ch in CHAPTERS:
        for line in (c_tree.get(ch) or '').splitlines():
            if line.strip() and line not in full:
                missing.append((ch, line[:60]))
    return missing


def parity_ok(c_tree):
    bad = []
    for x in INSTANCES:
        if x['item'].startswith('B'):
            ch = [y['file'] for y in INSTANCES if y['item'] == x['item'] and y['old'] == x['old'] and y['file'] != FULL]
            a = (c_tree.get(ch[0]) or '').count(x['new'])
            b = (c_tree.get(FULL) or '').count(x['new'])
            if (a, b) != (1, 1):
                bad.append((x['item'], a, b))
    return bad


def stamp_ok(md_text, tex_text):
    m = re.search(r'^% source-sha256: ([0-9a-f]{64})\s*$', tex_text or '', re.M)
    return bool(m) and m.group(1) == hashlib.sha256(md_text.encode('utf-8')).hexdigest()


def scan(texts):
    """texts: list of (item, file, new). Returns the hits."""
    hits = []
    for item, f, t in texts:
        pats = HISTORY + (REGISTER if f.startswith('papers/') else [])
        for p in pats:
            if re.search(p, t, re.I):
                hits.append((item, 'phrase', p))
        for m in CAPS.finditer(t):
            hits.append((item, 'caps', m.group()))
        for term in OUT_OF_SCOPE:
            if term in t:
                hits.append((item, 'scope', term))
    return hits


def regrep(c_corpus):
    return {p: sum(t.count(p) for t in c_corpus.values() if t) for p in REGREP}


def paths_ok(rows, final):
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    if not rec <= RECORD_FILES:
        return False
    if final:
        return exec_rows == {p: 'M' for p in GOVERNED}
    return set(exec_rows) <= GOVERNED and all(s == 'M' for s in exec_rows.values())


# ---------------------------------------------------------------- the commit check
def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [tuple(l.split('\t')) for l in r.stdout.splitlines() if l]
    check('P', 'delta(D, commit) is exactly the sixteen governed execution paths plus record files',
          r.returncode == 0 and paths_ok(rows, True))
    d_tree = tree_text(D, SOURCES)
    c_tree = tree_text(commit, SOURCES)
    check('I', 'at D every old occurs once in its file and its new does not occur (%d instances)' % len(INSTANCES),
          not instances_at_D(d_tree))
    bad = sources_ok(d_tree, c_tree)
    check('S', 'each source equals D\'s with exactly its instances substituted%s' % (' %s' % bad if bad else ''),
          not bad)
    bad = source_blobs_ok(c_tree)
    check('S', 'each source has its frozen blob%s' % (' %s' % bad if bad else ''), not bad)
    miss = mirror_ok(c_tree)
    check('M', 'every non-blank line of the edited chapters occurs in FULL.md%s' % (' %s' % miss[:2] if miss else ''),
          not miss)
    bad = parity_ok(c_tree)
    check('M', 'every book pair\'s new text occurs once in its chapter and once in FULL.md%s' % (' %s' % bad if bad else ''),
          not bad)
    for md, base in BUILT.items():
        tex = show(commit, base + '.tex')
        tex = tex.decode('utf-8') if tex is not None else None
        check('T', '%s.tex stamp matches its source' % base, stamp_ok(c_tree[md], tex))
        check('T', '%s.tex has its frozen blob' % base, blob(commit, base + '.tex') == TEX_BLOBS_AT_E[base + '.tex'])
        pdf = show(commit, base + '.pdf')
        check('B', '%s.pdf is a PDF rebuilt at this commit' % base,
              pdf is not None and pdf.startswith(b'%PDF-') and blob(commit, base + '.pdf') != blob(D, base + '.pdf'))
    hits = scan([(x['item'], x['file'], x['new']) for x in INSTANCES])
    check('R', 'register, history, caps and scope scans of the new text are clean%s' % (' %s' % hits if hits else ''),
          not hits)
    got = regrep(corpus(commit))
    d_got = regrep(corpus(D))
    bad = [p for p in REGREP if (d_got[p], got[p]) != tuple(REGREP[p])]
    check('G', 'corpus re-grep equals the frozen D and E columns%s' % (' %s' % bad if bad else ''), not bad)
    bad = [p for p in INVARIANT if d_got[p] != got[p]]
    check('G', 'invariant phrases unchanged from D%s' % (' %s' % bad if bad else ''), not bad)
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


# ---------------------------------------------------------------- self-test
def must(code, label, ok):
    check(code, label, ok)


def self_test():
    d_tree = tree_text(D, SOURCES)
    must('I', 'the instances hold at D', not instances_at_D(d_tree))
    e_tree = expected(d_tree)
    must('S', 'the predicted E sources pass the substitution check', not sources_ok(d_tree, e_tree))
    must('S', 'the predicted E sources have the frozen blobs', not source_blobs_ok(e_tree))
    must('M', 'the predicted E tree passes mirror and parity', not mirror_ok(e_tree) and not parity_ok(e_tree))
    must('S', 'countercontrol: D itself fails the substitution check', bool(sources_ok(d_tree, d_tree)))
    # mutation: the FULL.md side of one book pair omitted
    b2 = next(x for x in INSTANCES if x['item'] == 'B2' and x['file'] == FULL)
    m = dict(e_tree)
    m[FULL] = m[FULL].replace(b2['new'], b2['old'], 1)
    must('M', 'a chapter edit without its FULL.md pair fails parity and substitution',
         bool(parity_ok(m)) and bool(sources_ok(d_tree, m)))
    # mutation: an extra edit outside the frozen instances
    m = dict(e_tree)
    m['book/ch18-beyond.md'] = m['book/ch18-beyond.md'].replace('Penrose', 'Penrose-', 1)
    must('S', 'an extra edit in a governed source fails', bool(sources_ok(d_tree, m)))
    # mutation: a chapter line missing from FULL.md
    m = dict(e_tree)
    m['book/ch01-observation.md'] = m['book/ch01-observation.md'] + '\nAn unmirrored line.\n'
    must('M', 'a chapter line absent from FULL.md fails the mirror check', bool(mirror_ok(m)))
    # scans: a neutral text passes; prohibited texts fail
    must('R', 'a neutral new text passes the scans', not scan([('X', 'papers/Main.md', 'The definition covers every registering locus.')]))
    must('R', 'revision-history voice fails', bool(scan([('X', 'book/ch01-observation.md', 'The axiom is no longer called empirical.')])))
    must('R', 'meta-commentary in a paper fails', bool(scan([('X', 'papers/Main.md', 'The discipline maintained throughout.')])))
    must('R', 'caps emphasis fails', bool(scan([('X', 'papers/Main.md', 'This is NEVER a premise.')])))
    must('R', 'an out-of-scope term fails', bool(scan([('X', 'book/ch18-beyond.md', 'A feed-forward network fails C2.')])))
    # stamps
    must('T', 'a stale .tex stamp fails', not stamp_ok('a', '% source-sha256: ' + hashlib.sha256(b'b').hexdigest()))
    must('T', 'a matching .tex stamp passes', stamp_ok('a', '% source-sha256: ' + hashlib.sha256(b'a').hexdigest()))
    # paths
    good = [('M', p) for p in sorted(GOVERNED)] + [('A', PREREG)]
    must('P', 'the governed delta passes', paths_ok(good, True))
    must('P', 'a delta touching a non-governed path fails', not paths_ok(good + [('M', 'papers/Methodology.md')], True))
    must('P', 'a delta missing a rebuilt artifact fails', not paths_ok([r for r in good if r[1] != 'papers/GR.pdf'], True))
    # re-grep: an injected invariant phrase is caught
    c = corpus(D)
    base = regrep(c)
    c2 = dict(c)
    c2['book/ch01-observation.md'] = c2['book/ch01-observation.md'] + ' two axioms'
    must('G', 'an injected invariant phrase changes the invariant count', regrep(c2)['two axioms'] != base['two axioms'])
    must('G', 'the frozen D column matches D', all(base[p] == REGREP[p][0] for p in REGREP))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        self_test()
    elif len(a) >= 2 and a[0] == 'check':
        fz = a[a.index('--freeze') + 1] if '--freeze' in a else None
        run_check(a[1], fz)
    else:
        print(__doc__)
        sys.exit(2)
    print('controls: %s -- %d checks' % ('OK' if not FAILS else 'FAIL (%d)' % len(FAILS), COUNT[0]))
    sys.exit(1 if FAILS else 0)

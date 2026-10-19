#!/usr/bin/env python3
"""check_retention.py -- verifies the evidence-retention archive from the repository tree alone.

No network or third-party package is used, and the check uses no git history. From the repository root:

    python3 -I verification/audits/evidence-retention/check_retention.py           # check, exit 1 on any failure
    python3 -I verification/audits/evidence-retention/check_retention.py --self-test
    python3 -I verification/audits/evidence-retention/check_retention.py --later-provenance   # R10, uses git
    python3 -I verification/audits/evidence-retention/check_retention.py --module-sets   # R11, uses git
    python3 -I verification/audits/evidence-retention/check_retention.py --gate   # the release-gate step, uses git

Rules:
  R1  every listed file exists, and its size and sha256 are the recorded ones;
  R2  a "complete-as-cited" file has exactly the digest the citing record names, and that digest is one of the
      tokens its citations carry;
  R3  every citing file exists with its recorded git blob id (the historical record is unchanged), its cited line
      holds every recorded token, and every claim's text stands verbatim on the line it names;
  R4  every results.json is well formed: its schema, its run (id and head commit equal to the entry's run.json, and
      its job the Mathlib bridge job of the attested attempt), a recorded build, a gate with steps and a verdict,
      every governed module with a status consistent with its reports and #print axioms lines, every report's
      axioms a list or null, marker counts for every marker, and the reproduction recipe;
  R5  no file in the archive directory matches the secret patterns, an IPv4 address or an e-mail address;
  R6  every file in the archive directory is listed, or is README.md, manifest.json or this checker;
      R5 and R6 do not walk objects/, the retained off-main git objects, when objects/manifest.json is a listed
      file: that manifest is pinned here by size and sha256, and check_objects.py, also listed, verifies every
      file under objects/ against it (its O2 and O6 are R6 and R5 for those files);
  R7  the manifest is well formed: known kinds and claim statuses, paths inside the archive, every entry but the
      tranche's own record cited and only it uncited, every citing location annotated, every gap naming an entry;
  R8  each CI entry's files agree: its results.json is a Mathlib bridge result (kind "bridge"); every job in
      jobs.json is at the run's head commit; every partial or missing set of axiom reports, and every missing
      job list, is a recorded gap; a BG-3 entry's results and run metadata name the run, job and head commit of
      its provenance, and its results derive from its log;
  R9  coverage, recomputed from the tree: every receipt, and every certificate attestation citing runs, is
      covered or named as later than this tranche, and every one an entry cites is covered; every check-run
      attestation in a covered receipt, and every run of a covered certificate attestation, has an entry whose
      run metadata matches it; and covered files keep their blob ids. A path named as later must say where its
      evidence is retained, and may be neither covered nor cited by the tranche;
  R10 (with git history) the tranche base is in the repository and an ancestor of HEAD, and no path named as
      later existed at the base: the tree cannot order commits, so this is the independent check that a receipt
      named as later did land after this tranche. In history mode (--gate) R9's scope is read from git instead of
      the tree: every receipt, and every certificate attestation citing runs, that existed at the base must be
      covered, nothing else may be, and a receipt landed after the base is out of scope without a declaration.
  R11 (with git history; run by --module-sets and --gate) every expected result's module table is the set of Lean
      modules its run's rounds govern, re-derived from the rounds' records rather than from the archive. The
      receipts and certificate attestations at the tranche base, read from git and not from the manifest, fix
      the runs to check, the rounds that attest each run and the commit each attests, which must be the expected
      result's. The runs with a checked bridge result must be exactly the runs they attest, whatever the archive
      classifies its results as: a run with several bridge results has each checked, and counts once. For a
      receipt, each control-plane file is read at that commit and must be the blob the receipt pins; their
      v3-governed-paths block, its opener and closer recognized as G10 states and its entries hashed as S7
      states, must hash to the receipt's governed_paths_digest; and its paths under verification/lean-mathlib/
      ending in .lean are the governed modules. S7's validity rules and G10's near-miss rule are not applied
      here: the digest ties the entries to the receipt, whose block the V3 verifier validated. For a certificate
      attestation, which no v3-governed-paths block governs (CV-1's, with verification/certificates/CV1.json),
      the certificate is read at that commit and must be the blob the attestation pins, and the Lean modules
      among its contributions are the governed ones. A governed directory inside verification/lean-mathlib/, or
      one containing it, fails the check: it fixes no module set.
      The table must equal the union over the run's rounds. A CI entry's expected result must be a bridge result.
      Any other expected result is listed as outside the rule's scope, with its reason, only when no attestation
      at the base names its run, and it is of another kind (BG-3's design diagnostic) or its commit is not an
      ancestor of the base (BG-3's design trees, off main). A result of another kind whose run is attested fails;
      so does a bridge result of an unattested run at a commit on main, and one whose commit the repository
      cannot place (a shallow clone).
      R11 is a consistency check, not an independent derivation: build_archive.py read the module sets from the
      same governed-paths blocks, at the tranche base and with its own parser. R11 shows that the archive applied
      those blocks faithfully, as they stand at each run's commit and as the receipts' digests commit to them; it
      cannot show that the governed paths name the right modules.
  R12 each tranche-3 entry (run-<run_id>, a run no receipt or certificate attests, cited for its identity, its
      jobs or what one job printed) is well formed and its files agree: run.json names the run and its head commit,
      and the entry's expiry is its creation plus 90 days; every job in jobs.json is at that commit and attempt,
      with its steps; expected.json, when present, names the same run, head commit, event and attempt, and each
      output names a job of jobs.json, a known kind (base-check, guard), the commit it holds at (the run's head for
      a push; for a pull request the recorded base and the run's head, whose synthetic merge is the REF the log
      reports), a recipe, a source with its digest and line counts and job_outputs.py as extractor, and a well
      formed expectation, a guard's counts agreeing with its checks; the file's source_sha256 is its output's
      served digest. The tranche3 section lists every uncovered run not retained here, once, with its creation
      and expiry, in order of creation; no retained or remaining run is attested or already retained by
      tranches 1-2; no retained run expires after a remaining one (earliest expiry first); and its counts agree.
      R12 does not re-derive an expected result: job_outputs.py reproduce does, at the commit.
  R13 each entry retained ahead of its citing record (research-<run_id>, a research build of a workflow not on main)
      records where it is to be cited (pull request, record, line, head) and carries no citation, and no file of
      the tree outside the archive cites the run (once one does, the entry must carry that citation); its run.json,
      jobs.json and results.json, of kind research-build, name the same run, head commit and attempt and a job of
      jobs.json, and the result derives from the served log whose digest the entry records; the run has no other
      entry; and every item the result does not carry is a recorded gap: each partial or empty target module's
      reports, the release gate (a research build runs none, and R4 requires its result to record none), the design
      files' reports and the exact-control output; and its off-main source commit is retained under objects/ or
      is a recorded gap, not both. Its citation goes through the states check_objects.py's O10 gives a pending
      commit, judged against the tree under check, never against a pull request:
        pending   it records awaiting_citation (pull request, round, record, the line that is to cite the run, and
                  the record's head when the entry was cut) and carries no citation, and its record is not in the
                  tree. This passes, and the entry counts as not cited;
        eligible  the record is in the tree, every line of the tree outside the archive that names the run is in
                  it, the recorded line is one of them and cites the run free-standing, and every line of the record
                  naming the run obeys O10's citation rule (check_objects.run_citations, loaded from that file, so
                  both checkers apply one rule) for the run's head (run.json's head_sha): a free-standing citation
                  states the head (on it and on the line either side, every hex id word is a form of the head and
                  the full head is among them); a line naming the run only inside an identifier or file name is not
                  a citation and names no other head beside it. This passes, is printed as eligible for promotion
                  and counts as not cited: the commit that lands the record need not change this manifest;
        cited     a later archive commit replaces awaiting_citation with citations (R3 and R7 check them); no line
                  is mapped twice; no file outside the mapped ones names the run; in them, every free-standing
                  citation of the run is mapped, every mapped line is one, and every line naming the run obeys the
                  same rule;
        failing   a line outside the record names the run while it is pending; the record is in the tree and does
                  not cite the run, cites it on other lines than recorded or only inside an identifier there, or a
                  line naming it breaks the citation rule; a citation is unmapped or mapped twice once cited; or the
                  run's metadata is missing, not JSON or names no head commit (the lifecycle is not judged then, so
                  such an entry is never eligible).
      The rule's limitation (check_objects.py's docstring): a hex word of 64 digits or more is opaque, so another
      commit's id written as part of one is not read as a head.
      Verbatim mentions (provenance metadata, not a citation mapping). A research entry may carry
      verbatim_mentions: a line of a byte-identical copy of an off-main source that names the run as that source's
      own provenance. It is admitted only when it equals a tuple of VERBATIM_ALLOWLIST, hardcoded below, which
      holds exactly one owner-approved tuple; any other entry, run, path, integer line, blob, source or citation
      context fails, and a further exception needs a reviewed change to that allowlist. The copy must be a regular
      file at exactly the approved path, reached through no symbolic link (no component of the path is a link, and
      it resolves to itself), and, where the root is a git work tree, its index entry must be a regular file
      (100644) at the approved blob. The check hashes the copy's complete bytes itself, as a git blob id (SHA-1)
      and as SHA-256, and compares each with the approved value on its own; it never trusts the manifest's
      digests. The approved line must name the run exactly once, and no other line of the copy may name it. The
      approved line is then left out of the lines that name the run, and every other rule of R13 applies
      unchanged to the rest. A verbatim mention is never a citation: it is not counted as one, it does not satisfy
      awaiting_citation, it makes no entry eligible or cited, no citation of any entry, of any kind, may map the
      copy at any line, the copy may not be the pending record, and it carries no claim. It supports no
      scientific claim; it records why a pinned copy names the run. The self-test checks the same code path with
      stand-in tuples through a seam that is open only while the self-test runs; report() fails if it is open
      before or after its check, gate() if it is open before or after its history-mode check or after its
      self-test, and no flag, environment variable or manifest field reaches it.
The self-test mutates a copy once per failure message of these checks and requires that message; its R10 and R11
cases read the repository's history, and the self-test fails, with a FAIL line, when that history or a commit
the cases read is absent.
The gap list is printed: a gap is recorded, not a failure. R1-R9 check the archive against itself and against the
tree; they do not re-derive an expected result, which reproduce.py does at the commit, and R11 re-derives only
its module set. Whether a claim marked "retained" is carried by the files it names is a reading of those files;
the claim annotations name the files, so a reviewer can make that reading from the tree.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import types

HERE = os.path.dirname(os.path.abspath(__file__))
# R13's citation state of each research-build entry at the last check(): eid -> (pending | eligible | cited, lines)
R13_STATES = {}
_OBJECTS_RULES = None
# R13's verbatim mentions: the owner-approved tuples, and nothing else (2026-10-19, PR #864's pinned copy of F2
# thread I). Each tuple fixes the entry, its run and the run's head, the copy's path, the line naming the run and
# the copy's git blob id (SHA-1) and the SHA-256 of its raw bytes, each checked on its own, the source the copy
# reproduces, and the entry's citation context: its pending citation, or, once promoted, the record lines its
# citations map. Adding or changing a tuple needs the owner's authorization. Both digests were read from the source
# blob at copy_of, fetched from origin, not from the copy.
VERBATIM_ALLOWLIST = (
    {'entry': 'research-38450187534', 'run': '38450187534', 'head': 'e684897da41b1c3d066b880194c9beb87a19b7ad',
     'path': 'verification/programmes/oi-qm/reconstruction/research-planning/x-screen-20261018/src/I.md',
     'line': 378, 'blob': 'f20411d6583a28298aa8647ae456ce787083e31c',
     'sha256': 'ebfa6cdb2c8cfca2c63f8bb608d87627f4d4eded278bcb863385568d9973f2e9',
     'copy_of': {'commit': '804843f16b67061ac258ce00cefa2425d1b688c2',
                 'path': 'verification/programmes/oi-qm/reconstruction/f2-research-threads/I-f2-sufficiency-target.md'},
     'awaiting': {'pull_request': 831, 'round': 'PRESERVE-INDUCT-1',
                  'record': 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/preregistration.md',
                  'line': 69, 'head': '65b85147f85aa01770e0e60551152bc5f1d9ef29'},
     'cited_lines': [69]},
)
VERBATIM_KEYS = {'path', 'line', 'blob', 'sha256', 'copy_of', 'note'}
AWAITING_KEYS = ('pull_request', 'round', 'record', 'line', 'head')
# the self-test's seam: while its verbatim cases run, it substitutes a stand-in tuple, which then goes through the
# same verbatim_filter as the approved one. The substitute is honoured only while _IN_SELF_TEST holds, which
# self_test() alone sets, restoring both in a finally clause. No argument, environment variable or manifest field
# reaches either; report() and gate() fail if either is set outside the self-test.
_VERBATIM_OVERRIDE = None
_IN_SELF_TEST = False
# the verbatim mentions admitted by the last check(): eid -> (path, line)
VERBATIM_STATES = {}


def verbatim_allowlist():
    """The tuples verbatim_filter admits: the hardcoded allowlist, or the self-test's substitute while the
    self-test runs, and never otherwise."""
    return _VERBATIM_OVERRIDE if _IN_SELF_TEST and _VERBATIM_OVERRIDE is not None else VERBATIM_ALLOWLIST


def git_index_entry(root, path):
    """(mode, blob) of path's stage-0 entry in the git index of the work tree whose top is root; () when root is
    such a work tree and its index holds no single stage-0 entry at that path; None when root is not the top of a git
    work tree or git is not available (the index check then does not apply)."""
    try:
        top = subprocess.run(['git', '-C', root, 'rev-parse', '--show-toplevel'], capture_output=True, text=True)
        if top.returncode or os.path.realpath(top.stdout.strip()) != os.path.realpath(root):
            return None
        ls = subprocess.run(['git', '-C', root, 'ls-files', '-s', '-z', '--', path], capture_output=True)
    except OSError:
        return None
    if ls.returncode:
        return None
    rows = [r for r in ls.stdout.split(b'\0') if r]
    if len(rows) != 1:
        return ()
    meta, _, name = rows[0].partition(b'\t')
    f = meta.decode('ascii', 'replace').split()
    if name.decode('utf-8', 'replace') != path or len(f) != 3 or f[2] != '0':
        return ()
    return f[0], f[1]


def verbatim_seam_leak():
    """A failure message when the self-test's substitute or flag is set outside the self-test, else None."""
    if _VERBATIM_OVERRIDE is not None or _IN_SELF_TEST:
        return 'R13 the verbatim self-test substitute is set outside the self-test'
    return None


def objects_rules():
    """check_objects.py, beside this file, as a module, for its head rule: O10 and R13 apply the same one. Loaded
    from source, so no bytecode is written."""
    global _OBJECTS_RULES
    if _OBJECTS_RULES is None:
        p = os.path.join(HERE, 'check_objects.py')
        mod = types.ModuleType('check_objects_rules')
        mod.__file__ = p
        exec(compile(open(p, encoding='utf-8').read(), p, 'exec'), mod.__dict__)
        _OBJECTS_RULES = mod
    return _OBJECTS_RULES
FIXED = {'README.md', 'manifest.json', 'check_retention.py'}
SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key'
                    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)
RUN_URL = re.compile(r'/actions/runs/(\d+)(?:/attempts/(\d+))?')
MARKERS = ('sorryAx', 'Lean.ofReduceBool', "declaration uses 'sorry'", 'error:')
STATUSES = ('complete', 'partial', 'none', 'absent')


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def inside(rel):
    return isinstance(rel, str) and bool(rel) and not os.path.isabs(rel) and '\\' not in rel and \
        os.path.normpath(rel) == rel and rel.split('/')[0] != '..'


def check(archive, root, scope=None):
    fails = []
    F = fails.append
    R13_STATES.clear()
    VERBATIM_STATES.clear()
    try:
        man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return ['R7 manifest unreadable: %s' % exc], []
    if man.get('schema') != 'oi-evidence-retention' or man.get('version') != 3:
        return ['R7 manifest schema or version'], []
    kinds, statuses = set(man.get('kinds', {})), set(man.get('claim_status', {}))
    listed, ids, texts = set(), set(), {}

    def read_tree(path):
        p = os.path.join(root, path)
        return open(p, 'rb').read() if inside(path) and os.path.isfile(p) else None

    for e in man['entries']:
        eid = e.get('id')
        if not eid or eid in ids:
            F('R7 entry id %r missing or repeated' % eid)
        ids.add(eid)
        is_ci = 'kind' not in e and str(eid).startswith('ci-')
        if not is_ci and e.get('kind') not in kinds:
            F('R7 %s: unknown kind %r' % (eid, e.get('kind')))
        if not e.get('files'):
            F('R7 %s: no files' % eid)
        files = {}
        for f in e.get('files', []):
            rel = f.get('path', '')
            if not inside(rel):
                F('R7 %s: path %r is not inside the archive' % (eid, rel))
                continue
            if f.get('kind', e.get('kind')) not in kinds:
                F('R7 %s: %s has unknown kind %r' % (eid, rel, f.get('kind')))
            listed.add(rel)
            p = os.path.join(archive, rel)
            if not os.path.isfile(p):
                F('R1 %s: %s missing' % (eid, rel))
                continue
            data = open(p, 'rb').read()
            if len(data) != f.get('bytes'):
                F('R1 %s: %s size %d, recorded %r' % (eid, rel, len(data), f.get('bytes')))
            if hashlib.sha256(data).hexdigest() != f.get('sha256'):
                F('R1 %s: %s sha256 differs' % (eid, rel))
            files[rel] = texts[rel] = data.decode('utf-8', 'replace')
            if rel.endswith('/results.json') or (rel.startswith('bg3/results-') and rel.endswith('.json')):
                check_results(eid, rel, files[rel], e, F)
        cites = e.get('citations', [])
        if e.get('kind') != 'complete' and not cites and 'awaiting_citation' not in e:
            F('R7 %s: no citations' % eid)
        if e.get('kind') == 'complete' and cites:
            F('R7 %s: a "complete" entry carries citations' % eid)
        tokens = set()
        for c in cites:
            data = read_tree(c.get('path', ''))
            if data is None:
                F('R3 %s: citing file %s missing' % (eid, c.get('path')))
                continue
            if blob_id(data) != c.get('blob'):
                F('R3 %s: citing file %s changed (blob %s, recorded %s)' % (eid, c['path'], blob_id(data)[:12],
                                                                          str(c.get('blob'))[:12]))
            L = data.decode('utf-8', 'replace').split('\n')
            ln = c.get('line', 0)
            here = L[ln - 1] if isinstance(ln, int) and 0 < ln <= len(L) else None
            if not c.get('tokens'):
                F('R7 %s: %s:%s carries no token' % (eid, c['path'], ln))
            for t in c.get('tokens', []):
                tokens.add(t)
                if len(t) < 6:
                    F('R7 %s: token %r is too short to identify anything' % (eid, t))
                elif here is None or t not in here:
                    F('R3 %s: %s:%s no longer contains %s' % (eid, c['path'], ln, t[:16]))
            if not c.get('claims'):
                F('R7 %s: %s:%s has no claim annotation' % (eid, c['path'], ln))
            for k in c.get('claims') or []:
                n, t = k.get('line', 0), k.get('text', '')
                if len(t) < 3 or not (isinstance(n, int) and 0 < n <= len(L)) or t not in L[n - 1]:
                    F('R3 %s: claim %r is not verbatim at %s:%s' % (eid, t[:40], c['path'], n))
                if k.get('status') not in statuses:
                    F('R7 %s: claim status %r' % (eid, k.get('status')))
                if k.get('status') in ('retained', 'differs') and (not k.get('in') or not set(k['in']) <= set(files)):
                    F('R7 %s: claim %r names files %r outside the entry' % (eid, t[:40], k.get('in')))
                if k.get('status') == 'differs' and not k.get('note'):
                    F('R7 %s: a "differs" claim without a note' % eid)
        if e.get('kind') == 'complete-as-cited':
            f0 = (e.get('files') or [{}])[0]
            if f0.get('sha256') != e.get('cited_digest') or e.get('matches_cited_digest') is not True \
                    or e.get('cited_digest') not in tokens:
                F('R2 %s: not byte-identical to a digest its citations carry' % eid)
            pv = e.get('provenance', {})
            for rel, text in files.items():
                if rel.startswith('bg3/run-'):
                    run = json.loads(text)
                    if str(run.get('id')) != pv.get('run_id') or run.get('head_sha') != pv.get('head_sha') or \
                            rel != 'bg3/run-%s.json' % pv.get('run_id'):
                        F('R8 %s: %s differs from the entry\'s provenance' % (eid, rel))
                if rel.startswith('bg3/results-'):
                    try:
                        rr = json.loads(text).get('run') or {}
                    except ValueError:
                        rr = {}
                    fr = next((f for f in e['files'] if f['path'] == rel), {})
                    if rr.get('id') != pv.get('run_id') or rr.get('head_sha') != pv.get('head_sha') or rr.get('job_id') != pv.get('job_id') \
                            or rel != 'bg3/results-%s.json' % pv.get('job_id') or fr.get('source_sha256') != f0.get('sha256'):
                        F('R8 %s: %s names another run, job or head commit than the entry, or does not derive from its log' % (eid, rel))
        if is_ci:
            check_entry_files(e, files, man, F)
        if str(eid).startswith('run-') or e.get('tranche') == 3:
            check_run_entry(e, files, F)
        if 'verbatim_mentions' in e and eid not in {a['entry'] for a in verbatim_allowlist()}:
            F('R13 %s: verbatim_mentions on an entry outside the owner-approved allowlist' % eid)
        # a verbatim mention is never a citation: no citation of any entry, of any kind, may map an approved copy,
        # at any line, under its path or another path resolving to the same file
        for c in e.get('citations') or []:
            cp = c.get('path') if isinstance(c, dict) else None
            hit = next((a for a in verbatim_allowlist() if isinstance(cp, str) and (cp == a['path'] or (
                inside(cp) and os.path.realpath(os.path.join(root, cp)) ==
                os.path.realpath(os.path.join(root, a['path']))))), None)
            if hit:
                F('R13 %s: a verbatim mention is not a citation, and this entry maps %s:%s, the approved copy %s' % (
                    eid, cp, c.get('line'), hit['path']))
        if str(eid).startswith('research-') and eid != 'research-runs-record' or 'awaiting_citation' in e:
            check_research_entry(e, files, man, archive, root, F)
    for g in man.get('missing', []):
        if g.get('id') not in ids or not g.get('what') or not g.get('why'):
            F('R7 gap %r names no entry, or has no what/why' % g)
    check_coverage(man, archive, root, read_tree, F, scope)
    check_tranche3(man, read_tree, F)
    for dirpath, _, names in os.walk(archive):
        for fn in names:
            rel = os.path.relpath(os.path.join(dirpath, fn), archive).replace(os.sep, '/')
            if '__pycache__' in rel:
                continue
            if rel.startswith('objects/') and rel != 'objects/manifest.json' and 'objects/manifest.json' in listed:
                continue
            if rel not in listed and rel not in FIXED:
                F('R6 unlisted file %s' % rel)
            text = texts.get(rel)
            if text is None:
                text = open(os.path.join(dirpath, fn), 'rb').read().decode('utf-8', 'replace')
            hit = next((i + 1 for i, l in enumerate(text.split('\n')) if SECRET.search(l)), None)
            if hit:
                F('R5 %s:%d matches a secret pattern' % (rel, hit))
    return fails, man.get('missing', [])


def check_results(eid, rel, text, e, F):
    """R4: a results.json is well formed and names what its entry names."""
    try:
        r = json.loads(text)
    except ValueError:
        F('R4 %s: %s is not JSON' % (eid, rel))
        return
    if r.get('schema') != 'oi-evidence-result' or r.get('version') != 1 or \
            r.get('kind') not in ('bridge', 'design-diagnostic', 'research-build'):
        F('R4 %s: %s has an unknown schema, version or kind' % (eid, rel))
        return
    run, exp = r.get('run') or {}, r.get('expected') or {}
    if not run.get('id') or not re.fullmatch(r'[0-9a-f]{40}', str(run.get('head_sha', ''))) or not run.get('job_id'):
        F('R4 %s: %s names no run, head commit or job' % (eid, rel))
    if r['kind'] == 'design-diagnostic':
        if not exp.get('sha256sum_ok') or not exp.get('checks') or not (r.get('reproduce') or {}).get('recipe'):
            F('R4 %s: %s records no checks or no recipe' % (eid, rel))
        return
    if not r.get('source', {}).get('extractor') or not (r.get('reproduce') or {}).get('recipe'):
        F('R4 %s: %s records no extractor or no reproduction recipe' % (eid, rel))
    if exp.get('build_success') is not True:
        F('R4 %s: %s records no successful build' % (eid, rel))
    if r['kind'] == 'research-build':
        # a research workflow runs no release gate: the result records none, and the entry records the gap (R13)
        if exp.get('gate') is not None:
            F('R4 %s: %s is a research build and records a gate' % (eid, rel))
    else:
        g = exp.get('gate') or {}
        if not g.get('verdict') or not g.get('steps') or any(not st.get('name') or st.get('status') not in ('PASS', 'FAIL', 'SKIP')
                                                               for st in g.get('steps', [])):
            F('R4 %s: %s records no gate verdict or malformed gate steps' % (eid, rel))
    mods = exp.get('modules')
    if not isinstance(mods, dict):
        F('R4 %s: %s has no module table' % (eid, rel))
        mods = {}
    for mod, m in mods.items():
        st, reps = m.get('status'), m.get('reports')
        if st not in STATUSES or not isinstance(reps, list):
            F('R4 %s: %s module %s has status %r' % (eid, rel, mod, st))
            continue
        for rp in reps:
            if not rp.get('name') or not isinstance(rp.get('line'), int) or not (rp.get('axioms') is None or isinstance(rp['axioms'], list)):
                F('R4 %s: %s module %s has a malformed report' % (eid, rel, mod))
        lines = {rp.get('line') for rp in reps}
        if st == 'absent':
            if reps or m.get('prints') is not None:
                F('R4 %s: %s module %s is absent but has reports or prints' % (eid, rel, mod))
            continue
        pl = {n for a, b in (m.get('print_lines') or []) for n in range(a, b + 1)}
        if not isinstance(m.get('prints'), int) or m['prints'] != len(pl) or not lines <= pl:
            F('R4 %s: %s module %s has reports outside its #print axioms lines, or a wrong count' % (eid, rel, mod))
            continue
        want = 'complete' if lines == pl else 'partial' if lines else 'none'
        if st != want:
            F('R4 %s: %s module %s is recorded as %s, its lines give %s' % (eid, rel, mod, st, want))
    mk = exp.get('markers') or {}
    if any(k not in mk or not isinstance(mk[k], int) for k in MARKERS):
        F('R4 %s: %s records no count for every marker' % (eid, rel))


def check_entry_files(e, files, man, F):
    """R8: a CI entry's files agree with each other and with the gap list."""
    eid, rid = e['id'], e.get('run_id')
    gaps = {(g.get('id'), g.get('what')) for g in man.get('missing', [])}
    run = files.get('ci/%s/run.json' % rid)
    res = files.get('ci/%s/results.json' % rid)
    if run is None or res is None:
        F('R8 %s: no run.json or no results.json' % eid)
        return
    try:
        run, res = json.loads(run), json.loads(res)
    except ValueError:
        F('R8 %s: run.json or results.json is not JSON' % eid)
        return
    rr = res.get('run') or {}
    if str(run.get('id')) != rid or run.get('run_id') != rid or rr.get('id') != rid or rr.get('head_sha') != run.get('head_sha') \
            or rr.get('attempt') != run.get('run_attempt'):
        F('R8 %s: results.json names another run, head commit or attempt than run.json' % eid)
    if res.get('kind') != 'bridge':
        F('R8 %s: results.json is of kind %r, and a CI entry\'s expected result is a Mathlib bridge result'
          % (eid, res.get('kind')))
    jobs = files.get('ci/%s/jobs.json' % rid)
    if jobs is None:
        if (eid, 'job list') not in gaps:
            F('R8 %s: no jobs.json, and its absence is not a recorded gap' % eid)
    else:
        try:
            jl = json.loads(jobs)['jobs']
        except (ValueError, KeyError, TypeError):
            F('R8 %s: jobs.json is not a job list' % eid)
            jl = []
        for x in jl:
            if x['head_sha'] != run.get('head_sha'):
                F('R8 %s: job %s head_sha differs from the run' % (eid, x['id']))
        if not any(str(x['id']) == rr.get('job_id') and x['name'] == 'Mathlib bridge' and x['run_attempt'] == run.get('run_attempt')
                   for x in jl):
            F('R8 %s: the results are not from attempt %s\'s Mathlib bridge job' % (eid, run.get('run_attempt')))
    for mod, m in ((res.get('expected') or {}).get('modules') or {}).items():
        want = m.get('status') in ('partial', 'none')
        if ((eid, 'axiom reports of %s' % mod) in gaps) != want:
            F('R8 %s: %s is %s, and its gap record is %s' % (eid, mod, m.get('status'), 'present' if not want else 'absent'))


HEX40 = re.compile(r'[0-9a-f]{40}')
HEX64 = re.compile(r'[0-9a-f]{64}')
JOB_KINDS = ('base-check', 'guard')
EXTRACTOR3 = 'verification/audits/evidence-retention/job_outputs.py'


def expiry_of(created):
    import datetime
    try:
        t = datetime.datetime.strptime(str(created), '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return None
    return (t + datetime.timedelta(days=90)).strftime('%Y-%m-%d')


def check_run_entry(e, files, F):
    """R12: a tranche-3 entry's files agree with each other: run.json, jobs.json and, when a claim rests on what a
    job printed, expected.json."""
    eid, rid = e.get('id'), str(e.get('run_id'))
    if e.get('tranche') != 3 or eid != 'run-' + rid or not re.fullmatch(r'[0-9]{1,20}', rid):
        F('R12 %s: not an entry of tranche 3' % eid)
        return
    run, jobs, exp = (files.get('runs/%s/%s' % (rid, n)) for n in ('run.json', 'jobs.json', 'expected.json'))
    if run is None or jobs is None:
        F('R12 %s: no run.json or no jobs.json' % eid)
        return
    try:
        run, jobs = json.loads(run), json.loads(jobs)
        exp = json.loads(exp) if exp is not None else None
    except ValueError:
        F('R12 %s: run.json, jobs.json or expected.json is not JSON' % eid)
        return
    head = run.get('head_sha')
    if str(run.get('id')) != rid or run.get('run_id') != rid or not HEX40.fullmatch(str(head)):
        F('R12 %s: run.json names another run or no head commit' % eid)
        return
    if e.get('expires') is None or e.get('expires') != expiry_of(run.get('created_at')):
        F('R12 %s: the recorded expiry is not the run\'s creation plus 90 days' % eid)
    jl = jobs.get('jobs') if isinstance(jobs, dict) else None
    if jobs.get('run_id') != rid or not isinstance(jl, list) or not jl:
        F('R12 %s: jobs.json is not the run\'s job list' % eid)
        jl = []
    for j in jl:
        if j.get('head_sha') != head or j.get('run_attempt') != run.get('run_attempt') or not isinstance(j.get('steps'), list):
            F('R12 %s: job %s is at another head commit or attempt than the run, or has no steps' % (eid, j.get('id')))
    if exp is None:
        return
    if exp.get('schema') != 'oi-evidence-job-outputs' or exp.get('version') != 1:
        F('R12 %s: expected.json has an unknown schema or version' % eid)
        return
    er = exp.get('run') or {}
    if er.get('id') != rid or er.get('head_sha') != head or er.get('event') != run.get('event') \
            or er.get('attempt') != run.get('run_attempt'):
        F('R12 %s: expected.json names another run, head commit, event or attempt than run.json' % eid)
    outs = exp.get('outputs')
    if not isinstance(outs, list) or not outs or not (exp.get('reproduce') or {}).get('tool'):
        F('R12 %s: expected.json records no output or no reproduction tool' % eid)
        return
    byid = {str(j.get('id')): j for j in jl}
    for n, o in enumerate(outs):
        if o.get('kind') not in JOB_KINDS or str(o.get('job_id')) not in byid or \
                byid[str(o.get('job_id'))].get('name') != o.get('job_name'):
            F('R12 %s: output %d names no job of jobs.json, or has an unknown kind' % (eid, n))
            continue
        at = o.get('at') or {}
        if run.get('event') == 'pull_request':
            good = at.get('head') == head and all(HEX40.fullmatch(str(at.get(k))) for k in ('base', 'synthetic_merge')) \
                and 'commit' not in at and (o['kind'] != 'base-check' or at.get('ref_as_served') == at.get('synthetic_merge'))
        else:
            good = at.get('commit') == head and 'head' not in at and 'base' not in at and \
                (o['kind'] != 'base-check' or at.get('ref_as_served') == head)
        if not good:
            F('R12 %s: output %d is not at the run\'s commit' % (eid, n))
        rc = o.get('recipe') or {}
        if not isinstance(rc.get('argv'), list) or not rc['argv'] or not all(isinstance(x, str) and x for x in rc['argv']) \
                or not inside(rc.get('cwd') if rc.get('cwd') != '.' else 'x') or not isinstance(rc.get('env'), dict) \
                or not isinstance(rc.get('exit'), int):
            F('R12 %s: output %d has a malformed recipe' % (eid, n))
        src = o.get('source') or {}
        if not HEX64.fullmatch(str(src.get('served_sha256'))) or src.get('extractor') != EXTRACTOR3 or \
                not isinstance(src.get('served_lines'), int) or not isinstance(src.get('original_lines'), int) or \
                not 0 < src['served_lines'] <= src['original_lines']:
            F('R12 %s: output %d has a malformed source' % (eid, n))
        x = o.get('expected') or {}
        if o['kind'] == 'base-check':
            ls = x.get('lines')
            good = isinstance(ls, list) and ls and x.get('summary') == ls[-1] and \
                str(x.get('summary')).startswith('control_plane_base_check: ') and \
                sum(1 for l in ls if str(l).startswith('control_plane_base_check: mode ') and 'REF=<REF>,' in str(l)) == 1
        else:
            cs = x.get('checks')
            good = isinstance(cs, list) and cs and isinstance(x.get('quoted'), list) and \
                str(x.get('verdict')).startswith('edge_rigidity_probe: ') and \
                all(c.get('status') in ('PASS', 'FAIL') and c.get('tag') and HEX64.fullmatch(str(c.get('message_sha256')))
                    for c in cs)
            if good:
                ct = x.get('counts') or {}
                if ct.get('checks') != len(cs) or ct.get('R7') != sum(1 for c in cs if c['tag'].startswith('R7-')) or \
                        ct.get('PASS') != sum(1 for c in cs if c['status'] == 'PASS'):
                    F('R12 %s: the guard counts of output %d disagree with its checks' % (eid, n))
        if not good:
            F('R12 %s: output %d has a malformed expectation' % (eid, n))
    fr = next((f for f in e.get('files', []) if f.get('path') == 'runs/%s/expected.json' % rid), {})
    if len(outs) != 1 or fr.get('source_sha256') != (outs[0].get('source') or {}).get('served_sha256'):
        F('R12 %s: expected.json does not derive from its one output\'s served log' % eid)


SKIP_DIRS = {'.git', '.lake', 'node_modules', '__pycache__'}
SKIP_EXT = ('.pdf', '.tex', '.olean', '.ilean', '.png', '.jpg', '.gz', '.zip', '.bundle')


def citing_lines(root, token, archive):
    """Every (path, line) under root, outside the archive directory, whose text holds token as a whole number."""
    skip = os.path.realpath(archive)
    rx = re.compile(r'(?<![0-9])%s(?![0-9])' % re.escape(token))
    out = []
    for dirpath, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and os.path.realpath(os.path.join(dirpath, d)) != skip]
        for fn in names:
            if fn.endswith(SKIP_EXT):
                continue
            p = os.path.join(dirpath, fn)
            try:
                data = open(p, 'rb').read()
            except OSError:
                continue
            if token.encode('ascii') not in data:
                continue
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            out += [(rel, n) for n, l in enumerate(data.decode('utf-8', 'replace').split('\n'), 1) if rx.search(l)]
    return sorted(out)


def check_research_entry(e, files, man, archive, root, F):
    """R13: an entry retained ahead of its citing record (a research build) is well formed and its files agree:
    run.json, jobs.json and a research-build results.json of the job it names, at the run's head; its citation is
    pending, eligible or cited (research_lifecycle); its run is not attested or already retained; and every item
    its result does not carry
    is a recorded gap: each partial or empty target module's reports, the release gate, the design files' reports,
    the exact-control output, and its off-main source commit."""
    eid, rid = e.get('id'), str(e.get('run_id'))
    if eid != 'research-' + rid or not re.fullmatch(r'[0-9]{1,20}', rid) or e.get('kind') != 'derived':
        F('R13 %s: not a research-build entry' % eid)
        return
    aw = e.get('awaiting_citation')
    shaped = True
    if e.get('citations'):
        if aw is not None:
            F('R13 %s: carries citations and a pending citation together' % eid)
            shaped = False
    elif not isinstance(aw, dict) or not isinstance(aw.get('pull_request'), int) or not inside(aw.get('record')) \
            or not str(aw.get('record')).endswith('.md') or not isinstance(aw.get('round'), str) or not aw['round'] \
            or not isinstance(aw.get('line'), int) or not HEX40.fullmatch(str(aw.get('head'))):
        F('R13 %s: records no pending citation naming its record, round, pull request, line and head' % eid)
        shaped = False
    run, jobs, res = (files.get('ci/%s/%s' % (rid, n)) for n in ('run.json', 'jobs.json', 'results.json'))
    if run is None or jobs is None or res is None:
        F('R13 %s: no run.json, jobs.json or results.json' % eid)
        return
    try:
        run, jobs, res = json.loads(run), json.loads(jobs), json.loads(res)
    except ValueError:
        F('R13 %s: run.json, jobs.json or results.json is not JSON' % eid)
        return
    head, rr = run.get('head_sha'), res.get('run') or {}
    if str(run.get('id')) != rid or run.get('run_id') != rid or not HEX40.fullmatch(str(head)) or rr.get('id') != rid \
            or rr.get('head_sha') != head or rr.get('attempt') != run.get('run_attempt'):
        F('R13 %s: results.json names another run, head commit or attempt than run.json' % eid)
    if res.get('kind') != 'research-build':
        F('R13 %s: results.json is of kind %r, not a research-build result' % (eid, res.get('kind')))
    jl = jobs.get('jobs') if isinstance(jobs, dict) else None
    if not isinstance(jl, list) or not any(str(j.get('id')) == rr.get('job_id') and j.get('name') == rr.get('job_name')
                                           and j.get('run_attempt') == run.get('run_attempt') and j.get('head_sha') == head
                                           for j in jl):
        F('R13 %s: the results are not from a job of jobs.json at the run\'s head and attempt' % eid)
    fr = next((f for f in e.get('files', []) if f.get('path') == 'ci/%s/results.json' % rid), {})
    if fr.get('source_sha256') != (res.get('source') or {}).get('served_sha256'):
        F('R13 %s: results.json does not derive from its served log' % eid)
    gaps = {g.get('what') for g in man.get('missing', []) if g.get('id') == eid}
    # the off-main source commit is retained under objects/ (check_objects.py verifies it) or is a recorded gap
    try:
        objs = json.load(open(os.path.join(archive, 'objects', 'manifest.json'), encoding='utf-8')).get('objects', [])
    except (OSError, ValueError):
        objs = []
    held = any(o.get('oid') == head and o.get('type') == 'commit' and o.get('file') for o in objs)
    if held == ('source commit %s' % head in gaps):
        F('R13 %s: its source commit %s is %s' % (eid, str(head)[:12], 'retained and also a recorded gap' if held
                                                  else 'neither retained under objects/ nor a recorded gap'))
    want = {'release gate', 'exact-control replay output'}
    want |= {'axiom reports of %s' % m for m, x in ((res.get('expected') or {}).get('modules') or {}).items()
             if isinstance(x, dict) and x.get('status') in ('partial', 'none')}
    if not want <= gaps or not any(str(g).startswith('axiom reports of the research design') for g in gaps):
        F('R13 %s: an item its result does not carry is not a recorded gap: %s' % (eid, sorted(want - gaps)[:3] or
                                                                                   ['axiom reports of the research design']))
    attested = {str(x.get('run_id')) for x in man['entries'] if str(x.get('id', '')).startswith(('ci-', 'run-'))}
    attested |= {str((x.get('provenance') or {}).get('run_id')) for x in man['entries'] if (x.get('provenance') or {}).get('run_id')}
    if rid in attested:
        F('R13 %s: run %s already has another entry' % (eid, rid))
    research_lifecycle(e, eid, rid, head if HEX40.fullmatch(str(head)) else None, aw, shaped, archive, root, F)


def research_lifecycle(e, eid, rid, head, aw, shaped, archive, root, F):
    """R13's citation states (pending, eligible, cited); records the state in R13_STATES, or a failure. head is
    run.json's head_sha, or None when the run's metadata names none (a failure already reported), and then no state
    is judged."""
    cl = citing_lines(root, rid, archive)
    if 'verbatim_mentions' in e:
        cl = verbatim_filter(e, eid, rid, head, aw, root, cl, F)
        if cl is None:
            return
    rules = objects_rules()
    if e.get('citations'):
        # cited: no line mapped twice; nothing outside the mapped files names the run; in them, every free-standing
        # citation of the run is mapped, every mapped line is one, and every line naming the run obeys the citation
        # rule (check_objects.run_citations)
        listed = [(c.get('path'), c.get('line')) for c in e['citations']]
        twice = sorted({x for x in listed if listed.count(x) > 1}, key=str)
        if twice:
            F('R13 %s: its citations map %s:%s twice' % (eid, twice[0][0], twice[0][1]))
            return
        mapped = set(listed)
        paths = {p for p, _ in mapped}
        for path, line in cl:
            if path not in paths:
                F('R13 %s: run %s is now cited at %s:%d, and the entry does not map that citation' % (eid, rid, path, line))
                return
        if head is None or not shaped:
            return
        for p in sorted(paths, key=str):
            try:
                L = open(os.path.join(root, str(p)), encoding='utf-8').read().split('\n') if inside(p) else None
            except (OSError, UnicodeDecodeError):
                L = None
            lns = sorted(ln for q, ln in mapped if q == p)
            if L is None or not all(isinstance(ln, int) and 0 < ln <= len(L) for ln in lns):
                return                                  # R3 reports the missing file or line
            free, emb, why = rules.run_citations(head, rid, L)
            for n in free:
                if (p, n) not in mapped:
                    F('R13 %s: run %s is now cited at %s:%d, and the entry does not map that citation' % (eid, rid, p, n))
                    return
            for ln in lns:
                if ln not in free:
                    F('R13 %s: its citation at %s:%d names run %s %s, which is not a citation of it' % (
                        eid, p, ln, rid, 'only inside an identifier' if ln in emb else 'nowhere'))
                    return
            if why:
                F('R13 %s: its citation at %s %s' % (eid, p, why.replace('head', 'run head')))
                return
        R13_STATES[eid] = ('cited', sorted(mapped))
        return
    if not shaped:
        return
    rec = aw['record']
    # pending: no line outside the record may cite the run
    for path, line in cl:
        if path != rec:
            F('R13 %s: run %s is now cited at %s:%d, and the entry does not map that citation' % (eid, rid, path, line))
            return
    if not os.path.isfile(os.path.join(root, rec)):
        if head is not None:
            R13_STATES[eid] = ('pending', None)
        return
    if head is None:
        return
    lines = [n for _, n in cl]
    if not lines:
        F('R13 %s: its record %s is in the tree and does not cite run %s' % (eid, rec, rid))
        return
    if aw['line'] not in lines:
        F('R13 %s: its record %s cites run %s on line(s) %s, not on the recorded line %d' % (eid, rec, rid, lines,
                                                                                            aw['line']))
        return
    try:
        L = open(os.path.join(root, rec), encoding='utf-8').read().split('\n')
    except (OSError, UnicodeDecodeError):
        F('R13 %s: its record %s is in the tree and cannot be read' % (eid, rec))
        return
    # the citation rule (check_objects.run_citations) on every line of the record that names the run; the recorded
    # line must be a free-standing citation of it
    free, emb, why = rules.run_citations(head, rid, L)
    if aw['line'] not in free:
        F('R13 %s: its record %s names run %s on the recorded line %d only inside an identifier, which is not a '
          'citation' % (eid, rec, rid, aw['line']))
        return
    if why:
        F('R13 %s: its record %s %s' % (eid, rec, why.replace('head', 'run head')))
        return
    R13_STATES[eid] = ('eligible', free)


def verbatim_filter(e, eid, rid, head, aw, root, cl, F):
    """R13's verbatim mentions: cl, the lines naming the run, less the one line an owner-approved tuple admits, or
    None after recording a failure. Fails closed on anything but the exact tuple: the entry, run and head; the
    mention's form, path, line, blob and source; the citation context; the copy present, hashed here from its
    bytes, naming the run exactly once on the approved line and on no other. Admits no citation."""
    allowed = [a for a in verbatim_allowlist() if a['entry'] == eid]
    if len(allowed) != 1:
        return None                                    # reported by check(): an entry outside the allowlist
    a = allowed[0]
    if a['run'] != rid:
        F('R13 %s: verbatim mention names run %s, not the approved run %s' % (eid, rid, a['run']))
        return None
    vm = e.get('verbatim_mentions')
    v = vm[0] if isinstance(vm, list) and len(vm) == 1 and isinstance(vm[0], dict) else None
    if v is None or set(v) != VERBATIM_KEYS or not isinstance(v.get('copy_of'), dict) or \
            set(v['copy_of']) != {'commit', 'path'} or not isinstance(v.get('note'), str) or not v['note'].strip() \
            or type(v.get('line')) is not int:
        F('R13 %s: verbatim_mentions is malformed (exactly one mention: path, an integer line, blob, sha256, copy_of '
          '{commit, path} and a note, and nothing else)' % eid)
        return None
    if (v['path'], v['line'], v['blob'], v['sha256'], v['copy_of']) != \
            (a['path'], a['line'], a['blob'], a['sha256'], a['copy_of']):
        F('R13 %s: verbatim mention %s:%s is not the owner-approved tuple' % (eid, v['path'], v['line']))
        return None
    if head != a['head']:
        F('R13 %s: verbatim mention: run %s has head %s, not the approved head %s' % (eid, rid, head, a['head']))
        return None
    if e.get('citations'):
        ctx = sorted({(c.get('path'), c.get('line')) for c in e['citations']}, key=str)
        if any(p == a['path'] for p, _ in ctx):
            F('R13 %s: a verbatim mention is not a citation, and the entry maps %s' % (eid, a['path']))
            return None
        if ctx != [(a['awaiting']['record'], n) for n in a['cited_lines']]:
            F('R13 %s: verbatim mention: the entry\'s citations are not the approved citation context' % eid)
            return None
    elif not isinstance(aw, dict) or tuple(aw.get(k) for k in AWAITING_KEYS) != \
            tuple(a['awaiting'][k] for k in AWAITING_KEYS):
        F('R13 %s: verbatim mention: the pending citation is not the approved citation context' % eid)
        return None
    p = os.path.join(root, a['path'])
    if not inside(a['path']) or not os.path.isfile(p):
        F('R13 %s: verbatim mention %s is absent' % (eid, a['path']))
        return None
    # a regular file at exactly that path: no component of the path is a symbolic link, and it resolves to itself
    parts = a['path'].split('/')
    if any(os.path.islink(os.path.join(root, *parts[:n])) for n in range(1, len(parts) + 1)) or \
            os.path.realpath(p) != os.path.join(os.path.realpath(root), *parts):
        F('R13 %s: verbatim mention %s is reached through a symbolic link' % (eid, a['path']))
        return None
    idx = git_index_entry(root, a['path'])
    if idx is not None and idx != ('100644', a['blob']):
        F('R13 %s: verbatim mention %s: the git index holds %s, not a regular file (100644) at the approved blob %s'
          % (eid, a['path'], ' '.join(idx) if idx else 'nothing at that path', a['blob']))
        return None
    data = open(p, 'rb').read()
    # two digests of the complete bytes, computed here, each against the approved value on its own
    got = blob_id(data)
    if got != a['blob']:
        F('R13 %s: verbatim mention %s is not the approved blob (%s, approved %s)' % (eid, a['path'], got, a['blob']))
        return None
    got256 = hashlib.sha256(data).hexdigest()
    if got256 != a['sha256']:
        F('R13 %s: verbatim mention %s is not the approved sha256 (%s, approved %s)' % (eid, a['path'], got256,
                                                                                       a['sha256']))
        return None
    rx = re.compile(r'(?<![0-9])%s(?![0-9])' % re.escape(rid))
    L = data.decode('utf-8', 'replace').split('\n')
    if not (0 < a['line'] <= len(L)) or len(rx.findall(L[a['line'] - 1])) != 1:
        F('R13 %s: line %d of %s does not name run %s exactly once' % (eid, a['line'], a['path'], rid))
        return None
    other = [n for n, l in enumerate(L, 1) if n != a['line'] and rx.search(l)]
    if other:
        F('R13 %s: verbatim mention %s names run %s on another line (%s)' % (eid, a['path'], rid,
                                                                            ','.join(map(str, other))))
        return None
    VERBATIM_STATES[eid] = (a['path'], a['line'])
    return [x for x in cl if x != (a['path'], a['line'])]


def r13_summary():
    """The printed count of R13's states: an eligible entry is counted apart, never as cited."""
    n = lambda s: sum(1 for v in R13_STATES.values() if v[0] == s)
    return 'citations (R13): %d cited, %d pending (record not in the tree), %d eligible for promotion (not cited)' % (
        n('cited'), n('pending'), n('eligible'))


def print_r13_states():
    """The research-build entries' citation states; an eligible entry is listed apart and counts as not cited."""
    if not R13_STATES:
        return
    print(r13_summary())
    for eid, (s, lines) in sorted(R13_STATES.items()):
        if s != 'cited':
            print('  %-9s %s%s' % (s, eid, '  at line(s) %s' % ','.join(map(str, lines)) if lines else ''))
    for eid, (path, line) in sorted(VERBATIM_STATES.items()):
        print('  verbatim  %s  %s:%d (approved provenance metadata, not a citation)' % (eid, path, line))


def check_tranche3(man, read_tree, F):
    """R12: the tranche-3 section: the runs retained here are not attested runs (those are tranche 1's), and every
    uncovered run is either retained here or listed as remaining, earliest log expiry first."""
    t3 = [e for e in man.get('entries', []) if str(e.get('id', '')).startswith('run-')]
    sec = man.get('tranche3')
    if not t3 and sec is None:
        return
    if not isinstance(sec, dict) or not HEX40.fullmatch(str(sec.get('base'))) or not isinstance(sec.get('remaining'), list):
        F('R12 tranche3 section missing or malformed')
        return
    attested = {str(e.get('run_id')) for e in man['entries'] if str(e.get('id', '')).startswith('ci-')}
    attested |= {str((e.get('provenance') or {}).get('run_id')) for e in man['entries'] if (e.get('provenance') or {}).get('run_id')}
    for c in man.get('coverage', {}).get('files', []):
        data = read_tree(c.get('path', ''))
        try:
            doc = json.loads(data) if data is not None else {}
        except ValueError:
            doc = {}
        for a in doc.get('attestations', []) if isinstance(doc, dict) else []:
            m = a.get('kind') == 'check-run' and RUN_URL.search(str(a.get('record', '')))
            if m:
                attested.add(m.group(1))
        for v in (doc.get('ci') or {}).values() if isinstance(doc, dict) else []:
            if isinstance(v, dict) and v.get('run'):
                attested.add(str(v['run']))
    held = set()
    for e in t3:
        if str(e.get('run_id')) in attested:
            F('R12 %s: run %s is attested or already retained, so it is not tranche 3\'s' % (e.get('id'), e.get('run_id')))
        held.add(str(e.get('run_id')))
    seen, prev = set(), None
    for r in sec['remaining']:
        rid = str(r.get('run_id'))
        if not re.fullmatch(r'[0-9]{1,20}', rid) or rid in seen or r.get('expires') != expiry_of(r.get('created_at')):
            F('R12 tranche3: remaining run %s is malformed or repeated' % rid)
        seen.add(rid)
        if rid in held or rid in attested:
            F('R12 tranche3: remaining run %s has an entry' % rid)
        key = (str(r.get('created_at')), rid)
        if prev is not None and key < prev:
            F('R12 tranche3: the remaining runs are not in order of creation')
        prev = key
    if t3 and sec['remaining']:
        if max(str(e.get('expires')) for e in t3) > min(str(r.get('expires')) for r in sec['remaining']):
            F('R12 tranche3: a retained run expires after a remaining one')
    if sec.get('retained') != len(t3) or sec.get('uncovered') != len(t3) + len(sec['remaining']) or \
            sec.get('cited_runs') != sec.get('covered_before', -1) + sec.get('uncovered', -1):
        F('R12 tranche3: the counts disagree')


def check_coverage(man, archive, root, read_tree, F, scope=None):
    cov = man.get('coverage', {}).get('files', [])
    if not cov:
        F('R9 the manifest names no coverage files')
    by_run = {e.get('run_id'): e for e in man['entries'] if e.get('run_id')}
    listed = {c['path'] for c in cov}
    for p in sorted({c.get('path', '') for e in man['entries'] for c in e.get('citations', [])}):
        if p.startswith(('verification/receipts/', 'verification/certificates/attestations/')) and p not in listed:
            F('R9 cited file %s is not in the coverage list' % p)
    # the files to cover, recomputed from the tree: every receipt, and every certificate attestation citing runs
    later = {c.get('path') for c in man.get('coverage', {}).get('later', [])}
    cited = {c.get('path', '') for e in man['entries'] for c in e.get('citations', [])}
    for c in man.get('coverage', {}).get('later', []):
        if c.get('path') in listed:
            F('R9 %s is named both as covered and as later' % c.get('path'))
        if c.get('path') in cited:
            F('R9 %s is named as later, but the tranche cites it' % c.get('path'))
        if not c.get('evidence'):
            F('R9 %s is named as later without where its evidence is retained' % c.get('path'))
    in_tree = []
    rdir = os.path.join(root, 'verification', 'receipts')
    adir = os.path.join(root, 'verification', 'certificates', 'attestations')
    if os.path.isdir(rdir):
        in_tree += ['verification/receipts/' + f for f in sorted(os.listdir(rdir)) if f.endswith('.json')]
    if os.path.isdir(adir):
        for f in sorted(os.listdir(adir)):
            if f.endswith('.json'):
                d = json.load(open(os.path.join(adir, f), encoding='utf-8'))
                if any(isinstance(v, dict) and v.get('run') for v in (d.get('ci') or {}).values()):
                    in_tree.append('verification/certificates/attestations/' + f)
    if scope is None:
        for p in in_tree:
            if p not in listed and p not in later:
                F('R9 %s is in the tree but neither covered nor named as later than this tranche' % p)
    else:
        for p in sorted(scope):
            if p not in listed:
                F('R10 %s existed at the tranche base but is not covered' % p)
        for p in sorted(listed):
            if p not in scope:
                F('R10 covered file %s did not exist at the tranche base' % p)

    def run_of(rid):
        p = os.path.join(archive, 'ci', str(rid), 'run.json')
        if rid not in by_run or 'ci/%s/run.json' % rid not in {f['path'] for f in by_run[rid]['files']} or \
                not os.path.isfile(p):
            return None
        try:
            return json.load(open(p, encoding='utf-8'))
        except ValueError:
            return None

    for c in cov:
        data = read_tree(c['path'])
        if data is None or blob_id(data) != c['blob']:
            F('R9 coverage file %s missing or changed' % c['path'])
            continue
        doc = json.loads(data)
        if c['path'].startswith('verification/receipts/'):
            for a in doc.get('attestations', []):
                if a.get('kind') != 'check-run':
                    continue
                m = RUN_URL.search(a['record'])
                rid = m and m.group(1)
                run = run_of(rid) if m else None
                if run is None:
                    F('R9 %s %s: check run %s has no entry' % (doc.get('round'), a.get('subject'), rid))
                elif run.get('head_sha') != a['commit'] or (m.group(2) and int(m.group(2)) != run.get('run_attempt')):
                    F('R9 %s %s: run %s is at %s attempt %s; attested %s attempt %s' % (
                        doc.get('round'), a['subject'], rid, str(run.get('head_sha'))[:12], run.get('run_attempt'),
                        a['commit'][:12], m.group(2)))
                elif not any(r.get('round') == doc.get('round') and r.get('subject') == a['subject']
                             and r.get('commit') == a['commit'] for r in by_run[rid].get('roles', [])):
                    F('R9 %s %s: the entry for run %s does not record this role' % (doc.get('round'), a['subject'], rid))
        else:
            for role, v in doc.get('ci', {}).items():
                run = run_of(v['run'])
                if run is None or run.get('head_sha') != v['head_sha'] or run.get('conclusion') != v['conclusion']:
                    F('R9 %s %s: run %s has no matching entry' % (doc.get('round'), role, v['run']))


def later_provenance(man, root, later=None, head='HEAD'):
    """R10, which reads git history: no path named as later existed at the tranche base."""
    import subprocess
    base, fails = man.get('base', ''), []
    git = lambda *a: subprocess.run(['git', '-C', root] + list(a), capture_output=True).returncode
    if git('cat-file', '-e', base + '^{commit}') != 0:
        return ['R10 the tranche base %s is not in the repository' % base[:12]]
    if git('merge-base', '--is-ancestor', base, head) != 0:
        fails.append('R10 the tranche base %s is not an ancestor of %s' % (base[:12], head))
    for c in (man.get('coverage', {}).get('later', []) if later is None else later):
        if git('cat-file', '-e', '%s:%s' % (base, c.get('path'))) == 0:
            fails.append('R10 %s existed at the tranche base %s, so it is not later' % (c.get('path'), base[:12]))
    return fails


def base_scope(man, root):
    """R10's scope for R9: the receipts, and the certificate attestations citing runs, at the tranche base."""
    import subprocess
    base = man.get('base', '')
    git = lambda *a: subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    if git('cat-file', '-e', base + '^{commit}').returncode != 0:
        return None, ['R10 the tranche base %s is not in the repository' % base[:12]]
    scope = set()
    names = git('ls-tree', '-r', '--name-only', base, '--', 'verification/receipts',
                'verification/certificates/attestations').stdout.decode('utf-8').split('\n')
    for p in names:
        if p.startswith('verification/receipts/') and p.endswith('.json'):
            scope.add(p)
        elif p.startswith('verification/certificates/attestations/') and p.endswith('.json'):
            d = json.loads(git('show', '%s:%s' % (base, p)).stdout)
            if any(isinstance(v, dict) and v.get('run') for v in (d.get('ci') or {}).values()):
                scope.add(p)
    return scope, []


LEAN_ROOT = 'verification/lean-mathlib/'


def git_show(root):
    """show(rev, path): the bytes of the blob at path in rev, read from root's history, or None."""
    import subprocess

    def show(rev, path):
        p = subprocess.run(['git', '-C', root, 'cat-file', 'blob', '%s:%s' % (rev, path)], capture_output=True)
        return p.stdout if p.returncode == 0 else None
    return show


def governed_entries(texts):
    """The (class, ops, path) lines of the one v3-governed-paths block across a control plane's files, or None if
    there is not exactly one closed block or a line is not a class and two fields. The opener and the closer are
    recognized as G10 states them (exact lines), and the entries are split as S7 states them (fields separated by
    one space). S7's validity rules (the ops letters and their order, the path rules, a path given twice) and
    G10's near-miss rule are not applied, and the block is counted across all the files rather than required to
    lie in the preregistration (K2): the digest ties the entries to the receipt, whose block the V3 verifier
    validated. Its structure is close to tools/v3_verifier.py's parser, so it is not an independent
    implementation of the specification."""
    blocks = []
    for t in texts:
        lines = t.split('\n')
        i = 0
        while i < len(lines):
            if lines[i] == '```v3-governed-paths':
                if '```' not in lines[i + 1:]:
                    return None
                j = lines.index('```', i + 1)
                blocks.append(lines[i + 1:j])
                i = j + 1
            else:
                i += 1
    if len(blocks) != 1:
        return None
    out = []
    for ln in blocks[0]:
        if ln.strip() == '' or ln.startswith('#'):
            continue
        parts = ln.split(' ', 2)
        if len(parts) != 3 or parts[0] not in ('execution', 'record') or not parts[1] or not parts[2]:
            return None
        out.append(tuple(parts))
    return out


def governed_digest(entries):
    """S7's digest of a governed-path set: SHA-256 of the canonical bytes, the entries in ascending order of the
    UTF-8 bytes of their path, every field followed by one NUL byte."""
    out = b'v3-governed-paths\0v1\0'
    for e in sorted(entries, key=lambda e: e[2].encode('utf-8')):
        out += b''.join(f.encode('utf-8') + b'\0' for f in e)
    return hashlib.sha256(out).hexdigest()


def governed_modules(kind, doc, commit, show, F, eid):
    """The Lean modules a round governs, read at commit; None once F has recorded why they cannot be read there."""
    rnd, at = doc.get('round'), str(commit)[:12]
    if kind == 'receipt':
        texts = []
        for b in doc.get('control_plane_blobs') or []:
            data = show(commit, str(b.get('path')))
            if data is None or blob_id(data) != b.get('blob'):
                F('R11 %s: control-plane file %s of %s is not at its receipt\'s blob at %s' % (eid, b.get('path'), rnd, at))
                return None
            texts.append(data.decode('utf-8', 'replace'))
        entries = governed_entries(texts)
        if entries is None:
            F('R11 %s: the control plane of %s at %s carries no single well-formed v3-governed-paths block' % (eid, rnd, at))
            return None
        if governed_digest(entries) != doc.get('governed_paths_digest'):
            F('R11 %s: the governed paths of %s at %s do not hash to its receipt\'s governed_paths_digest' % (eid, rnd, at))
            return None
        paths = [p for _, _, p in entries]
    else:
        cpath = 'verification/certificates/%s.json' % rnd
        data, cert = show(commit, cpath), None
        if data is not None and blob_id(data) == doc.get('certificate'):
            try:
                cert = json.loads(data)
            except ValueError:
                cert = None
        if not isinstance(cert, dict) or not isinstance(cert.get('contributions'), list):
            F('R11 %s: %s at %s is not the certificate its attestation pins' % (eid, cpath, at))
            return None
        paths = [str(c.get('path', '')) for c in cert['contributions'] if isinstance(c, dict)]
    dirs = [p for p in paths if p.endswith('/') and (p.startswith(LEAN_ROOT) or LEAN_ROOT.startswith(p))]
    if dirs:
        F('R11 %s: the governed paths of %s at %s name the directory %s, so they fix no module set' % (eid, rnd, at, dirs[0]))
        return None
    return {p[len(LEAN_ROOT):] for p in paths if p.startswith(LEAN_ROOT) and p.endswith('.lean')}


def git_on_main(root, base):
    """on_main(commit): True if commit is an ancestor of base, False if it is not, None if this repository cannot
    place it. A repository that is not shallow holds every ancestor of base, so a commit it lacks is not one; in a
    shallow repository only an ancestor is decided."""
    import subprocess
    git = lambda *a: subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    shallow = git('rev-parse', '--is-shallow-repository').stdout.strip() != b'false'

    def on_main(commit):
        if not re.fullmatch(r'[0-9a-f]{40}', str(commit)):
            return None
        if git('merge-base', '--is-ancestor', commit, base).returncode == 0:
            return True
        return None if shallow else False
    return on_main


def module_sets(archive, root, man, show=None, on_main=None, scope=None):
    """R11, which reads git history: every expected result's module table is the set of Lean modules its run's
    rounds govern, re-derived from each round's control plane at that run's commit, and the runs checked are the
    runs the receipts and certificate attestations at the tranche base attest. scope is base_scope's set, read
    here when not given. Returns (failures, stats)."""
    show = show or git_show(root)
    fails = []
    F = fails.append
    base = man.get('base', '')
    on_main = on_main or git_on_main(root, base)
    stats = {'checked': 0, 'runs': 0, 'modules': 0, 'reads': 0, 'unscoped': []}
    if scope is None:
        scope = base_scope(man, root)[0]
    if scope is None:
        F('R11 the tranche base %s is not in the repository, so no attestation can be read there' % base[:12])
        return fails, stats
    # the runs to check, from the attestations at the base alone: no result's kind or entry enters here
    attest = {}
    for p in sorted(scope):
        raw = show(base, str(p))
        try:
            doc = json.loads(raw) if raw is not None else None
        except ValueError:
            doc = None
        if not isinstance(doc, dict):
            F('R11 %s cannot be read at the tranche base %s' % (p, base[:12]))
            continue
        if str(p).startswith('verification/receipts/'):
            for a in doc.get('attestations') or []:
                m = isinstance(a, dict) and a.get('kind') == 'check-run' and RUN_URL.search(str(a.get('record', '')))
                if m:
                    attest.setdefault(m.group(1), []).append(('receipt', doc, a.get('commit')))
        else:
            for v in (doc.get('ci') or {}).values():
                if isinstance(v, dict) and v.get('run'):
                    attest.setdefault(str(v['run']), []).append(('certificate', doc, v.get('head_sha')))
    cache, done = {}, set()
    none_at_base = 'is attested by no receipt or certificate attestation at the tranche base'
    for e in man.get('entries', []):
        eid = e.get('id')
        is_ci = str(eid).startswith('ci-')
        for f in e.get('files', []):
            rel = str(f.get('path', ''))
            if not (rel.endswith('/results.json') or (rel.startswith('bg3/results-') and rel.endswith('.json'))):
                continue
            try:
                r = json.load(open(os.path.join(archive, rel), encoding='utf-8'))
                kind = r.get('kind')
                rid, head = str(r['run']['id']), r['run']['head_sha']
                if kind == 'bridge':
                    table = r['expected']['modules']
                    if not isinstance(table, dict):
                        raise TypeError('module table')
            except (OSError, ValueError, KeyError, TypeError, AttributeError):
                F('R11 %s: %s is not a readable expected result' % (eid, rel))
                continue
            if kind != 'bridge':
                if is_ci:
                    F('R11 %s: %s is of kind %r, not a Mathlib bridge result, so no module table of it is checked'
                      % (eid, rel, kind))
                elif rid in attest:
                    F('R11 %s: %s is of kind %r, but an attestation at the tranche base names its run %s, so it must be '
                      'a bridge result whose module table is checked' % (eid, rel, kind, rid))
                elif kind == 'research-build':
                    stats['unscoped'].append((rel, 'of kind %r, whose module table is the build targets its workflow names, '
                                              'not a round\'s governed paths, and run %s %s' % (kind, rid, none_at_base)))
                else:
                    stats['unscoped'].append((rel, 'of kind %r, which records no module table, and run %s %s'
                                              % (kind, rid, none_at_base)))
                continue
            if rid not in attest:
                if is_ci:
                    F('R11 %s: run %s %s, so no round governs its modules' % (eid, rid, none_at_base))
                    continue
                where = on_main(head)
                if where is True:
                    F('R11 %s: run %s %s, but its commit %s is on main there' % (eid, rid, none_at_base, str(head)[:12]))
                elif where is None:
                    F('R11 %s: run %s %s, and this repository cannot decide whether its commit %s is on main '
                      '(a shallow clone)' % (eid, rid, none_at_base, str(head)[:12]))
                else:
                    stats['unscoped'].append((rel, 'run %s %s, and its commit %s is not on main there'
                                              % (rid, none_at_base, str(head)[:12])))
                continue
            derived, whole = set(), True
            for kind, doc, commit in attest[rid]:
                if commit != head:
                    F('R11 %s: %s %s attests run %s at %s; the expected result holds at %s' % (
                        eid, kind, doc.get('round'), rid, str(commit)[:12], str(head)[:12]))
                    whole = False
                    continue
                key = (kind, doc.get('round'), commit)
                if key not in cache:
                    cache[key] = governed_modules(kind, doc, commit, show, F, eid)
                    stats['reads'] += 1
                if cache[key] is None:
                    whole = False
                else:
                    derived |= cache[key]
            if not whole:
                continue
            if derived != set(table):
                F('R11 %s: the module table of %s differs from the Lean modules its run\'s rounds govern at %s: '
                  'missing %s, extra %s' % (eid, rel, head[:12], sorted(derived - set(table)), sorted(set(table) - derived)))
            stats['checked'] += 1
            stats['modules'] += len(table)
            done.add(rid)
    stats['runs'] = len(done)
    if done != set(attest):
        F('R11 the runs with a checked expected result are not the runs attested at the tranche base: %d attested, '
          '%d checked; unchecked %s, unattested %s' % (len(attest), len(done), sorted(set(attest) - done),
                                                       sorted(done - set(attest))))
    if not stats['checked']:
        F('R11 no expected result was checked against its rounds\' governed paths')
    return fails, stats


def print_unscoped(st):
    for rel, why in (st or {}).get('unscoped', []):
        print('UNSCOPED  %s: %s; R11 does not apply' % (rel, why))


def module_report(archive, root):
    """--module-sets: R11 alone, with what it checked and what lies outside its scope."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    fails, st = module_sets(archive, root, man)
    print_unscoped(st)
    for f in fails:
        print('FAIL  %s' % f)
    print('MODULE-SETS  %s (%d expected result(s) of %d attested run(s), %d module record(s), %d round control plane(s) '
          'read at their run\'s commit; %d outside its scope; %d failure(s))' % (
              'HOLDS' if not fails else 'FAILS', st['checked'], st['runs'], st['modules'], st['reads'], len(st['unscoped']),
              len(fails)))
    return 0 if not fails else 1


def history_mode(archive, root, man, tree=None):
    """The check in history mode, R1-R11: R1-R9 against the tree at tree (root by default), with R9's scope read
    from root's history, and R10 and R11 against that history. Returns (failures, R11's stats or None)."""
    scope, fails = base_scope(man, root)
    if scope is None:
        return fails, None
    f11, st = module_sets(archive, root, man, scope=scope)
    return fails + check(archive, tree or root, scope)[0] + later_provenance(man, root) + f11, st


def objects_gate(archive, root):
    """The retained off-main objects, when the archive holds them: check_objects.py in history mode, then its
    self-test. Returns (ran, ok)."""
    if not os.path.isdir(os.path.join(archive, 'objects')):
        return False, True
    tool = os.path.join(archive, 'check_objects.py')
    ok = True
    for args in (['--reconstitute'], ['--self-test']):
        p = subprocess.run([sys.executable, '-I', tool] + args, cwd=root, capture_output=True, text=True)
        print(p.stdout.rstrip())
        if p.returncode:
            print(p.stderr.rstrip()[-2000:])
            ok = False
    return True, ok


def job_outputs_gate(archive, root):
    """Tranche 3's comparator, when the archive holds it: job_outputs.py --self-test. Returns (ran, ok)."""
    tool = os.path.join(archive, 'job_outputs.py')
    if not os.path.isfile(tool):
        return False, True
    p = subprocess.run([sys.executable, '-I', '-B', tool, '--self-test'], cwd=root, capture_output=True, text=True)
    print(p.stdout.rstrip())
    if p.returncode:
        print(p.stderr.rstrip()[-2000:])
    return True, p.returncode == 0


def gate(archive, root):
    """The release-gate step: the check in history mode (R1-R13), then the self-test, then the retained objects'
    check and self-test, then tranche 3's comparator self-test. It fails at once if the self-test's verbatim
    substitute is set before it starts, and fails if the self-test leaves it set."""
    leak = verbatim_seam_leak()
    if leak:
        print('FAIL  %s' % leak)
        print('EVIDENCE-RETENTION  FAILS (%s)' % leak)
        return 1
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    fails, st11 = history_mode(archive, root, man)
    leak = verbatim_seam_leak()
    if leak:
        print('FAIL  %s' % leak)
        print('EVIDENCE-RETENTION  FAILS (%s)' % leak)
        return 1
    print_unscoped(st11)
    print_r13_states()
    for f in fails:
        print('FAIL  %s' % f)
    st = self_test(archive, root)
    leak = verbatim_seam_leak()
    if leak:
        fails.append(leak)
        print('FAIL  %s' % leak)
    ran, obj_ok = objects_gate(archive, root)
    jran, job_ok = job_outputs_gate(archive, root)
    good = not fails and st == 0 and obj_ok and job_ok
    print('EVIDENCE-RETENTION  %s (history mode: %d failure(s); self-test %s%s%s)' % (
        'HOLDS' if good else 'FAILS', len(fails), 'OK' if st == 0 else 'FAILED',
        ('; retained objects %s' % ('OK' if obj_ok else 'FAILED')) if ran else '',
        ('; job-output comparator %s' % ('OK' if job_ok else 'FAILED')) if jran else ''))
    return 0 if good else 1


def report(archive, root):
    leak = verbatim_seam_leak()
    if leak:
        print('FAIL  %s' % leak)
        print('RETENTION  FAILS (%s)' % leak)
        return 1
    fails, gaps = check(archive, root)
    leak = verbatim_seam_leak()
    if leak:
        print('FAIL  %s' % leak)
        print('RETENTION  FAILS (%s)' % leak)
        return 1
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    nfiles = sum(len(e.get('files', [])) for e in man['entries'])
    cites = [(e['id'], c) for e in man['entries'] for c in e.get('citations', [])]
    st = {}
    for _, c in cites:
        for k in c.get('claims', []):
            st[k.get('status')] = st.get(k.get('status'), 0) + 1
    print('RETENTION  %d entries, %d archived files, %d citing locations, %d claims (%s)' % (
        len(man['entries']), nfiles, len(cites), sum(st.values()),
        ', '.join('%d %s' % (v, k) for k, v in sorted(st.items()))))
    for g in gaps:
        print('GAP  %s' % json.dumps(g, sort_keys=True))
    for eid, c in cites:
        for k in c.get('claims', []):
            if k.get('status') in ('not retained', 'differs'):
                print('%s  %s  %s:%d  %r%s' % ('DIFFERS' if k['status'] == 'differs' else 'NOT RETAINED', eid, c['path'],
                                              k['line'], k['text'], ': ' + k['note'] if k.get('note') else ''))
    for c in man.get('coverage', {}).get('later', []):
        print('LATER  %s: %s (declared; --later-provenance checks it against git history)' % (c.get('path'), c.get('evidence')))
    print_r13_states()
    for f in fails:
        print('FAIL  %s' % f)
    print('RETENTION  %s (%d failure(s), %d gap(s))' % ('HOLDS' if not fails else 'FAILS', len(fails), len(gaps)))
    return 0 if not fails else 1


def r12_cases(man, ents, t3, tarch, expect, edit, back, json_edit, file_edit):
    """The self-test's R12 cases, each a mutation of a copy requiring its own message."""
    def has(e, n):
        return any(f['path'] == 'runs/%s/%s' % (e['run_id'], n) for f in e['files'])

    def load(e, n):
        return json.load(open(os.path.join(tarch, 'runs', e['run_id'], n), encoding='utf-8'))
    pick = lambda pred: next((i for i in t3 if pred(ents[i])), None)
    plain = pick(lambda e: not has(e, 'expected.json'))
    guard = pick(lambda e: has(e, 'expected.json') and load(e, 'expected.json')['outputs'][0]['kind'] == 'guard')
    prbc = pick(lambda e: has(e, 'expected.json') and load(e, 'run.json')['event'] == 'pull_request')
    pushbc = pick(lambda e: has(e, 'expected.json') and load(e, 'run.json')['event'] == 'push'
                  and load(e, 'expected.json')['outputs'][0]['kind'] == 'base-check')
    ci = next((i for i, e in enumerate(ents) if str(e.get('id', '')).startswith('ci-')), None)
    if None in (plain, guard, prbc, pushbc, ci) or len(man.get('tranche3', {}).get('remaining', [])) < 2:
        expect('the R12 cases need a plain, a guard, a pull-request and a push base-check entry, a CI entry and two '
               'remaining runs', lambda: None, lambda: None, 'R12', 'an impossible message')
        return
    P = lambda i, n: os.path.join(tarch, 'runs', ents[i]['run_id'], n)
    fi = lambda m, i, n: next(f for f in m['entries'][i]['files'] if f['path'].endswith('/' + n))
    O = lambda d: d['outputs'][0]
    expect('a tranche-3 entry whose id is not its run', edit(lambda m: m['entries'][plain].__setitem__('id', 'run-1')), back,
           'R12', 'not an entry of tranche 3')
    expect('a tranche-3 entry without jobs.json', edit(lambda m: m['entries'][plain].__setitem__(
        'files', [f for f in m['entries'][plain]['files'] if not f['path'].endswith('/jobs.json')])), back, 'R12',
           'no run.json or no jobs.json')
    expect('a run.json that is not JSON', *file_edit(P(plain, 'run.json'), lambda b: b[:-3]), rule='R12', msg='is not JSON')
    expect('a run.json naming no head commit', *json_edit(P(plain, 'run.json'), lambda d: d.__setitem__('head_sha', 'abc')),
           rule='R12', msg='run.json names another run')
    expect('a recorded expiry that is not the creation plus 90 days',
           edit(lambda m: m['entries'][plain].__setitem__('expires', '2000-01-01')), back, 'R12', 'creation plus 90 days')
    expect('a jobs.json with no jobs', *json_edit(P(plain, 'jobs.json'), lambda d: d.__setitem__('jobs', [])), rule='R12',
           msg='not the run\'s job list')
    expect('a job at another head commit', *json_edit(P(plain, 'jobs.json'), lambda d: d['jobs'][0].__setitem__('head_sha', '0' * 40)),
           rule='R12', msg='another head commit or attempt')
    expect('an expected.json of another schema', *json_edit(P(guard, 'expected.json'), lambda d: d.__setitem__('schema', 'x')),
           rule='R12', msg='unknown schema or version')
    expect('an expected.json naming another event', *json_edit(P(prbc, 'expected.json'), lambda d: d['run'].__setitem__('event', 'push')),
           rule='R12', msg='head commit, event or attempt than run.json')
    expect('an expected.json with no output', *json_edit(P(guard, 'expected.json'), lambda d: d.__setitem__('outputs', [])),
           rule='R12', msg='records no output')
    expect('an output naming no job of the run', *json_edit(P(guard, 'expected.json'), lambda d: O(d).__setitem__('job_id', '1')),
           rule='R12', msg='names no job of jobs.json')
    expect('an output of unknown kind', *json_edit(P(guard, 'expected.json'), lambda d: O(d).__setitem__('kind', 'lint')),
           rule='R12', msg='unknown kind')
    expect('a push output at another commit', *json_edit(P(pushbc, 'expected.json'),
                                                        lambda d: O(d)['at'].__setitem__('commit', '0' * 40)),
           rule='R12', msg='is not at the run\'s commit')
    expect('a pull-request output whose head is not the run\'s', *json_edit(P(prbc, 'expected.json'),
                                                                          lambda d: O(d)['at'].__setitem__('head', '0' * 40)),
           rule='R12', msg='is not at the run\'s commit')
    expect('a pull-request base check whose served REF is not the recorded merge',
           *json_edit(P(prbc, 'expected.json'), lambda d: O(d)['at'].__setitem__('ref_as_served', '0' * 40)),
           rule='R12', msg='is not at the run\'s commit')
    expect('an output with an empty command', *json_edit(P(guard, 'expected.json'), lambda d: O(d)['recipe'].__setitem__('argv', [])),
           rule='R12', msg='malformed recipe')
    expect('an output served more lines than the log has',
           *json_edit(P(guard, 'expected.json'), lambda d: O(d)['source'].__setitem__('served_lines', 10 ** 6)),
           rule='R12', msg='malformed source')
    expect('an output naming another extractor',
           *json_edit(P(guard, 'expected.json'), lambda d: O(d)['source'].__setitem__('extractor', 'x.py')),
           rule='R12', msg='malformed source')
    expect('a base check whose summary is not its last line',
           *json_edit(P(pushbc, 'expected.json'), lambda d: O(d)['expected'].__setitem__('summary', 'x')),
           rule='R12', msg='malformed expectation')
    expect('a guard check without a message digest',
           *json_edit(P(guard, 'expected.json'), lambda d: O(d)['expected']['checks'][0].__setitem__('message_sha256', 'x')),
           rule='R12', msg='malformed expectation')
    expect('guard counts that disagree with the checks',
           *json_edit(P(guard, 'expected.json'), lambda d: O(d)['expected']['counts'].__setitem__('R7', -1)),
           rule='R12', msg='guard counts')
    expect('an expected.json whose source digest is not its output\'s',
           edit(lambda m: fi(m, guard, 'expected.json').__setitem__('source_sha256', '0' * 64)), back, 'R12', 'does not derive')
    expect('a tranche-3 run that a CI entry already retains',
           edit(lambda m: m['entries'][ci].__setitem__('run_id', ents[plain]['run_id'])), back, 'R12', 'attested or already retained')
    expect('a manifest without its tranche3 section', edit(lambda m: m.pop('tranche3')), back, 'R12', 'section missing')
    expect('a remaining run with a wrong expiry',
           edit(lambda m: m['tranche3']['remaining'][0].__setitem__('expires', '2000-01-01')), back, 'R12', 'malformed or repeated')
    expect('a remaining run listed twice',
           edit(lambda m: m['tranche3']['remaining'].append(dict(m['tranche3']['remaining'][0]))), back, 'R12', 'malformed or repeated')
    expect('a remaining run that has an entry',
           edit(lambda m: m['tranche3']['remaining'][0].__setitem__('run_id', ents[plain]['run_id'])), back, 'R12', 'has an entry')
    expect('remaining runs out of order', edit(lambda m: m['tranche3']['remaining'].reverse()), back, 'R12', 'order of creation')
    expect('a retained run that expires after a remaining one',
           edit(lambda m: m['entries'][plain].__setitem__('expires', '2099-01-01')), back, 'R12', 'expires after a remaining one')
    expect('tranche-3 counts that disagree', edit(lambda m: m['tranche3'].__setitem__('retained', 0)), back, 'R12', 'counts disagree')


def r13_cases(man, ents, rs, troot, tarch, expect, edit, back, json_edit, file_edit):
    """The self-test's R4 research-build and R13 cases, each a mutation of a copy requiring its own message."""
    i = rs[0]
    e = ents[i]
    rid, eid = e['run_id'], e['id']
    P = lambda n: os.path.join(tarch, 'ci', rid, n)
    ci = next((k for k, x in enumerate(ents) if str(x.get('id', '')).startswith('ci-')), None)
    res = json.load(open(P('results.json'), encoding='utf-8'))
    part = next((m for m, x in res['expected']['modules'].items() if x['status'] in ('partial', 'none')), None)
    if ci is None or part is None:
        expect('the R13 cases need a CI entry and a research build with a partial module', lambda: None, lambda: None,
               'R13', 'an impossible message')
        return
    G = lambda m, what: m.__setitem__('missing', [g for g in m['missing'] if not (g['id'] == eid and g['what'] == what)])
    expect('a research entry with neither citations nor a pending citation',
           edit(lambda m: m['entries'][i].pop('awaiting_citation')), back, 'R7', 'no citations')
    expect('a research entry whose pending citation names no pull request',
           edit(lambda m: m['entries'][i]['awaiting_citation'].__setitem__('pull_request', 'x')), back, 'R13', 'no pending citation')
    expect('a research entry that carries citations and a pending citation together', edit(
        lambda m: m['entries'][i].__setitem__('citations', [{'path': 'x.md', 'line': 1, 'blob': '0' * 40, 'tokens': [rid],
                                                             'claims': []}])), back, 'R13', 'a pending citation together')
    expect('a research entry whose id is not its run', edit(lambda m: m['entries'][i].__setitem__('id', 'research-1')), back,
           'R13', 'not a research-build entry')
    expect('a research entry without results.json', edit(lambda m: m['entries'][i].__setitem__(
        'files', [f for f in m['entries'][i]['files'] if not f['path'].endswith('/results.json')])), back, 'R13',
           'no run.json, jobs.json or results.json')
    expect('a research run.json that is not JSON', *file_edit(P('run.json'), lambda b: b[:-3]), rule='R13', msg='is not JSON')
    expect('a research result at another head commit', *json_edit(P('results.json'), lambda d: d['run'].__setitem__('head_sha', '0' * 40)),
           rule='R13', msg='another run, head commit or attempt')
    expect('a research result relabelled as a bridge result',
           *json_edit(P('results.json'), lambda d: d.__setitem__('kind', 'bridge')), rule='R13', msg='not a research-build result')
    expect('the same relabel fails the gate rule', *json_edit(P('results.json'), lambda d: d.__setitem__('kind', 'bridge')),
           rule='R4', msg='no gate verdict')
    expect('a research build that records a gate',
           *json_edit(P('results.json'), lambda d: d['expected'].__setitem__('gate', {'verdict': 'PASS', 'steps': []})),
           rule='R4', msg='research build and records a gate')
    expect('a research result from another job', *json_edit(P('results.json'), lambda d: d['run'].__setitem__('job_id', '1')),
           rule='R13', msg='not from a job of jobs.json')
    expect('a research result whose source digest is not recorded',
           edit(lambda m: next(f for f in m['entries'][i]['files'] if f['path'].endswith('/results.json')).__setitem__(
               'source_sha256', '0' * 64)), back, 'R13', 'does not derive from its served log')
    for what in ('release gate', 'exact-control replay output', 'axiom reports of %s' % part):
        expect('a research entry without its gap %r' % what[:40], edit(lambda m, w=what: G(m, w)), back, 'R13', 'not a recorded gap')
    head = res['run']['head_sha']
    expect('a retained source commit also recorded as a gap', edit(lambda m: m['missing'].append(
        {'id': eid, 'run_id': rid, 'what': 'source commit %s' % head, 'why': 'x'})), back, 'R13', 'retained and also a recorded gap')
    op = os.path.join(tarch, 'objects', 'manifest.json')
    expect('a source commit neither retained nor a recorded gap', *file_edit(op, lambda b: json.dumps(dict(
        json.loads(b), objects=[o for o in json.loads(b)['objects'] if o['oid'] != head])).encode('utf-8')),
           rule='R13', msg='neither retained under objects/ nor a recorded gap')
    expect('a research entry without its gap for the design files\' reports', edit(lambda m: m.__setitem__('missing', [
        g for g in m['missing'] if not (g['id'] == eid and g['what'].startswith('axiom reports of the research design'))])), back,
           'R13', 'not a recorded gap')
    expect('a research run that a CI entry already retains',
           edit(lambda m: m['entries'][ci].__setitem__('run_id', rid)), back, 'R13', 'already has another entry')
    cite = os.path.join(troot, 'verification', 'ZZ-CITES.md')
    expect('a research run that a tracked file now cites', lambda: open(cite, 'w').write('run %s\n' % rid),
           lambda: os.remove(cite), 'R13', 'is now cited at verification/ZZ-CITES.md')
    expect('a pending citation that names no round', edit(lambda m: m['entries'][i]['awaiting_citation'].pop('round')),
           back, 'R13', 'no pending citation naming its record, round')
    # the citation lifecycle, on a stand-in for the record laid out as PRESERVE-INDUCT-1's is: the run's head in full
    # on the line before the recorded line, the run on the recorded line. Pending while the record is absent,
    # eligible (and not cited) once it lands, cited once mapped; a wrong head or run, a line elsewhere, an unmapped
    # line, or the record removed after the mapping fails.
    aw = e['awaiting_citation']
    rec, at = aw['record'], aw['line']
    rpath = os.path.join(troot, rec)
    head = json.load(open(P('run.json'), encoding='utf-8'))['head_sha']
    other = hashlib.sha1(b'another head ' + head.encode()).hexdigest()
    # every research entry pending on the same record: its run's head on the line before its recorded line
    same = [(x['run_id'], json.load(open(os.path.join(tarch, 'ci', x['run_id'], 'run.json'), encoding='utf-8'))['head_sha'],
             x['awaiting_citation']['line']) for x in ents if (x.get('awaiting_citation') or {}).get('record') == rec]

    def record(h=head, r=rid, extra=''):
        L = ['# a stand-in for %s as it lands on main' % aw['round']] + [''] * (max(n for _, _, n in same) - 1)
        for run_, h_, n in same:
            if run_ == rid:
                h_, run_ = h, r
            L[n - 2] = 'The design compiled at `%s`, workflow run' % h_
            L[n - 1] = '[%s](runs/%s).' % (run_, run_)
        return '\n'.join(L) + '\n' + extra

    def land(t):
        def go():
            os.makedirs(os.path.dirname(rpath), exist_ok=True)
            open(rpath, 'w', encoding='utf-8').write(t)
        return go

    def unland():
        if os.path.exists(rpath):
            os.remove(rpath)

    def mapped(t, lines, who=None):
        data = t.encode('utf-8')
        L = t.split('\n')
        k = i if who is None else who
        r_ = ents[k]['run_id']

        def fn(m):
            x = m['entries'][k]
            x.pop('awaiting_citation')
            x['citations'] = [{'path': rec, 'line': n, 'blob': blob_id(data), 'tokens': [r_],
                               'claims': [{'line': n, 'text': r_, 'status': 'retained', 'in': ['ci/%s/results.json' % r_],
                                           'note': 'results.json names the run'}]} for n in lines]
            assert all(r_ in L[n - 1] for n in lines)
        return fn

    def land_and_map(t, lines):
        def go():
            land(t)()
            edit(mapped(t, lines))()
        return go
    unmap = lambda: (unland(), back())
    good = record()
    assert good.split('\n')[at - 1].startswith('[%s]' % rid)
    expect('lifecycle (a): the intended record not in the tree, the entry pending', lambda: None, lambda: None,
           state=(eid, 'pending'))
    expect('lifecycle (b): the intended record lands citing the run and its head, the manifest unchanged (eligible)',
           land(good), unland, state=(eid, 'eligible'))
    expect('lifecycle (c): the entry maps the record\'s citing line (cited)', land_and_map(good, [at]), unmap,
           state=(eid, 'cited'))
    expect('lifecycle (d): the intended record lands naming another head beside the run', land(record(h=other)), unland,
           'R13', 'names another run head beside the run', who=eid)
    expect('lifecycle (d): the intended record lands citing another run', land(record(r='1' + rid)), unland, 'R13',
           'is in the tree and does not cite run %s' % rid, who=eid)
    expect('lifecycle (e): the record removed while the entry maps it', edit(mapped(good, [at])), back, 'R3',
           'citing file %s missing' % rec)
    expect('the intended record lands citing the run without its head', land(
        good.replace('The design compiled at `%s`, workflow run' % head, 'The design compiled at the source, workflow run')),
           unland, 'R13', 'does not state the full id beside the run', who=eid)
    expect('the intended record lands with the head mistyped after digit 10', land(record(
        h=head[:10] + ''.join('1' if c == '0' else '0' for c in head[10:18]) + head[18:])), unland, 'R13',
           'names another run head beside the run', who=eid)
    expect('the intended record lands citing the run on another line than recorded', land('\n' + good), unland, 'R13',
           'not on the recorded line %d' % at, who=eid)
    expect('the intended record lands, and another file also cites the run', lambda: (land(good)(), open(
        os.path.join(troot, 'verification', 'ZZ-CITES.md'), 'w').write('run %s\n' % rid)),
           lambda: (unland(), os.remove(os.path.join(troot, 'verification', 'ZZ-CITES.md'))), 'R13',
           'is now cited at verification/ZZ-CITES.md', who=eid)
    expect('a mapped citation whose line names another head', land_and_map(record(h=other), [at]), unmap, 'R13',
           'names another run head beside the run', who=eid)
    expect('the record cites the run on two lines and the entry maps one', land_and_map(good + 'Run %s again.\n' % rid, [at]),
           unmap, 'R13', 'is now cited at %s:%d' % (rec, good.count('\n') + 1), who=eid)
    expect('a research run.json that names no head commit', *json_edit(P('run.json'), lambda d: d.pop('head_sha')),
           rule='R13', msg='another run, head commit or attempt', who=eid)
    expect('a research run.json that names no head commit leaves no citation state',
           *json_edit(P('run.json'), lambda d: d.pop('head_sha')), rule='R13', msg='another run, head commit or attempt',
           who=eid, also=lambda: eid not in R13_STATES and r13_summary() == 'citations (R13): 0 cited, %d pending (record '
           'not in the tree), 0 eligible for promotion (not cited)' % (len(rs) - 1))
    expect('a research entry without run.json', edit(lambda m: m['entries'][i].__setitem__(
        'files', [f for f in m['entries'][i]['files'] if not f['path'].endswith('/run.json')])), back, 'R13',
           'no run.json, jobs.json or results.json', who=eid)
    # partial and full promotion of the entries pending on one record
    j = rs[1]
    eid2, at2 = ents[j]['id'], ents[j]['awaiting_citation']['line']

    def land_and_map_all(t):
        def go():
            land(t)()
            edit(lambda m: (mapped(t, [at])(m), mapped(t, [at2], who=j)(m)))()
        return go
    expect('lifecycle (c-partial): one entry mapped, the other on the same record still pending (eligible)',
           land_and_map(good, [at]), unmap, states=[(eid, 'cited'), (eid2, 'eligible')])
    expect('lifecycle (c-full): every entry on the record mapped (cited)', land_and_map_all(good), unmap,
           states=[(eid, 'cited'), (eid2, 'cited')])
    # the citation rule (check_objects.run_citations) on every line of the record that names the run
    digest = hashlib.sha256(b'a stand-in log\n').hexdigest()
    evrow = '| `evidence/run1-%s.json` | `%s` |\n' % (rid, digest)
    end = good.count('\n') + 1
    runl = good.split('\n')[at - 1]

    def line(t, n, new):
        L = t.split('\n')
        L[n - 1] = new
        return '\n'.join(L)
    expect('CN-3 d-far: a far line of the record cites the run beside another head',
           land(good + '\n' + 'Run %s was dispatched on `%s…`.\n' % (rid, other[:8])), unland, 'R13', 'names another run head',
           who=eid)
    expect('CN-3 d-far-nohead: a far line of the record cites the run without its head', land(good + 'Run %s passed.\n' % rid),
           unland, 'R13', 'does not state the full id', who=eid)
    expect('CN-3: a duplicate free-standing citation with a conflicting full head', land(
        good + '\n' + 'Compiled again at `%s`, workflow run\n[%s](runs/%s).\n' % (other, rid, rid)), unland, 'R13',
           'names another run head', who=eid)
    expect('CN-3: the run named inside an evidence file name with its digest (eligible)', land(good + evrow), unland,
           state=(eid, 'eligible'))
    expect('CN-3: the same, mapped to the citation alone (cited)', land_and_map(good + evrow, [at]), unmap,
           state=(eid, 'cited'))
    expect('CN-3: an embedded mention beside a different full head',
           land(good + '\n' + '| `evidence/run1-%s.json` | head `%s` |\n' % (rid, other)), unland, 'R13',
           'names another run head', who=eid)
    expect('N1: an all-decimal 45-digit word beside the run\'s file name',
           land(good + '\n' + '| `evidence/run1-%s.json` | `%s` |\n' % (rid, '9' * 45)), unland, 'R13',
           'names another run head', who=eid)
    expect('CN-3: the recorded line names the run only inside an identifier',
           land(line(good, at, '`evidence/run1-%s.json`.' % rid)), unland, 'R13', 'only inside an identifier', who=eid)
    expect('CN-3: a mapped line that names the run only inside an identifier', land_and_map(good + evrow, [at, end]),
           unmap, 'R13', 'only inside an identifier', who=eid)
    expect('CN-3: a citation mapped twice', land_and_map(good, [at, at]), unmap, 'R13', 'twice', who=eid)
    expect('N1: another head in uppercase beside the run', land(record(h=other.upper())), unland, 'R13',
           'names another run head', who=eid)
    expect('N2: the summary counts an eligible entry apart, never as cited', land(good), unland, state=(eid, 'eligible'),
           also=lambda: r13_summary() == 'citations (R13): 0 cited, 0 pending (record not in the tree), %d eligible for '
           'promotion (not cited)' % len(rs))
    # the digest boundary: a hex word of 64 digits or more is opaque. A genuine digest passes; a file name with a
    # digest never establishes the citation, and such a word never states the head; a conflicting head beside the
    # citation fails even beside a digest. Another head written as part of such a word is not read: the documented
    # limitation, recorded with its passing verdict so that a change of behaviour shows here
    expect('boundary (a): a genuine 64-digit digest beside the citation and the file name passes', land(line(
        good, at, runl + ' Log `evidence/run1-%s.json`, sha256 `%s`.' % (rid, digest))), unland, state=(eid, 'eligible'))
    expect('boundary (b): a file name with a digest never establishes the citation', land(line(
        good, at, '`evidence/run1-%s.json` sha256 `%s%s`.' % (rid, '0' * 24, head))), unland, 'R13',
           'only inside an identifier', who=eid)
    expect('boundary (b): a 64-digit hex word never states the head', land(line(line(
        good, at - 1, 'The design compiled at the source, workflow run'), at, runl + ' Digest `%s%s`.' % ('0' * 24, head))),
           unland, 'R13', 'does not state the full id', who=eid)
    expect('boundary (c): a conflicting head beside the citation fails, even beside a digest', land(line(
        record(h=other), at, runl + ' sha256 `%s`.' % digest)), unland, 'R13', 'names another run head', who=eid)
    expect('documented limitation: another head as the last 40 digits of a 64-digit word beside a file name passes',
           land(good + '| `evidence/run1-%s.json` | `%s%s` |\n' % (rid, '0' * 24, other)), unland, state=(eid, 'eligible'))
    verbatim_cases(ents, rs, i, e, rid, eid, head, other, aw, at, good, troot, ci, expect, edit, back, land, unland,
                   mapped, line)


def _set_verbatim_override(t):
    """The self-test's seam. Refuses outside the self-test."""
    global _VERBATIM_OVERRIDE
    if not _IN_SELF_TEST:
        raise RuntimeError('the verbatim substitute is set only by the self-test')
    _VERBATIM_OVERRIDE = t


def verbatim_cases(ents, rs, i, e, rid, eid, head, other, aw, at, good, troot, ci, expect, edit, back, land, unland,
                   mapped, line):
    """The self-test's verbatim-mention cases on the R13 fixture, through the seam: a stand-in tuple for entry i,
    whose copy is a stand-in file naming the run once on line 3. Each fail-closed case changes one thing; the
    citation cases show that a verbatim mention is never a citation."""
    A = VERBATIM_ALLOWLIST[0]
    TP, TP2 = 'verification/ZZ-SELF-TEST/verbatim-copy.md', 'verification/ZZ-SELF-TEST/verbatim-moved.md'
    cites = os.path.join(troot, 'verification', 'ZZ-CITES.md')

    def copy_text(at_lines=(3,), twice=False):
        L = ['# a stand-in for a pinned verbatim copy', '', '| HC6 | conditional, not re-verified |', '',
             '| HC7 | as H27 |', '']
        for n in at_lines:
            L[n - 1] = '| HC6 | conditional [D #831, run %s per B:260-264, not re-verified] |' % (
                rid + (' (run %s)' % rid if twice else ''))
        return ('\n'.join(L) + '\n').encode('utf-8')
    gc = copy_text()
    H = lambda b: hashlib.sha256(b).hexdigest()

    def tup(**kw):
        t = {'entry': eid, 'run': rid, 'head': head, 'path': TP, 'line': 3, 'blob': blob_id(gc), 'sha256': H(gc),
             'copy_of': dict(A['copy_of']), 'awaiting': {k: aw[k] for k in AWAITING_KEYS}, 'cited_lines': [at]}
        t.update(kw)
        return t

    def field(t, **kw):
        f = {'path': t['path'], 'line': t['line'], 'blob': t['blob'], 'sha256': t['sha256'], 'copy_of': dict(t['copy_of']),
             'note': 'a pinned verbatim copy names the run as its source\'s provenance; not a citation'}
        f.update(kw)
        return f

    def seam(t=None, copy=gc, at_path=TP, fld=None, mfn=None, rec_text=None, override=True, extra=None):
        t = t or tup()

        def go():
            if copy is not None:
                p = os.path.join(troot, at_path)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, 'wb').write(copy)
            if override:
                _set_verbatim_override((t,))

            def fn(m):
                m['entries'][i]['verbatim_mentions'] = fld if fld is not None else [field(t)]
                if mfn:
                    mfn(m)
            edit(fn)()
            if rec_text is not None:
                land(rec_text)()
            if extra:
                extra()

        def undo():
            _set_verbatim_override(None)
            while made:
                q = made.pop()
                if os.path.islink(q) or os.path.isfile(q):
                    os.remove(q)
                elif os.path.isdir(q):
                    shutil.rmtree(q)
            for p in (TP, TP2):
                if os.path.lexists(os.path.join(troot, p)):
                    os.remove(os.path.join(troot, p))
            if os.path.exists(cites):
                os.remove(cites)
            unland()
            back()
        return go, undo
    R = lambda name, msg, who=eid, **kw: expect(name, *seam(**kw), rule='R13', msg=msg, who=who)
    made = []

    def put(rel, data=None, link=None):
        """Creates troot/rel, a file of data or a symbolic link to link, and records it for the seam's undo."""
        q = os.path.join(troot, rel)
        os.makedirs(os.path.dirname(q), exist_ok=True)
        if link is not None:
            os.symlink(link, q)
        else:
            open(q, 'wb').write(data)
        made.append(q)

    def git(*args, data=None):
        r = subprocess.run(['git', '-C', troot] + list(args), input=data, capture_output=True)
        if r.returncode:
            raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr[-200:]))
        return r.stdout.decode().strip()

    def index(mode, content=gc, rel=TP):
        """Makes troot a git work tree whose index holds rel at mode with content's blob; mode None leaves it
        empty."""
        def go():
            made.append(os.path.join(troot, '.git'))
            git('init', '-q')
            if mode is not None:
                oid = git('hash-object', '-w', '--stdin', data=content)
                git('update-index', '--add', '--cacheinfo', '%s,%s,%s' % (mode, oid, rel))
        return go
    pend = 'citations (R13): 0 cited, %d pending (record not in the tree), 0 eligible for promotion (not cited)' % len(rs)
    # admitted, and never a citation
    expect('verbatim: the approved mention of a pinned copy passes, and the entry stays pending', *seam(),
           state=(eid, 'pending'), also=lambda: VERBATIM_STATES.get(eid) == (TP, 3) and R13_STATES[eid][1] is None
           and r13_summary() == pend)
    expect('verbatim: the record lands, and the entry is eligible on the record\'s line alone', *seam(rec_text=good),
           state=(eid, 'eligible'), also=lambda: R13_STATES[eid][1] == [at])
    expect('verbatim: promoted on the record\'s line alone, the entry is cited', *seam(mfn=mapped(good, [at]),
                                                                                       rec_text=good),
           state=(eid, 'cited'))
    R('verbatim: the mention does not satisfy the pending citation (the record lands without citing the run)',
      'is in the tree and does not cite run %s' % rid, rec_text=line(line(good, at, ''), at - 1, ''))

    def cite_copy(m):
        mapped(good, [at])(m)
        m['entries'][i]['citations'].append({'path': TP, 'line': 3, 'blob': blob_id(gc), 'tokens': [rid], 'claims': [
            {'line': 3, 'text': rid, 'status': 'retained', 'in': ['ci/%s/results.json' % rid], 'note': 'x'}]})
    # the entry's own citation of the copy fails in check() (F1) and also withdraws the admission in the filter
    expect('verbatim: the copy\'s line mapped as a citation', *seam(mfn=cite_copy, rec_text=good), rule='R13',
           msg='a verbatim mention is not a citation', who=eid, also=lambda: eid not in VERBATIM_STATES)
    R('verbatim: the copy named as the pending record', 'pending citation is not the approved citation context',
      mfn=lambda m: m['entries'][i]['awaiting_citation'].__setitem__('record', TP))
    # fail closed: the bytes, path, line and run
    R('verbatim: the copy changed by one byte, the manifest unchanged', 'is not the approved blob', copy=gc + b' ')
    R('verbatim: the manifest asserts the changed copy\'s blob', 'is not the owner-approved tuple', copy=gc + b' ',
      fld=[field(tup(), blob=blob_id(gc + b' '))])
    R('verbatim: the manifest asserts another sha256', 'is not the owner-approved tuple',
      fld=[field(tup(), sha256=H(gc + b' '))])
    # each digest on its own: a constructed tuple whose one digest is right and the other wrong
    R('verbatim: SHA-1 matches and SHA-256 does not', 'is not the approved sha256', t=tup(sha256=H(gc + b' ')))
    R('verbatim: SHA-256 matches and SHA-1 does not', 'is not the approved blob', t=tup(blob=blob_id(gc + b' ')))
    R('verbatim: the copy at another path, the manifest following it', 'is not the owner-approved tuple', at_path=TP2,
      fld=[field(tup(), path=TP2)])
    R('verbatim: the copy moved, the manifest unchanged', 'is absent', at_path=TP2)
    R('verbatim: the copy absent', 'is absent', copy=None)
    R('verbatim: the line changed in the manifest', 'is not the owner-approved tuple', fld=[field(tup(), line=4)])
    moved = copy_text((5,))
    R('verbatim: the mention moved to another line of the copy', 'does not name run %s exactly once' % rid, copy=moved,
      t=tup(blob=blob_id(moved), sha256=H(moved)))
    twice = copy_text(twice=True)
    R('verbatim: the run named twice on the approved line', 'does not name run %s exactly once' % rid, copy=twice,
      t=tup(blob=blob_id(twice), sha256=H(twice)))
    second = copy_text((3, 5))
    R('verbatim: a second line of the copy names the run', 'on another line (5)', copy=second,
      t=tup(blob=blob_id(second), sha256=H(second)))
    R('verbatim: another file also names the run', 'is now cited at verification/ZZ-CITES.md',
      extra=lambda: open(cites, 'w').write('run %s\n' % rid))
    R('verbatim: the approved run differs from the entry\'s run', 'not the approved run', t=tup(run='1' + rid))
    R('verbatim: the approved head differs from the run\'s head', 'not the approved head', t=tup(head=other))
    j = rs[1]
    eid2 = ents[j]['id']

    def move(m):
        m['entries'][j]['verbatim_mentions'] = m['entries'][i].pop('verbatim_mentions')
    R('verbatim: the mention listed on another research entry', 'outside the owner-approved allowlist', who=eid2, mfn=move)
    # fail closed: the citation context
    R('verbatim: the pending record changed', 'pending citation is not the approved citation context',
      mfn=lambda m: m['entries'][i]['awaiting_citation'].__setitem__('record', 'verification/ZZ-SELF-TEST/other.md'))
    R('verbatim: the pending line changed', 'pending citation is not the approved citation context',
      mfn=lambda m: m['entries'][i]['awaiting_citation'].__setitem__('line', at + 1))
    R('verbatim: the pending citation\'s head changed', 'pending citation is not the approved citation context',
      mfn=lambda m: m['entries'][i]['awaiting_citation'].__setitem__('head', other))
    R('verbatim: promoted on other record lines than approved', 'citations are not the approved citation context',
      t=tup(cited_lines=[at + 1]), mfn=mapped(good, [at]), rec_text=good)
    # the allowlist and the field's form
    R('verbatim: a tuple outside the hardcoded allowlist', 'is not the owner-approved tuple' if eid == A['entry']
      else 'outside the owner-approved allowlist', override=False)
    R('verbatim: the field on a CI entry', 'outside the owner-approved allowlist', who=ents[ci]['id'],
      mfn=lambda m: m['entries'][ci].__setitem__('verbatim_mentions', [field(tup())]))
    R('verbatim: two mentions', 'is malformed', fld=[field(tup()), field(tup())])
    R('verbatim: the field is not a list', 'is malformed', fld=field(tup()))
    R('verbatim: a claim annotation on the mention', 'is malformed', fld=[field(tup(), claims=[{'line': 3}])])
    R('verbatim: an empty note', 'is malformed', fld=[field(tup(), note=' ')])
    R('verbatim: the source changed', 'is not the owner-approved tuple',
      fld=[field(tup(), copy_of={'commit': other, 'path': A['copy_of']['path']})])
    # no citation of any entry may map the copy (F1): another entry, at the approved line and at another line, and
    # under another path that resolves to the copy
    ce = ents[ci]['id']

    def cross(line_, path_=TP):
        def fn(m):
            m['entries'][ci]['citations'].append({'path': path_, 'line': line_, 'blob': blob_id(gc), 'tokens': [rid],
                                                  'claims': [{'line': line_, 'text': rid, 'status': 'not retained',
                                                              'note': 'x'}]})
        return fn
    R('verbatim: another entry maps the copy at the approved line', 'a verbatim mention is not a citation', who=ce,
      mfn=cross(3))
    R('verbatim: another entry maps the copy at another line', 'a verbatim mention is not a citation', who=ce,
      mfn=cross(1))
    R('verbatim: another entry maps the copy under another path that resolves to it',
      'a verbatim mention is not a citation', who=ce, mfn=cross(3, 'verbatim-alias.md'),
      extra=lambda: put('verbatim-alias.md', link=TP))
    # a regular file at exactly that path, reached through no symbolic link (F2)
    real = 'verification/ZZ-SELF-TEST/verbatim-real.md'
    R('verbatim: a symbolic link at the copy\'s path', 'is reached through a symbolic link', copy=None,
      extra=lambda: (put(real, gc), put(TP, link='verbatim-real.md')))
    R('verbatim: a symbolic link at the copy\'s path to an unscanned extension', 'is reached through a symbolic link',
      copy=None, extra=lambda: (put(TP + '.tex', gc), put(TP, link='verbatim-copy.md.tex')))
    R('verbatim: a symbolic link at the copy\'s path into an unscanned directory', 'is reached through a symbolic link',
      copy=None, extra=lambda: (put('verification/ZZ-SELF-TEST/node_modules/c.md', gc),
                                put(TP, link='node_modules/c.md')))
    TPD = 'verification/ZZ-SELF-TEST/vdir/verbatim-copy.md'
    R('verbatim: a directory symbolic link at a parent of the copy\'s path', 'is reached through a symbolic link',
      copy=None, t=tup(path=TPD), extra=lambda: (put('verification/ZZ-SELF-TEST/node_modules/vreal/verbatim-copy.md', gc),
                                                 put('verification/ZZ-SELF-TEST/vdir', link='node_modules/vreal')))
    # where the tree is a git work tree, its index holds the copy as a regular file at the approved blob
    expect('verbatim: the git index holds the copy as a regular file at the approved blob', *seam(
        extra=index('100644')), state=(eid, 'pending'), also=lambda: VERBATIM_STATES.get(eid) == (TP, 3))
    R('verbatim: the git index holds the copy as a symbolic link (mode 120000)', 'the git index holds 120000',
      extra=index('120000'))
    R('verbatim: the git index holds the copy at another blob', 'the git index holds 100644',
      extra=index('100644', gc + b' '))
    R('verbatim: the git index holds nothing at the copy\'s path', 'the git index holds nothing', extra=index(None))
    # the line is an integer (N1)
    R('verbatim: a float line', 'is malformed', fld=[field(tup(), line=3.0)])
    one = copy_text((1,))
    R('verbatim: a bool line', 'is malformed', copy=one, t=tup(line=1, blob=blob_id(one), sha256=H(one)),
      fld=[field(tup(line=1, blob=blob_id(one), sha256=H(one)), line=True)])
    expect('verbatim: the seam is unset after the verbatim cases', lambda: None, lambda: None,
           also=lambda: _VERBATIM_OVERRIDE is None)


# the canonical form of VERBATIM_ALLOWLIST, pinned: a change to the allowlist changes this digest in the same
# reviewed diff
VERBATIM_ALLOWLIST_SHA256 = '9608ae67e75fbb6e1335d977f2995458fe2b86b260fa8205cd9be7bb4c794734'


def verbatim_live_cases(ents, troot, tarch, root, expect, edit, back):
    """The live tuple's cases, on the copy before the R13 fixture moves any entry: the allowlist is the one approved
    tuple; listing it fails closed without its copy or with other bytes at its path; the real entry's lifecycle
    (pending, eligible, cited) when the tree holds the approved copy, or, when it does not, no entry lists a verbatim
    mention; and the seam: closed outside the self-test, reachable by no flag, environment variable or manifest field."""
    A = VERBATIM_ALLOWLIST[0]
    canon = json.dumps(VERBATIM_ALLOWLIST, sort_keys=True, separators=(',', ':')).encode('utf-8')
    expect('verbatim (live): the hardcoded allowlist is exactly the one owner-approved tuple', lambda: None,
           lambda: None, also=lambda: len(VERBATIM_ALLOWLIST) == 1 and _VERBATIM_OVERRIDE is None and
           hashlib.sha256(canon).hexdigest() == VERBATIM_ALLOWLIST_SHA256)
    k = next((n for n, x in enumerate(ents) if x.get('id') == A['entry']), None)
    if k is None:
        expect('verbatim (live): the approved entry is in the manifest', lambda: None, lambda: None, 'R13',
               'an impossible message')
        return
    fld = {'path': A['path'], 'line': A['line'], 'blob': A['blob'], 'sha256': A['sha256'], 'copy_of': dict(A['copy_of']),
           'note': 'a pinned verbatim copy of F2 thread I names the run as its source\'s provenance; not a citation'}
    lp = os.path.join(troot, A['path'])

    def live(text, mfn=None, rec_text=None):
        saved = open(lp, 'rb').read() if os.path.isfile(lp) else None
        rp = os.path.join(troot, A['awaiting']['record'])
        rsaved = open(rp, 'rb').read() if os.path.isfile(rp) else None

        def go():
            def fn(m):
                m['entries'][k]['verbatim_mentions'] = [fld]
                if mfn:
                    mfn(m)
            edit(fn)()
            if text is None:
                if os.path.isfile(lp):
                    os.remove(lp)
            elif text is not True:
                os.makedirs(os.path.dirname(lp), exist_ok=True)
                open(lp, 'wb').write(text)
            if os.path.isfile(rp):
                os.remove(rp)
            if rec_text is not None:
                os.makedirs(os.path.dirname(rp), exist_ok=True)
                open(rp, 'w', encoding='utf-8').write(rec_text)

        def undo():
            back()
            if saved is None:
                if os.path.isfile(lp):
                    os.remove(lp)
            else:
                open(lp, 'wb').write(saved)
            if rsaved is None:
                if os.path.isfile(rp):
                    os.remove(rp)
            else:
                open(rp, 'wb').write(rsaved)
        return go, undo
    expect('verbatim (live): the approved tuple listed without its copy fails closed', *live(None), rule='R13',
           msg='is absent', who=A['entry'])
    expect('verbatim (live): other bytes at the approved path fail', *live(
        ('| HC6 | run %s |\n' % A['run']).encode('utf-8')), rule='R13', msg='is not the approved blob', who=A['entry'])
    # the real entry's lifecycle, through the approved tuple and no substitute, when this tree holds the copy
    eid = A['entry']
    if os.path.isfile(os.path.join(root, A['path'])):
        rec = A['awaiting']['record']
        on = [(str(x['run_id']), x['awaiting_citation']['line']) for x in ents
              if (x.get('awaiting_citation') or {}).get('record') == rec and x.get('id') != eid]
        on.append((A['run'], A['awaiting']['line']))
        hd = {r: json.load(open(os.path.join(tarch, 'ci', r, 'run.json'), encoding='utf-8'))['head_sha'] for r, _ in on}
        L = ['# a stand-in for %s as it lands on main' % A['awaiting']['round']] + [''] * (max(n for _, n in on) - 1)
        for r, n in on:
            L[n - 2] = 'The design compiled at `%s`, workflow run' % hd[r]
            L[n - 1] = '[%s](https://github.com/amaybaum/incompleteness/actions/runs/%s).' % (r, r)
        rtext = '\n'.join(L) + '\n'

        def pending(m):
            x = m['entries'][k]
            x.pop('citations', None)
            x['awaiting_citation'] = dict(x.get('awaiting_citation') or {}, **A['awaiting'])

        def cited(m):
            x = m['entries'][k]
            x.pop('awaiting_citation', None)
            x['citations'] = [{'path': rec, 'line': n, 'blob': blob_id(rtext.encode('utf-8')), 'tokens': [A['run']],
                               'claims': [{'line': n, 'text': A['run'], 'status': 'retained',
                                           'in': ['ci/%s/results.json' % A['run']], 'note': 'results.json names the run'}]}
                              for n in A['cited_lines']]
        adm = lambda: VERBATIM_STATES.get(eid) == (A['path'], A['line'])
        expect(LIVE_PRESENT_CASES[0], *live(True, mfn=pending), state=(eid, 'pending'), also=adm)
        expect(LIVE_PRESENT_CASES[1], *live(True, mfn=pending, rec_text=rtext), state=(eid, 'eligible'),
               also=lambda: adm() and R13_STATES[eid][1] == [A['awaiting']['line']])
        expect(LIVE_PRESENT_CASES[2], *live(True, mfn=cited, rec_text=rtext), state=(eid, 'cited'), also=adm)
    else:
        expect(LIVE_ABSENT_CASES[0], lambda: None, lambda: None, also=lambda: not any(
            'verbatim_mentions' in x for x in json.load(open(os.path.join(tarch, 'manifest.json'),
                                                             encoding='utf-8'))['entries']))
    # the seam, closed outside the self-test
    verbatim_seam_cases(k, eid, troot, tarch, root, expect, edit, back)


SEAM_NAMES = ('_VERBATIM_OVERRIDE', '_IN_SELF_TEST', '_set_verbatim_override', 'verbatim_allowlist',
              'VERBATIM_ALLOWLIST', 'VERBATIM_STATES', 'verbatim_seam_leak')


def seam_static_scan(src, objects_src):
    """The self-test's static scan of the seam: the problems found, [] when none. In this checker's source, the
    seam's names are assigned only at module level (None or False), in _set_verbatim_override and in self_test; the
    setter is called only from verbatim_cases; nothing reads the environment; and the CLI's modes are exactly the
    four known ones. check_objects.py, which R13 executes in-process, names no part of the seam and reaches no other
    module's namespace (no sys.modules, __import__, importlib or builtins)."""
    import ast
    bad = []
    t = ast.parse(src)
    top = {}
    for f in t.body:
        if isinstance(f, ast.FunctionDef):
            for x in ast.walk(f):
                top[id(x)] = f.name
    fn_of = lambda n: top.get(id(n), '<module>')
    seam = {'_VERBATIM_OVERRIDE', '_IN_SELF_TEST'}
    for n in ast.walk(t):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            tg = n.targets if isinstance(n, ast.Assign) else [n.target]
            names = {x.id for g in tg for x in ast.walk(g) if isinstance(x, ast.Name)}
            if names & seam:
                f = fn_of(n)
                if f == '<module>':
                    if not (isinstance(n.value, ast.Constant) and n.value.value in (None, False)):
                        bad.append('module-level %s' % sorted(names))
                elif f not in ('_set_verbatim_override', 'self_test'):
                    bad.append('%s assigns %s' % (f, sorted(names)))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == '_set_verbatim_override' \
                and fn_of(n) != 'verbatim_cases':
            bad.append('%s calls the setter' % fn_of(n))
        if isinstance(n, (ast.Name, ast.Attribute)) and getattr(n, 'id', getattr(n, 'attr', '')) in ('environ', 'getenv'):
            bad.append('%s reads the environment' % fn_of(n))
    hook = sorted(set(re.findall(r"sys\.argv\[1:\] == \[([^\]]*)\]", src)))
    if hook != ["'--gate'", "'--later-provenance'", "'--module-sets'", "'--self-test'"]:
        bad.append('the CLI modes are %s' % hook)
    for n in ast.walk(ast.parse(objects_src)):
        word = n.id if isinstance(n, ast.Name) else n.attr if isinstance(n, ast.Attribute) else \
            n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else \
            ' '.join(a.name for a in n.names) if isinstance(n, (ast.Import, ast.ImportFrom)) else ''
        if any(w in word for w in SEAM_NAMES + ('__import__', 'importlib', 'builtins')) or \
                isinstance(n, ast.Attribute) and n.attr == 'modules' and isinstance(n.value, ast.Name) and \
                n.value.id == 'sys':
            bad.append('check_objects.py reaches the seam or another module\'s namespace (%s)' % word[:40])
    return bad


def verbatim_seam_cases(k, eid, troot, tarch, root, expect, edit, back):
    """The self-test's substitute cannot be activated outside the self-test: no code but the self-test opens the
    seam (static); no flag reaches it; plain mode ignores the environment; and a substitute leaked into a fresh
    process is inert in check(), refused by the seam's setter, and failed by report() and gate()."""
    A = VERBATIM_ALLOWLIST[0]
    me = os.path.join(HERE, 'check_retention.py')
    src = open(me, encoding='utf-8').read()

    def static():
        return seam_static_scan(src, open(os.path.join(HERE, 'check_objects.py'), encoding='utf-8').read()) == []
    expect('verbatim (seam): only the self-test opens the seam, and nothing reads the environment', lambda: None,
           lambda: None, also=static)
    inject = '\nimport sys\nsys.modules[\'__main__\']._IN_SELF_TEST = True\n'
    expect('verbatim (seam): the static scan fails a check_objects.py that reaches the seam', lambda: None, lambda: None,
           also=lambda: any(x.startswith('check_objects.py') for x in seam_static_scan(src, open(os.path.join(
               HERE, 'check_objects.py'), encoding='utf-8').read() + inject)))

    def no_flags():
        for argv in (['--verbatim-override', '[]'], ['--allowlist', '[]'], ['--self-test', '--verbatim-override'],
                     ['--gate', '--verbatim-override']):
            p = subprocess.run([sys.executable, '-I', me] + argv, cwd=root, capture_output=True, text=True)
            if p.returncode != 2:
                return False
        return True
    expect('verbatim (seam): no command-line flag reaches the substitute', lambda: None, lambda: None, also=no_flags)

    def env_inert():
        st = json.dumps([dict(A, path='verification/ZZ-SELF-TEST/verbatim-copy.md')])
        base = subprocess.run([sys.executable, '-I', me], cwd=root, capture_output=True, text=True, env={})
        lit = subprocess.run([sys.executable, '-I', me], cwd=root, capture_output=True, text=True, env={
            'VERBATIM_OVERRIDE': st, '_VERBATIM_OVERRIDE': st, 'VERBATIM_ALLOWLIST': st,
            'CHECK_RETENTION_VERBATIM': st, '_IN_SELF_TEST': '1'})
        return (base.returncode, base.stdout) == (lit.returncode, lit.stdout)
    expect('verbatim (seam): plain mode ignores the environment', lambda: None, lambda: None, also=env_inert)
    # a substitute leaked into a fresh process, with the copy and field it would admit in the tree
    TP = 'verification/ZZ-SELF-TEST/verbatim-copy.md'
    run = A['run']
    copy = ('# a stand-in copy\n\n| HC6 | [run %s per B:260-264] |\n' % run).encode('utf-8')
    t = dict(A, path=TP, line=3, blob=blob_id(copy), sha256=hashlib.sha256(copy).hexdigest())
    fld = {'path': TP, 'line': 3, 'blob': t['blob'], 'sha256': t['sha256'], 'copy_of': dict(A['copy_of']),
           'note': 'a stand-in that only a substitute would admit'}
    tp = os.path.join(troot, TP)
    lp = os.path.join(troot, A['path'])
    saved = {}

    def go():
        saved['l'] = open(lp, 'rb').read() if os.path.isfile(lp) else None
        if saved['l'] is not None:
            os.remove(lp)
        os.makedirs(os.path.dirname(tp), exist_ok=True)
        open(tp, 'wb').write(copy)
        edit(lambda m: m['entries'][k].__setitem__('verbatim_mentions', [fld]))()

    def undo():
        back()
        if os.path.exists(tp):
            os.remove(tp)
        if saved.get('l') is not None:
            open(lp, 'wb').write(saved['l'])
    probe = r"""
import io, json, sys, types, contextlib
me, tarch, troot, t, eid = sys.argv[1], sys.argv[2], sys.argv[3], json.loads(sys.argv[4]), sys.argv[5]
m = types.ModuleType('check_retention_probe'); m.__file__ = me
exec(compile(open(me, encoding='utf-8').read(), me, 'exec'), m.__dict__)
assert m._VERBATIM_OVERRIDE is None and m._IN_SELF_TEST is False, 'seam open at import'
try:
    m._set_verbatim_override((t,)); raise SystemExit('the setter accepted a substitute outside the self-test')
except RuntimeError:
    pass
m._VERBATIM_OVERRIDE = (t,)
assert m.verbatim_allowlist() is m.VERBATIM_ALLOWLIST, 'a leaked substitute is honoured'
fails, _ = m.check(tarch, troot)
assert any(f.startswith('R13 %s:' % eid) and 'not the owner-approved tuple' in f for f in fails), fails[:3]
assert eid not in m.VERBATIM_STATES, 'a leaked substitute admitted the stand-in'
def past(*a, **k):
    raise SystemExit('ran past the entry guard')
m.check = m.history_mode = m.self_test = m.objects_gate = m.job_outputs_gate = past
for name, call in (('report', lambda: m.report(tarch, troot)), ('gate', lambda: m.gate(tarch, troot))):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = call()
    assert rc == 1 and 'set outside the self-test' in out.getvalue(), (name, rc, out.getvalue()[-300:])
m._VERBATIM_OVERRIDE, m._IN_SELF_TEST = None, True
m.check = past
out = io.StringIO()
with contextlib.redirect_stdout(out):
    rc = m.report(tarch, troot)
assert rc == 1 and 'set outside the self-test' in out.getvalue(), 'the flag alone is not refused'
print('PROBE-OK')
"""

    def leaked():
        p = subprocess.run([sys.executable, '-I', '-c', probe, me, tarch, troot, json.dumps(t), eid], cwd=troot,
                           capture_output=True, text=True)
        return p.returncode == 0 and p.stdout.strip().endswith('PROBE-OK')
    expect('verbatim (seam): a substitute leaked into a fresh process is inert, and report and gate refuse it', go,
           undo, 'R13', 'not the owner-approved tuple', who=eid, also=leaked)
    # the seam opened during the check, as code R13 executes in-process (check_objects.py) could: report() refuses
    # after its check, gate() after its history-mode check
    probe2 = r"""
import io, json, sys, types, contextlib
me, tarch, troot, t = sys.argv[1], sys.argv[2], sys.argv[3], json.loads(sys.argv[4])
def fresh():
    m = types.ModuleType('check_retention_probe'); m.__file__ = me
    exec(compile(open(me, encoding='utf-8').read(), me, 'exec'), m.__dict__)
    return m
def opened(m):
    m._IN_SELF_TEST, m._VERBATIM_OVERRIDE = True, (t,)
m = fresh()
real = m.objects_rules
def evil():
    opened(m)
    return real()
m.objects_rules = evil
out = io.StringIO()
with contextlib.redirect_stdout(out):
    rc = m.report(tarch, troot)
assert rc == 1 and 'set outside the self-test' in out.getvalue() and 'RETENTION  HOLDS' not in out.getvalue(), \
    ('report', rc, out.getvalue()[-300:])
m = fresh()
hm = m.history_mode
def hm2(*a, **k):
    r = hm(*a, **k)
    opened(m)
    return r
m.history_mode = hm2
def after(*a, **k):
    raise SystemExit('gate ran past its history-mode check with the seam open')
m.self_test = m.objects_gate = m.job_outputs_gate = after
out = io.StringIO()
with contextlib.redirect_stdout(out):
    rc = m.gate(tarch, troot)
assert rc == 1 and 'set outside the self-test' in out.getvalue() and 'HOLDS' not in out.getvalue(), \
    ('gate', rc, out.getvalue()[-300:])
print('PROBE2-OK')
"""

    def opened_mid():
        p = subprocess.run([sys.executable, '-I', '-c', probe2, me, tarch, troot, json.dumps(t)], cwd=troot,
                           capture_output=True, text=True)
        return p.returncode == 0 and p.stdout.strip().endswith('PROBE2-OK')
    expect('verbatim (seam): a substitute opened during the check fails report and gate after it', go, undo, 'R13',
           'not the owner-approved tuple', who=eid, also=opened_mid)


# the R13 cases the self-test must run (its fixture makes them run in every lifecycle state)
R13_CASES = (
    'a research entry with neither citations nor a pending citation',
    'a research entry whose pending citation names no pull request',
    'a research entry that carries citations and a pending citation together',
    'a research entry whose id is not its run',
    'a research entry without results.json',
    'a research entry without run.json',
    'a research run.json that is not JSON',
    'a research result at another head commit',
    'a research result relabelled as a bridge result',
    'a research build that records a gate',
    'a research result from another job',
    'a research result whose source digest is not recorded',
    'a retained source commit also recorded as a gap',
    'a source commit neither retained nor a recorded gap',
    'a research run that a CI entry already retains',
    'a research run that a tracked file now cites',
    'a pending citation that names no round',
    'lifecycle (a): the intended record not in the tree, the entry pending',
    'lifecycle (b): the intended record lands citing the run and its head, the manifest unchanged (eligible)',
    'lifecycle (c): the entry maps the record\'s citing line (cited)',
    'lifecycle (c-partial): one entry mapped, the other on the same record still pending (eligible)',
    'lifecycle (c-full): every entry on the record mapped (cited)',
    'lifecycle (d): the intended record lands naming another head beside the run',
    'lifecycle (d): the intended record lands citing another run',
    'lifecycle (e): the record removed while the entry maps it',
    'the intended record lands citing the run without its head',
    'the intended record lands with the head mistyped after digit 10',
    'the intended record lands citing the run on another line than recorded',
    'the intended record lands, and another file also cites the run',
    'a mapped citation whose line names another head',
    'the record cites the run on two lines and the entry maps one',
    'a research run.json that names no head commit',
    'a research run.json that names no head commit leaves no citation state',
    'N1: an all-decimal 45-digit word beside the run\'s file name',
    'CN-3 d-far: a far line of the record cites the run beside another head',
    'CN-3 d-far-nohead: a far line of the record cites the run without its head',
    'CN-3: a duplicate free-standing citation with a conflicting full head',
    'CN-3: the run named inside an evidence file name with its digest (eligible)',
    'CN-3: the same, mapped to the citation alone (cited)',
    'CN-3: an embedded mention beside a different full head',
    'CN-3: the recorded line names the run only inside an identifier',
    'CN-3: a mapped line that names the run only inside an identifier',
    'CN-3: a citation mapped twice',
    'N1: another head in uppercase beside the run',
    'N2: the summary counts an eligible entry apart, never as cited',
    'boundary (a): a genuine 64-digit digest beside the citation and the file name passes',
    'boundary (b): a file name with a digest never establishes the citation',
    'boundary (b): a 64-digit hex word never states the head',
    'boundary (c): a conflicting head beside the citation fails, even beside a digest',
    'documented limitation: another head as the last 40 digits of a 64-digit word beside a file name passes')
# the real entry's lifecycle cases: the first set runs on a tree that holds the approved copy, the second on one that
# does not; the self-test requires one set, in full
LIVE_PRESENT_CASES = (
    'verbatim (live lifecycle): the real entry pending, its approved copy admitted',
    "verbatim (live lifecycle): the real entry eligible on its record's line alone",
    "verbatim (live lifecycle): the real entry cited on its record's line alone")
LIVE_ABSENT_CASES = (
    'verbatim (live lifecycle): this tree holds no approved copy, and no entry lists a verbatim mention',)
# the verbatim-mention cases the self-test must run
VERBATIM_CASES = (
    'verbatim (live): the hardcoded allowlist is exactly the one owner-approved tuple',
    'verbatim (live): the approved tuple listed without its copy fails closed',
    'verbatim (live): other bytes at the approved path fail',
    'verbatim (seam): only the self-test opens the seam, and nothing reads the environment',
    'verbatim (seam): the static scan fails a check_objects.py that reaches the seam',
    'verbatim (seam): no command-line flag reaches the substitute',
    'verbatim (seam): plain mode ignores the environment',
    'verbatim (seam): a substitute leaked into a fresh process is inert, and report and gate refuse it',
    'verbatim (seam): a substitute opened during the check fails report and gate after it',
    'verbatim: the approved mention of a pinned copy passes, and the entry stays pending',
    "verbatim: the record lands, and the entry is eligible on the record's line alone",
    "verbatim: promoted on the record's line alone, the entry is cited",
    'verbatim: the mention does not satisfy the pending citation (the record lands without citing the run)',
    "verbatim: the copy's line mapped as a citation",
    'verbatim: the copy named as the pending record',
    'verbatim: the copy changed by one byte, the manifest unchanged',
    "verbatim: the manifest asserts the changed copy's blob",
    'verbatim: the manifest asserts another sha256',
    'verbatim: SHA-1 matches and SHA-256 does not',
    'verbatim: SHA-256 matches and SHA-1 does not',
    'verbatim: the copy at another path, the manifest following it',
    'verbatim: the copy moved, the manifest unchanged',
    'verbatim: the copy absent',
    'verbatim: the line changed in the manifest',
    'verbatim: the mention moved to another line of the copy',
    'verbatim: the run named twice on the approved line',
    'verbatim: a second line of the copy names the run',
    'verbatim: another file also names the run',
    "verbatim: the approved run differs from the entry's run",
    "verbatim: the approved head differs from the run's head",
    'verbatim: the mention listed on another research entry',
    'verbatim: the pending record changed',
    'verbatim: the pending line changed',
    "verbatim: the pending citation's head changed",
    'verbatim: promoted on other record lines than approved',
    'verbatim: a tuple outside the hardcoded allowlist',
    'verbatim: the field on a CI entry',
    'verbatim: two mentions',
    'verbatim: the field is not a list',
    'verbatim: a claim annotation on the mention',
    'verbatim: an empty note',
    'verbatim: the source changed',
    'verbatim: another entry maps the copy at the approved line',
    'verbatim: another entry maps the copy at another line',
    'verbatim: another entry maps the copy under another path that resolves to it',
    "verbatim: a symbolic link at the copy's path",
    "verbatim: a symbolic link at the copy's path to an unscanned extension",
    "verbatim: a symbolic link at the copy's path into an unscanned directory",
    "verbatim: a directory symbolic link at a parent of the copy's path",
    'verbatim: the git index holds the copy as a regular file at the approved blob',
    'verbatim: the git index holds the copy as a symbolic link (mode 120000)',
    'verbatim: the git index holds the copy at another blob',
    "verbatim: the git index holds nothing at the copy's path",
    'verbatim: a float line',
    'verbatim: a bool line',
    'verbatim: the seam is unset after the verbatim cases',
)


R13_STAND_IN = 'verification/ZZ-SELF-TEST/r13-stand-in.md'


def r13_fixture(m, tarch, troot, need):
    """The self-test's R13 lifecycle fixture, from the copy's manifest m: every research-build entry pending on
    R13_STAND_IN (recorded line 3+3k, its run's head on the line before), its citations removed, and the copied
    files that only those citations needed removed from troot. Returns ((manifest, entry indices), None), or
    (None, the reason it cannot be built)."""
    idx = [k for k, e in enumerate(m['entries']) if re.fullmatch(r'research-[0-9]{1,20}', str(e.get('id'))) and
           e.get('kind') == 'derived']
    if len(idx) < 2:
        return None, 'it needs two research-build entries, and the manifest has %d' % len(idx)
    if os.path.lexists(os.path.join(troot, R13_STAND_IN)):
        return None, 'the stand-in record %s exists' % R13_STAND_IN
    for k, i in enumerate(idx):
        e = m['entries'][i]
        try:
            head = json.load(open(os.path.join(tarch, 'ci', str(e['run_id']), 'run.json'), encoding='utf-8'))['head_sha']
        except (OSError, ValueError, KeyError, TypeError):
            return None, '%s has no readable run.json head' % e.get('id')
        e.pop('citations', None)
        # a verbatim mention is bound to its real citation context; the fixture moves the entry off it, so the
        # mention and its copy leave the fixture (the verbatim cases build their own)
        e.pop('verbatim_mentions', None)
        e['awaiting_citation'] = {'pull_request': 1, 'round': 'R13-SELF-TEST', 'record': R13_STAND_IN,
                                  'line': 3 + 3 * k, 'head': head}
    still = {c['path'] for e in m['entries'] for c in e.get('citations', [])} | \
        {c['path'] for c in m['coverage']['files']}
    for rel in sorted(set(need) - still):
        os.remove(os.path.join(troot, rel))
    for i in idx:
        cl = citing_lines(troot, str(m['entries'][i]['run_id']), tarch)
        if cl:
            return None, 'run %s is still named at %s:%d, which another entry needs' % (
                (m['entries'][i]['run_id'],) + cl[0])
    return (m, idx), None


def self_test(archive, root):
    """The self-test, with the verbatim seam open only for its duration: _IN_SELF_TEST is set here, and the flag
    and any substitute are restored in a finally clause, whatever the self-test does. A seam already open when it
    starts fails it."""
    global _IN_SELF_TEST, _VERBATIM_OVERRIDE
    if verbatim_seam_leak():
        print('FAIL self: %s' % verbatim_seam_leak())
        print('self-test: FAILED')
        return 1
    _IN_SELF_TEST = True
    try:
        return _self_test(archive, root)
    finally:
        _IN_SELF_TEST, _VERBATIM_OVERRIDE = False, None


def _self_test(archive, root):
    """Each mutation must be reported by the check it targets, identified by that check's own message; the
    unmutated copy must pass. Every failure message of check() has a mutation here."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        troot = os.path.join(tmp, 'root')
        tarch = os.path.join(troot, 'archive')
        shutil.copytree(archive, tarch, ignore=shutil.ignore_patterns('__pycache__'))
        need = {c['path'] for e in man['entries'] for c in e.get('citations', [])} | \
            {c['path'] for c in man['coverage']['files']}
        # the copies a listed verbatim mention names, when the tree holds them (an absent copy fails the check)
        need |= {v.get('path') for e in man['entries'] if isinstance(e.get('verbatim_mentions'), list)
                 for v in e['verbatim_mentions'] if isinstance(v, dict) and inside(v.get('path'))
                 and os.path.isfile(os.path.join(root, v['path']))}
        for rel in need:
            dst = os.path.join(troot, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(os.path.join(root, rel), dst)
        mp = os.path.join(tarch, 'manifest.json')
        morig = open(mp, 'rb').read()

        ran = []

        def expect(name, mutate, restore, rule=None, msg='', state=None, states=(), also=None, who=None):
            """who: the entry the case is about; its failure must be that entry's (the message starts with the rule
            and its id), so another entry's failure never satisfies the case. A case whose own condition raises
            fails; it never stops the self-test."""
            nonlocal ok
            ran.append(name)
            mutate()
            fails, _ = check(tarch, troot)
            try:
                extra = also is None or bool(also())
            except Exception:
                extra = False
            restore()
            head_ = rule + ' ' + ('%s:' % who if who else '') if rule is not None else None
            good = (not fails) if rule is None else any(f.startswith(head_) and msg in f for f in fails)
            # (entry id, state) pairs: each entry's R13 citation state after the check
            for eid_, st_ in ([state] if state is not None else []) + list(states):
                got_ = R13_STATES.get(eid_, ('none',))[0]
                if got_ != st_:
                    good = False
                    fails = fails + ['R13 state of %s %s, not %s' % (eid_, got_, st_)]
            if not extra:
                good = False
                fails = fails + ['the case\'s own condition does not hold']
            ok &= good
            print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if rule is None else ' (%s)' % rule))
            if not good:
                print('      got: %s' % (fails[:3],))

        def edit(fn):
            def go():
                m = json.loads(morig)
                fn(m)
                open(mp, 'w', encoding='utf-8').write(json.dumps(m))
            return go
        back = lambda: open(mp, 'wb').write(morig)

        def file_edit(path, fn):
            orig = open(path, 'rb').read()
            return (lambda: open(path, 'wb').write(fn(orig))), (lambda: open(path, 'wb').write(orig))

        noop = lambda: None
        ents = man['entries']
        idx = lambda pred: next(i for i, e in enumerate(ents) if pred(e))
        has = lambda e, suffix: any(f['path'].endswith(suffix) for f in e.get('files', []))
        ci = idx(lambda e: str(e.get('id', '')).startswith('ci-') and has(e, '/jobs.json'))
        nojobs = idx(lambda e: str(e.get('id', '')).startswith('ci-') and not has(e, '/jobs.json'))
        cac = idx(lambda e: e.get('kind') == 'complete-as-cited' and len(e['citations']) == 1)
        bgr = idx(lambda e: any(f['path'].startswith('bg3/run-') for f in e['files']))
        cert = idx(lambda e: any(r.get('kind') == 'V2 certificate' for r in e.get('roles', [])))
        rec = idx(lambda e: any(r.get('kind') == 'receipt check-run' for r in e.get('roles', [])))
        e_ci = ents[ci]
        rid = e_ci['run_id']
        rsj = next(j for j, f in enumerate(e_ci['files']) if f['path'].endswith('/results.json'))
        runj = next(j for j, f in enumerate(e_ci['files']) if f['path'].endswith('/run.json'))
        xp = os.path.join(tarch, e_ci['files'][rsj]['path'])
        cp = os.path.join(troot, e_ci['citations'][0]['path'])
        ret = next((j, k) for j, c in enumerate(e_ci['citations']) for k, x in enumerate(c['claims'])
                   if x['status'] == 'retained')
        loaded = {e['id']: json.load(open(os.path.join(tarch, next(f['path'] for f in e['files'] if f['path'].endswith('/results.json')))))
                  for e in ents if str(e.get('id', '')).startswith('ci-')}
        part = next(e['id'] for e in ents if e['id'] in loaded and any(m['status'] == 'partial' for m in loaded[e['id']]['expected']['modules'].values()))
        pmod = next(m for m, x in loaded[part]['expected']['modules'].items() if x['status'] == 'partial')
        pp = os.path.join(tarch, 'ci', part.split('-', 1)[1], 'results.json')
        comp = next(e['id'] for e in ents if e['id'] in loaded and any(m['status'] == 'complete' and m['reports'] for m in loaded[e['id']]['expected']['modules'].values()))
        cmod = next(m for m, x in loaded[comp]['expected']['modules'].items() if x['status'] == 'complete' and x['reports'])
        cpth = os.path.join(tarch, 'ci', comp.split('-', 1)[1], 'results.json')
        X = lambda m: m['entries'][ci]['files'][rsj]
        C0 = lambda m: m['entries'][ci]['citations'][0]
        RC = lambda m: m['entries'][ci]['citations'][ret[0]]['claims'][ret[1]]

        def json_edit(path, fn):
            def change(b):
                d = json.loads(b)
                fn(d)
                return json.dumps(d).encode('utf-8')
            mutate, restore = file_edit(path, change)
            # a changed file must still pass R1, so its recorded size and digest follow it
            rel = os.path.relpath(path, tarch).replace(os.sep, '/')

            def go():
                mutate()
                m = json.loads(open(mp, 'rb').read())
                for e in m['entries']:
                    for f in e['files']:
                        if f['path'] == rel:
                            data = open(path, 'rb').read()
                            f['bytes'], f['sha256'] = len(data), hashlib.sha256(data).hexdigest()
                open(mp, 'w', encoding='utf-8').write(json.dumps(m))

            def undo():
                restore()
                back()
            return go, undo

        expect('unmutated copy passes', noop, noop)
        # manifest form (R7)
        expect('an unreadable manifest', *file_edit(mp, lambda b: b[:-2]), rule='R7', msg='manifest unreadable')
        expect('a manifest of another version', edit(lambda m: m.__setitem__('version', 1)), back, 'R7', 'schema or version')
        expect('a repeated entry id', edit(lambda m: m['entries'][nojobs].__setitem__('id', e_ci['id'])), back, 'R7',
               'missing or repeated')
        expect('an unknown entry kind', edit(lambda m: m['entries'][cac].__setitem__('kind', 'complete-ish')), back, 'R7',
               ': unknown kind')
        expect('a cited entry relabelled "complete"', edit(lambda m: m['entries'][cac].__setitem__('kind', 'complete')),
               back, 'R7', 'carries citations')
        expect('an entry with no files', edit(lambda m: m['entries'][cac].__setitem__('files', [])), back, 'R7', 'no files')
        expect('a listed path outside the archive', edit(lambda m: m['entries'][ci]['files'].append(
            {'path': '../x', 'bytes': 0, 'sha256': '', 'kind': 'derived'})), back, 'R7', 'not inside the archive')
        expect('a file of unknown kind', edit(lambda m: m['entries'][ci]['files'][runj].__setitem__('kind', 'derived-ish')),
               back, 'R7', 'has unknown kind')
        expect('a CI entry with no citations', edit(lambda m: m['entries'][ci].__setitem__('citations', [])), back, 'R7',
               'no citations')
        expect('a citation with no token', edit(lambda m: C0(m).__setitem__('tokens', [])), back, 'R7', 'carries no token')
        expect('a token too short to identify anything', edit(lambda m: C0(m)['tokens'].append('abc')), back, 'R7',
               'too short')
        expect('a citing location with no claim annotation', edit(lambda m: C0(m).pop('claims')), back, 'R7',
               'no claim annotation')
        expect('an unknown claim status', edit(lambda m: C0(m)['claims'][0].__setitem__('status', 'proved')), back, 'R7',
               'claim status')
        expect('a retained claim naming a file outside the entry', edit(lambda m: RC(m).__setitem__('in', ['bg3/none.log'])),
               back, 'R7', 'outside the entry')
        expect('a "differs" claim without a note', edit(lambda m: (RC(m).__setitem__('status', 'differs'), RC(m).pop('note', None))),
               back, 'R7', 'without a note')
        expect('a gap that names no entry', edit(lambda m: m['missing'].append({'id': 'nowhere', 'what': 'x', 'why': 'y'})),
               back, 'R7', 'names no entry')
        # files (R1, R2, R5, R6)
        expect('a flipped byte in an archived file', *file_edit(xp, lambda b: bytes([b[0] ^ 1]) + b[1:]), rule='R1',
               msg='sha256 differs')
        expect('a removed archived file', lambda: os.rename(xp, xp + '.x'), lambda: os.rename(xp + '.x', xp), 'R1', 'missing')
        expect('a recorded size that differs', edit(lambda m: X(m).__setitem__('bytes', X(m)['bytes'] + 1)), back, 'R1', 'size')
        expect('a complete-as-cited entry whose match flag is false',
               edit(lambda m: m['entries'][cac].__setitem__('matches_cited_digest', False)), back, 'R2', 'not byte-identical')

        def drop_digest(m):
            c = m['entries'][cac]['citations'][0]
            c['tokens'] = [t for t in c['tokens'] if t != m['entries'][cac]['cited_digest']] or [m['entries'][cac]['files'][0]['path']]
        expect('a complete-as-cited digest that no citation carries', edit(drop_digest), back, 'R2', 'not byte-identical')
        expect('a token pattern in an archived file', *file_edit(xp, lambda b: b + b'ghp_' + b'A' * 36 + b'\n'), rule='R5',
               msg='secret pattern')
        expect('an IPv4 address in an archived file', *file_edit(xp, lambda b: b + b'connect 10.1.2' + b'.3 refused\n'),
               rule='R5', msg='secret pattern')
        expect('an e-mail address in an archived file',
               *file_edit(xp, lambda b: b + b'author someone' + b'@' + b'example.org\n'), rule='R5', msg='secret pattern')
        expect('a secret pattern in the README',
               *file_edit(os.path.join(tarch, 'README.md'), lambda b: b + b'ghp_' + b'B' * 36 + b'\n'), rule='R5',
               msg='README.md')
        extra = os.path.join(tarch, 'ci', 'unlisted.txt')
        expect('an unlisted file in the archive', lambda: open(extra, 'w').write('x'), lambda: os.remove(extra), 'R6', 'unlisted')
        if os.path.isdir(os.path.join(tarch, 'objects')):
            def unpin(m):
                for e in m['entries']:
                    e['files'] = [f for f in e.get('files', []) if f['path'] != 'objects/manifest.json']
            expect('retained objects whose manifest is not a listed file', edit(unpin), back, 'R6', 'unlisted file objects/')
        # citing files (R3)
        expect('a changed historical record', *file_edit(cp, lambda b: b + b'\n'), rule='R3', msg='changed (blob')
        expect('a removed historical record', lambda: os.rename(cp, cp + '.x'), lambda: os.rename(cp + '.x', cp), 'R3',
               'citing file')
        expect('a recorded token absent from its line', edit(lambda m: C0(m)['tokens'].append('Z' * 12)), back, 'R3',
               'no longer contains')
        expect('a claim whose text is not on its line', edit(lambda m: C0(m)['claims'][0].__setitem__('text', 'Z' * 12)),
               back, 'R3', 'not verbatim')
        # expected results (R4)
        expect('a results.json that is not JSON', *json_edit(xp, lambda d: None) if False else file_edit(xp, lambda b: b[:-3]),
               rule='R4', msg='not JSON')
        expect('a results.json of another schema', *json_edit(xp, lambda d: d.__setitem__('schema', 'x')), rule='R4',
               msg='unknown schema')
        expect('a results.json naming no head commit', *json_edit(xp, lambda d: d['run'].__setitem__('head_sha', 'abc')),
               rule='R4', msg='names no run')
        expect('a results.json without a reproduction recipe', *json_edit(xp, lambda d: d['reproduce'].__setitem__('recipe', [])),
               rule='R4', msg='no reproduction recipe')
        expect('a results.json recording no successful build', *json_edit(xp, lambda d: d['expected'].__setitem__('build_success', False)),
               rule='R4', msg='no successful build')
        expect('a results.json without a gate verdict', *json_edit(xp, lambda d: d['expected']['gate'].__setitem__('verdict', None)),
               rule='R4', msg='no gate verdict')
        expect('a gate step of unknown status',
               *json_edit(xp, lambda d: d['expected']['gate']['steps'][0].__setitem__('status', 'OK')), rule='R4',
               msg='malformed gate steps')
        expect('a results.json without a module table', *json_edit(xp, lambda d: d['expected'].__setitem__('modules', [])),
               rule='R4', msg='no module table')
        expect('a module of unknown status',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod].__setitem__('status', 'maybe')), rule='R4',
               msg='has status')
        expect('a malformed report',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod]['reports'][0].__setitem__('axioms', 'propext')), rule='R4',
               msg='malformed report')
        expect('an absent module with reports',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod].__setitem__('status', 'absent')), rule='R4',
               msg='is absent but has')
        expect('a report outside the module\'s #print axioms lines',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod]['reports'][0].__setitem__('line', 10 ** 6)), rule='R4',
               msg='outside its #print axioms lines')
        expect('a partial module recorded as complete',
               *json_edit(pp, lambda d: d['expected']['modules'][pmod].__setitem__('status', 'complete')), rule='R4',
               msg='its lines give')
        expect('a results.json without a marker count',
               *json_edit(xp, lambda d: d['expected']['markers'].pop('sorryAx')), rule='R4', msg='no count for every marker')
        # entry files agree (R8)
        expect('a BG-3 entry whose provenance names another head commit',
               edit(lambda m: m['entries'][bgr]['provenance'].__setitem__('head_sha', '0' * 40)), back, 'R8',
               'differs from the entry\'s provenance')
        bgres = next(f['path'] for f in ents[bgr]['files'] if f['path'].startswith('bg3/results-'))
        expect('a BG-3 results file naming another job',
               *json_edit(os.path.join(tarch, bgres), lambda d: d['run'].__setitem__('job_id', '1')), rule='R8',
               msg='names another run, job')
        expect('a CI entry without run.json', edit(lambda m: m['entries'][ci]['files'].pop(runj)), back, 'R8', 'no run.json')
        expect('a results.json naming another head commit than run.json',
               *json_edit(xp, lambda d: d['run'].__setitem__('head_sha', '0' * 40)), rule='R8', msg='names another run, head commit')
        expect('a missing job list that is not a recorded gap', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == ents[nojobs]['id'] and g['what'] == 'job list')])), back, 'R8',
               'not a recorded gap')
        dres = next(f['path'] for e in ents for f in e['files'] if f['path'] == 'bg3/results-116831668411.json')
        expect('a design-log result recording no checks',
               *json_edit(os.path.join(tarch, dres), lambda d: d['expected'].__setitem__('checks', [])), rule='R4',
               msg='records no checks or no recipe')
        rjp = os.path.join(tarch, 'ci', rid, 'run.json')
        expect('a run.json that is not JSON', *file_edit(rjp, lambda b: b[:-3]), rule='R8', msg='run.json or results.json is not JSON')
        jp = os.path.join(tarch, 'ci', rid, 'jobs.json')
        expect('a jobs.json that is not a job list', *json_edit(jp, lambda d: d.pop('jobs')), rule='R8', msg='not a job list')
        expect('a job at another head commit',
               *json_edit(jp, lambda d: d['jobs'][0].__setitem__('head_sha', '0' * 40)), rule='R8', msg='head_sha differs')
        expect('results from another job', *json_edit(xp, lambda d: d['run'].__setitem__('job_id', '1')), rule='R8',
               msg='not from attempt')

        def relabel(d):
            d['kind'] = 'design-diagnostic'
            d['expected']['sha256sum_ok'] = True
            d['expected']['checks'] = ['a relabelled bridge result']
        expect('a CI entry\'s results.json relabelled as a design diagnostic, its size and digest following it',
               *json_edit(xp, relabel), rule='R8', msg='is of kind')
        expect('a partial module whose gap record is removed', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == part and g['what'] == 'axiom reports of %s' % pmod)])),
               back, 'R8', 'its gap record is absent')
        # coverage (R9)
        cited = next(c['path'] for c in man['coverage']['files']
                     if any(x['path'] == c['path'] for e in ents for x in e.get('citations', [])))
        expect('a cited receipt dropped from the coverage list', edit(lambda m: m['coverage'].__setitem__(
            'files', [c for c in m['coverage']['files'] if c['path'] != cited])), back, 'R9', 'not in the coverage list')
        newr = os.path.join(troot, 'verification', 'receipts', 'ZZ-LATER.json')
        expect('a receipt in the tree that is neither covered nor named as later',
               lambda: open(newr, 'w').write('{}'), lambda: os.remove(newr), 'R9', 'neither covered')
        expect('a receipt named as later than this tranche passes',
               lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage'].__setitem__(
                   'later', [{'path': 'verification/receipts/ZZ-LATER.json', 'evidence': 'its own record directory'}]))()),
               lambda: (os.remove(newr), back()))
        expect('a cited, covered receipt moved to coverage.later', edit(lambda m: (
            m['coverage'].__setitem__('files', [c for c in m['coverage']['files'] if c['path'] != cited]),
            m['coverage'].__setitem__('later', [{'path': cited, 'evidence': 'x'}]))), back, 'R9', 'the tranche cites it')
        expect('a receipt named both as covered and as later', edit(lambda m: m['coverage'].__setitem__(
            'later', [{'path': cited, 'evidence': 'x'}])), back, 'R9', 'both as covered and as later')
        expect('a later receipt without where its evidence is retained',
               lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage'].__setitem__(
                   'later', [{'path': 'verification/receipts/ZZ-LATER.json'}]))()),
               lambda: (os.remove(newr), back()), 'R9', 'without where its evidence')
        # R10 reads the real repository's history, read-only
        import subprocess
        hist = subprocess.run(['git', '-C', root, 'cat-file', '-e', man['base'] + '^{commit}'], capture_output=True).returncode == 0
        if not hist:
            ok = False
            print('FAIL self: the R10 cases need the tranche base in this repository\'s history')
        else:
            def r10(name, fails, msg=None):
                nonlocal ok
                good = (not fails) if msg is None else any(f.startswith('R10 ') and msg in f for f in fails)
                ok &= good
                print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R10)'))
            r10('a receipt that did not exist at the base passes R10',
                later_provenance(man, root, [{'path': 'verification/receipts/ZZ-LATER.json'}]))
            r10('a frozen-tranche receipt named as later fails R10', later_provenance(man, root, [{'path': cited}]),
                'existed at the tranche base')
            r10('a tranche base absent from the repository fails R10',
                later_provenance(dict(man, base='0' * 40), root, []), 'not in the repository')
            r10('a HEAD that does not descend from the base fails R10',
                later_provenance(man, root, [], head=man['base'] + '^'), 'not an ancestor')
            scope, sf = base_scope(man, root)
            r10('the base scope is read from git', sf)
            r10('a tranche base absent from the repository has no scope', base_scope(dict(man, base='0' * 40), root)[1],
                'not in the repository')
            hist_check = lambda: check(tarch, troot, scope)[0]
            for name, mut, res, msg in (
                    ('history mode passes on the unmutated copy', noop, noop, None),
                    ('a base receipt dropped from coverage, in history mode',
                     edit(lambda m: m['coverage'].__setitem__('files', [c for c in m['coverage']['files'] if c['path'] != cited])),
                     back, 'existed at the tranche base but is not covered'),
                    ('a covered file that did not exist at the base, in history mode',
                     lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage']['files'].append(
                         {'path': 'verification/receipts/ZZ-LATER.json', 'blob': blob_id(b'{}')}))()),
                     lambda: (os.remove(newr), back()), 'did not exist at the tranche base'),
                    ('a receipt landed after the base needs no declaration in history mode',
                     lambda: open(newr, 'w').write('{}'), lambda: os.remove(newr), None)):
                mut()
                fails = hist_check()
                res()
                good = (not fails) if msg is None else any(f.startswith('R10 ') and msg in f for f in fails)
                ok &= good
                print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R10)'))
                if not good:
                    print('      got: %s' % (fails[:3],))
            # R11 reads the real repository's history through show(); a case replaces some reads, the base scope or
            # the ancestry test, or edits a copied expected result or the manifest, and requires that site's own
            # message
            real = git_show(root)
            base = man['base']
            have = lambda c: c is not None and subprocess.run(['git', '-C', root, 'cat-file', '-e', str(c) + '^{commit}'],
                                                              capture_output=True).returncode == 0

            def res_edit(path, fn):
                def change(b):
                    d = json.loads(b)
                    fn(d)
                    return json.dumps(d).encode('utf-8')
                return file_edit(path, change)

            def attestation_of(run):
                for c in man['coverage']['files']:
                    d = json.loads(real(base, c['path']))
                    for a in d.get('attestations', []):
                        mm = RUN_URL.search(a.get('record', ''))
                        if a.get('kind') == 'check-run' and mm and mm.group(1) == run:
                            return c['path'], d, a['commit']
                    for v in (d.get('ci') or {}).values():
                        if isinstance(v, dict) and str(v.get('run')) == run:
                            return c['path'], d, v['head_sha']

            def block_edit(text, fn):
                ls = text.decode('utf-8').split('\n')
                i = ls.index('```v3-governed-paths')
                j = ls.index('```', i + 1)
                return '\n'.join(ls[:i + 1] + fn(ls[i + 1:j]) + ls[j:]).encode('utf-8')

            crun = comp.split('-', 1)[1]
            ccert = ents[cert]
            cres = os.path.join(tarch, 'ci', ccert['run_id'], 'results.json')
            att, catt = attestation_of(crun), attestation_of(ccert['run_id'])
            rpath, rdoc, rcommit = att or (None, {}, None)
            cpath_, cdoc, ccommit = catt or (None, {}, None)
            pre = next((b['path'] for b in rdoc.get('control_plane_blobs', []) if b['path'].endswith('/preregistration.md')),
                       None)
            certp = 'verification/certificates/%s.json' % cdoc.get('round')

            def results_of(e):
                out = []
                for f in e['files']:
                    rel = f['path']
                    if rel.endswith('/results.json') or (rel.startswith('bg3/results-') and rel.endswith('.json')):
                        try:
                            d = json.load(open(os.path.join(tarch, rel), encoding='utf-8'))
                        except (OSError, ValueError):
                            continue
                        if isinstance(d, dict):
                            out.append((rel, d))
                return out
            run_of = lambda d: str((d.get('run') or {}).get('id'))
            cis = [e for e in ents if str(e.get('id', '')).startswith('ci-')]
            nonci = [(p, d) for e in ents if not str(e.get('id', '')).startswith('ci-') for p, d in results_of(e)]
            bg_runs = {run_of(d) for p, d in nonci if d.get('kind') == 'bridge'}
            # the relabel attack of a run with a second bridge result, so that only the kind rule can catch it
            relab = next((e for e in cis if e['run_id'] in bg_runs), cis[0] if cis else None)
            relp = next((os.path.join(tarch, f['path']) for f in (relab or {}).get('files', [])
                         if f['path'].endswith('/results.json')), None)
            only = next((e for e in cis if e['run_id'] not in bg_runs), None)
            other = next((p for p, d in nonci if d.get('kind') == 'bridge'), None)
            # a bridge result outside the CI entries whose run an attestation names (BG-3's E tail)
            atto = next((p for p, d in nonci if d.get('kind') == 'bridge' and run_of(d) in {e['run_id'] for e in cis}), None)
            otherp = other and os.path.join(tarch, other)
            nonbridge = {p for p, d in nonci if d.get('kind') != 'bridge'}
            lack = [what for what, v in (('a CI entry with a results.json', relp), ('a CI run with no other result', only),
                                         ('a bridge result outside the CI entries', other),
                                         ('such a result of an attested run', atto)) if v is None]
            if lack:
                ok = False
                print('FAIL self: the R11 cases need, in the archive, %s' % '; '.join(lack))
            elif not (pre and have(rcommit) and have(ccommit)) or real(rcommit, pre) is None or real(ccommit, certp) is None:
                ok = False
                print('FAIL self: the R11 cases need the commits %s and %s, which their attestations name, in this '
                      'repository\'s history' % (str(rcommit)[:12], str(ccommit)[:12]))
            else:
                ptext = real(rcommit, pre)

                def r11(name, msg=None, mutate=noop, restore=noop, over=None, m=None, also=None, sc=None, on_main=None,
                        fresh=False):
                    nonlocal ok
                    o = over() if over else {}
                    mutate()
                    try:
                        fails, st = module_sets(tarch, root, man if m is None else m,
                                                lambda rev, path: o[(rev, path)] if (rev, path) in o else real(rev, path),
                                                on_main, None if fresh else (scope if sc is None else sc))
                    finally:
                        restore()
                    good = (not fails) if msg is None else any(f.startswith('R11 ') and msg in f for f in fails)
                    if also is not None:
                        good = good and also(st)
                    ok &= good
                    print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R11)'))
                    if not good:
                        print('      got: %s' % (fails[:3],))

                def pinned(text, digest=False):
                    """The receipt and the preregistration at the run's commit, with the receipt's pin following the text."""
                    d = json.loads(json.dumps(rdoc))
                    for b in d['control_plane_blobs']:
                        if b['path'] == pre:
                            b['blob'] = blob_id(text)
                    if digest:
                        texts = [(text if b['path'] == pre else real(rcommit, b['path'])).decode('utf-8')
                                 for b in d['control_plane_blobs']]
                        d['governed_paths_digest'] = governed_digest(governed_entries(texts))
                    return {(rcommit, pre): text, (base, rpath): json.dumps(d).encode('utf-8')}


                def unattested_on_main(d):
                    d['run']['id'], d['run']['head_sha'] = '1', base

                def drop_only(mm):
                    mm = json.loads(json.dumps(mm))
                    for e in mm['entries']:
                        if e['id'] == only['id']:
                            e['files'] = [f for f in e['files'] if not f['path'].endswith('/results.json')]
                    return mm
                # a second round attesting the run of cpth at the same commit, governing one more module
                fpath, fpre, fmod = 'verification/receipts/ZZ-FORGED.json', 'verification/ZZ-FORGED/preregistration.md', \
                    'OIBridge/ZZForged.lean'
                ftext = ('```v3-governed-paths\nexecution AM %s%s\n```\n' % (LEAN_ROOT, fmod)).encode('utf-8')
                fdoc = {'round': 'ZZ-FORGED', 'control_plane_blobs': [{'path': fpre, 'blob': blob_id(ftext)}],
                        'governed_paths_digest': governed_digest(governed_entries([ftext.decode('utf-8')])),
                        'attestations': [{'kind': 'check-run', 'subject': 'E', 'commit': rcommit,
                                          'record': 'https://github.com/owner/repo/actions/runs/%s' % crun}]}
                forged = lambda: {(base, fpath): json.dumps(fdoc).encode('utf-8'), (rcommit, fpre): ftext}
                absent = {'status': 'absent', 'reports': [], 'prints': None, 'print_lines': None}

                r11('R11 passes on the unmutated copy, checks every CI entry\'s expected result, and lists every other '
                    'result outside its scope with a reason',
                    also=lambda st: st['checked'] >= len(cis) and st['runs'] > 0 and st['modules'] > 0 and
                    all((not u[0].startswith('ci/') or "'research-build'" in u[1]) and u[1] for u in st['unscoped']) and
                    nonbridge <= {u[0] for u in st['unscoped']})
                r11('a control plane altered only at the tranche base leaves R11 unchanged: it reads the run\'s commit',
                    over=lambda: {(base, pre): b'altered at the base'})
                r11('a tranche base absent from the repository', 'is not in the repository, so no attestation',
                    m=dict(man, base='0' * 40), fresh=True)
                r11('an attestation at the tranche base that cannot be read', 'cannot be read at the tranche base',
                    sc=scope | {'verification/receipts/ZZ-NONE.json'})
                r11('an expected result that cannot be read', 'is not a readable expected result',
                    *file_edit(cpth, lambda b: b[:-3]))
                r11('a CI entry\'s expected result relabelled as a design diagnostic', 'not a Mathlib bridge result',
                    *res_edit(relp, relabel))
                r11('an attested run\'s result outside the CI entries relabelled as a design diagnostic',
                    'but an attestation at the tranche base names its run', *res_edit(os.path.join(tarch, atto), relabel))
                r11('a CI entry\'s expected result of a run no attestation at the base names', 'so no round governs its modules',
                    *res_edit(cpth, lambda d: d['run'].__setitem__('id', '1')))
                r11('another expected result of a run no attestation names, at a commit on main', 'is on main there',
                    *res_edit(otherp, unattested_on_main))
                r11('the same result, at a commit off main, is listed outside the scope', None,
                    *res_edit(otherp, unattested_on_main), on_main=lambda c: False,
                    also=lambda st: other in {u[0] for u in st['unscoped']})
                r11('the same result, at a commit this repository cannot place', 'cannot decide whether',
                    *res_edit(otherp, unattested_on_main), on_main=lambda c: None)
                r11('a required run whose only expected result is dropped from its entry',
                    'are not the runs attested at the tranche base', m=drop_only(man))
                r11('an expected result at another commit than its attestation', 'the expected result holds at',
                    *res_edit(cpth, lambda d: d['run'].__setitem__('head_sha', '0' * 40)))
                r11('a control-plane file that is not at its receipt\'s blob at the run\'s commit',
                    'is not at its receipt\'s blob', over=lambda: {(rcommit, pre): ptext + b'\n'})
                r11('a control plane without a well-formed governed-paths block, its pin following it',
                    'no single well-formed v3-governed-paths block',
                    over=lambda: pinned(ptext.replace(b'\n```v3-governed-paths\n', b'\n```v3-governed-pathz\n', 1)))
                r11('governed paths that do not hash to the receipt\'s digest, the pin following them',
                    'do not hash to its receipt\'s governed_paths_digest',
                    over=lambda: pinned(block_edit(ptext, lambda body: [x for x in body if not x.endswith('.lean')])))
                r11('governed paths naming a directory of Lean modules, pin and digest following them', 'name the directory',
                    over=lambda: pinned(block_edit(ptext, lambda body: body + ['execution M ' + LEAN_ROOT + 'OIBridge/']), True))
                r11('a certificate that is not at the blob its attestation pins', 'is not the certificate its attestation pins',
                    over=lambda: {(ccommit, certp): real(ccommit, certp) + b' '})
                r11('a module table missing a governed module', 'differs from the Lean modules',
                    *res_edit(cpth, lambda d: d['expected']['modules'].pop(cmod)))
                r11('a module table with a module the round does not govern', 'differs from the Lean modules',
                    *res_edit(cpth, lambda d: d['expected']['modules'].__setitem__('OIBridge/NotGoverned.lean', dict(absent))))
                r11('a certificate run\'s module table with a module its certificate does not contribute',
                    'differs from the Lean modules', *res_edit(cres, lambda d: d['expected']['modules'].__setitem__(
                        'OIBridge/NotGoverned.lean', dict(absent))))
                r11('a second round attesting a run: a module table without that round\'s module fails',
                    'missing [%r]' % fmod, over=forged, sc=scope | {fpath})
                r11('a second round attesting a run: a module table equal to the union of both rounds\' modules passes', None,
                    *res_edit(cpth, lambda d: d['expected']['modules'].__setitem__(fmod, dict(absent))), over=forged,
                    sc=scope | {fpath})
                r11('a manifest with no expected result to check', 'no expected result was checked', m=dict(man, entries=[]))
                # the relabel attack end to end: the classification, size and digest change together; R8 rejects it
                # from the tree, R11 from history, and nothing else fails
                mut, und = json_edit(relp, relabel)
                mut()
                try:
                    hf = history_mode(tarch, root, json.load(open(mp, encoding='utf-8')), tree=troot)[0]
                finally:
                    und()
                good = any(f.startswith('R11 ') and 'not a Mathlib bridge result' in f for f in hf) and \
                    any(f.startswith('R8 ') and 'is of kind' in f for f in hf) and all(f.startswith(('R8 ', 'R11 ')) for f in hf)
                ok &= good
                print('%s self: the relabel with its recorded size and digest following it fails R8 and R11 in history '
                      'mode, and nothing else (R8, R11)' % ('PASS' if good else 'FAIL'))
                if not good:
                    print('      got: %s' % (hf[:3],))
        expect('a manifest that names no coverage files', edit(lambda m: m['coverage'].__setitem__('files', [])), back, 'R9',
               'no coverage files')
        expect('a coverage file whose blob changed',
               *file_edit(os.path.join(troot, man['coverage']['files'][0]['path']), lambda b: b + b' '), rule='R9',
               msg='missing or changed')

        def drop(i):
            def go(m):
                eid = m['entries'][i]['id']
                m['entries'].pop(i)
                m['missing'] = [g for g in m['missing'] if g.get('id') != eid]
            return go
        expect('an attested check run with no entry', edit(drop(rec)), back, 'R9', 'has no entry')
        rp = os.path.join(tarch, 'ci', ents[rec]['run_id'], 'run.json')
        expect('an attested run whose metadata names another head',
               *json_edit(rp, lambda d: d.__setitem__('head_sha', '0' * 40)), rule='R9', msg='attested')
        expect('an entry that does not record its attested role', edit(lambda m: m['entries'][rec].__setitem__(
            'roles', [r for r in m['entries'][rec]['roles'] if r.get('kind') != 'receipt check-run'])), back, 'R9',
               'does not record this role')
        expect('a certificate run with no entry', edit(drop(cert)), back, 'R9', 'no matching entry')
        # tranche 3 (R12)
        t3 = [i for i, e in enumerate(ents) if str(e.get('id', '')).startswith('run-')]
        if 'tranche3' in man or t3:
            r12_cases(man, ents, t3, tarch, expect, edit, back, json_edit, file_edit)
        # R13's verbatim mentions: the live tuple, before the fixture moves any entry off its citation context
        verbatim_live_cases(ents, troot, tarch, root, expect, edit, back)
        # R13's lifecycle, on a fixture built in the copy so that its cases run in every live state (pending,
        # eligible, partly or fully cited): every research-build entry pending on a stand-in record that no tree
        # holds, and the copied records that only their citations needed removed. A fixture that cannot be built,
        # or a named case that does not run, fails the self-test; neither is ever a skip.
        fx, why = r13_fixture(json.loads(morig), tarch, troot, need)
        if fx is None:
            ok = False
            print('FAIL self: the R13 lifecycle fixture cannot be built: %s' % why)
        else:
            morig = json.dumps(fx[0]).encode('utf-8')
            back()
            r13_cases(fx[0], fx[0]['entries'], fx[1], troot, tarch, expect, edit, back, json_edit, file_edit)
        missing = [n for n in R13_CASES + VERBATIM_CASES if n not in ran]
        for n in missing:
            ok = False
            print('FAIL self: %s (R13) did not run' % n)
        if not (all(n in ran for n in LIVE_PRESENT_CASES) or all(n in ran for n in LIVE_ABSENT_CASES)):
            ok = False
            print('FAIL self: neither set of the real entry\'s lifecycle cases ran in full')
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    root = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test(HERE, root))
    if sys.argv[1:] == ['--gate']:
        sys.exit(gate(HERE, root))
    if sys.argv[1:] == ['--module-sets']:
        sys.exit(module_report(HERE, root))
    if sys.argv[1:] == ['--later-provenance']:
        man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
        fails = later_provenance(man, root)
        for f in fails:
            print('FAIL  %s' % f)
        print('LATER-PROVENANCE  %s (%d path(s) named as later, %d failure(s))' % (
            'HOLDS' if not fails else 'FAILS', len(man.get('coverage', {}).get('later', [])), len(fails)))
        sys.exit(1 if fails else 0)
    if sys.argv[1:]:
        print(__doc__)
        sys.exit(2)
    sys.exit(report(HERE, root))

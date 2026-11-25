#!/usr/bin/env python3
"""Landing-package preparation of design r6, round 5: the owner decision of 2026-11-25T18:50:53Z (item 2).

Reads, read only: out-final5/ (the round-4 outputs, byte-identical to the directory
verification/audits/foundations/a1exit-design-r6-20261125/ at commit 2aec244e, with generator-round4 as
out-final5/build/), the layout generator-round4 itself reads (out-final4/ and c33/), and build/inputs/ beside this
file (the directory's tree at 2aec244e as read with a GET request, #1169 comments 7170390944 and 7171541574 as read
with GET requests, and P's edits_check.py as a byte copy of git blob 1153e039).  Every file read from out-final5/ is
checked against its git blob id at 2aec244e.  generator-round4 is executed in-process up to its report (it re-checks
its own inputs and regenerates the round-4 outputs, which must equal out-final5/), so that its round-3 and round-4
self-checks run on the round-4 outputs ("before") and on the round-5 outputs ("after").  Writes out-final6/.  Every
change is a logged edit tagged with the item of the decision it applies (D1: edits_check.py; D2: the generators;
D3: the historical statements), NIT2-NIT5 (round-4 delta review nits), NIT1 (the C-4 sentence) or `meta`.  The
generator re-runs itself in a separate process and compares every output's sha256 before writing.
"""
import collections
import hashlib
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
R6 = os.path.dirname(OUT)
IN5 = os.path.join(R6, 'out-final5')
G4 = os.path.join(IN5, 'build')
INP = os.path.join(HERE, 'inputs')
DIRPATH = 'verification/audits/foundations/a1exit-design-r6-20261125'
R4_COMMIT = '2aec244e283fc49a85af04f2d9c3a72ec4122340'
C33_COMMIT = 'c33d5b71a3e4e15028d19ff153afcee8f5aa90a3'
MAIN_AT = '4c3ad0796b578c6258d5aae58c9502d5155d74dc'
TOOL = 'a37992449b452021001277c06c524a30c92dfb87'
T1P = '14ac71b4b0a0c0aa2d7068d6799a73f474097060'
P_COMMIT = '4c79be642ca631573f06b444903be75ec4f5e2b6'
EC_BLOB = '1153e039d7223742de56a54ed201e8358324c742'
EC_SHA = '2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c'
EC_PATH = 'inputs/edits_check.py'
EC_SRC = 'verification/audits/foundations/a1exit-deletion-20261121/edits_check.py'
DEC5_ID, REV5_ID = '7171541574', '7170390944'
DEC5_AT = '2026-11-25T18:50:53Z'
OD5 = 'owner decision of %s' % DEC5_AT
REQ12 = ['R6.SPLIT.3', 'R6.PROF.3', 'R6.PROF.4', 'R6.PROF.5', 'R6.PROF.7', 'R6.PROF.8', 'R6.PROF.9', 'R6.PROF.10',
         'R6.PROF.12', 'R6.DENY.5', 'R6.A1CFG.2', 'OBL-1']


def rdb(p):
    with open(p, 'rb') as f:
        return f.read()


def rd(p):
    return rdb(p).decode('utf-8')


def sha(b):
    if isinstance(b, str):
        b = b.encode('utf-8')
    return hashlib.sha256(b).hexdigest()


def gitblob(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def rj(s):
    return json.loads(s, object_pairs_hook=collections.OrderedDict)


PROBLEMS = []
LOG = []


def log(dec, target, desc):
    LOG.append((dec, target, desc))


# =====================================================================================================
# inputs
# =====================================================================================================
TREE5 = rj(rd(os.path.join(INP, 'tree-2aec244e.json')))
BLOB5 = collections.OrderedDict((f['path'], f['blob']) for f in TREE5['files'])
REC5 = rj(rd(os.path.join(INP, 'records-1169-round5.json')))
EC = rdb(os.path.join(INP, 'edits_check.py'))
INPUT5 = collections.OrderedDict((n, sha(rdb(os.path.join(INP, n)))) for n in
                                 ('tree-2aec244e.json', 'records-1169-round5.json', 'edits_check.py'))
R4OUT = ['DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json', 'PARAPHRASED-DECISIONS.md', 'AUTHORIZATIONS.md',
         'FRESH-AUTHORIZATION.md', 'REVIEW-r6-round3.md', 'LANDING-MANIFEST.md', 'MIGRATION.json', 'V4-COMPARISON.md',
         'REVIEW-r6-round2.md', 'CORRECTION-REPORT-round4.md']
G4FILES = collections.OrderedDict([
    ('generator-round4/correct4.py', os.path.join(G4, 'correct4.py')),
    ('generator-round4/owner-decisions-A1-A5.json', os.path.join(G4, 'inputs', 'owner-decisions-A1-A5.json')),
    ('generator-round4/review-r6-round3.md', os.path.join(G4, 'inputs', 'review-r6-round3.md')),
    ('generator-round4/tree-c33d5b71.json', os.path.join(G4, 'inputs', 'tree-c33d5b71.json')),
    ('generator-round4/records-1169.json', os.path.join(G4, 'inputs', 'records-1169.json'))])
R4 = collections.OrderedDict()
for p in R4OUT:
    R4[p] = rdb(os.path.join(IN5, p))
    if gitblob(R4[p]) != BLOB5.get(p):
        PROBLEMS.append('input %s does not match its git blob at 2aec244e' % p)
for p, lp in G4FILES.items():
    if gitblob(rdb(lp)) != BLOB5.get(p):
        PROBLEMS.append('input %s does not match its git blob at 2aec244e' % p)
if len(BLOB5) != 45 or TREE5['commit'] != R4_COMMIT:
    PROBLEMS.append('tree listing: %d files at %s, expected 45 at 2aec244e' % (len(BLOB5), TREE5['commit']))
if gitblob(EC) != EC_BLOB or sha(EC) != EC_SHA:
    PROBLEMS.append('edits_check.py: git blob %s, sha256 %s' % (gitblob(EC), sha(EC)))
for cid in (DEC5_ID, REV5_ID):
    if REC5[cid]['user']['login'] != 'amaybaum':
        PROBLEMS.append('records: unexpected author of comment ' + cid)
DEC5_BODY, REV5_BODY = REC5[DEC5_ID]['body'], REC5[REV5_ID]['body']
DEC5_REC_AT, REV5_REC_AT = REC5[DEC5_ID]['created_at'], REC5[REV5_ID]['created_at']
if 'Owner decision (amaybaum, %s, coordinating session), quoted in full:' % DEC5_AT not in DEC5_BODY:
    PROBLEMS.append('decision record: author and time line missing')
_qa = DEC5_BODY.index('> Authorized as described')
_qb = DEC5_BODY.index('\n>\n> ### 3\\.')
_qg = DEC5_BODY.index('> These are explicit authorizations')
_qc = DEC5_BODY.index('> ### General constraints')
DEC5_QUOTE = DEC5_BODY[_qa:_qb] + '\n>\n' + DEC5_BODY[_qc:DEC5_BODY.index('\n', _qg)]
for line in ('> * Include `edits_check.py` and the round-4 generator in the proposed landing package.',
             '> * Preserve all 12 verification requirements without weakening them.',
             '> * Narrow the historical statements to what the evidence on `main` establishes and explicitly identify unsupported statements.',
             '> * Regenerate the documents and complete one focused independent review.',
             '> Preparation is authorized. Design adoption and merging into `main` still require separate approval.'):
    if line not in DEC5_QUOTE:
        PROBLEMS.append('decision quote: line missing: %r' % line[:60])
_ra = REV5_BODY.index('---- reviewer text begins ----') + len('---- reviewer text begins ----')
REV5_TEXT = REV5_BODY[_ra:REV5_BODY.index('---- reviewer text ends ----')].strip() + '\n'
_rsha = re.search(r'SHA-256 of the unredacted review text: `([0-9a-f]{64})`', REV5_BODY)
if not _rsha or _rsha.group(1) != sha(REV5_TEXT):
    PROBLEMS.append('round-4 delta review: sha256 of the reviewer text differs from the one the record states')
for nit in ('3. **The manifest lists three comment ids that do not exist.**', '5. **One id is classified as a reference when',
            '4. **The note that correct4.py carries only the listed references is slightly wrong.**',
            '2. **The A3 quotation joins five of the record\'s paragraphs into one.**', '1. **TR45-opC has no runner'):
    if nit not in REV5_TEXT:
        PROBLEMS.append('round-4 delta review: nit missing: ' + nit[:40])

# =====================================================================================================
# generator-round4, executed in-process up to its report
# =====================================================================================================
SRC4 = rd(G4FILES['generator-round4/correct4.py'])
_cut_c = SRC4.index('\n# =====================================================================================================\n'
                    '# self-checks\n')
_cut_r = SRC4.index('\ndef report():')
NS4 = {'__file__': G4FILES['generator-round4/correct4.py'], '__name__': 'correct4', '__builtins__': __builtins__}
exec(compile(SRC4[:_cut_r], 'correct4', 'exec'), NS4)
for p in NS4['PROBLEMS']:
    PROBLEMS.append('generator-round4: ' + p)
for n, c in NS4['CONTENT'].items():
    if c.encode('utf-8') != R4[n]:
        PROBLEMS.append('generator-round4 does not reproduce %s of 2aec244e' % n)
C4_REPRO = len(NS4['CONTENT'])
SEG_CHECKS = SRC4[_cut_c:SRC4.index('\n# =====================================================================================================\n'
                                    '# CORRECTION-REPORT-round4.md')]
CHK_BEFORE, VAL_BEFORE = NS4['CHK_AFTER'], NS4['VAL_AFTER']
OWN_BEFORE = NS4['OWN']
parse_reqs, bq, run_checks = NS4['parse_reqs'], NS4['bq'], NS4['run_checks']
block_span4 = NS4['NS']['block_span']
md_table = NS4['md_table']

T_IN = R4['DESIGN-r6.md'].decode('utf-8')
T = T_IN
AUTH = R4['AUTHORIZATIONS.md'].decode('utf-8')
FRESH = R4['FRESH-AUTHORIZATION.md'].decode('utf-8')


def edit(dec, target, old, new, count=1):
    global T
    n = T.count(old)
    if n != count:
        PROBLEMS.append('edit %s/%s: expected %d occurrence(s), found %d: %r' % (dec, target, count, n, old[:90]))
        return
    T = T.replace(old, new)
    log(dec, target, 'text edit')


def bedit(dec, rid, old, new, desc='text edit'):
    global T
    a, b = block_span4(rid, T)
    blk = T[a:b]
    if blk.count(old) != 1:
        PROBLEMS.append('bedit %s/%s: %d occurrences of %r' % (dec, rid, blk.count(old), old[:90]))
        return
    T = T[:a] + blk.replace(old, new) + T[b:]
    log(dec, rid, desc)


# =====================================================================================================
# historical statements (D3): the passages of the round-4 design found by the scan, each listed or excluded
# =====================================================================================================
HPAT = re.compile(r"tool commit|\btoday\b|a3799244|45569710442|T1'|14ac71b4|9f4fc3e8|ba37c1cd|ec384fdf|59b68984|2055e68f|"
                  r"528f146d|[Tt]he implementation|[Ss]urvivor|CI run|at drafting")


def units(text):
    out, cur, sec, buf, para = [], None, '', [], 0

    def flush():
        if buf:
            out.append((cur, '\n'.join(buf)))
        del buf[:]
    for ln in text.split('\n'):
        m = re.match(r'\*\*(R6\.[A-Z0-9]+\.\d+|OBL-\d+)\*\*', ln)
        h = re.match(r'#{2,4} (\S+)', ln)
        hist = re.match(r'- (HIST-\d+)\.', ln)
        inblk = (cur or '').startswith(('R6.', 'OBL-'))
        if m:
            flush(); cur = m.group(1); buf.append(ln); continue
        if h:
            flush(); sec = h.group(1).rstrip('.'); cur = 'sec. %s' % sec; para = 0; continue
        if hist:
            flush(); cur = hist.group(1); buf.append(ln); continue
        if ln.startswith('|') and not re.match(r'\|[-|]+\|$', ln) and not inblk:
            flush(); out.append(('sec. %s row %s' % (sec, [c.strip() for c in ln.strip('|').split('|')][0][:60]), ln)); continue
        if ln.strip() == '' and not inblk:
            flush(); para += 1; cur = 'sec. %s para %d' % (sec, para); continue
        if ln.strip() == '***':
            flush(); continue
        buf.append(ln)
    flush()
    return out


def scan_hits(text):
    res = collections.OrderedDict()
    for k, t in units(text):
        f = sorted(set(m.group(0) for m in HPAT.finditer(re.sub(r'\s+', ' ', t))))
        if f:
            res.setdefault(k, set()).update(f)
    return res


RUNVAR = 'the run variable `T` (R6.NOTE.7), not the tool commit a3799244'
GENERAL_IMPL = '"the implementation" in general; states nothing the tool commit does'
GENERAL_RUN = 'a CI run in general, not CI run 45569710442'
EXCLUDE = collections.OrderedDict([
    ('R6.STAT.3', RUNVAR), ('R6.NOTE.7', RUNVAR), ('R6.OUT.12', RUNVAR), ('R6.REC.18', RUNVAR), ('R6.REPRO.1', RUNVAR),
    ('OBL-16', RUNVAR), ('HIST-3', 'v6.0b\'s rule that the run\'s tool commit be on `main`\'s first-parent chain (the run variable)'),
    ('R6.STAT.5', 'a rule for differences from the implementation; states no content of it'),
    ('R6.CLASS.7', 'a rule for differences from the tool commit; states no content of it'),
    ('R6.STAT.10', 'states that adoption uses none of this content'),
    ('R6.STAT.9', 'names the `T1\'` cases of sec. 6 as a topic; states no content'),
    ('sec. 0.1 para 5', 'owner decision 4 on item11-T1p\'s earlier figure (the figure is listed under OBL-23)'),
    ('R6.CTX.1', 'a rule for the counts at `T1\'`; states none'),
    ('R6.PROF.11', 'excludes `T1\'` as a source'),
    ('R6.CTRL.11', 'names `T1\'` as RT-M\'s input (a control input; adoption-trace row of controls reading `T1\'` or `P`)'),
    ('R6.SPLIT.2', 'classifies R6.SPLIT.1\'s measurement sentence as history (R6.SPLIT.1 is listed)'),
    ('R6.ANCH.18', GENERAL_IMPL), ('R6.GATE.9', GENERAL_IMPL), ('R6.GATE.11', GENERAL_IMPL), ('R6.EVID.1', GENERAL_IMPL),
    ('R6.EVID.2', GENERAL_IMPL), ('R6.OUT.13', GENERAL_RUN), ('R6.OUT.14', GENERAL_RUN), ('R6.REC.6', GENERAL_RUN),
    ('R6.DELEG.13', GENERAL_RUN), ('R6.REPRO.2', GENERAL_RUN),
    ('R6.GATE.13', 'gate self-test cases (survivors in general)'),
    ('R6.CTRL.1', 'the runner-cite convention of Table 17.1 (provenance; adoption-trace row of the runner cites)'),
    ('sec. 32 para 1', 'the gates of sec. 32 (implementation certification in general)'),
    ('sec. 32 para 2', 'the gates of sec. 32 (implementation certification in general)'),
    ('OBL-26', 'classifies the conformance assessment as provenance and states the certification gate; its pointer to the '
               'statements that describe the tool commit names this list'),
])
EXCLUDE_PREFIX = ('sec. 32 row ', 'a row of the obligation table or of the adoption trace of sec. 32 (a classification, '
                  'not a statement of content)')
INCLUDE = collections.OrderedDict([
    # the tool commit a3799244
    ('R6.PUR.12', 'a symbolic-link or submodule side change outside `D_rec` reaches the side-change classifier\'s byte read at the tool commit'),
    ('R6.PIPE.3', 'the list of flags is the parser at the tool commit'),
    ('R6.ANCH.10', 'at the tool commit, adjudicated HP sites in a non-conforming file of a ledgered segment are excluded from the search (VD-2)'),
    ('R6.ANCH.12', 'at the tool commit the translation accepts any occurrence at the translated line (VD-3)'),
    ('R6.HP.7', 'at the tool commit an adjudicated site is marked only by its `provenance` reference and counted under its last segment state'),
    ('R6.OUT.4', 'at the tool commit the isolation refusal writes a message with no class'),
    ('R6.OUT.18', 'the basis marks S and E (in the schema file at, or emitted at, the tool commit), the fields the schema file does not list today, the candidate members at the tool commit and the further top-level fields it emits'),
    ('R6.OUT.24', 'the obligation definitions are the tool commit\'s obligation set'),
    ('R6.SPLIT.3', 'that the conformance check found these readings of `sentences_of` at the tool commit (the readings are stated by r6 itself as part of the splitter and are checked against `P`\'s checker, `inputs/edits_check.py`)'),
    ('R6.RULE.11', 'the implementation does not enforce the 8-character minimum today'),
    ('R6.RULE.12', 'the implementation does not enforce the zero-fingerprint check today'),
    ('R6.REC.20', 'the implementation exits 65 with a message and no class today'),
    ('R6.HIT.2', 'the tool commit emits a hit in an HP region as REVIEW_REQUIRED `unclassified` with obligation `HP`'),
    ('R6.CLASS.1', 'at the tool commit the op A record checks, the replay equality, `ck_errors` and `extended_unmapped` FAIL without an item'),
    ('R6.CLASS.11', 'the implementation today makes the outcome FAIL through `record_checks.holds` without an item'),
    ('R6.GATE.7', 'which runners keep only a summary today'),
    ('R6.GATE.10', 'which mutants survived, or were not applied, in the mutation run of the tool commit (CI run 45569710442)'),
    ('R6.CTRL.19', 'the figures runners assert today; the two `not determined` `H..T1\'` cases of sec. 6'),
    ('R6.CTRL.25', 'Z9-STAGED\'s record id is `outcome` today'),
    ('R6.CTRL.27', 'the mutation sets at the tool commit, and which of their mutants survived or were not applied'),
    ('R6.CTRL.29', 'the verification defects of controls at the tool commit, and the defects without a control today'),
    ('R6.CTRL.30', 'Table 17.1: Z9-STAGED\'s record id `outcome` today; in rows N10 and RT-DR3W, that the `AGENTS.md` of `X_rep` (blob 9f4fc3e830707c90ffc105842d26d5b51f01760b) is the bytes of `T1\'`\'s copy'),
    ('R6.TREE.13', 'what the landing check\'s composition and the landing builder at the tool commit do'),
    ('R6.RDIR.7', 'outside `D_rec` the tool at the tool commit passes a non-regular side change to the classifier\'s byte read'),
    ('R6.RECON.11', 'at the tool commit RC6 reads the candidate\'s bytes at the splice\'s `H` offset'),
    ('OBL-21', 'that the tool commit has the defects VD-1 to VD-12, the side-change entry-type defect and those of RD-35 that it corrects'),
    ('OBL-24', 'the seven known survivors and the one unapplied mutant of the mutation run of the tool commit'),
    ('OBL-28', 'the behaviour that each row\'s Obligation column ascribes to the tool commit, and the figures not asserted today (C-5)'),
    ('sec. 34 row isolation refusal (no class at the tool commit)', 'the isolation refusal has no class at the tool commit'),
    # CI run 45569710442
    ('R6.EVID.6', 'the run\'s RT-L2 PASS, made on a drafted, unreviewed reconciliation record under harness admission'),
    ('R6.GATE.16', 'the RT-L2 PASS recorded by the run, made on a drafted record'),
    ('R6.RECON.21', 'the RT-L2 PASS recorded by the run, made on a drafted record'),
    ('OBL-13', 'the run\'s RT-L2 PASS, at `X` = `T1\'` on a drafted record'),
    # T1' and its objects
    ('R6.NOTE.3', '`T1\'` is `H` plus the 399 ledgered splices'),
    ('R6.SPLIT.1', 'version 2 changes no deny count at `H` or `T1\'` (measured)'),
    ('R6.PLAN.8', 'item 7 as frozen does not pass at `T1\'`'),
    ('R6.EVID.4', 'the 176 `final-unclassified` lines of item11-T1p at `T1\'`'),
    ('R6.EVID.5', 'the measurements at `T1\'` it lists as historical'),
    ('R6.EVID.7', 'that every figure of R6.EVID.4 was obtained at r6\'s drafting'),
    ('R6.EVID.8', 'the expected figures of the `X_rep` rows are those measured with the tool commit at `T1\'`, and the `T1\'` measurements in their `reference`'),
    ('OBL-7', '`papers/GR.md:58` matches `ptr` at `T1\'`'),
    ('OBL-23', 'its figures were measured with the tool commit at `T1\'`, among them item11-T1p\'s 176 lines'),
    ('HIST-11', 'the frozen tool\'s error counts at `T1\'`'),
    ('HIST-15', 'no DR-1d or DR-2 match at `T1\'`'),
    ('HIST-16', 'the `resid` outcome at `T1\'`'),
    ('HIST-20', 'the hit lines and review load at `T1\'`'),
    ('HIST-21', 'no DR-1d, DR-2 or DR-3 match at `T1\'`'),
    ('HIST-23', '17 REVIEW lines added at `T1\'`'),
])
NO_MATCH = ['OBL-21']
HITS_IN = scan_hits(T_IN)
UNCLASSIFIED = [k for k in HITS_IN if k not in INCLUDE and k not in EXCLUDE and not k.startswith(EXCLUDE_PREFIX[0])]
STALE = [k for k in INCLUDE if k not in HITS_IN and k not in NO_MATCH] + [k for k in EXCLUDE if k not in HITS_IN]
EXP = rj(R4['EXPECTATIONS.json'].decode('utf-8'))
_hp = re.compile(r"T1'|a3799244|45569710442|14ac71b4")
EXP_REF = [r['id'] for r in EXP['rows'] if _hp.search(json.dumps(r.get('reference')))]
EXP_SRC = [r['id'] for r in EXP['rows'] if '45569710442' in json.dumps(r.get('source'))]
EXP_FLAG = [r['id'] for r in EXP['rows'] if '45569710442' in json.dumps(r.get('flags'))]


def where(k):
    if k.startswith('sec. 34 row'):
        return 'sec. 34, migration table'
    if k.startswith('HIST-'):
        return 'Appendix H, ' + k
    return k


HS_ROWS = [(where(k), v) for k, v in INCLUDE.items()] + [
    ('EXPECTATIONS.json, `reference` fields (%d rows)' % len(EXP_REF),
     'measurements at `T1\'` or with the tool commit, and the mutants\' killers at CI run 45569710442: ' + ', '.join(EXP_REF)),
    ('EXPECTATIONS.json, `source` fields (%d rows)' % len(EXP_SRC),
     'the mutation results of CI run 45569710442: ' + ', '.join(EXP_SRC)),
    ('EXPECTATIONS.json, `flags` (%d row)' % len(EXP_FLAG), 'the RT-L2 PASS of CI run 45569710442: ' + ', '.join(EXP_FLAG)),
    ('FRESH-AUTHORIZATION.md', 'its quotations and summaries of the requirements listed above (the same statements)'),
    ('V4-COMPARISON.md', 'v6.0e sec. 6.4.1\'s report that neither rule form matches any line at `T1\'`'),
]
HS_TABLE = md_table(['Where', 'Statement, unsupported on `main`'], HS_ROWS)
HS_INTRO = (
    'Historical statements (%s, sec. 0.1; AGENTS.md sec. A.42 item 8). The statements below say what the tool commit '
    '%s does, what CI run 45569710442 recorded, or what `T1\'` (%s) contains or measured. None of that content is on '
    '`main` (%s), and this directory does not land it. For these statements, content on `main` establishes only that '
    'the identifiers name objects that are not reachable from `main`. Each statement is narrowed to that: it reports '
    'what the drafting read or measured, establishes nothing about the content, and is unsupported on `main`. No '
    'requirement, control, expectation, gate or adoption step relies on it (R6.STAT.10): a requirement that contains '
    'one holds or fails by its own controls on the tool revision, and a verification defect it names is corrected and '
    'tested there (OBL-21, OBL-28), not established by the statement. The tool files on `main` are not read here in '
    'place of the tool commit\'s; the conformance checks against the landed tool revision are OBL-26. The list was made '
    'by scanning this document for "tool commit", "today", "the implementation", "CI run", "survivor", `T1\'` and the '
    'identifiers of these objects and classifying each passage found (OBL-21 is listed without a match); the other '
    'files of this directory were read for the same statements.' % (OD5, TOOL, T1P, MAIN_AT))

# =====================================================================================================
# DESIGN-r6.md
# =====================================================================================================
# ---- sec. 0.1: the round-5 decision quoted byte-exact (item 2 with its opening and closing lines)
R5_SEC = '\n'.join([
    'The owner (amaybaum) decided on the round-4 delta review (#1169 comment %s, %s; ACCEPT WITH NITS) in the '
    'coordinating session on 2026-11-25; the decision is recorded at #1169 comment %s (%s), which introduces it as '
    '"Owner decision (amaybaum, %s, coordinating session), quoted in full:". Its opening line, item 2 and its general '
    'constraints, byte-exact as recorded (items 3 and 4, which concern other work, are omitted):' % (REV5_ID, REV5_REC_AT, DEC5_ID, DEC5_REC_AT, DEC5_AT),
    '', DEC5_QUOTE, '',
    'How r6 applies it; it authorizes preparation only, and nothing is adopted, frozen or merged:', '',
    '- `P`\'s `edits_check.py` lands byte-exact in this directory as `%s` (git blob %s, sha256 %s; at `P` it is %s). The '
    '12 requirements whose semantics it defines (%s) are unchanged; their support is on `main` once the landing merge '
    'is (sec. 32, adoption trace).' % (EC_PATH, EC_BLOB, EC_SHA, EC_SRC, ', '.join(REQ12[:-1]) + ' and ' + REQ12[-1]),
    '- generator-round4 and generator-round5 land with the documents they produce (LANDING-MANIFEST.md sec. 1).',
    '- The statements of r6 about the tool commit a3799244, CI run 45569710442 and `T1\'` are narrowed to what content on '
    '`main` establishes; each statement that stays unsupported is named in sec. 32 (historical statements) and in '
    'LANDING-MANIFEST.md sec. 4.',
    '- The round-4 delta review is recorded at #1169 comment %s; its body lands in generator-round5/records-1169-round5.json. '
    'Its nits 2 to 5 are applied; nit 1 is left to the tool revision (OBL-28, C-4).' % REV5_ID, ''])
_anchor = ('One short independent delta review covers this revision before adoption (R6.STAT.10).\n\n***\n\n'
           '## 1. Notation and symbols')
if T.count(_anchor) != 1:
    PROBLEMS.append('sec. 0.1 anchor not unique')
else:
    _j = T.index(_anchor) + len('One short independent delta review covers this revision before adoption (R6.STAT.10).\n')
    T = T[:_j] + '\n' + R5_SEC + T[_j:]
    log('D1-D3', 'sec. 0.1', 'the owner decision of %s quoted byte-exact (opening line, item 2, general constraints), with how r6 applies it' % DEC5_AT)

# ---- NIT2: the A3 quotation note
edit('NIT2', 'sec. 0.1', 'Decisions A1 to A5 and the closing direction, byte-exact as relayed (each line prefixed by "> "):',
     'Decisions A1 to A5 and the closing direction, as relayed (each line prefixed by "> "), verbatim sentence by sentence; '
     'the A3 paragraph joins five paragraphs of the record into one:')

# ---- D1: the edits_check.py row of the adoption trace
edit('D1', 'sec. 32 adoption trace',
     '| the plan commit `P` (its record directory is on no commit reachable from `main`) | the normative meaning of these '
     'requirements | support off `main`: open; closed by landing that blob on `main` no later than the adoption record, or '
     'by r6 stating the semantics itself; the copy frozen at `F` reaches `main` only with the round\'s landing, after '
     'adoption |',
     '| `P`\'s `edits_check.py`, from the plan commit `P` (its record directory is on no commit reachable from `main`) | the '
     'normative meaning of these requirements | support on `main` once landed: the blob lands byte-exact in this directory '
     'as `%s` (git blob %s; %s, sec. 0.1) and these requirements read it there, unchanged; on `main` with the landing '
     'merge, no later than the adoption record; the copy frozen at `F` reaches `main` with the round\'s landing |'
     % (EC_PATH, EC_BLOB, OD5))

# ---- D3: the statements row, the controls row and the list of historical statements
_srow = re.search(r'\n\| statements of what the tool commit does \("at the tool commit", "today"\):[^\n]*\|\n', T)
if not _srow:
    PROBLEMS.append('sec. 32: statements row not found')
else:
    T = T[:_srow.start()] + (
        '\n| the historical statements listed below: what the tool commit a3799244 does, what CI run 45569710442 recorded, '
        'what `T1\'` contains or measured | the tool commit, its conformance assessment, the CI run, `T1\'` and its objects '
        '| each reports what the drafting read or measured; no requirement, control, expectation, gate or adoption step uses '
        'it (R6.STAT.10) | unsupported on `main`; each is narrowed and named below (%s, sec. 0.1); none supports adoption |\n'
        % OD5) + T[_srow.end():]
    log('D3', 'sec. 32 adoption trace', 'statements row: unsupported on main, named in the list of historical statements')
edit('D3', 'sec. 32 adoption trace', 'RT-C, the `T1\'` case of RT-DR, RT-M, RT-D-gr58, RT-L, S11-56,',
     'RT-C, the `T1\'` case of RT-DR, RT-M, RT-D-gr58, RT-L, RT-X, WB1, N-W, S11-56,')
_o1 = '\n\n**OBL-1** P-parity of `register` and `infinity`.'
if T.count(_o1) != 1:
    PROBLEMS.append('sec. 32: OBL-1 anchor not unique')
else:
    _k = T.index(_o1)
    T = T[:_k] + '\n\n' + HS_INTRO + '\n\n' + HS_TABLE + T[_k:]
    log('D3', 'sec. 32', 'list of historical statements: %d rows, each unsupported on main' % len(HS_ROWS))
bedit('D3', 'OBL-26', 'tool commit use it, and are listed in the adoption trace below as off-`main` support.',
      'tool commit use it; they are unsupported on `main` and are named in the historical statements of sec. 32.')

# ---- NIT1: C-4
bedit('NIT1', 'OBL-28', 'TR45-opC is deferred with R6.OUT.15 and recorded NOT RUN (owner decision A1 of 2026-11-25) |',
      'TR45-opC is deferred with R6.OUT.15 and recorded NOT RUN (owner decision A1 of 2026-11-25); the runner that records '
      'TR45-opC NOT RUN with the deferral reason, and TR45-opB\'s runner recording NOT RUN in place of the replay, are left '
      'to the tool revision (round-4 delta review, nit 1) |', 'C-4: the TR45-opC runner left to the tool revision')

# =====================================================================================================
# FRESH-AUTHORIZATION.md (quoted wording of changed blocks), AUTHORIZATIONS.md
# =====================================================================================================
REQS_IN = parse_reqs(T_IN)
REQS = parse_reqs(T)
CHANGED = [r for r in REQS_IN if REQS_IN[r]['text'] != REQS.get(r, {}).get('text')]
for rid in CHANGED:
    old, new = bq(NS4['NS']['block'](rid, T_IN)), bq(NS4['NS']['block'](rid, T))
    n = FRESH.count(old)
    if n:
        FRESH = FRESH.replace(old, new)
        log('meta', 'FRESH-AUTHORIZATION.md', 'quoted wording of %s regenerated (%d occurrence(s))' % (rid, n))
A5_AUTH = '\n'.join([
    '### #1169 comment %s (%s): owner decision of %s on the landing package of r6' % (DEC5_ID, DEC5_REC_AT, DEC5_AT), '',
    '- Given by the owner (amaybaum) in the coordinating session and recorded at #1169 comment %s, which quotes it in full '
    'with author and time; its opening line, item 2 and general constraints are quoted byte-exact in DESIGN-r6.md sec. 0.1 '
    'and below.' % DEC5_ID, '', DEC5_QUOTE, '',
    '- Permits: landing `P`\'s `edits_check.py` and generator-round4 in the proposed landing package; narrowing the '
    'historical statements and naming those that stay unsupported; regenerating the documents; one focused independent '
    'review. Preparation only.',
    '- Does not permit: design adoption or merging into `main`, each of which needs separate approval; weakening any of '
    'the 12 requirements that rest on `edits_check.py`.',
    '- Relied on by: the edits_check.py row of the adoption trace and the historical statements of DESIGN-r6.md sec. 32; '
    'LANDING-MANIFEST.md secs. 1 and 4.', ''])
_a2 = AUTH.index('***\n\n## 2. Class (ii)')
AUTH = AUTH[:_a2] + A5_AUTH + '\n' + AUTH[_a2:]
log('D1-D3', 'AUTHORIZATIONS.md', 'entry for the owner decision of %s added to sec. 1' % DEC5_AT)
AUTH = AUTH.rstrip('\n') + ('\n- #1169 comment %s (%s) records the delta review of the round-4 revision (commit %s), reviewer '
                            'text verbatim; its body lands in generator-round5/records-1169-round5.json. It is a review '
                            'record, not an owner decision.\n' % (REV5_ID, REV5_REC_AT, R4_COMMIT))
log('meta', 'AUTHORIZATIONS.md', 'sec. 5: the round-4 delta review record')

# =====================================================================================================
# LANDING-MANIFEST.md
# =====================================================================================================
G = NS4['GIT']
H, MAIN, OFF, HOST, NOOBJ = NS4['H'], NS4['MAIN'], NS4['OFF'], NS4['HOST'], NS4['NOOBJ']
SOM, SOMH, PROV = NS4['SOM'], NS4['SOMH'], NS4['PROV']
ONCE = 'on main once landed'
UNSUP = 'unsupported on main, named in DESIGN-r6.md sec. 32 (historical statements) and in sec. 4 below (%s)' % OD5
G[TOOL] = (G[TOOL][0], OFF, 'in DESIGN-r6.md: ' + PROV + ' for OBL-26 and the runner cites (no requirement rests on it); its '
           'statements of what the tool commit does: ' + UNSUP + '; in EXPECTATIONS.json (`runner`, `reference` keys) and '
           'MIGRATION.json: ' + PROV + '; in REVIEW-r6-round3.md and the review snapshots: ' + PROV)
G[T1P] = (G[T1P][0], OFF, 'in DESIGN-r6.md: R6.NOTE.3\'s statement of its content: ' + UNSUP + '; in EXPECTATIONS.json '
          '`reference` keys: ' + PROV + ' (never compared, R6.GATE.9)')
G[P_COMMIT] = (G[P_COMMIT][0], OFF, 'for the semantics of %s: support on main once landed, through `P`\'s edits_check.py, '
               'which lands as %s (sec. 4); the other uses of `P` (the external oracle of R6.GATE.7 and R6.GATE.8, '
               'controls reading `P`): as the adoption trace of DESIGN-r6.md sec. 32 classifies them, for implementation '
               'certification and the tool\'s landing, not adoption' % (', '.join(REQ12), EC_PATH))
_t1obj = ('; that it is `T1\'`\'s: ' + UNSUP)
G['9f4fc3e830707c90ffc105842d26d5b51f01760b'] = (G['9f4fc3e830707c90ffc105842d26d5b51f01760b'][0], OFF,
                                                  G['9f4fc3e830707c90ffc105842d26d5b51f01760b'][2] + _t1obj)
G['86d79863821f3f8cdad86771008b2df89fd1961a'] = (G['86d79863821f3f8cdad86771008b2df89fd1961a'][0], NOOBJ,
                                                  'not a reference: an expected value computed from on-main content '
                                                  '(`M`\'s AGENTS.md and splice D296)')
G[EC_BLOB] = ('blob of `P`\'s edits_check.py, landed as %s' % EC_PATH, ONCE,
              SOM + ' once landed: the semantics of the 12 requirements (sec. 4)')
G[R4_COMMIT] = ('round-4 outputs, input of generator-round5; reviewed by #1169 comment %s' % REV5_ID, H,
                SOMH + '; the claims citing it (generator inputs, the reviewed commit) read its content there')
G[MAIN_AT] = ('`main` at the round-5 revision', MAIN, SOM + ': the object is reachable from main, and every claim citing '
              'it reads it there')
for p, b in BLOB5.items():
    if b not in G:
        G[b] = ('blob of %s at 2aec244e' % p, H, PROV + ': an input pin of generator-round5 (tree-2aec244e.json)')
DIG = NS4['DIG']
DIG['59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2'] = (
    DIG['59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2'][0], OFF,
    DIG['59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2'][2] + _t1obj)
DIG[sha(REV5_TEXT)] = ('sha256 of the round-4 delta review text (#1169 comment %s)' % REV5_ID, HOST,
                       SOM + ': the text lands in generator-round5/records-1169-round5.json')
for cid, c in REC5.items():
    NS4['COMMENT_BODIES'][cid] = c['body']
    NS4['BODY_SHA'][sha(c['body'])] = cid
NS4['PAT']['comment'] = r'(?<![0-9a-f])7\d{9}(?![0-9a-f])'
FALSE_IDS = ['7156468072', '7393184198', '7416978004', '7428102037']  # the review named the last three; 7156468072 is of the same kind

# ---- landed files
NEW5 = collections.OrderedDict([('DESIGN-r6.md', T), ('AUTHORIZATIONS.md', AUTH), ('FRESH-AUTHORIZATION.md', FRESH)])
GEN5 = collections.OrderedDict([
    ('generator-round5/correct5.py', rdb(os.path.abspath(__file__))),
    ('generator-round5/tree-2aec244e.json', rdb(os.path.join(INP, 'tree-2aec244e.json'))),
    ('generator-round5/records-1169-round5.json', rdb(os.path.join(INP, 'records-1169-round5.json')))])
ROLE5 = collections.OrderedDict()
for p, r in NS4['ROLE'].items():
    ROLE5[p] = r
for p in G4FILES:
    ROLE5[p] = 'round-4 generator (produces the round-4 documents)'
ROLE5[EC_PATH] = 'committed input: `P`\'s edits_check.py, defining the semantics of 12 requirements'
for p in GEN5:
    ROLE5[p] = 'round-5 generator (produces the round-5 documents)'
LANDED5 = collections.OrderedDict()
SOURCE5 = collections.OrderedDict()
for p in ROLE5:
    if p in NEW5:
        LANDED5[p] = NEW5[p].encode('utf-8')
        SOURCE5[p] = 'round-5 output' if LANDED5[p] != R4.get(p) else 'unchanged from 2aec244e (blob %s)' % BLOB5[p][:12]
    elif p in GEN5:
        LANDED5[p], SOURCE5[p] = GEN5[p], 'round-5 generator'
    elif p == EC_PATH:
        LANDED5[p], SOURCE5[p] = EC, '`P` (%s), path %s (blob %s)' % (P_COMMIT[:12], EC_SRC, EC_BLOB[:12])
    elif p in G4FILES:
        LANDED5[p], SOURCE5[p] = rdb(G4FILES[p]), 'unchanged from 2aec244e (blob %s)' % BLOB5[p][:12]
    else:
        LANDED5[p] = R4[p] if p in R4 else NS4['SRC'][p]
        SOURCE5[p] = 'unchanged from 2aec244e (blob %s)' % BLOB5[p][:12]
    if p in BLOB5 and SOURCE5[p].startswith('unchanged') and gitblob(LANDED5[p]) != BLOB5[p]:
        PROBLEMS.append('manifest: %s marked unchanged but differs from 2aec244e' % p)
DROPPED5 = collections.OrderedDict(list(NS4['DROPPED'].items()) + [
    ('CORRECTION-REPORT-round4.md', 'report of the round-4 generator (regenerated by its recipe)')])
_cov = set(p for p in LANDED5 if p in BLOB5) | set(DROPPED5) | {'LANDING-MANIFEST.md'}
if _cov != set(BLOB5) or set(LANDED5) & set(DROPPED5):
    PROBLEMS.append('manifest: landed and dropped files do not partition the 45 files: %s' % sorted(set(BLOB5) ^ _cov))
FILE_SHA = NS4['FILE_SHA']
for p, b in LANDED5.items():
    FILE_SHA[sha(b)] = p
NS4['SNAP'].update(p for p in GEN5 if p != 'generator-round5/correct5.py')
NS4['SNAP'].add(EC_PATH)
GENS = ('generator-round4/correct4.py', 'generator-round5/correct5.py')
SCAN5 = [p for p in LANDED5 if p not in GENS]


def classify5(kind, tok, files):
    if files == {EC_PATH} or (files <= NS4['SNAP'] and EC_PATH in files and kind in ('comment', 'number', 'short')):
        if kind == 'short' and any(k.startswith(tok) for k in G):
            pass
        elif kind in ('comment', 'number', 'short'):
            st = MAIN if kind == 'short' else HOST
            return ('%s in a code comment of `P`\'s edits_check.py' % ({'comment': '#1169 comment', 'number': 'Issue or pull '
                    'request', 'short': 'commit prefix (on main)'}[kind]), st, PROV + ': a code comment; the requirements '
                    'use the functions and patterns of the file, not its comments')
    if kind == 'comment' and tok in FALSE_IDS:
        return (('not a comment id: a digit run that the round-4 delta review names as a false match of the round-4 scanner'
                 if tok != FALSE_IDS[0] else 'not a comment id: a digit run inside blob 4c18f7156468, a false match of the round-4 '
                 'scanner of the same kind'), NOOBJ, PROV + ': no comment of that id exists')
    if tok in (EC_SHA, EC_SHA[:8]):
        return ('sha256 of %s (`P`\'s edits_check.py)' % EC_PATH, ONCE, SOM + ' once landed: the semantics of the 12 requirements (sec. 4)')
    if kind == 'branch' and tok == 'ci/ledger-coverage-suite-a3799244':
        return ('branch ci/ledger-coverage-suite-a3799244, holding the tool commit a3799244', OFF, PROV + ': names where the '
                'tool commit is held; see the row of a37992449b45')
    if kind == 'run' and tok == '45569710442':
        return ('CI run 45569710442 (tool commit a3799244)', HOST, 'in DESIGN-r6.md: its statements of what the run recorded: '
                + UNSUP + '; in EXPECTATIONS.json `source` and `reference` fields: ' + PROV + ' (unsupported, named in the '
                'same list)')
    if kind == 'short' and tok in ('3ae6b8b2', '5f865f8c') and files <= NS4['SNAP']:
        return ('sha256 prefix of a round-4 output of 2aec244e (in the round-4 review text)', H, PROV + ': inside a verbatim '
                'snapshot; no claim of the documents uses it')
    c = NS4['classify'](kind, tok, files)
    if c is None and files <= NS4['SNAP'] and kind in ('hex40', 'short', 'sha256'):
        return ('id inside a verbatim snapshot or generator data', NOOBJ, PROV + ': no claim of the landed documents uses it')
    if c is not None:
        c = (c[0], c[1], c[2].replace('generator-round2, generator-round3 or generator-round4',
                                      'generator-round2, generator-round3, generator-round4 or generator-round5'))
    return c


def scan(paths, pat):
    found = collections.OrderedDict()
    for p in paths:
        t = LANDED5[p].decode('utf-8')
        for kind, rx in pat.items():
            for m in re.findall(rx, t):
                found.setdefault((kind, m), set()).add(p)
    return found


PAT = NS4['PAT']
FOUND5 = scan(SCAN5, PAT)
REFROWS = []
for (kind, tok), files in sorted(FOUND5.items(), key=lambda x: (list(PAT).index(x[0][0]), x[0][1])):
    c = classify5(kind, tok, files)
    if c is None:
        PROBLEMS.append('manifest: unclassified reference %s %s in %s' % (kind, tok, sorted(files)))
        continue
    REFROWS.append((tok, kind, c[0], c[1], ', '.join(sorted(files)), c[2]))
TABLE_TOKS = set(r[0] for r in REFROWS)
GEN_EXTRA = collections.OrderedDict()
for p in GENS:
    t = LANDED5[p].decode('utf-8')
    for kind in PAT:
        for m in re.findall(PAT[kind], t):
            if m not in TABLE_TOKS:
                c = classify5(kind, m, {p})
                GEN_EXTRA.setdefault(m, (kind, c, set()))[2].add(p)
GEN_NOTE = []
shown = lambda m: m[:12] if re.fullmatch('[0-9a-f]+', m) else m
for m, (kind, c, ps) in GEN_EXTRA.items():
    if c is None:
        st = 'value computed by the generator or an input pin it checks'
        if m in BLOB5.values() or m in [b for b in NS4['BLOB'].values()]:
            st = 'blob id of a file of this directory at c33d5b71 or 2aec244e'
        elif m in INPUT5.values() or m in [h for _, h in NS4['INPUT_SHA']]:
            st = 'sha256 of a generator input that lands'
        GEN_NOTE.append('%s (%s, %s)' % (shown(m), ', '.join(sorted(ps)), st))
    else:
        GEN_NOTE.append('%s (%s, %s: %s)' % (shown(m), ', '.join(sorted(ps)), c[1], c[0]))

# ---- section 4: support off main that remains
HS_LIST = '\n'.join('  - %s: %s' % (w, s) for w, s in HS_ROWS)
MANIFEST = '\n'.join([
    '# r6: landing manifest', '',
    'Owner decision A5 of 2026-11-25 (%s), quoted: "%s"' % (NS4['OWNER_AT'], NS4['body']('A5')), '',
    'Owner decision of %s (amaybaum, coordinating session; #1169 comment %s, %s), item 2, quoted: "Include `edits_check.py` '
    'and the round-4 generator in the proposed landing package." "Preserve all 12 verification requirements without '
    'weakening them." "Narrow the historical statements to what the evidence on `main` establishes and explicitly identify '
    'unsupported statements." "Regenerate the documents and complete one focused independent review." "Preparation is '
    'authorized. Design adoption and merging into `main` still require separate approval."' % (DEC5_AT, DEC5_ID, DEC5_REC_AT), '',
    'Directory: `%s/`. The landing tree of this directory is the round-4 tree (commit %s) with the round-5 outputs, the '
    'files of sec. 1 kept and those of sec. 2 removed. This manifest approves no merge; the landing pull request\'s merge '
    'needs its own owner approval (AGENTS.md sec. A.50 item 1).' % (DIRPATH, R4_COMMIT), '',
    '## 1. Files that land', '',
    md_table(['Path', 'Role', 'Source', 'sha256'], [(p, ROLE5[p], SOURCE5[p], sha(LANDED5[p])) for p in LANDED5] +
             [('LANDING-MANIFEST.md', 'this manifest (A5)', 'round-5 output', '(this file)')]), '',
    'Note on the generators and `%s`: generator-round4 and `%s` land by the owner decision of %s (item 2, quoted above). '
    'generator-round5 produces the round-5 documents and lands under the same decision as a committed input necessary '
    'for their reproducibility (A5). `%s` is `P`\'s file %s at commit %s, byte-exact (git blob %s, sha256 %s, both '
    'checked by generator-round5). CORRECTION-REPORT-round4.md and CORRECTION-REPORT-round5.md, which the generators '
    'write beside their outputs, are not landed (each is regenerated by its recipe).'
    % (EC_PATH, EC_PATH, DEC5_AT, EC_PATH, EC_SRC, P_COMMIT, EC_BLOB, EC_SHA), '',
    'Recipe (AGENTS.md sec. A.42 item 1): lay out `out-final4/`, `c33/` and `out-final5/build/` as the round-4 recipe '
    'states (generator-round4 as `out-final5/build/`, correct4.py with its four inputs in `inputs/`) and run it, which '
    'writes into `out-final5/` the twelve files of the directory at %s that generator-round4 produces (its eleven outputs '
    'and CORRECTION-REPORT-round4.md); then lay out `out-final6/build/` as '
    'generator-round5 (correct5.py, with tree-2aec244e.json, records-1169-round5.json and a copy of `%s` in `inputs/`). '
    'Run `python3 -I -B out-final6/build/correct5.py`. It exits 0 and writes the files of sec. 1 marked "round-5 output" '
    'with the sha256 stated, after running generator-round4 in-process and checking that it reproduces every round-4 '
    'output and that the twelve files equal their blobs at 2aec244e. The earlier generators reproduce their rounds as '
    'their own reports state.' % (R4_COMMIT[:8], EC_PATH), '',
    '## 2. Files left to Git history', '',
    'Each stays at %s (and its ancestors on the branch), reachable from main once the landing merge keeps the branch '
    'history.' % R4_COMMIT[:8], '',
    md_table(['Path', 'What it is', 'Blob at 2aec244e'], [(p, why, BLOB5[p]) for p, why in DROPPED5.items()]), '',
    'Landing precondition: the merge keeps the branch history (a merge commit or fast-forward, not a squash), so that '
    '2aec244e, c33d5b71, 400e4b4f, ad035ff5, a6b6884b, f4e18558, c1244459 and 4e9a1501 become reachable from main. Without '
    'it, every reference below classified "%s" is support off main.' % SOMH.split(' (')[0], '',
    '## 3. References of the landed files to content not on `main` (AGENTS.md sec. A.42 item 8)', '',
    'Every reference found in the landed files, except this manifest and the two generator programs, by commit, blob, tree '
    'or digest id, comment, Issue or pull-request number, CI run or branch name, each classified by the claim it is '
    'attached to. "Status" says where the referenced content is. A comment id is matched only where it is not part of a '
    'longer hexadecimal string. The generator programs correct4.py and correct5.py carry the references of this table and '
    'also: %s.' % ('; '.join(GEN_NOTE) if GEN_NOTE else 'none'), '',
    md_table(['Reference', 'Kind', 'What it names', 'Status', 'Occurs in', 'Classification'], REFROWS), '',
    '## 4. Support off `main` that remains', '',
    '- Closed by this landing: the semantics that %s define by reference to `P`\'s edits_check.py. The file lands '
    'byte-exact as `%s` (git blob %s, sha256 %s; %s, item 2); it is support on `main` once the landing merge is on `main`, '
    'no later than the adoption record. The 12 requirements are unchanged.' % (', '.join(REQ12[:-1]) + ' and ' + REQ12[-1],
                                                                              EC_PATH, EC_BLOB, EC_SHA, OD5),
    '- Unsupported on `main`, named here and in DESIGN-r6.md sec. 32 (historical statements), and landing by the %s, which '
    'directs that they be identified (AGENTS.md sec. A.42 item 8). Each statement is narrowed there to a report of what the '
    'drafting read or measured in the tool commit %s, CI run 45569710442 or `T1\'` (%s); none of that content is on `main` '
    'or lands, and no requirement, control, expectation, gate or adoption step relies on the statement (R6.STAT.10). The '
    'statements:' % (OD5, TOOL, T1P), HS_LIST,
    '- The other rows of the adoption trace of DESIGN-r6.md sec. 32 classified support off `main` stay as classified '
    'there: owner decisions recorded only in paraphrase or relayed in session (open until quoted with author and time in '
    'a record on `main`); the external oracle of R6.GATE.7 and R6.GATE.8 (implementation certification); and the controls '
    'reading `T1\'` or `P`, with the ledger and edit-list pins (acceptance references for the tool\'s landing). No claim of '
    'this landing uses the last two.', ''])
log('D1-D3', 'LANDING-MANIFEST.md', 'regenerated: %d landed files, %d left to history, %d references classified'
    % (len(LANDED5) + 1, len(DROPPED5), len(REFROWS)))
log('NIT3', 'LANDING-MANIFEST.md', 'comment ids matched only outside longer hexadecimal strings; the four false rows dropped (the three the review names, and 7156468072, of the same kind)')
log('NIT4', 'LANDING-MANIFEST.md', 'note on the generator programs completed with the references not in the table')
log('NIT5', 'LANDING-MANIFEST.md', '86d79863: not a reference')
log('D2', 'LANDING-MANIFEST.md', 'generator-round4 and generator-round5 land; the caveat on generator-round4 replaced by the decision')

# =====================================================================================================
# self-checks
# =====================================================================================================
EXP_OUT_TXT = R4['EXPECTATIONS.json'].decode('utf-8')
REQ_OUT_TXT = R4['REQUIREMENTS.json'].decode('utf-8')
CHK_AFTER, VAL_AFTER = run_checks(T, NS4['EXP_OUT']['rows'], NS4['REQ_OUT'], NS4['EXP_OUT'], NS4['PEND3'])
# round-4 checks on the round-5 outputs: generator-round4's own check code, with its documents replaced by round 5's
NS4B = dict(NS4)
NS4B.update({'T': T, 'REQS': REQS, 'FRESH': FRESH, 'LOG': list(NS4['LOG']) + LOG,
             'PROBLEMS': [p for p in PROBLEMS if p.startswith('manifest:')]})
exec(compile(SEG_CHECKS, 'correct4-checks', 'exec'), NS4B)
OWN_AFTER = NS4B['OWN']
for p in NS4B['PROBLEMS']:
    if p.startswith('check failed') and p not in PROBLEMS:
        PROBLEMS.append('round-4 ' + p)
_cB, _vB = run_checks(T_IN, NS4['EXP_OUT']['rows'], NS4['REQ_OUT'], NS4['EXP_OUT'], NS4['PEND3'])
OWN5 = collections.OrderedDict()
OWN5['inputs: every round-4 output and generator-round4 file equals its git blob at 2aec244e; edits_check.py is blob 1153e039 with sha256 2856e58c...d98c'] = [
    p for p in PROBLEMS if p.startswith(('input ', 'edits_check', 'tree listing'))]
OWN5['generator-round4 regenerates every round-4 output byte-identical to 2aec244e'] = [
    p for p in PROBLEMS if p.startswith('generator-round4')]
OWN5['records: the decision lines quoted occur verbatim in comment 7171541574; the review text has the sha256 its record states'] = [
    p for p in PROBLEMS if p.startswith(('records', 'decision', 'round-4 delta review'))]
OWN5['D1: edits_check.py lands byte-exact; the 12 requirement blocks and REQUIREMENTS.json unchanged'] = (
    ([] if LANDED5.get(EC_PATH) == EC else ['blob']) + [r for r in REQ12 if REQS_IN[r]['text'] != REQS[r]['text']] +
    ([] if REQ_OUT_TXT.encode('utf-8') == R4['REQUIREMENTS.json'] else ['REQUIREMENTS.json']))
OWN5['D1: no reference is support off main relied on by adoption; the P rows are support on main once landed'] = (
    [r[0] for r in REFROWS if 'relied on by adoption' in r[5] and 'not relied on by adoption' not in r[5]] +
    [r[0] for r in REFROWS if r[0] in (P_COMMIT, EC_BLOB, '1153e039', '2856e58c', EC_SHA) and 'once landed' not in r[5]])
OWN5['D2: generator-round4 lands byte-identical to 2aec244e, generator-round5 lands, no merge caveat remains'] = (
    [p for p in G4FILES if gitblob(LANDED5[p]) != BLOB5[p]] + [p for p in GEN5 if p not in LANDED5] +
    (['caveat'] if 'Its landing is part of the owner\'s merge decision' in MANIFEST else []))
OWN5['D3: every passage of the round-4 design found by the scan is listed or excluded with a reason; no stale entry'] = (
    UNCLASSIFIED + ['stale:' + k for k in STALE])
OWN5['D3: the list of unsupported statements is the same in DESIGN-r6.md sec. 32 and LANDING-MANIFEST.md sec. 4'] = [
    w for w, s in HS_ROWS if ('| %s | %s |' % (w, s.replace('|', '/'))) not in T or ('  - %s: %s' % (w, s)) not in MANIFEST]
OWN5['D3: every row of the manifest naming the tool commit, the run or `T1\'` as support off main names the list'] = [
    r[0] for r in REFROWS if 'support off main' in r[5] and 'acceptance references' not in r[5] and 'tool\'s landing' not in r[5]
    and 'certification' not in r[5]]
_old_found = scan([p for p in NS4['SCAN']], collections.OrderedDict([('comment', r'(?<!\d)7\d{9}(?!\d)')]))
_new_found = scan([p for p in NS4['SCAN']], collections.OrderedDict([('comment', PAT['comment'])]))
OWN5['NIT3: the hardened comment pattern drops exactly the four false ids (three named by the review, and 7156468072), and no other; none is classified a comment'] = (
    [] if sorted(set(k[1] for k in _old_found) - set(k[1] for k in _new_found)) == FALSE_IDS else ['diff']) + [
    r[0] for r in REFROWS if r[0] in FALSE_IDS and (r[4] != 'generator-round5/records-1169-round5.json' or not r[2].startswith('not a comment id'))]
OWN5['NIT4: the references of correct4.py and correct5.py outside the table are listed in the note'] = [
    m for m in GEN_EXTRA if shown(m) not in MANIFEST or GEN_EXTRA[m][1] is None]
OWN5['NIT5: 86d79863 is classified "not a reference"'] = [
    r[0] for r in REFROWS if r[0].startswith('86d79863') and not r[5].startswith('not a reference')]
OWN5['NIT1/NIT2: the C-4 sentence and the A3 note applied once each'] = (
    ([] if REQS['OBL-28']['text'].count('round-4 delta review, nit 1') == 1 else ['C-4']) +
    ([] if T.count('verbatim sentence by sentence;') == 1 and 'byte-exact as relayed' not in T else ['A3']))
OWN5['preservation: EXPECTATIONS.json byte-identical (rows, controls, expectations); requirement count and ids unchanged'] = (
    ([] if EXP_OUT_TXT.encode('utf-8') == R4['EXPECTATIONS.json'] else ['EXPECTATIONS.json']) +
    sorted(set(REQS_IN) ^ set(REQS)) + ([] if len(REQS) == 428 else ['count %d' % len(REQS)]))
OWN5['preservation: requirement blocks changed only where logged (OBL-26, OBL-28)'] = sorted(
    set(CHANGED) ^ {'OBL-26', 'OBL-28'})
OWN5['preservation: unchanged outputs byte-identical to 2aec244e'] = [
    p for p in ('EXPECTATIONS.json', 'REQUIREMENTS.json', 'PARAPHRASED-DECISIONS.md', 'REVIEW-r6-round3.md',
                'MIGRATION.json', 'V4-COMPARISON.md', 'REVIEW-r6-round2.md') if LANDED5[p] != R4[p]]
OWN5['manifest: every reference classified; landed and dropped partition the 45 files'] = [
    p for p in PROBLEMS if p.startswith('manifest:')]
for k, v in list(CHK_AFTER.items()) + list(OWN5.items()):
    if v and not k.startswith(('inputs:', 'generator-round4', 'records:')):
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================================
# CORRECTION-REPORT-round5.md
# =====================================================================================================
CONTENT = collections.OrderedDict([
    ('DESIGN-r6.md', T), ('AUTHORIZATIONS.md', AUTH), ('FRESH-AUTHORIZATION.md', FRESH), ('LANDING-MANIFEST.md', MANIFEST)] + [
    (p, R4[p].decode('utf-8')) for p in ('EXPECTATIONS.json', 'REQUIREMENTS.json', 'PARAPHRASED-DECISIONS.md',
                                         'REVIEW-r6-round3.md', 'MIGRATION.json', 'V4-COMPARISON.md', 'REVIEW-r6-round2.md')])
CONTENT[EC_PATH] = EC.decode('utf-8')


def report():
    hashes = collections.OrderedDict((n, sha(c)) for n, c in CONTENT.items())
    vk = list(VAL_AFTER)
    L = ['# r6, round 5: correction report', '',
         'Generator: build/correct5.py (landed as generator-round5/). Applies item 2 of the %s (#1169 comment %s, quoted in '
         'DESIGN-r6.md sec. 0.1) and nits 1 to 5 of the round-4 delta review (#1169 comment %s). Preparation only: nothing is '
         'adopted, frozen, merged or executed.' % (OD5, DEC5_ID, REV5_ID), '',
         '## 1. Inputs', '', md_table(['Input', 'sha256 or git blob'],
                                       [('directory at 2aec244e: ' + p, 'blob ' + b) for p, b in BLOB5.items()] +
                                       [('build/inputs/' + n, h) for n, h in INPUT5.items()]), '',
         'generator-round4 is executed in-process up to its report; it checks its own inputs against c33d5b71 and regenerated '
         '%d outputs, each byte-identical to 2aec244e.' % C4_REPRO, '',
         '## 2. Edits', '', md_table(['#', 'Item', 'Target', 'Edit'], [(i + 1, d, t, e) for i, (d, t, e) in enumerate(LOG)]), '',
         'Items: D1, `edits_check.py` lands as `%s`; D2, generator-round4 and generator-round5 land; D3, the historical '
         'statements narrowed and named; NIT1 to NIT5, the round-4 delta review\'s nits (nit 1 only as the C-4 sentence; its '
         'runner is left to the tool revision).' % EC_PATH, '',
         '## 3. Values, before (round 4) and after', '',
         md_table(['Value', 'Before', 'After'], [(k, VAL_BEFORE[k], VAL_AFTER[k]) for k in vk] + [
             ('historical statements named unsupported (rows of the list)', 0, len(HS_ROWS)),
             ('references classified in the manifest', len(NS4['REFROWS']), len(REFROWS)),
             ('references classified support off main relied on by adoption', len(NS4['N_OFF_ADOPT']),
              len([r for r in REFROWS if 'relied on by adoption' in r[5] and 'not relied on by adoption' not in r[5]])),
             ('files that land (with this manifest)', len(NS4['LANDED']) + 1, len(LANDED5) + 1),
             ('files left to Git history', len(NS4['DROPPED']), len(DROPPED5))]), '',
         '## 4. Self-checks', '', 'Round-3 checks (run_checks of correct3.py), before (round-4 outputs) and after:', '',
         md_table(['Check', 'Before', 'After'], [(k, len(CHK_BEFORE[k]) if CHK_BEFORE[k] else 'pass',
                                                  len(CHK_AFTER[k]) if CHK_AFTER[k] else 'pass') for k in CHK_AFTER]), '',
         'Round-4 checks (generator-round4\'s own check code, run on the round-4 outputs and on the round-5 outputs):', '',
         md_table(['Check', 'Before', 'After'], [(k, 'pass' if not OWN_BEFORE[k] else 'FAIL %s' % OWN_BEFORE[k][:5],
                                                  'pass' if not OWN_AFTER[k] else 'FAIL %s' % OWN_AFTER[k][:5]) for k in OWN_AFTER]), '',
         'Round-5 checks:', '', md_table(['Check', 'Result'], [(k, 'pass' if not v else 'FAIL %s' % v[:5]) for k, v in OWN5.items()]), '',
         '## 5. Historical statements left unsupported', '',
         'Named in DESIGN-r6.md sec. 32 and LANDING-MANIFEST.md sec. 4 (%d rows): %s.' % (
             len(HS_ROWS), '; '.join(w for w, _ in HS_ROWS)), '',
         'Passages found by the scan and excluded, with the reason: %s; and every row of the obligation table and the adoption '
         'trace of sec. 32 (a classification, not a statement of content).' % '; '.join('%s (%s)' % kv for kv in EXCLUDE.items()), '',
         '## 6. Outputs', '', md_table(['File', 'sha256'], list(hashes.items())), '',
         'EXPECTATIONS.json, REQUIREMENTS.json, PARAPHRASED-DECISIONS.md, REVIEW-r6-round3.md, MIGRATION.json, '
         'V4-COMPARISON.md and REVIEW-r6-round2.md are written unchanged; `%s` is written byte-exact. The generator re-runs '
         'itself in a separate process and writes only if every output\'s sha256 is equal.' % EC_PATH, '',
         '## 7. Before adoption', '',
         '- One focused independent review of this revision (%s, item 2).' % OD5,
         '- The landing: the owner-approved merge of the files of LANDING-MANIFEST.md sec. 1, keeping the branch history '
         '(AGENTS.md sec. A.50 item 1); the statements of its sec. 4 land named as unsupported.',
         '- Design adoption: a separate owner approval.', '']
    return '\n'.join(L)


CONTENT['CORRECTION-REPORT-round5.md'] = report()

# =====================================================================================================
# hygiene, reproducibility, write
# =====================================================================================================
ALLOWED = set(ch for c in [x.decode('utf-8') for x in R4.values()] + [DEC5_BODY, REV5_BODY] for ch in c if ord(ch) > 127)
BAD_SP = re.compile('[\\u00a0\\u1680\\u2000-\\u200b\\u202f\\u205f\\u3000\\ufeff]')
LONG_URL = re.compile(r'https?://github\.com/\S{60,}')
AT, TMP, HOME, SCR = chr(64), '/' + 'tmp', '/' + 'home', 'scratch' + 'pad'  # built, so this file carries none of them
for n, c in CONTENT.items():
    if n in (EC_PATH, 'MIGRATION.json', 'V4-COMPARISON.md', 'REVIEW-r6-round2.md'):
        continue
    for what, bad in ((AT, AT in c), (TMP, TMP in c), (HOME, HOME in c), (SCR, SCR in c),
                      ('session id', 'session_0' in c), ('github.com', 'github.com' in c), ('CR', '\r' in c),
                      ('format character', any(unicodedata.category(ch) == 'Cf' for ch in c)),
                      ('non-ASCII space', bool(BAD_SP.search(c))), ('long github URL', bool(LONG_URL.search(c))),
                      ('non-ASCII character outside inputs', bool(set(ch for ch in c if ord(ch) > 127) - ALLOWED))):
        if bad:
            PROBLEMS.append('hygiene: %s in %s' % (what, n))
HASHES = collections.OrderedDict((n, sha(c)) for n, c in CONTENT.items())
if '--hashes' in sys.argv:
    print(json.dumps(HASHES))
    sys.exit(0)
if PROBLEMS:
    for p in PROBLEMS:
        print('PROBLEM', p)
    sys.exit(1)
import subprocess  # noqa: E402
rerun = subprocess.run([sys.executable, '-I', '-B', os.path.abspath(__file__), '--hashes'], capture_output=True, text=True, cwd=HERE)
if rerun.returncode != 0 or json.loads(rerun.stdout) != HASHES:
    print('REPRODUCIBILITY FAILURE', rerun.stdout[-2000:], rerun.stderr[-2000:])
    sys.exit(1)
for n, c in CONTENT.items():
    dst = os.path.join(OUT, n)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(c.encode('utf-8'))
for n in CONTENT:
    print(n, HASHES[n])
for k in VAL_AFTER:
    print('VALUE', k, VAL_BEFORE[k], '->', VAL_AFTER[k])

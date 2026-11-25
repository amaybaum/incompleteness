#!/usr/bin/env python3
"""Final text-only revision of design r6, round 4: owner decisions A1-A5 of 2026-11-25 on the round-3 delta review.

Reads, read only: out-final4/ (the round-3 outputs, byte-identical to the directory
verification/audits/foundations/a1exit-design-r6-20261125/ at commit c33d5b71, with generator-round3 as
out-final4/build/), c33/ (byte copies of the directory's other files at c33d5b71) and build/inputs/ beside this
file (the directory's tree at c33d5b71 as read with a GET request, the owner decisions A1-A5 as relayed verbatim,
and the round-3 delta review text).  Every file read from out-final4/ or c33/ is checked against its git blob id
at c33d5b71.  Writes out-final5/.  Every change is a logged edit tagged with the owner decision it applies (A1-A5,
CLOSE for the owner's closing direction, NIT for the R6.TREE.19 clarifications) or `meta` for a mechanical
consequence.  The round-3 self-checks (run_checks, restated from generator-round3/correct3.py by extracting its
source) run on the round-3 outputs ("before") and on the outputs ("after").  The generator re-runs itself in a
separate process and compares every output's sha256 before writing.
"""
import ast
import collections
import copy
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
IN = os.path.join(R6, 'out-final4')
C33 = os.path.join(R6, 'c33')
INP = os.path.join(HERE, 'inputs')
DIRPATH = 'verification/audits/foundations/a1exit-design-r6-20261125'


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


def dumps(o):
    return json.dumps(o, indent=1, ensure_ascii=True) + '\n'


PROBLEMS = []
LOG = []


def log(dec, target, desc):
    LOG.append((dec, target, desc))


# =====================================================================================================
# inputs, checked against the directory's git blob ids at c33d5b71
# =====================================================================================================
TREE = rj(rd(os.path.join(INP, 'tree-c33d5b71.json')))
BLOB = collections.OrderedDict((f['path'], f['blob']) for f in TREE['files'])
OUT4 = {'AUTHORIZATIONS.md', 'CORRECTION-REPORT-round3.md', 'CORRECTION-REPORT.md', 'DESIGN-r6.md',
        'EXPECTATIONS.json', 'FRESH-AUTHORIZATION.md', 'MIGRATION.json', 'PARAPHRASED-DECISIONS.md',
        'REQUIREMENTS.json', 'REVIEW-r6-round2.md', 'V4-COMPARISON.md'}
G3 = {'generator-round3/correct3.py': 'build/correct3.py',
      'generator-round3/comments-round3.json': 'build/inputs/comments-round3.json',
      'generator-round3/review-r6-round2.md': 'build/inputs/review-r6-round2.md'}


def local(p):
    if p in OUT4:
        return os.path.join(IN, p)
    if p in G3:
        return os.path.join(IN, G3[p])
    return os.path.join(C33, p)


SRC = collections.OrderedDict()
for p, b in BLOB.items():
    data = rdb(local(p))
    if gitblob(data) != b:
        PROBLEMS.append('input %s does not match its git blob %s' % (p, b))
    SRC[p] = data
if len(BLOB) != 37:
    PROBLEMS.append('tree listing: %d files, expected 37' % len(BLOB))
INPUT_SHA = [('build/inputs/' + n, sha(rdb(os.path.join(INP, n)))) for n in
             ('tree-c33d5b71.json', 'owner-decisions-A1-A5.json', 'review-r6-round3.md', 'records-1169.json')]
S = lambda p: SRC[p].decode('utf-8')

T_IN = S('DESIGN-r6.md')
T = T_IN
EXP_TXT = S('EXPECTATIONS.json')
EXP = rj(EXP_TXT)
REQ_TXT = S('REQUIREMENTS.json')
REQ_IN = rj(REQ_TXT)
PARA_TXT = S('PARAPHRASED-DECISIONS.md')
AUTH_TXT = S('AUTHORIZATIONS.md')
FRESH_TXT = S('FRESH-AUTHORIZATION.md')
MAPPING = rj(S('MAPPING.json'))
INVENTORY = rj(S('INVENTORY.json'))
COMM = rj(S('generator-round2/comments-1169.json'))
COMM3 = rj(S('generator-round3/comments-round3.json'))
OD_FILE = rj(rd(os.path.join(INP, 'owner-decisions-A1-A5.json')))
OD = OD_FILE['decisions']
REV3 = rd(os.path.join(INP, 'review-r6-round3.md'))
REC = rj(rd(os.path.join(INP, 'records-1169.json')))  # #1169 comments 7169906297 and 7169923380 (GET)
DEC4_ID, REV4_ID = '7169906297', '7169923380'
DEC4_AT, REV4_AT = REC[DEC4_ID]['created_at'], REC[REV4_ID]['created_at']
OWNER_MSG_AT = '2026-11-25T16:17:51Z'
if any(REC[c]['user']['login'] != 'amaybaum' for c in REC) or OWNER_MSG_AT not in REC[DEC4_ID]['body']:
    PROBLEMS.append('records-1169.json: unexpected author or owner message time')
for _k, _v in OD.items():
    for _s in re.split(r'(?<=\.) ', _v.split(' | ', 1)[-1]):
        if _k != 'objective' and _s not in REC[DEC4_ID]['body']:
            PROBLEMS.append('decision %s: sentence not in comment %s: %r' % (_k, DEC4_ID, _s[:60]))
if REV3 not in REC[REV4_ID]['body']:
    PROBLEMS.append('round-3 review text not verbatim in comment ' + REV4_ID)

# =====================================================================================================
# helpers and self-checks restated from generator-round3/correct3.py (source extracted, not re-typed)
# =====================================================================================================
C3_SRC = S('generator-round3/correct3.py')
_mod = ast.parse(C3_SRC)
_segs = []
for node in _mod.body:
    if isinstance(node, ast.FunctionDef) and node.name in ('block_span', 'block', 'parse_list', 'parse_reqs', 'run_checks', 'bq'):
        _segs.append(ast.get_source_segment(C3_SRC, node))
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in ('BLOCK_END', 'REQ_RE', 'PEND3') for t in node.targets):
        _segs.append(ast.get_source_segment(C3_SRC, node))
NS = {'re': re, 'collections': collections, 'PROBLEMS': PROBLEMS, 'MAPPING': MAPPING, 'dumps': dumps, 'T': ''}
exec(compile('\n\n'.join(_segs), 'correct3-extract', 'exec'), NS)
if len(_segs) != 9:
    PROBLEMS.append('correct3 extraction: %d segments, expected 9' % len(_segs))
PEND3 = NS['PEND3']
bq = NS['bq']
parse_reqs = NS['parse_reqs']
run_checks = NS['run_checks']


def block_span(rid, text=None):
    return NS['block_span'](rid, T if text is None else text)


def block(rid, text=None):
    return NS['block'](rid, T if text is None else text)


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
    a, b = block_span(rid)
    blk = T[a:b]
    if blk.count(old) != 1:
        PROBLEMS.append('bedit %s/%s: %d occurrences of %r' % (dec, rid, blk.count(old), old[:90]))
        return
    T = T[:a] + blk.replace(old, new) + T[b:]
    log(dec, rid, desc)


def sedit(dec, name, text, old, new, count=1):
    n = text.count(old)
    if n != count:
        PROBLEMS.append('edit %s/%s: expected %d occurrence(s), found %d: %r' % (dec, name, count, n, old[:90]))
        return text
    log(dec, name, 'text edit (%d occurrence(s))' % count)
    return text.replace(old, new)


# =====================================================================================================
# the owner's decisions, as relayed verbatim
# =====================================================================================================
for k, frag in (('A1', 'Defer TR45-opB, TR45-opC, TR45 and OBL-17 together.'),
                ('A2', 'Correct both flags to "candidate evidence only, not acceptance support".'),
                ('A3-wording', 'The execution-exception route recorded in comment 7092885251 is superseded.'),
                ('A4', 'Confirm all 53 identified requirements'), ('A5', 'Classify every off-main reference individually.'),
                ('closing', 'including the R6.TREE.12 correction')):
    if frag not in OD.get(k, ''):
        PROBLEMS.append('owner decision %s: expected text missing' % k)
body = lambda k: OD[k].split(' | ', 1)[1]
OWNER_AT = 'amaybaum, coordinating session'
AREF = 'owner decision %s of 2026-11-25 (sec. 0.1)'
CONF_A4 = ('Confirmed by owner decision A4 of 2026-11-25 (sec. 0.1), within the reviewed r6 scope and subject to '
           'previously approved deferrals.')
OWN_REC = 'owner decisions A1-A5 of 2026-11-25 (amaybaum, coordinating session; #1169 comment %s)' % DEC4_ID

REQ_IDX_IN = collections.OrderedDict((q['id'], q) for q in REQ_IN)
PEND50 = [q['id'] for q in REQ_IN if q['pending_owner_confirmation']]
EXTRA3 = ['R6.OUT.5', 'R6.OUT.18', 'R6.DELEG.8']
A4SET = PEND50 + EXTRA3
if len(PEND50) != 50 or len(set(A4SET)) != 53:
    PROBLEMS.append('A4: %d pending, %d identified' % (len(PEND50), len(set(A4SET))))

# =====================================================================================================
# A1: TR45-opB, TR45-opC, TR45 and OBL-17 deferred with R6.OUT.15
# =====================================================================================================
bedit('A1', 'R6.OUT.15', 'together with the `replay` mode of R6.REC.24 and control TR45-opB.',
      'together with the `replay` mode of R6.REC.24; owner decision A1 of 2026-11-25 (sec. 0.1) defers with it the '
      'controls TR45-opB, TR45-opC and TR45 and the obligation OBL-17, and the A1 retirement does not depend on them.',
      'deferral extended to TR45-opC, TR45 and OBL-17')
bedit('A1', 'OBL-17',
      'snapshot\'s delegated evidence is a NOT RUN row, TR45-opC, with the release condition "delegated evidence\n'
      'recorded by native runs at `X` and `C`". Gates: the A1 retirement execution. Discharged by: TR45-opC\n'
      'run and PASS.',
      'snapshot\'s delegated evidence is the row TR45-opC. Deferred by owner decision A1 of 2026-11-25\n'
      '(sec. 0.1), together with R6.OUT.15, TR45-opB and TR45: the row is recorded NOT RUN with the deferral as\n'
      'its reason (R6.GATE.15), and the A1 retirement does not depend on it. Gates: none while deferred.\n'
      'Discharged by: TR45-opC run and PASS, once a recorded owner decision takes up R6.OUT.15.',
      'deferred; gates no step while deferred')
edit('A1', 'sec. 32 table', '| OBL-17 | the A1 retirement execution | 4 | no cycle |',
     '| OBL-17 | none while deferred (owner decision A1 of 2026-11-25) | 4 | no cycle |')
bedit('A1', 'R6.GATE.15', 'admit NOT RUN are RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch.',
      'admit NOT RUN are RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opB, TR45-opC and EI14-dispatch.', 'TR45-opB admits NOT RUN')
bedit('A1', 'R6.GATE.15', 'The composites TR45 and EI14 are NOT RUN by inheritance while their component is (R6.GATE.9).',
      'The composites TR45 and EI14 are NOT RUN by inheritance while their component is (R6.GATE.9).\n'
      'TR45-opB and TR45-opC are deferred with R6.OUT.15 (owner decision A1 of 2026-11-25, sec. 0.1): the runner\n'
      'records them NOT RUN, their `not_run` reason is the deferral, their release check is false until an\n'
      'owner-approved expectation change takes up R6.OUT.15, and the A1 retirement does not depend on them.',
      'deferred rows stated')
bedit('A1', 'R6.CTRL.5', 'G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch, and, by inheritance',
      'G-A1, RT-L2, RT-O9-L2, TR45-opB, TR45-opC and EI14-dispatch, and, by inheritance', 'TR45-opB admits NOT RUN')
bedit('A1', 'R6.CTRL.17', 'TR45\'s op-C half is the row TR45-opC, NOT RUN until delegated evidence is\n'
      'recorded by native runs at `X` and `C`.',
      'TR45\'s op-C half is the row TR45-opC; it and TR45-opB are\n'
      'deferred with R6.OUT.15 and recorded NOT RUN (owner decision A1 of 2026-11-25; R6.GATE.15).', 'TR45-opC deferred')
bedit('A1', 'R6.GATE.9', 'TR45 (component\nTR45-opC) and EI14 (component EI14-dispatch) are such composites.',
      'TR45 (components\nTR45-opB and TR45-opC, both deferred) and EI14 (component EI14-dispatch) are such composites.',
      'TR45 components named')
for rid in ('TR45-opB', 'TR45-opC', 'TR45'):
    m = re.search(r'^\| %s \| .* \|$' % re.escape(rid), T[T.index('**Table 17.1.'):T.index('**Table 17.2.')], re.M)
    if not m:
        PROBLEMS.append('Table 17.1 row %s not found' % rid)
        continue
    line = m.group(0)
    edit('A1', 'Table 17.1 ' + rid, line + '\n', line[:-2] + '; deferred with R6.OUT.15 (owner decision A1 of 2026-11-25), recorded NOT RUN |\n')
edit('A1', 'OBL-28', 'TR52-consumer, TR45-opC and S11-7 | each implemented; `missing-id` until then |',
     'TR52-consumer and S11-7 | each implemented; `missing-id` until then; TR45-opC is deferred with R6.OUT.15 and '
     'recorded NOT RUN (owner decision A1 of 2026-11-25) |')
edit('A1', 'sec. 0.1 decision 1',
     ' The expectation file keeps the rows TR45-opB and TR45 (a composite of TR45-opB and TR45-opC) unchanged in this '
     'text-only revision; how the deferred row is carried in the expectation file is a matter for the delta review and '
     'a later owner-approved expectation change.',
     ' Owner decision A1 (below) defers TR45-opB, TR45-opC, TR45 and OBL-17 with it.')

# =====================================================================================================
# A3: R6.STAT.8 satisfied by the owner's restatement
# =====================================================================================================
bedit('A3', 'R6.STAT.8', 'since the comment holds no owner words, the owner restates it.',
      'since the comment holds no owner words, the owner restates it. The owner\'s restatement is owner decision A3\n'
      'of 2026-11-25, quoted byte-exact in sec. 0.1, which satisfies this condition.', 'restatement given (A3)')
edit('A3', 'sec. 0.1 decision 5', 'R6.STAT.8 is confirmed as a requirement; the restatement of the landing-order decision in '
     'the owner\'s words, which it requires before adoption, is still owed.',
     'R6.STAT.8 is confirmed as a requirement; the restatement of the landing-order decision in the owner\'s words, which '
     'it requires before adoption, is owner decision A3.')

# =====================================================================================================
# A4: the 53 identified requirements confirmed
# =====================================================================================================
for rid in PEND50:
    bedit('A4', rid, PEND3, CONF_A4, 'pending mark replaced: confirmed (A4)')
for rid in EXTRA3:
    a, b = block_span(rid)
    blk = T[a:b]
    i = blk.rfind('\nSources:')
    if i < 0:
        PROBLEMS.append('A4: no Sources line in ' + rid)
        continue
    T = T[:a] + blk[:i] + '\n' + CONF_A4 + blk[i:] + T[b:]
    log('A4', rid, 'confirmed (A4; named by the round-3 delta review, F3)')
edit('A4', 'sec. 0.1 decision 5',
     'and not confirmed by decision 1 are marked "%s" (FRESH-AUTHORIZATION.md, sec. 3); r6\'s adoption is not used as '
     'their authorization.' % PEND3,
     'and not confirmed by decision 1 are identified in FRESH-AUTHORIZATION.md, sec. 3, and confirmed by owner decision '
     'A4; r6\'s adoption is not used as their authorization.')

# =====================================================================================================
# CLOSE: the R6.TREE.12 correction; NIT: R6.TREE.19 clarifications (a)-(c) of the round-3 delta review
# =====================================================================================================
bedit('CLOSE', 'R6.TREE.12', 'Until that procedure has passed its independent review (the\n'
      '    delta review of owner decision 4) and r6 is adopted, the path is REVIEW_REQUIRED for every candidate\n'
      '    `L` (LC-7);',
      'Until LC-7\'s cases are restated by an owner-approved expectation change, the path is\n'
      '    REVIEW_REQUIRED for every candidate `L` (LC-7);', 'condition: until LC-7\'s cases are restated')
edit('CLOSE', 'Table 17.1 LC-7', 'REVIEW_REQUIRED for every candidate `L` until a regeneration verification procedure is '
     'specified and independently reviewed (expected landing blob open, RE-18, OC-4) |',
     'REVIEW_REQUIRED for every candidate `L` until LC-7\'s cases are restated by an owner-approved expectation change '
     '(R6.TREE.19; expected landing blob open, RE-18, OC-4) |')
edit('CLOSE', 'sec. 0.1 decision 4', '(ii) The regeneration and byte-comparison procedure is R6.TREE.19, for the delta '
     'review; LC-7 stays REVIEW_REQUIRED until that review accepts it.',
     '(ii) The regeneration and byte-comparison procedure is R6.TREE.19, accepted by the round-3 delta review; LC-7 stays '
     'REVIEW_REQUIRED until its cases are restated by an owner-approved expectation change (R6.TREE.12).')
bedit('CLOSE', 'R6.TREE.19', 'For the delta review: this procedure is specified for the independent review that\n'
      'owner decision 4 requires. Until that review accepts it and r6 is adopted, R6.TREE.12 keeps the\n'
      'derived-artifact case REVIEW_REQUIRED, and LC-7\'s expectation is unchanged.',
      'The round-3 delta review (REVIEW-r6-round3.md) accepted this procedure with three\n'
      'clarifications, stated below. Until LC-7\'s cases are restated by an owner-approved expectation change,\n'
      'R6.TREE.12 keeps the derived-artifact case REVIEW_REQUIRED.', 'status after the round-3 delta review')
bedit('NIT', 'R6.TREE.19', '- Regeneration. The checker is the one committed on `main` and pinned by the configuration at `F` for\n'
      '  `p`\'s class under the delegation contract (sec. 13). The tool runs it itself',
      '- Regeneration. The program is a generator, not a verifier: the generator and command, committed on\n'
      '  `main`, that the delegation contract pinned at `F` names for `p`\'s class (sec. 13); a class that names\n'
      '  none leaves `p` REVIEW_REQUIRED `delegated-evidence-missing`. The tool runs it itself',
      'nit (a): generator, not checker')
bedit('NIT', 'R6.TREE.19', '  reader (R6.REC.17); this run alone establishes the expected bytes. No file, output, log or claim of\n'
      '  regeneration supplied by the evaluated tree or by the caller is an input.\n',
      '  reader (R6.REC.17); this run alone establishes the expected bytes. No file, output, log or claim of\n'
      '  regeneration supplied by the evaluated tree or by the caller is an input.\n'
      '- Isolation. The run uses the execution isolation of R6.DELEG.3 (its own disposable clone, no network\n'
      '  access, a fixed environment, `python3 -I -B`, writes only to `p`). Its failure classes are this\n'
      '  requirement\'s, not R6.DELEG.3\'s: it decides the derived-artifact case of R6.TREE.12 at `L` (obligation\n'
      '  `MAIN`), whose undecided state is REVIEW_REQUIRED `delegated-evidence-missing` (LC-7).\n',
      'nit (b): R6.DELEG.3 isolation cited; failure classes explained')
bedit('NIT', 'R6.TREE.19', '- Comparison. The bytes the checker writes', '- Comparison. The bytes the generator writes', 'nit (a)')
bedit('NIT', 'R6.TREE.19', 'records the checker blob sha256', 'records the generator blob sha256', 'nit (a)')
bedit('NIT', 'R6.TREE.19', 'A checker that cannot run', 'A generator that cannot run', 'nit (a)')
bedit('NIT', 'R6.TREE.19', '  log or a host attestation never stands in for the comparison.\n',
      '  log or a host attestation never stands in for the comparison. A generator whose output is not\n'
      '  byte-deterministic (for example a PDF build) yields FAIL for every such `p`; that FAIL is fail-closed,\n'
      '  and such a class is not discharged by this procedure.\n', 'nit (c): consequence for non-deterministic generators')
bedit('CLOSE', 'R6.TREE.19', 'Controls: none (procedure for the delta review; once it is accepted, LC-7\'s cases\n'
      'are restated by an owner-approved expectation change).',
      'Controls: none (procedure; LC-7\'s cases are restated by an owner-approved expectation\nchange).', 'controls note')

# =====================================================================================================
# R6.STAT.10 and the adoption trace: the round-3 review, this revision's delta review, the landing manifest
# =====================================================================================================
bedit('A5', 'R6.STAT.10', 'Before\n  adoption, one bounded delta review covers the changes of this revision (owner decision 5); with the\n'
      '  documents, it is part of the adoption\'s support.',
      'The\n  delta review of the round-3 revision is recorded in REVIEW-r6-round3.md, and the owner\'s decisions A1 to\n'
      '  A5 on it are quoted in sec. 0.1. Before adoption, one short independent delta review covers the changes\n'
      '  of the round-4 revision; with the documents and the earlier reviews, it is part of the adoption\'s\n'
      '  support. The files that land are listed in LANDING-MANIFEST.md (owner decision A5).', 'reviews and landing manifest')
edit('A5', 'sec. 32 adoption trace', '#1169 comment 7166666428 and REVIEW-r6-round2.md; the delta review of this revision)',
     '#1169 comment 7166666428 and REVIEW-r6-round2.md; the round-3 delta review, REVIEW-r6-round3.md; the delta '
     'review of the round-4 revision)')
edit('A5', 'sec. 32 adoption trace', 'and the owner decisions 1 to 5 of 2026-11-25, quoted in the owner\'s words in #1169 '
     'comment 7166844576 (sec. 0.1) |',
     'and the owner decisions 1 to 5 of 2026-11-25, quoted in the owner\'s words in #1169 comment 7166844576, and A1 to A5 '
     'of 2026-11-25 (sec. 0.1; #1169 comment %s) |' % DEC4_ID)
edit('meta', 'sec. 0.1', '- One bounded delta review covers the changes of this revision before adoption (R6.STAT.10).\n',
     '')

# ---- sec. 0.1: the decisions A1-A5 quoted byte-exact, and how r6 applies them
QUOTED = '\n>\n'.join(bq(OD[k]) for k in ('A1', 'A2', 'A3', 'A3-wording', 'A4', 'A5', 'closing'))
A_SEC = '\n'.join([
    '',
    'The owner (amaybaum) decided on the round-3 delta review (REVIEW-r6-round3.md) in the coordinating session on '
    '2026-11-25 (owner message of %s), recorded at #1169 comment %s (%s); every sentence quoted below occurs verbatim '
    'in that record. Decisions A1 to A5 and the closing direction, byte-exact as relayed (each line prefixed by "> "):'
    % (OWNER_MSG_AT, DEC4_ID, DEC4_AT), '', QUOTED, '',
    'How r6 applies them; each takes effect only with r6\'s adoption (R6.STAT.1):', '',
    '- Decision A1. TR45-opB, TR45-opC, their composite TR45 and OBL-17 are deferred with R6.OUT.15. The expectation file '
    'carries each deferred row in the form R6.GATE.2 and R6.GATE.15 permit for a row that is not run: `status_allowed` '
    'admits NOT RUN and `not_run` records the deferral as its reason, with the release condition that a recorded owner '
    'decision takes up R6.OUT.15 and a release check that is false until an owner-approved expectation change replaces the '
    'entry; `expect` and `restored` are kept as the deferred specification. An admitted NOT RUN does not fail the gate '
    '(R6.GATE.9) and meets the acceptance list (R6.GATE.11), so neither the tool\'s acceptance nor the A1 retirement '
    'depends on the deferred rows. Outcome DEFERRED is not used: R6.GATE.9\'s `deferred-expectation` never holds, so the '
    'gate would depend on the deferral. Moving the ids to `retired` is not used: a retired id is never reused (sec. 34), '
    'while the specification is kept. OBL-17 gates no step while deferred.',
    '- Decision A2. The two flags of item11-T1p read "candidate evidence only, not acceptance support"; its expectation is '
    'unchanged (OBL-23).',
    '- Decision A3. The owner\'s restatement quoted above is the wording R6.STAT.8 requires before adoption; R6.STAT.8 is '
    'satisfied by it.',
    '- Decision A4. The 53 identified requirements, the 50 found to rest on S1-D3 by the rules of FRESH-AUTHORIZATION.md, '
    'sec. 3, and R6.OUT.5, R6.OUT.18 and R6.DELEG.8, which the round-3 delta review named (F3), carry "Confirmed by owner '
    'decision A4", within the reviewed r6 scope and subject to previously approved deferrals; the confirmation does not '
    'extend to requirements that were not identified.',
    '- Decision A5. LANDING-MANIFEST.md lists the files of this directory that land and those left to Git history, and '
    'classifies each reference of the landed files to content not on `main` (AGENTS.md sec. A.42 item 8).',
    '- The R6.TREE.12 correction: the derived-artifact case stays REVIEW_REQUIRED until LC-7\'s cases are restated by an '
    'owner-approved expectation change. One short independent delta review covers this revision before adoption '
    '(R6.STAT.10).', ''])
_i = T.index('## 0.1 Owner decisions of 2026-11-25') if False else T.index('### 0.1 Owner decisions of 2026-11-25')
_j = T.index('\n***\n', _i)
T = T[:_j] + '\n' + A_SEC + T[_j:]
log('A1-A5', 'sec. 0.1', 'owner decisions A1-A5 quoted byte-exact, with how r6 applies them')
# no blank-line doubling at the junction
T = T.replace('(R6.STAT.5). R6.STAT.8 is confirmed as a requirement; the restatement of the landing-order decision in the owner\'s words, which it requires before adoption, is owner decision A3.\n\n\nThe owner decided',
              '(R6.STAT.5). R6.STAT.8 is confirmed as a requirement; the restatement of the landing-order decision in the owner\'s words, which it requires before adoption, is owner decision A3.\n\nThe owner decided')

# =====================================================================================================
# REQUIREMENTS.json: the index, kept equal to the text
# =====================================================================================================
REQ_OUT = copy.deepcopy(REQ_IN)
ROUT = collections.OrderedDict((q['id'], q) for q in REQ_OUT)


def od(dec, effect, basis):
    return collections.OrderedDict([('record', OWN_REC), ('decision', dec), ('effect', effect), ('decision_basis', basis)])


for rid in A4SET:
    ROUT[rid]['pending_owner_confirmation'] = []
    ROUT[rid]['owner_decision'].append(od('A4', 'confirmed within the reviewed r6 scope and subject to previously approved deferrals',
                                          ['round-3 delta review, F3'] if rid in EXTRA3 else ['S1-D3 identification, rules A to C (FRESH-AUTHORIZATION.md, sec. 3)']))
ROUT['R6.STAT.8']['owner_decision'].append(od('A3', 'landing-order decision restated in the owner\'s words (DESIGN-r6.md sec. 0.1)', ['R6.STAT.8 (RE-26)']))
ROUT['R6.OUT.15']['owner_decision'].append(od('A1', 'deferral extended to TR45-opC, TR45 and OBL-17', ['round-3 delta review, F1']))
ROUT['OBL-17']['owner_decision'].append(od('A1', 'deferred', ['round-3 delta review, F1']))
log('A4', 'REQUIREMENTS.json', '53 entries: pending key removed, owner decision A4 recorded')
log('A3', 'REQUIREMENTS.json', 'R6.STAT.8: owner decision A3 recorded')
log('A1', 'REQUIREMENTS.json', 'R6.OUT.15 and OBL-17: owner decision A1 recorded')
REQ_OUT_TXT = dumps(REQ_OUT)

# =====================================================================================================
# EXPECTATIONS.json: A1 (three rows recorded NOT RUN with the deferral) and A2 (two flags of item11-T1p)
# =====================================================================================================
EXP_OUT = copy.deepcopy(EXP)
EXP_OUT['record_id'] = 'r6-final5-1'
log('meta', 'EXPECTATIONS.json', 'record_id r6-final4-1 -> r6-final5-1')
EIDX = collections.OrderedDict((r['id'], r) for r in EXP_OUT['rows'])
DEF_NR = collections.OrderedDict([
    ('reason', 'deferred by owner decision A1 of 2026-11-25 (DESIGN-r6.md sec. 0.1), with R6.OUT.15 and OBL-17; the A1 '
               'retirement does not depend on this row'),
    ('release_condition', 'a recorded owner decision takes up R6.OUT.15'),
    ('release_check', 'false until an owner-approved expectation change replaces this entry')])
DEF_FLAG = ('deferred by owner decision A1 of 2026-11-25: recorded NOT RUN; expect and restored kept as the deferred '
            'specification (R6.OUT.15, R6.GATE.15)')
_b = EIDX['TR45-opB']
_new = collections.OrderedDict()
for k, v in _b.items():
    if k == 'source':
        _new['status_allowed'] = ['PASS', 'NOT RUN']
        _new['not_run'] = copy.deepcopy(DEF_NR)
    _new[k] = v
_new['flags'] = [DEF_FLAG]
_b.clear()
_b.update(_new)
log('A1', 'TR45-opB', 'NOT RUN admitted with the deferral as reason; flag added; expect and restored unchanged')
_c = EIDX['TR45-opC']
_c['not_run'] = copy.deepcopy(DEF_NR)
if _c['flags'] != ['named blocker (Q10): unexecuted control half']:
    PROBLEMS.append('TR45-opC flags unexpected')
_c['flags'] = [DEF_FLAG]
log('A1', 'TR45-opC', 'not_run: the deferral replaces the evidence release condition; flag "named blocker" replaced')
_t = EIDX['TR45']
_t['not_run'] = collections.OrderedDict([
    ('reason', 'components TR45-opB and TR45-opC are NOT RUN, deferred by owner decision A1 of 2026-11-25 (DESIGN-r6.md '
               'sec. 0.1); a composite is NOT RUN while any component is an admitted NOT RUN and none is FAIL or ERROR (Q14)'),
    ('release_condition', DEF_NR['release_condition']), ('release_check', DEF_NR['release_check'])])
_t['flags'] = _t['flags'] + [DEF_FLAG]
log('A1', 'TR45', 'not_run inherits the deferral; flag added')
_p = EIDX['item11-T1p']
F_OLD1 = 'inputs off main: acceptance reference only for runs with those pinned inputs (RD-23)'
F_NEW1 = 'inputs off main: candidate evidence only, not acceptance support (owner decision A2 of 2026-11-25; RD-23)'
F_OLD2_TAIL = ('the run on the exact tool candidate with X = T1\' is candidate evidence for the landing decision only; '
               'the enduring claim is a named provenance gap (OBL-23)')
F_NEW2_TAIL = ('the run on the exact tool candidate with X = T1\' is candidate evidence only, not acceptance support; no '
               'enduring claim rests on it (owner decision A2 of 2026-11-25; OBL-23)')
if _p['flags'][1] != F_OLD1 or not _p['flags'][2].endswith(F_OLD2_TAIL):
    PROBLEMS.append('item11-T1p flags unexpected')
else:
    _p['flags'][1] = F_NEW1
    _p['flags'][2] = _p['flags'][2][:-len(F_OLD2_TAIL)] + F_NEW2_TAIL
    log('A2', 'item11-T1p', 'the two flags corrected to "candidate evidence only, not acceptance support"; expect unchanged')
EXP_OUT_TXT = dumps(EXP_OUT)

# =====================================================================================================
# FRESH-AUTHORIZATION.md, PARAPHRASED-DECISIONS.md, AUTHORIZATIONS.md
# =====================================================================================================
REQS_IN = parse_reqs(T_IN)
REQS = parse_reqs(T)
CHANGED = [r for r in REQS_IN if REQS_IN[r]['text'] != REQS.get(r, {}).get('text')]
FRESH = FRESH_TXT
for rid in CHANGED:
    old, new = bq(block(rid, T_IN)), bq(block(rid, T))
    n = FRESH.count(old)
    if n:
        FRESH = FRESH.replace(old, new)
        log('meta', 'FRESH-AUTHORIZATION.md', 'quoted wording of %s regenerated (%d occurrence(s))' % (rid, n))
A4Q = body('A4')
FRESH = sedit('A4', 'FRESH-AUTHORIZATION.md', FRESH,
              'sec. 3 the requirements resting on owner decision S1-D3 (decision 5), which are pending owner confirmation for the adoption decision;',
              'sec. 3 the requirements resting on owner decision S1-D3 (decision 5), confirmed by owner decision A4 of 2026-11-25 '
              '(DESIGN-r6.md sec. 0.1) together with R6.OUT.5, R6.OUT.18 and R6.DELEG.8;')
FRESH = sedit('A4', 'FRESH-AUTHORIZATION.md', FRESH,
              '## 3. Requirements resting on owner decision S1-D3 (pending owner confirmation for the adoption decision)',
              '## 3. Requirements resting on owner decision S1-D3 (confirmed by owner decision A4)')
_d5 = FRESH.index('Owner decision 5, quoted: "However, do not use adoption')
_d5e = FRESH.index('\n', _d5)
FRESH = (FRESH[:_d5e] + '\n\nOwner decision A4 of 2026-11-25 (%s), quoted: "%s" The 53 identified requirements are the 50 '
         'listed below and R6.OUT.5, R6.OUT.18 and R6.DELEG.8, which the round-3 delta review (REVIEW-r6-round3.md, F3) '
         'named; each carries "Confirmed by owner decision A4" in DESIGN-r6.md. The identification is bounded by the rules '
         'below and by that review\'s sample.' % (OWNER_AT, A4Q) + FRESH[_d5e:])
log('A4', 'FRESH-AUTHORIZATION.md', 'sec. 3: owner decision A4 quoted')
FRESH = sedit('A4', 'FRESH-AUTHORIZATION.md', FRESH, 'Marked pending: 50.', 'Confirmed by owner decision A4: 50.')
FRESH = sedit('A4', 'FRESH-AUTHORIZATION.md', FRESH,
              'not confirmed; r6\'s adoption is not used as its authorization; pending owner confirmation for the adoption decision',
              'confirmed by owner decision A4 of 2026-11-25', count=50)
_rc = FRESH.index('\nFor each pending requirement the options are those of PARAPHRASED-DECISIONS.md')
_rce = FRESH.index('\n\n', _rc + 1)
FRESH = (FRESH[:_rc] + '\nNamed by the round-3 delta review (F3) and confirmed by owner decision A4:\n\n'
         '- R6.OUT.5: its `CONFIG_UNREVIEWED` branch, "not admitted from `F`\'s pin table", restates the B3 content.\n'
         '- R6.OUT.18: schema `/5` carries the admission snapshot, B1/B3 content.\n'
         '- R6.DELEG.8 (borderline): the local-run fallback that sends G4-G8 to CI.\n\n'
         'The wording of each requirement confirmed by owner decision A4, quoted mechanically from DESIGN-r6.md:'
         + FRESH[_rce:])
log('A4', 'FRESH-AUTHORIZATION.md', 'sec. 3: the three requirements named by the review; options paragraph replaced')
_s4 = FRESH.index('***\n\n## 4. Entries of sec. 1')
FRESH = FRESH[:_s4] + ''.join('### %s\n\n%s\n\n' % (r, bq(block(r))) for r in EXTRA3) + FRESH[_s4:]
log('A4', 'FRESH-AUTHORIZATION.md', 'sec. 3: wording of R6.OUT.5, R6.OUT.18 and R6.DELEG.8 added')
FRESH = sedit('A3', 'FRESH-AUTHORIZATION.md', FRESH,
              'which the requirement itself needs before adoption, is still owed.',
              'which the requirement itself needs before adoption, is owner decision A3 of 2026-11-25 (DESIGN-r6.md sec. 0.1).')
FRESH = sedit('A1', 'FRESH-AUTHORIZATION.md', FRESH,
              '- Deferral: with the `replay` mode of R6.REC.24 and control TR45-opB; accountable Issue #1169; the expectation '
              'rows TR45-opB and TR45 are unchanged in this revision (DESIGN-r6.md sec. 0.1).',
              '- Deferral: with the `replay` mode of R6.REC.24; owner decision A1 of 2026-11-25 defers with it TR45-opB, '
              'TR45-opC, TR45 and OBL-17, which the expectation file records NOT RUN with the deferral as reason; '
              'accountable Issue #1169 (DESIGN-r6.md sec. 0.1).')
PEND_LC = 'pending owner confirmation for the adoption decision (S1-D3)'
CONF_LC = 'confirmed by owner decision A4 of 2026-11-25'
NOTE_OLD = ('- Note: Identified under owner decision 5; marked "%s" except where decision 1 confirmed the requirement.' % PEND3)
NOTE_NEW = ('- Note: Identified under owner decision 5; confirmed by owner decision 1 or, for the others, by owner decision A4 '
            'of 2026-11-25, together with R6.OUT.5, R6.OUT.18 and R6.DELEG.8 (round-3 delta review, F3).')
PARA = sedit('A4', 'PARAPHRASED-DECISIONS.md', PARA_TXT, PEND_LC, CONF_LC, count=50)
PARA = sedit('A4', 'PARAPHRASED-DECISIONS.md', PARA, NOTE_OLD, NOTE_NEW)
PARA = sedit('A4', 'PARAPHRASED-DECISIONS.md', PARA, '50 requirements resting on S1-D3 are pending.',
             'the 50 requirements resting on S1-D3, with R6.OUT.5, R6.OUT.18 and R6.DELEG.8, are confirmed by owner decision '
             'A4 of 2026-11-25 (DESIGN-r6.md sec. 0.1); no requirement is pending.')
AUTH = sedit('A4', 'AUTHORIZATIONS.md', AUTH_TXT, PEND_LC, CONF_LC, count=50)
AUTH = sedit('A4', 'AUTHORIZATIONS.md', AUTH, NOTE_OLD, NOTE_NEW)
A_AUTH = '\n'.join([
    '### #1169 comment %s (%s): owner decisions A1 to A5 of 2026-11-25 on the round-3 delta review' % (DEC4_ID, DEC4_AT), '',
    '- Given by the owner (amaybaum) in the coordinating session (owner message of %s) and relayed verbatim to the writer '
    'of the round-4 revision; quoted byte-exact in DESIGN-r6.md sec. 0.1. Recorded at #1169 comment %s, in which every '
    'sentence quoted below occurs verbatim.' % (OWNER_MSG_AT, DEC4_ID), '',
    '\n>\n'.join(bq(OD[k]) for k in ('A1', 'A2', 'A3', 'A3-wording', 'A4', 'A5', 'closing')), '',
    '- Permits: deferring TR45-opB, TR45-opC, TR45 and OBL-17 and recording the three rows NOT RUN with the deferral (A1); '
    'correcting the two flags of item11-T1p (A2); the restatement R6.STAT.8 requires (A3); confirming the 53 identified '
    'requirements within the reviewed r6 scope (A4); the landing scope of LANDING-MANIFEST.md (A5); this bounded '
    'text-only revision with the R6.TREE.12 correction and one short independent delta review.',
    '- Does not permit: adoption, implementation, freezing, trials or merging, each of which keeps its own approval gate '
    '(AGENTS.md sec. A.50; A3); confirmation of requirements not identified (A4); reopening settled requirements or '
    'further features (closing direction); the execution-exception route of comment 7092885251 (A3).',
    '- Relied on by: R6.OUT.15, OBL-17, R6.GATE.15, R6.CTRL.5, R6.CTRL.17, R6.GATE.9 and the rows TR45-opB, TR45-opC and '
    'TR45 (A1); item11-T1p (A2); R6.STAT.8 (A3); the 53 confirmations (A4); LANDING-MANIFEST.md (A5); R6.TREE.12 and '
    'R6.TREE.19 (closing direction).', ''])
_a2 = AUTH.index('***\n\n## 2. Class (ii)')
AUTH = AUTH[:_a2] + A_AUTH + '\n' + AUTH[_a2:]
log('A1-A5', 'AUTHORIZATIONS.md', 'entry for owner decisions A1-A5 added to sec. 1')
AUTH = AUTH.rstrip('\n') + ('\n- REVIEW-r6-round3.md records the delta review of the round-3 revision (commit '
                            'c33d5b71a3e4e15028d19ff153afcee8f5aa90a3), reviewer text verbatim; recorded at #1169 comment %s (%s). '
                            'It is a review record, not an owner decision.\n' % (REV4_ID, REV4_AT))
log('A5', 'AUTHORIZATIONS.md', 'sec. 5: the round-3 delta review record')

# =====================================================================================================
# REVIEW-r6-round3.md
# =====================================================================================================
REV3_OUT = '\n'.join([
    '# Delta review of A1 design r6, round 3', '',
    '- Reviewer: a Claude reviewer agent launched by the coordinating session; it wrote none of the reviewed work and made '
    'no git or GitHub writes (as its Limitations section states).',
    '- Commit reviewed: c33d5b71a3e4e15028d19ff153afcee8f5aa90a3, parent 400e4b4fe5f3474b96ee4faa3c437e76e09db782 (this '
    'directory, %s/).' % DIRPATH,
    '- Date: 2026-11-25.',
    '- Record: #1169 comment %s (%s), which quotes the reviewer text verbatim. SHA-256 of the reviewer text below: %s.' % (REV4_ID, REV4_AT, sha(REV3)),
    '- Verdict: ACCEPT-WITH-NITS. The owner\'s decisions on it: owner decisions A1 to A5 of 2026-11-25 (DESIGN-r6.md '
    'sec. 0.1). Landing this file approves no merge (AGENTS.md sec. A.50 item 1).', '',
    'The reviewer text follows verbatim, between the two marker lines.', '',
    '---- reviewer text begins ----', '', REV3.rstrip('\n'), '', '---- reviewer text ends ----', ''])
_va = REV3_OUT.index('---- reviewer text begins ----\n\n') + len('---- reviewer text begins ----\n\n')
_vb = REV3_OUT.index('\n\n---- reviewer text ends ----')
REV3_OK = REV3_OUT[_va:_vb] == REV3
log('A5', 'REVIEW-r6-round3.md', 'review record: header and the reviewer text verbatim')

# =====================================================================================================
# LANDING-MANIFEST.md (A5)
# =====================================================================================================
GEN4 = collections.OrderedDict([
    ('generator-round4/correct4.py', rdb(os.path.abspath(__file__))),
    ('generator-round4/owner-decisions-A1-A5.json', rdb(os.path.join(INP, 'owner-decisions-A1-A5.json'))),
    ('generator-round4/review-r6-round3.md', rdb(os.path.join(INP, 'review-r6-round3.md'))),
    ('generator-round4/tree-c33d5b71.json', rdb(os.path.join(INP, 'tree-c33d5b71.json'))),
    ('generator-round4/records-1169.json', rdb(os.path.join(INP, 'records-1169.json')))])
NEWDOCS = collections.OrderedDict([
    ('DESIGN-r6.md', T), ('EXPECTATIONS.json', EXP_OUT_TXT), ('REQUIREMENTS.json', REQ_OUT_TXT),
    ('PARAPHRASED-DECISIONS.md', PARA), ('AUTHORIZATIONS.md', AUTH), ('FRESH-AUTHORIZATION.md', FRESH),
    ('REVIEW-r6-round3.md', REV3_OUT)])
ROLE = collections.OrderedDict([
    ('DESIGN-r6.md', 'final r6 document (the design)'), ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
    ('REQUIREMENTS.json', 'final r6 document (requirement index)'), ('MIGRATION.json', 'final r6 document (migration index)'),
    ('PARAPHRASED-DECISIONS.md', 'final r6 document (list of paraphrased decisions)'),
    ('AUTHORIZATIONS.md', 'final r6 document (decision records relied on)'),
    ('FRESH-AUTHORIZATION.md', 'final r6 document (requirement status and wording)'),
    ('V4-COMPARISON.md', 'final r6 document (cited by EXPECTATIONS.json and FRESH-AUTHORIZATION.md)'),
    ('REVIEW-r6-round2.md', 'review record (second correction round)'), ('REVIEW-r6-round3.md', 'review record (round-3 delta review)'),
    ('MAPPING.json', 'committed input of generators 2 to 4 (self-checks)'), ('INVENTORY.json', 'committed input of generator-round3'),
    ('PENDING-33.md', 'committed input of generator-round2 (correct2.py)')])
for p in BLOB:
    if p.startswith('generator-round2/'):
        ROLE[p] = 'round-2 generator'
    elif p.startswith('generator-round3/'):
        ROLE[p] = 'round-3 generator'
for p in GEN4:
    ROLE[p] = 'round-4 generator (produces the final documents; see sec. 1 note)'
LANDED = collections.OrderedDict()
for p in ROLE:
    if p in NEWDOCS:
        LANDED[p] = NEWDOCS[p].encode('utf-8')
    elif p in GEN4:
        LANDED[p] = GEN4[p]
    else:
        LANDED[p] = SRC[p]
DROPPED = collections.OrderedDict([
    ('CHECKS.txt', 'check output of an earlier drafting step'), ('CONFORMANCE.md', 'conformance assessment of the tool commit '
     'a3799244 (provenance for OBL-26; R6.STAT.10)'), ('CORRECTION-REPORT.md', 'earlier report (round 2)'),
    ('CORRECTION-REPORT-round3.md', 'earlier report (round 3)'), ('DECISIONS.md', 'decision package OD-1 to OD-31 (approved '
     'at 4e9a1501; provenance, R6.STAT.2)'), ('EXPECTATION-SOURCES.json', 'drafting input of the expectation file'),
    ('EXPECTATIONS-REPORT.md', 'earlier report'), ('EXPECTATIONS-draft.json', 'draft'), ('FINAL-REPORT.md', 'earlier report'),
    ('GATE-draft.md', 'draft'), ('INTEGRATION-REPORT.md', 'earlier report'), ('MAPPING-CHECK.txt', 'check output of an '
     'earlier drafting step'), ('OUTLINE.md', 'draft'), ('RE2-ROWS.md', 'drafting note'), ('RESIDUAL-2.md', 'decision package '
     'RE-1 to RE-38 (approved at f4e18558; provenance, R6.STAT.2)'), ('RESIDUAL.md', 'decision package RD-1 to RD-35 '
     '(approved at c1244459; provenance, R6.STAT.2)')])
_covered = set(p for p in LANDED if p in BLOB) | set(DROPPED)
if _covered != set(BLOB) or set(LANDED) & set(DROPPED):
    PROBLEMS.append('manifest: landed and dropped files do not partition the 37 files: %s' % sorted(set(BLOB) ^ _covered))

# ---- reference scan
SCAN = [p for p in LANDED if p != 'generator-round4/correct4.py']
SNAP = set(p for p in SCAN if p.startswith('generator-round') or p in ('INVENTORY.json', 'MAPPING.json', 'PENDING-33.md'))
PAT = collections.OrderedDict([
    ('hex40', r'(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])'),
    ('sha256', r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])'),
    ('short', r'(?<![0-9a-f])(?=[0-9a-f]*[a-f])(?=[0-9a-f]*[0-9])[0-9a-f]{7,12}(?![0-9a-f])'),
    ('comment', r'(?<!\d)7\d{9}(?!\d)'), ('number', r'#\d{3,5}\b'), ('run', r'(?<!\d)4\d{10}(?!\d)'),
    ('branch', r'\b(?:records|reconcile|ci)/[a-z0-9][a-z0-9.-]*-2026\d{4}\b|\bci/ledger-coverage-suite-[0-9a-f]{8}\b')])
FOUND = collections.OrderedDict()
for p in SCAN:
    t = LANDED[p].decode('utf-8')
    for kind, pat in PAT.items():
        for m in re.findall(pat, t):
            FOUND.setdefault((kind, m), set()).add(p)
H = 'on main once the landing merge keeps the branch history'
MAIN = 'on main'
OFF = 'not on main'
HOST = 'GitHub record'
NOOBJ = 'not an object in the repository'
SOM = 'support on main'
SOMH = 'support on main once the landing merge keeps the branch history (a merge commit or fast-forward, not a squash)'
PROV = 'provenance'
GIT = collections.OrderedDict()


def g(ident, names, status, cls):
    GIT[ident] = (names, status, cls)


for ident, n in (('e837e3dbaa605efc867a213f3345cee14c36d8f5', '`E`, the ledger pin (R6.NOTE.1)'),
                 ('53c6601a10419b6b333cc992474272501ab542af', '`H`, the scientific base (R6.NOTE.2)'),
                 ('413b0bb88f39cad901befcf4684355c7ee39480b', '`W` (R6.NOTE.5)'),
                 ('8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d', '`M` of the N10/N11 composition probe'),
                 ('9882df8f2d41eee47790560b0e22aac03e95370f', 'the commit at which the record tree `R` is stated'),
                 ('b05efdca935a42b9c94ef1748c964696bf58fcd9', 'the record tree `R` (a tree; also on main today)'),
                 ('ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf', 'the commit the sc42 class clone contains'),
                 ('3184c7f9075948d8474197eee03ba5b94ba85db5', 'tool commit of v6.0e implementation correction 1'),
                 ('e2e2a623265187a28ebec604ab8bcc672742888f', 'the v6.0e tool landing merge (main at drafting)'),
                 ('12a9281fb88c14395b6715a3bf4b4f6b030f433c', 'blob of AGENTS.md at `H`'),
                 ('6b1280fa92fa30e36555e9afd30cc0d6e992f5bb', 'blob of AGENTS.md at `M` (8e9b8334)'),
                 ('4d864dbd586cedd02f03cfe01b46db34f329d535', 'commit re-pinning controls.json (in a quoted comment)'),
                 ('4fb2c1eed350edf95da2b316abcca93717246589', 'merge commit (in a quoted comment)'),
                 ('0dba9faf3b0d82e450f3457c7144d68d5f3d3e68', 'merged head (in a quoted comment)')):
    g(ident, n, MAIN, SOM + ': the object is reachable from main, and every claim citing it reads it there')
for ident in ('0adc410c4ad8c3ff51fc77ebb2e055506d758fc8', '0ba358ccf05eb461c3a5bd686062f65115c293fc',
              '0cd5d5bfb4f6641c8b08706c4eb636ee730ebbf0', '1c7eedc402eafd2bac654484fa790874a33f444d',
              '4de2eabd6c7c88dc214db70a813ec44b8641b630', '7f28886f4cc96fbfa7407af1fdc37de2f0e562e5',
              'a1f38284d21338b66119c870a551a670c73e3fa7', 'f1c8c6b18b245c2faaa68abb464d70ab332b7bec',
              'fd9f99cc8866bd4f4244298f819fa99d5c707fba'):
    g(ident, 'base or merge commit of a pull request in `E..H` (sec. 5 tables, HIST-19)', MAIN,
      SOM + ': the site-change counts are read from these merges on main')
for ident, n in (('4e9a15010f7416978004a67049718ff8698ef170', 'branch commit holding DECISIONS.md as approved'),
                 ('c12444592cd3ece6794e3f9ffcc977a36ea412f3', 'branch commit holding RESIDUAL.md as approved'),
                 ('f4e185588711c8c6c42b6b203bbe8546da8ee6de', 'branch commit holding RESIDUAL-2.md as approved'),
                 ('a6b6884be7da56edc89fc93f2b557e9a6268e611', 'branch commit (finalized draft)'),
                 ('ad035ff513d61d94668b8fde86b7426fec6ef58f', 'round-1 outputs, input of generator-round2'),
                 ('400e4b4fe5f3474b96ee4faa3c437e76e09db782', 'round-2 outputs, input of generator-round3; reviewed by REVIEW-r6-round2.md'),
                 ('c33d5b71a3e4e15028d19ff153afcee8f5aa90a3', 'round-3 outputs, input of generator-round4; reviewed by REVIEW-r6-round3.md')):
    g(ident, n, H, SOMH + '; the claims citing it (owner approvals of a package at that commit, generator inputs, the '
      'reviewed commit) read its content there')
g('a37992449b452021001277c06c524a30c92dfb87', 'the tool commit (r5 corrections), branch ci/ledger-coverage-suite-a3799244', OFF,
  'in DESIGN-r6.md: ' + PROV + ' for OBL-26 and the runner cites (no requirement rests on it); ' + 'support off main for the '
  'statements of what the tool commit does (adoption trace, sec. 32), which adoption does not rely on (R6.STAT.10); in '
  'EXPECTATIONS.json (`runner`, `reference` keys) and MIGRATION.json: ' + PROV + '; in REVIEW-r6-round3.md: ' + PROV)
g('14ac71b4b0a0c0aa2d7068d6799a73f474097060', '`T1\'`, the executed trial tree (R6.NOTE.3)', OFF,
  'in DESIGN-r6.md: support off main for R6.NOTE.3\'s statement of its content (adoption trace), not relied on by '
  'adoption; in EXPECTATIONS.json `reference` keys: ' + PROV + ' (never compared, R6.GATE.9)')
g('4c79be642ca631573f06b444903be75ec4f5e2b6', '`P`, the frozen plan (R6.NOTE.4)', OFF,
  'support off main relied on by adoption: the semantics of R6.SPLIT.3, R6.PROF.3-5, 7-10, 12, R6.DENY.5, R6.A1CFG.2 and '
  'OBL-1 are defined by `P`\'s edits_check.py (adoption trace); open, see sec. 4')
g('68bab90e8f8c0cb060d318bfd17672833e3fe485', 'Stage A findings commit', OFF, PROV + ': cited as historical rationale (HIST)')
g('0fa0bc808cf70a05105c9dada7e407caba9b2ade', 'r5 amendment commit, branch reconcile/a1-amendment-20261125', OFF,
  PROV + ': occurs in the inventory and a quoted comment; r6 states r5\'s rules itself (R6.STAT.2)')
g('717159e2de7fe05adb8fc1d6bbf6bb14f00ca781', 'independent review of r2 (quoted in the inventory)', OFF, PROV)
g('9f4fc3e830707c90ffc105842d26d5b51f01760b', 'blob of `T1\'`\'s AGENTS.md', OFF,
  PROV + ' for adoption: a control input fixed by its bytes, which `X_rep` rebuilds from `H`, the ledger and the edit list '
  '(R6.EVID.8); support off main for the acceptance references until those inputs land with the tool revision')
g('ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e', 'blob of `P`\'s and `T1\'`\'s ledger.json', OFF,
  PROV + ' for adoption: a pin of an input that lands with the tool revision (R6.EVID.8); its content is needed by the '
  'tool\'s landing (OBL-13, OBL-14), not by adoption')
g('ec384fdfbc12937b860e2f226355e8c5d94820a5', 'blob of `P`\'s and `T1\'`\'s edits.json', OFF, GIT['ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e'][2])
g('86d79863821f3f8cdad86771008b2df89fd1961a', 'computed blob id of the N11 composition', NOOBJ,
  PROV + ': an expected value computed from on-main content (`M`\'s AGENTS.md and splice D296)')
g('e3edd9667d8801157c6d1074bb60d89dcd8ea458', 'blob of DESIGN-v5.2.md (records branch)', OFF,
  PROV + ': R6.SPLIT.1 restates the splitter verbatim; the blob names its origin')
for ident, n in (('1e3332edddc091f7952b80ef1c36a09e35d32b75', 'v1 DESIGN.md'), ('a501e7c177c6f9f8e8cf2a8484ca2710c959c999', 'DESIGN-v2.md'),
                 ('ca180164d70df9d66c5530bc6196d2377ee56e13', 'review-v2.md'), ('4c18f7156468072afe59a25aa927020568797527', 'DESIGN-v6.0e.md'),
                 ('1b4d7694a83b0e386bbe91d06bb1bfb5517403ca', 'r5.md')):
    g(ident, 'blob of the drafting source %s (records branch)' % n, OFF,
      PROV + ': an inventory source; the inventory labels in Sources are provenance, r6 states every rule itself (R6.STAT.2)')
for p, b in BLOB.items():
    if b not in GIT:
        g(b, 'blob of %s at c33d5b71' % p, H, PROV + ': an input pin of generator-round4 (tree-c33d5b71.json)')
SHORT = collections.OrderedDict([
    ('e5b97ef1', ('blob of DESIGN-v5.5.9.md (records branch)', OFF, PROV + ': a "where else stated" pointer; the status of the '
                  'requirements rests on owner decisions in the owner\'s words, quoted on main')),
    ('1153e039', ('blob of `P`\'s edits_check.py (in generator-round2 strings)', OFF, PROV + ' (generator data); the content is the '
                  'open item of `P` in sec. 4'))])
COMMENT_BODIES = collections.OrderedDict()
for d in (COMM, COMM3, REC):
    for cid, c in d.items():
        COMMENT_BODIES[cid] = c['body']
BODY_SHA = {sha(b): cid for cid, b in COMMENT_BODIES.items()}
FILE_SHA = {}
for p, b in list(LANDED.items()) + [(p, SRC[p]) for p in BLOB if p not in LANDED]:
    FILE_SHA.setdefault(sha(b), p)
FILE_SHA.setdefault(sha(S('generator-round3/review-r6-round2.md')), 'generator-round3/review-r6-round2.md')
FILE_SHA.setdefault(sha(REV3), 'the round-3 reviewer text')
INV_SRC = {v['sha256']: k for k, v in INVENTORY['sources'].items()}
DIG = collections.OrderedDict([
    ('d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27', ('sha256 of AGENTS.md at `H`', MAIN, SOM)),
    ('59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2', ('sha256 of `T1\'`\'s AGENTS.md (= `X_rep`\'s)', OFF,
     GIT['9f4fc3e830707c90ffc105842d26d5b51f01760b'][2])),
    ('2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5', ('sha256 of the ledger.json pin', OFF, GIT['ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e'][2])),
    ('528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1', ('sha256 of the edits.json pin', OFF, GIT['ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e'][2])),
    ('4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131', ('sha256 of DESIGN-v6.0e.md (records branch)', OFF,
     'in AUTHORIZATIONS.md: ' + SOM + ' for the claim made (the owner adopted v6.0e at this digest; quoted from comment '
     '7130449822, whose body lands in generator-round2/comments-1169.json); the document itself: ' + PROV)),
    ('11a9077c04622f0672687be694162f3ececc528ee5c7f2e599b27793aa32a653', ('sha256 of r5.md', OFF, PROV + ': names where a '
     'quotation stands; the entry permits nothing for r6'))])
SHORT_DIG = {'2856e58c': ('sha256 prefix of `P`\'s edits_check.py', OFF, GIT['4c79be642ca631573f06b444903be75ec4f5e2b6'][2])}


def snaponly(files):
    return files <= SNAP


def classify(kind, tok, files):
    """(names, status, classification) or None."""
    if kind == 'hex40':
        return GIT.get(tok)
    if kind == 'sha256':
        if tok in DIG:
            return DIG[tok]
        if tok in BODY_SHA:
            return ('sha256 of the body of #1169 comment %s' % BODY_SHA[tok], HOST, SOM + ': the body lands in a comment snapshot of generator-round2, generator-round3 or generator-round4')
        if tok in FILE_SHA:
            p = FILE_SHA[tok]
            st = H if (p in BLOB and p not in LANDED) else MAIN
            return ('sha256 of %s' % p, st, (SOMH if st == H else SOM + ' once landed'))
        if tok in INV_SRC:
            return ('sha256 of the drafting source %s (records branch)' % INV_SRC[tok], OFF, PROV + ': an inventory source (R6.STAT.2)')
        if files == {'EXPECTATIONS.json'}:
            return ('digest stated in an expectation (fixture or composed blob)', NOOBJ, PROV + ': names no repository content')
        if snaponly(files):
            return ('digest inside a verbatim snapshot or generator data', NOOBJ, PROV + ': no claim of the landed documents uses it')
        return None
    if kind == 'short':
        full = [k for k in GIT if k.startswith(tok)]
        if len(full) == 1:
            n, s_, c = GIT[full[0]]
            return ('prefix of %s: %s' % (full[0][:12], n), s_, c)
        fulld = [k for k in list(DIG) + list(BODY_SHA) + list(FILE_SHA) + list(INV_SRC) if k.startswith(tok)]
        if fulld:
            return classify('sha256', fulld[0], files)
        if tok in SHORT:
            return SHORT[tok]
        if tok in SHORT_DIG:
            return SHORT_DIG[tok]
        return None
    if kind == 'comment':
        if tok in COMMENT_BODIES:
            return ('#1169 comment %s' % tok, HOST, SOM + ': its body, author and time land in a comment snapshot, and the '
                    'documents quote it with author and time (AGENTS.md sec. A.42 item 7)')
        if tok == '7092885251':
            return ('#1169 comment 7092885251 (execution-exception route)', HOST, PROV + ': cited as superseded; that claim rests on '
                    'owner decision A3, quoted on main')
        return ('#1169 comment %s' % tok, HOST, PROV + ': named in a review\'s account of what it read, or inside a quoted comment; '
                'no claim of the documents uses its content')
    if kind == 'number':
        if tok == '#1169':
            return ('Issue #1169 (A1-EXIT)', HOST, PROV + ': the accountable Issue (planning; AGENTS.md sec. A.45 rule 1)')
        if tok in ('#1468', '#1470', '#1472', '#1473', '#1474', '#1475', '#1494'):
            return ('pull request %s, merged in `E..H`' % tok, HOST, SOM + ': the claims read its merge commit on main')
        if snaponly(files):
            return ('Issue or pull request %s' % tok, HOST, PROV + ': occurs only inside a quoted comment')
        return None
    if kind == 'run':
        if tok == '45569710442':
            return ('CI run 45569710442 (tool commit a3799244)', HOST, 'in DESIGN-r6.md: support off main for R6.EVID.6\'s and '
                    'sec. 16.9\'s statements of what the run recorded (adoption trace), not relied on by adoption; in '
                    'EXPECTATIONS.json `source` fields: ' + PROV)
        if snaponly(files):
            return ('CI run %s' % tok, HOST, PROV + ': occurs only inside a quoted comment')
        return None
    if kind == 'branch':
        if snaponly(files):
            return ('branch %s' % tok, OFF, PROV + ': occurs only inside a quoted comment')
        return None


REFROWS = []
for (kind, tok), files in sorted(FOUND.items(), key=lambda x: (list(PAT).index(x[0][0]), x[0][1])):
    c = classify(kind, tok, files)
    if c is None:
        PROBLEMS.append('manifest: unclassified reference %s %s in %s' % (kind, tok, sorted(files)))
        continue
    if 'support off main' in c[2] and not (files - SNAP):
        pass
    REFROWS.append((tok, kind, c[0], c[1], ', '.join(sorted(files)), c[2]))
N_OFF_ADOPT = [r for r in REFROWS if 'relied on by adoption' in r[5] and 'not relied on by adoption' not in r[5]]


def md_table(head, rows):
    return '\n'.join(['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] +
                     ['| ' + ' | '.join(str(x).replace('|', '/') for x in r) + ' |' for r in rows])


MANIFEST = '\n'.join([
    '# r6: landing manifest', '',
    'Owner decision A5 of 2026-11-25 (%s), quoted: "%s"' % (OWNER_AT, body('A5')), '',
    'Directory: `%s/`. The landing tree of this directory is the round-3 tree (commit c33d5b71a3e4e15028d19ff153afcee8f5aa90a3) '
    'with the round-4 outputs, the files of sec. 1 kept and those of sec. 2 removed. This manifest approves no merge; the '
    'landing pull request\'s merge needs its own owner approval (AGENTS.md sec. A.50 item 1).' % DIRPATH, '',
    '## 1. Files that land', '',
    md_table(['Path', 'Role', 'Source', 'sha256'],
             [(p, ROLE[p], 'round-4 output' if p in NEWDOCS else ('round-4 generator' if p in GEN4 else
              'unchanged from c33d5b71 (blob %s)' % BLOB[p][:12]), sha(LANDED[p])) for p in LANDED] +
             [('LANDING-MANIFEST.md', 'this manifest (A5)', 'round-4 output', '(this file)')]), '',
    'Note on generator-round4: owner decision A5 names the round-2 and round-3 generators; generator-round4 produces the '
    'final documents and is listed here as a committed input necessary for their reproducibility. Its landing is part of the '
    'owner\'s merge decision. CORRECTION-REPORT-round4.md, which generator-round4 writes beside its outputs, is not landed '
    '(it is regenerated by the recipe below).', '',
    'Recipe (AGENTS.md sec. A.42 item 1): lay out `out-final4/` as the round-3 files of c33d5b71 (the documents and reports at '
    'the directory root, generator-round3 as `out-final4/build/` with its two inputs in `out-final4/build/inputs/`), `c33/` as the '
    'directory at c33d5b71, and `out-final5/build/` as generator-round4 (correct4.py, with its four inputs in `inputs/`); run '
    '`python3 -I -B out-final5/build/correct4.py`. It exits 0 and writes the files of sec. 1 marked "round-4 output" with the '
    'sha256 stated. The earlier generators reproduce their rounds from c33d5b71\'s ancestors 400e4b4f and ad035ff5 as their own '
    'reports state.', '',
    '## 2. Files left to Git history', '',
    'Each stays at c33d5b71 (and its ancestors on the branch), reachable from main once the landing merge keeps the branch '
    'history.', '',
    md_table(['Path', 'What it is', 'Blob at c33d5b71'], [(p, why, BLOB[p]) for p, why in DROPPED.items()]), '',
    'Landing precondition: the merge keeps the branch history (a merge commit or fast-forward, not a squash), so that '
    'c33d5b71, 400e4b4f, ad035ff5, a6b6884b, f4e18558, c1244459 and 4e9a1501 become reachable from main. Without it, every '
    'reference below classified "%s" is support off main.' % SOMH.split(' (')[0], '',
    '## 3. References of the landed files to content not on `main` (AGENTS.md sec. A.42 item 8)', '',
    'Every reference found in the landed files (except this manifest and correct4.py, which carry only the references listed '
    'here) by commit, blob, tree or digest id, comment, Issue or pull-request number, CI run or branch name, each classified by '
    'the claim it is attached to. "Status" says where the referenced content is.', '',
    md_table(['Reference', 'Kind', 'What it names', 'Status', 'Occurs in', 'Classification'], REFROWS), '',
    '## 4. Support off `main` that remains', '',
    '- Relied on by adoption: the semantics that R6.SPLIT.3, R6.PROF.3, R6.PROF.4, R6.PROF.5, R6.PROF.7, R6.PROF.8, R6.PROF.9, '
    'R6.PROF.10, R6.PROF.12, R6.DENY.5, R6.A1CFG.2 and OBL-1 define by reference to `P`\'s edits_check.py (git blob 1153e039..., '
    'sha256 2856e58c...d98c), which is on no commit reachable from main. It is closed before adoption by landing that one blob '
    'in this directory, or by narrowing those requirements; either needs an owner decision, since owner decision A5 does not '
    'cover the blob.',
    '- Not relied on by adoption (R6.STAT.10), but claims of the landed design: its statements of what the tool commit '
    'a37992449b452021001277c06c524a30c92dfb87, CI run 45569710442 and `T1\'` contain (adoption trace, sec. 32). Under AGENTS.md '
    'sec. A.42 item 8 they are closed by the time the directory lands, by landing their content or narrowing them, or land by a '
    'recorded owner decision that names them as unsupported.',
    '- Acceptance references for the tool\'s landing (controls reading `T1\'` or `P`, the ledger and edit-list pins): no claim '
    'of this landing uses them; the design states them as open for the tool\'s landing.', ''])
log('A5', 'LANDING-MANIFEST.md', 'landed files, files left to history, %d references classified' % len(REFROWS))

# =====================================================================================================
# self-checks
# =====================================================================================================
CHK_BEFORE, VAL_BEFORE = run_checks(T_IN, EXP['rows'], REQ_IN, EXP, PEND3)
CHK_AFTER, VAL_AFTER = run_checks(T, EXP_OUT['rows'], REQ_OUT, EXP_OUT, PEND3)
IDX_IN = collections.OrderedDict((r['id'], r) for r in EXP['rows'])
A1ROWS = ('TR45-opB', 'TR45-opC', 'TR45')
ws = lambda s: re.sub(r'\s+', ' ', s).strip()
EDITED = set(t for _, t, _ in LOG)
OWN = collections.OrderedDict()
OWN['A1: the three rows keep expect, restored, requirements, runner and procedure; NOT RUN admitted with the deferral'] = [
    i for i in A1ROWS if any(dumps(IDX_IN[i].get(k)) != dumps(EIDX[i].get(k)) for k in ('expect', 'restored', 'requirements', 'runner', 'procedure', 'composed_of'))
    or 'NOT RUN' not in EIDX[i]['status_allowed'] or EIDX[i]['not_run']['release_condition'] != DEF_NR['release_condition']]
OWN['A1/A2: every other row byte-identical; order, count and retired unchanged'] = [
    a['id'] for a, b in zip(EXP['rows'], EXP_OUT['rows']) if a['id'] not in A1ROWS + ('item11-T1p',) and dumps(a) != dumps(b)] + (
    [] if [r['id'] for r in EXP['rows']] == [r['id'] for r in EXP_OUT['rows']] else ['order']) + (
    [] if dumps(EXP['retired']) == dumps(EXP_OUT['retired']) else ['retired'])
OWN['A1: OBL-17 gates no step; GATE.15 and CTRL.5 admit NOT RUN for TR45-opB'] = (
    (['OBL-17'] if 'Gates: none while deferred.' not in REQS['OBL-17']['text'] else []) +
    [r for r in ('R6.GATE.15', 'R6.CTRL.5') if 'TR45-opB, TR45-opC' not in REQS[r]['text']] +
    (['sec. 32 table'] if '| OBL-17 | the A1 retirement execution |' in T else []))
OWN['A2: item11-T1p differs only in its two flags, both "candidate evidence only, not acceptance support"'] = (
    [] if [k for k in IDX_IN['item11-T1p'] if k != 'flags'] == [k for k in EIDX['item11-T1p'] if k != 'flags'] and
    all(dumps(IDX_IN['item11-T1p'][k]) == dumps(EIDX['item11-T1p'][k]) for k in EIDX['item11-T1p'] if k != 'flags') and
    sum(1 for f in EIDX['item11-T1p']['flags'] if 'candidate evidence only, not acceptance support' in f) == 2 and
    'acceptance reference only' not in dumps(EIDX['item11-T1p']) else ['item11-T1p'])
OWN['A3: the owner\'s wording quoted byte-exact in sec. 0.1; R6.STAT.8 cites it'] = (
    ([] if bq(OD['A3-wording']) in T[T.index('### 0.1'):T.index('## 1. Notation')] else ['quote']) +
    ([] if 'owner decision A3' in REQS['R6.STAT.8']['text'] else ['STAT.8']))
OWN['A4: the 53 carry the confirmation once; no pending mark or key remains'] = (
    [r for r in A4SET if REQS[r]['text'].count(CONF_A4) != 1] + [r for r, q in REQS.items() if PEND3 in q['text']] +
    [q['id'] for q in REQ_OUT if q['pending_owner_confirmation']] +
    sorted(set(q['id'] for q in REQ_OUT if any(d['decision'] == 'A4' for d in q['owner_decision'])) ^ set(A4SET)))
OWN['CLOSE: R6.TREE.12 condition is the owner-approved restatement of LC-7'] = (
    [] if 'Until LC-7\'s cases are restated by an owner-approved expectation change' in REQS['R6.TREE.12']['text'] and
    'r6 is adopted' not in REQS['R6.TREE.12']['text'] else ['TREE.12'])
OWN['preservation: requirement ids unchanged'] = sorted(set(REQS_IN) ^ set(REQS))
OWN['preservation: sources, controls and OPEN markers of every requirement equal the index'] = [
    q['id'] for q in REQ_OUT if (REQS[q['id']]['sources'], REQS[q['id']]['controls'], REQS[q['id']]['open']) !=
    (q['sources'], q['controls'], q['open'])]
OWN['preservation: sources and controls unchanged from round 3'] = [
    q['id'] for q in REQ_OUT if (q['sources'], q['controls']) != (REQ_IDX_IN[q['id']]['sources'], REQ_IDX_IN[q['id']]['controls'])]
OWN['preservation: requirement blocks without a logged edit unchanged (whitespace-normalized)'] = [
    r for r in REQS_IN if r not in EDITED and ws(REQS_IN[r]['text']) != ws(REQS[r]['text'])]
OWN['preservation: sections 33, 34 and Appendix H unchanged'] = (
    [] if T[T.index('## 33. Retired'):] == T_IN[T_IN.index('## 33. Retired'):] else ['changed'])
OWN['FRESH-AUTHORIZATION.md: every quoted requirement wording equals the design'] = [
    r for r in REQS if ('### %s\n' % r) in FRESH and bq(block(r)) not in FRESH]
OWN['REVIEW-r6-round3.md holds the reviewer text verbatim'] = [] if REV3_OK else ['mismatch']
OWN['manifest: every reference classified; landed and dropped partition the 37 files'] = [
    p for p in PROBLEMS if p.startswith('manifest:')]
for k, v in list(CHK_AFTER.items()) + list(OWN.items()):
    if v:
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================================
# CORRECTION-REPORT-round4.md
# =====================================================================================================
CONTENT = collections.OrderedDict(list(NEWDOCS.items()) + [('LANDING-MANIFEST.md', MANIFEST)] + [
    (p, SRC[p].decode('utf-8')) for p in ('MIGRATION.json', 'V4-COMPARISON.md', 'REVIEW-r6-round2.md')])


def report():
    hashes = collections.OrderedDict((n, sha(c)) for n, c in CONTENT.items())
    L = ['# r6, round 4: correction report', '',
         'Generator: build/correct4.py (landed as generator-round4/). Applies owner decisions A1 to A5 of 2026-11-25 and the '
         'closing direction (quoted in DESIGN-r6.md sec. 0.1). Nothing is adopted, frozen, merged or executed.', '',
         '## 1. Inputs', '', md_table(['Input', 'sha256 or git blob'],
                                       [('directory at c33d5b71: ' + p, 'blob ' + b) for p, b in BLOB.items()] + INPUT_SHA), '',
         '## 2. Edits', '', md_table(['#', 'Decision', 'Target', 'Edit'], [(i + 1, d, t, e) for i, (d, t, e) in enumerate(LOG)]), '',
         'R6.TREE.19 clarifications of the round-3 delta review applied, each as one sentence or a word substitution (NIT): '
         '(a) the program is a generator named by the delegation contract pinned at `F`, a class naming none stays '
         'REVIEW_REQUIRED; (b) R6.DELEG.3\'s isolation cited and the different failure classes explained; (c) the consequence '
         'for a generator that is not byte-deterministic stated (fail-closed FAIL). Not applied: the review\'s nits N-a to N-d; '
         'the Table 17.1 description of item11-T1p ("candidate evidence for the landing decision only") is left as it stands, '
         'since owner decision A2 changes only the two flags; LC-7\'s row in the expectation file keeps its flag text until '
         'the owner-approved restatement of its cases.', '',
         '## 3. Values, before (round 3) and after', '',
         md_table(['Value', 'Before', 'After'], [(k, VAL_BEFORE[k], VAL_AFTER[k]) for k in VAL_AFTER]), '',
         '## 4. Self-checks', '', 'Round-3 checks (run_checks of correct3.py), before and after:', '',
         md_table(['Check', 'Before', 'After'], [(k, len(CHK_BEFORE[k]) if CHK_BEFORE[k] else 'pass',
                                                  len(CHK_AFTER[k]) if CHK_AFTER[k] else 'pass') for k in CHK_AFTER]), '',
         'Round-4 checks:', '', md_table(['Check', 'Result'], [(k, 'pass' if not v else 'FAIL %s' % v[:5]) for k, v in OWN.items()]), '',
         '## 5. Outputs', '', md_table(['File', 'sha256'], list(hashes.items())), '',
         'MIGRATION.json, V4-COMPARISON.md and REVIEW-r6-round2.md are written unchanged. The generator re-runs itself in a '
         'separate process and writes only if every output\'s sha256 is equal.', '',
         '## 6. Before adoption', '',
         '- Done: the owner decisions A1-A5 and the round-3 delta review are recorded at #1169 comments %s and %s.' % (DEC4_ID, REV4_ID),
         '- One short independent delta review of this revision (closing direction; R6.STAT.10).',
         '- `P`\'s edits_check.py semantics: support off main relied on by adoption (LANDING-MANIFEST.md sec. 4); an owner decision '
         'lands the blob or narrows the requirements.',
         '- The landing: the owner-approved merge of the files of LANDING-MANIFEST.md sec. 1, keeping the branch history, with the '
         'remaining item 8 gaps of its sec. 4 closed or named by an owner decision (AGENTS.md sec. A.42 item 8, sec. A.50 item 1).', '']
    return '\n'.join(L)


CONTENT['CORRECTION-REPORT-round4.md'] = report()

# =====================================================================================================
# hygiene, reproducibility, write
# =====================================================================================================
ALLOWED = set(ch for c in [T_IN, EXP_TXT, REQ_TXT, PARA_TXT, AUTH_TXT, FRESH_TXT, REV3] + list(OD.values()) for ch in c if ord(ch) > 127)
BAD_SP = re.compile('[   -​  　﻿]')
LONG_URL = re.compile(r'https?://github\.com/\S{60,}')
for n, c in CONTENT.items():
    for what, bad in (('@', '@' in c), ('/tmp', '/tmp' in c), ('scratchpad', 'scratchpad' in c), ('session id', 'session_0' in c),
                      ('github.com', 'github.com' in c), ('CR', '\r' in c),
                      ('format character', any(unicodedata.category(ch) == 'Cf' for ch in c)),
                      ('non-ASCII space', bool(BAD_SP.search(c))), ('long github URL', bool(LONG_URL.search(c))),
                      ('non-ASCII character outside inputs', bool(set(ch for ch in c if ord(ch) > 127) - ALLOWED))):
        if bad and not (n in ('MIGRATION.json', 'V4-COMPARISON.md', 'REVIEW-r6-round2.md')):
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
    with open(os.path.join(OUT, n), 'wb') as f:
        f.write(c.encode('utf-8'))
for n in CONTENT:
    print(n, HASHES[n])
for k in VAL_AFTER:
    print('VALUE', k, VAL_BEFORE[k], '->', VAL_AFTER[k])

#!/usr/bin/env python3
"""Final text-only revision of design r6 (owner decisions 1-5 of 2026-11-25, #1169 comment 7166844576).

Reads, read only: out-final3/ (the round-2 outputs, byte-identical to the directory
verification/audits/foundations/a1exit-design-r6-20261125/ at commit 400e4b4f), its build/text2.py (data of the
round-2 generator, imported without writing bytecode), gh7/sel.json (= generator-round2/comments-1169.json),
MAPPING.json and INVENTORY.json (= the directory's files of those names), and build/inputs/ beside this file
(the review text recorded at #1169 comment 7166666428 and the two comments of 2026-11-25 read with GET requests).
Writes out-final4/.  Every change is a logged edit tagged with the owner decision (D1-D5) or review finding
(R1-R6, N1-N6) it applies, or `meta` for a mechanical consequence.  The self-checks of round 2 (correct2.py's
run_checks, parameterized by the pending mark) are re-run on out-final3 ("before") and on the outputs
("after").  The generator re-runs itself in a separate process and compares every output's sha256 before
writing.
"""
import collections
import copy
import hashlib
import importlib.util
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
R6 = os.path.dirname(OUT)
IN = os.path.join(R6, 'out-final3')
INP = os.path.join(HERE, 'inputs')


def rd(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def sha(b):
    if isinstance(b, str):
        b = b.encode('utf-8')
    return hashlib.sha256(b).hexdigest()


def rj(s):
    return json.loads(s, object_pairs_hook=collections.OrderedDict)


def dumps(o):
    return json.dumps(o, indent=1, ensure_ascii=True) + '\n'


_spec = importlib.util.spec_from_file_location('text2', os.path.join(IN, 'build', 'text2.py'))
TX = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(TX)

INPUTS = [('out-final3/' + n, 'directory file ' + n) for n in (
    'DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json', 'MIGRATION.json', 'PARAPHRASED-DECISIONS.md',
    'AUTHORIZATIONS.md', 'FRESH-AUTHORIZATION.md', 'V4-COMPARISON.md', 'CORRECTION-REPORT.md')] + [
    ('out-final3/build/text2.py', 'generator-round2/text2.py'),
    ('out-final3/build/correct2.py', 'generator-round2/correct2.py (not executed; its functions are restated here)'),
    ('gh7/sel.json', 'generator-round2/comments-1169.json'),
    ('MAPPING.json', 'directory file MAPPING.json'),
    ('INVENTORY.json', 'directory file INVENTORY.json'),
    ('out-final4/build/inputs/review-r6-round2.md', 'the reviewer text of #1169 comment 7166666428'),
    ('out-final4/build/inputs/comments-round3.json', '#1169 comments 7166666428 and 7166844576 (GET; body, user.login, created_at)')]
INPUT_SHA = [(p, sha(open(os.path.join(R6, p), 'rb').read()), m) for p, m in INPUTS]

T_IN = rd(os.path.join(IN, 'DESIGN-r6.md'))
T = T_IN
EXP_TXT = rd(os.path.join(IN, 'EXPECTATIONS.json'))
EXP = rj(EXP_TXT)
REQ_TXT = rd(os.path.join(IN, 'REQUIREMENTS.json'))
REQ_IN = rj(REQ_TXT)
MIG_TXT = rd(os.path.join(IN, 'MIGRATION.json'))
PARA_TXT = rd(os.path.join(IN, 'PARAPHRASED-DECISIONS.md'))
AUTH_TXT = rd(os.path.join(IN, 'AUTHORIZATIONS.md'))
FRESH_TXT = rd(os.path.join(IN, 'FRESH-AUTHORIZATION.md'))
V4_TXT = rd(os.path.join(IN, 'V4-COMPARISON.md'))
REPORT2_TXT = rd(os.path.join(IN, 'CORRECTION-REPORT.md'))
MAPPING = rj(rd(os.path.join(R6, 'MAPPING.json')))
INV = collections.OrderedDict((i['id'], i) for i in rj(rd(os.path.join(R6, 'INVENTORY.json')))['items'])
COMM = rj(rd(os.path.join(R6, 'gh7', 'sel.json')))
COMM3 = rj(rd(os.path.join(INP, 'comments-round3.json')))
REVIEW = rd(os.path.join(INP, 'review-r6-round2.md'))
for k, v in COMM3.items():
    COMM[k] = v
DEC_ID = '7166844576'
REV_ID = '7166666428'
DEC_BODY = COMM[DEC_ID]['body']
DEC_AT = COMM[DEC_ID]['created_at']
REV_AT = COMM[REV_ID]['created_at']

LOG = []
PROBLEMS = []


def log(item, target, desc):
    LOG.append((item, target, desc))


# ------------------------------------------------------------------ text helpers (as correct2.py)
BLOCK_END = re.compile(r'\n(?=\*\*R6\.[A-Z0-9]+\.\d+\*\*|\*\*OBL-\d+\*\*|#|\*\*\*\s*$|\*\*Table )', re.M)


def block_span(rid, text=None):
    text = T if text is None else text
    a = text.index('**%s**' % rid)
    m = BLOCK_END.search(text, a + 3)
    return a, (m.start() if m else len(text))


def block(rid, text=None):
    text = T if text is None else text
    a, b = block_span(rid, text)
    return text[a:b]


def edit(item, target, old, new, count=1):
    global T
    n = T.count(old)
    if n != count:
        PROBLEMS.append('edit %s/%s: expected %d occurrence(s), found %d: %r' % (item, target, count, n, old[:80]))
        return
    T = T.replace(old, new)
    log(item, target, 'text edit (%d occurrence(s))' % count)


def in_block_edit(item, rid, old, new, desc='text edit'):
    global T
    a, b = block_span(rid)
    blk = T[a:b]
    if blk.count(old) != 1:
        PROBLEMS.append('in_block_edit %s/%s: %d occurrences of %r' % (item, rid, blk.count(old), old[:70]))
        return
    T = T[:a] + blk.replace(old, new) + T[b:]
    log(item, rid, desc)


def parse_list(s):
    s = re.sub(r'\([^()]*\)', '', s)
    s = re.sub(r'\([^()]*\)', '', s)
    out = []
    for t in s.split(','):
        t = t.strip().rstrip('.').strip()
        if t and t != 'none' and not t.startswith('none'):
            out.append(t)
    return out


PEND_TXT = 'Pending owner confirmation (see PARAPHRASED-DECISIONS.md).'
PEND3 = 'Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).'
REQ_RE = re.compile(r'^\*\*(R6\.[A-Z0-9]+\.\d+|OBL-\d+)\*\*', re.M)


def parse_reqs(text):
    out = collections.OrderedDict()
    for m in REQ_RE.finditer(text):
        rid = m.group(1)
        a, b = block_span(rid, text)
        blk = text[a:b]
        sm = re.search(r'Sources:(.*?)(?:Controls:|$)', blk, re.S)
        cm = re.search(r'Controls:(.*)$', blk, re.S)
        if rid in out:
            PROBLEMS.append('duplicate requirement id ' + rid)
        out[rid] = {'id': rid, 'sources': parse_list(sm.group(1)) if sm else [],
                    'controls': parse_list(cm.group(1)) if cm else [],
                    'open': re.findall(r'OPEN: ([^.]+)\.', blk), 'text': blk}
    return out


# =====================================================================================================
# The owner's decisions (#1169 comment 7166844576), extracted byte-exact
# =====================================================================================================
_a = DEC_BODY.index('quoted:\n\n"') + len('quoted:\n\n"')
_b = DEC_BODY.index('"\n\nAs recorded')
DEC_ALL = DEC_BODY[_a:_b]
_parts = re.split(r'\n\n(?=[2-5]\. )', DEC_ALL)
if len(_parts) != 5 or not all(p.startswith('%d. ' % (i + 1)) for i, p in enumerate(_parts)):
    PROBLEMS.append('decision text: unexpected structure')
DEC = {i + 1: p for i, p in enumerate(_parts)}
DEC_1_4 = DEC_ALL[:DEC_ALL.index('\n\n5. ')]
OWNER_LINE = 'Owner decision (amaybaum, 2026-11-25, coordinating session), quoted:'
DQ = collections.OrderedDict([
    ('D3-ACCEPT', 'Accept the reversal and retain human review for V15.'),
    ('D3-NORULE', 'Do not introduce additional rules based solely on constructed examples without an established scientific or verification need.'),
    ('D3-CAVEAT', 'This is a decision about the automated checker\'s scope, not permission to make scientifically unsupported claims about finiteness.'),
    ('D4-LAND', 'Prepare the r6 directory and review record for landing on `main`. Merge approval remains separate.'),
    ('D4-LC7', 'Establish the LC-7 regeneration and byte-comparison procedure, with independent review.'),
    ('D4-T1P', 'Treat the earlier T1′ figure solely as candidate evidence, not acceptance support.'),
    ('D5-S1D3', 'However, do not use adoption as blanket authorization for potentially under-marked S1-D3 requirements. Explicitly identify those requirements and establish their authorization status. Include them in the final adoption decision if necessary.'),
    ('D5-PEND', 'Non-confirmation must leave a requirement pending, not withdraw it.'),
    ('D5-SCOPE', 'This authorizes the final design revision and its review, not adoption, implementation, freezing, trial execution or merging.'),
    ('D5-REV', 'Include decisions 1–4 and address R1–R6 and N1–N6 within the identified scope.'),
    ('D1-DEFER', 'Defer R6.OUT.15 and its dependent offline replay mode.'),
    ('D1-SCOPE', 'Keep R6.STAT.4 and R6.EVID.5 as scope statements without redundant checks.'),
])
for k, q in DQ.items():
    if DEC_ALL.count(q) != 1:
        PROBLEMS.append('decision quote %s not found exactly once' % k)
if OWNER_LINE not in DEC_BODY:
    PROBLEMS.append('owner attribution line missing')


def dq(k):
    return '"%s"' % DQ[k]


# =====================================================================================================
# The review: four classes and the 12 flagged requirements (parsed from the reviewer text)
# =====================================================================================================
RID = r'(?:R6\.[A-Z0-9]+\.\d+|OBL-\d+)'
CLASS_ROWS = collections.OrderedDict()
for line in REVIEW.split('\n'):
    m = re.match(r'\| (Necessary for scientifically valid retirement|Necessary for reliable verification|'
                 r'Redundant with an existing safeguard|Unrelated to A1 retirement, can be deferred) \| (\d+) \| (.*) \|$', line)
    if m:
        name, n, cell = m.group(1), int(m.group(2)), m.group(3)
        if name.startswith('Necessary'):
            ids = re.findall(RID, cell)
        elif name.startswith('Redundant'):
            ids = re.findall(r'(?:^|; )(%s) \(' % RID, cell)
        else:
            ids = re.findall(r'^(%s),' % RID, cell)
        if len(ids) != n:
            PROBLEMS.append('review class %s: %d ids parsed, %d stated' % (name, len(ids), n))
        CLASS_ROWS[name] = ids
CL_V = CLASS_ROWS.get('Necessary for scientifically valid retirement', [])
CL_R = CLASS_ROWS.get('Necessary for reliable verification', [])
CL_S = CLASS_ROWS.get('Redundant with an existing safeguard', [])
CL_D = CLASS_ROWS.get('Unrelated to A1 retirement, can be deferred', [])
REV_CLASS = {}
for name, ids in CLASS_ROWS.items():
    for i in ids:
        REV_CLASS[i] = name
FLAGGED12 = collections.OrderedDict()
_fa = REVIEW.index('## The 12 flagged requirements')
_fb = REVIEW.index('None is (a).')
for line in REVIEW[_fa:_fb].split('\n'):
    m = re.match(r'\| (%s) \| \(([a-d])\) \| (.*) \|$' % RID, line)
    if m:
        FLAGGED12[m.group(1)] = (m.group(2), m.group(3))
if len(FLAGGED12) != 12:
    PROBLEMS.append('flagged table: %d rows' % len(FLAGGED12))
REV_SHA_STATED = re.search(r'SHA-256 of the unredacted review text: `([0-9a-f]{64})`', COMM[REV_ID]['body'])
_ra = COMM[REV_ID]['body'].index('---- reviewer text begins ----\n\n') + len('---- reviewer text begins ----\n\n')
_rb = COMM[REV_ID]['body'].index('\n\n---- reviewer text ends ----')
REV_INNER = COMM[REV_ID]['body'][_ra:_rb]

MARKED_IN = [q['id'] for q in REQ_IN if q['pending_owner_confirmation']]
if sorted(CL_V + CL_R + CL_S + CL_D) != sorted(MARKED_IN):
    PROBLEMS.append('decision 1 classes do not equal the 44 marked requirements')

# =====================================================================================================
# D1: confirmations, scope statements, deferral
# =====================================================================================================
D1REF = 'owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1)'
CONF_V = 'Confirmed by %s as necessary for scientifically valid retirement.' % D1REF
CONF_R = 'Confirmed by %s as necessary for reliable verification.' % D1REF
SCOPE_TXT = 'Scope statement by %s; it has no check of its own.' % D1REF
SCOPE_EVID5 = (SCOPE_TXT + ' GATE-16, named below, is the gate\'s reference-difference control of R6.GATE.9; it checks '
               'only that a figure kept as `reference` never changes a verdict.')
DEFER_TXT = ('Deferred by %s, together with the `replay` mode of R6.REC.24 and control TR45-opB. The text above is '
             'kept as the deferred specification; it binds no tool revision until a recorded owner decision takes it '
             'up. Accountable Issue: #1169. A committed result is re-established under AGENTS.md sec. A.42 item 1 by '
             'R6.OUT.14\'s recipe and a re-run on `main`.' % D1REF)
NEWMARK = {}
for r in CL_V:
    NEWMARK[r] = CONF_V
for r in CL_R:
    NEWMARK[r] = CONF_R
NEWMARK['R6.STAT.4'] = SCOPE_TXT
NEWMARK['R6.EVID.5'] = SCOPE_EVID5
NEWMARK['R6.OUT.15'] = DEFER_TXT
for rid in MARKED_IN:
    tag = 'D1-defer' if rid in CL_D else ('D1-scope' if rid in CL_S else 'D1')
    in_block_edit(tag, rid, PEND_TXT, NEWMARK[rid], 'pending mark replaced: %s' % (
        'deferred' if rid in CL_D else 'scope statement' if rid in CL_S else
        'confirmed (valid retirement)' if rid in CL_V else 'confirmed (reliable verification)'))
in_block_edit('D1-defer', 'R6.REC.24', 'The offline replay writes `mode: "replay"`.',
              'The offline replay writes `mode: "replay"`; that mode is deferred with R6.OUT.15 (owner decision 1,\nsec. 0.1).',
              'replay mode marked deferred')

# =====================================================================================================
# D3: the V4 group, resolution (a)
# =====================================================================================================
D3REF = 'owner decision 3 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1)'
in_block_edit('D3', 'R6.PUR.9',
    "**R6.PUR.9** For decision at adoption (not adopted by this draft): the residual for the deny rule\nDR-2.",
    "**R6.PUR.9** The residual for the deny rule DR-2, decided by %s; the decision takes effect\nwith r6's adoption." % D3REF,
    'status: decided (a)')
in_block_edit('D3', 'R6.PUR.9',
    "is an owner decision at adoption (RD-14, Q10), with\nthese options:",
    "was an owner decision (RD-14, Q10) among\nthese options:", 'options stated as the decision space')
in_block_edit('D3', 'R6.PUR.9',
    "V15. Until it is made, each of the four rows carries both candidate expectations, each marked\n"
    "\"not authoritative; decided at r6 adoption\", and an `expect` of outcome DEFERRED; the gate reports\n"
    "`deferred-expectation` for each and never holds on it (R6.GATE.9). Outstanding evidence, a named\n"
    "blocker on adoption of this requirement: the owner decision V5-D1 that dropped DR-2 is recorded only\n"
    "in paraphrase, in the session-written #1169 comment 7099655517 (ME-6); its text is to be recorded by\n"
    "the owner.",
    "V15. Owner decision 3 chose (a), in the owner's words: %s and %s The owner's caveat, quoted: %s Each of\n"
    "the four rows carries the expectation of the candidate \"reversal adopted\" as its `expect`, and no deny\n"
    "rule is added. The outstanding-evidence blocker on this requirement, that the owner decision V5-D1 that\n"
    "dropped DR-2 was recorded only in paraphrase in the session-written #1169 comment 7099655517 (ME-6), is\n"
    "discharged by the text of decision 3." % (dq('D3-ACCEPT'), dq('D3-NORULE'), dq('D3-CAVEAT')),
    'decision (a) recorded with the owner\'s words and caveat; outstanding-evidence blocker discharged by the decision text')
in_block_edit('D3', 'R6.DENY.6',
    "**Accepted residual: V4 and V27 (for decision at adoption; not adopted by this\ndraft).**",
    "**Accepted residual: V4 and V27 (confirmed by owner decision 3 of 2026-11-25,\nsec. 0.1).**",
    'status: confirmed (a)')
in_block_edit('D3', 'R6.DENY.6',
    "That decision (V5-D1) is recorded only in\nparaphrase, in the session-written #1169 comment 7099655517.",
    "That decision (V5-D1) is recorded only in\nparaphrase, in the session-written #1169 comment 7099655517; owner decision 3 accepts the reversal in\nthe owner's words.",
    'V5-D1 accepted by decision 3')
in_block_edit('D3', 'R6.DENY.6',
    "Until then the\nexpectations are deferred. The decision covers V4, V27, V27-glossary and V15 together (RE-1). Until it is made, each of the four\n"
    "rows carries both candidate expectations, each marked \"not authoritative; decided at r6 adoption\",\n"
    "and the gate reports `deferred-expectation` for it and never holds (sec. 16.5).",
    "Owner decision 3\nchose (a), confirming the PASS expectation knowingly. The decision covers V4, V27, V27-glossary and V15\n"
    "together (RE-1): each of the four rows carries the expectation of the candidate \"reversal adopted\" as\nits `expect` (R6.PUR.9).",
    'deferral replaced by the decision')
in_block_edit('D3', 'R6.CTRL.15',
    "It is adopted or rejected by the owner at r6's adoption;\n"
    "approving this draft does not adopt it. Until that decision, V4, V27, V27-glossary and V15 each\n"
    "carry both candidate expectations, marked \"not authoritative; decided at r6 adoption\", and the gate\n"
    "reports `deferred-expectation` for each (RE-1). If the reversal is rejected, V4's expectation is FAIL `deny-match` and the deny set\n"
    "needs",
    "%s accepts it (resolution (a) of\nR6.PUR.9), with effect from r6's adoption: V4, V27 and V27-glossary expect PASS and V15\n"
    "REVIEW_REQUIRED through `resid` (RE-1). The resolutions not chosen were these: had the reversal been\n"
    "rejected, V4's expectation would be FAIL `deny-match` and the deny set would need" % ('Owner decision 3 of 2026-11-25 (sec. 0.1)'),
    'reversal accepted; alternatives stated as not chosen')
in_block_edit('D3', 'R6.CTRL.15',
    "which is a plan-record change (sec. 12). V27 tests a sentence of the\nsame form and rests on the same decision, as do V27-glossary and V15, whose candidates are\n"
    "REVIEW_REQUIRED `unclassified` and FAIL `deny-match`; V15's FAIL candidate needs, in addition, a rule",
    "which is a plan-record change (sec. 12). V27 tests a sentence of the\nsame form and rests on the same decision, as do V27-glossary and V15, whose candidates were\n"
    "REVIEW_REQUIRED `unclassified` and FAIL `deny-match`; V15's FAIL candidate would have needed, in addition, a rule",
    'alternatives in the past conditional')
in_block_edit('D3', 'OBL-6',
    "Discharged by: the owner's recorded decision on the V4\nreversal at r6's adoption, among the resolutions (a), (b1) and (b2) of R6.PUR.9, and the reviewed rule\n"
    "records at `F`, including any new rule identifier that (b1) or (b2) needs.",
    "Discharged by: owner decision 3 of 2026-11-25 (sec. 0.1),\nwhich chose resolution (a) of R6.PUR.9 and takes effect with r6's adoption, and the reviewed rule\n"
    "records at `F`; r6 expects the outcomes of resolution (a), and no rule of the DR-1d or DR-2 form is\nrequired (rule content is plan content, R6.DENY.1; N5).",
    'discharge: decision 3 and the rule records at F')
in_block_edit('D3', 'R6.A1CFG.7',
    "The expected\noutcomes of V4, V27, V27-glossary and V15 are deferred until the owner's decision on the V4 reversal\n"
    "at r6's adoption (RE-1, OBL-6); until then they do not count toward S13.",
    "The expected\noutcomes of V4, V27, V27-glossary and V15 are those of owner decision 3 of 2026-11-25 (sec. 0.1;\n"
    "RE-1, OBL-6), and they count toward S13.",
    'S13 counts the four rows (the temporary narrowing of R6 ends)')
in_block_edit('D3', 'R6.CTRL.28',
    "V4, V27, V27-glossary and V15 are deferred to the owner's decision (R6.CTRL.15).",
    "V4, V27, V27-glossary and V15 carry the expectations of owner decision 3 (R6.CTRL.15).",
    'four rows decided')
edit('D3', 'sec. 32 table, OBL-6',
     "| OBL-6 | r6's adoption; plan freeze `F` | the owner's recorded decision (none of the four kinds); 4 for the rule records | no cycle; rests on V5-D1, pending owner confirmation |",
     "| OBL-6 | r6's adoption; plan freeze `F` | the owner's recorded decision (none of the four kinds), given as owner decision 3 of 2026-11-25; 4 for the rule records | no cycle; V5-D1's reversal accepted by owner decision 3 (sec. 0.1) |")

# =====================================================================================================
# D4 (iii): the T1' figure of item11-T1p is candidate evidence only
# =====================================================================================================
D4REF = 'owner decision 4 of 2026-11-25, sec. 0.1'
in_block_edit('D4iii', 'R6.EVID.4',
    "The figure whose\ncontrol needs `T1'` itself (item11-T1p) is an acceptance reference only while the objects of `T1'` it\n"
    "needs are reachable from `main`, and otherwise a historical measurement (OBL-23).",
    "The figure whose\ncontrol needs `T1'` itself (item11-T1p) is listed for identification only: it is candidate evidence,\n"
    "not acceptance support (%s; OBL-23)." % D4REF, 'item11-T1p: candidate evidence only')
in_block_edit('D4iii', 'R6.EVID.8',
    "it keeps `T1'` as\n  candidate evidence for the landing decision only, and its enduring claim stays a named provenance gap\n  (OBL-23: item11-T1p).",
    "its `T1'` figure is\n  candidate evidence only, not acceptance support, and no enduring claim rests on it (OBL-23:\n  item11-T1p; %s)." % D4REF,
    'item11-T1p: candidate evidence only')
in_block_edit('D4iii', 'R6.CTRL.19',
    "a figure that needs T1' itself is an acceptance reference only for a run that has\nT1' among its inputs;",
    "a figure that needs T1' itself is candidate evidence only, not acceptance support\n(OBL-23);",
    'T1\' figure: candidate evidence only')
in_block_edit('D4iii', 'OBL-23',
    "Its run on the exact tool candidate with `X` = `T1'` is candidate\n  evidence for the landing decision only; its enduring claim is a named provenance gap (AGENTS.md\n"
    "  sec. A.42 item 8, support off `main`) while the objects of `T1'` it needs are not reachable from\n"
    "  `main`. Whether a kind-1-only figure suffices for the landing gate is an owner question.",
    "Its earlier figure (176 lines at `T1'`) is candidate evidence only,\n  not acceptance support (%s, quoted: %s): it is not an acceptance reference for\n"
    "  the tool's landing, and no enduring claim rests on it." % (D4REF, dq('D4-T1P')),
    'owner question answered: candidate evidence only')
in_block_edit('D4iii', 'OBL-23',
    "for item11-T1p, the objects of `T1'` it needs reachable from `main`, or the owner's\n"
    "decision on a kind-1-only figure; otherwise the figure stays a historical measurement.",
    "item11-T1p's figure stays candidate evidence and is not used as an acceptance\nreference (owner decision 4).", 'discharge for item11-T1p')
in_block_edit('D4iii', 'OBL-23', "OPEN: T1'-bound evidence cannot qualify.\n", "",
              'OPEN marker removed: the gap is closed by narrowing the claim (AGENTS.md sec. A.42 item 8), as decision 4 (iii) directs')
edit('D4iii', 'sec. 32 table, OBL-23',
     "item11-T1p: 1 at `T1'` on the exact tool candidate, for the landing decision only | no cycle; item11-T1p's enduring claim is a named provenance gap while `T1'` is not reachable from `main` (open); whether a kind-1-only figure suffices for the landing gate is an owner question |",
     "item11-T1p: none; its earlier figure is candidate evidence only, not acceptance support (owner decision 4 of 2026-11-25) | no cycle; item11-T1p supports no acceptance and no enduring claim |")
edit('D4iii', 'sec. 32 adoption trace, item11-T1p',
     "| item11-T1p (OBL-23) | `T1'` | an acceptance reference that needs `T1'`'s exact tree | support off `main`: named provenance gap, open |",
     "| item11-T1p (OBL-23) | `T1'` | candidate evidence only (owner decision 4 of 2026-11-25) | provenance: no acceptance and no enduring claim rests on it |")

# =====================================================================================================
# D4 (i), R5: landing preparation, review record, one delta review
# =====================================================================================================
in_block_edit('D4i', 'R6.STAT.10',
    "\nOPEN: off-main support of adoption.",
    "\n- The independent review of the second correction round is recorded at #1169 comment 7166666428 and in\n"
    "  REVIEW-r6-round2.md of this directory; the owner's decisions on it are quoted in sec. 0.1. Before\n"
    "  adoption, one bounded delta review covers the changes of this revision (owner decision 5); with the\n"
    "  documents, it is part of the adoption's support. Preparing the directory and the review records for\n"
    "  landing approves no merge: the landing pull request's merge needs its own owner approval (AGENTS.md\n"
    "  sec. A.50 item 1), separate from adoption.\n"
    "OPEN: off-main support of adoption.", 'review record, delta review and separate merge approval stated (D4 (i), R5)')
edit('D4i', 'sec. 32 adoption trace, R6.STAT.10',
     "| R6.STAT.10 (the adoption record) | the r6 documents and their independent exact-head review | the adoption's support |",
     "| R6.STAT.10 (the adoption record) | the r6 documents and their independent exact-head review (the second-round review, #1169 comment 7166666428 and REVIEW-r6-round2.md; the delta review of this revision) | the adoption's support |")
edit('D5', 'sec. 32 adoption trace, owner decisions',
     "and the owner corrections OC-1 to OC-5 of 2026-11-25, quoted in the owner's words in #1169 comment 7163402499 |",
     "and the owner corrections OC-1 to OC-5 of 2026-11-25, quoted in the owner's words in #1169 comment 7163402499, and the owner decisions 1 to 5 of 2026-11-25, quoted in the owner's words in #1169 comment 7166844576 (sec. 0.1) |")

# =====================================================================================================
# D4 (ii): the LC-7 regeneration and byte-comparison procedure (for the delta review)
# =====================================================================================================
in_block_edit('D4ii', 'R6.TREE.12',
    "The regeneration is verified by a procedure, to be specified explicitly\n    and reviewed independently, in which the trusted checker establishes the expected output itself and\n"
    "    compares bytes; the evaluated tree's claim of regeneration is never sufficient. Until that procedure\n"
    "    is specified and reviewed, the path is REVIEW_REQUIRED for every candidate `L` (LC-7);",
    "The regeneration is verified by the procedure of R6.TREE.19, in which the\n    trusted checker establishes the expected output itself and compares bytes; the evaluated tree's claim\n"
    "    of regeneration is never sufficient. Until that procedure has passed its independent review (the\n"
    "    delta review of owner decision 4) and r6 is adopted, the path is REVIEW_REQUIRED for every candidate\n    `L` (LC-7);",
    'points to the procedure; REVIEW_REQUIRED kept until it is reviewed')
TREE19 = (
    "**R6.TREE.19** Regeneration and byte comparison for a derived artifact (LC-7, OC-4; owner decision 4 of\n"
    "2026-11-25, sec. 0.1). For the delta review: this procedure is specified for the independent review that\n"
    "owner decision 4 requires. Until that review accepts it and r6 is adopted, R6.TREE.12 keeps the\n"
    "derived-artifact case REVIEW_REQUIRED, and LC-7's expectation is unchanged.\n"
    "- Scope. Each path `p` of `L` that is a generated artifact of the configuration's derived set and is\n"
    "  changed on both sides to different blobs (the conflict case of R6.TREE.12).\n"
    "- Regeneration. The checker is the one committed on `main` and pinned by the configuration at `F` for\n"
    "  `p`'s class under the delegation contract (sec. 13). The tool runs it itself in a disposable full\n"
    "  clone at exact `L`, on the committed source paths of `L` for `p` only, read through the verified\n"
    "  reader (R6.REC.17); this run alone establishes the expected bytes. No file, output, log or claim of\n"
    "  regeneration supplied by the evaluated tree or by the caller is an input.\n"
    "- Comparison. The bytes the checker writes for `p` are compared with the blob `L[p]`, byte for byte over\n"
    "  the whole file, with no normalization of line endings, whitespace, timestamps or metadata. The run\n"
    "  records the checker blob sha256, the exact command line, the working directory, the exit status, and\n"
    "  the sha256 and length of the regenerated bytes and of `L[p]`.\n"
    "- Failure. Equal bytes discharge the derived-artifact case for `p`; any difference is FAIL\n"
    "  `delegated-evidence-invalid` for `p`. A checker that cannot run, exits nonzero, writes no output for\n"
    "  `p`, or needs an input that is missing or unpinned leaves `p` REVIEW_REQUIRED\n"
    "  `delegated-evidence-missing` (obligation `MAIN`); none of these is PASS. A reconciliation record, a CI\n"
    "  log or a host attestation never stands in for the comparison.\n"
    "Sources: OC-4, RE-18. Controls: none (procedure for the delta review; once it is accepted, LC-7's cases\n"
    "are restated by an owner-approved expectation change).\n\n")
edit('D4ii', 'R6.TREE.19 (new, after R6.TREE.12)', "\n**R6.TREE.13**", "\n" + TREE19 + "**R6.TREE.13**")

# =====================================================================================================
# N6: HIST-4
# =====================================================================================================
edit('N6', 'Appendix H HIST-4',
     "S1-D1 to S1-D3 and the\n  decisions of 2026-11-24; recorded on GitHub only by the coordinating session, without the owner's\n"
     "  words, the route authority of #1169 comment 7093128173 and v3 D1-D4, V5-D1 and V5-D2 (#1169 comment\n  7099655517).",
     "S1-D1 to S1-D3 and the\n  owner decisions of 2026-11-24 quoted in v6.0e (E-008, v6.0e line 95); recorded on GitHub only by the\n"
     "  coordinating session, without the owner's words, the route authority of #1169 comment 7093128173,\n"
     "  v3 D1-D4, V5-D1 and V5-D2 (#1169 comment 7099655517), and DI-2 of 2026-11-24 (#1169 comment\n  7121574479).")

# =====================================================================================================
# D5: requirements resting on S1-D3 (B1-B6), identified by a rule stated before the marking
# =====================================================================================================
B_LABEL = collections.OrderedDict([
    ('B1', 'acceptance reads admission; harness results never acceptable'),
    ('B2', 'native delegated execution in a clone at `X`; independent verification'),
    ('B3', "configuration admission from `F`'s pin table"),
    ('B4', 'commits of `C` classified path by path; widening reviews with coverage'),
    ('B5', 'engine purity over the adapter companions; guard pins in the adapter'),
    ('B6', 'control reporting with PASS, FAIL, SKIP and NOT RUN; predicates equal to expectations'),
])
B_ITEMS = collections.OrderedDict([
    ('B1', ['E-095', 'E-1191', 'E-1207']),
    ('B2', ['E-1038', 'E-1039', 'E-1040', 'E-1224', 'E-1225', 'E-1226', 'E-1227', 'E-1229']),
    ('B3', ['E-143', 'E-144', 'E-145', 'E-1208', 'E-1209', 'E-1210', 'E-1211']),
    ('B4', ['E-1305', 'E-162', 'E-1230', 'E-1231', 'E-1232']),
    ('B5', ['E-1377', 'E-1378', 'E-1428', 'E-1233', 'E-1387']),
    ('B6', ['E-1189', 'E-1190', 'E-1191']),
])
B_CONTROLS = collections.OrderedDict([
    ('B1', ['X11']), ('B2', ['G4', 'G5', 'G6', 'G7', 'G8']), ('B3', ['TR1', 'TR2', 'TR3', 'TR5']),
    ('B4', ['R16', 'R17', 'A12r']), ('B5', ['Z9g', 'Z9h']), ('B6', [])])
TIER_C = collections.OrderedDict([
    ('R6.REC.7', ('B4', 'states that a superseding record that widens the record it supersedes carries its widening review')),
    ('R6.REC.17', ('B2', 'states that the native clones of sec. 13 are full clones')),
])
KEYWORD_READ_NOT_MARKED = collections.OrderedDict([
    ('R6.REC.1', '"pin table" names where PIN_OK entries are listed; the record chain predates B3 (E-135)'),
    ('R6.REC.15', 'PIN_OK validity (E-164, RV-019); not the admission passage of B3'),
    ('R6.REC.18', 'execution identity (R-D3); names the native checker runs only to defer to sec. 13'),
    ('R6.REC.23', 'host reads; "admission refuses" names the consequence of a failed read'),
    ('R6.REC.25', 'residual trust; names the admission snapshot'),
    ('R6.GATE.2', '"mutation harness" and "NOT RUN" in the schema, not the control harness of B1 or the reporting of B6'),
    ('R6.GATE.10', 'the mutation harness, not the control harness of B1'),
    ('R6.GATE.13', 'the gate\'s own controls (Q1, Q8, RD-2)'),
    ('R6.GATE.14', 'CI under AGENTS.md sec. A.44 (V2-098, Q1)'),
    ('R6.GATE.16', 'RT-L2\'s NOT RUN rule (OD-18, Q2)'),
])
# The control ids' introduction by B1-B6 is read from E-034 (v6.0e sec. 0.2): check it.
_e034 = INV['E-034']['text']
for b, ctrls in B_CONTROLS.items():
    row = [l for l in _e034.split('\n') if l.startswith('| Stage 1 %s:' % b)]
    if len(row) != 1:
        PROBLEMS.append('E-034 row for %s' % b)
for b, items in B_ITEMS.items():
    for i in items:
        if i not in INV or INV[i]['doc'] != 'DESIGN-v6.0e.md':
            PROBLEMS.append('B item %s not a v6.0e inventory item' % i)


def s1d3_identify(reqs_idx):
    out = collections.OrderedDict()
    for q in reqs_idx:
        hits = []
        for b in B_ITEMS:
            s = [x for x in q['sources'] if x in B_ITEMS[b]]
            c = [x for x in q['controls'] if x in B_CONTROLS[b]]
            if s or c:
                hits.append((b, s, c))
        if hits:
            out[q['id']] = ('A' if any(h[1] for h in hits) else 'B', hits)
        elif q['id'] in TIER_C:
            out[q['id']] = ('C', [(TIER_C[q['id']][0], [], [])])
    return out


S1D3 = s1d3_identify(REQ_IN)
CONFIRMED_SET = set(CL_V) | set(CL_R)
S1D3_PENDING = [r for r in S1D3 if r not in CONFIRMED_SET and r not in CL_S and r not in CL_D]
S1D3_CONFIRMED = [r for r in S1D3 if r in CONFIRMED_SET]
for rid in S1D3_PENDING:
    global_T_before = T
    a, b = block_span(rid)
    blk = T[a:b]
    if PEND3 in blk or PEND_TXT in blk:
        PROBLEMS.append('S1-D3 mark: %s already marked' % rid)
        continue
    k = blk.rfind('\nSources:')
    if k >= 0:
        new = blk[:k] + '\n' + PEND3 + blk[k:]
    else:
        k = blk.rfind(' Sources:')
        if k < 0:
            PROBLEMS.append('S1-D3 mark: no Sources in ' + rid)
            continue
        new = blk[:k] + ' ' + PEND3 + blk[k:]
    T = T[:a] + new + T[b:]
    log('D5-S1D3', rid, 'marked "%s" (rule %s)' % (PEND3, S1D3[rid][0]))

# =====================================================================================================
# sec. 0.1: the owner's decisions quoted, and how r6 applies them
# =====================================================================================================
SEC01 = '\n'.join([
    '### 0.1 Owner decisions of 2026-11-25 on the decision package', '',
    'The owner decided on the decision package after the independent review recorded at #1169 comment '
    '7166666428 (REVIEW-r6-round2.md). The decisions are recorded in #1169 comment 7166844576 (%s), posted '
    'from the `amaybaum` account by the coordinating session, which introduces them as "%s" Decisions 1 to 4, '
    'byte-exact (each line prefixed by "> "):' % (DEC_AT, OWNER_LINE), '',
    '\n'.join(('> ' + x) if x else '>' for x in DEC_1_4.split('\n')), '',
    'Decision 5, quoted: %s, %s, %s and %s' % (dq('D5-REV'), dq('D5-S1D3'), dq('D5-PEND'), dq('D5-SCOPE')), '',
    'How r6 applies them; each takes effect only with r6\'s adoption (R6.STAT.1):', '',
    '- Decision 1. The %d requirements the review classes as necessary for scientifically valid retirement and '
    'the %d it classes as necessary for reliable verification carry "Confirmed by owner decision 1". R6.STAT.4 '
    'and R6.EVID.5 are scope statements with no check of their own. R6.OUT.15 is deferred, with the `replay` '
    'mode of R6.REC.24 and control TR45-opB; its text is kept as the deferred specification and the '
    'accountable Issue is #1169. Every mention of the offline replay in this design refers to that deferred '
    'specification. The expectation file keeps the rows TR45-opB and TR45 (a composite of TR45-opB and '
    'TR45-opC) unchanged in this text-only revision; how the deferred row is carried in the expectation file '
    'is a matter for the delta review and a later owner-approved expectation change.' % (len(CL_V), len(CL_R)),
    '- Decision 2. The classes of the 12 flagged requirements are recorded in FRESH-AUTHORIZATION.md, sec. 2.',
    '- Decision 3. V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED through `resid`; no deny rule '
    'is added (R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6, R6.A1CFG.7). The owner\'s caveat, quoted: %s'
    % dq('D3-CAVEAT'),
    '- Decision 4. (i) The review record is REVIEW-r6-round2.md; preparing the directory for landing approves '
    'no merge (R6.STAT.10). (ii) The regeneration and byte-comparison procedure is R6.TREE.19, for the delta '
    'review; LC-7 stays REVIEW_REQUIRED until that review accepts it. (iii) The earlier `T1\'` figure of '
    'item11-T1p is candidate evidence only, not acceptance support (OBL-23).',
    '- Decision 5. The %d requirements found to rest on owner decision S1-D3 (B1-B6) and not confirmed by '
    'decision 1 are marked "%s" (FRESH-AUTHORIZATION.md, sec. 3); r6\'s adoption is not used as their '
    'authorization. A requirement left unconfirmed stays pending and is never withdrawn by that alone; '
    'withdrawal needs an explicit owner choice, with its verification traced (R6.STAT.5). R6.STAT.8 is '
    'confirmed as a requirement; the restatement of the landing-order decision in the owner\'s words, which '
    'it requires before adoption, is still owed.' % (len(S1D3_PENDING), PEND3),
    '- One bounded delta review covers the changes of this revision before adoption (R6.STAT.10).', ''])
edit('D5', 'sec. 0.1 (new)', "\n***\n\n## 1. Notation and symbols", "\n" + SEC01 + "\n***\n\n## 1. Notation and symbols")

# =====================================================================================================
# blank line before any requirement directly after text (as F8)
# =====================================================================================================
_lines = T.split('\n')
_out = []
for _l in _lines:
    _m = re.match(r'\*\*(R6\.[A-Z0-9]+\.\d+|OBL-\d+)\*\*', _l)
    if _m and _out and _out[-1].strip() != '':
        _out.append('')
        log('meta', _m.group(1), 'blank line inserted before the requirement')
    _out.append(_l)
T = '\n'.join(_out)

# =====================================================================================================
# requirement index
# =====================================================================================================
KIND = {q['id']: q for q in REQ_IN}
KIND = dict(KIND)
KIND['R6.TREE.19'] = {'section': 'TREE', 'section_number': 20, 'kind': 'definition'}
PEND_IN = {q['id']: list(q['pending_owner_confirmation']) for q in REQ_IN}
PEND = {}
OWNDEC = {}
for q in REQ_IN:
    rid = q['id']
    PEND[rid] = ['S1-D3'] if rid in S1D3_PENDING else []
    eff = None
    if rid in CL_V:
        eff = 'confirmed: necessary for scientifically valid retirement'
    elif rid in CL_R:
        eff = 'confirmed: necessary for reliable verification'
    elif rid in CL_S:
        eff = 'scope statement without a check of its own'
    elif rid in CL_D:
        eff = 'deferred'
    OWNDEC[rid] = [] if eff is None else [collections.OrderedDict([
        ('record', '#1169 comment 7166844576'), ('decision', 1), ('effect', eff),
        ('decision_basis', PEND_IN[rid])])]
for rid in ('R6.PUR.9', 'R6.DENY.6', 'R6.CTRL.15', 'OBL-6'):
    OWNDEC[rid].append(collections.OrderedDict([('record', '#1169 comment 7166844576'), ('decision', 3),
                                                ('effect', 'resolution (a) chosen'), ('decision_basis', ['V5-D1'])]))
OWNDEC['OBL-23'] = [collections.OrderedDict([('record', '#1169 comment 7166844576'), ('decision', 4),
                                             ('effect', "item11-T1p's earlier T1' figure is candidate evidence only"),
                                             ('decision_basis', [])])]
OWNDEC['R6.TREE.19'] = [collections.OrderedDict([('record', '#1169 comment 7166844576'), ('decision', 4),
                                                 ('effect', 'procedure established for the delta review'),
                                                 ('decision_basis', [])])]
PEND['R6.TREE.19'] = []
for rid in S1D3_PENDING:
    log('D5-S1D3', 'REQ:' + rid, 'pending key S1-D3')
for rid in MARKED_IN:
    log('D1' if rid not in CL_S + CL_D else ('D1-scope' if rid in CL_S else 'D1-defer'), 'REQ:' + rid,
        'pending keys %s moved to owner_decision (decision 1)' % ', '.join(PEND_IN[rid]))


def req_index(reqs, kind, pend, owndec=None):
    out = []
    for rid, q in reqs.items():
        if rid not in kind:
            PROBLEMS.append('requirement without kind: ' + rid)
            continue
        sec, num, knd = kind[rid]['section'], kind[rid]['section_number'], kind[rid]['kind']
        if knd == 'testable':
            ver = ['controls']
        elif rid.startswith('OBL-'):
            ver = [rid]
        else:
            obls = []
            for o in re.findall(r'\bOBL-\d+\b', q['text']):
                if o not in obls:
                    obls.append(o)
            ver = obls or ['review']
        e = collections.OrderedDict([('id', rid), ('section', sec), ('section_number', num), ('kind', knd),
                                     ('sources', q['sources']), ('controls', q['controls']), ('verification', ver),
                                     ('open', q['open']), ('pending_owner_confirmation', pend.get(rid, []))])
        if owndec is not None:
            e['owner_decision'] = owndec.get(rid, [])
        out.append(e)
    return out


REQS = parse_reqs(T)
REQ_OUT = req_index(REQS, KIND, PEND, OWNDEC)
REPLAY_OK = dumps(req_index(parse_reqs(T_IN), KIND, PEND_IN)) == REQ_TXT
log('meta', 'REQUIREMENTS.json', 'field owner_decision added to every entry (the record, decision, effect and the decision basis keys); pending keys now S1-D3 only; R6.TREE.19 added')

# =====================================================================================================
# EXPECTATIONS.json: decision 3 selects the "reversal adopted" candidates; nothing else changes
# =====================================================================================================
EXP_OUT = copy.deepcopy(EXP)
EXP_OUT['record_id'] = 'r6-final4-1'
log('meta', 'EXPECTATIONS.json', 'record_id r6-final3-1 -> r6-final4-1')
V4ROWS = ('V4', 'V27', 'V27-glossary', 'V15')
RIDX_IN = collections.OrderedDict((r['id'], r) for r in EXP['rows'])
SELECTED = {}
for r in EXP_OUT['rows']:
    if r['id'] not in V4ROWS:
        continue
    cands = r['candidate_expectations']
    adopted = [c for c in cands if c['label'].startswith('reversal adopted')]
    rejected = [c for c in cands if c['label'].startswith('reversal rejected')]
    if len(adopted) != 1 or len(rejected) != 1 or r['expect'] != {'outcome': 'DEFERRED'}:
        PROBLEMS.append('V4 group row %s: unexpected candidates' % r['id'])
        continue
    SELECTED[r['id']] = (adopted[0], rejected[0])
    new = collections.OrderedDict()
    for k, v in r.items():
        if k == 'expect':
            new['expect'] = copy.deepcopy(adopted[0]['expect'])
        elif k == 'candidate_expectations':
            continue
        elif k == 'flags':
            fl = []
            for f in v:
                if f.startswith('RE-1: both candidate expectations'):
                    fl.append('owner decision 3 of 2026-11-25 (#1169 comment 7166844576): resolution (a); `expect` is the '
                              'candidate expectation recorded under RE-1 as "%s"; the candidate "reversal rejected (a plan '
                              'rule record of this form under a new identifier, sec. 12; DR-1d and DR-2 stay retired, '
                              'sec. 33)" is not selected (V4-COMPARISON.md)' % adopted[0]['label'])
                elif f.startswith('pending owner confirmation (see PARAPHRASED-DECISIONS.md): rests on V5-D1'):
                    fl.append('rests on V5-D1, whose reversal owner decision 3 accepts in the owner\'s words; no deny rule is added')
                else:
                    fl.append(f)
            new['flags'] = fl
        else:
            new[k] = v
    r.clear()
    r.update(new)
    log('D3', 'EXP:' + r['id'], 'expect := the "reversal adopted" candidate; candidate_expectations removed (R6.GATE.2: deferred rows only); flags restated')
MIG_OUT_TXT = MIG_TXT

# =====================================================================================================
# quotations
# =====================================================================================================
QUOTES = dict(TX.QUOTES)
QUOTES.update({
    'Q-7166844-D1': (DEC_ID, DEC[1]), 'Q-7166844-D2': (DEC_ID, DEC[2]), 'Q-7166844-D3': (DEC_ID, DEC[3]),
    'Q-7166844-D4': (DEC_ID, DEC[4]), 'Q-7166844-D5': (DEC_ID, DEC[5]), 'Q-7166844-OWN': (DEC_ID, OWNER_LINE),
    'Q-7166666-HEAD': (REV_ID, 'Independent review of A1 design r6 at `400e4b4fe5f3474b96ee4faa3c437e76e09db782`: reviewer text, verbatim.'),
})
for k, v in DQ.items():
    QUOTES['DQ-' + k] = (DEC_ID, v)
for qid, (cid, q) in QUOTES.items():
    if cid not in COMM or COMM[cid]['body'].count(q) < 1:
        PROBLEMS.append('quote %s not found in comment %s' % (qid, cid))
COMMENTS = list(TX.COMMENTS) + [REV_ID, DEC_ID]
BODY_SHA = collections.OrderedDict((cid, sha(COMM[cid]['body'])) for cid in COMMENTS)


def quote(qid):
    cid, q = QUOTES[qid]
    return '#1169 comment %s (%s): "%s"' % (cid, COMM[cid]['created_at'], q)


def bq(s):
    return '\n'.join(('> ' + x) if x else '>' for x in s.rstrip('\n').split('\n'))


# =====================================================================================================
# decision bases (text2's, with R1 and N2 applied, and the S1-D3 entry of decision 5)
# =====================================================================================================
NOTE_7130 = ("#1169 comment 7130449822 quotes the owner's adoption, in the owner's words, of DESIGN-v6.0e.md at its "
             "exact SHA-256, whose text contains this quote; confirming the requirements keyed here re-confirms a "
             "settled decision (R1). The adoption of v6.0e is context and is not treated as authorizing any r6 "
             "requirement (F9 of the grouped presentation); r6's adoption, and for these requirements owner decision 1, "
             "is the authority.")
BASES = []
for key, cls, head, qids, where, says, rule, note in TX.BASES:
    if key == 'V5-D1':
        cut = says.index(' As a consequence')
        note = ((note + ' ') if note else '') + (
            'Consequence, from v6.0e\'s measurement and not stated in the record (N2):' + says[cut:] +
            ' Owner decision 3 of 2026-11-25 (#1169 comment 7166844576) accepts the reversal in the owner\'s words.')
        says = says[:cut]
        _old1 = ('The four expectation rows V4, V27, V27-glossary and V15 carry both candidate expectations, each '
                 '"not authoritative; decided at r6 adoption" (RE-1).')
        if not note.startswith(_old1):
            PROBLEMS.append('V5-D1 note')
        note = ('The four expectation rows V4, V27, V27-glossary and V15 carry the expectations of resolution (a) '
                '(owner decision 3).') + note[len(_old1):]
        log('D3', 'AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D1', 'note: the four rows carry the expectations of resolution (a)')
        log('N2', 'AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D1', 'the v6.0e-derived consequence moved out of "what the record says"')
    if key == 'V5-D2':
        note = ('The same record holds a separate decision, quoted: %s; it is the more direct basis for R6.PUR.8 (N2).'
                % quote('Q-7099-LIMIT'))
        log('N2', 'AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D2', 'the coverage-limitation decision named as the direct basis of R6.PUR.8')
    if key in ('v6.0e line 31', 'v6.0e line 54'):
        note = NOTE_7130
        log('R1', 'AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: ' + key, 'the 7130449822 adoption of v6.0e noted')
    if key == 'v6.0e line 95':
        note = note + ' Confirming the requirements keyed here re-confirms a settled decision (R1).'
        log('R1', 'AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: ' + key, 're-confirmation of a settled decision noted')
    BASES.append((key, cls, head, qids, where, says, rule, note))
BASES.append(('S1-D3', 'iii', 'Owner decision S1-D3 (specify B1-B6: admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting)',
              [], 'DESIGN-v5.5.9.md, lines 94-98; CHANGES-v5.2.md, line 22 ("S1-D3: specify the fixes for B1-B6.") and sec. 2; v6.0e sec. 0.2 (inventory item E-034) maps B1-B6 to the v6.0e passages and controls that answer them.',
              'specify configuration admission, native delegated execution, the classification of `C`, widening reviews, engine purity over the adapter companions, and control reporting (B1-B6).',
              'FRESH-AUTHORIZATION.md, sec. 3 (rules A, B and C, stated before the marking).',
              'Identified under owner decision 5; marked "%s" except where decision 1 confirmed the requirement.' % PEND3))
BASE_KEYS = [b[0] for b in BASES]
CLS = {b[0]: b[1] for b in BASES}
BYKEY = collections.OrderedDict((k, []) for k in BASE_KEYS)
for rid in MARKED_IN:
    for k in PEND_IN[rid]:
        BYKEY[k].append(rid)
for rid in S1D3:
    BYKEY['S1-D3'].append(rid)


def status_of(rid):
    if rid in CL_V:
        return 'confirmed by owner decision 1 (necessary for scientifically valid retirement)'
    if rid in CL_R:
        return 'confirmed by owner decision 1 (necessary for reliable verification)'
    if rid in CL_S:
        return 'scope statement without a check of its own (owner decision 1)'
    if rid in CL_D:
        return 'deferred (owner decision 1)'
    if rid in S1D3_PENDING:
        return 'pending owner confirmation for the adoption decision (S1-D3)'
    return 'not marked; takes effect only by r6\'s adoption'


OPTIONS_TXT = ('Options: (a) confirm in the owner\'s own words; (b) fresh authorization; (c) withdraw, only by an '
               'explicit owner choice. Non-confirmation leaves the requirement pending.')


def para_md():
    L = ['# r6: requirements resting on paraphrased or unrecorded owner decisions', '',
         'This list does not reconstruct any authorization. Each entry names an owner decision that r6\'s requirements '
         'rest on, the class of its record, what the record says, the rule by which the requirements were found, and '
         'the requirements found with their status after the owner\'s decisions of 2026-11-25 (#1169 comment '
         '7166844576, quoted in DESIGN-r6.md sec. 0.1). A requirement still pending is marked in DESIGN-r6.md with '
         '"%s" and carries its key in the field `pending_owner_confirmation` of REQUIREMENTS.json; the decision basis '
         'of a requirement the owner decided is kept in its field `owner_decision`. The exact wording, purpose and '
         'consequences of each listed requirement are in FRESH-AUTHORIZATION.md; the evidence for each class is in '
         'AUTHORIZATIONS.md.' % PEND3, '',
         'Classes of record (verified by reading the #1169 comments with GET requests):', '',
         '- %s: a comment that quotes the owner\'s words explicitly; such decisions need no entry here and are listed in AUTHORIZATIONS.md;' % TX.CLASS_TEXT['i'],
         '- %s: a comment posted from the `amaybaum` account by the coordinating session that records an owner decision in the session\'s words and quotes no owner words;' % TX.CLASS_TEXT['ii'],
         '- %s: the decision is stated only in design documents relayed in session, with no comment id.' % TX.CLASS_TEXT['iii'], '',
         'Options for every entry:', '',
         '- (a) confirm in the owner\'s own words: the owner records the decision in a comment, which r6 quotes byte-exact with author and time (AGENTS.md sec. A.42 item 7);',
         '- (b) fresh authorization: the owner decides the question anew, in a recorded decision, and r6 cites that record;',
         '- (c) withdraw the requirement, only by an explicit owner choice: the requirement, or the part of it that rests on the decision, is removed or narrowed, with its verification traced (R6.STAT.5).', '',
         'Non-confirmation is none of these: a requirement the owner does not confirm stays pending, and r6 cannot be '
         'adopted while it is pending (R3; owner decision 5, quoted: %s).' % dq('D5-PEND'), '',
         'Status after 2026-11-25: of the 44 requirements previously marked, %d are confirmed by owner decision 1, '
         '%d are scope statements and %d is deferred; %d requirements resting on S1-D3 are pending.'
         % (len(CL_V) + len(CL_R), len(CL_S), len(CL_D), len(S1D3_PENDING)), '']
    for key, cls, head, qids, where, says, rule, note in BASES:
        L += ['***', '', '## ' + head, '', '- Key: `%s`' % key, '- Class: %s' % TX.CLASS_TEXT[cls]]
        if qids:
            L.append('- Record on GitHub (exact text):')
            for qid in qids:
                L.append('  - ' + quote(qid))
        else:
            L.append('- Record on GitHub: none.')
        L += ['- Where else stated: ' + where, '- What it says: ' + says, '- Rule used to find the requirements: ' + rule]
        rq = BYKEY[key]
        if rq:
            L.append('- Requirements affected, with their status:')
            for r in rq:
                L.append('  - %s: %s' % (r, status_of(r)))
        else:
            L.append('- Requirements affected: none found by the rule; nothing in r6 is marked for this entry.')
        if note:
            L.append('- Note: ' + note)
        L += ['- ' + OPTIONS_TXT, '']
    L += ['***', '', '## Requirements not marked', '',
          '- R6.DENY.1 and R6.DENY.2 cited E-1001 only because that item mentions the retired DR-1d and DR-2. Their content '
          '(rule records are plan records; the controls run on pinned rule inputs) does not depend on V5-D1, so they are not '
          'marked. Like every requirement of r6 they take effect only by r6\'s adoption; they are listed in '
          'FRESH-AUTHORIZATION.md. The review would class both as necessary for reliable verification.', '']
    return '\n'.join(L)


PARA_OUT = para_md()
log('D1', 'PARAPHRASED-DECISIONS.md', 'regenerated: every listed requirement with its status after decision 1')
log('R3', 'PARAPHRASED-DECISIONS.md', 'option (c) only by explicit owner choice; non-confirmation leaves a requirement pending')
log('D5-S1D3', 'PARAPHRASED-DECISIONS.md', 'entry S1-D3 added with the identified requirements')

# =====================================================================================================
# AUTHORIZATIONS.md
# =====================================================================================================
CLASS_I = []
for _e in TX.CLASS_I:
    if _e[0] == '7162098696':
        _u = _e[6].replace('the `candidate_expectations` and DEFERRED outcome of the four V4-group rows (RE-1)',
                           'the `candidate_expectations` and DEFERRED outcome that the four V4-group rows carried until owner decision 3 (RE-1)')
        if _u == _e[6]:
            PROBLEMS.append('CLASS_I 7162098696 text')
        _e = _e[:6] + (_u,)
        log('D3', 'AUTHORIZATIONS.md: 7162098696', 'relied-on text: the V4-group candidates carried until decision 3')
    CLASS_I.append(_e)
CLASS_I = CLASS_I + [
    (DEC_ID, DEC_AT, 'owner decisions 1-5 on the decision package of r6', ['Q-7166844-D1', 'Q-7166844-D2', 'Q-7166844-D3', 'Q-7166844-D4', 'Q-7166844-D5'],
     'confirming the 41 requirements of decision 1 and the two scope statements; deferring R6.OUT.15 with its replay mode; the classes of the 12 flagged requirements; resolution (a) of the V4 group; the three provenance fixes; this final text-only revision and one bounded delta review.',
     'adoption, implementation, freezing, trial execution or merging (decision 5); merge approval of the landing (decision 4: "Merge approval remains separate."); using adoption as blanket authorization for the requirements resting on S1-D3 (decision 5); scientifically unsupported claims about finiteness (decision 3).',
     'the confirmation, scope and deferral notes of decision 1; R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6, R6.A1CFG.7 and the four V4-group rows (decision 3); R6.STAT.10, R6.TREE.19, OBL-23 (decision 4); the S1-D3 marks (decision 5); sec. 0.1 of DESIGN-r6.md.'),
]
CLASS_I_PATTERN = (
    'Each of these comments is posted from the `amaybaum` account by the coordinating session. Each '
    'contains a passage introduced as the owner decision and quoted; that passage is the owner\'s own '
    'words. Where the owner approves a proposal "as proposed" or "including the refinements", the '
    'proposal text (quoted in the comment as relayed from the owner\'s independent review) and the '
    'session\'s refinements are approved by reference to that quoted approval; the refinements themselves '
    'are the session\'s words. None of these records adopts r6 or any requirement of it (N1): 7130449822 adopts '
    'v6.0e and authorizes its local implementation; 7153270569 starts the design; 7158516152 authorizes a '
    'read-only assessment; the others authorize drafting, correction, presentation or the decisions they state '
    'on r6, and each excludes adoption of r6.')
log('N1', 'AUTHORIZATIONS.md sec. 1', 'what each class (i) record authorizes stated; none adopts r6')
log('D5', 'AUTHORIZATIONS.md', 'comments 7166666428 and 7166844576 added; 7166844576 as a class (i) record')


def auth_md():
    L = ['# r6: authorizations and decision records the design relies on', '',
         'Every decision label the design relies on, classified by its record, with the evidence and with what it '
         'permits and does not permit. The comments were read with GET requests; for each, the time is the API\'s '
         '`created_at` and the body digest is the sha256 of the body as returned.', '',
         'Classes: %s; %s; %s.' % (TX.CLASS_TEXT['i'], TX.CLASS_TEXT['ii'], TX.CLASS_TEXT['iii']), '',
         '| Comment | created_at | Body sha256 |', '|---|---|---|']
    for cid in COMMENTS:
        L.append('| %s | %s | %s |' % (cid, COMM[cid]['created_at'], BODY_SHA[cid]))
    L += ['', '***', '', '## 1. Class (i): the owner\'s own words on GitHub', '', CLASS_I_PATTERN, '']
    for cid, when, what, qids, permits, notp, used in CLASS_I:
        L += ['### #1169 comment %s (%s): %s' % (cid, when, what), '', 'Owner\'s words and approved text (exact):', '']
        for qid in qids:
            q = QUOTES[qid][1]
            if '\n' in q:
                if L[-1] != '':
                    L.append('')
                L += [bq(q), '']
            else:
                L.append('- "%s"' % q)
        if L[-1] != '':
            L.append('')
        L += ['- Permits: ' + permits, '- Does not permit: ' + notp, '- Relied on by: ' + used, '']
    L += ['***', '', '## 2. Class (ii): session-written records without owner words', '',
          'Each record below opens with "Recorded by the coordinating session" and states owner decisions in the '
          'session\'s words. It shows that a decision was reported, not its wording. By itself it permits nothing '
          'for r6: a requirement resting on it needs confirmation in the owner\'s words or fresh authorization '
          '(quoted instruction of #1169 comment 7162098696: "%s"). Owner decision 1 of 2026-11-25 confirms the '
          'requirements so marked below.' % QUOTES['Q-7162-PARA'][1], '']
    for key, cls, head, qids, where, says, rule, note in BASES:
        if cls != 'ii':
            continue
        L += ['### ' + head, '', '- Key: `%s`' % key]
        for qid in qids:
            L.append('- ' + quote(qid))
        L += ['- Where else stated: ' + where, '- What the record says was decided: ' + says]
        if note:
            L.append('- Note: ' + note)
        L += ['- Permits: nothing by itself for r6.',
              '- Does not permit: treating the session\'s paraphrase as the owner\'s wording; reconstructing authorization from it.',
              '- Relied on by: ' + ('; '.join('%s (%s)' % (r, status_of(r)) for r in BYKEY[key]) or 'no requirement'), '']
    L += ['***', '', '## 3. Class (iii): no GitHub record', '',
          'These decisions are stated only in design documents relayed in session, each without a comment id. A '
          'search of all comments on #1169 for distinctive phrases of each (for example "S1-D1", "R-D1", "A-D5", '
          '"three stricter", "chained edits", "Approve O-1 option (b)", "historical authorization verification '
          'entirely", "Authorize the Stage A review") found no record of the decision; the labels S1-D1, S1-D2 and '
          'S1-D3 occur only in later session-written result comments. #1169 comment 7158801838 lists them as owner '
          'decisions without a record: "%s"' % QUOTES['Q-7158801-NOREC'][1], '']
    for key, cls, head, qids, where, says, rule, note in BASES:
        if cls != 'iii':
            continue
        L += ['### ' + head, '', '- Key: `%s`' % key, '- Where stated: ' + where, '- What it says: ' + says,
              '- Permits: nothing for r6.',
              '- Does not permit: citing the design document\'s quotation or label as an owner record.',
              '- Relied on by: ' + ('; '.join('%s (%s)' % (r, status_of(r)) for r in BYKEY[key]) or 'no requirement')]
        if note:
            L.append('- Note: ' + note)
        L.append('')
    L += ['***', '', '## 4. Labels that are not owner decisions', '',
          '- D1 to D8 of the Stage 1 review: review findings, applied by owner decision S1-D2 (class (iii)).',
          '- B1 to B6 of the Stage 1 review: implementation defects, whose fixes owner decision S1-D3 (class (iii)) asked to be specified; not the splice boundary cases B1-B6 of v6.0e sec. 10.1 (E-1092 to E-1097) or the r5 findings B1-B6.',
          '- C3 and C4: findings of the v5.4 review addendum, applied under the owner decisions R-D1 to R-D5 (class (iii)).',
          '- OD-1 to OD-31, MC-*, VD-*, ME-* (DECISIONS.md), RD-1 to RD-35 (RESIDUAL.md), RE-1 to RE-38 (RESIDUAL-2.md): '
          'recommendations prepared by the coordinating session, approved by the owner as the basis for drafting r6 '
          '(class (i): #1169 comments 7160281751, 7160980912, 7162098696). The approval covers drafting; the content '
          'takes effect only by r6\'s adoption.',
          '- OC-1 to OC-5: items 1 to 4 and 6 of the proposal quoted in #1169 comment 7163402499, authorized by the '
          'owner "as proposed" in the same comment (class (i)).',
          '- R1 to R6 and N1 to N6: findings of the independent review recorded at #1169 comment 7166666428 '
          '(REVIEW-r6-round2.md), addressed under owner decision 5.',
          '- E-*, V1-*, V2-*, A-*, RV-*: inventory and review items (provenance), not decisions.', '',
          '***', '', '## 5. Review records', '',
          '- #1169 comment 7166666428 (%s) records the independent review of the second correction round, reviewer '
          'text verbatim (REVIEW-r6-round2.md). It is a review record, not an owner decision: "%s"' % (REV_AT, QUOTES['Q-7166666-HEAD'][1]), '']
    return '\n'.join(L)


AUTH_OUT = auth_md()

# =====================================================================================================
# FRESH-AUTHORIZATION.md
# =====================================================================================================
NOTES = dict(TX.NOTES)
NOTES['R6.PUR.9'] = (
    'States the decision on the V4 reversal, resolution (a) of owner decision 3, and the resolutions not chosen.',
    'V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED through `resid`; the four rows count toward S13; no deny rule is added.',
    'The decision and the option statement are lost; the four rows would have no stated basis; ' + TX.NOT_AUTH_GENERIC + '.',
    'Records the owner\'s decision and caveat; a rejection would have needed a new rule identifier (F5), and V15\'s FAIL a rule of the DR-1d form (F6).',
    'Resolution (a) permits V4, V27 and V27-glossary to PASS and V15 to be REVIEW_REQUIRED, where v2\'s demonstration expected V4 FAIL and v4 expected V4 and V15 FAIL `deny-match` (DR-2, DR-1d). Chosen by owner decision 3 (V4-COMPARISON.md).')
NOTES['R6.A1CFG.7'] = (
    TX.NOTES['R6.A1CFG.7'][0],
    'S13 counts every stated A1 control outcome, including the four V4-group rows with the expectations of owner decision 3.',
    TX.NOTES['R6.A1CFG.7'][2],
    'S13 was temporarily narrower than v6.0e\'s, which counted V4, V27 and V15, while those rows were deferred; under owner decision 3 it counts them again.',
    None)
NOTES['R6.CTRL.19'] = (
    TX.NOTES['R6.CTRL.19'][0],
    'Figures become asserted counts; the `T1\'`-bound figure of item11-T1p is candidate evidence only (OBL-23, owner decision 4).',
    TX.NOTES['R6.CTRL.19'][2], TX.NOTES['R6.CTRL.19'][3], TX.NOTES['R6.CTRL.19'][4])
log('D3', 'FRESH-AUTHORIZATION.md: R6.PUR.9, R6.A1CFG.7', 'analysis restated for the decision (a)')
log('D4iii', 'FRESH-AUTHORIZATION.md: R6.CTRL.19', 'analysis restated: the T1\' figure is candidate evidence only')
GENERIC = TX.NOT_AUTH_GENERIC
R1_NOTE = ('The content is in DESIGN-v6.0e.md, which the owner adopted in the owner\'s words (#1169 comment 7130449822, '
           'class (i)); confirming it re-confirms a settled decision (R1).')
R1_TARGETS = ['R6.STAT.4', 'R6.PUR.11', 'R6.REC.18', 'R6.REC.19', 'R6.REC.20', 'R6.REC.21', 'R6.REC.22']
A1CFG7_R6 = ('R6.A1CFG.7 narrows a check: S13 was temporarily narrower than v6.0e\'s while V4, V27 and V15 were '
             'deferred. The review\'s class: (c), protection provided by R6.GATE.9 (`deferred-expectation` is a gate '
             'failure) and OBL-6 (an adoption blocker until the decision). Under owner decision 3 the four rows carry '
             'their expectations and count toward S13, so the narrowing ends with r6\'s adoption.')


def consequence(notauth):
    c = notauth.replace('; ' + GENERIC, '').replace(GENERIC + '; ', '').replace(GENERIC, '').strip()
    return c.rstrip('.') + '.' if c else ''


def fresh_md():
    entries = MARKED_IN + ['R6.DENY.1', 'R6.DENY.2']
    for rid in entries:
        if rid not in NOTES:
            PROBLEMS.append('no analysis for ' + rid)
    old_flagged = [r for r in entries if NOTES.get(r, (None,) * 5)[4]]
    L = ['# r6: requirements needing confirmation or fresh authorization', '',
         'State after the owner\'s decisions of 2026-11-25 (#1169 comment 7166844576, %s; quoted in DESIGN-r6.md '
         'sec. 0.1). Sec. 1 gives the status of the %d requirements presented in the previous revision; sec. 2 the '
         'classes of the flagged requirements (decision 2); sec. 3 the requirements resting on owner decision S1-D3 '
         '(decision 5), which are pending owner confirmation for the adoption decision; sec. 4 the entries of sec. 1 '
         'with their exact wording. Every requirement of r6 takes effect only by r6\'s adoption. A requirement that is '
         'not confirmed stays pending, and r6 cannot be adopted while it is pending; it is never withdrawn by '
         'non-confirmation (owner decision 5, quoted: %s). Withdrawal is a separate, explicit owner choice, with its '
         'verification traced (R6.STAT.5).' % (DEC_AT, len(entries), dq('D5-PEND')), '',
         'Decision 1 and 2, quoted:', '', bq(DEC[1]), '', bq(DEC[2]), '',
         '***', '', '## 1. Status of the requirements presented in the previous revision', '',
         '| Requirement | Decision basis | Class | Review\'s class (decision 1) | Status | Decision 2 class |', '|---|---|---|---|---|---|']
    for rid in entries:
        keys = PEND_IN.get(rid) or []
        cls = ', '.join(sorted(set(CLS.get(k, '-') for k in keys))) if keys else 'no decision cited'
        d2 = ('(%s)' % FLAGGED12[rid][0]) if rid in FLAGGED12 else ('(c), R6' if rid == 'R6.A1CFG.7' else '')
        L.append('| %s | %s | %s | %s | %s | %s |' % (rid, '; '.join(keys) or 'none (F4)', cls,
                                                      REV_CLASS.get(rid, 'not classed (would be: necessary for reliable verification)'),
                                                      status_of(rid), d2))
    L += ['', 'Not a requirement, listed for completeness: the row of sec. 33 "DR-1d, DR-2 | obsolete: dropped deny '
          'candidates (rationale in the appendix); never reused" rests on V5-D1 (class (ii)), whose reversal owner '
          'decision 3 accepts. A retired identifier is never reused (AGENTS.md sec. A.30).', '',
          '***', '', '## 2. Flagged requirements (decision 2; R6)', '',
          'The flag marks a requirement that permits something an earlier design prohibited, or narrows a check. The '
          'owner accepted the review\'s classification of the 12 requirements flagged in the previous revision: (b) '
          'corrections of overly restrictive rules, (c) redundant protections, (d) the four V4-dependent requirements, '
          'resolved through decision 3. The reasons are the reviewer\'s, quoted from REVIEW-r6-round2.md.', '',
          '| Requirement | Class | Reviewer\'s reason (quoted) | Resolution |', '|---|---|---|---|']
    for rid, (c, why) in FLAGGED12.items():
        res = {'b': 'accepted as a correction (decision 2)', 'c': 'accepted as a redundant protection (decision 2)',
               'd': 'resolved by decision 3, resolution (a)'}[c]
        L.append('| %s | (%s) | %s | %s |' % (rid, c, why, res))
    L.append('| R6.A1CFG.7 | (c) | %s | flagged under R6 in this revision; confirmed by decision 1; the narrowing ends under decision 3 |' % A1CFG7_R6.replace('|', '/'))
    L += ['', 'Previously flagged: %s. Added under R6: R6.A1CFG.7.' % ', '.join(old_flagged), '']
    # ---- sec. 3: S1-D3
    L += ['***', '', '## 3. Requirements resting on owner decision S1-D3 (pending owner confirmation for the adoption decision)', '',
          'Owner decision 5, quoted: %s' % dq('D5-S1D3'), '',
          'S1-D3 (class (iii), no GitHub record; DESIGN-v5.5.9.md lines 94-98, CHANGES-v5.2.md line 22) asked to '
          'specify the fixes of the Stage 1 review\'s implementation defects B1-B6. v6.0e sec. 0.2 (inventory item '
          'E-034) maps each to the passages and controls that answer it:', '']
    for b, lab in B_LABEL.items():
        L.append('- %s: %s; inventory items %s; controls %s.' % (b, lab, ', '.join(B_ITEMS[b]),
                                                                ', '.join(B_CONTROLS[b]) or 'none of its own (applies to all controls; the items carry the rule)'))
    L += ['', 'Rules, fixed before the marking and applied mechanically to the requirement index:', '',
          '- Rule A (citation): the requirement\'s Sources cite one of the inventory items above. These are the v6.0e '
          'passages labelled with a Stage 1 B label, their continuation paragraphs and the control rows that E-034 '
          'assigns to B1-B6. Excluded: E-1092 to E-1097 (the splice boundary cases B1-B6 of v6.0e sec. 10.1, a label '
          'collision), E-014, E-034 and E-1364 (lists of labels), and E-1228 (G9, from the v5.2 review\'s V7).',
          '- Rule B (control): the requirement\'s Controls include a control that E-034 assigns to B1-B5 (B6 names RT-T '
          'and RT-D only for specific clauses, which rule A covers through E-1190).',
          '- Rule C (text): a keyword reading of secs. 11, 13 and 16 ("harness", "full clone", "native", "path by '
          'path", "widening", "guard_pins", "adapter companions", "SKIP", "NOT RUN", "--freeze", "pin table", '
          '"admission"); each hit not found by rules A and B was read, and is listed below as marked or as read and '
          'not marked.', '',
          'Found: %d requirements (rule A %d, rule B only %d, rule C %d). Confirmed by owner decision 1: %s. Marked '
          'pending: %d.' % (len(S1D3), sum(1 for v in S1D3.values() if v[0] == 'A'),
                            sum(1 for v in S1D3.values() if v[0] == 'B'), sum(1 for v in S1D3.values() if v[0] == 'C'),
                            ', '.join(S1D3_CONFIRMED), len(S1D3_PENDING)), '',
          'Rule B is broad by construction: a requirement tested by a control that S1-D3 introduced or extended is '
          'listed although its own content may predate S1-D3 (for example Z9g, the real-engine purity PASS, tests '
          'R6.CORE.1 and R6.CORE.2). Confirming such a requirement settles only its authorization; withdrawing it '
          'remains a separate, explicit choice.', '',
          '| Requirement | Sec. | Rule | B labels | Items cited | Controls named | Current authorization status |', '|---|---|---|---|---|---|---|']
    kidx = {q['id']: q for q in REQ_IN}
    for rid, (tier, hits) in S1D3.items():
        labs = ', '.join(sorted(set(h[0] for h in hits)))
        items = ', '.join(x for h in hits for x in h[1]) or '-'
        ctrls = ', '.join(sorted(set(x for h in hits for x in h[2]))) or '-'
        st = ('confirmed by owner decision 1 (%s)' % REV_CLASS[rid].lower()) if rid in CONFIRMED_SET else \
            'not confirmed; r6\'s adoption is not used as its authorization; pending owner confirmation for the adoption decision'
        L.append('| %s | %s | %s | %s | %s | %s | %s |' % (rid, kidx[rid]['section_number'], tier, labs, items, ctrls, st))
    L += ['', 'Rule C, read and not marked:', '']
    for rid, why in KEYWORD_READ_NOT_MARKED.items():
        L.append('- %s: %s.' % (rid, why))
    L += ['', 'Rule C, marked or confirmed:', '']
    for rid, (b, why) in TIER_C.items():
        L.append('- %s (%s): %s.' % (rid, b, why))
    L += ['', 'For each pending requirement the options are those of PARAPHRASED-DECISIONS.md: (a) confirm in the '
          'owner\'s own words, (b) fresh authorization, or (c) withdraw, only by an explicit owner choice. If not '
          'confirmed, the requirement stays pending and r6 cannot be adopted while it is pending. The wording of each '
          'pending requirement, quoted mechanically from DESIGN-r6.md:', '']
    for rid in S1D3_PENDING:
        L += ['### ' + rid, '', bq(block(rid)), '']
    # ---- sec. 4: entries
    L += ['***', '', '## 4. Entries of sec. 1', '']
    for rid in entries:
        purpose, auth, notauth, safe, flag = NOTES[rid]
        keys = PEND_IN.get(rid) or []
        L += ['### ' + rid, '', 'Status: %s.' % status_of(rid)]
        if keys:
            L.append('Decision basis: ' + '; '.join('`%s`, class %s' % (k, TX.CLASS_TEXT[CLS[k]]) for k in keys) + '.')
        else:
            L.append('Decision basis: none cited (unmarked by F4); authorized only by r6\'s adoption.')
        L += ['', 'Current wording (DESIGN-r6.md):', '', bq(block(rid)), '',
              '- Purpose: ' + purpose, '- If confirmed: ' + auth,
              '- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).']
        c = consequence(notauth)
        if c:
            L.append('- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): ' + c)
        L.append('- Safeguards affected: ' + safe)
        if flag:
            L.append('- Flag, earlier designs: ' + flag)
        if rid in FLAGGED12:
            L.append('- Decision 2: class (%s).' % FLAGGED12[rid][0])
        if rid == 'R6.A1CFG.7':
            L.append('- Flag (R6): ' + A1CFG7_R6)
        if rid in R1_TARGETS:
            L.append('- Note (R1): ' + R1_NOTE)
        if rid == 'R6.STAT.8':
            L.append('- Note: confirmed as a requirement; the restatement of the landing-order decision in the owner\'s '
                     'words, which the requirement itself needs before adoption, is still owed.')
        if rid == 'R6.OUT.15':
            L.append('- Deferral: with the `replay` mode of R6.REC.24 and control TR45-opB; accountable Issue #1169; the '
                     'expectation rows TR45-opB and TR45 are unchanged in this revision (DESIGN-r6.md sec. 0.1).')
        L.append('')
    return '\n'.join(L)


FRESH_OUT = fresh_md()
log('D1', 'FRESH-AUTHORIZATION.md', 'status of every entry after decision 1 (confirmed, scope statement, deferred)')
log('D2', 'FRESH-AUTHORIZATION.md', 'sec. 2: the reviewer\'s classes of the 12 flagged requirements, accepted')
log('R6', 'FRESH-AUTHORIZATION.md', 'R6.A1CFG.7 flagged as narrowing, class (c), protected by R6.GATE.9 and OBL-6')
log('R3', 'FRESH-AUTHORIZATION.md', '"If not authorized" replaced by "If not confirmed: ... stays pending"; withdrawal stated as a separate explicit owner choice')
log('R1', 'FRESH-AUTHORIZATION.md', 'the 7130449822 adoption noted on R6.STAT.4, R6.PUR.11 and R6.REC.18 to R6.REC.22')
log('D5-S1D3', 'FRESH-AUTHORIZATION.md', 'sec. 3 (new): the requirements resting on S1-D3, rules, status and wording')

# =====================================================================================================
# V4-COMPARISON.md
# =====================================================================================================
MATCH = []
for name, text in TX.V_TEXTS:
    MATCH.append((name, text) + tuple('match' if re.search(TX.DR_PATTERNS[k], text) else 'no match' for k in ('DR-2', 'DR-1d')))
EXPECT_MATCH = {'V4': ('match', 'no match'), 'V27': ('match', 'no match'), 'V27-glossary': ('match', 'no match'),
                'V15': ('no match', 'match')}
for name, text, m2, m1 in MATCH:
    if name in EXPECT_MATCH and EXPECT_MATCH[name] != (m2, m1):
        PROBLEMS.append('V4-COMPARISON: unexpected rule match for %s' % name)
    if name == 'PUR.8 example' and (m2, m1) != ('no match', 'no match'):
        PROBLEMS.append('V4-COMPARISON: PUR.8 example matches a dropped rule: ' + text)
REJ_LABEL = 'reversal rejected (a plan rule record of this form under a new identifier, sec. 12; DR-1d and DR-2 stay retired, sec. 33)'


def v4_md():
    L = ['# r6: the V4 group, decided (resolution (a))', '',
         'Owner decision 3 of 2026-11-25 (#1169 comment 7166844576, %s), quoted:' % DEC_AT, '', bq(DEC[3]), '',
         'The four rows V4, V27, V27-glossary and V15 of EXPECTATIONS.json carry, as `expect`, the expectation of the '
         'candidate recorded as "reversal adopted"; the candidate "reversal rejected" is not selected; no deny rule is '
         'added. No other row changes.', '',
         '## 1. The candidates and the selection', '',
         'The candidates as recorded in the previous revision (each "not authoritative; decided at r6 adoption", RE-1), '
         'with the label of the rejected candidate restated (a rule of either form would take a new identifier):', '',
         '| Row | Selected: "reversal adopted" (now `expect`) | Not selected: "%s" |' % REJ_LABEL, '|---|---|---|']
    for rid in V4ROWS:
        a, r = SELECTED[rid]
        L.append('| %s | `%s` | `%s` |' % (rid, json.dumps(a['expect'], sort_keys=True), json.dumps(r['expect'], sort_keys=True)))
    L += ['', '## 2. The two rule forms and what they match', '',
          'Patterns as v6.0e sec. 6.4.1 records them (DR-1d and DR-2 are retired identifiers, sec. 33 of DESIGN-r6.md; '
          'a rule of either form would take a new identifier):', '']
    for k in ('DR-2', 'DR-1d'):
        L.append('- form of %s: `%s`' % (k, TX.DR_PATTERNS[k]))
    L += ['', 'Computed by the generator of this document (Python `re`, each text as one sentence; the V27-glossary text '
          'is the start of book/glossary.md line 13 at `H` with "The sixth of the framework\'s structural assumptions '
          'A1–A6" replaced by the V27 text, truncated after the first clause):', '',
          '| Text | Form of DR-2 | Form of DR-1d |', '|---|---|---|']
    for name, text, m2, m1 in MATCH:
        L.append('| %s: "%s" | %s | %s |' % (name, text, m2, m1))
    L += ['', 'A rule of the DR-2 form catches V4, V27 and V27-glossary but not V15; V15 needs a rule of the DR-1d form. '
          'None of the constructed examples of R6.PUR.8 matches either form. v6.0e sec. 6.4.1 ("What removing them '
          'costs (measured)") reports that neither form matches any line of any tree at E, H, W or T1\' and that the '
          'distinct deny-line counts at E, H and W are the same with or without them (95, 86, 86); it also reports a '
          'search of 4677 historical corpus blobs with no match. That search is a historical measurement, provenance '
          'only and not an acceptance reference (R6.EVID.5; R4). Under (b1) or (b2), RT-DR\'s asserted deny counts at '
          '`H` would have re-checked the rule forms on real trees; under the chosen resolution (a) no rule is added, so '
          'that re-check is moot.', '',
          '## 3. The three resolutions', '',
          'Earlier designs: v2\'s demonstration expected V4 FAIL (DESIGN-v2.md line 429); v4 expected V4 FAIL `deny-match` '
          'by DR-2 and V15 FAIL `deny-match` by DR-1d (DESIGN-v4.md lines 1172 and 1185); v5.5.9 and v6.0e expect V4 and '
          'V27 PASS and V15 REVIEW_REQUIRED.', '']
    for name, sel, rules, ids, outcome, earlier, s13 in TX.RESOLUTIONS:
        chosen = name.startswith('(a)')
        L += ['### ' + name + (' (chosen by owner decision 3)' if chosen else ' (not chosen)'), '',
              '| Row | Candidate | Expectation (exact) |', '|---|---|---|']
        for rid in V4ROWS:
            a, r = SELECTED[rid]
            c = a if sel[rid].startswith('reversal adopted') else r
            lab = a['label'] if c is a else REJ_LABEL
            L.append('| %s | %s | `%s` |' % (rid, lab, json.dumps(c['expect'], sort_keys=True)))
        if chosen:
            s13 = s13.replace("R6.PUR.9's outstanding-evidence blocker is discharged by the decision text",
                              "R6.PUR.9's outstanding-evidence blocker is discharged by the text of decision 3")
        else:
            s13 = s13 + '; R6.PUR.9\'s outstanding-evidence blocker would likewise have been discharged by the decision text (N4)'
        L += ['', '- Rules needed: ' + rules, '- Identifiers: ' + ids, '- What it permits and prohibits: ' + outcome,
              '- Relative to earlier designs: ' + earlier, '- S13 and obligations: ' + s13, '']
    L += ['## 4. Trade-offs', '',
          '- (a) needs no new rule and no review of new patterns, and leaves the ordinal-property and reversed-ordinal '
          'forms to review outside the tool (V15 at least REVIEW_REQUIRED). It permits what v2 and v4 prohibited. The '
          'owner\'s caveat, quoted: %s' % dq('D3-CAVEAT'),
          '- (b1) would have restored tool detection of the form v2 and v4 named for V4 at the cost of one new rule, its '
          'review and its reconciliation; V15 would have stayed REVIEW_REQUIRED, which v4 did not permit.',
          '- (b2) would have restored v4\'s detection for both forms at the cost of two new rules; neither form has a '
          'real-tree witness (v6.0e sec. 6.4.1), so both rules would rest on constructed strings only. Decision 3, '
          'quoted: %s' % dq('D3-NORULE'),
          '- In every resolution the retired identifiers DR-1d and DR-2 stay retired.', '',
          '## 5. Decision text and the rule records', '',
          'The decision is the owner\'s text quoted at the top of this document. With it, r6 expects the outcomes of '
          'resolution (a), and no rule of the DR-1d or DR-2 form is required; rule content stays plan content, reviewed '
          'with the deny set at `F` (R6.DENY.1, OBL-3; N5). The draft decision texts of the previous revision are kept '
          'in its history (commit 400e4b4fe5f3474b96ee4faa3c437e76e09db782).', '']
    return '\n'.join(L)


V4_OUT = v4_md()
log('D3', 'V4-COMPARISON.md', 'regenerated as decided: decision 3 quoted, selection per row, labels of the rejected candidate restated')
log('R4', 'V4-COMPARISON.md', 'the 4677-blob search marked provenance (R6.EVID.5); RT-DR re-check under (b) stated as moot under (a)')
log('N4', 'V4-COMPARISON.md', 'the blocker\'s discharge stated for every resolution')
log('N5', 'V4-COMPARISON.md', 'wording: r6 expects the outcomes of (a), and no such rule is required')

# =====================================================================================================
# REVIEW-r6-round2.md
# =====================================================================================================
REVIEW_OUT = '\n'.join([
    '# Independent review of A1 design r6, second correction round', '',
    '- Reviewer: a Claude reviewer agent started by the coordinating session with a fresh context; it wrote none of '
    'the reviewed work and made no GitHub or repository writes (as #1169 comment 7166666428 records).',
    '- Commit reviewed: 400e4b4fe5f3474b96ee4faa3c437e76e09db782 (this directory, '
    'verification/audits/foundations/a1exit-design-r6-20261125/).',
    '- Date: 2026-11-25 (the record\'s `created_at`, %s).' % REV_AT,
    '- Record: #1169 comment 7166666428, which quotes the reviewer text verbatim. SHA-256 of the reviewer text below: '
    '%s, equal to the digest stated in that comment.' % sha(REVIEW),
    '- Verdict: ACCEPT-WITH-NITS. The owner\'s decisions on it: #1169 comment 7166844576 (DESIGN-r6.md sec. 0.1). '
    'Acceptance of this record and of r6 is the owner\'s decision; landing this file approves no merge (AGENTS.md '
    'sec. A.50 item 1).', '',
    'The reviewer text follows verbatim, between the two marker lines.', '',
    '---- reviewer text begins ----', '', REVIEW.rstrip('\n'), '', '---- reviewer text ends ----', ''])
_va = REVIEW_OUT.index('---- reviewer text begins ----\n\n') + len('---- reviewer text begins ----\n\n')
_vb = REVIEW_OUT.index('\n\n---- reviewer text ends ----')
REVIEW_VERBATIM_OK = (REVIEW_OUT[_va:_vb] + '\n' == REVIEW and REVIEW_OUT[_va:_vb] == REV_INNER and
                      REV_SHA_STATED is not None and REV_SHA_STATED.group(1) == sha(REVIEW))
log('D4i', 'REVIEW-r6-round2.md', 'review record: header (reviewer, commit, date, comment) and the reviewer text verbatim')

# =====================================================================================================
# self-checks: round 2's run_checks, parameterized by the pending mark
# =====================================================================================================


def run_checks(text, rows, req_out, exp_out, mark):
    C = collections.OrderedDict()
    reqs = parse_reqs(text)
    ridx = collections.OrderedDict((r['id'], r) for r in rows)
    row_ids = set(ridx)
    ctrl_ids = set(i for i in row_ids if not i.startswith('MUT:'))
    req_ids = set(reqs)
    a17 = text.index('**Table 17.1. Control catalogue**')
    b17 = text.index('**Table 17.2. Record-directory mutants**')
    table_ids = []
    for line in text[a17:b17].split('\n'):
        if line.startswith('| ') and not line.startswith('| Id ') and not line.startswith('|---'):
            table_ids.append(line[2:-2].split(' | ')[0])
    C['completeness: MAPPING rows not cited in DESIGN-r6.md'] = [
        m['item'] for m in MAPPING['rows'] if not re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(m['item']), text)]
    C['consistency: named controls without a row'] = sorted(set(c for q in reqs.values() for c in q['controls'] if c not in row_ids))
    C['consistency: rows naming an unknown requirement'] = sorted(r['id'] for r in rows if any(x not in req_ids for x in r['requirements']))
    C['consistency: rows named by no requirement'] = sorted(r['id'] for r in rows if not r['requirements'])
    two_way = []
    for r in rows:
        for q in r['requirements']:
            if q in reqs and r['id'] not in reqs[q]['controls'] and not r.get('composed_of'):
                two_way.append('%s<-%s' % (r['id'], q))
    for q in reqs.values():
        for c in q['controls']:
            if c in ridx and q['id'] not in ridx[c]['requirements']:
                two_way.append('%s->%s' % (q['id'], c))
    C['consistency: one-way links'] = two_way
    C['consistency: rows with expect null'] = sorted(r['id'] for r in rows if r.get('expect') is None)
    ret_live = set()
    for e in exp_out['retired']:
        if e['disposition'].startswith(('merged', 'succeeded')):
            continue
        for t in re.split(r',\s*', e['old_id']):
            ret_live.add(t.split(' ')[0])
    named_all = set(c for q in reqs.values() for c in q['controls'])
    C['consistency: retired ids live (row or named control)'] = sorted(ret_live & (row_ids | named_all))
    C['consistency: Table 17.1 ids without a row, rows missing from Table 17.1'] = sorted(set(table_ids) ^ ctrl_ids)
    C['consistency: cited requirement ids that do not exist'] = sorted(set(re.findall(r'\bR6\.[A-Z0-9]+\.\d+\b', text)) - req_ids)
    C['consistency: cited OBL ids that do not exist'] = sorted(set(re.findall(r'\bOBL-\d+\b', text)) - req_ids)
    C['consistency: GATE-1 to GATE-30 rows present'] = [g for g in ['GATE-%d' % i for i in range(1, 31)] if g not in row_ids]
    C['consistency: rows with candidate expectations not DEFERRED'] = sorted(
        r['id'] for r in rows if 'candidate_expectations' in r and r['expect'] != {'outcome': 'DEFERRED'})
    C['consistency: superseded names remaining (ISOLATION_REFUSED, RD2-RD5, ...)'] = (
        [s for s in ('ISOLATION_REFUSED', 'REC-ORPHAN', 'REPRO-CLEAN') if s in text] + re.findall(r'\bRD[2-5]\b', text + dumps(exp_out)))
    C['consistency: paired_with naming an id that is not a row'] = sorted(r['id'] for r in rows for p in r.get('paired_with', []) if p not in row_ids)
    C['coverage: non-testable requirements without verification'] = [q['id'] for q in req_out if q['kind'] != 'testable' and not q['verification']]
    C['consistency: requirement ids in the text equal the requirement index'] = sorted(set(reqs) ^ set(q['id'] for q in req_out))
    marked_txt = sorted(r for r, q in reqs.items() if mark in q['text'])
    marked_idx = sorted(q['id'] for q in req_out if q['pending_owner_confirmation'])
    C['consistency: marked requirements in the text equal those keyed in the index'] = sorted(set(marked_txt) ^ set(marked_idx))
    C['OC-1: OBL-16 carries no OPEN marker and no "F on main" condition'] = (
        reqs['OBL-16']['open'] + (['F on main'] if re.search(r'F` on `main` with|plan commit `F` on `main`', reqs['OBL-16']['text']) else []) +
        (['TR5 release needs F on main'] if 'F on main whose' in dumps(ridx['TR5']) else []))
    C['OC-2: OBL-26 carries no circularity marker and is not gated on adoption'] = (
        reqs['OBL-26']['open'] + (['adoption gate'] if "Gates: r6's adoption" in reqs['OBL-26']['text'] else []))
    C['OC-4: LC-7 expects REVIEW_REQUIRED in every case and keeps its OPEN flag'] = (
        [c['case'] for c in ridx['LC-7']['expect']['cases'] if c['outcome'] != 'REVIEW_REQUIRED'] +
        ([] if any(f.startswith('OPEN: derived-artifact landing blob') for f in ridx['LC-7']['flags']) else ['flag missing']) +
        ([] if 'derived-artifact landing blob' in reqs['R6.TREE.12']['open'] else ['TREE.12 OPEN missing']))
    C['OC-3: rows on X_rep carry both invariants; item11-T1p does not'] = (
        [c for c in ('RT-L2', 'RT-O9-L2', 'RT-T', 'RT-T0', 'RT-D', 'RT-I7', 'RT-I7A', 'RT-DR3W', 'N10', 'N11', 'REP-BUILD')
         if 'representative_candidate' not in dumps(ridx[c])] +
        (['item11-T1p'] if 'representative_candidate' in dumps(ridx['item11-T1p']) else []))
    VALUES = collections.OrderedDict()
    VALUES['requirements'] = len(req_out)
    VALUES['expectation rows'] = len(rows)
    VALUES['rows flagged VD-RESTORE'] = sum(1 for r in rows if any(f.startswith('VD-RESTORE') for f in r.get('flags', [])))
    VALUES['requirements marked pending owner confirmation'] = len(marked_idx)
    VALUES['testable requirements without a control'] = len([q for q in req_out if q['kind'] == 'testable' and not q['controls']])
    VALUES['MAPPING rows placed'] = len(MAPPING['rows']) - len(C['completeness: MAPPING rows not cited in DESIGN-r6.md'])
    VALUES['OPEN markers in the requirement index'] = sum(len(q['open']) for q in req_out)
    VALUES['rows with expect DEFERRED'] = sum(1 for r in rows if r.get('expect') == {'outcome': 'DEFERRED'})
    return C, VALUES


CONTENT_REPORT2 = REPORT2_TXT
CHK_BEFORE, VAL_BEFORE = run_checks(T_IN, EXP['rows'], REQ_IN, EXP, PEND_TXT)
CHK_AFTER, VAL_AFTER = run_checks(T, EXP_OUT['rows'], REQ_OUT, EXP_OUT, PEND3)
OUT_IDX = collections.OrderedDict((r['id'], r) for r in EXP_OUT['rows'])
OWN = collections.OrderedDict()
OWN['replay: the index rule reproduces out-final3/REQUIREMENTS.json from out-final3/DESIGN-r6.md'] = [] if REPLAY_OK else ['mismatch']
OWN['D1: the review\'s classes (22, 19, 2, 1) parsed and equal to the 44 previously marked requirements'] = (
    ([] if (len(CL_V), len(CL_R), len(CL_S), len(CL_D)) == (22, 19, 2, 1) else ['counts']) +
    sorted(set(MARKED_IN) ^ set(CL_V + CL_R + CL_S + CL_D)))
OWN['D1: each of the 44 carries exactly its decision-1 text and no round-2 mark'] = [
    r for r in MARKED_IN if REQS[r]['text'].count(NEWMARK[r]) != 1 or PEND_TXT in REQS[r]['text']]
OWN['D1: no requirement anywhere carries the round-2 mark'] = [r for r, q in REQS.items() if PEND_TXT in q['text']]
OWN['D2: 12 flagged rows parsed, classes (b) x6, (c) x2, (d) x4'] = (
    [] if sorted(c for c, _ in FLAGGED12.values()) == sorted(['b'] * 6 + ['c'] * 2 + ['d'] * 4) else ['classes'])
OWN['D3: the four rows\' expect equals the out-final3 "reversal adopted" candidate, byte for byte; no candidates left'] = [
    i for i in V4ROWS if dumps(OUT_IDX[i]['expect']) != dumps([c for c in RIDX_IN[i]['candidate_expectations'] if c['label'].startswith('reversal adopted')][0]['expect'])
    or 'candidate_expectations' in OUT_IDX[i]]
OWN['D3: every other expectation row byte-identical to out-final3 (554 rows)'] = [
    a['id'] for a, b in zip(EXP['rows'], EXP_OUT['rows']) if a['id'] not in V4ROWS and dumps(a) != dumps(b)] + (
    [] if [r['id'] for r in EXP['rows']] == [r['id'] for r in EXP_OUT['rows']] else ['order or count'])
OWN['D3: the four rows differ from out-final3 only in expect, candidate_expectations and two flags'] = [
    i for i in V4ROWS if [k for k in RIDX_IN[i] if k not in ('expect', 'candidate_expectations', 'flags')] !=
    [k for k in OUT_IDX[i] if k not in ('expect', 'flags')] or any(RIDX_IN[i][k] != OUT_IDX[i][k] for k in OUT_IDX[i] if k not in ('expect', 'flags'))
    or len(RIDX_IN[i]['flags']) != len(OUT_IDX[i]['flags'])
    or sum(1 for x, y in zip(RIDX_IN[i]['flags'], OUT_IDX[i]['flags']) if x != y) != 2]
OWN['preservation: retired list unchanged'] = [] if dumps(EXP_OUT['retired']) == dumps(EXP['retired']) else ['changed']
OWN['preservation: requirement ids: only R6.TREE.19 added, none removed'] = sorted(set(parse_reqs(T_IN)) ^ set(REQS) ^ {'R6.TREE.19'})
OWN['preservation: sources and controls of every earlier requirement unchanged'] = [
    q['id'] for q in REQ_OUT if q['id'] in KIND and q['id'] != 'R6.TREE.19' and (q['sources'], q['controls']) != (KIND[q['id']]['sources'], KIND[q['id']]['controls'])]
OWN['preservation: sections 33 and 34 unchanged'] = (
    [] if T[T.index('## 33. Retired'):T.index('## Appendix H.')] == T_IN[T_IN.index('## 33. Retired'):T_IN.index('## Appendix H.')] else ['changed'])
H_OUT = T[T.index('## Appendix H.'):]
H_IN = T_IN[T_IN.index('## Appendix H.'):]
OWN['preservation: Appendix H changed only in HIST-4'] = (
    [] if re.sub(r'- HIST-4\..*?(?=\n- HIST-5\.)', '', H_OUT, flags=re.S) == re.sub(r'- HIST-4\..*?(?=\n- HIST-5\.)', '', H_IN, flags=re.S) else ['changed'])
OWN['preservation: MIGRATION.json and CORRECTION-REPORT.md unchanged'] = ([] if MIG_OUT_TXT == MIG_TXT else ['MIGRATION.json']) + (
    [] if CONTENT_REPORT2 == REPORT2_TXT else ['CORRECTION-REPORT.md'])
ws = lambda s: re.sub(r'\s+', ' ', s).strip()
EDITED = set(t for _, t, _ in LOG if re.match(r'(R6\.[A-Z0-9]+\.\d+|OBL-\d+)$', t))
OWN['preservation: requirement blocks without a logged edit unchanged (whitespace-normalized)'] = [
    rid for rid in parse_reqs(T_IN) if rid not in EDITED and ws(block(rid, T_IN)) != ws(block(rid, T))]
OWN['D4 (iii): OBL-23 carries no OPEN marker; OPEN markers are those of R6.STAT.10 and R6.TREE.12'] = sorted(
    set(r for r, q in REQS.items() if q['open']) ^ {'R6.STAT.10', 'R6.TREE.12'})
OWN['D4 (i): REVIEW-r6-round2.md holds the reviewer text verbatim; its sha256 equals the digest in comment 7166666428'] = [] if REVIEW_VERBATIM_OK else ['mismatch']
OWN['D5: decisions 1 to 4 quoted byte-exact in sec. 0.1'] = [] if bq(DEC_1_4) in T else ['missing']
OWN['D5: S1-D3 marks equal the identified requirements less those decision 1 confirmed'] = sorted(
    set(r for r, q in REQS.items() if PEND3 in q['text']) ^ set(S1D3_PENDING))
OWN['R3: no "If not authorized" line; every entry has "If not confirmed: ... stays pending"'] = (
    (['If not authorized'] if 'If not authorized' in FRESH_OUT else []) +
    [r for r in MARKED_IN + ['R6.DENY.1', 'R6.DENY.2'] if '### %s\n' % r not in FRESH_OUT] +
    ([] if FRESH_OUT.count('- If not confirmed: the requirement stays pending') == len(MARKED_IN) + 2 else ['count']))
OWN['quotes: every quotation of a comment occurs in its body'] = [p for p in PROBLEMS if p.startswith(('quote ', 'decision quote'))]
OWN['V4-COMPARISON: rule-form matches as expected'] = [p for p in PROBLEMS if p.startswith('V4-COMPARISON')]
for k, v in list(CHK_AFTER.items()) + list(OWN.items()):
    if v:
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================================
# CORRECTION-REPORT-round3.md
# =====================================================================================================


def table(head, rows_):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    for r in rows_:
        out.append('| ' + ' | '.join(str(x).replace('|', '/') for x in r) + ' |')
    return out


CONTENT = collections.OrderedDict()
CONTENT['DESIGN-r6.md'] = T
CONTENT['EXPECTATIONS.json'] = dumps(EXP_OUT)
CONTENT['REQUIREMENTS.json'] = dumps(REQ_OUT)
CONTENT['MIGRATION.json'] = MIG_OUT_TXT
CONTENT['PARAPHRASED-DECISIONS.md'] = PARA_OUT
CONTENT['AUTHORIZATIONS.md'] = AUTH_OUT
CONTENT['FRESH-AUTHORIZATION.md'] = FRESH_OUT
CONTENT['V4-COMPARISON.md'] = V4_OUT
CONTENT['REVIEW-r6-round2.md'] = REVIEW_OUT
CONTENT['CORRECTION-REPORT.md'] = CONTENT_REPORT2

ITEMS = collections.OrderedDict([
    ('D1', 'Decision 1: 22 + 19 requirements confirmed; R6.STAT.4 and R6.EVID.5 scope statements without a check of their own.'),
    ('D1-scope', 'Decision 1: the two scope statements.'),
    ('D1-defer', 'Decision 1: R6.OUT.15 deferred with the `replay` mode of R6.REC.24 and TR45-opB; accountable Issue #1169; text kept.'),
    ('D2', 'Decision 2: the reviewer\'s classes of the 12 flagged requirements accepted.'),
    ('D3', 'Decision 3: resolution (a) for V4, V27, V27-glossary and V15; candidate labels restated; the owner\'s caveat quoted; R6.PUR.9\'s blocker discharged by the decision text.'),
    ('D4i', 'Decision 4 (i): the review record REVIEW-r6-round2.md; adoption needs the landing pull request\'s separate merge approval.'),
    ('D4ii', 'Decision 4 (ii): the LC-7 regeneration and byte-comparison procedure, R6.TREE.19, for the delta review.'),
    ('D4iii', 'Decision 4 (iii): the T1\' figure of item11-T1p is candidate evidence only.'),
    ('D5', 'Decision 5: decisions 1-4 quoted into r6 (sec. 0.1); the bounded scope of this revision.'),
    ('D5-S1D3', 'Decision 5: the requirements resting on S1-D3 identified, listed and marked pending for the adoption decision.'),
    ('R1', 'R1: the 7130449822 adoption of v6.0e noted on R6.REC.18 to R6.REC.22 (and R6.STAT.4, R6.PUR.11) and on the line 31/54 keys.'),
    ('R3', 'R3: non-confirmation leaves a requirement pending; withdrawal is a separate explicit owner choice.'),
    ('R4', 'R4: the 4677-blob figure marked provenance; RT-DR\'s re-check under (b) stated, moot under (a).'),
    ('R6', 'R6: R6.A1CFG.7 flagged as narrowing, class (c), protected by R6.GATE.9 and OBL-6.'),
    ('N1', 'N1: what each class (i) record authorizes; none adopts r6.'),
    ('N2', 'N2: V5-D1\'s consequence attributed to v6.0e\'s measurement; 7099655517\'s coverage-limitation decision named as R6.PUR.8\'s direct basis.'),
    ('N4', 'N4: the blocker\'s discharge stated for every resolution.'),
    ('N5', 'N5: "r6 expects ..., and no such rule is required".'),
    ('N6', 'N6: HIST-4 disambiguated (the E-008 decisions of 2026-11-24; DI-2\'s class (ii) record).'),
    ('meta', 'Mechanical consequences: record id, index fields, blank lines.'),
])
SAFE = {
    'D1': 'neutral: the confirmations are the owner\'s; no content, check or expectation changes',
    'D1-scope': 'neutral: decision 1; no check removed (GATE-16 stays named by R6.EVID.5 and its other requirements)',
    'D1-defer': 'owner-decided deferral; the text, the rows TR45-opB and TR45 and every other check are kept',
    'D2': 'neutral: classification only',
    'D3': 'the owner\'s decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review',
    'D4i': 'neutral or stricter: separate merge approval stated',
    'D4ii': 'stricter: LC-7 stays REVIEW_REQUIRED until the delta review accepts the procedure',
    'D4iii': 'stricter: the T1\' figure supports no acceptance',
    'D5': 'neutral: quotation and scope',
    'D5-S1D3': 'stricter: 50 requirements marked pending for the adoption decision',
    'R1': 'neutral: notes', 'R3': 'stricter: no requirement is withdrawn by non-confirmation', 'R4': 'neutral',
    'R6': 'neutral: flag', 'N1': 'neutral', 'N2': 'neutral', 'N4': 'neutral', 'N5': 'neutral', 'N6': 'neutral',
    'meta': 'neutral'}
OPEN_ITEMS = [
    'Pending for the adoption decision: the %d requirements resting on S1-D3 that decision 1 did not confirm (FRESH-AUTHORIZATION.md, sec. 3); R6.STAT.8\'s own condition, the restatement of the landing-order decision in the owner\'s words.' % len(S1D3_PENDING),
    'R6.DENY.1 and R6.DENY.2 are not marked and were not among the requirements decision 1 confirmed; they take effect only by r6\'s adoption (the review would class both as necessary for reliable verification).',
    'R6.STAT.10, off-main support of adoption: open until the r6 documents, REVIEW-r6-round2.md and the delta review reach `main` by an owner-approved merge.',
    'R6.TREE.12 / LC-7: the procedure R6.TREE.19 awaits the delta review; LC-7\'s expectation is unchanged (REVIEW_REQUIRED) and its OPEN flag is kept; once the procedure is accepted, LC-7\'s cases need an owner-approved expectation change.',
    'The deferred R6.OUT.15: the expectation rows TR45-opB and TR45 (composite of TR45-opB and TR45-opC) are unchanged, as this revision changes no expectation except decision 3\'s selection; carried as they are, a tool revision without the replay mode would leave TR45-opB without a record (`missing-id`). Their treatment in the expectation file is for the delta review and a later owner-approved expectation change. R6.REC.24 still lists `"replay"` among the modes, marked deferred.',
    'R6.EVID.5 still names GATE-16 under Controls (its link in GATE-16\'s row is unchanged); GATE-16 is the gate\'s reference-difference control, not a check of R6.EVID.5\'s list.',
    'The expectation row item11-T1p is byte-identical; its flag "inputs off main: acceptance reference only for runs with those pinned inputs (RD-23)" predates decision 4 (iii), which OBL-23 now states; the flag is for the delta review.',
]
CONTRADICTIONS = [
    'CORRECTION-REPORT.md (round 2) says the previous report "is a record of its round and is not edited", yet it replaced the round-1 report in place; the round-1 text is in history at ad035ff5. It cites its generator and inputs as `build/correct2.py`, `out-final2/` and `gh7/sel.json`; in the directory these are `generator-round2/correct2.py`, the round-1 outputs at ad035ff5 and `generator-round2/comments-1169.json`, as `generator-round2/PROVENANCE.json` maps them (N3). This round leaves CORRECTION-REPORT.md byte-identical as the round-2 record and writes its own report to this file.',
    'Decision 1 confirms R6.STAT.8 as a requirement; the requirement itself asks that the landing-order decision be restated in the owner\'s words before adoption, which decision 1 does not do. Recorded as owed (sec. 0.1, FRESH-AUTHORIZATION.md).',
    'The review counts 44 pending requirements and 12 flagged; R6.A1CFG.7, flagged under R6, is one of the 22 decision 1 confirms, so its flag changes no status.',
]


def report():
    L = ['# r6 correction report, third round: final text-only revision (owner decisions 1-5 of 2026-11-25)', '',
         'Deterministic revision by `build/correct3.py`, which reads the round-2 outputs (read only), the review text '
         'recorded at #1169 comment 7166666428 and the owner\'s decisions recorded at #1169 comment 7166844576 (read '
         'with GET requests), and applies the logged edits below. Each edit carries the owner decision (D1-D5) or the '
         'review finding (R1-R6, N1-N6) it applies, or `meta`. Authorization, quoted: %s. Decision 5 authorizes this '
         'revision and one bounded delta review, not adoption, implementation, freezing, trial execution or merging. '
         'No governance rule is amended, no exception is created, no expectation changes except decision 3\'s '
         'selection, and r6 stays a draft. No git or GitHub write was made.' % quote('DQ-D5-SCOPE'), '',
         'Items applied:', '']
    for k, v in ITEMS.items():
        L.append('- %s: %s' % (k, v))
    L += ['- R2: addressed by decision 5 and the S1-D3 identification (FRESH-AUTHORIZATION.md, sec. 3).',
          '- R5: R6.STAT.10 and sec. 0.1 state that one bounded delta review covers this revision before adoption.',
          '- N3: see sec. 6.', '', '***', '', '## 1. Inputs and outputs (sha256)', '']
    L += table(['Input (read only)', 'In the directory or record', 'sha256'], [(p, m, s) for p, s, m in INPUT_SHA])
    L += ['']
    L += table(['Output', 'sha256'], [(n, sha(c)) for n, c in CONTENT.items()] +
               [('CORRECTION-REPORT-round3.md', 'this file (its digest is reported by the generator run)')])
    L += ['', 'CORRECTION-REPORT.md and MIGRATION.json are copied byte-identical from the round-2 outputs.', '',
          '***', '', '## 2. Edits applied', '']
    L += table(['#', 'Item', 'Target', 'Edit', 'Safeguard'],
               [(i + 1, a, b, d, SAFE[a]) for i, (a, b, d) in enumerate(LOG)])
    L += ['', '***', '', '## 3. Safeguards', '',
          'No safeguard is weakened by an edit of this round on its own authority. Decision 3 is the owner\'s choice of '
          'resolution (a), which permits what v2 and v4 prohibited (V4-COMPARISON.md), with V15 kept under human '
          'review; decision 1 defers R6.OUT.15 and its replay mode, keeping its text and rows. The "Safeguard" column '
          'above states the reason for each edit; it is asserted text, and the checks of sec. 4 measure what they '
          'name.', '',
          '***', '', '## 4. Self-checks (before: out-final3; after: out-final4)', '']
    rows_ = []
    for k in CHK_AFTER:
        b, a = CHK_BEFORE[k], CHK_AFTER[k]
        rows_.append((k, len(b) if not b else '%d (%s)' % (len(b), ', '.join(map(str, b[:6]))),
                      len(a) if not a else '%d (%s)' % (len(a), ', '.join(map(str, a[:6])))))
    L += table(['Check (round 2\'s run_checks; the mark is round 2\'s before and the S1-D3 mark after)', 'Before', 'After'], rows_)
    L += ['']
    WHY = {'requirements': 'R6.TREE.19 added (decision 4 (ii))',
           'requirements marked pending owner confirmation': '44 decided by decision 1 (41 confirmed, 2 scope, 1 deferred); %d S1-D3 requirements marked (decision 5)' % len(S1D3_PENDING),
           'OPEN markers in the requirement index': "OBL-23's marker removed: decision 4 (iii) narrows the claim",
           'rows with expect DEFERRED': 'decision 3 selects the four expectations',
           'testable requirements without a control': ''}
    L += table(['Value', 'Before', 'After', 'Why it changed'],
               [(k, VAL_BEFORE[k], VAL_AFTER[k], WHY.get(k, '') if VAL_BEFORE[k] != VAL_AFTER[k] else '') for k in VAL_AFTER])
    L += ['', 'Checks of this round:', '']
    for k, v in OWN.items():
        L.append('- %s: %s' % (k, len(v) if not v else '%d (%s)' % (len(v), ', '.join(map(str, v[:10])))))
    L += ['- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return, no invisible '
          'formatting character, no non-ASCII space, and no non-ASCII character outside those of the inputs and the '
          'quoted texts, in any output: checked',
          '- reproducibility: the generator re-ran itself in a separate process (`python3 -I -B`) and compared the '
          'sha256 of every output before writing; identical',
          '- generator problems: %d' % len(PROBLEMS), '', '***', '', '## 5. Remaining open items', '']
    L += ['- ' + o for o in OPEN_ITEMS]
    L += ['', '***', '', '## 6. Contradictions and departures found', '']
    L += ['- ' + c for c in CONTRADICTIONS]
    L += ['']
    return '\n'.join(L)


CONTENT['CORRECTION-REPORT-round3.md'] = report()

# =====================================================================================================
# hygiene, reproducibility, write
# =====================================================================================================


def nonascii(c):
    return set(ch for ch in c if ord(ch) > 127)


ALLOWED = nonascii(T_IN + EXP_TXT + REQ_TXT + MIG_TXT + PARA_TXT + AUTH_TXT + FRESH_TXT + V4_TXT + REPORT2_TXT + REVIEW + DEC_ALL) | set().union(
    *[nonascii(q) for _, q in QUOTES.values()])
BAD_SP = re.compile('[   -​  　﻿]')
LONG_URL = re.compile(r'https?://github\.com/\S{60,}')
SCR = 'scratch' + 'pad'  # built, as generator-round5 builds it, so that this file does not carry the word
for n, c in CONTENT.items():
    for what, bad in (('@', '@' in c), ('/tmp', '/tmp' in c), (SCR, SCR in c),
                      ('session id', 'session_0' in c), ('github.com', 'github.com' in c), ('CR', '\r' in c),
                      ('format character', any(unicodedata.category(ch) == 'Cf' for ch in c)),
                      ('non-ASCII space', bool(BAD_SP.search(c))), ('long github URL', bool(LONG_URL.search(c))),
                      ('non-ASCII character outside inputs and quotes', bool(nonascii(c) - ALLOWED))):
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
    with open(os.path.join(OUT, n), 'wb') as f:
        f.write(c.encode('utf-8'))
for n in CONTENT:
    print(n, HASHES[n])
for k in VAL_AFTER:
    print('VALUE', k, VAL_BEFORE[k], '->', VAL_AFTER[k])

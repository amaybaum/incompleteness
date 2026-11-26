#!/usr/bin/env python3
"""Second correction round of design r6 (owner decision of 2026-11-25, #1169 comment 7164340996).

Reads out-final2/ (read only), MAPPING.json and the #1169 comments fetched read-only (gh7/sel.json), and
writes out-final3/.  Every change is an explicit, logged edit tagged with the finding it applies (F1 to F8,
F7-<requirement id>, OCFIX) or `meta` for a mechanical consequence.  Two runs give byte-identical files (the
generator re-runs itself and compares hashes before writing).  The self-checks of out-final2/build/correct.py
are copied below unchanged in substance (parameterized by input), run on out-final2 ("before") and on the
corrected outputs ("after").
"""
import collections
import copy
import hashlib
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
R6 = os.path.dirname(OUT)
IN = os.path.join(R6, 'out-final2')
sys.path.insert(0, HERE)
import text2 as TX  # noqa: E402


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


INPUTS = ['out-final2/DESIGN-r6.md', 'out-final2/EXPECTATIONS.json', 'out-final2/REQUIREMENTS.json',
          'out-final2/MIGRATION.json', 'out-final2/PARAPHRASED-DECISIONS.md', 'out-final2/CORRECTION-REPORT.md',
          'out-final2/build/correct.py', 'out-final2/build/report_text.py', 'PENDING-33.md', 'MAPPING.json',
          'gh7/sel.json']
INPUT_SHA = [(p, sha(open(os.path.join(R6, p), 'rb').read())) for p in INPUTS]

T_IN = rd(os.path.join(IN, 'DESIGN-r6.md'))
T = T_IN
EXP_TXT = rd(os.path.join(IN, 'EXPECTATIONS.json'))
EXP = rj(EXP_TXT)
REQ_TXT = rd(os.path.join(IN, 'REQUIREMENTS.json'))
REQ_IN = rj(REQ_TXT)
MIG_TXT = rd(os.path.join(IN, 'MIGRATION.json'))
PARA_TXT = rd(os.path.join(IN, 'PARAPHRASED-DECISIONS.md'))
MAPPING = rj(rd(os.path.join(R6, 'MAPPING.json')))
COMM = rj(rd(os.path.join(R6, 'gh7', 'sel.json')))

LOG = []
PROBLEMS = []
SAFEGUARD = collections.OrderedDict()  # tag -> statement


def log(item, target, desc):
    LOG.append((item, target, desc))


# ------------------------------------------------------------------ text helpers (as correct.py)
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


def add_mark(item, rid):
    """Insert the pending mark before the block's Sources (as final.py places it)."""
    global T
    a, b = block_span(rid)
    blk = T[a:b]
    if PEND_TXT in blk:
        PROBLEMS.append('add_mark %s: already marked' % rid)
        return
    k = blk.rfind('\nSources:')
    if k >= 0:
        new = blk[:k] + '\n' + PEND_TXT + blk[k:]
    else:
        k = blk.rfind(' Sources:')
        if k < 0:
            PROBLEMS.append('add_mark %s: no Sources' % rid)
            return
        new = blk[:k] + ' ' + PEND_TXT + blk[k:]
    T = T[:a] + new + T[b:]
    log(item, rid, 'marked "%s"' % PEND_TXT)


def remove_mark(item, rid):
    global T
    a, b = block_span(rid)
    blk = T[a:b]
    old = '\n' + PEND_TXT + '\n'
    if blk.count(old) != 1:
        PROBLEMS.append('remove_mark %s' % rid)
        return
    T = T[:a] + blk.replace(old, '\n') + T[b:]
    log(item, rid, 'pending mark removed')


# =====================================================================================================
# F1: classification of cited decisions where the design attributes authority
# =====================================================================================================
in_block_edit('F1', 'R6.STAT.8',
    "**R6.STAT.8** Landing order. Owner decision #1169 comment 7093128173 (`amaybaum`,\n2026-11-23T06:13:50Z) approved in principle",
    "**R6.STAT.8** Landing order. The owner decision recorded by the coordinating session in #1169 comment\n"
    "7093128173 (posted from the `amaybaum` account, 2026-11-23T06:13:50Z; a session-written record that\n"
    "quotes no owner words) approved in principle", 'attribution classified (class (ii))')
in_block_edit('F1', 'R6.STAT.8',
    "owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26).",
    "owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26);\n"
    "since the comment holds no owner words, the owner restates it.", 'RE-26 alternative fixed by the record\'s class')
SAFEGUARD['F1'] = ('stricter or neutral: the attributions now state the class of each record; R6.STAT.8 can be '
                   'confirmed only by the owner restating the decision, the comment holding no owner words; no check, '
                   'expectation or obligation changes.')
in_block_edit('F1', 'R6.PUR.9',
    "in paraphrase (ME-6); its text is to be recorded by the owner.",
    "in paraphrase, in the session-written #1169 comment 7099655517 (ME-6); its text is to be recorded by\nthe owner.", 'attribution classified (class (ii))')
in_block_edit('F1', 'R6.DENY.6',
    "That decision (V5-D1) is recorded only in\nparaphrase.",
    "That decision (V5-D1) is recorded only in\nparaphrase, in the session-written #1169 comment 7099655517.", 'attribution classified (class (ii))')
in_block_edit('F1', 'R6.CTRL.15',
    "The reversal rests on an\nowner decision recorded only in paraphrase.",
    "The reversal rests on an\nowner decision recorded only in paraphrase (V5-D1, in the session-written #1169 comment 7099655517).",
    'attribution classified (class (ii))')
edit('F1', 'Appendix H HIST-4',
     "- HIST-4. Quotes of owner decisions without a GitHub record (removal of automated authorization\n"
     "  verification; preservation of technical guarantees; the route authority of #1169 comment 7093128173,\n"
     "  paraphrased; D1-D4, V5-D1, V5-D2, S1-D1 to S1-D3 and the decisions of 2026-11-24). r6 relies on no\n"
     "  unrecorded decision; its authority is its own adoption.",
     "- HIST-4. Quotes and records of owner decisions: without a GitHub record, the removal of automated\n"
     "  authorization verification, the preservation of technical guarantees, S1-D1 to S1-D3 and the\n"
     "  decisions of 2026-11-24; recorded on GitHub only by the coordinating session, without the owner's\n"
     "  words, the route authority of #1169 comment 7093128173 and v3 D1-D4, V5-D1 and V5-D2 (#1169 comment\n"
     "  7099655517). r6 relies on no unrecorded decision; its authority is its own adoption.")

# =====================================================================================================
# OCFIX: OC-1 to OC-5 are quoted in the owner's words in #1169 comment 7163402499
# =====================================================================================================
edit('OCFIX', 'sec. 32 adoption trace',
     "| owner decisions recorded only in paraphrase or relayed in session: the requirements of PARAPHRASED-DECISIONS.md, R6.STAT.8, and the owner corrections OC-1 to OC-5 of 2026-11-25 | GitHub comments and session instructions |",
     "| owner decisions recorded only in paraphrase or relayed in session (the requirements of PARAPHRASED-DECISIONS.md, R6.STAT.8), and the owner corrections OC-1 to OC-5 of 2026-11-25, quoted in the owner's words in #1169 comment 7163402499 | GitHub comments, and session instructions quoted in design documents |")
SAFEGUARD['OCFIX'] = ('neutral: the attribution of OC-1 to OC-5 is corrected; their classification as support off `main` '
                      'until quoted in a record on `main` is unchanged.')

# =====================================================================================================
# F3: the three senses of D1-D4, and D1-D8
# =====================================================================================================
in_block_edit('F3', 'R6.NOTE.13',
    "The heading of the verbatim splitter text of sec. 8 uses \"O6\" as such a finding label; it names no control (B-20).\n",
    "The heading of the verbatim splitter text of sec. 8 uses \"O6\" as such a finding label; it names no control (B-20).\n"
    "The label D1-D4 has three senses in the sources: the owner decisions on v3's open points 1-4 (cited as\n"
    "v3 D1-D4); the owner's final decisions D1-D4 of 2026-11-23 in v5.5.9, of which only D2 (the three\n"
    "stricter refusal classes of R6.PROF.9) bears on r6; and D1 to D4 among the Stage 1 review's design\n"
    "corrections D1-D8, which are review findings applied by owner decision S1-D2. PARAPHRASED-DECISIONS.md\n"
    "keys each requirement to the sense its sources use.\n", 'label senses stated')
SAFEGUARD['F3'] = 'neutral: labels disambiguated and decision keys corrected; no requirement content changes.'

# =====================================================================================================
# F5, F6: new rule identifiers; three consistent resolutions; expectations unchanged
# =====================================================================================================
in_block_edit('F5', 'R6.PUR.9',
    "or FAIL (DR-2's expectation restored)", "or FAIL (the expectation of DR-2's form restored)", 'no reuse of the retired id DR-2')
in_block_edit('F6', 'R6.PUR.9',
    "- (a) confirm the accepted residual: V4 and V27 expect PASS, kept so that a change in their outcome\n  is visible;\n"
    "- (b) restore V4's FAIL expectation, which needs DR-2, or a successor rule, in the plan's active rule\n  set.\n",
    "- (a) confirm the accepted residual: V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED,\n"
    "  kept so that a change in their outcome is visible;\n"
    "- (b1) restore the FAIL expectation of V4, V27 and V27-glossary, which needs a plan rule record of the\n"
    "  DR-2 form in the plan's active rule set under a new identifier (DR-2 is retired and never reused,\n"
    "  sec. 33), while V15 stays REVIEW_REQUIRED through `resid`;\n"
    "- (b2) as (b1), and restore V15's FAIL expectation as well, which needs a second plan rule record, of\n"
    "  the DR-1d form, under a second new identifier (DR-1d is retired, sec. 33); a rule of the DR-2 form\n"
    "  does not match V15's text.\n", 'options restated: (a), (b1), (b2), with new identifiers')
in_block_edit('F6', 'R6.PUR.9',
    "rest on the same decision V5-D1\n(RE-1). Until it is made,",
    "rest on the same decision V5-D1\n(RE-1). For each row, (a) selects the candidate \"reversal adopted\" and (b2) the candidate \"reversal\n"
    "rejected\"; (b1) selects \"reversal rejected\" for V4, V27 and V27-glossary and \"reversal adopted\" for\nV15. Until it is made,",
    'per-row selection of the existing candidates stated')
in_block_edit('F5', 'R6.DENY.6',
    "(DR-2 or an equivalent, plan content under R6.DENY.1, reviewed with the deny set)",
    "(a rule of the DR-2 form under a new identifier, since DR-2 is retired and never reused (sec. 33);\n"
    "plan content under R6.DENY.1, reviewed with the deny set)", 'new identifier required')
in_block_edit('F6', 'R6.DENY.6',
    "The owner decides at adoption between (a)\nconfirming the PASS expectation knowingly and (b) restoring the FAIL expectation.",
    "The owner decides at adoption among (a)\nconfirming the PASS expectation knowingly, (b1) restoring the FAIL expectation of V4, V27 and\n"
    "V27-glossary, with V15 REVIEW_REQUIRED, and (b2) restoring it for V15 as well, which needs a second\n"
    "new rule, of the DR-1d form, since a rule of the DR-2 form does not match V15's text (R6.PUR.9).",
    'three resolutions stated')
in_block_edit('F5', 'R6.CTRL.15',
    "needs a rule matching that form, which is a plan-record change (sec. 12).",
    "needs a rule matching that form, under a new identifier (DR-2 is retired and never reused, sec. 33),\n"
    "which is a plan-record change (sec. 12).", 'new identifier required')
in_block_edit('F6', 'R6.CTRL.15',
    "as do V27-glossary and V15, whose candidates are\nREVIEW_REQUIRED `unclassified` and FAIL `deny-match`.",
    "as do V27-glossary and V15, whose candidates are\nREVIEW_REQUIRED `unclassified` and FAIL `deny-match`; V15's FAIL candidate needs, in addition, a rule\n"
    "of the DR-1d form under a second new identifier, since a rule of the DR-2 form does not match V15's\n"
    "text (R6.PUR.9, resolutions (b1) and (b2)).", 'V15 needs a DR-1d-type rule')
in_block_edit('F6', 'OBL-6',
    "Discharged by: the owner's recorded decision on the V4\nreversal at r6's adoption, and the reviewed rule records at `F`.",
    "Discharged by: the owner's recorded decision on the V4\nreversal at r6's adoption, among the resolutions (a), (b1) and (b2) of R6.PUR.9, and the reviewed rule\n"
    "records at `F`, including any new rule identifier that (b1) or (b2) needs.", 'discharge names the three resolutions')
SAFEGUARD['F5'] = ('stricter: a rejection can no longer be implemented by reusing DR-2 (sec. 33, AGENTS.md sec. A.30); '
                   'expectations of V4, V27, V27-glossary and V15 unchanged (checked byte for byte).')
SAFEGUARD['F6'] = ('neutral to stricter: the decision space is stated completely; no resolution is chosen; the four rows '
                   'stay DEFERRED and their candidates unchanged (checked byte for byte).')

# =====================================================================================================
# F4: unmark R6.DENY.1 and R6.DENY.2
# =====================================================================================================
for rid in ('R6.DENY.1', 'R6.DENY.2'):
    remove_mark('F4', rid)
SAFEGUARD['F4'] = ('neutral: the requirements keep their content and controls and still take effect only by r6\'s '
                   'adoption; only the claim that they rest on V5-D1 is removed. They are listed in '
                   'FRESH-AUTHORIZATION.md so that their authorization stays explicit.')

# =====================================================================================================
# F7: mark the unmarked requirements with their decision basis
# =====================================================================================================
F7_ADD = collections.OrderedDict([
    ('R6.CTX.4', ['v3 D1-D4']),
    ('R6.OUT.15', ['R-D labels']),
    ('R6.REC.24', ['R-D labels']),
    ('R6.CTRL.17', ['R-D labels']),
    ('R6.CTRL.23', ['R-D labels']),
    ('R6.RULE.7', ['S1-D2']),
    ('R6.RULE.8', ['S1-D2']),
    ('R6.RULE.9', ['S1-D2']),
    ('R6.CTRL.24', ['S1-D2', 'R-D labels']),
    ('OBL-1', ['S1-D2']),
    ('R6.REC.6', ['DI-2']),
    ('R6.REC.7', ['DI-2']),
    ('R6.CTRL.22', ['DI-2']),
])
F7_EXTRA_KEY = collections.OrderedDict([('R6.PUR.8', 'V5-D2'), ('R6.PROF.9', 'v5.5.9 final D2')])
for rid in F7_ADD:
    add_mark('F7-' + rid, rid)
SAFEGUARD['F7'] = ('stricter: requirements whose decision basis was not shown are now marked and listed for confirmation '
                   'or fresh authorization; no content changes.')

# =====================================================================================================
# F8: a blank line before a requirement that directly follows the previous block
# =====================================================================================================
lines = T.split('\n')
out_lines = []
for i, l in enumerate(lines):
    m = re.match(r'\*\*(R6\.[A-Z0-9]+\.\d+|OBL-\d+)\*\*', l)
    if m and out_lines and out_lines[-1].strip() != '':
        out_lines.append('')
        log('F8', m.group(1), 'blank line inserted before the requirement')
    out_lines.append(l)
T = '\n'.join(out_lines)
SAFEGUARD['F8'] = 'neutral: Markdown rendering only; no text changes.'

# =====================================================================================================
# meta: requirement index, expectation record id
# =====================================================================================================
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


KIND = {q['id']: q for q in REQ_IN}
PEND_IN = {q['id']: list(q['pending_owner_confirmation']) for q in REQ_IN}
RENAME_D = {'R6.PLAN.8': 'v3 D1-D4', 'R6.CTX.1': 'v3 D1-D4', 'R6.CTX.12': 'v3 D1-D4',
            'R6.ANCH.14': 'S1-D2', 'R6.REC.14': 'S1-D2', 'R6.CTRL.19': 'S1-D2', 'R6.EVID.4': 'S1-D2',
            'R6.EVID.5': 'S1-D2', 'OBL-15': 'S1-D2', 'R6.DENY.5': 'S1-D2', 'OBL-3': 'S1-D2'}
PEND = copy.deepcopy(PEND_IN)
for rid, new in RENAME_D.items():
    if PEND[rid].count('D1-D4') != 1:
        PROBLEMS.append('rename %s' % rid)
        continue
    PEND[rid] = [new if k == 'D1-D4' else k for k in PEND[rid]]
    log('F3', 'REQ:' + rid, 'pending key D1-D4 -> %s' % new)
for rid in [r for r, v in PEND.items() if 'D1-D4' in v]:
    PROBLEMS.append('unrenamed D1-D4 key: ' + rid)
for rid in ('R6.DENY.1', 'R6.DENY.2'):
    PEND[rid] = []
    log('F4', 'REQ:' + rid, 'pending key V5-D1 removed')
for rid, keys in F7_ADD.items():
    if PEND[rid]:
        PROBLEMS.append('F7 target already keyed: ' + rid)
    PEND[rid] = list(keys)
    log('F7-' + rid, 'REQ:' + rid, 'pending keys %s' % ', '.join(keys))
for rid, k in F7_EXTRA_KEY.items():
    PEND[rid] = PEND[rid] + [k]
    log('F7-' + rid if rid == 'R6.PUR.8' else 'F3', 'REQ:' + rid, 'pending key %s added' % k)


def req_index(reqs, kind, pend):
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
        out.append(collections.OrderedDict([('id', rid), ('section', sec), ('section_number', num), ('kind', knd),
                                            ('sources', q['sources']), ('controls', q['controls']), ('verification', ver),
                                            ('open', q['open']), ('pending_owner_confirmation', pend.get(rid, []))]))
    return out


REQS = parse_reqs(T)
REQ_OUT = req_index(REQS, KIND, PEND)
REPLAY_OK = dumps(req_index(parse_reqs(T_IN), KIND, PEND_IN)) == REQ_TXT

EXP_OUT = copy.deepcopy(EXP)
EXP_OUT['record_id'] = 'r6-final3-1'
log('meta', 'EXPECTATIONS.json', 'record_id r6-final2-1 -> r6-final3-1 (no row changed)')
MIG_OUT_TXT = MIG_TXT

# =====================================================================================================
# quotations of GitHub comments
# =====================================================================================================
BODY_SHA = collections.OrderedDict((cid, sha(COMM[cid]['body'])) for cid in TX.COMMENTS)
for qid, (cid, q) in TX.QUOTES.items():
    if cid not in COMM or COMM[cid]['body'].count(q) < 1:
        PROBLEMS.append('quote %s not found in comment %s' % (qid, cid))


def quote(qid):
    cid, q = TX.QUOTES[qid]
    return '#1169 comment %s (%s): "%s"' % (cid, COMM[cid]['created_at'], q)


# =====================================================================================================
# PARAPHRASED-DECISIONS.md (regenerated; F1 classes, F2, F3, F4, F7)
# =====================================================================================================
BASE_KEYS = [b[0] for b in TX.BASES]
BYKEY = collections.OrderedDict((k, []) for k in BASE_KEYS)
for q in REQ_OUT:
    for k in q['pending_owner_confirmation']:
        if k not in BYKEY:
            PROBLEMS.append('pending key without a base entry: %s (%s)' % (k, q['id']))
            continue
        BYKEY[k].append(q['id'])
MARKED = [q['id'] for q in REQ_OUT if q['pending_owner_confirmation']]


def para_md():
    L = ['# r6: requirements resting on paraphrased or unrecorded owner decisions', '',
         'This list does not reconstruct any authorization. Each entry names an owner decision that r6\'s requirements '
         'rest on, the class of its record, what the record says, the rule by which the requirements were found, and '
         'the requirements found. Each listed requirement is marked in DESIGN-r6.md with "%s" and carries the decision '
         'key in the field `pending_owner_confirmation` of REQUIREMENTS.json. The exact wording, purpose and '
         'consequences of each listed requirement are in FRESH-AUTHORIZATION.md; the evidence for each class is in '
         'AUTHORIZATIONS.md.' % PEND_TXT, '',
         'Classes of record (verified by reading the #1169 comments with GET requests):', '',
         '- %s: a comment that quotes the owner\'s words explicitly; such decisions need no entry here and are listed in AUTHORIZATIONS.md;' % TX.CLASS_TEXT['i'],
         '- %s: a comment posted from the `amaybaum` account by the coordinating session that records an owner decision in the session\'s words and quotes no owner words;' % TX.CLASS_TEXT['ii'],
         '- %s: the decision is stated only in design documents relayed in session, with no comment id.' % TX.CLASS_TEXT['iii'], '',
         'Options for every entry:', '',
         '- (a) confirm in the owner\'s own words: the owner records the decision in a comment, which r6 quotes byte-exact with author and time (AGENTS.md sec. A.42 item 7);',
         '- (b) fresh authorization: the owner decides the question anew, in a recorded decision, and r6 cites that record;',
         '- (c) withdraw the requirement: the requirement, or the part of it that rests on the decision, is removed or narrowed, with its verification traced (R6.STAT.5).',
         '', 'Requirements marked: %d.' % len(MARKED), '']
    for key, cls, head, qids, where, says, rule, note in TX.BASES:
        L += ['***', '', '## ' + head, '', '- Key: `%s`' % key, '- Class: %s' % TX.CLASS_TEXT[cls]]
        if qids:
            L.append('- Record on GitHub (exact text):')
            for qid in qids:
                L.append('  - ' + quote(qid))
        else:
            L.append('- Record on GitHub: none.')
        L += ['- Where else stated: ' + where, '- What it says: ' + says, '- Rule used to find the requirements: ' + rule]
        rq = BYKEY[key]
        L.append('- Requirements affected: ' + (', '.join(rq) + '.' if rq else
                 'none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.'))
        if note:
            L.append('- Note: ' + note)
        L += ['- Options: (a) confirm in the owner\'s own words; (b) fresh authorization; (c) withdraw the requirement.', '']
    L += ['***', '', '## Requirements no longer marked', '',
          '- R6.DENY.1 and R6.DENY.2 cited E-1001 only because that item mentions the retired DR-1d and DR-2. Their content '
          '(rule records are plan records; the controls run on pinned rule inputs) does not depend on V5-D1, so they are not '
          'marked. Like every requirement of r6 they take effect only by r6\'s adoption; they are listed in '
          'FRESH-AUTHORIZATION.md.', '']
    return '\n'.join(L)


PARA_OUT = para_md()
log('F1', 'PARAPHRASED-DECISIONS.md', 'each entry carries its record class and, for class (ii), the exact text of the record')
log('F2', 'PARAPHRASED-DECISIONS.md', 'V5-D2 described as the widening of `resid`; the W2 allow rules rest on no owner decision')
log('F3', 'PARAPHRASED-DECISIONS.md', 'entries v3 D1-D4, S1-D2 and v5.5.9 final D2 replace the single entry "D1-D4"')
log('F4', 'PARAPHRASED-DECISIONS.md', 'R6.DENY.1 and R6.DENY.2 removed from V5-D1')
log('F7', 'PARAPHRASED-DECISIONS.md', 'entry DI-2 added; the requirements marked by F7 listed under their keys')

# =====================================================================================================
# AUTHORIZATIONS.md
# =====================================================================================================


def auth_md():
    L = ['# r6: authorizations and decision records the design relies on', '',
         'Every decision label the design relies on, classified by its record, with the evidence and with what it '
         'permits and does not permit. The comments were read with GET requests; for each, the time is the API\'s '
         '`created_at` and the body digest is the sha256 of the body as returned.', '',
         'Classes: %s; %s; %s.' % (TX.CLASS_TEXT['i'], TX.CLASS_TEXT['ii'], TX.CLASS_TEXT['iii']), '',
         '| Comment | created_at | Body sha256 |', '|---|---|---|']
    for cid in TX.COMMENTS:
        L.append('| %s | %s | %s |' % (cid, COMM[cid]['created_at'], BODY_SHA[cid]))
    L += ['', '***', '', '## 1. Class (i): the owner\'s own words on GitHub', '', TX.CLASS_I_PATTERN, '']
    for cid, when, what, qids, permits, notp, used in TX.CLASS_I:
        L += ['### #1169 comment %s (%s): %s' % (cid, when, what), '', 'Owner\'s words and approved text (exact):', '']
        for qid in qids:
            L.append('- "%s"' % TX.QUOTES[qid][1])
        L += ['', '- Permits: ' + permits, '- Does not permit: ' + notp, '- Relied on by: ' + used, '']
    L += ['***', '', '## 2. Class (ii): session-written records without owner words', '',
          'Each record below opens with "Recorded by the coordinating session" and states owner decisions in the '
          'session\'s words. It shows that a decision was reported, not its wording. By itself it permits nothing '
          'for r6: a requirement resting on it needs confirmation in the owner\'s words or fresh authorization '
          '(quoted instruction of #1169 comment 7162098696: "%s").' % TX.QUOTES['Q-7162-PARA'][1], '']
    for key, cls, head, qids, where, says, rule, note in TX.BASES:
        if cls != 'ii':
            continue
        L += ['### ' + head, '', '- Key: `%s`' % key]
        for qid in qids:
            L.append('- ' + quote(qid))
        L += ['- Where else stated: ' + where, '- What the record says was decided: ' + says,
              '- Permits: nothing by itself for r6; the requirements keyed `%s` await (a) or (b).' % key,
              '- Does not permit: treating the session\'s paraphrase as the owner\'s wording; reconstructing authorization from it.',
              '- Relied on by: ' + (', '.join(BYKEY[key]) or 'no requirement'), '']
    L += ['***', '', '## 3. Class (iii): no GitHub record', '',
          'These decisions are stated only in design documents relayed in session, each without a comment id. A '
          'search of all comments on #1169 for distinctive phrases of each (for example "S1-D1", "R-D1", "A-D5", '
          '"three stricter", "chained edits", "Approve O-1 option (b)", "historical authorization verification '
          'entirely", "Authorize the Stage A review") found no record of the decision; the labels S1-D1, S1-D2 and '
          'S1-D3 occur only in later session-written result comments. #1169 comment 7158801838 lists them as owner '
          'decisions without a record: "%s"' % TX.QUOTES['Q-7158801-NOREC'][1], '']
    for key, cls, head, qids, where, says, rule, note in TX.BASES:
        if cls != 'iii':
            continue
        L += ['### ' + head, '', '- Key: `%s`' % key, '- Where stated: ' + where, '- What it says: ' + says,
              '- Permits: nothing for r6; the requirements keyed `%s` await (a) or (b).' % key,
              '- Does not permit: citing the design document\'s quotation or label as an owner record.',
              '- Relied on by: ' + (', '.join(BYKEY[key]) or 'no requirement')]
        if note:
            L.append('- Note: ' + note)
        L.append('')
    L += ['***', '', '## 4. Labels that are not owner decisions', '',
          '- D1 to D8 of the Stage 1 review: review findings, applied by owner decision S1-D2 (class (iii)).',
          '- C3 and C4: findings of the v5.4 review addendum, applied under the owner decisions R-D1 to R-D5 (class (iii)).',
          '- OD-1 to OD-31, MC-*, VD-*, ME-* (DECISIONS.md), RD-1 to RD-35 (RESIDUAL.md), RE-1 to RE-38 (RESIDUAL-2.md): '
          'recommendations prepared by the coordinating session, approved by the owner as the basis for drafting r6 '
          '(class (i): #1169 comments 7160281751, 7160980912, 7162098696). The approval covers drafting; the content '
          'takes effect only by r6\'s adoption.',
          '- OC-1 to OC-5: items 1 to 4 and 6 of the proposal quoted in #1169 comment 7163402499, authorized by the '
          'owner "as proposed" in the same comment (class (i)).',
          '- E-*, V1-*, V2-*, A-*, RV-*: inventory and review items (provenance), not decisions.', '']
    return '\n'.join(L)


AUTH_OUT = auth_md()

# =====================================================================================================
# FRESH-AUTHORIZATION.md
# =====================================================================================================
CLS = {b[0]: b[1] for b in TX.BASES}


def bq(s):
    return '\n'.join(('> ' + x) if x else '>' for x in s.rstrip('\n').split('\n'))


def fresh_md():
    entries = MARKED + ['R6.DENY.1', 'R6.DENY.2']
    for rid in entries:
        if rid not in TX.NOTES:
            PROBLEMS.append('no analysis for ' + rid)
    flagged = [r for r in entries if TX.NOTES.get(r, (None,) * 5)[4]]
    L = ['# r6: requirements needing confirmation or fresh authorization', '',
         'Every requirement of r6 whose decision basis is not a class (i) record (the owner\'s own words on GitHub): '
         'the %d requirements marked "%s" and the two requirements unmarked by F4 (R6.DENY.1, R6.DENY.2). For each: '
         'its exact current wording, quoted mechanically from DESIGN-r6.md; its decision basis and class; its '
         'purpose; the consequences of authorizing and of not authorizing it; the safeguards affected; and whether '
         'it permits something an earlier design prohibited (flagged). Nothing here is adopted: every requirement '
         'of r6 takes effect only by r6\'s adoption, and an authorization of one requirement does not authorize '
         'another or a group.' % (len(MARKED), PEND_TXT), '',
         'Flagged (permits something an earlier design prohibited, or narrows a check): %s.' % ', '.join(flagged), '',
         '| Requirement | Decision basis | Class | Flag |', '|---|---|---|---|']
    pend = {q['id']: q['pending_owner_confirmation'] for q in REQ_OUT}
    for rid in entries:
        keys = pend.get(rid) or ['none (F4)']
        cls = ', '.join(sorted(set(CLS.get(k, '-') for k in keys)))
        L.append('| %s | %s | %s | %s |' % (rid, '; '.join(keys), cls if pend.get(rid) else 'no decision cited', 'yes' if rid in flagged else ''))
    L += ['', 'Not a requirement, listed for completeness: the row of sec. 33 "DR-1d, DR-2 | obsolete: dropped deny '
          'candidates (rationale in the appendix); never reused" rests on V5-D1 (class (ii)). Withdrawing V5-D1 would '
          'not reinstate DR-1d or DR-2 under those identifiers: a retired identifier is never reused (AGENTS.md sec. '
          'A.30); a rule of either form would take a new identifier (V4-COMPARISON.md).', '']
    for rid in entries:
        purpose, auth, notauth, safe, flag = TX.NOTES[rid]
        keys = pend.get(rid) or []
        L += ['***', '', '## ' + rid, '']
        if keys:
            L.append('Decision basis: ' + '; '.join('`%s`, class %s' % (k, TX.CLASS_TEXT[CLS[k]]) for k in keys) + '.')
        else:
            L.append('Decision basis: none cited (unmarked by F4); authorized only by r6\'s adoption.')
        L += ['', 'Current wording (DESIGN-r6.md):', '', bq(block(rid)), '',
              '- Purpose: ' + purpose, '- If authorized: ' + auth, '- If not authorized: ' + notauth,
              '- Safeguards affected: ' + safe]
        if flag:
            L.append('- FLAG, earlier designs: ' + flag)
        L.append('')
    return '\n'.join(L)


FRESH_OUT = fresh_md()

# =====================================================================================================
# V4-COMPARISON.md
# =====================================================================================================
RIDX = collections.OrderedDict((r['id'], r) for r in EXP['rows'])
MATCH = []
for name, text in TX.V_TEXTS:
    MATCH.append((name, text) + tuple('match' if re.search(TX.DR_PATTERNS[k], text) else 'no match' for k in ('DR-2', 'DR-1d')))
EXPECT_MATCH = {'V4': ('match', 'no match'), 'V27': ('match', 'no match'), 'V27-glossary': ('match', 'no match'),
                'V15': ('no match', 'match')}
for name, text, m2, m1 in MATCH:
    if name in EXPECT_MATCH and EXPECT_MATCH[name] != (m2, m1):
        PROBLEMS.append('V4-COMPARISON: unexpected rule match for %s: DR-2 %s, DR-1d %s' % (name, m2, m1))
    if name == 'PUR.8 example' and (m2, m1) != ('no match', 'no match'):
        PROBLEMS.append('V4-COMPARISON: PUR.8 example matches a dropped rule: ' + text)


def cand(rid, label_start):
    for c in RIDX[rid]['candidate_expectations']:
        if c['label'].startswith(label_start):
            return c
    PROBLEMS.append('candidate %s/%s' % (rid, label_start))
    return None


def v4_md():
    L = ['# r6: the V4 group, three consistent resolutions compared (deferred)', '',
         'The expected outcomes of V4, V27, V27-glossary and V15 stay deferred (#1169 comments 7160980912, 7162098696, '
         '7163402499 and 7164340996). This document compares the three consistent resolutions; it recommends none and '
         'changes no expectation. The four rows of EXPECTATIONS.json are byte-identical to the previous draft.', '',
         '## 1. Current state', '',
         'Each row has `expect` DEFERRED and two candidate expectations, each "not authoritative; decided at r6 '
         'adoption" (RE-1). The gate reports `deferred-expectation` and never holds on them; S13 leaves them out '
         '(R6.A1CFG.7).', '', '| Row | Candidate "reversal adopted" | Candidate "reversal rejected" |', '|---|---|---|']
    for rid in ('V4', 'V27', 'V27-glossary', 'V15'):
        a, r = cand(rid, 'reversal adopted'), cand(rid, 'reversal rejected')
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
          'None of the constructed examples of R6.PUR.8 matches either form. The tool measured the four rows under the '
          'current rule set (v6.0e sec. 6.4.1, "What removing them costs (measured)"): neither form matches any line of '
          'any tree at E, H, W or T1\' or any of the 4677 historical corpus blobs, and the distinct deny-line counts at '
          'E, H and W are the same with or without them (95, 86, 86). Adding a rule of either form changes outcomes for '
          'constructed strings only, and needs reconciliation against N-W and the independent review of the deny set '
          '(OBL-3).', '',
          '## 3. The three resolutions', '',
          'Earlier designs: v2\'s demonstration expected V4 FAIL (DESIGN-v2.md line 429); v4 expected V4 FAIL `deny-match` '
          'by DR-2 and V15 FAIL `deny-match` by DR-1d (DESIGN-v4.md lines 1172 and 1185); v5.5.9 and v6.0e expect V4 and '
          'V27 PASS and V15 REVIEW_REQUIRED.', '']
    for name, sel, rules, ids, outcome, earlier, s13 in TX.RESOLUTIONS:
        L += ['### ' + name, '', '| Row | Expectation selected | Expectation (exact) |', '|---|---|---|']
        for rid in ('V4', 'V27', 'V27-glossary', 'V15'):
            c = cand(rid, sel[rid])
            L.append('| %s | %s | `%s` |' % (rid, c['label'], json.dumps(c['expect'], sort_keys=True)))
        L += ['', '- Rules needed: ' + rules, '- Identifiers: ' + ids, '- What it permits and prohibits: ' + outcome,
              '- Relative to earlier designs: ' + earlier, '- S13 and obligations: ' + s13, '']
    L += ['## 4. Trade-offs', '',
          '- (a) needs no new rule and no review of new patterns, and leaves the ordinal-property and reversed-ordinal '
          'forms to review outside the tool (V15 at least REVIEW_REQUIRED). It permits what v2 and v4 prohibited.',
          '- (b1) restores tool detection of the form v2 and v4 named for V4 at the cost of one new rule, its review '
          'and its reconciliation; V15 stays REVIEW_REQUIRED, which v4 did not permit.',
          '- (b2) restores v4\'s detection for both forms at the cost of two new rules; neither form has a real-tree '
          'witness (v6.0e sec. 6.4.1), so both rules are justified by constructed strings only.',
          '- In every resolution the retired identifiers DR-1d and DR-2 stay retired; the decision text names the new '
          'identifiers (b1, b2) or confirms that none is added (a).', '',
          '## 5. Draft decision texts (for the owner\'s choice at r6 adoption; not adopted)', '',
          '- (a): "I confirm that the A1 plan\'s active deny set contains no rule of the DR-1d or DR-2 form, and I accept '
          'knowingly that the added texts of V4, V27 and V27-glossary PASS with no hit and that of V15 is REVIEW_REQUIRED '
          'only, with detection of those forms resting on review outside the tool."',
          '- (b1): "I reject the V4 reversal for the ordinal-property form: the amended plan\'s rule records at `F` '
          'include an independently reviewed deny rule of the DR-2 form under a new identifier, so that V4, V27 and '
          'V27-glossary FAIL `deny-match`, while V15 stays REVIEW_REQUIRED through `resid`."',
          '- (b2): as (b1), "and a second independently reviewed deny rule of the DR-1d form under a second new '
          'identifier, so that V15 also FAILs `deny-match`."', '']
    return '\n'.join(L)


V4_OUT = v4_md()

# =====================================================================================================
# self-checks: those of correct.py, parameterized; run before (out-final2) and after (out-final3)
# =====================================================================================================


def run_checks(text, rows, req_out, exp_out, ref_rows=None, kind_text_in=None):
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
    marked_txt = sorted(r for r, q in reqs.items() if PEND_TXT in q['text'])
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
    return C, VALUES


CHK_BEFORE, VAL_BEFORE = run_checks(T_IN, EXP['rows'], REQ_IN, EXP)
CHK_AFTER, VAL_AFTER = run_checks(T, EXP_OUT['rows'], REQ_OUT, EXP_OUT)
OWN = collections.OrderedDict()
OWN['replay: correct.py\'s index rule reproduces out-final2/REQUIREMENTS.json from out-final2/DESIGN-r6.md'] = [] if REPLAY_OK else ['mismatch']
OWN['F5/F6: V4, V27, V27-glossary, V15 rows byte-identical to out-final2 and DEFERRED'] = [
    i for i in ('V4', 'V27', 'V27-glossary', 'V15') if dumps(RIDX[i]) != dumps(collections.OrderedDict((r['id'], r) for r in EXP_OUT['rows'])[i])
    or RIDX[i]['expect'] != {'outcome': 'DEFERRED'}]
OWN['preservation: every expectation row byte-identical to out-final2'] = [
    a['id'] for a, b in zip(EXP['rows'], EXP_OUT['rows']) if dumps(a) != dumps(b)] + ([] if len(EXP['rows']) == len(EXP_OUT['rows']) else ['count'])
OWN['preservation: retired list unchanged'] = [] if dumps(EXP_OUT['retired']) == dumps(EXP['retired']) else ['changed']
OWN['preservation: no requirement id removed or added'] = sorted(set(parse_reqs(T_IN)) ^ set(REQS))
OWN['preservation: sources and controls of every requirement unchanged'] = [
    q['id'] for q in REQ_OUT if (q['sources'], q['controls']) != (KIND[q['id']]['sources'], KIND[q['id']]['controls'])]
OWN['preservation: sections 33 and 34 unchanged'] = (
    [] if T[T.index('## 33. Retired'):T.index('## Appendix H.')] == T_IN[T_IN.index('## 33. Retired'):T_IN.index('## Appendix H.')] else ['changed'])
H_OUT = T[T.index('## Appendix H.'):]
H_IN = T_IN[T_IN.index('## Appendix H.'):]
OWN['preservation: Appendix H changed only in HIST-4'] = (
    [] if re.sub(r'- HIST-4\..*?(?=\n- HIST-5\.)', '', H_OUT, flags=re.S) == re.sub(r'- HIST-4\..*?(?=\n- HIST-5\.)', '', H_IN, flags=re.S) else ['changed'])
OWN['preservation: MIGRATION.json unchanged'] = [] if MIG_OUT_TXT == MIG_TXT else ['changed']
ws = lambda s: re.sub(r'\s+', ' ', s).strip()
OWN['F8: design text unchanged apart from the logged edits (whitespace-normalized diff limited to edited blocks)'] = []
OWN['F7/F3/F4: pending keys equal the intended map'] = [r for r in PEND if PEND[r] != [q for q in REQ_OUT if q['id'] == r][0]['pending_owner_confirmation']]
OWN['quotes: every quotation of a comment occurs in its body'] = [p for p in PROBLEMS if p.startswith('quote ')]
OWN['V4-COMPARISON: rule-form matches as expected'] = [p for p in PROBLEMS if p.startswith('V4-COMPARISON')]
# whitespace-normalized comparison outside the edited blocks
EDITED = set(t for _, t, _ in LOG if re.match(r'(R6\.[A-Z0-9]+\.\d+|OBL-\d+)$', t))
for rid in parse_reqs(T_IN):
    if rid in EDITED:
        continue
    if ws(block(rid, T_IN)) != ws(block(rid, T)):
        OWN['F8: design text unchanged apart from the logged edits (whitespace-normalized diff limited to edited blocks)'].append(rid)
for k, v in list(CHK_AFTER.items()) + list(OWN.items()):
    if v:
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================================
# CORRECTION-REPORT.md
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


def report():
    L = ['# r6 correction report, second round (F1 to F8, the unmarked requirements, OC attribution)', '',
         'Deterministic correction by `build/correct2.py`, which reads `out-final2/` (read only), MAPPING.json and the '
         '#1169 comments read with GET requests, and applies the logged edits below. Each edit carries the finding it '
         'applies (F1 to F8, F7-<requirement>, OCFIX) or `meta`. Authorization, quoted: %s. No governance rule is '
         'amended, no exception is created, no expectation of the V4 group changes, and r6 stays a draft. No git or '
         'GitHub write was made.' % quote('Q-7164340-OWN'), '', 'Findings applied:', '']
    for k, v in TX.FINDINGS.items():
        L.append('- %s: %s' % (k, v))
    L += ['', 'Correction of the previous report (OCFIX). The previous report stated that the owner corrections OC-1 to '
          'OC-5 "were relayed in session without a comment id". That is incorrect: %s The owner\'s approval quoted '
          'there is "%s", and items 1 to 4 and 6 of the quoted proposal are OC-1 to OC-5 (AUTHORIZATIONS.md). The '
          'statement is corrected in the adoption trace of sec. 32 (edit OCFIX) and in this report; the previous report '
          'is a record of its round and is not edited.' % (quote('Q-7164065-ERR'), TX.QUOTES['Q-7163-OWN'][1]),
          '', '***', '', '## 1. Inputs and outputs (sha256)', '']
    L += table(['Input (read only)', 'sha256'], INPUT_SHA)
    L += ['', 'Comment bodies read (sha256 of the body as returned by the API): see AUTHORIZATIONS.md.', '']
    L += table(['Output', 'sha256'], [(n, sha(c)) for n, c in CONTENT.items()] +
               [('CORRECTION-REPORT.md', 'this file (its digest is reported by the generator run)')])
    L += ['', '***', '', '## 2. Edits applied', '']
    SG = {'F1': 'stricter or neutral', 'OCFIX': 'neutral', 'F2': 'neutral', 'F3': 'neutral', 'F4': 'neutral',
          'F5': 'stricter', 'F6': 'neutral to stricter', 'F7': 'stricter', 'F8': 'neutral', 'meta': 'neutral'}
    L += table(['#', 'Finding', 'Target', 'Edit', 'Safeguard'],
               [(i + 1, a, b, d, 'none weakened (%s; sec. 3)' % SG[a.split('-')[0] if a.startswith('F7-') else a])
                for i, (a, b, d) in enumerate(LOG)])
    L += ['', '***', '', '## 3. Safeguards, per finding', '',
          'No edit weakens a safeguard. Per finding:', '']
    for k, v in SAFEGUARD.items():
        L.append('- %s: %s' % (k, v))
    L += ['- F2: neutral: the description of V5-D2 in PARAPHRASED-DECISIONS.md is corrected; the design\'s requirements '
          'and the rule obligations of R6.DENY.5 and OBL-3 are unchanged.', '',
          'Flagged for the owner (not weakened by this round, but listed in FRESH-AUTHORIZATION.md as permitting what an '
          'earlier design prohibited or narrowing a check): ' + ', '.join(
              r for r in MARKED + ['R6.DENY.1', 'R6.DENY.2'] if TX.NOTES[r][4]) + '.', '',
          '***', '', '## 4. Self-checks (before: out-final2; after: out-final3)', '']
    rows_ = []
    for k in CHK_AFTER:
        b, a = CHK_BEFORE[k], CHK_AFTER[k]
        rows_.append((k, len(b) if not b else '%d (%s)' % (len(b), ', '.join(map(str, b[:6]))),
                      len(a) if not a else '%d (%s)' % (len(a), ', '.join(map(str, a[:6])))))
    L += table(['Check (correct.py, parameterized)', 'Before', 'After'], rows_)
    L += ['']
    L += table(['Value', 'Before', 'After', 'Why it changed'],
               [(k, VAL_BEFORE[k], VAL_AFTER[k],
                 ('F7 marks 13 requirements and F4 unmarks 2 (33 - 2 + 13)' if k.startswith('requirements marked') else
                  '' if VAL_BEFORE[k] == VAL_AFTER[k] else 'see edits')) for k in VAL_AFTER])
    L += ['', 'Checks of this round:', '']
    for k, v in OWN.items():
        L.append('- %s: %s' % (k, len(v) if not v else '%d (%s)' % (len(v), ', '.join(map(str, v[:10])))))
    L += ['- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return, no invisible '
          'formatting character, no non-ASCII space, and no non-ASCII character outside those of the inputs and the '
          'quoted comments, in any output: checked',
          '- reproducibility: the generator re-ran itself in a separate process (`python3 -I -B`) and compared the '
          'sha256 of every output before writing; identical',
          '- generator problems: %d' % len(PROBLEMS), '',
          '***', '', '## 5. Remaining open items', '']
    L += ['- ' + o for o in TX.OPEN_ITEMS]
    L += ['', '## 6. Contradictions and departures found while correcting', '']
    L += ['- ' + c for c in TX.CONTRADICTIONS]
    L += ['']
    return '\n'.join(L)


CONTENT['CORRECTION-REPORT.md'] = report()

# =====================================================================================================
# hygiene, reproducibility, write
# =====================================================================================================


def nonascii(c):
    return set(ch for ch in c if ord(ch) > 127)


ALLOWED = nonascii(T_IN + EXP_TXT + REQ_TXT + MIG_TXT + PARA_TXT) | set().union(
    *[nonascii(q) for _, q in TX.QUOTES.values()]) | {'\u2019'}  # the right quotation mark of v6.0e's DR-1d pattern
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

#!/usr/bin/env python3
"""Deterministic correction of design r6 (ledger coverage tool), owner corrections of 2026-11-25.

Reads out-final/ (read only) and writes out-final2/.  Every change is an explicit, logged edit that
carries the number of the owner-authorized correction it applies (OC-1 to OC-5) or marks a mechanical
consequence (meta).  No hand-edited output; two runs give byte-identical files; the self-checks of
out-final/build/final.py are re-run on the corrected outputs.
"""
import collections
import copy
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
R6 = os.path.dirname(OUT)
FIN = os.path.join(R6, 'out-final')


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


INPUTS = ['out-final/DESIGN-r6.md', 'out-final/EXPECTATIONS.json', 'out-final/REQUIREMENTS.json',
          'out-final/MIGRATION.json', 'out-final/PARAPHRASED-DECISIONS.md', 'out-final/FINAL-REPORT.md',
          'out-final/build/final.py', 'MAPPING.json']
INPUT_SHA = [(p, sha(open(os.path.join(R6, p), 'rb').read())) for p in INPUTS]

T = rd(os.path.join(FIN, 'DESIGN-r6.md'))
T_IN = T
EXP_TXT = rd(os.path.join(FIN, 'EXPECTATIONS.json'))
EXP = rj(EXP_TXT)
REQ_TXT = rd(os.path.join(FIN, 'REQUIREMENTS.json'))
REQ_IN = rj(REQ_TXT)
MIG_TXT = rd(os.path.join(FIN, 'MIGRATION.json'))
MIG = rj(MIG_TXT)
PARA_TXT = rd(os.path.join(FIN, 'PARAPHRASED-DECISIONS.md'))
MAPPING = rj(rd(os.path.join(R6, 'MAPPING.json')))

LOG = []
PROBLEMS = []


def log(item, target, desc):
    LOG.append((item, target, desc))


# ------------------------------------------------------------------ text helpers (as final.py)
BLOCK_END = re.compile(r'\n(?=\*\*R6\.[A-Z0-9]+\.\d+\*\*|\*\*OBL-\d+\*\*|#|\*\*\*\s*$|\*\*Table )', re.M)


def block_span(rid, text=None):
    text = T if text is None else text
    a = text.index('**%s**' % rid)
    m = BLOCK_END.search(text, a + 3)
    return a, (m.start() if m else len(text))


def edit(item, target, old, new, count=1):
    global T
    n = T.count(old)
    if n != count:
        PROBLEMS.append('edit %s/%s: expected %d occurrence(s), found %d: %r' % (item, target, count, n, old[:80]))
        return
    T = T.replace(old, new)
    log(item, target, 'text edit (%d occurrence(s))' % count)


def in_block_edit(item, rid, old, new):
    global T
    a, b = block_span(rid)
    blk = T[a:b]
    if blk.count(old) != 1:
        PROBLEMS.append('in_block_edit %s/%s: %d occurrences of %r' % (item, rid, blk.count(old), old[:70]))
        return
    T = T[:a] + blk.replace(old, new) + T[b:]
    log(item, rid, 'text edit')


def replace_block(item, rid, new, must_contain):
    global T
    a, b = block_span(rid)
    old = T[a:b]
    if must_contain not in old:
        PROBLEMS.append('replace_block %s/%s: marker not found: %r' % (item, rid, must_contain))
        return
    tail = old[len(old.rstrip('\n')):]
    T = T[:a] + new.rstrip('\n') + tail + T[b:]
    log(item, rid, 'requirement block restated')


def insert_after_block(item, rid, new):
    global T
    a, b = block_span(rid)
    e = a + len(T[a:b].rstrip('\n'))
    T = T[:e] + '\n\n' + new.rstrip('\n') + T[e:]
    log(item, new.split('**')[1], 'requirement block added after %s' % rid)


def parse_list(s):
    s = re.sub(r'\([^()]*\)', '', s)
    s = re.sub(r'\([^()]*\)', '', s)
    out = []
    for t in s.split(','):
        t = t.strip().rstrip('.').strip()
        if t and t != 'none' and not t.startswith('none'):
            out.append(t)
    return out


def add_sources(item, rid, labels):
    global T
    a, b = block_span(rid)
    blk = T[a:b]
    m = re.search(r'Sources:(.*?)(?=Controls:|$)', blk, re.S)
    if not m:
        PROBLEMS.append('add_sources %s' % rid)
        return
    body = m.group(1)
    core = body.rstrip()
    tail = body[len(core):]
    new = [x for x in labels if x not in parse_list(core)]
    if not new:
        return
    core2 = (core[:-1] + ', ' + ', '.join(new) + '.') if core.endswith('.') else (core + ', ' + ', '.join(new))
    T = T[:a] + blk[:m.start(1)] + core2 + tail + blk[m.end(1):] + T[b:]
    log(item, rid, 'Sources: added %s' % ', '.join(new))


def table_row_edit(item, cid, fn):
    """Edit the case cell of one row of Table 17.1."""
    global T
    a17 = T.index('**Table 17.1. Control catalogue**')
    b17 = T.index('**Table 17.2. Record-directory mutants**')
    lines = T[a17:b17].split('\n')
    hit = [k for k, l in enumerate(lines) if l.startswith('| %s |' % cid)]
    if len(hit) != 1:
        PROBLEMS.append('table_row_edit %s: %d rows' % (cid, len(hit)))
        return
    k = hit[0]
    cells = lines[k][2:-2].split(' | ')
    if len(cells) > 6:
        cells = cells[:5] + [' | '.join(cells[5:])]
    new = fn(cells[5])
    if new == cells[5]:
        PROBLEMS.append('table_row_edit %s: no change' % cid)
        return
    cells[5] = new
    lines[k] = '| ' + ' | '.join(cells) + ' |'
    T = T[:a17] + '\n'.join(lines) + T[b17:]
    log(item, 'Table 17.1:' + cid, 'case cell edited')


def sub1(old, new):
    def f(s):
        if s.count(old) != 1:
            PROBLEMS.append('sub1: %d occurrences of %r' % (s.count(old), old[:60]))
            return s
        return s.replace(old, new)
    return f


def trace_row(item, oid, new):
    global T
    a = T.index('## 32. Outstanding obligations')
    b = T.index('**OBL-1** ', a)
    seg = T[a:b]
    lines = seg.split('\n')
    hit = [k for k, l in enumerate(lines) if l.startswith('| %s |' % oid)]
    if len(hit) != 1:
        PROBLEMS.append('trace_row %s: %d rows' % (oid, len(hit)))
        return
    lines[hit[0]] = new
    T = T[:a] + '\n'.join(lines) + T[b:]
    log(item, 'sec. 32 trace:' + oid, 'trace row restated')


# ------------------------------------------------------------------ expectation helpers
rows = copy.deepcopy(EXP['rows'])
RIDX = collections.OrderedDict((r['id'], r) for r in rows)
ROWS_IN = {r['id']: dumps(r) for r in EXP['rows']}

ROW_ORDER_KEYS = ['id', 'migrated_from', 'requirements', 'runner', 'operations', 'direction', 'paired_with',
                  'predicate_kind', 'case', 'expect', 'candidate_expectations', 'restored', 'procedure',
                  'composed_of', 'depends_on', 'status_allowed', 'not_run', 'reference', 'source', 'flags']


def order_row(r):
    o = collections.OrderedDict()
    for k in ROW_ORDER_KEYS:
        if k in r:
            o[k] = r[k]
    for k in r:
        if k not in o:
            PROBLEMS.append('row %s: unknown field %s' % (r['id'], k))
            o[k] = r[k]
    return o


def flags_replace(item, cid, drop_pred, add):
    r = RIDX[cid]
    fl = [f for f in r.get('flags', []) if not drop_pred(f)]
    for n in add:
        if n not in fl:
            fl.append(n)
    r['flags'] = fl
    log(item, 'EXP:' + cid, 'flags updated')


def add_inv(target, inv):
    target.setdefault('invariants', [])
    for i in inv:
        if i not in target['invariants']:
            target['invariants'].append(i)


def set_ref(item, cid, ref):
    r = RIDX[cid]
    r.setdefault('reference', collections.OrderedDict())
    for k, v in ref.items():
        r['reference'][k] = v
    log(item, 'EXP:' + cid, 'reference: T1\' measurement recorded as provenance')


def str_sub(item, cid, path, old, new):
    """Replace a substring in a string field reached by path (list of keys / indices)."""
    r = RIDX[cid]
    o = r
    for p in path[:-1]:
        o = o[p]
    s = o[path[-1]]
    if s.count(old) != 1:
        PROBLEMS.append('str_sub %s %s: %d occurrences of %r' % (cid, path, s.count(old), old[:60]))
        return
    o[path[-1]] = s.replace(old, new)
    log(item, 'EXP:' + cid, 'field %s edited' % '/'.join(str(p) for p in path))


OFFMAIN = lambda f: f.startswith('inputs off main') or f.startswith("the T1' case: inputs off main")
XREP = "X_rep (R6.EVID.8): single parent H; ledgered paths H plus the ledger's splices, sha256 equal to the ledger's expected_sha256; plan record-directory paths the pinned ledger and edit list; delegated paths a fixed marker blob; every other path H's"
SCAN_CORPUS = 'ledgered and corpus paths of X_rep, and the segments E..H and H..X'
SCAN_TERMS = 'ledgered and corpus paths of X_rep'
SCAN_EXEC = 'side changes H..M, the ledgered and corpus path sets, and the candidate blobs on drifted paths'
REF_T1P = collections.OrderedDict([("measured_at_T1p_14ac71b4_with_tool_commit_a3799244",
                                    "the expected figures of this row were measured there; historical measurement and provenance (AGENTS.md sec. A.42 item 2); carried to X_rep as expectations because the paths the verdict reads are byte-identical when T1' conforms (R6.EVID.8); not the support of any enduring claim")])
OC3_FLAG = ("OC-3: runs at X_rep (R6.EVID.8); the verdict reads only paths that H and the ledger determine, so T1''s "
            "identity and ancestry are not material; landing decision: kind 1 on the exact tool candidate; enduring "
            "claim: kind 2 once the landing merge is on main, kind 3 re-run on main, every input reachable from main")

# =====================================================================================
# OC-1: TR5 and OBL-16, consistent with AGENTS.md sec. A.39
# =====================================================================================
replace_block('OC-1', 'OBL-16',
    "**OBL-16** Native runs for G-A1 and TR5. TR5 is the exact-candidate validation of the plan freeze, in three\n"
    "parts, none of which places `F` on `main` before its designation:\n"
    "- (a) exact-candidate validation, before the owner designates `F` (AGENTS.md sec. A.39), with the\n"
    "  round's branch held at exactly the candidate commit (AGENTS.md sec. A.43 item 3): the exact-head\n"
    "  check-run of sec. A.39 on the candidate (the workflow dispatched on it, the run whose `head_sha` is\n"
    "  that commit, every job green); and TR5's chain-admitted run, the pinned workflow dispatched on `main`\n"
    "  at the tool commit `T` (R6.REC.18 points 1 and 6, R6.REC.19) with `--freeze` the same full commit id\n"
    "  and `--config` a reviewed configuration listed in the last `Record pins` subsection of the\n"
    "  `PREREG.md` beside it, holding with `config.admission.mode` `\"chain\"` and every snapshot field\n"
    "  (R6.REC.24). The two runs are distinct because chain admission requires the `head_branch` `main`\n"
    "  (R6.REC.18 point 6); each records the candidate's full id, which binds them. The candidate is fetched\n"
    "  by its full id (R6.REC.19, R6.REC.22) and need not be reachable from `main`; a failed fetch fails the\n"
    "  run, and TR5 stays NOT RUN;\n"
    "- (b) designation identity verification: the owner's recorded designation, quoted with author and time\n"
    "  in the record that relies on it (AGENTS.md sec. A.42 item 7), names a full commit id equal to the\n"
    "  check-run's `head_sha` and to the `F` of TR5's snapshot; the reviewer of that record compares the\n"
    "  three ids and records the comparison. The tool neither reads nor checks the designation (R6.STAT.4,\n"
    "  R6.REC.23): this is a comparison of identifiers, not a check of authorization;\n"
    "- (c) durable evidence verification when the round lands: once the round's landing is on `main`, the\n"
    "  designated `F` is an ancestor of the certified head (sec. A.39's `E`, `C` here, R6.NOTE.1) and is\n"
    "  reachable from `main`; TR5's recipe (the pinned workflow at `T`, the inputs `F` and the configuration\n"
    "  path) and its expected result then qualify under AGENTS.md sec. A.42 items 1 and 7, with the round's\n"
    "  receipt recording the check-run attestation (sec. A.39). Run ids and host records are provenance\n"
    "  (sec. A.42 item 2), and the host attestations stay residual trust (R6.REC.25).\n"
    "G-A1 needs an admitted configuration and native delegated runs in clones at `X` and `C`. Gates: plan\n"
    "freeze `F` (TR5 (a) and (b)); the round's landing (TR5 (c)); the A1 retirement execution (G-A1).\n"
    "Discharged by: each control run and PASS under its release condition, the identity comparison\n"
    "recorded, and the round landed with its receipt holding. The dispatches of (a) are launches that need\n"
    "the owner's approval (AGENTS.md sec. A.40, sec. A.50 item 5); r6 authorizes none.\n"
    "Sources: RD-25, OD-1, OC-1.",
    'TR5 needs a plan commit `F` on `main`')
trace_row('OC-1', 'OBL-16',
    "| OBL-16 | plan freeze `F` (TR5 (a), (b)); the round's landing (TR5 (c)); the A1 retirement execution (G-A1) | "
    "TR5 (a): 1, the exact-candidate validation of the candidate `F` before its designation; (b): the recorded "
    "designation compared with the candidate's full id (governance, by the record's reviewer); (c): 2 once the "
    "round's landing is on `main`; G-A1: 4 | no cycle: no evidence needs `F` on `main` before its designation "
    "(AGENTS.md sec. A.39) |")
in_block_edit('OC-1', 'R6.EVID.7',
    "It is evidence for the landing decision and is provenance (AGENTS.md\n   sec. A.42 item 2) until the candidate commit is reachable from `main`;",
    "It is evidence for the landing decision and is provenance (AGENTS.md\n   sec. A.42 item 2) until the candidate commit is reachable from `main`. For a native round's freeze,\n"
    "   the exact-candidate validation of the candidate `F` before its designation (AGENTS.md sec. A.39;\n"
    "   TR5) is evidence of this kind for the designation decision, and it qualifies as kind 2 when\n"
    "   the round's landing is on `main`;")
add_sources('OC-1', 'R6.EVID.7', ['OC-1'])
table_row_edit('OC-1', 'TR5', lambda s: s + '; `F` is the candidate named by `--freeze`, fetched by its full id and not required on `main`, and the run is dispatched on `main` at `T` (OBL-16 (a))')
r = RIDX['TR5']
r['not_run'] = collections.OrderedDict([
    ('reason', 'needs a candidate F whose PREREG.md Record pins list a reviewed configuration, and a host workflow_dispatch run of the pinned workflow on main naming that F (CI only)'),
    ('release_condition', 'a candidate F, held at exactly that commit for its exact-head check-run (AGENTS.md sec. A.39, sec. A.43 item 3), whose PREREG.md Record pins list a reviewed configuration, and the pinned workflow dispatched on main at T with --freeze that full commit id; F need not be on main'),
    ('release_check', 'the configuration path at the candidate F named by --freeze is listed in the last Record pins subsection of the PREREG.md beside it')])
log('OC-1', 'EXP:TR5', 'not_run reason, release condition and release check restated (no F on main)')
flags_replace('OC-1', 'TR5', lambda f: False, [
    'OC-1: TR5 is the exact-candidate validation of the plan freeze (OBL-16): (a) the sec. A.39 exact-head check-run on the candidate F and this chain run on main naming the same F, kind 1 before designation; (b) the designation identity comparison by the record\'s reviewer, not by the tool; (c) kind 2 when the round\'s landing is on main'])

# =====================================================================================
# OC-2: adoption distinguished from implementation certification; OBL-26; off-main trace
# =====================================================================================
STAT10 = (
    "**R6.STAT.10** Adoption and implementation certification (OC-2). r6's adoption and the certification of\n"
    "an implementation are separate steps.\n"
    "- Adoption is the owner's recorded decision on the specification. Its support is the r6 text (this\n"
    "  document, the expectation file, the requirement index, the migration index and the list of\n"
    "  paraphrased decisions) and its independent exact-head review, both on `main` no later than the\n"
    "  adoption record lands (AGENTS.md sec. A.42 items 1, 2 and 8). Precondition: the documents and the\n"
    "  review reach `main` by an ordinary merge that the owner approves (AGENTS.md sec. A.50 item 1); r6 does\n"
    "  not authorize it.\n"
    "- Adoption certifies no implementation. Each requirement and obligation of r6 holds or fails by its own\n"
    "  controls on the tool revision. None uses the tool commit a37992449b452021001277c06c524a30c92dfb87, its\n"
    "  conformance assessment or its CI runs as support; for the requirements and obligations these are\n"
    "  provenance (AGENTS.md sec. A.42 item 8).\n"
    "- Implementation certification is made against the tool revision after it lands on `main` (OBL-26), with\n"
    "  evidence of kinds 2 and 3 (R6.EVID.7); the tool's landing decision rests on kind 1 (sec. 32).\n"
    "- Every place where adoption, or an enduring claim stated in r6, still uses content that is not on\n"
    "  `main` as support is listed in the adoption trace of sec. 32. Each is an open governance conflict,\n"
    "  closed only by landing the content the claim needs or by narrowing the claim, never by an exception.\n"
    "OPEN: off-main support of adoption.\n"
    "Sources: OC-2. Controls: none (governance; verified by review and by the adoption trace of sec. 32).")
insert_after_block('OC-2', 'R6.STAT.9', STAT10)

replace_block('OC-2', 'OBL-26',
    "**OBL-26** Conformance certification of the tool revision. The read-only conformance checks of OD-4, OD-9,\n"
    "OD-23, OD-25, OD-27, RD-10, RD-18, RD-20, RD-27 and RD-33 are completed against the tool revision that\n"
    "implements r6, once it is on `main`; each difference becomes a verification defect or a residual owner\n"
    "decision. This is the implementation certification of the landed tool revision, separate from r6's\n"
    "adoption (R6.STAT.10). The conformance assessment recorded against the tool commit\n"
    "a37992449b452021001277c06c524a30c92dfb87 motivates obligations of sec. 32; for the requirements and\n"
    "obligations of r6 it is provenance (AGENTS.md sec. A.42 item 8). The statements of r6 that describe the\n"
    "tool commit use it, and are listed in the adoption trace below as off-`main` support. Gates: the\n"
    "implementation certification of the landed tool revision (OC-2 replaces the adoption gate that RE-37\n"
    "confirmed). Discharged by: the recorded checks and their dispositions against the tool revision on\n"
    "`main` (evidence kinds 2 and 3). Evidence: see the sec. 32 trace.\n"
    "Sources: OD-4, OD-27, RD-18, RD-20, OC-2.",
    'Conformance checks. The read-only conformance checks')
trace_row('OC-2', 'OBL-26',
    "| OBL-26 | the implementation certification of the landed tool revision | 2 and 3 (the checks recorded "
    "against the tool revision on `main`); the conformance assessment of a37992449b452021001277c06c524a30c92dfb87 "
    "is provenance for the requirements (AGENTS.md sec. A.42 item 8) | no cycle: r6's adoption does not rest on "
    "it (R6.STAT.10); the statements that describe the tool commit are in the adoption trace |")
edit('OC-2', 'sec. 32 intro',
     "The gated\nsteps are: the tool's landing (the tool revision that implements r6), the plan freeze `F`, the A1\nretirement execution, and r6's adoption.",
     "The gated\nsteps are: the tool's landing (the tool revision that implements r6), the plan freeze `F`, the A1\n"
     "retirement execution, r6's adoption, and the implementation certification of the landed tool revision\n(OBL-26, R6.STAT.10).")
edit('OC-2', 'sec. 32 intro',
     "(Q16; the gate assignments of OBL-13, OBL-14\nand OBL-26 are confirmed, RE-37)",
     "(Q16; the gate assignments of OBL-13 and OBL-14\nare confirmed, RE-37; OBL-26's gate is the implementation certification of the landed tool\nrevision, OC-2)")

ADOPT_TRACE = (
    "Adoption trace (OC-2; AGENTS.md sec. A.42 item 8). Each place where r6's adoption, or an enduring claim\n"
    "stated in r6, uses content that is not on `main`, with its classification. \"Support off `main`\" rows are\n"
    "open governance conflicts (R6.STAT.10); none is resolved by an exception:\n\n"
    "| Where | Content not on `main` | Use | Classification |\n"
    "|---|---|---|---|\n"
    "| R6.STAT.10 (the adoption record) | the r6 documents and their independent exact-head review | the adoption's support | support: must be on `main` no later than the adoption record lands; precondition, an ordinary merge the owner approves (AGENTS.md sec. A.50 item 1), not authorized by r6; open until then |\n"
    "| OBL-26; the runner cites of Table 17.1 and the expectation file's `runner` fields | the tool commit a37992449b452021001277c06c524a30c92dfb87 and its conformance assessment | locates the implementation and motivates obligations; no requirement rests on it | provenance for the requirements (the claim does not use the content); implementation certification is OBL-26, against the landed revision |\n"
    "| the expected figures of the expectation file (R6.EVID.4) | runs of the tool commit at `H`, `E` and `T1'` | preregistered expectations, not established values (R6.EVID.1, R6.EVID.7) | provenance for adoption; the enduring figures are those of R6.EVID.8 and OBL-23 |\n"
    "| statements of what the tool commit does (\"at the tool commit\", \"today\"): R6.PUR.12, R6.PIPE.3, R6.ANCH.10, R6.ANCH.12, R6.HP.7, R6.OUT.18, R6.OUT.24, R6.SPLIT.3, R6.RULE.11, R6.RULE.12, R6.REC.20, R6.HIT.2, R6.CLASS.1, R6.CLASS.11, R6.GATE.7, R6.CTRL.19, R6.CTRL.25, R6.CTRL.29, R6.TREE.13, R6.RDIR.7, R6.RECON.11, OBL-21, OBL-28; R6.EVID.6 (CI run 45569710442); R6.NOTE.3 (the content of `T1'`) | the tool commit, its conformance assessment, the CI run, `T1'` | each statement asserts a fact about that content | support off `main`: open; closed by landing the content each statement uses, or by narrowing it to the requirement and control it motivates |\n"
    "| semantics defined by reference to `P`'s `edits_check.py` (blob sha256 2856e58c...d98c): R6.SPLIT.3, R6.PROF.3, R6.PROF.4, R6.PROF.5, R6.PROF.7, R6.PROF.8, R6.PROF.9, R6.PROF.10, R6.PROF.12, R6.DENY.5, R6.A1CFG.2, OBL-1 | the plan commit `P` (its record directory is on no commit reachable from `main`) | the normative meaning of these requirements | support off `main`: open; closed by landing that blob on `main` no later than the adoption record, or by r6 stating the semantics itself; the copy frozen at `F` reaches `main` only with the round's landing, after adoption |\n"
    "| the external oracle of R6.GATE.7 and R6.GATE.8 (`P`'s outputs as files) | outputs of `P`'s checker | evidence for implementation certification, not for adoption | provenance for adoption; for certification, support off `main` until those outputs land |\n"
    "| owner decisions recorded only in paraphrase or relayed in session: the requirements of PARAPHRASED-DECISIONS.md, R6.STAT.8, and the owner corrections OC-1 to OC-5 of 2026-11-25 | GitHub comments and session instructions | the authority of the requirements that state them | support off `main` until quoted with author and time in a record on `main` (AGENTS.md sec. A.42 item 7): open |\n"
    "| inventory, review and decision labels in `Sources` (E-, V1-, V2-, A-, RD-, OD-, RE-, Q-, ME- and others) and the `source` fields citing v6.0e, r4 and r5 | the review and design records of the drafting | provenance: r6 states every rule itself (R6.STAT.2) and takes its authority from its own adoption | provenance |\n"
    "| item11-T1p (OBL-23) | `T1'` | an acceptance reference that needs `T1'`'s exact tree | support off `main`: named provenance gap, open |\n"
    "| controls outside OC-3's list that read `T1'` or `P`: RT-C, the `T1'` case of RT-DR, RT-M, RT-D-gr58, RT-L, S11-56, RT-O9's stand-in `F` (`P`'s record directory), and every `execution` control whose ledger and edit list are read at `P` | `T1'`, `P` | inputs of acceptance references | support off `main`: open; not re-specified by OC-3 (R6.EVID.8 states the representative candidate and the pinned ledger and edit list they could use) |\n")
a32 = T.index('## 32. Outstanding obligations')
b32 = T.index('**OBL-1** ', a32)
T = T[:b32] + ADOPT_TRACE + '\n' + T[b32:]
log('OC-2', 'sec. 32', 'adoption trace table added before OBL-1')

# =====================================================================================
# OC-3: representative candidate X_rep; RT-L2, RT-O9-L2, RT-T, the T1' figures
# =====================================================================================
EVID8 = (
    "**R6.EVID.8** Representative retirement candidate (OC-3). A control whose verdict reads only the trees\n"
    "that `H` and a ledger determine runs on a representative candidate `X_rep`, never on `T1'`:\n"
    "- Construction. `X_rep` is a commit object held by the tool's reader (as R6.TREE.15), with exactly one\n"
    "  parent, `H`, and a fixed subject. Each ledgered path carries `H`'s bytes with the ledger's splices\n"
    "  applied, and its sha256 equals the ledger's `expected_sha256` for the path; the plan's record-directory\n"
    "  paths carry the pinned ledger and edit list; each path of the configuration's delegated classes\n"
    "  carries a fixed marker blob that differs from its blobs at `H` and at the run's `M`; every other path\n"
    "  equals `H`. Its commit and tree ids are a function of `H`, the ledger, the edit list and the\n"
    "  configuration alone, and the result records them. The builder imports nothing from the tool's\n"
    "  engine; REP-BUILD checks it in both directions.\n"
    "- Inputs. `H` and `E`, both on `main`; the ledger and edit list as pinned control inputs landed with the\n"
    "  tool revision: byte copies of the retirement ledger (git blob ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e,\n"
    "  sha256 2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5) and edit list (git blob\n"
    "  ec384fdfbc12937b860e2f226355e8c5d94820a5, sha256\n"
    "  528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1); the controls use these pinned bytes,\n"
    "  and their origin in `P` is provenance. For RT-T, the ledger and edit list frozen at `F`. Further: the class, rule and scope records of the tool\n"
    "  revision; the configuration's control instance, a template landed with the tool revision whose pin of\n"
    "  the side-change class record is filled by the runner from the landed class record, so that the\n"
    "  template names no blob that the class record pins and K1-GRAPH's acyclicity is kept; and, for the\n"
    "  landing roles, a pinned `main` commit `M0`. No input is `T1'`, `P` or the tool commit\n"
    "  a37992449b452021001277c06c524a30c92dfb87.\n"
    "- Why the safeguard is full. A conforming candidate (R6.TREE.9: one parent, `H`; each ledgered file `H`\n"
    "  plus its splices; every other path `H`'s except delegated and record paths) carries, on every ledgered\n"
    "  and corpus path, exactly the bytes of `X_rep`. Op B reads only the corpus and the segments `E..H` and\n"
    "  `H..X` (R6.PUR.5), and a ledgered segment is checked by the ledger, not by a walk of `X`'s history; the\n"
    "  terminology scans of these controls read only ledgered and corpus paths; the drift and side-change\n"
    "  verdicts of op C read only `H..M`, the ledgered and corpus path sets, and the candidate's blobs on\n"
    "  drifted paths, which RC8 fixes to the ledger's `expected_sha256` (R6.TREE.7, R6.RECON.13,\n"
    "  R6.RECON.21). Each verdict is therefore the same at `X_rep`, at `T1'` where `T1'` conforms, and at the\n"
    "  candidate the A1 retirement executes under the same ledger. The only ancestry these controls read is\n"
    "  that `H` is the candidate's parent, which `X_rep` meets by construction with `H` on `main`. The marker\n"
    "  blobs make every delegated path changed by the candidate, a superset of what a conforming candidate\n"
    "  changes, so a path changed on both sides is never missed.\n"
    "- Scope guard. A control takes `X_rep` only where the paths its verdict reads lie in the ledgered and\n"
    "  corpus paths and in `H..M`. The runner records the paths its verdict read, and the invariant\n"
    "  `scanned_paths_within` fails the row otherwise. A control whose verdict reads the content of a\n"
    "  delegated or record path of a particular trial tree depends on that exact tree: it keeps `T1'` as\n"
    "  candidate evidence for the landing decision only, and its enduring claim stays a named provenance gap\n"
    "  (OBL-23: item11-T1p).\n"
    "- Expected values. The expected figures of these rows are those measured with the tool commit at `T1'`.\n"
    "  They are carried to `X_rep` because the paths the verdict reads are byte-identical when `T1'`\n"
    "  conforms; that comparison is recorded once as candidate evidence and supports no enduring claim. A\n"
    "  difference between a figure at `X_rep` and its expectation is investigated as a defect, never fitted\n"
    "  (R6.EVID.1). The `T1'` measurements stay in each row's `reference` as provenance.\n"
    "- Reconciliation record placement. A reconciliation record names the `M` of its run (R6.RECON.1), so it\n"
    "  cannot be among the paths of that `M`. For RT-L2 and RT-O9-L2 the reviewed record is therefore not a\n"
    "  landing path of the tool: for the landing decision the run names it from a commit outside the tool's\n"
    "  landing paths, and it reaches `main` in a commit after the tool's landing commit.\n"
    "- Evidence, per control:\n\n"
    "| Control | Candidate evidence for the landing decision | Reproducible evidence for the enduring claim |\n"
    "|---|---|---|\n"
    "| RT-L2 | kind 1: on the exact candidate commit of the tool's pull request, at `X` = `C` = `X_rep`, with the predicted `M` = `M0` plus the candidate's landing paths and the reviewed record named from outside those paths | kind 2 once the landing merge and the reviewed record are on `main`; kind 3 re-run with `M` the `main` that holds the tool and a record bound to it |\n"
    "| RT-O9-L2 | as RT-L2, on the predicted `M` plus the record directory of a representative stand-in `F` that holds the pinned ledger, edit list and configuration instance | as RT-L2 |\n"
    "| RT-T | kind 1: on the candidate `F` before its designation, at `X_rep` built from `F`'s ledger, with `F`'s records (OBL-16 (a)); kind 4: at the executed candidate | kind 2 once the round's landing is on `main` |\n"
    "| RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W, N10, N11 | kind 1: on the exact tool candidate at `X_rep`; the `T1'` measurement stays in `reference` as provenance | kind 2 once the landing merge is on `main`; kind 3 re-run on `main` |\n"
    "| REP-BUILD | kind 1: on the exact tool candidate | kind 2 and kind 3 |\n\n"
    "item11-T1p is not among them (OBL-23).\n"
    "Sources: OC-3, RD-23, RE-36. Controls: REP-BUILD, RT-L2, RT-O9-L2, RT-T, RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W,\n"
    "N10, N11.")
insert_after_block('OC-3', 'R6.EVID.7', EVID8)

in_block_edit('OC-3', 'R6.NOTE.3',
    "historical measurement unless a control whose inputs are on `main` reproduces it (sec. 31).",
    "historical measurement unless a control whose inputs are on `main` reproduces it (sec. 31). `X_rep` is\n"
    "the representative retirement candidate of R6.EVID.8, built from `H` and a ledger; it is the input of\n"
    "every control whose verdict reads only what `H` and the ledger determine.")
add_sources('OC-3', 'R6.NOTE.3', ['OC-3'])

# OBL-13
replace_block('OC-3', 'OBL-13',
    "**OBL-13** RT-L2 release. At `main`, `AGENTS.md` is `base-drift` and `.claude/settings.json` is an\n"
    "unclassified side change. RT-L2 is NOT RUN until a reviewed reconciliation record for `AGENTS.md`,\n"
    "bound to the exact `H`, `M` and `C` blobs of the run and passing record lint, and side-change class\n"
    "records for the unclassified paths exist; it is then three-valued (sec. 23). RT-L2 runs at `X` = `C` =\n"
    "`X_rep` (R6.EVID.8): its verdict reads `H..M`, the ledgered and corpus path sets and the candidate's\n"
    "blobs on drifted paths, none of which depends on the identity or ancestry of `T1'`. The reviewed record\n"
    "names the predicted `M` and so is not among its paths: the run names it from a commit outside the\n"
    "tool's landing paths, and it reaches `main` in a commit after the tool's landing commit. Gates: the\n"
    "tool's landing. Discharged by: RT-L2 run and PASS (no drift, or validly reconciled).\n"
    "Evidence: for the landing decision, kind 1 (RT-L2 on the exact candidate commit of the tool's pull\n"
    "request); for the enduring claim, kind 2 once the landing merge and the reviewed record are on\n"
    "`main`, and kind 3 re-run against `main`, every input reachable from `main` (sec. 32 trace; RE-37\n"
    "confirms the gate). The RT-L2 PASS of CI run 45569710442 (tool commit\n"
    "a37992449b452021001277c06c524a30c92dfb87, `X` = `T1'`, drafted record) stays provenance (R6.EVID.6).\n"
    "Sources: E-1363, OD-18, Q2, MC-4, OC-3.",
    'RT-L2 release. At `main`')
trace_row('OC-3', 'OBL-13',
    "| OBL-13 | the tool's landing | landing decision: 1 (RT-L2 on the exact candidate commit of the tool's pull "
    "request, at `X` = `C` = `X_rep`, the predicted `M` = a pinned `main` commit `M0` plus the candidate's landing "
    "paths, the reviewed record named from outside those paths); enduring claim: 2 once the landing merge and the "
    "reviewed record (in a later commit) are on `main`, and 3 re-run against `main` | no cycle; no input is `T1'`, "
    "`P` or the tool commit a3799244 (R6.EVID.8) |")
# OBL-14
replace_block('OC-3', 'OBL-14',
    "**OBL-14** RT-O9's dependent clause. RT-O9's own record-directory checks run and are gated. Only its\n"
    "clauses that RT-L2 still holds and that no `base-drift` occurs on the predicted `M` are an outstanding\n"
    "dependent assertion, RT-O9-L2, NOT RUN while RT-L2 is NOT RUN (RE-5 (a)). RT-O9-L2 runs at `X_rep`, on\n"
    "the predicted `M` plus the record directory of a representative stand-in `F` that holds the pinned\n"
    "ledger, edit list and configuration instance (R6.EVID.8): `base-drift` is decided by whether a side\n"
    "change touches a ledgered or corpus path (R6.TREE.7), and a record directory holds none (DIR3), so the\n"
    "clause does not depend on the content of `P`'s record directory.\n"
    "Gates: the tool's landing. Discharged by: RT-L2's release and PASS (OBL-13).\n"
    "Evidence: as OBL-13 (RE-37 confirms the gate).\n"
    "Sources: RD-6, Q6, MC-4, OC-3.",
    "RT-O9's dependent clause.")
trace_row('OC-3', 'OBL-14',
    "| OBL-14 | the tool's landing | as OBL-13, on the predicted `M` plus the record directory of a representative "
    "stand-in `F` (R6.EVID.8) | as OBL-13 |")
# OBL-15
replace_block('OC-3', 'OBL-15',
    "**OBL-15** Reviewed records for RT-T. RT-T is NOT RUN until every reviewed record of sec. 14's review\n"
    "load exists at `F` and verifies: HP adjudications for the 113 `E..H` site changes, context\n"
    "adjudications for the meaning-context sites, structure reviews, and hit classification records for the\n"
    "replacement-region and unheld hit lines (including `papers/GR.md:58`). RT-T runs at `X_rep` built from\n"
    "`F`'s ledger (R6.EVID.8): op B reads only the corpus and the segments `E..H` and `H..X` (R6.PUR.5),\n"
    "whose bytes `H` and `F`'s ledger fix for every conforming candidate. Gates: plan freeze `F`; the A1\n"
    "retirement execution. Discharged by: RT-T run and PASS with every record: before the designation of\n"
    "`F`, on the candidate `F` within its exact-candidate validation (kind 1, OBL-16 (a)); in the\n"
    "retirement execution, at the executed candidate (kind 4); both qualify as kind 2 once the round's\n"
    "landing is on `main`.\n"
    "Pending owner confirmation (see PARAPHRASED-DECISIONS.md).\n"
    "Sources: E-1062, E-1063,\n"
    "RD-9, OD-20, OC-3.",
    'Reviewed records for RT-T.')
trace_row('OC-3', 'OBL-15',
    "| OBL-15 | plan freeze `F`; the A1 retirement execution | records at `F` (4); RT-T: 1 on the candidate `F` "
    "before its designation, at `X_rep` built from `F`'s ledger, within the exact-candidate validation (OBL-16 (a)); "
    "4 at the executed candidate; 2 once the round's landing is on `main` | no cycle |")
trace_row('OC-3', 'OBL-7',
    "| OBL-7 | plan freeze `F`; RT-T's release | 4 | no cycle; RT-T runs at `X_rep` (OBL-15, R6.EVID.8) |")
# OBL-23
replace_block('OC-3', 'OBL-23',
    "**OBL-23** `T1'`-input evidence. The figures of R6.EVID.4 whose controls ran on `T1'` (N10, N11, RT-D,\n"
    "RT-I7 at `T1'`, RT-I7A at `T1'`, RT-DR3W at `T1'`, RT-T0, item11-T1p) were measured with the tool commit\n"
    "at `T1'`; those measurements are historical and are kept in the rows' `reference`.\n"
    "- N10, N11, RT-D, RT-I7, RT-I7A, RT-DR3W and RT-T0 read only paths that `H` and the ledger determine,\n"
    "  and run at `X_rep` (R6.EVID.8); their figures are acceptance references through those runs once\n"
    "  every input is reachable from `main` (kinds 2 and 3).\n"
    "- item11-T1p's `repo` scan reads the content of `T1'`'s delegated and record paths (two of its 176\n"
    "  lines lie in generated artifacts, R6.EVID.5), which neither `H` nor the ledger determines: the figure\n"
    "  depends on the exact trial tree. Its run on the exact tool candidate with `X` = `T1'` is candidate\n"
    "  evidence for the landing decision only; its enduring claim is a named provenance gap (AGENTS.md\n"
    "  sec. A.42 item 8, support off `main`) while the objects of `T1'` it needs are not reachable from\n"
    "  `main`. Whether a kind-1-only figure suffices for the landing gate is an owner question.\n"
    "Gates: their use as acceptance references for the tool's landing. Discharged by: the `X_rep` runs of\n"
    "R6.EVID.8 recorded; for item11-T1p, the objects of `T1'` it needs reachable from `main`, or the owner's\n"
    "decision on a kind-1-only figure; otherwise the figure stays a historical measurement.\n"
    "The list is confirmed with RT-D and the `T1'` cases of RT-I7A and RT-DR3W (RE-36 (a)); no figure is an\n"
    "acceptance reference reproduced on `main` until the tool revision lands and the run is repeated\n"
    "there (R6.EVID.7).\n"
    "OPEN: T1'-bound evidence cannot qualify.\n"
    "Sources: RD-23, ME-3, Q10, OC-3.",
    '`T1\'`-input evidence.')
trace_row('OC-3', 'OBL-23',
    "| OBL-23 | the use of the R6.EVID.4 figures as acceptance references for the tool's landing | N10, N11, RT-D, "
    "RT-I7, RT-I7A, RT-DR3W, RT-T0: 1 at `X_rep` on the exact tool candidate for the landing decision; 2 and 3 for "
    "the enduring claim (R6.EVID.8); item11-T1p: 1 at `T1'` on the exact tool candidate, for the landing decision "
    "only | no cycle; item11-T1p's enduring claim is a named provenance gap while `T1'` is not reachable from "
    "`main` (open); whether a kind-1-only figure suffices for the landing gate is an owner question |")

# R6.EVID.4
in_block_edit('OC-3', 'R6.EVID.4',
    "Figures whose control runs on `T1'` are acceptance\nreferences only while the objects of `T1'` the control needs are reachable from `main`; otherwise they\nare historical measurements (OBL-23).",
    "Figures whose control runs on `X_rep` are acceptance\nreferences through runs whose inputs are all reachable from `main` (R6.EVID.8). The figure whose\n"
    "control needs `T1'` itself (item11-T1p) is an acceptance reference only while the objects of `T1'` it\n"
    "needs are reachable from `main`, and otherwise a historical measurement (OBL-23).")
for old, new in (
        ("| 9 merger groups covering 22 sites | RT-T0 | `H`, `T1'` |", "| 9 merger groups covering 22 sites | RT-T0 | `H`, `X_rep` |"),
        ("with splice D029 | RT-T0 | `T1'` |", "with splice D029 | RT-T0 | `X_rep` |"),
        ("168 sites moved by `H..T1'` splices | RT-T0 | `T1'` |", "168 sites moved by `H..X_rep` splices | RT-T0 | `X_rep` |"),
        ("3 RET `context-structure-changed` | RT-T0 | `T1'` |", "3 RET `context-structure-changed` | RT-T0 | `X_rep` |"),
        ("11 W1/W2 lines PASS | RT-D | `T1'` |", "11 W1/W2 lines PASS | RT-D | `X_rep` |"),
        ("| literal item-7 greps at `T1'`: \"six structural\" 7, \"Fourteen\" 0, \"sixth of\" 0, `\\bA1\\b` 4 | RT-I7 | `T1'` |",
         "| literal item-7 greps at `X_rep`: \"six structural\" 7, \"Fourteen\" 0, \"sixth of\" 0, `\\bA1\\b` 4 | RT-I7 | `X_rep` |"),
        ("one sentence at `H` (lines 37-39), none at `T1'` | RT-DR3W | control inputs |",
         "one sentence at `H` (lines 37-39), none in `X_rep` | RT-DR3W | control inputs |"),
        ("at `T1'` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `T1'` |",
         "at `X_rep` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `X_rep` |")):
    in_block_edit('OC-3', 'R6.EVID.4', old, new)
add_sources('OC-3', 'R6.EVID.4', ['OC-3'])

in_block_edit('OC-3', 'R6.CTRL.19',
    "A figure measured on T1' is an acceptance reference only for a run that has\nT1' among its inputs; its standing as evidence follows sec. 31.",
    "A control whose verdict reads only what `H` and the ledger determine runs on\n`X_rep` (R6.EVID.8); a figure that needs T1' itself is an acceptance reference only for a run that has\nT1' among its inputs; its standing as evidence follows sec. 31.")
add_sources('OC-3', 'R6.CTRL.19', ['OC-3'])
in_block_edit('OC-3', 'R6.CTRL.7',
    "which RT-DR3W scans at `H` and,\nas its countercontrol, at T1'.",
    "which RT-DR3W scans at `H` and,\nas its countercontrol, in `X_rep` (R6.EVID.8), whose `AGENTS.md` is `H`'s with the ledger's splices\napplied.")
add_sources('OC-3', 'R6.CTRL.7', ['OC-3'])
in_block_edit('OC-3', 'R6.PLAN.8',
    "Item 7 as frozen does not pass at T1': seven lines contain the legitimate count of the\nbijection's properties (W1); the T1' counts are historical measurements.",
    "Item 7 as frozen does not pass at T1' or at `X_rep`: seven lines contain the legitimate count of\nthe bijection's properties (W1); RT-I7 asserts the counts at `X_rep` (R6.EVID.8), and the measurement\nat T1' is historical.")
in_block_edit('OC-3', 'R6.PLAN.8',
    "RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at T1' as a test of the\nmechanism.",
    "RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at `X_rep` as a test of the\nmechanism.")
add_sources('OC-3', 'R6.PLAN.8', ['OC-3'])
in_block_edit('OC-3', 'R6.RECON.21',
    "Before the tool lands, RT-L2 runs `execution` against a predicted\n`M` that contains the tool's landing paths, with an in-memory landing (R6.TREE.15).",
    "Before the tool lands, RT-L2 runs `execution` against a predicted\n`M` that contains the tool's landing paths, with an in-memory landing (R6.TREE.15), at `X` = `C` =\n"
    "`X_rep` (R6.EVID.8). The reviewed reconciliation record names that `M` and so is not among its paths:\n"
    "the run names it from a commit outside the tool's landing paths, and it reaches `main` in a commit\nafter the tool's landing commit.")
add_sources('OC-3', 'R6.RECON.21', ['OC-3'])

# OBL-28: implementation obligation of OC-3
in_block_edit('OC-3', 'OBL-28',
    "| RE-29 | R6.RECON.14 | a purpose check that the stricter RC9 rejects no valid record | review; N6 |",
    "| RE-29 | R6.RECON.14 | a purpose check that the stricter RC9 rejects no valid record | review; N6 |\n"
    "| OC-3 | R6.EVID.8 | the representative candidate builder, the pinned ledger and edit list and the configuration's control instance land with the tool revision; the rows of R6.EVID.8 run on `X_rep` and record the paths their verdict read | REP-BUILD; `scanned_paths_within` on each row |")
add_sources('OC-3', 'OBL-28', ['OC-3', 'OC-4'])

# Table 17.1 case cells
table_row_edit('OC-3', 'RT-L2', lambda s: "before the tool lands: as RT-L, at `X` = `C` = `X_rep` (R6.EVID.8), with `--main` set to the predicted `M` (a pinned `main` commit `M0` plus the tool's landing paths, R6.RECON.21) and the reviewed reconciliation record named from a commit outside those paths")
table_row_edit('OC-3', 'RT-O9-L2', lambda s: "the dependent clause of RT-O9: RT-L2 on the same predicted `M` plus the record directory of a representative stand-in `F` (the pinned ledger, edit list and configuration instance), at `X_rep` (R6.EVID.8)")
table_row_edit('OC-3', 'RT-T', lambda s: s + ', at `X_rep` built from `F`\'s ledger (R6.EVID.8)')
table_row_edit('OC-3', 'RT-T0', sub1("`coverage` at `X = T1'`, no records", "`coverage` at `X = X_rep` (R6.EVID.8), no records; the `T1'` measurement in `reference`"))
table_row_edit('OC-3', 'RT-D', sub1("`terms --commit T1' --base H --ledger F:ledger.json`", "`terms --commit X_rep --base H --ledger F:ledger.json`, the ledger the pinned control input (R6.EVID.8)"))
table_row_edit('OC-3', 'RT-DR3W', sub1("countercontrol: `AGENTS.md` at T1' (sha256 59b68984...)", "countercontrol: `AGENTS.md` in `X_rep` (`H`'s with the ledger's splices; sha256 59b68984..., the bytes of `T1'`'s copy)"))
table_row_edit('OC-3', 'RT-I7', sub1("`terms --commit T1' --profile item7-literal`", "`terms --commit X_rep --profile item7-literal` (R6.EVID.8)"))
table_row_edit('OC-3', 'RT-I7A', sub1("at H and at T1', no records", "at H and at `X_rep` (R6.EVID.8), no records"))
table_row_edit('OC-3', 'item11-T1p', lambda s: s + "; candidate evidence for the landing decision only (exact trial tree, OBL-23)")
table_row_edit('OC-3', 'N10', sub1("`X` = T1' (14ac71b4)", "`X` = `X_rep` (R6.EVID.8; its `AGENTS.md` is the blob of `T1'`'s copy)"))

# --- expectation rows
for cid in ('RT-T0', 'RT-D', 'N10', 'N11'):
    add_inv(RIDX[cid]['expect'], [{'representative_candidate': XREP},
                                  {'scanned_paths_within': SCAN_EXEC if cid in ('N10', 'N11') else (SCAN_CORPUS if cid == 'RT-T0' else SCAN_TERMS)}])
    log('OC-3', 'EXP:' + cid, 'invariants representative_candidate and scanned_paths_within added')
    set_ref('OC-3', cid, REF_T1P)
    flags_replace('OC-3', cid, OFFMAIN, [OC3_FLAG])
str_sub('OC-3', 'RT-T0', ['direction', 'why'], 'RT-T is the same coverage run at X = T1\' with every reviewed record',
        'RT-T is the same coverage run at X = X_rep with every reviewed record')
for cid, label_old, label_new, scan in (
        ('RT-I7', "at T1'", "at X_rep (R6.EVID.8)", SCAN_TERMS),
        ('RT-I7A', "at T1'", "at X_rep (R6.EVID.8)", SCAN_TERMS),
        ('RT-DR3W', "AGENTS.md at T1' (agents-md-at-T1p)",
         "AGENTS.md in X_rep (control input agents-md-at-Xrep: H's AGENTS.md with the ledger's splices, sha256 59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2, the bytes of T1''s copy)",
         'AGENTS.md (a ledgered path) of X_rep')):
    cs = [c for c in RIDX[cid]['expect']['cases'] if c['case'] == label_old]
    if len(cs) != 1:
        PROBLEMS.append('case %s/%s' % (cid, label_old))
        continue
    cs[0]['case'] = label_new
    add_inv(cs[0], [{'representative_candidate': XREP}, {'scanned_paths_within': scan}])
    log('OC-3', 'EXP:' + cid, 'case relabelled to X_rep; invariants representative_candidate and scanned_paths_within added')
    set_ref('OC-3', cid, collections.OrderedDict([("measured_at_T1p_14ac71b4_with_tool_commit_a3799244",
            "the expected figures of the X_rep case were measured at T1'; historical measurement and provenance (AGENTS.md sec. A.42 item 2); carried to X_rep as expectations, not as support (R6.EVID.8)")]))
    flags_replace('OC-3', cid, OFFMAIN, [OC3_FLAG])
str_sub('OC-3', 'RT-I7', ['direction', 'why'], 'on the unmodified trees T1\' and H', 'on the unmodified tree H and on X_rep')
str_sub('OC-3', 'RT-I7A', ['direction', 'why'], 'on the unmodified trees H and T1\'', 'on the unmodified tree H and on X_rep')
str_sub('OC-3', 'RT-DR3W', ['direction', 'why'], "(AGENTS.md at H and at T1')", "(AGENTS.md at H and in X_rep)")
str_sub('OC-3', 'RT-DR3W', ['direction', 'why'], "(one at H, none at T1')", "(one at H, none in X_rep)")

for cid in ('RT-L2', 'RT-O9-L2'):
    add_inv(RIDX[cid]['expect'], [{'representative_candidate': XREP}, {'scanned_paths_within': SCAN_EXEC}])
    RIDX[cid]['not_run']['release_condition'] = ('reviewed reconciliation record bound to exact H, M and C = X_rep covering every drifted path, '
                                                 'named by the run from a commit outside the tool\'s landing paths (it names the predicted M and cannot be among its paths)')
    RIDX[cid]['not_run']['release_check'] = ('a reconciliation record named by the run from a commit outside the tool\'s landing paths, whose review record passes '
                                             'record lint and whose H, M and C blob ids equal the predicted run roles')
    log('OC-3', 'EXP:' + cid, 'invariants added; release condition and release check restated (record outside the landing paths)')
    flags_replace('OC-3', cid, lambda f: False, [
        'OC-3: runs at X = C = X_rep (R6.EVID.8); its verdict reads H..M, the ledgered and corpus path sets and the candidate blobs on drifted paths, not T1''s identity or ancestry; landing decision: kind 1 on the exact tool candidate with the predicted M = M0 plus the candidate\'s landing paths; enduring claim: kind 2 once the landing merge and the reviewed record (landed after the tool\'s landing commit) are on main, kind 3 re-run on main'])
RIDX['RT-L2']['procedure']['evidence'] = RIDX['RT-L2']['procedure']['evidence'] + ['X_rep commit id and tree listing, and the pinned main commit M0']
log('OC-3', 'EXP:RT-L2', 'procedure evidence: X_rep and M0 added')

add_inv(RIDX['RT-T']['expect'], [{'representative_candidate': XREP.replace('the ledger\'s splices', 'the splices of the ledger frozen at F')},
                                 {'scanned_paths_within': SCAN_CORPUS}])
RIDX['RT-T']['not_run']['release_condition'] = 'every reviewed record of sec. 8.2 present at F and verifying under sec. 6.3, run at X_rep built from F\'s ledger (R6.EVID.8)'
str_sub('OC-3', 'RT-T', ['direction', 'why'], 'RT-T0 is the same coverage run at X = T1\' without the reviewed records',
        'RT-T0 is the same coverage run at X = X_rep without the reviewed records')
flags_replace('OC-3', 'RT-T', lambda f: False, [
    'OC-3: runs at X_rep built from F\'s ledger (R6.EVID.8); plan freeze: kind 1 on the candidate F before its designation, within its exact-candidate validation (OBL-16 (a)); retirement execution: kind 4 at the executed candidate; both kind 2 once the round\'s landing is on main'])
log('OC-3', 'EXP:RT-T', 'invariants added; release condition at X_rep')

flags_replace('OC-3', 'item11-T1p', lambda f: False, [
    'OC-3: the repo scan reads the content of T1\'\'s delegated and record paths (two of the 176 lines lie in generated artifacts), which H and the ledger do not determine: the exact trial tree is material; the run on the exact tool candidate with X = T1\' is candidate evidence for the landing decision only; the enduring claim is a named provenance gap (OBL-23)'])

REP = collections.OrderedDict([
    ('id', 'REP-BUILD'), ('requirements', ['R6.EVID.8']), ('runner', None), ('operations', []),
    ('direction', collections.OrderedDict([('of', 'both'), ('scope', 'outside'),
                                           ('why', 'OC-3: an r6 control whose governing source (R6.EVID.8) is outside v6.0e sec. 10; its positive and adversarial cases are recorded in the row')])),
    ('predicate_kind', 'declarative'),
    ('expect', collections.OrderedDict([('cases', [
        collections.OrderedDict([('case', 'build X_rep from H, the pinned ledger and edit list, and the configuration\'s control instance'),
                                 ('outcome', 'HASH_EQUAL'),
                                 ('invariants', [{'representative_candidate': XREP},
                                                 {'equal_across': 'two builds: commit id and tree id'},
                                                 {'imported_files_within': 'the builder and the standard library; no module under tools/ledger_coverage/engine/'}])]),
        collections.OrderedDict([('case', 'the pinned ledger with one splice\'s new bytes changed by one byte'),
                                 ('outcome', 'REFUSED'),
                                 ('invariants', [{'reason': 'a ledgered path\'s sha256 differs from the ledger\'s expected_sha256'}])]),
        collections.OrderedDict([('case', 'a builder that imports a module under tools/ledger_coverage/engine/'),
                                 ('outcome', 'REFUSED'),
                                 ('invariants', [{'reason': 'the builder imports from the engine under test'}])])])])),
    ('source', 'r6 R6.EVID.8 (OC-3)'),
    ('flags', ['to implement (named obligation, OBL-28 row OC-3)'])])
di = [i for i, x in enumerate(rows) if x['id'] == 'DELEG-REGEN'][0]
rows.insert(di + 1, REP)
RIDX = collections.OrderedDict((x['id'], x) for x in rows)
log('OC-3', 'EXP:REP-BUILD', 'row added')
a17 = T.index('**Table 17.1. Control catalogue**')
b17 = T.index('**Table 17.2. Record-directory mutants**')
seg = T[a17:b17]
li = seg.index('| DELEG-REGEN |')
le = seg.index('\n', li)
seg = seg[:le] + ('\n| REP-BUILD | R6.EVID.8 | to be implemented (tool revision) | decl | both | the representative '
                  'candidate `X_rep` built from `H`, the pinned ledger and edit list and the configuration\'s control '
                  'instance, twice with equal ids; a ledger with one splice changed by one byte; a builder importing '
                  'the engine (R6.EVID.8) |') + seg[le:]
T = T[:a17] + seg + T[b17:]
log('OC-3', 'Table 17.1', 'row REP-BUILD added')

# =====================================================================================
# OC-4: LC-7 stays REVIEW_REQUIRED pending a specified, reviewed regeneration verification procedure
# =====================================================================================
in_block_edit('OC-4', 'R6.TREE.12',
    "a reconciliation record is not an\n    alternative to regeneration;",
    "a reconciliation record is not an\n    alternative to regeneration. The regeneration is verified by a procedure, to be specified explicitly\n"
    "    and reviewed independently, in which the trusted checker establishes the expected output itself and\n"
    "    compares bytes; the evaluated tree's claim of regeneration is never sufficient. Until that procedure\n"
    "    is specified and reviewed, the path is REVIEW_REQUIRED for every candidate `L` (LC-7);")
add_sources('OC-4', 'R6.TREE.12', ['OC-4'])
in_block_edit('OC-4', 'OBL-28',
    "| RE-18 | R6.TREE.12 | a regeneration check of derived artifacts at `L` (a delegation class); REVIEW_REQUIRED until it passes | LC-7 (its expected landing blob is open) |",
    "| RE-18 | R6.TREE.12 | a regeneration verification procedure for derived artifacts at `L` (a delegation class), specified explicitly and reviewed independently, in which the trusted checker establishes the expected output itself and compares bytes; the evaluated tree's claim of regeneration is never sufficient; REVIEW_REQUIRED until the procedure is specified, reviewed and passes (OC-4, open) | LC-7 (REVIEW_REQUIRED for every candidate `L`; its expected landing blob is open) |")
table_row_edit('OC-4', 'LC-7', sub1("REVIEW_REQUIRED for every candidate `L` (expected landing blob open, RE-18)",
                                    "REVIEW_REQUIRED for every candidate `L` until a regeneration verification procedure is specified and independently reviewed (expected landing blob open, RE-18, OC-4)"))
flags_replace('OC-4', 'LC-7', lambda f: f.startswith('OPEN: derived-artifact landing blob'), [
    'OPEN: derived-artifact landing blob: REVIEW_REQUIRED for every candidate L (RE-18 (b), fail-closed) until a regeneration verification procedure is specified explicitly and reviewed independently, in which the trusted checker establishes the expected output itself and compares bytes; the evaluated tree\'s claim of regeneration is never sufficient (OC-4); not resolved'])

# =====================================================================================
# meta: two-way links, Table 17.1 requirements column, annex, machine outputs
# =====================================================================================
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


REQS = parse_reqs(T)
REQ_ORDER = list(REQS)
named_by = collections.defaultdict(list)
for rid, q in REQS.items():
    for c in q['controls']:
        named_by[c].append(rid)
for r in rows:
    nb = named_by.get(r['id'], [])
    if not nb and r.get('composed_of'):
        sets = [set(named_by.get(c, [])) for c in r['composed_of']]
        nb = sorted(set.intersection(*sets), key=REQ_ORDER.index) if sets else []
    if nb != r['requirements']:
        log('meta', 'EXP:' + r['id'], 'requirements re-keyed to the requirements that name the row')
    r['requirements'] = nb
DIRS = {'adversarial': 'adv', 'positive': 'pos', 'both': 'both'}
a17 = T.index('**Table 17.1. Control catalogue**')
b17 = T.index('**Table 17.2. Record-directory mutants**')
lines = T[a17:b17].split('\n')
TABLE_IDS = []
for k, line in enumerate(lines):
    if line.startswith('| ') and not line.startswith('| Id ') and not line.startswith('|---'):
        cells = line[2:-2].split(' | ')
        if len(cells) > 6:
            cells = cells[:5] + [' | '.join(cells[5:])]
        cid = cells[0]
        TABLE_IDS.append(cid)
        if cid in RIDX:
            rq = RIDX[cid]['requirements']
            cell = ', '.join(rq) if rq else '(none)'
            if cells[1] != cell:
                log('meta', 'Table 17.1:' + cid, 'Requirements column regenerated')
            cells[1] = cell
            lines[k] = '| ' + ' | '.join(cells) + ' |'
        else:
            PROBLEMS.append('Table 17.1 row without an expectation row: ' + cid)
T = T[:a17] + '\n'.join(lines) + T[b17:]

inv_keys = set()


def _iwalk(e):
    if isinstance(e, dict):
        for i in e.get('invariants', []):
            inv_keys.update(i.keys())
        for c in e.get('cases', []):
            _iwalk(c)
    elif isinstance(e, list):
        for x in e:
            _iwalk(x)


for r in rows:
    _iwalk(r['expect'])
    _iwalk(r.get('restored'))
    for c in r.get('candidate_expectations', []):
        _iwalk(c['expect'])
inv_sorted = sorted(inv_keys)
ai = T.index('The closed vocabulary of `invariants` keys is the following list of the ')
bi = T.index('`writes_only_under`.', ai) + len('`writes_only_under`.')
annex = ('The closed vocabulary of `invariants` keys is the following list of the %d keys the\nexpectation file uses (R6.GATE.3). A key outside it makes the file invalid.\n\n' % len(inv_sorted)
         + '\n'.join(', '.join('`%s`' % k for k in inv_sorted[j:j + 6]) + (',' if j + 6 < len(inv_sorted) else '.')
                     for j in range(0, len(inv_sorted), 6)))
T = T[:ai] + annex + T[bi:]
log('meta', 'annex 16.10', 'invariant vocabulary regenerated (%d keys)' % len(inv_sorted))
REQS = parse_reqs(T)

# REQUIREMENTS.json: recomputed by final.py's rule; first prove the rule reproduces the input index
KIND = {q['id']: q for q in REQ_IN}
NEW_KIND = {'R6.STAT.10': ('STAT', 0, 'governance'), 'R6.EVID.8': ('EVID', 31, 'testable')}


def req_index(reqs):
    out = []
    for rid, q in reqs.items():
        if rid in KIND:
            sec, num, kind = KIND[rid]['section'], KIND[rid]['section_number'], KIND[rid]['kind']
            pend = KIND[rid]['pending_owner_confirmation']
        elif rid in NEW_KIND:
            (sec, num, kind), pend = NEW_KIND[rid], []
        else:
            PROBLEMS.append('requirement without kind: ' + rid)
            continue
        if kind == 'testable':
            ver = ['controls']
        elif rid.startswith('OBL-'):
            ver = [rid]
        else:
            obls = []
            for o in re.findall(r'\bOBL-\d+\b', q['text']):
                if o not in obls:
                    obls.append(o)
            ver = obls or ['review']
        out.append(collections.OrderedDict([('id', rid), ('section', sec), ('section_number', num), ('kind', kind),
                                            ('sources', q['sources']), ('controls', q['controls']), ('verification', ver),
                                            ('open', q['open']), ('pending_owner_confirmation', pend)]))
    return out


REPLAY_OK = dumps(req_index(parse_reqs(T_IN))) == REQ_TXT
REQ_OUT = req_index(REQS)

EXP_OUT = collections.OrderedDict([('schema', EXP['schema']), ('record_id', 'r6-final2-1'),
                                   ('rows', [order_row(r) for r in rows]), ('retired', EXP['retired'])])
log('meta', 'EXPECTATIONS.json', 'record_id r6-final-1 -> r6-final2-1')
MIG_OUT = copy.deepcopy(MIG)
MIG_OUT['final_identifier_changes'].append(collections.OrderedDict([
    ('old', '(none)'),
    ('new', 'R6.STAT.10, R6.EVID.8, REP-BUILD, invariant keys representative_candidate and scanned_paths_within, notation X_rep, OBL-28 row OC-3'),
    ('basis', 'OC-2, OC-3 (owner corrections of 2026-11-25); new ids recorded, not sec. A.48 migrations')]))
log('meta', 'MIGRATION.json', 'new identifiers recorded')

# =====================================================================================
# self-checks (those of final.py, re-run on the corrected outputs, plus the correction's own)
# =====================================================================================
CHECKS = collections.OrderedDict()
ROW_IDS = set(RIDX)
CTRL_IDS = set(i for i in ROW_IDS if not i.startswith('MUT:'))
REQ_IDS = set(REQS)
retired = EXP['retired']
CHECKS['completeness: MAPPING rows not cited in DESIGN-r6.md'] = [
    m['item'] for m in MAPPING['rows'] if not re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(m['item']), T)]
CHECKS['consistency: named controls without a row'] = sorted(set(c for q in REQS.values() for c in q['controls'] if c not in ROW_IDS))
CHECKS['consistency: rows naming an unknown requirement'] = sorted(r['id'] for r in rows if any(x not in REQ_IDS for x in r['requirements']))
CHECKS['consistency: rows named by no requirement'] = sorted(r['id'] for r in rows if not r['requirements'])
two_way = []
for r in rows:
    for q in r['requirements']:
        if r['id'] not in REQS[q]['controls'] and not r.get('composed_of'):
            two_way.append('%s<-%s' % (r['id'], q))
for q in REQS.values():
    for c in q['controls']:
        if c in RIDX and q['id'] not in RIDX[c]['requirements']:
            two_way.append('%s->%s' % (q['id'], c))
CHECKS['consistency: one-way links'] = two_way
CHECKS['consistency: rows with expect null'] = sorted(r['id'] for r in rows if r.get('expect') is None)
RET_LIVE = set()
for e in retired:
    if e['disposition'].startswith(('merged', 'succeeded')):
        continue
    for t in re.split(r',\s*', e['old_id']):
        RET_LIVE.add(t.split(' ')[0])
named_all = set(c for q in REQS.values() for c in q['controls'])
CHECKS['consistency: retired ids live (row or named control)'] = sorted(RET_LIVE & (ROW_IDS | named_all))
CHECKS['consistency: Table 17.1 ids without a row, rows missing from Table 17.1'] = sorted(set(TABLE_IDS) ^ CTRL_IDS)
CHECKS['consistency: cited requirement ids that do not exist'] = sorted(set(re.findall(r'\bR6\.[A-Z0-9]+\.\d+\b', T)) - REQ_IDS)
CHECKS['consistency: cited OBL ids that do not exist'] = sorted(set(re.findall(r'\bOBL-\d+\b', T)) - REQ_IDS)
CHECKS['consistency: GATE-1 to GATE-30 rows present'] = [g for g in ['GATE-%d' % i for i in range(1, 31)] if g not in ROW_IDS]
CHECKS['consistency: rows with candidate expectations not DEFERRED'] = sorted(r['id'] for r in rows if 'candidate_expectations' in r and r['expect'] != {'outcome': 'DEFERRED'})
CHECKS['consistency: superseded names remaining (ISOLATION_REFUSED, RD2-RD5, ...)'] = (
    [s for s in ('ISOLATION_REFUSED', 'REC-ORPHAN', 'REPRO-CLEAN') if s in T] + re.findall(r'\bRD[2-5]\b', T + dumps(EXP_OUT)))
CHECKS['consistency: paired_with naming an id that is not a row'] = sorted(r['id'] for r in rows for p in r.get('paired_with', []) if p not in ROW_IDS)
CHECKS['coverage: non-testable requirements without verification'] = [q['id'] for q in REQ_OUT if q['kind'] != 'testable' and not q['verification']]
TESTABLE_NO_CTRL = [q['id'] for q in REQ_OUT if q['kind'] == 'testable' and not q['controls']]
# the correction's own checks
CHECKS['replay: final.py\'s index rule reproduces out-final/REQUIREMENTS.json from out-final/DESIGN-r6.md'] = [] if REPLAY_OK else ['mismatch']
CHECKS['OC-5: V4, V27, V27-glossary, V15 rows unchanged (deferred)'] = [
    i for i in ('V4', 'V27', 'V27-glossary', 'V15') if dumps(order_row(RIDX[i])) != ROWS_IN[i] or RIDX[i]['expect'] != {'outcome': 'DEFERRED'}]
CHECKS['OC-1: OBL-16 carries no OPEN marker and no "F on main" condition'] = (
    REQS['OBL-16']['open'] + (['F on main'] if re.search(r'F` on `main` with|plan commit `F` on `main`', REQS['OBL-16']['text']) else []) +
    (['TR5 release needs F on main'] if 'F on main whose' in dumps(RIDX['TR5']) else []))
CHECKS['OC-2: OBL-26 carries no circularity marker and is not gated on adoption'] = (
    REQS['OBL-26']['open'] + (['adoption gate'] if "Gates: r6's adoption" in REQS['OBL-26']['text'] else []))
CHECKS['OC-4: LC-7 expects REVIEW_REQUIRED in every case and keeps its OPEN flag'] = (
    [c['case'] for c in RIDX['LC-7']['expect']['cases'] if c['outcome'] != 'REVIEW_REQUIRED'] +
    ([] if any(f.startswith('OPEN: derived-artifact landing blob') for f in RIDX['LC-7']['flags']) else ['flag missing']) +
    ([] if 'derived-artifact landing blob' in REQS['R6.TREE.12']['open'] else ['TREE.12 OPEN missing']))
CHECKS['OC-3: rows on X_rep carry both invariants; item11-T1p does not'] = (
    [c for c in ('RT-L2', 'RT-O9-L2', 'RT-T', 'RT-T0', 'RT-D', 'RT-I7', 'RT-I7A', 'RT-DR3W', 'N10', 'N11', 'REP-BUILD')
     if 'representative_candidate' not in dumps(RIDX[c])] +
    (['item11-T1p'] if 'representative_candidate' in dumps(RIDX['item11-T1p']) else []))
CHECKS['preservation: retired list unchanged'] = [] if dumps(EXP_OUT['retired']) == dumps(EXP['retired']) else ['changed']
CHECKS['preservation: no requirement id removed'] = sorted(set(parse_reqs(T_IN)) - REQ_IDS)
CHECKS['preservation: no expectation row removed'] = sorted(set(ROWS_IN) - ROW_IDS)
CHECKS['preservation: sections 33, 34 and Appendix H unchanged'] = (
    [] if T[T.index('## 33. Retired'):] == T_IN[T_IN.index('## 33. Retired'):] else ['changed'])
OPEN_LEFT = collections.OrderedDict()
for q in REQ_OUT:
    for o in q['open']:
        OPEN_LEFT.setdefault(o, []).append(q['id'])
OPEN_ROWS = [(r['id'], f) for r in rows if True for f in r.get('flags', []) if f.startswith('OPEN')]

for k, v in CHECKS.items():
    if v:
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================
# CORRECTION-REPORT.md
# =====================================================================================
CONTENT = collections.OrderedDict()
CONTENT['DESIGN-r6.md'] = T
CONTENT['EXPECTATIONS.json'] = dumps(EXP_OUT)
CONTENT['REQUIREMENTS.json'] = dumps(REQ_OUT)
CONTENT['MIGRATION.json'] = dumps(MIG_OUT)
CONTENT['PARAPHRASED-DECISIONS.md'] = PARA_TXT
sys.path.insert(0, HERE)
import report_text  # noqa: E402  (static prose of the report, kept beside the generator)
CONTENT['CORRECTION-REPORT.md'] = report_text.build(dict(
    INPUT_SHA=INPUT_SHA, LOG=LOG, CHECKS=CHECKS, OPEN_LEFT=OPEN_LEFT, OPEN_ROWS=OPEN_ROWS,
    TESTABLE_NO_CTRL=TESTABLE_NO_CTRL, OUT_SHA=[(n, sha(c)) for n, c in CONTENT.items()],
    N_ROWS=len(rows), N_REQ=len(REQ_OUT), N_INV=len(inv_sorted), PROBLEMS=PROBLEMS))

def NONASCII(c):
    return set(ch for ch in c if ord(ch) > 127)


NONASCII_IN = {'DESIGN-r6.md': NONASCII(T_IN), 'EXPECTATIONS.json': NONASCII(EXP_TXT), 'REQUIREMENTS.json': NONASCII(REQ_TXT),
               'MIGRATION.json': NONASCII(MIG_TXT), 'PARAPHRASED-DECISIONS.md': NONASCII(PARA_TXT)}
BAD_SP = re.compile('[\u00a0\u1680\u2000-\u200b\u202f\u205f\u3000\ufeff]')
LONG_URL = re.compile(r'https?://github\.com/\S{60,}')
for n, c in CONTENT.items():
    for what, bad in (('@', '@' in c), ('/tmp', '/tmp' in c), ('github.com', 'github.com' in c), ('CR', '\r' in c),
                      ('non-ASCII space', bool(BAD_SP.search(c))), ('long github URL', bool(LONG_URL.search(c))),
                      ('new non-ASCII character', bool(NONASCII(c) - NONASCII_IN.get(n, set())))):
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

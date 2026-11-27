"""Generator of amendment 2 to design r6 (owner decision of 2026-11-26T05:53:39Z, #1169 comment 7183914927).

Usage: python3 -I -B amend2.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, MIGRATION.json and LANDING-MANIFEST.md as amendment 1 leaves them
(each checked against its sha256 below; MIGRATION.json is unchanged from main 02b8e20839d4700de721f8427b3fe9f3c746b71f).
The script reads owner-decision-amendment2.json beside itself and writes into OUT the amended DESIGN-r6.md,
EXPECTATIONS.json and MIGRATION.json, the change record AMENDMENT-2.md and the updated LANDING-MANIFEST.md.

Amendment 2 makes two changes and no other:
- F1: the directory conditions DIR2-DIR5 of the approved migration are renamed Dir2-Dir5 (D2 -> DIR2 -> Dir2, and so
  on), because the A1 profile `register-caps` (P's `CAPS`, three or more capitals not followed by a letter, less
  `CAPS_OK`) matches "DIR" in the engine's string literals, which the purity lint Z9 (R6.CORE.3) checks;
- RT-T: the undefined reference "sec. 8.2" in RT-T's NOT RUN entry is replaced by the record kinds it means.

Every text edit is anchored on an exact string that must occur the stated number of times. Self-checks: the new
identifiers are matched by no run of three or more capitals (the `register-caps` pattern, restated below) and occur
nowhere in the base files; no DIR2-DIR5 remains outside the passages that record the superseded mapping; no
"sec. 8.2" remains; EXPECTATIONS.json changes only in the five `reason` values and RT-T's `not_run`; MIGRATION.json
changes only in its two DIR2-DIR5 entries. Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': '71165d951de96ab94d3900446a9907a39cef80ecea67437ea4df6e602bcf0225',
    'EXPECTATIONS.json': '786e2850f1365197c9d6b87dc98b61ca164ca56caab525eae8d37246a8fb7a19',
    'MIGRATION.json': '9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08',
    'LANDING-MANIFEST.md': '655547fe984e13cc5422121de22d1ef7333f7a12d732ba259d23b6c5e6e3aced',
}
HERE = os.path.dirname(os.path.abspath(__file__))
PLACES = None
# The pattern of P's `CAPS` (edits_check.py at the pinned P commit), restated for the self-check; the profile
# `register-caps` is this pattern less the tokens of `CAPS_OK`, none of which is a condition id.
CAPS = re.compile(r'(?<![A-Za-z\\])[A-Z]{3,}(?![A-Za-z])')
MAPPING = [
    ('D2', 'DIR2', 'Dir2', 'no entry inside `D_rec` exists at `H`'),
    ('D3', 'DIR3', 'Dir3', 'no ledgered, corpus, class-prefix or workflow path inside `D_rec`, at `F` or at `M`'),
    ('D4', 'DIR4', 'Dir4', '`F`\'s tree holds `P_cfg` and the file of record pins inside `D_rec`'),
    ('D5', 'DIR5', 'Dir5', 'no side-change class of the admitted class set uses the reserved class id '
                           '`record-directory`'),
]
OLD_RX = re.compile(r'\bDIR([2-5])\b')
KINDS = ('the reviewed HP adjudication, context-adjudication and hit-classification records (R6.HP.4, R6.CTX.7, '
         'R6.HIT.4)')
RTT_NOT_RUN = {
    'reason': ('needs the reviewed records of sec. 8.2, none of which exists',
               'needs %s, none of which exists' % KINDS),
    'release_condition': ('every reviewed record of sec. 8.2 present at F and verifying under sec. 6.3, run at X_rep '
                          'built from F\'s ledger (R6.EVID.8)',
                          'every one of %s present at F and verifying under the ownership chain and record lint of '
                          'sec. 11 (R6.REC.1 to R6.REC.6), run at X_rep built from F\'s ledger (R6.EVID.8)' % KINDS),
}
# Unqualified citations of the source design's sec. 6.3 in rows' provenance text (not expectation values): qualified as
# "v6.0e sec. 6.3", which is what they cite (the rows' sources are v6.0e locations).
V6_QUALIFY = {
    'GV-CACHE': ('source', 'direction.why'), 'GV-CACHE-AFTER-READ': ('source', 'direction.why'),
    'GV-CACHE-IMMUTABLE': ('source', 'direction.why'), 'GV-CACHE-KEY': ('source', 'direction.why'),
    'R4-B3-DUP': ('flags.0',),
}
UNQUALIFIED_63 = re.compile(r'(?<!v6\.0e )sec\. 6\.3\b')
# RT-T's release_check is a fixed key the gate maps to its evaluator (control_gate.py, RC_RTT); it is kept verbatim,
# and R6.GATE.15 defines the kinds it names. Changing the key is a change to the gate, made with the tool revision.
RTT_RELEASE_CHECK = 'a reviewed record of a sec. 8.2 kind referenced by the configuration at the commit under check'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what, n=1):
    c = text.count(old)
    if c != n:
        raise SystemExit('anchor for %s occurs %d times' % (what, c))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def new_id(m):
    return 'Dir' + m.group(1)


def note(owner):
    q = owner['quotes']
    rows = '\n'.join('| %s | %s | %s | %s |' % (o, s, n, meaning) for o, s, n, meaning in MAPPING)
    return (
        '\n### 0.3 Amendment 2 of 2026-11-26\n\n'
        'The owner decided on F1 and RT-T in the coordinating session; the decision is recorded at %s (%s, %s). '
        'Excerpt: the two table rows (table cells joined by " | ", table padding removed; each line prefixed by '
        '"> "):\n\n' % (owner['record'], owner['author'], owner['time'])
        + '\n>\n'.join('> ' + x for x in q) + '\n\n'
        '- F1. The approved migration (sec. 34, MIGRATION.json) named the directory conditions of sec. 21 DIR2-DIR5. '
        'The engine holds these names as string literals (the reasons of the record-directory rule, R6.CORE.2), and '
        'the purity lint Z9 checks every string literal of the engine against every review and deny profile of the '
        'A1 configuration (R6.CORE.3). The deny profile `register-caps` (P\'s `CAPS`, a run of three or more capitals '
        'not preceded by a letter or backslash and not followed by a letter, less `CAPS_OK`) matches "DIR", so Z9g '
        'and Z9-STAGED fail on them. The lint is kept. The conditions are named Dir2-Dir5, which contain no run of '
        'three capitals:\n\n'
        '| r5 label | Superseded name (approved migration) | Name | Condition (R6.RDIR.5) |\n'
        '|---|---|---|---|\n' + rows + '\n\n'
        '  The names Dir2-Dir5 occur in no file of this directory before amendment 2, and no record has given them a '
        'meaning; DIR2-DIR5 keep the meaning the approved migration gave them and are not reused. Checked with the '
        'tool\'s own lint (engine/purity.py and engine/profiles.py of the tool revision in development, '
        'adb8fc43, provenance) over the engine sources, with `register-caps` built from P\'s `edits_check.py` and the '
        'patterns of `register`, `infinity`, `ptr`, `repo`, `ledger-ext`, `p0-core`, `p0-para`, `count-grep` and the '
        'deny and `resid` rule files: the twelve findings at engine/reconcile.py with DIR2-DIR5 are gone with '
        'Dir2-Dir5, and no finding is added. The other migrated families: TT1-TT14 and RC1-RC13 contain at most two '
        'consecutive capitals and match no profile (RC1-RC13 are also engine enumerations, R6.CORE.5); RDIR-1 to '
        'RDIR-25, RDIR-12b and RDIR-m1 to RDIR-m17 match `register-caps` ("RDIR"), but they occur only in adapter '
        'modules and the expectation file, outside Z9\'s scope (R6.CORE.3), so the lint does not see them. The '
        'condition names are identified case-sensitively: the tool revision renames every occurrence in one change '
        '(OBL-22), with no alias and no case-folding. R6.CORE.2 does not list the reasons naming the conditions '
        'among the allowlisted engine enumerations, so the condition names stay under the profile check of Z9 (a '
        'change put to the owner with F1).\n'
        '- RT-T. RT-T\'s NOT RUN entry named the records it needs as the records "of sec. 8.2", a section r6 does not '
        'have. Its reason and release condition name them: %s. Its release check is a fixed key that the gate maps '
        'to its evaluator, so it keeps its text, and R6.GATE.15 states the kinds it means; the gate\'s key changes '
        'only with the tool revision. Its release condition also read "verifying under sec. 6.3", a section r6 does '
        'not have; the source design\'s sec. 6.3 (v6.0e, at the line RT-T\'s source cites) is the ownership chain and '
        'record lint, whose r6 successor is sec. 11, and it reads "verifying under the ownership chain and record '
        'lint of sec. 11 (R6.REC.1 to R6.REC.6)". Citations of the source design\'s sec. 6.3 in rows\' provenance '
        'text read "v6.0e sec. 6.3".\n\n'
        'Amendment 2 changes nothing else. Its identifier change is a sec. A.48 item 3 migration that needs the '
        'owner\'s approval and an independent review; the tool revision applies it (OBL-22). AMENDMENT-2.md maps each '
        'change to its decision and lists what the tool must change; amendment 2 authorizes no merge, dispatch, '
        'freeze or trial.\n' % (KINDS,))


def amend_design(t, owner):
    t = OLD_RX.sub(new_id, t)
    t = once(t, 'The names Dir2-Dir5 replace the r5 labels D2-D5 so that they cannot be read as the residual-decision\n'
                'labels RD-2 to RD-5 (RE-28; sec. 34).',
             'The names Dir2-Dir5 replace the r5 labels D2-D5 so that they cannot be read as the residual-decision\n'
             'labels RD-2 to RD-5 (RE-28; sec. 34), and they contain no run of three capitals, which the A1 profile\n'
             '`register-caps` matches in the engine\'s string literals (R6.CORE.3; amendment 2, sec. 0.3).',
             'R6.RDIR.5 naming sentence')
    t = once(t, '| D2-D5 (r5 directory conditions) | Dir2-Dir5 | OD-31, RE-28 |',
             '| D2-D5 (r5 directory conditions) | Dir2-Dir5 (DIR2-DIR5 of the approved migration, superseded by '
             'amendment 2, sec. 0.3) | OD-31, RE-28, amendment 2 |', 'sec. 34 row')
    t = once(t, '`not a regular file`, and the reasons naming Dir2-Dir5 and `directory not admitted`), and the path',
             '`not a regular file`, and `directory not admitted`), and the path', 'R6.CORE.2 allowlist clause')
    t = once(t, 'NOT RUN (Q6). RT-T is NOT RUN until the reviewed records it needs exist.',
             'NOT RUN (Q6). RT-T is NOT RUN until the reviewed records it needs exist: %s. The release check of its '
             'expectation row, a fixed key of the gate, names them as the records of "a sec. 8.2 kind"; it means these '
             'three kinds.' % KINDS, 'R6.GATE.15 RT-T')
    t = once(t, '\n***\n\n## 1. Notation and symbols', '\n' + note(owner) + '\n***\n\n## 1. Notation and symbols',
             '0.3 note')
    return t


def amend_expectations(E):
    E = copy.deepcopy(E)
    changes = []
    n = 0
    for r in E['rows']:
        for path, obj in walk_reasons(r):
            if isinstance(obj.get('reason'), str) and OLD_RX.fullmatch(obj['reason']):
                old = obj['reason']
                obj['reason'] = OLD_RX.sub(new_id, old)
                changes.append((r['id'], 'F1', '%s: reason "%s" -> "%s"' % (path, old, obj['reason'])))
                n += 1
        if r['id'] in V6_QUALIFY:
            for field in V6_QUALIFY[r['id']]:
                head, _, tail = field.partition('.')
                holder = r
                key = head
                if tail:
                    holder = r[head]
                    key = int(tail) if isinstance(holder, list) else tail
                old = holder[key]
                if len(UNQUALIFIED_63.findall(old)) != 1:
                    raise SystemExit('%s %s: expected one unqualified "sec. 6.3"' % (r['id'], field))
                holder[key] = UNQUALIFIED_63.sub('v6.0e sec. 6.3', old)
            changes.append((r['id'], 'RT-T (sec. 6.3)', '%s: "sec. 6.3" qualified as "v6.0e sec. 6.3" (provenance '
                                                        'text; no expectation value changed)'
                            % ', '.join(V6_QUALIFY[r['id']])))
        if r['id'] == 'RT-T':
            for k, (was, now) in RTT_NOT_RUN.items():
                if r['not_run'][k] != was:
                    raise SystemExit('RT-T not_run.%s differs from the base' % k)
                r['not_run'][k] = now
            if r['not_run']['release_check'] != RTT_RELEASE_CHECK:
                raise SystemExit('RT-T release_check differs from the base')
            changes.append(('RT-T', 'RT-T', 'not_run reason and release_condition: "sec. 8.2" replaced by the record '
                                            'kinds (R6.HP.4, R6.CTX.7, R6.HIT.4); release_condition: "verifying under '
                                            'sec. 6.3" replaced by "verifying under the ownership chain and record lint '
                                            'of sec. 11 (R6.REC.1 to R6.REC.6)"; release_check kept verbatim, a fixed '
                                            'key of the gate, its kinds defined in R6.GATE.15'))
    if n != 5:
        raise SystemExit('expected 5 reason values naming DIR2-DIR5, found %d' % n)
    return E, changes


def walk_reasons(x, path=''):
    if isinstance(x, dict):
        yield path or '/', x
        for k, v in x.items():
            for y in walk_reasons(v, path + '/' + k):
                yield y
    elif isinstance(x, list):
        for i, v in enumerate(x):
            for y in walk_reasons(v, path + '/' + str(i)):
                yield y


def amend_migration(M):
    M = copy.deepcopy(M)
    sd = [e for e in M['section_D_migration_index'] if e['new'] == 'DIR2-DIR5']
    fi = [e for e in M['final_identifier_changes'] if e['new'] == 'DIR2-DIR5']
    if len(sd) != 1 or len(fi) != 1:
        raise SystemExit('MIGRATION.json: DIR2-DIR5 entries %d, %d' % (len(sd), len(fi)))
    for e in sd + fi:
        e['new'] = 'Dir2-Dir5'
        e['superseded'] = 'DIR2-DIR5 (see the final_identifier_changes entry of amendment 2)'
    M['final_identifier_changes'].append(dict(MIG_ENTRY))
    return M


MIG_ENTRY = {'old': 'DIR2-DIR5 (approved migration, #1169 comment 7182798225)', 'new': 'Dir2-Dir5',
             'basis': 'amendment 2 (#1169 comment 7183914927)'}


def self_checks(t, E0, E, M0, M, base_texts):
    problems = []
    for _, _, n, _ in MAPPING:
        if CAPS.search(n):
            problems.append('%s is matched by the CAPS pattern' % n)
        for name, b in base_texts.items():
            if re.search(r'\b%s\b' % n, b):
                problems.append('%s already occurs in base %s' % (n, name))
    for _, s, _, _ in MAPPING:
        if not CAPS.search(s):
            problems.append('control: %s is not matched by the CAPS pattern' % s)
    a = t.index('### 0.3 Amendment 2')
    b = t.index('\n***\n', a)
    rest = t[:a] + t[b:]
    left = [m.start() for m in re.finditer(r'\bDIR[2-5]\b', rest)]
    allowed = [rest.index('Dir2-Dir5 (DIR2-DIR5 of the approved migration')]
    if [p for p in left if not any(0 <= p - q < 60 for q in allowed)]:
        problems.append('DIR2-DIR5 remains in DESIGN-r6.md outside sec. 0.3 and sec. 34')
    ex = json.dumps(E).replace(json.dumps(RTT_RELEASE_CHECK), '')
    if UNQUALIFIED_63.search(json.dumps(E)):
        problems.append('an unqualified "sec. 6.3" remains in EXPECTATIONS.json')
    if UNQUALIFIED_63.search(t[:t.index('### 0.3 Amendment 2')] + t[t.index('\n***\n', t.index('### 0.3 Amendment 2')):]):
        problems.append('an unqualified "sec. 6.3" remains in DESIGN-r6.md outside sec. 0.3')
    rs = rest.replace('names them as the records of "a sec. 8.2 kind"', '')
    for name, text in (('DESIGN-r6.md outside sec. 0.3', rs), ('EXPECTATIONS.json', ex)):
        if 'sec. 8.2' in text:
            problems.append('"sec. 8.2" remains in %s' % name)
    r0 = {r['id']: r for r in E0['rows']}
    r1 = {r['id']: r for r in E['rows']}
    if set(r0) != set(r1) or {k: v for k, v in E0.items() if k != 'rows'} != {k: v for k, v in E.items() if k != 'rows'}:
        problems.append('EXPECTATIONS.json: rows or top-level fields changed')
    for rid in r0:
        a0 = json.dumps(r0[rid], sort_keys=True)
        a1 = OLD_RX.sub(new_id, a0) if rid != 'RT-T' else a0
        b1 = json.dumps(r1[rid], sort_keys=True)
        if rid in V6_QUALIFY:
            b1 = b1.replace('v6.0e sec. 6.3', 'sec. 6.3')
            for f in ('expect', 'restored', 'not_run', 'requirements', 'status_allowed'):
                if r0[rid].get(f) != r1[rid].get(f):
                    problems.append('EXPECTATIONS.json: row %s field %s changed' % (rid, f))
        if rid == 'RT-T':
            x = copy.deepcopy(r1[rid])
            x['not_run'] = r0[rid]['not_run']
            b1 = json.dumps(x, sort_keys=True)
        if a1 != b1:
            problems.append('EXPECTATIONS.json: row %s changed beyond amendment 2' % rid)
    m0 = json.dumps(M0, sort_keys=True)
    m1 = copy.deepcopy(M)
    if m1['final_identifier_changes'][-1] != MIG_ENTRY:
        problems.append('MIGRATION.json: the amendment-2 entry is not last in final_identifier_changes')
    m1['final_identifier_changes'] = m1['final_identifier_changes'][:-1]
    for k in ('section_D_migration_index', 'final_identifier_changes'):
        for e in m1[k]:
            if e.get('superseded'):
                e['new'] = 'DIR2-DIR5'
                del e['superseded']
    if json.dumps(m1, sort_keys=True) != m0:
        problems.append('MIGRATION.json changed beyond its two DIR2-DIR5 entries')
    return problems


def design_places(t):
    """(occurrences, lines, places): each DIR2-DIR5 in the base design with the requirement, obligation, control-table
    row or section that holds it."""
    places = []
    occ = 0
    lines = 0
    pos = 0
    for line in t.split('\n'):
        k = len(OLD_RX.findall(line))
        if k:
            occ += k
            lines += 1
            before = t[:pos]
            ids = [(m.start(), m.group(1)) for m in re.finditer(r'^\*\*((?:R6\.[A-Z0-9]+\.[0-9]+)|OBL-[0-9]+)\*\*', before,
                                                             re.M)]
            secs = [(m.start(), m.group(1)) for m in re.finditer(r'^(#{2,3} [0-9.]+)', before, re.M)]
            row = re.match(r'^\| ((?:MUT:)?[A-Za-z0-9:.-]+) \|', line)
            if row:
                where = 'table row ' + row.group(1)
            else:
                cand = max(ids + secs) if ids or secs else (0, 'preamble')
                where = cand[1].lstrip('# ').strip()
                where = 'sec. ' + where.rstrip('.') if where[:1].isdigit() else where
            if where not in places:
                places.append(where)
        pos += len(line) + 1
    return occ, lines, places


def change_record(changes, owner, outs, gen_sha, owner_sha):
    lines = [
        '# r6 amendment 2: change record',
        '',
        'Owner decision (%s, %s; %s, relayed by the %s), quoted as an excerpt in DESIGN-r6.md sec. 0.3. Generated by '
        'generator-amendment2/amend2.py (sha256 %s) from the amendment-1 outputs and MIGRATION.json, and '
        'generator-amendment2/owner-decision-amendment2.json (sha256 %s). This record maps every change to the '
        'decision it implements; it adopts nothing beyond that decision and authorizes no merge, dispatch, freeze or '
        'trial. The identifier change is a migration under AGENTS.md sec. A.48 item 3: it needs the owner\'s approval '
        'in advance and an independent non-author review.' % (owner['author'], owner['time'], owner['record'],
                                                             owner['relayed_by'], gen_sha, owner_sha),
        '',
        '## 1. Mapping (F1)',
        '',
        '| r5 label | Superseded name | Name | Condition |',
        '|---|---|---|---|',
    ] + ['| %s | %s | %s | %s |' % m for m in MAPPING] + [
        '',
        'Justification: the names keep the reading "directory condition" and the numbering of sec. 21; they contain '
        'no run of three capitals, so `register-caps` (P\'s `CAPS` less `CAPS_OK`) does not match them; they occur in '
        'no file of the design directory, the tool branch or `main` before this amendment, so no record has given '
        'them a meaning (sec. A.48 item 3, sec. A.30). Rejected: DC2-DC5 (`DC1` and `DC4` name divergence conditions '
        'in verification/ROADMAP.md); RD2-RD5 (the integration name, and confusable with the residual-decision labels '
        'RD-2 to RD-5); D2-D5 (the decision labels D1-D8); allowlisting DIR2-DIR5 (an exemption from the lint, which '
        'the owner\'s decision excludes). DS2-DS5 also passes the lint and is unused; it was not chosen because it is '
        'less clear. Case: a case-insensitive search for DIR2 also returns Dir2, which names the same condition, and '
        'the unrelated DIR2 of the two oi-qm files (sec. 3); identification is case-sensitive, and the independent '
        'review confirmed it reliable on two conditions, both applied: the structured MIGRATION.json entry of sec. 2, '
        'and the tool revision renaming every occurrence in one change, with no alias and no case-folding (stated in '
        'DESIGN-r6.md sec. 0.3). The owner preferred Dir2-Dir5 on that confirmation (amaybaum, 2026-11-26, '
        'coordinating session).',
        '',
        '## 2. Changes',
        '',
        '| File | Place | Decision | Change |',
        '|---|---|---|---|',
        '| DESIGN-r6.md | sec. 0.3 (new) | F1, RT-T | the owner decision quoted as an excerpt; the mapping, its lint '
        'evidence and the RT-T correction stated |',
        '| DESIGN-r6.md | every occurrence of DIR2, DIR3, DIR4, DIR5 (%d occurrences on %d lines: %s) | F1 | renamed '
        'Dir2, Dir3, Dir4, Dir5 |' % (PLACES[0], PLACES[1], ', '.join(PLACES[2])),
        '| DESIGN-r6.md | R6.RDIR.5, naming sentence | F1 | states that the names contain no run of three capitals |',
        '| DESIGN-r6.md | R6.GATE.15, RT-T sentence | RT-T | names the three record kinds and defines the "sec. 8.2 '
        'kind" of RT-T\'s release check |',
        '| DESIGN-r6.md | sec. 34, row D2-D5 | F1 | Dir2-Dir5, with DIR2-DIR5 recorded as superseded |',
        '| MIGRATION.json | section_D_migration_index and final_identifier_changes, the DIR2-DIR5 entries | F1 | '
        '`new` Dir2-Dir5; `superseded` names DIR2-DIR5 and points to the amendment-2 entry |',
        '| MIGRATION.json | final_identifier_changes, appended | F1 | %s |' % json.dumps(MIG_ENTRY),
        '| DESIGN-r6.md | R6.CORE.2, allowlist clause | F1 (put to the owner with F1) | "the reasons naming Dir2-Dir5 '
        'and" removed, keeping `directory not admitted`, so the condition names stay under the profile check of Z9; '
        'this strengthens the lint |',
    ] + ['| EXPECTATIONS.json | %s | %s | %s |' % c for c in changes] + [
        '',
        '## 3. Reference trace (F1)',
        '',
        '| Place | Occurrences of DIR2-DIR5 | Disposition |',
        '|---|---|---|',
        '| DESIGN-r6.md | %d occurrences on %d lines | renamed by this amendment; the superseded name is recorded in '
        'sec. 34 and sec. 0.3 |' % (PLACES[0], PLACES[1]),
        '| EXPECTATIONS.json | 5 occurrences on 5 lines (`reason` values of RDIR rows) | renamed by this amendment |',
        '| MIGRATION.json | 4 occurrences on 2 lines | renamed by this amendment; superseded name recorded |',
        '| REQUIREMENTS.json | 0 occurrences | unchanged |',
        '| FRESH-AUTHORIZATION.md | 5 occurrences on 3 lines (quotations of the design) | unchanged: a record quoting '
        'the design as it stood |',
        '| generator-round2/correct.py, report_text.py, text2.py | 1, 1 and 2 occurrences, on 1 line each | unchanged: '
        'the generators of an earlier round, which reproduce their own outputs |',
        '| the tool (branch tools/a1-ledger-coverage-r6 at adb8fc43): engine/reconcile.py | 18 occurrences on 14 lines '
        '| the tool '
        'revision '
        'renames them (OBL-22): the keys of `conditions`, the `_stop` reasons and the comments |',
        '| the tool: adapters/record_directory_controls.py | 15 occurrences on 11 lines | the tool revision renames them (OBL-22) |',
        '| the tool: verification/audits/foundations/ledger-coverage-tool-20261123/IMPLEMENTATION-PLAN-r6.md | 6 occurrences on '
        '3 lines | '
        'the plan states the conflict (F1); updated with the tool revision |',
        '| the tool: engine/purity.py allowlist | 0 occurrences | no change: the names pass the lint without being '
        'allowlisted, and R6.CORE.2 no longer allowlists them (sec. 2) |',
        '| the gate: tools/ledger_coverage/gate/control_gate.py (RC_RTT and the comment above its record kinds) | 0 '
        'occurrences; RT-T\'s release-check key says "sec. 8.2" | changing the key is a gate change; if the tool '
        'revision changes it, the expectation file\'s release_check changes with it in the same change |',
        '| verification/programmes/oi-qm (pe01_bounded_tests_v1/run.py, round-ord-1-composition-order/controls.py) | '
        '6 occurrences on 6 lines | DIR2 there is a usage placeholder and a variable name with other meanings; unchanged, and a further '
        'reason the conditions take a name no record uses |',
        '',
        '## 4. The sec. 6.3 reference (RT-T)',
        '',
        'RT-T\'s release condition read "verifying under sec. 6.3"; r6 has no sec. 6.3. The independent review '
        'recovered its meaning from the source design: RT-T\'s source is v6.0e line 2210, and v6.0e sec. 6.3 is the '
        'ownership chain and record lint, whose r6 successor is sec. 11. The release condition reads "verifying under '
        'the ownership chain and record lint of sec. 11 (R6.REC.1 to R6.REC.6)". The rows that cite the source design\'s '
        'sec. 6.3 in provenance text (the `source` and `direction.why` of GV-CACHE, GV-CACHE-AFTER-READ, '
        'GV-CACHE-IMMUTABLE and GV-CACHE-KEY, and `flags[0]` of R4-B3-DUP) cite it as "v6.0e sec. 6.3": qualifying '
        'keeps them accurate as provenance, where replacing them with r6 requirement ids would change what they cite; '
        'no expectation value changes.',
        '',
        '## 5. Open items for the owner and the tool revision',
        '',
        '- RT-T\'s release check ("a reviewed record of a sec. 8.2 kind referenced by the configuration") is true once '
        'any one of the three kinds is referenced, while its release condition requires every one of them. A release '
        'check that holds early only lets the runner record RT-T, which then fails if a kind is missing, so it fails '
        'closed. The check is a fixed key of the gate (RC_RTT); aligning it with the release condition is a gate change '
        'for the tool revision, made together with the expectation file. Amendment 2 does not change it.',
        '',
        '## 6. Outputs',
        '',
        '| File | sha256 |',
        '|---|---|',
    ]
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'MIGRATION.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines += ['', 'REQUIREMENTS.json is not changed by amendment 2. Self-checks run by the generator: the new names are '
              'matched by no run of three capitals and occur in no base file; DIR2-DIR5 are matched (control); no '
              'DIR2-DIR5 remains outside the passages that record the superseded mapping; no "sec. 8.2" remains outside '
              'the gate key and its definition; no unqualified "sec. 6.3" remains; MIGRATION.json ends with the '
              'amendment-2 entry; '
              'EXPECTATIONS.json and MIGRATION.json change only where stated.', '']
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('MIGRATION.json', 'final r6 document (migration index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        m = m[:mm[0].start()] + '| %s | %s | amendment-2 output | %s |' % (n, label, sha(outs[n])) + m[mm[0].end():]
    rows = ('| AMENDMENT-2.md | change record of amendment 2 | amendment-2 output | %s |\n'
            '| generator-amendment2/amend2.py | amendment-2 generator | amendment-2 generator | %s |\n'
            '| generator-amendment2/owner-decision-amendment2.json | amendment-2 generator input (the owner decision '
            'quoted) | amendment-2 generator | %s |\n' % (sha(outs['AMENDMENT-2.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-1 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-2 output | (this file) |', 'manifest self row')
    para = ('\nAmendment 2 (owner decision of 2026-11-26T05:53:39Z, amaybaum, #1169 comment 7183914927, quoted in '
            'DESIGN-r6.md sec. 0.3): DESIGN-r6.md, EXPECTATIONS.json and MIGRATION.json are amended, and AMENDMENT-2.md '
            'maps each change to its decision. Recipe: run the amendment-1 recipe into `out1/`, copy MIGRATION.json of '
            'this directory at main 02b8e20839d4700de721f8427b3fe9f3c746b71f into `out1/`, and run `python3 -I -B '
            'generator-amendment2/amend2.py out1 out2`. It checks the four files against their sha256, exits 0 and '
            'writes into `out2/` the files of sec. 1 marked "amendment-2 output" with the sha256 stated and this '
            'manifest.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend2.py BASE OUT\n')
        return 64
    base, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(base, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decision-amendment2.json'), 'rb') as f:
        owner_b = f.read()
    owner = json.loads(owner_b)
    E0 = json.loads(data['EXPECTATIONS.json'])
    M0 = json.loads(data['MIGRATION.json'])
    if dumpj(M0) != data['MIGRATION.json'] or dumpj(E0) != data['EXPECTATIONS.json']:
        sys.stderr.write('JSON base files do not round-trip\n')
        return 65
    E, changes = amend_expectations(E0)
    M = amend_migration(M0)
    global PLACES
    PLACES = design_places(data['DESIGN-r6.md'].decode('utf-8'))
    t = amend_design(data['DESIGN-r6.md'].decode('utf-8'), owner)
    problems = self_checks(t, E0, E, M0, M, {n: b.decode('utf-8') for n, b in data.items()})
    if problems:
        sys.stderr.write('self-check failures:\n' + '\n'.join(problems) + '\n')
        return 1
    outs = {'DESIGN-r6.md': t.encode('utf-8'), 'EXPECTATIONS.json': dumpj(E), 'MIGRATION.json': dumpj(M)}
    with open(os.path.join(HERE, 'amend2.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-2.md'] = change_record(changes, owner, outs, gen_sha, sha(owner_b)).encode('utf-8')
    outs['LANDING-MANIFEST.md'] = manifest(data['LANDING-MANIFEST.md'].decode('utf-8'), outs, gen_sha,
                                           sha(owner_b)).encode('utf-8')
    os.makedirs(out, exist_ok=True)
    for n, b in sorted(outs.items()):
        with open(os.path.join(out, n), 'wb') as f:
            f.write(b)
        print('%s %s' % (sha(b), n))
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Round PRESERVE-INDUCT-1 -- the round's own static controls and verdict (draft, before F).

It reads nothing but the repository, through git, and certifies nothing on its own: the Lean kernel,
the axiom audit and the release gate establish the mathematics, the governed probe the exact layer,
and the V3 verifier the protocol. What it checks is that the execution carries the frozen surface of
the two modules, the statement-level design invariants the preregistration asserts, the frozen
execution blobs and the frozen workflow, import and census edits, the retained evidence the
preregistration pins, none of the excluded phrases, and no change outside the governed paths.

    python3 -I controls.py --self-test                    the checker's own controls, on a synthetic
                                                          D/F/E fixture and the preregistration
                                                          beside this file
    python3 -I controls.py check <E> --freeze <F> [--stage E|S1]
                                                          the static controls at E (stage E, the
                                                          default) or at the first execution commit
                                                          (stage S1)
    python3 -I controls.py verdict <E> --freeze <F> [--axioms LOG]
                                                          the cell tokens from the measurements at E:
                                                          the static controls, the probe blob at E run
                                                          with python3 -I -B, and the axiom reports of
                                                          E's exact-head bridge log

Parameters marked PENDING below are not yet fixed (preregistration, "Design and freeze boundary"
items 2-5). While any is None, the controls that depend on it fail closed, so neither `check` nor
`verdict` can pass. Exit 1 on any failure, 2 on a usage error.
"""
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import types

D = 'b96662e6be4f537502c772db369ea32a35b213a8'
ROUND = 'PRESERVE-INDUCT-1'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
CONTROLS = RDIR + 'controls.py'
FRUN = 'evidence/f-run/'
CORE = 'verification/lean-mathlib/OIBridge/PreservationInduction.lean'
INST = 'verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean'
PROBE = 'verification/lean/preserve_induct1_probe.py'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
REGISTRY = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LEGACY = 'verification/infrastructure/legacy-records.json'
RECEIPT = 'verification/receipts/PRESERVE-INDUCT-1.json'
RESEARCH_MARKS = ('ResearchDesign', 'PreservationInductionDesign')

ROUND_BLOCK = ['round ' + ROUND, 'kind non-sealing', 'record-directory ' + RDIR]
GOVERNED = [('record', 'AM', RDIR), ('record', 'AM', RECEIPT), ('execution', 'A', CORE),
            ('execution', 'A', INST), ('execution', 'A', PROBE), ('execution', 'M', ROOT),
            ('execution', 'M', REGISTRY), ('execution', 'M', WORKFLOW)]
FROZEN_PATHS = {CONTROLS, CORE, INST, PROBE}
RET_TITLE = 'Retained evidence (§A.42).'
HISTORICAL = {'core-build-38450187534', 'instance-build-38454439833'}  # a digest or a recorded gap
REQUIRED_PIN = 'predicted-tree'                                          # a digest only
EVIDENCE_ROWS = HISTORICAL | {REQUIRED_PIN}
GAP, NONE = 'GAP', 'NONE'
# Owner decision of 2026-10-17: the replacement drafting chain cites #831 and imports none of its commits.
OLD_CHAIN = {'5f614d60c3234cf35bc9b15e892388d576f77aa1', '65b85147f85aa01770e0e60551152bc5f1d9ef29'}
SUPERSEDED_CITE = ('65b85147f85aa01770e0e60551152bc5f1d9ef29', 'https://github.com/amaybaum/incompleteness/pull/831')
SYMPY_PIN = '1.14.0'

# The surface the preregistration names (sections "Research-design definition and theorem budget").
CORE_NAMES = ['CarrierConeFamily', 'AdditiveClosure', 'PreservesCarrier', 'PrimitivePreservation',
              'UniformAttachPreservation', 'AncillaDiscardPreservation', 'finite_sum_mem',
              'instAvail_preserves', 'instAvail_sum_preserves', 'instAvail_spectator_preserves',
              'instAvail_transport_preserves']
INST_NAMES = ['quantumCone', 'classicalCone', 'classicalClass', 'classicalCone_iff', 'quantum_additive',
              'quantum_conj', 'quantum_primitive', 'attachBlock', 'attachBlock_apply', 'uniformAttach_eq_blocks',
              'quantum_attach', 'ptraceAnc_eq_blocks', 'quantum_discard', 'quantum_instAvail',
              'quantum_fullClass', 'classical_additive', 'classical_conj', 'classical_primitive',
              'classical_attach', 'classical_discard', 'classical_readProj', 'classical_instAvail',
              'classical_native_readout']
INST_EXAMPLES = 2
CORE_IMPORTS = ['import OIBridge.ImplementationLocality']
INST_IMPORTS = ['import OIBridge.PreservationInduction', 'import OIBridge.StructuralClosure']
HEADLINE = 'instAvail_preserves'
COR_PRINTS = ['instAvail_sum_preserves', 'instAvail_spectator_preserves', 'instAvail_transport_preserves']
CORE_PRINTS = [HEADLINE] + COR_PRINTS
INST_PRINTS = ['quantum_instAvail', 'classical_instAvail', 'quantum_attach', 'quantum_discard',
               'classical_readProj', 'classical_native_readout']
ARMS = ['op', 'readout', 'coarse', 'bind', 'discard']
FIELDS = {'AdditiveClosure': ['zero_mem', 'add_mem'], 'PrimitivePreservation': ['op', 'readout']}
COROLLARY_USES = {'instAvail_sum_preserves': [HEADLINE],
                  'instAvail_spectator_preserves': [HEADLINE, 'instAvail_spectator'],
                  'instAvail_transport_preserves': [HEADLINE, 'instAvail_transport']}
CORE_EXCLUDED = r'PosSemidef|IsHermitian|Convex|IsClosed|\btrace\b|instAvail_trace|↔|\bIff\b|\breach'
FORBIDDEN = r'\b(sorry|admit|native_decide|axiom|implemented_by|extern)\b'

# Landed objects at D (file, line, name); their blobs at E are D's.
LP = 'verification/lean-mathlib/OIBridge/'
LANDED = [
    (LP + 'ImplementationLocality.lean', 244, 'ImplementationClass'),
    (LP + 'ImplementationLocality.lean', 256, 'readProj'),
    (LP + 'ImplementationLocality.lean', 268, 'InstAvail'),
    (LP + 'ImplementationLocality.lean', 317, 'instAvail_trace'),
    (LP + 'ImplementationLocality.lean', 359, 'ContextStable'),
    (LP + 'ImplementationLocality.lean', 364, 'LabelInvariant'),
    (LP + 'ImplementationLocality.lean', 374, 'fullClass'),
    (LP + 'ImplementationLocality.lean', 644, 'instAvail_transport'),
    (LP + 'ImplementationLocality.lean', 789, 'instAvail_spectator'),
    (LP + 'ImplementationLocality.lean', 820, 'instAvail_withSpectator'),
    (LP + 'OperationalAssembly.lean', 453, 'ptraceAnc'),
    (LP + 'OperationalAssembly.lean', 492, 'uniformAttach'),
    (LP + 'OperationalAssembly.lean', 515, 'discardWith'),
    (LP + 'MonoidalCompletion.lean', 360, 'conjChannel'),
    (LP + 'ReferenceExtension.lean', 131, 'amplRefL'),
    (LP + 'SpectatorBridge.lean', 348, 'transport'),
    (LP + 'StructuralClosure.lean', 180, 'substratumClass'),
    (LP + 'StructuralClosure.lean', 261, 'substratumClass_contextStable'),
    (LP + 'StructuralClosure.lean', 275, 'substratumClass_labelInvariant'),
]
ROOT_LINES = ['import OIBridge.PreservationInduction', 'import OIBridge.PreservationInductionInstances']
PHRASES = ['OI supplies', 'sources the preservation premises', 'preservation is derived from OI',
           'compatibility is derived', 'K2 is closed', 'P0 is closed', 'F2 is closed', 'OI implies QM',
           'the probe proves']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
BAD_LOG = ('sorryAx', 'Lean.ofReduceBool', 'Lean.trustCompiler')

# PENDING: fixed before F (preregistration items 2-5); None fails the dependent controls closed.
NS = None           # the adopted namespace (item 2)                        S1, verdict
SPLICES = None      # [(old, new)] edits to verify.yml at D, each anchored once (item 5)   W
FAMILIES = None     # the census families appended for the two modules (item 3)         J
PROBE_SPEC = None   # {'codes', 'independent', 'n', 'mutations', 'final', 'stdout_sha256', ['sympy']} (item 4)  EXACT, W
PENDING = ('NS', 'SPLICES', 'FAMILIES', 'PROBE_SPEC')

REQUIRED = {'E': ['C1', 'C2', 'S1', 'S2', 'S3', 'S4', 'W', 'I', 'J', 'P', 'R', 'G', 'T'],
            'S1': ['C1', 'C2', 'P', 'R', 'G', 'T']}
STAGES = tuple(REQUIRED)
CELLS = [('Q-CORE', 'PRESERVE-INDUCT-CORE-PROVED', 'PRESERVE-INDUCT-CORE-NOT-ESTABLISHED'),
         ('Q-COR', 'PRESERVE-INDUCT-COROLLARIES-PROVED', 'PRESERVE-INDUCT-COROLLARIES-NOT-ESTABLISHED'),
         ('Q-EXACT', 'PRESERVE-INDUCT-EXACT-CHECKED', 'PRESERVE-INDUCT-EXACT-NOT-ESTABLISHED')]
READ, NOT_READ = 'PRESERVE-INDUCT-1-READ', 'PRESERVE-INDUCT-1-NOT-READ'
POSITIVE = [c[1] for c in CELLS] + [READ]
SELF_CHECKS = 46  # the number of self-checks; a dropped self-check fails the count

FAIL = []
RAN = []


def report(name, ok, detail=''):
    ok = ok is True
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''))
    RAN.append(name)
    if not ok:
        FAIL.append(name)
    return ok


def git(*args):
    return subprocess.run(['git'] + list(args), capture_output=True, text=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def blob(commit, path):
    r = subprocess.run(['git', 'rev-parse', '--verify', '-q', '%s:%s' % (commit, path)],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def is_ancestor(a, b):
    return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0


def has_token(out, tok):
    return re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(tok), out) is not None


def flat(s):
    return ' '.join(s.split())


def uncomment(text):
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        if text.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth:
            if text.startswith('-/', i):
                depth -= 1; i += 2
            else:
                if text[i] == '\n':
                    out.append('\n')
                i += 1
            continue
        if text.startswith('--', i):
            j = text.find('\n', i); i = n if j < 0 else j; continue
        out.append(text[i]); i += 1
    return ''.join(out)


# ---------------------------------------------------------------- the preregistration's frozen tables

def fenced(prereg, info):
    """The bodies of every block opened by exactly ```info."""
    return re.findall(r'^```%s\n(.*?)^```$' % re.escape(info), prereg or '', re.S | re.M)


def governed(prereg):
    """[(class, ops, path)] of the single v3-governed-paths block, or None when absent or malformed."""
    blocks = fenced(prereg, 'v3-governed-paths')
    if len(blocks) != 1:
        return None
    out = []
    for ln in blocks[0].splitlines():
        if not ln.strip() or ln.startswith('#'):
            continue
        parts = ln.split(' ')
        if len(parts) != 3 or parts[0] not in ('record', 'execution') or not parts[1] or \
                any(c not in 'AMD' for c in parts[1]):
            return None
        out.append(tuple(parts))
    return out or None


def round_block(prereg):
    blocks = fenced(prereg, 'v3-round')
    return [ln for ln in blocks[0].splitlines() if ln.strip()] if len(blocks) == 1 else None


def table_after(prereg, title):
    """The rows of the table that directly follows the bold paragraph `title` (one blank line between), as lists
    of cells; [] when the paragraph or its table is absent. It never reaches a later table."""
    m = re.search(r'\*\*%s\*\*[^\n]*(?:\n[^\n|][^\n]*)*\n\n((?:\|[^\n]*\n)+)' % re.escape(title), prereg or '')
    if not m:
        return []
    rows = [[c.strip() for c in ln.strip().strip('|').split('|')] for ln in m.group(1).splitlines()]
    return [r for r in rows[2:] if r]


def pinned(prereg, title, width):
    """{path: digest or None (pending)} from a two-column pin table; None when a row is malformed or repeated."""
    out = {}
    for r in table_after(prereg, title):
        if len(r) != 2 or not re.fullmatch(r'`[^`]+`', r[0]):
            return None
        path, cell = r[0].strip('`'), r[1]
        if path in out:
            return None
        if re.fullmatch(r'`[0-9a-f]{%d}`' % width, cell):
            out[path] = cell.strip('`')
        elif cell.startswith('pending'):
            out[path] = None
        else:
            return None
    return out


def frozen_blobs(prereg):
    return pinned(prereg, 'Frozen execution blobs.', 40)


def retention(prereg):
    """{row label: (file, digest)} from the three-column retention table; None when a row is malformed or repeated.
    file: a record-relative `evidence/...` path, a repository path retained on main (`verification/...`, outside
    the record directory), None (pending) or NONE (a gap row names no file). digest: sha256, None (pending) or GAP
    (`gap:` and what is missing). Admitted pairs: (path, digest), (path or None, None), (NONE, GAP)."""
    out = {}
    for r in table_after(prereg, RET_TITLE):
        if len(r) != 3 or not re.fullmatch(r'`[a-z0-9-]+`', r[0]) or r[0].strip('`') in out:
            return None
        f, h = r[1], r[2]
        if re.fullmatch(r'`[^`\s]+`', f):
            path = f.strip('`')
            if not (path.startswith('evidence/') or (path.startswith('verification/') and not path.startswith(RDIR))):
                return None
        elif f.startswith('pending'):
            path = None
        elif f == 'none':
            path = NONE
        else:
            return None
        if re.fullmatch(r'`[0-9a-f]{64}`', h):
            dig = h.strip('`')
        elif h.startswith('pending'):
            dig = None
        elif re.match(r'gap: \S', h):
            dig = GAP
        else:
            return None
        if not ((dig not in (None, GAP) and path not in (None, NONE)) or (dig is None and path != NONE)
                or (path == NONE and dig == GAP)):
            return None
        out[r[0].strip('`')] = (path, dig)
    return out


def resolve(path):
    return RDIR + path if path.startswith('evidence/') else path


def record_files(rows):
    """The record-relative files the digest rows name."""
    return {p for p, h in rows.values() if h not in (None, GAP) and p not in (None, NONE) and p.startswith('evidence/')}


def landed_table(prereg):
    rows = table_after(prereg, "S2's landed objects at D.")
    out = []
    for r in rows:
        m = len(r) == 2 and re.fullmatch(r'`([^`]+)` \| `([A-Za-z]+\.lean):(\d+)`', r[0] + ' | ' + r[1])
        if not m:
            return None
        out.append((LP + m.group(2), int(m.group(3)), m.group(1)))
    return out


def frozen_surface(prereg):
    """(core block, instances block) from the section '## The statement surface (frozen', else None."""
    m = re.search(r'^## The statement surface \(frozen.*?(?=^## |\Z)', prereg or '', re.S | re.M)
    if not m:
        return None
    blocks = fenced(m.group(0), 'lean')
    return tuple(blocks) if len(blocks) == 2 and all(b.strip() for b in blocks) else None


# ---------------------------------------------------------------- Lean text

DECL = re.compile(r"^(?:noncomputable )?(def|abbrev|theorem|structure|inductive)\s+([A-Za-z_][\w.']*)", re.M)
BOUNDARY = re.compile(r"^(?:(?:noncomputable )?(?:def|abbrev|theorem|structure|inductive)\s|example\b|#|end\b|"
                      r"namespace\b|open\b|section\b|attribute\b|variable\b)")


def theorem_surface(lines):
    buf = []
    for l in lines:
        if ':=' in l:
            buf.append(l.split(':=', 1)[0]); break
        if l.rstrip().endswith(' where'):
            buf.append(l.rstrip()[:-len(' where')]); break
        buf.append(l)
    return flat('\n'.join(buf))


def chunks(code):
    """[(kind, name, lines)] for each declaration and example; a chunk ends at the next boundary line."""
    lines, out, cur = code.split('\n'), [], None
    for l in lines:
        m = DECL.match(l)
        if m or l.startswith('example'):
            cur = (m.group(1), m.group(2), [l]) if m else ('example', '', [l])
            out.append(cur)
        elif cur is not None and (BOUNDARY.match(l) or not l.strip()):
            cur = None if BOUNDARY.match(l) or cur[0] not in ('theorem', 'example') else cur
            if cur is not None:
                cur[2].append(l)
        elif cur is not None:
            cur[2].append(l)
    return out


def features(text):
    """What S1 compares: imports, namespace and open lines, declarations in order with their surfaces (a
    theorem's or example's up to its first ':=' or trailing 'where'; any other declaration's whole text up to
    a blank line), examples, prints."""
    code = uncomment(text)
    lines = [l.strip() for l in code.splitlines() if l.strip()]
    decls, examples = [], []
    for kind, name, ls in chunks(code):
        if kind in ('theorem', 'example'):
            surface = theorem_surface(ls)
        else:
            surface = flat('\n'.join(l for l in ls if l.strip()))
        (examples if kind == 'example' else decls).append((kind, name, surface))
    return {'imports': [l for l in lines if l.startswith('import ')],
            'scopes': [l for l in lines if re.match(r'(namespace|end|section)\b', l)],
            'opens': [l for l in lines if l.startswith('open ')],
            'decls': decls, 'examples': examples,
            'prints': [l for l in lines if l.startswith('#')]}


def body(text, name):
    for kind, n, ls in chunks(uncomment(text)):
        if n == name:
            joined = '\n'.join(ls)
            return joined.split(':=', 1)[1] if ':=' in joined else ''
    return None


def render_block(text):
    """The frozen-block form of a module: its code, blank lines dropped, with every theorem's and example's
    proof removed (a proof runs to the next boundary line, as in chunks())."""
    res, i, lines = [], 0, uncomment(text).split('\n')
    is_thm = lambda l: (DECL.match(l) is not None and DECL.match(l).group(1) == 'theorem') or l.startswith('example')
    while i < len(lines):
        l = lines[i]
        if is_thm(l):
            j = i
            while j < len(lines):
                if ':=' in lines[j]:
                    res.append(lines[j].split(':=', 1)[0].rstrip() + ' :='); break
                if lines[j].rstrip().endswith(' where'):
                    res.append(lines[j].rstrip()[:-len(' where')] + ' :='); break
                res.append(lines[j]); j += 1
            j += 1
            while j < len(lines) and not BOUNDARY.match(lines[j]):
                j += 1
            i = j
            continue
        if l.strip():
            res.append(l)
        i += 1
    return '\n'.join(res) + '\n'


def header_of(module):
    m = re.search(r'/-!(.*?)-/', module or '', re.S)
    return m.group(1) if m else ''


# ---------------------------------------------------------------- the controls

def s1(core, inst, surface, ns):
    """S1 surface. Returns a list of problems; [] means pass."""
    if surface is None:
        return ['frozen surface pending (no statement-surface section with two lean blocks)']
    if ns is None:
        return ['namespace pending (NS)']
    probs = []
    for label, text, block, names, imports, prints in (
            ('core', core, surface[0], CORE_NAMES, CORE_IMPORTS, CORE_PRINTS),
            ('instances', inst, surface[1], INST_NAMES, INST_IMPORTS, INST_PRINTS)):
        if not text:
            probs.append(label + ' module absent'); continue
        have, want = features(text), features(block)
        if [n for _, n, _ in want['decls']] != names:
            probs.append(label + ': frozen block does not declare the preregistration\'s names in order')
        if want['imports'] != imports or want['prints'] != ['#print axioms ' + p for p in prints]:
            probs.append(label + ': frozen block imports or prints differ from the preregistration')
        if want['scopes'] != ['namespace ' + ns, 'end ' + ns]:
            probs.append(label + ': frozen block namespace is not ' + ns)
        if label == 'instances' and len(want['examples']) != INST_EXAMPLES:
            probs.append('instances: frozen block does not carry the two examples')
        for k in ('imports', 'scopes', 'opens', 'decls', 'examples', 'prints'):
            if have[k] != want[k]:
                probs.append('%s: %s differ from the frozen block' % (label, k))
        if re.search(FORBIDDEN, uncomment(text)):
            probs.append(label + ': forbidden token')
    return probs


def s3(core, inst):
    """S3 statement-level design invariants of the preregistration. Returns a list of problems."""
    if not core or not inst:
        return ['a module is absent']
    probs, cc, ic = [], uncomment(core), uncomment(inst)
    if re.search(CORE_EXCLUDED, cc):
        probs.append('core: PSD, Hermiticity, convexity, closedness, trace, reachability or an iff appears')
    for name, fields in FIELDS.items():
        ch = [ls for k, n, ls in chunks(cc) if n == name and k == 'structure']
        got = [m.group(1) for l in (ch[0][1:] if len(ch) == 1 else []) for m in [re.match(r'^  (\w+) :', l)] if m]
        if got != fields:
            probs.append('%s fields %s, not %s' % (name, got, fields))
    hb = body(core, HEADLINE)
    arms = re.findall(r'^  \| (\w+)\b', hb or '', re.M)
    if hb is None or 'induction h with' not in hb or arms != ARMS:
        probs.append('the headline is not one induction on h with the five arms in order (%s)' % arms)
    for name, uses in COROLLARY_USES.items():
        b = body(core, name)
        if b is None or not all(re.search(r'\b%s\b' % u, b) for u in uses):
            probs.append('%s does not apply %s' % (name, ' to '.join(uses)))
    if any(mark in t for mark in RESEARCH_MARKS for t in (cc, ic)):
        probs.append('a research import or namespace remains')
    for k, n, ls in chunks(ic):
        if k in ('def', 'abbrev') and 'CarrierConeFamily' in ls[0] and re.search(r'InstAvail|reach', '\n'.join(ls)):
            probs.append('%s defines a preparation family through availability' % n)
    return probs


def s4(texts):
    return [(name, p) for name, t in texts for p in PHRASES if t and p.lower() in t.lower()]


def s2(E):
    probs = []
    for path, line, name in LANDED:
        bd, be = blob(D, path), blob(E, path)
        text = (show(E, path) or '').splitlines()
        found = len(text) >= line and re.match(r'(noncomputable )?(def|abbrev|theorem|structure|inductive) %s\b'
                                               % re.escape(name), text[line - 1])
        if bd is None or bd != be or not found:
            probs.append('%s:%d %s (blob at D %s, at E %s)' % (path, line, name, bd, be))
    return probs


def workflow(base, splices):
    if base is None or not splices:
        return None
    text = base
    for old, new in splices:
        if not old or text.count(old) != 1 or old == new:
            return None
        text = text.replace(old, new)
    return text


def pin_ok(splices, spec):
    """With the probe spec pending, False. When it names SymPy, the text the splices add installs exactly
    sympy==<pin> and names lowercase `sympy` in no other form; otherwise the splices add no sympy install."""
    if not splices or not spec:
        return False
    added = ''.join(new.replace(old, '', 1) if old in new else new for old, new in splices)
    forms = re.findall(r'\bsympy\b[=<>!~]*[\w.*]*', added)
    if spec.get('sympy'):
        return spec['sympy'] == SYMPY_PIN and bool(forms) and all(f == 'sympy==' + SYMPY_PIN for f in forms)
    return not forms


def root_expected(base):
    """D's root with ROOT_LINES inserted directly after its last import line; None when that is undefined."""
    if base is None:
        return None
    lines = base.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('import ')]
    if not idx or any(l in lines for l in ROOT_LINES):
        return None
    return '\n'.join(lines[:idx[-1] + 1] + ROOT_LINES + lines[idx[-1] + 1:])


def registry_ok(base, head, families):
    if base is None or head is None or not families:
        return False
    try:
        want = json.loads(base)
        want['families'].extend(families)
        return json.loads(head) == want
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def authorized(status, path, entries):
    cands = [e for e in entries if path == e[2] or (e[2].endswith('/') and path.startswith(e[2]))]
    if not cands:
        return False
    e = max(cands, key=lambda e: len(e[2]))
    return ('M' if status == 'T' else status) in e[1]


def g(diff_lines, entries):
    bad = []
    for ln in diff_lines:
        status, _, path = ln.partition('\t')
        if not path or not authorized(status[:1], path, entries) or path == LEGACY:
            bad.append(ln)
    return bad


def record_ok(names, files, at_e):
    rel = {n[len(RDIR):] for n in names if n.startswith(RDIR)}
    want = {'preregistration.md', 'controls.py'} | set(files) | ({'result.md'} if at_e else set())
    extra = {r for r in rel - want if not r.startswith('amendments/') and not r.startswith(FRUN)}
    frun = any(r.startswith(FRUN) for r in rel)
    return not (want - rel) and not extra and frun


def check(E, F, stage='E'):
    """Runs and prints the static controls of `stage`. Each control records its own outcome when it runs; the
    result maps exactly the codes that recorded one ({code: passed}). A code that never ran is absent, and
    verdict and main treat an absent code as failed. An unknown stage is refused."""
    if stage not in STAGES:
        raise ValueError('check: unknown stage %r (expected one of %s)' % (stage, ', '.join(STAGES)))
    outcomes = {}

    def record(code, name, ok, detail=''):
        ok = ok is True
        report(code + ' ' + name, ok, detail)
        outcomes[code] = outcomes.get(code, True) and ok

    at_e = stage == 'E'
    prereg_F, prereg_E = show(F, PREREG), show(E, PREREG)
    pf = prereg_F or ''
    record('C1', 'the preregistration at E is the one at F, with this round\'s D, declaration and #831 citation',
           prereg_F is not None and prereg_F == prereg_E and ('D: `%s`' % D) in pf
           and round_block(pf) == ROUND_BLOCK and all(c in pf for c in SUPERSEDED_CITE))
    fb = frozen_blobs(pf)
    want = FROZEN_PATHS if at_e else {CONTROLS}
    pend = sorted(p for p, b in (fb or {}).items() if b is None)
    bad = sorted(p for p in want if fb and fb.get(p) and blob(E, p) != fb[p])
    record('C2', 'the frozen execution blobs at ' + stage, fb is not None and set(fb) == FROZEN_PATHS
           and not pend and not bad, ('pending %s' % pend if pend else '') + (' differ %s' % bad if bad else ''))
    rows = retention(pf)
    ppend = sorted(l for l, (p, h) in (rows or {}).items() if p is None or h is None)
    gbad = sorted(l for l, (p, h) in (rows or {}).items() if h == GAP and l not in HISTORICAL)

    def digest_ok(p, h):
        q = resolve(p)
        t = show(E, q)
        ok = t is not None and hashlib.sha256(t.encode('utf-8')).hexdigest() == h
        # a file retained on main outside the record directory is there at D and unchanged at E
        return ok and (p.startswith('evidence/') or (blob(D, q) is not None and blob(D, q) == blob(E, q)))
    pbad = sorted(l for l, (p, h) in (rows or {}).items() if p not in (None, NONE) and h not in (None, GAP)
                  and not digest_ok(p, h))
    ngap = sum(h == GAP for _, h in (rows or {}).values())
    record('P', 'the retention rows at F: digests present at %s, gaps only on historical rows' % stage,
           rows is not None and set(rows) == EVIDENCE_ROWS and not ppend and not gbad and not pbad,
           str(ppend + gbad + pbad) if ppend or gbad or pbad else '%d digest(s), %d gap(s)' % (len(rows) - ngap, ngap))
    names = [x for x in git('ls-tree', '-r', '--name-only', E, '--', RDIR).splitlines() if x.strip()]
    record('R', 'the record directory holds exactly the frozen files, the record-relative evidence and evidence/f-run/',
           rows is not None and record_ok(names, record_files(rows or {}), at_e))
    diff = [x for x in git('diff', '--no-renames', '--name-status', D, E).splitlines() if x.strip()]
    gp = governed(pf)
    badg = g(diff, gp or [])
    record('G', 'every change from D lies in the governed paths at F; no receipt yet; the legacy manifest untouched',
           gp == GOVERNED and bool(diff) and not badg and blob(E, RECEIPT) is None
           and blob(D, LEGACY) is not None and blob(D, LEGACY) == blob(E, LEGACY),
           str(badg) if badg else '%d paths' % len(diff))
    fdelta = [x for x in git('diff', '--name-only', D, F).splitlines() if x.strip()]
    pre = [x for x in git('rev-list', '--parents', '%s..%s' % (D, F)).splitlines() if x.strip()]
    lin = [x for x in git('rev-list', '--parents', '%s..%s' % (F, E)).splitlines() if x.strip()]
    record('T', 'delta(D, F) is the control plane, drafted linearly from D without #831\'s commits; the execution '
           'is linear after F',
           PREREG in fdelta and all(p == PREREG or p.startswith(RDIR + 'amendments/') for p in fdelta)
           and bool(pre) and all(len(x.split()) == 2 for x in pre) and is_ancestor(D, F)
           and not any(x.split()[0] in OLD_CHAIN for x in pre)
           and bool(lin) and all(len(x.split()) == 2 for x in lin) and is_ancestor(F, E))
    if not at_e:
        return outcomes
    core, inst = show(E, CORE), show(E, INST)
    probs = s1(core, inst, frozen_surface(pf), NS)
    record('S1', 'surface: the two modules equal the frozen blocks', not probs, '; '.join(probs))
    probs = s2(E)
    record('S2', 'the landed objects resolve at D\'s blobs and lines', not probs, '; '.join(probs))
    probs = s3(core, inst)
    record('S3', 'the statement-level design invariants', not probs, '; '.join(probs))
    result = show(E, RESULT)
    hits = s4([('core header', header_of(core)), ('instances header', header_of(inst)), ('result note', result)])
    present = bool(header_of(core).strip()) and bool(header_of(inst).strip()) and bool((result or '').strip())
    record('S4', 'both module headers and the result note present, with no excluded phrase', present and not hits,
           str(hits) if hits else ('' if present else 'a header or the result note is absent'))
    wd, we = workflow(show(D, WORKFLOW), SPLICES), show(E, WORKFLOW)
    record('W', 'the workflow at E is D\'s with the frozen splices, installing the probe spec\'s SymPy pin',
           wd is not None and we is not None and we == wd and pin_ok(SPLICES, PROBE_SPEC),
           'splices pending (SPLICES)' if SPLICES is None else ('probe spec pending (PROBE_SPEC)' if PROBE_SPEC is None
                                                                else ''))
    rd, re_ = root_expected(show(D, ROOT)), show(E, ROOT)
    record('I', 'the two import lines after D\'s last import', rd is not None and re_ is not None and re_ == rd)
    record('J', 'the census at E is D\'s with the frozen families', registry_ok(show(D, REGISTRY), show(E, REGISTRY),
                                                                                   FAMILIES),
           'families pending (FAMILIES)' if FAMILIES is None else '')
    return outcomes


def passed(results, stage='E'):
    """True only when every code required at `stage` recorded an explicit True; absent or non-bool means failed."""
    return stage in REQUIRED and isinstance(results, dict) and all(results.get(c) is True for c in REQUIRED[stage])


def run_probe(E, *args):
    with tempfile.TemporaryDirectory() as tmp:
        arch = subprocess.run(['git', 'archive', E, PROBE], capture_output=True, check=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        r = subprocess.run([sys.executable, '-I', '-B', os.path.join(tmp, PROBE)] + list(args),
                           capture_output=True, text=True, cwd=tmp)
        return r.returncode, r.stdout, r.stderr


def probe_ok(rc, out, err, spec):
    """Q-EXACT's rule. The spec must name the probe's codes, the separate arithmetic implementation's codes, the
    check count, the mutations, the final line and the sha256 of the whole standard output (the byte replay)."""
    if not spec or not spec.get('codes') or not spec.get('independent') or not isinstance(spec.get('n'), int) \
            or not spec.get('final') or not re.fullmatch(r'[0-9a-f]{64}', spec.get('stdout_sha256') or ''):
        return False
    ok = rc == 0 and not err and not re.search(r'^FAIL\b', out, re.M)
    ok &= hashlib.sha256(out.encode('utf-8')).hexdigest() == spec['stdout_sha256']
    ok &= all(re.search(r'^PASS %s \(\d+\)$' % re.escape(c), out, re.M) for c in spec['codes'] + spec['independent'])
    if spec.get('sympy'):
        ok &= spec['sympy'] == SYMPY_PIN and re.search(r'^SYMPY %s$' % re.escape(SYMPY_PIN), out, re.M) is not None
    ok &= ('checks: %d, failures: 0' % spec['n']) in out and out.rstrip().endswith(spec['final'])
    muts = spec.get('mutations') or []
    ok &= bool(muts) and all(('REJECTED ' + m) in out for m in muts)
    ok &= ('mutations: %d rejected, 0 accepted' % len(muts)) in out
    return bool(ok)


def axioms_from(log, ns):
    rep = {}
    if not ns:
        return rep
    for m in re.finditer(r"'%s\.([\w']+)' depends on axioms: \[([^\]]*)\]" % re.escape(ns), log):
        rep.setdefault(m.group(1), set()).update(a.strip() for a in m.group(2).split(',') if a.strip())
    for m in re.finditer(r"'%s\.([\w']+)' does not depend on any axioms" % re.escape(ns), log):
        rep.setdefault(m.group(1), set())
    return rep


def cells(ax, log, exact):
    """Each cell from its own measurements; no cell reads another's outcome."""
    clean = lambda n: n in ax and ax[n] <= ALLOWED_AXIOMS
    nobad = bool(log) and not any(b in log for b in BAD_LOG)
    core = nobad and clean(HEADLINE) and all(clean(n) for n in INST_PRINTS)
    cor = nobad and clean(HEADLINE) and all(clean(n) for n in INST_PRINTS + COR_PRINTS)
    return core, cor, bool(exact)


def verdict(E, F, axlog, check_fn=None, probe_fn=None):
    """Every positive token is gated on every static control required at E: if any fails or is not reported,
    the failed controls are printed, the probe is not run, no axiom report is read, every cell prints
    NOT-ESTABLISHED, the round prints NOT-READ and the result is False. check_fn and probe_fn default to check
    and run_probe."""
    results = (check_fn or check)(E, F)
    results = results if isinstance(results, dict) else {}
    failed = [c for c in REQUIRED['E'] if results.get(c) is not True]
    if failed:
        print('STATIC CONTROLS FAILED: ' + ', '.join(failed))
        print('probe not run and axiom reports not read: a required static control failed')
        got = (False, False, False)
    else:
        rc, out, err = (probe_fn or run_probe)(E, '--self-test')
        print(out.rstrip())
        log = open(axlog, encoding='utf-8', errors='replace').read() if axlog else ''
        ax = axioms_from(log, NS)
        got = cells(ax, log, probe_ok(rc, out, err, PROBE_SPEC))
        print('axiom reports read: %d of %d prints' % (len([p for p in CORE_PRINTS + INST_PRINTS if p in ax]),
                                                      len(CORE_PRINTS + INST_PRINTS)))
    for (cell, pos, neg), ok in zip(CELLS, got):
        print('TOKEN %-7s %s' % (cell, pos if ok is True else neg))
    short = [c for (c, _, _), ok in zip(CELLS, got) if ok is not True]
    print('earned reading: %s' % ('full (every cell positive)' if not short else 'not full (%s not positive)'
                                  % ', '.join(short)))
    print('%s (static controls failed: %s)' % (NOT_READ, ', '.join(failed)) if failed else READ)
    return not failed


# ---------------------------------------------------------------- self-test fixture (synthetic, never compiled)

FIX_NS = 'OIBridge.PreservationInductionFixture'
FIX_CORE = '''import OIBridge.ImplementationLocality

/-!
Synthetic self-test fixture of controls.py: never compiled, not the adopted module.
-/

namespace {NS}

open Matrix InterventionLocality OperationalAssembly ReferenceExtension MonoidalCompletion SpectatorBridge

abbrev CarrierConeFamily :=
  ∀ (S : Type) [Fintype S] [DecidableEq S], Set (Matrix S S ℂ)

structure AdditiveClosure (C : CarrierConeFamily) : Prop where
  zero_mem : ∀ (S : Type) [Fintype S] [DecidableEq S], (0 : Matrix S S ℂ) ∈ C S
  add_mem : ∀ (S : Type) [Fintype S] [DecidableEq S] (X Y : Matrix S S ℂ),
    X ∈ C S → Y ∈ C S → X + Y ∈ C S

def PreservesCarrier (C : CarrierConeFamily) (S : Type) [Fintype S] [DecidableEq S]
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X, X ∈ C S → Φ X ∈ C S

structure PrimitivePreservation (𝓘 : ImplementationClass) (C : CarrierConeFamily) : Prop where
  op : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
    𝓘 S K → Kᴴ * K = 1 → PreservesCarrier C S (conjChannel K)
  readout : ∀ (S T : Type) [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S),
    (∀ k, 𝓘 S (Matrix.reindex e e (readProj T m k))) →
    ∀ k, PreservesCarrier C S (conjChannel (Matrix.reindex e e (readProj T m k)))

def UniformAttachPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C S → uniformAttach m X ∈ C (S × Fin m)

def AncillaDiscardPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C (S × Fin m) → ptraceAnc m X ∈ C S

theorem finite_sum_mem (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {S : Type} [Fintype S] [DecidableEq S] {ι : Type} (s : Finset ι)
    (X : ι → Matrix S S ℂ) (hX : ∀ i ∈ s, X i ∈ C S) :
    (∑ i ∈ s, X i) ∈ C S := by
  fixture_proof

theorem instAvail_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a) := by
  classical
  induction h with
  | op K hK hiso => exact fixture_op
  | readout e hP => exact fixture_readout
  | coarse f _ ih => exact finite_sum_mem C hC _ _ fixture_coarse
  | bind _ _ ihF ihG => exact fixture_bind
  | discard hm _ ih => exact hDiscard _ _ hm _ (ih a _ (hAttach _ _ hm X hX))

theorem instAvail_sum_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    PreservesCarrier C S (∑ a, F a) := by
  exact finite_sum_mem C hC _ _ fun a _ => instAvail_preserves C hC hPrim hAttach hDiscard h a

theorem instAvail_spectator_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (R : Type) [Fintype R] [DecidableEq R]
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C (R × S) (amplRefL R (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_spectator hc hl R h)

theorem instAvail_transport_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hl : LabelInvariant 𝓘)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F)
    (S' : Type) [Fintype S'] [DecidableEq S'] (e : S ≃ S') :
    ∀ a, PreservesCarrier C S' (transport e (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_transport hl h S' e)

#print axioms instAvail_preserves
#print axioms instAvail_sum_preserves
#print axioms instAvail_spectator_preserves
#print axioms instAvail_transport_preserves

end {NS}
'''
FIX_INST = '''import OIBridge.PreservationInduction
import OIBridge.StructuralClosure

/-!
Synthetic self-test fixture of controls.py: never compiled, not the adopted module.
-/

namespace {NS}

open Matrix InterventionLocality OperationalAssembly MonoidalCompletion
open scoped ComplexOrder

abbrev quantumCone : CarrierConeFamily := fun _ _ _ => {X | X.PosSemidef}

abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>
  {X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}

abbrev classicalClass : ImplementationClass := substratumClass

theorem classicalCone_iff {S : Type} [Fintype S] [DecidableEq S] (X : Matrix S S ℂ) :
    X ∈ classicalCone S ↔ ∃ d, (∀ i, 0 ≤ d i) ∧ X = Matrix.diagonal d := by
  fixture_proof

theorem quantum_additive : AdditiveClosure quantumCone where
  zero_mem := fixture_zero
  add_mem := fixture_add

theorem quantum_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) :
    PreservesCarrier quantumCone S (conjChannel K) := by
  fixture_proof

theorem quantum_primitive (𝓘 : ImplementationClass) : PrimitivePreservation 𝓘 quantumCone where
  op := fixture_op
  readout := fixture_readout

def attachBlock {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) : Matrix (S × Fin m) (S × Fin m) ℂ :=
  let P := Matrix.diagonal (fun p : S × Fin m => if p.2 = e then (1 : ℂ) else 0)
  P * X.submatrix Prod.fst Prod.fst * Pᴴ

theorem attachBlock_apply {S : Type} [Fintype S] [DecidableEq S] (m : ℕ) (e : Fin m)
    (X : Matrix S S ℂ) (p q : S × Fin m) :
    attachBlock m e X p q = if p.2 = e ∧ q.2 = e then X p.1 q.1 else 0 := by
  fixture_proof

theorem uniformAttach_eq_blocks {S : Type} [Fintype S] [DecidableEq S] (m : ℕ) (X : Matrix S S ℂ) :
    uniformAttach m X = (m : ℂ)⁻¹ • ∑ e : Fin m, attachBlock m e X := by
  fixture_proof

theorem quantum_attach : UniformAttachPreservation quantumCone := by
  fixture_proof

theorem ptraceAnc_eq_blocks {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (X : Matrix (S × Fin m) (S × Fin m) ℂ) :
    ptraceAnc m X = ∑ e : Fin m, X.submatrix (fun s => (s, e)) (fun s => (s, e)) := by
  fixture_proof

theorem quantum_discard : AncillaDiscardPreservation quantumCone := by
  fixture_proof

theorem quantum_instAvail {𝓘 : ImplementationClass}
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) :=
  instAvail_preserves quantumCone quantum_additive (quantum_primitive 𝓘) quantum_attach quantum_discard h

theorem quantum_fullClass {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail fullClass S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) := quantum_instAvail h

theorem classical_additive : AdditiveClosure classicalCone where
  zero_mem := fixture_zero
  add_mem := fixture_add

theorem classical_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) (hK : classicalClass S K) :
    PreservesCarrier classicalCone S (conjChannel K) := by
  fixture_proof

theorem classical_primitive : PrimitivePreservation classicalClass classicalCone where
  op := fixture_op
  readout := fixture_readout

theorem classical_attach : UniformAttachPreservation classicalCone := by
  fixture_proof

theorem classical_discard : AncillaDiscardPreservation classicalCone := by
  fixture_proof

theorem classical_readProj {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S) (k : Fin m) :
    classicalClass S (Matrix.reindex e e (readProj T m k)) := by
  fixture_proof

theorem classical_instAvail {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail classicalClass S O F) :
    ∀ a, PreservesCarrier classicalCone S (F a) :=
  instAvail_preserves classicalCone classical_additive classical_primitive classical_attach classical_discard h

theorem classical_native_readout {S T : Type} [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S) :
    ∀ k, PreservesCarrier classicalCone S (conjChannel (Matrix.reindex e e (readProj T m k))) := by
  fixture_proof

example : ContextStable classicalClass := substratumClass_contextStable
example : LabelInvariant classicalClass := substratumClass_labelInvariant

#print axioms quantum_instAvail
#print axioms classical_instAvail
#print axioms quantum_attach
#print axioms quantum_discard
#print axioms classical_readProj
#print axioms classical_native_readout

end {NS}
'''
FIX_SPLICES = [('    needs: [probes_a]\n', '    needs: [probes_a, probes_preserveinduct1]\n'),
               ('jobs:\n', 'jobs:\n  probes_preserveinduct1:\n    runs-on: fixture\n'
                '    steps:\n      - run: python -m pip install sympy==1.14.0\n')]
FIX_FAMILIES = [{'name': 'fixture family (synthetic)', 'modules': ['PreservationInduction',
                                                                   'PreservationInductionInstances'],
                 'status': 'kernel-only', 'manuscript': [], 'note': 'synthetic'}]
FIX_PROBE_OUT = 'SYMPY 1.14.0\nPASS FIX1 (3)\nPASS FIX2 (3)\nPASS IND1 (1)\nchecks: 7, failures: 0\n' \
                'REJECTED m1: FIX1\nmutations: 1 rejected, 0 accepted\nVERDICT FIXTURE\n'
FIX_SPEC = {'codes': ['FIX1', 'FIX2'], 'independent': ['IND1'], 'n': 7, 'mutations': ['m1: FIX1'],
            'final': 'VERDICT FIXTURE', 'sympy': '1.14.0',
            'stdout_sha256': hashlib.sha256(FIX_PROBE_OUT.encode('utf-8')).hexdigest()}


def git_blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def fix_log(ns, names, axioms='propext, Classical.choice, Quot.sound'):
    return '\n'.join("info: x.lean:1:0: '%s.%s' depends on axioms: [%s]" % (ns, n, axioms) for n in names) + '\n'


def set_row(prereg, label, file_cell, sha_cell):
    """Rewrite the retention row `label` with the given cells."""
    return re.sub(r'^\| `%s` \|[^\n]*$' % re.escape(label), lambda m: '| `%s` | %s | %s |' % (label, file_cell, sha_cell),
                  prereg, count=1, flags=re.M)


def fill(prereg, title, values):
    """Replace each pending cell of the pin table `title` by `values[path]`."""
    for path, v in values.items():
        prereg = re.sub(r'(\| `%s` \| )pending[^|\n]*\|' % re.escape(path), lambda m: m.group(1) + '`%s` |' % v,
                        prereg)
    return prereg


def fake_repo(prereg, src):
    """An in-memory D, F, E: D holds synthetic shared files, F adds the preregistration with every pending pin
    filled and a statement-surface section built from the fixture modules, and E holds the fixture execution:
    the two modules, a stub probe, this source, evidence files, an f-run file and a result note. Every file is
    synthetic and labelled as such; none is run evidence."""
    core, inst = FIX_CORE.replace('{NS}', FIX_NS), FIX_INST.replace('{NS}', FIX_NS)
    landed = {}
    for path, line, name in LANDED:
        landed.setdefault(path, {})[line] = 'def %s : fixture' % name
    Dm = {p: '\n'.join(v.get(i, '-- synthetic filler') for i in range(1, max(v) + 2)) + '\n' for p, v in landed.items()}
    Dm[WORKFLOW] = 'jobs:\n  probes_a:\n    runs-on: fixture\n  aggregate:\n    needs: [probes_a]\n'
    Dm[ROOT] = 'import OIBridge.A\nimport OIBridge.B\n\nnamespace OIBridge\n'
    Dm[REGISTRY] = json.dumps({'families': [{'name': 'x', 'modules': ['A']}]}, indent=2) + '\n'
    Dm[LEGACY] = '{"synthetic": true}\n'
    E = dict(Dm)
    E[CORE], E[INST] = core, inst
    E[PROBE] = '# synthetic stub probe; the self-test never runs it\n'
    E[CONTROLS] = src
    rows = {}
    for label in sorted(retention(prereg) or {}):
        p = 'evidence/%s.json' % label
        E[RDIR + p] = '{"synthetic": "controls self-test fixture, not run evidence", "row": "%s"}\n' % label
        rows[label] = (p, hashlib.sha256(E[RDIR + p].encode('utf-8')).hexdigest())
    E[RDIR + FRUN + 'f-run.json'] = '{"synthetic": "fixture"}\n'
    E[RESULT] = '# PRESERVE-INDUCT-1 result (synthetic self-test fixture)\n\nNo claim.\n'
    E[WORKFLOW] = workflow(Dm[WORKFLOW], FIX_SPLICES)
    E[ROOT] = root_expected(Dm[ROOT])
    reg = json.loads(Dm[REGISTRY]); reg['families'].extend(FIX_FAMILIES)
    E[REGISTRY] = json.dumps(reg, indent=2) + '\n'
    pf = fill(prereg, 'Frozen execution blobs.', {p: git_blob_id(E[p]) for p in FROZEN_PATHS})
    for label, (p, h) in rows.items():
        pf = set_row(pf, label, '`%s`' % p, '`%s`' % h)
    pf += '\n## The statement surface (frozen; synthetic fixture)\n\n```lean\n%s```\n\n```lean\n%s```\n' % (
        render_block(core), render_block(inst))
    Fm = dict(Dm); Fm[PREREG] = pf
    E[PREREG] = pf
    return {'D': Dm, 'F': Fm, 'E': E, 'flags': {'pre': 'F D', 'lin': 'E S1\nS1 F', 'anc': True}}


def install_fake(mod, repo):
    key = lambda c: 'D' if c == D else c
    mod.show = lambda c, p: repo[key(c)].get(p)
    mod.blob = lambda c, p: git_blob_id(repo[key(c)][p]) if repo[key(c)].get(p) is not None else None
    mod.is_ancestor = lambda a, b: repo['flags']['anc']

    def fgit(*args):
        if args[0] == 'ls-tree':
            return '\n'.join(sorted(p for p, t in repo[key(args[3])].items() if t is not None and p.startswith(args[5])))
        if args[:3] == ('diff', '--no-renames', '--name-status'):
            a, b = repo[key(args[3])], repo[key(args[4])]
            rows = [('A\t' if a.get(p) is None else 'M\t') + p for p in sorted(b) if b[p] is not None
                    and a.get(p) != b[p]]
            return '\n'.join(rows + ['D\t' + p for p in sorted(a) if a[p] is not None and b.get(p) is None])
        if args[:2] == ('diff', '--name-only'):
            a, b = repo[key(args[2])], repo[key(args[3])]
            return '\n'.join(p for p in sorted(set(a) | set(b)) if a.get(p) != b.get(p))
        if args[:2] == ('rev-list', '--parents'):
            return repo['flags']['pre' if args[2].endswith('..F') else 'lin']
        raise ValueError('fake git: unsupported ' + ' '.join(args))
    mod.git = fgit


def load(src, name, params=True, **override):
    """The module built from src, with the fixture's parameters (params True) or every PENDING one unset."""
    mod = types.ModuleType(name)
    mod.__file__ = __file__
    exec(compile(src, name, 'exec'), mod.__dict__)
    if params:
        mod.NS, mod.SPLICES, mod.FAMILIES, mod.PROBE_SPEC = FIX_NS, FIX_SPLICES, FIX_FAMILIES, FIX_SPEC
    else:
        mod.NS = mod.SPLICES = mod.FAMILIES = mod.PROBE_SPEC = None
    for k, v in override.items():
        setattr(mod, k, v)
    return mod


def end_to_end(src, repo, axlog, params=True, **override):
    """check() then verdict() of the module built from src, on the fake repo; (ok, output, probe calls)."""
    mod = load(src, 'controls_e2e', params, **override)
    install_fake(mod, repo)
    calls = []

    def probe(E, *a):
        calls.append(E)
        return 0, FIX_PROBE_OUT, ''
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ok = mod.verdict('E', 'F', axlog, probe_fn=probe)
    return ok, buf.getvalue(), len(calls)


def drop_record(src, code):
    """Source mutation: remove the record call of `code` inside check(), whole statement, replaced by `pass`."""
    start = src.index('def check(E, F')
    i = src.index("record('%s'," % code, start)
    depth, j = 0, i + len('record')
    while True:
        ch = src[j]
        depth += ch == '('
        depth -= ch == ')'
        j += 1
        if depth == 0:
            break
    return src[:i] + 'pass' + src[j:]


def failed_named(out, codes):
    m = re.search(r'^STATIC CONTROLS FAILED: (.*)$', out, re.M)
    return m is not None and all(c in m.group(1).split(', ') for c in codes)


def leaked(out):
    return [t for t in POSITIVE if has_token(out, t)]


def e2e_cases(prereg):
    """The real check() through verdict(): unmutated; each control's record call removed; each control's inputs
    absent; the shipped (pending) parameters; main()'s exits and stage handling. Returns (problems, cases)."""
    src = open(__file__, encoding='utf-8').read()
    problems, n = [], 0
    repo = fake_repo(prereg, src)
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'bridge.log')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(fix_log(FIX_NS, CORE_PRINTS + INST_PRINTS))
        n += 1
        ok, out, calls = end_to_end(src, repo, path)
        if not ok or calls != 1 or leaked(out) != POSITIVE or re.search(r'^FAIL ', out, re.M):
            problems.append('unmutated: result %s, probe calls %d, positive %s, failures %s' % (
                ok, calls, leaked(out), re.findall(r'^FAIL .*$', out, re.M)))
        for code in REQUIRED['E']:
            n += 1
            if src[src.index('def check(E, F'):].count("record('%s'," % code) != 1:
                problems.append('%s: not exactly one record call in check()' % code); continue
            ok, out, calls = end_to_end(drop_record(src, code), repo, path)
            if ok or leaked(out) or not failed_named(out, [code]) or calls:
                problems.append('%s record removed: result %s, positive %s, named %s, probe calls %d'
                                % (code, ok, leaked(out), failed_named(out, [code]), calls))

        def variant(edit):
            r = {k: dict(v) for k, v in repo.items()}
            edit(r)
            return r

        def drop(*spec):
            def ed(r):
                for c, p in spec:
                    r[c][p] = None
            return ed

        def prereg_edit(f):
            def ed(r):
                r['F'][PREREG] = r['E'][PREREG] = f(r['F'][PREREG])
            return ed
        def gapped(r, labels, keep=False):
            for c in ('F', 'E'):
                for label in labels:
                    r[c][PREREG] = set_row(r[c][PREREG], label, 'none', 'gap: log not recoverable (fixture)')
            if not keep:
                for label in labels:
                    r['E'][RDIR + 'evidence/%s.json' % label] = None

        def archived(r, labels, at_d=True):
            for label in labels:
                a = 'verification/audits/evidence-retention/fixture/%s.json' % label
                body = '{"synthetic": "archived fixture, not run evidence", "row": "%s"}\n' % label
                r['E'][a] = body
                if at_d:
                    r['D'][a] = r['F'][a] = body
                r['E'][RDIR + 'evidence/%s.json' % label] = None
                for c in ('F', 'E'):
                    r[c][PREREG] = set_row(r[c][PREREG], label, '`%s`' % a,
                                           '`%s`' % hashlib.sha256(body.encode('utf-8')).hexdigest())
        ev = sorted(p for p in repo['E'] if p.startswith(RDIR + 'evidence/') and not p.startswith(RDIR + FRUN))[:1]
        frun = [p for p in repo['E'] if p.startswith(RDIR + FRUN)]
        strip_hdr = lambda t: re.sub(r'/-!.*?-/\n', '', t, count=1, flags=re.S)
        cut = lambda title: (lambda t: re.sub(r'\*\*%s\*\*.*?\n\n(?:\|.*\n)+' % re.escape(title), '', t, count=1,
                                              flags=re.S))
        absences = [
            ('the preregistration absent at F and E', ['C1'], drop(('F', PREREG), ('E', PREREG))),
            ('the frozen-blob table absent', ['C2'], prereg_edit(cut('Frozen execution blobs.'))),
            ('the retained-evidence table absent', ['P', 'R'], prereg_edit(cut('Retained evidence (§A.42).'))),
            ('the statement-surface section absent', ['S1'],
             prereg_edit(lambda t: t[:t.index('\n## The statement surface (frozen')] + '\n')),
            ('the governed-path block absent', ['G'],
             prereg_edit(lambda t: re.sub(r'```v3-governed-paths\n.*?```\n', '', t, count=1, flags=re.S))),
            ('a landed file absent at D and E', ['S2'], drop(('D', LANDED[0][0]), ('E', LANDED[0][0]))),
            ('the core module absent at E', ['S1', 'S3'], drop(('E', CORE))),
            ('the instances header absent', ['S4'], lambda r: r['E'].__setitem__(INST, strip_hdr(r['E'][INST]))),
            ('the result note absent at E', ['S4', 'R'], drop(('E', RESULT))),
            ('the workflow absent at D and E', ['W'], drop(('D', WORKFLOW), ('E', WORKFLOW))),
            ('OIBridge.lean absent at D and E', ['I'], drop(('D', ROOT), ('E', ROOT))),
            ('the census absent at D and E', ['J'], drop(('D', REGISTRY), ('E', REGISTRY))),
            ('a pinned evidence file absent at E', ['P'], drop(*[('E', e) for e in ev])),
            ('evidence/f-run/ absent at E', ['R'], drop(*[('E', e) for e in frun])),
            ('E identical to D', ['G'], lambda r: r.__setitem__('E', dict(r['D']))),
            ('no execution commit after F', ['T'], lambda r: r['flags'].__setitem__('lin', '')),
            ('the legacy manifest absent at D and E', ['G'], drop(('D', LEGACY), ('E', LEGACY))),
            ('the predicted-tree row recorded as a gap', ['P'], lambda r: gapped(r, [REQUIRED_PIN])),
            ('a historical gap whose file stays in the record directory', ['R'],
             lambda r: gapped(r, sorted(HISTORICAL)[:1], keep=True)),
            ('a retention row dropped', ['P'], prereg_edit(lambda t: re.sub(
                r'^\| `%s` \|[^\n]*\n' % re.escape(REQUIRED_PIN), '', t, count=1, flags=re.M))),
            ('a historical row retained outside the record directory but absent at D', ['P'],
             lambda r: archived(r, sorted(HISTORICAL)[:1], at_d=False)),
            ('the #831 citation removed', ['C1'], prereg_edit(lambda t: t.replace(SUPERSEDED_CITE[1], '#831'))),
            ('an old #831 commit in the drafting chain', ['T'], lambda r: r['flags'].__setitem__(
                'pre', 'F %s\n%s D' % (sorted(OLD_CHAIN)[1], sorted(OLD_CHAIN)[1]))),
        ]
        for name, codes, edit in absences:
            n += 1
            ok, out, calls = end_to_end(src, variant(edit), path)
            if ok or calls or not failed_named(out, codes) or leaked(out):
                problems.append('%s: result %s, %s named %s, probe calls %d, positive %s'
                                % (name, ok, codes, failed_named(out, codes), calls, leaked(out)))
        # frozen splices that install SymPy unpinned, applied faithfully at E: W must still fail
        n += 1
        loose = [(o, nw.replace('sympy==1.14.0', 'sympy')) for o, nw in FIX_SPLICES]
        lrepo = variant(lambda r: r['E'].__setitem__(WORKFLOW, workflow(r['D'][WORKFLOW], loose)))
        ok, out, calls = end_to_end(src, lrepo, path, SPLICES=loose)
        if ok or calls or not failed_named(out, ['W']) or leaked(out):
            problems.append('unpinned SymPy splices: result %s, W named %s, probe calls %d' % (
                ok, failed_named(out, ['W']), calls))
        # historical rows recorded as gaps, or retained on main before D: passing states
        for label, edit in (('historical gaps', lambda r: gapped(r, sorted(HISTORICAL))),
                            ('historical rows retained on main at D', lambda r: archived(r, sorted(HISTORICAL)))):
            n += 1
            ok, out, calls = end_to_end(src, variant(edit), path)
            if not ok or calls != 1 or leaked(out) != POSITIVE:
                problems.append('%s: result %s, probe calls %d, positive %s, failures %s' % (
                    label, ok, calls, leaked(out), re.findall(r'^FAIL .*$', out, re.M)))
        # the pending state: the live preregistration as it stands, and every PENDING parameter unset
        n += 1
        shipped = variant(prereg_edit(lambda t: prereg))
        ok, out, calls = end_to_end(src, shipped, path, params=False)
        if ok or calls or not failed_named(out, ['C2', 'S1', 'W', 'J', 'P']) or leaked(out):
            problems.append('pending state: result %s, probe calls %d, positive %s' % (ok, calls, leaked(out)))
        # main(): exits, a record call removed, stage handling, unknown arguments
        mods = {'plain': load(src, 'controls_main'), 'dropped': load(drop_record(src, 'T'), 'controls_main_t'),
                'stage1': load(src, 'controls_main_s1')}
        for which, m in mods.items():
            install_fake(m, variant(drop(('E', RESULT))) if which == 'stage1' else repo)
        main_cases = [('plain', ['check', 'E', '--freeze', 'F'], 0),
                      ('stage1', ['check', 'E', '--freeze', 'F', '--stage', 'S1'], 0),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage', 'S1'], 1),
                      ('dropped', ['check', 'E', '--freeze', 'F'], 1),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage', 'e'], 2),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stage'], 2),
                      ('plain', ['check', 'E', '--freeze', 'F', '--stgae', 'S1'], 2),
                      ('plain', ['verdict', 'E', '--freeze', 'F', '--axioms'], 2)]
        for which, argv, want in main_cases:
            n += 1
            m = mods[which]
            del m.FAIL[:]
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    got = m.main(argv)
            except Exception as e:  # a refusal must be an exit status, not an exception
                got = '%s: %s' % (type(e).__name__, e)
            if got != want:
                problems.append('main %s %s: exit %s, expected %s' % (which, ' '.join(argv), got, want))
        n += 1
        m = load(src, 'controls_stage')
        install_fake(m, repo)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                m.check('E', 'F', 'e')
            problems.append("check() accepted the unknown stage 'e'")
        except ValueError:
            pass
    return problems, n


def verdict_regression():
    """Through verdict() itself, with injected static results: each required control failing alone, one left
    unreported, a non-bool value, and the all-clean case. Returns (problems, cases)."""
    problems = []
    mod = load(open(__file__, encoding='utf-8').read(), 'controls_vr')
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'bridge.log')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(fix_log(FIX_NS, CORE_PRINTS + INST_PRINTS))

        def run(results, log=path):
            buf, calls = io.StringIO(), []
            with contextlib.redirect_stdout(buf):
                ok = mod.verdict('E', 'F', log, check_fn=lambda E, F: dict(results),
                                 probe_fn=lambda E, *a: calls.append(E) or (0, FIX_PROBE_OUT, ''))
            return ok, buf.getvalue(), len(calls)
        clean = {c: True for c in REQUIRED['E']}
        ok, out, calls = run(clean)
        if not ok or leaked(out) != POSITIVE or calls != 1:
            problems.append('all-clean: result %s, positive %s, probe calls %d' % (ok, leaked(out), calls))
        cases = [(c, dict(clean, **{c: False})) for c in REQUIRED['E']]
        cases.append(('C2', {c: True for c in REQUIRED['E'] if c != 'C2'}))
        cases.append(('S3', dict(clean, S3=1)))
        for name, results in cases:
            ok, out, calls = run(results)
            if ok or leaked(out) or calls or not failed_named(out, [name]):
                problems.append('%s failing: result %s, positive %s, probe calls %d' % (name, ok, leaked(out), calls))
        # each cell reads its own measurements: a dirty instance report fails Q-CORE and Q-COR, not Q-EXACT
        dirty = os.path.join(tmp, 'dirty.log')
        with open(dirty, 'w', encoding='utf-8') as fh:
            fh.write(fix_log(FIX_NS, CORE_PRINTS + INST_PRINTS[1:]) + fix_log(FIX_NS, INST_PRINTS[:1], 'sorryAx'))
        ok, out, _ = run(clean, dirty)
        if not ok or leaked(out) != [CELLS[2][1], READ]:
            problems.append('dirty instance report: positive %s' % leaked(out))
        for label, text in (('instance report with an extra axiom', fix_log(FIX_NS, CORE_PRINTS + INST_PRINTS[1:])
                             + fix_log(FIX_NS, INST_PRINTS[:1], 'propext, Classical.choice, Quot.sound, oops')),
                            ('instance report missing', fix_log(FIX_NS, CORE_PRINTS + INST_PRINTS[1:]))):
            fp = os.path.join(tmp, 'inst.log')
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(text)
            ok, out, _ = run(clean, fp)
            if not ok or leaked(out) != [CELLS[2][1], READ]:
                problems.append('%s: positive %s' % (label, leaked(out)))
        cor_dirty = os.path.join(tmp, 'cor.log')
        with open(cor_dirty, 'w', encoding='utf-8') as fh:
            fh.write(fix_log(FIX_NS, [p for p in CORE_PRINTS + INST_PRINTS if p != COR_PRINTS[2]]))
        ok, out, _ = run(clean, cor_dirty)
        if not ok or leaked(out) != [CELLS[0][1], CELLS[2][1], READ]:
            problems.append('missing corollary report: positive %s' % leaked(out))
        ok, out, _ = run(clean, None)
        if not ok or leaked(out) != [CELLS[2][1], READ]:
            problems.append('no axiom log: positive %s' % leaked(out))
        head_dirty = os.path.join(tmp, 'head.log')
        with open(head_dirty, 'w', encoding='utf-8') as fh:
            fh.write(fix_log(FIX_NS, CORE_PRINTS[1:] + INST_PRINTS) + fix_log(FIX_NS, [HEADLINE], 'propext, oops'))
        ok, out, _ = run(clean, head_dirty)
        if not ok or leaked(out) != [CELLS[2][1], READ] or 'earned reading: not full (Q-CORE, Q-COR' not in out:
            problems.append('dirty headline report: positive %s' % leaked(out))
        # a failing probe leaves the Lean cells positive and the earned reading not full
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ok = mod.verdict('E', 'F', path, check_fn=lambda E, F: dict(clean),
                             probe_fn=lambda E, *a: (0, FIX_PROBE_OUT.replace('PASS IND1 (1)', 'FAIL IND1'), ''))
        out = buf.getvalue()
        if not ok or leaked(out) != [CELLS[0][1], CELLS[1][1], READ] or 'earned reading: not full (Q-EXACT' not in out:
            problems.append('failing probe: positive %s' % leaked(out))
        ok, out, _ = run(clean)
        if 'earned reading: full (every cell positive)' not in out:
            problems.append('all-clean: the earned reading is not full')
    return problems, len(REQUIRED['E']) + 11


def in_decl(text, name, old, new):
    """Replace old by new once, inside the declaration `name` only."""
    m = re.search(r'^(?:theorem|def|abbrev|structure) %s\b' % re.escape(name), text, re.M)
    if not m:
        return text
    rest = text[m.end():]
    k = re.search(r'^(?:(?:noncomputable )?(?:def|abbrev|theorem|structure)\s|example\b|#)', rest, re.M)
    end = m.end() + (k.start() if k else len(rest))
    return text[:m.start()] + text[m.start():end].replace(old, new, 1) + text[end:]


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, '..', '..', '..', '..', '..'))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    report('self: D agrees with the preregistration', ('D: `%s`' % D) in prereg)
    report('self: the round declaration parses', round_block(prereg) == ROUND_BLOCK)
    report('self: the governed-path block equals the frozen eight entries', governed(prereg) == GOVERNED)
    fb = frozen_blobs(prereg)
    report('self: the frozen-blob table names the four execution files', fb is not None and set(fb) == FROZEN_PATHS,
           '%s rows, %d pending' % (len(fb or {}), sum(v is None for v in (fb or {}).values())))
    rows = retention(prereg)
    report('self: the retention table parses into the three frozen rows', rows is not None and set(rows) == EVIDENCE_ROWS,
           '%d rows, %d pending' % (len(rows or {}), sum(p is None or h is None for p, h in (rows or {}).values())))
    report('self: the drafting decision\'s citation of 65b85147 and link to #831 are present',
           all(c in prereg for c in SUPERSEDED_CITE))
    report("self: the preregistration's S2 table equals LANDED", landed_table(prereg) == LANDED)
    live = []
    for path, line, name in LANDED:
        try:
            l = open(os.path.join(root, path), encoding='utf-8').read().splitlines()[line - 1]
        except (OSError, IndexError):
            l = ''
        if not re.match(r'(noncomputable )?(def|abbrev|theorem|structure|inductive) %s\b' % re.escape(name), l):
            live.append('%s:%d' % (path, line))
    report('self: every landed object resolves in this tree (%d)' % len(LANDED), not live, ', '.join(live))
    report('self: every surface name, print and token is named in the preregistration',
           all(('`%s`' % n) in prereg for n in CORE_NAMES + INST_NAMES + CORE_PRINTS + INST_PRINTS + POSITIVE
               + [READ, NOT_READ] + [c[2] for c in CELLS] + list(PENDING) + sorted(EVIDENCE_ROWS)))
    unset = [p for p in PENDING if globals()[p] is None]
    report('self: every PENDING parameter is set, or a frozen blob is still pending here',
           not unset or any(v is None for v in (fb or {}).values()), 'unset: ' + ', '.join(unset) if unset else '')
    core, inst = FIX_CORE.replace('{NS}', FIX_NS), FIX_INST.replace('{NS}', FIX_NS)
    surf = (render_block(core), render_block(inst))
    report('self: S1 accepts the fixture against its frozen blocks', s1(core, inst, surf, FIX_NS) == [])
    report('self: S1 fails closed with the surface or the namespace pending',
           bool(s1(core, inst, None, FIX_NS)) and bool(s1(core, inst, surf, None)))
    report('self: S3 accepts the fixture', s3(core, inst) == [])
    s1m = [
        ('hDiscard dropped from the headline', 'c', lambda t: in_decl(t, HEADLINE,
            '(hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)',
            '(hAttach : UniformAttachPreservation C)')),
        ('0 < m dropped from UniformAttachPreservation', 'c', lambda t: in_decl(t, 'UniformAttachPreservation',
            '(m : ℕ), 0 < m →', '(m : ℕ),')),
        ('the transport conclusion moved to the source carrier', 'c', lambda t: in_decl(
            t, 'instAvail_transport_preserves', "PreservesCarrier C S' (transport", 'PreservesCarrier C S (transport')),
        ('the headline restricted to fullClass', 'c', lambda t: in_decl(t, HEADLINE, '{𝓘 : ImplementationClass} (hPrim',
                                                                        '(hPrim')),
        ('quantum_instAvail restricted to fullClass', 'i', lambda t: in_decl(t, 'quantum_instAvail',
            'InstAvail 𝓘 S O F', 'InstAvail fullClass S O F')),
        ('an extra print', 'c', lambda t: t.replace('#print axioms instAvail_preserves\n',
                                                    '#print axioms instAvail_preserves\n#print axioms finite_sum_mem\n', 1)),
        ('a second import', 'c', lambda t: t.replace('import OIBridge.ImplementationLocality\n',
                                                     'import OIBridge.ImplementationLocality\nimport OIBridge.X\n', 1)),
        ('an example dropped', 'i', lambda t: t.replace('example : LabelInvariant classicalClass := '
                                                        'substratumClass_labelInvariant\n', '', 1)),
        ('a sorry in a proof', 'c', lambda t: t.replace('  fixture_proof\n', '  sorry\n', 1)),
        ('an open line changed', 'i', lambda t: t.replace('open scoped ComplexOrder\n', '', 1)),
        ('the classical cone redefined', 'i', lambda t: t.replace('{X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}',
                                                                  '{X | ∃ d, X = Matrix.diagonal d}', 1)),
    ]
    for name, which, f in s1m:
        mc, mi = (f(core), inst) if which == 'c' else (core, f(inst))
        report('self: S1 rejects: ' + name, (mc, mi) != (core, inst) and bool(s1(mc, mi, surf, FIX_NS)))
    s3m = [
        ('PSD used in a core proof', 'c', lambda t: t.replace('  fixture_proof\n',
                                                              '  have _ := Matrix.PosSemidef.zero\n', 1)),
        ('the discard arm removed', 'c', lambda t: t.replace(
            '  | discard hm _ ih => exact hDiscard _ _ hm _ (ih a _ (hAttach _ _ hm X hX))\n', '', 1)),
        ('the coarse and bind arms swapped', 'c', lambda t: t.replace('  | coarse f _ ih => ', '  | coarseX ', 1)
         .replace('  | bind _ _ ihF ihG => ', '  | coarse f _ ih => ', 1).replace('  | coarseX ', '  | bind _ _ ihF ihG => ', 1)),
        ('the transport corollary not built from instAvail_transport', 'c', lambda t: t.replace(
            '(instAvail_transport hl h S\' e)', '(fixture_transport hl h S\' e)', 1)),
        ('the spectator corollary not built from the headline', 'c', lambda t: t.replace(
            '  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_spectator',
            '  fixture_headline C hC hPrim hAttach hDiscard (instAvail_spectator', 1)),
        ('a research namespace left in the instances', 'i', lambda t: t.replace(
            'open scoped ComplexOrder\n', 'open scoped ComplexOrder\nopen OIBridge.PreservationInductionDesign\n', 1)),
        ('a third AdditiveClosure field', 'c', lambda t: t.replace(
            '    X ∈ C S → Y ∈ C S → X + Y ∈ C S\n',
            '    X ∈ C S → Y ∈ C S → X + Y ∈ C S\n  smul_mem : ∀ (S : Type), True\n', 1)),
    ]
    for name, which, f in s3m:
        mc, mi = (f(core), inst) if which == 'c' else (core, f(inst))
        report('self: S3 rejects: ' + name, (mc, mi) != (core, inst) and bool(s3(mc, mi)))
    reach = inst.replace('abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>',
                         'abbrev classicalCone : CarrierConeFamily := fun S _ _ => {X | InstAvail X} ∪', 1)
    report('self: S3 rejects a preparation family defined through availability', reach != inst and bool(s3(core, reach)))
    report('self: S4 flags each excluded phrase and passes the fixture headers',
           all(s4([('x', 'Here ' + p + '.')]) for p in PHRASES) and not s4([('h', header_of(core)),
                                                                              ('h', header_of(inst))]))
    wbase = 'jobs:\n  probes_a:\n    runs-on: fixture\n  aggregate:\n    needs: [probes_a]\n'
    report('self: W applies the splices once each, and fails closed with none, an absent base or a lost anchor',
           workflow(wbase, FIX_SPLICES) is not None and workflow(wbase, None) is None and workflow(None, FIX_SPLICES)
           is None and workflow(wbase.replace('needs: [probes_a]', 'needs: []'), FIX_SPLICES) is None)
    rbase = 'import OIBridge.A\nimport OIBridge.B\n\nnamespace OIBridge\n'
    report('self: I inserts both lines after the last import, and refuses a base already carrying one',
           root_expected(rbase) == 'import OIBridge.A\nimport OIBridge.B\n' + '\n'.join(ROOT_LINES) +
           '\n\nnamespace OIBridge\n' and root_expected(rbase + ROOT_LINES[0] + '\n') is None
           and root_expected(None) is None)
    jb = json.dumps({'families': [{'name': 'x'}]})
    jh = json.dumps({'families': [{'name': 'x'}] + FIX_FAMILIES})
    report('self: J accepts the families and rejects a changed status, none, or an absent base',
           registry_ok(jb, jh, FIX_FAMILIES) and not registry_ok(jb, jh.replace('kernel-only', 'current'), FIX_FAMILIES)
           and not registry_ok(jb, jb, []) and not registry_ok(None, jh, FIX_FAMILIES))
    bad = g(['M\tpapers/GR.md', 'M\t' + LEGACY, 'M\tverification/ROADMAP.md', 'A\t' + CORE, 'A\t' + RDIR + 'x',
             'M\t' + CORE, 'D\t' + WORKFLOW, 'M\t' + LP + 'ImplementationLocality.lean'], GOVERNED)
    gwant = ['M\tpapers/GR.md', 'M\t' + LEGACY, 'M\tverification/ROADMAP.md', 'M\t' + CORE, 'D\t' + WORKFLOW,
             'M\t' + LP + 'ImplementationLocality.lean']
    report('self: G authorizes by status letter and longest prefix', bad == gwant, '' if bad == gwant else str(bad))
    dig = {l: ('evidence/%s.json' % l, '0' * 64) for l in EVIDENCE_ROWS}
    files = record_files(dig)
    names = [RDIR + n for n in ['preregistration.md', 'controls.py', 'result.md', FRUN + 'x'] + sorted(files)]
    gapd = dict(dig, **{h: (NONE, GAP) for h in HISTORICAL})
    arch = dict(dig, **{h: ('verification/audits/evidence-retention/x/%s.json' % h, '0' * 64) for h in HISTORICAL})
    hist_files = {'evidence/%s.json' % h for h in HISTORICAL}
    report('self: R requires the frozen files, the record-relative digest rows\' files, f-run and (at E) the result '
           'note, and nothing else; a gap row or a file retained on main names no record file',
           len(files) == 3 and record_ok(names, files, True) and not record_ok(names + [RDIR + 'extra.md'], files, True)
           and not record_ok([x for x in names if FRUN not in x], files, True)
           and not record_ok([x for x in names if not x.endswith('result.md')], files, True)
           and record_ok([x for x in names if not x.endswith('result.md')], files, False)
           and record_files(gapd) == record_files(arch) == {'evidence/%s.json' % REQUIRED_PIN}
           and record_ok([x for x in names if x[len(RDIR):] not in hist_files], record_files(gapd), True)
           and not record_ok(names, record_files(gapd), True))
    report('self: the probe rule accepts the frozen shape and fails closed with no spec, a code missing or stderr',
           probe_ok(0, FIX_PROBE_OUT, '', FIX_SPEC) and not probe_ok(0, FIX_PROBE_OUT, '', None)
           and not probe_ok(0, FIX_PROBE_OUT.replace('PASS FIX2', 'PASS FIX'), '', FIX_SPEC)
           and not probe_ok(0, FIX_PROBE_OUT, 'x', FIX_SPEC) and not probe_ok(1, FIX_PROBE_OUT, '', FIX_SPEC))
    bump = FIX_PROBE_OUT + ' '
    noind = FIX_PROBE_OUT.replace('PASS IND1 (1)\n', '')
    report('self: the probe rule requires the separate implementation\'s codes, the byte replay and the SymPy line',
           not probe_ok(0, FIX_PROBE_OUT, '', dict(FIX_SPEC, independent=[]))
           and not probe_ok(0, bump, '', FIX_SPEC)
           and not probe_ok(0, FIX_PROBE_OUT, '', dict(FIX_SPEC, stdout_sha256=None))
           and not probe_ok(0, FIX_PROBE_OUT.replace('SYMPY 1.14.0', 'SYMPY 1.13.3'), '',
                            dict(FIX_SPEC, stdout_sha256=hashlib.sha256(FIX_PROBE_OUT.replace(
                                'SYMPY 1.14.0', 'SYMPY 1.13.3').encode()).hexdigest()))
           and not probe_ok(0, FIX_PROBE_OUT, '', dict(FIX_SPEC, sympy='1.13.3'))
           and not probe_ok(0, noind, '', dict(FIX_SPEC, stdout_sha256=hashlib.sha256(noind.encode()).hexdigest())))
    loose = [(o, n.replace('sympy==1.14.0', 'sympy')) for o, n in FIX_SPLICES]
    other = [(o, n.replace('sympy==1.14.0', 'sympy>=1.14')) for o, n in FIX_SPLICES]
    report('self: W\'s pin rule requires exactly sympy==1.14.0 when the spec names SymPy, and fails with the spec pending',
           pin_ok(FIX_SPLICES, FIX_SPEC) and not pin_ok(loose, FIX_SPEC) and not pin_ok(other, FIX_SPEC)
           and not pin_ok(FIX_SPLICES, None) and not pin_ok(FIX_SPLICES, dict(FIX_SPEC, sympy=None))
           and pin_ok([FIX_SPLICES[0]], dict(FIX_SPEC, sympy=None)))
    h0 = sorted(HISTORICAL)[0]
    gtab = prereg
    for h in HISTORICAL:
        gtab = set_row(gtab, h, 'none', 'gap: log expired')
    gp_ = retention(gtab)
    atab = set_row(prereg, h0, '`verification/audits/evidence-retention/x/a.json`', '`%s`' % ('0' * 64))
    bad_rows = [set_row(prereg, h0, 'none', 'gap:'), set_row(prereg, h0, '`evidence/a.json`', 'gap: lost'),
                set_row(prereg, h0, 'none', '`%s`' % ('0' * 64)), set_row(prereg, h0, 'pending', '`%s`' % ('0' * 64)),
                set_row(prereg, h0, '`%sx.json`' % RDIR, '`%s`' % ('0' * 64)),
                set_row(prereg, h0, '`papers/x.md`', '`%s`' % ('0' * 64))]
    report('self: the retention table takes an expected-result digest, a file retained on main or a recorded gap on '
           'a historical row, and refuses the inconsistent forms',
           gp_ is not None and set(gp_) == EVIDENCE_ROWS and all(gp_[h] == (NONE, GAP) for h in HISTORICAL)
           and (retention(atab) or {}).get(h0) == ('verification/audits/evidence-retention/x/a.json', '0' * 64)
           and all(retention(t) is None for t in bad_rows))
    report('self: passed() rejects an empty, non-bool or partial map and an unknown stage',
           not passed({}) and not passed({c: 1 for c in REQUIRED['E']}) and passed({c: True for c in REQUIRED['E']})
           and passed({c: True for c in REQUIRED['S1']}, 'S1') and not passed({c: True for c in REQUIRED['S1']})
           and not passed({c: True for c in REQUIRED['E']}, 'x'))
    problems, n = verdict_regression()
    report('self: verdict() prints no positive token when any required control fails, is unreported or non-bool, '
           'and each cell reads only its own reports (%d cases)' % n, not problems, '; '.join(problems))
    problems, n = e2e_cases(prereg)
    report('self: the real check() through verdict() fails, names the control, prints no positive token and never '
           'runs the probe with any record call removed or any control\'s inputs absent; unmutated it passes; main '
           'exits and refuses unknown stages and arguments (%d cases)' % n, not problems, '; '.join(problems))
    selfs = len([r for r in RAN if r.startswith('self:')]) + 1
    report('self: %d self-checks ran, as frozen (%d)' % (selfs, SELF_CHECKS), selfs == SELF_CHECKS)
    return not FAIL


def main(argv):
    def opts(rest, allowed):
        out, i = {}, 0
        while i < len(rest):
            if rest[i] not in allowed or i + 1 >= len(rest) or rest[i + 1].startswith('--'):
                return None
            out[rest[i]] = rest[i + 1]; i += 2
        return out
    if argv == ['--self-test']:
        ok = self_test()
    elif argv[:1] == ['check'] and len(argv) >= 4 and argv[2] == '--freeze':
        o = opts(argv[4:], {'--stage'})
        if o is None or o.get('--stage', 'E') not in STAGES:
            print('check: unknown argument or stage %r (expected --stage one of %s)' % (argv[4:], ', '.join(STAGES)))
            return 2
        stage = o.get('--stage', 'E')
        ok = passed(check(argv[1], argv[3], stage), stage)
    elif argv[:1] == ['verdict'] and len(argv) >= 4 and argv[2] == '--freeze':
        o = opts(argv[4:], {'--axioms'})
        if o is None:
            print('verdict: unknown argument %r' % (argv[4:],))
            return 2
        ok = verdict(argv[1], argv[3], o.get('--axioms'))
    else:
        print(__doc__)
        return 2
    print('controls: %s (%d failure(s))' % ('OK' if ok else 'FAILED', len(FAIL)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

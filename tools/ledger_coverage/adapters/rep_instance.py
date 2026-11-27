"""The configuration's control instance of design r6 R6.EVID.8 and the role binding at a record snapshot S of A1
staging amendment r2, sec. 2 ("R6.REC.7 and R6.EVID.8 for the designated roles").

- The control instance is a template landed with the tool revision: a configuration document in which the pin of the
  side-change class record is a hole, `{"fill": "class-tip-at-M"}`, filled by the runner from the landed class record
  that heads its lineage in the tree of the run's `M` (R6.EVID.8). The staged allow input may come from S (staging r2
  sec. 2): a rule reference may be the hole `{"fill": "allow-tip-at-S"}`, filled from the allow tip resolved at S.
  Filling replaces the `fill` key by `path` and `blob_sha256` and keeps every other key of the entry. The template
  names no blob of a record of the class lineage, so K1-GRAPH's acyclicity is kept; `fill` refuses a template that
  does.
- The role binding: the reviewed control inputs supply S and the sha256 of the transition descriptor S carries. The
  descriptor's base `B`, its custody archive at `B`, and the bounded namespace and records checks over the verified
  first-parent paths `B..S` and `B..M` are those of chain admission (engine `transition.representative_binding`); the
  class tip resolved at S equals the landed class tip in `M` by path and digest; the `tool-landing` pins of that tip
  are re-derived from `M` (R6.TREE.5): each pinned path's blob at `M` hashes to its pin. Anything else refuses the
  binding, and the affected controls stay open.

Usage:
  python3 -I -B tools/ledger_coverage/adapters/rep_instance.py --repo DIR --template REV:PATH --snapshot S
      --descriptor-sha256 HEX --main M --out DIR
      writes DIR/binding.json and, when the binding holds, DIR/control-instance.json; exit 0, or 3 when refused
  python3 -I -B tools/ledger_coverage/adapters/rep_instance.py --make-template CONFIG [--allow-path P ...]
      --write FILE
  python3 -I -B tools/ledger_coverage/adapters/rep_instance.py --self-test [OUT]
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage import record_authority as ra  # noqa: E402
from ledger_coverage.engine import gitobj, transition as tr  # noqa: E402

CLASS_FILL = 'class-tip-at-M'
ALLOW_FILL = 'allow-tip-at-S'
FILLS = (CLASS_FILL, ALLOW_FILL)
# the template's path in the tool's audit directory
TEMPLATE = 'rep/control-instance.json'


class Refused(Exception):
    """The control instance or the role binding cannot be established; the message is the reason."""


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _dump(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def holes(doc, at=''):
    """[(location, fill kind)] of every hole in the document."""
    out = []
    if isinstance(doc, dict):
        if 'fill' in doc:
            out.append((at or '/', doc['fill']))
        for k, v in doc.items():
            if k != 'fill':
                out += holes(v, '%s/%s' % (at, k))
    elif isinstance(doc, list):
        for i, v in enumerate(doc):
            out += holes(v, '%s/%d' % (at, i))
    return out


def _blobs(doc):
    if isinstance(doc, dict):
        return ({doc['blob_sha256']} if isinstance(doc.get('blob_sha256'), str) else set()) | \
            set().union(*[_blobs(v) for v in doc.values()])
    if isinstance(doc, list):
        return set().union(*[_blobs(v) for v in doc])
    return set()


def make_template(cfg, allow_paths=()):
    """A template from a configuration document: roles.side_change_classes and every `records` entry of kind
    side-change-classes become class holes; every `rules` entry whose path is in `allow_paths` becomes an allow hole."""
    t = copy.deepcopy(cfg)
    t['roles']['side_change_classes'] = {'fill': CLASS_FILL}
    t['records'] = [{'kind': r['kind'], 'fill': CLASS_FILL} if isinstance(r, dict) and
                    r.get('kind') == 'side-change-classes' else r for r in t['records']]
    t['rules'] = [{'fill': ALLOW_FILL} if isinstance(r, dict) and r.get('path') in allow_paths else r
                  for r in t['rules']]
    return t


def fill(template_bytes, binding):
    """The control instance: the template with each hole filled from the binding ({fill kind: {path, blob_sha256}};
    `class_chain`, the class lineage at M, is checked against the template's blobs)."""
    try:
        t = json.loads(template_bytes.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        raise Refused('the control-instance template is not JSON')
    if not isinstance(t, dict) or not isinstance(t.get('roles'), dict):
        raise Refused('the control-instance template is not a configuration document')
    hs = holes(t)
    if (t['roles'].get('side_change_classes') or {}).get('fill') != CLASS_FILL:
        raise Refused('the template\'s roles.side_change_classes is not the class hole')
    bad = sorted({k for _, k in hs if k not in FILLS})
    if bad:
        raise Refused('the template has holes of unknown kind: %s' % bad)
    lineage = {r['blob_sha256'] for r in binding.get('class_chain') or []}
    named = _blobs(t) & lineage
    if named:
        raise Refused('the template names a blob of the class lineage (K1-GRAPH): %s' % sorted(named))

    def walk(v):
        if isinstance(v, dict):
            if 'fill' in v:
                ref = binding.get(v['fill'])
                if not isinstance(ref, dict) or set(ref) != {'path', 'blob_sha256'}:
                    raise Refused('the binding gives no reference for the hole %s' % v['fill'])
                out = {k: walk(x) for k, x in v.items() if k != 'fill'}
                out.update(ref)
                return out
            return {k: walk(x) for k, x in v.items()}
        if isinstance(v, list):
            return [walk(x) for x in v]
        return v
    return _dump(walk(t))


def bind(repo, S, M, descriptor_sha256, roles=None, rec_dir=None):
    """The role binding at the snapshot S for the run's M (staging r2 sec. 2). Returns {fill kind: reference, B,
    descriptor, class_chain, pins_checked}; Refused when the snapshot or the role binding cannot be verified."""
    roles = roles or ra.transition_roles
    rec_dir = rec_dir or ra.authorized_record_directories[0] + '/'
    dpath = rec_dir + ra.transition_descriptor
    try:
        data = repo.read(S, dpath)
        if data is None:
            raise Refused('the snapshot S holds no transition descriptor at %s' % dpath)
        if _sha(data) != descriptor_sha256:
            raise Refused('the transition descriptor at S is not the reviewed one (sha256 differs)')
        desc = tr.parse_descriptor(data, ra.transition_descriptor_schema)
        B = repo.resolve(desc['base'])
        cust = repo.read(B, desc['custody']['path'])
        if cust is None or _sha(cust) != desc['custody']['blob_sha256']:
            raise Refused('the custody archive is not at B with its pinned digest')
        got = tr.representative_binding(repo, B, S, M, roles, desc)
        _path, chains_m = tr.walk(repo, B, M, roles, desc)
        tip = got['class_tip_at_M']
        doc = json.loads(repo.read(M, tip['path']).decode('utf-8'))
        pins, stale = 0, []
        for c in doc.get('classes') or []:
            if not isinstance(c, dict) or c.get('id') != ra.tool_landing_class_id:
                continue
            for p in c.get('pins') or []:
                pins += 1
                b = repo.read(M, p.get('path')) if isinstance(p, dict) and isinstance(p.get('path'), str) else None
                if b is None or _sha(b) != p.get('blob_sha256') or \
                        ('git_blob' in p and gitobj.blob_id_of(b) != p['git_blob']):
                    stale.append(p.get('path') if isinstance(p, dict) else p)
        if stale:
            raise Refused('tool-landing pins of the class tip differ from M\'s blobs: %s' % sorted(map(str, stale))[:5])
    except tr.Refused as exc:
        raise Refused(str(exc))
    except gitobj.Unresolvable as exc:
        raise Refused('an object the binding reads cannot be read: %s' % exc)
    return {CLASS_FILL: tip, ALLOW_FILL: got['tips_at_S']['allow'], 'S': S, 'M': M, 'B': B,
            'descriptor': {'path': dpath, 'blob_sha256': descriptor_sha256}, 'class_chain': chains_m['class'],
            'pins_checked': pins}


# ---- command line --------------------------------------------------------------------------------------------

def _full(repo_path, rev):
    r = subprocess.run(['git', '-C', repo_path, 'rev-parse', '--verify', '--quiet', rev + '^{commit}'],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('%s does not resolve to a commit' % rev)
    return r.stdout.strip()


def run(args):
    repo = gitobj.GitRepo(args.repo)
    trev, tpath = args.template.split(':', 1)
    template = repo.read(_full(args.repo, trev), tpath)
    os.makedirs(args.out, exist_ok=True)
    rec = {'template': {'path': tpath, 'blob_sha256': _sha(template) if template is not None else None}}
    try:
        if template is None:
            raise Refused('no template at %s' % args.template)
        b = bind(repo, _full(args.repo, args.snapshot), _full(args.repo, args.main), args.descriptor_sha256)
        inst = fill(template, b)
        with open(os.path.join(args.out, 'control-instance.json'), 'wb') as f:
            f.write(inst)
        rec.update(binding=b, instance={'blob_sha256': _sha(inst)})
        code = 0
    except Refused as exc:
        rec['refused'] = str(exc)
        code = 3
    with open(os.path.join(args.out, 'binding.json'), 'w') as f:
        json.dump(rec, f, indent=1, sort_keys=True)
        f.write('\n')
    print(json.dumps({'refused': rec.get('refused'), 'instance': rec.get('instance')}))
    return code


# ---- self-test: synthetic B..S..M in memory at the designated namespaces ---------------------------------------

def self_test(out=None):
    cls_role, allow_role = ra.transition_roles
    rec_dir = ra.authorized_record_directories[0] + '/'
    croot, aroot = cls_role['directory'] + cls_role['root'], allow_role['directory'] + allow_role['root']
    custody = 'syn/custody/CUSTODY.json'
    tool = 'tools/ledger_coverage/syn_tool.py'
    tool_b = b'# tool\n'

    def cls(n, sup, tool_pin=tool_b):
        return _dump({'schema': cls_role['schema'], 'record_id': cls_role['record_id'], 'supersedes': sup,
                      'author': 'session.fixture-writer',
                      'classes': [{'id': ra.tool_landing_class_id, 'prefixes': ['tools/ledger_coverage/'],
                                   'pins': [{'path': tool, 'blob_sha256': _sha(tool_pin)}], 'n': n}]})

    def ref(p, b):
        return {'path': p, 'blob_sha256': _sha(b)}
    allow0 = _dump({'schema': allow_role['schema'], 'record_id': allow_role['record_id'], 'supersedes': None,
                    'author': 'session.fixture-writer', 'rules': []})
    c0 = cls(0, None)
    p1 = cls_role['directory'] + 'a1-staging-class-v1.json'
    c1 = cls(1, ref(croot, c0))
    p2 = cls_role['directory'] + 'a1-staging-class-v2.json'
    c2 = cls(2, ref(p1, c1))
    repo = gitobj.Overlay(None)
    root = repo.add_commit({'README.md': b'synthetic\n', tool: tool_b}, [], subject='root')
    B = repo.derive(root, {custody: b'{"archive": true}\n', croot: c0, aroot: allow0}, parents=[root], subject='B')
    desc = _dump({'schema': ra.transition_descriptor_schema, 'base': B, 'custody': ref(custody, b'{"archive": true}\n'),
                  'class_root': ref(croot, c0), 'allow_root': ref(aroot, allow0)})
    dsha = _sha(desc)
    S = repo.derive(B, {p1: c1, rec_dir + ra.transition_descriptor: desc}, parents=[B], subject='S')
    M = repo.derive(S, {'notes/landing.txt': b'm\n'}, parents=[S], subject='M')
    cfg = {'schema': 'oi-retirement-config/1', 'roles': {'scientific_base': '0' * 40,
                                                        'side_change_classes': ref('old/classes.json', b'old')},
           'records': [{'kind': 'scope', 'path': 'syn/scope.json', 'blob_sha256': _sha(b'scope')},
                       {'kind': 'side-change-classes', 'path': 'old/classes.json', 'blob_sha256': _sha(b'old')}],
           'rules': [{'path': 'syn/deny.json', 'blob_sha256': _sha(b'deny')},
                     {'path': 'syn/allow-old.json', 'blob_sha256': _sha(b'allow-old')}]}
    tmpl = _dump(make_template(cfg, allow_paths=('syn/allow-old.json',)))
    cases = []

    def case(cid, expected, fn, want):
        try:
            got = ('ok', fn())
        except Refused as exc:
            got = ('refused', str(exc))
        holds = want(got)
        cases.append({'id': cid, 'expected': expected, 'actual': got if got[0] == 'refused' else 'ok',
                      'status': 'PASS' if holds else 'FAIL'})

    def positive():
        b = bind(repo, S, M, dsha)
        i1, i2 = fill(tmpl, b), fill(tmpl, b)
        doc = json.loads(i1)
        return i1 == i2, doc, b
    case('REP-INSTANCE/1', 'binding at S holds; the class hole is the class tip at M in roles and records, the allow '
                           'hole the allow tip at S; two fills are byte-equal', positive,
         lambda g: g[0] == 'ok' and g[1][0] and g[1][1]['roles']['side_change_classes'] == ref(p1, c1) and
         g[1][1]['records'][1] == dict(kind='side-change-classes', **ref(p1, c1)) and
         g[1][1]['rules'] == [cfg['rules'][0], ref(aroot, allow0)] and g[1][1]['records'][0] == cfg['records'][0] and
         g[1][2]['pins_checked'] == 1)
    M2 = repo.derive(S, {p2: c2}, parents=[S], subject='M with a newer class tip')
    case('REP-INSTANCE/2', 'M\'s landed class tip is newer than the tip at S: refused', lambda: bind(repo, S, M2, dsha),
         lambda g: g[0] == 'refused' and 'not the landed class tip in M' in g[1])
    case('REP-INSTANCE/3', 'the descriptor at S is not the reviewed one: refused', lambda: bind(repo, S, M, '0' * 64),
         lambda g: g[0] == 'refused' and 'not the reviewed one' in g[1])
    case('REP-INSTANCE/4', 'S carries no transition descriptor: refused', lambda: bind(repo, B, B, dsha),
         lambda g: g[0] == 'refused' and 'holds no transition descriptor' in g[1])
    M3 = repo.derive(S, {tool: b'# tool, changed\n'}, parents=[S], subject='M with another tool blob')
    case('REP-INSTANCE/5', 'a tool-landing pin of the class tip differs from M\'s blob (R6.TREE.5): refused',
         lambda: bind(repo, S, M3, dsha), lambda g: g[0] == 'refused' and 'differ from M\'s blobs' in g[1])
    off = repo.derive(root, {'notes/o.txt': b'o\n'}, parents=[root], subject='M off B')
    case('REP-INSTANCE/6', 'B is not on M\'s first-parent chain: refused', lambda: bind(repo, S, off, dsha),
         lambda g: g[0] == 'refused' and 'not on the first-parent chain' in g[1])
    b = bind(repo, S, M, dsha)
    t_cyc = json.loads(tmpl)
    t_cyc['records'].append({'kind': 'note', 'path': croot, 'blob_sha256': _sha(c0)})
    case('REP-INSTANCE/7', 'the template names a blob of the class lineage (the root): refused (K1-GRAPH)',
         lambda: fill(_dump(t_cyc), b), lambda g: g[0] == 'refused' and 'K1-GRAPH' in g[1])
    t_nohole = json.loads(tmpl)
    t_nohole['roles']['side_change_classes'] = ref(p1, c1)
    case('REP-INSTANCE/8', 'the template pins the class record itself instead of the hole: refused',
         lambda: fill(_dump(t_nohole), b), lambda g: g[0] == 'refused' and 'is not the class hole' in g[1])
    t_unk = json.loads(tmpl)
    t_unk['rules'].append({'fill': 'something-else'})
    case('REP-INSTANCE/9', 'a hole of unknown kind: refused', lambda: fill(_dump(t_unk), b),
         lambda g: g[0] == 'refused' and 'unknown kind' in g[1])
    case('REP-INSTANCE/10', 'a binding without the allow reference: refused',
         lambda: fill(tmpl, {CLASS_FILL: b[CLASS_FILL], 'class_chain': b['class_chain']}),
         lambda g: g[0] == 'refused' and 'no reference for the hole allow-tip-at-S' in g[1])
    bad = [c['id'] for c in cases if c['status'] != 'PASS']
    if out:
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'rep-instance-selftest.json'), 'w') as f:
            json.dump({'schema': 'oi-local-controls/1', 'suite': 'rep-instance', 'cases': cases}, f, indent=1,
                      sort_keys=True, default=str)
            f.write('\n')
    print(json.dumps({'cases': len(cases), 'failed': bad}))
    return 0 if not bad else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--self-test':
        return self_test(sys.argv[2] if len(sys.argv) > 2 else None)
    if len(sys.argv) > 1 and sys.argv[1] == '--make-template':
        ap = argparse.ArgumentParser()
        ap.add_argument('--make-template', required=True, metavar='CONFIG', help='a configuration document')
        ap.add_argument('--allow-path', action='append', default=[], help='a rules path that becomes the allow hole')
        ap.add_argument('--write', required=True, help='where the template is written')
        a = ap.parse_args()
        with open(a.make_template, 'rb') as f:
            t = make_template(json.loads(f.read().decode('utf-8')), tuple(a.allow_path))
        if len([h for h in holes(t) if h[1] == ALLOW_FILL]) != len(a.allow_path):
            raise SystemExit('an --allow-path is not a rules path of the configuration')
        with open(a.write, 'wb') as f:
            f.write(_dump(t))
        print(json.dumps({'holes': holes(t)}))
        return 0
    ap = argparse.ArgumentParser()
    for k in ('--repo', '--template', '--snapshot', '--descriptor-sha256', '--main', '--out'):
        ap.add_argument(k, required=True)
    return run(ap.parse_args())


if __name__ == '__main__':
    sys.exit(main())

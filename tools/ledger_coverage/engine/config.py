"""Configuration record oi-retirement-config/1: loading, fail-closed validation, adapter admission (sec. 16)."""
import json
import types

from . import outcome as oc
from . import profiles as pr
from . import records as rec
from . import util
from .gitobj import Unresolvable, on_first_parent_chain

config_schema = 'oi-retirement-config/1'
required = ['schema', 'config_id', 'version', 'supersedes', 'retirement', 'roles', 'corpus', 'adapters', 'profiles',
            'checks', 'rules', 'context_mapping', 'indicators', 'sentence', 'hp_obligations', 'delegation', 'records',
            'operations', 'controls', 'author']
optional = ['notes', 'sites']
operations = ('record', 'coverage', 'execution', 'terms')
interfaces = ('ledger', 'sitemap', 'replay', 'delegation')


def stop(cls, msg, **detail):
    if cls in oc.void_classes:
        return oc.Stop(oc.void, cls, msg, detail)
    return oc.Stop(oc.error, cls, msg, detail)


def read_ref(repo, rev, ref, what):
    """Bytes of {path, blob_sha256[, commit]} read from the object store; a source change on any mismatch."""
    commit = ref.get('commit') or rev
    try:
        data = repo.read(commit, ref['path'])
    except Unresolvable as exc:
        raise stop('SOURCE_CHANGED', '%s: %s' % (what, exc))
    if data is None:
        raise stop('SOURCE_CHANGED', '%s: %s not present at %s' % (what, ref['path'], commit[:12]))
    if util.sha256(data) != ref.get('blob_sha256'):
        raise stop('SOURCE_CHANGED', '%s: %s does not hash to its pin' % (what, ref['path']))
    return data


def admit_module(repo, rev, spec, interface):
    """Load an adapter module from its pinned blob; the engine names no adapter."""
    data = read_ref(repo, rev, spec['module'], 'adapter %s' % spec.get('adapter'))
    mod = types.ModuleType('adapter_' + util.sha256(data)[:16])
    try:
        exec(compile(data.decode('utf-8'), spec['module']['path'], 'exec'), mod.__dict__)
    except Exception as exc:  # an adapter that cannot load is a configuration defect
        raise stop('CONFIG_INVALID', 'adapter %s does not load: %s' % (spec.get('adapter'), exc))
    got = (getattr(mod, 'INTERFACE', None), getattr(mod, 'NAME', None), getattr(mod, 'VERSION', None))
    if got != (interface, spec.get('adapter'), spec.get('adapter_version')):
        raise stop('CONFIG_INVALID', 'adapter declares %r, configured %r' %
                   (got, (interface, spec.get('adapter'), spec.get('adapter_version'))))
    return mod, util.sha256(data)


def non_widening(old, new):
    """Sec. 16.2: is every change from old to new on the non-widening list? Returns the widening reasons."""
    why = []
    keys = set(old) | set(new)
    for k in sorted(keys - {'version', 'supersedes', 'profiles', 'context_mapping', 'checks', 'rules', 'controls',
                            'widening_review', 'author', 'config_id', 'records', 'notes'}):
        if util.canonical(old.get(k)) != util.canonical(new.get(k)):
            why.append('changed %s' % k)
    op = {p['name']: p for p in old.get('profiles', [])}
    np_ = {p['name']: p for p in new.get('profiles', [])}
    for n, p in op.items():
        if n not in np_:
            why.append('profile %s removed' % n)
        elif util.canonical(p) != util.canonical(np_[n]):
            q = np_[n]
            only_scope_added = (p.get('kind') == 'deny' and {k: v for k, v in p.items() if k != 'scope'} ==
                                {k: v for k, v in q.items() if k != 'scope'} and isinstance(p.get('scope'), list)
                                and isinstance(q.get('scope'), list) and set(p['scope']) <= set(q['scope']))
            if not only_scope_added:
                why.append('profile %s changed' % n)
    om, nm = old.get('context_mapping', {}), new.get('context_mapping', {})
    if util.canonical({k: v for k, v in om.items() if k != 'values'}) != \
            util.canonical({k: v for k, v in nm.items() if k != 'values'}):
        why.append('context mapping changed')
    for v, b in om.get('values', {}).items():
        if v not in nm.get('values', {}):
            why.append('context value %s removed' % v)
        elif bool(b) and not nm['values'][v]:
            why.append('context value %s true to false' % v)
    oc_ = {c['id']: c for c in old.get('checks', [])}
    nc = {c['id']: c for c in new.get('checks', [])}
    for i, c in oc_.items():
        if i not in nc:
            why.append('check %s removed' % i)
            continue
        if not set(c.get('final_profiles', [])) <= set(nc[i].get('final_profiles', [])):
            why.append('check %s final profile removed' % i)
        if c.get('profiles') != nc[i].get('profiles') and not set(c.get('profiles', [])) <= set(nc[i].get('profiles', [])):
            why.append('check %s profiles changed' % i)
    orl = {r['path']: r for r in old.get('rules', [])}
    nrl = {r['path']: r for r in new.get('rules', [])}
    for p_, r in nrl.items():
        if p_ not in orl or util.canonical(orl[p_]) != util.canonical(r):
            why.append('rule file %s added or changed' % p_)
    if util.canonical(old.get('controls')) != util.canonical(new.get('controls')):
        why.append('controls file changed (needs review of what changed)')
    return why


class Loaded:
    def __init__(self):
        self.config = None
        self.ref = None
        self.modules = {}
        self.adapter_records = []
        self.profiles = {}
        self.profile_records = []
        self.rule_files = []
        self.store = None
        self.admitted = set()
        self.admission = None
        self.controls = None
        self.problems = []


forbidden = ('owner', 'repository', 'workflow', 'engine_pins', 'plans', 'authority_thread', 'freeze_ledger_path',
             'forms', 'authority', 'admission')
retirement_fields = ('name', 'issue', 'owner')


def load(repo, rev, path, expected_sha, operation, mode, extra_records=(), admission=None, table=None):
    """Integrity stage for the configuration. mode: 'chain' (admitted by sec. 6.3: `admission` is the snapshot
    the authority module built, `table` the blobs F's pin table lists, {path: bytes}) or 'harness' (an in-process
    control run that admits a draft configuration without its chain; never acceptable)."""
    L = Loaded()
    if mode == 'chain' and (admission is None or table is None):
        raise stop('CONFIG_UNREVIEWED', 'no admission: the configuration is admitted only through sec. 6.3')
    try:
        commit = repo.resolve(rev)
    except Unresolvable as exc:
        raise stop('UNRESOLVABLE', str(exc))
    data = repo.read(commit, path)
    if data is None:
        raise stop('SOURCE_CHANGED', 'configuration %s not present at %s' % (path, commit[:12]))
    sha = util.sha256(data)
    if mode == 'chain' and table.get(path) != data:
        raise stop('CONFIG_UNREVIEWED', 'the configuration is not the blob F\'s pin table lists')
    if expected_sha is not None and sha != expected_sha:
        raise stop('CONFIG_UNREVIEWED' if mode == 'chain' else 'SOURCE_CHANGED',
                   'configuration does not equal --config-sha256')
    try:
        cfg = json.loads(data.decode('utf-8'))
    except ValueError as exc:
        raise stop('CONFIG_INVALID', 'configuration is not valid json: %s' % exc)
    L.config, L.ref = cfg, {'path': path, 'commit': commit, 'blob_sha256': sha}
    if not isinstance(cfg, dict) or cfg.get('schema') != config_schema:
        raise stop('CONFIG_INVALID', 'unknown configuration schema')
    missing = [k for k in required if k not in cfg]
    unknown = [k for k in cfg if k not in required and k not in optional]
    if missing or unknown:
        raise stop('CONFIG_INVALID', 'missing %s; unknown %s' % (missing, unknown))
    if not isinstance(cfg['retirement'], dict) or set(cfg['retirement']) - set(retirement_fields):
        raise stop('CONFIG_INVALID', 'unknown retirement field (authority values are never configuration): %s'
                   % sorted(set(cfg['retirement']) - set(retirement_fields)))
    if mode == 'chain' and cfg['retirement'].get('owner') != admission['owner_id']:
        raise stop('CONFIG_UNREVIEWED', 'retirement.owner is not the authority record\'s owner id')
    if not set(cfg['operations']) <= set(operations):
        raise stop('CONFIG_INVALID', 'unknown operation in operations')
    if operation is not None and operation not in cfg['operations']:
        raise stop('CONFIG_UNSUPPORTED', 'operation %s is not supported by this configuration' % operation)
    # adapters, by pinned blob
    for iface in ('ledger', 'sitemap', 'replay'):
        spec = cfg['adapters'].get(iface)
        if spec is None:
            continue
        mod, msha = admit_module(repo, commit, spec, iface)
        L.modules[iface] = mod
        L.adapter_records.append({'interface': iface, 'name': spec['adapter'], 'version': spec['adapter_version'],
                                  'module_sha256': msha, 'module_path': spec['module']['path']})
    if cfg['delegation'] is not None:
        read_ref(repo, commit, cfg['delegation'], 'delegation contract')
        for spec in cfg['delegation'].get('class_adapters', []):
            mod, msha = admit_module(repo, commit, spec, 'delegation')
            L.modules['delegation:' + spec['adapter']] = mod
            L.adapter_records.append({'interface': 'delegation', 'name': spec['adapter'],
                                      'version': spec['adapter_version'], 'module_sha256': msha,
                                      'module_path': spec['module']['path']})
    # referenced records and rule files, by pinned blob
    entries = []
    for r in list(cfg['rules']) + list(cfg['records']):
        entries.append((r['path'], read_ref(repo, commit, r, 'record %s' % r['path'])))
    controls_b = read_ref(repo, commit, cfg['controls'], 'controls file')
    for r in extra_records:
        entries.append((r['path'], r['data']))
    # the configuration's own review and authorization: under the chain, only the blobs F's pin table lists
    # (point 6; files beside the configuration are never admitted). The harness reads the draft's neighbours.
    cfg_dir = path.rsplit('/', 1)[0] + '/' if '/' in path else ''
    if mode == 'chain':
        for p, b in sorted(table.items()):
            if p != path and p.endswith('.json'):
                entries.append((p, b))
    else:
        for p, bid in sorted(repo.paths(commit).items()):
            if p.startswith(cfg_dir) and p.endswith('.json') and p != path and '/' not in p[len(cfg_dir):]:
                entries.append((p, repo.read_blob(bid)))
    entries.append((path, data))
    L.store = rec.Store(entries)

    def resolver(ref, _c=commit):
        try:
            b = repo.read(_c, ref['path'])
        except Unresolvable:
            return None
        if b is None or util.sha256(b) != ref['blob_sha256']:
            return None
        try:
            return json.loads(b.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return None
    L.store.resolver = resolver
    L.admitted = {r['blob_sha256'] for r in list(cfg['rules']) + list(cfg['records'])} | {sha}
    for p, d in entries:
        doc = L.store.by_sha[util.sha256(d)][1]
        if isinstance(doc, dict) and doc.get('schema') in (rec.review_schema, rec.auth_schema) and \
                (p in (table or {}) if mode == 'chain' else p.startswith(cfg_dir)):
            if doc.get('schema') == rec.review_schema and doc.get('reviewed', {}).get('blob_sha256') == sha:
                L.admitted.add(util.sha256(d))
            if doc.get('schema') == rec.auth_schema and any(e.get('record', {}).get('blob_sha256') == sha
                                                            for e in doc.get('authorizes', [])):
                L.admitted.add(util.sha256(d))
    # S7: a side-change class id is defined exactly once across the class records the configuration references
    seen_ids = []
    for r in cfg['records']:
        d = L.store.get(r)
        if isinstance(d, dict) and d.get('schema') == 'oi-side-change-classes/1':
            seen_ids += [c.get('id') for c in d.get('classes', [])]
    if len(seen_ids) != len(set(seen_ids)):
        raise stop('CONFIG_INCONSISTENT', 'a side-change class id is defined more than once: %s'
                   % sorted({i for i in seen_ids if seen_ids.count(i) > 1}))
    # review chain of the configuration itself
    if mode == 'chain':
        probs = rec.lint_chain({'path': path, 'blob_sha256': sha}, L.store, cfg['retirement'].get('owner'),
                               L.admitted)
        if probs:
            raise stop('CONFIG_UNREVIEWED', 'configuration review chain: %s' % '; '.join(probs[:4]))
        if cfg['supersedes'] is not None:
            old_b = read_ref(repo, commit, cfg['supersedes'], 'the configuration it supersedes')
            why = non_widening(json.loads(old_b.decode('utf-8')), cfg)
            if why:
                reviewers = rec.reviewers_of({'blob_sha256': sha}, L.store)
                if not rec.widening_review_ok({'path': path, 'blob_sha256': sha}, L.store, L.admitted,
                                              reviewers, cfg.get('author'), cfg['supersedes'],
                                              ['%s:%s' % (cfg['config_id'], w) for w in why],
                                              cfg['retirement'].get('owner')):
                    raise stop('CONFIG_UNREVIEWED', 'widening without a widening review: %s' % '; '.join(why[:4]))
        L.admission = dict(admission)
    else:
        L.admission = dict(admission or {}, mode='control-harness',
                           note='a draft configuration admitted without its chain by the control harness')
    # consistency
    names = [p['name'] for p in cfg['profiles']]
    if len(names) != len(set(names)):
        raise stop('CONFIG_INCONSISTENT', 'duplicate profile name')
    kinds = {p['name']: p['kind'] for p in cfg['profiles']}
    for c in cfg['checks']:
        for n in c.get('profiles', []):
            if n not in kinds:
                raise stop('CONFIG_INCONSISTENT', 'check %s names unknown profile %s' % (c['id'], n))
        for n in c.get('final_profiles', []):
            if kinds.get(n) != 'review' or n not in c.get('profiles', []):
                raise stop('CONFIG_INCONSISTENT', 'final profile %s of check %s is not a listed review profile'
                           % (n, c['id']))
    for p in cfg['profiles']:
        def rd(src, _p=p):
            ref = {'path': src['path'], 'blob_sha256': src['blob_sha256'], 'commit': src.get('commit')}
            return read_ref(repo, commit, ref, 'profile %s source' % _p['name'])
        try:
            prof, h = pr.load_profile(p, rd)
        except pr.ExtractFault as exc:
            raise stop('CONFIG_INCONSISTENT', 'profile %s: %s' % (p['name'], exc))
        if h != p.get('pattern_sha256'):
            raise stop('CONFIG_INCONSISTENT', 'profile %s: extractor output does not hash to pattern_sha256'
                       % p['name'])
        L.profiles[p['name']] = prof
        L.profile_records.append({'name': p['name'], 'kind': p['kind'], 'source_commit': p['source'].get('commit'),
                                  'path': p['source'].get('path'), 'blob_sha256': p['source'].get('blob_sha256'),
                                  'pattern_sha256': h})
    cm = cfg['context_mapping']
    if cm.get('default') != 'invalid' or not isinstance(cm.get('values'), dict):
        raise stop('CONFIG_INCONSISTENT', 'context mapping must list values with default invalid')
    hp_chain_check(repo, cfg)
    # controls
    try:
        controls = json.loads(controls_b.decode('utf-8'))
    except ValueError:
        controls = None
    L.controls = controls
    for op in cfg['operations']:
        cs = [c for c in (controls or {}).get('controls', []) if op in c.get('operations', [])]
        if not any(c.get('direction') == 'positive' for c in cs) or \
                not any(c.get('direction') == 'adversarial' for c in cs):
            raise stop('CONFIG_NO_CONTROLS', 'no positive and adversarial control for operation %s' % op)
    for r in cfg['rules']:
        L.rule_files.append((r, L.store.get(r)))
    return L


def hp_chain_check(repo, cfg):
    """Every HP obligation ends at the scientific base and every merge is on its first-parent chain."""
    base = cfg['roles']['scientific_base']
    for ob in cfg['hp_obligations']:
        frm, to = ob['segment']
        if to != base:
            raise stop('CONFIG_INCONSISTENT', 'HP obligation does not end at the scientific base')
        for m in ob['merges']:
            try:
                ps = repo.parents(m['commit'])
            except Unresolvable:
                raise stop('CONFIG_INCONSISTENT', 'merge %s is not resolvable' % m['commit'][:12])
            if not ps or ps[0] != m['first_parent'] or not on_first_parent_chain(repo, m['commit'], to) or \
                    not on_first_parent_chain(repo, frm, m['commit']):
                raise stop('CONFIG_INCONSISTENT', 'merge %s is off the chain or has another first parent'
                           % m['commit'][:12])
            if ('#%s' % str(m['pr']).lstrip('#')) not in repo.subject(m['commit']):
                raise stop('CONFIG_INCONSISTENT', 'merge %s subject does not name its PR' % m['commit'][:12])

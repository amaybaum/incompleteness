"""Configuration record oi-retirement-config/1: loading, fail-closed validation, adapter admission (sec. 16)."""
import json
import os
import posixpath
import re
import types

from . import outcome as oc
from . import profiles as pr
from . import records as rec
from . import rules as rulemod
from . import util
from .gitobj import Unresolvable, on_first_parent_chain

config_schema = 'oi-retirement-config/1'
required = ['schema', 'config_id', 'version', 'supersedes', 'retirement', 'roles', 'corpus', 'adapters', 'profiles',
            'checks', 'rules', 'context_mapping', 'indicators', 'sentence', 'hp_obligations', 'delegation', 'records',
            'tool', 'repository_id', 'operations', 'controls', 'author']
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


retirement_fields = ('name', 'issue')
_sha = re.compile(r'^[0-9a-f]{64}$')


def tool_layout():
    """The tool's own paths relative to the checkout it runs from: (entry point, package directory with a trailing
    slash), derived from this module's location, so the engine holds no path literal (sec. 16.1)."""
    pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.dirname(os.path.dirname(pkg))
    return os.path.relpath(pkg + '.py', root).replace(os.sep, '/'), \
        os.path.relpath(pkg, root).replace(os.sep, '/') + '/'


def tool_problems(tool, repository_id):
    """Sec. 16.2 lint of `tool` and `repository_id`: the files name the entry point and only paths under the package
    directory, each once, each with a sha256; the workflow a path and a sha256; the repository id a positive
    integer."""
    entry, pkg = tool_layout()
    out = []
    if not isinstance(tool, dict) or set(tool) != {'files', 'workflow'} or not isinstance(tool.get('files'), list):
        return ['tool must be {files, workflow}']
    paths = []
    for f in tool['files']:
        if not isinstance(f, dict) or set(f) != {'path', 'blob_sha256'} or not isinstance(f.get('path'), str) or \
                not _sha.match(str(f.get('blob_sha256'))):
            out.append('tool.files entry is not {path, blob_sha256}')
            continue
        paths.append(f['path'])
        if f['path'] != entry and not (f['path'].startswith(pkg) and len(f['path']) > len(pkg)):
            out.append('tool.files names a path outside the tool: %s' % f['path'])
    if len(paths) != len(set(paths)):
        out.append('tool.files names a path more than once')
    if entry not in paths:
        out.append('tool.files does not name the entry point')
    wf = tool.get('workflow')
    if not isinstance(wf, dict) or set(wf) != {'path', 'blob_sha256'} or not isinstance(wf.get('path'), str) or \
            not wf['path'] or not _sha.match(str(wf.get('blob_sha256'))):
        out.append('tool.workflow is not {path, blob_sha256}')
    if not isinstance(repository_id, int) or isinstance(repository_id, bool) or repository_id <= 0:
        out.append('repository_id is not a positive integer')
    return out


_pins_head = re.compile(r'^### \d+\.\d+ Record pins\b', re.M)
_pin_row = re.compile(r'^\| `([^`/\s]+)` \| `([0-9a-f]{64})` \|$')
_sep_row = re.compile(r'^\|(\s*:?-+:?\s*\|)+\s*$')


class PinTableError(Exception):
    pass


def read_pin_table(prereg):
    """The pin table of a plan record directory (sec. 6.3, configuration admission point 2): in the plan's file of
    record pins, the last subsection whose heading matches `### N.N Record pins`, with rows "| `file` | `sha256` |",
    each naming a file of that directory. A table line that is neither the header row, its separator nor such a row is
    malformed; a file named twice is malformed. Raises PinTableError."""
    try:
        t = prereg.decode('utf-8')
    except UnicodeDecodeError:
        raise PinTableError('the file of record pins is not utf-8')
    heads = [m.start() for m in _pins_head.finditer(t)]
    if not heads:
        raise PinTableError('the file of record pins has no Record pins subsection')
    i = heads[-1]
    j = t.find('\n#', i + 5)
    lines = t[i:j if j > 0 else None].split('\n')
    out = {}
    for k, line in enumerate(lines):
        if not line.startswith('|'):
            continue
        if _sep_row.match(line):
            continue
        if k + 1 < len(lines) and _sep_row.match(lines[k + 1]):
            continue  # the header row
        m = _pin_row.match(line)
        if not m or m.group(1) in ('.', '..'):
            raise PinTableError('malformed row in the last Record pins subsection: %r' % line[:120])
        if m.group(1) in out:
            raise PinTableError('a file is listed twice in the last Record pins subsection: %s' % m.group(1))
        out[m.group(1)] = m.group(2)
    return out


def admitted_by_table(repo, freeze, rec_dir, table):
    """Blobs the pin table admits, read from the freeze's tree as regular files: {path: bytes}."""
    out = {}
    for name, want in table.items():
        try:
            b = repo.read(freeze, rec_dir + name)
        except Unresolvable:
            continue
        if b is not None and util.sha256(b) == want:
            out[rec_dir + name] = b
    return out


def load(repo, rev, path, expected_sha, operation, mode, extra_records=(), admission=None, table=None):
    """Integrity stage for the configuration. mode: 'chain' (admitted by sec. 6.3: `admission` is the admission record
    with its snapshot, `table` the blobs F's pin table lists, {path: bytes}) or 'harness' (an in-process control run
    that admits a draft configuration without its chain; never acceptable)."""
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
                   'configuration does not equal the expected sha256')
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
        raise stop('CONFIG_INVALID', 'unknown retirement field: %s'
                   % sorted(set(cfg['retirement']) - set(retirement_fields)))
    tp = tool_problems(cfg['tool'], cfg['repository_id'])
    if tp:
        raise stop('CONFIG_INVALID', '; '.join(tp[:4]))
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
    # referenced records and rule files, by pinned blob, each from a regular-file entry (a record at a non-regular
    # entry is not read: it is record-invalid where it is used)
    entries = []
    L.nonregular = set()
    for r in list(cfg['rules']) + list(cfg['records']):
        if repo.mode(commit, r['path']) not in (None, '100644', '100755'):
            L.nonregular.add(r['path'])
            continue
        entries.append((r['path'], read_ref(repo, commit, r, 'record %s' % r['path'])))
    # a record kind this design does not define (for example a retired schema) is a configuration error (sec. 16.2)
    for r, (_, b) in zip([r for r in list(cfg['rules']) + list(cfg['records']) if r['path'] not in L.nonregular],
                         entries):
        if r not in cfg['records']:
            continue
        try:
            doc = json.loads(b.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            continue
        if isinstance(doc, dict) and 'schema' in doc and doc['schema'] not in rec.record_schemas + (rec.review_schema,):
            raise stop('CONFIG_INVALID', 'record %s has a kind this design does not define: %r'
                       % (r['path'], doc['schema']))
    controls_b = read_ref(repo, commit, cfg['controls'], 'controls file')
    for r in extra_records:
        entries.append((r['path'], r['data']))
    # the configuration's own review: under the chain, only the blobs F's pin table lists
    # (point 6; files beside the configuration are never admitted). The harness reads the draft's neighbours.
    cfg_dir = path.rsplit('/', 1)[0] + '/' if '/' in path else ''
    if mode == 'chain':
        for p, b in sorted(table.items()):
            if p != path and p.endswith('.json'):
                entries.append((p, b))
    else:
        for p, (mode, bid) in sorted(repo.entries(commit).items()):
            if p.startswith(cfg_dir) and p.endswith('.json') and p != path and '/' not in p[len(cfg_dir):] and \
                    mode in ('100644', '100755'):
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

    def scan(_c=commit):
        """DI-2: every json blob of the plan's record directory (the configuration's directory) and of the audit
        directory (the deepest directory holding every record and rule file the configuration references, or each
        such record's own directory when they share none) at F."""
        refs = [r['path'] for r in list(cfg['rules']) + list(cfg['records']) if isinstance(r.get('path'), str)]
        dirs = {cfg_dir}
        rdirs = [posixpath.dirname(q) for q in refs]
        common = posixpath.commonpath(rdirs) if rdirs else ''
        dirs |= {common + '/'} if common else {d + '/' if d else '' for d in rdirs}
        out = []
        for q, (mode, bid) in sorted(repo.entries(_c).items()):
            if q.endswith('.json') and any(q.startswith(d) for d in dirs) and mode in ('100644', '100755'):
                out.append((q, repo.read_blob(bid)))
        return out
    L.store.scan = scan

    def widening(old, new):
        """The widening items of a rule file or configuration against the record it supersedes (sec. 6.3, 16.2)."""
        try:
            if new.get('schema') == rulemod.rules_schema:
                return rulemod.file_widening(old, new)
            if new.get('schema') == config_schema and old is not None:
                return ['%s:%s' % (new.get('config_id'), w) for w in non_widening(old, new)]
        except (KeyError, TypeError, AttributeError) as exc:
            return ['%s:predecessor not comparable (%s)' % (new.get('record_id') or new.get('config_id'), exc)]
        return []
    L.store.widening = widening
    # DI-2, two heads: among the records the run reads
    L.store.heads_problems = rec.lineage_heads(list(cfg['rules']) + list(cfg['records']) +
                                               [{'path': path, 'blob_sha256': sha}], L.store)
    L.admitted = {r['blob_sha256'] for r in list(cfg['rules']) + list(cfg['records'])} | {sha}
    for p, d in entries:
        doc = L.store.by_sha[util.sha256(d)][1]
        if isinstance(doc, dict) and doc.get('schema') == rec.review_schema and \
                (p in (table or {}) if mode == 'chain' else p.startswith(cfg_dir)):
            if doc.get('reviewed', {}).get('blob_sha256') == sha:
                L.admitted.add(util.sha256(d))
    # S7: a side-change class id is defined exactly once across the class records the configuration references
    seen_ids = []
    for r in cfg['records']:
        d = L.store.get(r)
        if isinstance(d, dict) and d.get('schema') == 'oi-side-change-classes/1':
            cl = d.get('classes', [])
            # a record whose classes are not a list of objects is record-invalid where it is used (N6)
            seen_ids += [c.get('id') for c in cl if isinstance(c, dict)] if isinstance(cl, list) else []
    if len(seen_ids) != len(set(seen_ids)):
        raise stop('CONFIG_INCONSISTENT', 'a side-change class id is defined more than once: %s'
                   % sorted({i for i in seen_ids if seen_ids.count(i) > 1}))
    L.transition = None
    if mode == 'chain':
        L.transition = transition_admission(repo, commit, cfg_dir, path, sha, cfg, table)
        L.store.designated_roots = {(r['path'], r['blob_sha256'])
                                    for r in (L.transition or {}).get('roots', [])}
    # review chain of the configuration itself
    if mode == 'chain':
        own_review_problems(path, sha, cfg, table)
        probs = rec.lint_chain({'path': path, 'blob_sha256': sha}, L.store, L.admitted)
        if probs:
            raise stop('CONFIG_UNREVIEWED', 'configuration review chain: %s' % '; '.join(probs[:4]))
        if cfg['supersedes'] is not None:
            old_b = read_ref(repo, commit, cfg['supersedes'], 'the configuration it supersedes')
            why = non_widening(json.loads(old_b.decode('utf-8')), cfg)
            if why:
                # A1 staging amendment r2, sec. 3: the configuration's own widening review is selected from the
                # members of F's pin table only, names the exact new configuration in `reviewed` and the exact old
                # one in `replaces`, and is the only one of its kind there
                wides = [b for p_, b in sorted(table.items()) if _review_of(b, path, sha, 'widening')]
                if len(wides) > 1:
                    raise stop('CONFIG_UNREVIEWED', 'more than one widening review of the configuration in the pin '
                               'table')
                reviewers = rec.reviewers_of({'blob_sha256': sha}, L.store)
                pinned = {util.sha256(b) for b in table.values()}
                if not wides or not rec.widening_review_ok({'path': path, 'blob_sha256': sha}, L.store,
                                                           L.admitted & pinned, reviewers, cfg.get('author'),
                                                           cfg['supersedes'],
                                                           ['%s:%s' % (cfg['config_id'], w) for w in why]):
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
    # R6.CFG.4 and R6.RECON.33 as amended by the A1 staging amendment r2 (sec. 1): every check, of op `coverage` or
    # op `terms`, keeps exactly {id, profiles, final_profiles}; any other key, such as `default_for`, is an unknown
    # field (R6.VALID.2), so no default check is defined. An id names one check (as a profile name names one profile,
    # R6.VALID.4).
    if not isinstance(cfg['checks'], list):
        raise stop('CONFIG_INVALID', 'checks is not a list')
    for c in cfg['checks']:
        if not isinstance(c, dict) or set(c) != {'id', 'profiles', 'final_profiles'} or \
                not isinstance(c.get('id'), str) or not c['id'] or not isinstance(c.get('profiles'), list) or \
                not isinstance(c.get('final_profiles'), list):
            raise stop('CONFIG_INVALID', 'a check is not exactly {id, profiles, final_profiles}: %s'
                       % (sorted(c) if isinstance(c, dict) else type(c).__name__))
    cids = [c['id'] for c in cfg['checks']]
    if len(cids) != len(set(cids)):
        raise stop('CONFIG_INCONSISTENT', 'duplicate check id')
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


def _review_of(b, path, sha, kind):
    try:
        d = json.loads(b.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return False
    return isinstance(d, dict) and d.get('schema') == rec.review_schema and d.get('kind', 'review') == kind and \
        d.get('reviewed') == {'path': path, 'blob_sha256': sha}


def own_review_problems(path, sha, cfg, table):
    """A1 staging amendment r2, sec. 3 (R6.RECON.31, R6.REC.3-.5, R6.REC.16 as amended): the configuration's own
    ordinary review is a member of F's pin table naming its exact path and digest, and the only one of its kind there;
    the configuration's `records` hold no reference to a review of the configuration itself (its own reviews are
    bound by the external pin table, which keeps the binding acyclic)."""
    ordinary = [p for p, b in sorted(table.items()) if _review_of(b, path, sha, 'review')]
    if len(ordinary) != 1:
        raise stop('CONFIG_UNREVIEWED', '%d ordinary reviews of the configuration in the pin table, not one'
                   % len(ordinary))
    own = []
    for r in cfg['records']:
        b = table.get(r.get('path')) if isinstance(r, dict) else None
        try:
            d = json.loads(b.decode('utf-8')) if b is not None else None
        except (ValueError, UnicodeDecodeError):
            d = None
        if isinstance(d, dict) and d.get('schema') == rec.review_schema and \
                (d.get('reviewed') or {}).get('path') == path:
            own.append(r['path'])
    if own:
        raise stop('CONFIG_INVALID', 'the configuration\'s records reference a review of the configuration itself: %s'
                   % sorted(set(own))[0])


def transition_admission(repo, F, rec_dir, cpath, csha, cfg, table):
    """The transition to independently reviewed roots (A1 staging amendment r2, sec. 2), in a chain-admitted run.
    It is in play when the pin table binds the activation descriptor or the configuration references a member of a
    role namespace. Returns None when it is not in play, else {descriptor, base, tips, roots, prior}; any failed
    condition refuses admission (ERROR CONFIG_UNREVIEWED); an unreadable object is ERROR UNRESOLVABLE."""
    from .. import record_authority as ra
    from . import transition as tr
    roles = ra.transition_roles
    refs = [r for r in list(cfg['rules']) + list(cfg['records']) if isinstance(r, dict)]
    in_ns = [r for r in refs if isinstance(r.get('path'), str) and any(tr.in_namespace(r['path'], x) for x in roles)]
    dpath, ppath = rec_dir + ra.transition_descriptor, rec_dir + ra.transition_prior
    if dpath not in table and not in_ns:
        return None
    authorized = rec_dir.rstrip('/') in ra.authorized_record_directories
    try:
        if not authorized:
            raise tr.Refused('the transition is used from a record directory the tool does not admit')
        if dpath not in table or ppath not in table:
            raise tr.Refused('the pin table does not bind both %s and %s' % (ra.transition_descriptor,
                                                                          ra.transition_prior))
        desc = tr.parse_descriptor(table[dpath], ra.transition_descriptor_schema)
        prior = tr.parse_prior(table[ppath], ra.transition_prior_schema)
        try:
            B = repo.resolve(desc['base'])
        except Unresolvable as exc:
            raise stop('UNRESOLVABLE', 'the transition base B cannot be read: %s' % exc)
        cust = repo.read(B, desc['custody']['path'])
        if cust is None or util.sha256(cust) != desc['custody']['blob_sha256']:
            raise tr.Refused('the custody archive is not at B with its pinned digest')
        path, chains = tr.walk(repo, B, F, roles, desc)
        tips = {k: v[-1] for k, v in chains.items()}
        for r in in_ns:
            role = [x['role'] for x in roles if tr.in_namespace(r['path'], x)][0]
            if {'path': r['path'], 'blob_sha256': r.get('blob_sha256')} != tips[role]:
                raise tr.Refused('the configuration pins %s, not the current %s tip %s'
                                 % (r['path'], role, tips[role]['path']))

        def read_table(c):
            pt = repo.read(c, rec_dir + 'PREREG.md')
            if pt is None:
                raise tr.Refused('the prior freeze has no file of record pins')
            try:
                names = read_pin_table(pt)
            except PinTableError as exc:
                raise tr.Refused('the prior freeze\'s pin table cannot be read: %s' % exc)
            got = admitted_by_table(repo, c, rec_dir, names)
            return names, {p[len(rec_dir):]: b for p, b in got.items()}
        pc = tr.prior_continuity(path, F, prior, read_table, ra.transition_descriptor, util.sha256(table[dpath]),
                                 config_schema)
        if pc['freeze'] is not None and pc['configuration_sha256'] != csha:
            want = {'path': rec_dir + pc['configuration_name'], 'blob_sha256': pc['configuration_sha256']}
            if cfg.get('supersedes') != want:
                raise tr.Refused('the configuration changed since the prior freeze but does not supersede the exact '
                                 'configuration it binds')
    except tr.Refused as exc:
        raise stop('CONFIG_UNREVIEWED', 'transition: %s' % exc)
    except Unresolvable as exc:
        raise stop('UNRESOLVABLE', 'transition: %s' % exc)
    return {'descriptor': {'path': dpath, 'blob_sha256': util.sha256(table[dpath])}, 'base': B,
            'tips': tips, 'chains': chains, 'roots': [chains[x['role']][0] for x in roles if x['role'] == 'allow'],
            'prior': pc}


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
            # R6.HP.1: the subject's pull-request numbers are exactly the pinned one; a subject that names another
            # number (or none) is CONFIG_INVALID. Whole numbers only: #70 does not name #7.
            named = set(re.findall(r'#(\d+)(?!\d)', repo.subject(m['commit'])))
            if named != {str(m['pr']).lstrip('#')}:
                raise stop('CONFIG_INVALID', 'merge %s subject names pull request %s, not its pinned %s'
                           % (m['commit'][:12], sorted(named) or 'none', m['pr']))

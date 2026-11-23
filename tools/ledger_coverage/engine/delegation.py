"""Delegation contract oi-delegation/1: exact paths per class, verified by admitted class adapters (sec. 7)."""
import json
import os

from . import outcome as oc
from . import util

delegation_schema = 'oi-delegation/1'


class Delegation:
    def __init__(self, doc, modules):
        if doc.get('schema') != delegation_schema:
            raise oc.Stop(oc.error, 'CONFIG_INVALID', 'unknown delegation schema')
        self.doc = doc
        self.modules = modules  # {adapter name: module}
        for c in doc['classes']:
            if c['adapter'] not in modules:
                raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'delegation class %s has no class adapter' % c['id'])
            for p in c.get('paths', []):
                if '*' in p or p.endswith('/') and c.get('kind') != 'record-dir':
                    raise oc.Stop(oc.error, 'CONFIG_INVALID', 'delegation paths must be exact: %s' % p)

    def paths(self):
        return [p for c in self.doc['classes'] for p in c.get('paths', []) if not p.endswith('/')]

    def record_prefixes(self):
        return [p for c in self.doc['classes'] for p in c.get('paths', []) if p.endswith('/')]

    def owns_ledgered(self, path):
        return any(path in c.get('ledgered_paths', []) for c in self.doc['classes'])

    def verify(self, repo, roles, evidence_dir, ledger):
        """Returns the items delegated-evidence-missing (review) or delegated-evidence-invalid (fail) per class."""
        items = []
        report = []
        for c in self.doc['classes']:
            mod = self.modules[c['adapter']]
            ev = {}
            for name in c.get('evidence', []):
                p = os.path.join(evidence_dir, name) if evidence_dir else None
                ev[name] = open(p, 'rb').read() if p and os.path.isfile(p) else None
            try:
                res = mod.verify(repo, roles, c, ev, ledger)
            except Exception as exc:
                res = [('fail', 'class adapter raised %s: %s' % (type(exc).__name__, exc))]
            state = 'pass'
            for st, why in res:
                if st == 'fail':
                    state = 'fail'
                    items.append(oc.make_item('DELEGATED', 'delegated-evidence-invalid', '%s: %s' % (c['id'], why),
                                              None, {'class': c['id'], 'why': why}, delegated_class=c['id']))
                elif st == 'missing':
                    state = 'missing' if state == 'pass' else state
                    items.append(oc.make_item('DELEGATED', 'delegated-evidence-missing', '%s: %s' % (c['id'], why),
                                              None, {'class': c['id'], 'why': why}, delegated_class=c['id']))
            report.append({'class': c['id'], 'adapter': c['adapter'], 'state': state,
                           'evidence': {k: (util.sha256(v) if v is not None else None) for k, v in ev.items()}})
        return items, report

"""Independent outcome checker (S7): recomputes the outcome of a result.json without importing the engine."""
import json
import sys

codes = {'PASS': 0, 'REVIEW_REQUIRED': 10, 'FAIL': 20, 'USAGE': 64, 'ERROR': 65, 'VOID': 70, 'INTERNAL': 71}


def recompute(doc):
    if doc.get('outcome') in ('USAGE', 'ERROR', 'INTERNAL'):
        return doc['outcome']
    if doc.get('outcome') == 'VOID' and doc.get('stop'):
        return 'VOID'
    if any(not p.get('passed') for p in doc.get('preflight', [])):
        return 'VOID'
    rc = doc.get('record_checks')
    if rc is not None and not rc.get('holds'):
        return 'FAIL'
    decisions = [i.get('decision') for i in doc.get('items', [])]
    if 'FAIL' in decisions:
        return 'FAIL'
    if 'REVIEW_REQUIRED' in decisions:
        return 'REVIEW_REQUIRED'
    return 'PASS'


def accept(doc, exit_status, pins):
    """The acceptance predicate of sec. 5: exit 0, schema, the passing outcome recomputed, pinned blobs equal."""
    if exit_status != 0 or doc.get('schema') != 'oi-ledger-coverage/4':
        return False
    if doc.get('outcome') != 'PASS' or recompute(doc) != 'PASS' or doc.get('exit_status') != 0:
        return False
    eng = doc.get('engine', {})
    if pins.get('engine') is not None and eng.get('blob_sha256') != pins['engine']:
        return False
    for a in doc.get('adapters', []):
        want = pins.get('adapters', {}).get(a.get('name'))
        if want is not None and a.get('module_sha256') != want:
            return False
    if pins.get('config') is not None and doc.get('config', {}).get('blob_sha256') != pins['config']:
        return False
    return True


if __name__ == '__main__':
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    r = recompute(d)
    print(json.dumps({'recomputed': r, 'recorded': d.get('outcome'), 'agree': r == d.get('outcome')}))
    sys.exit(0 if r == d.get('outcome') else 1)

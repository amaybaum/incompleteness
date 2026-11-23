"""Independent outcome checker (S7) and the consumer's acceptance predicate (sec. 5), without the engine."""
import gzip
import hashlib
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


def admission_mode(doc):
    adm = doc.get('config', {}).get('admission')
    return adm.get('mode') if isinstance(adm, dict) else adm


def accept(doc, exit_status, pins):
    """Offline part of the acceptance predicate. pins: the consumer's own expectations: engine, adapters,
    config, and admission ({freeze, designation_comment_id, pin_table_sha256, authority_sha256}).
    A result whose admission is not the review chain, or that carries a harness marker, is never accepted."""
    if exit_status != 0 or doc.get('schema') != 'oi-ledger-coverage/4':
        return False
    if 'harness' in doc or admission_mode(doc) != 'chain':
        return False
    if doc.get('outcome') != 'PASS' or recompute(doc) != 'PASS' or doc.get('exit_status') != 0:
        return False
    eng = doc.get('engine', {})
    if pins.get('engine') is None or eng.get('blob_sha256') != pins['engine']:
        return False
    for a in doc.get('adapters', []):
        want = pins.get('adapters', {}).get(a.get('name'))
        if want is None or a.get('module_sha256') != want:
            return False
    if pins.get('config') is None or doc.get('config', {}).get('blob_sha256') != pins['config']:
        return False
    snap = doc['config']['admission'].get('snapshot') or {}
    want = pins.get('admission') or {}
    for key in ('freeze', 'designation_comment_id', 'pin_table_sha256', 'authority_sha256'):
        if want.get(key) is None or snap.get(key) != want[key]:
            return False
    return True


def accept_with_host(doc, exit_status, pins, host, landing):
    """The full predicate: the offline part, then trust-root points 1-3 repeated from the host by the consumer,
    the evaluated commits against the landing record, and the result file against the run's artifact."""
    if not accept(doc, exit_status, pins):
        return False
    snap = doc['config']['admission']['snapshot']
    run = host.run_record(snap['run']['run_id'], pins['repository_id'])
    if run is None or run['repository_id'] != pins['repository_id'] or run.get('fork'):
        return False
    if run['workflow_path'] != pins['workflow_path'] or run['head_sha'] != snap['run']['head_sha']:
        return False
    main = host.main_head(run['repository_id'])
    if not host.on_first_parent_chain(run['repository_id'], run['head_sha'], main):
        return False
    wf = host.file_at(run['repository_id'], run['head_sha'], pins['workflow_path'])
    if wf is None or hashlib.sha256(wf).hexdigest() != pins['workflow_sha256']:
        return False
    for path, want in pins['engine_pins'].items():
        b = host.file_at(run['repository_id'], run['head_sha'], path)
        if b is None or hashlib.sha256(b).hexdigest() != want:
            return False
    # point 3 (K7): only the pinned files, the authority record and the workflow, each a regular file
    a_path = 'tools/ledger_coverage/authority.json'
    permitted = {a_path: pins.get('authority_blob_sha256'), pins['workflow_path']: pins['workflow_sha256']}
    for path, kind in host.entries_at(run['repository_id'], run['head_sha'], a_path.rsplit('/', 1)[0] + '/'):
        if kind != 'file' or (path not in pins['engine_pins'] and path not in permitted):
            return False
        if path in permitted and path not in pins['engine_pins']:
            b = host.file_at(run['repository_id'], run['head_sha'], path)
            if b is None or hashlib.sha256(b).hexdigest() != permitted[path]:
                return False
    if snap.get('evaluated') != landing.get('evaluated'):
        return False
    art = host.artifact_sha256(run['repository_id'], snap['run']['run_id'], landing.get('artifact_name'))
    if art is None or art != landing.get('result_sha256'):
        return False
    return True


def deterministic_gzip(data):
    """gzip with mtime 0, no file name, level 9 and operating-system byte 255 (sec. 5)."""
    out = bytearray(gzip.compress(data, compresslevel=9, mtime=0))
    out[9] = 255
    return bytes(out)


def verify_compressed(gz, recorded_uncompressed_sha256):
    """Landing check of a committed compressed result (control TR46)."""
    try:
        raw = gzip.decompress(gz)
    except OSError:
        return False
    return hashlib.sha256(raw).hexdigest() == recorded_uncompressed_sha256


if __name__ == '__main__':
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    r = recompute(d)
    print(json.dumps({'recomputed': r, 'recorded': d.get('outcome'), 'agree': r == d.get('outcome'),
                      'admission': admission_mode(d)}))
    sys.exit(0 if r == d.get('outcome') else 1)

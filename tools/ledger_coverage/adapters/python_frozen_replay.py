"""Replay adapter: calls the frozen A1-EXIT ledger tool's functions at its pin, in a materialization.

The frozen main() is never called. Every call is wrapped; no printed text is read.
"""
import json
import os
import subprocess
import sys

INTERFACE = 'replay'
NAME = 'python-frozen-replay'
VERSION = 1
# record directories the frozen tool reads, relative to the directory of its module
SIBLINGS = ['../a1-scope-phase0-20261120', '../a1-scope-phase2-20261120']

DRIVER = r'''
import json, sys
sys.path[:] = [sys.argv[1]] + [p for p in sys.path if 'site-packages' not in p and p != '']
out = {'calls': {}}
def save():
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)
def stop(stage, exc):
    out['exception'] = {'stage': stage, 'class': type(exc).__name__, 'message': str(exc)[:500]}
    save()
    sys.exit(0)
def call(name, fn):
    try:
        value = fn()
    except BaseException as exc:
        stop(name, exc)
    out['calls'][name] = value
    return value
try:
    import ledger_check as L
except BaseException as exc:
    stop('import', exc)
sm = call('load_sitemap', lambda: L.load(L.SITEMAP))
rows = call('load_rows', lambda: L.load(L.ROWS))
call('manuscript_digest', lambda: L.manuscript_digest())
call('build', lambda: L.build())
def rendered():
    blocks = L.render(sm, rows)
    text = open(L.os.path.join(L.HERE, 'LEDGER.md'), encoding='utf-8').read()
    new = text
    for k, v in blocks.items():
        new = L.splice_block(new, k, v)
    return new == text
call('render_equal', rendered)
call('check', lambda: L.check(sm, rows, quiet=True))
call('extended_unmapped', lambda: L.extended_unmapped(sm))
import io, contextlib
def st():
    with contextlib.redirect_stdout(io.StringIO()):
        return bool(L.self_test())
call('self_test', st)
out['sitemap'] = sm
save()
'''


def materialize(read, pin, record_commit, module_path, corpus_paths, root):
    """Write the pin's corpus and the record directories at record_commit under root; returns the module dir."""
    mdir = os.path.dirname(module_path)
    dirs = [mdir] + [os.path.normpath(os.path.join(mdir, s)) for s in SIBLINGS]
    for p in corpus_paths:
        dst = os.path.join(root, p)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(read(pin, p))
    for d, files in read.listing(record_commit, dirs):
        for p, data in files:
            dst = os.path.join(root, p)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, 'wb') as f:
                f.write(data)
    return os.path.join(root, mdir)


def replay(read, pin, record_commit, module_path, corpus_paths, root):
    mod_dir = materialize(read, pin, record_commit, module_path, corpus_paths, root)
    drv = os.path.join(root, 'replay-driver.py')
    with open(drv, 'w', encoding='utf-8') as f:
        f.write(DRIVER)
    res = os.path.join(root, 'replay-result.json')
    r = subprocess.run([sys.executable, '-I', '-B', drv, mod_dir, res], capture_output=True, cwd=root)
    if r.returncode != 0 or not os.path.exists(res):
        return {'equalities': [], 'errors': ['replay process exited %d' % r.returncode], 'self_test': False}
    with open(res, encoding='utf-8') as f:
        out = json.load(f)
    if 'exception' in out:
        return {'exception': out['exception'], 'calls': list(out['calls'])}
    val = out['calls'].get
    with open(os.path.join(mod_dir, 'sitemap.json'), encoding='utf-8') as f:
        frozen = json.load(f)
    eq = [{'name': 'digest_equal', 'equal': val('manuscript_digest') == frozen.get('manuscript_digest')},
          {'name': 'rebuild_equal', 'equal': val('build') == frozen},
          {'name': 'render_equal', 'equal': val('render_equal') is True},
          {'name': 'ck_errors_empty', 'equal': val('check') == []},
          {'name': 'extended_unmapped_empty', 'equal': val('extended_unmapped') == []}]
    return {'equalities': eq, 'errors': [], 'self_test': val('self_test') is True,
            'ck_errors': val('check'), 'extended_unmapped': val('extended_unmapped'),
            'sites': len(frozen.get('sites', []))}

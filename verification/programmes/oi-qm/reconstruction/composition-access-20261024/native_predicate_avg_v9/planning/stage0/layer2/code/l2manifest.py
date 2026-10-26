"""NP-AVG-1 Stage 0 Layer 2: the code manifest (certificate item 1).

LAYER2-MANIFEST.json, beside this file, lists the SHA-256 of every .py file in this
directory and the configuration digest (l2config.config_sha256). code_digest is the
SHA-256 of the canonical JSON of {files, config_sha256}; every structured output records
it, and the merge refuses outputs whose code_digest differs.

Usage: python3 -I -B l2manifest.py --verify   (exit 0 if the manifest matches, else prints
                                              VOID JSON and exits 2)
       python3 -I -B l2manifest.py --write    (regenerate; used at the Layer-2 freeze)
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = 'LAYER2-MANIFEST.json'
sys.path.insert(0, HERE)
import l2config as CFG  # noqa: E402


def sha_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def compute(code_dir=HERE):
    files = {fn: sha_file(os.path.join(code_dir, fn)) for fn in sorted(os.listdir(code_dir)) if fn.endswith('.py')}
    body = {'files': files, 'config_sha256': CFG.config_sha256()}
    return dict(body, schema='np-avg-1/stage0/layer2/manifest/1', code_digest=digest(body))


def digest(body):
    return hashlib.sha256(CFG.canonical({'files': body['files'], 'config_sha256': body['config_sha256']}).encode()).hexdigest()


def load(code_dir=HERE):
    with open(os.path.join(code_dir, NAME)) as f:
        return json.load(f)


def verify(code_dir=HERE):
    """(ok, differences, recorded manifest or None)."""
    try:
        rec = load(code_dir)
    except (OSError, ValueError) as e:
        return False, ['manifest unreadable: %s' % type(e).__name__], None
    cur = compute(code_dir)
    diffs = []
    for fn in sorted(set(rec.get('files', {})) | set(cur['files'])):
        a, b = rec.get('files', {}).get(fn), cur['files'].get(fn)
        if a != b:
            diffs.append('%s: recorded %s, present %s' % (fn, a, b))
    if rec.get('config_sha256') != cur['config_sha256']:
        diffs.append('config digest differs')
    if 'files' not in rec or 'config_sha256' not in rec or rec.get('code_digest') != digest(rec):
        diffs.append('recorded code_digest inconsistent')
    return not diffs, diffs, rec


def main():
    if '--write' in sys.argv[1:]:
        m = compute()
        m['status'] = 'draft: WIP / UNREVIEWED, not frozen'
        with open(os.path.join(HERE, NAME), 'w') as f:
            json.dump(m, f, indent=1, sort_keys=True)
            f.write('\n')
        print(json.dumps({'written': NAME, 'code_digest': m['code_digest']}, sort_keys=True))
        return
    ok, diffs, rec = verify()
    out = {'manifest_ok': ok, 'differences': diffs, 'code_digest': rec.get('code_digest') if rec else None}
    if not ok:
        out['label'] = 'VOID'
        out['reason'] = 'certificate item 1: code or configuration differs from the manifest'
    print(json.dumps(out, sort_keys=True))
    sys.exit(0 if ok else 2)


if __name__ == '__main__':
    main()

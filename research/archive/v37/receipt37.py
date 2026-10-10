#!/usr/bin/env python3
"""Scratch: V3-7 receipt builder for pilot round PILOT-SB1. Never landed.

build_receipt(repo_dir, d, f, e, lb, lam, recs, attest) returns the receipt JSON text for a
complete, non-sealing round, every field derived from the repository with tools/v3_verifier.py's
own functions (S4, S7, S8). `attest` is a list of (kind, subject, commit, record)."""
import json
import os
import sys
import types


def load_tool(repo_dir):
    src = open(os.path.join(repo_dir, 'tools', 'v3_verifier.py'), encoding='utf-8').read()
    m = types.ModuleType('v3tool')
    m.__file__ = os.path.join(repo_dir, 'tools', 'v3_verifier.py')
    exec(compile(src, 'v3tool', 'exec'), m.__dict__)
    return m


ROUND = 'PILOT-SB1'
RDIR = 'verification/infrastructure/v3/pilots/round-pilot-sb1/'


def build_receipt(repo_dir, d, f, e, lb, lam, recs, attest):
    t = load_tool(repo_dir)
    repo = t.Repo(repo_dir)
    fmt = repo.fmt()
    cp = {p: o for p, (mode, o) in repo.entries(f).items()
          if p == (RDIR + 'preregistration.md').encode() or p.startswith((RDIR + 'amendments/').encode())}
    pre = repo.blob(cp[(RDIR + 'preregistration.md').encode()]).decode('utf-8')
    entries = t.parse_governed_text(pre)
    assert not isinstance(entries, str), entries
    r = {
        'schema': 'v3-receipt', 'version': 1, 'round': ROUND, 'status': 'complete',
        'kind': 'non-sealing', 'object_format': fmt, 'd': d, 'f': f,
        'control_plane_blobs': [{'path': p.decode('utf-8'), 'blob': cp[p]} for p in sorted(cp)],
        'governed_paths_digest': t.governed_digest(entries),
        'e': e, 'tree_e': repo.tree(e),
        'execution_delta_digest': t.delta_digest(repo.delta(f, e), fmt),
        'candidates': [],
        'landing': {'base': lb, 'object': lam, 'reconciliations': list(recs),
                    'resolved_paths': [], 'delta_digest': t.delta_digest(repo.delta(lb, lam), fmt)},
        'attestations': [{'kind': k, 'subject': s, 'commit': c, 'record': rec}
                         for k, s, c, rec in attest],
    }
    assert not t.validate_receipt(r), t.validate_receipt(r)
    return json.dumps(r, indent=2, ensure_ascii=False) + '\n'


if __name__ == '__main__':
    # usage: receipt37.py <repo> <d> <f> <e> <lb> <lambda> <attest.json> <recon>...
    repo_dir, d, f, e, lb, lam, att = sys.argv[1:8]
    recs = sys.argv[8:]
    attest = [tuple(x) for x in json.load(open(att, encoding='utf-8'))]
    sys.stdout.write(build_receipt(repo_dir, d, f, e, lb, lam, recs, attest))

"""Delegation class adapter artifact-hash/1 (synthetic configuration): a declared file must equal the hex
SHA-256 of the declared source files' bytes, concatenated in order, with a final LF."""
import hashlib

INTERFACE = 'delegation'
NAME = 'artifact-hash'
VERSION = 1


def verify(repo, roles, cls, evidence, ledger):
    X = roles.get('candidate')
    art = repo.read(X, cls['paths'][0])
    if art is None:
        return [('missing', 'artifact %s absent at the candidate' % cls['paths'][0])]
    h = hashlib.sha256()
    for p in cls['params']['sources']:
        h.update(repo.read(X, p) or b'')
    if art != (h.hexdigest() + '\n').encode():
        return [('fail', 'artifact does not equal its recipe')]
    return []

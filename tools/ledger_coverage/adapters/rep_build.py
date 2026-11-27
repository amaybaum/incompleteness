"""The representative retirement candidate X_rep of design r6 R6.EVID.8 (OC-3), built from H, the pinned ledger and
edit list and the configuration's control instance alone.

X_rep has exactly one parent, H, and the fixed subject SUBJECT. Each ledgered path carries H's bytes with the ledger's
splices applied, and its sha256 equals the ledger's `expected_sha256` for the path; the plan's record-directory paths
`ledger.json` and `edits.json` carry the pinned ledger and edit list; each file path of the configuration's delegated
classes that is not ledgered (R6.TREE.9: a path is in exactly one class) carries a fixed marker blob that differs from its blob at H (the runner checks it also differs at the run's
M); every other path equals H. `changes` returns the change set; the caller derives the commit in its own reader
(R6.TREE.15), so the commit and tree ids are a function of H and the change set, which is a function of H, the
ledger, the edit list and the configuration.

This module imports only the standard library and nothing from the tool's engine (R6.EVID.8; REP-BUILD checks the
import set from this file's own syntax tree before the module is loaded).
"""
import hashlib
import json

SUBJECT = 'X_rep: the representative retirement candidate of design r6 R6.EVID.8'
MARKER = b'X_rep delegated-path marker (design r6 R6.EVID.8): %s\n'
ALLOWED_IMPORTS = ('hashlib', 'json')


class Refused(Exception):
    """The inputs do not determine a representative candidate; the message is the reason."""


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def delegated_paths(delegation_doc):
    """The file paths of the delegation contract's classes (a class path ending in `/` names a directory, the plan's
    record directory, whose files are the record-directory paths and keep H's bytes or the pinned inputs)."""
    out = set()
    for c in (delegation_doc or {}).get('classes') or []:
        for p in (c.get('paths') or []) if isinstance(c, dict) else []:
            if isinstance(p, str) and p and not p.endswith('/'):
                out.add(p)
    return sorted(out)


def changes(h, ledger_bytes, edits_bytes, delegation_doc, read_h, plan_dir):
    """{path: bytes} of X_rep against H. read_h(path) returns H's bytes at a path, or None where H has no file."""
    try:
        ledger = json.loads(ledger_bytes.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        raise Refused('the pinned ledger is not JSON')
    if not isinstance(ledger, dict) or not isinstance(ledger.get('files'), dict) or \
            not isinstance(ledger.get('splices'), list):
        raise Refused('the pinned ledger has no files and splices')
    if ledger.get('base') != h:
        raise Refused('the pinned ledger\'s base is not H')
    if ledger.get('edits_sha256') != _sha(edits_bytes):
        raise Refused('the pinned edit list is not the one the ledger names')
    by_file = {}
    for s in ledger['splices']:
        if not isinstance(s, dict) or s.get('file') not in ledger['files']:
            raise Refused('a splice names a file outside the ledger\'s files')
        by_file.setdefault(s['file'], []).append(s)
    out = {}
    for path in sorted(ledger['files']):
        want = ledger['files'][path]
        base = read_h(path)
        if base is None or _sha(base) != want.get('base_sha256'):
            raise Refused('a ledgered path\'s bytes at H differ from the ledger\'s base_sha256: %s' % path)
        body = base
        spl = sorted(by_file.get(path, []), key=lambda s: (s['start'], s['end']))
        for a, b in zip(spl, spl[1:]):
            if b['start'] < a['end']:
                raise Refused('two splices of %s overlap' % path)
        for s in reversed(spl):
            new = s.get('new')
            if not isinstance(new, str) or _sha(base[s['start']:s['end']]) != s.get('old_sha256') or \
                    _sha(new.encode('utf-8')) != s.get('new_sha256'):
                raise Refused('splice %s does not apply to H\'s bytes of %s' % (s.get('id'), path))
            body = body[:s['start']] + new.encode('utf-8') + body[s['end']:]
        if _sha(body) != want.get('expected_sha256'):
            raise Refused('a ledgered path\'s sha256 differs from the ledger\'s expected_sha256: %s' % path)
        if body != base:
            out[path] = body
    pinned = {plan_dir + 'ledger.json': ledger_bytes, plan_dir + 'edits.json': edits_bytes}
    for p, b in pinned.items():
        if p in ledger['files']:
            raise Refused('a plan record-directory path is ledgered: %s' % p)
        out[p] = b
    for p in delegated_paths(delegation_doc):
        # a path is in exactly one class (R6.TREE.9) and a ledgered file equals H plus its splices, so a ledgered path
        # that a delegated class also names (the coverage ledger) keeps its ledgered bytes
        if p in ledger['files']:
            continue
        if p in pinned:
            raise Refused('a delegated path is a plan record-directory path: %s' % p)
        m = MARKER % p.encode('utf-8')
        if read_h(p) == m:
            raise Refused('the marker blob equals H\'s blob at %s' % p)
        out[p] = m
    return out

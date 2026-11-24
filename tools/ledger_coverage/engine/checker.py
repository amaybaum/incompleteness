"""Independent outcome checker (S7) and the consumer's acceptance predicate (sec. 5), without the engine."""
import gzip
import hashlib
import json
import re
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


# The `uses:` line rule on the workflow blob's raw text (sec. 6.3, execution identity point 5; no YAML parser). It only
# refuses: a line containing `uses` in any letter case that is not exactly an action named by a full commit id, its
# owner a GitHub account name (letters, digits and single inner hyphens, so no local or parent path); a line
# whose first character after its indentation and any `-` or `---` markers is a quote, a flow collection, a complex
# key, an anchor, an alias or a tag; a colon followed by whitespace and then a flow collection, anchor, alias or tag.
_uses = re.compile(r'^\s*(- )?uses: [A-Za-z0-9](?:-?[A-Za-z0-9])*/[A-Za-z0-9_.-]+(/[^@\s]+)?@[0-9a-f]{40}\s*$')
_uses_word = re.compile(r'uses', re.I)
_prefix = re.compile(r'^\s*((-|---)\s+)*')
_value = re.compile(r':\s+[{[&*!]')


def uses_line_problems(blob):
    """[(line number, reason)] of every line of a workflow blob the line rule refuses; [] when it passes."""
    try:
        text = blob.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        return [(0, 'not utf-8 text')]
    out = []
    for n, line in enumerate(text.split('\n'), 1):
        if _uses_word.search(line) and not _uses.match(line):
            out.append((n, 'a uses line that does not name an action by a full commit id'))
            continue
        rest = line[_prefix.match(line).end():]
        if rest[:1] and rest[:1] in '"\'{[?&*!':
            out.append((n, 'an entry starting with %r' % rest[:1]))
            continue
        if _value.search(line):
            out.append((n, 'a flow collection, anchor, alias or tag as a value'))
    return out


def accept(doc, exit_status, pins):
    """Offline part of the acceptance predicate (sec. 5). pins: the consumer's own expectations, from the landing
    record and the configuration at F: {'config': {path, blob_sha256}, 'adapters': {name: module sha256}, 'freeze': F,
    'pin_table': {path, blob_sha256}, 'tool': the configuration's tool pins}. A result whose admission is not
    "chain", or that carries a harness marker, is never accepted."""
    if exit_status != 0 or doc.get('schema') != 'oi-ledger-coverage/5':
        return False
    if 'harness' in doc or admission_mode(doc) != 'chain':
        return False
    if doc.get('outcome') != 'PASS' or recompute(doc) != 'PASS' or doc.get('exit_status') != 0:
        return False
    for a in doc.get('adapters', []):
        want = (pins.get('adapters') or {}).get(a.get('name'))
        if want is None or a.get('module_sha256') != want:
            return False
    cfg = doc.get('config') or {}
    if pins.get('config') is None or {'path': cfg.get('path'), 'blob_sha256': cfg.get('blob_sha256')} != pins['config']:
        return False
    snap = cfg['admission'].get('snapshot') or {}
    if pins.get('freeze') is None or snap.get('freeze') != pins['freeze'] or cfg.get('commit') != pins['freeze']:
        return False
    if pins.get('pin_table') is None or snap.get('pin_table') != pins['pin_table']:
        return False
    if snap.get('configuration') != pins['config']:
        return False
    tool = pins.get('tool') or {}
    want_files = {f['path']: f['blob_sha256'] for f in tool.get('files', [])}
    if not want_files or snap.get('tool_blobs') != want_files or snap.get('workflow') != tool.get('workflow'):
        return False
    return True


def accept_with_host(raw, exit_status, pins, host, landing, repo):
    """The full predicate over the result file's raw bytes (sec. 5): the offline part, then execution identity
    points 1-3, the `uses:` rule of point 5 and point 6 repeated by the consumer from the host's rest records and from
    its own verified object store `repo`, the evaluated commits against the landing record, and the result file against
    the run's artifact. pins as for `accept`, plus 'repository_id' (the configuration's). landing: {'evaluated',
    'artifact_name', 'result_sha256', 'main'} with `main` the M re-resolved as sec. 13.4 states. The consumer hashes the
    bytes it is given itself; any failed or incomplete host read is non-acceptance."""
    if not isinstance(raw, bytes):
        return False
    try:
        doc = json.loads(raw.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return False
    if not isinstance(doc, dict) or not accept(doc, exit_status, pins):
        return False
    snap = doc['config']['admission']['snapshot']
    rid = pins.get('repository_id')
    tool = pins['tool']
    try:
        run = host.run_record((snap.get('run') or {}).get('run_id'), rid)
        if not isinstance(run, dict):
            return False
        if run.get('repository_id') != rid or run.get('head_repository_id') != rid or \
                run.get('event') not in ('push', 'workflow_dispatch'):
            return False
        T = run.get('head_sha')
        if T != snap.get('tool_commit') or run.get('workflow_path') != tool['workflow']['path']:
            return False
        ents = repo.entries(repo.resolve(T))
        pins_f = {f['path']: f['blob_sha256'] for f in tool['files']}
        # the entry point is the pinned module whose name, less `.py`, is the directory of the other pinned files
        entries_py = [p for p in pins_f if p.endswith('.py') and any(q.startswith(p[:-3] + '/') for q in pins_f)]
        if len(entries_py) != 1:
            return False
        pkg = entries_py[0][:-3] + '/'
        mine = {p: e for p, e in ents.items() if p == entries_py[0] or p.startswith(pkg)}
        if set(mine) != set(pins_f):
            return False
        for p, (mode, _) in mine.items():
            if mode not in ('100644', '100755') or hashlib.sha256(repo.read(T, p)).hexdigest() != pins_f[p]:
                return False
        wf = repo.read(T, tool['workflow']['path'])
        if wf is None or hashlib.sha256(wf).hexdigest() != tool['workflow']['blob_sha256'] or uses_line_problems(wf):
            return False
        M = landing.get('main')
        if not isinstance(M, str) or not _on_first_parent_chain(repo, T, M):
            return False
        if snap.get('evaluated') != landing.get('evaluated'):
            return False
        art = host.artifact_sha256(rid, snap['run']['run_id'], landing.get('artifact_name'))
    except Exception:  # a failed or incomplete read, or an object the verified reader refuses: non-acceptance
        return False
    if art is None or art != landing.get('result_sha256') or hashlib.sha256(raw).hexdigest() != art:
        return False
    return True


def _on_first_parent_chain(repo, a, b):
    c = b
    while True:
        if c == a:
            return True
        ps = repo.parents(c)
        if not ps:
            return False
        c = ps[0]


def resolve_main(ls_remote, repo, landing_first_parent):
    """Sec. 13.4: re-resolve `M` immediately before landing. `ls_remote()` returns (exit status, stdout) of
    `git ls-remote <repository> refs/heads/main`. Returns M, or raises ValueError, refusing the landing, on a failed
    command, an output without exactly one `refs/heads/main` line, an id that is not a full 40-hex id or that the
    verified reader `repo` cannot read, or an id other than L's first parent (control EI5)."""
    try:
        code, out = ls_remote()
    except Exception as exc:
        raise ValueError('git ls-remote failed: %s' % exc)
    if code != 0:
        raise ValueError('git ls-remote exited %s' % code)
    lines = [l for l in (out or '').split('\n') if l.strip()]
    hits = [l.split('\t') for l in lines if l.endswith('\trefs/heads/main')]
    if len(hits) != 1 or len(hits[0]) != 2:
        raise ValueError('git ls-remote returned %d refs/heads/main lines' % len(hits))
    M = hits[0][0]
    if not re.match(r'^[0-9a-f]{40}$', M):
        raise ValueError('the resolved main is not a full 40-hex id')
    try:
        repo.resolve(M)
    except Exception as exc:
        raise ValueError('the resolved main cannot be read: %s' % exc)
    if M != landing_first_parent:
        raise ValueError('the resolved main is not the landing\'s first parent')
    return M


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

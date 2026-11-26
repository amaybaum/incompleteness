"""Independent check of the category-3 read domain a result records (OBL-29 r9 sec. 5.3, R6.EVID.8): every
tree-derived record read comes from a named root of the walk or from that root's verified history, under the fixed
prefix, at the recorded blob; every explicitly read record names its admitted source. Imports nothing from the engine:
it reads the result and a reader with parents(c), read(c, path) (bytes or None)."""
import hashlib


PREFIX = 'verification/audits/'


def problems(reader, result, roots, sources=()):
    """[problem] for the read domain of one result; `roots` are the run's M, F and REV as the caller knows them, and
    `sources` the commits an explicitly read record may come from (the configuration commit and the admitted REVs)."""
    rd = result.get('category3_read_domain')
    if not isinstance(rd, dict):
        return ['no category-3 read domain recorded']
    out = []
    if sorted(rd.get('roots') or []) != sorted(r for r in roots if r):
        out.append('the recorded roots %r are not the run\'s roots' % (rd.get('roots'),))
    seen, stack = set(), [r for r in roots if r]
    while stack:
        c = stack.pop()
        if c in seen:
            continue
        seen.add(c)
        stack.extend(reader.parents(c))
    prefix = PREFIX
    if rd.get('prefix') != PREFIX:
        out.append('the recorded prefix %r is not %s' % (rd.get('prefix'), PREFIX))
    for x in rd.get('reads') or []:
        c, p, b = x.get('commit'), x.get('path'), x.get('blob_sha256')
        if c not in seen:
            out.append('%s read from %s, outside the roots\' history' % (p, c))
            continue
        if not isinstance(p, str) or not p.startswith(prefix):
            out.append('%s is outside %s' % (p, prefix))
            continue
        data = reader.read(c, p)
        if data is None or hashlib.sha256(data).hexdigest() != b:
            out.append('%s at %s is not the recorded blob' % (p, c))
    for x in rd.get('explicit') or []:
        src, p, b = x.get('source'), x.get('path'), x.get('blob_sha256')
        if src not in set(sources):
            out.append('explicit record %s names a source %r that is neither the configuration commit nor an admitted '
                       'REV' % (p, src))
            continue
        data = reader.read(src, p) if isinstance(p, str) else None
        if data is None or hashlib.sha256(data).hexdigest() != b:
            out.append('explicit record %s is not present at its source with its blob' % p)
    return out

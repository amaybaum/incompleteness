"""Independent check of the category-3 read domain a result records (OBL-29 r9 sec. 5.3, R6.EVID.8): every
tree-derived record read comes from a named root of the walk or from that root's verified history, under the fixed
prefix, at the recorded blob; every explicitly read record names its admitted source. Imports nothing from the engine:
it reads the result and a reader with parents(c), read(c, path) (bytes or None)."""
import hashlib


def problems(reader, result, roots):
    """[problem] for the read domain of one result; `roots` are the run's M, F and REV as the caller knows them."""
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
    prefix = rd.get('prefix') or ''
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
        if not x.get('source'):
            out.append('explicit record %s names no admitted source' % x.get('path'))
    return out

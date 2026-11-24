"""Site anchors and relocation through ledgered and unledgered segments (v1 sec. 4.2-4.4; sec. 3, 5)."""
import difflib

from . import util


class FileText:
    """A file at a tree: bytes, decoded lines, byte spans of the lines, and a line index."""

    def __init__(self, data, where):
        self.data = data if data is not None else b''
        self.exists = data is not None
        self.text = util.decode(self.data, where) if data is not None else ''
        self.lines = util.lines_of(self.text)
        self.spans = util.line_spans(self.data)
        self._index = None

    def index(self):
        if self._index is None:
            ix = {}
            for i, l in enumerate(self.lines):
                ix.setdefault(l, []).append(i)
            self._index = ix
        return self._index

    def occurrences(self, block):
        """0-based start indices where block occurs as a whole-line block."""
        if not block:
            return []
        out = []
        n = len(block)
        for i in self.index().get(block[0], []):
            if self.lines[i:i + n] == block:
                out.append(i)
        return out


def overlaps(s_start, s_end, a, b):
    """Sec. 5: start < site_end and end > site_start (an interior zero-length splice overlaps)."""
    return s_start < b and s_end > a


def apply_splices(data, splices):
    out = []
    pos = 0
    for sp in sorted(splices, key=lambda x: (x['start'], x['end'])):
        out.append(data[pos:sp['start']])
        out.append(sp['new_bytes'])
        pos = sp['end']
    out.append(data[pos:])
    return b''.join(out)


def translate(off, splices):
    d = 0
    for sp in splices:
        if sp['end'] <= off:
            d += len(sp['new_bytes']) - (sp['end'] - sp['start'])
    return off + d


def diff_ranges(expected, actual):
    """Line ranges of actual that differ from expected (diagnostic only)."""
    a = util.lines_of(expected.decode('utf-8', 'replace'))
    b = util.lines_of(actual.decode('utf-8', 'replace'))
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != 'equal':
            out.append([j1 + 1, max(j1 + 1, j2)])
    return out


def deletion_kind(from_lines, to_lines, idx):
    """Diagnostic for a site not found: replaced (unauthorized-change) or deleted (missing)."""
    sm = difflib.SequenceMatcher(None, from_lines, to_lines, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if i1 <= idx < i2:
            if tag == 'delete':
                return 'missing'
            if tag == 'replace':
                return 'unauthorized-change'
            return 'unauthorized-change'
    return 'missing'


def whitespace_only(a, b):
    return ' '.join(a.split()) == ' '.join(b.split())


class SiteState:
    """Mutable relocation state of one site."""

    def __init__(self, site, file, start, block, count):
        self.site = site
        self.file = file
        self.start = start          # 0-based line index of the block in the current tree
        self.block = list(block)    # current lines
        self.count = count          # occurrences of the block at the previous endpoint
        self.resolved = True
        self.status = 'unchanged'
        self.segment_status = {}
        self.splice_ids = []
        self.image_lines = None     # [first, last] 1-based in the current tree after a replacement
        self.hp = False
        self.text_unchanged = True  # the site's own bytes equal its classified bytes


def search_relocate(st, ft_from, ft_to, ctx_from):
    """Unledgered rules (v1 sec. 4.4) for one resolved site; returns (status, class or None, detail)."""
    occ = ft_to.occurrences(st.block)
    n = len(occ)
    if n == 0:
        kind = deletion_kind(ft_from.lines, ft_to.lines, st.start)
        ws = False
        if kind == 'unauthorized-change' and len(st.block) == 1:
            sm = difflib.SequenceMatcher(None, ft_from.lines, ft_to.lines, autojunk=False)
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if i1 <= st.start < i2 and tag == 'replace':
                    ws = any(whitespace_only(st.block[0], x) for x in ft_to.lines[j1:j2])
        return 'unresolved', kind, {'whitespace_only': ws}
    if n != st.count:
        return 'unresolved', 'duplicated', {'count_from': st.count, 'count_to': n}
    if n == 1:
        old = st.start
        st.start = occ[0]
        return ('moved' if occ[0] != old else 'unchanged'), None, {'line_delta': occ[0] - old}
    keep = [i for i in occ if util.context_hash_block(ft_to.lines, i, i + len(st.block)) == ctx_from]
    if len(keep) == 1:
        ordinal = occ.index(keep[0]) + 1
        if ordinal == st.site.get('ordinal', 1):
            old = st.start
            st.start = keep[0]
            return ('moved' if keep[0] != old else 'unchanged'), None, {'line_delta': keep[0] - old}
    return 'unresolved', 'ambiguous', {'count': n, 'context_matches': len(keep)}


def ledgered_file(states, ft_from, ft_to, splices, path):
    """Ledgered rules (v1 sec. 4.3) for the conforming file; returns per-state outcomes."""
    sps = sorted(splices, key=lambda x: (x['start'], x['end']))
    out = []
    for st in states:
        if not st.resolved:
            continue
        i0, i1 = st.start, st.start + len(st.block)
        a = ft_from.spans[i0][0]
        b = ft_from.spans[i1 - 1][1]
        hit = [sp for sp in sps if overlaps(sp['start'], sp['end'], a, b)]
        if not hit:
            ta = translate(a, sps)
            want = ft_from.data[a:b]
            occ = ft_to.occurrences(st.block)
            ok_bytes = ft_to.data[ta:ta + len(want)] == want
            tl = util.line_of_offset(ft_to.data, ta) - 1 if ft_to.data else 0
            if ok_bytes and len(occ) == st.count == 1 and occ[0] == tl:
                old = st.start
                st.start = tl
                out.append((st, 'moved' if tl != old else 'unchanged', None, {'line_delta': tl - old}))
            elif ok_bytes and st.count > 1 and tl in occ:
                old = st.start
                st.start = tl
                out.append((st, 'moved' if tl != old else 'unchanged', None, {'line_delta': tl - old}))
            else:
                out.append((st, 'unresolved', 'ambiguous', {'translated_line': tl + 1, 'search': [x + 1 for x in occ]}))
            continue
        ra, rb = a, b
        while True:
            hit = [sp for sp in sps if overlaps(sp['start'], sp['end'], ra, rb)]
            na = min([ra] + [sp['start'] for sp in hit])
            nb = max([rb] + [sp['end'] for sp in hit])
            la = util.line_of_offset(ft_from.data, na) - 1
            lb = util.line_of_offset(ft_from.data, max(na, nb - 1)) - 1
            na, nb = ft_from.spans[la][0], ft_from.spans[lb][1]
            if (na, nb) == (ra, rb):
                break
            ra, rb = na, nb
        local = [dict(sp, start=sp['start'] - ra, end=sp['end'] - ra) for sp in hit]
        new = apply_splices(ft_from.data[ra:rb], local)
        ta = translate(ra, [sp for sp in sps if sp not in hit])
        if ft_to.data[ta:ta + len(new)] != new:
            out.append((st, 'unresolved', 'unauthorized-change', {'reason': 'image differs from the splice result'}))
            continue
        st.splice_ids = sorted(sp['id'] for sp in hit)
        st.from_region = ft_from.data[ra:rb]
        if not new.strip():
            st.resolved = False
            st.removed_at = util.line_of_offset(ft_to.data, ta) if ft_to.data else 1
            out.append((st, 'authorized-removal', None, {'splice_ids': st.splice_ids, 'offset_line': st.removed_at}))
            continue
        first = util.line_of_offset(ft_to.data, ta)
        last = util.line_of_offset(ft_to.data, ta + len(new) - 1)
        block = ft_to.lines[first - 1:last]
        st.block = block
        st.start = first - 1
        st.image_lines = [first, last]
        st.text_unchanged = False
        n = len(ft_to.occurrences(block))
        if n != 1:
            st.resolved = False
            out.append((st, 'unresolved', 'duplicated', {'region_count': n, 'splice_ids': st.splice_ids}))
            continue
        st.count = 1
        out.append((st, 'authorized-replacement', None, {'splice_ids': st.splice_ids, 'lines': [first, last],
                                                         'new_region_sha256': util.sha256(new)}))
    return out


# ---- historical provenance walk (sec. 3.2) ------------------------------------------------------------

def block_sha(lines):
    return util.sha256('\n'.join(lines))


def walk_region(repo, chain, parent_of, path, block, decoded):
    """The region walk of sec. 3.2 for one site. Returns (status, steps, final block)."""
    region = list(block)
    steps = []
    for k, c in enumerate(chain, 1):
        p = parent_of[c]
        bp, bc = repo.blob_id(p, path), repo.blob_id(c, path)
        if bp == bc:
            continue
        lp = decoded(p, path)
        lc = decoded(c, path)
        op, oc = lp.occurrences(region), lc.occurrences(region)
        if len(op) == 1 and len(oc) == 1:
            continue
        if len(op) != 1:
            return 'provenance-ambiguous', steps, region, {'commit': c, 'count_at_parent': len(op)}
        i0 = op[0]
        i1 = i0 + len(region)
        cp = {}
        for l in lp.lines:
            cp[l] = cp.get(l, 0) + 1
        cc = {}
        for l in lc.lines:
            cc[l] = cc.get(l, 0) + 1
        ua = next((j for j in range(i0 - 1, -1, -1) if cp[lp.lines[j]] == 1 and cc.get(lp.lines[j], 0) == 1), None)
        la = next((j for j in range(i1, len(lp.lines)) if cp[lp.lines[j]] == 1 and cc.get(lp.lines[j], 0) == 1), None)
        ca = lc.lines.index(lp.lines[ua]) if ua is not None else -1
        cb = lc.lines.index(lp.lines[la]) if la is not None else len(lc.lines)
        if ca >= cb:
            return 'provenance-ambiguous', steps, region, {'commit': c, 'reason': 'anchors out of order'}
        pre = trim(lp.lines[(ua + 1 if ua is not None else 0):(la if la is not None else len(lp.lines))])
        post = trim(lc.lines[ca + 1:cb])
        steps.append({'commit': c, 'parent': p, 'position': k, 'pre_sha256': block_sha(pre),
                      'post_sha256': block_sha(post), 'post': post})
        region = list(post)
        if not region:
            return 'removed', steps, region, {}
    return ('changed' if steps else 'carried'), steps, region, {}


def trim(lines):
    a, b = 0, len(lines)
    while a < b and not lines[a].strip():
        a += 1
    while b > a and not lines[b - 1].strip():
        b -= 1
    return list(lines[a:b])

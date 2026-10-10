#!/usr/bin/env python3
"""G6 check.py -- independent check of graph.tsv (A1.4 item 4). Read-only; stdout only.

Run from pt/G6/ as `python3 -I -B check.py`. Independent of parse.py / edges.py / classify.py: it imports none
of them and re-reads the record ids, titles and statuses from the four inventories (../I1/INVENTORY.md,
../I2/INVENTORY.md, ../I3/INVENTORY.md, ../I4/records.txt), the kernel at L
(../base/verification/lean-mathlib/OIBridge/*.lean and OIBridge.lean) and the design modules
(../inputs/fourcopy/*.lean, for D: targets only). From graph.tsv it reads the node rows and the edge rows.

CHECKS (decision rule fixed before the first run):
  C0  graph.tsv has exactly the 633 record ids found in the inventories, each with a non-empty kind, status,
      level and class in {a,b,c,d,e}, and every edge source is one of them.                       PASS/FAIL
  C1  every edge target (all kinds, Y included) is a record id, or K:<name> with <name> declared at L, or
      D:<name> declared in a design module.                                                         PASS/FAIL
  C2  the dependency edges (R, RA, RN, KC) between records contain no directed cycle (iterative
      three-colour DFS; the first cycle found is printed).                                          PASS/FAIL
  C3  kernel-signature agreement on the sample below. For a sampled node u, its declarations are the
      theorems named (backticked) in its header block (I1: title, kind, level, status lines; I2, I3: title
      and kind line) or, for I4, the declaration at its src file:line. SIG(u) = heads of the declared
      arguments (binders before the top-level ':' of each declaration, with the file's `variable` binders
      whose names occur in the signature), restricted to heads that name a record or a Prop-valued /
      structure / class / inductive declaration at L, bound names excluded. REC(u) = targets of u's R, RA,
      RN edges; GRAPH(u) = REC(u) plus u's KC targets. A head is represented by a record target whose title
      names it or by K:<head>. Outcome: AGREE-RECORDED (SIG within REC); INCOMPLETE-RECORDED (SIG within
      GRAPH, not within REC); DISAGREE (SIG not within GRAPH, or a K: target or a kernel-status record
      target named nowhere in the declaration's text, signature or proof). Targets that are manuscript
      records (no kernel status) are listed as MS-links, not judged. C3 PASS iff the sample has >= 40 nodes
      with >= 1 from each inventory and no DISAGREE.                                                PASS/FAIL
  Countercontrols (each must behave as stated, else FAIL): CC1 an added edge to 'I9.1' makes C1 fail;
  CC2 an added edge I1.1 -> I1.3 makes C2 find a cycle (I1.3 -> I1.1 is recorded); CC3 removing one SIG
  head's target from GRAPH(u) of the first sampled node with non-empty SIG gives DISAGREE.
  A line 'VERDICT GRAPH CHECKED' prints only if C0-C3 PASS and CC1-CC3 behave.
AMENDMENT before run 2 (18:22Z; run 1 kept as check.run1.{py,out,err}; C0-C2, the sample and CC1-CC3
  unchanged). Run 1 implemented DISAGREE more strictly than NOTES N1, which reads "carries a dependency absent
  from the declaration with no recorded reason", and it looked a target record up by its title only, so a
  record whose kernel name stands in its statement (I1.40, I1.44, I1.45) could never be found. In C3 the
  extra-target test now (i) looks a target record up by every backticked identifier of its title, status and
  statement bullet (representation of SIG heads still uses titles only), and (ii) accepts a recorded reason:
  the target is named in the depends_on text after 'through' or 'via'. Everything else is as before.
AMENDMENT before run 3 (18:23Z; run 2 kept as check.run2.{py,out,err}; rules unchanged): runs 1 and 2 searched
  for a cycle starting from an unordered set, so the cycle printed depended on the interpreter's string-hash
  seed (run 1 printed I2.42 -> I2.56, run 2 I2.10 -> I2.6). The search now starts from the ids in numeric
  order, and C2 also prints every strongly connected component with more than one node (Tarjan, iterative),
  so the output is deterministic and complete.

SAMPLING RULE (fixed before the first run): eligible = graph.tsv rows with derived = 'derived', status
starting 'K' or containing 'proved [K]', kind starting 'theorem'; per inventory, sorted by numeric id; take
the elements at positions floor(j*n/m), j = 0..m-1, with m = 10 for I1 and I2 and m = 12 for I3 and I4 (n =
number eligible: I1 20, I2 22, I3 61, I4 140). A sampled node whose header names no theorem declared at L is
replaced by the next eligible node of its inventory (numeric order, wrapping) not yet sampled; each
replacement is printed. The sample so drawn (44 nodes), listed before the first run:
  I1: I1.27 I1.40 I1.44 I1.46 I1.52 I1.54 I1.62 I1.80 I1.82 I1.84
  I2: I2.21 I2.25 I2.27 I2.30 I2.33 I2.36 I2.39 I2.94 I2.96 I2.98
  I3: I3.12 I3.17 I3.22 I3.28 I3.37 I3.44 I3.53 I3.78 I3.83 I3.90 I3.105 I3.122
  I4: I4.5 I4.19 I4.40 I4.59 I4.83 I4.101 I4.122 I4.142 I4.160 I4.173 I4.192 I4.212
"""
import os
import re

KD = '../base/verification/lean-mathlib/OIBridge'
KR = '../base/verification/lean-mathlib/OIBridge.lean'
DD = '../inputs/fourcopy'
SAMPLE = {'I1': 'I1.27 I1.40 I1.44 I1.46 I1.52 I1.54 I1.62 I1.80 I1.82 I1.84'.split(),
          'I2': 'I2.21 I2.25 I2.27 I2.30 I2.33 I2.36 I2.39 I2.94 I2.96 I2.98'.split(),
          'I3': 'I3.12 I3.17 I3.22 I3.28 I3.37 I3.44 I3.53 I3.78 I3.83 I3.90 I3.105 I3.122'.split(),
          'I4': 'I4.5 I4.19 I4.40 I4.59 I4.83 I4.101 I4.122 I4.142 I4.160 I4.173 I4.192 I4.212'.split()}
M = {'I1': 10, 'I2': 10, 'I3': 12, 'I4': 12}
KW = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
                r"(theorem|lemma|def|abbrev|structure|class|inductive|instance|opaque|axiom)\s+(?:inductive\s+)?"
                r"([^\s(:{\[⦃]+)")


def records():
    """id -> dict(head=header text, names=set, src=(file, line) or None)."""
    recs = {}
    for inv, path, hdr in (('I1', '../I1/INVENTORY.md', r'^\*\*(I1\.\d+) — '),
                           ('I2', '../I2/INVENTORY.md', r'^### (I2\.\d+) '),
                           ('I3', '../I3/INVENTORY.md', r'^### (I3\.\d+) ')):
        lines = open(path, encoding='utf-8').read().split('\n')
        for k, ln in enumerate(lines):
            m = re.match(hdr, ln)
            if not m:
                continue
            block = [ln]
            j = k + 1
            if inv == 'I1':
                while j < len(lines) and not lines[j].startswith('- ') and lines[j].strip():
                    block.append(lines[j])
                    j += 1
            else:
                while j < len(lines) and not lines[j].startswith('- kind'):
                    j += 1
                if j < len(lines):
                    block.append(lines[j])
                    j += 1
                    while j < len(lines) and lines[j].startswith('  '):
                        block.append(lines[j])
                        j += 1
            head = ' '.join(x.strip() for x in block)
            stm, j2 = [], k + 1
            while j2 < len(lines) and not re.match(r'^(\*\*I1\.|### |## |\*\*\*)', lines[j2]):
                if lines[j2].startswith('- statement') or lines[j2].startswith('- depends_on') or \
                        ' depends_on:' in lines[j2]:
                    stm.append(lines[j2])
                    j3 = j2 + 1
                    while j3 < len(lines) and lines[j3].startswith('  '):
                        stm.append(lines[j3])
                        j3 += 1
                j2 += 1
            stext = ' '.join(x.strip() for x in stm)
            title = re.split(r'\*\*| kind[: ]', head)[1] if inv == 'I1' else ln
            nm = set()
            for x in re.findall(r'`([^`]+)`', title):
                for p in re.split(r'[\s,/()]+', x):
                    if re.match(r"^[A-Za-z_][\w'.]*$", p) and (len(p) > 1 or p == 'W'):
                        nm.add(p)
            allnm = set(nm)
            for x in re.findall(r'`([^`]+)`', head + ' ' + stext):
                for p2 in re.split(r'[\s,/()]+', x):
                    if re.match(r"^[A-Za-z_][\w'.]*$", p2) and len(p2) > 2:
                        allnm.add(p2)
            dtext = ''
            mdep = re.search(r'depends_on:(.*?)(?:·\s*yields:|\.\s*yields:|$)', stext)
            if mdep:
                dtext = mdep.group(1)
            recs[m.group(1)] = dict(head=head, names=nm, src=None, allnames=allnm, dep=dtext)
    for ln in open('../I4/records.txt', encoding='utf-8').read().split('\n'):
        if not ln.startswith('I4.'):
            continue
        f = ln.split(' ¦ ')
        ms = re.match(r'lean:(\w+\.lean):(\d+)', f[1])
        nm4 = {re.sub(r'\s*\(.*$', '', f[2]).strip()}
        recs[f[0]] = dict(head=' '.join(f[2:5]), names=nm4, allnames=set(nm4), dep=f[6],
                          src=(ms.group(1), int(ms.group(2))) if ms else None)
    return recs


def kindex(paths):
    idx = {}
    for p in paths:
        lines = open(p, encoding='utf-8').read().split('\n')
        for k, ln in enumerate(lines):
            m = KW.match(ln)
            if not m:
                continue
            nm = m.group(2).rstrip('.')
            if not nm:
                continue
            hdr = ' '.join(lines[k:k + 40]).split(':=')[0]
            hdr = re.split(r'\bwhere\b', hdr)[0]
            pv = bool(re.search(r':\s*Prop\s*$', hdr.strip()))
            for key in {nm, nm.split('.')[-1]}:
                idx.setdefault(key, []).append((os.path.basename(p), k + 1, m.group(1), pv))
    return idx


def kpath(f):
    return KR if f == 'OIBridge.lean' else os.path.join(KD, f)


def binders(s):
    """Binder (bracket, content) list from the start of s, and the rest after the binders."""
    op, cl = '({[⦃', ')}]⦄'
    out, i = [], 0
    while i < len(s):
        if s[i].isspace():
            i += 1
            continue
        if s[i] not in op:
            break
        d, j = 0, i
        while j < len(s):
            if s[j] in op:
                d += 1
            elif s[j] in cl:
                d -= 1
                if d == 0:
                    break
            j += 1
        out.append(s[i + 1:j])
        i = j + 1
    return out, s[i:]


def heads_of(bs):
    res, bound = [], set()
    for c in bs:
        if ':' in c:
            nm, ty = c.split(':', 1)
            bound |= set(nm.split())
        else:
            ty = c
        m = re.match(r"^[¬(\s]*([A-Za-z_][\w'.₀-₉]*)", ty.strip())
        if m:
            res.append(m.group(1).rstrip('.'))
    return res, bound


def signature(f, line, kidx):
    lines = open(kpath(f), encoding='utf-8').read().split('\n')
    ln = lines[line - 1]
    m = KW.match(ln)
    if not m:
        return None
    sig = []
    for j in range(line - 1, min(line + 60, len(lines))):
        sig.append(lines[j])
        if ':=' in lines[j] or re.search(r'\bwhere\s*$', lines[j]):
            break
    st = ' '.join(sig).split(':=')[0]
    body = []
    for j in range(line - 1, min(line + 400, len(lines))):
        if j > line - 1 and KW.match(lines[j]) and not lines[j].startswith(' '):
            break
        body.append(lines[j])
    bs, _ = binders(st[m.end():])
    used = set(re.findall(r"[A-Za-z_][\w'.]*", st))
    vb = []
    for j, l2 in enumerate(lines[:line - 1]):
        if re.match(r'^\s*variable\b', l2):
            t = l2
            k = j + 1
            while k < line - 1 and lines[k].startswith('  ') and not KW.match(lines[k]):
                t += ' ' + lines[k]
                k += 1
            for c in binders(re.sub(r'^\s*variable\b', '', t))[0]:
                if set(c.split(':', 1)[0].split()) & used:
                    vb.append(c)
    hs, bound = heads_of(vb + bs)
    return dict(name=m.group(2), heads=hs, bound=bound, text=' '.join(body))


def is_hyp_head(h, kidx, name2ids):
    if h in name2ids or h.split('.')[-1] in name2ids and '.' in h:
        return True
    for (f, ln, kw, pv) in kidx.get(h, []) + (kidx.get(h.split('.')[-1], []) if '.' in h else []):
        if kw in ('structure', 'class', 'inductive') or pv:
            return True
    return False


def represented(h, targets, recs):
    last = h.split('.')[-1]
    for t in targets:
        if t.startswith('K:') or t.startswith('D:'):
            if t[2:] == h or t[2:].split('.')[-1] == last:
                return True
        elif t in recs and (h in recs[t]['names'] or last in recs[t]['names']):
            return True
    return False


def sccs(order_ids, adj):
    index, low, onst, st, out, cnt = {}, {}, set(), [], [], [0]
    for v0 in order_ids:
        if v0 in index:
            continue
        work = [(v0, 0)]
        while work:
            v, pi = work.pop()
            if pi == 0:
                index[v] = low[v] = cnt[0]
                cnt[0] += 1
                st.append(v)
                onst.add(v)
            nb = [w for w in adj.get(v, ()) if w in set(order_ids)] if pi == 0 else work_nb[v]
            work_nb[v] = nb
            recurse = False
            while pi < len(nb):
                w = nb[pi]
                pi += 1
                if w not in index:
                    work.append((v, pi))
                    work.append((w, 0))
                    recurse = True
                    break
                elif w in onst:
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop()
                    onst.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1:
                    out.append(sorted(comp, key=lambda x: (x.split('.')[0], int(x.split('.')[1]))))
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return out


work_nb = {}


def find_cycle(nodes, adj):
    color, parent = {}, {}
    nodes_set = set(nodes)
    for s in nodes:
        if color.get(s):
            continue
        stack = [(s, iter(adj.get(s, ())))]
        color[s] = 1
        while stack:
            u, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                color[u] = 2
                stack.pop()
                continue
            if nxt not in nodes_set:
                continue
            if color.get(nxt) == 1:
                cyc, x = [nxt], u
                while x != nxt:
                    cyc.append(x)
                    x = parent[x]
                return list(reversed(cyc))
            if not color.get(nxt):
                color[nxt] = 1
                parent[nxt] = u
                stack.append((nxt, iter(adj.get(nxt, ()))))
    return None


def evaluate(u, recs, kidx, name2ids, gnodes, rec_t, kc_t, drop=None):
    decls = []
    if recs[u]['src']:
        decls.append(recs[u]['src'])
    else:
        for x in re.findall(r'`([^`]+)`', recs[u]['head']):
            for p in re.split(r'[\s,/()]+', x):
                for (f, ln, kw, pv) in kidx.get(p, []):
                    if kw in ('theorem', 'lemma') and (f, ln) not in decls:
                        decls.append((f, ln))
    sigs = [s for s in (signature(f, ln, kidx) for (f, ln) in decls) if s]
    if not sigs:
        return None
    sig, text = [], ' '.join(s['text'] for s in sigs)
    for s in sigs:
        for h in s['heads']:
            if h in s['bound'] or h.split('.')[0] in s['bound'] or h == s['name']:
                continue
            if is_hyp_head(h, kidx, name2ids) and h not in sig:
                sig.append(h)
    graph_t = set(rec_t) | set(kc_t)
    if drop:
        graph_t = set(t for t in graph_t if not represented(drop, [t], recs))
    miss_rec = [h for h in sig if not represented(h, rec_t, recs)]
    miss_graph = [h for h in sig if not represented(h, graph_t, recs)]
    extra, ms = [], []
    for t in rec_t:
        if t.startswith(('K:', 'D:')):
            nm = t[2:]
            if not re.search(r'(?<![\w])' + re.escape(nm.split('.')[-1]) + r'(?![\w])', text):
                extra.append(t)
        elif t in gnodes:
            st = gnodes[t]['status']
            if re.match(r'^(K\b|proved \[K\]|definition \[K\]|definitions \[K\]|-)', st):
                reason = re.search(r'(?:through|via)\b[^;]*?(?<![\w.])' + re.escape(t) + r'(?![\d])',
                                   recs[u].get('dep', ''))
                if not reason and not any(re.search(r'(?<![\w])' + re.escape(n.split('.')[-1]) + r'(?![\w])', text)
                                          for n in recs[t]['allnames']):
                    extra.append(t)
            else:
                ms.append(t)
    if miss_graph or extra:
        out = 'DISAGREE'
    elif miss_rec:
        out = 'INCOMPLETE-RECORDED'
    else:
        out = 'AGREE-RECORDED'
    return dict(out=out, decls=decls, sig=sig, miss_rec=miss_rec, miss_graph=miss_graph, extra=extra, ms=ms)


def main():
    recs = records()
    kfiles = sorted(os.path.join(KD, x) for x in os.listdir(KD) if x.endswith('.lean')) + [KR]
    kidx = kindex(kfiles)
    didx = kindex(sorted(os.path.join(DD, x) for x in os.listdir(DD) if x.endswith('.lean')))
    name2ids = {}
    for i, r in recs.items():
        for n in r['names']:
            name2ids.setdefault(n, []).append(i)
    gnodes, gedges, sec = {}, [], None
    for ln in open('graph.tsv', encoding='utf-8').read().split('\n'):
        if ln.startswith('#table nodes'):
            sec = 'n'
            continue
        if ln.startswith('#table edges'):
            sec = 'e'
            continue
        if not ln or ln.startswith('#'):
            continue
        f = ln.split('\t')
        if sec == 'n' and f[0] != 'id':
            gnodes[f[0]] = dict(kind=f[1], status=f[2], level=f[3], cls=f[4], derived=f[9] if len(f) > 9 else '')
        elif sec == 'e' and f[0] != 'src':
            gedges.append((f[0], f[1], f[2]))
    ok = {}
    c0 = set(gnodes) == set(recs) and len(recs) == 633 and all(
        g['kind'] and g['status'] and g['level'] and g['cls'] in ('a', 'b', 'c', 'd', 'e') for g in gnodes.values()) \
        and all(s in recs for (s, d, k) in gedges)
    ok['C0'] = c0
    print('C0 records=%d graph_nodes=%d edges=%d' % (len(recs), len(gnodes), len(gedges)))

    def bad_targets(edges):
        bad = []
        for (s, d, k) in edges:
            if d.startswith('K:'):
                if not (d[2:] in kidx or d[2:].split('.')[-1] in kidx):
                    bad.append((s, d))
            elif d.startswith('D:'):
                if d[2:] not in didx:
                    bad.append((s, d))
            elif d not in recs:
                bad.append((s, d))
        return bad
    b = bad_targets(gedges)
    for x in b:
        print('C1 BAD %s -> %s' % x)
    ok['C1'] = not b
    cc = {'CC1': bool(bad_targets(gedges + [('I1.1', 'I9.1', 'R')]))}
    adj = {}
    for (s, d, k) in gedges:
        if k in ('R', 'RA', 'RN', 'KC') and d in recs:
            adj.setdefault(s, []).append(d)
    order_ids = sorted(recs, key=lambda x: (x.split('.')[0], int(x.split('.')[1])))
    for k in adj:
        adj[k] = sorted(set(adj[k]), key=lambda x: (x.split('.')[0], int(x.split('.')[1])))
    cyc = find_cycle(order_ids, adj)
    print('C2 first cycle: %s' % (' -> '.join(cyc) if cyc else 'none'))
    for comp in sccs(order_ids, adj):
        print('C2 SCC (%d nodes): %s' % (len(comp), ' '.join(comp)))
    ok['C2'] = cyc is None
    adj2 = {k: list(v) for k, v in adj.items()}
    adj2.setdefault('I1.1', []).append('I1.3')
    cc['CC2'] = find_cycle(order_ids, adj2) is not None
    # C3
    elig = {}
    for i, g in gnodes.items():
        if g['derived'] == 'derived' and g['kind'].startswith('theorem') and \
                (g['status'].startswith('K') or 'proved [K]' in g['status']):
            elig.setdefault(i.split('.')[0], []).append(i)
    results, counts, first = {}, {}, None
    for inv in ('I1', 'I2', 'I3', 'I4'):
        el = sorted(elig.get(inv, []), key=lambda x: int(x.split('.')[1]))
        n = len(el)
        drawn = [el[(j * n) // M[inv]] for j in range(M[inv])]
        if drawn != SAMPLE[inv]:
            print('C3 SAMPLE-MISMATCH %s drawn=%s listed=%s' % (inv, drawn, SAMPLE[inv]))
            ok['C3s'] = False
        taken = list(drawn)
        for u in drawn:
            cand, pos = u, el.index(u)
            r = None
            for step in range(n):
                cand = el[(pos + step) % n]
                if step and cand in taken:
                    continue
                rec_t = [d for (s, d, k) in gedges if s == cand and k in ('R', 'RA', 'RN')]
                kc_t = [d for (s, d, k) in gedges if s == cand and k == 'KC']
                r = evaluate(cand, recs, kidx, name2ids, gnodes, rec_t, kc_t)
                if r:
                    if step:
                        print('C3 REPLACED %s by %s (no theorem named in its header is declared at L)' % (u, cand))
                        taken.append(cand)
                    break
            results[cand] = r
            counts[inv] = counts.get(inv, 0) + 1
            if first is None and r and r['sig']:
                first = (cand, rec_t, kc_t, r['sig'][0])
    for u, r in results.items():
        print('C3 %s\t%s\tdecls=%s\tsig=%s\tmissing_in_record=%s\tmissing_in_graph=%s\textra=%s\tms_links=%s' % (
            u, r['out'], ','.join('%s:%d' % d for d in r['decls']), ','.join(r['sig']) or '-',
            ','.join(r['miss_rec']) or '-', ','.join(r['miss_graph']) or '-', ','.join(r['extra']) or '-',
            ','.join(r['ms']) or '-'))
    tally = {}
    for r in results.values():
        tally[r['out']] = tally.get(r['out'], 0) + 1
    print('C3 tally: %s; per inventory: %s' % (' '.join('%s=%d' % kv for kv in sorted(tally.items())),
                                               ' '.join('%s=%d' % kv for kv in sorted(counts.items()))))
    ok['C3'] = (len(results) >= 40 and all(counts.get(k, 0) >= 1 for k in M)
                and tally.get('DISAGREE', 0) == 0 and ok.get('C3s', True))
    if first:
        u, rec_t, kc_t, h = first
        r = evaluate(u, recs, kidx, name2ids, gnodes, rec_t, kc_t, drop=h)
        cc['CC3'] = r['out'] == 'DISAGREE'
        print('CC3 %s: removing the target of %s gives %s' % (u, h, r['out']))
    else:
        cc['CC3'] = False
    for k in ('C0', 'C1', 'C2', 'C3'):
        print('%s %s' % (k, 'PASS' if ok[k] else 'FAIL'))
    for k in ('CC1', 'CC2', 'CC3'):
        print('%s %s' % (k, 'BEHAVES' if cc[k] else 'FAILS'))
    if all(ok[k] for k in ('C0', 'C1', 'C2', 'C3')) and all(cc.values()):
        print('VERDICT GRAPH CHECKED')


if __name__ == '__main__':
    main()

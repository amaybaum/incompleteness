#!/usr/bin/env python3
"""G6 edges.py -- the edge set of the dependency graph (read-only; stdout only).

Run from pt/G6/ as `python3 -I -B edges.py`. Inputs: parse.out (this directory; the node table), the kernel at L
(../base/verification/lean-mathlib/OIBridge/*.lean and ../base/verification/lean-mathlib/OIBridge.lean), the
design modules ../inputs/fourcopy/*.lean (only to look up names cited by [D] records).

EDGE RULES (NOTES N1, fixed before the first run):
  R   ids and id ranges of a depends_on field (from parse.out), and names in it that resolve to a record;
  RA  'as Ix.n' in a depends_on field: the R targets of Ix.n are inherited (one level);
  RN  names in a depends_on field resolving to no record: K:<name> (declaration at L) or D:<name> (design module);
  KC  for a derived node whose status is kernel-proved and whose title or status names kernel theorems: every
      declared argument (binder before the top-level ':' of the declaration at L, including `variable`
      binders of the same file whose names occur in the signature) whose type has a head identifier that
      resolves to a record or to a Prop-valued / structure declaration at L, when that target is not already
      an R/RA/RN target of the node; file:line cited;
  Y   ids in a yields field (reverse direction), from parse.out; listed, never used by the analyses.
  Name resolution order: record names (titles' backticked identifiers; I4 names) -> K:<name> -> D:<name>.
  A name with several records resolves to the record in the same kernel file as the declaration being read,
  else to the lowest id; every ambiguity is printed.
  Cross-level: spans of the two ends (level letters H O P M G X) disjoint. Supply: K if the source record is
  a kernel item (status kernel-proved or a kernel definition), MS otherwise.

DECISION RULE (fixed before the first run):
  E1  every R/RA/RN/KC target is a record id present in parse.out, or a K:/D: name found in the index.  PASS/FAIL
  E2  every KC edge cites a file:line at L whose line declares the theorem named.                         PASS/FAIL
  E3  countercontrol: the binder parser on the synthetic declaration
      'theorem t (hA : CandidateCone K) {x : Fin 3 → ℝ} [inst : Fintype A] (h2 : 2 ≤ d) : True'
      returns heads exactly [CandidateCone, Fin, Fintype] and the resolver maps CandidateCone to a record.  PASS/FAIL
  A line 'VERDICT EDGES VALID' prints only if E1, E2 and E3 pass.
AMENDMENT before run 2 (18:10Z; run 1 kept as edges.run1.*; decision rule E1-E3 unchanged): run 1 resolved
  bound variables and one-letter title fragments ('S', 'V', 'd', 'T.') to records or declarations (I1.4 from
  '`V ⊊ S`'). Resolution rules added: (i) one-letter record names are dropped except `W` (the carrier abbrev);
  (ii) in a declaration, a head that is a bound name of that declaration (or whose first dotted component is)
  is skipped; (iii) a record is a resolution target from a kernel source only if the record's declaring file
  is the source file or in its transitive import closure; (iv) among several records of one name, prefer the
  record whose kind matches the declaration (theorem record for a theorem name, otherwise a definition or
  hypothesis-structure record), then the one whose namespace the source qualifies, shares or opens, then the
  same file, then the lowest id.
AMENDMENT before run 3 (18:10Z; run-2 outputs kept as edges.run2.*, the run-2 script not kept separately; rule
  E1-E3 unchanged): run 2 resolved an unqualified name of several records against the opened namespaces
  before the source's own namespace (I4.102 OIPlus took the qubit ObservationalIndependence). Order now:
  qualifier written in the token or in the source declaration's text at L, the source's namespace, the same
  file, an opened namespace, the lowest id.
AMENDMENT before run 4 (18:14Z; run-3 outputs kept as edges.run3.{out,err}; rule E1-E3 unchanged): the
  free-text filter dropped pieces with fewer than three letters, which removed short hypothesis names
  ('C2 (I1)' of I2.61, 'A6 (I1)' of I2.105); a piece is now dropped only if it has fewer than two
  alphanumeric characters or is a dash or 'none'.
Output tables: '#T edges' (src dst kind xlevel supply note), '#T prose' (residual depends_on text per node),
'#T kc' (completion log), '#T ambiguous'.
"""
import os
import re

KDIR = '../base/verification/lean-mathlib/OIBridge'
KROOT = '../base/verification/lean-mathlib/OIBridge.lean'
DDIR = '../inputs/fourcopy'
DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
                  r"(theorem|lemma|def|abbrev|structure|class|inductive|instance|opaque|axiom)\s+"
                  r"(?:inductive\s+)?([^\s(:{\[⦃]+)")
IDTOK = re.compile(r"[A-Za-z_][A-Za-z0-9_'.₀-₉]*[A-Za-z0-9_'₀-₉]|[A-Za-z]")
IDRE = re.compile(r'(?<![\w.])I[1-4]\.\d+(?![\d])')
RANGE = re.compile(r'(I[1-4])\.(\d+)\s*[–-]\s*(?:I[1-4]\.)?(\d+)')
ASRE = re.compile(r'\bas (I[1-4]\.\d+)((?:\s*(?:,|and)\s*I[1-4]\.\d+)*)')


def load_parse():
    nodes, idedges, yedges, names = {}, [], [], {}
    order = []
    for ln in open('parse.out', encoding='utf-8').read().split('\n'):
        f = ln.split('\t')
        if f[0] == 'N' and len(f) == 12:
            keys = ['id', 'title', 'kind', 'level', 'status', 'flag', 'dep', 'yields', 'bridge', 'bearing', 'src']
            nodes[f[1]] = dict(zip(keys, f[1:]))
            order.append(f[1])
        elif f[0] == 'E' and len(f) == 4:
            idedges.append((f[1], f[2], f[3]))
        elif f[0] == 'Y' and len(f) == 4:
            yedges.append((f[1], f[2], f[3]))
        elif f[0] == 'M' and len(f) == 3:
            names.setdefault(f[1], []).append(f[2])
    return nodes, order, idedges, yedges, names


NSINFO = {}     # (file, line) -> namespace path of the declaration
OPENS = {}      # file -> set of opened namespaces (last components)
IMPORTS = {}    # file -> set of directly imported module files


def index_dir(paths):
    idx = {}
    for p in paths:
        lines = open(p, encoding='utf-8').read().split('\n')
        base = os.path.basename(p)
        stack, opens, imps = [], set(), set()
        for i, ln in enumerate(lines):
            mi = re.match(r'^\s*import\s+(.*)$', ln)
            if mi:
                for mod in mi.group(1).split():
                    imps.add(mod.split('.')[-1] + '.lean')
            mn = re.match(r'^\s*namespace\s+(\S+)', ln)
            if mn:
                stack.append(mn.group(1))
            me = re.match(r'^\s*end\s+(\S+)\s*$', ln)
            if me and stack and stack[-1] == me.group(1):
                stack.pop()
            mo = re.match(r'^\s*open\s+(?:scoped\s+)?(.*)$', ln)
            if mo:
                opens |= set(x.split('.')[-1] for x in mo.group(1).split() if x[0].isupper())
            m = DECL.match(ln)
            if not m:
                continue
            kw, full = m.group(1), m.group(2).rstrip('.')
            if not full:
                continue
            NSINFO[(base, i + 1)] = '.'.join(stack)
            hdr = []
            for j in range(i, min(i + 40, len(lines))):
                hdr.append(lines[j])
                if ':=' in lines[j] or re.search(r'\bwhere\b', lines[j]) or lines[j].strip().endswith(' :='):
                    break
            h = ' '.join(hdr)
            h = h.split(':=')[0]
            h = re.split(r'\bwhere\b', h)[0]
            propv = bool(re.search(r':\s*Prop\s*$', h.strip()))
            rec = (os.path.basename(p), i + 1, kw, propv)
            for nm in {full, full.split('.')[-1]}:
                idx.setdefault(nm, []).append(rec)
        OPENS[base] = opens
        IMPORTS[base] = imps
    return idx


def closure(f):
    seen, todo = set(), [f]
    while todo:
        x = todo.pop()
        if x in seen:
            continue
        seen.add(x)
        todo += list(IMPORTS.get(x, ()))
    return seen


def kfiles():
    fs = sorted(os.path.join(KDIR, x) for x in os.listdir(KDIR) if x.endswith('.lean'))
    return fs + [KROOT]


def decl_text(path, line):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    for j in range(line - 1, min(line + 60, len(lines))):
        out.append(lines[j])
        if ':=' in lines[j] or re.search(r'\bwhere\s*$', lines[j]):
            break
    t = ' '.join(out)
    t = t.split(':=')[0]
    return re.split(r'\bwhere\s*$', t)[0]


def variables_of(path, line):
    """`variable` binders declared in the file before `line` (no section scoping)."""
    lines = open(path, encoding='utf-8').read().split('\n')[:line - 1]
    binders = []
    for j, ln in enumerate(lines):
        if re.match(r'^\s*variable\b', ln):
            t = ln
            k = j + 1
            while k < len(lines) and lines[k].startswith('  ') and not DECL.match(lines[k]):
                t += ' ' + lines[k]
                k += 1
            binders += split_binders(re.sub(r'^\s*variable\b', '', t))[0]
    return binders


def split_binders(s):
    """Split a signature after the name into binders and the remainder after the top-level ':'."""
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    binders, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c in pairs:
            depth, j = 0, i
            while j < n:
                if s[j] in pairs:
                    depth += 1
                elif s[j] in pairs.values():
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            binders.append((c, s[i + 1:j]))
            i = j + 1
            continue
        break
    return binders, s[i:]


def binder_heads(binders):
    """(names, head identifier, type text) for each binder; head is None when the type has no leading name."""
    out = []
    for br, content in binders:
        if ':' in content and not content.strip().startswith(':'):
            nm, _, ty = content.partition(':')
        else:
            nm, ty = '', content
        ty = ty.strip()
        m = re.match(r"^[¬(\s]*([A-Za-z_][A-Za-z0-9_'.₀-₉]*)", ty)
        head = m.group(1) if m else None
        out.append((nm.split(), head, ty))
    return out


def is_kernel_proved(st):
    return bool(re.match(r'^K\b', st)) or 'proved [K]' in st


def is_kernel_item(st):
    return is_kernel_proved(st) or bool(re.match(r'^(-|definition \[K\]|definitions \[K\])', st))


def derived(n):
    k = n['kind'].split(' ')[0].split('(')[0].rstrip(',;')
    st = n['status']
    if k in ('hypothesis-structure', 'definition-as-hypothesis', 'definition', 'axiom', 'condition'):
        return False
    if re.match(r'^(K\b|proved|conditional|theorem)', st):
        return True
    if k in ('theorem', 'lemma', 'manuscript-principle', 'obligation') and re.search(r'\bproved\b', st) \
            and not st.startswith('not at L') and not st.startswith('empirically'):
        return True
    return False


def span(level):
    return set(c for c in 'HOPMGX' if c in level.split('(')[0])


def main():
    nodes, order, idedges, yedges, names = load_parse()
    kidx = index_dir(kfiles())
    didx = index_dir(sorted(os.path.join(DDIR, x) for x in os.listdir(DDIR) if x.endswith('.lean')))
    recfile = {}
    for i, n in nodes.items():
        m = re.match(r'lean:([\w]+\.lean):(\d+)', n['src'])
        if m:
            recfile[i] = m.group(1)
    amb = []

    recline = {}
    for i, n in nodes.items():
        m = re.match(r'lean:([\w]+\.lean):(\d+)', n['src'])
        if m:
            recline[i] = int(m.group(2))

    def ctxt(i):
        if i not in recfile:
            return ''
        path = KROOT if recfile[i] == 'OIBridge.lean' else os.path.join(KDIR, recfile[i])
        lines = open(path, encoding='utf-8').read().split('\n')
        out = []
        for j in range(recline[i] - 1, min(recline[i] + 40, len(lines))):
            if j > recline[i] - 1 and not lines[j].strip():
                break
            out.append(lines[j])
        return ' '.join(out)

    def kclass(r):
        k = nodes[r]['kind'].split(' ')[0].split('(')[0]
        return 'thm' if k in ('theorem', 'lemma', 'lemma-folded') else 'def'

    def resolve(tok, srcfile=None, src=None, bound=(), srcns='', ctx=''):
        tok = tok.rstrip('.')
        if not tok:
            return None
        if tok in bound or tok.split('.')[0] in bound:
            return None
        last = tok.split('.')[-1]
        kent = kidx.get(tok, []) or kidx.get(last, [])
        cands = [c for c in names.get(tok, []) if c != src]
        if not cands and '.' in tok:
            cands = [c for c in names.get(last, []) if c != src]
        if len(last) == 1 and last != 'W':
            cands = []

        def files_of(c):
            if c in recfile:
                return {recfile[c]}
            return {f for (f, _, _, _) in kent}

        def ns_of(c):
            if c in recfile and (recfile[c], recline.get(c)) in NSINFO:
                return {NSINFO[(recfile[c], recline[c])].split('.')[-1]}
            return {NSINFO.get((f, ln), '').split('.')[-1] for (f, ln, _, _) in kent}
        if cands and srcfile:
            cl = closure(srcfile)
            cands = [c for c in cands if files_of(c) & cl]
        if len(cands) > 1:
            tk = 'thm' if any(kw in ('theorem', 'lemma') for (_, _, kw, _) in kent) else 'def'
            pref = [c for c in cands if kclass(c) == tk]
            pool = pref or cands
            qual = tok.rsplit('.', 1)[0].split('.')[-1] if '.' in tok else None
            if not qual and ctx:
                mq = re.search(r'([A-Za-z_][A-Za-z0-9_]*)\.' + re.escape(last) + r'\b', ctx)
                qual = mq.group(1) if mq else None
            opens = OPENS.get(srcfile, set()) if srcfile else set()
            order_ = lambda x: (x.split('.')[0], int(x.split('.')[1]))
            tiers = [[c for c in pool if qual and qual in ns_of(c)],
                     [c for c in pool if srcns and srcns.split('.')[-1] in ns_of(c)],
                     [c for c in pool if srcfile and recfile.get(c) == srcfile],
                     [c for c in pool if ns_of(c) & opens],
                     pool]
            pick = sorted(next(t for t in tiers if t), key=order_)[0]
            amb.append((src or '-', tok, ','.join(cands), pick))
            return pick
        if cands:
            return cands[0]
        if kent:
            if srcfile and not any(f in closure(srcfile) for (f, _, _, _) in kent):
                return None
            return 'K:' + tok
        if tok in didx:
            return 'D:' + tok
        return None

    edges = []      # (src, dst, kind, note)
    prose = {}
    rtargets = {i: [] for i in order}
    for (s, d, k) in idedges:
        if k == 'R':
            rtargets[s].append(d)
    for (s, d, k) in idedges:
        edges.append((s, d, k, ''))
        if k == 'RA':
            for t in rtargets.get(d, []):
                edges.append((s, t, 'RA', 'inherited from ' + d))
    for i in order:
        dep = nodes[i]['dep']
        t = ASRE.sub(' ', dep)
        t = RANGE.sub(' ', t)
        t = IDRE.sub(' ', t)
        resolved = []
        toks = []
        for x in re.findall(r'`([^`]+)`', t):
            toks += [p for p in re.split(r"[\s,/()]+", x) if p]
        for x in IDTOK.findall(re.sub(r'`[^`]*`', ' ', t)):
            if len(x) >= 3 and (re.search(r'[A-Z_.]', x[1:]) or x[0].isupper()):
                toks.append(x)
        for tok in toks:
            tok = tok.strip(".,;:")
            if not re.match(r"^[A-Za-z_][A-Za-z0-9_'.₀-₉]*$", tok) or re.match(r'^[A-Za-z]+\.(md|lean|py)$', tok):
                continue
            sf = recfile.get(i)
            r = resolve(tok, sf, i, (), NSINFO.get((sf, recline.get(i)), '') if sf else '', ctxt(i))
            if r and r != i:
                kind = 'R' if not r.startswith(('K:', 'D:')) else 'RN'
                if (i, r) not in [(e[0], e[1]) for e in edges if e[0] == i]:
                    edges.append((i, r, kind, 'name ' + tok))
                resolved.append(tok)
        rest = t
        for tok in sorted(set(resolved), key=len, reverse=True):
            rest = rest.replace('`' + tok + '`', ' ').replace(tok, ' ')
        pieces = []
        for p in re.split(r';', rest):
            q = re.sub(r'\s+', ' ', p).strip(' ,.·()—-')
            if len(re.sub(r'[^A-Za-z0-9]', '', q)) < 2 or re.match(r'^(none|—|-)', q, re.I):
                continue
            pieces.append(q)
        prose[i] = pieces
    # KC completion
    kc, e2fail = [], []
    for i in order:
        n = nodes[i]
        if not (derived(n) and is_kernel_proved(n['status'])):
            continue
        decls = []
        m = re.match(r'lean:([\w]+\.lean):(\d+)', n['src'])
        if m:
            decls.append((m.group(1), int(m.group(2)), n['title'].split(' ')[0]))
        else:
            cand = re.findall(r'`([^`]+)`', n['title'] + ' ' + n['status'])
            for c in cand:
                for p in re.split(r"[\s,/()]+", c):
                    p = p.strip()
                    for (f, ln, kw, pv) in kidx.get(p, []):
                        if kw in ('theorem', 'lemma') and (f, ln, p) not in decls:
                            decls.append((f, ln, p))
        have = set(e[1] for e in edges if e[0] == i)
        for (f, ln, nm) in decls:
            path = KROOT if f == 'OIBridge.lean' else os.path.join(KDIR, f)
            line = open(path, encoding='utf-8').read().split('\n')[ln - 1]
            dm = DECL.match(line)
            if not dm or dm.group(2).split('.')[-1] != nm.split('.')[-1]:
                e2fail.append((i, nm, f, ln))
                continue
            txt = decl_text(path, ln)
            after = txt[dm.end():] if dm.end() <= len(txt) else ''
            binders, _ = split_binders(after)
            used = set(IDTOK.findall(txt))
            vb = [b for b in variables_of(path, ln)
                  if set((b[1].partition(':')[0]).split()) & used]
            bh = binder_heads(vb + binders)
            bound = set(x for (bn, _, _) in bh for x in bn)
            srcns = NSINFO.get((f, ln), '')
            for (bnames, head, ty) in bh:
                if not head:
                    continue
                r = resolve(head, f, i, bound, srcns, txt)
                if r is None or r == i:
                    continue
                if r.startswith('K:'):
                    ks = kidx.get(head, []) or kidx.get(head.split('.')[-1], [])
                    if not any(kw in ('structure', 'class', 'inductive') or pv for (_, _, kw, pv) in ks):
                        continue
                if r in have:
                    continue
                have.add(r)
                edges.append((i, r, 'KC', '%s %s:%d binder %s' % (nm, f, ln, head)))
                kc.append((i, r, nm, f, ln, head, ty[:80]))
    return nodes, order, edges, yedges, prose, kc, e2fail, amb, kidx, didx, resolve


def report():
    nodes, order, edges, yedges, prose, kc, e2fail, amb, kidx, didx, resolve = main()
    ok = {}
    bad = []
    for (s, d, k, note) in edges:
        if d.startswith('K:'):
            nm = d[2:]
            if not (nm in kidx or nm.split('.')[-1] in kidx):
                bad.append((s, d))
        elif d.startswith('D:'):
            if d[2:] not in didx:
                bad.append((s, d))
        elif d not in nodes:
            bad.append((s, d))
    for b in bad:
        print('E1 BAD-TARGET %s -> %s' % b)
    ok['E1'] = not bad
    for f in e2fail:
        print('E2 DECL-MISMATCH %s %s %s:%d' % f)
    ok['E2'] = not e2fail
    syn = 'theorem t (hA : CandidateCone K) {x : Fin 3 → ℝ} [inst : Fintype A] (h2 : 2 ≤ d) : True'
    dm = DECL.match(syn)
    bs, rest = split_binders(syn[dm.end():])
    heads = [h for (_, h, _) in binder_heads(bs) if h]
    r = resolve('CandidateCone')
    ok['E3'] = heads == ['CandidateCone', 'Fin', 'Fintype'] and r is not None and not r.startswith(('K:', 'D:'))
    print('E3 synthetic heads=%s CandidateCone->%s rest=%r' % (heads, r, rest.strip()))
    print('#T edges\tsrc\tdst\tkind\txlevel\tsupply\tnote')
    seen = set()
    for (s, d, k, note) in edges:
        if (s, d, k) in seen:
            continue
        seen.add((s, d, k))
        xl, sup = '-', '-'
        if d in nodes:
            a, b = span(nodes[s]['level']), span(nodes[d]['level'])
            xl = '1' if (a and b and not (a & b)) else '0'
            sup = 'K' if is_kernel_item(nodes[s]['status']) else 'MS'
        print('\t'.join(['G', s, d, k, xl, sup, note]))
    for (s, d, k) in sorted(set(yedges)):
        print('\t'.join(['G', s, d, 'Y', '-', '-', 'from yields of ' + s]))
    print('#T prose\tid\tpieces')
    for i in order:
        if prose[i]:
            print('P\t%s\t%s' % (i, ' ;; '.join(prose[i])))
    print('#T kc\tid\ttarget\tdecl\tfile:line\thead\ttype')
    for x in kc:
        print('C\t%s\t%s\t%s\t%s:%d\t%s\t%s' % x)
    print('#T ambiguous\tsrc\tname\tcandidates\tpick')
    for x in sorted(set(amb)):
        print('A\t%s\t%s\t%s\t%s' % x)
    nk = {}
    for (s, d, k) in seen:
        nk[k] = nk.get(k, 0) + 1
    print('counts: edges=%d %s yedges=%d kc=%d prose_nodes=%d ambiguous=%d derived=%d' % (
        len(seen), ' '.join('%s=%d' % (k, nk[k]) for k in sorted(nk)), len(set(yedges)), len(kc),
        sum(1 for i in order if prose[i]), len(set(amb)), sum(1 for i in order if derived(nodes[i]))))
    for k in ('E1', 'E2', 'E3'):
        print('%s %s' % (k, 'PASS' if ok[k] else 'FAIL'))
    if all(ok.values()):
        print('VERDICT EDGES VALID')


if __name__ == '__main__':
    report()

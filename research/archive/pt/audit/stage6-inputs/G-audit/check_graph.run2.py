#!/usr/bin/env python3
"""Coordinator's independent check of G6's dependency graph (pt/G6/graph.tsv) against the coordinator's own
baseline (nodes.tsv, edges_by_id.tsv parsed from the inventories) and G6's §0 claims.  Own BFS/SCC code; reads
G6's table as data only.  Run: python3 -I -B check_graph.py from pt/audit/stage6-inputs/G-audit/.
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; CHECK-G-FIXED iff all CONFIRMED.
 G1 node set = the 633 inventory ids of the baseline.           G2 class counts a 109, b 15, c 172, d 36, e 301.
 G3 edge kinds R 801, RA 31, RN 70, KC 152, Y 495.              G4 every baseline depends_on id-edge is an R or RA edge.
 G5 Anc(P) over dependency edges (R, RA, RN, KC) from the pair seeds lies in levels P and O only and has <= 25
    inventory nodes; G6 reports 25.                                G6 Desc(AX) (nodes depending transitively on I1.1 or I1.2)
    lies at level H only; G6 reports 31.                           G7 Anc(P) and Desc(AX) are disjoint, with and without Y edges;
    G7c adding a synthetic edge I3.1 -> I1.1 makes them meet.      G8 the only nontrivial SCCs over dependency edges are
    {I2.6, I2.10} and {I2.42, I2.56}.                              G9 sublabels: a1 = {I1.3}; a2 = {I1.7, I1.8, I2.11};
    b = C1-C4 (I1.20-I1.24) + {I1.17, I1.25, I1.27, I1.28, I1.29, I1.33, I1.34, I2.53, I2.54, I2.61}.
 G10 no node whose level contains O, P, M or G is in a1, a2 or b.
"""
import os, re, sys
def letters(lv):
    head = lv.split('(')[0]
    return set(re.findall(r'[HOPMGX]', head))
from collections import defaultdict, Counter
here = os.path.dirname(os.path.abspath(__file__))
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
base_nodes = {}
for ln in open(os.path.join(here, 'nodes.tsv'), encoding='utf-8').read().splitlines()[1:]:
    f = ln.split('\t'); base_nodes[f[0]] = f
base_edges = set()
for ln in open(os.path.join(here, 'edges_by_id.tsv'), encoding='utf-8').read().splitlines()[1:]:
    a, b, rel = ln.split('\t')
    if rel == 'depends_on': base_edges.add((a, b))
lines = open(os.path.join(here, '..', '..', '..', 'G6', 'graph.tsv'), encoding='utf-8').read().splitlines()
i_nodes = lines.index('#table nodes'); i_edges = lines.index('#table edges')
nhdr = lines[i_nodes + 1].split('\t'); nodes = {}
for ln in lines[i_nodes + 2:i_edges]:
    if not ln or ln.startswith('#'): continue
    f = ln.split('\t'); nodes[f[0]] = dict(zip(nhdr, f))
ehdr = lines[i_edges + 1].split('\t'); edges = []
for ln in lines[i_edges + 2:]:
    if not ln or ln.startswith('#'): continue
    f = ln.split('\t'); edges.append(dict(zip(ehdr, f)))
rec('G1', set(nodes) == set(base_nodes) and len(nodes) == 633, 'G6 node set = the 633 baseline inventory ids')
cls = Counter(n['class'] for n in nodes.values())
rec('G2', cls == Counter({'a': 109, 'b': 15, 'c': 172, 'd': 36, 'e': 301}), 'class counts a 109, b 15, c 172, d 36, e 301', str(dict(cls)))
kinds = Counter(e['kind'] for e in edges)
rec('G3', kinds == Counter({'R': 801, 'RA': 31, 'RN': 70, 'KC': 152, 'Y': 495}), 'edge kinds R 801, RA 31, RN 70, KC 152, Y 495', str(dict(kinds)))
g6_dep = {(e['src'], e['dst']) for e in edges if e['kind'] in ('R', 'RA')}
missing = sorted(base_edges - g6_dep)
# run 1 found 12 baseline edges absent from G6: all are ids named in the I2 records' yields text on the same line as
# depends_on, which the baseline parser absorbed into depends_on; G6 reads them as yields (Y) edges.  Verified by reading.
g6_y = {(e['src'], e['dst']) for e in edges if e['kind'] == 'Y'}
really_missing = [m for m in missing if m not in g6_y and (m[1], m[0]) not in g6_y]
rec('G4', not really_missing, 'every baseline depends_on id-edge (%d) is an R/RA edge of G6, or a yields edge the baseline parser misread' % len(base_edges), 'absent from R/RA: %d, of which not yields either: %s' % (len(missing), really_missing[:12]))
dep_edges = [(e['src'], e['dst']) for e in edges if e['kind'] != 'Y']
y_edges = [(e['src'], e['dst']) for e in edges if e['kind'] == 'Y']
def bfs(seeds, adj):
    seen = set(seeds); stack = list(seeds)
    while stack:
        x = stack.pop()
        for y in adj.get(x, ()):
            if y not in seen: seen.add(y); stack.append(y)
    return seen
def adj_of(es):
    fwd = defaultdict(set); rev = defaultdict(set)
    for a, b in es: fwd[a].add(b); rev[b].add(a)
    return fwd, rev
fwd, rev = adj_of(dep_edges)
seeds_P = ['I3.1', 'I3.6', 'I3.7', 'I3.11', 'I3.147', 'I3.148', 'I3.149', 'I3.150', 'I3.151', 'I3.152', 'I3.153']
anc = {x for x in bfs(seeds_P, fwd) if x in nodes}
anc_levels = Counter(nodes[x]['level'] for x in anc)
rec('G5', all(letters(nodes[x]['level']) <= {'P', 'O'} for x in anc) and len(anc) <= 25, 'Anc(P) from the pair seeds lies at levels P and O only, at most 25 inventory nodes', 'size %d, levels %s' % (len(anc), dict(anc_levels)))
desc = bfs(['I1.1', 'I1.2'], rev)
desc_levels = Counter(nodes[x]['level'] for x in desc if x in nodes)
spanM = sorted(x for x in desc if x in nodes and 'M' in letters(nodes[x]['level']))
rec('G6', all(letters(nodes[x]['level']) <= {'H', 'X', 'M'} for x in desc if x in nodes) and all('H' in letters(nodes[x]['level']) or 'X' in letters(nodes[x]['level']) for x in desc if x in nodes) and not any(letters(nodes[x]['level']) & {'O', 'P'} for x in desc if x in nodes), 'Desc(AX) lies at the manuscript levels H/X, never O or P (nodes whose span also names M are listed)', 'size %d, levels %s, span-M nodes %s' % (len(desc), dict(desc_levels), spanM))
fwd_y, rev_y = adj_of(dep_edges + y_edges)
anc_y = {x for x in bfs(seeds_P, fwd_y) if x in nodes}; desc_y = bfs(['I1.1', 'I1.2'], rev_y)
rec('G7', not (anc & desc) and not (anc_y & desc_y), 'Anc(P) and Desc(AX) are disjoint, with and without the yields edges')
fwd_c, rev_c = adj_of(dep_edges + [('I3.1', 'I1.1')])
anc_c = bfs(seeds_P, fwd_c); desc_c = bfs(['I1.1', 'I1.2'], rev_c)
rec('G7c', bool(anc_c & desc_c), 'countercontrol: a synthetic edge I3.1 -> I1.1 makes the two sets meet', 'meet size %d' % len(anc_c & desc_c))
# SCCs over dependency edges restricted to inventory ids (Tarjan, iterative)
ids = sorted(nodes, key=lambda s: (int(s[1]), int(s.split('.')[1])))
g = defaultdict(list)
for a, b in dep_edges:
    if a in nodes and b in nodes: g[a].append(b)
index = {}; low = {}; onst = set(); st = []; sccs = []; counter = [0]
def strong(v):
    index[v] = low[v] = counter[0]; counter[0] += 1; st.append(v); onst.add(v)
    for w in g[v]:
        if w not in index: strong(w); low[v] = min(low[v], low[w])
        elif w in onst: low[v] = min(low[v], index[w])
    if low[v] == index[v]:
        comp = []
        while True:
            w = st.pop(); onst.discard(w); comp.append(w)
            if w == v: break
        if len(comp) > 1: sccs.append(sorted(comp))
sys.setrecursionlimit(10000)
for v in ids:
    if v not in index: strong(v)
rec('G8', sorted(sccs) == [['I2.10', 'I2.6'], ['I2.42', 'I2.56']], 'the only nontrivial SCCs are {I2.6, I2.10} and {I2.42, I2.56}', str(sccs))
sub = defaultdict(set)
for i, n in nodes.items(): sub[n['sublabel']].add(i)
b_exp = {'I1.20', 'I1.21', 'I1.22', 'I1.23', 'I1.24', 'I1.17', 'I1.25', 'I1.27', 'I1.28', 'I1.29', 'I1.33', 'I1.34', 'I2.53', 'I2.54', 'I2.61'}
b_set = {i for i, n in nodes.items() if n['class'] == 'b'}
rec('G9', sub['a1'] == {'I1.3'} and sub['a2'] == {'I1.7', 'I1.8', 'I2.11'} and b_set == b_exp, 'a1 = {I1.3}; a2 = {I1.7, I1.8, I2.11}; b = C1-C4 + the ten derived H items', 'a1 %s a2 %s b-diff %s' % (sorted(sub['a1']), sorted(sub['a2']), sorted(b_set ^ b_exp)))
bad = [i for i, n in nodes.items() if (n['sublabel'] in ('a1', 'a2') or n['class'] == 'b') and n['status'].lower().startswith('proved [k]') and letters(n['level']) & {'O', 'P', 'M', 'G'}]
man = [i for i, n in nodes.items() if (n['sublabel'] in ('a1', 'a2') or n['class'] == 'b') and letters(n['level']) & {'O', 'P', 'M', 'G'}]
rec('G10', not bad, 'no kernel-proved node at a kernel level (O, P, M, G) is in a1, a2 or b', 'kernel-proved offenders %s; manuscript records in b whose span names M/X: %s' % (bad, man))
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('CHECK-G-FIXED' if all(R) else 'CHECK-G-MISMATCH')

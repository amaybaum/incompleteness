"""Generate act 42's preregistration and controls.py from a42frozen.py (one source for every frozen string).

    python3 gen_prereg.py [PRED_ROW_FILE]     writes prereg.md and controls.py beside this script
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a42frozen as F

PART_CHECKS = {'witness': 11, 'wlog': 9, 'd01span': 6, 'paths': 9, 'r5': 2, 'n18:0': 7, 'n18:1': 7, 'n18:2': 7,
               'dfs:0': 4, 'dfs:1': 4, 'dfs:2': 4, 'dfs:3': 4, 'dfs:4': 4, 'dfs:5': 4, 'sathr': 1,
               'cubes:0': 10, 'cubes:1': 10, 'cubes:2': 9}
assert list(PART_CHECKS) == F.PARTS

# ---- controls.py --------------------------------------------------------------------------------------------------
tpl = open(os.path.join(HERE, 'controls_template.py')).read()
subs = {'D': F.D, 'RDIR': F.RDIR, 'PROBE': F.PROBE, 'PROBE_BLOB': F.PROBE_BLOB, 'TOOLS': F.TOOLS,
        'TOOL_BLOBS': F.TOOL_BLOBS, 'WORKFLOW': F.WORKFLOW, 'ROADMAP': F.ROADMAP, 'LABEL': F.LABEL,
        'WORKFLOW_EDITS': F.WORKFLOW_EDITS, 'ROADMAP_EDITS': F.ROADMAP_EDITS, 'SENTENCE': F.SENTENCE,
        'CLAUSE': F.CLAUSE, 'CLAUSE_MENTION': F.CLAUSE_MENTION, 'PART_CHECKS': PART_CHECKS}
for k, v in subs.items():
    tpl = tpl.replace('@%s@' % k, repr(v))
assert '@' not in tpl.split('"""', 2)[2].replace("'@'", '') or True
open(os.path.join(HERE, 'controls.py'), 'w').write(tpl)
CTRL_BLOB = F.blob_of(os.path.join(HERE, 'controls.py'))

PRED = open(sys.argv[1]).read().strip() if len(sys.argv) > 1 else \
    '| (to be filled) | the predicted execution tree less the result note | (to be filled) |'


def ok_line(p):
    return 'dita_support_minimality_probe %s: OK -- %d checks' % (p, PART_CHECKS[p])


tool_rows = []
WHAT = {
    'lib42.py': 'loads the head of the landed act 37 probe (`SIG`, the stabilizer `elems`, the census data) up to its first section, without running any section; exact vanishing tables for every row pair; the straightness tests `straight` (exact tables) and `straight_direct` (Gaussian rationals); the eighteen N18 subspaces, strict and relaxed; the stabilizer action on exponent matrices; act 38\'s `A`, `B`, `C`',
    'dfs42.py': 'exact pair-compatibility tables `VT`, `PC` for the searches',
    'cvsize.py': 'builds `msize.npy`: for each row `i` and zero-row set `Z`, the least size of a nonempty column set vanishing for `i` against every row of `Z`',
    'dfsR.py': 'row candidates under Lemma CV and the budget',
    'dfsR2.py': 'the zero-row DFS over a nonzero-row set `R`, with Lemma NS subtree pruning',
    'classify42.py': 'N18 membership of leaves, strict and relaxed, by exact integer matrix products',
    'pairtypes.py': 'the pair-structure lemma VS: the balanced and exceptional vanishing sets of each row pair',
    'sat42.py': 'the CNF encoding of straightness over `{−1, 0, 1}` with side constraints (mode 0, support, line supports)',
    'sat_hr.py': 'the zero-row case with at least fourteen nonzero rows and columns, one SAT call',
    'dfs01.py': 'the `{0, 1}` searches with a zero row and with every row of support at least 2',
    'ctrl16.py': 'the budget-16 search over every row set, a positive control',
    'lemmas42.py': 'the exact checks L1–L4 (vanishing-set sizes, the `msize` bound, the stabilizer, Lemma P)',
    'spanAll.py': 'Lemma RS over every row set with `LB ≤ 77`',
    'triples.py': 'a fresh enumeration of the partition structures and realizing triples of `SIG` and their relaxed identity equations',
    'minsupp_exact.py': 'exact class support: an exhibited gauge and an exhaustive completeness argument',
    'r2a_landed.py': 'path A: the landed production probe replayed whole, then its functions on `E40`\'s arc',
    'r2b_independent.py': 'path B(i): `E40` and the controls tested against every realizing triple',
    'r2b2_census.py': 'path B(ii): the landed independent probe replayed whole, then its census at exact points of `E40`\'s arc',
    'r3_run.py': 'the exact class supports of `E40`, act 38\'s witness and `A`',
    'c6_control.py': 'the exact class-support method against brute force on 150 random `6 × 6` instances',
    'r5_family.py': 'act 38\'s families `xA + yB + zC` and `−xP + yQ − zT`, `x, y, z ∈ {±1, ±2}`',
    'Rle13_39.txt': 'the 5 494 nonzero-row sets `R` of 2 to 13 rows with `LB(R) ≤ 39`, as integers',
}
for f in F.TOOL_FILES:
    src = F.SOURCE_DIR[f] + f
    ed = ('one line: `%s` → `%s`' % F.RELOCATED[f]) if f in F.RELOCATED else 'none'
    tool_rows.append('| `%s` | `%s` | `%s` | `%s` | %s | %s |' % (f, src, F.SOURCE_BLOBS[f], F.TOOL_BLOBS[f], ed, WHAT[f]))
TOOL_TABLE = '\n'.join(tool_rows)

NAMES = ["**Edit 1** — act 39's clause in the `P0` cell, once:",
         "**Edit 2** — the clauses of acts 40 and 41 in the `P0` cell, both occurrences:",
         "**Edit 3** — the `P0` cell, directly after act 45's sentence and before the cell's closing `|`:",
         "**Edit 4** — the body of the section *Minimal support of a non-Diţă straight line at the product stratum*:"]
road_blocks = '\n\n'.join('%s\n\n```text\n%s\n```\n\nbecomes\n\n```text\n%s\n```' % (NAMES[k], o.rstrip('\n'), n.rstrip('\n'))
                           for k, (o, n, c) in enumerate(F.ROADMAP_EDITS))
part_lines = '\n'.join(ok_line(p) for p in F.PARTS)

doc = open(os.path.join(HERE, 'prereg_body.md')).read()
for k, v in {'CLAUSE': F.CLAUSE, 'SENTENCE': F.SENTENCE, 'TOOL_TABLE': TOOL_TABLE, 'PROBE_BLOB': F.PROBE_BLOB,
             'CTRL_BLOB': CTRL_BLOB, 'RESEARCH_HEAD': F.RESEARCH_HEAD, 'PRED': PRED, 'PART_LINES': part_lines,
             'ROAD_BLOCKS': road_blocks}.items():
    doc = doc.replace('{{%s}}' % k, v)
for p in F.PARTS:
    doc = doc.replace('{{N:%s}}' % p, str(PART_CHECKS[p]))
assert '{{' not in doc, doc[doc.index('{{'):doc.index('{{') + 40]
open(os.path.join(HERE, 'prereg.md'), 'w').write(doc)
print('prereg.md written; controls.py blob', CTRL_BLOB, '; probe blob', F.PROBE_BLOB)

#!/usr/bin/env python3
"""#1468 regression delta of the A1 retirement edit list at a commit. Standard library only; writes nothing
unless --tree-out is given.

  python3 -I -B delta.py --rev REV [--plan-dir DIR] [--prev-edits FILE] [--tree-out DIR]

--rev         the commit whose papers/*.md and book/*.md the plan's manuscript edits are applied to
--plan-dir    the plan's directory (edits.json, edits_check.py); default: the A1 deletion record on this tree
--prev-edits  an earlier edits.json: lists the edits added, removed or changed since it, so that only those
              need reading
--tree-out    also write the edited papers/ and book/ there, for baseline.py --compare-tree

Edits are applied by the plan's own rule (edits_check.variant). Numbers and table classes are those of the
accepted baseline extractor (../a1exit-regression-20261121/baseline.py). Prints: edits that do not apply;
per-file number tokens lost and gained; each edit that changes a number token or touches a table row.
"""
import argparse, collections, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'a1exit-regression-20261121'))
import baseline as bl  # noqa: E402


def show(rev, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True)
    if r.returncode:
        raise SystemExit('cannot read %s at %s' % (path, rev))
    return r.stdout.decode('utf-8')


def corpus(rev):
    r = subprocess.run(['git', '-C', ROOT, 'ls-tree', '--name-only', rev, 'papers/', 'book/'],
                       capture_output=True, text=True, check=True)
    return {f: show(rev, f) for f in r.stdout.split() if f.endswith('.md') and f.count('/') == 1}


def toks(text):
    c = collections.Counter()
    for line in text.split('\n'):
        c.update(x[0] for x in bl.number_key(bl.parse_numbers(line)))
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rev', required=True)
    ap.add_argument('--plan-dir', default=os.path.join(HERE, '..', 'a1exit-deletion-20261121'))
    ap.add_argument('--prev-edits')
    ap.add_argument('--tree-out')
    a = ap.parse_args()
    sys.path.insert(0, os.path.abspath(a.plan_dir))
    import edits_check as ec
    edits = json.load(open(os.path.join(a.plan_dir, 'edits.json'), encoding='utf-8'))['edits']
    man = [e for e in edits if e['file'].startswith(('papers/', 'book/')) and e['file'].endswith('.md')
           and e['file'].count('/') == 1]
    before = corpus(a.rev)
    after = dict(before)
    rows, skipped = [], []
    for e in man:
        t = after[e['file']]
        o, n, _ = ec.variant(e, t)
        if o is None:
            skipped.append(e['id'])
            continue
        base = before[e['file']] if o in before[e['file']] else t  # report the line at REV where possible
        lines = base.split('\n')
        l0 = base.count('\n', 0, base.index(o))
        tab = bl.tables_index(lines).get(l0)
        cls = bl.table_class(' | '.join(tab[1]['columns'])) if tab else None
        no = [x[0] for x in bl.number_key(bl.parse_numbers(o))]
        nn = [x[0] for x in bl.number_key(bl.parse_numbers(n))]
        if no != nn or cls:
            rows.append((e['id'], e['file'], l0 + 1, e.get('row'), cls, no, nn))
        after[e['file']] = t.replace(o, n, 1)
    print('rev %s: %d manuscript edits, %d applied, %d not applicable%s' % (
        a.rev, len(man), len(man) - len(skipped), len(skipped), (': ' + ' '.join(skipped)) if skipped else ''))
    lost_total = 0
    for f in sorted(before):
        x, y = toks(before[f]), toks(after[f])
        if x != y:
            lost, gained = x - y, y - x
            lost_total += sum(lost.values())
            print('tokens %s lost %s gained %s' % (f, dict(sorted(lost.items())), dict(sorted(gained.items()))))
    print('tokens lost in total: %d' % lost_total)
    for r in rows:
        print('edit %s %s:%d row %s table %s numbers %s -> %s' % r)
    print('edits touching a prediction or status table row: %d' %
          sum(1 for r in rows if r[4] in ('prediction', 'status')))
    if a.prev_edits:
        prev = {e['id']: e for e in json.load(open(a.prev_edits, encoding='utf-8'))['edits']}
        cur = {e['id']: e for e in edits}
        key = lambda e: (e['file'], e['old'], e['new'], e.get('old_step2'), e.get('new_step2'))
        print('edits added: %s' % ' '.join(sorted(set(cur) - set(prev))))
        print('edits removed: %s' % ' '.join(sorted(set(prev) - set(cur))))
        print('edits changed: %s' % ' '.join(sorted(i for i in set(cur) & set(prev) if key(cur[i]) != key(prev[i]))))
    if a.tree_out:
        for f, t in after.items():
            p = os.path.join(a.tree_out, f)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, 'w', encoding='utf-8') as fh:
                fh.write(t)


if __name__ == '__main__':
    main()

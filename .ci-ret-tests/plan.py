"""The CI matrix: every job of the run, as a GitHub Actions output line (matrix=<json>). No argument."""
import json, os

H = os.path.dirname(os.path.abspath(__file__))


def mutants():
    src = open(os.path.join(H, 'mutants_all.py'), encoding='utf-8').read()
    src = src.split('origin, fn, kind, reason, edits, want = M[which]')[0]
    ns = {}
    exec(src.replace('wt, which, outdir = sys.argv[1:4]', "wt, which, outdir = '/nonexistent', None, None"), ns)
    return list(ns['M'])


BASELINE = ['co', 'co-recon', 'co-self', 'cr', 'cr-self', 'cr-gate', 'legacy']
CLI = ['N-all-free', 'N-no-joiners', 'N-64-as-head']
ISO = ['headless', 'farline', 'digitbound', 'pin:a', 'pin:b', 'pin:c', 'decimal', 'crash']


def jobs():
    return ([{'kind': 'baseline', 'name': n} for n in BASELINE] + [{'kind': 'regression42', 'name': 'all'}] +
            [{'kind': 'mutant', 'name': n} for n in mutants()] + [{'kind': 'cli', 'name': n} for n in CLI] +
            [{'kind': 'iso', 'name': n} for n in ISO])


if __name__ == '__main__':
    j = jobs()
    print('matrix=' + json.dumps({'include': [dict(x, id=('%s-%s' % (x['kind'], x['name'])).replace(':', '_'))
                                              for x in j]}))
    print('count=%d' % len(j))

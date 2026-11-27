"""WIP / UNVERIFIED staging draft. Countercontrols for `rederive_allow_root.py`: each mutant of the draft allow root
must make the re-derivation fail (exit 1), and the unmutated draft must make it hold (exit 0).

Usage: python3 -I countercontrols.py --repo <git dir> --tool <tool root> --root <draft root> --deny <draft dr-deny>
Prints one line per case and exits 0 only when every case behaves as stated.
"""
import argparse
import copy
import json
import os
import subprocess
import sys
import tempfile


def mutants(d):
    def m(f):
        x = copy.deepcopy(d)
        f(x)
        return x

    def w1a_equiv(x):
        r = copy.deepcopy(x['rules'][0])
        r.update(id='W1-z', scope={'files': ['papers/SM.md']})
        r['matcher'] = dict(r['matcher'], literal='satisfying the six structural properties', context=[])
        x['rules'].append(r)
    return [
        ('context hash of a W1-b fingerprint changed', m(lambda x: x['rules'][0]['fingerprints'][0].update(
            context_sha256='0' * 64))),
        ('W1-c allowance raised to finit: 2', m(lambda x: x['rules'][1]['fingerprints'][0].update(
            negative_allowance={'finit': 2}))),
        ('W2-a scope missing its mirror', m(lambda x: x['rules'][3]['scope'].update(
            files=x['rules'][3]['scope']['files'][:1]))),
        ('a W1-a equivalent under another id', m(w1a_equiv)),
        ('W1-d literal shortened to the generic trigger', m(lambda x: x['rules'][2]['matcher'].update(
            literal='six structural'))),
        ('W1-a sentence dropped from W1-b negative examples', m(lambda x: x['rules'][0].update(
            negative_examples=x['rules'][0]['negative_examples'][:1]))),
        ('W2-b max_instances 3', m(lambda x: x['rules'][4].update(max_instances=3))),
    ]


def main():
    ap = argparse.ArgumentParser()
    for k in ('repo', 'tool', 'root', 'deny'):
        ap.add_argument('--' + k, required=True)
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    d = json.load(open(a.root, encoding='utf-8'))
    tmp = tempfile.mkdtemp()

    def run(path):
        return subprocess.run([sys.executable, '-I', os.path.join(here, 'rederive_allow_root.py'), '--repo', a.repo,
                               '--tool', a.tool, '--root', path, '--deny', a.deny],
                              capture_output=True).returncode
    ok = run(a.root) == 0
    print('unmutated draft holds:', ok)
    for i, (name, x) in enumerate(mutants(d)):
        p = os.path.join(tmp, 'm%d.json' % i)
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(x, fh, ensure_ascii=False)
        rc = run(p)
        print('mutant detected (%s):' % name, rc == 1)
        ok = ok and rc == 1
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()

"""E3: apply the evidence-retention archive's R4 well-formedness check to a retained expected result.

Usage:
    python3 -I E3_r4_check.py CHECK_RETENTION_PY RESULTS_JSON

CHECK_RETENTION_PY  check_retention.py of the frozen archive, e.g.
                    `git show 48b18ac5:verification/audits/evidence-retention/check_retention.py > X`
RESULTS_JSON        e.g. `git show 4a260ca9:papers/introduction_repro/results-121598983127.json > Y`

The archive left the tree at 5c4e5087, so its tree mode does not apply to `papers/introduction_repro/`;
this runs only R4 (`check_results`) on the file, then three countercontrols that must each be caught.
Exit status 0 iff the file passes and every countercontrol is caught.
"""
import copy
import importlib.util
import json
import sys


def load(path):
    spec = importlib.util.spec_from_file_location('check_retention', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def r4(mod, text, entry):
    fails = []
    mod.check_results('E3', 'results.json', text, entry, fails.append)
    return fails


def main():
    mod = load(sys.argv[1])
    text = open(sys.argv[2], encoding='utf-8').read()
    r = json.loads(text)
    entry = {'run': r['run']['id'], 'job': r['run']['job_id'], 'head_sha': r['run']['head_sha']}
    base = r4(mod, text, entry)
    print('R4 on the retained file:', 'no failure' if not base else base)
    bad = 1 if base else 0
    mutations = {
        'no build': lambda d: d['expected'].__setitem__('build_success', False),
        'short head id': lambda d: d['run'].__setitem__('head_sha', d['run']['head_sha'][:12]),
        'no recipe': lambda d: d['reproduce'].__setitem__('recipe', []),
    }
    for name, f in mutations.items():
        d = copy.deepcopy(r)
        f(d)
        got = r4(mod, json.dumps(d), entry)
        print('countercontrol %-14s %s' % (name, 'caught: ' + got[0] if got else 'NOT CAUGHT'))
        bad += 0 if got else 1
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

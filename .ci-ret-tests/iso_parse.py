"""Parse isolated.py output into {label: PASS|FAIL} (and the headless flags line). Shared by the expectation build and
the CI check, so both read the same keys. argv for a check: <expected.json> <output files...>; exit 1 on any mismatch."""
import json, re, sys


def parse(paths):
    exp = {}
    for p in paths:
        for l in open(p, encoding='utf-8', errors='replace'):
            m = re.match(r'^  (.+?)\s+verdict (PASS|FAIL)\s', l)
            if m:
                exp[m.group(1).strip()] = m.group(2)
                continue
            m = re.match(r'^  (real|N-pin-digest-off)\s+near-miss \+ (.+?)\s+tree exit (\d)', l)
            if m:
                exp['%s | near-miss + %s' % (m.group(1), m.group(2).strip())] = 'FAIL' if m.group(3) == '1' else 'PASS'
                continue
            m = re.match(r'^  (real|N-pin-digest-off)\s+(.+?)\s+exit (\d)\s', l)
            if m:
                exp['%s | %s' % (m.group(1), m.group(2).strip())] = 'FAIL' if m.group(3) == '1' else 'PASS'
                continue
            if l.startswith('  same exit:'):
                exp['headless flags'] = l.strip()
    return exp


if __name__ == '__main__':
    want = json.load(open(sys.argv[1], encoding='utf-8'))
    got = parse(sys.argv[2:])
    keys = [k for k in got if k in want]
    bad = [(k, got[k], want[k]) for k in keys if got[k] != want[k]]
    for k, g, w in bad:
        print('MISMATCH %s: got %s, expected %s' % (k, g, w))
    print('checked %d isolated verdicts against expectations; %d mismatch(es)%s' % (
        len(keys), len(bad), '' if keys else ' (NONE CHECKED)'))
    sys.exit(1 if bad or not keys else 0)

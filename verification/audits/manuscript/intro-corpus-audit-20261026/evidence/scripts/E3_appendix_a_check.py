"""E3: check the Introduction's Appendix A declarations against the retained expected result.

Usage:
    python3 -I E3_appendix_a_check.py INTRODUCTION.md EXPECTED.json LEAN_TREE

INTRODUCTION.md  papers/Introduction.md at the commit under audit (e.g. `git show 4a260ca9:papers/Introduction.md`)
EXPECTED.json    papers/introduction_repro/results-121598983127.json at the same commit
LEAN_TREE        a directory holding verification/lean-mathlib/OIBridge/ at the pinned Lean commit (17b830bc)

For every backticked identifier in Appendix A that names a declaration, with its (Module:line) or (:line):
  1. the source line at LEAN_TREE declares that short name (theorem/lemma/def ... <name>);
  2. the expected result carries exactly one report of a fully qualified name ending in .<name>, in that module;
  3. that report's axioms are exactly propext, Classical.choice, Quot.sound.
Also reports the expected result's markers and gate verdict. Exit status 0 iff every check passes.
"""
import json
import os
import re
import sys

ALLOWED = ['propext', 'Classical.choice', 'Quot.sound']


def appendix_items(text):
    sec = text.split('## Appendix A.', 1)[1].split('## Appendix B.', 1)[0]
    items = []
    for line in sec.splitlines():
        if not line.startswith('- '):
            continue
        # walk tokens in order; a (Module:n, :m, :k) group assigns lines to the preceding names
        pending = []
        module = None
        for m in re.finditer(r'`([A-Za-z_][A-Za-z0-9_.]*)`|\(([^()]*)\)|(?<![\w`]):(\d+)', line):
            if m.group(1):
                pending.append(m.group(1))
            elif m.group(2) is not None:
                grp = m.group(2)
                refs = re.findall(r'(?:([A-Z][A-Za-z0-9]*):|:)(\d+)', grp)
                if not refs:
                    continue
                nums = []
                for mod, n in refs:
                    if mod:
                        module = mod
                    nums.append((module, int(n)))
                # one line per pending name, in order; extra names (none expected) unmatched
                if 'premise discharged by' in grp:
                    # "(IsometryExtension:179, premise discharged by `x`, :116)": first ref -> earlier name
                    inner = re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', grp)
                    items.append((pending[-1], nums[0]))
                    items.append((inner[0], nums[1]))
                    pending = []
                    continue
                for name, ref in zip(pending, nums):
                    items.append((name, ref))
                pending = pending[len(nums):]
            elif m.group(3) and pending:
                items.append((pending.pop(0), (module, int(m.group(3)))))
    return items


def main():
    intro, expected, tree = sys.argv[1:4]
    text = open(intro, encoding='utf-8').read()
    exp = json.load(open(expected, encoding='utf-8'))['expected']
    items = appendix_items(text)
    fails = 0
    seen = set()
    for name, (module, line) in items:
        if (name, module, line) in seen:
            continue
        seen.add((name, module, line))
        path = os.path.join(tree, 'verification', 'lean-mathlib', 'OIBridge', module + '.lean')
        src = open(path, encoding='utf-8').read().splitlines()
        decl = src[line - 1] if 0 < line <= len(src) else ''
        ok_decl = re.search(r'\b(theorem|lemma|def|abbrev|instance)\s+' + re.escape(name) + r'\b', decl) is not None
        reps = [r for r in exp['modules'].get('OIBridge/' + module + '.lean', {}).get('reports', [])
                if r['name'].split('.')[-1] == name]
        ok_rep = len(reps) == 1 and reps[0]['axioms'] == ALLOWED
        status = 'OK  ' if ok_decl and ok_rep else 'FAIL'
        if status == 'FAIL':
            fails += 1
        print(f"{status} {name:58s} {module}:{line} decl={'yes' if ok_decl else 'NO'} "
              f"reports={len(reps)} axioms={reps[0]['axioms'] if reps else None}")
    print(f'declarations checked: {len(seen)}; failures: {fails}')
    print('markers:', exp['markers'])
    print('gate verdict:', exp['gate']['verdict'], f"({exp['gate']['steps_pass']}/{exp['gate']['steps_total']})")
    print('build_success:', exp['build_success'])
    if any(exp['markers'].values()) or not exp['build_success'] or exp['gate']['steps_pass'] != exp['gate']['steps_total']:
        fails += 1
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()

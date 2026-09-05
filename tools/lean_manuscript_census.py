#!/usr/bin/env python3
"""lean_manuscript_census.py — are the manuscripts synchronized with the Lean corpus?

The verification layer has repeatedly outrun the manuscripts: a theorem is strengthened, the
verification notes and guards follow in the same round, and a paper keeps citing the superseded
package. The staleness check compares a source with its own build and cannot see this; the
R7 guards pin individual statements and cannot see a citation they were never told about. This
check reads the whole manuscript tree against the whole kernel and a registry
(verification/lean-manuscript-census.json) that records, for every OIBridge module, which
publication-facing family it belongs to and what the manuscripts must carry for it.

WHAT IT CHECKS
  1. RESOLUTION   every kernel identifier cited in a manuscript is declared in OIBridge, and
                  every cited OIBridge path exists.
  2. SUPERSESSION a manuscript paragraph citing an identifier the registry marks superseded also
                  cites its successor (a citation of the older form is legitimate only next to
                  the current one).
  3. COVERAGE     every OIBridge module is assigned to exactly one registry family, so a new
                  module cannot appear without a disposition (current / consistent-uncited /
                  scope-consistent / kernel-only / verification-only).
  4. ANCHORS      every family recorded as current, consistent-uncited or scope-consistent names
                  at least one manuscript anchor, and every anchor the registry names is present
                  in the manuscript it names, so a family whose conclusion the manuscripts carry
                  cannot silently lose its statement.

WHAT IT CANNOT CHECK
  The check is complete relative to the maintained registry. It cannot infer that a theorem inside
  an existing module has become stronger: a strengthening whose supersession entry or anchor is not
  recorded passes all four checks. The registry contract (AGENTS.md, section A.35) therefore
  requires every publication-facing strengthening to update the registry in the same commit, and
  guard R7-MSP pins that contract.

It prints the classification table and exits nonzero on any failure.

Usage:  python3 tools/lean_manuscript_census.py [--root DIR]
"""
import glob
import json
import os
import re
import sys

STATUSES = ('current', 'consistent-uncited', 'scope-consistent', 'kernel-only',
            'verification-only')
# the dispositions under which the manuscripts carry the family's conclusion or scope, and which
# must therefore name at least one anchor
ANCHORED = ('current', 'consistent-uncited', 'scope-consistent')
IDENT = re.compile(r'`([A-Za-z_][A-Za-z0-9_\'₀₁₂]*)`')
PATH = re.compile(r'`(OIBridge/[A-Za-z0-9_]+\.lean)`')
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:protected\s+)?'
                  r'(?:theorem|lemma|def|abbrev|structure|instance|class)\s+'
                  r'([A-Za-z_][A-Za-z0-9_\'₀₁₂.]*)', re.M)


def load_kernel(root):
    decls, modules = {}, []
    for lf in sorted(glob.glob(os.path.join(root, 'verification/lean-mathlib/OIBridge/*.lean'))):
        mod = os.path.basename(lf)[:-5]
        modules.append(mod)
        src = open(lf, encoding='utf-8').read()
        for ident in DECL.findall(src):
            decls.setdefault(ident.split('.')[-1], set()).add(mod)
            decls.setdefault(ident, set()).add(mod)
    return decls, modules


def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    reg = json.load(open(os.path.join(root, 'verification/lean-manuscript-census.json'),
                         encoding='utf-8'))
    decls, modules = load_kernel(root)
    fails = []
    msgs = []

    # 1. resolution, over every manuscript source (papers and the book chapters + mirror)
    sources = sorted(glob.glob(os.path.join(root, 'papers/*.md'))) + \
        sorted(glob.glob(os.path.join(root, 'book/*.md')))
    texts = {}
    cited = {}
    for f in sources:
        s = open(f, encoding='utf-8').read()
        texts[f] = s
        for m in re.finditer(r'kernel:([^)]*)\)', s):
            for i in IDENT.findall(m.group(1)):
                cited.setdefault(i, set()).add(os.path.relpath(f, root))
        for p in PATH.findall(s):
            if not os.path.exists(os.path.join(root, 'verification/lean-mathlib', p)):
                fails.append(f"  PATH   {p} cited in {os.path.relpath(f, root)} does not exist")
    for i, fs in sorted(cited.items()):
        if i not in decls:
            fails.append(f"  IDENT  `{i}` cited in {sorted(fs)} is declared nowhere in OIBridge")

    # 2. supersession, paragraph by paragraph
    sup = reg['supersessions']
    for old, new in sup.items():
        if new not in decls:
            fails.append(f"  REGISTRY successor `{new}` of `{old}` is not declared in OIBridge")
        for f, s in texts.items():
            for para in s.split('\n\n'):
                if f'`{old}`' in para and f'`{new}`' not in para:
                    fails.append(f"  STALE  {os.path.relpath(f, root)} cites `{old}` without its "
                                 f"successor `{new}` in the same paragraph")

    # 3. coverage of the module inventory
    assigned = {}
    for fam in reg['families']:
        if fam['status'] not in STATUSES:
            fails.append(f"  STATUS family '{fam['name']}' has unknown status {fam['status']!r}")
        for mod in fam['modules']:
            if mod in assigned:
                fails.append(f"  DUP    module {mod} assigned to '{assigned[mod]}' and "
                             f"'{fam['name']}'")
            assigned[mod] = fam['name']
    for mod in modules:
        if mod not in assigned:
            fails.append(f"  UNCLASSIFIED module {mod} has no registry family; give it a "
                         f"disposition in verification/lean-manuscript-census.json")
    for mod in assigned:
        if mod not in modules:
            fails.append(f"  GHOST  registry names module {mod}, which does not exist")

    # 4. anchors: a family the manuscripts carry must name at least one, and each must be present
    for fam in reg['families']:
        if fam['status'] in ANCHORED and not fam.get('manuscript'):
            fails.append(f"  NOANCHOR family '{fam['name']}' is {fam['status']} but names no "
                         f"manuscript anchor; a {fam['status']} family must name at least one")
        for a in fam.get('manuscript', []):
            path = os.path.join(root, a['file'])
            if not os.path.exists(path):
                fails.append(f"  ANCHOR file {a['file']} for '{fam['name']}' does not exist")
                continue
            flat = re.sub(r'\s+', ' ', open(path, encoding='utf-8').read())
            if a['anchor'] not in flat:
                fails.append(f"  ANCHOR '{fam['name']}': {a['file']} lacks {a['anchor']!r}")

    # the table
    ncur = sum(1 for f in reg['families'] if f['status'] == 'current')
    print("lean_manuscript_census: %d modules, %d families, %d cited identifiers, "
          "%d supersessions" % (len(modules), len(reg['families']), len(cited), len(sup)))
    for fam in reg['families']:
        print("  %-19s %-52s %d module(s), %d anchor(s)"
              % (fam['status'], fam['name'], len(fam['modules']), len(fam.get('manuscript', []))))
    if fails:
        print()
        for m in fails:
            print(m)
        print(f"\nlean_manuscript_census: FAILED ({len(fails)} problem(s))")
        return 1
    print(f"lean_manuscript_census: OK (every cited identifier and path resolves, no superseded "
          f"citation without its successor, every module classified, every carried family "
          f"anchored and every anchor present; {ncur} current families; complete relative to "
          f"the maintained registry)")
    return 0


if __name__ == '__main__':
    sys.exit(main())

"""Import closures of OIBridge modules from their header `import` lines.

Usage: python3 -I closure.py <lean-mathlib dir> <design dir> <root module>...
Prints, for each root, the OIBridge closure and the direct Mathlib imports met in it.
Then prints the set difference closure(EqvK2MaxCone) minus closure(design roots).
"""
import os
import re
import sys


def strip_header(text):
    """Return the import module names from the file header (before first non-import token)."""
    out = []
    i = 0
    n = len(text)
    depth = 0
    buf = []
    # remove comments (nested block comments and line comments) up to first non-import token
    while i < n:
        if text.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth > 0:
            if text.startswith('-/', i):
                depth -= 1
                i += 2
            else:
                i += 1
            continue
        if text.startswith('--', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
            continue
        buf.append(text[i])
        i += 1
    toks = ''.join(buf).split()
    k = 0
    while k < len(toks):
        if toks[k] == 'prelude':
            k += 1
            continue
        if toks[k] == 'import' and k + 1 < len(toks):
            out.append(toks[k + 1])
            k += 2
            continue
        break
    return out


def resolve(mod, roots):
    rel = mod.replace('.', '/') + '.lean'
    for r in roots:
        p = os.path.join(r, rel)
        if os.path.exists(p):
            return p
    return None


def closure(start, roots):
    seen = {}
    mathlib = {}
    stack = list(start)
    while stack:
        m = stack.pop()
        if m in seen or m in mathlib:
            continue
        p = resolve(m, roots)
        if p is None:
            mathlib[m] = True
            continue
        with open(p, encoding='utf-8') as f:
            imps = strip_header(f.read())
        seen[m] = imps
        stack.extend(imps)
    return seen, sorted(mathlib)


def main():
    lm, dd = sys.argv[1], sys.argv[2]
    roots = [lm, dd]
    sets = {}
    for root in sys.argv[3:]:
        mods, ext = closure([root], roots)
        sets[root] = (set(mods), set(ext), mods)
        print('== %s: %d local modules, %d external (non-local) imports' % (root, len(mods), len(ext)))
        print('   local:', ' '.join(sorted(mods)))
        print('   external:', ' '.join(ext))
    if 'OIBridge.EqvK2MaxCone' in sets:
        a_loc, a_ext, a_mods = sets['OIBridge.EqvK2MaxCone']
        others = [r for r in sets if r != 'OIBridge.EqvK2MaxCone']
        o_loc = set().union(*[sets[r][0] for r in others]) if others else set()
        o_ext = set().union(*[sets[r][1] for r in others]) if others else set()
        print('== closure(EqvK2MaxCone) minus union of closures(%s)' % ', '.join(others))
        print('   local:', ' '.join(sorted(a_loc - o_loc)))
        print('   external:', ' '.join(sorted(a_ext - o_ext)))
        for m in sorted(a_loc - o_loc):
            print('   %s imports %s' % (m, ' '.join(a_mods[m])))


if __name__ == '__main__':
    main()

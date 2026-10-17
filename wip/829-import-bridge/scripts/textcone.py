"""Static (textual) dependency cone of a design declaration.

Usage: python3 -I textcone.py <target short name> <oibridge dir> <design file>...
Splits the design files into declaration spans (a span runs from one top-level declaration to the
next), takes identifier tokens of each span, and closes over design declarations from the target.
Every token in the cone that is not a design declaration is looked up among OIBridge declarations
(short-name match, any namespace) and reported with its defining module. This over-approximates
direct citations (a short-name match may be spurious) and under-approximates elaboration-introduced
references (instances, simp lemmas, coercions), which only a kernel walk sees.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decls import decls, strip_comments  # noqa: E402

TOK = re.compile(r"[A-Za-z_][A-Za-z0-9_'!?₀-₉]*(?:\.[A-Za-z_][A-Za-z0-9_'!?₀-₉]*)*")


def spans(path):
    ds = decls(path)
    lines = strip_comments(open(path, encoding='utf-8').read()).splitlines()
    out = []
    for k, (p, ln, full, kind) in enumerate(ds):
        end = ds[k + 1][1] - 1 if k + 1 < len(ds) else len(lines)
        # a span also ends at the first top-level command that is not part of a declaration
        for j in range(ln, end):
            if re.match(r'(#|open\b|end\b|section\b|namespace\b|attribute\b|variable\b|noncomputable section)', lines[j]):
                end = j
                break
        out.append((full.rsplit('.', 1)[-1], full, os.path.basename(p), ln, set(TOK.findall('\n'.join(lines[ln - 1:end])))))
    return out


def main():
    target, odir, files = sys.argv[1], sys.argv[2], sys.argv[3:]
    design = {}
    for f in files:
        for short, full, base, ln, toks in spans(f):
            design.setdefault(short, []).append((full, base, ln, toks))
    oib = {}
    for f in sorted(os.listdir(odir)):
        if f.endswith('.lean'):
            for p, ln, full, kind in decls(os.path.join(odir, f)):
                oib.setdefault(full.rsplit('.', 1)[-1], []).append('%s:%d %s' % (f, ln, full))
    seen, stack, ext = {target}, [target], {}
    while stack:
        s = stack.pop()
        for full, base, ln, toks in design.get(s, []):
            for t in toks:
                last = t.rsplit('.', 1)[-1]
                if last in design and last not in seen:
                    seen.add(last); stack.append(last)
                elif last not in design and last in oib:
                    ext.setdefault(last, set()).add(s)
    print('design declarations in the textual cone of %s: %d' % (target, len(seen)))
    mods = {}
    for last in sorted(ext):
        for loc in oib[last]:
            mods.setdefault(loc.split(':')[0], set()).add(last)
    for m in sorted(mods):
        print('%-28s %s' % (m, ' '.join(sorted(mods[m]))))


if __name__ == '__main__':
    main()

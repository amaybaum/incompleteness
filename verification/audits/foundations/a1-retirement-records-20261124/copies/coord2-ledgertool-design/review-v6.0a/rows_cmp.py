"""Independent row comparison: every markdown table row keyed by (first cell); report retained/modified/removed/added."""
import sys, re, collections
def rows(path):
    out = collections.OrderedDict(); dup = collections.Counter()
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        s = line.rstrip('\n')
        if not s.startswith('|') or re.match(r'^\|[-| :]+\|$', s): continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        k = cells[0]; dup[k] += 1
        key = k if dup[k] == 1 else '%s#%d' % (k, dup[k])
        out[key] = (n, s)
    return out
a, b = rows(sys.argv[1]), rows(sys.argv[2])
ret = [k for k in a if k in b and a[k][1] == b[k][1]]
mod = [k for k in a if k in b and a[k][1] != b[k][1]]
rem = [k for k in a if k not in b]
add = [k for k in b if k not in a]
print('A rows', len(a), 'B rows', len(b), 'retained', len(ret), 'modified', len(mod), 'removed', len(rem), 'added', len(add))
for tag, ks in (('MOD', mod), ('REM', rem), ('ADD', add)):
    for k in ks:
        print(tag, k[:60].replace('\n',' '))

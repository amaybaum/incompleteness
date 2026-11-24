"""Independent row comparison: every markdown table line ('|' first char), keyed by
(first cell, occurrence index of that key). Prints removed / added / changed keys and,
separately, a multiset comparison of all table lines."""
import sys, collections
def rows(p):
    d = collections.OrderedDict(); cnt = collections.Counter(); allrows = []
    for l in open(p, encoding='utf-8'):
        if not l.startswith('|'): continue
        cells = [c.strip() for c in l.rstrip('\n').split('|')]
        k = cells[1] if len(cells) > 1 else ''
        if set(k) <= set('-: '): continue          # separator lines
        cnt[k] += 1
        d[(k, cnt[k])] = l.rstrip('\n'); allrows.append(l.rstrip('\n'))
    return d, allrows
a, ra = rows(sys.argv[1]); b, rb = rows(sys.argv[2])
print('table rows', sys.argv[1], len(a), sys.argv[2], len(b))
rem = [k for k in a if k not in b]; add = [k for k in b if k not in a]
chg = [k for k in a if k in b and a[k] != b[k]]
fmt = lambda ks: ', '.join(f'{k}' + (f'#{n}' if n > 1 else '') for k, n in ks)
print('removed:', fmt(rem) or 'none'); print('added:', fmt(add) or 'none'); print('changed:', fmt(chg) or 'none')
ma, mb = collections.Counter(ra), collections.Counter(rb)
print('multiset: lines only in first', sum((ma - mb).values()), '; only in second', sum((mb - ma).values()))
for k in chg:
    print('\n== CHANGED', k); print('-', a[k]); print('+', b[k])

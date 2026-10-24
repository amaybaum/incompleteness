exec(open('corr2.py').read().split("std=G_of")[0])
w5=[w for w in itertools.product(alphabet,repeat=5)]
cards5={w:card_records(w) for w in w5}
for t in passing:
    G=G_of(*t); bad=next((w for w in w5 if qm_records(w,G)!=cards5[w]),None)
    print(t,'agrees with cards on all length-5 words:',bad is None, '' if bad is None else 'first disagreement: '+' '.join(bad))

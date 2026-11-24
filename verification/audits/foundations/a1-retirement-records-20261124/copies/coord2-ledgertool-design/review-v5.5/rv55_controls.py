"""The design's new controls S11-58i, j, k, run through my v5.5 implementation (rv55_parity.v55) and P."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import rv55_parity as rp
cases = [('S11-58i', [{'id': 'a', 'file': 'f', 'old': 'aa', 'new': 'b'}], {'f': 'xaaay'}),
 ('S11-58j', [{'id': '1', 'file': 'f', 'old': 'cat fox', 'new': 'fox cat'}, {'id': '2', 'file': 'f', 'old': 'cat', 'new': 'dog'}], {'f': 'cat fox.'}),
 ('S11-58k', [{'id': '1', 'file': 'f', 'old': 'ab q', 'new': 'xy'}, {'id': '2', 'file': 'f', 'old': 'zz', 'new': 'Q', 'old_step2': 'yc', 'new_step2': 'Q'}], {'f': 'ab qc'})]
for cid, e, t in cases:
    print(cid, 'P:', rp.p_apply(e, t)[0], rp.p_apply(e, t)[1], '| v5.5:', rp.v55(e, t)[0], '| compare:', rp.cmp(e, t), '| selected offset', t['f'].find(e[0]['old']))
# a corrected S11-58k: a variant unique at H, then, after edit 1, only the second variant matches, across the image boundary
fix = [{'id': '1', 'file': 'f', 'old': 'ab q', 'new': 'xy'}, {'id': '2', 'file': 'f', 'old': 'qc', 'new': 'Q', 'old_step2': 'yc', 'new_step2': 'Q'}]
print('S11-58k corrected', 'P:', rp.p_apply(fix, {'f': 'ab qc'}), '| v5.5:', rp.v55(fix, {'f': 'ab qc'})[0], '| compare:', rp.cmp(fix, {'f': 'ab qc'}))

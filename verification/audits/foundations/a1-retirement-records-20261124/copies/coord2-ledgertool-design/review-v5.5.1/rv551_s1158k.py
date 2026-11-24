"""S11-58k as specified in DESIGN-v5.5.1, run through P's own variant()/apply and my v5.5 rule implementation."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import rv55_parity as rp
edits = [{'id': '1', 'file': 'f', 'old': 'ab q', 'new': 'xy'},
         {'id': '2', 'file': 'f', 'old': 'qc', 'new': 'Q', 'old_step2': 'yc', 'new_step2': 'Q'}]
H = {'f': 'ab qc'}
print('P at H selects for edit 2:', rp.ec.variant(edits[1], H['f'])[2], '| after edit 1:', rp.ec.variant(edits[1], 'xyc')[2])
print('P applies:', rp.p_apply(edits, H))
print('v5.5 rule:', rp.v55(edits, H)[0])

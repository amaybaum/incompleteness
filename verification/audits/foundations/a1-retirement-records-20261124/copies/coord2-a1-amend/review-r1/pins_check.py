# Reviewer: run both pin-table parsers (P's preserve_check.read_pins, S1 authority.read_pin_table) on P's and the proposed PREREG,
# and on the proposed PREREG with placeholders replaced by dummy hex (to see which rows each parser admits).
import sys, re, importlib.util, hashlib
pc_path, tc, prereg_p, prereg_new = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('pc', pc_path); pc = importlib.util.module_from_spec(spec); spec.loader.exec_module(pc)
sys.path.insert(0, tc + '/tools')
from ledger_coverage.engine import authority as au
for name, path in [('P', prereg_p), ('proposed', prereg_new)]:
    b = open(path, 'rb').read(); t = b.decode()
    heads = [(m.start(), m.group(0)) for m in re.finditer(r'^### \d+\.\d+ Record pins\b', t, re.M)]
    print(name, 'last Record pins head:', heads[-1][1], 'count', len(heads))
    a = pc.read_pins(b); s = au.read_pin_table(b)
    print('  preserve_check rows', len(a), sorted(a)); print('  tool rows', len(s), sorted(s)); print('  agree', a == s)
b = open(prereg_new, 'rb').read().decode()
filled = b.replace('`<SHA256>`', '`' + '0'*64 + '`').replace('`<each review record of §32.5>`', '`review-w1-w2-allow-v2.json`')
fb = filled.encode(); a = pc.read_pins(fb); s = au.read_pin_table(fb)
print('filled: preserve_check rows', len(a), sorted(a)); print('filled: tool rows', len(s), sorted(s))
P = pc.read_pins(open(prereg_p,'rb').read())
print('six PINNED digests unchanged vs P (31.31):', all(a[k] == P[k] for k in pc.PINNED))

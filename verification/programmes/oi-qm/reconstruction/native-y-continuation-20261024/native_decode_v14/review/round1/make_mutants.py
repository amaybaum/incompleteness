import sys
from pathlib import Path
base = Path(sys.argv[1]); src = (base/'native_decode_v14/checks.py').read_text()
muts = {
 'm1_contexts': ("if (k[3], k[4]) != (0, 1))", "if (k[3], k[4]) != (1, 0))"),
 'm2_sign_drop_u': ("x = s ^ k[0] ^ k[3]\n            for w in range(64):\n                q[s][j][w]", "x = s ^ k[3]\n            for w in range(64):\n                q[s][j][w]"),
 'm3_solverB_offbyone': ("                for t in range(d + 1):\n                    if (e >> t) & 1:", "                for t in range(d):\n                    if (e >> t) & 1:"),
 'm4_table_corrupt': ("table = [int(ch, 16) for ch in table_hex]", "table = [int(ch, 16) ^ (1 if i % 97 == 0 else 0) for i, ch in enumerate(table_hex)]"),
 'm5_readout_drop_s0': ("if not (d >> q[0][j][w]) & 1 and (d >> q[1][j][w]) & 1:", "if (d >> q[1][j][w]) & 1:"),
}
for name, (old, new) in muts.items():
    assert src.count(old) == 1, name
    d = base/name; d.mkdir(exist_ok=True)
    (d/'checks.py').write_text(src.replace(old, new))
    print(name)

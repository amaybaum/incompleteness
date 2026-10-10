"""Hash-chains ledger.md after the run: entries are the header block and each '## n18:K' section, in order.
h_0 = sha256(header); h_i = sha256(h_{i-1} || entry_i). Writes ledger.chain.md with every h_i and the head."""
import hashlib, re
text = open('ledger.md', encoding='utf-8').read()
parts = re.split(r'(?m)^(?=## n18:)', text)
prev = ''
lines = ['# ledger.md hash chain', '', '| entry | sha256(prev || entry) |', '| --- | --- |']
for i, p in enumerate(parts):
    prev = hashlib.sha256((prev + p).encode('utf-8')).hexdigest()
    name = 'header' if i == 0 else p.splitlines()[0][3:]
    lines.append('| %s | `%s` |' % (name, prev))
lines += ['', 'head: `%s`' % prev, 'ledger.md sha256: `%s`' % hashlib.sha256(text.encode('utf-8')).hexdigest()]
open('ledger.chain.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines))

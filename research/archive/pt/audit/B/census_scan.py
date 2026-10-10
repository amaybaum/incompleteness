"""Coordinator's independent census scan (audit of thread B, B2.6): every landed Prop-valued declaration whose
signature mentions the pair carrier W (W d, W 2, W 3) or a linear equivalence of it. Multi-line signatures are
joined up to ':=' or 'where'. Prints the names, sorted, and the count. Not a substitute for reading: a text scan."""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
hdr = re.compile(r'^\s*(?:noncomputable\s+|private\s+|protected\s+)*(structure|class|def|abbrev|inductive)\s+([A-Za-z0-9_\'.]+)')
found = []
nfiles = 0
for f in sorted(root.rglob('*.lean')):
    if '.lake' in f.parts:
        continue
    nfiles += 1
    lines = f.read_text(encoding='utf-8').splitlines()
    i = 0
    while i < len(lines):
        m = hdr.match(lines[i])
        if m:
            sig = lines[i]
            j = i
            while not re.search(r':=|\bwhere\b', sig) and j + 1 < len(lines) and j - i < 12:
                j += 1
                sig += ' ' + lines[j]
            head = re.split(r':=|\bwhere\b', sig)[0]
            if re.search(r'\bW (d|2|3)\b', head) and re.search(r':\s*Prop\s*$|→\s*Prop\s*$', head.strip()):
                found.append((m.group(2), f.relative_to(root).as_posix(), i + 1))
            i = j + 1
        else:
            i += 1
print(f'files scanned: {nfiles}')
for name, path, ln in sorted(found):
    print(f'{name}  {path}:{ln}')
print(f'count: {len(found)}')

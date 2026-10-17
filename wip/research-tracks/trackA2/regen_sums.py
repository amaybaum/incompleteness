import hashlib, sys, pathlib
d = pathlib.Path(sys.argv[1])
lines = (d / 'SHA256SUMS').read_text(encoding='utf-8').splitlines()
out = []
for ln in lines:
    h, name = ln.split('  ', 1)
    out.append(hashlib.sha256((d / name).read_bytes()).hexdigest() + '  ' + name)
(d / 'SHA256SUMS').write_text('\n'.join(out) + '\n', encoding='utf-8')

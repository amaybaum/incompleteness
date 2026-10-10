import re, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
parts = re.split(r'(?=\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z )', s)
lines = [re.sub(r'^\d{4}-\d\d-\d\dT[\d:.]+Z ', '', p) for p in parts]
open(dst, 'w').write('\n'.join(lines))
oi = [l for l in lines if 'OrbitIsometryGroup' in l]
errs = [l for l in oi if l.startswith('error')]
sorry = [l for l in oi if 'sorryAx' in l]
print(len(lines), 'lines;', len(oi), 'OIG lines;', len(errs), 'errors;', len(sorry), 'sorry-dependent')
for l in sorry: print('  ', re.search(r"'([^']*)'", l).group(1))
for i, l in enumerate(lines):
    if l.startswith('error') and 'OrbitIsometryGroup' in l:
        print('=====', l[:200])
        j = i + 1
        while j < len(lines) and not lines[j].startswith(('error', 'info', 'warning', 'ℹ', '✖', '✔')) and j < i + int(sys.argv[3] if len(sys.argv) > 3 else 40):
            print(lines[j][:500]); j += 1

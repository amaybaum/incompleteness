"""Emit a text file as GitHub Actions notice annotations, readable through the check-runs annotations API.
argv: <file> <title> [max_lines]. Lines are chunked ~25 per annotation (at most 9 annotations), so nothing is
lost to the per-step annotation cap; a final notice states whether the file was truncated."""
import sys
path, title = sys.argv[1], sys.argv[2]
cap = int(sys.argv[3]) if len(sys.argv) > 3 else 225
try:
    lines = open(path, encoding='utf-8', errors='replace').read().rstrip('\n').split('\n')
except OSError as e:
    lines = ['(unreadable: %r)' % e]
enc = lambda s: s.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
shown = lines[:cap]
for i in range(0, len(shown), 25):
    chunk = shown[i:i + 25]
    print('::notice title=%s [%d-%d of %d]::%s' % (title, i + 1, i + len(chunk), len(lines), enc('\n'.join(chunk))))
if len(lines) > cap:
    print('::notice title=%s::TRUNCATED: %d of %d lines shown' % (title, cap, len(lines)))

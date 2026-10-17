"""Print a batch's outcome and every archived file's sha256, from manifest.json, completeness.json and scan.json.

The lines are deterministic, so the archive job's summary and the verify job's can be compared line for line. It
reports; it decides nothing. The archive job's completeness gate and the verify job's verify_batch.py decide.
Usage: python3 -I summarize.py OUT_DIR"""
import json, os, sys

out = sys.argv[1]
load = lambda f: json.load(open(os.path.join(out, f))) if os.path.exists(os.path.join(out, f)) else None
m, c, hits = load('manifest.json'), load('completeness.json'), load('scan.json')
print('## log archive batch')
if m is None:
    print('manifest: missing')
    sys.exit(0)
print('counts: ' + json.dumps(m['counts'], sort_keys=True))
print('rehash_mismatches: %d' % len(m['rehash_mismatches']))
print('completeness: %s' % ('not checked' if c is None else '%s, %d required, %d missing or incomplete' % (
    'complete' if c['complete'] else 'NOT COMPLETE', c['required'], len(c['missing_or_incomplete']))))
for i in (c or {}).get('missing_or_incomplete', []):
    print('MISSING %s %s' % (i['key'], i['state'][:200]))
print('scan: %s' % ('not run' if hits is None else '%d credential-shaped line(s)%s' % (
    len(hits), ': ' + '; '.join('%s %s:%d' % (h['file'], h['member'], h['line']) for h in hits[:50]) if hits else '')))
for e in sorted(m['items'], key=lambda e: e['key']):
    if e['outcome'] == 'archived':
        print('ARCHIVED %s %s %d %s' % (e['key'], e['sha256'], e['bytes'],
                                        '' if not e['key'].startswith('zip:') else 'complete' if e.get('complete') else 'INCOMPLETE'))
    elif e['outcome'] != 'ok':
        print('%s %s %s' % (e['outcome'].upper(), e['key'], e.get('detail', '')[:200]))

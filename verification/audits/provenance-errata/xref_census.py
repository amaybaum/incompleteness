"""Cross-reference census for the provenance errata: every place a commit's tracked text names an errata entry's
cited head, its real head, a prefix of either, or its run id.

For each entry of errata.json and each tracked text file at COMMIT, a hex token is classified by the longest
prefix it shares with the cited and the real head:
  cited-full     the cited 40-hex id
  cited-prefix   9 to 39 hex digits that continue the cited id and not the real head
  shared-prefix  7 or 8 hex digits, a prefix of both; since the cited id names no object, it resolves to the
                 real head
  real-full      the real head's 40-hex id
  real-prefix    9 to 39 hex digits that continue the real head and not the cited id
and a decimal token equal to the run id is `run-id`. Each occurrence carries its file's class, by the off-main
audit's rule (receipt, native-record, legacy-record, mutable) refined for this census:
  frozen           a receipt, native-record or legacy-record file: kept byte-identical
  integrity-bound  a file of the evidence-retention archive, whose manifest pins its bytes and its citations
  errata           this directory
  mutable          any other file
Usage: python3 -I xref_census.py COMMIT [OUT.json]"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      check=True).stdout.strip()
REL = os.path.relpath(HERE, ROOT) + '/'
ARCHIVE = 'verification/audits/evidence-retention/'
SKIP = ('.pdf', '.tex', '.olean', '.png', '.jpg', '.gz', '.zip', '.ilean', '.bundle')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, check=True).stdout


def main(commit, out=None):
    commit = git('rev-parse', commit).decode().strip()
    show = lambda p: git('show', '%s:%s' % (commit, p))
    files = [f for f in git('ls-tree', '-r', '--name-only', commit).decode().split('\n') if f and not f.endswith(SKIP)]
    record_dirs = []
    for r in [f for f in files if f.startswith('verification/receipts/') and f.endswith('.json')]:
        for b in json.loads(show(r)).get('control_plane_blobs', []):
            m = re.search(r'```v3-round\n(.*?)```', show(b['path']).decode('utf-8'), re.S)
            d = m and re.search(r'^record-directory (\S+)', m.group(1), re.M)
            if d:
                record_dirs.append(d.group(1).rstrip('/') + '/')
    legacy = set(json.loads(show('verification/infrastructure/legacy-records.json'))['records'])

    def klass(p):
        if p.startswith(REL):
            return 'errata'
        if p.startswith('verification/receipts/') or any(p.startswith(d) for d in record_dirs) or p in legacy:
            return 'frozen'
        if p.startswith(ARCHIVE):
            return 'integrity-bound'
        return 'mutable'

    entries = json.load(open(os.path.join(HERE, 'errata.json'), encoding='utf-8'))['entries']
    hexre = re.compile(r'(?<![0-9A-Za-z])[0-9a-f]{7,40}(?![0-9A-Za-z])')
    texts = {}
    for f in files:
        b = show(f)
        if b'\0' not in b[:8192]:
            texts[f] = b.decode('utf-8', 'replace').split('\n')
    res = {'commit': commit, 'rule': __doc__.split('\n\n')[0], 'entries': []}
    for e in entries:
        c, h, run = e['cited_head'], e['real_head'], e['run_id']
        runre = re.compile(r'(?<![0-9A-Za-z.])%s(?![0-9A-Za-z])' % run)
        occ = []
        for f, lines in texts.items():
            for i, line in enumerate(lines, 1):
                kinds = []
                for m in hexre.finditer(line):
                    t = m.group(0)
                    if t == c:
                        kinds.append('cited-full')
                    elif t == h:
                        kinds.append('real-full')
                    elif c.startswith(t) and h.startswith(t):
                        kinds.append('shared-prefix')
                    elif c.startswith(t):
                        kinds.append('cited-prefix')
                    elif h.startswith(t):
                        kinds.append('real-prefix')
                if runre.search(line):
                    kinds.append('run-id')
                if kinds:
                    occ.append({'location': '%s:%d' % (f, i), 'class': klass(f), 'kinds': sorted(set(kinds)),
                                'names_a_head': any(k != 'run-id' for k in kinds), 'text': line.strip()[:220]})
        res['entries'].append({'id': e['id'], 'run_id': run, 'occurrences': occ})
    if out:
        json.dump(res, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        open(out, 'a').write('\n')
    for e in res['entries']:
        print('%s run %s: %d occurrence(s)' % (e['id'], e['run_id'], len(e['occurrences'])))
        for o in e['occurrences']:
            print('   %-15s %-34s %s' % (o['class'], ','.join(o['kinds']), o['location']))
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:3]))

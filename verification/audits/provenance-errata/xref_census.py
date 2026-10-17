"""Cross-reference census for the provenance errata: every place a commit's tracked text names an errata entry's
cited id, its real head, a prefix of either, or its run id.

For each entry of errata.json and each tracked text file at COMMIT, `.tex` included, a hex token (7 to 40 hex digits,
bounded by no letter or digit) is classified against the cited id c and the real head h, which share their first s
hex digits (s >= 7):
  cited-full     c itself, as the record cites it
  cited-prefix   a proper prefix of c longer than s digits, so not a prefix of h
  shared-prefix  a prefix of both, of 7 to s digits; since c names no object, it names h where h is present
  real-full      h's 40-hex id
  real-prefix    a proper prefix of h longer than s digits, so not a prefix of c
and a decimal token equal to the run id, not part of a decimal fraction, is `run-id`. A text file is one whose first
8192 bytes hold no NUL byte. Each occurrence carries its file's class, by the off-main audit's rule (receipt,
native-record, legacy-record, mutable) refined for this census:
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


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, check=True).stdout


def main(commit, out=None):
    commit = git('rev-parse', commit).decode().strip()
    show = lambda p: git('show', '%s:%s' % (commit, p))
    files = [f for f in git('ls-tree', '-r', '-z', '--name-only', commit).decode().split('\0') if f]
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
    texts, binary = {}, 0
    for f in files:
        b = show(f)
        if b'\0' in b[:8192]:
            binary += 1
            continue
        texts[f] = b.decode('utf-8', 'replace').split('\n')
    res = {'commit': commit, 'rule': __doc__.split('\n\n')[0], 'files_scanned': len(texts),
           'files_skipped_binary': binary, 'entries': []}
    for e in entries:
        c, h, run = e['cited_head'], e['real_head'], e['run_id']
        s = len(os.path.commonprefix([c, h]))
        runre = re.compile(r'(?<![0-9A-Za-z.])%s(?![0-9A-Za-z]|\.[0-9])' % run)
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
        res['entries'].append({'id': e['id'], 'run_id': run, 'shared_digits': s, 'occurrences': occ})
    if out:
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(res, indent=1, ensure_ascii=False) + '\n')
    print('census at %s: %d text files (%d binary skipped)' % (commit[:8], len(texts), binary))
    for e in res['entries']:
        print('%s run %s: %d occurrence(s)' % (e['id'], e['run_id'], len(e['occurrences'])))
        for o in e['occurrences']:
            print('   %-15s %-34s %s' % (o['class'], ','.join(o['kinds']), o['location']))
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:3]))

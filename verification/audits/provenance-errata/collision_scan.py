"""Prefix-collision scan: cited ids that name no object and share at least their first 7 hex digits with a CI run's
head without being a prefix of it.

A run listing (the host's runs API, as a JSON object keyed by run id, each value carrying `head_sha`) supplies the
heads; the repository supplies the objects. Every tracked file at COMMIT whose first 8192 bytes hold no NUL byte is
read, `.tex` included. A hex token is a maximal run of 7 to 40 lowercase hex digits bounded by no letter or digit.

  same-line  for each line naming a listed run id, each hex token on the line other than the run ids themselves is
             compared with the heads of the runs the line names:
               head, full       the token is a head
               head, abbrev.    the token is a proper prefix of a head
               collision        no head has the token as a prefix, some head shares its first 7 hex digits, and the
                                token names no object in the repository
               near, object     as a collision, but the token names an object
               other            anything else: blobs, trees, other commits, job ids and other numbers on the line
  corpus     every hex token of every scanned line, whether or not the line names a run, that names no object and
             shares its first 7 hex digits with a listed head of which it is not a prefix

`names no object` is git cat-file --batch-check answering `missing`; an ambiguous abbreviation names an object.
A run id is a decimal token of 11 digits, bounded by no letter or digit and not part of a decimal fraction. Such
tokens that are not listed run ids are counted, since a collision with an unlisted run's head is outside what the
listing can find.
With --full-only, a hex token is exactly 40 digits.
Usage: python3 -I collision_scan.py [--full-only] COMMIT LISTING.json [OUT.json]"""
import collections, hashlib, json, re, subprocess, sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      check=True).stdout.strip()
HEXRE = re.compile(r'(?<![0-9A-Za-z])[0-9a-f]{7,40}(?![0-9A-Za-z])')
HEXRE40 = re.compile(r'(?<![0-9A-Za-z])[0-9a-f]{40}(?![0-9A-Za-z])')
DECRE = re.compile(r'(?<![0-9A-Za-z.])[0-9]{11}(?![0-9A-Za-z]|\.[0-9])')


def git(*a, inp=None):
    return subprocess.run(['git', '-C', ROOT, *a], input=inp, capture_output=True, check=True).stdout


def texts_at(commit):
    files = [f for f in git('ls-tree', '-r', '-z', '--name-only', commit).decode().split('\0') if f]
    p = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, skipped = {}, []
    for f in files:
        p.stdin.write(('%s:%s\n' % (commit, f)).encode())
        p.stdin.flush()
        hdr = p.stdout.readline().split()
        n = int(hdr[2])
        b = p.stdout.read(n)
        p.stdout.read(1)
        if hdr[1] != b'blob':
            continue
        if b'\0' in b[:8192]:
            skipped.append(f)
            continue
        out[f] = b.decode('utf-8', 'replace').split('\n')
    p.stdin.close()
    p.wait()
    return out, skipped


def resolve(tokens):
    """token -> True when it names an object (found or ambiguous), False when git answers missing."""
    toks = sorted(tokens)
    if not toks:
        return {}
    q = git('cat-file', '--batch-check', inp=('\n'.join(toks) + '\n').encode()).decode().split('\n')
    res = {}
    for t, line in zip(toks, q):
        res[t] = not line.endswith(' missing')
    return res


def scan(commit, listing, hexre=HEXRE):
    commit = git('rev-parse', commit).decode().strip()
    heads = {str(k): v['head_sha'] for k, v in listing.items()}
    by7 = collections.defaultdict(set)
    for h in heads.values():
        by7[h[:7]].add(h)
    texts, skipped = texts_at(commit)
    alltok = set()
    for lines in texts.values():
        for line in lines:
            alltok.update(hexre.findall(line))
    names = resolve(alltok)
    same = collections.Counter()
    lines_with = 0
    collisions, near = [], []
    corpus = []
    unlisted = set()
    for f in sorted(texts):
        for i, line in enumerate(texts[f], 1):
            toks = hexre.findall(line)
            for d in DECRE.findall(line):
                if d not in heads:
                    unlisted.add(d)
            for t in toks:
                hs = [h for h in by7.get(t[:7], ()) if not h.startswith(t)]
                if hs and not names[t] and not any(h.startswith(t) for h in by7.get(t[:7], ())):
                    corpus.append({'location': '%s:%d' % (f, i), 'token': t, 'heads': sorted(hs)})
            runs = sorted({d for d in DECRE.findall(line) if d in heads})
            if not runs:
                continue
            hl = {heads[r] for r in runs}
            toks = [t for t in toks if t not in runs]
            if not toks:
                continue
            lines_with += 1
            for t in toks:
                if t in hl:
                    same['head, full'] += 1
                elif any(h.startswith(t) for h in hl):
                    same['head, abbrev.'] += 1
                elif any(h[:7] == t[:7] for h in hl):
                    rec = {'location': '%s:%d' % (f, i), 'token': t, 'runs': runs,
                           'heads': sorted(h for h in hl if h[:7] == t[:7]),
                           'shared_digits': max(len(os.path.commonprefix([t, h])) for h in hl if h[:7] == t[:7])}
                    if names[t]:
                        same['near, object'] += 1
                        near.append(rec)
                    else:
                        same['collision'] += 1
                        collisions.append(rec)
                else:
                    same['other'] += 1
    return {
        'commit': commit,
        'listing_runs': len(heads),
        'files_scanned': len(texts),
        'files_skipped_binary': len(skipped),
        'same_line': {'lines': lines_with,
                      'tokens': {k: same.get(k, 0) for k in ('head, full', 'head, abbrev.', 'collision',
                                                             'near, object', 'other')},
                      'collisions': collisions, 'near_object': near},
        'corpus': corpus,
        'unlisted_11_digit_decimals': len(unlisted),
    }


def main(*args):
    full = '--full-only' in args
    commit, listing_path, out = (list(a for a in args if a != '--full-only') + [None])[:3]
    raw = open(listing_path, 'rb').read()
    res = scan(commit, json.loads(raw), HEXRE40 if full else HEXRE)
    res['tokens'] = '40 hex digits' if full else '7 to 40 hex digits'
    res['listing_sha256'] = hashlib.sha256(raw).hexdigest()
    text = json.dumps(res, indent=1, ensure_ascii=False, sort_keys=True) + '\n'
    if out:
        open(out, 'w', encoding='utf-8').write(text)
    s = res['same_line']
    print('collision scan at %s, tokens of %s: %d files (%d binary skipped), listing %d runs' % (
        res['commit'][:8], res['tokens'], res['files_scanned'], res['files_skipped_binary'], res['listing_runs']))
    print('  same line: %d lines; tokens %s' % (s['lines'], json.dumps(s['tokens'])))
    for c in s['collisions']:
        print('    collision %-40s %s (shares %d)' % (c['token'], c['location'], c['shared_digits']))
    print('  corpus: %d token(s) naming no object that collide with a listed head' % len(res['corpus']))
    for c in res['corpus']:
        print('    %-40s %s' % (c['token'], c['location']))
    print('  unlisted 11-digit decimals: %d' % res['unlisted_11_digit_decimals'])
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))

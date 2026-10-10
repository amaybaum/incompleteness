"""Scratch: V3-13's edits to tools/v3_verifier.py, as exact (old, new) pairs. Never landed as is."""

VERIFIER = 'tools/v3_verifier.py'
_D = open('/home/user/incompleteness/tools/v3_verifier.py', encoding='utf-8').read()
# the two blocks removed whole, taken from the file at D between fixed anchors
_RULE = '# ' + '-' * 93 + '\n'
BLOCK_SETTLED = _D[_D.index('SETTLED = (\n'):_D.index("HEX = {'sha1': 40")]
BLOCK_PROJECTION = _D[_D.index(_RULE + '# the projection'):_D.index(_RULE + '# synthetic repositories')]

EDITS = [
# ---- the docstring: the verdict, the modes, no V2 surface
("""This tool implements the protocol-3 specification (verification/infrastructure/v3/architecture.md).
Its --receipts mode is the V3 verdict the release gate runs: it verifies every receipt in a
commit's tree from the commit that last wrote it and exits 1 on any receipt that does not hold. The
projection over the V2 attestation rows, and the shadow report that prints it, gate nothing. V1 and
V2 keep running beside it; they do not decide whether a native round is protocol-valid.
""",
"""This tool implements the protocol-3 specification (verification/infrastructure/v3/architecture.md).
Its --receipts mode is the V3 verdict the release gate runs: it verifies every receipt in a
commit's tree from the commit that last wrote it, requires the round's record directory and seal
record to be unchanged since that commit (G13), and exits 1 on any receipt that does not hold. The
release gate also runs --self-test and --corpus, as regression evidence for this implementation.
"""),
("""    --receipts <C>                 every receipt in C's tree, verified from the commit reachable
                                   from C that last wrote it; exit 1 on any that does not hold
    --project <subject>            the projection of the V2 attestation rows read at <subject>
    --mode shadow --subject <C>    the corpus and the projection, reported; always exits 0
""",
"""    --receipts <C>                 every receipt in C's tree, verified from the commit reachable
                                   from C that last wrote it, with the round's records unchanged
                                   at C since then (G13); exit 1 on any that does not hold
"""),
("""It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.
""",
"""It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed,
of G8-G12 that round V3-5 fixed, and of G13 that round V3-13 fixed, with G12 as V3-13 restated it.
"""),
# ---- constants
("""ATTESTATION_DIR = 'verification/certificates/attestations/'
""", ""),
(BLOCK_SETTLED, ""),
# ---- G12: the legacy namespace is no V3 rule's
("""def foreign(own, path):
    \"\"\"G12: whether `path` is receipt or seal state that is not the round's own, where `own` is
    the round's (receipt path, seal record path or None).\"\"\"
    if isinstance(path, bytes):
        path = path.decode('utf-8', 'replace')
    return (path.startswith('verification/receipts/') and path != own[0]) \\
        or path.startswith('verification/seals/') \\
        or (path.startswith('verification/v3-seals/') and path != own[1])
""",
"""def foreign(own, path):
    \"\"\"G12: whether `path` is receipt or seal state that is not the round's own, where `own` is
    the round's (receipt path, seal record path or None). Pre-V3 state is no V3 rule's: the release
    gate's legacy-records step keeps it immutable.\"\"\"
    if isinstance(path, bytes):
        path = path.decode('utf-8', 'replace')
    return (path.startswith('verification/receipts/') and path != own[0]) \\
        or (path.startswith('verification/v3-seals/') and path != own[1])
"""),
# ---- G13 in --receipts
("""def receipts(repo, c):
    \"\"\"(all hold, lines): every receipt in C's tree, each verified from its receipt commit, the
    commit reachable from C that last wrote it. A path under verification/receipts/ that is not a
    receipt path fails, and so does a receipt whose receipt commit does not hold. UNDECIDABLE, a
    shallow repository included, is never promoted to HOLDS.\"\"\"
""",
"""def records_unchanged(repo, c, q, receipt_path):
    \"\"\"G13 codes for one held receipt: the files under the round's record directory at C are
    exactly those at its receipt commit Q, path for path and blob for blob, and so is the seal
    record the receipt names.\"\"\"
    r = read_receipt_at(repo, q, receipt_path)
    if r is None:
        return ['g13:receipt-unreadable']
    pre = [b['path'] for b in r['control_plane_blobs'] if b['path'].endswith('/preregistration.md')]
    if len(pre) != 1:
        return ['g13:record-directory']
    rdir = pre[0][:-len('preregistration.md')].encode('utf-8')
    at_q = {p: s for p, s in repo.entries(q).items() if p.startswith(rdir)}
    at_c = {p: s for p, s in repo.entries(c).items() if p.startswith(rdir)}
    codes = []
    if at_c != at_q:
        codes.append('g13:record-directory-changed')
    for rec in (r.get('seal') or {}).get('records', []):
        st = repo.state(c, rec['path'].encode('utf-8'))
        if st is None or st[1] != rec['blob']:
            codes.append('g13:seal-record-changed')
    return codes


def receipts(repo, c):
    \"\"\"(all hold, lines): every receipt in C's tree, each verified from its receipt commit, the
    commit reachable from C that last wrote it, and its round's records unchanged at C since that
    commit (G13). A path under verification/receipts/ that is not a receipt path fails, and so does
    a receipt whose receipt commit does not hold. UNDECIDABLE, a shallow repository included, is
    never promoted to HOLDS.\"\"\"
"""),
("""        verdict, codes, _att = verify_round(repo, q)
        lines.append('RECEIPT  %s  Q %s  %s%s' % (name, q, verdict,
                                                   '  ' + ', '.join(codes) if codes else ''))
""",
"""        verdict, codes, _att = verify_round(repo, q)
        if verdict == 'HOLDS':
            try:
                codes = records_unchanged(repo, c, q, p)
            except Undecidable as u:
                verdict, codes = 'UNDECIDABLE', [u.code]
            if codes and verdict == 'HOLDS':
                verdict = 'FAILS'
        lines.append('RECEIPT  %s  Q %s  %s%s' % (name, q, verdict,
                                                   '  ' + ', '.join(codes) if codes else ''))
"""),
# ---- the projection, removed with its last caller
(BLOCK_PROJECTION, ""),
# the corpus runner: a receipts check for repository vectors
("""            elif step['check'] == 'delta':
                r = Repo(workdir)
                got = ('HOLDS', [delta_digest(r.delta(args[0], args[1]), r.fmt())])
""",
"""            elif step['check'] == 'delta':
                r = Repo(workdir)
                got = ('HOLDS', [delta_digest(r.delta(args[0], args[1]), r.fmt())])
            elif step['check'] == 'receipts':
                ok_r, lines = receipts(Repo(workdir), args[0])
                got = ('HOLDS' if ok_r else 'FAILS',
                       sorted({c for ln in lines if ln.startswith('RECEIPT  ')
                               for c in ln.split('  ')[-1].split(', ') if ':' in c}))
"""),
# ---- main: the two modes go
("""USAGE = ('usage: v3_verifier.py --self-test | --corpus [DIR] | --verify-round <Q> | '
         '--reachable <C> <Q> | --receipts <C> | --project <subject> | '
         '--mode shadow --subject <commit>')
""",
"""USAGE = ('usage: v3_verifier.py --self-test | --corpus [DIR] | --verify-round <Q> | '
         '--reachable <C> <Q> | --receipts <C>')
"""),
("""        if argv[:1] == ['--project'] and len(argv) == 2:
            s = check_oid(argv[1])
            print('\\n'.join(project(Repo(cwd), s)))
            return 0
        if argv[:2] == ['--mode', 'shadow'] and len(argv) == 4 and argv[2] == '--subject':
            try:
                s = check_oid(argv[3])
            except Refused as rf:
                print('v3_verifier shadow report: subject refused (%s)' % rf.code)
                return 0
            print('v3_verifier shadow report -- DIAGNOSTIC: this report gates nothing; the V3 '
                  'verdict is --receipts, run by the release gate')
            print('settled rules (verification/infrastructure/v3/architecture.md):')
            for k in SETTLED:
                print('  ' + k)
            ok, lines = run_corpus(DEFAULT_CORPUS, cwd)
            print('\\n'.join(lines))
            print('\\n'.join(project(Repo(cwd), s)))
            print('v3_verifier: shadow report complete (%s)' % (
                'corpus as expected' if ok else 'SHADOW DEFECT: corpus not as expected'))
            return 0
""", ""),
]

p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v314/retire.py'
t = open(p).read()
def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)

# reasons for the removed statements
rep("""        if (chk, line) in amended:
            if cls != 'retain' or amended.pop((chk, line)) != sha:
                raise SystemExit('retire: amendment row %s %d is not a retained census row with '
                                 'its hash' % (chk, line))
            removed.add(n)
            tally['amendment'] += 1
        elif cls in RETIRE or (disp[chk] == 'removed whole'):
            removed.add(n)
            tally['census' if cls in RETIRE else 'structural removed'] += 1""",
"""        if (chk, line) in amended:
            if cls != 'retain' or amended.pop((chk, line)) != sha:
                raise SystemExit('retire: amendment row %s %d is not a retained census row with '
                                 'its hash' % (chk, line))
            removed.add(n)
            why[n] = 'amendment'
            tally['amendment'] += 1
        elif cls in RETIRE or (disp[chk] == 'removed whole'):
            removed.add(n)
            why[n] = 'census' if cls in RETIRE else 'census-structural'
            tally['census' if cls in RETIRE else 'structural removed'] += 1""")
rep("""    removed, keep_texts, retained = set(), collections.Counter(), []
    amended =""", """    removed, keep_texts, retained = set(), collections.Counter(), []
    why = {}
    amended =""")
rep("""    for chk, d in disp.items():
        if d == 'removed whole':
            removed.add(checks[chk])""", """    for chk, d in disp.items():
        if d == 'removed whole':
            removed.add(checks[chk])
            why[checks[chk]] = 'emptied-check'""")
rep("""        dead, live = mark_sweep(src, removed, roots - removed)
        removed |= set(dead)
        removed |= counters(src, removed, predicates, mismatches)
        emptied(src, removed)""", """        dead, live = mark_sweep(src, removed, roots - removed)
        for x in dead:
            why.setdefault(x, 'dead-code')
        removed |= set(dead)
        for x in counters(src, removed, predicates, mismatches):
            why.setdefault(x, 'counter')
            removed.add(x)
        emptied(src, removed)""")

# the tail: everything after validate works on (D line, text) entries, and the ledger is emitted
a = t.index("    ranges = [stmt_range(src, n) for n in removed] + [(k, k) for k in else_lines]\n")
b = t.index("    # the controls\n")
t = t[:a] + """    for x in removed:
        why.setdefault(x, 'emptied-block')
    reason = {}
    for x in sorted(removed, key=lambda x: -(stmt_range(src, x)[1] - stmt_range(src, x)[0])):
        lo, hi = stmt_range(src, x)
        for i in range(lo, hi + 1):
            reason[i] = why[x]
    for k in else_lines:
        reason[k] = 'else-line'
    drop = set(reason)
    for k in attached_comments(src.lines, drop) | orphan_paragraphs(src.lines, drop):
        reason.setdefault(k, 'comment')
    doc = Doc(src.lines, reason)
    doc.comment_paragraphs(comment_only_paragraphs(text0))
    for chk, new in sorted(messages.items()):
        s = Source(doc.text())
        arg = checks_of(s.tree)[chk].value.args[2]
        a, b = arg.lineno, arg.end_lineno
        first, last = s.lines[a - 1], s.lines[b - 1]
        pre, post = first[:arg.col_offset], last[arg.end_col_offset:]
        body = format_message(new, len(pre))
        lines = [pre + body[0]] + body[1:-1] + ([body[-1] + post] if len(body) > 1 else [])
        if len(body) == 1:
            lines = [pre + body[0] + post]
        doc.replace(a - 1, b, lines, 'message')
    doc.comments(headers, {c for c, d in disp.items() if d == 'removed whole'})
    text = doc.text()
    open(outpath, 'w', encoding='utf-8', newline='\\n').write(text)
    if ledger_path:
        with open(ledger_path, 'w', encoding='utf-8', newline='\\n') as fh:
            fh.write(json.dumps(doc.ledger(text0, text), indent=1, sort_keys=True) + '\\n')
""" + t[b:]
rep("""    guard, census_path, outpath = argv[0:3]
    messages = json.load(open(argv[3], encoding='utf-8')) if len(argv) > 3 else {}
    headers = json.load(open(argv[4], encoding='utf-8')) if len(argv) > 4 else {}""",
"""    ledger_path = None
    if '--ledger' in argv:
        k = argv.index('--ledger')
        ledger_path = argv[k + 1]
        argv = argv[:k] + argv[k + 2:]
    guard, census_path, outpath = argv[0:3]
    messages = json.load(open(argv[3], encoding='utf-8')) if len(argv) > 3 else {}
    headers = json.load(open(argv[4], encoding='utf-8')) if len(argv) > 4 else {}""")

# the Doc class, replacing comment_paragraphs() and comments() on strings
a = t.index("def comment_paragraphs(text, at_d):")
b = t.index("def checks_of(tree):")
t = t[:a] + t[b:]
a = t.index("def comments(text, headers, emptied):")
b = t.index("def format_message(msg, indent):")
t = t[:a] + '''class Doc:
    """The guard as a list of entries [D line, text], a D line of None for a replacement line, so
    that every change after the statement removals is recorded against the D lines it replaces.
    Dropped and replaced D lines carry their reason; ledger() emits the changes as D-side splices."""

    def __init__(self, lines, reason):
        self.reason = dict(reason)
        self.e = [[i, l] for i, l in enumerate(lines, 1) if i not in reason]
        self.n = len(lines)

    def text(self):
        return '\\n'.join(l for _i, l in self.e)

    def drop(self, idx, why):
        for k in sorted(idx, reverse=True):
            d = self.e[k][0]
            if d is not None:
                self.reason[d] = why
            del self.e[k]

    def replace(self, a, b, lines, why):
        """Entries a..b-1 (indices into the current text's lines) replaced by `lines`."""
        for d, _l in self.e[a:b]:
            if d is not None:
                self.reason[d] = why
        self.e[a:b] = [[None, l] for l in lines]

    def collapse(self, blank, keep, why):
        run, idx = 0, []
        for k, (_d, l) in enumerate(self.e):
            run = run + 1 if blank(l) else 0
            if run > keep:
                idx.append(k)
        self.drop(idx, why)

    def comment_paragraphs(self, at_d):
        """The paragraphs (blank-line separated) that consist only of comments and did not at D:
        the comments whose code the transformation removed. A paragraph that was comment-only at D
        is kept. Then runs of more than two blank lines are collapsed."""
        idx, para = [], []

        def flush():
            ls = [self.e[k][1] for k in para]
            if para and all(l.strip().startswith('#') for l in ls) and '\\n'.join(ls) not in at_d:
                idx.extend(para)
        for k, (_d, l) in enumerate(self.e):
            if l.strip() == '':
                flush()
                para = []
            else:
                para.append(k)
        flush()
        self.drop(idx, 'comment')
        self.collapse(lambda l: l.strip() == '', 2, 'blank')

    def comments(self, headers, emptied):
        """Each comment paragraph opening with ORPHAN -- the description of a base or seal constant
        that round SI-3 removed and whose comment it left -- deleted; each check's header paragraph,
        `# ---- <tag>: ...`, replaced by its text in `headers`; the drift-control lines in
        DRIFT_LINES deleted; and the header and end marker of every check removed whole deleted
        when `headers` gives no text for it."""
        i, done = 0, set()
        while i < len(self.e):
            j = i
            while j < len(self.e) and self.e[j][1].startswith('#'):
                j += 1
            if j == i:
                i += 1
                continue
            para = [l for _d, l in self.e[i:j]]
            m = re.match(r'# ---- (R7-[A-Z0-9]+)(:| ends\\.)', para[0])
            new = None
            if para[0].startswith(ORPHAN) or (para == [para[0]] and para[0] in DRIFT_LINES):
                new, why = [], 'comment'
            elif m and m.group(2) == ':' and m.group(1) in headers:
                new, why = headers[m.group(1)].split('\\n'), 'header'
                done.add(m.group(1))
            elif m and m.group(1) in emptied:
                new, why = [], 'comment'
            elif para[0] in headers:
                new, why = (headers[para[0]].split('\\n') if headers[para[0]] else []), 'header'
                done.add(para[0])
            if new is None:
                i = j
                continue
            self.replace(i, j, new, why)
            i += len(new)
        if done != set(headers):
            raise SystemExit('retire: header paragraphs not found: %s' % sorted(set(headers) - done))
        self.collapse(lambda l: l == '', 2, 'blank')

    def ledger(self, text0, text):
        """The changes as D-side splices, in D order: each a maximal span of D lines not kept, with
        the replacement lines standing in their place."""
        lines0 = text0.split('\\n')
        out, prev, pending = [], 0, []

        def flush(upto):
            if upto > prev + 1 or pending:
                lo, hi = prev + 1, upto - 1
                old = '\\n'.join(lines0[lo - 1:hi])
                new = '\\n'.join(pending)
                out.append({'d_start': lo, 'd_end': hi,
                            'old_sha256': hashlib.sha256(old.encode('utf-8')).hexdigest(),
                            'new': pending[:],
                            'new_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
                            'reasons': sorted({self.reason[i] for i in range(lo, hi + 1)})})
        for d, l in self.e:
            if d is None:
                pending.append(l)
                continue
            flush(d)
            prev, pending = d, []
        flush(self.n + 1)
        sha = lambda s: hashlib.sha1(b'blob %d\\0' % len(s.encode()) + s.encode()).hexdigest()
        return {'schema': 'v3-14-splice-ledger', 'version': 1,
                'base': {'path': 'verification/lean/edge_rigidity_probe.py', 'blob': sha(text0)},
                'output': {'blob': sha(text)}, 'splices': out}


''' + t[b:]
open(p, 'w').write(t)

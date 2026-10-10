#!/usr/bin/env python3
"""Scratch: execute one V3-9 stage in the repository, reading the frozen builder text, the frozen
section and the frozen sentences back from the preregistration at B. Never landed.

Usage: exec39.py <B> <stage 1|2>   (EXEC_REPO overrides the repository, for rehearsal)
Stage 1 writes tools/v3_receipt.py and runs C1-C4; stage 2 appends the section to AGENTS.md,
replaces the preamble sentence and runs C4, C5. It commits nothing."""
import os
import re
import subprocess
import sys

REPO = os.environ.get('EXEC_REPO', '/home/user/incompleteness')
B, n = sys.argv[1], int(sys.argv[2])
P = 'verification/infrastructure/round-v3-9-operationalization/preregistration.md'
TOOL, ARCH, AG = 'tools/v3_receipt.py', 'verification/infrastructure/v3/architecture.md', 'AGENTS.md'
VARIANTS = {
    'execution delta from D': ("v3.delta_digest(repo.delta(f, e), fmt)", "v3.delta_digest(repo.delta(d, e), fmt)"),
    'landing base is the second parent': ("r['landing'] = {'base': lp[0],", "r['landing'] = {'base': lp[1],"),
    'control-plane blobs in reverse order': ("for p in sorted(cp_files)]", "for p in sorted(cp_files, reverse=True)]"),
    'no withdrawal reason when none exists': ("        if withdrawal is None:\n            absent['withdrawal'] = 'no-execution-commits'\n", ""),
    'seal blob without the object header': ("return h(b'blob %d\\0' % len(data) + data).hexdigest()", "return h(data).hexdigest()"),
    'every attestation on F': ("subj = {'F': f, 'E': e}", "subj = {'F': f, 'E': f}"),
}
ok = True


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True, check=True).stdout.decode()


def report(label, cond):
    global ok
    ok &= bool(cond)
    print('%-5s %s' % ('PASS' if cond else 'FAIL', label))


def run(*a):
    p = subprocess.run([sys.executable] + list(a), cwd=REPO, capture_output=True)
    return p.returncode, p.stdout.decode().rstrip('\n')


def rd(p):
    return open(os.path.join(REPO, p), encoding='utf-8').read()


def wr(p, s):
    open(os.path.join(REPO, p), 'w', encoding='utf-8').write(s)


pre = git('show', '%s:%s' % (B, P))
sec = lambda a, b: pre[pre.index(a):pre.index(b)]
builder = re.findall(r'```text\n(.*?)```', sec('## The builder, FROZEN by semantics', '## The rule and the preamble'), re.S)
texts = re.findall(r'```text\n(.*?)```', sec('## The rule and the preamble, FROZEN as text', '## The controls, FROZEN'), re.S)
assert len(builder) == 1 and len(texts) == 3
v3b = git('rev-parse', '%s:tools/v3_verifier.py' % B).strip()

if n == 1:
    assert not os.path.exists(os.path.join(REPO, TOOL))
    wr(TOOL, builder[0])
    print('stage 1 builder blob %s' % git('hash-object', TOOL).strip())
    rc, out = run(TOOL, '--self-test')
    print('\n'.join('      ' + x for x in out.split('\n')))
    report('C1 self-test exit %d, %r' % (rc, out.split('\n')[-1]), rc == 0 and out.endswith('v3_receipt: self-test OK'))
    procs = {}
    for i, (name, (old, new)) in enumerate(VARIANTS.items()):
        assert builder[0].count(old) == 1, name
        path = os.path.join(REPO, 'tools', 'v3_receipt_variant_%d.py' % i)
        open(path, 'w', encoding='utf-8').write(builder[0].replace(old, new))
        procs[name] = (path, subprocess.Popen([sys.executable, path, '--self-test'], cwd=REPO,
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT))
    for name, (path, p) in procs.items():
        out = p.communicate()[0].decode()
        fails = [x for x in out.split('\n') if x.startswith('FAIL')]
        report('C2 variant %-40s exit %d, %d FAIL line(s)' % (name, p.returncode, len(fails)),
               p.returncode == 1 and 'self-test FAILED' in out and fails)
        os.remove(path)
    rc1, o1 = run(TOOL, '--status', 'complete', '--d', 'HEAD', '--f', 'HEAD')
    rc2, o2 = run(TOOL)
    report('C3 a ref name refused: exit %d, %r' % (rc1, o1), rc1 == 2 and o1 == 'v3_receipt: refused (input:not-an-object-id)')
    report('C3 no arguments: exit %d, usage' % rc2, rc2 == 2 and o2.startswith('usage: v3_receipt.py'))
else:
    ag0 = rd(AG)
    wr(AG, ag0 + texts[0])
    ar0 = rd(ARCH)
    assert ar0.count(texts[1]) == 1
    wr(ARCH, ar0.replace(texts[1], texts[2]))
    ag1, ar1 = rd(AG), rd(ARCH)
    print('stage 2 AGENTS.md blob %s, architecture.md blob %s'
          % (git('hash-object', AG).strip(), git('hash-object', ARCH).strip()))
    report('C5 AGENTS.md is its B bytes followed by the frozen text', ag1 == git('show', '%s:%s' % (B, AG)) + texts[0])
    report('C5 one "## §A.39 " heading and no §A.38', ag1.count('## §A.39 ') == 1 and '§A.38' not in ag1)
    report('C5 architecture.md differs from B by the frozen sentence alone',
           ar1 == git('show', '%s:%s' % (B, ARCH)).replace(texts[1], texts[2]))
    report('C5 no "is not operative"', 'is not operative' not in ar1)

report('C4 tools/v3_verifier.py has its D blob', git('hash-object', 'tools/v3_verifier.py').strip() == v3b)
rc, out = run('tools/v3_verifier.py', '--corpus')
report('C4 %s' % out.split('\n')[-1], rc == 0 and out.split('\n')[-1] == 'CORPUS  135 vector(s), exact and as expected')
rc, out = run('tools/v3_verifier.py', '--self-test')
report('C4 %s' % out, rc == 0)
print('STAGE %d CHECKPOINT %s' % (n, 'PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)

"""Reviewer probe (Layer 2 v8 lock). Constructs NO Context on v8 and computes NO closure.
Only: guard predicates, num_records / record_at (combinatorics), and the pure decide()."""
import sys
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF, l2auth as AUTH, l2config as CFG
v8 = CFG.make_setup(G, 'v8')
res = []
def tryit(name, f):
    try:
        r = f(); res.append((name, 'NOT refused -> %r' % (r,)))
    except PermissionError:
        res.append((name, 'refused'))
    except Exception as e:
        res.append((name, 'error ' + type(e).__name__ + ': ' + str(e)[:60]))
tryit('default: num_records(v8)', lambda: G.num_records(v8))
tryit('authorized_v8=True', lambda: G.num_records(v8, 2, True))
class Sub(G.V8Grant):
    pass
tryit('V8Grant subclass', lambda: G.num_records(v8, 2, Sub('a'*40, 'b'*64, 'c'*64, 'x')))
tryit('duck-typed grant', lambda: G.num_records(v8, 2, type('V8Grant', (), {'key': (3, 6, (0, 0, -3)), 'commit': 'a'*40, 'manifest_sha256': 'b'*64, 'config_sha256': 'c'*64})()))
tryit('V8Grant with bad hex', lambda: G.num_records(v8, 2, G.V8Grant('A'*40, 'b'*64, 'c'*64, 'x')))
# forged well-formed grant constructed directly (no l2auth): combinatorics only
forged = G.V8Grant('0'*40, '0'*64, '0'*64, 'forged')
tryit('FORGED V8Grant (direct construction), num_records only', lambda: G.num_records(v8, 2, forged))
tryit('FORGED V8Grant, record_at(0) only', lambda: G.record_at(v8, 0, forged))
tryit('FORGED RefGrant: s0ref._ref_granted', lambda: REF._ref_granted(REF.RefGrant('0'*40)) or (_ for _ in ()).throw(PermissionError()))
# decide() is pure: fabricated artifact + fabricated owner check against fabricated facts
head = 'f'*40; cd = 'd'*64; cfg = CFG.config_sha256()
art = {'schema': AUTH.SCHEMA, 'scope': AUTH.SCOPE, 'commit': head, 'code_digest': cd, 'config_sha256': cfg,
       'owner': 'amaybaum', 'designation_url': AUTH.REPO_URL + 'issues/1#issuecomment-1', 'designated_at': 'x'}
own = {'schema': AUTH.OWNER_SCHEMA, 'comment_url': art['designation_url'], 'author_login': 'amaybaum',
       'body_sha256': '0'*64, 'body_contains_required_line': True, 'commit': head}
facts = {'head_commit': head, 'tree_clean': True, 'manifest_ok': True, 'code_digest': cd, 'config_sha256': cfg}
res.append(('decide(fabricated artifact, fabricated owner check)', AUTH.decide(art, own, facts)))
for k, v in res:
    print('%-62s %s' % (k, v))

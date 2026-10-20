"""A15: write the 32 members of R's local-relabelling class in F (as in a14 (ii)) to JSON files."""
import itertools, json, os, sys
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
body = cv.Body('eball3'); R = body.reference
gam = [cv.diag([1] + list(s)) for s in itertools.product((1, -1), repeat=3)]
seen = {}
for A, B, C, D in itertools.product(gam, repeat=4):
    M = cv.mat_mul(cv.mat_mul(cv.kron(A, B), R), cv.kron(C, D))
    fr, rt, rc = cv.check_VL(body, M)
    if fr and rt and rc:
        seen.setdefault(json.dumps(cv.to_json_matrix(M)), M)
for i, (k, M) in enumerate(sorted(seen.items())):
    json.dump({'control': 'eball3', 'G': json.loads(k)}, open(os.path.join(sys.argv[2], 'member-%02d.json' % i), 'w'))
print('members written:', len(seen))

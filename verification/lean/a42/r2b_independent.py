"""R2 path B(i): E40 against every realizing triple of SIG, by the independent enumeration in triples.py; controls
C1c, C2, C3 (gauge), C5 (sorted restriction). Reads L41's measurements.json only to compare. Writes r2b.json."""
import json, os, random, time
import triples as T
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
t0 = time.time()
CEN = T.census()
rec = json.load(open(os.path.join(REPO, 'verification', 'programmes', 'oi-qm', 'track-b', 'act-41-index-map-semantics', 'measurements.json')))
def norm(key, k): form, mn, blocks, classes = key; return [form, list(mn), sorted(map(sorted, blocks)), sorted(map(sorted, classes)), k]
mine = sorted(norm(k, len(v)) for k, v in CEN.items())
landed = sorted(json.loads(json.dumps(rec['production']['sig']['relaxed']['census'])))
out = {'partitions': len(CEN), 'triples': sum(len(v) for v in CEN.values())}
out['C1c_equals_L41_relaxed_census'] = mine == landed
out['C1c_equals_L41_strict_census'] = mine == sorted(rec['production']['sig']['strict']['census'])
# C5: the sorted alignment alone
def is_sorted(key, th):
    form, (m, n), blocks, classes = key
    return all(th[a][b] == sorted(classes[b])[a] for a in range(m) for b in range(n))
sorted_parts = sorted(norm(k, 1) for k, v in CEN.items() if any(is_sorted(k, th) for th in v))
out['C5_sorted_partitions'] = len(sorted_parts)
print('census: %d partitions, %d triples; equals L41 relaxed %s strict %s; sorted-alignment partitions %d (%.0fs)' % (
    out['partitions'], out['triples'], out['C1c_equals_L41_relaxed_census'], out['C1c_equals_L41_strict_census'], out['C5_sorted_partitions'], time.time() - t0), flush=True)
# C3: the identities annihilate gauge, for every triple
GG = T.gauge_generators()
out['C3_gauge_annihilated'] = all(T.member(Gm, k, th) for k, v in CEN.items() for th in v for Gm in GG)
# SIG consistency: the identities hold for 0
Z = [[0] * 16 for _ in range(16)]
out['zero_in_all'] = all(T.member(Z, k, th) for k, v in CEN.items() for th in v)
def pieces():
    def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
    P = piece(lambda a, b, c, d: int(b == 0 and c == 0)); Q = piece(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
    Tt = piece(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
    A = piece(lambda a, b, c, d: int(a % 2 == 1 and b == 3 and c % 2 == 1)); B = piece(lambda a, b, c, d: int(a == 2 and d == 1))
    C = piece(lambda a, b, c, d: int((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))))
    return P, Q, Tt, A, B, C
P, Q, Tt, A, B, C = pieces()
def lin(coefs, Ms): return [[sum(c * M[i][j] for c, M in zip(coefs, Ms)) for j in range(16)] for i in range(16)]
E40 = lin([-1, 1, -1], [P, Q, Tt]); EE = lin([1, 1, 1], [A, B, C])
rng = random.Random(4242)
al = [rng.randint(-3, 3) for _ in range(16)]; be = [rng.randint(-3, 3) for _ in range(16)]
E40g = [[E40[i][j] + al[i] + be[j] for j in range(16)] for i in range(16)]
def members(E): return sorted(norm(k, 0)[:4] + [list(map(list, th))] for k, v in CEN.items() for th in v if T.member(E, k, th))
tests = {'E40': E40, 'E40_gauge': E40g, 'act38_E': EE, 'A': A, 'B': B, 'C': C, 'P': P, 'Q': Q, 'T': Tt,
         '-P+Q': lin([-1, 1], [P, Q]), '-P-T': lin([-1, -1], [P, Tt]), 'Q-T': lin([1, -1], [Q, Tt])}
out['members'] = {}
for nm, E in tests.items():
    mm = members(E)
    out['members'][nm] = {'count': len(mm), 'partitions': sorted(set(json.dumps(x[:4]) for x in mm)), 'triples': mm if len(mm) <= 40 else len(mm)}
    print('  %-10s member of %4d triples in %2d partition structures' % (nm, len(mm), len(out['members'][nm]['partitions'])), flush=True)
print('C3 gauge annihilated: %s; zero in all: %s (%.0fs)' % (out['C3_gauge_annihilated'], out['zero_in_all'], time.time() - t0))
json.dump(out, open(os.path.join(HERE, 'r2b.json'), 'w'), indent=1, sort_keys=True)

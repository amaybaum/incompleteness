"""Reviewer mutants of checks.py. Usage: python3 -I -B my_mutants.py <checks.py> <abs work dir> [names]"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
M = {
 'R1_region_shrunk': ("REGION = sorted(ball(RHO))", "REGION = sorted(ball(RHO-1))"),
 'R2_Y_consistently_wrong': ("        self.Y = tuple(comp(q8[l], 1) for l in lanes)",
                             "        self.Y = tuple(comp(q8[l], 0) for l in lanes)"),
 'R3_target_sign_flipped': ("        self.t1, self.t0 = targets(self.s)", "        self.t1, self.t0 = targets(1-self.s)"),
 'R4_law_one_orientation': ("        if c1 == self.t1 and c0 == self.t0:\n            return 1",
                            "        if False:\n            return 1"),
 'R5_inject_A_permuted_native': ("            fam, row = run_family(seed)",
                                 "            fam, row = run_family(seed, ((4, 0, 0), 12))"),
 'R6_inject_A_xor_VB_native': ("            fam, row = run_family(seed)",
                               "            fam, row = run_family(seed, ((4, 0, 0), 12))"),
 'R7_law_checks_block_sizes_only': ("        if c0 == self.t1 and c1 == self.t0:\n            return 0\n        if c1 == self.t1 and c0 == self.t0:\n            return 1",
                                    "        if sum(c0) == sum(self.t1) and sum(c1) == sum(self.t0):\n            return 0\n        if sum(c1) == sum(self.t1) and sum(c0) == sum(self.t0):\n            return 1"),
 'R8_tend_shrunk': ("TEND = NS+1+TAU ", "TEND = NS+1+TAU-8 "),
}
EXTRA = {
 'R5_inject_A_permuted_native': ("            self.vals[inject] = tuple(2*a for a in self.A)",
                                 "            self.vals[inject] = tuple(2*a for a in self.A_bad)"),
 'R6_inject_A_xor_VB_native': ("            self.vals[inject] = tuple(2*a for a in self.A)",
                               "            self.vals[inject] = tuple(2*(self.A[l] ^ comp(self.V[l], 1)) for l in lanes)"),
}
src, work = sys.argv[1], os.path.abspath(sys.argv[2])
names = sys.argv[3:] or sorted(M)
text = open(src).read()
def run(name):
    t = text
    for old, new in [M[name]] + ([EXTRA[name]] if name in EXTRA else []):
        assert t.count(old) == 1, (name, old)
        t = t.replace(old, new)
    p = os.path.join(work, name + '.py'); open(p, 'w').write(t)
    pr = subprocess.run([sys.executable, '-I', '-B', p], cwd=work, capture_output=True, text=True, timeout=1500)
    try:
        o = json.loads(pr.stdout)
        return name, pr.returncode, o.get('verdict'), o.get('required_controls', {}).get('failed'), o.get('common_stream_closed_admissible_R'), o.get('scaled_parameters', {}).get('read_site_times')
    except ValueError:
        return name, pr.returncode, 'UNPARSED', pr.stderr.strip().splitlines()[-1:], None, None
with ThreadPoolExecutor(3) as ex:
    for r in ex.map(run, names):
        print(json.dumps(r))

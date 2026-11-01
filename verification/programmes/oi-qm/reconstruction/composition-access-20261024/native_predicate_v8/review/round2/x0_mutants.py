"""Reviewer x0 mutants. Usage: python3 -I -B x0_mutants.py <checks.py> <abs work dir>"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
M = {
 'X1_region_shifted_same_size': ("REGION = sorted(ball(RHO))", "REGION = sorted(add(x, (1, 0, 0)) for x in ball(RHO))"),
 'X2_slices_shifted_same_count': ("SLICES = tuple(range(-1, TEND+1))", "SLICES = tuple(range(0, TEND+2))"),
 'X3_site_list_reordered': ("SITE_TIMES = [(x, t) for t in SLICES for x in REGION]", "SITE_TIMES = [(x, t) for x in REGION for t in SLICES]"),
 'X4_one_site_swapped': ("REGION = sorted(ball(RHO))", "REGION = sorted(ball(RHO))[:-1] + [(5, 0, 0)]"),
 'X5_ball_itself_shifted': ("                out.append((x, y, z))", "                out.append((x+1, y, z))"),
 'X6_n_seven': ("NS = 6 ", "NS = 7 "),
}
src, work = sys.argv[1], os.path.abspath(sys.argv[2]); text = open(src).read()
def run(name):
    old, new = M[name]; assert text.count(old) == 1, name
    p = os.path.join(work, name + '.py'); open(p, 'w').write(text.replace(old, new))
    pr = subprocess.run([sys.executable, '-I', '-B', p], cwd=work, capture_output=True, text=True, timeout=1500)
    try:
        o = json.loads(pr.stdout); return name, pr.returncode, o.get('verdict'), o.get('required_controls', {}).get('failed')
    except ValueError:
        return name, pr.returncode, 'UNPARSED', pr.stderr.strip().splitlines()[-1:]
with ThreadPoolExecutor(2) as ex:
    for r in ex.map(run, sorted(M)): print(json.dumps(r), flush=True)

"""Reviewer targeted mutants for a97c852a (run one per invocation, in parallel).
Usage: python3 -I -B mut6.py <a2_memory_v8 dir> <work dir> <name>
Copies checks.py, PLAN.md and the pinned v7 result.json into <work>/<name>/, applies the edits, runs -I -B,
prints exit code and first output line."""
import os, subprocess, sys
SRC, WORK, NAME = sys.argv[1:4]
MUT = {
    # owner's scenario, reported result edited directly: every power-rule half depth one block early
    'T1_reported_depths_edited': [("    fam, encl = family()\n",
        "    fam, encl = family()\n    for _key, _e in fam.items():\n        if '_k' in _key:\n"
        "            _k = int(_key.split('_k')[1])\n            _e['post_plan']['power_rule_T_above_half_for_h_at_least'] -= _k\n")],
    # consistent wrong preregistered depth: one block early in the rule and in its own minimality check
    'T2_prereg_depth_one_block_early': [
        ("                n_half = floor_q(1 / c_low) + 1 ", "                n_half = floor_q(1 / c_low) "),
        ("check(n_half * c_low > 1 and (n_half - 1) * c_low <= 1,", "check((n_half + 1) * c_low > 1 and n_half * c_low <= 1,")],
    # label remap: member (B,k) reported with the block law of k+1 (k<16)
    'T3_label_remap_k_plus_1': [("            law = block_law(B, k)\n", "            law = block_law(B, k + 1 if k < 16 else k)\n")],
}
src = open(os.path.join(SRC, 'checks.py')).read()
for o, n in MUT[NAME]:
    assert src.count(o) == 1, (NAME, o)
    src = src.replace(o, n)
base = os.path.join(WORK, NAME)
os.makedirs(os.path.join(base, 'a2_memory_v8'), exist_ok=True)
os.makedirs(os.path.join(base, 'a2_depth_v7'), exist_ok=True)
open(os.path.join(base, 'a2_memory_v8', 'checks.py'), 'w').write(src)
open(os.path.join(base, 'a2_memory_v8', 'PLAN.md'), 'wb').write(open(os.path.join(SRC, 'PLAN.md'), 'rb').read())
open(os.path.join(base, 'a2_depth_v7', 'result.json'), 'wb').write(open(os.path.join(SRC, '..', 'a2_depth_v7', 'result.json'), 'rb').read())
run = os.path.join(base, 'run'); os.makedirs(run, exist_ok=True)
p = subprocess.run([sys.executable, '-I', '-B', os.path.join(base, 'a2_memory_v8', 'checks.py')], capture_output=True, text=True, cwd=run)
first = p.stdout.splitlines()[0][:140] if p.stdout else 'STDERR:' + (p.stderr.strip().splitlines() or [''])[-1][:120]
print(f'{NAME}: exit {p.returncode}; {first}')

"""Fill result.draft.md -> result.md from the final module (stage2.lean) and runs.txt.
usage: python3 fill_result.py   (needs stage2.lean from stage33.py, runs.txt with the design-evidence sentence)"""
import re, subprocess, importlib.util
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a33/'
spec = importlib.util.spec_from_file_location('c33', S + 'controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
src = open(S + 'stage2.lean', encoding='utf-8').read()
code = C.strip_comments(src)
th = C.theorems(code)
n = len(th)
NUM = {349: 'three hundred and forty-nine', 350: 'three hundred and fifty', 351: 'three hundred and fifty-one',
       352: 'three hundred and fifty-two', 353: 'three hundred and fifty-three', 354: 'three hundred and fifty-four'}
nk = len(re.findall(r'(?m)^theorem (\S+) :(?:(?!^theorem ).)*?decide \+kernel', code, re.S))
# audit of off-list helpers, per theorem (same rule as stage33.py)
F = 'd5126a3d61f78ab38e3cca0ee7f744ce645d7196'
files = subprocess.run(['git', 'ls-tree', '-r', '--name-only', F, 'verification/lean-mathlib/OIBridge/'], capture_output=True, text=True, cwd='/home/user/incompleteness').stdout.split()
names = {}
for p in files:
    s = subprocess.run(['git', 'show', F + ':' + p], capture_output=True, text=True, cwd='/home/user/incompleteness').stdout
    for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+|noncomputable[ \t]+)*(?:theorem|lemma|def|abbrev)[ \t]+(\S+)', s):
        names.setdefault(m.group(1), p.split('/')[-1][:-5])
PROV = set("""FibreGram GramPhaseEquiv RealizableGram AdmissibleDilationAt sh1_necessity gramPhaseEquiv_refl gramPhaseEquiv_symm gramPhaseEquiv_trans realizable_of_gramPhaseEquiv hadamard_z_admissible mixedTriple mixedTriple_gauge mixedTriple_star dist_eq_norm_toLp coord_le_dist fourier_dist_le geo1_class_invariant geo1_equiv_of_zero_single iso1_single_carrier iso2_classes_single mixedTriple_relabel2 mixedTriple_transpose fibreGram_unique relabel2_isometry conj_isometry relabel2_realizable featureVec normalizedSet IsSurjIsometryOn featureVec_gauge gramPhaseEquiv_of_featureVec_eq featureVec_mem_normalizedSet relabelled_fourier_mem_normalizedSet normalizedSet_eq_iUnion bridge_of_tuple_isometry tuple_isometry_of_bridge eqOn_affineSpan_of_agree exists_affineIsometryEquiv_of_isSurjIsometryOn a26_0_affine_extension a26_1_circle_count rigid_motion_of_tuple_isometry a32_shared_fourier_star a32_shared_coord_inj a32_shared_fourier_inj a32_shared_pair a32_shared_classify a32_control_overlap a32_shared_exists a32_shared_isometry a32_shared_separation a32_shared_relabel a32_shared_star_mul_self a32_not_rigid""".split())
ORBIT = {'OrbitGeometryRigidity', 'OrbitGeometryIsometries', 'OrbitGeometrySelector', 'OrbitIsometryClassification', 'OrbitLawGaps', 'OrbitLawRigidityTwisted', 'GramTrajectorySelection', 'TwoSidedGauge'}
by_helper = {}
for b in re.split(r'(?m)^(?=theorem )', code):
    m = re.match(r'theorem (\S+)', b)
    if not m:
        continue
    proof = b[b.index(':= by') + 5:] if ':= by' in b else b
    for ident in set(re.findall(r"(?<![A-Za-z0-9_'.])[A-Za-z_][A-Za-z0-9_']*", proof)):
        if ident in names and names[ident] in ORBIT and ident not in PROV and not ident.startswith('a33_'):
            by_helper.setdefault((ident, names[ident]), []).append(m.group(1))
for (h, f), ts in by_helper.items():
    assert all(t.startswith('a33_shared_') for t in ts), (h, ts)
rows = ['| `%s` | `%s.lean` | %s |' % (h, f, ', '.join('`%s`' % t for t in ts)) for (h, f), ts in sorted(by_helper.items())]
runs = open(S + 'runs.txt', encoding='utf-8').read().strip()
t = open(S + 'result.draft.md', encoding='utf-8').read()
rep = {'@@NTHM@@': NUM[n], '@@NKERNEL@@': str(nk), '@@DEVIATIONS@@': '\n'.join(rows), '@@RUNS@@': runs}
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'result.md', 'w', encoding='utf-8').write(t)
print('theorems', n, 'kernel-decided', nk, 'deviations', len(by_helper))
print('note findings', C.note_ok(t, 'A33-CLASSIFIED'))

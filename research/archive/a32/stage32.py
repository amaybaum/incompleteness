"""Write A32's execution stages into the protocol worktree. Usage: stage32.py <worktree> <1|2|3|note>"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WT, STAGE = sys.argv[1], sys.argv[2]
RDIR = 'verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/'
MODULE = 'verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
D = 'd61c6c5409db201e3c25abbf3ec0ecce1f530684'


def at_d(p):
    return subprocess.run(['git', '-C', WT, 'show', '%s:%s' % (D, p)], capture_output=True,
                          check=True).stdout.decode('utf-8')


def put(p, text):
    with open(os.path.join(WT, p), 'w', encoding='utf-8', newline='') as f:
        f.write(text)


if STAGE == '1':
    shutil.copyfile(os.path.join(HERE, 'controls.py'), os.path.join(WT, RDIR, 'controls.py'))
    shutil.copyfile(os.path.join(HERE, 'mod32-s1.lean'), os.path.join(WT, MODULE))
    root = at_d(ROOT)
    a = 'import OIBridge.StrictNaturalLift\n'
    assert root.count(a) == 1
    put(ROOT, root.replace(a, a + 'import OIBridge.OrbitIsometryClassification\n', 1))
elif STAGE == '2':
    shutil.copyfile(os.path.join(HERE, 'mod32-s2.lean'), os.path.join(WT, MODULE))
elif STAGE == '3':
    cen = json.loads(at_d('verification/lean-manuscript-census.json'))
    cen['families'].append({
        'name': 'the surjective isometries of the normalized single-carrier space and the four-shape family (act 32, Track B)',
        'modules': ['OrbitIsometryClassification'],
        'status': 'kernel-only',
        'manuscript': [],
        'note': open(os.path.join(HERE, 'census32.txt'), encoding='utf-8').read().strip(),
    })
    put('verification/lean-manuscript-census.json', json.dumps(cen, indent=2, ensure_ascii=False) + '\n')
    shutil.copyfile(os.path.join(HERE, 'road-notrigid.md'), os.path.join(WT, 'verification/ROADMAP.md'))
    shutil.copyfile(os.path.join(HERE, 'guard-retired32.py'),
                    os.path.join(WT, 'verification/lean/edge_rigidity_probe.py'))
elif STAGE == 'note':
    shutil.copyfile(os.path.join(HERE, 'result.md'), os.path.join(WT, RDIR, 'result.md'))
else:
    sys.exit('bad stage')

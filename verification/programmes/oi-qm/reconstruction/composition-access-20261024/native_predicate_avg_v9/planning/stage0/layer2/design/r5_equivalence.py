"""Layer-2 design evidence: the Layer-2 engine changes (the grant-based guard; the memoized G
eligibility) leave the control suite's results unchanged. Runs the frozen design-evidence suite
stage0/code-r5/s0controls.py --quick (read-only, toy instances) and compares its JSON with the
Layer-2 suite's quick result retained in toyrun/preflight.json. Every control must agree except
the refusal check, which Layer 2 extends (36 attempts to 46); there the Layer-2 result must
refuse every attempt. Usage: python3 -I -B r5_equivalence.py <stage0/code-r5> <toyrun dir>.
Prints JSON; exit 0 iff so."""
import json
import os
import subprocess
import sys

r5, toyrun = sys.argv[1], sys.argv[2]
p = subprocess.run([sys.executable, '-I', '-B', os.path.join(r5, 's0controls.py'), '--quick'],
                   capture_output=True, text=True)
a = json.loads(p.stdout)
with open(os.path.join(toyrun, 'preflight.json')) as f:
    b = json.load(f)['s0controls_result']
diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
ref = b.get('V8_refused', {})
ok = p.returncode == 0 and diff == ['V8_refused'] and ref.get('refused') == ref.get('of') == 46 and ref.get('pass')
print(json.dumps({'code_r5_exit': p.returncode, 'keys_compared': len(set(a) | set(b)), 'differing_keys': diff,
                  'code_r5_refusal': a.get('V8_refused'), 'layer2_refusal': ref, 'pass': bool(ok)},
                 indent=1, sort_keys=True))
sys.exit(0 if ok else 2)

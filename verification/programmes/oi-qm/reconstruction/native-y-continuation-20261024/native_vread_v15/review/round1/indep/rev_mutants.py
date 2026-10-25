"""Reviewer mutants of native_vread_v15/checks.py (beyond the author's 21).

Usage: python3 -I -B rev_mutants.py <checks.py> <source-root> <workdir>
Each mutant replaces one exact span (must occur exactly once unless count given).
Reports exit code, first VOID line or verdict outcome + free-key lists.
"""
import json
import subprocess
import sys
from pathlib import Path

CHECKS, ROOT, WORK = (Path(a) for a in sys.argv[1:4])
SRC = CHECKS.read_text()

M = [
    # K1
    ('K1_v14_pin', "'3172e7d013c09cdcdf638a7ace68e0eff98bb3cd0411e8666b76a8226ad59034'",
     "'3172e7d013c09cdcdf638a7ace68e0eff98bb3cd0411e8666b76a8226ad59035'"),
    ('K1_table_truncated', "table = route['q10_table_hex']", "table = route['q10_table_hex'][:-1]"),
    ('K1_source_count', "need(len(sources) == 1479", "need(len(sources) == 1478"),
    # K2: cone formula shifted to previous-slice semantics (wrong for current cells)
    ('K2_cone_shift', 'return d <= t and (t-d) % 2 == 0', 'return d <= t-1 and (t-1-d) % 2 == 0'),
    ('K2_cone_wider', 'return d <= t and (t-d) % 2 == 0', 'return d <= t+2 and (t-d) % 2 == 0'),
    ('K2_counter_threshold', 'if len(reached) >= 2 and', 'if len(reached) >= 7 and'),
    # K3: H not bijective in BOTH evaluators (scalar h and packed rule)
    ('K3_H_nonbijective_both', 'return (old[0] ^ b, old[1] ^ d, old[2] ^ (a ^ (b & d)))',
     'return (old[0] ^ b, old[1] ^ d, old[2] ^ (b & d))'),
    # K3: key planted in previous slice in both evaluators
    ('K3_key_prev_slice_both', None, None),
    # K3 countercontrol out of cone
    ('K3_counter_out_of_cone', 'off = (-n, 0, -1)', 'off = (-n, 0, -3)'),
    # K3: other-neighbour independence check made vacuous AND key that leaks into a second
    # neighbour: off-axis key replaces the axial one (should fail 'other neighbors independent')
    ('K3_key_offaxis_all', 'key = tuple((n+1)*v for v in e)',
     'key = tuple((n+1)*v for v in e) if e[2] == 0 else (1, 0, n*e[2])'),
    # K4 null with non-uniform key (7 of 8 values)
    ('K4_nonuniform_key', 'laws = [Counter(table[o, kv] for kv in range(8)) for o in range(8)]',
     'laws = [Counter(table[o, kv] for kv in range(7)) for o in range(8)]'),
    # K4 positive with operand out of V's cone but inside... operand in previous slice => no effect
    ('K4_operand_far', 'operand = (0, 0, n+1)', 'operand = (0, 0, n+2)'),
    # K5: inflate q9 ready ball by 2 -> pins F8 and the -x/+y keys
    ('K5_q9_ball_inflated', 'balls += [((0, S, 68+k), R+k) for k in range(10)]',
     'balls += [((0, S, 68+k), R+k+(2 if k == 9 else 0)) for k in range(10)]'),
    # K5: E moved off its declared position in the classifier inventory
    ('K5_E_moved', "'E': (0, -78, 78), 'N'", "'E': (0, -78, 79), 'N'"),
    # K5: q10 extension radius too small
    ('K5_q10_radius', 'return balls, balls+[(Q10, L+1)]', 'return balls, balls+[(Q10, L-1)]'),
    # K6: old q9 fixed payload codes changed
    ('K6_q9_codes', 'zip((x, u, my, mr, a, b, 4, 5, 7)', 'zip((x, u, my, mr, a, b, 4, 5, 6)'),
    # K6: shell parity flipped
    ('K6_shell_parity', 'active = (sum(cell)-sum(Q9)-(L+2)) % 2 == 0', 'active = (sum(cell)-sum(Q9)-(L+1)) % 2 == 0'),
    # K6: s definition wrong (x^u instead of x^u^a)
    ('K6_s_definition', "        s = x ^ u ^ a\n        need(old_q9", "        s = x ^ u\n        need(old_q9"),
    # K6: E,N ready-ball avoidance check against wrong E (adjacent cell in q10 extension? use E inside ball)
    ('K6_EN_avoid', 'for pos in ((0, -78, 78), (0, S, S+156)):', 'for pos in ((0, -78, 78), (0, S, S+80)):'),
    # G: uniform-table check with non-bijective H applied only in the table check
    ('G_table_nonbijective', 'Vs = Counter(p ^ h(c ^ m ^ rest) for m in range(8))',
     'Vs = Counter(p ^ (h(c ^ m ^ rest) & 6) for m in range(8))'),
    # Verdict-change mutants (not controls): a missing ready region pinning the -x and +y keys
    ('VERDICT_missing_region_pins_keys', "balls += [((-48*L, 0, 0), L)]\n    need(len(balls) == 24",
     "balls += [((-48*L, 0, 0), L)]\n    balls += [((-(L+2), S, 77), 0), ((0, S+L+2, 77), 0)]\n    need(len(balls) == 26"),
    ('VERDICT_missing_region_pins_minus_x', "balls += [((-48*L, 0, 0), L)]\n    need(len(balls) == 24",
     "balls += [((-48*L, 0, 0), L)]\n    balls += [((-(L+2), S, 77), 0)]\n    need(len(balls) == 25"),
    ('VERDICT_receiver_near_keys', 'RECEIVERS = [p for p, _, _ in PORTS]+[(-48*L, 0, 0)]',
     'RECEIVERS = [p for p, _, _ in PORTS]+[(-48*L, 0, 0), (-(L+2), S, 0), (0, S+L+2, 0)]'),
    # Countercontrol strengthened: require it for every n in SHA-256 worlds (does it still hold?)
    ('STRENGTHEN_counter_every_n', "need(any(counter['sha256']), 'K3 countercontrol: off-axis cell must change two neighbors')",
     "need(any(counter['sha256']), 'K3 countercontrol: off-axis cell must change two neighbors')\n"
     "    need(all(any(counter['sha256'][3*i:3*i+3]) for i in range(4)), 'K3 countercontrol per n')"),
    ('STRENGTHEN_counter_polynomial_only', "need(any(counter['sha256'])", "need(any(counter['polynomial'])"),
]


def apply(name, old, new):
    if name == 'K3_key_prev_slice_both':
        s = SRC
        for o, n in (('        if t == 0 and p in planted:\n            return planted[p]',
                      '        if t == -1 and p in planted:\n            return planted[p]'),
                     ('        if t == 0 and p in assignment:\n            return assignment[p]',
                      '        if t == -1 and p in assignment:\n            return assignment[p]')):
            if s.count(o) != 1:
                return None, 'span count %d' % s.count(o)
            s = s.replace(o, n)
        return s, None
    if SRC.count(old) != 1:
        return None, 'span count %d' % SRC.count(old)
    return SRC.replace(old, new), None


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    lines = []
    for name, old, new in M:
        text, err = apply(name, old, new)
        if err:
            lines.append('%-36s SPAN-ERROR %s' % (name, err))
            continue
        path = WORK/(name+'.py')
        path.write_text(text)
        done = subprocess.run([sys.executable, '-I', '-B', str(path), '--source-root', str(ROOT)],
                              capture_output=True, text=True)
        out = done.stdout
        if done.returncode == 0:
            v = json.loads(out)['verdict']
            desc = '%s free=%s public=%s' % (v['outcome'], v['free_keys_unseen_by_public_records'],
                                            v['free_keys_reaching_a_public_port_by_L+2'])
        else:
            desc = out.splitlines()[0] if out else ('stderr: '+done.stderr.strip().splitlines()[-1])
        lines.append('%-36s exit=%d %s' % (name, done.returncode, desc))
    print('\n'.join(lines))


main()

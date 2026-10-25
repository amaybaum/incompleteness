"""Mutation runs for native_vread_v15/checks.py.

Each mutant replaces one exact text span of the checker (the span must occur
exactly once), runs the mutant with the interpreter flags of the replay, and
counts as caught only if it exits with status 2 and prints VOID with the
label prefix of the control it targets. The unmodified checker runs first
and must reproduce result.json byte for byte; otherwise no mutant runs.

Usage: python3 -I -B mutants/make_mutants.py [--source-root DIR]
Output is deterministic and is retained as mutants/OUTPUT.txt.
"""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile


MUTANTS = [
    ('K1_table_digest', "TABLE_SHA256 = 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'",
     "TABLE_SHA256 = 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cd'",
     'K1 recomputed table digest'),
    ('K1_review_pin', "'73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e4'",
     "'73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e5'",
     'K1 input pin'),
    ('K2_drop_parity', 'return d <= t and (t-d) % 2 == 0', 'return d <= t',
     'K2 keys are exactly the axial cells'),
    ('K2_counter_vacuous', 'dist(c, origin) == n+1 and sum(1 for v in c if v) > 1',
     'dist(c, origin) == n+9 and sum(1 for v in c if v) > 1',
     'K2 countercontrol'),
    ('K3_packed_drops_old_local', 'return (old[0] ^ b, old[1] ^ d, old[2] ^ (a ^ (b & d)))',
     'return (b, d, a ^ (b & d))', 'K3'),
    ('K3_offaxis_key', 'key = tuple((n+1)*v for v in e)',
     'key = tuple((n+1)*v for v in e) if e != (1, 0, 0) else (n, 1, 0)', 'K3'),
    ('K3_scalar_H', 'return (b << 2) | (d << 1) | (a ^ (b & d))',
     'return (b << 2) | (d << 1) | (a ^ b)', 'K3 scalar and packed evaluators agree'),
    ('K3_counter_axial', 'off = (-n, 0, -1)', 'off = (-(n+1), 0, 0)',
     'K3 countercontrol: off-axis cell must change two neighbors'),
    ('K4_operand_out_of_cone', 'operand = (0, 0, n+1)', 'operand = (0, 0, n+3)',
     'K4 positive'),
    ('K4_key_out_of_cone', 'key = (-(n+1), 0, 0)', 'key = (-(n+3), 0, 0)', 'K4 null'),
    ('K5_no_q10_extension', 'return balls, balls+[(Q10, L+1)]', 'return balls, balls',
     'K5 anchor q10 ready ball'),
    ('K5_no_banks', 'if dl < t <= 2*L:', 'if dl < t <= dl:', 'K5 anchor port-0 bank'),
    ('K5_F8_pinned', "'F10_pin': (-(L+1), S, 78),", "'F10_pin': (-(L+1), S, 78), 'F8': (-(L+1), S, 76),",
     'K5 anchor F8 free'),
    ('K6_q9_row_order', 'zip((x, u, my, mr, a, b, 4, 5, 7)', 'zip((x, u, my, mr, b, a, 4, 5, 7)',
     'K6 old q9'),
    ('K5_receiver_threshold', "return nearest, text, slack <= 2", "return nearest, text, slack <= -L",
     'K5 anchor receiver reached'),
    ('K6_law', 'FEWEST_LAW = (1, 5, 1, 4, 1, 5)', 'FEWEST_LAW = (1, 5, 1, 4, 1, 4)',
     'K6 v14 fewest-seed law'),
    ('K6_f9_cell_shifted', 'f9 = add(Q9, (-1, 0, 0), L+2)', 'f9 = add(Q9, (-1, 0, 0), L+3)',
     'K6 Native A f9 public slack 79'),
    ('K6_shell_bound', 'min(2*L, t0+slack)', 'min(t0, t0+slack)', 'K6 shell bank count'),
    ('K6_v14_index', 'counts[240-1] == 1456', 'counts[240] == 1456', 'K6 v14 q10.A law count'),
    ('G_uniform_table', 'for m in range(8))', 'for m in range(4))',
     'G uniform key gives uniform V on table rows'),
    ('K1_route_checks_pin', "'8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856'",
     "'8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed857'", 'K1 input pin'),
    ('K2_propagation_drops_old_local', 'acc = set(dep(t-2, p))', 'acc = set()', 'K2 propagated'),
    ('K3_counter_per_n', 'off = (-n, 0, -1)', 'off = (-n, 0, -1) if n != 2 else (-(n+1), 0, 0)',
     'K3 countercontrol: off-axis cell must change two neighbors for every n'),
    ('K3_previous_key_shifted', 'pkey = tuple(n*v for v in e)', 'pkey = tuple((n-1)*v for v in e)',
     'K3 V is a permutation of the previous-slice key'),
    ('K5_E_moved', "'E': (0, -78, 78), 'N'", "'E': (0, -78, 79), 'N'",
     'K5 anchor E,N are their declared sources'),
    ('K5_ready_list_retyped', 'balls += [((T, 0, 0), T), ((-T, 0, 0), T)',
     'balls += [((T, 0, 0), T+1), ((-T, 0, 0), T)', 'K5 ready list equals native_route_v13 geometry()'),
    ('K5_previous_radius', 'if dist(cell, center) <= radius-1:', 'if dist(cell, center) <= radius:',
     'K5 anchor previous N position free'),
    ('D1_formula', 'pd ^ sa ^ (sb & sd)', 'pd ^ sa ^ (sa & sd)', 'D1 V field formulas'),
]


def run(script, root, optimized):
    flags = ['-I', '-B']+(['-O'] if optimized else [])
    done = subprocess.run([sys.executable]+flags+[str(script), '--source-root', str(root)],
                          capture_output=True, text=True)
    return done.returncode, done.stdout


def main():
    here = Path(__file__).resolve().parent
    package = here.parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=package.parent)
    args = parser.parse_args()
    root = args.source_root.resolve()
    source = (package/'checks.py').read_text()
    expected = (package/'result.json').read_text()
    lines = []
    for optimized in (False, True):
        code, out = run(package/'checks.py', root, optimized)
        if code != 0 or out != expected:
            print('VOID: unmodified checker does not reproduce result.json (-O=%s)' % optimized)
            sys.exit(2)
    lines.append('unmodified checker: exit 0, result.json reproduced (normal and -O)')
    caught = 0
    with tempfile.TemporaryDirectory() as work:
        for name, old, new, label in MUTANTS:
            if source.count(old) != 1:
                print('VOID: mutant %s span occurs %d times' % (name, source.count(old)))
                sys.exit(2)
            script = Path(work)/('%s.py' % name)
            script.write_text(source.replace(old, new))
            code, out = run(script, root, False)
            first = out.splitlines()[0] if out else ''
            ok = code == 2 and first.startswith('VOID: '+label)
            caught += ok
            lines.append('%-28s exit=%d %-8s %s' % (name, code, 'CAUGHT' if ok else 'MISSED', first))
    lines.append('caught %d of %d mutants' % (caught, len(MUTANTS)))
    print('\n'.join(lines))
    if caught != len(MUTANTS):
        sys.exit(2)


if __name__ == '__main__':
    main()

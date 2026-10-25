"""Exact native-pool/abstract-X-predicate assembly; no author engine imports."""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


TR = tuple(product((0, 1), repeat=3))
TABLE_H = (0, 2, 4, 7, 1, 3, 5, 6)
THRESHOLDS = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def tv(p, q):
    return sum((abs(p.get(k, F())-q.get(k, F())) for k in p.keys() | q.keys()), F())/2


def pool_fields(q8, q10):
    return q8[1], q10[2], q10[1], q8[0]+2*q8[2]+4*q10[0]


def abstract_flag(s, q8, q10, thresholds=THRESHOLDS):
    y, r, z, k = pool_fields(q8, q10)
    return k < thresholds[y ^ s, r ^ s]


def mu_x(s):
    return {(s, s ^ a, s ^ b, z): F(n, 20)
            for (a, b), n in THRESHOLDS.items() if n
            for z in (0, 1)}


def normalized_pool_law(s, thresholds=THRESHOLDS, stale=None, reused_r=None, shared_z=False):
    count = Counter()
    accepted = 0
    for q8, q10 in product(TR, repeat=2):
        y, r, z, k = pool_fields(q8, q10)
        if reused_r is not None:
            r = reused_r
        if shared_z:
            z = y ^ s
        selector = s if stale is None else stale
        if k < thresholds[y ^ selector, r ^ selector]:
            count[s, y, r, z] += 1
            accepted += 1
    return {j: F(n, accepted) for j, n in count.items()}, F(accepted, 64)


def pool_checks():
    laws = []
    all_raw_failures = 0
    for s in (0, 1):
        got, rate = normalized_pool_law(s)
        require(got == mu_x(s) and rate == F(5, 16), 'whole 12-state X target from pool')
        # Exact full accepted physical phases are retained, not assigned a
        # replacement output on failure. The private K fields remain workspace.
        accepted_phases = [(q8, q10) for q8, q10 in product(TR, repeat=2)
                           if abstract_flag(s, q8, q10)]
        failure_phases = [(q8, q10) for q8, q10 in product(TR, repeat=2)
                          if not abstract_flag(s, q8, q10)]
        require(len(accepted_phases) == 20 and len(failure_phases) == 44,
                'all pool phases partitioned')
        require(len(set(accepted_phases+failure_phases)) == 64,
                'all accepted/rejected raw cells retained')
        all_raw_failures += len(failure_phases)
        z_marginal = {z: sum(p for j, p in got.items() if j[3] == z) for z in (0, 1)}
        require(z_marginal == {0: F(1, 2), 1: F(1, 2)}, 'Z fair')
        require(all(got[s, y, r, 0] == got[s, y, r, 1]
                    for _, y, r, _ in got), 'Z jointly independent')
        laws.append({'s': s, 'success_probability': str(rate),
                     'failure_probability': '11/16',
                     'target_cells': [{'j': j, 'probability': str(p)} for j, p in sorted(got.items())]})
    mutants = {}
    swapped = {(0, 0): 5, (0, 1): 0, (1, 0): 1, (1, 1): 4}
    bad01 = {(0, 0): 5, (0, 1): 1, (1, 0): 4, (1, 1): 1}
    for s in (0, 1):
        target = mu_x(s)
        bad, rate = normalized_pool_law(s, thresholds=swapped)
        require(rate == F(5, 16) and tv(bad, target) == F(3, 10), 'swapped4:1 rejected')
        mutants['swapped_plane_weights_tv'] = str(tv(bad, target))
        bad, rate = normalized_pool_law(s, thresholds=bad01)
        require(rate == F(11, 32) and any((j[1] ^ s, j[2] ^ s) == (0, 1) for j in bad),
                'forbidden plane and changed rate rejected')
        mutants['forbidden01_success_probability'] = str(rate)
        bad, rate = normalized_pool_law(s, stale=1 ^ s)
        require(rate == F(5, 16) and tv(bad, target) == F(4, 5), 'stale old Y rejected')
        mutants['stale_y_in_place_of_x_tv'] = str(tv(bad, target))
        bad, rate = normalized_pool_law(s, shared_z=True)
        require(tv(bad, target) == F(1, 2), 'joint shared-Z defect')
        require(sum(p for j, p in bad.items() if j[3] == 0) == F(1, 2),
                'shared-Z mutant still has fair marginal')
        mutants['shared_z_joint_tv_with_fair_marginal'] = str(tv(bad, target))
        for r in (s, 1 ^ s):
            bad, rate = normalized_pool_law(s, reused_r=r)
            expected = F(1, 10) if r == s else F(9, 10)
            require(tv(bad, target) == expected, 'used public R is not fresh')
            mutants['used_r_equal_x_tv' if r == s else 'used_r_opposite_x_tv'] = str(expected)
    return laws, mutants, all_raw_failures


def old_kernel(table, x, u, my, mr, a, b):
    index = 0
    for value, size in zip((x, u, my, mr, a, b, 4, 5, 7), (2, 2, 2, 2, 2, 2, 8, 8, 8)):
        index = index*size+value
    return TR[int(table[index], 16)]


def old_native_flags(program):
    flags = {}
    for a, b, k in product((0, 1), (0, 1), range(8)):
        seed = a+2*b+4*k
        register = 0
        for constant, terms in program[:2684]:
            control = constant
            for bit, mask in terms:
                if seed >> bit & 1:
                    control ^= mask
            register = TABLE_H[register ^ control]
        raw = TABLE_H[TABLE_H[register]]
        require(raw in (0, 2), 'old native whole herald phase')
        flags[a, b, k] = raw // 2
        require(bool(flags[a, b, k]) == (k < {(0, 0): 5, (0, 1): 0,
                                                             (1, 0): 3, (1, 1): 2}[a, b]),
                'old native word implements retained threshold')
    return flags


def complete_assembly(root):
    table = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    require(len(table) == 32768, 'complete native old table')
    word = json.loads((root/'parallel_v3/direct_reset/herald.json').read_text())['program']
    flags = old_native_flags(word)
    worlds = blocks = raw_failure_phases = 0
    examples = []
    for x, u, my, mr in product((0, 1), repeat=4):
        y = x ^ u
        accepted = Counter()
        failed = Counter()
        old_terminal_failures = Counter()
        old_record = Counter()
        physical_all = Counter()
        physical_accepted = Counter()
        physical_rejected = Counter()
        false_resurrections = 0
        for a, b, k, old_z in product((0, 1), (0, 1), range(8), (0, 1)):
            old_raw = old_kernel(table, x, u, my, mr, a, b)
            old_g = flags[a, b, k]
            s = old_raw[1]
            for q8, q10 in product(TR, repeat=2):
                worlds += 1
                yn, rn, zn, kk = pool_fields(q8, q10)
                new_g = abstract_flag(s, q8, q10)
                offered = bool(old_g and new_g)
                j = (s, yn, rn, zn)
                # All physical branches retain actual previous q9, previous
                # old Z and both fresh current whole cells. None is erased.
                physical = (old_raw, (0, 0, old_z), (0, old_g, 0), q8, q10)
                physical_all[physical] += 1
                if offered:
                    physical_accepted[physical] += 1
                else:
                    physical_rejected[physical] += 1
                if not old_g:
                    old_terminal_failures[old_raw] += 1
                    false_resurrections += new_g
                    require(not offered, 'earlier failure cannot be resurrected')
                else:
                    old_record[old_raw] += 1
                    if new_g:
                        accepted[old_raw, j] += 1
                    else:
                        failed[old_raw] += 1
                        raw_failure_phases += 1
        denominator = 64*64
        require(sum(accepted.values()) == 400, 'joint old/new success count')
        require(sum(failed.values()) == 880, 'new failure after valid old success')
        require(sum(old_terminal_failures.values()) == 2816, 'all old failures retained')
        require(sum(old_record.values()) == 1280, 'old success branch count')
        require(sum(accepted.values())+sum(failed.values())+sum(old_terminal_failures.values())
                == denominator, 'all finite worlds retained')
        require(physical_accepted+physical_rejected == physical_all and
                sum(physical_rejected.values()) == 3696,
                'complete physical phase measures partition including old failures')
        require(F(false_resurrections, denominator) == F(55, 256),
                'resurrection mutant has positive false-offer mass')
        for raw, count in old_record.items():
            s = raw[1]
            for j, probability in mu_x(s).items():
                require(F(accepted[raw, j], denominator) == F(count, denominator)*F(5, 16)*probability,
                        'whole old raw record and outgoing carrier factor jointly')
            require(F(failed[raw], denominator) == F(count, denominator)*F(11, 16),
                    'failure law conditional on whole old raw record')
        expected_old = {(0, y, y): F(1, 2), (0, 1 ^ y, y): F(3, 10),
                        (0, 1 ^ y, 1 ^ y): F(1, 5)}
        require({raw: F(n, 1280) for raw, n in old_record.items()} == expected_old,
                'actual post-Y whole-port old record')
        if my == mr == 0:
            examples.append({'x': x, 'u': u, 'old_y': y,
                             'accepted_worlds': sum(accepted.values()),
                             'new_failure_after_old_success_worlds': sum(failed.values()),
                             'old_terminal_failure_worlds': sum(old_terminal_failures.values()),
                             'full_rejected_physical_measure_sha256': hashlib.sha256(
                                 json.dumps(sorted(physical_rejected.items()), separators=(',', ':')).encode()).hexdigest()})
        blocks += 1
    return {'finite_worlds': worlds, 'old_input_history_blocks': blocks,
            'new_rejected_physical_worlds_after_old_success': raw_failure_phases,
            'joint_success_probability_per_block': '25/256',
            'new_failure_after_old_success_probability_per_block': '55/256',
            'old_terminal_failure_probability_per_block': '11/16',
            'whole_old_raw_record_factorization': True,
            'resurrection_mutant_false_offer_probability': '55/256',
            'examples': examples}


def main():
    ap = argparse.ArgumentParser()
    default = Path(__file__).resolve().parent.parent
    if not (default/'parallel_v3').exists():
        default = default/'checkpoint_v10'
    ap.add_argument('--source-root', type=Path, default=default)
    ap.add_argument('--native-author-root', type=Path, default=Path(__file__).resolve().parent.parent/'native_v11')
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    pins = json.loads((here/'PROVENANCE.json').read_text())
    for name, digest in pins['native_pool_source_files'].items():
        require(hashlib.sha256((args.native_author_root/name).read_bytes()).hexdigest() == digest,
                'native first-front pool source '+name)
    for name, digest in pins['old_instrument_files'].items():
        require(hashlib.sha256((args.source_root/name).read_bytes()).hexdigest() == digest,
                'old native instrument source '+name)
    actual_pool = json.loads((args.native_author_root/'result.json').read_text())
    require(actual_pool['conditional_law']['next_q8_q10_joint_cell_probability'] == '1/64',
            'retained native pool law')
    laws, mutants, rejected = pool_checks()
    result = {'schema': 'oi.native-pool-abstract-X-target.v11',
              'native_source_revision': pins['native_source_revision'],
              'pool_bits': 6, 'abstract_thresholds_00_01_10_11': [5, 0, 4, 1],
              'conditional_X_target_laws': laws,
              'retained_pool_rejection_phases_both_X_signs': rejected,
              'joint_assembly': complete_assembly(args.source_root),
              'countercontrols': mutants,
              'verdict': {'native_resource': 'conditional six-bit fresh local pool',
                          'abstract_X_predicate': 'full finite target law passes',
                          'native_X_predicate': 'not_constructed',
                          'old_X_delivery_to_native_gate': 'open',
                          'delayed_full_public_history_joint_law': 'open',
                          'reusable_native_instrument': 'not_constructed'}}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

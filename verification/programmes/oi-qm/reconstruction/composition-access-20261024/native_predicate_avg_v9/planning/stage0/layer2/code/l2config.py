"""NP-AVG-1 Stage 0 Layer 2: configuration constants (certificate item 1).

Every constant the production run depends on is here, as integers, strings and lists only.
config_sha256() is the SHA-256 of the canonical JSON of CONFIG; the Layer-2 manifest
records it, and l2cert verifies it at start-up before anything is computed.

Profiles: 'v8' is the configuration of the enumeration, which is not authorized; 'toy' is
the design-evidence class (3D, n = 2, ball(1), last slice 6, port (0, 0, -2): 1,400 records,
488 C4v orbits). Sampling rates are 1-in-R; the toy profile samples every record so that
every in-run gate is exercised on the design evidence.
"""
import hashlib
import json

CONFIG = {
    'schema': 'np-avg-1/stage0/layer2/config/1',
    'layer1': {
        'plan': 'stage0/r5/STAGE0-PLAN-r5.md',
        'plan_sha256': '1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e',
        'freeze_commit': 'f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966',
    },
    'profiles': {
        'v8': {
            'setup': {'dim': 3, 'n': 6, 'rho': 4, 'tlast': 23, 'port': [0, 0, -3],
                      'sources': [[-8, 0, 0], [-7, 0, -1], [-7, 0, 1]]},
            'k': 2,
            'requires_authorization': True,
            'sampling': {'C7': 1000, 'C8_orbits': 100, 'C11i': 1000, 'C17': 1000, 'C18': 1000},
            'shards': 32,
        },
        'toy': {
            'setup': {'dim': 3, 'n': 2, 'rho': 1, 'tlast': 6, 'port': [0, 0, -2],
                      'sources': [[-4, 0, 0], [-3, 0, -1], [-3, 0, 1]]},
            'k': 2,
            'requires_authorization': False,
            'sampling': {'C7': 1, 'C8_orbits': 1, 'C11i': 1, 'C17': 1, 'C18': 1},
            'shards': 4,
        },
    },
    'v8_key': [3, 6, [0, 0, -3]],
    'rules': {
        'L3prime': {'far': True, 'offaxis': 'none', 'wrong_far': False, 'far_cone': True, 'delta': 0,
                    'swap': False, 'keep_odd': False, 'stop_after': None, 'nopar': False, 'symblind': False,
                    'blind_dir': None, 'ignore_fixed_dir': None, 'decide_blind_dir': None,
                    'decide_ignore_fixed_dir': None, 'blind_only_type': None, 'blind_only_G': False,
                    'decide_inelig_free_dir': None},
        'L3': 'L3prime with far = False',
    },
    'depth_ranges': {'A_F': [0, 15], 'A_B': [0, 8], 'G_F': [0, 23], 'G_B': [0, 0]},
    'sampling_salt': 'np-avg-1/stage0/layer2/sample/1',
    'C7_shared_tip_scope': 'initial_context',
    'C7_brute_limit': 8,
    'S_max_bits': 27,
    'budget': {
        'runner_hours': 24,
        'max_shards': 32,
        'timeout_minutes': {'dryrun': 10, 'preflight': 30, 's1a': 40, 'shard': 40, 'merge': 20},
        'launch_if_estimate_at_most_numerator': 1,
        'launch_if_estimate_at_most_denominator': 2,
        'gate_overhead_factor': 2,
    },
    'group': 'C4v: the stabilizer in O_h of {Reg, q9, Phi site set, port}, fixing q8 and q10',
    'expected': {
        'v8': {
            'items': 3225, 'pairs': 5160000, 'records': 5163225,
            'single_orbits': 875, 'pair_orbits': 815175, 'orbits': 816050,
            'O_h_order': 48, 'group_order': 8, 'region_sites': 129,
            'port_even_samples': [1, 3, 5],
            'B8_even_cells': 833,
            'C6_base': {'A': {'retained': [], 'survivor': False},
                        'G': {'retained': [[[0, 0, -3], 1], [[0, 0, -3], 3], [[0, 0, -3], 5]],
                              'survivor': False}},
            'C6_q9_9': {'A': {'retained': [], 'survivor': False, 'in_clear': [[[0, 0, 0], 6], [[0, 0, 0], 8]]},
                        'G': {'retained': [[[0, 0, -3], 1], [[0, 0, -3], 3], [[0, 0, -3], 5],
                                           [[0, 0, 0], 0], [[0, 0, 0], 2], [[0, 0, 0], 4]],
                              'survivor': False, 'truncated': [[[0, 0, 0], 0], [[0, 0, 0], 2], [[0, 0, 0], 4]]}},
        },
        'toy': {'records': 1400, 'orbits': 488, 'group_order': 8, 'reported_counts': 54},
        'controls_full': {'C1_perturbations': 301640, 'C2_tips': 541, 'C2_offaxis_contrasts': 39,
                          'C11i_tables': 16831, 'C11iii_planted_sets': 96, 'C11ii_retained_sets': 24,
                          'refusal_attempts': 46, 'S6_subsets': 22, 'S6_target_law_classes': 0},
    },
    'rule_T': {
        'inputs': 'L_A: non-fixed quantities of the L3prime global bound under A whose cone contains a Phi cell; '
                  'L_G: quantities of the L3prime global bound under G with a seed tip whose cone contains a '
                  'source cell',
        'zero_text': 'No record whose items lie in Reg x {-1, ..., 23}, of any size, has a linked survivor (PO4). '
                     'The report states this geometric fact only; law failure beyond k <= 2 is not claimed, since '
                     'PO8 covers at most two Phi triples in clear.',
        'positive_text': 'S1b (the minimal self-supporting record search, m <= 4, restricted to the global bound) '
                         'is put to the owner as a new preregistration. S1c is taken up only if S1b\'s own '
                         'preregistered rule calls for it.',
        'not_evaluated_text': 'S1a is VOID, MISMATCH or INCOMPLETE: rule T is not evaluated and S1b and S1c are '
                              'not proposed.',
        'wording_status': 'provisional: retained pending owner confirmation (owner decision 2026-10-26)',
    },
    'labels': ['VOID', 'MISMATCH', 'INCOMPLETE', 'BASE_RESIDUE', 'COLLAPSE_ALL', 'RESIDUE_UNLINKED', 'RESIDUE'],
    'mismatch_controls': ['C6_execution', 'C9', 'C10ii', 'C11ii', 'C12'],
    'coverage_limits': [
        'k <= 2 stream items; v8\'s region and slices; the scaled control.',
        'One port; no later reads, unless S3 extends them.',
        'Conventions A and G, with the declared frame.',
        'L3prime and L3 only; survivors are not shown to be informative.',
        'No law computed, apart from the S6 proof-check on Phi\'s reference structure.',
        'Nothing at actual L; no A1/A2 statement; no claim about OI beyond the class.',
    ],
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def config_sha256():
    return hashlib.sha256(canonical(CONFIG).encode()).hexdigest()


def profile(name):
    return CONFIG['profiles'][name]


def make_setup(G, name):
    s = profile(name)['setup']
    return G.Setup(s['dim'], s['n'], s['rho'], s['tlast'], tuple(s['port']),
                   tuple(tuple(x) for x in s['sources']))


if __name__ == '__main__':
    print(config_sha256())

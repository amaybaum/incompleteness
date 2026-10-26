"""NP-AVG-1 Stage 0 Layer 2: configuration constants (certificate item 1).

Every constant the production run depends on is here, as integers, strings and lists only.
config_sha256() is the SHA-256 of the canonical JSON of CONFIG; the Layer-2 manifest
records it, and l2cert verifies it at start-up before anything is computed.

Profiles: 'v8' is the configuration of the enumeration, which is not authorized; 'toy' is
the design-evidence class (3D, n = 2, ball(1), last slice 6, port (0, 0, -2): 1,400 records,
488 C4v orbits). Sampling rates are 1-in-R. The toy profile samples every representative for
the gates sampled by representative (C8, C11 (i), C17, C18), so that each is exercised on the
design evidence; C7's two record-index samples (erratum E1, item E1-F3) use the v8 rates on
the toy profile as well, so that the toy run's per-set C7 coverage can be compared with the
erratum's independent computation (E1-check part J).

Owner rulings (erratum E1, in effect, amendments/E1-LAYER1-ERRATUM.md) are filled in below.
Three owner decisions remain open placeholders: kappa (the launch margin, S7), the Lemma G-D
reference form (E1 section 9) and O1 (E_G as a fifth C7 set, E1 section 9). l2cert.startup
refuses the v8 profile while any placeholder remains. No value for kappa is set anywhere.
"""
import hashlib
import json

# An owner ruling that does not yet exist. Every production entry point refuses the v8 profile
# while any value in the configuration equals it (l2cert.startup, certificate item 1).
OWNER = 'OWNER-PLACEHOLDER'

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
            'sampling': {'C8_orbits': 100, 'C11i': 1000, 'C17': 1000, 'C18': 1000},
            'C7_samples': {'H100': {'stream': 'C7_H100', 'rate': 100}, 'H1000': {'stream': 'C7_H1000', 'rate': 1000}},
            'shards': 32,
            'C7_scope': 'E1-F3',
        },
        'toy': {
            'setup': {'dim': 3, 'n': 2, 'rho': 1, 'tlast': 6, 'port': [0, 0, -2],
                      'sources': [[-4, 0, 0], [-3, 0, -1], [-3, 0, 1]]},
            'k': 2,
            'requires_authorization': False,
            'sampling': {'C8_orbits': 1, 'C11i': 1, 'C17': 1, 'C18': 1},
            'C7_samples': {'H100': {'stream': 'C7_H100', 'rate': 100}, 'H1000': {'stream': 'C7_H1000', 'rate': 1000}},
            'shards': 4,
            'C7_scope': 'E1-F3',
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
    'C7_brute_limit': 8,
    # E1-F3: C7 runs per record on sets 1-4; every record in scope is closed directly by the
    # production engine and by the full s0ref reference (the default the owner kept, E1 section 9),
    # and its carried result is compared with its direct closure. The Lemma G-D reference form is
    # not implemented: it is a non-executing proposal pending the owner (owner_rulings.G_D).
    'C7': {'sets': ['1_Surv', '2_set2', '3_I_and_H100', '4_H1000'],
           'set2_A': 'T_A: the computed closure has a shared near tip (T_A within Surv_A, proved)',
           'set2_G': '(T_G and Surv_G) union F_G; F_G = {R : In(R) has a shared near tip}, closure-free',
           'reference_form': 'full_s0ref',
           'per_record': True},
    'S_max_bits': 27,
    'budget': {
        'runner_hours': 24,
        'max_shards': 32,
        'timeout_minutes': {'dryrun': 10, 'preflight': 30, 's1a': 40, 'shard': 40, 'merge': 20},
        # kappa: the launch margin, an owner-set resource constant (not a Layer-1 requirement),
        # fixed with its basis before the complete estimate is computed. Launch iff
        # kappa * total <= budget and kappa * each job's estimate <= that job's timeout.
        'kappa': OWNER,
        'gate_overhead_factor': 2,
        # survivor representatives per shard whose gates and residue detail are computed; beyond
        # it the shard records survivor_cap_exceeded and the merge labels the run INCOMPLETE.
        # Layer-2 value, bounding the survivor-gate term of the estimate; the owner may revise it.
        # Basis: on the planted calibration a survivor orbit costs about 14 runner-seconds per run
        # (up to 8 members x (4 closures + 8 reference gates) at the largest context), so 10 per
        # shard bounds the term at about 9,000 runner-seconds with the -O copy.
        'survivor_cap_per_shard': 10,
        # fixed job costs used by the estimate (seconds), with their basis
        'preflight_seconds': 300,
        'preflight_basis': 'design-r5 full suite 134 s, S6 18 s, symcheck 20 s, plus self-test and C11 mutants',
        'merge_seconds': 300,
        'merge_basis': 'not measured on v8: 32 shard files and the class-key union; a stated allowance per run',
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
        'toy': {'records': 1400, 'orbits': 488, 'group_order': 8, 'reported_counts': 58},
        'controls_full': {'C1_perturbations': 301640, 'C2_tips': 541, 'C2_offaxis_contrasts': 39,
                          'C11i_tables': 16831, 'C11iii_planted_sets': 96, 'C11ii_retained_sets': 24,
                          'refusal_attempts': 46, 'S6_subsets': 22, 'S6_target_law_classes': 0},
    },
    'owner_rulings': {
        'source': 'stage0/amendments/E1-LAYER1-ERRATUM.md (in effect), amaybaum 2026-10-26',
        'T1': {'ruling': 'L3prime bound; L3 values reported only (E1-T1, "Approve erratum")',
               'question': 'rule T bound: L3prime or L3'},
        'T2': {'ruling': 'sigma, S1a\'s own diagnostic status, cases 1-4 of E1-T2 with case 2 (d); rule T evaluated iff '
                         'sigma = OK; sigma never overrides the run label ("Give S1a its own diagnostic status, not an '
                         'overriding success label"; "Add it")',
               'question': 'S1a status'},
        'T5': {'ruling': 'L_G counts quantities with a seed tip whose own cone contains a source cell (E1-T5)',
               'question': 'L_G wording'},
        'T6': {'ruling': 'geometric fact only, approved with qualification (E1-T6)',
               'question': 'standing of rule T\'s L_A = L_G = 0 consequence'},
        'F3': {'ruling': 'E1-F3: sets 1-4, every record index, per record, full s0ref reference',
               'question': 'C7 scope'},
        'F6': {'ruling': '58 counts (E1-F6: four added survivor cross-tabulations)',
               'question': 'C8 list (54) or 4-count erratum (58)'},
        'kappa': {'ruling': OWNER, 'question': 'launch margin and budget (S7)', 'layer2_reading': 'none: no default',
                  'owner_answer': 'Decide later'},
        'G_D': {'ruling': OWNER, 'question': 'Lemma G-D reference form in C7 (E1 section 9)',
                'layer2_reading': 'not implemented; the full s0ref closure is the only reference form',
                'owner_answer': 'Conditionally approved; non-executing until the owner confirms the proof'},
        'O1': {'ruling': OWNER, 'question': 'E_G as a fifth C7 set under G (E1 section 9; optional)',
               'layer2_reading': 'not adopted: E_G is not a check set'},
    },
    'accepted_readings': {
        'source': 'review/LAYER2-REVIEW.md (a63db7ba), section 5',
        'F1': 'BASE_RESIDUE is reachable only after the MISMATCH-resolution amendment L1 section 5 requires',
        'F4': 'residual support as defined in LAYER2-PLAN.md section 4, reported only',
        'F5': 'masking equivalence by equal even-class contexts (L1 text); code-r5 reading reported',
        'F7': 'C12 per-record clause checked on the universe (PO-L2-9)',
        'F8': 'C11 (i), C17 and C18 sampled 1 in 1,000 (L1 N6: Layer-2 configuration constants)',
        'F10': 'the engine implementing the frozen rule; guard and memo edits leave geometry and closure unchanged',
        'F11': 'C6 execution instances, C10 (ii) and C12 on v8 run in the authorized pre-flight',
    },
    'rule_T': {
        'inputs': 'L_A: non-fixed quantities of ret_L3prime_A(U) whose cone contains a Phi cell; L_G: quantities of '
                  'ret_L3prime_G(U) with a seed tip whose own cone contains a source cell (E1-T1, E1-T5)',
        'bound_rule': 'L3prime',
        'zero_text': 'No record whose items lie in Reg \u00d7 {\u22121, \u2026, 23}, of any size, has a linked '
                     'survivor under the specified closure (L3\u2032, the declared conventions and frame). This is a '
                     'geometric property of that closure. It is not a probabilistic result, an empirical observation, '
                     'or an independent theorem about the full model, and no law statement is made beyond k \u2264 2.',
        'positive_text': 'S1b (the minimal self-supporting record search, m <= 4, restricted to the global bound) '
                         'is put to the owner as a new preregistration. S1c is taken up only if S1b\'s own '
                         'preregistered rule calls for it.',
        'not_evaluated_text': 'S1a is VOID, MISMATCH or INCOMPLETE: rule T is not evaluated and S1b and S1c are '
                              'not proposed.',
        'beside_failed_label_text': 'Rule T was evaluated (sigma = OK) in a run whose label is not passing; the outcome '
                                    'is recorded beside that label, and no S1b proposal is made from this run without '
                                    'the owner\'s separate decision (E1-T2).',
        'cost_clause': 'not evaluable in Stage 0 (E1-T3)',
        'wording_status': 'confirmed with qualification (E1-T6, amaybaum 2026-10-26)',
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


def placeholders(obj=CONFIG, path=''):
    """Paths of every OWNER placeholder in the configuration."""
    out = []
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            out += placeholders(v, path + '/' + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out += placeholders(v, path + '/' + str(i))
    elif obj == OWNER:
        out.append(path)
    return out


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

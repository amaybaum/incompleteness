#!/usr/bin/env python3
"""SUBSTATE-2: predeclared exact inverse-limit/scale-feedback/gauge controls.

All computations finite and integer/rational. Infinite-depth conclusions
rest on separate mathematics; these finite tests are controls, not proof.
No quantum instruments, physical OI update or YM action is constructed.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json

EDGE = ((0, 1), (1, 2), (2, 3), (3, 0))


def need(cond, title):
    if not cond:
        raise AssertionError(title)


def model_a():
    out = []
    for n in range(1, 10):
        q = 2 ** n
        counts = Counter((x & 1, ((x + 1) % q) & 1, ((x + 2) % q) & 1)
                         for x in range(q))
        need(counts == Counter({(0, 1, 0): q // 2, (1, 0, 1): q // 2}), f'A joint n{n}')
        need(all(((x + 1) % q) % 2 == (x + 1) % 2 for x in range(q)), f'A factor n{n}')
        if n > 1:
            h = q // 2
            need(all(((x + 1) % q) % h == ((x % h + 1) % h) for x in range(q)),
                 f'A projection n{n}')
        out.append({'level': n, 'states': q, 'one_step': [[0, 1], [1, 0]],
                    'return_time': 2, 'nonpermutation': False})
    return {'label': 'A_2adic_odometer', 'status': 'PASS_NEGATIVE_CONTROL', 'stages': out,
            'scope': 'Exact finite quotients n=1..9; all-level compatibility follows by modular arithmetic'}


def model_b():
    fixed = []
    bits = 8
    q = 1 << bits
    for m in [1, 2, 3, 5, 7]:
        def step(x):
            return x ^ ((x >> m) & 1)
        need(all(step(step(x)) == x for x in range(q)), f'B involution depth{m}')
        counts = Counter(((x & 1), (step(x) & 1), (step(step(x)) & 1)) for x in range(q))
        expected = Counter({(0, 0, 0): q//4, (0, 1, 0): q//4,
                            (1, 0, 1): q//4, (1, 1, 1): q//4})
        need(counts == expected, f'B full triple depth{m}')
        need((0 % (1 << m) == (1 << m) % (1 << m))
             and ((step(0) & 1) != (step(1 << m) & 1)), f'B depth witness {m}')
        fixed.append({'hidden_bit_depth': m, 'states_enumerated': q,
                      'P_X0_X1_X2': {'000':'1/4','010':'1/4','101':'1/4','111':'1/4'},
                      'rooted_Gamma_1': [['1/2','1/2'],['1/2','1/2']],
                      'rooted_Gamma_2': [[1,0],[0,1]],
                      'conditional_mutual_information_bits': 1,
                      'minimal_initial_prefix_length_for_next_readout': m + 1})
    shifts=[]
    for n in range(3, 10):
        total = 1 << n
        def shift(x):
            return (x >> 1) | ((x & 1) << (n-1))
        need(all(shift(x) < total for x in range(total)), 'B shift range')
        for x in range(total):
            y=x
            for _ in range(n): y=shift(y)
            need(y == x, f'B cyclic return n{n}')
        for t in range(1, n):
            bits_out = Counter(((x & 1), ((x >> t) & 1)) for x in range(total))
            need(all(bits_out[(a,b)] == total // 4 for a in (0,1) for b in (0,1)),
                 f'B shift two-time n{n} t{t}')
        for h in range(min(4, n-1) + 1):
            counts=Counter(tuple((x >> t)&1 for t in range(h+1)) for x in range(total))
            need(len(counts) == (1 << (h+1)), f'B shift word support n{n} h{h}')
            need(set(counts.values()) == {total >> (h+1)}, f'B shift word mass n{n} h{h}')
        shifts.append({'cycle_length': n, 'states': total,
                       'Gamma_for_0_lt_t_lt_n': [['1/2','1/2'],['1/2','1/2']],
                       'return_time': n, 'all_tested_words_uniform': True})
    return {'label': 'B_feedback_and_scale_conveyor', 'status': 'PASS_DISTINCT_CONTROLS',
            'fixed_depth_feedback': fixed, 'cyclic_shift_approximations': shifts,
            'scope': 'Finite tests; infinite bi-infinite shift has iid forward bits by independent coordinates, no finite exact return a.e.'}


def gauge(u, g, q):
    return tuple((u[i] + g[a] - g[b]) % q for i, (a,b) in enumerate(EDGE))


def model_c():
    stages = []
    for n in range(1, 5):
        q=1 << n
        counts=Counter()
        for u in product(range(q), repeat=4):
            k=sum(u)%q
            nxt=((u[0]+1)%q, *u[1:])
            prev=((nxt[0]-1)%q, *nxt[1:])
            need(prev == u, f'C inverse n{n}')
            need(sum(nxt)%q == (k+1)%q, f'C loop shift n{n}')
            need(((sum(nxt)%q)&1) == (1-(k&1)), f'C bit flip n{n}')
            for vertex in range(4):
                g=tuple(int(i==vertex) for i in range(4))
                need(sum(gauge(u,g,q))%q == k, f'C gauge holonomy n{n}')
                need(gauge(nxt,g,q) == ((gauge(u,g,q)[0]+1)%q, *gauge(u,g,q)[1:]),
                     f'C gauge equivariance n{n}')
            if n>1:
                p=q//2
                need(tuple(x%p for x in nxt) == (((u[0]%p +1)%p),*(x%p for x in u[1:])),
                     f'C reduction commute n{n}')
            counts[k]+=1
        need(all(counts[k] == q**3 for k in range(q)), f'C Haar holonomy n{n}')
        need(sum((counts[k] for k in range(q))) == q**4, f'C Haar normalization n{n}')
        if n<=2:
            for f in product(range(q), repeat=4):
                u=tuple((f[b]-f[a])%q for a,b in EDGE)
                need(sum(u)%q == 0, f'C gradient n{n}')
        need(sum((1,0,0,0))%q == 1%q, f'C nonflat witness n{n}')
        stages.append({'level': n, 'link_states_enumerated': q**4,
                       'holonomy_count_per_value': q**3,
                       'nonflat_holonomy_exists': True,
                       'finite_visible_return_time': 2,
                       'U1_SU2_gauge_carrier_derived': False})
    c={0:F(1),1:F(0),2:F(-1),3:F(0)}
    w={k:F(1)-c[k] for k in range(4)}
    w2={k:w[k]*w[k] for k in range(4)}
    need(w[1]==1 and w2[1]==1 and w[2]==2 and w2[2]==4, 'C nonproportional actions')
    need(sum(c.values())==0, 'C Haar cos zero')
    need(sum(w.values())/4 == 1 and sum(w2.values())/4 == F(3,2), 'C Haar moments')
    return {'label': 'C_profinite_gauge_tower', 'status': 'PASS_KINEMATICS_ACTION_NOT_SELECTED',
            'stages': stages, 'quarter_turn_action_control': {'k1_w': '1','k1_w2':'1',
            'k2_w':'2','k2_w2':'4', 'haar_mean_w':'1','haar_mean_w2':'3/2'},
            'scope': 'Finite Z/2^n abelian gauge tower, not connected U(1), SU(2), SU(3) or YM dynamics'}


def main():
    a=model_a();b=model_b();c=model_c()
    out={'status': 'PASS_EXACT_FINITE_CONTROLS',
         'A': {'status':a['status'], 'stages': [s['level'] for s in a['stages']],
               'joint_probabilities': {'010':'1/2','101':'1/2'},
               'visible_period':2,'rooted_nonpermutation':False},
         'B1': {'status':'PASS_FEEDBACK_ROOTED_INDIVISIBLE',
                'hidden_depths_checked':[s['hidden_bit_depth'] for s in b['fixed_depth_feedback']],
                'three_time_law':b['fixed_depth_feedback'][0]['P_X0_X1_X2'],
                'Gamma_1':b['fixed_depth_feedback'][0]['rooted_Gamma_1'],
                'Gamma_2':b['fixed_depth_feedback'][0]['rooted_Gamma_2'],
                'conditional_memory_bits':1,'visible_period':2},
         'B2': {'status':'PASS_SHIFT_CONVEYOR',
                'cycle_lengths_checked':[s['cycle_length'] for s in b['cyclic_shift_approximations']],
                'pre_return_rooted':b['cyclic_shift_approximations'][0]['Gamma_for_0_lt_t_lt_n'],
                'infinite_shift_common_visible_return':False},
         'C': {'status':c['status'],'levels':[s['level'] for s in c['stages']],
               'max_link_states_enumerated':c['stages'][-1]['link_states_enumerated'],
               'full_link_prior':'independent counting Haar',
               'gauge_action':'local additive vertex shifts on finite Z/2^n links',
               'nonflat_witness':True, 'finite_visible_period':2,
               'action_nonuniqueness':c['quarter_turn_action_control']},
         'lean_status':'no Lean evidence from this script',
         'native_OI_dynamics_derived':False,
         'operational_QM_derived':False,
         'YM_action_derived':False,
         'log_periodic_signal_derived':False,
         'finite_physical_boundary_entropy_derived':False}
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__=='__main__': main()

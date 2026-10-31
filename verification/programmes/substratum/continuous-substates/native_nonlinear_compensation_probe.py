#!/usr/bin/env python3
"""A sourced two-tick product at J, followed by a whole-carrier test."""
import argparse
import ast
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


D = tuple(tuple(s if j == a else 0 for j in range(3))
          for a in range(3) for s in (-1, 1))
Z = (0, 0, 0)


def add(a, b): return tuple(x+y for x, y in zip(a, b))
def dist(a, b): return sum(abs(x-y) for x, y in zip(a, b))
def enc(a, b, d): return 4*a+2*b+d


def xor(values):
    out = 0
    for value in values:
        out ^= value
    return out


def h(v):
    a, b, d = v >> 2, (v >> 1) & 1, v & 1
    return enc(b, d, a ^ (b & d))


def index(values, sizes):
    out = 0
    for value, size in zip(values, sizes):
        out = size*out+value
    return out


def anf(values):
    out = list(values)
    for bit in range(4):
        for mask in range(16):
            if mask & (1 << bit):
                out[mask] ^= out[mask ^ (1 << bit)]
    return [i for i, value in enumerate(out) if value]


def read_pinned(path, digest):
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == digest, 'source pin '+path.name)
    return raw.decode()


def run(root):
    route_text = read_pinned(root/'native_route_v13/checks.py',
                            '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856')
    read_text = read_pinned(root/'native_vread_v15/checks.py',
                           '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    inventory = json.loads(read_pinned(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json',
                                      '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d'))['sources']
    qt = json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt = json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(hashlib.sha256(qt.encode()).hexdigest() == 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'q10 table pin')
    need(hashlib.sha256(pt.encode()).hexdigest() == 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf', 'q9 table pin')
    T = 185
    P = 12*840**185
    S, R, L = P+T, P+T+68, P+T+77
    env = {'T': T, 'P': P, 'S': S, 'R': R, 'L': L, '__builtins__': {}}
    # Read only the primary named-source/port data, not its probe engine.
    tree = ast.parse(read_text)
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'local_sources')
    sources_node = next(n.value for n in fn.body if isinstance(n, ast.Return))
    named = eval(compile(ast.Expression(sources_node), '<pinned source positions>', 'eval'), env)
    ports_node = next(n.value for n in tree.body if isinstance(n, ast.Assign) and
                      any(isinstance(t, ast.Name) and t.id == 'PORTS' for t in n.targets))
    ports = eval(compile(ast.Expression(ports_node), '<pinned bank positions>', 'eval'), env)
    j, q = named['J'], (0, S, 78)
    need(len(inventory) == 1479 and len(named) == 17 and len(ports) == 8, 'declared geometry counts')
    need(dist(j, q) == L-1 and dist(named['N'], j) == 2, 'two-tick computation on original N front')
    need(dist(j, q)+2 == L+1, 'computed-field causal arrival bound')
    need(all(dist(named[name], (0, S, 77)) == L+2 for name in ('E', 'N')),
         'E/N cannot affect the retained old q9 record')
    need({k for k, v in named.items() if dist(v, j) <= 2} == {'J', 'G', 'N', 'Kplus', 'Kminus'},
         'exact named sources in the local current cone')
    need(all(dist(tuple(row['position']), j) > 2 for row in inventory), 'no compiled source omitted locally')
    need([tuple(row['position']) for row in inventory if dist(tuple(row['position']), q) <= L+1] == [Z],
         'only reflection-invariant compiled origin reaches q10')
    asym = {name for name, pos in named.items() if dist(pos, q) <= L+1 and pos[0] != 0}
    need(asym == {'Kplus', 'Kminus', 'selector_plus', 'selector_minus', 'F10_pin'},
         'only paired sources and replaced zero pin are asymmetric in the deadline cone')
    for left, right in (('Kplus', 'Kminus'), ('selector_plus', 'selector_minus')):
        need((-named[left][0], named[left][1], named[left][2]) == named[right],
             'physical paired-source reflection')
    for d in D:
        need(dist(add(j, d), q) <= L, 'local previous cone inside prepared previous ball')
        for e in D:
            need(dist(add(add(j, d), e), q) <= L+1, 'local current cone inside prepared full ball')
    for port, direction, deadline in ports:
        axis = next(i for i, value in enumerate(direction) if value)
        optimum = (q[axis]-port[axis])*direction[axis]
        times = (deadline+1, 2*L, min(2*L, max(deadline+1, optimum)))
        need(min(dist(tuple(v+t*w for v, w in zip(port, direction)), q) for t in times) > L+1,
             'all reserved bank cells excluded from q10 deadline cone')
    # Extract the original affine upper source lambdas as data. They are not
    # a native evaluator; the local native recursion below is independent.
    route_ast = ast.parse(route_text)
    dictionary = next(n.value for n in route_ast.body if isinstance(n, ast.Assign) and
                      any(isinstance(t, ast.Name) and t.id == 'SOURCES' for t in n.targets))
    tr = tuple(itertools.product(range(2), repeat=3))
    functions = {ast.literal_eval(k): eval(compile(ast.Expression(v.args[0]), '<pinned affine payload>', 'eval'),
                                          {'TR': tr, '__builtins__': {}})
                 for k, v in zip(dictionary.keys, dictionary.values)}
    local_keys = {'J': (0, 0, -18), 'G': (0, 0, -16), 'N': (0, 0, -20),
                  'Kplus': (1, 0, -17), 'Kminus': (-1, 0, -17)}
    for name, key in local_keys.items():
        need(tuple(v-w for v, w in zip(named[name], j)) == (key[0], key[1], -(key[2]+18)),
             'physical source positions agree with signed upper cluster')
    bit_tables = []
    nonlinearity_controls = old_term_controls = 0
    for setting in range(2):
        outputs = []
        initial = [[] for _ in range(15)]
        for row in range(16):
            u, a, b, mr = ((row >> i) & 1 for i in range(4))
            n = u ^ a ^ mr  # N=(0,0,u XOR a XOR mR), affine and independent of unknown x.
            values = {name: enc(*functions[key](u, a, b, n)) for name, key in local_keys.items()}
            if setting:
                values['Kplus'], values['Kminus'] = values['Kminus'], values['Kplus']
            relative = {tuple(v-w for v, w in zip(named[name], j)): values[name] for name in local_keys}
            for f, value in enumerate(values.values()):
                for bit in range(3):
                    initial[3*f+bit].append((value >> (2-bit)) & 1)
            @lru_cache(None)
            def value(t, p):
                if t < 0:
                    return 0
                if t == 0:
                    return relative.get(p, 0)
                return value(t-2, p) ^ h(xor(value(t-1, add(p, d)) for d in D))
            result = value(2, Z)
            want = enc(1 ^ a ^ b ^ mr, 1 ^ (a & mr), mr ^ u ^ (u & a) ^ (u & a & mr))
            need(result == want and value(1, Z) == 0, 'full computed triple and previous local slice')
            neighbor_sum = xor(value(1, d) for d in D)
            old_term_controls += (h(neighbor_sum) != result)
            def linear_h(v): return enc((v >> 1) & 1, v & 1, v >> 2)
            first_linear = {d: linear_h(xor(relative.get(add(d, e), 0) for e in D)) for d in D}
            linear_result = relative[Z] ^ linear_h(xor(first_linear.values()))
            nonlinearity_controls += linear_result != result
            outputs.append(result)
        need(all(max((i.bit_count() for i in anf(v)), default=0) <= 1 for v in initial),
             'every initial payload field is affine; no product preloaded')
        monomials = [anf([(value >> (2-bit)) & 1 for value in outputs]) for bit in range(3)]
        need(monomials == [[0, 2, 4, 8], [0, 10], [1, 3, 8, 11]], 'independent exact Mobius reconstruction')
        bit_tables.append(monomials)
    need(nonlinearity_controls > 0 and old_term_controls > 0, 'native nonlinear and old-local controls nonvacuous')
    # Local x reflection reconstructs the swapped q10 response. Independent
    # E/N values remain fixed when the +/-T selector labels exchange.
    swapped = ''.join(qt[index((x, u, mr, my, a, b, e, n), (2,)*6+(8, 8))]
                      for x, u, my, mr, a, b in itertools.product(range(2), repeat=6)
                      for e, n in itertools.product(range(8), repeat=2))
    need(hashlib.sha256(swapped.encode()).hexdigest() == '1a3a88b8832985efab3000852fcb13357832d04e2bcee77d077af5c8b09dd754',
         'full swapped native response matches accepted reconstruction')
    changed = continuing = terminal = 0
    candidate_values = []
    first = None
    for bits in itertools.product(range(2), repeat=6):
        x, u, my, mr, a, b = bits
        e, n, n0 = 7-2*my, u ^ a ^ mr, 4*my+2+(1 ^ my)
        base = int(qt[index(bits+(e, n0), (2,)*6+(8, 8))], 16)
        out = int(swapped[index(bits+(e, n), (2,)*6+(8, 8))], 16)
        candidate_values.append(out)
        need(pt[index(bits+(4, 5, 7), (2,)*6+(8,)*3)] == pt[index(bits+(4, 7, 5), (2,)*6+(8,)*3)],
             'complete old q9 record including terminal rows preserved')
        stop = (a, b) == (0, 1)
        terminal += stop
        continuing += not stop
        if out != base:
            changed += 1
            if not stop and first is None:
                first = {'bits_x_u_mY_mR_a_b': bits, 'baseline_Q': base, 'candidate_Q': out}
    need(continuing == 48 and terminal == 16 and len(candidate_values) == 64, 'full source and terminal coverage')
    return {'status': 'PASS',
            'verdict': 'NATIVE_PRODUCT_COMPUTED_CARRIER_NOT_PRESERVED' if first else 'NATIVE_PRODUCT_ONLY',
            'local_source_contexts': 32, 'initial_field_degree_at_most': 1,
            'computed_J_B_ANF_masks_u_a_b_mR': [0, 10], 'full_J_ANF_by_orientation': bit_tables,
            'nonlinear_rule_control_changed_worlds': nonlinearity_controls,
            'omitted_old_term_changed_worlds': old_term_controls,
            'computation_time': 2, 'earliest_q10_arrival': 'L+1', 'delivery_certificate': 'NOT_ESTABLISHED',
            'changed_Q_rows': changed, 'continuing_source_rows': continuing,
            'terminal_microscopic_rows': terminal, 'first_continuing_Q_change': first,
            'candidate_Q_table_hex': ''.join(format(v, 'x') for v in candidate_values),
            'new_sources': 0, 'new_reads': 0, 'native_measurement_or_reuse': 'NOT_ESTABLISHED'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[2] /
                        'oi-qm/reconstruction/native-y-continuation-20261024')
    args = parser.parse_args()
    try:
        result = run(args.source_root)
    except (RuntimeError, ValueError, KeyError, OSError, StopIteration, TypeError) as exc:
        print(json.dumps({'status': 'VOID', 'reason': str(exc)}, sort_keys=True))
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))

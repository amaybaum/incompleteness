"""Independent bounded controls of written native transport/frontier proofs.

No author engines, imports, files, floating point, or external programs.
"""
from functools import lru_cache
from itertools import permutations, product
from math import gcd, lcm
import json


STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
         (0, -1, 0), (0, 0, 1), (0, 0, -1))


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def h(s):
    a, b, d = s >> 2, (s >> 1) & 1, s & 1
    return 4 * b + 2 * d + (a ^ (b & d))


def hinv(s):
    a, b, d = s >> 2, (s >> 1) & 1, s & 1
    return 4 * (d ^ (a & b)) + 2 * a + b


def plus(p, q):
    return tuple(x + y for x, y in zip(p, q))


def distance(p, q):
    return sum(abs(x - y) for x, y in zip(p, q))


def dense(p, old=False):
    x, y, z = p
    return ((x * x + 3 * y * y + 5 * z + x * y + 19 * old) ^
            (7 * x - 9 * y + z * z + 11 * old)) & 7


def evaluator(current, previous, side=None):
    """Independent backward-cone definition of the complete native rule."""
    def norm(p):
        return tuple(v % side for v in p) if side else p

    @lru_cache(None)
    def raw(t, p):
        if t == 0:
            return current(p)
        if t == -1:
            return previous(p)
        summed = 0
        for step in STEPS:
            summed ^= raw(t - 1, norm(plus(p, step)))
        return raw(t - 2, p) ^ h(summed)

    return lambda t, p: raw(t, norm(p))


def front_points(radius):
    return sorted(((x, z) for x in range(-radius, radius + 1)
                   for z in range(-radius, radius + 1)
                   if abs(x) + abs(z) <= radius),
                  key=lambda p: (-abs(p[0]) - abs(p[1]), p))


def front_step(values, points):
    result = {}
    for x, z in points:
        r = abs(x) + abs(z)
        total = values[x, z]
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = x + dx, z + dz
            if q in result and abs(q[0]) + abs(q[1]) == r + 1:
                total ^= result[q]
        result[x, z] = h(total)
    return result


def front_inverse(values, points):
    result = {}
    for x, z in points:
        r = abs(x) + abs(z)
        total = hinv(values[x, z])
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = x + dx, z + dz
            if q in values and abs(q[0]) + abs(q[1]) == r + 1:
                total ^= values[q]
        result[x, z] = total
    return result


def global_inverse_control():
    # A random-looking complete 3^3 torus; duplicate neighbors would also
    # remain valid because the inverse uses the identical neighbor operator.
    points = tuple(product(range(3), repeat=3))
    comparisons = 0
    for seed in range(12):
        old = {p: (dense(p, True) + seed * (1 + sum(p))) & 7 for p in points}
        now = {p: (dense(p) ^ (seed + p[0])) & 7 for p in points}
        for local in (h, lambda s: 0):
            future = {}
            for p in points:
                total = 0
                for step in STEPS:
                    total ^= now[tuple(v % 3 for v in plus(p, step))]
                future[p] = old[p] ^ local(total)
            for p in points:
                total = 0
                for step in STEPS:
                    total ^= now[tuple(v % 3 for v in plus(p, step))]
                need((future[p] ^ local(total)) == old[p], "global inverse")
                comparisons += 1
    return comparisons


def axial_control():
    comparisons = 0
    maps = 0
    for delta in STEPS:
        for length in range(1, 5):
            source = tuple(-length * d for d in delta)
            for background in range(2):
                base_current = lambda p: dense(p) if background else 0
                base_previous = lambda p: dense(p, True) if background else 0
                baseline = evaluator(lambda p: 0 if p == source else base_current(p),
                                     base_previous)
                image = []
                for value in range(8):
                    run = evaluator(lambda p: value if p == source else base_current(p),
                                    base_previous)
                    predicted = value
                    for k in range(1, length + 1):
                        p = plus(source, tuple(k * d for d in delta))
                        predecessor = plus(p, tuple(-d for d in delta))
                        background_sum = 0
                        for step in STEPS:
                            q = plus(p, step)
                            if q != predecessor:
                                background_sum ^= baseline(k - 1, q)
                        predicted = baseline(k - 2, p) ^ h(predicted ^ background_sum)
                    actual = run(length, (0, 0, 0))
                    need(actual == predicted, "dirty-background axial response")
                    image.append(actual)
                    comparisons += 1
                need(len(set(image)) == 8, "unique axis map is permutation")
                maps += 1
    return maps, comparisons


def extrusion_control():
    comparisons = 0
    prefixes = 0
    for radius in (1, 2, 3):
        points = front_points(radius)
        delay = 4
        end = (0, delay, 0)
        horizon = radius + delay
        shell = tuple((x, y, z)
                      for x, y, z in product(range(-radius, radius + 1), repeat=3)
                      if y <= 0 and abs(x) + abs(y) + abs(z) == radius)
        for seed in (1, 2, 5):
            sources = {p: (dense(p) + seed * (3 + 2 * p[0] + p[2])) & 7
                       for p in shell}

            def current(p):
                if p in sources:
                    return sources[p]
                return 0 if distance(p, end) <= horizon else dense(p)

            def previous(p):
                return 0 if distance(p, end) <= horizon - 1 else dense(p, True)

            run = evaluator(current, previous)
            front = {p: run(radius - abs(p[0]) - abs(p[1]), (p[0], 0, p[1]))
                     for p in points}
            for depth in range(delay + 1):
                for x, z in points:
                    actual = run(radius - abs(x) - abs(z) + depth, (x, depth, z))
                    need(actual == front[x, z], "complete native extrusion recurrence")
                    comparisons += 1
                need(front_inverse(front_step(front, points), points) == front,
                     "abstract front inverse")
                front = front_step(front, points)
            for tick in range(horizon):
                need(run(tick, end) == 0, "blank first-arrival prefix")
                prefixes += 1
    return comparisons, prefixes


def complete_radius_one():
    points = front_points(1)
    size = 8 ** len(points)

    def encode(values):
        return sum(values[p] << (3 * i) for i, p in enumerate(points))

    def decode(value):
        return {p: (value >> (3 * i)) & 7 for i, p in enumerate(points)}

    table = []
    for raw in range(size):
        state = decode(raw)
        target = front_step(state, points)
        need(front_inverse(target, points) == state, "all-state inverse")
        table.append(encode(target))
    need(len(set(table)) == size, "all-state bijection")
    visited = set()
    orders = []
    for start in range(size):
        if start in visited:
            continue
        p = start
        length = 0
        while p not in visited:
            visited.add(p)
            length += 1
            p = table[p]
        need(p == start, "permutation cycle closure")
        orders.append(length)
    order = lcm(*orders)
    need(order == 720 and (12 * 840) % order == 0, "radius-one exact period")
    return size, len(orders), order, sorted(set(orders))


def frontier_pair(shared=False, pinned=False, cyclic=False):
    if cyclic:
        ports = ((0, 0, 0), (1, 1, 0))
        sources = ((0, 3, 0), (-2, 1, 0))
    else:
        ports = ((1, 0, 0), (0, 1, 0))
        sources = ((1, 3, 0), (0, 4, 0))
    outputs = set()
    for a, b in product(range(8), repeat=2):
        if shared and a != b:
            continue
        if pinned and b:
            continue
        initial = {sources[0]: a, sources[1]: b}
        run = evaluator(lambda p: initial.get(p, 0 if cyclic else dense(p)),
                        lambda p: 0 if cyclic else dense(p, True))
        pair = tuple(run(3, p) for p in ports)
        if cyclic:
            target = h(h(h(a) ^ h(b)))
            need(pair == (target, target), "equal-time dependency cycle collapse")
        outputs.add(pair)
    return len(outputs)


def wings_control():
    comparisons = 0
    terminal_omissions = 0
    for deadline in (2, 3, 4, 5):
        for seed in range(6):
            controls = [((seed + 1) * (t + 2) ^ (t * t + seed)) & 7
                        for t in range(deadline - 1)] + [0]
            profile = {}
            for wing in range(3):
                for t in range(deadline):
                    component = (wing - t) % 3
                    profile[wing, t] = (controls[t] >> (2 - component)) & 1
            sources = {}
            for wing in range(3):
                for q in range(deadline):
                    value = 0
                    for e in range(q + 1):
                        if e & ~q == 0:
                            value ^= profile[wing, e]
                    position = ((deadline - 1 - q, q + 1, 0),
                                (deadline - 1 - q, -q - 1, 0),
                                (deadline - 1 - q, 0, q + 1))[wing]
                    sources[position] = sources.get(position, 0) ^ (value << (2 - wing))
            run = evaluator(lambda p: sources.get(p, 0), lambda p: 0)
            state = 0
            for t, control in enumerate(controls):
                state = h(state ^ control)
                position = (deadline - 1 - t, 0, 0)
                need(run(t + 1, position) == state, "whole native wing/spine step")
                comparisons += 1
            need(all(run(t, (0, 0, 0)) == 0 for t in range(deadline)), "wing blank prefix")
            truncated = {p: s for p, s in sources.items() if p[0] != 0}
            omit = evaluator(lambda p: truncated.get(p, 0), lambda p: 0)
            if omit(deadline, (0, 0, 0)) != state:
                terminal_omissions += 1
    need(terminal_omissions > 0, "terminal row omission countercontrol")
    return comparisons, terminal_omissions


def main():
    need(all(hinv(h(s)) == s for s in range(8)), "H inverse")
    state_order = []
    for start in range(8):
        value = h(start)
        count = 1
        while value != start:
            value = h(value)
            count += 1
        state_order.append(count)
    need(lcm(*state_order) == 12, "H exact order")
    need(h(h(h(3))) != 3, "three-step pure-bit rotation is not a raw-triple period")
    need(h(2 ^ 1) != (h(2) ^ h(1)), "nonlinear H prevents pulse superposition")
    permutations_checked = 0
    for p in permutations(range(8)):
        seen = set()
        order = 1
        for s in range(8):
            if s in seen:
                continue
            value = s
            length = 0
            while value not in seen:
                seen.add(value)
                length += 1
                value = p[value]
            need(value == s, "eight-symbol permutation cycle")
            order = lcm(order, length)
        need(840 % order == 0, "universal eight-symbol exponent")
        permutations_checked += 1
    p_actual = 12 * 840 ** 185
    need(all(p_actual % (12 * 840 ** r) == 0 for r in (0, 18, 144, 176, 185)),
         "actual P divides covered strip/front bounds")
    need(p_actual % (12 * 840 ** 186) != 0, "larger budget not implied")
    maps, axial_cases = axial_control()
    front_cases, prefixes = extrusion_control()
    front_states, cycles, order, cycle_lengths = complete_radius_one()
    diagonal_images = []
    for source_value in range(8):
        run = evaluator(lambda p: source_value if p == (1, 1, 0) else 0, lambda p: 0)
        diagonal_images.append(run(2, (0, 0, 0)))
    need(diagonal_images == [0] * 8, "two shortest paths cancel at diagonal")
    pair = frontier_pair()
    shared = frontier_pair(shared=True)
    pinned = frontier_pair(pinned=True)
    cyclic = frontier_pair(cyclic=True)
    need(pair == 64 and shared == pinned == 8, "frontier block controls")
    need(cyclic < 64, "same-time cycle can destroy joint frontier bijection")
    # This witness does not say every cyclic dependency graph is singular.
    wrap = evaluator(lambda p: 4 if p == (2, 0, 0) else 0, lambda p: 0, side=3)
    need(wrap(1, (0, 0, 0)) == h(4) != 0, "wrap violates nominal blank prefix")
    wing_steps, terminal_omissions = wings_control()
    result = {
        "schema": "oi-native-transport-proof-audit-v1",
        "verdict": "ACCEPT_SCOPED_LEMMAS",
        "H_order": 12,
        "raw_H_cubed_identity_rejected": True,
        "pulse_superposition_countercontrol_detected": True,
        "eight_symbol_permutations_checked": permutations_checked,
        "global_inverse_site_comparisons": global_inverse_control(),
        "axial_maps": maps,
        "axial_value_comparisons": axial_cases,
        "native_extrusion_front_values": front_cases,
        "blank_prefix_values": prefixes,
        "radius_one_states": front_states,
        "radius_one_cycles": cycles,
        "radius_one_order": order,
        "radius_one_cycle_lengths": cycle_lengths,
        "diagonal_two_path_images": diagonal_images,
        "frontier_pair_distinct_images": pair,
        "frontier_pair_shared_images": shared,
        "frontier_pair_pinned_images": pinned,
        "frontier_pair_cyclic_diagnostic_images": cyclic,
        "wrap_early_arrival_detected": True,
        "native_wing_spine_steps": wing_steps,
        "terminal_row_omission_cases_detected": terminal_omissions,
        "all_required_controls": "PASS",
        "scope": "Written proof plus bounded controls; no giant-time simulation, reusable instrument, or external review."
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

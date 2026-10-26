"""Count the certificate checks the audit should perform, from reported depths alone, and list which
certificate kinds are reached per member. Usage: python3 -I -B count_certs.py result.json"""
import json, sys
r = json.load(open(sys.argv[1])); fam = r['family_RS']
tot = 0; per = {}; never_half = []
for B in (2, 3, 4):
    for k in range(1, 17):
        e = fam[f'B{B}_k{k}']; pp = e['post_plan']
        hp = pp['power_rule_T_above_half_for_h_at_least'] // k; nh = e['certified_T_above_half_for_h_at_least'] // k
        lp = pp['power_rule_T_at_most_half_for_h_at_most'] // k; nt = e['certified_T_at_most_tenth_for_h_at_most'] // k
        c = {'gt_half': 0, 'le_half': 0, 'le_tenth': 0, 'k1': 0}
        n = 1
        while n * k <= 16:
            if n >= hp or n >= nh: c['gt_half'] += 1
            if n <= lp: c['le_half'] += 1
            if n <= nt: c['le_tenth'] += 1
            n += 1
        if k == 1:
            c['k1'] = sum(1 for x in (hp, nh, lp) if x >= 1) + (1 if nt >= 1 else 0)
        per[(B, k)] = c; tot += sum(c.values())
        if c['gt_half'] == 0 and c['k1'] == 0: never_half.append((B, k))
print('total', tot, 'audit reports', r['independent_certificate_audit_post_recheck2'])
print('members whose T>1/2 certificate is never checked against exact TV:', len(never_half), never_half)
print('members with gt_half checked:', [(B, k) for (B, k), c in per.items() if c['gt_half'] or (k == 1)])

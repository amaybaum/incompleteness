"""Compare retained per_mutant_numbers.json with the reviewer's original per-mutant outputs.
Usage: python3 -I -B check_pmn.py pmn.json <recheck2 rmut3 dir> <recheck3 rmut5 dir>"""
import hashlib, json, os, sys
pmn = json.load(open(sys.argv[1])); r3, r4 = sys.argv[2], sys.argv[3]
bad = 0
w = pmn['round3_W_depth_shifts']
for name, ent in w['mutants'].items():
    path = os.path.join(r3, name, 'run2', 'out.json'); raw = open(path, 'rb').read(); out = json.loads(raw)
    if hashlib.sha256(raw).hexdigest() != ent['source_output_sha256']: bad += 1; print('SHA MISMATCH', name)
    for key, vals in ent['members'].items():
        e = out['family_RS'][key]
        mine = [e['certified_T_above_half_for_h_at_least'], e['post_plan']['power_rule_T_above_half_for_h_at_least'],
                e['post_plan']['power_rule_T_at_most_half_for_h_at_most']]
        if mine != vals: bad += 1; print('VALUE MISMATCH', name, key, mine, vals)
l = pmn['round4_L_audit_counts']
for name, ent in l['mutants'].items():
    path = os.path.join(r4, name, 'run', 'out.json'); raw = open(path, 'rb').read(); out = json.loads(raw)
    if hashlib.sha256(raw).hexdigest() != ent['source_output_sha256']: bad += 1; print('SHA MISMATCH', name)
    a = out['independent_certificate_audit_post_recheck2']
    if (a['members'], a['certificates_checked_against_exact_tv']) != (ent['members'], ent['certificates_checked_against_exact_tv']):
        bad += 1; print('VALUE MISMATCH', name)
print('mismatches', bad)

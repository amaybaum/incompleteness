"""Summarize mutant runs. Usage: summarize.py <mutdir> <result.json>."""
import json
import os
import sys

mutdir, ref_path = sys.argv[1], sys.argv[2]
with open(ref_path) as fh:
    ref = json.load(fh)
for name in sorted(os.listdir(mutdir)):
    run = os.path.join(mutdir, name, 'run')
    rc = open(os.path.join(run, 'rc')).read().strip()
    err = open(os.path.join(run, 'err.txt')).read()
    cells = [ln for ln in err.splitlines() if ln.startswith('CELLS')]
    tb = [ln for ln in err.splitlines() if 'Error' in ln]
    try:
        r = json.load(open(os.path.join(run, 'out.json')))
    except Exception:
        print(name, 'rc', rc, 'NO JSON', tb[-1:] if tb else '')
        continue
    fams = r['scaled_families']
    g = r['actual_geometry']
    print(f"{name}: rc={rc} verdict={r['verdict']} controls={ {k: v for k, v in r['required_controls'].items() if not v} or 'all true'}")
    print('   g1', g['g1_tail_reaches_no_carrier_site_time'], 'slack', g['g1_min_tail_slack_over_carrier_site_times'],
          '| cells', [c.split()[2] for c in cells])
    for f in fams:
        print('   seed', f['seed'], 's1', f['s1_pre_tail_records_constant'], 's2', f['s2_pool_tail_record_support'],
              's3', f['s3_complete_record_law_matches_v6'], 'tv', f['s3_fresh_tail_record_carrier_tv'],
              'x1mm', f['x1_scalar_mismatched_outputs'], 'x2', f['x2_pass'],
              'c2', f['c2_duplicated_tail_record_carrier_tv'], 'x3sup', f['x3_duplicated_tail_support'],
              'c1max', f['c1_max_record_carrier_tv'], 'c1min', f['c1_min_record_carrier_tv'],
              'c3', f['c3_native_q8_at_horizon_tail_record_tv'], 'c3pre', f['c3_native_q8_two_ticks_before_tail_arrival_tv'])
    print('   bank_lb', r['known_tail_countercontrol_shows_bank_load_bearing'],
          'storage_lb', r['native_continuation_shows_frozen_storage_load_bearing'],
          'same_as_ref', r == ref)

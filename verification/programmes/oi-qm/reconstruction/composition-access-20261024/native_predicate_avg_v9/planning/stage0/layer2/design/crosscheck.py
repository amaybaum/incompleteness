"""Layer-2 design evidence: the production path's 54 reported counts on the toy class (sharded,
orbit-reduced, merged: toyrun/result.json) against the full per-record computation of the
control suite (s0controls C8 'counts', retained in toyrun/preflight.json). Both are read from
structured files. masking_equivalent_records is compared in both readings: the merge's
(contexts with E1 merges) and code-r5's (record samples), which coincide on the toy class.
Usage: python3 -I -B crosscheck.py <toyrun dir>. Prints JSON; exit 0 iff every count agrees."""
import json
import os
import sys

d = sys.argv[1]
with open(os.path.join(d, 'result.json')) as f:
    res = json.load(f)
with open(os.path.join(d, 'preflight.json')) as f:
    full = json.load(f)['controls_counts_C8']
merged = res['counts']
diff = {k: [merged.get(k), full[k]] for k in sorted(full) if merged.get(k) != full[k]}
extra = sorted(set(merged) - set(full))
reading = [res['masking_equivalent_records_record_sample_reading'], full['masking_equivalent_records']]
nonzero = sum(1 for v in full.values() if v)
out = {'compared': len(full), 'differences': diff, 'keys_only_in_merge': extra,
       'record_sample_reading_vs_code_r5': reading, 'counts_nonzero': nonzero,
       'counts_identically_zero': len(full) - nonzero, 'label': res['label'],
       'pass': len(full) == 54 and not diff and not extra and reading[0] == reading[1]}
print(json.dumps(out, indent=1, sort_keys=True))
sys.exit(0 if out['pass'] else 2)

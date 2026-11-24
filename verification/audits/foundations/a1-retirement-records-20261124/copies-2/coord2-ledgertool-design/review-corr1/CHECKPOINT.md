# Checkpoint: review of correction 1 (3184c7f9)

Scratch: SP/rv-corr1 (tree/ = checkout-index of 3184c7f9, 3660 files, all blobs verified; gitcopy/ = git-init'd copy;
cfg-0ba40976.json = private hash-verified staged config; run.sh = full suite, mirrors rv-perf/v2/run.sh, entry -I -S -B).

## Done
- inputs hash-verified (CORRECTION-1 3352a14e, review 68d4e071, perf review 6def2c2a, DESIGN 4024a31c, config 0ba40976)
- commit object read: tree d3423182, parent c59b562c, signed, trailers present, 9 paths changed
- full suite started in background: `sh SP/rv-corr1/run.sh 3184c7f9075948d8474197eee03ba5b94ba85db5 c1 SP/rv-corr1/cfg-0ba40976.json 0ba40976...` -> SP/rv-corr1/logs, out

## Remaining
- task 1 diff mapping; task 2 probes (line rule, pre-run, yaml, bash -n, O3); task 3 D-2; task 4 controls.json; task 5 mutants; task 6 governance
- compare my run with writer's logs/corr1/full

## Progress 2 (after ~40 min)
- steps 1-5 of my run PASS (exit 0); step 6 (A1 controls) running
- task 1 diff: 9 paths, all map to items; no path outside exception (443e871f..3184c7f9)
- governance: identity ok, trailers ok, SSH sig VALID (python ed25519 check, same key as c59b562c), class record 53 pins = ls-tree, config pins (83 refs) all match, config diff vs c59b562c staged = notes + record sha x2 + 5 tool pins + workflow pin
- probes: line rule (SP/rv-corr1/probe/line_rule.out) 0 unexpected on r01-27,c01,c02,b1a-c,new wf; MY extra: foo/..@hex and foo/bar/../../x@hex PASS the rule (observation, outside B-1)
- yaml check identical to writer, bash -n 0, prerun step identical to c59b562c, runblock argv probe (probe/runblock_args.out), argparse injection refused (probe/inj)
- O3: system config isolation works (C08 = test gap), GIT_CONFIG_COUNT env bypasses (observation) probe/o3_sys.out
- FINDING (candidate BLOCKING): EI6 predicate admits /usr/local/lib/python3.13/site-packages (nested under stdlib dir) -> probe/ei6_predicate.out; expectation says "standard library"; design 10.4 predicate-weaker-than-expectation
- D-2: omitted --classify only removes PASS-enabling records (fail-closed); execution reads class/recon records from cfg['records'] (cli.py 1147-1171), so reading 3's consequence is wrong; records.admit refuses unconfigured records in non-harness mode; item11 --scope path ($D/repo-scope.json) differs from config (tool audit dir) -> SOURCE_CHANGED; no --certified -> C defaults to X
- controls.json: pinned by config as retirement control set (design 16.2), read only for control_inputs; rows GV4/EI5/EI7 narrower than runner

## Progress 3
- my steps 2-5 outputs identical to writer's logs/corr1/full (cmp: SP/rv-corr1/cmp.py); writer head.txt=3184c7f9, staged sha=0ba40976, status clean
- MANIFEST impl-v6.0e: 191 lines verify, first 57 = e65ee36d; corr1 entries from line 132; review-impl & review-perf manifests verify; staging/ 5af8f07e, staging-c59b562c b45be784 intact
- proposal r5 config: delegation = tool-dir delegation-draft.json, scope = tool-dir records/repo-scope-v1.json, class + recon records in cfg.records -> workflow arms 3-14 ($D/delegation.json) and item11 ($D/repo-scope.json) would ERROR SOURCE_CHANGED; items 1,2 lack --classify (proposal 32.4 needs it) -> cannot PASS; item14-landing lacks --certified C (proposal 32.4 has it)
- EI6 predicate finding demonstrated (probe/ei6_predicate.out): certifi from /usr/local/lib/python3.13/site-packages admitted
- remaining: wait step 6, compare with writer's a1-controls.json, write review.md + MANIFEST

## Progress 4
- pre-run probes rerun (probe/run_probes.out) == writer's modulo F ids; program sha 001a3357 same as impl review
- CX-3 rerun (probe/cx3.out): no shadow load, USAGE 64
- release gate in gitcopy (logs/7-gate.log): same rows as writer except legacy-records & citation-roles PASS here (non-shallow); remaining FAIL lean-axioms, v3-corpus, v3-receipts (environment)
- EI6 fix candidate checked (probe/ei6_fix_check.out): excluding sysconfig purelib/platlib (realpath) refuses certifi and admits every import of a -I -S -B tool run
- review.md draft started; verdict REJECT on R-B1 (EI6 predicate)

## DONE
- step 6 (A1 controls) exit 1, 91 PASS 1 NOT RUN, 1188.6 s, 1.48 GB; identical to writer apart from seconds fields
- review.md written (verdict REJECT on R-B1 EI6 predicate); evidence/ copied; MANIFEST.sha256 written

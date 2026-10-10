# n18 equivalence ledger (append-only): per pair, sha256 of the old and new records, written before the next shard starts
environment: see environment.txt; worktree d6b64580 (carry-forward-manifest.md -> 88bb2641)

## n18:0
- old record `n18_0_old.json` sha256 `7f09f247b7f47c06be74058b2fc436dcb594cb2e6da9344a0f05e1672d758e83`; new record `n18_0_new.json` sha256 `343386558c373b27021bee357789ca8e13b831f98382ee22a8cf92a8096cb7af`
- candidates old 340 / new 340; subspaces ['e1 row', 'k1 column', 'k2 row', 'k4 column', 't1 column', 't2 row']; ranks {'e1 row': 161, 'k1 column': 171, 'k2 row': 171, 'k4 column': 171, 't1 column': 119, 't2 row': 119}
- same subspaces True; same ranks True; identical sorted match lists True; exactly one match each (old) True
- unprofiled wall time old 814.9 s, new 73.7 s; new splits {'census': 69.3, 'identity_eqs': 0.6, 'index': 0.0, 'modp': 0.0, 'rank': 3.7}
- verdict: EXACT

## n18:1
- old record `n18_1_old.json` sha256 `638b4d09fd0e7dc983cac157d211792bfa719e2f0b885e5665d0fd2c6a3854a8`; new record `n18_1_new.json` sha256 `06ee8bd7fa50b0b5943453a142133e7cd033a18bf38817a5d906b57972a35927`
- candidates old 284 / new 284; subspaces ['e2 column', 'k1 row', 'k3 column', 'k4 row', 't1 row', 't3 column']; ranks {'e2 column': 161, 'k1 row': 171, 'k3 column': 171, 'k4 row': 171, 't1 row': 119, 't3 column': 119}
- same subspaces True; same ranks True; identical sorted match lists True; exactly one match each (old) True
- unprofiled wall time old 687.5 s, new 73.3 s; new splits {'census': 69.2, 'identity_eqs': 0.5, 'index': 0.0, 'modp': 0.0, 'rank': 3.5}
- verdict: EXACT

## n18:2
- old record `n18_2_old.json` sha256 `33a3430d3f15fba73cd2e7b1c973b14ec36984aeef21c96a8ad6837da62f27ac`; new record `n18_2_new.json` sha256 `4383e43d003a566eaf72981dc30d337083b4d3deb1efc0e0bbbc627926b772ff`
- candidates old 336 / new 336; subspaces ['e1 column', 'e2 row', 'k2 column', 'k3 row', 't2 column', 't3 row']; ranks {'e1 column': 161, 'e2 row': 161, 'k2 column': 171, 'k3 row': 171, 't2 column': 119, 't3 row': 119}
- same subspaces True; same ranks True; identical sorted match lists True; exactly one match each (old) True
- unprofiled wall time old 926.3 s, new 71.1 s; new splits {'census': 66.2, 'identity_eqs': 0.7, 'index': 0.0, 'modp': 0.0, 'rank': 4.2}
- verdict: EXACT

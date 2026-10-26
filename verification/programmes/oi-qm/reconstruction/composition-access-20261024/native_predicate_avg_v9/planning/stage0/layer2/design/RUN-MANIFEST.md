# Stage 0 Layer 2 run manifest (design evidence)

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

NP-AVG-1 Stage 0 Layer 2 design evidence (WIP / UNREVIEWED, not frozen): toy, planted and small-window instances, S6's carrier and v8 configuration combinatorics only; no closure on v8's configuration class (the v8 profile is refused without an authorization artifact). The quick mutant campaign is local; the full campaign is CI-only and pending owner-approved dispatch. Timing steps (calibration_planted, dryrun_v8_estimate, kappa_calibration_repeats) are not deterministic. Commit caveat (L2-R5): this evidence was produced on an uncommitted working tree; the structured files record the HEAD at run time (field commit) and tree_clean = false, so they are design evidence only. At the Layer-2 freeze the evidence is regenerated at a recorded commit.

HEAD at run: `53786e6e9e6f59347d20cac9f9875fdf7b4d8f67`; Layer-2 tree clean at run: False.

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| manifest_verify | `python3 -I -B stage0/layer2/code/l2manifest.py --verify` | 0 | 0 | True | `b988132bbbd77961eb228792ee45149d0a189d8164a06cf501f2b6cf4b683725` |
| l2_selftest | `python3 -I -B stage0/layer2/code/l2selftest.py` | 0 | 33 | True | `47811dce746544869b2ac2ab4a3eccad2e512444cd0e0b935a3c17a03cff5d82` |
| calibration_planted | `python3 -I -B stage0/layer2/code/l2calib.py --out stage0/layer2/design/toyrun/calib.json` | 0 | 10 | n/a | `2416d8729c9a4d8e7655c09f83b8ccf78741d86adb8ab28a5bbc1bcfa198a484` |
| dryrun_toy | `python3 -I -B stage0/layer2/code/l2plan.py --profile toy --calib stage0/layer2/design/toyrun/calib.json --shared-tips --out stage0/layer2/design/toyrun/dryrun.json` | 0 | 1 | True | `47a53d8277e3316cd1e8e6f482f5d4b646b8fc9db3576828d01fd9791ad0bc64` |
| dryrun_v8_plan_no_closure | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8` | 0 | 0 | True | `358c4d93c51d0a4ef99e8358a0bcaf9326b82c229402783d4d9482e493540270` |
| dryrun_v8_estimate | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8 --calib stage0/layer2/design/toyrun/calib.json` | 0 | 0 | n/a | `1e2616cb5928627f6ab05b473e668d65b7b8c22f531525def43f2143e42dc02d` |
| preflight_toy_quick | `python3 -I -B stage0/layer2/code/l2preflight.py --profile toy --workdir stage0/layer2/design/toyrun --quick` | 0 | 125 | n/a | `c1527f157c99afe9546dc8ee99b66f5cd9ad240521a3cfdbd0e4defb08d28dc6` |
| mutants_quick | `python3 -I -B stage0/layer2/code/l2mutants.py --workdir stage0/layer2/design/toyrun` | 0 | 145 | n/a | `41428d159e31601d4ef6481844d0d73f7b6c42741526cb71a338058b7cdd8663` |
| s1a_toy | `python3 -I -B stage0/layer2/code/l2s1a.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `feddf9338991f35c1003a592a486e2abb270c0bd03ac7b19c7680c29b6591b94` |
| shard_toy_0 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 0 --workdir stage0/layer2/design/toyrun` | 0 | 6 | True | `40185fe3c0d30b626b74fd0aa902955c725009c71203994ae21ca2e1513853d4` |
| shard_toy_1 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 1 --workdir stage0/layer2/design/toyrun` | 0 | 1 | True | `0c6f7129038629aec8ab04b687c0873b7dff683684a8844d8f9ab19463b65063` |
| shard_toy_2 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 2 --workdir stage0/layer2/design/toyrun` | 0 | 2 | True | `c536021b2489fe55584f9ecdf72c8f5d078fbf1b754ca8a67be12cce228aefa9` |
| shard_toy_3 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 3 --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `fbc36339987012806c1af1fd5598f48344369dd753a9c1244027281f016e7b1b` |
| merge_toy | `python3 -I -B stage0/layer2/code/l2merge.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `bd8ca82536afe94368203567f5a13a60e6bfa692b148c5eb63ebaea7fabf3d36` |
| certificate_toy | `python3 -I -B stage0/layer2/code/l2cert.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `0776b2911d40238f8064d68f7c1e378fa7cb05dc83b19b02ba58a31acedb396a` |
| crosscheck_toy_counts | `python3 -I -B stage0/layer2/design/crosscheck.py stage0/layer2/design/toyrun stage0/code-r5` | 0 | 8 | True | `e04859f9b1b820e914ad9ef0418eb33e55c40cc8e564c6033537101e980e8a05` |
| e1check_replay | `python3 -I -B stage0/layer2/design/e1check_replay.py stage0/amendments/E1-check` | 0 | 18 | True | `9b0be14fd1f35ea1edd00da5b04674cac0a424d60bfc69774cd6adbbe0487656` |
| code_r5_equivalence_quick | `python3 -I -B stage0/layer2/design/r5_equivalence.py stage0/code-r5 stage0/layer2/design/toyrun` | 0 | 43 | n/a | `cca1570baa43bff143db2fba8e2980cc768304406a36439b6b27d8a9ce6c7f5a` |
| planted_survivor_path | `python3 -I -B stage0/layer2/design/planted_shard.py stage0/layer2/code` | 0 | 1 | True | `8655262044849e40e6106ea3e45280388073e46679bbb4ec2c2e902c40d81824` |
| refusal_probe_v8 | `python3 -I -B stage0/layer2/design/refusal_probe.py stage0/layer2/code <scratch>` | 0 | 1 | True | `1682b6cda6d4b4c080d2c6caaad1187386fa667a0d750286a4ed8eb885d29f64` |
| kappa_calibration_repeats | `python3 -I -B stage0/layer2/design/kappa_calibration.py stage0/layer2/code stage0/layer2/design/kappa/calibration-repeats.json` | 0 | 137 | n/a | `1c11007ed377540e16d65fce82c9532cd13ad2c21e2ab215c377f0a8b17c7f57` |

| file | SHA-256 |
| --- | --- |
| stage0/layer2/code/LAYER2-MANIFEST.json | `a6b8d9b67941d2bfafada142b466458913870137d66907c4428cb4ce1f2eaf9e` |
| stage0/layer2/code/l2analysis.py | `0c61690071848022c6c78e6eccab1533ede41240b70aac85459876b3168e25fc` |
| stage0/layer2/code/l2auth.py | `e1be779494f3f553ccdb7102c22f394a0c122cb63502ccb398ee16aa836bcb91` |
| stage0/layer2/code/l2calib.py | `48427e257d350a279ea4430feebb9bfafe376c5e9af725c16ea49cb21a45b0e5` |
| stage0/layer2/code/l2cert.py | `021a4d50d946e456e7f6e801b2bea9b19690cb7467c40932ed7f434f732ece30` |
| stage0/layer2/code/l2config.py | `d5455e3e2ec72280b95e568a847918d33eb114ab686e9309a2f54a0c1f708f10` |
| stage0/layer2/code/l2enum.py | `7c7f78472a589dc2f57ef3067bfb67d5cc2b580e7d8b9bb45c01beee88c439d8` |
| stage0/layer2/code/l2landing.py | `0af56760310ee4bf255bc9b5bc26be9b15d8ff2662486ba1778a2fe170c0644f` |
| stage0/layer2/code/l2manifest.py | `d30c92f4eac252992c8ecbb03cb89bbb39a6a968b57f4ab359f331beceb4dea0` |
| stage0/layer2/code/l2merge.py | `881bda621718ef4f885566797f9894cc180b341e14962ce387bf6b20ae59ee77` |
| stage0/layer2/code/l2mutants.py | `73c5e2fa733844ec21af149daa81d37cb7f650453fc41504658f2563c45a90ad` |
| stage0/layer2/code/l2plan.py | `67e0603f1ed877649e6361b25aaacbb01dd1de1325c7b71b2a59ad0201513516` |
| stage0/layer2/code/l2preflight.py | `ee50c6e4f1cb1b5d7b8cf044999b43009792bb26a54bfb13c34ddc9770a18671` |
| stage0/layer2/code/l2refcheck.py | `0049d2103fa03b6a1141212da74b9945e145eeea5ebcb26b5916d78f88b07d46` |
| stage0/layer2/code/l2run.py | `f271571480a5beab8e93ff4cd65d1ece640b0c6d3c41ce650975aa363cb1f0af` |
| stage0/layer2/code/l2s1a.py | `2ef4073d8913e02f98ba01102c43053196482ffebdf873617aa7766b7d913f48` |
| stage0/layer2/code/l2selftest.py | `fe73112ab74667267f172d286a776ed001950cd76f2c6655981d33ae02cf2b32` |
| stage0/layer2/code/s0controls.py | `81994f1b8375c988f0d622d202a0896e44338ac8d08c888eaa119c3ef7f103cb` |
| stage0/layer2/code/s0geom.py | `9ab0d64cbf7efef231355a46d9264658735f314a325c02067fffabd15eba8e13` |
| stage0/layer2/code/s0native.py | `4206549e8c01d62c684d4375fb11ae79e2fe69ef059c61600ae3db04570c8526` |
| stage0/layer2/code/s0ref.py | `4aa701f44309d15546182f47625c8a0d5fff060e0273c9e8b85324560d473859` |
| stage0/layer2/code/s0s6.py | `110f275cd83edb759b40c249900bc397e1fc3accc9571add50fa8bac3e42289a` |
| stage0/layer2/code/s0symcheck.py | `ffe390ae7a7491ab32a2e08c2d739c1be3028b465cf571842198c3c487f618f2` |
| stage0/layer2/design/crosscheck.py | `bc9157104b5cc7967eb8a764c8c076b90c5b422b023a0f5ea10c6cafe505370d` |
| stage0/layer2/design/e1check_replay.py | `edf282712115413b7e8c9b7c0c46ea6638053c1b0c834424acc25aa6f64d8516` |
| stage0/layer2/design/kappa_calibration.py | `7c804037619344be5e90a5db45e34c662207355cf1ffdf7b72726aeccd53d498` |
| stage0/layer2/design/planted_shard.py | `f64186f30655cff5589cc07271f31bc0332a0373f8ecbe0444558c166fc22d8c` |
| stage0/layer2/design/r5_equivalence.py | `ca2ee6be0d6d918683e2f67072fb526459ff7a1c91ac3a8eb9502cdc7f10fc71` |
| stage0/layer2/design/refusal_probe.py | `32ebcfde74341725797e2a69a6df251c5ee9d94c40053ecc5c29de01ce4e35ba` |

| toy-run file | SHA-256 |
| --- | --- |
| stage0/layer2/design/toyrun/calib.json | `2416d8729c9a4d8e7655c09f83b8ccf78741d86adb8ab28a5bbc1bcfa198a484` |
| stage0/layer2/design/toyrun/certificate.json | `2006d16951f52007ba3afbff0631fcb029d04b83ffab9f46a986114cbca8b1b1` |
| stage0/layer2/design/toyrun/dryrun.json | `47a53d8277e3316cd1e8e6f482f5d4b646b8fc9db3576828d01fd9791ad0bc64` |
| stage0/layer2/design/toyrun/expected-controls.json | `9b422c543d3b37df988358db3d5ff2e6246427a906d925caaa80b9bafb20a14e` |
| stage0/layer2/design/toyrun/mutant-campaign.json | `41428d159e31601d4ef6481844d0d73f7b6c42741526cb71a338058b7cdd8663` |
| stage0/layer2/design/toyrun/preflight.json | `aeb5a340ecc51e7b8503a1fd808a5782bde3175db27885386d0095fe4d0553cf` |
| stage0/layer2/design/toyrun/result.O.json | `16b45f87a199e01642578f9d1ed20ba3a980d1ce0654ef446c3a1274f3fde17f` |
| stage0/layer2/design/toyrun/result.json | `16b45f87a199e01642578f9d1ed20ba3a980d1ce0654ef446c3a1274f3fde17f` |
| stage0/layer2/design/toyrun/s1a.O.json | `811633ce3b6b930d80d55ed224896a4796441dbf4064fdf172d96e300bab38ef` |
| stage0/layer2/design/toyrun/s1a.json | `811633ce3b6b930d80d55ed224896a4796441dbf4064fdf172d96e300bab38ef` |
| stage0/layer2/design/toyrun/shard-0.O.json | `2f514f5f3c5b6cae2e042816c37f9ded245390cd27eface9d802f72f247cd82a` |
| stage0/layer2/design/toyrun/shard-0.json | `2f514f5f3c5b6cae2e042816c37f9ded245390cd27eface9d802f72f247cd82a` |
| stage0/layer2/design/toyrun/shard-1.O.json | `728522ab91a3ae703eea05bac76e8ded18960f80809ad9563a608368a3b11da8` |
| stage0/layer2/design/toyrun/shard-1.json | `728522ab91a3ae703eea05bac76e8ded18960f80809ad9563a608368a3b11da8` |
| stage0/layer2/design/toyrun/shard-2.O.json | `c4ba882347f8c51c759665f9986387082f119c477ce38fcd448b4adfd8854961` |
| stage0/layer2/design/toyrun/shard-2.json | `c4ba882347f8c51c759665f9986387082f119c477ce38fcd448b4adfd8854961` |
| stage0/layer2/design/toyrun/shard-3.O.json | `067f7658d7db07f79741ff79d613e897cd58b964ed7addde2885c3b89a5c0a2b` |
| stage0/layer2/design/toyrun/shard-3.json | `067f7658d7db07f79741ff79d613e897cd58b964ed7addde2885c3b89a5c0a2b` |

| kappa calibration file | SHA-256 |
| --- | --- |
| stage0/layer2/design/kappa/calibration-repeats.json | `5a34c122e58c231c0eb464d29bafde99c89e3ffbedef1952cf8b1ea69b822815` |

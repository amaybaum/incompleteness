# Stage 0 Layer 2 run manifest (design evidence)

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

NP-AVG-1 Stage 0 Layer 2 design evidence (WIP / UNREVIEWED, not frozen): toy, planted and small-window instances, S6's carrier and v8 configuration combinatorics only; no closure on v8's configuration class (the v8 profile is refused without an authorization artifact). The quick mutant campaign is local; the full campaign is CI-only and pending owner-approved dispatch. Timing steps (calibration_planted, dryrun_v8_estimate, kappa_calibration_repeats, overhead_measure, survivor_cap_measure) are not deterministic. Commit caveat (L2-R5): this evidence was produced on an uncommitted working tree; the structured files record the HEAD at run time (field commit) and tree_clean = false, so they are design evidence only. At the Layer-2 freeze the evidence is regenerated at a recorded commit.

HEAD at run: `a782aa549061ad5417d939da932fa1c7f66ac022`; Layer-2 tree clean at run: False.

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| manifest_verify | `python3 -I -B stage0/layer2/code/l2manifest.py --verify` | 0 | 0 | True | `27ef5c7f4aaeab195a947e57c5e2cb66c007a14485386495ef1189c3e61e893d` |
| l2_selftest | `python3 -I -B stage0/layer2/code/l2selftest.py` | 0 | 37 | True | `6b804eaaa934f32aa1ed032c8f9940f6f2163be8b5f6b26a06922f64a3a516fe` |
| calibration_planted | `python3 -I -B stage0/layer2/code/l2calib.py --out stage0/layer2/design/toyrun/calib.json` | 0 | 11 | n/a | `eed82d0199ef7ce54f288261f8f56dbe81bc149463a7800c5745ca4d10d7b9f3` |
| dryrun_toy | `python3 -I -B stage0/layer2/code/l2plan.py --profile toy --calib stage0/layer2/design/toyrun/calib.json --shared-tips --out stage0/layer2/design/toyrun/dryrun.json` | 0 | 1 | True | `fcc6cacd4e296aba3624d8c2dd261a3ee514ae8be734a089664254e35c9db329` |
| dryrun_v8_plan_no_closure | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8` | 0 | 0 | True | `60d1b4e56b75769d74fb482b4cb9faa22bf936c22ed28274e8323ea5d4947609` |
| dryrun_v8_estimate | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8 --calib stage0/layer2/design/toyrun/calib.json` | 0 | 0 | n/a | `8d876c3559341dc824f7028e185c7a76f9ae6d458c04bd92b490c8e9bd15adef` |
| preflight_toy_quick | `python3 -I -B stage0/layer2/code/l2preflight.py --profile toy --workdir stage0/layer2/design/toyrun --quick` | 0 | 131 | n/a | `c1527f157c99afe9546dc8ee99b66f5cd9ad240521a3cfdbd0e4defb08d28dc6` |
| mutants_quick | `python3 -I -B stage0/layer2/code/l2mutants.py --workdir stage0/layer2/design/toyrun` | 0 | 150 | n/a | `57fa55a3acfd27285fad379d52b04e273f266dc9aea60997fc5fda5c5abd1069` |
| s1a_toy | `python3 -I -B stage0/layer2/code/l2s1a.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `feddf9338991f35c1003a592a486e2abb270c0bd03ac7b19c7680c29b6591b94` |
| shard_toy_0 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 0 --workdir stage0/layer2/design/toyrun` | 0 | 6 | True | `7523465b3b2fc69b9e63be43f338875c5b655a6072291882a33a05e527cb753d` |
| shard_toy_1 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 1 --workdir stage0/layer2/design/toyrun` | 0 | 1 | True | `2640d854c124e07324a965746f407791d077ad273753d6cbb6e4352da4b540ab` |
| shard_toy_2 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 2 --workdir stage0/layer2/design/toyrun` | 0 | 2 | True | `36caa01d8b5a7f43539cdfd7c33fbf9b3ca49572c3380a458ead5f18b53e8201` |
| shard_toy_3 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 3 --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `dc995839e7132e9509d1cdba01f0ecb62072e84eeed5976abca4700632029c56` |
| merge_toy | `python3 -I -B stage0/layer2/code/l2merge.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `bd8ca82536afe94368203567f5a13a60e6bfa692b148c5eb63ebaea7fabf3d36` |
| certificate_toy | `python3 -I -B stage0/layer2/code/l2cert.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `0776b2911d40238f8064d68f7c1e378fa7cb05dc83b19b02ba58a31acedb396a` |
| crosscheck_toy_counts | `python3 -I -B stage0/layer2/design/crosscheck.py stage0/layer2/design/toyrun stage0/code-r5` | 0 | 9 | True | `e04859f9b1b820e914ad9ef0418eb33e55c40cc8e564c6033537101e980e8a05` |
| e1check_replay | `python3 -I -B stage0/layer2/design/e1check_replay.py stage0/amendments/E1-check` | 0 | 19 | True | `9b0be14fd1f35ea1edd00da5b04674cac0a424d60bfc69774cd6adbbe0487656` |
| code_r5_equivalence_quick | `python3 -I -B stage0/layer2/design/r5_equivalence.py stage0/code-r5 stage0/layer2/design/toyrun` | 0 | 42 | n/a | `cca1570baa43bff143db2fba8e2980cc768304406a36439b6b27d8a9ce6c7f5a` |
| planted_survivor_path | `python3 -I -B stage0/layer2/design/planted_shard.py stage0/layer2/code` | 0 | 1 | True | `f601b2226b0e3a06d38cb6ef10463c9b4473341651936620e5e09b80cfdcd247` |
| refusal_probe_v8 | `python3 -I -B stage0/layer2/design/refusal_probe.py stage0/layer2/code <scratch>` | 0 | 1 | True | `1682b6cda6d4b4c080d2c6caaad1187386fa667a0d750286a4ed8eb885d29f64` |
| kappa_calibration_repeats | `python3 -I -B stage0/layer2/design/kappa_calibration.py stage0/layer2/code stage0/layer2/design/kappa/calibration-repeats.json` | 0 | 136 | n/a | `f3710dc655289690f71013f3dd49afd47c2f7e7c07c7b50f23b22311f4f4d3f9` |
| overhead_measure | `python3 -I -B stage0/layer2/design/overhead_measure.py stage0/layer2/code stage0/layer2/design/overhead/overhead.json` | 0 | 7 | n/a | `a8978345cb2ed3a8990d5cba5e443b03bfbe1398c83c4984ddd34e390891eae6` |
| survivor_cap_measure | `python3 -I -B stage0/layer2/design/survivor_cap_measure.py stage0/layer2/code stage0/layer2/design/kappa/calibration-repeats.json stage0/layer2/design/overhead/survivor-cap.json` | 0 | 46 | n/a | `0057668bc0d8ca551b77869aa1bcb79700b4f5fa6acd04c05f775bc266a6ae5d` |
| ci_calibration_local_check | `python3 -I -B stage0/layer2/design/ci_local_check.py stage0/layer2/ci <scratch>` | 0 | 11 | True | `71f7bc57e4e1c221c31320028eaa6e19d2efd9f3e829097cd1cdf41c377db4ff` |

| file | SHA-256 |
| --- | --- |
| stage0/layer2/code/LAYER2-MANIFEST.json | `65e70d91b7f7c34cd22b282ca1804445cf5cc93ba7b8a4b33f93a21297a52260` |
| stage0/layer2/code/l2analysis.py | `0c61690071848022c6c78e6eccab1533ede41240b70aac85459876b3168e25fc` |
| stage0/layer2/code/l2auth.py | `e1be779494f3f553ccdb7102c22f394a0c122cb63502ccb398ee16aa836bcb91` |
| stage0/layer2/code/l2calib.py | `48427e257d350a279ea4430feebb9bfafe376c5e9af725c16ea49cb21a45b0e5` |
| stage0/layer2/code/l2cert.py | `37a8bda45bf1f1d73ac67d82697b419366fd157b7ff76616ce7b9aaabffa3a83` |
| stage0/layer2/code/l2config.py | `0268ba764d0b8f18ee4c9e334e4d177a113533f0cced0ff011c3612cee6af5d8` |
| stage0/layer2/code/l2enum.py | `ab4e8120a14ddb936b63619cd160198982ad2785f6ed6dda034631d3ce15ad5b` |
| stage0/layer2/code/l2landing.py | `0af56760310ee4bf255bc9b5bc26be9b15d8ff2662486ba1778a2fe170c0644f` |
| stage0/layer2/code/l2manifest.py | `d30c92f4eac252992c8ecbb03cb89bbb39a6a968b57f4ab359f331beceb4dea0` |
| stage0/layer2/code/l2merge.py | `53b86107966877b10aaf5ef08664d3a90c19be0fff66ad9f6493d29b35e5af74` |
| stage0/layer2/code/l2mutants.py | `73c5e2fa733844ec21af149daa81d37cb7f650453fc41504658f2563c45a90ad` |
| stage0/layer2/code/l2plan.py | `26727c440fc0497bf9802224e592574d7a2bcf6044ea74e9d3fcca41d1562cf2` |
| stage0/layer2/code/l2preflight.py | `ee50c6e4f1cb1b5d7b8cf044999b43009792bb26a54bfb13c34ddc9770a18671` |
| stage0/layer2/code/l2refcheck.py | `0049d2103fa03b6a1141212da74b9945e145eeea5ebcb26b5916d78f88b07d46` |
| stage0/layer2/code/l2run.py | `8c092a6a1a7f120b02984e376d230521c580d65c64e91eab70f806bffc3ae9d4` |
| stage0/layer2/code/l2s1a.py | `2ef4073d8913e02f98ba01102c43053196482ffebdf873617aa7766b7d913f48` |
| stage0/layer2/code/l2selftest.py | `f386bf9e7bf05e90253db40b2abebcd28a16cfab043eac22e9e49ebeba0d5cee` |
| stage0/layer2/code/s0controls.py | `81994f1b8375c988f0d622d202a0896e44338ac8d08c888eaa119c3ef7f103cb` |
| stage0/layer2/code/s0geom.py | `9ab0d64cbf7efef231355a46d9264658735f314a325c02067fffabd15eba8e13` |
| stage0/layer2/code/s0native.py | `4206549e8c01d62c684d4375fb11ae79e2fe69ef059c61600ae3db04570c8526` |
| stage0/layer2/code/s0ref.py | `4aa701f44309d15546182f47625c8a0d5fff060e0273c9e8b85324560d473859` |
| stage0/layer2/code/s0s6.py | `110f275cd83edb759b40c249900bc397e1fc3accc9571add50fa8bac3e42289a` |
| stage0/layer2/code/s0symcheck.py | `ffe390ae7a7491ab32a2e08c2d739c1be3028b465cf571842198c3c487f618f2` |
| stage0/layer2/design/ci_local_check.py | `c9b895a39c0d01791d3c8f396727780001f88cf7ee8e6a90002efe9168ca8117` |
| stage0/layer2/design/crosscheck.py | `bc9157104b5cc7967eb8a764c8c076b90c5b422b023a0f5ea10c6cafe505370d` |
| stage0/layer2/design/e1check_replay.py | `edf282712115413b7e8c9b7c0c46ea6638053c1b0c834424acc25aa6f64d8516` |
| stage0/layer2/design/kappa_calibration.py | `076f2cafa94217b2fac82875621b07bfff32463cfe0739d98974594bea8120a4` |
| stage0/layer2/design/overhead_measure.py | `5362455b72f3320439faf5b0e8677e0a52ea1d3a0e5c98e89bca877773f0adfe` |
| stage0/layer2/design/planted_shard.py | `f64186f30655cff5589cc07271f31bc0332a0373f8ecbe0444558c166fc22d8c` |
| stage0/layer2/design/r5_equivalence.py | `ca2ee6be0d6d918683e2f67072fb526459ff7a1c91ac3a8eb9502cdc7f10fc71` |
| stage0/layer2/design/refusal_probe.py | `32ebcfde74341725797e2a69a6df251c5ee9d94c40053ecc5c29de01ce4e35ba` |
| stage0/layer2/design/survivor_cap_measure.py | `37f58c4a737d9c2c85c84096b2fb773445b63def831f07332d744ddd3bbbbaba` |
| stage0/layer2/ci/calib_aggregate.py | `4a00736e34b8483cd5dc260446989c43b8a636e6431326d5765278dc8144fd3f` |
| stage0/layer2/ci/calib_ci.py | `305a86c6fc7b095718a955f431642970c2e8efa52645c340b5736e1f2fd9829f` |
| stage0/layer2/ci/np-avg-1-stage0-planted-calibration.yml | `59d66f723978e670967fce38ca97daca2b31ae670a52d9d5c573ba4d2281351a` |

| toy-run file | SHA-256 |
| --- | --- |
| stage0/layer2/design/toyrun/calib.json | `eed82d0199ef7ce54f288261f8f56dbe81bc149463a7800c5745ca4d10d7b9f3` |
| stage0/layer2/design/toyrun/certificate.json | `66f0633f132e78e2449ddde03972df4842beb8d4c99b2e63bbf4c079e05dc4cc` |
| stage0/layer2/design/toyrun/dryrun.json | `fcc6cacd4e296aba3624d8c2dd261a3ee514ae8be734a089664254e35c9db329` |
| stage0/layer2/design/toyrun/expected-controls.json | `9b422c543d3b37df988358db3d5ff2e6246427a906d925caaa80b9bafb20a14e` |
| stage0/layer2/design/toyrun/mutant-campaign.json | `57fa55a3acfd27285fad379d52b04e273f266dc9aea60997fc5fda5c5abd1069` |
| stage0/layer2/design/toyrun/preflight.json | `34ad72266efd50d70eb7999b2c564f9906afcd723443fa0e016cb90f28811b09` |
| stage0/layer2/design/toyrun/result.O.json | `b63b25164f3eb1ac98628739a5a7712a9f4da88e335c9cf8bf44889e3f842c33` |
| stage0/layer2/design/toyrun/result.json | `b63b25164f3eb1ac98628739a5a7712a9f4da88e335c9cf8bf44889e3f842c33` |
| stage0/layer2/design/toyrun/s1a.O.json | `e29a1a04b29c83cd698ab6b4139c8c706b3cb850b3ee055d953ee090232a1053` |
| stage0/layer2/design/toyrun/s1a.json | `e29a1a04b29c83cd698ab6b4139c8c706b3cb850b3ee055d953ee090232a1053` |
| stage0/layer2/design/toyrun/shard-0.O.json | `ebf20219ac16cfa7930fb85f6a2443632121c053fc1e8abead4b1a3a2e53e72f` |
| stage0/layer2/design/toyrun/shard-0.json | `ebf20219ac16cfa7930fb85f6a2443632121c053fc1e8abead4b1a3a2e53e72f` |
| stage0/layer2/design/toyrun/shard-1.O.json | `949a7257346776cd76bdcbb73f79b44746b13c82a04eaff116a6b0df7dc0d909` |
| stage0/layer2/design/toyrun/shard-1.json | `949a7257346776cd76bdcbb73f79b44746b13c82a04eaff116a6b0df7dc0d909` |
| stage0/layer2/design/toyrun/shard-2.O.json | `742a82dc61126480c362480cb7de3304cea24376a182ae0d9b4d7b045dd510f6` |
| stage0/layer2/design/toyrun/shard-2.json | `742a82dc61126480c362480cb7de3304cea24376a182ae0d9b4d7b045dd510f6` |
| stage0/layer2/design/toyrun/shard-3.O.json | `8ea77fa3030be4825b76c715a879a8da39910ac1ba40e18b91bb64ec3abf1f5d` |
| stage0/layer2/design/toyrun/shard-3.json | `8ea77fa3030be4825b76c715a879a8da39910ac1ba40e18b91bb64ec3abf1f5d` |

| kappa calibration file | SHA-256 |
| --- | --- |
| stage0/layer2/design/kappa/calibration-repeats.json | `9bf67c670a68a979cb49561a6d9490959511e1fc9a4549c65a48583deb23a710` |
| stage0/layer2/design/overhead/overhead.json | `a8978345cb2ed3a8990d5cba5e443b03bfbe1398c83c4984ddd34e390891eae6` |
| stage0/layer2/design/overhead/survivor-cap.json | `1cd10da2f9ff21987f95de3295b8bd0208130f9575712776e845ef9dc45e1213` |

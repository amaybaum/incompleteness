# Stage 0 Layer 2 run manifest (design evidence)

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

NP-AVG-1 Stage 0 Layer 2 design evidence (WIP / UNREVIEWED, not frozen): toy, planted and small-window instances, S6's carrier and v8 configuration combinatorics only; no closure on v8's configuration class (the v8 profile is refused without an authorization artifact). The quick mutant campaign is local; the full campaign is CI-only and pending owner-approved dispatch.

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| manifest_verify | `python3 -I -B stage0/layer2/code/l2manifest.py --verify` | 0 | 0 | True | `0a3180b65a29688328e21a1227ed6e02e2b12d42df7064d6009aa131b17f9d8f` |
| l2_selftest | `python3 -I -B stage0/layer2/code/l2selftest.py` | 0 | 5 | True | `6f8f47e30d58edb84237ee3c6171236998f88f241a9277ab2c3b489129add20d` |
| dryrun_toy | `python3 -I -B stage0/layer2/code/l2plan.py --profile toy --out stage0/layer2/design/toyrun/dryrun.json` | 0 | 0 | True | `c2a8dfe911a548c30ef392fcf0028fa075eb5b9eeae9402698304a7a55a75834` |
| dryrun_v8_plan_no_closure | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8` | 0 | 0 | True | `c1451147515d301e584915022cb5d5eba644176f3bc51a942cc545d271389df4` |
| calibration_planted | `python3 -I -B stage0/layer2/code/l2calib.py --out stage0/layer2/design/toyrun/calib.json` | 0 | 11 | n/a | `f94d41fda14310722a59c6a0dab234395462bfd9cca023b3512e0780e0e0f672` |
| dryrun_v8_estimate | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8 --calib stage0/layer2/design/toyrun/calib.json` | 0 | 0 | n/a | `46ff4abd24173ad55fbdba6b8d5c60f169a2db82db9ce85bb23a87b4d30729ce` |
| preflight_toy_quick | `python3 -I -B stage0/layer2/code/l2preflight.py --profile toy --workdir stage0/layer2/design/toyrun --quick` | 0 | 99 | n/a | `c1527f157c99afe9546dc8ee99b66f5cd9ad240521a3cfdbd0e4defb08d28dc6` |
| mutants_quick | `python3 -I -B stage0/layer2/code/l2mutants.py --workdir stage0/layer2/design/toyrun` | 0 | 180 | n/a | `239d884d3ecd3435529a393c341ca9c6a5f260e9e3a486c87978bcc5b23dd9bf` |
| s1a_toy | `python3 -I -B stage0/layer2/code/l2s1a.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `feddf9338991f35c1003a592a486e2abb270c0bd03ac7b19c7680c29b6591b94` |
| shard_toy_0 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 0 --workdir stage0/layer2/design/toyrun` | 0 | 6 | True | `9e8049052abb9ff0d01edfe4de66d17df57131912d53ce564b6bb43ab16cc69e` |
| shard_toy_1 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 1 --workdir stage0/layer2/design/toyrun` | 0 | 1 | True | `d80e3bcdfdae647e5fbe3c574c3ffc15fc96afb00b9c866295da049c83519fc4` |
| shard_toy_2 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 2 --workdir stage0/layer2/design/toyrun` | 0 | 2 | True | `580feba77b2c5f5633b92066eb130b2c5c4bbbbf6c642412bcd79326d422cc5c` |
| shard_toy_3 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 3 --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `9595d5a4aaea50e2667838543fabb74f4e93a6897eca0a51620a6f87a460b7a1` |
| merge_toy | `python3 -I -B stage0/layer2/code/l2merge.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `bd8ca82536afe94368203567f5a13a60e6bfa692b148c5eb63ebaea7fabf3d36` |
| certificate_toy | `python3 -I -B stage0/layer2/code/l2cert.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `0776b2911d40238f8064d68f7c1e378fa7cb05dc83b19b02ba58a31acedb396a` |
| crosscheck_toy_counts | `python3 -I -B stage0/layer2/design/crosscheck.py stage0/layer2/design/toyrun` | 0 | 0 | True | `695ab124ecc42b2c774f99501527674903778acac128c46a31c889b55389e534` |
| code_r5_equivalence_quick | `python3 -I -B stage0/layer2/design/r5_equivalence.py stage0/code-r5 stage0/layer2/design/toyrun` | 0 | 42 | n/a | `cca1570baa43bff143db2fba8e2980cc768304406a36439b6b27d8a9ce6c7f5a` |
| planted_survivor_path | `python3 -I -B stage0/layer2/design/planted_shard.py stage0/layer2/code` | 0 | 1 | True | `d33a4cf31036c079294710b81a333c29466f288f4a51fe203d94132320b665c9` |
| refusal_probe_v8 | `python3 -I -B stage0/layer2/design/refusal_probe.py stage0/layer2/code <scratch>` | 0 | 1 | True | `6188755b634d40e1a85ba4a5a683fe1521265b328370a1f9d148600d4b0ea94c` |

| file | SHA-256 |
| --- | --- |
| stage0/layer2/code/LAYER2-MANIFEST.json | `5f38b7adeeeb95a1d11f93f9adbba51333a5543ad6ee0f5e2b54dd838e6a3e30` |
| stage0/layer2/code/l2analysis.py | `2b58a175b24ba3f6d63e6eade4f0fa02cc07fcfd18f18a29b4c692d97d92dc7d` |
| stage0/layer2/code/l2auth.py | `6f8aadfc59921d1f7975a2fb31fffd4f522da594412fce4ebe4099fcdc43631a` |
| stage0/layer2/code/l2calib.py | `48427e257d350a279ea4430feebb9bfafe376c5e9af725c16ea49cb21a45b0e5` |
| stage0/layer2/code/l2cert.py | `ff4d84544b393b5729d85cfc9fbfc24f8ece9850d201a126af701e22360fc700` |
| stage0/layer2/code/l2config.py | `da8122819389b72b3cc38b45ebe82231d2430bd8051ee83e0f5a2ed73058af69` |
| stage0/layer2/code/l2enum.py | `eb6f328b8659cfd307bd8194920836f6cad77cb5308e48efaafe6c0e4a548561` |
| stage0/layer2/code/l2manifest.py | `d30c92f4eac252992c8ecbb03cb89bbb39a6a968b57f4ab359f331beceb4dea0` |
| stage0/layer2/code/l2merge.py | `647201ef1a663f2aeb079bc41b48eb54d6459db8bfcf01a318c16843153bf563` |
| stage0/layer2/code/l2mutants.py | `99b0645ef96446a855943fb508dc43711741d2b7ec15bdba62e9573012dec9e8` |
| stage0/layer2/code/l2plan.py | `33b71572111e9dfe8ce0bffce77c91d365ceba200f4b46ed80ff9e932985491b` |
| stage0/layer2/code/l2preflight.py | `7a66757cf911bc45555909ee20773b3c33fe34ec0c28b975547bc45bcf27e6f5` |
| stage0/layer2/code/l2refcheck.py | `b4f9dfdb8331c42e5ae6779b6ff332f6593052dc39edd307fabb3d482a6d750c` |
| stage0/layer2/code/l2run.py | `a194f22ccbfc0a43c170c1819c646004877402ebdcd1d81bc411dccce6dd3ef2` |
| stage0/layer2/code/l2s1a.py | `dbae348c82d1a929e3e28d8a9eabad57baa678ec276f3bfbb9ebf5990618a26d` |
| stage0/layer2/code/l2selftest.py | `76e1ee13daa67a02e700eddb5b403cdfdd4d9e7357ce2ee4f1f696a6ad62c2dd` |
| stage0/layer2/code/s0controls.py | `81994f1b8375c988f0d622d202a0896e44338ac8d08c888eaa119c3ef7f103cb` |
| stage0/layer2/code/s0geom.py | `3d0888fe653b091153ffe302eb9ea7980182ffa31f6cb4314ae60fc9a91c8a88` |
| stage0/layer2/code/s0native.py | `4206549e8c01d62c684d4375fb11ae79e2fe69ef059c61600ae3db04570c8526` |
| stage0/layer2/code/s0ref.py | `491bc4df2c298814024932a1dcbd22c7e869200903f2fb1e92a7d47fc41055a8` |
| stage0/layer2/code/s0s6.py | `110f275cd83edb759b40c249900bc397e1fc3accc9571add50fa8bac3e42289a` |
| stage0/layer2/code/s0symcheck.py | `ffe390ae7a7491ab32a2e08c2d739c1be3028b465cf571842198c3c487f618f2` |
| stage0/layer2/design/crosscheck.py | `a3b963ad40966f268d117c4737530fc68f8c20f7c4ba7f374dca027b037d9d0a` |
| stage0/layer2/design/planted_shard.py | `40e3ef512fb1da4f12544e843e35278064c428f01c67e3c3fb404a3809adc45b` |
| stage0/layer2/design/r5_equivalence.py | `ca2ee6be0d6d918683e2f67072fb526459ff7a1c91ac3a8eb9502cdc7f10fc71` |
| stage0/layer2/design/refusal_probe.py | `29670a0a6f6dbb8d6b54919922136d1669f3f1583740675d156e3f476a9cc149` |

| toy-run file | SHA-256 |
| --- | --- |
| stage0/layer2/design/toyrun/calib.json | `f94d41fda14310722a59c6a0dab234395462bfd9cca023b3512e0780e0e0f672` |
| stage0/layer2/design/toyrun/certificate.json | `ecfc46cd6a73e0a6e1190717a59a8b41a5a943d0772cb856b213a693058e8093` |
| stage0/layer2/design/toyrun/dryrun.json | `c2a8dfe911a548c30ef392fcf0028fa075eb5b9eeae9402698304a7a55a75834` |
| stage0/layer2/design/toyrun/expected-controls.json | `40c5dfb8ac2d4463de93de1faa8dd3c74cac76e08a92fd2f1e39cd6284ed97ac` |
| stage0/layer2/design/toyrun/mutant-campaign.json | `239d884d3ecd3435529a393c341ca9c6a5f260e9e3a486c87978bcc5b23dd9bf` |
| stage0/layer2/design/toyrun/preflight.json | `529fd601b8f7a0ee7cc781ee3b99746dc8afe92162d39c1c674b4d0342831c87` |
| stage0/layer2/design/toyrun/result.O.json | `f89daaca5eb5265b373c732854956c78eaeb4afeaed4cf410ad63a127990be4a` |
| stage0/layer2/design/toyrun/result.json | `f89daaca5eb5265b373c732854956c78eaeb4afeaed4cf410ad63a127990be4a` |
| stage0/layer2/design/toyrun/s1a.O.json | `3aa6206a737a47af788dbc5bcf470df7ed2da3f4896e17c810936c40c2478e1d` |
| stage0/layer2/design/toyrun/s1a.json | `3aa6206a737a47af788dbc5bcf470df7ed2da3f4896e17c810936c40c2478e1d` |
| stage0/layer2/design/toyrun/shard-0.O.json | `0066eb0e117f50c44f058410cb712959309cebdb6d6d0d41b1f329bb7e542b66` |
| stage0/layer2/design/toyrun/shard-0.json | `0066eb0e117f50c44f058410cb712959309cebdb6d6d0d41b1f329bb7e542b66` |
| stage0/layer2/design/toyrun/shard-1.O.json | `79c3ee2e252aab7c95c8eb530267e5a20f24a4ea762cf6e162a4321f8bf114dd` |
| stage0/layer2/design/toyrun/shard-1.json | `79c3ee2e252aab7c95c8eb530267e5a20f24a4ea762cf6e162a4321f8bf114dd` |
| stage0/layer2/design/toyrun/shard-2.O.json | `207048694ffa62a00b4e8c04d0c843d1609695b721193604ae8561aa5393334c` |
| stage0/layer2/design/toyrun/shard-2.json | `207048694ffa62a00b4e8c04d0c843d1609695b721193604ae8561aa5393334c` |
| stage0/layer2/design/toyrun/shard-3.O.json | `9a7ffd99ebf1c81be1f8c0724b97dbad929dd26c9222267cf41c04ab28b95cdd` |
| stage0/layer2/design/toyrun/shard-3.json | `9a7ffd99ebf1c81be1f8c0724b97dbad929dd26c9222267cf41c04ab28b95cdd` |

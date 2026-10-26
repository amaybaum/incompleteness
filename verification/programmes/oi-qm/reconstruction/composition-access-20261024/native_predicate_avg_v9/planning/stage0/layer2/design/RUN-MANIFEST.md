# Stage 0 Layer 2 run manifest (design evidence)

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

NP-AVG-1 Stage 0 Layer 2 design evidence (WIP / UNREVIEWED, not frozen): toy, planted and small-window instances, S6's carrier and v8 configuration combinatorics only; no closure on v8's configuration class (the v8 profile is refused without an authorization artifact). The quick mutant campaign is local; the full campaign is CI-only and pending owner-approved dispatch. Commit caveat (L2-R5): this evidence was produced on an uncommitted working tree; the structured files record the HEAD at run time (field commit) and tree_clean = false, so they are design evidence only. At the Layer-2 freeze the evidence is regenerated at a recorded commit.

HEAD at run: `a63db7ba5852969b324c1932d4f2495fe601dcdb`; Layer-2 tree clean at run: False.

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| manifest_verify | `python3 -I -B stage0/layer2/code/l2manifest.py --verify` | 0 | 0 | True | `4dc246f0a8352311272e522f7a872fddaa3848b87d4272f67d186b00e4d14af0` |
| l2_selftest | `python3 -I -B stage0/layer2/code/l2selftest.py` | 0 | 5 | True | `4d84403b34e52d2e4edc27461d136fcfc933d9d4aaad3eaf556b45cf85f8a9c8` |
| calibration_planted | `python3 -I -B stage0/layer2/code/l2calib.py --out stage0/layer2/design/toyrun/calib.json` | 0 | 11 | n/a | `60e2a38a4e55e5409c6a4d6f24d8fcb6eb6542161f18f96bb4d4abcb693f8cff` |
| dryrun_toy | `python3 -I -B stage0/layer2/code/l2plan.py --profile toy --calib stage0/layer2/design/toyrun/calib.json --shared-tips --out stage0/layer2/design/toyrun/dryrun.json` | 0 | 0 | True | `b0c06aceb0038628381a84283816e9b760c34942b5788478df8d91d68ebc5675` |
| dryrun_v8_plan_no_closure | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8` | 0 | 0 | True | `f32cf58a2e810a85aaf336c94deb87bd2867c6284a095d38ad10e7a0e39e3df5` |
| dryrun_v8_estimate | `python3 -I -B stage0/layer2/code/l2plan.py --profile v8 --calib stage0/layer2/design/toyrun/calib.json` | 0 | 0 | n/a | `22ba0a01b1575a94936589ba8353d0556a4092370a5509d0e2d51f9285990923` |
| preflight_toy_quick | `python3 -I -B stage0/layer2/code/l2preflight.py --profile toy --workdir stage0/layer2/design/toyrun --quick` | 0 | 95 | n/a | `c1527f157c99afe9546dc8ee99b66f5cd9ad240521a3cfdbd0e4defb08d28dc6` |
| mutants_quick | `python3 -I -B stage0/layer2/code/l2mutants.py --workdir stage0/layer2/design/toyrun` | 0 | 197 | n/a | `cd8d07c7cc2102cdfd0cfa983945103a0a4ca5d65c500a16e68c279aa6a2400c` |
| s1a_toy | `python3 -I -B stage0/layer2/code/l2s1a.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `feddf9338991f35c1003a592a486e2abb270c0bd03ac7b19c7680c29b6591b94` |
| shard_toy_0 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 0 --workdir stage0/layer2/design/toyrun` | 0 | 5 | True | `51790128a65249b33abf7e757b737842d6213ffcdb0862c74c746a952d671d31` |
| shard_toy_1 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 1 --workdir stage0/layer2/design/toyrun` | 0 | 1 | True | `2df7e7fc93b031964f52720eeedc6adff4343f7625ca9f3012f19f3998088177` |
| shard_toy_2 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 2 --workdir stage0/layer2/design/toyrun` | 0 | 1 | True | `55a1cb8ac3e51fbe85b9ff47801edc8bc1c6fef67f5bb3b2ff23c21389728367` |
| shard_toy_3 | `python3 -I -B stage0/layer2/code/l2enum.py --profile toy --shard 3 --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `9148d0133142cd637daf95771638d3e4afcaeb40db5badd4c2d09548ed03c6b2` |
| merge_toy | `python3 -I -B stage0/layer2/code/l2merge.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `bd8ca82536afe94368203567f5a13a60e6bfa692b148c5eb63ebaea7fabf3d36` |
| certificate_toy | `python3 -I -B stage0/layer2/code/l2cert.py --profile toy --workdir stage0/layer2/design/toyrun` | 0 | 0 | True | `0776b2911d40238f8064d68f7c1e378fa7cb05dc83b19b02ba58a31acedb396a` |
| crosscheck_toy_counts | `python3 -I -B stage0/layer2/design/crosscheck.py stage0/layer2/design/toyrun` | 0 | 0 | True | `695ab124ecc42b2c774f99501527674903778acac128c46a31c889b55389e534` |
| code_r5_equivalence_quick | `python3 -I -B stage0/layer2/design/r5_equivalence.py stage0/code-r5 stage0/layer2/design/toyrun` | 0 | 39 | n/a | `cca1570baa43bff143db2fba8e2980cc768304406a36439b6b27d8a9ce6c7f5a` |
| planted_survivor_path | `python3 -I -B stage0/layer2/design/planted_shard.py stage0/layer2/code` | 0 | 1 | True | `e0cc6cb7dc099458ddfe468eb3b2516573137e26e571cdaef09dd2b800d37a43` |
| refusal_probe_v8 | `python3 -I -B stage0/layer2/design/refusal_probe.py stage0/layer2/code <scratch>` | 0 | 1 | True | `5685420a3c41e18a37e26dd562255209a8cadd3ea8baf2666bab89d8c8b7336f` |

| file | SHA-256 |
| --- | --- |
| stage0/layer2/code/LAYER2-MANIFEST.json | `5769320f3752ff5a5971162e3a19938049a829c2df543a0b27607e93d28caeb9` |
| stage0/layer2/code/l2analysis.py | `2b58a175b24ba3f6d63e6eade4f0fa02cc07fcfd18f18a29b4c692d97d92dc7d` |
| stage0/layer2/code/l2auth.py | `e1be779494f3f553ccdb7102c22f394a0c122cb63502ccb398ee16aa836bcb91` |
| stage0/layer2/code/l2calib.py | `48427e257d350a279ea4430feebb9bfafe376c5e9af725c16ea49cb21a45b0e5` |
| stage0/layer2/code/l2cert.py | `d39b3856b998f42716c846ab6cba2bb116e173e966789e10327feef371c603bd` |
| stage0/layer2/code/l2config.py | `c5e3a24954501b95c36d54e53c87eebee6b3514760f69c7adf5c8622357182c5` |
| stage0/layer2/code/l2enum.py | `51ef53bfa4dfd15997320cafe8b24da1a41f8c76448e004f8acb79a0d24d411e` |
| stage0/layer2/code/l2landing.py | `0af56760310ee4bf255bc9b5bc26be9b15d8ff2662486ba1778a2fe170c0644f` |
| stage0/layer2/code/l2manifest.py | `d30c92f4eac252992c8ecbb03cb89bbb39a6a968b57f4ab359f331beceb4dea0` |
| stage0/layer2/code/l2merge.py | `80b5aa92411c660469ef5d99a9611b8156d73466727fa90b98ada009b55772cc` |
| stage0/layer2/code/l2mutants.py | `99b0645ef96446a855943fb508dc43711741d2b7ec15bdba62e9573012dec9e8` |
| stage0/layer2/code/l2plan.py | `52ff47469ad6fe5fe6e8457517b366f53bc8c5ad8fe11dc149608e516b66549d` |
| stage0/layer2/code/l2preflight.py | `ec919bbd14da0731433de4df0c4723035fbadfb934b757b6fe15603c71babadb` |
| stage0/layer2/code/l2refcheck.py | `0f80b0afa068170088e3ed0f853301afd01d0df98b3d3c4726586512b52317a8` |
| stage0/layer2/code/l2run.py | `17f744a9ee0a71176a51e5ab887c46a86b98ae9bd1a0a42f01743d5aed157f3a` |
| stage0/layer2/code/l2s1a.py | `d6ee05e082db7982e180097037014f24befcc380c101a37257ef9b8f7cc29385` |
| stage0/layer2/code/l2selftest.py | `1e820347d8d3cc5298caf1080ac025a3360376076cd496daa7315aa2c6d11345` |
| stage0/layer2/code/s0controls.py | `81994f1b8375c988f0d622d202a0896e44338ac8d08c888eaa119c3ef7f103cb` |
| stage0/layer2/code/s0geom.py | `9ab0d64cbf7efef231355a46d9264658735f314a325c02067fffabd15eba8e13` |
| stage0/layer2/code/s0native.py | `4206549e8c01d62c684d4375fb11ae79e2fe69ef059c61600ae3db04570c8526` |
| stage0/layer2/code/s0ref.py | `4aa701f44309d15546182f47625c8a0d5fff060e0273c9e8b85324560d473859` |
| stage0/layer2/code/s0s6.py | `110f275cd83edb759b40c249900bc397e1fc3accc9571add50fa8bac3e42289a` |
| stage0/layer2/code/s0symcheck.py | `ffe390ae7a7491ab32a2e08c2d739c1be3028b465cf571842198c3c487f618f2` |
| stage0/layer2/design/crosscheck.py | `a3b963ad40966f268d117c4737530fc68f8c20f7c4ba7f374dca027b037d9d0a` |
| stage0/layer2/design/planted_shard.py | `e86df3d274540b43e8db73e738a12a8dbe6ba0b74578bd305a1dd827e5a4a340` |
| stage0/layer2/design/r5_equivalence.py | `ca2ee6be0d6d918683e2f67072fb526459ff7a1c91ac3a8eb9502cdc7f10fc71` |
| stage0/layer2/design/refusal_probe.py | `3384a3847e47a5a2eb8a3055625f6bccf9bad580a0ae3a7daaf6afeecd70b7d2` |

| toy-run file | SHA-256 |
| --- | --- |
| stage0/layer2/design/toyrun/calib.json | `60e2a38a4e55e5409c6a4d6f24d8fcb6eb6542161f18f96bb4d4abcb693f8cff` |
| stage0/layer2/design/toyrun/certificate.json | `d00017cf9807606cd537aba55e97fa1d724c16ea236ba7a06cc151a4f3d1f791` |
| stage0/layer2/design/toyrun/dryrun.json | `b0c06aceb0038628381a84283816e9b760c34942b5788478df8d91d68ebc5675` |
| stage0/layer2/design/toyrun/expected-controls.json | `40c5dfb8ac2d4463de93de1faa8dd3c74cac76e08a92fd2f1e39cd6284ed97ac` |
| stage0/layer2/design/toyrun/mutant-campaign.json | `cd8d07c7cc2102cdfd0cfa983945103a0a4ca5d65c500a16e68c279aa6a2400c` |
| stage0/layer2/design/toyrun/preflight.json | `cd411d0f6e9727d5432fa76c4ab8f35ff7fe251f2e0d8d90ccb111e12bbf773e` |
| stage0/layer2/design/toyrun/result.O.json | `d427f4523f1f3371f97317e4930fc8e01462bc77a81c83fa5936ec1236071213` |
| stage0/layer2/design/toyrun/result.json | `d427f4523f1f3371f97317e4930fc8e01462bc77a81c83fa5936ec1236071213` |
| stage0/layer2/design/toyrun/s1a.O.json | `73cc58f1da7f58c262632dda60bfb21d6cab04439e22926e05784a90a6a19a2d` |
| stage0/layer2/design/toyrun/s1a.json | `73cc58f1da7f58c262632dda60bfb21d6cab04439e22926e05784a90a6a19a2d` |
| stage0/layer2/design/toyrun/shard-0.O.json | `f7f70fe48269d226e07262d8d59547d7557cb50aa48fac65a85bad62de45604a` |
| stage0/layer2/design/toyrun/shard-0.json | `f7f70fe48269d226e07262d8d59547d7557cb50aa48fac65a85bad62de45604a` |
| stage0/layer2/design/toyrun/shard-1.O.json | `a87584fd2336266b41cb0fe3024bcd3ceebf4ee9755c09129ed3472a716557e3` |
| stage0/layer2/design/toyrun/shard-1.json | `a87584fd2336266b41cb0fe3024bcd3ceebf4ee9755c09129ed3472a716557e3` |
| stage0/layer2/design/toyrun/shard-2.O.json | `2c674bfa9e4447c82d17756300161eed71832054e47cc3198e054873ec696c21` |
| stage0/layer2/design/toyrun/shard-2.json | `2c674bfa9e4447c82d17756300161eed71832054e47cc3198e054873ec696c21` |
| stage0/layer2/design/toyrun/shard-3.O.json | `d73dc1f723326fbf529d6572ad9ff032912209818668e5440ef5807141dd8a3b` |
| stage0/layer2/design/toyrun/shard-3.json | `d73dc1f723326fbf529d6572ad9ff032912209818668e5440ef5807141dd8a3b` |

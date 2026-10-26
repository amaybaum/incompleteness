# Stage 0 run manifest

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

toys, planted sets, small exhaustive windows and the S6 reference structure only; v8 configuration class not run (s0geom refuses it).

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| controls_frozen_full | `/usr/bin/python3 -I -B stage0-code/s0controls.py` | 0 | 73 | True | `cc01c766e8a8f0eac767faf01f68a3c58e7f3b79aaa893b4968b6041a42b582c` |
| s6_po8_proofcheck | `/usr/bin/python3 -I -B stage0-code/s0s6.py` | 0 | 17 | True | `ebecfa9687e9e45e35ae979b1f3aa6d151c86ac7c2999f6602f0cbf709fcede5` |
| mutants_quick | `/usr/bin/python3 -I -B stage0-code/s0mutants.py` | 0 | 301 | n/a | `c4f79d5dfec05cca9aa9e4e956f9d895bd00f34f63abeb5a581877d7cfecc7de` |
| mutants_full | `/usr/bin/python3 -I -B stage0-code/s0mutants.py --full` | 0 | 896 | n/a | `895f17e668213ef3b76c9664ab34f76e9bf974b46e2bd346b4bf30df8f2abb4b` |
| toy_rerun_L4 | `/usr/bin/python3 -I -B rerun.py .` | 0 | 9 | n/a | `e54f68e1661b71b2ccaceae282cd57301db5d5d979d8b534c04d4ba3c48cbfd2` |
| toy_planted | `/usr/bin/python3 -I -B planted.py .` | 0 | 0 | n/a | `8a4ebd8cd4c04b681a8515f79f197a093cabf90304570b785531cf5d4e7106d8` |
| toy_radius_mutants | `/usr/bin/python3 -I -B radius_mutants.py .` | 0 | 0 | n/a | `5d826a8415a4a5ca7c51dd19c5abd8d237502225b9cc01a0d65b112a040b9ff7` |
| toy_exact_small | `/usr/bin/python3 -I -B exact_small.py .` | 0 | 141 | n/a | `a0455a8889639109e5327feb40756c2acedf107bed78124ee9a31770d514cb6c` |

| file | SHA-256 |
| --- | --- |
| stage0-code/s0controls.py | `cae8a01469840fd5d7e64faba17b27f075b79b9784b198144f274412f6c715b3` |
| stage0-code/s0geom.py | `bc87c639ad7bc79ee67092a06394f078282fd0e1f2503e833310d1aa68f7445b` |
| stage0-code/s0mutants.py | `e03b4d3b1483b5eb8eb1de983a95a7694039ff718bfe112ff0d9776863b0b56d` |
| stage0-code/s0native.py | `41286c946d59af0c23e9fd70cdc5e9c06170957eb100ee119b9f7864487386ec` |
| stage0-code/s0ref.py | `492b53099780d39723e793add9c962a2e141378eee2359d2f7f0c7b9117eef2a` |
| stage0-code/s0run.py | `424f6c6577075ac4b42119a534f648e9b26f37f26e2adef281ffd8dc7dd33537` |
| stage0-code/s0s6.py | `28a95db1095df670f3188912599e1cba1c848fe6c512728d1521cbcb69ac7a40` |
| stage0-design-r2/exact_small.py | `8196ab1598437e929bfedac9d818c620fc19cce48e4ddc286b137e02d4fa6d3a` |
| stage0-design-r2/planted.py | `36753f3cb12365ae35dad624f22c3f5df227242521eed42076f3918a1427a6c9` |
| stage0-design-r2/proto.py | `24806c62c5e3b123e405183fddd717a264be73014bb38c9aa2ee1dfaae3f4ec8` |
| stage0-design-r2/radius_mutants.py | `b6362a43f9c0d910c1c97938c1c5e059f9ea2a25264c386a8dcfeafb6503d270` |
| stage0-design-r2/rerun.py | `77badd86f3905e77f1dbc30cce565cf40af9d21afbdf05a9f87c69a650a448db` |

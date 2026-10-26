# Stage 0 run manifest (r3)

Python 3.13.16 on Linux-6.18.44-fc-v153-x86_64-with-glibc2.39.

Stage 0 design evidence (r3; not frozen code: the implementation is layer 2): toys, planted sets, generic random backgrounds, small exhaustive windows, the S6 reference structure and v8 configuration combinatorics (counts, orbits) only; no closure on v8's configuration class (s0geom refuses it).

| step | command | exit | s | -O identical | stdout SHA-256 |
| --- | --- | --- | --- | --- | --- |
| controls_frozen_full | `/usr/bin/python3 -I -B stage0-code-r3/s0controls.py` | 0 | 124 | True | `a0743c03b48e0dd4e0fac6e2df6daaeb74964aca836733a74a9f3aed4e79cdb2` |
| s6_po8_proofcheck | `/usr/bin/python3 -I -B stage0-code-r3/s0s6.py` | 0 | 17 | True | `0f0bca68f34aa498e5026952cda77637ca7cfe8cb69c3eec0e96768aaa939c5d` |
| symcheck_v8_combinatorics | `/usr/bin/python3 -I -B stage0-code-r3/s0symcheck.py` | 0 | 19 | True | `76779524835103d032eda1d2170a6c1a4e57d5fb9cdb342835f5c03056c2d8b5` |
| mutants_quick | `/usr/bin/python3 -I -B stage0-code-r3/s0mutants.py` | 0 | 589 | n/a | `9c7939068c440344e69e972154b15a230179978b86a392683fbf2f656a91a0f4` |
| mutants_full | `/usr/bin/python3 -I -B stage0-code-r3/s0mutants.py --full` | 0 | 1982 | n/a | `831322578468461040705474f10a760b6846113e0bbbfac8eeeb9f3a98630fbe` |
| toy_rerun_L4 | `/usr/bin/python3 -I -B rerun.py .` | 0 | 10 | True | `cb843f0fdf42944041f12f19e904b9893b436db0f1e87cb0db9e8f4e739e825f` |
| toy_planted | `/usr/bin/python3 -I -B planted.py .` | 0 | 0 | True | `8a4ebd8cd4c04b681a8515f79f197a093cabf90304570b785531cf5d4e7106d8` |
| toy_radius_mutants | `/usr/bin/python3 -I -B radius_mutants.py .` | 0 | 1 | True | `5d826a8415a4a5ca7c51dd19c5abd8d237502225b9cc01a0d65b112a040b9ff7` |
| toy_exact_small | `/usr/bin/python3 -I -B exact_small.py .` | 0 | 153 | True | `a0455a8889639109e5327feb40756c2acedf107bed78124ee9a31770d514cb6c` |

| file | SHA-256 |
| --- | --- |
| stage0-code-r3/s0controls.py | `bc07ccf2a381400c3a688413d4c872a1cf5243cb3f72793f36fbf17014d01d38` |
| stage0-code-r3/s0geom.py | `bb6ef25d37c9826a7984c57e76c7cceef78356b639d97884192e0159b9e1459e` |
| stage0-code-r3/s0mutants.py | `6f5e1c9f27de74a781259a3d229deaf214eb2fd649541566c792c397b111f982` |
| stage0-code-r3/s0native.py | `4206549e8c01d62c684d4375fb11ae79e2fe69ef059c61600ae3db04570c8526` |
| stage0-code-r3/s0ref.py | `88f6ab52afede894e031bbee2643ada200e8ceb58e0050a050bbb3065315be5d` |
| stage0-code-r3/s0run.py | `d1db884ad86d8f82e8d578930f94f096965f378b5a9b3d770053861f2d239fa0` |
| stage0-code-r3/s0s6.py | `110f275cd83edb759b40c249900bc397e1fc3accc9571add50fa8bac3e42289a` |
| stage0-code-r3/s0symcheck.py | `f5783eb4a46dd1b3503bbd07e4e435ed3cb0b4a47cd14cb92d423e9b6950f757` |
| stage0-design-r3/exact_small.py | `8196ab1598437e929bfedac9d818c620fc19cce48e4ddc286b137e02d4fa6d3a` |
| stage0-design-r3/planted.py | `36753f3cb12365ae35dad624f22c3f5df227242521eed42076f3918a1427a6c9` |
| stage0-design-r3/proto.py | `24806c62c5e3b123e405183fddd717a264be73014bb38c9aa2ee1dfaae3f4ec8` |
| stage0-design-r3/radius_mutants.py | `b6362a43f9c0d910c1c97938c1c5e059f9ea2a25264c386a8dcfeafb6503d270` |
| stage0-design-r3/rerun.py | `a208f10cfcb75ca359ed23d7c6a1ea3c1bae729d3a9d99ba35794be392dd8b83` |

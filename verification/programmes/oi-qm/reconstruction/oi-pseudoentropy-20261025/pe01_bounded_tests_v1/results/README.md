# PE-01 results: run 40271434371

These are the structured outputs of the PE-01 run, retained as plan §8 and §11 and amendment A1 require. They are
the run's own bytes: nothing here was edited. The verdict text is `verdict.txt`; this file states only where the
outputs come from and how they were checked.

- **Run:** `40271434371`, attempt 1, workflow `.github/workflows/pe01-bounded-tests.yml`, event `workflow_dispatch`, branch `research/oi-pseudoentropy-20261025`.
- **Head:** `549641460b8ddb536178f95fac2ec9390e84a987`, which is the commit every shard and `measurements.json` record.
- **Run conclusion:** `success`, created 2026-10-26T04:54:19Z, updated 2026-10-26T05:53:23Z.
- **Jobs:** 78, all at `head_sha` `549641460b8ddb536178f95fac2ec9390e84a987`; conclusions: 78 success.
- **Verdict class:** `COUNTEREXAMPLE`, with the VG self-test passing (`verdict.json`).

## Files

- `measurements.json`, `verdict.json`, `verdict.txt`: the contents of the `pe01-results` artifact.
- `shards/<id>.json`: each shard's output. It records the commit and the recipe; it omits the run id so that its
  replay can be compared byte for byte.
- `shards/<id>.provenance.json`: the shard's run id, attempt, job, commit and recipe, from the same artifact.
- `shards/<id>.rp.json`: the replay job's record for the shard (artifact `rp-<id>`).
- `SHA256SUMS`: the sha256 of every file in this directory except itself.

The artifact zips are not committed. Their digests are listed below.

## Artifacts

Downloaded from `https://api.github.com/repos/amaybaum/incompleteness/actions/runs/40271434371/artifacts` and
`.../actions/artifacts/<id>/zip`.

| Artifact | Id | Size (bytes) | sha256 of the zip |
|---|---|---|---|
| `pe01-results` | 12630192834 | 175489 | `4904d2c7dbaaafc3fa971126d6252a83eb13acf641f544846c44374a245066ca` |
| `rp-controls` | 12629352596 | 189 | `be852342dd62e65902366387a369ac76c4486e36beb5768ae9a38ce86ac41e6d` |
| `rp-n3-clk` | 12629845382 | 183 | `0b737c02d5ed5b4be13efb8002587c2c22fcc45d138c837d948b4f3a3bc78428` |
| `rp-n3-clk-m3` | 12629268546 | 192 | `93f474fe555ee81510b1b68d47e062a390f2ef907f22ba9ef64ccb247a05d589` |
| `rp-n3-filt` | 12629746376 | 186 | `837213912b114e65ac5364f5df4b3f4b663cae94ca26a2c38ba527991bed739e` |
| `rp-n3-filt-m3` | 12629398669 | 195 | `6da900661ad266510efd5160d224c90a4646224edf24325dedecf4bcedd0ffcf` |
| `rp-n3-lin` | 12629925326 | 183 | `92a72de99c35b6c0c917d88e482272298e19f7d25877fdcbb8d0274a0586f5d8` |
| `rp-n3-lin-m3` | 12629214216 | 192 | `c9575f369355732562848554fe56fc07521c83f26a22b34a3bc58b66f57aa1b7` |
| `rp-n4-clk` | 12629790706 | 183 | `b2737b22d0dbf1c070919b292685ae997bf0c1b8c3b46d276334770849b31574` |
| `rp-n4-clk-m3` | 12630085679 | 192 | `e16d1cd9798defa12757ac0919e90e62f11d79978eae8d10308df84c663658b8` |
| `rp-n4-filt` | 12629342636 | 186 | `5d363dfb71ce3f3d73040a881597562fc3ce124cf11ea5445f20256932d1326c` |
| `rp-n4-filt-m3` | 12629248948 | 195 | `aace55f718e3e306b66c6d543137cbc02f1d2cf5e99ed3104a0efbb9fea20174` |
| `rp-n4-lin` | 12628714960 | 183 | `0d4fc32443b8ea6f7ea92787d6249f01c8e629787ec1c7b55705b9e532a29030` |
| `rp-n4-lin-m3` | 12629523567 | 192 | `6eafa9f3a692da6ab24586252f6c7d85a183201338828a1f4b96c3ca29b10318` |
| `rp-n5-clk` | 12630020236 | 183 | `d25b180d9d57096e208924d01c077eff17f3952d5f1e597c127d3562ad3e16b6` |
| `rp-n5-clk-m3` | 12629414272 | 192 | `abd41e0db6951e0f0499fd0dcc3e47d9ae206221ce141ea0488682376a51162f` |
| `rp-n5-filt` | 12629502360 | 186 | `6486fe5f1f0b3178f7f0dd9c8064802745ca36e3c591a0bdeb2efbea5da3a8c2` |
| `rp-n5-filt-m3` | 12630066217 | 195 | `aba6917cc624e6c30b219a090393d35e41d38a9ee62dfc06c9658d32ffb6e860` |
| `rp-n5-lin` | 12629352825 | 183 | `9d158c6e43688979fe237c6b23be66b2bd011bc885d9d1f721538f95b8c6a940` |
| `rp-n5-lin-m3` | 12630580037 | 192 | `490eb878722b47e443252793d9d8ecf3f6f072ecfb194649db9829ebec0fa105` |
| `rp-n6-clk` | 12629323798 | 183 | `244351580b17c014f9fc937a7e45812755d86fd81cea0ea98e24a788dee3eae3` |
| `rp-n6-clk-m3` | 12629084948 | 192 | `4c4e9c5ed3e3970ec699dae1be380f8d50ae1e1f9e6ac0384756065bf7eabbfa` |
| `rp-n6-filt` | 12629681212 | 186 | `e05745d8ff06b0a4f6a0dd297cb6c662ca407f84fc9a9ade60e065dad1603d4a` |
| `rp-n6-filt-m3` | 12630576388 | 195 | `5f90d503607082fc8cc7b0fa183c3fd060ee1271cb7d8294201e413226cf7966` |
| `rp-n6-lin` | 12630160241 | 183 | `ef05f43580f8b7c4dd0951f8a8ba4308be56ac417bf8e79754159cc3e2493446` |
| `rp-n6-lin-m3` | 12630726337 | 192 | `8fadeb6b8610a2e2109d1f0b4cdf4246dea58bd2ee31e05777a0f00f5cb0c895` |
| `rp-n7-clk` | 12629114562 | 183 | `31a0d6a17080a8a5011eabc1af49bcb5779b2dafdb333691e11917dbce8fc192` |
| `rp-n7-clk-m3` | 12629508065 | 192 | `c8cbca1d2e69a2e3eea1d44471aae6193a771cbcf91fc88025f3b22c3482af28` |
| `rp-n7-filt` | 12629906471 | 186 | `04572553cfa18fb4970dd7c6c338890c6b00debf2d2ea030bf135dd485e17a76` |
| `rp-n7-filt-m3` | 12630031506 | 195 | `6672673f494ef582539e6682fe68227be92e381699ceb5f136eeac81aab92922` |
| `rp-n7-lin` | 12629936741 | 183 | `5f737d2a531059f1d5df1da002620af5a8113bd1e99b2dc9c318f40d56cf04dc` |
| `rp-n7-lin-m3` | 12629852126 | 192 | `09650be309c38d8f679d4cc2e011e2a812c1a89f850005c1c9b88078b1d8facd` |
| `rp-n8-clk` | 12630176871 | 183 | `ead075114ef25eefba720faf2f3dcb574574f7cec696bacc292c7fbc4f6cbd36` |
| `rp-n8-clk-m3` | 12629972051 | 192 | `c21a4efc1e5de7131440128e0568faa869aed9bf0f76dc6bbbf8be8b53bf6597` |
| `rp-n8-filt` | 12629857047 | 186 | `740ab987b8006dd3b1f50be43918322f454eb6f5d319c1c04646125bb153a19b` |
| `rp-n8-filt-m3` | 12630510119 | 195 | `9f49eb07a80e04e5a35955c5e65e0e6268b4ab86698b0c4c6302e54d5f00a76f` |
| `rp-n8-lin` | 12630086062 | 183 | `a2ebce5c4a106243cf6b33cd82ce5afd31d1b09836215056c83173db5b30a932` |
| `rp-n8-lin-m3` | 12629771884 | 192 | `a93483fa76bb62c067cc75ed976eeb53a42dbdbdfa9aa419cb8dacb1118a8bba` |
| `rp-tape` | 12629895960 | 177 | `d2487b55696e5030545b96ab585e4de08176d4d4d4e85d27cf76bf0fb6b798f8` |
| `shard-controls` | 12628433220 | 3002 | `026e6cbd9f9c718c8c3b18edf47a833e5057d9e0056b83f2c0052f8005bbaad0` |
| `shard-n3-clk` | 12628664311 | 11950 | `9e64e78a1b7b90a6e103e0a3c4c5b27c96ee80aba2b6ed6793ea5f7c52df6be8` |
| `shard-n3-clk-m3` | 12628947275 | 4738 | `3cf99032922c08f1d5c27c7bf85e4dc736771639364c90fed1d5123fffa28ca4` |
| `shard-n3-filt` | 12628477769 | 11648 | `d9693e80b852f1fd95d9a26f7b40f2853cc36b236d5ccf17cc9b09b8ced50dc9` |
| `shard-n3-filt-m3` | 12629021629 | 4937 | `a40c66bbb828a747e9133faa635259696d64deb31fa69af0af6e0a7bb67469ad` |
| `shard-n3-lin` | 12628608139 | 11386 | `79f9be62876a20d4b0cdfc6fe15775aeb423dea986ca740be9ebd3f2c6e76778` |
| `shard-n3-lin-m3` | 12628173350 | 4679 | `58faf83c2afbd2b8eda035966fffd52151c87679f9b3f2acc83eede4b3b664b4` |
| `shard-n4-clk` | 12629017735 | 19512 | `ba7da72a20d702270d8047e2a1befefc1b53f1efe944f74a75e24c7ca18f4422` |
| `shard-n4-clk-m3` | 12628513545 | 7520 | `8166d420754b0cb5012ab8731481c09c4d14de6d08218fd20b759485ff805ca9` |
| `shard-n4-filt` | 12628768445 | 18065 | `1efd8b4e1cf8f13363b8a7cb555d0a16120e5df56285c33d8f25aacb3007aefb` |
| `shard-n4-filt-m3` | 12628761704 | 7402 | `7165b97e13abaed79465c43d20992d9bb8beb46bc1f4d138e4d72afedd00eb13` |
| `shard-n4-lin` | 12628828864 | 16349 | `d8c76e1ebe929dd1693dfbfe1253e9322320ebebece8250beee7a790c6b319d9` |
| `shard-n4-lin-m3` | 12628164089 | 7249 | `de9c7ff0f8538582499f83a7080dbe6b8a3441640c551c80569967b9da48a15e` |
| `shard-n5-clk` | 12628192493 | 57321 | `37626f584b8cbc9a84ef76c046a93d498a64b07207ec0c65e0edd93a9bbf6cf4` |
| `shard-n5-clk-m3` | 12628964666 | 14530 | `0d0d53e4bcd5f31ed6a0568134952c400fd6520e2bce0865995f98d5c5373ad2` |
| `shard-n5-filt` | 12628292737 | 43494 | `20d51217dda721624c4fb4ea26989e365eabadf89e651c3aa6806ab059e619dc` |
| `shard-n5-filt-m3` | 12628649732 | 13990 | `ac05c21c80807ee126cfb9647974bb8bea8db7c69096b26b8edf88bc8b612408` |
| `shard-n5-lin` | 12628134866 | 37393 | `d16f8c8d5e2a9343514eb7a2f0b97b81cf1cfc12e13cb0c6bc795f5d739886df` |
| `shard-n5-lin-m3` | 12629295946 | 14394 | `2a4e747afce84da55333f7a51f91ca5128c2ce1ee2c58e0c26317b1892cc216d` |
| `shard-n6-clk` | 12628209582 | 146361 | `bca81e8e8ef0935077bbd25201cc5b9ffde56b076d11025077ea85ed8aeaab81` |
| `shard-n6-clk-m3` | 12628384732 | 23784 | `6f7525d03ddaf5cb20cfbc6f9430a3d5d99e40ca15b479a389c251dbebf0ca3a` |
| `shard-n6-filt` | 12628708068 | 106098 | `9f0c22e75b7fd1f3971127c8c7887381a3d546849bf3e70347db5249ff409a0e` |
| `shard-n6-filt-m3` | 12629217353 | 21948 | `e605a3701556a30fc558dc24f4a3a8bf58546ce6ab80c1a8ccc553c01acb6caf` |
| `shard-n6-lin` | 12628282644 | 104243 | `36ea1d29dfc2a5e30bd9efb9f57546a71b77793eaddc545bc44230e4c37bbe46` |
| `shard-n6-lin-m3` | 12629143199 | 24753 | `072158856c5bfe666d45167cbd7c3cb09e8f6228a332771c356a998217c7b51b` |
| `shard-n7-clk` | 12628924612 | 431360 | `5a027890a6a3aea3b6fa436cc5745b02228a57905cd904e1308c4f1a093a0920` |
| `shard-n7-clk-m3` | 12628328248 | 3592 | `dfbe5d421a1a1e15f5b592b99b4bf798b59cfcbb4ba95614dee3ee156aeec3e1` |
| `shard-n7-filt` | 12629545552 | 239221 | `51f2b65a52e18808afb399f2edcfb7299acad20cdb288ee1f81bab4e608576aa` |
| `shard-n7-filt-m3` | 12628833030 | 3593 | `d3af6483d5ffce0bd4440ec245ae2478ce2127fa14458374062698ef5ecd5a57` |
| `shard-n7-lin` | 12629180875 | 245305 | `d27c786bd91d10523a74453ffdce817f79331dfc9ab240bc888d1df3d017cc0f` |
| `shard-n7-lin-m3` | 12628788082 | 3389 | `2a26e33e958fa5f0373ce1798e548cbcab2c4fbd997fc79a74c03afefa84471a` |
| `shard-n8-clk` | 12628089624 | 1021220 | `0f36b3f791d2bccb400f8e5bcca595c155f62856d32e882440cb0424da7110e9` |
| `shard-n8-clk-m3` | 12628582977 | 4680 | `6122cccd6cad1516a3617b2c0800dffe941117bb3a14d937c28f949898dd1b33` |
| `shard-n8-filt` | 12629706213 | 460272 | `8f080781ffb6ada4586f409ee2ac7b970ec1c8aa40ec4835448e1a51929eeb8f` |
| `shard-n8-filt-m3` | 12629135067 | 4625 | `061a95057c716a10a1c0478d5736723059167c3985079b760c6b4f089159f8ca` |
| `shard-n8-lin` | 12629097207 | 613936 | `416c5721acf7006aff9d99efbc2fabbd00bb29084a7af77e5cab28be191270ed` |
| `shard-n8-lin-m3` | 12629181101 | 4678 | `d8834e5bd0a84c1d9a33b11cbc8256d610d97707b627bbf3282f85b4ad912160` |
| `shard-tape` | 12628769069 | 2455 | `c7f7567c94d63a26d7615bd1478be165205df1a0a80aa23ee185c357831065ad` |

## Checks made before committing

- Each zip was extracted into its own empty directory, refusing absolute paths, `..` components and symbolic links.
  None was refused, and nothing from the artifacts was executed.
- The shard ids of `measurements.json["shards"]`, the `shard-*` artifacts and the `rp-*` artifacts are the same 38 ids.
- For every shard, the sha256 and byte length of `shards/<id>.json` equal `measurements.json["shards"][id]`, its
  status there is `complete`, and its provenance names run `40271434371`, the attempt and job recorded there, and
  commit `549641460b8ddb536178f95fac2ec9390e84a987`.
- Every replay record reads `{"shard": <id>, "identical": true}`, and `measurements.json` records
  `replay_identical: true` for that shard.
- The files were scanned for local paths, tokens, keys, URLs, e-mail and IP addresses; there were no hits.

## Regeneration

At commit `549641460b8ddb536178f95fac2ec9390e84a987`, from the repository root:

```sh
python3 -I -B verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/verdict.py verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/results/measurements.json --out <dir>
```

`<dir>/verdict.json` and `<dir>/verdict.txt` are byte-identical to the files here (sha256 `eeebc2196dee2d80dfa721ae2657fb8550fd8c0147f93c62710125ce42eb4e23` and
`3b8f5924af25efe0223a8c9f4118caa283d3129713f0b10afdd9668961771987`). `verdict.json` records the sha256 of `measurements.json`, `f17109f10379d648fcb055c2a1868666205fae8499b35ca65ecedae7a41f067a`.

# F2 census checks

Exact audit checks behind four corrections to the F2 research records on this branch. They decide nothing for any
round, adopt nothing, and are research material, not a native round.

| check | script | question | cited by |
| --- | --- | --- | --- |
| A | `layer_images.py` | images of the kernel's shear and swap layers, and of E1-L's layers, under F2-5's dictionary at `q = 3` | — |
| B | `monitored_law.py` | whether E1's registration reproduces OI's monitored trajectory law at `q = 3`, `N = 1` | H N2 and summary item 5; F2-1 C1 |
| C | `asp_laws.py` | which one-step registered-value laws E1-admissible classical data give | — |
| D | `scale_gauge.py`, `scale_gauge_xcheck.py` | positivity and complete positivity of `Φ_{diag(1,d)}` for odd `q ≤ 13`, cross-checked with F2-5 at `q = 3` | F2-5 §2, §3, O1 |

**Recipe.** Each script takes the path of `../f2-5-operational-dictionary/f2_5_dict.py` as its argument; those that
reuse F2-5's definitions pin it by sha256 `211ce708…`. Run from this directory:

```
python3 -I <script>.py ../f2-5-operational-dictionary/f2_5_dict.py > <script>.out
```

**Provenance.** Written in an earlier session as working material and carried on the session handoff branch
(`wip/f2-census-checks/`, verified there against its `SHA256SUMS`). Replayed on 2026-10-17 against this branch's
`f2_5_dict.py`: all five outputs byte-identical to the committed `.out` files. These are local runs, not `check-run`
attestations.

| file | sha256 |
| --- | --- |
| `asp_laws.py` | `26d7bbcdfeda6c5c6401e5109602758b93b0036f2772a37d9428407bf358baa0` |
| `layer_images.py` | `857e0225d6aa7ee00f1dd79a07118a394923a4b33b00ac50d36e2657ea007c79` |
| `monitored_law.py` | `3842951319be18048a2033b439373a2ac07df8542932dcd5ea79f59fbfc336c9` |
| `scale_gauge.py` | `c7defe64bb41242735adf0c4842eae95a4ff630e664b47fe44310aa9582307b5` |
| `scale_gauge_xcheck.py` | `e0a05daa98312a8d48a2f8524dd8ba3fc147b616967f73723862c4a9df9ef7db` |
| `asp_laws.out` | `da44dee76df512032839b111500fd67561daa7b219d923e0ea04697c2b13699c` |
| `layer_images.out` | `8f76e42382ddcf2569fd7031a290a4e870a36ab0d29f0101e20792e883626b9b` |
| `monitored_law.out` | `f0dbf2fff1dee4df828f87c6be5239c2687ce7e6d43af05af272f6535cab33c8` |
| `scale_gauge.out` | `a8a5ffd499655b523fb32d2d37db8e33cbb27fd60b4be78fd20888880e9bcba4` |
| `scale_gauge_xcheck.out` | `fc1834b38ec9c50338680f7b6dd695018d06f787734144ed269f2caf3d9b0d4d` |

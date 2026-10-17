# F2 census checks

Exact checks behind four corrections to the F2 research records on this branch. They decide nothing for any
round, adopt nothing, and are research material, not a native round.

| check | script | question | cited by |
| --- | --- | --- | --- |
| B | `monitored_law.py` | whether E1's registration reproduces OI's monitored trajectory law at `q = 3`, `N = 1` | thread H (N2, P-1, E3, the E1/E3 table, summary item 5); F2-1 C1; F2-2 C-OI |
| D | `scale_gauge.py`, `scale_gauge_xcheck.py` | positivity and complete positivity of `Φ_{diag(1,d)}` for odd `q ≤ 13`, cross-checked with F2-5 at `q = 3` | F2-5 §2, §3, O1 |

**Recipe.** Each script takes the path of `../f2-5-operational-dictionary/f2_5_dict.py` as its argument; those that
reuse F2-5's definitions pin it by sha256 `211ce708…`. Run from this directory:

```
python3 -I <script>.py ../f2-5-operational-dictionary/f2_5_dict.py > <script>.out
```

**Replay.** Run as above against this branch's `f2_5_dict.py`, each script reproduces its committed `.out` byte for
byte. These are local runs, not `check-run` attestations.

| file | sha256 |
| --- | --- |
| `monitored_law.py` | `70359bfc483c41f862b8cae3d6e5753688cc24a45b73d4ecf3f25066e2aec178` |
| `scale_gauge.py` | `c7defe64bb41242735adf0c4842eae95a4ff630e664b47fe44310aa9582307b5` |
| `scale_gauge_xcheck.py` | `e0a05daa98312a8d48a2f8524dd8ba3fc147b616967f73723862c4a9df9ef7db` |
| `monitored_law.out` | `634e1639637e9e803f9d6a65786023cba47f2f9362aec358118d53f48ffdac5d` |
| `scale_gauge.out` | `a8a5ffd499655b523fb32d2d37db8e33cbb27fd60b4be78fd20888880e9bcba4` |
| `scale_gauge_xcheck.out` | `fc1834b38ec9c50338680f7b6dd695018d06f787734144ed269f2caf3d9b0d4d` |

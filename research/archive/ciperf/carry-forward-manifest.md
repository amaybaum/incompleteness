# n18 carry-forward manifest: D d6b6458010a6d2812bd3215a8bb6f8a1bab37f00 -> base 88bb2641e8e6822398b4df862cf5ce0b3479ba99
| path | blob at D | blob at base | identical |
| --- | --- | --- | --- |
| `verification/lean/dita_support_minimality_probe.py` | `f65ec4fd66f6a50d62cb231734889817aaf68187` | `f65ec4fd66f6a50d62cb231734889817aaf68187` | yes |
| `verification/lean/a42/Rle13_39.txt` | `cb40df5fbe9f2aa6cb88e61ffb4989bb66772c21` | `cb40df5fbe9f2aa6cb88e61ffb4989bb66772c21` | yes |
| `verification/lean/a42/c6_control.py` | `b532a9fe275443975c10d0d3e6c5fdf0ca78d53e` | `b532a9fe275443975c10d0d3e6c5fdf0ca78d53e` | yes |
| `verification/lean/a42/classify42.py` | `b29549361ae74a35029bbc1c77659aac85abd402` | `b29549361ae74a35029bbc1c77659aac85abd402` | yes |
| `verification/lean/a42/ctrl16.py` | `bef4ab5c2d6f4db3452962473ac61c207695f490` | `bef4ab5c2d6f4db3452962473ac61c207695f490` | yes |
| `verification/lean/a42/cvsize.py` | `c0e30682e76c77116d03a6507f1fe3c6ab433bb7` | `c0e30682e76c77116d03a6507f1fe3c6ab433bb7` | yes |
| `verification/lean/a42/dfs01.py` | `cb6d0d03ff639586549da424ec6d59708a9147b1` | `cb6d0d03ff639586549da424ec6d59708a9147b1` | yes |
| `verification/lean/a42/dfs42.py` | `c7052346d472de34f29566dde7bee2ede5a27707` | `c7052346d472de34f29566dde7bee2ede5a27707` | yes |
| `verification/lean/a42/dfsR.py` | `adadda4f3ae438ed9a580db803cf57c036d46888` | `adadda4f3ae438ed9a580db803cf57c036d46888` | yes |
| `verification/lean/a42/dfsR2.py` | `67cd77161476adfeda38f475e0c955d467ad1b55` | `67cd77161476adfeda38f475e0c955d467ad1b55` | yes |
| `verification/lean/a42/lemmas42.py` | `de7d3f39e03c58b745dc537aa759aa8764192c60` | `de7d3f39e03c58b745dc537aa759aa8764192c60` | yes |
| `verification/lean/a42/lib42.py` | `0d9a80f5467cc9690b78aed3c094a2a8a57dcc73` | `0d9a80f5467cc9690b78aed3c094a2a8a57dcc73` | yes |
| `verification/lean/a42/minsupp_exact.py` | `390243fd8f540e33749ebf5df17adad278bb42a8` | `390243fd8f540e33749ebf5df17adad278bb42a8` | yes |
| `verification/lean/a42/pairtypes.py` | `1a31f1d9de73922e63b5e5882b8ce79bb1b7c88a` | `1a31f1d9de73922e63b5e5882b8ce79bb1b7c88a` | yes |
| `verification/lean/a42/r2a_landed.py` | `3e71d33dd14edd926a55258d062f832979146ba0` | `3e71d33dd14edd926a55258d062f832979146ba0` | yes |
| `verification/lean/a42/r2b2_census.py` | `bd5bfcc4d5fe0974fbf1c00c16c411fc5377fc61` | `bd5bfcc4d5fe0974fbf1c00c16c411fc5377fc61` | yes |
| `verification/lean/a42/r2b_independent.py` | `c4a4cf3eea048f25248f9b9023c3ea8e6271eb98` | `c4a4cf3eea048f25248f9b9023c3ea8e6271eb98` | yes |
| `verification/lean/a42/r3_run.py` | `f7e318ddb5a891b87866baff07f5ed345a385864` | `f7e318ddb5a891b87866baff07f5ed345a385864` | yes |
| `verification/lean/a42/r5_family.py` | `c7cd1ab4fe7c705c48f7a9272a3b6d5aa4db263c` | `c7cd1ab4fe7c705c48f7a9272a3b6d5aa4db263c` | yes |
| `verification/lean/a42/sat42.py` | `3c0f700a27ab0e3856fb82057479c3e1abaebfc7` | `3c0f700a27ab0e3856fb82057479c3e1abaebfc7` | yes |
| `verification/lean/a42/sat_hr.py` | `f233b115791e3a1b82e1ff5092c06e1debcf9299` | `f233b115791e3a1b82e1ff5092c06e1debcf9299` | yes |
| `verification/lean/a42/spanAll.py` | `51e1fcfb81a0f66909c3dfe0caf2d88cab254132` | `51e1fcfb81a0f66909c3dfe0caf2d88cab254132` | yes |
| `verification/lean/a42/triples.py` | `bc881bd2040538296af255107d8469141303efce` | `bc881bd2040538296af255107d8469141303efce` | yes |

Files under a42/ at base not at D: 0

Workflow fragment (probes_a42_exclusion job), identical at D and base: yes

```yaml
  probes_a42_exclusion:
    name: Numerical probes / A42 exclusion (${{ matrix.part }})
    if: ${{ github.event_name == 'workflow_dispatch' }}
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        part: ['paths', 'r5', 'n18:0', 'n18:1', 'n18:2', 'dfs:0', 'dfs:1', 'dfs:2', 'dfs:3', 'dfs:4', 'dfs:5',
               'sathr', 'cubes:0', 'cubes:1', 'cubes:2']
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install numpy==2.4.6 python-sat==1.9.dev15

      - name: A42 exclusion shard
        working-directory: verification/lean
        run: python3 dita_support_minimality_probe.py --part '${{ matrix.part }}'

  probes_foundations:
```

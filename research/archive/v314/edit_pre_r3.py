p = 'preregistration.md'
s = open(p).read()
def r(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90])
    s = s.replace(old, new)
r("retire.py` | `7f38c4ad6265e98c3b6c7b648700474ed2dbb58f`", "retire.py` | `f2e49fc6a39de15d3fd653502a4946f2406a5016`")
r("controls.py` | `7c2ac406d7913e55b8b439213bdb2860a075e107`", "controls.py` | `0282cbeedd18d67e4746427a9ded9c3b60b7a855`")
r("preserve.py` | `edc3be8295509631c3a8251907167242d8e61dde`", "preserve.py` | `e2e275aca4bc228228fd9e865047ad0fba0776d7`")
r("ledger.json` | `0d135c79f10d6f2d14a0c741d5eb880102ff8cb3`", "ledger.json` | `79a1645d484b2d7ef71b871a612e8d36aafe8e60`")
r("| `verification/lean/edge_rigidity_probe.py` | `f4fee29505b572161a22eccee3ae8b35aa48ab61` |",
  "| `verification/lean/edge_rigidity_probe.py` | `8dad60d0aac870fced7deeec44c0dbdfcb3d45de` |")
r("| `AGENTS.md` | `ee9c7bf280bdac2c263ae0f1006f4aca2eb068da` |", "| `AGENTS.md` | `7931dc848133a19e0927dd1cd57b01002deeac07` |")
r("""  - `preserve.py` prints `preserve: all hold`, and `preserve.py --self-test` prints
    `preserve: self-test OK` with all twelve mutants failing as required;""",
  """  - `preserve.py` prints `preserve: all hold`, and `preserve.py --self-test` prints
    `preserve: self-test OK` with all fifteen mutants failing as required;""")
r("""    commit, fails the four checks and names all seven sites;""",
  """    commit, fails the five checks and names all ten sites;""")
r("""| the seven damaged sites are preserved | `C2` (`S4`) |
| no dead code leaves a surviving module-level block | `C2` (`S5`) |""",
  """| the ten damaged sites are preserved | `C2` (`S4`) |
| no dead code leaves a surviving module-level block | `C2` (`S5`) |
| no removed in-place change reaches an object surviving code reads | `C2` (`S6`) |""")
r("""| `ast.unparse` text hashes differ between Python versions |""",
  """| the transformation and the checker share one model of aliasing, so a mutation outside it (through a helper function that changes a global, or a call on an argument that is no plain name) could escape both | the whole predicted tree ran in CI before `F`; every retained mutation control executes there and fails closed on an unmutated input, which is how the three aliasing sites were found |
| `ast.unparse` text hashes differ between Python versions |""")
open(p, 'w').write(s)
print('ok')

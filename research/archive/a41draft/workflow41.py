"""The frozen workflow edit: D's verify.yml with the three A41 shards added and required by the aggregate."""
import sys
JOBS = """  probes_a41_production:
    name: Numerical probes / A41 production
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: A41 index-map probe, the production path
        working-directory: verification/lean
        run: |
          echo "=== dita_index_map_probe.py ==="
          python3 dita_index_map_probe.py

  probes_a41_independent:
    name: Numerical probes / A41 independent
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: A41 index-map probe, the independent path
        working-directory: verification/lean
        run: |
          echo "=== dita_index_map_independent.py ==="
          python3 dita_index_map_independent.py

  probes_a41_hulls:
    name: Numerical probes / A41 hulls
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install numpy scipy

      - name: A41 hull census
        working-directory: verification/lean
        run: |
          echo "=== dita_index_map_hulls.py ==="
          python3 dita_index_map_hulls.py

"""
EDITS = [
 ("  probes_foundations:\n    name: Numerical probes / foundations\n", JOBS + "  probes_foundations:\n    name: Numerical probes / foundations\n"),
 ("    needs: [probes_core_a, probes_core_b, probes_a36, probes_a38, probes_a40, probes_foundations]\n",
  "    needs: [probes_core_a, probes_core_b, probes_a36, probes_a38, probes_a40, probes_a41_production, probes_a41_independent, probes_a41_hulls, probes_foundations]\n"),
 ("          A40_RESULT: ${{ needs.probes_a40.result }}\n",
  "          A40_RESULT: ${{ needs.probes_a40.result }}\n          A41P_RESULT: ${{ needs.probes_a41_production.result }}\n          A41I_RESULT: ${{ needs.probes_a41_independent.result }}\n          A41H_RESULT: ${{ needs.probes_a41_hulls.result }}\n"),
 ('          echo "a40=${A40_RESULT}"\n',
  '          echo "a40=${A40_RESULT}"\n          echo "a41_production=${A41P_RESULT}"\n          echo "a41_independent=${A41I_RESULT}"\n          echo "a41_hulls=${A41H_RESULT}"\n'),
 ('          test "${A40_RESULT}" = success\n',
  '          test "${A40_RESULT}" = success\n          test "${A41P_RESULT}" = success\n          test "${A41I_RESULT}" = success\n          test "${A41H_RESULT}" = success\n'),
]
def apply(text):
    for old, new in EDITS:
        assert text.count(old) == 1, old
        text = text.replace(old, new)
    return text
if __name__ == '__main__':
    sys.stdout.write(apply(sys.stdin.read()))

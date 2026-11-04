"""Re-check of fee98794: compare the plan's two admissible-region tables cell by cell with an independent
recomputation (Z from checks3 logic), and confirm K_cx. Design quantities only."""
import importlib.util, sys, io, contextlib, re
from math import ceil, log2
def load(name, path, argv):
    spec = importlib.util.spec_from_file_location(name, path); mod = importlib.util.module_from_spec(spec)
    old = sys.argv; sys.argv = [path] + argv
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    sys.argv = old; return mod
here = sys.argv[1]
c3 = load("c3", here + "/checks3.py", [here + "/checks.py"])
plan = open(sys.argv[2]).read()
sec = plan[plan.index("$\\theta = n$:\n"):]
tabs = re.split(r"\$\\theta = n\+1\$:\n", sec, maxsplit=1)
def parse(t):
    out = {}
    for line in t.splitlines():
        m = re.match(r"\s*\| (\d) \| (.*)\|\s*$", line)
        if m:
            cells = [x.strip() for x in m.group(2).split(" | ")]
            for mm, cell in enumerate(cells, 1):
                out[(int(m.group(1)), mm)] = [p.strip() for p in cell.split("\\|")]
    return out
P0, P1 = parse(tabs[0].split("Consequences")[0]), parse(tabs[1].split("Consequences")[0])
bad = 0
for th, P in ((0, P0), (1, P1)):
    for n in range(3, 9):
        for m in range(1, 5):
            mine = [c3.region(g, n, m, n + th, c3.Zs[(g, n)] + 1) for g in ("lin", "filt", "clk")]
            mine = [x if x != "-" else "–" for x in mine]
            if P.get((n, m)) != mine:
                bad += 1; print("MISMATCH", th, n, m, P.get((n, m)), mine)
print("cells compared:", len(P0) + len(P1), "mismatches:", bad)
print("K_cx:", {g: [c3.KCX[g](n) for n in range(3, 9)] for g in ("lin", "filt", "clk")})

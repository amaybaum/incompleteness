"""Toy follow-up: the self-supporting core of the toy block, and targeted
off-axis / symmetric-radius countercontrols on it (toy geometry only)."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location('tc', sys.argv[1])
src = open(sys.argv[1]).read().split('# --- Hand-checked instance')[0]
ns = {}
exec(src, ns)
Geometry, ball, even, AX = ns['Geometry'], ns['ball'], ns['even'], ns['AX']
L = 3
gA, gS, gO = Geometry(L), Geometry(L, symmetric=True), Geometry(L, offaxis=True)
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
FIXED = PHI | {((0, 0, 0), L-2)}
block = [q for q in ((c, t) for c in ball(1) for t in range(L-2, L+2)) if even(q) and q not in FIXED]
core = gA.closure(FIXED, set(block))
print('core', sorted(core))
print('core is a fixed point:', gA.closure(FIXED, core) == core)
print('off-axis mutant on core retains', len(gO.closure(FIXED, core)), 'of', len(core))
print('symmetric radii on block retains', len(gS.closure(FIXED, set(block))), 'vs', len(core))
# single-member removals: does the rest collapse?
for q in sorted(core):
    print('  remove', q, '-> retained', len(gA.closure(FIXED, core - {q})))
# without the fixed Phi analogue
print('core without Phi analogue retains', len(gA.closure(set(), core)))

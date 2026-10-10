#!/usr/bin/env python3
"""REL-C dependency audit (read-only).  Syntactic call graph of OIBridge/CompositeDimension.lean at L:
which declarations consume the `relT` (resp. `relC`) field of a NativeGate hypothesis, directly or
through another declaration of the file.  Usage: dep_audit.py <path to CompositeDimension.lean>"""
import re, sys

src = open(sys.argv[1]).read()
lines = src.split("\n")
decl_re = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(theorem|lemma|def|abbrev|structure)\s+([A-Za-z_][A-Za-z0-9_'.]*)")
decls, cur = [], None
for i, ln in enumerate(lines):
    m = decl_re.match(ln)
    if m or ln.startswith("end ") or ln.startswith("#print"):
        if cur:
            decls.append(cur)
        cur = (m.group(2), i + 1, [ln]) if m else None
    elif cur:
        cur[2].append(ln)
if cur:
    decls.append(cur)
body = {n: "\n".join(b) for n, _, b in decls}
line_of = {n: l for n, l, _ in decls}
names = set(body)
ident = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*")


def refs(n):
    toks = set(ident.findall(body[n].split("\n", 1)[1] if "\n" in body[n] else ""))
    # also header (hypotheses may mention other defs); calls live in the proof
    toks |= set(ident.findall(body[n].split("\n", 1)[0]))
    out = set()
    for t in toks:
        for cand in (t, t.split(".")[-1]):
            if cand in names and cand != n:
                out.add(cand)
    return out


graph = {n: refs(n) for n in names}
opaque = re.compile(r"\bh[GR]\.[0-9]\b|(?:obtain|rcases|cases)[^\n]*:=\s*h[GR]\s*$|(?:rcases|cases)\s+h[GR]\b", re.M)


def taint(field):
    direct = {n for n in names if re.search(r"\bh[A-Za-z]*\." + field + r"\b", body[n])}
    T = set(direct)
    changed = True
    while changed:
        changed = False
        for n in names:
            if n not in T and graph[n] & T:
                T.add(n)
                changed = True
    return direct, T


dT, T = taint("relT")
dC, C = taint("relC")
op = sorted(n for n in names if opaque.search(body[n]))
print("declarations parsed:", len(names))
print("opaque uses of a gate hypothesis (anonymous projections / destructuring):", op or "none")
print("direct consumers of .relT:", sorted(dT))
print("direct consumers of .relC:", sorted(dC))

chain = ["dim_of_nativeGate", "three_of_nativeGate", "blockData_of_nativeGate", "blockData_of_orthonormal",
         "finrank_plus_eq_finrank_minus", "not_even_of_nativeGate", "not_entangling_one",
         "Lop_anti", "Lop_eq_zero", "Lop_injective", "gate_corner", "gate_corner_symm", "Mfwd_Minv",
         "Minv_Mfwd", "lor_Minv", "gate_actC", "gate_corner_neg", "gt_corner", "gt_corner_neg", "gt_center",
         "gt_tangent_corners", "gt_sphere", "gt_sphere_corner", "Phi_sphere", "Phi_center", "Phi_center_all",
         "Phi_hom_zero_eq_zero", "Phi_lift_z_eq_zero", "gate_actT", "Mfwd_homMap", "Minv_homMap",
         "opGate_comp_homMap", "opGate_homMap_comp"]
print("\n%-28s %-6s %-6s  relT-tainted callees" % ("declaration", "relT", "relC"))
for n in chain:
    print("%-28s %-6s %-6s  %s" % (n, n in T, n in C, sorted(graph[n] & T)))

print("\nlines of blockData_of_orthonormal that reference a relT-tainted declaration:")
for k, ln in enumerate(body["blockData_of_orthonormal"].split("\n")):
    toks = set(t.split(".")[-1] for t in ident.findall(ln))
    if toks & (T - {"blockData_of_orthonormal"}):
        print("  L%d: %s" % (line_of["blockData_of_orthonormal"] + k, ln.strip()))

# controls
ok = True
ok &= {"opGate_comp_homMap", "gate_actT"} <= dT            # positive: the two known relT sites
ok &= "Lop_anti" not in T and "gt_center" not in T          # countercontrol: relC-only lemmas stay clean
ok &= {"opGate_homMap_comp", "gate_actC"} <= dC             # relC sites are found
ok &= "gate_corner_neg" in C and "gate_corner_neg" not in T
print("\naudit controls:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)

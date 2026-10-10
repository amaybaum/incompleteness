"""Independent verifier for RelcSelectBlock.lean (does not import gen_block / rcs_common).

Checks
  V1  every copied declaration equals the landed one modulo the renaming map, except the two
      listed line edits (each must occur exactly once, at the stated line);
  V2  the module declares nothing beyond the copies and the listed new declarations;
  V3  no relT-reading declaration or `.relT` projection is referenced; no `NativeGate`-typed
      hypothesis remains on a copied declaration;
  V4  closure: every landed declaration referenced by the module whose landed statement takes a
      `NativeGate` hypothesis has been replaced by its copy (no un-renamed reference), and every
      copy is reachable from the exported theorems (nothing unnecessary);
  V5  freshness of every new name across verification/lean-mathlib/OIBridge;
  V6  name resolution: no short identifier used by the module is declared in two of the opened
      namespaces, or shadowed from `OIBridge` / `OIBridge.RelcSelect`;
  V7  sorry / admit count;
  C   controls: two mutations of the module (one changed proof token, one un-renamed reference)
      must each make V1 / V4 fail.
"""
import os
import re
import sys

SCRATCH = "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad"
ROOT = os.path.join(SCRATCH, "wt-L/verification/lean-mathlib/OIBridge")
LANDED = os.path.join(ROOT, "CompositeDimension.lean")
MODULE = os.path.join(SCRATCH, "rcs/block/RelcSelectBlock.lean")

MAP = {
    "gate_corner": "gate_corner_ctrl", "gate_corner_symm": "gate_corner_symm_ctrl",
    "Mfwd_Minv": "Mfwd_Minv_ctrl", "lor_Minv": "lor_Minv_ctrl", "gate_actC": "gate_actC_ctrl",
    "gate_corner_neg": "gate_corner_neg_ctrl", "gt_corner": "gt_corner_ctrl",
    "gt_corner_neg": "gt_corner_neg_ctrl", "gt_center": "gt_center_ctrl",
    "gt_tangent_corners": "gt_tangent_corners_ctrl", "gt_sphere": "gt_sphere_ctrl",
    "gt_sphere_corner": "gt_sphere_corner_ctrl", "Phi_sphere": "Phi_sphere_ctrl",
    "Phi_center": "Phi_center_ctrl", "Phi_center_all": "Phi_center_all_ctrl",
    "Phi_hom_zero_eq_zero": "Phi_hom_zero_eq_zero_ctrl",
    "Phi_lift_z_eq_zero": "Phi_lift_z_eq_zero_ctrl",
    "blockData_of_orthonormal": "blockData_of_orthonormal_ctrl",
    "blockData_of_nativeGate": "blockData_of_ctrlGate",
    "not_entangling_one": "not_entangling_one_ctrl",
    "dim_of_nativeGate": "dim_of_ctrlGate", "three_of_nativeGate": "three_of_ctrlGate",
}
TYPE_MAP = {"NativeGate": "CtrlGate"}
ALLOWED_EDITS = {
    "blockData_of_orthonormal_ctrl": [(
        "            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]",
        "            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl")],
    "dim_of_ctrlGate": [(
        "    have hbal := finrank_plus_eq_finrank_minus hN hG",
        "    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC")],
}
NEW_DECLS = {"CtrlGate", "ctrlGate_of_nativeGate", "gt_center_two_ctrl", "phi_lift_minus_ctrl",
             "phi_bvec_minus_unit_ctrl", "phi_minusSpace_ctrl", "homMap_eq_self_of_orth_minusSpace",
             "actT_slice_ctrl"}
EXPORTS = ["ctrlGate_of_nativeGate", "blockData_of_ctrlGate", "dim_of_ctrlGate", "three_of_ctrlGate"]
FORBIDDEN_REFS = ["gate_actT", "Mfwd_homMap", "Minv_homMap", "Minv_Mfwd", "opGate_comp_homMap",
                  "Lop_eq_zero", "Lop_injective", "finrank_plus_eq_finrank_minus"]
OPENED = ["KInfFoundations", "TransitiveBody", "NativeGateBall", "CompositeDimension",
          "EffectSpace", "ParityNot"]
EXTERNAL_OK = {"finrank_plus_eq_finrank_minus_relC"}  # supplied by OIBridge.RelcSelectParity

HEAD = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:private\s+|protected\s+)?"
                  r"(theorem|lemma|def|abbrev|structure|instance|class|inductive)\s+"
                  r"([A-Za-z_][A-Za-z0-9_'.]*)")
IDENT = re.compile(r"(?<![A-Za-z0-9_'.])([A-Za-z_][A-Za-z0-9_']*)(?![A-Za-z0-9_'])")


def strip_comments(text):
    text = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"--[^\n]*", "", text)


def decls(text):
    lines = text.split("\n")
    heads = [(i, HEAD.match(l).group(2)) for i, l in enumerate(lines) if HEAD.match(l)]
    out = {}
    for i, name in heads:
        j = i + 1
        while j < len(lines) and not (lines[j] and not lines[j][0].isspace()):
            j += 1
        body = lines[i:j]
        while body and not body[-1].strip():
            body.pop()
        assert name not in out, name
        out[name] = body
    return out


def ren(line):
    for old in sorted({**MAP, **TYPE_MAP}, key=len, reverse=True):
        new = {**MAP, **TYPE_MAP}[old]
        line = re.sub(r"(?<![A-Za-z0-9_'.])" + re.escape(old) + r"(?![A-Za-z0-9_'])", new, line)
    return line


def check_copies(mod_text, landed_d, report):
    md = decls(mod_text)
    ok = True
    for old, new in MAP.items():
        if new not in md:
            report.append(f"V1 FAIL {new}: missing"); ok = False; continue
        exp = [ren(l) for l in landed_d[old]]
        got = md[new]
        allowed = list(ALLOWED_EDITS.get(new, []))
        if len(exp) != len(got):
            report.append(f"V1 FAIL {new}: {len(got)} lines vs landed {len(exp)}"); ok = False; continue
        diffs = [(k, e, g) for k, (e, g) in enumerate(zip(exp, got)) if e != g]
        used = []
        for k, e, g in diffs:
            if (e, g) in allowed and (e, g) not in used:
                used.append((e, g))
            else:
                report.append(f"V1 FAIL {new}: line {k}: landed {e!r} / module {g!r}"); ok = False
        if len(used) != len(allowed):
            report.append(f"V1 FAIL {new}: an allowed edit was not applied"); ok = False
        if ok:
            report.append(f"V1 ok   {new:34s} = {old} ({len(got)} lines, {len(used)} allowed edit(s))")
    return ok, md


def landed_names_with_nativegate(landed_d):
    out = set()
    for name, body in landed_d.items():
        stmt = []
        for l in body:
            stmt.append(l)
            if ":= by" in l or l.rstrip().endswith(":=") or " := " in l:
                break
        if re.search(r"\bNativeGate\b", " ".join(stmt)):
            out.add(name)
    return out


def check_closure(mod_text, md, landed_d, report):
    ok = True
    code = strip_comments(mod_text)
    ng = landed_names_with_nativegate(landed_d)
    used = set(IDENT.findall(code))
    bad = sorted((used & ng) - {"NativeGate"} - {"ctrlGate_of_nativeGate"})
    # ctrlGate_of_nativeGate legitimately mentions NativeGate as a type, not a lemma
    if bad:
        report.append(f"V4 FAIL un-renamed NativeGate lemmas referenced: {bad}"); ok = False
    else:
        report.append("V4 ok   no landed NativeGate-taking lemma is referenced un-renamed")
    # reachability
    graph = {n: set(IDENT.findall(strip_comments("\n".join(b)))) & set(md) for n, b in md.items()}
    seen, todo = set(), list(EXPORTS)
    while todo:
        n = todo.pop()
        if n in seen:
            continue
        seen.add(n)
        todo.extend(graph.get(n, ()))
    unreached = sorted(set(md) - seen)
    if unreached:
        report.append(f"V4 FAIL declarations not reachable from exports: {unreached}"); ok = False
    else:
        report.append(f"V4 ok   all {len(md)} declarations reachable from {EXPORTS}")
    return ok


def ns_decls():
    """Fully qualified OIBridge declaration names, by a namespace-stack parse of every file."""
    full = {}
    for fn in sorted(os.listdir(ROOT)):
        if not fn.endswith(".lean"):
            continue
        stack = []
        for l in strip_comments(open(os.path.join(ROOT, fn), encoding="utf-8").read()).split("\n"):
            m = re.match(r"^namespace\s+(\S+)", l)
            if m:
                stack.append(("ns", m.group(1))); continue
            m = re.match(r"^section\b\s*(\S*)", l)
            if m:
                stack.append(("sec", m.group(1))); continue
            m = re.match(r"^end\b\s*(\S*)", l)
            if m and stack:
                stack.pop(); continue
            m = HEAD.match(l)
            if m:
                ns = ".".join(x for k, x in stack if k == "ns")
                q = (ns + "." if ns else "") + m.group(2)
                full.setdefault(q, []).append(fn)
                if m.group(1) == "structure":
                    pass
    return full


def main(mod_path=MODULE, quiet=False):
    report = []
    mod_text = open(mod_path, encoding="utf-8").read()
    landed_d = decls(open(LANDED, encoding="utf-8").read())
    ok1, md = check_copies(mod_text, landed_d, report)
    extra = sorted(set(md) - set(MAP.values()) - NEW_DECLS)
    missing_new = sorted(NEW_DECLS - set(md))
    ok2 = not extra and not missing_new
    report.append(("V2 ok   " if ok2 else "V2 FAIL ") +
                  f"declarations: {len(md)} = {len(MAP)} copies + {len(NEW_DECLS)} new; "
                  f"extra={extra} missing={missing_new}")
    code = strip_comments(mod_text)
    refs = sorted({r for r in FORBIDDEN_REFS if re.search(r"(?<![A-Za-z0-9_'.])" + r + r"(?![A-Za-z0-9_'])", code)})
    relT = len(re.findall(r"\.relT\b", code))
    ng_hyp = [n for n in MAP.values() if re.search(r"\bNativeGate\b", "\n".join(md.get(n, [])))]
    ok3 = not refs and relT == 0 and not ng_hyp
    report.append(("V3 ok   " if ok3 else "V3 FAIL ") +
                  f"forbidden refs={refs} .relT projections={relT} NativeGate in copies={ng_hyp}")
    ok4 = check_closure(mod_text, md, landed_d, report)
    full = ns_decls()
    short = {}
    for q in full:
        short.setdefault(q.split(".")[-1], []).append(q)
    clash = sorted(n for n in set(md) if any(q.split(".")[-1] == n for q in full))
    ok5 = not clash
    report.append(("V5 ok   " if ok5 else "V5 FAIL ") + f"new names already declared in OIBridge: {clash}")
    visible = ["OIBridge"] + ["OIBridge." + o for o in OPENED]
    amb = []
    for tok in sorted(set(IDENT.findall(code))):
        if tok in md or tok in EXTERNAL_OK:
            continue
        cands = [q for q in short.get(tok, []) if q.rsplit(".", 1)[0] in visible]
        shadow = [q for q in short.get(tok, []) if q.rsplit(".", 1)[0] in ("OIBridge", "OIBridge.RelcSelect")]
        if len(cands) > 1 or shadow:
            amb.append((tok, cands, shadow))
    ok6 = not amb
    report.append(("V6 ok   " if ok6 else "V6 FAIL ") + f"ambiguous/shadowed identifiers: {amb}")
    sorries = len(re.findall(r"\bsorry\b|\badmit\b", code))
    ok7 = sorries == 0
    report.append(("V7 ok   " if ok7 else "V7 FAIL ") + f"sorry/admit count = {sorries}")
    allok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
    if not quiet:
        print("\n".join(report))
    return allok


def controls():
    text = open(MODULE, encoding="utf-8").read()
    import tempfile
    res = []
    # C1: change one proof token inside a copy -> V1 must fail
    m1 = text.replace("rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG]",
                      "rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG, add_zero]", 1)
    # C2: re-introduce an un-renamed NativeGate lemma reference -> V4 (and V1) must fail
    m2 = text.replace("exact Phi_hom_zero_eq_zero_ctrl hN hG hc hzc u (hom 0)",
                      "exact Phi_hom_zero_eq_zero hN hG hc hzc u (hom 0)", 1)
    # C3: re-introduce the relT step -> V1 and V3 must fail
    m3 = text.replace("            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl",
                      "            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]", 1)
    for label, mt in (("C1 mutated proof token", m1), ("C2 un-renamed reference", m2),
                      ("C3 relT step restored", m3)):
        assert mt != text, label + ": mutation did not apply"
        with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False, encoding="utf-8") as f:
            f.write(mt)
        r = main(f.name, quiet=True)
        os.unlink(f.name)
        res.append((label, not r))
        print(f"{label}: verifier {'REJECTS (control PASS)' if not r else 'ACCEPTS (control FAIL)'}")
    return all(x for _, x in res)


if __name__ == "__main__":
    a = main()
    c = controls()
    print("VERDICT:", "PASS" if a and c else "FAIL")
    sys.exit(0 if a and c else 1)

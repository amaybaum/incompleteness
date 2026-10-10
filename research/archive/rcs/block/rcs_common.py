"""Shared constants for the RELC-SELECT-1 block-module generator and its verifier.

Read-only use of the landed source at L = e2426ba4.
"""
import os
import re

SCRATCH = "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad"
LANDED = os.path.join(SCRATCH, "wt-L/verification/lean-mathlib/OIBridge/CompositeDimension.lean")
BLOCK = os.path.join(SCRATCH, "rcs/block")
TEMPLATE = os.path.join(BLOCK, "RelcSelectBlock.template.lean")
OUT = os.path.join(BLOCK, "RelcSelectBlock.lean")

# Landed declarations copied over `CtrlGate`, in landed order, with their new names.
COPIES = [
    ("gate_corner", "gate_corner_ctrl"),
    ("gate_corner_symm", "gate_corner_symm_ctrl"),
    ("Mfwd_Minv", "Mfwd_Minv_ctrl"),
    ("lor_Minv", "lor_Minv_ctrl"),
    ("gate_actC", "gate_actC_ctrl"),
    ("gate_corner_neg", "gate_corner_neg_ctrl"),
    ("gt_corner", "gt_corner_ctrl"),
    ("gt_corner_neg", "gt_corner_neg_ctrl"),
    ("gt_center", "gt_center_ctrl"),
    ("gt_tangent_corners", "gt_tangent_corners_ctrl"),
    ("gt_sphere", "gt_sphere_ctrl"),
    ("gt_sphere_corner", "gt_sphere_corner_ctrl"),
    ("Phi_sphere", "Phi_sphere_ctrl"),
    ("Phi_center", "Phi_center_ctrl"),
    ("Phi_center_all", "Phi_center_all_ctrl"),
    ("Phi_hom_zero_eq_zero", "Phi_hom_zero_eq_zero_ctrl"),
    ("Phi_lift_z_eq_zero", "Phi_lift_z_eq_zero_ctrl"),
    ("blockData_of_orthonormal", "blockData_of_orthonormal_ctrl"),
    ("blockData_of_nativeGate", "blockData_of_ctrlGate"),
    ("not_entangling_one", "not_entangling_one_ctrl"),
    ("dim_of_nativeGate", "dim_of_ctrlGate"),
    ("three_of_nativeGate", "three_of_ctrlGate"),
]

# The renaming map: every copied declaration, plus the hypothesis structure.
RENAME = dict(COPIES)
RENAME["NativeGate"] = "CtrlGate"

# Declarations that must NOT be copied (they read `relT`).
FORBIDDEN = ["gate_actT", "Mfwd_homMap", "Minv_homMap", "Minv_Mfwd", "opGate_comp_homMap",
             "Lop_eq_zero", "Lop_injective", "finrank_plus_eq_finrank_minus"]

# The only permitted non-renaming edits: (declaration, landed line after renaming, new line).
EDITS = [
    ("blockData_of_orthonormal",
     "            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]",
     "            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl"),
    ("dim_of_nativeGate",
     "    have hbal := finrank_plus_eq_finrank_minus hN hG",
     "    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC"),
]

DECL_RE = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:private\s+)?"
                     r"(theorem|lemma|def|abbrev|structure)\s+([A-Za-z_][A-Za-z0-9_'.]*)")


def rename(text):
    for old, new in sorted(RENAME.items(), key=lambda kv: -len(kv[0])):
        text = re.sub(r"(?<![A-Za-z0-9_'.])" + re.escape(old) + r"(?![A-Za-z0-9_'])", new, text)
    return text


def extract_decls(path):
    """Map declaration name -> list of lines (from the keyword line to the line before the next
    column-0 item; trailing blank lines removed). Docstrings are not part of the body."""
    lines = open(path, encoding="utf-8").read().split("\n")
    starts = []
    for i, ln in enumerate(lines):
        m = DECL_RE.match(ln)
        if m:
            starts.append((i, m.group(2)))
    out = {}
    for idx, (i, name) in enumerate(starts):
        j = i + 1
        while j < len(lines):
            ln = lines[j]
            if ln and not ln[0].isspace():
                break
            j += 1
        body = lines[i:j]
        while body and body[-1].strip() == "":
            body.pop()
        if name in out:
            raise SystemExit(f"duplicate declaration {name} in {path}")
        out[name] = (i + 1, body)
    return out

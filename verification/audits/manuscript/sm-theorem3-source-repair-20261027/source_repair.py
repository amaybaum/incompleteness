#!/usr/bin/env python3
"""Prepare, but never apply, the SM Theorem 3 source-repair draft.

Pinned after SC-17 so its accepted corrections are not overwritten. This is an
author draft, not independent acceptance or a Lean certificate. AGENTS A.34's
separate directional kernel witnesses are still required before publishing the
new equivalence. Corpus propagation, registry/coverage reconciliation and the
canonical build remain outstanding. No #918 text is changed by this tool.

Run --self-test for fragment/guard tests. In a checkout containing BASE, run
--repo PATH > proposal.patch. Every affected working file must still equal its
pinned blob; otherwise no patch is emitted. The script never writes repository
files, invokes a build, commits, pushes, or changes status classifications.
"""
from __future__ import annotations
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys

BASE = "81654257152d0efd2101b183aacef2e169959525"
PROOF = "d2e01a3a2670dab1a0f613d2dcfb7193e2608e1a"
SM_OLD = r'''**Theorem 3.** *Center independence of the lattice dynamics is equivalent to exact chiral symmetry of the emergent staggered fermions.*

*Proof.* The staggered mass term squares to $\Box_{\text{lat}}\phi = -4m_{\text{lat}}^2\phi$: center dependence. Conversely, center independence gives $D_{\text{st}}\chi = 0$, invariant under $\chi \to \varepsilon\chi$ (chiral symmetry). $\square$'''
SM_NEW = r'''**Theorem 3 (on-site terms on the fixed staggered branch).** *Work over the real or complex numbers. Let the fixed staggered hopping operator $D_{\text{st}}$ and site-parity operator $\varepsilon$ satisfy $\varepsilon^2=I$ and $\{D_{\text{st}},\varepsilon\}=0$. An on-site perturbation $C_{\mathrm{on}}$ commuting with $\varepsilon$ preserves this anticommutation exactly when $C_{\mathrm{on}}=0$. For $C_{\mathrm{on}}=m\varepsilon+p_0I$ with scalar $m,p_0$ and both parity eigenspaces nonzero, this is equivalent to $m=p_0=0$.*

*Proof.* Since $C_{\mathrm{on}}$ commutes with site parity,
$$\{D_{\text{st}}+C_{\mathrm{on}},\varepsilon\}=2C_{\mathrm{on}}\varepsilon.$$
If the anticommutator vanishes, multiplication on the right by $\varepsilon$ gives $2C_{\mathrm{on}}=0$, hence $C_{\mathrm{on}}=0$. Conversely, $C_{\mathrm{on}}=0$ leaves the assumed anticommutation of $D_{\text{st}}$ unchanged. In the scalar family, $C_{\mathrm{on}}=0$ acts on the two parity eigenspaces as $m+p_0=0$ and $-m+p_0=0$, so $m=p_0=0$; setting both coefficients to zero gives the reverse implication. $\square$

Here site parity acts as a scalar sign on each site's internal space, so an on-site block commutes with it. The fixed hopping structure is a hypothesis: zero diagonal alone does not make an arbitrary lattice operator chiral. A periodic staggered realization requires even extents. Both parity sectors are needed to identify the scalar coefficients separately, not to conclude $C_{\mathrm{on}}=0$. General operator-valued coefficients can cancel without vanishing separately.'''
CHAIN_OLD = "**Revised chain.** Center independence implies the chiral statement of Theorem 3 on the staggered branch; it is not derived here from P-indivisibility."
CHAIN_NEW = "**Scope of the structural chain.** Theorem 3 concerns on-site perturbations of the fixed first-order staggered operator, not an arbitrary microscopic update or its observer projection. The diagonal of a squared operator is a different object from its first-order on-site term."
BOOK_OLD = r'''Center independence also has a structural meaning in the fermionic description. On the staggered branch it gives exact chiral symmetry of the emergent staggered fermions: a staggered mass term squares to a center coupling, so a center-free rule carries none (SM §4.3, Theorem 3).'''
BOOK_NEW = r'''In the fermionic description, center-free refers here to the absence of an on-site term in the fixed first-order staggered operator. That operator anticommutes with site parity. Adding an on-site term $C_{\mathrm{on}}$ commuting with parity changes the anticommutator to $2C_{\mathrm{on}}\varepsilon$; over the real or complex numbers, preserving the symmetry therefore forces $C_{\mathrm{on}}=0$ (SM §4.3, Theorem 3). This argument concerns the first-order operator, not an arbitrary center term in a second-order update.'''
EXPLAINER_OLD = "**Chiral symmetry and the Higgs mechanism.** On the staggered branch, center independence — no center coupling in the update — gives exact chiral symmetry of the emergent staggered fermions, since a staggered mass term squares to a center coupling [SM §4.3, Theorem 3]."
EXPLAINER_NEW = "**Chiral symmetry and the Higgs mechanism.** On the fixed staggered branch, the first-order hopping operator anticommutes with site parity. Over the real or complex numbers, an on-site term commuting with parity preserves this symmetry only when that term vanishes [SM §4.3, Theorem 3]. A central term in the squared operator need not break this first-order symmetry."
ROADMAP_OLD = '''- Theorem 3 is formalized at operator level: {D + m·ε + p₀·1, ε} = 2m + 2p₀·ε, so center
  independence of the diagonal of D_st is equivalent to exact chirality. Per the SM
  remark, the second-order update's self-term C = 2(1−d) is the Laplacian diagonal, not a
  mass term; the statement encodes this scope.'''
ROADMAP_NEW = '''- Theorem 3's operator identity is formalized by `Chiral.center_anticommutator`:
  {D + m·ε + p₀·1, ε} = 2m + 2p₀·ε. This identity alone does not identify m and p₀
  separately. The on-site converse and scalar-coefficient identification have paper
  proofs with additional hypotheses; their directional kernel witnesses are pending.
  The second-order update's self-term C = 2(1−d) is a Laplacian diagonal, not a Dirac
  mass term; the first-order and second-order notions of center term are distinct.'''
LEAN_OLD = "{D + m·ε + p₀, ε} = (m + m) + (p₀·ε + p₀·ε) — zero iff the center terms vanish. -/"
LEAN_NEW = "{D + m·ε + p₀, ε} = (m + m) + (p₀·ε + p₀·ε) — an identity, not coefficient uniqueness. -/"
PROBE_OLD = '''C3 Theorem 3 (SM 4.3): {D + m*eps + p0, eps} = 2m + 2 p0 eps exactly — center
   independence of the diagonal of D_st iff exact chirality; (D + m*eps)^2 = D^2 + m^2.'''
PROBE_NEW = '''C3 Theorem 3 (SM 4.3): separate mass and scalar-offset anticommutator identities
   and (D + m*eps)^2 = D^2 + m^2 in concrete integer matrices; not a universal converse.'''
PRINT_OLD = 'print("C3 PASS: {D+mε+p₀, ε} = 2m·I + 2p₀·ε exactly — center-free in D_st ⟺ exact chirality; (D+mε)² = D²+m²")'
PRINT_NEW = 'print("C3 PASS: separate mass/offset anticommutator identities and (D+mε)² = D²+m² in the tested integer matrices")'

# Full-file Git blob identifiers, not hashes of the fetched excerpts.
SPECS = {
 "papers/SM.md": ("7820c79469830282646da0cd0f44e9d6949301d9", [(SM_OLD, SM_NEW), (CHAIN_OLD, CHAIN_NEW)]),
 "book/ch05-gauge-structure.md": ("ed6ffbc2211fd02bdd7221ecd013d45be7bbd102", [(BOOK_OLD, BOOK_NEW)]),
 "book/The-Incompleteness-of-Observation-FULL.md": ("a17775cd6c42e2b06eb924a0bd7ceab3d57f0eee", [(BOOK_OLD, BOOK_NEW)]),
 "papers/Explainer.md": ("6bc25794cdc9d5de0291bf7dbf091f9691ec988c", [(EXPLAINER_OLD, EXPLAINER_NEW)]),
 "verification/lean/ROADMAP.md": ("2f7838aba2b32d726a7f544680c301f1cabd3813", [(ROADMAP_OLD, ROADMAP_NEW)]),
 "verification/lean/OI_Structural_Core.lean": ("87a389f7b487cecd62223acb7b9c843347d76664", [(LEAN_OLD, LEAN_NEW)]),
 "verification/lean/structural_chain_probe.py": ("24aa1fe627bf7fdad65b00e3501b8897f6227566", [(PROBE_OLD, PROBE_NEW), (PRINT_OLD, PRINT_NEW)]),
}


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError("expected exactly one old-text occurrence")
    if new in text:
        raise ValueError("replacement text already present")
    return text.replace(old, new, 1)


def blob_hash(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          timeout=30).stdout


def numerical_ast(text: str) -> str:
    """Compare this probe with only top-level docstrings and print calls removed."""
    tree = ast.parse(text)
    tree.body = [node for node in tree.body if not (
        isinstance(node, ast.Expr) and (
            isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
            or isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "print"))]
    return ast.dump(tree, include_attributes=False)


def prepare(repo: Path) -> tuple[str, dict]:
    root = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    resolved = git(root, "rev-parse", "--verify", BASE + "^{commit}").decode().strip()
    if resolved != BASE:
        raise ValueError("base commit mismatch")
    git(root, "merge-base", "--is-ancestor", BASE, "HEAD")
    patches, records = [], []
    for name, (expected, edits) in SPECS.items():
        path = root / name
        if path.is_symlink() or path.resolve() != path:
            raise ValueError("symlink or noncanonical source path: " + name)
        original = git(root, "show", BASE + ":" + name)
        if blob_hash(original) != expected or path.read_bytes() != original:
            raise ValueError("pinned blob or working-copy mismatch: " + name)
        # Refuse to prepare against a different staged version as well.
        if git(root, "rev-parse", ":" + name).decode().strip() != expected:
            raise ValueError("index differs from pinned source: " + name)
        before = original.decode("utf-8")
        after = before
        for old, new in edits:
            after = replace_once(after, old, new)
        if name.endswith(".lean") and before.count("\n") != after.count("\n"):
            raise ValueError("Lean line count changed")
        if name.endswith("structural_chain_probe.py") and numerical_ast(before) != numerical_ast(after):
            raise ValueError("probe computation changed")
        patches.append("diff --git a/" + name + " b/" + name + "\n")
        patches.append("index " + expected + ".." + blob_hash(after.encode()) + "\n")
        patches.extend(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                          fromfile="a/" + name, tofile="b/" + name))
        records.append({"path": name, "old_blob": expected,
                        "new_blob": blob_hash(after.encode()), "replacements": len(edits)})
    return "".join(patches), {"schema": "sm-source-repair-draft-v1", "base": BASE,
        "proof_reference": PROOF, "files": records, "applied": False,
        "full_corpus_propagation_complete": False, "independent_acceptance": False,
        "required_before_landing": ["directional kernel witnesses under AGENTS A.34",
            "independent mathematical and source-scope review", "remaining corpus-site audit",
            "coverage and registry reconciliation", "canonical rebuild and full verification",
            "explicit exact-SHA merge approval"]}


def self_test() -> dict:
    checks = 0
    for _, edits in SPECS.values():
        for old, new in edits:
            fixture = "untouched-prefix\n" + old + "\nuntouched-suffix\n"
            expected = "untouched-prefix\n" + new + "\nuntouched-suffix\n"
            if replace_once(fixture, old, new) != expected:
                raise RuntimeError("positive replacement failed")
            checks += 1
            for bad in ("no matching content", old + "\n" + old, expected):
                try:
                    replace_once(bad, old, new)
                except ValueError:
                    checks += 1
                else:
                    raise RuntimeError("negative guard failed")
    if checks != 36:
        raise RuntimeError("self-test inventory changed")
    return {"schema": "sm-source-repair-fragments-v1", "checks": checks, "passed": True,
        "scope": "fragment replacement and missing/duplicate/already-applied guards only; not checkout, proof, build, or review evidence"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), indent=2, sort_keys=True))
        return
    patch, record = prepare(args.repo.resolve())
    # Every preflight completed before either output is emitted.
    print(json.dumps(record, indent=2, sort_keys=True), file=sys.stderr)
    sys.stdout.write(patch)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print("REFUSED: " + str(exc), file=sys.stderr)
        sys.exit(2)

"""A33 module generator. Usage: build_mod33.py <out.lean> <phase>. Phase 1: foundations."""
import json, sys, importlib.util
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a33/'
d = json.load(open(S + 'props33.json', encoding='utf-8'))
P, OPEN = d['props'], d['open']
RTXT = "![" + ", ".join(f"({a}, {b})" for a, b in [("(1 : Equiv.Perm (Fin 4))", "(1 : Equiv.Perm (Fin 4))"), ("(1 : Equiv.Perm (Fin 4))", "Equiv.swap (2 : Fin 4) 3"), ("(1 : Equiv.Perm (Fin 4))", "Equiv.swap (1 : Fin 4) 2"), ("Equiv.swap (2 : Fin 4) 3", "(1 : Equiv.Perm (Fin 4))"), ("Equiv.swap (2 : Fin 4) 3", "Equiv.swap (2 : Fin 4) 3"), ("Equiv.swap (2 : Fin 4) 3", "Equiv.swap (1 : Fin 4) 2"), ("Equiv.swap (1 : Fin 4) 2", "(1 : Equiv.Perm (Fin 4))"), ("Equiv.swap (1 : Fin 4) 2", "Equiv.swap (2 : Fin 4) 3"), ("Equiv.swap (1 : Fin 4) 2", "Equiv.swap (1 : Fin 4) 2")]) + "]"
tab = json.load(open(S + 'tables33.json'))
spec = importlib.util.spec_from_file_location('circ', S + 'circles.py'); circ = importlib.util.module_from_spec(spec); spec.loader.exec_module(circ)
IDX = [tuple(map(tuple, x)) for x in tab['idx']]
OUT = sys.argv[1]; PHASE = int(sys.argv[2]) if len(sys.argv) > 2 else 1

E = "EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))"
T = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
IDXT = "(Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)"
FZ = lambda z: ("FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
                f"        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}] p.1 q.1))")
MAT = lambda z: f"!![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}]"
P1, S23, S12 = "(1 : Equiv.Perm (Fin 4))", "(Equiv.swap (2 : Fin 4) 3)", "(Equiv.swap (1 : Fin 4) 2)"
R9 = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23), (S12, S12)]
CIRC = lambda r, z: f"(fun i => ({FZ(z)} ({R9[r][0]} i)).submatrix {R9[r][1]} {R9[r][1]})"
CIRCAB = lambda z: f"(fun i => ({FZ(z)} (a i)).submatrix b b)"
MSGN = "(fun x y : Fin 4 => if 1 ≤ x.val ∧ 1 ≤ y.val ∧ x ≠ y then (-1 : ℂ) else 1)"
MEXP = "(fun x y : Fin 4 => if x.val % 2 = 1 ∧ y.val % 2 = 1 then 1 else 0)"
HX = "  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0\n"
UNIT = """  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : star z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
"""
def idx(p):
    (a, b, c), (x, y, w) = p
    return f"(({a}, {b}, {c}), ({x}, {y}, {w}))"

out = ["import OIBridge.OrbitGeometryRigidity", "",
       "/-! Act 33 — development module (disposable). -/", "",
       "namespace OIBridge", "namespace OrbitIsometryGroup", "", OPEN.rstrip("\n"), ""]
names = []


def thm(nm, stmt, proof):
    names.append(nm)
    out.append(f"theorem {nm} :\n    {stmt} := by\n{proof.rstrip()}\n#print axioms {nm}\n")



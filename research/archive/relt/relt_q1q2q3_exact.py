"""REL-T, nodes N1-N3: exact computation (sympy Rational).

Q1/Q2: the controlled-N gate G = Pi_a (x) I + Pi_b (x) homMap N meets IsNot, the frame, relT and
invertibility in every dimension, for every NOT N; relC fails exactly when Pi_a, Pi_b are not exchanged
by homMap N. Explicit even-d countermodels at d = 2 and d = 4; the parity map of DIM-1 stays injective
(relT) and loses its anticommutation (relC).
Q3: the same construction at d = 3 with PARITY-NOT-1's refl3 and negId3.

Controls:
  positive  : DIM-1's cnot with nflip at d = 3 reproduces cnot_frame, cnot_relT, cnot_relC, the
              parity map is injective and anticommutes, and the eigenspaces are (2, 2);
              PARITY-NOT-1's gJ3_value = -1/10 is reproduced by the same evaluator.
  counter   : the controlled-N gate must FAIL relC (else the construction would contradict the landed
              not_even_of_gateRel); refl3/negId3 must fail relC with every gate tried.
"""
import sys
from relt_common import *

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


# ---------------- positive control: DIM-1 cnot / nflip ----------------
z3 = col(0, 0, 1)
nflip = diagN([1, -1, -1])
G = dim1_cnot()
check("PC cnot: IsNot nflip", all(isNot(z3, nflip).values()))
check("PC cnot: frame (cnot_frame)", frame(G, z3))
check("PC cnot: relT (cnot_relT)", relT(G, nflip))
check("PC cnot: relC (cnot_relC)", relC(G, nflip))
check("PC cnot: invertible", invertible(G))
check("PC cnot: eigen dims (2,2)", eig_dims(nflip) == (2, 2))
pd = parity_map_data(G, nflip)
check("PC cnot: Lop injective and anticommuting", pd["injective"] and pd["anti"])
check("PC cnot: ker(Pop-1) = ker(Pop+1)", pd["ker_P_minus_1"] == pd["ker_P_plus_1"])
# reproduce gJ3_value = -1/10
odd3 = [False, False, True, True]
perm3 = [3, 2, 1, 0]
gJ3 = sgate(odd3, perm3, 4)
w3 = col(0, R(-3, 5), R(-4, 5))
xplus = col(1, 0, 0)
val = pairVal(sharpVec(w3), sharpVec(z3), apply(gJ3, prod(xplus, z3)))
check("PC gJ3_value = -1/10 reproduced", val == R(-1, 10))
check("PC gJ3 relT and relC (gateRel_gJ3)", relT(gJ3, nflip) and relC(gJ3, nflip))

# ---------------- Q1/Q2: even-d countermodels ----------------
cases = {
    "CM2r d=2 N=diag(1,-1)": (col(0, 1), diagN([1, -1])),
    "CM2n d=2 N=-id": (col(0, 1), diagN([-1, -1])),
    "CM4r d=4 N=diag(1,1,1,-1)": (col(0, 0, 0, 1), diagN([1, 1, 1, -1])),
    "CM4m d=4 N=diag(1,-1,-1,-1)": (col(0, 0, 0, 1), diagN([1, -1, -1, -1])),
    "CM4n d=4 N=-id": (col(0, 0, 0, 1), diagN([-1, -1, -1, -1])),
}
for name, (z, N) in cases.items():
    G, Pa, Pb = controlled_N_gate(z, N)
    n = z.shape[0] + 1
    check(name + ": IsNot", all(isNot(z, N).values()))
    check(name + ": frame", frame(G, z))
    check(name + ": relT", relT(G, N))
    check(name + ": G^2 = I (invertible)", (G * G - eye(n * n)).is_zero_matrix)
    check(name + ": relC FAILS (countercontrol)", not relC(G, N))
    p, m = eig_dims(N)
    check(name + f": eigenspaces unbalanced ({p},{m}), d even", p != m and (n - 1) % 2 == 0)
    pd = parity_map_data(G, N)
    check(name + ": parity map Lop injective (relT step survives)", pd["injective"])
    check(name + ": parity map Lop NOT anticommuting (relC step lost)", not pd["anti"])
    # posFwd failure witness: x = e1 (tangent), y = z, control effect (1,-1,0..), target effect hom(-z)
    d = n - 1
    x = zeros(d, 1); x[0] = 1
    e = zeros(n, 1); e[0] = 1; e[1] = -1
    f = hom(-z)
    v = pairVal(e, f, apply(G, prod(x, z)))
    check(name + f": posFwd fails, value {v} < 0 with Lor effects", v < 0 and lor(e) and lor(f))

# the relC criterion for the controlled-N family: relC <=> homMap N exchanges Pi_a and Pi_b
for name, (z, N) in cases.items():
    G, Pa, Pb = controlled_N_gate(z, N)
    Nh = homMap(N)
    exch = (Nh * Pa * Nh - Pb).is_zero_matrix
    check(name + ": relC <-> (N Pi_a N = Pi_b) agrees", exch == relC(G, N))

# ---------------- Q3: d = 3, refl3 and negId3 ----------------
refl3 = diagN([1, 1, -1])
negId3 = diagN([-1, -1, -1])
for name, N in [("refl3", refl3), ("negId3", negId3)]:
    G, Pa, Pb = controlled_N_gate(z3, N)
    check(f"Q3 {name}: IsNot", all(isNot(z3, N).values()))
    check(f"Q3 {name}: det = -1", N.det() == -1)
    check(f"Q3 {name}: controlled-N gate frame", frame(G, z3))
    check(f"Q3 {name}: controlled-N gate relT", relT(G, N))
    check(f"Q3 {name}: controlled-N gate invertible (G^2=I)", (G * G - eye(16)).is_zero_matrix)
    check(f"Q3 {name}: relC fails (consistent with not_gateRel_{name})", not relC(G, N))
    # cnot with this N: relT must fail (computed in the written analysis: Ad_CNOT does not commute)
    check(f"Q3 {name}: DIM-1 cnot does not satisfy relT with {name}", not relT(dim1_cnot(), N))
# nflip with the controlled-N gate: relC fails too (Pi_a has rank 1, Pi_b rank 3: never exchanged)
G, Pa, Pb = controlled_N_gate(z3, nflip)
check("Q3 nflip: controlled-N gate relT, frame; relC fails (rank 1 vs 3)",
      relT(G, nflip) and frame(G, z3) and not relC(G, nflip))

# countercontrols for the frame evaluator
z2 = col(0, 1); N2 = diagN([1, -1]); n2 = 3
check("CC identity gate: relT holds, frame FAILS (frame is what the even-d positivity exclusions read)",
      relT(eye(9), N2) and not frame(eye(9), z2))
hm = hom(-z2); Pa_bad = hm * hm.T / 2; Pb_bad = eye(3) - Pa_bad; Nh2 = homMap(N2)
Gbad = gate_from_fun(lambda w: Pa_bad * w + Pb_bad * w * Nh2.T, 3)
check("CC controlled-N gate with the wrong corner projector: relT holds, frame FAILS", relT(Gbad, N2) and not frame(Gbad, z2))

npass = sum(1 for _, c in checks if c)
print(f"relt_q1q2q3_exact: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)

"""
colors.py — SU(3) fundamental-rep generators T^a = λ^a/2, structure constants,
and color-trace helpers for the Γ_3 calculation.

Convention:  T(R) = 1/2,  [T^a, T^b] = i f^{abc} T^c,  {T^a, T^b} = (1/3)δ^{ab} 𝟙 + d^{abc} T^c.
Then:  Tr[T^a T^b T^c] = (1/4)(d^{abc} + i f^{abc}).
"""
import numpy as np

# --- Gell-Mann matrices λ^1..λ^8 ---
_l = [None]*9
_l[1] = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
_l[2] = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
_l[3] = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
_l[4] = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
_l[5] = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
_l[6] = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
_l[7] = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
_l[8] = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / np.sqrt(3)

# T^a = λ^a / 2. Index 1..8 (T[0] is None to align indices).
T = [None] + [_l[a]/2.0 for a in range(1, 9)]


def trace3(a, b, c):
    """Tr[T^a T^b T^c] for SU(3) fundamental. Returns complex scalar."""
    return np.trace(T[a] @ T[b] @ T[c])


def f_abc(a, b, c):
    """Structure constant f^{abc} from [T^a, T^b] = i f^{abc} T^c.
    Computed numerically: f^{abc} = -2i · Tr([T^a, T^b] T^c).
    """
    return np.real(-2j * np.trace((T[a]@T[b] - T[b]@T[a]) @ T[c]))


def d_abc(a, b, c):
    """Structure constant d^{abc} from {T^a, T^b} = (1/3)δ^{ab}𝟙 + d^{abc} T^c.
    Computed numerically: d^{abc} = 2 · Tr({T^a, T^b} T^c).
    """
    return np.real(2 * np.trace((T[a]@T[b] + T[b]@T[a]) @ T[c]))


# --- Sanity tables ---
if __name__ == "__main__":
    # Known: f_{123} = 1, f_{147}=f_{246}=f_{257}=f_{345}=1/2,
    #        f_{156}=f_{367}=-1/2, f_{458}=f_{678}=sqrt(3)/2
    # d_{118}=d_{228}=d_{338}=1/sqrt(3), d_{888}=-1/sqrt(3),
    # d_{146}=d_{157}=d_{247}=d_{344}=d_{355}=1/2,
    # d_{256}=-1/2, d_{366}=d_{377}=-1/2
    print("=== SU(3) structure constants self-test ===")
    print(f"f(1,2,3)   = {f_abc(1,2,3):.6f}    expect  1")
    print(f"f(1,4,7)   = {f_abc(1,4,7):.6f}    expect  0.5")
    print(f"f(4,5,8)   = {f_abc(4,5,8):.6f}    expect  √3/2 = {np.sqrt(3)/2:.6f}")
    print(f"d(1,1,8)   = {d_abc(1,1,8):.6f}    expect  1/√3 = {1/np.sqrt(3):.6f}")
    print(f"d(1,2,3)   = {d_abc(1,2,3):.6f}    expect  0")
    print(f"d(1,4,6)   = {d_abc(1,4,6):.6f}    expect  0.5")
    print(f"d(8,8,8)   = {d_abc(8,8,8):.6f}    expect  -1/√3 = {-1/np.sqrt(3):.6f}")
    print()
    # Check Tr[T^a T^b T^c] = (1/4)(d + i f):
    for (a, b, c) in [(1,2,3), (1,4,6), (1,1,8), (4,5,8)]:
        tr = trace3(a, b, c)
        expected = 0.25 * (d_abc(a,b,c) + 1j*f_abc(a,b,c))
        err = abs(tr - expected)
        print(f"Tr[T^{a}T^{b}T^{c}] = {tr:.6f}   expected  {expected:.6f}   err={err:.1e}")

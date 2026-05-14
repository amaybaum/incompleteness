"""
c_topology_wrapper.py — Python wrappers around the compiled C binaries for
the O(N^8) topologies (T1a, T1b, G_a, G_b, G_c). Falls back to numpy for
the O(N^4) topologies (T1c, T1d, T1e, G_d).

Each wrapper has the same signature as the corresponding numpy *_sigma function,
returning a 4×4 numpy array.

Validated at N=4 and N=6 to machine precision (≤ 1e-13 max abs diff vs numpy).

Speedups over numpy at N=6 (m_reg=0.2):
  T1a: ~5x       T1b: ~7x       G_a: ~22x      G_b: ~5x       G_c: ~9x

C binaries built in ./c_lib/ via:
  gcc -O3 -fopenmp -ffast-math -march=native <topology>.c -o <topology> -lm
"""
import numpy as np
import subprocess
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
C_LIB_DIR = os.path.join(HERE, "c_lib")
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

# Numpy fallbacks (for O(N^4) topologies that don't need C)

from T1c_V4g_bubble import V4g_bubble_sigma
from T1d_V4g_tadpole import V4g_tadpole_sigma
from T1e_V4g_triple_line import V4g_triple_line_sigma
from G_d_V4g_ghost_bubble import V4g_ghost_bubble_sigma


def _call_c_binary(binary, N, p_ext, m_reg, threads=None):
    """Call a C topology binary, parse 16-double output into 4×4 Σ.

    Currently only supports p_ext = (p0, 0, 0, 0) (along ê_0). For other
    directions we'd need to either generalize the C binaries or rotate the
    grid before calling. This is fine for the current p-extrapolation
    pattern which only varies p along ê_0.
    """
    p_arr = np.asarray(p_ext, dtype=float)
    # Verify p along ê_0 (other components zero)
    if not (abs(p_arr[1]) < 1e-12 and abs(p_arr[2]) < 1e-12 and abs(p_arr[3]) < 1e-12):
        raise ValueError(f"C wrapper currently requires p along ê_0; got {p_arr}")
    p0 = float(p_arr[0])

    args = [os.path.join(C_LIB_DIR, binary), str(N), str(m_reg), str(p0)]
    if threads is not None:
        args.append(str(threads))

    result = subprocess.run(args, capture_output=True, text=True, check=True)
    vals = list(map(float, result.stdout.strip().split()))
    if len(vals) != 16:
        raise RuntimeError(f"Expected 16 values from C binary, got {len(vals)}: {result.stdout[:200]}")
    return np.array(vals).reshape(4, 4)


# === O(N^8) topologies in C ===

def kite_sigma_C(N, p_ext, m_reg, **_):
    """C version of T1a kite. Same signature as kite_sigma."""
    return _call_c_binary("kite_T1a", N, p_ext, m_reg)


def vertex_correction_sigma_C(N, p_ext, m_reg, **_):
    """C version of T1b vertex correction."""
    return _call_c_binary("vertex_T1b", N, p_ext, m_reg)


def ghost_square_sigma_C(N, p_ext, m_reg, **_):
    """C version of G_a ghost-square."""
    return _call_c_binary("ghost_Ga", N, p_ext, m_reg)


def ghost_vertex_correction_sigma_C(N, p_ext, m_reg, **_):
    """C version of G_b ghost vertex correction."""
    return _call_c_binary("ghost_Gb", N, p_ext, m_reg)


def ghost_triangle_sigma_C(N, p_ext, m_reg, **_):
    """C version of G_c ghost-triangle."""
    return _call_c_binary("ghost_Gc", N, p_ext, m_reg)


# === Hybrid driver ===

def compute_all_sigmas_at_p_C(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν} for all 9 topologies at (N, p_ext, m_reg).

    Uses C binaries for O(N^8) topologies, numpy for O(N^4) ones.
    Returns dict keyed by topology name.
    """
    import time
    sigmas = {}
    timings = {}

    # O(N^8) — use C
    for name, fn in [
        ('T1a', kite_sigma_C),
        ('T1b', vertex_correction_sigma_C),
        ('G_a', ghost_square_sigma_C),
        ('G_b', ghost_vertex_correction_sigma_C),
        ('G_c', ghost_triangle_sigma_C),
    ]:
        t0 = time.time()
        sigmas[name] = fn(N, p_ext, m_reg)
        timings[name] = time.time() - t0
        if verbose:
            print(f"      {name} (C): {timings[name]:.2f}s")

    # O(N^4) — numpy is plenty fast
    for name, fn in [
        ('T1c', V4g_bubble_sigma),
        ('T1d', V4g_tadpole_sigma),
        ('T1e', V4g_triple_line_sigma),
        ('G_d', V4g_ghost_bubble_sigma),
    ]:
        t0 = time.time()
        sigmas[name] = fn(N, p_ext, m_reg)
        timings[name] = time.time() - t0
        if verbose:
            print(f"      {name} (np): {timings[name]:.2f}s")

    return sigmas, timings


if __name__ == "__main__":
    # Quick self-test
    import time
    print("=== c_topology_wrapper self-test ===\n")
    for N in [4, 6]:
        m, p0 = 0.2, 2*np.pi/N
        p_ext = [p0, 0, 0, 0]
        print(f"--- N={N}, m_reg={m}, p_ext = (κ, 0, 0, 0) ---")
        t_total = time.time()
        sigmas, _ = compute_all_sigmas_at_p_C(N, p_ext, m, verbose=True)
        print(f"  Total: {time.time() - t_total:.2f}s")
        # Sanity-check Π_T values
        p2_lat = (2 * np.sin(p0/2))**2
        for k, sigma in sigmas.items():
            pi_t = (sigma[1,1] - sigma[0,0]) / p2_lat
            print(f"  {k}: Π_T = {pi_t:+.4e}")
        print()

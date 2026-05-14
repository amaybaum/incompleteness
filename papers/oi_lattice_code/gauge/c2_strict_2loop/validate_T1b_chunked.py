"""
validate_T1b_chunked.py — Verify vertex_T1b_chunked matches vertex_T1b.

Run vertex_T1b at (N, p0) -> Σ_unchunked (with prefactors applied)
Run vertex_T1b_chunked for chunk 0..K-1 -> sum chunks * (0.5/N^8) -> Σ_chunked
Assert |Σ_unchunked - Σ_chunked| < 1e-12 (machine precision).
"""
import numpy as np
import subprocess
import sys
import os

C_LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "c_lib")


def run_unchunked(N, m_reg, p0):
    args = [os.path.join(C_LIB, "vertex_T1b"), str(N), str(m_reg), str(p0)]
    out = subprocess.run(args, capture_output=True, text=True, check=True)
    vals = list(map(float, out.stdout.strip().split()))
    return np.array(vals).reshape(4, 4)


def run_chunked(N, m_reg, p0, num_chunks):
    Npts = N ** 4
    accum = np.zeros((4, 4))
    for c in range(num_chunks):
        args = [os.path.join(C_LIB, "vertex_T1b_chunked"),
                str(N), str(m_reg), str(p0), str(c), str(num_chunks)]
        out = subprocess.run(args, capture_output=True, text=True, check=True)
        vals = list(map(float, out.stdout.strip().split()))
        accum += np.array(vals).reshape(4, 4)
    # Apply final prefactor: 0.5 (sym) * (1/N^4)^2 (two integrals)
    accum *= 0.5 / Npts ** 2
    return accum


def main():
    cases = [
        (4, 0.2, 2 * np.pi / 4),
        (6, 0.2, 2 * np.pi / 6),
        (6, 0.2, 2 * 2 * np.pi / 6),
    ]

    print("Validating vertex_T1b_chunked against vertex_T1b:")
    print()
    print(f"{'N':>3}  {'p0':>7}  {'chunks':>6}  {'max |Σ_chk - Σ|':>17}  "
          f"{'(Σ^11 - Σ^00)':>14}  {'OK?':>4}")
    print("-" * 75)

    for N, m_reg, p0 in cases:
        Sigma_un = run_unchunked(N, m_reg, p0)
        for nc in [2, 4, 8]:
            Sigma_ch = run_chunked(N, m_reg, p0, nc)
            diff = np.max(np.abs(Sigma_un - Sigma_ch))
            pi_t = (Sigma_ch[1, 1] - Sigma_ch[0, 0])
            ok = "YES" if diff < 1e-12 else "NO"
            print(f"{N:>3}  {p0:>7.4f}  {nc:>6d}  {diff:>17.4e}  "
                  f"{pi_t:>+14.4e}  {ok:>4}")
        print()

    print("If all OK, vertex_T1b_chunked is bit-equivalent (to 1e-12) with vertex_T1b.")


if __name__ == "__main__":
    main()

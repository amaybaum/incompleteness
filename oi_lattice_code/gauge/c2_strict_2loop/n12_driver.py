"""
n12_driver.py — Run the c_2(N=12) sequence with persistent state.

Strategy: enumerate every per-topology, per-lambda task as a discrete unit
(T1a/T1b chunks broken out individually). Track status in a JSON state file.
Each invocation runs as many pending tasks as fit in BUDGET_SEC, then exits.
Reinvoke until everything is done.

Usage:
  python3 n12_driver.py [BUDGET_SEC]
  python3 n12_driver.py status        # just print state
  python3 n12_driver.py aggregate     # finalize: combine into per-lambda
                                      # sigma sums, run p-extrap, append to
                                      # global c_2(N) sequence.

Run conditions: N=12, m_reg=0.2, m_f=0.05, lambdas=(1,2,3), aligned with
the existing N=6,8,10 sequence in c2_N_sequence.json.
"""
import json
import os
import sys
import time
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

C_LIB = os.path.join(HERE, "c_lib")

STATE_FILE = os.path.join(DATA, "n12_state.json")

N = 12
M_REG = 0.2
M_F = 0.05
LAMBDAS = [1, 2, 3]
T1A_NUM_CHUNKS = 32   # ~19s each at N=12
T1B_NUM_CHUNKS = 4    # ~50s each at N=12

DEFAULT_BUDGET_SEC = 60


def kappa(): return 2 * np.pi / N


def p_ext_for_lam(lam):
    return [lam * kappa(), 0.0, 0.0, 0.0]


def fresh_state():
    state = {
        "N": N, "m_reg": M_REG, "m_f": M_F,
        "lambdas": LAMBDAS, "tasks": {}
    }
    for lam in LAMBDAS:
        # numpy O(N^4) topologies
        for top in ["T1c", "T1d", "T1e", "G_d"]:
            state["tasks"][f"lam{lam}_{top}"] = {"status": "pending", "kind": "numpy"}
        # C O(N^8) ghost (single call)
        for top in ["G_a", "G_b", "G_c"]:
            state["tasks"][f"lam{lam}_{top}"] = {"status": "pending", "kind": "c_single"}
        # T1b chunked
        for c in range(T1B_NUM_CHUNKS):
            state["tasks"][f"lam{lam}_T1b_chunk_{c}of{T1B_NUM_CHUNKS}"] = \
                {"status": "pending", "kind": "c_chunk_T1b", "chunk_idx": c, "num_chunks": T1B_NUM_CHUNKS}
        # T1a chunked
        for c in range(T1A_NUM_CHUNKS):
            state["tasks"][f"lam{lam}_T1a_chunk_{c}of{T1A_NUM_CHUNKS}"] = \
                {"status": "pending", "kind": "c_chunk_T1a", "chunk_idx": c, "num_chunks": T1A_NUM_CHUNKS}
        # std-QCD LO intercept (for capture and iterated subtraction)
        state["tasks"][f"lam{lam}_stdQCD"] = {"status": "pending", "kind": "stdqcd"}
    return state


def load_state():
    if not os.path.exists(STATE_FILE):
        s = fresh_state()
        with open(STATE_FILE, "w") as f: json.dump(s, f, indent=2)
        return s
    with open(STATE_FILE) as f: return json.load(f)


def save_state(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f: json.dump(state, f, indent=2)
    os.replace(tmp, STATE_FILE)


# === Per-task runners ===

def run_numpy_topology(top, lam):
    """Run an O(N^4) numpy topology at (N, lambda)."""
    p_ext = np.array(p_ext_for_lam(lam))
    if top == "T1c":
        from T1c_V4g_bubble import V4g_bubble_sigma
        sigma = V4g_bubble_sigma(N, p_ext, M_REG)
    elif top == "T1d":
        from T1d_V4g_tadpole import V4g_tadpole_sigma
        sigma = V4g_tadpole_sigma(N, p_ext, M_REG)
    elif top == "T1e":
        from T1e_V4g_triple_line import V4g_triple_line_sigma
        sigma = V4g_triple_line_sigma(N, p_ext, M_REG)
    elif top == "G_d":
        from G_d_V4g_ghost_bubble import V4g_ghost_bubble_sigma
        sigma = V4g_ghost_bubble_sigma(N, p_ext, M_REG)
    else:
        raise ValueError(f"Unknown numpy topology: {top}")
    return sigma.tolist()


C_BINARIES = {
    "G_a": "ghost_Ga", "G_b": "ghost_Gb", "G_c": "ghost_Gc",
}


def run_c_single(top, lam):
    """Run an O(N^8) C ghost binary as a single call."""
    binary = C_BINARIES[top]
    p_ext = p_ext_for_lam(lam)
    args = [os.path.join(C_LIB, binary), str(N), str(M_REG), str(p_ext[0])]
    out = subprocess.run(args, capture_output=True, text=True, check=True)
    vals = list(map(float, out.stdout.strip().split()))
    sigma = np.array(vals).reshape(4, 4)
    return sigma.tolist()


def run_c_chunk(top_label, lam, chunk_idx, num_chunks):
    """Run a single chunk of T1a or T1b. Returns PARTIAL sigma (no prefactor)."""
    binary = "kite_T1a_chunked" if top_label == "T1a" else "vertex_T1b_chunked"
    p_ext = p_ext_for_lam(lam)
    args = [os.path.join(C_LIB, binary),
            str(N), str(M_REG), str(p_ext[0]),
            str(chunk_idx), str(num_chunks)]
    out = subprocess.run(args, capture_output=True, text=True, check=True)
    vals = list(map(float, out.stdout.strip().split()))
    sigma_partial = np.array(vals).reshape(4, 4)
    return sigma_partial.tolist()


def run_stdqcd(lam):
    """Std-QCD bubble + ghost at (N, lambda) -> Π_T."""
    from qcd_crosscheck import bubble_standard_qcd, ghost_standard_qcd
    p_ext = np.array(p_ext_for_lam(lam))
    Sigma_b = bubble_standard_qcd(N, p_ext, m_reg=M_REG)
    Sigma_g = ghost_standard_qcd(N, p_ext, m_reg=M_REG)
    Sigma = Sigma_b + Sigma_g
    p2_lat = (2 * np.sin(p_ext[0] / 2)) ** 2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return {"Pi_T": Pi_T, "p2_lat": p2_lat,
            "Sigma_total": Sigma.tolist(),
            "Sigma_bubble": Sigma_b.tolist(),
            "Sigma_ghost": Sigma_g.tolist()}


# === Orchestration ===

def run_one(task_name, task):
    """Dispatch and run one task. Returns updated task dict."""
    # Strip "lamX_" prefix; the remainder is the topology / chunk descriptor.
    rest = task_name.split("_", 1)[1]            # e.g. "G_d" / "T1a_chunk_0of32"
    lam = int(task_name.split("_", 1)[0][3:])     # "lam1" -> 1
    kind = task["kind"]
    t0 = time.time()
    if kind == "numpy":
        # rest is the topology name directly: T1c, T1d, T1e, G_d
        top = rest
        result = run_numpy_topology(top, lam)
        task["sigma"] = result
    elif kind == "c_single":
        top = rest                                # G_a, G_b, G_c
        result = run_c_single(top, lam)
        task["sigma"] = result
    elif kind == "c_chunk_T1a":
        result = run_c_chunk("T1a", lam, task["chunk_idx"], task["num_chunks"])
        task["sigma_partial"] = result
    elif kind == "c_chunk_T1b":
        result = run_c_chunk("T1b", lam, task["chunk_idx"], task["num_chunks"])
        task["sigma_partial"] = result
    elif kind == "stdqcd":
        result = run_stdqcd(lam)
        task.update(result)
    else:
        raise ValueError(f"Unknown task kind: {kind}")
    task["status"] = "done"
    task["wall_time_s"] = time.time() - t0
    return task


def status(state):
    by_status = {"pending": 0, "done": 0, "error": 0}
    by_kind = {}
    for name, task in state["tasks"].items():
        s = task.get("status", "pending")
        by_status[s] = by_status.get(s, 0) + 1
        k = task["kind"]
        by_kind.setdefault(k, {"pending": 0, "done": 0, "error": 0})
        by_kind[k][s] = by_kind[k].get(s, 0) + 1
    print(f"\nN={N} state: {by_status}")
    print("By kind:")
    for k, counts in sorted(by_kind.items()):
        print(f"  {k}: {counts}")
    # Show per-lambda summary
    print("\nPer-lambda completion:")
    for lam in LAMBDAS:
        prefix = f"lam{lam}_"
        relevant = [t for n, t in state["tasks"].items() if n.startswith(prefix)]
        n_done = sum(1 for t in relevant if t.get("status") == "done")
        print(f"  lambda={lam}: {n_done}/{len(relevant)} done")


def drive(budget_sec):
    state = load_state()
    pending = [(n, t) for n, t in state["tasks"].items() if t.get("status") != "done"]
    if not pending:
        print("All tasks already complete. Use 'aggregate' to finalize.")
        return
    print(f"Driving with budget {budget_sec}s. {len(pending)} tasks pending.")
    t_start = time.time()
    n_done_this_run = 0
    # Order: cheapest first
    order_priority = {
        "numpy": 0, "stdqcd": 1, "c_single": 2,
        "c_chunk_T1b": 3, "c_chunk_T1a": 4
    }
    pending.sort(key=lambda nt: (order_priority.get(nt[1]["kind"], 99), nt[0]))
    for name, task in pending:
        elapsed = time.time() - t_start
        if elapsed >= budget_sec:
            print(f"  ⏸  budget reached ({elapsed:.0f}s); pausing. Re-invoke to continue.")
            break
        try:
            t0 = time.time()
            task = run_one(name, task)
            state["tasks"][name] = task
            save_state(state)  # persist after each task
            dt = time.time() - t0
            print(f"  ✓ {name} ({task['kind']}, {dt:.1f}s)")
            n_done_this_run += 1
        except subprocess.CalledProcessError as e:
            task["status"] = "error"
            task["error"] = str(e)
            state["tasks"][name] = task
            save_state(state)
            print(f"  ✗ {name}: {e}")
        except Exception as e:
            task["status"] = "error"
            task["error"] = str(e)
            state["tasks"][name] = task
            save_state(state)
            print(f"  ✗ {name}: {e}")
    print(f"\nThis run: {n_done_this_run} tasks completed in "
          f"{time.time()-t_start:.1f}s")
    pending_after = sum(1 for t in state["tasks"].values()
                         if t.get("status") != "done")
    print(f"Remaining pending: {pending_after} of {len(state['tasks'])}")


def aggregate():
    """Combine all per-task outputs into per-lambda sigma matrices,
    apply prefactors for chunked ones, run p-extrapolation, and report."""
    from paper_pi_s import compute_pi_s
    from A5_OI_p_extrapolation_C import (
        extract_PiT_at_p, total_OI_PiT_at_p, small_p_fit,
    )

    state = load_state()
    # Verify all tasks done
    incomplete = [n for n, t in state["tasks"].items() if t.get("status") != "done"]
    if incomplete:
        print(f"Cannot aggregate: {len(incomplete)} tasks still pending/errored.")
        for name in incomplete[:5]:
            print(f"  {name}: {state['tasks'][name].get('status')}")
        return

    pi_s = compute_pi_s(N, M_F)
    print(f"\nN={N}, m_reg={M_REG}, m_f={M_F}, Π_s = {pi_s:.5f}")
    print()

    # Reconstruct per-(lambda, topology) sigma
    Npts = N ** 4

    # Per-topology induced prop count (matches A5_OI_p_extrapolation_C.py)
    N_INDUCED_PROPS = {
        'T1a': 5, 'T1b': 5, 'T1c': 4, 'T1d': 4, 'T1e': 3,
        'G_a': 5, 'G_b': 5, 'G_c': 5, 'G_d': 4,
    }

    p2_lats = []
    PiT_PiS2_vals = []
    per_lambda_data = []
    stdqcd_per_lam = {}

    for lam in LAMBDAS:
        sigmas = {}
        for top in ["T1c", "T1d", "T1e", "G_d"]:
            sigmas[top] = np.array(state["tasks"][f"lam{lam}_{top}"]["sigma"])
        for top in ["G_a", "G_b", "G_c"]:
            sigmas[top] = np.array(state["tasks"][f"lam{lam}_{top}"]["sigma"])
        # T1a: sum chunks, multiply by 0.5 / N^8
        T1a_partial_sum = np.zeros((4, 4))
        for c in range(T1A_NUM_CHUNKS):
            T1a_partial_sum += np.array(
                state["tasks"][f"lam{lam}_T1a_chunk_{c}of{T1A_NUM_CHUNKS}"]["sigma_partial"])
        sigmas["T1a"] = T1a_partial_sum * (0.5 / Npts ** 2)
        # T1b: sum chunks, multiply by 0.5 / N^8
        T1b_partial_sum = np.zeros((4, 4))
        for c in range(T1B_NUM_CHUNKS):
            T1b_partial_sum += np.array(
                state["tasks"][f"lam{lam}_T1b_chunk_{c}of{T1B_NUM_CHUNKS}"]["sigma_partial"])
        sigmas["T1b"] = T1b_partial_sum * (0.5 / Npts ** 2)
        # std-QCD
        stdqcd_per_lam[lam] = state["tasks"][f"lam{lam}_stdQCD"]

        # OI total Π_T·Π_s²
        p_ext = np.array(p_ext_for_lam(lam))
        total_PiT_PiS2, contribs = total_OI_PiT_at_p(sigmas, p_ext, pi_s)
        p2_lat = (2 * np.sin(p_ext[0] / 2)) ** 2

        p2_lats.append(p2_lat)
        PiT_PiS2_vals.append(total_PiT_PiS2)

        # Per-topology Π_T (induced)
        per_top_pi_T = {}
        for top in sigmas:
            pi_T_std = extract_PiT_at_p(sigmas[top], p_ext)
            per_top_pi_T[top] = float(pi_T_std)

        per_lambda_data.append({
            "lam": lam, "p2_lat": float(p2_lat),
            "Pi_T_PiS2": float(total_PiT_PiS2),
            "per_top_PiT_std": per_top_pi_T,
            "per_top_OI_contrib": {k: float(v) for k, v in contribs.items()},
        })
        print(f"  λ={lam}: p̂²={p2_lat:.4f}, Π_T·Π_s²={total_PiT_PiS2:+.5e}")

    # Linear fit
    p2_arr = np.array(p2_lats)
    PiT_arr = np.array(PiT_PiS2_vals)
    intercept, slope = small_p_fit(p2_arr, PiT_arr)
    print(f"\n  Linear fit: intercept = {intercept:+.5e}, slope = {slope:+.5e}")
    print()

    # Std-QCD intercept (LO)
    stdqcd_p2 = []; stdqcd_Pi = []
    for lam in LAMBDAS:
        d = stdqcd_per_lam[lam]
        stdqcd_p2.append(d["p2_lat"])
        stdqcd_Pi.append(d["Pi_T"])
    stdqcd_p2 = np.array(stdqcd_p2); stdqcd_Pi = np.array(stdqcd_Pi)
    coef = np.polyfit(stdqcd_p2, stdqcd_Pi, 1)
    intercept_LO = float(coef[1])
    slope_LO = float(coef[0])
    print(f"  Std-QCD LO intercept: {intercept_LO:+.5e}, slope: {slope_LO:+.5e}")

    B0 = 11.0 / 3.0
    Pi_T_exp = -B0 / (16 * np.pi ** 2) * np.log(np.pi ** 2 / M_REG ** 2)
    capture = stdqcd_Pi[0] / Pi_T_exp  # at lambda=1, matching the LO convention
    print(f"  capture(N={N}, m_reg={M_REG}) = {capture:.4f}")
    print()

    # Save into c2_N_sequence.json (preserve existing N=6,8,10)
    seq_path = os.path.join(DATA, "c2_N_sequence.json")
    with open(seq_path) as f:
        seq = json.load(f)
    seq[str(N)] = {
        "pi_s": float(pi_s),
        "intercept": float(intercept),
        "slope": float(slope),
    }
    with open(seq_path, "w") as f:
        json.dump(seq, f, indent=2)
    print(f"Updated {seq_path}")

    # Also write a richer N=12 detail file
    detail_path = os.path.join(DATA, "n12_aggregate.json")
    detail = {
        "N": N, "m_reg": M_REG, "m_f": M_F, "pi_s": float(pi_s),
        "lambdas": LAMBDAS,
        "per_lambda": per_lambda_data,
        "intercept_PiT_PiS2": float(intercept),
        "slope_PiT_PiS2": float(slope),
        "stdQCD_intercept_LO": intercept_LO,
        "stdQCD_slope_LO": slope_LO,
        "capture_lambda1": float(capture),
        "Pi_T_textbook_LO": float(Pi_T_exp),
    }
    with open(detail_path, "w") as f:
        json.dump(detail, f, indent=2)
    print(f"Wrote detail: {detail_path}")
    print()

    # Final report
    print("=" * 78)
    print("c_2(N) sequence (raw intercepts):")
    print("=" * 78)
    print(f"{'N':>4}  {'Π_s':>8}  {'c_2_raw':>13}  {'slope':>13}")
    for n in sorted(int(k) for k in seq.keys()):
        d = seq[str(n)]
        print(f"{n:>4}  {d['pi_s']:>8.4f}  {d['intercept']:>+13.5e}  "
              f"{d['slope']:>+13.5e}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        status(load_state()); return
    if len(sys.argv) > 1 and sys.argv[1] == "aggregate":
        aggregate(); return
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BUDGET_SEC
    drive(budget)


if __name__ == "__main__":
    main()

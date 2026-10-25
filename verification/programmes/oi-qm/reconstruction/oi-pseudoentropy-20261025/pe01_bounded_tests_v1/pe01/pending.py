"""Points where PLAN.md, as written, does not determine the computation or cannot be implemented as
stated. None of them is decided in code: each is listed here, the computation it governs is either
not run (smoke mode records it as pending) or, where the code carries the most literal reading,
that reading is named. A run in result mode refuses to start while any item is open; an amendment
in ../amendments/ must settle it first (PLAN.md §11).
"""

PENDING = {
    "B3W-K0": (
        "B3 window class, K0 (worst and average): §3 asks for max over (window, test) of min_phi, "
        "exact, over all tests on windows of w <= 16 positions. A window of w positions carries "
        "2^(2^w) tests, so exact enumeration is impossible for w >= 5, and the worst case over "
        "them is a max-min integer program with no exact method stated. Not computed."
    ),
    "LF-A": (
        "Linear-filter observers: §3 defines them by rho_x(v) = A v XOR x b and does not state the "
        "setting map a. The code reads them as passive (a = 0), the only reading under which the "
        "subclass is enumerable; the reading is recorded with every linear-filter result."
    ),
}


def open_items():
    return sorted(PENDING)

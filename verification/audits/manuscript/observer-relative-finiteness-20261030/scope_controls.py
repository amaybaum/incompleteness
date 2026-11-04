#!/usr/bin/env python3
"""Research-only control checks for observer-relative finiteness scope audit.

Usage: python3 scope_controls.py [--sources PATH_TO_REPO]
This does not prove infinite-carrier physics, energy conservation from OI,
or adoption of a manuscript correction.
"""
from pathlib import Path
import argparse

OLD = {
    "papers/Main.md": [
        "What distinguishes the present setting is not the existence of such a map but that it acts on a *finite* $S$ (Lemma 1);",
        "only finite visible resolution is a theorem (Lemma 1)",
    ],
    "papers/GR.md": ["Lemma 1 requires $S$ finite for the recurrence proof ([Main, §2.3])"],
    "book/ch01-observation.md": [
        "it acts on a *finite* system; finiteness, not the dynamics, is the load-bearing commitment.",
        "On each accessible orbit the invariant measure is unique and uniform",
    ],
    "book/glossary.md": ["**Axiom 2 (Finiteness).**"],
    "book/ch05-gauge-structure.md": [
        "Part I established that any observer embedded in a finite deterministic universe",
        "The framework's content rests on a minimal mathematical structure: a finite set $S$",
    ],
}


def exact_source_matches(root: Path):
    checked = 0
    for relative, needles in OLD.items():
        data = (root / relative).read_text(encoding="utf-8")
        for needle in needles:
            n = data.count(needle)
            assert n == 1, (relative, needle, n)
            checked += 1
    assert checked == 8, checked
    print(f"PASS SOURCE-OLD-CLAUSES {checked} unique matches; no source edit")


def energy_countercontrols():
    # T(x,p)=(p,-x); the identity H(T(x,p))=p^2+(-x)^2=H(x,p)
    # is algebraic for all real x,p. These integer probes are only regression.
    seen = set()
    for x in range(-13, 14):
        for p in range(-13, 14):
            nx, np = p, -x
            h = x*x + p*p
            assert nx*nx + np*np == h
            seen.add(h)
    assert len(seen) > 1
    print("PASS INFINITE-CARRIER conserved nonconstant H=x^2+p^2; 729 integer samples")

    # A full cyclic finite permutation has one orbit. All invariant functions
    # are constant, because invariance propagates around the entire cycle.
    for q in range(2, 24):
        orbit = []
        x = 0
        for _ in range(q):
            orbit.append(x)
            x = (x + 1) % q
        assert x == 0 and len(set(orbit)) == q
        values = [i*i for i in range(q)]
        assert any(values[(i+1) % q] != values[i] for i in range(q))
    print("PASS FINITE-CYCLE 22 orbit controls: invariance forces H constant")

    # Map from infinite microscopic space to finite visible alphabet.
    # This demonstrates cardinality non-implication only, no measured law.
    assert {x & 1 for x in range(-200, 201)} == {0, 1}
    print("PASS FINITE-OBSERVER binary readout compatible with infinite Z^2 carrier")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", type=Path, help="run read-only historical source checks")
    args = ap.parse_args()
    energy_countercontrols()
    if args.sources is not None:
        exact_source_matches(args.sources)
    print("VERDICT SCOPE-CONTROLS-RESEARCH-ONLY")


if __name__ == "__main__":
    main()

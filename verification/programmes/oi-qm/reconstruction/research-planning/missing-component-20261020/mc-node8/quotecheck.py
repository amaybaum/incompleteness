"""Drafting check for mc8/PREREG.md: each quoted fragment occurs, whitespace-normalized and
case-sensitive, within the stated line range of the stated file at the given commit.
Usage: python3 -I -B quotecheck.py <repo-worktree> <commit>"""
import subprocess, sys, re

Q = [
    ("papers/Main.md", 44, 44, ["an observer $V \\subsetneq S$ — a proper subsystem with finitely many distinguishable internal states, coupled to the complement $H = S \\setminus V$ through $\\varphi$"]),
    ("papers/Main.md", 48, 48, ["The observer has finitely many distinguishable internal states, so the visible configuration space $\\mathcal{C}_V$ is finite, with a discreteness scale $\\epsilon$ providing a finite minimal cell volume."]),
    ("papers/Main.md", 50, 50, ["The observer is a proper subsystem: $V \\subsetneq S$. The complement $H = S \\setminus V$ is the hidden sector."]),
    ("papers/Main.md", 56, 56, ["a bijection: distinct states have distinct successors and predecessors", "globally, the counting measure is selected among invariant measures as the maximal-entropy one"]),
    ("papers/Main.md", 60, 60, ["a realization in the sense of §3.4 carries its own fixed hidden prior $\\mu_H$ as part of the realization datum", "the counting measure is the default, not a constraint on representations"]),
    ("papers/Main.md", 62, 62, ["Of the structure above, only finite visible resolution is a theorem (Lemma 1).", "injectivity is the requirement that the dynamics preserve the observer's records"]),
    ("papers/Main.md", 78, 78, ["The hidden sector has enough distinguishable states to encode the observed conditional past–future information"]),
    ("papers/Main.md", 80, 80, ["two visible histories with the same current state induce different next-step laws, mediated through the hidden state"]),
    ("papers/Main.md", 82, 82, ["the Bell-violating branch adopted in §3.3 retains measurement independence and relinquishes ontic parameter independence while preserving operational no-signaling"]),
    ("papers/Main.md", 115, 117, ["let $\\varphi: \\mathcal{C}_V \\times \\mathcal{C}_H \\to \\mathcal{C}_V \\times \\mathcal{C}_H$ be a bijection", "\\pi_V(\\varphi(x_i, h)) = x_j"]),
    ("papers/Main.md", 356, 356, ["the same reversible response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box behavior", "The selector in a Bell experiment is therefore causal locality, not representability."]),
    ("papers/Main.md", 358, 358, ["Thus a setting intervention supported in region $A$ cannot alter a readout in region $B$ before the corresponding causal cones meet."]),
    ("papers/Main.md", 361, 365, ["(i) the dynamics is deterministic; (ii) the setting operations are", "(iv) the interventions act on one common", "pre-setting ensemble, so $p(\\Omega\\mid a,b)=p(\\Omega)$"]),
    ("papers/Main.md", 392, 392, ["at the microstate level, one wing's response depends on the remote setting. This is not an operational signal", "a Bell preparation supplies bounded-degree long edges or an equivalent nonlocal response map"]),
    ("papers/Main.md", 405, 405, ["If $\\Lambda$ is coarser than the response-relevant microstate, $I(\\Lambda;Z)$ alone does not control CHSH"]),
    ("papers/Main.md", 407, 407, ["a later local setting cannot produce an operational signal at the remote wing", "Dropping that spatial/intervention structure returns the unrestricted OI behavior class, including PR, which is the mandatory negative control."]),
    ("papers/Main.md", 486, 488, ["I(X_{<t} ; X_{>t} \\mid X_t) \\leq \\log_2 m", "Conditioning on $X_t$: $X_{<t} \\to H_t \\to X_{>t}$ is a Markov chain. By data processing:"]),
    ("papers/Main.md", 522, 522, ["arises from marginalizing a deterministic bijection on $\\mathcal{C}_V \\times \\mathcal{C}_H$"]),
    ("papers/Main.md", 550, 550, ["Each labelled instrument is one fixed map, applied whenever chosen, in every context; context enters only through the state."]),
    ("papers/Main.md", 578, 578, ["the response-table construction realizes arbitrary finite stochastic behavior, quantum or not"]),
    ("papers/Main.md", 630, 630, ["It does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category."]),
    ("papers/Main.md", 708, 708, ["(viii) site factorization — the configuration space is identified with a product of local configuration spaces over a set of sites"]),
    ("papers/SM.md", 156, 156, ["is a sufficient sparsity condition for *typical local neighborhoods* to retain the reference graph geometry.", "This is not a theorem that $\\kappa_{OR}$ converges everywhere"]),
    ("papers/Substratum.md", 44, 44, ["φ is a bijection: *perfect memory* — information is never created or destroyed.", "The partition $V$ defines the observer's *access* — both read and write."]),
    ("papers/Substratum.md", 92, 92, ["E3, with the holographic bound read as a Hilbert-space dimension cutoff"]),
    ("papers/Computation.md", 130, 130, ["realizable correlations are those approximable by finite-dimensional strategies"]),
    ("papers/Methodology.md", 393, 393, ["one wing's response can depend on the remote setting at the microstate level even though the averaged outcome distribution is operationally no-signaling"]),
    ("verification/lean-mathlib/OIBridge/FiniteEntropy.lean", 383, 385, ["theorem cmi_le_of_deterministic", "cmi w a b (fun s => g (b s, c s)) ≤ cmi w a b c"]),
    ("verification/lean-mathlib/OIBridge/FiniteEntropy.lean", 457, 459, ["theorem cmi_le_log_card", "cmi w a b c ≤ Real.log (Fintype.card γ)"]),
    ("verification/lean-mathlib/OIBridge/C3Necessity.lean", 80, 80, ["theorem c3_necessity"]),
    # revision 2 (owner redirect, 2026-10-21): C1-C4 start, branch 1 and branch 2 sources
    ("papers/Main.md", 20, 20, ["it is also universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process", "The discriminating content is history readback."]),
    ("papers/Main.md", 72, 72, ["(C1) and (C3) follow from (C4) in any faithful realization, and (C2) is a physical-regime premise"]),
    ("papers/Main.md", 74, 74, ["hidden degrees of freedom affect the visible evolution at some accessible step — the conditional law of some visible transition depends on the hidden state"]),
    ("papers/Main.md", 76, 76, ["a hidden record of visible history, once written, persists to the readback that uses it"]),
    ("papers/Main.md", 82, 82, ["C4 is not needed for the existence of a quantum representation; it is what makes the OI sector nontrivial."]),
    ("papers/Main.md", 604, 604, ["Of the three structural conditions, only (C4) is logically independent."]),
    ("papers/Main.md", 664, 664, ["the operational theory's unique selection remaining open (§3.4)"]),
    ("papers/Main.md", 666, 666, ["The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events.", "A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms.", "The Born rule, often treated as an independent postulate, is here part of the exact fixed-basis representation dictionary"]),
    ("papers/Main.md", 668, 668, ["each partition satisfying the characterization conditions produces its own C1–C4-quantum description of the remaining degrees of freedom"]),
    ("papers/Main.md", 674, 674, ["exists and is unique given $\\varphi$. Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively."]),
    ("papers/Explainer.md", 566, 566, ["The mystery dissolves not into another postulate but into a derivation: this is what marginal statistics look like when paths through the partition are indistinguishable."]),
    ("book/ch01-observation.md", 280, 282, ["a player who prices hands divisibly loses money at a rate equal to the interference term", "Interference is not a substance; it is the failure of divisibility"]),
    ("book/appendix-c-objections.md", 228, 228, ["which an ordinary classical stochastic process also reprodu"]),
    ("papers/Structure.md", 1312, 1312, ["bounded the magnitude of three-path interference to less than $10^{-2}$ of the expected two-path interference"]),
    ("papers/SM.md", 296, 296, ["The *exact* dynamics is the linear rule $f = \\sum_{\\text{nn}} x - x(t-1)$ over $\\mathbb{Z}/q\\mathbb{Z}$"]),
    ("papers/Main.md", 716, 716, ["the realization's permutation unitary, $\\hat{H} = i\\log U$, exact at integer horizon times for uniform, slice, and weighted priors"]),
    ("papers/Main.md", 534, 534, ["exact coherent/composite compatibility is the residual operational-lifting problem"]),
    # revision 3 (owner's sharpened direction, 2026-10-21)
    ("papers/Main.md", 80, 80, ["The condition is operational; it does not by itself assert a causal write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it (the response-table construction, §3.4)."]),
    ("papers/Main.md", 560, 560, ["The per-instrument family assembles into one map: on the enlarged hidden sector carrying a read-only program register — the protocol table — alongside the visible record, the seeds, and the branch register"]),
    ("papers/Main.md", 600, 600, ["**Theorem (canonical predictive quotient — a purification ingredient, substratum form).**"]),
    ("papers/Main.md", 602, 602, ["purification demands existence and essential uniqueness — up to reversible transformations of the purifying system — within the operational theory"]),
    ("papers/Main.md", 666, 666, ["In the double-slit experiment, the particle traverses a single slit in the deterministic substratum."]),
    ("verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/PLAN.md", 121, 122, ["Purification with uniqueness would cover all three, but only as a posit."]),
    ("verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node3/NODE.md", 232, 233, ["Purification is the closest to what OI states. None of the three is derivable under κ1–κ4."]),
    ("verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node5/NODE.md", 263, 263, ["The purification uniqueness that would give O-B is not supplied (Main.md:602; MC2 §3)."]),
    ("verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node5/NODE.md", 344, 346, ["Each posits continuous reversibility or purification with uniqueness."]),
]

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def main():
    repo, commit = sys.argv[1], sys.argv[2]
    bad = 0
    for path, lo, hi, frags in Q:
        text = subprocess.run(["git", "-C", repo, "show", f"{commit}:{path}"],
                              capture_output=True, text=True, check=True).stdout.split("\n")
        window = norm(" ".join(text[lo - 1:hi]))
        for f in frags:
            ok = norm(f) in window
            bad += not ok
            print(("PASS" if ok else "FAIL"), f"{path}:{lo}-{hi}", norm(f)[:70])
    print(f"{len(sum((q[3] for q in Q), []))} fragments, {bad} failing")
    sys.exit(1 if bad else 0)

main()

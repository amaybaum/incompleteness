#!/usr/bin/env python3
"""Generate matrix/part-B2.json (claims I-092..I-171 and sub-claims) for the intro corpus audit."""
import json, sys

AUD = sys.argv[1]  # audit directory
C = "eae01647"

claims = json.load(open(AUD + "/inventory/claims.json"))
byid = {e["id"]: e for e in claims}


def M(line):
    return f"papers/Main.md:{line}@{C}"


def G(line):
    return f"papers/GR.md:{line}@{C}"


def Lk(mod, line, name):
    return f"lean:{mod}.lean:{line}:{name}"


def link(what, source, layer, hyps, status):
    return {"link": what, "source": source, "layer": layer, "hypotheses": hyps, "link_status": status}


# ---------- reusable links ----------
FR = "faithful realization: bijection of C_V x C_H with an initial law (possibly correlating x and h) reproducing the law (Main:97 §1.5)"
JL = "kernel object: bijection `step` plus an arbitrary joint law w on (X_<t, X_t, H_t) (HiddenMemory.Realization)"
HM_a = link("(a) nextLaw = marg(post, nextVis): next-step law is the pushforward of the hidden posterior, for a joint law on (X_<t,X_t,H_t) with X_{t+1} defined as the visible part of the bijection",
            Lk("HiddenMemory", 83, "pushforward_identity"), "kernel", [JL], "proved")
HM_b = link("(b) tv(nextLaw p x, nextLaw p' x) <= tv(post p x, post p' x)",
            Lk("HiddenMemory", 114, "distinguishability_floor"), "kernel", [JL], "proved")
HM_c = link("(c) memory <= cmiBits(X_<t;H_t|X_t) <= logb 2 |H| (data processing through the deterministic readout; cmi w a b c = I(a;c|b), FiniteEntropy:352)",
            Lk("HiddenMemory", 170, "capacity_floor"), "kernel", [JL, "Nonempty H"], "proved")
HM_all = link("(a)-(c) bundled", Lk("HiddenMemory", 185, "unavoidable_hidden_predictive_memory"), "kernel", [JL, "Nonempty H"], "proved")
TIMET = link("Reading a faithful realization's time-t law as the kernel's joint law of history, present and hidden state: written argument (determinism makes X_{t+1} a function of (X_t,H_t)); Main states it is 'not formalized'",
             M(582), "paper-derivation", [FR], "proved")
MAINPROOF2 = link("Written proof of Theorem (unavoidable hidden predictive memory) (a)-(c); certified over all 1,464 realizations at (2,2),(2,3),(3,2) in memory_probes.py",
                  M(590), "paper-derivation", [FR], "proved")
VANISH = link("Vanishing criterion: I(A;B|C)=0 iff A and B are conditionally independent given C, so M_t>0 iff two positive-probability histories ending at the same x_t have different next-step laws (Main:97 'by the standard vanishing criterion ... which is not formalized')",
              "[CT06] (standard; not read in the audits per the reference comment)", "literature", [], "proved")
SIMPD = link("Every finite stochastic law has a finite reversible realization (initial law may correlate x and h)",
             Lk("Equivalence", 422, "S_imp_D"), "kernel", ["finite C_V", "finite horizon K"], "proved")
TVMUL = link("A row-stochastic Lambda contracts total variation: tv(p Lambda, q Lambda) <= tv(p,q)",
             Lk("CausalReadback", 96, "tv_mul_le"), "kernel", ["Lambda row-stochastic"], "proved")
PDIV_DEF = link("Rooted P-divisibility within K: for all s<t<=K some row-stochastic Lambda with Gamma t = Gamma s * Lambda (PDivisible, CausalReadback:52); PIndivisibleWithin = negation",
                "lean:CausalReadback.lean:52:PDivisible", "kernel", [], "proved")
THM3K = link("Rooted realization (bijection + one hidden prior shared by every root): identity return rootedMap n = 1 and an overlap of two distinct roots' rows at s<n give PIndivisibleWithin n",
             Lk("RecurrenceHorizon", 148, "pIndivisible_of_rooted_identity_return_of_overlap"), "kernel",
             ["RootedRealization: step : V x H ≃ V x H, prior : H -> R shared by every root (CausalReadback:178)", "s < n", "rootedMap R n = 1", "a ≠ b, 0 < rootedMap R s a x, 0 < rootedMap R s b x"], "proved")
MAIN23 = link("Main §2.3 Theorem: uniform hidden prior (counting measure), |C_V|>=2, T not a permutation => P-indivisible, via recurrence T^(N)=I and strict contraction at step 1 (special case s=1 of Theorem 3)",
              M(115), "paper-derivation", ["uniform hidden prior", "one-step T non-permutation"], "proved")
STOCHINV = link("If A,B row-stochastic and AB=1 or BA=1 then A is a permutation matrix",
                Lk("EquivalenceChain", 110, "isPermMatrix_of_stochastic_inverse"), "kernel", ["finite square matrices"], "proved")
PERIODIC = link("Rooted maps of a finite rooted realization are periodic with Gamma_0 = I (finite order of the bijection)",
                Lk("RootedClassification", 135, "rootedMap_periodic"), "kernel", [], "proved")
GRTHM4 = link("GR states Theorem (operational-completion characterization) with 'on the system and on every positive ancilla level'; no paper proof, kernel chain cited",
              G(218), "paper-derivation", ["nonempty finite visible system", "operational theory closed under coarse-graining and outcome-conditioned composition with spectator-independent ancilla readout"], "proved")
EXACTALL = link("ExactAllFiniteEndomorphicQuantumOps T <-> PhysicalCompletionConditions T for every nonempty finite A (ExactAll = system exactness ∧ exactness at every level k+1, LevelOneSeam:186, AncillaClosure:364)",
                Lk("GeneralCarrier", 100, "exactAll_iff_physical_general"), "kernel", ["Nonempty A", "Fintype A", "FiniteOperationalTheory A (OperationalAssembly:594)"], "proved")
NEC = link("Necessity: ExactAll => five conditions; declared in section Necessity with variable {A} [Fintype A] [DecidableEq A] [Nonempty A] (PhysicalCharacterization:224), i.e. every nonempty finite carrier",
           Lk("PhysicalCharacterization", 301, "physical_of_exactAll"), "kernel", ["Nonempty A", "FiniteOperationalTheory A"], "proved")
SUF = link("Sufficiency: five conditions => ExactAll, via krausSoundExt_of_validity_inert (OperationalValidity:124), compositeCompleteness_unconditional (IsometryExtension:179, premise discharged by finiteIsometryExtensionSF_discharged :116) and exactAll_of_levelOne (LevelOneSeam:196)",
           Lk("GeneralCarrier", 93, "exactAll_of_physical_general"), "kernel", ["Nonempty A", "FiniteOperationalTheory A"], "proved")
FIVEWAY = link("For each of the five conditions there is a FiniteOperationalTheory (Fin 2) satisfying the other four and RealizesSealedOICore (CoreC1C4 plus availability of the core's channels and readout, OIRealization:234) and failing that one",
               Lk("RankGapTheory", 702, "five_way_minimality"), "kernel", ["qubit carrier Fin 2"], "proved")
OIALONE = link("∃ T on Fin 2 with RealizesSealedOICore T ∧ ¬ExactAll T (witness diagTheory, the diagonal-preserving theory)",
               Lk("GeneralCarrier", 160, "oi_alone_not_qm"), "kernel", ["qubit carrier Fin 2", "'OI' formalized as realizing the sealed C1-C4 core"], "proved")
GL2 = link("∃ visible family Gamma and coherent lifts U, U' = U*K with K time-dependent in the strong anchor stabilizer (invisible to the visible law) whose relative candidates (readback of |U_1 U_0^†|^2) differ — existential, one exhibited 2x2 instance",
           Lk("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate"), "kernel", ["fixed carrier Fin 2 x Fin 2, anchor 0"], "proved")
GL3 = link("For constant unitary K: (U t K)(U s K)^† = U t (U s)^†",
           Lk("CoherentLiftGauge", 451, "gl3_constant_gauge_preserves_relative"), "kernel", ["K unitary, constant in time"], "proved")
REMARK_REL = link("Main Remark (scope: representability, not selection of the relating evolution): distinct coherent lifts with different relating evolutions; constant deformation cancels; 'Uniqueness needs a selection condition beyond visible-law representability and ordinary coherence; this paper neither supplies one nor says what form one must take'; selection 'is open'",
                  M(624), "paper-derivation", [], "proved")
BRIDGE = link("Two trivial-ancilla admissible dilations of the same slice G (|U_ij|^2 = G_ij), composed with permClass interventions M,N on either side, give equal root-conditioned trajectory laws rootTraj K a for every K and root a",
              Lk("TrackBQfbBridge", 276, "bridge_traj"), "kernel", ["trivial ancilla", "realData: uniform initial law, identity readout", "M,N in permClass (identity allowed)"], "proved")
ROOTEDIFF = link("For trivial-ancilla admissible dilations of slices G, G': (∀ t a j, rooted families agree) ↔ G = G'; forward = slice_eq_of_rooted_eq (rooted ⇒ slice, via the t=1 rooted map being the Born matrix), backward = visible_congr",
                 Lk("TrackBQfbBridge", 180, "rooted_eq_iff_slice_eq"), "kernel", ["trivial ancilla", "uniform initial law", "identity readout"], "proved")
REALSTOCH = link("For unitary U and every K, a: rootTraj K a of realData U is QfbRealizable (qfbRealizable_rootTraj) and Stochastic (Qfb_imp_S)",
                 Lk("TrackBQfbBridge", 286, "realData_traj_stochastic"), "kernel", ["U unitary", "Nonempty V"], "proved")
FACTOR = link("Elementary factorization: a fixed realization with N ontic configurations has behaviour B = Xi M with M column-stochastic over N states and Xi in [0,1]; nonnegative rank <= N",
              M(538), "paper-derivation", ["preparation -> finite ontic system -> measurement interface"], "proved")
HKLP = link("For all d,m >= 2 there is a communication matrix C with dim_Q(C) <= d and dim_C(C) >= m (qubit d=2: classical dimension unbounded over finite tasks); read in the retained text of arXiv:2308.07727",
            "[HKLP24, Thm 4]", "literature", [], "proved")
BELL = link("Theorem (Bell ceiling for a screened local completion): response-fixing pre-setting microstate, determinism, local interventions, readout before cones meet, common pre-setting ensemble p(Ω|a,b)=p(Ω) => deterministic local response functions, |S_CHSH|<=2; certified in equivalence_recovery_probes.py check 11 (no ledger row)",
            M(360), "paper-derivation", ["determinism", "interventions supported in the wings", "readout before post-setting cones meet", "measurement independence"], "proved")
BELL_LIT = link("Bell-local models obey |S_CHSH| <= 2", "[Bel64; CHSH69]", "literature", [], "proved")


def row(cid, chain, req, pstatus, strongest, verdict, contra=None, fix=None, notes="", cond=None, sub=None):
    if sub is None:
        e = byid[cid]
        r = {"id": cid, "section": e["section"], "line": e["line"], "text": e["text"],
             "status_as_stated": e["status_as_stated"]}
    else:
        parent = byid[cid]
        sc = [s for s in parent["direction"]["sub_claims"] if s["id"] == sub][0]
        r = {"id": sub, "section": parent["section"], "line": parent["line"], "text": parent["text"],
             "sub_claim": {"label": sc["label"], "claim": sc["claim"]},
             "status_as_stated": {"level": sc["status_as_stated"], "cited": sc.get("cited", []),
                                  "note": sc.get("note", "")}}
    r["chain"] = chain
    r["required_assumptions"] = req
    r["proof_status"] = pstatus
    if cond:
        r["conditional_on"] = cond
    r["strongest_verified_source"] = strongest
    r["verdict"] = verdict
    r["contradictions"] = contra or []
    r["proposed_fix"] = fix
    r["notes"] = notes
    return r


NO939 = "No #939 change touches this site (git diff b64919cd eae01647 changes only ħ wording in Main/GR/ch00/ch01)."
R = []

# ---------------- §2.4 ----------------
R.append(row("I-092",
    [link("M_t := I(X_<t; X_{t+1} | X_t); Main §1.5 uses the same definition", M(97), "paper-derivation", [], "proved"),
     link("Kernel `memory R := cmiBits R.w varHist varNow (varNext R)` = I(X_<t; X_{t+1} | X_t) in bits", "lean:HiddenMemory.lean:138:memory", "kernel", [JL], "proved")],
    [], "proved-kernel", Lk("HiddenMemory", 138, "memory"), "FAITHFUL",
    notes="Definition matches Main §1.5 and the kernel. " + NO939))

for cid, lk, part in [("I-093", HM_a, "(a)"), ("I-094", HM_b, "(b)"), ("I-095", HM_c, "(c) first inequality"), ("I-096", HM_c, "(c) second inequality")]:
    R.append(row(cid, [lk, TIMET, MAINPROOF2],
        [FR, "finite C_V, C_H", "histories p, p' ending at x (posterior defined for positive-probability histories)"] + (["Nonempty C_H"] if cid in ("I-095", "I-096") else []),
        "proved-paper", Lk("HiddenMemory", 185, "unavoidable_hidden_predictive_memory") + " + " + M(582), "FAITHFUL",
        notes=f"Theorem 2{part}. The kernel proves the clause for any joint law on (X_<t,X_t,H_t) with X_{{t+1}} defined from the bijection; identifying that law with a realization's time-t law is a written step (Main:582 kernel note: 'not formalized'). Weakest link is therefore paper-level, matching the Introduction's line 80. The kernel's division by histProb makes (a) hold vacuously at zero-probability histories; Main §1.5 restricts to positive-probability histories. Cited [Main §3.4] is correct (Main:582). Ledger MAIN:T-unavoidable-hidden-predictive-memory K3. " + NO939))

R.append(row("I-097", [HM_a, HM_b, HM_c, HM_all], [JL, "Nonempty C_H for (c)"], "proved-kernel",
    Lk("HiddenMemory", 185, "unavoidable_hidden_predictive_memory"), "FAITHFUL",
    notes="Declarations exist at HiddenMemory:83, :114, :170, :185 (Appendix A lines correct at eae01647, sources identical to 17b830bc). Statement types match (a)-(c) for a joint law; `#print axioms` lines present in the module."))
R.append(row("I-098", [TIMET], [FR], "proved-paper", M(582), "FAITHFUL",
    notes="Main:582 and Main:580 (Summary (2)) both state that reading a realization's time-t law as the joint law is not formalized; no kernel declaration covers it (searched HiddenMemory, C3Necessity, Equivalence)."))
R.append(row("I-099", [MAINPROOF2], [FR], "proved-paper", M(582), "FAITHFUL",
    notes="Theorem at Main:582, proof at Main:590 (PROOFS-README: inline-proof). [CT06] is cited 'see also' for data processing; its content was not read in the audits (reference comment)."))

# Corollary
COR_M = link("Main §1.5: 'a finite-horizon law has a memory witness at t ... equivalently M_t>0 ... exactly when every faithful realization carries readout-relevant hidden memory at t ... the forward direction is the pushforward identity applied in each realization, the converse the same identity applied in one realization, which exists (kernel: S_imp_D)'; restated at Main:580 Summary (2) and Main:592 Remark",
             M(97), "paper-derivation", [FR], "proved")
R.append(row("I-100", [COR_M, VANISH, HM_a, TIMET, SIMPD],
    [FR, "positive-probability histories", "finite horizon K >= t+1"], "proved-paper", M(97), "FAITHFUL",
    notes="Attention resolved: Main §1.5 (Main:97, 'The four layers') does carry the Corollary, so [Main §1.5] is the right locator; it is also restated in Main §3.4 (Summary (2), Main:580; Remark (what this strengthens), Main:592). Both directions traced separately (I-100.a, I-100.b). Each rests on kernel (a) plus two unformalized steps (vanishing criterion, time-t identification), exactly as the Introduction says. " + NO939))
R.append(row("I-100", [VANISH, HM_a, TIMET], [FR, "positive-probability histories"], "proved-paper", M(97), "FAITHFUL",
    notes="Forward: M_t>0 gives two positive-probability histories with different next-step laws (vanishing criterion); in any faithful realization (a) turns them into posteriors with different f_x-pushforwards. Valid for every realization.", sub="I-100.a"))
R.append(row("I-100", [SIMPD, HM_a, TIMET, VANISH], [FR, "positive-probability histories"], "proved-paper", M(97), "FAITHFUL",
    notes="Converse: the hypothesis is universal over faithful realizations; S_imp_D supplies one, in which (a) turns differing pushforwards into differing next-step laws, hence M_t>0. The converse is not vacuous because a realization exists. Pressure-tested: S_imp_D's realization allows a correlated initial law, which the Introduction's definition of faithful realization (line 30) permits.", sub="I-100.b"))
R.append(row("I-101", [VANISH, TIMET], [], "proved-paper", M(97), "FAITHFUL",
    notes="Main:97 and Main:580 both say the vanishing criterion is not formalized; no kernel CMI-vanishing lemma found in FiniteEntropy.lean (cmi_nonneg, cmi_le_of_deterministic, cmi_le_log_card only)."))

R.append(row("I-102",
    [link("Corollary (per-process capacity bound): any deterministic-bijection realization of a process with I* = sup_t I(X_<t; X_>t | X_t) requires m >= 2^{I*}", M(492), "paper-derivation", ["deterministic bijection realization"], "proved"),
     link("Theorem (C3 necessity): I(X_<t;X_>t|X_t) <= log2 m by data processing", M(484), "paper-derivation", [], "proved"),
     link("cmiBits(X_<t; future_L | X_t) <= logb 2 |H| for the same Realization (joint-law) object as Theorem 2", Lk("C3Necessity", 80, "c3_necessity"), "kernel", [JL, "Nonempty H"], "proved"),
     link("2^{I*} <= |H| with I* the max over a finite nonempty family of slices sharing H", Lk("C3Necessity", 117, "card_hidden_ge_two_pow_Istar"), "kernel", [JL, "Nonempty H", "finite nonempty family of slices"], "proved"),
     TIMET],
    [FR, "finite hidden alphabet"], "proved-paper", Lk("C3Necessity", 117, "card_hidden_ge_two_pow_Istar") + " + " + M(492), "IMPRECISE",
    fix="A realization of a law whose conditional past–future information $I^*=\\max_t I(X_{<t};X_{>t}\\mid X_t)$ is positive needs $|\\mathcal C_H|\\ge2^{I^*}$ (machine-checked for a joint law of history, present and hidden state, as for Theorem 2) [Main §3.4, Corollary (per-process capacity bound)].",
    notes="Attention resolved: the quantity is Main's I* = sup_t I(X_<t; X_>t | X_t) (Main:492), past-to-whole-future, not M_t; the kernel's `varFuture R L` is the L-step future and `Istar` a max over a finite family of slices sharing H. 'Machine-checked in the same form as Theorem 2' is accurate: the same HiddenMemory.Realization joint-law object, so the time-t identification is again a written step. The Introduction neither defines I* nor cites a manuscript location for this sentence (only Appendix A). Content correct; the defect is the undefined quantity and missing locator. Ledger MAIN:T-c3-necessity K3; MAIN:C-per-process-capacity-bound P."))

R.append(row("I-103",
    [link("Lemma (accessible backflow from readback): two histories with common present, each Pr >= p0, next-step laws at TV >= delta => I(X_<k;X_{k+1}|X_k) >= p0 delta^2/ln2; written proof via mixture divergence, Pinsker, triangle inequality", M(167), "paper-derivation", ["histories of length k with common present c", "Pr[X_<k=p, X_k=c] >= p0"], "proved"),
     link("Pinsker's inequality D >= (2/ln2) TV^2 in bits", "[CT06]", "literature", [], "proved"),
     link("Probe c4_backflow_probes.py: probabilities in Fractions but the CMI is accumulated in floating point (float(p)*log2(...)) and compared with tolerance 1e-12, on chosen gap/revival/parametric families — not an exhaustive exact-rational enumeration", "papers/oi_lattice_code/foundations/c4_backflow_probes.py:17@" + C, "numerical", [], "proved")],
    ["two positive-probability histories with a common present"], "proved-paper", M(170), "IMPRECISE",
    contra=[{"site": M(170), "text": "Certified exactly on gap families, the revival family, and a small-gap parametric family, with the coin silent, in `c4_backflow_probes.py`.", "nature": "Main also calls the probe 'exact', although its information values are floating-point; same imprecision at the source."}],
    fix="... then $I(X_{<k};X_{k+1}\\mid X_k)\\ge p_0\\delta^2/\\ln2$ (in bits), by Pinsker's inequality (proved on paper) [Main §2.3; CT06].",
    notes="The bound and its proof are correct (re-derived: P(c)w_a >= p0 and TV(P,P̄)^2+TV(P',P̄)^2 >= δ^2/2). The status tag '(with exact probes)' does not meet the Introduction's own definition (line 30: exhaustive computation in exact rational arithmetic at small size): the probe evaluates logarithms in floating point on hand-picked families. Relevant to attention item I-054. Ledger MAIN:L-accessible-backflow-from-readback P. " + NO939))

R.append(row("I-104",
    [link("Main §1.3 names (C1) Non-zero coupling (hidden influence on some visible transition), (C2) Memory persistence, (C3) Sufficient memory capacity, (C4) History readback: 'at some order, two visible histories with the same current state induce different next-step laws, mediated through the hidden state'", M(74), "paper-derivation", [], "proved")],
    [], "proved-paper", M(80), "FAITHFUL",
    notes="Labels and content match Main:74-80. Main's (C4) also says 'mediated through the hidden state' and 'at some order'; neither Main nor the Introduction says 'positive-probability' in the definition (Main §1.5 does when defining the memory witness)."))

C4EQ = link("Remark (the conditions are diagnostics, not hypotheses): in a faithful realization every correlation is mediated through the hidden state, so (C4) coincides with clause (ii) (CMI > 0 at some order); exhaustive enumeration agrees on 24/720/720 realizations", M(596), "paper-derivation", [FR], "proved")
WIT = link("Main §1.5: memory witness at t = two positive-probability histories ending at the same x_t with different next-step laws, equivalently M_t>0 by the vanishing criterion", M(97), "paper-derivation", [], "proved")
R.append(row("I-105", [C4EQ, WIT, VANISH], [FR, "positive-probability histories", "(C4) read at the same time t"], "proved-paper", M(596), "IMPRECISE",
    fix="In a faithful realization, (C4) at $t$ — two positive-probability histories with the same present $x_t$ inducing different next-step laws — coincides with $M_t>0$ by the vanishing criterion [CT06; Main §3.4, Remark (the conditions are diagnostics, not hypotheses)], and the Corollary places it in the hidden state;",
    notes="Attention resolved: Main §1.3 defines (C4) 'at some order' with a mediation clause; the clause 'in a faithful realization' matters only for that mediation clause, which the Introduction's own (C4) (line 86) omits, so in the Introduction's wording it is idle. The coincidence is with M_t>0 at the matching time t, and the histories must have positive probability (otherwise next-step laws are undefined). Two small slips of index and support; content correct.",))
R.append(row("I-105", [VANISH, WIT], ["positive-probability histories"], "proved-paper", M(97), "IMPRECISE",
    fix="As for I-105: state (C4) at $t$ with two positive-probability histories.", notes="(C4) ⇒ M_t>0 needs the two histories to have positive probability; the Introduction's (C4) does not say so.", sub="I-105.a"))
R.append(row("I-105", [VANISH, WIT], [], "proved-paper", M(97), "FAITHFUL",
    notes="M_t>0 ⇒ some pair of positive-probability histories with the same x_t and different next-step laws, by the vanishing criterion.", sub="I-105.b"))

R.append(row("I-106", [COR_M, C4EQ, HM_a], [FR], "proved-paper", M(97), "FAITHFUL",
    notes="Follows from I-105 and the Corollary (I-100.a)."))
R.append(row("I-107",
    [link("(C1) dependency: a readback gap requires hidden mediation, so any realization satisfying C4 satisfies C1; zero-coupling realizations show no gap (exhaustive enumeration at (2,2),(2,3),(3,2), primitive_probes.py)", M(74), "paper-derivation", [FR], "proved"),
     link("Remark (what this strengthens): (C1) follows 'because a hidden distinction invisible to f_x produces identical pushforwards'", M(592), "paper-derivation", [FR], "proved"),
     HM_a],
    [FR], "proved-paper", M(74), "FAITHFUL",
    notes="Main:72 states '(C1) and (C3) follow from (C4) in any faithful realization'. Written argument plus exhaustive small-size enumeration; no kernel declaration for the implication."))
R.append(row("I-108",
    [link("(C3) dependency: like C1, C3 follows from C4 within any faithful realization by data processing", M(78), "paper-derivation", [FR], "proved"),
     link("C3 bound holds in every faithful realization (joint-law form)", Lk("C3Necessity", 117, "card_hidden_ge_two_pow_Istar"), "kernel", [JL], "proved"), TIMET],
    [FR], "proved-paper", Lk("C3Necessity", 117, "card_hidden_ge_two_pow_Istar") + " + " + M(78), "FAITHFUL",
    notes="Pressure-tested: (C3) in the form log2|C_H| >= I* holds in every faithful realization whether or not (C4) holds, so 'follows from it' is true a fortiori; the kernel covers it in the joint-law form."))
R.append(row("I-109",
    [link("(C2) status: 'a physical-regime premise, not a structural condition'; the characterization's equivalence runs over C1, C3, C4 and the existential realization satisfies C2 with a static bath", M(76), "paper-derivation", [], "proved"),
     link("Theorem (C2 necessity, quantitative mixing form) and Theorem (physical memory: C2, process form): conditional on the hidden-sector mixing hypothesis, observed conditional memory forces a lower bound on the mixing residual (written proofs; c2_mixing_probes.py)", M(433), "paper-derivation", ["conditional-mixing hypothesis (ETH-motivated)"], "conditional"),
     link("Remark (Status of ETH): C2 necessity is conditional on the quantitative mixing hypothesis; ETH is a well-supported conjecture", M(480), "paper-derivation", [], "conditional")],
    [], "conditional", M(76), "FAITHFUL", cond=["hidden-sector conditional-mixing hypothesis (for the necessity direction only)"],
    contra=[{"site": "papers/Introduction.md:185@4a260ca9", "text": "(4) (C2) necessity, which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §3.4]", "nature": "Not a contradiction with line 86: §6.3 lists the necessity direction among 'further open problems', whereas Main proves it on paper conditional on the mixing hypothesis (Main:433, :447; ledger P). What is open is the hypothesis, not the conditional theorem; §6.3's wording understates (outside this range, I-29x)."},
            {"site": M(592), "text": "(C2-structural) as the retention required by (b)", "nature": "Main also says the structural form of (C2) follows from Theorem 2(b); the Introduction's unqualified '(C2) is a physical-regime premise' matches Main §1.3, which reserves the premise status for the physical (C2-slow/persistence) reading."}],
    notes="Attention resolved: line 86 ('physical-regime premise') and §6.3 item (4) ('necessity ... conditional on a mixing hypothesis') describe two different things — the premise's role in the equivalence, and the conditional necessity theorem — and agree with Main §1.3 and §3.4. Proof status 'conditional' refers to the necessity direction; the premise statement itself is a scope classification. ROADMAP:843 records that at the lattice cut C2 and C4 both remain hypotheses."))
R.append(row("I-110",
    [link("Remark (the conditions are diagnostics, not hypotheses); the equivalence of §3.4 quantifies over none of them", M(596), "paper-derivation", [], "proved"),
     link("Theorem 1's kernel statement has no C1-C4 hypothesis", Lk("Equivalence", 462, "finite_horizon_equivalence"), "kernel", [], "proved")],
    [], "proved-kernel", Lk("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL",
    notes="Main:72 says the same."))

# ---------------- §2.5 ----------------
BD16 = link("BD16 Prop. 1 (semiclassical case): a discrete-time dynamical mapping (N_i) from t0 to t_i is divisible iff information decreasing; Cor. 1 is the fully classical case — both are rooted at t0 with no invertibility assumption", "[BD16, Prop. 1; Cor. 1] (arXiv:1408.7062v3, read in retained text)", "literature", [], "proved")
RHP = link("RHP14 Def. 2.2 builds the intermediate maps from the rooted family T(x2,t2|x0,t0)[P(x1,t1|x0,t0)]^{-1} (Eq. 14, invertibility assumed); Thm 2.4: divisible iff the L1 norm of every vector v does not increase; the 'only if' half is stochastic contraction", "[RHP14, Thm 2.4] (arXiv:1405.0303v2, fetched and read)", "literature", ["invertible rooted maps (for the 'if' half)"], "proved")
R.append(row("I-111", [PDIV_DEF, BD16, RHP], [], "proved-kernel", "lean:CausalReadback.lean:52:PDivisible", "FAITHFUL",
    notes="Attention resolved: the Introduction's rooted definition is exactly the kernel's PDivisible. BD16's divisibility is itself rooted at t0 (dynamical mapping N_i from t0), with no invertibility assumption, so the BD16 attribution applies to the rooted form. RHP14's divisibility is rooted too (Eq. 14) but assumes the rooted maps invertible; the Introduction's 'some stochastic Λ' generalizes it to non-invertible families."))
R.append(row("I-112", [TVMUL, RHP], ["Λ row-stochastic"], "proved-kernel", Lk("CausalReadback", 96, "tv_mul_le"), "FAITHFUL",
    notes="δ_aΓ_t − δ_bΓ_t = (δ_aΓ_s − δ_bΓ_s)Λ; tv_mul_le is used by c4r_implies_pIndivisible (CausalReadback:134). Also Main:121 (proof, 'a stochastic divisor is a total-variation contraction')."))
R.append(row("I-113", [RHP, BD16], [], "proved-paper", "[RHP14, Thm 2.4]", "IMPRECISE",
    fix="This is the 'only if' direction of the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1; Cor. 1].",
    notes="The sentence names 'the divisibility criterion' (an iff) but what precedes it is only the elementary 'only if' half (stochastic Λ contracts L1/TV). RHP14's 'if' half requires contraction of every vector (not just differences of probability rows) and invertible rooted maps; the next paragraph rightly says monotone distance is not sufficient. BD16 Prop. 1 is the semiclassical case; the fully classical statement is its Cor. 1. Both sources read first-hand (RHP14 fetched to the scratchpad; BD16 from the retained text)."))

R.append(row("I-114", [THM3K, MAIN23, PDIV_DEF],
    ["bijection of C_V x C_H (not used by the kernel)", "one hidden prior shared by every root x_0", "two distinct roots' rows of Γ_s overlap in a column", "Γ_n = I for some n > s"],
    "proved-kernel", Lk("RecurrenceHorizon", 148, "pIndivisible_of_rooted_identity_return_of_overlap"), "IMPRECISE",
    contra=[{"site": "verification/lean-manuscript-census.json families[34]@" + C, "text": "recurrence horizon: an identity return with an earlier overlap forbids divisibility — status kernel-only, manuscript: []", "nature": "No manuscript carries the general statement the Introduction calls Theorem 3; Main §2.3 (Main:115) proves only the case s=1 under the uniform hidden prior (non-permutation one-step matrix)."}],
    fix="**Theorem 3** (recurrence and overlap; [Main §2.3] for a non-permutation one-step matrix under the uniform prior). *Let $\\varphi$ be a bijection of $\\mathcal C_V\\times\\mathcal C_H$ with a hidden prior independent of $x_0$. If two rows of $\\Gamma_s$ overlap in a column and $\\Gamma_n=I$ for some $n>s$, the family is not P-divisible on $\\{0,\\dots,n\\}$.*",
    notes="Attention resolved: 'fixed hidden prior' in the kernel is RootedRealization.prior, 'the fixed hidden prior, shared by every root' (CausalReadback:181) — independent of x_0 and not time-indexed. The statement matches the kernel exactly, with hypotheses and direction; the kernel does not even use reversibility (RecurrenceHorizon Section A). The citation is the problem: Main §2.3's Theorem (Main:115) is the special case s=1 with counting-measure prior, proved by the same contraction-plus-recurrence argument; the general overlap-at-s, return-at-n form, with an arbitrary shared prior, exists only in the kernel (census family 34, kernel-only). Ledger MAIN:T-unnamed-182a6975 (Main:115) level P."))
R.append(row("I-115", [THM3K], [], "proved-kernel", Lk("RecurrenceHorizon", 148, "pIndivisible_of_rooted_identity_return_of_overlap"), "FAITHFUL",
    notes="Declaration at RecurrenceHorizon:148 as Appendix A states; `#print axioms` line present."))
R.append(row("I-116",
    [link("Doukas Prop. 1 (No distinguishability revival): Markov compatibility (column-stochastic K(t,u) with CK and K(t,s)=Γ(t←s)) implies D(t) <= D(u) for s<=u<=t; applied to Rabi oscillations, where two rows coincide at t* and then separate. No recurrence, return-to-identity or row-overlap argument appears (grep of v3 text for recurren/return/overlap/permutation: none)", "[Dou26, Prop. 1] (arXiv:2602.22095v3, retained text, lines 977-1050)", "literature", [], "proved")],
    [], "proved-paper", "[Dou26, Prop. 1]", "IMPRECISE",
    fix="Doukas states the distinguishability-revival obstruction that this argument instantiates, concurrently [Dou26, Prop. 1].",
    notes="Doukas's Prop. 1 is the general revival criterion (monotone distance under a rooted stochastic divisor); Theorem 3 is an instance in which the revival is from an overlap (TV<1) to an identity return (TV=1). 'The same overlap-and-return argument' overstates the match: the overlap-and-return mechanism, and finite recurrence, are not in Doukas. Same attribution recurs at line 28 (I-04x, outside this range)."))
R.append(row("I-117", [TVMUL, link("Main §2.3 proof: monotonicity is a necessary condition for P-divisibility", M(121), "paper-derivation", [], "proved")], [], "proved-kernel", Lk("CausalReadback", 96, "tv_mul_le"), "FAITHFUL"))
R.append(row("I-118",
    [link("Main §2.3: explicit stochastic pairs whose unique divisor has a negative entry while TV is non-increasing for every p,q (one strictly contracting at n=2, one doubly stochastic at n=3)", M(121), "paper-derivation", [], "proved"),
     link("translation_probes.py (A): both witnesses checked in exact Fractions — negative divisor entry and TV-monotonicity over all pairs", "papers/oi_lattice_code/foundations/translation_probes.py:45@" + C, "exact-algebra", [], "proved")],
    [], "proved-paper", "papers/oi_lattice_code/foundations/translation_probes.py:45@" + C, "FAITHFUL",
    notes="Exact witness (n=2: T1=[[0,1],[1/2,1/2]], T2=[[4/5,1/5],[1,0]]). Consistent with RHP14 Thm 2.4, whose iff needs contraction of every vector, not only of zero-sum differences."))
R.append(row("I-119", [STOCHINV, link("Lemma (stochastic inverse), written proof", M(133), "paper-derivation", [], "proved"),
                      link("Problem 23: a stochastic n x n matrix whose inverse is stochastic is a permutation matrix", "[BB12, Problem 23] (arXiv:1209.3632v5, retained text line 6992)", "literature", [], "proved")],
    ["finite square matrices"], "proved-kernel", Lk("EquivalenceChain", 110, "isPermMatrix_of_stochastic_inverse"), "FAITHFUL",
    notes="Kernel hypothesis A*B=1 ∨ B*A=1 matches 'one-sided inverse' (for finite square matrices one-sided implies two-sided). Ledger MAIN:L-stochastic-inverse K3."))

HR = link("Theorem (history readback + finite recurrence implies indivisibility): finite order L gives Γ_L=I; if every earlier Γ_k were a permutation, two positive-probability histories with the same endpoint would fix the same x_0 and could not differ, contradicting C4; so some Γ_k is non-permutation and a divisor from k to L would be a stochastic one-sided inverse", M(137), "paper-derivation", ["fixed finite reversible representative", "history-level (C4)"], "proved")
R.append(row("I-120", [HR, STOCHINV, PERIODIC], ["fixed finite reversible substratum (one bijection, one hidden prior)", "(C4) history readback"], "proved-paper", M(137), "FAITHFUL",
    notes="Proof re-checked: sound. Scope remark (Main:141): global recurrence-cycle result, not every short window. Ledger MAIN:T-history-readback-finite-recurrence-implies P."))
ROUTED1 = link("RoutedReadback K R (round C4-1; store clause on the root-conditioned weight of the initial hidden seed) ⇒ ∃ n, PIndivisibleWithin n (rootedMap R), via horizon_verdict (the route of Theorem 3) and rootedMap_periodic", Lk("PhysicalC4Discharge", 122, "routed_forces_indivisible_somewhere"), "kernel", ["RootedRealization", "RoutedReadback K R (seed-posterior reading)"], "proved")
ROUTED2 = link("RoutedReadbackAtStorage K R (round C4-2; store clause on Law(H_s | X_s=x, X_0=a), the hidden state at the storage time) ⇒ ∃ n, PIndivisibleWithin n (rootedMap R)", Lk("PhysicalC4StorageReadback", 256, "routedAtStorage_forces_indivisible_somewhere"), "kernel", ["RootedRealization", "RoutedReadbackAtStorage K R"], "proved")
R.append(row("I-121", [ROUTED1, ROUTED2, THM3K, link("Main §1.3 (C4) realization clause: the mediation is a causal read-write cycle, 'a property to be independently demonstrated there'; GR:52 words it as a record written into hidden boundary degrees and routed back", M(80), "paper-derivation", [], "proved")],
    ["routed-readback form of (C4) on a rooted realization"], "proved-kernel", Lk("PhysicalC4StorageReadback", 256, "routedAtStorage_forces_indivisible_somewhere"), "MISCITED",
    contra=[{"site": "verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean:28@" + C, "text": "A recorded discrepancy, not repaired here. The frozen spelling of `rootedPosterior` divides the root-conditioned weight of the initial hidden seed ... while the discovery round's clause S names the law of the hidden state at the storage time", "nature": "The module cited in Appendix A flags its own predicate as diverging from the clause it transcribes; on the sealed C1–C4 core it never holds (core_not_routedReadback)."},
            {"site": "verification/lean-manuscript-census.json families[35],[36]@" + C, "text": "status kernel-only, manuscript: []", "nature": "Neither routed-readback form is carried by any manuscript; the two readings are incomparable as predicates (storageReadback_not_implies_routedReadback, routedReadback_not_implies_storageReadback)."}],
    fix="The conclusion is machine-checked, by the route of Theorem 3, from a routed-readback form of (C4), in which a visible-history record written into the hidden state is read back later (`routedAtStorage_forces_indivisible_somewhere`, and `routed_forces_indivisible_somewhere` for a seed-conditioned reading) [Main §1.3, the realization clause of (C4)]; from history-level (C4) it is proved on paper.",
    notes="Content is fine: both kernel readings force indivisibility at a return horizon (∃ n — the kernel gives n=(s+1)M; reduction to one recurrence cycle is immediate by periodicity but not stated in the kernel). The Introduction's gloss ('a visible-history record written into the hidden state is read back later') matches the storage-time reading of round C4-2, whereas Appendix A cites only round C4-1's seed-posterior reading, which its own module records as a discrepancy with that clause. Citation, not content. The Main §1.3 citation is acceptable: GR:52 attributes the read-write cycle to Main §1.3. ROADMAP:66 keeps physical C4 discharge OPEN."))
R.append(row("I-122", [HR, STOCHINV], ["history-level (C4)", "fixed finite reversible representative"], "proved-paper", M(137), "FAITHFUL",
    notes="No kernel declaration derives indivisibility from history-level (C4); PhysicalC4Discharge records that the routed form implies the history-level condition, not the converse."))
R.append(row("I-123",
    [link("Main §2.4 'Explicit Construction: A Minimal Model': C_V={0,1}, C_H={1..6}, σ^2=id, T(1,0)=[[2/3,1/3],[1/3,2/3]], T(2,0)=I, Λ(2,1) with negative entries", M(178), "paper-derivation", [], "proved")],
    [], "proved-paper", M(178), "IMPRECISE",
    fix="Appendix B works examples: a six-hidden-state model of Theorem 3 [Main §2.4], memory without short-window indivisibility, and a two-card game, the smallest realization of Theorem 3.",
    notes="Attention resolved: 'minimal' is Main §2.4's title, meaning a simple explicit model, not a smallest one; the card game (two hidden values) is smaller. Calling both 'minimal' and 'smallest' in one sentence invites a contradiction. The model does instantiate Theorem 3 (overlap at s=1, return at n=2 under the uniform prior)."))
R.append(row("I-124",
    [link("Book §1.11: 'The minimal such game is the coin-and-die model of §1.5 dealt onto a table' — asserted, no argument", "book/ch01-observation.md:273@" + C, "paper-derivation", [], "unsupported"),
     link("Elementary argument (not in the corpus): Theorem 3 needs two distinct roots (|C_V|>=2) and an overlapping pair of rows; with |C_H|=1 every Γ_s is a permutation, so |C_H|>=2. The 2x2 card game attains both minima (4 total states).", "none (audit derivation)", "none", [], "unsupported")],
    [], "unsupported", "book/ch01-observation.md:273@" + C, "UNSUPPORTED",
    fix="... and a two-card game, which with two visible and two hidden values is the smallest realization of Theorem 3 (with one hidden value every $\\Gamma_s$ is a permutation).",
    notes="Attention resolved: no proof or measure of size anywhere in the corpus (searched Main, book ch01, appendix B, Lean). The claim is true in the natural measure (|C_V|, |C_H| and |C_V||C_H| are each minimal) by a two-line argument; severity low. Fix states the measure and the reason."))

# ---------------- §3.1 ----------------
R.append(row("I-125", [link("Scope: 'a global recurrence-cycle result. It does not say that C4 forces P-indivisibility on every accessible short-time window; the XOR control remains a counterexample'", M(141), "paper-derivation", [], "proved"), ROUTED2],
    [], "proved-paper", M(141), "FAITHFUL"))
R.append(row("I-126",
    [link("XOR family: T^(k)=T^k exactly with one full bit of conditional memory (review4_probes.py); the Introduction's B.2 gives the exact case X_2 = X_0 ⊕ X_1", M(453), "exact-algebra", [], "proved"),
     link("Scope remark: XOR control is a counterexample to short-window indivisibility from C4", M(141), "paper-derivation", [], "proved")],
    [], "proved-paper", M(141), "FAITHFUL",
    notes="A single exact counterexample suffices for the negative claim; B.2's arithmetic (every two-time matrix ½J, I(X0;X2|X1)=1 bit) is exact."))
R.append(row("I-127",
    [link("Remark (three notions, kept apart): '(1) accessible finite-horizon memory ... (2) stochastic P-indivisibility ... (3) generic quantum non-Markovianity ... No unconditional implication among the three is asserted here'", M(334), "paper-derivation", [], "proved"),
     link("Counter-direction: a Markov law (all M_t = 0) is P-divisible, with Λ_{s,t}(k,j)=P(X_t=j|X_s=k), so P-indivisibility of the population law forces M_t>0 at some t (under an initial law with full support on x_0)", "[RHP14, Cor. 2.1] + elementary (audit derivation)", "literature", ["initial law with full support on x_0, product hidden prior"], "refuted")],
    [], "unsupported", M(334), "OVERCLAIM",
    contra=[{"site": M(334), "text": "No unconditional implication among the three is asserted here.", "nature": "Source makes a non-assertion; the Introduction turns it into a negative claim ('no unconditional implication holds')."}],
    fix="Three notions are distinct [Main §3.2, Remark (three notions, kept apart)]: (1) accessible memory, $M_t>0$; (2) stochastic P-indivisibility of the visible population law; (3) quantum non-Markovianity under a chosen criterion. A Markov law is P-divisible, so (2) forces (1) at some time; (1) does not force (2) on short windows (Appendix B), and outside the diagonal-preserving class (2) and (3) come apart.",
    notes="Main asserts no implication; it does not deny them. One direction holds unconditionally in the natural reading: Markov ⇒ rooted P-divisible (RHP14 Cor. 2.1: Markov transition matrices satisfy (11)-(13)), so P-indivisible ⇒ non-Markov ⇒ M_t>0 for some t. The only escape is rooted rows from roots of zero probability, which the Introduction does not invoke. (1)⇏(2) (XOR, B.2) and (2)⇏(3) (Hadamard) are supported; (3)⇏(2) is not shown anywhere but is not needed by the text. Minimal alternative fix: '... and no unconditional implication among them is asserted [Main §3.2 ...]'. Severity moderate: a false negative claim in the body."))
R.append(row("I-128",
    [link("Lemma (diagonal preservation)", M(322), "paper-derivation", ["permutation unitary U", "diagonal hidden state μ_H"], "proved"),
     link("Φ_t maps diagonal states to diagonal states", Lk("EquivalenceChain", 253, "isDiag_Phi"), "kernel", ["φ a permutation of V x H", "μ diagonal prior state"], "proved")],
    ["permutation unitary", "diagonal hidden state"], "proved-kernel", Lk("EquivalenceChain", 253, "isDiag_Phi"), "FAITHFUL",
    notes="Ledger MAIN:L-diagonal-preservation K3."))
R.append(row("I-129",
    [link("Theorem (CP-indivisibility, framework scope): for the permutation-dilation family, P-indivisibility of the populations implies no CPTP Λ with Φ_t2 = Λ∘Φ_t1 (written proof: a CPTP Λ would induce a stochastic population divisor)", M(326), "paper-derivation", ["permutation-dilation family", "diagonal-preservation lemma"], "proved"),
     link("Diagonal preservation", Lk("EquivalenceChain", 253, "isDiag_Phi"), "kernel", [], "proved")],
    ["channels from a permutation unitary with a diagonal hidden state"], "proved-paper", M(326), "FAITHFUL",
    contra=[{"site": "book/appendix-b-derivations.md:92@" + C, "text": "B.2.5 states CP-indivisibility 'of the substratum dynamics (under C1–C4)'", "nature": "Signal S3: Appendix B words the scope differently from Main's 'for the permutation-dilation family'; the Introduction follows Main."}],
    notes="Proof re-checked; it uses only positivity and trace preservation of Λ, so it holds for every diagonal-preserving family. Ledger MAIN:T-cp-indivisibility-framework-scope P."))
R.append(row("I-130",
    [link("Remark (scope: P-indivisibility is not quantum non-Markovianity): Φ_t1 = Ad_H, Φ_t2 = id is CP-divisible, populations ½J → I P-indivisible; certified exactly over Q(√2) in c1_cp_scope_probes.py", M(330), "exact-algebra", [], "proved")],
    [], "proved-paper", M(330), "FAITHFUL",
    notes="Re-checked: Λ = Ad_H is a unitary CPTP divisor; (½J)Λ has equal rows for every stochastic Λ, so ½J → I is P-indivisible."))
R.append(row("I-131",
    [link("BLP09: for all processes with the divisibility property, the trace distance is non-increasing (σ <= 0); so backflow implies non-divisibility. No converse is claimed", "[BLP09] (arXiv:0908.0238v2, fetched and read)", "literature", [], "proved"),
     link("BJA17: an ancilla is necessary for the equivalence to hold in general (system-only monotonicity does not imply CP-divisibility)", "[BJA17] (arXiv:1603.04288v2, fetched and read)", "literature", [], "proved"),
     link("Main: 'Backflow in the system alone is therefore sufficient evidence of indivisibility, never necessary'", M(332), "paper-derivation", [], "proved")],
    [], "proved-paper", "[BLP09]", "FAITHFUL",
    notes="BLP09 supplies the witness direction; that the converse fails is shown in BJA17 and Main:332, not in BLP09 itself. Acceptable as a compressed attribution."))
R.append(row("I-132",
    [link("BJA17 abstract: 'a bijective dynamical map is completely-positive-divisible if and only if a monotonic non-increase of distinguishability is observed for two equiprobable states of the evolving system and an ancilla'; ancilla dimension d+1", "[BJA17] (arXiv:1603.04288v2, fetched and read)", "literature", ["bijective dynamical maps"], "proved")],
    ["bijective (invertible) dynamical maps"], "proved-paper", "[BJA17]", "FAITHFUL",
    notes="Main:332 states the same with [9]."))
R.append(row("I-132", [link("CP-divisible ⇒ monotone distinguishability on system+ancilla", "[BJA17]", "literature", [], "proved")], ["bijective dynamical maps"], "proved-paper", "[BJA17]", "FAITHFUL", sub="I-132.a"))
R.append(row("I-132", [link("Monotone distinguishability with a (d+1)-dimensional ancilla ⇒ CP-divisible (constructive proof)", "[BJA17]", "literature", [], "proved")], ["bijective dynamical maps"], "proved-paper", "[BJA17]", "FAITHFUL", sub="I-132.b"))
R.append(row("I-133", [link("Remark (representation, not explanation)", M(616), "paper-derivation", [], "proved")], [], "proved-paper", M(616), "FAITHFUL"))
R.append(row("I-134", [link("Calvo abstract (v2): 'we prove the six axioms of textbook quantum mechanics from a single axiom: every physical system evolves according to a, generally indivisible, stochastic law'", "[Cal26] (arXiv:2601.18720v2, retained text)", "literature", [], "proved")],
    [], "proved-paper", "[Cal26]", "FAITHFUL", notes="'States a proof' correctly attributes without endorsing."))
R.append(row("I-135", [link("Theorem 1 is a correspondence of classes of finite-horizon laws whose quantum side presupposes the Born dictionary (Main:534: 'the Born dictionary p=|U|^2 ... is part of the definition of the class')", M(534), "paper-derivation", [], "proved"),
                      link("finite_horizon_equivalence: equality of classes of laws", Lk("Equivalence", 462, "finite_horizon_equivalence"), "kernel", [], "proved")],
    [], "proved-kernel", Lk("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL"))

# ---------------- §3.2 ----------------
R.append(row("I-136", [link("Remark (what this equivalence does and does not say): the theorem does not prove that all coherent preparations, noncommuting interventions and composites are represented by one standard local quantum instrument theory", M(534), "paper-derivation", [], "proved")],
    [], "proved-paper", M(534), "FAITHFUL"))
R.append(row("I-137",
    [link("FiniteOperationalTheory fields: avail_id, avail_coarse, availExt_coarse, availExt_bind (outcome-conditioned composition at every level n), prepAvail_uniform (maximally mixed ancilla), prepAvail_post, readout with readout_local (spectator-independent), prepAvail_discard", "lean:OperationalAssembly.lean:594:FiniteOperationalTheory", "kernel", [], "proved"),
     link("GR prose: 'closed under coarse-graining and outcome-conditioned composition, with a spectator-independent local readout of the ancilla'", G(216), "paper-derivation", [], "proved")],
    [], "proved-kernel", "lean:OperationalAssembly.lean:594:FiniteOperationalTheory", "FAITHFUL",
    contra=[{"site": G(216), "text": "a specification ... closed under coarse-graining and outcome-conditioned composition, with a spectator-independent local readout of the ancilla", "nature": "GR's prose omits the uniform-ancilla preparation, post-composition and discard fields that the kernel structure carries and the Introduction states; the Introduction is the more complete transcription."}],
    notes="Matches the kernel structure field by field."))
R.append(row("I-138",
    [link("Five conditions: CompositeOperationalValidity (OperationalValidity:88), SystemToLevelOne (LevelOneSeam:117), InertSpectatorCompositionality (SpectatorBridge:223), HasCompositeUnitaryControl (OperationalAssembly), IteratedAncillaClosure (AncillaClosure:247), bundled as PhysicalCompletionConditions", "lean:PhysicalCharacterization.lean:295:PhysicalCompletionConditions", "kernel", [], "proved"),
     link("GR (i)-(v) in prose", G(216), "paper-derivation", [], "proved")],
    [], "proved-kernel", "lean:PhysicalCharacterization.lean:295:PhysicalCompletionConditions", "FAITHFUL",
    notes="(i) in the kernel is positivity and trace preservation at every ancilla level n (system-level validity enters through (ii)); the Introduction's prose is an accurate summary."))
R.append(row("I-139", [GRTHM4, EXACTALL, NEC, SUF], ["nonempty finite system", "standing operational structure (FiniteOperationalTheory)"], "proved-kernel",
    Lk("GeneralCarrier", 100, "exactAll_iff_physical_general"), "FAITHFUL",
    notes="Attention resolved: ExactAll is 'system ∧ every level k+1' (positive ancilla levels), as Theorem 4 says; the standing structure specifies families at every level n including 0 (availExt n), as line 114 says. Both directions traced (I-139.a, I-139.b). Ledger GR:T-operational-completion-characterization K3. Strongest support is kernel; GR has no paper proof (kernel-only)."))
R.append(row("I-139", [NEC], ["Nonempty A"], "proved-kernel", Lk("PhysicalCharacterization", 301, "physical_of_exactAll"), "FAITHFUL", sub="I-139.a"))
R.append(row("I-139", [SUF], ["Nonempty A"], "proved-kernel", Lk("GeneralCarrier", 93, "exactAll_of_physical_general"), "FAITHFUL", sub="I-139.b",
    notes="No external premise: finiteIsometryExtensionSF_discharged (IsometryExtension:116) discharges the isometry-extension fact."))
R.append(row("I-140", [NEC], ["Nonempty A"], "proved-kernel", Lk("PhysicalCharacterization", 301, "physical_of_exactAll"), "FAITHFUL",
    notes="Attention resolved: physical_of_exactAll sits in section Necessity of PhysicalCharacterization.lean with variable {A : Type} [Fintype A] [DecidableEq A] [Nonempty A] (line 224) — carrier-general, not qubit-only. GeneralCarrier:100 uses it for every nonempty finite A. The module difference is cosmetic."))
R.append(row("I-141", [SUF], ["Nonempty A"], "proved-kernel", Lk("GeneralCarrier", 93, "exactAll_of_physical_general"), "FAITHFUL"))
R.append(row("I-142", [FIVEWAY, link("GR: 'Each of the five is independent of the other four and of the observation process itself'", G(220), "paper-derivation", [], "proved")],
    ["qubit carrier"], "proved-kernel", Lk("RankGapTheory", 702, "five_way_minimality"), "FAITHFUL",
    notes="'Independent of ... a fixed finite observation process' is meant as non-implication: no condition follows from the other four together with the C1–C4 core. The other half of logical independence (consistency of all five with the core) holds because exact QM realizes the core (qm_implies_oiCore, CompletedOI:549). Note that (iv) alone implies the core (realizesSealedOICore_of_control, OIRealization:252), so 'independent of the observation process' does not hold in both directions for (iv) taken alone; the next sentence of the Introduction states the intended reading."))
R.append(row("I-143", [FIVEWAY], ["qubit carrier"], "proved-kernel", Lk("RankGapTheory", 702, "five_way_minimality"), "FAITHFUL"))
R.append(row("I-144", [OIALONE], ["qubit carrier"], "proved-kernel", Lk("GeneralCarrier", 160, "oi_alone_not_qm"), "FAITHFUL",
    notes="Witness diagTheory is the diagonal-preserving theory, i.e. one that never creates coherence."))
R.append(row("I-145", [OIALONE, link("GR box 'bare finite OI ⇏ QM'", G(222), "paper-derivation", [], "proved")],
    ["'OI' formalized as realizing the sealed C1-C4 core on a qubit"], "proved-kernel", Lk("GeneralCarrier", 160, "oi_alone_not_qm"), "FAITHFUL",
    contra=[{"site": "papers/Main.md:2@" + C, "text": "### The Equivalence of Quantum Mechanics and Embedded Observation", "nature": "Main's title asserts an unqualified equivalence; its own body scopes it to finite observable laws (Main:20, Main:624 'three statuses'), and the Introduction (I-145, I-252) denies that OI alone yields QM."},
            {"site": "book/ch00-introduction.md:39@" + C, "text": "Quantum mechanics is therefore an exact observer-level representation of the incomplete finite law, not an extra microscopic postulate placed on top of it.", "nature": "Unscoped: the corpus establishes only the fixed-basis representation (Q_fb); exact operational QM is conditional on (i)–(v). A corpus overclaim relative to GR:222 and ch19:263."},
            {"site": M(624), "text": "none of it makes embedded observation and quantum mechanics inequivalent", "nature": "Compatible but different emphasis: Main denies inequivalence at the finite-law layer; the Introduction denies implication at the operational layer."}],
    notes="Pressure-tested: the witness is a theory realizing a C1–C4 observation process that is not exactly quantum, which is exactly the non-implication claimed. Quantum-equivalence status across the corpus: proved — S_K=D_K=Q_K (kernel), Theorem 4 (kernel), OI ⇏ QM (kernel), OI⁺ ⟺ exact finite endomorphic operational QM (kernel carrier_general_oiPlus, CarrierGeneralOIPlus:213, a characterization of an extension), substratum + continuous off-diagonal controllability ⟺ QM (substratum_plus_control_qm, StructuralClosure:414); conditional — operational QM on (i)–(v)/OI⁺ principles; coherent-completion uniqueness up to unitary gauge and one antiunitary (GR:198, conditional on existence); open — physical source of the resource (ROADMAP F2), relating evolution (P0), H-Bell (P1), K pre-quantum kinematics (P1), H-∞ (P1); settled negatively — the presently stated architecture does not source phases or dense control (ROADMAP:1521 INDEPENDENT), which retires the equivalence endpoint F1 for that architecture."))
R.append(row("I-146",
    [link("GR: 'The substantive physical question it isolates is whether the OI substratum supplies (iii)–(v)'", G(220), "paper-derivation", [], "proved"),
     link("GR substratum-source form: the concrete OI substratum, with one stated phase-intervention principle, 'supplies the structural part in full' (closure under composition, coarse-graining, ancilla blocks; stable under an uncoupled spectator; relabelling- and adjoint-invariant) but, under finite bijective read-write dynamics, 'not the continuously tunable state-mixing operation'; QM is obtained exactly when that resource is added", G(260), "paper-derivation", ["phase intervention assumed"], "proved"),
     link("A read-write-sourced theory has no composite unitary control (fails (iv)); hence not exact QM", Lk("ReadWriteControl", 169, "readWriteSourced_not_control"), "kernel", ["qubit carrier", "ReadWriteSourced: every available composite conjugation is a permutation operator"], "proved"),
     link("The substratum class is an architecture, context-stable, label-invariant, dagger-stable, does not drive the elementary transitions and its generated theory is not finite operational QM", Lk("StructuralClosure", 383, "substratum_residual"), "kernel", [], "proved"),
     link("Substratum class + continuous off-diagonal controllability ⟺ exact finite endomorphic operational QM", Lk("StructuralClosure", 414, "substratum_plus_control_qm"), "kernel", ["Nonempty A"], "proved"),
     link("ROADMAP 'Settled negatively — INDEPENDENT': phases and dense/nonclassical operational control are not sourced by the presently stated architecture; F1 retired for that architecture, F2 (an extension principle) OPEN", "verification/ROADMAP.md:1521@" + C, "paper-derivation", [], "proved")],
    [], "open", G(260), "UNDERCLAIM", cond=None,
    contra=[{"site": "book/ch19-open-problems.md:126@" + C, "text": "the concrete OI substratum supplies the structural architecture ... but, under finite bijective read-write dynamics, not the continuously tunable state-mixing operation", "nature": "Book and GR state a partial answer that the Introduction omits."},
            {"site": "papers/Introduction.md:12@4a260ca9", "text": "Open are which of conditions (iii)–(v) a physical substratum supplies", "nature": "Same understatement in the abstract and at §6.3 (line 183); propagate any fix (outside this range)."}],
    fix="The finite reversible substratum, with a relative-phase intervention assumed, has the structural closure properties, but its bijective read-write dynamics generates no continuously tunable state mixing and so no theory with full reversible control (iv) (machine-checked on the qubit); exact operational quantum mechanics follows exactly when that one controllability resource is added [GR §3.3]. Whether a physical substratum supplies it is open.",
    notes="Attention resolved: the Introduction gives no statement about (i)-(ii) because GR treats them as well-formedness of any operational theory (GR:220, exactAll_iff_substantive). The substantive omission is the kernel-proved negative: under the stated architecture, (iv) is not supplied (readWriteSourced_not_control; substratum_residual; ROADMAP INDEPENDENT rows), and QM follows exactly when continuous off-diagonal controllability is added (substratum_plus_control_qm). 'Which of (iii)–(v) ... is open' reads as if nothing were known. What remains open is whether the physical world supplies the controllability resource and the phase intervention (ROADMAP F2). Whether the stated structural closures coincide exactly with (iii) and (v) of the theorem is not asserted in GR; the fix avoids that identification. Severity moderate: this is the central quantum-equivalence status sentence."))

# ---------------- §3.3 ----------------
R.append(row("I-147", [GL2, REMARK_REL, link("ROADMAP P0 OPEN: what additional structure determines the relative quantum evolution OI leaves free", "verification/ROADMAP.md:63@" + C, "paper-derivation", [], "open")],
    [], "proved-kernel", Lk("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate"), "IMPRECISE",
    fix="### 3.3 Representability does not select the evolution relating two times",
    notes="The body (and Main:624) says representability with ordinary coherence does not select it, and that selection is open — 'this paper neither closes the third nor claims it cannot be closed'. The bare heading 'is not selected' can be read as a claim that nothing selects it. Scope slip in a heading; low severity."))
R.append(row("I-148", [REMARK_REL, GL2], [], "proved-kernel", Lk("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate"), "FAITHFUL"))
R.append(row("I-149", [GL2, REMARK_REL], ["coherent lifts on a fixed carrier and anchor"], "proved-kernel", Lk("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate"), "FAITHFUL",
    notes="Existential, as 'can' says: one exhibited 2x2 instance. The kernel docstring warns that neither GL2 nor GL3 says every time-dependent gauge moves every candidate; 'and then have different relating evolutions' must be read with the same 'can'. Census family 54, status current."))
R.append(row("I-150", [GL3], ["constant unitary right action"], "proved-kernel", Lk("CoherentLiftGauge", 451, "gl3_constant_gauge_preserves_relative"), "FAITHFUL"))
R.append(row("I-151", [link("realData U: evolution U, init uniform 1/|V|, read = id; pad U is the trivial-ancilla padding", "lean:TrackBQfbBridge.lean:43:realData", "kernel", [], "proved"), REMARK_REL],
    [], "proved-kernel", "lean:TrackBQfbBridge.lean:43:realData", "FAITHFUL"))
R.append(row("I-152", [BRIDGE], ["trivial ancilla", "same one-step visible matrix (slice) G"], "proved-kernel", Lk("TrackBQfbBridge", 276, "bridge_traj"), "FAITHFUL",
    notes="bridge_traj is more general (permClass interventions on either side); the Introduction states the identity-intervention case."))
R.append(row("I-153", [ROOTEDIFF, BRIDGE], ["trivial ancilla", "uniform initial law", "identity readout"], "proved-kernel", Lk("TrackBQfbBridge", 180, "rooted_eq_iff_slice_eq"), "FAITHFUL",
    contra=[{"site": M(624), "text": "two such data have equal trajectory laws exactly when their visible laws are equal ... (kernel: `bridge_traj`, `rooted_eq_iff_slice_eq`, `realData_traj_stochastic`)", "nature": "Main states an iff on trajectory laws; the kernel's converse is on rooted families. Equal trajectory laws imply equal rooted families by marginalization, a step not machine-checked; Main's citation is slightly stronger than its kernel anchor. The Introduction states the kernel's form."}],
    notes="Attention resolved (§A.34): the two directions use different middle terms, but harmlessly. Equality of root-conditioned trajectory laws at every horizon implies equality of rooted families (the rooted family is a marginal of the trajectory law), so the stated converse 'rooted families agree ⇒ one-step matrices equal' is stronger than the converse of I-152. Together: one-step equal ⇒ trajectory laws equal (bridge_traj) ⇒ rooted equal (marginalization, unformalized) ⇒ one-step equal (forward of rooted_eq_iff_slice_eq). The Introduction claims no iff, so no §A.34 defect. It cites only the forward direction of an iff declaration; the backward direction (visible_congr) is also proved, so nothing is overstated."))
R.append(row("I-153", [BRIDGE], ["trivial ancilla"], "proved-kernel", Lk("TrackBQfbBridge", 276, "bridge_traj"), "FAITHFUL", sub="I-153.a"))
R.append(row("I-153", [ROOTEDIFF], ["trivial ancilla"], "proved-kernel", Lk("TrackBQfbBridge", 180, "rooted_eq_iff_slice_eq"), "FAITHFUL", sub="I-153.b",
    notes="Forward direction = slice_eq_of_rooted_eq (TrackBQfbBridge:171): the t=1 rooted map is the Born matrix."))
R.append(row("I-154", [REALSTOCH], ["U unitary"], "proved-kernel", Lk("TrackBQfbBridge", 286, "realData_traj_stochastic"), "FAITHFUL",
    notes="Attention resolved: the declaration's conclusion is QfbRealizable(rootTraj K a) ∧ Stochastic(rootTraj K a), so it establishes fixed-basis realizability as well as stochasticity."))
R.append(row("I-155", [REALSTOCH], ["U unitary"], "proved-kernel", Lk("TrackBQfbBridge", 286, "realData_traj_stochastic"), "FAITHFUL"))
R.append(row("I-156", [BRIDGE, ROOTEDIFF, REMARK_REL], ["trivial ancilla at one time"], "proved-kernel", M(624), "FAITHFUL",
    notes="Verbatim from Main:624, which also records that the trivial ancilla is part of the statement (a non-tensor ancilla carried between steps can separate two lifts of one visible law, by exact computation). The Introduction's 'therefore' is confined to 'such data'."))
R.append(row("I-157", [GL2, REMARK_REL], [], "proved-kernel", Lk("CoherentLiftGauge", 537, "gl2_strong_gauge_moves_relative_candidate"), "FAITHFUL",
    notes="Follows from GL2: since representability and coherence leave two lifts with different relating evolutions, uniqueness needs more."))
R.append(row("I-158", [REMARK_REL, link("ROADMAP P0 OPEN, localized two-part (Gram/orbit trajectory across time; cross-time threading)", "verification/ROADMAP.md:63@" + C, "paper-derivation", [], "open")],
    [], "open", "verification/ROADMAP.md:63@" + C, "FAITHFUL"))

# ---------------- §3.4 ----------------
OBSTR = [FACTOR, HKLP,
         link("Main's Proposition imports the unboundedness from HKLP [55] (alternative route Garner–Müller [56]); 'the elementary factorization half proved here, the unboundedness imported'", M(538), "paper-derivation", [], "proved"),
         link("Summary (3): 'No fixed finite classical carrier reproduces full qubit operational behavior — proved under the stated operational interface, the unbounded-dimension half imported'", M(580), "paper-derivation", [], "proved")]
R.append(row("I-159", OBSTR, ["fixed finite realization", "prepare-measure factorization interface"], "proved-paper", M(538), "IMPRECISE",
    contra=[{"site": "papers/Introduction.md:118@4a260ca9", "text": "for every nonempty finite carrier", "nature": "Theorem 4 uses 'carrier' for the quantum system on which exact operational QM is characterized; a finite carrier of size 2 with (i)–(v) is the qubit. The §3.4 heading uses 'carrier' for an ontic substratum. Main uses the word both ways (Main:542 'no fixed finite carrier'; GR:218 'nonempty finite visible system')."}],
    fix="### 3.4 No fixed finite realization reproduces a qubit's prepare-and-measure theory",
    notes="Attention resolved: the heading is broader than the body ('the full prepare-and-measure theory of a qubit exactly') and reuses 'carrier' in a second sense. The body is faithful (I-164)."))
R.append(row("I-160", [FACTOR], ["preparation → finite ontic system → measurement interface"], "proved-paper", M(538), "FAITHFUL",
    notes="No kernel declaration (searched DimensionalObstruction, DimensionalCountermodel, Lean trees for nonnegative factorization). No ledger row (proof-inventory gap list)."))
R.append(row("I-161", [HKLP], [], "proved-paper", "[HKLP24, Thm 4]", "FAITHFUL",
    notes="Imported, as the Introduction says two sentences later; HKLP24 Thm 4 read in the retained PDF text."))
R.append(row("I-162",
    [link("GH03 abstract: a qubit interacting with a classical field can answer a yes/no question that a classical system can answer only if it carries an arbitrarily large amount of information — an explicit task", "[GH03] (arXiv:quant-ph/0110166v3, retained text)", "literature", [], "proved"),
     link("Mon08 abstract: proof that Markovian ontological theories need at least 2N−2 continuous variables (N the Hilbert-space dimension); a lower bound on ontological dimension, not an explicit finite task", "[Mon08] (arXiv:0711.4770v2, retained text)", "literature", [], "proved")],
    [], "proved-paper", "[GH03]", "IMPRECISE",
    fix="explicit tasks are given by Galvão and Hardy [GH03] and by Heinosaari et al. [HKLP24, Thm 4], and Montina bounds the number of continuous ontic variables from below [Mon08]",
    notes="GH03 gives an explicit task (though with sequential local interactions, not bare prepare-and-measure). In the retained text, Mon08 proves a dimension lower bound for Markovian ontological models and states no task; the explicit finite prepare-and-measure tasks the corpus actually relies on are HKLP24's (Main:538 cites [55] only). Low severity; attribution precision."))
R.append(row("I-163", [link("Montina: 'L. Hardy [10]. He proved that the number of ontic states can not be finite' (and again at line 643)", "[Mon08] (arXiv:0711.4770v2, retained text lines 83-85)", "literature", [], "proved")],
    [], "proved-paper", "[Mon08]", "FAITHFUL",
    notes="Verified in Montina's text. [Har04] itself is unread (VERIFY comment), and the Introduction correctly cites it 'as reported'."))
R.append(row("I-164", OBSTR, ["fixed finite realization", "prepare-measure factorization interface", "imported unboundedness of classical dimension [HKLP24]"], "proved-paper", M(538), "FAITHFUL",
    notes="One link is literature (HKLP24 Thm 4, proved there); the corpus link is a written factorization argument. Main's 'under the stated operational interface' is carried by the Introduction's first sentence ('behaviour matrices that factor nonnegatively')."))
R.append(row("I-165", OBSTR, [], "proved-paper", M(538), "FAITHFUL"))
R.append(row("I-166", [link("Proposition text: 'It does not touch the equivalence theorem — there the realization is chosen per finite-horizon law'", M(538), "paper-derivation", [], "proved")], [], "proved-paper", M(538), "FAITHFUL"))

# ---------------- §3.5 ----------------
R.append(row("I-167",
    [link("Main abstract: the equivalence 'does not select the quadratic exponent, which is named as a frontier item'; Main:534: 'Why the quadratic functional is the physical one is therefore a frontier item about the dictionary's origin, not a gap in the equivalence'", M(534), "paper-derivation", [], "open"),
     link("Born Representation Theorem: every M x N stochastic matrix is Γ_ij = tr(E_i P_j) for some POVM and PVM — Born form exists for any stochastic data, so its presence selects nothing", "[Bar26, Thm 3.1] (arXiv:2608.04354v1, retained text line 212)", "literature", [], "proved")],
    [], "open", M(534), "FAITHFUL",
    contra=[{"site": "book/ch18-beyond.md:34@" + C, "text": "The open frontier is not a separate choice of probability exponent inside that representation; it is the common coherent operational extension", "nature": "Different framing: the book places the open frontier in the operational extension and treats the exponent as part of the representation dictionary; Main and the Introduction call the exponent's origin an open frontier item. Not a contradiction of fact (both agree the exponent is not selected), but the book's ch18/ch19:126 wording ('not a separate exponent-selection problem') reads as if nothing about the exponent were open."},
            {"site": "book/ch18-beyond.md:30@" + C, "text": "18.2 The Born rule as dynamical equilibrium", "nature": "The book offers a mechanism proposal (equilibrium reading of the read-write cycle), explicitly 'a structural commitment ... not a proved theorem'; consistent with 'open'."}],
    notes="Verdict pressure-tested: no corpus document claims to derive the exponent."))
R.append(row("I-168", [BELL, BELL_LIT], ["determinism", "pointwise causal cones (interventions local, readout before cones meet)", "setting-independent pre-setting ensemble"], "proved-paper", M(360), "FAITHFUL",
    notes="Matches Main:379's own summary sentence. Main's theorem also assumes a response-fixing microstate, automatic for a deterministic completion's full state. No ledger row (proof-inventory gap list)."))
R.append(row("I-169", [BELL, link("'Determinism is constitutional here, so exactly two hypotheses remain available'", M(379), "paper-derivation", [], "proved")], [], "proved-paper", M(360), "FAITHFUL"))
R.append(row("I-170", [link("(a) Ontic parameter dependence — the option taken; no operational signal", M(392), "paper-derivation", [], "proved"),
                      link("Corollary (Bell–lattice obstruction): the reference nearest-neighbour cubic graph alone cannot supply option (a)", M(394), "paper-derivation", [], "proved")],
    ["H-Bell (for compatibility)"], "conjecture", M(392), "FAITHFUL", cond=["H-Bell"],
    notes="A posited choice, as stated. Completeness note: Main's abstract and Corollary add that the specific nearest-neighbour cubic representative is not itself a Bell-violating completion under measurement independence; preparation-indexed adjacency is needed. The Introduction does not say this; optional."))
R.append(row("I-171",
    [link("Main §3.3: 'What remains to be proved is H-Bell: the prepared graph family must preserve operational no-signaling and satisfy a curvature/metric convergence condition strong enough for the Ollivier–Ricci continuum step'; the hop-metric curvature route FAILS for the reference family before any Bell edge is added", M(394), "paper-derivation", [], "open"),
     link("Substratum H-Bell: preparation-indexed graphs must (i) supply the ontic parameter dependence, (ii) preserve operational no-signaling, (iii) satisfy a metric/Ollivier–Ricci stability condition", "papers/Substratum.md:132@" + C, "paper-derivation", [], "open"),
     link("ROADMAP P1 H-Bell OPEN; 'downstream of a harder obligation' (curvature functional must be re-founded)", "verification/ROADMAP.md:955@" + C, "paper-derivation", [], "open")],
    [], "open", "verification/ROADMAP.md:955@" + C, "FAITHFUL", cond=["H-Bell"],
    contra=[{"site": "papers/Substratum.md:132@" + C, "text": "the preparation-indexed graphs must (i) supply the required ontic parameter dependence, (ii) preserve operational no-signaling, and (iii) satisfy a metric/Ollivier--Ricci stability condition", "nature": "Substratum's H-Bell has a third clause (that the graphs supply the dependence); Main's and the Introduction's two-clause forms omit it. Minor definitional drift across companions."}],
    notes="Completeness note: the corpus records that the stated route to H-Bell's continuum clause already fails for the reference graph (Main:394, ROADMAP:963). The Introduction's 'open' is accurate but does not convey that the existing route is refuted; optional."))

json.dump(R, open(AUD + "/matrix/part-B2.json", "w"), ensure_ascii=False, indent=1)
print(len(R), "rows")
from collections import Counter
print(Counter(r["verdict"] for r in R))

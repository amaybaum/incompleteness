import json, sys, collections

base = sys.argv[1]
inp = json.load(open(base + "/dispositions/input.json"))

def resolve(src):
    parts = [p.strip().replace("@eae01647", "") for p in src.split(";")]
    out, path = [], None
    for p in parts:
        if ":" in p:
            path, line = p.rsplit(":", 1)
        else:
            line = p
        out.append(f"{path}:{line}")
    return "; ".join(out)

E, PC, PP, EL, SC, NP = "elementary", "proof-central", "proof-peripheral", "elementary", "standard-cited", "not-a-proof"

# index -> (category, priority, reason, notes)
D = {
0: (NP, None, "Abstract statement ('The discriminating content is history readback'); no argument.",
    "mislocated: the quoted sentence is at papers/Main.md:20, not :16 (line 16 is the S<=>D<=>Q_fb paragraph)."),
1: (PC, "medium", "Remark carries the written converse of the Corollary (M_t>0 iff readout-relevant memory in every faithful realization) and the one-line derivation of (C1) from (a); the Corollary is labelled 'proved on paper' in Intro §2.4 and feeds the abstract's memory claim.",
    "Short argument; read: correct given Theorem 2(a), existence of one faithful realization at horizon >= t+1 (S_imp_D) and the CMI vanishing criterion. Same content as :99 (entries Main.md:97/:99); review together."),
2: (PC, "medium", "Written derivation of the Corollary (forward: pushforward identity in each realization; converse: in one realization supplied by S_imp_D) plus the unformalized time-t identification; supports abstract claim 'every deterministic completion carries the visible memory' (each with one step not machine-checked).",
    "mislocated: the cited text (faithful realization definition, memory witness, Corollary, 'S<=>D and this universal statement are the paper's core') is on papers/Main.md:99; line :97 is only the 'Layer 1 — reversible dilation' lead-in and :98 a display. Duplicate of entry papers/Main.md:99; review once."),
3: (PC, "high", "Theorem (history readback + finite recurrence implies indivisibility) and its written proof; the history-level (C4) form is the one on-paper step of the abstract's recurrence claim and Intro §2.5.",
    "Read: argument is finite order L => Gamma_L=I; all Gamma_k permutation for k<=t => histories determined by x_0 => no C4 gap; so some Gamma_k is non-permutation; divisor k->L would be a stochastic right inverse, excluded by Lemma (stochastic inverse) at :133-135. Points a reviewer should check: rows of Gamma_k for initial visible states of zero probability (rooted matrix convention), and that the C4 gap time precedes the first non-permutation Gamma_k as needed. Same proof as entries Main.md:139 and :137."),
4: (NP, None, "Summary (the equivalence at maximum proved strength): a status summary restating clauses (2) and (3); the arguments are at papers/Main.md:582-592 and :538.",
    "Line :580 is in R1's line set, but R1 covers only clause (4) (epsilon-realization); these rows cite clauses (2) and (3), which R1 does not review. Their supports are entries Main.md:582/:590/:592 (clause 2) and Main.md:538 (clause 3)."),
5: (PC, "high", "Proof of the history-readback theorem: the step 'history-level C4 => some non-permutation rooted map' is the on-paper step named in the abstract.",
    "Same proof as entries Main.md:137-139 and :137; review once."),
6: (NP, None, "Statement of the two descriptive levels (Friedmann value at the classical level, zero-point sum in emergent QFT) and the status sentence 'descriptive-level distinction is established'; classification, not a derivation.",
    "Line :336 is the emergent-QFT scope paragraph; :338/:340 the two levels; :356 the status paragraph."),
7: (NP, None, "Definition of observation (S, phi, V) (:44), Lemma 2 causal partition (definitional, :50), Lemma 3 determinism/measure (:56), Remark on early commitments (:62).",
    "Row I-022 is a modelling definition."),
8: (NP, None, "Explanatory statement of emergent stochasticity (different hidden states compatible with x send it to different futures).", ""),
9: (NP, None, "Scope/falsifiability statement ('the characterization theorem is mathematical').", ""),
10: (NP, None, "Interpretive statement on uncertainty relations and the hidden sector.",
    "I-032's 'no uncertainty relation constrains fixed-readout visible laws' is an elementary consequence of Theorem 1 (every law in S_K is realized in Q_fb, so the class carries no nontrivial constraint); I-031 restates the Corollary."),
11: (NP, None, "Remark (what this equivalence does and does not say): scope remark.",
    "Embedded elementary step for I-087 checked: the supplied unitaries are permutations with entries 0/1, and 0^p=0, 1^p=1 for p>0, so |U|^p gives the same table for every p>0 (exponent not selected). Verified."),
12: (NP, None, "Status ledger header (:710) and probe-code pointer (:494); no argument.", ""),
13: (NP, None, "Book section heading (§1.11 The card table and the chessboard); location pointer for the card game.", ""),
14: (PC, "medium", "Written proof of Theorem (unavoidable hidden predictive memory) (a)-(c): determinism, TV monotonicity under channels, data processing. Theorem 2 is a numbered §2.4 result; its time-t identification is the abstract's 'one step not machine-checked'.",
    "Read: each step is one line and correct (X_{t+1}=pi_V(phi(X_t,H_t)); Markov chain X_<t -> H_t -> X_{t+1} given X_t; I <= H(H_t|X_t) <= log2|C_H|). The non-kernel content is only identifying the realization's path law of (X_<t, X_t, H_t) with the kernel's joint law; a reviewer could likely close it quickly. For I-049 the data-processing characterisation is confirmed by reading. Same proof as entry Main.md:582."),
15: ("review-R4", None, "Proof of Lemma (accessible backflow from readback) via Pinsker's inequality; part of R4 (Main.md:160-172).", ""),
16: (EL, None, "I-050 is an attribution claim about the structure of the recurrence argument. Check: Step 1 uses phi^N=id (finite order); Steps 2-3 use only the contraction direction of [4,5] (stochastic divisor contracts TV). Verified by reading.",
    "The proof is a written version of Theorem 3, which the Intro states is machine-checked in rooted form."),
17: (NP, None, "Book glossary definition of 'Substratum'.", ""),
18: (NP, None, "Remark (status of the early commitments): 'the bijective substratum is a representation choice' — a status/definition statement.", ""),
19: (NP, None, "Remark (the measure as a realization datum): definitional statement that the emergent law is a function of (phi, partition, mu_H).",
    "Illustration (two-state swap under uniform vs point-mass priors gives different visible laws) is elementary and correct."),
20: (EL, None, "Lemma 3 / Remark: (i) on one cycle of a permutation the invariant measure is uniform; (ii) the counting measure is invariant and has maximal entropy among all measures, hence among invariant ones; (iii) the prior is a realization datum (definitional). Verified by reading.",
    ""),
21: ("review-R2", None, "Theorem (finite-horizon process dilation): R2 (Main.md:496).", ""),
22: ("review-R2", None, "Extension (arbitrary priors — the response-table form): R2 (Main.md:498).", ""),
23: ("review-R2", None, "Status-ledger row (ii)=>(iii) citing the response-table extension: in R2's line set (Main.md:715).",
    "The line itself is a status ledger row, not a proof."),
24: (EL, None, "Lemma (one-step ancilla dilation). Check: <Wi|Wi'> = delta_ii' sum_j T_ij = delta_ii'; |<j,alpha|W|i>|^2 = T_ij delta_alpha,i so the ancilla marginal is T_ij; an isometry extends to a unitary. Verified.",
    "Row I-078 is an attribution claim (coincides with [Bar26, Thm 3.3] and [Sch21, Thm 2]); the literature comparison itself was not checked here."),
25: (EL, None, "Remark (consolidation). Check: a bijection of a finite set has finite order L, so X_{k+L}=X_k pathwise under any fixed prior and the multi-time law is L-periodic; a nonperiodic target therefore has no exact all-time realization by one fixed finite substratum. Verified.", ""),
26: (PP, None, "Proposition (no horizon-independent intervened representation): a dimension count (reachable intervened statistics are a polynomial image of a parameter space linear in K, against a comb family of dimension ~(n_V|A|)^K). It supports only the intervened-case side remark of I-091, a §2.3 scope statement.",
    "Link fit is loose: the Intro claim I-091 concerns passive nonperiodic laws, whose support is the finite-order argument at papers/Main.md:618; this Proposition is about action-labelled combs on a fixed representation. The parameter count n_out d^4 - d^2 and the measure-zero step were not checked."),
27: (PC, "medium", "Theorem (unavoidable hidden predictive memory) = Intro Theorem 2; its written proof (:590) and the unformalized identification of a realization's time-t law with the kernel's joint law support the abstract and §2.4 rows.",
    "Same proof as entry Main.md:590; review once. Read: correct; identification is a definitional step (the realization's path measure induces the joint law of (X_<t, X_t, H_t))."),
28: (EL, None, "Corollary (per-process capacity bound): take the sup over t in the C3 necessity bound, giving I* <= log2 m, i.e. m >= 2^{I*}. Verified.", ""),
29: (EL, None, "Theorem (C3 necessity). Check: X_{>t} is a function of (X_t, H_t) by determinism, so X_<t -> H_t -> X_>t given X_t; DPI then I(X_<t;H_t|X_t) <= H(H_t|X_t) <= log2 m. Verified.",
    "Intro states this bound is machine-checked (C3Necessity.lean) in the same form as Theorem 2."),
30: ("review-R4", None, "Lemma (accessible backflow from readback) statement: R4 (Main.md:160-172).", ""),
31: (EL, None, "I-104: definition of (C1)-(C4). I-107: the (C1) dependency. Check: if no visible transition depends on the hidden state, each X_{t+1} is a fixed function of X_t, so the process is Markov and no two histories with a common present have different next-step laws; hence C4 implies C1. Verified.",
    "The enumeration at (2,2),(2,3),(3,2) is a probe; not re-run."),
32: (EL, None, "Remark (the conditions are diagnostics): (C4) coincides with M_t>0 in a faithful realization. Check: by the CMI vanishing criterion, M_t=0 iff P(X_{t+1}|p,x) is the same for all positive-probability p ending at x, i.e. iff there is no C4 gap; mediation is automatic because every visible correlation passes through (X_t,H_t). Verified.",
    "The vanishing criterion is standard [CT06]; not machine-checked (as the Intro says)."),
33: (EL, None, "(C3) dependency: data processing gives log2|C_H| >= I* in every faithful realization (same check as C3 necessity at papers/Main.md:484-490). Verified.",
    "The bound holds in every realization, with or without C4; 'follows from C4' is satisfied a fortiori."),
34: (EL, None, "Monotone TV is necessary but not sufficient for P-divisibility. Check by an own 2-state example: T1=[[.9,.1],[.1,.9]], T2=[[1,0],[.5,.5]]; d contracts by |det| = 0.8 then 0.5 (non-increasing, strictly contracting), but T1^{-1}T2 has first row (1.0625,-0.0625), a negative entry, so no stochastic divisor. Verified.",
    "The paper's own pairs are in translation_probes.py; not re-run."),
35: (PC, "high", "Theorem (history readback + finite recurrence implies indivisibility): statement and proof (:137-139). Supports I-120/I-122 (§2.5) and I-330 ('on paper for (C4)').",
    "Same proof as entries Main.md:137-139 and :139; review once."),
36: (NP, None, "Scope remark: the result is global over the recurrence cycle; refers to the XOR control as the counterexample to the short-window form.",
    "The XOR control itself is in Appendix/probe material, not at this line."),
37: ("review-R3", None, "Theorem (CP-indivisibility, framework scope): R3 (Main.md:326).", ""),
38: (SC, None, "Breuer–Laine–Piilo criterion [63] (trace-distance backflow witnesses non-Markovianity), Rivas–Huelga–Plenio [4] (ancilla-assisted entanglement witness) and Bylicka–Johansson–Acín [9] (CP-divisibility of invertible maps iff monotone trace distance with a (d+1)-dimensional ancilla).",
    "The 'sufficient, never necessary' direction rests on contraction under divisors (standard) plus the classical P-indivisible-but-monotone example (see entry Main.md:121, verified)."),
39: (NP, None, "Remark (representation, not explanation): interpretive scope remark.", ""),
40: (SC, None, "Heinosaari–Kerppo–Leppäjärvi–Plávala [55]: qubit prepare-and-measure behaviours have unbounded nonnegative rank (classical dimension) over finite prepare-measure sets; alternative route Garner–Müller [56].",
    "The in-house half is elementary and verified: a fixed N-state realization has B = Xi M with M column-stochastic and Xi in [0,1], so nonnegative rank <= N. I-166 is a scope sentence of the Proposition."),
41: (PC, "low", "Theorem (Bell ceiling for a screened local completion) and its 4-line proof; Intro §3.5 result (I-168) and §6 claims (I-249, I-250).",
    "Standard Bell/CHSH local bound once (i)-(iv) are granted; the framework-specific step is the coupling-graph cone lemma at papers/Main.md:358 (induction on graph distance, elementary). Certified by a probe (check 11)."),
42: (EL, None, "Contrapositive of the Bell ceiling with determinism held fixed: to exceed |S_CHSH|=2 a deterministic completion must drop pointwise cone locality (ontic parameter dependence) or the common pre-setting ensemble (measurement independence). Verified by reading.",
    "mislocated: the quoted sentence 'Determinism is constitutional here, so exactly two hypotheses remain available' is at papers/Main.md:389; :379-381 carries the bold contrapositive. Hypotheses (ii)-(iii) are folded into the cone-locality option."),
43: (NP, None, "Statement of the two descriptive levels (classical Friedmann density; emergent zero-point sum).", ""),
44: (EL, None, "Status paragraph plus the two-completions argument. Check (I-184): adding C*I to the emergent generator multiplies the evolution by a global phase e^{-iCt}, leaving every transition probability unchanged; the two gravitational equations differ only on the gravitational side, so they share substratum, partition, reduced law, representation and calibration. Verified.",
    "I-175/I-180/I-181/I-182 are status statements (descriptive distinction established; coupling theorem open at G3)."),
45: (NP, None, "Book mirror of GR §6.2's status sentence ('The descriptive distinction is established').", ""),
46: (NP, None, "GR abstract / dependency ladder: status ledger (G3 open) and the target equation form.", ""),
47: (NP, None, "Premise statement: gravity is sourced by the classical stress-energy of the total microstate.", ""),
48: (NP, None, "Scope statement: the framework does not explain why rho ~ H^2/G.", ""),
49: (NP, None, "Book mirror of GR's scope statement on the vacuum-energy scale.", ""),
50: (NP, None, "Scope statement: coupling of EW/QCD transition energy needs the same open step.", ""),
51: (NP, None, "BHa answer to claim A: explanatory statement (bijectivity is global, records are a projection); its support is the exhaustive counterexamples, not a proof.", ""),
52: (NP, None, "Book statement that recovery is a separate question bijectivity does not settle.", ""),
53: ("review-R5", None, "BHa proofs section: Lemma 0, C1, C2, C3, C4 (Lemma L), D1 are R5.",
    "Lines 139-142 (item E, the GR Theorem A.1 Fubini identity) are outside R5's list; elementary (the same terms summed in two orders) and carry no Intro claim. Row I-208 only needs the characterisation 'written proofs checked exhaustively at small size', which the section heading at :88 states."),
54: (NP, None, "BHb verdict summary lines (C1, C2 universal proofs; C6 textual analyses of GR A.8-A.9); a status summary for I-208.",
    "BHb C1 (permutation maps basis vectors to basis vectors, so orbit states are product, S(R)=0) is elementary and verified; BHb C2 (entropy budget, S(R) <= H(p0)) is a short written proof not under R1-R5 and carries no Intro claim in this input. BHb is not covered by R5 (BH-01 only)."),
55: (PP, None, "GR Theorems A.8-A.9 with proofs (Lévy/HLW measure concentration plus cycle counting; A.9 by substitution), conditional on H-scramble and H-decouple. The Intro reports them as conditional and not established, and row I-208 needs only their nature (measure-concentration argument, not a finite computation), which is checkable by reading.",
    "Cycle-counting step read: a bad cycle needs f_j >= eps/ln d_min, giving the stated fraction bound. If the Intro §5 sentence restating A.8's conditional conclusion is audited elsewhere, a low-priority review of this proof would cover it."),
56: (NP, None, "BHa scope list: maps not derived from OI's substratum; prior and layout taken from GR App. A.", ""),
57: (NP, None, "BHb scope line: no specific substratum map tested.", ""),
58: (EL, None, "Written counterexample F(b,r)=(b,r). Check: the identity is a bijection; the radiation register r is unchanged and independent of b, so the radiation reveals nothing about b while all information is conserved. Verified.", ""),
59: ("review-R5", None, "BHa C1 written proof (REPORT.md:98-102) and the independent review's verdict line (REVIEW.md:3): R5.", ""),
60: ("review-R5", None, "BHa C2 written proof (P_succ >= 1/|K|): R5.", ""),
61: (NP, None, "BHa scope line: uniform message prior with equal-size supports.", ""),
62: (EL, None, "Corollary of C2. Check: zero advantage means P_succ = 1/|M|; C2 gives P_succ >= 1/|K|; hence |K| >= |M|. Verified (given C2, which is R5).",
    "Line 318 is a post-review change record ('Claim A qualified by C2'), not an argument."),
63: (SC, None, "The known fact: guessing probability rises by at most a factor |K| with |K|-valued side information (the min-entropy chain rule, H_min(X|YK) >= H_min(X|Y) - log|K|).",
    "The corpus names the fact without a citation. Lines 109-112 lie inside C2's text (R5); the row's attribution claim is what is classified here."),
64: (NP, None, "GR App. A.1 definition of C_V x C_B x C_D (:719) and the A.7 evaporation setup with B -> R mode transfer (:807).", ""),
65: (EL, None, "H-scramble fails for every bijection on a definite configuration. Check: a bijection maps configurations to configurations, so the orbit consists of product basis states across an aligned bipartition and S(rho_R)=0 along it, while S_Page>0. Also checked the stated gap ln4 - 4/8 = 0.886 nats at d_B=d_R=4. Verified.", ""),
66: (NP, None, "Book mirror of GR App. A's H-scramble remark.", ""),
67: (EL, None, "Timescale ordering. Check: t_evap ≈ 8.4e-17 s (M/kg)^3 equals 1/H ~ 1e17 s at M ≈ 1e11 kg, and is ~1e79 s at 30 M_sun, so t_evap >> tau_B^D; Theorem A.7 is stated for t << tau_B^D, hence it cannot supply H-decouple over the evaporation. Verified (consistent with BHa item F's interval [1.06e10, 4.92e12] kg).",
    "I-267 is a not-claimed statement (no claim that A.7 fails within its stated scope); this line confirms A.7's stated scope."),
68: (NP, None, "Theorem A.8 statement: whole configuration space as a single energy shell. Textual check: verified at :817.", ""),
69: (EL, None, "Proper energy shells. Check: if the Hamiltonian takes more than one value on C_B x C_R, its shells are proper subspaces, so the full product space is a single shell only when the energy is constant there. Verified. (Side value checked: diagonal-shell mean H_2 - 1 = 1/2 against Page's exact 1/3 at d_B=d_R=2.)", ""),
70: (NP, None, "Statement that an evaporating black hole whose radiation carries away its energy is in the proper-shell case (GR :843) and its book mirror (ch07:126).",
    "Implicit reasoning: energy moves between B and R, so the Hamiltonian on C_B x C_R is not constant. Asserted, not derived."),
71: (NP, None, "Scope remark: Theorem A.9 is a full-cycle average at a fixed bipartition.", ""),
72: (EL, None, "PR-box from the response-table construction when the wings share globally coupled setting-dependent hidden dynamics. Check: the PR box is a finite conditional law P(q,r|a,b); a global register that reads both settings and outputs from a stored response table realizes any such table, so representability does not bound CHSH. Verified at the level stated; the construction text itself (§3.4) was not re-read.", ""),
73: (NP, None, "Abstract statement (Bell accounting; parameter dependence or setting-dependent ensembles); contrapositive of the Bell ceiling.", ""),
74: (NP, None, "Remark (three notions, kept apart): definitions of notions (1)-(3) and a scope disclaimer.", ""),
75: ("review-R5", None, "BHa generated verdict line for C1 (status summary of an R5 proof).",
    "The link also cites C2, whose verdict line is :21, not :20."),
76: (NP, None, "BHb C6(c) verdict line: textual analysis of GR A.8's shell factorization, with certified numerical bounds; status summary.",
    "The link cites C6(b)-(d), which span lines :19-:21; line :20 is C6(c) only."),
77: (NP, None, "Theorem A.7 statement (effective pure state on t << tau_B^D).", ""),
78: (NP, None, "Book statement: a card mechanism is a local classical toy; no card arrangement violates a Bell inequality.",
    "Follows from the Bell ceiling (deterministic local cards with a setting-independent deal)."),
79: (NP, None, "Statement that the vacuum-energy normalization rho_Lambda ~ H^2/G is the Friedmann scale and its value an input.", ""),
80: (PC, "medium", "Written derivation of the Corollary (M_t>0 iff readout-relevant hidden memory in every faithful realization) and the unformalized time-t identification; supports I-299 (§6.4 conclusion).",
    "Same content as entries Main.md:97 (whose cited text is this line) and Main.md:592; review once."),
81: (NP, None, "Abstract statement ('every faithful deterministic completion contains readout-relevant hidden predictive memory').", ""),
82: (NP, None, "Book description of the two-card game (definition of the example).",
    "mislocated (minor): book/ch01-observation.md:265 (and FULL:609) is the §1.11 heading; the game's rules (burn card, shuffle, peek with forced re-burn) are at book/ch01-observation.md:271-282."),
83: (NP, None, "Definition of the visible-sector channel Phi(rho_V) = Tr_H[U_phi(rho_V ⊗ rho_H)U_phi†] with rho_H = I_m/m (set at :276).",
    "The display at :278 shows rho_H; the substitution rho_H = I_m/m is in the preceding sentence. The constant-channel claim for the card game rests on entry Main.md:286."),
84: (EL, None, "Remark (failure of (C1)). Check: for the swap, Tr_H[SWAP(rho ⊗ I/2)SWAP†] = tr(rho) I/2, a constant channel, hence measure-and-prepare and entanglement-breaking. Verified.", ""),
85: (EL, None, "Swap with an initialized hidden slot. Check: step 1 gives rho -> |0><0|, step 2 returns rho. Any instrument summing to rho -> tr(rho)|0><0| has elements rho -> c_o(rho)|0><0|, so every outcome-conditioned processing is measure-and-prepare (entanglement-breaking) and so is their sum, while the identity is not; no classical-memory decomposition exists. Verified.", ""),
}

assert len(inp) == 86 and set(D) == set(range(86))
out = []
for i, e in enumerate(inp):
    cat, pri, reason, notes = D[i]
    rows = sorted(set(l["row"] for l in e["links"]), key=lambda r: (int(r.split("-")[1].split(".")[0]), r))
    out.append(dict(source=e["source"], resolved_source=resolve(e["source"]), category=cat,
                    priority=pri, reason=reason, rows=rows, notes=notes))
json.dump(out, open(base + "/dispositions/dispositions.json", "w"), indent=1, ensure_ascii=False)
c = collections.Counter(o["category"] for o in out)
print(c)
for o in out:
    if o["category"] == "proof-central":
        print(o["priority"], o["resolved_source"], o["rows"])
for o in out:
    if "mislocated" in o["notes"]:
        print("MIS", o["resolved_source"])

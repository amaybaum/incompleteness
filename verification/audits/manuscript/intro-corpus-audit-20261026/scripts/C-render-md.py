import json, sys, collections
S=sys.argv[1]; A=sys.argv[2]
ns={}; exec(open(f'{S}/C-completeness-data.py').read(), ns); CMP=ns['ROWS']
ns2={}; exec(open(f'{S}/C-consistency-data.py').read(), ns2); CON=ns2['ROWS']
TITLES={
 "CMP-01":"ε-realization, gluing and finite-test density (Main §3.4)",
 "CMP-02":"Stated substratum does not supply condition (iv); one control resource completes it (GR §3.3, kernel)",
 "CMP-03":"Full reversible control realizes the OI core: Theorem 4 classifies, it does not derive",
 "CMP-04":"OI⁺ and its primitive-source and typed forms",
 "CMP-05":"Coherent-completion classification and orientation no-go",
 "CMP-06":"Bohr-frequency completeness; two-branch form conditional on H-BG",
 "CMP-07":"Exact one-time classification of lift freedom (fibre-Gram data)",
 "CMP-08":"Intervention dilation (classical comb) and the horizon obstruction",
 "CMP-09":"Bell: cost of measurement dependence; PR-box countercontrol",
 "CMP-10":"Main's Characterization theorem (Main:516, proof :608)",
 "CMP-11":"Fixed-Ĥ form; non-unique continuous interpolation",
 "CMP-12":"Canonical predictive quotient",
 "CMP-13":"Passive observation in the kernel",
 "CMP-14":"Lemma 3 measure selection in the kernel",
 "CMP-15":"Deep-sector cardinality is gauge",
 "CMP-16":"Separability threshold (lattice realization)",
 "CMP-17":"Open obligations missing from §6.3 (kinematics, H-∞, (Obs, μ), lattice C4)",
 "CMP-18":"SM exact geometry (H-link conditional)",
 "CMP-19":"Further black-hole theorems (A.1–A.7, Page-time β-dependence)",
 "CMP-20":"GR's further Λ claims",
 "CMP-21":"Genericity of the non-permutation witness",
 "CMP-22":"Independent-prior realization for every law, not only rational ones",
 "CMP-23":"All-time rooted classification: realizable ⟺ periodic (kernel only)",
 "CMP-24":"(C2) necessity is proved under the mixing hypothesis",
 "CMP-25":"BHb C2: permutation entanglement capped by initial basis entropy",
 "CMP-26":"BHa D1/D2 and the linear rank law",
}
def st(r):
    s=r['status']; x=s['proof_status']
    if s.get('conditional_on'): x+=" (on "+"; ".join(s['conditional_on'])+")"
    return x
L=[]
L.append("# Completeness: established results the Introduction omits or understates (audit step 5)\n")
L.append("Mapper C. Introduction at `4a260ca9`; corpus at `eae01647`. Machine-readable rows: `completeness.json`. Each row was checked against the source it cites; kernel rows against the `.lean` statement.\n")
L.append("The question for each row is the owner's: does the corpus establish, proved or conditionally derived, something on the Introduction's subject that the Introduction omits or states more weakly? A row is not a recommendation to add it: the Introduction limits its scope on purpose, and each row says whether that scope should carry the result.\n")
c=collections.Counter(r['recommendation'] for r in CMP); p=collections.Counter(r['priority'] for r in CMP)
L.append(f"**Counts.** {len(CMP)} rows: {c['strengthen']} strengthen, {c['add']} add, {c['cite']} cite, {c['leave out']} leave out. Priority: {p['high']} high, {p['medium']} medium, {p['low']} low.\n")
L.append("## What the Introduction should change\n")
L.append("1. **CMP-01 (high), with CMP-08.** §3.4 gives only the obstruction (no fixed finite carrier reproduces a qubit). Main proves the positive half on paper: for fixed dimension, instrument family, horizon and accuracy, one finite reversible realization reproduces every adaptive protocol within ε, and the realized and quantum operational theories are mutually ε-dense. Main's own summary calls this the maximal equivalence available. The Introduction should state it, with its limit (density, not identity).")
L.append("2. **CMP-02 (high), with CMP-03.** The Introduction says which of (iii)–(v) a physical substratum supplies is open. For the substratum as stated the kernel settles part of it: the stated finite read-write architecture does not supply (iv), and with an assumed phase intervention one continuous state-mixing operation completes it to exact finite operational QM. What is open is whether a physical substratum supplies that operation. Add also that full control realizes the OI core, so Theorem 4 classifies and does not derive.")
L.append("3. **CMP-22.** L56 restricts the independent-prior realization to rational laws; Main's response-table extension removes the restriction (confirms B1's I-071).")
L.append("4. **CMP-05, CMP-07, CMP-09, CMP-12, CMP-14, CMP-23, CMP-25: cite.** One clause each, optional, all sharpening statements the Introduction already makes.")
L.append("5. **CMP-17, CMP-24: §6.3's open list.** Add the assumed complex matrix kinematics, H-∞, the (Obs, μ) interface and the lattice cut of (C4); reword (C2) necessity as proved under an open hypothesis.\n")
L.append("Nothing in the corpus makes the Introduction's central claims too weak to stand: the deliberate limits (no derivation of QM, Born exponent not selected, Λ a proposal, Page curve not established) are all borne out.\n")
L.append("## Main's Characterization theorem (Main:516, proof Main:608)\n")
r10=[r for r in CMP if r['id']=='CMP-10'][0]
L.append(r10['result']+"\n")
L.append("- **Proof and status.** Both directions of (ii)⟺(iii) are proved in prose (Main:608) and neither is formalized: (iii)⟹(ii) is the Pinsker readback lemma (Main:167); (ii)⟹(iii) is existence by process dilation (Main:496), whose correlated-prior form is the kernel's `S_imp_D`. Clause (i) is imported from Barandes under (T), which is checked only by probes at (2,2), (2,3), (3,2). The theorem has no ledger or census row (signal S1).")
L.append("- **Introduction.** It does not name the theorem but carries its proved content at equal or higher rigor: Theorem 1 (kernel) for existence and for the representation, which supersedes (i) in rigor; the Corollary (L82) for the per-witness biconditional; L84 and L86 for the readback bound and C1/C3 following from C4. Omitted: the compressed ≤n³ form of (i) under (T), and the time-homogeneous fixed-Ĥ form.")
L.append("- **Recommendation.** Leave the name out; optionally one sentence assembling the biconditional, labelled 'proved on paper; not machine-checked' and 'time-homogeneous'. Corpus issues found while checking: CON-17 (no ledger row), CON-18 (Main:72 vs :76), CON-19 (appendix B's proof structure differs from Main's).\n")
L.append("## Summary table\n")
L.append("| ID | Pri. | Result | Status (weakest link) | Introduction | Recommendation |")
L.append("|---|---|---|---|---|---|")
for r in CMP:
    L.append(f"| {r['id']} | {r['priority']} | {TITLES[r['id']]} | {st(r)} | {r['intro_treatment']['kind']} ({', '.join(x.split(':')[1].split('@')[0] for x in r['intro_treatment']['sites'])}) | **{r['recommendation']}** |")
L.append("\nIntroduction line numbers are at `4a260ca9`.\n")
L.append("## Rows\n")
for r in CMP:
    L.append(f"### {r['id']} — {TITLES[r['id']]}\n")
    L.append(f"- **Result.** {r['result']}")
    L.append(f"- **Sources.** " + "; ".join(f"`{x}`" for x in r['sources']))
    L.append(f"- **Proof location.** {r['proof_location']}")
    s=r['status']
    L.append(f"- **Status.** {st(r)}; layer: {s['layer']}; kernel: {s['kernel']}; ledger: {s['ledger']}. Hypotheses: " + ("; ".join(s['hypotheses']) if s['hypotheses'] else "none beyond scope") + f". Weakest link: {s['weakest_link']}.")
    it=r['intro_treatment']
    L.append(f"- **Introduction.** {it['kind']} — " + ", ".join(f"`{x}`" for x in it['sites']) + (f". {it['note']}" if it.get('note') else ""))
    L.append(f"- **Should the scope carry it?** {r['scope']}")
    L.append(f"- **Recommendation: {r['recommendation']}.**" + (f" {r['proposed_text']}" if r.get('proposed_text') else ""))
    if r.get('notes'): L.append(f"- **Notes.** {r['notes']}")
    L.append("")
L.append("## Mapper items folded in\n")
L.append("Each was re-verified at the cited source before inclusion. B1: ε-realization (CMP-01), coherent completions and OI⁺ (CMP-05, CMP-04), comb (CMP-08), independent prior (CMP-22, confirms I-071), Characterization theorem optional (CMP-10). B2: negative sourcing (CMP-02), OI⁺ (CMP-04), coherent uniqueness (CMP-05); the general Theorem 3 is already in the Introduction, kernel-only in the corpus (CON-41). B3: BHb C2 (CMP-25), A.6 (CMP-19, leave out), BHa D1 and the linear rank law (CMP-26). B4: negative sourcing (CMP-02, adds `frozen_sourcing_verdict`, `substratum_residual`), all-time rooted classification (CMP-23), (C2) necessity (CMP-24), open items (CMP-17). B5: independent prior (CMP-22).\n")
open(f'{A}/COMPLETENESS.md','w').write("\n".join(L))

# CONSISTENCY
M=[]
M.append("# Corpus consistency for the Introduction's topics (audit step 4, corpus-wide)\n")
M.append("Mapper C. Corpus at `eae01647`; Introduction at `4a260ca9`. Machine-readable rows: `consistency.json`. Sites are `file:line@eae01647`; `[FULL:n]` is the byte-identical mirror line in `book/The-Incompleteness-of-Observation-FULL.md`.\n")
M.append("Each row gives the conflicting or incomplete formulations, the authoritative anchor (the most rigorous statement, not the most detailed), its severity, whether it touches the Introduction, and a proposed resolution. Discrepancies outside the Introduction are corpus findings for separate correction; nothing here edits the corpus. The early signals S1–S13 of PROOFS-README.md are each resolved into a row, and #939's ħ and θ₀ corrections were re-checked corpus-wide (CON-40).\n")
sv=collections.Counter(r['severity'] for r in CON); ti=sum(r['touches_intro'] for r in CON)
M.append(f"**Counts.** {len(CON)} rows: {sv['high']} high, {sv['medium']} medium, {sv['low']} low, {sv['info']} informational. {ti} touch the Introduction (as a site, or because the Introduction relies on the conflicting source). Rows on lines #939 edited: {sum(r['changed_by_939'] for r in CON)}.\n")
M.append("## Findings that touch the Introduction\n")
M.append("- **CON-01 (high).** GR Theorem A.8 counts initial *configurations* with the B|R bipartition aligned to them — exactly the setting in which GR:833–835 shows H-scramble fails for every bijection. The conditional result is vacuous as stated; GR:835 assigns the failure only to A.7's proof. The Introduction reports A.8's 'all but an exponentially negligible fraction of initial conditions' without saying this.")
M.append("- **CON-42 (medium).** Intro L106: 'no unconditional implication holds among' the three notions. Main:334 says only that none 'is asserted', and Main:606 states that Markov implies P-divisible, so P-indivisibility implies memory at some time.")
M.append("- **CON-25 (medium).** Intro L84 calls the Pinsker-bound probes 'exact'; `c4_backflow_probes.py` evaluates the information quantities in floating point with 1e-12 tolerances (Main:170 says 'Certified exactly').")
M.append("- **CON-24, CON-41, CON-43, CON-26 (low).** 'Minimal model' with six hidden states beside a two-state 'smallest' realization; the general Theorem 3 is kernel-only (Main §2.3 proves the uniform-prior special case); the cited routed-readback declaration uses a frozen spelling, with a storage-time variant available; the fixed-dimension counterexample used only uniform priors.")
M.append("- **Faithful against conflicting corpus (the corpus is wrong, the Introduction right):** CON-02 (book: BH paradox 'resolved'), CON-04 (Λ 'dissolution' headings), CON-06 (GR §6.2 asserts Einstein's equations while G3 is open), CON-10 (QM 'derived'), CON-12 and CON-44 (Born exponent framing), CON-21 (bijectivity a 'lemma'), CON-22 (finiteness of S from Lemma 1).\n")
M.append("## Anchors by topic\n")
M.append("| Topic | Authoritative anchor | Rows |")
M.append("|---|---|---|")
M.append("| Embedded observation (finiteness, bijectivity, measure) | Main:62 Remark (status of the early commitments) and Main:708 posit ledger; kernel `CanonicalMeasure` | CON-21, CON-22 |")
M.append("| Finite-horizon correspondence | Main §3.4 Theorem (finite-horizon equivalence) with kernel `finite_horizon_equivalence`; Main:758 for the meaning of 'equivalence' | CON-16, CON-46, CON-20, CON-28 |")
M.append("| Characterization theorem | Main:516 with proof Main:608 (prose; not formalized) | CON-17, CON-18, CON-19, CON-27 |")
M.append("| Hidden memory | Main §3.4 Theorem (unavoidable hidden predictive memory), kernel `HiddenMemory` for the joint-law form | CON-25, CON-26, CON-42 |")
M.append("| Recurrence and indivisibility | kernel `pIndivisible_of_rooted_identity_return_of_overlap`; Main:137 for readback ⟹ indivisibility | CON-23, CON-24, CON-41, CON-43, CON-38 |")
M.append("| Quantum emergence, operational QM | GR §3.3 (kernel characterization and substratum-source form); Main:562, :624 | CON-09, CON-10, CON-11, CON-13, CON-14, CON-15, CON-30, CON-46, CON-47, CON-48 |")
M.append("| Born rule | Main:534 (exponent not selected; origin a frontier item) | CON-12, CON-44 |")
M.append("| Bell | Main §3.3 Bell ceiling theorem; H-Bell at Substratum:132 | CON-45 |")
M.append("| Relating evolution / phase locking | Main:624; GR:182 for H-BG's open status | CON-29, CON-47 |")
M.append("| Cosmological constant | GR §6.2 (:358): descriptive distinction established, dissolution conditional on G3 | CON-04, CON-05, CON-06, CON-07, CON-08 |")
M.append("| Black-hole information | GR App. A.7 (:833–:845) with ch07:161 (conservation is a premise) | CON-01, CON-02, CON-03 |")
M.append("| Outside the Introduction's topics | SM §7.6 table (:1255–:1300); #939 CHANGE-NOTE | CON-31–CON-37, CON-39, CON-40 |")
M.append("")
M.append("## Early signals S1–S13\n")
M.append("S1 → CON-17. S2 → CON-29. S3 → CON-30. S4, S6 → CON-34. S5 → CON-32 (extended: SM's abstract, a line #939 edited, also says 0.23σ). S7, S8 → CON-33 (S8's 105.74 MeV row is now distinctly labelled by #939; the chain-table label remains ambiguous). S9 → CON-35. S10 → CON-21. S11 → CON-36. S12, S13 → CON-37.\n")
M.append("## #939 (ħ framing and θ₀)\n")
r40=[r for r in CON if r['id']=='CON-40'][0]
M.append(r40['resolution']+"\n")
M.append("## Summary table\n")
M.append("| ID | Sev. | Topic | Kind | Touches Intro | #939 line |")
M.append("|---|---|---|---|---|---|")
for r in CON:
    M.append(f"| {r['id']} | {r['severity']} | {r['topic']} | {r['kind']} | {'yes' if r['touches_intro'] else 'no'} | {'yes' if r['changed_by_939'] else ''} |")
M.append("\n## Rows\n")
for r in CON:
    M.append(f"### {r['id']} — {r['topic']} ({r['severity']}; {r['kind']}; signal: {r['signal']})\n")
    M.append("**Sites.**\n")
    for x in r['sites']: M.append(f"- `{x['site']}` — {x['text']}")
    M.append(f"\n**Anchor.** `{r['anchor']['site']}` — {r['anchor']['why']}\n")
    M.append(f"**Touches the Introduction:** {'yes' if r['touches_intro'] else 'no'}." + (f" {r['intro_note']}" if r.get('intro_note') else "") + "\n")
    M.append(f"**Proposed resolution.** {r['resolution']}\n")
M.append("## Mapper items folded in\n")
M.append("All were re-verified at the cited lines. B1: Main:46 finiteness (CON-22), Methodology bijectivity (CON-21), GR §6 heading (CON-04), ch01:261 (CON-10), Main:704/:706 (CON-27), BH-01 header (CON-03), Main:170 float probe (CON-25). B2: ch00:39 (CON-46), H-Bell clauses (CON-45), GR:216 setting (CON-48), Born framing (CON-44), Main:624 biconditional (CON-47), Main:334 (CON-42), routed readback spelling (CON-43), Theorem 3 kernel-only (CON-41). B3: A.8 setting (CON-01), 'resolved' status (CON-02), dissolution headings (CON-04), GR:352 ħ (CON-08: #939 classed it CONTEXT-OK; kept as optional), GR:573 (CON-05). B4: Main title (CON-16), headings (CON-04), appendix C:317 (CON-07), Main:758 (CON-14), Main:594 probe priors (CON-26; B4's recheck count not reproduced here), BH-01 header (CON-03). B5: minimal model (CON-24), B.2.5 (CON-30), routed-readback spelling (CON-43: no manuscript names either predicate; it touches only the Introduction's Appendix A).\n")
open(f'{A}/CONSISTENCY.md','w').write("\n".join(M))
print('ok')

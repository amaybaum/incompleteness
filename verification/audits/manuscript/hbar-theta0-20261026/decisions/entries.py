# (group, id, file, line, old, new)
CH7='book/ch07-gravity.md'; CH6='book/ch06-matter-content.md'; CH9='book/ch09-universality.md'
E=[]
def e(g,i,f,n,o,nw): E.append((g,i,f,n,o,nw))
# ---------------- N-H: ħ corrections (no owner decision)
e('H','H1',CH7,10,r"The horizon's geometric and thermodynamic properties — surface gravity $\kappa$, area $A$, Hawking temperature $T$ — fix the values of the emergent physics: the action scale $\hbar$, the Bekenstein-Hawking entropy with its $1/4$ coefficient, the form of the dark-energy equation of state.",
 r"The horizon's thermodynamics relates the emergent action scale $\hbar$ to the discreteness scale $\epsilon$, with $\kappa$ and $A$ dropping out of $\hbar$ (Sections 7.3–7.4); it recovers the Bekenstein-Hawking entropy with its $1/4$ coefficient as a consistency relation of that calibration and supplies the dark-energy bookkeeping read in the running-vacuum channel (Section 7.8).")
e('H','H2',CH7,14,r"the value of $\hbar$, the discreteness scale",r"the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the discreteness scale")
e('H','H3',CH7,36,r"The most distinctive content of the framework's gravitational sector is the derivation of Planck's constant $\hbar$ as an emergent quantity determined by the cosmological horizon's thermodynamic properties. The standard view treats $\hbar$ as a fundamental constant of nature whose value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ is measured rather than derived.",
 r"The most distinctive content of the framework's gravitational sector is the treatment of Planck's constant $\hbar$ as an emergent action scale whose relation to the boundary geometry is fixed by the cosmological horizon's thermodynamics. The standard view treats $\hbar$ as a fundamental constant of nature, its value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ measured.")
e('H','H4',CH7,50,r"a QFT on a bifurcate Killing horizon, under the H-Hawking conditions, background must be periodic in imaginary time with period $\beta = 2\pi c / \kappa$, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$. This is a theorem *within* the derived QFT, not an external import — the regularity requirement follows from the Wick rotation's analytic structure.",
 r"a QFT on this bifurcate Killing horizon background is periodic in imaginary time with period $\beta = 2\pi c / \kappa$ under the H-Hawking conditions, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$ when the emergent state belongs to that KMS class (H-spectrum). The step is therefore a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).")
e('H','H5',CH7,82,r"This is not an additional empirical input but an algebraic consequence of the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ together with the definition of $l_p$.",
 r"It adds no relation beyond the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ and the definition of $l_p$, and its numerical value takes the measured $\hbar$ as input.")
e('H','H6','book/ch01-observation.md',87,r"Chapter 7 shows that the cosmological partition produces $\hbar$ as a thermodynamic identity at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following under the horizon conditions named there",
 r"Chapter 7 shows that, under the horizon conditions named there, the cosmological partition relates $\hbar$ to the discreteness scale through a thermal self-consistency condition at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following")
e('H','H7','book/ch02-substratum.md',22,r"Chapter 7 develops each of these as theorems;",r"Chapter 7 develops each of these under the conditions it names;")
e('H','H8','book/ch02-substratum.md',110,r"Stage 3 takes Stage 2's output and derives the emergent value of $\hbar$. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics — forces the relation",
 r"Stage 3 takes Stage 2's output and derives the emergent action-scale relation. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics, conditional on H-slope with the horizon and frame conditions named there — forces the relation")
e('H','H9','book/ch02-substratum.md',112,r"as the unique simultaneous solution.",r"as the unique simultaneous solution, which fixes only the ratio $\epsilon/\sqrt{\sigma} = 2\,\ell_P$.")
e('H','H10','book/ch02-substratum.md',228,r"the boundary thermodynamics, the value of $\hbar$, the Bekenstein-Hawking",r"the boundary thermodynamics, the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking")
e('H','H11','book/ch00-introduction.md',97,r"the Bekenstein-Hawking $1/4$ factor and the value of $\hbar$ from horizon thermodynamics under named horizon conditions",r"the Bekenstein-Hawking $1/4$ factor and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ as consistency relations of horizon thermodynamics under named horizon conditions")
e('H','H12','book/ch04-methodology.md',204,r"the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from horizon thermodynamics are conditional on",r"the Bekenstein-Hawking $1/4$ coefficient and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ from horizon thermodynamics are consistency relations conditional on")
e('H','H13',CH6,348,r"the value of $\hbar$ from horizon thermodynamics,",r"the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ relating the action scale to the discreteness scale (a self-consistency condition, §7.4),")
e('H','H14a',CH9,14,r"Some predictions are *universality-class* results",r"Some results are *universality-class* results")
e('H','H14b',CH9,14,r"the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry conditional on the horizon conditions named in Chapter 7",r"the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$ from partition geometry, consistency relations conditional on the horizon conditions named in Chapter 7")
e('H','H15',CH9,48,r"the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry sit at the same level",r"the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, consistency relations, sit at the same level")
e('H','H16',CH9,92,r"*The value of $\hbar$ from partition geometry.*",r"*The action-scale relation from partition geometry.*")
e('H','H17',CH9,118,r"Bekenstein-Hawking $1/4$ and $\hbar$ from partition geometry under the horizon conditions of Chapter 7",r"the Bekenstein-Hawking $1/4$ and the action-scale relation for $\hbar$ as consistency relations under the horizon conditions of Chapter 7")
e('H','H18','book/ch12-evolution-intelligence.md',197,r"— the value of $\hbar$, the Standard Model,",r"— the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the Standard Model,")
e('H','H19','book/glossary.md',73,r"The framework's derivation of Planck's constant from horizon thermodynamics.",r"It relates Planck's constant to the discreteness scale, conditional on H-slope, and fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$: a self-consistency condition, not an independent determination of the value of $\hbar$.")
e('H','H20','book/readers-guide.md',77,r"the gap equation deriving $\hbar$",r"the gap equation relating $\hbar$ to the discreteness scale")
e('H','H21','book/appendix-b-derivations.md',16,r"The framework derives Planck's constant $\hbar$ from a thermal self-consistency argument",r"The framework relates Planck's constant $\hbar$ to the discreteness scale through a thermal self-consistency argument")
e('H','H22','book/appendix-b-derivations.md',173,r"The framework derives Planck's constant $\hbar$ as the unique self-consistent value matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory.",
 r"The framework derives the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ between Planck's constant and the discreteness scale by matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory, conditional on H-slope with the horizon and frame conditions of Chapter 7 §7.3; with $\epsilon$ not independently known, it fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ (Chapter 7 §7.4), not the value of $\hbar$.")
e('H','H23','book/appendix-b-derivations.md',211,r"with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import.",
 r"with $\hbar$ unknown. The periodicity holds under the H-Hawking conditions and the KMS identification requires the emergent state to belong to that class (H-spectrum), so the matching below is a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).")
e('H','H24','book/appendix-b-derivations.md',471,r"B.4 establishes the gap equation determining $\hbar$ from horizon thermodynamics",r"B.4 establishes the gap equation relating $\hbar$ to the discreteness scale through horizon thermodynamics")
e('H','H25','book/appendix-c-objections.md',20,r"the gap equation deriving $\hbar$)",r"the gap equation for $\hbar$)")
e('H','H26','book/appendix-c-objections.md',236,r"## C.10 Circularity concerns: the gap equation deriving $\hbar$",r"## C.10 Circularity concerns: the gap equation for $\hbar$")
e('H','H27','book/appendix-c-objections.md',238,r"the framework's gap equation in Chapter 7 §7.4, which derives the Planck constant $\hbar$ from the cosmological horizon's geometric properties.",r"the framework's gap equation in Chapter 7 §7.3, which relates the Planck constant $\hbar$ to the discreteness scale through the cosmological horizon's thermodynamics.")
e('H','H28','book/appendix-c-objections.md',242,r"The logical chain in Chapter 7 §7.4",r"The logical chain in Chapter 7 §7.3")
e('H','H29','book/appendix-c-objections.md',257,r"- Classical-temperature matching → $\hbar$ fixed.",r"- Classical-temperature matching → $\hbar$ fixed in terms of $\epsilon$ (conditional on H-slope, Chapter 7 §7.3).")
e('H','H30','book/appendix-c-objections.md',263,r"The framework's derivation of $\hbar$ is therefore consistent",r"The gap equation is therefore consistent")
e('H','H31','book/README.md',64,r"the framework's $\hbar$ derivation from thermal self-consistency at the cosmological horizon",r"the framework's action-scale relation for $\hbar$ from thermal self-consistency at the cosmological horizon")
e('H','H32','papers/GR.md',18,r"— the value of $\hbar$, the Bekenstein-Hawking area law,",r"— the origin of the action scale $\hbar$, the Bekenstein-Hawking area law,")
e('H','H33','papers/GR.md',170,r"Step 4 will fix its value via thermal matching.",r"Step 4 will fix it in terms of $\epsilon$ via thermal matching.")
e('H','H34','papers/GR.md',336,r"The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, the Type II RVM form of the dark energy) depend on",r"The framework's Part II results (the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, $S_{\text{dS}}$, the Type II RVM reading of the dark energy) depend on")
e('H','H35','papers/Main.md',684,r"the framework derives $\hbar$ and the Bekenstein–Hawking coefficient downstream, and the derived bound",r"the framework relates $\hbar$ to the discreteness scale and recovers the Bekenstein–Hawking coefficient downstream, as consistency relations of its horizon calibration [GR §3–§5], and the derived bound")
e('H','H36','papers/SM.md',1350,r"including the derivation of $\hbar$, the Bekenstein-Hawking area law, the dissolution of the cosmological constant problem,",r"including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking area law, the conditional dissolution of the cosmological constant problem ([GR §6.2]),")
e('H','H37','papers/SM.md',1576,r"including the derivation of $\hbar$ from the cosmological horizon and the Bekenstein-Hawking area law including the $1/4$ coefficient (both conditional on the horizon conditions recorded there)",r"including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking area law with its $1/4$ coefficient (consistency relations, both conditional on the horizon conditions recorded there)")
e('H','H38','papers/SM.md',1378,r", ℏ = c³ε²/(4G), the Bekenstein-Hawking formula, and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems.",
 r", and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems on the branch stated in §1 (Tier 2), with the conditions marked at each entry. The horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking coefficient it matches hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5]).")
e('H','H39','papers/Substratum.md',22,r"the framework determines $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, for an entropy $\sigma$ per boundary mode, the Bekenstein-Hawking entropy with the $1/4$ coefficient, and the dissolution of the cosmological constant problem.",
 r"the framework relates the action scale to the discreteness scale through the calibration $\hbar = c^3 \epsilon^2 / (4G\sigma)$, which fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ for an entropy $\sigma$ per boundary mode, and recovers the Bekenstein-Hawking entropy with the $1/4$ coefficient as a consistency relation of that calibration, both conditional on H-slope [GR §3.2], and proposes a dissolution of the cosmological constant problem conditional on the covariant coupling step [GR §6.2].")
e('H','H40','papers/Substratum.md',178,r"**Output:** The emergent value of $\hbar$ is $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]).",
 r"**Output:** The emergent action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$, equivalently $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]); it fixes only $\epsilon/\sqrt{\sigma}$, not the value of $\hbar$ ([GR §4]).")
e('H','H41','papers/Substratum.md',180,r"detailed balance (consequence of $\varphi$ being a bijection). No new structural assumptions beyond Stages 1–2.",
 r"and the infrared detailed-balance condition H-slope with the horizon and frame conditions ([GR §2, §3.2, §8.5]), which does not follow from $\varphi$ being a bijection ([GR §3.2]) and is an assumption beyond Stages 1–2.")
e('H','H42','papers/Explainer.md',411,r"The value of ℏ is determined by the partition geometry — which is what Section 5 derives.",r"The action scale ℏ is fixed by the partition geometry in terms of the discreteness scale — which is what Section 5 derives.")
e('H','H43','papers/Explainer.md',477,r"The gap equation relates one free geometric parameter (ε), at given σ, to one output (ℏ).",r"The gap equation, conditional on the infrared detailed-balance condition H-slope with the horizon and frame conditions [GR §3.2], relates one free geometric parameter (ε), at given σ, to one output (ℏ).")
e('H','H44','papers/Explainer.md',662,r"It makes quantitative predictions — the value of ℏ and dark energy evolution — that interpretations do not, and it accounts for",r"It relates ℏ to the discreteness scale and carries a running-vacuum reading of dark energy whose falsifiable content is the Type II channel ([GR §7.1]) — content that interpretations do not have — and it accounts for")
e('H','H45','papers/Explainer.md',992,r"which derives ℏ, the Bekenstein-Hawking area law, and dark-sector phenomenology",r"which relates ℏ to the discreteness scale, recovers the Bekenstein-Hawking area law, and develops dark-sector phenomenology")
# ---------------- N-T: θ0 figures and labels
e('T','T1','papers/SM.md',14,r"the Koide angle $\theta_0 = 2/9$ to $0.02\%$",r"the Koide angle $\theta_0 = 2/9$ to $0.001\%$")
e('T','T2a','papers/SM.md',928,r"misses the observed $0.2227$ by a factor of four",r"misses the observed $0.2222$ by a factor of four")
e('T','T2b','papers/SM.md',928,r"The empirical match at $0.02\%$ does not",r"The empirical match at $0.001\%$ does not")
e('T','T3','papers/SM.md',934,r"(observed $0.2227$)",r"(observed $0.222225$)")
e('T','T4','papers/SM.md',1318,r"| Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.2222 | 0.2222 | 0.02% |",r"| Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.22222 | 0.222225 | 0.001% |")
e('T','T5','papers/SM.md',1329,r"$\theta_0$ at $0.02\%$)",r"$\theta_0$ at $0.001\%$)")
e('T','T6','papers/SM.md',1572,r"the Koide angle from the cubic-group quadratic Casimir to $0.02\%$",r"the Koide angle from the cubic-group quadratic Casimir to $0.001\%$")
e('T','T7','papers/Juno.md',401,r"Koide θ₀ (0.02%)",r"Koide θ₀ (0.001%)")
e('T','T8','papers/Substratum.md',446,r"(0.02%)",r"(0.001%)")
e('T','T9','book/README.md',62,r"Koide $\theta_0 = 2/9$ at $0.02\%$",r"Koide $\theta_0 = 2/9$ at $0.001\%$")
e('T','T10','book/ch05-gauge-structure.md',196,r"the Koide relation $2/9$ matched to $0.02\%$",r"the Koide angle $\theta_0 = 2/9$ matched to $0.001\%$")
e('T','T11',CH6,171,r"which is the angular form of the $Q = 2/3$ relation under the standard $\mathbb{Z}_3$-symmetric parametrization of three masses by an angle. The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222220$ at $0.02\%$",
 r"which is the phase of the standard $\mathbb{Z}_3$-symmetric parametrization of three masses, independent of the amplitude that $Q = 2/3$ fixes (SM §7.2). The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222225 \pm 0.000006$ at $0.001\%$ ($0.4\sigma$)")
e('T','T12',CH6,303,r"| $2/9$ | $0.22222$ | $0.02\%$ |",r"| $2/9$ | $0.222225$ | $0.001\%$ |")
for i,n in (('T13',68),('T14',177),('T15',210)):
    e('T',i,'book/ch08-juno.md',n,r"the Koide angle at $0.02\%$",r"the Koide angle at $0.001\%$")
e('T','T16','book/ch03-structural-realism.md',42,r"the Koide relation $2/9$",r"the Koide angle $2/9$")
e('T','T17','book/ch03-structural-realism.md',118,r"the Koide relation as $2/9$",r"the Koide angle as $2/9$")
e('T','T18','book/appendix-a-prediction-status.md',80,r"| C | 1 | Within 1% | Ch 6 §6.5 |",r"| C | 1 | 0.001% | Ch 6 §6.5 |")
# ---------------- N-M: stale m_tau mass rows
e('M','M1','papers/SM.md',1269,r"| 0.51096 MeV | 0.51100 MeV | 0.007% |",r"| 0.51098 MeV | 0.51100 MeV | 0.003% |")
e('M','M2','papers/SM.md',1270,r"| 105.652 MeV | 105.658 MeV | 0.006% |",r"| 105.656 MeV | 105.658 MeV | 0.002% |")
e('M','M3',CH6,12,r"$\theta_0 = 2/9$ — at $0.007\%$.",r"$\theta_0 = 2/9$ — at $0.003\%$.")
e('M','M4a',CH6,181,r"(the tau mass $m_\tau = 1776.86$ MeV)",r"(the tau mass $m_\tau = 1776.93$ MeV)")
e('M','M4b',CH6,181,r"$m_e = 0.51096$ MeV and $m_\mu = 105.652$ MeV against $0.51100$ and $105.658$ observed ($0.007\%$ and $0.006\%$; SM §7.2)",r"$m_e = 0.51098$ MeV and $m_\mu = 105.656$ MeV against $0.51100$ and $105.658$ observed ($0.003\%$ and $0.002\%$; SM §7.2)")
e('M','M5',CH6,189,r"| $0.51096$ MeV | $0.5110$ | $0.007\%$ |",r"| $0.51098$ MeV | $0.51100$ | $0.003\%$ |")
e('M','M6',CH6,304,r"| $0.51096$ MeV | $0.51100$ MeV | $0.007\%$ |",r"| $0.51098$ MeV | $0.51100$ MeV | $0.003\%$ |")
e('M','M7',CH6,344,r"($m_e$ at $0.007\%$ and $m_\mu$ at $0.006\%$",r"($m_e$ at $0.003\%$ and $m_\mu$ at $0.002\%$")
# ---------------- O1
e('O1A','O1-1','papers/Substratum.md',182,r"([GR §3, Theorem])",r"([GR §3.2])")
e('O1A','O1-2','papers/Substratum.md',184,r"**Status:** Theorem.",r"**Status:** Conditional on H-slope with the horizon and frame conditions ([GR §3.2]).")
e('O1A','O1-3','papers/Substratum.md',192,r"and $\hbar=c^3\epsilon^2/(4G\sigma)$, with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.",r"and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope with the horizon and frame conditions of [GR §3.2], with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.")
e('O1A','O1-4','papers/Structure.md',47,r"and $\hbar=c^3\epsilon^2/(4G\sigma)$, $\sigma$ the entropy per boundary mode [GR §3.1].",r"and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope [GR §3.2], $\sigma$ the entropy per boundary mode [GR §3.1].")
e('O1A','O1-5','papers/Methodology.md',339,r"and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ tying Planck's constant",r"and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$, conditional on H-slope ([GR §3.2]), tying Planck's constant")
# ---------------- O2
e('O2a','O2a-1',CH6,320,r"Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These seven relations are tested through five empirical channels",
 r"Koide $Q = 2/3$, Koide $\theta_0 = 2/9$ (independent of $Q$: the amplitude and the phase of the same parametrization, SM §7.2), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These eight relations are tested through five empirical channels")
e('O2a','O2a-2',CH6,320,r"lepton-mass dynamics (Koide $Q$)",r"lepton-mass dynamics (Koide $Q$ and $\theta_0$)")
e('O2a','O2a-3',CH6,332,r"eight Category A rows representing seven independent relations (the Koide relation and its angle have separate rows)",r"eight Category A rows, one for each relation")
e('O2b','O2b-1',CH6,320,r"Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form)",r"the Koide entry — $Q = 2/3$ and $\theta_0 = 2/9$, two independent observables (amplitude and phase, SM §7.2) counted here as one relation")
e('O2b','O2b-2',CH6,332,r"representing seven independent relations (the Koide relation and its angle have separate rows)",r"representing seven relations (the Koide amplitude $Q$ and angle $\theta_0$, independent observables, are counted as one Koide relation with separate rows)")
# ---------------- O3
OLD71=r"| Level G4 (universality class) | $S = A/(4 l_p^2)$, CC dissolution, $\hbar$ from partition geometry, RVM form | structural ($1/4$ untested directly) |"
e('O3a','O3a-1',CH9,71,OLD71,r"| Level G4 (universality class) | $S = A/(4 l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ (consistency relations), CC dissolution (descriptive), RVM form | structural ($1/4$ untested directly) |")
e('O3b','O3b-1',CH9,71,OLD71,r"| Level G4 (universality class) | RVM reading (form shared by every smooth model) | non-discriminating; the consistency relations $S = A/(4l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ and the descriptive CC distinction are stated in Chapter 7 §7.10 |")
e('O3x','O3-76',CH9,76,r"with the strongest confirmations at the universality-class level and the open research program",r"with the universality-class level consistent with observation rather than sharply tested and the open research program")
# ---------------- O4
e('O4a','O4a-1','papers/SM.md',940,r"The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds the taste-structured part of an emergent mass-level dressing by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$.",
 r"The agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); a second-order lepton-Yukawa loop, of order $10^{-6}$, lies inside that interval for either sign, by a factor of about two, so the comparison is not decisive.")
e('O4a','O4a-2',CH6,179,r"constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies (SM §7.2).",
 r"constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, an interval that a lepton-Yukawa loop of order $10^{-6}$ lies inside for either sign, by a factor of about two (SM §7.2).")
e('O4c','O4c-1','papers/SM.md',940,r"The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds the taste-structured part of an emergent mass-level dressing by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$.",
 r"How tightly the observed $\theta_0$ bounds the taste-structured part of an emergent mass-level dressing, and whether a second-order lepton-Yukawa loop (of order $10^{-6}$) respects that bound, is not quantified here.")
e('O4c','O4c-2',CH6,179,r"constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies (SM §7.2).",
 r"constrains it, and whether a lepton-Yukawa loop respects that constraint is not quantified (SM §7.2).")
# ---------------- O5
e('O5a','O5a-1','book/ch04-methodology.md',134,r"(matched to $0.001\%$, the sharpest empirical agreement in the framework)",r"(matched to $0.001\%$)")
e('O5a','O5a-2',CH6,171,r" — the sharpest empirical agreement in the framework.",r".")
e('O5a','O5a-3','papers/Substratum.md',446,r"— the sharpest empirical match in the framework",r"— matched to observation")
e('O5a','O5a-4','papers/SM.md',1329,r"the two tightest (",r"two of the tightest (")
e('O5a','O5a-5','book/appendix-a-prediction-status.md',215,r"— the framework's sharpest individual empirical match.",r"— the framework's sharpest individual empirical match in relative precision.")
e('O5c','O5c-extra1',CH6,12,r", the sharpest empirical agreement in the framework,",r",")
e('O5c','O5c-extra2','book/appendix-a-prediction-status.md',215,r"**Sharpest single match.** Koide $Q = 2/3$ to better than 0.001% (entry 10) — the framework's sharpest individual empirical match.",r"**Koide match.** Koide $Q = 2/3$ to better than 0.001% (entry 10).")
e('O5c','O5c-extra3','book/appendix-a-prediction-status.md',98,r"— the sharpest framework prediction across all 23, matching",r"— matching")
# ---------------- O6
e('O6A','O6-i-1',CH6,190,r"| $m_\mu$ | Koide closure with $m_e$, $m_\tau$ | $105.74$ MeV | $105.66$ | $0.07\%$ |",r"| $m_\mu$ | Koide closure with the structural $m_e/m_\tau = 1/(36\pi^4)$ and $m_\tau$ | $105.74$ MeV | $105.66$ | $0.08\%$ |")
e('O6A','O6-i-2',CH6,192,r"agrees with observation more tightly ($0.07\%$)",r"agrees with observation more tightly ($0.08\%$)")
e('O6A','O6-ii',CH6,305,r"| $m_\mu$ | Koide closure | $105.74$ MeV | $105.66$ MeV | $0.07\%$ |",r"| $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | $105.656$ MeV | $105.658$ MeV | $0.002\%$ |")
e('O6A','O6-iii-1',CH6,217,r"| Layer 1 | $0.51096$ MeV | $0.511$ | $0.007\%$ |",r"| Layer 1 | $0.505$ MeV | $0.511$ | $1.2\%$ |")
e('O6A','O6-iii-2',CH6,218,r"| $m_\mu$ | Koide closure | Layer 1 | $105.74$ MeV | $105.66$ | $0.07\%$ |",r"| $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | Layer 1 | $104.4$ MeV | $105.66$ | $1.2\%$ |")
e('O6B','O6B-i-1',CH6,190,r"| $m_\mu$ | Koide closure with $m_e$, $m_\tau$ | $105.74$ MeV | $105.66$ | $0.07\%$ |",r"| $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | $105.656$ MeV | $105.658$ | $0.002\%$ |")
e('O6B','O6B-i-2',CH6,192,r"The implied $m_\mu/m_\tau = 0.0595$ from Koide closure agrees with observation more tightly ($0.07\%$) than the $m_e/m_\tau$ structural relation itself ($0.84\%$) — the pattern is consistent with electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, where the larger $m_\tau$ Yukawa receives proportionally smaller logarithmic corrections than the small $m_e$ Yukawa.",r"The $m_e/m_\tau$ structural relation itself lies at $0.84\%$.")
# ---------------- O7
e('O7a','O7a-1','book/ch00-introduction.md',77,r"the observed value is $0.666661 \pm 0.000007$, a match to better than $0.001\%$ ($0.8\sigma$)",r"the observed value is $0.666664 \pm 0.000005$, a match to better than $0.001\%$ ($0.4\sigma$)")
e('O7a','O7a-2','book/glossary.md',97,r"Observed value $Q = 0.666661 \pm 0.000007$.",r"Observed value $Q = 0.666664 \pm 0.000005$.")
e('O7a','O7a-3','book/glossary.md',97,r"the match is better than $0.001\%$ ($0.8\sigma$)",r"the match is better than $0.001\%$ ($0.4\sigma$)")
e('O7a','O7a-4','papers/SM.md',1267,r"| 0.66667 | 0.66666 | $< 0.01\%$ |",r"| 0.66667 | 0.666664 | $0.0003\%$ |")
e('O7a','O7a-5',CH6,302,r"| $2/3$ | $0.66667$ | $0.001\%$ |",r"| $2/3$ | $0.666664$ | $0.0003\%$ |")
e('O7a','O7a-6',CH6,12,r"matched to $0.001\%$",r"matched to $0.0003\%$")
e('O5a','O5a-6',CH6,12,r", the sharpest empirical agreement in the framework,",r", the sharpest empirical agreement in the framework in relative precision,")
e('O5a','O5a-7','book/appendix-a-prediction-status.md',98,r"— the sharpest framework prediction across all 23,",r"— the sharpest framework prediction across all 23 in relative precision,")

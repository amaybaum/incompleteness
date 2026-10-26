import sys, json, collections
WT = sys.argv[1]
sys.path.insert(0, WT + '/verification/audits/manuscript/hbar-theta0-20261026/decisions')
from entries import E
REC = {'O1A','O2a','O3b','O3x','O4a','O5a','O6A','O7a'}
CH6='book/ch06-matter-content.md'
# Qualification adjustments (owner qualifications to O4-a and O6-A): override NEW text
OVR = {
 'O4a-1': r"In this linear-response model, with $\kappa \approx -35$ and $\lambda_E/\lambda_{A_1} = 0.22$–$0.24$, the agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); the interval is conditional on that response model, its sensitivity coefficient and the range of $\lambda_E/\lambda_{A_1}$, and is not a model-independent exclusion. A second-order lepton-Yukawa loop, of order $10^{-6}$, is compatible with the interval for either sign, by a factor of about two; the comparison is not decisive, and the loop estimate is not a confirmed prediction.",
 'O4a-2': r"constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, conditional on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above) rather than as a model-independent exclusion; a lepton-Yukawa loop of order $10^{-6}$ is compatible with that interval for either sign, by a factor of about two, but is not a confirmed prediction (SM §7.2).",
}
# Additional edits: qualification adjustment (O6 RG reading) and residue found by the re-grep
ADD = [
 ('Q6','Q6-rg',CH6,192, r"— the pattern is consistent with electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, where the larger $m_\tau$ Yukawa receives proportionally smaller logarithmic corrections than the small $m_e$ Yukawa.",
   r"— one possible explanation of the pattern is electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, in which the larger $m_\tau$ Yukawa would receive proportionally smaller logarithmic corrections than the small $m_e$ Yukawa; the agreement of the mass ratios does not by itself establish that running."),
 ('R','R1',CH6,179, r"the empirical match at $0.02\%$ confirms", r"the empirical match at $0.001\%$ confirms"),
 ('R','R2','book/ch07-gravity.md',8, r"with the measured comparisons spanning $0.02\%$ to $1.2\%$", r"with the measured comparisons spanning $0.0003\%$ to $1.2\%$"),
]
sel = [(g,i,f,n,o,OVR.get(i,nw)) for g,i,f,n,o,nw in E if g in ('H','T','M') or g in REC] + ADD
FULLp = WT + '/book/The-Incompleteness-of-Observation-FULL.md'
F = open(FULLp, encoding='utf-8').read().split('\n')
cache = {}
def lines(f):
    if f not in cache: cache[f] = open(WT+'/'+f, encoding='utf-8').read().split('\n')
    return cache[f]
# pre-compute FULL line for each (f,n) from ORIGINAL text
fullmap = {}
for g,i,f,n,o,nw in sel:
    if f.startswith('book/') and f != 'book/README.md' and (f,n) not in fullmap:
        L = lines(f)[n-1]
        m = [k for k,x in enumerate(F) if x == L]
        assert len(m) == 1, (i, f, n, m)
        fullmap[(f,n)] = m[0]
rec = []
for g,i,f,n,o,nw in sel:
    L = lines(f)
    assert L[n-1].count(o) == 1, (i, f, n, L[n-1].count(o))
    L[n-1] = L[n-1].replace(o, nw)
    fl = ''
    if (f,n) in fullmap:
        k = fullmap[(f,n)]; assert F[k].count(o) == 1, (i, 'FULL'); F[k] = F[k].replace(o, nw); fl = str(k+1)
    rec.append(dict(id=i, group=g, file=f, line=n, full=fl, old=o, new=nw))
for f,L in cache.items():
    open(WT+'/'+f, 'w', encoding='utf-8').write('\n'.join(L))
open(FULLp, 'w', encoding='utf-8').write('\n'.join(F))
for f,L in cache.items():
    if f.startswith('book/') and f != 'book/README.md':
        for (ff,n),k in fullmap.items():
            if ff == f: assert F[k] == L[n-1], (f, n)
json.dump(rec, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('applied', len(rec), 'edits;', collections.Counter(r['group'] for r in rec))

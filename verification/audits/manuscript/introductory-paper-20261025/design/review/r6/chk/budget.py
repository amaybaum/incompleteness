import re,sys
r4=open(sys.argv[1],encoding='utf-8').read().split('\n')
out=open(sys.argv[2],encoding='utf-8').read().split('\n')
def w(s): s=re.sub(r'<!--.*?-->','',s); return len(s.split())
def L(a,b=None): b=b or a; return sum(w(r4[i-1]) for i in range(a,b+1))
def sents(n): return re.split(r'(?<=[.!?])\s+(?=[A-Z(*$\\])', re.sub(r'<!--.*?-->','',r4[n-1]).strip())
def S(n,idx): ss=sents(n); return sum(len(ss[i].split()) for i in idx if i<len(ss))
def q(a,b): # quoted block lines '>' in OUTLINE-r6 lines a..b
    return sum(len(re.sub(r'^\s*>\s?','',l).split()) for l in out[a-1:b] if l.strip().startswith('>'))
print("r4:12 sentences:",[len(s.split()) for s in sents(12)])
abs_=S(12,[0,1,2,4])+8+S(12,[5,6])+q(130,132)+q(135,137)
print("Abstract",abs_)
s1=L(20,26)+ (w(r4[29])-len(sents(30)[-1].split())) + q(152,154) + q(157,161) + (w(r4[31])-S(32,[0,1,2])) + L(34)
print("S1",s1, " (r4:32 tail", w(r4[31])-S(32,[0,1,2]),")")
# S2: r4:40-64, 70-72, 74-80, 82-90, 92 first two sents, 94 replaced by S-4, 96, 98, 108, 110, 112 s3-4, 114 s1 + last + S-5, S-1, S-2, N-LIT1, pointer
s1t="For S_K⊆D_K the realization stores a sampled trajectory, with a clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]. A realization whose hidden prior is independent of x_0 also exists [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper, with exact probes."
s2t="For D_K⊆Q_K the representation is the permutation unitary U_φ|x,h⟩=|φ(x,h)⟩, read out in the configuration basis at every step [Main §3.4]; Q_K⊆S_K is the Born rule."
s4t="Corollary (proved on paper [Main §1.5]). M_t>0 holds exactly when every faithful realization carries readout-relevant hidden memory at t, that is, a pair of posteriors with different pushforwards. The forward direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which Theorem 1 supplies (S_imp_D); both use the standard vanishing criterion for conditional mutual information [CT06], which, like the time-t identification, is not machine-checked."
s5t="On a fixed finite reversible substratum, history readback forces indivisibility somewhere in the recurrence cycle [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]."
s2=L(40,64)+L(70,72)+L(74,80)+L(82,90)+S(92,[0,1])+L(96)+L(98)+L(108)+L(110)+S(112,[2,3])+S(114,[0])+len(sents(114)[-1].split())+sum(len(x.split()) for x in (s1t,s2t,s4t,s5t))+q(203,204)+q(211,212)+6
print("S2",s2, " last s of 114:",len(sents(114)[-1].split()))
s3=L(118,122)+L(210,230)+25+ (w(r4[233])*0.6)
print("S3",round(s3)," (r4:234 total",w(r4[233]),")")
s4=q(249,302)
print("S4 quoted",s4,"+ N-LIT2 ~70 =",s4+70)
s5=S(172,[0,1,2,4])+q(326,335)+12+ (len(sents(181)[-2].split())+len(sents(181)[-1].split()))+q(341,362)
print("S5",s5)
s6=q(390,393)+L(238,240)+q(404,409)+L(242,243)+25+q(418,419)+q(423,428)+40+80
print("S6 (items1-3,5,6 verbatim + new + r4 6.4(1)-(4) not counted)",s6)
tot=abs_+s1+s2+s3+s4+70+s5+s6
print("TOTAL",round(tot), "pp at 395:",round(tot/395,2))
rem = L(66)+L(68)+len(sents(92)[2].split())+L(94)+S(112,[0,1])+ (L(114)-S(114,[0])-len(sents(114)[-1].split()))
add = sum(len(x.split()) for x in (s1t,s2t,s4t,s5t))
print("sketch words removed",rem,"added",add,"net saving",rem-add)
print("r4 S2-equivalent (40-100 + 106-114):",L(40,100)+L(106,114))

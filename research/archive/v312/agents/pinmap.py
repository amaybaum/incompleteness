import re,json,sys
def locate(path, phrases):
    lines=open(path,encoding='utf-8').read().split('\n')
    # build flattened text with char->line map
    flat=[];lm=[]
    for i,l in enumerate(lines,1):
        toks=l.split()
        for t in toks:
            if flat: flat.append(' '); lm.append(i)
            for ch in t: flat.append(ch); lm.append(i)
    f=''.join(flat)
    out=[]
    for ph,guardline,kind in phrases:
        p=' '.join(ph.split())
        idx=f.find(p)
        cnt=f.count(p)
        if idx<0: out.append((ph,guardline,kind,None,None,0))
        else: out.append((ph,guardline,kind,lm[idx],lm[idx+len(p)-1],cnt))
    return out
agents=[
 ('## §A.35 Registry contract for the Lean-to-manuscript census',2933,'required (R7-MSP)'),
 ('updates the registry in the same commit',2934,'required (R7-MSP)'),
 ("### Sealing through the manifest, from `SI-2`'s landing",30664,'required (R7-SI2 SI2-7, unflattened)'),
 ("writes **the round's own manifest record**",30665,'required (R7-SI2 SI2-7)'),
 ('`sealed_head` = `E` and `merge` = `L`',30666,'required (R7-SI2 SI2-7)'),
 ('It writes **no legacy constant**',30667,'required (R7-SI2 SI2-7)'),
 ('How a new `sealed` record is created',30668,'required (R7-SI2 SI2-7)'),
 ("How a completed non-sealing round's `base-only` record is created",30669,'required (R7-SI2 SI2-7)'),
 ('**cease to GATE**',30670,'required (R7-SI2 SI2-7; mutation at 30973)'),
 ('has recreated the representation `SI-2` retired',30671,'required (R7-SI2 SI2-7)'),
 ('**PROTECTED HISTORICAL SEAL STATE**',30672,'required (R7-SI2 SI2-7; mutation at 30974)'),
 ('makes the round that does it *sealing*',30673,'required (R7-SI2 SI2-7)'),
 ('**The retirement round is sealing.**',30674,'required (R7-SI2 SI2-7)'),
 ('`sealed_head` = its `E`, `merge` = its `L` — and writes no legacy constant',30675,'required (R7-SI2 SI2-7)'),
 ("governs **rounds begun after `SI-2`'s landing merge**",30676,'required (R7-SI2 SI2-7)'),
 ('`P` sets the constants it owns to `E` and to `L`',30677,'forbidden (R7-SI2 SI2-7; mutation at 30975)'),
 ("### The representation retired, from `SI-3`'s landing",31366,'required (R7-SI3 SI3-6, unflattened)'),
 ('**The legacy representation is retired.**',31367,'required (R7-SI3 SI3-6; mutation at 31690)'),
 ('**zero legacy assignment statements in the file**',31368,'required (R7-SI3 SI3-6)'),
 ('has recreated the representation that was retired',31369,'required (R7-SI3 SI3-6)'),
 ('**manifest accessor**',31370,'required (R7-SI3 SI3-6)'),
 ('**prospective declaration**',31371,'required (R7-SI3 SI3-6)'),
 ('**`P` removes the entry when it writes the record**',31372,'required (R7-SI3 SI3-6)'),
 ('**declared baseline**',31373,'required (R7-SI3 SI3-6)'),
 ("**A closed round's contracts are read over the records it manifested.**",31374,'required (R7-SI3 SI3-6; mutation at 31691)'),
 ('**The censuses are history.**',31375,'required (R7-SI3 SI3-6)'),
 ('never read as evidence about a later head',31376,'required (R7-SI3 SI3-6)'),
 ("both of which held until `SI-3`'s landing",31377,'required (R7-SI3 SI3-6)'),
 ('remained **PROTECTED HISTORICAL SEAL STATE**',31378,'required (R7-SI3 SI3-6; mutation at 31688)'),
 ('remain **PROTECTED HISTORICAL SEAL STATE**',31379,'forbidden (R7-SI3 SI3-6)'),
]
readme=[
 ('Guard `R7-INV`',2759,'required (R7-INV, _rd1)'),
 ('Guard `R7-MIN`',2865,'required (R7-MIN, _rd1)'),
 ('Guard `R7-A6P`',16410,'required in A6P paragraph (R7-A6P P9); mutation at 16542'),
 ('preregistration blob `e7cb701`, committed alone as `d24dc3c`',16406,'required in A6P paragraph (R7-A6P P9)'),
 ('The substratum A6 covariance propagation (`audits/foundations/',16291,'A6P paragraph start anchor'),
 ('`.github/workflows/verify.yml` runs',16292,'A6P/A6I paragraph END anchor (also 18787)'),
 ('The substratum A6 instantiation round 2 (`programmes/substratum/a6-instantiation/`',18785,'A6I paragraph start anchor'),
 ('preregistration blob `6f991c1`, merged alone by PR #623 as `3e5d6a8`, the mandated execution base',19110,'required in A6I paragraph (R7-A6I I23)'),
 ('Guard `R7-A6I`',19119,'required in A6I paragraph (R7-A6I I23)'),
 ('is a definition round, not a proof round, and is owner-called',19125,'required (R7-A6I I23)'),
 ('Guard `R7-WTS` pins the preregistration blob by content',16947,'required (R7-WTS W24)'),
 ('which is a propagation round of its own',3388,'required (R7-RB1 loop)'),
 ('owner decision',3777,'required (R7-SUB loop)'),
 ('third preregistered outcome',3777,'required (R7-SUB loop)'),
 ('preregistered at level two',4189,'required (R7-FLOW loop)'),
 ('realization by one protocol',4395,'required (R7-PROP loop)'),
 ('that the preregistered Q3 or Q4 holds as stated',3631,'required (R7-LIFT loop)'),
]
json.dump({'agents':locate('AGENTS.md',agents),'readme':locate('verification/README.md',readme)},open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
for k in ('agents','readme'):
    for r in json.load(open(sys.argv[1]))[k]: print(k,r[1],r[3],r[4],r[5],r[0][:70])

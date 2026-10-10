import json, re, sys
d = json.load(open('decls.json'))['decls']
files = {
 'Defs': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyDefs.lean',
          ['CompositeDimension','K2Guard']),
 'Parity': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyParity.lean',
          ['CompositeDimension','K2Guard','EffectSpace','KInfFoundations','TransitiveBody']),
 'Package': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyPackage.lean',
          ['CompositeDimension','K2Guard','EffectSpace','KInfFoundations','TransitiveBody','CompositeInterface','OrbitNormalization']),
}
newdecls = set()
for k,(p,_) in files.items():
    for line in open(p):
        m = re.match(r'^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(def|theorem|lemma|abbrev|structure|inductive)\s+([^\s:(\[{]+)', line)
        if m: newdecls.add(m.group(2))
for k,(p,opens) in files.items():
    src = open(p).read()
    src = re.sub(r'/-.*?-/', '', src, flags=re.S)
    src = re.sub(r'--.*', '', src)
    toks = set(re.findall(r'(?<![\w.\'])([A-Za-z_][\w\'₀-₉]*(?:\.[A-Za-z_][\w\'₀-₉]*)*)', src))
    for t in sorted(toks):
        cands = []
        # namespace-priority candidates
        for pre in ['OIBridge.FourCopy.', 'OIBridge.']:
            if pre+t in d: cands.append(('NS', pre+t))
        if t in newdecls or t.split('.')[0] in newdecls: 
            continue
        oc = []
        for o in opens:
            if 'OIBridge.'+o+'.'+t in d: oc.append('OIBridge.'+o+'.'+t)
        if cands or len(oc) > 1:
            print(k, t, cands, oc)

import json, re
d = json.load(open('decls.json'))['decls']
files = {
 'Defs': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyDefs.lean',
          ['CompositeDimension','K2Guard']),
 'Parity': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyParity.lean',
          ['CompositeDimension','K2Guard','EffectSpace','KInfFoundations','TransitiveBody']),
 'Package': ('/home/user/incompleteness/verification/lean-mathlib/OIBridge/FourCopyPackage.lean',
          ['CompositeDimension','K2Guard','EffectSpace','KInfFoundations','TransitiveBody','CompositeInterface','OrbitNormalization']),
}
allres = set()
for k,(p,opens) in files.items():
    src = open(p).read()
    src = re.sub(r'/-.*?-/', '', src, flags=re.S)
    src = re.sub(r'--.*', '', src)
    toks = set(re.findall(r'(?<![\w.\'])([A-Za-z_][\w\'₀-₉]*(?:\.[A-Za-z_][\w\'₀-₉]*)*)', src))
    for t in sorted(toks):
        oc = [o for o in opens if 'OIBridge.'+o+'.'+t in d]
        if oc:
            allres.add(t)
print(' '.join(sorted(allres)))

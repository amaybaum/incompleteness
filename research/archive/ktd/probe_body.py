import io, json, re, subprocess, sys, os
H=os.path.dirname(os.path.abspath(__file__))
src=open(H+'/helpers.py').read()+'\n'+open(H+'/body.py').read()
ns={'D':'06b6f94e479bc19a28979c72316823cbdd0fb62b','LEAN':'verification/lean-mathlib/OIBridge/',
    'DECL':re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)', re.M),
    'CTX':re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$', re.M),
    'FAILS':[], 'COUNT':[0], 'PRINTS':[], 'N_PRINTS':0, 'TEXTS':{}, 'DECLS':[], 'PREAMBLE':'', 'CONTEXT':[]}
exec('import io,json,re,subprocess,sys\n'+src, ns)
mod=open(sys.argv[1],encoding='utf-8').read()
landed=ns['landed_at_d']()
for k,v in landed.items(): print('L',k,'|',v[:150])
print(ns['verdicts'](mod,landed))
for d,(m,l) in ns['PAIRS'].items():
    print(d, ns['pair_ok'](mod,landed,d,l))
inv=ns['d_inventory_files']()
names,spaces=ns['inventory'](inv+[mod])
print(len(names), sorted(spaces))
for d,(m,l) in ns['PAIRS'].items():
    lt=[t for t in inv if ('\nnamespace %s\n'%m) in t]
    print(d, len(lt), ns['resolution_bad'](mod,d,lt[0],l,names,spaces), sorted(set(ns['strip_binders'](ns['effective'](mod,d)))))
print('--- resolution non-vacuity')
d='three_of_nativeGateOf_dense'; m,l=ns['PAIRS'][d]
dsc=ns['scopes_at'](mod)[d]; lt=[t for t in inv if ('\nnamespace %s\n'%m) in t][0]; lsc=ns['scopes_at'](lt)[l]
dv=ns['visible'](dsc[1],dsc[2],spaces); lv=ns['visible'](lsc[1],lsc[2],spaces)
print(dv); print(lv)
for t in sorted(set(ns['strip_binders'](ns['effective'](mod,d)))): print(t, ns['resolve'](t,dv,names), ns['resolve'](t,lv,names))
print('--- S6 clashes')
others=ns['inventory'](inv)[0]
for k,n in ns['decls'](mod):
    sc=ns['scopes_at'](mod)[n]; h=ns['resolve'](n, ns['visible'](sc[1],sc[2],spaces), others)
    if h: print('CLASH',n,h)
print('--- def effective', ns['effective'](mod,'DenseBoundaryOrbit'))

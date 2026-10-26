import re,sys,glob
src=sys.argv[1]
def norm(s): return re.sub(r'\s+|\\,|\;|\\!|\\left|\\right','',s)
corpus=''.join(norm(open(f).read()) for f in glob.glob(src+'/book/*.md')+glob.glob(src+'/papers/*.md') if not f.endswith('Explainer.md'))
txt=open(src+'/Explainer.md').read()
for m in re.finditer(r'\$\$(.+?)\$\$',txt,re.S):
    ln=txt[:m.start()].count('\n')+1
    e=norm(m.group(1))
    print(ln, 'FOUND' if e in corpus else 'notfound', m.group(1).strip()[:90].replace('\n',' '))

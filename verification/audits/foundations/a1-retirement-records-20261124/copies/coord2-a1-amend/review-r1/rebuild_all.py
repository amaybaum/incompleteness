# Reviewer's rebuild: H + P's ledger splices for ALL ledgered files, compared to T1' blobs; GR.md:58 provenance.
import sys, json, subprocess, hashlib
REPO=sys.argv[1]; H='53c6601a10419b6b333cc992474272501ab542af'; P='4c79be642ca631573f06b444903be75ec4f5e2b6'; T='14ac71b4b0a0c0aa2d7068d6799a73f474097060'
def show(c,p):
    r=subprocess.run(['git','-C',REPO,'show','%s:%s'%(c,p)],capture_output=True); return r.stdout if r.returncode==0 else None
def bid(b): return hashlib.sha1(b'blob %d\0'%len(b)+b).hexdigest()
led=json.loads(show(P,'verification/audits/foundations/a1exit-deletion-20261121/ledger.json'))
assert led['base']==H, led['base']
sp=led['splices']; files=sorted({s['file'] for s in sp}); print('splices',len(sp),'files',len(files))
neq=0; gr=None
for f in files:
    h=show(H,f); b=bytearray(h)
    ss=sorted([s for s in sp if s['file']==f], key=lambda s:s['start'], reverse=True)
    prev=None
    for s in ss:
        assert prev is None or s['end']<=prev, ('overlap',f)
        prev=s['start']
        assert hashlib.sha256(h[s['start']:s['end']]).hexdigest()==s['old_sha256'], s['id']
        new=s['new'].encode(); assert hashlib.sha256(new).hexdigest()==s['new_sha256']
        b[s['start']:s['end']]=new
    b=bytes(b); t=show(T,f)
    eq = (b==t)
    if not eq: neq+=1; print("NOT EQUAL", f)
    if f in ('papers/GR.md','papers/SM.md','book/ch09-universality.md','book/ch19-open-problems.md','book/The-Incompleteness-of-Observation-FULL.md'):
        print(f, len(ss), bid(b), 'T1p', bid(t) if t else None, eq)
    if f=='papers/GR.md': gr=(h,b,[s for s in sp if s['file']==f])
print('files not equal to T1p:', neq)
# appendix-b
print('appendix-b H==T1p', show(H,'book/appendix-b-derivations.md')==show(T,'book/appendix-b-derivations.md'), bid(show(T,'book/appendix-b-derivations.md')))
h,b,gs=gr
L=b.split(b'\n')[57]; print('GR:58 rebuilt sha256', hashlib.sha256(L).hexdigest()[:16], L[:90])
off=sum(len(x)+1 for x in h.split(b'\n')[:57]); end=off+len(h.split(b'\n')[57])
print('splices touching H line 58:', [s['id'] for s in gs if s['start']<end and s['end']>=off])
print('H GR:58', h.split(b'\n')[57][:90])
# any T1' file outside the ledger that differs from H (trial adds record dir etc.)
d=subprocess.run(['git','-C',REPO,'diff','--name-only',H,T],capture_output=True,text=True).stdout.split()
print('H..T1p changed paths not in ledger:', [x for x in d if x not in files][:20], 'count', len([x for x in d if x not in files]))

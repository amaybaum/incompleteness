import sys, subprocess, base64, hashlib, struct
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
def obj(c): return subprocess.run(['git','-C',sys.argv[1],'cat-file','commit',c],capture_output=True,check=True).stdout
def split(raw):
    lines = raw.split(b'\n'); out=[]; sig=[]; i=0
    while i < len(lines):
        l = lines[i]
        if l.startswith(b'gpgsig '):
            sig.append(l[7:]); i+=1
            while lines[i].startswith(b' '): sig.append(lines[i][1:]); i+=1
            continue
        out.append(l); i+=1
    return b'\n'.join(out), b'\n'.join(sig)
def rd(b,o):
    n=struct.unpack('>I',b[o:o+4])[0]; return b[o+4:o+4+n], o+4+n
def verify(c):
    payload, arm = split(obj(c))
    blob = base64.b64decode(b''.join(l for l in arm.split(b'\n') if not l.startswith(b'-----')))
    assert blob[:6]==b'SSHSIG'; o=10
    pk,o=rd(blob,o); ns,o=rd(blob,o); res,o=rd(blob,o); ha,o=rd(blob,o); sg,o=rd(blob,o)
    t,p=rd(pk,0); key,_=rd(pk,p); st,p=rd(sg,0); s,_=rd(sg,p)
    h = hashlib.sha512(payload).digest() if ha==b'sha512' else hashlib.sha256(payload).digest()
    def S(x): return struct.pack('>I',len(x))+x
    data = b'SSHSIG'+S(ns)+S(res)+S(ha)+S(h)
    try: Ed25519PublicKey.from_public_bytes(key).verify(s,data); ok=True
    except Exception: ok=False
    return ok, t.decode(), ns.decode(), base64.b64encode(pk).decode()
for c in sys.argv[2:]:
    print(c[:12], verify(c))

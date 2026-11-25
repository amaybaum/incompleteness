import json,subprocess,sys,os
sys.path.insert(0,'../../write-safety')
from gate import Gate, Halted, FOOTER
class Gh:
    def request(self, method, path, payload):
        args=['gh','api','-i','-X',method,path]
        inp=None
        if payload is not None: args+=['--input','-']; inp=json.dumps(payload)
        r=subprocess.run(args,input=inp,capture_output=True,text=True)
        out=r.stdout
        head,_,body=out.partition('\r\n\r\n') if '\r\n\r\n' in out else out.partition('\n\n')
        status=int(head.split()[1]) if head.startswith('HTTP') else None
        if status is None: raise RuntimeError('no status line; rc=%d %s'%(r.returncode,r.stderr[:200]))
        return status,(json.loads(body) if body.strip() else None)
class NoGit:
    def run(self,a): raise RuntimeError('no git')
    def remote_sha(self,*a): raise RuntimeError('no git')
    def is_ancestor(self,*a): raise RuntimeError('no git')
V=sys.argv[1]
body=open(V+'/validation-body.md',encoding='utf-8').read()
reg={"issue.edit_body":{"validated":False,"send_form":"footer"}}
log=[]
g=Gate(Gh(),NoGit(),V+'/gate-run/HALT','amaybaum/incompleteness',reg,evidence_dir=V+'/gate-run',log=log)
g.grant_single_write("issue.edit_body",1548)
try:
    st=g.write("issue.edit_body",1548,{"body":body})
    open(V+'/gate-run/stored-body.md','w',encoding='utf-8',newline='').write(st['body'])
    print('VALIDATION PASS: stored body equals expected byte for byte; updated_at',st.get('updated_at'))
    rc=0
except Halted as e:
    print('HALTED:',e); rc=3
json.dump(log,open(V+'/gate-run/log.json','w'),indent=1)
sys.exit(rc)

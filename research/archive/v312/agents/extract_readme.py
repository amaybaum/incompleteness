import ast,re,json,sys
path='verification/lean/edge_rigidity_probe.py'
src=open(path).read()
tree=ast.parse(src)
RV={'_rd','_rd1','_A6P_README','_WTSREADME','_A6IREADME','rd','readme'}
# map names bound to tuples/lists of str constants (module-level & function-level, last binding wins per lineno)
binds={}
for n in ast.walk(tree):
    if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
        v=n.value
        if isinstance(v,(ast.Tuple,ast.List)) and all(isinstance(e,ast.Constant) and isinstance(e.value,str) for e in v.elts):
            binds.setdefault(n.targets[0].id,[]).append((n.lineno,[e.value for e in v.elts]))
parent={}
for p in ast.walk(tree):
    for c in ast.iter_child_nodes(p): parent[c]=p
def consts_of(node, at):
    if isinstance(node,ast.Constant) and isinstance(node.value,str): return [node.value]
    if isinstance(node,ast.JoinedStr): return None
    if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Add):
        a=consts_of(node.left,at); b=consts_of(node.right,at)
        if a and b and len(a)==1 and len(b)==1: return [a[0]+b[0]]
        return None
    if isinstance(node,ast.Name):
        # loop var
        p=node
        while p in parent:
            p=parent[p]
            if isinstance(p,(ast.For,ast.comprehension)) and isinstance(p.target,ast.Name) and p.target.id==node.id:
                it=p.iter
                if isinstance(it,(ast.Tuple,ast.List)):
                    out=[]
                    for e in it.elts:
                        r=consts_of(e,at)
                        if r: out+=r
                    return out
                if isinstance(it,ast.Name) and it.id in binds:
                    cands=[b for b in binds[it.id] if b[0]<=at] or binds[it.id]
                    return cands[-1][1]
                return None
        return None
    return None
def readme_name(n):
    if isinstance(n,ast.Name) and n.id in RV: return n.id
    return None
res=[]
for n in ast.walk(tree):
    if isinstance(n,ast.Compare) and len(n.ops)==1 and isinstance(n.ops[0],(ast.In,ast.NotIn)):
        v=readme_name(n.comparators[0])
        if v:
            cs=consts_of(n.left,n.lineno)
            res.append((n.lineno,v,'required' if isinstance(n.ops[0],ast.In) else 'forbidden',cs))
    if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='_asserted' and len(n.args)==2 and readme_name(n.args[0]):
        # likely inside 'not _asserted' -> forbidden
        cs=consts_of(n.args[1],n.lineno)
        res.append((n.lineno,n.args[0].id,'forbidden-asserted',cs))
    if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ('count','find','index') and readme_name(n.func.value):
        cs=consts_of(n.args[0],n.lineno) if n.args else None
        res.append((n.lineno,n.func.value.id,'count/find',cs))
json.dump(res,open(sys.argv[1],'w'),indent=0)
print(len(res), sum(1 for r in res if r[3] is None))

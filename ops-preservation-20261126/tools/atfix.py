import sys,hashlib
p=sys.argv[1]; b=open(p,encoding='utf-8').read()
n=b.count('@')
if n:
    assert b.count('"@"')==n, 'unexpected at sign form'
    b=b.replace('"@"','"[at sign]"')
    old="Redaction: no redaction."
    assert old in b
    b=b.replace(old,"Redaction: not verbatim in %d place%s: each quoted at-sign character is written as \"[at sign]\" (disclosed rewrite, as for the less-than/exclamation sequence); the SHA-256 below is of the original text, preserved byte for byte." % (n, '' if n==1 else 's'))
    open(p,'w',encoding='utf-8',newline='').write(b)
print('rewritten',n)

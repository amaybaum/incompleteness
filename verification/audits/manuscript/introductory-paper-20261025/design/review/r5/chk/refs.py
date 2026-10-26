import sys,glob,os
root=sys.argv[1]
def f(name):
    m={'GR':'papers/GR.md','Main':'papers/Main.md','SM':'papers/SM.md','Substratum':'papers/Substratum.md','Juno':'papers/Juno.md','Explainer':'papers/Explainer.md','FULL':'book/The-Incompleteness-of-Observation-FULL.md'}
    if name in m: return os.path.join(root,m[name])
    g=glob.glob(os.path.join(root,'book',name+'*.md')); return g[0] if g else None
checks=[('GR',366,'expects'),('GR',162,'alternative'),('GR',546,'2\\pi/8\\pi'),('GR',707,'mode counting'),('GR',567,'our universe'),('GR',711,'unique self-consistent'),('GR',709,'95'),('GR',601,'memory'),('GR',605,'Page'),('GR',611,'Page'),('GR',869,'Popescu'),('GR',164,'Jacobson'),('GR',358,'fit'),('GR',96,'first law'),('Main',666,'dissolves'),('SM',16,'forced'),('appendix-a',93,'24'),('appendix-a',95,'S'),('appendix-a',103,'scramble'),('appendix-a',110,'G4'),('appendix-a',113,'G7'),('appendix-a',116,'G11'),('appendix-a',119,'G14'),('appendix-a',121,'Summary'),('appendix-a',183,'F5'),('appendix-a',185,'F7'),('appendix-a',208,'echo'),('appendix-a',209,'phantom'),('appendix-a',229,'no current content'),('appendix-a',231,'S'),('ch07',12,'counting'),('ch07',14,'coupling'),('ch07',104,'derived structural'),('ch07',110,'resolves'),('ch07',143,'open'),('ch07',147,'Page'),('ch07',159,'falsif'),('ch07',161,'sharp prediction'),('ch07',167,'dissolves'),('ch07',195,'expect'),('ch07',201,'eliminates'),('ch07',260,'Q'),('ch18',114,'unpredict'),('ch18',146,'dissolution'),('ch18',148,'mass-independent'),('ch18',349,'Twenty-two'),('ch19',28,'seven'),('ch19',330,'Dissolved'),('ch19',333,'Measurement'),('ch19',334,'Resolved'),('ch19',336,'Hierarchy'),('ch19',339,'Dark'),('ch19',362,'preregistered'),('ch19',370,'ten'),('ch00',21,'postulate'),('ch00',81,'mode counting'),('ch00',89,'a_0'),('preface',7,'postulate'),('glossary',17,'postulate'),('glossary',113,'Page'),('ch02',192,'dissolves'),('Explainer',477,'alternative'),('Explainer',533,'dissolves'),('Explainer',549,'expect'),('ch09',108,'Page'),
('FULL',1889,'counting'),('FULL',1981,'derived structural'),('FULL',257,'postulate'),('FULL',78,'postulate'),('FULL',317,'mode counting'),('FULL',325,'a_0'),('FULL',6639,'postulate'),('FULL',5663,'G4'),('FULL',2044,'dissolves'),('FULL',835,'dissolves'),('FULL',5214,'Dissolved at the descriptive'),('FULL',5506,'Dissolved'),('FULL',2078,'eliminates'),('FULL',5666,'G7'),('FULL',5672,'G14'),('FULL',5509,'Measurement'),('FULL',5169,'Twenty-two'),('FULL',5538,'preregistered'),('FULL',5204,'seven'),('FULL',5515,'Dark'),('FULL',5512,'Hierarchy'),('FULL',5627,'Cabibbo'),('FULL',5248,'information preservation'),('FULL',1987,'resolves'),('FULL',4966,'dissolution'),('FULL',4968,'mass-independent'),('FULL',5510,'Resolved'),('FULL',4984,'echo'),('FULL',2026,'Page'),('FULL',1993,'Page'),('FULL',4976,'non-renormal'),('FULL',2007,'H-scramble'),('FULL',1891,'coupling')]
for doc,n,kw in checks:
    p=f(doc)
    if not p: print('NOFILE',doc); continue
    L=open(p,encoding='utf-8').read().split('\n')
    t=L[n-1] if n<=len(L) else ''
    ok=kw.lower() in t.lower()
    near=''
    if not ok:
        for d in range(1,6):
            for m in (n-d,n+d):
                if 0<m<=len(L) and kw.lower() in L[m-1].lower(): near=near or f'{m}'
    print(('OK  ' if ok else 'MISS'),f'{doc}:{n}',repr(kw),('near '+near if near else ''),'|',t[:110].replace('\n',' '))

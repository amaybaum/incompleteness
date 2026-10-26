import sys,re
f,pats=sys.argv[1],sys.argv[2:]
pages=open(f,encoding='utf-8',errors='replace').read().split('\f')
for p in pats:
    hits=[i+1 for i,pg in enumerate(pages) if p.replace(' ','') in re.sub(r'\s+','',pg)]
    # printed page number guess: last numeric-only line of page
    pr=[]
    for i in hits:
        nums=[l.strip() for l in pages[i-1].splitlines() if re.fullmatch(r'\s*\d{1,4}\s*',l)]
        heads=re.findall(r'(\d{2,4})\s*$',pages[i-1].splitlines()[0]) if pages[i-1].splitlines() else []
        pr.append((i,nums[-1:] ,pages[i-1].strip().splitlines()[0][:80]))
    print(p[:50],'->',pr)

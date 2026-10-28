from pathlib import Path
import fitz,json,hashlib,statistics,subprocess,re,argparse
from PIL import Image,ImageOps,ImageDraw

parser=argparse.ArgumentParser(description='Canonical OI publication statistics and selected-page render QA')
parser.add_argument('--root',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
ROOT=args.root.resolve()
OUT=args.output.resolve();OUT.mkdir(parents=True,exist_ok=True)
names=['Complexity','Computation','Explainer','GR','Juno','Methodology','SM','Structure','Substratum','book']
queries={
 'SM':['Theorem 3','Generic unitary stabilizer','Correlated central quotient','Fixed-family anomaly-free','Compact-charge strengthening','Faithful charged-family image'],
 'Structure':['Definition 9.1','Proposition 9.7b','Proposition 9.7c'],
 'Substratum':['Minimal linear word realizations','Passive finite-permutation predictive quotient','Triple identification'],
 'book':['Recovery from complete multi-time records','A constructive Standard Model quotient','Restricted chirality','On this selected charge branch','The cumulative chain retains'],
 'GR':['shell-orientation theorem']
}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
stats={};thumbs=[]
for name in names:
 base=ROOT/('book/The-Incompleteness-of-Observation-FULL' if name=='book' else 'papers/'+name)
 pdf=base.with_suffix('.pdf');md=base.with_suffix('.md');tex=base.with_suffix('.tex')
 stamp='% source-sha256: '+sha(md)
 assert stamp in tex.read_text(),('stale TeX',name)
 doc=fitz.open(pdf);text=[p.get_text() for p in doc]
 extracted=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
 chars=[len(x.strip()) for x in extracted.split('\f') if x.strip()]
 assert len(chars)==len(doc),(name,len(chars),len(doc))
 found={}
 for query in queries.get(name,[]):
  # Simple whitespace/hyphen normalization makes line wraps searchable.
  needle=' '.join(query.lower().split())
  for i,t in enumerate(text):
   normalized=' '.join(t.lower().replace('–','-').replace('−','-').split())
   if needle in normalized:found[query]=i+1;break
 pages=sorted(set([1,len(doc)]+list(found.values())))
 if len(pages)==2:pages.insert(1,max(1,len(doc)//2))
 bounds=[]
 for i,p in enumerate(doc):
  for word in p.get_text('words'):
   if word[0]<-1 or word[1]<-1 or word[2]>p.rect.width+1 or word[3]>p.rect.height+1:
    bounds.append({'page':i+1,'box':list(word[:4]),'word':word[4]})
 stats[name]={'pages':len(doc),'median_characters_per_page':statistics.median(chars),'min_characters_per_page':min(chars),'source_sha256':sha(md),'pdf_sha256':sha(pdf),'tex_sha256':sha(tex),'tex_source_stamp_matches':True,'query_pages':found,'rendered_pages':pages,'out_of_page_word_boxes':bounds}
 assert statistics.median(chars)>1500,('implausibly sparse document',name)
 for page in pages:
  target=OUT/f'{name}-p{page:03}.png'
  pix=doc[page-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False);pix.save(target)
  im=Image.open(target).convert('RGB');im.thumbnail((320,460))
  card=Image.new('RGB',(340,495),'#dddddd');card.paste(im,((340-im.width)//2,25))
  ImageDraw.Draw(card).text((10,7),f'{name}  page {page}/{len(doc)}',fill='black')
  thumbs.append((name,page,card))
 doc.close()
(OUT/'stats.json').write_text(json.dumps(stats,indent=2)+'\n')
for offset in range(0,len(thumbs),12):
 items=thumbs[offset:offset+12];sheet=Image.new('RGB',(340*4,495*3),'white')
 for j,(_,_,card) in enumerate(items):sheet.paste(card,((j%4)*340,(j//4)*495))
 sheet.save(OUT/f'contact-{offset//12+1}.jpg',quality=88)
print(json.dumps({n:{'pages':s['pages'],'median_characters_per_page':s['median_characters_per_page'],'rendered_pages':s['rendered_pages'],'out_of_page_boxes':len(s['out_of_page_word_boxes'])} for n,s in stats.items()},indent=2))

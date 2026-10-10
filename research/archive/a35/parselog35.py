import sys, re
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
t = t.replace('\\n', '\n').replace('\\u001b', '')
i = t.find('=== ERRORS ===')
j = t.find('=== SORRY ===')
seg = t[i:j] if i >= 0 and j > i else t[-6000:]
seg = re.sub(r'\d{4}-\d\d-\d\dT[\d:.]+Z ', '', seg)
print(seg[:int(sys.argv[2]) if len(sys.argv) > 2 else 12000])

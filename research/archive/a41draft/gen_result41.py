"""A41's result note, generated from measurements.json and the shards' final lines (draft for the local rehearsal)."""
import importlib.util, json, sys
C_PATH, MEAS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
FINALS = sys.argv[4:]
spec = importlib.util.spec_from_file_location('c41', C_PATH); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
meas = json.load(open(MEAS, encoding='utf-8'))
label, dis = C.agree(meas)
if label == 'A41-CENSUS-CORRECTED':
    sentence = C.render(C.SENTENCES[label], C.values_from_measurements(meas))
else:
    sentence = C.render(C.SENTENCES[label], {'note.disagreements': '; '.join(dis), 'note.failing': '; '.join(dis)})
note = """# Track B act 41 — partition structures, index maps and factorization classes: RESULT

**Outcome:** `%s`

## The post-round sentence

> %s

## The shards' final lines

```text
%s
```
""" % (label, sentence, '\n'.join(FINALS))
open(OUT, 'w', encoding='utf-8').write(note)
print(label)

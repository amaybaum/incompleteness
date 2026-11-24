"""What P's "two-step" edit is: an alternative variant (old_step2 is the old text on the projected integration),
chosen by P's variant() as the first pair whose old occurs exactly once; P applies ONE pair, not both.
Checks v5.3's correspondence rule ("replaced bytes equal e.old and image equals the result of both steps")
against P's own apply_edits on two toy texts."""
import importlib.util, hashlib, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
assert hashlib.sha256(open(os.path.join(D, 'edits_check.py'), 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('pec', os.path.join(D, 'edits_check.py')); ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
e = {'id': 'Z1', 'file': 'f.md', 'kind': 'ptr', 'old': 'item (ii) states A1', 'new': 'item (ii) is removed',
     'old_step2': 'item (ii), as merged, states A1', 'new_step2': 'item (ii), as merged, is removed'}
def both_steps(text):  # v5.3's reading: apply step 1, then step 2
    t = text.replace(e['old'], e['new'], 1)
    return t.replace(e['old_step2'], e['new_step2'], 1)
for label, H in (('H holds old', 'A. item (ii) states A1. B.'), ('H holds old_step2 (projected integration)', 'A. item (ii), as merged, states A1. B.')):
    o, n, which = ec.variant(e, H)
    p_result = ec.apply_edits({'edits': [e]}, lambda f: H)['f.md']
    v53_old_ok = (o == e['old'])
    v53_img_ok = (n == both_steps(o) if o else False)
    print('%-42s P applies %-9s P result %r' % (label, which, p_result))
    print('%42s v5.3 rule: replaced bytes == e.old: %s; image == result of both steps: %s -> %s' % ('', v53_old_ok, v53_img_ok, 'accepted' if v53_old_ok and v53_img_ok else 'ERROR SOURCE_CHANGED, while P applies it'))
print('P static_new on the edit (both pairs scanned independently):', [len(x) for x in ec.static_new({'edits': [e]})[:3]])

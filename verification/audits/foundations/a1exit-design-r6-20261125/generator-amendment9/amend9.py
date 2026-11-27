"""Generator of the expectation change of r6 amendment 9 (owner-approved; recorded on #1169, the text drafted
separately): the rows whose runs read the configuration's rule records admit NOT RUN at the tool's landing, released
when every rule record the configuration references is reviewed (OBL-3), in the form of RT-T's release. A record
that a runner makes is evaluated as for any row. No other row and no expected value changes.

Usage: python3 -I -B amend9.py DIR OUT   (DIR holds EXPECTATIONS.json as amendment 8 leaves it)

The row list is the set of kept rows whose retained evidence, in the local measurement at 768825452 (the A1 real-tree
suites with the staged draft), names a rule record of the configuration as having no review record.
"""
import hashlib
import json
import os
import sys

BASE_SHA256 = '1ebed4bf28d662d24c86d96883c3914d649bc3619ec339e551ad6cef44b5b745'
RC_RULES = 'every rule record referenced by the configuration at the commit under check is reviewed (OBL-3)'
REASON = ('reads the configuration\'s rule records, which are reviewed and adopted with the amended plan at F (OBL-3); '
          'it gates plan freeze F, not the tool\'s landing (amendment 9)')
RELEASE = 'every rule record the configuration at the commit under check references carries an accepting review (OBL-3)'
ROWS = ['A11r', 'A2r', 'A4r', 'A5r', 'A7r', 'A9r', 'G1', 'G2', 'G3', 'L1', 'L2', 'L3', 'L4', 'N-W', 'N3-config-route', 'RT-A', 'RT-C', 'RT-D', 'RT-D-gr58', 'RT-DR', 'RT-E', 'RT-H0', 'RT-L', 'RT-O9', 'RT-T0', 'RT-X', 'S11-11', 'S11-14', 'S11-2a', 'S11-3', 'S11-4', 'S11-56', 'S2r', 'V1', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V2', 'V20', 'V21', 'V22', 'V25', 'V26', 'V27', 'V27-glossary', 'V3', 'V4', 'V5', 'V6', 'V7a', 'V7b', 'V7c', 'V9', 'WB1', 'WB10', 'WB12', 'WB13', 'WB14', 'WB15', 'WB2', 'WB3', 'WB4', 'WB5', 'WB6', 'WB7', 'WB8', 'WB9', 'item11-T1p']


def main(base, out):
    raw = open(os.path.join(base, 'EXPECTATIONS.json'), 'rb').read()
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise SystemExit('EXPECTATIONS.json is not the amendment-8 file')
    exp = json.loads(raw)
    by = {r['id']: r for r in exp['rows']}
    if len(set(ROWS)) != 75 or not set(ROWS) <= set(by):
        raise SystemExit('row list')
    for i in ROWS:
        r = by[i]
        if 'not_run' in r:
            raise SystemExit('%s already carries not_run' % i)
        r['status_allowed'] = list(r.get('status_allowed', ['PASS'])) + ['NOT RUN']
        r['not_run'] = {'reason': REASON, 'release_condition': RELEASE, 'release_check': RC_RULES}
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'EXPECTATIONS.json'), 'wb') as f:
        f.write((json.dumps(exp, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
    print('rows', len(ROWS))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

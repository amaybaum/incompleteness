"""Site-map adapter for the frozen A1-EXIT site map, its rows and the Phase-0 quotes."""
import json

INTERFACE = 'sitemap'
NAME = 'a1exit-sitemap'
VERSION = 2
SITEMAP_SCHEMA = 'a1exit site map v2'
CONTEXT_FIELD = 's3'


def load(main, companions, read=None):
    """main: sitemap.json bytes; companions: {'rows': rows.json, 'phase0': Phase-0 sites.json}."""
    sm = json.loads(main.decode('utf-8'))
    if sm.get('schema') != SITEMAP_SCHEMA:
        return {'errors': [('schema', 'unknown site-map schema %r' % sm.get('schema'))]}
    p0 = json.loads(companions['phase0'].decode('utf-8')) if companions.get('phase0') else {'sites': []}
    rows = json.loads(companions['rows'].decode('utf-8')) if companions.get('rows') else {}
    quotes = {s['id']: s.get('quote') for s in p0.get('sites', [])}
    sites = []
    for s in sm['sites']:
        sites.append({'file': s['file'], 'line': s['line'],
                      'carried': {'row': s.get('row'), 'code': s.get('code'), 'owner': s.get('owner')},
                      'context_field_value': s.get(CONTEXT_FIELD), 'quote': quotes.get(s.get('p0_id')),
                      'p0_id': s.get('p0_id')})
    overrides = {k: v.get('anchor') for k, v in rows.get('site_overrides', {}).items()}
    reads = []
    for r in rows.get('new_site_rules', []):
        reads += list(r.get('read', []))
    return {'pin': sm['pin'], 'manuscript_digest': sm.get('manuscript_digest'), 'sites': sites,
            'override_anchors': overrides, 'read_entries': sorted(set(reads)), 'errors': [],
            'context_field': CONTEXT_FIELD}

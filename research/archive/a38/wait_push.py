"""Wait for the workflow_dispatch run at a head sha to complete; print job conclusions. usage: wait_run.py <sha>"""
import json, sys, time, urllib.request
sha = sys.argv[1]
def get(url):
    return json.load(urllib.request.urlopen(url))
run = None
while run is None:
    for r in get('https://api.github.com/repos/amaybaum/incompleteness/actions/runs?event=push&per_page=10')['workflow_runs']:
        if r['head_sha'] == sha: run = r; break
    if run is None: time.sleep(20)
while True:
    r = get('https://api.github.com/repos/amaybaum/incompleteness/actions/runs/%d' % run['id'])
    if r['status'] == 'completed': break
    time.sleep(30)
jobs = get('https://api.github.com/repos/amaybaum/incompleteness/actions/runs/%d/jobs' % run['id'])['jobs']
print('run', run['id'], 'conclusion', r['conclusion'])
for j in jobs: print('  %-32s %s %s' % (j['name'], j['conclusion'], j['id']))

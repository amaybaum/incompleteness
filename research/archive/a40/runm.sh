for s in locus39.py locus40b.py; do
  python3 -c "
import resource,runpy,sys,time
t=time.time(); sys.argv=['$s']
try: runpy.run_path('$s', run_name='__main__')
finally: print('WALL %.1fs  MAXRSS %.0f MB' % (time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024), flush=True)
" > m_$s.log 2>&1
done

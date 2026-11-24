import resource, subprocess, sys, time
out, name, so, se = sys.argv[1:5]; cmd = sys.argv[sys.argv.index('--')+1:]
t = time.time()
p = subprocess.Popen(cmd, stdout=open(so, 'wb'), stderr=open(se, 'wb'))
_, status, ru = __import__('os').wait4(p.pid, 0)
w = time.time() - t
open(out, 'a').write('%s %s %.1f %d\n' % (name, __import__('os').waitstatus_to_exitcode(status), w, ru.ru_maxrss))

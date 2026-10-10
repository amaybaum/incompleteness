import subprocess, sys, time, resource
t=time.time(); r=subprocess.run(sys.argv[1:]); w=time.time()-t
u=resource.getrusage(resource.RUSAGE_CHILDREN)
print('wall %.1f user %.1f sys %.1f maxrss_MB %.0f minflt %d majflt %d nvcsw %d nivcsw %d exit %d'%(w,u.ru_utime,u.ru_stime,u.ru_maxrss/1024,u.ru_minflt,u.ru_majflt,u.ru_nvcsw,u.ru_nivcsw,r.returncode), file=sys.stderr)

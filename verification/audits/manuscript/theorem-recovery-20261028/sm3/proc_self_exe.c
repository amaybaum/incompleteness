/* Runtime-path adapter for executor PID/proc namespace mismatch.
   No kernel, proof, tactic, environment, or file content is modified. */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

ssize_t readlink(const char *path, char *buf, size_t bufsiz) {
    static ssize_t (*actual)(const char *, char *, size_t);
    if (!actual) actual = dlsym(RTLD_NEXT, "readlink");
    char own[64];
    snprintf(own, sizeof(own), "/proc/%d/exe", (int)getpid());
    if (strcmp(path, own) == 0)
        return actual("/proc/self/exe", buf, bufsiz);
    return actual(path, buf, bufsiz);
}

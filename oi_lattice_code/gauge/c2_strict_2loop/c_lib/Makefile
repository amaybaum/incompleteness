# Makefile for c2_strict_2loop/c_lib/
#
# Build all C+OpenMP binaries with `make`.
# Clean with `make clean`.
#
# Requirements: gcc with OpenMP support.

CC = gcc
CFLAGS = -O3 -fopenmp -ffast-math -march=native
LDLIBS = -lm

BINARIES = kite_T1a kite_T1a_chunked vertex_T1b vertex_T1b_chunked \
           ghost_Ga ghost_Gb ghost_Gc

all: $(BINARIES)

%: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

clean:
	rm -f $(BINARIES)

.PHONY: all clean

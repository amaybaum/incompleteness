#!/bin/bash
# K=6 Constraint Effective Potential — h-scan
# Scans the Higgs background field h at fixed bare mass m
# Measures dV/dh decomposed into fermion and gauge contributions
#
# Usage: bash run_cep_scan.sh [L] [mass] [N_traj]
# Default: L=6, mass=0.10, 100 trajectories per h value

L=${1:-6}
MASS=${2:-0.10}
N=${3:-100}
NTHM=20

echo "============================================="
echo "K=6 Constraint Effective Potential h-scan"
echo "L=$L  mass=$MASS  $N trajectories per h"
echo "============================================="

# Compile
echo "Compiling..."
gcc -O3 -fopenmp -o k6_cep k6_cep.c -lm
if [ $? -ne 0 ]; then echo "Compile failed!"; exit 1; fi

# Summary file
SUMF="cep_summary_L${L}_m$(printf '%03d' $(echo "$MASS*1000" | bc | cut -d. -f1)).dat"
echo "# CEP h-scan: L=$L mass=$MASS N=$N" > $SUMF
echo "# h  pbp  pbp_err  dvdh_f  dvdh_g  dvdh_tot  dvdh_err  P3  P2  P1  acc%" >> $SUMF

# Scan h values: 0.0 to 2.0
for h in 0.00 0.05 0.10 0.15 0.20 0.30 0.40 0.50 0.70 1.00 1.50 2.00; do
    OUTF="cep_L${L}_m$(printf '%03d' $(echo "$MASS*1000" | bc | cut -d. -f1))_h$(printf '%04d' $(echo "$h*1000" | bc | cut -d. -f1)).dat"
    echo ""
    echo "--- h=$h → $OUTF ---"
    ./k6_cep $L $MASS $h $N $NTHM $OUTF

    # Extract result line and append to summary
    RESULT=$(grep "^# RESULT" $OUTF | tail -1)
    if [ -n "$RESULT" ]; then
        # Parse: mass, h, pbp±err, dvdh±err, acc
        PBP=$(echo $RESULT | sed 's/.*<pbp>=\([^ ]*\)±.*/\1/')
        PBPE=$(echo $RESULT | sed 's/.*<pbp>=[^±]*±\([^ ]*\).*/\1/')
        DVDH=$(echo $RESULT | sed 's/.*<dV\/dh>=\([^ ]*\)±.*/\1/')
        DVDHE=$(echo $RESULT | sed 's/.*<dV\/dh>=[^±]*±\([^ ]*\).*/\1/')
        ACC=$(echo $RESULT | sed 's/.*acc=\([0-9]*\)%.*/\1/')
        # Get last trajectory line for plaquettes and dvdh decomposition
        LASTLINE=$(grep -v '^#' $OUTF | tail -1)
        DVF=$(echo $LASTLINE | awk '{print $10}')
        DVG=$(echo $LASTLINE | awk '{print $11}')
        P3=$(echo $LASTLINE | awk '{print $13}')
        P2=$(echo $LASTLINE | awk '{print $14}')
        P1=$(echo $LASTLINE | awk '{print $15}')
        echo "$h  $PBP  $PBPE  $DVF  $DVG  $DVDH  $DVDHE  $P3  $P2  $P1  $ACC" >> $SUMF
    fi
done

echo ""
echo "============================================="
echo "SCAN COMPLETE — Summary in $SUMF"
echo "============================================="
echo ""
cat $SUMF
echo ""
echo "Key diagnostic: if dvdh_g becomes less negative (or positive)"
echo "as h increases, the gauge-Higgs coupling is providing the"
echo "stabilizing force needed for electroweak symmetry breaking."
echo ""
echo "Also check: P2 should increase toward 1 as h increases"
echo "(SU(2) ordering from W/Z mass). The entropy cost of this"
echo "ordering is the effective quartic λh⁴ stabilization."

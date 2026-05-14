#!/bin/bash
# K=6 Dynamical Higgs — κ scan
# Finds the Higgs phase transition by scanning the hopping parameter κ
# The critical κ_c marks electroweak symmetry breaking
#
# Usage: bash run_higgs_scan.sh [L] [lambda] [N_traj]
# Default: L=6, λ=0.01, 200 trajectories per κ
#
# OI-predicted parameters:
#   λ ≈ 0   (λ(M_Pl)=0 from composite A₁ taste → use small λ for stability)
#   y = 0.122 (m_match = λ_Cab × g₀²)
#   m₀ = 0.10 (bare fermion mass)
#   κ: SCAN — the critical κ_c determines the VEV

L=${1:-6}
LAM=${2:-0.01}
N=${3:-200}
NTHM=30
M0=0.10
YUK=0.122

echo "============================================="
echo "K=6 Dynamical Higgs — κ scan"
echo "L=$L  λ=$LAM  y=$YUK  m₀=$M0"
echo "$N trajectories per κ"
echo "============================================="

# Compile
echo "Compiling..."
gcc -O3 -o k6_higgs k6_higgs.c -lm
if [ $? -ne 0 ]; then echo "Compile failed!"; exit 1; fi

# Summary file
SUMF="higgs_summary_L${L}_lam$(printf '%04d' $(echo "$LAM*10000" | bc | cut -d. -f1)).dat"
echo "# Higgs κ-scan: L=$L lambda=$LAM yukawa=$YUK m0=$M0 N=$N" > $SUMF
echo "# kappa  phi_mod  phi_err  hop  hop_err  chi_hop  P2  acc%" >> $SUMF

# Free-field κ_c = 1/(2d) = 1/6 ≈ 0.167
# With gauge+fermion interactions, κ_c shifts — scan broadly
for k in 0.05 0.08 0.10 0.12 0.14 0.16 0.18 0.20 0.22 0.25 0.30 0.35 0.40 0.50; do
    OUTF="higgs_L${L}_k$(printf '%04d' $(echo "$k*1000" | bc | cut -d. -f1))_lam$(printf '%04d' $(echo "$LAM*10000" | bc | cut -d. -f1)).dat"
    echo ""
    echo "--- κ=$k → $OUTF ---"
    ./k6_higgs $L $M0 $k $LAM $YUK $N $NTHM $OUTF

    # Extract result
    RESULT=$(grep "^# RESULT" $OUTF | tail -1)
    if [ -n "$RESULT" ]; then
        PM=$(echo $RESULT | sed 's/.*⟨|Φ|⟩=\([^ ]*\)±.*/\1/')
        PME=$(echo $RESULT | sed 's/.*⟨|Φ|⟩=[^±]*±\([^ ]*\).*/\1/')
        HOP=$(echo $RESULT | sed 's/.*⟨hop⟩=\([^ ]*\)±.*/\1/')
        HOPE=$(echo $RESULT | sed 's/.*⟨hop⟩=[^±]*±\([^ ]*\).*/\1/')
        CHI=$(echo $RESULT | sed 's/.*chi_hop=\([^ ]*\) .*/\1/')
        ACC=$(echo $RESULT | sed 's/.*acc=\([0-9]*\)%.*/\1/')
        P2=$(grep -v '^#' $OUTF | tail -1 | awk '{print $10}')
        echo "$k  $PM  $PME  $HOP  $HOPE  $CHI  $P2  $ACC" >> $SUMF
    fi
done

echo ""
echo "============================================="
echo "SCAN COMPLETE — Summary in $SUMF"
echo "============================================="
echo ""
cat $SUMF
echo ""
echo "Key diagnostics (gauge-invariant, Elitzur-safe):"
echo "  1. χ_hop peak → κ_c (phase transition)"
echo "  2. ⟨hop⟩ jumps from ~0 to ~O(1) at κ_c"
echo "  3. Repeat at L=8 to confirm volume independence"
echo ""
echo "In the BROKEN phase (κ > κ_c):"
echo "  ⟨hop⟩ ≈ |Φ|² × ⟨Re[U₂]⟩ — measures the gauge-invariant VEV"
echo "  The W-boson mass m_W ∝ √(κ × ⟨hop⟩)"

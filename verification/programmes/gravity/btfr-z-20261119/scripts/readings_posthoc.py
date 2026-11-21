"""Post hoc, descriptive only (amendment 1): a0(z) under three horizon-temperature readings.

Written after the preregistered result was known. Nothing here is a preregistered test, and no
verdict is drawn from it: choosing a temperature reading after seeing the data is the kind of
adjustable variant that §A.29 rejects. It reads `results.json` (the measured O and sigma_O) and
prints the z-scores that the PREREG §7 formula would give for each reading.

Readings (a0 taken proportional to the horizon surface gravity, as in the G3-HOM record §3.4):
  hubble  -- kappa = H                         (GR §7.3 as written; the preregistered reading)
  kodama  -- kappa = H |1 + Hdot/(2 H^2)|      (Hayward-Kodama apparent-horizon temperature, GR:56)
  event   -- kappa = c / R_E, R_E = a * int_a^inf c da' / (a'^2 H(a'))   (event horizon)
Run:  python3 -I verification/programmes/gravity/btfr-z-20261119/scripts/readings_posthoc.py
"""
import json
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import oi_model as om  # noqa: E402


def E(z, omv):
    return math.sqrt(omv * (1 + z) ** 3 + 1 - omv)


def H0_RE(z, omv):
    """Physical event-horizon radius in units of c/H0 at redshift z (flat LCDM)."""
    a0 = 1.0 / (1.0 + z)
    amax = 1.0e4
    la = np.linspace(math.log(a0), math.log(amax), 400001)
    a = np.exp(la)
    integrand = 1.0 / (a * np.sqrt(omv / a ** 3 + 1 - omv))      # da/(a^2 E) = dlna/(a E)
    integral = float(np.sum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(la)))
    integral += 1.0 / (amax * math.sqrt(1 - omv))                 # de Sitter tail
    return a0 * integral


def kappa(z, reading, omv):
    if reading == "hubble":
        return E(z, omv)
    if reading == "kodama":
        omz = omv * (1 + z) ** 3 / E(z, omv) ** 2
        return E(z, omv) * abs(1 - 0.75 * omz)                    # Hdot/H^2 = -1.5 Om(z)
    if reading == "event":
        return 1.0 / H0_RE(z, omv)
    raise ValueError(reading)


def main():
    unit = HERE.parent
    r = json.loads((unit / "results.json").read_text())
    M = r["measurements"]
    omv = om.OM_PRIMARY
    control = H0_RE(0.0, 0.31)
    out = {"control_H0RE0_Om0.31": control, "control_expected": 1.147,
           "control_pass": abs(control - 1.147) < 0.002}
    zz = {"z0.9": M["T1_z0.9"]["median_z"], "z2.3": M["T1_z2.3"]["median_z"]}
    k0 = {rd: kappa(0.0, rd, omv) for rd in ("hubble", "kodama", "event")}
    out["ratio_a0_z2_over_z0"] = {rd: kappa(2.0, rd, omv) / k0[rd] for rd in k0}
    out["dex_vs_hubble_at_z2"] = {rd: math.log10(out["ratio_a0_z2_over_z0"]["hubble"]
                                                 / out["ratio_a0_z2_over_z0"][rd]) for rd in k0}
    rows = {}
    for rd in k0:
        P1 = -math.log10(kappa(zz["z0.9"], rd, omv) / k0[rd])
        P2 = -math.log10(kappa(zz["z2.3"], rd, omv) / k0[rd])
        sc = (lambda z, o, rd=rd: kappa(z, rd, o) / kappa(0.0, rd, o))
        fwd = om.P_vmax_variants(242.0, zz["z0.9"], 4.8, zz["z2.3"], 4.0, sc)
        fwd_c = fwd[("sph", "simple", om.H0_PRIMARY, om.OM_PRIMARY)]
        e = {"T1_z0.9_P": P1, "T1_z2.3_P": P2, "T2_P_asym": P2 - P1, "T2_P_vmax": fwd_c}
        for key, P, test in (("z_T1_z0.9", P1, "T1_z0.9"), ("z_T1_z2.3", P2, "T1_z2.3"),
                             ("z_T2_asym", P2 - P1, "T2"), ("z_T2_vmax", fwd_c, "T2")):
            e[key] = abs(M[test]["O"] - P) / M[test]["sigma_O"]
        rows[rd] = e
    out["readings"] = rows
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()

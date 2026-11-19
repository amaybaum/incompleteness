"""BTFR-z analysis: implements PREREG.md (sections 3-9) and writes results.json and RESULT.md.

Run:  python3 -I verification/programmes/gravity/btfr-z-20261119/scripts/btfr_z.py
Deterministic: fixed seeds, no timestamps.  Requires numpy.
"""
import hashlib
import io
import json
import math
import pathlib
import sys
import zipfile

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
UNIT = HERE.parent
DATA = UNIT / "data"
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import oi_model as om  # noqa: E402

SEED = 20261119
NBOOT = 2000
NMOCK = 500
VREF = 242.0
LOG_VREF = math.log10(VREF)
EXPECTED_RESULTS_SHA = "f4a51766a5b6c8c9eb94683b8bf5cae7e83b874f23e3c3fd29fce630e018b01e"  # recorded run

# PREREG §3 hashes: (file sha256 or None, content sha256 over lines not starting with '#')
HASHES = {
    "Rotmod_LTG.zip": ("0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588", None),
    "SPARC_Lelli2016c.mrt": ("5aa0501f6b0d881fa579030e315e7b5b6ef561a5bd3a07472f9929c7e5728243", None),
    "lelli2016_btfr_fig2.tsv": (None, "53685f8574c4afa154c6c1e7b8ac3ae722d3268734a67bada6b35d30a9e24a76"),
    "ubler2017_table3.tsv": (None, "91742f444278810e0fef788b1ce3512d193e35248452ad0e8184e205b1d0a5a7"),
}


def check_hashes():
    out = {}
    for name, (full, content) in HASHES.items():
        b = (DATA / name).read_bytes()
        fh = hashlib.sha256(b).hexdigest()
        ch = None
        if content is not None:
            lines = [ln for ln in b.decode().splitlines(keepends=True) if not ln.startswith("#")]
            ch = hashlib.sha256("".join(lines).encode()).hexdigest()
        ok = (full is None or fh == full) and (content is None or ch == content)
        out[name] = {"sha256": fh, "content_sha256": ch, "ok": ok}
        if not ok:
            sys.exit(f"data hash mismatch: {name}")
    return out


# ---------------------------------------------------------------- parsing
def read_vizier_tsv(path):
    rows = [ln.rstrip("\n") for ln in path.read_text().splitlines()
            if ln.strip() and not ln.startswith("#")]
    header = [h.strip() for h in rows[0].split("\t")]
    data = []
    for ln in rows[3:]:                       # skip units and dashes lines
        f = [c.strip() for c in ln.split("\t")]
        data.append(dict(zip(header, f)))
    return data


def read_sparc():
    out = {}
    for ln in (DATA / "SPARC_Lelli2016c.mrt").read_text().splitlines():
        # 19 whitespace-separated fields per galaxy row (the byte offsets in the
        # file's own header are shifted by one column relative to the rows).
        t = ln.split()
        if len(t) != 19:
            continue
        try:
            rec = {"T": int(t[1]), "D": float(t[2]), "Inc": float(t[5]), "e_Inc": float(t[6]),
                   "L36": float(t[7]), "Rdisk": float(t[11]), "MHI": float(t[13]),
                   "Vflat": float(t[15]), "Q": int(t[17])}
        except ValueError:
            continue
        out[t[0]] = rec
    return out


def read_rotmod():
    z = zipfile.ZipFile(DATA / "Rotmod_LTG.zip")
    out = {}
    for n in z.namelist():
        rows = []
        for ln in io.StringIO(z.read(n).decode()):
            if ln.startswith("#") or not ln.strip():
                continue
            f = ln.split()
            rows.append((float(f[0]), float(f[1]), float(f[2])))
        out[n.replace("_rotmod.dat", "")] = np.array(rows)
    return out


# ---------------------------------------------------------------- fitting (PREREG §4)
def _chi2_fixed(x, y, sx, sy, s, zeta):
    w = 1.0 / (sy ** 2 + (s * sx) ** 2 + zeta ** 2)
    b = np.sum(w * (y - s * x)) / np.sum(w)
    return float(np.sum(w * (y - s * x - b) ** 2)), b


def _solve_zeta(chi2_of_zeta, dof):
    if chi2_of_zeta(0.0) / dof <= 1.0:
        return 0.0
    lo, hi = 0.0, 3.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if chi2_of_zeta(mid) / dof > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fit_fixed(x, y, sx, sy, s):
    zeta = _solve_zeta(lambda zt: _chi2_fixed(x, y, sx, sy, s, zt)[0], len(x) - 1)
    return _chi2_fixed(x, y, sx, sy, s, zeta)[1], zeta


def _best_slope(x, y, sx, sy, zeta):
    lo, hi = 0.5, 10.0
    gr = (math.sqrt(5) - 1) / 2
    a, b = hi - gr * (hi - lo), lo + gr * (hi - lo)
    fa, fb = _chi2_fixed(x, y, sx, sy, a, zeta)[0], _chi2_fixed(x, y, sx, sy, b, zeta)[0]
    while hi - lo > 1e-7:
        if fa < fb:
            hi, b, fb = b, a, fa
            a = hi - gr * (hi - lo)
            fa = _chi2_fixed(x, y, sx, sy, a, zeta)[0]
        else:
            lo, a, fa = a, b, fb
            b = lo + gr * (hi - lo)
            fb = _chi2_fixed(x, y, sx, sy, b, zeta)[0]
    return 0.5 * (lo + hi)


def fit_free(x, y, sx, sy):
    def chi2z(zt):
        s = _best_slope(x, y, sx, sy, zt)
        return _chi2_fixed(x, y, sx, sy, s, zt)[0]
    zeta = _solve_zeta(chi2z, len(x) - 2)
    s = _best_slope(x, y, sx, sy, zeta)
    b = _chi2_fixed(x, y, sx, sy, s, zeta)[1]
    return s, b, zeta


def boot_fixed(x, y, sx, sy, s, rng, n=NBOOT):
    N = len(x)
    out = np.empty(n)
    for i in range(n):
        k = rng.integers(0, N, N)
        out[i] = fit_fixed(x[k], y[k], sx[k], sy[k], s)[0]
    return float(np.std(out, ddof=1))


def boot_free(x, y, sx, sy, rng, n=NBOOT):
    N = len(x)
    ss, bb = np.empty(n), np.empty(n)
    for i in range(n):
        k = rng.integers(0, N, N)
        ss[i], bb[i], _ = fit_free(x[k], y[k], sx[k], sy[k])
    return float(np.std(ss, ddof=1)), float(np.std(bb, ddof=1))


# ---------------------------------------------------------------- decision rule (PREREG §7)
def verdict(O, sO, P, sP):
    z = abs(O - P) / math.sqrt(sO ** 2 + sP ** 2)
    v = "consistent" if z <= 2 else ("in tension" if z <= 3 else "excluded")
    return {"z": z, "verdict": v}


SEVERITY = {"consistent": 0, "in tension": 1, "excluded": 2}


def main():
    res = {"seed": SEED, "nboot": NBOOT, "nmock": NMOCK, "numpy": np.__version__,
           "python": sys.version.split()[0]}
    res["data"] = check_hashes()

    # ---------------- anchor data
    lel = read_vizier_tsv(DATA / "lelli2016_btfr_fig2.tsv")
    sparc = read_sparc()
    rot = read_rotmod()
    L = {"name": np.array([r["Name"] for r in lel]),
         "fD": np.array([int(r["f_Dist"]) for r in lel]),
         "logMb": np.array([float(r["logMb"]) for r in lel]),
         "e_logMb": np.array([float(r["e_logMb"]) for r in lel]),
         "logVf": np.array([float(r["logVf"]) for r in lel]),
         "e_logVf": np.array([float(r["e_logVf"]) for r in lel])}
    acc = np.isin(L["fD"], [2, 3, 4, 5])
    res["anchor_counts"] = {"total": int(len(L["name"])), "accurate": int(acc.sum()),
                            "sparc_rows": len(sparc), "rotmod_files": len(rot)}

    rng = np.random.default_rng(SEED)
    controls = {}

    # ---------------- C1: Lelli+2016a reproduction
    c1 = {}
    for tag, sel, s_pub, sds, lA in (("total", np.ones_like(acc), 3.71, 0.08, 2.27),
                                     ("accurate", acc, 3.75, 0.11, 2.18)):
        x = L["logVf"][sel] - LOG_VREF
        s, b, zt = fit_free(x, L["logMb"][sel], L["e_logVf"][sel], L["e_logMb"][sel])
        pub = s_pub * LOG_VREF + lA
        c1[tag] = {"N": int(sel.sum()), "slope": s, "logM_242": b, "zeta": zt,
                   "pub_slope": s_pub, "pub_slope_err": sds, "pub_logM_242": pub,
                   "pass": abs(s - s_pub) <= sds and abs(b - pub) <= 0.05}
    # C1b: masses from the SPARC table
    diffs = []
    for i, n in enumerate(L["name"]):
        if n not in sparc:
            continue
        r = sparc[n]
        diffs.append(math.log10((0.5 * r["L36"] + 1.33 * r["MHI"]) * 1e9) - L["logMb"][i])
    diffs = np.array(diffs)
    c1["b_masses"] = {"median_abs_diff": float(np.median(np.abs(diffs))),
                      "max_abs_diff": float(np.max(np.abs(diffs))), "N_matched": int(len(diffs)),
                      "unmatched": sorted(str(n) for n in L["name"] if n not in sparc),
                      "pass": float(np.median(np.abs(diffs))) <= 0.02}
    # V_max anchor (58 accurate galaxies)
    # V_max needs the SPARC mass-model file; accurate-distance galaxies without one are dropped
    accm = acc & np.array([n in rot and n in sparc for n in L["name"]])
    vmx, evmx = [], []
    for n in L["name"][accm]:
        rc = rot[n]
        k = int(np.argmax(rc[:, 1]))
        V, eV = rc[k, 1], rc[k, 2]
        inc = math.radians(sparc[n]["Inc"])
        dinc = math.radians(sparc[n]["e_Inc"])
        sV = math.sqrt(eV ** 2 + (V * dinc / math.tan(inc)) ** 2)
        vmx.append(V)
        evmx.append(sV / (V * math.log(10)))
    vmx, evmx = np.array(vmx), np.array(evmx)
    xm = np.log10(vmx) - LOG_VREF
    sm, bm, ztm = fit_free(xm, L["logMb"][accm], evmx, L["e_logMb"][accm])
    pub19 = 3.52 * LOG_VREF + 2.59
    c1["c_vmax"] = {"N": int(accm.sum()), "dropped": sorted(str(n) for n in L["name"][acc & ~accm]), "slope": sm, "logM_242": bm, "zeta": ztm,
                    "pub_slope": 3.52, "pub_slope_err": 0.07, "pub_logM_242": pub19,
                    "median_Vmax_over_Vf": float(np.median(vmx / 10 ** L["logVf"][accm])),
                    "pass": abs(sm - 3.52) <= 0.14 and abs(bm - pub19) <= 0.10}
    controls["C1"] = c1

    # anchors used by T1/T2 (58 accurate galaxies)
    xa, ya = L["logVf"][acc] - LOG_VREF, L["logMb"][acc]
    sxa, sya = L["e_logVf"][acc], L["e_logMb"][acc]
    s_f, b_f, z_f = fit_free(xa, ya, sxa, sya)
    sd_sf, sd_bf = boot_free(xa, ya, sxa, sya, rng)
    sd_sm, sd_bm = boot_free(xm, L["logMb"][accm], evmx, L["e_logMb"][accm], rng)
    b_f4, _ = fit_fixed(xa, ya, sxa, sya, 4.0)
    anchor = {"Vf": {"slope": s_f, "slope_boot_sd": sd_sf, "b242": b_f, "b242_boot_sd": sd_bf, "zeta": z_f},
              "Vmax": {"slope": sm, "slope_boot_sd": sd_sm, "b242": bm, "b242_boot_sd": sd_bm, "zeta": ztm},
              "Vf_slope4": {"b242": b_f4}}
    res["anchor"] = anchor

    # ---------------- high-z data
    ub = read_vizier_tsv(DATA / "ubler2017_table3.tsv")
    z = np.array([float(r["z"]) for r in ub])
    lms = np.array([float(r["logM*"]) for r in ub])
    lmb = np.array([float(r["logMb"]) for r in ub])
    vc = np.array([float(r["Vcirc"]) for r in ub])
    s0 = np.array([float(r["sigma0"]) for r in ub])
    fstar = 10 ** (lms - lmb)
    fgas = 1.0 - fstar
    sy_h = np.sqrt((fstar * 0.15) ** 2 + (fgas * 0.20) ** 2)
    vrot = np.sqrt(vc ** 2 - 4.4 * s0 ** 2)
    bins = {"z0.9": z < 1.2, "z1.5": (z >= 1.2) & (z < 1.9), "z2.3": z >= 1.9}
    res["highz_counts"] = {k: int(v.sum()) for k, v in bins.items()}
    res["highz_min_fgas"] = float(fgas.min())

    def hz(sel, v, s):
        x = np.log10(v[sel]) - LOG_VREF
        sx = 20.0 / (v[sel] * math.log(10))
        b, zt = fit_fixed(x, lmb[sel], sx, sy_h[sel], s)
        return x, sx, b, zt

    # ---------------- C2: Übler reproduction
    c2 = {"counts_pass": res["highz_counts"] == {"z0.9": 65, "z1.5": 24, "z2.3": 46}}
    pubL = 3.75 * LOG_VREF + 2.18
    for tag, sel, b_pub, sd_pub, d_pub, drot_pub in (
            ("z0.9", bins["z0.9"], 10.68, 0.04, -0.44, -0.33),
            ("z2.3", bins["z2.3"], 10.85, 0.05, -0.27, -0.09),
            ("all", np.ones_like(z, bool), 10.75, 0.03, None, None)):
        x, sx, b, zt = hz(sel, vc, 3.75)
        sd = boot_fixed(x, lmb[sel], sx, sy_h[sel], 3.75, rng)
        e = {"b": b, "b_pub": b_pub, "boot_sd": sd, "boot_sd_pub": sd_pub, "zeta": zt,
             "pass_b": abs(b - b_pub) <= 0.03, "pass_sd": abs(sd - sd_pub) <= 0.02}
        if d_pub is not None:
            _, _, brot, _ = hz(sel, vrot, 3.75)
            e.update({"db": b - pubL, "db_pub": d_pub, "db_rot": brot - pubL, "db_rot_pub": drot_pub,
                      "pass_db": abs(b - pubL - d_pub) <= 0.03,
                      "pass_db_rot": abs(brot - pubL - drot_pub) <= 0.04})
        e["pass"] = all(v for k, v in e.items() if k.startswith("pass"))
        c2[tag] = e
    c2["pass"] = c2["counts_pass"] and all(c2[t]["pass"] for t in ("z0.9", "z2.3", "all"))
    controls["C2"] = c2

    # ---------------- C5, C6
    Ez = {k: round(float(om.E(k)), 2) for k in (1, 2, 3)}
    controls["C5"] = {"E": Ez, "pass": Ez == {1: 1.79, 2: 3.03, 3: 4.57}}
    lim = om.limit_controls()
    bes = om.bessel_selftest()
    controls["C6"] = {"limits": lim, "bessel_max_rel_err": bes,
                      "pass": abs(lim["deep_mond_shift"] - lim["deep_mond_expected"]) <= 0.01
                      and abs(lim["newton_shift"]) <= 0.01 and bes <= 1e-6}

    # ---------------- T1 and T2 measurements (PREREG §5, §6)
    meas = {}
    fits = {}
    for tag in ("z0.9", "z1.5", "z2.3"):
        sel = bins[tag]
        x, sx, b, zt = hz(sel, vc, s_f)
        sd = boot_fixed(x, lmb[sel], sx, sy_h[sel], s_f, rng)
        _, _, b_rot, _ = hz(sel, vrot, s_f)
        _, _, b_m, _ = hz(sel, vc, sm)
        _, _, b_4, _ = hz(sel, vc, 4.0)
        fits[tag] = {"x": x, "sx": sx, "sel": sel, "b": b, "zeta": zt, "boot_sd": sd}
        T1 = b - b_f
        fs, fg = float(np.median(fstar[sel])), float(np.median(fgas[sel]))
        budget = {"stat": math.hypot(sd, sd_bf),
                  "ps": 0.5 * abs((b_rot - b_f) - T1),
                  "vdef": 0.5 * abs((b_m - bm) - T1),
                  "imf": 0.10 * fs,
                  "gas": math.hypot(0.15 * fg, 0.05),
                  "incl": 0.02, "sel": 0.06, "dist": 0.04, "H0": 0.03}
        sO = math.sqrt(sum(v ** 2 for v in budget.values()))
        meas["T1_" + tag] = {"N": int(sel.sum()), "median_z": float(np.median(z[sel])),
                             "median_v": float(np.median(vc[sel])), "b": b, "b_boot_sd": sd,
                             "zeta": zt, "O": T1, "O_vrot": b_rot - b_f, "O_Vmax_anchor": b_m - bm,
                             "O_slope4": b_4 - b_f4, "median_fstar": fs, "median_fgas": fg,
                             "budget": budget, "sigma_O": sO}
    b1, b2 = fits["z0.9"]["b"], fits["z2.3"]["b"]
    T2 = b2 - b1
    T2rot = meas["T1_z2.3"]["O_vrot"] - meas["T1_z0.9"]["O_vrot"]
    T2_4 = meas["T1_z2.3"]["O_slope4"] - meas["T1_z0.9"]["O_slope4"]
    f1, f2 = meas["T1_z0.9"]["median_fstar"], meas["T1_z2.3"]["median_fstar"]
    budget2 = {"stat": math.hypot(fits["z0.9"]["boot_sd"], fits["z2.3"]["boot_sd"]),
               "ps": 0.5 * abs(T2rot - T2),
               "imf": math.hypot(0.10 * abs(f2 - f1), 0.05 * 0.5 * (f1 + f2)),
               "gas": math.hypot(0.10 * meas["T1_z2.3"]["median_fgas"], 0.02),
               "sel": 0.06}
    sO2 = math.sqrt(sum(v ** 2 for v in budget2.values()))
    meas["T2"] = {"O": T2, "O_vrot": T2rot, "O_slope4": T2_4, "budget": budget2, "sigma_O": sO2}
    res["measurements"] = meas

    # ---------------- predictions (PREREG §2)
    def pasym_bin(sel, omv=om.OM_PRIMARY):
        return float(np.mean(om.P_asym(z[sel], omv)))

    preds = {}
    for tag in ("z0.9", "z1.5", "z2.3"):
        sel = bins[tag]
        vals = [pasym_bin(sel, o) for o in (om.OM_PRIMARY,) + om.OM_BAND]
        preds["T1_" + tag] = {"OI_asym": (vals[0], 0.5 * (max(vals) - min(vals))),
                              "MOND_const": (0.0, 0.0),
                              "LCDM_halo": (vals[0], 0.5 * (max(vals) - min(vals)))}
    t2v = [pasym_bin(bins["z2.3"], o) - pasym_bin(bins["z0.9"], o) for o in (om.OM_PRIMARY,) + om.OM_BAND]
    zm1, zm2 = meas["T1_z0.9"]["median_z"], meas["T1_z2.3"]["median_z"]
    fo = om.summarize(om.P_vmax_variants(VREF, zm1, 4.8, zm2, 4.0, om.oi_scaling))
    fm = om.summarize(om.P_vmax_variants(VREF, zm1, 4.8, zm2, 4.0, om.mond_scaling))
    preds["T2"] = {"OI_asym": (t2v[0], 0.5 * (max(t2v) - min(t2v))),
                   "OI_vmax": (fo["central"], fo["band_halfwidth"]),
                   "MOND_const_asym": (0.0, 0.0),
                   "MOND_const_vmax": (fm["central"], fm["band_halfwidth"]),
                   "LCDM_halo": (t2v[0], 0.5 * (max(t2v) - min(t2v)))}
    res["predictions"] = {k: {m: {"P": p, "sigma_P": s} for m, (p, s) in v.items()} for k, v in preds.items()}

    # ---------------- C3: injection-recovery
    rngm = np.random.default_rng(SEED + 1)
    c3 = {}
    sdT2 = budget2["stat"]
    for inj in ("const", "OI"):
        rec = {"z0.9": [], "z2.3": []}
        for _ in range(NMOCK):
            for tag in ("z0.9", "z2.3"):
                F = fits[tag]
                sel = F["sel"]
                d = om.P_asym(z[sel]) if inj == "OI" else np.zeros(sel.sum())
                sig = np.sqrt(sy_h[sel] ** 2 + (s_f * F["sx"]) ** 2 + F["zeta"] ** 2)
                y = b_f + s_f * F["x"] + d + rngm.normal(0.0, 1.0, sel.sum()) * sig
                rec[tag].append(fit_fixed(F["x"], y, F["sx"], sy_h[sel], s_f)[0] - b_f)
        r1, r2 = np.array(rec["z0.9"]), np.array(rec["z2.3"])
        inj1 = pasym_bin(bins["z0.9"]) if inj == "OI" else 0.0
        inj2 = pasym_bin(bins["z2.3"]) if inj == "OI" else 0.0
        t2r = r2 - r1
        e = {"inj_T1_z0.9": inj1, "rec_T1_z0.9": float(r1.mean()),
             "inj_T1_z2.3": inj2, "rec_T1_z2.3": float(r2.mean()),
             "inj_T2": inj2 - inj1, "rec_T2": float(t2r.mean()), "sd_rec_T2": float(t2r.std(ddof=1)),
             "data_boot_sd_T2": sdT2}
        e["pass"] = (abs(e["rec_T1_z0.9"] - inj1) <= 0.02 and abs(e["rec_T1_z2.3"] - inj2) <= 0.02
                     and abs(e["rec_T2"] - (inj2 - inj1)) <= 0.02
                     and sdT2 / 1.5 <= e["sd_rec_T2"] <= 1.5 * sdT2)
        if inj == "const":
            P = preds["T2"]["OI_asym"][0]
            e["power_OIasym_excluded_stat_only"] = float(np.mean(np.abs(t2r - P) / sdT2 > 3))
        c3[inj] = e
    c3["pass"] = c3["const"]["pass"] and c3["OI"]["pass"]
    controls["C3"] = c3
    res["controls"] = controls

    # ---------------- verdicts (PREREG §7)
    c1ok = all(c1[k]["pass"] for k in ("total", "accurate", "b_masses", "c_vmax"))
    ok = {"T1": c1ok and c2["pass"] and controls["C5"]["pass"] and controls["C6"]["pass"],
          "T2": c2["pass"] and c3["pass"] and controls["C5"]["pass"] and controls["C6"]["pass"]}
    verd = {}
    for test in ("T1_z0.9", "T1_z2.3", "T2"):
        m = meas[test]
        out = {}
        for model, (P, sP) in preds[test].items():
            if not ok[test.split("_")[0]]:
                out[model] = {"verdict": "VOID", "z": None}
                continue
            out[model] = verdict(m["O"], m["sigma_O"], P, sP)
        verd[test] = out
    # sensitivity flags
    pairs = {"T1_z0.9": [("OI_asym", "MOND_const")], "T1_z2.3": [("OI_asym", "MOND_const")],
             "T2": [("OI_asym", "MOND_const_asym"), ("OI_vmax", "MOND_const_vmax")]}
    sens = {}
    for test, pl in pairs.items():
        for a, b in pl:
            sep = abs(preds[test][a][0] - preds[test][b][0])
            disc = sep >= 2 * meas[test]["sigma_O"]
            sens[f"{test}:{a}|{b}"] = {"separation": sep, "two_sigma_O": 2 * meas[test]["sigma_O"],
                                       "discriminating": disc}
            if not disc:
                # the ΛCDM halo scaling shares OI-asym's prediction, hence its flag
                for mm in (a, b) + (("LCDM_halo",) if a == "OI_asym" else ()):
                    if verd[test][mm]["verdict"] == "consistent":
                        verd[test][mm]["verdict"] = "consistent, non-discriminating"
    res["verdicts"] = verd
    res["sensitivity"] = sens
    if ok["T2"]:
        cand = [verd["T2"]["OI_asym"], verd["T2"]["OI_vmax"]]
        head = min(cand, key=lambda d: SEVERITY[d["verdict"].split(",")[0]])
        res["OI_headline"] = head["verdict"]
    else:
        res["OI_headline"] = "VOID"
    E1, E2 = float(om.E(zm1)), float(om.E(zm2))
    lg = math.log10(E2 / E1)
    res["R3_fitted_p"] = {"p_hat": -T2 / lg, "sigma_p": sO2 / lg}
    # Robustness beyond the rule (not part of any verdict): the coherent change of the gas masses of
    # one bin, at that bin's median gas fraction, that would bring each OI prediction to z = 2 on T2.
    rob = {}
    for mdl in ("OI_asym", "OI_vmax"):
        P2, sP2 = preds["T2"][mdl]
        need = T2 - P2 - 2.0 * math.sqrt(sO2 ** 2 + sP2 ** 2)
        e = {"required_shift_T2": need}
        for tag, sign in (("z2.3", -1.0), ("z0.9", +1.0)):
            fs_, fg_ = meas["T1_" + tag]["median_fstar"], meas["T1_" + tag]["median_fgas"]
            arg = (10 ** (sign * need) - fs_) / fg_
            e["gas_dex_" + tag] = math.log10(arg) if arg > 0 else None
        rob[mdl] = e
    res["robustness_gas"] = rob
    res["favourable_branch"] = (verd["T2"]["OI_asym"]["verdict"].startswith("consistent")
                                and verd["T2"]["MOND_const_asym"]["verdict"] == "excluded")

    (UNIT / "results.json").write_text(json.dumps(res, indent=1, sort_keys=True, default=float) + "\n")
    write_result_md(res)
    print("OI headline (T2):", res["OI_headline"])
    for test, d in verd.items():
        print(test, {k: v["verdict"] for k, v in d.items()})


# ---------------------------------------------------------------- RESULT.md (generated)
def f(x, n=3, sign=True):
    return (f"{x:+.{n}f}" if sign else f"{x:.{n}f}")


def write_result_md(r):
    C, M, P, V = r["controls"], r["measurements"], r["predictions"], r["verdicts"]
    L = []
    a = L.append
    a("# BTFR-z: result of the preregistered high-redshift BTFR test of a₀(z) = cH(z)/6")
    a("")
    a("*Generated by `scripts/btfr_z.py` from `results.json`; edit the script, not this file.*")
    a("Preregistration: `PREREG.md`, commit `7b51814046c351b0060eb9413dc4d985f08b91b1`, pushed before "
      "any statistic was computed from the data. Unit BTFR-z (#873), authorization #1169 comment "
      "7023834853; investigation only.")
    a("")
    a("**Goal link (§A.47).** As in PREREG: decides whether a₀(z) = cH(z)/6 survives the published "
      "z ≈ 0.9–2.3 BTFR data; does not decide G3, a₀ at z = 0, or the radial law.")
    a("")
    a("## Recipe and expected result (§A.42)")
    a("")
    a("```")
    a("python3 -I verification/programmes/gravity/btfr-z-20261119/scripts/btfr_z.py")
    a("```")
    a("")
    a(f"Environment of the recorded run: Python {r['python']}, numpy {r['numpy']}; seed {r['seed']}, "
      f"{r['nboot']} bootstrap resamples, {r['nmock']} mocks per injection. The run is deterministic: "
      "it rewrites `results.json` and this file byte for byte. Expected headline: "
      f"**OI on T2: {r['OI_headline']}**, with the values in the tables below. In the recorded environment "
      f"two consecutive runs gave `results.json` SHA-256 `{EXPECTED_RESULTS_SHA}`; `results.json` records the "
      "Python and numpy versions, so its digest is specific to them.")
    a("")
    a("Amendment 1 adds `scripts/readings_posthoc.py` (post hoc, descriptive; reads `results.json`):")
    a("")
    a("```")
    a("python3 -I verification/programmes/gravity/btfr-z-20261119/scripts/readings_posthoc.py")
    a("```")
    a("")
    a("Data (checked by the script against PREREG §3 before anything is computed):")
    a("")
    a("| File | SHA-256 | content SHA-256 (non-`#` lines) |")
    a("|---|---|---|")
    for k, v in sorted(r["data"].items()):
        a(f"| `data/{k}` | `{v['sha256']}` | `{v["content_sha256"] or "—"}` |")
    a("")
    a("## Controls")
    a("")
    c1 = C["C1"]
    a("| Control | Measured | Target | Pass |")
    a("|---|---|---|---|")
    for t in ("total", "accurate"):
        e = c1[t]
        a(f"| C1 Lelli+2016a, {e['N']} galaxies | s = {e['slope']:.3f}, log M_b(242) = {e['logM_242']:.3f} | "
          f"s = {e['pub_slope']} ± {e['pub_slope_err']}, {e['pub_logM_242']:.3f} ± 0.05 | {e['pass']} |")
    e = c1["b_masses"]
    unm = ", ".join(e["unmatched"]) or "none"
    a(f"| C1b log(0.5 L + 1.33 M_HI) vs Lelli log M_b ({e['N_matched']} matched; not in SPARC: {unm}) | "
      f"median \\|Δ\\| = {e['median_abs_diff']:.4f} "
      f"(max {e['max_abs_diff']:.3f}) | ≤ 0.02 | {e['pass']} |")
    e = c1["c_vmax"]
    drp = ", ".join(e["dropped"]) or "none"
    a(f"| C1c V_max anchor, {e['N']} galaxies (dropped, no SPARC rotation curve: {drp}) | s ={e['slope']:.3f}, log M_b(242) = {e['logM_242']:.3f} "
      f"(median V_max/V_f = {e['median_Vmax_over_Vf']:.3f}) | s = 3.52 ± 0.14, {e['pub_logM_242']:.3f} ± 0.10 "
      f"(Lelli+2019) | {e['pass']} |")
    c2 = C["C2"]
    a(f"| C2 band counts | {r['highz_counts']} | 65/24/46 | {c2['counts_pass']} |")
    for t in ("z0.9", "z2.3", "all"):
        e = c2[t]
        s = (f"| C2 Übler+2017 {t}, s = 3.75 | b = {e['b']:.3f} ± {e['boot_sd']:.3f}")
        tgt = f"{e['b_pub']} ± {e['boot_sd_pub']} (tol. 0.03; σ tol. 0.02)"
        if "db" in e:
            s += f"; Δb = {e['db']:+.3f}; Δb(v_rot) = {e['db_rot']:+.3f}"
            tgt += f"; Δb = {e['db_pub']} (±0.03); Δb(v_rot) = {e['db_rot_pub']} (±0.04)"
        a(s + f" | {tgt} | {e['pass']} |")
    e = C["C3"]
    for inj in ("const", "OI"):
        g = e[inj]
        a(f"| C3 injection ({inj}) | T1: {g['rec_T1_z0.9']:+.3f}, {g['rec_T1_z2.3']:+.3f}; T2: {g['rec_T2']:+.3f} "
          f"(sd {g['sd_rec_T2']:.3f}) | {g['inj_T1_z0.9']:+.3f}, {g['inj_T1_z2.3']:+.3f}; {g['inj_T2']:+.3f} "
          f"(±0.02; sd within ×1.5 of {g['data_boot_sd_T2']:.3f}) | {g['pass']} |")
    a(f"| C5 E(1), E(2), E(3) | {C['C5']['E']} | 1.79, 3.03, 4.57 | {C['C5']['pass']} |")
    lim = C["C6"]["limits"]
    a(f"| C6 forward-model limits | deep-MOND {lim['deep_mond_shift']:+.4f} (vs {lim['deep_mond_expected']:+.4f}); "
      f"Newtonian {lim['newton_shift']:+.4f}; Bessel {C['C6']['bessel_max_rel_err']:.1e} | ±0.01; ±0.01; ≤1e-6 | "
      f"{C['C6']['pass']} |")
    a("")
    a(f"Power of T2 against OI (C3, constant-a₀ truth, statistical σ only): OI-asym is excluded in "
      f"{100 * C['C3']['const']['power_OIasym_excluded_stat_only']:.1f}% of mocks.")
    a("")
    a("## Anchor and measurements")
    a("")
    an = r["anchor"]
    a(f"Anchor (58 accurate-distance SPARC galaxies): V_f relation s = {an['Vf']['slope']:.3f} ± "
      f"{an['Vf']['slope_boot_sd']:.3f}, log M_b(242) = {an['Vf']['b242']:.3f} ± {an['Vf']['b242_boot_sd']:.3f}; "
      f"V_max relation s = {an['Vmax']['slope']:.3f} ± {an['Vmax']['slope_boot_sd']:.3f}, log M_b(242) = "
      f"{an['Vmax']['b242']:.3f} ± {an['Vmax']['b242_boot_sd']:.3f} (bootstrap). High-z fits use the V_f slope.")
    a("")
    a("| Statistic | N | median z | O (dex) | O with v_rot | O with V_max anchor | O, slope 4 | σ_O |")
    a("|---|---|---|---|---|---|---|---|")
    for t in ("T1_z0.9", "T1_z1.5", "T1_z2.3"):
        m = M[t]
        a(f"| {t.replace('_', ' ')} | {m['N']} | {m['median_z']:.3f} | {f(m['O'])} | {f(m['O_vrot'])} | "
          f"{f(m['O_Vmax_anchor'])} | {f(m['O_slope4'])} | {m['sigma_O']:.3f} |")
    m = M["T2"]
    a(f"| T2 (z~2.3 − z~0.9) | 46/65 | — | {f(m['O'])} | {f(m['O_vrot'])} | (anchor-free) | {f(m['O_slope4'])} | "
      f"{m['sigma_O']:.3f} |")
    a("")
    a("T1 z~1.5 is descriptive only (PREREG §3). Uncertainty budgets (dex):")
    a("")
    keys = ["stat", "ps", "vdef", "imf", "gas", "incl", "sel", "dist", "H0"]
    a("| Statistic | " + " | ".join(keys) + " | total |")
    a("|---" * (len(keys) + 2) + "|")
    for t in ("T1_z0.9", "T1_z2.3", "T2"):
        b = M[t]["budget"]
        a(f"| {t.replace('_', ' ')} | " + " | ".join(f"{b[k]:.3f}" if k in b else "—" for k in keys)
          + f" | {M[t]['sigma_O']:.3f} |")
    a("")
    a("## Predictions and verdicts (rule of PREREG §7)")
    a("")
    a("| Statistic | Model | P (dex) | σ_P | O − P | z | Verdict |")
    a("|---|---|---|---|---|---|---|")
    for t in ("T1_z0.9", "T1_z2.3", "T2"):
        for mdl, pp in P[t].items():
            v = V[t][mdl]
            zz = "—" if v["z"] is None else f"{v['z']:.2f}"
            a(f"| {t.replace('_', ' ')} | {mdl} | {f(pp['P'])} | {pp['sigma_P']:.3f} | {f(M[t]['O'] - pp['P'])} | "
              f"{zz} | {v['verdict']} |")
    a("")
    a("Sensitivity (PREREG §7):")
    a("")
    for k, s in r["sensitivity"].items():
        a(f"- {k}: separation {s['separation']:.3f} dex vs 2σ_O = {s['two_sigma_O']:.3f} → "
          f"{'discriminating' if s['discriminating'] else 'non-discriminating'}.")
    a("")
    a("## Verdict")
    a("")
    t2 = V["T2"]
    a(f"- **OI, headline (T2, less severe of its two predictions): {r['OI_headline']}.** "
      f"OI-asym {t2['OI_asym']['verdict']} (z = {t2['OI_asym']['z']:.2f}); OI forward model "
      f"{t2['OI_vmax']['verdict']} (z = {t2['OI_vmax']['z']:.2f}).")
    a(f"- Constant-a₀ MOND on T2: asymptotic {t2['MOND_const_asym']['verdict']} (z = "
      f"{t2['MOND_const_asym']['z']:.2f}); forward model {t2['MOND_const_vmax']['verdict']} "
      f"(z = {t2['MOND_const_vmax']['z']:.2f}).")
    a(f"- ΛCDM analytic halo scaling on T2: {t2['LCDM_halo']['verdict']} (z = {t2['LCDM_halo']['z']:.2f}); "
      "its prediction is identical to OI-asym, so this test does not separate them.")
    for t in ("T1_z0.9", "T1_z2.3"):
        vv = V[t]
        a(f"- {t.replace('_', ' ')}: OI-asym {vv['OI_asym']['verdict']} (z = {vv['OI_asym']['z']:.2f}); "
          f"constant-a₀ MOND {vv['MOND_const']['verdict']} (z = {vv['MOND_const']['z']:.2f}).")
    t1o = [V[t]["OI_asym"]["verdict"].split(",")[0] for t in ("T1_z0.9", "T1_z2.3")]
    if len(set(t1o + [r["OI_headline"].split(",")[0]])) > 1:
        a("- T1 and T2 verdicts for OI differ; both are stated and no single verdict is drawn from T1 (PREREG §7).")
    a(f"- Favourable branch triggered: {r['favourable_branch']}.")
    p = r["R3_fitted_p"]
    a(f"- R3 (retrodiction, not a test): fitting a₀ ∝ H(z)^p to T2 gives p = {p['p_hat']:.2f} ± {p['sigma_p']:.2f} "
      "(p = 1 is OI, p = 0 constant a₀). R1 (free zero-points) and R2 (Übler's tuned toy model) fit these data by "
      "construction and are not scored.")
    a("")
    a("Every verdict is conditional on the mass-inference chain of PREREG §3: the high-z baryonic masses use "
      "SED stellar masses and a molecular-gas scaling relation, not per-galaxy gas measurements, and the high-z "
      "velocities are model peak circular velocities with a pressure-support correction. One high-z sample "
      "(KMOS³D) carries the whole high-z evidence.")
    a("")
    a("Scope (amendment 1, `amendments/AMENDMENT-1-20261119-temperature-reading.md`, written after this result "
      "was known): every OI verdict above is for GR §7.3 as written, a₀(z) = cH(z)/6 with the de Sitter "
      "temperature ħH/2πk_B on the Hubble horizon c/H(z). The Hayward–Kodama apparent-horizon and event-horizon "
      "readings were not preregistered and are not tested here; the amendment describes them post hoc only.")
    a("")
    a("## Deviations from the preregistration")
    a("")
    c1b, c1c = C["C1"]["b_masses"], C["C1"]["c_vmax"]
    a(f"- The V_max anchor has {c1c['N']} galaxies, not 58: {', '.join(c1c['dropped'])} is in the Lelli+2016a "
      "accurate-distance table but has no public SPARC rotation curve. The V_f anchor keeps all 58.")
    a(f"- C1b compares {c1b['N_matched']} galaxies ({', '.join(c1b['unmatched'])} are not in the public SPARC "
      f"table). One galaxy differs by {c1b['max_abs_diff']:.2f} dex; the anchor fits use the Lelli table's masses, "
      "so C1b checks the mass recipe and does not enter any statistic.")
    a("- SPARC Table 1 is parsed as 19 whitespace-separated fields; the byte offsets in the file's header are "
      "shifted by one column relative to its rows.")
    a("- The sensitivity flag (PREREG §7) is applied to the ΛCDM halo scaling together with OI-asym, whose "
      "prediction it shares.")
    a("")
    a("## Robustness beyond the rule (not part of any verdict)")
    a("")
    a("Coherent change of one bin's gas masses (at its median gas fraction) that would bring an OI prediction "
      "to z = 2 on T2, all other inputs fixed:")
    a("")
    for mdl, e in r["robustness_gas"].items():
        g2 = "not reachable even with zero gas" if e["gas_dex_z2.3"] is None else f"{e['gas_dex_z2.3']:+.2f} dex"
        g1 = "not reachable" if e["gas_dex_z0.9"] is None else f"{e['gas_dex_z0.9']:+.2f} dex"
        a(f"- {mdl}: T2 must fall by {e['required_shift_T2']:.3f} dex; z ~ 2.3 gas masses {g2}, or z ~ 0.9 "
          f"gas masses {g1}.")
    a("")
    a("The preregistered gas term for T2 allows 0.10 dex of differential calibration error in the z ~ 2.3 "
      "scaling-relation gas masses. A larger epoch-dependent bias of the Tacconi relation, a selection "
      "difference between the bins beyond Übler's alternatives, or a velocity-definition effect that differs "
      "between z ~ 0.9 and z ~ 2.3 would each act on T2 directly; these are the places review should press.")
    a("")
    a("## Findings for routing (no manuscript edit in this unit)")
    a("")
    a("- Axis (§A.23): a₀(z) = cH(z)/6 is fixed by H₀, the imported 1/6 and a supplied background, and was not "
      "fitted to these data, so this is a correctness-axis confrontation. It is not externally replicated and "
      "has had no independent review.")
    a("- `papers/GR.md`:516 states that the BTFR-evolution tension \"is not yet statistically quantified\". This "
      "record quantifies it for one sample under stated systematics. Any change to GR §7.3, to `book/ch07-gravity.md` "
      "or to the FULL mirror needs independent review of this record and a separate owner decision (§A.25, §A.27).")
    a("- Status-surface discrepancy found while tracing the claim: `book/ch09-universality.md`:150 (mirrored in "
      "`book/The-Incompleteness-of-Observation-FULL.md`:2563) lists \"Baryonic Tully-Fisher v^4 = G M_B · cH/6\" as "
      "\"confirmed empirical relation\", while `papers/GR.md`:547 and `book/ch07-gravity.md`:299 give its "
      "normalization comparison as open.")
    a("- The #873 G3-SCOPE proposal (U2) classes v_flat and baryonic mass as raw-direct under §A.24. For the "
      "available high-z samples neither is: the velocities are model peak circular velocities with a "
      "pressure-support correction, and the gas masses come from a scaling relation (PREREG §3).")
    a("- The analytic ΛCDM halo scaling M_h = V³/(10 G H(z)) at fixed disk mass fraction predicts the same "
      "−log₁₀ E(z) shift as OI's asymptotic law, so a BTFR zero-point confirmation of that size would not "
      "discriminate OI from it.")
    a("")
    (UNIT / "RESULT.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()

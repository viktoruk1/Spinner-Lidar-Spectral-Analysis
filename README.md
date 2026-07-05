# Task 1 — SpinnerLidar Spectral Analysis

**Course:** Wind Physics Measurement Project (WPMP), Summer Semester 2026
**Institution:** Carl von Ossietzky Universität Oldenburg
**Group:** 4 — Victor Ukoha & Illechukwu Jackson

---

## What this project does

Reproduces the line-of-sight (LOS) wind speed from raw SpinnerLidar spectra and validates it against the lidar's own onboard value. Uses 1 second of measurement (312 laser shots, one per rosette-scan point) from a nacelle-mounted SpinnerLidar on turbine AV04 (Alpha Ventus offshore wind farm).

**End result:** centroid method matches the lidar to within ⅛ of a bin (R² = 1.00 after filtering); the filtered wind field reveals a wake from an upstream turbine.

---

## Repository structure

```
Task1_SpinnerLidar/
├── data/
│   ├── SpinnerLidar_Data_1s.txt         # metadata: 312 rows × 11 cols
│   └── SpinnerLidar_Spectra_1s.txt      # raw spectra: 312 rows × 256 bins
├── src/
│   ├── Task1_SpinnerLidar_SpectralAnalysis.ipynb   # main notebook
│   ├── Correlation.py                   # helper — scatter + regression
│   ├── Gauss_Fit_Peak.py                # helper — Gaussian peak fit
│   ├── Goodness_of_Fit.py               # helper — R², slope, intercept
│   └── Rosette_Scan_Plot.py             # helper — 2D wind field plot
├── results/figures/                     # exported plots
└── README.md
```

---

## How to run

**1. Environment** (Anaconda recommended):
```bash
conda create -n lidar python=3.11 numpy pandas scipy matplotlib jupyter -y
conda activate lidar
```

**2. Launch the notebook** from the `src/` folder:
```bash
jupyter notebook Task1_SpinnerLidar_SpectralAnalysis.ipynb
```

**3. Run all cells** (Kernel → Restart & Run All). All figures are saved to `../results/figures/`.

---

## The physics in one paragraph

The SpinnerLidar fires a laser upstream through the rotor. Aerosols moving with the wind scatter light back, Doppler-shifted. The frequency shift Δf gives the line-of-sight wind speed via

**v_LOS = ½ · Δf · λ**   (factor ½ from double-scattering; λ = 1560 nm)

Each spectrum has 256 frequency bins spanning a 50 MHz bandwidth → 0.152 m/s per bin. We find the peak location in each spectrum, convert it to m/s, and cross-check against the lidar's onboard value.

---

## The 5 steps of the analysis

| Step | What we did | Result |
|---|---|---|
| **1** | Subtract the median of each spectrum → removes the flat noise floor | Baseline at 0 for all 312 spectra |
| **2** | Convert bin number → frequency → wind speed | Δv ≈ 0.152 m/s per bin, range 0 → 38.8 m/s |
| **3** | Centroid method (power-weighted average) on ±15-bin window | Centroid matches lidar to ~0.02 m/s (⅛ of a bin) |
| **4** | Correlate with lidar's own v_LOS, filter outliers | 6 blade-reflection outliers rejected; R² 0.932 → 1.00 |
| **5** | Plot filtered wind field on the rosette scan | Wake from upstream turbine visible |

---

## Key finding — blade reflections

The 6 outliers weren't weak-signal shots. Every outlier spectrum contained a huge **DC spike near 0 m/s** on top of the true wind peak at ~9 m/s. Physical cause: a rotor blade of AV04 sweeping through the beam reflects light with essentially zero Doppler shift (tangential motion). The centroid gets pulled toward that spike. Filter used:

**|v_LOS,centroid − v_LOS,lidar| > 0.5 m/s → reject**

(0.5 m/s sits in the empty gap between good spectra, |Δ| < 0.1 m/s, and bad ones, |Δ| > 7 m/s.)

---

## Notes for future users

- The helper `Rosette_Scan_Plot.py` had to be patched — the original used the deprecated `fig.gca(projection='3d')` syntax. Fixed to use standard `pcolormesh`.
- Column meanings in the metadata file were verified via `describe()` — the original script comments had one column shifted.
- Peak-power thresholding was ineffective (all peaks were strong); residual-based filtering was used instead.
- Rosette plot uses cubic interpolation for a smoother visualisation.

---

## Deliverables

- **Notebook** — `Task1_SpinnerLidar_SpectralAnalysis.ipynb`, all 5 steps with commentary
- **Figures** — 6 plots in `results/figures/`
- **Presentation** — `Group4_Lidar_Task1.pptx` (10 slides)

---

## Contact

Paul Meyer — paul.meyer@uni-oldenburg.de (module coordinator)

# -*- coding: utf-8 -*-
"""
Correlation plot with clean formatting.
"""

import numpy as np
import matplotlib.pyplot as plt
from Goodness_of_Fit import Goodness_of_Fit


def Correlation(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    r2, slope, intercept, N, reg_str, corr_str, N_str = Goodness_of_Fit(a, b, 'linear')

    mask = ~np.isnan(a) & ~np.isnan(b)
    lo = float(min(np.min(a[mask]), np.min(b[mask]))) - 0.5
    hi = float(max(np.max(a[mask]), np.max(b[mask]))) + 0.5

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.scatter(a, b, s=25, alpha=0.7, color='steelblue',
               edgecolor='navy', linewidth=0.4, label='data', zorder=3)

    ax.plot([lo, hi], [lo, hi], color='black', linewidth=1.2,
            label='y = x', zorder=2)

    ax.plot([lo, hi], [slope*lo + intercept, slope*hi + intercept],
            color='crimson', linewidth=1.5, linestyle='--',
            label=f'fit: y = {slope:.3f} x + {intercept:.3f}', zorder=4)

    ax.set_xlabel(r'$v_{LOS}$  [m s$^{-1}$]  (SpinnerLidar)', fontsize=12)
    ax.set_ylabel(r'$v_{LOS}$  [m s$^{-1}$]  (Centroid)',     fontsize=12)

    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect('equal')

    stats_text = f"{corr_str.strip()}\n{N_str.strip()}"
    ax.text(0.03, 0.97, stats_text,
            transform=ax.transAxes, fontsize=11,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white',
                      edgecolor='gray', alpha=0.9))

    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig, ax
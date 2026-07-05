# -*- coding: utf-8 -*-
"""
Rosette scan wind field plot — modernised for matplotlib >= 3.4
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from scipy import interpolate


def Rosette_Scan_Plot(x, y, vlos, x_background, y_background):
    # Interpolate onto a regular grid so the colour surface looks smooth
    meshgridvector = np.arange(-40, 41, 2)
    xi, yi = np.meshgrid(meshgridvector, meshgridvector)

    # Combine x and y into (N, 2) point array — needed by griddata
    points = np.column_stack([np.asarray(x).flatten(),
                              np.asarray(y).flatten()])
    vlos_arr = np.asarray(vlos).flatten()

    # Drop NaN points before interpolating (blade-filtered spectra)
    good = ~np.isnan(vlos_arr)
    vlosi = interpolate.griddata(points[good], vlos_arr[good], (xi, yi),
                                 method='linear')

    # Set up the colour map
    vmin = np.nanmin(vlosi)
    vmax = np.nanmax(vlosi)
    norm = Normalize(vmin=vmin, vmax=vmax)
    scalarMap = cm.ScalarMappable(norm=norm, cmap='jet')

    # 2D plot (much easier to read than the old 3D version)
    fig, ax = plt.subplots(figsize=(8, 7))

    # Coloured wind field
    pcm = ax.pcolormesh(xi, yi, vlosi, cmap='jet',
                        norm=norm, shading='auto')

    # Overlay measurement points (kept ones)
    ax.plot(np.asarray(x).flatten()[good],
            np.asarray(y).flatten()[good],
            'o', color='black', markersize=2, alpha=0.4,
            label='kept measurements')

    # Overlay all background points (grey outline of full rosette)
    ax.plot(np.asarray(x_background).flatten(),
            np.asarray(y_background).flatten(),
            '.', color='grey', markersize=1, alpha=0.3)

    # Colorbar
    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical')
    cbar.set_label(r'$v_{LOS}$  [m s$^{-1}$]', fontsize=12)

    ax.set_xlabel('y [m]  (horizontal)', fontsize=12)
    ax.set_ylabel('z [m]  (vertical)',   fontsize=12)
    ax.set_title('SpinnerLidar rosette scan — line-of-sight wind field',
                 fontsize=12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return fig, ax
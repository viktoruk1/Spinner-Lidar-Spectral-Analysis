# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:50:35 2023

@author: tusha
"""


import pandas as pd
import numpy as np
from Correlation import Correlation
from Rosette_Scan_Plot import Rosette_Scan_Plot
from Gauss_Fit_Peak import Gauss_Fit_Peak
from Gauss_Fit_Peak import modalfun

# %%Reading the line-of-sight data of the SpinnerLidar
spinnerlidar_data = pd.read_csv('C:/PhD_Documents/Courses/UOl/SoSe 25/WPMP/Lidar module/Exercises (for Students)/Ex. 1/SpinnerLidar_Data_1s.txt', delimiter="\t", header=None)
spinnerlidar_spectra = pd.read_csv('C:/PhD_Documents/Courses/UOl/SoSe 25/WPMP/Lidar module/Exercises (for Students)/Ex. 1/SpinnerLidar_Spectra_1s.txt', delimiter="\t", header=None)

index = spinnerlidar_data.iloc[:,0]   # Lidar measurement index
vlos = spinnerlidar_data.iloc[:,2]    # Line-of-sight measurement
power = spinnerlidar_data.iloc[:4]    # Backscatter power
sx = spinnerlidar_data.iloc[:,6]      # Laser pointing unit vector x-component
sy = spinnerlidar_data.iloc[:,7]      # Laser pointing unit vector y-component
focus = spinnerlidar_data.iloc[:,8]   # Focus distance of Lidar

sz = np.sqrt(1-sx**2-sy**2)
x = pd.DataFrame(sz.values*focus.values)
y = pd.DataFrame(-sy.values*focus.values)
z = pd.DataFrame(sx.values*focus.values)

# %% Reading the spectrum data of the SpinnerLidar
bins = 256              # amount of bins in each spectrum
bandwidth = 50e+06      # frequency bandwith of the spectra
Lambda = 1560e-09       # wavelength of the laser light


# Calculate the frequency resolution of the spectra, the Doppler frequency 
# of each bin and from that the wind speed corresponding to each bin:
    
# f = ...
# v = ...
# vlos_calculated = ...   
    
# %% Finding the spectra peaks



# %% Plotting

#Correlation(vlos,vlos_calculated)

#Rosette_Scan_Plot(y, z, vlos_calculated, y, z)


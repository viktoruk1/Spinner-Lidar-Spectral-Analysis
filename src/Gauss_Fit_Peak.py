# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:50:35 2023

@author: tusha
"""
import numpy as np
from scipy.optimize import curve_fit

def modalfun(v, a, b, c):
    return a*np.exp(-(v - b)**2 / (2*(c**2)))
     

def Gauss_Fit_Peak(v,spectrum_measured,std_guess,peak_guess,v_guess):
    
    modelfun = lambda x: x[0]*np.exp(-(v - x[1])**2 / (2*(x[2]**2)))
    
    output = [peak_guess, v_guess, std_guess]
    a = peak_guess
    b = v_guess
    c = std_guess
    lb =     [1, 0 , 0]
    rb =     np.multiply(3,output)
    
    if np.any(lb==rb):
        p1 = np.nan
        p2 = np.nan
        p3 = np.nan
        
    else:
        popt, pcov = curve_fit(modalfun, v, spectrum_measured, p0=[a,b,c], bounds=(lb, rb))
        p1 = popt[0]
        p2 = popt[1]
        p3 = popt[2]
        
    return p1, p2, p3
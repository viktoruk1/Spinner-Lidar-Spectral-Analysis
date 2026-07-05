# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:42:10 2023

@author: tusha
"""

import numpy as np


def Goodness_of_Fit(x, y, method):
    
    nanindex = np.where(np.logical_and(~np.isnan(x), ~np.isnan(y)))
    N = len(nanindex[0])
    x = x[nanindex]
    y = y[nanindex]
    N_string = 'N = %d\n' % N
    
    # calculation of fit: y2 = ay1 + b
    fit_parameter = np.polyfit(x, y, 1)
    a = fit_parameter[0]
    b = fit_parameter[1]

    regression_string = 'y = {} x + ({})'.format(np.round(a,4), np.round(b,4))
    
    if method == 'correlation':
        # Coefficient of determination of a correlation
        sigma_squared_xy = 1/(N-2) * np.sum((y - x)**2)
        sigma_squared_yy = 1/(N-1) * np.sum((y - np.mean(y))**2)
        correlation_coefficient = 1 - (sigma_squared_xy/sigma_squared_yy)
        correlation_string = 'R-sq. = {}'.format(np.round(correlation_coefficient, 3))
        
    elif method == 'linear':
        # Coefficient of determination of a linear fit
        sigma_squared_xy = 1/(N-2) * np.sum((y - (a*x + b))**2)
        sigma_squared_yy = 1/(N-1) * np.sum((y - np.mean(y))**2)
        correlation_coefficient = 1 - (sigma_squared_xy/sigma_squared_yy)
        # correlation_string = 'R-sq. = %d' % correlation_coefficient
        correlation_string = 'R-sq. = {}'.format(np.round(correlation_coefficient, 3))
        
    elif method == 'Pearson':
        sigma_matrix = np.sqrt(np.cov(x, y))
        correlation_coefficient = (sigma_matrix[0,1]*sigma_matrix[1,0]) / (sigma_matrix[0,0]*sigma_matrix[1,1])
        correlation_string = 'rho_{xy} = %d' %correlation_coefficient
        
    else:
        print('No method is passed!')
    
    return correlation_coefficient, a, b, N, regression_string, correlation_string, N_string

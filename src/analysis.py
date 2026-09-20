"""
Анализ результатов.
"""

import numpy as np
from scipy.stats import linregress


def btfr_analysis(M_b, v0):
    """
    Анализ барионного соотношения Талли-Фишера.
    
    Parameters
    ----------
    M_b : array-like
        Барионная масса галактик (M_sun)
    v0 : array-like
        Характеристическая скорость (км/с)
    
    Returns
    -------
    result : dict
        Словарь с результатами: alpha, beta, r_value, p_value
    """
    log_M = np.log10(M_b)
    log_v4 = np.log10(np.asarray(v0)**4)
    
    slope, intercept, r_value, p_value, std_err = linregress(log_M, log_v4)
    
    return {
        'alpha': slope,           # должно быть ~1
        'beta': intercept,
        'r_value': r_value,
        'r_squared': r_value**2,
        'p_value': p_value,
        'std_err': std_err,
    }
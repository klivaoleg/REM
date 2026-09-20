"""
Функции для подгонки моделей к данным.
"""

from scipy.optimize import curve_fit
import numpy as np


def fit_v0(v_visible, v_obs, v_err=None):
    """
    Подгоняет v0 к наблюдаемым данным.
    
    Parameters
    ----------
    v_visible : array-like
        Скорость от видимого вещества
    v_obs : array-like
        Наблюдаемая скорость
    v_err : array-like, optional
        Погрешности измерений
    
    Returns
    -------
    v0 : float
        Оптимальное значение v0
    v0_err : float
        Погрешность v0
    """
    from .models import v_model
    
    if v_err is None:
        popt, pcov = curve_fit(v_model, v_visible, v_obs)
    else:
        popt, pcov = curve_fit(v_model, v_visible, v_obs, sigma=v_err)
    
    v0 = popt[0]
    v0_err = np.sqrt(pcov[0, 0])
    return v0, v0_err


def compute_chi2(v_obs, v_model_pred, v_err=None):
    """
    Вычисляет хи-квадрат.
    """
    v_obs = np.asarray(v_obs)
    v_model_pred = np.asarray(v_model_pred)
    
    if v_err is None:
        v_err = np.ones_like(v_obs)
    
    residuals = (v_obs - v_model_pred) / v_err
    return np.sum(residuals**2)
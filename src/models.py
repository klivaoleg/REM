"""
Математические модели для проекта Elastic Spacetime.

Содержит:
- v_model: наша модель упругого пространства-времени
- v_dm_model: модель с тёмной материей (изотермическое гало)
"""

import numpy as np


def v_model(v_visible, v0):
    """
    Наша модель: v(r) = sqrt(v_visible(r)^2 + v0^2)
    
    Parameters
    ----------
    v_visible : array-like
        Скорость от видимого вещества (звёзды + газ) на разных радиусах
    v0 : float
        Характеристическая скорость упругого провиса (км/с)
    
    Returns
    -------
    v : array-like
        Предсказанная моделью скорость вращения
    """
    return np.sqrt(np.asarray(v_visible)**2 + v0**2)


def v_dm_model(r, rho0, rh):
    """
    Модель с тёмной материей (изотермическое гало).
    
    v_DM^2 = 4*pi*G*rho0*rh^3/r * [arctan(r/rh) - (r/rh)/(1+(r/rh)^2)]
    
    Parameters
    ----------
    r : array-like
        Радиус (кпк)
    rho0 : float
        Центральная плотность гало
    rh : float
        Характеристический радиус гало (кпк)
    
    Returns
    -------
    v_dm : array-like
        Скорость от тёмной материи
    """
    r = np.asarray(r)
    x = r / rh
    # Коэффициент 4*pi*G в удобных единицах: 
    # G = 4.3e-6 кпк*(км/с)^2/M_sun, rho0 в M_sun/пк^3
    # Нужна аккуратная работа с единицами — пока заглушка
    G_units = 4.3009e-6  # кпк * (км/с)^2 / M_sun
    factor = 4 * np.pi * G_units * rho0 * rh**3
    v_dm_sq = factor / r * (np.arctan(x) - x / (1 + x**2))
    return np.sqrt(np.maximum(v_dm_sq, 0))
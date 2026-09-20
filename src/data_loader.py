"""
Загрузка данных SPARC.

Формат файлов:
- Каждый файл .dat содержит кривую вращения одной галактики
- Имя файла = имя галактики (например, NGC3198.dat)
- Столбцы: Rad, Vobs, errV, Vgas, Vdisk, Vbul, SBdisk, SBbul
- Строки с # — комментарии
"""

import os
import numpy as np
import pandas as pd


def load_rotation_curve(galaxy_name, data_dir='data/raw/SPARC'):
    """
    Загружает кривую вращения для конкретной галактики.
    
    Parameters
    ----------
    galaxy_name : str
        Имя галактики (например, 'NGC3198')
    data_dir : str
        Путь к папке с данными
    
    Returns
    -------
    data : dict
        Словарь с массивами:
        - r: радиус (кпк)
        - v_obs: наблюдаемая скорость (км/с)
        - v_err: погрешность (км/с)
        - v_gas: вклад газа (км/с)
        - v_disk: вклад диска (км/с)
        - v_bul: вклад балджа (км/с)
        - v_visible: полная видимая скорость (км/с)
    """
    path = os.path.join(data_dir, f'{galaxy_name}.dat')
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    # Загружаем данные (пропускаем строки с #)
    data_raw = np.loadtxt(path, comments='#')
    
    # Извлекаем столбцы
    r = data_raw[:, 0]           # радиус (кпк)
    v_obs = data_raw[:, 1]       # наблюдаемая скорость (км/с)
    v_err = data_raw[:, 2]       # погрешность
    v_gas = data_raw[:, 3]       # вклад газа
    v_disk = data_raw[:, 4]      # вклад диска
    v_bul = data_raw[:, 5]       # вклад балджа
    
    # Видимая скорость = sqrt(v_gas^2 + v_disk^2 + v_bul^2)
    v_visible = np.sqrt(v_gas**2 + v_disk**2 + v_bul**2)
    
    return {
        'r': r,
        'v_obs': v_obs,
        'v_err': v_err,
        'v_gas': v_gas,
        'v_disk': v_disk,
        'v_bul': v_bul,
        'v_visible': v_visible,
    }


def list_galaxies(data_dir='data/raw/SPARC'):
    """
    Возвращает список всех галактик в базе SPARC.
    
    Returns
    -------
    galaxies : list
        Список имён галактик (без расширения .dat)
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Папка не найдена: {data_dir}")
    
    files = [f.replace('.dat', '') for f in os.listdir(data_dir) if f.endswith('.dat')]
    return sorted(files)
"""
Загрузка данных SPARC.
"""

import os
import numpy as np
import pandas as pd


def load_sparc_catalog(data_dir='data/raw'):
    """
    Загружает основной каталог SPARC (data.csv).
    
    Returns
    -------
    catalog : pd.DataFrame
        Каталог галактик с параметрами
    """
    path = os.path.join(data_dir, 'data.csv')
    # SPARC использует пробелы как разделители
    catalog = pd.read_csv(path, sep=',')  # или sep='\s+' если нужно
    return catalog


def load_rotation_curve(galaxy_name, data_dir='data/raw'):
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
        Словарь с массивами: r, v_obs, v_err, v_star, v_gas
    """
    # Файлы в SPARC называются типа RC_GC_data.dat
    # Точное имя нужно будет уточнить после скачивания данных
    path = os.path.join(data_dir, f'{galaxy_name}', 'RC_GC_data.dat')
    
    # Формат: R Vobs Vobs_err Vstar Vgas (и другие столбцы)
    data_raw = np.loadtxt(path, comments='#')
    
    return {
        'r': data_raw[:, 0],       # радиус (кпк)
        'v_obs': data_raw[:, 1],   # наблюдаемая скорость (км/с)
        'v_err': data_raw[:, 2],   # погрешность
        'v_star': data_raw[:, 3],  # вклад звёзд
        'v_gas': data_raw[:, 4],   # вклад газа
    }
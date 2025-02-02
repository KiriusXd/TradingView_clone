# app/services/ta_lib_utils.py
import talib
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=100)
def calculate_indicator(indicator_name: str, close_prices: np.ndarray, **params):
    if not hasattr(talib, indicator_name):
        raise ValueError(f"Индикатор {indicator_name} не поддерживается.")
    func = getattr(talib, indicator_name)
    return func(close_prices, **params)

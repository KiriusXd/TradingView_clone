# app/core/cache.py
from cachetools import cached, TTLCache

ohlcv_cache = TTLCache(maxsize=100, ttl=300)  # Кеш на 5 минут


@cached(ohlcv_cache)
async def get_cached_ohlcv(symbol: str, timeframe: str):
    # Запрос к базе данных или Bybit
    pass

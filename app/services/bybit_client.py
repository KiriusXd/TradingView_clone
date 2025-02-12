# app/services/bybit_client.py
import ccxt.async_support as ccxt
from ..core.config import settings


class BybitClient:
    def __init__(self):
        # Берем ключи из config.ini
        bybit_config = settings.get_bybit_keys()
        self.exchange = ccxt.bybit({
            'apiKey': bybit_config["api_key"],
            'secret': bybit_config["api_secret"],
            'enableRateLimit': True,
        })

    # app/services/bybit_client.py


async def fetch_ohlcv(self, symbol: str, timeframe: str = '1h', limit: int = 100):
    try:
        data = await self.exchange.fetch_ohlcv(symbol, timeframe, limit)
        if not data:
            return []
        return data
    except ccxt.NetworkError as e:
        print(f"Ошибка сети: {e}")
        return []

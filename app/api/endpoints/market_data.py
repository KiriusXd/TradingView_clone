# app/api/endpoints/market_data.py
from fastapi import APIRouter, HTTPException
from app.services.bybit_client import BybitClient
from app.core.config import logger

router = APIRouter(prefix="/api")  # Все эндпоинты будут начинаться с /api


@router.get("/ohlcv/{symbol}", tags=["Market Data"])
async def get_ohlcv(symbol: str, timeframe: str = "1h"):
    logger.info(f"Запрос OHLCV для {symbol} ({timeframe})")
    try:
        async with BybitClient() as client:
            data = await client.fetch_ohlcv(symbol, timeframe)
            if not data:
                logger.warning(f"Нет данных для {symbol}")
                return []
            return data
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

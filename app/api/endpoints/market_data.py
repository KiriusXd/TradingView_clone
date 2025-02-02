# app/api/endpoints/market_data.py
from fastapi import APIRouter
from app.services.bybit_client import BybitClient
from app.services.database import get_db

router = APIRouter()


@router.get("/ohlcv/{symbol}")
async def get_ohlcv(symbol: str, timeframe: str = "1h"):
    async with BybitClient() as client:
        data = await client.fetch_ohlcv(symbol, timeframe)
    return data

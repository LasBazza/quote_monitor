import asyncio

from aiohttp import ClientSession
from fastapi import APIRouter

from core.config import settings

router = APIRouter()

main_session = ClientSession()


async def send_request(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()


@router.get('/stocks')
async def stocks(ticker: str):
    params = {
        'function': settings.QUOTE_FUNCTION,
        'apikey': settings.API_KEY,
        'symbol': ticker
    }
    async with main_session:
        return await send_request(main_session, url=settings.BASE_URL, params=params)


@router.get('/currency')
async def quotes(to_currency: str, from_currency: str):
    params = {
        'function': settings.CURRENCY_FUNCTION,
        'apikey': settings.API_KEY,
        'from_currency': from_currency,
        'to_currency': to_currency
    }
    async with main_session:
        return await send_request(main_session, url=settings.BASE_URL, params=params)

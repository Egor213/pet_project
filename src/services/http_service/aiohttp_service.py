import asyncio

import aiohttp

from .base import BaseHttpService


class AioHttpService(BaseHttpService):
    def __init__(self, max_connections: int = 10, timeout: int = 10):
        self._connector = aiohttp.TCPConnector(limit=max_connections)
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._session = None

    def start(self):
        if self._session is None:
            self._session = aiohttp.ClientSession(
                connector=self._connector, timeout=self._timeout
            )

    def _check_session(self):
        if self._session is None:
            raise RuntimeError("Service not started")

    async def _parse_response(self, resp):
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return await resp.json()
        elif "text/" in content_type:
            return await resp.text()
        else:
            return await resp.read()

    async def get(self, url, params=None, **kwargs):
        self._check_session()
        async with self._session.get(url, params=params, **kwargs) as resp:
            resp.raise_for_status()
            return await self._parse_response(resp)

    async def post(self, url, data=None, json=None, **kwargs):
        self._check_session()
        async with self._session.post(url, data=data, json=json, **kwargs) as resp:
            resp.raise_for_status()
            return await self._parse_response(resp)

    async def close(self):
        if self._session:
            await self._session.close()
            self._session = None

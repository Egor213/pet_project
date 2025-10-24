import pytest
import asyncio
from unittest.mock import AsyncMock

from src.services.http_service.aiohttp_service import AioHttpService
from src.services.pool_service.async_pool_service import AsyncPoolService
from src.services.parce_contract_service.parce_site_service import ParceSiteService



@pytest.fixture
async def http_service():
    service = AioHttpService()
    service.start()
    yield service
    await service.close()


@pytest.fixture
def pool_service(http_service):
    async_pool = AsyncPoolService(
        handler=AsyncMock(),
        num_workers=2,
        max_wait_time=10,
        http_service=http_service,
    )
    return async_pool


@pytest.fixture
def parce_site_service(pool_service, mocker):
    repo = mocker.AsyncMock()
    service = ParceSiteService(contract_repository=repo, pool_service=pool_service)
    return service

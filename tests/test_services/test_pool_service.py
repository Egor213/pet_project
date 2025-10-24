import pytest
import asyncio
from src.services.pool_service.async_pool_service import AsyncPoolService
from src.processing_site.dto_workers import ParceSiteDto


@pytest.mark.asyncio
async def test_pool_add_task_and_result(mocker):
    async def handler(dto: ParceSiteDto):
        return dto.url_site.upper()

    pool = AsyncPoolService(handler=handler, num_workers=2)
    await pool.run()
    await pool.add_task(ParceSiteDto(url_site="http://test.com", id="123"))
    res = await pool.get_result()
    await pool.stop()
    assert res == "HTTP://TEST.COM"

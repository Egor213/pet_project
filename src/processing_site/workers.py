import asyncio

from .dto_workers import ParceSiteDto


async def parce_site_worker(pasrce_site_dto: ParceSiteDto):
    print(f"Start: {pasrce_site_dto.url_site}")
    await asyncio.sleep(3)
    print(f"Done: {pasrce_site_dto.url_site}")

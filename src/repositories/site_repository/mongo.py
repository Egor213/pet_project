from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorClient

from .base import BaseSiteRepository


@dataclass
class MongoSiteRepository(BaseSiteRepository):
    mongo_db_client: AsyncIOMotorClient
    mongo_db_db_name: str
    mongo_db_collection_name: str


    async def temp():
        ...
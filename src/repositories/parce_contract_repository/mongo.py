from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorClient

from src.repositories.main import BaseMongoDBRepository
from .base import BaseParceSiteRepository


@dataclass
class MongoParceSiteRepository(BaseParceSiteRepository, BaseMongoDBRepository):
    mongo_db_client: AsyncIOMotorClient
    mongo_db_db_name: str
    mongo_db_collection_name: str


    async def get_all_contracts(self):
        return await self._collection.find().to_list(None)
from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import InsertOneResult, UpdateResult

from src.repositories.main import BaseMongoDBRepository

from .base import BaseParceSiteRepository


@dataclass
class MongoParceSiteRepository(BaseParceSiteRepository, BaseMongoDBRepository):
    mongo_db_client: AsyncIOMotorClient
    mongo_db_db_name: str
    mongo_db_collection_name: str

    async def get_all_contracts(self) -> list[dict]:
        return await self._collection.find().to_list(None)

    async def get_contract_by_id(self, contract_id: str) -> dict:
        return await self._collection.find_one({"id": contract_id})

    async def create_contract(self, contract: dict) -> InsertOneResult:
        return await self._collection.insert_one(contract)

    async def replace_contract(self, new_contract: dict) -> UpdateResult:
        return await self._collection.replace_one(
            {"id": new_contract["id"]}, new_contract
        )

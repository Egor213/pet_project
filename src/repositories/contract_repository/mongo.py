from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorClient

from src.repositories.main import BaseMongoDBRepository
from .base import BaseContractRepository


@dataclass
class MongoContractRepository(BaseContractRepository, BaseMongoDBRepository):
    mongo_db_client: AsyncIOMotorClient
    mongo_db_db_name: str
    mongo_db_collection_name: str


    async def create_temp(self) -> None:
        return await self._collection.insert_one({
            "test": "test",
            "test2": "test2",
            "test3": "test3",
            "test4": "test4",
            "test5": "test5",
            "test6": "test6",
            "test7": "test7",
            "test8": "test8",
            "test9": "test9",
            "test10": "test10",
            "test11": "test11",
            "test12": "test12",
            "test13": "test13",
            "test14": "test14",
            "test15": "test15",
            "test16": "test16",
            "test17": "test17",
            "test18": "test18",
            "test19": "test19",
            "test20": "test20",
            "test21": "test21",
            "test22": "test22",
            "test23": "test23",
            "test24": "test24",
            "test25": "test25",
            "test26": "test26",
            
        })
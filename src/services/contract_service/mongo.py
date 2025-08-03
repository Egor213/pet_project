from dataclasses import dataclass
from .base import BaseContractService
from src.repositories.contract_repository import MongoContractRepository

@dataclass
class MongoContractService(BaseContractService):
    contract_repository: MongoContractRepository
    
    async def temp():
        ...
    
    async def create_temp(self) -> None:
        return await self.contract_repository.create_temp()
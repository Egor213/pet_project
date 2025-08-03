from dataclasses import dataclass
from .base import BaseContractService
from src.repositories.contract_repository import MongoContractRepository

@dataclass
class MongoContractService(BaseContractService):
    contract_repository: MongoContractRepository
    
    async def temp():
        ...
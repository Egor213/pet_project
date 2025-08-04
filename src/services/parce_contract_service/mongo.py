from dataclasses import dataclass
from .base import BaseParceSiteService
from src.repositories.parce_contract_repository import MongoParceSiteRepository

@dataclass
class MongoParceSiteService(BaseParceSiteService):
    contract_repository: MongoParceSiteRepository
    
    async def temp():
        ...
    
    async def create_temp(self) -> None:
        return await self.contract_repository.create_temp()
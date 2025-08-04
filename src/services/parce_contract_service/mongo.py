from dataclasses import dataclass
from .base import BaseParceSiteService
from src.repositories.parce_contract_repository import MongoParceSiteRepository

@dataclass
class MongoParceSiteService(BaseParceSiteService):
    contract_repository: MongoParceSiteRepository
    
    async def get_all_contracts(self):
        return await self.contract_repository.get_all_contracts()
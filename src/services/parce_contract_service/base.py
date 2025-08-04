from dataclasses import dataclass
from abc import ABC, abstractmethod

from src.entity import ParceSiteContract


@dataclass
class BaseParceSiteService(ABC):
    @abstractmethod
    async def get_all_contracts() -> list[dict]:
        ...


    @abstractmethod
    async def get_contract_by_id(self, contract_id: str) -> dict:
        ...
    
    
    @abstractmethod
    async def create_contract(self, url_site: str) -> ParceSiteContract:
        ...

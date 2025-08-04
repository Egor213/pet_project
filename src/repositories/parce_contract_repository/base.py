from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymongo.results import InsertOneResult


@dataclass
class BaseParceSiteRepository(ABC):
    @abstractmethod
    async def get_all_contracts() -> dict: ...

    @abstractmethod
    async def get_contract_by_id(self, contract_id: str) -> dict: ...

    @abstractmethod
    async def create_contract(self, contract: dict) -> InsertOneResult: ...

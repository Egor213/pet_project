from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseParceSiteRepository(ABC):
    @abstractmethod
    async def get_all_contracts() -> dict():
        ...
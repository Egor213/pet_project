from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseParceSiteRepository(ABC):
    @abstractmethod
    async def create_temp():
        ...
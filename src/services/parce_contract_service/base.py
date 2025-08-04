from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseParceSiteService(ABC):
    @abstractmethod
    async def temp():
        ...
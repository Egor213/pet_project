from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseSiteRepository(ABC):
    @abstractmethod
    async def temp():
        ...
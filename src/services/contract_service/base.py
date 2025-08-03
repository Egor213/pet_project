from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseContractService(ABC):
    @abstractmethod
    async def temp():
        ...
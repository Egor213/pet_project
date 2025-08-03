from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseContractRepository(ABC):
    @abstractmethod
    async def create_temp():
        ...
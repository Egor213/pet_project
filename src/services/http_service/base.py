import typing as tp
from abc import ABC, abstractmethod


class BaseHttpService(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    async def get(self, url: str, params: dict[str, tp.Any], **kwargs) -> tp.Any:
        pass

    @abstractmethod
    async def post(
        self, url: str, data: tp.Any | None = None, json: tp.Any | None = None, **kwargs
    ) -> tp.Any:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

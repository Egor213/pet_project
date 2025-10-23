import typing as tp
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class BasePoolService(ABC):

    @abstractmethod
    def add_result_handler(self, result_handler: tp.Callable):
        pass

    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    async def add_task(self, task_dto):
        pass

    @abstractmethod
    async def stop(self):
        pass

    @abstractmethod
    async def get_result(self):
        pass

    @abstractmethod
    def get_output_queue(self):
        pass

    @abstractmethod
    def get_input_queue(self):
        pass

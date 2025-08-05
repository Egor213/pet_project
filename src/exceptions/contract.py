from dataclasses import dataclass

from .base import LogicException, ApplicationException


@dataclass(eq=False)
class NotFoundContract(LogicException):
    @property
    def message(self):
        return 'Контракт не найден'

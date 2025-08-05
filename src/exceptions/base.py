from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationException(Exception):
    text: str = ""
    @property
    def message(self):
        return 'Произошла ошибка приложения'


@dataclass(eq=False)
class LogicException(Exception):
    text: str = ""
    @property
    def message(self):
        return 'В обработки запроса возникла ошибка'


@dataclass(eq=False)
class ValidationError(ApplicationException):
    @property
    def message(self):
        return f'Ошибка валидации. {self.text}'
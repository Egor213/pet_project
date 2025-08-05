from functools import wraps
from fastapi import status, responses

from src.exceptions.contract import ApplicationException, LogicException, NotFoundContract

def exception_handler(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        try:
            return await function(*args, **kwargs)
        except NotFoundContract as exception:
            return responses.JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": exception.message})
        except ApplicationException as exception:
            return responses.JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": exception.message})
    return wrapper

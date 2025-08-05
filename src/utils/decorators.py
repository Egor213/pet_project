from functools import wraps
from fastapi import status, responses


# TODO: пока так, но, возможно, надо сделать более частные ошибки
def exception_handler(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        try:
            return await function(*args, **kwargs)
        except Exception as exception:
            return responses.JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exception)})

    return wrapper

from fastapi import routing

v1_router = routing.APIRouter(
    prefix="/v1",
)

from .handlers.test import test_router

v1_router.include_router(test_router)
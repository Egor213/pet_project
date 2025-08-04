from fastapi import routing

v1_router = routing.APIRouter(
    prefix="/v1",
)

from .health_check import health_check_router
from .parce_contract import test_router

v1_router.include_router(test_router)
v1_router.include_router(health_check_router)

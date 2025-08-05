from fastapi import routing

v1_router = routing.APIRouter(
    prefix="/v1",
)

from .contracts import contract_router
from .health_check import health_check_router

v1_router.include_router(contract_router)
v1_router.include_router(health_check_router)

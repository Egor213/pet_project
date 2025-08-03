from fastapi import Depends, routing

from src.api import container
from src.services.contract_service import BaseContractService


test_router = routing.APIRouter(
    tags=["test"],
)

def contract_service() -> BaseContractService:
    return container.resolve(BaseContractService)

@test_router.get("/test")
async def test(service: BaseContractService = Depends(contract_service)) -> dict:
    await service.create_temp()
    return {"test": "test3"}
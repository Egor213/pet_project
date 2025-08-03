from fastapi import Depends, routing

from src.api import container
from src.services.contract_service import BaseContractService


test_router = routing.APIRouter(
    tags=["test"],
)

def contract_service() -> BaseContractService:
    return container.resolve(BaseContractService)

@test_router.get("/test")
async def test(container: BaseContractService = Depends(contract_service)) -> dict:
    # config = container.resolve(Config)
    # print(config)
    print(type(container))
    return {"test": "test3"}
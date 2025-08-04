from fastapi import Depends, routing

from src.api import container
from src.services.parce_contract_service import BaseParceSiteService


test_router = routing.APIRouter(
    tags=["test"],
)

def contract_service() -> BaseParceSiteService:
    return container.resolve(BaseParceSiteService)

@test_router.get("/test")
async def test(service: BaseParceSiteService = Depends(contract_service)) -> dict:
    res = await service.get_all_contracts()
    print(res)
    print(type(res[0]))
    return {"test": "test"}
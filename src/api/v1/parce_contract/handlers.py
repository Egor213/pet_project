from fastapi import Depends, routing

from .schemas import CreateContractSchema

from src.api import container
from src.services.parce_contract_service import BaseParceSiteService


test_router = routing.APIRouter(
    tags=["test"],
)

def contract_service() -> BaseParceSiteService:
    return container.resolve(BaseParceSiteService)

@test_router.get("/create_site_contract/{url_site}")
async def create_site_contract_handler(
    url_site: str,
    service: BaseParceSiteService = Depends(contract_service)
) -> CreateContractSchema:
    contract = await service.create_contract(url_site=url_site)
    return CreateContractSchema.from_entity(contract)
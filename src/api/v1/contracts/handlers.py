import punq
from fastapi import Depends, Query, routing, status
from pydantic import HttpUrl

from src.api.schemas import ErrorSchema
from src.app.init import init_container
from src.services.parce_contract_service import ParceSiteService
from src.utils.decorators import exception_handler

from .schemas import ContractSchema, CreateContractSchema

contract_router = routing.APIRouter(
    tags=["contracts"],
    prefix="/contracts",
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
        status.HTTP_404_NOT_FOUND: {"model": ErrorSchema},
    },
)


@contract_router.post(
    "/parce_site",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": CreateContractSchema},
    },
)
@exception_handler
async def create_site_contract_handler(
    url_site: HttpUrl = Query(..., example="https://example.com"),
    container: punq.Container = Depends(init_container),
) -> CreateContractSchema:
    service = container.resolve(ParceSiteService)
    contract = await service.create_contract(url_site=str(url_site))
    return CreateContractSchema.from_entity(contract)


@contract_router.get(
    "/parce_site/{contract_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ContractSchema},
    },
)
@exception_handler
async def get_site_contract_handler(
    contract_id: str,
    container: punq.Container = Depends(init_container),
) -> ContractSchema:
    service = container.resolve(ParceSiteService)
    contract = await service.get_contract_by_id(contract_id=contract_id)
    return ContractSchema.from_entity(contract)


@contract_router.get(
    "/parce_site",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ContractSchema},
    },
)
@exception_handler
async def get_all_site_contracts_handler(
    container: punq.Container = Depends(init_container),
) -> list[ContractSchema]:
    service = container.resolve(ParceSiteService)
    contracts = await service.get_all_contracts()
    return [ContractSchema.from_entity(contract) for contract in contracts]


@contract_router.post("/test")
async def test(test: str, container: punq.Container = Depends(init_container)):
    from src.processing_site.dto_workers import ParceSiteDto
    from src.services import BasePoolService

    async_pool_service = container.resolve(BasePoolService)
    for i in range(100):
        await async_pool_service.add_task(ParceSiteDto(url_site=test + str(i)))
    return {"test": test}

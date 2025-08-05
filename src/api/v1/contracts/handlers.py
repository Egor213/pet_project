from fastapi import Depends, routing, status, Path
from pydantic import HttpUrl

from src.api import container
from src.services.parce_contract_service import BaseParceSiteService
from src.utils.decorators import exception_handler
from src.api.schemas import ErrorSchema

from .schemas import CreateContractSchema, ContractSchema

contract_router = routing.APIRouter(
    tags=["contracts"],
    prefix="/contracts",
)


def contract_service() -> BaseParceSiteService:
    return container.resolve(BaseParceSiteService)


@contract_router.post(
    "/parce_site/{url_site}",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": CreateContractSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
@exception_handler
async def create_site_contract_handler(
    url_site: HttpUrl = Path(example="https://example.com"),
    service: BaseParceSiteService = Depends(contract_service),
) -> CreateContractSchema:
    contract = await service.create_contract(url_site=url_site)
    return CreateContractSchema.from_entity(contract)


@contract_router.get(
    "/parce_site/{contract_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ContractSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
        status.HTTP_404_NOT_FOUND: {"model": ErrorSchema},
    },
)
@exception_handler
async def get_site_contract_handler(
    contract_id: str,
    service: BaseParceSiteService = Depends(contract_service),
) -> ContractSchema:
    contract = await service.get_contract_by_id(contract_id=contract_id)
    return ContractSchema.from_entity(contract)


@contract_router.get(
    "/parce_site",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": ContractSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
        status.HTTP_404_NOT_FOUND: {"model": ErrorSchema},
    },
)
@exception_handler
async def get_all_site_contracts_handler(
    service: BaseParceSiteService = Depends(contract_service),
) -> list[ContractSchema]:
    contracts = await service.get_all_contracts()
    return [ContractSchema.from_entity(contract) for contract in contracts]

from dataclasses import dataclass

from src.entity import ParceSiteContract
from src.repositories.parce_contract_repository import BaseParceSiteRepository
from src.services.validators import validate_found_entity, validate_uuid
from src.processing_site.dto_workers import ParceSiteDto
from src.services import AsyncPoolService, BasePoolService

from .converters import (convert_document_to_parce_site_contract,
                         convert_parce_site_contract_to_document)


@dataclass
class ParceSiteService:
    contract_repository: BaseParceSiteRepository
    pool_service: BasePoolService

    async def get_all_contracts(self):
        contracts_list = await self.contract_repository.get_all_contracts()
        validate_found_entity(contracts_list)
        return [convert_document_to_parce_site_contract(c) for c in contracts_list]

    async def get_contract_by_id(self, contract_id: str) -> dict:
        validate_uuid(contract_id)
        contract = await self.contract_repository.get_contract_by_id(contract_id)
        validate_found_entity(contract)
        return convert_document_to_parce_site_contract(contract)

    async def create_contract(self, url_site: str) -> ParceSiteContract:
        contract = ParceSiteContract.create_contract(url_site)
        # По хорошему тут нужна валидация, создалось ли вообще?
        await self.contract_repository.create_contract(
            convert_parce_site_contract_to_document(contract),
        )
        await self.pool_service.add_task(ParceSiteDto(url_site=url_site, id=contract.id))
        return contract

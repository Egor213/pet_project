from dataclasses import dataclass
from datetime import datetime

from src.entity import ParceSiteContract
from src.processing_site.dto_workers import ParceSiteDto, ParceSiteResultDto
from src.repositories.parce_contract_repository import BaseParceSiteRepository
from src.services.pool_service import BasePoolService
from src.services.validators import validate_found_entity, validate_uuid

from .converters import (
    convert_document_to_parce_site_contract,
    convert_parce_site_contract_to_document,
    convert_parce_site_result_dto_to_dict,
    merge_dict_fields,
)


@dataclass
class ParceSiteService:
    contract_repository: BaseParceSiteRepository
    pool_service: BasePoolService

    async def get_all_contracts(self):
        contracts_list = await self.contract_repository.get_all_contracts()
        validate_found_entity(contracts_list)
        return [convert_document_to_parce_site_contract(c) for c in contracts_list]

    async def get_contract_by_id(self, contract_id: str) -> ParceSiteContract:
        validate_uuid(contract_id)
        contract = await self.contract_repository.get_contract_by_id(contract_id)
        validate_found_entity(contract)
        return convert_document_to_parce_site_contract(contract)

    async def finalize_contract(self, parce_site_dto: ParceSiteResultDto):
        # TODO: Можно улучшить
        contract = await self.get_contract_by_id(parce_site_dto.id)
        contract_dict = convert_parce_site_contract_to_document(contract)
        new_data_dict = convert_parce_site_result_dto_to_dict(parce_site_dto)
        new_data_dict["updated_at"] = datetime.now()
        if new_data_dict["error"] is not None:
            new_data_dict["status"] = "failed"
        else:
            new_data_dict["status"] = "success"
        res_contract_dict = merge_dict_fields(new_data_dict, contract_dict)
        print(res_contract_dict)
        await self.contract_repository.replace_contract(res_contract_dict)

    async def create_contract(self, url_site: str) -> ParceSiteContract:
        contract = ParceSiteContract.create_contract(url_site)
        # По хорошему тут нужна валидация, создалось ли вообще?
        await self.contract_repository.create_contract(
            convert_parce_site_contract_to_document(contract),
        )
        await self.pool_service.add_task(
            ParceSiteDto(url_site=url_site, id=contract.id)
        )
        return contract

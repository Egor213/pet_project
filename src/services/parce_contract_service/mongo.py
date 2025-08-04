from dataclasses import dataclass

from src.entity import ParceSiteContract
from src.repositories.parce_contract_repository import MongoParceSiteRepository

from .base import BaseParceSiteService
from .converters import convert_parce_site_contract_to_document


@dataclass
class MongoParceSiteService(BaseParceSiteService):
    contract_repository: MongoParceSiteRepository

    async def get_all_contracts(self):
        return await self.contract_repository.get_all_contracts()

    async def get_contract_by_id(self, contract_id: str) -> dict:
        return await self.contract_repository.get_contract_by_id(contract_id)

    async def create_contract(self, url_site: str) -> ParceSiteContract:
        contract = ParceSiteContract.create_contract(url_site)
        await self.contract_repository.create_contract(
            convert_parce_site_contract_to_document(contract),
        )
        # TODO: добавить обработку контрактов
        return contract

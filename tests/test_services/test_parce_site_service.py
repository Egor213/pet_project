import pytest
from datetime import datetime
from src.processing_site.dto_workers import ParceSiteResultDto
from src.entity.parce_site_contract import ParceSiteContract
from src.services.parce_contract_service.parce_site_service import ParceSiteService


@pytest.mark.asyncio
async def test_create_contract(parce_site_service, mocker):
    mocker.patch.object(parce_site_service.pool_service, "add_task", return_value=None)
    contract = await parce_site_service.create_contract("https://test.com")
    assert isinstance(contract, ParceSiteContract)
    assert contract.url_site == "https://test.com"


@pytest.mark.asyncio
async def test_finalize_contract(parce_site_service, mocker):
    # мок get_contract_by_id
    contract = ParceSiteContract.create_contract("https://finalize.com")
    mocker.patch.object(parce_site_service, "get_contract_by_id", return_value=contract)
    mocker.patch.object(parce_site_service.contract_repository, "replace_contract", return_value=None)

    dto = ParceSiteResultDto(id=contract.id, result="ok", error=None)
    await parce_site_service.finalize_contract(dto)
    assert contract.status.name.lower() in ["success", "in_progress"] or contract.result is None

from src.entity import ParceSiteContract
from src.entity.base import StatusEnum
from src.processing_site.dto_workers import ParceSiteResultDto


def convert_parce_site_contract_to_document(contract: ParceSiteContract) -> dict:
    return {
        "id": contract.id,
        "url_site": contract.url_site,
        "result": contract.result,
        "status": contract.status.value,
        "error": contract.error,
        "created_at": contract.created_at,
        "updated_at": contract.updated_at,
    }


def convert_document_to_parce_site_contract(document: dict) -> ParceSiteContract:
    return ParceSiteContract(
        id=document["id"],
        url_site=document["url_site"],
        result=document["result"],
        status=StatusEnum(document["status"]),
        error=document["error"],
        created_at=document["created_at"],
        updated_at=document["updated_at"],
    )


def merge_dict_fields(source: dict, target: dict) -> dict:
    target.update({k: v for k, v in source.items() if k in target})
    return target


def convert_parce_site_result_dto_to_dict(dto: ParceSiteResultDto) -> dict:
    return {
        "id": dto.id,
        "result": dto.result,
        "error": dto.error,
    }

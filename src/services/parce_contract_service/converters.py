from src.entity import ParceSiteContract


def convert_parce_site_contract_to_document(contract: ParceSiteContract) -> dict:
    return {
        "id": contract.id,
        "url_site": contract.url_site,
        "result": contract.result,
        "status": contract.status.value,
        "error": contract.error,
        "created_at": contract.created_at,
        "updated_at": contract.updated_at
    }
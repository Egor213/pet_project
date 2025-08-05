from pydantic import BaseModel
from datetime import datetime

from src.entity import ParceSiteContract, StatusEnum


class CreateContractSchema(BaseModel):
    id: str
    url_site: str
    status: StatusEnum

    @classmethod
    def from_entity(cls, entity: ParceSiteContract) -> "CreateContractSchema":
        return cls(
            id=entity.id,
            url_site=entity.url_site,
            status=entity.status.value,
        )


class ContractSchema(BaseModel):
    id: str
    url_site: str
    status: StatusEnum
    result: str | None
    error: str | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: ParceSiteContract) -> "CreateContractSchema":
        return cls(
            id=entity.id,
            url_site=entity.url_site,
            status=entity.status.value,
            result=entity.result,
            error=entity.error,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

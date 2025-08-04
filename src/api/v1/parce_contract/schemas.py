from pydantic import BaseModel

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

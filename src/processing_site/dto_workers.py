from pydantic import BaseModel


class ParceSiteDto(BaseModel):
    url_site: str
    id: str

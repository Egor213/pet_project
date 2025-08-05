from dataclasses import dataclass

from .base import BaseContract


@dataclass
class ParceSiteContract(BaseContract):
    url_site: str
    result: dict | None = None
    error: str | None = None

    @classmethod
    def create_contract(cls, url_site: str) -> "ParceSiteContract":
        return cls(url_site=url_site)

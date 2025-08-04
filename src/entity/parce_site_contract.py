from dataclasses import dataclass
from .base import BaseContract


@dataclass
class ParceSiteContract(BaseContract):
    url_site: str
    result: dict | None
    error: dict | None

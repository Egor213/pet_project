from dataclasses import dataclass


@dataclass
class ParceSiteDto:
    url_site: str
    id: str


@dataclass
class ParceSiteResultDto:
    id: str
    result: str | None = None
    error: str | None = None

import asyncio
import re

from bs4 import BeautifulSoup

from src.services.http_service import BaseHttpService

from .dto_workers import ParceSiteDto, ParceSiteResultDto


def chunk_sentences(text: str, max_chars: int = 200):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunk = ""
    for s in sentences:
        if len(chunk) + len(s) <= max_chars:
            chunk += " " + s
        else:
            yield chunk.strip()
            chunk = s
    if chunk:
        yield chunk.strip()


async def parce_site_worker(
    parce_site_dto: ParceSiteDto, http_service: BaseHttpService
) -> ParceSiteResultDto:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = await http_service.get(parce_site_dto.url_site, headers=headers)
    except Exception as e:
        return ParceSiteResultDto(id=parce_site_dto.id, error=str(e))
    soup = BeautifulSoup(response, "html.parser")
    clean_text = soup.get_text(separator=" ", strip=True)

    return ParceSiteResultDto(id=parce_site_dto.id, result=clean_text)

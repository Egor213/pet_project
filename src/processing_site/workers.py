import asyncio
import re

from bs4 import BeautifulSoup

from src.services.http_service import BaseHttpService

from .dto_workers import ParceSiteDto, ParceSiteResultDto

# TODO: пусть он ходит к lm_studio
# 1. С помощью Beautiful Soup парсим страничку
# 2. Отправляем данные в lm_studio
# 3. После парсинга отправим данные в топик кафки
# 4. С другой стороны считает тг бот


# Можно поднять гошный сервис авторизации и через него получать токен, а тут провалидировать его
# К контракту надо добавить владельца
# Нужно тогда поставить мидлваре, чтобы проверять токен


# Можно сделать отдельную абстракцию над LM_Studio, но мне не хочется)


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
    # clean_text = clean_text[:400]

    # url = "http://127.0.0.1:1234/v1/chat/completions"
    # headers = {"Content-Type": "application/json"}
    # context_messages = []

    # for chunk in chunk_sentences(clean_text, max_chars=200):
    #     payload = {
    #         "model": "ibm/granite-4-h-tiny",
    #         "messages": context_messages
    #         + [{"role": "user", "content": f"Кратно опиши: {chunk}"}],
    #     }
    #     try:
    #         response = await http_service.post(url=url, json=payload, headers=headers)
    #     except Exception as e:
    #         return e

    #     lm_output = response["choices"][0]["message"]["content"]
    #     context_messages.append({"role": "assistant", "content": lm_output})

    # final_output = " ".join(
    #     [msg["content"] for msg in context_messages if msg["role"] == "assistant"]
    # )

    return ParceSiteResultDto(id=parce_site_dto.id, result=clean_text)

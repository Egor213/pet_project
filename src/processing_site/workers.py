import asyncio

from .dto_workers import ParceSiteDto

# TODO: пусть он ходит к lm_studio
# 1. С помощью Beautiful Soup парсим страничку
# 2. Отправляем данные в lm_studio
# 3. После парсинга отправим данные в топик кафки
# 4. С другой стороны считает тг бот


# Можно поднять гошный сервис авторизации и через него получать токен, а тут провалидировать его
# К контракту надо добавить владельца
# Нужно тогда поставить мидлваре, чтобы проверять токен

async def parce_site_worker(parce_site_dto: ParceSiteDto):
    print(parce_site_dto)
    print(f"Start: {parce_site_dto.url_site}")
    await asyncio.sleep(3)
    print(f"Done: {parce_site_dto.url_site}")
    return 1

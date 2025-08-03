from fastapi import Depends, routing
import punq

from src.app.config.main import Config
from src.api import container
from src.services.site_service import BaseSiteService, MongoSiteService


test_router = routing.APIRouter(
    tags=["test"],
)

def contract_service() -> BaseSiteService:
    return container.resolve(BaseSiteService)

@test_router.get("/test")
async def test(container: punq.Container = Depends(contract_service)) -> dict:
    # config = container.resolve(Config)
    # print(config)
    print(type(container))
    return {"test": "test3"}
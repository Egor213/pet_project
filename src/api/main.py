import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1 import v1_router
from src.app.init import init_container
from src.app.logger import init_logger
from src.services import BasePoolService
from src.services.http_service import BaseHttpService


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = init_container()

    http_service = container.resolve(BaseHttpService)
    http_service.start()

    pool_service = container.resolve(BasePoolService)
    await pool_service.run()
    init_logger()
    yield
    await http_service.close()
    await pool_service.stop()


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="Pet-Project",
        docs_url="/api/docs",
        lifespan=lifespan,
    )
    app.include_router(v1_router, prefix="/api")
    return app

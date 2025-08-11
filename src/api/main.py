import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1 import v1_router
from src.app.init import init_container
from src.app.logger import init_logger
from src.services import AsyncPoolService


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = init_container()
    async_pool_service = container.resolve(AsyncPoolService)
    await async_pool_service.run()
    init_logger()
    yield
    await async_pool_service.stop()


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="Pet-Project",
        docs_url="/api/docs",
        lifespan=lifespan,
    )
    app.include_router(v1_router, prefix="/api")
    return app

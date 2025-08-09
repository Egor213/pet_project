import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1 import v1_router
from src.app.logger import init_logger
from src.parcers.main import init_parce_site_workers


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(init_parce_site_workers())
    init_logger()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="Pet-Project",
        docs_url="/api/docs",
        lifespan=lifespan,
    )
    app.include_router(v1_router, prefix="/api")
    return app

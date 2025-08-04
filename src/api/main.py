from fastapi import FastAPI

from src.api.v1 import v1_router


def create_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        title="Pet-Project",
        docs_url="/api/docs",
    )
    app.include_router(v1_router, prefix="/api")
    return app

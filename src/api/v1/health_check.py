from fastapi import routing

health_check_router = routing.APIRouter(
    prefix="/health_check",
    tags=["health_check"],
)


@health_check_router.get("/")
async def health_check() -> dict:
    return {"status": "ok"}

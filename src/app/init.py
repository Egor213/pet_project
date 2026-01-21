import logging
from functools import lru_cache

import punq
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.config import Config
from src.processing_site.result_handlers import update_parce_site_contract
from src.processing_site.workers import parce_site_worker
from src.repositories.parce_contract_repository import (
    BaseParceSiteRepository,
    MongoParceSiteRepository,
)
from src.services.grpc_service import BaseGrpcService, LogGrpcService
from src.services.http_service import AioHttpService, BaseHttpService
from src.services.parce_contract_service import ParceSiteService
from src.services.pool_service import AsyncPoolService, BasePoolService


def init_parce_site_repository_mongo():
    config: Config = Config()
    client = AsyncIOMotorClient(config.db.uri, serverSelectionTimeoutMS=3000)
    return MongoParceSiteRepository(
        mongo_db_client=client,
        mongo_db_db_name=config.db.db_name,
        mongo_db_collection_name=config.db.collection_name,
    )


def init_async_pool_service(container) -> AsyncPoolService:
    http_service = container.resolve(BaseHttpService)
    async_pool = AsyncPoolService(
        handler=parce_site_worker,
        num_workers=10,
        max_wait_time=1200,
        logger=logging.getLogger(__name__),
        http_service=http_service,
    )
    return async_pool


def init_parce_site_service_mongo(container):
    contract_repo = init_parce_site_repository_mongo()
    pool_serv = container.resolve(BasePoolService)
    return ParceSiteService(contract_repository=contract_repo, pool_service=pool_serv)


@lru_cache(1)
def init_container():
    container = punq.Container()

    container.register(Config, instance=Config(), scope=punq.Scope.singleton)

    container.register(
        BaseParceSiteRepository,
        factory=init_parce_site_repository_mongo,
        scope=punq.Scope.singleton,
    )
    # AsyncPool
    container.register(
        BaseHttpService,
        instance=AioHttpService(
            max_connections=10,
            timeout=1200,
        ),
        scope=punq.Scope.singleton,
    )
    container.register(
        ParceSiteService,
        factory=lambda: init_parce_site_service_mongo(container),
        scope=punq.Scope.singleton,
    )
    container.register(
        BasePoolService,
        factory=lambda: init_async_pool_service(container),
        scope=punq.Scope.singleton,
    )

    container.register(
        BaseGrpcService,
        instance=LogGrpcService(
            port=3000,
        ),
        scope=punq.Scope.singleton,
    )

    return container

import logging
from functools import lru_cache

import punq
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.config import Config
from src.processing_site.workers import parce_site_worker
from src.repositories.parce_contract_repository import (
    BaseParceSiteRepository, MongoParceSiteRepository)
from src.services import AsyncPoolService, ParceSiteService


def init_parce_site_repository_mongo():
    config: Config = Config()
    client = AsyncIOMotorClient(config.db.uri, serverSelectionTimeoutMS=3000)
    return MongoParceSiteRepository(
        mongo_db_client=client,
        mongo_db_db_name=config.db.db_name,
        mongo_db_collection_name=config.db.collection_name,
    )


def init_parce_site_service_mongo():
    contract_repo = init_parce_site_repository_mongo()
    return ParceSiteService(contract_repository=contract_repo)


@lru_cache(1)
def init_container():
    container = punq.Container()

    container.register(Config, instance=Config(), scope=punq.Scope.singleton)

    container.register(
        BaseParceSiteRepository,
        factory=init_parce_site_repository_mongo,
        scope=punq.Scope.singleton,
    )
    container.register(
        ParceSiteService,
        factory=init_parce_site_service_mongo,
        scope=punq.Scope.singleton,
    )

    # AsyncPool
    container.register(
        AsyncPoolService,
        scope=punq.Scope.singleton,
        instance=AsyncPoolService(
            handler=parce_site_worker,
            num_workers=10,
            logger=logging.getLogger(__name__),
        ),
    )

    return container

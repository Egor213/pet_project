import punq
from motor.motor_asyncio import AsyncIOMotorClient
from src.app.config import Config
from src.services.site_service import BaseSiteService, MongoSiteService
from src.repositories.site_repository import BaseSiteRepository, MongoSiteRepository


def init_site_repository_mongo():
    config: Config = Config()
    client = AsyncIOMotorClient(config.db.uri, serverSelectionTimeoutMS=3000)
    return MongoSiteRepository(
        mongo_db_client=client,
        mongo_db_db_name="contracts",
        mongo_db_collection_name="contracts",
    )


def init_site_service_mongo():
    site_repo = init_site_repository_mongo()
    return MongoSiteService(site_repository=site_repo)


def init_container():
    container = punq.Container()

    container.register(Config, instance=Config(), scope=punq.Scope.singleton)

    container.register(
        BaseSiteRepository,
        factory=init_site_repository_mongo,
        scope=punq.Scope.singleton,
    )

    container.register(
        BaseSiteService,
        factory=init_site_service_mongo,
        scope=punq.Scope.singleton,
    )

    return container

import punq
from motor.motor_asyncio import AsyncIOMotorClient
from src.app.config import Config
from src.services.parce_contract_service import BaseParceSiteService, MongoParceSiteService
from src.repositories.parce_contract_repository import BaseParceSiteRepository, MongoParceSiteRepository


def init_contract_repository_mongo():
    config: Config = Config()
    client = AsyncIOMotorClient(config.db.uri, serverSelectionTimeoutMS=3000)
    return MongoParceSiteRepository(
        mongo_db_client=client,
        mongo_db_db_name="contracts",
        mongo_db_collection_name="contracts",
    )


def init_contract_service_mongo():
    contract_repo = init_contract_repository_mongo()
    return MongoParceSiteService(contract_repository=contract_repo)


def init_container():
    container = punq.Container()

    container.register(Config, instance=Config(), scope=punq.Scope.singleton)

    container.register(
        BaseParceSiteRepository,
        factory=init_contract_repository_mongo,
        scope=punq.Scope.singleton,
    )

    container.register(
        BaseParceSiteService,
        factory=init_contract_service_mongo,
        scope=punq.Scope.singleton,
    )

    return container

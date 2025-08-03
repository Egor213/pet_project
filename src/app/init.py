import punq
from motor.motor_asyncio import AsyncIOMotorClient
from src.app.config import Config
from src.services.contract_service import BaseContractService, MongoContractService
from src.repositories.contract_repository import BaseContractRepository, MongoContractRepository


def init_contract_repository_mongo():
    config: Config = Config()
    client = AsyncIOMotorClient(config.db.uri, serverSelectionTimeoutMS=3000)
    return MongoContractRepository(
        mongo_db_client=client,
        mongo_db_db_name="contracts",
        mongo_db_collection_name="contracts",
    )


def init_contract_service_mongo():
    contract_repo = init_contract_repository_mongo()
    return MongoContractService(contract_repository=contract_repo)


def init_container():
    container = punq.Container()

    container.register(Config, instance=Config(), scope=punq.Scope.singleton)

    container.register(
        BaseContractRepository,
        factory=init_contract_repository_mongo,
        scope=punq.Scope.singleton,
    )

    container.register(
        BaseContractService,
        factory=init_contract_service_mongo,
        scope=punq.Scope.singleton,
    )

    return container

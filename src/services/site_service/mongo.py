from dataclasses import dataclass
from .base import BaseSiteService
from src.repositories.site_repository import MongoSiteRepository

@dataclass
class MongoSiteService(BaseSiteService):
    site_repository: MongoSiteRepository
    
    async def temp():
        ...
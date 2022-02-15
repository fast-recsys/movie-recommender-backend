from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config import get_settings

settings = get_settings()

motor_client = AsyncIOMotorClient(settings.mongodb_url)
database = motor_client[settings.mongodb_dbname]

def get_database() -> AsyncIOMotorDatabase:
    return database


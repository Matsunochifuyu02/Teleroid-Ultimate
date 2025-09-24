from core.db import PostgresDB, MongoDB, RedisCache
from core.logger import logger
from core.loader import load_plugins
import config

async def startup():
    logger.info("Starting Teleroid Ultimate Bot...")

    pg = PostgresDB(config.POSTGRES_DSN)
    await pg.connect()
    logger.info("Postgres Connected.")

    mongo = MongoDB(config.MONGO_URI, "teleroid")
    logger.info("MongoDB Connected.")

    redis = RedisCache(config.REDIS_URL)
    await redis.connect()
    logger.info("Redis Connected.")

    plugins = load_plugins()
    logger.info(f"Loaded {len(plugins)} plugins.")

    # Here, connect/start your chosen framework: Pyrogram, Telethon, or Aiogram

if __name__ == "__main__":
    import asyncio
    asyncio.run(startup())

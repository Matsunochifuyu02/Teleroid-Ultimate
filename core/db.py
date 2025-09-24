import asyncpg
import motor.motor_asyncio
import aioredis
import os

class PostgresDB:
    def __init__(self, dsn):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(dsn=self.dsn)

    async def fetch(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query, *args):
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

class MongoDB:
    def __init__(self, uri, dbname):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client[dbname]

    def get_collection(self, collection_name):
        return self.db[collection_name]

class RedisCache:
    def __init__(self, url):
        self.url = url
        self.cache = None

    async def connect(self):
        self.cache = await aioredis.from_url(self.url)

    async def get(self, key):
        return await self.cache.get(key)

    async def set(self, key, value):
        await self.cache.set(key, value)
  

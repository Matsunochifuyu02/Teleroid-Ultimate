import os

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_apihash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "yourbottoken")
POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://user:pass@localhost/db")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

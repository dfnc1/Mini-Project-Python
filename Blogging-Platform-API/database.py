import asyncpg, os
from dotenv import load_dotenv

load_dotenv()
pool = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        dsn=os.getenv("DB_URL"),
        min_size=1,
        max_size=10
    )

async def get_db():
    global pool
    async with pool.acquire() as conn:
        yield conn

async def close_db():
    global pool
    await pool.close
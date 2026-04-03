from contextlib import asynccontextmanager
from fastapi import FastAPI

from .routers import auth, posts
from . import get_pool, close_pool

@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_pool()
    yield
    await close_pool()

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(posts.router)
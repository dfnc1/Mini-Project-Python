from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import *
from model import Post

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()
app = FastAPI(lifespan=lifespan)

@app.get("/blogs")
async def get_blog(term: str = None, conn= Depends(get_db)) :
    try:
        if term:
            return await conn.fetch("SELECT * FROM posts WHERE title = $1 OR content = $1 OR category = $1", term)
        else:
            return await conn.fetch("SELECT * FROM posts")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/blogs/{id}")
async def get_blog_by_id(id: int, conn= Depends(get_db)):
    try:
        return await conn.fetchrow("SELECT * FROM posts WHERE id = $1", id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/blogs")
async def post_blog(data: Post, conn= Depends(get_db)):
    try:
        return await conn.fetchrow("INSERT INTO posts (title, content, category, tags) VALUES ($1,$2,$3,$4) RETURNING * ",
                                  data.title, data.content, data.category, data.tags)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/blogs/{id}")
async def delete_blog(id: int, conn= Depends(get_db)):
    try:
        return await conn.fetchrow("DELETE FROM posts WHERE id = $1 RETURNING *", id)
    except Exception as e:
        HTTPException(status_code=500, detail=str(e))

@app.patch("/blogs/{id}")
async def update_blog(id: int, data: Post, conn= Depends(get_db)):
    try:
        return await conn.fetchrow("UPDATE posts SET title = $1, content = $2, category = $3, tags = $4, update_at = NOW() WHERE id = $5  RETURNING * ",
                            data.title, data.content, data.category, data.tags, id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


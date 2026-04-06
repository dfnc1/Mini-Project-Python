import asyncpg

from app.schemas import Post

async def create_post(conn: asyncpg.Pool, data: Post) -> Post :
    return await conn.fetchrow("INSERT INTO posts (title, description) VALUES ($1, $2) RETURNING id, title, description",
                               data.title, data.description)

async def update_post(conn: asyncpg.Pool, id: int, data: Post):
    return await conn.fetchrow("UPDATE posts SET title = $1, description = $2 WHERE id=$3",
                               data.title, data.description, id)

async def delete_post(conn: asyncpg.Pool, id: int):
    return await conn.fetchrow("DELETE FROM posts WHERE id = $1",
                               id)

async def get_post(conn: asyncpg.Pool, page: int , limit: int ) -> list[Post] :
    return await conn.fetch("SELECT * FROM posts WHERE id BETWEEN $1 AND $2 ORDER BY id ASC",
                                page, limit)
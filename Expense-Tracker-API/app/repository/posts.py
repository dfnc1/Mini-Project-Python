from datetime import datetime
from typing import List

import asyncpg

from app.schemas import Post

async def add_post(
        *,
        data: Post,
        conn: asyncpg.Pool
) -> Post:
    return await conn.fetchrow("INSERT INTO post (description, categories, amount) VALUES ($1, $2, $3) RETURNING *",
                               data.description, data.category, data.amount)

async def delete_post(
        *,
        id: int,
        conn: asyncpg.Pool
) -> Post:
    return await conn.fetchrow("DELETE FROM post WHERE id = $1", id)

async def update_post(
        *,
        id: int,
        data: Post,
        conn: asyncpg.Pool
) -> Post:
    return await conn.fetchrow("UPDATE post SET description = $1, categories = $2, amount = $3, update_at = CURRENT_TIMESTAMP WHERE id = $4",
                               data.description, data.category, data.amount, id)

async def get_posts(
        *,
        filter_date: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        conn: asyncpg.Pool
) -> List[Post]:
    global data
    start_obj = datetime.strptime(start_date, '%Y-%m-%d').date() if start_date else None
    end_obj = datetime.strptime(end_date, '%Y-%m-%d').date() if end_date else None
    if filter_date:
        data = await conn.fetch("""SELECT * FROM post 
                                   WHERE created_at >= NOW() - ($1 * INTERVAL '1 days') 
                                      OR update_at >= NOW() - ($1 * INTERVAL '1 days')""", filter_date)
    if start_date and end_date:
        data = await conn.fetch("""SELECT * FROM post 
            WHERE (created_at >= $1 AND created_at < $2::DATE + INTERVAL '1 day')
               OR (update_at >= $1 AND update_at < $2::DATE + INTERVAL '1 day')""", start_obj, end_obj)
    return data

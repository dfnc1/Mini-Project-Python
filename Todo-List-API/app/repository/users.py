from fastapi import Depends, HTTPException

from .. import get_db

async def get_user(username: str, conn= Depends(get_db)):
    try:
        user = await conn.fetchrow("SELECT * FROM users where username = $1", username)
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

async def get_user_by_email(email: str, conn= Depends(get_db)):
    try:
        user = await conn.fetchrow("SELECT * FROM users where email = $1", email)
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")


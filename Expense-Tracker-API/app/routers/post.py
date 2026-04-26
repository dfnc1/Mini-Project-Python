from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.databases import get_db
from app.security import get_current_user
from app.schemas import User, Post

router = APIRouter(prefix="/post", tags=["post"])

@router.post("/expense", status_code=status.HTTP_201_CREATED)
async def create_expense(data: Post, current_user: Annotated[User, Depends(get_current_user)], conn= Depends(get_db)):
    return {"hello": "world"}
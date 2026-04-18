import os
from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from pwdlib import PasswordHash
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import asyncpg

from app.schemas import TokenData

load_dotenv()
password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(int(os.getenv("ACCES_TOKEN_EXPIRE_MINUTES")))})
    return jwt.encode(to_encode, key=os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))

async def get_current_user(token: Annotated[str, Depends()]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = await jwt.decode(token, key=os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except:
        raise credentials_exception

    user = None
    if user is None:
        raise credentials_exception
    return user

async def authenticate_user(email: str, password: str, conn: asyncpg.Pool):
    user = None
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user
from typing import Annotated

from pwdlib import PasswordHash

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .. import Register, get_db
router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

password_hasher = PasswordHash.recommended()

@router.post("/register")
async def register(payload: Register, conn= Depends(get_db)):
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    exist_user = await conn.fetchrow("SELECT * FROM users WHERE email = $1",
                                     payload.email)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    try:
        await conn.fetchval("INSERT INTO users (NAME, EMAIL, PASSWORD) VALUES ($1, $2, $3)",
                            payload.username, payload.email, password_hasher.hash(payload.password))

        return {"token": f"Bearer{payload.email}"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], conn= Depends(get_db)):
    user = await conn.fetchrow("SELECT * FROM users WHERE email = $1 ",form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")

    verify_password = password_hasher.verify(form_data.password, user["password"])
    if not verify_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")


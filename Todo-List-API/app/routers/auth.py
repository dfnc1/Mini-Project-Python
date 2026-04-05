from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.security import get_password_hash, create_access_token, authenticate_user
from app.schemas import UserInDB, Token, Register
from app.repository.users import get_user, add_user

router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})

@router.post("/register")
async def register(payload: Register, conn= Depends(get_db)):
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    exist_user = await get_user(payload.email, conn)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    try:
        new_user = UserInDB(name=payload.name, email=payload.email, hashed_password=get_password_hash(payload.password))
        await add_user(new_data=new_user, conn=conn)

        access_token = create_access_token(data={"sub": payload.email})
        return Token(access_token=access_token, token_type="bearer")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], conn= Depends(get_db)):
    user = await authenticate_user(form_data.username, form_data.password, conn)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user["email"]})
    return Token(access_token=access_token, token_type="bearer")
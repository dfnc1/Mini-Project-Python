from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Register(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class TokenData(BaseModel):
    email: str
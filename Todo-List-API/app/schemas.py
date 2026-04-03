from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

class UserInDB(User):
    hashed_password: str

class Register(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

class Post(BaseModel):
    title: str
    description: str
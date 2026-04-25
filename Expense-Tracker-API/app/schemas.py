from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Register(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str

class UserInDB(User):
    hashed_password: str

class TokenData(BaseModel):
    email: str

class Post(BaseModel):
    description: str
    category: str
    amount: float
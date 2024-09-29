from datetime import datetime
from typing import Optional

from pydantic import BaseModel,EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id:int
    title: str
    content: str
    published: bool
    created_at:datetime
    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenData(BaseModel):
    id:Optional[str]=None

class Token(BaseModel):
    access_token:str
    token_type:str
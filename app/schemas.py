from datetime import datetime
from typing import Optional

from pydantic import BaseModel,EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at:datetime

    class Config:
        from_attributes = True


class Post(BaseModel):
    id:int
    title: str
    content: str
    published: bool
    created_at:datetime
    owner_id:int
    owner:UserResponse

    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    email : EmailStr
    password: str


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenData(BaseModel):
    id:Optional[str]=None

class Token(BaseModel):
    access_token:str
    token_type:str
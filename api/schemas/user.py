from typing import Optional
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: Optional[str] = Field(..., example="pyoe")
    email: Optional[str] = Field(..., example="sample@gmail.com")


class UserCreate(UserBase):
    password: Optional[str] = Field(..., example="p@ssw0rd")


class UserDisplay(UserBase):
    id: int

    class Config:
        orm_mode = True

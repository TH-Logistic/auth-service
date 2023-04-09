from pydantic import BaseModel, Field, EmailStr
from pydantic import UUID4
import datetime
from ..models.role import Role
from enum import Enum


class UserBase(BaseModel):
    name: str
    email: str
    birthday: datetime.datetime | None
    avatar: str
    role: Role

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(min_length=1)


class UserOut(UserBase):
    id: UUID4
    deletedAt: datetime.datetime | None


class UserOutWithPassword(UserOut):
    password: str

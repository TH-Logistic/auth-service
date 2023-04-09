from pydantic import BaseModel, Field, EmailStr
from pydantic import UUID4
import datetime
from ..models.role import Role
from enum import Enum
from bson import ObjectId
from src.utils.py_objectid import PyObjectId


class UserBase(BaseModel):
    name: str = Field(min_length=1)
    email: str = EmailStr()
    birthday: datetime.datetime | None
    avatar: str
    role: Role
    deletedAt: datetime.datetime | None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(min_length=1)


class UserOut(UserBase):
    id: PyObjectId = Field(alias='_id')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserOutWithPassword(UserBase):
    id: PyObjectId = Field(alias='_id')
    password: str


class UserOutWithPassword(UserOut):
    password: str

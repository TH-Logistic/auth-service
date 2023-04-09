from fastapi import Depends, HTTPException
from bson import ObjectId
from ..models.user import User
from src.config.settings import settings
from sqlalchemy.orm import Session
from json.encoder import JSONEncoder
import sqlalchemy.exc
from ..schemas.user import UserCreate, UserBase, UserOut, UserOutWithPassword
from ..models.role import Role
from psycopg2 import Error
import uuid
from passlib.context import CryptContext
from src.config.database import mongo_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCRUD():

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def get_user_by_id(self, id: str) -> User | None:
        users = mongo_db['users'].find_one({"_id": ObjectId(id)})
        return users

    def get_users(self) -> list[UserOut]:
        return mongo_db['users'].find()

    def get_user_by_email(self, email: str) -> UserOutWithPassword | None:
        user = mongo_db['users'].find_one({"email": email})
        return UserOutWithPassword(**user)

    def create_user(self, user_create: UserCreate) -> UserOut | None:
        user_create.password = self.get_password_hash(user_create.password)
        created_user = mongo_db['users'].insert_one(user_create.dict())
        created_user = mongo_db["users"].find_one(
            {"_id": created_user.inserted_id}, {'password': 0}
        )

        created_user = UserOut(
            **created_user
        )

        return created_user

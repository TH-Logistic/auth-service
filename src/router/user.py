from fastapi import APIRouter, Path, Depends
from src.crud.user import UserCRUD
from sqlalchemy.orm import Session
from ..schemas.user import UserOut
from ..config.database import get_db

router = APIRouter(prefix="")

user_crud = UserCRUD()


@router.get("/user/{id}", response_model=UserOut)
def get_user_by_id(id: str = Path()) -> UserOut | None:
    user = user_crud.get_user_by_id(id=id)
    return user


@router.get("/users")
def get_users() -> list:
    return user_crud.get_users()

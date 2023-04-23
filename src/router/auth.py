from fastapi import APIRouter, Query, HTTPException, Body, Security, Response
from fastapi.responses import JSONResponse
from fastapi.security import SecurityScopes
from datetime import timedelta
from src.models.token_payload import TokenPayload

from sqlalchemy.orm import Session
from fastapi import Depends
from src.models.base_response import BaseResponse
from src.models.role import Role
from src.schemas.user import UserOut, UserCreate
from src.dependencies import auth
from src.models.token import Token, TokenType
from src.crud import user

router = APIRouter(prefix="")

user_crud = user.UserCRUD()


@router.post("/login")
async def login(response: Response, email: str = Body(), password: str = Body()):
    user = auth.authenticate_user(email=email, password=password)

    if not user:
        content = BaseResponse()
        content.success = False
        content.message = "Incorrect username or password"
        content.data = None

        response.status_code = 401
        return content
    else:
        access_token = auth.create_token(
            TokenPayload(
                sub=str(user.id),
                scopes=[user.role]
            ),
            token_expire=timedelta(minutes=60)
        )
        refesh_token = auth.create_token(
            TokenPayload(
                sub=str(user.id),
                scopes=[user.role]
            ),
            token_expire=timedelta(hours=60)
        )

        return {
            "success": True,
            "message": None,
            "data": Token(
                access_token=access_token,
                refresh_token=refesh_token,
                token_type=TokenType.BEARER
            )
        }


@router.post("/register")
async def register(user_create: UserCreate = Body()):
    user = user_crud.create_user(user_create)

    if user:
        access_token = auth.create_token(
            TokenPayload(
                sub=str(user.id),
                scopes=[user.role]
            ),
            token_expire=timedelta(minutes=60)
        )
        refesh_token = auth.create_token(
            TokenPayload(
                sub=str(user.id),
                scopes=[user.role]
            ),
            token_expire=timedelta(hours=60)
        )

        return {
            "success": True,
            "message": None,
            "data": Token(
                access_token=access_token,
                refresh_token=refesh_token,
                token_type=TokenType.BEARER
            )
        }


@router.post("/check-permissions")
async def check_permission(scopes: list[str] = Body(), token: str = Depends(auth.oauth2_scheme)):
    user = auth.get_current_user(
        security_scopes=SecurityScopes(scopes),
        token=token
    )

    return {
        "success": True,
        "message": None,
        "data": user
    }

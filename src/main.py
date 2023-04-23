from fastapi import FastAPI, Request, HTTPException
from pymongo import errors
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models.base_response import BaseResponse
from fastapi.middleware.cors import CORSMiddleware
from src.models import user
from src.router import user
from src.router import auth
from src.router import auth
from src.config.database import Base, engine

app = FastAPI()

app.include_router(router=user.router)
app.include_router(router=auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_credentials=True,
    allow_origins=["*"]
)


@app.exception_handler(Exception)
def handle_exceptions(req: Request, err: Exception):
    message = ''
    status_code = 500
    print(err)
    if isinstance(err, HTTPException):
        message = err.detail
        status_code = err.status_code

    if isinstance(err, errors.DuplicateKeyError):
        message = err.details['errmsg']
        status_code = 400

    response = BaseResponse()
    response.message = message

    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=status_code
    )

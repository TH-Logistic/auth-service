from fastapi import FastAPI
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

from pydantic import BaseModel
from uuid import UUID


class TokenPayload(BaseModel):
    sub: str
    scopes: list[str] = []

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pydantic import BaseModel
from ..config.database import Base
from .role import Role
import uuid


class User(Base):
    __tablename__ = "user"

    id: UUID = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
    )
    name: str = Column(String)
    password: str = Column(String)
    email: str = Column(String, unique=True)
    birthday = Column(DateTime)
    avatar: str = Column(String)
    deletedAt = Column(DateTime)
    role: Role = Column(ENUM('admin', name='role'))

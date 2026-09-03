import uuid

from sqlalchemy import UUID, Column, String

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hash_password = Column(String)

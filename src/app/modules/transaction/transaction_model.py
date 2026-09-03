import uuid

from src.database import Base

from sqlalchemy import UUID, Column, Integer, Float, String, DateTime, ForeignKey, Enum
from datetime import datetime

type_enum = Enum("income", "expense", name="transaction_type")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(type_enum, nullable=False)
    category= Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.now)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id",ondelete="CASCADE"), nullable=False)



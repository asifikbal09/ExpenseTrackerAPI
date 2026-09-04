from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.modules.transaction.transaction_validation import CreateTransaction
from src.app.dependency.auth import get_current_user_id
from src.app.modules.transaction.transaction_controller import (
    create_transaction_controller,
)
from src.database import get_db

transaction_router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

db_dependency = Depends(get_db)
user_id_dependency = Depends(get_current_user_id)


@transaction_router.post("/", status_code=201)
def create_transaction_endpoint(
    payload: CreateTransaction,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return create_transaction_controller(db, payload, user_id)

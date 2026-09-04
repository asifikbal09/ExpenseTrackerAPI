from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.modules.transaction.transaction_validation import CreateTransaction
from src.app.dependency.auth import get_current_user_id
from src.app.modules.transaction.transaction_controller import (
    create_transaction_controller,
    get_transaction_by_id_controller,
    get_transactions_controller,
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

@transaction_router.get("/", status_code=200)
def get_transactions_endpoint(
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return get_transactions_controller(db, user_id)

@transaction_router.get("/{transaction_id}", status_code=200)
def get_transaction_by_id_endpoint(
    transaction_id: UUID,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return get_transaction_by_id_controller(db, transaction_id, user_id)

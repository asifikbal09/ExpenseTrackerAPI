from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.modules.transaction.transaction_validation import CreateTransaction, UpdateTransaction
from src.app.dependency.auth import get_current_user_id
from src.app.modules.transaction.transaction_controller import (
    create_transaction_controller,
    delete_transaction_controller,
    get_transaction_by_id_controller,
    get_transactions_by_filter_controller,
    get_transactions_controller,
    update_transaction_controller,
)

from typing import Literal, Optional

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

@transaction_router.get("/filter", status_code=200)
def get_transactions_by_filter_endpoint(
    type: Optional[Literal["income", "expense"]] = None,
    category: Optional[str] = None,
    minmun_amount: Optional[float] = None,
    maximum_amount: Optional[float] = None,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return get_transactions_by_filter_controller(db, user_id, type, category, minmun_amount, maximum_amount)

@transaction_router.get("/{transaction_id}", status_code=200)
def get_transaction_by_id_endpoint(
    transaction_id: UUID,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return get_transaction_by_id_controller(db, transaction_id, user_id)

@transaction_router.put("/{transaction_id}", status_code=200)
def update_transaction_endpoint(
    transaction_id: UUID,
    payload: UpdateTransaction,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return update_transaction_controller(db, transaction_id, user_id, payload)

@transaction_router.delete("/{transaction_id}", status_code=200)
def delete_transaction_endpoint(
    transaction_id: UUID,
    db: Session = db_dependency,
    user_id: UUID = user_id_dependency,
):
    return delete_transaction_controller(db, transaction_id, user_id)


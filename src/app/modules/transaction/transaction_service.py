from uuid import UUID
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from datetime import datetime

from src.app.modules.transaction.transaction_model import Transaction
from src.app.modules.transaction.transaction_validation import CreateTransaction

from fastapi.encoders import jsonable_encoder

from src.app.modules.transaction.transaction_validation import UpdateTransaction


def create_transaction(
    db: Session,
    payload: CreateTransaction,
    user_id: UUID,
) -> Transaction:

    transaction ={
        "title": payload.title,
        "amount": payload.amount,
        "type": payload.type,
        "category": payload.category,
        "date": datetime.now(),
        "user_id": user_id
    }
    
    new_transaction = Transaction(**transaction)
    print(new_transaction.__dict__)

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return jsonable_encoder(new_transaction)

def get_transactions(db: Session, user_id: UUID):
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    return jsonable_encoder(transactions)

def get_transaction_by_id(db: Session, transaction_id: UUID, user_id: UUID):
    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id, Transaction.user_id == user_id)
        .first()
    )
    return jsonable_encoder(transaction)

def update_transaction(db: Session, transaction_id: UUID, user_id: UUID, payload: UpdateTransaction):
    
    print(f"Updating transaction {transaction_id} for user {user_id} with payload: {payload.dict(exclude_unset=True)}")
    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id, Transaction.user_id == user_id)
        .first()
    )

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)

    return jsonable_encoder(transaction)



def delete_transaction(db: Session, transaction_id: UUID, user_id: UUID):
    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id, Transaction.user_id == user_id)
        .first()
    )

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return jsonable_encoder(transaction)

def get_transactions_by_filter(db: Session, user_id: UUID, type: Optional[str] = None, category: Optional[str] = None, minmun_amount: Optional[float] = None, maximum_amount: Optional[float] = None):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)

    if type:
        query = query.filter(Transaction.type == type)
    if category:
        query = query.filter(Transaction.category == category)
    if minmun_amount is not None:
        query = query.filter(Transaction.amount >= minmun_amount)
    if maximum_amount is not None:
        query = query.filter(Transaction.amount <= maximum_amount)

    transactions = query.all()
    return jsonable_encoder(transactions)
    
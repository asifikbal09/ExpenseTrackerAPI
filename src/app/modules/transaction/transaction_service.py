from uuid import UUID

from sqlalchemy.orm import Session

from datetime import datetime

from src.app.modules.transaction.transaction_model import Transaction
from src.app.modules.transaction.transaction_validation import CreateTransaction

from fastapi.encoders import jsonable_encoder


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

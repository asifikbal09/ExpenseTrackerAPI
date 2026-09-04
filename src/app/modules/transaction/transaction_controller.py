from src.app.utils.sendResponse import send_response

from src.app.modules.transaction.transaction_service import (
    create_transaction,
    get_transactions,
    get_transaction_by_id,
)


def create_transaction_controller(db, payload, user_id):
    transaction = create_transaction(db, payload, user_id)
    return send_response(
        status_code=201,
        success=True,
        message="Transaction created successfully",
        data=transaction,
    )


def get_transactions_controller(db, user_id):
    transactions = get_transactions(db, user_id)
    return send_response(
        status_code=200,
        success=True,
        message="Transactions retrieved successfully",
        data=transactions,
    )


def get_transaction_by_id_controller(db, transaction_id, user_id):
    transaction = get_transaction_by_id(db, transaction_id, user_id)
    if not transaction:
        return send_response(
            status_code=404, success=False, message="Transaction not found", data=None
        )
    return send_response(
        status_code=200,
        success=True,
        message="Transaction retrieved successfully",
        data=transaction,
    )

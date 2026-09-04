from src.app.utils.sendResponse import send_response

from src.app.modules.transaction.transaction_service import create_transaction



def create_transaction_controller(db, payload, user_id):
    transaction = create_transaction(db, payload, user_id)
    return send_response(
        status_code=201,
        success=True,
        message="Transaction created successfully",
        data=transaction
    )

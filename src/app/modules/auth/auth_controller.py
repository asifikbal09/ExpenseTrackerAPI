from src.app.utils.sendResponse import send_response

from src.app.modules.auth import auth_service
from src.app.modules.user.user_validation import CrateUser, LoginUser


def register_user(payload: CrateUser, db):
    result = auth_service.registerUser(payload,db)
    return send_response(
        status_code=201,
        success=True,
        message="User registered successfully",
        data=result,
    )

def login_user(payload: LoginUser, db):
    result = auth_service.loginUser(payload,db)
    if not result:
        return send_response(
            status_code=401,
            success=False,
            message="Invalid email or password",
            data=None,
        )
    return send_response(
        status_code=200,
        success=True,
        message="User logged in successfully",
        data=result,
    )
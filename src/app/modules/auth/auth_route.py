from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.app.modules.auth.auth_controller import login_user, register_user
from src.app.modules.user.user_validation import CrateUser, LoginUser
from src.database import get_db

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

DB_DEPENDENCY = Depends(get_db)


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user_endpoint(payload: CrateUser, db: Session = DB_DEPENDENCY):
    return register_user(payload, db)

@auth_router.post("/login", status_code=status.HTTP_200_OK)
def login_user_endpoint(payload: LoginUser, db: Session = DB_DEPENDENCY):
    return login_user(payload, db)
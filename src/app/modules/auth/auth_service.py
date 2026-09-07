import os
from fastapi import HTTPException
from passlib.context import CryptContext
from dotenv import load_dotenv
load_dotenv()


from src.app.modules.user.uesr_model import User
from src.app.modules.user.user_validation import CrateUser, LoginUser
from src.app.utils.jwt_helper import generate_jwt_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





def registerUser(payload:CrateUser, db):
    
    hash_password = pwd_context.hash(payload.password)
    
    user = {
        "username": payload.username,
        "email": payload.email,
        "hash_password": hash_password,
    }
    
    new_user = User(**user)
    db.add(new_user)
    db.commit()
    
    return {
        "username": new_user.username,
        "email": new_user.email,
    }


def loginUser(payload:LoginUser, db):
    user = db.query(User).filter(User.username == payload.username).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not pwd_context.verify(payload.password, user.hash_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = generate_jwt_token(user.id, os.getenv("ACCESS_TOKEN_SECRET"), "HS256", int(os.getenv("ACCESS_TOKEN_EXPIRE_IN")))
    access_token_type = "Bearer"
    
    return {
        "username": user.username,
        "access_token": access_token,
        "token_type": access_token_type
    }


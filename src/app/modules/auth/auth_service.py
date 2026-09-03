from src.app.modules.user.user_validation import CrateUser, LoginUser
from src.app.modules.user.uesr_model import User
from passlib.context import CryptContext


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
    user = db.query(User).filter(User.email == payload.email).first()
    
    if not user:
        return None
    
    if not pwd_context.verify(payload.password, user.hash_password):
        return None
    
    return {
        "username": user.username,
        "email": user.email,
    }


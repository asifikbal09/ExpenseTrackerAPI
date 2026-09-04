from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt


def generate_jwt_token(
    user_id: UUID,
    secret_key: str,
    algorithm: str,
    expiration_minutes: int,
) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(
        minutes=expiration_minutes
    )

    payload = {
        "user_id": str(user_id),
        "exp": expiration_time,
    }

    return jwt.encode(
        payload,
        secret_key,
        algorithm=algorithm,
    )
    
def verify_jwt_token(
    token: str,
    secret_key: str,
    algorithm: str,
) -> dict:
    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=[algorithm],
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
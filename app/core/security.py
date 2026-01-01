from datetime import datetime, timedelta
from typing import Any, Union

# Dummy implementations for security utils

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    return "dummy_access_token_exemplar"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return plain_password == "password" # Dummy check

def get_password_hash(password: str) -> str:
    return "dummy_hashed_" + password

import os
import uuid
import hashlib
import hmac
import logging

logger = logging.getLogger(__name__)

def generate_secret(length: int = 32) -> str:
    return str(uuid.uuid4().hex)[:length]

def hash_password(password: str, salt: str) -> str:
    """Hash a password for storing."""
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 
                             salt.encode('utf-8'), 100000)

def verify_password(stored_password: str, provided_password: str, salt: str) -> bool:
    """Verify a stored password against one provided by user"""
    return hmac.compare_digest(hash_password(provided_password, salt), stored_password)

def generate_token(length: int = 32) -> str:
    return str(uuid.uuid4().hex)[:length]
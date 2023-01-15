import hashlib

from decouple import config
from passlib.hash import pbkdf2_sha256

PEPER = config("PEPER")


def encrypt_sha265(content: str) -> str:
    encoded_string = (PEPER + content).encode()
    return hashlib.sha256(encoded_string).hexdigest()


def gen_pbkdf2_sha256(content: str) -> str:
    return pbkdf2_sha256.hash(PEPER + content)


def verify_encryption(in_content: str, db_content: str) -> bool:
    return pbkdf2_sha256.verify(PEPER + in_content, db_content)

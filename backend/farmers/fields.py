from django.db import models
from cryptography.fernet import Fernet, InvalidToken
from django.conf import settings
from utils.fernet import fernet

class EncryptedCharField(models.CharField):
    def get_prep_value(self, value):
        if value:
            # Encrypt the value before saving it to the database
            encrypted = fernet.encrypt(value.encode()).decode()
            return encrypted
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            decrypted = settings.fernet.decrypt(value.encode()).decode()
            return decrypted
        except InvalidToken:
            return value  # fallback if already decrypted or token is invalid

    def to_python(self, value):
        if value is None or isinstance(value, str):
            return value
        try:
            return settings.fernet.decrypt(value.encode()).decode()
        except InvalidToken:
            return value

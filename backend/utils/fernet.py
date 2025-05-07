from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPTED_FIELDS_KEY)

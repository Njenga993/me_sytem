# encryption_utils.py

import os
from pathlib import Path
import environ
from cryptography.fernet import Fernet

# Define BASE_DIR to locate .env
BASE_DIR = Path(__file__).resolve().parent

# Initialize environment and load .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Read the encryption key
ENCRYPTED_FIELDS_KEY = env("ENCRYPTED_FIELDS_KEY")

# Create a Fernet instance for encryption/decryption
fernet = Fernet(ENCRYPTED_FIELDS_KEY)

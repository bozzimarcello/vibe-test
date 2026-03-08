#!/usr/bin/env python3
"""
Script to generate a strong secret key for JWT signing.
"""

import secrets
import string

def generate_secret_key(length=32):
    """Generate a cryptographically secure random secret key."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated Secret Key:")
    print(f"SECRET_KEY={secret_key}")
    print("\nAdd this to your .env file.")
    print("⚠️  Keep this key secure and never commit it to version control!")

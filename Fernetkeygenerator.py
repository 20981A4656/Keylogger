from cryptography.fernet import Fernet

# Generate a new encryption key
encryption_key = Fernet.generate_key()

print("Generated Encryption Key:", encryption_key)

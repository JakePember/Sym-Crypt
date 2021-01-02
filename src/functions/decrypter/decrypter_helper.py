from cryptography.fernet import Fernet


def decrypt_values(decipher_key, encrypted_keys):
    storage_locker = Fernet(decipher_key)
    deciphered_keys = []
    for encrypted_key in encrypted_keys:
        deciphered_keys.append(storage_locker.decrypt(encrypted_key))
    return deciphered_keys

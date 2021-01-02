from cryptography.fernet import Fernet


def encrypt_values(list_of_values, storage_locker):
    key_and_value_dict = {}
    for value in list_of_values:
        key_and_value_dict[value] = storage_locker.encrypt(value)
    return key_and_value_dict

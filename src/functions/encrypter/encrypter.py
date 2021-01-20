from cryptography.fernet import Fernet
from functions.encrypter.encrypter_helper import encrypt_values
from utils.user_questions import UserQuestions


class EncrypterHandler:

    @staticmethod
    def encrypter_handler():
        amt_to_encrypt = int(input('Number of values do you want to encrypt: '))

        # Prompts user to enter in the values they want encrypted or decrypted
        list_of_values = UserQuestions().get_user_crypt_values(amt_to_encrypt, 1)

        # Generate key and create the storage locker
        key = Fernet.generate_key()  # this is your "password"
        storage_locker = Fernet(key)  # Creates 'storage' that can only be opened with the new key

        dict_of_value_and_key = encrypt_values(list_of_values, storage_locker)

        print('--------------------------------------------------------------')
        print(f'Decipher Key: {key.decode("utf-8")}')
        print('--------------------------------------------------------------')
        for value, key in dict_of_value_and_key.items():
            print(f'VALUE: {value.decode("utf-8")}')
            print(f'KEY  : {key.decode("utf-8")} \n')

from utils.user_questions import UserQuestions
from functions.decrypter.decrypter_helper import decrypt_values


class DecryptHandler:
    @staticmethod
    def decrypt_handler():
        decipher_key = UserQuestions().get_decipher_key()
        amt_to_decrypt = int(input('Number of values you want to encrypt: '))

        list_of_encryption_values = UserQuestions().get_user_crypt_values(amt_to_decrypt, 2)

        deciphered_values = decrypt_values(decipher_key, list_of_encryption_values)

        for value in deciphered_values:
            print(f'VALUE: {value.decode("utf-8")}')

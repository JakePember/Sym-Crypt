import getpass


class UserQuestions:
    @staticmethod
    def get_user_crypt_values(amount_of_crypt_values, crypt_path):
        method_type = ''
        value_type = ''
        if crypt_path == 1:
            method_type = 'encrypt'
            value_type = 'value'
        if crypt_path == 2:
            method_type = 'decrypt'
            value_type = 'encrypted value key'

        # Get the user values to encrypt
        list_of_values = []
        for x in range(1, amount_of_crypt_values + 1):
            value = input(f'Enter {value_type} {x} of {amount_of_crypt_values} to {method_type}: ')

            list_of_values.append(bytes(value, 'utf-8'))
        return list_of_values

    @staticmethod
    def get_decipher_key():
        key = input(f'What is the decipher key: ')
        return bytes(key, 'utf-8')

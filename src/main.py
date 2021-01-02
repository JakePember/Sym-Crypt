from functions.encrypter.encrypter import encrypter_handler
from functions.decrypter.decrypter import decrypt_handler

if __name__ == '__main__':
    path = int(input(f'Encrypt(1) OR Decrypt(2): '))

    if path == 1:
        encrypter_handler()
    else:
        decrypt_handler()

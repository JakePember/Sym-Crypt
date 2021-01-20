from functions.encrypter.encrypter import EncrypterHandler
from functions.decrypter.decrypter import DecryptHandler

if __name__ == '__main__':
    path = int(input(f'Encrypt(1) OR Decrypt(2): '))

    if path == 1:
        EncrypterHandler().encrypter_handler()
    else:
        DecryptHandler().decrypt_handler()

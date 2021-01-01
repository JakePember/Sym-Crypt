from cryptography.fernet import Fernet


# username = bytes('financials@bles.co', 'utf-8')
# password = bytes('Zie2uCEdljT5ryfO', 'utf-8')
# username = bytes('some_email@some_provider.com', 'utf-8')
# password = bytes('super_secure_password', 'utf-8')
#
# key = Fernet.generate_key()  # this is your "password"
# cipher_suite = Fernet(key)
# encoded_username = cipher_suite.encrypt(username)
# encoded_password = cipher_suite.encrypt(password)
#
# print(f'KEY: {key}')
# print(f'encoded_username: {encoded_username}')
# print(f'encoded_password: {encoded_password}')


# cipher_suite = Fernet(b'PkMSP6ydCA37au230TdkN6EHRh_8V7q6IS3zKEr1RO4=')
# decypted_username = cipher_suite.decrypt(b'gAAAAABf6NjcO4TD1UYs5kebHfSXfZy_Y4S0TEkba6Gx7Rg4uN3sDLQToA7-bdh89gl_c4x0dyOWhzllamiHFSnbqTQZoHL_YUjo-DOdONzE8MjhTnYCWFs=')
# decrypted_password = cipher_suite.decrypt(b'gAAAAABf6NjcEUvakjqC5VNYGFH8sKJzykk2Uob-a39gNXo2zDK10b7lWL_sN2D3fCGexkloaKywaoBntQXxynTmSfELVM0a1Rm3WJvZPWN_4mBYdn5sHJU=')

# print(f'encoded_username: {decypted_username}')
# print(f'encoded_password: {decrypted_password}')

def encrypt_values(values):
    key_and_value_dict = {}
    for value in list_of_values:
        key_and_value_dict[value] = storage_locker.encrypt(value)
    return key_and_value_dict


amt_of_values = int(input('Number of values do you want to encrypt: '))

list_of_values = []
for x in range(1, amt_of_values + 1):
    list_of_values.append(bytes(input(f'Enter value {x}: '), 'utf-8'))

key = Fernet.generate_key()  # this is your "password"
storage_locker = Fernet(key)  # Creates 'storage' that can only be opened with the new key

value_key_dict = encrypt_values(list_of_values)

print(value_key_dict)

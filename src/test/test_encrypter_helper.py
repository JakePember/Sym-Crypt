import unittest
from cryptography.fernet import Fernet

from context import encrypt_values

mock_key_value = 'O4DFjZBz0J716Wjd-BMfsqPLGp25E9kgSP-IaO82zKo='
mock_username_value = 'gAAAAABf-3WXNYS3TcH4-UlEicH8jRQIkUG6n0QforvKnchF5fprSzpOO63kibijtc22zZ2C9Wy31IzvzcWb0fghAXhyPqVKYw=='
mock_password_value = 'gAAAAABf-3WXSGgQlErNxFiM70D-kgOoFcDyNdmuxQ9yFj8xW3HbvAI7RtpDdggLQeBpKiX0QsiwSzSr-hP-eSAWiqleCpKVxg=='


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_encrypt_values(self):
        # Generate key and create the storage locker
        storage_locker = Fernet(Fernet.generate_key())  # Creates 'storage' that can only be opened with the new key

        result = encrypt_values([b'user_john_doe', b'password_1234'], storage_locker)
        print()
        actual = {
            b'user_john_doe': b'gAAAAABgB5absY_-iMDDoOV_KoxsjQaFjTf572xiRpLTYlBs1PGrLU3iOuNbMPvR2hr9uOO4aP2BVGywfhD-DtLEhWeDzLTHlA==',
            b'password_1234': b'gAAAAABgB5ab25h5ZlEyRor_zTR6cSN1ieilUI98c9w7zbfIwfMswBBf3FcN0fBiv_sqaMjjvuoKzE3eZrbF8eQKsuapL4kIjQ=='
        }
        self.assertEqual(list(result.items())[0][0], b'user_john_doe')
        self.assertRegex((list(result.items())[0][1]).decode('utf-8'), r'[A-Za-z0-9=_-]{99}')

        self.assertEqual(list(result.items())[1][0], b'password_1234')
        self.assertRegex((list(result.items())[1][1]).decode('utf-8'), r'[A-Za-z0-9=_-]{99}')


if __name__ == '__main__':
    unittest.main()

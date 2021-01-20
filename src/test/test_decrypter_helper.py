import unittest

from context import decrypt_values

mock_key_value = 'O4DFjZBz0J716Wjd-BMfsqPLGp25E9kgSP-IaO82zKo='
mock_username_value = 'gAAAAABf-3WXNYS3TcH4-UlEicH8jRQIkUG6n0QforvKnchF5fprSzpOO63kibijtc22zZ2C9Wy31IzvzcWb0fghAXhyPqVKYw=='
mock_password_value = 'gAAAAABf-3WXSGgQlErNxFiM70D-kgOoFcDyNdmuxQ9yFj8xW3HbvAI7RtpDdggLQeBpKiX0QsiwSzSr-hP-eSAWiqleCpKVxg=='


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_decrypt_values(self):
        result_keys = decrypt_values(mock_key_value, [bytes(mock_username_value, 'utf-8'), bytes(mock_password_value, 'utf-8')])
        self.assertEqual(result_keys, [b'user_john_doe', b'password_1234'])


if __name__ == '__main__':
    unittest.main()

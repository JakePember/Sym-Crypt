import unittest
from unittest.mock import patch

from context import UserQuestions

mock_key_value = 'O4DFjZBz0J716Wjd-BMfsqPLGp25E9kgSP-IaO82zKo='
mock_username_encode = 'gAAAAABf-3WXNYS3TcH4-UlEicH8jRQIkUG6n0QforvKnchF5fprSzpOO63kibijtc22zZ2C9Wy31IzvzcWb0fghAXhyPqVKYw=='
mock_password_encode = 'gAAAAABf-3WXSGgQlErNxFiM70D-kgOoFcDyNdmuxQ9yFj8xW3HbvAI7RtpDdggLQeBpKiX0QsiwSzSr-hP-eSAWiqleCpKVxg=='


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    @patch('builtins.input')
    def test_get_user_crypt_values(self, mock_input):
        mock_input.side_effect = ['user_john_doe', 'pass_1234', mock_username_encode, mock_password_encode]

        result = UserQuestions.get_user_crypt_values(2, 1)  # encrypt path
        self.assertEqual(result, [b'user_john_doe', b'pass_1234'])

        result = UserQuestions.get_user_crypt_values(2, 2)  # decrypt path
        self.assertEqual(result, [bytes(mock_username_encode, 'utf-8'), bytes(mock_password_encode, 'utf-8')])

    @patch('builtins.input')
    def test_get_decipher_key(self, mock_input):
        mock_input.side_effect = [mock_key_value]

        result = UserQuestions.get_decipher_key()
        self.assertEqual(result, bytes(mock_key_value, 'utf-8'))


if __name__ == '__main__':
    unittest.main()

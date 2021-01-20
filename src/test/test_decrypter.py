import unittest
import io
import sys
from unittest.mock import patch
from unittest.mock import Mock

from context import DecryptHandler, UserQuestions

mock_key_value = 'O4DFjZBz0J716Wjd-BMfsqPLGp25E9kgSP-IaO82zKo='
mock_username_value = 'gAAAAABf-3WXNYS3TcH4-UlEicH8jRQIkUG6n0QforvKnchF5fprSzpOO63kibijtc22zZ2C9Wy31IzvzcWb0fghAXhyPqVKYw=='
mock_password_value = 'gAAAAABf-3WXSGgQlErNxFiM70D-kgOoFcDyNdmuxQ9yFj8xW3HbvAI7RtpDdggLQeBpKiX0QsiwSzSr-hP-eSAWiqleCpKVxg=='


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    @patch('context.UserQuestions.get_decipher_key')
    @patch('builtins.input')
    def test_get_key_env(self, mock_input, mock_decipher_key):
        output = io.StringIO()  # console out will be stored here
        sys.stdout = output  # redirecting stdout
        mock_decipher_key.return_value = mock_key_value
        mock_input.side_effect = [2, mock_username_value, mock_password_value]
        DecryptHandler.decrypt_handler()
        self.assertEqual(output.getvalue(), 'VALUE: user_john_doe\nVALUE: password_1234\n')


if __name__ == '__main__':
    unittest.main()

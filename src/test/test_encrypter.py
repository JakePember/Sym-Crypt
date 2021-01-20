import unittest
import io
import sys
import re
from unittest.mock import patch
from unittest.mock import Mock

from context import UserQuestions, EncrypterHandler

mock_key_value = 'O4DFjZBz0J716Wjd-BMfsqPLGp25E9kgSP-IaO82zKo='
mock_username_value = 'gAAAAABf-3WXNYS3TcH4-UlEicH8jRQIkUG6n0QforvKnchF5fprSzpOO63kibijtc22zZ2C9Wy31IzvzcWb0fghAXhyPqVKYw=='
mock_password_value = 'gAAAAABf-3WXSGgQlErNxFiM70D-kgOoFcDyNdmuxQ9yFj8xW3HbvAI7RtpDdggLQeBpKiX0QsiwSzSr-hP-eSAWiqleCpKVxg=='


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    # @patch('context.UserQuestions.get_user_crypt_values')
    @patch('builtins.input')
    def test_get_key_env(self, mock_input):
        output = io.StringIO()  # console out will be stored here
        sys.stdout = output  # redirecting stdout
        # mock_crypt_values.return_value = [b'user_john_doe', b'pass_1234']
        mock_input.side_effect = [2, 'user_john_doe', 'pass_1234']
        EncrypterHandler.encrypter_handler()
        self.assertRegex(output.getvalue(), r'Decipher Key: [A-Za-z0-9=_-]{44}')
        self.assertRegex(output.getvalue(), r'VALUE: user_john_doe\nKEY  : [A-Za-z0-9=_-]{99}')
        self.assertRegex(output.getvalue(), r'VALUE: pass_1234\nKEY  : [A-Za-z0-9=_-]{99}')


if __name__ == '__main__':
    unittest.main()

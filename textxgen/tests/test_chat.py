# tests/test_chat.py

import unittest
from unittest.mock import patch
from textxgen.endpoints.chat import ChatEndpoint
from textxgen.exceptions import InvalidInputError


class TestChatEndpoint(unittest.TestCase):
    def setUp(self):
        self.chat = ChatEndpoint()

    @patch("textxgen.client.APIClient._make_request")
    def test_chat_success(self, mock_make_request):
        """Test successful chat request."""
        mock_make_request.return_value = {"choices": [{"message": {"content": "Hello!"}}]}

        response = self.chat.chat(messages=[{"role": "user", "content": "Hello"}])
        self.assertEqual(response, {"choices": [{"message": {"content": "Hello!"}}]})

    def test_chat_invalid_input(self):
        """Test invalid input for chat."""
        with self.assertRaises(InvalidInputError):
            self.chat.chat(messages=[])

        with self.assertRaises(InvalidInputError):
            self.chat.chat(messages="invalid")


if __name__ == "__main__":
    unittest.main()
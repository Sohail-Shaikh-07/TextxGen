# tests/test_completions.py

import unittest
from unittest.mock import patch
from textxgen.endpoints.completions import CompletionsEndpoint
from textxgen.exceptions import InvalidInputError


class TestCompletionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.completions = CompletionsEndpoint()

    @patch("textxgen.client.APIClient._make_request")
    def test_complete_success(self, mock_make_request):
        """Test successful completion request."""
        mock_make_request.return_value = {"completions": [{"text": "Once upon a time"}]}

        response = self.completions.complete(prompt="Once upon a time")
        self.assertEqual(response, {"completions": [{"text": "Once upon a time"}]})

    def test_complete_invalid_input(self):
        """Test invalid input for completion."""
        with self.assertRaises(InvalidInputError):
            self.completions.complete(prompt="")

        with self.assertRaises(InvalidInputError):
            self.completions.complete(prompt=None)


if __name__ == "__main__":
    unittest.main()
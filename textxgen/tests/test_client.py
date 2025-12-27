# tests/test_client.py

import unittest
from unittest.mock import patch, Mock
from textxgen.client import APIClient
from textxgen.exceptions import APIError


class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("requests.request")
    def test_make_request_success(self, mock_request):
        """Test successful API request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": "success"}
        mock_request.return_value = mock_response

        response = self.client._make_request("/test", method="GET")
        self.assertEqual(response, {"result": "success"})

    @patch("requests.request")
    def test_make_request_failure(self, mock_request):
        """Test failed API request."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = Exception("Bad Request")
        mock_request.return_value = mock_response

        with self.assertRaises(APIError):
            self.client._make_request("/test", method="GET")


if __name__ == "__main__":
    unittest.main()
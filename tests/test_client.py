import pytest
from unittest.mock import patch, Mock
from jsonplaceholder.client import JsonPlaceholder


class TestJsonPlaceholder:
    @pytest.fixture
    def api_client(self):
        return JsonPlaceholder()

    @patch('requests.request')
    def test_get_all_posts(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.json.return_value = [{"id": 1}, {"id": 2}]
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        result = api_client.get_all_posts()
        assert len(result) == 2

    # Add more test methods for other functionality
import pytest
from unittest.mock import patch, Mock
from jsonplaceholder.client import JsonPlaceholder
import requests

class TestJsonPlaceholder:
    @pytest.fixture
    def api_client(self):
        return JsonPlaceholder()

    @patch('requests.request')
    def test_get_all_posts(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.json.return_value = [{"id": 1}, {"id": 2}]
        mock_response.headers = {}
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        data, headers = api_client.get_all_posts()
        assert len(data) == 2
        assert headers == {}

    @patch('requests.request')
    def test_get_post(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.json.return_value = {"id": 10, "title": "Test Post"}
        mock_response.headers = {"X-Powered-By": "Express"}
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        data, headers = api_client.get_post(10)
        assert data["title"] == "Test Post"
        assert headers["X-Powered-By"] == "Express"

    @patch('requests.request')
    def test_get_comments_for_post(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.json.return_value = [{"id": 1, "postId": 8}]
        mock_response.headers = {}
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        data, _ = api_client.get_comments_for_post(8)
        assert data[0]["postId"] == 8

    @patch('requests.request')
    def test_update_comment(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "new", "email": "new@test.com"}
        mock_response.headers = {}
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        data, _ = api_client.update_comment(1, {"name": "new", "email": "new@test.com"})
        assert data["id"] == 1

    @patch('requests.request')
    def test_error_handling(self, mock_request, api_client):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        data, headers = api_client.get_post(999)
        assert data is None
        assert headers is None
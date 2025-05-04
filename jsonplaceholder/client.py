import requests
import json


class JsonPlaceholder:
    """
    A client for interacting with the JSONPlaceholder API.
    Handles all operations for posts, comments, and users endpoints.
    """

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        """
        Initialize the API client with base URL.
        
        Args:
            base_url (str): Base URL for the API endpoint
        """
        self.base_url = base_url

    def _make_request(self, endpoint, method="GET", params=None, data=None):
        """
        Internal method to handle API requests with error handling.
        
        Args:
            endpoint (str): API endpoint to call
            method (str): HTTP method (GET, POST, etc.)
            params (dict): Query parameters
            data (dict): Request body data
            
        Returns:
            tuple: (response_data, response_headers) or (None, None) on failure
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method, 
                url, 
                params=params, 
                json=data,
                headers={'Accept': 'application/json'}
            )
            response.raise_for_status()
            return response.json(), response.headers
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
            print(f"Status code: {getattr(response, 'status_code', 'No response')}")
            return None, None

    def get_all_posts(self):
        """Retrieve all posts from the API."""
        return self._make_request("/posts")

    def get_post(self, post_id):
        """Retrieve a specific post by ID."""
        return self._make_request(f"/posts/{post_id}")

    def get_posts_by_user(self, user_id):
        """Retrieve all posts for a specific user."""
        return self._make_request("/posts", params={"userId": user_id})

    def get_comments_for_post(self, post_id):
        """Retrieve all comments for a specific post."""
        return self._make_request(f"/posts/{post_id}/comments")

    def update_comment(self, comment_id, data):
        """Update a comment with new data using PUT method."""
        return self._make_request(f"/comments/{comment_id}", method="PUT", data=data)

    def get_all_users(self):
        """Retrieve all users from the API."""
        return self._make_request("/users")
import requests
import json


class JsonPlaceholder:
    """
    A client for interacting with the JSONPlaceholder API (https://jsonplaceholder.typicode.com/).
    Encapsulates common operations for posts, comments, and users endpoints.
    """

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        """
        Initialize the client with the base URL of the API.
        
        Args:
            base_url (str): The base URL of the JSONPlaceholder API. 
                           Defaults to "https://jsonplaceholder.typicode.com".
        """
        self.base_url = base_url

    def _make_request(self, endpoint, method="GET", params=None, data=None):
        """
        Internal method to make HTTP requests to the API with error handling.
        
        Args:
            endpoint (str): The API endpoint to call (e.g., "/posts")
            method (str): HTTP method (GET, POST, PUT, etc.)
            params (dict): Query parameters for the request
            data (dict): Data to send in the request body
            
        Returns:
            dict or list: Parsed JSON response if successful, None otherwise
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, params=params, json=data)
            response.raise_for_status()  # Raises exception for 4XX/5XX status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
            print(f"Status code: {getattr(response, 'status_code', 'No response')}")
            return None

    def get_all_posts(self):
        """Retrieve all posts from the API."""
        return self._make_request("/posts")

    def get_post(self, post_id):
        """
        Retrieve a specific post by ID.
        
        Args:
            post_id (int): The ID of the post to retrieve
            
        Returns:
            dict: The post data if found, None otherwise
        """
        return self._make_request(f"/posts/{post_id}")

    def get_posts_by_user(self, user_id):
        """
        Retrieve all posts for a specific user.
        
        Args:
            user_id (int): The user ID to filter posts by
            
        Returns:
            list: A list of posts by the specified user
        """
        return self._make_request("/posts", params={"userId": user_id})

    def get_comments_for_post(self, post_id):
        """
        Retrieve all comments for a specific post.
        
        Args:
            post_id (int): The post ID to get comments for
            
        Returns:
            list: A list of comments for the specified post
        """
        return self._make_request(f"/posts/{post_id}/comments")

    def update_comment(self, comment_id, data):
        """
        Update a comment with new data using PUT method.
        
        Args:
            comment_id (int): The ID of the comment to update
            data (dict): The new data for the comment
            
        Returns:
            dict: The updated comment data if successful, None otherwise
        """
        return self._make_request(f"/comments/{comment_id}", method="PUT", data=data)
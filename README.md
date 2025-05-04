# JSONPlaceholder API Client

A Python client for interacting with the JSONPlaceholder API.

## Features

- Retrieve posts, comments, and users
- Filter by user ID or post ID
- Update resources
- Error handling

## Installation

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/bin/activate` (mac) or `.\venv\Scripts\Activate.ps1` (windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run test: `pytest tests/test_client.py`
6. Run app: `python main.py`

## Usage

```python
from jsonplaceholder.client import JsonPlaceholder

api = JsonPlaceholder()
posts = api.get_all_posts()
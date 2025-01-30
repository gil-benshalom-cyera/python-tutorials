import pytest
from unittest.mock import MagicMock
from dependency_injection.api_client import APIClient
from dependency_injection.data_handler import DataHandler


@pytest.fixture
def mock_api_client():
    """Creates a mock for APIClient."""
    mock_client = MagicMock(spec=APIClient)

    # Mock data similar to what the real API returns
    mock_client.fetch_data.return_value = [
        {"title": "Post One", "body": "This is the body of post one with many words."},
        {"title": "Post Two", "body": "Another post body that has a different length."},
        {"title": "Special Keyword", "body": "Keyword-specific post that should be tested."},
    ]
    return mock_client


def test_get_top_posts(mock_api_client):
    """Test that get_top_posts returns the expected number of posts."""
    handler = DataHandler(mock_api_client)
    posts = handler.get_top_posts(limit=2, word_limit=3)

    assert len(posts) == 2
    assert posts[0]["title"] == "Post One"
    assert posts[0]["body"] == "This is the"
    assert posts[1]["title"] == "Post Two"
    assert posts[1]["body"] == "Another post body"


def test_get_top_posts_with_keyword(mock_api_client):
    """Test filtering functionality using a keyword."""
    handler = DataHandler(mock_api_client)
    posts = handler.get_top_posts(limit=5, word_limit=4, keyword="keyword")

    assert len(posts) == 1
    assert posts[0]["title"] == "Special Keyword"
    assert posts[0]["body"] == "Keyword-specific post that should"


def test_get_top_posts_empty_response():
    """Test the case where the API returns an empty list."""
    mock_client = MagicMock(spec=APIClient)
    mock_client.fetch_data.return_value = []

    handler = DataHandler(mock_client)
    posts = handler.get_top_posts()

    assert posts == []  # Should return an empty list


def test_get_top_posts_exceeds_available(mock_api_client):
    """Test that get_top_posts does not return more posts than available."""
    handler = DataHandler(mock_api_client)
    posts = handler.get_top_posts(limit=10)

    assert len(posts) == 3  # Only 3 posts exist in mock


def test_get_top_posts_network_failure():
    """Test how DataHandler behaves when APIClient returns an error (empty list)."""
    mock_client = MagicMock(spec=APIClient)
    mock_client.fetch_data.return_value = []  # Simulating a failed request

    handler = DataHandler(mock_client)
    posts = handler.get_top_posts(limit=5)

    assert posts == []  # Should return an empty list

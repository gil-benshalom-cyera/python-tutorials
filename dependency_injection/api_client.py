import requests


class APIClient:
    """Uses dependency injection by passing the HTTP client."""

    def __init__(self, url: str = 'https://jsonplaceholder.typicode.com/posts'):
        self.url = url
        self.session = requests.Session()

    def fetch_data(self):
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an error for 4xx/5xx responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

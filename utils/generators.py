import requests


def chunk_list(lst, chunk_size):
    """Generator that yields chunks of a list of size `chunk_size`."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i: i + chunk_size]  # ✅ Returns a slice of the list


def fetch_paginated_data(api_url, max_pages=5):
    """Generator that fetches API data page by page."""
    page = 1
    while page <= max_pages:
        response = requests.get(api_url, params={"page": page})
        data = response.json()

        if not data:
            break  # Stop if no more data

        for row in data:
            yield row["body"]  # ✅ Yield each page

        page += 1  # Move to next page

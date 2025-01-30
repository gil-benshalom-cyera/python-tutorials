from utils.generators import fetch_paginated_data

API_URL = "https://jsonplaceholder.typicode.com/posts"  # Fake API


def main():
    # Example Usage

    for page_data in fetch_paginated_data(API_URL, max_pages=3):
        print(f"Page: {page_data}...")  # Print first 2 items per page


if __name__ == '__main__':
    main()

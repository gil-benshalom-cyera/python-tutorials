from dependency_injection.api_client import APIClient


class DataHandler:
    """Uses dependency injection by passing the API client."""

    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_top_posts(self, limit: int = 10, word_limit: int = 5, keyword: str = None):
        posts = self.api_client.fetch_data()
        structured_output = []
        count = 0

        for post in posts:
            if count >= limit:
                break

            if keyword and keyword.lower() not in post["title"].lower():
                continue  # Skip posts that do not contain the keyword

            output = {
                "title": post["title"],
                "body": ' '.join(post["body"].split(' ')[0:word_limit])
            }
            structured_output.append(output)
            count += 1

        return structured_output



def main():
    api_client = APIClient(url='https://jsonplaceholder.typicode.com/posts')
    data_handler = DataHandler(api_client=api_client)
    top_posts = data_handler.get_top_posts(limit=5)
    print(top_posts)


if __name__ == '__main__':
    main()

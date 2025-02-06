from utils.decorators import save_to_dict


# Example Usage
cache = {}

@save_to_dict(cache)
def fetch_data(key):
    """Simulates fetching data (output must be a dictionary)."""
    return {"data": f"Value for {key}"}



def main():
    fetch_data("user1")
    fetch_data("user2")
    print(cache)


if __name__ == '__main__':
    main()
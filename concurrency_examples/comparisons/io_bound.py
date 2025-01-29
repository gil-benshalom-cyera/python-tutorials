import threading
import multiprocessing
import asyncio
import requests
import aiohttp
from utils.decorators import time_it

# 2. API Setup
API_URL = "https://jsonplaceholder.typicode.com/posts/{}"
POST_IDS = list(range(1, 51))  # Fetch 50 posts


# 3. Synchronous (Single-threaded) Requests
def fetch_post(post_id):
    """Fetch a post from the API (blocking request)."""
    response = requests.get(API_URL.format(post_id))
    return response.json()


@time_it
def run_single_thread():
    """Fetch posts synchronously (one at a time)."""
    return [fetch_post(post_id) for post_id in POST_IDS]


# 4. Multithreading for Concurrent Requests
@time_it
def run_multithreading():
    """Fetch posts using multiple threads."""
    threads = []
    results = []

    def worker(post_id):
        results.append(fetch_post(post_id))

    for _post_id in POST_IDS:
        thread = threading.Thread(target=worker, args=(_post_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


# 5. Multiprocessing (Not Ideal for I/O)
@time_it
def run_multiprocessing():
    """Fetch posts using multiple processes."""
    with multiprocessing.Pool(processes=8) as pool:  # 8 parallel processes
        results = pool.map(fetch_post, POST_IDS)
    return results


# 6. AsyncIO + AIOHTTP (Best for High-Concurrency I/O)
async def fetch_post_async(session, post_id):
    """Async function to fetch a post using aiohttp (disabling SSL verification)."""
    async with session.get(API_URL.format(post_id), ssl=False) as response:
        return await response.json()


@time_it
def run_asyncio():
    """Fetch posts using asyncio."""

    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_post_async(session, post_id) for post_id in POST_IDS]
            return await asyncio.gather(*tasks)

    return asyncio.run(main())


def execute():
    print("=== API REQUESTS BENCHMARK ===")
    run_single_thread()
    run_multithreading()
    run_multiprocessing()
    run_asyncio()


# 7. Execution
if __name__ == "__main__":
    execute()

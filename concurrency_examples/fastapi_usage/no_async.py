import time
from fastapi import FastAPI

# https://blog.apify.com/python-asyncio-tutorial/

app = FastAPI()


@app.get('/')
def read_root() -> dict:
    time.sleep(1)  # Simulating a delay, e.g., fetching data or processing
    return {'Hello': 'World'}

# uvicorn no_async:app --reload
# wrk -t12 -c400 -d15s http://127.0.0.1:8000/

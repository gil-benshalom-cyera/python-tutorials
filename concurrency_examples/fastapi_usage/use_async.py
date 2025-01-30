import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root() -> dict:
    await asyncio.sleep(1)  # Simulating a delay
    return {'Hello': 'World'}

# uvicorn use_async:app --reload
# wrk -t12 -c400 -d15s http://127.0.0.1:8000/

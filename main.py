from typing import Union

from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(auth_router)
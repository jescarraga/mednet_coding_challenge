from fastapi import FastAPI
from .routers import convert


app = FastAPI()

app.include_router(convert.router)

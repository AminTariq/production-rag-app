from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(".env")

from routes import base

app = FastAPI()

app.include_router(base.base_router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class GreetingRequest(BaseModel):
    name: str


@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello, {name}!"
    }

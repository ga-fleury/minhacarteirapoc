from fastapi import FastAPI
from mangum import Mangum
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)
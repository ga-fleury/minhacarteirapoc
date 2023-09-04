from fastapi import FastAPI
from mangum import Mangum
import json

app = FastAPI()

@app.get("/")
async def root():
    return {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": json.dumps({
            "message": "Hello World"
        }),
        "isBaseEncoded64": "false"
        }

handler = Mangum(app=app)
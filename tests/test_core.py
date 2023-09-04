from fastapi.testclient import TestClient
from api.main import app
import json

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": json.dumps({
            "message": "Hello World"
        }),
        "isBaseEncoded64": "false"
        }
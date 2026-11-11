from fastapi.testclient import TestClient
from app import app
from model import predict_square

client = TestClient(app)

def test_predict_square():
    assert predict_square(3) == 9
    assert predict_square(0) == 0
    assert predict_square(-2) == 4

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200

def test_api_predict():
    response = client.get("/predict/5")
    assert response.status_code == 200
    assert response.json() == {"input": 5.0, "prediction": 25.0}
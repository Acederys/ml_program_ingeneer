from fastapi.testclient import TestClient
from API_main import app
import httpx
client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message':'Helloworld'}

def test_predict():
    response = client.post("/predict/", json={"text":"I live in Moscow"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Я живу в Москве.'
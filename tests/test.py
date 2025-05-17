from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/ask", json={
        "question": "سلول گیاهی چیست؟"
    })
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "source_passage" in response.json()

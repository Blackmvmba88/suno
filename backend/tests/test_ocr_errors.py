import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ocr_with_invalid_data_returns_500():
    # send random bytes that are not a valid image
    r = client.post('/api/ocr', files={'file': ('test.bin', b'not-an-image', 'application/octet-stream')})
    assert r.status_code == 500
    assert 'error' in r.json()

from app.main import app
from fastapi.testclient import TestClient

testclient = TestClient(app)


def test_auth():
    response = testclient.post(
        "/user/login",
        json={
            "email": "muhammadtalhasaleem.2004@gmail.com",
            "password": "Talha-61555@"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    
    
def test_false_auth():
    
    response=testclient.post(
        '/user/login',
        json={
             "email": "muhammadtalhasaleem.2004@gmail.com",
             "password": "Talha-61555"
        }
    )
    
    assert response.status_code==400
    
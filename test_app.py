import pytest
from app import app  # make sure your Flask app is named app.py

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Flask App" in response.data


def test_addition(client):
    # test simple addition
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert b"3 + 5 = 8" in response.data

    # test addition with negative number
    response = client.get("/add/-2/7")
    assert response.status_code == 200
    assert b"-2 + 7 = 5" in response.data


def test_reverse_query(client):
    # test reversing a normal string
    response = client.get("/reverse?q=hello")
    assert response.status_code == 200
    assert b"hello: olleh" in response.data

    # test reversing empty string
    response = client.get("/reverse?q=")
    assert response.status_code == 200
    assert b": " in response.data


def test_reverse_missing_param(client):
    # test when query parameter is missing
    response = client.get("/reverse")
    assert response.status_code == 200
    assert b"<p>: </p>" in response.data

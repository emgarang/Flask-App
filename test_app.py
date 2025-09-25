import pytest
from webbapp import app

@pytest.fixture
def client():
    return app.test_client()

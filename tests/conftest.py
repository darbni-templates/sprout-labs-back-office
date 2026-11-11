import pytest

from backoffice import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.sqlite")})
    return app.test_client()


@pytest.fixture
def manager(client):
    """A client logged in as Khalid, the shop manager."""
    client.post("/login", data={"username": "khalid", "password": "manager123"})
    return client

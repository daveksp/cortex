from fastapi.testclient import TestClient

from cortex import __version__
from cortex.main import app
from cortex.shared.config import settings


def test_root_returns_application_metadata() -> None:
    response = TestClient(app).get("/")

    assert response.status_code == 200
    assert response.json() == {
        "name": settings.app_name,
        "version": __version__,
        "environment": settings.environment,
    }

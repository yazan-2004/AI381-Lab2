from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_setosa():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 200
    assert response.json()["species"] == "setosa"


def test_predict_returns_valid_species():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 6.0,
            "sepal_width": 2.9,
            "petal_length": 4.5,
            "petal_width": 1.5,
        },
    )
    assert response.status_code == 200
    assert response.json()["species"] in {
        "setosa",
        "versicolor",
        "virginica",
    }


def test_missing_field_is_rejected():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
        },
    )
    assert response.status_code == 422


def test_non_positive_measurement_is_rejected():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 0,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 422
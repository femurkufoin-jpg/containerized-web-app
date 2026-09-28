from app import create_app


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_visits():
    app = create_app()
    client = app.test_client()

    first_response = client.get("/visits")
    second_response = client.get("/visits")

    assert first_response.status_code == 200
    assert first_response.get_json() == {"visits": 1}

    assert second_response.status_code == 200
    assert second_response.get_json() == {"visits": 2}
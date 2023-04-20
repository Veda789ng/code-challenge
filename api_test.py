import pytest
from .app import app

@pytest.fixture(scope="module")
def test_client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_weather(test_client):
    response = test_client.get('weather/')
    assert response.status_code == 200
    response = test_client.get('weather/?date=19850101&station=USC00257715')
    assert response.json[0]["station"] == "USC00257715"
    assert response.json[0]["date"] == "19850101"
    response = test_client.get('weather/?date=19860101&station=USC00110187')
    assert response.json[0]["station"] == "USC00110187"
    assert response.json[0]["date"] == "19860101"

def test_stats(test_client):
    response = test_client.get('weather/stats')
    assert response.status_code == 200
    response = test_client.get('weather/stats?date=19850101&station=USC00257715')
    assert response.json[0]["station"] == "USC00257715"
    assert response.json[0]["date"] == "19850101"
    response = test_client.get('weather/stats?date=19860101&station=USC00110187')
    assert response.json[0]["station"] == "USC00110187"
    assert response.json[0]["date"] == "19860101"
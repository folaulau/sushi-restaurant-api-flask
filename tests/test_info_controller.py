from app import app

def test_home(client):
    app.logger.info('test_home')

    response = client.get('/')

    assert response.status_code == 200
    assert response.json == {"status":"Welcome to Sushi API"}

def test_ping(client):
    app.logger.info('test_ping')

    response = client.get('/ping')

    assert response.status_code == 200
    assert response.json == {"status":"good"}

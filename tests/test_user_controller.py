from app import app

def test_sign_up(client):
    app.logger.info('test_home')

    response = client.post('/authenticate', json={
        "token": "asdfsadfjlajl;kasjdf",
        "rememberMe": True
    })

    assert response.status_code == 200

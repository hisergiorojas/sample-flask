import json

def test_index(app, client):
    res = client.get('/api/usd')
    assert res.status_code == 200

def test_api_usd(app, client):
    res = client.post('/api/usd')
    assert res.status_code == 200

def test_api_usd_file(app, client):
    res = client.post('/api/usd', {})
    assert res.status_code == 200
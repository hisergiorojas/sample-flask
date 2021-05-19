from werkzeug.datastructures import FileStorage
import json
import os


def test_index(app, client):
    res = client.get('/api/usd')
    assert res.status_code == 200

def test_api_usd_no_file(app, client):
    res = client.post('/api/usd')
    assert res.status_code == 500

def test_api_usd_file(app, client):
    avocado = os.path.join('tests/assets/Avocado.glb')

    file = FileStorage(
        stream=open(avocado, 'rb'),
        filename='Avocado.glb',
        content_type='glb'
    )

    res = client.post(
        '/api/usd',
        data={
            'file': file
        },
        content_type='multipart/form-data'
    )
    assert res.status_code == 200

def test_api_usd_name(app, client):
    avocado = os.path.join('tests/assets/Avocado.glb')

    file = FileStorage(
        stream=open(avocado, 'rb'),
        filename='Avocado.glb',
        content_type='glb'
    )

    res = client.post(
        '/api/usd',
        data = {
            'file': file
        },
        content_type='multipart/form-data'
    )
    assert res.status_code == 200

    # The file is one of supported file
    # The model is converted to .usd
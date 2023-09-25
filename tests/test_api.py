
def test_api_settings(testapp):
    res = testapp.get('/api/v1/settings')
    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert res.json == {'hostname': 'spionisto', 'https_enabled': False}


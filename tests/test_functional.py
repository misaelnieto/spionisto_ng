def test_root(testapp):
    res = testapp.get('/', status=200)
    assert b'Pyramid' in res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404


def test_settings(testapp):
    res = testapp.get('/settings', status=200)
    assert """<input type="text" name="hostname" value="spionisto""" in res.text
    assert "https_enabled" in res.text

    res = testapp.post('/settings', {
            "hostname": "spionisto.new.hostname",
            "https_enabled": True,
            "submit": "submit"
        }, status=200
    )

    assert 'name="https_enabled" value="true"' in res.text
    assert 'name="hostname" value="spionisto.new.hostname"' in res.text


def test_agents(testapp):
    res = testapp.get('/agents', status=200)
    assert "No agents" in res.text

    res = testapp.post('/agents', {
            "name": "my_agent_1",
            "security_token": 'abc11234df',
            "submit": "submit"
        }, status=200
    )

    assert "1 agent" in res.text


    res = testapp.post('/agents', {
            "name": "my_agent_2",
            "security_token": 'abc11234df',
            "submit": "submit"
        }, status=200
    )

    assert "2 agents" in res.text

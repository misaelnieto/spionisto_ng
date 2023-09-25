from spionisto import models

def test_root_model():
    root = models.SpionistoRoot()
    assert root.__parent__ is None
    assert root.__name__ is None


def test_settings_model():
    settings = models.Settings()
    assert settings.hostname == 'spionisto'
    assert settings.https_enabled == False


def test_appmaker():
    root = {}
    models.appmaker(root)
    assert isinstance(root['app_root'], models.SpionistoRoot)
    settings = root['app_root']['settings']
    assert settings.hostname == 'spionisto'
    assert settings.https_enabled == False

import morepath
from ekklesia_portal.app import get_app_settings


def test_get_app_settings_default(monkeypatch):
    monkeypatch.delenv("EKKLESIA_PORTAL_CONFIG")
    settings = get_app_settings(None)
    assert "app" in settings
    assert "database" in settings
    assert settings["app"]["instance_name"] == "ekklesia_portal"


def test_get_app_settings(config_filepath):
    settings = get_app_settings(config_filepath)
    assert "app" in settings
    assert "database" in settings
    assert "test_section" in settings
    assert settings["app"]["instance_name"] == "test"
    assert settings["test_section"]["test_setting"] == "test"


def test_make_wsgi_app(app):
    assert isinstance(app, morepath.App)
    assert app.settings.test_section.test_setting == "test"
    assert app.settings.app.instance_name == "test"


def test_app_babel_config(app):
    assert app.babel.domain.dirname.endswith("/ekklesia_portal/translations")

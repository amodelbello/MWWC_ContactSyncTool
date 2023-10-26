import pytest
from mwwc_airtable import Airtable
from __init__ import create_app


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert b"The UI goes here." in response.data


@pytest.mark.skip(reason="not ready")
def test_sync_contacts(client, monkeypatch):
    data = "some data"

    def mockreturn(*args, **kwargs):
        return data

    monkeypatch.setattr(Airtable, "get_banana_data", mockreturn)
    request = client.get("/sync-contacts")
    assert bytes(data, "utf-8") in request.data


@pytest.mark.skip(reason="not ready")
def test_sync_contacts_airtable_exception(monkeypatch, client):
    error = "Something went wrong"

    def mockreturn(*args, **kwargs):
        raise Exception(error)

    monkeypatch.setattr(Airtable, "get_banana_data", mockreturn)
    response = client.get("/sync-contacts")
    assert bytes(error, "utf-8") in response.data

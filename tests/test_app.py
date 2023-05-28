import sys
import pytest
from mwwc_sync_contacts.external_services import airtable
from mwwc_sync_contacts.app import index, sync_contacts
from mwwc_sync_contacts import create_app

sys.path.append("..")


@pytest.fixture()
def app():
    app = create_app(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index():
    data = index()
    assert "The UI goes here." in data


def test_sync_contacts(client, monkeypatch):
    data = "{'some': 'data'}"

    def mockreturn(*args, **kwargs):
        return data

    monkeypatch.setattr(airtable, "get_banana_data", mockreturn)
    assert client.get("/sync_contacts") == data


def test_get_banana_data_exception(monkeypatch):
    error = "Something went wrong"

    def mockreturn(*args, **kwargs):
        raise Exception(error)

    monkeypatch.setattr(airtable, "get_banana_data", mockreturn)
    with pytest.raises(Exception, match=error):
        sync_contacts()

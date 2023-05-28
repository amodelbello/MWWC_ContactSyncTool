import sys
import pytest
from pyairtable import Table
from mwwc_sync_contacts.external_services.airtable import get_banana_data

sys.path.append("...")


def test_get_banana_data(monkeypatch):
    data = "{'some': 'data'}"

    def mockreturn(*args, **kwargs):
        return data

    monkeypatch.setattr(Table, "all", mockreturn)
    assert get_banana_data() == data


def test_get_banana_data_exception(monkeypatch):
    error = "Something went wrong"

    def mockreturn(*args, **kwargs):
        raise Exception(error)

    monkeypatch.setattr(Table, "all", mockreturn)
    with pytest.raises(Exception, match=error):
        get_banana_data()

import sys
import pytest
from pyairtable import Table
from mwwc_sync_contacts.airtable import Airtable

sys.path.append("...")

config_fixture = {
    "AIRTABLE_API_KEY": "api_key",
    "AIRTABLE_BASE_ID": "base_id",
    "AIRTABLE_TABLE_ID": "table_id",
    "AIRTABLE_VIEW_ID": "view_id",
    "AIRTABLE_CHOSEN_FIRST_NAME": "first_name",
    "AIRTABLE_CHOSEN_LAST_NAME": "last_name",
    "AIRTABLE_BU_STATUS": "bu_status",
    "AIRTABLE_AREA": "area",
    "AIRTABLE_MIGS": "MIGS?",
    "AIRTABLE_STEWARD": "steward",
    "AIRTABLE_ELECTED_POSITION": "elected_position",
    "AIRTABLE_PERSONAL_EMAIL": "personal_email",
}


def test_get_banana_data(monkeypatch):
    data = "{'some': 'data'}"

    def mockreturn(*args, **kwargs):
        return data

    monkeypatch.setattr(Table, "all", mockreturn)
    airtable = Airtable()
    airtable.get_banana_data(config_fixture)
    assert airtable.banana_data == data


def test_get_banana_data_exception(monkeypatch):
    error = "Something went wrong"

    def mockreturn(*args, **kwargs):
        raise Exception(error)

    monkeypatch.setattr(Table, "all", mockreturn)
    airtable = Airtable()
    with pytest.raises(Exception, match=error):
        airtable.get_banana_data(config_fixture)


# To mock:
# write_backup_file():
# open - to open file for writing, return mock file
# file.write
# file.close
# glob.glob to return backup filenames
# open - to open file for reading, return mock file
# file.read - return text
# file.close
def test_get_differences(monkeypatch):
    pass

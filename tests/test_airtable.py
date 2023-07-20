import sys
import os
import glob
import json
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


def test_get_differences_no_data():
    error = "Data from Airtable is missing"

    airtable = Airtable()
    with pytest.raises(Exception, match=error):
        airtable.get_differences()


def test_get_differences_no_backups(monkeypatch, airtable_data):
    def mock_listdir(bkp_dir):
        return ["one-file"]

    monkeypatch.setattr(os, "listdir", mock_listdir)

    def mock_write_backup_file(filename, data):
        return

    monkeypatch.setattr(Airtable, "write_backup_file", mock_write_backup_file)

    airtable = Airtable()
    airtable.banana_data = airtable_data

    differences = airtable.get_differences()

    # TODO: This will change when the logic is written
    assert differences is None


def test_get_no_differences_with_backup(monkeypatch, airtable_data):
    file_names = ["one-file", "two-files"]

    def mock_listdir(_):
        return file_names

    monkeypatch.setattr(os, "listdir", mock_listdir)

    def mock_glob(_):
        return file_names

    monkeypatch.setattr(glob, "glob", mock_glob)

    def mock_getctime(_):
        return lambda _: "key"

    monkeypatch.setattr(os.path, "getctime", mock_getctime("filename"))
    monkeypatch.setattr(
        Airtable, "read_backup_file", lambda _: json.dumps(airtable_data)
    )

    def mock_write_backup_file(filename, data):
        return

    monkeypatch.setattr(Airtable, "write_backup_file", mock_write_backup_file)

    airtable = Airtable()
    airtable.banana_data = airtable_data

    differences = airtable.get_differences()

    # TODO: This will change when the logic is written
    assert differences is None


def test_get_differences_with_deletion(
    monkeypatch, airtable_data, airtable_data_with_deletion
):
    old_file = "old_file"
    new_file = "new_file"
    file_names = [old_file, new_file]

    def mock_listdir(_):
        return file_names

    monkeypatch.setattr(os, "listdir", mock_listdir)

    def mock_glob(_):
        return file_names

    monkeypatch.setattr(glob, "glob", mock_glob)

    def mock_getctime(_):
        return lambda _: "key"

    monkeypatch.setattr(os.path, "getctime", mock_getctime("filename"))

    mock_files = {
        old_file: json.dumps(airtable_data),
        new_file: json.dumps(airtable_data_with_deletion),
    }

    def mock_read_backup_file(filename):
        print(filename)
        return mock_files.get(filename, {})

    monkeypatch.setattr(Airtable, "read_backup_file", mock_read_backup_file)

    def mock_write_backup_file(filename, data):
        return

    monkeypatch.setattr(Airtable, "write_backup_file", mock_write_backup_file)

    airtable = Airtable()
    airtable.banana_data = airtable_data_with_deletion

    differences = airtable.get_differences()

    assert differences is not None


def test_get_differences_with_addition(
    monkeypatch, airtable_data, airtable_data_with_addition
):
    old_file = "old_file"
    new_file = "new_file"
    file_names = [old_file, new_file]

    def mock_listdir(_):
        return file_names

    monkeypatch.setattr(os, "listdir", mock_listdir)

    def mock_glob(_):
        return file_names

    monkeypatch.setattr(glob, "glob", mock_glob)

    def mock_getctime(_):
        return lambda _: "key"

    monkeypatch.setattr(os.path, "getctime", mock_getctime("filename"))

    mock_files = {
        old_file: json.dumps(airtable_data),
        new_file: json.dumps(airtable_data_with_addition),
    }

    def mock_read_backup_file(filename):
        print(filename)
        return mock_files.get(filename, {})

    monkeypatch.setattr(Airtable, "read_backup_file", mock_read_backup_file)

    def mock_write_backup_file(filename, data):
        return

    monkeypatch.setattr(Airtable, "write_backup_file", mock_write_backup_file)

    airtable = Airtable()
    airtable.banana_data = airtable_data_with_addition

    differences = airtable.get_differences()

    assert differences is not None


def test_get_differences_with_change(
    monkeypatch, airtable_data, airtable_data_with_change
):
    old_file = "old_file"
    new_file = "new_file"
    file_names = [old_file, new_file]

    def mock_listdir(_):
        return file_names

    monkeypatch.setattr(os, "listdir", mock_listdir)

    def mock_glob(_):
        return file_names

    monkeypatch.setattr(glob, "glob", mock_glob)

    def mock_getctime(_):
        return lambda _: "key"

    monkeypatch.setattr(os.path, "getctime", mock_getctime("filename"))

    mock_files = {
        old_file: json.dumps(airtable_data),
        new_file: json.dumps(airtable_data_with_change),
    }

    def mock_read_backup_file(filename):
        print(filename)
        return mock_files.get(filename, {})

    monkeypatch.setattr(Airtable, "read_backup_file", mock_read_backup_file)

    def mock_write_backup_file(filename, data):
        return

    monkeypatch.setattr(Airtable, "write_backup_file", mock_write_backup_file)

    airtable = Airtable()
    airtable.banana_data = airtable_data_with_change

    differences = airtable.get_differences()

    assert differences is not None

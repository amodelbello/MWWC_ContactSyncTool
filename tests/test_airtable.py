import sys
import os
import glob
import json
import pytest
from pytest import MonkeyPatch
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


class TestAirtable:
    def setUp(self, old_file="old_file", new_file="new_file"):
        self.old_file = old_file
        self.new_file = new_file
        self.file_names = [old_file, new_file]
        self.mock_files = {}

        self.monkeypatch = MonkeyPatch()
        self.glob_func = glob.glob
        self.listdir_func = os.listdir
        self.getctime_func = os.path.getctime
        self.monkeypatch.setattr(glob, "glob", lambda _: self.file_names)
        self.monkeypatch.setattr(os, "listdir", lambda _: self.file_names)
        self.monkeypatch.setattr(os.path, "getctime", lambda _: "key")
        self.monkeypatch.setattr(Airtable, "write_backup_file", lambda f, d: None)
        self.monkeypatch.setattr(
            Airtable, "read_backup_file", lambda f: self.mock_files.get(f, {})
        )

    def tearDown(self):
        self.monkeypatch.setattr(glob, "glob", self.glob_func)
        self.monkeypatch.setattr(os, "listdir", self.listdir_func)
        self.monkeypatch.setattr(os.path, "getctime", self.getctime_func)

    def test_get_banana_data(self):
        self.setUp()
        data = "{'some': 'data'}"

        def mockreturn(*args, **kwargs):
            return data

        self.monkeypatch.setattr(Table, "all", mockreturn)
        airtable = Airtable()
        airtable.get_banana_data(config_fixture)
        assert airtable.banana_data == data
        self.tearDown()

    def test_get_banana_data_exception(self):
        self.setUp()
        error = "Something went wrong"

        def mockreturn(*args, **kwargs):
            raise Exception(error)

        self.monkeypatch.setattr(Table, "all", mockreturn)
        airtable = Airtable()
        with pytest.raises(Exception, match=error):
            airtable.get_banana_data(config_fixture)
        self.tearDown()

    def test_get_differences_no_data(self):
        self.setUp()
        error = "Data from Airtable is missing"

        airtable = Airtable()
        with pytest.raises(Exception, match=error):
            airtable.get_differences()
        self.tearDown()

    def test_get_differences_no_backups(self, airtable_data):
        self.setUp()
        self.file_names = ["one-file"]

        airtable = Airtable()
        airtable.banana_data = airtable_data

        differences = airtable.get_differences()

        # TODO: This will change when the logic is written
        assert differences is None
        self.tearDown()

    def test_get_no_differences_with_backup(self, airtable_data):
        self.setUp()
        self.monkeypatch.setattr(
            Airtable, "read_backup_file", lambda _: json.dumps(airtable_data)
        )

        airtable = Airtable()
        airtable.banana_data = airtable_data
        differences = airtable.get_differences()

        # TODO: This will change when the logic is written
        assert differences is None
        self.tearDown()

    def test_get_differences_with_deletion(
        self, airtable_data, airtable_data_with_deletion
    ):
        self.setUp()
        self.mock_files = {
            self.old_file: json.dumps(airtable_data),
            self.new_file: json.dumps(airtable_data_with_deletion),
        }

        airtable = Airtable()
        airtable.banana_data = airtable_data_with_deletion
        differences = airtable.get_differences()

        self.tearDown()
        assert len(differences["additions"]) == 1
        assert len(differences["deletions"]) == 0

    def test_get_differences_with_addition(
        self, airtable_data, airtable_data_with_addition
    ):
        self.setUp()
        self.mock_files = {
            self.old_file: json.dumps(airtable_data),
            self.new_file: json.dumps(airtable_data_with_addition),
        }

        airtable = Airtable()
        airtable.banana_data = airtable_data_with_addition
        differences = airtable.get_differences()

        self.tearDown()
        assert len(differences["additions"]) == 0
        assert len(differences["deletions"]) == 1

    def test_get_differences_with_change(
        self, airtable_data, airtable_data_with_change
    ):
        self.setUp()
        self.mock_files = {
            self.old_file: json.dumps(airtable_data),
            self.new_file: json.dumps(airtable_data_with_change),
        }

        airtable = Airtable()
        airtable.banana_data = airtable_data_with_change
        differences = airtable.get_differences()

        self.tearDown()
        assert len(differences["additions"]) == 1
        assert len(differences["deletions"]) == 1

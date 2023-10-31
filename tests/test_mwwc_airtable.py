import pytest
from unittest.mock import patch
from mwwc_airtable import Airtable


class TestAirtable:
    @patch('pyairtable.Table.all')
    def test_get_banana_data_okay(
            self,
            mock_table_all,
            airtable_config_data,
            airtable_data
    ):
        mock_table_all.side_effect = [airtable_data]
        airtable = Airtable(airtable_config_data)
        airtable.get_banana_data()
        assert airtable.banana_data == airtable_data

    @patch('pyairtable.Table.all')
    def test_get_banana_data_exception(self, mock_table_all, airtable_config_data):
        error = "Something went wrong"
        mock_table_all.side_effect = Exception(error)
        airtable = Airtable(airtable_config_data)
        with pytest.raises(Exception, match=error):
            airtable.get_banana_data()

    @patch('pyairtable.Table.all')
    def test_get_banana_data_validate(self, mock_table_all, airtable_config_data):
        error = "json returned from airtable is invalid"
        mock_table_all.side_effect = "this is not okay"
        airtable = Airtable(airtable_config_data)
        with pytest.raises(Exception, match=error):
            airtable.get_banana_data()

    def test_get_differences_no_data(self, airtable_config_data):
        error = "Data from Airtable is missing"

        airtable = Airtable(airtable_config_data)
        with pytest.raises(Exception, match=error):
            airtable.get_differences()

    def test_get_differences_no_backups(
            self,
            tmp_path,
            airtable_config_data,
            airtable_data
    ):
        airtable_config_data["AIRTABLE_BACKUP_DIR"] = tmp_path
        airtable = Airtable(airtable_config_data)
        airtable.banana_data = airtable_data

        differences = airtable.get_differences()

        # TODO: This will change when the logic is written
        assert differences is None

    def test_get_no_differences_with_backup(
            self,
            tmp_path,
            create_airtable_files,
            airtable_config_data,
            airtable_data,
    ):
        create_airtable_files(["2023-2-26 01:28:03.097417.json",
                               "2023-10-27 01:28:03.097417.json"])

        airtable_config_data["AIRTABLE_BACKUP_DIR"] = tmp_path
        airtable = Airtable(airtable_config_data)
        airtable.banana_data = airtable_data
        differences = airtable.get_differences()

        # TODO: This will change when the logic is written
        assert differences is None

    def test_get_differences_with_deletion(
            self,
            tmp_path,
            create_airtable_files,
            airtable_config_data,
            airtable_data,
            airtable_data_with_deletion,
    ):
        create_airtable_files(["2023-10-26 01:28:03.097417.json",
                               "2023-10-27 01:28:03.097417.json"])

        airtable_config_data["AIRTABLE_BACKUP_DIR"] = tmp_path
        airtable = Airtable(airtable_config_data)
        airtable.banana_data = airtable_data_with_deletion

        differences = airtable.get_differences()

        assert len(differences["additions"]) == 0
        assert len(differences["deletions"]) == 1

    def test_get_differences_with_addition(
            self,
            tmp_path,
            create_airtable_files,
            airtable_config_data,
            airtable_data,
            airtable_data_with_addition,
    ):
        create_airtable_files(["2023-10-26 01:28:03.097417.json",
                               "2023-10-27 01:28:03.097417.json"])

        airtable_config_data["AIRTABLE_BACKUP_DIR"] = tmp_path
        airtable = Airtable(airtable_config_data)
        airtable.banana_data = airtable_data_with_addition
        differences = airtable.get_differences()

        assert len(differences["additions"]) == 1
        assert len(differences["deletions"]) == 0

    def test_get_differences_with_change(
            self,
            tmp_path,
            create_airtable_files,
            airtable_config_data,
            airtable_data,
            airtable_data_with_change,
    ):
        create_airtable_files(["2023-10-26 01:28:03.097417.json",
                               "2023-10-27 01:28:03.097417.json"])

        airtable_config_data["AIRTABLE_BACKUP_DIR"] = tmp_path
        airtable = Airtable(airtable_config_data)
        airtable.banana_data = airtable_data_with_change
        differences = airtable.get_differences()

        assert len(differences["additions"]) == 1
        assert len(differences["deletions"]) == 1

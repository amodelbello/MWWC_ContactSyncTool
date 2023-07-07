import os
import json
import glob
from pathlib import Path
from datetime import datetime
from pyairtable import Table

BACKUP_DIR = f"{Path(__file__).parent}/airtable_backups"


class Airtable:
    has_differences = False

    # Latest data from Airtable
    banana_data = None

    # Newest backup file
    new_banana_data = {}

    # Second newest backup file
    old_banana_data = {}

    def get_banana_data(self, c):
        fields = [
            c["AIRTABLE_CHOSEN_FIRST_NAME"],
            c["AIRTABLE_CHOSEN_LAST_NAME"],
            c["AIRTABLE_BU_STATUS"],
            c["AIRTABLE_AREA"],
            c["AIRTABLE_MIGS"],
            c["AIRTABLE_STEWARD"],
            c["AIRTABLE_ELECTED_POSITION"],
            c["AIRTABLE_PERSONAL_EMAIL"],
        ]

        banana_table = Table(
            c["AIRTABLE_API_KEY"],
            c["AIRTABLE_BASE_ID"],
            c["AIRTABLE_TABLE_ID"],
        )
        self.banana_data = banana_table.all(view=c["AIRTABLE_VIEW_ID"], fields=fields)

    @classmethod
    def write_backup_file(cls, new_filename, file_contents):
        file = open(new_filename, "w")
        file.write(file_contents)
        file.close()

    @classmethod
    def read_backup_file(cls, backup_filename):
        file = open(backup_filename, "r")
        text = file.read()
        file.close()
        return text

    @classmethod
    def banana_list_to_dict(cls, list_data):
        dict_data = {}
        for i in list_data:
            dict_data[i["id"]] = i
        return dict_data

    def get_differences(self):
        if self.banana_data is None:
            raise ValueError(
                "Data from Airtable is missing. You must call get_banana_data() first."
            )

        self._write_latest_banana_data_to_file()
        if not self.has_differences:
            print("There are no updates to Airtable.")
            # return

        filenames_sorted_desc = sorted(
            glob.glob(BACKUP_DIR + "/*"), key=os.path.getctime, reverse=True
        )
        new_filename = filenames_sorted_desc[0]
        new_data = Airtable.banana_list_to_dict(
            json.loads(Airtable.read_backup_file(new_filename))
        )

        old_filename = filenames_sorted_desc[1]
        backup_data = Airtable.banana_list_to_dict(
            json.loads(Airtable.read_backup_file(old_filename))
        )

        return backup_data

    def _write_latest_banana_data_to_file(self):
        new_filename = f"{BACKUP_DIR}/{datetime.utcnow()}.json"
        file_text = json.dumps(self.banana_data)

        if len(os.listdir(BACKUP_DIR)) == 1:  # The .keep file will be in there
            Airtable.write_backup_file(new_filename, file_text)
        else:
            latest_backup_filename = max(
                glob.glob(BACKUP_DIR + "/*"), key=os.path.getctime
            )
            latest_backup_text = Airtable.read_backup_file(latest_backup_filename)

            if latest_backup_text != file_text:
                self.has_differences = True
                Airtable.write_backup_file(new_filename, file_text)

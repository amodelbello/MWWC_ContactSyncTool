import os
import json
import glob
from pathlib import Path
from datetime import datetime
from pyairtable import Table
from jsonschema import validate

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
            c["AIRTABLE_GOOGLE_WRITE_PERMISSIONS"],
            c["AIRTABLE_NON_BU_ASSOCIATE"],
        ]

        banana_table = Table(
            c["AIRTABLE_API_KEY"],
            c["AIRTABLE_BASE_ID"],
            c["AIRTABLE_TABLE_ID"],
        )

        try:
            self.banana_data = banana_table.all(
                view=c["AIRTABLE_VIEW_ID"], fields=fields
            )
        except Exception as e:
            raise ValueError(f"Error getting data from airtable: {e}")

        try:
            self.validate_airtable_response()
        except Exception as e:
            raise ValueError(f"json returned from airtable is invalid: {e}")

    def validate_airtable_response(self):
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "createdTime": {"type": "string"},
                        "fields": {
                            "type": "object",
                            "properties": {
                                "Area": {"type": "string"},
                                "BU Status": {"type": "string"},
                                "Chosen First Name": {"type": "string"},
                                "Chosen Last Name": {"type": "string"},
                                "MIGS?": {"type": "string"},
                                "Personal Email": {"type": "string"},
                                "Steward": {"type": "boolean"},
                                "Elected Position": {"type": "string"},
                            },
                        },
                        "id": {"type": "string"},
                    },
                    "required": ["createdTime", "fields", "id"],
                }
            ],
        }

        validate(instance=self.banana_data, schema=schema)

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
            """
            TODO: If there is only a single airtable backup
            it means that we need to delete all data in
            google & action network and add the data from the file,
            because this is the first run of the software.
            We need to be VERY careful with this step.
            """
            print("There are no updates to Airtable.")
            return None

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

        return self._calc_differences(new_data, backup_data)

    def _write_latest_banana_data_to_file(self):
        new_filename = f"{BACKUP_DIR}/{datetime.utcnow()}.json"
        file_text = json.dumps(self.banana_data)

        if len(os.listdir(BACKUP_DIR)) < 2:  # The .keep file will be in there
            Airtable.write_backup_file(new_filename, file_text)
        else:
            latest_backup_filename = max(
                glob.glob(BACKUP_DIR + "/*"), key=os.path.getctime
            )
            latest_backup_text = Airtable.read_backup_file(latest_backup_filename)

            if latest_backup_text != file_text:
                self.has_differences = True
                Airtable.write_backup_file(new_filename, file_text)

    def _calc_differences(self, new_data, old_data):
        additions = []
        deletions = []

        for key, value in old_data.items():
            if key not in new_data.keys():
                deletions.append(old_data[key])

        for key, value in new_data.items():
            if key not in old_data.keys():
                additions.append(new_data[key])
            elif new_data[key] != old_data[key]:
                additions.append(new_data[key])
                deletions.append(old_data[key])

        return {
            "additions": additions,
            "deletions": deletions,
        }

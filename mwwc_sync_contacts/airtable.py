import os
import json
import glob
from pathlib import Path
from datetime import datetime
from pyairtable import Table

BACKUP_DIR = f"{Path(__file__).parent}/airtable_backups"


def get_banana_data(c):
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
    return banana_table.all(view=c["AIRTABLE_VIEW_ID"], fields=fields)


def write_backup_file(new_filename, file_contents):
    file = open(new_filename, "w")
    file.write(file_contents)
    file.close()


def read_backup_file(backup_filename):
    file = open(backup_filename, "r")
    text = file.read()
    file.close()
    return text


def write_latest_banana_data_to_file(banana_data):
    new_filename = f"{BACKUP_DIR}/{datetime.utcnow()}.json"
    file_text = json.dumps(banana_data)

    if len(os.listdir(BACKUP_DIR)) == 1:  # The .keep file will be in there
        print("It's empty")
        write_backup_file(new_filename, file_text)
    else:
        print("It's NOT empty")
        latest_backup_filename = max(glob.glob(BACKUP_DIR + "/*"), key=os.path.getctime)
        latest_backup_text = read_backup_file(latest_backup_filename)

        # def ordered(obj):
        #     if isinstance(obj, dict):
        #         return sorted((k, ordered(v)) for k, v in obj.items())
        #     if isinstance(obj, list):
        #         return sorted(ordered(x) for x in obj)
        #     else:
        #         return obj

        if latest_backup_text != file_text:
            print("The files are NOT equal")
            write_backup_file(new_filename, file_text)
        else:
            print("The files are equal")

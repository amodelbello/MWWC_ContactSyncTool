import os
import sys
from dotenv import load_dotenv
from pyairtable import Table

sys.path.append("...")
load_dotenv()

api_key = os.environ["AIRTABLE_API_KEY"]
base_id = os.environ["AIRTABLE_BASE"]
table_id = os.environ["AIRTABLE_TABLE"]


def get_banana_data():
    banana_table = Table(api_key, base_id, table_id)
    return banana_table.all()
